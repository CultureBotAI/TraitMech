---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:16:57.923476'
end_time: '2026-08-04T10:26:15.851539'
duration_seconds: 557.93
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: tailed shaped
  trait_identifier: METPO:1000695
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: tailed_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has an elongated polar appendage or
    stalk extending from the cell body.
  parent_traits: METPO:1000666
  synonyms: tailed
  evidence_summary: 'DOI:10.1146/annurev.micro.061705.103240: prosthecate bacteria
    (Prosthecate-bacteria review supports tailed/stalked cell morphology in Caulobacter
    and related lineages.) | DOI:10.1146/annurev-cellbio-101011-155745: polar growth
    (Cell-shape review supports unipolar peptidoglycan growth as the basis for stalk-like
    polar appendages.)'
  causal_graph_summary: 'tailed_shaped_polar_stalk_growth: 11 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** tailed shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000695
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated polar appendage or stalk extending from the cell body.
- **Parent traits:** METPO:1000666
- **Synonyms:** tailed
- **Existing evidence:** DOI:10.1146/annurev.micro.061705.103240: prosthecate bacteria (Prosthecate-bacteria review supports tailed/stalked cell morphology in Caulobacter and related lineages.) | DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports unipolar peptidoglycan growth as the basis for stalk-like polar appendages.)
- **Existing causal graph summary:** tailed_shaped_polar_stalk_growth: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **tailed shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/tailed_shaped.yaml`.

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
- **Trait label:** tailed shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000695
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated polar appendage or stalk extending from the cell body.
- **Parent traits:** METPO:1000666
- **Synonyms:** tailed
- **Existing evidence:** DOI:10.1146/annurev.micro.061705.103240: prosthecate bacteria (Prosthecate-bacteria review supports tailed/stalked cell morphology in Caulobacter and related lineages.) | DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports unipolar peptidoglycan growth as the basis for stalk-like polar appendages.)
- **Existing causal graph summary:** tailed_shaped_polar_stalk_growth: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **tailed shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/tailed_shaped.yaml`.

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


# Curation report: microbial “tailed shaped” morphology

## Executive summary

The target is the reviewed morphology class **“tailed shaped”**, identifier **“METPO:1000695”**, defined as a cell shape in which an organism has an elongated polar appendage or stalk extending from the cell body. For TraitMech, the defensible core interpretation is a **prosthecate/stalked cell-envelope morphology**, not any tail-like appendage.

The best-resolved mechanism is in *Caulobacter crescentus*: localized remodeling and synthesis of peptidoglycan (PG) at the old pole produces a stalk containing inner membrane, PG, and outer membrane. A specialized MreB-dependent complex spatially coordinates synthases and hydrolases, while a BacA/B–PbpC module promotes extension. Under phosphate limitation, stalks can lengthen as much as **20-fold**; 2024 work refines this response by showing that low **cytoplasmic**, rather than PhoB activation alone, controls the characteristic morphological adaptation. Mechanistic variants occur in *Asticcacaulis* and *Hyphomonas*, so these should be represented as taxon-specific branches rather than universal requirements. (billini2019aspecializedmrebdependent pages 2-3, billini2019aspecializedmrebdependent pages 18-19, billini2024thecytoplasmicphosphate pages 10-11, billini2024thecytoplasmicphosphate pages 1-2)

## 1. Trait scope and boundaries

### Included phenotype

A positive instance should exhibit a relatively narrow, elongated extension continuous with the cell envelope—a **stalk or prostheca**—arising from a defined cell-body site. In *C. crescentus*, the stalk contains inner membrane, PG, and outer membrane but lacks cytoplasm; it is therefore an envelope extension rather than a second cell compartment. New PG is incorporated in a stalk-proximal polar zone, supporting growth by remodeling the old polar cap into stalk material. (billini2019aspecializedmrebdependent pages 2-3, billini2019aspecializedmrebdependent pages 19-21, billini2019aspecializedmrebdependent pages 18-19)

The class can encompass:

- single polar stalks, such as in *Caulobacter*;
- subpolar or bilateral prosthecae in related stalked bacteria, if they satisfy the supplied definition despite its use of “polar”;
- normal developmental stalk stages in dimorphic or budding organisms;
- environmentally lengthened stalks, which are changes in degree rather than distinct traits.

