# Bacterial Polar Flagellar Ejection

## Scope And Hierarchy

Propose **bacterial polar flagellar ejection**, `METPO:1068500`, for
`traitmech:000732` (`PHYSIOLOGY`, `CLASS`, `PROPOSED`).

Definition: A physiological phenotype in which a bacterium actively ejects
previously assembled axial structures of a polar flagellum by separation at
its base.

Scope A contains one new class. Scopes B and C contain no new predicates or
schema-enum lifts. Phenotype `METPO:1000059`, below quality `METPO:1000188`,
is a definition-based parent inference. Locomotory possession is not a required
parent. Hook-filament release is an observed endpoint, not a requirement that
every released structure contain exactly the same complete set of components.

Possession, arrangement, assembly failure, motor arrest, reduced motility,
daughter-cell dilution and passive midfilament breakage alone do not establish
this endpoint. Periplasmic resorption and eukaryotic axonemal autotomy are
distinct. No universal nutrient trigger, precise severing site, relic structure,
nonmotility, complete loss of all flagella or organism-level disjointness is
asserted. No exact synonyms, xrefs, SSSOM mappings, canonical taxa, proteins or
causal graphs are added. Sequence features alone cannot establish the phenotype.

## Evidence And Limits

1. [Ferreira et al. 2019](https://doi.org/10.1371/journal.pbio.3000165),
   PMID:30889173, PMC6424402, is the definition authority. The 12-word Results
   snippet is directly matched to publisher HTML in the sole paragraph of
   "Shed hook-filament structures accumulate in P. shigelloides supernatant",
   anchor `article1.body1.sec2.sec4.p1` (PDF pp. 4-5),
   with Figure 1G. Native `NOT_IN_ABSTRACT` is retained. All 25 main PDF pages
   and six actual figures were inspected, not raw supplemental data.
   Hook-bearing released material, population measurements and relic/assembly
   comparisons support ejection. Figure 1E reports 34 hooked ends among 70
   ends, not 34 of 70 complete flagella. Cryo-ET snapshots are not a time course.
   Minimal medium with glucose is not complete carbon starvation. Species and
   treatments differ; energy conservation and leakage prevention are interpretations.
2. [Zhuang et al. 2020](https://doi.org/10.1111/mmi.14511), PMID:32259388,
   provides a distinct experimental paper. Its nine-word scientific-abstract
   snippet matches MED and publisher text with native `VERIFIED`. Main
   publisher text, Methods and six captions were read, not the actual figures,
   PDF or supplement. OD times flagellated fraction is a population proxy.
   VIO5 and engineered EGFP-FliG NMB344 are distinct; Figure 3 panels are not
   the same cells. Two-color observations in Figures 5-6 support release,
   while rod breakage remains inferred. Surface immobilization and medium
   exchanges constrain the assays. The 69/72 shedding cases are not biological
   replicates. Source-designated wild type is not proof of natural provenance.
3. [Guo et al. 2026](https://doi.org/10.1038/s41467-026-75593-6),
   PMID:42660870, PMC13521929.1, supplies a current nutrient-depletion
   comparison. The 15-word snippet exactly matches JATS Results, "Two distinct
   in situ architectures of the flagellar motor in V. cholerae"; native
   `NOT_IN_ABSTRACT` is retained. All 12 main PDF pages and six main figures,
   actual Supplementary Figure 4 and supplementary tables were inspected.
   Other supplementary material remains incompletely read. The 81/273
   observations are cells in the caption but tomograms in Methods/Table 4,
   not biological replicates or ejection rates. Main text points to Table 3
   instead of Table 4. Wild-type nutrient assays and delta-flhG structural
   preparations must remain separate.

The current FlgI closure interpretation is not a universal unidentified added
plug. Gate-deletion assembly defects alone do not show ejection failure.
Taxon-paired protein authority, strain provenance and edge-specific mechanism
evidence remain open. Only the local record and the 2019 DOI annotate the
definition. Three publications are not a claim of independent replication.

The [source receipt](../../research/traits/physiology/bacterial_polar_flagellar_ejection-source-verification.json)
retains actual verdicts, hashes, source locators and access limits. Native Wiley
retrieval returned 403 while web access supplied full HTML; figures and
supplement remain unread. The initial Ferreira HTML parser failed after a
successful download; a standard-library follow-up verified the archived text.
MED/publisher notice checks are bounded, not comprehensive clearance.
PMID:30948839 is a Comment on Ferreira, not a correction or another experiment.
No raw-data reanalysis, paid research or human sign-off is implied.

## Identity And Reservation

Accepted at `2026-10-15T11:39:29Z` on main
`616a97577299f7a33d9b6c98ab29c28b30c64758`. Reserve `traitmech:000732`,
`metpo_traitmech_v608` and the whole block **1068500-1068599**.
Only `METPO:1068500` is populated; subset `metpo_traitmech_2026_10`.

Ignored and hidden current files were searched in 204 known locations, plus
295 retained heads containing 86,276 TraitMech and 9,268 CommunityMech unique
regular blobs. Nine removed worktree paths remain unavailable. All 458 bounded
biological contexts and 66 exact-token/overlapping-range contexts were assessed.
The latter contain only the general 1000000-1999999 editor envelope, no exact
candidate token. Historical tracked content cannot reconstruct lost ignored files.

The refreshed remote snapshot covered 13 open/draft PRs: TraitMech #1938,
#1937, #1936, #973 and draft #924; CommunityMech #2018 and draft #935; METPO
#644, #643, #641, #640, #638 and #629. It screened 812 nonremoved changed-file
blobs and 587 selected upstream owners. New CommunityMech #2018 at
`262d1716cd587693f5784e064c93dd112d0829b8` has 28 changed files with no
candidate matches. Its changed local worktree was separately rechecked,
including ignored files, with stable before/after catalogues. Matches were
unrelated numerical intervals or prior reservations, not this candidate.
The 11:39:13 UTC guard confirmed unchanged main, PR heads, bases, descriptions,
draft states and selected upstream heads after this reassessment.

Complete proposal and remote content checks, including wrapped ranges and gzip
decoding, covered 189,221 owner contexts and 2,636 unique contents. All 27
overlapping contents describe the general 1000000-1999999 editor envelope,
not a competing narrow reservation. No exact candidate token or binary limit
was reported. These are context counts, not counts of traits.

Pinned/current METPO releases distinguish motility, flagellar possession and
polar arrangement from ejection. Historical METPO:0000089 and METPO:000090 are
deprecated with OMO:0001000; METPO:1000381 uses IAO:0000226. Their replacement
METPO:1000704 denotes locomotory possession, not shedding. Deprecated flagellum
METPO:1000123 has OMO:0001000 and no observed replacement/consider annotation.
These are not exact xrefs and are not revived. The current editor is an import
stub, not the full release. The ontology pin stays unchanged.

Checks are bounded, not an atomic reservation or exhaustive literature search.
Lost ignored history, symlink targets, arbitrary archives and unchanged PR files
were not reconstructed. Refresh remote reservations before publication.

## Verification And Upstream Path

The class table preserves the canonical 11-column headers checked against the
KG-Microbe template at `1acb8b61fcae24fafc0640b1bf6e5be669f315f9`.
Run the maintained verifier and ROBOT/ELK wrapper, then inspect actual
`https://w3id.org/metpo/` child-parent-quality IRIs and definition annotations.
This instruction does not claim that unrun gates passed.

Submit the reviewed class upstream separately. The reserved ID is not released.
After acceptance and release, separately review scope, update the pin, re-seed
and migrate the local identifier while retaining its prior spelling for
traceability. No upstream PR or human scientific approval is implied here.
