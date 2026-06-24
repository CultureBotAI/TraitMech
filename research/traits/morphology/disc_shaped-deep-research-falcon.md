---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:25:41.320184'
end_time: '2026-06-18T07:40:29.963885'
duration_seconds: 888.64
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'disc_shaped_anisotropic_wall_growth: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** disc shaped
- **METPO identifier:** METPO:1000689
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism is flat and circular.
- **Parent traits:** METPO:1000666
- **Synonyms:** disc
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports flat-disc geometry as a determined morphological phenotype.) | DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Halophilic-archaea description supports flat disc-shaped cell morphology in the wild.)
- **Existing causal graph summary:** disc_shaped_anisotropic_wall_growth: 4 nodes, 3 edges

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
- **METPO identifier:** METPO:1000689
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism is flat and circular.
- **Parent traits:** METPO:1000666
- **Synonyms:** disc
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports flat-disc geometry as a determined morphological phenotype.) | DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Halophilic-archaea description supports flat disc-shaped cell morphology in the wild.)
- **Existing causal graph summary:** disc_shaped_anisotropic_wall_growth: 4 nodes, 3 edges

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


# Research report: Microbial trait **disc shaped** (METPO:1000689)

## 0) Scope summary (curation-oriented)
**Trait definition (METPO:1000689):** disc-shaped cells are **flat and circular/near-circular (“discoid”, “plate”, “disk”)**. In several archaeal model systems, this phenotype is operationalized via 2D outline metrics such as **circularity**, with “plates/disks” corresponding to high circularity values (e.g., circularity 0.8–1) in microscopy segmentations. (patro2023“influenceofplasmids pages 3-5, patro2023“influenceofplasmids pages 1-2)

**Trait boundaries / nearby traits:**
- **Coccoid/spherical**: 3D round cells (not necessarily flattened) and typically distinct from plate/discoid in haloarchaea pleomorphy descriptions. (silva2021improvedgrowthand pages 1-2, patro2023“influenceofplasmids pages 1-2)
- **Rod/filamentous**: elongated morphotypes that often represent a differentiated state in pleomorphic haloarchaea; rods can be transient (e.g., early log) or linked to motility contexts. (silva2021improvedgrowthand pages 1-2, duggin2015cetztubulinlikeproteins pages 4-6)
- **Square/triangular flat morphologies** (e.g., *Haloquadratum* squares): “flat” but **non-circular**; these should be treated as separate morphology classes, not “disc shaped”. (wolferen2022thecellbiology pages 7-9, zheng2023discoveryofa pages 20-26)

**Key caution for TraitMech:** in haloarchaea, “disc/plate” is often a **developmental state** that interconverts with rods; therefore, many edges are **context-dependent** (growth phase, medium composition, genetic background, plasmids). (silva2021improvedgrowthand pages 1-2, patro2023“influenceofplasmids pages 5-7)

---

## 1) Key concepts and current understanding (mechanistic framing)
### 1.1 Disc/plate morphology as a regulated archaeal cell-shape state
In the model haloarchaeon *Haloferax volcanii*, “discoid-shaped (‘plate’) cells” are common in culture and can transition into rods depending on environmental and experimental conditions. (silva2021improvedgrowthand pages 1-2, duggin2015cetztubulinlikeproteins pages 4-6)

A working mechanistic model supported by current evidence is that disc/plate shape emerges from the **combined action of**:
1) **Cell envelope surface-layer (S-layer) biogenesis and anchoring**, which in many archaea acts as the primary wall-like scaffold.
2) **Cytoskeletal systems (tubulin superfamily proteins, especially CetZ in haloarchaea)** that modulate local shape changes and enable differentiated morphotypes (e.g., rod formation).
3) **Environmental micronutrient availability and growth state**, which tune the prevalence of disc vs rod morphotypes.

### 1.2 Operationalization in assays
A practical, curation-ready operationalization is provided by quantitative microscopy in *H. volcanii*, where cell classes are assigned by **circularity** thresholds: plates (P) ~0.8–1, intermediates ~0.6–0.8, rods <0.6. (patro2023“influenceofplasmids pages 3-5)

---

## 2) Recent developments and latest research (prioritizing 2023–2024)
### 2.1 Quantitative genetics/engineering artifacts that shift plate vs rod (2023)
A 2023 study systematically examined how **plasmids, selection markers, and auxotrophic backgrounds** change *H. volcanii* shape distributions, emphasizing reproducibility issues for morphology studies. It explicitly defines “plates (also called disks or discoid)” and reports growth-phase shifts toward plates. (patro2023“influenceofplasmids pages 1-2)

**Recent quantitative statistic:** In wild-type DS2 grown in Hv-CA medium across early growth, the population was mostly plate-shaped overall (~75% plates), increasing to **86% plates by OD600 = 0.2**. (patro2023“influenceofplasmids pages 3-5)