### Excluded or separately represented structures

1. **Flagella and pili:** these are proteinaceous motility or adhesion appendages, not extensions of the cell envelope and PG sacculus.
2. **Holdfast alone:** the adhesive holdfast can occur at the stalk tip but is a chemically and developmentally distinct adhesin. Holdfast synthesis may precede stalk biogenesis and should be modeled as associated with, rather than constitutive of, the tailed shape.
3. **Ordinary rod poles or polar cell-body elongation:** polar PG growth is not sufficient unless it creates a distinct appendage.
4. **Division necks and chains:** failed cytokinesis can produce skinny, stalk-like connections, but these are pathological division products rather than normal prosthecae.
5. **Reproductive hyphae:** *Rhodomicrobium* and related bacteria make offspring through hyphae. These may look tail-like but combine extension with reproductive growth and should not automatically be merged with non-reproductive stalks.
6. **Pseudostalks:** amorphous protrusions caused by loss of spatial control are valuable negative/abnormal phenotypes, not straightforward positive instances of normal “tailed shaped.” In *Asticcacaulis biprosthecum*, deletion of `bacA` or its terminal domains causes unconstrained PG insertion and pseudostalks. (jacq2024functionalspecializationof pages 6-10)

## 2. Current mechanistic model

### Core *Caulobacter* mechanism

Stalk production is best modeled as **spatially restricted cell-wall morphogenesis**. Zonal PG synthesis at the old pole/stalk base creates the extension. MreB acts as a central organizer for a specialized complex combining elongasome components—RodZ, RodA, PBP2, and MreC—with hydrolase/remodeling proteins DipM, SdpA, SdpB, and CrbA. Unlike cytokinesis, stalk formation does not require FtsZ, even though some participating factors were co-opted from divisome-associated machinery. An `mreB` sandwich-fusion allele abolished stalk formation under phosphate-replete and phosphate-limited conditions while causing only mild general shape defects, providing unusually strong stalk-specific evidence. (billini2019aspecializedmrebdependent pages 19-21, billini2019aspecializedmrebdependent pages 18-19, billini2019aspecializedmrebdependent pages 14-16)

A partly downstream extension module consists of the bactofilins BacA/B and class-A PBP PbpC. BacA/B assemble at the nascent stalked pole and remain at the stalk base, where they recruit PbpC. Loss of BacA/B, PbpC, or StpX decreases stalk length without destroying gross stalk architecture, supporting a role in elongation rather than initiation. BacA localization is MreB-independent, but the BacA–PbpC module cannot establish a stalk without functional MreB-dependent machinery. (billini2019aspecializedmrebdependent pages 21-22, barrows2023synchronizedswarmersand pages 11-13)

The stalk is mechanically and diffusively specialized. Its PG has elevated crosslinkage, especially 3–3 crosslinks associated with LD-transpeptidase activity, potentially increasing resistance to bending and breakage under flow. StpABCD crossbands form non-selective diffusion barriers; StpA recruits the remainder of that complex. (billini2019aspecializedmrebdependent pages 2-3, billini2019aspecializedmrebdependent pages 21-22, barrows2023synchronizedswarmersand pages 11-13)

### Environmental regulation

Phosphate limitation induces extensive stalk elongation—reported as up to **20 times** the phosphate-replete length. PstSCAB is the high-affinity phosphate ABC transporter whose transport state communicates environmental phosphate availability to PhoR–PhoB. Low external phosphate promotes PhoR kinase activity and PhoB phosphorylation, inducing genes for phosphate scavenging and uptake. A 2016 ChIP-seq/expression study identified nearly **50 PhoB-regulated genes**, including **15 membrane transporters**. (billini2019aspecializedmrebdependent pages 2-3, lubin2016identificationofthe pages 1-2)

The 2024 update materially changes the causal interpretation: heterologous PitA transport was used to uncouple phosphate uptake from PstSCAB signaling. The results support a two-pronged response in which PstSCAB–PhoR–PhoB primarily activates alternative-phosphate utilization, whereas the **cytoplasmic phosphate pool controls cell and stalk elongation** during global phosphate limitation. The study defined a robust PhoB-associated set of **47 genes** and showed that replenishing cytoplasmic phosphate restored normal stalk length even in a `pstS` mutant. The sensor of cytoplasmic phosphate remains unknown; PhoU depletion did not block PitA-mediated restoration, arguing against PhoU as the principal sensor. (billini2024thecytoplasmicphosphate pages 8-9, billini2024thecytoplasmicphosphate pages 10-11, billini2024thecytoplasmicphosphate pages 1-2, billini2024thecytoplasmicphosphate pages 7-8)

