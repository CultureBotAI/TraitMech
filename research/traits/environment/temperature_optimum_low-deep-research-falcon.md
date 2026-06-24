---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:00:25.550281'
end_time: '2026-06-18T02:13:27.106672'
duration_seconds: 781.56
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum low
  trait_identifier: METPO:1000442
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ between approximately 10 and 22 \xB0C, characteristic of psychrophilic or psychrotolerant\
    \ physiology."
  parent_traits: METPO:1000304
  synonyms: Psychrophile, Psychrotolerant, TO_10_to_22
  evidence_summary: 'DOI:10.1038/sj.embor.7400662: growing well at temperatures around
    the freezing point of water (Psychrophile review supports low-but-not-freezing
    optima as the psychrophile / psychrotolerant category.)'
  causal_graph_summary: 'temperature_optimum_low_psychrotolerant_setpoint: 4 nodes,
    3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum low
- **METPO identifier:** METPO:1000442
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 10 and 22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, Psychrotolerant, TO_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports low-but-not-freezing optima as the psychrophile / psychrotolerant category.)
- **Existing causal graph summary:** temperature_optimum_low_psychrotolerant_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_low.yaml`.

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
- **Trait label:** temperature optimum low
- **METPO identifier:** METPO:1000442
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 10 and 22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, Psychrotolerant, TO_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports low-but-not-freezing optima as the psychrophile / psychrotolerant category.)
- **Existing causal graph summary:** temperature_optimum_low_psychrotolerant_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_low.yaml`.

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


## Research report: Microbial trait “temperature optimum low” (METPO:1000442)

### Executive scope summary (TraitMech curation)
**Target trait:** *temperature optimum low* (METPO:1000442) — best-growth ambient temperature between ~10 and 22 °C, corresponding largely to **psychrotolerant/psychrotrophic** microorganisms and overlapping the upper end of **psychrophiles**.

**Key boundary distinctions (operational definitions used in recent sources):**
- **Psychrophiles**: can grow at 0 °C, with optima near ~15 °C and (in one definition) **unable to grow at 20 °C**. (ramon2023ageneraloverview pages 1-2)
- **Psychrotolerant/psychrotrophs**: can grow at 4 °C but have **optimal growth temperatures above 20 °C**. (ramon2023ageneraloverview pages 1-2)
- Another widely used threshold scheme places psychrophiles at **optimum ≤15 °C** and **maximum ≤20 °C**, while psychrotolerant organisms can grow at low temperature but have **optima >15 °C**. (gao2023thegrowthlipid pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10)

**How METPO:1000442 fits:** the 10–22 °C optimum band captures many psychrotolerants (optimum often 15–20 °C) and a subset of “milder” psychrophiles depending on the definition and assay conditions. A key boundary case is a **mesophile that exhibits an acute cold-shock response** after a temperature downshift, which should not be conflated with a true low-temperature optimum phenotype. (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 7-8)

### 1) Key concepts and definitions (current understanding)

#### Phenotype definition and assay reality
“Temperature optimum” is an experimentally determined growth phenotype (e.g., max specific growth rate or biomass accumulation across temperatures). Mechanistically, **low-temperature optimum** reflects a set of adaptations that keep core cellular processes functional as temperature decreases: membrane dynamics, enzyme catalysis, nucleic-acid/translation homeostasis, cryoprotection, and oxidative-stress management. (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10)

**Boundary cases to distinguish in curation:**
- **Growth vs survival:** some organisms survive subzero conditions but do not grow; trait curation should focus on *best-growth temperature* rather than survival alone. (gao2023thegrowthlipid pages 1-2, purwar2024adaptationsofpsychrophilic pages 3-4)
- **Cold shock vs cold optimum:** cold-shock systems (CSPs, RNA helicases, chaperones) may be induced in mesophiles after a rapid downshift (<20 °C) without implying a low optimum. (purwar2024adaptationsofpsychrophilic pages 7-8)

### 2) Recent developments and latest research (prioritize 2023–2024)

#### Quantitative membrane-physics measurements (2024)
A key 2024 methodological advance is **quantitative measurement of bacterial membrane fluidity in vivo** using **TIR-FCS**, which provides diffusion coefficients for fluorescent membrane probes and time-resolved adaptation after temperature shifts. In *Bacillus subtilis*, a shift from **37 °C to 20 °C** roughly **halved** membrane fluidity at steady state and showed **recovery within ~30 min**. (barbotin2024quantificationofmembrane pages 1-3, barbotin2024quantificationofmembrane pages 10-11, barbotin2024quantificationofmembrane media 6a485ede, barbotin2024quantificationofmembrane media eb95dc53)

