---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:12:47.562126'
end_time: '2026-06-18T05:26:34.157165'
duration_seconds: 826.6
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: metabolism
  trait_identifier: METPO:1000060
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: metabolism
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biological process that maintains life in an organism.
  parent_traits: METPO:1000630
  synonyms: ''
  evidence_summary: 'DOI:10.1126/science.1238842: energy and microbial life (Microbial-energetics
    review supports metabolism as the energy and material-flow process maintaining
    microbial life.) | DOI:10.1146/annurev.biochem.71.110601.135503: ATP synthesis
    (ATP-energetics review supports energy conservation as the central output of catabolic
    metabolism.)'
  causal_graph_summary: 'metabolism_substrate_to_growth: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** metabolism
- **METPO identifier:** METPO:1000060
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biological process that maintains life in an organism.
- **Parent traits:** METPO:1000630
- **Synonyms:** 
- **Existing evidence:** DOI:10.1126/science.1238842: energy and microbial life (Microbial-energetics review supports metabolism as the energy and material-flow process maintaining microbial life.) | DOI:10.1146/annurev.biochem.71.110601.135503: ATP synthesis (ATP-energetics review supports energy conservation as the central output of catabolic metabolism.)
- **Existing causal graph summary:** metabolism_substrate_to_growth: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/metabolism.yaml`.

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
- **Trait label:** metabolism
- **METPO identifier:** METPO:1000060
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biological process that maintains life in an organism.
- **Parent traits:** METPO:1000630
- **Synonyms:** 
- **Existing evidence:** DOI:10.1126/science.1238842: energy and microbial life (Microbial-energetics review supports metabolism as the energy and material-flow process maintaining microbial life.) | DOI:10.1146/annurev.biochem.71.110601.135503: ATP synthesis (ATP-energetics review supports energy conservation as the central output of catabolic metabolism.)
- **Existing causal graph summary:** metabolism_substrate_to_growth: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/metabolism.yaml`.

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


## Microbial trait causal graph report: **Metabolism** (METPO:1000060)

### 1) Scope summary (TraitMech curation)

**Trait definition in practice.** For TraitMech curation, *microbial metabolism* can be operationalized as the **ensemble of biochemical transformations and energy-conservation processes that (i) harvest free energy from electron donors/substrates and terminal electron acceptors, (ii) generate energy currency (ATP and ion gradients), and (iii) supply reducing power and precursors for biomass synthesis and maintenance**. A mechanistic core that is broadly conserved is that **electron flow (e.g., from NADH/FADH2/ferredoxin) can be coupled to ion-gradient formation (proton motive force) and ATP synthesis by ATP synthase** (williams2024mappingthemetabolic pages 17-22, williams2024mappingthemetabolic pages 22-26, althaher2023anoverviewof pages 1-2).

**Boundary with adjacent traits.**
- *Metabolism vs growth rate:* Growth rate is a downstream emergent property of metabolic fluxes and allocation; trait-based energy-budget modeling explicitly frames **growth rate as “power”** and distinguishes it from **growth efficiency (yield)** (marschmann2024predictionsofrhizosphere pages 1-2). 
- *Metabolism vs carbon use efficiency (CUE):* CUE is a coarse *summary* metric for how carbon uptake is partitioned between biomass formation and losses (e.g., respiration/exudation). Recent synthesis emphasizes that **models often compress diverse metabolic pathways into CUE**, and that CUE declines when more carbon is diverted to respiration to meet energy demands (maintenance, uptake, enzyme production) (he2024emergingmultiscaleinsights pages 1-2). Thus, CUE is best treated as an *output* of metabolism rather than the metabolism trait itself.
- *Metabolism vs respiration:* Respiration is one energy-conserving mode within metabolism. Metabolism also includes fermentation, chemolithotrophy, and electron-bifurcation-based strategies that are prominent in anaerobes/archaea (williams2024mappingthemetabolic pages 17-22, jin2023syntrophicpropionateoxidation pages 1-2).

### 2) Key concepts and definitions (current understanding)

#### Core energy conservation mechanisms
Recent mechanistic synthesis highlights **three overarching methods of microbial energy conservation**: 
1) **Substrate-level phosphorylation** (direct ATP formation in a small set of reactions), 
2) **Electron-transport-linked chemiosmotic phosphorylation** (ion-gradient-driven ATP synthase), and 
3) **Electron bifurcation** (coupling exergonic to endergonic electron transfers) (williams2024mappingthemetabolic pages 17-22).

**Chemiosmosis / proton motive force (pmf).** In chemiosmotic coupling, reduced cofactors are oxidized by membrane systems to generate an ion gradient; **ATP synthase converts pmf into ATP**, with reported stoichiometry on the order of **~3–4 protons per ATP** in the cited synthesis (williams2024mappingthemetabolic pages 22-26). A general ATP synthase review summarizes this as ATP synthases converting ADP + Pi to ATP using an **electrochemical proton motive force generated by electron transfer through respiratory chains** (althaher2023anoverviewof pages 1-2).