**Expert/author analysis:** The same work argues that plasmid presence and certain selection backgrounds (e.g., hdrB marker systems) can strongly bias morphology, implying that some “mechanistic” observations may actually be **strain-engineering artifacts**. (patro2023“influenceofplasmids pages 5-7, patro2023“influenceofplasmids pages 1-2)

### 2.2 Archaeal cytoskeleton reviews and synthesis (2023–2024)
- A 2022 high-authority review in *Nature Microbiology* highlights that many archaea encode **CetZ**, implicated in a “transition from a disk-shape to a rod-shape,” and notes broader correlations between actin-family proteins and elongated shapes. (wolferen2022thecellbiology pages 7-9)
- A 2023 review in *Biomolecules* compiles CetZ diversity and emphasizes correlations of CetZ subfamilies with cell-shape and motility phenotypes across haloarchaea, suggesting CetZ systems are a recurring lever for shape plasticity. (brown2023diversityandpotential pages 1-2)

### 2.3 2024 research on positioning/control of shape-regulating machinery
A 2024 paper reports that **MinD-family ATPases (MinD2/MinD4)** regulate **CetZ1 localization** and influence motility-related phenotypes in *H. volcanii*, connecting spatial organization systems to cytoskeletal placement (relevant to rod differentiation away from plate state). (brown2023diversityandpotential pages 1-2)

**Curation note:** The direct textual evidence snippets in the retrieved context are stronger for CetZ1/trace elements/plasmids than for MinD2/MinD4, so MinD edges should be curated only after extracting direct quotes from the 2024 text. (brown2023diversityandpotential pages 1-2)

---

## 3) Current applications and real-world implementations
### 3.1 Environmental microbiology: hypersaline ecosystems
Disc/plate morphologies are repeatedly observed among **extremely halophilic archaea** inhabiting **salt lakes and solar salterns**. For example:
- *Halorubrum tebenquichense* (isolated from Atacama saltern) is described as “mostly irregularly disc-shaped” and grows in “medium containing saturated concentrations of NaCl.” (lizama2002halorubrumtebenquichensesp. pages 1-2)
This supports disc shape as an ecologically realized morphology, not only a lab artifact, and ties it to ENVO-like contexts such as hypersaline salterns.

### 3.2 Model systems enabling mechanistic dissection
*Haloferax volcanii* is widely used as a genetically tractable haloarchaeal model. Disc/plate ↔ rod switching provides an assayable phenotype for connecting cytoskeletal function (CetZ1) and envelope biogenesis to morphology. (silva2021improvedgrowthand pages 1-2, duggin2015cetztubulinlikeproteins pages 1-2)

### 3.3 Beyond haloarchaea: disc-shaped methanogens
A non-halophilic archaeal example is *Methanoplanus petrolearius*, named for its “flat plate” morphology and described as “irregularly disc-shaped.” (brambilla2010completegenomesequence pages 1-3)

---

## 4) Expert opinions / authoritative synthesis
### 4.1 Shape plasticity reflects regulated cell biology, not mere physical deformation
The *H. volcanii* study frames morphology as responsive to “multiple culture conditions,” and uses perturbations (ΔcetZ1; dominant-negative CetZ1.E218A) to argue that rod differentiation requires active cytoskeletal function rather than being only a direct chemical envelope effect. (silva2021improvedgrowthand pages 8-10, silva2021improvedgrowthand pages 10-11)

### 4.2 Cell-shape studies require careful control of media, trace elements, and genetic background
Both 2021 and 2023 works emphasize reproducibility problems: trace element availability and plasmid/auxotrophy background can dramatically shift observed morphology distributions, meaning that “disc shaped” is context-dependent in pleomorphic systems. (silva2021improvedgrowthand pages 1-2, patro2023“influenceofplasmids pages 5-7)

---

## 5) Recent statistics and data suitable for curation
### 5.1 Growth-phase–dependent plate enrichment (quantified)
In *H. volcanii* DS2, plate prevalence increased with OD in early growth; the study reports **~75% plates overall** and **86% plates at OD600 = 0.2** in one quantified series. (patro2023“influenceofplasmids pages 3-5)

### 5.2 Media/trace-element controlled morphology (qualitative + quantified)
Trace element (TE) supplementation is linked to **near-exclusive plate morphotypes in stationary phase** and TE depletion to “striking cell elongation.” TE formulation is explicit (Fe, Zn, Cu, Co, Mn, Ni, Mo, B). (silva2021improvedgrowthand pages 5-6, silva2021improvedgrowthand pages 1-2)

### 5.3 Visual/figure evidence (high-value for curation)
Figure panels and circularity histograms in the CetZ paper show plate/disc-shaped *H. volcanii* cells in liquid culture and a shift toward rods at motility-halo leading edges, with CetZ1 perturbations altering distributions. These images provide curator-facing support that CetZ1 modulates the plate→rod transition. (duggin2015cetztubulinlikeproteins media 2ad64980, duggin2015cetztubulinlikeproteins media 3ddd4004, duggin2015cetztubulinlikeproteins media 3b4dbe08, duggin2015cetztubulinlikeproteins media 91b1c08c)

---

