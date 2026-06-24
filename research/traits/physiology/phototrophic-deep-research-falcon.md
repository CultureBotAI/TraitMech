---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:25:57.177570'
end_time: '2026-06-18T12:42:41.110916'
duration_seconds: 1003.93
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: phototrophic
  trait_identifier: METPO:1000660
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: phototrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type characterized by the use of light as the primary energy
    source for metabolic processes, regardless of carbon source.
  parent_traits: METPO:1000631
  synonyms: TT_phototroph, aerobic_anoxygenic_phototrophy, phototroph
  evidence_summary: 'DOI:10.3389/fmicb.2011.00165: use light as the energy source
    (Review supports light-driven ATP and reductant generation by phototrophic bacteria.)
    | DOI:10.1093/femsre/fuv032: bacteriochlorophyll-containing reaction centers (Review
    supports bacteriochlorophyll reaction centers in aerobic anoxygenic phototrophs.)'
  causal_graph_summary: 'phototrophic_light_energy_capture: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** phototrophic
- **METPO identifier:** METPO:1000660
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the primary energy source for metabolic processes, regardless of carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_phototroph, aerobic_anoxygenic_phototrophy, phototroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: use light as the energy source (Review supports light-driven ATP and reductant generation by phototrophic bacteria.) | DOI:10.1093/femsre/fuv032: bacteriochlorophyll-containing reaction centers (Review supports bacteriochlorophyll reaction centers in aerobic anoxygenic phototrophs.)
- **Existing causal graph summary:** phototrophic_light_energy_capture: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **phototrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/phototrophic.yaml`.

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
- **Trait label:** phototrophic
- **METPO identifier:** METPO:1000660
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the primary energy source for metabolic processes, regardless of carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_phototroph, aerobic_anoxygenic_phototrophy, phototroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: use light as the energy source (Review supports light-driven ATP and reductant generation by phototrophic bacteria.) | DOI:10.1093/femsre/fuv032: bacteriochlorophyll-containing reaction centers (Review supports bacteriochlorophyll reaction centers in aerobic anoxygenic phototrophs.)
- **Existing causal graph summary:** phototrophic_light_energy_capture: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **phototrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/phototrophic.yaml`.

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


## Research report: Microbial trait **phototrophic** (METPO:1000660)

### 1) Scope summary (trait meaning, boundaries, and operationalization)
**Trait definition (curation target).** *Phototrophic* organisms capture **light energy** and convert it into metabolically usable energy. In bacteria, this includes (i) **chlorophototrophy**, based on **photochemical reaction centers** with (bacterio)chlorophyll pigments, and (ii) **retinalophototrophy**, based on **rhodopsins** that pump ions across membranes. (tinguely2023diurnalcyclesdrive pages 1-2)

**Key boundary distinctions (avoid conflation during curation).**
- **Phototrophy vs. photoautotrophy:** many phototrophs are **photoheterotrophs** (light as energy source; organic carbon as carbon source). Aerobic anoxygenic phototrophs (AAP/AAnP) are explicitly described as relying on organic carbon and being unable to grow photoautotrophically because they lack carbon fixation pathways. (koblizek2015ecologyofaerobic pages 2-4, villenaalemany2024phenologyandecological pages 1-2)
- **Oxygenic vs. anoxygenic phototrophy:** oxygenic phototrophy uses **water as electron donor** and produces **O2**, whereas anoxygenic phototrophy uses other electron donors (commonly **H2S**, also H2 or Fe2+ in broader anoxygenic contexts) and does **not** evolve O2. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, tahon2016diversityofphototrophic pages 1-2, tinguely2023diurnalcyclesdrive pages 1-2)
- **Aerobic anoxygenic phototrophy (AAP/AAnP)** is a major boundary case: it operates under **aerobic conditions** yet is **anoxygenic** (no H2O splitting/O2 release), and is commonly **facultative photoheterotrophy** rather than primary production. (tinguely2023diurnalcyclesdrive pages 1-2, stojan2024ecologyofaerobic pages 1-2)

**Assay-observed trait indicators (practical curation hooks).**
- **Infrared epifluorescence microscopy** detects bacteriochlorophyll-a autofluorescence as an AAP readout; FISH‑IR adds taxonomic quantification. (stojan2024ecologyofaerobic pages 2-5, stojan2024ecologyofaerobic pages 1-2)
- **pufM marker gene**: widely used for AAP community tracking; pufM encodes a reaction-center subunit (M-chain) and is a standard metabarcoding locus. (stojan2024ecologyofaerobic pages 2-5, tahon2016diversityofphototrophic pages 1-2, villenaalemany2024phenologyandecological pages 1-2)

### 2) Key concepts and current mechanistic understanding
#### 2.1 Chlorophototrophy (reaction-center-based)
A canonical mechanistic chain (supported in purple sulfur bacteria) is: **photons → light-harvesting complexes → reaction center charge separation → quinone/cytochrome redox chain → proton motive force → ATP synthase**. (alarcon2024evidenceforautotrophic pages 1-2)

In AAP bacteria, **carotenoids** extend absorption into blue-green wavelengths, and excitation energy can be transferred to bacteriochlorophyll a for primary charge separation in the reaction center. (koblizek2015ecologyofaerobic pages 2-4)

#### 2.2 Retinalophototrophy (rhodopsin-based)
Facultative phototrophy can be mediated by **rhodopsins** that **pump ions through the membrane** (light-driven ion pumping), providing an energy-conservation mechanism distinct from reaction-center photochemistry. (tinguely2023diurnalcyclesdrive pages 1-2)

#### 2.3 Regulation and tradeoffs (oxygen + light, ROS)
A recurring mechanistic constraint for aerobic chlorophototrophs is that bacteriochlorophyll a biosynthesis/phototrophy can generate toxic byproducts such as **singlet oxygen** and other **reactive oxygen species** in the presence of oxygen and light; consequently, many aerobic anoxygenic phototrophs strictly regulate bacteriochlorophyll production and may limit synthesis to dark phases. (tinguely2023diurnalcyclesdrive pages 1-2)

Consistent with this, a foundational review notes that **“BChl a synthesis in most AAP species is inhibited by light.”** (koblizek2015ecologyofaerobic pages 2-4)

### 3) Recent developments and latest research (prioritizing 2023–2024)
#### 3.1 Diurnal biology and fitness effects of facultative phototrophy (2023)
A 2023 ISME Communications study in a Porphyrobacter model links **fitness/survival** under nutrient limitation to **functional reaction centers**, and connects light regime (dark–light alternation) to physiology and transcriptional rhythms, framing facultative phototrophy as an energy-sparing strategy under scarcity. (tinguely2023diurnalcyclesdrive pages 1-2)

#### 3.2 Freshwater phenology of AAPs over multi-year time series (2024)
A 2024 Microbiome study performed biweekly sampling across **3 years** (215 samples) and used pufM metabarcoding with an expanded reference database (3633 sequences) to show strong seasonal succession: **“less than 2% of AAP species detected during the whole year”** and a spring maximum following phytoplankton blooms; in lakes, AAP can reach **“up to 22% of bacteria”** during spring. (villenaalemany2024phenologyandecological pages 1-2)