### Recent taxon-specific advances

In *Hyphomonas neptunium*, BacA/BacD polymers move between stalk-base and bud-neck boundaries. Depletion or deletion causes unconstrained stalk and bud growth. In the bactofilin-null background, RodZ-containing elongasomes enter the nascent stalk and produce amorphous extensions, whereas in wild type RodZ complexes are excluded. Thus, the bactofilin structure appears to delimit growth zones rather than simply recruit a synthase. (pohl2024adynamicbactofilin pages 6-7, pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 9-10)

The same 2024 study identified LmdC, an M23-family PG endopeptidase, as a BacA partner. CRISPRi depletion caused distorted or amorphous stalked/budding cells, and bio-layer interferometry measured direct BacA binding to the cytoplasmic domain of LmdC with an apparent **KD of approximately 15 μM**. This supports a bactofilin–hydrolase morphogenesis module, but not a universal stalk mechanism. (pohl2024adynamicbactofilin pages 15-16)

A December 2024 *A. biprosthecum* preprint resolved BacA domain functions. Its β-helical core supports polymerization, the N-terminal region contributes to membrane association/localization, and the C-terminal region is implicated in interaction with SpmX. Removing the N-terminal domain reduced wild-type-like stalks from **46 ± 3%** to **5 ± 1%**. A C-to-C polymerization mutant formed stalks in **41%** of cells versus **50%** in wild type, but those stalks were short and thin. These results strengthen BacA’s role as a topological organizer but should remain explicitly preprint-qualified. (jacq2024functionalspecializationof pages 13-17, jacq2024functionalspecializationof pages 6-10, jacq2024functionalspecializationof pages 1-6)

## 3. Candidate graph nodes

### Trait and anatomical nodes

- **“METPO:1000695”** — tailed shaped; target class.
- Stalk/prostheca — label-only candidate unless an appropriate anatomy CURIE is identified.
- Stalk base / old cell pole / stalked pole — cellular-localization candidates.
- Cell body.
- Crossband.
- Holdfast — separate associated structure, not a component of the trait definition.
- Pseudostalk — abnormal morphology node.

### Processes and molecular structures

- Peptidoglycan biosynthetic process — **GO:0009252**.
- Peptidoglycan metabolic process — **GO:0000270**.
- Zonal stalk-base PG synthesis — label-only specialized process.
- PG remodeling/hydrolysis.
- Bactofilin polymerization.
- Protein localization to the stalk base.
- Stalk elongation.
- Crossband-mediated diffusion barrier formation.
- Phosphate-starvation response — candidate GO mapping should be checked before curation.

### Genes and proteins

- **MreB**, **RodZ**, **RodA**, **MreC**, **PBP2** — scaffold and synthase components.
- **BacA**, **BacB**, **PbpC**, **StpX** — *Caulobacter* extension/localization module.
- **DipM**, **SdpA**, **SdpB**, **CrbA**, **LdpA** — PG remodeling factors.
- **StpA**, **StpB**, **StpC**, **StpD** — crossband complex.
- **PhoR**, **PhoB**, **PhoU**, **PstS/PstC/PstA/PstB**, heterologous **PitA** — phosphate response nodes.
- **SpmX** — *Asticcacaulis*-specific positional regulator.
- **BacD**, **LmdC** — *H. neptunium*-specific morphogenesis factors.

Species/strain-specific proteins should initially remain label-only or use verified organism-specific UniProt accessions. Gene symbols alone are not globally unique.

### Chemicals and environmental factors

- Inorganic phosphate — **CHEBI:18367**.
- Low extracellular inorganic phosphate.
- Low cytoplasmic inorganic phosphate.
- Peptidoglycan — **CHEBI:8005**.
- Phosphate-replete versus phosphate-free/limiting growth medium.
- Fluorescent D-amino acids and radiolabeled D-cysteine/glucose — assay factors, not causal biological nodes unless the graph represents measurement provenance.

