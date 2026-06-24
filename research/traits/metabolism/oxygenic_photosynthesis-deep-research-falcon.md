---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:27:45.854262'
end_time: '2026-06-18T05:41:47.171098'
duration_seconds: 841.32
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: oxygenic photosynthesis
  trait_identifier: traitmech:000034
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: oxygenic_photosynthesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phototrophic metabolism that uses light energy to fix CO2, oxidizing
    water as the electron donor and releasing molecular oxygen. It uses two linked
    photosystems and chlorophyll, and is characteristic of cyanobacteria (and plant
    chloroplasts).
  parent_traits: traitmech:000038
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic
    photosynthesis and phototrophy illuminated", contrasts oxygenic photosynthesis
    (water-splitting, O2-evolving) in cyanobacteria with anoxygenic phototrophy.)
    | DOI:10.1146/annurev-earth-060313-054810:  (Fischer et al., "Evolution of Oxygenic
    Photosynthesis", supports water-oxidizing, oxygen-evolving photosynthesis as a
    distinct, cyanobacterial innovation.)'
  causal_graph_summary: 'oxygenic_photosynthesis_water_splitting: 4 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** oxygenic photosynthesis
- **METPO identifier:** traitmech:000034
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy to fix CO2, oxidizing water as the electron donor and releasing molecular oxygen. It uses two linked photosystems and chlorophyll, and is characteristic of cyanobacteria (and plant chloroplasts).
- **Parent traits:** traitmech:000038
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", contrasts oxygenic photosynthesis (water-splitting, O2-evolving) in cyanobacteria with anoxygenic phototrophy.) | DOI:10.1146/annurev-earth-060313-054810:  (Fischer et al., "Evolution of Oxygenic Photosynthesis", supports water-oxidizing, oxygen-evolving photosynthesis as a distinct, cyanobacterial innovation.)
- **Existing causal graph summary:** oxygenic_photosynthesis_water_splitting: 4 nodes, 2 edges

## Research Objective

Research the microbial trait **oxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/oxygenic_photosynthesis.yaml`.

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
- **Trait label:** oxygenic photosynthesis
- **METPO identifier:** traitmech:000034
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy to fix CO2, oxidizing water as the electron donor and releasing molecular oxygen. It uses two linked photosystems and chlorophyll, and is characteristic of cyanobacteria (and plant chloroplasts).
- **Parent traits:** traitmech:000038
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", contrasts oxygenic photosynthesis (water-splitting, O2-evolving) in cyanobacteria with anoxygenic phototrophy.) | DOI:10.1146/annurev-earth-060313-054810:  (Fischer et al., "Evolution of Oxygenic Photosynthesis", supports water-oxidizing, oxygen-evolving photosynthesis as a distinct, cyanobacterial innovation.)
- **Existing causal graph summary:** oxygenic_photosynthesis_water_splitting: 4 nodes, 2 edges

## Research Objective

Research the microbial trait **oxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/oxygenic_photosynthesis.yaml`.

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


# Oxygenic Photosynthesis (traitmech:000034) — Curation-Focused Research Report (2023–2024 emphasis)

## Scope summary (TraitMech intent)
**Oxygenic photosynthesis** is a phototrophic metabolism defined by **light-driven water oxidation at Photosystem II (PSII)** producing **molecular oxygen (O2)** and **electrons** that flow through an electron transport chain (ETC) to Photosystem I (PSI), generating **NADPH** and a **proton motive force (pmf)** used for **ATP synthesis**, which together power **CO2 fixation** (typically via the Calvin–Benson–Bassham (CBB) cycle). This definition is explicitly captured in recent authoritative reviews describing PSII as the catalyst of water oxidation (OEC/Mn4CaO5) and PSII/PSI as central drivers of oxygenic photosynthesis. (shevela2023solarenergyconversion pages 1-2, shevela2023solarenergyconversion pages 2-4, vinyard2024bicarbonateisa pages 1-3, grettenberger2024limitingfactorsin pages 2-4)

**Boundary cases / trait discrimination**:
- **Bicarbonate is not a substrate** for O2 evolution; it is described as a **regulator** (acceptor-side non-heme iron ligand and/or proton-transfer facilitator) rather than an O-atom source for O2, despite recurring alternative hypotheses. (vinyard2024bicarbonateisa pages 1-3, shevela2023solarenergyconversion pages 4-5, vinyard2024bicarbonateisa pages 3-4)
- Assemblies or physiological states where PSII lacks a functional **oxygen-evolving complex (OEC)** should not be curated as “oxygenic photosynthesis,” even if other photochemistry is present (i.e., oxygen evolution is the defining assayable outcome). (vinyard2024bicarbonateisa pages 1-3, shevela2023solarenergyconversion pages 2-4)

## 1) Key concepts and definitions (current understanding)
### Defining mechanistic features
1. **Water is the electron donor; O2 is released**: PSII oxidizes water at the Mn4CaOx oxygen-evolving complex (OEC), producing O2 while extracting electrons and protons from H2O. (vinyard2024bicarbonateisa pages 1-3, shevela2023solarenergyconversion pages 2-4, shevela2023solarenergyconversion pages 9-10)
2. **Two linked photosystems**: Oxygenic photosynthesis is driven by PSII and PSI in thylakoid membranes, connected by mobile carriers (plastoquinone/plastoquinol; plastocyanin or cytochrome c6) and cytochrome b6f. (shevela2023solarenergyconversion pages 1-2, grettenberger2024limitingfactorsin pages 1-2, milrad2024regulationofmicroalgal pages 1-3)
3. **Chemiosmotic coupling**: Electron transfer generates a transmembrane pmf (ΔpH + ΔΨ) that drives ATP synthesis by ATP synthase; NADPH is produced via PSI → ferredoxin → FNR. (shevela2023solarenergyconversion pages 2-4, milrad2024regulationofmicroalgal pages 1-3, grettenberger2024limitingfactorsin pages 2-4)

