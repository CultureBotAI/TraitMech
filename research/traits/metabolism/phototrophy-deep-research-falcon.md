---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:43:58.923645'
end_time: '2026-08-04T06:50:28.823832'
duration_seconds: 389.9
template_file: templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'phototrophy_light_energy_capture: 11 nodes, 9 edges'
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
- **Trait label:** phototrophy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000037
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism captures light as its energy source. It encompasses chlorophyll-based photosynthesis (with photochemical reaction centers) and retinal-based (rhodopsin) light-driven ion pumping.
- **Parent traits:** METPO:1000060
- **Synonyms:** phototrophic metabolism
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", frames phototrophy as the broad use of light for energy, spanning chlorophyll- and rhodopsin-based mechanisms; parent of the photosynthesis and proteorhodopsin phototrophy sub-variants.) | DOI:10.1126/science.289.5486.1902:  (Béjà et al. established retinal-based proteorhodopsin phototrophy as a light-energy capture mechanism distinct from chlorophyll-based photosynthesis.)
- **Existing causal graph summary:** phototrophy_light_energy_capture: 11 nodes, 9 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000037
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism captures light as its energy source. It encompasses chlorophyll-based photosynthesis (with photochemical reaction centers) and retinal-based (rhodopsin) light-driven ion pumping.
- **Parent traits:** METPO:1000060
- **Synonyms:** phototrophic metabolism
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", frames phototrophy as the broad use of light for energy, spanning chlorophyll- and rhodopsin-based mechanisms; parent of the photosynthesis and proteorhodopsin phototrophy sub-variants.) | DOI:10.1126/science.289.5486.1902:  (Béjà et al. established retinal-based proteorhodopsin phototrophy as a light-energy capture mechanism distinct from chlorophyll-based photosynthesis.)
- **Existing causal graph summary:** phototrophy_light_energy_capture: 11 nodes, 9 edges

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


# Curation-focused research report: microbial phototrophy

## Trait record and scope

