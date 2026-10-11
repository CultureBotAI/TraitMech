# METPO proposal v575: periplasmic bacterial predation

## Context and scope

Lift `traitmech:000699` to placeholder `METPO:1065200`: one reusable
ECOLOGY CLASS, PROPOSED pending human signoff. It denotes a feeding
phenotype, not an interaction instance, taxon, gene or sequence signature.

| Scope | Parent | New classes | Properties |
| --- | --- | ---: | ---: |
| A: local trophic phenotype | predatory bacterium `METPO:1007653` | 1 | 0 |
| B/C: predicates/schema | Not included | 0 | 0 |

## Hierarchy and boundaries

The TraitRecord parent is `traitmech:000054`, predatory bacterium. Its v5
placeholder `METPO:1007653` is repeated unchanged for a standalone proposal,
below phenotype `METPO:1000059` and quality `METPO:1000188`; it is not a new
identifier or a second reservation. The new differentia is prey-periplasm
entry with nutritional growth and reproduction there.

The existing parent's `intraperiplasmic_growth` node is a lifecycle stage,
not the complete feeding phenotype. It is not an exact grounding candidate
for the new term. The parent graph already qualifies its invasive branch
to B. bacteriovorus. No existing TraitRecord is edited. Epibiotic bacterial
predation `traitmech:000697` has an external predator cell body; generic
intracellular predation can include other locations. Endoparasitism and
endosymbiosis are not asserted exact synonyms. No organism-level disjointness,
universal prey range, fixed division pattern or obligate dependence is added.
No exact xref, synonym or protein-resolved graph is proposed.

## Evidence and limits

- [Lai et al. 2025](https://doi.org/10.1038/s42003-025-09010-x),
  PMID:41125861, PMC12546842: definition source. The short quotation is
  from the Introduction, not the scientific Abstract. Publisher HTML and
  full-text XML agree. Selected Results, Methods and Discussion and actual
  Figures 1/4 were read. The lifecycle schematic is not experimental imaging.
- [Fenton et al. 2010](https://doi.org/10.1128/JB.00914-10),
  PMID:20935099: scientific Abstract supports prey-derived replication.
  Full text, actual figures and supplement were inaccessible. The MED link
  is a commentary, not a correction; publisher notice status is inaccessible.
- [Burnham et al. 1968](https://doi.org/10.1128/jb.96.4.1366-1381.1968),
  PMID:4879563: directly read scientific Abstract supports the entry-location
  interpretation, not permanent prey-membrane integrity or nutrient tracing.
  Full text/figures were unavailable and publisher notice status unverified.

Each evidence item has a short, contiguous source quotation. Direct matching
is separate from the native abstract resolver's outcome. Retrieved MED
records and the accessible 2025 publisher page exposed no linked correction
or retraction; this is not proof that none exists. The 2025 linked preprint
is not counted as an independent paper. The 2023 cryo-ET paper is a research
lead already cited by the parent; its full text was not obtained in this
cycle, so no new full-text claim is imported from it.

The canonical example is wild-type `NCBITaxon:264462`, Bdellovibrio
bacteriovorus HD100, independently verified at NCBI including strain rank
and its DSM 50701 synonym. The [DSMZ collection entry](https://webshop.dsmz.de/en/bacteria/Bdellovibrio-bacteriovorus.html)
supports natural soil-isolate provenance, not another feeding experiment.
The laboratory prey and engineered derivatives in the papers are not
silently generalized to field predation or to every HD100 derivative.
Exact mappings and protein/taxon-grounded mechanisms remain open discussions.

## ID space, subset and novelty

Reserve `traitmech:000699`, cohort v575 and the complete
`METPO:1065200-1065299` block; populate only 1065200. Subset:
`metpo_traitmech_2026_10`. Allocation base:
`bd802f4c1aef68578ef56fc1dfb2f09109797e8d`.

The 2026-10-11 14:16 UTC audit searched all 22 pre-existing TraitMech roots,
including ignored/hidden files and binary-as-text matches, for candidate
labels, citations, taxa, the local ID, cohort and full block. It inspected
574 cohorts and 4,082 narrative interval occurrences. The closest mentions
were the broad parent, its stages, sibling evidence and research leads,
not an exact record or an unresolved exact trait node. The 2010 citation
was additionally searched across the same roots after source selection.

All 127 registered CommunityMech roots were inventoried without modification;
530 extant proposal files had no block conflict. CommunityMech v1's
`METPO:1007131` is a broader interaction, not an organismal phenotype or
an equivalent. The reserved block is outside its existing blocks.

Fresh main heads verified immutable upstream snapshots: CommunityMech
`80049bcc9195480a58633236169b62f86c23489a`, METPO
`1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, and kg-microbe
`1408e7099d039026d7611c240938d8e177753406`. All reused source bytes were
checked by SHA-256 and Git blob SHA. Freshly retrieved METPO all-state
issue/PR bodies (644) and issue comments (654) had no candidate/block hit.

Fresh temporary seeding yielded 399 records, 344 already present among
1,093 live records. The 55 absent IDs remain leads, not a missing-work queue.
The frozen 1,546-row release table, 153-row active review and policy were
reconciled with live data/history; none supplied this candidate. No exact
term appeared in the pinned or inspected current METPO sources.

Complete paginated changed-file lists and immutable heads were checked for
all open PRs, including drafts:

| TraitMech PR | Head | Reservation |
| --- | --- | --- |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

CommunityMech draft #935 and METPO PRs #644, #643, #641, #640, #638 and
#629 were also checked without a candidate/block conflict. Recheck before
publication. Searches do not follow symlink directories, decode compressed
archives or inventory unregistered work. This is bounded candidate discovery,
not exhaustive microbial-trait discovery.

The add-trait skill covers this addition without a further update.

## Files and verification

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | Two headers, reused parent and new child, 11 columns |
| `proposal.md` | Scope, evidence, allocation and round trip |
| Properties/SSSOM | Not emitted: no predicate or established equivalence |

Pinned upstream class/property headers were checked at the kg-microbe
commit above (blobs `b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`). Preserve required trailing
directive cells and use w3id METPO IRIs, not legacy OBO stubs.

The dry-run-first writer prevalidates and guards parent projection and
target/proposal drift. Required checks include LinkML/strict/history,
proposal/ROBOT/ELK, snippets, live taxonomy, QC/products, focused/full tests,
preservation, rendered pages and immutable scientific review. Actual
outcomes belong in the PR and saved review, not an assumed pass here.

## Upstream and round trip

After human signoff, submit the TSV to berkeleybop/metpo. No upstream issue
or acceptance is claimed. After official minting, refresh the ontology,
migrate identifier/references, retain `traitmech:000699` as a provenance
synonym and preserve append-only history without duplicating the record.

## Change log

- v575, 2026-10-11: propose periplasmic bacterial predation.
