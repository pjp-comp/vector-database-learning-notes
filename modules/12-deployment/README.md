# Module 12 — Deployment & basic ops

> Guide module. Getting it off your laptop and keeping it alive.

A project nobody can reach isn't finished. You don't need Kubernetes — you need
*one* place it runs and a few habits so it doesn't surprise you.

## Getting it deployed (pick the simplest that works)
- **Streamlit Community Cloud** — free, dead-simple for a Streamlit app + GitHub.
- **Render / Railway / Fly.io** — easy hosts for a FastAPI service.
- **A container (Docker)** — once you outgrow the above; "runs the same everywhere."

For a beginner capstone, **Streamlit Cloud or Render is plenty.** Don't over-engineer.

## The three things to watch in production
1. **Cost** — LLM and embedding calls cost money per request. Know your per-query
   cost. Use a smaller model (Haiku) where quality allows; use **prompt caching**
   for repeated context.
2. **Latency** — embedding + retrieval + LLM all add up. Stream the answer so it
   *feels* fast; cache repeated queries.
3. **Errors** — the LLM API will sometimes be slow, rate-limited, or down. Log
   failures, retry sensibly, and never show the user a raw stack trace.

## Secrets in production
Same rule as Module 10, enforced harder: API keys come from the host's
**environment/secrets manager**, never from code or the repo. A leaked key is a
real bill and a real incident.

## What "good enough" looks like for a beginner
- It's deployed at a URL you can share.
- Keys are in environment variables, not committed.
- It doesn't crash on a weird question — it degrades gracefully.
- You can state its rough per-query cost and latency.

Hit those four and you can honestly say you've **shipped an AI app.**

→ Next: [the Capstone](../capstone/)
