import os
from dotenv import load_dotenv
from fastapi import FastAPI
from groq import Groq

from app.agents.research_agent import ResearchAgent
from app.agents.analysis_agent import AnalysisAgent
from app.agents.validation_agent import ValidationAgent
from app.agents.summary_agent import SummaryAgent
from app.orchestrator import Orchestrator

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not set")

client = Groq(api_key=GROQ_API_KEY)


class GroqWrapper:
    async def invoke(self, prompt):
        completion = client.chat.completions.create(
          model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
        )
        content = completion.choices[0].message.content
        return type("Obj", (), {"content": content})


llm = GroqWrapper()

research_agent = ResearchAgent(llm)
analysis_agent = AnalysisAgent(llm)
validation_agent = ValidationAgent(llm)
summary_agent = SummaryAgent(llm)

orchestrator = Orchestrator(
    research_agent,
    analysis_agent,
    validation_agent,
    summary_agent
)

app = FastAPI(title="Enterprise 4-Agent AI with Groq")


@app.post("/process")
async def process(query: str):
    result = await orchestrator.execute(query)
    return result