- **Trait label:** phototrophy
- **Trait identifier:** `traitmech:000037`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1000060`
- **Recommended operational definition:** the capacity to capture photon energy and convert it into metabolically available chemical or electrochemical energy that supports cellular maintenance, growth, or biosynthesis.

Phototrophy is broader than photosynthesis. Photosynthesis uses light-derived energy and reducing power to reduce CO₂ into biomass, whereas phototrophy only requires light-to-chemical-energy conversion supporting growth. Thus, every photosynthetic microorganism is phototrophic, but a rhodopsin-powered photoheterotroph that does not fix CO₂ is still phototrophic. The two independently evolved core implementations are **chlorophototrophy**, based on chlorophyll/bacteriochlorophyll photochemical reaction centers, and **retinalophototrophy**, based on retinal-bound microbial rhodopsins. (bryant2006prokaryoticphotosynthesisand pages 2-3, peterson2023usinglightfor pages 1-5, bryant2006prokaryoticphotosynthesisand pages 1-2)

### Boundaries

**Include:**

1. Oxygenic chlorophototrophy in cyanobacteria and microbial eukaryotic phototrophs.
2. Anoxygenic chlorophototrophy, including cyclic photoheterotrophy and photoautotrophy using donors such as sulfide, sulfur, thiosulfate, H₂, or Fe²⁺.
3. Energy-conserving retinal phototrophy mediated by outward proton- or other ion-pumping rhodopsins.
4. Facultative phototrophy in organisms that principally use organic substrates but supplement their energy budget with light.

**Do not equate with:**

- **Photoautotrophy:** requires light plus autotrophic carbon fixation; it is a narrower composite phenotype.
- **Photosynthesis:** in the strict definition used by Bryant and Frigaard, it includes light-powered CO₂ reduction; phototrophy need not.
- **Pigmentation:** pigment presence alone does not establish energy conservation.
- **Photoreception/phototaxis:** sensory rhodopsins or other photoreceptors that alter behavior without conserving photon energy should not establish this trait.
- **Fluorescence or photoprotection:** light absorption without productive energy transduction is insufficient.
- **Genomic potential alone:** a rhodopsin gene or photosynthesis gene cluster is evidence of candidate capacity, not necessarily an expressed phenotype.

## Candidate graph architecture

The graph should have `traitmech:000037` as the phenotype endpoint and two parallel mechanistic branches. Both converge on an electrochemical gradient and/or reducing equivalents that support ATP production and growth. Oxygenic, anoxygenic, and carbon-fixing processes should be represented as conditional subgraphs rather than universal requirements.

| Module | Minimal causal chain | Evidence strength | Curation status |
|---|---|---|---|
| Chlorophyll reaction-center phototrophy | light -> (bacterio)chlorophyll reaction center -> charge separation/electron transfer -> proton motive force -> ATP synthesis -> phototrophic energy conservation (bryant2006prokaryoticphotosynthesisand pages 2-3, bryant2006prokaryoticphotosynthesisand pages 1-2, kacar2406foundationsforreconstructing pages 15-18) | Strong review-supported core mechanism | Curate as core generalized module |
| Oxygenic branch | light -> PSII/PSI-type oxygenic photosystems -> H2O oxidation -> O2 production -> electron transport -> proton motive force -> ATP/NADPH -> carbon fixation or growth support (bryant2006prokaryoticphotosynthesisand pages 1-2, kacar2406foundationsforreconstructing pages 15-18) | Strong for cyanobacterial oxygenic phototrophy; some steps review-level here | Curate as child branch; taxon-specific to oxygenic phototrophs |
| Anoxygenic sulfur branch | light -> anoxygenic reaction center -> cyclic/linked electron transport -> sulfur compound oxidation (H2S/S0/thiosulfate) -> proton motive force/reducing power -> ATP + CO2 fixation or photoheterotrophic support (bryant2006prokaryoticphotosynthesisand pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 18-18) | Strong review support; donor usage varies by lineage | Curate with uncertainty tags on donor specificity and lineage scope |
| Retinal/rhodopsin branch | light -> retinal-bound microbial rhodopsin -> retinal isomerization -> proton/ion pumping -> proton motive force -> ATP synthesis -> phototrophic energy gain (bryant2006prokaryoticphotosynthesisand pages 2-3, peterson2023usinglightfor pages 1-5, davison2022engineeringarhodopsinbased pages 1-2) | Strong for proton-pumping phototrophy; direct engineering evidence for ATP-linked outcomes | Curate as core generalized module; ion specificity may need subtype nodes |
| Ecological fitness branch | diurnal light-dark cycles + nutrient limitation -> facultative phototrophy deployment -> rhythmic physiology/survival advantage in stationary phase (tinguely2023diurnalcyclesdrive pages 9-10) | Moderate; direct experiment but taxon/condition specific | Curate as conditional ecology branch; mark assay- and taxon-specific |
| Engineered application branch | heterologous rhodopsin + retinal + electron donor/electrode -> light-driven proton motive force -> ATP-supported CO2 fixation -> enhanced growth / photo-electrosynthesis (davison2022engineeringarhodopsinbased pages 1-2, tu2024engineeringrhodopsinbasedartificial pages 102-105) | Moderate to strong for engineered systems; not native trait evidence | Do not use as native core edge; curate separately as engineered implementation |


*Table: This table summarizes the main candidate modules for a phototrophy causal graph, with minimal mechanism chains, evidence strength, and curation recommendations. It helps separate core native mechanisms from lineage-specific ecology and engineered applications.*

## Candidate nodes grouped by type

### Environmental and experimental factors

- incident light / photon
- wavelength or spectral quality
- green light and blue light
- light intensity
- light–dark or diurnal cycle
- nutrient limitation
- anoxic or sulfidic environment
- availability of H₂S, sulfur, thiosulfate, H₂, or Fe²⁺
- availability of retinal or retinal precursors
- exogenous trans-retinal — assay-specific
- electron donor, including formate — engineered systems
- electrode, solar panel, riboflavin electron shuttle — engineered systems

### Pigments, cofactors, and chemicals

- chlorophyll
- bacteriochlorophyll a/b/c/d/e
- retinal / all-trans-retinal — `CHEBI:15035` should be independently verified before use
- 13-cis-retinal — label only pending identifier verification
- proton — `CHEBI:15378`
- water — `CHEBI:15377`
- molecular oxygen — `CHEBI:15379`
- carbon dioxide — `CHEBI:16526`
- hydrogen sulfide — `CHEBI:16136` should be independently verified
- elemental sulfur — label only
- thiosulfate — label only pending charge-state-specific grounding
- molecular hydrogen — `CHEBI:18276` should be independently verified
- iron(II) — label only pending ionic-species verification
- ATP — `CHEBI:15422`
- NADPH and reduced ferredoxin — label only pending exact species
- quinone pool
- decanoate — candidate placeholder in retinal-free proteoopsin; do not curate from the present evidence set without the primary structural excerpt

### Proteins and complexes

- Type I photochemical reaction center
- Type II photochemical reaction center
- Photosystem I
- Photosystem II
- oxygen-evolving complex
- reaction-center core proteins PufL/PufM (`pufL`, `pufM`)
- bacteriochlorophyll biosynthesis proteins BchH/BchD/BchI and BchL/BchN/BchB
- chlorosome antenna complex
- electron-transport chain
- ferredoxin–NAD(P) oxidoreductase
- dissimilatory sulfur oxidation/reduction machinery, including Dsr-related systems where lineage-appropriate
- ATP synthase
- microbial rhodopsin
- proteorhodopsin
- Gloeobacter rhodopsin
- retinal biosynthesis module
- MtrCAB extracellular electron-transfer complex — engineered branch only
- carbonic anhydrase — engineered branch only

### Cellular structures and localizations

- cytoplasmic membrane
- periplasm or extracellular side of the membrane
- thylakoid membrane
- photosynthetic intracytoplasmic membrane
- chlorosome
- reaction-center antenna supercomplex
- proton-motive force across an energy-transducing membrane

### Processes and pathways

- phototrophy — `traitmech:000037`
- photosynthesis — `GO:0015979`
- light harvesting
- photochemical charge separation
- cyclic photosynthetic electron transport
- linear photosynthetic electron transport
- proton translocation
- proton-motive-force generation
- photophosphorylation
- water oxidation
- oxygen evolution
- sulfur-compound oxidation
- carbon fixation
- Calvin–Benson–Bassham cycle
- reductive tricarboxylic-acid cycle
- retinal photoisomerization
- stationary-phase survival

## Evidence-backed candidate edges

Snippets below are concise quotations or close source summaries returned from the full-text evidence extraction; wording should be checked against the final PDF during YAML curation.

| # | Subject — predicate — object | Reference and supporting snippet | Curation note |
|---|---|---|---|
| 1 | photon — **is absorbed by** — chlorophyll/bacteriochlorophyll reaction center | Bryant & Frigaard: photochemical reaction centers containing (bacterio)chlorophyll initiate light-driven electron transfer. (bryant2006prokaryoticphotosynthesisand pages 2-3, bryant2006prokaryoticphotosynthesisand pages 1-2) | **Core; strong review support.** |
| 2 | excited reaction center — **initiates** — electron transfer | “(B)Chl-containing photochemical reaction centers … initiate light-driven electron transfer,” producing oxidants/reductants. (bryant2006prokaryoticphotosynthesisand pages 2-3) | **Core.** Consider separate Type I and Type II children. |
| 3 | photosynthetic electron transfer — **generates** — proton-motive force | Reaction-center electron flow may be cyclic or linear and generates proton-motive force. (bryant2006prokaryoticphotosynthesisand pages 2-3) | **Core**, but exact proton-translocation complex depends on lineage. |
| 4 | proton-motive force — **drives** — ATP synthase | Rhodopsin- and reaction-center-derived gradients are used for ATP synthesis. (bryant2006prokaryoticphotosynthesisand pages 2-3, peterson2023usinglightfor pages 1-5, davison2022engineeringarhodopsinbased pages 1-2) | **Core convergence edge.** |
| 5 | ATP synthase — **produces** — ATP | Light-generated proton gradients support ATP synthesis. (peterson2023usinglightfor pages 1-5, davison2022engineeringarhodopsinbased pages 1-2) | **Core**, but represent ADP/Pi substrates if graph granularity permits. |
| 6 | water — **donates electrons to** — oxygenic photosynthetic electron transport | Cyanobacterial oxygenic photosynthesis uses water as electron donor and evolves O₂. (bryant2006prokaryoticphotosynthesisand pages 1-2) | **Strong, cyanobacteria/oxygenic branch only.** |
| 7 | water oxidation — **produces** — molecular oxygen | Oxygenic photosynthesis is distinguished by water as donor and O₂ evolution. (bryant2006prokaryoticphotosynthesisand pages 1-2, kacar2406foundationsforreconstructing pages 18-21) | **Conditional, not a defining edge for all phototrophy.** |
| 8 | H₂S / sulfur / thiosulfate / H₂ / Fe²⁺ — **donates electrons to** — anoxygenic photosynthetic electron transport | The foundational review lists sulfide, sulfur, thiosulfate, Fe²⁺, and H₂ as donors used by different anoxygenic phototrophs. (bryant2006prokaryoticphotosynthesisand pages 1-2) | **Taxon-specific donor alternatives; never assert all donors for one organism.** |
| 9 | green sulfur bacterium — **oxidizes** — H₂S to elemental sulfur | The 2024 review describes green sulfur bacteria using H₂S as the principal donor and oxidizing it to elemental sulfur. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18) | **Taxon-specific; strong review support.** |
| 10 | chlorosome — **harvests light for** — Type I reaction center | Chlorobi contain BChl c/d/e in chlorosomes coupled to Type I reaction centers. (bryant2006prokaryoticphotosynthesisand pages 1-2) | **Taxon-specific structural edge.** |
| 11 | light — **activates** — retinal-bound microbial rhodopsin | Retinalophototrophy uses a microbial rhodopsin covalently bound to all-trans-retinal; absorption activates the pump. (peterson2023usinglightfor pages 1-5) | **Core retinal branch.** |
| 12 | retinal photoisomerization — **causes** — outward proton translocation | Bryant and Frigaard describe light-induced retinal isomerization causing proton translocation to the periplasm. (bryant2006prokaryoticphotosynthesisand pages 2-3, bryant2006prokaryoticphotosynthesisand pages 1-2) | **Core for outward proton pumps; not universal to sensory, chloride-, or sodium-pumping rhodopsins.** |
| 13 | outward proton-pumping rhodopsin — **generates** — proton-motive force | Rhodopsins directly expel protons without an electron-transfer chain, creating a gradient used by ATP synthase. (bryant2006prokaryoticphotosynthesisand pages 2-3) | **Core retinal branch.** |
| 14 | retinal-bound rhodopsin — **pumps approximately** — one proton per absorbed photon | The 2023 synthetic-construction paper characterizes the simple retinal system as pumping one proton per photon. (peterson2023usinglightfor pages 1-5) | **Uncertain/generalized:** preprint and protein/condition dependence; do not encode universal stoichiometry without primary kinetic evidence. |
| 15 | functional reaction centers under diurnal light and nutrient limitation — **increase** — stationary-phase survival | In *Porphyrobacter* ULC335, survival depended on functional reaction centers; light–dark cycles changed expression of over 50% of genes. (tinguely2023diurnalcyclesdrive pages 9-10) | **Direct but taxon-, phase-, and assay-specific.** |
| 16 | photosynthesis gene cluster — **confers candidate capacity for** — Type II reaction-center phototrophy | Myxococcota metagenomes contained PGCs with `PufLM`, `BchHDI`, and `BchLNB`; expression was detected environmentally and pigment genes functioned heterologously. (li2023globallydistributedmyxococcota pages 4-5) | **Uncertain for native phenotype:** metagenomic/transcriptomic inference plus heterologous support, not cultivation-level demonstration. |
| 17 | Gloeobacter rhodopsin + retinal + light — **generates** — proton gradient/ATP | Engineered *Ralstonia eutropha* used GR and retinal as a light-driven proton pump coupled to ATP synthase. (davison2022engineeringarhodopsinbased pages 1-2) | **Direct engineered evidence; exclude from native core evidence.** |
| 18 | GR-supported ATP production — **supports** — Calvin-cycle CO₂ fixation | The engineered strain linked rhodopsin-generated ATP to native Calvin-cycle carbon fixation. (davison2022engineeringarhodopsinbased pages 1-2) | **Engineered and host-specific.** Rhodopsin phototrophy does not generally imply autotrophy. |
| 19 | light + GR with formate donor — **increases** — engineered bacterial growth | Light produced a **20% growth enhancement** when formate supplied electrons. (davison2022engineeringarhodopsinbased pages 1-2) | **Quantitative, engineered assay-specific edge.** |
| 20 | solar-electrode/riboflavin electron delivery — **supports** — engineered photoelectrosynthetic CO₂ growth | The system reported a maximum **20% electron-transfer efficiency** and growth with CO₂ as sole carbon source. (davison2022engineeringarhodopsinbased pages 1-2) | **Application only; reactor-specific.** |

## Recent developments and expert analysis

### Hidden phylogenetic diversity

A 2023 *Nature Communications* study identified putative Type II photosynthesis gene clusters across at least six Myxococcota families. Its phylogenetic interpretation favors one ancestral acquisition followed by repeated losses over 14 independent acquisitions, although predation-mediated or mobile-element-mediated horizontal transfer remains plausible. This materially expands the candidate distribution of chlorophototrophy, but the phenotype remains incompletely demonstrated in native isolates. (li2023globallydistributedmyxococcota pages 4-5)

### Phototrophy as a temporally regulated survival strategy

The 2023 *ISME Communications* experiment moves beyond gene-presence evidence. Under nutrient limitation, a facultative aerobic anoxygenic phototroph coordinated growth, replication, stress responses, and lysis with light–dark cycles. More than 50% of genes showed cycle-associated transcriptional effects, and functional reaction centers improved stationary-phase survival. The expert interpretation is that facultative phototrophy should be modeled as a conditional energy-supplementation trait, not necessarily as constitutive biomass production. (tinguely2023diurnalcyclesdrive pages 9-10)

### Mechanistic simplicity and transferability of retinal phototrophy

Retinal phototrophy can require a single rhodopsin plus access to retinal, whereas chlorophototrophy requires a much larger multigene apparatus. A 2023 synthetic-construction preprint reported that targeting a fungal rhodopsin to the yeast vacuole produced a green-light-dependent fitness advantage. This supports evolutionary accessibility but should remain outside a microbial bacterial/archaeal native core graph until peer-reviewed and independently replicated. (peterson2023usinglightfor pages 1-5)

### Sulfur-remediation potential

The 2024 green-sulfur-bacterium review connects light capture, sulfide oxidation, elemental-sulfur production, and reductive-TCA carbon fixation, supporting applications in detoxifying illuminated anoxic, sulfide-rich waters. The mechanism is credible, but performance depends on light penetration, sulfide load, reactor ecology, and recovery of sulfur products; it is not a universal phototrophy application. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18)

## Current and emerging applications

1. **Photoelectrosynthetic CO₂ conversion.** Engineered *R. eutropha* bearing Gloeobacter rhodopsin showed 20% light-dependent growth enhancement with formate and up to 20% electron-transfer efficiency in a solar-panel/electrode configuration. This is a laboratory implementation rather than an established industrial process. (davison2022engineeringarhodopsinbased pages 1-2)
2. **Sulfide detoxification and sulfur recovery.** Green sulfur bacteria can oxidize H₂S to elemental sulfur while using light and fixing CO₂ through the reductive TCA cycle, making illuminated anaerobic treatment systems plausible. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18)
3. **Resource-efficient survival engineering.** Rhodopsin modules can supplement cellular energy under carbon or nutrient limitation because they generate proton motive force without a conventional photosynthetic electron-transfer apparatus. (bryant2006prokaryoticphotosynthesisand pages 2-3, peterson2023usinglightfor pages 1-5)
4. **Solar fuels and biohybrid devices.** Rewiring photosynthetic electron-transfer chains and combining rhodopsins with extracellular electron-transfer systems are active research directions. The retrieved evidence supports feasibility but not commercial-scale performance. (tu2024engineeringrhodopsinbasedartificial pages 102-105, davison2022engineeringarhodopsinbased pages 1-2)
5. **Wastewater and biomass valorization.** Phototrophic consortia and microalgae are being investigated for nutrient removal and production of biomass-derived products. These are applications of particular photosynthetic organisms or communities, not causal evidence that every organism annotated `traitmech:000037` performs remediation.

## Recommended minimum YAML graph

A conservative initial graph should retain only broadly supported nodes and edges:

1. `light` → **activates** → `photochemical reaction center`
2. `photochemical reaction center` → **drives** → `photosynthetic electron transport`
3. `photosynthetic electron transport` → **generates** → `proton-motive force`
4. `light` → **activates** → `retinal-bound outward proton-pumping rhodopsin`
5. `retinal-bound outward proton-pumping rhodopsin` → **translocates** → `proton`
6. `proton translocation` → **generates** → `proton-motive force`
7. `proton-motive force` → **drives** → `ATP synthase`
8. `ATP synthase` → **produces** → `ATP`
9. `ATP` → **supports** → `cellular maintenance and growth`
10. `light-to-chemical-energy conservation` → **realizes** → `traitmech:000037`

Oxygenic water oxidation, sulfur donors, carbon fixation, chlorosomes, diurnal survival, and engineered electron-transfer modules should be separate optional branches with taxonomic or experimental qualifiers.

## Warnings: claims not ready for TraitMech curation

- Do not make **CO₂ fixation**, oxygen evolution, or autotrophy necessary conditions of phototrophy.
- Do not infer phototrophy from an uncharacterized rhodopsin sequence; sensory and inward ion-pumping functions exist.
- Do not infer functional chlorophototrophy from pigment-biosynthesis genes alone; require a coherent reaction-center/antenna/electron-transfer module and preferably expression or physiological evidence.
- Do not encode “one proton per photon” as universal; the available support here includes a preprint-level generalization. (peterson2023usinglightfor pages 1-5)
- Do not curate Myxococcota as experimentally verified native phototrophs solely from metagenomes, environmental transcription, and heterologous pigment-gene expression. (li2023globallydistributedmyxococcota pages 4-5)
- Do not generalize the *Porphyrobacter* diurnal survival result beyond nutrient-limited stationary-phase conditions. (tinguely2023diurnalcyclesdrive pages 9-10)
- Do not place MtrCAB, electrodes, riboflavin shuttles, formate, or carbonic anhydrase in the native trait core; these belong to engineered implementations. (tu2024engineeringrhodopsinbasedartificial pages 102-105, davison2022engineeringarhodopsinbased pages 1-2)
- The proposed CHEBI identifiers marked “verify” and all protein/database accessions should be checked against the current ontology release before committing YAML.
- Structural claims about proteorhodopsin pentamer/hexamer assembly, signal-peptide effects, decanoate as a retinal-pocket placeholder, and environmental retinal scavenging were identified in the 2024 literature search but were not recovered as citable full-text evidence in this run; they should not yet be curated.

## DOI-first bibliography

1. Bryant DA, Frigaard N-U. **Prokaryotic photosynthesis and phototrophy illuminated.** *Trends in Microbiology*. Published November 2006. https://doi.org/10.1016/j.tim.2006.09.001. Foundational scope and mechanism review. (bryant2006prokaryoticphotosynthesisand pages 2-3, bryant2006prokaryoticphotosynthesisand pages 1-2)
2. Li L, et al. **Globally distributed Myxococcota with photosynthesis gene clusters illuminate the origin and evolution of a potentially chimeric lifestyle.** *Nature Communications*. Published October 2023. https://doi.org/10.1038/s41467-023-42193-7. (li2023globallydistributedmyxococcota pages 4-5)
3. Tinguely C, et al. **Diurnal cycles drive rhythmic physiology and promote survival in facultative phototrophic bacteria.** *ISME Communications*. Published September 2023. https://doi.org/10.1038/s43705-023-00334-5. (tinguely2023diurnalcyclesdrive pages 9-10)
4. Kushkevych I, et al. **Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments.** *Frontiers in Microbiology*. Published July 2024. https://doi.org/10.3389/fmicb.2024.1417714. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18)
5. Davison PA, et al. **Engineering a Rhodopsin-Based Photo-Electrosynthetic System in Bacteria for CO₂ Fixation.** *ACS Synthetic Biology*. Published October 2022. https://doi.org/10.1021/acssynbio.2c00397. (davison2022engineeringarhodopsinbased pages 1-2)
6. Peterson A, et al. **Using light for energy: examining the evolution of phototrophic metabolism through synthetic construction.** *bioRxiv* preprint, April 2023. https://doi.org/10.1101/2022.12.06.519405. Treat as preprint evidence. (peterson2023usinglightfor pages 1-5)
7. Kaçar B. **Foundations for reconstructing early microbial life.** arXiv preprint, 2024; metadata returned an erroneous year of 2406. https://doi.org/10.48550/arXiv.2406.09354. Use only for contextual evolutionary interpretation, not primary graph edges. (kacar2406foundationsforreconstructing pages 18-21, kacar2406foundationsforreconstructing pages 15-18)

References

1. (bryant2006prokaryoticphotosynthesisand pages 2-3): Donald A. Bryant and Niels-Ulrik Frigaard. Prokaryotic photosynthesis and phototrophy illuminated. Trends in microbiology, 14 11:488-96, Nov 2006. URL: https://doi.org/10.1016/j.tim.2006.09.001, doi:10.1016/j.tim.2006.09.001. This article has 813 citations and is from a domain leading peer-reviewed journal.

2. (peterson2023usinglightfor pages 1-5): Autumn Peterson, Carina Baskett, William C. Ratcliff, and Anthony Burnetti. Using light for energy: examining the evolution of phototrophic metabolism through synthetic construction. bioRxiv, Apr 2023. URL: https://doi.org/10.1101/2022.12.06.519405, doi:10.1101/2022.12.06.519405. This article has 8 citations.

3. (bryant2006prokaryoticphotosynthesisand pages 1-2): Donald A. Bryant and Niels-Ulrik Frigaard. Prokaryotic photosynthesis and phototrophy illuminated. Trends in microbiology, 14 11:488-96, Nov 2006. URL: https://doi.org/10.1016/j.tim.2006.09.001, doi:10.1016/j.tim.2006.09.001. This article has 813 citations and is from a domain leading peer-reviewed journal.

4. (kacar2406foundationsforreconstructing pages 15-18): Betul Kacar. Foundations for reconstructing early microbial life. Preprint, Jan 2406. URL: https://doi.org/10.48550/arxiv.2406.09354, doi:10.48550/arxiv.2406.09354. This article has 3 citations.

5. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

6. (davison2022engineeringarhodopsinbased pages 1-2): Paul A. Davison, Weiming Tu, Jiabao Xu, Simona Della Valle, Ian P. Thompson, C. Neil Hunter, and Wei E. Huang. Engineering a rhodopsin-based photo-electrosynthetic system in bacteria for co2 fixation. ACS Synthetic Biology, 11:3805-3816, Oct 2022. URL: https://doi.org/10.1021/acssynbio.2c00397, doi:10.1021/acssynbio.2c00397. This article has 36 citations and is from a domain leading peer-reviewed journal.

7. (tinguely2023diurnalcyclesdrive pages 9-10): Camille Tinguely, Mélanie Paulméry, Céline Terrettaz, and Diego Gonzalez. Diurnal cycles drive rhythmic physiology and promote survival in facultative phototrophic bacteria. ISME Communications, Sep 2023. URL: https://doi.org/10.1038/s43705-023-00334-5, doi:10.1038/s43705-023-00334-5. This article has 13 citations and is from a peer-reviewed journal.

8. (tu2024engineeringrhodopsinbasedartificial pages 102-105): Engineering rhodopsin-based artificial photosynthesis This article has 0 citations.

9. (kacar2406foundationsforreconstructing pages 18-21): Betul Kacar. Foundations for reconstructing early microbial life. Preprint, Jan 2406. URL: https://doi.org/10.48550/arxiv.2406.09354, doi:10.48550/arxiv.2406.09354. This article has 3 citations.

10. (li2023globallydistributedmyxococcota pages 4-5): Liuyang Li, Danyue Huang, Yaoxun Hu, Nicola M. Rudling, Daniel P. Canniffe, Fengping Wang, and Yinzhao Wang. Globally distributed myxococcota with photosynthesis gene clusters illuminate the origin and evolution of a potentially chimeric lifestyle. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42193-7, doi:10.1038/s41467-023-42193-7. This article has 78 citations and is from a highest quality peer-reviewed journal.