### PSII donor-side mechanism (OEC; Kok cycle)
- The **Kok S-state cycle** describes “period-four” accumulation of four oxidizing equivalents before O2 formation; proton-coupled electron transfer and structured water/proton channels support water access and proton release. (shevela2023solarenergyconversion pages 12-13, shevela2023solarenergyconversion pages 14-16, shevela2023solarenergyconversion pages 9-10)
- The redox-active **TyrZ (YZ)** mediates electron transfer from the OEC toward the primary photo-oxidant (P680•+), linking photochemistry to catalysis. (shevela2023solarenergyconversion pages 9-10, shevela2023solarenergyconversion pages 12-13)

### ETC modules and energetic outputs
- Canonical flow in oxygenic systems: **PSII → PQ/PQH2 → cytochrome b6f → plastocyanin (or cytochrome c6) → PSI → ferredoxin → FNR → NADPH**; the pmf drives ATP synthesis. (grettenberger2024limitingfactorsin pages 1-2, milrad2024regulationofmicroalgal pages 1-3, grettenberger2024limitingfactorsin pages 2-4)
- **Cyclic electron transport (CET/CEF)** around PSI (not producing NADPH) can return electrons to the PQ pool (often via NDH-1), increasing pmf/ATP and helping manage redox balance and oxidative stress. (grettenberger2024limitingfactorsin pages 4-5, shevela2023solarenergyconversion pages 2-4)

## 2) Recent developments and latest research (prioritize 2023–2024)
### High-resolution PSII mechanism focus (2023–2024)
- A 2023 PSII synthesis emphasizes **high-resolution structures** of PSII intermediates and mechanistic mapping of water oxidation chemistry (overall reaction including PQ reduction and lumenal proton release), highlighting remaining open questions about O–O bond formation pathways. (shevela2023solarenergyconversion pages 2-4, shevela2023solarenergyconversion pages 14-16)
- 2024 work continues to refine donor-side chemistry with theoretical/quantum mechanistic proposals for O–O bond formation that explicitly incorporate **Ca(H2O)n involvement** and **YZ-coupled** electron transfer, integrating evidence from advanced spectroscopy/XFEL/FTIR. (yamaguchi2024theoreticalelucidationof pages 1-2)

### Bicarbonate controversy clarification (2024)
- A 2024 perspective explicitly argues bicarbonate is a **key regulator** but **not a substrate** of O2 evolution, noting that biochemical/spectroscopic/structural studies fail to detect bicarbonate near the OEC active site; bicarbonate’s key role is positioned at the acceptor side (non-heme iron ligand) and in proton handling/assembly acceleration. (vinyard2024bicarbonateisa pages 1-3, vinyard2024bicarbonateisa pages 3-4)

### Cyanobacterial CCM coupling to photosynthesis (2024)
- 2024 reviews provide a detailed, component-resolved view of the cyanobacterial **carbon concentrating mechanism (CCM)** linking Ci transport (BCT1, BicA, SbtA), thylakoid NDH-1 variants (NDH-1₃/CupA; NDH-1₄/CupB), and **carboxysomes** (Rubisco + carbonic anhydrase) that convert HCO3− → CO2 proximal to Rubisco. (kurkela2024inorganiccarbonsensing pages 3-3, kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 1-2)
- Newer modeling-focused work emphasizes carboxysome shell permeability/architecture as a design parameter for engineered carbon fixation; the review notes carboxysome function is to create a favorable microenvironment and discusses computational approaches to pore-mediated diffusion and assembly. (trettel2024modelingbacterialmicrocompartment pages 1-2, trettel2024modelingbacterialmicrocompartment pages 2-3)

## 3) Current applications and real-world implementations
### Cyanobacteria as biotechnology chassis (2024 synthesis)
Cyanobacteria are described as attractive platforms due to diverse growth environments, tractable genetics, and biotechnological uses including **bioplastics, biofertilizers, carbon capture, biofuels, and secondary metabolites**. (grettenberger2024limitingfactorsin pages 1-2, grettenberger2024limitingfactorsin pages 8-9)

Practical constraints for implementations include light regime management (self-shading, fluctuating light), nutrient/metal supply (Fe, Mn, Cu, etc.), and stressors (UV, salinity, temperature), all of which can limit photosystem function and product yield. (grettenberger2024limitingfactorsin pages 8-9, grettenberger2024limitingfactorsin pages 5-7, grettenberger2024limitingfactorsin pages 7-8)

### Photosynthesis-linked hydrogen/solar fuels concepts (2024)
Recent application-focused discussion highlights the use of oxygenic photosynthesis and phototroph biomass in broader clean-energy strategies (biohydrogen/artificial photosynthesis framing), emphasizing scale-up constraints like light penetration and competing metabolic sinks. (kossalbayev2024photosynthesisandhydrogen pages 2-3)

## 4) Expert opinions / authoritative analysis (as represented in recent reviews)
- **PSII-centered definition**: PSII water oxidation is treated as the defining biochemical innovation of oxygenic photosynthesis and a template for renewable-energy catalysts. (shevela2023solarenergyconversion pages 2-4, shevela2023solarenergyconversion pages 1-2)
- **Environmental limitation framing for deployment**: Biotechnology-focused review analysis stresses that environmental factors (light quality/intensity, UV, nutrients, temperature, salinity) are the dominant operational constraints and must be engineered around for real-world cyanobacterial applications. (grettenberger2024limitingfactorsin pages 1-2, grettenberger2024limitingfactorsin pages 8-9)
- **CCM as essential augmentation to oxygenic photosynthesis in air**: Cyanobacterial oxygenic photosynthesis is closely tied to CCM operation under ambient CO2; multiple Ci uptake systems and carboxysomes are portrayed as key to maintaining high Rubisco carboxylation efficiency in oxygen-rich conditions. (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 3-3)

