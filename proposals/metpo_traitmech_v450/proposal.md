# METPO Proposal v450: Lamassu Type I System

## Context and Scope

Lift `traitmech:000573`, Lamassu type I system, as an organism-level
possession trait for a Lamassu locus encoding LmuA and LmuB without LmuC.
It is not an individual protein, an annotation failure or an engineered
type-II deletion. This resolves a component-class discovery lead already
named in the Lamassu parent, short-family and type-II discussions.

| Scope | Parent | Leaves |
| --- | --- | ---: |
| A: trait class | Lamassu system, `METPO:1018600` | 1 |
| B: predicates | Not applicable | 0 |
| C: schema vocabulary | Not applicable | 0 |

## Evidence and Boundaries

[Haudiquet et al.](https://doi.org/10.1073/pnas.2519643122) explicitly
identify the LmuC-loss architecture as type I in their Results paragraph
on effector diversity. The 24-word stored span includes the biological
absence claim, clade reference and exact naming. It is contiguous in the
full-text XML, not reconstructed from a detector table.

[Li et al.](https://doi.org/10.1038/s41589-025-02102-z) independently
distinguish type-I and type-II complexes in their abstract. The stored
15-word span retains both source-qualified complexes. These are two
independent primary studies. Full-paper biochemical generalization is
not claimed from an abstract or a structure deposition.

[Reviewed UniProt P0DW44](https://rest.uniprot.org/uniprotkb/P0DW44.json)
explicitly annotates the LmuA/LmuB type-I system in the NIO-1130 source
strain. Entry version 8, sequence version 1, was retrieved on 2026-10-03.
Its cited functional experiments expressed the system in B. subtilis
BEST7003; this is not evidence of native-host resistance.
[PDB 9UX7 entity 1](https://data.rcsb.org/rest/v1/core/polymer_entity/9UX7/1)
independently maps the source to P0DW44 and taxon 1761765, with E. coli as
the separate expression host. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1761765&mode=Info)
confirms the exact current label, Bacillus sp. nio-1130. The article's
B. cellulasensis name is retained only as source wording, not asserted
as a taxonomic synonym. No assembly or species-wide trait is inferred.

The canonical example cites the source-strain-specific UniProt annotation,
not a generic LmuB homology assignment. The PDB identity snippet is a
contiguous raw JSON span; no joined HTML blocks are presented as a quote.

## Hierarchy

The only parent is Lamassu system (`traitmech:000232`, v109
`METPO:1018600`). Type I is defined by component architecture, not a
short-LmuB length threshold or a fixed gene count. The reported clade S
belongs to the short family, but the entire short family is not type I;
clade O's effector-domain loss is a different observation. Broader
phylogenetic scope remains open, so no additional length-family parent
or model-derived child placement is asserted.

Existing parent, short-family and type-II records receive discussion links
and curation events only. Their definitions, parents, evidence, canonical
examples and older history are preserved. Their broader knowledge gaps
remain OPEN. Historical proposal files are unchanged.

Missing detector hits, incomplete assemblies, purified-complex omissions
and experimental knockouts do not establish the natural architecture.
Different loci can coexist in a genome, so the organism-level type-I and
type-II possession classes are not declared disjoint. No universal
effector chemistry, native-host resistance or causal graph is inferred.
No exact external equivalence or SSSOM mapping is asserted.

## Identifiers and Files

Reserve `METPO:1052700` in the next unused hundred block after v449's
`METPO:1052600`; subset `metpo_traitmech_2026_10`. Whole-repository
ignored-and-hidden searches found no exact record, METPO class or ID
collision. The existing mentions are broader scope or discovery leads.
A fresh 399-record seed projection against 967 live records yielded
55 exact-ID leads, whose release-review dispositions are duplicates or
supporting-field vocabulary rather than new primary traits.

| Artifact | Scope | Rows |
| --- | --- | ---: |
| `metpo_proposal_classes_robot.tsv` | A | 1 |
| Property template | B, not applicable | 0 |
| SSSOM mappings | No exact equivalence asserted | 0 |

## Verification and Upstream Path

The writer is dry-run-first, guards all three existing preimages, rejects
target and proposal drift, and prevalidates every changed record before
writing. Tests cover component scope, source-host separation, unchanged
hierarchy, full existing-record preservation, idempotence and fail-closed
behavior. Verify snippets directly, resolve the source taxon, regenerate
affected artifacts and pass proposal verification, ROBOT/ELK, full QC,
history validation and the test suite before merge.

Submit under [METPO #535](https://github.com/berkeleybop/metpo/issues/535).
After human review and upstream minting, refresh METPO and replace the
temporary local identifier with the assigned identifier while preserving
provenance. Bot approval leaves the record PROPOSED, not REVIEWED.

## Change Log

- v450, 2026-10-03: propose the LmuC-lacking Lamassu component class,
  reconcile three discovery links and document source-strain provenance.
