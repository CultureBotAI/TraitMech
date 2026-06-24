---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:43:44.539183'
end_time: '2026-06-18T06:01:30.906554'
duration_seconds: 1066.37
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: proteorhodopsin phototrophy
  trait_identifier: traitmech:000036
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: proteorhodopsin_phototrophy
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A light-harvesting metabolism in which a retinal-containing membrane
    protein (proteorhodopsin) acts as a light-driven proton pump, generating proton
    motive force without chlorophyll-based reaction centers. Widespread among marine
    bacterioplankton.
  parent_traits: traitmech:000037
  synonyms: rhodopsin-based phototrophy
  evidence_summary: "DOI:10.1126/science.289.5486.1902:  (B\xE9j\xE0 et al. identified\
    \ proteorhodopsin, a retinal-binding light-driven proton pump in an uncultivated\
    \ marine bacterium, as evidence for a new type of phototrophy in the sea.) | DOI:10.1038/35081051:\
    \  (B\xE9j\xE0 et al., \"Proteorhodopsin phototrophy in the ocean\", supports\
    \ proteorhodopsin as a widespread, spectrally tuned light-energy capture system\
    \ in marine bacteria.)"
  causal_graph_summary: 'proteorhodopsin_light_driven_proton_pump: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** proteorhodopsin phototrophy
- **METPO identifier:** traitmech:000036
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A light-harvesting metabolism in which a retinal-containing membrane protein (proteorhodopsin) acts as a light-driven proton pump, generating proton motive force without chlorophyll-based reaction centers. Widespread among marine bacterioplankton.
- **Parent traits:** traitmech:000037
- **Synonyms:** rhodopsin-based phototrophy
- **Existing evidence:** DOI:10.1126/science.289.5486.1902:  (Béjà et al. identified proteorhodopsin, a retinal-binding light-driven proton pump in an uncultivated marine bacterium, as evidence for a new type of phototrophy in the sea.) | DOI:10.1038/35081051:  (Béjà et al., "Proteorhodopsin phototrophy in the ocean", supports proteorhodopsin as a widespread, spectrally tuned light-energy capture system in marine bacteria.)
- **Existing causal graph summary:** proteorhodopsin_light_driven_proton_pump: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **proteorhodopsin phototrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteorhodopsin_phototrophy.yaml`.

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
- **Trait label:** proteorhodopsin phototrophy
- **METPO identifier:** traitmech:000036
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A light-harvesting metabolism in which a retinal-containing membrane protein (proteorhodopsin) acts as a light-driven proton pump, generating proton motive force without chlorophyll-based reaction centers. Widespread among marine bacterioplankton.
- **Parent traits:** traitmech:000037
- **Synonyms:** rhodopsin-based phototrophy
- **Existing evidence:** DOI:10.1126/science.289.5486.1902:  (Béjà et al. identified proteorhodopsin, a retinal-binding light-driven proton pump in an uncultivated marine bacterium, as evidence for a new type of phototrophy in the sea.) | DOI:10.1038/35081051:  (Béjà et al., "Proteorhodopsin phototrophy in the ocean", supports proteorhodopsin as a widespread, spectrally tuned light-energy capture system in marine bacteria.)
- **Existing causal graph summary:** proteorhodopsin_light_driven_proton_pump: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **proteorhodopsin phototrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteorhodopsin_phototrophy.yaml`.

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


## Proteorhodopsin phototrophy (TraitMech: traitmech:000036) — curation-focused research report

### 1) Scope summary (trait definition, boundaries, and assay-observed phenotype)

**Trait definition (current understanding).** Proteorhodopsin (PR) phototrophy is a retinal-based, rhodopsin-mediated energy-harvesting strategy in which a single membrane protein functions as a **light-dependent proton pump**, generating **proton motive force (PMF)** that can be used to make ATP and power other energy-requiring processes. This distinguishes the trait from chlorophyll-based photosystems by its molecular simplicity and retinal chromophore dependence (“validated … as a light-dependent proton pump”). (zambrano2024enlightenedbymicrobial pages 1-4)

