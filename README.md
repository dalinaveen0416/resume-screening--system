# Intelligent AI Resume Screening System

## Overview

The Intelligent AI Resume Screening System is an end-to-end Generative AI application that helps recruiters automatically evaluate and rank resumes based on a given job description.

Instead of manually reviewing each resume, this system uses **embeddings, semantic similarity, and LLM-based evaluation** to identify the most relevant candidates and generate detailed hiring insights.

This project demonstrates how modern AI can be applied to solve real-world recruitment problems using Python, FastAPI, LangChain, Hugging Face embeddings, and Groq LLM.

---

## Key Features

* Upload and process PDF resumes
* Semantic similarity matching using embeddings
* Resume ranking based on job description relevance
* LLM-based candidate evaluation (Strengths, Gaps, Recommendation)
* Automatic shortlist / reject classification
* FastAPI backend with REST endpoints
* Streamlit frontend for recruiter-friendly UI
* Modular, scalable, and production-ready structure
* API test support and evaluation pipeline

---

## How It Works

The system follows this pipeline:

1. Recruiter uploads resumes
2. Recruiter enters a job description
3. System converts resumes and job description into embeddings
4. Cosine similarity is calculated
5. Resumes are ranked based on similarity score
6. Groq LLM evaluates each resume and generates hiring insights
7. UI displays ranking, scores, and recommendations

---

## Project Structure

```
Intelligent-Resume-Screening-System/
│
├── backend/
│   ├── main.py
│   ├── embeddings.py
│   ├── ranking.py
│   ├── llm_evaluator.py
│   ├── utils.py
│   └── config.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── resumes/
│
├── tests/
│   └── test_api.py
│
├── eval/
│   ├── eval_data.json
│   └── evaluate.py
│
├── requirements.txt
└── README.md
```

---

## Tech Stack

**Programming Language**

* Python

**Backend**

* FastAPI

**Frontend**

* Streamlit

**AI / GenAI**

* LangChain
* Hugging Face Embeddings
* Groq LLM

**ML / Data**

* Scikit-learn
* Cosine Similarity

**Other**

* PyPDF
* Requests
* Pytest

---

## Installation

### 1. Clone Repository

```
git clone https://github.com/your-username/intelligent-resume-screening-system.git

cd intelligent-resume-screening-system
```

---

### 2. Create Virtual Environment

```
python -m venv env
```

Activate environment:

Windows:

```
env\Scripts\activate
```

Mac/Linux:

```
source env/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Set Groq API Key

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## 🚀 Running the Application

### Start Backend

```
python -m uvicorn backend.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

### Start Frontend

Open new terminal:

```
streamlit run frontend/app.py
```

Frontend runs on:

```
http://localhost:8501
```

---

## API Endpoints

### Upload Resume

```
POST /upload_resume
```

---

### Rank Resumes

```
POST /rank
```

Input:

```
{
  "job_description": "Python developer with SQL skills"
}
```

---

### Evaluate Resume

```
POST /evaluate_resume
```

---

## Running Tests

```
pytest tests/
```

---

## Example Output

Ranking:

```
Resume: Naveen_data_analyst_CV.pdf
Score: 0.82
Status: Shortlisted
```

Evaluation:

```
Strengths:
Strong SQL and Python skills

Skill Gap:
No Tableau experience

Recommendation:
Shortlist
```

---

## Real-World Use Case

This system can be used by:

* HR teams
* Recruiters
* Hiring managers
* Talent acquisition platforms

To automate and improve hiring efficiency.

---

## Skills Demonstrated

This project demonstrates:

* Generative AI integration
* RAG-style semantic search
* FastAPI backend development
* Streamlit frontend development
* LLM prompt engineering
* Embedding-based similarity matching
* API design and testing
* End-to-end AI application deployment

---

##  Future Improvements

Possible enhancements:

* Skill extraction scoring
* Analytics dashboard
* Resume parsing into structured format
* Multi-job comparison
* Deployment on cloud (AWS / Render)
* Authentication system

---

## Author

**Naveen Dali**

Python Developer | Generative AI Engineer

---

## Conclusion

This project showcases how AI can automate resume screening and help recruiters make faster, smarter, and more accurate hiring decisions.

It reflects real-world AI engineering skills including backend development, LLM integration, and full-stack AI application design.

---