## 5) Relevant statistics and data (recently summarized)
- **Light-to-biomass conversion efficiency** in cyanobacteria is reported as **<10%** (in a 2024 cyanobacteria-focused review citing foundational work). (grettenberger2024limitingfactorsin pages 1-2)
- **PSII repair burden**: new D1 proteins are synthesized approximately **every 30–60 minutes**, reflecting rapid turnover under photostress/photoinhibition conditions. (grettenberger2024limitingfactorsin pages 5-7)
- **UV fractions of surface irradiance**: UV-B (280–315 nm) is reported as **<1%** and UV-A (315–400 nm) as **<7%** of surface irradiance in the cited synthesis, yet both can cause significant photodamage at high exposure. (grettenberger2024limitingfactorsin pages 5-7)
- **Iron/metal demand**: cellular iron demand in cyanobacteria is described as **~10× higher** than in non-phototrophs; the linear electron transport chain requires **~20 iron atoms**, and PSI contains **three [Fe4S4] clusters**—making Fe supply a major determinant of photosynthetic capacity. (grettenberger2024limitingfactorsin pages 7-8)
- **CCM transporter requirement**: Na+-bicarbonate symporters **SbtA and BicA require ~1 mM Na+**, indicating an ionic dependency that can be modeled as an environmental constraint on Ci uptake. (kurkela2024inorganiccarbonsensing pages 2-3)

---

## Candidate nodes for `oxygenic_photosynthesis.yaml` (grouped)
### A. Trait / process nodes
- Oxygenic photosynthesis (METPO: traitmech:000034) (given)
- Light reactions of oxygenic photosynthesis (process; candidate GO mapping if needed)
- Linear electron transport (LET) (process) (shevela2023solarenergyconversion pages 2-4, grettenberger2024limitingfactorsin pages 1-2)
- Cyclic electron transport / cyclic electron flow (CET/CEF) (process) (grettenberger2024limitingfactorsin pages 4-5, shevela2023solarenergyconversion pages 2-4)
- Proton motive force (pmf = ΔpH + ΔΨ) (process/biophysical state) (milrad2024regulationofmicroalgal pages 1-3)
- Kok cycle / S-state cycle (process) (shevela2023solarenergyconversion pages 12-13, shevela2023solarenergyconversion pages 14-16)
- Calvin–Benson–Bassham cycle (CBB cycle) (process) (shevela2023solarenergyconversion pages 2-4, kurkela2024inorganiccarbonsensing pages 2-3)
- Carbon concentrating mechanism (CCM) (process) (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 3-3)
- Carboxysome biogenesis/assembly (process) (kurkela2024inorganiccarbonsensing pages 6-6)

### B. Molecular complex nodes
- Photosystem II (PSII) (GO:0030095 candidate) (shevela2023solarenergyconversion pages 2-4, shevela2023solarenergyconversion pages 1-2)
- Oxygen-evolving complex / water-oxidizing complex (OEC/WOC; Mn4CaOx / Mn4CaO5) (candidate CHEBI/GO complex mapping) (shevela2023solarenergyconversion pages 9-10, vinyard2024bicarbonateisa pages 1-3)
- Photosystem I (PSI) (GO:0009522 candidate) (grettenberger2024limitingfactorsin pages 2-4, grettenberger2024limitingfactorsin pages 1-2)
- Cytochrome b6f complex (GO:0009512 candidate) (milrad2024regulationofmicroalgal pages 1-3, grettenberger2024limitingfactorsin pages 1-2)
- ATP synthase (thylakoid) (GO:0009535 candidate) (kurkela2024inorganiccarbonsensing pages 3-3, shevela2023solarenergyconversion pages 2-4)
- NDH-1 complexes (NDH-1₃ / NDH-13; NDH-1₄ / NDH-14) with CupA/CupB (kurkela2024inorganiccarbonsensing pages 3-3, kurkela2024inorganiccarbonsensing pages 1-2)
- Phycobilisome (PBS) light-harvesting antenna (GO:0030089 candidate) (grettenberger2024limitingfactorsin pages 1-2)
- Carboxysome (Bacterial microcompartment) (GO:0031470 candidate) (kurkela2024inorganiccarbonsensing pages 3-3, trettel2024modelingbacterialmicrocompartment pages 1-2)

### C. Genes/proteins (examples; map to UniProt/KEGG/NCBI Gene during curation)
- **psbA (D1 protein)**; D2 (psbD; not explicitly cited by gene symbol here, but D2 subunit referenced) (shevela2023solarenergyconversion pages 4-5, vinyard2024bicarbonateisa pages 1-3)
- **TyrZ/YZ** (D1 redox-active tyrosine) (shevela2023solarenergyconversion pages 9-10, shevela2023solarenergyconversion pages 12-13)
- **FNR** (ferredoxin–NADP+ reductase) (grettenberger2024limitingfactorsin pages 2-4)
- **Transporters**: SbtA, BicA, BCT1 (cmp operon) (kurkela2024inorganiccarbonsensing pages 2-3)
- **Regulator**: SbtB (PII-type regulator of SbtA) (kurkela2024inorganiccarbonsensing pages 3-3)
- **CupA/CupB, EcaB** (NDH-linked CO2 hydration module regulation) (kurkela2024inorganiccarbonsensing pages 3-3)
- **Carboxysome assembly**: CcmM, CcmN, CcmK, CcmL (kurkela2024inorganiccarbonsensing pages 6-6, kurkela2024inorganiccarbonsensing pages 5-6)

