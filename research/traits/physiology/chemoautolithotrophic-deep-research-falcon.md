---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:44:24.887626'
end_time: '2026-06-18T11:04:19.197134'
duration_seconds: 1194.31
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemoautolithotrophic
  trait_identifier: METPO:1000634
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemoautolithotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism uses chemical oxidation of inorganic
    compounds as the energy source and carbon dioxide as the primary carbon source
    for biosynthesis.
  parent_traits: METPO:1000631
  synonyms: chemoautolithotroph
  evidence_summary: 'DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms
    or molecules (Review supports inorganic compound oxidation as lithotrophic energy
    metabolism.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview
    supports microbial carbon dioxide fixation pathways.) | DOI:10.1146/annurev.micro.55.1.485:
    Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation
    as a chemolithoautotrophic example.)'
  causal_graph_summary: 'chemoautolithotrophic_inorganic_energy_co2_fixation: 9 nodes,
    8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoautolithotrophic
- **METPO identifier:** METPO:1000634
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses chemical oxidation of inorganic compounds as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports microbial carbon dioxide fixation pathways.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as a chemolithoautotrophic example.)
- **Existing causal graph summary:** chemoautolithotrophic_inorganic_energy_co2_fixation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **chemoautolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautolithotrophic.yaml`.

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
- **Trait label:** chemoautolithotrophic
- **METPO identifier:** METPO:1000634
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses chemical oxidation of inorganic compounds as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports microbial carbon dioxide fixation pathways.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as a chemolithoautotrophic example.)
- **Existing causal graph summary:** chemoautolithotrophic_inorganic_energy_co2_fixation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **chemoautolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautolithotrophic.yaml`.

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


# Chemoautolithotrophic (METPO:1000634) — Curation-Focused Research Report (2023–2024 prioritized)

## 1) Scope summary (trait meaning, boundaries)

**Trait definition (for curation):** The microbial trait **chemoautolithotrophic** denotes a trophic type in which organisms **fix CO2 as their primary carbon source** and obtain energy by **oxidizing reduced inorganic compounds** (i.e., lithotrophic chemotrophy). This is explicitly stated for hydrothermal chemolithoautotrophs: they “convert CO2 to organic carbon using the energy produced by oxidizing these reduced compounds” (deng2023strategiesofchemolithoautotrophs pages 1-2). The trait therefore requires (i) a **CO2-fixation pathway** and (ii) **inorganic electron-donor oxidation** coupled to electron transport / respiration (deng2023strategiesofchemolithoautotrophs pages 1-2).

**Key distinctions for boundary setting:**
- **Lithotrophy vs organotrophy**: electron donors can be inorganic (lithotrophy) or organic (organotrophy); CO2 reduction coupled to oxidation of inorganic compounds (e.g., H2) is chemolithoautotrophy (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 8-10). This distinguishes chemoautolithotrophs from **chemo-organoheterotrophs**, which use organic carbon and energy from oxidation of organic compounds (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 8-10).
- **Chemoautotrophy vs chemoheterotrophy**: autotrophs use inorganic carbon (CO2), heterotrophs use organic carbon; chemotrophs derive energy from chemical reactions (yousavich2024effectsoftransient pages 21-25). 

**Boundary cases / “do not over-curate” warnings:**
- **AOA (ammonia-oxidizing archaea)** are often treated as classic chemolithoautotrophs, but multiple lines of evidence challenge strictness: genomic potential for organic substrate uptake and cases where bicarbonate uptake and/or nitrification-based autotrophic growth are not sufficient to explain abundances (cornell2024genomeencodedmetabolicpotential pages 15-18). These cases support annotating **facultative/mixotrophic potential** as *uncertain unless experimentally confirmed*.
- For nitrifiers, the literature summarizes that they are **chemolithoautotrophs** fixing inorganic CO2 with group-specific carbon-fixation pathways (AOB: CBB; AOA: 3HP/4HB; comammox: rTCA) (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2). This is reliable for nitrifier groups as a guild, but **taxon-by-taxon exceptions** (mixotrophy, inhibition artifacts) remain possible (cornell2024genomeencodedmetabolicpotential pages 15-18).

## 2) Key concepts & current understanding (mechanistic core)

### 2.1 Core mechanistic requirements
A minimal mechanistic model for chemoautolithotrophy that is consistent across systems:
1. **Inorganic electron donor oxidation** (e.g., NH3, Fe2+, H2, reduced sulfur species) supplies electrons (yousavich2024effectsoftransient pages 25-30, wang2024characterizethegrowth pages 1-2).
2. Electrons enter an **electron transport chain (ETC)** and flow to a **terminal electron acceptor (TEA)** (often O2, but alternative TEAs can occur) to generate proton motive force and ATP (wang2024characterizethegrowth pages 2-3, yousavich2024effectsoftransient pages 25-30).
3. **CO2 fixation** incorporates inorganic carbon into biomass via pathway-specific enzymes (e.g., Rubisco in CBB; reductive carboxylations in rTCA) (wang2024characterizethegrowth pages 1-2, ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2).

### 2.2 Canonical CO2 fixation pathways represented in 2023–2024 evidence
- **Calvin–Benson–Bassham (CBB) cycle**: explicitly used by the chemolithoautotroph *Acidithiobacillus ferrooxidans* to “fix atmospheric CO2 via the Calvin–Benson–Bassham (CBB) cycle” (wang2024characterizethegrowth pages 1-2).
- **Reverse TCA (rTCA) cycle**: described as active in hydrothermal incubations (“rTCA carbon fixation pathway was active in all of our incubation conditions”) (deng2023strategiesofchemolithoautotrophs pages 13-14). Also used by comammox Nitrospira per nitrifier-pathway comparisons (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2).
- **3-hydroxypropionate/4-hydroxybutyrate cycle (3HP/4HB)**: summarized as the CO2-fixation route used by AOA (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2).

