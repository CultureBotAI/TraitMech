---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:17:08.749880'
end_time: '2026-06-18T02:33:42.887550'
duration_seconds: 994.14
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature phenotype with numerical limits
  trait_identifier: METPO:1000533
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by specific temperature values or ranges that
    define growth or activity limits.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of
    high temperature (Thermophile-adaptation review supports temperature as the quantitative
    axis defining psychrophile, mesophile, and thermophile classification.) | DOI:10.1038/sj.embor.7400662:
    growing well at temperatures around the freezing point of water (Psychrophile
    review supports the low end of the temperature axis as a distinct quantitative
    phenotype.)'
  causal_graph_summary: 'temperature_phenotype_numerical_axis: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature phenotype with numerical limits
- **METPO identifier:** METPO:1000533
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific temperature values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports temperature as the quantitative axis defining psychrophile, mesophile, and thermophile classification.) | DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports the low end of the temperature axis as a distinct quantitative phenotype.)
- **Existing causal graph summary:** temperature_phenotype_numerical_axis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **temperature phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** temperature phenotype with numerical limits
- **METPO identifier:** METPO:1000533
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific temperature values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports temperature as the quantitative axis defining psychrophile, mesophile, and thermophile classification.) | DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports the low end of the temperature axis as a distinct quantitative phenotype.)
- **Existing causal graph summary:** temperature_phenotype_numerical_axis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **temperature phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_phenotype_with_numerical_limits.yaml`.

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


## Microbial Trait Causal Graph Curation Report

### Target trait
**Trait:** temperature phenotype with numerical limits (METPO:1000533; ENVIRONMENT; CLASS)

### Scope summary (curation-oriented)
This trait represents a **quantitative growth (or activity) phenotype defined by explicit temperature values/ranges**—classically the **cardinal temperatures** **Tmin**, **Topt**, and **Tmax**—that bound the temperatures at which a microorganism can grow (or a defined biological activity is measurable). It should be curated as **growth-limit phenotype parameters** rather than as an acute stress response (heat shock/cold shock), although stress-response mechanisms are often key causal mediators that shift/enable these limits. (ramon2023ageneraloverview pages 1-2, moon2023temperaturemattersbacterial pages 1-3)

**Thermal classes as boundary cases along the numerical axis.** Recent reviews operationalize these classes by growth-based temperature cutoffs: psychrophiles can grow at **0 °C** with **optima near/below ~15 °C** and may not grow at **20 °C**; psychrotolerant/psychrotroph microbes can grow at **4 °C** but have optima **above ~20 °C**; mesophiles grow roughly **~20–45 °C**; thermophiles have optima **~50–80 °C** and hyperthermophiles **~80–110 °C**. (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 1-3)

**Assay boundary considerations.** Curators should distinguish:
- **Steady-state growth limits (Tmin/Topt/Tmax)** vs **transient cold-shock/heat-shock responses**, since many mechanistic sources describe acute shifts rather than long-term growth boundaries. (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9)
- **Growth vs metabolic activity**: some sources cite metabolic activity at temperatures lower than sustained growth (e.g., activity at −20 °C). (purwar2024adaptationsofpsychrophilic pages 1-3)
- **Model-based inference of Tmin/Topt/Tmax** from growth-rate vs temperature data (e.g., Arrhenius/Ratkowsky/Cardinal models), which can produce numerical Tmin estimates with uncertainty depending on sampling near boundaries. (purwar2024adaptationsofpsychrophilic pages 8-10, omac2025comparisonofsecondary pages 1-2)

---

## 1) Key concepts and definitions (current understanding)

### Cardinal temperatures and numeric phenotype definition
- The quantitative axis is most naturally represented using **Tmin, Topt, Tmax** (cardinal temperatures for growth). Thermal classes (psychrophile/mesophile/thermophile) are defined by these growth boundaries. (jie2025thermaldiversityof pages 1-4, ramon2023ageneraloverview pages 1-2)
- One approach to quantifying temperature dependence of growth is fitting growth rate vs temperature with models; a 2024 review notes Arrhenius-type behavior used to describe temperature impacts on growth rates and discusses characteristic linearity ranges for psychrophiles vs mesophiles. (purwar2024adaptationsofpsychrophilic pages 8-10)

### Thermal class definitions (examples)
- Psychrophiles: “optimal temperature for growth at about 15 °C or lower… maximal… about 20 °C… minimal… 0 °C or below.” (jie2025thermaldiversityof pages 1-4)
- Psychrotrophs: can grow down to ~0 °C but have optima >15 °C. (jie2025thermaldiversityof pages 1-4)
- Review-level synthesis reports broad boundaries: psychrophiles grow at 0 °C with optima near 15 °C; thermophiles ~50–80 °C; hyperthermophiles ~80–110 °C. (ramon2023ageneraloverview pages 1-2)

### Mechanistic framing
A consistent mechanistic framing in 2023–2024 sources is that temperature limits are set by multiple coupled constraints on:
1) **Membrane physical state** (fluidity, thickness, phase behavior) and associated signaling. (maiti2024extrememakeoverthe pages 3-4, ramon2023ageneraloverview pages 2-4)
2) **Proteostasis and folding kinetics** (chaperones; prolyl isomerization; protein denaturation). (moon2023temperaturemattersbacterial pages 7-9)
3) **RNA structure/translation** (cold-shock proteins; RNA helicases; ribosome/translation recovery). (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9)
4) **DNA topology and transcriptional control** (supercoiling; gyrase/topoisomerase; ATP/ADP coupling). (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial media e9d8fc9d)
5) **Cryoprotection/ice interaction** for subzero persistence (antifreeze/ice-binding proteins; EPS; compatible solutes). (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 6-7, ramon2023ageneraloverview pages 21-22)

---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 Membrane homeoviscous adaptation as a central causal module
A 2024 feature article synthesizes **homeoviscous adaptation (HVA)** as a broadly conserved strategy in extremophiles: sensor proteins detect membrane physical changes (fluidity/lipid packing density) and trigger lipidome remodeling to avoid lethal gelation at low temperature (“fluid-to-gel phase transition”). (maiti2024extrememakeoverthe pages 3-4)

A 2023 cold-adaptation review emphasizes the same principle: the membrane undergoes a **liquid-crystalline → gel** transition as temperature falls, and the transition temperature depends on lipid composition; HVA includes increasing unsaturation, shortening chains, and adding branched-chain lipids as well as changing hopanoids and pigments. (ramon2023ageneraloverview pages 2-4)

### 2.2 Temperature sensing via membrane-associated two-component signaling (DesK/DesR)
A 2023 review of bacterial temperature responses describes transmembrane sensing and regulatory coupling: **DesK** (sensor kinase) and **DesR** (response regulator) induce desaturase transcription upon cooling. (moon2023temperaturemattersbacterial pages 7-9)

A 2023 cold adaptation review also generalizes this: cooling rigidifies membranes and can activate two-component systems that trigger transcriptional responses including desaturase induction. (ramon2023ageneraloverview pages 1-2)

### 2.3 DNA topology as a thermosensory/response axis (2023)
Moon et al. (2023) explicitly summarize the concept that **DNA topology participates in temperature sensing and response**: “DNA can function as a thermosensor by shifting the degree of supercoiling,” and energy state can couple through ATP-dependent gyrase (“Changes in [ATP]/[ADP] ratio may also affect DNA topology via ATP-dependent gyrase”). (moon2023temperaturemattersbacterial pages 1-3)

The paper’s schematic reinforces this cold/heat contrast in supercoiling and topoisomerase/gyrase involvement. (moon2023temperaturemattersbacterial media e9d8fc9d)

### 2.4 RNA-centric cold adaptation (CspA, CsdA, RNase R; 2023)
Moon et al. (2023) describes RNA maintenance during cold stress as a core necessity because low temperature increases inhibitory RNA secondary structures; they report RNase R collaboration: “RNase R selectively degrade the mRNA hairpin in collaboration with CspA and CsdA.” (moon2023temperaturemattersbacterial pages 1-3)

### 2.5 Expert views / gaps (2024)
A 2024 psychrophile-focused review highlights that despite many known adaptations and applications, “understanding their underlying mechanisms remains an ongoing challenge” and emphasizes a need to better understand metabolic adjustments. (purwar2024adaptationsofpsychrophilic pages 13-15)

---

## 3) Current applications and real-world implementations

### 3.1 Predictive microbiology and food safety: estimating Tmin from growth data
A recent applied modeling study (leafy greens; Salmonella) illustrates how **numerical Tmin can be inferred from growth-rate vs temperature datasets**. Using secondary growth models, the suboptimal Ratkowsky model provided an estimate **Tmin ≈ 7.3 °C** for Salmonella growth in leafy greens (and discusses parameter uncertainty when supra-optimal data are sparse). (omac2025comparisonofsecondary pages 1-2)

**Curation relevance:** this supports representing the trait with explicit numeric parameters and capturing “assay/model context” nodes (e.g., medium/host matrix) when available.

### 3.2 Cold-active enzymes and low-temperature bioprocessing
The 2024 psychrophile review lists multiple cold-active enzyme examples with operational points around **10 °C** (e.g., α-amylase, glucanases, aminopeptidase) and cites applications including textile processing (cold-active cellulases) and low-temperature biomass fermentation (example strain named). (purwar2024adaptationsofpsychrophilic pages 13-15)

### 3.3 Industrial and ecological implications of cold-capable growth
The 2023 cold adaptation review notes that **cold-adapted microbes/enzymes with high catalytic constants** are relevant to bioremediation and industrial processes (review-level claim). (ramon2023ageneraloverview pages 1-2)

The 2024 review emphasizes that psychrotrophs can be problematic in dairy contexts because they can grow at low temperatures and persist through processing. (purwar2024adaptationsofpsychrophilic pages 1-3, purwar2024adaptationsofpsychrophilic pages 13-15)

---

## 4) Candidate causal graph entities (nodes) with ontology grounding suggestions

| Group | Node label | Type | Suggested ontology grounding | Notes |
|---|---|---|---|---|
| Candidate graph nodes |  |  |  |  |
| Environmental/assay factors | Temperature | environmental factor | ENVO:09200014 (temperature) | Primary environmental axis determining observed growth limits and thermal classification (ramon2023ageneraloverview pages 1-2, moon2023temperaturemattersbacterial pages 1-3) |
| Environmental/assay factors | Cold shock | environmental factor | label-only candidate | Temperature downshift distinct from steady-state low-temperature growth assays; useful as assay context, not identical to Tmin/Topt/Tmax phenotype (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9) |
| Environmental/assay factors | Heat shock | environmental factor | label-only candidate | Temperature upshift distinct from long-term maximum growth temperature phenotype; should be separated from constitutive thermophily (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9) |
| Phenotype parameters | Tmin | phenotype parameter | label-only candidate | Minimum temperature permitting growth; central quantitative parameter for this trait (purwar2024adaptationsofpsychrophilic pages 8-10, omac2025comparisonofsecondary pages 1-2) |
| Phenotype parameters | Topt | phenotype parameter | label-only candidate | Temperature of maximal growth rate; used with Tmin/Tmax to classify thermal phenotype (ramon2023ageneraloverview pages 1-2) |
| Phenotype parameters | Tmax | phenotype parameter | label-only candidate | Maximum temperature permitting growth; part of cardinal temperature framework (jie2025thermaldiversityof pages 1-4, ramon2023ageneraloverview pages 1-2) |
| Phenotype parameters | Psychrophile | phenotype parameter | label-only candidate | Growth at 0 °C or below with optimum near or below 15 °C; thermal class on low end of axis (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 1-3) |
| Phenotype parameters | Psychrotroph / psychrotolerant | phenotype parameter | label-only candidate | Can grow at low temperature but has optimum above psychrophile range; boundary case near refrigeration growth (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 1-3) |
| Phenotype parameters | Mesophile | phenotype parameter | label-only candidate | Moderate-temperature growth class, roughly 20–45 °C in reviews (ramon2023ageneraloverview pages 1-2) |
| Phenotype parameters | Thermophile | phenotype parameter | label-only candidate | High-temperature growth class, roughly 50–80 °C in reviews (ramon2023ageneraloverview pages 1-2) |
| Membrane/lipid entities | Membrane fluidity | process | GO:0016042 | Core physical determinant of cold/heat adaptation and growth capability across temperatures (maiti2024extrememakeoverthe pages 3-4, moon2023temperaturemattersbacterial pages 7-9) |
| Membrane/lipid entities | Membrane thickness | process | label-only candidate | Physical property sensed by DesK; relevant to cold-induced signaling (moon2023temperaturemattersbacterial media e9d8fc9d, ramon2023ageneraloverview pages 22-23) |
| Membrane/lipid entities | Homeoviscous adaptation | process | label-only candidate | Lipid remodeling process maintaining membrane function across temperatures (maiti2024extrememakeoverthe pages 3-4, ramon2023ageneraloverview pages 2-4) |
| Membrane/lipid entities | Fatty acid unsaturation | process | GO:0033559 (unsaturated fatty acid biosynthetic process) | Increased at low temperature to prevent gelation and preserve growth (ramon2023ageneraloverview pages 2-4, purwar2024adaptationsofpsychrophilic pages 8-10) |
| Membrane/lipid entities | Fatty acid chain shortening | process | label-only candidate | Shorter acyl chains lower transition temperature and support low-temperature fluidity (maiti2024extrememakeoverthe pages 3-4, purwar2024adaptationsofpsychrophilic pages 8-10) |
| Membrane/lipid entities | Branched-chain fatty acids | chemical/process | CHEBI:35819 | Increased branching, especially anteiso forms, supports membrane fluidity in the cold (ramon2023ageneraloverview pages 4-5, purwar2024adaptationsofpsychrophilic pages 8-10) |
| Membrane/lipid entities | DesK | protein | UniProt/GO label-only candidate | Membrane sensor kinase detecting cooling-associated membrane changes (moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial media e9d8fc9d) |
| Membrane/lipid entities | DesR | protein | UniProt/GO label-only candidate | Response regulator activated by DesK to induce des expression (moon2023temperaturemattersbacterial pages 7-9) |
| Membrane/lipid entities | des (fatty acid desaturase gene) | gene | EC:1.14.19.- (broad desaturase class) | Encodes desaturase induced during cold adaptation in Bacillus model systems (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 22-23) |
| Membrane/lipid entities | FabF | protein | EC:2.3.1.179 | β-ketoacyl-ACP synthase II implicated in cis-vaccenic acid increase during cooling (ramon2023ageneraloverview pages 4-5) |
| Membrane/lipid entities | FabA | protein | EC:4.2.1.59 | Unsaturated fatty acid pathway component in E. coli cold-response remodeling (ramon2023ageneraloverview pages 2-4) |
| Membrane/lipid entities | FabB | protein | EC:2.3.1.41 | Unsaturated fatty acid synthesis component adjusting SFA/UFA balance (ramon2023ageneraloverview pages 2-4) |
| Membrane/lipid entities | FabR | protein | UniProt/GO label-only candidate | Transcriptional regulator of fatty acid composition in E. coli (ramon2023ageneraloverview pages 2-4) |
| Membrane/lipid entities | ACP (acyl carrier protein) | protein | UniProt label-only candidate | Carrier for fatty acid biosynthesis/remodeling mentioned in cold adaptation context (ramon2023ageneraloverview pages 4-5) |
| Membrane/lipid entities | cis-Vaccenic acid | chemical | CHEBI:30807 | Unsaturated fatty acid that increases during cooling in E. coli (ramon2023ageneraloverview pages 4-5, moon2023temperaturemattersbacterial pages 7-9) |
| Membrane/lipid entities | Palmitic acid | chemical | CHEBI:15756 | Saturated fatty acid decreased relative to unsaturated species during cold adaptation example (moon2023temperaturemattersbacterial pages 7-9) |
| Membrane/lipid entities | Hopanoids | chemical | CHEBI:51963 | Membrane-ordering lipids adjusted with temperature adaptation (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 22-23) |
| Membrane/lipid entities | Carotenoids | chemical | CHEBI:23044 | Pigments that modulate membrane properties during cold adaptation (ramon2023ageneraloverview pages 4-5, purwar2024adaptationsofpsychrophilic pages 6-7) |
| Membrane/lipid entities | Pigments | chemical | label-only candidate | Broad category including carotenoids and melanin associated with cold adaptation (purwar2024adaptationsofpsychrophilic pages 6-7) |
| Protein quality control & chaperones | DnaK | protein | UniProt/GO label-only candidate | Hsp70-family chaperone supporting protein folding under temperature stress (purwar2024adaptationsofpsychrophilic pages 6-7, moon2023temperaturemattersbacterial media 88a52e5a) |
| Protein quality control & chaperones | DnaJ | protein | UniProt/GO label-only candidate | Cochaperone in bacterial heat/cold stress protein quality control (moon2023temperaturemattersbacterial media 88a52e5a) |
| Protein quality control & chaperones | GroEL | protein | UniProt/GO label-only candidate | Chaperonin implicated in low-temperature protein folding support (purwar2024adaptationsofpsychrophilic pages 6-7, moon2023temperaturemattersbacterial media 88a52e5a) |
| Protein quality control & chaperones | GroES | protein | UniProt/GO label-only candidate | GroEL cochaperonin in cold-stress folding network (purwar2024adaptationsofpsychrophilic pages 6-7, moon2023temperaturemattersbacterial media 88a52e5a) |
| Protein quality control & chaperones | Trigger factor | protein | UniProt/GO label-only candidate | Ribosome-associated chaperone strongly overexpressed during cold adaptation example (moon2023temperaturemattersbacterial pages 7-9) |
| Protein quality control & chaperones | PPIases | protein/process | GO:0003755 | Peptidyl-prolyl isomerases help overcome slow proline isomerization at low temperature (moon2023temperaturemattersbacterial pages 7-9) |
| RNA/DNA-level factors | CspA | protein | UniProt/GO label-only candidate | Canonical cold shock protein that limits inhibitory RNA secondary structures (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9) |
| RNA/DNA-level factors | CsdA | protein | UniProt/GO label-only candidate | DEAD-box RNA helicase supporting translation and cold adaptation (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9) |
| RNA/DNA-level factors | RNase R | protein | UniProt/GO label-only candidate | Collaborates with CspA and CsdA in cold-response RNA processing (moon2023temperaturemattersbacterial pages 1-3) |
| RNA/DNA-level factors | DNA supercoiling | process | GO:0044781 | Temperature-responsive DNA topology linked to cold/heat adaptation and gene regulation (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial media e9d8fc9d) |
| RNA/DNA-level factors | DNA gyrase | protein complex/enzyme | EC:5.6.2.2 | ATP-dependent topoisomerase affecting supercoiling during temperature responses (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial media e9d8fc9d) |
| RNA/DNA-level factors | Topoisomerase I | protein/enzyme | EC:5.6.2.1 | Acts with gyrase in heat/cold-associated supercoiling shifts (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial media e9d8fc9d) |
| RNA/DNA-level factors | ATP/ADP ratio | chemical/state variable | CHEBI:15422 / CHEBI:16761 | Cellular energetic state modulates gyrase activity and DNA topology in temperature response (moon2023temperaturemattersbacterial pages 1-3) |
| Cryoprotection/solutes | Trehalose | chemical | CHEBI:16589 | Compatible solute associated with protection against freezing/cold stress (ramon2023ageneraloverview pages 21-22) |
| Cryoprotection/solutes | Glycine betaine | chemical | CHEBI:17750 | Compatible solute associated with protection against freezing/cold stress (ramon2023ageneraloverview pages 21-22) |
| Cryoprotection/solutes | Antifreeze proteins | protein | GO label-only candidate | Ice-binding proteins preventing ice crystal growth/recrystallization (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 6-7) |
| Cryoprotection/solutes | Ice-binding proteins | protein | GO label-only candidate | Proteins binding ice surfaces to protect cells in freezing environments (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 6-7) |
| Cryoprotection/solutes | EPS (extracellular polysaccharides) | chemical/process | GO:0045226 | Protective extracellular matrix/cryoprotectant noted in cold adaptation (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10) |
| Metabolic/other | Cold-adapted enzymes | process/protein class | label-only candidate | High catalytic efficiency at low temperature supports psychrophilic growth (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 13-15) |
| Metabolic/other | Two-component signaling | process | GO:0000160 | Membrane-state sensing and transcriptional response mechanism in cold adaptation (ramon2023ageneraloverview pages 1-2, moon2023temperaturemattersbacterial pages 7-9) |


*Table: This table compiles candidate nodes for a TraitMech causal graph of microbial temperature phenotype with numerical limits. It groups supported entities by biological role and suggests ontology grounding where plausible, helping prioritize curatable nodes.*

---

## 5) Evidence-backed candidate edges (triples) for curation

| Subject | Predicate | Object | Evidence (citation id, DOI, year, URL) | Supporting snippet (short quote) | Notes for curation (including whether it supports Tmin/Topt/Tmax; taxon/assay specificity) | Certainty |
|---|---|---|---|---|---|---|
| Membrane rigidification during cooling | activates | DesK/DesR two-component signaling | pqac-00000008; DOI:10.1007/s42770-023-01057-4; 2023; https://doi.org/10.1007/s42770-023-01057-4 | "Membrane-based cold sensing occurs via modification of the liquid-crystalline membrane state, activating two-component signalling" | Good generic cold-adaptation edge; supports mechanism underlying lower-temperature growth, but not a direct numeric Tmin/Topt/Tmax parameter. Broad microbial review; not universal for all taxa. | high |
| DesK | phosphorylates/activates | DesR | pqac-00000013; DOI:10.1007/s12275-023-00031-x; 2023; https://doi.org/10.1007/s12275-023-00031-x | "transmembrane kinases (DesK) ... phosphorylate DesR to induce D5-desaturase transcription during cooling" | Strong mechanistic edge from Bacillus subtilis model. Taxon-specific but canonical for membrane-thickness sensing in Gram-positive bacteria. Indirect support for low-temperature growth limit adaptation. | high |
| DesR | induces expression of | des (fatty acid desaturase gene) | pqac-00000013; DOI:10.1007/s12275-023-00031-x; 2023; https://doi.org/10.1007/s12275-023-00031-x | "phosphorylate DesR to induce D5-desaturase transcription during cooling" | Curatable as regulatory edge if des is represented as fatty acid desaturase. Strong but Bacillus-focused. Supports adaptation below Topt rather than cardinal limits directly. | high |
| des / fatty acid desaturase activity | increases | fatty acid unsaturation | pqac-00000009; DOI:10.1007/s42770-023-01057-4; 2023; https://doi.org/10.1007/s42770-023-01057-4 | "a two-component sensor triggers transcriptional activation of desaturases that introduce double bonds into membrane fatty acids" | Broad review-level support. Object can be modeled as unsaturated fatty acid biosynthetic process. Mechanistically linked to cold growth capacity. | high |
| Increased fatty acid unsaturation | increases | membrane fluidity | pqac-00000012; DOI:10.37256/amtt.5220244537; 2024; https://doi.org/10.37256/amtt.5220244537 | "decreasing lipid saturation, to maintain optimal membrane fluidity" | Strong generic membrane-physics edge. Supports low-temperature growth competence rather than a specific Tmin value. | high |
| Membrane fluidity maintenance | supports | growth at low temperature | pqac-00000010; DOI:10.1039/d4cc03114h; 2024; https://doi.org/10.1039/d4cc03114h | "trigger lipidome remodeling to prevent a lethal fluid-to-gel phase transition at low temperature" | Good high-level phenotype edge. Connects membrane state to survival/growth near low-temperature boundary. Not organism-specific; suitable as generic process→phenotype edge. | high |
| FabF | increases | cis-vaccenic acid during cooling | pqac-00000005; DOI:10.1007/s42770-023-01057-4; 2023; https://doi.org/10.1007/s42770-023-01057-4 | "The key enzyme in the increase of cis-vaccenic acid is FabF" | Strong enzyme→lipid edge. Mostly based on E. coli/mesophile literature within review; taxon specificity should be noted. Useful mechanistic subgraph for cold adaptation. | high |
| Hopanoid composition change | modulates | membrane ordering/fluidity during cold adaptation | pqac-00000005; DOI:10.1007/s42770-023-01057-4; 2023; https://doi.org/10.1007/s42770-023-01057-4 | "Hopanols ... enhance the ordering of lipid chains" | Good biochemical edge, but role can vary by taxon and direction depends on hopanoid type/unsaturation. Supports membrane adaptation, not direct cardinal temperature assignment. | medium |
| Carotenoids/pigments | modulate | membrane physical properties during cold adaptation | pqac-00000015; DOI:10.37256/amtt.5220244537; 2024; https://doi.org/10.37256/amtt.5220244537 | "Carotenoids, melanin" | Evidence is review-level and more general than gene-specific. Curate cautiously as pigment→membrane adaptation, with broad taxon scope and uncertain magnitude. | medium |
| Low temperature | induces | CspA | pqac-00000002; DOI:10.1007/s12275-023-00031-x; 2023; https://doi.org/10.1007/s12275-023-00031-x | "cspA gene is induced during cold shocks" | Strong cold-shock edge, especially in E. coli. Distinguish transient cold-shock response from constitutive low Tmin phenotype. | high |
| Low temperature | induces | CsdA RNA helicase | pqac-00000013; DOI:10.1007/s12275-023-00031-x; 2023; https://doi.org/10.1007/s12275-023-00031-x | "cells overexpress ... RNA helicases (CsdA) and cold-shock proteins (CspA)" | Good cold-response edge. Better curated as acclimation mechanism rather than direct determinant of numerical Tmin. | high |
| Low temperature | induces | trigger factor / PPIases | pqac-00000013; DOI:10.1007/s12275-023-00031-x; 2023; https://doi.org/10.1007/s12275-023-00031-x | "overexpress PPIases and chaperones (e.g., trigger factor ~40-fold)" | Strong response edge from review. Best represented as protein-folding support subgraph. Assay context is cold shift/adaptation. | high |
| RNase R | collaborates with | CspA and CsdA to degrade mRNA hairpins | pqac-00000002; DOI:10.1007/s12275-023-00031-x; 2023; https://doi.org/10.1007/s12275-023-00031-x | "RNase R selectively degrade the mRNA hairpin in collaboration with CspA and CsdA" | Clear mechanistic RNA-processing edge. Supports translation under cold stress, indirectly affecting low-temperature growth. Likely species/examples from model bacteria. | high |
| Temperature shift | changes | ATP/ADP ratio | pqac-00000002; DOI:10.1007/s12275-023-00031-x; 2023; https://doi.org/10.1007/s12275-023-00031-x | "Changes in [ATP]/[ADP] ratio may also affect DNA topology" | Intermediate state variable edge. Evidence connects energetic state to temperature response; directness varies with organism and shock conditions. | medium |
| ATP/ADP ratio | modulates | DNA gyrase activity | pqac-00000002; DOI:10.1007/s12275-023-00031-x; 2023; https://doi.org/10.1007/s12275-023-00031-x | "affect DNA topology via ATP-dependent gyrase" | Strong enzyme-regulation edge. Useful in DNA-topology branch; not directly cardinal-temperature-specific. | high |
| DNA gyrase / topoisomerase I activity | changes | DNA supercoiling | pqac-00000002; DOI:10.1007/s12275-023-00031-x; 2023; https://doi.org/10.1007/s12275-023-00031-x | "gyrase cooperates with topoisomerase I" | Good topology edge. Figure-based summary also supports heat causes relaxation and cold enhances negative supercoiling (moon2023temperaturemattersbacterial media e9d8fc9d). Consider representing as process-level edge. | high |
| DNA supercoiling change | changes | transcription during temperature response | pqac-00000002; DOI:10.1007/s12275-023-00031-x; 2023; https://doi.org/10.1007/s12275-023-00031-x | "DNA can function as a thermosensor by shifting the degree of supercoiling" | Strong mechanistic statement linking topology to gene regulation. General bacterial response edge, indirect to Tmin/Topt/Tmax. | high |
| Antifreeze / ice-binding proteins | bind | ice crystal surfaces | pqac-00000007; DOI:10.37256/amtt.5220244537; 2024; https://doi.org/10.37256/amtt.5220244537 | "protecting cells by binding to ice crystal surfaces" | Strong cryoprotection edge relevant to subzero survival. Best tied to survival/growth below 0 °C in psychrophiles rather than generic bacteria. | high |
| Antifreeze proteins | prevent | formation and growth of ice crystals | pqac-00000003; DOI:10.37256/amtt.5220244537; 2024; https://doi.org/10.37256/amtt.5220244537 | "prevent the formation and growth of ice crystals" | Strong mechanistic protection edge; good support for very low Tmin or below-freezing persistence. May be survival-focused rather than growth-focused. | high |
| Trehalose / glycine betaine | protect against | freezing and osmotic stress | pqac-00000009; DOI:10.1007/s42770-023-01057-4; 2023; https://doi.org/10.1007/s42770-023-01057-4 | "compatible solutes (trehalose, glycine-betaine)" | Review states these as protective solutes in cold adaptation. Specific mechanism broad; curate as compatible solute→cold protection, with phenotype link indirect. | medium |
| Cold-adapted enzymes | enable | high catalytic efficiency at low temperature | pqac-00000008; DOI:10.1007/s42770-023-01057-4; 2023; https://doi.org/10.1007/s42770-023-01057-4 | "cold-adapted proteins ... yielding high catalytic efficiency" | Strong high-level edge from review. Suitable process-class node; broad and not gene-specific. Supports Topt/Tmin adaptation conceptually. | high |
| High catalytic efficiency at low temperature | supports | growth at low temperature | pqac-00000019; DOI:10.37256/amtt.5220244537; 2024; https://doi.org/10.37256/amtt.5220244537 | "cold-active enzymes" with examples operating at "10 °C" | Useful phenotype edge linking enzyme performance to real-world low-temperature growth/activity. Evidence is application-oriented and somewhat indirect for growth limits. | medium |


*Table: This table compiles evidence-backed candidate triples for a TraitMech graph of microbial temperature phenotype with numerical limits. It links membrane remodeling, RNA/protein quality control, DNA topology, and cryoprotection mechanisms to low-temperature growth capacity and related thermal limits.*

---

## 6) Relevant statistics and data points (recent sources)

### Global prevalence of cold environments (context for trait importance)
- A 2023 review states that **~85% of the terrestrial biosphere** remains **below 5 °C** year-round and **~90% of oceans** are **<5 °C**, implying that Tmin and low-temperature growth capacity are broadly ecologically relevant traits. (ramon2023ageneraloverview pages 1-2)

### Reported extremes (species-level)
- A 2024 review reports that *Psychrobacter cryopegella* can “thrive” at **−10 °C** and maintain metabolic activity at **−20 °C**, while microbial habitats are described as spanning **122 °C to −20 °C** (note: activity vs growth should be separated in curation). (purwar2024adaptationsofpsychrophilic pages 1-3)

### Thermal class numeric boundaries (review-level)
- Psychrophiles: growth at 0 °C, optimum near ~15 °C, not at 20 °C; psychrotolerants: grow at 4 °C with optima >20 °C; thermophiles and hyperthermophiles have optima in 50–80 °C and 80–110 °C ranges, respectively. (ramon2023ageneraloverview pages 1-2)

### Example numeric phenotype parameter from an applied dataset/model
- Salmonella in leafy greens: estimated **Tmin = 7.3 °C** in a suboptimal Ratkowsky fit to literature-derived μmax vs temperature data. (omac2025comparisonofsecondary pages 1-2)

---

## 7) Visual evidence (useful for curators)
Moon et al. (2023) provides a compact visual summary connecting temperature changes to (i) **DNA supercoiling/topoisomerase-gyrase involvement**, (ii) **chaperone systems**, and (iii) **membrane lipid adaptation**, useful as a high-level mechanistic scaffold for node/edge selection. (moon2023temperaturemattersbacterial media e9d8fc9d, moon2023temperaturemattersbacterial media 88a52e5a, moon2023temperaturemattersbacterial media 7b86c835)

---

## Warnings / curation cautions (what should not yet be curated as strong TraitMech edges)
1) **Cold shock vs Tmin:** Many mechanistic claims are described for **acute cold shock** (e.g., induction of CspA/CsdA) rather than steady-state growth at Tmin; curate these as **context-dependent acclimation mechanisms** unless the source explicitly links them to a measured shift in Tmin/Tmax. (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9)
2) **Survival vs growth:** Antifreeze/ice-binding proteins and compatible solutes often support **survival/persistence** below freezing rather than sustained growth; avoid over-asserting direct effects on “growth Tmin” without explicit evidence. (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 6-7, ramon2023ageneraloverview pages 21-22)
3) **Pigments/hopanoids:** Evidence is frequently review-level and can be taxon- and condition-dependent; treat these edges as **medium certainty** until supported by direct experimental causal tests in defined taxa. (ramon2023ageneraloverview pages 4-5, purwar2024adaptationsofpsychrophilic pages 6-7)
4) **Ontology grounding:** Many protein/gene nodes (DesK/DesR/CspA/CsdA etc.) are **taxon-specific**; do not assign a single UniProt ID unless the curated edge is explicitly species/strain-grounded.

---

## DOI-first bibliography (with dates and URLs)

1. Ramón A, Esteves A, Villadóniga C, Chalar C, Castro-Sowinski S. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology.* **2023-07**. DOI: **10.1007/s42770-023-01057-4**. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 21-22, ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 22-23)
2. Moon S, Ham S, Jeong J, Ku H, Kim H, Lee C. **Temperature matters: bacterial response to temperature change.** *Journal of Microbiology.* **2023-03**. DOI: **10.1007/s12275-023-00031-x**. https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial media e9d8fc9d, moon2023temperaturemattersbacterial media 88a52e5a, moon2023temperaturemattersbacterial media 7b86c835)
3. Purwar S, Srivastava S. **Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.** *Applied Microbiology: Theory ＆ Technology.* **2024-10**. DOI: **10.37256/amtt.5220244537**. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 1-3, purwar2024adaptationsofpsychrophilic pages 3-4, purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 13-15)
4. Maiti A, Erimban S, Daschakraborty S. **Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.** *Chemical Communications.* **2024-08**. DOI: **10.1039/d4cc03114h**. https://doi.org/10.1039/d4cc03114h (maiti2024extrememakeoverthe pages 3-4)

(Additional, non-2023/2024 applied example)
5. Omaç B. **Comparison of Secondary Models for Modelling the Growth of Salmonella in Leafy Greens.** *Turkish Journal of Agriculture - Food Science and Technology.* **2025-12**. DOI: **10.24925/turjaf.v13is3.3927-3933.8140**. https://doi.org/10.24925/turjaf.v13is3.3927-3933.8140 (omac2025comparisonofsecondary pages 1-2)


References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

3. (purwar2024adaptationsofpsychrophilic pages 1-3): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

4. (moon2023temperaturemattersbacterial pages 7-9): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

5. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

6. (omac2025comparisonofsecondary pages 1-2): Basri Omaç. Comparison of secondary models for modelling the growth of salmonella in leafy greens. Turkish Journal of Agriculture - Food Science and Technology, 13:3927-3933, Dec 2025. URL: https://doi.org/10.24925/turjaf.v13is3.3927-3933.8140, doi:10.24925/turjaf.v13is3.3927-3933.8140. This article has 0 citations.

7. (jie2025thermaldiversityof pages 1-4): CX Jie, NHM Yusuf, and CMWV Ling. Thermal diversity of bacteria and their secrets to cold survival. Unknown journal, 2025.

8. (maiti2024extrememakeoverthe pages 3-4): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

9. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

10. (moon2023temperaturemattersbacterial media e9d8fc9d): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

11. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

12. (ramon2023ageneraloverview pages 21-22): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

13. (purwar2024adaptationsofpsychrophilic pages 13-15): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

14. (ramon2023ageneraloverview pages 22-23): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

15. (ramon2023ageneraloverview pages 4-5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

16. (moon2023temperaturemattersbacterial media 88a52e5a): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

17. (moon2023temperaturemattersbacterial media 7b86c835): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

18. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.