### D. Metabolites / ions / cofactors
- H2O, O2 (trait defining outputs) (vinyard2024bicarbonateisa pages 1-3)
- CO2, HCO3− (Ci pool) (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 3-3)
- PQ/PQH2 (plastoquinone/plastoquinol) (shevela2023solarenergyconversion pages 2-4, milrad2024regulationofmicroalgal pages 1-3)
- Plastocyanin (Pc) and/or cytochrome c6 (Cyt c6) (milrad2024regulationofmicroalgal pages 1-3)
- Ferredoxin; NADP+ / NADPH (grettenberger2024limitingfactorsin pages 2-4)
- Protons (H+) in lumen and cytoplasm/stroma; ΔpH component of pmf (vinyard2024bicarbonateisa pages 1-3, milrad2024regulationofmicroalgal pages 1-3)
- Na+ (required for SbtA/BicA activity) (kurkela2024inorganiccarbonsensing pages 2-3)
- Fe/Mn/Cu (nutrient-metal constraints) (grettenberger2024limitingfactorsin pages 7-8)

### E. Environmental / experimental factors (candidate ENVO terms)
- Light intensity; light wavelength/spectrum; UV-A/UV-B exposure (grettenberger2024limitingfactorsin pages 1-2, grettenberger2024limitingfactorsin pages 5-7)
- Ambient vs high CO2 conditions (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 6-6)
- Alkaline pH (growth phenotype interactions with transporter KO) (kurkela2024inorganiccarbonsensing pages 2-3)
- Metal availability: Fe, Mn, Cu (grettenberger2024limitingfactorsin pages 7-8, milrad2024regulationofmicroalgal pages 1-3)
- Salinity, temperature (biotech constraints) (grettenberger2024limitingfactorsin pages 8-9)

---

## Evidence-backed candidate causal edges (curation table)
The following table is intended to be directly actionable for TraitMech causal-graph curation.