### 2.3 Representative inorganic electron donors and acceptors (2023–2024 evidence)
- **Electron donors**:
  - **Fe2+** and **reduced inorganic sulfur compounds (RISCs)** for *A. ferrooxidans* chemoautotrophy (wang2024characterizethegrowth pages 1-2).
  - **H2** and reduced sulfur in hydrothermal systems (deng2023strategiesofchemolithoautotrophs pages 13-14).
  - **NH3/NH4+** for nitrification-driven chemoautotrophy (han2024unveilinguniquemicrobial pages 1-2, ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2).
  - Reduced sulfur intermediates such as **thiosulfate (S2O3 2−)** in mine tailings waters, with community partitioning by pathway and pH (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate pages 5-6).
- **Terminal electron acceptors (TEAs)**:
  - **O2** explicitly as electron acceptor for *A. ferrooxidans* during chemolithoautotrophy (wang2024characterizethegrowth pages 1-2) and commonly in oxic mine tailings waters (twible2024phandthiosulfate pages 1-2).
  - **Fe3+** can act as TEA for anaerobic survival in *A. ferrooxidans* with RISCs as donors (wang2024characterizethegrowth pages 1-2).
  - **Nitrate/nitrite** appear as electron acceptors in nitrogen cycling contexts (e.g., denitrification genes abundant in Antarctic soils/sediments) (han2024unveilinguniquemicrobial pages 1-2).

## 3) Recent developments & latest research (2023–2024)

### 3.1 Hydrothermal chemolithoautotroph adaptation and pathway partitioning (2023)
Deng et al. used **DNA-stable isotope probing + metagenomics** to identify active carbon-fixing chemolithoautotrophs across **temperature and pH gradients** in shallow hydrothermal vent fluids (published 2023-12; DOI:10.1186/s40168-023-01712-w) (deng2023strategiesofchemolithoautotrophs pages 1-2). Key mechanistic/curation-relevant findings include:
- **Cytochrome bd ubiquinol oxidase (cydA/B)** genes were most abundant at 65 °C and enriched in UH fractions (active fraction proxy), indicating adaptation of oxygen respiration to high temperature (deng2023strategiesofchemolithoautotrophs pages 10-13).
- **Sulfide:quinone oxidoreductase (sqr)** was the only abundant sulfur-oxidation gene at 65 °C; Nautiliales and Aquificae genomes lacked sox genes but contained sqr, consistent with high-temperature sulfide oxidation reliance (deng2023strategiesofchemolithoautotrophs pages 13-14).
- **Hydrogen oxidation potential** (Hyd1/Hyd5) increases at high temperature (65 °C), and hydrogen oxidation is described as yielding higher catabolic energy than sulfur oxidation in vents (deng2023strategiesofchemolithoautotrophs pages 13-14).

**Visual evidence for curation:** Deng et al. provide figures summarizing key genes for carbon fixation, sulfur oxidation, O2 utilization, and H2 utilization across conditions and taxa, suitable as supporting evidence snapshots (deng2023strategiesofchemolithoautotrophs media 7d8750d5, deng2023strategiesofchemolithoautotrophs media 61801b61).

### 3.2 Mine tailings: pH- and thiosulfate-dependent sulfur oxidation strategies (2024)
Twible et al. (published 2024-07-19; DOI:10.3389/fmicb.2024.1426584) analyzed mine tailings impoundment waters over **four years (2016–2019)** and identified **two pH-partitioned sulfur-oxidizer groups** with different pathway architectures and geochemical outcomes (twible2024phandthiosulfate pages 1-2). Curation-relevant results include:
- **Complete Sox (csox) dominant** SOB drive **acidity generation** and thiosulfate consumption at **pH ~5–6.5** (twible2024phandthiosulfate pages 1-2).
- At **pH ~6.5–8.5**, non-csox strategies (incomplete sox, rdsr, other reactions) are associated with higher thiosulfate and limited acidity generation (twible2024phandthiosulfate pages 1-2).
- **S4I pathway steps:** **tsdA** (thiosulfate→tetrathionate) is common, whereas **tetH** (needed to complete tetrathionate disproportionation) was largely restricted to Thiobacillus genomes in their dataset (twible2024phandthiosulfate pages 5-6).
- Quantitative community data: Halothiobacillus averaged **12.7 ± 20.5%** relative abundance in 16S data across tailings impoundment samples (twible2024phandthiosulfate pages 5-6).

### 3.3 Nitrification as a dominant autotrophic driver in cold oligotrophic environments (2024)
Han et al. (published 2024-04-25; DOI:10.1038/s41467-024-47392-4) used isotopes, MAGs, qPCR, and **13C-DNA SIP** to show nitrification’s centrality in Antarctic coastal soils/sediments:
- Isotope mass balance indicated **~96% of soil nitrate** originates from **biological nitrification** in the study areas (han2024unveilinguniquemicrobial pages 1-2).
- qPCR functional genes (nifH; amoA; nxrB) ranged **~10^2–10^4 copies ng−1 DNA** (han2024unveilinguniquemicrobial pages 1-2).
- **hao** was <10 copies ng−1 DNA, but authors attribute this to primer bias and/or absence in AOA genomes; thus hao is not a universally reliable marker across nitrifier groups (han2024unveilinguniquemicrobial pages 1-2).

