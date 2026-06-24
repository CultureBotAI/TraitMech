---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:33:58.350746'
end_time: '2026-06-18T10:54:38.209487'
duration_seconds: 1239.86
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: autotrophic
  trait_identifier: METPO:1000632
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: autotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism produces organic compounds from
    inorganic carbon sources (primarily carbon dioxide or bicarbonate) using energy
    from light (photoautotrophy) or from the oxidation of inorganic compounds (chemoautotrophy).
  parent_traits: METPO:1000631
  synonyms: TT_autotroph, autotroph, autotrophy
  evidence_summary: 'DOI:10.1038/nrmicro.2016.130: require only CO2 as a carbon source
    (Review defines autotrophic organisms by CO2 use as carbon source for growth.)
    | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports Calvin-Benson
    and other microbial CO2-fixation pathways.) | PMID:8590279: Synechocystis sp.
    strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model autotrophic
    cyanobacterium that fixes CO2 via the Calvin-Benson cycle (Kaneko et al. 1996,
    DNA Res, full genome).)'
  causal_graph_summary: 'autotrophic_inorganic_carbon_fixation: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** autotrophic
- **METPO identifier:** METPO:1000632
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism produces organic compounds from inorganic carbon sources (primarily carbon dioxide or bicarbonate) using energy from light (photoautotrophy) or from the oxidation of inorganic compounds (chemoautotrophy).
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_autotroph, autotroph, autotrophy
- **Existing evidence:** DOI:10.1038/nrmicro.2016.130: require only CO2 as a carbon source (Review defines autotrophic organisms by CO2 use as carbon source for growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports Calvin-Benson and other microbial CO2-fixation pathways.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model autotrophic cyanobacterium that fixes CO2 via the Calvin-Benson cycle (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** autotrophic_inorganic_carbon_fixation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **autotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/autotrophic.yaml`.

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
- **Trait label:** autotrophic
- **METPO identifier:** METPO:1000632
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism produces organic compounds from inorganic carbon sources (primarily carbon dioxide or bicarbonate) using energy from light (photoautotrophy) or from the oxidation of inorganic compounds (chemoautotrophy).
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_autotroph, autotroph, autotrophy
- **Existing evidence:** DOI:10.1038/nrmicro.2016.130: require only CO2 as a carbon source (Review defines autotrophic organisms by CO2 use as carbon source for growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports Calvin-Benson and other microbial CO2-fixation pathways.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model autotrophic cyanobacterium that fixes CO2 via the Calvin-Benson cycle (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** autotrophic_inorganic_carbon_fixation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **autotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/autotrophic.yaml`.

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


## Microbial trait causal graph report: **autotrophic** (METPO:1000632)

### Scope summary (TraitMech curation intent)
**Autotrophic (METPO:1000632)** denotes a physiological trophic type where organisms **use inorganic carbon (CO2 and/or HCO3−)** as the principal carbon source for biomass formation, by coupling carbon fixation to an energy source (light in photoautotrophy; oxidation of inorganic/trace gases in chemoautotrophy/chemolithoautotrophy). Autotrophy is therefore best represented mechanistically as **capacity for net inorganic carbon fixation into organic biomass** via one (or more) prokaryotic/archaeal CO2-fixation pathways plus supporting uptake/energy modules. (wang2023microbialconversionand pages 7-8, scott2024widespreaddissolvedinorganic pages 1-2)

**Boundary cases and nearby traits**
- **Heterotrophy**: growth on organic carbon substrates (e.g., carbohydrates, lipids, organic acids) rather than requiring CO2 as the main carbon source; many organisms are **facultative**, switching between autotrophy and heterotrophy depending on conditions (e.g., *Cupriavidus necator* grows heterotrophically on organics, but autotrophically on H2/CO2/O2). (li2024productionofsuccinate pages 1-2)
- **Mixotrophy**: explicitly defined as “**the simultaneous usage of heterotrophic and autotrophic processes, thereby involving multiple different inorganic and organic carbon and energy sources**.” This overlaps with autotrophy but should not be conflated with strict/obligate autotrophy. (ray2023clearingtheair pages 2-4)
- **Lithotrophy vs organotrophy** (energy/electron source traits): autotrophy can be lithoautotrophic (H2, CO, sulfide oxidation, etc.) or photoautotrophic; these are separable axes from carbon source.

### Key concepts and current understanding (2023–2024 emphasis)
#### Inorganic carbon pool and speciation
A central mechanistic constraint is that dissolved inorganic carbon (DIC = CO2 + HCO3− + CO32−) is **pH-speciated**, which controls which inorganic carbon species dominates and thus which uptake/enzymatic strategies are favorable: “**CO2 predominates below ~pH 6.4, HCO3− at circumneutral pH, and CO32− above ~pH 10.3**.” (scott2024widespreaddissolvedinorganic pages 7-10)

#### Carbon concentrating mechanisms (CCMs) and DIC toolkits
Many autotrophs (notably cyanobacteria and some proteobacteria) require modules that bridge environmental DIC supply to intracellular carboxylation demand. Cyanobacterial CCM components include:
- **Bicarbonate transporters**: SbtA, BicA, and BCT1. (kurkela2024inorganiccarbonsensing pages 1-2)
- **Specialized NDH complexes (NDH-13/NDH-14)** that “**convert CO2 to HCO3− in the cytoplasm**.” (kurkela2024inorganiccarbonsensing pages 1-2)
- **Carboxysomes**, microcompartments containing RuBisCO and carbonic anhydrase, “in which the first reaction of carbon fixation occurs.” (kurkela2024inorganiccarbonsensing pages 1-2)

The DIC toolkit framing emphasizes that carbonic anhydrases (CAs) and DIC transporters solve the kinetic and permeability mismatch between CO2 and HCO3− supply and demand, and that CCMs can be disrupted by mis-localizing CA activity, causing CO2 leakage (reviewed mechanistically). (scott2024widespreaddissolvedinorganic pages 2-4)

#### Core CO2 fixation pathways (mechanism nodes)
Recent synthesis and pathway cataloging reinforces that autotrophy can be realized through multiple microbial pathways beyond the Calvin–Benson–Bassham (CBB) cycle, with major ecological and engineering relevance. A wetland-focused synthesis explicitly organizes these as “Pathways for autotrophic CO2 fixation” and provides energetic and environmental constraints (e.g., oxygen sensitivity, ATP costs), including rTCA, Wood–Ljungdahl (WLP), 3HP/4HB, DC/4HB, and reductive glycine. (gruterich2024metagenomicandmetatranscriptomic pages 21-23)

### Recent developments and latest research (prioritize 2023–2024)
#### 1) New carboxysomal carbonic anhydrase type (ιCA) in sulfur chemolithoautotrophs (2024)
A key 2024 advance is direct functional evidence for **iota-class carbonic anhydrase (ιCA)** as a carboxysomal CA in *Thiomicrospira* spp., addressing a long-standing puzzle where canonical carboxysomal CA genes were missing.

Wieschollek et al. (AEM, 2024) report that CCMs “**consist of CO2 and HCO3− transporters and carboxysomes**,” and that carboxysomes contain CA and RuBisCO such that “**When cytoplasmic HCO3− enters carboxysomes, CA converts it to CO2, and it is fixed by RubisCO**.” (wieschollek2024anewtype pages 1-2)

Crucially, they show gene-to-phenotype causality: “**When the gene encoding ιCA was interrupted in T. pelophila, cells could no longer grow under low-CO2 conditions, and CA activity was no longer detectable in their carboxysomes**.” (wieschollek2024anewtype pages 1-2)

Figure evidence supporting locus context and functional assays for ιCA within carboxysome loci is available from the paper’s extracted figures. (wieschollek2024anewtype media 33d6b164, wieschollek2024anewtype media d5c01eee, wieschollek2024anewtype media 023b26e3, wieschollek2024anewtype media 9979b826, wieschollek2024anewtype media cebe6107, wieschollek2024anewtype media 95ec58ec)

#### 2) Atmospheric chemosynthesis and trace-gas powered chemoautotrophy (2023)
A 2023 MMBR review synthesizes “atmospheric chemosynthesis” as a proposed minimal chemoautotrophic primary production mode, linking **high-affinity H2 and CO oxidation** to energy generation and the CBB cycle. It provides quantitative kinetic and environmental context (e.g., high-affinity hydrogenase Km = 30–200 nM) and frames mixotrophy explicitly. However, it also notes ongoing debate about whether trace-gas oxidation is directly coupled to net carbon fixation in situ, so this edge should be curated as **contextual/uncertain**. (ray2023clearingtheair pages 2-4)

#### 3) Expanded engineering playbook for acetogenic CO2 fixation and CCU (2024)
A 2024 RSC Chemical Biology review emphasizes acetogens as CCU biocatalysts using the **Wood–Ljungdahl pathway**, described as “the most energetically efficient CO2 fixation pathway in nature,” and provides mechanistic bookkeeping: “**two CO2 molecules to acetyl-CoA via the WLP**,” requiring “**one ATP molecule and eight electrons**,” with reducing equivalents supplied by electron carriers (ferredoxin/NADH) and typically by H2 or CO as energy sources. (bae2024harnessingacetogenicbacteria pages 1-2)

A 2024 Nature Communications study in *Acetobacterium woodii* provides additional primary evidence linking electron flow/redox modules to acetogenic performance and industrially relevant substrates (CO, formate), including quantitative outcomes (e.g., CO-adapted mutant “final biomass twice” wild type on formate; growth under 25% CO after adaptation; acetate production ~21–25 mM). (moon2024redirectingelectronflow pages 1-2)

### Current applications and real-world implementations
#### Carbon capture and utilization (CCU) with acetogens and microbial electrosynthesis (MES)
The acetogen CCU literature emphasizes practical routes where reducing power is supplied by **electricity (MES)** or **light-driven systems** to convert CO2 into multicarbon products. MES performance data in the 2024 review include titers and rates across systems (e.g., acetate titers reported up to 11 g L−1 in *Sporomusa ovata*; and “highest acetate titer of 16.0 g L−1” in lab-scale fed-batch reactors), illustrating real-world oriented scaling metrics. (bae2024harnessingacetogenicbacteria pages 10-12)

#### Engineered CO2 incorporation into commodity chemicals: succinate case (2024)
A 2024 Microbial Cell Factories study demonstrates an engineered strategy to increase carbon efficiency by coupling organic feedstocks (fatty acids) to CO2 fixation through a portion of the **3-hydroxypropionate (3HP) cycle** in *Cupriavidus necator*.
- Stoichiometric/statistical claim: “**single succinate molecule from one acetyl-CoA molecule and two CO2 molecules**” with isotope verification; “**50% of the carbon atoms present in succinate are derived from CO2**,” “twofold increase in efficiency” vs prior methods, and a resulting titer of **3.6 g/L succinate (159% increase)** over starting strain. (li2024productionofsuccinate pages 1-2)
These are valuable for the **applications** section but should be curated as **synthetic/engineered** rather than native autotrophy mechanism edges.

### Relevant statistics and data points from recent studies
- DIC speciation threshold summary: CO2 vs HCO3− vs CO32− transitions around pH ~6.4 and ~10.3 (qualitative thresholds). (scott2024widespreaddissolvedinorganic pages 7-10)
- Atmospheric chemosynthesis kinetics and activity examples: high-affinity hydrogenase Km 30–200 nM; soils oxidized H2 at 3.49 nmol/h/g and CO at 0.42 nmol/h/g; prevalence of relevant markers in MAGs reported in the review’s compiled datasets. (ray2023clearingtheair pages 2-4)
- Soil ecosystem-scale patterns (China survey): paddy soils had stronger inferred contributions from autotrophic microorganisms (e.g., “autotrophic microorganisms were more important in paddy soils (53%)”), and phototrophic protists contributed “up to 21%” to C storage in paddy soils; flooding increased fixation vs well-drained conditions in a parallel experiment. (liao2023microbialautotrophyexplains pages 6-7, liao2023microbialautotrophyexplains pages 9-10)
- Engineered succinate production: 3.6 g/L succinate; 159% increase; 50% of succinate carbon from CO2. (li2024productionofsuccinate pages 1-2)

### Candidate nodes (grouped by type; ontology grounding suggestions)
#### Trait node
- autotrophic (METPO:1000632)

#### Pathways / modules
- Calvin–Benson–Bassham (CBB) cycle (label-only)
- Carbon concentrating mechanism (CCM) (label-only)
- Wood–Ljungdahl pathway / acetyl-CoA pathway (label-only; MetaCyc/KEGG mapping recommended) (bae2024harnessingacetogenicbacteria pages 1-2, gruterich2024metagenomicandmetatranscriptomic pages 21-23)
- reductive TCA (rTCA) cycle (label-only) (gruterich2024metagenomicandmetatranscriptomic pages 21-23)
- 3HP/4HB cycle; DC/4HB cycle; 3HP bicycle (label-only) (gruterich2024metagenomicandmetatranscriptomic pages 21-23)
- reductive glycine pathway (rGly) (label-only) (gruterich2024metagenomicandmetatranscriptomic pages 21-23)

#### Genes/proteins/complexes (representative, not exhaustive)
- RuBisCO (EC:4.1.1.39); gene labels rbcL/rbcS and cbbL/cbbS depending on clade/context (kurkela2024inorganiccarbonsensing pages 1-2, wieschollek2024anewtype pages 1-2)
- carbonic anhydrase (EC:4.2.1.1); includes iota-class CA (ιCA; label-only subclass) (wieschollek2024anewtype pages 1-2)
- bicarbonate transporters: SbtA, BicA, BCT1 (GO:0015701 bicarbonate transport) (kurkela2024inorganiccarbonsensing pages 1-2)
- NDH-13/NDH-14 specialized complexes (label-only; involved in Ci uptake) (kurkela2024inorganiccarbonsensing pages 1-2)
- carboxysome (cellular microcompartment; label-only) (kurkela2024inorganiccarbonsensing pages 1-2)
- CODH/ACS (carbon monoxide dehydrogenase/acetyl-CoA synthase complex; EC label needs subunit-specific mapping) (bae2024harnessingacetogenicbacteria pages 1-2)
- hydrogen-dependent CO2 reductase (HDCR; label-only) and hydrogenases implicated in acetogen electron flow (moon2024redirectingelectronflow pages 1-2)

#### Chemicals / substrates
- CO2 (CHEBI:16526)
- HCO3− bicarbonate (CHEBI:17544)
- CO (CHEBI:17245)
- H2 (CHEBI:18276)
- acetyl-CoA (CHEBI:15351)
- succinate (CHEBI:15741)

#### Environmental / experimental factors
- environmental pH (ENVO label-only) (scott2024widespreaddissolvedinorganic pages 7-10)
- O2 availability / oxic vs anoxic constraints (important for pathway choice; e.g., WLP oxygen sensitivity in pathway syntheses) (li2024productionofsuccinate pages 1-2, gruterich2024metagenomicandmetatranscriptomic pages 21-23)
- CO2 availability (e.g., low-CO2 vs high-CO2 conditions for CCM relevance) (wieschollek2024anewtype pages 1-2)
- flooding/water content in soils (ENVO label-only; affects phototrophic contributions) (liao2023microbialautotrophyexplains pages 9-10)

### Candidate causal edges (evidence-backed)
The following edge table is designed for direct translation into TraitMech-style YAML after selecting which edges are sufficiently general (vs taxon-specific, engineered, or ecological).

| Edge (subject–predicate–object) | Node grounding suggestions (CURIEs where available) | Evidence snippet (short quote) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|
| environmental_pH — determines_speciation_of — dissolved_inorganic_carbon | ENVO:environmental material [label-only context]; CHEBI:16526 carbon dioxide; CHEBI:17544 bicarbonate; CHEBI:18367 carbonate | “CO2 predominates below ~pH 6.4, HCO3− at circumneutral pH, and CO32− above ~pH 10.3” (scott2024widespreaddissolvedinorganic pages 7-10) | Scott et al., doi:10.1128/AEM.01557-23, 2024, https://doi.org/10.1128/AEM.01557-23 | Strong general edge for autotrophy because DIC form availability constrains uptake and fixation route choice. |
| bicarbonate_transporter_SbtA/BicA/BCT1 — enables — carbon_concentrating_mechanism | UniProt/GO label-only: SbtA, BicA, BCT1; GO:0015701 bicarbonate transport; GO:0033340 response to carbon dioxide | “The CCM includes bicarbonate transporters SbtA, BicA and BCT1” (kurkela2024inorganiccarbonsensing pages 1-2) | Kurkela & Tyystjärvi, doi:10.1111/ppl.14140, 2024, https://doi.org/10.1111/ppl.14140 | Strong for cyanobacteria; taxon-scoped to cyanobacterial CCM unless broadened with additional sources. |
| NDH-13/NDH-14_complex — converts — CO2_to_HCO3−_in_cytoplasm | GO label-only: NDH-13, NDH-14; CHEBI:16526; CHEBI:17544 | “specialized NDH complexes NDH-13 and NDH-14, which convert CO2 to HCO3− in the cytoplasm” (kurkela2024inorganiccarbonsensing pages 1-2) | Kurkela & Tyystjärvi, doi:10.1111/ppl.14140, 2024, https://doi.org/10.1111/ppl.14140 | Strong, cyanobacteria-focused mechanistic edge upstream of CCM-mediated autotrophy. |
| carboxysome — contains — RubisCO | GO label-only: carboxysome; EC:4.1.1.39 RuBisCO; gene labels rbcL/rbcS, cbbL/cbbS | “carboxysomes that are protein shell encapsulated ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCo)” (kurkela2024inorganiccarbonsensing pages 1-2) | Kurkela & Tyystjärvi, doi:10.1111/ppl.14140, 2024, https://doi.org/10.1111/ppl.14140 | Strong and broadly curatable for cyanobacterial/proteobacterial CBB autotrophs. |
| carboxysome — contains — carbonic_anhydrase | GO label-only: carboxysome; EC:4.2.1.1 carbonic anhydrase | “Carboxysomes contain two key enzymes: (i) carbonic anhydrase (CA) … and (ii) RubisCO” (wieschollek2024anewtype pages 1-2) | Wieschollek et al., doi:10.1128/AEM.01075-24, 2024, https://doi.org/10.1128/AEM.01075-24 | Strong for carboxysome-based CCMs. |
| carbonic_anhydrase — converts — HCO3−_to_CO2 | EC:4.2.1.1; CHEBI:17544 bicarbonate; CHEBI:16526 carbon dioxide | “When cytoplasmic HCO3− enters carboxysomes, CA converts it to CO2, and it is fixed by RubisCO” (wieschollek2024anewtype pages 1-2) | Wieschollek et al., doi:10.1128/AEM.01075-24, 2024, https://doi.org/10.1128/AEM.01075-24 | Strong direct biochemical edge. |
| RubisCO — fixes — CO2 | EC:4.1.1.39; gene labels rbcL/rbcS, cbbL/cbbS; CHEBI:16526 | “RubisCO, which uses CO2 as its substrate to carboxylate ribulose 1,5-bisphosphate” (wieschollek2024anewtype pages 1-2) | Wieschollek et al., doi:10.1128/AEM.01075-24, 2024, https://doi.org/10.1128/AEM.01075-24 | Core autotrophy edge for CBB users. |
| cytoplasmic_HCO3−_accumulation — supplies_substrate_to — carboxysomal_CO2_fixation | CHEBI:17544; GO label-only: carboxysome, carbon fixation | “CA, together with transporters and CO2-active systems, ‘generate elevated intracellular HCO3− concentrations.’ HCO3− is delivered into carboxysomes” (scott2024widespreaddissolvedinorganic pages 2-4) | Scott et al., doi:10.1128/AEM.01557-23, 2024, https://doi.org/10.1128/AEM.01557-23 | Mechanistic integrator edge; wording synthesized from review summary, but well supported. |
| iota_carboxysomal_CA — required_for — low_CO2_growth_in_Thiomicrospira_pelophila | EC:4.2.1.1 [family iota-CA label-only]; NCBITaxon label-only: Thiomicrospira pelophila | “When the gene encoding ιCA was interrupted in T. pelophila, cells could no longer grow under low-CO2 conditions” (wieschollek2024anewtype pages 1-2) | Wieschollek et al., doi:10.1128/AEM.01075-24, 2024, https://doi.org/10.1128/AEM.01075-24 | Strong but taxon-specific; should be marked organism-specific in TraitMech. |
| iota_carboxysomal_CA — required_for — carboxysomal_CA_activity | EC:4.2.1.1 [iota-CA label-only] | “CA activity was no longer detectable in their carboxysomes” after ιCA interruption (wieschollek2024anewtype pages 1-2) | Wieschollek et al., doi:10.1128/AEM.01075-24, 2024, https://doi.org/10.1128/AEM.01075-24 | Strong taxon-specific evidence linking gene to molecular function. |
| Wood–Ljungdahl_pathway — fixes — CO2_to_acetyl-CoA | MetaCyc/KEGG label-only: Wood–Ljungdahl pathway; CHEBI:16526; CHEBI:15351 acetyl-CoA | “two CO2 molecules to acetyl-CoA via the WLP” and “requires one ATP molecule and eight electrons” (bae2024harnessingacetogenicbacteria pages 1-2) | Bae et al., doi:10.1039/D4CB00099D, 2024, https://doi.org/10.1039/D4CB00099D | Strong pathway-level edge for acetogenic autotrophy. |
| CODH/ACS — catalyzes_terminal_step_of — Wood–Ljungdahl_CO2_fixation | EC label-only: carbon monoxide dehydrogenase/acetyl-CoA synthase complex; gene labels cooS/acs/codh-acs | “CO dehydrogenase/acetyl-CoA synthase (CODH/ACS), resulting in acetyl-CoA” (bae2024harnessingacetogenicbacteria pages 1-2) | Bae et al., doi:10.1039/D4CB00099D, 2024, https://doi.org/10.1039/D4CB00099D | Strong enzymatic edge, though exact subunit grounding may vary by taxon. |
| H2 — provides_reducing_equivalents_for — Wood–Ljungdahl_pathway | CHEBI:18276 molecular hydrogen; pathway label-only | “As CO2 is fully oxidized, H2 or CO must be utilized as an energy source to provide these reducing equivalents” (bae2024harnessingacetogenicbacteria pages 1-2) | Bae et al., doi:10.1039/D4CB00099D, 2024, https://doi.org/10.1039/D4CB00099D | Strong but pathway-context dependent; applies to acetogenic growth modes using H2. |
| CO_oxidation — provides_electrons_for — acetogenesis_from_CO | CHEBI:17245 carbon monoxide; CHEBI:16526 carbon dioxide; pathway label-only: acetogenesis | “some acetogenic … microbes can couple CO oxidation to CO2 reduction to acetate” (moon2024redirectingelectronflow pages 1-2) | Moon et al., doi:10.1038/s41467-024-49680-5, 2024, https://doi.org/10.1038/s41467-024-49680-5 | Strong for CO-based acetogenesis; not universal to all autotrophs. |
| high-affinity_H2/CO_oxidation — provides_electrons_and_ATP_for — Calvin-Benson-Bassham_cycle | gene labels hhyL, coxL, rbcL1E; GO label-only: ATP synthesis coupled electron transport; CBB cycle label-only | “liberate electrons that feed the electron transport chain, producing ATP which can drive the CBB cycle” (ray2023clearingtheair pages 2-4) | Ray et al., doi:10.1128/MMBR.00048-23, 2023, https://doi.org/10.1128/MMBR.00048-23 | Useful chemoautotrophy edge for atmospheric chemosynthesis; currently best curated as contextual/uncertain because direct fixation linkage remains disputed in review. |
| paddy_soil_environment — associated_with_higher — CO2_fixation_rate | ENVO label-only: paddy soil, upland soil, forest soil | “Paddy soils … display four-fold of CO2 fixation rates over upland and forest soils” (from paper abstract summary in search result) and “autotrophic microorganisms were more important in paddy soils (53%)” (liao2023microbialautotrophyexplains pages 6-7) | Liao et al., doi:10.1111/GCB.16452, 2023, https://doi.org/10.1111/GCB.16452 | Strong ecological association, but environmental-context edge rather than core cellular mechanism. Use cautiously in TraitMech if graph is phenotype-mechanism focused. |
| phototrophic_protists_in_paddy_soils — positively_associated_with — CO2_fixation_rate | label-only: phototrophic protists; possible NCBITaxon labels Chlorophyceae, Trebouxiophyceae | “higher contribution of phototrophic protists to CO2 fixation was observed in paddy soils” and “up to 21% contribution of phototrophic protists to C storage in paddy soils” (liao2023microbialautotrophyexplains pages 6-7, liao2023microbialautotrophyexplains pages 9-10) | Liao et al., doi:10.1111/GCB.16452, 2023, https://doi.org/10.1111/GCB.16452 | Ecological association, not a universal microbial-autotrophy mechanism; may be out-of-scope for a generic trait graph. |
| flooding/high_water_content — enhances — photosynthetic_C_fixation_in_paddy_soils | ENVO label-only: flooding; GO label-only: photosynthetic carbon fixation | “significantly higher C fixation rates under flooding than well-drained conditions” (liao2023microbialautotrophyexplains pages 9-10) | Liao et al., doi:10.1111/GCB.16452, 2023, https://doi.org/10.1111/GCB.16452 | Environment/assay-specific; useful context node, not a universal edge for autotrophy. |
| partial_3HP_cycle_engineering_in_Cupriavidus_necator_H16 — enables — CO2_dependent_succinate_production | NCBITaxon:Cupriavidus necator [label if exact CURIE unavailable]; pathway label-only: 3HP cycle; CHEBI:15741 succinate | “drive CO2 fixation to produce succinate through a portion of the 3-hydroxypropionate (3HP) cycle” (li2024productionofsuccinate pages 1-2) | Li et al., doi:10.1186/S12934-024-02470-6, 2024, https://doi.org/10.1186/S12934-024-02470-6 | Engineered-system edge; not native trait mechanism, so should be flagged non-native/synthetic. |
| engineered_3HP_succinate_pathway — incorporates — two_CO2_per_succinate | CHEBI:16526; CHEBI:15741; CHEBI:15351 acetyl-CoA | “single succinate molecule from one acetyl-CoA molecule and two CO2 molecules… 50% of the carbon atoms present in succinate are derived from CO2” (li2024productionofsuccinate pages 1-2) | Li et al., doi:10.1186/S12934-024-02470-6, 2024, https://doi.org/10.1186/S12934-024-02470-6 | Quantitative engineered-pathway edge; useful for applications section, not native TraitMech curation. |


*Table: This table compiles evidence-backed candidate causal edges for the microbial trait autotrophic (METPO:1000632), emphasizing mechanistic entities, environmental context, and curation-relevant uncertainty. It is useful as a starting point for selecting which edges are generic enough for TraitMech versus which are taxon-specific, ecological, or engineered-system claims.*

### Expert interpretation and curation guidance (what to curate vs defer)
1. **Core, broadly curatable mechanistic spine** for autotrophy across many microbes:
   - CO2/HCO3− availability (DIC speciation) → uptake/conversion modules (CA/transporters) → carboxylation enzyme activity (RuBisCO or alternative carboxylases) → biomass carbon assimilation. The pH→DIC speciation edge and the CCM/carboxysome edges are high-value because they connect **environmental availability** to **molecular capacity**. (scott2024widespreaddissolvedinorganic pages 7-10, kurkela2024inorganiccarbonsensing pages 1-2, wieschollek2024anewtype pages 1-2)
2. **Taxon-specific but strong gene→function→phenotype edges**:
   - ιCA requirement for low-CO2 growth in *T. pelophila* is excellent for mechanistic curation but should be tagged as **organism- or clade-scoped** (not a universal CCM component). (wieschollek2024anewtype pages 1-2)
3. **Ecological association edges** (use with caution for TraitMech):
   - Soil-scale CO2 fixation differences (paddy vs upland/forest) and protist contributions are important for “real-world implementation” and statistics, but they describe **community/ecosystem outcomes** rather than cell-intrinsic mechanisms. Keep them as optional environment/context nodes or curate into a separate ecological layer if TraitMech is intended to remain cell-mechanistic. (liao2023microbialautotrophyexplains pages 6-7, liao2023microbialautotrophyexplains pages 9-10)
4. **Engineered-system edges**:
   - Succinate production via partial 3HP module in *C. necator* is a strong application example but is not itself evidence that the organism is natively autotrophic; curate as engineered application edges with a “synthetic” flag. (li2024productionofsuccinate pages 1-2)
5. **Uncertain/contested links**:
   - Atmospheric chemosynthesis: the review provides mechanistic plausibility and quantitative trace-gas kinetics but also emphasizes that the “direct link” between trace gas oxidation and carbon fixation remains disputable. These edges should be marked **uncertain** unless corroborated with direct net-fixation experiments in the target system. (ray2023clearingtheair pages 2-4)

### DOI-first bibliography (with URLs and publication dates)
- Scott KM, Payne RR, Gahramanova A. **Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic Bacteria and Archaea…** *Applied and Environmental Microbiology* (Feb 2024). DOI: **10.1128/aem.01557-23**. https://doi.org/10.1128/aem.01557-23 (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 7-10)
- Kurkela J, Tyystjärvi T. **Inorganic carbon sensing and signalling in cyanobacteria.** *Physiologia Plantarum* (Accepted Dec 12, 2023; published 2024). DOI: **10.1111/ppl.14140**. https://doi.org/10.1111/ppl.14140 (kurkela2024inorganiccarbonsensing pages 1-2)
- Wieschollek J, Fuller D, Gahramanova A, et al. **A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments.** *Applied and Environmental Microbiology* (Published Aug 23, 2024). DOI: **10.1128/aem.01075-24**. https://doi.org/10.1128/aem.01075-24 (wieschollek2024anewtype pages 1-2, wieschollek2024anewtype media 33d6b164)
- Ray AE, Tribbia DZ, Cowan DA, Ferrari BC. **Clearing the air: unraveling past and guiding future research in atmospheric chemosynthesis.** *Microbiology and Molecular Biology Reviews* (Dec 2023). DOI: **10.1128/mmbr.00048-23**. https://doi.org/10.1128/mmbr.00048-23 (ray2023clearingtheair pages 2-4)
- Bae J, Park C, Jung H, Jin S, Cho B-K. **Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production.** *RSC Chemical Biology* (Accepted Jul 6, 2024; 2024). DOI: **10.1039/d4cb00099d**. https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 1-2, bae2024harnessingacetogenicbacteria pages 10-12)
- Moon J, Poehlein A, Daniel R, Müller V. **Redirecting electron flow in Acetobacterium woodii enables growth on CO…** *Nature Communications* (Accepted Jun 14, 2024; 2024). DOI: **10.1038/s41467-024-49680-5**. https://doi.org/10.1038/s41467-024-49680-5 (moon2024redirectingelectronflow pages 1-2)
- Liao H, Hao X, Qin F, et al. **Microbial autotrophy explains large-scale soil CO2 fixation.** *Global Change Biology* (Oct 2023). DOI: **10.1111/gcb.16452**. https://doi.org/10.1111/gcb.16452 (liao2023microbialautotrophyexplains pages 6-7, liao2023microbialautotrophyexplains pages 9-10)
- Li L, Zhou X, Gao Z, Xiong P, Liu X. **Production of succinate with two CO2 fixation reactions from fatty acids in Cupriavidus necator H16.** *Microbial Cell Factories* (Jul 2024). DOI: **10.1186/s12934-024-02470-6**. https://doi.org/10.1186/s12934-024-02470-6 (li2024productionofsuccinate pages 1-2)
- Lucius S, Hagemann M. **The primary carbon metabolism in cyanobacteria and its regulation.** *Frontiers in Plant Science* (Jul 2024). DOI: **10.3389/fpls.2024.1417680**. https://doi.org/10.3389/fpls.2024.1417680 (lucius2024theprimarycarbon pages 1-2)
- Wang G-G, Yuan Z, Wang X-Y, Zhang G-L. **Microbial Conversion and Utilization of CO2.** *Annals of Civil and Environmental Engineering* (Sep 2023). DOI: **10.29328/journal.acee.1001055**. https://doi.org/10.29328/journal.acee.1001055 (wang2023microbialconversionand pages 7-8)

