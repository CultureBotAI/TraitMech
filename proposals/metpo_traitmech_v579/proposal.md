# METPO proposal v579: expansion-driven sliding motility

## Scope and hierarchy

Propose `traitmech:000703` as placeholder `METPO:1065600`, one MORPHOLOGY
CLASS below `METPO:1000059 phenotype`. Scope A adds one organismal phenotype;
Scopes B/C add no predicates or schema vocabulary. Status remains PROPOSED.
The qualifier denotes passive cellular displacement during colony expansion,
including conventional growth-associated and interpreted hydraulic cases.
It does not require one motor, surfactant, colony shape, or direct division
pressure in every instance. A sequence annotation alone is not the phenotype.

The current motility and motile parents require independent movement;
motile additionally specifies metabolic energy. Neither is a suitable
parent for passively displaced cells. Active swimming, swarming, gliding
and twitching are not exact matches. They can coexist in an organism;
no organism-level disjointness is asserted. Wetting, colony diameter or
bulk transport alone does not establish the qualified behavior.

Unqualified sliding and surfing are deliberately not exact synonyms.
The [Kovacs et al. letter](https://doi.org/10.1073/pnas.1710371114)
and [Hennes et al. reply](https://doi.org/10.1073/pnas.1712278114)
disagree about including gravity-driven droplet translation under sliding.
Their actual PDFs and short contiguous snippets were inspected. These are
primary naming positions, not two additional experimental replications.
Whole-droplet translation under gravity alone is outside this definition.

## Evidence and limitations

- [Pollitt et al. 2025](https://doi.org/10.1111/1758-2229.70214),
  PMID:41152213, PMC12568390: passive mycobacterial surface spreading,
  including a hydraulic interpretation. Scientific abstract, main text,
  actual Figure 1 and the downloaded DOCX supplement were inspected.
- [Fall et al. 2006](https://doi.org/10.1186/1471-2180-6-31),
  PMID:16545127, PMC1501027: conventional growth-associated spreading in
  constructed DS64 material. The terminology snippet is from Background;
  primary Results and Methods support the observed phenotype.

The record preserves source-specific qualifiers, conflicting Figure 1
time labels in Fall, and limits on interpreting Pollitt's force mechanism.
Unobserved division is not proof of no growth; gel comparisons also change
concentration. Qualified MED and Crossref records plus inspected publisher
pages exposed no linked correction or retraction on 2026-10-11. That is a
bounded notice check, not a guarantee of permanent absence. No raw movies
were reanalyzed. The original author's
[mc2 155 provenance account](https://doi.org/10.1128/microbiolspec.MGM2-0037-2013)
identifies a laboratory-selected, plasmid-cured mutant derivative; it is
provenance evidence, not another trait experiment.

Neither experimental strain is presented as an unqualified natural
canonical example. Exact taxon/protein branches and the hydraulic molecular
mechanism remain unresolved. No graph, canonical example, external xref,
exact synonym or SSSOM equivalence is asserted to fill these gaps.

## Historical identity and novelty

Pinned and current METPO contain deprecated `METPO:0000096`,
`METPO:000097` and `METPO:1000388`, without replacement annotations.
The second identifier has six digits; `METPO:0000097` instead denotes
historical swarming. Generator commit
`38fbfb82c6cc962009582eb7f8652e48ede0f9c2` assigned reason codes by ID era,
not a sliding-specific biological assessment.
[METPO #521](https://github.com/berkeleybop/metpo/issues/521) disputes that
metadata and [#271](https://github.com/berkeleybop/metpo/issues/271) requests
motility coverage. Neither resolves equivalence to this qualified class.
No obsolete identifier is reused, reactivated, put in xrefs or replaced.

Ignored/hidden lexical searches across all 22 pre-existing TraitMech
worktrees were complemented by structured review of 1,112 unique record
versions, neighboring active motility traits, research, proposals,
history and pending PR metadata. The fresh seed has 399 records, 344
overlapping the 1,097-record pre-addition corpus; 55 absent IDs remain
leads, not an automatic add queue. The frozen release inventory has three
deprecated sliding entries. No active exact record or same-scope unresolved
node requiring repair was identified in the inspected material.

## Reservation

Reserve local ID `traitmech:000703`, cohort v579 and the entire
`METPO:1065600-1065699` block, populating only 1065600. Subset:
`metpo_traitmech_2026_10`. Base:
`b9d7582f119444165d5095cc945e8ec30157010b`.
The 2026-10-11 21:19 UTC allocation check covered 578 existing cohorts,
4,086 narrative intervals, 127 CommunityMech roots and 530 proposal files,
with no conflict. All pre-existing worktree states were preserved.

Hash-verified upstream heads: CommunityMech
`80049bcc9195480a58633236169b62f86c23489a`, METPO
`1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, kg-microbe
`1408e7099d039026d7611c240938d8e177753406`.
All 644 METPO issue/PR bodies and 654 comments were searched. Complete
paginated changed-file lists and immutable heads for open TraitMech
PRs #1782, #1476, #973 and draft #924, CommunityMech draft #935 and METPO
#644, #643, #641, #640, #638 and #629 had no candidate/block conflict.
Recheck before publication.

Searches included ignored and hidden files, with normal binary handling
in the refresh and a retained earlier binary-as-text audit. They do not
follow symlink directories or inspect compressed archives or unregistered
work. This bounded result does not establish exhaustion of new traits.

## Verification and round trip

Use the canonical 11-column class template, including required trailing
directive cells. Verify the template and parse ROBOT/ELK output to confirm
`https://w3id.org/metpo/` IRIs and the existing phenotype hierarchy. Run the
guarded writer, schema/snippet/history/product gates, full QC and tests,
generated-artifact checks and immutable adversarial review. Actual outcomes
belong in the review and PR, not predicted success here.

The add-trait skill already covers qualified scope, deprecated identities
and genotype/phenotype interpretation; no further guidance change is needed
for this record. Human signoff and upstream acceptance remain outstanding.
After official minting, refresh the ontology and migrate references,
retaining local provenance without duplicating the record or rewriting history.

## Change log

- v579, 2026-10-11: propose expansion-driven sliding motility.
