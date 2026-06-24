---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:09:33.738846'
end_time: '2026-06-17T21:46:25.290132'
duration_seconds: 2211.55
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: alkalotolerant
  trait_identifier: METPO:1003009
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: alkalotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference in which an organism can tolerate alkaline pH
    but grows optimally at neutral pH.
  parent_traits: METPO:1003000
  synonyms: alkalitolerant
  evidence_summary: 'DOI:10.1016/j.bbamem.2005.09.010: alkali-tolerant and extremely
    alkaliphilic bacteria (Supports alkaline pH tolerance as a microbial pH-homeostasis
    phenotype.)'
  causal_graph_summary: 'alkalotolerant_alkaline_stress_homeostasis: 5 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** alkalotolerant
- **METPO identifier:** METPO:1003009
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can tolerate alkaline pH but grows optimally at neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkalitolerant
- **Existing evidence:** DOI:10.1016/j.bbamem.2005.09.010: alkali-tolerant and extremely alkaliphilic bacteria (Supports alkaline pH tolerance as a microbial pH-homeostasis phenotype.)
- **Existing causal graph summary:** alkalotolerant_alkaline_stress_homeostasis: 5 nodes, 5 edges

## Research Objective

Research the microbial trait **alkalotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkalotolerant.yaml`.

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
- **Trait label:** alkalotolerant
- **METPO identifier:** METPO:1003009
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can tolerate alkaline pH but grows optimally at neutral pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkalitolerant
- **Existing evidence:** DOI:10.1016/j.bbamem.2005.09.010: alkali-tolerant and extremely alkaliphilic bacteria (Supports alkaline pH tolerance as a microbial pH-homeostasis phenotype.)
- **Existing causal graph summary:** alkalotolerant_alkaline_stress_homeostasis: 5 nodes, 5 edges

## Research Objective

Research the microbial trait **alkalotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkalotolerant.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **alkalotolerant** (METPO:1003009)

### 1) Scope summary (TraitMech curation target)

**Trait definition (METPO:1003009):** *alkalotolerant* (syn. alkalitolerant) denotes an organism that **tolerates alkaline pH** but whose **optimal growth remains near neutral pH**.

**Operational boundary vs. “alkaliphile”:** Authoritative extremophile reviews emphasize that strict definitions can be fuzzy, but adopt an operational distinction in which **alkaliphiles grow optimally or very well above pH 9 (often pH 10–12) and cannot grow or grow only slowly near neutral pH (~6.5)**, whereas **alkalitolerant/alkalotolerant organisms can grow at high pH but have optimal growth near neutral**. (horikoshi1999alkaliphilessomeapplications pages 1-3, gondal2021adaptabilityofsoil pages 3-4, horikoshi2016alkaliphiles pages 1-2)

**Boundary-case example from a hyperalkaline ecosystem:** In isolates from a serpentinizing system, one strain grew **pH 7–10 (optimum 7–9)** (closer to alkalotolerance), while another grew **pH 10–12 (optimum 11)** (alkaliphilic) (Table image). (thompson2023insightsintothe media ecd4bf5a)

**How the phenotype is measured/assayed:**
- **Growth range and growth optimum across an external pH gradient** (liquid/plate culture) are commonly used, including *pHmax* (“maximum pH that allows growth”) as a quantitative tolerance endpoint. (sawatari2007diversityandmechanisms pages 1-1, thompson2023insightsintothe media ecd4bf5a)
- **Intracellular pH homeostasis** (e.g., internal pH maintained ~8 under external pH 8–11 in alkaliphiles) is a mechanistic readout frequently used to interpret alkaline tolerance strategies. (horikoshi1999alkaliphilessomeapplications pages 4-5, horikoshi2016alkaliphiles pages 2-5)

### 2) Key concepts and mechanistic understanding (current consensus)

Alkaline environments challenge microbes because **external [H+] is low**, reducing the ability to build a classical proton motive force and increasing the need to **retain/recapture protons** and **export Na+** while keeping cytoplasmic pH near neutral. A recurring mechanistic theme is that alkaliphiles/alkalotolerant organisms **maintain internal pH far below external pH** (often around 8–9) using **cell-envelope chemistry** and **cation/proton antiport systems**. (horikoshi1999alkaliphilessomeapplications pages 4-5, horikoshi2016alkaliphiles pages 2-5)

**Canonical mechanistic modules to curate into a TraitMech causal graph** include:
- **Cation/proton antiport (Na+/H+ antiporters and Mrp complexes)** as core pH and Na+ homeostasis machinery; membrane potential can drive Na+ extrusion and becomes especially important at alkaline pH. (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5, foreman2021geneticandbiochemical pages 12-13)
- **Cell-wall/cell-surface acidic polymers** (including teichuronic-acid-related adaptations in Bacillus) that help create a more favorable surface microenvironment by adsorbing Na+ and hydronium while repelling hydroxide. (horikoshi1999alkaliphilessomeapplications pages 4-5, chia2025roleofextremophiles pages 6-8)
- **Na+-based bioenergetics (sodium motive force)** and Na+-coupled transport as an alternative energetic strategy in alkaline settings. (chia2025roleofextremophiles pages 6-8)
- **Stress-protective osmolyte/ion modules** that frequently co-occur in haloalkaline ecosystems (e.g., compatible solutes and K+ management in soda-lake organisms). (xing2024thepolyextremophilenatranaerobius pages 1-2)

### 3) Candidate graph entities (nodes) with ontology grounding suggestions

The following node set is derived directly from the retrieved evidence and is organized to support `data/traits/environment/alkalotolerant.yaml` curation.

| Node label | Type | Definition/role in alkalotolerance | Evidence source (DOI/URL/year) | Suggested ontology grounding |
|---|---|---|---|---|
| **Environmental/assay factors** |  |  |  |  |
| alkaline pH stress | environmental factor | High external pH challenge that requires pH homeostasis and specialized transport/cell-envelope adaptations for survival or growth at alkaline pH (horikoshi1999alkaliphilessomeapplications pages 1-3, horikoshi2016alkaliphiles pages 1-2, horikoshi1999alkaliphilessomeapplications pages 4-5) | 10.1128/MMBR.63.4.735-750.1999 / https://doi.org/10.1128/MMBR.63.4.735-750.1999 / 1999; 10.1007/978-4-431-55408-0_4 / https://doi.org/10.1007/978-4-431-55408-0_4 / 2016 | ENVO:alkaline environment candidate |
| external pH ≥9 | assay/environmental factor | Operational threshold commonly used to distinguish alkaline conditions and alkaliphile/alkalitolerant growth assays; alkaliphiles typically require or grow very well above pH 9, whereas alkalitolerant taxa can grow there but often have neutral optima (horikoshi1999alkaliphilessomeapplications pages 1-3, gondal2021adaptabilityofsoil pages 3-4, horikoshi2016alkaliphiles pages 1-2) | 10.1128/MMBR.63.4.735-750.1999 / https://doi.org/10.1128/MMBR.63.4.735-750.1999 / 1999; 10.18488/journal.68.2021.82.71.79 / https://doi.org/10.18488/journal.68.2021.82.71.79 / 2021; 10.1007/978-4-431-55408-0_4 / https://doi.org/10.1007/978-4-431-55408-0_4 / 2016 |  |
| pHmax | assay factor | Maximum pH that allows growth; used as a quantitative phenotype for alkali tolerance in Lactobacillus comparisons (sawatari2007diversityandmechanisms pages 1-1, sawatari2007diversityandmechanisms pages 6-7) | 10.1128/AEM.02834-06 / https://doi.org/10.1128/AEM.02834-06 / 2007 |  |
| Nigericin | perturbation/assay factor | Ionophore used to dissipate transmembrane pH gradient; lowering pHmax after treatment supports causal contribution of reversed ΔpH to alkali tolerance (sawatari2007diversityandmechanisms pages 6-7, sawatari2007diversityandmechanisms pages 3-5) | 10.1128/AEM.02834-06 / https://doi.org/10.1128/AEM.02834-06 / 2007 | CHEBI:29107 candidate |
| **Biological processes** |  |  |  |  |
| cytoplasmic pH homeostasis / internal pH ~8 | biological process | Maintenance of a near-neutral internal pH despite alkaline external pH; a core physiological hallmark of alkaliphily/alkalitolerance (horikoshi1999alkaliphilessomeapplications pages 4-5, horikoshi2016alkaliphiles pages 2-5) | 10.1128/MMBR.63.4.735-750.1999 / https://doi.org/10.1128/MMBR.63.4.735-750.1999 / 1999; 10.1007/978-4-431-55408-0_4 / https://doi.org/10.1007/978-4-431-55408-0_4 / 2016 | GO:0051453 candidate |
| sodium motive force | biological process/energetic state | Na+-based bioenergetic gradient used when external H+ is scarce; supports intracellular pH control and transport in alkaliphiles (chia2025roleofextremophiles pages 6-8) | 10.1007/s11244-024-01919-7 / https://doi.org/10.1007/s11244-024-01919-7 / 2025 |  |
| K+ accumulation / K+ homeostasis | biological process | Maintenance or accumulation of intracellular K+ contributes to ion homeostasis under haloalkaline stress; supported by transporter upregulation in Natranaerobius thermophilus (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24 / https://doi.org/10.1128/AEM.00145-24 / 2024 | GO:0055075 candidate |
| compatible solute uptake / accumulation | biological process | Import and/or accumulation of osmoprotective compatible solutes such as glycine betaine, proline, and glutamate; important in polyextremophiles from alkaline saline systems (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 10-14) | 10.1128/AEM.00145-24 / https://doi.org/10.1128/AEM.00145-24 / 2024 | GO:0015843 candidate |
| reversed ΔpH under alkaline conditions | biological process | Higher intracellular than extracellular proton gradient component under alkaline conditions; experimentally shown to contribute to alkali tolerance in Lactobacillus (sawatari2007diversityandmechanisms pages 6-7, sawatari2007diversityandmechanisms pages 3-5) | 10.1128/AEM.02834-06 / https://doi.org/10.1128/AEM.02834-06 / 2007 |  |
| **Transporters/complexes** |  |  |  |  |
| Na+/H+ antiporter NhaA | transporter | Electrogenic Na+/H+ antiporter; membrane potential-driven Na+ extrusion is particularly important at alkaline external pH, and NhaA supports growth at alkaline pH in E. coli (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | 10.3390/ijms23169156 / https://doi.org/10.3390/ijms23169156 / 2022 | GO:0015385 candidate |
| Na+/H+ antiporter NhaB | transporter | Electrogenic Na+/H+ antiporter contributing to Na+ handling and alkaline/high-Na+ growth phenotypes in Pseudomonas aeruginosa and other bacteria (patinoruiz2022prokaryoticna+h+exchangers—transport pages 19-20, foreman2021geneticandbiochemical pages 12-13, patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | 10.1128/JB.00284-21 / https://doi.org/10.1128/JB.00284-21 / 2021; 10.3390/ijms23169156 / https://doi.org/10.3390/ijms23169156 / 2022 | GO:0015385 candidate |
| Na+/H+ antiporter NhaC | transporter | NhaC-family cation/proton antiporter implicated in alkaline/salt tolerance; also represented by archaeal NhaC1/NhaC2 antiporters active up to pH 9.5 in Natronorubrum daqingense (patinoruiz2022prokaryoticna+h+exchangers—transport pages 19-20, wang2023characterizationoftwo pages 16-16, patinoruiz2022prokaryoticna+h+exchangers—transport pages 23-23) | 10.3390/ijms241310786 / https://doi.org/10.3390/ijms241310786 / 2023; 10.3390/ijms23169156 / https://doi.org/10.3390/ijms23169156 / 2022 | GO:0015385 candidate |
| Na+/H+ antiporter NhaD | transporter | NhaD-family antiporter implicated in marine/halophilic and alkaline adaptation contexts (patinoruiz2022prokaryoticna+h+exchangers—transport pages 19-20, patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | 10.3390/ijms23169156 / https://doi.org/10.3390/ijms23169156 / 2022 | GO:0015385 candidate |
| Na+/H+ antiporter NhaE | transporter | NhaE-family cation/proton antiporter listed among bacterial alkaline/salt homeostasis antiporters (patinoruiz2022prokaryoticna+h+exchangers—transport pages 19-20, patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | 10.3390/ijms23169156 / https://doi.org/10.3390/ijms23169156 / 2022 | GO:0015385 candidate |
| Na+/H+ antiporter NhaP | transporter | NhaP-family antiporter; part of broader prokaryotic Na+/H+ antiporter repertoire supporting cation/proton exchange and pH homeostasis (patinoruiz2022prokaryoticna+h+exchangers—transport pages 19-20, patinoruiz2022prokaryoticna+h+exchangers—transport pages 20-22) | 10.3390/ijms23169156 / https://doi.org/10.3390/ijms23169156 / 2022 | GO:0015385 candidate |
| Mrp antiporter complex (MrpABCDEFG) | transporter complex | Multisubunit Na+/H+ antiporter complex; all subunits are required for full activity, active under alkaline conditions, and can rescue alkaline-sensitive strains (patinoruiz2022prokaryoticna+h+exchangers—transport pages 8-10, patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | 10.3390/ijms23169156 / https://doi.org/10.3390/ijms23169156 / 2022 |  |
| MrpA | transporter complex subunit | Mrp subunit directly participating in cation/H+ translocation in the Mrp complex (patinoruiz2022prokaryoticna+h+exchangers—transport pages 8-10) | 10.3390/ijms23169156 / https://doi.org/10.3390/ijms23169156 / 2022 |  |
| MrpD | transporter complex subunit | Mrp subunit directly participating in cation/H+ translocation in the Mrp complex (patinoruiz2022prokaryoticna+h+exchangers—transport pages 8-10) | 10.3390/ijms23169156 / https://doi.org/10.3390/ijms23169156 / 2022 |  |
| ATP-driven K+/H+ antiporter | transporter | Energy-dependent antiporter proposed to contribute to reversed ΔpH and alkali tolerance in Lactobacillus and Enterococcus-related mechanisms (sawatari2007diversityandmechanisms pages 6-7, sawatari2007diversityandmechanisms pages 3-5) | 10.1128/AEM.02834-06 / https://doi.org/10.1128/AEM.02834-06 / 2007 |  |
| Na+-translocating FOF1-ATPase | transporter/ATPase complex | Na+-coupled ATPase present and upregulated in Natranaerobius thermophilus, linked to adaptation to extreme saline-alkaline conditions (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24 / https://doi.org/10.1128/AEM.00145-24 / 2024 | GO:0046933 candidate |
| Opu/ProU ABC transporters | transporter | Glycine betaine/compatible-solute ABC transporters used in long-term adaptation of Natranaerobius thermophilus under haloalkaline stress (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24 / https://doi.org/10.1128/AEM.00145-24 / 2024 |  |
| SSS family Na+/solute symporters | transporter | Na+/solute symporters implicated in compatible-solute acquisition during adaptation to high-salt alkaline habitats (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24 / https://doi.org/10.1128/AEM.00145-24 / 2024 |  |
| **Cell envelope components** |  |  |  |  |
| teichuronic acid (TUA) | cell envelope component | Acidic cell-envelope polymer enriched in some alkaliphilic Bacillus cell walls; contributes to acidic surface properties and pH balance at high external pH (chia2025roleofextremophiles pages 6-8) | 10.1007/s11244-024-01919-7 / https://doi.org/10.1007/s11244-024-01919-7 / 2025 |  |
| teichuronopeptide (TUP) | cell envelope component | Acidic cell-envelope component that, with TUA/peptidoglycan, contributes to acidic cell-surface adaptation in alkaliphilic Bacillus (chia2025roleofextremophiles pages 6-8) | 10.1007/s11244-024-01919-7 / https://doi.org/10.1007/s11244-024-01919-7 / 2025 |  |
| acidic nonpeptidoglycan cell-wall polymers | cell envelope component | Negatively charged polymers that adsorb Na+ and hydronium and repel OH−, assisting growth in alkaline environments and helping reduce surface pH (horikoshi1999alkaliphilessomeapplications pages 4-5, horikoshi2016alkaliphiles pages 2-5) | 10.1128/MMBR.63.4.735-750.1999 / https://doi.org/10.1128/MMBR.63.4.735-750.1999 / 1999; 10.1007/978-4-431-55408-0_4 / https://doi.org/10.1007/978-4-431-55408-0_4 / 2016 | GO:0005618 candidate |
| peptidoglycan | cell envelope component | Structural cell-wall component contributing to protective acidic cell-envelope architecture in some alkaliphiles (chia2025roleofextremophiles pages 6-8, horikoshi2016alkaliphiles pages 2-5) | 10.1007/s11244-024-01919-7 / https://doi.org/10.1007/s11244-024-01919-7 / 2025; 10.1007/978-4-431-55408-0_4 / https://doi.org/10.1007/978-4-431-55408-0_4 / 2016 | GO:0009273 candidate |
| **Metabolites/ions** |  |  |  |  |
| glycine betaine | compatible solute | Compatible solute whose intracellular abundance increases with salinity in Natranaerobius thermophilus; part of hybrid adaptation in haloalkaline settings (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24 / https://doi.org/10.1128/AEM.00145-24 / 2024 | CHEBI:17750 |
| proline | compatible solute | Compatible solute accumulated under saline-alkaline stress and in Natranaerobius thermophilus salinity adaptation (xing2024thepolyextremophilenatranaerobius pages 1-2, wang2023salinealkalisoilproperty pages 1-2) | 10.1128/AEM.00145-24 / https://doi.org/10.1128/AEM.00145-24 / 2024; 10.3390/ijms24097737 / https://doi.org/10.3390/ijms24097737 / 2023 | CHEBI:26271 |
| glutamate | compatible solute/metabolite | Intracellular metabolite/compatible solute elevated with salinity in Natranaerobius thermophilus (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24 / https://doi.org/10.1128/AEM.00145-24 / 2024 | CHEBI:29991 |
| succinate | organic acid | Organic acid cited as part of local pH-calibration strategy in alkaliphiles (chia2025roleofextremophiles pages 6-8) | 10.1007/s11244-024-01919-7 / https://doi.org/10.1007/s11244-024-01919-7 / 2025 | CHEBI:30031 |
| lactate | organic acid | Organic acid cited as part of local pH-calibration strategy in alkaliphiles; also increased in saline-alkali tolerant Priestia aryabhattai JL-5 (chia2025roleofextremophiles pages 6-8, wang2023salinealkalisoilproperty pages 1-2) | 10.1007/s11244-024-01919-7 / https://doi.org/10.1007/s11244-024-01919-7 / 2025; 10.3390/ijms24097737 / https://doi.org/10.3390/ijms24097737 / 2023 | CHEBI:24996 |
| acetate | organic acid | Organic acid cited as part of local pH-calibration strategy in alkaliphiles (chia2025roleofextremophiles pages 6-8) | 10.1007/s11244-024-01919-7 / https://doi.org/10.1007/s11244-024-01919-7 / 2025 | CHEBI:30089 |
| Na+ | ion | Central exchanged ion in Na+/H+ antiport and sodium motive force; often specifically required by alkaliphiles (horikoshi1999alkaliphilessomeapplications pages 4-5, patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5, horikoshi2016alkaliphiles pages 2-5) | 10.1128/MMBR.63.4.735-750.1999 / https://doi.org/10.1128/MMBR.63.4.735-750.1999 / 1999; 10.3390/ijms23169156 / https://doi.org/10.3390/ijms23169156 / 2022 | CHEBI:29101 |
| K+ | ion | Intracellular ion accumulated/maintained under extreme saline-alkaline conditions to support ion homeostasis (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24 / https://doi.org/10.1128/AEM.00145-24 / 2024 | CHEBI:29103 |
| OH− | ion | Hydroxide ion repelled by acidic cell-surface polymers in classic alkaliphile cell-envelope model (horikoshi1999alkaliphilessomeapplications pages 4-5) | 10.1128/MMBR.63.4.735-750.1999 / https://doi.org/10.1128/MMBR.63.4.735-750.1999 / 1999 | CHEBI:24634 |
| **Example taxa** |  |  |  |  |
| Pseudomonas aeruginosa | example taxon | Experimental system showing that NhaB and Mrp can sustain growth across pH 6.5–8.5 and high Na+, whereas loss of all Na+/H+ antiporters causes marked Na+ sensitivity at higher pH (foreman2021geneticandbiochemical pages 12-13) | 10.1128/JB.00284-21 / https://doi.org/10.1128/JB.00284-21 / 2021 | NCBITaxon:287 |
| Natranaerobius thermophilus | example taxon | Polyextremophile from soda lakes; 2024 multi-omics study showed compatible-solute accumulation, K+ maintenance, Na+/K+/H+ transporter upregulation, and Na+-FOF1-ATPase in haloalkaline adaptation (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24 / https://doi.org/10.1128/AEM.00145-24 / 2024 | NCBITaxon:445972 candidate |
| Lactobacillus spp. | example taxon | Group used to quantify alkali tolerance by pHmax and demonstrate contribution of reversed ΔpH to alkali tolerance (sawatari2007diversityandmechanisms pages 1-1, sawatari2007diversityandmechanisms pages 6-7, sawatari2007diversityandmechanisms pages 3-5) | 10.1128/AEM.02834-06 / https://doi.org/10.1128/AEM.02834-06 / 2007 | NCBITaxon:1578 candidate |
| Natronorubrum daqingense | example taxon | Haloarchaeal system in which NhaC-family antiporters conferred resistance up to pH 8.5–9.5 and had optimal antiport activity at pH 9.5 (wang2023characterizationoftwo pages 16-16) | 10.3390/ijms241310786 / https://doi.org/10.3390/ijms241310786 / 2023 | NCBITaxon: candidate |
| alkaliphilic Bacillus spp. | example taxon group | Canonical systems for cell-envelope acidic polymer and Na+-linked alkaliphily mechanisms, including Bacillus halodurans and Bacillus lentus examples (chia2025roleofextremophiles pages 6-8, horikoshi1999alkaliphilessomeapplications pages 4-5, horikoshi2016alkaliphiles pages 2-5) | 10.1007/s11244-024-01919-7 / https://doi.org/10.1007/s11244-024-01919-7 / 2025; 10.1128/MMBR.63.4.735-750.1999 / https://doi.org/10.1128/MMBR.63.4.735-750.1999 / 1999 | NCBITaxon:1386 candidate |
| Ali-BS5-314 | example taxon/isolate | Hyperalkaline serpentinizing-system isolate growing from pH 10–12 with optimum at pH 11; useful boundary-case example of alkaliphily rather than alkalotolerance (thompson2023insightsintothe pages 5-7, thompson2023insightsintothe media ecd4bf5a) | 10.3389/fmicb.2023.1179857 / https://doi.org/10.3389/fmicb.2023.1179857 / 2023 |  |
| Paeni-Cedars | example taxon/isolate | Serpentinizing-system isolate growing from pH 7–10 with optimum pH 7–9; useful example closer to alkalotolerance because growth extends into alkaline range while optimum remains near neutral (thompson2023insightsintothe pages 5-7, thompson2023insightsintothe media ecd4bf5a) | 10.3389/fmicb.2023.1179857 / https://doi.org/10.3389/fmicb.2023.1179857 / 2023 |  |


*Table: This table lists candidate nodes for an alkalotolerant TraitMech graph, grouped by node type and annotated with roles, supporting sources, and possible ontology groundings. It is useful for translating the literature into a curation-ready set of graph entities.*

### 4) Evidence-backed candidate causal edges (triples)

Edges below are curated as subject–predicate–object claims. Each edge includes an evidence snippet and a curation note (including when evidence is alkaliphile-focused or stress-context-confounded).

| Subject node | Predicate | Object node | Evidence snippet (verbatim or near-verbatim) | Source (DOI + URL + year) | Notes/uncertainty | Suggested CURIEs (where possible) |
|---|---|---|---|---|---|---|
| alkaline external pH | increases importance of | electrogenic Na+/H+ antiport | “the negative-inside membrane potential can drive Na+ extrusion, a mechanism that is particularly important when the extracellular pH is alkaline” (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | 10.3390/ijms23169156; https://doi.org/10.3390/ijms23169156; 2022 | General prokaryotic mechanism; strong but not specific to alkalotolerant class | ENVO:alkaline environment candidate; GO:0015385 sodium:proton antiporter activity |
| NhaA | enables | Na+ extrusion | “NhaA and NhaB are electrogenic antiporters with distinct H+:Na+ stoichiometries (2:1 for NhaA, 3:2 for NhaB)” and membrane potential can drive Na+ extrusion (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | 10.3390/ijms23169156; https://doi.org/10.3390/ijms23169156; 2022 | Mechanistic edge well supported; exact organism context often E. coli | TCDB family-level candidate; GO:0015385 |
| NhaA | supports | growth at alkaline pH | “why NhaA supports the growth of E. coli at alkaline pH, whereas NhaB does not” (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | 10.3390/ijms23169156; https://doi.org/10.3390/ijms23169156; 2022 | Species-specific to E. coli; useful as prototype antiporter evidence | NCBITaxon:562; GO:0015385 |
| nhaA and nhaB deletion | prevents | growth at moderate Na+ | “Deletion of both nhaA and nhaB genes prevents the growth of E. coli at even moderate Na+ concentrations” (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | 10.3390/ijms23169156; https://doi.org/10.3390/ijms23169156; 2022 | Salt + pH homeostasis evidence; indirect for alkalotolerance | NCBITaxon:562; GO:0015385 |
| Mrp Na+/H+ antiporter complex | rescues | alkaline-sensitive growth phenotype | “an Mrp Na+/H+ exchanger was identified by its ability to ‘rescue’ growth of an alkaline-sensitive strain” (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5) | 10.3390/ijms23169156; https://doi.org/10.3390/ijms23169156; 2022 | Strong classic causal edge; taxon-specific rescue assay | GO:0015385; Mrp complex label-only candidate |
| Mrp and NhaB | sustains | growth across high pH and Na+ | “strains with only NhaB or only Mrp sustain growth similar to wild type across pH 6.5–8.5 and high Na+” (foreman2021geneticandbiochemical pages 12-13) | 10.1128/JB.00284-21; https://doi.org/10.1128/JB.00284-21; 2021 | Pseudomonas aeruginosa-specific but direct physiological evidence | NCBITaxon:287; GO:0015385 |
| loss of all four Na+/H+ antiporters | increases sensitivity to | Na+ at higher pH | “deleting them produces a strain that is highly sensitive to Na+, especially at higher pH (minimal or no growth at 50 mM Na+ at pH 8.5)” (foreman2021geneticandbiochemical pages 12-13) | 10.1128/JB.00284-21; https://doi.org/10.1128/JB.00284-21; 2021 | Strong mutant phenotype; supports antiporter importance | NCBITaxon:287; GO:0015385 |
| acidic nonpeptidoglycan cell-surface polymers | assists growth in | alkaline environments | “may give the cell surface its ability to adsorb sodium and hydronium ions and repulse hydroxide ions and, as a consequence, may assist cells to grow in alkaline environments” (horikoshi1999alkaliphilessomeapplications pages 4-5) | 10.1128/MMBR.63.4.735-750.1999; https://doi.org/10.1128/MMBR.63.4.735-750.1999; 1999 | Foundational, authoritative, but older and mostly alkaliphile-focused | GO:0005618 cell wall; acidic polymer label-only candidate |
| acidic nonpeptidoglycan polymers | adsorbs | sodium and hydronium ions | “adsorb sodium and hydronium ions and repulse hydroxide ions” (horikoshi1999alkaliphilessomeapplications pages 4-5) | 10.1128/MMBR.63.4.735-750.1999; https://doi.org/10.1128/MMBR.63.4.735-750.1999; 1999 | Cell-envelope chemistry mechanism; older source | CHEBI:29101 sodium(1+); CHEBI:15378 hydron |
| acidic nonpeptidoglycan polymers | repels | hydroxide | “repulse hydroxide ions” (horikoshi1999alkaliphilessomeapplications pages 4-5) | 10.1128/MMBR.63.4.735-750.1999; https://doi.org/10.1128/MMBR.63.4.735-750.1999; 1999 | Same mechanism as above; older but explicit | CHEBI:24634 hydroxide |
| external pH 8–11 | coexists with | internal pH ~8 | “internal pH was maintained at around 8, despite a high external pH of 8 to 11” (horikoshi1999alkaliphilessomeapplications pages 4-5) | 10.1128/MMBR.63.4.735-750.1999; https://doi.org/10.1128/MMBR.63.4.735-750.1999; 1999 | Key phenotype-level homeostasis edge; mostly alkaliphiles | GO:0051453 regulation of intracellular pH |
| cell-surface acidic polymers / cell wall | helps maintain | intracellular pH around 9 | “acidic non-peptidoglycan polymers in cell walls create negative charges that function as a matrix to reduce pH at the cell surface and help keep intracellular pH around 9” (horikoshi2016alkaliphiles pages 2-5) | 10.1007/978-4-431-55408-0_4; https://doi.org/10.1007/978-4-431-55408-0_4; 2016 | Conceptual synthesis; phrasing from chapter summary | GO:0051453; GO:0005618 |
| reversed ΔpH in alkaline conditions | contributes to | alkali tolerance | “the reversed ΔpH formed in alkaline conditions contributes to the alkali tolerance of the tested Lactobacillus strains” (sawatari2007diversityandmechanisms pages 3-5) | 10.1128/AEM.02834-06; https://doi.org/10.1128/AEM.02834-06; 2007 | Direct physiological evidence; applies to Lactobacillus | GO:0051453; NCBITaxon:1578 candidate |
| nigericin treatment | reduces | pHmax for growth | “dissipating the reversed pH with nigericin reduced the pHmax for growth by ~0.5” (sawatari2007diversityandmechanisms pages 6-7) | 10.1128/AEM.02834-06; https://doi.org/10.1128/AEM.02834-06; 2007 | Strong intervention evidence; assay-specific | CHEBI:29107 nigericin candidate; pHmax label-only candidate |
| ATP-driven K+/H+ antiporter and/or Na+/H+ antiporter | contributes to | reversed pH under alkaline conditions | “The reversed pH is said to arise likely from the Donnan potential and/or energy-dependent antiporters (ATP-dependent K+/H+ antiporters and Na(K)/H antiporter(s))” (sawatari2007diversityandmechanisms pages 6-7) | 10.1128/AEM.02834-06; https://doi.org/10.1128/AEM.02834-06; 2007 | More tentative (“likely”); curate as uncertain | GO:0015385; K+/H+ antiporter label-only candidate |
| high Na+/salt stress | upregulates | Na+/K+/H+ transporters | “the upregulation of Na+/ K+/ H+ transporters facilitates the maintenance of intracellular K+ concentration, ensuring cellular ion homeostasis” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24; https://doi.org/10.1128/AEM.00145-24; 2024 | Strong recent primary evidence, but from combined salinity/alkaline polyextremophile | NCBITaxon:Natranaerobius thermophilus candidate; GO:0015385 |
| Na+/K+/H+ transporter upregulation | facilitates maintenance of | intracellular K+ concentration | “facilitates the maintenance of intracellular K+ concentration, ensuring cellular ion homeostasis” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24; https://doi.org/10.1128/AEM.00145-24; 2024 | Strong direct mechanistic statement | CHEBI:29103 potassium(1+); ion homeostasis label-only candidate |
| high Na+/salt stress | increases accumulation of | glycine betaine, glutamate, proline | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24; https://doi.org/10.1128/AEM.00145-24; 2024 | Strong recent evidence, but salinity-centered; relevance to alkalotolerance is indirect unless coupled with haloalkaline settings | CHEBI:17750 glycine betaine; CHEBI:29991 L-glutamate; CHEBI:26271 L-proline |
| Na+-translocating FOF1-ATPase | supports | Na+-based bioenergetics / adaptation to extremes | “a large set of Na+(K+)/H+ antiporters and a Na+-translocating FOF1-ATPase are present and upregulated, which the authors link to adaptation to extremes” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/AEM.00145-24; https://doi.org/10.1128/AEM.00145-24; 2024 | Good recent evidence; combined stress context | GO:0046933 proton-transporting ATP synthase complex, rotational mechanism candidate |
| sodium motive force | supports | intracellular pH control | “a sodium motive force mediated by Na+/H+ antiporters, Na+ channels or stator proteins supports intracellular pH control” (chia2025roleofextremophiles pages 6-8) | 10.1007/s11244-024-01919-7; https://doi.org/10.1007/s11244-024-01919-7; 2025 | Review-level synthesis; broad, not trait-specific | sodium motive force label-only candidate; GO:0051453 |
| production of succinate/lactate/acetate | acts as | local pH calibration strategy | “metabolic generation/release of organic acids (e.g., succinate, lactate, acetate) acts as a local pH-calibration strategy” (chia2025roleofextremophiles pages 6-8) | 10.1007/s11244-024-01919-7; https://doi.org/10.1007/s11244-024-01919-7; 2025 | More general/less direct to alkalotolerant trait; curate cautiously | CHEBI:30031 succinate; CHEBI:24996 lactate; CHEBI:30089 acetate |


*Table: This table compiles candidate subject-predicate-object edges for an alkalotolerance causal graph, with source-backed snippets, DOI/URL citations, and curation notes. It is designed to support direct TraitMech curation while flagging taxon-specific or indirect claims.*

### 5) Recent developments and latest research (prioritizing 2023–2024)

**2024: multi-omics dissection of a soda-lake polyextremophile.** In *Natranaerobius thermophilus* (an alkalithermophile from hypersaline alkaline systems), proteomics and targeted assays support a **hybrid “compatible-solute + salt-in” strategy** with **upregulation of Na+/K+/H+ transporters** and a **Na+-translocating FOF1-ATPase**, along with measured **increases in intracellular compatible solutes (glycine betaine, glutamate, proline)** and **K+** under rising salinity; this provides a current, systems-level view of ion/solute modules often embedded in haloalkaline tolerance. (xing2024thepolyextremophilenatranaerobius pages 1-2)

**2023: transporter discovery in haloarchaea at alkaline pH.** Two Na+(K+,Li+)/H+ antiporters (NhaC-family) from *Natronorubrum daqingense* conferred host tolerance to alkaline pH (up to pH 8.5/9.5 depending on gene) and had optimal activity at pH 9.5, supporting archaeal extension of the antiporter-centered alkalinity module. (wang2023characterizationoftwo pages 16-16)

**2023: physiological characterization of hyperalkaline isolates.** Isolates from a terrestrial serpentinizing system include strains with growth spanning neutral to alkaline (pH 7–10) and obligately alkaliphilic growth (pH 10–12), reinforcing that **growth range/optimum** is a practical discriminator for curation of “alkalotolerant” vs “alkaliphilic” traits. (thompson2023insightsintothe media ecd4bf5a)

### 6) Current applications and real-world implementations (with recent quantitative data)

**Saline-alkali soil and crop productivity (field-scale evidence).** A 2025 coastal saline-alkali field experiment reported that **co-inoculation** with *Bacillus subtilis* and *Bradyrhizobium liaoningense* increased soybean yield to **3182.67 kg/hm²** (**+18.03%**) relative to conventional fertilization, with improvements in rhizosphere soil indicators: **pH −2.8%**, electrical conductivity **−11.0%**, and total water-soluble salts **−5.4%**; soil enzyme activities increased (e.g., alkaline phosphatase **+14.9%**, sucrase **+22.4%**). This is a recent example of deploying alkali/saline-tolerant microbes in real agricultural alkaline-sodic settings. (he2025coinoculationofbacillus pages 1-2)

**Rhizosphere engineering under alkaline–sodic stress (2024 mechanistic implementation).** A 2024 study using *Bacillus altitudinis* AD13-4 (selected on carbonate medium at pH 8.0) found inoculation reshaped rhizosphere community composition and improved soil functional indicators under saline–alkali stress (with deep sequencing coverage >97%). While the excerpted sections emphasize community and enzyme restoration rather than providing a single headline % yield figure, it documents real-world implementable screening and microbial inoculation workflows for alkaline–sodic contexts. (khoso2024bacillusaltitudinisad13−4 pages 11-14, khoso2024bacillusaltitudinisad13−4 pages 2-3)

**Industrial biotechnology context (expert synthesis).** Classic but still authoritative synthesis highlights that alkaliphiles/alkali-tolerant microbes have historically enabled industrial alkaline enzymes (e.g., detergent enzymes) and alkaline bioprocessing where enzymes must function stably at elevated pH. This provides mechanistic/engineering framing but should not be used alone for edge-level curation without newer, mechanism-specific sources for each application. (horikoshi1999alkaliphilessomeapplications pages 1-3)

### 7) Expert opinions / authoritative analysis (how to interpret the trait)

- **Definitions are operational rather than absolute.** Horikoshi emphasizes that precise definitions can be difficult because some microorganisms exhibit multiple pH optima depending on conditions, motivating the curation practice of anchoring the trait to **measured growth optima and growth ranges**, plus mechanistic readouts (cytoplasmic pH). (horikoshi1999alkaliphilessomeapplications pages 1-3)
- **Mechanistic convergence is common:** independent lineages frequently converge on the same core modules—**Na+/H+ antiport**, **cell-envelope charge/chemistry**, and **maintenance of internal pH near neutrality**—consistent with alkaline pH presenting a shared physicochemical constraint. (horikoshi1999alkaliphilessomeapplications pages 4-5, patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5)

### 8) Warnings / curation cautions (do not curate yet or mark uncertain)

1. **Haloalkaline confounding:** Many mechanistic studies in soda-lake organisms are driven by combined extremes (high Na+, alkalinity, sometimes temperature). Edges from such sources (e.g., compatible-solute accumulation) should be flagged as **“contextual/likely contributing”** rather than as uniquely alkalotolerance-specific, unless alkaline pH was independently varied. (xing2024thepolyextremophilenatranaerobius pages 1-2)
2. **Alkaliphile-to-alkalotolerant transfer:** Classic cell-wall polymer and “internal pH ~8” models are often drawn from **alkaliphiles**. They are useful as mechanistic hypotheses for alkalotolerant taxa, but curation should note whether a source explicitly studied **alkalotolerant (neutral-optimum) organisms**. (horikoshi1999alkaliphilessomeapplications pages 4-5, horikoshi2016alkaliphiles pages 2-5)
3. **Transporter family generalization:** Evidence for NhaA/NhaB/Mrp causal importance is strong in particular taxa (e.g., *E. coli*, *P. aeruginosa*). When curating edges, note taxon scope or represent the node at the **functional level (Na+/H+ antiport activity)** rather than asserting universal gene-level causality. (foreman2021geneticandbiochemical pages 12-13, patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5)

---

## DOI-first bibliography (with URLs and publication dates)

1. **Xing Q. et al.** (May 2024). *Applied and Environmental Microbiology.* “The polyextremophile **Natranaerobius thermophilus** adopts a dual adaptive strategy…” DOI: **10.1128/aem.00145-24**. https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2)
2. **Thompson J. et al.** (Jul 2023). *Frontiers in Microbiology.* “Insights into the physiological and genomic characterization…” DOI: **10.3389/fmicb.2023.1179857**. https://doi.org/10.3389/fmicb.2023.1179857 (thompson2023insightsintothe media ecd4bf5a)
3. **Wang Q. et al.** (Jun 2023). *International Journal of Molecular Sciences.* “Characterization of Two Na+(K+, Li+)/H+ Antiporters…” DOI: **10.3390/ijms241310786**. https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 16-16)
4. **Patiño-Ruiz M. et al.** (Aug 2022). *International Journal of Molecular Sciences.* “Prokaryotic Na+/H+ Exchangers—Transport Mechanism…” DOI: **10.3390/ijms23169156**. https://doi.org/10.3390/ijms23169156 (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5)
5. **Foreman S. et al.** (Aug 2021). *Journal of Bacteriology.* “Genetic and Biochemical Characterization of the Na+/H+ Antiporters…” DOI: **10.1128/jb.00284-21**. https://doi.org/10.1128/jb.00284-21 (foreman2021geneticandbiochemical pages 12-13)
6. **Gondal A.H. et al.** (Jan 2021). *Current Research in Agricultural Sciences.* “Adaptability of Soil pH through Innovative Microbial Approach” DOI: **10.18488/journal.68.2021.82.71.79**. https://doi.org/10.18488/journal.68.2021.82.71.79 (gondal2021adaptabilityofsoil pages 3-4)
7. **Sawatari Y., Yokota A.** (Jun 2007). *Applied and Environmental Microbiology.* “Diversity and Mechanisms of Alkali Tolerance in Lactobacilli” DOI: **10.1128/aem.02834-06**. https://doi.org/10.1128/aem.02834-06 (sawatari2007diversityandmechanisms pages 6-7)
8. **Horikoshi K.** (Dec 1999). *Microbiology and Molecular Biology Reviews.* “Alkaliphiles: Some Applications of Their Products for Biotechnology” DOI: **10.1128/mmbr.63.4.735-750.1999**. https://doi.org/10.1128/mmbr.63.4.735-750.1999 (horikoshi1999alkaliphilessomeapplications pages 1-3)
9. **Horikoshi K.** (Jan 2016). Book chapter “Alkaliphiles.” DOI: **10.1007/978-4-431-55408-0_4**. https://doi.org/10.1007/978-4-431-55408-0_4 (horikoshi2016alkaliphiles pages 1-2)
10. **He C. et al.** (Oct 2025). *Frontiers in Plant Science.* “Co-inoculation of Bacillus subtilis and Bradyrhizobium…” DOI: **10.3389/fpls.2025.1677763**. https://doi.org/10.3389/fpls.2025.1677763 (he2025coinoculationofbacillus pages 1-2)
11. **Khoso M.A. et al.** (May 2024). *International Journal of Molecular Sciences.* “Bacillus altitudinis AD13−4 Enhances Saline–Alkali Stress Tolerance…” DOI: **10.3390/ijms25115785**. https://doi.org/10.3390/ijms25115785 (khoso2024bacillusaltitudinisad13−4 pages 11-14)
12. **Wang Y. et al.** (Apr 2023). *International Journal of Molecular Sciences.* “Saline-Alkali Soil Property Improved…” DOI: **10.3390/ijms24097737**. https://doi.org/10.3390/ijms24097737 (wang2023salinealkalisoilproperty pages 1-2)

### Visual evidence used
- Cropped table showing growth pH ranges/optima for hyperalkaline isolates (useful for boundary definitions). (thompson2023insightsintothe media ecd4bf5a)

References

1. (horikoshi1999alkaliphilessomeapplications pages 1-3): Koki Horikoshi. Alkaliphiles: some applications of their products for biotechnology. Microbiology and Molecular Biology Reviews, 63:735-750, Dec 1999. URL: https://doi.org/10.1128/mmbr.63.4.735-750.1999, doi:10.1128/mmbr.63.4.735-750.1999. This article has 1278 citations and is from a domain leading peer-reviewed journal.

2. (gondal2021adaptabilityofsoil pages 3-4): Aqarab Husnain Gondal, Qammar Farooq, Sidra Sohail, Shamal Shasang Kumar, Muhammad Danish Toor, Asma Zafar, and Bushra Rehman. Adaptability of soil ph through innovative microbial approach. Current Research in Agricultural Sciences, 8:71-79, Jan 2021. URL: https://doi.org/10.18488/journal.68.2021.82.71.79, doi:10.18488/journal.68.2021.82.71.79. This article has 37 citations.

3. (horikoshi2016alkaliphiles pages 1-2): Koki Horikoshi. Alkaliphiles, pages 53-78. Springer Japan, Jan 2016. URL: https://doi.org/10.1007/978-4-431-55408-0\_4, doi:10.1007/978-4-431-55408-0\_4. This article has 71 citations and is from a peer-reviewed journal.

4. (thompson2023insightsintothe media ecd4bf5a): Jaclyn Thompson, Casey Barr, Lydia Babcock-Adams, Lina Bird, Eugenio La Cava, Arkadiy Garber, Yuichi Hongoh, Mark Liu, Kenneth H. Nealson, Akihiro Okamoto, Daniel Repeta, Shino Suzuki, Clarissa Tacto, Michelle Tashjian, and Nancy Merino. Insights into the physiological and genomic characterization of three bacterial isolates from a highly alkaline, terrestrial serpentinizing system. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1179857, doi:10.3389/fmicb.2023.1179857. This article has 7 citations and is from a peer-reviewed journal.

5. (sawatari2007diversityandmechanisms pages 1-1): Yuki Sawatari and Atsushi Yokota. Diversity and mechanisms of alkali tolerance in lactobacilli. Applied and Environmental Microbiology, 73:3909-3915, Jun 2007. URL: https://doi.org/10.1128/aem.02834-06, doi:10.1128/aem.02834-06. This article has 64 citations and is from a peer-reviewed journal.

6. (horikoshi1999alkaliphilessomeapplications pages 4-5): Koki Horikoshi. Alkaliphiles: some applications of their products for biotechnology. Microbiology and Molecular Biology Reviews, 63:735-750, Dec 1999. URL: https://doi.org/10.1128/mmbr.63.4.735-750.1999, doi:10.1128/mmbr.63.4.735-750.1999. This article has 1278 citations and is from a domain leading peer-reviewed journal.

7. (horikoshi2016alkaliphiles pages 2-5): Koki Horikoshi. Alkaliphiles, pages 53-78. Springer Japan, Jan 2016. URL: https://doi.org/10.1007/978-4-431-55408-0\_4, doi:10.1007/978-4-431-55408-0\_4. This article has 71 citations and is from a peer-reviewed journal.

8. (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5): Miyer Patiño-Ruiz, Constanța Ganea, and Octavian Călinescu. Prokaryotic na+/h+ exchangers—transport mechanism and essential residues. International Journal of Molecular Sciences, 23:9156, Aug 2022. URL: https://doi.org/10.3390/ijms23169156, doi:10.3390/ijms23169156. This article has 27 citations.

9. (foreman2021geneticandbiochemical pages 12-13): Sara Foreman, Kristina Ferrara, Teri N. Hreha, Ana E. Duran-Pinedo, Jorge Frias-Lopez, and Blanca Barquera. Genetic and biochemical characterization of the na <sup>+</sup> /h <sup>+</sup> antiporters of pseudomonas aeruginosa. Aug 2021. URL: https://doi.org/10.1128/jb.00284-21, doi:10.1128/jb.00284-21. This article has 11 citations and is from a peer-reviewed journal.

10. (chia2025roleofextremophiles pages 6-8): Xing Kai Chia, Tony Hadibarata, Muhammad Noor Hazwan Jusoh, Lies Indah Sutiknowati, Inn Shi Tan, and Henry Chee Yew Foo. Role of extremophiles in biodegradation of emerging pollutants. Topics in Catalysis, Feb 2025. URL: https://doi.org/10.1007/s11244-024-01919-7, doi:10.1007/s11244-024-01919-7. This article has 28 citations and is from a peer-reviewed journal.

11. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

12. (sawatari2007diversityandmechanisms pages 6-7): Yuki Sawatari and Atsushi Yokota. Diversity and mechanisms of alkali tolerance in lactobacilli. Applied and Environmental Microbiology, 73:3909-3915, Jun 2007. URL: https://doi.org/10.1128/aem.02834-06, doi:10.1128/aem.02834-06. This article has 64 citations and is from a peer-reviewed journal.

13. (sawatari2007diversityandmechanisms pages 3-5): Yuki Sawatari and Atsushi Yokota. Diversity and mechanisms of alkali tolerance in lactobacilli. Applied and Environmental Microbiology, 73:3909-3915, Jun 2007. URL: https://doi.org/10.1128/aem.02834-06, doi:10.1128/aem.02834-06. This article has 64 citations and is from a peer-reviewed journal.

14. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

15. (patinoruiz2022prokaryoticna+h+exchangers—transport pages 19-20): Miyer Patiño-Ruiz, Constanța Ganea, and Octavian Călinescu. Prokaryotic na+/h+ exchangers—transport mechanism and essential residues. International Journal of Molecular Sciences, 23:9156, Aug 2022. URL: https://doi.org/10.3390/ijms23169156, doi:10.3390/ijms23169156. This article has 27 citations.

16. (wang2023characterizationoftwo pages 16-16): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

17. (patinoruiz2022prokaryoticna+h+exchangers—transport pages 23-23): Miyer Patiño-Ruiz, Constanța Ganea, and Octavian Călinescu. Prokaryotic na+/h+ exchangers—transport mechanism and essential residues. International Journal of Molecular Sciences, 23:9156, Aug 2022. URL: https://doi.org/10.3390/ijms23169156, doi:10.3390/ijms23169156. This article has 27 citations.

18. (patinoruiz2022prokaryoticna+h+exchangers—transport pages 20-22): Miyer Patiño-Ruiz, Constanța Ganea, and Octavian Călinescu. Prokaryotic na+/h+ exchangers—transport mechanism and essential residues. International Journal of Molecular Sciences, 23:9156, Aug 2022. URL: https://doi.org/10.3390/ijms23169156, doi:10.3390/ijms23169156. This article has 27 citations.

19. (patinoruiz2022prokaryoticna+h+exchangers—transport pages 8-10): Miyer Patiño-Ruiz, Constanța Ganea, and Octavian Călinescu. Prokaryotic na+/h+ exchangers—transport mechanism and essential residues. International Journal of Molecular Sciences, 23:9156, Aug 2022. URL: https://doi.org/10.3390/ijms23169156, doi:10.3390/ijms23169156. This article has 27 citations.

20. (wang2023salinealkalisoilproperty pages 1-2): Yujue Wang, Yan Wang, Qian Zhang, Hangzhe Fan, Xinyu Wang, Jianan Wang, Ying Zhou, Zhanyu Chen, Fengjie Sun, and Xiyan Cui. Saline-alkali soil property improved by the synergistic effects of priestia aryabhattai jl-5, staphylococcus pseudoxylosus xw-4, leymus chinensis and soil microbiota. International Journal of Molecular Sciences, 24:7737, Apr 2023. URL: https://doi.org/10.3390/ijms24097737, doi:10.3390/ijms24097737. This article has 20 citations.

21. (thompson2023insightsintothe pages 5-7): Jaclyn Thompson, Casey Barr, Lydia Babcock-Adams, Lina Bird, Eugenio La Cava, Arkadiy Garber, Yuichi Hongoh, Mark Liu, Kenneth H. Nealson, Akihiro Okamoto, Daniel Repeta, Shino Suzuki, Clarissa Tacto, Michelle Tashjian, and Nancy Merino. Insights into the physiological and genomic characterization of three bacterial isolates from a highly alkaline, terrestrial serpentinizing system. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1179857, doi:10.3389/fmicb.2023.1179857. This article has 7 citations and is from a peer-reviewed journal.

22. (he2025coinoculationofbacillus pages 1-2): Caizhi He, Tongguo Gao, Xinxin Wang, Renqiang Chen, Huiyan Gao, and Hongquan Liu. Co-inoculation of bacillus subtilis and bradyrhizobium liaoningense increased soybean yield and improved soil bacterial community composition in coastal saline-alkali land. Frontiers in Plant Science, Oct 2025. URL: https://doi.org/10.3389/fpls.2025.1677763, doi:10.3389/fpls.2025.1677763. This article has 7 citations.

23. (khoso2024bacillusaltitudinisad13−4 pages 11-14): Muneer Ahmed Khoso, Mingyu Wang, Zhenzhen Zhou, Yongxue Huang, Shenglin Li, Yiming Zhang, Guangtao Qian, Song Nam Ko, Qiuying Pang, Changli Liu, and Lixin Li. Bacillus altitudinis ad13−4 enhances saline–alkali stress tolerance of alfalfa and affects composition of rhizosphere soil microbial community. International Journal of Molecular Sciences, 25:5785, May 2024. URL: https://doi.org/10.3390/ijms25115785, doi:10.3390/ijms25115785. This article has 27 citations.

24. (khoso2024bacillusaltitudinisad13−4 pages 2-3): Muneer Ahmed Khoso, Mingyu Wang, Zhenzhen Zhou, Yongxue Huang, Shenglin Li, Yiming Zhang, Guangtao Qian, Song Nam Ko, Qiuying Pang, Changli Liu, and Lixin Li. Bacillus altitudinis ad13−4 enhances saline–alkali stress tolerance of alfalfa and affects composition of rhizosphere soil microbial community. International Journal of Molecular Sciences, 25:5785, May 2024. URL: https://doi.org/10.3390/ijms25115785, doi:10.3390/ijms25115785. This article has 27 citations.