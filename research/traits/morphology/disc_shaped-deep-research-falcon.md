---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:09:16.615910'
end_time: '2026-08-04T08:17:52.781649'
duration_seconds: 516.17
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: disc shaped
  trait_identifier: METPO:1000689
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: disc_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism is flat and circular.
  parent_traits: METPO:1000666
  synonyms: disc
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review supports flat-disc geometry as a determined morphological
    phenotype.) | DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Halophilic-archaea
    description supports flat disc-shaped cell morphology in the wild.)'
  causal_graph_summary: 'disc_shaped_anisotropic_wall_growth: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** disc shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000689
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism is flat and circular.
- **Parent traits:** METPO:1000666
- **Synonyms:** disc
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports flat-disc geometry as a determined morphological phenotype.) | DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Halophilic-archaea description supports flat disc-shaped cell morphology in the wild.)
- **Existing causal graph summary:** disc_shaped_anisotropic_wall_growth: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **disc shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/disc_shaped.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** disc shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000689
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism is flat and circular.
- **Parent traits:** METPO:1000666
- **Synonyms:** disc
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports flat-disc geometry as a determined morphological phenotype.) | DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Halophilic-archaea description supports flat disc-shaped cell morphology in the wild.)
- **Existing causal graph summary:** disc_shaped_anisotropic_wall_growth: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **disc shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/disc_shaped.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.


# Curation report: microbial disc-shaped morphology

## Executive assessment

The requested class is **“METPO:1000689”**, defined as “a cell shape in which an organism is flat and circular.” The strongest mechanism-level evidence found is for the pleomorphic haloarchaeon *Haloferax volcanii*, in which “plate,” “disk,” “discoid,” and “disc-shaped” refer to the same broad flat-cell state. Current evidence supports a regulatory switch between motile rods and non-elongated disks rather than a single constitutive wall-growth program. The most defensible core graph is:

**DdfA-dependent regulation → volactin-supported rod-to-disk morphogenesis → disc-shaped cell**, opposed by a **CetZ1/RdfA/Sph3 rod-development branch**, and conditioned by growth phase, medium composition, and surface attachment. DdfA and volactin are the strongest positive disk determinants; CetZ1, RdfA, and Sph3 are experimentally validated rod determinants whose loss yields disk-biased or disk-only cells. (schiller2024identificationofstructural pages 5-5, schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 7-9, schiller2024identificationofstructural pages 6-7)

## 1. Trait scope and boundaries

### Intended phenotype

For TraitMech, the class should represent **whole-cell three-dimensional geometry**: a cell flattened along one axis and approximately circular, discoid, or polygonal in face view. In *H. volcanii*, routine cultures contain pleomorphic “discoid (plate)” and rod morphologies; late-log and stationary cultures commonly revert to plates. (silva2021improvedgrowthand pages 1-2)

Operational microscopy criteria vary:

- Schiller et al. classified cells with **aspect ratio <2** as “disks and/or short rods,” explicitly showing that this threshold alone does not cleanly distinguish disks from short rods. Their genetic comparisons included 936–2,698 cells per strain at early log and 1,339–2,624 at late log. (schiller2024identificationofstructural pages 3-5)
- Patro et al. used image circularity: **0.8–1.0 for plate-like cells**, **≤0.6 for rods**, and **0.6–0.8 as intermediate morphology**. (patro2023“influenceofplasmids pages 2-3)

Accordingly, curation should require either an author-assigned disk/plate phenotype or combined evidence for high circularity/low aspect ratio **and flatness**. A two-dimensional circular outline alone is insufficient.

### Boundary cases to exclude or annotate separately