#### Refinement of DesK/DesR in vivo function (2024)
Work in 2024 highlighted that the canonical *B. subtilis* **DesK/DesR/des** thickness/fluidity feedback model may behave subtly in vivo; e.g., **des expression is activated only by mild temperature shocks** and membrane phase behavior can impair DesK thickness sensing. (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14)

#### Yeast comparative genomics (2023)
Comparative genomics of psychrophilic yeasts emphasizes **expanded fatty-acid desaturase gene repertoires** (Δ6/Δ9/Δ12/Δ15) enabling broad PUFA production and membrane fluidity maintenance, plus antifreeze/ice-binding proteins. (liu2023psychrophilicyeastsinsights pages 4-5, liu2023psychrophilicyeastsinsights pages 7-11)

#### Proteomics of a psychrotolerant microalga (2023)
A 2023 proteomics study on *Xanthonema hormidioides* (psychrotolerant microalga) provides a system-level view: optimum growth **15–20 °C**, multi-day lag at lower temperatures, and co-upregulation under low temperature of **ribosome-related proteins**, **antioxidant systems**, and **cold shock proteins**. (gao2023thegrowthlipid pages 1-2)

### 3) Current applications and real-world implementations

Mechanisms underlying low temperature optima are relevant to multiple applied domains:
- **Biotechnology/bioproducts from psychrotolerant microalgae:** *X. hormidioides* produced high biomass and very high lipid content (up to **56.63% of dry weight**) under tested conditions, relevant to biofuels and nutritional products; low temperature promoted unsaturated fatty-acid accumulation. (gao2023thegrowthlipid pages 1-2)
- **Cold-adapted molecules for biotech and environmental use:** Antarctic bacteria/psychrophiles are discussed as sources of cold-active enzymes and cold-adapted molecules (e.g., antifreeze proteins, EPS) with potential industrial and biotechnological applications. (ramasamy2023comprehensiveinsightson pages 3-4)
- **Membrane-physics assays for antimicrobial research:** quantitative fluidity assays (TIR-FCS) are positioned as enabling broader studies of membrane interactions with environmental stresses and membrane-acting antibiotics (a practical research implementation). (barbotin2024quantificationofmembrane pages 1-3)

### 4) Expert opinions and analysis (authoritative synthesis)

**Consensus mechanistic pillars** supported across 2023–2024 reviews and primary work:
1. **Homeoviscous adaptation**: temperature downshift rigidifies membranes, selecting for lipid remodeling (desaturation, branching, chain-length changes) to restore functional viscosity. (ramon2023ageneraloverview pages 1-2, sidarta2024lipidphaseseparation pages 1-2, barbotin2024quantificationofmembrane pages 10-11)
2. **Information-processing resilience**: cold impairs transcription/translation through RNA secondary structures and slowed kinetics; microbes deploy CSPs, RNA helicases (e.g., CsdA), and ribosome biogenesis factors (RbfA), plus chaperones to keep protein folding/assembly functional. (purwar2024adaptationsofpsychrophilic pages 7-8)
3. **Cryoprotection and ice management**: EPS, compatible solutes, and ice-binding/antifreeze proteins inhibit ice recrystallization and mitigate freeze–thaw and dehydration stresses, supporting growth near freezing and in cold niches. (purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 10-11, liu2023psychrophilicyeastsinsights pages 7-11)
4. **Metabolic rewiring under cold/ROS**: cold-associated increases in oxygen solubility/ROS and altered enzyme kinetics correspond to shifts away from some core energy pathways and toward alternative carbon/acetyl-CoA/glyoxylate and related routes, and use of storage polymers (PHAs) for redox/energy buffering. (purwar2024adaptationsofpsychrophilic pages 10-11)

### 5) Relevant statistics and data from recent studies

**Quantitative membrane fluidity (Bacillus subtilis, 2024):**
- Nile Red diffusion: **4.4 ± 0.3 µm²/s (37 °C)** vs **2.2 ± 0.2 µm²/s (20 °C)** (~2× decrease). (barbotin2024quantificationofmembrane pages 10-11, barbotin2024quantificationofmembrane media 6a485ede)
- Di4-ANEPPS diffusion: **1.9 ± 0.1 µm²/s (37 °C)** vs **0.9 ± 0.07 µm²/s (20 °C)** (~2.1× decrease). (barbotin2024quantificationofmembrane pages 10-11, barbotin2024quantificationofmembrane media 6a485ede)
- Adaptation kinetics: diffusion decreases immediately after downshift and increases over **~30 min**, consistent with rapid membrane adaptation. (barbotin2024quantificationofmembrane pages 10-11, barbotin2024quantificationofmembrane media eb95dc53)

