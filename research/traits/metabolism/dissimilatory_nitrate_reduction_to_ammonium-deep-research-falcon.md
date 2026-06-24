---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:40:54.613090'
end_time: '2026-06-18T04:50:39.940386'
duration_seconds: 585.33
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dissimilatory nitrate reduction to ammonium
  trait_identifier: traitmech:000030
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dissimilatory_nitrate_reduction_to_ammonium
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which nitrate is reduced via
    nitrite to ammonium (rather than to N2), conserving fixed nitrogen within the
    ecosystem. It is favored over denitrification under nitrate-limited, high-electron-donor
    conditions.
  parent_traits: METPO:1000802
  synonyms: DNRA, nitrate ammonification
  evidence_summary: 'DOI:10.1126/science.1254070:  (Kraft et al. show the donor-to-acceptor
    ratio governs whether nitrate respiration ends in ammonium (DNRA) or N2 (denitrification).)
    | DOI:10.1007/s11157-025-09719-5:  (Review of DNRA vs denitrification supports
    DNRA''s competitive advantage and nitrogen-retaining role under nitrate-limited
    conditions.)'
  causal_graph_summary: 'dnra_nitrate_to_ammonium: 4 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory nitrate reduction to ammonium
- **METPO identifier:** traitmech:000030
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which nitrate is reduced via nitrite to ammonium (rather than to N2), conserving fixed nitrogen within the ecosystem. It is favored over denitrification under nitrate-limited, high-electron-donor conditions.
- **Parent traits:** METPO:1000802
- **Synonyms:** DNRA, nitrate ammonification
- **Existing evidence:** DOI:10.1126/science.1254070:  (Kraft et al. show the donor-to-acceptor ratio governs whether nitrate respiration ends in ammonium (DNRA) or N2 (denitrification).) | DOI:10.1007/s11157-025-09719-5:  (Review of DNRA vs denitrification supports DNRA's competitive advantage and nitrogen-retaining role under nitrate-limited conditions.)
- **Existing causal graph summary:** dnra_nitrate_to_ammonium: 4 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory nitrate reduction to ammonium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.yaml`.

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
- **Trait label:** dissimilatory nitrate reduction to ammonium
- **METPO identifier:** traitmech:000030
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which nitrate is reduced via nitrite to ammonium (rather than to N2), conserving fixed nitrogen within the ecosystem. It is favored over denitrification under nitrate-limited, high-electron-donor conditions.
- **Parent traits:** METPO:1000802
- **Synonyms:** DNRA, nitrate ammonification
- **Existing evidence:** DOI:10.1126/science.1254070:  (Kraft et al. show the donor-to-acceptor ratio governs whether nitrate respiration ends in ammonium (DNRA) or N2 (denitrification).) | DOI:10.1007/s11157-025-09719-5:  (Review of DNRA vs denitrification supports DNRA's competitive advantage and nitrogen-retaining role under nitrate-limited conditions.)
- **Existing causal graph summary:** dnra_nitrate_to_ammonium: 4 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory nitrate reduction to ammonium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.yaml`.

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


## Microbial TraitMech Curation Report: Dissimilatory nitrate reduction to ammonium (DNRA)

**Target trait:** dissimilatory nitrate reduction to ammonium (DNRA)  
**METPO identifier:** traitmech:000030  
**Synonyms:** nitrate ammonification, respiratory ammonification  

### 1) Scope summary (trait definition, boundaries, and readouts)

**Definition / current understanding.** DNRA is a dissimilatory (energy-conserving) nitrate/nitrite respiratory pathway in which **nitrate (NO3−) is reduced to nitrite (NO2−) and then to ammonium (NH4+)**, retaining fixed nitrogen in the system rather than releasing it as gaseous N species. The mechanistic two-step framing (2-e− NO3−→NO2−; 6-e− NO2−→NH4+) and the nitrogen-retaining contrast with denitrification are explicitly described in a recent mechanistic paper that also distinguishes assimilation and catalogs enzyme options for each step. (egas2024anovelmechanism pages 1-2)

**Boundary cases / nearby traits.**
- **Denitrification**: reduces nitrate/nitrite to gaseous nitrogen products (NO, N2O, N2), causing N loss from ecosystems; DNRA retains N as NH4+. The competing pathways share the same substrates and **nitrite is the shared nodal intermediate**, driving competition for NOx. (wu2024aerobiccarbonmetabolism pages 1-5, kostyuk2024mathematicalmodellingof pages 8-12)
- **Assimilatory nitrate/nitrite reduction**: reduces nitrate/nitrite to ammonium for biosynthesis, not primarily for energy conservation. In the DNRA-focused Acididesulfobacillus study, the authors explicitly differentiate dissimilatory vs assimilatory nitrite reductases and list known assimilatory enzymes (NasB, NirA, NirB). (egas2024anovelmechanism pages 1-2)
- **Noncanonical DNRA routes**: the 2024 mSystems study demonstrates DNRA phenotype in an organism lacking recognized nitrite reductase genes, implying that “DNRA” as a trait should be phenotypically defined (NO3−/NO2−→NH4+ in respiration) rather than strictly by canonical gene presence. (egas2024anovelmechanism pages 2-5)

**Recommended assay/readout scope for TraitMech curation.**
- **Process rate**: ^15N isotope tracer (e.g., Na^15NO3 in slurries) with measurement of ^15NH4+ formation for potential DNRA. (yuan2024spatiotemporalpatternsand pages 4-5)
- **Stoichiometric end-products**: accumulation/production of NH4+ (and monitoring nitrite/NO as intermediates). (egas2024anovelmechanism pages 2-5)
- **Functional gene abundance and expression**: **nrfA** as a key DNRA nitrite reductase marker (with caveats for noncanonical pathways); qPCR and nrfA amplicon sequencing commonly used. (yuan2024spatiotemporalpatternsand pages 4-5, wu2024aerobiccarbonmetabolism pages 1-5)
- **Boundary indicators**: N2O/N2 production (denitrification), and presence of assimilatory nitrite reductase systems when interpreting genomes. (egas2024anovelmechanism pages 1-2)

### 2) Key concepts and mechanistic entities (candidate nodes)

Below are candidate nodes for a TraitMech causal graph. Grounding is suggested where stable identifiers are clear; otherwise nodes are listed as label-only candidates for later curation.

#### A. Pathways / modules
- **DNRA module (NO3−→NO2−→NH4+)** (trait-level module): DNRA is defined as nitrate reduction via nitrite to ammonium. (egas2024anovelmechanism pages 1-2)
- **Nitrate reduction (first step)**: periplasmic NapAB or cytoplasmic NarGHI as nitrate reductase options. (egas2024anovelmechanism pages 1-2)
- **Nitrite ammonification (second step)**: cytochrome c nitrite reductase **NrfA** (canonical), often with redox partner **NrfH** in some systems. (hird2025fromgenesto pages 11-13)
- **Noncanonical nitrite-to-ammonium reduction candidates**: AsrABC (anaerobic sulfite reductase-like activity) and a putative ferredoxin-dependent NirA homolog (DEACI_1836) proposed in Acididesulfobacillus acetoxydans. (egas2024anovelmechanism pages 2-5, egas2024anovelmechanism pages 9-10)

#### B. Genes / proteins / complexes (labels; add UniProt/EC/GO as available during curation)
- **narGHI** (membrane-bound nitrate reductase complex; nitrate→nitrite). Strongly upregulated in nitrate-reducing vs sulfate-reducing conditions in Acididesulfobacillus. (egas2024anovelmechanism pages 2-5)
- **napAB / nap operon** (periplasmic nitrate reductase; nitrate→nitrite). Operon-level description in DNRA gene-to-function review. (hird2025fromgenesto pages 11-13)
- **narK** (nitrate/nitrite transporter) implicated in Acididesulfobacillus nitrate respiration context. (egas2024anovelmechanism pages 2-5)
- **nrfA** (cytochrome c nitrite reductase; NO2−→NH4+). Central DNRA marker and enzyme. (hird2025fromgenesto pages 11-13)
- **nrfH** (redox partner for NrfA in some systems). (hird2025fromgenesto pages 11-13)
- **asrABC** (anaerobic sulfite reductase-like; proposed nitrite reductase activity in noncanonical DNRA). (egas2024anovelmechanism pages 2-5, egas2024anovelmechanism pages 9-10)
- **hcp** (hybrid cluster protein; proposed high-affinity NO reductase for nitrosative stress management). (egas2024anovelmechanism pages 2-5, egas2024anovelmechanism pages 9-10)
- **nosZ** (N2O reductase; upregulated in Acididesulfobacillus; relevant as side-pathway to close N balance under nitrosative stress). (egas2024anovelmechanism pages 9-10)
- **Regulators**: FNR (O2/NO-sensing), NarX-NarL and NarQ-NarP (nitrate/nitrite sensing) regulating nap/nrf expression. (hird2025fromgenesto pages 11-13)

#### C. Chemicals / metabolites / electron donors & acceptors
- **Electron acceptors**: nitrate (CHEBI:17632), nitrite (CHEBI:16301). (egas2024anovelmechanism pages 1-2)
- **End product**: ammonium (CHEBI:28938). (egas2024anovelmechanism pages 1-2)
- **Reactive intermediates / stress species**: nitric oxide (CHEBI:16480), hydroxylamine (mentioned as candidate intermediate), nitrous oxide (CHEBI:17045). (egas2024anovelmechanism pages 1-2, egas2024anovelmechanism pages 2-5, egas2024anovelmechanism pages 9-10)
- **Electron donors (contextual)**: labile organic carbon such as glucose (CHEBI:17234) used to shift pathway partitioning in soils; dissolved organic carbon (DOC) and DOC/NO3 ratio used as driver. (wu2024aerobiccarbonmetabolism pages 1-5, hong2024artificialcultivationof pages 8-11)
- **Electron carrier**: reduced ferredoxin (label-only) proposed to supply electrons to the DEACI_1836 nitrite reduction step in Acididesulfobacillus; linked to pyruvate ferredoxin oxidoreductase (Pfor, label-only). (egas2024anovelmechanism pages 9-10)

#### D. Environmental / experimental factors (candidate nodes)
- Oxygen regime / history (aerobic preincubation vs direct anoxia) (wu2024aerobiccarbonmetabolism pages 1-5)
- DOC/NO3− ratio (hong2024artificialcultivationof pages 8-11)
- ORP / redox and conductivity and TOC (rhizosphere drivers) (hong2024artificialcultivationof pages 8-11)
- Temperature, water depth, reservoir age (field drivers for DNRA rates) (yuan2024spatiotemporalpatternsand pages 7-10)
- Nitrite accumulation (inhibitory threshold; organism-specific) (egas2024anovelmechanism pages 2-5)

### 3) Recent developments and latest research (2023–2024 priority)

#### 3.1. Field-scale quantification of DNRA rates and gene abundance (2024)
A 2024 reservoir-sediment study used ^15N tracer slurry incubations to quantify DNRA potentials and paired these with nrfA qPCR. Reported **potential DNRA rates were 0.01–0.15 nmol-N cm−3 h−1** and **nrfA abundance ranged from 1.08×10^5 to 2.51×10^6 copies g−1 dry weight**, with slightly higher summer vs winter means. (egas2024anovelmechanism pages 1-2, yuan2024spatiotemporalpatternsand pages 4-5)

They also report correlations consistent with mechanistic expectations: potential DNRA rate correlates positively with NH4+-N (R=0.602) and temperature (R=0.497), and negatively with water depth (R=−0.429). (yuan2024spatiotemporalpatternsand pages 7-10)

#### 3.2. Plant-mediated reshaping of DNRA-associated communities (2024)
A 2024 drainage-ditch sediment study found that **aquatic plant cultivation increased nitrogen transformation and shifted functional gene family composition**, with functional annotation showing **dissimilatory nitrate reduction (DNRA) relative abundance 8.84–10.46%** and denitrification 13.89–18.61% (annotation-based). (hong2024artificialcultivationof pages 8-11)

The same study links DNRA-associated genera to electron-donor/acceptor balance: **Anaeromyxobacter and Geobacter were positively correlated with DOC/NO3−-N ratio and NH4+-N and negatively with NO3−-N**. (hong2024artificialcultivationof pages 8-11)

#### 3.3. Manipulating oxygen history and labile carbon to redirect NOx partitioning (2024)
A 2024 soil microcosm preprint suggests DNRA can be **substantially increased by aerobic carbon metabolism prior to anoxia**: with aerobic incubation plus labile carbon (glucose) followed by anaerobic incubation, **up to 55.8% of nitrite reduction shifted to DNRA**, with associated increases in DNRA-related genes (including nrfA assays and metagenomics). (wu2024aerobiccarbonmetabolism pages 1-5)

This is positioned against ecosystem heterogeneity where DNRA can be minor in some temperate systems (5–19% of nitrate reduction in some temperate freshwater/paddy soils) but dominant in others. (wu2024aerobiccarbonmetabolism pages 5-8)

#### 3.4. Expanding mechanistic repertoire: noncanonical DNRA route in an acidophilic sulfate reducer (2024)
A key 2024 mechanistic advance is the demonstration of DNRA in **Acididesulfobacillus acetoxydans** despite the genome lacking known nitrite reductase genes. The authors propose that nitrite→NH4+ reduction may proceed via **previously undescribed nitrite reductase activity of AsrABC and/or a ferredoxin-dependent NirA-like protein (DEACI_1836)**, supported by comparative transcriptomics/proteomics and intermediate measurements (transient NO, nitrite accumulation). (egas2024anovelmechanism pages 2-5, egas2024anovelmechanism pages 9-10)

Figures in this paper summarize the proposed pathway and highlight the upregulated proteins/genes used to build the mechanistic model. (egas2024anovelmechanism media 3da222ff, egas2024anovelmechanism media 6e971979)

### 4) Current applications and real-world implementations (from retrieved sources)

**Agricultural nitrogen retention strategies.** Both field and microcosm work motivate DNRA as a **nitrogen-conserving lever**: increasing DNRA fraction can retain N as NH4+ and potentially reduce denitrification-associated N loss. The 2024 upland soil microcosm proposes manipulating microbiota via carbon-oxygen regimes as a strategy for improving fertilizer use efficiency and lowering N loss. (wu2024aerobiccarbonmetabolism pages 1-5)

**Managed drainage ditches / nature-based solutions.** Aquatic plant cultivation in drainage ditches is presented as an in situ intervention that alters sediment microbial community structure and functional gene signatures (including DNRA-related fractions), suggesting a potentially actionable management approach for agricultural runoff nitrogen. (hong2024artificialcultivationof pages 8-11)

**Engineered treatment contexts (evidence in retrieved corpus is indirect).** A 2025 hydrogen-based reactor paper (retrieved but only partially evidenced in the excerpt) frames DNRA as relevant in engineered nitrate reduction contexts and cites multiple recent studies, but the excerpt available here does not provide direct quantitative DNRA performance metrics for the reactor itself. (zhao2025investigationofnitrogen pages 15-17)

### 5) Relevant statistics & data (recent studies)

Key quantitative findings are compiled below.

| Study (year) | System | Metric | Value (with units) | Notes |
|---|---|---|---|---|
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Potential DNRA rate, summer | 0.06 ± 0.02 nmol-N cm^-3 h^-1 | Slightly higher in summer than winter; measured by ^15N isotope tracing in sediment slurries (yuan2024spatiotemporalpatternsand pages 4-5) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Potential DNRA rate, winter | 0.05 ± 0.03 nmol-N cm^-3 h^-1 | Longitudinal decline downstream also reported (yuan2024spatiotemporalpatternsand pages 4-5) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | nrfA abundance, summer | 1.15 ± 0.22 × 10^6 copies g^-1 dry weight | Higher than winter; qPCR-based estimate (yuan2024spatiotemporalpatternsand pages 4-5) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | nrfA abundance, winter | 0.98 ± 0.08 × 10^6 copies g^-1 dry weight | Seasonal difference consistent with slightly higher summer DNRA potential (yuan2024spatiotemporalpatternsand pages 4-5) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Potential DNRA rate range | 0.01–0.15 nmol-N cm^-3 h^-1 | Reported study-wide range across sites/seasons (egas2024anovelmechanism pages 1-2) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | nrfA abundance range | 1.08 × 10^5–2.51 × 10^6 copies g^-1 dry weight | Reported study-wide range across sites/seasons (egas2024anovelmechanism pages 1-2) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Correlation of DNRA rate with NH4+-N | R = 0.602 | Positive correlation (yuan2024spatiotemporalpatternsand pages 7-10) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Correlation of DNRA rate with temperature | R = 0.497 | Positive correlation (yuan2024spatiotemporalpatternsand pages 7-10) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Correlation of DNRA rate with reservoir age | R = 0.436 | Positive correlation (yuan2024spatiotemporalpatternsand pages 7-10) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Correlation of DNRA rate with water depth | R = -0.429 | Negative correlation (yuan2024spatiotemporalpatternsand pages 7-10) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Dominant DNRA taxon abundance: Anaeromyxobacter | 4.52% average relative abundance | One of the most abundant nrfA-associated genera (yuan2024spatiotemporalpatternsand pages 7-10) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Dominant DNRA taxon abundance: Polyangium | 4.09% average relative abundance | Among top DNRA-associated genera (yuan2024spatiotemporalpatternsand pages 7-10) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Dominant DNRA taxon abundance: Archangium | 1.86% average relative abundance | Among top DNRA-associated genera (yuan2024spatiotemporalpatternsand pages 7-10) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Dominant DNRA taxon abundance: Geobacter | 1.34% average relative abundance | Among top DNRA-associated genera (yuan2024spatiotemporalpatternsand pages 7-10) |
| Yuan et al. (2024) | Surface sediments of Lancang River cascade reservoirs | Dominant DNRA taxon abundance: Lacunisphaera | 1.32% average relative abundance | Among top DNRA-associated genera (yuan2024spatiotemporalpatternsand pages 7-10) |
| Wu et al. (2024) | Agricultural upland soil microcosms | Shift of nitrite reduction to DNRA under aerobic incubation with labile C followed by anoxia | Up to 55.8% of nitrite reduction | Indicates strong promotion of DNRA by prior aerobic carbon metabolism (wu2024aerobiccarbonmetabolism pages 1-5) |
| Wu et al. (2024) | Agricultural upland soil / literature context | DNRA share of nitrate reduction in temperate freshwater and paddy soils | 5–19% of nitrate reduction | Reported as literature context showing DNRA can be minor in some systems (wu2024aerobiccarbonmetabolism pages 5-8, wu2024aerobiccarbonmetabolism pages 1-5) |
| Hong et al. (2024) | Rhizosphere sediments in agricultural drainage ditches with aquatic plant cultivation | Functional gene relative abundance: DNRA | 8.84–10.46% | NCyc functional annotation; plant cultivation shifted N-cycling community structure (hong2024artificialcultivationof pages 8-11) |
| Hong et al. (2024) | Rhizosphere sediments in agricultural drainage ditches with aquatic plant cultivation | Functional gene relative abundance: denitrification | 13.89–18.61% | Higher than DNRA in this dataset (hong2024artificialcultivationof pages 8-11) |
| Hong et al. (2024) | Rhizosphere sediments in agricultural drainage ditches with aquatic plant cultivation | Functional gene relative abundance: assimilatory nitrate reduction | 8.23–12.76% | Similar order of magnitude to DNRA (hong2024artificialcultivationof pages 8-11) |
| Hong et al. (2024) | Rhizosphere sediments in agricultural drainage ditches with aquatic plant cultivation | Example genus abundance: Anaeromyxobacter | 0.26–3.66% | Increased significantly in cultivated groups; associated with N cycling/DNRA (hong2024artificialcultivationof pages 8-11) |
| Hong et al. (2024) | Rhizosphere sediments in agricultural drainage ditches with aquatic plant cultivation | Example genus abundance: Pseudomonas | 0.22–2.22% | N-cycling-associated genus (hong2024artificialcultivationof pages 8-11) |
| Hong et al. (2024) | Rhizosphere sediments in agricultural drainage ditches with aquatic plant cultivation | Example genus abundance: Geobacter | 0.14–2.01% | Increased in cultivated groups; linked to DNRA-associated community shift (hong2024artificialcultivationof pages 8-11) |
| Hong et al. (2024) | Rhizosphere sediments in agricultural drainage ditches with aquatic plant cultivation | Example genus abundance: Thiobacillus | 0.11–1.65% | Increased in cultivated groups (hong2024artificialcultivationof pages 8-11) |
| Hong et al. (2024) | Rhizosphere sediments in agricultural drainage ditches with aquatic plant cultivation | Correlation of DNRA-associated genera with DOC/NO3^--N ratio and NH4+-N | Positive | Anaeromyxobacter and Geobacter were positively correlated with DOC/NO3^--N ratio and NH4+-N, negatively with NO3^--N (hong2024artificialcultivationof pages 8-11) |


*Table: This table compiles recent quantitative findings on DNRA activity, gene abundance, community composition, and environmental correlations from 2024 studies. It is useful for identifying candidate TraitMech nodes and evidence-backed environmental drivers for DNRA curation.*

### 6) Candidate causal edges (evidence-backed triples)

The following table contains **proposed causal edges** suitable for consideration in `dissimilatory_nitrate_reduction_to_ammonium.yaml`. Each edge includes a snippet and uncertainty notes.

| Edge (triple) | Evidence snippet (short quote) | Reference (DOI, year, URL) | Notes/uncertainty | Suggested ontology grounding (CURIEs where possible) |
|---|---|---|---|---|
| nitrate [CHEBI:17632] —is reduced to→ nitrite [CHEBI:16301] via NarGHI | “nitrate is reduced via nitrite… Known nitrate reductases include periplasmic NapAB and cytoplasmic NarGHI” (egas2024anovelmechanism pages 1-2) | 10.1128/msystems.00967-23 (2024) https://doi.org/10.1128/msystems.00967-23 | Supports canonical first DNRA step; source is general/mechanistic review within primary paper context. | CHEBI:17632 nitrate; CHEBI:16301 nitrite; NarGHI label-only candidate; GO:nitrate respiration (candidate) |
| nitrate [CHEBI:17632] —is reduced to→ nitrite [CHEBI:16301] via NapAB | “Known nitrate reductases include periplasmic NapAB and cytoplasmic NarGHI” (egas2024anovelmechanism pages 1-2) | 10.1128/msystems.00967-23 (2024) https://doi.org/10.1128/msystems.00967-23 | NapAB is a candidate first-step module for some DNRA taxa; taxon/context dependence should be preserved. | CHEBI:17632; CHEBI:16301; NapAB label-only candidate |
| nitrite [CHEBI:16301] —is reduced to→ ammonium [CHEBI:28938] via NrfA | “The second step of the pathway is performed by cytochrome c nitrite reductase (NrfA)… reduction of nitrite to ammonium” (hird2025fromgenesto pages 11-13) | 10.1128/aem.00292-25 (2025) https://doi.org/10.1128/aem.00292-25 | Strong support for canonical DNRA nitrite reductase. | CHEBI:16301; CHEBI:28938; NrfA label-only candidate; GO:nitrite reductase activity (candidate) |
| nrfA abundance —positively correlates with→ DNRA rate | “abundance of gene markers… DNRA (DNRA nitrite reductase nrfA)… with significant relationships between… DNRA and nrfA abundance” (wu2024aerobiccarbonmetabolism pages 5-8) | 10.3389/fmicb.2015.00542 (2015) https://doi.org/10.3389/fmicb.2015.00542 | Correlative, not necessarily causal; useful as an evidence-backed assay/biomarker edge. | nrfA label-only candidate; DNRA traitmech:000030 |
| high DOC/NO3 ratio —promotes→ DNRA-associated taxa (Anaeromyxobacter, Geobacter) | “Anaeromyxobacter and Geobacter positively correlated with DOC/NO3−-N ratio and NH4+-N and negatively with NO3−-N” (hong2024artificialcultivationof pages 8-11) | 10.3390/land13101557 (2024) https://doi.org/10.3390/land13101557 | Correlation in rhizosphere ditch sediments; taxa association stronger than direct process causation. | DOC label-only candidate; CHEBI:17632 nitrate; NCBITaxon:Anaeromyxobacter (candidate); NCBITaxon:Geobacter |
| aerobic carbon preincubation —increases→ DNRA share of nitrite reduction | “soils pre-incubated aerobically with added labile carbon… showed a marked rise in DNRA… up to 55.8% of nitrite reduction shifted to DNRA” (wu2024aerobiccarbonmetabolism pages 1-5) | 10.1101/2024.11.04.621907 (2024) https://doi.org/10.1101/2024.11.04.621907 | Preprint; assay-specific microcosm evidence, but directly useful for environmental-factor node/edge. | glucose [CHEBI:17234] candidate donor; aerobic preincubation label-only; DNRA traitmech:000030 |
| nitrite accumulation [CHEBI:16301] —inhibits→ growth of Acididesulfobacillus acetoxydans | “nitrite accumulation halts growth at ~0.8–1 mM” (egas2024anovelmechanism pages 2-5) | 10.1128/msystems.00967-23 (2024) https://doi.org/10.1128/msystems.00967-23 | Taxon-specific inhibition threshold; should be marked uncertain/generalization-limited. | CHEBI:16301; NCBITaxon:Acididesulfobacillus acetoxydans (candidate) |
| Hcp —reduces→ nitric oxide [CHEBI:16480] to nitrous oxide [CHEBI:17045] | “Hcp, highly abundant, likely functions as a high-affinity nitric oxide reductase converting NO to N2O and helping manage nitrosative stress” (egas2024anovelmechanism pages 9-10) | 10.1128/msystems.00967-23 (2024) https://doi.org/10.1128/msystems.00967-23 | Explicitly presented as likely/proposed in this organism; curate as uncertain and taxon-specific. | Hcp label-only candidate; CHEBI:16480 nitric oxide; CHEBI:17045 nitrous oxide |
| pyruvate ferredoxin oxidoreductase (Pfor) —supplies reduced ferredoxin to→ DEACI_1836-mediated nitrite reduction | “Reduced ferredoxin is supplied by pyruvate ferredoxin oxidoreductase (Pfor), linking central metabolism… to DNRA electron supply” (egas2024anovelmechanism pages 9-10) | 10.1128/msystems.00967-23 (2024) https://doi.org/10.1128/msystems.00967-23 | Strong mechanistic proposal in noncanonical DNRA; enzyme identity/function for DEACI_1836 remains inferred. | Pfor label-only candidate; ferredoxin label-only candidate; DEACI_1836 label-only candidate; CHEBI:16301 |
| DEACI_1836 —may reduce→ nitrite [CHEBI:16301] to ammonium [CHEBI:28938] | “DEACI_1836 contains ferredoxin-like and 4Fe-4S domains and is hypothesized to reduce nitrite to ammonia” (egas2024anovelmechanism pages 9-10) | 10.1128/msystems.00967-23 (2024) https://doi.org/10.1128/msystems.00967-23 | Noncanonical/taxon-specific and explicitly hypothesized; high uncertainty for graph curation. | DEACI_1836 label-only candidate; CHEBI:16301; CHEBI:28938 |
| NarX/NarL —activates expression of→ nap operon | “NarX-NarL and NarQ-NarP (nitrate/nitrite sensing) … activate transcription under appropriate conditions” (hird2025fromgenesto pages 11-13) | 10.1128/aem.00292-25 (2025) https://doi.org/10.1128/aem.00292-25 | Regulatory edge supported at system level; organism-specific details vary. | NarX label-only candidate; NarL label-only candidate; nap operon label-only candidate |
| NarX/NarL —activates expression of→ nrf operon | “Expression of nap and nrf operons is tightly regulated by… NarX-NarL and NarQ-NarP” (hird2025fromgenesto pages 11-13) | 10.1128/aem.00292-25 (2025) https://doi.org/10.1128/aem.00292-25 | Good generic regulation edge; taxon-specific promoter architecture may differ. | NarX; NarL; nrf operon label-only candidate |
| FNR —activates expression of→ nap/nrf operons under anaerobic conditions | “FNR (O2/NO sensing)… activate transcription under appropriate conditions (anaerobic and nitrate/nitrite-rich)” (hird2025fromgenesto pages 11-13) | 10.1128/aem.00292-25 (2025) https://doi.org/10.1128/aem.00292-25 | Regulatory scope broad but not universal; better curated as condition-dependent regulation. | FNR label-only candidate; ENVO:anaerobic environment (candidate); nap operon; nrf operon |


*Table: This table lists evidence-backed candidate subject–predicate–object edges for a DNRA TraitMech graph, emphasizing canonical pathway steps, environmental drivers, and regulatory mechanisms. It is useful for deciding which nodes and edges are strong enough for curation and which should remain uncertain or taxon-specific.*

### 7) Expert opinions / authoritative synthesis (from retrieved authoritative sources)

**Gene-to-function consensus for DNRA nitrite ammonification.** A 2025 review in *Applied and Environmental Microbiology* emphasizes that the DNRA second step is performed by **cytochrome c nitrite reductase NrfA**, describing its catalytic electron/proton demands and its genetic/regulatory context, including the nrf operons and common redox partners such as NrfH for some variants. (hird2025fromgenesto pages 11-13)

**Regulatory framing (oxygen and nitrate/nitrite sensing).** The same review highlights that DNRA-related operons (nap and nrf) are **tightly regulated by oxygen and nitrate/nitrite responsive regulators** including FNR and NarX/NarL-type systems, supporting explicit “environment→gene expression→pathway flux” edges for the causal graph (condition dependent). (hird2025fromgenesto pages 11-13)

**Mechanistic diversity beyond canonical gene sets.** The 2024 Acididesulfobacillus paper argues that DNRA potential can be missed by genome screening for canonical nitrite reductases, motivating cautious inference from gene content alone and supporting inclusion of “noncanonical enzyme candidates” nodes as uncertain. (egas2024anovelmechanism pages 2-5)

### 8) Ontology grounding suggestions (non-exhaustive)

**Chemicals (high confidence):**
- Nitrate: CHEBI:17632  
- Nitrite: CHEBI:16301  
- Ammonium: CHEBI:28938  
- Nitric oxide: CHEBI:16480  
- Nitrous oxide: CHEBI:17045  
- Glucose: CHEBI:17234  

**Environment (candidates; confirm exact ENVO terms during curation):** anaerobic environment; sediment; rhizosphere sediment; agricultural soil; reservoir sediment.

**Genes/proteins:** nrfA, nrfH, narGHI, napAB, narK, asrABC, hcp, nosZ, fnr, narX, narL (label-only in this report; map to UniProt/EC/GO as needed per taxon).

### 9) Warnings / curation cautions

1. **Correlation vs causation:** Several environmental and community edges are correlational (e.g., nrfA abundance vs DNRA rate; DOC/NO3 ratio vs taxa), and should be curated with “association” or “increases” predicates only if your schema supports it, or marked uncertain. (yuan2024spatiotemporalpatternsand pages 7-10, hong2024artificialcultivationof pages 8-11)
2. **Preprint evidence:** The 2024 upland soil study is a bioRxiv preprint; treat claims (e.g., 55.8% shift) as provisional unless validated by peer-reviewed follow-up. (wu2024aerobiccarbonmetabolism pages 1-5)
3. **Taxon-specific mechanisms:** The Acididesulfobacillus noncanonical nitrite reduction mechanism (AsrABC/DEACI_1836) is compelling but explicitly proposed/hypothesized and may not generalize; curate as organism-specific and uncertain. (egas2024anovelmechanism pages 9-10)
4. **Gene-marker incompleteness:** DNRA phenotype can occur without canonical nitrite reductase genes detectable by standard annotation; avoid using “nrfA present” as a strict necessary condition for DNRA across all taxa. (egas2024anovelmechanism pages 2-5)

---

## DOI-first bibliography (retrieved in this run)

1. **Egas RA, Kurth JM, Boeren S, et al.** *A novel mechanism for dissimilatory nitrate reduction to ammonium in Acididesulfobacillus acetoxydans.* **mSystems**. Published 2024-03. DOI: **10.1128/msystems.00967-23**. URL: https://doi.org/10.1128/msystems.00967-23 (egas2024anovelmechanism pages 1-2, egas2024anovelmechanism pages 2-5, egas2024anovelmechanism pages 9-10, egas2024anovelmechanism media 3da222ff, egas2024anovelmechanism media 6e971979)
2. **Yuan B, Guo M, Zhou X, Li M, Xie S.** *Spatiotemporal patterns and co-occurrence patterns of dissimilatory nitrate reduction to ammonium community in sediments of the Lancang River cascade reservoirs.* **Frontiers in Microbiology**. Published 2024-06. DOI: **10.3389/fmicb.2024.1411753**. URL: https://doi.org/10.3389/fmicb.2024.1411753 (yuan2024spatiotemporalpatternsand pages 4-5, yuan2024spatiotemporalpatternsand pages 7-10, yuan2024spatiotemporalpatternsand pages 2-4)
3. **Hong Y, He Z, Liu R, et al.** *Artificial Cultivation of Aquatic Plants Promotes Nitrogen Transformation and the Abundance of Key Functional Genes in Agricultural Drainage Ditch Sediments in the Yellow River Irrigation Area in China.* **Land**. Published 2024-09. DOI: **10.3390/land13101557**. URL: https://doi.org/10.3390/land13101557 (hong2024artificialcultivationof pages 8-11)
4. **Wu X, Yu S, Sui W, et al.** *Aerobic carbon metabolism modulates nitrite ammonifiers for inhibiting nitrogen loss as revealed by microcosm experiment of agricultural upland soil.* **bioRxiv** (preprint). Posted 2024-11-04. DOI: **10.1101/2024.11.04.621907**. URL: https://doi.org/10.1101/2024.11.04.621907 (wu2024aerobiccarbonmetabolism pages 1-5, wu2024aerobiccarbonmetabolism pages 5-8, wu2024aerobiccarbonmetabolism pages 12-16)
5. **Hird K, Campeciño JO, Hegg EL.** *From genes to function: regulation, maturation, and evolution of cytochrome c nitrite reductase in nitrate reduction to ammonium.* **Applied and Environmental Microbiology**. Published 2025-07. DOI: **10.1128/aem.00292-25**. URL: https://doi.org/10.1128/aem.00292-25 (hird2025fromgenesto pages 11-13)
6. **Zhao Y-F, Lai C-Y, Zhao H-P.** *Investigation of nitrogen conversion efficiency in hydrogen-based autotrophic nitrate reduction reactor.* **Journal of Water Process Engineering**. Published 2025-04. DOI: **10.1016/j.jwpe.2025.107536**. URL: https://doi.org/10.1016/j.jwpe.2025.107536 (zhao2025investigationofnitrogen pages 15-17)

(Additional older/background sources were retrieved but not used as primary evidence for 2023–2024 prioritization in this report.)


References

1. (egas2024anovelmechanism pages 1-2): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 10 citations and is from a peer-reviewed journal.

2. (wu2024aerobiccarbonmetabolism pages 1-5): Xiaogang Wu, Siyu Yu, Weikang Sui, Xinyu Zhang, Ji Li, Qiaoyu Wu, and Xiaojun Zhang. Aerobic carbon metabolism modulates nitrite ammonifiers for inhibiting nitrogen loss as revealed by microcosm experiment of agricultural upland soil. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.04.621907, doi:10.1101/2024.11.04.621907. This article has 1 citations.

3. (kostyuk2024mathematicalmodellingof pages 8-12): T Kostyuk. Mathematical modelling of complete and truncated dentrification and dissimilatory nitrate reduction to ammonium (dnra) in agricultural soils. Unknown journal, 2024.

4. (egas2024anovelmechanism pages 2-5): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 10 citations and is from a peer-reviewed journal.

5. (yuan2024spatiotemporalpatternsand pages 4-5): Bo Yuan, Mengjing Guo, Xiaode Zhou, Miaojie Li, and Shuguang Xie. Spatiotemporal patterns and co-occurrence patterns of dissimilatory nitrate reduction to ammonium community in sediments of the lancang river cascade reservoirs. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1411753, doi:10.3389/fmicb.2024.1411753. This article has 4 citations and is from a peer-reviewed journal.

6. (hird2025fromgenesto pages 11-13): Krystina Hird, Julius O. Campeciño, and Eric L. Hegg. From genes to function: regulation, maturation, and evolution of cytochrome <i>c</i> nitrite reductase in nitrate reduction to ammonium. Jul 2025. URL: https://doi.org/10.1128/aem.00292-25, doi:10.1128/aem.00292-25. This article has 6 citations and is from a peer-reviewed journal.

7. (egas2024anovelmechanism pages 9-10): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 10 citations and is from a peer-reviewed journal.

8. (hong2024artificialcultivationof pages 8-11): Yu Hong, Ziqi He, Ruliang Liu, Wenhua Xiang, Pifeng Lei, and Xi Fang. Artificial cultivation of aquatic plants promotes nitrogen transformation and the abundance of key functional genes in agricultural drainage ditch sediments in the yellow river irrigation area in china. Land, Sep 2024. URL: https://doi.org/10.3390/land13101557, doi:10.3390/land13101557. This article has 2 citations.

9. (yuan2024spatiotemporalpatternsand pages 7-10): Bo Yuan, Mengjing Guo, Xiaode Zhou, Miaojie Li, and Shuguang Xie. Spatiotemporal patterns and co-occurrence patterns of dissimilatory nitrate reduction to ammonium community in sediments of the lancang river cascade reservoirs. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1411753, doi:10.3389/fmicb.2024.1411753. This article has 4 citations and is from a peer-reviewed journal.

10. (wu2024aerobiccarbonmetabolism pages 5-8): Xiaogang Wu, Siyu Yu, Weikang Sui, Xinyu Zhang, Ji Li, Qiaoyu Wu, and Xiaojun Zhang. Aerobic carbon metabolism modulates nitrite ammonifiers for inhibiting nitrogen loss as revealed by microcosm experiment of agricultural upland soil. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.04.621907, doi:10.1101/2024.11.04.621907. This article has 1 citations.

11. (egas2024anovelmechanism media 3da222ff): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 10 citations and is from a peer-reviewed journal.

12. (egas2024anovelmechanism media 6e971979): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 10 citations and is from a peer-reviewed journal.

13. (zhao2025investigationofnitrogen pages 15-17): Yu-Fei Zhao, Chun-Yu Lai, and He-Ping Zhao. Investigation of nitrogen conversion efficiency in hydrogen-based autotrophic nitrate reduction reactor. Journal of Water Process Engineering, Apr 2025. URL: https://doi.org/10.1016/j.jwpe.2025.107536, doi:10.1016/j.jwpe.2025.107536. This article has 0 citations and is from a peer-reviewed journal.

14. (yuan2024spatiotemporalpatternsand pages 2-4): Bo Yuan, Mengjing Guo, Xiaode Zhou, Miaojie Li, and Shuguang Xie. Spatiotemporal patterns and co-occurrence patterns of dissimilatory nitrate reduction to ammonium community in sediments of the lancang river cascade reservoirs. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1411753, doi:10.3389/fmicb.2024.1411753. This article has 4 citations and is from a peer-reviewed journal.

15. (wu2024aerobiccarbonmetabolism pages 12-16): Xiaogang Wu, Siyu Yu, Weikang Sui, Xinyu Zhang, Ji Li, Qiaoyu Wu, and Xiaojun Zhang. Aerobic carbon metabolism modulates nitrite ammonifiers for inhibiting nitrogen loss as revealed by microcosm experiment of agricultural upland soil. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.04.621907, doi:10.1101/2024.11.04.621907. This article has 1 citations.