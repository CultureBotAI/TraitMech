# METPO proposal v574: ixotrophy

## Context and scope

Lift `traitmech:000698` to placeholder `METPO:1065100`: one reusable
ECOLOGY CLASS, PROPOSED pending human signoff. This is a feeding phenotype,
not an interaction instance, secretion-system gene or sequence profile.

| Scope | Parent | Classes | Properties |
| --- | --- | ---: | ---: |
| A: local trophic phenotype | phenotype `METPO:1000059` | 1 | 0 |
| B/C: predicates/schema | Not included | 0 | 0 |

## Hierarchy and boundaries

Use phenotype `METPO:1000059`, below quality `METPO:1000188`.
The definition combines filamentous bacterial surface capture, prey killing
and nutritional uptake. Capture is a capability, not a required sequence in
every encounter: the 2024 model also contacts prey by gliding on solid media.
Neither adhesion, gliding nor antagonism alone establishes this phenotype.

Predatory bacterium `traitmech:000054` requires bacterial prey, whereas the
ixotrophy literature includes nonbacterial microbes. Epibiotic bacterial
predation `traitmech:000697` requires attached external growth on bacterial
prey. Neither is established as a broader parent at this scope. The 2026
Heng et al. abstract (DOI:10.1007/s00248-026-02864-6) calls ixotrophy epibiotic
in a broader sense; this attributed terminology is not silently equated with
the narrower existing record. No organism-level disjointness is asserted.
No exact xref, synonym or protein-resolved graph is proposed.

## Evidence and limits

- [Lien et al. 2024](https://doi.org/10.1126/science.adp0614), PMID:39418385:
  direct experimental uptake evidence; scientific abstract distinguished
  from the separate article summary. Selected Methods, Results, Discussion
  and actual Figures 1, 5 and 6 inspected; other figures, supplements and
  movies not fully assessed. Author-hosted published PDF read.
- [Lewin 1997](https://doi.org/10.1007/s002489900052), PMID:9337418:
  publisher abstract supports capture, killing and nutrition in Saprospira.
  Full text unavailable; MED supplied metadata without an abstract.
- [Furusawa et al. 2015](https://doi.org/10.1099/mic.0.000158), PMID:26306656:
  direct scientific abstract supports adhesion/capture, not direct nutrient
  tracing. Full-text delivery failed; no unread Methods claims imported.

All three evidence entries carry short contiguous quotes. Preserve actual
resolver outcomes separately from manual source checks. The 2015 and 2024
papers overlap in authors and CCB-QB1 material, not independent-group
replication. No linked correction/retraction appeared in the retrieved MED
records or accessible publisher pages; the Science publisher status page
was inaccessible, which limits that check. No universal molecular mechanism,
prey range, flagellum dependence or obligate feeding requirement is asserted.

`NCBITaxon:1313421` independently resolves as Aureispira sp. CCB-QB1.
The example is qualified to ixotrophy-positive WT, not IS-inactivated
derivatives. The primary abstract at PMID:25468060,
DOI:10.1016/j.margen.2014.10.006, establishes coastal Penang isolate provenance;
it is not counted as a fourth predation experiment. The 2026 abstract is
terminology context only. Exact mappings and protein/taxon grounding remain
explicit open discussions.

## ID space, subset and novelty

Reserve `traitmech:000698`, cohort v574 and the complete
`METPO:1065100-1065199` block; populate only 1065100. Subset:
`metpo_traitmech_2026_10`. Allocation base:
`082bccd52ed185b8331020f3c6592764a4b5b4fd`.

The 2026-10-11 12:55 UTC audit searched all 22 pre-existing TraitMech roots,
including ignored/hidden files and binary-as-text matches, for candidate
labels, citations, taxa, the local ID, cohort and full block. It inspected
573 cohorts and 4,081 narrative interval occurrences. The only relevant
scientific mentions were research leads and rendered copies, not an exact
curated record or unresolved exact node. Other grappling-hook hits describe
twitching, not predation. Existing records remain unchanged.

All 127 registered CommunityMech roots were inventoried without modifying
them; 530 extant proposal files, including root-level documents, had no
conflict. Empty/prunable registrations were not treated as live checkouts.
The block is outside CommunityMech v1 and its extensions.

Fresh main heads verified immutable upstream snapshots: CommunityMech
`80049bcc9195480a58633236169b62f86c23489a`, METPO
`1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, and kg-microbe
`1408e7099d039026d7611c240938d8e177753406`. Reused snapshot bytes were
checked by SHA-256 and Git blob SHA, then searched for this candidate and
reservation. METPO's 644 all-state issue/PR bodies and 654 issue comments
were freshly retrieved and contained no matching reservation or candidate.

Temporary seeding yielded 399 records, with 344 identifiers already present
among 1,092 live records; the 55 absent IDs are leads, not a missing-work queue.
The 1,546-row frozen release table, 153-row active-review table and policy
were reconciled with live data/history; none has an ixotrophy candidate.
No exact term was found in pinned or inspected current METPO sources.

Complete paginated changed-file lists and immutable heads were checked for
all open PRs, including drafts. They match the previously inspected snapshots:

| TraitMech PR | Head | Reservation |
| --- | --- | --- |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

CommunityMech draft #935 and METPO PRs #644, #643, #641, #640, #638 and
#629 were also checked with no candidate/block conflict. Recheck before
publication. Searches do not follow symlink directories, decode compressed
archives or inventory unregistered work. This is bounded candidate discovery,
not proof that all microbial traits have been exhausted.

The add-trait skill's current scope, sequence-interpretation, notice-check,
provenance and review rules cover this addition; no skill change is needed.

## Files and verification

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | Two headers, one class, 11 columns |
| `proposal.md` | Scope, evidence, allocation and round trip |
| Properties/SSSOM | Not emitted: no predicate or established equivalence |

Upstream headers were checked at the kg-microbe commit above, class blob
`b590cf303dc2fbdd57bed021668641cd0c32396d`, property blob
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`. Required trailing directive
cells remain. Use w3id METPO IRIs, not legacy OBO stubs.
The writer defaults to dry run, prevalidates, guards parent projection and
target/proposal drift, and supports exact replay without changing the parent.

Required checks: LinkML/strict/history, proposal/ROBOT/ELK, snippets, live
canonical taxonomy, QC/products, focused/full tests, preservation, rendered
pages and immutable scientific review. Actual outcomes belong in the PR
and saved review, not an assumed pass here.

## Upstream and round trip

After human signoff, submit the TSV to berkeleybop/metpo; no upstream issue
or acceptance is claimed. After official minting, refresh the ontology,
migrate identifier/references, retain `traitmech:000698` as a provenance
synonym, and preserve append-only history without duplicating the record.

## Change log

- v574, 2026-10-11: propose ixotrophy.
