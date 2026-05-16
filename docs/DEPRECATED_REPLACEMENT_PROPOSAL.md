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
identifier: traitmech:UCS_GLUCOSE
label: uses glucose as carbon source
definition: A metabolic trait in which an organism uses glucose as
  its sole or primary carbon source for growth.
definition_source: DOI:10.1016/B978-012373944-5.00083-3
trait_category: METABOLISM
term_kind: CLASS
mapping_status: REVIEWED
parent_traits:
- METPO:1000060          # 'metabolism' umbrella CLASS — the right
                         # rdfs:subClassOf parent. METPO:2000006
                         # (the OBJECT_PROPERTY this record replaces)
                         # belongs in xrefs / curation_history, NOT
                         # in parent_traits (property vs class
                         # hierarchy).
xrefs:
- CHEBI:17234            # glucose
- METPO:2000006          # replaces this deprecated relation carrier
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
    grounding: traitmech:UCS_GLUCOSE
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
  - subject: glucose_uptake
    predicate: feeds
    object: glycolysis
    description: Imported glucose enters the glycolytic pathway.
    evidence:
    - reference: DOI:10.1128/JB.183.16.4641-4654.2001
      snippet: glucose
      notes: Supports glucose as the substrate entering glycolysis.
  - subject: glycolysis
    predicate: produces
    object: precursor_metabolites
    description: Glycolysis yields pyruvate and central intermediates
      for biosynthesis.
    evidence:
    - reference: DOI:10.1128/JB.183.16.4641-4654.2001
      snippet: glycolysis
      notes: Supports glycolysis as a producer of central catabolic
        precursors.
  - subject: precursor_metabolites
    predicate: enables
    object: cellular_growth
    description: Central metabolites supply biosynthesis required
      for net biomass accumulation.
    evidence:
    - reference: DOI:10.1128/JB.183.16.4641-4654.2001
      snippet: growth
      notes: Supports central catabolic precursors as required for
        growth on glucose.
  - subject: cellular_growth
    predicate: manifests as
    object: trait
    description: Net growth on glucose manifests the
      use-glucose-as-carbon-source trait.
    evidence:
    - reference: DOI:10.1128/JB.183.16.4641-4654.2001
      snippet: glucose as the sole carbon source
      notes: Supports the trait endpoint.
curation_history:
- timestamp: '...'
  curator: claude
  action: REPLACES_DEPRECATED_RELATION
  changes: 'Replaces the generic METPO:2000006 (uses_as_carbon_source)
    carrier for glucose specifically. Replacement lineage:
    replaces METPO:2000006 + CHEBI:17234.'
  llm_assisted: true
```

(The example above is intentionally a complete-edge graph so it can
be lifted directly as a starting record once the identifier policy
is settled. Note that lineage is recorded in `changes` and in
`xrefs`, not in a dedicated `replaced_by:` field, since
`CurationEvent` does not currently support one — see Decision 4
below.)

## Key design decisions for the user

1. **Identifier prefix**. METPO IDs are assigned upstream by the
   METPO maintainers, so TraitMech cannot mint new METPO IDs.
   Options:
   - **(a)** Coordinate with METPO upstream: file an issue listing
     the specific records we want and get METPO IDs assigned. Slow
     but keeps the namespace clean.
   - **(b)** Use the local `traitmech:` prefix for now (the schema
     already declares it; CURIE pattern accepts it). Later, when
     METPO accepts the records, do a one-off ID rewrite (a regex
     over `data/traits/` is straightforward).
   - **(c)** Don't replace; keep the deprecated records and use
     `xrefs` or `synonyms` on existing trait records to express the
     substrate-specific information.
   - The recommended option is **(b)** for tractable progress with
     **(a)** filed as a parallel upstream issue. The worked example
     above uses option (b) (`traitmech:UCS_GLUCOSE`). Note that the
     schema's declared prefix is **lowercase** `traitmech:` (matching
     the lowercase `traitmech: https://w3id.org/traitmech/` mapping
     in `src/traitmech/schema/traitmech.yaml`); the ID's local part
     can be mixed-case for readability.

2. **Naming scheme**. A coherent ID/slug pattern keeps the corpus
   navigable. Suggestion:
   - ID: `traitmech:<RELATION>_<CHEMICAL>` where `<RELATION>` is a
     short code (`UCS` = uses as carbon source, `UES` = uses as
     energy source, `UEA` = uses as electron acceptor, `UED` = uses
     as electron donor, `FERM` = ferments, etc.) and `<CHEMICAL>` is
     the substrate's slug.
   - File slug: `uses_glucose_as_carbon_source.yaml` (i.e., the
     human-readable form), placed under `data/traits/metabolism/`.
     File slug uses snake_case to match the rest of the corpus.
   - Label: human-readable (`uses glucose as carbon source`),
     spaces not underscores.

3. **Scope of the first batch**. 94 metabolism relation carriers × N
   substrates is intractable as one PR. A sensible first batch
   is **~5 substrates × ~3 relations = ~15 records**, picking
   high-value pairs:
   - Substrates: glucose, acetate, lactate, hydrogen, nitrate (a
     mix of carbon, electron-donor, and electron-acceptor uses).
   - Relations: `uses_as_carbon_source`, `uses_as_electron_donor`,
     `uses_as_electron_acceptor` (the three most-queried use
     relations).
   - Not every cross-pair is biologically meaningful — e.g.,
     `uses_glucose_as_electron_acceptor` isn't a real phenotype.
     Curate only meaningful pairs, expected to be 10–15 records
     out of the 5×3 = 15 candidate matrix.
   - Avoid an "every substrate × every relation" first batch.

4. **Replacement lineage** (existing DEPRECATED records → new
   records). Two important constraints:
   - The DEPRECATED record is an `OBJECT_PROPERTY` (relation), not a
     `CLASS`. It is **not** the rdfs:subClassOf parent of the new
     record. `parent_traits` should point to a real class anchor
     (e.g., the `metabolism` umbrella `METPO:1000060`), not to the
     deprecated property.
   - The schema's `CurationEvent` currently does **not** have a
     dedicated `replaced_by:` field — it carries `timestamp`,
     `curator`, `action`, `changes`, `llm_assisted` only. Record
     replacement lineage in two existing slots:
     - **`xrefs:`** on the new record points to the deprecated
       METPO ID (e.g., `xrefs: [METPO:2000006, CHEBI:17234]`).
     - **`curation_history.changes:`** explicitly states "replaces
       METPO:2000006 + CHEBI:17234".
   - If a structured lineage field is desired, propose a small
     schema extension in a separate PR (e.g., a `replaces:` field
     on `TraitRecord` that takes a list of CURIEs). Don't invent
     unsupported fields in YAML — they would break validation.
   - Leave the DEPRECATED records themselves in place; they remain
     as the upstream-METPO IDs that downstream consumers may still
     reference.

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
