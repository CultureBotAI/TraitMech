# METPO proposal v577: collective bacterial predation

## Context and scope

Lift `traitmech:000701` to placeholder `METPO:1065400`: one reusable
ECOLOGY CLASS, PROPOSED pending human signoff. It describes coordinated
group feeding by bacterial cells, not an interaction instance, taxon,
gene, sequence signature or experimental segmentation bin.

| Scope | Parent | New classes | Properties |
| --- | --- | ---: | ---: |
| A: local trophic phenotype | predatory bacterium `METPO:1007653` | 1 | 0 |
| B/C: predicates/schema | Not included | 0 | 0 |

## Hierarchy and boundaries

The TraitRecord parent is `traitmech:000054`, predatory bacterium. Its v5
placeholder `METPO:1007653` is repeated unchanged for standalone reasoning,
below phenotype `METPO:1000059` and quality `METPO:1000188`. This does not
mint or reserve another parent. Killing and nutrition come from the parent;
coordinated multicellular predation is the differentia.

Group feeding is not cell density, aggregation, motility or killing alone.
It is expressed in a group context, not displayed by an isolated cell.
Solitary killing can coexist with the capability. Neither obligate group
dependence, equal individual benefit, evolutionary cooperation nor all
predators simultaneously attacking one prey is required. Cooperative and
wolf-pack predation are therefore not asserted exact synonyms.

Swarming motility `traitmech:000062` is flagella-dependent. Gliding
`METPO:1000706` and twitching `traitmech:000061` need not involve feeding.
Predator-location subtypes (epibiotic, periplasmic and cytoplasmic) are
orthogonal to group organization. The parent's existing graph describes
the Bdellovibrio model, not this mechanism. Its nodes are not exact matches.
Research mentions of wolf-pack feeding remain literature context, not
duplicate primary records. No existing record is edited.

## Evidence and limits

- [Rombouts et al. 2023](https://doi.org/10.1038/s41467-023-41193-x),
  PMID:37696789, PMC10495355: primary collective-motility and predation
  evidence. The snippet is from the scientific abstract, not the separate
  editor summary. Relevant Results, Discussion and Methods were directly
  read; Figure 5 and Supplementary Table 1 (p. 12) were visually inspected.
  The strain table identifies DZ2 laboratory material and engineered
  reporters/motility mutants, not DK1622 or an established untouched wild
  isolate. Figure 5 measures prey fluorescence loss, not nutrient tracing
  or individual fitness benefits. Movies/source data were not reanalyzed.
- [Zhang et al. 2020](https://doi.org/10.1128/AEM.02286-19),
  PMID:31704687, PMC6974655: primary boundary evidence that individual
  M. xanthus can kill E. coli. The snippet comes from the scientific
  ABSTRACT, not IMPORTANCE. Post-killing behavior, conclusions, the strain
  table and tracking Methods were directly read from PMC. The delta-aglZ
  analysis also includes individuals in small groups; do not call every
  observation solitary. This is not replication of the 2023 experiment.

Both snippets are short contiguous source spans. Exact MED queries were
source-qualified and PMID/title/DOI checked. MED/Crossref expose no linked
correction or retraction; the 2023 source links a preprint. None was found
on its retrieved publisher page. The 2020 publisher returned 403, so its
publisher notice status is unverified. Its failed Europe PMC XML fetch
was followed by a successful PMC HTML retrieval; that limitation does not
mean the source is unindexed or the full text unavailable.

Canonical examples, exact xrefs/synonyms and protein examples remain unset.
Natural-material provenance, taxon identity and mechanism breadth require
further work. A/S motility contributes to the studied assay but is not
imposed universally. No generic causal graph is inferred from those
taxon-scoped results. Two OPEN discussions retain these limits, including
that sequence features alone do not establish collective prey consumption.

## ID space and novelty

Reserve `traitmech:000701`, cohort v577 and the entire
`METPO:1065400-1065499` block; populate only 1065400. Subset:
`metpo_traitmech_2026_10`. Allocation base:
`e0280303cbbfe3ab7970a17d0f27fcd015e1c5e6`.

The 2026-10-11 16:58 UTC audit searched ignored/hidden files and binary
content as text across all 22 pre-existing TraitMech worktrees. Structured
record inventories and semantic comparison complemented lexical searches
for collective/cooperative/group predation, hunting, wolf-pack terminology,
citations, gliding/social motility and rippling. Complementary searches
covered social/multicellular/swarm predation and hunting, including
whitespace-normalized complete record content, without another match.
The allocation scan
covered 576 cohorts and 4,084 narrative intervals without conflicts.
Existing scientific hits are broader predation, distinct locomotion, and
research/discussion mentions, not exact records or unresolved same-scope
trait nodes. No synonym is silently relabeled as an exact match.

All 127 registered CommunityMech roots and 530 extant proposal files were
checked without modifications or block conflicts. Its v1 `METPO:1007131`
is a broader ecological interaction, not this organismal capability.

Fresh upstream heads matched immutable, hash-verified snapshots:
CommunityMech `80049bcc9195480a58633236169b62f86c23489a`, METPO
`1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, and kg-microbe
`1408e7099d039026d7611c240938d8e177753406`. Fresh METPO all-state
issue/PR bodies (644) and comments (654) yielded gliding terminology
context (#57 and #271), not a collective-predation term or reservation.

A fresh temporary seed produced 399 records, 344 present among 1,095 live
records before this addition. The 55 absent identifiers are leads, not an
automatic add queue. The frozen 1,546-row release table and 153-row active
review were reconciled with live records/history. Obsolete gliding motility
`METPO:1000141` is not this trait; no exact candidate was identified.

Complete paginated changed-file lists and stable immutable heads were
checked for all open PRs, including drafts:

| TraitMech PR | Head | Reservation |
| --- | --- | --- |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

CommunityMech draft #935 and METPO #644, #643, #641, #640, #638 and #629
also had no candidate/block conflicts. Recheck before publishing. Searches
do not traverse symlink directories, decompress archives or inventory
unregistered work. This is bounded candidate discovery, not proof that
microbial trait discovery is exhausted.

## Artifacts and verification

The 11-column class template contains two headers, the reused parent and
the new child. No property template or SSSOM mapping is emitted because
no predicate or established equivalence is proposed. Upstream template
headers were checked; preserve trailing directive cells and the correct
`https://w3id.org/metpo/` IRIs.

The writer validates before mutation, defaults to dry-run, guards the
parent projection and refuses unexpected target/proposal preimages.
README counts are derived from the live corpus. Native QC, schema/history,
proposal/ROBOT, snippet, focused/full test, generated artifact and immutable
review checks are required; their actual outcomes belong in the review and
PR. The existing add-trait skill covers this cycle without another update.

## Upstream and round trip

After human signoff, submit to berkeleybop/metpo; no upstream issue or
acceptance is claimed. After official minting, refresh the ontology,
migrate identifiers and references, and retain `traitmech:000701` as
provenance without creating a duplicate or rewriting history.

## Change log

- v577, 2026-10-11: propose collective bacterial predation.
