# Cell-Body Contraction

## Context And Scope

Propose `METPO:1068100`, **cell-body contraction**, for local
`traitmech:000728` (`PHYSIOLOGY`, `CLASS`, `PROPOSED`).

Definition: A physiological phenotype in which a microbial cell actively
shortens its body by contraction of intracellular structures.

| Scope | Classes | Properties | Parent |
|---|---:|---:|---|
| A: one synthetic trait lift | 1 | 0 | METPO:1000059 phenotype |
| B: predicates | 0 | 0 | Not needed |
| C: schema enums | 0 | 0 | Not needed |

This independently supported phenotype is not a gene, protein, organelle,
single assay result or sequence-feature row. No equivalent external mapping
was accepted, so no SSSOM file is emitted. Prior cohorts remain unchanged.

## Hierarchy Decisions

Phenotype `METPO:1000059` is active below quality `METPO:1000188`.
Motility `METPO:1000701` concerns locomotion through the environment; motile
`METPO:1000702` specifies independent movement using metabolic energy.
Body shortening need not establish either endpoint. Retain the broad
phenotype parent while a closer contractility hierarchy is assessed.

Body contraction is not displacement caused only by stalk coiling, axopodial
retraction, contractile-vacuole cycling, injection-system contraction,
cytokinetic constriction, passive osmotic shrinkage, death or static short-cell
size. Habituation changes a response's probability, not its identity.
The broader cellular-contractility parent TODO in rapid axopodial contraction
`traitmech:000682` is not resolved by this body-specific class. It is not
reparented here. No organism-level disjointness, universal speed, fractional
shortening, calcium concentration, ATP independence, protein or function is
required. Generic contractility is not asserted as an exact synonym.

## Evidence And Limits

