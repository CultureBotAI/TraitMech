# Proposal: replacing the 121 DEPRECATED relation carriers

## Background

The current TraitMech corpus has **121 records with
`mapping_status: DEPRECATED`**, split as:

| Category | Count | What they are |
|---|---:|---|
| metabolism | 94 | `OBJECT_PROPERTY` relation predicates seeded from METPO (`uses_as_carbon_source`, `does_not_use_as_carbon_source`, `ferments`, `has_phenotype`, `has_growth_temperature_observation`, …) |
| observation | 20 | `CLASS` records representing generic observation/value carriers seeded from METPO (`growth NaCl observation`, `optimum pH observation`, …) |
| quantitative_property | 7 | `DATATYPE_PROPERTY` records (`has maximum observed value`, `has value`, …) |

Each carries a deprecation note that says, roughly:

> Deprecated generic ... relation carrier; later replacement should
> use more specific trait records that combine the relation with the
> chemical, metabolic role, growth condition, and positive or
> negative usage context.

This file proposes how those replacements should be structured so a
future curation push can produce them coherently. **No new TraitRecord
YAMLs are committed in this PR** — the proposal is meant to be
discussed and approved before scaling.

## What "specific trait records" should look like

Take `uses_as_carbon_source` (METPO:2000006) as the worked example.
A single specific replacement record might look like:

```yaml
identifier: TRAITMECH:UCS_GLUCOSE
label: uses glucose as carbon source
definition: A metabolic trait in which an organism uses glucose as
  its sole or primary carbon source for growth.
definition_source: DOI:10.1016/B978-012373944-5.00083-3
trait_category: METABOLISM
term_kind: CLASS
mapping_status: REVIEWED
parent_traits:
- METPO:2000001          # the generic 'metabolic relation' anchor
xrefs:
- CHEBI:17234            # glucose
synonyms:
- synonym_text: glucose as sole carbon source
  synonym_type: RELATED_SYNONYM
  source: traitmech
evidence:
- reference: DOI:10.1128/JB.183.16.4641-4654.2001
  snippet: glucose as the sole carbon source
  notes: Salmonella Typhimurium grown on glucose as sole carbon
    source — example of a specific use-as-carbon-source observation.
causal_graphs:
- graph_id: uses_glucose_as_carbon_source_assimilation
  title: Use of glucose as carbon source
  description: Glucose enters the cell, is funnelled through
    glycolysis into central catabolism, and supplies precursor
    metabolites and energy for growth.
  nodes:
  - node_id: trait
    label: uses glucose as carbon source
    node_type: TRAIT
    grounding: TRAITMECH:UCS_GLUCOSE
    description: Use of glucose as the sole/primary carbon source.
  - node_id: glucose
    label: glucose
    node_type: CHEMICAL
    grounding: CHEBI:17234
    description: Hexose sugar serving as the carbon source.
  - node_id: glucose_uptake
    label: glucose transport
    node_type: BIOLOGICAL_PROCESS
    grounding: GO:0015758
    description: Cellular import of glucose (PTS, MFS, ABC, etc.).
  - node_id: glycolysis
    label: glycolysis
    node_type: PATHWAY
    grounding: GO:0006096
    description: Embden–Meyerhof–Parnas pathway producing pyruvate
      and ATP/NADH.
  - node_id: precursor_metabolites
    label: precursor metabolites
    node_type: CHEMICAL
    description: Central intermediates feeding biosynthesis.
  - node_id: cellular_growth
    label: cellular growth
    node_type: BIOLOGICAL_PROCESS
    description: Net biomass accumulation.
  edges:
  - subject: glucose
    predicate: imported by
    object: glucose_uptake
    description: Extracellular glucose is taken up via dedicated
      transporters before catabolism.
    evidence:
    - reference: DOI:10.1128/JB.183.16.4641-4654.2001
      snippet: glucose as the sole carbon source
      notes: Supports glucose import as the first step of glucose
        catabolism.
  # ... remaining edges glycolysis → precursors → growth ...
curation_history:
- timestamp: '...'
  curator: claude
  action: REPLACES_DEPRECATED_RELATION
  changes: Replaces the generic METPO:2000006 (uses_as_carbon_source)
    carrier for glucose specifically.
  llm_assisted: true
```

## Key design decisions for the user