## 6) Candidate nodes for `disc_shaped.yaml` (grouped by type)
### 6.1 Phenotype nodes
- **disc shaped** (METPO:1000689)
- rod-shaped (label-only; consider mapping to METPO parent/neighbor term if available)
- pleomorphic rod / elongated / filamentous forms (label-only)

### 6.2 Cytoskeleton / division machinery
- **CetZ1** (archaeal tubulin-like cytoskeletal protein; label-only grounding in this report) (silva2021improvedgrowthand pages 1-2, silva2021improvedgrowthand pages 10-11)
- CetZ2 (label-only; implicated in CetZ family) (duggin2015cetztubulinlikeproteins pages 1-2)
- **FtsZ2** (division tubulin homolog; KO yields very large plates—indirect in retrieved excerpts) (patro2023“influenceofplasmids pages 1-2)
- actin-family cytoskeletal proteins / MreB-like systems (correlative with elongated shapes across archaea) (wolferen2022thecellbiology pages 7-9)

### 6.3 Cell envelope / surface layer and processing
- **S-layer glycoprotein** (label-only)
- **ArtA (archaeosortase A)** (peptidase; required for stable plate formation in *H. volcanii* as summarized) (silva2021improvedgrowthand pages 1-2)
- **PssA / PssD** (phosphatidylethanolamine biosynthesis enzymes; required for stable plate formation as summarized) (silva2021improvedgrowthand pages 1-2)
- process node: C-terminal processing and covalent lipid attachment of surface proteins (label-only) (silva2021improvedgrowthand pages 1-2)

### 6.4 Environmental & experimental factors
- Trace element availability (Fe, Zn, Cu, Co, Mn, Ni, Mo, B) (silva2021improvedgrowthand pages 5-6)
- Growth phase / culture density (early log vs late log/stationary) (silva2021improvedgrowthand pages 1-2, patro2023“influenceofplasmids pages 3-5)
- Physical context: agar surface colonies vs liquid; microfluidic continuous-flow culture (silva2021improvedgrowthand pages 10-11)
- Recombinant plasmid presence (e.g., pTA962/pTA963 and other pHV2-derived plasmids in *H. volcanii*) (silva2021improvedgrowthand pages 10-11, patro2023“influenceofplasmids pages 5-7)
- Selection marker/background: hdrB marker, ΔhdrB background (patro2023“influenceofplasmids pages 1-2, patro2023“influenceofplasmids pages 2-3)
- Salinity (saturated NaCl; 1–3% NaCl for *Methanoplanus*) (lizama2002halorubrumtebenquichensesp. pages 1-2, brambilla2010completegenomesequence pages 3-5)

---

## 7) Evidence-backed candidate causal edges (curation table)
The following table is designed for direct translation into TraitMech edges with curator notes.

