---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:33:35.399349'
end_time: '2026-06-17T22:42:41.670145'
duration_seconds: 546.27
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: hyperthermophilic
  trait_identifier: METPO:1000617
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: hyperthermophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature preference in which growth is favored at very high temperatures,\
    \ typically \u226580 \xB0C."
  parent_traits: METPO:1000613
  synonyms: extreme thermophilic
  evidence_summary: "DOI:10.1111/j.1574-6976.1996.tb00233.x: optimal growth temperatures\
    \ between 80\xB0C and 110\xB0C (Supports hyperthermophile growth at very high\
    \ temperatures.) | PMID:9348040: hyperthermophilic archaeon, Pyrococcus furiosus\
    \ (Organism example: Pyrococcus furiosus is described as hyperthermophilic.)"
  causal_graph_summary: 'hyperthermophilic_thermostability: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** hyperthermophilic
- **METPO identifier:** METPO:1000617
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at very high temperatures, typically ≥80 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** extreme thermophilic
- **Existing evidence:** DOI:10.1111/j.1574-6976.1996.tb00233.x: optimal growth temperatures between 80°C and 110°C (Supports hyperthermophile growth at very high temperatures.) | PMID:9348040: hyperthermophilic archaeon, Pyrococcus furiosus (Organism example: Pyrococcus furiosus is described as hyperthermophilic.)
- **Existing causal graph summary:** hyperthermophilic_thermostability: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **hyperthermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/hyperthermophilic.yaml`.

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
- **Trait label:** hyperthermophilic
- **METPO identifier:** METPO:1000617
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at very high temperatures, typically ≥80 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** extreme thermophilic
- **Existing evidence:** DOI:10.1111/j.1574-6976.1996.tb00233.x: optimal growth temperatures between 80°C and 110°C (Supports hyperthermophile growth at very high temperatures.) | PMID:9348040: hyperthermophilic archaeon, Pyrococcus furiosus (Organism example: Pyrococcus furiosus is described as hyperthermophilic.)
- **Existing causal graph summary:** hyperthermophilic_thermostability: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **hyperthermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/hyperthermophilic.yaml`.

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


# Research Report: Hyperthermophilic Microbial Trait (METPO:1000617)

## 1) Scope summary (trait meaning, boundaries, assays)

**Trait definition and operationalization.** The METPO:1000617 trait *hyperthermophilic* denotes a temperature preference in which **growth is favored at very high temperatures, typically ≥80 °C**. A recent extremophile review explicitly classifies hyperthermophiles as organisms that “**grow above 80 °C**” (rekadwad2023extremophilesthespecies pages 2-4). In mechanistic and systems studies, hyperthermophily is typically operationalized using **growth-rate vs. temperature curves** and derived metrics such as **optimal growth temperature (Topt)** and maximum growth temperature (Tmax).

**Boundary cases / nearby traits.** The same source distinguishes “strict thermophile” (Topt 65–80 °C) from hyperthermophile (>80 °C) (rekadwad2023extremophilesthespecies pages 2-4). A heat-shock systems study in *Sulfolobus acidocaldarius* states it thrives with **optimal growth at 75 °C** (thermophilic/thermoacidophilic; adjacent to the hyperthermophile boundary) (baes2023transcriptionalandtranslational pages 1-2). By contrast, *Pyrococcus furiosus* is treated as a **hyperthermophilic archaeon**; it can “**grow … from 70 °C to 104 °C**” (grunberger2023uncoveringthetemporal pages 1-2), and is experimentally cultivated at **Topt ~95 °C** in thermal stress experiments (grunberger2023uncoveringthetemporal pages 10-12).

**Upper-limit exemplars (Tmax).** Reported upper growth/survival temperatures include *Pyrolobus fumarii* “**106 to 113 °C**” and *Methanopyrus kandleri* “**up to 122 °C**” (rekadwad2023extremophilesthespecies pages 2-4). These values are useful for trait boundary validation and for anchoring extreme ends of the hyperthermophilic phenotype.

## 2) Key concepts and current mechanistic understanding (candidate causal graph entities)

Hyperthermophily is typically understood as an emergent property arising from **(i) macromolecule stabilization (DNA/RNA/proteins), (ii) proteostasis and stress regulation, (iii) membrane architecture and lipid remodeling, and (iv) cytosolic solute chemistry (compatible solutes/extremolytes)**, all interacting with the environmental factor **high temperature**.

### Candidate nodes (grouped by type) with ontology grounding suggestions

**Environmental / experimental factors**
- High temperature / elevated growth temperature (ENVO label candidate)
- Heat shock (temperature upshift; GO:0009408 *response to heat* candidate)
- Hydrothermal vents / geothermal hot springs (ENVO candidates; context for natural hyperthermophiles)
- Pressure (high/low hydrostatic pressure; ENVO candidate; relevant to lipid shifts) (taubner2023lipidomicsandcomparative pages 11-12)

