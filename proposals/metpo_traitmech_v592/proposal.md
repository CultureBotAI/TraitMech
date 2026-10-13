# Kin Discrimination

## Context And Scope

One Scope-A ecological CLASS, `traitmech:000716`, proposed as `METPO:1066900`:
**kin discrimination**. It denotes an ecological phenotype in which microbial
cells preferentially associate with kin or exclude nonkin through differential
interactions according to genetic similarity or relatedness.

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: new phenotype | 1 | METPO:1000059 phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

This reusable organism-level disposition is neither a recognition gene nor an
individual pairing result. No universal genetic-distance threshold, cognition,
obligate killing, or monotonic distance-response relationship is required.
The record remains `PROPOSED`; no exact synonyms, xrefs, SSSOM mappings,
canonical taxa, protein examples or causal graph are asserted.

## Evidence And Definition Authority

- [Ostrowski et al. 2008](https://doi.org/10.1371/journal.pbio.0060287),
  PMID:19067487: preferential coaggregation, partial sorting, microsatellite
  distance rather than genome-wide identity.
- [Stefanic et al. 2015](https://doi.org/10.1073/pnas.1512671112),
  PMID:26438858: relatedness-associated swarm merging; directly read scientific
  abstract only. Full text, figures and supplements remain inaccessible.
- [Lyons and Kolter 2017](https://doi.org/10.1128/mBio.00723-17),
  PMID:28679746: nonkin exclusion extending to nearby species, with varied
  outcomes farther away. Its Introduction distinguishes both discrimination
  modes. This is the definition authority for the attributed broader scope.

The 2015 source defines conspecific discrimination; the 2017 paper expressly
extends it. Both usages remain attributed, not silently harmonized. The three
corrected snippets are contiguous scientific-abstract result spans. Native
verification returned three `VERIFIED` rows; scientific-section identity was
checked separately. The [source sidecar](../../research/traits/ecology/kin_discrimination-source-verification.json)
preserves actual outcomes, hashes, stable URLs and bounded inspection scope.

QS45 appears in the 2008 Methods but not its retrieved strain table. The 2017
Figure 2A/2C labels WNC032 with different species; Data Set S1 assigns it to
B. megaterium. Neither discrepancy is silently resolved. The 2017 relatedness
proxy is type-strain 16S, not whole-genome identity of every isolate. Selected
figures and spreadsheet checks are not statistical replication or complete
supplement review. The 2015 and 2017 papers share an investigator. Bounded
metadata checks and publisher access limits do not establish exhaustive notice
clearance. Full publications are retained locally, not redistributed.

## Hierarchy Decisions

`METPO:1000059` phenotype is the conservative broader class. The active parent
was inspected in pinned and current released METPO RDF; its parent is
`METPO:1000188`. No active exact kin-discrimination term was identified in the
inspected ontologies, templates, local corpus and pending changes. The only
broad lexical ontology hit was obsolete compatible solute, not an identity
candidate. The pinned ontology remains unchanged.

Mutualism (000041) requires reciprocal benefit; biofilm formation (000053) is
neither necessary nor sufficient. Outer membrane exchange (000650) is material
transfer and explicitly separates a negative kin-discrimination result.
Heterokaryon incompatibility (000606) is postfusion restriction, not automatically
equivalent or reparented. DNA self/nonself defense and predation have different
targets or endpoints. No exact older node, synonym or parent TODO requires
migration in the inspected scope. Kin recognition and allorecognition are not
automatically exact synonyms; allele specificity is not genome-wide sensing.

## Novelty And Reservation

Acceptance confirmation: `2026-10-13T09:09:53Z`; current main and refreshed
origin/main: `0f58024643a5357500f2eccb805bd4d9368de8eb`.
Searches included ignored and hidden files. The local audit covered 164
registered or retained locations, including 15 independent recovery copies.
Unavailable worktrees received tracked-history fallback, not reconstructed
untracked files. Alias history was restricted to named maintained-owner trees.

Fresh remote checks covered 11 open/draft PRs and 783 nonremoved changed-file
blobs, plus 587 selected upstream blobs. Relevant PRs: TraitMech #1782, #1476,
#973 and draft #924; CommunityMech draft #935; METPO #644, #643, #641, #640,
#638 and #629. Pagination, file counts, Git blob/SHA-256 identities and stable
before/after heads were checked.

- METPO main: `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- CommunityMech main: `8df89370be840a4b58a9d8a7407c66c7471a5085`.
- KG-Microbe main: `bb3072f59f6d9e098ae40c4dce2c60a9dec9af42`.

The only exact numeric string hit was embedding coordinate `-0.1066948` for
`METPO:1001002` in draft #924, not an identifier. Of 154 raw interval overlaps,
147 concern the formal editor namespace envelope or earlier documentation;
seven are partial numeric matches in Biopython chromosome/alignment fixtures.
All were explicitly adjudicated, leaving no conflicting reservation in scope.
These are bounded checks, not atomic allocation or global proof of novelty.
Lost ignored/untracked files, archives, symlink directories and unchanged
pending-tree files are not reconstructed. Recheck before publication.

## ID Space And Files

- Local identifier: `traitmech:000716`.
- Cohort: `metpo_traitmech_v592`.
- Reserved block: `METPO:1066900`-`METPO:1066999`.
- Only populated placeholder: `METPO:1066900`, not a released identifier.
- Subset: `metpo_traitmech_2026_10`; curator: codex.
- The block does not overlap CommunityMech v1 or its documented extensions.

| Artifact | Rows |
|---|---:|
| `metpo_proposal_classes_robot.tsv` | 2 headers + 1 class |
| Property template | 0; omitted |
| SSSOM mapping template | 0; omitted |

The two 11-column headers match the pinned upstream class template, including
required blank ROBOT cells. Definition citations are provenance, not equivalence.

## Verification And Upstream Path

Before publication: strict/schema validation, focused and full tests, native
snippet verification, proposal verification, ROBOT/ELK and parsed RDF parent
checks, generated products, full QC, history and saved successor review.
This requirement list is not a claim that unfinished checks have passed.

After curator sign-off, submit the TSV and narrative to METPO or KG-Microbe.
Adoption requires a separately reviewed pinned release refresh and identifier
migration preserving the old local ID's provenance and incoming references.
The placeholder does not authorize a silent ID swap or REVIEWED promotion.

## Change Log

- 2026-10-13, v592: one relational ecological phenotype with three DOI excerpts.
- Before publication, #1909/#1910: corrected excerpt self-containment and
  definition authority, retaining original curation and append-only history.