**Thermodynamic context.** The cited 2024 synthesis provides quantitative anchors for ATP bioenergetics and redox thermodynamics, including that ATP phosphorylation free energy is on the order of **~31 kJ/mol under standard conditions** and that oxygen’s high redox potential makes it an effective terminal electron acceptor (**E° ~ +800 mV**) (williams2024mappingthemetabolic pages 17-22). It also reports example redox free energies for alternative acceptors/donors and emphasizes that carrier redox potentials (e.g., ferredoxin) shape feasibility and thus growth potential (williams2024mappingthemetabolic pages 22-26).

**Syntrophy at energetic limits.** In anoxic environments, syntrophic propionate oxidation is presented as a rate-limiting process near thermodynamic limits; the review cites a **minimum energy threshold for ATP synthesis of ~15–25 kJ** and reports that propionate can contribute **up to 15–30%** of methane production in anoxic systems (jin2023syntrophicpropionateoxidation pages 1-2). These values are useful for representing “metabolism at the limit” subgraphs.

### 3) Recent developments and latest research (prioritizing 2023–2024)

#### 3.1 Mechanistic bioenergetics emphasizing “limits of life”
A 2024 study/review on energy conservation at the limits of life reiterates the centrality of **pmf-driven ATP synthase, redox carrier constraints, and electron bifurcation** for anaerobic/archaeal energy conservation (williams2024mappingthemetabolic pages 17-22, williams2024mappingthemetabolic pages 22-26). It also demonstrates that **electron flux can be re-routed** in an archaeal model system (Thermococcus kodakarensis) by protein-interaction changes and engineered fusions, affecting reductive sinks (e.g., hydrogen generation) with limited growth defects—supporting the notion that *network wiring* can causally change metabolic outputs (williams2024mappingthemetabolic pages 40-43).

#### 3.2 Trait-based ecology linking genomes, energy budgets, and metabolic trade-offs
A 2024 Nature Microbiology study (DEBmicroTrait) integrates genome-inferred traits and substrate uptake kinetics into a dynamic energy budget model to predict emergent strategies and explicitly highlights **resource-dependent trade-offs between microbial growth rate and efficiency** (marschmann2024predictionsofrhizosphere pages 1-2). This work provides a conceptually useful bridge from mechanistic metabolism to field-observed traits, particularly for soil/rhizosphere contexts.

#### 3.3 Genome-scale metabolic models (GEMs) and community GEMs as operational metabolism representations
A 2024 review summarizes how GEMs are used to study microbial metabolic adaptation to environmental and genetic perturbations, integrating multi-omics to create context-specific models and applying them to stress responses and pathogenesis/virulence contexts (carter2024applicationsofgenomescale pages 1-1, carter2024applicationsofgenomescale pages 1-2, carter2024applicationsofgenomescale pages 6-7). In parallel, community GEMs (cGEMs) are proposed for quantifying ecosystem services, bioremediation strategies, and improving climate/biogeochemical models (robainaestevez2024applicationsofmarine pages 1-2).

#### 3.4 Curated pathway/module resources expanding “metabolic potential” annotation
Enteropathway (2024) provides a manually curated database for gut microbiota metabolism, integrating **~3,269 compounds, 3,677 reactions, and 876 modules**, with **~698 modules** reported as unique relative to other databases in the excerpted text (shiroma2024enteropathwaythemetabolic pages 1-2). For TraitMech, this supports node discovery and module-level mechanistic anchors (pathway → reaction → metabolite).

### 4) Current applications and real-world implementations

1. **Industrial strain design / fermentation trait prediction via GEMs.** A 2024 mSystems study built a curated Lactobacillaceae pan-reactome and generated **2,446 strain-specific GEMs** across **26 species**, explicitly positioning GEMs as tools to predict growth conditions, essential media components, fermentation capabilities, and strain-improvement targets relevant to commercial products (ardalani2024pangenomereconstructionof pages 1-3).
2. **Microbiome function inference and metabolite prediction from metagenomes.** A 2024 mSystems study compares MAG-guided vs reference-guided community metabolic modeling and validates predicted metabolites using untargeted metabolomics in human samples, highlighting both overlap and approach-specific predictions and cautioning interpretation (majzoub2024refiningmicrobialcommunity pages 1-2).
3. **Marine ecosystem modeling and bioremediation planning.** A 2024 review argues that cGEMs combined with meta-omics and environmental data can guide **bioremediation** and improve ecosystem-service quantification and climate/biogeochemical models (robainaestevez2024applicationsofmarine pages 1-2).
4. **Community interaction inference (cross-feeding).** Genome-scale community modeling in marine bacterioplankton predicts conserved cross-feeding, including **amino acids and group B vitamins** (giordano2024genomescalecommunitymodelling media e09c444a), supporting causal subgraphs where auxotrophy → metabolite exchange → community assembly/function.

### 5) Relevant recent statistics and data (examples suitable for curation notes)

