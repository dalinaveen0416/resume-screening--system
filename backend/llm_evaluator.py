from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

class LLMEvaluator:

    def __init__(self):

        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.1-8b-instant",
            temperature=0
        )
        self.prompt = ChatPromptTemplate.from_template(

            """
            You are an HR AI assistant.

            Your expert in resume screening.
            Evaluate the candidate resume against job description.

            Don't halucinate. Be objective and precise.

            Resume:{resume}
            Job Description:{jd}

            give :
            -Strengths
            -skills match
            -skills gaps
            -final recommendation (shortlist/reject)
            """
        )

    def evaluate(self,resume,jd):

        chain = self.prompt | self.llm

        response = chain.invoke(
            {
                'resume':resume,
                'jd':jd
            }
        )

        return response.content