**Organisms / taxa (examples and models)**
- *Pyrococcus furiosus* (NCBITaxon:2261) (grunberger2023uncoveringthetemporal pages 1-2)
- *Methanopyrus kandleri* (NCBITaxon candidate) (rekadwad2023extremophilesthespecies pages 2-4)
- *Pyrolobus fumarii* (NCBITaxon candidate) (rekadwad2023extremophilesthespecies pages 2-4)
- Archaeoglobi (e.g., *Archaeoglobus profundus*, *A. fulgidus*) (NCBITaxon candidates) (garcia2024identificationoftwo pages 6-7)
- Thermoproteales example: *Vulcanisaeta distributa* (NCBITaxon candidate) (garcia2024identificationoftwo pages 6-7)

**Genes / proteins / complexes (proteostasis, regulation, DNA topology, lipid biosynthesis)**
- **Reverse gyrase** (enzyme; creates positive DNA supercoils) (grunberger2023uncoveringthetemporal pages 1-2)
- Reverse gyrase **TopR1** (gene/protein label in Sulfolobales context) (baes2023transcriptionalandtranslational pages 1-2)
- **Thermosome** (archaeal group II chaperonin; complex) (grunberger2023uncoveringthetemporal pages 10-12, baes2023transcriptionalandtranslational pages 1-2)
- Small heat shock proteins (sHSPs) and **prefoldin** (protein folding/holding factors) (baes2023transcriptionalandtranslational pages 1-2)
- **Phr** transcriptional regulator (heat shock orchestrator in *P. furiosus*) (grunberger2023uncoveringthetemporal pages 1-2)
- **VAT1** (AAA+ ATPase/proteostasis factor induced in heat shock in *P. furiosus*) (grunberger2023uncoveringthetemporal pages 10-12)

**Membrane lipids and lipid-modifying enzymes**
- GDGTs: glycerol dialkyl glycerol tetraethers (lipid class; used as biomarkers and membrane-spanning lipids) (garcia2024identificationoftwo pages 1-2)
- GMGTs: glycerol monoalkyl glycerol tetraethers (aka H-GDGTs; cross-linked tails) (garcia2024identificationoftwo pages 1-2)
- **Gms** (GMGT synthase; radical SAM enzyme catalyzing C–C cross-link formation) (li2024biosynthesisofgmgt pages 2-3, garcia2024identificationoftwo pages 1-2)
- **Gmm** (GMGT methylase; adds methyl groups to GMGTs) (garcia2024identificationoftwo pages 1-2)
- Macrocyclic archaeol (diether lipid; affects permeability/rigidity) (taubner2023lipidomicsandcomparative pages 11-12)

**Compatible solutes / extremolytes (cytosolic chemistry and macromolecule protection)**
- **Di-myo-inositol-phosphate (DIP)** (CHEBI candidate; compatible solute) (grunberger2023uncoveringthetemporal pages 10-12)
- Myo-inositol-1-phosphate synthase (PF1616 in *P. furiosus*; DIP precursor biosynthesis enzyme) (grunberger2023uncoveringthetemporal pages 10-12)
- **Cyclic 2,3-diphosphoglycerate (cDPG)** (CHEBI candidate; extremolyte) (rose2023structuralcharacterizationof pages 1-2, rose2023structuralcharacterizationof pages 2-4)
- cDPG biosynthetic enzyme: cyclic di-phosphoglycerate synthetase (cDPGS; enzyme node) (rose2023structuralcharacterizationof pages 1-2)

## 3) Recent developments (2023–2024 prioritized)

### 3.1 Systems biology of hyperthermophile thermal stress (2023)
A 2023 multi-omics study in the model hyperthermophile *Pyrococcus furiosus* quantified genome-wide response to thermal shocks. The organism is described as adapted to “**temperatures exceeding 80 °C**” and able to grow **70–104 °C** (grunberger2023uncoveringthetemporal pages 1-2). Under a 5-minute **heat shock at 105 °C** (growth-inhibiting), ~68% of the transcriptome changed (grunberger2023uncoveringthetemporal pages 10-12), and classic proteostasis factors were induced including **thermosome**, **HSP20**, and **VAT1** (grunberger2023uncoveringthetemporal pages 10-12). The study also directly links hyperthermophily to DNA topology stabilization, noting “**positive DNA supercoiling by reverse gyrase**” (grunberger2023uncoveringthetemporal pages 1-2), and identifies transcriptional control by **Phr** (“Heat shock … orchestrated by … Phr”) (grunberger2023uncoveringthetemporal pages 1-2).

### 3.2 Archaeal heat-shock machinery in a thermoacidophile near the hyperthermophile boundary (2023)
A 2023 study in *Sulfolobus acidocaldarius* (Topt 75 °C) demonstrates a profound reduction in transcription/translation after upshift to 86 °C, while still allowing neosynthesis (baes2023transcriptionalandtranslational pages 1-2). Mechanistically, it describes a canonical archaeal proteostasis pipeline in which “**Small HSPs (sHSPs) and prefoldin… shuttle them to the… thermosome**” (baes2023transcriptionalandtranslational pages 1-2) and notes DNA-topology adaptation via “**reverse gyrase TopR1**” (baes2023transcriptionalandtranslational pages 1-2). While *S. acidocaldarius* is not strictly hyperthermophilic by the ≥80 °C criterion, the described molecular modules are directly relevant candidate nodes for hyperthermophile causal graphs (with appropriate boundary warnings).