1. **Cocci or spherical cells:** circular in projection but not flattened.
2. **Short or rounded rods:** can satisfy aspect ratio <2; Schiller et al. explicitly combined these with disks in quantitative bins. (schiller2024identificationofstructural pages 3-5)
3. **Large, flat amorphous cells:** the *H. volcanii* ΔftsZ2 phenotype is described as “larger, flat, amorphic,” not necessarily a regular disk. (cooper2023archaealtubulinlikeproteins pages 1-2)
4. **Square, triangular, or irregular plates:** related haloarchaeal morphologies, but not circular disks unless the ontology deliberately treats polygonal discoids as within scope. Haloarchaea can display rods, plates/disks, triangles, squares, and exotic forms. (patro2023“influenceofplasmids pages 1-2)
5. **Filaments and biofilm rods:** attachment can shift flat circular planktonic cells toward rod and filamentous states. (cooper2023archaealtubulinlikeproteins pages 1-2)
6. **Transient assay states:** *H. volcanii* progresses from early-log rods through mixed populations to smaller plates in stationary phase; morphology is not a fixed species-level character. (patro2023“influenceofplasmids pages 1-2)

## 2. Current mechanistic understanding

### Regulatory and structural core

**DdfA (HVO_2176)** is the strongest positive regulatory determinant. Deleting it produces hypermotile cells that remain rods across growth phases, while complementation restores disk formation. DdfA contains a HalOD1 output domain associated with signal transduction, but its upstream signal, biochemical activity, and physical partners remain unresolved. Thus, `DdfA required_for disk formation` is curatable, whereas a specific DdfA signaling pathway is not yet established. (schiller2024identificationofstructural pages 5-5, schiller2024identificationofstructural pages 7-9)

**Volactin/VolA (HVO_2015)** is an actin homolog supporting timely disk morphogenesis. A complete deletion could not be recovered among 100 tested colonies in this polyploid archaeon; the partial deletion ΔvolA* retained gene copies. At mid log, ΔvolA* contained significantly more rods than wild type, and complementation corrected the defect. By late log, however, the mutant still formed disks, so VolA promotes the timing and efficiency of the transition rather than being proven absolutely required for every disk. (schiller2024identificationofstructural pages 6-7)

Live-cell imaging supplies the principal structural mechanism: VolA forms dynamic polymers that elongate, rapidly depolymerize, and form/disappear as patches. Filaments bridge the cytoplasm and attach to the membrane by their tips rather than lying along it; their assembly is independent of the FtsZ1 division site. Mid-log mixed populations show stronger VolA polymer signal than early-log rod populations. These observations support a cytoskeletal disk-morphogenesis module but do not yet establish how filament force or envelope remodeling produces flattening. (schiller2024identificationofstructural pages 7-9, schiller2024identificationofstructural pages 6-7)

### Opposing rod-development branch

**CetZ1**, an archaeal tubulin-family protein, is required for rod development. ΔcetZ1 is used as a disk-only mutant, and trace-element-controlled experiments show that both ordinary early-log rods and abnormal elongated/tubulated forms depend on CetZ1. Therefore, the native positive edge is `CetZ1 promotes rod formation`; `loss of CetZ1 causes disks` is useful mutant evidence but should not be mistaken for the normal disk-building mechanism. (silva2021improvedgrowthand pages 1-2, schiller2024identificationofstructural pages 3-5)

**RdfA (HVO_2174)** and **Sph3 (HVO_2175)** are also required for rods: individual deletions formed only disks across all examined growth phases, and plasmid complementation restored rod formation. Sph3 is SMC-like, but a structural mechanism has not been demonstrated. (schiller2024identificationofstructural pages 3-5)

Recent work further shows that **MinD2**, and more weakly MinD4, controls CetZ1 localization in rod cells. Deleting minD2 altered CetZ1 distribution and inhibited its polar localization, but minD2/minD4 mutants still formed early-log rods. Consequently, MinD proteins should not yet be curated as disk determinants. (brown2024mindproteinsregulate pages 1-2)

### Envelope-associated branch

