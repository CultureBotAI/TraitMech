# METPO proposal v580: diauxic growth

## Scope and hierarchy

Propose `traitmech:000704` as placeholder `METPO:1065700`, one PHYSIOLOGY
CLASS below `METPO:1000059 phenotype`. Scope A adds one conditional
population-growth phenotype; Scopes B/C add no predicates or schema vocabulary.
Status remains PROPOSED. The definition denotes two successive growth phases
associated with switching preferential nutrient use as the first source becomes
limiting. It is not an arbitrary biphasic curve or a fixed species identity.

Boulineau's Introduction supplies the sequential-use definition authority.
Sandercock and Page support extending carbon-source usage to nitrogen-source
transitions. Lag-emphasizing accounts operationalize a narrower pattern;
Wang reports short or nonexistent diauxic lags. The definition does not impose
a positive minimum lag, arrest of every cell, strictly zero secondary-substrate
use, glucose preference, or initial supplementation of both sources.

`diauxie` is an exact synonym in this nutrient-switching sense. Diauxic shift
names the transition, while polyauxie and unqualified diphasic growth are not
exact synonyms. No external xrefs or SSSOM equivalences are asserted.
`METPO:1000731 nutrient adaptation` is a trophic-type class whose local record
operationalizes chronic copiotroph/oligotroph regimes, not this temporal growth
pattern. Phenotype is the conservative parent pending upstream review.
Generalist (`METPO:1005040`) and specialist (`traitmech:000177`) describe niche
breadth, not the new trait. Dormancy, carbon catabolite repression and generic
resource-use relations also have different scope.

## Evidence and limits

- [Boulineau et al. 2013](https://doi.org/10.1371/journal.pone.0061686),
  PMID:23637881, PMC3640066: sequential-use definition and cell-level variation.
  Scientific abstract, relevant main sections, actual Figure 2 and Text S1 prose
  inspected. AB460 is an engineered MG1655 derivative; medium exchange is not
  mixed-substrate batch culture. DOC extraction loses embedded equations, which
  were not visually verified or used for mechanistic claims.
- [George et al. 1985](https://doi.org/10.1128/jb.164.2.866-871.1985),
  PMID:3863813, PMC214331: acetate/glucose diauxie with acetate preferred.
  Direct source-qualified MED abstract only; full text and figures not inspected.
  XML endpoint HTTP 500 is an access limit, not proof of missing full text.
- [Sandercock and Page 2008](https://doi.org/10.1128/jb.01571-06),
  PMID:18055600, PMC2223558: carbon and nitrogen transitions in UW batch culture.
  Abstract, relevant Methods/Results and actual Figure 3 inspected. Ammonium
  augmentation addresses the oxygen-limitation alternative; RpoS is not a
  universal mechanism. Later PHB consumption was explicitly unmeasured.
- [Wang et al. 2015](https://doi.org/10.1371/journal.pbio.1002041),
  PMID:25626068, PMC4308108: a spectrum including operationally absent lag.
  Scientific abstract, relevant Results/Methods, actual Figure 1 and S1 EPS
  inspected. Zero lag means no local minimum in smoothed growth rate, not
  equal simultaneous substrate use. Figure 1 caption says eleven strains but
  the image has twelve labels; no strain count is propagated.
- [Zampar et al. 2013](https://doi.org/10.1038/msb.2013.11),
  PMID:23549479, PMC3693829: initially glucose-grown FY4 later uses produced
  ethanol. Introduction, relevant Results/Methods and actual Figure 1 inspected.
  The snippet is from Introduction, not the abstract. Fitted rates and
  model-constrained flux ranges are not direct intracellular flux measurements.
  Raw supplement data and the complete mechanism were not reanalyzed.

Each source has a short, contiguous, directly checked snippet. MED and Crossref
metadata for all five and available primary pages exposed no linked correction
or retraction on 2026-10-11. This is a bounded check, not a permanent guarantee;
Wang's preprint link is not a correction. No canonical example is asserted
without strain provenance and resolved taxon identity. No shared universal
mechanism is established, so no causal graph or taxon-paired protein branch is
invented. Gene annotations, RpoS expression and predicted flux alone do not
establish observed diauxic growth.

## Novelty and reservations

Ignored/hidden searches across all 22 pre-existing TraitMech worktrees plus
structured review of 1,113 unique trait YAML versions found no exact record.
Prior natural-competence and rrn-copy research mentions are not curated
diauxie entries. Pinned/current METPO have no inspected active or deprecated
lexical match. The fresh 399-record seed overlaps 344 of the 1,098 pre-addition
records; its 55 absent IDs remain leads, not a work queue. Neither frozen
release-review table contains a diauxie candidate.

Reserve `traitmech:000704`, cohort v580 and the full
`METPO:1065700-1065799` block, populating only 1065700; subset
`metpo_traitmech_2026_10`. Base:
`94e5d07e80ef4885a40f640f85cb39ddf5a2492c`.
The 2026-10-11 23:42 UTC check covered 579 existing cohorts, 4,087 narrative
intervals, 127 CommunityMech roots and 530 proposal files, without conflict.

Fresh upstream heads matched hash-verified snapshots: CommunityMech
`80049bcc9195480a58633236169b62f86c23489a`, METPO
`1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, kg-microbe
`1408e7099d039026d7611c240938d8e177753406`.
Full paginated changed-file lists at stable open heads covered TraitMech
#1782, #1476, #973 and draft #924, CommunityMech draft #935, and METPO
#644, #643, #641, #640, #638 and #629. All-state METPO issue/PR bodies and
issue comments were searched. The complete pending #629 range research
document was also inspected; its generic editor range is not an occupancy
reservation, and its specific reservations do not overlap this block.
Recheck before publication.

Searches included ignored and hidden files with normal binary handling;
they did not unpack archives, follow symlink directories or claim coverage of
unregistered work, private decisions or every PR review-thread comment.
No claim of microbial trait exhaustion follows from this bounded audit.

## Verification and round trip

Use the canonical 11-column class template with required trailing directive
cells. Inspect ROBOT/ELK output with an RDF parser for the w3id METPO namespace
and existing phenotype hierarchy. Run guarded writer, schema/snippet/history/
product gates, QC, tests, generated-artifact inspection and immutable scientific
review. Actual outcomes belong in the review and PR, not predicted success here.

Existing add-trait guidance already covers scope, sequence-feature interpretation,
section identity, provenance and figure discrepancies; no skill edit is required
for this addition. Human signoff and upstream acceptance remain outstanding.
After official minting, refresh the ontology and migrate references, preserving
local provenance without duplicating the record or rewriting history.

## Change log

- v580, 2026-10-11: propose diauxic growth.