**Psychrotolerant growth optimum and lipid statistics (Xanthonema hormidioides, 2023):**
- Optimum growth temperature range: **15–20 °C**. (gao2023thegrowthlipid pages 1-2)
- Maximum biomass concentration: **11.73 g/L at 20 °C**. (gao2023thegrowthlipid pages 1-2)
- Highest total lipid content: **56.63% of dry weight**. (gao2023thegrowthlipid pages 1-2)
- Specific fatty acids: palmitoleic acid **23.64%**, EPA **2.49%**, total fatty acid **41.14% of dry weight** (reported maxima). (gao2023thegrowthlipid pages 1-2)

---

## Candidate causal graph entities (nodes) grouped by type

### A. Environmental and experimental/assay factors
- **Temperature** (downshift; constant low temperature), including common lab contrasts (e.g., 37→20 °C). (barbotin2024quantificationofmembrane pages 1-3, barbotin2024quantificationofmembrane pages 10-11)
- **Freeze–thaw / ice presence** and cold + salinity contexts (relevant to ice-binding proteins, solutes, EPS). (purwar2024adaptationsofpsychrophilic pages 6-7)
- **Membrane-fluidity assays**: TIR-FCS diffusivity with Nile Red / Di4-ANEPPS; Laurdan GP (not quantitative here, but used to detect rigidification). (barbotin2024quantificationofmembrane pages 1-3, sidarta2024lipidphaseseparation pages 12-14)

### B. Cellular structures and properties
- Plasma/cytoplasmic membrane (GO:0005886) and emergent properties: **fluidity/viscosity**, **thickness**, phase behavior. (sidarta2024lipidphaseseparation pages 1-2, barbotin2024quantificationofmembrane pages 10-11)

### C. Genes/proteins/regulators
**Membrane sensing and lipid regulation**
- DesK (sensor histidine kinase; label-only grounding) and DesR (response regulator; label-only grounding). (sidarta2024lipidphaseseparation pages 1-2)
- Des (fatty-acid desaturase; label-only). (sidarta2024lipidphaseseparation pages 1-2)

**Cold-shock / RNA / ribosome modules**
- CSPs / CspA family (label-only). (purwar2024adaptationsofpsychrophilic pages 7-8)
- CsdA (DEAD-box RNA helicase; GO:0003724 candidate). (purwar2024adaptationsofpsychrophilic pages 7-8)
- RbfA (30S maturation; GO:0042254 candidate). (purwar2024adaptationsofpsychrophilic pages 7-8)
- PNPase and NusA (RNA processing/transcription-associated). (purwar2024adaptationsofpsychrophilic pages 7-8)

**Chaperones/protein quality control**
- GroEL(cpn60) / GroES(cpn10), DnaK (Hsp70 family), Clp proteases, trigger factor (TF). (purwar2024adaptationsofpsychrophilic pages 7-8)

### D. Pathways and processes
- Fatty-acid desaturation; PUFA biosynthesis (yeasts). (liu2023psychrophilicyeastsinsights pages 4-5)
- Ribosome biogenesis / translation homeostasis under cold stress. (purwar2024adaptationsofpsychrophilic pages 7-8)
- Oxidative-stress response / antioxidant systems. (gao2023thegrowthlipid pages 10-11, purwar2024adaptationsofpsychrophilic pages 10-11)
- Metabolic rewiring: acetyl-CoA metabolism, glyoxylate cycle, 2-methylcitrate / methylglyoxal-related cycles (label-only for exact pathway identifiers in this corpus). (purwar2024adaptationsofpsychrophilic pages 10-11, purwar2024adaptationsofpsychrophilic pages 8-10)
- PHA metabolism (PhaP/phasin; PHA depolymerase; label-only). (purwar2024adaptationsofpsychrophilic pages 10-11)

### E. Chemicals/metabolites/polymers
- Compatible solutes (CHEBI candidates): **glycine betaine, trehalose, glycerol, sucrose, mannitol, sorbitol**. (purwar2024adaptationsofpsychrophilic pages 10-11)
- Extracellular polymeric substances (EPS; label-only). (purwar2024adaptationsofpsychrophilic pages 8-10)
- Reactive oxygen species (CHEBI:reactive oxygen species). (purwar2024adaptationsofpsychrophilic pages 10-11)

### F. Ice-active proteins
- Antifreeze / ice-binding proteins (IBPs/AFPs), including DUF3494-containing proteins (domain label). (purwar2024adaptationsofpsychrophilic pages 6-7, liu2023psychrophilicyeastsinsights pages 7-11)