| Edge (subject–predicate–object) | Evidence snippet | Reference | DOI | URL | Notes |
|---|---|---|---|---|---|
| Photosystem II (PSII) — oxidizes — H2O | “PSII is the primary catalyst of water oxidation in oxygenic photosynthesis” (shevela2023solarenergyconversion pages 2-4) | Shevela et al., 2023, *Solar energy conversion by photosystem II: principles and structures*, Photosynthesis Research | 10.1007/s11120-022-00991-y | https://doi.org/10.1007/s11120-022-00991-y | Strong, core defining edge for trait. |
| PSII — produces — O2 | “PSII uses light energy to oxidize water and to reduce plastoquinone… O2 is produced as a byproduct” (vinyard2024bicarbonateisa pages 1-3) | Vinyard & Govindjee, 2024, *Bicarbonate is a key regulator but not a substrate for O2 evolution in Photosystem II*, Photosynthesis Research | 10.1007/s11120-024-01111-8 | https://doi.org/10.1007/s11120-024-01111-8 | Strong; explicitly supports oxygen evolution. |
| Mn4CaO5 oxygen-evolving complex (OEC) — is catalytic site for — water oxidation | “the Mn4CaO5 cluster… catalytic site” and “PSII performs water oxidation at the Oxygen Evolving Complex (OEC/WOC)” (shevela2023solarenergyconversion pages 9-10) | Shevela et al., 2023, *Solar energy conversion by photosystem II: principles and structures*, Photosynthesis Research | 10.1007/s11120-022-00991-y | https://doi.org/10.1007/s11120-022-00991-y | Strong; node should be grounded as OEC / Mn4CaO5 cluster. |
| D1 protein (psbA product) — harbors ligands/cofactors required for — water oxidation | “D1 and D2 proteins… harbor all the redox cofactors… including water oxidation” (shevela2023solarenergyconversion pages 4-5) | Shevela et al., 2023, *Solar energy conversion by photosystem II: principles and structures*, Photosynthesis Research | 10.1007/s11120-022-00991-y | https://doi.org/10.1007/s11120-022-00991-y | Strong at complex level; exact residue-level mapping may need finer curation. |
| Redox-active TyrZ/YZ (D1) — transfers electrons from — Mn4CaO5 OEC | “YZ (TyrZ) is identified as the redox-active tyrosine that transfers electrons from the Mn4CaO5 catalytic site to P680” (shevela2023solarenergyconversion pages 9-10) | Shevela et al., 2023, *Solar energy conversion by photosystem II: principles and structures*, Photosynthesis Research | 10.1007/s11120-022-00991-y | https://doi.org/10.1007/s11120-022-00991-y | Strong mechanistic edge within PSII donor side. |
| Kok S-state cycle — accumulates four oxidizing equivalents before — O2 formation | “accumulates four oxidizing equivalents over four charge separations… before O2 is produced” (shevela2023solarenergyconversion pages 12-13) | Shevela et al., 2023, *Solar energy conversion by photosystem II: principles and structures*, Photosynthesis Research | 10.1007/s11120-022-00991-y | https://doi.org/10.1007/s11120-022-00991-y | Strong; useful process-level node. |
| OEC water oxidation — releases protons to — thylakoid lumen | “Protons removed from water are released into the thylakoid lumen” (vinyard2024bicarbonateisa pages 1-3) | Vinyard & Govindjee, 2024, *Bicarbonate is a key regulator but not a substrate for O2 evolution in Photosystem II*, Photosynthesis Research | 10.1007/s11120-024-01111-8 | https://doi.org/10.1007/s11120-024-01111-8 | Strong; links donor chemistry to pmf generation. |
| PSII — reduces — plastoquinone (PQ) to plastoquinol (PQH2) | “water oxidation… producing O2 and extracting electrons that reduce plastoquinone (PQ → PQH2)” (shevela2023solarenergyconversion pages 2-4) | Shevela et al., 2023, *Solar energy conversion by photosystem II: principles and structures*, Photosynthesis Research | 10.1007/s11120-022-00991-y | https://doi.org/10.1007/s11120-022-00991-y | Strong; core ETC edge. |
| Plastoquinol (PQH2) — donates electrons to — cytochrome b6f complex | “PQH2 diffuses to reduce the cytochrome b6f complex (Cytb6f)” (milrad2024regulationofmicroalgal pages 1-3) | Milrad et al., 2024, *Regulation of Microalgal Photosynthetic Electron Transfer*, Plants | 10.3390/plants13152103 | https://doi.org/10.3390/plants13152103 | Strong, but review includes microalgae broadly; still canonical for oxygenic phototrophs. |
| Cytochrome b6f complex — transfers electrons to PSI via — plastocyanin or cytochrome c6 | “Electrons are then transferred from Cytb6f to PSI via soluble carriers plastocyanin (Pc) or cytochrome c6 (Cytc6)” (milrad2024regulationofmicroalgal pages 1-3) | Milrad et al., 2024, *Regulation of Microalgal Photosynthetic Electron Transfer*, Plants | 10.3390/plants13152103 | https://doi.org/10.3390/plants13152103 | Strong; cyanobacteria often use plastocyanin or cytochrome c6 depending on metals. |
| Photosystem I (PSI) — reduces — ferredoxin | “PSI… oxidizes plastocyanin and reduces ferredoxin” (grettenberger2024limitingfactorsin pages 2-4) | Grettenberger et al., 2024, *Limiting factors in the operation of photosystems I and II in cyanobacteria*, Microbial Biotechnology | 10.1111/1751-7915.14519 | https://doi.org/10.1111/1751-7915.14519 | Strong. |
| Ferredoxin-NADP+ reductase (FNR) — reduces — NADP+ to NADPH | “electrons via ferredoxin and Fd–NAD(P)H oxidoreductase (FNR) reduce NADP+ to NADPH” (grettenberger2024limitingfactorsin pages 2-4) | Grettenberger et al., 2024, *Limiting factors in the operation of photosystems I and II in cyanobacteria*, Microbial Biotechnology | 10.1111/1751-7915.14519 | https://doi.org/10.1111/1751-7915.14519 | Strong. |
| Linear electron transport — generates — proton motive force (pmf) | “The membrane proton motive force (pmf) produced by these transfers comprises ∆pH… and ∆Ψ” (milrad2024regulationofmicroalgal pages 1-3) | Milrad et al., 2024, *Regulation of Microalgal Photosynthetic Electron Transfer*, Plants | 10.3390/plants13152103 | https://doi.org/10.3390/plants13152103 | Strong process-level edge. |
| Proton motive force — drives — ATP synthesis | “thereby raising proton motive force (pmf) and ATP synthesis by ATP synthase” (shevela2023solarenergyconversion pages 2-4) | Shevela et al., 2023, *Solar energy conversion by photosystem II: principles and structures*, Photosynthesis Research | 10.1007/s11120-022-00991-y | https://doi.org/10.1007/s11120-022-00991-y | Strong. |
| Cyclic electron transport (CET) around PSI — returns electrons to — PQ pool | “Cyclic electron flow (CEF) recycles electrons from the PSI …” / “CET around PSI mediated by NDH-1 donating electrons back to the PQ pool” (grettenberger2024limitingfactorsin pages 4-5) | Grettenberger et al., 2024, *Limiting factors in the operation of photosystems I and II in cyanobacteria*, Microbial Biotechnology | 10.1111/1751-7915.14519 | https://doi.org/10.1111/1751-7915.14519 | Strong; nomenclature CET/CEF varies by source. |
| CET around PSI — increases — proton gradient / ATP synthesis | “CET and linear electron flow together generate a proton gradient across the thylakoid membrane for ATP synthesis” (grettenberger2024limitingfactorsin pages 4-5) | Grettenberger et al., 2024, *Limiting factors in the operation of photosystems I and II in cyanobacteria*, Microbial Biotechnology | 10.1111/1751-7915.14519 | https://doi.org/10.1111/1751-7915.14519 | Strong. |
| Bicarbonate — regulates but is not substrate for — O2 evolution in PSII | “bicarbonate functions as a regulator… but is not a substrate of O2 evolution” (vinyard2024bicarbonateisa pages 1-3) | Vinyard & Govindjee, 2024, *Bicarbonate is a key regulator but not a substrate for O2 evolution in Photosystem II*, Photosynthesis Research | 10.1007/s11120-024-01111-8 | https://doi.org/10.1007/s11120-024-01111-8 | Strong negative/boundary-case edge; important warning against miscoding substrate. |
| Bicarbonate — ligates/regulates — non-heme iron on PSII acceptor side | “bicarbonate functions as a regulator (acting on the acceptor side by ligating the NHI)” (vinyard2024bicarbonateisa pages 1-3) | Vinyard & Govindjee, 2024, *Bicarbonate is a key regulator but not a substrate for O2 evolution in Photosystem II*, Photosynthesis Research | 10.1007/s11120-024-01111-8 | https://doi.org/10.1007/s11120-024-01111-8 | Strong; should be modeled as regulatory not substrate role. |
| SbtA — imports — HCO3− | “Bicarbonate uptake is mediated by Na+/HCO3- symporters SbtA and BicA” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Strong; cyanobacteria-specific CCM edge. |
| BicA — imports — HCO3− | “BicA is described as a high-flux, low-affinity sodium–bicarbonate symporter” (kurkela2024inorganiccarbonsensing pages 5-6) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Strong; useful to note transporter properties in node metadata. |
| BCT1 transporter — pumps — HCO3− using ATP | “High-affinity uptake is provided by the ABC-type BCT1 HCO3- pump” and “BCT1 is ATP-fuelled” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Strong. |
| SbtB — regulates — SbtA activity | “SbtA activity is regulated by the PII-type protein SbtB” (kurkela2024inorganiccarbonsensing pages 3-3) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Strong regulatory edge. |
| NDH-13/CupA and NDH-14/CupB — convert — CO2 to HCO3− in cytoplasm | “specialized NDH complexes… ‘convert CO2 to HCO3- in the cytoplasm’” (kurkela2024inorganiccarbonsensing pages 1-2) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Strong; central CCM edge. |
| EcaB — regulates — CupA/CupB-mediated CO2-to-HCO3− conversion | “EcaB… interacts with CupA/CupB and regulates this conversion” (kurkela2024inorganiccarbonsensing pages 3-3) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Moderate; mechanistic direction supported in review but may merit primary-source confirmation before strict curation. |
| Carboxysome shell — encapsulates — Rubisco and carbonic anhydrase | “carboxysomes are protein shells containing RuBisCo and carbonic anhydrase” (kurkela2024inorganiccarbonsensing pages 1-2) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Strong. |
| Carboxysomal carbonic anhydrase — converts — HCO3− to CO2 | “Cytoplasmic HCO3 diffuses into carboxysomes where carbonic anhydrase converts it to CO2” (kurkela2024inorganiccarbonsensing pages 3-3) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Strong. |
| Carboxysome — increases local CO2 around — Rubisco | “carboxysomes… increase CO2 concentration and reduce O2 near the RuBisCo active site” (kurkela2024inorganiccarbonsensing pages 1-2) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Strong; trait-adjacent because supports CO2 fixation efficiency rather than defining oxygenic photosynthesis itself. |
| Rubisco — fixes — CO2 in Calvin-Benson-Bassham cycle | “inside the carboxysome Rubisco catalyses the first step of the Calvin–Benson–Bassham cycle” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Strong; downstream of light reactions. |
| Na+ — is required for activity of — SbtA and BicA | “they require ~1 mM Na+” (kurkela2024inorganiccarbonsensing pages 2-3) | Kurkela & Tyystjärvi, 2024, *Inorganic carbon sensing and signalling in cyanobacteria*, Physiologia Plantarum | 10.1111/ppl.14140 | https://doi.org/10.1111/ppl.14140 | Strong environmental dependency; cyanobacterial CCM-specific. |
| Copper vs iron availability — determines use of — plastocyanin vs cytochrome c6 | “expression of these carriers depends on environmental metal availability (copper vs iron)” (milrad2024regulationofmicroalgal pages 1-3) | Milrad et al., 2024, *Regulation of Microalgal Photosynthetic Electron Transfer*, Plants | 10.3390/plants13152103 | https://doi.org/10.3390/plants13152103 | Moderate; broad oxygenic phototroph context, but mechanistically useful. |
| Iron limitation — decreases — light-dependent electron transfer and photosynthetic activity | “Iron… limitation… decreasing light-dependent electron transfer and photosynthetic activity” (grettenberger2024limitingfactorsin pages 7-8) | Grettenberger et al., 2024, *Limiting factors in the operation of photosystems I and II in cyanobacteria*, Microbial Biotechnology | 10.1111/1751-7915.14519 | https://doi.org/10.1111/1751-7915.14519 | Strong environmental edge. |
| Light intensity/wavelength — remodels — phycobilisomes / PSI:PSII ratio / photosystem transcription | “light intensity and wavelength drive remodeling… change PSI:PSII ratios, modulate transcription of PSI/PSII/PBS” (grettenberger2024limitingfactorsin pages 4-5) | Grettenberger et al., 2024, *Limiting factors in the operation of photosystems I and II in cyanobacteria*, Microbial Biotechnology | 10.1111/1751-7915.14519 | https://doi.org/10.1111/1751-7915.14519 | Strong environmental regulation; phenotype plasticity rather than core trait definition. |
| UV light — damages — phycobilisomes, pigments, PSII, and DNA | “UV light breaks phycobilisomes, bleaches pigments, and damages PSII” (grettenberger2024limitingfactorsin pages 1-2) | Grettenberger et al., 2024, *Limiting factors in the operation of photosystems I and II in cyanobacteria*, Microbial Biotechnology | 10.1111/1751-7915.14519 | https://doi.org/10.1111/1751-7915.14519 | Strong stress edge; DNA damage also noted in source. |