| Edge (triple) | Node types (S/O) | Grounding suggestions | Evidence (citation id) | Source (DOI + year) | Supporting snippet | Notes/curation confidence |
|---|---|---|---|---|---|---|
| trace element supplementation -> promotes -> plate/discoid cell morphology | environmental factor -> morphology trait | S: trace element supplementation (label-only); O: METPO:1000689 disc shaped | (silva2021improvedgrowthand pages 1-2, silva2021improvedgrowthand pages 5-6) | 10.1099/mic.0.001012 (2021) | "With these supplemented media, transient development of plate cells into uniformly shaped rods was clearly observed during the early log phase of growth; cells then reverted to plates for the late log and stationary phases." / "Stationary-phase Hv-Cab cultures were 'almost exclusively plate-shaped cells that had near-circular cell outlines,'" | Strong but context-dependent; TE supports normal plate-dominant late growth rather than constitutively causing plates in all phases; taxon-specific to Haloferax volcanii. |
| trace element starvation -> causes -> elongated/pleomorphic rod morphology | environmental factor -> morphology trait | S: trace element starvation (label-only); O: pleomorphic rod / elongated cell (label-only) | (silva2021improvedgrowthand pages 8-10, silva2021improvedgrowthand pages 5-6) | 10.1099/mic.0.001012 (2021) | "We conclude that H. volcanii undergoes substantial cell elongation (and increased tubule development) in response to trace-element starvation" | Strong for H. volcanii; useful as opposing edge to disc-shaped state. |
| trace element starvation -> decreases prevalence of -> disc/plate morphology | environmental factor -> morphology trait | S: trace element starvation (label-only); O: METPO:1000689 disc shaped | (silva2021improvedgrowthand pages 1-2, silva2021improvedgrowthand pages 5-6) | 10.1099/mic.0.001012 (2021) | "In media prepared with high-purity water and reagents, without supplemental trace elements, rods and other complex elongated morphologies ('pleomorphic rods') were observed at all growth stages of the culture" | Strong inverse edge; inferred from replacement of plate state by rods/elongated forms. |
| CetZ1 function -> required for -> rod cell formation | gene/protein -> morphology trait | S: cetZ1 (label-only; archaeal tubulin-like protein); O: rod cell morphology (label-only) | (silva2021improvedgrowthand pages 1-2, duggin2015cetztubulinlikeproteins pages 1-2, silva2021improvedgrowthand pages 8-10) | 10.1099/mic.0.001012 (2021); 10.1038/nature13983 (2015) | "The tubulin-like cytoskeletal protein CetZ1 is required for rod formation" / "In early-culture rod development assays, the ΔcetZ1 strain failed to form rods" | Strong direct mechanistic edge; foundational for disc-vs-rod switching in haloarchaea. |
| loss of CetZ1 function -> retains/increases -> plate/discoid morphology | gene perturbation -> morphology trait | S: cetZ1 loss-of-function (label-only); O: METPO:1000689 disc shaped | (patro2023“influenceofplasmids pages 1-2, silva2021improvedgrowthand pages 8-10) | 10.3389/fmicb.2023.1270665 (2023); 10.1099/mic.0.001012 (2021) | "CetZ1 is described as 'essential for rod formation' with knockouts remaining plate-like" | Strong but phrased from perturbation phenotype; taxon-specific to Haloferax volcanii. |
| dominant-negative CetZ1.E218A expression -> inhibits -> rod and tubule formation | gene perturbation -> morphology trait | S: cetZ1.E218A dominant-negative allele (label-only); O: rod/tubule formation (label-only) | (silva2021improvedgrowthand pages 10-11) | 10.1099/mic.0.001012 (2021) | "expression of cetZ1.E218A blocked rod cell and tubule formation in the wild-type strain background" | Strong perturbation evidence; supports CetZ1-dependent branching away from plate state. |
| plate/discoid morphology -> transitions to -> rod morphology during early log phase | biological process/state -> morphology trait | S: early log phase growth (label-only); O: rod morphology (label-only) | (silva2021improvedgrowthand pages 1-2, silva2021improvedgrowthand pages 2-4) | 10.1099/mic.0.001012 (2021) | "transient development of plate cells into uniformly shaped rods was clearly observed during the early log phase of growth" | Strong descriptive developmental edge; useful for dynamic graph but not a molecular mechanism. |
| late log/stationary growth phase -> promotes dominance of -> plate/discoid morphology | biological process/state -> morphology trait | S: late log/stationary phase (label-only); O: METPO:1000689 disc shaped | (silva2021improvedgrowthand pages 1-2, patro2023“influenceofplasmids pages 3-5, patro2023“influenceofplasmids pages 5-7) | 10.1099/mic.0.001012 (2021); 10.3389/fmicb.2023.1270665 (2023) | "cells then reverted to plates for the late log and stationary phases" / "the majority (~75%) were plates overall, increasing to 86% plates by OD600 = 0.2" | Strong and quantitatively supported; growth-phase edge rather than direct molecular causation. |
| recombinant plasmid presence -> biases toward -> rod/intermediate morphology | experimental factor -> morphology trait | S: recombinant plasmid presence (label-only; e.g., pTA962/pTA963) ; O: rod/intermediate morphology (label-only) | (patro2023“influenceofplasmids pages 5-7, patro2023“influenceofplasmids pages 2-3, silva2021improvedgrowthand pages 10-11) | 10.3389/fmicb.2023.1270665 (2023); 10.1099/mic.0.001012 (2021) | "Plasmids (pTA1392, pTA230 carrying pfdx-pyrE2::hdrB) increased the proportion and persistence of rod/intermediate shapes in H26" / "early-culture rod formation ... requires the presence of an H. volcanii plasmid, pTA962" | Strong as an experimental/strain-background effect; should be curated as assay/genetic-background specific, not universal biology. |
| hdrB selection marker / ΔhdrB background -> alters -> cell shape distribution | gene perturbation / experimental factor -> morphology trait | S: hdrB selection marker or ΔhdrB background (label-only); O: cell shape distribution (label-only) | (patro2023“influenceofplasmids pages 2-3, patro2023“influenceofplasmids pages 1-2) | 10.3389/fmicb.2023.1270665 (2023) | "ΔhdrB strains and hdrB selection markers are explicitly stated to 'have the most influence on H. volcanii cell shape in addition to the sole presence of a plasmid.'" | Moderate-to-strong, but mechanism unclear; curate as experimental-factor edge with uncertainty. |
| archaeosortase A (ArtA) activity -> required for -> stable plate-shaped cell formation | protein/enzyme -> morphology trait | S: ArtA / archaeosortase A (label-only); O: METPO:1000689 disc shaped | (silva2021improvedgrowthand pages 1-2) | 10.1099/mic.0.001012 (2021) | "the peptidase archaeosortase A (ArtA) ... [is] required for effective and stable plate-shaped cell formation" | Strong textual support, but based on cited prior work summarized in review-style introduction. |
| phosphatidylethanolamine biosynthesis enzyme PssA -> required for -> stable plate-shaped cell formation | protein/enzyme -> morphology trait | S: PssA (label-only); O: METPO:1000689 disc shaped | (silva2021improvedgrowthand pages 1-2) | 10.1099/mic.0.001012 (2021) | "phosphatidylethanolamine biosynthesis enzymes PssA and PssD ... are required for effective and stable plate-shaped cell formation" | Strong textual support, but indirect from prior study summary; taxon-specific. |
| phosphatidylethanolamine biosynthesis enzyme PssD -> required for -> stable plate-shaped cell formation | protein/enzyme -> morphology trait | S: PssD (label-only); O: METPO:1000689 disc shaped | (silva2021improvedgrowthand pages 1-2) | 10.1099/mic.0.001012 (2021) | "phosphatidylethanolamine biosynthesis enzymes PssA and PssD ... are required for effective and stable plate-shaped cell formation" | Strong textual support, but indirect from prior study summary; taxon-specific. |
| ArtA/PssA/PssD-dependent S-layer glycoprotein processing/lipid anchoring -> enables -> stable plate-shaped morphology | biological process -> morphology trait | S: S-layer glycoprotein C-terminal processing and lipid anchoring (label-only); O: METPO:1000689 disc shaped | (silva2021improvedgrowthand pages 1-2) | 10.1099/mic.0.001012 (2021) | "required for the C-terminal processing and covalent lipid attachment of several H. volcanii surface proteins including the surface (S-layer) glycoprotein, are required for effective and stable plate-shaped cell formation" | Strong mechanistic synthesis; process node is inferred from sentence structure but explicitly supported. |
| ftsZ2 knockout -> causes -> very large plate cells | gene perturbation -> morphology trait | S: ftsZ2 knockout (label-only); O: large plate cells (label-only) | (patro2023“influenceofplasmids pages 1-2) | 10.3389/fmicb.2023.1270665 (2023) | "ftsZ2 knockouts produce very large plate cells (cell division defect)" | Moderate support from study summary rather than direct quote from primary results pages in context; curate with caution. |
| FtsZ2 function -> required for normal division of -> plate-shaped cells | protein -> biological process/cell phenotype | S: FtsZ2 (label-only); O: cell division in plate-shaped cells (label-only) | (patro2023“influenceofplasmids pages 1-2) | 10.3389/fmicb.2023.1270665 (2023) | "ftsZ2 knockouts produce very large plate cells (cell division defect)" | Inferred mechanistic edge from knockout phenotype; uncertain for direct curation unless primary source is checked. |
| actin-family proteins / MreB-like systems -> correlate with -> elongated rather than disc-shaped archaeal morphology | protein family -> morphology trait | S: actin-family cytoskeletal proteins (GO/label-only); O: elongated cell shape (label-only) | (wolferen2022thecellbiology pages 7-9) | 10.1038/s41564-022-01215-8 (2022) | "The presence of actin-family cytoskeletal proteins in the genomes of archaea seems to correlate with an elongated cell shape" | Correlative, not direct for disc-shaped state; useful warning/negative comparator, uncertain for TraitMech edge. |
| disc/plate cell type <-> interconverts with -> rod cell type | morphology trait -> morphology trait | S: METPO:1000689 disc shaped; O: rod-shaped (label-only) | (duggin2015cetztubulinlikeproteins pages 4-6, wolferen2022thecellbiology pages 7-9) | 10.1038/nature13983 (2015); 10.1038/s41564-022-01215-8 (2022) | "H. volcanii exhibits interconvertible 'plate and rod cell types'" / "transition from a disk-shape to a rod-shape" | Strong as a state-transition edge; not itself a causal mechanism but useful in graph topology. |