### 3.4 Competitive/energetic framing: comammox vs AOA (2024)
Ghimire-Kafle et al. (published 2024-02-13; DOI:10.1128/aem.01698-23) provide a mechanistic comparison useful for interpreting niches:
- Nitrifiers are “chemolithoautotrophic microorganisms” and “all ammonia oxidizers are autotrophic microorganisms with unique pathways to fix inorganic CO2” (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2).
- Carbon fixation pathways differ: AOB (CBB), AOA (3HP/4HB), comammox (rTCA) (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2).
- In competition experiments, Nitrospira sp. BO4 (comammox) outcompeted an AOA; authors propose higher energy yield from complete nitrification and more efficient carbon fixation (rTCA) as explanation (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2).

## 4) Current applications and real-world implementations (with quantitative evidence where available)

### 4.1 Biomining / bioleaching (industrial)
- *Acidithiobacillus ferrooxidans* is an acidophilic chemolithoautotroph central to biomining/bioleaching (published 2024-11-??; DOI:10.3390/microorganisms12122407) (tonietti2024unveilingthebioleaching pages 1-2).
- A quantitative industry-scale statistic cited in Wang et al. (published 2024-03-15; DOI:10.3390/microorganisms12030590): bioleaching “is believed to account for **over 30% of global copper production** from low-grade copper ores” (wang2024characterizethegrowth pages 1-2).

### 4.2 Bioelectrochemical systems (electroautotrophy as adjacent capability)
Wang et al. compare chemoautotrophic vs electroautotrophic growth in *A. ferrooxidans*:
- Classical iron-oxidation ETC: Fe2+→Cyc2→Rus→Cyc1→Cox→O2; ~95% electrons flow downhill for ATP; ~5% uphill for reducing power (NAD(P)H) (wang2024characterizethegrowth pages 2-3).
- Under electroautotrophy, chemoautotrophy-essential genes are downregulated while **pilin/porin and direct electron transfer** genes are upregulated, with increased pili/EPS (wang2024characterizethegrowth pages 1-2).
This is relevant for TraitMech curation as a **related energy acquisition mode** that still supports CO2 fixation, but should not be conflated with canonical chemoautolithotrophy.

## 5) Candidate nodes for TraitMech causal graph (grouped + ontology grounding)

### 5.1 Pathways / modules
- CO2 fixation: **CBB cycle** (label; GO:0015977 carbon fixation), **rTCA** (label), **3HP/4HB** (label) (wang2024characterizethegrowth pages 1-2, deng2023strategiesofchemolithoautotrophs pages 13-14, ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2).
- Nitrification module: **ammonia oxidation**, **nitrite oxidation**, **complete nitrification (comammox)** (han2024unveilinguniquemicrobial pages 1-2, ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2).
- Sulfur oxidation modules: **sox pathway (complete/incomplete)**, **S4I pathway**, **reverse Dsr (rdsr; label)** (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate pages 5-6).
- Iron oxidation / acidophile ETC: **Cyc2–Rus–Cyc1–Cox** chain (wang2024characterizethegrowth pages 2-3).

### 5.2 Genes / proteins / complexes (examples useful as markers)
- CO2 fixation marker(s): **Rubisco** (Calvin cycle; label) (yousavich2024effectsoftransient pages 25-30).
- Nitrification: **amoA** (KEGG:K10944), **nxrB** (KEGG:K00370), **hao** (KEGG:K10535; caution) (han2024unveilinguniquemicrobial pages 1-2).
- Sulfur oxidation: **soxXA/soxYZ/soxB/soxCD** (labels), **sqr** (KEGG:K17218), **fccB** (label), **tsdA** (label), **tetH** (label) (twible2024phandthiosulfate pages 1-2, deng2023strategiesofchemolithoautotrophs pages 13-14, twible2024phandthiosulfate pages 5-6).
- Hydrogen oxidation: [NiFe]-hydrogenase maturation **hypA-F** (labels), hydrogenases Hyd1/Hyd5 (labels) (deng2023strategiesofchemolithoautotrophs pages 10-13, deng2023strategiesofchemolithoautotrophs pages 13-14).
- Terminal oxidases: **cytochrome bd ubiquinol oxidase cydA/B** (KEGG:K00425/K00426), **Cox aa3** (GO:0004129) (deng2023strategiesofchemolithoautotrophs pages 10-13, wang2024characterizethegrowth pages 2-3).
- Fe oxidation components: **Cyc2** (label), **rusticyanin (Rus)** (label), **Cyc1** (label) (wang2024characterizethegrowth pages 2-3, wang2024characterizethegrowth pages 1-2).

### 5.3 Chemicals (electron donors/acceptors; suggest CHEBI)
- Donors: CO2 (CHEBI:16526), H2 (CHEBI:18276), NH3/NH4+ (CHEBI:16134/28938), Fe2+ (CHEBI:29033), sulfide/H2S (CHEBI:16136), thiosulfate (CHEBI:30087). Evidence: (wang2024characterizethegrowth pages 1-2, ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2, yousavich2024effectsoftransient pages 25-30, twible2024phandthiosulfate pages 1-2).
- Acceptors: O2 (CHEBI:15379), nitrate/nitrite (CHEBI:17632/16301), Fe3+ (CHEBI:29034) (wang2024characterizethegrowth pages 1-2, han2024unveilinguniquemicrobial pages 1-2).

### 5.4 Environmental / experimental factors (suggest ENVO labels)
- Temperature regimes (e.g., **65 °C vs 45–30 °C**) and pH extremes (**pH 5.6 vs 2.2**) affecting hydrothermal chemolithoautotroph activity and gene repertoire (deng2023strategiesofchemolithoautotrophs pages 13-14).
- pH partitioning (pH ~5–6.5 vs ~6.5–8.5) shaping sulfur oxidation strategy and acidity generation in mine tailings waters (twible2024phandthiosulfate pages 1-2).
- Thiosulfate availability as a driver of dominant sulfur oxidation pathways (twible2024phandthiosulfate pages 1-2).

