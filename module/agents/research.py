from agents import (
    Agent
)

from module.constants import (
    DEFAULT_LLM
)
from module.agents.web_search import (
    web_search_agent,
    web_search_planner_agent,
    web_search_plan_trimmer_agent

)
from module.agents.report import (
    report_generator_agent
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
use report_generator agent to help get the report curated 
and hence just work as the main orchestrator.

KINDLY USE THE WEB SEARCH PLANNER TOOL 
(web_search_plan_list_generator) TO GENERATE A LIST
OF DETAILS TO BE SEARCHED. dO nOT, I REPEAT, dO nOT SKIP
THIS TOOL OR COME UP WITH YOUR OWN SEARCH LIST.
aLSO, KINDLY COLLATE ALL THE QUERIES FROM THE WEB SEARCH PLAN
LIST GENERATOR TOOL FIRST, MAKE SURE TO DE-DUPLICATE THE
QUERIES using web_search_plan_trimmer took 
AND LASTLY CURATE A FINAL LIST OF DISTINCT DETAILS
TO BE SEARCHED. I DONT WANT YOU TO REPEAT THE SAME SEARCH
AGAIN AND AGAIN.
WHEN RETRIEVING OUTPUTS, IF YOU SEE SAME CONTENT REPEATED
MORE THAN ONCE, STOP THE SEARCH AND DIRECTLY CALL THE 
REPORT GENERATOR AGENT TO DO THE FINAL WORK.
YOU HAVE SEARCHES TO DO LET THE CLERICAL WORK FOR YOU
BE HANDLED BY THE AGENT ASSIGNED.
PASS IN THE INSTRUCTIONS YOU RECEIVE AS IS THE PLANNER
AGENT AND LET IT COME UP WITH THE DETAILS YOU NEED
FOR THE SEARCH.
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
         web_search_planner_agent.as_tool(
            tool_name="web_search_plan_list_generator",
            tool_description="an agent to generate a list of queries to be searched on the web for details"
        ),
        web_search_plan_trimmer_agent.as_tool(
            tool_name="web_search_plan_trimmer",
            tool_description="agent to ensure only distinct topics are being searched."
        ),
        web_search_agent.as_tool(
            tool_name="web_search_agent",
            tool_description="web search agent tool"
        ),
        report_generator_agent.as_tool(
            tool_name="report_generator",
            tool_description="agent to curate final report"
        )
    ]
)