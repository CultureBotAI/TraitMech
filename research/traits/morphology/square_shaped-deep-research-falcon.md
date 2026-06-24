---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:52:41.553784'
end_time: '2026-06-18T10:18:37.718050'
duration_seconds: 1556.16
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: square shaped
  trait_identifier: METPO:1000694
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: square_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism forms flat, square or rectangular
    cells.
  parent_traits: METPO:1000666
  synonyms: square
  evidence_summary: 'DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Haloquadratum
    walsbyi description supports flat square cell morphology in halophilic archaea.)
    | DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined
    (Cell-shape review supports anisotropic envelope growth as the basis for non-round
    cell geometries.)'
  causal_graph_summary: 'square_shaped_planar_anisotropic_growth: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** square shaped
- **METPO identifier:** METPO:1000694
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, square or rectangular cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** square
- **Existing evidence:** DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Haloquadratum walsbyi description supports flat square cell morphology in halophilic archaea.) | DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope growth as the basis for non-round cell geometries.)
- **Existing causal graph summary:** square_shaped_planar_anisotropic_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **square shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/square_shaped.yaml`.

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
- **Trait label:** square shaped
- **METPO identifier:** METPO:1000694
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, square or rectangular cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** square
- **Existing evidence:** DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Haloquadratum walsbyi description supports flat square cell morphology in halophilic archaea.) | DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope growth as the basis for non-round cell geometries.)
- **Existing causal graph summary:** square_shaped_planar_anisotropic_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **square shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/square_shaped.yaml`.

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


## Microbial Trait Causal Graph Report: **Square shaped** (METPO:1000694)

### Scope summary (TraitMech curation target)
**Trait definition (METPO:1000694):** “A cell shape in which an organism forms flat, square or rectangular cells.”

**Operational phenotype:** an *individual microbial cell* whose 2D outline is approximately square/rectangular and typically **flat/ultrathin** (planar morphology), observed by microscopy/AFM/EM. *Haloquadratum walsbyi* is the canonical exemplar and is explicitly described as “square or rectangular” with typical dimensions reported as **2–5 μm wide by 0.1–0.2 μm thick** in the AFM study introduction (note: the paper’s printed units are “mm”; interpreted here as μm in context with figure scale bars). (saponetti2011morphologicalandstructural pages 1-2)

**Boundary cases / exclusions (avoid mis-curation):**
1. **Polygonal/discoid/triangular** archaeal morphologies are nearby traits; the archaeal literature notes both “flat squares … and triangles” as distinct geometric morphologies. (wolferen2022thecellbiology pages 3-4)
2. **Rectangular multicellular/assembled structures**: 2023 work describing “rectangular bacterial structures” in dolphin mouth highlights that rectangular appearance may reflect encapsulated parallel “segments … likely cells,” not necessarily a single square cell. This should be curated separately from METPO:1000694 unless single-cell square morphology is demonstrated. (dudek2023previouslyuncharacterizedrectangular pages 45-48)
3. **Assay artefacts**: drying and substrate adhesion can exaggerate flattening and disrupt surface layers; the *H. walsbyi* AFM work explicitly monitors capsule disruption during drying, so “square” should preferably be supported by imaging in liquid/near-physiological conditions or corroborated by independent microscopy. (saponetti2011morphologicalandstructural pages 5-8)

---

## 1) Key concepts & definitions (current understanding)

### 1.1 Square/rectangular morphology as an archaeal “geometric” cell shape
A high-authority archaeal cell biology review explicitly recognizes that some archaea display “strikingly geometric morphologies … forming flat squares … and triangles.” (wolferen2022thecellbiology pages 3-4)

The same review provides a mechanistic framing: these geometric shapes “arise as the result of precise cellular control of local growth and the axis of division under the guidance of cytoskeletal filaments and an overlying coat of glycosylated proteins, also termed the S-layer.” (wolferen2022thecellbiology pages 3-4)

### 1.2 S-layer as a primary structural determinant of archaeal shape
The archaeal **surface layer (S-layer)** is described as “formed by one or two different protein subunits that self-assemble into para-crystalline lattices.” (wolferen2022thecellbiology pages 4-6)

Functions attributed to archaeal S-layers include: “defining the cell-shape, providing mechanical stability and functioning as molecular sieves.” (wolferen2022thecellbiology pages 4-6)

Experimental genetic support in another archaeon is summarized: S-layer proteins in *Sulfolobus islandicus* were “dispensable for … viability … but cells lacking these proteins exhibited profound defects in cell shape and size.” (wolferen2022thecellbiology pages 4-6)