ArtA and the phosphatidylethanolamine-biosynthesis proteins PssA/PssD participate in C-terminal processing and lipid attachment of surface proteins, including the S-layer glycoprotein, and are reported to be required for effective, stable plate formation. Their depletion or loss increases rod-biased phenotypes. This supports an envelope-processing branch, but the specific processed substrate responsible for disk geometry has not been isolated. (silva2021improvedgrowthand pages 1-2, schiller2024identificationofstructural pages 9-9)

Proteomics also found Agl11 and Agl12, components of an Agl15-dependent N-glycosylation pathway, more abundant in disk-forming conditions. This is association, not causal genetic evidence. The Agl pathway should remain a candidate rather than a curated causal route. (schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 5-6)

## 3. Candidate nodes grouped by type

### Trait and taxon

- **disc shaped** — **“METPO:1000689”**; retain verbatim.
- Parent trait — **METPO:1000666**, as supplied.
- *Haloferax volcanii* — use the verified NCBI Taxonomy CURIE from the project’s taxonomy resolver; do not infer it manually during curation.

### Genes and proteins

- **ddfA / DdfA — HVO_2176:** disk-determining regulatory factor; HalOD1-containing protein.
- **volA / volactin — HVO_2015:** actin homolog and dynamic cytoskeletal polymer.
- **cetZ1 / CetZ1:** archaeal tubulin-family rod determinant.
- **rdfA / RdfA — HVO_2174:** rod-determining factor.
- **sph3 / Sph3 — HVO_2175:** SMC-like rod determinant.
- **artA / archaeosortase A:** surface-protein C-terminal processing.
- **pssA, pssD:** phosphatidylethanolamine-biosynthesis proteins involved in lipid attachment of ArtA substrates.
- **agl11 — HVO_2057; agl12 — HVO_2059; agl14 — HVO_2058; agl9 — HVO_2048:** N-glycosylation candidates; presently proteomic associations rather than proven disk determinants. (schiller2024identificationofstructural pages 5-6)
- **ftsZ1/FtsZ1:** cytokinetic-ring marker used to show that VolA dynamics are division-site independent.
- **minD2, minD4:** CetZ1-positioning factors relevant to the rod branch, not currently disk determinants.

Locus tags are preferable to uncertain UniProt mappings. No UniProt, KEGG, EC, Rhea, or MetaCyc identifiers should be assigned without database verification.

### Cellular structures and processes

- Volactin filament/polymer.
- Cytoplasmic bridging by tip-anchored VolA filaments.
- Rod-to-disk morphological transition.
- CetZ1-dependent rod morphogenesis.
- S-layer glycoprotein processing and lipid anchoring.
- Agl15-dependent N-glycosylation pathway—candidate only.
- Cell division/cytokinetic ring—contextual, not demonstrated as the disk-forming process.

Possible generic GO groundings, subject to ontology-version verification, include **GO:0007010 cytoskeleton organization**, **GO:0005200 structural constituent of cytoskeleton**, **GO:0007049 cell cycle**, and **GO:0051301 cell division**. These generic terms should not replace organism-specific mechanistic nodes.

### Environmental and experimental factors

- Early-, mid-, late-log, and stationary growth phases.
- Trace-element-replete versus trace-element-depleted medium.
- Planktonic shaking culture.
- Surface attachment/early biofilm growth.
- Soft-agar motility conditions.
- Recombinant plasmid presence.
- Auxotrophic background and selection markers, especially ΔhdrB/hdrB.
- Culture density and microscopy segmentation thresholds.

## 4. Candidate causal edges

The table below separates direct determinants from opposing rod branches, conditional environmental effects, and associations that should remain provisional.

