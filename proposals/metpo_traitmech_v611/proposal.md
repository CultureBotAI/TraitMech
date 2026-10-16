# Bacterial Flagellar Filament Internalization

## Context And Scope

Propose **bacterial flagellar filament internalization**, `METPO:1068800`, for
`traitmech:000735` (`PHYSIOLOGY`, `CLASS`, `PROPOSED`). This is a reusable
physiological phenotype, not a flagellar structure or source-specific locus.

Definition: A physiological phenotype in which a bacterium withdraws an
assembled portion of its own flagellar filament from outside its cell body
into its cell-body periplasm.

| Scope | Classes | Predicates | Enum Lifts |
|---|---:|---:|---:|
| A: one local trait | 1 | 0 | 0 |
| B: causal predicates | 0 | 0 | 0 |
| C: schema enums | 0 | 0 | 0 |

## Hierarchy Decisions

Phenotype `METPO:1000059`, below quality `METPO:1000188`, is a
definition-based broader parent inference. Locomotion is not required.
Cell-body periplasm excludes a lumen inside an external flagellar sheath.
Static endoflagella, abnormal assembly, import of free flagellin, uptake of
another cell's material and predator entry into prey periplasm do not establish
withdrawal of the cell's own assembled filament.

Partial withdrawal counts; permanent intactness and complete withdrawal are
not required. Bacterial polar ejection (`traitmech:000732`) releases structures
externally. Eukaryotic axoneme internalization (`traitmech:000734`) involves a
different apparatus. These distinctions do not imply disjoint organisms.
Neither a universal early-entry time nor a requirement for motor displacement,
P/L-ring separation, sheath zippering, lipid effects, proteases, complete
digestion or recycling is asserted. Sequence features and flagellin expression
alone cannot establish this phenotype. Canonical taxa, exact synonyms, xrefs
and a universal protein-resolved graph remain omitted pending their own review.

## Evidence And Limits

