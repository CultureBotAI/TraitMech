# Eukaryotic Flagellar Resorption

## Context And Scope

Propose **eukaryotic flagellar resorption**, `METPO:1068600`, for
`traitmech:000733` (`PHYSIOLOGY`, `CLASS`, `PROPOSED`). The reusable phenotype
has no active exact METPO class within the inspected scope.

Definition: A physiological phenotype in which a microbial eukaryote shortens
previously assembled cilia or flagella through disassembly of their axonemes.

| Scope | Classes | Predicates | Enum Lifts |
|---|---:|---:|---:|
| A: one local trait | 1 | 0 | 0 |
| B: causal predicates | 0 | 0 | 0 |
| C: schema enums | 0 | 0 | 0 |

## Hierarchy Decisions

Phenotype `METPO:1000059`, below quality `METPO:1000188`, is a
definition-based parent inference. Locomotory flagellar possession is not a
required parent. Static short flagella, assembly failure, nonmotility, coiling,
passive breakage or shedding a largely intact organelle alone do not establish
shortening through disassembly. No complete disappearance, complete recycling,
universal disassembly direction, absence of basal severing, cell-cycle stage or
stimulus is required. Remnants can remain after resorption.

The current autotomy (`traitmech:000731`) and bacterial polar ejection
(`traitmech:000732`) records explicitly distinguish this endpoint. Bacterial
periplasmic resorption involves a different apparatus. Palmelloid formation
(`traitmech:000654`) does not require flagellar loss. No organism-level
disjointness, exact synonyms, xrefs, SSSOM mappings, canonical taxa, proteins or
causal graphs are asserted. A sequence feature alone cannot establish this
physiological phenotype.

## Evidence And Limits

