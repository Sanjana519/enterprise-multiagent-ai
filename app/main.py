from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from dotenv import load_dotenv
load_dotenv()

from app.orchestrator import Orchestrator, GroqWrapper
from app.agents.research_agent import ResearchAgent
from app.agents.analysis_agent import AnalysisAgent
from app.agents.summary_agent import SummaryAgent
from app.agents.validation_agent import ValidationAgent


app = FastAPI(
    title="Enterprise Multi-Agent AI",
    version="1.0.0"
)


# Create LLM
llm = GroqWrapper()

# Create Agents
research_agent = ResearchAgent(llm)
analysis_agent = AnalysisAgent(llm)
summary_agent = SummaryAgent(llm)
validation_agent = ValidationAgent(llm)

# Create Orchestrator
orchestrator = Orchestrator(
    research=research_agent,
    analysis=analysis_agent,
    summary=summary_agent,
    validation=validation_agent
)


@app.post("/process")
async def process(query: str = Query(...)):
    result = await orchestrator.run(query)
    return JSONResponse(content=result)


app.mount("/", StaticFiles(directory="static", html=True), name="static")