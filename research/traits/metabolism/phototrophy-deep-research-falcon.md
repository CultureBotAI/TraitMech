---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:30:19.119918'
end_time: '2026-06-18T05:55:01.507373'
duration_seconds: 1482.39
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: phototrophy
  trait_identifier: traitmech:000037
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: phototrophy
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which an organism captures light as its energy source.
    It encompasses chlorophyll-based photosynthesis (with photochemical reaction centers)
    and retinal-based (rhodopsin) light-driven ion pumping.
  parent_traits: METPO:1000060
  synonyms: phototrophic metabolism
  evidence_summary: "DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, \"Prokaryotic\
    \ photosynthesis and phototrophy illuminated\", frames phototrophy as the broad\
    \ use of light for energy, spanning chlorophyll- and rhodopsin-based mechanisms;\
    \ parent of the photosynthesis and proteorhodopsin phototrophy sub-variants.)\
    \ | DOI:10.1126/science.289.5486.1902:  (B\xE9j\xE0 et al. established retinal-based\
    \ proteorhodopsin phototrophy as a light-energy capture mechanism distinct from\
    \ chlorophyll-based photosynthesis.)"
  causal_graph_summary: 'phototrophy_light_energy_capture: 3 nodes, 2 edges'
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
- **Trait label:** phototrophy
- **METPO identifier:** traitmech:000037
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism captures light as its energy source. It encompasses chlorophyll-based photosynthesis (with photochemical reaction centers) and retinal-based (rhodopsin) light-driven ion pumping.
- **Parent traits:** METPO:1000060
- **Synonyms:** phototrophic metabolism
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", frames phototrophy as the broad use of light for energy, spanning chlorophyll- and rhodopsin-based mechanisms; parent of the photosynthesis and proteorhodopsin phototrophy sub-variants.) | DOI:10.1126/science.289.5486.1902:  (Béjà et al. established retinal-based proteorhodopsin phototrophy as a light-energy capture mechanism distinct from chlorophyll-based photosynthesis.)
- **Existing causal graph summary:** phototrophy_light_energy_capture: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **phototrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/phototrophy.yaml`.

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
- **Trait label:** phototrophy
- **METPO identifier:** traitmech:000037
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism captures light as its energy source. It encompasses chlorophyll-based photosynthesis (with photochemical reaction centers) and retinal-based (rhodopsin) light-driven ion pumping.
- **Parent traits:** METPO:1000060
- **Synonyms:** phototrophic metabolism
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", frames phototrophy as the broad use of light for energy, spanning chlorophyll- and rhodopsin-based mechanisms; parent of the photosynthesis and proteorhodopsin phototrophy sub-variants.) | DOI:10.1126/science.289.5486.1902:  (Béjà et al. established retinal-based proteorhodopsin phototrophy as a light-energy capture mechanism distinct from chlorophyll-based photosynthesis.)
- **Existing causal graph summary:** phototrophy_light_energy_capture: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **phototrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/phototrophy.yaml`.

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


## Microbial Trait Causal Graph Research Report: **Phototrophy** (traitmech:000037)

### Executive scope summary (TraitMech curation-ready)
**Phototrophy** is best curated as the *capacity to capture light energy and convert it into biologically usable energy* (typically as a proton motive force and/or ATP), spanning two mechanistic classes: **(i) chlorophyll/(bacterio)chlorophyll reaction-center phototrophy** and **(ii) retinal/rhodopsin-based phototrophy**. A key boundary is that **photosynthesis** (in the strict sense) is *light-driven redox chemistry that can support CO2 reduction*, whereas **rhodopsin phototrophy** often provides *photosystem-independent* energy conservation (e.g., ion pumping) without direct photochemical electron transfer; thus “all photosynthetic bacteria are phototrophic but not all phototrophic bacteria are photosynthetic” (bryant2006prokaryoticphotosynthesisand pages 2-3, bryant2006prokaryoticphotosynthesisand pages 1-2). This trait should therefore sit above narrower child traits such as oxygenic photosynthesis, anoxygenic photosynthesis, and proteorhodopsin phototrophy.

**Boundary cases to flag for curation:**
1. **Photoheterotrophs with reaction centers** (e.g., some RC-containing bacteria) remain phototrophic even if not fixing CO2 (bryant2006prokaryoticphotosynthesisand pages 2-3, bryant2006prokaryoticphotosynthesisand pages 1-2).
2. **Rhodopsin systems co-occurring with chlorophyll photosystems** (dual systems) should still map to phototrophy, but edges should be curated with explicit mechanism (photosystem vs rhodopsin) (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2).
3. **Engineered phototrophy** (synthetic photoelectrosynthesis; optogenetic bioenergetics) is useful for mechanistic support but should be curated as **application/implementation** rather than “native trait mechanism” unless explicitly observed in natural isolates (tu2023engineeringartificialphotosynthesis pages 2-3, tu2024engineeringbionanoreactorin pages 9-9).

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Definition of phototrophy vs photosynthesis
Foundational reviews distinguish **photosynthesis** as “the reduction of carbon dioxide into biomass using energy derived from light,” while **phototrophy** is broader: converting light to chemical energy for growth, not necessarily carbon fixation (bryant2006prokaryoticphotosynthesisand pages 1-2, bryant2006prokaryoticphotosynthesisand pages 2-3). This framing justifies TraitMech phototrophy (traitmech:000037) as a parent to multiple mechanistic subclasses.

