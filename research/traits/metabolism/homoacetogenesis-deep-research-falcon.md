---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:58:49.006033'
end_time: '2026-06-18T05:09:17.135849'
duration_seconds: 628.13
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Homoacetogenesis
  trait_identifier: METPO:1000846
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: homoacetogenesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which acetate is produced as the sole reduced end product
    from reduction of CO2 via the acetyl-CoA pathway.
  parent_traits: METPO:1000060
  synonyms: Reductive acetyl-CoA pathway, Wood-Ljungdahl pathway
  evidence_summary: 'DOI:10.1016/j.tibtech.2019.05.008: two mol of carbon dioxide
    are reduced to one mol of acetyl-CoA (Review supports Wood-Ljungdahl reduction
    of CO2 to acetyl-CoA and acetate.) | DOI:10.1016/j.bbapap.2008.08.012: Wood-Ljungdahl
    Pathway of CO2 Fixation (Review supports acetogens using the Wood-Ljungdahl pathway
    for CO2 fixation.)'
  causal_graph_summary: 'homoacetogenesis_wood_ljungdahl_acetate: 9 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Homoacetogenesis
- **METPO identifier:** METPO:1000846
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which acetate is produced as the sole reduced end product from reduction of CO2 via the acetyl-CoA pathway.
- **Parent traits:** METPO:1000060
- **Synonyms:** Reductive acetyl-CoA pathway, Wood-Ljungdahl pathway
- **Existing evidence:** DOI:10.1016/j.tibtech.2019.05.008: two mol of carbon dioxide are reduced to one mol of acetyl-CoA (Review supports Wood-Ljungdahl reduction of CO2 to acetyl-CoA and acetate.) | DOI:10.1016/j.bbapap.2008.08.012: Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogens using the Wood-Ljungdahl pathway for CO2 fixation.)
- **Existing causal graph summary:** homoacetogenesis_wood_ljungdahl_acetate: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **Homoacetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/homoacetogenesis.yaml`.

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
- **Trait label:** Homoacetogenesis
- **METPO identifier:** METPO:1000846
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which acetate is produced as the sole reduced end product from reduction of CO2 via the acetyl-CoA pathway.
- **Parent traits:** METPO:1000060
- **Synonyms:** Reductive acetyl-CoA pathway, Wood-Ljungdahl pathway
- **Existing evidence:** DOI:10.1016/j.tibtech.2019.05.008: two mol of carbon dioxide are reduced to one mol of acetyl-CoA (Review supports Wood-Ljungdahl reduction of CO2 to acetyl-CoA and acetate.) | DOI:10.1016/j.bbapap.2008.08.012: Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogens using the Wood-Ljungdahl pathway for CO2 fixation.)
- **Existing causal graph summary:** homoacetogenesis_wood_ljungdahl_acetate: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **Homoacetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/homoacetogenesis.yaml`.

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


## Microbial trait causal-graph research report: Homoacetogenesis (METPO:1000846)

### 1) Scope summary (trait meaning, boundaries, assays)

**Trait definition (what is being captured).** Homoacetogenesis is the physiological capacity to conserve energy and grow (or maintain metabolism) by **reducing CO2 via the Wood–Ljungdahl pathway (WLP; reductive acetyl‑CoA pathway) such that acetate is the main/sole reduced end product**, with acetyl‑CoA as the central intermediate. In acetogens, the canonical overall stoichiometry is described as **4 H2 + 2 CO2 → CH3COOH + 2 H2O**, with ΔG0′ reported around **−104 kJ** under standard conditions in a 2023 review of an obligately autotrophic acetogen. (frolov2023obligateautotrophyat pages 1-2)

**Trait as a TraitMech phenotype.** For curation, homoacetogenesis is best treated as a **metabolic capability** evidenced by one or more of:
- Growth (or sustained acetate formation) under **H2 + CO2** atmosphere with acetate production. (boer2024isolationandcharacterization pages 1-2, frolov2023obligateautotrophyat pages 1-2)
- Genomic/enzymatic evidence of a **complete WLP** plus appropriate energy-conservation modules (Rnf- or Ech-based), with compatible redox carriers (ferredoxin, NADH). (bae2024harnessingacetogenicbacteria pages 2-3, frolov2023obligateautotrophyat pages 1-2)

