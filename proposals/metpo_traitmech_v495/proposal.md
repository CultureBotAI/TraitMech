# Tripolar Mating System: METPO Proposal v495

## Context

Lift `traitmech:000618 tripolar mating system`, a PROPOSED PHYSIOLOGY
class. Whole-repository searches included ignored and hidden files, labels,
hyphenated variants, citations, identifiers, discussions, graphs, research,
history and generated pages. No exact record, prior proposal or allocation
collision was found before writing. The available sibling CommunityMech
proposal tree was also searched with ignored and hidden files included.

The pinned 12,617-triple METPO graph contains no matching mating-system
literal. A fresh 399-record seed compared with the 1,012-record pre-addition
corpus has 344 present and 55 absent IDs. Both frozen release-review tables
classify all 55 as 38 supporting-field rows and 17 duplicates. The all-state
upstream tripolar issue search returned no results on 2026-10-05. Paginated
file inventories of open PRs #1477, #1476, #973 and #924 contain no competing
trait or proposal allocation. This does not establish discovery exhaustion.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

This is a reusable, experimentally demonstrated mating-system phenotype,
not an individual sequence feature or a record of a single experimental
observation. Its unit is a cross or system with differently organized
partners: one linked mating-type region versus two unlinked regions.
It must not be assigned unqualified to either parental species, or interpreted
as three mating types or three independently segregating loci per genome.

Uniform single-factor (`traitmech:000616`) and two-factor
(`traitmech:000615`) compatibility systems are not exact equivalents.
Pseudobipolar mating (`traitmech:000617`) concerns recombination-permitting
chromosomal colocation, not the asymmetric parental organization here.
The sources' heterothallic framing does not establish universal
separate-partner dependence under `traitmech:000610`; progeny self-fertility
can differ. No disjointness is asserted.

Use released `METPO:1000059 phenotype`, with `METPO:1000188 quality`
ancestry, in both record and template. A narrower relational-phenotype
hierarchy needs curator review. PHYSIOLOGY is a filesystem category, not an
ontology parent. PROPOSED status is retained pending human signoff.

## Evidence and Limitations

- `DOI:10.1128/ec.00271-08`, `PMID:18723606`, `PMC2568056`:
  the first tripolar-cross Results subsection supplies the definition snippet,
  exact-matched against raw PMC HTML. Engineered C. neoformans crosses support
  function through germinating and segregating progeny. Methods, relevant
  Results and Discussion were read. Actual Figure 1 shows filamentation;
  Figure 2 is a genotype model. Other actual figures and supplements remain
  uninspected. Multiple SXI2a copies in JF289 and strain-specific outcomes
  preclude a universal fertility fraction or sterility rule.
- `DOI:10.1128/mbio.00059-26`, `PMID:41841731`, `PMC13059729`:
  the Results s2-2 snippet is exact-matched against raw Europe PMC full-text
  XML, not the scientific abstract or IMPORTANCE section. Engineered
  C. amylolentus MAT-fused partners cross with wild-type unlinked partners.
  Relevant construction, mating and sequencing Methods and Results s2-4
  were read. Its 42 sequenced progeny include 26 tripolar progeny, not 42.
  Figure 2/4 captions were read, but actual figures and supplements remain
  uninspected after image endpoints failed. Other source sections remain
  unread. Bilateral bipolar-cross defects do not establish tripolar defects.

Both sources test engineered systems; neither establishes natural prevalence
or proves the proposed ancestral evolutionary trajectory. No natural
canonical example is inferred. Keep genotype, filamentation, germination,
meiosis and later mating ability distinct. Full-text snippet checks do not
replace the abstract resolver's actual verdicts. Two CURATION_TODOs retain
hierarchy, source and mechanism gaps; no protein accession, xref, synonym or
causal graph is introduced, and no NONMECHANISTIC workaround is used.

## ID Space and Subset

Reserve `METPO:1057200` in `1057200-1057299`, after v494's block.
Subset: `metpo_traitmech_2026_10`. This does not overlap CommunityMech v1's
`1007100-1007220` range. Keep `traitmech:000618` until upstream acceptance
and release; the placeholder is not a released METPO identifier.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or SSSOM template is needed. The 11-column class header follows
Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018`, including three empty trailing
directive cells. The expected local contract is absent, so its pinned copy
is reused. CommunityMech v1 is the worked reference. Legacy OBO-prefix
examples do not override the ontology's actual w3id IRIs.

## Verification

```bash
just verify-proposal metpo_traitmech_v495
just robot-validate-proposal metpo_traitmech_v495
just audit-proposal-coverage
just qc
```

Check record/template label, definition and parent parity. Inspect emitted
`https://w3id.org/metpo/` IRIs, the actual phenotype label and quality
ancestry; ELK success with a detached parent is insufficient.

Local proposal verification passed with zero failures and complete
cross-cohort coverage of 618 local IDs. ROBOT/ELK passed without UNSAT;
merged/reasoned output has 23,322/23,326 lines. Structured inspection
confirmed the proposed w3id class is below the labeled phenotype parent
and its quality ancestor. Both snippets returned `NOT_IN_ABSTRACT` in the
maintained resolver and separately matched their raw full-text passages.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` after local review.

## Round-Trip Plan

After upstream acceptance and release, refresh the ontology and migrate to
the accepted METPO CURIE. Preserve the local ID in an explicit migration
artifact and append-only history, regenerate dependent artifacts, and avoid
creating a duplicate primary record.

## Change Log

- v495, 2026-10-05: propose tripolar mating with two DOI-backed full-text
  snippets, cross-level scope and explicit engineered-source limitations.