---

## Evidence-backed candidate causal edges (curation table)
The following table is designed to be directly mined into `data/traits/environment/temperature_optimum_low.yaml` after curator selection and normalization.

| Edge (subject–predicate–object) | Node type(s) | Suggested ontology grounding | Evidence snippet (verbatim short quote) | Reference (DOI, year, URL) | Notes for curation |
|---|---|---|---|---|---|
| temperature downshift (37→20 °C) → decreases → membrane fluidity | environment → cellular property/assay | ENVO:temperature; GO:0005886 plasma membrane; label: membrane fluidity | “steady-state membrane fluidity at 20°C was about half that measured at 37°C” (barbotin2024quantificationofmembrane pages 1-3) | 10.1101/2023.10.13.562271, 2024, https://doi.org/10.1101/2023.10.13.562271 | Strong quantitative assay evidence in *Bacillus subtilis*; assay-specific TIR-FCS readout, not a universal trait-defining edge. |
| Nile Red diffusion coefficient at 37 °C → is greater than → Nile Red diffusion coefficient at 20 °C | assay measurement | label: Nile Red; label: diffusion coefficient | “Nile Red diffusion coefficients of 4.4 ± 0.3 µm2/s at 37°C and 2.2 ± 0.2 µm2/s at 20°C” (barbotin2024quantificationofmembrane pages 10-11) | 10.1101/2023.10.13.562271, 2024, https://doi.org/10.1101/2023.10.13.562271 | Quantitative support for preceding edge; measurement node useful only if assay entities are modeled. |
| Di4-ANEPPS diffusion coefficient at 37 °C → is greater than → Di4-ANEPPS diffusion coefficient at 20 °C | assay measurement | label: Di4-ANEPPS; label: diffusion coefficient | “Di4-ANEPPS values of 1.9 ± 0.1 µm2/s at 37°C and 0.9 ± 0.07 µm2/s at 20°C” (barbotin2024quantificationofmembrane pages 10-11) | 10.1101/2023.10.13.562271, 2024, https://doi.org/10.1101/2023.10.13.562271 | Second quantitative assay support, same caveat as above. |
| membrane adaptation after cold shock → partially restores within ~30 min → membrane fluidity | biological process/assay | GO:0006629 lipid metabolic process; label: homeoviscous adaptation | “steady-state fluidity was recovered within ~30 minutes after the shift” (barbotin2024quantificationofmembrane pages 1-3) | 10.1101/2023.10.13.562271, 2024, https://doi.org/10.1101/2023.10.13.562271 | Captures dynamic adaptation rather than static trait; likely via lipid remodeling. |
| low temperature → rigidifies/thickens → membrane | environment → cellular property | ENVO:temperature; GO:0005886 plasma membrane | “A temperature decrease causes the membrane to rigidify and thicken” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | Strong mechanistic framing from *B. subtilis* DesK model; taxon-specific sensor system. |
| membrane rigidification/thickening → activates kinase state of → DesK | cellular property → protein | label: membrane thickness; UniProt/label: DesK histidine kinase | “which switches DesK to a kinase-dominant state” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | Canonical temperature-sensing mechanism in *B. subtilis*; curatable as taxon-specific exemplar. |
| DesK → phosphorylates/activates → DesR | protein → protein | label: DesK; label: DesR response regulator | “DesK dimerizes, autophosphorylates His188, and phosphorylates DesR” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | Specific two-component signaling edge; strong but *Bacillus*-specific. |
| phosphorylated DesR → activates transcription of → des | protein → gene | label: DesR; label: des | “Phosphorylated DesR activates the des promoter, increasing Des expression” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | Strong mechanistic edge for desaturase regulation. |
| Des desaturase expression → increases → fatty-acyl double bonds / membrane unsaturation | gene/protein → lipid state | label: des; GO:0016125 sterol metabolic?; label: fatty acid desaturation | “Des introduces double bonds into fatty acyl chains” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | Des-specific; grounding for bacterial Δ5 phospholipid desaturase may require external curation. |
| increased fatty-acyl unsaturation → increases → membrane fluidity | lipid state → cellular property | CHEBI:unsaturated fatty acid; label: membrane fluidity | “fluidizing the membrane and reducing bilayer thickness” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | Broadly generalizable homeoviscous adaptation edge. |
| restored membrane fluidity/thickness → switches off → des transcription via DesK phosphatase state | cellular property/protein/gene regulation | label: membrane fluidity; label: DesK; label: des | “this restores the phosphatase-dominant state of DesK and provides negative feedback to turn off des transcription” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | Negative-feedback edge; useful for causal graph loop but taxon-specific. |
| low temperature → induces → cold shock proteins (CSPs) | environment → protein family | GO:0009409 response to cold; label: CSP family/CspA family | “Cold shock proteins (CSPs) are ‘induced at high levels during temperature shifts below 20 °C’” (purwar2024adaptationsofpsychrophilic pages 7-8) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Broad review statement; useful generic edge though not tied to one gene across taxa. |
| CSPs → regulate/support → unsaturated fatty acid synthesis | protein family → pathway | label: CSP family; GO:0006636 unsaturated fatty acid biosynthetic process | “aid in cellular viability under cold stress conditions by regulating essential processes like unsaturated fatty acid synthesis” (purwar2024adaptationsofpsychrophilic pages 7-8) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Curate as uncertain/generalized; source is review-level and mechanism may vary by taxon. |
| CsdA RNA helicase → ensures → proper RNA structure and function during cold shock adaptation | protein → biological process | label: CsdA; GO:0003724 RNA helicase activity | “the DEAD-box RNA helicase CsdA, described as ‘crucial for cold shock adaptation, ensuring proper RNA structure and function’” (purwar2024adaptationsofpsychrophilic pages 7-8) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Good candidate node/edge; mostly from bacterial cold-shock literature, not necessarily low-optimum specialists only. |
| RbfA → required for → 30S ribosomal maturation under cold stress | protein → process/complex | label: RbfA; GO:0042254 ribosome biogenesis; label: 30S ribosomal subunit | “RbfA, required for 30S ribosomal maturation under cold stress” (purwar2024adaptationsofpsychrophilic pages 7-8) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Strong mechanistic ribosome-related edge; likely broadly conserved in bacteria. |
| PNPase and NusA → contribute to → RNA processing/transcription during cold adaptation | protein → process | label: PNPase; label: NusA; GO:0006396 RNA processing; GO:0006351 transcription, DNA-templated | “PNPase and NusA are also listed as RNA-processing/transcription factors linked to cold adaptation” (purwar2024adaptationsofpsychrophilic pages 7-8) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Review-derived and somewhat indirect; mark uncertain unless primary citation is added during curation. |
| low temperature → upregulates → molecular chaperones GroEL/GroES/DnaK/Clp/TF | environment → proteins | label: GroEL; label: GroES; label: DnaK; label: Clp; label: trigger factor | “Clps, TF, GroEL, DnaK, GroES) are ‘continuously overexpressed or upregulated at low temperatures to counteract cold denaturation’” (purwar2024adaptationsofpsychrophilic pages 7-8) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Broad but useful protective module edge. |
| GroEL/GroES expression from *Oleispira antarctica* → facilitates growth of → *E. coli* at 4 °C | protein → phenotype | label: GroEL/cpn60; label: GroES/cpn10; NCBITaxon:562 *E. coli* | “the expression of cpn60 (GroEL) and cpn10 (GroES) from the Antarctic bacterium Oleispira antarctica facilitates E. coli growth at 4 °C” (purwar2024adaptationsofpsychrophilic pages 7-8) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Heterologous-expression evidence; strong for sufficiency but not native-trait universality. |
| low temperature → promotes accumulation of → compatible solutes (glycine betaine, trehalose, glycerol, sucrose, mannitol, sorbitol) | environment → metabolites | CHEBI:glycine betaine; CHEBI:trehalose; CHEBI:glycerol; CHEBI:sucrose; CHEBI:mannitol; CHEBI:sorbitol | “Compatible solutes are explicitly listed: ‘glycine, betaine, glycerol, trehalose, sucrose, mannitol, and sorbitol’” (purwar2024adaptationsofpsychrophilic pages 10-11) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Strong review summary, broad across taxa. |
| compatible solutes → stabilize → proteins and membranes / lower freezing point | metabolites → processes/structures | same as above; GO:0006457 protein folding; GO:0005886 plasma membrane | “with functions in freezing-point depression and stabilization” (purwar2024adaptationsofpsychrophilic pages 10-11) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Good generic mechanistic edge for cryoprotection. |
| low temperature → increases → EPS production | environment → pathway/product | label: extracellular polymeric substances (EPS) | “EPS are described as cryoprotectants protecting against freeze–thaw” (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Review-level, taxon-general; useful candidate edge. |
| EPS → protects against → freeze–thaw stress | metabolite/polymer → stress tolerance | label: EPS; label: freeze–thaw protection | “EPS are described as cryoprotectants protecting against freeze–thaw” (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Could also be modeled as EPS → inhibits → ice recrystallization, but explicit wording here is freeze–thaw protection. |
| antifreeze/ice-binding proteins (IBPs/AFPs) → bind/inhibit growth of → ice crystals / ice recrystallization | protein → physical process | label: IBP/AFP; DUF3494 domain; label: ice recrystallization inhibition | “AFGPs... play crucial roles in protecting cells by binding to ice crystal surfaces” (purwar2024adaptationsofpsychrophilic pages 6-7) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Strong general cryoprotection edge; useful across fungi/algae/bacteria. |
| DUF3494-containing type I IBPs → contribute to → low-temperature adaptation | protein domain → phenotype | label: DUF3494; label: type I IBP | “Type I IBPs (DUF3494) reported in Antarctic green algae” (purwar2024adaptationsofpsychrophilic pages 6-7) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Domain grounding available; taxon examples are algal, so extrapolation to all microbes should be marked uncertain. |
| low temperature → increases → ROS / oxidative stress | environment → metabolite/stress process | CHEBI:reactive oxygen species; GO:0006979 response to oxidative stress | “Cold causes increased oxygen solubility and ROS” (purwar2024adaptationsofpsychrophilic pages 10-11) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Broadly plausible and review-supported. |
| ROS increase → depresses/downregulates → glycolysis, TCA, and electron transport chain | stress process → pathways | GO:glycolytic process; GO:TCA cycle; GO:electron transport chain | “often depress[es] pathways like glycolysis... the TCA, and the electron transport chain” (purwar2024adaptationsofpsychrophilic pages 10-11) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Captures metabolic pressure under cold/oxidative stress; indirect to trait. |
| low temperature → induces shift toward → glyoxylate cycle / acetyl-CoA metabolism / 2-methylcitrate pathway | environment → pathways | GO:glyoxylate cycle; CHEBI:acetyl-CoA; label: 2-methylcitrate pathway | “upregulation of acetyl-CoA metabolism”; “increased glyoxylate-cycle enzyme expression”; “upregulates the 2-methylcitrate pathway at 10°C” (purwar2024adaptationsofpsychrophilic pages 10-11) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Composite edge from multiple taxa; split into separate edges in YAML if needed. |
| glyoxylate cycle / acetyl-CoA / 2-methylcitrate pathway remodeling → supports → growth at low temperature | pathways → phenotype | same as above; METPO:1000442 | “driving metabolic reprogramming” and examples across psychrophiles/psychrotolerants (purwar2024adaptationsofpsychrophilic pages 10-11) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Supportive but indirect; causality is inferential from upregulation/association. Mark uncertain. |
| low temperature → upregulates → antioxidant enzymes and glutathione-linked protection | environment → proteins/process | label: antioxidant enzymes; CHEBI:glutathione; GO:response to oxidative stress | “Antioxidant enzymes are also up-regulated under low-temperature stress” (gao2023thegrowthlipid pages 10-11) | 10.1186/s13068-022-02249-0, 2023, https://doi.org/10.1186/s13068-022-02249-0 | Stronger in algal system; glutathione S-thiolation specifically mentioned in review context elsewhere, but not directly quoted here. |
| low temperature → upregulates → fatty acid desaturase genes (Δ6/Δ9/Δ12/Δ15) in psychrophilic yeasts | environment → genes | label: fatty acid desaturase delta6/delta9/delta12/delta15 | “fatty acid desaturase (FAD) genes (delta6, 9, 12, 15)” and “upregulated FAD genes at 15 °C, 0 °C, and −12 °C” (liu2023psychrophilicyeastsinsights pages 4-5) | 10.3390/genes14010158, 2023, https://doi.org/10.3390/genes14010158 | Good eukaryotic counterpart to bacterial Des system; psychrophilic yeast-specific. |
| fatty acid desaturase repertoire (Δ6/Δ9/Δ12/Δ15) → enables → PUFA biosynthesis (C18:1/C18:2/C18:3) | genes/pathway → metabolites | label: FADs; CHEBI:polyunsaturated fatty acid; CHEBI:alpha-linolenic acid | “enabling synthesis of C18:1, C18:2 and C18:3 PUFAs” (liu2023psychrophilicyeastsinsights pages 4-5) | 10.3390/genes14010158, 2023, https://doi.org/10.3390/genes14010158 | Strong pathway edge in yeasts. |
| PUFA biosynthesis → maintains → membrane fluidity at low temperature | pathway/metabolites → cellular property | CHEBI:polyunsaturated fatty acid; label: membrane fluidity | “maintain membrane fluidity” (liu2023psychrophilicyeastsinsights pages 4-5) | 10.3390/genes14010158, 2023, https://doi.org/10.3390/genes14010158 | Broad, well-supported mechanism; likely generalizable beyond yeasts. |


*Table: This table lists candidate causal edges for METPO:1000442 temperature optimum low, with ontology suggestions, evidence snippets, citations, and curation notes. It is designed to support TraitMech YAML curation by separating broadly generalizable mechanisms from taxon-specific or assay-specific claims.*

### Visual quantitative evidence (for curator verification)
- Table and figure crops supporting the quantitative membrane-fluidity edges: diffusion coefficients at 37 °C vs 20 °C and the ~30 min recovery time-course. (barbotin2024quantificationofmembrane media 6a485ede, barbotin2024quantificationofmembrane media eb95dc53)

---

## Warnings / curation cautions (what not to over-claim)
1. **Assay-specificity:** membrane “fluidity” depends on method (TIR-FCS diffusivity vs laurdan GP vs other probes). Quantitative edges should be tagged with assay context rather than treated as universal constants. (barbotin2024quantificationofmembrane pages 1-3, sidarta2024lipidphaseseparation pages 12-14)
2. **Taxon-specific regulators:** DesK/DesR/des is a well-studied Gram-positive model, but its presence and quantitative contribution to low-temperature optimum varies by lineage. Encode as a lineage-specific subgraph unless evidence supports broader generalization. (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14)
3. **Cold-shock vs low optimum:** Many edges (CSP induction, RNA helicases, chaperones) describe *responses to downshift below ~20 °C*, which can occur in mesophiles and do not alone define a low optimum. (purwar2024adaptationsofpsychrophilic pages 7-8)
4. **Metabolic rewiring edges often associative:** statements like pathway upregulation under cold should be curated as **putative/uncertain** unless linked to perturbation experiments showing growth causality. (purwar2024adaptationsofpsychrophilic pages 10-11, purwar2024adaptationsofpsychrophilic pages 8-10)

---

## DOI-first bibliography (publication date and URL)

1. **Barbotin A, et al.** “Quantification of membrane fluidity in bacteria using TIR-FCS.” *Biophysical Journal* (Oct 2024). DOI: **10.1101/2023.10.13.562271**. URL: https://doi.org/10.1101/2023.10.13.562271 (barbotin2024quantificationofmembrane pages 1-3, barbotin2024quantificationofmembrane pages 10-11)
2. **Sidarta M, et al.** “Lipid phase separation impairs membrane thickness sensing by the *Bacillus subtilis* sensor kinase DesK.” *Microbiology Spectrum* (Jun 2024). DOI: **10.1128/spectrum.03925-23**. URL: https://doi.org/10.1128/spectrum.03925-23 (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14)
3. **Purwar S, Srivastava S.** “Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.” *Applied Microbiology: Theory ＆ Technology* (Oct 2024). DOI: **10.37256/amtt.5220244537**. URL: https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 7-8, purwar2024adaptationsofpsychrophilic pages 10-11)
4. **Ramón A, et al.** “A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.” *Brazilian Journal of Microbiology* (Jul 2023). DOI: **10.1007/s42770-023-01057-4**. URL: https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2)
5. **Liu H, et al.** “Psychrophilic Yeasts: Insights into Their Adaptability to Extremely Cold Environments.” *Genes* (Jan 2023). DOI: **10.3390/genes14010158**. URL: https://doi.org/10.3390/genes14010158 (liu2023psychrophilicyeastsinsights pages 4-5, liu2023psychrophilicyeastsinsights pages 7-11)
6. **Gao B, et al.** “The growth, lipid accumulation and adaptation mechanism in response to variation of temperature and nitrogen supply in psychrotrophic filamentous microalga *Xanthonema hormidioides*.” *Biotechnology for Biofuels and Bioproducts* (Jan 2023). DOI: **10.1186/s13068-022-02249-0**. URL: https://doi.org/10.1186/s13068-022-02249-0 (gao2023thegrowthlipid pages 1-2, gao2023thegrowthlipid pages 10-11)
7. **Wu G, et al.** “Molecular Mechanisms of Lipid-Based Metabolic Adaptation Strategies in Response to Cold.” *Cells* (May 2023). DOI: **10.3390/cells12101353**. URL: https://doi.org/10.3390/cells12101353 (wu2023molecularmechanismsof pages 3-5)
8. **Ramasamy KP, et al.** “Comprehensive insights on environmental adaptation strategies in Antarctic bacteria and biotechnological applications of cold adapted molecules.” *Frontiers in Microbiology* (Jun 2023). DOI: **10.3389/fmicb.2023.1197797**. URL: https://doi.org/10.3389/fmicb.2023.1197797 (ramasamy2023comprehensiveinsightson pages 3-4)



