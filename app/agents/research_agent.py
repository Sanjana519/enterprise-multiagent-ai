from app.agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    async def run(self, input_data):

        prompt = f"""
        Conduct structured research on:
        {input_data}

        Provide:
        - Key concepts
        - Important insights
        - Relevant examples
        """

        return await self.llm.generate(prompt)