#### 3.3 Experimental manipulation of carbon availability and light (2024)
A 2024 FEMS Microbiology Ecology community-manipulation experiment in a freshwater lake used **dark vs infrared light** incubations and carbon manipulations with measured DOC. In June control conditions, AAP growth in IR was ~2× faster than in dark (0.66 ± 0.02 d−1 vs 0.37 ± 0.07 d−1) with end abundances 5.57 ± 0.66 ×10^5 vs 3.43 ± 0.28 ×10^5 cells mL−1; AAP contribution rose to 26.6 ± 1.5% in IR vs 15.9 ± 1.2% in dark. (piwosz2024responseofaerobic pages 3-4)

#### 3.4 Marine AAP community ecology at genus-level resolution (2024)
A 2024 Environmental Microbiome study combining pufM metabarcoding and FISH‑IR reported pronounced seasonality in the Adriatic Sea with **maximum average abundances in spring 2.136 ± 0.081 ×10^4 cells mL−1** and minimum in summer 0.86 ×10^4 cells mL−1, and group-level contributions (e.g., Roseobacter clade mean contribution 37.66%). (stojan2024ecologyofaerobic pages 1-2)

#### 3.5 New electron donor contexts for anoxygenic phototrophy (2024)
A 2024 Applied and Environmental Microbiology study demonstrated **autotrophic growth** of the purple sulfur bacterium *Allochromatium vinosum* using **pyrite (FeS2) as electron and sulfur source**, and reported strong expression shifts including “up to ~200-fold upregulation” of cytochrome genes and “extensive downregulation” of LH/RC genes, suggesting electron-source–dependent control of photosynthetic activity. (alarcon2024evidenceforautotrophic pages 1-2)

### 4) Current applications and real-world implementations
**Environmental management / biotechnology (anoxygenic sulfur phototrophs).** A 2024 review emphasizes green sulfur bacteria (GSB) and related anoxygenic phototrophs for **H2S detoxification** in anoxic environments; it notes elemental sulfur production as a separable product and discusses application possibilities in environmental management and biotechnology. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)

**Ecological modeling and carbon cycling.** Long-term freshwater AAP phenology is integrated with ecological models (e.g., PEG framework) to contextualize AAP roles in recycling dissolved organic matter released during spring phytoplankton blooms. (villenaalemany2024phenologyandecological pages 1-2)

**Aquatic monitoring and microbial oceanography/limnology.** AAP detection is operationalized using **BChl a infrared autofluorescence microscopy** and **pufM** metabarcoding (including expanded pufM reference databases), enabling high-throughput monitoring of phototrophic functional groups in situ. (stojan2024ecologyofaerobic pages 2-5, villenaalemany2024phenologyandecological pages 1-2)

### 5) Relevant statistics and quantitative data (recent studies)
- **Marine seasonal abundance (Adriatic Sea):** spring maximum **2.136 ± 0.081 ×10^4 cells mL−1**; summer minimum **0.86 ×10^4 cells mL−1**. (stojan2024ecologyofaerobic pages 1-2)
- **Freshwater relative abundance:** AAP “may account for up to **22% of bacteria**” during spring peaks. (villenaalemany2024phenologyandecological pages 1-2)
- **Experimental IR-light stimulation (freshwater community incubations):** in June control, AAP growth rate **0.66 ± 0.02 d−1 (IR)** vs **0.37 ± 0.07 d−1 (dark)**; end abundance **5.57 ± 0.66 ×10^5** vs **3.43 ± 0.28 ×10^5 cells mL−1**; contribution **26.6 ± 1.5%** vs **15.9 ± 1.2%**. (piwosz2024responseofaerobic pages 3-4)
- **Depth distribution:** AAP are concentrated in the euphotic zone, with depth profiles summarized in a FEMS Microbiology Reviews figure showing AAP abundance (10^3 cells mL−1) versus depth alongside chlorophyll a and temperature profiles. (koblizek2015ecologyofaerobic media 84704fb5, koblizek2015ecologyofaerobic pages 9-11)