### 1.2 Mechanistic subclasses under phototrophy
**A. Reaction-center/chlorophyll-based phototrophy**
- Uses photochemical **reaction centers** and photosystems to drive electron transfer, building a proton gradient and generating **ATP and reductant (e.g., NADPH)** for biosynthesis and potentially CO2 fixation (grettenberger2024limitingfactorsin pages 1-2).

**B. Retinal/rhodopsin-based phototrophy (“retinalophototrophy”)**
- Uses single-protein photoreceptors binding **retinal**; visible-light activation triggers a **photocycle** and ion transport (e.g., outward H+ pumping) that builds a proton gradient used to synthesize ATP (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2, li2024insitucommunity pages 13-15).

### 1.3 Dual phototrophic systems and spectral complementarity
Cyanobacteria can contain **chlorophyll-based photosystems plus rhodopsin ion pumps**, suggested to enable more efficient sunlight capture across complementary wavelength ranges (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2).

---

## 2) Candidate causal-graph nodes (entities) grouped by type (with grounding suggestions)

### 2.1 Environmental/exposure variables (candidate ENVO/PATO)
- Light exposure / visible light; **light intensity and wavelength** (grettenberger2024limitingfactorsin pages 1-2)
- **UV light** (photodamage driver) (grettenberger2024limitingfactorsin pages 1-2)
- **Salinity** (environmental modulator; correlated with non-Calvin carbon fixation activity in some taxa) (li2024insitucommunity pages 13-15)
- **Nutrient limitation** (modulates photosynthesis and mixotrophy; also context for rhodopsin benefits) (li2024insitucommunity pages 13-15, grettenberger2024limitingfactorsin pages 1-2)
- **pH** (critical for some rhodopsin clades) (okhrimenko2023mirrorproteorhodopsins pages 1-2)
- **Zn2+** as inhibitor for mirror proteorhodopsins (CHEBI:29105) (okhrimenko2023mirrorproteorhodopsins pages 1-2)

### 2.2 Core mechanistic complexes and processes (candidate GO)
**Chlorophyll-based phototrophy (oxygenic example in cyanobacteria):**
- Phycobilisome **GO:0030089** (antenna) (grettenberger2024limitingfactorsin pages 1-2)
- Photosystem II **GO:0009523**; Photosystem I **GO:0009522** (grettenberger2024limitingfactorsin pages 1-2)
- Cytochrome b6f complex **GO:0009512** (grettenberger2024limitingfactorsin pages 1-2)
- Electron carriers: plastocyanin/cytochrome c553 (label), ferredoxin (label) (grettenberger2024limitingfactorsin pages 1-2)
- Calvin–Benson–Bassham cycle (KEGG module label) and RuBisCO (enzyme node) (grettenberger2024limitingfactorsin pages 1-2)

**Rhodopsin-based phototrophy:**
- Microbial rhodopsin (opsin) + retinal chromophore (CHEBI:30526) (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2, li2024insitucommunity pages 13-15)
- Proton motive force / proton gradient (process node) (li2024insitucommunity pages 13-15)
- ATP synthase (complex node; label/EC:7.1.2.2) (bryant2006prokaryoticphotosynthesisand pages 2-3, tu2023engineeringartificialphotosynthesis pages 2-3)

**Rhodopsin antenna augmentation:**
- Hydroxylated carotenoids as antennas (e.g., **lutein**, CHEBI:17583) with absorption/excitation coupling evidence (chazan2023phototrophybyantennacontaining media 6d67b0c1)
- Canthaxanthin (CHEBI:23086) used as antenna/support in engineered rhodopsin phototrophy (tu2023engineeringartificialphotosynthesis pages 2-3, tu2024engineeringbionanoreactorin pages 9-9)

### 2.3 Chemicals/metabolites (candidate CHEBI)
- CO2 (CHEBI:16526); ATP (CHEBI:15422); NADPH (CHEBI:16474)
- Water (CHEBI:15377)
- Plastoquinone (CHEBI:16389)
- Retinal (CHEBI:30526)

### 2.4 Genes/proteins and engineered coupling modules (stable IDs often strain-specific; label nodes acceptable)
- **Proteorhodopsin / proton-pump rhodopsin (PPR)** (label) (li2024insitucommunity pages 13-15)
- Cyanorhodopsin-II clades (YCyR-II, GCyR-II) (label) (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2)
- Mirror proteorhodopsin SpaR (label) (okhrimenko2023mirrorproteorhodopsins pages 1-2)
- **MtrCAB** extracellular electron transfer conduit (label/UniProt grounding depends on strain) (tu2023engineeringartificialphotosynthesis pages 2-3)
- Flavins / riboflavin shuttle (CHEBI:17015 riboflavin) (tu2023engineeringartificialphotosynthesis pages 2-3, davison2022engineeringarhodopsinbased pages 1-2)