**Boundary cases / nearby traits (what it is not).**
- **Not methanogenesis:** both compete for H2/CO2, but methanogens generally have higher H2 affinity and additional energy-conserving steps; thus “acetogenesis” is often less competitive in mixed communities unless conditions suppress methanogenesis. (ferretti2025bioelectrochemicalconversionof pages 19-23)
- **Not heterotrophic acetogenesis / mixotrophy:** many acetogens also run WLP as an electron sink during heterotrophic growth, producing acetate plus other products. The strict “sole reduced end product” criterion can be violated when ethanol, lactate, etc. are formed. This matters for trait assignment: e.g., Terrisporobacter isolate COMᵀ produced ethanol in addition to acetate under H2-supplemented conditions, suggesting the phenotype can deviate from “sole end product” depending on strain/conditions. (boer2024isolationandcharacterization pages 1-2)
- **Not syntrophic acetate oxidation (reverse WLP):** not covered by the retrieved evidence set; should be treated as a distinct trait until specifically supported.

### 2) Key concepts and current understanding (mechanism-focused)

#### 2.1 Core pathway architecture: WLP methyl + carbonyl branches
A 2024 chemostat study in *Clostridium autoethanogenum* describes the WLP as **two converging branches**: an “eastern/methyl” branch reducing CO2 to formate and onward to methyl‑tetrahydrofolate, and a “western/carbonyl” branch reducing CO2 to CO (or using CO directly), which converge at the **ACS/CODH (acetyl‑CoA synthase / carbon monoxide dehydrogenase) complex**. (davin2024clostridiumautoethanogenumalters pages 1-2)

A 2024 review emphasizes the WLP’s efficiency and summarizes key steps, including: CO2 reduction to **formate** by formate dehydrogenase (**Fdh**), and conversion of formate to **formyl‑THF** by formyl‑THF synthetase (**Fhs**), culminating in acetyl‑CoA and acetate formation. (bae2024harnessingacetogenicbacteria pages 2-3)

#### 2.2 Redox and energy conservation: ATP-neutral WLP requires coupling to ion gradients
Multiple sources frame acetogenesis as **modular**: an electron-donating module, the reductive WLP, and a **membrane-associated energy conservation module** involving **Rnf or Ech** complexes plus ATP synthase. (frolov2023obligateautotrophyat pages 1-2, bae2024harnessingacetogenicbacteria pages 2-3)

A key bioenergetic point for the trait is that **acetate formation yields ATP by substrate-level phosphorylation**, but the WLP itself is described as **net ATP neutral**, so **chemiosmotic coupling (Rnf/Ech → ion gradient → ATP synthase)** is central to making homoacetogenesis viable. (bae2024harnessingacetogenicbacteria pages 2-3, frolov2023obligateautotrophyat pages 1-2)

#### 2.3 Electron supply: ferredoxin, NADH, and electron bifurcation
A 2024 review describes how reduced ferredoxin (Fdred) and NADH support WLP operation, and highlights **electron-bifurcating hydrogenases** that oxidize H2 to yield **both reduced ferredoxin and NADH**, linking exergonic and endergonic electron flows. (bae2024harnessingacetogenicbacteria pages 1-2, bae2024harnessingacetogenicbacteria pages 2-3)

It also states that **CODH oxidizes CO to CO2 and produces reduced ferredoxin**, connecting CO metabolism to the low-potential electron supply needed for CO2 reduction steps. (bae2024harnessingacetogenicbacteria pages 2-3)

### 3) Recent developments (prioritize 2023–2024)

#### 3.1 2024: Gas feed composition as a control knob for CO2 incorporation (industrial relevance)
A 2024 study established chemostats of *C. autoethanogenum* with a **novel high H2:CO uptake ratio (11:1)** vs. a lower (5:1) condition. It reports that higher H2:CO drives **higher CO2 utilization**, and that **≥75% of the carbon in ethanol** came from CO2 under the high H2:CO condition versus **~50%** under the lower condition. It also states that **H2:CO uptake ratios >2:1 are sufficient to achieve 100% carbon efficiency**. (davin2024clostridiumautoethanogenumalters pages 1-2)

Mechanistically, the study reports WLP protein abundance remained largely consistent between conditions while **redox/cofactor pathways and post-translational regulation (lysine acetylation)** appeared more important for fine tuning. (davin2024clostridiumautoethanogenumalters pages 1-2)