### 1.3 Haloquadratum walsbyi envelope/capsule features relevant to square morphology
AFM imaging of *H. walsbyi* in near physiological conditions reports a “regular corrugation with a periodicity of **16–20 nm** attributed to the … S-layer protein lattice.” (saponetti2011morphologicalandstructural pages 1-2)

The same AFM study reports an “external capsule” during drying and suggests it “might correspond to the giant protein halomucin, predicted by the genome but never before observed by other microscopy studies.” (saponetti2011morphologicalandstructural pages 1-2)

---

## 2) Recent developments & latest research (prioritizing 2023–2024)

### 2.1 2024 structural+functional dissection of archaeal S-layer integrity and shape maintenance (analog evidence)
A 2024 *Nature* paper on the marine archaeon *Nitrosopumilus maritimus* (ammonia-oxidizing archaeon) uses cryo-ET/cryo-EM and biochemistry to show S-layer disassembly affects surface binding and potentially morphology.

Key findings:
- Environmental ammonium in oceans is “reported in the **10−8 to 10−9 M** range,” motivating surface enrichment mechanisms. (kugelgen2024membranelesschannelssieve pages 1-2)
- EGTA (a chelator) perturbs the S-layer; “Near-complete disruption of the S-layer with **5 mM EGTA** entirely abolished ammonium binding.” (kugelgen2024membranelesschannelssieve pages 5-6)
- Authors conclude: “an intact S-layer is critical for ammonium binding and **may also be important for cell shape maintenance … in a calcium-dependent manner**.” (kugelgen2024membranelesschannelssieve pages 5-6)

Relevance to square-shaped trait: while not *Haloquadratum*, this is high-authority 2024 evidence that **S-layer integrity can be causally tied to shape maintenance** in archaea, strengthening the plausibility of S-layer-focused causal graphs for METPO:1000694. (kugelgen2024membranelesschannelssieve pages 5-6)

### 2.2 2023 discovery of rectangular bacterial structures (boundary case)
A 2023 study reports “rectangular bacterial structures” with an “S-layer-like periodic surface covering” and provides an observed periodicity scale (~7–9 nm) along a membrane edge, but the work emphasizes uncultured/novel structures and does not establish single-cell “square” as the unit of morphology. (dudek2023previouslyuncharacterizedrectangular pages 45-48)

Relevance: this expands the space of rectangular morphologies beyond haloarchaea, but is currently best treated as a **nearby phenotype** rather than direct evidence for METPO:1000694 curation.

---

## 3) Current applications and real-world implementations

### 3.1 S-layer self-assembly as a materials/biotechnology platform
The *H. walsbyi* AFM study notes that reassembled S-layer patches (nearly hexagonal lattice) reflect a “2D self assembling reconstruction process … used to realize matrices for the binding of functional molecules such as enzymes, antibodies, antigens etc.” (saponetti2011morphologicalandstructural pages 8-8)

This is a direct real-world application hook: S-layer lattices are used as **functionalizable 2D scaffolds**; while not unique to square cells, *H. walsbyi* provides an S-layer system with well-characterized nanoscale periodicity. (saponetti2011morphologicalandstructural pages 8-8)

### 3.2 Halomucin/capsule-inspired bioengineering ideas
The same paper proposes halomucin-like materials could be used “to create engineered biological filters … improve drug delivery … polymeric gel for biosensors or other biotechnological devices.” (saponetti2011morphologicalandstructural pages 8-8)

Curation note: this is an application-oriented discussion and does not directly validate capsule identity as halomucin in the AFM experiments.

---

## 4) Expert opinions / authoritative analysis (what is well-supported vs open)

### 4.1 Strong consensus: S-layer contributes to archaeal morphology
Authoritative review statements support that archaeal S-layers define shape and provide mechanical stability. (wolferen2022thecellbiology pages 4-6)

### 4.2 Mechanistic model for geometric shapes is plausible but under-tested in Haloquadratum
The review’s mechanism—localized envelope growth + division-axis control guided by cytoskeletal filaments plus an overlying glycosylated S-layer—provides a conceptual causal backbone for a TraitMech graph for “square shaped,” but remains **not directly demonstrated** for *H. walsbyi* in the evidence assembled here. (wolferen2022thecellbiology pages 3-4)

