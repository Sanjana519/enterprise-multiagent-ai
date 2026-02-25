class Orchestrator:

    def __init__(self, research, analysis, validation, summary):
        self.research = research
        self.analysis = analysis
        self.validation = validation
        self.summary = summary

    async def execute(self, query):
        research_output = await self.research.run(query)
        analysis_output = await self.analysis.run(research_output)
        validated_output = await self.validation.run(analysis_output)
        summary_output = await self.summary.run(validated_output)

        return {
            "research": research_output,
            "analysis": analysis_output,
            "validated": validated_output,
            "summary": summary_output
        }