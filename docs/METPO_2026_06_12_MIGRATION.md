# METPO 2026-06-12 source migration review

Issue: [#515](https://github.com/CultureBotAI/TraitMech/issues/515)

## Outcome

TraitMech now pins the hash-verified METPO 2026-06-12 snapshot and migrates the
three active canonical-label changes that triggered the review:

| CURIE | old label | new label |
|---|---|---|
| `METPO:1003002` | alkaphilic | alkaliphilic |
| `METPO:1003004` | obligately alkaphilic | obligately alkaliphilic |
| `METPO:1003005` | facultatively alkaphilic | facultatively alkaliphilic |

The migration also updates each record's grounded TRAIT-node label. For
`METPO:1003004`, it adopts the release's revised definition and parent
(`METPO:1003002`). Stable filenames, graph/node identifiers, verbatim evidence,
and old curation events are intentionally unchanged. Synonyms are rebuilt from
the release at their declared scope; an old canonical spelling is not invented
as a synonym when METPO does not declare it.

## Full release measurement

The machine-readable inventory is
[`reports/metpo_2026_06_12_release_delta.tsv`](../reports/metpo_2026_06_12_release_delta.tsv).
It compares the prior 2025-11-25 bytes (SHA-256
`b64c91ec876d468492ba5c43d8a47f1ec535d6031f86b591917726422b6ae790`)
with the locked 2026-06-12 bytes (SHA-256
`8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415`).

| measurement | count |
|---|---:|
| numeric METPO entities, old → new | 357 → 1,619 |
| added entities | 1,262 |
| removed entities | 0 |
| added entities explicitly deprecated | 1,168 |
| active additions held for review | 94 |
| entities in the new snapshot marked deprecated | 1,216 |
| field deltas on the 357 existing entities | 284 |

Existing-entity field deltas are: 51 labels, 47 definitions, 54 parent sets,
31 synonym sets, 26 domains, 26 ranges, 48 deprecation flags, and one creator.
The TSV records every addition and field delta with its disposition.

## Scope decisions

- The seeder now reads `owl:deprecated` and excludes all 1,216 retired
  entities. Before this guard, the refreshed source would have proposed 1,615
  records, most of them obsolete legacy terms.
- No new primary TraitRecords are generated in this source migration. The 94
  active additions require a separate duplicate/category review; several
  overlap current records under new CURIEs (for example denitrification).
- Genes and operons remain out of scope as primary entries. They may occur only
  in supporting YAML fields. The active-addition inventory contains no gene or
  operon class proposed for primary seeding; gene-count entries are datatype
  properties, not gene entities.
- Forty-seven source-deprecated records were already locally marked
  `DEPRECATED`; their historical display labels and metadata are retained.
- METPO now also deprecates `METPO:1001000` (observation), while TraitMech has a
  deliberately reviewed upper record and graph for it. That policy conflict is
  deferred to a curator rather than silently changing the local record.
- The other 59 active, non-target source-field deltas are measured in the TSV
  but do not overwrite reviewed local definitions/hierarchy automatically.

## Reproducibility and safeguards

`scripts/refresh_metpo_source.py` replaces the stale sibling-copy recipe. It
downloads the manifest-locked snapshot, verifies byte count and SHA-256, and
installs atomically; the command itself is dry-run by default.

`scripts/migrate_metpo_2026_06_12.py` is also dry-run by default. It validates
the source lock, checks expected old/new values, writes through TraitRecord
validation, records per-record curation provenance, and is idempotent.

The refreshed source is retained for resolution and historical interpretation;
its presence is not authorization to seed every entity it contains.