### Warnings (claims not ready for TraitMech curation)
- **Atmospheric chemosynthesis**: mechanistically plausible but explicitly disputed linkage between trace gas oxidation and net carbon fixation; curate as **uncertain** unless direct fixation evidence is added. (ray2023clearingtheair pages 2-4)
- **Ecosystem-level soil edges** (paddy vs upland/forest): strong associations but may not be appropriate if TraitMech is strictly cell-mechanistic; consider separate ecological graph layer. (liao2023microbialautotrophyexplains pages 6-7, liao2023microbialautotrophyexplains pages 9-10)
- **Engineered succinate pathway**: application evidence; not a native autotrophy marker; tag as synthetic/engineered. (li2024productionofsuccinate pages 1-2)


References

1. (wang2023microbialconversionand pages 7-8): Ge-Ge Wang, Zhang Yuan, Xiao-Yan Wang, and Gen-Lin Zhang. Microbial conversion and utilization of co2. Annals of Civil and Environmental Engineering, 7:045-060, Sep 2023. URL: https://doi.org/10.29328/journal.acee.1001055, doi:10.29328/journal.acee.1001055. This article has 3 citations.

2. (scott2024widespreaddissolvedinorganic pages 1-2): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

3. (li2024productionofsuccinate pages 1-2): Linqing Li, Xiuyuan Zhou, Zhuoao Gao, Peng Xiong, and Xiutao Liu. Production of succinate with two co2 fixation reactions from fatty acids in cupriavidus necator h16. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02470-6, doi:10.1186/s12934-024-02470-6. This article has 11 citations and is from a peer-reviewed journal.

