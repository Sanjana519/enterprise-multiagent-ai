from .base_agent import BaseAgent


class ValidationAgent(BaseAgent):

    async def run(self, analysis_data):
        response = await self.llm.invoke(
            f"Validate and improve the following content:\n{analysis_data}"
        )
        return response.content