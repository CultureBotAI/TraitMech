---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:06:01.426428'
end_time: '2026-06-18T01:28:41.687987'
duration_seconds: 1360.26
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pressure range
  trait_identifier: traitmech:000005
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: pressure_range
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pressure phenotype with numerical limits that bounds the minimum and
    maximum hydrostatic pressures supporting growth of an organism.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum,
    120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a bounded growth-supporting
    pressure span (80-140 MPa), the quantity this phenotype records.) | DOI:10.3389/fmolb.2022.1058381:
    Microorganisms adapted to HHP are usually known as piezophiles, referring to their
    preference for high pressure (Pressure-adaptation review supports the bounded
    span of growth-permissive hydrostatic pressure as a defining quantitative descriptor.)'
  causal_graph_summary: 'pressure_range_growth_bounded_span: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pressure range
- **METPO identifier:** traitmech:000005
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits that bounds the minimum and maximum hydrostatic pressures supporting growth of an organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a bounded growth-supporting pressure span (80-140 MPa), the quantity this phenotype records.) | DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports the bounded span of growth-permissive hydrostatic pressure as a defining quantitative descriptor.)
- **Existing causal graph summary:** pressure_range_growth_bounded_span: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pressure range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_range.yaml`.

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
- **Trait label:** pressure range
- **METPO identifier:** traitmech:000005
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits that bounds the minimum and maximum hydrostatic pressures supporting growth of an organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a bounded growth-supporting pressure span (80-140 MPa), the quantity this phenotype records.) | DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports the bounded span of growth-permissive hydrostatic pressure as a defining quantitative descriptor.)
- **Existing causal graph summary:** pressure_range_growth_bounded_span: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pressure range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_range.yaml`.

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


## Microbial TraitMech Curation Report: **pressure range** (traitmech:000005)

### Scope summary (what the trait represents)
**Pressure range** (TraitMech: pressure_range; METPO identifier *traitmech:000005*) is a **quantitative growth phenotype** describing the **bounded minimum and maximum hydrostatic pressures (e.g., MPa) that support growth** of an organism under defined culture conditions (temperature, salinity, electron acceptor, medium, incubation duration, etc.). It is distinct from:

* **Optimal growth pressure** (a single value at which growth rate is maximal) (peoples2020distinctivegeneand pages 1-2, li2023strategyforthe pages 2-4).
* **Piezophily / piezotolerance categories** (qualitative preference/tolerance terms); these classify organisms by where their *optimum* lies and whether they can grow at 0.1 MPa, but they do not by themselves encode min–max bounds (scheffer2023themysteryof pages 1-2, tamby2023microbialmembranelipid pages 1-2).
* **Survival under pressure** (viability after exposure) without demonstrated replication; survival can extend beyond growth limits and should not be curated as pressure range (malas2024biologicalfunctionsat pages 1-2).

**Assay boundary cases / curation cautions:**
* **Temperature confounding:** many deep-sea piezophiles are also psychrophiles; membrane lipid changes and other responses can be induced by cold or pressure, requiring controlled designs to attribute causality to pressure (scheffer2023themysteryof pages 6-7, tamby2023microbialmembranelipid pages 1-2).
* **Exposure time confounding:** brief exposures can show metabolic activity/viability at pressures above growth-permissive ranges (malas2024biologicalfunctionsat pages 1-2).

### Current understanding: what sets the bounded growth limits?
Evidence across recent reviews and experiments supports a multi-layer mechanism in which **pressure pushes membranes toward ordered states, perturbs protein conformational ensembles and hydration, and stresses redox/energy systems**, thereby setting growth boundaries unless organisms mount compensatory responses.

Key mechanistic themes most consistently connected to high-pressure growth are:

1. **Membrane homeoviscous/homeophasic adaptation** via increased fatty-acyl **unsaturation**, altered branching/chain length, and (in some taxa) enrichment of long-chain **ω-3 polyunsaturated fatty acids** (PUFAs), which counteract pressure-induced tight packing and preserve membrane protein function (tamby2023microbialmembranelipid pages 2-4, scheffer2023themysteryof pages 6-7, peters2023effectsofcrowding pages 24-26).
2. **Pressure-responsive regulation of envelope proteins** (e.g., porins) affecting transport/permeability at pressure (scheffer2023themysteryof pages 7-9).
3. **Redox/respiratory remodeling and oxidative-stress control**, including elevated antioxidant defenses and alternative electron acceptor use (notably nitrate reduction) under HHP (li2023strategyforthe pages 1-2, li2023strategyforthe pages 6-8, li2023strategyforthe pages 8-10).
4. **Compatible solutes (“piezolytes”)** such as **betaine, glutamate, β-hydroxybutyrate, and TMAO**, proposed to stabilize proteins via **preferential hydration** and altered hydration dynamics, supporting function under pressure (scheffer2023themysteryof pages 9-10, peters2023effectsofcrowding pages 50-52).
5. **Pressure-tolerant cell division machinery**, especially the FtsZ cytoskeleton/Z-ring system, which is vulnerable to pressure in model bacteria but shows pressure-stable variants in obligate piezophiles (cui2024nterminusgtpasedomain pages 1-2).