#### 3.2 2024: Functional genetics of key coupling points in a thermophilic acetogen (preprint)
A 2024 bioRxiv preprint in *Thermoanaerobacter kivui* provides trait-mechanistic evidence useful for causal-graph edges:
- WLP genes form a large operon beginning with **fhs** (formyl‑THF synthetase). (zeldes2024knockdownofgenes pages 1-4)
- **Energy conservation during WLP requires coupling** via **Rnf or Ech** complexes. (zeldes2024knockdownofgenes pages 1-4)
- *T. kivui* encodes two Ech gene clusters; an **Ech2 knockout cannot grow on CO or pyruvate**, interpreted as a defect in ferredoxin recycling when ferredoxin is the sole redox carrier. (zeldes2024knockdownofgenes pages 1-4)
- Repressing **fhs** expression caused **significant extracellular formate accumulation**, supporting a bottleneck at formate consumption. (zeldes2024knockdownofgenes pages 1-4)
- **Ech1** could not be knocked out (repeated failures), suggested as **essential** for energy conservation during acetogenesis; this is indirect and should be curated as uncertain until supported by direct conditional depletion/essentiality assays. (zeldes2024knockdownofgenes pages 1-4)

#### 3.3 2024: Expanding phenotypic coverage—new acetogenic isolates with H2-dependent acetogenesis
A 2024 Frontiers in Microbiology paper reports isolation of four acetogenic **Terrisporobacter** strains and one **Acetoanaerobium** strain, with explicit phenotype evidence: under a **H2 + CO2 atmosphere**, “continuous acetate production was indicative of H2-dependent acetogenesis.” (boer2024isolationandcharacterization pages 1-2)

### 4) Current applications and real-world implementations

#### 4.1 Industrial gas fermentation and C1 valorization
A 2024 review frames acetogens as platforms for converting **C1 substrates (CO2, CO, formate, methanol)** into chemicals via WLP, citing commercialization of *C. autoethanogenum* (e.g., industrial gas fermentation contexts). (bae2024harnessingacetogenicbacteria pages 2-3, davin2024clostridiumautoethanogenumalters pages 1-2)

#### 4.2 Process control for improved carbon capture
The 2024 *C. autoethanogenum* chemostat study is directly relevant for industrial implementation: manipulating **H2:CO uptake ratio** is presented as a lever to increase **CO2 incorporation into products** and overall carbon efficiency. (davin2024clostridiumautoethanogenumalters pages 1-2)

#### 4.3 Anaerobic and mixed-culture systems (competition with methanogens)
A bioelectrochemical review (2025; lower priority than 2023–2024 but relevant for applications) highlights that in mixed cultures methanogens often outcompete acetogens for H2 and that **methanogenesis inhibitors (e.g., BESA)** are used to favor acetogenesis/acetate accumulation. (ferretti2025bioelectrochemicalconversionof pages 19-23)

### 5) Relevant statistics and quantitative data (from retrieved sources)

**Thermodynamics / yields**
- Standard free energy for 4 H2 + 2 CO2 → acetate + 2 H2O is reported as **ΔG0′ = −104 kJ**. (frolov2023obligateautotrophyat pages 1-2)
- WLP reduction of CO2 to acetate in a bioelectrochemical review is reported **~ΔG°′ = −95 kJ·mol−1**. (ferretti2025bioelectrochemicalconversionof pages 19-23)
- An energetic estimate in a 2024 review states **~0.3 mol ATP per mol acetate from CO2/H2** (context: energetic limitation of acetogens). (bae2024harnessingacetogenicbacteria pages 2-3)

**Bioprocess / carbon incorporation**
- *C. autoethanogenum* chemostats: **11:1 vs 5:1 H2:CO uptake ratio**; **≥75% vs ~50%** of ethanol carbon from CO2 at high vs lower ratio; and a claim that **>2:1 H2:CO uptake ratio** is sufficient for **100% carbon efficiency**. (davin2024clostridiumautoethanogenumalters pages 1-2)

**Diversity / prevalence**
- A 2023 article states **“over 100 acetogens across 28 genera have been isolated.”** (frolov2023obligateautotrophyat pages 1-2)

### 6) Candidate nodes for TraitMech curation (grouped)

