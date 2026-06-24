---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:10:22.827792'
end_time: '2026-06-18T10:24:23.832746'
duration_seconds: 841.0
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'tailed_shaped_polar_stalk_growth: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 14
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** tailed shaped
- **METPO identifier:** METPO:1000695
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated polar appendage or stalk extending from the cell body.
- **Parent traits:** METPO:1000666
- **Synonyms:** tailed
- **Existing evidence:** DOI:10.1146/annurev.micro.061705.103240: prosthecate bacteria (Prosthecate-bacteria review supports tailed/stalked cell morphology in Caulobacter and related lineages.) | DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports unipolar peptidoglycan growth as the basis for stalk-like polar appendages.)
- **Existing causal graph summary:** tailed_shaped_polar_stalk_growth: 4 nodes, 3 edges

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
- **METPO identifier:** METPO:1000695
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated polar appendage or stalk extending from the cell body.
- **Parent traits:** METPO:1000666
- **Synonyms:** tailed
- **Existing evidence:** DOI:10.1146/annurev.micro.061705.103240: prosthecate bacteria (Prosthecate-bacteria review supports tailed/stalked cell morphology in Caulobacter and related lineages.) | DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports unipolar peptidoglycan growth as the basis for stalk-like polar appendages.)
- **Existing causal graph summary:** tailed_shaped_polar_stalk_growth: 4 nodes, 3 edges

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


# Research report: METPO:1000695 “tailed shaped” (prosthecate/stalked morphology)

## 1) Scope summary (trait definition and boundaries)

**Trait label:** tailed shaped (syn. *tailed*)  
**METPO:** METPO:1000695  
**Category:** MORPHOLOGY  
**Curatable phenotype:** a **prostheca/stalk**—an **elongated polar extension of the cell envelope** (inner membrane, outer membrane, and peptidoglycan) that contains a **thin thread of cytoplasm** and grows by **zonal cell-wall insertion at its base**. In *Caulobacter crescentus*, the stalk is described as an envelope extension and a distinct compartment that lacks ribosomes/nucleoid and contains crossbands that restrict diffusion along the stalk. (barrows2023synchronizedswarmersand pages 5-7, barrows2023synchronizedswarmersand pages 11-13, pohl2024adynamicbactofilin pages 2-3)

### Boundary cases / what this trait is **not**
* **Not flagella or pili:** swarmer cells bear **flagellum** and **type IV pili**, which are proteinaceous surface filaments for motility/sensing/attachment; stalks are envelope-bound protrusions built by peptidoglycan morphogenesis rather than external filament polymers. (barrows2023synchronizedswarmersand pages 5-7)
* **Stalks vs hyphae:** prosthecate appendices can be classified by function into **stalks** (nonreproductive; attachment/elevation/nutrient uptake) versus **hyphae** (reproductive appendices dedicated to offspring formation; e.g., *Rhodomicrobium vannielii*, *Hyphomonas neptunium*). This distinction matters for curation: hyphal phenotypes may not map 1:1 to “tailed shaped” if METPO intends the *nonreproductive stalk* concept. (richter2023interactingbactofilinsimpact pages 13-15)
* **Malformed prosthecae (“pseudostalks”):** loss of topology control can yield short, wide, irregular protrusions (“pseudostalks”) that should be treated as **boundary/mis-phenotypes** rather than canonical tailed-shaped morphology. (pohl2024adynamicbactofilin pages 2-3)

## 2) Current mechanistic understanding (key concepts)

### 2.1 Structural/biophysical concept: a compartmentalized envelope extension
In *C. crescentus*, the stalk is an envelope extension and includes **diffusion-limiting crossbands** composed of a protein complex (StpABCD). Crossbands create diffusion barriers along the stalk; StpA directs recruitment of the remaining proteins. (barrows2023synchronizedswarmersand pages 5-7, barrows2023synchronizedswarmersand pages 11-13)