| subject | predicate | object | evidence class (direct/conditional/inferred) | taxon/condition | DOI | short exact supporting snippet | curation recommendation |
|---|---|---|---|---|---|---|---|
| DdfA (HVO_2176) | required_for | disk-shaped cell formation | direct | *Haloferax volcanii* liquid culture; early- and late-log comparisons | 10.1038/s41467-024-45196-0 | "The Δhvo_2176 deletion mutant is hypermotile and forms only rods regardless of growth phase"; "Complementation with ddfAext ... restored disk formation" (schiller2024identificationofstructural pages 5-5) | **Curate yes.** Strong gene→trait edge for disks. Note phenotype is in a pleomorphic archaeon with assay based on microscopy; Schiller et al. use aspect ratio with "Aspect ratios <2 are considered disks and/or short rods," so annotate carefully against short-rod boundary cases (schiller2024identificationofstructural pages 3-5). |
| Volactin / VolA (HVO_2015) | promotes | timely rod-to-disk transition | direct | *H. volcanii* mid-log liquid culture | 10.1038/s41467-024-45196-0 | "Mid-log ΔvolA* cultures contained significantly more rods relative to wild-type cultures ... indicating that volactin is important for rod-to-disk shape transitions." (schiller2024identificationofstructural pages 6-7) | **Curate yes.** Best as process edge to disk transition, not absolute requirement for final disk state, because "as ΔvolA* cultures transitioned to late log, they formed disks like wild type" (schiller2024identificationofstructural pages 6-7). |
| Volactin / VolA (HVO_2015) filaments | part_of / supports | disk-shape morphogenesis cytoskeletal system | direct | *H. volcanii* live-cell imaging | 10.1038/s41467-024-45196-0 | "volactin-tip anchoring"; "filaments never were adjacent to the membrane but rather bound the membrane by their tips, bridging the cytoplasm"; "reveal volactin as part of a cytoskeletal system involved in disk-shape formation" (schiller2024identificationofstructural pages 7-9) | **Curate yes.** Strong structural node/edge. Use separate node for volactin polymer/filament if TraitMech supports macromolecular structures. |
| CetZ1 | required_for | rod development | direct | *H. volcanii* planktonic shaking cultures | 10.1099/mic.0.001012 | "The tubulin-like cytoskeletal protein CetZ1 is required for rod formation" (silva2021improvedgrowthand pages 1-2) | **Curate yes, but as an opposing branch.** Loss of CetZ1 biases cells toward disk-only states in shape screens; represent as CetZ1 → rod morphology, then rod morphology negatively related to disk state within this pleomorphic system (schiller2024identificationofstructural pages 3-5). |
| loss of CetZ1 | biases_toward | disk-only morphology | direct | *H. volcanii* deletion mutant in proteomic/genetic comparisons | 10.1038/s41467-024-45196-0 | "disk-only (ΔcetZ1)" (schiller2024identificationofstructural pages 3-5) | **Curate cautiously.** Useful mutant-state edge, but cleaner mechanistic curation is the positive edge CetZ1 → rod formation. Avoid overgeneralizing loss-of-function states as native disk mechanism. |
| RdfA (HVO_2174) | required_for | rod formation | direct | *H. volcanii* all growth phases | 10.1038/s41467-024-45196-0 | "both Δhvo_2174 and Δsph3 formed only disks across all growth phases"; "cells regained the ability to form rods" after complementation; authors "propose to annotate HVO_2174 as rod-determining factor A (RdfA)" (schiller2024identificationofstructural pages 3-5) | **Curate yes, indirect-to-disk.** Strong rod determinant; deletion yields disks. Best modeled as competing branch rather than direct positive determinant of disks. |
| Sph3 (HVO_2175) | required_for | rod formation | direct | *H. volcanii* all growth phases | 10.1038/s41467-024-45196-0 | "both Δhvo_2174 and Δsph3 formed only disks across all growth phases"; complementation restored rods (schiller2024identificationofstructural pages 3-5) | **Curate yes, indirect-to-disk.** Same logic as RdfA. Taxon-specific and mechanism unresolved beyond SMC-like protein annotation. |
| late-log / stationary growth phase | promotes | plate/disk morphology | conditional | *H. volcanii* liquid batch culture | 10.1099/mic.0.001012 | "cells then reverted to plates for the late log and stationary phases" (silva2021improvedgrowthand pages 1-2) | **Curate yes as environmental/physiological context.** Good conditional edge. Note phenotype depends on standardized medium and growth conditions. |
| trace-element-replete medium | permits | early rods followed by late-log reversion to plates | conditional | *H. volcanii* supplemented with eight trace elements | 10.1099/mic.0.001012 | "With these supplemented media, transient development of plate cells into uniformly shaped rods was clearly observed during the early log phase of growth; cells then reverted to plates for the late log and stationary phases." (silva2021improvedgrowthand pages 1-2) | **Curate yes as conditional edge.** Supports medium composition as a context node affecting the rod↔disk program, not a direct molecular determinant of disks. |
| surface attachment / early biofilm development | shifts_from | disk-shaped cells toward rods/filaments | conditional | *H. volcanii* attached to substratum | 10.3390/genes14101861 | "cells exhibited morphological changes going from circular and flat (disk-shaped) while shaking to two co-existing forms when they became sessile: a rod and a filamentous shape" (cooper2023archaealtubulinlikeproteins pages 1-2) | **Curate yes as negative contextual influence on disk state.** Strong condition effect, but specific to biofilm initiation/attachment assay. |
| ArtA, PssA, PssD activity | supports | stable plate/disk formation | inferred | *H. volcanii* surface-protein processing mutants | 10.1099/mic.0.001012 | "ArtA and phosphatidylethanolamine biosynthesis enzymes PssA and PssD ... are required for effective and stable plate-shaped cell formation" (silva2021improvedgrowthand pages 1-2) | **Curate as uncertain/indirect only.** Strongly relevant envelope branch, but current excerpts do not fully resolve whether effect is direct on disk morphogenesis or mediated through S-layer/surface protein processing. Also later work notes depletion causes increased rods at mid-log (schiller2024identificationofstructural pages 9-9). |
| Agl11 / Agl12 (Agl15-dependent N-glycosylation pathway) | associated_with | disk-forming conditions | inferred | *H. volcanii* comparative proteomics | 10.1038/s41467-024-45196-0 | "Agl11 and Agl12 showed higher abundance in disk-forming conditions and mutants" (schiller2024identificationofstructural pages 3-5) | **Do not yet curate as causal.** Association only; no direct knockout-to-disk evidence in the retrieved text. Good candidate nodes for future testing. |
| plasmid presence; auxotrophic markers (especially ΔhdrB / hdrB) | confounds_measurement_of | disk-vs-rod morphology | conditional | *H. volcanii* strain engineering backgrounds | 10.3389/fmicb.2023.1270665 | "plasmid presence ... favoring the development of rods in early stages of growth"; "ΔhdrB strains and hdrB selection markers have the most influence on H. volcanii cell shape" (patro2023“influenceofplasmids pages 1-2) | **Not a trait edge; include as curation warning.** Record as assay confounder metadata. Patro et al. also define circularity classes: plate 0.8-1.0, rods ≤0.6, intermediate 0.6-0.8 (patro2023“influenceofplasmids pages 2-3), while Schiller et al. use aspect ratio <2 (schiller2024identificationofstructural pages 3-5). |
| biofilm tubulin-gene background (ΔcetZ1, ΔcetZ3, ΔftsZ2, etc.) | alters | roundness/flatness/filamentation under attachment | direct | *H. volcanii* early biofilm development | 10.3390/genes14101861 | "∆cetZ1 and ∆cetZ3 were significantly rounder than the parental, and ∆ftsZ2 generated larger, flat, amorphic cells" (cooper2023archaealtubulinlikeproteins pages 1-2) | **Curate selectively.** Useful for nearby morphology traits and contextual support that tubulin-family proteins modulate shape under sessile conditions, but not specific enough alone for disc-shaped TraitMech edges. |


