# Epibiotic Bacterial Predation: METPO Proposal v573

## Context

Add `traitmech:000697 epibiotic bacterial predation`, a PROPOSED ECOLOGY
class for attached bacterial killing and nutrition while the predator cell body
remains external. This is an organismal feeding phenotype, not a gene signature,
an individual interaction observation, or attachment alone.

Ignored-and-hidden searches covered all 22 pre-existing TraitMech roots, the
pinned ontology, history, research, proposals and generated artifacts. No exact
primary record or proposal was identified. The live `METPO:1007093 epibiont
phenotype` is broader surface association, despite its frozen June inventory
disposition of NO_CORPUS_DEMAND_NO_PRIMARY. September history confirms its
existing curation. The fresh 399-record seed shares 344 IDs with the 1,091-record
pre-addition corpus; its 55 absent IDs are not a missing-work queue. The
1,546-row release delta, 153-row active-review inventory and policy were read.

The existing predation research report mentions epibiotic feeding but contains
no structured exact node, synonym or discussion requiring a new grounding.
Its broader wolf-pack usage is acknowledged in the new scope discussion;
the attached-feeding meaning follows the directly read primary literature.
Other ectosymbiosis and CPR-association hits are not exact predation claims.
This bounded assessment does not establish global discovery exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Existing Classes Reused | Parent |
| --- | ---: | ---: | --- |
| A: synthetic trait | 1 | 1 | METPO:1007653 predatory bacterium |
| B: predicates | 0 | 0 | Not applicable |
| C: schema enums | 0 | 0 | Not applicable |

`traitmech:000054` supplies bacterial killing and nutrition. External attached
growth, without entry of the predator body, is the differentia. The template
reuses its existing v5 ID `METPO:1007653`, definition and phenotype parent,
also reused by v502. That row is included for standalone labeled hierarchy,
not reallocated. The parent's invasion graph is explicitly qualified to its
B. bacteriovorus model (issue #1865); its identity and graph topology stay intact.

Epibiont association does not require killing or feeding. Cannibalism concerns
prey relatedness, not predator location. No exact equivalence with epibiosis,
ectoparasitism, vampirism, general extracellular killing, saprotrophy or
phagotrophy is asserted. The class neither prohibits envelope-crossing feeding
structures nor requires binary division, polar attachment, a particular prey
range, or obligate dependence. No organism-level disjointness is asserted.

## Evidence and Limits

- `DOI:10.1038/ismej.2013.164`, `PMID:24088628`, `PMC3930308`: definition
  authority; short Introduction quote and direct JSS/EPB observations.
- `DOI:10.1099/ijs.0.039701-0`, `PMID:22368169`: primary scientific Abstract
  supports natural JSS provenance and external predation; full text unavailable.
- `DOI:10.1038/s41467-024-48042-5`, `PMID:38678033`, `PMC11055950`:
  strongest lifecycle/structural evidence; scientific-Abstract quote, time-lapse
  observations and actual Figures 2-5 inspected. Nutritional transfer is not
  directly molecularly traced. Other Methods/figures and supplements remain
  incompletely assessed, as specified in the record.

The full notice `DOI:10.1038/s41467-025-58758-7`, `PMID:40234419`,
`PMC12000597` was read. Corrected prey-range scope and removal of the
S-layer-defense recommendation are respected. This notice is context, not a
fourth independent experiment. The add-trait skill now explicitly requires
literature-status checks (issue #1864). The 2013/2014 papers share authors and
JSS material; distinct citations are not independent-group replication.

All three evidence items have directly checked contiguous snippets. Qualified
example `NCBITaxon:453816 Pseudobdellovibrio exovorus` denotes JSS
(ATCC BAA-2330 = DSM 25223), not every species member. NCBI identity was
resolved independently of the source's older Bdellovibrio name. Natural
provenance concerns the predator, not engineered prey used in some assays.
No protein accession, causal graph, exact synonym, xref or SSSOM mapping is
added for the child. Two OPEN discussions retain scope/mapping and machinery
limitations. PROPOSED remains pending human scientific signoff.

## ID Space and Reservations

Reserve `1065000-1065099`, populate `METPO:1065000`, following v572's
`1064900-1064999`; subset `metpo_traitmech_2026_10`. Main was
`e0f7352618bf57999c1057cb43f5eac4d766a6b0` at the 2026-10-11 audit.
All 21 unowned worktrees were preserved. Whole-block and historical proposal
checks found no conflict; numeric PDF destinations were unrelated false hits.

Complete paginated pending-PR file inventories, including drafts, were inspected
at immutable heads and rechecked at 11:36 UTC:

| TraitMech PR | Head | Files |
| --- | --- | ---: |
| #1782 | 35099af2b7d5347f2ca6e418c4a139979071644d | 1 |
| #1476 | b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3 | 8 |
| #973 | 331f9517bbdf4d2c9fa97b338ee59a8986f2f174 | 3 |
| #924 (draft) | e61ce120b8da953da097b9f94bfed7f292e5675a | 692 |

None supplies a competing allocation. CommunityMech main
`80049bcc9195480a58633236169b62f86c23489a`, local proposals and draft #935
were checked. Upstream METPO main `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`,
six pending PRs (#644, #643, #641, #640, #638, #629), 644 all-state issue/PR
bodies and 654 issue comments yielded no exact candidate proposal. The
[epibiont comment on #424](https://github.com/berkeleybop/metpo/issues/424#issuecomment-4577725651)
is broader, not a competing feeding class. These snapshots are not an atomic
reservation service; recheck before publishing.

The canonical class headers were read at kg-microbe commit
`1408e7099d039026d7611c240938d8e177753406`. Preserve the 11 columns and three
empty trailing directive cells. TraitMech's maintained wrapper expands METPO
to `https://w3id.org/metpo/`, not the older OBO stub in upstream example prose.

## Files and Verification

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 2, including unchanged parent identity |
| property template | Omitted |
| SSSOM mappings | Omitted |

Validation results will be recorded after the maintained gates run. No baseline
exceptions, source-counter inflation or human-review status promotion is intended.

## Upstream and Round Trip

Submit this cohort for METPO review. When accepted IDs appear in a pinned
release, migrate the local child and parent references consistently, preserve
local-ID provenance in append-only history, and regenerate products without
duplicate primary records. No separate upstream candidate issue is claimed.

## Change Log

- v573, 2026-10-11: propose source-bounded external attached bacterial predation,
  qualify the parent illustration and add literature-correction guidance.