---

## 3) Recent developments and latest research (prioritizing 2023–2024)

### 3.1 Antenna-containing rhodopsin phototrophy (2023)
A key 2023 advance is experimental evidence that rhodopsin proton pumps can be **augmented by carotenoid antennas**, enabling energy transfer from antenna pigments to the retinal-based system. The supplementary spectral evidence for a rhodopsin–carotenoid complex (Kin4B8 + lutein) shows absorbance and fluorescence excitation consistent with antenna function (chazan2023phototrophybyantennacontaining media 6d67b0c1) (chazan2023phototrophybyantennacontaining pages 1-7).

### 3.2 Expanded diversity of cyanobacterial rhodopsins (2024)
Metagenome mining revealed a novel cyanobacteria-specific rhodopsin clade **Cyanorhodopsin-II**, functioning as **light-driven outward H+ pumps**, with subclades absorbing different wavelengths (yellow vs green), and structural/mutational support for spectral tuning near the retinal chromophore (DOI:10.1093/ismejo/wrae175; published Jan 2024) (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2).

### 3.3 Community transcriptomics linking proton-pump rhodopsins to carbon fixation potential (2024)
In situ plankton metatranscriptomics in the South China Sea identified **positive correlations between proton-pump rhodopsin expression and non-Calvin carbon fixation gene expression** in several bacterial orders, supporting the hypothesis that rhodopsin-derived energy can subsidize carbon fixation pathways in marine bacteria (DOI:10.1128/spectrum.02177-23; published Mar 2024) (li2024insitucommunity pages 13-15).

### 3.4 Environmental constraints and optimization targets in cyanobacterial photosystems (2024)
A 2024 review summarizes how cyanobacterial phototrophy is limited by **light intensity/wavelength, UV exposure, nutrient limitation, temperature, and salinity**, and provides a mechanistic overview of PSI/PSII electron flow and pigment absorption peaks relevant to modeling phototrophic performance and photodamage (DOI:10.1111/1751-7915.14519; published Aug 2024) (grettenberger2024limitingfactorsin pages 1-2).

### 3.5 pH- and metal-dependent rhodopsin phototrophy (2023)
Discovery/characterization of “mirror proteorhodopsins” expands the operating envelope of rhodopsin proton pumps: SpaR functions as a light-driven proton pump at **acidic pH (<6.5)**, and **Zn2+ inhibits** outward proton pumping at millimolar concentrations (DOI:10.1038/s42004-023-00884-8; published May 2023) (okhrimenko2023mirrorproteorhodopsins pages 1-2).

---

## 4) Current applications and real-world implementations

### 4.1 Cyanobacteria as biotechnological chassis (applications and constraints)
Cyanobacteria are positioned for carbon capture, bioplastics, biofertilizers, and other bioproducts, but photosynthetic conversion efficiency and environmental limitations constrain implementation; one quantitative benchmark cited is **light-to-biomass conversion efficiency <10%** in cyanobacteria (DOI:10.1111/1751-7915.14519; 2024) (grettenberger2024limitingfactorsin pages 1-2).

### 4.2 Engineered rhodopsin photoelectrosynthesis for CO2 fixation (2023)
A 2023 Nature Communications study engineered *Ralstonia eutropha* to integrate rhodopsin proton pumping with **MtrCAB-mediated extracellular electron uptake** and flavin mediation to generate reducing power (NADH/NADPH) and ATP, enabling **photoelectrosynthetic CO2 fixation** in a bio-hybrid system (DOI:10.1038/s41467-023-43524-4; published Dec 2023) (tu2023engineeringartificialphotosynthesis pages 2-3).

### 4.3 Bio-hybrid hydrogen production using light-driven rhodopsin proton pumping (2024)
A 2024 PNAS implementation engineered a periplasmic “bionanoreactor” in *Shewanella* integrating electron transfer (including MtrCAB and nanomaterials) and **Gloeobacter rhodopsin + canthaxanthin** to boost proton pumping; the reported **Faraday efficiency reached 80% for hydrogen production** (DOI:10.1073/pnas.2404958121; published Jul 2024) (tu2024engineeringbionanoreactorin pages 9-9).

---

## 5) Expert opinions and analysis (authoritative synthesis)

### 5.1 Why phototrophy should be curated as a parent trait
The Bryant & Frigaard synthesis argues for phototrophy as a broad category encompassing multiple “light-to-energy” strategies, including rhodopsin-based proton pumping and chlorophyll-based reaction-center systems, explicitly separating *energy capture* from *CO2 reduction* (bryant2006prokaryoticphotosynthesisand pages 2-3, bryant2006prokaryoticphotosynthesisand pages 1-2). This supports curating **phototrophy** (traitmech:000037) as a parent trait with mechanism-specific subtraits.