1. [Kaplan et al. 2023](https://doi.org/10.1038/s41564-023-01401-2),
   PMID:37349588, PMC11061892.1, is the definition authority. The 11-word
   excerpt is in Results S3, Attachment of B. bacteriovorus to prey, the
   paragraph beginning In cells with larger portions; direct JATS was checked.
   HD100 frozen cryo-ET stages show partial through nearly complete withdrawal
   into the predator's own periplasm, not the prey's. Methods S8-S12 qualify
   minicell enrichment and possible physiology effects. Frozen stages are not
   same-cell trajectories. Main Figure 3 and supplement PDF pages 1, 22-35,
   66-67 were visually inspected, not all 67 pages. S20-S21 distinguish external
   and internal portions; S22 is a schematic. Table S2's 8/4/30 observations are
   feature counts, not culture replicates or a prevalence denominator. S15/S16
   and S19 measure different ring distances. The publisher's 100 nm main Figure
   3 scale bar differs from the manuscript caption's 50 nm; neither is silently
   substituted. Main PDF, other actual main figures, unselected supplemental
   images, movies, peer responses and raw data remain unread.
2. [Kaplan 2024](https://doi.org/10.1063/pt.nkma.bqid), Physics Today,
   supplies a 13-word excerpt in the Figure 5 caption. Direct publisher HTML,
   Disassembly processes, reference 16 and actual Figure 5 were checked.
   This is a distinct author-perspective publication about the same 2023
   experiment, **not independent experimental replication**. Colored
   segmentation is not another experiment. Presumed digestion and the proposed
   evolutionary connection to spirochaete endoflagella are not established
   consequences or defining requirements.
3. [Lambert et al. 2006](https://doi.org/10.1111/j.1365-2958.2006.05081.x),
   PMID:16573680, PMC1453311.1, is **comparison context only**, stored in a
   discussion as `NO_EVIDENCE`, not a third definition citation. Its 14-word
   excerpt was checked directly in Results, Flagella are not always shed upon
   prey entry. Source strain 109J with flagella-minus E. coli DFB225 prey is not
   pooled with HD100. Approximately 80% of more than 100 assessable early
   bdelloplasts had externally retained flagella; aggregates were excluded and
   the whole-population proportion may be overestimated. The complement is
   not an internalization frequency. Actual Figure 1 was inspected at 456 by
   390 pixels. Twenty minutes after mixing is not withdrawal duration; PTA
   staining differs from cryo-ET. Other actual figures, supplements and main
   PDF remain unread. Retention does not establish absence of later or partial
   internalization.

Native snippet outcomes remain `NOT_IN_ABSTRACT`, `UNRESOLVED` and
`NOT_IN_ABSTRACT`, respectively; direct full-text matches are separate checks.
The second outcome means no usable abstract was returned, not an invalid DOI.
Only the local record and the 2023 DOI annotate the definition. No unqualified
canonical taxon is asserted from a transient experimentally enriched state.

The [source receipt](../../research/traits/physiology/bacterial_flagellar_filament_internalization-source-verification.json)
retains source identities, locators, hashes, native outcomes and access limits.
Qualified MED and Crossref notice checks are bounded, not comprehensive
correction/retraction clearance. The linked 2023 post-publication review,
DOI:10.3410/f.742690890.793599662, remains unread; failed access is not a negative
notice search. No raw-data reanalysis, paid research or human sign-off is implied.

## Identity And Reservation

Allocated at 2026-10-16T01:41:19.482095+00:00 after the stable
2026-10-16T01:40:20.324460+00:00 guard, based on main
`aa5f955e20f904859dfd7016a1ffb7fce039c0c7`: local `traitmech:000735`, cohort
v611 and full block `1068800-1068899`. Only `METPO:1068800` is populated,
in subset `metpo_traitmech_2026_10`.

The local scan covered 213 known current locations, 310 retained heads,
89,818 TraitMech and 9,308 CommunityMech unique regular Git blobs, including
ignored and hidden files. Twelve copies were unavailable, including the
deliberately removed prior-unit worktree; its two independent recovery clones
were included. Of 324 biological contexts, 307 retained byte-verified prior
assessments and all 17 new contexts were read. They concern EET, nutrient
uptake, eukaryotic resorption, predatory research leads, ixotrophy or explicit
scope contrasts, not an existing equivalent accepted trait. All 76 local
allocation contexts concern broad editor envelopes, not a narrower reservation.

The remote snapshot covered 12 open/draft PRs, 784 nonremoved changed blobs
and 587 selected upstream blobs: TraitMech #1938, #1937, #1936, #973 and
draft #924; CommunityMech draft #935; METPO #644, #643, #641, #640, #638 and
#629. Eight biological matching pages were byte-identical to previously
assessed pages. The two new matching owners concern nutrient uptake and
flagellin-associated EET. Existing predatory-bacterium edges cite the 2023
study for other stages, not an internalization node. Three exact numeric
matches were parsed as decimal embedding cells, not identifiers. Complete
range checks covered 211,271 owner contexts and 2,627 unique contents;
31 of 32 matching contents describe the general 1000000-1999999 editor
envelope and one contains the numeric embedding false positives.

The [allocation receipt](../../research/traits/physiology/bacterial_flagellar_filament_internalization-allocation.json)
retains pinned heads, input hashes, dispositions and scope limits. The final
guard verified unchanged source hashes, worktree catalogs, upstream heads and
PR heads/bases/descriptions/draft states. No competing reservation remained in
this inspected scope. This is not an atomic lock or literature exhaustion.
Lost ignored history, symlink targets, arbitrary archives and unchanged PR
files are not reconstructed. Refresh remote reservations before publication.

Pinned/current METPO releases and templates distinguish possession and static
arrangement from withdrawal. Active flagellated `METPO:1000704` and axially
filamented `METPO:1000705` are not equivalent. Deprecated `METPO:0000089`
and `METPO:000090` carry OMO:0001000; `METPO:1000381` carries IAO:0000226;
their replacement is `METPO:1000704`. Deprecated flagellum `METPO:1000123`
carries OMO:0001000 with no observed replacement/consider annotation. None is
reactivated or asserted as an exact xref. Reason-code interpretation remains
separate from equivalence. The ontology pin is unchanged; the metadata-only
editor is not the complete release.

## Files And Verification

| Artifact | Content |
|---|---|
| `metpo_proposal_classes_robot.tsv` | One class, canonical 11-column headers |
| `proposal.md` | Scope, evidence, reservation and upstream path |
| Properties and SSSOM | Omitted: no predicates or equivalent mappings |

Headers were checked against KG-Microbe at
`1acb8b61fcae24fafc0640b1bf6e5be669f315f9`; the v610 dependency is hash-guarded.
Run the native proposal verifier and ROBOT/ELK wrapper, then inspect actual
`https://w3id.org/metpo/` child-parent-quality IRIs and definition annotations.
This instruction does not claim unrun gates passed.

## Upstream Path

Submit the reviewed class upstream separately. The placeholder is not released.
After acceptance and release, separately review scope, update the ontology pin,
re-seed and migrate the local identifier while retaining its prior spelling for
traceability. No upstream submission or human scientific approval is implied.

## Change Log

- 2026-10-16, v611: propose one bacterial own-filament internalization phenotype.
