# Promote PROPOSED → REVIEWED — batch 1

**Date:** 2026-06-08 · **Curator:** claude (LLM-assisted)

## What this does

Begins the PROPOSED → REVIEWED promotion of the 120 literature-backed candidate traits by
adding **evidence-backed `causal_graphs`** (the curation depth the seeded corpus carries) and
flipping `mapping_status` to `REVIEWED`. This is **batch 1 (4 traits)** — a quality-first
exemplar across categories; the remaining ~116 are ongoing.

Each added causal graph: typed nodes with **ontology groundings** (CHEBI/GO + the trait's own
`traitmech:` IRI), and edges that each carry **≥1 literature citation** (reused from the trait's
own evidence) plus a **grounded `predicate_id`** drawn from `mappings/predicate_grounding.tsv`
(RO / METPO / biolink). No CURIE was invented — chemical/process groundings were verified against
ChEBI/GO, and predicate groundings reuse the repo's existing verified mapping.

## Promoted traits
| Trait | ID | Causal graph | Node groundings | Predicate groundings |
|-------|----|--------------|-----------------|----------------------|
| catalase activity | traitmech:000075 | H2O2 dismutation | CHEBI:16240 (H2O2), CHEBI:15379 (O2), CHEBI:15377 (water), GO:0004096 | RO:0002327, biolink:consumes, METPO:2000202 |
| nitrogen fixation | traitmech:000103 | nitrogenase N2 reduction | CHEBI:17997 (N2), CHEBI:16134 (ammonia), GO:0009399 | RO:0002327, biolink:consumes, METPO:2000202, RO:0002502 |
| sulfur oxidation | traitmech:000106 | Sox sulfur → sulfate | CHEBI:16136 (H2S), CHEBI:16189 (sulfate) | RO:0002327, METPO:2000016, METPO:2000202 |
| iron oxidation | traitmech:000107 | Fe(II) → Fe(III) | CHEBI:29033 (Fe2+), CHEBI:29034 (Fe3+) | METPO:2000016, METPO:2000202 |

## Validation
- `just validate-strict` → 0 errors over **471** files (causal-graph structure + required edge
  evidence all valid).
- `audit-proposals` → **110/110** remaining PROPOSED still passing (the 4 promoted exit the audit
  as REVIEWED).
- `pytest` → 70 passed.

## Method (repeatable for the remaining ~116)
1. Author a causal graph whose node/predicate labels match `mappings/*.tsv` (so groundings reuse
   verified CURIEs); add new ChEBI/GO node groundings only after verifying the ID.
2. Edge evidence reuses the trait's existing verified citations (every edge ≥1 reference).
3. Set `mapping_status: REVIEWED`; append a `CURATED_CAUSAL_GRAPH` curation event.
4. `validate-strict` + `pytest`.

## Remaining
~116 PROPOSED traits still to promote in later batches, prioritizing those with the clearest
mechanisms and best ChEBI/GO grounding coverage.
