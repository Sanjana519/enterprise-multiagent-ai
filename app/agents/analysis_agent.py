from .base_agent import BaseAgent


class AnalysisAgent(BaseAgent):

    async def run(self, research_data):
        response = await self.llm.invoke(
            f"Analyze this research and extract key insights:\n{research_data}"
        )
        return response.content