**Key boundary vs chlorophyll-based photosynthesis.** A central boundary for TraitMech curation is that PR phototrophy supplies **ATP via PMF** but (in the general case) does **not provide reducing power** for anabolic metabolism; Oh et al. state explicitly that PR “supplies only ATP” and that “PR can never be harnessed to generate NAD (P)H for anabolic metabolism.” (oh2024effectoflight pages 13-14)

**Operational boundary vs other phototrophic modes in environmental omics.** In metatranscriptomic field datasets, PR phototrophy is often operationalized using the **prd** marker gene, while oxygenic photosynthesis is tracked by **rubisco** genes and aerobic anoxygenic phototrophy (AAP; bacteriochlorophyll-based) by **puf** genes. This provides a practical boundary for curation and for interpreting in situ expression. (delgadillonuno2024coastalupwellingsystems pages 7-9)

**Boundary cases / cautions.** 
* Phenotype expression is highly context dependent: IMCC1322 exhibited PR photoheterotrophy only under specific lab contexts (“nutrient-replete cultures with higher inoculating cell densities”). (oh2024effectoflight pages 1-2)
* PR-driven proton pumping can be beneficial, neutral, or harmful depending on physiology and environment; PR-associated **excess protons** can generate acid stress. (oh2024effectoflight pages 1-2)
* Some literature (cited within a 2024 transcriptomics paper) reports that PR-driven proton pumping “can completely substitute respiration … under specific environmental conditions,” but this is an indirect citation in the evidence gathered here and should be curated as **conditional**. (lee2024effectsoflight pages 1-2)

### 2) Key concepts and mechanistic entities for causal graph nodes

Below are candidate nodes grouped by type. Where stable identifiers are not available in the retrieved evidence, label-only nodes are provided.

#### A. Genes / proteins / complexes
- **proteorhodopsin (PR)**; **prd** (marker gene in field transcriptomics) (delgadillonuno2024coastalupwellingsystems pages 7-9)
- **F0F1 ATP synthase** (driven by PMF; implied by “membrane potential for ATP production”) (lee2024effectsoflight pages 1-2)
- **Retinal-binding lysine (Schiff base lysine; PR chromophore linkage)** (hirschi2024structuralinsightsinto pages 8-9)
- **β-carotene dioxygenase** (enzyme that cleaves β-carotene to retinal; gene name not specified in snippet) (jing2022revealingco2fixingsar11 pages 11-11)
- **Photocycle/proton-transfer residues** (e.g., Asp97/Asp227 discussed in broader rhodopsin literature context; may be relevant but not essential to trait-level curation here) (hasegawatakano2024cyanorhodopsiniirepresentsa pages 9-10)
- **Spectral tuning site: residue 105 (Leu105/Gln105)** controlling green vs blue variants (mao2024molecularmechanismsand pages 2-3, mao2024molecularmechanismsand pages 1-2)

#### B. Chemicals / metabolites
- **all-trans retinal** (CHEBI identifier should be added during curation if desired) (hirschi2024structuralinsightsinto pages 8-9, hirschi2024structuralinsightsinto pages 6-8)
- **β-carotene** (precursor to retinal) (jing2022revealingco2fixingsar11 pages 11-11)
- **Decanoate / decanoic acid (capric acid)** (temporary chromophore-pocket placeholder for retinal in proteoopsin) (hirschi2024structuralinsightsinto pages 5-6)
- **ATP** (quantified as mM and zeptomoles per cell in IMCC1322) (oh2024effectoflight pages 1-2, oh2024effectoflight media 7c5e5ff1)

#### C. Biological processes / functions (candidate GO grounding)
- **Light-driven proton transmembrane transport** (GO: proton transmembrane transport; candidate)
- **Generation of proton motive force** (process node)
- **ATP biosynthetic process / oxidative phosphorylation coupling to PMF** (candidate GO)
- **Photophosphorylation** (term used in evidence) (lee2024effectsoflight pages 1-2)
- **Acid stress / pH homeostasis** (process node; linked to “excessive protons” and mitigation) (oh2024effectoflight pages 1-2)