*Table: This table compiles compact, curation-ready candidate causal edges for the disc-shaped microbial trait in Haloferax volcanii, separating strong direct determinants from conditional and uncertain associations. It is designed to help prioritize which edges are suitable for TraitMech curation and which should remain warnings or future candidates.*

### Recommended minimal graph

For an initial conservative revision of `disc_shaped.yaml`, the most defensible triples are:

1. `DdfA — required_for → disc-shaped cell formation`.
2. `DdfA — promotes → rod-to-disk transition`.
3. `volactin — promotes → timely rod-to-disk transition`.
4. `volactin — forms → dynamic cytoplasmic filaments`.
5. `volactin filament — tip_anchors_to → cell membrane`.
6. `volactin cytoskeletal system — contributes_to → disc-shaped morphogenesis`.
7. `CetZ1 — promotes → rod formation`.
8. `RdfA — required_for → rod formation`.
9. `Sph3 — required_for → rod formation`.
10. `late-log/stationary growth — promotes → plate/disk state`.
11. `surface attachment — promotes → rod/filament transition` and therefore conditionally opposes the planktonic disk state.
12. `trace-element-replete medium — enables → reproducible growth-phase-dependent rod-to-plate cycle`.

Edges 7–9 belong in an antagonistic or alternative-morphology branch. If TraitMech predicates cannot represent competing states cleanly, retain their mutant consequences as evidence notes rather than encoding `rod inhibits disk` as a universal biological rule.