### 5.2 Mechanistic convergence: PMF as a shared causal hub
Across rhodopsin phototrophy (PPR pumping protons) and photosystem-based phototrophy (electron transport coupled proton gradient formation), the **proton gradient/PMF** emerges as a convergent intermediate driving ATP synthesis (li2024insitucommunity pages 13-15, grettenberger2024limitingfactorsin pages 1-2). A TraitMech causal graph can therefore reuse shared nodes (PMF → ATP synthesis) while preserving distinct upstream mechanisms.

### 5.3 Caution on ecological correlation vs causation
Field meta-omics correlations (e.g., rhodopsin expression correlating with non-Calvin carbon fixation genes; salinity correlating with NCF transcript contribution) are informative but should be curated as **uncertain/modulatory** edges unless supported by perturbation experiments (li2024insitucommunity pages 13-15).

---

## 6) Relevant statistics and quantitative data from recent studies

- **Cyanobacteria:** light-to-biomass conversion efficiency reported as **<10%** (review benchmark; Aug 2024) (grettenberger2024limitingfactorsin pages 1-2).
- **Engineered rhodopsin-driven CO2 fixation (2022, still widely used as quantitative benchmark for later systems):** **20% growth enhancement** under illumination with formate electron donor; **maximum electron transfer efficiency 20%** in a bio-hybrid configuration (DOI:10.1021/acssynbio.2c00397; Oct 2022) (davison2022engineeringarhodopsinbased pages 1-2).
- **Hydrogen production bio-hybrid (2024):** **Faraday efficiency 80%** for H2 production (DOI:10.1073/pnas.2404958121; Jul 2024) (tu2024engineeringbionanoreactorin pages 9-9).
- **Proteorhodopsin photoheterotrophy physiology (2024):** cellular ATP in stationary/death phases **0.0331–1.74 mM**, corresponding to **13.9–367 zeptomoles ATP per cell**, and no significant difference in inorganic carbon assimilation between constant light vs dark in late log phase (DOI:10.4014/jmb.2410.10034; Nov 2024) (oh2024effectoflight pages 1-2).

---

## 7) Candidate causal edges (curation-ready)
The following edge table is designed to be directly transcribed into `data/traits/metabolism/phototrophy.yaml` after curator review.

