---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:42:07.686063'
end_time: '2026-06-18T07:56:05.550102'
duration_seconds: 837.86
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: flask shaped
  trait_identifier: METPO:1000675
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: flask_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a bulbous body with a narrower
    neck-like extension at one pole.
  parent_traits: METPO:1000666
  synonyms: flask, flask-shaped
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape
    review supports polarized peptidoglycan growth as a mechanism producing asymmetric
    flask-like morphology.)'
  causal_graph_summary: 'flask_shaped_asymmetric_polar_growth: 4 nodes, 3 edges'
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
- **Trait label:** flask shaped
- **METPO identifier:** METPO:1000675
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bulbous body with a narrower neck-like extension at one pole.
- **Parent traits:** METPO:1000666
- **Synonyms:** flask, flask-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports polarized peptidoglycan growth as a mechanism producing asymmetric flask-like morphology.)
- **Existing causal graph summary:** flask_shaped_asymmetric_polar_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **flask shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flask_shaped.yaml`.

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
- **Trait label:** flask shaped
- **METPO identifier:** METPO:1000675
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bulbous body with a narrower neck-like extension at one pole.
- **Parent traits:** METPO:1000666
- **Synonyms:** flask, flask-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports polarized peptidoglycan growth as a mechanism producing asymmetric flask-like morphology.)
- **Existing causal graph summary:** flask_shaped_asymmetric_polar_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **flask shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flask_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: *flask shaped* (METPO:1000675)

### Executive scope summary
**Trait definition (given):** “A cell shape in which an organism has a bulbous body with a narrower neck-like extension at one pole.” (METPO:1000675).  
**Current mechanistic understanding:** The literature supports at least two mechanistic “routes” to a flask-like outline:  
1) **Wall-less Mollicutes (e.g., *Mycoplasma*)**: the “neck” corresponds to a **polar protrusion called the attachment/terminal organelle**, which both defines the bottle/flask outline and confers polarized host interaction and gliding. *M. genitalium* is explicitly described as bottle/flask-shaped due to attachment-organelle protrusion. (chen2025unravelingtherole pages 4-7, chen2025unravelingtherole media b5911218)  
2) **Walled bacteria with polar/zonal envelope growth (prosthecae/stalks/budding forms)**: a bulb+neck-like geometry can arise by **zonal peptidoglycan (PG) insertion** restricted to a pole or a neck region, often organized by scaffolds (e.g., bactofilins) and coordinated PG synthase/hydrolase modules. (kysela2016diversitytakesshape pages 5-7, pohl2024adynamicbactofilin pages 1-2)

**Boundary cases to distinguish in curation:**  
- **Curved/helical cells** (shape due to asymmetric sidewall growth or curvature modules) are not necessarily flask-shaped unless there is a clear bulb+neck pole asymmetry (e.g., curvature scaffolds are relevant but not sufficient). (kysela2016diversitytakesshape pages 5-7)  
- **Prosthecate/stalked** cells can resemble “flask shaped” when the stalk is short relative to the cell body; otherwise they may be better represented as “stalked/prosthecate” traits, with mechanistic overlap (polar PG insertion). (kysela2016diversitytakesshape pages 5-7)  
- **Budding/hyphal/filamentous appendages** can include a neck-like constriction but often involve multi-compartment development; only curate to “flask shaped” if the primary observation is a single cell body with a single polar neck. (pohl2024adynamicbactofilin pages 1-2, richter2023interactingbactofilinsimpact pages 1-2)

---

## 1) Key concepts and definitions (current understanding)

### A. Trait as an observable morphological class
- **Operational phenotype:** microscopy-observed **asymmetric cell outline** with (i) a broader body and (ii) a narrower polar extension/neck. This can be a stable morphology (genetically encoded) or conditionally variable (plastic). (schwab2022characterizationofputative pages 7-10, schwab2022characterizationofputative pages 1-7)

### B. Two major mechanistic concept families relevant to causal graphs
1) **Polar organelle protrusion (wall-less bacteria)**  
   In *Mycoplasma genitalium* relatives, the cell is described as **“bottle-shaped”** (functionally equivalent to the METPO flask description) and this shape **“arises from the protrusion of the attachment organelle.”** (chen2025unravelingtherole pages 4-7, chen2025unravelingtherole media b5911218)

2) **Polar/zonal cell-wall growth and remodeling (walled bacteria)**  
   Reviews of bacterial morphogenesis emphasize that **spatially restricted (“zonal”) PG synthesis** at poles can produce polar extensions such as prosthecae/stalks, and that repositioning of growth zones changes appendage placement and morphology. (kysela2016diversitytakesshape pages 5-7)

---

## 2) Recent developments and latest research (prioritize 2023–2024)

### A. 2023–2024: Cytoskeletal scaffolds + PG hydrolase modules as “shape-determining units”
A key 2023 preprint and its 2024 published/updated form identify a conserved morphogenetic module in morphologically complex Alphaproteobacteria:
- **Bactofilin polymers** localize to **stalk base and bud neck**, and their absence leads to **“unconstrained growth”** of these compartments—directly linking a scaffold to spatial restriction of envelope growth zones. (pohl2024adynamicbactofilin pages 1-2)  
- Bactofilins are functionally coupled to an **M23-family endopeptidase (LmdC)**; **LmdC interacts directly with bactofilin in vitro** and is required for normal morphology, supporting scaffold–hydrolase coupling that modifies local PG insertion/remodeling at neck-like sites. (pohl2024adynamicbactofilin pages 1-2)

These papers provide curation-ready mechanistic entities for edges that generalize to flask-like morphologies in walled organisms where a polar neck is produced by localized wall growth. (pohl2024adynamicbactofilin pages 19-21)

### B. 2024: Comparative “plasticity” framing for localization of PG synthesis
A 2024 preprint (and later 2025 publication) emphasizes that even closely related bacteria can use distinct combinations of dispersed/midcell/polar growth and that **localization of PG synthases (e.g., PBP2) correlates with elongation mode**. This supports causal-graph nodes for **enzyme localization** and **growth zone placement** as mechanistic intermediates connecting genotype → growth mode → morphology. (delaby2024phenotypicplasticityin pages 35-38, delaby2025phenotypicplasticityin pages 10-10)

---

## 3) Current applications and real-world implementations

### A. Host interaction and pathogenicity relevance (Mycoplasma)
“Flask-shaped cells with an attachment organelle” are linked to **polar adhesion to host cells** and **unidirectional gliding motility**, and in some cases contribute to division—connecting morphology to clinically relevant behaviors such as adherence and motility. (schwab2022characterizationofputative pages 7-10, schwab2022characterizationofputativea pages 7-10)

### B. Morphogenesis modules as targets or design elements (general)
The PG-growth-zone concept and cytoskeletal scaffolding modules are frequently discussed as central to bacterial shape determination; by analogy, interventions that disrupt coordination between localized PG synthesis and hydrolases can have strong morphological consequences (e.g., loss of rod shape or altered polar structures), motivating use in **antimicrobial target discovery** and **synthetic control of morphology** (conceptually supported by the importance of coordinated PG synthesis/remodeling for maintaining shape). (kysela2016diversitytakesshape pages 5-7)

---

## 4) Expert opinions and analysis (authoritative sources)

### A. Review-level synthesis: spatial regulation of PG synthesis as a primary shape determinant
Kysela et al. (PLOS Biology) synthesize a broad view that **where** PG is inserted (lateral vs medial vs polar, and how zones move) governs morphology, including prosthecate and branched forms, with scaffolds providing structural constraints. This framework supports curating “growth zone placement” and “localized PG insertion” as core causal intermediates for any flask-like polar extension in walled microbes. (kysela2016diversitytakesshape pages 5-7)

### B. Module concept: scaffold–hydrolase coupling as a conserved driver of complex shapes
Pöhl et al. argue that **bactofilins and M23 peptidases form a conserved functional module** that creates **local changes in cell wall biosynthesis**, supporting a reusable mechanistic subgraph for polar neck/outgrowth formation in multiple lineages. (pohl2024adynamicbactofilin pages 1-2)

---

## 5) Relevant statistics and data from recent studies

### Quantitative structural dimensions (Mycoplasma attachment organelle architecture)
Chen et al. provide nanometer-scale dimensions for core attachment-organelle substructures in the schematic comparison (terminal button, paired plates/rod, bowl/wheel complex). The figure includes labeled values **53 nm (terminal button), 212 nm (paired plates), and 51 nm (bowl complex)**, and the same work connects bottle/flask shape to attachment organelle protrusion. (chen2025unravelingtherole pages 4-7, chen2025unravelingtherole media b5911218)

**Visual evidence:** the paper contains a figure explicitly illustrating the bottle/flask-shaped *M. genitalium* morphology and attachment organelle, and a schematic of the internal architecture with labeled dimensions. (chen2025unravelingtherole media b5911218, chen2025unravelingtherole media e3717844)

---

## TraitMech curation content

### A. Candidate nodes grouped by type (with grounding suggestions)

#### Phenotype / trait node
- **flask shaped** — METPO:1000675 (given)

#### Cellular structures / localization
- **polar neck-like extension** (label-only; maps to pole-associated protrusion)
- **attachment organelle / terminal organelle (Mycoplasma)** (label-only; concept is explicitly used) (chen2025unravelingtherole pages 4-7, schwab2022characterizationofputative pages 7-10)
- **terminal button** (label-only structural subpart) (chen2025unravelingtherole pages 4-7)
- **rod / paired plates** (label-only structural subpart) (chen2025unravelingtherole pages 4-7)
- **wheel / bowl complex** (label-only structural subpart) (chen2025unravelingtherole pages 4-7)
- **stalk base / bud neck** (label-only locations for polar growth control in stalked budding bacteria) (pohl2024adynamicbactofilin pages 1-2)

#### Biological processes (suggest GO grounding where appropriate)
- **polar growth / unipolar growth** (label-only; GO mapping unclear from provided evidence)
- **peptidoglycan biosynthetic process** — GO:0009252 (candidate) (supported conceptually by polar PG insertion framework) (kysela2016diversitytakesshape pages 5-7)
- **peptidoglycan catabolic process / remodeling** — GO:0009253 (candidate) (pohl2024adynamicbactofilin pages 1-2)
- **cell adhesion** — GO:0007155 (candidate) (polar adhesion) (schwab2022characterizationofputative pages 7-10)
- **gliding motility** (label-only; GO term exists but not grounded in evidence text) (schwab2022characterizationofputative pages 7-10)

#### Genes / proteins (with suggested identifiers)
**Mycoplasma genitalium attachment-organelle proteins (from Chen 2025):**  
- MG217, MG317 (terminal button proteins) (chen2025unravelingtherole pages 4-7)  
- MG312, MG218 (rod proteins) (chen2025unravelingtherole pages 4-7)  
- MG491, MG386, MG269, MG200 (wheel complex proteins) (chen2025unravelingtherole pages 4-7)  
*(Grounding suggestion: UniProt IDs likely exist but are not provided in evidence; curate as locus tags unless resolved.)*

**Walled bacteria polar growth scaffolds/remodelers (from Pöhl 2023/2024 and reviews):**  
- **Bactofilin (e.g., BacA)** (protein family; grounding requires organism-specific UniProt) (pohl2024adynamicbactofilin pages 1-2)  
- **LmdC (M23 endopeptidase)** (M23-family PG hydrolase; EC/UniProt not provided) (pohl2024adynamicbactofilin pages 1-2)  
- **PBP2** (penicillin-binding protein 2; bPBP; likely UniProt/EC not provided) (delaby2025phenotypicplasticityin pages 1-2, delaby2025phenotypicplasticityin pages 10-10)

#### Chemicals / inhibitors (optional candidate nodes)
- None were directly evidenced in a flask-shape context within the retrieved excerpts.

#### Environmental / experimental factors
- **host cell contact / host environment** (shape changes prior to invasion; relevant to *Mycoplasma* plasticity) (schwab2022characterizationofputative pages 1-7)
- **intracellular metabolite levels** (shape plasticity described as metabolite-induced, requiring metabolic activity) (schwab2022characterizationofputative pages 1-7)

---

### B. Candidate evidence-backed causal edges (curation table)
The following table lists candidate subject–predicate–object triples with evidence snippets, sources, and notes for curation.

| Edge (triple) | Mechanistic rationale | Evidence snippet (short quote) | Source (DOI/URL, year) | Strength/notes |
|---|---|---|---|---|
| attachment organelle — contributes_to — flask-shaped cell morphology | In Mycoplasma, the narrow polar extension is the protruding attachment organelle, producing a bottle/flask outline. | “M. genitalium has a ‘bottle-shaped’… morphology that arises from the protrusion of the attachment organelle.” (chen2025unravelingtherole pages 4-7, chen2025unravelingtherole media b5911218) | Chen et al. 2025. https://doi.org/10.1186/s12866-025-04320-w (2025) | Strong for Mycoplasma; taxon-specific morphology mechanism. |
| attachment organelle — confers — polar adhesion to host cells | The defining neck-like pole in flask-shaped mycoplasmas is functionally specialized for attachment. | “flask-shaped cells with an attachment organelle, which confers polar adhesion to host cells” (schwab2022characterizationofputative pages 7-10, schwab2022characterizationofputativea pages 7-10) | Schwab 2022. Dissertation/unknown journal (2022) | Moderate; descriptive source, but directly links flask shape to organelle function. |
| attachment organelle — enables — unidirectional gliding motility | Polarized organelle function supports asymmetric morphology and movement from one pole. | “confers polar adhesion to host cells and unidirectional gliding motility” (schwab2022characterizationofputative pages 7-10, schwab2022characterizationofputativea pages 7-10) | Schwab 2022. Dissertation/unknown journal (2022) | Moderate; useful functional edge for phenotype context. |
| attachment organelle — may_contribute_to — cell division | Some flask-shaped mycoplasmas use the polar organelle in division, linking morphology to cell cycle organization. | “and, in some cases, contributes to cell division” (schwab2022characterizationofputative pages 7-10, schwab2022characterizationofputativea pages 7-10) | Schwab 2022. Dissertation/unknown journal (2022) | Uncertain; explicitly qualified as “in some cases.” |
| terminal button protein MG217 — part_of — attachment organelle cytoskeleton | Organellar substructures provide the scaffold underlying the flask/bottle neck. | “terminal button proteins MG217 and MG317” (chen2025unravelingtherole pages 4-7) | Chen et al. 2025. https://doi.org/10.1186/s12866-025-04320-w (2025) | Strong structural part-of edge; taxon-specific to M. genitalium. |
| terminal button protein MG317 — part_of — attachment organelle cytoskeleton | Same as above; component grounding for mechanistic node set. | “terminal button proteins MG217 and MG317” (chen2025unravelingtherole pages 4-7) | Chen et al. 2025. https://doi.org/10.1186/s12866-025-04320-w (2025) | Strong structural edge; taxon-specific. |
| rod protein MG312 — part_of — attachment organelle cytoskeleton | Rod/paired-plate core helps create the elongated neck-like extension. | “rod proteins MG312 and MG218” (chen2025unravelingtherole pages 4-7) | Chen et al. 2025. https://doi.org/10.1186/s12866-025-04320-w (2025) | Strong structural edge; taxon-specific. |
| rod protein MG218 — part_of — attachment organelle cytoskeleton | Same rationale; supports curation of organelle submodule. | “rod proteins MG312 and MG218” (chen2025unravelingtherole pages 4-7) | Chen et al. 2025. https://doi.org/10.1186/s12866-025-04320-w (2025) | Strong structural edge; taxon-specific. |
| wheel-complex protein MG491 — part_of — attachment organelle cytoskeleton | Wheel/bowl complex is a core architectural element associated with the protrusion. | “wheel-complex proteins MG491, MG386, MG269, and MG200” (chen2025unravelingtherole pages 4-7) | Chen et al. 2025. https://doi.org/10.1186/s12866-025-04320-w (2025) | Strong structural edge; taxon-specific. |
| wheel-complex protein MG386 — part_of — attachment organelle cytoskeleton | Same as above. | “wheel-complex proteins MG491, MG386, MG269, and MG200” (chen2025unravelingtherole pages 4-7) | Chen et al. 2025. https://doi.org/10.1186/s12866-025-04320-w (2025) | Strong structural edge; taxon-specific. |
| wheel-complex protein MG269 — part_of — attachment organelle cytoskeleton | Same as above. | “wheel-complex proteins MG491, MG386, MG269, and MG200” (chen2025unravelingtherole pages 4-7) | Chen et al. 2025. https://doi.org/10.1186/s12866-025-04320-w (2025) | Strong structural edge; taxon-specific. |
| wheel-complex protein MG200 — part_of — attachment organelle cytoskeleton | Same as above. | “wheel-complex proteins MG491, MG386, MG269, and MG200” (chen2025unravelingtherole pages 4-7) | Chen et al. 2025. https://doi.org/10.1186/s12866-025-04320-w (2025) | Strong structural edge; taxon-specific. |
| zonal polar peptidoglycan synthesis — produces — prostheca/stalk outgrowth | Polarized cell-wall insertion is a general mechanism for asymmetric bulb-plus-neck morphologies. | “the Caulobacter prostheca arises from zonal growth at the pole” (kysela2016diversitytakesshape pages 5-7) | Kysela et al. 2016. https://doi.org/10.1371/journal.pbio.1002565 (2016) | Strong review-level mechanistic generalization; supports inferred flask-shape graph. |
| repositioning of polar PG growth zones — alters — appendage position/shape | Moving the localized growth zone changes where neck-like extensions form. | “Asticcacaulis prosthecate variants result from repositioning growth zones to subpolar/bilateral sites” (kysela2016diversitytakesshape pages 5-7) | Kysela et al. 2016. https://doi.org/10.1371/journal.pbio.1002565 (2016) | Moderate; not flask-specific but highly relevant boundary mechanism. |
| bactofilin polymers — localize_to — stalk base and bud neck | Spatially restricted scaffold marks the exact growth zones that generate asymmetric necked morphologies. | “bactofilin polymers localize dynamically to the stalk base and the bud neck” (pohl2024adynamicbactofilin pages 1-2) | Pöhl et al. 2024. https://doi.org/10.7554/elife.86577.2 (2024) | Strong for Hyphomonas; direct localization evidence. |
| bactofilin cytoskeleton — constrains — growth of stalk and bud compartments | Loss-of-function phenotype shows scaffold is needed to prevent uncontrolled asymmetric outgrowth. | “their loss causes ‘unconstrained growth of the stalk and bud compartments’” (pohl2024adynamicbactofilin pages 1-2) | Pöhl et al. 2024. https://doi.org/10.7554/elife.86577.2 (2024) | Strong genetic evidence; not named as flask-shaped but highly analogous. |
| LmdC (M23 endopeptidase) — interacts_with — bactofilin | PG hydrolase plus scaffold likely remodel local wall geometry at neck/stalk zones. | “the H. neptunium M23 homolog LmdC interacts directly with bactofilin in vitro” (pohl2024adynamicbactofilin pages 1-2) | Pöhl et al. 2024. https://doi.org/10.7554/elife.86577.2 (2024) | Strong interaction edge; species-specific. |
| bactofilin–LmdC module — promotes_local_changes_in — cell wall biosynthesis | Combined scaffold/hydrolase module is proposed as a conserved morphogenetic unit for complex shapes. | “bactofilins and M23 peptidases form a conserved functional module that promotes local changes in the mode of cell wall biosynthesis” (pohl2024adynamicbactofilin pages 1-2) | Pöhl et al. 2024. https://doi.org/10.7554/elife.86577.2 (2024) | Strong for complex alphaproteobacterial morphogenesis; inferred extension to flask-shaped trait. |


*Table: This table compiles curation-ready subject–predicate–object edges for the microbial trait 'flask shaped' (METPO:1000675), emphasizing direct evidence for attachment-organelle-based flask morphology in Mycoplasma and inferred polar-growth/PG-remodeling mechanisms from stalked budding alphaproteobacteria.*

---

## Warnings / claims to treat as uncertain prior to TraitMech curation
1) **“Flask-shaped” vs “bottle-shaped” equivalence:** The Chen et al. paper uses “bottle-shaped” for *M. genitalium*; this is likely congruent with METPO’s flask-shaped definition, but curators should confirm terminological equivalence in the target ontology usage notes. (chen2025unravelingtherole pages 4-7)
2) **Cell division involvement of the attachment organelle:** Schwab states the organelle contributes to division “in some cases,” which is explicitly qualified and should be curated as uncertain/taxon-dependent unless corroborated with primary experimental evidence. (schwab2022characterizationofputative pages 7-10)
3) **Generalizing stalk/bud polar PG modules to flask-shaped trait:** Bactofilin–LmdC evidence is strong for stalked/budding morphogenesis, but mapping it directly onto “flask shaped” is an inference that depends on whether the flask phenotype in a given taxon is indeed a polar envelope outgrowth rather than an organelle protrusion in wall-less bacteria. Curate as a conditional mechanism path. (pohl2024adynamicbactofilin pages 1-2)
4) **Missing 2023–2024 primary reviews explicitly naming “flask shaped” in bacteria:** Within the retrieved set, the most direct flask-shape mechanism evidence is Mycoplasma-focused and/or older review-level. A dedicated 2023–2024 bacterial morphology review explicitly anchoring “flask shaped” as a term across taxa was not retrieved here.

---

## DOI-first bibliography (with URLs and publication dates)

1) **Pöhl S. et al.** *A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis.* eLife version via DOI **10.7554/eLife.86577.2** (posted Jan 2024). https://doi.org/10.7554/elife.86577.2 (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 19-21)  
2) **Richter P. et al.** *Interacting bactofilins impact cell shape of the MreB-less multicellular Rhodomicrobium vannielii.* PLOS Genetics (May 2023). DOI: **10.1371/journal.pgen.1010788**. https://doi.org/10.1371/journal.pgen.1010788 (richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 26-27, richter2023interactingbactofilinsimpact pages 15-16)  
3) **Kysela DT. et al.** *Diversity Takes Shape: Understanding the Mechanistic and Adaptive Basis of Bacterial Morphology.* PLOS Biology (Oct 2016). DOI: **10.1371/journal.pbio.1002565**. https://doi.org/10.1371/journal.pbio.1002565 (kysela2016diversitytakesshape pages 5-7)  
4) **Schwab N.** *Characterization of Putative Virulence-Associated Traits in Mycoplasma penetrans Using Clinical Isolates and Mycoplasma iowae as Models.* (2022; dissertation/unknown journal metadata in retrieval). (schwab2022characterizationofputative pages 7-10, schwab2022characterizationofputativea pages 7-10, schwab2022characterizationofputative pages 1-7)  
5) **Delaby M-H. et al.** *Phenotypic plasticity in bacterial elongation among closely related species.* bioRxiv (Nov 2024). DOI: **10.1101/2024.11.07.622495**. https://doi.org/10.1101/2024.11.07.622495 (delaby2024phenotypicplasticityin pages 35-38)  
6) **Delaby M-H. et al.** *Phenotypic plasticity in cell elongation among closely related bacterial species.* Nature Communications (Jun 2025). DOI: **10.1038/s41467-025-60005-y**. https://doi.org/10.1038/s41467-025-60005-y (delaby2025phenotypicplasticityin pages 1-2, delaby2025phenotypicplasticityin pages 10-10)  
7) **Chen J. et al.** *Unraveling the role of distinct cytoskeletal motility structures in Mycoplasma pneumoniae relatives.* BMC Microbiology (Aug 2025). DOI: **10.1186/s12866-025-04320-w**. https://doi.org/10.1186/s12866-025-04320-w (chen2025unravelingtherole pages 4-7, chen2025unravelingtherole media b5911218, chen2025unravelingtherole media e3717844)


References

1. (chen2025unravelingtherole pages 4-7): Jiaxin Chen, Yalan Jiang, Yifei Wang, Gao Zeng, Peng Liu, Jindou She, Keming Zhong, Baihuan Duan, Hong Huang, Yating Wen, and Wenxin Chen. Unraveling the role of distinct cytoskeletal motility structures in mycoplasma pneumoniae relatives. BMC Microbiology, Aug 2025. URL: https://doi.org/10.1186/s12866-025-04320-w, doi:10.1186/s12866-025-04320-w. This article has 2 citations and is from a peer-reviewed journal.

2. (chen2025unravelingtherole media b5911218): Jiaxin Chen, Yalan Jiang, Yifei Wang, Gao Zeng, Peng Liu, Jindou She, Keming Zhong, Baihuan Duan, Hong Huang, Yating Wen, and Wenxin Chen. Unraveling the role of distinct cytoskeletal motility structures in mycoplasma pneumoniae relatives. BMC Microbiology, Aug 2025. URL: https://doi.org/10.1186/s12866-025-04320-w, doi:10.1186/s12866-025-04320-w. This article has 2 citations and is from a peer-reviewed journal.

3. (kysela2016diversitytakesshape pages 5-7): David T. Kysela, Amelia M. Randich, Paul D. Caccamo, and Yves V. Brun. Diversity takes shape: understanding the mechanistic and adaptive basis of bacterial morphology. PLOS Biology, 14:e1002565, Oct 2016. URL: https://doi.org/10.1371/journal.pbio.1002565, doi:10.1371/journal.pbio.1002565. This article has 149 citations and is from a highest quality peer-reviewed journal.

4. (pohl2024adynamicbactofilin pages 1-2): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

5. (richter2023interactingbactofilinsimpact pages 1-2): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

6. (schwab2022characterizationofputative pages 7-10): N Schwab. Characterization of putative virulence-associated traits in mycoplasma penetrans using clinical isolates and mycoplasma iowae as models. Unknown journal, 2022.

7. (schwab2022characterizationofputative pages 1-7): N Schwab. Characterization of putative virulence-associated traits in mycoplasma penetrans using clinical isolates and mycoplasma iowae as models. Unknown journal, 2022.

8. (pohl2024adynamicbactofilin pages 19-21): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

9. (delaby2024phenotypicplasticityin pages 35-38): Marie-Helene Delaby, Liu Yang, Maxime Jacq, Kelley A Gallagher, David T. Kysela, Velocity Hughes, Francisco Pulido, Frédéric J. Veyrier, Michael S VanNieuwenhze, and Yves V. Brun. Phenotypic plasticity in bacterial elongation among closely related species. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.07.622495, doi:10.1101/2024.11.07.622495. This article has 1 citations.

10. (delaby2025phenotypicplasticityin pages 10-10): Marie-Helene Delaby, Liu Yang, Maxime Jacq, Kelley A Gallagher, David T. Kysela, Velocity Hughes, Francisco Pulido, Frédéric J. Veyrier, Michael S VanNieuwenhze, and Yves V. Brun. Phenotypic plasticity in cell elongation among closely related bacterial species. Nature Communications, Jun 2025. URL: https://doi.org/10.1038/s41467-025-60005-y, doi:10.1038/s41467-025-60005-y. This article has 8 citations and is from a highest quality peer-reviewed journal.

11. (schwab2022characterizationofputativea pages 7-10): N Schwab. Characterization of putative virulence-associated traits in mycoplasma penetrans using clinical isolates and mycoplasma iowae as models. Unknown journal, 2022.

12. (chen2025unravelingtherole media e3717844): Jiaxin Chen, Yalan Jiang, Yifei Wang, Gao Zeng, Peng Liu, Jindou She, Keming Zhong, Baihuan Duan, Hong Huang, Yating Wen, and Wenxin Chen. Unraveling the role of distinct cytoskeletal motility structures in mycoplasma pneumoniae relatives. BMC Microbiology, Aug 2025. URL: https://doi.org/10.1186/s12866-025-04320-w, doi:10.1186/s12866-025-04320-w. This article has 2 citations and is from a peer-reviewed journal.

13. (delaby2025phenotypicplasticityin pages 1-2): Marie-Helene Delaby, Liu Yang, Maxime Jacq, Kelley A Gallagher, David T. Kysela, Velocity Hughes, Francisco Pulido, Frédéric J. Veyrier, Michael S VanNieuwenhze, and Yves V. Brun. Phenotypic plasticity in cell elongation among closely related bacterial species. Nature Communications, Jun 2025. URL: https://doi.org/10.1038/s41467-025-60005-y, doi:10.1038/s41467-025-60005-y. This article has 8 citations and is from a highest quality peer-reviewed journal.

14. (richter2023interactingbactofilinsimpact pages 26-27): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

15. (richter2023interactingbactofilinsimpact pages 15-16): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.