## 5. Recent developments, applications, and statistics

The major 2024 advance was the combination of iterative proteomics, reverse genetics, and live-cell imaging to distinguish shape-specific protein changes from growth-phase changes. Initial proteomics quantified **1,944 proteins**, of which **314** differed in at least one comparison; subsequent filtering identified a smaller set of high-priority shape-associated proteins. A second analysis reported **2,328 identified proteins**, with **938 differential abundances across conditions**, illustrating that growth phase creates a broad proteomic signal and must be experimentally separated from shape itself. (schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 5-5)

The VolA mid-log comparison analyzed **2,804 wild-type and 1,668 ΔvolA*** cells and found a significant aspect-ratio difference (**p<0.001**). The inability to isolate a complete deletion among **100 colonies** suggests essentiality, although polyploidy and retained copies prevent a definitive essential-gene conclusion. (schiller2024identificationofstructural pages 7-9, schiller2024identificationofstructural pages 6-7)

In 2023, biofilm experiments expanded the system beyond planktonic cultures. Deleting any of the eight tubulin-family genes altered morphology at most attachment time points; ΔcetZ1 and ΔcetZ3 produced rounder cells, whereas ΔftsZ1 and several CetZ deletions increased elongation or filamentation. These findings demonstrate context-dependent cytoskeletal control but should not all be converted into disk-specific edges. (cooper2023archaealtubulinlikeproteins pages 1-2)

In November 2024, MinD2 was identified as a spatial regulator of CetZ1, connecting a ParA/MinD ATPase system to an archaeal tubulin-family protein for the first time. Because MinD mutants retained early-log rods, this refines the rod/motility branch rather than establishing a disk mechanism. (brown2024mindproteinsregulate pages 1-2)

### Real-world and research applications

There is not yet a direct industrial implementation of engineered disk morphology. Current practical uses are research-oriented:

- **Reproducible archaeal cell biology:** trace-element supplementation suppresses uncontrolled pleomorphic rods and creates a reproducible early-rod/late-plate cycle. (silva2021improvedgrowthand pages 1-2)
- **Live-cell cytoskeleton imaging:** large, flattened *H. volcanii* cells facilitate visualization of dynamic polymers and division structures.
- **Biofilm and motility studies:** disk-to-rod/filament transitions link morphology with attachment and swimming states. (cooper2023archaealtubulinlikeproteins pages 1-2)
- **Evolutionary cell biology:** VolA, CetZ1, FtsZ, and S-layer-dependent morphology provide a comparative system spanning actin-, tubulin-, and envelope-based shape control.
- **Genetic-screen design:** the 2023 plasmid/marker study provides concrete controls needed to avoid false morphology assignments. (patro2023“influenceofplasmids pages 1-2)

## 6. Expert interpretation

