from app.agents.base_agent import BaseAgent


class ValidationAgent(BaseAgent):
    async def run(self, input_data):

        prompt = f"""
        Validate and refine the following summary:

        {input_data}

        Ensure:
        - Clarity
        - Logical consistency
        - Professional tone
        """

        return await self.llm.generate(prompt)