#### 6.1 Pathways / modules
- Wood–Ljungdahl pathway / reductive acetyl‑CoA pathway (label; KEGG/MetaCyc grounding recommended) (bae2024harnessingacetogenicbacteria pages 2-3, davin2024clostridiumautoethanogenumalters pages 1-2)
- WLP methyl branch (CO2 → formate → methyl‑THF intermediates) (davin2024clostridiumautoethanogenumalters pages 1-2)
- WLP carbonyl branch (CO2 → CO; CO utilization) (davin2024clostridiumautoethanogenumalters pages 1-2)
- Energy conservation module: Rnf-type vs Ech-type acetogens (frolov2023obligateautotrophyat pages 1-2, bae2024harnessingacetogenicbacteria pages 2-3)

#### 6.2 Genes / proteins / complexes (candidate nodes)
- Formate dehydrogenase (Fdh; EC 1.17.1.9) (bae2024harnessingacetogenicbacteria pages 2-3)
- Formyl‑THF synthetase / formate—THF ligase (Fhs; EC 6.3.4.3) (bae2024harnessingacetogenicbacteria pages 2-3, zeldes2024knockdownofgenes pages 1-4)
- CODH/ACS complex (EC 1.2.7.4 / 2.3.1.169; complex node) (davin2024clostridiumautoethanogenumalters pages 1-2, bae2024harnessingacetogenicbacteria pages 2-3)
- Electron‑bifurcating hydrogenase (Hyd; HydABC naming not explicit in extracted snippets, so gene-level grounding uncertain) (bae2024harnessingacetogenicbacteria pages 1-2, bae2024harnessingacetogenicbacteria pages 2-3)
- Rnf complex (ferredoxin:NAD+ oxidoreductase; ion-translocating) (bae2024harnessingacetogenicbacteria pages 2-3, frolov2023obligateautotrophyat pages 1-2)
- Ech (energy‑converting hydrogenase; Fd:H+ oxidoreductase) including *T. kivui* Ech1/Ech2 clusters (bae2024harnessingacetogenicbacteria pages 2-3, zeldes2024knockdownofgenes pages 1-4)
- ATP synthase (chemiosmotic phosphorylation) (frolov2023obligateautotrophyat pages 1-2, bae2024harnessingacetogenicbacteria pages 2-3)

#### 6.3 Chemicals / metabolites / electron donors & acceptors
- CO2 (CHEBI:16526), H2 (CHEBI:18276), CO (CHEBI:17245) (frolov2023obligateautotrophyat pages 1-2, davin2024clostridiumautoethanogenumalters pages 1-2, bae2024harnessingacetogenicbacteria pages 2-3)
- Formate (CHEBI:15740), acetyl‑CoA (label; CHEBI grounding recommended), acetate (CHEBI:15366) (bae2024harnessingacetogenicbacteria pages 2-3)
- Ferredoxin (CHEBI:36110), NADH (CHEBI:57945) (bae2024harnessingacetogenicbacteria pages 1-2, bae2024harnessingacetogenicbacteria pages 2-3)

#### 6.4 Environmental / experimental factors
- Strict anaerobiosis (qualitative; ENVO grounding recommended) (frolov2023obligateautotrophyat pages 1-2, ferretti2025bioelectrochemicalconversionof pages 19-23)
- Gas composition and **H2:CO uptake ratio** (process factor) (davin2024clostridiumautoethanogenumalters pages 1-2)
- H2 + CO2 atmosphere (culture condition) (boer2024isolationandcharacterization pages 1-2)
- pH range reported for acetogens (~5.7–7.8) in MES-focused review (use cautiously; secondary source) (ferretti2025bioelectrochemicalconversionof pages 19-23)
- Methanogen competition; methanogenesis inhibition by BESA (application constraint) (ferretti2025bioelectrochemicalconversionof pages 19-23)

### 7) Evidence-backed candidate causal edges (curation-ready)

The table below compiles proposed edges as subject–predicate–object triples with evidence, snippets, and curation notes.