The evidence favors a **regulated morphological-state transition** rather than the existing summary’s simple “anisotropic wall growth” model. *H. volcanii* lacks bacterial peptidoglycan, and the retrieved studies do not demonstrate anisotropic wall synthesis as the proximal cause of its disks. The most credible model is that DdfA-dependent signaling shifts the cell away from the CetZ1/RdfA/Sph3 rod program, while dynamic VolA polymers participate structurally in remodeling or stabilizing the flat disk. ArtA/PssA/PssD-mediated surface-layer anchoring is likely permissive for stable plate geometry. The physical coupling among VolA, membrane curvature, S-layer insertion, and DdfA remains unknown. (silva2021improvedgrowthand pages 1-2, schiller2024identificationofstructural pages 7-9, schiller2024identificationofstructural pages 6-7)

Accordingly, the existing `disc_shaped_anisotropic_wall_growth` graph should not be treated as generally established for this trait. A taxon-specific graph named along the lines of `disc_shaped_haloferax_shape_transition` would better match the evidence.

## 7. Warnings: claims not yet ready for TraitMech

1. **Do not curate Agl11/Agl12 abundance as causation.** Direct deletion/complementation evidence for disk morphology was not retrieved. (schiller2024identificationofstructural pages 3-5)
2. **Do not claim that VolA is absolutely essential for disks.** ΔvolA* is a partial deletion and eventually forms disks in late log. (schiller2024identificationofstructural pages 6-7)
3. **Do not equate aspect ratio <2 with a disk.** The source explicitly includes short rods in this category. (schiller2024identificationofstructural pages 3-5)
4. **Do not generalize from *H. volcanii* to all disc-shaped microorganisms.** The mechanism is presently haloarchaeon-specific.
5. **Do not encode CetZ1 loss as the normal positive disk mechanism.** CetZ1 is a rod determinant; disk-only ΔcetZ1 is a loss-of-function consequence. (silva2021improvedgrowthand pages 1-2)
6. **Do not make MinD2/MinD4 disk nodes.** Their demonstrated role concerns CetZ1 localization and motility; early-log rod formation persists. (brown2024mindproteinsregulate pages 1-2)
7. **Do not infer a peptidoglycan or bacterial MreB mechanism.** The VolA filaments differ spatially from bacterial MreB and *H. volcanii* uses an archaeal S-layer envelope. (schiller2024identificationofstructural pages 7-9)
8. **Treat ArtA/PssA/PssD as an unresolved envelope branch.** Stable plates depend on these functions, but the causal substrate and physical mechanism remain unknown. (silva2021improvedgrowthand pages 1-2)
9. **Control genetic background.** Plasmids, ΔhdrB, hdrB selection, and other auxotrophies alter length, area, aspect ratio, and circularity; plasmids can favor early rods independently of the intended mutation. (patro2023“influenceofplasmids pages 1-2)
10. **Do not curate FtsZ2-deficient amorphous flat cells as ordinary disks.** Cell-division defects can produce large, irregular flat cells that are a distinct phenotype. (patro2023“influenceofplasmids pages 1-2, cooper2023archaealtubulinlikeproteins pages 1-2)

## DOI-first bibliography

