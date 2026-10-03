# METPO Proposal v449: Lamassu Type II System

## Context and Scope

One Scope-A class lifts `traitmech:000572`, an organism-level possession
trait for LmuC-containing Lamassu architecture. It is neither an isolated
protein nor a source-database row. Scope B and C have zero rows; no exact
external equivalence or SSSOM mapping is asserted.

## Evidence and Boundaries

[Payne et al.](https://doi.org/10.1093/nar/gkab883) define the additional
LmuC-containing subtype as type II. The stored full-text sentence includes
the exact synonym. Its counts describe that study's RefSeq v201 survey,
not a universal frequency. The Methods and Figure 3 identify DSM 9628 as
the source of a locus amplified from genomic DNA and tested in E. coli
BL21-AI. The example is source-strain possession, not native-host activity.

[Li et al.](https://doi.org/10.1038/s41589-025-02102-z) independently use
the type-I/type-II classification in a structural study. The second exact
snippet is a contiguous abstract span naming both source-qualified
complexes, including the type-II V. cholerae complex. It does not transfer
one nuclease mechanism to every effector architecture. These citations
are two independent studies, not an article and its supplement.

NCBI Nuccore resolves the Methods accession `NZ_HG322949.1` to
Janthinobacterium agaricidamnosum DSM 9628 and strain taxon
`NCBITaxon:1349767`. NCBI Taxonomy independently confirms the complete
label `Janthinobacterium agaricidamnosum NBRC 102515 = DSM 9628`.
No assembly accession or species-wide assertion is inferred.

Type II denotes the additional LmuC component, not exactly three genes,
a long/short LmuB family, an isolated LmuC hit, a fixed effector chemistry,
or demonstrated universal LmuC essentiality. No new causal graph is
asserted without resolving protein anchors and the scope of mechanistic
generalization. Type I remains a distinct discovery lead.

## Hierarchy

The parent is Lamassu system (`traitmech:000232`; v109 `METPO:1018600`).
Three existing biological definitions already require LmuC. The local
hierarchy is therefore refined by definition-based inference:

| Existing trait | Historical placeholder | Added superclass |
| --- | --- | --- |
| Hydrolase-Protease, `traitmech:000567` | v444 `METPO:1052100` | `METPO:1052600` |
| HNH, `traitmech:000568` | v445 `METPO:1052200` | `METPO:1052600` |
| SMEK, `traitmech:000569` | v446 `METPO:1052300` | `METPO:1052600` |

HNH retains short Lamassu (`traitmech:000570`, `METPO:1052400`) as an
additional parent. LmuC presence and LmuB-length family are separate
axes. Hydrolase-Protease has a paired effector module, so the new class
deliberately does not impose an exact three-gene count. SMEK's long-profile
exception remains unresolved and does not prevent this component-based
classification. None of these refinements is new experimental validation.

Historical proposal IDs and broader parent axioms are retained because
they remain true. On upstream minting, add the three superclass axioms
above and retain the previously proposed HNH short-family axiom. Legacy
detector-defined effector records and the whole long/short families are
not reparented from optional component calls or name similarity.

## Identifiers and Files

Reserve `METPO:1052600` in the next unused hundred block after v448's
`METPO:1052500`; use subset `metpo_traitmech_2026_10`.

| Artifact | Scope | Rows |
| --- | --- | ---: |
| `metpo_proposal_classes_robot.tsv` | A | 1 |
| Property template | B, not applicable | 0 |
| SSSOM mappings | No exact equivalence asserted | 0 |

Whole-repository ignored-and-hidden searches found no exact record,
METPO class or identifier collision. Existing LmuABC mentions belong to
the broad parent's scoped mechanism or narrower architecture records.
The shared PADLOC citation in Hma supports a distinct system, not this
class. A fresh 399-record seed projection against 966 live records yielded
55 exact-ID leads already classified as 17 duplicates and 38 supporting
properties in the release review.

## Verification and Upstream Path

The dry-run-first writer prevalidates all five changed records and rejects
identity, definition, hierarchy, discussion and output drift. Test parent
preservation, HNH's dual classification, idempotence and failure before
any live write. Verify both source spans directly, resolve the exact
taxon/accession, validate histories, regenerate artifacts, run proposal
verification, ROBOT/ELK, full QC and the full suite before merge.

Submit under [METPO #535](https://github.com/berkeleybop/metpo/issues/535).
After human review and minting, refresh METPO, replace temporary local IDs
with assigned identifiers while retaining provenance, and translate the
three new child axioms plus HNH's retained short-family relation. Bot
review does not promote this record from PROPOSED to REVIEWED.

## Change Log

- v449, 2026-10-03: propose the LmuC-containing Lamassu class and document
  three existing child refinements with two independent primary sources.