*Table: This table compiles candidate subject–predicate–object edges for a TraitMech causal graph of oxygenic photosynthesis, spanning PSII water splitting, electron transport, carbon concentrating mechanisms, and environmental regulation. Each edge is paired with a short evidence snippet, source citation, DOI/URL, and curation notes on strength or scope.*

### Visual evidence (CCM module)
A recent CCM schematic is available and can be cited for component localization and flow (outer membrane entry, bicarbonate transporters, NDH-1₃/₄ CupA/B conversion, and carboxysome CA/Rubisco). (kurkela2024inorganiccarbonsensing media 0717bd5a)

---

## Warnings / claims to treat cautiously before curation
1. **Do not model bicarbonate as an O-atom substrate** for oxygen evolution; recent expert synthesis explicitly rejects this and frames bicarbonate as regulatory. (vinyard2024bicarbonateisa pages 1-3)
2. **Taxon-/condition-specific acclimation programs** (e.g., wavelength-dependent remodeling programs referenced as FaRLiP/LoLiP) should be captured as *regulatory/context nodes* rather than definitional edges of oxygenic photosynthesis, unless TraitMech intends conditional subtraits. (grettenberger2024limitingfactorsin pages 4-5)
3. **Quantitative claims like “carboxysomes concentrate CO2 >1000×”** appear in a 2024 modeling review; this may be suitable as a contextual assertion but should be cross-checked against primary experimental sources before hard-coding as a mechanistic parameter in TraitMech. (trettel2024modelingbacterialmicrocompartment pages 2-3)
4. **Mechanistic details from theory-focused work** (e.g., specific O–O bond formation pathway proposals) should be labeled *uncertain* unless supported by convergent experimental data. (yamaguchi2024theoreticalelucidationof pages 1-2)

