---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:37:01.741309'
end_time: '2026-06-18T04:58:47.313810'
duration_seconds: 1305.57
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dissimilatory manganese reduction
  trait_identifier: traitmech:000108
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dissimilatory_manganese_reduction
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which an organism conserves energy
    by reducing Mn(IV) oxides to soluble Mn(II) as a terminal electron acceptor while
    oxidizing organic matter or hydrogen.
  parent_traits: traitmech:000039
  synonyms: Mn(IV) reduction
  evidence_summary: 'DOI:10.1128/mr.55.2.259-287.1991:  (Lovley establishes dissimilatory
    Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration on metal-oxide
    acceptors.) | PMID:7826009:  (Nealson & Saffarini review iron and manganese in
    anaerobic respiration as terminal electron acceptors.)'
  causal_graph_summary: 'dmr_mn_oxide_respiration: 3 nodes, 2 edges'
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
- **Trait label:** dissimilatory manganese reduction
- **METPO identifier:** traitmech:000108
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy by reducing Mn(IV) oxides to soluble Mn(II) as a terminal electron acceptor while oxidizing organic matter or hydrogen.
- **Parent traits:** traitmech:000039
- **Synonyms:** Mn(IV) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991:  (Lovley establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration on metal-oxide acceptors.) | PMID:7826009:  (Nealson & Saffarini review iron and manganese in anaerobic respiration as terminal electron acceptors.)
- **Existing causal graph summary:** dmr_mn_oxide_respiration: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory manganese reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_manganese_reduction.yaml`.

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
- **Trait label:** dissimilatory manganese reduction
- **METPO identifier:** traitmech:000108
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy by reducing Mn(IV) oxides to soluble Mn(II) as a terminal electron acceptor while oxidizing organic matter or hydrogen.
- **Parent traits:** traitmech:000039
- **Synonyms:** Mn(IV) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991:  (Lovley establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration on metal-oxide acceptors.) | PMID:7826009:  (Nealson & Saffarini review iron and manganese in anaerobic respiration as terminal electron acceptors.)
- **Existing causal graph summary:** dmr_mn_oxide_respiration: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory manganese reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_manganese_reduction.yaml`.

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


## Microbial trait causal-graph curation report: Dissimilatory manganese reduction (METPO:traitmech:000108)

### Scope summary (trait meaning, assays, boundaries)
Dissimilatory manganese reduction (DMR) is an **anaerobic, energy-conserving respiratory metabolism** in which microorganisms oxidize electron donors (e.g., organic matter or H2) while using **Mn(IV) oxides (e.g., MnO2) as terminal electron acceptors**, producing soluble **Mn(II)**. This coupling is framed as a major sediment/soil redox process that contributes to oxidation of organic matter to CO2 and affects contaminant transformations and metal/nutrient mobilization. (lovley1991dissimilatoryfe(iii)and pages 1-2)

**Boundary cases important for curation** include abiotic Mn(IV) reduction pathways that can generate Mn(II) without microbial energy conservation. Lovley summarizes several such reactions, including **Fe(II)-driven**, **sulfide-driven**, **nitrite-driven**, and **H2O2-driven** reduction of MnO2; these can confound phenotype attribution if experiments only measure Mn(II) accumulation. (lovley1991dissimilatoryfe(iii)and pages 8-10)

**Near-traits to distinguish**:
- **Dissimilatory Fe(III) reduction** is often mechanistically similar (shared extracellular electron transfer strategies) but is a separate trait with different terminal acceptor chemistry (Fe(III) vs Mn(IV)). (lovley1991dissimilatoryfe(iii)and pages 1-2, shi2012molecularunderpinningsof pages 1-2)
- **Mn(II) oxidation** is the reverse redox direction and should not be conflated with Mn(IV) reduction (not a part of this trait).
- **Metal-dependent anaerobic oxidation of methane (Fe/Mn-AOM)** can couple CH4 oxidation to Fe/Mn reduction at the community scale; this can be treated as an extension/linked trait module rather than the canonical “heterotrophic/H2-driven DMR.” (sivan2024enigmaticfemnfueledanaerobic pages 1-4, sivan2024enigmaticfemnfueledanaerobic pages 8-12)

Operationalization in experiments typically involves: (i) incubations with Mn(IV) oxide minerals as the sole terminal acceptor and monitoring Mn(II) production; and/or (ii) electrochemical analogs (electrodes as extracellular acceptors) used to dissect extracellular electron transfer (EET) machinery, which is also relevant to reduction of insoluble Mn(IV) oxides. (shi2012molecularunderpinningsof pages 1-2, shi2012molecularunderpinningsof media 6eae1135)

---

### Key concepts & current mechanistic understanding

#### 1) Extracellular electron transfer (EET) as the core constraint for Mn(IV) oxide respiration
Because Mn(IV) oxides are often insoluble under circumneutral pH conditions, organisms must transfer electrons **outside** the cell envelope, making EET components central causal-graph entities. In *Shewanella oneidensis* MR-1, the **Mtr pathway** is the best-characterized conduit for electron transfer from the inner membrane quinone pool to extracellular mineral acceptors. Shi et al. describe the canonical components **CymA → MtrA/MtrB → MtrC/OmcA**, where MtrC and OmcA act as terminal reductases at the cell surface, and additionally state that the Mtr pathway is “also involved in reduction of manganese oxides.” (shi2012molecularunderpinningsof pages 1-2)

A figure-level schematic of this pathway (Figure 3 in Shi et al.) visually depicts electron flow from inner-membrane processes to outer-surface cytochromes and the use of secreted flavins as shuttles/cofactors in mineral reduction. (shi2012molecularunderpinningsof media 6eae1135)

#### 2) Mediated EET via secreted flavins
Shi et al. report that MtrC and OmcA can use **secreted flavins** as diffusible cofactors to increase reduction rates of Fe(III) oxides (and by implication, potentially other external acceptors handled by the same EET machinery). (shi2012molecularunderpinningsof pages 1-2)

Recent electrochemical work in a different system (gut biofilm isolates) provides additional 2024-era support that **flavin addition can increase current production**, consistent with flavin-mediated EET being a generalizable mechanistic motif. (naradasu2024electrochemicalcharacterizationof pages 8-9)

#### 3) Geobacter-style direct EET and cytochrome specialization
For *Geobacter sulfurreducens*, Ueki summarizes a multi-component direct-EET architecture involving outer-membrane cytochrome complexes (e.g., **OmaB/OmbB/OmcB**), periplasmic electron carriers (**PpcA**), and extracellular/surface cytochromes (e.g., **OmcS, OmcE**) often associated with electrically conductive structures (**e-pili/PilA**). (ueki2021cytochromesinextracellular pages 8-10)

