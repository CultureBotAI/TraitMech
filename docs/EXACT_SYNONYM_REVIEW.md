# Exact-synonym and ontology-grounding review

Review date: **2026-08-25**
Review branch: `codex/exact-match-synonyms`

## Scope and rule

This review covers both grounding layers without conflating them:

1. Primary `TraitRecord.identifier` / `xrefs` and the record-level scoped
   `synonyms` field.
2. Causal-node, causal-predicate, and curated mapping-table groundings.

An exact lexical match means only one of:

- the ontology canonical label (`rdfs:label` / OBO `name`); or
- a synonym explicitly asserted as `oboInOwl:hasExactSynonym` / OBO `EXACT`.

Related, broad, and narrow synonyms are excluded. Comparison performs Unicode
NFC normalization, case folding, and whitespace collapse, but does not erase
punctuation or biological qualifiers. A lexical match is still only a mapping
candidate: definitions and entity types must agree before a new xref is added.

Genes and operons are outside the scope of primary TraitRecord entries. They
may be represented only in supporting fields of an existing YAML record, such
as causal-graph nodes, protein examples, or mechanism evidence; an exact name
match to a gene or operon therefore cannot create or ground a primary trait.

## Evidence sources

The authoritative pass used direct official snapshots for METPO, GO, ChEBI,
ENVO, PATO, and RO. Versions, byte counts, source URLs, and SHA-256 checksums are
in `reports/ontology_snapshot_manifest.tsv`; the large snapshots are not
committed.

OAK sqlite adapters independently checked labels and predicate-preserving alias
relationships for every resolvable asserted grounding. OLS4 was used to
spot-check release deltas and disputed terms. In particular:

- OAK, METPO 2026-06-12, and OLS4 all return `mesophilic` as an exact synonym
  of `METPO:1000443`–`1000446` and `METPO:1000450`–`1000453`.
- OAK, GO 2026-07-26, and OLS4 all return `physiological process` as an exact
  synonym of `GO:0008150`.
- OLS4's `ontology=` filter can leak results from other ontologies, so OLS
  evidence was accepted only when the returned `obo_id` exactly matched the
  CURIE under review.
- MICRO could not be independently refreshed: its OBO PURL returned HTTP 404,
  its local OAK adapter is empty, and OLS4 returned no MICRO documents for the
  four asserted `MICRO:0001460`–`0001463` xrefs.

## Results applied

The corpus has 477 TraitRecords: 357 METPO identifiers and 120 locally minted
`traitmech:` identifiers. Before this pass it held 94 exact synonyms and eight
record-level xrefs. After review it holds:

- **128 exact synonyms** (34 added or promoted);
- **39 record-level xrefs** (31 approved mappings added);
- **50 external exact-label candidates reviewed**: 35 approved, including four
  pre-existing xrefs, and 15 rejected after definition/type comparison.

The decision ledger is `mappings/trait_exact_match_review.tsv`. Rejections are
material: identical text would otherwise have produced wrong mappings such as
microbial `acidophilic` growth to PATO's affinity for acidic histological dyes,
organism-to-chemical `imports` to an RO process-to-cargo relation, and a
cell-level catalase-positive phenotype to a GO molecular activity.

All exact synonyms declared by the current direct snapshots for non-deprecated,
exactly aligned asserted TraitRecord groundings are now present. The remaining
record-grounding audit states are:

- 336 `EXACT_COMPLETE` asserted groundings;
- 53 deprecated TraitRecords/terms retained as historical records;
- three METPO canonical-label changes (`alkaphilic` spellings) reported but not
  rewritten because the records were seeded from the committed METPO 2025-11-25
  snapshot and a source-snapshot migration is a separate operation;
- 120 local identifiers plus four unresolved MICRO xrefs with no direct source
  term available in this source set.

## Causal-grounding corrections

The direct release pass also found live obsolete or unresolvable graph terms:

- `denitrification`: `GO:0019330` (now obsolete aldoxime metabolism) was
  replaced by current `GO:0019333` denitrification pathway;
