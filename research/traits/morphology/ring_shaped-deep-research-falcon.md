---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:19:51.578770'
end_time: '2026-06-18T09:39:59.013529'
duration_seconds: 1207.43
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: ring shaped
  trait_identifier: METPO:1000680
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: ring_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism forms circular or toroidal structures.
  parent_traits: METPO:1000666
  synonyms: ring, ring-shaped
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell curvature (Cell-shape
    review supports curvature-generating wall patterning as the basis for closed-ring
    morphology.)'
  causal_graph_summary: 'ring_shaped_curved_growth_closure: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ring shaped
- **METPO identifier:** METPO:1000680
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms circular or toroidal structures.
- **Parent traits:** METPO:1000666
- **Synonyms:** ring, ring-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell curvature (Cell-shape review supports curvature-generating wall patterning as the basis for closed-ring morphology.)
- **Existing causal graph summary:** ring_shaped_curved_growth_closure: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **ring shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/ring_shaped.yaml`.

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
- **Trait label:** ring shaped
- **METPO identifier:** METPO:1000680
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms circular or toroidal structures.
- **Parent traits:** METPO:1000666
- **Synonyms:** ring, ring-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell curvature (Cell-shape review supports curvature-generating wall patterning as the basis for closed-ring morphology.)
- **Existing causal graph summary:** ring_shaped_curved_growth_closure: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **ring shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/ring_shaped.yaml`.

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


## Microbial Trait Causal Graph Report: **ring shaped** (METPO:1000680)

### Executive scope summary
The METPO trait **ring shaped** is defined as a **whole-cell morphology** in which an organism forms a **closed circular/toroidal cell body** (a “donut” shaped cell) rather than an open curved rod or helix. A key curation risk is conflating this trait with **ring-shaped intracellular assemblies**, which are common in microbes (e.g., the **FtsZ Z-ring** during cytokinesis) but do **not** imply a toroidal cell body (bhambhani2020bacteriophagesp01gene pages 1-2, middlemiss2024molecularmotortugofwar pages 1-2). Another common confusion is with **toroidal chromosome/nucleoid conformations** in stressed or sporulating cells, which again are intracellular architectures rather than cell shape traits (bauda2024ultrastructureofmacromolecular pages 1-2).

Because the available evidence set strongly supports **mechanistic generation of ring-like/toroidal *structures*** (division rings; in vitro toroids of cytoskeletal polymers) and **curvature/shape control** (MreB/bactofilins/peptidoglycan patterning), but contains **limited direct evidence of naturally occurring toroidal whole-cell bodies**, the most curation-ready strategy is:
1) curate a **core mechanistic subgraph** for *closed-loop polymer and cell-envelope patterning that can in principle yield closed-loop morphologies*; and
2) clearly mark as **boundary/uncertain** anything that only pertains to *intracellular rings* (Z-ring) or *toroidal chromosomes*.

---

## 1) Trait scope and boundary cases (curation guidance)

### What the trait represents (recommended operationalization)
- **Primary phenotype:** a **toroidal/circular cell body** (closed loop). This is more stringent than “curved,” “crescent,” or “helical.”
- **Assay readout:** microscopy-based shape classification (phase contrast/DIC/fluorescence) with clear evidence of a closed loop.

### Boundary cases to exclude or separately curate
1) **Cytokinetic Z-ring (intracellular, transient):** FtsZ “assembles into a toroidal array” at midcell to organize septation; this is a ring-shaped *protein structure* during division, not a ring-shaped cell body (bhambhani2020bacteriophagesp01gene pages 1-2).
2) **Toroidal chromosomes/nucleoids:** during early sporulation, the *chromosome* adopts a toroidal structure (bauda2024ultrastructureofmacromolecular pages 1-2). This is not a morphology trait.
3) **Circumferential growth patterns:** elongasome complexes move around the cell circumference and insert circumferential glycan strands that reinforce rods (middlemiss2024molecularmotortugofwar pages 1-2). This produces ring-like *patterning* on the envelope, not necessarily toroidal cells.
4) **Curved/helical rods:** curvature determinants such as CrvA (skewing peptidoglycan synthesis rates) and crescentin (intermediate-filament-like curvature factor) produce curved/helical forms but not necessarily a closed loop (schiller2024identificationofstructural pages 1-2).

**Curation warning:** unless METPO intends to include *ring-shaped intracellular structures*, TraitMech edges about FtsZ/ZapD should be flagged as **supporting mechanistic plausibility** rather than direct determinants of the whole-cell “ring shaped” class.

