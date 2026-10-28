# Portfolio Project Extraction Prompt

Copy everything below the line into a Claude Code session opened **inside the project folder you want to showcase**. It will inspect the codebase and produce a single structured brief. Paste that brief back into the portfolio session and I will turn it into a portfolio project card and a CV entry.

---

You are helping me prepare a project for my software engineering portfolio and CV. You are running inside this project's repository. Investigate the codebase directly before writing anything: read the README, package manifests (package.json, pyproject.toml, requirements.txt, go.mod, etc.), the main entry points, config, infra/deploy files (Dockerfile, terraform, cloudbuild, workflows), and the folder structure. Do not guess the tech stack, confirm it from the files. If the repo does not answer something, ask me a short question or mark it `UNKNOWN`, never invent facts, numbers, or outcomes.

Then output ONE markdown brief in exactly the structure below, and nothing else.

## Required output structure

```
### Project Brief

- **Project name:** short, how it should read as a card title
- **Context/owner:** who it was for (company, client, hackathon, personal) and your role
- **Status:** Production | POC | In Progress | Archived
- **Sponsor/trigger (optional):** who asked for it or what problem forced it, named if relevant

**The problem (2 to 4 sentences):**
What was broken or manual before this existed, and why it mattered (time lost, backlog, risk, cost). Use concrete scale if the repo or I can confirm it.

**What was built (2 to 3 short paragraphs):**
The actual architecture and the hard parts. Name the real components (services, parsers, resolvers, integrations, data stores, auth) and what each does. Call out anything non-obvious or clever. Include concrete numbers only if verifiable (counts of tools/endpoints, line volumes, validation ratios, record sizes).

**Impact (1 to 2 sentences):**
Before vs after in measurable terms if possible (hours to minutes, N-day to N-day, % reduction, backlog cleared). Mark `UNKNOWN` if you cannot verify it, do not fabricate a metric.

**Tech stack (flat list, most important first):**
Comma-separated. Lead with AI/agent tech if present, then languages (Python first if used), then cloud/infra, frameworks, data, tools. Only list what is actually in the repo.

**Links & media (optional):**
- Live URL, demo video URL, docs/report PDFs if any
- Screenshot image files that exist in this repo (give repo-relative paths); note if none

**CV one-liner:**
A single sentence (max ~30 words) summarizing the project for a CV bullet, impact-forward.
```

## Writing rules (strict, these match my portfolio style)

1. Never use em dashes, en dashes, or arrow symbols. Use commas, " | ", or "to" instead. Plain hyphens inside words are fine.
2. No emojis anywhere in the brief.
3. Never say "vibe coding". If AI tooling was used to build it, describe it as "AI-augmented engineering" or "AI-assisted development".
4. Put AI/agent technology first in any ordering; Python first when listing languages.
5. Prefer concrete, verifiable detail over adjectives. No "cutting-edge", "robust", "seamless" filler.
6. Every number must be traceable to the code or to something I confirm. When unsure, write `UNKNOWN` and move on.
7. Keep it factual and specific. I will handle the final polish and the HTML.
