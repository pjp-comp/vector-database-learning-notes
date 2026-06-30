# Phase 6b — Corrective RAG (CRAG)

**Big idea:** plain RAG answers from the top chunk even when it's a bad match.
**CRAG** grades the retrieved chunk first — and if it's weak, it corrects the
query and retries, or **refuses to answer** instead of hallucinating.

## Run
```bash
python modules/07-corrective-rag/example.py
```

## What you'll see
- **Case A** — "can I get my money back": the first chunk grades as *AMBIGUOUS*,
  so CRAG rewrites the query and the second retrieval is *CORRECT*.
- **Case B** — "how long does international shipping take": the knowledge base has
  no shipping info, so the chunk grades *INCORRECT* and CRAG **refuses** rather
  than guessing.

## The grader's three verdicts
| Verdict | Score | Action |
|---|---|---|
| CORRECT | high | trust the chunk, answer |
| AMBIGUOUS | middling | rewrite the query, retry |
| INCORRECT | low | fall back / refuse (don't hallucinate) |

## About the "grader brain"
A real CRAG system uses an **LLM** to judge "is this chunk relevant?". Here that's
faked with a cosine-score threshold so it runs with no API key. The
*grade → correct → answer* loop is the real lesson.

## How it relates to Module 06
Agentic RAG ([Module 06](../06-agentic-rag/)) loops to *improve* a weak result. CRAG adds the
explicit **grade-and-fall-back** safety net — its job is to *avoid confident wrong
answers* when the knowledge base has gaps.

→ Map of all RAG types: [rag_architecture_types.md](../../rag_architecture_types.md)
→ Full explanation: [learning_notes.md](../../learning_notes.md)