Importantly for Mn(IV) specificity:
- **OmcE deletion affects Mn(IV) oxide reduction** (lag phenotype), supporting OmcE as a mechanistic node that modulates DMR capacity in *Geobacter*. (ueki2021cytochromesinextracellular pages 8-10)
- **OmcT transcript is highly upregulated** during growth on Fe(III) or Mn(IV) oxide, but OmcT protein is reported as **not essential** for Mn(IV) oxide reduction—useful as a negative constraint in curation. (ueki2021cytochromesinextracellular pages 8-10)

---

### Recent developments and latest research (2023–2024 prioritized)

#### A) Metal-driven AOM: Fe/Mn-AOM as a linked module with quantitative geochemical signatures
A 2024 preprint reports geochemical evidence consistent with Fe/Mn-fueled AOM in sulfidic coastal sediments and provides quantitative ranges for porewater redox products and isotopic signals.
- Porewater **Fe2+** ranges reported include **10.75–361.3 µM** (zone-i) and **14.9–387.5 µM** (zone-ii).
- Porewater **Mn2+** ranges reported include **0.28–7.39 µM** (zone-i) and **0.41–10.17 µM** (zone-ii).
- A sulfate–methane transition zone (SMTZ) is described with **CH4 188.9–503.2 µM** and very negative **δ13CCH4 (−105.6 to −98.6 ‰)**; below SMTZ, CH4 reaches **1.04–4.19 mM** with additional δ13C signals.
- Strong negative correlations between DIC and δ13CDIC are reported (e.g., **R² = 0.82 overall; R² = 0.96 for Fe-Mn-AOM-specific points**), used as evidence for AOM coupled to metal reduction. (sivan2024enigmaticfemnfueledanaerobic pages 8-12)

These quantitative geochemical features can justify nodes/edges linking CH4 oxidation, DIC production, Fe/Mn reduction, and environmental zonation (SMTZ), but they are **community-level** and may not map cleanly to single-gene causal edges. (sivan2024enigmaticfemnfueledanaerobic pages 1-4, sivan2024enigmaticfemnfueledanaerobic pages 8-12)

#### B) Multiheme cytochromes in Methanoperedenaceae EET (2023): quantitative transcriptomics and community contribution
A 2023 study on ‘**Candidatus Methanoperedens nitroreducens**’ reports strong evidence for cytochrome-mediated EET to external acceptors and includes quantitative molecular indicators:
- The organism encodes **38 putative multiheme c-type cytochromes (MHCs)**.
- Shifting from nitrate to soluble iron upregulated extracellular MHCs, with a **16-heme MHC** and an **8-heme MHC** showing **38.2-fold** and **7.6-fold** increases, respectively.
- In an electrode-dependent AOM biofilm context, the authors report that **‘Ca. M. nitroreducens’ and Geobacter were transcriptionally dominant** with **9.6% and 23.6% of mRNA reads**, respectively. (zhang2023multihemecytochromemediatedextracellular pages 6-7, zhang2023multihemecytochromemediatedextracellulara pages 5-6)

Mn(IV) oxides are referenced as known acceptors for AOM, but the specific quantitative expression data in the provided excerpts are strongest for iron/electrodes; Mn-specific mechanistic edges should be marked as **inferred** unless Mn oxide incubations are directly evidenced in the same primary study section. (zhang2023multihemecytochromemediatedextracellulara pages 1-2, zhang2023multihemecytochromemediatedextracellulara pages 6-7)

#### C) 2024 electrochemical measurements consistent with mediator-enhanced EET
A 2024 study reports a measurable current density in a two-strain gut biofilm system and mediator sensitivity:
- Mixed culture current density: ~**35 nA/cm²** (about half of OTU0002 alone).
- EET conditions: ITO electrode, poised at **+0.4 V vs SHE**, 10 mM glucose.
- **Flavin addition increased current production**, supporting a flavin-mediated EET mechanism. (naradasu2024electrochemicalcharacterizationof pages 8-9)

Although not a Mn(IV)-oxide respiration assay, this supports inclusion of “flavin-mediated electron transfer” as a general mechanistic entity. (naradasu2024electrochemicalcharacterizationof pages 8-9)

---

### Current applications and real-world implementations

1. **Environmental biogeochemistry and contaminant transformations**: Foundational literature emphasizes that Mn(IV) reduction coupled to organic matter oxidation is a major driver of sediment/soil redox cycling and can influence release/mobilization of metals and nutrients, as well as contaminant oxidation/reduction dynamics. (lovley1991dissimilatoryfe(iii)and pages 1-2)

2. **Bioelectrochemical systems (BES) and microbial electrosynthesis**: EET machinery used for extracellular mineral respiration can be repurposed for electron exchange with electrodes. A 2024 *Applied and Environmental Microbiology* paper highlights bidirectional operation of *S. oneidensis* electron transport enabling microbial electrosynthesis and explicitly references the outer-membrane MtrCAB pathway in this context. (ford2024theelectrontransport pages 12-14)

3. **Linkage to methane mitigation in sediments**: 2024 geochemical evidence suggests Fe/Mn-AOM can operate even in sulfidic sediments and across the SMTZ, potentially impacting methane fluxes; this motivates inclusion of a “metal-dependent AOM” connected module in trait graphs for environments where Mn(IV) reduction couples to CH4 oxidation. (sivan2024enigmaticfemnfueledanaerobic pages 1-4, sivan2024enigmaticfemnfueledanaerobic pages 8-12)

---

### Expert interpretation and curation guidance

**What is sufficiently grounded for a TraitMech graph now**:
- Core DMR chemistry and environmental scope (donors → Mn(IV) reduction → Mn(II)) are well supported in foundational synthesis. (lovley1991dissimilatoryfe(iii)and pages 1-2)
- Key EET modules that plausibly govern Mn(IV) oxide reduction are strongly supported in model systems:
  - *Shewanella* Mtr conduit (CymA/MtrA/MtrB/MtrC/OmcA) and the statement that it is involved in reduction of manganese oxides. (shi2012molecularunderpinningsof pages 1-2, shi2012molecularunderpinningsof media 6eae1135)
  - *Geobacter* cytochrome components affecting Mn(IV) reduction phenotype (OmcE) and regulatory/expression signals (omcT upregulation but non-essential). (ueki2021cytochromesinextracellular pages 8-10)