#### D. Environmental / experimental factors (candidate ENVO grounding)
- **Light regime** (constant light, constant dark, diel cycles) and **irradiance** (oh2024effectoflight pages 2-3, oh2024effectoflight media 7c5e5ff1)
- **Water-column depth / spectral environment** (shallow vs deep; blue vs green light) (mao2024molecularmechanismsand pages 1-2)
- **Nutrient status** (nutrient-replete vs nutrient-limited; oligotrophic) (oh2024effectoflight pages 1-2, zambrano2024enlightenedbymicrobial pages 4-4)
- **Phytoplankton blooms / DOM release** (summer blooms; complex carbon uptake) (delgadillonuno2024coastalupwellingsystems pages 13-14)

#### E. Assays / observables (for trait evidence)
- **ATP/cell** (zeptomoles per cell) and bulk ATP (mM) (oh2024effectoflight pages 1-2, oh2024effectoflight media 7c5e5ff1)
- **prd transcript abundance (TPM)** in metatranscriptomics (delgadillonuno2024coastalupwellingsystems pages 7-9)
- **Stable isotope inorganic carbon assimilation (no difference under LL vs DD in late log phase)** (oh2024effectoflight pages 1-2)

### 3) Evidence-backed candidate causal edges (triples) for TraitMech

The following table is designed for direct transposition into a TraitMech YAML (with further normalization/grounding as needed).