References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (gao2023thegrowthlipid pages 1-2): Baoyan Gao, Jian Hong, Jiamin Chen, Hu Zhang, Ren Hu, and Chengwu Zhang. The growth, lipid accumulation and adaptation mechanism in response to variation of temperature and nitrogen supply in psychrotrophic filamentous microalga xanthonema hormidioides (xanthophyceae). Biotechnology for Biofuels and Bioproducts, Jan 2023. URL: https://doi.org/10.1186/s13068-022-02249-0, doi:10.1186/s13068-022-02249-0. This article has 79 citations and is from a domain leading peer-reviewed journal.

3. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

4. (purwar2024adaptationsofpsychrophilic pages 7-8): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

5. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

6. (barbotin2024quantificationofmembrane pages 1-3): Aurélien Barbotin, Cyrille Billaudeau, Erdinc Sezgin, and Rut Carballido-López. Quantification of membrane fluidity in bacteria using tir-fcs. Biophysical Journal, 123:2484-2495, Oct 2024. URL: https://doi.org/10.1101/2023.10.13.562271, doi:10.1101/2023.10.13.562271. This article has 19 citations and is from a domain leading peer-reviewed journal.

7. (barbotin2024quantificationofmembrane pages 10-11): Aurélien Barbotin, Cyrille Billaudeau, Erdinc Sezgin, and Rut Carballido-López. Quantification of membrane fluidity in bacteria using tir-fcs. Biophysical Journal, 123:2484-2495, Oct 2024. URL: https://doi.org/10.1101/2023.10.13.562271, doi:10.1101/2023.10.13.562271. This article has 19 citations and is from a domain leading peer-reviewed journal.