### Recent developments & latest research (prioritized 2023–2024)
#### 1) Membrane lipid adaptation synthesis and strain-level patterns (2023)
A focused 2023 review synthesizes marine microbial lipid adaptations to high hydrostatic pressure (HHP), emphasizing increased **unsaturated and branched-chain fatty acids** with rising HHP and the frequent association of **C20:5 (EPA) and C22:6 (DHA)** with adaptation (tamby2023microbialmembranelipid pages 2-4, tamby2023microbialmembranelipid pages 1-2). The review also highlights that strategies are **not universal** (some taxa lack key PUFAs or show opposite regulation), a critical warning for graph generalization (tamby2023microbialmembranelipid pages 2-4, tamby2023microbialmembranelipid pages 6-7).

A key visual synthesis in this review is shown in **Figure 1** and a cross-taxon adaptation summary in **Table 1**, useful as curated background for membrane-related nodes/edges (tamby2023microbialmembranelipid media 0d6dd688, tamby2023microbialmembranelipid media d89ff60b).

#### 2) Quantitative, multi-omics evidence linking HHP to oxidative stress and nitrate respiration (2023)
In *Halomonas titanicae* ANRCS81, growth was demonstrated across a broad **0.1–55 MPa** range, and pressure-dependent growth-rate differences were quantified (e.g., maximal growth at 35 MPa; anaerobic growth at 40 MPa reported) (li2023strategyforthe pages 2-4). At **40 MPa**, transcriptomics and physiology indicated that HHP triggers **intracellular oxidative stress** and induces a coordinated response:

* Upregulation of antioxidant-defense regulators/enzymes (including **sod1/sod2**, **oxyR/soxR**) and increased **SOD activity** (li2023strategyforthe pages 1-2, li2023strategyforthe pages 6-8).
* Upregulation of **dissimilatory nitrate reduction/denitrification** genes and increased nitrate/nitrite consumption with increased ammonium generation, consistent with altered energy metabolism under HHP (li2023strategyforthe pages 6-8, li2023strategyforthe pages 8-10).

This provides relatively direct edges from HHP → oxidative stress response → growth under HHP, and HHP → nitrate respiration → growth under HHP.

#### 3) Pressure-responsive respiratory gene regulation via TorRS → torA (2023)
A 2023 study identifies a **two-component system (TorRS)** mediating HHP-responsive induction of **TMAO reductase (torA)** in *Vibrio fluvialis*, explicitly stating that HHP induction of TMAO reductase is mediated by TorRS (liu2023thetorrstwo pages 1-2). The paper also notes *V. fluvialis* QY27 can grow up to **50 MPa** (liu2023thetorrstwo pages 1-2). This is a high-confidence regulatory edge suitable for mechanistic curation (with taxon-specific annotation).

#### 4) Cell-division adaptation at high pressure: FtsZ pressure tolerance (2024)
A 2024 mechanistic study compares FtsZ from a pressure-sensitive *Shewanella* and an obligate piezophile (*Shewanella benthica* DB21MT-2) and reports that HHP **hardly affected Z-ring formation** in the piezophile FtsZ, with filaments remaining more stable after incubation under **50 MPa**; mutations in the **N-terminal GTPase domain** impaired Z-ring formation under HHP (cui2024nterminusgtpasedomain pages 1-2). This supports explicit curation of FtsZ-domain features → Z-ring stability → cell division under HHP.

#### 5) Extremes relevant to astrobiology: gene regulation at 158 MPa (2024)
A 2024 transcriptome study exposed *Shewanella oneidensis* MR-1 to **158 MPa** (Titan-relevant) and reports MR-1 remains metabolically active and can show viable growth following 2 h exposure, with regulation of hundreds of genes including membrane reconfiguration and stress responses (malas2024biologicalfunctionsat pages 1-2). While this does not establish a long-term growth range at 158 MPa, it supports boundary-case separation between survival/metabolic activity and sustained growth.

