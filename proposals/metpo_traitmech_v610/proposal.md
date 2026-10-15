# Eukaryotic Flagellar Axoneme Internalization

## Context And Scope

Propose **eukaryotic flagellar axoneme internalization**, `METPO:1068700`, for
`traitmech:000734` (`PHYSIOLOGY`, `CLASS`, `PROPOSED`). This is a reusable
physiological phenotype, not an axoneme structure or a source-specific locus.

Definition: A physiological phenotype in which a microbial eukaryote internalizes
the intact axoneme of its own cilium or flagellum into its cell body.

| Scope | Classes | Predicates | Enum Lifts |
|---|---:|---:|---:|
| A: one local trait | 1 | 0 | 0 |
| B: causal predicates | 0 | 0 | 0 |
| C: schema enums | 0 | 0 | 0 |

## Hierarchy Decisions

Phenotype `METPO:1000059`, below quality `METPO:1000188`, is a
definition-based parent inference. Locomotion is not a requirement. Static
internal localization, uptake of another cell's material, external coiling,
failed assembly, motor arrest, breakage or shedding alone do not establish
internalization of the cell's own intact axoneme.

Venard et al. 2020 classify internalization within a broad cilium-disassembly
program but separate it from subsequent axoneme degradation. The existing
operational resorption class (`traitmech:000733`) requires shortening through
axonemal disassembly, not intact withdrawal alone. Later degradation may follow
internalization: no disjoint taxa or permanently intact internal axoneme is
asserted. Autotomy (`traitmech:000731`) and bacterial polar flagellar ejection
(`traitmech:000732`) have different endpoints. Bacterial periplasmic flagella
and type IV pili are different apparatuses.

No universal reeling, lash-around, membrane-loss, cortical-tethering, actin,
dynein, proteolysis, rate, cell-cycle or recycling requirement is imposed.
Canonical taxa, exact synonyms, equivalent mappings and protein-resolved graphs
remain omitted pending their own provenance and authority checks. A sequence
feature or detector profile alone cannot establish the phenotype.

## Evidence And Limits

