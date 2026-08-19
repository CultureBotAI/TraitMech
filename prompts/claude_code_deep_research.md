# Claude Code task: one TraitMech deep-research curation

Work from the TraitMech repository root. Read `CLAUDE.md`, any applicable
`AGENTS.md`, `history/README.md`, the LinkML schema, and the selected record
before editing.

## Mission

Select exactly one high-value microbial-trait mechanism question, research it
with the `claude_code` deep-research provider, and curate supported findings into
one schema-compliant `TraitRecord` YAML file.

The Markdown report under `research/` is raw evidence discovery, not the final
data product. The final product is the updated canonical `TraitRecord`, plus its
required append-only history record, with all validation gates passing.

## Constraints

- Use only `claude_code`. Do not call Falcon/Edison, Cyberian, or another
  provider and do not fall back to one. Run at most one new research job.
- Check for an existing matching Claude Code report first; do not duplicate a
  completed question.
- Do not print or change secrets, `.env`, or API keys.
- Do not change the schema or validators to make generated data pass.
- Prefer primary literature. Keep review evidence clearly identified as review
  evidence. Do not invent CURIEs, predicate identifiers, citations, snippets,
  causal direction, or mechanistic specificity.
- A causal edge requires evidence for that relationship, not merely separate
  evidence that its subject and object exist.
- Keep the edit to one trait and the minimum necessary history/provenance files.

## 1. Pick one question

Inspect the existing, read-only planning evidence first:

- `reports/knowledge_gap_scan.json` and `.md`, if present
- `reports/graph_enrichment_backlog.md`
- `reports/research_grounding_backlog.tsv`
- existing records under `data/traits/`
- existing `research/traits/**/*claude_code*` reports, if present

Choose one existing record with a consequential, researchable causal-mechanism
gap and no equivalent Claude Code report. Prefer a reviewed or seeded trait whose
definition is usable but whose mechanism, causal graph, or edge evidence is
missing or weak. State the category, slug, file path, selection rationale, and
one precise question before running research. Use this form:

> What source-backed molecular, physiological, or ecological mechanism causes
> or enables **<trait>**, and which directed steps can be represented as an
> evidence-backed TraitMech causal graph?

Do not run `knowledge-gap-scan --apply` and do not edit during selection.

## 2. Check the provider, then run one job

Run the non-research provider fit check:

```bash
just deep-research-provider claude_code causal_mechanism
```

If unavailable, stop; do not switch providers. Otherwise run exactly once:

```bash
just research-trait <category> <slug> --provider claude_code
```

Wait for completion and capture the printed report path. Confirm that it is
non-empty and has traceable citations. A failed or evidence-free job is not
permission to retry or to add speculative YAML.

## 3. Save accepted findings as a TraitRecord

Read the schema and comparable curated records before editing
`data/traits/<category>/<slug>.yaml`. Curate claim by claim:

- Improve the definition or definition source only when the source directly
  supports it.
- Model only necessary, directed causal-graph nodes and edges.
- Use schema-allowed node types and existing predicate conventions. Add a
  predicate CURIE only when verified; otherwise retain the supported text form
  if the schema permits it.
- Put evidence on the exact edge or assertion it supports. Use stable DOI/PMID
  identifiers and verbatim snippets where the schema calls for snippets.
- Do not convert correlations, co-occurrence, or predictions into causal edges.
- Preserve mapping status and curator-review status unless the evidence and repo
  policy explicitly justify a change.

Create the required append-only record under `history/` with `just new-history`
and the conventions in `history/README.md`. Mark the work as LLM-assisted and
reference the canonical target and raw Claude Code report. Never edit an old
history entry.

## 4. Validate

Run:

```bash
just validate data/traits/<category>/<slug>.yaml
just validate-strict data/traits/<category>/<slug>.yaml
just audit-graphs
just audit-snippets
just validate-history <new-history-path>
```

Fix the record or new history entry if a check fails. Do not weaken baselines,
edit validators, or launch another research job. Finish with `git diff --check`
and inspect only the intended diff.

## Completion report

Return the selected question and rationale, provider check, single research
command, raw report path, canonical YAML and history paths, accepted/rejected
claims, every validation result, and remaining uncertainty.