| Edge (S–P–O) | Evidence snippet (verbatim short quote) | Source (first author year) | DOI | URL |
|---|---|---|---|---|
| Light → activates proteorhodopsin proton pumping | “validated functionally in *Escherichia coli* as a light-dependent proton pump” (zambrano2024enlightenedbymicrobial pages 1-4) | Zambrano 2024 | N/A | N/A |
| Proteorhodopsin proton pumping → proton motive force | “PR drives PMF generation” (oh2024effectoflight pages 13-14) | Oh 2024 | 10.4014/jmb.2410.10034 | https://doi.org/10.4014/jmb.2410.10034 |
| Proteorhodopsin-mediated proton transport → ATP production | “PR-mediated proton transport could generate a sufficient membrane potential for ATP production” (lee2024effectsoflight pages 1-2) | Lee 2024 | 10.1007/s12275-024-00125-0 | https://doi.org/10.1007/s12275-024-00125-0 |
| Proteorhodopsin phototrophy → does not generate NAD(P)H | “PR can never be harnessed to generate NAD (P)H for anabolic metabolism” (oh2024effectoflight pages 13-14) | Oh 2024 | 10.4014/jmb.2410.10034 | https://doi.org/10.4014/jmb.2410.10034 |
| PR-driven proton pumping → can substitute for respiration under specific conditions | “the light-driven proton pumping by PR can completely substitute respiration as a cellular energy source under specific environmental conditions” (lee2024effectsoflight pages 1-2) | Lee 2024 | 10.1007/s12275-024-00125-0 | https://doi.org/10.1007/s12275-024-00125-0 |
| Leu105 at residue 105 → green-shifted absorption | “Leu105 is predominant in green PRs (GPRs) from shallow waters” (mao2024molecularmechanismsand pages 2-3) | Mao 2024 | 10.1126/sciadv.adj0384 | https://doi.org/10.1126/sciadv.adj0384 |
| Gln105 at residue 105 → blue-shifted absorption | “Gln105 is predominant in blue PRs (BPRs) from deeper waters” (mao2024molecularmechanismsand pages 2-3) | Mao 2024 | 10.1126/sciadv.adj0384 | https://doi.org/10.1126/sciadv.adj0384 |
| Depth / blue-light environment → selects for Gln105 blue PR variants | “Gln105 variants are enriched in deeper waters where blue light penetrates and dominates the deep photic zone” (mao2024molecularmechanismsand pages 1-2) | Mao 2024 | 10.1126/sciadv.adj0384 | https://doi.org/10.1126/sciadv.adj0384 |
| Shallow / green-light environment → selects for Leu105 green PR variants | “Leu105 variants predominate in upper waters tuned to green light” (mao2024molecularmechanismsand pages 1-2) | Mao 2024 | 10.1126/sciadv.adj0384 | https://doi.org/10.1126/sciadv.adj0384 |
| All-trans retinal → required for functional proteorhodopsin | “Functional proteorhodopsin requires insertion of all-trans retinal by formation of a Schiff base with a central lysine” (hirschi2024structuralinsightsinto pages 8-9) | Hirschi 2024 | 10.1038/s41467-024-50960-3 | https://doi.org/10.1038/s41467-024-50960-3 |
| β-carotene dioxygenase cleavage → retinal | “β-carotene can be cleaved by dioxygenase into retinal, which is an important element in functional PR” (jing2022revealingco2fixingsar11 pages 11-11) | Jing 2022 | 10.34133/2022/9782712 | https://doi.org/10.34133/2022/9782712 |
| Lack of retinal biosynthesis pathway → retinal scavenging from environment | “some proteorhodopsin-expressing bacteria lack endogenous retinal biosynthesis pathways and likely scavenge retinal from the environment” (hirschi2024structuralinsightsinto pages 1-2) | Hirschi 2024 | 10.1038/s41467-024-50960-3 | https://doi.org/10.1038/s41467-024-50960-3 |
| Decanoate placeholder in proteoopsin → facilitates retinal incorporation | “might serve as a mechanism for facilitating the substitution of decanoate with retinal, allowing the protein to scavenge the cofactor from the environment” (hirschi2024structuralinsightsinto pages 5-6) | Hirschi 2024 | 10.1038/s41467-024-50960-3 | https://doi.org/10.1038/s41467-024-50960-3 |
| prd transcript abundance in upwelling bacterioplankton → remains high and stable | “proteorhodopsin (prd) transcript levels were relatively stable and high (~4000 TPM) across all samples” (delgadillonuno2024coastalupwellingsystems pages 7-9) | Delgadillo-Nuño 2024 | 10.3389/fmars.2023.1259783 | https://doi.org/10.3389/fmars.2023.1259783 |
| Summer phytoplankton blooms → elevate Cellvibrionales prd transcription | “elevated transcription of the proteorhodopsin gene (prd) by Cellvibrionales during summer phytoplankton blooms” (delgadillonuno2024coastalupwellingsystems pages 13-14) | Delgadillo-Nuño 2024 | 10.3389/fmars.2023.1259783 | https://doi.org/10.3389/fmars.2023.1259783 |
| Elevated Cellvibrionales prd transcription → supplemental energy for uptake of complex carbon | “proteorhodopsin-driven proton pumps providing supplemental energy to uptake recently released complex carbon compounds” (delgadillonuno2024coastalupwellingsystems pages 13-14) | Delgadillo-Nuño 2024 | 10.3389/fmars.2023.1259783 | https://doi.org/10.3389/fmars.2023.1259783 |
| Nutrient-replete conditions / higher inoculum → PR photoheterotrophy in IMCC1322 | “strain IMCC1322 exhibited proteorhodopsin photoheterotrophy” under “nutrient-replete cultures with higher inoculating cell densities” (oh2024effectoflight pages 1-2) | Oh 2024 | 10.4014/jmb.2410.10034 | https://doi.org/10.4014/jmb.2410.10034 |
| PR-generated excess protons → acid stress | “IMCC1322 may suffer from excessive protons generated by proteorhodopsin under light conditions” and “acid stress could also be mitigated” (oh2024effectoflight pages 1-2) | Oh 2024 | 10.4014/jmb.2410.10034 | https://doi.org/10.4014/jmb.2410.10034 |
| Membrane unsaturation / cyclopropanation → mitigates proton stress | “acid stress could also be mitigated by refining membrane permeability through unsaturation and cyclopropanation of phospholipids” (oh2024effectoflight pages 1-2) | Oh 2024 | 10.4014/jmb.2410.10034 | https://doi.org/10.4014/jmb.2410.10034 |


*Table: This table summarizes evidence-backed candidate subject–predicate–object edges for curating a TraitMech causal graph of proteorhodopsin phototrophy. It covers core mechanism, spectral adaptation, retinal biogenesis/scavenging, ecological expression patterns, and physiological context-dependent outcomes.*

