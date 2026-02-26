from app.agents.base_agent import BaseAgent


class SummaryAgent(BaseAgent):
    async def run(self, input_data):

        prompt = f"""
        Summarize the following analysis clearly and concisely:

        {input_data}

        Provide a structured summary.
        """

        return await self.llm.generate(prompt)
        