**Bioenergetic / thermodynamic quantitative anchors**
- ATP synthesis coupling: **~3–4 protons per ATP** in the cited synthesis (williams2024mappingthemetabolic pages 22-26).
- Oxygen redox potential: **E° ~ +800 mV** as a high-potential terminal electron acceptor (williams2024mappingthemetabolic pages 17-22).
- Syntrophic energetic constraints: **minimum energy for ATP synthesis ~15–25 kJ** and propionate contribution **up to 15–30%** of methane in anoxic systems; **only ~10 species** reported as syntrophic propionate oxidizers (jin2023syntrophicpropionateoxidation pages 1-2).

**Knowledgebase / model resource quantitative anchors**
- Enteropathway database scale: **~3,269 compounds, 3,677 reactions, 876 modules**; **~698 modules** unique in the excerpt (shiroma2024enteropathwaythemetabolic pages 1-2).
- Lactobacillaceae metabolism modeling: **75,299 gene–protein–reaction associations; 2,446 GEMs; 26 species** (ardalani2024pangenomereconstructionof pages 1-3).

### 6) Candidate nodes for `metabolism.yaml` (grouped by type)

#### 6.1 Biological processes / metabolic modules (candidate nodes)
- ATP biosynthesis / energy currency: ATP biosynthetic process (GO:0006754) (williams2024mappingthemetabolic pages 22-26)
- Proton motive force generation and utilization: proton motive force (GO:0015992) (williams2024mappingthemetabolic pages 22-26)
- Respiratory electron transport chain (GO:0022904) (althaher2023anoverviewof pages 1-2)
- Electron bifurcation (label-only; needs ontology mapping) (williams2024mappingthemetabolic pages 17-22)
- Substrate-level phosphorylation (label-only) (williams2024mappingthemetabolic pages 17-22)
- Syntrophic propionate oxidation (label-only) (jin2023syntrophicpropionateoxidation pages 1-2)

#### 6.2 Enzymes / complexes / functional systems
- ATP synthase complex (GO:0046933) (williams2024mappingthemetabolic pages 22-26, althaher2023anoverviewof pages 1-2)
- Membrane proton pumps / hydrogenases (label-only in provided evidence) (williams2024mappingthemetabolic pages 17-22)

#### 6.3 Chemicals / metabolites / carriers
- ATP (CHEBI:15422), ADP (CHEBI:16761), phosphate (CHEBI:43474) (althaher2023anoverviewof pages 1-2)
- Oxygen (CHEBI:15379), H+ (CHEBI:15378) (williams2024mappingthemetabolic pages 17-22, williams2024mappingthemetabolic pages 22-26)
- NADH, FADH2 (CHEBI identifiers referenced conceptually; specific CHEBI IDs not provided in evidence) (williams2024mappingthemetabolic pages 17-22)
- Formate (CHEBI:15740), hydrogen (CHEBI:18276) (jin2023syntrophicpropionateoxidation pages 1-2)
- Propionate (CHEBI:32816), methane (CHEBI:16183) (jin2023syntrophicpropionateoxidation pages 1-2)
- Thiamine / vitamin B1 (CHEBI:26948) and amino acids (CHEBI:33709) as cross-fed metabolites (giordano2024genomescalecommunitymodelling media e09c444a)

#### 6.4 Environmental / experimental factors
- Anoxic environments (ENVO label candidate) (jin2023syntrophicpropionateoxidation pages 1-2)
- Rhizosphere (ENVO:00005801) (marschmann2024predictionsofrhizosphere pages 1-2)
- Resource availability: organic carbon input, substrate concentration, and substrate free energy content (label-only) (marschmann2024predictionsofrhizosphere pages 2-3, marschmann2024predictionsofrhizosphere pages 1-2)

#### 6.5 Assay/modeling entities (should be separated from biology nodes)
- Genome-scale metabolic model (GEM) (label-only) (carter2024applicationsofgenomescale pages 1-1)
- Community GEM (cGEM) (label-only) (robainaestevez2024applicationsofmarine pages 1-2)
- Metagenome-assembled genome (MAG) (label-only) (majzoub2024refiningmicrobialcommunity pages 1-2)
- Pathway/module database objects: Enteropathway modules (label-only) (shiroma2024enteropathwaythemetabolic pages 1-2)

### 7) Evidence-backed candidate causal edges (triples)

The table below is designed for direct conversion into `metabolism.yaml` candidate edges (with uncertainty flags and grounding).