4. (ray2023clearingtheair pages 2-4): Angelique E. Ray, Dana Z. Tribbia, Don A. Cowan, and Belinda C. Ferrari. Clearing the air: unraveling past and guiding future research in atmospheric chemosynthesis. Microbiology and Molecular Biology Reviews, Dec 2023. URL: https://doi.org/10.1128/mmbr.00048-23, doi:10.1128/mmbr.00048-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

5. (scott2024widespreaddissolvedinorganic pages 7-10): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

6. (kurkela2024inorganiccarbonsensing pages 1-2): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 23 citations and is from a peer-reviewed journal.

7. (scott2024widespreaddissolvedinorganic pages 2-4): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

8. (gruterich2024metagenomicandmetatranscriptomic pages 21-23): CL Grüterich. Metagenomic and metatranscriptomic insights into wetland plant-microbe interactions and dark co2 fixation. Unknown journal, 2024.

9. (wieschollek2024anewtype pages 1-2): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

10. (wieschollek2024anewtype media 33d6b164): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

11. (wieschollek2024anewtype media d5c01eee): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

12. (wieschollek2024anewtype media 023b26e3): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

13. (wieschollek2024anewtype media 9979b826): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

14. (wieschollek2024anewtype media cebe6107): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

15. (wieschollek2024anewtype media 95ec58ec): Jana Wieschollek, Daniella Fuller, Arin Gahramanova, Terrence Millen, Ashianna J. Mislay, Ren R. Payne, Daniel P. Walsh, YuXuan Zhao, Madilyn Carney, Jaden Cross, John Kashem, Ruchi Korde, Christine Lacy, Noah Lyons, Tori Mason, Kayla Torres-Betancourt, Tyler Trapnell, Clare L. Dennison, Dale Chaput, and Kathleen M. Scott. A new type of carboxysomal carbonic anhydrase in sulfur chemolithoautotrophs from alkaline environments. Sep 2024. URL: https://doi.org/10.1128/aem.01075-24, doi:10.1128/aem.01075-24. This article has 8 citations and is from a peer-reviewed journal.