---

## 2) Candidate causal graph entities (nodes) grounded where possible

### A. Cell division ring / divisome (closed-loop cytoskeletal structure)
- **FtsZ** (tubulin-like GTPase; Z-ring polymer)
  - Forms a “ring-shaped structure” at cytokinesis; “toroidal array of treadmilling polymers” (bhambhani2020bacteriophagesp01gene pages 1-2)
- **Divisome recruitment targets:** **FtsW**, **Pbp2B** (septal wall synthesis) (bhambhani2020bacteriophagesp01gene pages 1-2)
- **Anchors/regulators mentioned:** **FtsA**, **SepF**, **ZipA** (contextual divisome components; competition for binding cited in ZapD paper) (merinosalomon2025crosslinkingbyzapd pages 10-12, bhambhani2020bacteriophagesp01gene pages 1-2)
- **Crosslinkers/bundlers:** **ZapD**, **ZapA** (merinosalomon2025crosslinkingbyzapd pages 10-12)

### B. Cytoskeletal crosslinking and toroid formation (in vitro but mechanistically precise)
- **ZapD–FtsZ interaction stoichiometry** (experimental factor/node): 0.3–0.4 vs 1.1 mol ZapD/mol FtsZ influences toroid vs bundle (merinosalomon2025crosslinkingbyzapd pages 10-12)
- **Inter-filament spacing** (physical node): spacing changes with crosslinking (merinosalomon2025crosslinkingbyzapd pages 10-12)

### C. Cell wall synthesis patterning / elongation machinery (envelope patterning)
- **MreB** (actin-like cytoskeleton) controlling lateral/circumferential peptidoglycan insertion (dersch2024adaptationofbacillus pages 1-2, middlemiss2024molecularmotortugofwar pages 1-2)
- **RodZ** (MreB interactor; diffusive fraction changes under stress) (dersch2024adaptationofbacillus pages 1-2)
- **RodA** (glycosyltransferase) and **PBP2A/PBPH** (transpeptidases) as core elongasome enzymes (middlemiss2024molecularmotortugofwar pages 1-2)

### D. Accessory cytoskeleton–hydrolase modules (local wall remodeling; curvature control)
- **Bactofilins** (InterPro:IPR007607; cytoskeletal polymers) (pohl2024adynamicbactofilin pages 1-2)
- **M23 peptidase family hydrolase (LmdC)** interacting with bactofilin; required for proper shape (pohl2024adynamicbactofilin pages 1-2)

### E. Environmental/experimental factors
- **Osmotic upshift / osmotic stress** (ENVO label candidate)
- **Potassium influx / K+** affecting MreB filament disassembly and survival (dersch2024adaptationofbacillus pages 1-2)

### F. Boundary-case toroids (exclude from “cell shape” unless trait definition expanded)
- **Forespore chromosome toroid** during sporulation (bauda2024ultrastructureofmacromolecular pages 1-2)

---

## 3) Candidate causal edges (curation-ready triples)
The following table is designed for direct conversion into a TraitMech YAML graph. It emphasizes edges with evidence snippets and explicit uncertainty markers.