**Visual quantitative evidence (Table).** Oh et al. provide a compiled table reporting ATP per cell (13.9–367 zmol·cell−1) together with irradiance (11.4 µmol·m−2·s−1), PR λmax (522 nm), and light regime for IMCC1322, supporting quantitative encoding of “light regime → ATP phenotype” and “spectral tuning/λmax” nodes. (oh2024effectoflight media 7c5e5ff1)

### 4) Recent developments and latest research (prioritizing 2023–2024)

**(i) Retinal scavenging and PR biogenesis mechanisms (2024).** Hirschi et al. (Nature Communications, 2024-08-xx) provide structural and computational evidence that some PR-expressing microbes may lack retinal biosynthesis and instead **scavenge retinal**; they solved a retinal-free structure and identify **decanoate** as a chromophore-pocket ligand, proposing it as a temporary placeholder that can be exchanged for retinal (“facilitating the substitution of decanoate with retinal, allowing the protein to scavenge the cofactor from the environment”). (hirschi2024structuralinsightsinto pages 5-6, hirschi2024structuralinsightsinto pages 1-2)

**(ii) Mechanistic basis of spectral tuning and depth adaptation (2024).** Mao et al. (Science Advances, 2024-01-xx) analyzed thousands of PR sequences and show a strong association of **residue 105** with spectral variants: “Leu105 is predominant in green PRs (GPRs) from shallow waters” and “Gln105 is predominant in blue PRs (BPRs) from deeper waters,” consistent with depth-dependent light spectra. (mao2024molecularmechanismsand pages 2-3, mao2024molecularmechanismsand pages 1-2)

**(iii) In situ functional expression patterns in dynamic coastal systems (2024).** Delgadillo-Nuño et al. (Frontiers in Marine Science, 2024-01-xx) report that **prd** transcript abundance was “stable and high (~4000 TPM)” across a NW Iberian upwelling study, largely from Pelagibacterales, and interpret elevated **Cellvibrionales prd** transcription during summer phytoplankton blooms as enabling “supplemental energy to uptake … complex carbon compounds.” (delgadillonuno2024coastalupwellingsystems pages 7-9, delgadillonuno2024coastalupwellingsystems pages 13-14)

**(iv) Physiological context dependence and ATP budget framing (2024).** Oh et al. (Journal of Microbiology and Biotechnology, 2024-11-xx) emphasize that PR phototrophy may increase ATP under some conditions but can also create PMF/pH stress, and that PR-derived ATP can be too small to support major anabolic demands; they explicitly frame the biochemical boundary that PR “can never be harnessed to generate NAD (P)H.” (oh2024effectoflight pages 13-14, oh2024effectoflight pages 1-2)

### 5) Current applications and real-world implementations

**Ecology/biogeochemistry implementation (field monitoring).** PR phototrophy is already used as a field-interpretable functional module via marker genes (**prd**) in metatranscriptomic workflows, allowing comparisons against rubisco (chlorophyll photosynthesis) and puf (bacteriochlorophyll/AAP). (delgadillonuno2024coastalupwellingsystems pages 7-9)

**Bioengineering / synthetic biology implementations.** Rhodopsin-based phototrophy is being explored as a modular, non-redox light-harvesting component because it is “independent of electron transfer,” yet can power downstream metabolism via PMF coupling; this motivates engineered “rhodopsin-based artificial photosynthesis” designs. (tu2024engineeringrhodopsinbasedartificial pages 102-105)

### 6) Expert analysis and authoritative interpretations

**Energetic boundary as a curation principle.** A key expert-level interpretation emphasized in the 2024 physiology study is that PR provides an **ATP-only** benefit, not a full photosynthetic redox-energy package; thus, PR phototrophy is best curated as an **auxiliary energy module** that can modulate survival, uptake, and maintenance rather than a primary carbon-fixation pathway. This is grounded in the explicit statement that PR cannot generate NAD(P)H for anabolic metabolism. (oh2024effectoflight pages 13-14)

**Trait conditionality.** Multiple recent sources converge on the idea that the phenotypic impact of PR is conditional (growth stage, nutrient regime, and taxon-specific physiology), so causal edges from PR to “growth increase” should be annotated as uncertain or context-specific. (oh2024effectoflight pages 1-2, oh2024effectoflight pages 2-3)