### 2.2 Morphogenetic concept: polarized peptidoglycan growth controlled by scaffolds and enzymes
Across multiple Alphaproteobacteria, stalk/prostheca growth is tightly linked to **spatially restricted peptidoglycan (PG) synthesis and remodeling**:
* **Bactofilins (BacA/B/C family)** are cytoskeletal scaffolds that polymerize and localize to specific growth zones (e.g., stalk base), organizing where PG synthesis/remodeling occurs. (barrows2023synchronizedswarmersand pages 11-13, pohl2024adynamicbactofilin pages 2-3)
* In *Caulobacter*, **BacA/BacB** interact with the cell-wall synthase **PbpC**, which is required to recruit **StpX**, a stalk-elongation modulator; absence of these factors decreases stalk length. (barrows2023synchronizedswarmersand pages 11-13)
* The **elongasome** components **MreB** and **RodA** localize to the stalk base and are necessary for stalk formation; depletion causes stalk elongation defects. (barrows2023synchronizedswarmersand pages 11-13)
* **Autolysins/remodelers** (DipM, SdpAB, CrbA; plus LdpA) are implicated in stalk morphogenesis; MreB inhibition prevents these enzymes (but not BacA) from localizing to the stalked pole, suggesting hierarchical assembly. (barrows2023synchronizedswarmersand pages 11-13)

### 2.3 Conserved module highlighted by 2024 work: bactofilin–M23 endopeptidase coupling
A 2024 study in the stalked budding alphaproteobacterium *Hyphomonas neptunium* identifies a conserved functional module where **bactofilin polymers** act as a barrier to retain cell-wall biosynthetic machinery in growth zones and **directly interact** with an **M23-family peptidoglycan endopeptidase (LmdC)**. LmdC depletion (CRISPRi) also causes unconstrained growth, supporting a functional interaction. (pohl2024adynamicbactofilin pages 2-3)

## 3) Recent developments (prioritizing 2023–2024)

### 3.1 2023: integrated, curation-friendly map of *Caulobacter* morphogenesis (review)
Barrows & Goley (2023) synthesize the field view that **bactofilins and MreB** recruit and regulate stalk elongation machinery at the stalk base, with specific factors (BacA/B, PbpC, StpX; StpABCD crossbands; MreB/RodA; autolysins) forming a linked mechanistic system. The paper also notes that several stalk-related genes are not well conserved outside *Caulobacter*, supporting clade-specific variants of the mechanism. (barrows2023synchronizedswarmersand pages 11-13)

### 3.2 2023: mechanistic separation of stalk vs reproductive hypha programs in Hyphomicrobiaceae
Richter et al. (2023) argue prosthecae subdivide into stalks versus hyphae and show that **bactofilin interactions** (e.g., BacA–BacC dependency for confined localization) are key to maintaining proper hyphal morphogenesis in *R. vannielii*. Their discussion emphasizes that prostheca formation can be mechanistically distinct even among related lineages (e.g., stalk-base vs tip-localized PG incorporation patterns). (richter2023interactingbactofilinsimpact pages 13-15)

### 3.3 2023: nutrient-responsive regulation linking nitrogen assimilation and polar morphogenesis
North et al. (2023) connect the **NtrB–NtrC** two-component system (nitrogen assimilation regulator) to development, reporting that **loss of NtrC function led to elongated polar stalks** and elevated envelope polysaccharide synthesis—an explicit regulatory link between nutrient status and the tailed-shaped phenotype. (north2023thecaulobacterntrbntrc pages 1-2)

### 3.4 2024: conserved “bactofilin + M23 endopeptidase” morphogenesis module
Pöhl et al. (eLife version via DOI, 2024) extend bactofilin function from a *Caulobacter*-centric view to a broader alphaproteobacterial module: localized bactofilin polymers regulate stalk/bud growth by **retaining** PG machinery at growth zones and by partnering with **LmdC**. The work also highlights **pseudostalk** formation when topology control fails (e.g., in *Asticcacaulis*). (pohl2024adynamicbactofilin pages 2-3)

## 4) Current applications and real-world implementations

### 4.1 Model systems and assay implementations
* **Model organism:** *C. crescentus* is used as a central model for asymmetric division and appendage biogenesis; stalk morphogenesis is integrated into a temporally regulated developmental program. (barrows2023synchronizedswarmersand pages 5-7, barrows2023synchronizedswarmersand pages 11-13)
* **Imaging/phenotyping practice:** Recent work emphasizes localization-based interpretation of morphogenesis: cytoskeletal proteins (including bactofilins and MreB) localize to the stalk base during the swarmer-to-stalk transition. (barrows2023synchronizedswarmersand pages 11-13, barrows2023synchronizedswarmersand media 86ba8ef1, barrows2023synchronizedswarmersand media 7cd7048b)