1. [Venard et al. 2020](https://doi.org/10.1002/cm.21637), PMID:33103844,
   PMC7944584, is the definition authority. Its five-word excerpt is in
   Results 2.2, the TEM interpretation following Figure 2, and was checked
   directly in PMC HTML. Main text and all five actual main figures were read.
   Fixed cross-sections retain axonemal architecture without surrounding
   ciliary membrane; fixed TEM is not continuous same-cell tracking. The
   Figure 1 counts of 23 and 32 are selected retraction events, not culture
   replicates. Complete-only latrunculin movie selection does not establish
   all-cell retraction probabilities. Preserve the plating/post-retraction
   time-zero and Table 1/Table 2 unit discrepancies. Actual supplemental
   PDFs/videos and the main PDF remain unread. The official supplement endpoint
   returned an HTTP-200 XML error, not a ZIP archive.
2. [Fritz-Laylin et al. 2017](https://doi.org/10.1083/jcb.201701074),
   PMID:28473602, PMC5461030.1, is a distinct supporting publication. Its
   14-word excerpt is in Discussion JATS s11, printed page 1681/PDF page 9,
   checked against direct JATS and typeset text. Results s10, Discussion s11,
   Methods s20 and selected PDF pages were read. The observation concerns
   source-designated JEL423 synchronized zoospores under confinement. Video 5
   was inspected through 16 sampled frames and one enlarged frame, not
   continuously. File metadata, burned-in labels and caption timing are not
   silently reconciled; no rate or retraction replication count is inferred.
   WASP/SCAR pseudopod experiments do not establish an internalization mechanism.
3. [Long et al. 2025](https://doi.org/10.1091/mbc.E24-12-0577),
   PMID:40833813, PMC12659703.2, supports a later-degradation/centriole-remodeling
   discussion, **not a third definition citation**. The nine-word excerpt is in
   Results S7 beside Figure 4C. Fixed U-ExM stages are not trajectories.
   Actual Figure 4, all supplement text and visual supplement pages 4, 7 and 8
   were inspected. Preserve the S2/S3 pointer and 4.5 versus 5.5 +/- 0.2
   expansion discrepancies. Figure 4F counts sporangia, not retraction events;
   the two-hour timeline is attributed to 2020. Remaining actual main figures
   and main PDF were not inspected. The preprint is another version of this
   study, not an additional publication.

All three excerpts retain native `NOT_IN_ABSTRACT`; direct full-text checks are
reported separately. Only the local record and the 2020 DOI annotate the
definition. Two supporting papers do not establish independent-laboratory
replication. Source-designated strains are qualified life-stage observations,
not authority-verified natural canonical taxa.

The [source receipt](../../research/traits/physiology/eukaryotic_flagellar_axoneme_internalization-source-verification.json)
preserves locators, hashes, actual resolver outcomes and access limits. MED and
Crossref notice checks are bounded, not comprehensive clearance. The linked
2017 Comment/Editorial, DOI:10.1080/15384101.2017.1360655, PMID:28820330,
PMC5628642, has no returned abstract and its content remains unread; it is not
counted evidence. No failed access attempt is reclassified as successful, and
no raw-data reanalysis, paid research or human sign-off is implied.

## Identity And Reservation

Allocated at 2026-10-15T20:08:47.827435+00:00 after the stable 2026-10-15T20:08:05.338409+00:00
refresh, based on main `a1db3a44599b96d564d7c3bd5ecc0ace19add76e`: local
`traitmech:000734`, cohort v610 and full block `1068700-1068799`.
Only `METPO:1068700` is populated, in subset `metpo_traitmech_2026_10`.

The completed local scan covered 210 known current locations, 306 retained
heads, 88,636 TraitMech and 9,308 CommunityMech unique regular Git blobs.
Ignored and hidden files were included. Eleven copies were unavailable.
All 76 biological contexts retain byte-verified prior assessments; all 74
local allocation contexts concern the general 1000000-1999999 editor envelope,
not a competing narrower reservation.

The remote snapshot covered 12 open/draft PRs, 784 nonremoved changed blobs
and 587 selected upstream blobs. Pending PR reservations were inspected at
their saved heads: TraitMech #1938, #1937, #1936, #973 and draft #924;
CommunityMech draft #935; METPO #644, #643, #641, #640, #638 and #629.
The five biological matching files are byte-identical to previously assessed
pilus/motility contexts. Four exact numeric matches are decimal embedding
cells in draft #924; `gmelin:1068715` maps to CHEBI:32552, not METPO.
Full-content checks, including wrapped ranges and gzip decoding, covered
203,913 owner contexts and 2,625 unique contents. Of 32 matching contents,
30 describe the general editor envelope and two contain those numeric false
positives. No competing reservation remained in this inspected scope.

The [allocation receipt](../../research/traits/physiology/eukaryotic_flagellar_axoneme_internalization-allocation.json)
retains input hashes, pinned PR heads, dispositions and scope limits.
The final guard found unchanged source hashes, worktree catalogs, upstream
heads and PR heads/bases/descriptions/draft states. This is not an atomic lock.

Pinned/current METPO releases and templates distinguish possession and
arrangement from internalization. Deprecated METPO:0000089 and METPO:000090
carry OMO:0001000; METPO:1000381 carries IAO:0000226. Their active replacement
METPO:1000704 denotes locomotory possession, not internalization. Deprecated
ciliated METPO:0000093 and METPO:000094 carry OMO:0001000, while METPO:1000385
carries IAO:0000226. No replacement/consider annotation was observed for these
or deprecated flagellum METPO:1000123 with OMO:0001000. None is reactivated or
asserted as an exact xref. [METPO issue 521](https://github.com/berkeleybop/metpo/issues/521)
leaves reason-code interpretation unresolved. Upstream's bacterial/archaeal
focus requires maintainer review of microbial-eukaryote inclusion. The ontology
pin is unchanged; the metadata-only editor is not the complete release.

Checks are bounded, not atomic allocation or literature exhaustion. Lost ignored
history, symlink targets, arbitrary archives and unchanged PR files are not
reconstructed. Refresh remote reservations before publication.

## Files And Verification

| Artifact | Content |
|---|---|
| `metpo_proposal_classes_robot.tsv` | One class, canonical 11-column headers |
| `proposal.md` | Scope, evidence, reservation and upstream path |
| Properties and SSSOM | Omitted: no predicates or equivalent mappings |

Headers were checked against the KG-Microbe template at
`1acb8b61fcae24fafc0640b1bf6e5be669f315f9`; the v609 dependency is
hash-guarded. Run the native proposal verifier and ROBOT/ELK wrapper, then
inspect actual `https://w3id.org/metpo/` child-parent-quality IRIs and definition
annotations. This instruction does not claim unrun gates passed.

## Upstream Path

Submit the reviewed class upstream separately. The placeholder is not released.
After acceptance and release, separately review scope, update the ontology pin,
re-seed and migrate the local identifier while retaining its prior spelling for
traceability. No upstream submission or human scientific approval is implied.

## Change Log

- 2026-10-15, v610: propose one microbial-eukaryote intact-axoneme internalization phenotype.
