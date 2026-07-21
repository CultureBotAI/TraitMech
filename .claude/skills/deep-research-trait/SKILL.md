---
name: deep-research-trait
description: Run Edison Scientific deep research (PaperQA3) for a TraitMech trait record to gather source-backed mechanism, expression conditions, measurement/assay basis, and ontology grounding (METPO/GO/CHEBI/ENVO). Captures a full provenance bundle (answer, citations, agent state, cost) and produces a curation-focused report for a curator to review and apply. Use when a TraitRecord needs literature evidence before its causal graph or evidence blocks can be curated.
category: research
requires_database: false
requires_internet: true
version: 1.0.0
---

# Deep Research for a Trait (Edison API)

## Overview

Drives the Edison Scientific `edison-client` SDK directly against a TraitMech
`TraitRecord`, so you get Edison's job selection and a complete provenance
bundle. This is the TraitMech port of CommunityMech's `deep-research-community`;
`scripts/_edison_capture.py` is vendored byte-identical across the Mech repos.

**Why not `just research-trait`?** That recipe goes through
`deep-research-client`, whose `falcon` provider *is* Edison — but it exposes no
job control and writes only the answer plus a citations file. Use it for a quick
look; use this skill when the output has to be auditable or re-runnable.

The output is **research input, not curated content**. Nothing here writes to
`data/traits/`. A curator reads the report and hand-applies only DOI-backed
claims, exactly as `README.md` prescribes.

## Prerequisites

- `EDISON_API_KEY` in the repo-root `.env` (see `.env.example`). `just` loads it
  automatically; a bare `python scripts/...` run does not, which is why the
  script calls `load_dotenv()` itself.
- Do **not** also export `EDISON_PLATFORM_API_KEY` unless it is the same
  credential. Two different Edison keys means `just` and direct `python` runs
  authenticate as different accounts, silently splitting task history and
  billing.

## Inputs

A target, in any of three forms:

| Form | Example | Notes |
|---|---|---|
| `category/slug` | `physiology/autotrophic` | preferred — always unambiguous |
| bare slug | `autotrophic` | resolved across categories; **refused** if it matches more than one |
| YAML path | `data/traits/physiology/autotrophic.yaml` | |

Slugs are unique only *within* a category, so the bare form errors rather than
guessing when it is ambiguous — guessing would file research against the wrong
trait.

## Workflow

1. **Pick the job.** `literature` (PaperQA3, default) suits "what mechanism
   produces this trait, under what conditions is it expressed, what is the
   evidence". `literature-high` reads more and costs more. `precedent` finds
   first mentions. `phoenix` synthesises.

2. **Dry-run first.** This renders the full query and writes the `-meta.yaml`
   without calling the API, so you can read the exact prompt before spending:

   ```bash
   just research-trait-edison physiology/autotrophic --dry-run
   ```

   Check `query_chars` and the rendered `query` in the meta file. If the trait's
   `definition` or `evidence` fields are thin, the query will be thin too — fix
   the record first; a vague prompt returns vague literature.

3. **Run it.**

   ```bash
   just research-trait-edison physiology/autotrophic
   just research-trait-edison physiology/autotrophic --job literature-high
   ```

4. **Batch**, from a JSON list of `category/slug` strings (or objects with
   `category` + `slug`):

   ```bash
   just research-trait-edison-batch queue.json --limit 5 --dry-run
   ```

   Unresolvable entries are reported and skipped, not fatal.

5. **Curate.** Open the `.md`, cross-check claims against `-citations.md`, and
   hand-apply only DOI-backed statements into the TraitRecord's `evidence` /
   `causal_graphs`. Cite the DOI, never the report.

## File outputs at a glance

Written to `research/traits/<category>/`, stem
`<slug>-edison-<job>[-<label>]`:

| File | Contents |
|---|---|
| `.md` | the answer — the thing a curator reads |
| `-meta.yaml` | query, task_id, status, total_cost, template path + vars, timestamps |
| `-citations.md` | parsed citation list |
| `-response.json` | raw API response |
| `-agent-state.json` | agent trajectory, when available |
| `-files.json` | files the agent produced |

`--label` suffixes the stem so a run with a non-default template does not
overwrite the default run for the same trait + job.

## Cost & safety

- Every run bills the Edison account behind `EDISON_API_KEY`. `--dry-run` costs
  nothing and still produces the meta file.
- `literature-high` is materially more expensive than `literature`; reach for it
  when the default returns thin results, not by default.
- The per-run `total_cost` is recorded in `-meta.yaml`, and batch runs print a
  total at the end.
- Re-running the same trait + job overwrites in place. Compare `query_sha256`
  across meta files to spot an identical re-run before paying for it.

## Backfilling provenance

Older reports that predate the capture plumbing can be enriched without
re-billing — it refetches from the stored `task_id`:

```bash
just enrich-edison-response --dry-run
just enrich-edison-response
```

The default pattern is recursive (`**/*-edison-*-meta.yaml`) because TraitMech
nests output per category, unlike the flat layout in the sibling Mechs.

## Error handling

| Symptom | Cause |
|---|---|
| `EDISON_API_KEY is not set` | missing from `.env`; see `.env.example` |
| `Ambiguous target '<slug>'` | slug exists in several categories — qualify as `category/slug` |
| `No trait '<slug>' in any category` | wrong slug; the error lists valid categories |
| `Unknown --job` | the message lists valid aliases |
| auth failure on direct `python` but not `just` | a second Edison key is exported in your shell |

## Related

- `scripts/research_trait_edison.py` — this runner
- `scripts/research_trait.py` — the deep-research-client path (`--provider falcon`)
- `scripts/enrich_edison_response.py` — retroactive provenance backfill
- `scripts/_edison_capture.py` — vendored byte-identical across the Mech repos;
  fix it in one place and sync to all
- CommunityMech `deep-research-community`, MIM `deep-research-ingredient`,
  CultureMech `deep-research-medium` — the sibling skills

## Quick reference

```bash
just research-trait-edison physiology/autotrophic --dry-run   # inspect the prompt, free
just research-trait-edison physiology/autotrophic             # default LITERATURE job
just research-trait-edison autotrophic --job literature-high  # deeper, pricier
just research-trait-edison-batch queue.json --limit 5         # batch
just enrich-edison-response --dry-run                         # backfill provenance
```
