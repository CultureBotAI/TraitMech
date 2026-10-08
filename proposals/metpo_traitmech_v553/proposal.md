# METPO proposal v553: fungal constricting-ring trap formation

## Context, scope and hierarchy

Lift `traitmech:000677` as `METPO:1063000`: one reusable morphological
phenotype, used in one new record and kept `PROPOSED` pending human review.
Scope A: one class. Scope B: zero predicates. Scope C: zero schema enums.

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
This is formation of a three-cell hyphal trapping apparatus, not the
individual-cell geometry of ring shaped `METPO:1000680`, generic mycelial
growth, hyphal anastomosis, nematophagy, or a fungal taxon. It excludes
adhesive non-constricting rings and adhesive networks. Formation includes
morphologically complete immature rings; maturation and inflation are
separate readouts. No exact existing node, synonym or TODO needs repair.
Closer-parent interpretation remains open. No synonyms, xrefs, SSSOM
equivalences, or organism-level disjointness are asserted.

## Evidence and limits

- [Chen et al. 2023](https://doi.org/10.1038/s41467-023-43235-w): primary XML,
  developmental Results, relevant Methods and actual Figure 1 distinguish
  formation, maturation and inward inflation. Immediate inflation competence
  is not inferred from a complete ring. The protein-resolved mechanism is
  deferred pending remaining perturbation figures, supplements and accessions.
  Wild-type strain 29 is qualified evidence, not a provenance-verified natural
  canonical example.
- [Zhang et al. 2022](https://doi.org/10.3897/BDJ.10.e96642): primary XML,
  isolation/induction Methods, taxon descriptions and actual Figure 1e document
  soil-isolated fungi producing constricting rings. Published 16 December 2022,
  despite the 2023 PubMed indexing context. The natural-isolate example is
  CGMCC3.20131, source-named Drechslerella daliensis. Live `NCBITaxon:2743661`
  resolves to **Drechslerella daliensis (nom. inval.)**, rank species. Preserve
  that nomenclatural caveat; this proposal does not validate the fungal name.

The two positive trait studies have directly checked contiguous snippets. The canonical
example is culture/condition-qualified. No universal induction medium, rapid
inflation timing, native protein dependency or field biocontrol efficacy is
asserted. Scientific hierarchy/mechanism discussions remain OPEN.

Adversarial review [#1823](https://github.com/CultureBotAI/TraitMech/issues/1823)
found that the initial label also fits intracellular constricting rings in
fungal cytokinesis. The corrected label adds **trap**, without changing the
definition, identifier or filename. [Stachowiak et al. 2014](https://doi.org/10.1016/j.devcel.2014.04.021),
read directly at PMC4137230 and via its scientific abstract, is a third
evidence item solely for this terminology boundary, not a third positive
trap study. Its contiguous snippet supports the explicit exclusion of
cytokinetic actomyosin rings. Both curation histories preserve the initial
event and append the correction.

## Allocation and novelty

Reserve local **traitmech:000677**, cohort **v553**, and the entire
**METPO:1063000-1063099** block; only 1063000 is populated. This follows
v552's 1062900-1062999 block and does not overlap CommunityMech v1.
Subset: `metpo_traitmech_2026_10`.

Allocation main: `95179adbd0c13c2ca24e25cb160105cc92444544`.
Ignored-and-hidden searches covered all 20 then-existing TraitMech worktrees,
the entire CommunityMech checkout and a fresh open-PR curation snapshot:
22 roots. Searches included constricting/ring-trap/nematode-trapping variants,
Drechslerella, Arthrobotrys, both DOI/PMIDs, local ID, cohort and the full
hundred block. All returned matches were inspected: numeric cache fixtures,
an unrelated OWL string/tetrapolar lexical match, bacterial entrapment and a
CommunityMech cached reference to Arthrobotrys prey attraction are not exact
traits or reservations. No exact record or reservation was found. The parsed
12,617-triple pinned METPO ontology has no exact class. A fresh 399-record seed
projection has 55 exact IDs absent from the 1,071-record live corpus, none an
exact constricting-ring term; that projection is not a curation queue.

Complete paginated open-head inventory, including drafts, at allocation:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

File counts, immutable selected curation blobs and before/after head stability
were checked. Recheck main and reservations immediately before publication.

## Artifacts and verification

One class TSV contains two 11-column headers and one class row; `proposal.md`
is the narrative. No property or SSSOM file is needed. Preserve the three
empty trailing ROBOT directive cells. The upstream skill and templates at
`1408e7099d039026d7611c240938d8e177753406` were directly retrieved. Class blob
`b590cf303dc2fbdd57bed021668641cd0c32396d` and property blob
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` have 11/13-column headers.
Use the maintained w3id METPO prefix, not the upstream example's legacy OBO stub.

Required verification: maintained proposal verifier, ROBOT template/merge/ELK,
parsed OWL parent identity, strict/LinkML validation, history/QC/product gates,
snippet verification with direct-source fallback, live NCBI example resolution,
writer and full tests, and generated browser/dashboard inspection. Actual
results are recorded in the PR validation receipt, not presumed here.

## Upstream and round trip

After human signoff, submit the TSV to berkeleybop/metpo. No separate upstream
issue or accepted METPO ID is claimed. After upstream release, refresh the
pinned ontology, re-seed the accepted class, migrate this identifier to its
accepted METPO CURIE and preserve the local identifier in migration provenance.
Do not emit the reserved proposal ID as an already released ontology term.

## Change log

- v553, 2026-10-08: first proposal; trap-qualified label corrects #1823.
