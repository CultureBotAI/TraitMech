---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:46:35.335172'
end_time: '2026-06-17T22:04:37.289336'
duration_seconds: 1081.95
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: delta phenotype with numerical limits
  trait_identifier: METPO:1000534
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: delta_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by the difference between maximum and minimum
    values of a growth parameter.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports the breadth of a growth-supporting environmental range as a derived quantitative
    descriptor of microbial physiology.) | DOI:10.1016/s0300-9629(97)00003-0: adapted
    to environments of high temperature (Thermophile-adaptation review supports thermal-tolerance
    breadth as a comparable derived quantitative descriptor.)'
  causal_graph_summary: 'delta_phenotype_breadth_descriptor: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** delta phenotype with numerical limits
- **METPO identifier:** METPO:1000534
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the difference between maximum and minimum values of a growth parameter.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the breadth of a growth-supporting environmental range as a derived quantitative descriptor of microbial physiology.) | DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports thermal-tolerance breadth as a comparable derived quantitative descriptor.)
- **Existing causal graph summary:** delta_phenotype_breadth_descriptor: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **delta phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/delta_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** delta phenotype with numerical limits
- **METPO identifier:** METPO:1000534
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the difference between maximum and minimum values of a growth parameter.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the breadth of a growth-supporting environmental range as a derived quantitative descriptor of microbial physiology.) | DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports thermal-tolerance breadth as a comparable derived quantitative descriptor.)
- **Existing causal graph summary:** delta_phenotype_breadth_descriptor: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **delta phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/delta_phenotype_with_numerical_limits.yaml`.

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


## Scope summary (curation-focused)

**Trait label:** delta phenotype with numerical limits  
**METPO:** METPO:1000534  
**Definition:** difference between maximum and minimum values of a growth parameter (e.g., temperature, pH, salinity, pressure) that support “positive growth.”  

In a curation-ready framing, **delta phenotype with numerical limits** is best treated as a **derived assay descriptor**: for each *specified* growth parameter, the trait value is computed as **Δ = max(growth-positive condition) − min(growth-positive condition)**. Recent work that operationalizes this at scale (from BacDive) defines min/max as the least/greatest values where growth is described as “positive” (salinity additionally allows “inconsistent”), and uses reported optima (or midpoint of an optimum-range, common for pH) while filtering low-quality records based on minimum span thresholds (≥10°C temperature, ≥1.5 pH units, ≥1.5% NaCl, etc.). (barnum2024predictingmicrobialgrowth pages 16-19)

### Boundary cases / nearby traits

* **Not the same as an optimum** (single value) or a qualitative class label (“thermophile”, “halophile”); those can be derived from min/optimum/max, but Δ is explicitly a *range breadth* quantity. (barnum2024predictingmicrobialgrowth pages 3-6, barnum2024predictingmicrobialgrowth pages 16-19)
* **Assay- and protocol-dependent**: Δ depends on which points were tested and how “growth-positive” was called (e.g., OD600 increase vs colony formation vs growth rate threshold). Barnum et al. explicitly cull datasets with too-narrow spans or too-few points to mitigate this. (barnum2024predictingmicrobialgrowth pages 16-19)
* **Parameter-specific**: the same organism has different Δ for temperature vs salinity vs pressure, etc.; in curation, Δ nodes should be parameter-qualified.

## Key concepts and current understanding (mechanistic view)

Across modern stress physiology, Δ breadth is constrained by **multiple coupled failure modes**: (i) membrane physical state (fluidity/packing, phase transitions), (ii) macromolecular stability (protein folding/aggregation; nucleic acid structure/translation), and (iii) redox/energy balance (ROS handling; respiration mode; flux rewiring). Recent reviews emphasize **homeoviscous adaptation** (HVA: lipidome remodeling) and **osmolyte-mediated adaptation** (OMA: compatible solutes protecting membranes/proteins), with proteins (chaperones, proteases, stress sigma factors) directly and indirectly supporting membrane integrity and proteostasis under extremes. (maiti2024extrememakeoverthe pages 1-2)

### Membrane-centered limits (HVA)

A 2024 feature article synthesizes HVA as a universal paradigm: sensor systems respond to altered membrane fluidity/packing density, and cells remodel lipid composition to avoid lethal **fluid-to-gel phase transitions** under cold, high pressure, and dehydration. Enrichment of low-melting lipids (MUFA/PUFA, branched, short-chain, hydroxylated fatty acids; headgroup changes) increases fluidity and reduces packing, explicitly supporting survival/growth under extremes. (maiti2024extrememakeoverthe pages 3-4)

### Osmolytes/compatible solutes (OMA)

Cold and osmotic stresses often co-occur (e.g., freeze concentration). A 2024 review of psychrophile adaptation summarizes that compatible solutes such as **glycine betaine, trehalose, glycerol, sucrose, sarcosine, mannitol, sorbitol** can accumulate to molar concentrations and stabilize proteins/membranes, restore osmotic balance, and counteract water loss/shrinkage—mechanisms that can widen growth-positive windows. (purwar2024adaptationsofpsychrophilic pages 10-11)

### Proteostasis and transcription/translation control

A 2023 bacterial temperature response review describes regulatory networks that buffer macromolecular function across temperature shifts: heat-shock sigma factors (RpoH/RpoE), chaperone DnaK control, and periplasmic proteases (DegS, HtrA/DegP) support refolding/degradation and envelope integrity at high temperature. In cold shock, RNA structure stabilization is countered by cold-shock proteins (e.g., CspA as a major RNA-binding protein fraction after cold shock), and by RpoS-linked trehalose accumulation for cold tolerance. (moon2023temperaturemattersbacterial pages 3-5)

### Systems-level “buffering” as a mechanism of breadth

Riccardi et al. (2023) provide experimental evidence that **broad transcriptional rewiring** can preserve core metabolite concentrations across a wide temperature gap (0°C vs 15°C) in an Antarctic bacterium—an example of *systems-level buffering* that helps maintain growth-positive phenotypes across environmental shifts. (riccardi2023metabolicrobustnessto pages 2-5)

## Recent developments and latest research (prioritize 2023–2024)

### (A) Quantitative trait extraction & prediction from large databases (2024)

Barnum et al. (bioRxiv 2024) demonstrate a modern data-driven pipeline: BacDive growth-condition data were curated with explicit min/max/optimum rules and QC thresholds for continuous traits. Dataset sizes after curation: **temperature (n=2418 genomes), pH (n=1020), salinity (n=801), oxygen tolerance (n=7293)**; distributions remained imbalanced (e.g., **87% mesophiles** with 15–45°C optima; **74%** with optimum salinity 0–5% NaCl; **65%** with optimum pH 6–8). (barnum2024predictingmicrobialgrowth pages 3-6)

They trained genome/proteome-composition models achieving **92% balanced accuracy** (oxygen tolerance), **R²=0.73** (optimum temperature), **R²=0.81** (salinity), and **R²=0.48** (pH). (barnum2024predictingmicrobialgrowth pages 1-3)

*Curation relevance:* This provides a reproducible operational definition of numerical limits (min/max/optimum) suitable for computing Δ traits at scale, while highlighting systematic error sources (e.g., extreme-value inaccuracies; inconsistent reporting). (barnum2024predictingmicrobialgrowth pages 16-19)

### (B) Multi-stress range phenotyping and mechanistic “common adaptation” framing (2023)

Li et al. (AEM 2023) quantify a deep-sea **Halomonas titanicae** strain ANRCS81 that grows across broad ranges: **temperature 2–45°C**, **pressure 0.1–55 MPa**, **NaCl 0.5–17.5% (w/v)** (survival to 20–30% NaCl), and **Mg²⁺ 0–0.9 M**; growth is reported as specific growth rates under each condition. (li2023strategyforthe pages 1-2, li2023strategyforthe pages 2-4)

Mechanistically, under 40 MPa the strain upregulates genes related to **antioxidant defenses**, **anaerobic respiration**, and **fermentation**, with increased **SOD activity**, consistent with pressure-induced intracellular oxidative stress and redox/energy reprogramming as part of multi-stress adaptation. (li2023strategyforthe pages 1-2)

*Curation relevance:* This paper provides explicit numeric min/max values for multiple parameters and can serve as an archetypal, evidence-rich seed for edges connecting redox defense and energy metabolism to range breadth (especially pressure). (li2023strategyforthe pages 1-2)

### (C) 2024 mechanistic synthesis of membrane strategies

Maiti et al. (ChemComm 2024) consolidates HVA and OMA as foundational for extremophile survival, explicitly tying lipid remodeling and osmolytes to tolerance across temperature, salinity, pH, and pressure stresses, with additional mention that phenotypic adaptation can occur over minutes–days (relevant to acclimation vs long-term Δ differences across taxa). (maiti2024extrememakeoverthe pages 1-2)

## Current applications and real-world implementations

1. **Guiding cultivation of uncultivated taxa / environmental microbiology:** Genome-based prediction of growth requirements (temperature/pH/salinity/oxygen tolerance) is positioned to narrow experimental condition searches for cultivation and to infer constraints for metagenome-assembled genomes; this is a direct practical use of min/max/optimum traits and their derived descriptors. (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 14-16)
2. **Industrial robustness & strain selection:** Reviews of bacterial stress responses highlight that engineering or selecting strains with better heat/cold tolerance depends on chaperone/protease systems, envelope stress responses, membrane lipid remodeling, and compatible-solute management—mechanisms that directly impact the breadth of growth-positive windows used in industrial operation. (moon2023temperaturemattersbacterial pages 3-5, maiti2024extrememakeoverthe pages 1-2)
3. **Deep-sea/biogeochemical modeling:** Multi-stress tolerant strains such as Halomonas ANRCS81 illustrate coupled pressure–salinity–temperature tolerance and redox adaptations relevant to deep biosphere functioning; pressure-associated oxidative stress responses and energy regulation can be treated as mechanistic nodes influencing growth breadth in high-pressure environments. (li2023strategyforthe pages 1-2)

## Relevant statistics and quantitative data (recent)

### Database-derived statistics (BacDive curation; 2024)

* Dataset sizes after curation: temperature 2418, pH 1020, salinity 801, oxygen tolerance 7293. (barnum2024predictingmicrobialgrowth pages 3-6)
* Distribution imbalances (examples): 87% mesophiles (15–45°C), 74% optimum salinity 0–5% NaCl, 65% optimum pH 6–8. (barnum2024predictingmicrobialgrowth pages 3-6)
* Prediction performance from sequence composition: oxygen 92% balanced accuracy; temperature R²=0.73; salinity R²=0.81; pH R²=0.48. (barnum2024predictingmicrobialgrowth pages 1-3)

### Strain-level range breadth and growth-rate examples (2023)

For **H. titanicae ANRCS81**, Table 1 reports growth rates under multiple conditions, including growth at **2°C** (0.115 h⁻¹), temperature-supported growth up to **45°C** (0.174 h⁻¹), pressure-supported growth up to **55 MPa** (0.065 h⁻¹), NaCl-supported growth from **0.5% to 30%** (growth at 30% for ANRCS81; no growth at 30% for BH1), and Mg²⁺ tolerance up to **0.9 M** (growth at 0.9 M for ANRCS81; no growth for BH1). (li2023strategyforthe media 51209483)

For **Pseudoalteromonas haloplanktis TAC125**, bioreactor growth at 0°C vs 15°C yielded average growth rates **0.016 h⁻¹ vs 0.11 h⁻¹** (and exponential-phase rates 0.027 h⁻¹ vs 0.27 h⁻¹), providing a quantitative anchor for temperature performance differences while highlighting metabolome robustness across conditions. (riccardi2023metabolicrobustnessto pages 2-5)

## Candidate nodes grouped by type (curation-oriented)

| Node label | Node type | Suggested grounding | Evidence/source |
|---|---|---|---|
| growth temperature | environmental factor | unresolved | Explicit min/max/optimum growth parameter used to define range breadth; e.g., ANRCS81 grows from 2–45°C and BacDive curation uses reported minimum/maximum/optimum temperature values (li2023strategyforthe pages 2-4, barnum2024predictingmicrobialgrowth pages 16-19) |
| salinity (NaCl concentration) | environmental factor | CHEBI:26710 sodium chloride | Explicit growth parameter for range breadth; ANRCS81 grows at 0.5–17.5% NaCl and survives 20–30% NaCl; BacDive salinity min/max curated as numerical values (li2023strategyforthe pages 2-4, barnum2024predictingmicrobialgrowth pages 16-19) |
| pH | environmental factor | unresolved | Explicit growth parameter in BacDive-derived min/max/optimum curation; pH range used as a quantitative phenotype (barnum2024predictingmicrobialgrowth pages 16-19, barnum2024predictingmicrobialgrowth pages 14-16) |
| hydrostatic pressure | environmental factor | unresolved | ANRCS81 grew under 0.1–55 MPa, making pressure range a concrete breadth phenotype in a primary study (li2023strategyforthe pages 1-2, li2023strategyforthe pages 2-4) |
| Mg2+ concentration (chaotropic agent) | environmental factor | CHEBI:18420 magnesium(2+) | ANRCS81 tolerated 0–0.9 M Mg2+ as a measured environmental range variable (li2023strategyforthe pages 1-2, li2023strategyforthe pages 2-4) |
| oxygen availability | environmental factor | CHEBI:15379 dioxygen | Growth with oxygen vs nitrate as electron acceptor is part of stress-breadth phenotyping and phenotype prediction datasets (li2023strategyforthe pages 1-2, barnum2024predictingmicrobialgrowth pages 16-19) |
| nitrate | environmental factor | CHEBI:17632 nitrate | Used as alternate electron acceptor in ANRCS81 anaerobic growth assays under pressure (li2023strategyforthe pages 1-2, li2023strategyforthe pages 2-4) |
| minimum growth-supporting value | assay variable | unresolved | Barnum et al. define minimum as the least value where growth was described as “positive” (barnum2024predictingmicrobialgrowth pages 16-19) |
| maximum growth-supporting value | assay variable | unresolved | Barnum et al. define maximum as the greatest value where growth was described as “positive” (barnum2024predictingmicrobialgrowth pages 16-19) |
| optimum growth value | assay variable | unresolved | Barnum et al. use reported optimum, or midpoint when optimum was reported as a range (barnum2024predictingmicrobialgrowth pages 16-19) |
| delta phenotype (max − min) | assay variable | METPO:1000534 | Trait definition corresponds to difference between maximum and minimum growth-parameter values; operationalized by curated min/max values (barnum2024predictingmicrobialgrowth pages 16-19) |
| positive growth call | assay variable | unresolved | Growth limit curation depends on whether growth was reported “positive”; salinity may also use “inconsistent” (barnum2024predictingmicrobialgrowth pages 16-19) |
| OD600 increase | assay variable | unresolved | Li et al. used OD600 and noted no growth when OD600 did not increase (li2023strategyforthe pages 2-4) |
| specific growth rate | assay variable | unresolved | Used to quantify breadth across tested conditions in ANRCS81 and P. haloplanktis temperature comparisons (li2023strategyforthe pages 2-4, riccardi2023metabolicrobustnessto pages 2-5) |
| homeoviscous adaptation | process | GO:0055088 lipid homeostasis | Core membrane adaptation process regulating lipid composition to maintain membrane structure/fluidity under stress (maiti2024extrememakeoverthe pages 1-2, maiti2024extrememakeoverthe pages 3-4) |
| osmolyte-mediated adaptation | process | unresolved | Small organic molecules protect lipid membranes under stress; central mechanism in extremophile adaptation (maiti2024extrememakeoverthe pages 1-2, maiti2024extrememakeoverthe pages 5-6) |
| membrane lipid remodeling | process | GO:0006644 phospholipid metabolic process | Lipidome remodeling via altered headgroups, unsaturation, chain length, and branching is repeatedly linked to tolerance breadth (maiti2024extrememakeoverthe pages 3-4) |
| cold sensing via membrane state | process | unresolved | Ramón et al. describe sensing cold through changes in the liquid-crystalline membrane state leading to signaling (ramon2023ageneraloverview pages 1-2) |
| two-component signaling system | process | GO:0000160 phosphorelay signal transduction system | Activated by cold-induced membrane-state changes in review of cold adaptation (ramon2023ageneraloverview pages 1-2) |
| antioxidant defense | process | GO:0006979 response to oxidative stress | Li et al. identify antioxidant defenses as a core common adaptation to multiple stresses including HHP, salinity, pH, temperature (li2023strategyforthe pages 1-2) |
| anaerobic respiration | process | GO:0009061 anaerobic respiration | Upregulated under 40 MPa in ANRCS81 as part of pressure adaptation (li2023strategyforthe pages 1-2) |
| fermentation | process | GO:0006113 fermentation | Upregulated under 40 MPa in ANRCS81 as part of pressure adaptation (li2023strategyforthe pages 1-2) |
| transcriptomic buffering of metabolism | process | unresolved | Riccardi et al. show broad transcriptional rewiring maintains similar core metabolite patterns across 0 and 15°C (riccardi2023metabolicrobustnessto pages 2-5) |
| glycolysis | process | GO:0006096 glycolytic process | Listed among versatile energy-generation pathways in Halomonas and temperature-response physiology (li2023strategyforthe pages 1-2, purwar2024adaptationsofpsychrophilic pages 10-11) |
| tricarboxylic acid cycle | process | GO:0006099 tricarboxylic acid cycle | Core metabolic pathway implicated in temperature and pressure adaptation studies (li2023strategyforthe pages 1-2, riccardi2023metabolicrobustnessto pages 2-5) |
| pentose phosphate pathway | process | GO:0006098 pentose-phosphate shunt | Part of energy/redox metabolism discussed in Halomonas and cold adaptation (li2023strategyforthe pages 1-2, purwar2024adaptationsofpsychrophilic pages 10-11) |
| gluconeogenesis | process | GO:0006094 gluconeogenesis | Identified in Halomonas genomic potential and cold-adaptation metabolic rewiring examples (li2023strategyforthe pages 1-2, purwar2024adaptationsofpsychrophilic pages 10-11) |
| membrane fluidity maintenance | process | GO:0016042 lipid catabolic process | Central biophysical target of fatty-acid and lipid-composition changes across temperature extremes (maiti2024extrememakeoverthe pages 3-4, moon2023temperaturemattersbacterial pages 3-5) |
| phase transition avoidance (fluid-to-gel) | process | unresolved | Explicitly described as necessary to avoid lethal membrane ordering at low temperature/high pressure (maiti2024extrememakeoverthe pages 3-4) |
| RNA unwinding / RNA chaperoning | process | GO:0003723 RNA binding | Cold-shock proteins and RNA helicases help maintain translation under cold stress (moon2023temperaturemattersbacterial pages 3-5, shaffer2023genomicandphenotypic pages 1-2) |
| heat-shock response | process | GO:0009408 response to heat | RpoH/RpoE-controlled heat-response network supports upper-temperature tolerance (moon2023temperaturemattersbacterial pages 3-5) |
| cold-shock response | process | GO:0009409 response to cold | CspA, RpoS, DsrA/RprA and membrane changes contribute to low-temperature adaptation (moon2023temperaturemattersbacterial pages 3-5, ramon2023ageneraloverview pages 1-2) |
| ion transport | process | GO:0006811 ion transport | Comparative genomics in Halomonas links membrane transporters and ion transport to broad stress tolerance (li2023strategyforthe pages 2-4, li2023strategyforthe pages 1-2) |
| compatible-solute biosynthesis | process | GO:0005975 carbohydrate metabolic process | Halomonas genomes are described as carrying genes for compatible-solute biosynthesis supporting stress adaptation (li2023strategyforthe pages 1-2) |
| membrane transporters | protein | unresolved | ANRCS81-specific genes include multiple membrane transporters associated with broader tolerance than BH1 (li2023strategyforthe pages 2-4) |
| ion transporter E8A47_RS04055 | protein | unresolved | Unique ANRCS81 transporter candidate linked by comparative genomics to broader growth-condition tolerance (li2023strategyforthe pages 2-4) |
| LysE family transporter | protein | unresolved | ANRCS81-specific transporter family candidate from comparative genomics (li2023strategyforthe pages 2-4) |
| ABC transporter substrate-binding protein | protein | unresolved | Unique ANRCS81 transporter component candidate (li2023strategyforthe pages 2-4) |
| ABC transporter ATP-binding protein | protein | unresolved | Unique ANRCS81 transporter component candidate (li2023strategyforthe pages 2-4) |
| major facilitator superfamily transporter | protein | unresolved | ANRCS81-specific MFS transporters proposed as part of broader stress adaptation (li2023strategyforthe pages 2-4) |
| YidC membrane insertase | protein | unresolved | ANRCS81-specific membrane insertase enabling insertion of newly synthesized membrane proteins (li2023strategyforthe pages 2-4) |
| superoxide dismutase (SOD) | protein | unresolved | SOD activity increased under high pressure in ANRCS81, supporting antioxidant defense as adaptation mechanism (li2023strategyforthe pages 1-2) |
| oxidase | protein | unresolved | Oxidase activity is noted for Halomonas species as part of redox/antioxidant capacity (li2023strategyforthe pages 1-2) |
| catalase | protein | unresolved | Catalase activity is noted for Halomonas species as part of stress-defense repertoire (li2023strategyforthe pages 1-2) |
| RpoH (sigma-32) | protein | unresolved | Heat-shock-responsive sigma factor inducing heat-shock genes (moon2023temperaturemattersbacterial pages 3-5) |
| RpoE (sigma-24) | protein | unresolved | Heat-response sigma factor activated by unfolded periplasmic proteins; induces membrane protein folding/LPS genes (moon2023temperaturemattersbacterial pages 3-5) |
| DnaK | protein | unresolved | Molecular chaperone that retains/inactivates RpoH until stress conditions change (moon2023temperaturemattersbacterial pages 3-5) |
| DegS protease | protein | unresolved | Recognizes periplasmic denatured proteins and helps activate RpoE (moon2023temperaturemattersbacterial pages 3-5) |
| RseA anti-sigma factor | protein | unresolved | Anti-sigma factor controlling RpoE activation during heat stress (moon2023temperaturemattersbacterial pages 3-5) |
| HtrA / DegP protease | protein | unresolved | Periplasmic proteases induced by RpoE under heat stress (moon2023temperaturemattersbacterial pages 3-5) |
| CspA cold-shock protein | protein | unresolved | Major cold-shock RNA-binding protein that maintains translation after cold shock (moon2023temperaturemattersbacterial pages 3-5) |
| RNA helicases | protein | unresolved | Identified in Massilia frigida genome as genes associated with cold/salt tolerance (shaffer2023genomicandphenotypic pages 1-2) |
| protein chaperones | protein | unresolved | Identified in Massilia frigida genome as genes associated with cold/salt tolerance (shaffer2023genomicandphenotypic pages 1-2) |
| cation/proton antiporters | protein | unresolved | Identified in Massilia frigida genome as genes associated with cold and salt tolerance; antiporter systems also noted in alkaliphiles (shaffer2023genomicandphenotypic pages 1-2, rekadwad2023extremophilesthespecies pages 10-11) |
| electrogenic antiporters | protein | unresolved | Mentioned for alkaliphilic cyanobacteria in context of pH/salinity adaptation (rekadwad2023extremophilesthespecies pages 10-11) |
| ice-binding proteins | protein | unresolved | Cold-adaptation proteins protecting cells in low-temperature environments (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 10-11) |
| antifreeze proteins | protein | unresolved | Cold-adaptation proteins protecting against freezing damage (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 10-11) |
| phasins (e.g., PhaP) | protein | unresolved | PHA granule-associated proteins elevated at low temperatures and linked to stress protection (purwar2024adaptationsofpsychrophilic pages 10-11) |
| phospholipid bilayer / cell membrane | structure | GO:0016020 membrane | Primary structure whose fluidity, packing, and integrity constrain growth-parameter breadth (maiti2024extrememakeoverthe pages 1-2, maiti2024extrememakeoverthe pages 3-4) |
| outer membrane lipopolysaccharide (LPS) | structure | CHEBI:16412 lipopolysaccharide | LPS composition changes are discussed in temperature adaptation; RpoE induces LPS biosynthesis genes (maiti2024extrememakeoverthe pages 3-4, moon2023temperaturemattersbacterial pages 3-5) |
| thylakoid membrane | structure | unresolved | Used in Maiti et al. to illustrate temperature-dependent phase behavior and membrane limits (maiti2024extrememakeoverthe pages 5-6) |
| membrane proteins | structure | GO:0016021 integral component of membrane | Folding/insertion machinery and stress regulation target membrane proteins under heat and other stresses (li2023strategyforthe pages 2-4, moon2023temperaturemattersbacterial pages 3-5) |
| saturated fatty acids | metabolite | CHEBI:26607 saturated fatty acid | Their relative abundance versus unsaturated fatty acids modulates membrane stability across temperatures (moon2023temperaturemattersbacterial pages 3-5, maiti2024extrememakeoverthe pages 3-4) |
| unsaturated fatty acids | metabolite | CHEBI:27208 unsaturated fatty acid | Increased at low temperature/high pressure to maintain fluidity and avoid gel transition (maiti2024extrememakeoverthe pages 3-4) |
| monounsaturated fatty acids (MUFA) | metabolite | unresolved | Specifically enriched under low temperature/high pressure in HVA review (maiti2024extrememakeoverthe pages 3-4) |
| polyunsaturated fatty acids (PUFA) | metabolite | CHEBI:26208 polyunsaturated fatty acid | Enriched in cold adaptation; EPA/DHA/ARA highlighted as membrane-fluidizing lipids (maiti2024extrememakeoverthe pages 3-4, purwar2024adaptationsofpsychrophilic pages 10-11) |
| branched-chain fatty acids | metabolite | unresolved | Increase in psychrophiles to maintain fluidity at low temperature (maiti2024extrememakeoverthe pages 3-4, purwar2024adaptationsofpsychrophilic pages 10-11) |
| short-chain fatty acids | metabolite | unresolved | Enriched in some psychrophiles/extremophiles to reduce membrane melting temperature (maiti2024extrememakeoverthe pages 3-4) |
| hydroxylated fatty acids | metabolite | unresolved | Included among low-melting-point lipids used in HVA (maiti2024extrememakeoverthe pages 3-4) |
| cyclopropane fatty acids | metabolite | unresolved | Cyclic fatty-acid modifications implicated in tuning packing density/fluidity (maiti2024extrememakeoverthe pages 5-6, maiti2024extrememakeoverthe pages 3-4) |
| hopanoids | metabolite | unresolved | Cold-adaptation review notes changes in hopanoid composition during membrane adaptation (ramon2023ageneraloverview pages 1-2) |
| glycerol dibiphytanyl glycerol tetraethers (GDGTs) | metabolite | unresolved | Archaeal membrane lipids whose methylation state is described as a low-temperature HVA strategy (maiti2024extrememakeoverthe pages 5-6) |
| acetyl-CoA | metabolite | CHEBI:15351 acetyl-CoA | Proposed contributor to stress-induced lipidome remodeling in HVA review; central metabolite in temperature adaptation studies (maiti2024extrememakeoverthe pages 3-4, purwar2024adaptationsofpsychrophilic pages 10-11) |
| malonyl-CoA | metabolite | CHEBI:15531 malonyl-CoA | Proposed contributor to lipidome remodeling under stress (maiti2024extrememakeoverthe pages 3-4) |
| trehalose | metabolite | CHEBI:18150 trehalose | Cold/osmotic compatible solute; intracellular accumulation linked to cold-shock tolerance (moon2023temperaturemattersbacterial pages 3-5, purwar2024adaptationsofpsychrophilic pages 10-11) |
| glycine betaine | metabolite | CHEBI:17750 glycine betaine | Compatible solute cited as cryoprotectant/osmoprotectant in cold adaptation (purwar2024adaptationsofpsychrophilic pages 10-11) |
| glycerol | metabolite | CHEBI:17754 glycerol | Compatible solute/cryoprotectant in cold adaptation (purwar2024adaptationsofpsychrophilic pages 10-11) |
| sucrose | metabolite | CHEBI:17992 sucrose | Compatible solute in cold/osmotic adaptation (purwar2024adaptationsofpsychrophilic pages 10-11) |
| sarcosine | metabolite | CHEBI:17817 sarcosine | Accumulated cryoprotectant noted in cold-adapted Mesorhizobium example (purwar2024adaptationsofpsychrophilic pages 10-11) |
| mannitol | metabolite | CHEBI:16899 mannitol | Compatible solute in cold/osmotic adaptation (purwar2024adaptationsofpsychrophilic pages 10-11) |
| sorbitol | metabolite | CHEBI:17924 sorbitol | Compatible solute in cold/osmotic adaptation (purwar2024adaptationsofpsychrophilic pages 10-11) |
| glutathione | metabolite | CHEBI:16856 glutathione | Protein S-thiolation regulated by glutathione is discussed as a cold adaptation mechanism (purwar2024adaptationsofpsychrophilic pages 10-11) |
| carbon dioxide | metabolite | CHEBI:16526 carbon dioxide | Reduced CO2 generation under HHP is part of Halomonas metabolic adaptation readout (li2023strategyforthe pages 1-2) |
| ammonium | metabolite | CHEBI:28938 ammonium | Increased ammonium generation under HHP accompanies nitrate/nitrite consumption in Halomonas (li2023strategyforthe pages 1-2) |
| reactive oxygen species | metabolite | CHEBI:26523 reactive oxygen species | Stress-linked redox imbalance is proposed as a common consequence of extreme temperature, salinity, pH, and pressure (li2023strategyforthe pages 1-2, purwar2024adaptationsofpsychrophilic pages 10-11) |
| phosphoenolpyruvate (PEP) | metabolite | CHEBI:18021 phosphoenolpyruvate | Identified as a key intermediate in temperature-dependent metabolic adaptation in P. haloplanktis (riccardi2023metabolicrobustnessto pages 2-5) |
| glutamate | metabolite | CHEBI:29985 L-glutamate | Quantified central metabolite in P. haloplanktis temperature study; proteome glutamate frequency also correlates with growth conditions in Barnum et al. (riccardi2023metabolicrobustnessto pages 2-5, barnum2024predictingmicrobialgrowth pages 3-6) |
| gluconate | metabolite | CHEBI:24290 D-gluconate | Quantified extracellular metabolite in temperature adaptation experiment (riccardi2023metabolicrobustnessto pages 2-5) |
| NADX/NADPX pool | metabolite | unresolved | Central redox metabolite pool tracked in temperature robustness study (riccardi2023metabolicrobustnessto pages 2-5) |
| polyhydroxyalkanoates (PHAs) | metabolite | unresolved | Storage/stress-protective polymers contributing to cryoprotection and oxidative-stress resistance (purwar2024adaptationsofpsychrophilic pages 10-11) |
| extracellular polysaccharides (EPS) | structure | GO:0005618 cell wall | Protective cold-adaptation matrix that helps against ice and osmotic stress (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10) |
| Halomonas titanicae ANRCS81 | structure | NCBITaxon:unresolved | Primary strain example with measured broad temperature, salinity, pressure, and Mg2+ ranges (li2023strategyforthe pages 1-2, li2023strategyforthe pages 2-4) |
| Pseudoalteromonas haloplanktis TAC125 | structure | NCBITaxon:unresolved | Primary strain example for transcriptomic buffering across 0 and 15°C growth (riccardi2023metabolicrobustnessto pages 2-5) |
| Massilia frigida DJPM01 | structure | NCBITaxon:unresolved | Antarctic strain with genomic candidates for cold/salt tolerance including antiporters and chaperones (shaffer2023genomicandphenotypic pages 1-2) |


*Table: This table lists candidate mechanistic and environmental nodes relevant to curating a causal graph for the microbial trait 'delta phenotype with numerical limits'. It groups assay variables, environmental factors, processes, proteins, metabolites, and structures supported by the cited 2023-2024 sources.*

## Candidate causal edges (triples) with evidence snippets

| Edge (subject—predicate→object) | Parameter affected | Direction on delta | Evidence snippet (short quote) | Reference (authors, year, DOI) | URL | Notes/strength |
|---|---|---|---|---|---|---|
| Homeoviscous adaptation (HVA)—maintains→membrane structure/fluidity under stress | general (temperature/salinity/pH) | increase/maintain | “Key strategies include homeoviscous adaptation (HVA), involving the regulation of lipid composition” and these mechanisms are linked to tolerance of “temperature… salinity, and pH extremes” (maiti2024extrememakeoverthe pages 1-2) | Maiti et al., 2024, 10.1039/d4cc03114h | https://doi.org/10.1039/d4cc03114h | Strong general review evidence; mechanism broad but not tied to one assay-defined delta value. |
| Unsaturated/branched/short-chain fatty acid enrichment—prevents→fluid-to-gel phase transition | temperature, pressure | increase | “At low temperatures and high pressure, lipids with low melting temperatures… MUFA, PUFA, branched fatty acids, short-chain fatty acids… are incorporated in a higher proportion” and this “avoid[s] the fluid-to-gel phase transition” (maiti2024extrememakeoverthe pages 3-4) | Maiti et al., 2024, 10.1039/d4cc03114h | https://doi.org/10.1039/d4cc03114h | Strong review support for broader thermal/pressure tolerance via membrane remodeling. |
| Membrane fluidity sensing / two-component signaling—activates→cold adaptation program | temperature | increase | Cold adaptation includes “sensing the cold, mainly through the modification of the liquid-crystalline membrane state, leading to the activation of a two-component system” (ramon2023ageneraloverview pages 1-2) | Ramón et al., 2023, 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Strong review support; upstream regulatory edge rather than direct assay manipulation. |
| Double bonds in lipids / altered hopanoids / pigments—adapts→membrane composition for proper function | temperature | increase | Cold adaptation includes “adapting the composition of membranes for proper functions mainly due to the production of double bonds in lipids, changes in hopanoid composition, and the inclusion of pigments” (ramon2023ageneraloverview pages 1-2) | Ramón et al., 2023, 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Strong general evidence for widening low-temperature growth capacity. |
| Altered saturated:unsaturated fatty-acid ratio—modulates→membrane stability | temperature | maintain | “membrane stability is modulated by alteration of the ratio of saturated and unsaturated fatty acids” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al., 2023, 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Strong review evidence; phrased as maintenance across temperature shifts. |
| Compatible solutes/osmolytes—stabilize→proteins and membranes | temperature/salinity/general osmotic stress | increase/maintain | “Compatible solutes… depress the freezing point… stabilize proteins and membranes, restore osmotic balance” (purwar2024adaptationsofpsychrophilic pages 10-11) | Purwar & Srivastava, 2024, 10.37256/amtt.5220244537 | https://doi.org/10.37256/amtt.5220244537 | Strong review evidence for cold + osmotic breadth; not tied to one species. |
| Trehalose accumulation (RpoS/otsAB)—helps withstand→cold shock | temperature | increase | “The up-regulation of ostAB operon by RpoS mediates intracellular accumulation of trehalose to withstand cold shock” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al., 2023, 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Moderate-to-strong; specific to E. coli regulatory model but mechanistically clear. |
| Cold-shock protein CspA—maintains→translation at low temperature | temperature | increase | “CspA comprises ~15% of total protein synthesis after a cold shock” and “bind[s] to RNA and promot[es] the formation of single-stranded RNA” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al., 2023, 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Strong mechanistic review support for low-temperature tolerance; indirect on delta breadth. |
| RpoH heat-shock sigma factor—induces→heat-shock genes | temperature | increase | “RpoH… is a heat-shock-responsive sigma factor, which induces… heat-shock genes” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al., 2023, 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Strong review support for upper-temperature tolerance mechanisms. |
| RpoE activation—induces→periplasmic proteases, membrane protein folding, LPS biosynthesis genes | temperature | increase | “The activated RpoE not only induces expression of heat-shock-related proteins and periplasmic proteases… but also induces genes involved in folding of membrane proteins and biosynthesis of lipopolysaccharides” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al., 2023, 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Strong for heat tolerance maintenance; likely expands upper limit. |
| Antioxidant defense genes / elevated SOD activity—supports→adaptation to multiple stresses | pressure/general | increase | Under HHP, “genes related to antioxidant defenses… were upregulated” and “SOD activity increased”; authors note “antioxidants and energy generation are the core components” of common adaptation to HHP, temperature, salinity, pH (li2023strategyforthe pages 1-2) | Li et al., 2023, 10.1128/aem.01304-22 | https://doi.org/10.1128/aem.01304-22 | Strong strain-specific evidence for pressure; broader generalization to multiple stresses is review-like within paper. |
| Anaerobic respiration and fermentation pathway upregulation—supports→growth under HHP | pressure | increase | “when the strain was incubated at 40 MPa, genes related to antioxidant defenses, anaerobic respiration, and fermentation were upregulated” (li2023strategyforthe pages 1-2) | Li et al., 2023, 10.1128/aem.01304-22 | https://doi.org/10.1128/aem.01304-22 | Strong strain-specific pressure edge; causal for pressure breadth in ANRCS81. |
| Membrane transporters (ion/LysE/ABC/MFS) and YidC—support→broad tolerance to pressures, temperatures, salinities | general | increase | ANRCS81 had unique genes “related to membrane transporters” and “membrane insertase YidC”; the strain “grew under a broad range of… pressures, temperatures, and salinities” (li2023strategyforthe pages 2-4) | Li et al., 2023, 10.1128/aem.01304-22 | https://doi.org/10.1128/aem.01304-22 | **Uncertain**: comparative genomic association, not direct perturbation; useful candidate nodes only. |
| Ion transport + compatible-solute biosynthesis—enables→adaptation to various extreme environments | salinity/general | increase | Halomonas BH1 genome contains genes related to “biosynthesis of compatible solutes, and ion transport. The aforementioned features allow Halomonas to adapt to various extreme environments” (li2023strategyforthe pages 1-2) | Li et al., 2023, 10.1128/aem.01304-22 | https://doi.org/10.1128/aem.01304-22 | **Uncertain** and genus/relative-strain based; supportive but indirect for delta breadth. |
| Cation/proton antiporters—contribute to→cold and salt tolerance | salinity/temperature | increase | Massilia frigida genome contained “multiple RNA helicases, protein chaperones, and cation/proton antiporters” and these were identified as genes “associated with cold and salt tolerance” (shaffer2023genomicandphenotypic pages 1-2) | Shaffer et al., 2023, 10.3389/fmicb.2023.1156033 | https://doi.org/10.3389/fmicb.2023.1156033 | Moderate strain-specific genomic inference; not gene knockout evidence. |
| RNA helicases and protein chaperones—contribute to→cold tolerance | temperature | increase | Genome analysis identified “multiple RNA helicases, protein chaperones… associated with cold… tolerance” (shaffer2023genomicandphenotypic pages 1-2) | Shaffer et al., 2023, 10.3389/fmicb.2023.1156033 | https://doi.org/10.3389/fmicb.2023.1156033 | Moderate strain-specific inference; phenotype-genotype linkage but not causal perturbation. |
| Transcriptomic buffering / regulatory–metabolic cross talk—maintains→core metabolism across wide temperatures | temperature | maintain | “different growth temperatures induce broad transcriptional changes… however… most key central metabolites show overlapping trends” and “there exists intense cross talk between regulatory and metabolic networks” (riccardi2023metabolicrobustnessto pages 2-5) | Riccardi et al., 2023, 10.1128/msystems.01124-22 | https://doi.org/10.1128/msystems.01124-22 | Strong experimental systems-biology evidence for maintenance across 0 and 15°C; mechanism broad, not single gene. |
| Electrogenic antiporters—support→alkaliphilic pH tolerance | pH | increase | “certain alkaliphilic cyanobacteria ‘carry electrogenic antiporters’” in context of pH/salinity tolerance (rekadwad2023extremophilesthespecies pages 10-11) | Rekadwad et al., 2023, 10.1007/s13205-023-03733-6 | https://doi.org/10.1007/s13205-023-03733-6 | **Uncertain**: broad review, limited mechanistic detail and taxon specificity. |
| Protein/proteome sequence composition shifts (acidic residues, lower pI, amino-acid frequencies)—tracks→adaptation to salinity, pH, temperature, oxygen | general | maintain/**uncertain increase** | Models found “increased acidic residues and lower pI at higher salinity” and amino-acid composition predictive of growth conditions (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 3-6) | Barnum et al., 2024, 10.1101/2024.03.22.586313 | https://doi.org/10.1101/2024.03.22.586313 | **Uncertain** for curation as causal edge: predictive correlates from comparative genomics, not intervention evidence. |


*Table: This table compiles evidence-backed candidate causal edges for microbial growth-parameter range breadth, using only the specified 2023-2024 sources available in context. It highlights which mechanisms are strongly supported versus uncertain genomic or correlational candidates for TraitMech curation.*

## Expert opinions / authoritative synthesis (from sources)

* **Membrane-first framing:** Extremophile growth breadth is repeatedly tied to maintaining membrane fluidity/packing to avoid phase transitions, with HVA described as a “universal paradigm of membrane adaptation” that spans diverse extremophiles and stressors. (maiti2024extrememakeoverthe pages 3-4)
* **Common adaptation hypothesis across multiple stresses:** Li et al. argue microorganisms may use shared strategies to cope with combined pressure, temperature, salinity and other stresses, where **antioxidant defenses and energy generation** are “core components.” (li2023strategyforthe pages 1-2)
* **Temperature response as layered regulation:** Moon et al. emphasize that bacterial temperature tolerance depends on integrated regulation (sigma factors, chaperones/proteases), membrane compositional tuning, and small-molecule protective strategies (trehalose). (moon2023temperaturemattersbacterial pages 3-5)

## Ontology grounding (suggestions)

Grounding suggestions for many nodes (especially chemicals and broad processes) are included in the node table (artifact-01). Key stable groundings that are directly supported:

* **METPO:** METPO:1000534 (delta phenotype with numerical limits). (barnum2024predictingmicrobialgrowth pages 16-19)
* **CHEBI examples:** NaCl (CHEBI:26710), dioxygen (CHEBI:15379), nitrate (CHEBI:17632), magnesium(2+) (CHEBI:18420), trehalose (CHEBI:18150), glycine betaine (CHEBI:17750), glycerol (CHEBI:17754), sucrose (CHEBI:17992), glutathione (CHEBI:16856). (li2023strategyforthe pages 2-4, purwar2024adaptationsofpsychrophilic pages 10-11)
* **GO examples (process-level):** response to oxidative stress (GO:0006979), anaerobic respiration (GO:0009061), fermentation (GO:0006113), glycolysis (GO:0006096), TCA (GO:0006099), PPP (GO:0006098), response to heat (GO:0009408), response to cold (GO:0009409). (li2023strategyforthe pages 1-2, moon2023temperaturemattersbacterial pages 3-5, ramon2023ageneraloverview pages 1-2)

## Warnings / claims not yet ready for TraitMech curation

1. **Correlational sequence-composition signals are not mechanistic edges.** Barnum et al. show amino-acid composition predicts optima and is correlated with salinity/pH/oxygen tolerance, but these are population-level correlates and not intervention evidence. Curate as *predictive features* only if the ontology supports such nodes; otherwise mark as uncertain. (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 14-16)
2. **Comparative genomics “unique genes” are candidates, not confirmed causes.** The association of ANRCS81-specific transporters/YidC with broader tolerance vs BH1 lacks perturbation (knockout/overexpression) evidence; treat as candidate nodes and uncertain edges. (li2023strategyforthe pages 2-4)
3. **Antiporter mentions in broad extremophile reviews are taxon-specific and underspecified.** The electrogenic antiporter statement (alkaliphilic cyanobacteria) lacks gene/protein identifiers and experimental linkage to a quantified Δ phenotype; curate as tentative. (rekadwad2023extremophilesthespecies pages 10-11)
4. **Parameter interactions complicate Δ interpretation.** Pressure and temperature can interact (e.g., pressure shifting apparent temperature limits), so a Δ node should ideally store assay context (pressure, medium composition, electron acceptor) to avoid mixing incomparable measurements. (rekadwad2023extremophilesthespecies pages 10-11, li2023strategyforthe pages 2-4)

## DOI-first bibliography (with dates and URLs)

1. **Maiti A, Erimban S, Daschakraborty S.** *Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.* **Chemical Communications**. Published Aug 2024. DOI: **10.1039/d4cc03114h**. https://doi.org/10.1039/d4cc03114h (maiti2024extrememakeoverthe pages 1-2, maiti2024extrememakeoverthe pages 3-4)
2. **Purwar S, Srivastava S.** *Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.* **Applied Microbiology: Theory & Technology**. Published Oct 2024. DOI: **10.37256/amtt.5220244537**. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 10-11)
3. **Moon S, Ham S, Jeong J, et al.** *Temperature Matters: Bacterial Response to Temperature Change.* **Journal of Microbiology**. Published Mar 2023. DOI: **10.1007/s12275-023-00031-x**. https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 3-5)
4. **Ramón A, Esteves A, Villadóniga C, et al.** *A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.* **Brazilian Journal of Microbiology**. Published online 21 Jul 2023. DOI: **10.1007/s42770-023-01057-4**. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2)
5. **Li J, Xiao X, Zhou M, Zhang Y.** *Strategy for the Adaptation to Stressful Conditions of the Novel Isolated Conditional Piezophilic Strain Halomonas titanicae ANRCS81.* **Applied and Environmental Microbiology**. Published 13 Mar 2023. DOI: **10.1128/aem.01304-22**. https://doi.org/10.1128/aem.01304-22 (li2023strategyforthe pages 1-2, li2023strategyforthe media 51209483)
6. **Riccardi C, Calvanese M, Ghini V, et al.** *Metabolic Robustness to Growth Temperature of a Cold-Adapted Marine Bacterium.* **mSystems**. Published Apr 2023. DOI: **10.1128/msystems.01124-22**. https://doi.org/10.1128/msystems.01124-22 (riccardi2023metabolicrobustnessto pages 2-5)
7. **Shaffer JMC, Giddings L-A, Samples RM, Mikucki JA.** *Genomic and phenotypic characterization of a red-pigmented strain of Massilia frigida isolated from an Antarctic microbial mat.* **Frontiers in Microbiology**. Published May 2023. DOI: **10.3389/fmicb.2023.1156033**. https://doi.org/10.3389/fmicb.2023.1156033 (shaffer2023genomicandphenotypic pages 1-2)
8. **Rekadwad BN, Li W-J, Gonzalez JM, et al.** *Extremophiles: the species that evolve and survive under hostile conditions.* **3 Biotech**. Published Aug 2023. DOI: **10.1007/s13205-023-03733-6**. https://doi.org/10.1007/s13205-023-03733-6 (rekadwad2023extremophilesthespecies pages 10-11)
9. **Barnum TP, Crits-Christoph A, Molla M, et al.** *Predicting microbial growth conditions from amino acid composition.* **bioRxiv**. Posted 22 Mar 2024. DOI: **10.1101/2024.03.22.586313**. https://doi.org/10.1101/2024.03.22.586313 (barnum2024predictingmicrobialgrowth pages 16-19, barnum2024predictingmicrobialgrowth pages 1-3)




References

1. (barnum2024predictingmicrobialgrowth pages 16-19): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 47 citations.

2. (barnum2024predictingmicrobialgrowth pages 3-6): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 47 citations.

3. (maiti2024extrememakeoverthe pages 1-2): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

4. (maiti2024extrememakeoverthe pages 3-4): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

5. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

6. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

7. (riccardi2023metabolicrobustnessto pages 2-5): Christopher Riccardi, Marzia Calvanese, Veronica Ghini, Tania Alonso-Vásquez, Elena Perrin, Paola Turano, Giorgio Giurato, Alessandro Weisz, Ermenegilda Parrilli, Maria Luisa Tutino, and Marco Fondi. Metabolic robustness to growth temperature of a cold- adapted marine bacterium. mSystems, Apr 2023. URL: https://doi.org/10.1128/msystems.01124-22, doi:10.1128/msystems.01124-22. This article has 20 citations and is from a peer-reviewed journal.

8. (barnum2024predictingmicrobialgrowth pages 1-3): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 47 citations.

9. (li2023strategyforthe pages 1-2): Jiakang Li, Xiang Xiao, Meng Zhou, and Yu Zhang. Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain halomonas titanicae anrcs81. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01304-22, doi:10.1128/aem.01304-22. This article has 17 citations and is from a peer-reviewed journal.

10. (li2023strategyforthe pages 2-4): Jiakang Li, Xiang Xiao, Meng Zhou, and Yu Zhang. Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain halomonas titanicae anrcs81. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01304-22, doi:10.1128/aem.01304-22. This article has 17 citations and is from a peer-reviewed journal.

11. (barnum2024predictingmicrobialgrowth pages 14-16): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 47 citations.

12. (li2023strategyforthe media 51209483): Jiakang Li, Xiang Xiao, Meng Zhou, and Yu Zhang. Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain halomonas titanicae anrcs81. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01304-22, doi:10.1128/aem.01304-22. This article has 17 citations and is from a peer-reviewed journal.

13. (maiti2024extrememakeoverthe pages 5-6): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

14. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

15. (shaffer2023genomicandphenotypic pages 1-2): Jacob M. C. Shaffer, Lesley-Ann Giddings, Robert M. Samples, and Jill A. Mikucki. Genomic and phenotypic characterization of a red-pigmented strain of massilia frigida isolated from an antarctic microbial mat. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1156033, doi:10.3389/fmicb.2023.1156033. This article has 16 citations and is from a peer-reviewed journal.

16. (rekadwad2023extremophilesthespecies pages 10-11): Bhagwan Narayan Rekadwad, Wen-Jun Li, Juan M. Gonzalez, Rekha Punchappady Devasya, Arun Ananthapadmanabha Bhagwath, Ruchi Urana, and Khalid Parwez. Extremophiles: the species that evolve and survive under hostile conditions. 3 Biotech, Aug 2023. URL: https://doi.org/10.1007/s13205-023-03733-6, doi:10.1007/s13205-023-03733-6. This article has 49 citations and is from a peer-reviewed journal.

17. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.