### 4.2 Environmental/nutrient response relevant to ecology
* **Phosphate starvation → stalk elongation:** stalk length is environmentally plastic; phosphate starvation induces elongated stalks in *Caulobacter*, consistent with a role in nutrient acquisition or microhabitat positioning. This provides a clean experimental lever (nutrient limitation) for inducing and assaying the trait. (barrows2023synchronizedswarmersand pages 5-7)

## 5) Candidate graph nodes (grouped by type)

### Phenotype nodes
* **Tailed shaped / stalked / prosthecate morphology** (METPO:1000695)
* **Stalk length** (label-only quantitative phenotype)
* **Pseudostalk** (label-only malformed prostheca phenotype; boundary case) (pohl2024adynamicbactofilin pages 2-3)

### Cellular structures / localizations
* **Stalk base** (site of zonal PG insertion) (pohl2024adynamicbactofilin pages 2-3)
* **Crossbands (diffusion barriers)** (label-only structure) (barrows2023synchronizedswarmersand pages 5-7, barrows2023synchronizedswarmersand pages 11-13)
* **Bud neck (in budding prosthecate bacteria)** (pohl2024adynamicbactofilin pages 2-3)

### Biological processes (GO grounding suggested; specific GO IDs not asserted here)
* Peptidoglycan biosynthetic process / cell wall morphogenesis (pohl2024adynamicbactofilin pages 2-3, barrows2023synchronizedswarmersand pages 11-13)
* Polarized/zonal growth at stalk base (pohl2024adynamicbactofilin pages 2-3)
* Protein localization to the stalked pole / stalk base (barrows2023synchronizedswarmersand pages 11-13)

### Genes/proteins/complexes (label-level candidates)
* **Bactofilins:** BacA, BacB, BacC (barrows2023synchronizedswarmersand pages 11-13, richter2023interactingbactofilinsimpact pages 13-15)
* **PG synthesis machinery:** PbpC; RodA; MreB (barrows2023synchronizedswarmersand pages 11-13)
* **Stalk elongation modulator:** StpX (barrows2023synchronizedswarmersand pages 11-13)
* **Crossband complex:** StpABCD (StpA as recruiter) (barrows2023synchronizedswarmersand pages 11-13)
* **Autolysins/remodelers:** DipM, SdpAB, CrbA; LdpA (barrows2023synchronizedswarmersand pages 11-13)
* **M23 PG endopeptidase module:** LmdC (pohl2024adynamicbactofilin pages 2-3)
* **Nutrient signaling regulators:** NtrB/NtrC (two-component system) (north2023thecaulobacterntrbntrc pages 1-2)

### Environmental/experimental factors (ENVO-style grounding suggested)
* **Phosphate starvation / phosphate limitation** (barrows2023synchronizedswarmersand pages 5-7)
* **Nitrogen status / ammonium as sole N source (via NtrB/NtrC control of nitrogen assimilation)** (north2023thecaulobacterntrbntrc pages 1-2)

## 6) Candidate causal edges (curation-focused)

The table below is structured for direct curation into a TraitMech causal graph (subject–predicate–object), with evidence snippets, DOI-first references, and grounding suggestions.

