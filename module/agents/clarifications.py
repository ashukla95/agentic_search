from agents import (
    Agent
)
from pydantic import (
    BaseModel,
    Field
)

from module.constants import (
    DEFAULT_LLM,
    DEFAULT_CLARIFICATIONS_TO_ASK
)


class QueryList(BaseModel):
    questions: list[str] = Field(
        "List of clarification queries."
    )


AGENT_INSTRUCTION = (
    "You are a query clarification expert. "
    "What does it mean? "
    "You will be presented with a query for which research "
    "is to be done. You task is to come up with "
    f"{DEFAULT_CLARIFICATIONS_TO_ASK} to ensure that research "
    "happens on the concise context to the largest extent "
    "possible. "
    "An example is, let's say someone says, give me detail on "
    "stock market. A few clarifications could be: "
    "1) Do you have a specific stock in mind? "
    "2) Do you want details of a specific time or a time range? "
    "3) What exact details do you seek? "
    "Ensure that plain text is returned and no markdowns. "
    "Make sure to return questions only and nothing else. "
)


clarification_agent = Agent(
    name="Clarifications",
    instructions=AGENT_INSTRUCTION,
    model=DEFAULT_LLM,
    output_type=QueryList
)