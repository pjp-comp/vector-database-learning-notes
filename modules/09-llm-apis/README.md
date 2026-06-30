# Module 09 — Calling LLM APIs (Claude)

> Guide module. Needs a real API key, so there's no no-key demo here — this
> explains *what to learn and why*, with the smallest possible first step.

So far every "LLM" in this repo has been a **labeled fake** (modules 04b, 06, 07,
both PDF demos) so things run with no key. This module replaces that fake with a
real call. That single swap turns your retrieval pipeline into real RAG.

## Use the latest Claude models
Default to the most capable current models — the **Claude 4.x family**:
- **Opus 4.8** (`claude-opus-4-8`) — most capable.
- **Sonnet 4.6** (`claude-sonnet-4-6`) — strong balance of quality/speed/cost.
- **Haiku 4.5** (`claude-haiku-4-5-20251001`) — fastest/cheapest.

Don't hardcode old model names from memory — check the current list when you build.

## What to learn (in order)
1. **A basic message call** — system prompt + user message → response.
2. **Prompting** — clear instructions, examples, telling it what *not* to do.
3. **Structured output** — get back JSON you can parse (not prose).
4. **Tool use (function calling)** — let the model call *your* functions
   (e.g. your `search()` from module 04) and use the results.
5. **Streaming** — tokens as they arrive, for responsive UIs.
6. **Tokens & cost** — why prompts cost money; prompt caching to cut it.

## Your first concrete step
Open [modules/04-rag-basics/example_4b_rag.py](../04-rag-basics/example_4b_rag.py),
find the **fake LLM** function, and replace it with a real Claude call that takes
the retrieved chunks as context. That's RAG, for real.

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...   # keep keys out of code (see Module 10)
```

```python
from anthropic import Anthropic
client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment

def real_llm(question, context_chunks):
    context = "\n\n".join(context_chunks)
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=400,
        system="Answer ONLY from the provided context. If it's not there, say you don't know.",
        messages=[{"role": "user",
                   "content": f"Context:\n{context}\n\nQuestion: {question}"}],
    )
    return msg.content[0].text
```

That `system` prompt ("answer only from context, else say you don't know") is the
single most important RAG instruction — it's what stops hallucination.

## Reference
For exact, current API details (params, tool use, caching, model IDs, pricing)
use the project's **claude-api** skill, or the official Anthropic docs. Don't rely
on memory for API shapes — they change.

→ Next: [Module 10 — Building apps](../10-building-apps/)