| Edge (subject–predicate–object) | Entity type(s) | Suggested ontology grounding (CURIEs where known) | Evidence (paper, year, DOI, URL) | Supporting snippet (verbatim/near-verbatim) | Curation notes incl. uncertainty/taxon-specific |
|---|---|---|---|---|---|
| carbon dioxide — is reduced by formate dehydrogenase to — formate | chemical → enzyme activity → chemical | CHEBI:16526 carbon dioxide; EC:1.17.1.9 formate dehydrogenase; CHEBI:15740 formate | Bae et al., 2024, DOI:10.1039/d4cb00099d, https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) | “CO2 → formate catalyzed by formate dehydrogenase (Fdh)” | Core WLP methyl-branch step; broadly applicable to acetogens. Curate as pathway-level edge; specific Fdh isoforms vary by taxon. |
| formate — is converted by formyl-THF synthetase to — formyl-THF | chemical → enzyme activity → chemical | CHEBI:15740 formate; EC:6.3.4.3 formate--tetrahydrofolate ligase/Fhs; CHEBI:15637 tetrahydrofolate; candidate: formyl-THF | Bae et al., 2024, DOI:10.1039/d4cb00099d, https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3); Zeldes et al., 2024, DOI:10.1101/2024.06.18.598388, https://doi.org/10.1101/2024.06.18.598388 (zeldes2024knockdownofgenes pages 1-4) | “formate → formyl-THF by formyl-THF synthetase (Fhs)” ; “most WLP genes form a large operon beginning with formyl-THF synthetase (fhs)” | Strong pathway evidence. Compound identifier for formyl-THF may need curator confirmation. |
| methyl branch of WLP — converges with carbonyl branch at — ACS/CODH complex | pathway → complex → pathway junction | KEGG/MetaCyc candidate: Wood-Ljungdahl pathway; EC:1.2.7.4 CODH; EC:2.3.1.169 ACS; candidate complex: CODH/ACS | Davin et al., 2024, DOI:10.1186/s13068-024-02554-w, https://doi.org/10.1186/s13068-024-02554-w (davin2024clostridiumautoethanogenumalters pages 1-2) | “the two branches (eastern/methyl branch… and the carbonyl/western branch) meeting at the acetyl-CoA synthase/carbon monoxide dehydrogenase complex (ACS/CODH)” | High-confidence pathway architecture. Evidence from C. autoethanogenum but canonical for bacterial WLP. |
| carbon monoxide oxidation by CODH — produces — reduced ferredoxin | chemical/enzyme activity → redox carrier | CHEBI:17245 carbon monoxide; EC:1.2.7.4 carbon-monoxide dehydrogenase; CHEBI:36110 ferredoxin | Bae et al., 2024, DOI:10.1039/d4cb00099d, https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) | “CODH oxidizes CO to CO2 and produces reduced ferredoxin (Fdred)” | Useful mechanistic edge for CO-fed acetogenesis; may be substrate-context dependent. |
| electron-bifurcating hydrogenase — couples H2 oxidation to production of — NADH and reduced ferredoxin | enzyme complex/process → redox carriers | candidate HydABC; CHEBI:18276 hydrogen; CHEBI:57945 NADH; CHEBI:36110 ferredoxin | Bae et al., 2024, DOI:10.1039/d4cb00099d, https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) | “an electron-bifurcating hydrogenase (Hyd) oxidizes H2 to yield reduced Fd and NADH, linking exergonic and endergonic electron flows” | Good generic edge for acetogens; HydABC naming not explicit in cited context, so gene-level grounding should be marked uncertain. |
| Wood–Ljungdahl pathway — is ATP-neutral; acetate formation via acetate kinase — generates — ATP by substrate-level phosphorylation | pathway/process → energetic property/process | candidate WLP; EC:2.7.2.1 acetate kinase; CHEBI:15366 acetate; GO:candidate substrate-level phosphorylation | Bae et al., 2024, DOI:10.1039/d4cb00099d, https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) | “acetyl-CoA → acetate via acetyl-phosphate with ATP from substrate-level phosphorylation (acetate kinase), resulting in net-zero ATP from the WLP” | Important trait-defining energetic edge. Consider splitting into two edges in YAML: WLP ATP-neutral; acetate kinase generates ATP. |
| Rnf complex — generates — transmembrane ion gradient that drives ATP synthase | membrane complex → process → complex | candidate Rnf complex; GO:candidate ion transmembrane transport; EC:7.1.1.2/ferredoxin:NAD+ oxidoreductase candidate; EC:7.1.2.2 ATP synthase | Bae et al., 2024, DOI:10.1039/d4cb00099d, https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3); Frolov et al., 2023, DOI:10.3389/fmicb.2023.1185739, https://doi.org/10.3389/fmicb.2023.1185739 (frolov2023obligateautotrophyat pages 1-2) | “Rnf transfers electrons from Fdred to NAD+ while translocating Na+/H+” ; “membrane-associated energy-conservation module involving Rnf… plus ATP synthase” | Strong but acetogen-specific architecture varies (Rnf-type vs Ech-type). Curate as one alternative energy-conservation module. |
| Ech complex — generates — transmembrane ion gradient that drives ATP synthase | membrane complex → process → complex | candidate Ech complex; GO:candidate proton transmembrane transport; EC:1.12.7.- hydrogenase candidate; EC:7.1.2.2 ATP synthase | Bae et al., 2024, DOI:10.1039/d4cb00099d, https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3); Frolov et al., 2023, DOI:10.3389/fmicb.2023.1185739, https://doi.org/10.3389/fmicb.2023.1185739 (frolov2023obligateautotrophyat pages 1-2) | “Ech acts as an Fd:H+ oxidoreductase” ; “membrane-associated energy-conservation module involving… Ech… plus ATP synthase” | Alternative to Rnf in Ech-type acetogens; do not require both Rnf and Ech simultaneously for trait. |
| increased H2:CO uptake ratio — increases — CO2 utilization and carbon efficiency in Clostridium autoethanogenum | experimental/environmental factor → physiological outcome | candidate environmental factor: H2:CO uptake ratio; NCBITaxon:511683 Clostridium autoethanogenum | Davin et al., 2024, DOI:10.1186/s13068-024-02554-w, https://doi.org/10.1186/s13068-024-02554-w (davin2024clostridiumautoethanogenumalters pages 1-2) | “The study established chemostats with a high (11:1) H2:CO uptake ratio… Increased H2:CO drives higher CO2 utilization” ; “H2:CO uptake ratios >2:1 are sufficient to achieve 100% carbon efficiency” | Strong recent application/process edge, but organism- and reactor-condition-specific; curate as experimental-factor edge with taxon/process notes. |
| Ech2 knockout — impairs growth on — CO and pyruvate in Thermoanaerobacter kivui | gene/complex perturbation → phenotype/substrate utilization | candidate ech2 gene cluster; NCBITaxon:167785 Thermoanaerobacter kivui; CHEBI:17245 carbon monoxide; CHEBI:15361 pyruvate | Zeldes et al., 2024, DOI:10.1101/2024.06.18.598388, https://doi.org/10.1101/2024.06.18.598388 (zeldes2024knockdownofgenes pages 1-4) | “an Ech2 knockout cannot grow on CO or pyruvate, indicating its role in ferredoxin recycling when ferredoxin is the sole redox carrier” | Strong functional genetics evidence but taxon-specific. Best curated as support for Ech-linked redox balancing rather than universal homoacetogenesis requirement. |
| repeated failure to knock out Ech1 — supports essentiality for — homoacetogenic growth in Thermoanaerobacter kivui | gene/complex perturbation evidence → phenotype | candidate ech1 gene cluster; NCBITaxon:167785 Thermoanaerobacter kivui | Zeldes et al., 2024, DOI:10.1101/2024.06.18.598388, https://doi.org/10.1101/2024.06.18.598388 (zeldes2024knockdownofgenes pages 1-4) | “Ech1 is hypothesized… to be the key coupling point to proton-motive-force energy conservation; repeated attempts to knock out ech1 failed, suggesting essentiality” | Evidence is indirect (failed knockout) and preprint; curate cautiously and mark uncertain/taxon-specific. |
| repression of fhs — causes accumulation of — formate in Thermoanaerobacter kivui | gene expression perturbation → metabolite accumulation | gene: fhs/EC:6.3.4.3; CHEBI:15740 formate; NCBITaxon:167785 Thermoanaerobacter kivui | Zeldes et al., 2024, DOI:10.1101/2024.06.18.598388, https://doi.org/10.1101/2024.06.18.598388 (zeldes2024knockdownofgenes pages 1-4) | “repression of fhs (growth on glucose) led to significant extracellular formate accumulation, demonstrating a metabolic bottleneck” | Strong causal support for Fhs consuming formate in vivo; preprint and taxon-specific but mechanistically compelling. |
| H2 + CO2 atmosphere — enables — H2-dependent acetogenesis with acetate production in Terrisporobacter isolates | environmental substrate condition → phenotype/metabolite output | CHEBI:18276 hydrogen; CHEBI:16526 carbon dioxide; CHEBI:15366 acetate; NCBITaxon:candidate Terrisporobacter | Böer et al., 2024, DOI:10.3389/fmicb.2024.1426882, https://doi.org/10.3389/fmicb.2024.1426882 (boer2024isolationandcharacterization pages 1-2) | “All Terrisporobacter isolates showed a characteristic growth pattern under a H2 + CO2 atmosphere” ; “continuous acetate production was indicative of H2-dependent acetogenesis” | Good phenotype-level edge for trait assignment in this genus. Not all Terrisporobacter may share identical end products; one isolate also produced ethanol. |
| acetogens — use membrane-associated Rnf or Ech modules plus ATP synthase for — energy conservation during acetogenesis | trait/class → bioenergetic module | METPO:1000846 homoacetogenesis; candidate Rnf complex; candidate Ech complex; EC:7.1.2.2 ATP synthase | Frolov et al., 2023, DOI:10.3389/fmicb.2023.1185739, https://doi.org/10.3389/fmicb.2023.1185739 (frolov2023obligateautotrophyat pages 1-2); Bae et al., 2024, DOI:10.1039/d4cb00099d, https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) | “acetogenesis is modular… a membrane-associated energy-conservation module involving Rnf… or Ech… plus ATP synthase” | Good summary edge for trait graph backbone. Should likely be represented as several lower-level edges rather than one broad assertion. |