### Key quantitative examples & statistics (recent and foundational)
* **Hydrostatic pressure context:** deep sea (>1,000 m) is typically >**10 MPa**, and pressure increases ~**1 MPa per 100 m** (tamby2023microbialmembranelipid pages 1-2). The highest explored natural deep-sea habitat is ~**110 MPa** at Challenger Deep (malas2024biologicalfunctionsat pages 1-2).
* **Trait-defining bounded growth ranges:**
  * *Colwellia marinimaniae* MTCD1 grows **80–140 MPa** with an **optimum at 120 MPa** (a canonical example of a bounded growth-supporting pressure span) (peoples2020distinctivegeneand pages 1-2).
  * *Halomonas titanicae* ANRCS81 grows **0.1–55 MPa**, with maximal growth reported at **35 MPa** and measured growth rates across pressures (li2023strategyforthe pages 2-4).
* **Pressure-responsive envelope protein magnitude:** OmpH abundance increased **~10–100×** when pressure increased from **0.1 to 28 MPa** (scheffer2023themysteryof pages 7-9).
* **Pressure-associated lipid shift magnitude:** in *Marinobacter hydrocarbonoclasticus*, unsaturated wax esters were **~46% at 35 MPa** vs **3% at atmospheric pressure**, consistent with increased unsaturation under pressure (scheffer2023themysteryof pages 9-10).
* **Biophysical data for piezolyte-like stabilization:** in a piezophilic system accumulating mannosyl-glycerate (MG), hydration-water diffusion coefficients under pressure decrease less when MG is present (quantified at 400 bar), supporting osmolyte limitation of pressure-induced hydration mobility changes (peters2023effectsofcrowding pages 47-50).

### Current applications and real-world implementations
* **Deep-sea ecology and biogeochemical cycling:** Pressure tolerance and the resulting pressure range shapes whether taxa can be active on sinking particles or in hadal sediments; pressure can suppress respiration and restructure microbial communities, impacting carbon processing at depth (context for why pressure-range traits matter in situ) (malas2024biologicalfunctionsat pages 1-2).
* **Astrobiology / icy-ocean habitability assessments:** Titan’s subsurface ocean pressures are modeled ≥**150 MPa**, motivating experiments at ~158 MPa to determine whether terrestrial microbes can remain active and what mechanisms might support function; this connects pressure range and mechanistic nodes (membrane remodeling, stress responses) to life-detection and habitability modeling (malas2024biologicalfunctionsat pages 1-2).
* **Biotechnology (emerging, indirect):** Mechanistic insights (lipid remodeling, osmolytes, pressure-tolerant enzymes/proteomes) inform extremophile chassis/enzymes for industrial processes operating under nonstandard conditions; however, direct industrial implementations tied specifically to *growth pressure range* remain less explicit in the retrieved corpus and should be curated cautiously.

### Expert synthesis / authoritative analysis (what experts emphasize)
* **No single universal adaptation:** membrane strategies (PUFAs, MUFAs, branching, headgroups) vary by lineage, and some taxa show opposite PUFA regulation under HHP—so causal graphs should encode **taxon-specific** or **contextual** edges rather than universal ones (tamby2023microbialmembranelipid pages 2-4, tamby2023microbialmembranelipid pages 6-7).
* **Mechanistic coupling of pressure and temperature:** expert reviews emphasize that pressure effects are hard to disentangle from cold adaptation in deep-sea isolates (tamby2023microbialmembranelipid pages 1-2, scheffer2023themysteryof pages 6-7).
* **Pressure acts strongly through hydration/volume effects:** high pressure alters protein hydration/void volumes and membrane order; compatible solutes influence hydration dynamics and protein energy landscapes, providing a mechanistic basis for “piezolytes” beyond descriptive taxonomy (peters2023effectsofcrowding pages 50-52, scheffer2023themysteryof pages 9-10).

---

## Candidate causal-graph nodes (grouped by type)

### Trait node
* **pressure range** (TraitMech: **traitmech:000005**) — bounded min/max hydrostatic pressures supporting growth (peoples2020distinctivegeneand pages 1-2, li2023strategyforthe pages 2-4).

### Environmental / experimental context nodes
* **High hydrostatic pressure (HHP)** (label-only; can also reference “hydrostatic pressure” as an environmental variable) (tamby2023microbialmembranelipid pages 1-2, malas2024biologicalfunctionsat pages 1-2).
* **Deep-sea environment** (ENVO term suggested; label-only if not mapped) (tamby2023microbialmembranelipid pages 1-2).
* **Temperature** (confounder and interacting variable) (scheffer2023themysteryof pages 6-7, tamby2023microbialmembranelipid pages 1-2).
* **Electron acceptor availability** (O2 vs nitrate vs TMAO) (li2023strategyforthe pages 2-4, liu2023thetorrstwo pages 1-2).

