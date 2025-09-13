"""
Author: Aishwary Shukla
Details: Trying to mess with Deep Search.
There are some structiral hard codings which
I will remove if I feel like doing it ;p
"""
from agents import (
    Runner,
    trace
)
from agents.exceptions import (
    InputGuardrailTripwireTriggered
)
from dotenv import load_dotenv
from gradio import (
    Blocks,
    Button,
    Markdown,
    Textbox,
    Column,
    Row
)
from gradio.themes import (
    Default
)

from module.agents.clarifications import (
    clarification_agent
)

import gradio as gr
from traceback import print_exc


# load env variables once
load_dotenv(
    override=True
)



# declare run
async def generate_followups(
    query: str
):
    try:
        with trace("clarifications"):
            result = await Runner.run(
                clarification_agent,
                query
            )
            print(f"result: {result}")
            print(f"result type: {type(result)}")
            result = result.final_output
            yield [
                query,
                gr.update(visible=True, interactive=True),
                gr.update(visible=True, interactive=True),
                gr.update(visible=True, interactive=True),
                gr.update(visible=True, value=f"{result.questions[0]}"),
                gr.update(visible=True, value=f"{result.questions[1]}"),
                gr.update(visible=True, value=f"{result.questions[2]}"),
                gr.update(visible=False),
                gr.update(visible=False),
            ]
    except (InputGuardrailTripwireTriggered) as e:
        print(f"Exception: {e}")
        print(f"Exception traceback: {print_exc()}")
        yield [
                query,
                gr.update(visible=False),
                gr.update(visible=False),
                gr.update(visible=False),
                gr.update(visible=False),
                gr.update(visible=False),
                gr.update(visible=False),
                gr.update(visible=True),
                gr.update(visible=True, value=f"Input is not acceptable: {e}."),
            ]


async def run(
    query: str, 
    question_1: str, answer_1: str, 
    question_2: str, answer_2: str, 
    question_3: str, answer_3: str
):
    print(
        f"Final details: {query}, {question_1}, {answer_1}, {question_2}, {answer_2}, {question_3}, {answer_3}"
    )
    yield "complete"


with Blocks(
    theme=Default(
        primary_hue="sky"
    )
) as ui:
    
    # UI Elements
    Markdown("# My experiments with Deep Search.")
    main_query = Textbox(
        label = "Give me a topic to search"
    )
    with Column():
        with Row():
            # question_1 = Textbox(label="Q_1", visible=False)
            question_1 = Markdown(value="Q_1", visible=False)
            answer_1 = Textbox(label="Answer", visible=False)
        with Row():
            question_2 = Markdown(value="Q_2", visible=False)
            # question_2 = Textbox(label="Q_2", visible=False)
            answer_2 = Textbox(label="Answer", visible=False)
        with Row():
            question_3 = Markdown(value="Q_3", visible=False)
            # question_3 = Textbox(label="Q_3", visible=False)
            answer_3 = Textbox(label="Answer", visible=False)
    followup_button = Button(
        "Generate Followup queries.",
        variant="primary"
    )
    run_button = Button(
        "Run Search",
        variant="primary"
    )
    report = Markdown(
        label="Report"
    )

    # Actions
    followup_button.click(
        fn=generate_followups,
        inputs=[main_query],
        outputs=[
            main_query, 
            answer_1, answer_2, answer_3, 
            question_1, question_2, question_3, 
            followup_button, report
        ]
    )
    run_button.click(
        fn=run, 
        inputs=[
            main_query, 
            question_1, answer_1, 
            question_2, answer_2, 
            question_3, answer_3
        ],
        outputs=[report]
    )


# Start workflow
ui.launch(inbrowser=True)


# give me details about AAPL stock