| Edge (Subject—predicate—Object) | Edge type (gene/protein/process/environment) | Taxon scope | Evidence snippet (verbatim from sources) | Reference (DOI URL + year) | Confidence | Ontology grounding suggestions | Notes for YAML curation |
|---|---|---|---|---|---|---|---|
| BacA/BacB—interacts_with/recruits—PbpC | gene/protein | *Caulobacter crescentus* | “These bactofilins interact with the cell wall synthase PbpC” (barrows2023synchronizedswarmersand pages 11-13) | https://doi.org/10.1128/jb.00384-22 (2023) | high | BacA/BacB: label-only bactofilin proteins; PbpC: penicillin-binding protein/cell wall synthase label-only; GO: peptidoglycan biosynthetic process | Direct molecular interaction edge; taxon-specific to *Caulobacter* unless homolog evidence added. |
| PbpC—required_for_recruitment_of—StpX | gene/protein | *Caulobacter crescentus* | “PbpC, which is required for the recruitment of the stalk elongation modulator StpX” (barrows2023synchronizedswarmersand pages 11-13) | https://doi.org/10.1128/jb.00384-22 (2023) | high | PbpC: label-only; StpX: label-only stalk elongation modulator; GO: protein localization, peptidoglycan biosynthetic process | Good directional edge; links synthase to elongation modulator at stalk. |
| BacA/BacB/PbpC/StpX—positively_regulates—stalk extension | gene/protein | *Caulobacter crescentus* | “The absence of any of these factors results in a decrease in stalk length but do not change overall stalk structure, indicating roles specifically in stalk extension” (barrows2023synchronizedswarmersand pages 11-13) | https://doi.org/10.1128/jb.00384-22 (2023) | high | METPO:1000695 tailed shaped; GO: cell morphogenesis involved in differentiation | Could be decomposed into separate edges for each factor; phenotype is stalk length, not all-or-none presence. |
| MreB—required_for—stalk formation | gene/protein | *Caulobacter crescentus* | “MreB and RodA… are necessary for stalk formation, as depletion of either protein results in a stalk elongation defect” (barrows2023synchronizedswarmersand pages 11-13) | https://doi.org/10.1128/jb.00384-22 (2023) | high | MreB: bacterial actin homolog label-only; GO: cell shape determination, peptidoglycan biosynthetic process | Strong edge; may also support MreB localizes_to stalk base. |
| RodA—required_for—stalk formation | gene/protein | *Caulobacter crescentus* | “MreB and RodA… are necessary for stalk formation, as depletion of either protein results in a stalk elongation defect” (barrows2023synchronizedswarmersand pages 11-13) | https://doi.org/10.1128/jb.00384-22 (2023) | high | RodA: SEDS peptidoglycan polymerase label-only; GO: peptidoglycan glycosyltransferase activity | Strong edge; specific to elongation machinery. |
| MreB inhibition—prevents_localization_of—DipM/SdpAB/CrbA at stalked pole | process/gene-protein | *Caulobacter crescentus* | “MreB inhibition results in a failure of each of the autolytic enzymes, but not BacA, to localize to the stalked pole” (barrows2023synchronizedswarmersand pages 11-13) | https://doi.org/10.1128/jb.00384-22 (2023) | medium | DipM/SdpAB/CrbA: label-only autolysins; GO: cell wall hydrolase activity | Localization edge rather than direct morphology edge; supports hierarchical assembly of stalk machinery. |
| StpA—recruits—StpBCD complex | gene/protein | *Caulobacter crescentus* | “the aforementioned crossbands that limit diffusion along the length of the stalk are composed of a complex of four proteins, StpABCD, with StpA directing the recruitment of the rest of the complex” (barrows2023synchronizedswarmersand pages 11-13) | https://doi.org/10.1128/jb.00384-22 (2023) | high | StpA/B/C/D: label-only; GO: protein complex assembly | Strong assembly edge for diffusion-barrier subgraph. |
| StpABCD complex—forms—stalk crossband diffusion barriers | gene/protein/process | *Caulobacter crescentus* | “crossbands that limit diffusion along the length of the stalk are composed of a complex of four proteins, StpABCD” (barrows2023synchronizedswarmersand pages 11-13) | https://doi.org/10.1128/jb.00384-22 (2023) | high | GO: establishment of localization; cellular component label-only crossband; METPO:1000695 | This is more about stalk compartmentalization than initiation; still relevant stalk-structure edge. |
| Phosphate starvation—induces—elongated stalks | environment | *Caulobacter crescentus*; likely related prosthecate alphaproteobacteria | “cells starved of phosphate grow elongated stalks” (barrows2023synchronizedswarmersand pages 5-7) | https://doi.org/10.1128/jb.00384-22 (2023) | high | CHEBI: phosphate label-only; ENVO: nutrient limitation label-only | Clear environment→phenotype edge; useful for conditional regulation node. |
| Bactofilin absence—causes—pseudostalks | gene/protein | *Asticcacaulis biprosthecum* | “Its absence leads to the development of pseudostalks, which are much shorter and wider than normal stalks and irregularly shaped” (pohl2024adynamicbactofilin pages 2-3) | https://doi.org/10.7554/eLife.86577 (2024) | high | Bactofilin/BacA: label-only; METPO:1000695; GO: regulation of peptidoglycan biosynthetic process | Important boundary-case edge: pseudostalks are malformed analogs and should not be equated with normal tailed morphology. |
| Bactofilin—limits—peptidoglycan biosynthesis to stalk base | gene/protein/process | *Asticcacaulis biprosthecum* | “required to efficiently initiate stalk formation and limit peptidoglycan biosynthesis to the stalk base” (pohl2024adynamicbactofilin pages 2-3) | https://doi.org/10.7554/eLife.86577 (2024) | high | GO: peptidoglycan biosynthetic process; cellular component: stalk base label-only | Strong mechanistic edge connecting scaffold to spatial PG control. |
| Bactofilin polymers—localize_to—stalk base | gene/protein/localization | *Caulobacter crescentus*, *Asticcacaulis biprosthecum* | “In C. crescentus and Asticcacaulis biprosthecum, bactofilin polymers were shown to localize to the stalk base to direct proper stalk formation” (pohl2024adynamicbactofilin pages 2-3) | https://doi.org/10.7554/eLife.86577 (2024) | high | GO: protein localization to cell pole; cellular component: stalk base label-only | Localization edge; useful parent for downstream recruitment edges. |
| Bactofilins—recruit—cell wall synthase contributing to stalk elongation | gene/protein | *Caulobacter crescentus* | “In C. crescentus, they recruit a cell wall synthase that contributes to stalk elongation” (pohl2024adynamicbactofilin pages 2-3) | https://doi.org/10.7554/eLife.86577 (2024) | high | Bactofilin label-only; GO: peptidoglycan biosynthetic process | Slightly redundant with BacA/BacB→PbpC, but broader and independently stated. |
| Bactofilin polymers—act_as_barrier_retaining—cell wall biosynthetic machinery in growth zones | gene/protein/process | *Hyphomonas neptunium* | “bactofilin polymers localize dynamically to the stalk base and then to the incipient bud neck… acting as a barrier that retains the cell wall biosynthetic machinery in the respective growth zones” (pohl2024adynamicbactofilin pages 2-3) | https://doi.org/10.7554/eLife.86577 (2024) | high | GO: localization of cell wall synthesis machinery label-only; cellular component: stalk base, bud neck | Valuable for spatial-control subgraph; note organism uses reproductive stalk/bud cycle. |
| Loss of bactofilins—causes—unconstrained growth of stalk and bud compartments | gene/protein | *Hyphomonas neptunium* | “the lack of bactofilins causes severe morphological defects, resulting from unconstrained growth of the stalk and bud compartments” (pohl2024adynamicbactofilin pages 2-3) | https://doi.org/10.7554/eLife.86577 (2024) | high | METPO:1000695; GO: cell morphogenesis involved in differentiation | Strong phenotype edge; more about shape regulation than simple presence/absence of stalk. |
| LmdC—interacts_directly_with—bactofilin | gene/protein | *Hyphomonas neptunium*; conserved module in alphaproteobacteria | “LmdC, is an essential bitopic membrane protein with peptidoglycan hydrolase activity that interacts directly with bactofilin” (pohl2024adynamicbactofilin pages 2-3) | https://doi.org/10.7554/eLife.86577 (2024) | high | LmdC: M23 peptidase label-only; GO: peptidoglycan endopeptidase activity | Strong direct interaction edge; could support conserved submodule node. |
| LmdC depletion—causes—unconstrained cell growth | gene/protein | *Hyphomonas neptunium* | “Its CRISPRi-mediated depletion also results in unconstrained cell growth” (pohl2024adynamicbactofilin pages 2-3) | https://doi.org/10.7554/eLife.86577 (2024) | high | LmdC label-only; GO: regulation of cell morphogenesis | Supports role of hydrolase in constraining stalk/bud morphogenesis. |
| BacA—required_for_confined_localization_of—BacC | gene/protein | *Rhodomicrobium vannielii* | “Filamentous localization of mNeonGreen-BacC requires BacA” (richter2023interactingbactofilinsimpact pages 13-15) | https://doi.org/10.1371/journal.pgen.1010788 (2023) | high | BacA/BacC: label-only bactofilins; GO: protein localization | Strong localization dependency edge in hyphal prostheca system. |
| BacA localization—coincides_with—discrete PG incorporation at hyphal tips | gene/protein/process | *Rhodomicrobium vannielii* | “BacARvan localized to the hyphal tips and branching sites. This pattern coincides with discrete spots of PG incorporation at the hyphal tips” (richter2023interactingbactofilinsimpact pages 13-15) | https://doi.org/10.1371/journal.pgen.1010788 (2023) | medium | GO: peptidoglycan biosynthetic process; cellular component: hyphal tip label-only | Coincidence, not direct causation; curate as uncertain/spatial association unless stronger source added. |
| bacA deletion—causes—kinked/buckled hyphae | gene/protein | *Rhodomicrobium vannielii* | “the kinked hyphae of the R. vannielii bacA mutant still retain their length and thinness” (richter2023interactingbactofilinsimpact pages 13-15) | https://doi.org/10.1371/journal.pgen.1010788 (2023) | high | BacA label-only; GO: cell shape determination | Boundary case: reproductive hyphae rather than classical non-reproductive stalks; may belong in related but distinct trait graph. |
| NtrC loss of function—causes—elongated polar stalks | gene/protein/environment-regulatory | *Caulobacter crescentus* | “loss of NtrC function led to elongated polar stalks” (north2023thecaulobacterntrbntrc pages 1-2) | https://doi.org/10.1128/jb.00181-23 (2023) | high | NtrC: nitrogen response regulator label-only; GO: regulation of transcription, nitrogen utilization | Strong regulatory edge linking nutrient signaling to stalk morphology. |
| NtrC loss of function—causes—elevated synthesis of cell envelope polysaccharides | gene/protein/process | *Caulobacter crescentus* | “loss of NtrC function led to elongated polar stalks and elevated synthesis of cell envelope polysaccharides” (north2023thecaulobacterntrbntrc pages 1-2) | https://doi.org/10.1128/jb.00181-23 (2023) | high | NtrC label-only; GO: polysaccharide biosynthetic process | Could support separate envelope-polysaccharide node; relation to stalk elongation may be indirect. |