### 4.3 Surface diversification is strongly evidenced genomically, but its effect on square shape is uncertain
A 2015 BMC Genomics study shows a “cell-wall associated genomic island” (GI1) contains genes for “biosynthesis of surface layer … cell surface glycoproteins … envelope formation,” and that diversity arises via “homologous recombination” and “mobile genetic elements, including viruses.” (martincuadrado2015diversityofthe pages 1-2)

This strongly supports nodes/edges for **surface-layer composition variability**, but does not directly connect GI1 alleles to *square vs non-square* morphology.

---

## 5) Relevant statistics and quantitative data from the retrieved evidence

### Square-cell morphology and envelope nanostructure (Haloquadratum walsbyi)
- Reported typical dimensions: “2–5 … wide by 0.1–0.2 … thick” (context strongly suggests μm scale for cells). (saponetti2011morphologicalandstructural pages 1-2)
- S-layer periodicity: “periodicity of **16–20 nm** attributed to the … S-layer protein lattice.” (saponetti2011morphologicalandstructural pages 1-2)
- Drying time-course: the paper records capsule disruption over hours; “the main cause of the capsule disruption seems to be water loss.” (saponetti2011morphologicalandstructural pages 5-8)

### Ecological prevalence and hypersaline context
- “*Haloquadratum walsbyi* represents up to **80% of cells in NaCl-saturated brines worldwide**.” (martincuadrado2015diversityofthe pages 1-2)
- Hypersaline waters “over **30% w/v**” can have ~**10^7 cells/ml** and ~**10^9 virus particles/ml** (used in discussion of virus/surface interplay). (martincuadrado2015diversityofthe pages 7-8)

### Genomic island content and diversification (GI1)
- GI1 content: genes “putatively involved in biosynthesis of surface layer … cell surface glycoproteins … envelope formation.” (martincuadrado2015diversityofthe pages 1-2)
- Recombination signals: PHI test statistic Φ = 0.000 (recombination) and recombination events can include the S-layer gene; recombined segments can span ~21–25 kb in some GI1 versions. (martincuadrado2015diversityofthe pages 7-8)

### 2024 S-layer integrity perturbation (Nitrosopumilus maritimus; analog evidence)
- Ocean ammonium: **10−8 to 10−9 M**. (kugelgen2024membranelesschannelssieve pages 1-2)
- EGTA perturbation: **5 mM EGTA** abolishes ammonium binding when S-layer is disrupted. (kugelgen2024membranelesschannelssieve pages 5-6)

---

