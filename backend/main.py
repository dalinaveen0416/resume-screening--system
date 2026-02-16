from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import shutil
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from backend.utils import extract_text
from backend.embeddings import EmbeddingService
from backend.llm_evaluator import LLMEvaluator
from backend.ranking import RankingService
from backend.config import UPLOAD_DIR


app = FastAPI(title="AI Resume Screening System")

embedding = EmbeddingService()
llm_eval = LLMEvaluator()
ranker = RankingService()


class JobRequest(BaseModel):
    job_description: str

@app.get("/")
def health():
    return {
        'status': 'Resume Screening System running'
    }

@app.post("/upload_resume")
async def upload_resume(file: UploadFile= File(...)):
    file_path = os.path.join(UPLOAD_DIR,file.filename)

    with open(file_path,'wb') as buffer:
        shutil.copyfileobj(file.file,buffer)

    return {
        'message':f'{file.filename} uploaded successfully'
    }

@app.post('/evaluate_resume')
async def evaluate_resume(jd: JobRequest):

    evaluations =[]

    for file in os.listdir(UPLOAD_DIR):
        path =os.path.join(UPLOAD_DIR,file)
        text = extract_text(path)

        analysis =llm_eval.evaluate(text,jd.job_description)

        evaluations.append({
            'resume':file,
            'analysis':analysis
        })

        return {'evaluations':evaluations}
    
@app.post('/rank')
async def rank_resumes(jd: JobRequest):

    jd_vec =embedding.get_embedding(jd.job_description)

    results =[]

    for file in os.listdir(UPLOAD_DIR):
        path =os.path.join(UPLOAD_DIR,file)
        text = extract_text(path)
        resume_vec = embedding.get_embedding(text)

        score = ranker.compute_score(resume_vec,jd_vec)

        results.append({
            'resume':file,
            'score':round(float(score),2),
            'status':'Shortlist' if score > 0.7 else 'Reject'
        })

    results.sort(key=lambda x:x['score'],reverse=True)

    return {'rankings':results}