1. [Zhang et al. 2023](https://doi.org/10.1126/sciadv.add6550),
   `PMID:36812318`, `PMCID:PMC9946354`: definition authority and observed
   contraction in study-identified Spirostomum minus. The 22-word Results
   excerpt directly matches JATS; native `NOT_IN_ABSTRACT`. Source superscript
   exponents mean `10^(-6)` to `10^(-2)` M; plain-text normalization loses that
   styling, so the adjacent record notes clarify it (#1933). Actual Figure 1A
   shows body shortening. The 38-to-16-second quantity is an interval between
   contractions, not contraction duration. Supplementary Figure 7 illustrates
   shortening during death, which is insufficient. The RNAi abnormal-cell
   table is **Supplementary Table 2**, not Table S1 as the Results pointer says.
   Rare twisted phenotypes are not every treated cell; Figure 9 is a proposed
   mechanistic schematic, not universal molecular proof.
2. [Floyd et al. 2023](https://doi.org/10.1073/pnas.2217737120),
   `PMID:37307463`, `PMCID:PMC10288572`: primary Spirostomum length trajectories
   in Figures 1A/2A-B, distinguished from fitted models. The 15-word Figure 4
   caption excerpt reports asymmetric contraction of the imaged cell-body
   endpoints; actual panels A-C show shortening and staggered endpoint movement,
   separately from dashed fitted curves. It directly matches JATS; native
   `NOT_IN_ABSTRACT`. The former Results A data-presentation excerpt and the
   intermediate no-snippet attempt are retained only as historical provenance
   (#1935). The latter failed the snippet gate and was never published.
   Supplementary S3
   measures central-backbone length, not area or volume. S6 explicitly leaves
   repeated contractions versus different organisms unresolved: five traces
   are not five established biological replicates. Vorticella panels measure
   stalk contraction and do not establish body shortening. No species identity,
   universal calcium-wave mechanism or viscosity law is inferred.
3. [Katoh and Naitoh 1994](https://doi.org/10.1242/jeb.189.1.163),
   `PMID:9317557`: the 19-word scientific Abstract item 3 clause directly
   matches the namespace-qualified MED response; native `VERIFIED`. Living
   Vorticella body shrinkage is graded, unlike the same sentence's
   all-or-nothing stalk coiling. Other abstract items concern Triton-extracted
   preparations, not that living-cell assay. Publisher HTML/PDF returned 403;
   full Methods, figures and strain provenance were not accessed.

Only Zhang and the local record annotate the proposal definition. The other
two publications provide supporting evidence, not extra definition annotations.
The [source-verification sidecar](../../research/traits/physiology/cell_body_contraction-source-verification.json)
retains exact sections, retrieval URLs, hashes, native record-CLI outcomes and
bounded read scope. Direct full-text matching does not upgrade abstract verdicts.
Retrieved metadata identifies the PNAS preprint relationship, not a correction.
Publisher access limits and bounded notice checks preclude comprehensive
correction/retraction clearance. Raw videos and all modeling calculations were
not reanalyzed.

No canonical taxa, protein accessions, causal graph, exact synonyms or xrefs are
asserted. Study-isolate/current-taxonomy correspondence and taxon-paired causal
proteins remain open tasks. Mechanistic evidence is not claimed absent; the
first-pass record does not turn sequence features or fitted models into a
universal mechanism. Three OPEN discussions retain hierarchy, identity and
mechanism/provenance questions. Human scientific sign-off has not occurred.

## Identity And Reservations

Allocation accepted at `2026-10-14T17:32:15Z`, clean main
`caba6de6cdeec9f0e10c026ff2e2356df3427c04`. Ignored and hidden files were
included in 195 known locations. Retained-history screening covered 143 heads,
23,435 TraitMech and 5,815 CommunityMech regular-file blobs. All 194 unique
matched path/text variants (8,001 occurrences) were assessed. Existing hits
concern distinct physiological endpoints, cell-size/division contexts,
metazoan contraction, passive water loss, taxon names or software contracts.
No exact synonym, ungrounded graph node or parent TODO requiring migration
was identified. The broader axopodial parent gap stays open.

RDF inspection covered the pinned/current METPO releases (12,617/12,649
triples), hash-verified editor conversion and inspected template owners.
The editor alone is not absence evidence. Historical obsolete Motility
`METPO:0000006`/`METPO:000006` points to active `METPO:1000701`; obsolete
Motile `METPO:0000087`/`METPO:000088` points to active `METPO:1000702`.
These are related locomotion identities, not exact contraction matches.
No retired identifier is revived and the ontology pin is unchanged.

Remote screening covered 11 open/draft PRs: TraitMech #1782, #1476, #973 and
draft #924; CommunityMech draft #935; METPO #644, #643, #641, #640, #638 and
#629. Heads, descriptions and states were refreshed before allocation.
Pending lexical hits repeat cell-length contexts. Compressed KG-Microbe
matches concern Haloplasma contractile taxonomy; FOODON context describes
muscle tissue, not a same-scope microbial phenotype.

Reserve `traitmech:000728`, `metpo_traitmech_v604`, and the full METPO block
**1068100-1068199**; only `METPO:1068100` is proposed. The numeric lookalikes
are a `Contig_Lengths` value in a cached genome supplement and `1.1068147`,
an embedding component for `METPO:1000463` in draft PR924. Neither reserves a
METPO identifier. All 1,160 interval hits denote the broad 1000000-1999999
editor envelope or its documentation. Full-content range inspection covered
50,347 owner contexts and 2,569 unique contents, including wrapped proposal
ranges. No conflicting narrower reservation was identified. CommunityMech's
1007100-1007220 block does not overlap. Subset: `metpo_traitmech_2026_10`.

These are bounded checks, not atomic allocation or literature exhaustion.
Lost ignored/untracked history, symlink targets, submodules, arbitrary archives
and unchanged PR files were not reconstructed. Refresh reservations before
publication.

## Files And Verification

| File | Content |
|---|---|
| metpo_proposal_classes_robot.tsv | One class, canonical 11-column two-row template |
| proposal.md | Scope, evidence, reservations and migration plan |
| Source-verification sidecar | Source and search provenance |

Required commands: `just verify-proposal metpo_traitmech_v604` and
`just robot-validate-proposal metpo_traitmech_v604`. Inspect emitted RDF for
`https://w3id.org/metpo/` IRIs, the actual phenotype/quality hierarchy and
definition annotations. Results belong in the saved review; this narrative
does not assert that unrun gates passed. Canonical header bytes were checked
against KG-Microbe at `b4b4cee330768083494f6f7e556314b25d75f2b6`.

## Upstream And Round Trip

After local sign-off, submit the ROBOT template to berkeleybop/metpo.
This placeholder is not a released METPO identifier. On upstream acceptance
and release, a separately reviewed migration must recheck exact identity,
update the pinned snapshot, re-seed, and replace the local identifier while
preserving the old identifier as a traceability synonym. No upstream PR is
implied by this local proposal.

## Change Log

- 2026-10-14: v604 introduces one active cell-body-shortening phenotype;
  prior records, cohorts and protected spore germination remain unchanged.