## Candidate nodes grouped by type (curation-ready)
| Node label | Type | Suggested grounding | Supported by (citation IDs) |
|---|---|---|---|
| square-shaped cell morphology | structure | METPO:1000694 | (wolferen2022thecellbiology pages 3-4, saponetti2011morphologicalandstructural pages 1-2) |
| flat square archaeal morphology | structure | label-only | (wolferen2022thecellbiology pages 3-4, saponetti2011morphologicalandstructural pages 1-2) |
| triangular archaeal morphology | structure | label-only | (wolferen2022thecellbiology pages 3-4) |
| archaeal S-layer | structure | GO:0030111 | (wolferen2022thecellbiology pages 4-6, wolferen2022thecellbiology pages 3-4) |
| S-layer lattice | structure | label-only | (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8) |
| S-layer corrugation (16–20 nm) | structure | label-only | (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8) |
| cell wall / cell envelope | structure | GO:0030313 | (wolferen2022thecellbiology pages 4-6, martincuadrado2015diversityofthe pages 1-2, saponetti2011morphologicalandstructural pages 1-2) |
| external capsule | structure | GO:0030314 | (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8, saponetti2011morphologicalandstructural pages 8-8) |
| quasi-periplasm / pseudoperiplasmic space | structure | label-only | (wolferen2022thecellbiology pages 4-6, kugelgen2024membranelesschannelssieve pages 1-2) |
| gas vesicles | structure | GO:0031410 | (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 3-5) |
| PHB granules | structure | label-only | (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8) |
| major cell surface glycoprotein (MCSG) | gene/protein | label-only | (martincuadrado2015diversityofthe pages 4-7) |
| S-layer protein / SLG | gene/protein | label-only | (wolferen2022thecellbiology pages 4-6, martincuadrado2015diversityofthe pages 4-7) |
| halomucin | gene/protein | label-only | (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 8-8) |
| halomucin 2 (hmu2) | gene/protein | label-only | (martincuadrado2015diversityofthe pages 4-7, martincuadrado2015diversityofthe pages 7-8) |
| archaeosortase | gene/protein | label-only | (martincuadrado2015diversityofthe pages 4-7) |
| cytoskeletal filaments | gene/protein | GO:0005856 | (wolferen2022thecellbiology pages 3-4) |
| CetZ tubulin-like proteins | gene/protein | label-only | (wolferen2022thecellbiology pages 7-9) |
| FtsZ1 | gene/protein | label-only | (wolferen2022thecellbiology pages 9-11) |
| FtsZ2 | gene/protein | label-only | (wolferen2022thecellbiology pages 9-11) |
| N-linked glycosylation | process | GO:0006487 | (wolferen2022thecellbiology pages 4-6, martincuadrado2015diversityofthe pages 7-8) |
| O-linked glycosylation | process | GO:0006493 | (martincuadrado2015diversityofthe pages 4-7) |
| local growth | process | GO:0040007 | (wolferen2022thecellbiology pages 3-4) |
| division axis control | process | label-only | (wolferen2022thecellbiology pages 3-4) |
| S-layer insertion at mid-cell | process | label-only | (wolferen2022thecellbiology pages 4-6) |
| cell-shape maintenance | process | GO:0008360 | (wolferen2022thecellbiology pages 4-6, kugelgen2024membranelesschannelssieve pages 5-6) |
| mechanical stability | process | label-only | (wolferen2022thecellbiology pages 4-6) |
| water reservoir function | process | label-only | (saponetti2011morphologicalandstructural pages 8-8) |
| homologous recombination | process | GO:0035825 | (martincuadrado2015diversityofthe pages 1-2, martincuadrado2015diversityofthe pages 7-8) |
| mobile genetic element activity | process | GO:0006313 | (martincuadrado2015diversityofthe pages 1-2, martincuadrado2015diversityofthe pages 4-7) |
| hypersaline brine | environmental factor | ENVO:01000127 | (martincuadrado2015diversityofthe pages 1-2, saponetti2011morphologicalandstructural pages 1-2) |
| NaCl-saturated brine | environmental factor | label-only | (martincuadrado2015diversityofthe pages 1-2) |
| water activity limitation | environmental factor | label-only | (saponetti2011morphologicalandstructural pages 1-2) |
| desiccation | environmental factor | GO:0009269 | (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 8-8) |
| nitrogen limitation | environmental factor | label-only | (saponetti2011morphologicalandstructural pages 5-8) |
| water loss | environmental factor | label-only | (saponetti2011morphologicalandstructural pages 5-8, saponetti2011morphologicalandstructural pages 8-8) |
| virus predation pressure | environmental factor | label-only | (martincuadrado2015diversityofthe pages 1-2, martincuadrado2015diversityofthe pages 7-8) |
| calcium ion | chemical | CHEBI:29108 | (martincuadrado2015diversityofthe pages 4-7, kugelgen2024membranelesschannelssieve pages 5-6) |
| EGTA | chemical | CHEBI:30759 | (kugelgen2024membranelesschannelssieve pages 5-6) |
| ammonium | chemical | CHEBI:28938 | (kugelgen2024membranelesschannelssieve pages 5-6, kugelgen2024membranelesschannelssieve pages 1-2) |
| sodium chloride | chemical | CHEBI:26710 | (martincuadrado2015diversityofthe pages 1-2) |
| AFM imaging in liquid / near physiological conditions | assay | label-only | (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8) |
| drying-process time-course AFM | assay | label-only | (saponetti2011morphologicalandstructural pages 5-8, saponetti2011morphologicalandstructural pages 8-8) |
| cryo-electron tomography | assay | label-only | (kugelgen2024membranelesschannelssieve pages 5-6, kugelgen2024membranelesschannelssieve pages 1-2) |
| isothermal titration calorimetry (ITC) | assay | label-only | (kugelgen2024membranelesschannelssieve pages 5-6) |
| GI1 cell-wall associated genomic island | structure | label-only | (martincuadrado2015diversityofthe pages 1-2, martincuadrado2015diversityofthe pages 7-8) |
| viruses | structure | label-only | (martincuadrado2015diversityofthe pages 1-2, martincuadrado2015diversityofthe pages 4-7, martincuadrado2015diversityofthe pages 7-8) |


*Table: This table lists candidate nodes for curating the square-shaped microbial trait into a TraitMech-style graph. It groups phenotype, envelope structures, processes, genes/proteins, chemicals, environmental factors, and assays, with suggested ontology grounding and direct support from the retrieved evidence.*

---

