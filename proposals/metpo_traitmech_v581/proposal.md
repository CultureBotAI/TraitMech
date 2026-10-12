# METPO proposal v581: aerobic overflow metabolism

## Context and scope

Propose `traitmech:000705` as placeholder `METPO:1065800`: one PHYSIOLOGY
CLASS below `METPO:1000059 phenotype`. Scope A adds one conditional microbial
phenotype. Scopes B and C add no predicates or schema vocabulary. Status remains
PROPOSED pending human scientific signoff and upstream acceptance.

The oxygen-sufficient qualifier is intentional, not an exact synonym for every
use of unqualified overflow metabolism. This is not a substrate-use pair,
individual observation, gene, sequence feature or universal metabolic pathway.

## Hierarchy and evidence

The definition authority is [Molenaar et al. 2009](https://doi.org/10.1038/msb.2009.82),
PMID:19888218, PMC2795476. Its terminology section describes the aerobic scope;
the paper is a modeling Perspective, not a new experimental replication.
[Basan et al. 2015](https://doi.org/10.1038/nature15765), PMID:26632588,
PMC4843128, and [Hagman et al. 2014](https://doi.org/10.1111/febs.13019),
PMID:25161062, PMC4240471, provide distinct bacterial and yeast studies.
The record preserves source-section, oxygen-control, model and access limits.
All three snippets are short, contiguous spans checked against retrieved XML;
Molenaar's is from the body, not the abstract.

Phenotype is the conservative parent because the record describes a conditional
organismal property, not a biochemical process. METPO:1000060 metabolism is
process-shaped. The local METPO:1002005 fermentation definition excludes external
electron acceptors and is not interchangeable with Basan's oxidative accounting.
[METPO issue 468](https://github.com/berkeleybop/metpo/issues/468) discusses this
hierarchy; the pinned ontology already differs from the retained local record,
as allowed by the frozen release-review policy. Neither is silently changed here.

The assay context differs from product-specific ethanol/butanediol fermentation,
oxygen preference, aerotolerance, copiotrophy and sequential-use diauxie.
No exact synonyms, external xrefs or SSSOM equivalences are asserted. Oxygen
presence and product detection alone do not diagnose oxygen-sufficient overflow.
Conditional evidence is retained without canonical taxa or a protein-resolved
graph; natural strain provenance and mechanistic grounding remain explicit gaps.

## Novelty and ID space

Ignored-and-hidden searches across all 22 pre-existing TraitMech worktrees and
structured inspection of 1,114 distinct trait-record versions found no exact
record. The butanediol record's overflow-metabolite evidence is not equivalent;
nearby Falcon research drafts are leads, not curated overflow records. No exact
causal node or synonym needs migration. Current METPO release/templates and the
pinned ontology expose no active or deprecated candidate match. The editable
OWL root contains imports, not a complete standalone term inventory; the
released graph and maintained templates were checked separately.

A fresh 399-record seed overlaps 344 of 1,099 pre-addition records. Its 55 absent
IDs remain leads, not a missing-work queue. Neither frozen release-review table
contains this candidate. This bounded search does not establish trait exhaustion.

Reserve local ID `traitmech:000705`, cohort v581 and the full
`METPO:1065800-1065899` block, populating only 1065800. The subset is
`metpo_traitmech_2026_10`. Base: `8abebd0652f3de39d8de1d86a246cfe768df7bcc`.
The 2026-10-12 01:03 UTC reservation check covered 580 cohorts, 4,088 narrative
intervals, 127 CommunityMech worktrees and 530 proposal files, without conflict.
CommunityMech v1's 1007100-1007220 range is separate.

Fresh upstream heads matched immutable hash-verified source snapshots:
CommunityMech `80049bcc9195480a58633236169b62f86c23489a`, METPO
`1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, kg-microbe
`1408e7099d039026d7611c240938d8e177753406`. Complete paginated changed-file
lists covered TraitMech #1782, #1476, #973 and draft #924, CommunityMech draft
#935, and METPO #644, #643, #641, #640, #638 and #629 at stable heads.
All-state METPO issue/PR bodies and issue comments were searched. The complete
pending #629 range research document was read: its generic editor range is not
a reservation of every class ID, and its specific reservations do not overlap.
Recheck immediately before publishing.

Searches used normal binary handling and included ignored and hidden files.
They did not unpack archives, follow symlink directories or cover unregistered
work, private decisions or every PR review-thread comment.

## Files and verification

| Artifact | Rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | two headers and one class |
| proposal.md | this narrative |
| properties / SSSOM | omitted; no applicable rows |

The canonical 11-column class header retains required trailing directive cells.
Run guarded-writer tests, strict schema, history, snippet, proposal, product and
QC gates, then inspect ROBOT/ELK's actual w3id METPO parent hierarchy and generated
pages. Actual results belong in the structured review and PR, not predicted
success here. The add-trait skill already covers the interpretation and evidence
requirements encountered; no skill change is necessary for this addition.

## Upstream and round trip

Submit the class template to METPO after TraitMech review. Once the official term
is minted, refresh the ontology and migrate the local identifier and references
to the accepted CURIE, preserving `traitmech:000705` provenance without creating
a duplicate record or rewriting append-only history.

## Change log

- v581, 2026-10-12: propose aerobic overflow metabolism.
