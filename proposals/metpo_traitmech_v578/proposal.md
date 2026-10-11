# METPO proposal v578: swimming motility

## Scope and hierarchy

Lift `traitmech:000702` to placeholder `METPO:1065500`, one MORPHOLOGY
CLASS below existing `METPO:1000702 motile`. Scope A adds one phenotype;
Scopes B/C add no predicates or schema vocabulary. PROPOSED status awaits
human signoff. The definition concerns self-propulsion through liquid,
not a gene, apparatus, sequence prediction, single observation or speed bin.

The existing motile parent supplies energy-dependent locomotion. Swimming
adds the liquid-medium differentia. Swarming, twitching and gliding are
not exact synonyms. Swimming near a boundary still concerns movement
through liquid, not locomotion across a supporting substrate. Neither
chemotaxis, solitary movement, one propulsion apparatus nor a speed range
is required. Passive displacement and colony expansion alone are excluded.
Multiple motility modes can occur in one organism; no disjointness is asserted.

Existing flagellar-motility BIOLOGICAL_PROCESS nodes are mechanism-specific;
swimming-velocity CAPACITY nodes concern speed. Neither is an exact instance
of this organismal trait. Taxis and kinesis definitions add other conditions,
not duplicate swimming records. No same-scope parent-gap TODO or synonym
requires repair; all prior trait YAMLs remain unchanged.

## Evidence

- [Thornton et al. 2020](https://doi.org/10.1038/s41467-020-18253-7),
  PMID:32901025: tracked archaeal liquid propulsion, distinct from diffusion.
  The short snippet is from the scientific abstract.
- [Kuhn et al. 2018](https://doi.org/10.1038/s41467-018-07802-w),
  PMID:30560868: bacterial free swimming versus soft-agar spreading, with
  deletion-bearing backgrounds explicitly retained. The snippet is from
  Results, not the abstract.

Source-qualified MED identities, direct full texts, Methods, relevant
figures and supplementary provenance were checked. The record retains
source-specific qualifiers and inspection limits. Neither sequence
features nor simulations substitute for observed propulsion. The current
bundle is not an exhaustive survey of mechanisms or eukaryotic swimming.
Canonical examples, protein examples and graphs await exact taxon and
mechanism grounding; engineered observations are not thereby invalidated.
No xrefs, synonyms or SSSOM equivalence are asserted.

## Novelty and reservations

Reserve `traitmech:000702`, cohort v578 and the entire
`METPO:1065500-1065599` block; populate only 1065500. Subset:
`metpo_traitmech_2026_10`. Allocation base:
`f3e7a74fc511d23530133c3f17ac419716ca7606`.

The 2026-10-11 18:14 UTC reservation audit included ignored/hidden files
and binary-as-text searches across all 22 pre-existing TraitMech worktrees,
577 proposal cohorts and 4,085 narrative intervals. Structured record,
synonym, discussion and node inspection complemented lexical searches for
swimming, natation, liquid locomotion, slugs and full source identifiers.
No exact existing record or reservation conflict was found in that scope.
All 127 registered CommunityMech roots and 530 extant proposal files were
checked without modifications or conflicts.

Fresh upstream heads matched hash-verified snapshots: CommunityMech
`80049bcc9195480a58633236169b62f86c23489a`, METPO
`1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, and kg-microbe
`1408e7099d039026d7611c240938d8e177753406`. METPO's 644 all-state
issue/PR bodies and 654 comments were searched. Existing
[METPO issue #271](https://github.com/berkeleybop/metpo/issues/271)
requests swimming among missing motility classes; it is a coverage request,
not an accepted term or an identifier reservation.

The fresh temporary seed contained 399 records, 344 among the 1,096 live
records before this addition. The other 55 IDs remain leads rather than
an automatic add queue. The 1,546-row frozen release inventory and 153-row
active review were reconciled against live records/history; no exact
swimming term was identified.

Complete paginated changed-file lists and immutable heads were checked
for every open PR, including drafts:

| TraitMech PR | Head | Reservation |
| --- | --- | --- |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

CommunityMech draft #935 and METPO #644, #643, #641, #640, #638 and #629
also had no candidate/block conflicts. Recheck before publication. Searches
do not follow symlink directories, decompress archives or cover unregistered
work. This is bounded discovery, not evidence that new traits are exhausted.

## Verification and round trip

The template uses the checked 11-column upstream class headers, with their
required trailing directive cells. It contains one new row; no parent is
reminted. Verify the proposal and parsed ROBOT/ELK output, including
`https://w3id.org/metpo/` IRIs and the existing motile hierarchy. Run the
guarded writer's tests, snippet resolver, schema/history/product checks,
full QC and tests, regeneration and immutable adversarial review. Actual
results belong in the review and PR, not a predicted success here.

The native add-trait skill already covers this cycle's scope, provenance
and sequence-interpretation risks; no guidance change is currently needed.
After human signoff, submit this cohort in connection with METPO #271.
No upstream submission or acceptance is claimed. After official minting,
refresh the ontology, migrate identifiers and references, retain the old
local ID as provenance, and do not create a duplicate or rewrite history.

## Change log

- v578, 2026-10-11: propose swimming motility.
