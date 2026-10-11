# METPO proposal v570: quorum quenching

## Context and scope

Lift `traitmech:000694` as `METPO:1064700`: one PHYSIOLOGY CLASS,
kept PROPOSED pending human signoff. Scope A: one class used in one record;
B/C: zero. This is a reusable microbial interference capability, not an
enzyme, peptide, sequence feature, chemical intervention or assay column.

## Hierarchy and boundaries

Parent phenotype `METPO:1000059`, below quality `METPO:1000188`, is used
in both the record and standalone TSV. Positive quorum sensing
`traitmech:000084` is not a broader class of quenching. A microorganism
may exhibit both capabilities; no organism-level disjointness is asserted.
Its existing AiiA and inhibitor nodes denote a protein and a chemical,
not unresolved exact phenotype nodes. No existing record needs repair.

Signal inactivation and inhibitory products are demonstrated routes,
not an exhaustive mechanism definition. Growth inhibition or reporter
toxicity alone is insufficient evidence. Neither AHL substrates, aiiA,
interspecies interaction, growth neutrality, a fitness benefit nor disease
prevention is universally required. Loss of sensing in a treated target
is not itself the actor's interference capability.

## Evidence and limits

- [Dong et al. 2004](https://doi.org/10.1128/AEM.70.2.954-960.2004),
  PMID:14766576, PMC348924: definition authority explicitly identifies
  quorum quenching with signal interference; coculture supports the
  microbial phenotype. The Results snippet is manually matched in full text,
  not in the abstract resolver (`NOT_IN_ABSTRACT`).
- [Dong et al. 2002](https://doi.org/10.1128/AEM.68.4.1754-1759.2002),
  PMID:11916693, PMC123891: whole-cell signal inactivation, not merely
  sequence homology. Authors overlap the 2004 study.
- [Williams et al. 2019](https://doi.org/10.1126/scitranslmed.aat8329),
  PMID:31043573, PMC7106486: a separate group supports non-AHL signaling
  interference. Native isolate and synthetic-peptide experiments remain
  distinct; the supplement could not be read.

All three quotations are short contiguous spans of directly retrieved source
text. Qualified `EXT_ID:<PMID> AND SRC:MED` results matched source, ID,
title and DOI on 2026-10-11; the two scientific-abstract snippets returned
native `VERIFIED`. Record notes state the exact reading/figure coverage,
strain caveats and condition-specific controls. Studies are not uniformly
independent replications. Unread sources are not counted as evidence.

Canonical taxa, taxon-paired protein mechanisms and mappings remain OPEN
pending authority and strain-provenance reconciliation. No graph, exact
synonym, xref or SSSOM equivalence is asserted. These are explicit curation
gaps, not claims that examples or mechanisms do not exist.

## Allocation and novelty

Reserve `traitmech:000694`, v570, and all of `METPO:1064700-1064799`;
populate only 1064700. Subset `metpo_traitmech_2026_10`. Allocation main:
`0d07de261f26685207a6592f69edbc85e3ab5fb3`.

Whole-repository searches across all 22 pre-existing worktrees included
ignored and hidden files, quenching/interference/inhibition variants,
autoinducer inactivation, AHL lactonase, DOI/PMID/PMC identities and the
entire candidate ID block. Relevant hits are molecular nodes, provenance
and research leads, not an exact record or prior proposal. An equally
inclusive CommunityMech block search found no conflicting reservation.

Fresh seeding produced 399 records; 55 IDs absent from 1,088 live records
are 38 supporting properties and 17 adjudicated semantic duplicates.
The 12,617-triple ontology has only an obsolete quorum-sensing label for
the searched signaling concepts, not an exact quenching term. The complete
1,546-row release delta, 153-row active-review table and active policy
were inspected. This bounded audit does not establish global exhaustion.

All open PRs, including drafts, were checked through complete paginated
file lists, immutable affected curation blobs and rechecked heads on
2026-10-11:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | Existing Shedu 000220; no new allocation |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

Recheck main and reservations immediately before publishing. Protected
spore germination and all unowned work are excluded.

## Artifacts and verification

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | One class, canonical 11 columns |
| `proposal.md` | Scope, allocation, evidence and round trip |
| Property/SSSOM templates | Not emitted: no predicate or justified mapping |

The three empty trailing directive cells are intentional. Upstream contract
commit `1408e7099d039026d7611c240938d8e177753406`, class/property blobs
`b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` supply the headers.
CommunityMech's legacy 12-column property table is not the canonical
13-column header. Use maintained w3id METPO IRIs, not OBO stubs.

The writer defaults to dry run, checks parent scope, prevalidates, refuses
target/proposal drift and supports exact replay. Require strict/LinkML,
native history/QC/products, proposal/ROBOT/ELK, source/snippet, focused/full
tests, preservation and desktop/mobile rendering checks. Actual outcomes
belong in the PR and immutable review, not assumed here.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream issue
or acceptance is claimed. On acceptance refresh the pinned ontology,
migrate identifiers and references, preserve minting provenance and
append-only history, and do not retain a duplicate primary.

## Change log

- v570, 2026-10-11: propose quorum quenching.
