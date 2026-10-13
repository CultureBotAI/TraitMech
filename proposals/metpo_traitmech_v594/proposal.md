# Fungal Nematode-Trap Formation

## Context And Scope

One Scope-A morphological CLASS, `traitmech:000718`, proposed as
`METPO:1067100`: **fungal nematode-trap formation**. A fungus differentiates
hyphae into specialized nematode-capturing structures. This supplies the
missing shared parent requested by five existing trap-formation records.

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: new phenotype | 1 | METPO:1000059 phenotype | 0; five existing children |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

Formation is distinct from maturation, capture, killing, penetration,
digestion and assimilation. Morphologically complete immature traps are
included. No universal inducer, medium, protein inventory or immediate
capture guarantee is asserted. The five children are not an exhaustive or
disjoint partition. Taxonomic membership, generic hyphae, fusion, attraction,
nematicidal activity or a sequence annotation alone is insufficient.
No exact synonym, xref, SSSOM mapping, canonical example, protein example or
causal graph is added to the parent. The record remains `PROPOSED`.

## Evidence

- [Ji et al. 2020](https://doi.org/10.1016/j.isci.2020.101057),
  PMID:32339992: scientific Summary, main text, actual Figure 1 and selected
  supplemental pages support the morphological umbrella. Four representative
  trap types are not an exhaustive classification. Native excerpt result:
  `VERIFIED`. Gene-family and expression associations are not causal proof.
- [Yang et al. 2011](https://doi.org/10.1371/journal.ppat.1002179),
  PMID:21909256: directly matched Author Summary and actual Figure 1 support
  adhesive networks and separate predation stages. The Author Summary is not
  the scientific abstract; native result remains `NOT_IN_ABSTRACT`. Shared
  authors with Ji do not establish independent-laboratory replication.
- [Chen et al. 2023](https://doi.org/10.1038/s41467-023-43235-w),
  PMID:37968349: directly matched Results and actual Figure 1 distinguish
  ring differentiation from inflation competence. Native result remains
  `NOT_IN_ABSTRACT`. Separate induction and inflation assays are not universal
  requirements; later mechanism figures and supplements were not fully audited.
- [Saikawa and Takahashi 2002](https://doi.org/10.1007/s102670200061):
  all three [PDF pages](https://www.jstage.jst.go.jp/article/mycosci/43/5/43_MYC43417/_pdf)
  and their figures support nonconstricting-ring inclusion. The Figure 8
  excerpt directly matches; native resolution remains `UNRESOLVED` for its
  exact DOI query, not a claim of universal non-indexing. Earlier adhesive
  ultrastructure observations are attributed, not new experiments here.

The [source sidecar](../../research/traits/morphology/fungal_nematode_trap_formation-source-verification.json)
retains raw-response hashes, exact sections, snippets and bounded inspection
claims without redistributing full publications. Cell/Crossmark access failed;
PubMed, Crossref and three publisher records were inspected. Yang's linked
`CommentIn` is not a correction designation or positive experimental evidence.
These checks are not comprehensive notice clearance.

## Hierarchy Decisions

The parent is `METPO:1000059` phenotype, itself below `METPO:1000188`.
Mycelial growth (000074) is explicitly bacterial; hyphal anastomosis (000605)
denotes fusion. Neither is the exact umbrella. Autophagy and myzocytosis have
different endpoints. Nutritional nematophagy is not an exact synonym.

The five existing definitions entail specialized hyphal trap formation.
This coupled change replaces their direct local phenotype parent with
`traitmech:000718` and resolves only their parent-gap discussions. Historical
rationales, evidence, examples, other uncertainties and curation events remain.

| Existing TraitMech child | Existing cohort | Requested additional axiom |
|---|---|---|
| 000677 constricting ring | v553 | METPO:1063000 SubClassOf METPO:1067100 |
| 000678 adhesive net | v554 | METPO:1063100 SubClassOf METPO:1067100 |
| 000679 adhesive knob | v555 | METPO:1063200 SubClassOf METPO:1067100 |
| 000680 nonconstricting ring | v556 | METPO:1063300 SubClassOf METPO:1067100 |
| 000681 adhesive column | v557 | METPO:1063400 SubClassOf METPO:1067100 |

The one-row ROBOT template emits the new parent, **not these five additional
axioms**. Apply them when integrating the cohorts upstream. Preserve the older
TSVs and their still-valid broader phenotype axioms; no child ID is reminted.

The column child retains its narrower serial-cell definition. Ji's main
Introduction supports serial cells, while Transparent Methods page 12 allows
one or more. A separate OPEN discussion requests reconciliation with knob
terminology; it is not silently resolved by this parent. YMF1.00569 in the
2020 supplement is not the 2016 child's YMF1.01472. Source inconsistencies
about ring-isolate origin and adhesive-layer measurements remain qualified.

Pinned and current METPO lexical hits `METPO:0000261`, `METPO:000262` and
`METPO:1000125` are deprecated fungal-spore concepts, not exact counterparts.
No replacement/consider annotation was observed. `OMO:0001000` reasons do
not invalidate biology or authorize identifier reuse; retain numeric spellings
exactly and do not add them as xrefs. The pinned ontology is unchanged.

## Novelty And Reservation

Acceptance: `2026-10-13T13:31:56Z`. Main:
`e7207688b2a55056698d31b83a3f3fee0f97b23c`.
Ignored and hidden files were included in 168 known local locations; an
existing directory was not assumed to be a complete checkout. Unavailable
registered worktrees received retained tracked-history checks with positive
regex controls. The sidecar records the completed scope and dispositions.

Remote screening covered 11 open/draft PRs, 783 nonremoved pending blobs and
587 selected upstream blobs with hashes, pagination and stable heads checked.
Pending: TraitMech #1782, #1476, #973 and draft #924; CommunityMech draft #935;
METPO #644, #643, #641, #640, #638 and #629. Reservation refresh retained the
same heads as the novelty audit.

- METPO main: `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- CommunityMech main: `8df89370be840a4b58a9d8a7407c66c7471a5085`.
- KG-Microbe main: `bb3072f59f6d9e098ae40c4dce2c60a9dec9af42`.

Thirteen exact-number matches are decimal measurements `876.1067184` in
retained reference caches. The remaining `1.1067159` is an embedding value
for METPO:1005014 in draft #924. None is a term reservation. All 259 interval
overlaps denote the broad `1000000-1999999` editor envelope or documentation
of it, not narrower reserved blocks. No competing reservation remained in
the inspected scope. Recheck before publishing; this is not atomic allocation.

Lost ignored/untracked history, directory symlinks and undecoded archives are
not reconstructed. Pending-file checks do not inspect every unchanged PR-tree
file. Reference-cache hits are research leads, not automatically trait records.
These are bounded checks, not global novelty proof or discovery exhaustion.

## ID Space And Files

Local `traitmech:000718`, cohort `metpo_traitmech_v594`, reserves the whole
`METPO:1067100`-`METPO:1067199` block. Only `METPO:1067100` is populated;
it is not a released identifier. Subset: `metpo_traitmech_2026_10`; curator:
codex. No overlap with inspected CommunityMech v1 or extensions was found.

| Artifact | Rows |
|---|---:|
| `metpo_proposal_classes_robot.tsv` | 2 headers + 1 class |
| Property template | 0; omitted |
| SSSOM template | 0; omitted |

Both 11-column headers follow the pinned upstream class template, retaining
the required blank cells. Citations are not equivalence mappings. METPO IRIs
must expand to `https://w3id.org/metpo/`, not a legacy OBO stub.

## Verification And Upstream Path

Required before publication: strict/schema validation of all six records,
guarded-writer tests, native snippet checks with manual full-text assessment,
proposal coverage, ROBOT/ELK and RDF parent inspection, history, generated
products, full QC and a saved adversarial batch review. This is a requirement,
not a claim that unfinished checks passed.

After curator sign-off, submit the template and five additional hierarchy
axioms to METPO or KG-Microbe. Adoption requires a separately reviewed pinned
release refresh and identifier migration preserving local provenance and
incoming references. Neither the placeholder nor passing automated checks
authorizes automatic `REVIEWED` promotion.

## Change Log

- 2026-10-13, v594: one morphological parent, four DOI excerpts and five
  narrowly scoped child-parent refinements.
