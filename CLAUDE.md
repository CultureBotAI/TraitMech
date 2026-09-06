# Claude guidance for TraitMech

TraitMech is a knowledge base of microbial ecophysiological traits. Curated
records live under `data/traits/`; their authoritative LinkML schema is
`src/traitmech/schema/traitmech.yaml`.

Use live commands and tracked files as the source of truth. Do not rely on
record counts, proposal versions, coverage percentages, or identifier ranges
quoted in prose; derive them again before planning or reporting.

## Fact-based answers only

Verify any comparison, count, status, or historical claim with a live tool
call (`gh`, `git`, `grep`, `Read`) before stating it; "I recall" or a prior
summary in this conversation is not verification. The intro paragraph above
is one instance of this rule (record counts, proposal versions, coverage
percentages, identifier ranges), not a separate concern -- it applies to any
claim. If something can't be verified this session, say so instead of
presenting a guess as fact.

## Route work to the maintained guidance

- New trait records: [add-trait](.claude/skills/add-trait/SKILL.md)
- Schema, instance, or writer quality: [audit-schema-gaps](.claude/skills/audit-schema-gaps/SKILL.md)
- Identifier choice or minting: [manage-identifiers](.claude/skills/manage-identifiers/SKILL.md)
- METPO proposals: [metpo-proposal](.claude/skills/metpo-proposal/SKILL.md)
- Research and curation prioritization: [trait-priority](.claude/skills/trait-priority/SKILL.md)
- Paid trait research: [deep-research-trait](.claude/skills/deep-research-trait/SKILL.md) or [research-causal-graphs](.claude/skills/research-causal-graphs/SKILL.md)
- Backlog reconciliation: [next-tasks](.claude/skills/next-tasks/SKILL.md)
- Full open-issue queue triage: [review-open-issues](.claude/skills/review-open-issues/SKILL.md)

Read [the curation playbook](docs/CURATION_PLAYBOOK.md) and [grounding
policy](docs/GROUNDING_POLICY.md) before changing curated data. Records listed
in [DO_NOT_WORK.md](DO_NOT_WORK.md) are excluded from agentic curation; do not
edit them unless a user removes the entry.

## Safe mutation contract

- Inspect first. Mutation commands must default to a dry run or require an
  explicit `--apply`/`--write` action.
- Every changed trait must receive a per-record `curation_history` event through
  `record_curation_event`, and writers must use `write_validated_trait`; do not
  bypass closed-schema validation or provenance.
- The same trait change also requires an append-only repository history record. Follow
  [history/README.md](history/README.md) and scaffold it with `just new-history`.
  Use one record per hand-curated target or one record per coherent bulk change.
- Regenerate every affected derived report, dashboard, graph audit, mapping,
  and rendered page through its maintained `just` recipe. Never hand-edit a
  generated artifact to make a freshness check pass. This applies again after
  merging `main` into a branch: two curation PRs will normally conflict on
  `pages/` by construction, and the resolution is regeneration, never picking a
  side. See
  [the playbook](docs/CURATION_PLAYBOOK.md#merging-when-another-curation-pr-lands-first-622).
- Preserve unrelated work in a dirty tree and keep changes scoped.

## Required validation

Run focused tests while editing, then run:

```bash
just qc
```

Also run the relevant domain checks when applicable:

```bash
just validate-history
just validate-products
```

Use `just validate-all` or `just validate-strict` for closed-schema corpus
validation; `validate-all` delegates to the strict implementation. Treat a
non-zero exit as a real failure.

## Research and generated artifacts

Research under `research/` is tracked provenance because recreating it may cost
money. Inspect existing reports and manifests before launching research. Always
dry-run and review a single canary first, and obtain explicit user approval
before any paid call or batch expansion.

Generated LinkML dataclasses are ignored and regenerable; do not commit
`src/traitmech/schema/traitmech_dataclasses.py`. Other reports, dashboards,
proposal artifacts, audits, and pages may be tracked inputs or freshness-gated
outputs. Check `.gitignore`, the relevant `just` recipe, and `git status`
instead of assuming their policy.

If guidance and executable behavior disagree, verify the tests, follow the
live implementation, and update the guidance in the same change.