16. (bae2024harnessingacetogenicbacteria pages 1-2): Jiyun Bae, Chanho Park, Hyunwoo Jung, Sangrak Jin, and Byung-Kwan Cho. Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production. RSC Chemical Biology, 5:812-832, Jul 2024. URL: https://doi.org/10.1039/d4cb00099d, doi:10.1039/d4cb00099d. This article has 19 citations and is from a peer-reviewed journal.

17. (moon2024redirectingelectronflow pages 1-2): Jimyung Moon, Anja Poehlein, Rolf Daniel, and Volker Müller. Redirecting electron flow in acetobacterium woodii enables growth on co and improves growth on formate. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49680-5, doi:10.1038/s41467-024-49680-5. This article has 8 citations and is from a highest quality peer-reviewed journal.

18. (bae2024harnessingacetogenicbacteria pages 10-12): Jiyun Bae, Chanho Park, Hyunwoo Jung, Sangrak Jin, and Byung-Kwan Cho. Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production. RSC Chemical Biology, 5:812-832, Jul 2024. URL: https://doi.org/10.1039/d4cb00099d, doi:10.1039/d4cb00099d. This article has 19 citations and is from a peer-reviewed journal.

19. (liao2023microbialautotrophyexplains pages 6-7): Hao Liao, Xiuli Hao, Fei Qin, Manuel Delgado‐Baquerizo, Yurong Liu, Jizhong Zhou, Peng Cai, Wenli Chen, and Qiaoyun Huang. Microbial autotrophy explains large‐scale soil co2 fixation. Global Change Biology, 29:231-242, Oct 2023. URL: https://doi.org/10.1111/gcb.16452, doi:10.1111/gcb.16452. This article has 107 citations and is from a highest quality peer-reviewed journal.

20. (liao2023microbialautotrophyexplains pages 9-10): Hao Liao, Xiuli Hao, Fei Qin, Manuel Delgado‐Baquerizo, Yurong Liu, Jizhong Zhou, Peng Cai, Wenli Chen, and Qiaoyun Huang. Microbial autotrophy explains large‐scale soil co2 fixation. Global Change Biology, 29:231-242, Oct 2023. URL: https://doi.org/10.1111/gcb.16452, doi:10.1111/gcb.16452. This article has 107 citations and is from a highest quality peer-reviewed journal.

21. (lucius2024theprimarycarbon pages 1-2): Stefan Lucius and Martin Hagemann. The primary carbon metabolism in cyanobacteria and its regulation. Frontiers in Plant Science, Jul 2024. URL: https://doi.org/10.3389/fpls.2024.1417680, doi:10.3389/fpls.2024.1417680. This article has 88 citations.