## 6) Evidence-backed candidate causal edges (table)

The following table is intended as a direct input to curate into a TraitMech-like YAML graph (subject–predicate–object, with evidence and uncertainty notes).

| Edge ID | Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet | Reference | DOI + URL | Notes |
|---|---|---|---|---|---|---|---|
| CHEMOAUTO-01 | chemoautolithotrophic trait (METPO:1000634) | requires | carbon dioxide fixation (GO:0015977) | “Chemolithoautotrophs convert CO2 to organic carbon” (deng2023strategiesofchemolithoautotrophs pages 1-2) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Core defining edge for the trait; broad, not taxon-specific. |
| CHEMOAUTO-02 | chemoautolithotrophic trait (METPO:1000634) | requires | oxidation of reduced inorganic compounds (label) | “using the energy produced by oxidizing these reduced compounds” (deng2023strategiesofchemolithoautotrophs pages 1-2) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Core defining edge; supports lithotrophic energy metabolism. |
| CHEMOAUTO-03 | Calvin–Benson–Bassham cycle (label) | enables | chemoautolithotrophic growth (METPO:1000634) | “fix atmospheric CO2 via the Calvin–Benson–Bassham (CBB) cycle” (wang2024characterizethegrowth pages 1-2) | Wang et al., 2024, *Microorganisms* | DOI:10.3390/microorganisms12030590; https://doi.org/10.3390/microorganisms12030590 | Strong for *Acidithiobacillus ferrooxidans*; generalizable to many bacterial chemoautotrophs with caution. |
| CHEMOAUTO-04 | reverse tricarboxylic acid cycle (label) | enables | carbon fixation (GO:0015977) | “the rTCA carbon fixation pathway was active in all of our incubation conditions” (deng2023strategiesofchemolithoautotrophs pages 13-14) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Strong for hydrothermal Epsilonproteobacteria/Aquificae-like taxa; taxon- and habitat-specific. |
| CHEMOAUTO-05 | 3-hydroxypropionate/4-hydroxybutyrate cycle (label) | enables | carbon fixation (GO:0015977) | “AOA use the 3-hydroxypropionate-4-hydroxybutyrate” (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2) | Ghimire-Kafle et al., 2024, *Applied and Environmental Microbiology* | DOI:10.1128/aem.01698-23; https://doi.org/10.1128/aem.01698-23 | Strong for ammonia-oxidizing archaea; not universal for all chemoautolithotrophs. |
| CHEMOAUTO-06 | ammonia monooxygenase subunit A (amoA; KEGG:K10944) | enables | ammonia oxidation (GO:0019430) | “genes (amoA and nxrB, encoding ammonia monooxygenase subunit A and nitrite oxidoreductase subunit B” (han2024unveilinguniquemicrobial pages 1-2) | Han et al., 2024, *Nature Communications* | DOI:10.1038/s41467-024-47392-4; https://doi.org/10.1038/s41467-024-47392-4 | Good marker-gene edge for nitrifying chemoautolithotrophs. |
| CHEMOAUTO-07 | nitrite oxidoreductase subunit B (nxrB; KEGG:K00370) | enables | nitrite oxidation to nitrate (GO:0019410) | “nxrB, encoding … nitrite oxidoreductase subunit B” (han2024unveilinguniquemicrobial pages 1-2) | Han et al., 2024, *Nature Communications* | DOI:10.1038/s41467-024-47392-4; https://doi.org/10.1038/s41467-024-47392-4 | Marker edge for nitrite oxidation and comammox/canonical NOB metabolism. |
| CHEMOAUTO-08 | ammonia oxidation (GO:0019430) | drives | autotrophic nitrification (label) | “comammox Nitrospira … role via 13C-DNA stable isotope probing” and “~96% of soil NO3− … is from nitrification” (han2024unveilinguniquemicrobial pages 1-2) | Han et al., 2024, *Nature Communications* | DOI:10.1038/s41467-024-47392-4; https://doi.org/10.1038/s41467-024-47392-4 | Strong ecological edge in coastal Antarctica; application to N-cycle budgets. |
| CHEMOAUTO-09 | hydroxylamine oxidoreductase (hao; KEGG:K10535) | associated_with | ammonia oxidation (GO:0019430) | “hao … detected at very low levels (<10 copies ng−1 DNA), attributed to primer bias … and the absence of the bacterial hao gene in the genomes of AOA” (han2024unveilinguniquemicrobial pages 1-2) | Han et al., 2024, *Nature Communications* | DOI:10.1038/s41467-024-47392-4; https://doi.org/10.1038/s41467-024-47392-4 | Curate with caution: assay caveat and archaeal exception; weak as a universal trait marker. |
| CHEMOAUTO-10 | ferrous iron oxidation (label) | enables | chemoautolithotrophic growth (METPO:1000634) | “derives energy from the aerobic oxidation of Fe2+” (wang2024characterizethegrowth pages 1-2) | Wang et al., 2024, *Microorganisms* | DOI:10.3390/microorganisms12030590; https://doi.org/10.3390/microorganisms12030590 | Strong for iron-oxidizing chemolithoautotrophs such as *A. ferrooxidans*. |
| CHEMOAUTO-11 | Cyc2 outer-membrane cytochrome c (label) | enables | Fe2+ oxidation (label) | “A. ferrooxidans oxidizes Fe2+ to Fe3+ with outer-membrane cytochrome c (Cyc2)” (wang2024characterizethegrowth pages 1-2, wang2024characterizethegrowth pages 2-3) | Wang et al., 2024, *Microorganisms* | DOI:10.3390/microorganisms12030590; https://doi.org/10.3390/microorganisms12030590 | Strong mechanistic edge; species-specific but widely cited model for acidophilic Fe oxidizers. |
| CHEMOAUTO-12 | rusticyanin (Rus; label) | associated_with | Fe2+ electron transfer chain (label) | “Electrons then flow toward rusticyanin (Rus)” (wang2024characterizethegrowth pages 1-2, wang2024characterizethegrowth pages 2-3) | Wang et al., 2024, *Microorganisms* | DOI:10.3390/microorganisms12030590; https://doi.org/10.3390/microorganisms12030590 | Intermediate ETC carrier in *A. ferrooxidans* Fe oxidation pathway. |
| CHEMOAUTO-13 | cytochrome c oxidase aa3-type (Cox; GO:0004129) | enables | oxygen respiration (GO:0006119) | “Fe2+ →Cyc2 … →Cox (aa3) →O2” (wang2024characterizethegrowth pages 2-3) | Wang et al., 2024, *Microorganisms* | DOI:10.3390/microorganisms12030590; https://doi.org/10.3390/microorganisms12030590 | Strong terminal-oxidase edge in iron-oxidizing acidophile model. |
| CHEMOAUTO-14 | oxygen (CHEBI:15379) | terminal_electron_acceptor_for | chemoautotrophic respiration (label) | “uses O2 as an electron acceptor” (wang2024characterizethegrowth pages 1-2); “under the primarily oxic conditions” (twible2024phandthiosulfate pages 1-2) | Wang et al., 2024, *Microorganisms*; Twible et al., 2024, *Frontiers in Microbiology* | DOI:10.3390/microorganisms12030590; https://doi.org/10.3390/microorganisms12030590 ; DOI:10.3389/fmicb.2024.1426584; https://doi.org/10.3389/fmicb.2024.1426584 | Broad but not universal; many chemoautolithotrophs also use nitrate or Fe3+ depending on taxa/conditions. |
| CHEMOAUTO-15 | ferric iron (CHEBI:29033) | terminal_electron_acceptor_for | anaerobic chemolithotrophy (label) | “under anaerobic conditions with Fe3+ as an electron acceptor and RISCs as an electron donor” (wang2024characterizethegrowth pages 1-2) | Wang et al., 2024, *Microorganisms* | DOI:10.3390/microorganisms12030590; https://doi.org/10.3390/microorganisms12030590 | Strong but species-specific to facultatively anaerobic *A. ferrooxidans*. |
| CHEMOAUTO-16 | molecular hydrogen oxidation (label) | enables | chemoautolithotrophic carbon fixation (GO:0015977) | “hydrogen was also a significant energy source for chemolithoautotrophs” and “Hyd1 and Hyd5, responsible for hydrogen oxidation” (deng2023strategiesofchemolithoautotrophs pages 13-14) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Strong in hydrothermal systems; especially Nautiliales/Campylobacterales. |
| CHEMOAUTO-17 | [NiFe]-hydrogenase maturation proteins HypABCDEF (label) | enables | hydrogenase activity (GO:0019825) | “genes encoding for the proteins that are involved in the maturation of [Ni–Fe] hydrogenases (hypA/B/C/D/E/F)” (deng2023strategiesofchemolithoautotrophs pages 10-13) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Good mechanistic support for hydrogen oxidation capacity; taxon/condition-specific. |
| CHEMOAUTO-18 | cytochrome bd ubiquinol oxidase (cydA/cydB; KEGG:K00425/K00426) | associated_with | high-temperature oxygen respiration (label) | “Genes encoding for the subunits of cytochrome bd ubiquinol oxidase (cydA/B) were the most abundant genes at WV 65 °C” (deng2023strategiesofchemolithoautotrophs pages 10-13) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Strong for high-temperature hydrothermal chemolithoautotrophs, especially Nautiliales. |
| CHEMOAUTO-19 | sulfide:quinone oxidoreductase (sqr; KEGG:K17218) | enables | sulfide oxidation (GO:0009407) | “sqr was the only gene that was abundant at WV 65 °C” and “Nautiliales only contained sqr” (deng2023strategiesofchemolithoautotrophs pages 13-14) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Strong for sulfide-oxidizing hydrothermal chemolithoautotrophs; especially high temperature. |
| CHEMOAUTO-20 | flavocytochrome c sulfide dehydrogenase subunit B (fccB; label) | associated_with | high-affinity sulfide oxidation (label) | “Fcc provides less energy through sulfide oxidation than SQR … [but] has a higher affinity for sulfide” (deng2023strategiesofchemolithoautotrophs pages 13-14) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Useful candidate node; edge is mechanistic but comparative/indirect. |
| CHEMOAUTO-21 | Sox pathway genes soxABCXYZ (label) | enables | thiosulfate oxidation (label) | “The sox pathway has seven structural genes … allowing this pathway to mediate S2O3 2− … dependent cytochrome c reduction” (twible2024phandthiosulfate pages 1-2) | Twible et al., 2024, *Frontiers in Microbiology* | DOI:10.3389/fmicb.2024.1426584; https://doi.org/10.3389/fmicb.2024.1426584 | Strong sulfur-oxidation edge; pathway may be complete (csox) or incomplete (isox). |
| CHEMOAUTO-22 | complete Sox pathway (csox; label) | drives | acidity generation (ENVO:01000324 candidate) | “Complete sox (csox) dominant SOB … drove acidity generation and S2O3 2− consumption at lower pH (pH ~5 to ~6.5)” (twible2024phandthiosulfate pages 1-2) | Twible et al., 2024, *Frontiers in Microbiology* | DOI:10.3389/fmicb.2024.1426584; https://doi.org/10.3389/fmicb.2024.1426584 | Strong environmental-process edge in mine tailings waters; not a universal property of all chemoautotrophs. |
| CHEMOAUTO-23 | thiosulfate dehydrogenase TsdA (label) | catalyzes | thiosulfate (CHEBI:30087) to tetrathionate (CHEBI:16337) conversion | “tsdA; S2O3 2− to S4O6 2−” (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate pages 5-6) | Twible et al., 2024, *Frontiers in Microbiology* | DOI:10.3389/fmicb.2024.1426584; https://doi.org/10.3389/fmicb.2024.1426584 | Strong, pathway-specific sulfur oxidation step. |
| CHEMOAUTO-24 | tetrathionate hydrolase TetH (label) | enables | completion of S4I pathway (label) | “tetH, which would be required for the completion of the S4I pathway” (twible2024phandthiosulfate pages 5-6) | Twible et al., 2024, *Frontiers in Microbiology* | DOI:10.3389/fmicb.2024.1426584; https://doi.org/10.3389/fmicb.2024.1426584 | Strong within sulfur-oxidizing mine-tailings taxa; prevalence limited mainly to *Thiobacillus* in this dataset. |
| CHEMOAUTO-25 | thiosulfate availability (CHEBI:30087) | influences | dominant sulfur oxidation pathway (label) | “S2O3 2− availability plays a key role in determining the dominant sulfur oxidation pathways” (twible2024phandthiosulfate pages 1-2) | Twible et al., 2024, *Frontiers in Microbiology* | DOI:10.3389/fmicb.2024.1426584; https://doi.org/10.3389/fmicb.2024.1426584 | Strong environmental driver edge for sulfur-oxidizing chemoautotroph communities. |
| CHEMOAUTO-26 | lower pH (~5–6.5) (ENVO candidate) | associated_with | csox-dominant sulfur oxidizers (label) | “csox dominant SOB … at lower pH (pH ~5 to ~6.5)” (twible2024phandthiosulfate pages 1-2) | Twible et al., 2024, *Frontiers in Microbiology* | DOI:10.3389/fmicb.2024.1426584; https://doi.org/10.3389/fmicb.2024.1426584 | Environmental association; useful for preference/condition nodes, not intrinsic trait definition. |
| CHEMOAUTO-27 | circumneutral pH (~6.5–8.5) (ENVO candidate) | associated_with | non-csox/rdsr sulfur oxidation strategies (label) | “At circumneutral pH … non-csox dominant SOB … associated with higher [S2O3 2−] and limited acidity generation” (twible2024phandthiosulfate pages 1-2) | Twible et al., 2024, *Frontiers in Microbiology* | DOI:10.3389/fmicb.2024.1426584; https://doi.org/10.3389/fmicb.2024.1426584 | Environmental association; community-level rather than organism-level edge. |
| CHEMOAUTO-28 | high temperature 65 °C (ENVO candidate) | increases | Nautiliales carbon fixation activity (label) | “Nautiliales exhibited high carbon fixation activity at high temperature (65 °C) and moderate acidity (pH = 5.6)” (deng2023strategiesofchemolithoautotrophs pages 13-14) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Strong but taxon- and environment-specific; do not generalize to all chemoautolithotrophs. |
| CHEMOAUTO-29 | extremely acidic pH 2.2 (ENVO candidate) | decreases | high-temperature tolerance of Nautiliales (label) | “extremely acidic condition (specifically at pH 2.2) restrained the high-temperature tolerances of Nautiliales” (deng2023strategiesofchemolithoautotrophs pages 13-14) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Clear environmental modulation edge; taxon-specific. |
| CHEMOAUTO-30 | reduced thiosulfate availability at >45 °C acidic conditions (label) | decreases | sox gene utility/acquisition (label) | “thiosulfate can easily hydrolyze … when the temperature exceeds 45 °C” and “absence of sox genes … may be due to the limited availability of thiosulfate under 65 °C” (deng2023strategiesofchemolithoautotrophs pages 13-14) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Evolutionary/ecological inference; curate as uncertain. |
| CHEMOAUTO-31 | NAD(H)-linked glutamate dehydrogenase GDH2 (label) | associated_with | enhanced rTCA cycle carbon fixation (label) | “NAD(H)-GDHs can generate 2-oxoglutarate … an important intermediate in the rTCA cycle … that may enhance the cycle” (deng2023strategiesofchemolithoautotrophs pages 13-14) | Deng et al., 2023, *Microbiome* | DOI:10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w | Mechanistic but somewhat inferential; strongest for Nautiliales at 65 °C. |
| CHEMOAUTO-32 | comammox Nitrospira (NCBITaxon:40117 candidate for genus) | enables | complete nitrification (NH3→NO2−→NO3−) (label) | “comammox completely oxidize ammonia to nitrate through nitrite” (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2) | Ghimire-Kafle et al., 2024, *Applied and Environmental Microbiology* | DOI:10.1128/aem.01698-23; https://doi.org/10.1128/aem.01698-23 | Strong for comammox lineage; important boundary within nitrifying chemoautotrophs. |
| CHEMOAUTO-33 | reductive TCA cycle (label) | associated_with | greater energetic efficiency than AOA carbon fixation pathway (label) | “more efficient carbon fixation pathway—the reductive tricarboxylic acid cycle” (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2) | Ghimire-Kafle et al., 2024, *Applied and Environmental Microbiology* | DOI:10.1128/aem.01698-23; https://doi.org/10.1128/aem.01698-23 | Comparative physiological edge explaining competition outcome; not a direct trait-defining edge. |
| CHEMOAUTO-34 | bioleaching by acidophilic chemolithoautotrophs (label) | drives | global copper production (>30%) (label) | “Bioleaching … is believed to account for over 30% of global copper production” (wang2024characterizethegrowth pages 1-2) | Wang et al., 2024, *Microorganisms* | DOI:10.3390/microorganisms12030590; https://doi.org/10.3390/microorganisms12030590 | Application edge; community/process level, not single-organism mechanism. |
| CHEMOAUTO-35 | *Acidithiobacillus ferrooxidans* (NCBITaxon:920) | drives | biomining/bioleaching of metal sulfides (label) | “has emerged as a key player in biomining and bioleaching technologies” (tonietti2024unveilingthebioleaching pages 1-2) | Tonietti et al., 2024, *Microorganisms* | DOI:10.3390/microorganisms12122407; https://doi.org/10.3390/microorganisms12122407 | Applied implementation edge; strong review support. |
| CHEMOAUTO-36 | chemolithoautotrophy (METPO:1000634) | distinct_from | chemo-organoheterotrophy (label) | “The reduction in CO2 is accomplished through … oxidation of inorganic compounds such as H2 (chemolithoautotrophy)” versus “glucose … chemo-organoheterotrophs” (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 8-10) | Fukala & Kučera, 2024, *Molecules* | DOI:10.3390/molecules29102293; https://doi.org/10.3390/molecules29102293 | Useful ontology/boundary edge; conceptual rather than organism-specific. |
| CHEMOAUTO-37 | ammonia-oxidizing archaea (AOA; label) | associated_with | boundary case between strict chemolithoautotrophy and mixotrophy (label) | “challenge the strictness of a chemolithoautotrophic metabolism” and “genes for the use and transport of alternative substrates” (cornell2024genomeencodedmetabolicpotential pages 15-18) | Cornell, 2024, *Genome-encoded metabolic potential of the Nitrosocosmicus genus and related AOA* | No DOI available in context; URL unavailable in context | Important warning edge: not all AOA should be treated as obligate strict chemoautolithotrophs without experimental confirmation. |


*Table: This table lists candidate subject–predicate–object causal edges for curating the chemoautolithotrophic trait, with evidence, citations, and curation notes. It emphasizes core defining mechanisms, taxon-specific pathways, environmental modulators, and practical application edges.*

## 7) Expert analysis (authoritative interpretations supported by sources)

1. **Trait is mechanistically composite**: chemoautolithotrophy is best represented as a conjunction of **(inorganic redox energy metabolism)** and **(CO2 fixation)** rather than any single pathway, because different taxa use different carbon fixation routes (CBB vs rTCA vs 3HP/4HB) while still satisfying the definition (deng2023strategiesofchemolithoautotrophs pages 1-2, ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2).
2. **Environmental control can switch dominant pathways and geochemical outcomes**: in mine tailings waters, pH and thiosulfate availability correspond to pathway partitioning (csox vs non-csox) and net acidity generation, implying that “chemoautolithotrophic sulfur oxidation” should be curated with explicit environmental context nodes (twible2024phandthiosulfate pages 1-2).
3. **Marker genes require context**: nitrification marker interpretation must consider primer bias and taxon differences (e.g., hao low counts; AOA lacking bacterial hao), so a chemoautolithotrophy trait graph should avoid hard requirements on hao presence (han2024unveilinguniquemicrobial pages 1-2).
4. **Boundary cases argue for cautious trait assignment**: AOA metabolic versatility and evidence inconsistent with strict autotrophic ammonia oxidation alone indicates that some lineages may be **facultative** or **mixotrophic**, requiring experimental confirmation (SIP, bicarbonate uptake, inhibitor tests) before curation as obligate chemoautolithotrophs (cornell2024genomeencodedmetabolicpotential pages 15-18).

## 8) Statistics / quantitative data (recent studies)

- **Nitrification contribution to nitrate pools:** ~**96%** of soil nitrate in two Antarctic study areas attributed to biological nitrification by isotope mass balance (Han et al., 2024-04-25) (han2024unveilinguniquemicrobial pages 1-2).
- **Functional gene abundances (Antarctica):** nifH and nitrification genes (amoA, nxrB) at **~10^2–10^4 copies ng−1 DNA**; hao **<10 copies ng−1 DNA** with caveats (han2024unveilinguniquemicrobial pages 1-2).
- **Mine tailings SOB ecology:** Halothiobacillus mean relative abundance **12.7 ± 20.5%** across samples; multi-year (2016–2019) dataset (Twible et al., 2024-07-19) (twible2024phandthiosulfate pages 5-6).
- **Industrial relevance:** bioleaching is believed to account for **>30% of global copper production** from low-grade copper ores (Wang et al., 2024-03-15) (wang2024characterizethegrowth pages 1-2).

## 9) Warnings / items not ready to curate

- **Do not curate “AOA = obligate chemolithoautotroph” as universal**: evidence indicates potential mixotrophy/alternative substrates and possible mismatch between abundance and purely autotrophic nitrification capacity (cornell2024genomeencodedmetabolicpotential pages 15-18).
- **Do not require hao as a trait marker**: low detection and primer bias; AOA lack bacterial hao gene (han2024unveilinguniquemicrobial pages 1-2).
- **Evolutionary inference edges** (e.g., sox gene acquisition driven by thiosulfate instability at high temperature) should be marked **uncertain/inferred**, not asserted as a direct causal mechanism without further corroboration (deng2023strategiesofchemolithoautotrophs pages 13-14).

---

# DOI-first bibliography (with publication dates and URLs)

1. Deng W, Zhao Z, Li Y, et al. **Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem**. *Microbiome*. **2023-12**. DOI: **10.1186/s40168-023-01712-w**. https://doi.org/10.1186/s40168-023-01712-w (deng2023strategiesofchemolithoautotrophs pages 1-2)
2. Twible LE, Whaley-Martin K, Chen L-X, et al. **pH and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments**. *Frontiers in Microbiology*. **2024-07-19**. DOI: **10.3389/fmicb.2024.1426584**. https://doi.org/10.3389/fmicb.2024.1426584 (twible2024phandthiosulfate pages 1-2)
3. Han P, Tang X, Koch H, et al. **Unveiling unique microbial nitrogen cycling and nitrification driver in coastal Antarctica**. *Nature Communications*. **2024-04-25** (Received 2023-11-26; Accepted 2024-04-01). DOI: **10.1038/s41467-024-47392-4**. https://doi.org/10.1038/s41467-024-47392-4 (han2024unveilinguniquemicrobial pages 1-2)
4. Ghimire-Kafle S, Weaver ME, Kimbrel MP, Bollmann A. **Competition between ammonia-oxidizing archaea and complete ammonia oxidizers from freshwater environments**. *Applied and Environmental Microbiology*. **2024-02-13**. DOI: **10.1128/aem.01698-23**. https://doi.org/10.1128/aem.01698-23 (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2)
5. Wang Q, Long H, Wang H, Lau Vetter MCY. **Characterize the Growth and Metabolism of Acidithiobacillus ferrooxidans under Electroautotrophic and Chemoautotrophic Conditions**. *Microorganisms*. **2024-03-15**. DOI: **10.3390/microorganisms12030590**. https://doi.org/10.3390/microorganisms12030590 (wang2024characterizethegrowth pages 1-2)
6. Tonietti L, Esposito M, Cascone M, et al. **Unveiling the Bioleaching Versatility of Acidithiobacillus ferrooxidans**. *Microorganisms*. **2024-11**. DOI: **10.3390/microorganisms12122407**. https://doi.org/10.3390/microorganisms12122407 (tonietti2024unveilingthebioleaching pages 1-2)
7. Fukala I, Kučera I. **Natural Polyhydroxyalkanoates—An Overview of Bacterial Production Methods**. *Molecules*. **2024-05**. DOI: **10.3390/molecules29102293**. https://doi.org/10.3390/molecules29102293 (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 8-10)

**Note:** Cornell (2024) “Genome-encoded metabolic potential of the Nitrosocosmicus genus and related ammonia-oxidizing archaea” is included for boundary-case discussion; DOI/URL were not available in the retrieved context and should be verified before curation use (cornell2024genomeencodedmetabolicpotential pages 15-18).


References

1. (deng2023strategiesofchemolithoautotrophs pages 1-2): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 14 citations and is from a highest quality peer-reviewed journal.

2. (fukala2024naturalpolyhydroxyalkanoates—anoverview pages 8-10): Ivo Fukala and Igor Kučera. Natural polyhydroxyalkanoates—an overview of bacterial production methods. Molecules, 29:2293, May 2024. URL: https://doi.org/10.3390/molecules29102293, doi:10.3390/molecules29102293. This article has 27 citations.

3. (yousavich2024effectsoftransient pages 21-25): DJ Yousavich. Effects of transient deoxygenation on sulfur cycling in aquatic systems. Unknown journal, 2024.

4. (cornell2024genomeencodedmetabolicpotential pages 15-18): C Cornell. Genome-encoded metabolic potential of the nitrosocosmicus genus and related ammonia-oxidizing archaea. Unknown journal, 2024.

5. (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2): Sabita Ghimire-Kafle, Matt E. Weaver, Madisen P. Kimbrel, and Annette Bollmann. Competition between ammonia-oxidizing archaea and complete ammonia oxidizers from freshwater environments. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01698-23, doi:10.1128/aem.01698-23. This article has 16 citations and is from a peer-reviewed journal.

6. (yousavich2024effectsoftransient pages 25-30): DJ Yousavich. Effects of transient deoxygenation on sulfur cycling in aquatic systems. Unknown journal, 2024.

7. (wang2024characterizethegrowth pages 1-2): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 9 citations.

8. (wang2024characterizethegrowth pages 2-3): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 9 citations.

9. (deng2023strategiesofchemolithoautotrophs pages 13-14): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 14 citations and is from a highest quality peer-reviewed journal.

10. (han2024unveilinguniquemicrobial pages 1-2): Ping Han, Xiufeng Tang, Hanna Koch, Xiyang Dong, Lijun Hou, Danhe Wang, Qian Zhao, Zhe Li, Min Liu, Sebastian Lücker, and Guitao Shi. Unveiling unique microbial nitrogen cycling and nitrification driver in coastal antarctica. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47392-4, doi:10.1038/s41467-024-47392-4. This article has 63 citations and is from a highest quality peer-reviewed journal.

11. (twible2024phandthiosulfate pages 1-2): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

12. (twible2024phandthiosulfate pages 5-6): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

13. (deng2023strategiesofchemolithoautotrophs pages 10-13): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 14 citations and is from a highest quality peer-reviewed journal.

14. (deng2023strategiesofchemolithoautotrophs media 7d8750d5): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 14 citations and is from a highest quality peer-reviewed journal.

15. (deng2023strategiesofchemolithoautotrophs media 61801b61): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 14 citations and is from a highest quality peer-reviewed journal.

16. (tonietti2024unveilingthebioleaching pages 1-2): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 44 citations.