## Candidate causal edges (subject–predicate–object) with evidence snippets
| Subject (node) | Predicate | Object (node) | Evidence snippet (verbatim quote) | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| archaeal S-layer | defines | cell shape | “S-layers are known to fulfil roles in defining the cell-shape, providing mechanical stability and functioning as molecular sieves” (wolferen2022thecellbiology pages 4-6) | 10.1038/s41564-022-01215-8, 2022, https://doi.org/10.1038/s41564-022-01215-8 | Strong general archaeal edge; not square-specific but directly relevant to morphology. |
| archaeal S-layer | provides | mechanical stability | “S-layers are known to fulfil roles in defining the cell-shape, providing mechanical stability and functioning as molecular sieves” (wolferen2022thecellbiology pages 4-6) | 10.1038/s41564-022-01215-8, 2022, https://doi.org/10.1038/s41564-022-01215-8 | Strong general archaeal edge. |
| precise local growth and division-axis control under cytoskeletal guidance | gives rise to | flat square/triangular archaeal shapes | “These cell shapes arise as the result of precise cellular control of local growth and the axis of division under the guidance of cytoskeletal filaments and an overlying coat of glycosylated proteins, also termed the S-layer.” (wolferen2022thecellbiology pages 3-4) | 10.1038/s41564-022-01215-8, 2022, https://doi.org/10.1038/s41564-022-01215-8 | Strong conceptual mechanism for geometric archaeal morphologies; not experimentally resolved in Haloquadratum specifically. |
| Haloquadratum walsbyi S-layer | has periodicity | 16–20 nm lattice corrugation | “we demonstrate the presence of a regular corrugation with a periodicity of 16–20 nm attributed to the surface layer (S-layer) protein lattice” (saponetti2011morphologicalandstructural pages 1-2) | 10.1371/journal.pone.0018653, 2011, https://doi.org/10.1371/journal.pone.0018653 | Strong descriptive edge; supports node grounding for S-layer lattice, not by itself a causal shape mechanism. Taxon-specific. |
| external capsule / halomucin | acts as | water reservoir avoiding desiccation | “the capsule appears to be swollen with water, collapsing later during the drying process, and this observation confirms the idea of a capsule acting as a water reservoir to avoid desiccation and to regulate water activity” (saponetti2011morphologicalandstructural pages 8-8) | 10.1371/journal.pone.0018653, 2011, https://doi.org/10.1371/journal.pone.0018653 | Moderate support; capsule identity as halomucin is interpreted, not genetically verified in this experiment. Taxon-specific. |
| halomucin / external capsule | contributes to rigidity and maintenance of | unique square cell morphology | “it has been suggested that halomucin might establish the framework of a cross-linked extracellular matrix contributing to the rigidity and maintenance of H walsbyi’s unique square cell morphology” (saponetti2011morphologicalandstructural pages 8-8) | 10.1371/journal.pone.0018653, 2011, https://doi.org/10.1371/journal.pone.0018653 | Important but explicitly speculative (“it has been suggested”); curate as uncertain. Taxon-specific. |
| water loss during drying | disrupts | external capsule | “the main cause of the capsule disruption seems to be water loss” (saponetti2011morphologicalandstructural pages 5-8) | 10.1371/journal.pone.0018653, 2011, https://doi.org/10.1371/journal.pone.0018653 | Strong observational edge for environmental perturbation of capsule integrity. Taxon-specific, assay-specific. |
| nitrogen limitation with abundant carbon sources | causes accumulation of | PHB granules | “They are accumulated in unbalanced growth conditions i.e. in conditions of nitrogen limitation and abundant carbon sources” (saponetti2011morphologicalandstructural pages 5-8) | 10.1371/journal.pone.0018653, 2011, https://doi.org/10.1371/journal.pone.0018653 | Strong physiological edge for PHB accumulation; not square-specific. |
| PHB granules | decrease | cellular energy demand for ionic homeostasis | “they could also serve to reduce the cytosol volume, decreasing the cellular energy demand for ionic homeostasis” (saponetti2011morphologicalandstructural pages 5-8) | 10.1371/journal.pone.0018653, 2011, https://doi.org/10.1371/journal.pone.0018653 | Mechanistic interpretation by authors; indirect link to shape. Taxon-specific and somewhat inferential. |
| NaCl-saturated brines | support high abundance of | Haloquadratum walsbyi | “Haloquadratum walsbyi represents up to 80 % of cells in NaCl-saturated brines worldwide” (martincuadrado2015diversityofthe pages 1-2) | 10.1186/s12864-015-1794-8, 2015, https://doi.org/10.1186/s12864-015-1794-8 | Strong ecology edge for environmental context of the trait. |
| GI1 (cell-wall associated genomic island) | contains genes for | S-layer biosynthesis / cell surface glycoproteins / envelope formation | “The islands predominantly contained genes putatively involved in biosynthesis of surface layer, genes encoding cell surface glycoproteins and genes involved in envelope formation.” (martincuadrado2015diversityofthe pages 1-2) | 10.1186/s12864-015-1794-8, 2015, https://doi.org/10.1186/s12864-015-1794-8 | Strong genomic content edge; supports candidate mechanistic nodes. Taxon-specific. |
| homologous recombination and mobile genetic elements, including viruses | drive diversity of | GI1 / surface structures including cell wall | “the diversity of this region arises through homologous recombination but also through the action of mobile genetic elements, including viruses” (martincuadrado2015diversityofthe pages 1-2) | 10.1186/s12864-015-1794-8, 2015, https://doi.org/10.1186/s12864-015-1794-8 | Strong population-genomic edge; effect is surface diversification, not directly proven square-shape modulation. Taxon-specific. |
| EGTA pretreatment / S-layer disruption | abolishes | ammonium binding | “Near-complete disruption of the S-layer with 5 mM EGTA entirely abolished ammonium binding” (kugelgen2024membranelesschannelssieve pages 5-6) | 10.1038/s41586-024-07462-5, 2024, https://doi.org/10.1038/s41586-024-07462-5 | Strong experimental edge in N. maritimus; not square-shape-specific, but supports causal importance of intact S-layer. |
| intact S-layer | may be important for | cell shape maintenance | “These experiments indicate that an intact S-layer is critical for ammonium binding and may also be important for cell shape maintenance in N. maritimus in a calcium-dependent manner.” (kugelgen2024membranelesschannelssieve pages 5-6) | 10.1038/s41586-024-07462-5, 2024, https://doi.org/10.1038/s41586-024-07462-5 | Recent high-authority support; explicitly tentative (“may also”). Different archaeal taxon; use as general S-layer-shape support, not Haloquadratum-specific. |
| loss of S-layer proteins in Sulfolobus islandicus | causes defects in | cell shape and size | “S-layer proteins were recently found to be dispensable for S.islandicus viability under laboratory conditions, but cells lacking these proteins exhibited profound defects in cell shape and size” (wolferen2022thecellbiology pages 4-6) | 10.1038/s41564-022-01215-8, 2022, https://doi.org/10.1038/s41564-022-01215-8 | Strong functional edge for causal role of S-layer in archaeal morphology; taxon-specific but broadly relevant. |