*Table: This table compiles curation-ready candidate causal edges for the METPO:1000695 tailed-shaped trait, emphasizing recent 2023–2024 evidence on stalk/prostheca morphogenesis. It is designed to support direct TraitMech YAML curation with edge direction, taxon scope, evidence snippets, and ontology suggestions.*

## 7) Visual evidence (figure support)

Barrows & Goley (2023) Figure 5 provides a compact schematic of **spatial regulation of morphogenesis** in *Caulobacter*, including a panel explicitly placing **bactofilin and MreB** at the **base of the stalk** where they recruit/regulate stalk elongation machinery—useful for anchoring the causal edges involving these proteins and the stalk base localization node. (barrows2023synchronizedswarmersand media 86ba8ef1, barrows2023synchronizedswarmersand media 7cd7048b)

## 8) Data/statistics from recent studies (extractable, trait-relevant)

* **Qualitative but explicit phenotypes:**
  * “absence … results in a decrease in stalk length” for BacA/B, PbpC, StpX; “depletion … results in a stalk elongation defect” for MreB/RodA. (barrows2023synchronizedswarmersand pages 11-13)
  * “pseudostalks … much shorter and wider … and irregularly shaped” upon loss of bactofilin topology control in *Asticcacaulis biprosthecum*. (pohl2024adynamicbactofilin pages 2-3)
  * “lack of bactofilins … unconstrained growth of the stalk and bud compartments” and LmdC depletion causing “unconstrained cell growth” in *H. neptunium*. (pohl2024adynamicbactofilin pages 2-3)
  * “loss of NtrC function led to elongated polar stalks” in *Caulobacter*. (north2023thecaulobacterntrbntrc pages 1-2)