### 6) Candidate causal-graph nodes (grouped by type)
| Group | Node label | Brief definition/role | Suggested CURIE grounding | Primary supporting source | DOI URL |
|---|---|---|---|---|---|
| A. Phenotypes/subtraits | phototrophic | Broad trait: use of light as a primary energy source for metabolism | METPO:1000660 | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| A. Phenotypes/subtraits | chlorophototrophy | Phototrophy based on photochemical reaction centers containing chlorophylls or bacteriochlorophylls | GO:0015979 (broadly related) | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| A. Phenotypes/subtraits | retinalophototrophy | Phototrophy using rhodopsins to pump ions across membranes | label-only candidate | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| A. Phenotypes/subtraits | aerobic anoxygenic phototrophy (AAP/AAnP) | Aerobic light-powered photoheterotrophy without water splitting or oxygen release | label-only candidate | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| A. Phenotypes/subtraits | oxygenic photosynthesis | Cyanobacterial phototrophy using water as electron donor and releasing O2 | GO:0015979 | Kushkevych 2024 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | https://doi.org/10.3389/fmicb.2024.1417714 |
| A. Phenotypes/subtraits | anoxygenic photosynthesis | Phototrophy using reduced electron donors such as H2S, H2, or Fe2+ rather than water | GO:0015979 (broadly related) | Tahon 2016 (tahon2016diversityofphototrophic pages 1-2) | https://doi.org/10.3389/fmicb.2016.02026 |
| A. Phenotypes/subtraits | purple sulfur bacterial phototrophy | Sulfur-oxidizing anoxygenic phototrophy typical of purple sulfur bacteria | NCBITaxon:label-only Chromatiaceae-related | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| A. Phenotypes/subtraits | green sulfur bacterial phototrophy | Low-light adapted sulfur-based anoxygenic phototrophy with chlorosomes and CO2 fixation via rTCA | NCBITaxon:1090 (family Chlorobiaceae) | Kushkevych 2024 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | https://doi.org/10.3389/fmicb.2024.1417714 |
| B. Complexes/structures | type II photochemical reaction center | Chlorophototrophic reaction center whose M subunit is marked by pufM | label-only candidate | Tahon 2016 (tahon2016diversityofphototrophic pages 1-2) | https://doi.org/10.3389/fmicb.2016.02026 |
| B. Complexes/structures | reaction center (RC) | Central photochemical complex where charge separation occurs | GO:reaction center label-only | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| B. Complexes/structures | light-harvesting complex LH1 | Antenna complex encoded in part by pufA/pufB apoproteins | label-only candidate | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| B. Complexes/structures | light-harvesting complex LH2 | Accessory antenna complex encoded by puc gene pairs in purple bacteria | label-only candidate | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| B. Complexes/structures | chlorosome | Lipid-monolayer light-collecting antenna structure of green sulfur bacteria | GO:0030084 | Kushkevych 2024 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | https://doi.org/10.3389/fmicb.2024.1417714 |
| B. Complexes/structures | ATP synthase complex | Uses proton motive force generated by phototrophic electron transport to make ATP | GO:0045263 | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| B. Complexes/structures | intracytoplasmic membrane | Membrane location of LH complexes and RCs in purple sulfur bacteria | GO:0019866 (membrane, broad) | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| C. Genes/markers | pufM | Marker gene encoding the M-chain/subunit of the type II photosynthetic reaction center | gene:pufM | Stojan 2024 (stojan2024ecologyofaerobic pages 2-5) | https://doi.org/10.1186/s40793-024-00573-6 |
| C. Genes/markers | pufL | Reaction-center subunit gene in purple sulfur bacteria | gene:pufL | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| C. Genes/markers | pufC | Reaction-center subunit gene in purple sulfur bacteria | gene:pufC | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| C. Genes/markers | pufA | LH1 apoprotein gene | gene:pufA | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| C. Genes/markers | pufB | LH1 apoprotein gene | gene:pufB | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| C. Genes/markers | puc gene pairs | Genes encoding LH2 α/β apoproteins | gene:puc | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| C. Genes/markers | bchL | (Bacterio)chlorophyll biosynthesis gene; part of DPOR-related machinery | gene:bchL | Tahon 2016 (tahon2016diversityofphototrophic pages 1-2) | https://doi.org/10.3389/fmicb.2016.02026 |
| C. Genes/markers | chlL | Chlorophyll biosynthesis gene discussed with bchL in DPOR context | gene:chlL | Tahon 2016 (tahon2016diversityofphototrophic pages 1-2) | https://doi.org/10.3389/fmicb.2016.02026 |
| C. Genes/markers | bchX | Marker from bacteriochlorophyll branch; part of COR-related system | gene:bchX | Tahon 2016 (tahon2016diversityofphototrophic pages 1-2) | https://doi.org/10.3389/fmicb.2016.02026 |
| C. Genes/markers | bchXYZ | Genes encoding chlorin oxidoreductase for bacteriochlorophyllide formation | gene:bchXYZ | Tahon 2016 (tahon2016diversityofphototrophic pages 1-2) | https://doi.org/10.3389/fmicb.2016.02026 |
| D. Pigments/cofactors/chemicals | bacteriochlorophyll a | Main light-harvesting pigment in AAP and many anoxygenic phototrophs | CHEBI:28133 | Koblížek 2015 (koblizek2015ecologyofaerobic pages 2-4) | https://doi.org/10.1093/femsre/fuv032 |
| D. Pigments/cofactors/chemicals | chlorophyll | Pigment basis of chlorophototrophy and oxygenic photosynthesis | CHEBI:28966 | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| D. Pigments/cofactors/chemicals | carotenoids | Auxiliary pigments for blue-green absorption extension and photoprotection | CHEBI:23044 | Koblížek 2015 (koblizek2015ecologyofaerobic pages 2-4) | https://doi.org/10.1093/femsre/fuv032 |
| D. Pigments/cofactors/chemicals | retinal | Rhodopsin chromophore/cofactor in retinalophototrophy | CHEBI:30527 | pqac-00000003 | https://doi.org/10.48550/arxiv.2406.09354 |
| D. Pigments/cofactors/chemicals | light | Primary energy source for phototrophic metabolism | CHEBI:24866 | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| D. Pigments/cofactors/chemicals | hydrogen sulfide | Major electron donor in sulfur-based anoxygenic photosynthesis | CHEBI:16136 | Kushkevych 2024 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | https://doi.org/10.3389/fmicb.2024.1417714 |
| D. Pigments/cofactors/chemicals | water | Electron donor in oxygenic photosynthesis | CHEBI:15377 | Kushkevych 2024 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | https://doi.org/10.3389/fmicb.2024.1417714 |
| D. Pigments/cofactors/chemicals | dioxygen | Product of oxygenic photosynthesis and inhibitor context for some anoxygenic pigment synthesis | CHEBI:15379 | Kushkevych 2024 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | https://doi.org/10.3389/fmicb.2024.1417714 |
| D. Pigments/cofactors/chemicals | elemental sulfur | Oxidation product of H2S in green sulfur bacteria | CHEBI:26806 | Kushkevych 2024 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | https://doi.org/10.3389/fmicb.2024.1417714 |
| D. Pigments/cofactors/chemicals | quinone/quinol | Electron carriers in purple sulfur bacterial photosynthetic electron transport | CHEBI:16389 / label-only quinol | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| D. Pigments/cofactors/chemicals | cytochromes b/c and c | Electron transfer proteins in phototrophic redox chain | GO:0020037 (heme binding, broad) | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| D. Pigments/cofactors/chemicals | proton motive force | Electrochemical gradient linking electron transport to ATP synthesis | GO:0015992 | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| D. Pigments/cofactors/chemicals | ATP | Energy currency produced downstream of phototrophic electron transport | CHEBI:15422 | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| D. Pigments/cofactors/chemicals | singlet oxygen | Toxic ROS associated with BChl biosynthesis under light and oxygen | CHEBI:35697 | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| D. Pigments/cofactors/chemicals | reactive oxygen species | Toxic byproducts constraining oxic phototrophic pigment biosynthesis | CHEBI:26523 | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| D. Pigments/cofactors/chemicals | carbon dioxide | Carbon source for GSB via reverse TCA; limited co-assimilation in AAP | CHEBI:16526 | Kushkevych 2024 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | https://doi.org/10.3389/fmicb.2024.1417714 |
| D. Pigments/cofactors/chemicals | pyrite | Electron and sulfur source for Allochromatium vinosum in recent study | CHEBI:46661 | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| D. Pigments/cofactors/chemicals | acetate | Low-energy carbon source tested in AAP physiology experiments | CHEBI:30089 | Piwosz 2024 (piwosz2024responseofaerobic pages 2-3, piwosz2024responseofaerobic pages 3-4) | https://doi.org/10.1093/femsec/fiae090 |
| D. Pigments/cofactors/chemicals | lignin | Recalcitrant carbon source tested in AAP physiology experiments | CHEBI:6457 | Piwosz 2024 (piwosz2024responseofaerobic pages 2-3, piwosz2024responseofaerobic pages 3-4) | https://doi.org/10.1093/femsec/fiae090 |
| E. Pathways/processes | photosynthetic light harvesting | Antenna-mediated capture and transfer of excitation energy to RCs | GO:0009765 | Koblížek 2015 (koblizek2015ecologyofaerobic pages 2-4) | https://doi.org/10.1093/femsre/fuv032 |
| E. Pathways/processes | primary charge separation | Initial photochemical event in the reaction center | label-only candidate | Koblížek 2015 (koblizek2015ecologyofaerobic pages 2-4) | https://doi.org/10.1093/femsre/fuv032 |
| E. Pathways/processes | photosynthetic electron transport | RC-driven redox reactions involving quinones and cytochromes | GO:0009773 / label-only broad | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| E. Pathways/processes | photophosphorylation | ATP generation from light-driven electron transport in AAP | GO:0009774 | Stojan 2024 (stojan2024ecologyofaerobic pages 1-2) | https://doi.org/10.1186/s40793-024-00573-6 |
| E. Pathways/processes | bacteriochlorophyll biosynthesis | Synthesis of BChl pigments needed for chlorophototrophy | GO:0015995 (chlorophyll biosynthetic process, related) | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| E. Pathways/processes | DPOR-mediated protochlorophyllide reduction | Key step in (bacterio)chlorophyll synthesis involving bchL/chlL | label-only candidate | Tahon 2016 (tahon2016diversityofphototrophic pages 1-2) | https://doi.org/10.3389/fmicb.2016.02026 |
| E. Pathways/processes | chlorin oxidoreductase reaction | Reduction of chlorin to bacteriochlorophyllide by bchXYZ | EC:label-only / MetaCyc label-only | Tahon 2016 (tahon2016diversityofphototrophic pages 1-2) | https://doi.org/10.3389/fmicb.2016.02026 |
| E. Pathways/processes | reverse tricarboxylic acid cycle | CO2 fixation route in green sulfur bacteria | KEGG:reverse TCA cycle / MetaCyc:rTCA | Kushkevych 2024 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | https://doi.org/10.3389/fmicb.2024.1417714 |
| E. Pathways/processes | anaplerotic carboxylation | Limited light-linked CO2 incorporation in AAP | label-only candidate | Koblížek 2015 (koblizek2015ecologyofaerobic pages 2-4) | https://doi.org/10.1093/femsre/fuv032 |
| E. Pathways/processes | rhodopsin-based ion pumping | Membrane ion transport powered by rhodopsins | GO:0006811 (broadly related) | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| E. Pathways/processes | sulfur oxidation during phototrophy | Oxidation of reduced sulfur compounds supporting anoxygenic photosynthesis | GO:0000104 (sulfur compound metabolic process, broad) | Kushkevych 2024 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | https://doi.org/10.3389/fmicb.2024.1417714 |
| F. Environmental/exposure factors | oxygen / oxic conditions | Key boundary factor; AAP are aerobic, but oxygen can repress or complicate some anoxygenic pigment biosynthesis | ENVO:09200014 / CHEBI:15379 | Koblížek 2015 (koblizek2015ecologyofaerobic pages 2-4) | https://doi.org/10.1093/femsre/fuv032 |
| F. Environmental/exposure factors | anoxic conditions | Required for phototrophic growth in purple sulfur bacteria | ENVO:label-only anoxic environment | Alarcon 2024 (alarcon2024evidenceforautotrophic pages 1-2) | https://doi.org/10.1128/aem.00863-24 |
| F. Environmental/exposure factors | dark phase | Condition permitting BChl synthesis in many AAP bacteria | ENVO:label-only dark period | Tinguely 2023 (tinguely2023diurnalcyclesdrive pages 1-2) | https://doi.org/10.1038/s43705-023-00334-5 |
| F. Environmental/exposure factors | infrared light | Experimental light regime that stimulated AAP growth in control treatments | ENVO:label-only infrared light exposure | Piwosz 2024 (piwosz2024responseofaerobic pages 2-3, piwosz2024responseofaerobic pages 3-4) | https://doi.org/10.1093/femsec/fiae090 |
| F. Environmental/exposure factors | blue-green light | Penetrating aquatic wavelengths captured with carotenoid help | ENVO:label-only blue-green light | Koblížek 2015 (koblizek2015ecologyofaerobic pages 2-4) | https://doi.org/10.1093/femsre/fuv032 |
| F. Environmental/exposure factors | carbon limitation | Condition under which AAP induce photoheterotrophic metabolism | ENVO:label-only carbon limitation | Piwosz 2024 (piwosz2024responseofaerobic pages 2-3) | https://doi.org/10.1093/femsec/fiae090 |
| F. Environmental/exposure factors | dissolved organic carbon (DOC) | Major carbon pool correlated with AAP abundance/diversity dynamics | CHEBI:label-only DOC | Villena-Alemany 2024 (villenaalemany2024phenologyandecological pages 1-2) | https://doi.org/10.1186/s40168-024-01786-0 |
| F. Environmental/exposure factors | irradiance | Environmental driver correlated with AAP abundance and diversity | ENVO:label-only irradiance | Villena-Alemany 2024 (villenaalemany2024phenologyandecological pages 1-2) | https://doi.org/10.1186/s40168-024-01786-0 |
| F. Environmental/exposure factors | temperature | Correlated ecological driver in AAP field studies | ENVO:01000203 | Villena-Alemany 2024 (villenaalemany2024phenologyandecological pages 1-2) | https://doi.org/10.1186/s40168-024-01786-0 |
| F. Environmental/exposure factors | chlorophyll-a bloom / spring phytoplankton bloom | Seasonal ecological context associated with AAP spring maximum | CHEBI:28966 / ENVO:label-only phytoplankton bloom | Villena-Alemany 2024 (villenaalemany2024phenologyandecological pages 1-2) | https://doi.org/10.1186/s40168-024-01786-0 |
| F. Environmental/exposure factors | euphotic zone | Depth range where AAP are concentrated in aquatic systems | ENVO:01000311 | Koblížek 2015 (koblizek2015ecologyofaerobic pages 9-11, koblizek2015ecologyofaerobic media 84704fb5) | https://doi.org/10.1093/femsre/fuv032 |
| G. Assays/observables | pufM amplicon sequencing / metabarcoding | Marker-gene assay for tracking AAP community composition and succession | label-only assay | Villena-Alemany 2024 (villenaalemany2024phenologyandecological pages 1-2) | https://doi.org/10.1186/s40168-024-01786-0 |
| G. Assays/observables | infrared epifluorescence microscopy | Detects BChl a-containing AAP cells via autofluorescence | label-only assay | Stojan 2024 (stojan2024ecologyofaerobic pages 2-5) | https://doi.org/10.1186/s40793-024-00573-6 |
| G. Assays/observables | FISH-IR | Combined fluorescence in situ hybridization and IR detection for quantitative AAP group analysis | label-only assay | Stojan 2024 (stojan2024ecologyofaerobic pages 1-2) | https://doi.org/10.1186/s40793-024-00573-6 |
| G. Assays/observables | absorption spectroscopy | Demonstrates functional pigments and reaction-center/antenna absorption features | label-only assay | Koblížek 2015 (koblizek2015ecologyofaerobic pages 2-4) | https://doi.org/10.1093/femsre/fuv032 |
| G. Assays/observables | IR kinetic fluorescence measurements | Assay supporting functionality of photosynthetic reaction centers in AAP bacteria | label-only assay | Koblížek 2015 (koblizek2015ecologyofaerobic pages 2-4) | https://doi.org/10.1093/femsre/fuv032 |
| G. Assays/observables | AAP abundance (cells mL−1) | Quantitative ecological observable used in seasonal studies | label-only observable | Stojan 2024 (stojan2024ecologyofaerobic pages 1-2) | https://doi.org/10.1186/s40793-024-00573-6 |
| G. Assays/observables | AAP relative contribution to community (%) | Observable used to quantify ecological importance of AAPs | label-only observable | Villena-Alemany 2024 (villenaalemany2024phenologyandecological pages 1-2) | https://doi.org/10.1186/s40168-024-01786-0 |