*Table: This table compiles candidate causal edges for square-shaped microbial morphology, emphasizing S-layer, capsule/halomucin, environmental context, and genomic-island evidence. It is useful for curating a TraitMech graph because it pairs each proposed edge with a verbatim evidence snippet, citation, and uncertainty note.*

---

## Mechanistic causal graph sketch (minimal, evidence-anchored)
A conservative TraitMech causal graph that stays close to explicit evidence can be organized around:
1) **S-layer lattice (composition/assembly/integrity)** → **cell shape maintenance** (supported generally for archaea; directly for *S. islandicus*; tentatively for *N. maritimus*). (wolferen2022thecellbiology pages 4-6, kugelgen2024membranelesschannelssieve pages 5-6)
2) **Capsule/halomucin-like matrix** → **water reservoir / desiccation protection**; and (uncertain) → **rigidity/maintenance of square morphology**. (saponetti2011morphologicalandstructural pages 8-8)
3) **Hypersaline brine environment / water activity limitation** → selection pressure for envelope solutions (S-layer, capsule; population dominance). (martincuadrado2015diversityofthe pages 1-2, saponetti2011morphologicalandstructural pages 1-2)
4) **GI1 surface-layer gene content + recombination/mobile elements** → **surface structure diversity** (potentially affecting envelope mechanics; direct link to square trait remains unproven). (martincuadrado2015diversityofthe pages 1-2, martincuadrado2015diversityofthe pages 7-8)
5) **Local growth + division axis control guided by cytoskeletal filaments + S-layer** → **geometric (square/triangular) shapes** (conceptual, review-derived). (wolferen2022thecellbiology pages 3-4)

---

