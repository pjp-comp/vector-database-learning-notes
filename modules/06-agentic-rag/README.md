# Phase 6 — Advanced & agentic retrieval

**Big idea:** plain RAG searches once. An **agent** can loop — search, judge
whether the result is good enough, rewrite the query, and search again — like a
person refining their research.

## Run
```bash
python modules/06-agentic-rag/example.py
```

## What you'll see
A vague question ("can I get my money back") gets a weak first result. The agent
notices the low score, rewrites it to "refund policy", searches again, and finds
the right answer.

## About the "agent brain"
A real agent uses an **LLM** to decide "good enough?" and to rewrite the query.
Here those steps are faked with a simple rule + fixed rewrite so it runs with no
API key. The retrieval *loop* is the real lesson.

## Words to know
- **Agentic RAG** — an LLM agent that retrieves, evaluates, and retrieves again.
- **GraphRAG** — retrieval using a knowledge graph (relationships, not just similarity).
- **Multi-modal** — embedding images/audio/code, not just text.
- **Long-context** — sometimes a huge context window reduces the need to retrieve.

→ Full explanation: [learning_notes.md](../../learning_notes.md)
