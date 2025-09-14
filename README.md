# Deep Research 

Tried OpenAI SDK based agents to perform Deep Research.
Has two modes of working:
1) With followup queries to make a concise search.
2) Direct search

To limit the token usage given the experimental ideation, I have limited the search to three topics only.
Has input guardrail implemented if followup queries are posted. If directly searched, no guardrails exist.
It uses agents as tools and not handoffs as I wanted to implement a decent orchestrator and for some reason,
I would prefer to use airflow type orchestrator with permanent storage rather than handoff to make things
really idempotent.
Uses Gradio to allow interactions.
I could have deployed it to huggingface but fear misuse and hence is restricted to repo only for now.
Feel free to use it and cite if it helps even for a bit.
To run it:
1) Make sure python is installed on the system
2) Create a venv
3) Activate the venv
4) Clone the repo.
5) Once inside the repo locally, run pip3 install -r requirements.txt . If using other package manager run required commands.
6) Since I am using uv, the final command to run the app is: uv run deep_research_runner.py


One thing to call out is the fact that I would say after developing this that 
non-sentient orchestration is necessary to control the side-effects of using agents.