### Molecular / chemical nodes (CHEBI-groundable)
* **Trimethylamine N-oxide (TMAO)** (CHEBI:15724) (peters2023effectsofcrowding pages 50-52, scheffer2023themysteryof pages 9-10).
* **Betaine** (CHEBI:17750) (scheffer2023themysteryof pages 9-10).
* **L-glutamate** (CHEBI:29991) (scheffer2023themysteryof pages 9-10).
* **β-hydroxybutyrate** (CHEBI:15946) (scheffer2023themysteryof pages 9-10).
* **Unsaturated fatty acids** (CHEBI:27208), **branched-chain fatty acids** (CHEBI:35819), **PUFAs** (CHEBI:36315) (tamby2023microbialmembranelipid pages 2-4, scheffer2023themysteryof pages 7-9).
* **Nitrate/nitrite** (CHEBI:17632 / CHEBI:16301) (li2023strategyforthe pages 8-10).
* **Reactive oxygen species (ROS)** (CHEBI:26523) (li2023strategyforthe pages 1-2).

### Genes/proteins/complexes (ground where possible; otherwise label-only)
* **pfa operon / ω-3 PUFA synthase** (label-only; KEGG/RefSeq varies) (scheffer2023themysteryof pages 6-7).
* **Δ9 acyl-phospholipid desaturase** (label-only) (scheffer2023themysteryof pages 6-7).
* **OmpH porin** (label-only) (scheffer2023themysteryof pages 7-9).
* **TorRS two-component system** (label-only) and **torA (TMAO reductase)** (label-only) (liu2023thetorrstwo pages 1-2).
* **FtsZ** (cell division cytoskeleton protein) (label-only UniProt per taxon) (cui2024nterminusgtpasedomain pages 1-2).
* **NADH dehydrogenase I (nuo operon)** (KEGG K00330–K00346 block; label-only for the operon as a node) (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7).
* **Antioxidant genes/regulators:** **sod1/sod2**, **oxyR**, **soxR** (label-only gene nodes) (li2023strategyforthe pages 6-8).

### Processes/functions (GO-groundable)
* **Homeoviscous adaptation** (label-only but aligns to membrane-fluidity regulation concepts) (tamby2023microbialmembranelipid pages 2-4, peters2023effectsofcrowding pages 24-26).
* **Response to oxidative stress** (GO:0006979) (li2023strategyforthe pages 6-8).
* **Protein stabilization / preferential hydration** (GO:0044380 suggested for “protein stabilization”; preferential hydration as label-only mechanism) (peters2023effectsofcrowding pages 50-52, scheffer2023themysteryof pages 9-10).
* **Division septum assembly / cell division under HHP** (GO:0000917 suggested) (cui2024nterminusgtpasedomain pages 1-2).

---

## Candidate evidence-backed causal edges
The following table is designed for direct curation into `data/traits/environment/pressure_range.yaml`.