| Edge (triple) | Evidence snippet (quote) | Source (citation id) | DOI/URL | Pub year/date | Notes/uncertainty | Suggested ontology grounding (GO/CHEBI/ENVO/EC/etc) |
|---|---|---|---|---|---|---|
| reduced cofactors / electron transport chain -> generates -> proton motive force | "reduced cofactors (e.g., NADH, FADH2, reduced ferredoxin) are oxidized at membrane proton pumps or hydrogenases to generate a proton/ion gradient" (williams2024mappingthemetabolic pages 17-22) | (williams2024mappingthemetabolic pages 17-22) | DOI not available in evidence | 2024 | Broad mechanistic edge; applies across many bacteria/archaea; exact pump identity taxon-specific | subject: CHEBI:NADH, CHEBI:FADH2, ferredoxin(label); predicate: generates; object: proton motive force GO:0015992 |
| proton motive force -> drives -> ATP synthase-mediated ATP production | "Upon binding 3-4 protons, the membrane-bound ATP synthase converts the potential energy...by phosphorylating ADP to ATP" (williams2024mappingthemetabolic pages 22-26) | (williams2024mappingthemetabolic pages 22-26) | DOI not available in evidence | 2024 | Strong core bioenergetic edge; proton stoichiometry varies by enzyme/taxon | subject: GO:0015992 proton motive force; object: GO:0006754 ATP biosynthetic process; protein complex: ATP synthase GO:0046933 |
| ATP synthase -> uses -> electrochemical proton motive force | "They convert ADP + Pi to ATP using an electrochemical proton motive force generated by electron transfer through respiratory chains" (althaher2023anoverviewof pages 1-2) | (althaher2023anoverviewof pages 1-2) | https://doi.org/10.1016/j.heliyon.2023.e22459 | 2023-11 | General across bacterial cytoplasmic membranes and other bioenergetic membranes | ATP synthase GO:0046933; proton motive force GO:0015992; ADP CHEBI:16761; phosphate CHEBI:43474; ATP CHEBI:15422 |
| electron transfer through respiratory chains -> generates -> proton gradient | "proton movement from the matrix to the cristae lumen creates the gradient that powers ATP synthesis" (althaher2023anoverviewof pages 1-2) | (althaher2023anoverviewof pages 1-2) | https://doi.org/10.1016/j.heliyon.2023.e22459 | 2023-11 | Source is broad ATP synthase review with mixed systems; microbial applicability inferred but standard | respiratory electron transport chain GO:0022904; proton gradient GO:1990815 |
| substrate-level phosphorylation -> produces -> ATP | "only three overarching methods of energy conservation have been defined: substrate level" and "Less than ten biological reactions" directly yield ATP (williams2024mappingthemetabolic pages 17-22) | (williams2024mappingthemetabolic pages 17-22) | DOI not available in evidence | 2024 | High-level mechanism; edge is strong but not tied to a specific reaction in provided evidence | GO:0006757 ATP generation from ADP; substrate-level phosphorylation label-only candidate |
| electron bifurcation -> couples -> endergonic and exergonic electron transfer | "electron bifurcation wherein an endergonic electron transfer is coupled to an exergonic transfer" (williams2024mappingthemetabolic pages 17-22) | (williams2024mappingthemetabolic pages 17-22) | DOI not available in evidence | 2024 | Strong mechanism but often enzyme-system specific; curate as process-level node | electron bifurcation label-only candidate; flavin-dependent oxidoreductase activity GO:0010181 candidate |
| oxygen -> serves as -> high-potential terminal electron acceptor | "oxygen has a high reduction potential (\"E˚ = ~ +800 mV\") making it an effective terminal electron acceptor" (williams2024mappingthemetabolic pages 17-22) | (williams2024mappingthemetabolic pages 17-22) | DOI not available in evidence | 2024 | General aerobic-respiration edge; not universal to all microbes | oxygen CHEBI:15379; terminal electron acceptor label; aerobic respiration GO:0009060 |
| proton / H+ -> can serve as -> terminal electron acceptor in some metabolisms | "while protons (E˚ ~ -414 mV) ... set limits on feasible redox reactions" and discussion of protons as terminal acceptor context (williams2024mappingthemetabolic pages 22-26) | (williams2024mappingthemetabolic pages 22-26) | DOI not available in evidence | 2024 | Weaker, context-dependent; applicable to hydrogenogenic systems; mark uncertain | CHEBI:15378 hydron; hydrogen metabolism GO:0006073 candidate |
| low environmental H2/formate concentrations -> enable -> syntrophic propionate oxidation | "Syntrophy is defined as a tightly coupled, energetically limited mutualism between H2/formate-producing bacteria and H2/formate-consuming methanogens that must keep exchanged intermediates at very low concentrations" (jin2023syntrophicpropionateoxidation pages 1-2) | (jin2023syntrophicpropionateoxidation pages 1-2) | https://doi.org/10.1128/aem.00384-23 | 2023-05 | Strong but specific to syntrophic anaerobic systems | hydrogen CHEBI:18276; formate CHEBI:15740; syntrophy label; ENVO:01000179 anoxic environment candidate |
| propionate oxidation -> contributes to -> methane production in anoxic systems | "Propionate can contribute substantially to methane production (up to 15–30% of total CH4 in anoxic systems)" (jin2023syntrophicpropionateoxidation pages 1-2) | (jin2023syntrophicpropionateoxidation pages 1-2) | https://doi.org/10.1128/aem.00384-23 | 2023-05 | Ecosystem-level edge rather than single-cell trait; still relevant environmental linkage | propionate CHEBI:32816; methane CHEBI:16183; methanogenesis GO:0015948; ENVO:01000179 anoxic environment candidate |
| flavin-based electron bifurcation/confurcation systems -> help enable -> low-potential H2/formate formation | "The flavin-based electron bifurcation/confurcation (FBEB/C) systems have been proposed to help solve the thermodynamic dilemma during the formation of the low-potential products H2 and formate" (jin2023syntrophicpropionateoxidation pages 1-2) | (jin2023syntrophicpropionateoxidation pages 1-2) | https://doi.org/10.1128/aem.00384-23 | 2023-05 | Proposed mechanism in SPOB review; useful but should be marked uncertain/proposed | hydrogen CHEBI:18276; formate CHEBI:15740; electron bifurcation label-only candidate |
| higher respiration costs / energy demand -> decreases -> carbon use efficiency | "CUE declines when more carbon is diverted to respiration to generate energy (for substrate uptake, maintenance, enzyme production) or to exudation" (he2024emergingmultiscaleinsights pages 1-2) | (he2024emergingmultiscaleinsights pages 1-2) | https://doi.org/10.1038/s41467-024-52160-5 | 2024-09 | Strong conceptual edge linking metabolism to yield; trait-adjacent rather than core pathway | respiration GO:0045333; carbon use efficiency label-only candidate; maintenance process label |
| substrate complexity / need for enzymatic degradation -> increases -> energetic cost of metabolism | "the energy required depends on whether compounds are directly taken up or need enzymatic degradation" (he2024emergingmultiscaleinsights pages 1-2) | (he2024emergingmultiscaleinsights pages 1-2) | https://doi.org/10.1038/s41467-024-52160-5 | 2024-09 | Broad ecology/process edge; exact compounds not specified in excerpt | substrate label; extracellular enzyme activity GO:0003824 candidate; uptake GO:0006810 |
| resource availability and substrate free energy -> shape -> growth rate vs efficiency trade-offs | "resource-dependent trade-offs between microbial growth rate and efficiency" and "growth efficiency...varies with resource concentration and the free energy content of compounds" (marschmann2024predictionsofrhizosphere pages 1-2, marschmann2024predictionsofrhizosphere pages 2-3) | (marschmann2024predictionsofrhizosphere pages 1-2, marschmann2024predictionsofrhizosphere pages 2-3) | https://doi.org/10.1038/s41564-023-01582-w | 2024-02 | Strong systems-level trait edge; not a single biochemical reaction | growth rate label; efficiency/CUE label; resource availability ENVO label; Gibbs free energy label |
| organic carbon inputs and energy availability -> limit -> rhizosphere bacterial metabolism | "bacteria in the rhizosphere are primarily limited by organic C inputs and energy availability" (marschmann2024predictionsofrhizosphere pages 1-2) | (marschmann2024predictionsofrhizosphere pages 1-2) | https://doi.org/10.1038/s41564-023-01582-w | 2024-02 | Environment-specific (rhizosphere) but mechanistically useful | organic carbon label; ENVO:00005801 rhizosphere |
| genome-inferred metabolic potential -> constrains/predicts -> substrate utilization capacity | "Genomic data are used to infer 'metabolic potential to utilize organic acids'" and "assess functional potential—the capacity for organisms to perform" (marschmann2024predictionsofrhizosphere pages 1-2) | (marschmann2024predictionsofrhizosphere pages 1-2) | https://doi.org/10.1038/s41564-023-01582-w | 2024-02 | Inferred/model-based edge; useful for assay/omics interpretation, not direct physiology | metabolic potential label-only candidate; organic acid CHEBI:35366 |
| amino acid and B-vitamin cross-feeding -> supports -> microbial community interactions | "Figure 5 summarizes conserved metabolic cross-feedings (including amino acids and B vitamins) and community interactions" (giordano2024genomescalecommunitymodelling media e09c444a) | (giordano2024genomescalecommunitymodelling media e09c444a) | https://doi.org/10.1038/s41467-024-46374-w | 2024-03 | Image-context support only; metabolite identities partly specific (e.g., thiamin, L-arginine, L-glutamate) but mechanism is community-model inferred | amino acid CHEBI:33709; vitamin B/thiamine CHEBI:26948; cross-feeding label-only candidate |
| community GEMs + meta-omics/environmental data -> enable -> prediction of ecosystem functions/bioremediation | "three primary applications of cGEMs: quantifying marine ecosystem services, guiding bioremediation strategies for environmental challenges, and enhancing climate and biogeochemical models" (robainaestevez2024applicationsofmarine pages 1-2) | (robainaestevez2024applicationsofmarine pages 1-2) | https://doi.org/10.1371/journal.pstr.0000145 | 2024-11 | Implementation/application edge, not biological causation; do not curate as biological mechanism | community genome-scale metabolic model label; bioremediation ENVO/NCIT candidate |
| reference-guided community GEM input -> predicts -> more metabolites than MAG-guided approach in some sample types | "the reference-guided approach predicted more metabolites than the MAG-guided approach" (majzoub2024refiningmicrobialcommunity pages 1-2) | (majzoub2024refiningmicrobialcommunity pages 1-2) | https://doi.org/10.1128/msystems.00746-24 | 2024-09 | Method-comparison edge only; assay/computation-specific, not trait mechanism | reference-guided GEM label; MAG-guided GEM label; metabolite prediction label |
| Enteropathway manual curation -> expands -> known gut microbial metabolic modules | "integrates 3,121 compounds, 3,460 reactions, and 837 modules" and "757 modules...are new entries" (shiroma2024enteropathwaythemetabolic pages 1-2) | (shiroma2024enteropathwaythemetabolic pages 1-2) | https://doi.org/10.1093/bib/bbae419 | 2024-06 | Knowledgebase/resource edge only; useful for node discovery, not direct biology | pathway database label; compounds/reactions/modules label |
| curated Lactobacillaceae GEMs -> predict -> species-specific metabolic traits and fermentation capabilities | "2,446 genome-scale metabolic models" that "predict species-specific metabolic reactions... essential media components... and fermentation capabilities" (ardalani2024pangenomereconstructionof pages 1-3) | (ardalani2024pangenomereconstructionof pages 1-3) | https://doi.org/10.1128/msystems.00156-24 | 2024-07 | Computational prediction edge; useful for supporting downstream trait curation but not direct mechanistic physiology | GEM label; fermentation GO:0046358; Lactobacillaceae NCBITaxon:33958 |


