# METPO proposal v548: baeocyte formation

## Context

Lift `traitmech:000672`, minted by codex for a reusable cyanobacterial
reproductive morphology absent from the pinned METPO ontology. The definition
is supported by DOI:10.1007/s10482-021-01672-x; PMID:18365724 supplies a
separate primary microscopy study and a division-sequence constraint.
The record remains `PROPOSED`, pending human review and upstream adoption.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait class | 1 | phenotype METPO:1000059 | 1 |
| B: causal predicates | 0 | not applicable | 0 |
| C: schema enums | 0 | not applicable | 0 |

The new identifier is used by one TraitRecord. No unsupported protein graph,
property, synonym or external equivalence is proposed.

## Hierarchy decisions

Use active phenotype `METPO:1000059`, below quality `METPO:1000188`.
Binary fission `METPO:1000033`, reproductive process `METPO:1000264` and
reproductive structure `METPO:1000265` are obsolete. The existing sporulation
record `METPO:1000870` describes dormant resistant endospores, not this trait.
Coenobium formation `traitmech:000655` has a colony-development criterion that
multiple fission alone does not satisfy. Historical nanocyte/endospore usage
is an open terminology question, not an exact synonym assignment.

Formation, release and growth are distinct stages. The definition does not
require simultaneous cleavage, a fixed count or diameter, a particular release
route, motility, dormancy, an invariant sheath state or a gene profile.
The KI4 example retains its non-axenic culture and strain-level taxonomy
qualifiers. Paper supplements and the Russian full paper behind PMID:18365724
were not inspected; the directly retrieved English abstract is the cited text.
No protein-resolved mechanism is claimed from genome annotations or images.

## ID space and subset

Reserve **METPO:1062500-1062599**; the single row is **METPO:1062500**.
Subset: `metpo_traitmech_2026_10`. Local fallback: `traitmech:000672`.
This fresh block follows v547 (1062400-1062499) and does not overlap the
CommunityMech v1 or its v1.1/v1.2 extensions, all inspected before writing.

At allocation, main was `d59d8c1b16836c9fe457f7c1a0d479b6bfe083cc`.
Ignored-and-hidden searches covered all 15 then-existing TraitMech worktrees,
the whole CommunityMech checkout and a complete pending-PR snapshot. Exact
IDs, the whole block, cohort names, lexical variants and both citations were
checked; numeric substring hits in dependencies and coordinates were not
reservations. The pinned METPO graph had 12,617 triples and no matching
baeocyte/nanocyte/multiple-fission literal. The old morphology frontier's
baeocyte mention is a lead, not a prior allocated record. Existing
multiple-fission mentions describe coenobia or a different bacterial morphology.

All open heads, including drafts, were checked through paginated file lists:

| PR | Head at allocation | Curation reservations |
| --- | --- | --- |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed trait/proposal/history paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed trait/proposal/history paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed trait/proposal/history paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed trait/proposal/history paths |

Recheck main, worktrees and open heads before publishing; this is an allocation
snapshot, not a claim that remote state cannot change.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 2 headers + 1 class | upstream template |
| `proposal.md` | not applicable | review narrative |
| properties / SSSOM | omitted | no predicate or verified equivalent |

## Verification

The pinned upstream class/property headers were rechecked at kg-microbe commit
`1408e7099d039026d7611c240938d8e177753406`: blobs
`b590cf303dc2fbdd57bed021668641cd0c32396d` (11-column classes) and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (13-column properties).
The class template retains the three empty trailing directive cells.

Required before merge:

```bash
just verify-proposal metpo_traitmech_v548
just robot-validate-proposal metpo_traitmech_v548
```

Inspect RDF, not only the ROBOT exit status: proposed and parent IRIs must use
`https://w3id.org/metpo/`, with the parent's label and quality ancestry intact.
Keep the maintained snippet resolver's verdict separate from direct reading
of the publisher's genus Description and PubMed's scientific abstract.

## Upstream path

After TraitMech review, submit the TSV and this narrative to berkeleybop/metpo
or the kg-microbe proposal pipeline. This reserved ID is not a released METPO
term. No separate upstream issue is claimed.

## Round-trip plan

After upstream acceptance, refresh `data/raw/metpo.owl`, re-seed and migrate
the record and references to the accepted METPO identifier. Preserve the old
`traitmech:000672` as traceability metadata, not an asserted lexical synonym.
Keep curation and repository history intact.

## Change log

- v548, 2026-10-08: one source-qualified baeocyte-formation phenotype.
