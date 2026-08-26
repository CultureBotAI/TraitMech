# METPO 2026-06-12 active-addition and field-drift review

Issues: [#515](https://github.com/CultureBotAI/TraitMech/issues/515),
[#534](https://github.com/CultureBotAI/TraitMech/issues/534)

## Decision

The 94 active additions and 59 non-target field deltas held by the initial
release migration have now been classified. No new primary TraitRecord is
created and no reviewed local field is overwritten merely because it changed in
the ontology source.

Final dispositions remain in the complete
[`release-delta inventory`](../reports/metpo_2026_06_12_release_delta.tsv); the
compact [`active-review table`](../reports/metpo_2026_06_12_active_review.tsv)
records the 153 row-level rationales and related TraitRecord CURIEs. They are
reproducibly applied by
`scripts/finalize_metpo_2026_06_12_review.py`, which is dry-run by default.

| final disposition | rows |
|---|---:|
| supporting-field vocabulary (datatype/object properties) | 38 |
| out-of-scope non-trait material entity | 1 |
| duplicate or near-duplicate of an existing primary record | 17 |
| active class with no demonstrated corpus need | 38 |
| retain curated local synonyms | 31 |
| retain curated local definition after semantic source rewrite | 8 |
| retain local scientific typography or grammar | 12 |
| retain curated local hierarchy | 8 |

## Primary-entry scope

TraitMech is a curated microbial-trait catalog, not a mirror of every METPO
class and property. Ontology membership alone is not evidence of a corpus need.
The 38 unselected classes include biochemical tests, colony morphologies, and
other plausible future vocabulary; they can be reconsidered when a concrete,
evidence-backed use case exists.

Genes and operons are out of scope as primary entries. They may occur in
supporting YAML fields. None of the 56 active class additions is a gene or
operon class. The two gene-count additions are datatype properties and are
classified as supporting-field vocabulary, not primary TraitRecords.

## Duplicate handling

Seventeen source classes overlap existing reviewed entries, including
denitrification, nitrogen fixation, flagellar arrangement and four arrangement
subtypes, pressure/radiation/metal tolerance, capsule, biofilm formation,
three diagnostic enzyme-activity positives, and xerophily. The report names the
related TraitRecord CURIE. They are not automatically added as `xrefs`: a new
source CURIE is not by itself proof of exact semantic equivalence, and adding a
second primary record would create the duplication this review is preventing.

## Existing-field handling

The synonym deltas are retained locally because they consist of redundant
canonical labels, over-broad phenotype labels on numerical bins, rotated GC-bin
aliases, or typography-only substitutions. Twelve definition changes remove
scientific typography (for example O₂ and °C) or introduce no improvement.

Eight definition rewrites and eight paired parent changes are semantically
meaningful, but the local records are already `REVIEWED` and cite their own
definition sources. Changing their hierarchy would alter inference. The review
therefore records an explicit decision to retain the curated local model rather
than treating upstream prose or hierarchy as automatically authoritative.