**Where curation should be conservative (mark uncertain)**:
- Treat **flavin-mediated acceleration** as strong for Fe(III) oxide reduction; using it as a Mn(IV)-specific edge is biologically plausible but **inferred** unless Mn oxide-specific experiments are cited. (shi2012molecularunderpinningsof pages 1-2)
- Fe/Mn-AOM edges are strong at the geochemical association level, but mapping to a DMR trait graph requires careful scoping: it may represent a **linked process module** rather than the canonical DMR trait in heterotrophic bacteria. (sivan2024enigmaticfemnfueledanaerobic pages 8-12)

---

## Candidate node inventory (grouped, with grounding)
| Group | Candidate node label | Node type | Suggested grounding | Notes for curation | Key support |
|---|---|---|---|---|---|
| Phenotype/trait | dissimilatory manganese reduction | trait | METPO:traitmech:000108 | Anaerobic energy-conserving respiration using Mn(IV) oxides as terminal electron acceptors, yielding Mn(II) | (lovley1991dissimilatoryfe(iii)and pages 1-2, lovley1991dissimilatoryfe(iii)and pages 8-10) |
| Phenotype/trait | Mn(IV) oxide respiration | biological process |  | Near-synonym of trait; useful label node if process/trait separation is needed | (lovley1991dissimilatoryfe(iii)and pages 1-2) |
| Electron acceptor | manganese dioxide | chemical | CHEBI:16653 | Canonical Mn(IV) oxide acceptor; solid-phase external acceptor | (lovley1991dissimilatoryfe(iii)and pages 8-10) |
| Electron acceptor | Mn(IV) oxide | chemical class |  | Broad mineral acceptor class; preferable parent node when mineral identity is unspecified | (lovley1991dissimilatoryfe(iii)and pages 1-2, lovley1991dissimilatoryfe(iii)and pages 8-10) |
| Electron acceptor | Mn(II) | chemical | CHEBI:29035 | Reduced soluble product of DMR | (lovley1991dissimilatoryfe(iii)and pages 1-2, lovley1991dissimilatoryfe(iii)and pages 8-10) |
| Electron acceptor | Mn(III)/Mn(IV) (oxyhydr)oxides | chemical class |  | Boundary-expansion node for recent environmental literature where mixed-valence phases are discussed | (sivan2024enigmaticfemnfueledanaerobic pages 1-4) |
| Electron acceptor | ferric iron / Fe(III) oxide | chemical | CHEBI:18248 | Nearby trait comparator; often shares EET machinery with Mn reduction but is distinct from target trait | (lovley1991dissimilatoryfe(iii)and pages 1-2, shi2012molecularunderpinningsof pages 1-2) |
| Electron donor | hydrogen | chemical | CHEBI:18276 | Foundational donor for metal reduction | (lovley1991dissimilatoryfe(iii)and pages 1-2) |
| Electron donor | organic matter | material |  | Broad donor pool in sediments/soils | (lovley1991dissimilatoryfe(iii)and pages 1-2) |
| Electron donor | fatty acids | chemical class |  | Donor class completely oxidized by some metal reducers | (lovley1991dissimilatoryfe(iii)and pages 1-2) |
| Electron donor | monoaromatic compounds | chemical class |  | Donor class cited in foundational review | (lovley1991dissimilatoryfe(iii)and pages 1-2) |
| Electron donor | methane | chemical | CHEBI:16183 | Relevant in Fe/Mn-AOM boundary case and coupled metabolism | (sivan2024enigmaticfemnfueledanaerobic pages 1-4, zhang2023multihemecytochromemediatedextracellular pages 1-2) |
| Pathway/process | anaerobic respiration | biological process | GO:0009061 | Parent respiratory process for DMR | (lovley1991dissimilatoryfe(iii)and pages 1-2) |
| Pathway/process | extracellular electron transfer | biological process | GO:0097009 | Core mechanistic process for reduction of external Mn oxides | (shi2012molecularunderpinningsof pages 1-2, ueki2021cytochromesinextracellular pages 8-10) |
| Pathway/process | quinol oxidation | molecular function/process |  | Inner-membrane entry point into Shewanella Mtr chain via CymA | (shi2012molecularunderpinningsof pages 1-2, shi2012molecularunderpinningsof pages 2-3) |
| Pathway/process | terminal reduction of external metal oxides | biological process |  | Useful mechanistic node for outer-surface cytochrome action | (shi2012molecularunderpinningsof pages 1-2, ueki2021cytochromesinextracellular pages 8-10) |
| Pathway/process | anaerobic oxidation of methane coupled to metal reduction | biological process |  | Boundary/extension node connecting Mn reduction to CH4 oxidation in some systems | (sivan2024enigmaticfemnfueledanaerobic pages 1-4, zhang2023multihemecytochromemediatedextracellular pages 1-2) |
| Shewanella gene/protein | CymA | protein |  | Inner-membrane tetraheme cytochrome; quinol dehydrogenase feeding Mtr pathway | (shi2012molecularunderpinningsof pages 1-2, shi2012molecularunderpinningsof pages 2-3) |
| Shewanella gene/protein | MtrA | protein |  | Periplasm-spanning/decaheme cytochrome embedded with MtrB | (shi2012molecularunderpinningsof pages 1-2, shi2012molecularunderpinningsof pages 2-3) |
| Shewanella gene/protein | MtrB | protein |  | Outer-membrane porin-like scaffold for MtrA/MtrC conduit | (shi2012molecularunderpinningsof pages 1-2, shi2012molecularunderpinningsof pages 2-3) |
| Shewanella gene/protein | MtrC | protein |  | Outer-surface decaheme terminal reductase for external metals | (shi2012molecularunderpinningsof pages 1-2, shi2012molecularunderpinningsof pages 2-3) |
| Shewanella gene/protein | OmcA | protein |  | Outer-surface decaheme terminal reductase partnering with MtrC | (shi2012molecularunderpinningsof pages 1-2) |
| Shewanella gene/protein | MtrAB | complex |  | Subcomplex delivering electrons across outer membrane | (shi2012molecularunderpinningsof pages 1-2, shi2012molecularunderpinningsof pages 2-3) |
| Shewanella gene/protein | MtrABC | complex/pathway module |  | Best-supported Shewanella metal-reduction conduit; implicated in manganese oxide reduction | (shi2012molecularunderpinningsof pages 1-2, ford2024theelectrontransport pages 12-14) |
| Shewanella gene/protein | UndA | protein |  | Alternative extracellular cytochrome replacing OmcA in some Shewanella | (shi2012molecularunderpinningsof pages 1-2) |
| Shewanella gene/protein | UndA1 | protein |  | Homolog noted in comparative analysis of metal-reducing strains | (shi2012molecularunderpinningsof pages 2-3) |
| Shewanella taxon | Shewanella oneidensis MR-1 | organism | NCBITaxon:211586 | Model Mn/Fe-reducing bacterium for mechanistic curation | (shi2012molecularunderpinningsof pages 1-2, ford2024theelectrontransport pages 12-14) |
| Geobacter gene/protein | OmaB/OmbB/OmcB complex | complex |  | Major outer-membrane/periplasmic conduit to extracellular acceptors | (ueki2021cytochromesinextracellular pages 8-10, ueki2021cytochromesinextracellular pages 10-12) |
| Geobacter gene/protein | PpcA | protein |  | Predominant periplasmic electron carrier bridging inner and outer pathways | (ueki2021cytochromesinextracellular pages 8-10, alves2024potentialofelectrogenic pages 27-31) |
| Geobacter gene/protein | OmcS | protein |  | Outer-surface cytochrome associated with e-pili; terminal reductase for insoluble oxides | (ueki2021cytochromesinextracellular pages 8-10, ueki2021cytochromesinextracellular pages 10-12) |
| Geobacter gene/protein | OmcT | protein |  | OmcS homolog; transcript upregulated during growth on Fe(III)/Mn(IV) oxide, but not essential for Mn reduction | (ueki2021cytochromesinextracellular pages 8-10) |
| Geobacter gene/protein | OmcE | protein |  | Deletion causes lag/lower rates for metal oxide reduction and affects Mn(IV) reduction | (ueki2021cytochromesinextracellular pages 8-10) |
| Geobacter gene/protein | PilA | protein |  | Structural pilin for e-pili | (ueki2021cytochromesinextracellular pages 8-10) |
| Geobacter gene/protein | electrically conductive pili (e-pili) | cellular structure |  | Extracellular conductive appendages associated with direct EET | (ueki2021cytochromesinextracellular pages 8-10, alves2024potentialofelectrogenic pages 57-60) |
| Geobacter gene/protein | PgcA | protein |  | Extracellular c-type cytochrome/electron shuttle that can increase oxide reduction rates | (ueki2021cytochromesinextracellular pages 8-10, ueki2021cytochromesinextracellular pages 10-12) |
| Geobacter taxon | Geobacter sulfurreducens | organism | NCBITaxon:35554 | Model direct-EET metal reducer with Mn-associated cytochromes | (ueki2021cytochromesinextracellular pages 8-10) |
| Mediator | flavins | chemical class | CHEBI:30527 | Secreted diffusible cofactors/mediators enhancing Shewanella oxide reduction | (shi2012molecularunderpinningsof pages 1-2) |
| Mediator | riboflavin | chemical | CHEBI:17015 | Specific flavin commonly implicated in mediated EET | (marco2022ericstevensand pages 84-88) |
| Environmental/expt factor | anoxia | environmental condition | ENVO:01001019 | Required respiratory context for trait | (lovley1991dissimilatoryfe(iii)and pages 1-2) |
| Environmental/expt factor | circumneutral pH | environmental condition |  | Common condition where Mn/Fe oxides are insoluble and external to cell | (shi2012molecularunderpinningsof pages 1-2, lovley1991dissimilatoryfe(iii)and pages 8-10) |
| Environmental/expt factor | Fe(II) | chemical | CHEBI:29033 | Abiotic reductant of Mn(IV); confounder/boundary case | (lovley1991dissimilatoryfe(iii)and pages 8-10) |
| Environmental/expt factor | sulfide | chemical | CHEBI:16199 | Abiotic reductant of Mn(IV); can confound assignment to microbial DMR | (lovley1991dissimilatoryfe(iii)and pages 8-10) |
| Environmental/expt factor | nitrite | chemical | CHEBI:16301 | Abiotic reductant/denitrification intermediate; confounder | (lovley1991dissimilatoryfe(iii)and pages 8-10, hou2024biologicalandchemical pages 1-2) |
| Environmental/expt factor | hydrogen peroxide | chemical | CHEBI:16240 | Abiotic MnO2 reductant; boundary-case inhibitor/confounder node | (lovley1991dissimilatoryfe(iii)and pages 8-10) |
| Environmental/expt factor | bioelectrochemical system | experimental system |  | Practical EET assay/application context; useful for mechanistic evidence but not trait-defining | (ford2024theelectrontransport pages 12-14, naradasu2024electrochemicalcharacterizationof pages 8-9) |
| Environmental/expt factor | electrode | material |  | External solid electron acceptor analog used in EET studies | (ford2024theelectrontransport pages 12-14, zhang2023multihemecytochromemediatedextracellulara pages 5-6) |
| AOM coupling entity | dissolved inorganic carbon | metabolite | CHEBI:29985 | Product/indicator measured in Fe/Mn-AOM studies | (sivan2024enigmaticfemnfueledanaerobic pages 1-4, sivan2024enigmaticfemnfueledanaerobic pages 8-12) |
| AOM coupling entity | Methanoperedens nitroreducens | organism |  | Archaeal methanotroph linked to metal-dependent AOM via extracellular MHCs | (zhang2023multihemecytochromemediatedextracellular pages 1-2, zhang2023multihemecytochromemediatedextracellular pages 6-7) |
| AOM coupling entity | ANME archaea | organism group |  | Broader AOM-performing archaeal group implicated in Fe/Mn reduction | (sivan2024enigmaticfemnfueledanaerobic pages 1-4) |
| AOM coupling entity | multiheme c-type cytochromes | protein family |  | Candidate archaeal/bacterial EET conduits to metal oxides/electrodes | (zhang2023multihemecytochromemediatedextracellular pages 1-2, zhang2023multihemecytochromemediatedextracellular pages 6-7) |
| AOM coupling entity | MK:cytochrome c oxidoreductase clusters | pathway module |  | Differentially expressed respiratory modules in Methanoperedens under different acceptors | (zhang2023multihemecytochromemediatedextracellular pages 6-7, zhang2023multihemecytochromemediatedextracellulara pages 6-7) |