*Table: This table lists candidate nodes for a phototrophic TraitMech causal graph, grouped by biological role and grounded to available identifiers where possible. It is useful for curating a node inventory before selecting evidence-backed causal edges.*

### 7) Evidence-backed candidate causal edges (triples)
| Edge (subject–predicate–object) | Edge type | Evidence source | DOI URL | Publication date | Supporting snippet | Notes/uncertainty | Suggested ontology grounding | Citation |
|---|---|---|---|---|---|---|---|---|
| chlorophototrophy — uses energy from — light | mechanistic | Tinguely 2023, ISME Communications | https://doi.org/10.1038/s43705-023-00334-5 | 09/2023 | “chlorophototrophy, which is based on photochemical reaction centers containing chlorophylls or bacteriochlorophylls” | Broad definition-level edge for chlorophyll-based phototrophy. | subject: GO:0015979 photosynthesis; object: CHEBI:24866 light | (tinguely2023diurnalcyclesdrive pages 1-2) |
| retinalophototrophy — uses — rhodopsins | mechanistic | Tinguely 2023, ISME Communications | https://doi.org/10.1038/s43705-023-00334-5 | 09/2023 | “retinalophototrophy, which uses rhodopsins to pump ions through the membrane” | Supports a distinct phototrophic mechanism outside chlorophototrophy. | subject: label-only retinalophototrophy; object: GO:0016036 rhodopsin; CHEBI:30527 retinal | (tinguely2023diurnalcyclesdrive pages 1-2) |
| rhodopsins — pump — ions across membrane | mechanistic | Tinguely 2023, ISME Communications | https://doi.org/10.1038/s43705-023-00334-5 | 09/2023 | “uses rhodopsins to pump ions through the membrane” | General rhodopsin-phototrophy edge; ion identity not specified in this excerpt. | subject: GO:0016036 rhodopsin; object: GO:0006811 ion transport | (tinguely2023diurnalcyclesdrive pages 1-2) |
| AAnP — produces usable energy from — light | mechanistic | Tinguely 2023, ISME Communications | https://doi.org/10.1038/s43705-023-00334-5 | 09/2023 | “usable energy is produced from light under aerobic conditions” | Defines aerobic anoxygenic phototrophy as a light-energy metabolism. | subject: METPO:1000660 phototrophic; object: CHEBI:24866 light | (tinguely2023diurnalcyclesdrive pages 1-2) |
| AAnP — lacks — H2O dissociation and O2 release | mechanistic | Tinguely 2023, ISME Communications | https://doi.org/10.1038/s43705-023-00334-5 | 09/2023 | “in the absence of H2O dissociation and O2 release” | Useful boundary edge distinguishing anoxygenic from oxygenic phototrophy. | subject: label-only aerobic anoxygenic phototrophy; object: CHEBI:15377 water / CHEBI:15379 dioxygen | (tinguely2023diurnalcyclesdrive pages 1-2) |
| bacteriochlorophyll a biosynthesis — generates risk of — reactive oxygen species | regulatory | Tinguely 2023, ISME Communications | https://doi.org/10.1038/s43705-023-00334-5 | 09/2023 | “bacteriochlorophyll a biosynthesis and AAnP represent a significant energy investment and are known to generate toxic byproducts, especially singlet oxygen and other reactive oxygen species” | Strong mechanistic rationale for regulation; mostly discussed for AAnP under oxic light conditions. | subject: GO:0015995 chlorophyll biosynthetic process / bacteriochlorophyll biosynthesis label; object: CHEBI:24726 reactive oxygen species, CHEBI:35697 singlet oxygen | (tinguely2023diurnalcyclesdrive pages 1-2) |
| oxygen plus light — promotes formation of — reactive oxygen species during BChl synthesis | regulatory | Tinguely 2023, ISME Communications | https://doi.org/10.1038/s43705-023-00334-5 | 09/2023 | “in the presence of oxygen and light” | Context-dependent; best curated as environmental modulation of pigment-biosynthesis hazard. | subject: CHEBI:15379 dioxygen + CHEBI:24866 light; object: CHEBI:24726 reactive oxygen species | (tinguely2023diurnalcyclesdrive pages 1-2) |
| dark phase — permits — bacteriochlorophyll a synthesis in many AAP bacteria | regulatory | Tinguely 2023, ISME Communications | https://doi.org/10.1038/s43705-023-00334-5 | 09/2023 | “many aerobic anoxygenic phototrophs tend to regulate bacteriochlorophyll a production strictly and limit its synthesis to dark phases” | Taxon-general but not universal; keep as tendency, not absolute rule. | subject: ENVO:01000755 dark period (label); object: CHEBI:28133 bacteriochlorophyll a | (tinguely2023diurnalcyclesdrive pages 1-2) |
| light — inhibits — BChl a synthesis in most AAP species | regulatory | Koblížek 2015, FEMS Microbiology Reviews | https://doi.org/10.1093/femsre/fuv032 | 11/2015 | “BChl a synthesis in most AAP species is inhibited by light” | Strong curation candidate for regulatory edge in AAP subgraph. | subject: CHEBI:24866 light; object: CHEBI:28133 bacteriochlorophyll a | (koblizek2015ecologyofaerobic pages 2-4) |
| carotenoids — extend absorption into — blue-green spectrum | mechanistic | Koblížek 2015, FEMS Microbiology Reviews | https://doi.org/10.1093/femsre/fuv032 | 11/2015 | “Carotenoids serve as auxiliary pigments which extend absorption to the blue-green part of the spectrum” | Good pigment-function edge. | subject: CHEBI:23044 carotenoid; object: label-only blue-green light | (koblizek2015ecologyofaerobic pages 2-4) |
| carotenoid-captured excitation energy — is transferred to — BChl a molecules | mechanistic | Koblížek 2015, FEMS Microbiology Reviews | https://doi.org/10.1093/femsre/fuv032 | 11/2015 | “The excitation energy captured by the carotenoids is transferred within picoseconds to the BChl a molecules” | Direct light-harvesting edge. | subject: CHEBI:23044 carotenoid; object: CHEBI:28133 bacteriochlorophyll a | (koblizek2015ecologyofaerobic pages 2-4) |
| BChl a in reaction center — enables — primary charge separation | mechanistic | Koblížek 2015, FEMS Microbiology Reviews | https://doi.org/10.1093/femsre/fuv032 | 11/2015 | “and used for primary charge separation in the reaction center” | Foundational photochemistry edge. | subject: CHEBI:28133 bacteriochlorophyll a; object: GO:0006979 response to oxidative? / label-only primary charge separation | (koblizek2015ecologyofaerobic pages 2-4) |
| AAP bacteria — lack — carbon fixation pathways | mechanistic | Koblížek 2015, FEMS Microbiology Reviews | https://doi.org/10.1093/femsre/fuv032 | 11/2015 | “AAP bacteria are unable to grow photoautotrophically as they lack carbon fixation pathways” | Important negative edge delimiting phototrophic vs photoautotrophic scope. | subject: label-only AAP bacteria; object: GO:0015977 carbon fixation | (koblizek2015ecologyofaerobic pages 2-4) |
| anaplerotic carboxylation — contributes — limited cellular carbon in AAP | mechanistic | Koblížek 2015, FEMS Microbiology Reviews | https://doi.org/10.1093/femsre/fuv032 | 11/2015 | “The anaplerotic carboxylation may contribute 0.6–11% of total cellular carbon” | Quantitative but AAP-specific; not equivalent to autotrophic carbon fixation. | subject: GO:0046394 carboxylic acid biosynthetic/anaplerotic carboxylation label; object: label-only cellular carbon pool | (koblizek2015ecologyofaerobic pages 2-4) |
| pufM gene — encodes subunit of — type 2 photochemical reaction center | assay | Tahon 2016, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2016.02026 | 12/2016 | “pufM genes, encoding a subunit of the type 2 photochemical reaction center found in anoxygenic phototrophic bacteria” | Strong assay/marker edge for RCII-containing phototrophs. | subject: gene:pufM; object: label-only type II photochemical reaction center | (tahon2016diversityofphototrophic pages 1-2) |
| bchL/chlL — involved in — (bacterio)chlorophyll synthesis | assay | Tahon 2016, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2016.02026 | 12/2016 | “bchL and chlL, involved in (bacterio)chlorophyll synthesis” | Useful candidate gene-to-process edge. | subject: gene:bchL/chlL; object: GO:0015995 chlorophyll biosynthetic process | (tahon2016diversityofphototrophic pages 1-2) |
| bchXYZ — encodes — chlorin oxidoreductase for bacteriochlorophyllide formation | mechanistic | Tahon 2016, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2016.02026 | 12/2016 | “chlorin oxidoreductase (COR), encoded by bchXYZ genes, reduces chlorin to bacteriochlorophyllide” | Strong pathway edge for bacteriochlorophyll branch. | subject: gene:bchXYZ; object: KEGG/MetaCyc chlorin oxidoreductase / CHEBI:bacteriochlorophyllide label | (tahon2016diversityofphototrophic pages 1-2) |
| early anoxygenic phototrophy — uses electron donor — H2S | mechanistic | Tahon 2016, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2016.02026 | 12/2016 | “used reductants such as H2, Fe2+, or H2S for bacteriochlorophyll-dependent anaerobic anoxygenic phototrophy” | Historical/general statement; applicable to anoxygenic phototrophic scope, not all phototrophs. | subject: label-only anoxygenic phototrophy; object: CHEBI:16136 hydrogen sulfide | (tahon2016diversityofphototrophic pages 1-2) |
| early anoxygenic phototrophy — uses electron donor — H2 | mechanistic | Tahon 2016, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2016.02026 | 12/2016 | “used reductants such as H2, Fe2+, or H2S” | Broad/general edge; likely lineage-specific in modern taxa. | subject: label-only anoxygenic phototrophy; object: CHEBI:18276 hydrogen | (tahon2016diversityofphototrophic pages 1-2) |
| early anoxygenic phototrophy — uses electron donor — Fe2+ | mechanistic | Tahon 2016, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2016.02026 | 12/2016 | “used reductants such as H2, Fe2+, or H2S” | Broad/general edge; curate cautiously unless taxon-specific support added. | subject: label-only anoxygenic phototrophy; object: CHEBI:29033 iron(2+) | (tahon2016diversityofphototrophic pages 1-2) |
| cyanobacterial oxygenic phototrophy — uses electron donor — water | mechanistic | Kushkevych 2024, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2024.1417714 | 07/2024 | “water acts as an electron donor being oxidized to molecular oxygen (O2)” | This edge belongs to oxygenic phototrophy branch; not universal for all phototrophs. | subject: label-only oxygenic photosynthesis; object: CHEBI:15377 water | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| green sulfur bacteria — use electron donor — H2S | mechanistic | Kushkevych 2024, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2024.1417714 | 07/2024 | “In anoxygenic photosynthesis, hydrogen sulfide (H2S) is used as the main electron donor” | Good edge for GSB/PSB sulfur-phototrophy branch. | subject: NCBITaxon:1090 Chlorobiaceae / label-only GSB; object: CHEBI:16136 hydrogen sulfide | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| green sulfur bacteria — oxidize — H2S to elemental sulfur | mechanistic | Kushkevych 2024, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2024.1417714 | 07/2024 | “GSB oxidize H2S to elemental sulfur” | Strong sulfur-metabolism edge in phototrophic context. | subject: label-only GSB; object: CHEBI:16136 hydrogen sulfide / CHEBI:26806 sulfur | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| chlorosomes — serve as — light-collecting antennas | mechanistic | Kushkevych 2024, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2024.1417714 | 07/2024 | “Chlorosomes are vesicles that are surrounded by a lipid monolayer that serve as light-collecting antennas” | Strong structure-to-function edge for GSB. | subject: GO:0030084 chlorosome; object: GO:0009765 photosynthesis, light harvesting | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| carbon dioxide — is assimilated through — reverse tricarboxylic acid cycle in GSB | mechanistic | Kushkevych 2024, Frontiers in Microbiology | https://doi.org/10.3389/fmicb.2024.1417714 | 07/2024 | “The carbon source of GSB is carbon dioxide, which is assimilated through the reverse tricarboxylic acid cycle” | Good carbon-fixation linkage, specific to GSB branch. | subject: CHEBI:16526 carbon dioxide; object: KEGG:reverse tricarboxylic acid cycle / MetaCyc:rTCA | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| photons absorbed by LH complexes — funnel energy to — reaction center | mechanistic | Alarcon 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00863-24 | 06/2024 | “incident photons are absorbed by an array of light-harvesting (LH) complexes… funneling it down an energy gradient to a central reaction center (RC)” | Strong canonical edge for purple sulfur bacteria. | subject: label-only light-harvesting complexes; object: label-only reaction center | (alarcon2024evidenceforautotrophic pages 1-2) |
| reaction center charge separation — drives — redox reactions via quinone/quinol and cytochromes | mechanistic | Alarcon 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00863-24 | 06/2024 | “In RC, charge separation occurs across the membrane and drives a series of redox reactions involving… quinone/quinol, cytochrome b/c, and cytochrome c complexes” | Good electron-transport edge in PSB. | subject: label-only reaction center charge separation; object: GO:0055114 oxidation-reduction process / quinone pool | (alarcon2024evidenceforautotrophic pages 1-2) |
| electron transport — forms — proton motive force | mechanistic | Alarcon 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00863-24 | 06/2024 | “Along with electron transport, proton motive force (PMF) is formed” | Core bioenergetic edge for chlorophototrophy. | subject: GO:0022900 electron transport chain; object: GO:0015992 proton motive force generation | (alarcon2024evidenceforautotrophic pages 1-2) |
| proton motive force — powers — ATP synthase complexes | mechanistic | Alarcon 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00863-24 | 06/2024 | “and powers ATP synthase complexes” | Strong energy-conversion edge. | subject: GO:0015992 proton motive force generation; object: GO:0016887 ATP hydrolysis activity / ATP synthase complex GO:0045263 | (alarcon2024evidenceforautotrophic pages 1-2) |
| pufC/pufM/pufL — encode subunits of — reaction center | mechanistic | Alarcon 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00863-24 | 06/2024 | “identifying three subunits of the RC, pufC, pufM, and pufL” | Gene-to-complex grounding for purple sulfur bacteria. | subject: gene:pufC/pufM/pufL; object: label-only photosynthetic reaction center | (alarcon2024evidenceforautotrophic pages 1-2) |
| pufA/pufB — encode — LH1 apoproteins | mechanistic | Alarcon 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00863-24 | 06/2024 | “pufA and pufB genes encoding light-harvesting complex (LH1) apoproteins” | Useful gene-to-antenna edge. | subject: gene:pufA/pufB; object: label-only LH1 complex | (alarcon2024evidenceforautotrophic pages 1-2) |
| puc gene pairs — encode — LH2 apoproteins | mechanistic | Alarcon 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00863-24 | 06/2024 | “Six potential puc gene pairs were also identified that encode α- and β-apoproteins for several LH2 complex types” | Good but specific to purple bacteria. | subject: gene:puc; object: label-only LH2 complex | (alarcon2024evidenceforautotrophic pages 1-2) |
| pyrite electron source — downregulates — LH and RC genes | regulatory | Alarcon 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00863-24 | 06/2024 | “extensive downregulation of genes related to LH and RC complex components indicates that the electron source may have direct control over the bacterial cells’ photosynthetic activity” | Strong but pyrite-condition-specific. | subject: CHEBI:46661 pyrite; object: label-only LH/RC gene expression | (alarcon2024evidenceforautotrophic pages 1-2) |
| pufM metabarcoding — assays — AAP community composition | assay | Villena-Alemany 2024, Microbiome | https://doi.org/10.1186/s40168-024-01786-0 | 03/2024 | “we followed their seasonal succession using the amplicon sequencing of the pufM marker gene” | Strong assay edge, especially for aquatic AAP studies. | subject: gene:pufM; object: label-only AAP community composition | (villenaalemany2024phenologyandecological pages 1-2) |
| IR light — increases growth rate of — AAP bacteria in control treatment | environmental | Piwosz 2024, FEMS Microbiology Ecology | https://doi.org/10.1093/femsec/fiae090 | 06/2024 | “their growth rate was almost twice as fast in the IR light than in the dark” | Experimental, treatment-specific; do not overgeneralize beyond tested freshwater community. | subject: label-only infrared light; object: label-only AAP growth rate | (piwosz2024responseofaerobic pages 2-3) |
| carbon limitation — induces — photoheterotrophic metabolism in AAP bacteria | environmental | Piwosz 2024, FEMS Microbiology Ecology | https://doi.org/10.1093/femsec/fiae090 | 06/2024 | “AAP bacteria induce photoheterotrophic metabolism under carbon limitation” | Comes from article abstract/evidence summary; ecological inference for natural communities. | subject: ENVO:label carbon limitation; object: label-only photoheterotrophic metabolism | (piwosz2024responseofaerobic pages 2-3) |
| lignin or acetate carbon source — inhibits growth of — AAP bacteria, especially in light | environmental | Piwosz 2024, FEMS Microbiology Ecology | https://doi.org/10.1093/femsec/fiae090 | 06/2024 | “recalcitrant (lignin) or low-energy (acetate) carbon sources inhibited the growth of AAP bacteria, especially in light” | Experimental and substrate-specific; useful negative ecological edge. | subject: CHEBI:17579 acetate / label-only lignin; object: label-only AAP growth | (piwosz2024responseofaerobic pages 2-3, piwosz2024responseofaerobic pages 3-4) |
| AAP abundance — peaks after — spring phytoplankton bloom | environmental | Villena-Alemany 2024, Microbiome | https://doi.org/10.1186/s40168-024-01786-0 | 03/2024 | “AAP bacteria displayed a clear seasonal trend with a spring maximum following the bloom of phytoplankton” | Ecological pattern, not direct mechanism. | subject: label-only AAP abundance; object: ENVO:label spring phytoplankton bloom | (villenaalemany2024phenologyandecological pages 1-2) |
| AAP abundance — may account for up to — 22% of bacteria in lakes during spring | environmental | Villena-Alemany 2024, Microbiome | https://doi.org/10.1186/s40168-024-01786-0 | 03/2024 | “AAP bacteria peak during spring in lakes, when they may account for up to 22% of bacteria” | Useful quantitative ecology statistic; phenotype prevalence, not mechanism. | subject: label-only AAP abundance; object: label-only total bacterial community fraction | (villenaalemany2024phenologyandecological pages 1-2) |
| IR/FISH-IR BChl autofluorescence — detects — AAP cells | assay | Stojan 2024, Environmental Microbiome | https://doi.org/10.1186/s40793-024-00573-6 | 04/2024 | “Bacteriochlorophyll-a (Bchl a) autofluorescence is used to detect AAPs by infrared epifluorescence microscopy” | Strong assay edge; signal fading caveat in methods paper. | subject: CHEBI:28133 bacteriochlorophyll a autofluorescence; object: label-only AAP cells | (stojan2024ecologyofaerobic pages 2-5) |
| pufM — encodes — M-chain of photosynthetic reaction centre complex | assay | Stojan 2024, Environmental Microbiome | https://doi.org/10.1186/s40793-024-00573-6 | 04/2024 | “pufM gene (encoding the M-chain of the photosynthetic reaction centre complex)” | Reinforces pufM grounding as assay marker. | subject: gene:pufM; object: label-only reaction centre M-chain | (stojan2024ecologyofaerobic pages 2-5) |


