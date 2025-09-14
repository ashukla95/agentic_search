from agents import (
    Agent
)

from module.constants import (
    DEFAULT_LLM
)
from module.agents.web_search import (
    web_search_agent
)


RESEARCH_AGENT_INSTRUCTIONS = f"""
You are an agent who will be receiving a topic to research.
The topic may be accompanied by some clarifications to help
you define a research path. 
Your task is to call the tools provided to you 
and provide concise details about the topic to be researched. 
The return type should not be of markdown type.
Kindly do not write anything yourself. Use tools at disposal
to get the job done.
Kindly ensure that redundant information is removed and thus
a concise detail is generated.
"""


# BEWARE! THIS WILL GENERATE N INPUT QUERY X M SEARCH LIST PER QUERY
# IF YOU WANT TO CONTROL THIS BEHAVIOUR, USE THE PLANNER TOOL AS A 
# TOOL HERE AND CONTROL THE OVERALL SEARCH TOPICS.
# OR ANOTHER WAY IS TO ORCHESTRATE THIS VIA A RUNNER CLASS.
# PERKS OF TOO MUCH AUTONOMY!!
research_agent = Agent(
    name="Research Agent",
    model=DEFAULT_LLM,
    instructions=RESEARCH_AGENT_INSTRUCTIONS,
    tools=[
        web_search_agent.as_tool(
            tool_name="web_search_agent",
            tool_description="web search agent tool"
        )
    ]
)