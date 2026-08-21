---
name: trait-priority
description: Build a live-state TraitMech curation queue with a recommended action per record. Use when asked what to curate or research next, how to prioritize graph work, or whether binned trait families should be lumped.
---

# Trait priority

Use the maintained live-state queue:

```bash
just trait-priority
just trait-priority --top 0
just trait-priority --action DEEPEN_CAUSAL_GRAPH
just trait-priority --action ADD_CANONICAL_EXAMPLES
just trait-priority --unresearched-only
just trait-priority --format tsv --top 0
just gen-priority-dashboard
```

The weights and thresholds are declared in `conf/trait_priority.yaml`. The CLI
and `app/dashboard/priority.{html,json}` use the same implementation in
`scripts/trait_priority.py`.

## Why this is the authoritative queue

The queue reads current trait records and computes graph size, fragmentation,
orphans, evidence, examples, hierarchy, and series overlap from the live corpus.
It recommends an action instead of presenting one ambiguous score.

Do not rank from `reports/graph_completeness_audit.tsv` or
`reports/graph_enrichment_backlog.md`. They are retained paid-research snapshots,
not generated views of the current corpus. Their old `missing_modules` values
cannot be refreshed locally and must not contribute to a live score (#443,
#480). The backlog remains useful as a DOI-backed lead for a selected record,
but verify every proposed edge against that record's current graph before
applying it.

## Interpret the actions

- `DEEPEN_CAUSAL_GRAPH` is the main queue for applying existing research to a
  thin or fragmented graph.
- `ADD_CANONICAL_EXAMPLES` identifies graph-bearing records without organism
  exemplars.
- `BUILD_CAUSAL_GRAPH` identifies a mechanism record with no graph.
- `DROP_NON_MECHANISM` and `DROP_DEPRECATED` are set aside; they are not
  research targets.
- `LUMP_INTO_PARENT` fires only when measured sibling overlap crosses the
  configured threshold. Series names alone are not evidence of duplication.

Always report the command's live totals and exclusions rather than copying
counts from this guidance.

## Before paid research

Inspect the selected record, its existing report under `research/traits/`, and
the historical enrichment-backlog row. Most graph work is application of
research already on disk. New research is paid: use the provider workflow,
obtain explicit user approval, and run one canary before any batch.

Related workflows: `research-causal-graphs`, `deep-research-trait`,
`audit-graphs`, and `audit-canonical-examples`.