| Edge (S–P–O) | Entity type(s) | Suggested ontology grounding (CURIEs if known) | Evidence snippet (short quote) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| FtsZ polymerization/assembly → forms → Z-ring (toroidal division ring) | protein; biological process; cellular structure | FtsZ: UniProt family label only; cytokinetic ring: GO:0000917 | “FtsZ assembles into a toroidal array of treadmilling polymers” (bhambhani2020bacteriophagesp01gene pages 1-2) | 10.1128/JB.00463-20, 2020, https://doi.org/10.1128/JB.00463-20 | Strong for division-ring toroids; supports ring-like intracellular structure, not whole-cell toroidal morphology. |
| FtsZ ring → scaffolds recruitment of → septal cell wall synthesis machinery | cellular structure; biological process; proteins/complex | GO:0000917; septal PG synthesis: label only; Pbp2B/PBP2B: label only; FtsW: UniProt family label only | “This FtsZ ring serves as a scaffold for recruitment of other proteins into a mature division-competent structure permitting membrane constriction and septal cell wall synthesis” (bhambhani2020bacteriophagesp01gene pages 1-2) | 10.1128/JB.00463-20, 2020, https://doi.org/10.1128/JB.00463-20 | Strong for divisome mechanism; trait relevance indirect unless ring-shaped trait is defined broadly to include closed-loop intracellular ring structures. |
| gp56 → inhibits recruitment of → Pbp2B/FtsW | phage protein; proteins | gp56: label only; Pbp2B: label only; FtsW: UniProt family label only | “gp56 interferes with the recruitment of late division proteins, including Pbp2b and FtsW” (bhambhani2020bacteriophagesp01gene pages 1-2) | 10.1128/JB.00463-20, 2020, https://doi.org/10.1128/JB.00463-20 | Bacillus subtilis/phage-specific perturbation; informative negative/regulatory edge for ring function, not ring-shape generation. |
| gp56 localization/activity → depends on → FtsL interaction | phage protein; divisome protein | gp56: label only; FtsL: UniProt family label only | “gp56 localization and activity depend on its interaction with FtsL” (bhambhani2020bacteriophagesp01gene pages 1-2) | 10.1128/JB.00463-20, 2020, https://doi.org/10.1128/JB.00463-20 | Taxon- and infection-specific; useful for divisome perturbation graph, not core morphology determinant. |
| ZapD crosslinking of FtsZ → stabilizes/promotes → toroidal FtsZ macrostructures | crosslinker protein; cytoskeletal protein; supramolecular structure | ZapD: label only; FtsZ: UniProt family label only; cytokinetic ring: GO:0000917 | “ZapD helps to stabilize these toroids by crosslinking” (merinosalomon2025crosslinkingbyzapd pages 10-12) | 10.1101/2023.01.12.523557, 2025 preprint, https://doi.org/10.1101/2023.01.12.523557 | In vitro preprint; strong mechanistic support for toroid formation in reconstituted system. |
| Low ZapD:FtsZ stoichiometry (0.3–0.4 mol/mol) → favors formation of → toroids | experimental factor; proteins; supramolecular structure | ZapD: label only; FtsZ: UniProt family label only | “toroids are the most prominent structures, with a binding stoichiometry of ZapD in the polymer of 0.3-0.4 moles of ZapD per mole of FtsZ” (merinosalomon2025crosslinkingbyzapd pages 10-12) | 10.1101/2023.01.12.523557, 2025 preprint, https://doi.org/10.1101/2023.01.12.523557 | Quantitative, assay-specific, in vitro. Strong for conditional edge. |
| High ZapD:FtsZ stoichiometry (1.1 mol/mol) → reorganizes into → straight bundles | experimental factor; proteins; supramolecular structure | ZapD: label only; FtsZ: UniProt family label only | “This leads to a reorganization of the polymer bundles, resulting in straight structures” (merinosalomon2025crosslinkingbyzapd pages 10-12) | 10.1101/2023.01.12.523557, 2025 preprint, https://doi.org/10.1101/2023.01.12.523557 | Negative/alternative morphology edge; useful boundary case distinguishing toroids from bundles. |
| Increased ZapD-mediated crosslink density → reduces flexibility needed for → toroidal structures | protein interaction state; physical process; supramolecular structure | label only | “The increase in the number of ZapD-FtsZ contacts likely reduces the flexibility needed to form toroidal structures” (merinosalomon2025crosslinkingbyzapd pages 10-12) | 10.1101/2023.01.12.523557, 2025 preprint, https://doi.org/10.1101/2023.01.12.523557 | Mechanistic inference by authors; curate as uncertain/physical mechanism. |
| MreB filament motion → correlates with → rate of cell wall growth | cytoskeletal protein; biological process | MreB: UniProt family label only; lateral cell wall biogenesis: GO label only | “the motion of MreB filaments correlates with the rate of cell wall growth” (dersch2024adaptationofbacillus pages 1-2) | 10.3390/microorganisms12071309, 2024, https://doi.org/10.3390/microorganisms12071309 | General shape-control edge; supports wall-patterning basis of morphology, not ring-specific by itself. |
| Osmotic upshift → causes disassembly/release of → MreB filaments | environmental factor; cytoskeletal protein | osmotic stress: ENVO label candidate; MreB: UniProt family label only | “In response to osmotic upshift, MreB molecules were released from filaments” (dersch2024adaptationofbacillus pages 1-2) | 10.3390/microorganisms12071309, 2024, https://doi.org/10.3390/microorganisms12071309 | Environmental modulation; B. subtilis-specific experiment. |
| MreB filament disassembly → leads to less organized → peptidoglycan synthesis pattern | cytoskeletal process; biological process | MreB: UniProt family label only; peptidoglycan biosynthetic process: GO:0009252 | “the peptidoglycan synthesis pattern became less organized” after MreB release (dersch2024adaptationofbacillus pages 1-2) | 10.3390/microorganisms12071309, 2024, https://doi.org/10.3390/microorganisms12071309 | Supports causal link between cytoskeleton and wall patterning; indirect for ring-shaped trait. |
| Potassium influx deficiency → prevents → MreB filament disassembly after osmotic shock | ion transport/environmental response; cytoskeletal process | potassium ion transport: GO:0006813; MreB: UniProt family label only | “mutant strains that prevent efficient potassium influx… show a failure to disassemble MreB filaments” (dersch2024adaptationofbacillus pages 1-2) | 10.3390/microorganisms12071309, 2024, https://doi.org/10.3390/microorganisms12071309 | Useful environmental/regulatory edge; not ring-specific. |
| RodA-containing elongasome → inserts glycan strands circumferentially → rod-shaped cell wall | enzyme/complex; biological process; morphology | RodA: UniProt family label only; peptidoglycan glycosyltransferase activity: GO label candidate | “elongasome… moves processively around the cell circumference and inserts long glycan strands… thereby giving rise to a rod-shaped cell” (middlemiss2024molecularmotortugofwar pages 1-2) | 10.1038/s41467-024-49785-x, 2024, https://doi.org/10.1038/s41467-024-49785-x | Strong for circumferential wall patterning; informs parent trait curved/rod morphogenesis more than closed-ring phenotype. |
| MreB double filaments → guide peptidoglycan insertion → perpendicular to long axis | cytoskeletal structure; biological process | MreB: UniProt family label only | “These cytoskeletal structures guide peptidoglycan insertion perpendicular to the long axis of the cell” (middlemiss2024molecularmotortugofwar pages 1-2) | 10.1038/s41467-024-49785-x, 2024, https://doi.org/10.1038/s41467-024-49785-x | General wall-patterning mechanism; indirect for ring-shaped trait. |
| Bactofilin polymers → spatially regulate → cell wall biosynthesis | cytoskeletal protein; biological process | bactofilin: InterPro:IPR007607; peptidoglycan biosynthetic process: GO:0009252 | “bactofilin polymers localize dynamically to the stalk base and the bud neck… indicating a central role in the spatial regulation of cell wall biosynthesis” (pohl2024adynamicbactofilin pages 1-2) | 10.7554/eLife.86577.2, 2024, https://doi.org/10.7554/eLife.86577.2 | Strong for localized morphogenesis; not directly toroidal/ring-shaped cells. |
| LmdC (M23 peptidase) → interacts with → bactofilin | hydrolase; cytoskeletal protein | M23 peptidase family: EC label candidate; bactofilin: InterPro:IPR007607 | “the H. neptunium M23 peptidase homolog LmdC interacts directly with bactofilin in vitro” (pohl2024adynamicbactofilin pages 1-2) | 10.7554/eLife.86577.2, 2024, https://doi.org/10.7554/eLife.86577.2 | Strong direct interaction; species-specific. |
| Bactofilin–LmdC module → promotes local changes in → cell wall biosynthesis mode | protein module; biological process | bactofilin: InterPro:IPR007607; M23 peptidase: EC label candidate | “bactofilins and M23 peptidases form a conserved functional module that promotes local changes in the mode of cell wall biosynthesis” (pohl2024adynamicbactofilin pages 1-2) | 10.7554/eLife.86577.2, 2024, https://doi.org/10.7554/eLife.86577.2 | Good higher-level causal edge; cross-taxon generalization from multiple alphaproteobacteria. |
| Bactofilin–LmdC co-localization at inner curve → modulates → degree of cell curvature | protein module; morphology | bactofilin: InterPro:IPR007607; cell curvature: label only | “co-localize at the inner curve of the cell, modulating the degree of cell curvature” (pohl2024adynamicbactofilin pages 1-2) | 10.7554/eLife.86577.2, 2024, https://doi.org/10.7554/eLife.86577.2 | Curvature rather than closed ring; probably parent-trait evidence, not direct ring-shaped trait evidence. |
| CrvA polymer formation → skews → peptidoglycan synthesis rates | cytoskeletal/shape protein; biological process | CrvA: label only; peptidoglycan biosynthetic process: GO:0009252 | “CrvA in Vibrio cholerae… skews peptidoglycan synthesis rates” (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0, 2024, https://doi.org/10.1038/s41467-024-45196-0 | Review-like summary within archaeal paper; indirect but authoritative support for curvature-generating wall patterning. |
| Crescentin → promotes → cell curvature | intermediate-filament-like protein; morphology | crescentin/CreS: label only | “the intermediate filament-like protein crescentin in C. crescentus” generates curvature (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0, 2024, https://doi.org/10.1038/s41467-024-45196-0 | Canonical curvature determinant; supports parent-trait mechanism, not closed-loop phenotype directly. |
| Volactin (archaeal actin homolog) → contributes to → disk-shape morphogenesis | actin-like protein; morphology | volactin: label only; actin family: InterPro label candidate | “an actin homolog that plays a role in disk-shape morphogenesis, which we named volactin” (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0, 2024, https://doi.org/10.1038/s41467-024-45196-0 | Archaeal, non-ring phenotype; useful cautionary comparator for non-bacterial shape control. |
| CetZ1 loss → causes absence of → disk formation | tubulin-like protein; morphology | CetZ1: label only | “cells lacking archaeal tubulin homolog CetZ1 only make disks” / “CetZ1… required for disk formation” summarized in text (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0, 2024, https://doi.org/10.1038/s41467-024-45196-0 | Archaeal disk-shape determinant; boundary-case evidence distinguishing disk from ring/toroid. |
| Forespore chromosome during early sporulation → adopts → toroidal structure | chromosome; cellular structure; developmental stage | chromosome organization: GO label only | “the chromosome in the forespore adopts a toroidal structure” (bauda2024ultrastructureofmacromolecular pages 1-2) | 10.1038/s41467-024-45770-6, 2024, https://doi.org/10.1038/s41467-024-45770-6 | Important toroid example, but this is chromosome architecture, not cell shape; should not be conflated with trait. |


*Table: This table compiles evidence-backed causal edges relevant to the microbial morphology trait 'ring shaped,' focusing on supported mechanisms from the available contexts. It is designed for TraitMech curation by separating direct toroidal/ring-structure evidence from broader cell-shape and boundary-case mechanisms.*

### Visual evidence supporting a key mechanistic edge
Cropped figure panels retrieved from Merino-Salomón et al. show **ZapD-induced toroidal FtsZ assemblies** and a **schematic of concentration-dependent transitions** (toroids → straight bundles) with quantitative measurements (outer diameter/thickness; spacing; stoichiometry) (merinosalomon2025crosslinkingbyzapd media 2f2f3495, merinosalomon2025crosslinkingbyzapd media a57e5489, merinosalomon2025crosslinkingbyzapd media 22c0d621, merinosalomon2025crosslinkingbyzapd media 1d9bbab1). These images support the curated edge family: *ZapD crosslinking/stoichiometry → toroidal FtsZ macrostructures*.

---

## 4) Recent developments and “latest research” emphasis (2023–2024 priority)

### 4.1 Single-molecule mapping of circumferential wall synthesis dynamics (2024)
Middlemiss et al. (Nature Communications, published 2024-06; DOI:10.1038/s41467-024-49785-x) developed **single-molecule VerCINI** to track elongasome complexes around the entire cell circumference for minutes, addressing prior TIRF geometric limitations (middlemiss2024molecularmotortugofwar pages 1-2). They note prior elongasome processivity estimates were **400–600 nm** and define processivity explicitly as distance traveled until pausing/reversal/termination (middlemiss2024molecularmotortugofwar pages 1-2). This is immediately relevant to ring-shaped trait mechanistic hypotheses because it operationalizes how **circumferential insertion** patterns can be produced and regulated.

### 4.2 Environmental control of cytoskeletal assembly and PG patterning (2024)
Dersch & Graumann (Microorganisms, published 2024-06-27; DOI:10.3390/microorganisms12071309) report that during **osmotic upshift**, MreB molecules are released from filaments with a concomitant loss of organized PG synthesis pattern and slowed extension (dersch2024adaptationofbacillus pages 1-2). They further show that mutants preventing early **potassium influx** fail to disassemble MreB filaments and have altered outcomes; importantly, lack of early K+ influx “strongly decreases cell survival” (dersch2024adaptationofbacillus pages 1-2). This supports environmental edges linking ionic stress response → cytoskeletal state → wall synthesis patterning.

### 4.3 Conserved accessory cytoskeleton–hydrolase modules for local wall remodeling (2024)
Pöhl et al. (eLife, version of record 2024-01-31; DOI:10.7554/eLife.86577.2) provide evidence for a conserved module where **bactofilin polymers** spatially regulate wall biosynthesis and physically/biochemically interact with an **M23 endopeptidase (LmdC)** that is required for proper morphology (pohl2024adynamicbactofilin pages 1-2). Their conclusion that bactofilins and M23 peptidases form a conserved module that “promotes local changes in the mode of cell wall biosynthesis” provides curation-ready mid-level mechanistic edges (pohl2024adynamicbactofilin pages 1-2).

### 4.4 Cross-domain expansion of cell shape determinants (archaea; 2024)
Schiller et al. (Nature Communications, published 2024-02; DOI:10.1038/s41467-024-45196-0) frame bacterial shape control as often mediated via **peptidoglycan modulation**, highlighting curvature factors (CrvA; crescentin) and MreB-dependent lateral synthesis, while also identifying archaeal shape determinants (e.g., actin homolog “volactin” for disk morphogenesis) (schiller2024identificationofstructural pages 1-2). This is useful for ontology grounding and boundary conditions (ring-shaped cell bodies vs disk/rod transitions).

---

## 5) Current applications and real-world implementations

1) **Antibiotic mechanism and development context:** The elongasome and divisome are core cell wall synthesis systems and primary antibiotic targets; understanding their dynamics is directly motivated by antibiotic resistance and therapeutic development (middlemiss2024molecularmotortugofwar pages 1-2).
2) **Quantitative imaging pipelines for shape mechanisms:**
   - **smVerCINI** for long-duration circumferential tracking of elongasome/MreB dynamics (middlemiss2024molecularmotortugofwar pages 1-2).
   - **FDAA labeling** (HADA) as a practical method to visualize PG synthesis patterns in vivo (reported experimental protocol) (dersch2024adaptationofbacillus pages 15-17).
3) **Reconstitution and synthetic-biology style “minimal systems”:** ZapD–FtsZ reconstituted toroids provide a controlled system to tune ring formation via crosslinking stoichiometry and filament geometry, informing efforts to reverse-engineer division ring mechanics (merinosalomon2025crosslinkingbyzapd pages 10-12).

---

## 6) Expert opinions / authoritative interpretations (from sources)

- **Stoichiometric window hypothesis (ZapD):** authors hypothesize that “functional, curved FtsZ macrostructures occurs only within a specific stoichiometric range” of ZapD–FtsZ interactions; excessive crosslinking yields rigid straight bundles (merinosalomon2025crosslinkingbyzapd pages 10-12). This is a direct, curation-relevant mechanistic claim, though currently **in vitro and preprint**.
- **Molecular motor tug-of-war model:** authors propose elongasome dynamics/processivity are regulated by a tug-of-war between oppositely oriented synthesis complexes associated with MreB filaments (middlemiss2024molecularmotortugofwar pages 1-2).
- **Ionic mediation model (osmotic response):** potassium ions are known to negatively affect MreB polymerization in vitro; authors interpret that MreB polymer disassembly is “directly mediated” by physical consequences of the osmotic stress response (dersch2024adaptationofbacillus pages 1-2).

---

## 7) Relevant statistics and quantitative data (from recent studies)

### Quantitative ring/toroid assembly parameters (ZapD–FtsZ)
- ZapD increases spacing between FtsZ filaments from **5.9 ± 0.8 nm** to **7.9 ± 2 nm** in toroids (merinosalomon2025crosslinkingbyzapd pages 10-12).
- Toroid-favoring binding stoichiometry: **0.3–0.4 mol ZapD per mol FtsZ** (≈ one ZapD dimer per 4–6 FtsZ molecules) (merinosalomon2025crosslinkingbyzapd pages 10-12).
- Bundle-favoring binding stoichiometry: **1.1 mol ZapD per mol FtsZ** (≈ one ZapD dimer per 2 FtsZ molecules) (merinosalomon2025crosslinkingbyzapd pages 10-12).
- Image-derived toroid dimensions and summary schematics are available from extracted figure panels (merinosalomon2025crosslinkingbyzapd media 2f2f3495, merinosalomon2025crosslinkingbyzapd media a57e5489, merinosalomon2025crosslinkingbyzapd media 22c0d621, merinosalomon2025crosslinkingbyzapd media 1d9bbab1).

### Quantitative elongasome/MreB geometry and prior limits (2024)
- MreB double filament length: **~170 nm**; monomer length **~5 nm**, implying **~68 subunits** per double filament (middlemiss2024molecularmotortugofwar pages 1-2).
- Prior elongasome processivity estimates: **400–600 nm** (noted as potentially TIRF-limited) (middlemiss2024molecularmotortugofwar pages 1-2).
- VerCINI imaging slice thickness: **~0.5 µm** (middlemiss2024molecularmotortugofwar pages 1-2).

### Division placement precision (divisome regulation context)
- FtsZ division positioning reported as “highly precise, with a **1% margin of error**” (bhambhani2020bacteriophagesp01gene pages 1-2).

---

## 8) Bibliography (DOI-first; with dates and URLs)

1. Middlemiss S, et al. **Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in Bacillus subtilis**. *Nature Communications*. **2024-06**. DOI: **10.1038/s41467-024-49785-x**. https://doi.org/10.1038/s41467-024-49785-x (middlemiss2024molecularmotortugofwar pages 1-2)
2. Dersch S, Graumann PL. **Adaptation of Bacillus subtilis MreB Filaments to Osmotic Stress Depends on Influx of Potassium Ions**. *Microorganisms*. **2024-06-27**. DOI: **10.3390/microorganisms12071309**. https://doi.org/10.3390/microorganisms12071309 (dersch2024adaptationofbacillus pages 1-2)
3. Schiller H, et al. **Identification of structural and regulatory cell-shape determinants in Haloferax volcanii**. *Nature Communications*. **2024-02**. DOI: **10.1038/s41467-024-45196-0**. https://doi.org/10.1038/s41467-024-45196-0 (schiller2024identificationofstructural pages 1-2)
4. Pöhl S, et al. **A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis**. *eLife*. **2024-01-31** (version of record). DOI: **10.7554/eLife.86577.2**. https://doi.org/10.7554/eLife.86577.2 (pohl2024adynamicbactofilin pages 1-2)
5. Bauda E, et al. **Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography**. *Nature Communications*. **2024-02** (accepted 2024-02-02). DOI: **10.1038/s41467-024-45770-6**. https://doi.org/10.1038/s41467-024-45770-6 (bauda2024ultrastructureofmacromolecular pages 1-2)
6. Bhambhani A, et al. **Bacteriophage SP01 Gene Product 56 Inhibits Bacillus subtilis Cell Division by Interacting with FtsL and Disrupting Pbp2B and FtsW Recruitment**. *Journal of Bacteriology*. **2020-12** (published 2020-12-18; cited as Jan 2021 issue). DOI: **10.1128/JB.00463-20**. https://doi.org/10.1128/JB.00463-20 (bhambhani2020bacteriophagesp01gene pages 1-2)
7. Merino-Salomón A, et al. **Crosslinking by ZapD drives the assembly of short FtsZ filaments into toroidal structures in solution**. *bioRxiv preprint* (posted 2023-01-12; version listed 2025). DOI: **10.1101/2023.01.12.523557**. https://doi.org/10.1101/2023.01.12.523557 (merinosalomon2025crosslinkingbyzapd pages 10-12)

---

## 9) Warnings / claims not yet ready for TraitMech curation

1) **Whole-cell toroidal morphology is under-supported in the retrieved evidence.** The strongest direct “ring/toroid” evidence concerns **protein rings** (FtsZ Z-ring) and **reconstituted FtsZ toroids** (ZapD), not naturally occurring toroidal cell bodies. Curate these as mechanistic precursors, not as direct determinants of METPO:1000680.
2) **Toroidal chromosome evidence must be excluded** from a cell-morphology causal graph unless the trait is explicitly expanded to “toroidal intracellular organization” (bauda2024ultrastructureofmacromolecular pages 1-2).
3) **Preprint status / in vitro conditions:** ZapD–FtsZ toroids are mechanistically strong but are **in vitro** and from a preprint; edges should be tagged as **assay-specific** and “uncertain for in vivo whole-cell ring phenotype” (merinosalomon2025crosslinkingbyzapd pages 10-12).
4) **Taxon-specific perturbations:** phage gp56 inhibition edges are Bacillus-/SP01-specific and should be tagged as perturbation/regulatory rather than core determinants (bhambhani2020bacteriophagesp01gene pages 1-2).


