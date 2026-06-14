# METPO ROBOT Template Proposal — TraitMech Synthetic Trait Lift (v5, 2026-06)

> **Upstream submission:** consolidated in [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535) (2026-06-14) — requesting real METPO IDs for this cohort.

## Context

TraitMech is a consumer of METPO: seeded trait records carry `METPO:` identifiers.
When a curator proposes a trait that METPO does not yet contain, it is minted under the
reserved `traitmech:NNNNNN` fallback prefix (see `manage-identifiers` skill). Six
literature-backed proposal rounds (environment, metabolism ×2, ecology, morphology,
physiology, genomics, plus a leftover round) have now minted **120 synthetic traits**,
`traitmech:000001`–`traitmech:000120`, each carrying ≥2 verified literature citations and
enforced by `scripts/audit_proposals.py`.

This **Scope-A** cohort lifts all 120 into METPO so the IDs can round-trip (METPO mints
real IDs → TraitMech re-seeds → `traitmech:` fallbacks retire into synonyms). Earlier
cohorts (v1 causal-graph scaffold + `CausalNodeTypeEnum`; v2/v4 predicate residual; v3
classes) carried **zero** Scope-A rows because no `traitmech:` IDs existed when they were
drafted. This is the first cohort to cover them, and it covers them all.

## Scope

| Scope | # rows | Lift status |
|---|---:|---|
| A (synthetic trait classes) | **120** | this cohort |
| B (causal predicates) | 0 | handled by v2/v4; not re-opened here |
| C (schema enums) | 0 | `CausalNodeTypeEnum` already lifted in v1 |

Scope-A answer: each row was minted as `traitmech:NNNNNN` during 2026-05/06 literature
curation because METPO had no equivalent, and is in active use as the `identifier:` of one
trait record.

## Hierarchy decisions

Each row's `SC %` parent is taken from the source record's `parent_traits[0]`:

- Rows whose parent is an existing METPO class point straight at it — e.g.
  `METPO:1000059` (phenotype) for most environment/physiology/genomics leaves,
  `METPO:1000060` (metabolism) and `METPO:1000802` (anaerobic respiration) for metabolic
  processes, `METPO:1000666` (cell shape) for morphological arrangements,
  `METPO:1002005` (fermentation) for product-specific fermentations,
  `METPO:1000704`/`METPO:1000702` for flagellar/motility sub-types,
  `METPO:1000188` (quality) for genomics composition, `METPO:1004000`
  (pathogenic to host) for opportunistic pathogen.
- Rows whose parent is itself a synthetic axis (e.g. `mobile genetic element`,
  `biopolymer degradation`, `symbiosis`, `habitat association`, `intracellular inclusion`,
  `dormancy`, `stress response`, `carbon fixation`, `flagellar arrangement`,
  `dissimilatory metal reduction`, `phototrophy`/`photosynthesis`) point at that axis's
  **own proposed METPO ID in this cohort** — the in-file parent links resolve cleanly.

Aristotelian definitions are carried over from the trait records (already authored in
`<genus> in which/that <differentia>` form). `definition_source` cites the TraitMech
source file; the supporting literature DOIs/PMIDs live in each record's `evidence`.
Only `EXACT_SYNONYM` entries are emitted (per OBO convention for `hasExactSynonym`).

## ID space and subset

- **Block:** `METPO:1007600`–`METPO:1007719` (120 contiguous IDs), in trait-ID order.
  Clear of all prior cohorts (v1 `1007400`–`1007423`; v3 up to `1007505`) and of the
  CommunityMech block (`1007100`–`1007220`).
- **Subset tag:** `metpo_traitmech_2026_06`.

## Files
| File | Rows |
|---|---|
| `metpo_proposal_classes_robot.tsv` | 120 class rows (+2 header) |
| `proposal.md` | this narrative |

## Verification
`just verify-proposal metpo_traitmech_v5` → **PASS** (failures: 0): column counts (11),
parent integrity (all `SC %` resolve in-file or to known METPO IRIs), subset tag uniform,
**Scope-A coverage: all 120 traitmech IDs covered**.

## Upstream path
After TraitMech sign-off, submit the TSV to [berkeleybop/metpo](https://github.com/berkeleybop/metpo)
(or copy to `kg-microbe/mappings/`). METPO maintainers audit for existing equivalents,
mint real `METPO:` IDs, and release.

## Round-trip plan (Scope A)
Once upstream mints the real IDs: refresh `data/raw/metpo.owl`, re-seed, and swap each
record's `identifier:` from `traitmech:NNNNNN` to the new `METPO:` CURIE, preserving the
old `traitmech:` ID as a synonym for traceability. Until then the `traitmech:` IDs remain
authoritative locally.

## Change log
- v5, 2026-06: first Scope-A cohort — lifts all 120 `traitmech:000001`–`000120` synthetic
  trait classes into `METPO:1007600`–`1007719`.
