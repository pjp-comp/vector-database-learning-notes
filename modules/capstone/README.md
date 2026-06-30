# Capstone — Build one real thing, end to end

> The most important module. One finished, deployed project teaches more — and
> says more to an employer — than every tutorial combined.

## The rule
Pick **one** brief below (or your own). Take it all the way: real data, real Claude
calls, a UI, basic evaluation, and a deployed URL. Done beats perfect.

## Brief A — "Chat with your docs" (recommended first capstone)
A RAG app that answers questions over **your own** PDFs/notes.
- **Data:** your documents (reuse the PDF flow from [bonus/pdf-rag](../../bonus/pdf-rag/)).
- **Retrieve:** chunk + embed + vector search (modules 01–04).
- **Generate:** real Claude call with the "answer only from context" system prompt
  (module 09).
- **Interface:** a Streamlit chat UI that shows the answer **and its sources**
  (module 10).
- **Evaluate:** a dozen Q→expected-source pairs; report hit-rate (module 11).
- **Deploy:** Streamlit Cloud or Render (module 12).

## Brief B — Support / FAQ bot
A bot that answers product questions and **refuses when it doesn't know.**
- Hybrid search (module 05) so exact codes/terms work.
- CRAG-style grading (module 07): if retrieval is weak, say "I don't know" instead
  of guessing. This refusal behavior is the whole point — it's what makes it
  trustworthy.
- Same app/eval/deploy stack as Brief A.

## Brief C — Your own idea
Anything that uses **retrieval + a real LLM + a UI**. Keep the scope tiny enough to
actually finish.

## Definition of done (all briefs)
- [ ] Runs on real data, not toy strings.
- [ ] Uses a real Claude call (the latest suitable model), key in an env var.
- [ ] Has a UI a non-coder could use.
- [ ] Cites its sources in the answer.
- [ ] Has a small eval set you ran before/after at least one change.
- [ ] Is deployed at a shareable URL.
- [ ] Has a short README: what it does, how to run it, what you learned.

## After the capstone
Write up what you built and the decisions you made (chunk size, model, why CRAG).
*That writeup* is your portfolio. Then revisit the
"[what's intentionally not here](../../ROADMAP.md#whats-intentionally-not-here-and-where-to-go-next)"
list in the roadmap for where to go next.
