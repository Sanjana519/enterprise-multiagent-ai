from .base_agent import BaseAgent


class ResearchAgent(BaseAgent):

    async def run(self, query):
        response = await self.llm.invoke(
            f"Research deeply about: {query}"
        )
        return response.content