## Warnings (claims not yet ready for strong curation)
1. **Halomucin causes/maintains square shape**: the AFM study states “it has been suggested” halomucin contributes to rigidity/maintenance of square morphology; treat as **uncertain** unless supported by genetic perturbation or direct biochemical identification of capsule as halomucin. (saponetti2011morphologicalandstructural pages 8-8)
2. **GI1 variation causes square vs non-square morphology**: GI1 clearly encodes S-layer/surface glycoproteins and is diversified by recombination/viruses, but no direct mapping to the square phenotype is provided in the cited text; curate as **surface-structure diversity**, not shape causation. (martincuadrado2015diversityofthe pages 1-2)
3. **Use of N. maritimus S-layer evidence for Haloquadratum**: 2024 work supports S-layer integrity and possible shape maintenance in archaea, but it is a different lineage and phenotype; curate cross-taxon edges as **general archaeal envelope principle**, not Haloquadratum-specific. (kugelgen2024membranelesschannelssieve pages 5-6)
4. **Units for H. walsbyi dimensions**: the text uses “mm” while figures use μm-scale bars; treat dimensions as μm with a note to verify against the PDF/errata before final YAML commit. (saponetti2011morphologicalandstructural pages 1-2)

---

## Key figures (visual evidence)
AFM figures demonstrating square/flat morphology, S-layer periodicity, and capsule disruption were retrieved from the 2011 *H. walsbyi* study. (saponetti2011morphologicalandstructural media 72dc8c3f, saponetti2011morphologicalandstructural media 3342d5f0, saponetti2011morphologicalandstructural media f6bb3a53, saponetti2011morphologicalandstructural media 2530383d, saponetti2011morphologicalandstructural media 6268c752)

---

## DOI-first bibliography (with dates and URLs)
1. **von Kügelgen A. et al.** “Membraneless channels sieve cations in ammonia-oxidizing marine archaea.” *Nature* (Published online **29 May 2024**). DOI: **10.1038/s41586-024-07462-5**. URL: https://doi.org/10.1038/s41586-024-07462-5 (kugelgen2024membranelesschannelssieve pages 1-2)
2. **Sublimi Saponetti M. et al.** “Morphological and Structural Aspects of the Extremely Halophilic Archaeon *Haloquadratum walsbyi*.” *PLoS ONE* (**29 Apr 2011**). DOI: **10.1371/journal.pone.0018653**. URL: https://doi.org/10.1371/journal.pone.0018653 (saponetti2011morphologicalandstructural pages 1-2)
3. **Martin-Cuadrado A.-B. et al.** “Diversity of the cell-wall associated genomic island of the archaeon *Haloquadratum walsbyi*.” *BMC Genomics* (**Aug 2015**). DOI: **10.1186/s12864-015-1794-8**. URL: https://doi.org/10.1186/s12864-015-1794-8 (martincuadrado2015diversityofthe pages 1-2)
4. **van Wolferen M. et al.** “The Cell Biology of Archaea.” *Nature Microbiology* (**Oct 2022**). DOI: **10.1038/s41564-022-01215-8**. URL: https://doi.org/10.1038/s41564-022-01215-8 (wolferen2022thecellbiology pages 3-4)
5. **Dudek N.K. et al.** “Previously uncharacterized rectangular bacterial structures in the dolphin mouth.” *Nature Communications* / preprint DOI shown (**Oct 2023**; text retrieved is via bioRxiv DOI). DOI: **10.1101/2021.10.23.465578**. URL: https://doi.org/10.1101/2021.10.23.465578 (dudek2023previouslyuncharacterizedrectangular pages 45-48)

References

1. (saponetti2011morphologicalandstructural pages 1-2): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

2. (wolferen2022thecellbiology pages 3-4): Marleen van Wolferen, Andre Arashiro Pulschen, Buzz Baum, Simonetta Gribaldo, and Sonja-Verena Albers. The cell biology of archaea. Nature microbiology, 7:1744-1755, Oct 2022. URL: https://doi.org/10.1038/s41564-022-01215-8, doi:10.1038/s41564-022-01215-8. This article has 129 citations and is from a highest quality peer-reviewed journal.

3. (dudek2023previouslyuncharacterizedrectangular pages 45-48): Natasha K. Dudek, Jesus G. Galaz-Montoya, Handuo Shi, Megan Mayer, Cristina Danita, Arianna I. Celis, Tobias Viehboeck, Gong-Her Wu, Barry Behr, Silvia Bulgheresi, Kerwyn Casey Huang, Wah Chiu, and David A. Relman. Previously uncharacterized rectangular bacterial structures in the dolphin mouth. Nature Communications, Oct 2023. URL: https://doi.org/10.1101/2021.10.23.465578, doi:10.1101/2021.10.23.465578. This article has 7 citations and is from a highest quality peer-reviewed journal.

4. (saponetti2011morphologicalandstructural pages 5-8): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

