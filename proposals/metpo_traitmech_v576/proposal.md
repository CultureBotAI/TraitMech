# METPO proposal v576: cytoplasmic bacterial predation

## Context and scope

Lift `traitmech:000700` to placeholder `METPO:1065300`: one reusable
ECOLOGY CLASS, PROPOSED pending human signoff. This is a feeding phenotype,
not a taxon, an interaction instance, a gene or a sequence signature.

| Scope | Parent | New classes | Properties |
| --- | --- | ---: | ---: |
| A: local trophic phenotype | predatory bacterium `METPO:1007653` | 1 | 0 |
| B/C: predicates/schema | Not included | 0 | 0 |

## Hierarchy and boundaries

The TraitRecord parent is `traitmech:000054`, predatory bacterium. Its v5
placeholder `METPO:1007653` is repeated unchanged for standalone reasoning,
below phenotype `METPO:1000059` and quality `METPO:1000188`. It is not a
new identifier or a second reservation. The differentia is destructive
feeding and reproduction within the bacterial prey cytoplasm.

Periplasmic bacterial predation `traitmech:000699` and epibiotic bacterial
predation `traitmech:000697` differ in predator location. The parent's
intraperiplasmic-growth node is a lifecycle stage, not this whole trait.
No existing record is edited. Generic intracellular predation,
endoparasitism and endosymbiosis are not exact synonyms. The 1986 paper's
discussion of predator/parasite and primary-consumer terminology is retained
in the new record's scope discussion, not silently treated as settled.
No organism-level disjointness, fixed prey range or obligate dependence is
asserted. Synonyms, exact xrefs and a causal graph are deferred.

## Evidence and limits

- [Guerrero et al. 1986](https://doi.org/10.1073/pnas.83.7.2138),
  PMID:11542073, PMC323246, is the primary definition source. The full
  five-page paper was directly read and Figure 2E/F and its continued
  caption visually inspected. The snippet is from the caption on p. 2141,
  not the scientific abstract. Microscopy is not nutrient tracing or a
  live-cell time course; Figure 3 is a schematic.
- [LPSN Daptobacter](https://lpsn.dsmz.de/genus/daptobacter), permanent
  [record 684](https://doi.org/10.83108/rn.684), supplies terminology and
  nomenclatural context. Its snippet quotes Madigan et al. 2019, whose
  book was not independently read. This is explicitly secondary evidence,
  not a second experiment or modern replication.

These are two distinct citable sources, not two independent experimental
studies. Both short snippets were checked against directly retrieved text.
The primary scientific abstract was separately verified using a qualified
MED query and matching PMID, title and DOI. MED and Crossref exposed no
linked notice; publisher notice access returned 403, so its correction or
retraction status remains unverified. The full-text XML route failed, but
the Europe PMC PDF was accessible. Native resolver outcomes are reported
separately from the manual full-text check.

No NCBITaxon identity for the historical material has been established in
this curation. Canonical examples are therefore omitted rather than
inventing an identifier. LPSN marks the name not validly published; its
placement is not sequence-based identity evidence. Exact mappings,
modern replication and a protein-resolved mechanism remain open discussions.

## ID space, subset and novelty

Reserve `traitmech:000700`, cohort v576 and the full
`METPO:1065300-1065399` block; populate only 1065300. Subset:
`metpo_traitmech_2026_10`. Allocation base:
`0d9feeda54221644b56d07d4a5fbf99956cd0704`.

The 2026-10-11 15:30 UTC audit included ignored/hidden files and
binary-as-text matches across all 22 pre-existing TraitMech worktrees.
It checked labels, candidate synonyms, citations, the local ID, cohort
and full block, including 575 cohorts and 4,083 narrative intervals.
The lexical hits concerned periplasmic evidence and unrelated cytoplasmic
features in research; none was an exact record or same-scope unresolved
trait node. PMID:11542073 was additionally searched after source resolution.

All 127 registered CommunityMech roots and 530 extant proposal files were
checked without modification or block conflicts. CommunityMech v1's
`METPO:1007131` is a broader interaction, not the organismal phenotype.
The new block does not overlap its reservations.

Fresh main heads verified immutable upstream snapshots: CommunityMech
`80049bcc9195480a58633236169b62f86c23489a`, METPO
`1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, and kg-microbe
`1408e7099d039026d7611c240938d8e177753406`. Reused source bytes were
verified with SHA-256 and Git blob SHA. Fresh METPO all-state issue/PR
bodies (644) and issue comments (654) had no candidate or allocation hit.

A fresh temporary seed produced 399 records, 344 already present among
1,094 live records; its 55 absent identifiers are leads, not an add queue.
The frozen 1,546-row release table and 153-row active review were reconciled
with live data/history. They did not supply this candidate. No exact term
appeared in the pinned or inspected current METPO sources.

Complete paginated changed-file lists and immutable heads were checked for
all open PRs, including drafts:

| TraitMech PR | Head | Reservation |
| --- | --- | --- |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

CommunityMech draft #935 and METPO PRs #644, #643, #641, #640, #638 and
#629 were also checked without candidate/block conflicts. Recheck before
publication. Searches do not follow symlink directories, decode compressed
archives or inventory unregistered work. This is bounded candidate discovery,
not exhaustive microbial-trait discovery.

The existing add-trait skill covers this addition without another update.

## Files and verification

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | Two headers, reused parent and new child, 11 columns |
| `proposal.md` | Scope, evidence, reservations and round trip |
| Properties/SSSOM | Not emitted: no predicate or established equivalence |

Pinned upstream headers were checked at the kg-microbe commit above.
Preserve trailing directive cells and the `https://w3id.org/metpo/` IRIs.
The dry-run-first writer guards parent projection and existing target and
proposal content. Required checks include LinkML/strict/history, proposal,
ROBOT/ELK, snippets, QC/products, focused/full tests, corpus preservation,
rendered pages and immutable scientific review. Actual outcomes belong in
the PR and review rather than an assumed pass here.

## Upstream and round trip

After human signoff, submit the TSV to berkeleybop/metpo; no upstream issue
or acceptance is claimed. After official minting, refresh the ontology,
migrate identifier/references and retain `traitmech:000700` as a provenance
synonym while preserving history and avoiding a duplicate record.

## Change log

- v576, 2026-10-11: propose cytoplasmic bacterial predation.
