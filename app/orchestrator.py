from groq import Groq
import os


# =========================================
# LLM Wrapper
# =========================================
class GroqWrapper:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not set in environment.")

        self.client = Groq(api_key=api_key)

    async def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
           model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content


# =========================================
# Orchestrator
# =========================================
class Orchestrator:
    def __init__(self, research, analysis, summary, validation):
        self.research = research
        self.analysis = analysis
        self.summary = summary
        self.validation = validation

    async def run(self, query: str) -> dict:

        research_output = await self.research.run(query)

        analysis_output = await self.analysis.run(research_output)

        summary_output = await self.summary.run(analysis_output)

        validation_output = await self.validation.run(summary_output)

        return {
            "research": research_output,
            "analysis": analysis_output,
            "summary": summary_output,
            "validation": validation_output
        }