### 7) Relevant statistics and data (recent studies)

**Prevalence (marine).** A 2024 transcriptomics paper reports the field prevalence statistic: “PR-containing bacteria account for 13% of the sea-surface microorganisms and more than 50% of the total microbial community within the euphotic zone.” (lee2024effectsoflight pages 1-2)

**In situ expression magnitude.** In a coastal upwelling metatranscriptome, “proteorhodopsin (prd) transcript levels were relatively stable and high (~4000 TPM) across all samples.” (delgadillonuno2024coastalupwellingsystems pages 7-9)

**Physiology: ATP per cell and light parameters (2024 culture study).** Oh et al. report stationary/death phase ATP for IMCC1322 in the range of 13.9–367 zmol·cell−1, and Table 1 compiles PR λmax (522 nm) and irradiance (11.4 µmol·m−2·s−1) for that experimental context. (oh2024effectoflight media 7c5e5ff1)

### 8) Ontology grounding suggestions (non-exhaustive)

- **Trait:** METPO traitmech:000036 (proteorhodopsin phototrophy; provided)
- **Processes (GO candidates):** proton transmembrane transport; photophosphorylation; ATP biosynthetic process; response to acid stress / pH homeostasis (label-only here)
- **Chemicals (CHEBI candidates):** all-trans-retinal; β-carotene; decanoic acid
- **Environment (ENVO candidates):** marine photic zone / euphotic zone; oligotrophic marine water; coastal upwelling system

### 9) Curation warnings (claims not ready for strong edges)

1. **Respiration substitution claim is indirect** in the retrieved evidence: “can completely substitute respiration …” appears in a 2024 paper as a cited statement; curate as conditional and ideally verify in the primary study before encoding as a strong universal edge. (lee2024effectsoflight pages 1-2)
2. **Growth benefits are not universal**: the same physiological system can yield no growth effect or even stress depending on conditions; avoid a generic PR → increased growth edge without specifying environmental modifiers (nutrients, growth phase, light regime). (oh2024effectoflight pages 1-2, oh2024effectoflight pages 2-3)
3. **Retinal scavenging is compelling but may be taxon-specific**: Hirschi et al. provide strong mechanistic support in a model PR system; curators should record taxonomic scope (organisms lacking retinal synthesis pathways) where possible. (hirschi2024structuralinsightsinto pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates where available)

1. Oh H-M, Lee JH, Choi A, et al. *Effect of Light Regime on Candidatus Puniceispirillum marinum IMCC1322 in Nutrient-Replete Conditions.* **Journal of Microbiology and Biotechnology**. 2024-11 (online). DOI: **10.4014/jmb.2410.10034**. URL: https://doi.org/10.4014/jmb.2410.10034 (oh2024effectoflight pages 1-2, oh2024effectoflight pages 13-14)
2. Lee JH, Oh H-M. *Effects of Light and Dark Conditions on the Transcriptome of Aging Cultures of Candidatus Puniceispirillum marinum IMCC1322.* **Journal of Microbiology**. 2024-04. DOI: **10.1007/s12275-024-00125-0**. URL: https://doi.org/10.1007/s12275-024-00125-0 (lee2024effectsoflight pages 1-2)
3. Hirschi S, Lemmin TM, Ayoub NFN, et al. *Structural insights into the mechanism and dynamics of proteorhodopsin biogenesis and retinal scavenging.* **Nature Communications**. 2024-08. DOI: **10.1038/s41467-024-50960-3**. URL: https://doi.org/10.1038/s41467-024-50960-3 (hirschi2024structuralinsightsinto pages 5-6, hirschi2024structuralinsightsinto pages 1-2)
4. Mao J, Jin X, Shi M, et al. *Molecular mechanisms and evolutionary robustness of a color switch in proteorhodopsins.* **Science Advances**. 2024-01. DOI: **10.1126/sciadv.adj0384**. URL: https://doi.org/10.1126/sciadv.adj0384 (mao2024molecularmechanismsand pages 2-3, mao2024molecularmechanismsand pages 1-2)
5. Delgadillo-Nuño E, Teira E, Pontiller B, et al. *Coastal upwelling systems as dynamic mosaics of bacterioplankton functional specialization.* **Frontiers in Marine Science**. 2024-01. DOI: **10.3389/fmars.2023.1259783**. URL: https://doi.org/10.3389/fmars.2023.1259783 (delgadillonuno2024coastalupwellingsystems pages 7-9, delgadillonuno2024coastalupwellingsystems pages 13-14)
6. Jing X, Gong Y, Xu T, et al. *Revealing CO2-Fixing SAR11 Bacteria in the Ocean by Raman-Based Single-Cell Metabolic Profiling and Genomics.* **Biodesign Research**. 2022-10. DOI: **10.34133/2022/9782712**. URL: https://doi.org/10.34133/2022/9782712 (jing2022revealingco2fixingsar11 pages 11-11)