| Subject node | Predicate | Object node | Evidence (short snippet) | Reference (DOI, year, URL) | Curation notes/uncertainty | Suggested identifiers (CURIEs) for subject/object when possible |
|---|---|---|---|---|---|---|
| polyunsaturated fatty acid biosynthesis | increases | membrane fluidity under HHP | “PUFAs… associated with adaptation to HHP are C20:5 and C22:6” (tamby2023microbialmembranelipid pages 2-4) | 10.3389/fmolb.2022.1058381, 2023, https://doi.org/10.3389/fmolb.2022.1058381 | Broad mechanism across taxa; supports intermediate node more directly than trait endpoint | Subject: GO:0006636; Object: label-only candidate “membrane fluidity under HHP” |
| pfa operon | enables increased ω-3 PUFA synthesis | unsaturated membrane lipids | “increase in ω-3 polyunsaturated fatty acids… linked to the pfa operon encoding an ω-3 PUFA synthase” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Gene cluster identity may vary by taxon; curate as taxon-sensitive mechanism | Subject: KEGG module/gene cluster label-only “pfa operon”; Object: CHEBI:36315 polyunsaturated fatty acid |
| delta-9 acyl-phospholipid desaturase | promotes synthesis of | unsaturated fatty acids | “Only piezophilic Colwellia contained a δ-9-acyl-phospholipid-desaturase gene promoting unsaturated fatty acid synthesis” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Strong taxon-specific genomic association; not universal across piezophiles | Subject: label-only candidate “delta-9 acyl-phospholipid desaturase”; Object: CHEBI:27208 unsaturated fatty acid |
| unsaturated membrane lipids | positively regulates | growth at high hydrostatic pressure | “mutants with reduced C18:1 could not [withstand] high pressure” and unsaturation counters pressure ordering (tamby2023microbialmembranelipid pages 6-7, peters2023effectsofcrowding pages 24-26) | 10.3389/fmolb.2022.1058381, 2023, https://doi.org/10.3389/fmolb.2022.1058381; 10.1021/acs.chemrev.3c00432, 2023, https://doi.org/10.1021/acs.chemrev.3c00432 | Mechanistic but composite; endpoint is growth/tolerance rather than directly numeric range | Subject: CHEBI:27208; Object: traitmech:000005 pressure range |
| branched-chain fatty acid increase | increases | membrane fluidity under HHP | “increase in branched iso- and anteiso-fatty acids” under high pressure (scheffer2023themysteryof pages 7-9) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Supported in some taxa (e.g., P. elfii, Clostridium paradoxum), absent in others; uncertain generality | Subject: CHEBI:35819 branched-chain fatty acid; Object: label-only candidate “membrane fluidity under HHP” |
| increased membrane fluidity under HHP | expands | growth-supporting pressure range | Pressure compacts membranes; organisms “counter this by increasing unsaturated fatty acids to restore membrane disorder and function” (scheffer2023themysteryof pages 6-7, peters2023effectsofcrowding pages 24-26) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629; 10.1021/acs.chemrev.3c00432, 2023, https://doi.org/10.1021/acs.chemrev.3c00432 | Inferred bridge from biophysics to trait; suitable as higher-level causal edge | Subject: label-only candidate “membrane fluidity under HHP”; Object: traitmech:000005 pressure range |
| OmpH abundance | increases | membrane transport under pressure | “OmpH abundance increased ~10–100-fold when pressure rose from 0.1 MPa to 28 MPa” (scheffer2023themysteryof pages 7-9) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Functional consequence inferred as transport/outer-membrane adaptation; direct trait link weaker | Subject: label-only candidate “OmpH porin”; Object: GO:0055085 transmembrane transport |
| TorRS two-component system | positively regulates expression of | torA / TMAO reductase under HHP | “the induction of TMAO reductase by HHP is mediated through the TorRS system” (liu2023thetorrstwo pages 1-2) | 10.3389/fmicb.2023.1291578, 2023, https://doi.org/10.3389/fmicb.2023.1291578 | Strong direct regulatory evidence in Vibrio fluvialis; taxon-specific | Subject: label-only candidate “TorRS”; Object: UniProt/KEGG label-only candidate “torA” |
| torA / TMAO reductase expression | improves | pressure tolerance | “HHP-inducible TMAO reductase contributes to improved pressure tolerance” (liu2023thetorrstwo pages 10-10, liu2023thetorrstwo pages 1-2) | 10.3389/fmicb.2023.1291578, 2023, https://doi.org/10.3389/fmicb.2023.1291578 | Evidence combines current paper and cited prior work; curate with note that phenotype is tolerance/growth, not always full range | Subject: label-only candidate “torA / TMAO reductase”; Object: traitmech:000005 pressure range |
| trimethylamine N-oxide (TMAO) | stabilizes | proteins via preferential hydration | “TMAO is described as preferentially excluded from the protein hydration layer, causing preferential hydration” (peters2023effectsofcrowding pages 50-52) | 10.1021/acs.chemrev.3c00432, 2023, https://doi.org/10.1021/acs.chemrev.3c00432 | Strong biophysical mechanism; not microbe-specific | Subject: CHEBI:15724 trimethylamine N-oxide; Object: GO:0044380 protein stabilization |
| TMAO | increases | pressure tolerance | “TMAO is noted to increase pressure tolerance in some organisms” (scheffer2023themysteryof pages 9-10) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Moderate evidence; sometimes TMAO is respiratory substrate instead of piezolyte, so role must be context-annotated | Subject: CHEBI:15724; Object: traitmech:000005 pressure range |
| betaine / glutamate / β-hydroxybutyrate accumulation | stabilizes | proteins via preferential hydration | “compatible solutes act by displacing water molecules bound to proteins… ‘preferential hydration’” and examples include “glutamate, betaine, and β-hydroxybutyrate” (scheffer2023themysteryof pages 9-10) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Good review support; compound-specific concentrations often lacking | Subject: CHEBI:17750 betaine; CHEBI:29991 L-glutamate; CHEBI:15946 3-hydroxybutyrate; Object: GO:0044380 protein stabilization |
| betaine / glutamate / β-hydroxybutyrate accumulation | associated with growth at | 20–30 MPa | “detected when grown at 20–30 MPa (its growth optimum)” (scheffer2023themysteryof pages 9-10) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Association from Photobacterium profundum; direct causality to range expansion remains uncertain | Subject: CHEBI:17750 / CHEBI:29991 / CHEBI:15946; Object: label-only candidate “growth at 20–30 MPa” |
| antioxidant defense genes and SOD activity | mitigates | intracellular oxidative stress under HHP | “genes for antioxidant defenses… were upregulated” and “cellular SOD activity increases under HHP” at 40 MPa (li2023strategyforthe pages 1-2, li2023strategyforthe pages 6-8) | 10.1128/aem.01304-22, 2023, https://doi.org/10.1128/aem.01304-22 | Strong within Halomonas titanicae ANRCS81; likely broader but should be curated taxon-aware | Subject: GO:0006979 response to oxidative stress / EC 1.15.1.1 superoxide dismutase; Object: CHEBI:26523 reactive oxygen species |
| antioxidant defense genes and SOD activity | supports growth at | 40 MPa | “when the strain was incubated at 40 MPa, genes related to antioxidant defenses… were upregulated” (li2023strategyforthe pages 1-2, li2023strategyforthe pages 6-8) | 10.1128/aem.01304-22, 2023, https://doi.org/10.1128/aem.01304-22 | Correlative but experimentally grounded; not isolated by knockout | Subject: GO:0006979 / EC:1.15.1.1; Object: label-only candidate “growth at 40 MPa” |
| nitrate reduction / denitrification genes | increases | energy generation under HHP | “genes for… nitrogen metabolism (explicitly ‘dissimilatory nitrate reduction and denitrification’) are upregulated” (li2023strategyforthe pages 6-8, li2023strategyforthe pages 8-10) | 10.1128/aem.01304-22, 2023, https://doi.org/10.1128/aem.01304-22 | Strong transcriptomic/physiological evidence in one strain; causal step to trait likely indirect | Subject: GO:0042128 nitrate assimilation? / better label-only “dissimilatory nitrate reduction and denitrification genes”; Object: GO:0006091 generation of precursor metabolites and energy |
| nitrate/nitrite consumption with ammonium generation | supports | growth under HHP | “much higher nitrate/nitrite consumption with increased ammonia production at HHP” (li2023strategyforthe pages 8-10) | 10.1128/aem.01304-22, 2023, https://doi.org/10.1128/aem.01304-22 | Physiological support for functional nitrate respiration under HHP; endpoint generalized | Subject: CHEBI:17632 nitrate / CHEBI:16301 nitrite; Object: traitmech:000005 pressure range |
| FtsZ N-terminal GTPase domain residues | maintains | Z-ring stability at 50 MPa | “identified five residues in the N-terminal GTPase domain… whose mutation would impair the Z-ring formation under HHP”; FtsZSb filaments “more stable… under 50 MPa” (cui2024nterminusgtpasedomain pages 1-2) | 10.3389/fmicb.2024.1441398, 2024, https://doi.org/10.3389/fmicb.2024.1441398 | Strong mechanistic evidence for cell-division adaptation; direct effect on range is inferred | Subject: UniProt/GO label-only “FtsZ”; Object: GO:0000921 septin ring organization? better label-only “Z-ring stability” |
| Z-ring stability under HHP | enables | cell division under HHP | “HHP hardly affected the Z-ring formation of FtsZSb” in obligate piezophile (cui2024nterminusgtpasedomain pages 1-2) | 10.3389/fmicb.2024.1441398, 2024, https://doi.org/10.3389/fmicb.2024.1441398 | Good mechanistic bridge; curate as process node linked to division | Subject: label-only candidate “Z-ring stability”; Object: GO:0000917 division septum assembly |
| more basic and hydrophobic proteome | stabilizes | proteins under extreme pressure | “more basic and hydrophobic proteome… may stabilize proteins and limit water intrusion under high pressure” (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7) | 10.1186/s12864-020-07102-y, 2020, https://doi.org/10.1186/s12864-020-07102-y | Comparative genomic inference, not direct manipulation; still highly relevant for extreme piezophily | Subject: label-only candidate “basic/hydrophobic proteome”; Object: GO:0044380 protein stabilization |
| more basic and hydrophobic proteome | associated with growth across | 80–140 MPa | MTCD1 “grows from 80 to 140 MPa with an optimum at 120 MPa” and piezophiles show such proteome features (peoples2020distinctivegeneand pages 1-2) | 10.1186/s12864-020-07102-y, 2020, https://doi.org/10.1186/s12864-020-07102-y | Association at genus/strain level; not direct proof of causation | Subject: label-only candidate “basic/hydrophobic proteome”; Object: traitmech:000005 pressure range |
| NADH dehydrogenase I (nuo operon) presence | increases | proton translocation / energy conservation | “nuo dehydrogenase… present only in the piezophiles” and linked to respiratory adaptation (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7) | 10.1186/s12864-020-07102-y, 2020, https://doi.org/10.1186/s12864-020-07102-y | Genomic association, mechanism plausible via proton pumping; direct phenotype test lacking | Subject: KEGG:K00330-K00346 label-only “nuo operon”; Object: GO:0015986 ATP synthesis coupled proton transport |
| tad pilus | contributes to | deep-sea particle/host association fitness | “a tad pilus only present in the piezophiles” (peoples2020distinctivegeneand pages 1-2) | 10.1186/s12864-020-07102-y, 2020, https://doi.org/10.1186/s12864-020-07102-y | Ecological/fitness association, not a direct pressure-range mechanism; flag uncertain for TraitMech | Subject: label-only candidate “tad pilus”; Object: GO:0044403 symbiont process / label-only “particle-host association” |