### 3.3 Mechanistic elucidation of GMGT lipid biosynthesis and temperature dependence (2024)
Two 2024 studies provide major advances in the **biochemistry and physiology of archaeal membrane-spanning lipids**:

- **Enzymology of GMGT formation (Nature Communications, 2024).** A radical SAM enzyme termed **GMGT synthase (Gms)** is shown to catalyze formation of a C–C linkage between GDGT isoprenoid chains: “**Gms catalyzes the formation of a C–C linkage between two isoprenoid chains on GDGT-0 to produce GMGT-0**” (li2024biosynthesisofgmgt pages 2-3). The paper also summarizes a prevailing physiological model: GMGTs “**are thought to contribute to increased membrane rigidity at high temperature**” (li2024biosynthesisofgmgt pages 1-2). (Li et al., received 18 Jan 2024; accepted 11 Jun 2024) (li2024biosynthesisofgmgt pages 1-2).

- **Gms/Gmm discovery and temperature-response lipidomics (PNAS, 2024).** A PNAS 2024 study identifies **Gms** (required for GMGT cross-link) and **Gmm** (GMGT methylase) and shows via culturing that “**GMGT production and methylation increases with elevated temperatures**” (garcia2024identificationoftwo pages 1-2). Quantitatively, in *Archaeoglobus profundus* GMGTs increase with temperature, “**accounting for >90% of total monolayer lipids at 90 °C**” (garcia2024identificationoftwo pages 6-7), and Figure 5 provides a visual, temperature-stratified summary of this relationship (garcia2024identificationoftwo media 97b87a64).

### 3.4 Extremolyte cDPG: distribution, concentration ranges, and protective roles (2023)
A 2023 structural/biochemical study of cyclic di-phosphoglycerate synthetase contextualizes **cDPG** as an extremolyte “**exclusively found in the hyperthermophilic archaeal methanogens**” (rose2023structuralcharacterizationof pages 1-2, rose2023structuralcharacterizationof pages 2-4). It provides quantitative intracellular concentration ranges (0.3–1.1 M) and states that **cDPG biosynthesis is temperature-triggered** (“**triggered by an increase in the growth temperature**”) (rose2023structuralcharacterizationof pages 2-4). It also links cDPG to molecular protection: “**increases the thermostability of archaeal proteins**” and “**protects the DNA against oxidative damage caused by hydroxyl radicals**” (rose2023structuralcharacterizationof pages 1-2).

## 4) Current applications and real-world implementations

**Biotechnology platform uses of hyperthermophiles and their biomolecules**
- **Extremolyte production.** cDPG is highlighted as an “unusual extremolyte… [with] important industrial applications” (rose2023structuralcharacterizationof pages 1-2). The same work notes a previously established process using *Thermus thermophilus* as a “whole-cell factory” for cDPG production (rose2023structuralcharacterizationof pages 1-2), supporting a real-world implementation pathway for extremolyte manufacturing.
- **Lipid biomarkers and engineered lipid biology.** GMGT/GDGT lipid chemistry has direct applications as biomarkers and as targets for synthetic biology/biophysical studies. The PNAS 2024 work frames GDGT modifications as adaptive responses and connects them to paleotemperature proxies and membrane stress physiology (garcia2024identificationoftwo pages 1-2), and provides culturing evidence linking lipid composition to temperature (garcia2024identificationoftwo pages 6-7).
- **Industrial enzyme discovery/production using archaeal hosts.** Thermophilic archaea such as *Sulfolobus acidocaldarius* are described as recombinant protein production platforms (baes2023transcriptionalandtranslational pages 1-2), and hyperthermophilic proteins are noted to be amenable to purification via heat precipitation in archaeal expression contexts (grunberger2023uncoveringthetemporal pages 10-12).

## 5) Relevant statistics and data points from recent studies

- **Trait threshold:** hyperthermophile “grow above 80 °C” (rekadwad2023extremophilesthespecies pages 2-4).
- ***P. furiosus* growth range:** 70–104 °C (grunberger2023uncoveringthetemporal pages 1-2); cultivated at Topt 95 °C in stress study (grunberger2023uncoveringthetemporal pages 10-12).
- **Thermal-stress transcriptome scale:** 5-min heat shock at 105 °C changes ~68% of transcripts (330 up >2-fold; 411 down >2-fold) in *P. furiosus* (grunberger2023uncoveringthetemporal pages 10-12).
- **cDPG concentration trend with organism Topt:** 70 mM (*M. thermoautotrophicum*, 65 °C) to 300 mM (*M. fervidus*, 84 °C) to 1 M (*M. kandleri*, 98 °C) (rose2023structuralcharacterizationof pages 2-4).
- **GMGT temperature response (culture lipidomics):** GMGT relative abundance increases with growth temperature in multiple archaea; in *A. profundus* reaches “>90%… at 90 °C”; in *V. distributa* “>20%… at 99 °C” (garcia2024identificationoftwo pages 6-7), visualized in Fig. 5 (garcia2024identificationoftwo media 97b87a64).
- **Methanogen lipidome quantitative physiology:** *Methanocaldococcus villosus* had higher total lipid production rate under standard conditions (127.7 ± 18.5 nmol g−1 h−1) vs *M. okinawensis* (27.4 ± 7.0) and *M. marburgensis* (17.7 ± 1.2) (taubner2023lipidomicsandcomparative pages 11-12). The study summarizes a general trend that diether lipids adapt to lower temperatures/higher pressures, with tetraether lipids favored under the inverse conditions (taubner2023lipidomicsandcomparative pages 11-12).