### Taxon/context nodes

- *Caulobacter crescentus* — **NCBITaxon:155892** is commonly used for strain CB15; verify strain alignment for each experiment.
- *Asticcacaulis biprosthecum* — taxon CURIE should be registry-verified before insertion.
- *Hyphomonas neptunium* — taxon CURIE should be registry-verified before insertion.

## 4. Candidate causal edges

The following compact table is suitable as the starting point for converting the existing 11-node/10-edge summary into a better-supported, taxon-aware graph.

| Subject | Predicate | Object | Taxon/context | Evidence strength | Reference DOI |
|---|---|---|---|---|---|
| Low cytoplasmic phosphate | increases | stalk elongation | *Caulobacter crescentus* phosphate starvation response; morphology controlled mainly by cytoplasmic Pi rather than PhoB alone (billini2024thecytoplasmicphosphate pages 10-11, billini2024thecytoplasmicphosphate pages 1-2) | Strong direct | 10.1038/s42003-024-06469-y |
| Zonal peptidoglycan synthesis at the old cell pole / stalk base | produces | stalk/prostheca elongation | *Caulobacter crescentus*; radiolabel and FDAA evidence for stalk-proximal PG incorporation (billini2019aspecializedmrebdependent pages 2-3, billini2019aspecializedmrebdependent pages 18-19) | Strong direct | 10.1371/journal.pgen.1007897 |
| MreB | organizes/recruits | stalk peptidoglycan biosynthetic machinery | *Caulobacter crescentus*; MreB central scaffold, stalkless phenotype in mreBsw mutant, polar recruitment defects (billini2019aspecializedmrebdependent pages 19-21, billini2019aspecializedmrebdependent pages 18-19, billini2019aspecializedmrebdependent pages 14-16) | Strong direct | 10.1371/journal.pgen.1007897 |
| RodZ | enables | stalk peptidoglycan synthesis | *Caulobacter crescentus* phosphate-limited stalk formation; stalk-base localization (billini2019aspecializedmrebdependent pages 14-16) | Moderate direct | 10.1371/journal.pgen.1007897 |
| RodA | enables | stalk peptidoglycan synthesis | *Caulobacter crescentus*; elongasome-specific GTase required for stalk elongation (billini2019aspecializedmrebdependent pages 2-3, barrows2023synchronizedswarmersand pages 11-13) | Moderate direct | 10.1371/journal.pgen.1007897 |
| MreC | enables/scaffolds | stalk peptidoglycan synthesis machinery | *Caulobacter crescentus*; interacts with PG enzymes and is essential for stalk biosynthesis (billini2019aspecializedmrebdependent pages 14-16) | Moderate direct | 10.1371/journal.pgen.1007897 |
| PBP2 | contributes to | stalk peptidoglycan synthesis complex | *Caulobacter crescentus* specialized stalk biosynthetic complex (billini2019aspecializedmrebdependent pages 18-19) | Moderate direct | 10.1371/journal.pgen.1007897 |
| BacA/B bactofilins | recruit | PbpC | *Caulobacter crescentus* stalk-base extension module (billini2019aspecializedmrebdependent pages 21-22, barrows2023synchronizedswarmersand pages 11-13) | Strong direct | 10.1371/journal.pgen.1007897 |
| PbpC | supports | stalk extension | *Caulobacter crescentus*; absence decreases stalk length without changing overall structure (barrows2023synchronizedswarmersand pages 11-13) | Moderate direct | 10.1128/jb.00384-22 |
| PbpC | recruits/supports recruitment of | StpX | *Caulobacter crescentus*; PbpC required for recruitment of stalk elongation modulator StpX (barrows2023synchronizedswarmersand pages 11-13) | Moderate review-backed | 10.1128/jb.00384-22 |
| DipM / SdpA / SdpB / CrbA | remodel | stalk-base peptidoglycan | *Caulobacter crescentus*; autolytic/divisome-linked factors localize to stalk base and are required for morphogenesis (billini2019aspecializedmrebdependent pages 18-19, billini2019aspecializedmrebdependent pages 14-16) | Strong direct | 10.1371/journal.pgen.1007897 |
| SpmX | positions | BacA and stalk synthesis site | *Asticcacaulis biprosthecum* / *Asticcacaulis* spp.; taxon-specific, preprint-backed interaction model via BacA C-terminus (jacq2024functionalspecializationof pages 13-17, jacq2024functionalspecializationof pages 1-6) | Moderate, taxon-specific, preprint | 10.1101/2024.12.16.628611 |
| BacA polymerization and membrane association | enables | proper stalk morphology | *Asticcacaulis biprosthecum*; loss of N/C termini or polymerization defects yields pseudostalks (jacq2024functionalspecializationof pages 13-17, jacq2024functionalspecializationof pages 6-10, jacq2024functionalspecializationof pages 1-6) | Moderate direct, preprint | 10.1101/2024.12.16.628611 |
| BacA/BacD bactofilin cytoskeleton | excludes/confines | RodZ elongasome from stalk compartment | *Hyphomonas neptunium*; loss causes RodZ entry into stalk and amorphous extensions (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 9-10) | Strong direct, taxon-specific | 10.7554/eLife.86577 |
| LmdC (M23 peptidase) | interacts with | BacA | *Hyphomonas neptunium*; direct binding by bio-layer interferometry, apparent KD ~15 µM (pohl2024adynamicbactofilin pages 15-16) | Strong direct, taxon-specific | 10.7554/eLife.86577 |
| LmdC | supports | proper stalked/budding morphology | *Hyphomonas neptunium*; CRISPRi depletion causes distorted/amorphous cells (pohl2024adynamicbactofilin pages 15-16) | Strong direct, taxon-specific | 10.7554/eLife.86577 |
| StpABCD complex | forms | crossband diffusion barriers | *Caulobacter crescentus* stalk; limits diffusion along stalk length (barrows2023synchronizedswarmersand pages 11-13, billini2019aspecializedmrebdependent pages 2-3) | Moderate review + prior primary support | 10.1128/jb.00384-22 |