*Table: This table compiles candidate evidence-backed causal edges for homoacetogenesis centered on the Wood–Ljungdahl pathway, with recent and foundational support restricted to the specified context IDs. It is intended to help curate TraitMech-ready nodes and edges while flagging taxon-specific or uncertain claims.*

### 8) Expert opinions and analysis (authoritative synthesis)

**Energetic limitation is central.** Across sources, acetogens are portrayed as operating near thermodynamic limits, with WLP ATP-neutrality necessitating coupling to membrane energy conservation (Rnf or Ech) and ATP synthase to make growth possible; this theme is explicit in both 2023 and 2024 reviews. (frolov2023obligateautotrophyat pages 1-2, bae2024harnessingacetogenicbacteria pages 2-3)

**Engineering and process control focus on redox/ATP availability.** The 2024 review explicitly frames “enhancing ATP and redox availability” as a major lever for improving acetogenic C1 conversion performance, while the 2024 chemostat study shows that large changes in CO2 incorporation can be achieved by adjusting gas feed ratios with only modest changes in WLP protein abundance—suggesting regulation is distributed across redox/cofactor networks and PTMs rather than only WLP enzyme levels. (bae2024harnessingacetogenicbacteria pages 2-3, davin2024clostridiumautoethanogenumalters pages 1-2)