---

## DOI-first bibliography (recent prioritized; with publication dates and URLs)
- Shevela D, Kern J, Govindjee, Messinger J. **Solar energy conversion by photosystem II: principles and structures**. *Photosynthesis Research*. **Feb 2023**. DOI: **10.1007/s11120-022-00991-y**. https://doi.org/10.1007/s11120-022-00991-y (shevela2023solarenergyconversion pages 2-4, shevela2023solarenergyconversion pages 1-2)
- Kurkela J, Tyystjärvi T. **Inorganic carbon sensing and signalling in cyanobacteria**. *Physiologia Plantarum*. **Jan 2024**. DOI: **10.1111/ppl.14140**. https://doi.org/10.1111/ppl.14140 (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 3-3, kurkela2024inorganiccarbonsensing pages 2-3)
- Vinyard DJ, Govindjee. **Bicarbonate is a key regulator but not a substrate for O2 evolution in Photosystem II**. *Photosynthesis Research*. **Jul 2024**. DOI: **10.1007/s11120-024-01111-8**. https://doi.org/10.1007/s11120-024-01111-8 (vinyard2024bicarbonateisa pages 1-3, vinyard2024bicarbonateisa pages 3-4)
- Grettenberger CL, Abou‐Shanab R, Hamilton TL. **Limiting factors in the operation of photosystems I and II in cyanobacteria**. *Microbial Biotechnology*. **Aug 2024**. DOI: **10.1111/1751-7915.14519**. https://doi.org/10.1111/1751-7915.14519 (grettenberger2024limitingfactorsin pages 1-2, grettenberger2024limitingfactorsin pages 5-7, grettenberger2024limitingfactorsin pages 7-8)
- Milrad Y, Mosebach L, Buchert F. **Regulation of Microalgal Photosynthetic Electron Transfer**. *Plants*. **Jul 2024**. DOI: **10.3390/plants13152103**. https://doi.org/10.3390/plants13152103 (milrad2024regulationofmicroalgal pages 1-3)
- Trettel DS, Pacheco SL, Laskie AK, et al. **Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation**. *Frontiers in Plant Science*. **Feb 2024**. DOI: **10.3389/fpls.2024.1346759**. https://doi.org/10.3389/fpls.2024.1346759 (trettel2024modelingbacterialmicrocompartment pages 2-3, trettel2024modelingbacterialmicrocompartment pages 1-2)
- Yamaguchi K, Miyagawa K, Shoji M, et al. **Theoretical elucidation… CaMn4Ox clusters… whole Kok cycle… O–O bond formation**. *Photosynthesis Research*. **Nov 2024**. DOI: **10.1007/s11120-023-01053-7**. https://doi.org/10.1007/s11120-023-01053-7 (yamaguchi2024theoreticalelucidationof pages 1-2)
- Kossalbayev BD, Yilmaz G, Ozcan HG, et al. **Photosynthesis and hydrogen energy for sustainability: harnessing the sun for a greener future**. *Photosynthetica*. **Jun 2024**. DOI: **10.32615/ps.2024.013**. https://doi.org/10.32615/ps.2024.013 (kossalbayev2024photosynthesisandhydrogen pages 2-3)


References

1. (shevela2023solarenergyconversion pages 1-2): D. Shevela, J. Kern, Govindjee Govindjee, and J. Messinger. Solar energy conversion by photosystem ii: principles and structures. Photosynthesis Research, 156:279-307, Feb 2023. URL: https://doi.org/10.1007/s11120-022-00991-y, doi:10.1007/s11120-022-00991-y. This article has 187 citations and is from a peer-reviewed journal.

2. (shevela2023solarenergyconversion pages 2-4): D. Shevela, J. Kern, Govindjee Govindjee, and J. Messinger. Solar energy conversion by photosystem ii: principles and structures. Photosynthesis Research, 156:279-307, Feb 2023. URL: https://doi.org/10.1007/s11120-022-00991-y, doi:10.1007/s11120-022-00991-y. This article has 187 citations and is from a peer-reviewed journal.

3. (vinyard2024bicarbonateisa pages 1-3): David J. Vinyard and Govindjee Govindjee. Bicarbonate is a key regulator but not a substrate for o2 evolution in photosystem ii. Photosynthesis Research, 162:93-99, Jul 2024. URL: https://doi.org/10.1007/s11120-024-01111-8, doi:10.1007/s11120-024-01111-8. This article has 14 citations and is from a peer-reviewed journal.

4. (grettenberger2024limitingfactorsin pages 2-4): Christen L. Grettenberger, Reda Abou‐Shanab, and Trinity L. Hamilton. Limiting factors in the operation of photosystems i and ii in cyanobacteria. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14519, doi:10.1111/1751-7915.14519. This article has 14 citations and is from a peer-reviewed journal.

5. (shevela2023solarenergyconversion pages 4-5): D. Shevela, J. Kern, Govindjee Govindjee, and J. Messinger. Solar energy conversion by photosystem ii: principles and structures. Photosynthesis Research, 156:279-307, Feb 2023. URL: https://doi.org/10.1007/s11120-022-00991-y, doi:10.1007/s11120-022-00991-y. This article has 187 citations and is from a peer-reviewed journal.

6. (vinyard2024bicarbonateisa pages 3-4): David J. Vinyard and Govindjee Govindjee. Bicarbonate is a key regulator but not a substrate for o2 evolution in photosystem ii. Photosynthesis Research, 162:93-99, Jul 2024. URL: https://doi.org/10.1007/s11120-024-01111-8, doi:10.1007/s11120-024-01111-8. This article has 14 citations and is from a peer-reviewed journal.