References

1. (bhambhani2020bacteriophagesp01gene pages 1-2): Amit Bhambhani, Isabella Iadicicco, Jules Lee, Syed Ahmed, Max Belfatto, David Held, Alexia Marconi, Aaron Parks, Charles R. Stewart, William Margolin, Petra Anne Levin, and Daniel P. Haeusser. Bacteriophage sp01 gene product 56 inhibits bacillus subtilis cell division by interacting with ftsl and disrupting pbp2b and ftsw recruitment. Journal of Bacteriology, Dec 2020. URL: https://doi.org/10.1128/jb.00463-20, doi:10.1128/jb.00463-20. This article has 18 citations and is from a peer-reviewed journal.

2. (middlemiss2024molecularmotortugofwar pages 1-2): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 20 citations and is from a highest quality peer-reviewed journal.

3. (bauda2024ultrastructureofmacromolecular pages 1-2): Elda Bauda, Benoit Gallet, Jana Moravcova, Gregory Effantin, Helena Chan, Jiri Novacek, Pierre-Henri Jouneau, Christopher D. A. Rodrigues, Guy Schoehn, Christine Moriscot, and Cecile Morlot. Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45770-6, doi:10.1038/s41467-024-45770-6. This article has 18 citations and is from a highest quality peer-reviewed journal.