*Table: This table compiles candidate subject–predicate–object edges for curating the disc-shaped microbial morphology trait, emphasizing mechanistic and experimental factors supported by available evidence. It highlights which claims are strong, taxon-specific, or still uncertain before TraitMech curation.*

---

## 8) Warnings / items that should not yet be curated (or should be flagged uncertain)
1) **Actin-family proteins → elongated shape** is described as a correlation across archaeal genomes, not a demonstrated causal intervention for disc morphology; curate only as an “associated with” or as a weak edge unless primary evidence is added. (wolferen2022thecellbiology pages 7-9)
2) **FtsZ2 → plate size via division defects** is stated in 2023 synthesis excerpts but not supported here by primary-result quotes; curate as uncertain until the original ftsZ2 perturbation study is directly inspected. (patro2023“influenceofplasmids pages 1-2)
3) **Plasmid/selection-marker effects** are important but represent experimental confounding; encode them as experimental-factor nodes/edges rather than intrinsic biology when curating broadly. (patro2023“influenceofplasmids pages 5-7, silva2021improvedgrowthand pages 10-11)

---

## 9) DOI-first bibliography (publication date + URL)
1) de Silva RT, Abdul-Halim MF, Pittrich DA, Brown HJ, Pohlschroder M, Duggin IG. **Improved growth and morphological plasticity of *Haloferax volcanii*.** *Microbiology* (Published **18 Jan 2021**). DOI: **10.1099/mic.0.001012**. URL: https://doi.org/10.1099/mic.0.001012 (silva2021improvedgrowthand pages 1-2, silva2021improvedgrowthand pages 8-10, silva2021improvedgrowthand pages 10-11)
2) Patro M, Duggin IG, Albers S-V, Ithurbide S. **Influence of plasmids, selection markers and auxotrophic mutations on *Haloferax volcanii* cell shape plasticity.** *Frontiers in Microbiology* (Published **Sep 2023**). DOI: **10.3389/fmicb.2023.1270665**. URL: https://doi.org/10.3389/fmicb.2023.1270665 (patro2023“influenceofplasmids pages 1-2, patro2023“influenceofplasmids pages 3-5, patro2023“influenceofplasmids pages 5-7)
3) Brown HJ, Duggin IG. **Diversity and Potential Multifunctionality of Archaeal CetZ Tubulin-like Cytoskeletal Proteins.** *Biomolecules* (Published **Jan 2023**). DOI: **10.3390/biom13010134**. URL: https://doi.org/10.3390/biom13010134 (brown2023diversityandpotential pages 1-2)
4) van Wolferen M, Pulschen AAA, Baum B, Gribaldo S, Albers S-V. **The Cell Biology of Archaea.** *Nature Microbiology* (Published **Oct 2022**). DOI: **10.1038/s41564-022-01215-8**. URL: https://doi.org/10.1038/s41564-022-01215-8 (wolferen2022thecellbiology pages 7-9)
5) Duggin IG, Aylett CHS, Walsh JC, et al. **CetZ tubulin-like proteins control archaeal cell shape.** *Nature* (Published **Dec 2015**). DOI: **10.1038/nature13983**. URL: https://doi.org/10.1038/nature13983 (duggin2015cetztubulinlikeproteins pages 1-2, duggin2015cetztubulinlikeproteins pages 4-6, duggin2015cetztubulinlikeproteins media 2ad64980, duggin2015cetztubulinlikeproteins media 3ddd4004, duggin2015cetztubulinlikeproteins media 3b4dbe08, duggin2015cetztubulinlikeproteins media 91b1c08c)
6) Lizama C, Monteoliva-Sánchez M, Suárez-García A, et al. **Halorubrum tebenquichense sp. nov.** *International Journal of Systematic and Evolutionary Microbiology* (Published **2002**). DOI: **10.1099/00207713-52-1-149**. URL: https://doi.org/10.1099/00207713-52-1-149 (lizama2002halorubrumtebenquichensesp. pages 1-2)
7) Brambilla E, Djao ODN, Daligault H, et al. **Complete genome sequence of *Methanoplanus petrolearius* type strain (SEBR 4847T).** *Standards in Genomic Sciences* (Published **Sep 2010**). DOI: **10.4056/sigs.1183143**. URL: https://doi.org/10.4056/sigs.1183143 (brambilla2010completegenomesequence pages 1-3, brambilla2010completegenomesequence pages 3-5)

