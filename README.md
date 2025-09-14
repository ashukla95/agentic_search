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