### 9) Warnings / do-not-curate-yet flags

1. **Preprint-only functional genetics:** The *T. kivui* knock-down/essentiality inferences (e.g., Ech1 essentiality inferred from failed knockouts; knock-down constructs) are from bioRxiv and should be curated as **uncertain** until peer-reviewed replication. (zeldes2024knockdownofgenes pages 1-4)
2. **“Sole reduced end product” vs observed product spectra:** Some strains/conditions produce ethanol or other reduced products alongside acetate (e.g., Terrisporobacter isolate COMᵀ). Curate homoacetogenesis as a capacity that can be condition-dependent; treat “sole end product” as assay-specific. (boer2024isolationandcharacterization pages 1-2)
3. **HydABC/HDCR/CoFeSP granularity:** Several commonly cited WLP components (CoFeSP, HDCR naming) are not explicitly evidenced in the retrieved snippets; avoid curating those nodes/edges until directly supported by accessible primary literature in the evidence set.

---

## DOI-first bibliography (with dates/URLs)

1. Frolov EN, et al. **Obligate autotrophy at the thermodynamic limit of life in a new acetogenic bacterium.** *Frontiers in Microbiology* (May 2023). DOI: **10.3389/fmicb.2023.1185739**. URL: https://doi.org/10.3389/fmicb.2023.1185739 (frolov2023obligateautotrophyat pages 1-2)
2. Bae J, Park C, Jung H, Jin S, Cho B-K. **Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production.** *RSC Chemical Biology* (Jul 2024). DOI: **10.1039/d4cb00099d**. URL: https://doi.org/10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3, bae2024harnessingacetogenicbacteria pages 1-2)
3. Davin ME, et al. **Clostridium autoethanogenum alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated H2:CO feedstock ratios for enhancing carbon capture efficiency.** *Biotechnology for Biofuels and Bioproducts* (Sep 2024). DOI: **10.1186/s13068-024-02554-w**. URL: https://doi.org/10.1186/s13068-024-02554-w (davin2024clostridiumautoethanogenumalters pages 1-2)
4. Böer T, et al. **Isolation and characterization of novel acetogenic strains of the genera Terrisporobacter and Acetoanaerobium.** *Frontiers in Microbiology* (Jul 2024). DOI: **10.3389/fmicb.2024.1426882**. URL: https://doi.org/10.3389/fmicb.2024.1426882 (boer2024isolationandcharacterization pages 1-2)
5. Zeldes B, et al. **Knock-down of genes essential for homoacetogenic growth using sugar inducible promoters in the thermophile Thermoanaerobacter kivui.** *bioRxiv* (Jun 2024). DOI: **10.1101/2024.06.18.598388**. URL: https://doi.org/10.1101/2024.06.18.598388 (preprint) (zeldes2024knockdownofgenes pages 1-4)
6. Ferretti J. **Bioelectrochemical conversion of CO2 to acetate: innovative strategies for controlling methanogenesis in mixed and pure cultures.** (2025; journal not resolved in retrieved metadata). Used here only for contextual application constraints; prioritize peer-reviewed 2023–2024 sources for curation where possible. (ferretti2025bioelectrochemicalconversionof pages 19-23)