## 6) Candidate causal edges for TraitMech curation

The following table is designed for direct transfer into a TraitMech/TraitMech-like YAML curation workflow.

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet (verbatim short quote) | Source | Notes on scope/uncertainty | Suggested confidence |
|---|---|---|---|---|---|---|
| hyperthermophilic (METPO:1000617) | defined_as_growth_above | 80 degree Celsius (CHEBI:46645) | "hyperthermophile (grow above 80 °C)" (rekadwad2023extremophilesthespecies pages 2-4) | Rekadwad 2023, doi:10.1007/s13205-023-03733-6, https://doi.org/10.1007/s13205-023-03733-6, Aug 2023 | Direct trait definition from review; broad but not mechanism-specific | high |
| Pyrolobus fumarii (NCBITaxon candidate) | has_maximum_growth_temperature | 106–113 degree Celsius (label) | "Pyrolobus fumarii can survive from 106 to 113 °C" (rekadwad2023extremophilesthespecies pages 2-4) | Rekadwad 2023, doi:10.1007/s13205-023-03733-6, https://doi.org/10.1007/s13205-023-03733-6, Aug 2023 | Organism-specific exemplar for upper thermal limit; survival/growth wording from review | medium |
| Methanopyrus kandleri strain 116 (NCBITaxon candidate) | has_maximum_growth_temperature | 122 degree Celsius (label) | "Methanopyrus kandleri strain 116 can grow up to 122 °C" (rekadwad2023extremophilesthespecies pages 2-4) | Rekadwad 2023, doi:10.1007/s13205-023-03733-6, https://doi.org/10.1007/s13205-023-03733-6, Aug 2023 | Organism-specific exemplar; useful boundary case for hyperthermophily | high |
| Pyrococcus furiosus (NCBITaxon:2261) | has_growth_range | 70–104 degree Celsius (label) | "grow over a broad temperature range from 70°C to 104°C" (grunberger2023uncoveringthetemporal pages 1-2) | Grünberger 2023, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23, Dec 2023 | Taxon-specific but directly measured/quoted in model hyperthermophile | high |
| hyperthermophilic archaea (label) | associated_with | positive DNA supercoiling by reverse gyrase (GO candidate) | "positive DNA supercoiling by reverse gyrase" (grunberger2023uncoveringthetemporal pages 1-2) | Grünberger 2023, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23, Dec 2023 | General adaptation statement in introduction/review framing; not direct perturbation experiment | medium |
| heat shock at 105°C (label) | upregulates | myo-inositol-1-phosphate synthase PF1616 (gene/protein label) | "Myo-inositol-1-phosphate synthase (PF1616, log2FC: 4.0)" (grunberger2023uncoveringthetemporal pages 10-12) | Grünberger 2023, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23, Dec 2023 | Assay-specific to P. furiosus heat shock; supports precursor biosynthesis response | high |
| myo-inositol-1-phosphate synthase PF1616 (gene/protein label) | participates_in_biosynthesis_of | di-myo-inositol-phosphate (CHEBI candidate) | "catalyzing a precursor of the compatible solute Di-myo-inositol-phosphate (DIP)" (grunberger2023uncoveringthetemporal pages 10-12) | Grünberger 2023, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23, Dec 2023 | Indirect edge via precursor formation; not full pathway curation | medium |
| di-myo-inositol-phosphate (CHEBI candidate) | stabilizes | proteins (GO:0006457 candidate / label) | "DIP is suggested to have a protein-stabilizing role in hyperthermophiles" (grunberger2023uncoveringthetemporal pages 10-12) | Grünberger 2023, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23, Dec 2023 | Explicitly framed as suggested; keep as uncertain/general | medium |
| Phr transcriptional regulator (gene/protein label) | regulates | heat shock response genes (GO:0009408 candidate / label) | "Heat shock triggers extensive transcriptome reprogramming, orchestrated by the transcriptional regulator Phr" (grunberger2023uncoveringthetemporal pages 1-2) | Grünberger 2023, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23, Dec 2023 | Taxon-specific to P. furiosus; strong regulatory evidence | high |
| heat shock at 105°C (label) | upregulates | thermosome (archaeal group II chaperonin complex; GO candidate) | "thermosome (log2FC: 2.7)" (grunberger2023uncoveringthetemporal pages 10-12) | Grünberger 2023, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23, Dec 2023 | Assay-specific transcript response in P. furiosus | high |
| heat shock at 105°C (label) | upregulates | HSP20 (protein label) | "HSP20 (log2FC: 5.4)" (grunberger2023uncoveringthetemporal pages 10-12) | Grünberger 2023, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23, Dec 2023 | Assay-specific transcript response | high |
| heat shock at 105°C (label) | upregulates | VAT1 AAA ATPase/proteostasis factor (protein label) | "VAT1 (log2FC: 6.7)" (grunberger2023uncoveringthetemporal pages 10-12) | Grünberger 2023, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23, Dec 2023 | Assay-specific; useful proteostasis node | high |
| heat shock (label) | induces | altered lipid composition of cytoplasmic membrane (GO/label) | "heat shock response leads to an altered lipid composition of the cytoplasmic membrane" (baes2023transcriptionalandtranslational pages 1-2) | Baes 2023, doi:10.1128/mbio.03593-22, https://doi.org/10.1128/mbio.03593-22, Oct 2023 | Thermoacidophile S. acidocaldarius, not hyperthermophile by strict >80°C definition; neighboring trait evidence | medium |
| small HSPs and prefoldin (protein labels) | shuttle_substrates_to | thermosome (archaeal group II chaperonin complex; GO candidate) | "Small HSPs (sHSPs) and prefoldin... shuttle them to the HSP60-type group II chaperonin complex, also referred to as the thermosome" (baes2023transcriptionalandtranslational pages 1-2) | Baes 2023, doi:10.1128/mbio.03593-22, https://doi.org/10.1128/mbio.03593-22, Oct 2023 | Mechanistic edge from thermophilic Sulfolobales; may generalize to hyperthermophiles but keep moderate confidence | medium |
| reverse gyrase TopR1 (gene/protein label) | increases | positive DNA supercoiling (GO candidate) | "increased DNA positive supercoiling via reverse gyrase TopR1" (baes2023transcriptionalandtranslational pages 1-2) | Baes 2023, doi:10.1128/mbio.03593-22, https://doi.org/10.1128/mbio.03593-22, Oct 2023 | Mechanistic statement in Sulfolobales heat-shock context; supports DNA topology node | high |
| cyclic 2,3-diphosphoglycerate (cDPG; CHEBI candidate) | found_exclusively_in | hyperthermophilic archaeal methanogens (label) | "cDPG has been exclusively found in the hyperthermophilic archaeal methanogens" (rose2023structuralcharacterizationof pages 1-2, rose2023structuralcharacterizationof pages 2-4) | De Rose 2023, doi:10.3389/fmicb.2023.1267570, https://doi.org/10.3389/fmicb.2023.1267570, Nov 2023 | Strong scope statement but taxonomically narrow (methanogens) | high |
| cyclic 2,3-diphosphoglycerate (cDPG; CHEBI candidate) | increases_thermostability_of | archaeal proteins (label) | "Its presence increases the thermostability of archaeal proteins" (rose2023structuralcharacterizationof pages 1-2) | De Rose 2023, doi:10.3389/fmicb.2023.1267570, https://doi.org/10.3389/fmicb.2023.1267570, Nov 2023 | Good mechanistic node for thermoprotection; compound-specific | high |
| cyclic 2,3-diphosphoglycerate (cDPG; CHEBI candidate) | protects | DNA from hydroxyl-radical oxidative damage (GO/label) | "protects the DNA against oxidative damage caused by hydroxyl radicals" (rose2023structuralcharacterizationof pages 1-2) | De Rose 2023, doi:10.3389/fmicb.2023.1267570, https://doi.org/10.3389/fmicb.2023.1267570, Nov 2023 | Mechanistic protection edge; likely relevant under combined heat/oxidative stress | high |
| increased growth temperature (label) | triggers_biosynthesis_of | cDPG (CHEBI candidate) | "cDPG biosynthesis is triggered by an increase in the growth temperature" (rose2023structuralcharacterizationof pages 2-4) | De Rose 2023, doi:10.3389/fmicb.2023.1267570, https://doi.org/10.3389/fmicb.2023.1267570, Nov 2023 | Strong environmental trigger edge in hyperthermophilic methanogens | high |
| optimum growth temperature (label) | positively_correlates_with | intracellular cDPG concentration (label) | "The accumulation of this extremolyte in the cells is correlated with the optimum growth temperature... 70 mM... 300 mM... 1 M" (rose2023structuralcharacterizationof pages 2-4) | De Rose 2023, doi:10.3389/fmicb.2023.1267570, https://doi.org/10.3389/fmicb.2023.1267570, Nov 2023 | Cross-species comparative correlation; useful quantitative pattern, not single-organism causality | medium |
| Gms / GMGT synthase (protein label) | catalyzes_formation_of | C(sp3)-C(sp3) linkage in GMGT (reaction/process label) | "Gms catalyzes the formation of a C–C linkage between two isoprenoid chains on GDGT-0 to produce GMGT-0" (li2024biosynthesisofgmgt pages 2-3) | Li 2024, doi:10.1038/s41467-024-49650-x, https://doi.org/10.1038/s41467-024-49650-x, Jun 2024 | Direct enzymology, strong for edge from gene/protein to lipid modification | high |
| GMGTs (lipid class label) | contribute_to | increased membrane rigidity at high temperature (label) | "are thought to contribute to increased membrane rigidity at high temperature" (li2024biosynthesisofgmgt pages 1-2) | Li 2024, doi:10.1038/s41467-024-49650-x, https://doi.org/10.1038/s41467-024-49650-x, Jun 2024 | Explicitly phrased as thought to; mechanism plausible but partly inferential | medium |
| elevated growth temperature (label) | increases_production_of | GMGTs (lipid class label) | "GMGT production and methylation increases with elevated temperatures" (garcia2024identificationoftwo pages 1-2) | Garcia 2024, doi:10.1073/pnas.2318761121, https://doi.org/10.1073/pnas.2318761121, Jun 17 2024 | Broad conclusion across three cultured archaea; strong trait-mechanism relevance | high |
| Gms (protein label) | required_for | GMGT cross-link formation (reaction/process label) | "Gms, that is required to form the bridging cross-link of a GMGT" (garcia2024identificationoftwo pages 1-2) | Garcia 2024, doi:10.1073/pnas.2318761121, https://doi.org/10.1073/pnas.2318761121, Jun 17 2024 | Direct functional assignment via heterologous expression/genetics | high |
| Gmm (protein label) | adds_methyl_groups_to | GMGTs (lipid class label) | "a second protein, Gmm, that adds additional methyl groups to this unique lipid" (garcia2024identificationoftwo pages 1-2) | Garcia 2024, doi:10.1073/pnas.2318761121, https://doi.org/10.1073/pnas.2318761121, Jun 17 2024 | Direct functional assignment; methylation role may vary by lineage | high |
| increasing growth temperature (label) | increases_relative_abundance_of | GMGTs in Archaeoglobus profundus (NCBITaxon candidate) | "GMGTs gradually increase in their relative abundance with increased growth temperature, eventually becoming dominant over GDGTs and accounting for >90% of total monolayer lipids at 90 °C" (garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo media 97b87a64) | Garcia 2024, doi:10.1073/pnas.2318761121, https://doi.org/10.1073/pnas.2318761121, Jun 17 2024 | Strong quantitative, taxon-specific culture evidence | high |
| increasing growth temperature (label) | increases_relative_abundance_of | GMGTs in Vulcanisaeta distributa (NCBITaxon candidate) | "GMGT production increases with temperature and accounts for >20% of monolayer lipids at the highest growth temperature of 99 °C" (garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo media 97b87a64) | Garcia 2024, doi:10.1073/pnas.2318761121, https://doi.org/10.1073/pnas.2318761121, Jun 17 2024 | Strong quantitative, taxon-specific evidence | high |
| increasing growth temperature (label) | increases | GMGT methylation index in Vulcanisaeta distributa (label) | "increased at higher growth temperatures in V. distributa from an MI = 0.09 (±0.01) at 85 °C to an MI = 0.34 (±0.01) at 99 °C" (garcia2024identificationoftwo pages 6-7) | Garcia 2024, doi:10.1073/pnas.2318761121, https://doi.org/10.1073/pnas.2318761121, Jun 17 2024 | Quantitative but taxon-specific; physiological interpretation uncertain | medium |
| lower temperature and higher pressure (ENVO candidate / label) | favor_production_of | diether lipids / archaeol (lipid class label) | "diether lipid production seems to be a membrane lipid adaption to lower temperatures and higher pressures" (taubner2023lipidomicsandcomparative pages 11-12) | Taubner 2023, doi:10.1128/msystems.01159-22, https://doi.org/10.1128/msystems.01159-22, Apr 2023 | Generalized from comparative methanogen study and prior literature; environmental tradeoff edge | medium |
| high temperature and low pressure (ENVO candidate / label) | favor_production_of | tetraether membrane lipids (GDGT/GMGT; lipid class label) | "vice versa for the production of tetraether membrane lipids" and "tetraether lipids were increased with low pressure and high temperatures" (taubner2023lipidomicsandcomparative pages 11-12) | Taubner 2023, doi:10.1128/msystems.01159-22, https://doi.org/10.1128/msystems.01159-22, Apr 2023 | Broad adaptation trend; partly synthesized from current and cited prior studies | medium |
| macrocyclic archaeol (lipid class label) | decreases | water permeability (GO/label) | "macrocyclization leads to decreased water permeability" (taubner2023lipidomicsandcomparative pages 11-12) | Taubner 2023, doi:10.1128/msystems.01159-22, https://doi.org/10.1128/msystems.01159-22, Apr 2023 | Based on vesicle/tubule experiments with synthetic archaeon-type phosphatidylcholines; assay-derived | medium |
| macrocyclic archaeol (lipid class label) | increases | membrane stability and rigidity (GO/label) | "could increase overall membrane stability and rigidity and reduce membrane fluidity" (taubner2023lipidomicsandcomparative pages 11-12) | Taubner 2023, doi:10.1128/msystems.01159-22, https://doi.org/10.1128/msystems.01159-22, Apr 2023 | Mechanistic inference from model membranes and comparative cultures; useful but indirect | medium |


