# TraitMech

Microbial ecophysiological trait knowledge base, seeded from
[METPO](https://w3id.org/metpo) and curated incrementally.

## Overview

TraitMech is the trait/phenotype counterpart of [CultureMech](../CultureMech)
(growth media), [MediaIngredientMech](../MediaIngredientMech) (chemical
ingredients), and [CommunityMech](../CommunityMech) (microbial communities).
Each trait — Gram type, motility, pH optimum, "uses as carbon source",
"halophilic", etc. — lives in its own YAML file with provenance back to its
METPO source class and (optionally) to literature evidence.

**Initial seed (from `data/raw/metpo.owl`, METPO 2025-11-25) and current curation status:**

| Category | REVIEWED | DEPRECATED | causal_graphs | Total |
|---|---:|---:|---:|---:|
| MORPHOLOGY | 88 | 0 | 88 | 88 |
| PHYSIOLOGY | 45 | 0 | 45 | 45 |
| ENVIRONMENT | 121 | 0 | 121 | 121 |
| ECOLOGY | 26 | 0 | 26 | 26 |
| GENOMICS | 19 | 0 | 19 | 19 |
| UPPER | 8 | 0 | 5 | 8 |
| METABOLISM | 120 | 23 | 49 | 143 |
| OBSERVATION | 0 | 20 | 0 | 20 |
| QUANTITATIVE_PROPERTY | 0 | 7 | 0 | 7 |
| **TOTAL** | **427** | **50** | **353** | **477** |

All 477 records have a terminal curation status: 427 are `REVIEWED` and 50 are
`DEPRECATED`. Of the reviewed records, 353 currently carry causal graphs. The
50 deprecated records (23 metabolism, 20 observation, 7 quantitative_property)
are generic relation or measurement carriers from the upstream METPO seed that
are not intended to carry mechanism graphs in TraitMech. They are retained for
traceability while specific trait records capture the chemical, quality,
measurement, or growth context.

(`material entity` subtree — chemicals / microbes / enzymes — is not
seeded; those belong in MIM / CultureMech.)

## Quick start

```bash
just install                  # uv sync --extra dev
just gen-schema               # generate dataclasses from LinkML
just seed-from-metpo          # dry-run; print per-category counts
just seed-apply               # write data/traits/<category>/<slug>.yaml
just validate-all             # validate every TraitRecord YAML
```

## Schema

`src/traitmech/schema/traitmech.yaml` defines:

- **TraitRecord** — root class, one per YAML file. Carries
  `identifier` (METPO CURIE), `label`, `definition`, `parent_traits`,
  `xrefs`, `synonyms`, `trait_category`, `term_kind`, optional
  `evidence`, optional `curation_history`, and optional inline
  `causal_graphs`.
- **CausalGraph / CausalNode / CausalEdge** — evidence-backed causal
  mechanism graphs for trait pages. Nodes can represent traits,
  pathways, environmental factors, experimental factors, genes/proteins,
  chemicals, organelles, cellular localizations, molecular functions, or
  biological processes. Gene/protein nodes use taxon-agnostic semantic CURIEs
  in `grounding`; organism-specific UniProt accessions are stored as
  taxon-paired, evidence-bearing `ProteinExample` entries.
- **ProteinExample / CanonicalExample** — source-backed protein instances and
  canonical organism exemplars linked by the same `NCBITaxon` identifier.
- **TraitSynonym / EvidenceItem / CurationEvent** — ancillary classes.
- **TraitCategoryEnum** — 11 schema buckets (the 9 populated buckets above,
  plus `DETECTION` and `OTHER`).
- **TermKindEnum** — `CLASS` / `DATATYPE_PROPERTY` /
  `OBJECT_PROPERTY` / `ANNOTATION_PROPERTY`.
- **MappingStatusEnum** — `SEEDED` / `REVIEWED` / `DEPRECATED`.
- **PriorityEnum**, **SynonymTypeEnum**.

## Layout

```
TraitMech/
├── data/
│   ├── raw/metpo.owl                    # vendored METPO release (2025-11-25)
│   ├── embeddings/                      # graph, nearest-neighbour, and UMAP data
│   └── traits/<category>/<slug>.yaml    # 477 curated TraitRecords
├── mappings/                                # reviewed node and predicate groundings
├── research/traits/                         # source-finding reports and sidecars
├── proposals/                               # upstream METPO proposal cohorts
├── reports/                                 # audits, residuals, and curation backlogs
├── history/                                 # append-only curation provenance
├── pages/                                   # rendered trait browser and graph views
├── app/                                     # priority and discussion dashboards
├── src/traitmech/
│   └── schema/traitmech.yaml            # LinkML schema
├── scripts/
│   └── *.py                             # seed, validate, audit, migrate, and render
├── tests/
└── docs/
    ├── CURATION_PLAYBOOK.md             # how to curate a TraitRecord
    ├── GROUNDING_POLICY.md              # which ontology to ground to
    ├── WORKFLOW_CONVENTIONS.md          # CI: action pinning, concurrency
    └── SCHEMA.md
```

## Artifacts and outputs

The [rendered TraitMech site](pages/index.html) is the main human-facing entry
point. It includes the [trait browser](pages/browse.html), [causal graph
explorer](pages/graph.html), and [UMAP view](pages/umap.html). Additional views
are the [QC dashboard](dashboard/index.html), [research-priority
dashboard](app/dashboard/priority.html), and [curation discussions
dashboard](app/discussions/index.html).

The complete artifact collections are:

| Collection | Contents |
|---|---|
| [Trait records](data/traits/) | The authoritative per-trait YAML corpus, grouped by category |
| [Schemas](src/traitmech/schema/) | TraitMech, shared Mech, and curation-history LinkML schemas |
| [Vendored sources](data/raw/) | The pinned METPO and Biolink Model inputs |
| [Grounding mappings](mappings/) | Reviewed node, predicate, and UniProt grounding tables |
| [Derived embeddings](data/embeddings/) | Trait graph, DeepWalk, nearest-neighbour, and UMAP artifacts |
| [Research artifacts](research/traits/) | Per-trait deep-research reports and citation sidecars |
| [METPO proposals](proposals/README.md) | Upstream proposal cohorts, reviewer narratives, ROBOT tables, and SSSOM mappings |
| [Audit and backlog reports](reports/) | Quality reports, residuals, match candidates, and curation queues |
| [Curation history](history/README.md) | Append-only provenance for record, mapping, report, and infrastructure changes |
| [Rendered pages](pages/) | Generated trait pages, category indexes, graph data, and static assets |
| [Dashboards and apps](app/) | Research prioritization and discussion artifacts |
| [QC dashboard artifacts](dashboard/) | Coverage dashboard HTML and chart |
| [Research prompts](prompts/) | Reusable Claude Code and backlog-loop prompts |
| [Research template](templates/trait_causal_graph_research.md) | Causal-graph research report template |
| [Audit configuration](conf/) | Ratchet baselines, provider routing, QC, and prioritization configuration |
| [Documentation](docs/) | Schema, curation, grounding, workflow, and integration guidance |
| [Claude skills](.claude/skills/) and [command](.claude/commands/) | Repository-specific agent workflows and guardrails |

For direct access to every committed report, see:

- Graph quality: [causal graph audit](reports/causal_graph_audit.tsv),
  [connectivity](reports/causal_graph_connectivity.tsv), [protein/taxon
  coverage](reports/graph_protein_taxon_coverage.tsv), historical paid-research
  snapshots for [completeness](reports/graph_completeness_audit.tsv) and the
  [enrichment backlog](reports/graph_enrichment_backlog.md), and [audit
  manifest](reports/trait_graph_audit_manifest.tsv).
- Validation and pipeline quality: [instance summary](reports/instance_validation_summary.md),
  [instance failures](reports/instance_validation_failures.tsv), [schema gap
  audit](reports/schema_gap_audit.md), [pipeline gap
  audit](reports/pipeline_gap_audit.md), [writer
  audit](reports/pipeline_writers_audit.tsv), [Biolink
  coverage](reports/biolink_coverage.tsv), and [predicate domain
  audit](reports/predicate_domain_audit.tsv).
- Grounding quality: [node residual](reports/node_grounding_residual.tsv),
  [predicate residual](reports/predicate_grounding_residual.tsv), [node match
  candidates](reports/node_match_candidates.tsv), [enriched node
  candidates](reports/node_match_candidates_enriched.tsv), [fuzzy node
  candidates](reports/node_fuzzy_candidates.tsv), [research grounding
  backlog](reports/research_grounding_backlog.tsv), [research grounding
  drift](reports/research_grounding_drift.tsv), [UniProt
  audit](reports/uniprot_grounding_audit.tsv), [UniProt
  candidates](reports/uniprot_match_candidates.tsv), [label
  drift](reports/label_drift.tsv), [trait exact-synonym
  audit](reports/trait_exact_synonym_audit.tsv), [exact-match
  candidates](reports/trait_exact_match_candidates.tsv), [exact-synonym
  collisions](reports/exact_synonym_collisions.tsv), [causal-grounding
  exactness](reports/causal_grounding_exactness.tsv), and the [ontology
  snapshot manifest](reports/ontology_snapshot_manifest.tsv). The [METPO
  2026-06-12 release delta](reports/metpo_2026_06_12_release_delta.tsv) records
  every source addition and changed field considered during that migration;
  its [active-review table](reports/metpo_2026_06_12_active_review.tsv) and
  [review narrative](docs/METPO_2026_06_12_ACTIVE_REVIEW.md) document the final
  curation decisions.
- Curation queues: [gap-fix narrative](reports/gap_fix_backlog.md), [gap-fix
  table](reports/gap_fix_backlog.tsv), [knowledge-gap
  narrative](reports/knowledge_gap_scan.md), [knowledge-gap
  data](reports/knowledge_gap_scan.json), [promotion
  review](reports/promote_reviewed_batch1.md), and [proposal citation
  audit](reports/proposal_citation_audit.tsv).
- Trait proposal reports: [ecology](reports/ecology_trait_proposals.md),
  [environment](reports/environment_trait_proposals.md),
  [genomics](reports/genomics_trait_proposals.md),
  [metabolism](reports/metabolism_trait_proposals.md), [metabolism round
  2](reports/metabolism_round2_trait_proposals.md),
  [morphology](reports/morphology_trait_proposals.md),
  [physiology](reports/physiology_trait_proposals.md), and
  [leftovers](reports/leftover_trait_proposals.md).

## Workflow

1. **Refresh upstream**: `just refresh-metpo` copies the latest
   `metpo.owl` from `../assays/assay-metadata/`.
2. **Seed**: `just seed-apply` creates new YAMLs without touching
   existing ones (use `--force` to overwrite).
3. **Curate**: edit `data/traits/<category>/<slug>.yaml` directly;
   set `mapping_status: REVIEWED`, append a `CurationEvent`, attach
   `EvidenceItem` blocks with PMID + verbatim snippet.
4. **Add causal graphs**: add `causal_graphs` only when the trait has
   source-backed mechanism structure. Every `CausalEdge` must include
   edge-level `evidence`; prefer grounded CURIEs for nodes and
   predicates when a suitable ontology or database term is known.
5. **Validate**: `just validate-all` (alias for `just validate-strict`)
   runs closed-mode LinkML validation over every record; unknown fields
   and missing required attributes fail with exit 1 and a row in
   `reports/instance_validation_failures.tsv`.

## Deep Research

TraitMech mirrors DisMech's `deep-research-client` workflow for agentic
curation support. Use Edison (Falcon) research reports as source-finding
inputs, then manually curate only DOI-backed claims into TraitRecord YAML.

`edison` is the default provider — a TraitMech alias for `deep-research-client`'s
`falcon`, the Edison Scientific research agent. The client has no provider
literally named `edison`; see `.claude/skills/research-causal-graphs/SKILL.md`.
`rosalind` is OpenAI's GPT-Rosalind life-sciences model, driven through the
client's `openai` provider with an explicit model id and written to its own
`-deep-research-rosalind.md` namespace; see `docs/DEEP_RESEARCH_PROVIDERS.md`.

```bash
export EDISON_API_KEY=...        # Edison platform credential; also what falcon needs
export ROSALIND_API_KEY=...      # GPT-Rosalind: the only key the lane reads
just research-provider falcon
just rosalind-canary                                  # unbilled: key sees the model?
just deep-research-providers causal_mechanism
just deep-research-provider asta definition_grounding
just research-trait physiology autotrophic            # Edison (default provider)
just research-trait physiology autotrophic --dry-run
just research-trait physiology autotrophic --provider openai   # override
just research-trait ecology gut_associated --provider rosalind  # GPT-Rosalind
```

Reports are written under `research/traits/<category>/` with separate citation
files. The API key is read from the environment and is never written by the
TraitMech tooling.

`deep-research-providers` performs TraitMech-specific triage across discovery,
mechanistic synthesis, and independent edge/identifier verification. Use
`definition_grounding` when the target is scope, synonyms, parents, or ontology
mapping rather than a causal graph.

## Cross-repo integration

- Records preserve their METPO CURIE in `identifier` so trait references
  in CultureMech / MediaIngredientMech / kg-microbe (where METPO terms
  already appear) resolve directly to a TraitMech YAML.
- `xrefs` carries equivalents in PATO / GO / NCIT / ENVO / CHEBI / UO
  for cross-ontology lookup.

## License

CC0-1.0 — Public Domain Dedication.