*Table: This table lists candidate subject-predicate-object edges for a microbial metabolism causal graph, restricted to claims directly supported by the cited 2023-2024 evidence. It distinguishes core mechanistic edges from computational or ecosystem-level inferences and flags uncertainty where claims are taxon-, assay-, or model-specific.*

### 8) Expert synthesis / analysis (how to curate “metabolism” without overbreadth)

1. **Curate metabolism as a *mechanistic hub trait* anchored in energy conservation.** The strongest universally applicable subgraph is **electron carriers → pmf → ATP synthase → ATP**, plus **substrate-level phosphorylation → ATP**, with electron bifurcation as a conserved auxiliary mechanism (williams2024mappingthemetabolic pages 17-22, williams2024mappingthemetabolic pages 22-26, althaher2023anoverviewof pages 1-2). This aligns with using metabolism as the trait root, with multiple child graphs (aerobic respiration, anaerobic respiration, fermentation/syntrophy, phototrophy).
2. **Separate “metabolic potential” (genome-/model-inferred) from “metabolic activity” (assay-observed).** Genomic inference and GEM reconstructions are powerful but can inflate claims if curated as physiology; include them as *evidence types* or *supporting annotations*, not as direct biochemical causal edges unless experimentally validated (carter2024applicationsofgenomescale pages 1-1, majzoub2024refiningmicrobialcommunity pages 1-2, marschmann2024predictionsofrhizosphere pages 1-2).
3. **Use environment-specific modules to bound scope.** Syntrophy (propionate oxidation) and rhizosphere energy-budget constraints are mechanistically rich but context-specific; include as optional subgraphs with ENVO-conditioned edges (jin2023syntrophicpropionateoxidation pages 1-2, marschmann2024predictionsofrhizosphere pages 1-2).

