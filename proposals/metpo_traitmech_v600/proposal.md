# Nematode Egg-Hatching Stimulatory Activity

## Proposed Class

`METPO:1067700`: **nematode egg-hatching stimulatory activity**. A physiological
capability of a microorganism to increase nematode egg hatching over a defined
observation interval relative to comparable controls without that microbial influence.

Local identifier: `traitmech:000724`, category `PHYSIOLOGY`, status `PROPOSED`.
Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
This is a positive capability, not mere absence of inhibition, microbial development,
nematode susceptibility or embryo development without emergence. Attraction,
trapping, paralysis and killing do not establish this endpoint. Infection,
nutrition or benefit to the microorganism is not required. Opposite responses in
different hosts or culture conditions do not make organism-level traits disjoint.

## Evidence And Limits

- **Definition authority:** [Meyer et al. 2004](https://doi.org/10.1163/156854104323072883).
  The fungal-filtrate screen reports stimulation relative to uninoculated potato
  dextrose broth. Counts include motile and immotile juveniles at 14 days, divided
  by initial eggs and then related to control hatch. Culture age is not exposure
  time. The paper's strong-effect threshold is not the class boundary; only 40 of
  253 isolates were retested. Consumption of inhibitory nutrients versus added
  stimulants remains unresolved. Host, isolate and culture age affect direction.
- **Second primary experiment:** [Vejzagic et al. 2015](https://doi.org/10.1186/s13071-015-0986-z),
  `PMID:26174801`, `PMCID:PMC4501204`. This is its own bacterial experiment.
  Scientific Abstract Results and full Results/Figure 2 support variable hatch
  enhancement in the tested Trichuris muris conditions. Enterococcus caccae and
  Lactobacillus reuteri exceed bacteria-free controls after 20 h without
  antimicrobials. Little Trichuris suis hatch is not absolute inability. The
  separate E. coli strain/concentration ANOVA excludes near-zero controls.

Only Meyer and the local record annotate the proposal definition. The second
paper supports the broader microbial capability but is not appended to the
definition annotation as a bibliography. No canonical taxon, exact synonym,
xref, shared molecule, protein, direct-contact mechanism or causal edge is
asserted. No field efficacy, environmental safety, infectivity benefit or
therapeutic use follows. Host-generalism and secretion are not necessary.

The 17-word Meyer excerpt was checked against the USDA-hosted typeset page 28
(PDF page 6). PDFKit splits the word controls across lines: direct visual
verification is not native `VERIFIED` or an exact plain text-layer match.
The maintained abstract function returned `UNRESOLVED`. The 19-word Vejzagic
excerpt matches the publisher/XML scientific Abstract Results and the maintained
function returned `VERIFIED`. The record-specific CLI report is separately
retained in the [verification sidecar](../../research/traits/physiology/nematode_egg_hatching_stimulatory_activity-source-verification.json).

Methods, own results and selected figures were inspected, not the full raw data.
Meyer publisher access returned 403; its USDA article was directly available.
Crossref and exact DOI Europe PMC checks were inspected. Crossmark returned
script shells, not current-status verdicts. Targeted correction/retraction
searches returned no exact notice, a bounded result rather than notice clearance.
Source identities, URLs, locators, hashes and limitations remain in the sidecar.

## Novelty And Reservations

Accepted at `2026-10-14T06:04:12Z` on clean main
`e420fcd29b89d3383c3cc9cff2fcf5498cfbd9ae`.
Searches included ignored and hidden files across 185 known locations, 180
available, and 139 retained heads. Five unavailable deleted worktrees and lost
untracked/ignored history cannot be reconstructed. Historical searches inspected
23,434 TraitMech and 5,802 CommunityMech unique regular-file blobs, with native
whole-tree comparison controls. Existing lethal, paralysis and hatch-inhibition
records have distinct endpoints. TYQ1 cached literature concerns suppression,
not an exact positive-hatch trait. No exact synonym, ungrounded causal node or
same-scope parent-gap discussion was found in the inspected maintained context.

Pinned/current METPO release, explicit editor OWL and six selected TSV owners
include deprecated/draft content. The only matching morphology is unrelated
fried-egg-shaped colony `METPO:1007069`, not a historical counterpart. The
byte-verified editor conversion has 31 triples and no imports. The current and
pinned phenotype parent agree. The pinned ontology was not replaced.

Live screening covered 11 open/draft PRs, 783 nonremoved changed blobs and 587
selected upstream owners. TraitMech PRs #1782, #1476, #973 and draft #924;
CommunityMech draft #935; METPO #644, #643, #641, #640, #638 and #629 were
included. Their exact heads, bodies and states were rechecked at acceptance.
Upstream snapshots: CommunityMech `8df89370be840a4b58a9d8a7407c66c7471a5085`,
METPO `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, KG-Microbe
`9d84fdf903788423ea0c36104d7fc64e01be52be` (master).

Reserve local `traitmech:000724`, cohort `metpo_traitmech_v600` and the entire
`1067700-1067799` block; only `METPO:1067700` is proposed here. The 255 raw
numeric matches were supplementary decimal values `1067725.377` or embedding
coordinates `5.1067753`/`3.1067753` for unrelated nodes in draft #924. All 760
interval overlaps were the broad `1000000-1999999` editor envelope or its
documentation, not narrower competing reservations. This is a bounded check,
not an atomic allocation or exhaustive search of every host path and ontology.
Recheck pending reservations before publication.

## Round Trip

The canonical 11-column class template uses `metpo_traitmech_2026_10`, preserves
empty cells and carries the local ID in `traits_addressed`. No SSSOM file is
needed without an exact external equivalence. Run `just verify-proposal
metpo_traitmech_v600` and `just robot-validate-proposal metpo_traitmech_v600`;
inspect emitted definition annotations and the real `https://w3id.org/metpo/`
parent, not a legacy namespace stub. After upstream acceptance and release,
verify exact identity before a separate reviewed local-to-METPO migration;
do not mark this proposal as already released or human-reviewed.

Two OPEN discussions retain hierarchy and source/mechanism limits. Existing
add-trait guidance covers these issues and requires no new skill edit for this
addition. All preexisting records, including protected spore germination, are
outside this change.