| Edge (subject–predicate–object) | Candidate node grounding (CURIEs where possible) | Evidence snippet (short quote) | Reference (DOI, year, URL) | Notes/uncertainty (taxon/assay specificity) |
|---|---|---|---|---|
| light exposure → activates → microbial rhodopsin photocycle | ENVO:01001148 light; GO:0016036 cellular response to الضوء?; retinal-bound microbial rhodopsin (label) | “All rhodopsins are activated by visible light and return to their original state through a photocycle” (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2) | 10.1093/ismejo/wrae175 (2024) https://doi.org/10.1093/ismejo/wrae175 | Broad rhodopsin mechanism; not limited to one taxon. |
| visible light absorption by rhodopsin → enables → ion transport function | retinal (CHEBI:30526); microbial rhodopsin (label); GO:0006811 ion transport | “During the photocycle, they exhibit their cognate protein functions such as ion transport” (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2) | 10.1093/ismejo/wrae175 (2024) https://doi.org/10.1093/ismejo/wrae175 | General mechanistic edge for rhodopsin phototrophy. |
| proton-pumping proteorhodopsin/PPR → generates → proton gradient / proton motive force | proteorhodopsin/PPR (label); GO:0015992 proton transport; proton motive force (label) | “pump protons outside of the cell membrane, thus creating a proton gradient” (li2024insitucommunity pages 13-15) | 10.1128/spectrum.02177-23 (2024) https://doi.org/10.1128/spectrum.02177-23 | Strong for marine PPR-bearing bacteria. |
| proton gradient / PMF → drives → ATP synthesis | ATP synthase (EC:7.1.2.2); ATP (CHEBI:15422) | “creating a proton gradient to drive the synthesis of ATP” (li2024insitucommunity pages 13-15) | 10.1128/spectrum.02177-23 (2024) https://doi.org/10.1128/spectrum.02177-23 | Direct support for rhodopsin-based energy conservation. |
| rhodopsin phototrophy → supports → survival/growth in nutrient-limited environments | phototrophy traitmech:000037; nutrient limitation (ENVO label) | “the energy harnessed facilitates the survival and growth of the bacteria in nutrient-limited environments” (li2024insitucommunity pages 13-15) | 10.1128/spectrum.02177-23 (2024) https://doi.org/10.1128/spectrum.02177-23 | Ecological association; strongest for marine bacteria. |
| rhodopsin expression → positively correlates with → non-Calvin carbon fixation gene expression | rhodopsin gene (label); NCF pathways (label) | “rhodopsin expression level of these four orders exhibited significantly positive correlations with their NCF gene expression” (li2024insitucommunity pages 13-15) | 10.1128/spectrum.02177-23 (2024) https://doi.org/10.1128/spectrum.02177-23 | Correlative, not direct causation; curate as uncertain/supporting ecological edge. |
| photons captured by phycobilisomes/pigments → transfer energy to → photosystems | phycobilisome (GO:0030089); chlorophyll a (CHEBI:28966); carotenoid (CHEBI:23044) | “Photons are captured at specialized structures called phycobilisomes… capture light energy and transfer it to the photosystems” (grettenberger2024limitingfactorsin pages 1-2) | 10.1111/1751-7915.14519 (2024) https://doi.org/10.1111/1751-7915.14519 | Oxygenic cyanobacterial mechanism. |
| photosystem II water oxidation → supplies → electrons to electron transport chain | PSII (GO:0009523); water (CHEBI:15377); plastoquinone (CHEBI:16389) | “electrons from the photo-oxidation of water in PSII are transferred through… plastoquinone to cytochrome b6f” (grettenberger2024limitingfactorsin pages 1-2) | 10.1111/1751-7915.14519 (2024) https://doi.org/10.1111/1751-7915.14519 | Oxygenic photosynthesis-specific. |
| cytochrome b6f / PSI electron flow → produces → NADPH | cytochrome b6f complex (GO:0009512); PSI (GO:0009522); ferredoxin (CHEBI:17739); NADPH (CHEBI:16474) | “These electrons are eventually transferred to ferredoxin and NADP+ to form NADPH” (grettenberger2024limitingfactorsin pages 1-2) | 10.1111/1751-7915.14519 (2024) https://doi.org/10.1111/1751-7915.14519 | Canonical oxygenic phototrophy edge. |
| photosynthetic electron transfer / proton gradient → produces → ATP | proton gradient (label); ATP (CHEBI:15422) | “NADPH and ATP are produced from a proton gradient” (grettenberger2024limitingfactorsin pages 1-2) | 10.1111/1751-7915.14519 (2024) https://doi.org/10.1111/1751-7915.14519 | Canonical oxygenic phototrophy edge. |
| blue/green/yellow spectral environment → selects for → rhodopsin absorption variants | retinal chromophore (CHEBI:30526); cyanorhodopsin-II (label) | “blue-light enriched deep/pelagic waters” versus “green-light-enriched surface/coastal waters”; YCyR-II “absorbed yellow light (λmax = 570 nm), whereas GCyR-II absorbed green light (λmax = 550 nm)” (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2) | 10.1093/ismejo/wrae175 (2024) https://doi.org/10.1093/ismejo/wrae175 | Habitat-adaptation edge; taxon-specific to cyanobacterial rhodopsins/proteorhodopsins. |
| high light → damages/inhibits → PSII | high light (ENVO label); PSII (GO:0009523) | “High-energy photons and the generation of free radicals damage PSII” (grettenberger2024limitingfactorsin pages 1-2) | 10.1111/1751-7915.14519 (2024) https://doi.org/10.1111/1751-7915.14519 | Strong environmental inhibitor edge for cyanobacterial photosynthesis. |
| UV light → damages → phycobilisomes/pigments/PSII | ultraviolet light (ENVO label); phycobilisome (GO:0030089); PSII (GO:0009523) | “UV light breaks phycobilisomes, bleaches pigments, and damages PSII” (grettenberger2024limitingfactorsin pages 1-2) | 10.1111/1751-7915.14519 (2024) https://doi.org/10.1111/1751-7915.14519 | Strong inhibitor edge. |
| nutrient limitation → modulates/reduces → photosynthesis or shifts to compensatory trophic modes | nutrient limitation (ENVO label); photosynthesis (GO:0015979) | “use phagotrophy to compensate for the reduction of photosynthesis due to nutrient limitation” (li2024insitucommunity pages 13-15) | 10.1128/spectrum.02177-23 (2024) https://doi.org/10.1128/spectrum.02177-23 | Indirect/modulatory; shown in subtropical ocean phytoplankton. |
| salinity → modulates → non-Calvin carbon fixation activity | salinity (ENVO:3100031 if available, else label); NCF pathways (label) | “Cytophagales, Nitrospinales, and Oceanospirillales was significantly positively correlated with salinity” (li2024insitucommunity pages 13-15) | 10.1128/spectrum.02177-23 (2024) https://doi.org/10.1128/spectrum.02177-23 | Environmental modulation of light-supported carbon fixation; not phototrophy-exclusive. |
| acidic pH (<6.5) → permits/activates → mirror proteorhodopsin outward proton pumping | mirror proteorhodopsin/SpaR (label); pH (PATO:0001923) | “SpaR operates as a light-driven proton pump at pH < 6.5” (okhrimenko2023mirrorproteorhodopsins pages 1-2) | 10.1038/s42004-023-00884-8 (2023) https://doi.org/10.1038/s42004-023-00884-8 | Taxon/clade-specific; do not generalize to all proteorhodopsins. |
| Zn2+ → inhibits → mirror proteorhodopsin proton pumping | zinc(2+) (CHEBI:29105); mirror proteorhodopsin/SpaR (label) | “at mM concentrations of Zn2+, outward proton pumping is inhibited” (okhrimenko2023mirrorproteorhodopsins pages 1-2) | 10.1038/s42004-023-00884-8 (2023) https://doi.org/10.1038/s42004-023-00884-8 | Strong but clade-specific inhibition; not generalizable to all rhodopsins. |
| rhodopsin + MtrCAB-mediated extracellular electron uptake → enables → photoelectrosynthetic CO2 fixation | Gloeobacter rhodopsin (label); MtrCAB complex (UniProt/label); Calvin-Benson-Bassham cycle (KEGG:00710); CO2 (CHEBI:16526) | “The engineered bacteria obtain electrons from the electrode, mediated by the Mtr complex and flavins, to synthesise reducing power… In the presence of ATP and NADPH, the Calvin–Benson–Bassham (CBB) cycle is activated” (tu2023engineeringartificialphotosynthesis pages 2-3) | 10.1038/s41467-023-43524-4 (2023) https://doi.org/10.1038/s41467-023-43524-4 | Synthetic-biology implementation in engineered R. eutropha; curate separately from natural trait edges. |
| light-driven rhodopsin + canthaxanthin in periplasmic bionanoreactor → boosts → hydrogen production | Gloeobacter rhodopsin (label); canthaxanthin (CHEBI:23086); hydrogenase ([FeFe]-hydrogenase, EC:1.12.7.2); H2 (CHEBI:18276) | “The introduction of Gloeobacter rhodopsin and canthaxanthin boosted proton pumping into the periplasm… achieved a Faraday efficiency of 80% for hydrogen production” (tu2024engineeringbionanoreactorin pages 9-9) | 10.1073/pnas.2404958121 (2024) https://doi.org/10.1073/pnas.2404958121 | Engineered application, not native microbial trait mechanism; useful as implementation example only. |