*Table: This table compiles the strongest curation-ready causal edges for the tailed/stalked morphology trait METPO:1000695. It highlights core *Caulobacter* mechanisms and clearly marks taxon-specific and preprint-supported extensions from *Asticcacaulis* and *Hyphomonas*.*

### Recommended predicate discipline

Use predicates such as `positively_regulates`, `required_for`, `recruits`, `localizes_to`, `directly_interacts_with`, `produces`, and `part_of`. Avoid collapsing all findings into `causes`. For example, mutant loss-of-function supports “required for normal stalk elongation” more directly than “causes tailed shape.” Experimental context and taxon should be attached to every edge.

## 5. Curation-ready evidence snippets and interpretation

| Proposed triple | Supporting snippet | Interpretation and caution |
|---|---|---|
| Low cytoplasmic Pi — `positively_regulates_when_decreased` → stalk elongation | “the cytoplasmic phosphate level controls the morphological and physiological adaptation” | Strong 2024 evidence from uncoupling PstSCAB signaling and uptake; encode low cytoplasmic Pi, not PhoB activation, as the proximal regulatory state. (billini2024thecytoplasmicphosphate pages 1-2) |
| PhoR–PhoB — `promotes` → alternative-phosphate utilization | “PhoR-PhoB signaling mostly facilitates the utilization of alternative phosphate sources” | Strong, but this is not equivalent to directly causing stalk elongation. (billini2024thecytoplasmicphosphate pages 1-2) |
| Zonal polar PG synthesis — `produces` → stalk | “stalk formation occurs through zonal peptidoglycan synthesis at the stalk base” | Direct labeling evidence; suitable core edge. (billini2019aspecializedmrebdependent pages 2-3) |
| MreB — `required_for` → stalk formation | `mreBsw` “completely abolished stalk formation under all growth conditions” | Strong genetic evidence; allele-specific but highly informative. (billini2019aspecializedmrebdependent pages 18-19) |
| MreB — `recruits` → stalk PG machinery | MreB “mediates recruitment of synthetic and lytic proteins to the stalked pole” | Strong localization/genetic evidence; individual client dependencies vary. (billini2019aspecializedmrebdependent pages 19-21) |
| BacA/B — `recruits` → PbpC | “These bactofilins interact with … PbpC … and recruit it to the stalk” | Strong in *C. crescentus*; do not universalize to all prosthecate bacteria. (barrows2023synchronizedswarmersand pages 11-13) |
| PbpC — `promotes` → stalk extension | Loss decreases stalk length without changing overall structure | Supports extension, not initial specification. (barrows2023synchronizedswarmersand pages 11-13) |
| StpABCD — `forms` → crossband diffusion barrier | “crossbands … are composed of a complex of four proteins, StpABCD” | Secondary-review statement; trace to primary crossband paper before final production curation. (barrows2023synchronizedswarmersand pages 11-13) |
| SpmX — `positions` → *Asticcacaulis* stalk synthesis | BacA C-terminal defects imply interaction with “the stalk-specific morphological regulator SpmX” | Taxon-specific and partly interaction-model based; preprint evidence. (jacq2024functionalspecializationof pages 13-17) |
| BacA polymerization — `required_for` → normal *Asticcacaulis* stalk | Polymerization-defective mutants “lead to stalk synthesis defects” | Direct mutational evidence, but December 2024 preprint. (jacq2024functionalspecializationof pages 1-6) |
| BacA/D — `excludes` → RodZ elongasome from stalk | Without BacA/D, elongasome “was no longer excluded from the nascent stalk” | Strong microscopy evidence in *H. neptunium*; organism-specific mechanism. (pohl2024adynamicbactofilin pages 9-10) |
| LmdC — `directly_interacts_with` → BacA | One-site fit yielded apparent **KD ≈15 μM** | Direct in-vitro binding; couple to in-vivo depletion evidence for morphology. (pohl2024adynamicbactofilin pages 15-16) |

