---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:28:49.436306'
end_time: '2026-06-18T01:45:59.445087'
duration_seconds: 1030.01
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature delta high
  trait_identifier: METPO:1000487
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_delta_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature delta phenotype with a growth-supporting temperature\
    \ breadth above approximately 30 \xB0C, characteristic of extreme-eurythermal\
    \ physiology."
  parent_traits: METPO:1000303
  synonyms: Td_>30
  evidence_summary: 'DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty
    acids (Membrane-adaptation review supports very broad homoviscous remodeling capacity
    as the basis of extreme-eurythermal physiology.) | DOI:10.1128/MMBR.65.1.1-43.2001:
    resistant to irreversible inactivation at high temperatures (Thermostable-protein
    review supports robust thermostability as the basis of extending tolerance beyond
    standard mesophile ranges.)'
  causal_graph_summary: 'temperature_delta_high_eurythermal: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta high
- **METPO identifier:** METPO:1000487
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth above approximately 30 °C, characteristic of extreme-eurythermal physiology.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_>30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports very broad homoviscous remodeling capacity as the basis of extreme-eurythermal physiology.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports robust thermostability as the basis of extending tolerance beyond standard mesophile ranges.)
- **Existing causal graph summary:** temperature_delta_high_eurythermal: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_high.yaml`.

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
- **Trait label:** temperature delta high
- **METPO identifier:** METPO:1000487
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth above approximately 30 °C, characteristic of extreme-eurythermal physiology.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_>30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports very broad homoviscous remodeling capacity as the basis of extreme-eurythermal physiology.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports robust thermostability as the basis of extending tolerance beyond standard mesophile ranges.)
- **Existing causal graph summary:** temperature_delta_high_eurythermal: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_high.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **temperature delta high** (Td_>30; METPO:1000487)

### Scope summary (trait definition and boundaries)
**Target trait:** *temperature delta high* is a **growth-supporting temperature breadth** phenotype, defined in METPO as a temperature-delta phenotype with a growth-supporting temperature breadth **above ~30 °C**, characteristic of **extreme eurythermal physiology** (synonym: Td_>30). For TraitMech curation, this trait should be interpreted as the ability to **sustain growth across a wide temperature interval**, not merely survive transient heat shock or cold shock.

**How to distinguish from neighboring traits (boundary cases):**
- **Thermotolerance/heat-shock survival**: survival after acute exposure to high temperature (e.g., 45–55 °C exposure assays) can support mechanisms relevant to the upper-temperature arm, but does *not* alone establish a **growth breadth** trait (e.g., improved survival at 45 °C is not equivalent to growth over a >30 °C interval). (wang2023characterizationofhsp17 pages 7-10)
- **Thermophile/hyperthermophile**: these are *high optimum temperature* categories rather than breadth per se. Hyperthermophiles are described as organisms that “grow optimally at temperatures between **80 and 110 °C**” and have enzymes active above **70 °C**. (vieille2001hyperthermophilicenzymessources pages 2-3)
- **Psychrophile/psychrotolerant**: these define adaptation to low temperature, again not necessarily breadth. Quantitative anchors: mesophiles ~**20–45 °C**, psychrophiles prefer ~**15 °C or below**, psychrotolerant bacteria may grow optimally at **20–25 °C** but survive below **0 °C**. (wu2023molecularmechanismsof pages 2-3)

**Operationalization recommendation for curation** (assay/metadata): curate Td_>30 when a strain/species has documented **minimum growth temperature (Tmin)** and **maximum growth temperature (Tmax)** with **Tmax − Tmin > 30 °C** (growth, not survival). In absence of explicit Tmin/Tmax in evidence, curate mechanistic edges as **supporting mechanisms** for the phenotype, flagged as **inferred** until breadth measurements are available.

---

### Current understanding: key mechanistic concepts (expert synthesis backed by sources)
#### 1) Membrane-centric temperature sensing and lipid remodeling (homoviscous/homeoviscous adaptation)
A central mechanistic concept enabling broad thermal growth is **maintenance of membrane physical state** (fluidity/phase) across temperatures. A canonical mechanism is **homoviscous adaptation**, where bacteria remodel membrane lipid composition to maintain fluid bilayers as temperature decreases by increasing unsaturated (or functionally analogous) fatty acids. (mendoza2014temperaturesensingby pages 1-2)

Mechanistic detail: temperature changes alter membrane order/viscosity; cells sense this through membrane-associated sensory systems and induce lipid remodeling (e.g., desaturases). (wu2023molecularmechanismsof pages 3-5, mendoza2014temperaturesensingby pages 1-2)

Key authoritative framing (review): bacteria “remodel the fluidity of their membrane bilayer… as growth temperature decreases,” and microbes sense fluidity changes and “upregulate the biosynthesis of unsaturated fatty acids.” (mendoza2014temperaturesensingby pages 1-2)

A key *curatable* signaling example is the **DesK/DesR two-component system** (Bacillus exemplar), which senses bilayer physical properties and induces desaturation to restore membrane fluidity. (wu2023molecularmechanismsof pages 3-5, mendoza2014temperaturesensingby media 26a67188, mendoza2014temperaturesensingby media 83d7475c)

#### 2) Protein stability and proteostasis (heat-shock proteins / chaperones)
Broad thermal growth requires preventing loss of protein function at extremes (misfolding, aggregation, irreversible inactivation). A 2023 bacterial primary study demonstrates a direct genetic determinant: overexpression of a **small heat shock protein (sHSP) Hsp17** increases survival at high temperature, while deletion decreases heat resistance. (wang2023characterizationofhsp17 pages 7-10)

These data support inclusion of **proteostasis/chaperone systems** as nodes mediating the high-temperature arm of thermal breadth.

#### 3) Thermostable enzymes as an upper-temperature enabling mechanism
A foundational, highly cited review states that enzymes from hyperthermophiles are “typically thermostable (i.e., resistant to irreversible inactivation at high temperatures)” and remain optimally active at high temperatures. (vieille2001hyperthermophilicenzymessources pages 2-3)

While hyperthermophily is not identical to Td_>30 breadth, the concept of **intrinsic thermostability resisting irreversible inactivation** is directly reusable as a mechanistic node for upper-temperature growth limits and may contribute to broad breadth when combined with low-temperature adaptations.

#### 4) Nucleic-acid/cold-shock factors in low-temperature growth
Low temperature impacts nucleic-acid secondary structure and translation/transcription efficiency; cold-shock nucleic-acid binding factors are commonly induced. In a 2024 transcriptomic study, a “cold-shock DNA-binding domain” gene is upregulated **5.77-fold** under low temperature. (jing2024transcriptomeresponseof pages 7-8)

#### 5) Ecological and evolutionary framing for broad thermal niches
In hot-spring microbiomes spanning **54.8–80 °C**, thermal niche breadth was operationalized as “T-resistant” taxa occurring across ≥5 temperatures vs T-sensitive taxa restricted to a specific temperature; broad-niche taxa show a “jack-of-all-trades, master-of-none” tradeoff (niche expansion with poorer local performance and higher extinction). (he2023highspeciationrate pages 1-2)

This supports curating **tradeoff/cost** nodes/edges (optional) for Td_>30: wide breadth may involve compromises in maximal growth rate or local fitness.

---

### Candidate causal-graph nodes (grouped by type; with suggested grounding)
#### A) Environmental & experimental factors
- **Temperature shift / growth temperature decrease** (label node) (mendoza2014temperaturesensingby pages 1-2)
- **Low temperature exposure** (label node) (jing2024transcriptomeresponseof pages 7-8)
- **High temperature stress / heat exposure** (label node) (wang2023characterizationofhsp17 pages 7-10)
- **Hot spring thermal gradient** (ENVO:00000599 hot spring; label node: temperature gradient) (he2023highspeciationrate pages 1-2)

#### B) Cellular/biophysical state nodes
- **Membrane fluidity** (label node) (mendoza2014temperaturesensingby pages 1-2)
- **Reduced membrane fluidity / membrane rigidification** (label node) (mendoza2014temperaturesensingby pages 1-2)
- **Membrane viscosity / phase behavior (Tm concept)** (label node) (mendoza2014temperaturesensingby pages 1-2)

#### C) Molecular/pathway nodes: lipids & remodeling
- **Unsaturated fatty acids** (CHEBI:3558) (mendoza2014temperaturesensingby pages 1-2)
- **Fatty-acid desaturation / lipid desaturase activity** (GO:0006636 fatty acid metabolic process; specific desaturase GO terms may vary) (wu2023molecularmechanismsof pages 2-3)
- **Short-chain fatty acids (SCFA)** (CHEBI:26666) (wu2023molecularmechanismsof pages 3-5)
- **Branched-chain fatty acids (BCFA)** (CHEBI:35756) (wu2023molecularmechanismsof pages 3-5)
- **Lysophospholipids (LPLs)** (CHEBI:32957) (wu2023molecularmechanismsof pages 3-5)
- **cis–trans isomerase (Cti)** (label node; protein) (wu2023molecularmechanismsof pages 2-3)

#### D) Signaling/regulatory modules
- **Two-component system DesK/DesR** (label nodes; Bacillus exemplar) (wu2023molecularmechanismsof pages 3-5)

#### E) Proteostasis and heat-shock modules
- **Small heat shock protein Hsp17 (hsp17 gene)** (label node) (wang2023characterizationofhsp17 pages 7-10)
- **Protein folding / chaperone function** (GO:0006457 protein folding) (wang2023characterizationofhsp17 pages 7-10)

#### F) Nucleic-acid/cold response
- **Cold-shock DNA-binding domain protein** (label node; GO:0003676 nucleic acid binding as coarse grounding) (jing2024transcriptomeresponseof pages 7-8)

#### G) Enzyme stability / high-temperature performance
- **Thermostable enzyme** (label node) (vieille2001hyperthermophilicenzymessources pages 2-3)
- **Irreversible protein inactivation (avoidance)** (label node) (vieille2001hyperthermophilicenzymessources pages 2-3)

---

### Candidate causal edges (evidence-backed triples)
The following table is formatted for direct TraitMech-style edge consideration.

| Edge (triple) | Mechanistic interpretation | Evidence snippet (verbatim) | Source (authors, year, title) | DOI | URL | Notes/uncertainty | Suggested ontology grounding (GO/CHEBI/ENVO/UniProt/etc if possible) |
|---|---|---|---|---|---|---|---|
| decreased growth temperature → increases → unsaturated fatty acid biosynthesis | Core homoviscous adaptation mechanism expanding low-temperature growth capacity and thus broadening temperature breadth | “Bacteria remodel the fluidity of their membrane bilayer precisely via the incorporation of proportionally more unsaturated fatty acids (or fatty acids with analogous properties) as growth temperature decreases.” (mendoza2014temperaturesensingby pages 1-2) | de Mendoza, 2014, *Temperature sensing by membranes* | 10.1146/annurev-micro-091313-103612 | https://doi.org/10.1146/annurev-micro-091313-103612 | Strong general mechanism; supports low-temperature arm of eurythermality rather than full Td_>30 by itself | GO:0006636 fatty acid biosynthetic process; CHEBI:3558 unsaturated fatty acid; label node: membrane fluidity |
| homoviscous adaptation → maintains → membrane fluidity/permeability homeostasis | Membrane physical homeostasis is a proximal mechanism for sustaining growth across thermal shifts | “This process, termed homoviscous adaptation, is suited to disrupt the order of the lipid bilayer and optimizes the performance of a large array of cellular physiological processes at the new temperature.” (mendoza2014temperaturesensingby pages 1-2) | de Mendoza, 2014, *Temperature sensing by membranes* | 10.1146/annurev-micro-091313-103612 | https://doi.org/10.1146/annurev-micro-091313-103612 | Strong review evidence; process-level edge | GO:0008150 biological process; label node: homoviscous adaptation; GO:0016042 lipid catabolic process not exact—keep label-level if needed |
| decreased membrane fluidity → upregulates → unsaturated fatty acid biosynthesis | Temperature sensing is mediated by membrane physical state, not temperature alone | “microbes have developed molecular strategies to sense changes in membrane fluidity, provoked by a decrease in environmental temperature, and initiate cellular responses that upregulate the biosynthesis of unsaturated fatty acids.” (mendoza2014temperaturesensingby pages 1-2) | de Mendoza, 2014, *Temperature sensing by membranes* | 10.1146/annurev-micro-091313-103612 | https://doi.org/10.1146/annurev-micro-091313-103612 | Strong but system-level; subject may be represented as “reduced membrane fluidity” | label node: reduced membrane fluidity; GO:0006636 fatty acid biosynthetic process; CHEBI:3558 |
| lipid desaturase activity → increases → membrane fluidity | Desaturation creates packing defects that preserve bilayer function at low temperature | “organisms maintain membrane fluidity/thickness by activating lipid desaturases that introduce cis double bonds into fatty acids to increase packing defects (a ~30° kink) and therefore fluidity.” (wu2023molecularmechanismsof pages 2-3) | Wu, Baumeister, Heimbucher, 2023, *Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold* | 10.3390/cells12101353 | https://doi.org/10.3390/cells12101353 | Strong mechanistic review; broad across poikilotherms/microbes | GO:0004768 stearoyl-CoA 9-desaturase activity (generic desaturase only approximate); GO:0006636; CHEBI:3558; label node: membrane fluidity |
| cis–trans isomerase activity → increases → membrane viscosity at higher temperature | Rapid remodeling of existing UFAs can counter excess fluidity during warming, relevant to wide thermal breadth | “An alternative rapid response is cis–trans isomerization of existing UFAs by a periplasmic cis–trans isomerase (Cti)… increased fluidity at higher temperature allows isomerization” and “trans-UFAs resemble SFAs and raise membrane viscosity” (wu2023molecularmechanismsof pages 2-3) | Wu, Baumeister, Heimbucher, 2023, *Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold* | 10.3390/cells12101353 | https://doi.org/10.3390/cells12101353 | Supports high-temperature compensation arm; wording combines two adjacent evidence statements from same excerpt | label node: cis-trans isomerase (Cti); CHEBI:3558 unsaturated fatty acid; label node: membrane viscosity |
| DesK/DesR two-component system → induces → acyl lipid desaturase expression | Membrane-bound signaling module causally links membrane rigidification to remodeling response | “Bacterial kinase-based two-component systems (e.g., DesK in Bacillus subtilis and Hik33 in Synechocystis) sense changes in bilayer viscosity/thickness or lipid motion and activate response regulators that induce acyl lipid desaturases, promoting membrane fluidity.” (wu2023molecularmechanismsof pages 3-5) | Wu, Baumeister, Heimbucher, 2023, *Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold* | 10.3390/cells12101353 | https://doi.org/10.3390/cells12101353 | Strong but taxon-specific exemplar; curate with Bacillus-specific note if gene-level node used | GO:0000160 phosphorelay signal transduction system; GO:0006636; UniProt/KEGG not provided in evidence; label nodes: DesK, DesR |
| increased short-/branched-/unsaturated fatty acids → increases → membrane fluidity | Multiple lipid chemistries jointly support low-temperature growth and broader thermal breadth | “Membrane composition adjustments highlighted include shifts in phospholipid headgroups (PC/PE), changes in acyl chain length/branching (SCFA, BCFA, anteiso vs iso), and increases in lysophospholipids (LPLs), all of which can increase membrane fluidity at lower temperatures.” (wu2023molecularmechanismsof pages 3-5) | Wu, Baumeister, Heimbucher, 2023, *Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold* | 10.3390/cells12101353 | https://doi.org/10.3390/cells12101353 | Strong but compositional summary; may be split into separate edges later | CHEBI:26666 short-chain fatty acid; CHEBI:35756 branched-chain fatty acid; CHEBI:3558 unsaturated fatty acid; CHEBI:32957 lysophospholipid; label node: membrane fluidity |
| low temperature exposure → upregulates → FAD2 omega-6 desaturase | Primary 2024 transcriptomic support for desaturase-mediated membrane remodeling under cold | “The paper notes FAD2 (omega-6 desaturase) and increased unsaturation at low temperature to maintain membrane fluidity” (jing2024transcriptomeresponseof pages 7-8) | Jing et al., 2024, *Transcriptome response of diatom Skeletonema marinoi to lower temperature* | 10.1007/s00227-024-04434-1 | https://doi.org/10.1007/s00227-024-04434-1 | Strong for cold response; eukaryotic microbe (diatom), not bacteria/archaea | GO:0006636 fatty acid biosynthetic process; label node: FAD2 omega-6 desaturase; CHEBI:3558 |
| low temperature exposure → upregulates → acyl-CoA/fatty-acid biosynthesis genes | Broader lipid biosynthesis activation supports membrane remodeling under cold | “Ten fatty-acid–related genes were upregulated at LT, with seven overlapping fatty-acid metabolism and biosynthesis categories; ACP and Acyl-CoA pathways are highlighted as central to fatty-acid synthesis and temperature adaptation.” (jing2024transcriptomeresponseof pages 7-8) | Jing et al., 2024, *Transcriptome response of diatom Skeletonema marinoi to lower temperature* | 10.1007/s00227-024-04434-1 | https://doi.org/10.1007/s00227-024-04434-1 | Strong pathway-level evidence; exact gene ortholog set not fully specified in excerpt | GO:0006633 fatty acid biosynthetic process; CHEBI:37554 acyl-CoA; label nodes: ACP pathway, Acyl-CoA pathway |
| low temperature exposure → upregulates → cold-shock DNA-binding domain protein | Nucleic-acid binding cold-shock proteins likely mitigate RNA/DNA structural constraints at low temperature | “a cold-shock DNA-binding domain upregulated 5.77-fold” (jing2024transcriptomeresponseof pages 7-8) | Jing et al., 2024, *Transcriptome response of diatom Skeletonema marinoi to lower temperature* | 10.1007/s00227-024-04434-1 | https://doi.org/10.1007/s00227-024-04434-1 | Strong expression evidence; mechanistic link to Td_>30 is inferred from cold acclimation | GO:0003676 nucleic acid binding; label node: cold-shock DNA-binding domain protein |
| hsp17 overexpression → increases → heat survival | Small heat shock protein directly improves bacterial thermotolerance, supporting high-temperature arm of broad thermal breadth | “At 45°C, TY(hsp17) survival after 4 h was ~76.90% versus 42.77% for wild type, and after 6 h TY(hsp17) stayed ~73.66% versus 30.40% for wild type.” (wang2023characterizationofhsp17 pages 7-10) | Wang et al., 2023, *Characterization of Hsp17, a Novel Small Heat Shock Protein, in Sphingomonas melonis TY under Heat Stress* | 10.1128/spectrum.01360-23 | https://doi.org/10.1128/spectrum.01360-23 | Strong direct genetics evidence; heat survival assay, not full growth-range phenotype | label node: hsp17; GO:0006457 protein folding; GO:0031072 heat shock protein binding maybe approximate; label node: heat survival |
| hsp17 deletion → decreases → ability to withstand high temperatures | Loss-of-function evidence strengthens causal role of Hsp17 in thermotolerance | “Deletion of hsp17 reduced heat resistance (TYDhsp17 ‘lost the ability to withstand high temperatures, especially at 37°C’)” (wang2023characterizationofhsp17 pages 7-10) | Wang et al., 2023, *Characterization of Hsp17, a Novel Small Heat Shock Protein, in Sphingomonas melonis TY under Heat Stress* | 10.1128/spectrum.01360-23 | https://doi.org/10.1128/spectrum.01360-23 | Strong gene-specific evidence; assay/species specific | label node: hsp17; GO:0006457; label node: thermotolerance |
| hsp17 overexpression → maintains → normal cell morphology under heat stress | Proteostasis can protect cellular architecture as well as viability under heat | “overexpression limited heat-induced filamentation and excessive cell elongation” (wang2023characterizationofhsp17 pages 7-10) | Wang et al., 2023, *Characterization of Hsp17, a Novel Small Heat Shock Protein, in Sphingomonas melonis TY under Heat Stress* | 10.1128/spectrum.01360-23 | https://doi.org/10.1128/spectrum.01360-23 | Strong within-species evidence; morphology maintenance is indirect support for broad temperature tolerance | label node: hsp17; GO:0006457; label node: cell morphology maintenance |
| heterologous hsp17 expression in E. coli → confers → heat resistance | Demonstrates transferable causal role of Hsp17 as a thermotolerance determinant | “the overexpression of hsp17 enabled the E. coli DH5a strain to grow... at 55°C for 3 h” (wang2023characterizationofhsp17 pages 7-10) | Wang et al., 2023, *Characterization of Hsp17, a Novel Small Heat Shock Protein, in Sphingomonas melonis TY under Heat Stress* | 10.1128/spectrum.01360-23 | https://doi.org/10.1128/spectrum.01360-23 | Strong heterologous functional evidence; survival/growth under assay conditions, not native Td_>30 trait | label node: hsp17; NCBITaxon:562 *Escherichia coli*; GO:0006457 |
| hyperthermophilic enzyme thermostability → resists → irreversible inactivation at high temperatures | Protein intrinsic stability is a direct mechanistic basis for extending upper growth limits | “Enzymes synthesized by hyperthermophiles… are typically thermostable (i.e., resistant to irreversible inactivation at high temperatures)” (vieille2001hyperthermophilicenzymessources pages 2-3) | Vieille & Zeikus, 2001, *Hyperthermophilic Enzymes: Sources, Uses, and Molecular Mechanisms for Thermostability* | 10.1128/MMBR.65.1.1-43.2001 | https://doi.org/10.1128/MMBR.65.1.1-43.2001 | Strong authoritative review; supports high-temperature arm generally, not specific breadth >30°C | GO:0003824 catalytic activity; label node: thermostable enzyme; label node: irreversible protein inactivation |
| hyperthermophile growth optimum >80°C → associated with → enzymes optimally active above 70°C | Coupling of organismal thermal adaptation to enzyme performance at high temperature | “hyperthermophiles are described as organisms that ‘grow optimally at temperatures between 80 and 110°C.’ It states that enzymes from hyperthermophiles have ‘high thermostability and optimal activity at temperatures above 70°C.’” (vieille2001hyperthermophilicenzymessources pages 2-3) | Vieille & Zeikus, 2001, *Hyperthermophilic Enzymes: Sources, Uses, and Molecular Mechanisms for Thermostability* | 10.1128/MMBR.65.1.1-43.2001 | https://doi.org/10.1128/MMBR.65.1.1-43.2001 | Strong association but not a direct manipulable edge; useful as background edge only | ENVO:09200014 hot spring not required; label node: hyperthermophile; label node: thermostable enzyme |
| broader thermal tolerance niche (T-resistant species) → trades off with → local performance | Ecological evidence that wide temperature breadth can incur “jack-of-all-trades, master-of-none” costs | “T-resistant species are advantageous of niche expansion but with poor local performance, as shown by wide niche breadth with high extinction, indicating these niche generalists are ‘jack-of-all-trades, master-of-none’.” (he2023highspeciationrate pages 1-2) | He et al., 2023, *High speciation rate of niche specialists in hot springs* | 10.1038/s41396-023-01447-4 | https://doi.org/10.1038/s41396-023-01447-4 | Ecological, not molecular; useful as cautionary systems-level edge for breadth trait | label node: thermal niche breadth; label node: local performance; ENVO:00000599 hot spring |
| high temperature environmental filtering → decreases → community-level thermal niche breadth | Hot-spring community study shows temperature can constrain realized breadth even in extreme systems | “higher temperature enhances environmental filtering, which reduces community abundance, reshapes community structure, and decreases community-level thermal niche breadth.” (he2023highspeciationrate pages 10-11) | He et al., 2023, *High speciation rate of niche specialists in hot springs* | 10.1038/s41396-023-01447-4 | https://doi.org/10.1038/s41396-023-01447-4 | Ecological community-level edge, not individual-cell mechanism; should be curated cautiously | ENVO:00000599 hot spring; label node: environmental filtering; label node: thermal niche breadth |


*Table: This table lists evidence-backed candidate causal edges for the microbial trait temperature delta high (extreme eurythermality), using only the specified sources. It is designed for TraitMech-style curation, with direct snippets, uncertainty notes, and provisional ontology grounding.*

**Key visual evidence for curation:** de Mendoza 2014 includes figures depicting lipid structural effects on membrane transition temperature and a mechanistic model of DesK/DesR control of unsaturated fatty-acid synthesis (mendoza2014temperaturesensingby media 26a67188, mendoza2014temperaturesensingby media 83d7475c).

---

### Recent developments (prioritizing 2023–2024)
1. **Direct genetic causality for thermotolerance via sHSPs (2023):** Hsp17 manipulation (deletion/overexpression) in *Sphingomonas melonis* shows clear causality between an sHSP and high-temperature survival outcomes, including heterologous transfer to *E. coli*. Quantitative survival at 45 °C (4–6 h) is explicitly reported. (wang2023characterizationofhsp17 pages 7-10)
2. **Transcriptomic evidence of lipid and cold-shock pathway induction under low temperature (2024):** in a eukaryotic microbe (*Skeletonema marinoi*), low temperature induces fatty-acid pathway genes and a cold-shock DNA-binding domain protein (5.77-fold), supporting the universality of lipid remodeling and nucleic-acid stress responses as components of broad thermal tolerance architectures. (jing2024transcriptomeresponseof pages 7-8)
3. **Thermal niche breadth operationalization in natural extreme gradients (2023):** hot-spring community analysis (54.8–80 °C) formalizes the niche-breadth concept and documents tradeoffs for temperature generalists (T-resistant taxa). (he2023highspeciationrate pages 1-2)

---

### Current applications and real-world implementations
**Industrial biotechnology / biocatalysis (thermostable enzymes):** Thermostable enzymes from thermophiles/hyperthermophiles are used because they withstand high temperatures and enable high-temperature catalysis; the hyperthermophilic enzyme review discusses industrial and research uses and emphasizes resistance to irreversible inactivation and high-temperature optima. (vieille2001hyperthermophilicenzymessources pages 2-3)

**Synthetic biology / strain engineering for stress tolerance:** The Hsp17 study explicitly notes that identifying heat resistance elements can support “synthetic biological applications,” and shows that heterologous expression can transfer heat resistance to *E. coli*—a relevant implementation pathway for engineering broad thermal performance in microbial hosts. (wang2023characterizationofhsp17 pages 7-10)

**Environmental and climate microbiology:** Thermal gradients shape microbial community structure and niche breadth; understanding breadth mechanisms informs predictions under warming and fluctuating thermal regimes (e.g., hot springs as natural thermal laboratories). (he2023highspeciationrate pages 1-2)

---

### Relevant statistics and quantitative data from cited studies
- **Thermal category anchors (review synthesis):** mesophiles favor ~**20–45 °C**; psychrophiles prefer ~**15 °C or below**; psychrotolerant bacteria may grow optimally at **20–25 °C** but survive below **0 °C**. (wu2023molecularmechanismsof pages 2-3)
- **Hot-spring gradient used to analyze thermal niche breadth:** **54.8–80 °C**. (he2023highspeciationrate pages 1-2)
- **Hsp17 thermotolerance effect sizes (primary data):** at 45 °C, survival after 4 h ~**76.90%** vs **42.77%** (overexpression vs WT); after 6 h ~**73.66%** vs **30.40%**; heterologous expression enables *E. coli* growth at **55 °C for 3 h** under the assay conditions. (wang2023characterizationofhsp17 pages 7-10)
- **Cold response expression change:** cold-shock DNA-binding domain upregulated **5.77-fold** in low-temperature treatment. (jing2024transcriptomeresponseof pages 7-8)

---

### DOI-first bibliography (with URLs and publication dates)
- de Mendoza D. **Temperature sensing by membranes.** *Annual Review of Microbiology* (Sep 2014). DOI: **10.1146/annurev-micro-091313-103612**. https://doi.org/10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 1-2)
- Wu G, Baumeister R, Heimbucher T. **Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold.** *Cells* (May 2023). DOI: **10.3390/cells12101353**. https://doi.org/10.3390/cells12101353 (wu2023molecularmechanismsof pages 2-3)
- Wang Y, Wang X, Wu H, et al. **Characterization of Hsp17, a Novel Small Heat Shock Protein, in Sphingomonas melonis TY under Heat Stress.** *Microbiology Spectrum* (Aug 2023). DOI: **10.1128/spectrum.01360-23**. https://doi.org/10.1128/spectrum.01360-23 (wang2023characterizationofhsp17 pages 7-10)
- Jing X, Zhen Y, Mi T-Z, et al. **Transcriptome response of diatom Skeletonema marinoi to lower temperature.** *Marine Biology* (Apr 2024). DOI: **10.1007/s00227-024-04434-1**. https://doi.org/10.1007/s00227-024-04434-1 (jing2024transcriptomeresponseof pages 7-8)
- He Q, Wang S, Feng K, et al. **High speciation rate of niche specialists in hot springs.** *The ISME Journal* (Jun 2023). DOI: **10.1038/s41396-023-01447-4**. https://doi.org/10.1038/s41396-023-01447-4 (he2023highspeciationrate pages 1-2)
- Vieille C, Zeikus GJ. **Hyperthermophilic Enzymes: Sources, Uses, and Molecular Mechanisms for Thermostability.** *Microbiology and Molecular Biology Reviews* (Mar 2001). DOI: **10.1128/MMBR.65.1.1-43.2001**. https://doi.org/10.1128/mmbr.65.1.1-43.2001 (vieille2001hyperthermophilicenzymessources pages 2-3)

---

### Curation warnings (claims not yet ready to curate into TraitMech as strong edges)
1. **Trait-level Td_>30 requires explicit Tmin/Tmax growth data.** The current evidence set strongly supports mechanisms (lipid remodeling, chaperones, thermostable enzymes), but does not provide a single microbial strain example with a documented growth interval explicitly exceeding 30 °C breadth; therefore, node/edge curation should be mechanistic unless additional breadth measurements are added.
2. **Assay mismatch risk:** high-temperature *survival* assays (e.g., 45–55 °C exposure) should be curated as **thermotolerance** mechanisms and only linked to Td_>30 as **supporting/inferred** unless accompanied by growth-range measurements. (wang2023characterizationofhsp17 pages 7-10)
3. **Taxon specificity:** DesK/DesR is a Bacillus exemplar; it may not generalize as gene-level nodes across taxa, though the two-component sensing concept is general. Curate as either Bacillus-specific edges or as a generic “two-component membrane fluidity sensing system” node if cross-taxa gene mapping is not intended. (wu2023molecularmechanismsof pages 3-5)
4. **Ecological breadth vs. physiological breadth:** hot-spring “T-resistant” operational definitions (presence across ≥5 temperatures) reflect distributional niche breadth, which may not equal organismal growth breadth in controlled assays. Curate these edges as ecological context or mark uncertain for direct mechanistic TraitMech nodes. (he2023highspeciationrate pages 1-2)


References

1. (wang2023characterizationofhsp17 pages 7-10): Yihan Wang, Xiaoyu Wang, Hao Wu, Lvjing Wang, Haixia Wang, and Zhenmei Lu. Characterization of hsp17, a novel small heat shock protein, in sphingomonas melonis ty under heat stress. Microbiology Spectrum, Aug 2023. URL: https://doi.org/10.1128/spectrum.01360-23, doi:10.1128/spectrum.01360-23. This article has 4 citations and is from a domain leading peer-reviewed journal.

2. (vieille2001hyperthermophilicenzymessources pages 2-3): Claire Vieille and Gregory J. Zeikus. Hyperthermophilic enzymes: sources, uses, and molecular mechanisms for thermostability. Microbiology and Molecular Biology Reviews, 65:1-43, Mar 2001. URL: https://doi.org/10.1128/mmbr.65.1.1-43.2001, doi:10.1128/mmbr.65.1.1-43.2001. This article has 2823 citations and is from a domain leading peer-reviewed journal.

3. (wu2023molecularmechanismsof pages 2-3): Gang Wu, Ralf Baumeister, and Thomas Heimbucher. Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold. Cells, 12:1353, May 2023. URL: https://doi.org/10.3390/cells12101353, doi:10.3390/cells12101353. This article has 87 citations.

4. (mendoza2014temperaturesensingby pages 1-2): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 209 citations and is from a peer-reviewed journal.

5. (wu2023molecularmechanismsof pages 3-5): Gang Wu, Ralf Baumeister, and Thomas Heimbucher. Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold. Cells, 12:1353, May 2023. URL: https://doi.org/10.3390/cells12101353, doi:10.3390/cells12101353. This article has 87 citations.

6. (mendoza2014temperaturesensingby media 26a67188): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 209 citations and is from a peer-reviewed journal.

7. (mendoza2014temperaturesensingby media 83d7475c): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 209 citations and is from a peer-reviewed journal.

8. (jing2024transcriptomeresponseof pages 7-8): Xiaoli Jing, Yu Zhen, Tie-zhu Mi, Zhigang Yu, Yucheng Wang, and Xiaohong Wang. Transcriptome response of diatom skeletonema marinoi to lower temperature. Marine Biology, Apr 2024. URL: https://doi.org/10.1007/s00227-024-04434-1, doi:10.1007/s00227-024-04434-1. This article has 3 citations and is from a peer-reviewed journal.

9. (he2023highspeciationrate pages 1-2): Qing He, Shang Wang, Kai Feng, Sean T Michaletz, Weiguo Hou, Wenhui Zhang, Fangru Li, Yidi Zhang, Danrui Wang, Xi Peng, Xingsheng Yang, and Ye Deng. High speciation rate of niche specialists in hot springs. The ISME Journal, 17:1303-1314, Jun 2023. URL: https://doi.org/10.1038/s41396-023-01447-4, doi:10.1038/s41396-023-01447-4. This article has 71 citations.

10. (he2023highspeciationrate pages 10-11): Qing He, Shang Wang, Kai Feng, Sean T Michaletz, Weiguo Hou, Wenhui Zhang, Fangru Li, Yidi Zhang, Danrui Wang, Xi Peng, Xingsheng Yang, and Ye Deng. High speciation rate of niche specialists in hot springs. The ISME Journal, 17:1303-1314, Jun 2023. URL: https://doi.org/10.1038/s41396-023-01447-4, doi:10.1038/s41396-023-01447-4. This article has 71 citations.