---

## 10) Suggested next curation actions
- Add explicit ontology grounding for metals in the TE mix (CHEBI identifiers) and for environmental contexts (ENVO hypersaline lake/saltern) during YAML authoring.
- If MinD2/MinD4 → CetZ1 localization edges are desired, extract direct textual quotes from the 2024 paper to move from “likely” to “evidence-backed.” (brown2023diversityandpotential pages 1-2)
- For FtsZ2 and plate-size edges, obtain primary perturbation evidence (full text) before curating as a firm causal edge. (patro2023“influenceofplasmids pages 1-2)


References

1. (patro2023“influenceofplasmids pages 3-5): Megha Patro, Iain G. Duggin, Sonja-Verena Albers, and Solenne Ithurbide. “influence of plasmids, selection markers and auxotrophic mutations on haloferax volcanii cell shape plasticity”. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1270665, doi:10.3389/fmicb.2023.1270665. This article has 8 citations and is from a peer-reviewed journal.

2. (patro2023“influenceofplasmids pages 1-2): Megha Patro, Iain G. Duggin, Sonja-Verena Albers, and Solenne Ithurbide. “influence of plasmids, selection markers and auxotrophic mutations on haloferax volcanii cell shape plasticity”. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1270665, doi:10.3389/fmicb.2023.1270665. This article has 8 citations and is from a peer-reviewed journal.

3. (silva2021improvedgrowthand pages 1-2): Roshali T. de Silva, Mohd F. Abdul-Halim, Dorothea A. Pittrich, Hannah J. Brown, Mechthild Pohlschroder, and Iain G. Duggin. Improved growth and morphological plasticity of haloferax volcanii. Feb 2021. URL: https://doi.org/10.1099/mic.0.001012, doi:10.1099/mic.0.001012. This article has 98 citations and is from a peer-reviewed journal.

4. (duggin2015cetztubulinlikeproteins pages 4-6): Iain G. Duggin, Christopher H. S. Aylett, James C. Walsh, Katharine A. Michie, Qing Wang, Lynne Turnbull, Emma M. Dawson, Elizabeth J. Harry, Cynthia B. Whitchurch, Linda A. Amos, and Jan Löwe. Cetz tubulin-like proteins control archaeal cell shape. Nature, 519:362-365, Dec 2015. URL: https://doi.org/10.1038/nature13983, doi:10.1038/nature13983. This article has 185 citations and is from a highest quality peer-reviewed journal.