*Table: This table lists candidate entities for a TraitMech causal graph of dissimilatory manganese reduction, grouped by trait, chemistry, pathways, proteins, taxa, mediators, environment, and AOM-coupled extensions. Suggested ontology CURIEs are included where reasonably confident, and each row cites supporting context for curation.*

---

## Evidence-backed candidate causal edges (triples)
| Subject | Predicate | Object | Evidence snippet / quote | Reference (year) | Curation notes |
|---|---|---|---|---|---|
| organic matter | is_oxidized_coupled_to | dissimilatory manganese reduction | “The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV)…” and organisms “can completely oxidize fatty acids, hydrogen, or a variety of monoaromatic compounds” with Mn(IV) as sole acceptor (lovley1991dissimilatoryfe(iii)and pages 1-2) | Lovley 1991. DOI: https://doi.org/10.1128/mr.55.2.259-287.1991 | Strong foundational trait-scope edge; broad, not gene-specific. |
| hydrogen | donates_electrons_to | dissimilatory manganese reduction | Organisms with Fe(III) or Mn(IV) as sole electron acceptor “can completely oxidize fatty acids, hydrogen…” (lovley1991dissimilatoryfe(iii)and pages 1-2) | Lovley 1991. DOI: https://doi.org/10.1128/mr.55.2.259-287.1991 | Strong foundational edge; general across DMR-capable taxa. |
| MnO2 / Mn(IV) oxide | is_reduced_to | Mn2+ | Lovley summarizes Mn(IV) reduction as producing soluble Mn(II); abiotic reactions explicitly show “MnO2 … -> Mn(II)” (lovley1991dissimilatoryfe(iii)and pages 8-10, lovley1991dissimilatoryfe(iii)and pages 1-2) | Lovley 1991. DOI: https://doi.org/10.1128/mr.55.2.259-287.1991 | Core chemistry/product edge; curate as trait-defining output. |
| anoxia | enables | dissimilatory manganese reduction | DMR is defined as an anaerobic respiratory metabolism; Lovley repeatedly frames Mn(IV) reduction in “aquatic sediments, soils, and groundwater” under anaerobic conditions (lovley1991dissimilatoryfe(iii)and pages 1-2) | Lovley 1991. DOI: https://doi.org/10.1128/mr.55.2.259-287.1991 | Strong scope edge; environment/process relation rather than molecular mechanism. |
| CymA | transfers_electrons_to | MtrA | “CymA oxidizes the quinol in the inner-membrane and transfers the released electrons to MtrA either directly or indirectly…” (shi2012molecularunderpinningsof pages 1-2) | Shi et al. 2012. DOI: https://doi.org/10.3389/fmicb.2012.00050 | Strong for Shewanella Mtr pathway; taxon-specific. |
| MtrAB | delivers_electrons_to | MtrC/OmcA | “MtrAB deliver the electrons through the outer-membrane to the MtrC and OmcA on the outmost bacterial surface” (shi2012molecularunderpinningsof pages 1-2) | Shi et al. 2012. DOI: https://doi.org/10.3389/fmicb.2012.00050 | Strong for Shewanella; taxon-specific conduit edge. |
| MtrC/OmcA | directly_reduce | external metal oxides | “Functioning as terminal reductases, MtrC and OmcA can bind the surface of Fe(III) oxides and transfer electrons directly…”; “Mtr pathway is also involved in reduction of manganese oxides” (shi2012molecularunderpinningsof pages 1-2) | Shi et al. 2012. DOI: https://doi.org/10.3389/fmicb.2012.00050 | Strong pathway-to-function edge; Mn specificity is pathway-level, not direct MtrC-only knockout for Mn in this source. Mark taxon-specific. |
| MtrABC pathway | enables | reduction of manganese oxides | “In addition to Fe(III) oxides, Mtr pathway is also involved in reduction of manganese oxides and other metals” (shi2012molecularunderpinningsof pages 1-2) | Shi et al. 2012. DOI: https://doi.org/10.3389/fmicb.2012.00050 | Best direct Shewanella-to-Mn edge available here; strong, taxon-specific. |
| MtrAB | forms_complex_with | MtrC | “MtrABC forms a 1:1:1 complex… Sedimentation equilibrium gives a high binding affinity (Kd < 0.1 μM) between MtrAB and MtrC” (shi2012molecularunderpinningsof pages 2-3) | Shi et al. 2012. DOI: https://doi.org/10.3389/fmicb.2012.00050 | Structural/mechanistic support for conduit assembly; taxon-specific. |
| flavins | increase_rate_of | extracellular metal oxide reduction | “To increase their reaction rates, MtrC and OmcA can use the flavins secreted by S. oneidensis MR-1 cells as diffusible co-factors for reduction of Fe(III) oxides” (shi2012molecularunderpinningsof pages 1-2) | Shi et al. 2012. DOI: https://doi.org/10.3389/fmicb.2012.00050 | Strong for mediated EET; Mn effect inferred from shared Mtr pathway, so mark inferred for DMR-specific curation. |
| flavin addition | increases | extracellular electron transfer current | “Flavin addition increased current production, leading the authors to propose a flavin-cofactor enzyme and flavin-bound cell-surface enzymes as possible EET mechanisms” (naradasu2024electrochemicalcharacterizationof pages 8-9) | Naradasu et al. 2024. DOI: https://doi.org/10.3390/microorganisms12020257 | Recent quantitative EET support; not DMR-specific, so use as supporting but indirect evidence. |
| OmcE | affects | Mn(IV) oxide reduction phenotype | “OmcE is abundant and its deletion causes a long lag and lower reduction rates for Fe(III) oxide and affects Mn(IV) oxide reduction with a lag” (ueki2021cytochromesinextracellular pages 8-10) | Ueki 2021. DOI: https://doi.org/10.1128/aem.03109-20 | Strong phenotype edge for Geobacter; taxon-specific. |
| omcT expression | is_upregulated_during_growth_on | Mn(IV) oxide | “OmcT is a homolog of OmcS… its transcript is highly upregulated during growth on Fe(III) or Mn(IV) oxide” (ueki2021cytochromesinextracellular pages 8-10) | Ueki 2021. DOI: https://doi.org/10.1128/aem.03109-20 | Expression edge only; taxon-specific. |
| OmcT | not_essential_for | Mn(IV) oxide reduction | “OmcT… transcript is highly upregulated… but OmcT protein is not essential for Mn(IV) oxide reduction” (ueki2021cytochromesinextracellular pages 8-10) | Ueki 2021. DOI: https://doi.org/10.1128/aem.03109-20 | Important negative/qualifying edge; taxon-specific. |
| OmaB/OmbB/OmcB complex | transfers_electrons_to | OmcS | “For insoluble Fe(III) oxide, electrons are transferred from that complex to OmcS associated with e-pili…” (ueki2021cytochromesinextracellular pages 8-10) | Ueki 2021. DOI: https://doi.org/10.1128/aem.03109-20 | Strong Geobacter EET edge; Mn application inferred via shared insoluble oxide respiration. |
| OmcS associated with e-pili | acts_as_terminal_reductase_for | insoluble metal oxides | “OmcS associated with e-pili… serve as terminal reductases” (ueki2021cytochromesinextracellular pages 8-10) | Ueki 2021. DOI: https://doi.org/10.1128/aem.03109-20 | Strong for insoluble oxide reduction; Mn-specific use inferred. Taxon-specific, inferred for DMR. |
| PgcA | increases_rate_of | Fe(III) oxide reduction | “Purified PgcA increases Fe(III) oxide reduction rates” (ueki2021cytochromesinextracellular pages 8-10) | Ueki 2021. DOI: https://doi.org/10.1128/aem.03109-20 | Strong shuttle/rate edge; DMR-specific extrapolation uncertain. |
| PgcA | compensates_for_loss_of | PilA/e-pili during oxide reduction | “Purified PgcA… compensates in PilA (e-pili) deletion mutants” (ueki2021cytochromesinextracellular pages 8-10) | Ueki 2021. DOI: https://doi.org/10.1128/aem.03109-20 | Useful alternative-path edge; taxon-specific and mainly Fe(III)-oxide assay evidence. |
| Fe2+ | abiotically_reduces | MnO2 | “2Mn(IV) + 2Fe(II) -> 2Mn(II) + 2Fe(III)” (lovley1991dissimilatoryfe(iii)and pages 8-10) | Lovley 1991. DOI: https://doi.org/10.1128/mr.55.2.259-287.1991 | Boundary-case edge; abiotic confounder, should not be curated as microbial mechanism. |
| sulfide | abiotically_reduces | MnO2 | Lovley describes “sulfide-driven reduction of MnO2” and gives reaction “3H+ + MnO2 + HS- -> Mn2+ + S0 + 2H2O” (lovley1991dissimilatoryfe(iii)and pages 8-10) | Lovley 1991. DOI: https://doi.org/10.1128/mr.55.2.259-287.1991 | Boundary-case edge; abiotic confounder. |
| nitrite | abiotically_reduces | MnO2 | “NO2- + MnO2 + 2H+ -> Mn2+ + NO3- + H2O” (lovley1991dissimilatoryfe(iii)and pages 8-10) | Lovley 1991. DOI: https://doi.org/10.1128/mr.55.2.259-287.1991 | Boundary-case edge; abiotic confounder. |
| hydrogen peroxide | abiotically_reduces | MnO2 | “H2O2 + MnO2 + 2H+ -> Mn(II) + 2H2O + O2” (lovley1991dissimilatoryfe(iii)and pages 8-10) | Lovley 1991. DOI: https://doi.org/10.1128/mr.55.2.259-287.1991 | Boundary-case edge; abiotic confounder. |
| methane oxidation | is_coupled_to | Fe/Mn reduction | “AOM coupled with Fe-Mn reduction (Fe-Mn-AOM) is considered a globally important biogeochemical process” and reactions are given for MnO2-coupled AOM (sivan2024enigmaticfemnfueledanaerobic pages 1-4) | Sivan et al. 2024. DOI: https://doi.org/10.5194/egusphere-2024-1829 | Strong environmental coupling edge; mechanism may vary by community. |
| Fe/Mn-AOM | is_associated_with | increased porewater Fe2+/Mn2+ | “concurrent decrease in CH4 concentrations… coupled with the enrichment of porewater Fe2+ and Mn2+ concentrations” and ranges reported for Fe2+/Mn2+ across zones (sivan2024enigmaticfemnfueledanaerobic pages 1-4, sivan2024enigmaticfemnfueledanaerobic pages 8-12) | Sivan et al. 2024. DOI: https://doi.org/10.5194/egusphere-2024-1829 | Strong geochemical association; community-level, not single-organism mechanism. |
| Fe/Mn-AOM | is_associated_with | isotopic shifts in δ13CCH4 and δ13CDIC | “concurrent decreases in CH4 concentrations and isotopic shifts (δ13CCH4, δ13CDIC) coupled with enrichment of porewater Fe2+ and Mn2+” (sivan2024enigmaticfemnfueledanaerobic pages 1-4, sivan2024enigmaticfemnfueledanaerobic pages 8-12) | Sivan et al. 2024. DOI: https://doi.org/10.5194/egusphere-2024-1829 | Strong environmental signature edge. |
| Methanoperedens extracellular multiheme cytochromes | are_upregulated_under | iron respiration | “Several extracellular MHCs are strongly upregulated during iron respiration… 16-heme MHC… and 8-heme MHC… fold-changes of 38.2 and 7.6” (zhang2023multihemecytochromemediatedextracellular pages 6-7, zhang2023multihemecytochromemediatedextracellulara pages 6-7) | Zhang et al. 2023. URL unavailable in context; cited via context. Year 2023 | Strong expression edge for archaeal metal-dependent EET; Mn relevance inferred, not directly shown in these pages. |
| Methanoperedens extracellular multiheme cytochromes | support | extracellular electron transfer to external acceptors | “The authors present experimental evidence that ‘Ca. Methanoperedens nitroreducens’ performs cytochrome-mediated EET for reduction of metals and electrodes” (zhang2023multihemecytochromemediatedextracellulara pages 1-2, zhang2023multihemecytochromemediatedextracellulara pages 5-6) | Zhang et al. 2023. URL unavailable in context; cited via context. Year 2023 | Strong EET mechanism edge; direct for iron/electrode, inferred for manganese. |
| Mtr pathway | enables | bidirectional extracellular electron transfer in Shewanella | Ford & TerAvest cite that “the cell can … via the outer membrane MtrCAB pathway” and describe the electron transport chain operating bidirectionally in BES (ford2024theelectrontransport pages 12-14) | Ford & TerAvest 2024. DOI: https://doi.org/10.1128/aem.01387-23 | Supports broader EET competence of Mtr system; indirect for DMR, but useful application/mechanistic context. |