*Table: This table lists curation-ready candidate causal edges for the hyperthermophilic trait, linking environmental temperature preference to specific molecular mechanisms, lipids, regulators, and protective solutes. It is designed to support TraitMech graph construction with source quotes, scope notes, and confidence ratings.*

### Visual evidence (temperature-linked GMGT remodeling)
Figure 5 from Garcia et al. (PNAS 2024) shows stacked-bar lipidome shifts across growth temperatures in *A. fulgidus*, *A. profundus*, and *V. distributa*, illustrating increased GMGT fractions at higher temperatures (garcia2024identificationoftwo media 97b87a64).

## 7) Expert opinions and analysis (authoritative interpretations)

- **Reverse gyrase as a hyperthermophile-associated DNA topology strategy.** The *P. furiosus* study frames hyperthermophily as involving increased nucleoid-associated proteins and “positive DNA supercoiling by reverse gyrase” (grunberger2023uncoveringthetemporal pages 1-2). This supports curating reverse gyrase as a candidate mechanistic node/edge, but the statement is largely contextual (introductory) rather than a direct perturbation.
- **Membrane-spanning lipid modifications as adaptive stress responses.** The PNAS 2024 study explicitly positions GDGT modifications as aiding survival under “extreme environmental conditions such as high temperatures” (garcia2024identificationoftwo pages 1-2), and provides direct culture evidence that GMGT increases with growth temperature (garcia2024identificationoftwo pages 6-7).
- **Extremolytes as multi-target stabilizers.** The cDPG study places extremolytes within the broader framework that osmolytes increase thermodynamic stability of proteins/nucleic acids without compromising activity, and then provides direct cDPG-specific claims for protein thermostability and DNA protection (rose2023structuralcharacterizationof pages 1-2).