## 6. Applications and real-world relevance

This research currently has three principal applications:

1. **Morphology prediction and phenotype annotation.** A taxon-aware causal graph can improve interpretation of genomes containing bactofilins, PG synthases, and polarity factors. Presence of BacA alone is not predictive, however, because bactofilins have many non-stalk functions.
2. **Environmental adaptation studies.** Stalk length is widely used as a morphological marker of phosphate status in *Caulobacter*. The 2024 distinction between extracellular PstSCAB–PhoB signaling and cytoplasmic-phosphate control means that stalk length should not be interpreted as a simple reporter of PhoB phosphorylation. (billini2024thecytoplasmicphosphate pages 10-11, billini2024thecytoplasmicphosphate pages 1-2)
3. **Synthetic and comparative morphogenesis.** The modular reuse of elongasome/divisome components and taxon-specific regulators provides a tractable framework for repositioning PG growth. The authoritative 2023 synthesis emphasizes that core factors are conserved but `bacB`, `pbpC`, `stpX`, and `stpABCD` are poorly conserved outside *Caulobacter*, demonstrating that similar stalk phenotypes can arise through distinct molecular architectures. (barrows2023synchronizedswarmersand pages 11-13)

There is presently no demonstrated clinical implementation specific to stalk formation. Antimicrobial targeting of generic PG enzymes is relevant broadly, but should not be presented as a real-world application of this trait mechanism without direct evidence.

## 7. Warnings: claims not yet ready for TraitMech

- **Do not curate “PhoB directly causes stalk elongation.”** Current evidence places cytoplasmic phosphate downstream or parallel to environmental sensing as the closer morphological control variable. (billini2024thecytoplasmicphosphate pages 10-11, billini2024thecytoplasmicphosphate pages 1-2)
- **Do not make SpmX universal.** It specifies stalk position in *Asticcacaulis*, whereas it is not required for correct stalk localization in *Caulobacter*. (billini2019aspecializedmrebdependent pages 21-22)
- **Do not make PbpC, StpX, or StpABCD universal.** Their conservation outside *Caulobacter* is poor. (barrows2023synchronizedswarmersand pages 11-13)
- **Do not merge pseudostalks with normal stalks.** Pseudostalks reflect loss of zonal control and are abnormal protrusions.
- **Do not equate stalks with holdfasts, pili, flagella, or reproductive hyphae.** These differ in composition and developmental function.
- **Treat BacA–SpmX domain assignments as provisional.** The principal 2024 source is a bioRxiv preprint, and some interaction language is inferential. (jacq2024functionalspecializationof pages 13-17, jacq2024functionalspecializationof pages 1-6)
- **Treat the nutrient-uptake advantage as plausible but not universal.** Surface-area and transporter-localization arguments do not prove that every stalk improves phosphate acquisition under every ecological condition.
- **Verify all ontology identifiers and organism-specific accessions at ingest time.** No UniProt, EC, Rhea, or KEGG identifiers should be inferred from gene labels alone.
- **Do not curate FtsZ as required for stalk biogenesis.** Direct work found stalk formation independent of FtsZ, although several divisome-associated hydrolases were co-opted into the stalk complex. (billini2019aspecializedmrebdependent pages 18-19)