1. Schiller H, Hong Y, Kouassi J, et al. **Identification of structural and regulatory cell-shape determinants in *Haloferax volcanii*.** *Nature Communications* 15, 1414. Published February 2024. DOI: [10.1038/s41467-024-45196-0](https://doi.org/10.1038/s41467-024-45196-0). Central source for DdfA, RdfA, Sph3, VolA, proteomics, complementation, and live-cell imaging. (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 7-9, schiller2024identificationofstructural pages 6-7)
2. Brown HJ, Duggin IG. **MinD proteins regulate CetZ1 localization in *Haloferax volcanii*.** *Frontiers in Microbiology* 15. Published 22 November 2024. DOI: [10.3389/fmicb.2024.1474697](https://doi.org/10.3389/fmicb.2024.1474697). (brown2024mindproteinsregulate pages 1-2)
3. Patro M, Duggin IG, Albers S-V, Ithurbide S. **Influence of plasmids, selection markers and auxotrophic mutations on *Haloferax volcanii* cell shape plasticity.** *Frontiers in Microbiology* 14:1270665. Published 29 September 2023. DOI: [10.3389/fmicb.2023.1270665](https://doi.org/10.3389/fmicb.2023.1270665). (patro2023“influenceofplasmids pages 1-2)
4. Cooper A, Makkay AM, Papke RT. **Archaeal Tubulin-like Proteins Modify Cell Shape in *Haloferax volcanii* during Early Biofilm Development.** *Genes* 14:1861. Published 25 September 2023. DOI: [10.3390/genes14101861](https://doi.org/10.3390/genes14101861). (cooper2023archaealtubulinlikeproteins pages 1-2)
5. de Silva RT, Abdul-Halim MF, Pittrich DA, et al. **Improved growth and morphological plasticity of *Haloferax volcanii*.** *Microbiology* 167:001012. Published 18 January 2021. DOI: [10.1099/mic.0.001012](https://doi.org/10.1099/mic.0.001012). Foundational controlled-medium evidence for growth-phase transitions, CetZ1, and stable plate formation. (silva2021improvedgrowthand pages 1-2)

**Curation priority:** implement DdfA and VolA as the positive disk branch; retain CetZ1, RdfA, and Sph3 as the experimentally supported competing rod branch; include growth phase, trace elements, and attachment as conditional nodes; and defer Agl proteins and a detailed S-layer mechanical pathway until direct perturbation evidence links them specifically to “METPO:1000689”.

References

1. (schiller2024identificationofstructural pages 5-5): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

2. (schiller2024identificationofstructural pages 3-5): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

3. (schiller2024identificationofstructural pages 7-9): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

4. (schiller2024identificationofstructural pages 6-7): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

5. (silva2021improvedgrowthand pages 1-2): Roshali T. de Silva, Mohd F. Abdul-Halim, Dorothea A. Pittrich, Hannah J. Brown, Mechthild Pohlschroder, and Iain G. Duggin. Improved growth and morphological plasticity of haloferax volcanii. Feb 2021. URL: https://doi.org/10.1099/mic.0.001012, doi:10.1099/mic.0.001012. This article has 100 citations and is from a peer-reviewed journal.

6. (patro2023“influenceofplasmids pages 2-3): Megha Patro, Iain G. Duggin, Sonja-Verena Albers, and Solenne Ithurbide. “influence of plasmids, selection markers and auxotrophic mutations on haloferax volcanii cell shape plasticity”. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1270665, doi:10.3389/fmicb.2023.1270665. This article has 8 citations and is from a peer-reviewed journal.

7. (cooper2023archaealtubulinlikeproteins pages 1-2): Alexei Cooper, Andrea M. Makkay, and R. Thane Papke. Archaeal tubulin-like proteins modify cell shape in haloferax volcanii during early biofilm development. Genes, 14:1861, Sep 2023. URL: https://doi.org/10.3390/genes14101861, doi:10.3390/genes14101861. This article has 1 citations.

8. (patro2023“influenceofplasmids pages 1-2): Megha Patro, Iain G. Duggin, Sonja-Verena Albers, and Solenne Ithurbide. “influence of plasmids, selection markers and auxotrophic mutations on haloferax volcanii cell shape plasticity”. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1270665, doi:10.3389/fmicb.2023.1270665. This article has 8 citations and is from a peer-reviewed journal.

9. (brown2024mindproteinsregulate pages 1-2): Hannah J. Brown and Iain G. Duggin. Mind proteins regulate cetz1 localization in haloferax volcanii. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1474697, doi:10.3389/fmicb.2024.1474697. This article has 6 citations and is from a peer-reviewed journal.

10. (schiller2024identificationofstructural pages 9-9): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

11. (schiller2024identificationofstructural pages 5-6): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

12. (schiller2024identificationofstructural pages 1-2): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.