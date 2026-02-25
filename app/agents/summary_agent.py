from .base_agent import BaseAgent


class SummaryAgent(BaseAgent):

    async def run(self, validated_data):
        response = await self.llm.invoke(
            f"Provide a professional executive summary:\n{validated_data}"
        )
        return response.content