5. (wolferen2022thecellbiology pages 4-6): Marleen van Wolferen, Andre Arashiro Pulschen, Buzz Baum, Simonetta Gribaldo, and Sonja-Verena Albers. The cell biology of archaea. Nature microbiology, 7:1744-1755, Oct 2022. URL: https://doi.org/10.1038/s41564-022-01215-8, doi:10.1038/s41564-022-01215-8. This article has 129 citations and is from a highest quality peer-reviewed journal.

6. (kugelgen2024membranelesschannelssieve pages 1-2): Andriko von Kügelgen, C. Keith Cassidy, Sofie van Dorst, Lennart L. Pagani, Christopher Batters, Zephyr Ford, Jan Löwe, Vikram Alva, Phillip J. Stansfeld, and Tanmay A. M. Bharat. Membraneless channels sieve cations in ammonia-oxidizing marine archaea. Nature, 630:230-236, May 2024. URL: https://doi.org/10.1038/s41586-024-07462-5, doi:10.1038/s41586-024-07462-5. This article has 31 citations and is from a highest quality peer-reviewed journal.

7. (kugelgen2024membranelesschannelssieve pages 5-6): Andriko von Kügelgen, C. Keith Cassidy, Sofie van Dorst, Lennart L. Pagani, Christopher Batters, Zephyr Ford, Jan Löwe, Vikram Alva, Phillip J. Stansfeld, and Tanmay A. M. Bharat. Membraneless channels sieve cations in ammonia-oxidizing marine archaea. Nature, 630:230-236, May 2024. URL: https://doi.org/10.1038/s41586-024-07462-5, doi:10.1038/s41586-024-07462-5. This article has 31 citations and is from a highest quality peer-reviewed journal.

8. (saponetti2011morphologicalandstructural pages 8-8): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

9. (martincuadrado2015diversityofthe pages 1-2): Ana-Belen Martin-Cuadrado, Lejla Pašić, and Francisco Rodriguez-Valera. Diversity of the cell-wall associated genomic island of the archaeon haloquadratum walsbyi. BMC Genomics, Aug 2015. URL: https://doi.org/10.1186/s12864-015-1794-8, doi:10.1186/s12864-015-1794-8. This article has 26 citations and is from a peer-reviewed journal.

10. (martincuadrado2015diversityofthe pages 7-8): Ana-Belen Martin-Cuadrado, Lejla Pašić, and Francisco Rodriguez-Valera. Diversity of the cell-wall associated genomic island of the archaeon haloquadratum walsbyi. BMC Genomics, Aug 2015. URL: https://doi.org/10.1186/s12864-015-1794-8, doi:10.1186/s12864-015-1794-8. This article has 26 citations and is from a peer-reviewed journal.

11. (saponetti2011morphologicalandstructural pages 3-5): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

12. (martincuadrado2015diversityofthe pages 4-7): Ana-Belen Martin-Cuadrado, Lejla Pašić, and Francisco Rodriguez-Valera. Diversity of the cell-wall associated genomic island of the archaeon haloquadratum walsbyi. BMC Genomics, Aug 2015. URL: https://doi.org/10.1186/s12864-015-1794-8, doi:10.1186/s12864-015-1794-8. This article has 26 citations and is from a peer-reviewed journal.

13. (wolferen2022thecellbiology pages 7-9): Marleen van Wolferen, Andre Arashiro Pulschen, Buzz Baum, Simonetta Gribaldo, and Sonja-Verena Albers. The cell biology of archaea. Nature microbiology, 7:1744-1755, Oct 2022. URL: https://doi.org/10.1038/s41564-022-01215-8, doi:10.1038/s41564-022-01215-8. This article has 129 citations and is from a highest quality peer-reviewed journal.

14. (wolferen2022thecellbiology pages 9-11): Marleen van Wolferen, Andre Arashiro Pulschen, Buzz Baum, Simonetta Gribaldo, and Sonja-Verena Albers. The cell biology of archaea. Nature microbiology, 7:1744-1755, Oct 2022. URL: https://doi.org/10.1038/s41564-022-01215-8, doi:10.1038/s41564-022-01215-8. This article has 129 citations and is from a highest quality peer-reviewed journal.

15. (saponetti2011morphologicalandstructural media 72dc8c3f): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

16. (saponetti2011morphologicalandstructural media 3342d5f0): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

17. (saponetti2011morphologicalandstructural media f6bb3a53): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

18. (saponetti2011morphologicalandstructural media 2530383d): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

19. (saponetti2011morphologicalandstructural media 6268c752): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.