## 8) Curation warnings (what should *not* yet be curated as strong edges)

1. **Generalized “hyperthermophile hallmarks” without direct causal tests.** Statements such as “positive DNA supercoiling by reverse gyrase” as a hyperthermophile adaptation are compelling but often appear as background generalizations; curate as **medium-confidence** unless supported by organism-specific genetic/biochemical perturbation evidence in the same source (grunberger2023uncoveringthetemporal pages 1-2).
2. **Mechanistic interpretations phrased as “thought to” or “suggested.”** For example, GMGTs “are thought to contribute to increased membrane rigidity at high temperature” (li2024biosynthesisofgmgt pages 1-2), and DIP is “suggested” to stabilize proteins (grunberger2023uncoveringthetemporal pages 10-12). These are valuable but should be marked **inferred/uncertain** unless paired with direct biophysical assays.
3. **Trait-boundary mismatch.** *Sulfolobus acidocaldarius* (Topt 75 °C) is thermophilic/thermoacidophilic rather than strictly hyperthermophilic; its heat-shock modules are still relevant, but edges derived from it should be flagged as **adjacent-trait evidence** rather than definitive hyperthermophile-only mechanisms (baes2023transcriptionalandtranslational pages 1-2).

---

# DOI-first bibliography (with URLs and publication dates where available)