*Table: This table lists candidate mechanistic edges for microbial phototrophy spanning chlorophyll-based photosystems, rhodopsin-based proton pumps, environmental modulators, and engineered implementations. It is designed to support TraitMech curation of traitmech:000037 with concise evidence, grounding, and uncertainty notes.*

---

## 8) Warnings / claims not yet safe to curate into TraitMech

1. **“Rhodopsin supports carbon fixation”**: meta-omics evidence currently supports *correlation* between proton-pump rhodopsin expression and non-Calvin carbon fixation genes in multiple taxa, but causality is not experimentally resolved in situ; curate as **uncertain** or as a modulatory/association edge (li2024insitucommunity pages 13-15).
2. **Engineered photoelectrosynthesis edges** (MtrCAB + rhodopsin; periplasmic bionanoreactor H2) demonstrate mechanistic feasibility but should be separated as **applications/implementations** rather than baseline trait mechanism (tu2023engineeringartificialphotosynthesis pages 2-3, tu2024engineeringbionanoreactorin pages 9-9).
3. **Zn2+ inhibition** and **acidic pH operation** are strong for mirror proteorhodopsins but should not be generalized to all proteorhodopsins or proton-pumping rhodopsins without additional evidence (okhrimenko2023mirrorproteorhodopsins pages 1-2).

---

## DOI-first bibliography (with dates and URLs where available)

**2024**
- Grettenberger CL, Abou-Shanab R, Hamilton TL. *Limiting factors in the operation of photosystems I and II in cyanobacteria.* **Microbial Biotechnology** (published Aug 2024). DOI: **10.1111/1751-7915.14519**. URL: https://doi.org/10.1111/1751-7915.14519 (grettenberger2024limitingfactorsin pages 1-2)
- Hasegawa-Takano M, et al. *Cyanorhodopsin-II represents a yellow-absorbing proton-pumping rhodopsin clade within cyanobacteria.* **The ISME Journal** (published Jan 2024). DOI: **10.1093/ismejo/wrae175**. URL: https://doi.org/10.1093/ismejo/wrae175 (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2)
- Li H, et al. *In situ community transcriptomics illuminates CO2-fixation potentials and supporting roles of phagotrophy and proton pump in plankton in a subtropical marginal sea.* **Microbiology Spectrum** (published Mar 2024). DOI: **10.1128/spectrum.02177-23**. URL: https://doi.org/10.1128/spectrum.02177-23 (li2024insitucommunity pages 13-15)
- Oh H-M, et al. *Effect of Light Regime on Candidatus Puniceispirillum marinum IMCC1322 in Nutrient-Replete Conditions.* **Journal of Microbiology and Biotechnology** (published Nov 2024). DOI: **10.4014/jmb.2410.10034**. URL: https://doi.org/10.4014/jmb.2410.10034 (oh2024effectoflight pages 1-2)
- Tu W, Thompson IP, Huang WE. *Engineering bionanoreactor in bacteria for efficient hydrogen production.* **PNAS** (published Jul 2024). DOI: **10.1073/pnas.2404958121**. URL: https://doi.org/10.1073/pnas.2404958121 (tu2024engineeringbionanoreactorin pages 9-9)

