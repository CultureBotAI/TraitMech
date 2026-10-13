# Enhanced Transcriptional Reactivation Memory

## Scope And Definition

One Scope-A physiological CLASS, `traitmech:000713`, proposed as
`METPO:1066600`: **enhanced transcriptional reactivation memory**.

A physiological phenotype in which a microbial cell or lineage retains a
non-genetic state from prior inducing conditions that enhances the rate or
magnitude of later transcriptional activation after intervening repression.

The definition concerns a history-dependent response under matched later
test conditions, not a gene, regulatory site, chromatin mark, persistent
reporter, ongoing expression, or a growth/resistance endpoint alone. It does
not require identical first and second stimuli, a fixed duration, universal
mitotic inheritance, or a common molecular mechanism. Transcript abundance
kinetics support the operational endpoint but do not directly measure
initiation rate or alone separate synthesis from degradation.

The record remains `PROPOSED`. No canonical natural taxa, causal graph,
protein examples, exact synonyms or external equivalence mappings are added.
No SSSOM file is emitted because no semantic cross-ontology alignment is
asserted. The pinned ontology and all existing records are unchanged.

## Primary Evidence

1. [Sump et al. 2022](https://doi.org/10.7554/eLife.77646), PMID:35579426,
   PMC9129879. Selected Results/Methods and actual Figure 1 support faster
   INO1 reactivation in the synthetic Opi1 Anchor-Away context (1D), not
   clearly faster ordinary-starvation reactivation (1B). Figure 1 supplement
   1C separately concerns CHO1/ACT1 after three-hour repression; its generic
   significance comparator is ambiguous. The 18-hour localization assay
   (supplement 2E) and competitive fitness panel (1G) have different endpoints.
2. [D'Urso et al. 2016](https://doi.org/10.7554/eLife.16691), PMID:27336723,
   PMC4951200. Figure 7A compares selected mRNA responses after salt exposure,
   two-hour recovery and peroxide challenge. The quoted Results sentence
   attributes its gene count and four-generation duration to Guan 2012;
   that duration is not measured by Figure 7A. Actual 7B/C/D contents conflict
   with their caption assignments; the discrepancy remains explicit.

Two distinct publications do not establish independent-laboratory replication:
these papers share the Brickner research lineage. Laboratory/engineered strain
contexts do not establish species-wide natural exemplars. Selected strain-table
rows were read, not a complete rendered supplement audit. The CHO1 locator and
HTA1-mCherry/Pho88 source discrepancies remain unresolved.

Both short snippets are contiguous Results spans directly matched in primary
XML and publisher Version-of-Record HTML. Native DOI/abstract verification
returns `NOT_IN_ABSTRACT`, not `VERIFIED`; the separate full-text match is the
supporting check. No snippet baseline exception is introduced. Scientific
abstracts were read separately. Selected text/caption agreement after Unicode
and whitespace normalization is not whole-article version equality; limited-
resolution figure inspection is not numerical or raw-data reanalysis.

Source URLs, hashes, quote locations, canary verdicts, figure acquisitions,
strain provenance, acceptance and reservation receipts are in
[`enhanced_transcriptional_reactivation_memory-source-verification.json`](../../research/traits/physiology/enhanced_transcriptional_reactivation_memory-source-verification.json).
Bounded publisher, qualified MED and Crossref notice checks exposed no linked
correction or retraction on 2026-10-12; this is not proof of notice absence.

## Identity And Hierarchy

The conservative parent is `METPO:1000059` phenotype, whose reviewed identity,
definition, provenance, category, kind, status and parents are checked before
writing. Carbon-source memory (`traitmech:000706`) spans induction and growth
and is not reparented wholesale. Memory of acquired stress resistance
(`traitmech:000712`) requires retained resistance, not enhanced transcription.
Anticipation, bet hedging and unqualified epigenetic memory are not exact
equivalents. Existing nearby discussion mentions qualify nonequivalence;
they are not exact ungrounded causal nodes or misplaced synonyms to migrate.

Pinned and inspected current METPO graphs contain deprecated lexical
neighbors `METPO:1000108` epigenetic modification and `METPO:1000310`
transcription factor, below ObsoleteClass, without replacement/consider
annotations in those graphs. Their OMO:0001000 reason means out of scope,
but the mechanical assignment is disputed in
[METPO issue 521](https://github.com/berkeleybop/metpo/issues/521).
Original historical definitions and parent axioms remain unassessed.
Historical labels do not prove exact equivalence or nonequivalence.

This separately defined assayable phenotype is accepted from positive primary
evidence, not merely because those labels are deprecated. No old identifier is
revived and no historical exact mapping is asserted. The open identity TODO
records that limitation. This is not an ontology refresh or a sequence-feature
record.

## Novelty And Reservation

The decision was made at `2026-10-13T00:34:29Z` against main
`62f45e1749fa3d3e5ca8b9a3a4ba5bb0361beb8b` after PR #1900's complete lifecycle.
Ignored and hidden available files were included, with 22 registered locations,
18 retained historical tracked trees and nine completed independent copies.
Historical regex behavior had a known-positive control. Normalized semantic
review covered 1,122 distinct YAML versions and nine matching trait identities;
none defined this exact endpoint. These are bounded checks, not a global
absence claim.

Fresh paginated open/draft PR manifests and hash-checked complete nonremoved
changed blobs cover TraitMech #1782, #1476, #973 and draft #924, CommunityMech
draft #935, and METPO #644, #643, #641, #640, #638 and #629. Changed-file
manifests and heads remained stable. Unchanged PR tree files, comments and
deleted historical blobs are outside this scan. Gzip embedding content was
decoded and parsed, not treated as a textual patch.

Current upstream selected ontology/template, proposal and mapping snapshots:

- METPO: `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- CommunityMech: `88050e999dd5699d08456f7f6495505618d6ead6`.
- KG-Microbe: `f54598d5c289f72fb954fcd06c38a2d3b608a3be`.

Allocation checked 588 cohorts, 8,742 interval occurrences and 127 registered
CommunityMech locations plus available historical proposals. The eight broad
editor-namespace hits, including repeated v587 documentation, were individually
hash/context checked as envelopes rather than exclusive reservations. The
only literal candidate-number hit was `1.1066657` in draft #924's embedding
table, line 120, field `d459`, for `METPO:2000001`; structured parsing confirms
it is a coordinate, not a reserved identifier. Narrower ranges remained
checked. No conflicting reservation remained in the inspected scope.

Unavailable ignored/untracked historical bytes cannot be reconstructed.
Symlink directories were not traversed and arbitrary archives were not
expanded. Reservation checks must be refreshed before publication and cannot
eliminate concurrent-allocation races.

## ID Space And Validation

- Local identifier: `traitmech:000713`.
- Cohort: `metpo_traitmech_v589`.
- Full reserved block: `METPO:1066600`-`METPO:1066699`.
- Only populated placeholder: `METPO:1066600`, not a released identifier.
- Subset: `metpo_traitmech_2026_10`.

The one-row class template preserves the canonical 11-column two-row header,
including three trailing blank ROBOT directive cells. The guarded writer
defaults to dry run, prevalidates before either output, permits identical
replay and refuses parent, target or proposal drift. Both DOI references are
definition provenance, not ontology equivalence mappings.

Required gates include strict/schema checks, final-record snippet resolution,
proposal verification and ROBOT/ELK with RDF round-trip assertions, generated
artifact freshness, repository QC, full tests, both histories and an immutable
scientific review. A passing mechanical gate does not resolve the stated
scientific limitations. Discovery remains active, not exhausted.