1. Rekadwad BN et al. **Extremophiles: the species that evolve and survive under hostile conditions.** *3 Biotech* (Aug 2023). DOI: **10.1007/s13205-023-03733-6**. URL: https://doi.org/10.1007/s13205-023-03733-6 (rekadwad2023extremophilesthespecies pages 2-4)
2. Grünberger F et al. **Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics.** *mBio* (Dec 2023). DOI: **10.1128/mbio.02174-23**. URL: https://doi.org/10.1128/mbio.02174-23 (grunberger2023uncoveringthetemporal pages 10-12, grunberger2023uncoveringthetemporal pages 1-2)
3. Baes R et al. **Transcriptional and translational dynamics underlying heat shock response in the thermophilic crenarchaeon *Sulfolobus acidocaldarius*.** *mBio* (Oct 2023). DOI: **10.1128/mbio.03593-22**. URL: https://doi.org/10.1128/mbio.03593-22 (baes2023transcriptionalandtranslational pages 1-2)
4. De Rose SA et al. **Structural characterization of a novel cyclic 2,3-diphosphoglycerate synthetase involved in extremolyte production in the archaeon *Methanothermus fervidus*.** *Frontiers in Microbiology* (Published 16 Nov 2023). DOI: **10.3389/fmicb.2023.1267570**. URL: https://doi.org/10.3389/fmicb.2023.1267570 (rose2023structuralcharacterizationof pages 1-2, rose2023structuralcharacterizationof pages 2-4)
5. Taubner R-S et al. **Lipidomics and Comparative Metabolite Excretion Analysis of Methanogenic Archaea Reveal Organism-Specific Adaptations to Varying Temperatures and Substrate Concentrations.** *mSystems* (Apr 2023). DOI: **10.1128/msystems.01159-22**. URL: https://doi.org/10.1128/msystems.01159-22 (taubner2023lipidomicsandcomparative pages 11-12)
6. Li Y et al. **Biosynthesis of GMGT lipids by a radical SAM enzyme associated with anaerobic archaea and oxygen-deficient environments.** *Nature Communications* (Accepted 11 Jun 2024; received 18 Jan 2024). DOI: **10.1038/s41467-024-49650-x**. URL: https://doi.org/10.1038/s41467-024-49650-x (li2024biosynthesisofgmgt pages 1-2, li2024biosynthesisofgmgt pages 2-3)
7. Garcia AA et al. **Identification of two archaeal GDGT lipid–modifying proteins reveals diverse microbes capable of GMGT biosynthesis and modification.** *PNAS* (Published 17 Jun 2024). DOI: **10.1073/pnas.2318761121**. URL: https://doi.org/10.1073/pnas.2318761121 (garcia2024identificationoftwo pages 1-2, garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo media 97b87a64)


References