*Table: This table compiles candidate subject-predicate-object edges for curating the microbial trait pressure range, with short evidence snippets, DOI-first references, and ontology grounding suggestions. It emphasizes mechanisms with the strongest current support and flags taxon-specific or indirect ecological claims.*

### Visual evidence (membrane adaptation schematic + cross-taxon summary)
* Tamby et al. provide a schematic and tabular summary of lipid adaptations (unsaturation/PUFAs/branching) used as mechanistic support for membrane-related nodes and edges (tamby2023microbialmembranelipid media 0d6dd688, tamby2023microbialmembranelipid media d89ff60b).

---

## Warnings / claims to treat as uncertain (not yet ready for strong curation)
1. **Temperature vs pressure causality:** lipid remodeling (including pfa operon responses) can be induced by cold; pressure attribution should be curated as **context-dependent** unless experiments explicitly disentangle drivers (scheffer2023themysteryof pages 6-7, tamby2023microbialmembranelipid pages 1-2).
2. **Ecological association nodes (e.g., tad pilus):** evidence supports presence/enrichment in piezophiles but direct causal impact on the numeric **pressure range** is indirect (fitness/association), so these edges should be marked **uncertain** or excluded from TraitMech unless explicitly tied to growth bounds (peoples2020distinctivegeneand pages 1-2).
3. **Proteome composition as mechanism:** “more basic/hydrophobic proteome” is a strong comparative-genomic hypothesis but not an experimentally perturbed mechanism; curate as **inferred** unless validated by functional tests (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7).
4. **Pressure tolerance vs growth range:** many studies report increased tolerance or viability after exposure; only curate into **pressure range** when replication/growth is measured across pressures (malas2024biologicalfunctionsat pages 1-2).