These sources (as retrieved) did not provide consistent numeric distributions of stalk lengths in the quoted sections; if TraitMech requires quantitative thresholds (e.g., stalk length in μm under starvation), additional primary data extraction from the cited primary papers (e.g., Aaron et al. 2007; Randich & Brun 2015, referenced within the 2024 paper) would be needed. (pohl2024adynamicbactofilin pages 2-3)

## 9) Expert opinion / authoritative analysis (as statements in recent reviews)

* The 2023 *Journal of Bacteriology* minireview frames stalk morphogenesis as an emergent property of **combined regulation** across scaffolding proteins (bactofilins), PG synthases (MreB/RodA/PbpC), remodeling enzymes (DipM/SdpAB/CrbA), and diffusion barrier proteins (StpABCD), and emphasizes incomplete conservation across related taxa—supporting a curation approach that marks some edges as **clade-specific**. (barrows2023synchronizedswarmersand pages 11-13)

## 10) Warnings / curation pitfalls (do not curate without caution)

1. **Do not collapse “hyphae” into “stalks” without checking METPO intent.** Richter et al. explicitly separate prosthecae into stalks vs reproductive hyphae; hypha edges (e.g., *R. vannielii* bacA → kinked hyphae) may belong to a related-but-distinct trait graph (e.g., “hyphal/prosthecate reproductive appendage”). (richter2023interactingbactofilinsimpact pages 13-15)
2. **Pseudostalks are malformed outcomes.** Treat as boundary phenotypes; they support edges about spatial PG regulation but should not be curated as positive evidence for a normal “tailed shaped” trait state. (pohl2024adynamicbactofilin pages 2-3)
3. **Co-localization ≠ causation.** Edges such as “BacA localization coincides with PG incorporation” are supportive but should be marked **uncertain** unless backed by perturbation experiments explicitly changing PG incorporation patterns. (richter2023interactingbactofilinsimpact pages 13-15)
4. **Taxon portability is limited.** Several stalk genes are not well conserved outside *Caulobacter* (bacB, pbpC, stpX, stpABCD), so edges involving these should be tagged **taxon-specific** unless orthology evidence is added. (barrows2023synchronizedswarmersand pages 11-13)