### 9) Warnings / claims not ready for curation

- **Computation-only edges:** “cGEMs enable bioremediation planning” and “reference-guided predicts more metabolites” are methodological/application claims and should not be encoded as organismal metabolic mechanism edges (robainaestevez2024applicationsofmarine pages 1-2, majzoub2024refiningmicrobialcommunity pages 1-2).
- **Cross-feeding mechanism details:** The community cross-feeding figure supports cross-feeding as a modeled pattern, but **specific donor/recipient taxa and transport mechanisms** are not established in the provided excerpt; curate cross-feeding edges as **uncertain/model-inferred** unless backed by direct experiments (giordano2024genomescalecommunitymodelling media e09c444a).
- **Carrier/pump identity:** The synthesis references “membrane proton pumps or hydrogenases” broadly; specific complexes (Complex I/III/IV, Rnf, Ech, etc.) need additional taxon/pathway-specific sources before adding detailed edges (williams2024mappingthemetabolic pages 17-22).

---

## DOI-first bibliography (2023–2024 prioritized)

- Williams SA, Santangelo T, Hansen JC, Pilon M. *Mapping the metabolic protein interactome that supports energy conservation at the limits of life.* 2024. (DOI not available in retrieved text excerpt) (williams2024mappingthemetabolic pages 17-22, williams2024mappingthemetabolic pages 22-26, williams2024mappingthemetabolic pages 40-43)
- Marschmann GL et al. *Predictions of rhizosphere microbiome dynamics with a genome-informed and trait-based energy budget model.* **Nature Microbiology** (Feb 2024). DOI: **10.1038/s41564-023-01582-w**. https://doi.org/10.1038/s41564-023-01582-w (marschmann2024predictionsofrhizosphere pages 1-2)
- He X et al. *Emerging multiscale insights on microbial carbon use efficiency in the land carbon cycle.* **Nature Communications** (Sep 2024). DOI: **10.1038/s41467-024-52160-5**. https://doi.org/10.1038/s41467-024-52160-5 (he2024emergingmultiscaleinsights pages 1-2)
- Althaher AR, Alwahsh M. *An overview of ATP synthase, inhibitors, and their toxicity.* **Heliyon** (Nov 2023). DOI: **10.1016/j.heliyon.2023.e22459**. https://doi.org/10.1016/j.heliyon.2023.e22459 (althaher2023anoverviewof pages 1-2)
- Jin Y, Lu Y. *Syntrophic Propionate Oxidation: One of the Rate-Limiting Steps of Organic Matter Decomposition in Anoxic Environments.* **Applied and Environmental Microbiology** (May 2023). DOI: **10.1128/aem.00384-23**. https://doi.org/10.1128/aem.00384-23 (jin2023syntrophicpropionateoxidation pages 1-2)
- Carter EL, Constantinidou C, Alam MT. *Applications of genome-scale metabolic models to investigate microbial metabolic adaptations in response to genetic or environmental perturbations.* **Briefings in Bioinformatics** (Nov 2024). DOI: **10.1093/bib/bbad439**. https://doi.org/10.1093/bib/bbad439 (carter2024applicationsofgenomescale pages 1-1, carter2024applicationsofgenomescale pages 1-2, carter2024applicationsofgenomescale pages 6-7)
- Robaina-Estévez S, Gutiérrez J. *Applications of marine microbial community models in the nature-based economy.* **PLOS Sustainability and Transformation** (Nov 2024). DOI: **10.1371/journal.pstr.0000145**. https://doi.org/10.1371/journal.pstr.0000145 (robainaestevez2024applicationsofmarine pages 1-2)
- Ardalani O et al. *Pangenome reconstruction of Lactobacillaceae metabolism predicts species-specific metabolic traits.* **mSystems** (Jul 2024). DOI: **10.1128/msystems.00156-24**. https://doi.org/10.1128/msystems.00156-24 (ardalani2024pangenomereconstructionof pages 1-3)
- Shiroma H et al. *Enteropathway: the metabolic pathway database for the human gut microbiota.* **Briefings in Bioinformatics** (Jun 2024). DOI: **10.1093/bib/bbae419**. https://doi.org/10.1093/bib/bbae419 (shiroma2024enteropathwaythemetabolic pages 1-2)
- Majzoub ME et al. *Refining microbial community metabolic models derived from metagenomics using reference-based taxonomic profiling.* **mSystems** (Sep 2024). DOI: **10.1128/msystems.00746-24**. https://doi.org/10.1128/msystems.00746-24 (majzoub2024refiningmicrobialcommunity pages 1-2)
- Giordano N et al. *Genome-scale community modelling reveals conserved metabolic cross-feedings in epipelagic bacterioplankton communities.* **Nature Communications** (Mar 2024). DOI: **10.1038/s41467-024-46374-w**. https://doi.org/10.1038/s41467-024-46374-w (giordano2024genomescalecommunitymodelling media e09c444a)