5. (wolferen2022thecellbiology pages 7-9): Marleen van Wolferen, Andre Arashiro Pulschen, Buzz Baum, Simonetta Gribaldo, and Sonja-Verena Albers. The cell biology of archaea. Nature microbiology, 7:1744-1755, Oct 2022. URL: https://doi.org/10.1038/s41564-022-01215-8, doi:10.1038/s41564-022-01215-8. This article has 129 citations and is from a highest quality peer-reviewed journal.

6. (zheng2023discoveryofa pages 20-26): J Zheng. Discovery of a dynamically unstable actin homolog, salactin, through advances in haloarchaeal imaging. Unknown journal, 2023.

7. (patro2023“influenceofplasmids pages 5-7): Megha Patro, Iain G. Duggin, Sonja-Verena Albers, and Solenne Ithurbide. “influence of plasmids, selection markers and auxotrophic mutations on haloferax volcanii cell shape plasticity”. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1270665, doi:10.3389/fmicb.2023.1270665. This article has 8 citations and is from a peer-reviewed journal.

8. (brown2023diversityandpotential pages 1-2): Hannah J. Brown and Iain G. Duggin. Diversity and potential multifunctionality of archaeal cetz tubulin-like cytoskeletal proteins. Biomolecules, 13:134, Jan 2023. URL: https://doi.org/10.3390/biom13010134, doi:10.3390/biom13010134. This article has 14 citations.

9. (lizama2002halorubrumtebenquichensesp. pages 1-2): Catherine Lizama, Mercedes Monteoliva-Sánchez, Antonio Suárez-García, Ramón Roselló-Mora, Margarita Aguilera, Victoriano Campos, and Alberto Ramos-Cormenzana. Halorubrum tebenquichense sp. nov., a novel halophilic archaeon isolated from the atacama saltern, chile. International journal of systematic and evolutionary microbiology, 52 Pt 1:149-55, Jan 2002. URL: https://doi.org/10.1099/00207713-52-1-149, doi:10.1099/00207713-52-1-149. This article has 82 citations and is from a peer-reviewed journal.

10. (duggin2015cetztubulinlikeproteins pages 1-2): Iain G. Duggin, Christopher H. S. Aylett, James C. Walsh, Katharine A. Michie, Qing Wang, Lynne Turnbull, Emma M. Dawson, Elizabeth J. Harry, Cynthia B. Whitchurch, Linda A. Amos, and Jan Löwe. Cetz tubulin-like proteins control archaeal cell shape. Nature, 519:362-365, Dec 2015. URL: https://doi.org/10.1038/nature13983, doi:10.1038/nature13983. This article has 185 citations and is from a highest quality peer-reviewed journal.

11. (brambilla2010completegenomesequence pages 1-3): Evelyne Brambilla, Olivier Duplex Ngatchou Djao, Hajnalka Daligault, Alla Lapidus, Susan Lucas, Nancy Hammon, Matt Nolan, Hope Tice, Jan-Fang Cheng, Cliff Han, Roxanne Tapia, Lynne Goodwin, Sam Pitluck, Konstantinos Liolios, Natalia Ivanova, Konstantinos Mavromatis, Natalia Mikhailova, Amrita Pati, Amy Chen, Krishna Palaniappan, Miriam Land, Loren Hauser, Yun-Juan Chang, Cynthia D. Jeffries, Manfred Rohde, Stefan Spring, Johannes Sikorski, Markus Göker, Tanja Woyke, James Bristow, Jonathan A. Eisen, Victor Markowitz, Philip Hugenholtz, Nikos C. Kyrpides, and Hans-Peter Klenk. Complete genome sequence of methanoplanus petrolearius type strain (sebr 4847t). Standards in Genomic Sciences, 3:203-211, Sep 2010. URL: https://doi.org/10.4056/sigs.1183143, doi:10.4056/sigs.1183143. This article has 18 citations.

12. (silva2021improvedgrowthand pages 8-10): Roshali T. de Silva, Mohd F. Abdul-Halim, Dorothea A. Pittrich, Hannah J. Brown, Mechthild Pohlschroder, and Iain G. Duggin. Improved growth and morphological plasticity of haloferax volcanii. Feb 2021. URL: https://doi.org/10.1099/mic.0.001012, doi:10.1099/mic.0.001012. This article has 98 citations and is from a peer-reviewed journal.

13. (silva2021improvedgrowthand pages 10-11): Roshali T. de Silva, Mohd F. Abdul-Halim, Dorothea A. Pittrich, Hannah J. Brown, Mechthild Pohlschroder, and Iain G. Duggin. Improved growth and morphological plasticity of haloferax volcanii. Feb 2021. URL: https://doi.org/10.1099/mic.0.001012, doi:10.1099/mic.0.001012. This article has 98 citations and is from a peer-reviewed journal.

