from app.agents.base_agent import BaseAgent


class AnalysisAgent(BaseAgent):
    async def run(self, input_data):

        prompt = f"""
        Analyze the following research output:

        {input_data}

        Provide:
        - Deep reasoning
        - Patterns
        - Critical evaluation
        """

        return await self.llm.generate(prompt)