References

1. (williams2024mappingthemetabolic pages 17-22): SA Williams, T Santangelo, JC Hansen, and M Pilon. Mapping the metabolic protein interactome that supports energy conservation at the limits of life. Unknown journal, 2024.

2. (williams2024mappingthemetabolic pages 22-26): SA Williams, T Santangelo, JC Hansen, and M Pilon. Mapping the metabolic protein interactome that supports energy conservation at the limits of life. Unknown journal, 2024.

3. (althaher2023anoverviewof pages 1-2): Arwa R. Althaher and Mohammad Alwahsh. An overview of atp synthase, inhibitors, and their toxicity. Heliyon, 9:e22459, Nov 2023. URL: https://doi.org/10.1016/j.heliyon.2023.e22459, doi:10.1016/j.heliyon.2023.e22459. This article has 36 citations.

4. (marschmann2024predictionsofrhizosphere pages 1-2): Gianna L. Marschmann, Jinyun Tang, Kateryna Zhalnina, Ulas Karaoz, Heejung Cho, Beatrice Le, Jennifer Pett-Ridge, and Eoin L. Brodie. Predictions of rhizosphere microbiome dynamics with a genome-informed and trait-based energy budget model. Nature Microbiology, 9:421-433, Feb 2024. URL: https://doi.org/10.1038/s41564-023-01582-w, doi:10.1038/s41564-023-01582-w. This article has 68 citations and is from a highest quality peer-reviewed journal.

5. (he2024emergingmultiscaleinsights pages 1-2): Xianjin He, Elsa Abs, Steven D. Allison, Feng Tao, Yuanyuan Huang, Stefano Manzoni, Rose Abramoff, Elisa Bruni, Simon P. K. Bowring, Arjun Chakrawal, Philippe Ciais, Lars Elsgaard, Pierre Friedlingstein, Katerina Georgiou, Gustaf Hugelius, Lasse Busk Holm, Wei Li, Yiqi Luo, Gaëlle Marmasse, Naoise Nunan, Chunjing Qiu, Stephen Sitch, Ying-Ping Wang, and Daniel S. Goll. Emerging multiscale insights on microbial carbon use efficiency in the land carbon cycle. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52160-5, doi:10.1038/s41467-024-52160-5. This article has 125 citations and is from a highest quality peer-reviewed journal.