*Table: This table compiles evidence-backed subject-predicate-object triples for curating a TraitMech causal graph of dissimilatory manganese reduction, including core respiratory chemistry, Shewanella and Geobacter extracellular electron-transfer components, abiotic confounders, and metal-dependent AOM extensions.*

---

### Quantitative/statistical highlights (recent)
- Fe/Mn-AOM porewater enrichment: Fe2+ up to ~**387.5 µM** and Mn2+ up to ~**10.17 µM**, with methane/isotopic signatures across sediment zones and **R² up to 0.96** for DIC–δ13CDIC relationships used to support Fe-Mn-AOM. (sivan2024enigmaticfemnfueledanaerobic pages 8-12)
- Methanoperedens EET gene expression: extracellular MHC upregulation under iron respiration (e.g., **38.2-fold** increase for a 16-heme MHC), and community transcript dominance (**9.6%** Methanoperedens; **23.6%** Geobacter mRNA reads) in an electrode-dependent AOM biofilm. (zhang2023multihemecytochromemediatedextracellular pages 6-7, zhang2023multihemecytochromemediatedextracellulara pages 5-6)
- 2024 EET current density in a biofilm system and mediator effect: mixed culture ~**35 nA/cm²**; flavin addition increased current. (naradasu2024electrochemicalcharacterizationof pages 8-9)