4. (schiller2024identificationofstructural pages 1-2): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 36 citations and is from a highest quality peer-reviewed journal.

5. (merinosalomon2025crosslinkingbyzapd pages 10-12): Adrián Merino-Salomón, Jonathan Schneider, Leon Babl, Jan-Hagen Krohn, Marta Sobrinos-Sanguino, Tillman Schäfer, Juan R. Luque-Ortega, Carlos Alfonso, Mercedes Jiménez, Marion Jasnin, Petra Schwille, and Germán Rivas. Crosslinking by zapd drives the assembly of short ftsz filaments into toroidal structures in solution. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2023.01.12.523557, doi:10.1101/2023.01.12.523557. This article has 4 citations.

6. (dersch2024adaptationofbacillus pages 1-2): Simon Dersch and Peter L. Graumann. Adaptation of bacillus subtilis mreb filaments to osmotic stress depends on influx of potassium ions. Microorganisms, 12:1309, Jun 2024. URL: https://doi.org/10.3390/microorganisms12071309, doi:10.3390/microorganisms12071309. This article has 5 citations.

7. (pohl2024adynamicbactofilin pages 1-2): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

8. (merinosalomon2025crosslinkingbyzapd media 2f2f3495): Adrián Merino-Salomón, Jonathan Schneider, Leon Babl, Jan-Hagen Krohn, Marta Sobrinos-Sanguino, Tillman Schäfer, Juan R. Luque-Ortega, Carlos Alfonso, Mercedes Jiménez, Marion Jasnin, Petra Schwille, and Germán Rivas. Crosslinking by zapd drives the assembly of short ftsz filaments into toroidal structures in solution. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2023.01.12.523557, doi:10.1101/2023.01.12.523557. This article has 4 citations.