1. **Identifier prefix**. METPO IDs are assigned upstream by the
   METPO maintainers, so TraitMech cannot mint new METPO IDs.
   Options:
   - **(a)** Coordinate with METPO upstream: file an issue listing
     the specific records we want and get METPO IDs assigned. Slow
     but keeps the namespace clean.
   - **(b)** Use a local `TRAITMECH:` prefix for now (the schema
     pattern `^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$` already
     accepts it). Later, when METPO accepts the records, do a one-off
     ID rewrite (a regex over `data/traits/` is straightforward).
   - **(c)** Don't replace; keep the deprecated records and use
     `xrefs` or `synonyms` on existing trait records to express the
     substrate-specific information.
   - The recommended option is **(b)** for tractable progress with
     **(a)** filed as a parallel upstream issue. The worked example
     above uses option (b) (`TRAITMECH:UCS_GLUCOSE`).

2. **Naming scheme**. A coherent ID/slug pattern keeps the corpus
   navigable. Suggestion:
   - ID: `TRAITMECH:<RELATION>_<CHEMICAL>` where `<RELATION>` is a
     short code (`UCS` = uses as carbon source, `UES` = uses as
     energy source, `UEA` = uses as electron acceptor, `UED` = uses
     as electron donor, `FERM` = ferments, etc.) and `<CHEMICAL>` is
     the substrate's slug.
   - File slug: `uses_glucose_as_carbon_source.yaml` (i.e., the
     human-readable form), placed under `data/traits/metabolism/`.
   - Label: same as file slug but with spaces.

3. **Scope of the first batch**. 94 metabolism relation carriers × N
   substrates is intractable as one PR. A sensible first batch is:
   - Pick **5–10 high-value substrate × relation pairs** that
     downstream consumers actually need (e.g., glucose, acetate,
     lactate, citrate, fumarate, hydrogen, nitrate, sulfate, oxygen,
     ammonia × the canonical relations).
   - That generates **~30–60 new records**, manageable as one or two
     PRs.

4. **What happens to the existing DEPRECATED records?**
   - Leave them in place with their `DEPRECATED` status (they still
     serve as anchors for the new records' `parent_traits` and
     `replaces` xref).
   - Add a `replaced_by:` field in `curation_history` of the new
     record (or as an `xref`) so the lineage is traceable.

5. **Negative usage** (`does_not_use_as_carbon_source` style). 47 of
   the 94 metabolism deprecated records are explicit negations. The
   replacement pattern would mirror the positive form but with
   `does_not_use_glucose_as_carbon_source` records. Recommend
   deferring negation expansion to a later batch (they're 2× the
   work and less central to most downstream queries).

6. **Observation and quantitative_property categories**. These 27
   records are structurally different — they represent observation
   data carriers, not phenotype claims. They probably belong in a
   separate replacement initiative tied to the `BacDive`-style
   strain-observation modelling (see also PR #40 / #41). Defer until
   the metabolism-relation replacement pattern is settled.

## Suggested next step

If options (b) and the worked example look reasonable:

1. Write a small CLI helper (`scripts/replace_deprecated.py`) that
   takes a YAML manifest of `(relation, chemical, label,
   parent_metpo_id)` rows and emits one TraitRecord YAML per row
   with skeletal causal graph nodes (substrate → uptake → pathway →
   biomass) that a human curator fills in.
2. Curate the first batch (glucose, acetate, lactate, citrate, ...
   × `uses_as_carbon_source` and `uses_as_electron_donor`) by hand,
   following the playbook conventions in `docs/CURATION_PLAYBOOK.md`.
3. PR per batch (~10–15 records each), Copilot-reviewed, merged
   into main.
4. After ~50 records, evaluate whether the pattern holds and decide
   whether to keep going manually or invest in heavier automation.

## Why this proposal instead of committing records

The user's earlier note characterised this task as "substantial
scope" needing a pilot. Three things made it preferable to write a
proposal first rather than commit even a single record:

1. **Identifier minting** is a policy decision (option a/b/c above)
   that should be made by maintainers, not unilaterally by the
   curator.
2. **Naming scheme** affects every future replacement; getting it
   wrong creates rework.
3. **Scope** (5–10 substrates × N relations × 94 metabolism records)
   is large enough that a coherent plan beats opportunistic
   per-record curation.

With the decisions made, the replacement push becomes a clear
multi-PR initiative that can run alongside the rest of TraitMech
maintenance.
