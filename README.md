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

**Initial seed (from `data/raw/metpo.owl`, METPO 2025-11-25):**

| Category | Count |
|---|---:|
| MORPHOLOGY | 65 |
| PHYSIOLOGY | 31 |
| ENVIRONMENT | 103 |
| METABOLISM | 108 |
| GENOMICS | 5 |
| ECOLOGY | 10 |
| OBSERVATION | 20 |
| QUANTITATIVE_PROPERTY | 7 |
| UPPER | 5 |
| **TOTAL** | **354** |

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
  biological processes. Use ontology/database CURIEs in `grounding`
  when available; label-only draft nodes are permitted in v1.
- **TraitSynonym / EvidenceItem / CurationEvent** — ancillary classes.
- **TraitCategoryEnum** — the 10 buckets above.
- **TermKindEnum** — `CLASS` / `DATATYPE_PROPERTY` /
  `OBJECT_PROPERTY` / `ANNOTATION_PROPERTY`.
- **MappingStatusEnum** — `SEEDED` / `REVIEWED` / `DEPRECATED`.
- **PriorityEnum**, **SynonymTypeEnum**.

## Layout

```
TraitMech/
├── data/
│   ├── raw/metpo.owl                    # vendored METPO release (2025-11-25)
│   └── traits/<category>/<slug>.yaml    # 354 seeded TraitRecords
├── src/traitmech/
│   └── schema/traitmech.yaml            # LinkML schema
├── scripts/
│   └── seed_from_metpo.py               # OWL → YAML seeder
├── tests/
└── docs/
```

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
5. **Validate**: `just validate-all` runs `linkml-validate` over
   every record.

## Deep Research

TraitMech mirrors DisMech's `deep-research-client` workflow for agentic
curation support. Use Falcon/FutureHouse research reports as source-finding
inputs, then manually curate only DOI-backed claims into TraitRecord YAML.

```bash
export EDISON_API_KEY=...        # or FUTUREHOUSE_API_KEY; the wrapper maps it
just research-provider falcon
just research-trait falcon physiology autotrophic
just research-trait falcon physiology autotrophic --dry-run
```

Reports are written under `research/traits/<category>/` with separate citation
files. The API key is read from the environment and is never written by the
TraitMech tooling.

## Cross-repo integration

- Records preserve their METPO CURIE in `identifier` so trait references
  in CultureMech / MediaIngredientMech / kg-microbe (where METPO terms
  already appear) resolve directly to a TraitMech YAML.
- `xrefs` carries equivalents in PATO / GO / NCIT / ENVO / CHEBI / UO
  for cross-ontology lookup.

## License

CC0-1.0 — Public Domain Dedication.