7. (shevela2023solarenergyconversion pages 9-10): D. Shevela, J. Kern, Govindjee Govindjee, and J. Messinger. Solar energy conversion by photosystem ii: principles and structures. Photosynthesis Research, 156:279-307, Feb 2023. URL: https://doi.org/10.1007/s11120-022-00991-y, doi:10.1007/s11120-022-00991-y. This article has 187 citations and is from a peer-reviewed journal.

8. (grettenberger2024limitingfactorsin pages 1-2): Christen L. Grettenberger, Reda Abou‐Shanab, and Trinity L. Hamilton. Limiting factors in the operation of photosystems i and ii in cyanobacteria. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14519, doi:10.1111/1751-7915.14519. This article has 14 citations and is from a peer-reviewed journal.

9. (milrad2024regulationofmicroalgal pages 1-3): Yuval Milrad, Laura Mosebach, and Felix Buchert. Regulation of microalgal photosynthetic electron transfer. Plants, 13:2103, Jul 2024. URL: https://doi.org/10.3390/plants13152103, doi:10.3390/plants13152103. This article has 12 citations.

10. (shevela2023solarenergyconversion pages 12-13): D. Shevela, J. Kern, Govindjee Govindjee, and J. Messinger. Solar energy conversion by photosystem ii: principles and structures. Photosynthesis Research, 156:279-307, Feb 2023. URL: https://doi.org/10.1007/s11120-022-00991-y, doi:10.1007/s11120-022-00991-y. This article has 187 citations and is from a peer-reviewed journal.

11. (shevela2023solarenergyconversion pages 14-16): D. Shevela, J. Kern, Govindjee Govindjee, and J. Messinger. Solar energy conversion by photosystem ii: principles and structures. Photosynthesis Research, 156:279-307, Feb 2023. URL: https://doi.org/10.1007/s11120-022-00991-y, doi:10.1007/s11120-022-00991-y. This article has 187 citations and is from a peer-reviewed journal.

12. (grettenberger2024limitingfactorsin pages 4-5): Christen L. Grettenberger, Reda Abou‐Shanab, and Trinity L. Hamilton. Limiting factors in the operation of photosystems i and ii in cyanobacteria. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14519, doi:10.1111/1751-7915.14519. This article has 14 citations and is from a peer-reviewed journal.

13. (yamaguchi2024theoreticalelucidationof pages 1-2): Kizashi Yamaguchi, Koichi Miyagawa, Mitsuo Shoji, Takashi Kawakami, Hiroshi Isobe, Shusuke Yamanaka, and Takahito Nakajima. Theoretical elucidation of the structure, bonding, and reactivity of the camn4ox clusters in the whole kok cycle for water oxidation embedded in the oxygen evolving center of photosystem ii. new molecular and quantum insights into the mechanism of the o–o bond formation. Photosynthesis Research, 162:291-330, Nov 2024. URL: https://doi.org/10.1007/s11120-023-01053-7, doi:10.1007/s11120-023-01053-7. This article has 7 citations and is from a peer-reviewed journal.

14. (kurkela2024inorganiccarbonsensing pages 3-3): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.

15. (kurkela2024inorganiccarbonsensing pages 2-3): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.

16. (kurkela2024inorganiccarbonsensing pages 1-2): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.

17. (trettel2024modelingbacterialmicrocompartment pages 1-2): Daniel S. Trettel, Sara L. Pacheco, Asa K. Laskie, Raul Gonzalez-Esquer, Jianping Yu, Harvey J. M. Hou, and Denis Jallet. Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1346759, doi:10.3389/fpls.2024.1346759. This article has 8 citations.

18. (trettel2024modelingbacterialmicrocompartment pages 2-3): Daniel S. Trettel, Sara L. Pacheco, Asa K. Laskie, Raul Gonzalez-Esquer, Jianping Yu, Harvey J. M. Hou, and Denis Jallet. Modeling bacterial microcompartment architectures for enhanced cyanobacterial carbon fixation. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1346759, doi:10.3389/fpls.2024.1346759. This article has 8 citations.

19. (grettenberger2024limitingfactorsin pages 8-9): Christen L. Grettenberger, Reda Abou‐Shanab, and Trinity L. Hamilton. Limiting factors in the operation of photosystems i and ii in cyanobacteria. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14519, doi:10.1111/1751-7915.14519. This article has 14 citations and is from a peer-reviewed journal.

20. (grettenberger2024limitingfactorsin pages 5-7): Christen L. Grettenberger, Reda Abou‐Shanab, and Trinity L. Hamilton. Limiting factors in the operation of photosystems i and ii in cyanobacteria. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14519, doi:10.1111/1751-7915.14519. This article has 14 citations and is from a peer-reviewed journal.

21. (grettenberger2024limitingfactorsin pages 7-8): Christen L. Grettenberger, Reda Abou‐Shanab, and Trinity L. Hamilton. Limiting factors in the operation of photosystems i and ii in cyanobacteria. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14519, doi:10.1111/1751-7915.14519. This article has 14 citations and is from a peer-reviewed journal.

22. (kossalbayev2024photosynthesisandhydrogen pages 2-3): B. D. Kossalbayev, G. Yilmaz, H. G. Ozcan, G. Soykan, S. Yalcin, and S. I. Allakhverdiev. Photosynthesis and hydrogen energy for sustainability: harnessing the sun for a greener future. Photosynthetica, 62:138-146, Jun 2024. URL: https://doi.org/10.32615/ps.2024.013, doi:10.32615/ps.2024.013. This article has 8 citations and is from a peer-reviewed journal.

23. (kurkela2024inorganiccarbonsensing pages 6-6): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.

24. (kurkela2024inorganiccarbonsensing pages 5-6): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.

25. (kurkela2024inorganiccarbonsensing media 0717bd5a): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 15 citations and is from a peer-reviewed journal.