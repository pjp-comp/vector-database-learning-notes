# Module 11 — Evaluation (measure, don't guess)

> Guide module. The skill that separates hobby projects from real engineering.

"Did that change make it better?" is **unanswerable by vibes.** When you tweak chunk
size, swap a model, or add re-ranking, you need numbers — otherwise you're guessing.

## The two things to measure in RAG
1. **Retrieval quality** — did we fetch the *right* chunks?
   - Build a small set of `(question → which chunk should answer it)` pairs.
   - Metrics: **hit rate** (was the right chunk retrieved at all?) and **MRR**
     (how high did it rank?).
2. **Answer quality** — given good chunks, is the answer good?
   - **Faithfulness** — is the answer grounded in the retrieved text, or made up?
   - **Relevance** — does it actually answer the question?

## Tools
- **RAGAS** — a library that scores faithfulness, answer relevance, and context
  precision/recall for RAG pipelines. The standard starting point.
- **LLM-as-judge** — use a strong model (e.g. Claude) to grade answers against a
  rubric. Cheap to set up, surprisingly effective. (You already saw the *idea* in
  [Module 07 — CRAG](../07-corrective-rag/), where a grader decides if retrieval is
  good enough.)

## The minimum viable eval
You don't need a framework to start. A dozen hand-written
`(question, expected-source, ideal-answer)` rows in a list, plus a script that runs
your pipeline over them and prints hit-rate, gets you 80% of the value. Add RAGAS
once that hurts.

## The habit to build
Before/after **every** change, run your eval set. Keep the number. If it didn't go
up, the change wasn't an improvement — revert it. This is the discipline that makes
you trusted with a real system.

→ Next: [Module 12 — Deployment](../12-deployment/)