---

# DOI-first bibliography (with dates/URLs)

1. Barrows JM, Goley ED. **Synchronized Swarmers and Sticky Stalks: *Caulobacter crescentus* as a Model for Bacterial Cell Biology.** *Journal of Bacteriology.* **2023-02**. DOI: 10.1128/jb.00384-22. URL: https://doi.org/10.1128/jb.00384-22 (barrows2023synchronizedswarmersand pages 5-7, barrows2023synchronizedswarmersand pages 11-13)
2. North H, McLaughlin M, Fiebig A, Crosson S. **The *Caulobacter* NtrB-NtrC two-component system bridges nitrogen assimilation and cell development.** *Journal of Bacteriology.* **2023-10**. DOI: 10.1128/jb.00181-23. URL: https://doi.org/10.1128/jb.00181-23 (north2023thecaulobacterntrbntrc pages 1-2)
3. Richter P, Melzer B, Müller FD. **Interacting bactofilins impact cell shape of the MreB-less multicellular *Rhodomicrobium vannielii*.** *PLOS Genetics.* **2023-05-31**. DOI: 10.1371/journal.pgen.1010788. URL: https://doi.org/10.1371/journal.pgen.1010788 (richter2023interactingbactofilinsimpact pages 13-15)
4. Pöhl S, Osorio-Valeriano M, Cserti E, et al. **A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis.** (eLife version via DOI). **2024-01 (as retrieved)**. DOI: 10.7554/eLife.86577.2. URL: https://doi.org/10.7554/eLife.86577.2 (pohl2024adynamicbactofilin pages 2-3)



References

1. (barrows2023synchronizedswarmersand pages 5-7): Jordan M. Barrows and Erin D. Goley. Synchronized swarmers and sticky stalks: caulobacter crescentus as a model for bacterial cell biology. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00384-22, doi:10.1128/jb.00384-22. This article has 59 citations and is from a peer-reviewed journal.

2. (barrows2023synchronizedswarmersand pages 11-13): Jordan M. Barrows and Erin D. Goley. Synchronized swarmers and sticky stalks: caulobacter crescentus as a model for bacterial cell biology. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00384-22, doi:10.1128/jb.00384-22. This article has 59 citations and is from a peer-reviewed journal.

3. (pohl2024adynamicbactofilin pages 2-3): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

4. (richter2023interactingbactofilinsimpact pages 13-15): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

5. (north2023thecaulobacterntrbntrc pages 1-2): Hunter North, Maeve McLaughlin, Aretha Fiebig, and Sean Crosson. The <i>caulobacter</i> ntrb-ntrc two-component system bridges nitrogen assimilation and cell development. Journal of Bacteriology, Oct 2023. URL: https://doi.org/10.1128/jb.00181-23, doi:10.1128/jb.00181-23. This article has 18 citations and is from a peer-reviewed journal.

6. (barrows2023synchronizedswarmersand media 86ba8ef1): Jordan M. Barrows and Erin D. Goley. Synchronized swarmers and sticky stalks: caulobacter crescentus as a model for bacterial cell biology. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00384-22, doi:10.1128/jb.00384-22. This article has 59 citations and is from a peer-reviewed journal.

7. (barrows2023synchronizedswarmersand media 7cd7048b): Jordan M. Barrows and Erin D. Goley. Synchronized swarmers and sticky stalks: caulobacter crescentus as a model for bacterial cell biology. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00384-22, doi:10.1128/jb.00384-22. This article has 59 citations and is from a peer-reviewed journal.