---

### Mechanistic figure (visual evidence)
A schematic of the *Shewanella* Mtr pathway (CymA → MtrA/MtrB → MtrC/OmcA) and flavin involvement in extracellular reduction of metal oxides is captured in Figure 3 from Shi et al. (shi2012molecularunderpinningsof media 6eae1135)

---

## DOI-first bibliography (with URLs and publication dates where available)

1. Lovley DR. **Dissimilatory Fe(III) and Mn(IV) reduction.** *Microbiological Reviews* (Jun 1991). DOI: **10.1128/mr.55.2.259-287.1991**. URL: https://doi.org/10.1128/mr.55.2.259-287.1991 (lovley1991dissimilatoryfe(iii)and pages 1-2, lovley1991dissimilatoryfe(iii)and pages 8-10)

2. Shi L, Rosso KM, Clarke TA, Richardson DJ, Zachara JM, Fredrickson JK. **Molecular Underpinnings of Fe(III) Oxide Reduction by Shewanella oneidensis MR-1.** *Frontiers in Microbiology* (Feb 2012). DOI: **10.3389/fmicb.2012.00050**. URL: https://doi.org/10.3389/fmicb.2012.00050 (shi2012molecularunderpinningsof pages 1-2, shi2012molecularunderpinningsof pages 2-3, shi2012molecularunderpinningsof media 6eae1135)