6. (jin2023syntrophicpropionateoxidation pages 1-2): Yidan Jin and Yahai Lu. Syntrophic propionate oxidation: one of the rate-limiting steps of organic matter decomposition in anoxic environments. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00384-23, doi:10.1128/aem.00384-23. This article has 48 citations and is from a peer-reviewed journal.

7. (williams2024mappingthemetabolic pages 40-43): SA Williams, T Santangelo, JC Hansen, and M Pilon. Mapping the metabolic protein interactome that supports energy conservation at the limits of life. Unknown journal, 2024.

8. (carter2024applicationsofgenomescale pages 1-1): Elena Lucy Carter, Chrystala Constantinidou, and Mohammad Tauqeer Alam. Applications of genome-scale metabolic models to investigate microbial metabolic adaptations in response to genetic or environmental perturbations. Briefings in Bioinformatics, Nov 2024. URL: https://doi.org/10.1093/bib/bbad439, doi:10.1093/bib/bbad439. This article has 43 citations and is from a domain leading peer-reviewed journal.

9. (carter2024applicationsofgenomescale pages 1-2): Elena Lucy Carter, Chrystala Constantinidou, and Mohammad Tauqeer Alam. Applications of genome-scale metabolic models to investigate microbial metabolic adaptations in response to genetic or environmental perturbations. Briefings in Bioinformatics, Nov 2024. URL: https://doi.org/10.1093/bib/bbad439, doi:10.1093/bib/bbad439. This article has 43 citations and is from a domain leading peer-reviewed journal.

10. (carter2024applicationsofgenomescale pages 6-7): Elena Lucy Carter, Chrystala Constantinidou, and Mohammad Tauqeer Alam. Applications of genome-scale metabolic models to investigate microbial metabolic adaptations in response to genetic or environmental perturbations. Briefings in Bioinformatics, Nov 2024. URL: https://doi.org/10.1093/bib/bbad439, doi:10.1093/bib/bbad439. This article has 43 citations and is from a domain leading peer-reviewed journal.

11. (robainaestevez2024applicationsofmarine pages 1-2): Semidán Robaina-Estévez and Jay Gutiérrez. Applications of marine microbial community models in the nature-based economy. PLOS Sustainability and Transformation, 3:e0000145, Nov 2024. URL: https://doi.org/10.1371/journal.pstr.0000145, doi:10.1371/journal.pstr.0000145. This article has 6 citations and is from a peer-reviewed journal.

12. (shiroma2024enteropathwaythemetabolic pages 1-2): Hirotsugu Shiroma, Youssef Darzi, Etsuko Terajima, Zenichi Nakagawa, Hirotaka Tsuchikura, Naoki Tsukuda, Yuki Moriya, Shujiro Okuda, Susumu Goto, and Takuji Yamada. Enteropathway: the metabolic pathway database for the human gut microbiota. Briefings in Bioinformatics, Jun 2024. URL: https://doi.org/10.1093/bib/bbae419, doi:10.1093/bib/bbae419. This article has 13 citations and is from a domain leading peer-reviewed journal.

13. (ardalani2024pangenomereconstructionof pages 1-3): O. Ardalani, P. V. Phaneuf, O. S. Mohite, L. K. Nielsen, and B. O. Palsson. Pangenome reconstruction of <i>lactobacillaceae</i> metabolism predicts species-specific metabolic traits. mSystems, Jul 2024. URL: https://doi.org/10.1128/msystems.00156-24, doi:10.1128/msystems.00156-24. This article has 21 citations and is from a peer-reviewed journal.

14. (majzoub2024refiningmicrobialcommunity pages 1-2): Marwan E. Majzoub, Laurence D. W. Luu, Craig Haifer, Sudarshan Paramsothy, Thomas J. Borody, Rupert W. Leong, Torsten Thomas, and Nadeem O. Kaakoush. Refining microbial community metabolic models derived from metagenomics using reference-based taxonomic profiling. mSystems, Sep 2024. URL: https://doi.org/10.1128/msystems.00746-24, doi:10.1128/msystems.00746-24. This article has 6 citations and is from a peer-reviewed journal.

15. (giordano2024genomescalecommunitymodelling media e09c444a): Nils Giordano, Marinna Gaudin, Camille Trottier, Erwan Delage, Charlotte Nef, Chris Bowler, and Samuel Chaffron. Genome-scale community modelling reveals conserved metabolic cross-feedings in epipelagic bacterioplankton communities. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46374-w, doi:10.1038/s41467-024-46374-w. This article has 76 citations and is from a highest quality peer-reviewed journal.

16. (marschmann2024predictionsofrhizosphere pages 2-3): Gianna L. Marschmann, Jinyun Tang, Kateryna Zhalnina, Ulas Karaoz, Heejung Cho, Beatrice Le, Jennifer Pett-Ridge, and Eoin L. Brodie. Predictions of rhizosphere microbiome dynamics with a genome-informed and trait-based energy budget model. Nature Microbiology, 9:421-433, Feb 2024. URL: https://doi.org/10.1038/s41564-023-01582-w, doi:10.1038/s41564-023-01582-w. This article has 68 citations and is from a highest quality peer-reviewed journal.