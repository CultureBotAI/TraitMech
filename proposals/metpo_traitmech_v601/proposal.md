# Nematode-Repelling Activity

## Proposed Class

`METPO:1067800`: **nematode-repelling activity**. A physiological capability of a
microorganism to elicit active movement of nematodes away from itself or
substances it produces.

Local identifier: `traitmech:000725`, category `PHYSIOLOGY`, status `PROPOSED`.
Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
The bearer is the microorganism, not the moving nematode. Microbial taxis, lack
of attraction, relative food preference alone, paralysis, killing, trapping,
feeding or altered egg hatching does not establish this capability. Infection,
prior ingestion or benefit to the microorganism is not required. Attraction and
lethality are not declared disjoint at organism level; responses are conditional.

## Evidence And Limits

- **Definition authority:** [Pradel et al. 2007](https://doi.org/10.1073/pnas.0610281104),
  `PMID:17267603`, `PMCID:PMC1892944`. Own experiments show initial lawn entry
  followed by leaving Serratia marcescens. The swrA insertion mutant has reduced
  avoidance but similar multiday killing. Purified serrawettin W2 on OP50 lawns
  and acute drop-induced reversal are separate assays. Chemical recognition
  versus a mechanical surfactant cue remains unresolved; other cues can contribute.
- **Second primary experiment:** [Prakash et al. 2021](https://doi.org/10.15252/embj.2020106938),
  `PMID:34086368`, `PMCID:PMC8246062`. Figure 1A-B shows decreased Pseudomonas
  aeruginosa PA14 lawn occupancy over 12 hours. Pure 1-undecene chemotaxis and
  omega turns in Figure 2/Appendix S2 are distinct from bacterial lawn leaving.
  PA14-versus-undA odor choice demonstrates relative preference, not by itself
  repulsion or complete loss of bacterial repellence. Peer-review reply page 14
  reports reversals without complete leaving of 1-undecene-treated OP50 lawns;
  the adjacent-lawn crossing experiment is not eviction from an occupied lawn.

Only Pradel and the local record annotate the proposal definition. Prakash
supports the general microbial capability but is not added to the definition
annotation as bibliography. The 18-word Pradel scientific-abstract excerpt
directly matches PMC text and the native function returned `VERIFIED`. The
21-word Prakash Discussion excerpt matches JATS, PMC and publisher text; native
`NOT_IN_ABSTRACT` is retained, not converted to `VERIFIED`. The record-specific
CLI result is separate in the [verification sidecar](../../research/traits/physiology/nematode_repelling_activity-source-verification.json).

Own results, methods and actual Pradel Figures 1-4 and Prakash Figures 1-2 were
inspected. The Prakash appendix was read throughout; actual S1, S2 and S4 were
inspected, while S3 and strain-table coverage was textual. Selected peer-review
reports/replies were read, including rendered reply pages 14 and 30. Added
alleles and controls do not establish a successful AWB ablation or blanket
physiological specificity. Main Methods and Appendix S1A differ on headspace
preparation timing/temperature; no harmonized protocol is invented. Greater
roaming or mean square displacement alone is not directional avoidance.

No shared microbial mechanism, universal host response, canonical taxon,
protein, chemical xref, causal graph, exact synonym or external equivalence is
asserted. Compound production and gene presence alone are insufficient. Neither
universal nonlethality nor field efficacy, environmental safety or therapeutic
use follows. Chai, Zhao, Li and the unread Chen lead remain research context,
not extra supporting citations. Exact DOI metadata and bounded notice searches
were checked; no comprehensive correction/retraction clearance is claimed.
Pradel publisher access returned 403 but PMC was available. Prakash published
assets were accessible after correcting a temporary helper's omitted `/pmc/`
URL segment; the earlier 404s were not evidence of missing published figures.

## Novelty And Reservations

Accepted at `2026-10-14T09:11:26Z` on clean main
`55407337d8572f15d01f47bf6c9a99abc05d264a`.
Ignored and hidden files were included across 188 known locations and 143
retained heads. The history search covered 23,435 TraitMech and 5,815
CommunityMech unique regular-file blobs, with native whole-tree comparison
controls. All 719 unique matched path/text variants were assessed: 556 baseline,
161 new current-copy variants and two extra historical generated immune-evasion
graphs. None defines this exact microbial capability. Existing attraction,
paralysis, killing and hatch records have distinct endpoints. No exact synonym,
same-scope ungrounded node or parent-gap discussion requires a coupled repair.

Pinned/current METPO releases, explicit editor OWL and six selected TSV owners
include deprecated/draft content. Deprecated chemotaxis `METPO:1000062` has no
replacement or consider annotation in the inspected ontology and is not an
exact counterpart. No revival or mapping to it is proposed. Active phenotype
`METPO:1000059` agrees in pinned/current ontology; the pin is unchanged. The
byte-verified explicit editor conversion has 31 triples and no imports.

Live screening covered 11 open/draft PRs, 783 nonremoved changed blobs and 587
selected upstream owners; all 21 matched files were assessed. CeMbio member odor
preferences do not constitute an exact trait or whole-consortium repulsion.
Included PRs: TraitMech #1782, #1476, #973, draft #924; CommunityMech draft #935;
METPO #644, #643, #641, #640, #638 and #629. Heads, bodies and states were
rechecked at acceptance. Upstream heads: CommunityMech
`8df89370be840a4b58a9d8a7407c66c7471a5085`, METPO
`1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, KG-Microbe
`9d84fdf903788423ea0c36104d7fc64e01be52be`.

Reserve `traitmech:000725`, cohort `metpo_traitmech_v601` and the full
`1067800-1067899` block; only `METPO:1067800` is proposed. Two numeric matches
are draft #924 embedding coordinates `3.1067874` and `-2.1067863` for unrelated
nodes, parsed as floating-point columns. All 857 interval overlaps refer to the
broad `1000000-1999999` editor envelope or its documentation, including wrapped
context checked separately. No competing narrower reservation was identified.

Coverage is bounded: missing ignored/untracked history cannot be reconstructed;
symlink targets, submodules and arbitrary archives are excluded. Remote coverage
is selected owners and changed blobs, not every unchanged PR file or ontology.
This is not atomic allocation, a global absence claim or literature exhaustion.
Recheck pending reservations before publication.

## Round Trip

The canonical 11-column class template uses `metpo_traitmech_2026_10`, preserves
empty cells and carries the local ID in `traits_addressed`. No SSSOM file is
needed without exact equivalence. Run `just verify-proposal metpo_traitmech_v601`
and `just robot-validate-proposal metpo_traitmech_v601`; inspect emitted
definition annotations and the real `https://w3id.org/metpo/` parent. After
upstream acceptance and release, verify exact identity before a separate
reviewed local-to-METPO migration. This proposal is not released or human-reviewed.

Two OPEN discussions retain hierarchy and source/mechanism limits. Existing
add-trait guidance covers these boundaries; no skill edit is needed for this
addition. All preexisting records, including protected spore germination, remain
outside the change.