## 8. DOI-first bibliography

1. **Billini M, Hoffmann T, Kühn J, Bremer E, Thanbichler M.** “The cytoplasmic phosphate level has a central regulatory role in the phosphate starvation response of *Caulobacter crescentus*.” *Communications Biology* 7:772. Published **June 2024**. DOI: [10.1038/s42003-024-06469-y](https://doi.org/10.1038/s42003-024-06469-y). (billini2024thecytoplasmicphosphate pages 1-2)
2. **Pöhl S, Osorio-Valeriano M, Cserti E, et al.** “A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis.” *eLife*. Version of record published **31 January 2024**. DOI: [10.7554/eLife.86577](https://doi.org/10.7554/eLife.86577). (pohl2024adynamicbactofilin pages 1-2)
3. **Jacq M, Caccamo PD, Brun YV.** “Functional specialization of the subdomains of a bactofilin driving stalk morphogenesis in *Asticcacaulis biprosthecum*.” bioRxiv preprint, published **16 December 2024**. DOI: [10.1101/2024.12.16.628611](https://doi.org/10.1101/2024.12.16.628611). (jacq2024functionalspecializationof pages 1-6)
4. **Barrows JM, Goley ED.** “Synchronized Swarmers and Sticky Stalks: *Caulobacter crescentus* as a Model for Bacterial Cell Biology.” *Journal of Bacteriology* 205(2). Published **February 2023**. DOI: [10.1128/jb.00384-22](https://doi.org/10.1128/jb.00384-22). (barrows2023synchronizedswarmersand pages 11-13)
5. **Billini M, Biboy J, Kühn J, Vollmer W, Thanbichler M.** “A specialized MreB-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in *Caulobacter crescentus*.” *PLoS Genetics* 15:e1007897. Published **February 2019**. DOI: [10.1371/journal.pgen.1007897](https://doi.org/10.1371/journal.pgen.1007897). (billini2019aspecializedmrebdependent pages 2-3, billini2019aspecializedmrebdependent pages 18-19)
6. **Lubin EA, Henry JT, Fiebig A, Crosson S, Laub MT.** “Identification of the PhoB Regulon and Role of PhoU in the Phosphate Starvation Response of *Caulobacter crescentus*.” *Journal of Bacteriology* 198:187–200. Published **January 2016**. DOI: [10.1128/JB.00658-15](https://doi.org/10.1128/JB.00658-15). (lubin2016identificationofthe pages 1-2)
7. **Jiang C, Brown PJB, Ducret A, Brun YV.** “Sequential evolution of bacterial morphology by co-option of a developmental regulator.” *Nature*. Published **2014**. DOI: [10.1038/nature12900](https://doi.org/10.1038/nature12900). This is the foundational source for SpmX-dependent repositioning and multiplication of stalk sites; its full text was not available in the retrieved evidence set, so exact edge wording should be checked before production curation.
8. **Schlimpert S, Klein EA, Briegel A, et al.** “General protein diffusion barriers create compartments within bacterial cells.” *Cell* 151:1270–1282. Published **December 2012**. DOI: [10.1016/j.cell.2012.10.046](https://doi.org/10.1016/j.cell.2012.10.046). Foundational crossband/diffusion-barrier source; verify exact protein-level claims against the full article before ingest.

## Recommended TraitMech structure

Retain a small universal core—**localized PG synthesis/remodeling → stalk/prostheca → “METPO:1000695”**—and place molecular implementations beneath taxon-qualified branches. A *Caulobacter* branch should contain low cytoplasmic phosphate, MreB/Rod machinery, hydrolases, and BacA/B–PbpC; an *Asticcacaulis* branch should contain SpmX and BacA topological organization; and a *Hyphomonas* branch should contain the BacA/D growth-zone barrier and LmdC. This structure reflects convergent or diverged implementations without asserting that one model organism’s gene set defines the morphology class.

References

1. (billini2019aspecializedmrebdependent pages 2-3): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

2. (billini2019aspecializedmrebdependent pages 18-19): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

3. (billini2024thecytoplasmicphosphate pages 10-11): Maria Billini, Tamara Hoffmann, Juliane Kühn, Erhard Bremer, and Martin Thanbichler. The cytoplasmic phosphate level has a central regulatory role in the phosphate starvation response of caulobacter crescentus. Communications Biology, Jun 2024. URL: https://doi.org/10.1038/s42003-024-06469-y, doi:10.1038/s42003-024-06469-y. This article has 12 citations and is from a peer-reviewed journal.

4. (billini2024thecytoplasmicphosphate pages 1-2): Maria Billini, Tamara Hoffmann, Juliane Kühn, Erhard Bremer, and Martin Thanbichler. The cytoplasmic phosphate level has a central regulatory role in the phosphate starvation response of caulobacter crescentus. Communications Biology, Jun 2024. URL: https://doi.org/10.1038/s42003-024-06469-y, doi:10.1038/s42003-024-06469-y. This article has 12 citations and is from a peer-reviewed journal.

5. (billini2019aspecializedmrebdependent pages 19-21): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

6. (jacq2024functionalspecializationof pages 6-10): Maxime Jacq, Paul D. Caccamo, and Yves V. Brun. Functional specialization of the subdomains of a bactofilin driving stalk morphogenesis in asticcacaulis biprosthecum. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.16.628611, doi:10.1101/2024.12.16.628611. This article has 1 citations.

7. (billini2019aspecializedmrebdependent pages 14-16): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

8. (billini2019aspecializedmrebdependent pages 21-22): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

9. (barrows2023synchronizedswarmersand pages 11-13): Jordan M. Barrows and Erin D. Goley. Synchronized swarmers and sticky stalks: caulobacter crescentus as a model for bacterial cell biology. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00384-22, doi:10.1128/jb.00384-22. This article has 61 citations and is from a peer-reviewed journal.

10. (lubin2016identificationofthe pages 1-2): Emma A. Lubin, Jonathan T. Henry, Aretha Fiebig, Sean Crosson, and Michael T. Laub. Identification of the phob regulon and role of phou in the phosphate starvation response of caulobacter crescentus. Jan 2016. URL: https://doi.org/10.1128/jb.00658-15, doi:10.1128/jb.00658-15. This article has 96 citations and is from a peer-reviewed journal.

11. (billini2024thecytoplasmicphosphate pages 8-9): Maria Billini, Tamara Hoffmann, Juliane Kühn, Erhard Bremer, and Martin Thanbichler. The cytoplasmic phosphate level has a central regulatory role in the phosphate starvation response of caulobacter crescentus. Communications Biology, Jun 2024. URL: https://doi.org/10.1038/s42003-024-06469-y, doi:10.1038/s42003-024-06469-y. This article has 12 citations and is from a peer-reviewed journal.

12. (billini2024thecytoplasmicphosphate pages 7-8): Maria Billini, Tamara Hoffmann, Juliane Kühn, Erhard Bremer, and Martin Thanbichler. The cytoplasmic phosphate level has a central regulatory role in the phosphate starvation response of caulobacter crescentus. Communications Biology, Jun 2024. URL: https://doi.org/10.1038/s42003-024-06469-y, doi:10.1038/s42003-024-06469-y. This article has 12 citations and is from a peer-reviewed journal.

13. (pohl2024adynamicbactofilin pages 6-7): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

14. (pohl2024adynamicbactofilin pages 1-2): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

15. (pohl2024adynamicbactofilin pages 9-10): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

16. (pohl2024adynamicbactofilin pages 15-16): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

17. (jacq2024functionalspecializationof pages 13-17): Maxime Jacq, Paul D. Caccamo, and Yves V. Brun. Functional specialization of the subdomains of a bactofilin driving stalk morphogenesis in asticcacaulis biprosthecum. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.16.628611, doi:10.1101/2024.12.16.628611. This article has 1 citations.

18. (jacq2024functionalspecializationof pages 1-6): Maxime Jacq, Paul D. Caccamo, and Yves V. Brun. Functional specialization of the subdomains of a bactofilin driving stalk morphogenesis in asticcacaulis biprosthecum. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.16.628611, doi:10.1101/2024.12.16.628611. This article has 1 citations.