- bacterial plasmid `conjugation`: obsolete `GO:0000746` was replaced by
  `GO:0009291` unidirectional conjugation;
- `ribulose monophosphate cycle`: obsolete `GO:0019647` was retracted rather
  than replaced by broader `GO:0019649` formaldehyde assimilation, already a
  separate graph concept;
- `sulfane sulfur`: unresolved/wrong `CHEBI:15037` was retracted; ChEBI 254 and
  OLS4 expose no exact replacement.

The product label validator now uses `synonym_scope: exact`; related aliases can
no longer make an id/label pair pass. `reports/causal_grounding_exactness.tsv`
keeps semantic-but-not-lexical mappings separate from genuine exact lexical
evidence. Proposed METPO CURIEs absent from the current upstream release remain
visible as `TERM_NOT_FOUND` rather than being mistaken for synonym failures.

## Ambiguity is preserved, not hidden

Exact ontology scope does not imply unique lookup. There are 19 normalized
strings owned by multiple TraitRecords when considering primary labels plus
exact synonyms. The current METPO release makes `mesophilic` the largest
collision: it is the label of `METPO:1000615` and an exact synonym of eight
temperature-bin records. `reports/exact_synonym_collisions.tsv` records every
owner so downstream resolvers can require context instead of silently selecting
the first record.

The resolver policy is fail-closed:

1. A supplied CURIE resolves directly.
2. A string with exactly one canonical-label owner resolves to that owner.
3. Otherwise, a string with exactly one exact-synonym owner resolves to that
   owner.
4. Multiple canonical-label or exact-synonym owners are ambiguous and must not
   be reduced to a single record without additional context. Related, broad,
   and narrow synonyms never participate in exact resolution.

`just audit-exact-synonym-collisions` regenerates the exact-only collision table
without ontology downloads and compares it with the committed report. It is in
`just qc`, so any ownership change must be reviewed and committed explicitly.

## Prioritized follow-up issues

| Priority | Issue | Disposition |
|---|---|---|
| P0 | [#464 — exact-name collisions](https://github.com/CultureBotAI/TraitMech/issues/464) | Implemented on this branch: exact-only report, fail-closed resolver policy, and snapshot-free QC freshness gate. |
| P1 | [#512 — proposed METPO CURIE reconciliation](https://github.com/CultureBotAI/TraitMech/issues/512) | Needs upstream/human action: 39 proposed CURIEs account for 89 `TERM_NOT_FOUND` assertions. |
| P1 | [#514 — unresolved MICRO xrefs](https://github.com/CultureBotAI/TraitMech/issues/514) | Needs curator action: recover an authoritative source or replace/retract four unverifiable xrefs. |
| P2 | [#515 — METPO source and label refresh](https://github.com/CultureBotAI/TraitMech/issues/515) | Agent-safe migration after measuring the complete release delta; covers the three `alkaphilic` label drifts. |
| P2 | [#513 — reproducible snapshot acquisition](https://github.com/CultureBotAI/TraitMech/issues/513) | Implemented on this branch: manifest-locked download/reuse with byte-count and SHA-256 verification. |

No separate issue was filed for the 53 deprecated historical records or 120
local `traitmech:` identifiers: both are intentional corpus states rather than
ontology-resolution failures. The single PATO `light intensity` exception is
already an explicit `skos:closeMatch` with a narrowly keyed validator exception,
so it remains documented rather than being misclassified as exact-match work.

## Reproduction

After downloading the files named in `reports/ontology_snapshot_manifest.tsv`
to one directory:

```bash
just fetch-exact-synonym-snapshots /path/to/snapshots
just report-exact-synonyms /path/to/snapshots \
  --oak-dir /path/to/oaklib
just apply-trait-exact-matches /path/to/snapshots
```

The fetch command treats the manifest as a lock: it verifies byte counts and
SHA-256 digests, reuses existing verified files, and refuses to overwrite a
mismatched file. Pass `--verify-only` for a network-free replay check.

The third command is dry-run by default; append `--apply` to write approved
xrefs and synonyms. The migration is idempotent and schema-validates every
changed record before writing.