8. (barbotin2024quantificationofmembrane media 6a485ede): Aurélien Barbotin, Cyrille Billaudeau, Erdinc Sezgin, and Rut Carballido-López. Quantification of membrane fluidity in bacteria using tir-fcs. Biophysical Journal, 123:2484-2495, Oct 2024. URL: https://doi.org/10.1101/2023.10.13.562271, doi:10.1101/2023.10.13.562271. This article has 19 citations and is from a domain leading peer-reviewed journal.

9. (barbotin2024quantificationofmembrane media eb95dc53): Aurélien Barbotin, Cyrille Billaudeau, Erdinc Sezgin, and Rut Carballido-López. Quantification of membrane fluidity in bacteria using tir-fcs. Biophysical Journal, 123:2484-2495, Oct 2024. URL: https://doi.org/10.1101/2023.10.13.562271, doi:10.1101/2023.10.13.562271. This article has 19 citations and is from a domain leading peer-reviewed journal.

10. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

11. (sidarta2024lipidphaseseparation pages 12-14): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

12. (liu2023psychrophilicyeastsinsights pages 4-5): Haisheng Liu, Guiliang Zheng, Zhongwei Chen, Xiaoya Ding, Jinran Wu, Haili Zhang, and Shulei Jia. Psychrophilic yeasts: insights into their adaptability to extremely cold environments. Genes, 14:158, Jan 2023. URL: https://doi.org/10.3390/genes14010158, doi:10.3390/genes14010158. This article has 21 citations.