1. (rekadwad2023extremophilesthespecies pages 2-4): Bhagwan Narayan Rekadwad, Wen-Jun Li, Juan M. Gonzalez, Rekha Punchappady Devasya, Arun Ananthapadmanabha Bhagwath, Ruchi Urana, and Khalid Parwez. Extremophiles: the species that evolve and survive under hostile conditions. 3 Biotech, Aug 2023. URL: https://doi.org/10.1007/s13205-023-03733-6, doi:10.1007/s13205-023-03733-6. This article has 49 citations and is from a peer-reviewed journal.

2. (baes2023transcriptionalandtranslational pages 1-2): Rani Baes, Felix Grünberger, Sébastien Pyr dit Ruys, Mohea Couturier, Sarah De Keulenaer, Sonja Skevin, Filip Van Nieuwerburgh, Didier Vertommen, Dina Grohmann, Sébastien Ferreira-Cerca, and Eveline Peeters. Transcriptional and translational dynamics underlying heat shock response in the thermophilic crenarchaeon <i>sulfolobus acidocaldarius</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.03593-22, doi:10.1128/mbio.03593-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

3. (grunberger2023uncoveringthetemporal pages 1-2): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

4. (grunberger2023uncoveringthetemporal pages 10-12): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

5. (taubner2023lipidomicsandcomparative pages 11-12): Ruth-Sophie Taubner, Lydia M. F. Baumann, Michael Steiner, Kevin Pfeifer, Barbara Reischl, Kordian Korynt, Thorsten Bauersachs, Barbara Mähnert, Elisabeth L. Clifford, Jörn Peckmann, Bernhard Schuster, Daniel Birgel, and Simon K.-M. R. Rittmann. Lipidomics and comparative metabolite excretion analysis of methanogenic archaea reveal organism-specific adaptations to varying temperatures and substrate concentrations. Apr 2023. URL: https://doi.org/10.1128/msystems.01159-22, doi:10.1128/msystems.01159-22. This article has 20 citations and is from a peer-reviewed journal.

6. (garcia2024identificationoftwo pages 6-7): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

7. (garcia2024identificationoftwo pages 1-2): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

8. (li2024biosynthesisofgmgt pages 2-3): Yanan Li, Ting Yu, Xi Feng, Bo Zhao, Huahui Chen, Huan Yang, Xing Chen, Xiao-Hua Zhang, Hayden R. Anderson, Noah Z. Burns, Fuxing Zeng, Lizhi Tao, and Zhirui Zeng. Biosynthesis of gmgt lipids by a radical sam enzyme associated with anaerobic archaea and oxygen-deficient environments. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49650-x, doi:10.1038/s41467-024-49650-x. This article has 21 citations and is from a highest quality peer-reviewed journal.

9. (rose2023structuralcharacterizationof pages 1-2): Simone A De Rose, M. Isupov, H. Worthy, Christina Stracke, N. Harmer, Bettina Siebers, J. Littlechild, Bettina Christopher Christina Benjamin Michail N. Nicholas Siebers Bräsen Stracke Meyer Isupov Harmer De Rose, Bettina Siebers, C. Bräsen, Christina Stracke, Benjamin H. Meyer, M. Isupov, N. Harmer, Simone A De Rose, J. Littlechild, E. Bonch-Osmolovskaya, Sergey Gavrilov, Ilya V Kublanov, Daniela Monti, E. Ferrandi, Eleonora Dore, Felix Müller, and Jacky L. Snoep. Structural characterization of a novel cyclic 2,3-diphosphoglycerate synthetase involved in extremolyte production in the archaeon methanothermus fervidus. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1267570, doi:10.3389/fmicb.2023.1267570. This article has 2 citations and is from a peer-reviewed journal.

10. (rose2023structuralcharacterizationof pages 2-4): Simone A De Rose, M. Isupov, H. Worthy, Christina Stracke, N. Harmer, Bettina Siebers, J. Littlechild, Bettina Christopher Christina Benjamin Michail N. Nicholas Siebers Bräsen Stracke Meyer Isupov Harmer De Rose, Bettina Siebers, C. Bräsen, Christina Stracke, Benjamin H. Meyer, M. Isupov, N. Harmer, Simone A De Rose, J. Littlechild, E. Bonch-Osmolovskaya, Sergey Gavrilov, Ilya V Kublanov, Daniela Monti, E. Ferrandi, Eleonora Dore, Felix Müller, and Jacky L. Snoep. Structural characterization of a novel cyclic 2,3-diphosphoglycerate synthetase involved in extremolyte production in the archaeon methanothermus fervidus. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1267570, doi:10.3389/fmicb.2023.1267570. This article has 2 citations and is from a peer-reviewed journal.

11. (li2024biosynthesisofgmgt pages 1-2): Yanan Li, Ting Yu, Xi Feng, Bo Zhao, Huahui Chen, Huan Yang, Xing Chen, Xiao-Hua Zhang, Hayden R. Anderson, Noah Z. Burns, Fuxing Zeng, Lizhi Tao, and Zhirui Zeng. Biosynthesis of gmgt lipids by a radical sam enzyme associated with anaerobic archaea and oxygen-deficient environments. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49650-x, doi:10.1038/s41467-024-49650-x. This article has 21 citations and is from a highest quality peer-reviewed journal.

12. (garcia2024identificationoftwo media 97b87a64): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.