References

1. (frolov2023obligateautotrophyat pages 1-2): Evgenii N. Frolov, Alexander G. Elcheninov, Alexandra V. Gololobova, Stepan V. Toshchakov, Andrei A. Novikov, Alexander V. Lebedinsky, and Ilya V. Kublanov. Obligate autotrophy at the thermodynamic limit of life in a new acetogenic bacterium. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1185739, doi:10.3389/fmicb.2023.1185739. This article has 30 citations and is from a peer-reviewed journal.

2. (boer2024isolationandcharacterization pages 1-2): Tim Böer, Miriam Antonia Schüler, Alina Lüschen, Lena Eysell, Jannina Dröge, Melanie Heinemann, Lisa Engelhardt, Mirko Basen, Rolf Daniel, and Anja Poehlein. Isolation and characterization of novel acetogenic strains of the genera terrisporobacter and acetoanaerobium. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426882, doi:10.3389/fmicb.2024.1426882. This article has 18 citations and is from a peer-reviewed journal.

3. (bae2024harnessingacetogenicbacteria pages 2-3): Jiyun Bae, Chanho Park, Hyunwoo Jung, Sangrak Jin, and Byung-Kwan Cho. Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production. RSC Chemical Biology, 5:812-832, Jul 2024. URL: https://doi.org/10.1039/d4cb00099d, doi:10.1039/d4cb00099d. This article has 19 citations and is from a peer-reviewed journal.

4. (ferretti2025bioelectrochemicalconversionof pages 19-23): J Ferretti. Bioelectrochemical conversion of co₂ to acetate: innovative strategies for controlling methanogenesis in mixed and pure cultures. Unknown journal, 2025.

5. (davin2024clostridiumautoethanogenumalters pages 1-2): Megan E. Davin, R. Adam Thompson, Richard J. Giannone, Lucas W. Mendelson, Dana L. Carper, Madhavi Z. Martin, Michael E. Martin, Nancy L. Engle, Timothy J. Tschaplinski, Steven D. Brown, and Robert L. Hettich. Clostridium autoethanogenum alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated h2:co feedstock ratios for enhancing carbon capture efficiency. Biotechnology for Biofuels and Bioproducts, Sep 2024. URL: https://doi.org/10.1186/s13068-024-02554-w, doi:10.1186/s13068-024-02554-w. This article has 18 citations and is from a domain leading peer-reviewed journal.

6. (bae2024harnessingacetogenicbacteria pages 1-2): Jiyun Bae, Chanho Park, Hyunwoo Jung, Sangrak Jin, and Byung-Kwan Cho. Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production. RSC Chemical Biology, 5:812-832, Jul 2024. URL: https://doi.org/10.1039/d4cb00099d, doi:10.1039/d4cb00099d. This article has 19 citations and is from a peer-reviewed journal.

7. (zeldes2024knockdownofgenes pages 1-4): Benjamin Zeldes, Sabina Mittelstedt, Christoph Baum, Adilia Shakirova, Anja Poehlein, Rolf Daniel, Volker Müller, and Mirko Basen. Knock-down of genes essential for homoacetogenic growth using sugar inducible promoters in the thermophile thermoanaerobacter kivui. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.18.598388, doi:10.1101/2024.06.18.598388. This article has 2 citations.