*Table: This table compiles candidate subject–predicate–object edges for a phototrophic TraitMech graph, grounded in recent and foundational literature. It spans core mechanisms, regulation, environmental drivers, and commonly used assay markers, with verbatim supporting snippets and ontology suggestions for curation.*

### 8) Expert opinions / authoritative synthesis (interpretive notes)
- **AAP as facultative photoheterotrophs:** Multiple authoritative sources frame AAP as organisms that use light to increase energy efficiency while relying on organic carbon; mechanistic links include reduced respiration and increased biomass yield, consistent with their ecological role as recyclers of dissolved organic matter rather than primary producers. (villenaalemany2024phenologyandecological pages 1-2, stojan2024ecologyofaerobic pages 1-2, koblizek2015ecologyofaerobic pages 2-4)
- **Regulatory logic under oxic illumination:** The repeated observation that BChl synthesis is inhibited by light in many AAP taxa is consistent with ROS/phototoxicity risks of pigment biosynthesis under oxygen and light, motivating explicit regulation edges in the causal graph. (koblizek2015ecologyofaerobic pages 2-4, tinguely2023diurnalcyclesdrive pages 1-2)

### 9) Curation warnings (claims to treat as uncertain or out-of-scope)
1. **Overgeneralizing electron donors across “anoxygenic phototrophy.”** Statements that early anoxygenic phototrophs used H2, Fe2+, or H2S are broad and historically framed; curating them as universal edges for all modern anoxygenic phototrophs would be overreach without lineage-specific support. Mark as *uncertain/general*. (tahon2016diversityofphototrophic pages 1-2)
2. **Treating AAP as photoautotrophs.** AAP are repeatedly described as lacking carbon fixation pathways and thus not photoautotrophic; any carbon fixation node/edge should be placed in oxygenic phototrophy or specific anoxygenic autotroph branches (e.g., GSB rTCA), not in core AAP. (koblizek2015ecologyofaerobic pages 2-4, kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
3. **Rhodopsin-based phototrophy details.** Within the available excerpts, rhodopsin phototrophy is defined at a high level (ion pumping), but specific ion species, stoichiometries, or antenna/rhodopsin structural details are not supported by the provided text and should not yet be curated as mechanistic edges beyond ion pumping. (tinguely2023diurnalcyclesdrive pages 1-2)
4. **Substrate-specific responses.** Lignin/acetate inhibitory effects and pyrite-driven regulation are context-specific experimental findings; curate as conditional edges (environmental/modulatory) rather than universal properties of phototrophy. (piwosz2024responseofaerobic pages 3-4, alarcon2024evidenceforautotrophic pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates where available)
1. Villena‑Alemany C. et al. **Phenology and ecological role of aerobic anoxygenic phototrophs in freshwaters.** *Microbiome* (Mar 2024). https://doi.org/10.1186/s40168-024-01786-0 (villenaalemany2024phenologyandecological pages 1-2)
2. Stojan I. et al. **Ecology of aerobic anoxygenic phototrophs… in Adriatic Sea…** *Environmental Microbiome* (Apr 2024). https://doi.org/10.1186/s40793-024-00573-6 (stojan2024ecologyofaerobic pages 1-2)
3. Piwosz K. et al. **Response of aerobic anoxygenic phototrophic bacteria to limitation and availability of organic carbon.** *FEMS Microbiology Ecology* (Jun 2024). https://doi.org/10.1093/femsec/fiae090 (piwosz2024responseofaerobic pages 2-3, piwosz2024responseofaerobic pages 3-4)
4. Alarcon H.V. et al. **Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source.** *Applied and Environmental Microbiology* (Published 20 Jun 2024; issue Jul 2024). https://doi.org/10.1128/aem.00863-24 (alarcon2024evidenceforautotrophic pages 1-2)
5. Kushkevych I. et al. **Anoxygenic photosynthesis with emphasis on green sulfur bacteria…** *Frontiers in Microbiology* (11 Jul 2024). https://doi.org/10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
6. Tinguely C. et al. **Diurnal cycles drive rhythmic physiology and promote survival in facultative phototrophic bacteria.** *ISME Communications* (Sep 2023). https://doi.org/10.1038/s43705-023-00334-5 (tinguely2023diurnalcyclesdrive pages 1-2)
7. Koblížek M. **Ecology of aerobic anoxygenic phototrophs in aquatic environments.** *FEMS Microbiology Reviews* (Nov 2015). https://doi.org/10.1093/femsre/fuv032 (koblizek2015ecologyofaerobic pages 2-4)
8. Tahon G. et al. **Diversity of phototrophic genes suggests multiple bacteria may be able to exploit sunlight in exposed soils… Antarctica.** *Frontiers in Microbiology* (19 Dec 2016). https://doi.org/10.3389/fmicb.2016.02026 (tahon2016diversityofphototrophic pages 1-2)

### Figure cited
- Depth profile of AAP abundance vs depth (Figure 7, Koblížek 2015) (koblizek2015ecologyofaerobic media 84704fb5)


References

1. (tinguely2023diurnalcyclesdrive pages 1-2): Camille Tinguely, Mélanie Paulméry, Céline Terrettaz, and Diego Gonzalez. Diurnal cycles drive rhythmic physiology and promote survival in facultative phototrophic bacteria. ISME Communications, Sep 2023. URL: https://doi.org/10.1038/s43705-023-00334-5, doi:10.1038/s43705-023-00334-5. This article has 13 citations and is from a peer-reviewed journal.

2. (koblizek2015ecologyofaerobic pages 2-4): Michal Koblížek. Ecology of aerobic anoxygenic phototrophs in aquatic environments. FEMS microbiology reviews, 39 6:854-70, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv032, doi:10.1093/femsre/fuv032. This article has 253 citations and is from a domain leading peer-reviewed journal.

3. (villenaalemany2024phenologyandecological pages 1-2): Cristian Villena-Alemany, Izabela Mujakić, Livia K. Fecskeová, Jason Woodhouse, Adrià Auladell, Jason Dean, Martina Hanusová, Magdalena Socha, Carlota R. Gazulla, Hans-Joachim Ruscheweyh, Shinichi Sunagawa, Vinicius Silva Kavagutti, Adrian-Ştefan Andrei, Hans-Peter Grossart, Rohit Ghai, Michal Koblížek, and Kasia Piwosz. Phenology and ecological role of aerobic anoxygenic phototrophs in freshwaters. Microbiome, Mar 2024. URL: https://doi.org/10.1186/s40168-024-01786-0, doi:10.1186/s40168-024-01786-0. This article has 18 citations and is from a highest quality peer-reviewed journal.

4. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

5. (tahon2016diversityofphototrophic pages 1-2): Guillaume Tahon, Bjorn Tytgat, and Anne Willems. Diversity of phototrophic genes suggests multiple bacteria may be able to exploit sunlight in exposed soils from the sør rondane mountains, east antarctica. Frontiers in Microbiology, Dec 2016. URL: https://doi.org/10.3389/fmicb.2016.02026, doi:10.3389/fmicb.2016.02026. This article has 29 citations and is from a peer-reviewed journal.

6. (stojan2024ecologyofaerobic pages 1-2): Iva Stojan, Danijela Šantić, Cristian Villena-Alemany, Željka Trumbić, Frano Matić, Ana Vrdoljak Tomaš, Ivana Lepen Pleić, Kasia Piwosz, Grozdan Kušpilić, Živana Ninčević Gladan, Stefanija Šestanović, and Mladen Šolić. Ecology of aerobic anoxygenic phototrophs on a fine-scale taxonomic resolution in adriatic sea unravelled by unsupervised neural network. Environmental Microbiome, Apr 2024. URL: https://doi.org/10.1186/s40793-024-00573-6, doi:10.1186/s40793-024-00573-6. This article has 6 citations and is from a peer-reviewed journal.

7. (stojan2024ecologyofaerobic pages 2-5): Iva Stojan, Danijela Šantić, Cristian Villena-Alemany, Željka Trumbić, Frano Matić, Ana Vrdoljak Tomaš, Ivana Lepen Pleić, Kasia Piwosz, Grozdan Kušpilić, Živana Ninčević Gladan, Stefanija Šestanović, and Mladen Šolić. Ecology of aerobic anoxygenic phototrophs on a fine-scale taxonomic resolution in adriatic sea unravelled by unsupervised neural network. Environmental Microbiome, Apr 2024. URL: https://doi.org/10.1186/s40793-024-00573-6, doi:10.1186/s40793-024-00573-6. This article has 6 citations and is from a peer-reviewed journal.

8. (alarcon2024evidenceforautotrophic pages 1-2): Hugo V. Alarcon, Jonathon E. Mohl, Grace W. Chong, Ana Betancourt, Yi Wang, Weinan Leng, Jason C. White, and Jie Xu. Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source. Jul 2024. URL: https://doi.org/10.1128/aem.00863-24, doi:10.1128/aem.00863-24. This article has 5 citations and is from a peer-reviewed journal.

9. (piwosz2024responseofaerobic pages 3-4): Kasia Piwosz, Cristian Villena-Alemany, Joanna Całkiewicz, Izabela Mujakić, Vít Náhlík, Jason Dean, and Michal Koblížek. Response of aerobic anoxygenic phototrophic bacteria to limitation and availability of organic carbon. FEMS Microbiology Ecology, Jun 2024. URL: https://doi.org/10.1093/femsec/fiae090, doi:10.1093/femsec/fiae090. This article has 6 citations and is from a peer-reviewed journal.

10. (koblizek2015ecologyofaerobic media 84704fb5): Michal Koblížek. Ecology of aerobic anoxygenic phototrophs in aquatic environments. FEMS microbiology reviews, 39 6:854-70, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv032, doi:10.1093/femsre/fuv032. This article has 253 citations and is from a domain leading peer-reviewed journal.

11. (koblizek2015ecologyofaerobic pages 9-11): Michal Koblížek. Ecology of aerobic anoxygenic phototrophs in aquatic environments. FEMS microbiology reviews, 39 6:854-70, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv032, doi:10.1093/femsre/fuv032. This article has 253 citations and is from a domain leading peer-reviewed journal.

12. (piwosz2024responseofaerobic pages 2-3): Kasia Piwosz, Cristian Villena-Alemany, Joanna Całkiewicz, Izabela Mujakić, Vít Náhlík, Jason Dean, and Michal Koblížek. Response of aerobic anoxygenic phototrophic bacteria to limitation and availability of organic carbon. FEMS Microbiology Ecology, Jun 2024. URL: https://doi.org/10.1093/femsec/fiae090, doi:10.1093/femsec/fiae090. This article has 6 citations and is from a peer-reviewed journal.