3. Ueki T. **Cytochromes in Extracellular Electron Transfer in Geobacter.** *Applied and Environmental Microbiology* (Apr 2021). DOI: **10.1128/aem.03109-20**. URL: https://doi.org/10.1128/aem.03109-20 (ueki2021cytochromesinextracellular pages 8-10)

4. Ford KC, TerAvest MA. **The electron transport chain of Shewanella oneidensis MR-1 can operate bidirectionally to enable microbial electrosynthesis.** *Applied and Environmental Microbiology* (Jan 2024). DOI: **10.1128/aem.01387-23**. URL: https://doi.org/10.1128/aem.01387-23 (ford2024theelectrontransport pages 12-14)

5. Naradasu D, Miran W, Okamoto A. **Electrochemical Characterization of Two Gut Microbial Strains Cooperatively Promoting Multiple Sclerosis Pathogenesis.** *Microorganisms* (Jan 2024). DOI: **10.3390/microorganisms12020257**. URL: https://doi.org/10.3390/microorganisms12020257 (naradasu2024electrochemicalcharacterizationof pages 8-9)

6. Sivan K, Peketi A, Mazumdar A, et al. **Enigmatic Fe-Mn-fueled Anaerobic Oxidation of Methane in sulfidic coastal sediments of the Eastern Arabian Sea.** *EGUsphere preprint* (Jul 2024). DOI: **10.5194/egusphere-2024-1829**. URL: https://doi.org/10.5194/egusphere-2024-1829 (sivan2024enigmaticfemnfueledanaerobic pages 1-4, sivan2024enigmaticfemnfueledanaerobic pages 8-12)

7. Zhang X, Joyce GH, Leu AO, Zhao J, Rabiee H. **Multi-heme cytochrome-mediated extracellular electron transfer by the anaerobic methanotroph ‘Candidatus Methanoperedens nitroreducens’.** (2023). URL/DOI not available in retrieved context. (zhang2023multihemecytochromemediatedextracellulara pages 1-2, zhang2023multihemecytochromemediatedextracellular pages 6-7, zhang2023multihemecytochromemediatedextracellulara pages 5-6)

8. Alves FMCJ. **Potential of Electrogenic Bacteria in the Development of Sustainable Technologies for Bioremediation and Bioenergy Production.** (2024; journal/DOI not available in retrieved context). (alves2024potentialofelectrogenic pages 57-60, alves2024potentialofelectrogenic pages 27-31)

---

## Warnings / “do not curate yet” items
- **Do not encode abiotic MnO2 reduction reactions as microbial causal edges** (Fe2+, sulfide, nitrite, H2O2), except as explicit “confounder/boundary” relationships, because they can mimic the Mn(II) phenotype without energy conservation. (lovley1991dissimilatoryfe(iii)and pages 8-10)
- **Avoid asserting flavins specifically accelerate Mn(IV) oxide reduction** unless a Mn-oxide experiment is directly cited; the strongest explicit statement here is for Fe(III) oxides, with Mn implication via shared Mtr machinery. Mark as inferred if included. (shi2012molecularunderpinningsof pages 1-2)
- **Metal-AOM modules** (Fe/Mn-AOM) have strong geochemical support but require additional organism-specific evidence to link directly to Mn(IV) oxide reduction genes/proteins in a trait graph; curate as a linked/conditional module tied to environment and community composition. (sivan2024enigmaticfemnfueledanaerobic pages 8-12)


References

1. (lovley1991dissimilatoryfe(iii)and pages 1-2): D R Lovley. Dissimilatory fe(iii) and mn(iv) reduction. Microbiological Reviews, 55:259-287, Jun 1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991, doi:10.1128/mr.55.2.259-287.1991. This article has 2590 citations.

2. (lovley1991dissimilatoryfe(iii)and pages 8-10): D R Lovley. Dissimilatory fe(iii) and mn(iv) reduction. Microbiological Reviews, 55:259-287, Jun 1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991, doi:10.1128/mr.55.2.259-287.1991. This article has 2590 citations.