---

## DOI-first bibliography (with publication dates and URLs)

1. **Cui X-H, et al.** (Aug 2024). *N-terminus GTPase domain of the cytoskeleton protein FtsZ plays a critical role in its adaptation to high hydrostatic pressure.* **Frontiers in Microbiology.** DOI: **10.3389/fmicb.2024.1441398**. https://doi.org/10.3389/fmicb.2024.1441398 (cui2024nterminusgtpasedomain pages 1-2)
2. **Malas J, et al.** (Feb 2024). *Biological functions at high pressure: transcriptome response of Shewanella oneidensis MR-1 to hydrostatic pressure relevant to Titan and other icy ocean worlds.* **Frontiers in Microbiology.** DOI: **10.3389/fmicb.2024.1293928**. https://doi.org/10.3389/fmicb.2024.1293928 (malas2024biologicalfunctionsat pages 1-2)
3. **Tamby A, Damsté JSS, Villanueva L.** (Jan 2023). *Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment.* **Frontiers in Molecular Biosciences.** DOI: **10.3389/fmolb.2022.1058381**. https://doi.org/10.3389/fmolb.2022.1058381 (tamby2023microbialmembranelipid pages 2-4)
4. **Scheffer G, Gieg LM.** (Jun 2023). *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface.* **Microorganisms.** DOI: **10.3390/microorganisms11071629**. https://doi.org/10.3390/microorganisms11071629 (scheffer2023themysteryof pages 1-2)
5. **Li J, et al.** (Mar 2023). *Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain Halomonas titanicae ANRCS81.* **Applied and Environmental Microbiology.** DOI: **10.1128/aem.01304-22**. https://doi.org/10.1128/aem.01304-22 (li2023strategyforthe pages 2-4)
6. **Liu N, et al.** (Nov 2023). *The TorRS two component system regulates expression of TMAO reductase in response to high hydrostatic pressure in Vibrio fluvialis.* **Frontiers in Microbiology.** DOI: **10.3389/fmicb.2023.1291578**. https://doi.org/10.3389/fmicb.2023.1291578 (liu2023thetorrstwo pages 1-2)
7. **Peters J, et al.** (Nov 2023). *Effects of Crowding and Cosolutes on Biomolecular Function at Extreme Environmental Conditions.* **Chemical Reviews.** DOI: **10.1021/acs.chemrev.3c00432**. https://doi.org/10.1021/acs.chemrev.3c00432 (peters2023effectsofcrowding pages 50-52)
8. **Peoples LM, et al.** (Oct 2020). *Distinctive gene and protein characteristics of extremely piezophilic Colwellia.* **BMC Genomics.** DOI: **10.1186/s12864-020-07102-y**. https://doi.org/10.1186/s12864-020-07102-y (peoples2020distinctivegeneand pages 1-2)



References

1. (peoples2020distinctivegeneand pages 1-2): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