Non-DOI / limited-metadata sources used cautiously:
- Zambrano MM. *Enlightened by Microbial Rhodopsins.* 2024. (Metadata incomplete in retrieved text.) (zambrano2024enlightenedbymicrobial pages 1-4)
- Tu W. *Engineering rhodopsin-based artificial photosynthesis.* University of Oxford dissertation. 2024-01. DOI: 10.5287/ora-8jgz2nrvd. URL: https://doi.org/10.5287/ora-8jgz2nrvd (tu2024engineeringrhodopsinbasedartificial pages 102-105)


References

1. (zambrano2024enlightenedbymicrobial pages 1-4): MM Zambrano. Enlightened by microbial rhodopsins. Unknown journal, 2024.

2. (oh2024effectoflight pages 13-14): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

3. (delgadillonuno2024coastalupwellingsystems pages 7-9): Erick Delgadillo-Nuño, Eva Teira, Benjamin Pontiller, Daniel Lundin, Vanessa Joglar, Carlos Pedrós-Alió, Emilio Fernández, Jarone Pinhassi, and Sandra Martínez-García. Coastal upwelling systems as dynamic mosaics of bacterioplankton functional specialization. Frontiers in Marine Science, Jan 2024. URL: https://doi.org/10.3389/fmars.2023.1259783, doi:10.3389/fmars.2023.1259783. This article has 10 citations.

4. (oh2024effectoflight pages 1-2): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

5. (lee2024effectsoflight pages 1-2): Ji Hyen Lee and Hyun-Myung Oh. Effects of light and dark conditions on the transcriptome of aging cultures of candidatus puniceispirillum marinum imcc1322. Journal of microbiology, 62:297-314, Apr 2024. URL: https://doi.org/10.1007/s12275-024-00125-0, doi:10.1007/s12275-024-00125-0. This article has 2 citations and is from a peer-reviewed journal.

6. (hirschi2024structuralinsightsinto pages 8-9): Stephan Hirschi, Thomas Max Lemmin, Nooraldeen Fathi Nooraldeen Ayoub, David Andreas Kalbermatter, Daniele Pellegata, Zöhre Ucurum Fotiadis, Jürg Gertsch, and Dimitrios José Fotiadis. Structural insights into the mechanism and dynamics of proteorhodopsin biogenesis and retinal scavenging. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-50960-3, doi:10.1038/s41467-024-50960-3. This article has 4 citations and is from a highest quality peer-reviewed journal.

7. (jing2022revealingco2fixingsar11 pages 11-11): Xiaoyan Jing, Yanhai Gong, Teng Xu, Paul A. Davison, Craig MacGregor-Chatwin, C. Neil Hunter, La Xu, Yu Meng, Yuetong Ji, Bo Ma, Jian Xu, and Wei E. Huang. Revealing co2-fixing sar11 bacteria in the ocean by raman-based single-cell metabolic profiling and genomics. Biodesign Research, 2022:9782712, Oct 2022. URL: https://doi.org/10.34133/2022/9782712, doi:10.34133/2022/9782712. This article has 27 citations.

8. (hasegawatakano2024cyanorhodopsiniirepresentsa pages 9-10): Masumi Hasegawa-Takano, Toshiaki Hosaka, Keiichi Kojima, Yosuke Nishimura, Marie Kurihara, Yu Nakajima, Yoshiko Ishizuka-Katsura, Tomomi Kimura-Someya, Mikako Shirouzu, Yuki Sudo, and Susumu Yoshizawa. Cyanorhodopsin-ii represents a yellow-absorbing proton-pumping rhodopsin clade within cyanobacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae175, doi:10.1093/ismejo/wrae175. This article has 4 citations.