**2023**
- Chazan A, et al. *Phototrophy by antenna-containing rhodopsin pumps in aquatic environments.* **Nature** (published Mar 2023). DOI: **10.1038/s41586-023-05774-6**. URL: https://doi.org/10.1038/s41586-023-05774-6 (chazan2023phototrophybyantennacontaining media 6d67b0c1, chazan2023phototrophybyantennacontaining pages 1-7)
- Okhrimenko IS, et al. *Mirror proteorhodopsins.* **Communications Chemistry** (published May 2023). DOI: **10.1038/s42004-023-00884-8**. URL: https://doi.org/10.1038/s42004-023-00884-8 (okhrimenko2023mirrorproteorhodopsins pages 1-2)
- Tu W, Xu J, Thompson IP, Huang WE. *Engineering artificial photosynthesis based on rhodopsin for CO2 fixation.* **Nature Communications** (published Dec 2023). DOI: **10.1038/s41467-023-43524-4**. URL: https://doi.org/10.1038/s41467-023-43524-4 (tu2023engineeringartificialphotosynthesis pages 2-3)

**2022 (quantitative engineering benchmark)**
- Davison PA, et al. *Engineering a Rhodopsin-Based Photo-Electrosynthetic System in Bacteria for CO2 Fixation.* **ACS Synthetic Biology** (published Oct 2022). DOI: **10.1021/acssynbio.2c00397**. URL: https://doi.org/10.1021/acssynbio.2c00397 (davison2022engineeringarhodopsinbased pages 1-2)
- Tu W, Huang WE. *Rhodopsin driven microbial CO2 fixation using synthetic biology design.* **Environmental Microbiology** (published Oct 2022). DOI: **10.1111/1462-2920.16243**. URL: https://doi.org/10.1111/1462-2920.16243 (tu2022rhodopsindrivenmicrobial pages 1-3)

**Foundational scope**
- Bryant DA, Frigaard N-U. *Prokaryotic photosynthesis and phototrophy illuminated.* **Trends in Microbiology** (published Nov 2006). DOI: **10.1016/j.tim.2006.09.001**. URL: https://doi.org/10.1016/j.tim.2006.09.001 (bryant2006prokaryoticphotosynthesisand pages 1-2, bryant2006prokaryoticphotosynthesisand pages 2-3, bryant2006prokaryoticphotosynthesisand pages 6-7)


References

1. (bryant2006prokaryoticphotosynthesisand pages 2-3): Donald A. Bryant and Niels-Ulrik Frigaard. Prokaryotic photosynthesis and phototrophy illuminated. Trends in microbiology, 14 11:488-96, Nov 2006. URL: https://doi.org/10.1016/j.tim.2006.09.001, doi:10.1016/j.tim.2006.09.001. This article has 812 citations and is from a domain leading peer-reviewed journal.

2. (bryant2006prokaryoticphotosynthesisand pages 1-2): Donald A. Bryant and Niels-Ulrik Frigaard. Prokaryotic photosynthesis and phototrophy illuminated. Trends in microbiology, 14 11:488-96, Nov 2006. URL: https://doi.org/10.1016/j.tim.2006.09.001, doi:10.1016/j.tim.2006.09.001. This article has 812 citations and is from a domain leading peer-reviewed journal.

3. (hasegawatakano2024cyanorhodopsiniirepresentsa pages 1-2): Masumi Hasegawa-Takano, Toshiaki Hosaka, Keiichi Kojima, Yosuke Nishimura, Marie Kurihara, Yu Nakajima, Yoshiko Ishizuka-Katsura, Tomomi Kimura-Someya, Mikako Shirouzu, Yuki Sudo, and Susumu Yoshizawa. Cyanorhodopsin-ii represents a yellow-absorbing proton-pumping rhodopsin clade within cyanobacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae175, doi:10.1093/ismejo/wrae175. This article has 4 citations.

4. (tu2023engineeringartificialphotosynthesis pages 2-3): Weiming Tu, Jiabao Xu, Ian P. Thompson, and Wei E. Huang. Engineering artificial photosynthesis based on rhodopsin for co2 fixation. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43524-4, doi:10.1038/s41467-023-43524-4. This article has 68 citations and is from a highest quality peer-reviewed journal.

5. (tu2024engineeringbionanoreactorin pages 9-9): Weiming Tu, Ian P. Thompson, and Wei E. Huang. Engineering bionanoreactor in bacteria for efficient hydrogen production. Proceedings of the National Academy of Sciences of the United States of America, Jul 2024. URL: https://doi.org/10.1073/pnas.2404958121, doi:10.1073/pnas.2404958121. This article has 36 citations and is from a highest quality peer-reviewed journal.

6. (grettenberger2024limitingfactorsin pages 1-2): Christen L. Grettenberger, Reda Abou‐Shanab, and Trinity L. Hamilton. Limiting factors in the operation of photosystems i and ii in cyanobacteria. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14519, doi:10.1111/1751-7915.14519. This article has 14 citations and is from a peer-reviewed journal.

7. (li2024insitucommunity pages 13-15): Hongfei Li, Jianwei Chen, Liying Yu, Guangyi Fan, Tangcheng Li, Ling Li, Huatao Yuan, Jingtian Wang, Cong Wang, Denghui Li, and Senjie Lin. <i>in situ</i> community transcriptomics illuminates co <sub>2</sub> -fixation potentials and supporting roles of phagotrophy and proton pump in plankton in a subtropical marginal sea. Mar 2024. URL: https://doi.org/10.1128/spectrum.02177-23, doi:10.1128/spectrum.02177-23. This article has 6 citations and is from a domain leading peer-reviewed journal.