2. (li2023strategyforthe pages 2-4): Jiakang Li, Xiang Xiao, Meng Zhou, and Yu Zhang. Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain halomonas titanicae anrcs81. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01304-22, doi:10.1128/aem.01304-22. This article has 17 citations and is from a peer-reviewed journal.

3. (scheffer2023themysteryof pages 1-2): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

4. (tamby2023microbialmembranelipid pages 1-2): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

5. (malas2024biologicalfunctionsat pages 1-2): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

6. (scheffer2023themysteryof pages 6-7): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

7. (tamby2023microbialmembranelipid pages 2-4): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

8. (peters2023effectsofcrowding pages 24-26): Judith Peters, Rosario Oliva, Antonino Caliò, Philippe Oger, and Roland Winter. Effects of crowding and cosolutes on biomolecular function at extreme environmental conditions. Chemical reviews, 123:13441-13488, Nov 2023. URL: https://doi.org/10.1021/acs.chemrev.3c00432, doi:10.1021/acs.chemrev.3c00432. This article has 46 citations and is from a highest quality peer-reviewed journal.

9. (scheffer2023themysteryof pages 7-9): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

10. (li2023strategyforthe pages 1-2): Jiakang Li, Xiang Xiao, Meng Zhou, and Yu Zhang. Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain halomonas titanicae anrcs81. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01304-22, doi:10.1128/aem.01304-22. This article has 17 citations and is from a peer-reviewed journal.

11. (li2023strategyforthe pages 6-8): Jiakang Li, Xiang Xiao, Meng Zhou, and Yu Zhang. Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain halomonas titanicae anrcs81. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01304-22, doi:10.1128/aem.01304-22. This article has 17 citations and is from a peer-reviewed journal.

12. (li2023strategyforthe pages 8-10): Jiakang Li, Xiang Xiao, Meng Zhou, and Yu Zhang. Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain halomonas titanicae anrcs81. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01304-22, doi:10.1128/aem.01304-22. This article has 17 citations and is from a peer-reviewed journal.

13. (scheffer2023themysteryof pages 9-10): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

14. (peters2023effectsofcrowding pages 50-52): Judith Peters, Rosario Oliva, Antonino Caliò, Philippe Oger, and Roland Winter. Effects of crowding and cosolutes on biomolecular function at extreme environmental conditions. Chemical reviews, 123:13441-13488, Nov 2023. URL: https://doi.org/10.1021/acs.chemrev.3c00432, doi:10.1021/acs.chemrev.3c00432. This article has 46 citations and is from a highest quality peer-reviewed journal.

15. (cui2024nterminusgtpasedomain pages 1-2): Xue-Hua Cui, Yu-Chen Wei, Xue-Gong Li, Xiao-Qing Qi, Long-Fei Wu, and Wei-Jia Zhang. N-terminus gtpase domain of the cytoskeleton protein ftsz plays a critical role in its adaptation to high hydrostatic pressure. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1441398, doi:10.3389/fmicb.2024.1441398. This article has 1 citations and is from a peer-reviewed journal.

16. (tamby2023microbialmembranelipid pages 6-7): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

17. (tamby2023microbialmembranelipid media 0d6dd688): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

18. (tamby2023microbialmembranelipid media d89ff60b): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

19. (liu2023thetorrstwo pages 1-2): Na Liu, Ting Jiang, Wen-Peng Cui, Xiao-Qing Qi, Xue-Gong Li, Yuan Lu, Long-Fei Wu, and Wei-Jia Zhang. The torrs two component system regulates expression of tmao reductase in response to high hydrostatic pressure in vibrio fluvialis. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1291578, doi:10.3389/fmicb.2023.1291578. This article has 3 citations and is from a peer-reviewed journal.

20. (peters2023effectsofcrowding pages 47-50): Judith Peters, Rosario Oliva, Antonino Caliò, Philippe Oger, and Roland Winter. Effects of crowding and cosolutes on biomolecular function at extreme environmental conditions. Chemical reviews, 123:13441-13488, Nov 2023. URL: https://doi.org/10.1021/acs.chemrev.3c00432, doi:10.1021/acs.chemrev.3c00432. This article has 46 citations and is from a highest quality peer-reviewed journal.

21. (peoples2020distinctivegeneand pages 5-7): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

22. (liu2023thetorrstwo pages 10-10): Na Liu, Ting Jiang, Wen-Peng Cui, Xiao-Qing Qi, Xue-Gong Li, Yuan Lu, Long-Fei Wu, and Wei-Jia Zhang. The torrs two component system regulates expression of tmao reductase in response to high hydrostatic pressure in vibrio fluvialis. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1291578, doi:10.3389/fmicb.2023.1291578. This article has 3 citations and is from a peer-reviewed journal.