9. (merinosalomon2025crosslinkingbyzapd media a57e5489): Adrián Merino-Salomón, Jonathan Schneider, Leon Babl, Jan-Hagen Krohn, Marta Sobrinos-Sanguino, Tillman Schäfer, Juan R. Luque-Ortega, Carlos Alfonso, Mercedes Jiménez, Marion Jasnin, Petra Schwille, and Germán Rivas. Crosslinking by zapd drives the assembly of short ftsz filaments into toroidal structures in solution. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2023.01.12.523557, doi:10.1101/2023.01.12.523557. This article has 4 citations.

10. (merinosalomon2025crosslinkingbyzapd media 22c0d621): Adrián Merino-Salomón, Jonathan Schneider, Leon Babl, Jan-Hagen Krohn, Marta Sobrinos-Sanguino, Tillman Schäfer, Juan R. Luque-Ortega, Carlos Alfonso, Mercedes Jiménez, Marion Jasnin, Petra Schwille, and Germán Rivas. Crosslinking by zapd drives the assembly of short ftsz filaments into toroidal structures in solution. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2023.01.12.523557, doi:10.1101/2023.01.12.523557. This article has 4 citations.

11. (merinosalomon2025crosslinkingbyzapd media 1d9bbab1): Adrián Merino-Salomón, Jonathan Schneider, Leon Babl, Jan-Hagen Krohn, Marta Sobrinos-Sanguino, Tillman Schäfer, Juan R. Luque-Ortega, Carlos Alfonso, Mercedes Jiménez, Marion Jasnin, Petra Schwille, and Germán Rivas. Crosslinking by zapd drives the assembly of short ftsz filaments into toroidal structures in solution. bioRxiv, Jun 2025. URL: https://doi.org/10.1101/2023.01.12.523557, doi:10.1101/2023.01.12.523557. This article has 4 citations.

12. (dersch2024adaptationofbacillus pages 15-17): Simon Dersch and Peter L. Graumann. Adaptation of bacillus subtilis mreb filaments to osmotic stress depends on influx of potassium ions. Microorganisms, 12:1309, Jun 2024. URL: https://doi.org/10.3390/microorganisms12071309, doi:10.3390/microorganisms12071309. This article has 5 citations.