9. (mao2024molecularmechanismsand pages 2-3): Jiafei Mao, Xinsheng Jin, Man Shi, David Heidenreich, Lynda J. Brown, Richard C. D. Brown, Moreno Lelli, Xiao He, and Clemens Glaubitz. Molecular mechanisms and evolutionary robustness of a color switch in proteorhodopsins. Science Advances, Jan 2024. URL: https://doi.org/10.1126/sciadv.adj0384, doi:10.1126/sciadv.adj0384. This article has 13 citations and is from a highest quality peer-reviewed journal.

10. (mao2024molecularmechanismsand pages 1-2): Jiafei Mao, Xinsheng Jin, Man Shi, David Heidenreich, Lynda J. Brown, Richard C. D. Brown, Moreno Lelli, Xiao He, and Clemens Glaubitz. Molecular mechanisms and evolutionary robustness of a color switch in proteorhodopsins. Science Advances, Jan 2024. URL: https://doi.org/10.1126/sciadv.adj0384, doi:10.1126/sciadv.adj0384. This article has 13 citations and is from a highest quality peer-reviewed journal.

11. (hirschi2024structuralinsightsinto pages 6-8): Stephan Hirschi, Thomas Max Lemmin, Nooraldeen Fathi Nooraldeen Ayoub, David Andreas Kalbermatter, Daniele Pellegata, Zöhre Ucurum Fotiadis, Jürg Gertsch, and Dimitrios José Fotiadis. Structural insights into the mechanism and dynamics of proteorhodopsin biogenesis and retinal scavenging. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-50960-3, doi:10.1038/s41467-024-50960-3. This article has 4 citations and is from a highest quality peer-reviewed journal.

12. (hirschi2024structuralinsightsinto pages 5-6): Stephan Hirschi, Thomas Max Lemmin, Nooraldeen Fathi Nooraldeen Ayoub, David Andreas Kalbermatter, Daniele Pellegata, Zöhre Ucurum Fotiadis, Jürg Gertsch, and Dimitrios José Fotiadis. Structural insights into the mechanism and dynamics of proteorhodopsin biogenesis and retinal scavenging. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-50960-3, doi:10.1038/s41467-024-50960-3. This article has 4 citations and is from a highest quality peer-reviewed journal.

13. (oh2024effectoflight media 7c5e5ff1): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

14. (oh2024effectoflight pages 2-3): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

15. (zambrano2024enlightenedbymicrobial pages 4-4): MM Zambrano. Enlightened by microbial rhodopsins. Unknown journal, 2024.

16. (delgadillonuno2024coastalupwellingsystems pages 13-14): Erick Delgadillo-Nuño, Eva Teira, Benjamin Pontiller, Daniel Lundin, Vanessa Joglar, Carlos Pedrós-Alió, Emilio Fernández, Jarone Pinhassi, and Sandra Martínez-García. Coastal upwelling systems as dynamic mosaics of bacterioplankton functional specialization. Frontiers in Marine Science, Jan 2024. URL: https://doi.org/10.3389/fmars.2023.1259783, doi:10.3389/fmars.2023.1259783. This article has 10 citations.

17. (hirschi2024structuralinsightsinto pages 1-2): Stephan Hirschi, Thomas Max Lemmin, Nooraldeen Fathi Nooraldeen Ayoub, David Andreas Kalbermatter, Daniele Pellegata, Zöhre Ucurum Fotiadis, Jürg Gertsch, and Dimitrios José Fotiadis. Structural insights into the mechanism and dynamics of proteorhodopsin biogenesis and retinal scavenging. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-50960-3, doi:10.1038/s41467-024-50960-3. This article has 4 citations and is from a highest quality peer-reviewed journal.

18. (tu2024engineeringrhodopsinbasedartificial pages 102-105): Engineering rhodopsin-based artificial photosynthesis This article has 0 citations.