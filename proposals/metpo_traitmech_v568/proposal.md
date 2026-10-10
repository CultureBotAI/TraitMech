# METPO proposal v568: diatom seta production

## Context and scope

Lift `traitmech:000692` as `METPO:1064500`: one PHYSIOLOGY class,
kept PROPOSED pending human signoff. Scope A: one class used in one local
record; B/C: zero. The phenotype is formation of siliceous whisker-like
diatom cell-wall extensions called setae, not a material structure,
sequence feature or generic organism-chemical production pair.

## Hierarchy and boundaries

The local direct parent is biomineralization `traitmech:000690`, whose
definition covers mineral formation. Its released METPO ancestor is
phenotype `METPO:1000059`, below quality `METPO:1000188`. The standalone
TSV uses that released ancestor because v566's `METPO:1064300` remains
proposed. On joint adoption request
`METPO:1064500 SubClassOf METPO:1064300`. This refinement is explicit in
the narrative and TSV observations, not emitted by the standalone template.
Do not re-emit or modify v566 or v567.

This is formation, not inherited appendage possession, silica uptake or
adsorption. Valve/girdle production, siliceous scales and auxospore
coverings alone do not establish this endpoint, nor do setae alone establish
those endpoints. The existing frustule scope note distinguishes setae and
is not an unresolved exact grounding. No existing trait YAML changes.
No organism-level disjointness, universal number, length, shape, cell-cycle
coupling, buoyancy or fitness benefit is asserted. Extracellular formation
is not definitional. No synonyms, xrefs or SSSOM mappings are asserted
without authority-backed equivalence review; generic bristles and spines
are not automatically equivalent to diatom setae.

## Evidence and limits

- [Mayzel et al. 2021](https://doi.org/10.1038/s41467-021-24944-6),
  PMID:34330922, PMC8324917: definition authority and seta-formation
  evidence in Chaetoceros tenuissimus under the source name. Scientific
  Abstract, Introduction, Results, Discussion, Methods, main captions and
  Table 1 read in official Europe PMC full-text XML. Actual Figures 2, 3
  and 5 inspected. The short quote is from the Introduction. Figure 2
  PDMPO labeling at growing tips supports new deposition. Figure 3 shows
  membrane, silica and an external organic layer; the extracellular route
  is a proposed interpretation, not universal SDV absence. Figure 5 uses
  per-cell scoring for silicon limitation and per-valve scoring for
  germanium/PDMPO, not a shared denominator. New valves form under the
  latter treatment but their texture is altered. No universal threshold
  or rate is inferred. Other actual figures, supplements and movies
  remain unread; unavailable supplemental files were not treated as read.
- [Safadi et al. 2025](https://doi.org/10.1016/j.jsb.2025.108205),
  PMID:40294667: complete scientific Abstract directly read in official
  Europe PMC CORE; online 2025-04-26, June issue. In-cell cryoET during
  seta formation in Chaetoceros rostratus supports the endpoint and an
  organic sheath outside the plasma membrane. Suggested macromolecular
  control of shape is not proven necessity. Full Methods, actual figures
  and supplements remain unread. This is a distinct primary study with
  overlapping authors, not independent-laboratory replication.

Both queries use `EXT_ID:<PMID> AND SRC:MED`; ID, source, title and DOI
were checked together. Both items have contiguous source snippets. The
native abstract-verifier result is separate from direct full-text quote
verification. No canonical taxon, strain accession or protein is assigned.
Exact mappings, exemplar provenance and functional mechanisms remain in
two OPEN discussions. Sequence features and ultrastructural association
alone do not support protein-level causal edges.

## Allocation and novelty

Reserve `traitmech:000692`, cohort v568 and the complete
`METPO:1064500-1064599` block; populate only 1064500. Subset:
`metpo_traitmech_2026_10`. Allocation main:
`1ea1527332f364b1249e860633413bb0a894be17`.

Ignored-and-hidden searches covered the complete repository and all 22
pre-existing worktrees. Terms included seta/setae, setal/setose/setiform,
Chaetoceros, diatom/silica bristle/spine/appendage/whisker variants,
silicification, frustules, biomineralization, both DOI/PMID values and
PMC8324917. Local ID, cohort and full numeric block were also checked.
Relevant hits distinguish frustules and setae, or concern existing mineral
and scale formation, fungal spines, reproduction, feeding on diatoms,
organoheterotrophy and generic causal-graph wording. Dependency-code hits
were not biological records. No exact trait or conflicting reservation
was found in that explicitly searched scope.

The pinned METPO graph has 12,617 triples. Fresh seeding emitted 399
records; 55 IDs absent from the 1,086 live records comprise 38 supporting
properties and 17 semantic duplicates. The full 1,546-row release delta
and 153-row active-review table were parsed and their policy read. No
exact METPO term is available for this candidate. Seed absence is not
novelty or exhaustion proof.
An additional whole-graph silica/appendage search found only
`METPO:1000022`, labeled obsolete appendage and explicitly deprecated
under ObsoleteClass. It is neither an active phenotype nor an exact
seta-formation term and is not reused.

The full numeric block was searched throughout CommunityMech, including
ignored and hidden files. Eight hits are the BLAST taxonomy identifier
1064592 in cached Biopython test inputs/assertions, not METPO reservations.
The reviewed CommunityMech v1 blocks do not overlap.

Paginated complete changed-file lists and immutable curation blobs were
checked for all open PRs, including drafts, on 2026-10-10:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | Existing Shedu 000220; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

Recheck main and reservations immediately before publishing. Protected
spore germination and all unowned work are excluded from curation.

## Artifacts and verification

One 11-column class TSV and this narrative; no property or SSSOM file.
Three empty trailing ROBOT directive cells are intentional. Upstream
contract commit `1408e7099d039026d7611c240938d8e177753406`, class/property
blobs `b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` define the canonical headers.
Use maintained w3id METPO IRIs, not legacy OBO stubs. CommunityMech's
historical 12-column property format is not the canonical 13-column header.

The writer defaults to dry run, checks parent identity/scope, refuses
target/proposal drift, prevalidates before writes and supports exact replay.
Tests use controlled temporary preimages. Require strict/LinkML validation,
history, QC, products, proposal/ROBOT/ELK, snippets, focused/full tests,
generated-product preservation and desktop/mobile page inspection. Actual
outcomes belong in the PR and immutable review; no unrun check is claimed.

## Upstream and round trip

After human signoff submit the TSV and v566 biomineralization refinement
to berkeleybop/metpo. No upstream issue or accepted term is claimed.
After acceptance refresh the pinned ontology, migrate the local identifier
and references, and preserve minting provenance and append-only history
without retaining a duplicate primary record.

## Change log

- v568, 2026-10-10: propose diatom seta production.