8. (okhrimenko2023mirrorproteorhodopsins pages 1-2): Ivan S. Okhrimenko, Kirill Kovalev, Lada E. Petrovskaya, Nikolay S. Ilyinsky, Alexey A. Alekseev, Egor Marin, Tatyana I. Rokitskaya, Yuri N. Antonenko, Sergey A. Siletsky, Petr A. Popov, Yuliya A. Zagryadskaya, Dmytro V. Soloviov, Igor V. Chizhov, Dmitrii V. Zabelskii, Yury L. Ryzhykau, Alexey V. Vlasov, Alexander I. Kuklin, Andrey O. Bogorodskiy, Anatolii E. Mikhailov, Daniil V. Sidorov, Siarhei Bukhalovich, Fedor Tsybrov, Sergey Bukhdruker, Anastasiia D. Vlasova, Valentin I. Borshchevskiy, Dmitry A. Dolgikh, Mikhail P. Kirpichnikov, Ernst Bamberg, and Valentin I. Gordeliy. Mirror proteorhodopsins. Communications Chemistry, May 2023. URL: https://doi.org/10.1038/s42004-023-00884-8, doi:10.1038/s42004-023-00884-8. This article has 12 citations and is from a peer-reviewed journal.

9. (chazan2023phototrophybyantennacontaining media 6d67b0c1): Ariel Chazan, Ishita Das, Takayoshi Fujiwara, Shunya Murakoshi, Andrey Rozenberg, Ana Molina-Márquez, Fumiya K. Sano, Tatsuki Tanaka, Patricia Gómez-Villegas, Shirley Larom, Alina Pushkarev, Partha Malakar, Masumi Hasegawa, Yuya Tsukamoto, Tomohiro Ishizuka, Masae Konno, Takashi Nagata, Yosuke Mizuno, Kota Katayama, Rei Abe-Yoshizumi, Sanford Ruhman, Keiichi Inoue, Hideki Kandori, Rosa León, Wataru Shihoya, Susumu Yoshizawa, Mordechai Sheves, Osamu Nureki, and Oded Béjà. Phototrophy by antenna-containing rhodopsin pumps in aquatic environments. Nature, 615:535-540, Mar 2023. URL: https://doi.org/10.1038/s41586-023-05774-6, doi:10.1038/s41586-023-05774-6. This article has 49 citations and is from a highest quality peer-reviewed journal.

10. (davison2022engineeringarhodopsinbased pages 1-2): Paul A. Davison, Weiming Tu, Jiabao Xu, Simona Della Valle, Ian P. Thompson, C. Neil Hunter, and Wei E. Huang. Engineering a rhodopsin-based photo-electrosynthetic system in bacteria for co2 fixation. ACS Synthetic Biology, 11:3805-3816, Oct 2022. URL: https://doi.org/10.1021/acssynbio.2c00397, doi:10.1021/acssynbio.2c00397. This article has 33 citations and is from a domain leading peer-reviewed journal.

11. (chazan2023phototrophybyantennacontaining pages 1-7): Ariel Chazan, Ishita Das, Takayoshi Fujiwara, Shunya Murakoshi, Andrey Rozenberg, Ana Molina-Márquez, Fumiya K. Sano, Tatsuki Tanaka, Patricia Gómez-Villegas, Shirley Larom, Alina Pushkarev, Partha Malakar, Masumi Hasegawa, Yuya Tsukamoto, Tomohiro Ishizuka, Masae Konno, Takashi Nagata, Yosuke Mizuno, Kota Katayama, Rei Abe-Yoshizumi, Sanford Ruhman, Keiichi Inoue, Hideki Kandori, Rosa León, Wataru Shihoya, Susumu Yoshizawa, Mordechai Sheves, Osamu Nureki, and Oded Béjà. Phototrophy by antenna-containing rhodopsin pumps in aquatic environments. Nature, 615:535-540, Mar 2023. URL: https://doi.org/10.1038/s41586-023-05774-6, doi:10.1038/s41586-023-05774-6. This article has 49 citations and is from a highest quality peer-reviewed journal.

12. (oh2024effectoflight pages 1-2): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

13. (tu2022rhodopsindrivenmicrobial pages 1-3): Weiming Tu and Wei E. Huang. Rhodopsin driven microbial <scp>co<sub>2</sub></scp> fixation using synthetic biology design. Oct 2022. URL: https://doi.org/10.1111/1462-2920.16243, doi:10.1111/1462-2920.16243. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (bryant2006prokaryoticphotosynthesisand pages 6-7): Donald A. Bryant and Niels-Ulrik Frigaard. Prokaryotic photosynthesis and phototrophy illuminated. Trends in microbiology, 14 11:488-96, Nov 2006. URL: https://doi.org/10.1016/j.tim.2006.09.001, doi:10.1016/j.tim.2006.09.001. This article has 812 citations and is from a domain leading peer-reviewed journal.