3. (shi2012molecularunderpinningsof pages 1-2): Liang Shi, Kevin M. Rosso, Tomas A. Clarke, David J. Richardson, John M. Zachara, and James K. Fredrickson. Molecular underpinnings of fe(iii) oxide reduction by shewanella oneidensis mr-1. Frontiers in Microbiology, Feb 2012. URL: https://doi.org/10.3389/fmicb.2012.00050, doi:10.3389/fmicb.2012.00050. This article has 293 citations and is from a peer-reviewed journal.

4. (sivan2024enigmaticfemnfueledanaerobic pages 1-4): Kalyani Sivan, Aditya Peketi, Aninda Mazumdar, Anjali Zatale, Sai Pavan Kumar Pillutla, Ankita Ghosh, Mohd Sadique, and Jittu Mathai. Enigmatic fe-mn-fueled anaerobic oxidation of methane in sulfidic coastal sediments of the eastern arabian sea. Jul 2024. URL: https://doi.org/10.5194/egusphere-2024-1829, doi:10.5194/egusphere-2024-1829.

5. (sivan2024enigmaticfemnfueledanaerobic pages 8-12): Kalyani Sivan, Aditya Peketi, Aninda Mazumdar, Anjali Zatale, Sai Pavan Kumar Pillutla, Ankita Ghosh, Mohd Sadique, and Jittu Mathai. Enigmatic fe-mn-fueled anaerobic oxidation of methane in sulfidic coastal sediments of the eastern arabian sea. Jul 2024. URL: https://doi.org/10.5194/egusphere-2024-1829, doi:10.5194/egusphere-2024-1829.

6. (shi2012molecularunderpinningsof media 6eae1135): Liang Shi, Kevin M. Rosso, Tomas A. Clarke, David J. Richardson, John M. Zachara, and James K. Fredrickson. Molecular underpinnings of fe(iii) oxide reduction by shewanella oneidensis mr-1. Frontiers in Microbiology, Feb 2012. URL: https://doi.org/10.3389/fmicb.2012.00050, doi:10.3389/fmicb.2012.00050. This article has 293 citations and is from a peer-reviewed journal.

7. (naradasu2024electrochemicalcharacterizationof pages 8-9): Divya Naradasu, Waheed Miran, and Akihiro Okamoto. Electrochemical characterization of two gut microbial strains cooperatively promoting multiple sclerosis pathogenesis. Microorganisms, 12:257, Jan 2024. URL: https://doi.org/10.3390/microorganisms12020257, doi:10.3390/microorganisms12020257. This article has 3 citations.

8. (ueki2021cytochromesinextracellular pages 8-10): Toshiyuki Ueki. Cytochromes in extracellular electron transfer in <i>geobacter</i>. Apr 2021. URL: https://doi.org/10.1128/aem.03109-20, doi:10.1128/aem.03109-20. This article has 195 citations and is from a peer-reviewed journal.

9. (zhang2023multihemecytochromemediatedextracellular pages 6-7): X Zhang, GH Joyce, AO Leu, J Zhao, and H Rabiee. Multi-heme cytochrome-mediated extracellular electron transfer by the anaerobic methanotroph 'candidatus methanoperedens nitroreducens'. Unknown journal, 2023.

10. (zhang2023multihemecytochromemediatedextracellulara pages 5-6): X Zhang, GH Joyce, AO Leu, J Zhao, and H Rabiee. Multi-heme cytochrome-mediated extracellular electron transfer by the anaerobic methanotroph 'candidatus methanoperedens nitroreducens'. Unknown journal, 2023.

11. (zhang2023multihemecytochromemediatedextracellulara pages 1-2): X Zhang, GH Joyce, AO Leu, J Zhao, and H Rabiee. Multi-heme cytochrome-mediated extracellular electron transfer by the anaerobic methanotroph 'candidatus methanoperedens nitroreducens'. Unknown journal, 2023.

12. (zhang2023multihemecytochromemediatedextracellulara pages 6-7): X Zhang, GH Joyce, AO Leu, J Zhao, and H Rabiee. Multi-heme cytochrome-mediated extracellular electron transfer by the anaerobic methanotroph 'candidatus methanoperedens nitroreducens'. Unknown journal, 2023.

13. (ford2024theelectrontransport pages 12-14): Kathryne C. Ford and Michaela A. TerAvest. The electron transport chain of <i>shewanella oneidensis</i> mr-1 can operate bidirectionally to enable microbial electrosynthesis. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01387-23, doi:10.1128/aem.01387-23. This article has 34 citations and is from a peer-reviewed journal.

14. (zhang2023multihemecytochromemediatedextracellular pages 1-2): X Zhang, GH Joyce, AO Leu, J Zhao, and H Rabiee. Multi-heme cytochrome-mediated extracellular electron transfer by the anaerobic methanotroph 'candidatus methanoperedens nitroreducens'. Unknown journal, 2023.

15. (shi2012molecularunderpinningsof pages 2-3): Liang Shi, Kevin M. Rosso, Tomas A. Clarke, David J. Richardson, John M. Zachara, and James K. Fredrickson. Molecular underpinnings of fe(iii) oxide reduction by shewanella oneidensis mr-1. Frontiers in Microbiology, Feb 2012. URL: https://doi.org/10.3389/fmicb.2012.00050, doi:10.3389/fmicb.2012.00050. This article has 293 citations and is from a peer-reviewed journal.

16. (ueki2021cytochromesinextracellular pages 10-12): Toshiyuki Ueki. Cytochromes in extracellular electron transfer in <i>geobacter</i>. Apr 2021. URL: https://doi.org/10.1128/aem.03109-20, doi:10.1128/aem.03109-20. This article has 195 citations and is from a peer-reviewed journal.

17. (alves2024potentialofelectrogenic pages 27-31): FMCJ Alves. Potential of electrogenic bacteria in the development of sustainable technologies for bioremediation and bioenergy production. Unknown journal, 2024.

18. (alves2024potentialofelectrogenic pages 57-60): FMCJ Alves. Potential of electrogenic bacteria in the development of sustainable technologies for bioremediation and bioenergy production. Unknown journal, 2024.

19. (marco2022ericstevensand pages 84-88): M Marco. Eric stevens and maria marco department of food science & technology, university of california, davis, ca, usa. Unknown journal, 2022.

20. (hou2024biologicalandchemical pages 1-2): Lingyu Hou, Xiangyu Bai, Zihe Sima, Jiani Zhang, Luyao Yan, Ding Li, and Yongguang Jiang. Biological and chemical processes of nitrate reduction and ferrous oxidation mediated by shewanella oneidensis mr-1. Microorganisms, 12:2454, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122454, doi:10.3390/microorganisms12122454. This article has 6 citations.