1. [L'Hernault and Rosenbaum 1985](https://doi.org/10.1083/jcb.100.2.457),
   PMID:3968171, PMC2113451.1, is the definition authority. The eight-word
   excerpt is in printed page 458, Results, "Monitoring of Flagellar Length
   during In Vivo Labeling", sole paragraph; Figure 2 is on page 459.
   Its typeset passage and OCR text were checked. Native `NOT_IN_ABSTRACT`
   is retained; the XML body is one OCR block, not section-structured JATS.
   Regenerated flagella of source-designated wild-type 21gr shorten after
   pyrophosphate/cycloheximide treatment, rather than failing to assemble.
   Reported stubs prevent a claim of complete disappearance. All six main
   pages, three figures and Table I were inspected, not raw data. Two
   determinations or two gels are not established biological replicates.
2. [Parker and Quarmby 2003](https://doi.org/10.1186/1471-2121-4-11),
   PMID:12930563, PMC194436, provides a distinct supporting publication.
   The nine-word excerpt is Figure 7's first caption sentence, page 9 of 12,
   JATS `F7` under `sec9/sec5`. The actual figure and caption were checked;
   native `NOT_IN_ABSTRACT` is retained. Acid-shocked fa1, fa2 and adf1
   mutants coil and incompletely resorb flagella; wild type sheds and regrows
   in this comparison. The plotted endpoint is cells with flagella longer
   than 7 micrometers, not resorption rates or released-organelle counts.
   Separate fla10 temperature assays and low-calcium conditions must retain
   their own qualifiers. Low calcium is not zero calcium. All twelve main
   pages and eight figures were inspected.
3. [Parker et al. 2010](https://doi.org/10.1002/cm.20454), PMID:20506243,
   PMC2897710.1, supports the remnant limitation in a discussion, **not a
   third definition citation**. Its 12-word excerpt is in the scientific
   abstract, JATS `P2`, third sentence; direct text and native `VERIFIED`
   agree. Main text and three captions were read, not actual figures, PDF,
   supplementary video/legend or raw data. Live pf6 CC1029 and wild-type
   137c mt- CC124 electron microscopy are different preparations. Remnants
   may remain in the wall or be expelled; this does not impose a universal
   severing mechanism or cell-cycle restriction.

Only the local record and the 1985 DOI annotate the definition. Two supporting
publications are not a claim of independent-laboratory replication. The 2010
context shares authors with 2003. Strain provenance, protein-resolved mechanisms
and microbial-eukaryote scope remain explicit review questions.

The [source receipt](../../research/traits/physiology/eukaryotic_flagellar_resorption-source-verification.json)
preserves precise locators, asset hashes, actual resolver outcomes and access
limits. MED/Crossref and available publisher/PubMed notice checks are bounded,
not comprehensive correction/retraction clearance. Failed publisher/PMC/PubMed
requests remain failures; public primary assets have separate successful
provenance. No raw-data reanalysis, paid research or human sign-off is implied.

## Identity And Reservation

Biological acceptance preceded allocation. The observed allocation decision is
`2026-10-15T16:01:11Z`, on main
`565b6ef5602922935029943db3229c91968da10d`. Reserve `traitmech:000733`,
`metpo_traitmech_v609` and the whole block **1068600-1068699**. Only
`METPO:1068600` is populated; subset `metpo_traitmech_2026_10`.

The ignored-and-hidden search covered 207 known current locations and 303
retained heads, with 87,457 TraitMech and 9,308 CommunityMech unique regular
Git blobs. Ten old current copies were unavailable; tracked history cannot
reconstruct their lost ignored files. All 75 biological context hashes match
previously read dispositions, not a fresh full-owner reading of every copy.
All 81 local allocation contexts were assessed: nine are taxonomy fields in an
ignored Biopython BLAST fixture, and the rest document the general
1000000-1999999 editor envelope, not narrower reservations.

The remote snapshot covered 12 open/draft PRs: TraitMech #1938, #1937, #1936,
#973 and draft #924; CommunityMech draft #935; METPO #644, #643, #641, #640,
#638 and #629. All 784 nonremoved changed blobs and 587 selected upstream
files were screened. Exact numeric matches are embedding decimals or
`gmelin:1068689`, not METPO reservations. Other biological matches concern
bacterial appendages or pilus retraction.

Complete current/retained proposal text, remote content, and all 12 PR
descriptions were checked for wrapped ranges, with gzip decoding where needed:
197,791 owner contexts and 2,623 unique contents. The 29 overlapping contents
describe the general editor envelope; two additional matched contents contain
only embedding decimals and the GMELIN identifier. No binary limit was
reported. These are content counts, not trait counts. The final 16:00:17 UTC
guard confirmed stable main, relevant worktrees, source hashes, PR
heads/bases/descriptions/draft states and selected upstream heads.

Pinned/current METPO releases and templates distinguish possession and
arrangement from resorption. Deprecated METPO:0000089 and METPO:000090 carry
OMO:0001000; METPO:1000381 carries IAO:0000226. Their active replacement
METPO:1000704 denotes locomotory possession, not resorption. Deprecated ciliated
METPO:0000093 and METPO:000094 carry OMO:0001000, while METPO:1000385 carries
IAO:0000226; no replacement/consider annotation was observed for these or
deprecated flagellum METPO:1000123, whose reason is OMO:0001000. These are not
exact xrefs and are not revived. Upstream issue #521 leaves reason-code
interpretation unresolved. Its bacterial/archaeal focus requires explicit
maintainer review of this microbial-eukaryote proposal. The ontology pin stays
unchanged; the editor import stub is not the complete release.

Checks are bounded, not atomic allocation or literature exhaustion. Lost ignored
history, symlink targets, arbitrary archives and unchanged PR files were not
reconstructed. Refresh remote reservations before publication.

## Files And Verification

| Artifact | Content |
|---|---|
| `metpo_proposal_classes_robot.tsv` | One class, canonical 11-column headers |
| `proposal.md` | Scope, evidence, reservation and upstream path |
| Properties and SSSOM | Omitted: no predicates or equivalent mappings |

Headers were checked against the KG-Microbe template at
`1acb8b61fcae24fafc0640b1bf6e5be669f315f9` and the v608 dependency is
hash-guarded. Run the native proposal verifier and ROBOT/ELK wrapper, then
inspect actual `https://w3id.org/metpo/` child-parent-quality IRIs and definition
annotations. This instruction does not claim unrun gates passed.

## Upstream Path

Submit the reviewed class upstream separately. This placeholder is not released.
After acceptance and release, separately review scope, update the ontology pin,
re-seed and migrate the local identifier, retaining its prior spelling for
traceability. No upstream submission or human scientific approval is implied.

## Change Log

- 2026-10-15, v609: propose one microbial-eukaryote axonemal-resorption phenotype.