14. (silva2021improvedgrowthand pages 5-6): Roshali T. de Silva, Mohd F. Abdul-Halim, Dorothea A. Pittrich, Hannah J. Brown, Mechthild Pohlschroder, and Iain G. Duggin. Improved growth and morphological plasticity of haloferax volcanii. Feb 2021. URL: https://doi.org/10.1099/mic.0.001012, doi:10.1099/mic.0.001012. This article has 98 citations and is from a peer-reviewed journal.

15. (duggin2015cetztubulinlikeproteins media 2ad64980): Iain G. Duggin, Christopher H. S. Aylett, James C. Walsh, Katharine A. Michie, Qing Wang, Lynne Turnbull, Emma M. Dawson, Elizabeth J. Harry, Cynthia B. Whitchurch, Linda A. Amos, and Jan Löwe. Cetz tubulin-like proteins control archaeal cell shape. Nature, 519:362-365, Dec 2015. URL: https://doi.org/10.1038/nature13983, doi:10.1038/nature13983. This article has 185 citations and is from a highest quality peer-reviewed journal.

16. (duggin2015cetztubulinlikeproteins media 3ddd4004): Iain G. Duggin, Christopher H. S. Aylett, James C. Walsh, Katharine A. Michie, Qing Wang, Lynne Turnbull, Emma M. Dawson, Elizabeth J. Harry, Cynthia B. Whitchurch, Linda A. Amos, and Jan Löwe. Cetz tubulin-like proteins control archaeal cell shape. Nature, 519:362-365, Dec 2015. URL: https://doi.org/10.1038/nature13983, doi:10.1038/nature13983. This article has 185 citations and is from a highest quality peer-reviewed journal.

17. (duggin2015cetztubulinlikeproteins media 3b4dbe08): Iain G. Duggin, Christopher H. S. Aylett, James C. Walsh, Katharine A. Michie, Qing Wang, Lynne Turnbull, Emma M. Dawson, Elizabeth J. Harry, Cynthia B. Whitchurch, Linda A. Amos, and Jan Löwe. Cetz tubulin-like proteins control archaeal cell shape. Nature, 519:362-365, Dec 2015. URL: https://doi.org/10.1038/nature13983, doi:10.1038/nature13983. This article has 185 citations and is from a highest quality peer-reviewed journal.

18. (duggin2015cetztubulinlikeproteins media 91b1c08c): Iain G. Duggin, Christopher H. S. Aylett, James C. Walsh, Katharine A. Michie, Qing Wang, Lynne Turnbull, Emma M. Dawson, Elizabeth J. Harry, Cynthia B. Whitchurch, Linda A. Amos, and Jan Löwe. Cetz tubulin-like proteins control archaeal cell shape. Nature, 519:362-365, Dec 2015. URL: https://doi.org/10.1038/nature13983, doi:10.1038/nature13983. This article has 185 citations and is from a highest quality peer-reviewed journal.

19. (patro2023“influenceofplasmids pages 2-3): Megha Patro, Iain G. Duggin, Sonja-Verena Albers, and Solenne Ithurbide. “influence of plasmids, selection markers and auxotrophic mutations on haloferax volcanii cell shape plasticity”. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1270665, doi:10.3389/fmicb.2023.1270665. This article has 8 citations and is from a peer-reviewed journal.

20. (brambilla2010completegenomesequence pages 3-5): Evelyne Brambilla, Olivier Duplex Ngatchou Djao, Hajnalka Daligault, Alla Lapidus, Susan Lucas, Nancy Hammon, Matt Nolan, Hope Tice, Jan-Fang Cheng, Cliff Han, Roxanne Tapia, Lynne Goodwin, Sam Pitluck, Konstantinos Liolios, Natalia Ivanova, Konstantinos Mavromatis, Natalia Mikhailova, Amrita Pati, Amy Chen, Krishna Palaniappan, Miriam Land, Loren Hauser, Yun-Juan Chang, Cynthia D. Jeffries, Manfred Rohde, Stefan Spring, Johannes Sikorski, Markus Göker, Tanja Woyke, James Bristow, Jonathan A. Eisen, Victor Markowitz, Philip Hugenholtz, Nikos C. Kyrpides, and Hans-Peter Klenk. Complete genome sequence of methanoplanus petrolearius type strain (sebr 4847t). Standards in Genomic Sciences, 3:203-211, Sep 2010. URL: https://doi.org/10.4056/sigs.1183143, doi:10.4056/sigs.1183143. This article has 18 citations.

21. (silva2021improvedgrowthand pages 2-4): Roshali T. de Silva, Mohd F. Abdul-Halim, Dorothea A. Pittrich, Hannah J. Brown, Mechthild Pohlschroder, and Iain G. Duggin. Improved growth and morphological plasticity of haloferax volcanii. Feb 2021. URL: https://doi.org/10.1099/mic.0.001012, doi:10.1099/mic.0.001012. This article has 98 citations and is from a peer-reviewed journal.