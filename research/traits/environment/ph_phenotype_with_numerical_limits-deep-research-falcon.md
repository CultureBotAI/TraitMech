---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:30:45.788020'
end_time: '2026-06-18T00:46:00.463795'
duration_seconds: 914.68
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH phenotype with numerical limits
  trait_identifier: METPO:1000531
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by specific pH values or ranges that define
    growth or activity limits.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports
    external pH as the quantitative axis underlying acidophile, neutrophile, and alkaliphile
    classification.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis
    review supports the proton motive force across the cell envelope as the physical
    link between external pH and microbial growth physiology.)'
  causal_graph_summary: 'ph_phenotype_numerical_axis: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH phenotype with numerical limits
- **METPO identifier:** METPO:1000531
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific pH values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports external pH as the quantitative axis underlying acidophile, neutrophile, and alkaliphile classification.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force across the cell envelope as the physical link between external pH and microbial growth physiology.)
- **Existing causal graph summary:** ph_phenotype_numerical_axis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pH phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** pH phenotype with numerical limits
- **METPO identifier:** METPO:1000531
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific pH values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports external pH as the quantitative axis underlying acidophile, neutrophile, and alkaliphile classification.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force across the cell envelope as the physical link between external pH and microbial growth physiology.)
- **Existing causal graph summary:** ph_phenotype_numerical_axis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pH phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_phenotype_with_numerical_limits.yaml`.

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


## Scope summary (METPO:1000531)

**Trait label:** pH phenotype with numerical limits (METPO:1000531)

**Operational interpretation for curation:** a quantitative phenotype describing **external environmental pH values/ranges that bound growth or activity** (minimum permissible pH, maximum permissible pH, and/or optimum pH). This trait should be curated as a *measured, numeric axis* (external pH), while mechanisms generally act by maintaining **intracellular pH homeostasis and proton motive force (PMF)** despite external pH variation. Neutralophilic bacteria commonly maintain internal pH ~7.0–7.5 and a relatively constant PMF over an external pH range ~5–8, implying that **failure of homeostasis mechanisms at extremes** contributes to minimum/maximum growth pH limits. (poolman2023physicochemicalhomeostasisin pages 1-2)

### Boundary cases / distinctions

1. **Preference vs tolerance:** “pH preference” (optimum growth/activity) differs from “tolerance/survival” at extreme pH without growth. For example, E. coli strains may grow across an intestinal range ~pH 4.5–9.0 but can **survive** at pH 2 without growing for hours. (li2024responseofescherichia pages 1-2)
2. **Category tendencies vs numeric trait:** Extremophile category terms provide approximate numeric tendencies—acidophiles “generally grow optimally at pH below 3,” whereas alkaliphiles “require pH 9 or above for growth.” These are useful for annotation but are not substitutes for species/strain-specific numeric limits measured in defined assays. (rekadwad2023extremophilesthespecies pages 8-10)
3. **Assay-defined vs environment-inferred pH phenotypes:** Culture-based determination of pH range/optimum can miss diversity; one high-pH sediment example (pH 9.16–10.16) notes that a large fraction of microbes are not recovered by cultivable methods, emphasizing bias that should be captured as *evidence context*, not biology. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7)

## Key concepts and definitions (current understanding)

### External pH, intracellular pH, and proton motive force (PMF)

A mechanistic backbone linking external pH to growth limits is the requirement to maintain **intracellular pH and PMF**. Poolman (2023) emphasizes that many bacteria maintain internal pH ~7.0–7.5 and regulate PMF (Δψ + ΔpH term), with **Na+/H+ and K+/H+ antiporters**, **proton-pumping respiratory chains**, **F0F1-ATPase**, and **metabolite decarboxylation pathways** among “main regulators of internal pH/PMF.” (poolman2023physicochemicalhomeostasisin pages 1-2)

### Proton-consuming reactions and antiport cycles

Poolman (2023) describes amino-acid **decarboxylation + antiporter** systems as directly consuming protons: the decarboxylation reaction consumes a proton and, when coupled to transport, yields an effective proton pumping effect (≈1 proton per decarboxylation). This provides a *self-regulatory* pH homeostasis mechanism because decarboxylases can be activated when internal pH drops. (poolman2023physicochemicalhomeostasisin pages 2-4)

### Canonical acid-resistance modules (E. coli)

A well-defined mechanistic example is E. coli’s glutamate-dependent acid resistance system (AR2/Gad). GadA/GadB decarboxylate glutamate to GABA + CO2 while consuming H+, and GadC antiports GABA for extracellular glutamate, sustaining proton consumption. Deleting gadA/gadB/gadC impairs survival at pH ~2–3 in cited work summarized by Li et al. (2024). (li2024responseofescherichia pages 2-4)

### Quantitative internal vs external pH separation in acidophiles

Acidophiles can maintain relatively higher internal pH while growing at far lower external pH. Acidophilic sulphate reducers are described as maintaining internal pH around 6.0 while growing below external pH 3.0, implying that the pH phenotype with numerical limits is ultimately constrained by the capacity to preserve large ΔpH gradients. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

## Recent developments and latest research (prioritizing 2023–2024)

### (1) Genome-to-phenotype associations for pH preference across environments (2023)

Ramoneda et al. (Science Advances, 2023) compiled distribution data across **1470 samples** spanning soil/freshwater pH gradients and linked gene families to pH preference, including consistent associations across multiple datasets. Mechanistically plausible gene categories include **Na+/H+ antiporters** (linked to higher-pH preference) and **urease/urea transport** (linked to low-pH preference via production of basic compounds). The authors stress these are primarily **associations** (hypothesis-generating) rather than confirmed causal determinants of growth pH limits. (ramoneda2023buildingagenomebased pages 3-5)

### (2) Systems-level characterization and engineering of acid tolerance (2024)

Qin et al. (Microorganisms, 2024) studied an engineered acid-tolerant E. coli strain containing a synthetic module including **gadE**, **hdeB**, and ROS scavengers (**sodB**, **katE**). Under mild acid stress (pH 6.0), the engineered strain achieved a **final OD600 131%** (and 124% in another comparison) relative to its parent, while transcriptomics associated tolerance with **oxidative phosphorylation**, **TCA cycle**, and transport/metabolic modules (e.g., **ABC transporters**). (qin2024characterizationofmild pages 1-2)

### (3) Environmental/engineering microbiology: small-molecule modulation of pH stress (2024)

In activated sludge biofilms, Jiang et al. (Applied and Environmental Microbiology, 2024) report that exogenous **putrescine** can act as a “switch-like distributor” of pH stress adaptability: at low pH, increased protonation promotes entry and boosts proton-consuming strategies (glutamate-based AR and GABA metabolism) and ATPase expression, whereas under alkaline conditions limited protonation and intracellular H+ consumption can exacerbate alkali stress. (jiang2024exogenousputrescineplays pages 1-2)

### (4) Updated synthesis for low-pH biotechnology (2024)

Atasoy et al. (FEMS Microbiology Reviews, 2024) synthesize the state of the art in exploiting microbial activities at low pH across food, environmental and biomanufacturing contexts, including quantitative industrial metrics (see Applications section). (atasoy2024exploitationofmicrobial pages 10-11)

## Current applications and real-world implementations (with recent quantitative data)

### Low-pH biomanufacturing (organic acids)

Atasoy et al. (2024) summarize industrially relevant low-pH production metrics for lactic acid: **Rhizopus oryzae** can reach lactic acid concentrations up to **230 g/L** but at medium pH >4.5, while an engineered yeast (Cargill CB1) can produce **>135 g/L lactic acid at pH 3** (with ~90% in free lactic acid form). These figures illustrate that *low pH is both a stressor and a process lever* (reduced contamination, altered product speciation), motivating selection/engineering of pH-robust strains. (atasoy2024exploitationofmicrobial pages 10-11)

### Wastewater/bioremediation under acidic conditions

Atasoy et al. (2024) cite an acidic-sediment reactor achieving **>99% dissolved metals removal** (except Mn), **>75% sulfate removal**, and **>85% iron removal**, demonstrating real-world engineering relevance of low-pH-adapted microbial processes. (atasoy2024exploitationofmicrobial pages 10-11)

### Acid mine drainage (AMD) treatment and circular-economy metal recovery

Valdez-Nuñez et al. (2024) emphasize acidophilic sulphate-reducing bacteria (aSRB) as candidates for AMD treatment (AMD often **pH <3**), leveraging biogenic sulfide production to precipitate metals and potentially recover metal sulfide nanoparticles. They compile occurrences/enrichments of aSRB in acidic settings (e.g., sediments/pore waters around pH ~2.6–4.8 with reported sulfate and Eh ranges), supporting feasibility and constraints for implementation. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2)

## Expert opinions and analysis (authoritative sources)

### Mechanistic consensus: pH limits emerge from homeostasis capacity

A cross-source consensus is that external pH phenotypes (min/max/optimum) reflect the **cell’s ability to maintain internal pH/PMF** and prevent macromolecular damage. Poolman (2023) highlights regulation of internal pH and PMF by ion antiporters, proton pumps, ATPase, and proton-consuming metabolism. (poolman2023physicochemicalhomeostasisin pages 1-2)

### Evidence quality: association vs causation in genome-based pH prediction

Ramoneda et al. (2023) provide a rigorous genome/environment association framework and predictive modeling for pH preference, but explicitly the mechanistic interpretation should be curated as **uncertain** unless validated experimentally; this is crucial for TraitMech causal graphs, which require causal edges rather than only correlational associations. (ramoneda2023buildingagenomebased pages 3-5)

### Assay bias is material to pH phenotype claims

For high-pH environments, cultivation bias can strongly distort observed pH phenotype distributions; the alkaliphilic fungi review notes many taxa are missed by culture-based methods, which should be recorded as evidence context when importing “pH range” claims from environmental datasets or enrichments. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7)

## Candidate causal-graph nodes (grouped by type)

### Trait/environment nodes
- **External pH (axis node)** (CHEBI:33996 for hydrogen ion activity; label-only node “external pH”) (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Minimum growth pH / maximum growth pH / optimum growth pH** (label-only phenotype nodes under METPO:1000531)
- **Intracellular pH** (label-only), **pH homeostasis** (candidate GO:0006885, approximate) (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Proton motive force (PMF)** (label-only; related to membrane potential and ΔpH) (poolman2023physicochemicalhomeostasisin pages 1-2)

### Transporters/complexes
- **F-type ATPase / F0F1-ATPase** (GO:0046933) (poolman2023physicochemicalhomeostasisin pages 1-2, li2024responseofescherichia pages 2-4)
- **Na+/H+ antiporters** (GO:0015385) (poolman2023physicochemicalhomeostasisin pages 1-2)
- **K+/H+ antiporters** (label-only; antiporter activity) (poolman2023physicochemicalhomeostasisin pages 1-2)

### Acid resistance / metabolic proton consumption
- **GadA/GadB glutamate decarboxylases** (label-only protein nodes), **GadC antiporter** (label-only) (li2024responseofescherichia pages 2-4)
- **YbaS glutaminase** (label-only), **ammonia** (CHEBI:16134) as buffering agent (li2024responseofescherichia pages 2-4)
- **Amino-acid decarboxylase + antiporter systems** (label-only module node) (poolman2023physicochemicalhomeostasisin pages 2-4)

### Membrane/cell envelope adaptations
- **Saturated fatty acids / lipid remodeling** (label-only; membranes less proton-permeable) (yao2023howmethanotrophsrespond pages 5-7)
- **S-layer glycoproteins / SCWPs** (label-only; increased negative surface charge to recruit protons in alkaliphiles) (yao2023howmethanotrophsrespond pages 5-7)

### Chemicals/modulators
- **Putrescine** (CHEBI:17126) (jiang2024exogenousputrescineplays pages 1-2)
- **GABA** (CHEBI:16865) (li2024responseofescherichia pages 2-4)
- **Glycine betaine** (CHEBI:17750) and compatible solute transport (label-only; OpuA mentioned) (poolman2023physicochemicalhomeostasisin pages 2-4)

### Evidence/assay context nodes
- **Cultivation bias / uncultured fraction** (label-only) (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7)
- **Biogeographic inference / genome-based prediction** (label-only) (ramoneda2023buildingagenomebased pages 3-5)

## Candidate causal edges (evidence-backed)

The table below is a curation-ready set of candidate edges (SPO triples) with snippets and notes.

| Subject node (CURIE) | Predicate | Object node (CURIE) | Context/condition | Evidence snippet | Reference | Curation notes |
|---|---|---|---|---|---|---|
| external pH (CHEBI:33996) | determines | proton motive force across cell envelope (label-only candidate; related GO:0098869) | neutralophilic bacteria across external pH ~5–8 | “neutralophilic bacteria maintaining a relatively constant proton motive force across external pH ~5–8” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | Broad review-level edge; suitable as high-level trait axis. |
| external pH (CHEBI:33996) | perturbs | cytoplasmic pH homeostasis (GO:0006885 approximate) | low-pH stress / acidophiles | acidophiles maintain “internal pH of around 6.0 while growing at pH lower than 3.0” and must “keep pH gradients of considerable orders of magnitude” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Valdez-Nuñez 2024, doi:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 | Good evidence for external-vs-internal pH separation; mostly acidophile-focused. |
| F-type H+-transporting ATPase / F0F1-ATPase (GO:0046933) | consumes intracellular H+ to maintain | pH homeostasis (GO:0006885 approximate) | E. coli under acid stress | “under acid stress the ATPase hydrolyzes ATP to consume intracellular H+ to maintain homeostasis” (li2024responseofescherichia pages 2-4) | Li 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 | Strong but taxon-specific wording from review; curate as conserved mechanism with E. coli evidence. |
| F0F1-ATPase (GO:0046933) | enables | ATP synthesis from PMF (GO:0015986) | general bacterial homeostasis | “F0F1-ATP synthase typically uses 3–5 protons per ATP, linking PMF to ATP synthesis and pH homeostasis” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | Broad energetic link; supports physical mechanism rather than pH-limit phenotype directly. |
| Na+/H+ antiporter activity (GO:0015385) | regulates | internal pH / PMF (label-only candidate) | general bacteria; alkaliphiles | “Main regulators of internal pH/PMF include Na+/H+ and K+/H+ antiporters” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | High-level review evidence; non-gene-specific. |
| K+/H+ antiporter activity (label-only candidate) | regulates | internal pH / PMF (label-only candidate) | general bacteria; alkaliphiles | “Main regulators of internal pH/PMF include Na+/H+ and K+/H+ antiporters” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | High-level review evidence; non-gene-specific. |
| Mrp/Mnh/Pha-family Na+/H+ antiporters (label-only candidates; e.g., MrpF, MnhG, PhaGF) | are associated with | higher-pH preference (METPO:1000531 child candidate) | comparative genomics / biogeography | “Genes linked to higher-pH preference include Na+/H+ antiporters (PhaGF, MnhG, MrpF, YufB)” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | Correlational genomic association, not direct causal proof; curate as uncertain. |
| amino-acid decarboxylase + antiporter systems (label-only candidate) | consume | intracellular H+ (CHEBI:15378) | acid stress | “decarboxylation reaction consumes a proton, raising internal pH” and “the equivalent of 1 proton is pumped per molecule decarboxylated” (poolman2023physicochemicalhomeostasisin pages 2-4) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | Strong mechanistic edge; broad across amino-acid decarboxylase systems. |
| GadA/GadB glutamate decarboxylases (label-only; E. coli proteins) | convert | glutamate (CHEBI:29985) to GABA (CHEBI:16865) + CO2 (CHEBI:16526) while consuming H+ (CHEBI:15378) | E. coli AR2 at pH ~2–3 | “GadA/GadB decarboxylate intracellular glutamate to GABA + CO2, consuming H+” (li2024responseofescherichia pages 2-4) | Li 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 | Strong E. coli-specific mechanism; useful canonical acid-resistance edge. |
| GadC glutamate/GABA antiporter (label-only candidate) | sustains | glutamate-dependent acid resistance (label-only candidate) | E. coli AR2 | “GadC antiporter exports GABA in exchange for external glutamate, sustaining the cycle” (li2024responseofescherichia pages 2-4) | Li 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 | Strong, but transporter identity not grounded here to stable external ID. |
| gadA/gadB/gadC loss of function (label-only genotype node) | impairs | survival at very low pH (METPO:1000531 low-end limit candidate) | E. coli at pH ~2–3 | “Deletion of gadA/gadB/gadC impairs survival at pH ~2–3” (li2024responseofescherichia pages 2-4) | Li 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 | Strong phenotype association but assay-specific and E. coli-specific. |
| urease / urea transporter genes (e.g., UreE_C, ureide permeases) | produce | basic compounds / ammonia buffering capacity (CHEBI:16134) | low-pH preference in comparative genomics | “production of basic compounds (urease and urea transporters)” and genes linked to low-pH preference include “ureide_permeases and UreE_C” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | Correlational genomics; plausible mechanism but not experimentally resolved in this paper. |
| glutaminase YbaS (label-only candidate) | releases | ammonia (CHEBI:16134) | E. coli; ambient pH below 6.0 | “Glutaminase YbaS converts glutamine to glutamate and releases ammonia (ambient pH below 6.0), further neutralizing intracellular protons” (li2024responseofescherichia pages 2-4) | Li 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 | Strong E. coli-specific acid-response edge. |
| saturated membrane fatty acids (CHEBI:26666 approximate) | reduce | proton permeability of cytoplasmic membrane (label-only candidate) | acidophilic methanotrophs / acid adaptation | “cytoplasmic membranes with saturated fatty acids are formed” to stop protons entering; also “reduce proton permeability” (yao2023howmethanotrophsrespond pages 5-7) | Yao 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | Broad review synthesis; taxon examples from methanotrophs. |
| membrane lipid remodeling (unsaturated→saturated FA conversion) (label-only candidate) | limits | proton diffusion into cell (label-only candidate) | activated-sludge biofilm under acidic conditions | “conversion of unsaturated to saturated fatty acids” to limit proton diffusion (jiang2024exogenousputrescineplays pages 1-2) | Jiang 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Mechanistic but community-level/biofilm context; no specific genes in provided excerpt. |
| S-layer glycoproteins / secondary cell wall polymers (label-only candidate) | increase | negative surface charge that attracts external protons (label-only candidate) | alkaliphilic methanotrophs | “Alkaline adaptation includes development of S-layer glycoproteins/SCWPs that increase net negative surface charge to attract external protons” (yao2023howmethanotrophsrespond pages 5-7) | Yao 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | Good mechanistic edge for high-pH adaptation; review-level. |
| compatible-solute uptake / glycine betaine accumulation via OpuA (label-only candidate; glycine betaine CHEBI:17750) | contributes to | physicochemical regulation supporting pH homeostasis (label-only candidate) | general bacterial homeostasis | “compatible-solute uptake (e.g., OpuA-mediated glycine betaine accumulation) as part of osmotic/physicochemical regulation” (poolman2023physicochemicalhomeostasisin pages 2-4) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | Indirect link to pH phenotype; support is broader physicochemical homeostasis, so curate cautiously. |
| cytoplasmic buffering by phosphate pools (CHEBI:26078 approximate) | stabilizes | internal pH (label-only candidate) | general bacteria | “Cytoplasmic buffering is important” and L. lactis has “∼100 mM organic/inorganic phosphates” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | Good mechanistic support for buffering node; not a dedicated pH-limit determinant alone. |
| Pal/Rim pH-sensing pathway (label-only candidate; components Rim21/PalH, Rim8/PalF, Rim20/PalA, Rim13/PalB, Rim23/PalC, Rim9/PalI) | proteolytically activates | PacC transcription factor (label-only candidate) | alkaliphilic/alkali-tolerant fungi under alkaline pH | “pH is regulated by a signal transduction pathway that leads to the proteolytic activation of ... PacC” (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7) | Fernández-López 2023, doi:10.3390/jof9060652, https://doi.org/10.3390/jof9060652 | Strong fungal-specific regulatory edge; not broadly transferable to bacteria. |
| PacC transcription factor (label-only candidate) | activates/represses | alkaline-expressed genes / acid-expressed genes (label-only candidates) | fungal alkaline response | PacC27 “inhibits acid-expressed genes while activating alkaline-expressed genes” (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7) | Fernández-López 2023, doi:10.3390/jof9060652, https://doi.org/10.3390/jof9060652 | Strong but fungal-specific; likely out-of-scope if TraitMech is bacteria-only. |
| potassium uptake transporters / symporters-antiporters (label-only candidates) | discharge | excess intracellular protons (CHEBI:15378) | acidophilic methanotrophs | “using potassium uptake transporters and symporters/antiporters to discharge excess intracellular protons” (yao2023howmethanotrophsrespond pages 5-7) | Yao 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | Useful broad edge; review-level and taxon-specific examples. |
| cultivation method bias (label-only assay factor) | underestimates recovery of | alkaliphile diversity / pH phenotype distribution (label-only candidate) | high-pH sediment metagenomes pH 9.16–10.16 | “Approximately 80% ... not recovery by cultivable methods” in sediments at “pH 9.16–10.16” (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7) | Fernández-López 2023, doi:10.3390/jof9060652, https://doi.org/10.3390/jof9060652 | Important assay-bias edge; should be curated as evidence-quality/context factor, not biology. |
| biogeographic genomic signatures (label-only assay/analysis factor) | predict | bacterial pH preference (METPO:1000531 proxy) | soil and freshwater datasets; 1470 samples | authors “developed and validated a machine learning model to estimate bacterial pH preferences from genomic information alone” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | Predictive association, not mechanistic causal edge; useful as evidence framework, uncertain for direct TraitMech curation. |


*Table: This table compiles evidence-backed candidate causal edges relevant to the microbial trait 'pH phenotype with numerical limits' (METPO:1000531). It emphasizes mechanisms that connect external pH to intracellular pH homeostasis, membrane energetics, and assay-dependent interpretation, while flagging taxon-specific or correlational claims for cautious curation.*

## Quantitative examples of pH numerical limits (recent sources)

### Category-level tendencies (for annotation, not as strict cutoffs)
- Acidophiles: “generally grow optimally at pH below 3.” (rekadwad2023extremophilesthespecies pages 8-10)
- Alkaliphiles: “require pH 9 or above for growth.” (rekadwad2023extremophilesthespecies pages 8-10)

### Strain-level pH optima and ranges (example dataset)

Yao et al. (2023) provide strain-level pH optima/ranges for methanotrophs (Table 1) and a schematic of acidophilic vs alkaliphilic pH homeostasis (Figure 2). These are suitable sources to seed curated numeric pH limits for specific taxa/isolates if the curation scope includes methanotrophs. (yao2023howmethanotrophsrespond media 85fb8f31, yao2023howmethanotrophsrespond media e927d25f, yao2023howmethanotrophsrespond media ab5afa78)

## Warnings / claims not ready for TraitMech curation

1. **Correlation-only gene→pH preference edges:** Genomic associations (e.g., antiporters, urease genes) from Ramoneda et al. (2023) are powerful for hypothesis generation but should be marked **uncertain** unless a causal perturbation or mechanistic experiment is available. (ramoneda2023buildingagenomebased pages 3-5)
2. **Cross-domain mechanism transfer:** Fungal Pal/Rim→PacC signaling is mechanistically strong in fungi but may be out-of-scope for bacterial TraitMech graphs; curate only if the trait is defined across microbes broadly. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7)
3. **Environment-inferred ranges vs growth ranges:** Environmental pH ranges where taxa are detected (metagenomes, enrichments) are not necessarily the organism’s growth range; capture as *evidence context* and prefer growth curves in defined media for numerical limits. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7, ramoneda2023buildingagenomebased pages 3-5)

## DOI-first bibliography (with dates and URLs)

- Poolman B. **Physicochemical homeostasis in bacteria.** *FEMS Microbiology Reviews* (Jun 2023). https://doi.org/10.1093/femsre/fuad033 (doi:10.1093/femsre/fuad033). (poolman2023physicochemicalhomeostasisin pages 1-2, poolman2023physicochemicalhomeostasisin pages 2-4)
- Ramoneda J, et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances* (Apr 2023). https://doi.org/10.1126/sciadv.adf8998 (doi:10.1126/sciadv.adf8998). (ramoneda2023buildingagenomebased pages 3-5)
- Yao X, Wang J, Hu B. **How methanotrophs respond to pH: A review of ecophysiology.** *Frontiers in Microbiology* (Jan 2023). https://doi.org/10.3389/fmicb.2022.1034164 (doi:10.3389/fmicb.2022.1034164). (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond media 85fb8f31, yao2023howmethanotrophsrespond media e927d25f, yao2023howmethanotrophsrespond media ab5afa78)
- Rekadwad BN, et al. **Extremophiles: the species that evolve and survive under hostile conditions.** *3 Biotech* (Aug 2023). https://doi.org/10.1007/s13205-023-03733-6 (doi:10.1007/s13205-023-03733-6). (rekadwad2023extremophilesthespecies pages 8-10)
- Fernández-López M.G., et al. **Alkaliphilic/Alkali-Tolerant Fungi: Molecular, Biochemical, and Biotechnological Aspects.** *Journal of Fungi* (Jun 2023). https://doi.org/10.3390/jof9060652 (doi:10.3390/jof9060652). (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7)
- Li Z, Huang Z, Gu P. **Response of Escherichia coli to Acid Stress: Mechanisms and Applications—A Narrative Review.** *Microorganisms* (Aug 2024). https://doi.org/10.3390/microorganisms12091774 (doi:10.3390/microorganisms12091774). (li2024responseofescherichia pages 2-4, li2024responseofescherichia pages 1-2)
- Qin J, et al. **Characterization of Mild Acid Stress Response in an Engineered Acid-Tolerant Escherichia coli Strain.** *Microorganisms* (Jul 2024). https://doi.org/10.3390/microorganisms12081565 (doi:10.3390/microorganisms12081565). (qin2024characterizationofmild pages 1-2)
- Jiang G, et al. **Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.** *Applied and Environmental Microbiology* (Jul 2024). https://doi.org/10.1128/aem.00569-24 (doi:10.1128/aem.00569-24). (jiang2024exogenousputrescineplays pages 1-2)
- Valdez-Nuñez LF, et al. **Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.** *Environmental Microbiology Reports* (Oct 2024). https://doi.org/10.1111/1758-2229.70019 (doi:10.1111/1758-2229.70019). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- Atasoy M, et al. **Exploitation of microbial activities at low pH to enhance planetary health.** *FEMS Microbiology Reviews* (Nov 2024). https://doi.org/10.1093/femsre/fuad062 (doi:10.1093/femsre/fuad062). (atasoy2024exploitationofmicrobial pages 10-11, atasoy2024exploitationofmicrobial pages 5-6, atasoy2024exploitationofmicrobial pages 2-3)


References

1. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

2. (li2024responseofescherichia pages 1-2): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

3. (rekadwad2023extremophilesthespecies pages 8-10): Bhagwan Narayan Rekadwad, Wen-Jun Li, Juan M. Gonzalez, Rekha Punchappady Devasya, Arun Ananthapadmanabha Bhagwath, Ruchi Urana, and Khalid Parwez. Extremophiles: the species that evolve and survive under hostile conditions. 3 Biotech, Aug 2023. URL: https://doi.org/10.1007/s13205-023-03733-6, doi:10.1007/s13205-023-03733-6. This article has 49 citations and is from a peer-reviewed journal.

4. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7): Maikel Gilberto Fernández-López, Ramón Alberto Batista-García, and Elva Teresa Aréchiga-Carvajal. Alkaliphilic/alkali-tolerant fungi: molecular, biochemical, and biotechnological aspects. Journal of Fungi, 9:652, Jun 2023. URL: https://doi.org/10.3390/jof9060652, doi:10.3390/jof9060652. This article has 35 citations.

5. (poolman2023physicochemicalhomeostasisin pages 2-4): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

6. (li2024responseofescherichia pages 2-4): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

7. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

8. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

9. (qin2024characterizationofmild pages 1-2): Jingliang Qin, Han Guo, Xiaoxue Wu, Shuai Ma, Xin Zhang, Xiaofeng Yang, Bin Liu, Lu Feng, Huanhuan Liu, and Di Huang. Characterization of mild acid stress response in an engineered acid-tolerant escherichia coli strain. Microorganisms, 12:1565, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081565, doi:10.3390/microorganisms12081565. This article has 2 citations.

10. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

11. (atasoy2024exploitationofmicrobial pages 10-11): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

12. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

13. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

14. (yao2023howmethanotrophsrespond media 85fb8f31): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

15. (yao2023howmethanotrophsrespond media e927d25f): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

16. (yao2023howmethanotrophsrespond media ab5afa78): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

17. (atasoy2024exploitationofmicrobial pages 5-6): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

18. (atasoy2024exploitationofmicrobial pages 2-3): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.