13. (liu2023psychrophilicyeastsinsights pages 7-11): Haisheng Liu, Guiliang Zheng, Zhongwei Chen, Xiaoya Ding, Jinran Wu, Haili Zhang, and Shulei Jia. Psychrophilic yeasts: insights into their adaptability to extremely cold environments. Genes, 14:158, Jan 2023. URL: https://doi.org/10.3390/genes14010158, doi:10.3390/genes14010158. This article has 21 citations.

14. (ramasamy2023comprehensiveinsightson pages 3-4): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 69 citations and is from a peer-reviewed journal.

15. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

16. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

17. (gao2023thegrowthlipid pages 10-11): Baoyan Gao, Jian Hong, Jiamin Chen, Hu Zhang, Ren Hu, and Chengwu Zhang. The growth, lipid accumulation and adaptation mechanism in response to variation of temperature and nitrogen supply in psychrotrophic filamentous microalga xanthonema hormidioides (xanthophyceae). Biotechnology for Biofuels and Bioproducts, Jan 2023. URL: https://doi.org/10.1186/s13068-022-02249-0, doi:10.1186/s13068-022-02249-0. This article has 79 citations and is from a domain leading peer-reviewed journal.

18. (wu2023molecularmechanismsof pages 3-5): Gang Wu, Ralf Baumeister, and Thomas Heimbucher. Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold. Cells, 12:1353, May 2023. URL: https://doi.org/10.3390/cells12101353, doi:10.3390/cells12101353. This article has 87 citations.