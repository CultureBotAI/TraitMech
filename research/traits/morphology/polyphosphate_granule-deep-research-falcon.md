---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:06:26.769038'
end_time: '2026-06-18T09:25:54.317938'
duration_seconds: 1167.55
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: polyphosphate granule
  trait_identifier: traitmech:000068
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: polyphosphate_granule
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An intracellular storage inclusion of inorganic polyphosphate (a polymer
    of many phosphate residues), historically called a volutin or metachromatic granule,
    serving as a phosphate and energy reserve.
  parent_traits: traitmech:000066
  synonyms: volutin granule, metachromatic granule
  evidence_summary: "DOI:10.1146/annurev.biochem.77.083007.093039:  (Rao, G\xF3mez-Garc\xED\
    a & Kornberg review inorganic polyphosphate, accumulated as granules, as a phosphate/energy\
    \ reserve essential for growth and survival.) | DOI:10.1038/s41579-020-0413-0:\
    \  (Greening & Lithgow include polyphosphate bodies among bacterial intracellular\
    \ inclusions.)"
  causal_graph_summary: 'polyphosphate_granule_storage: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** polyphosphate granule
- **METPO identifier:** traitmech:000068
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion of inorganic polyphosphate (a polymer of many phosphate residues), historically called a volutin or metachromatic granule, serving as a phosphate and energy reserve.
- **Parent traits:** traitmech:000066
- **Synonyms:** volutin granule, metachromatic granule
- **Existing evidence:** DOI:10.1146/annurev.biochem.77.083007.093039:  (Rao, Gómez-García & Kornberg review inorganic polyphosphate, accumulated as granules, as a phosphate/energy reserve essential for growth and survival.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include polyphosphate bodies among bacterial intracellular inclusions.)
- **Existing causal graph summary:** polyphosphate_granule_storage: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **polyphosphate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyphosphate_granule.yaml`.

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
- **Trait label:** polyphosphate granule
- **METPO identifier:** traitmech:000068
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion of inorganic polyphosphate (a polymer of many phosphate residues), historically called a volutin or metachromatic granule, serving as a phosphate and energy reserve.
- **Parent traits:** traitmech:000066
- **Synonyms:** volutin granule, metachromatic granule
- **Existing evidence:** DOI:10.1146/annurev.biochem.77.083007.093039:  (Rao, Gómez-García & Kornberg review inorganic polyphosphate, accumulated as granules, as a phosphate/energy reserve essential for growth and survival.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include polyphosphate bodies among bacterial intracellular inclusions.)
- **Existing causal graph summary:** polyphosphate_granule_storage: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **polyphosphate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyphosphate_granule.yaml`.

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


# Research Report: Microbial Polyphosphate Granule (METPO:traitmech:000068)

## 1) Scope summary (trait meaning, boundaries, nearby traits)

**Trait meaning.** The trait *polyphosphate granule* refers to an **intracellular inclusion body enriched in inorganic polyphosphate (polyP)**, often appearing **electron-dense** and historically described as **volutin** or **metachromatic granules** because they stain metachromatically with basic dyes. (docampo2024advancesinthe pages 2-4, rao2009inorganicpolyphosphateessential pages 4-5)

**Synonymy and relationship to acidocalcisomes.** Modern literature links these microbial polyP inclusions to **acidocalcisomes** (acidic, Ca2+/polyP-rich compartments) as evolutionarily related structures; however, boundary cases exist where **acidocalcisomes and polyP granules are reported as distinct structures in some bacteria** (e.g., *Agrobacterium tumefaciens*), so “polyP granule = acidocalcisome” should be curated cautiously and possibly as *related_to* rather than strict equivalence for all taxa. (moreno2013polyphosphateandits pages 1-2, docampo2024advancesinthe pages 1-2, docampo2024advancesinthe pages 29-30, docampo2024advancesinthe pages 2-4)

**Boundary cases and confounders.**
- Environmental samples can contain **P-rich inclusions** that are not exclusively polyP; dye staining alone can be nonspecific and requires confirmatory methods (e.g., TEM+EDX/EELS, 31P NMR). (hupfer2008methodsfordetection pages 5-8)
- PolyP granules can be confused with other inclusion bodies (e.g., PHB granules) unless differentiated by **double staining** or elemental analysis. (hupfer2008methodsfordetection pages 5-8)

**Operational/assay definition for curation.** For TraitMech purposes, this morphology trait is best captured as: “**presence/formation of discrete intracellular polyP-rich inclusions** detectable by polyP-specific staining/probes and/or elemental/spectroscopic confirmation.” (docampo2024advancesinthe pages 2-4, hupfer2008methodsfordetection pages 5-8)

## 2) Key concepts and current understanding (mechanistic overview)

### 2.1 Core chemistry and compartment properties
PolyP is a linear polymer of orthophosphate residues linked by energy-rich phosphoanhydride bonds and serves as a phosphate/energy reservoir and stress-related factor. (iakovchuk2024extraordinaryphysiologyof pages 1-4, schoeppe2024anupdateonc pages 1-2)

PolyP in granules is commonly associated with counter-ions (e.g., Ca2+, Mg2+, K+), and polyP’s biophysical state depends strongly on cation binding (e.g., Ca2+ binding can strongly change polymer properties/solubility). (docampo2024advancesinthe pages 1-2, schoeppe2024anupdateonb pages 2-4, schoeppe2024anupdateond pages 2-4)

### 2.2 Core enzymes: synthesis and degradation
**Synthesis:** In bacteria, polyP synthesis is classically attributed to **polyphosphate kinase (PPK/PPK1)**, which uses ATP to polymerize phosphate into polyP. (baijal2024polyphosphatekinaseregulates pages 1-2, baijal2024polyphosphatekinaseregulates pages 2-3)

**Degradation:** PolyP degradation is classically carried out by **exopolyphosphatase (PPX)** hydrolyzing polyP to Pi. (baijal2024polyphosphatekinaseregulates pages 1-2)

**Diversity/complexity:** Some taxa show unexpected polyP network wiring, e.g., in *Lacticaseibacillus paracasei* a putative “exopolyphosphatase” **Ppx1 is essential for polyP accumulation** and **enhances Ppk activity** despite lacking canonical catalytic motifs, while Ppx2 shows in vitro PPX activity but is not required for accumulation in that strain. This is a strong example that “PPX = degradation only” is not universally safe to curate without taxon context. (corrales2024ppx1putativeexopolyphosphatase pages 1-6)

### 2.3 Environmental drivers (canonical patterns)
**Starvation/nutrient downshift:** PolyP levels are induced by diverse stressors; in *E. coli*, shifting from rich LB to minimal MOPS triggers **PPK-dependent polyP accumulation**, absent in Δppk mutants. (baijal2024polyphosphatekinaseregulates pages 1-2, baijal2024polyphosphatekinaseregulates pages 2-3)

**EBPR redox cycling:** In EBPR, PAOs typically **take up phosphate aerobically to synthesize polyP**, and **hydrolyze polyP anaerobically with phosphate release** to support metabolism. (ruizhaddadUnknownyearenvironmentalscienceanda pages 1-3)

**Metal stress:** PolyP responds to metals, including copper stress in archaea where polyP degradation correlates with copper concentration. (acevedolopez2024roleofpolyphosphate pages 1-2)

## 3) Recent developments and latest research (prioritize 2023–2024)

### 3.1 2024 authoritative synthesis on organelles/definitions
Docampo’s 2024 Microbiology and Molecular Biology Reviews article consolidates current understanding of acidocalcisomes and their relationship to microbial volutin/metachromatic granules, emphasizing shared features (acidity, high polyP and calcium) and methods used to characterize them (microscopy, NMR, X-ray microanalysis, proteomics), while also noting boundary cases where structures are distinct. (docampo2024advancesinthe pages 1-2, docampo2024advancesinthe pages 29-30, docampo2024advancesinthe pages 2-4)

### 3.2 2024: single-cell and advanced measurement approaches
**Single-cell Raman:** A 2024 ecosystem-engineering preprint introduced an in situ workflow using **Raman-activated cell sorting** to quantify polyP at the single-cell level via the **polyphosphate Raman band**, enabling selection/cultivation of in situ high-activity PAOs. (xu2024miningrobustin pages 1-6)

**Expanded assay toolbox:** A 2024 review highlights broadening approaches for microbial polyP detection including DAPI-based quantification, tetracycline labeling, flow cytometry, Raman microscopy, and cryo-ET/spectroscopic imaging for subcellular bodies. (schoeppe2024anupdateon pages 16-17)

### 3.3 2024: new mechanistic links from primary studies
**Starvation → membrane remodeling and antibiotic susceptibility:** A 2024 *PLOS Biology* study provides detailed mechanistic links from PPK (and/or polyP) to starvation-induced regulation of BasRS and lipid A modification enzymes (Arn/EptA), affecting polymyxin resistance. (baijal2024polyphosphatekinaseregulates pages 20-21, baijal2024polyphosphatekinaseregulates pages 8-9, baijal2024polyphosphatekinaseregulates pages 9-11)

**Fe(III) exposure suppresses EBPR polyP metabolism:** A 2024 *Frontiers in Microbiology* study shows chronic ferric dosing shifts communities away from polyP accumulation and decreases intracellular P storage, with quantitative impacts (see statistics section). (hong2024inhibitionofphosphorus pages 1-2)

**Archaeal copper stress:** A 2024 *Microorganisms* study supports polyP as an inorganic chaperone-like factor under copper stress, with copper-concentration-dependent degradation of polyP. (acevedolopez2024roleofpolyphosphate pages 1-2)

## 4) Current applications and real-world implementations

### 4.1 Wastewater EBPR and ecosystem engineering
**EBPR is a direct real-world implementation of polyP granule biology**: it leverages microbes that store phosphorus intracellularly as polyP and removes P via sludge wasting. (ruizhaddadUnknownyearenvironmentalscienceanda pages 1-3, xu2024miningrobustin pages 1-6)

A 2024 in situ PAO mining/augmentation study reports that time- and location-specific introduction of a Raman-selected isolate (**Micrococcus luteum MCI5-8**) improved P removal efficiency in an AAO reactor from **45% to 89%**. (xu2024miningrobustin pages 1-6)

### 4.2 Interactions with chemical phosphorus removal strategies
Simultaneous chemical phosphorus removal (SCPR) with iron salts is widely used operationally; a 2024 study notes that in China **SCPR accounts for >43.5% of phosphorus treatment** of approximately **0.31 million tons P annually**, but can inhibit EBPR intracellular P storage under certain dosing regimes. (hong2024inhibitionofphosphorus pages 1-2)

### 4.3 Antimicrobial/anti-virulence relevance
PPK/polyP is microbe-centered and linked to stress survival phenotypes; the 2024 *PLOS Biology* study provides a mechanistic rationale that interfering with PPK/polyP pathways can impact **polymyxin resistance** via lipid A remodeling during starvation. (baijal2024polyphosphatekinaseregulates pages 20-21, baijal2024polyphosphatekinaseregulates pages 1-2)

## 5) Relevant statistics and quantitative data (recent studies)

- **EBPR augmentation performance:** AAO reactor phosphorus removal increased from **45% to 89%** after introducing a Raman-selected PAO isolate (MCI5-8) guided by in situ single-cell polyP activity. (xu2024miningrobustin pages 1-6)
- **Fe(III) inhibition of intracellular P storage:** Under prolonged Fe(III) exposure in SBRs (155 days; Fe/P 1.0–2.0), intracellular P storage decreased to **3.11–7.67 mg P/g VSS**, which was **26.01–64.13% of control**. (hong2024inhibitionofphosphorus pages 1-2)
- **Beggiatoa phosphate uptake rate after refeeding:** After phosphate reintroduction, Beggiatoa sp. 35Flor showed rapid uptake within 10 min with rates up to **298 mmol P g−1 protein d−1**, estimated at **0.6–6 mmol m−2 d−1** for typical filament densities in coastal sediments. (iakovchuk2024extraordinaryphysiologyof pages 1-4)
- **Copper stress threshold (archaea):** At **2 mM Cu2+ (MIC)**, polyP degradation stabilized after ~2 h and showed no recovery after 24 h in *Saccharolobus solfataricus*. (acevedolopez2024roleofpolyphosphate pages 1-2)

## 6) Candidate nodes (grouped by type, with grounding)

| Type | Node label | Suggested identifier/CURIE | Notes (1 sentence) | Key supporting citations |
|---|---|---|---|---|
| Cellular structure/localization | polyphosphate granule (volutin granule; metachromatic granule) | METPO:traitmech:000068 | Intracellular electron-dense polyphosphate inclusion used for phosphate/energy storage and historically identified by metachromasy. | (docampo2024advancesinthe pages 2-4, rao2009inorganicpolyphosphateessential pages 4-5) |
| Cellular structure/localization | acidocalcisome-like organelle | GO:0020015 | Acidic polyP- and Ca-rich compartment related to bacterial/archaeal volutin granules, though distinct from polyP granules in some taxa. | (moreno2013polyphosphateandits pages 1-2, docampo2024advancesinthe pages 1-2, docampo2024advancesinthe pages 29-30) |
| Cellular structure/localization | cytoplasmic polyP inclusion | GO:1905630 | PolyP inclusions are typically intracellular/cytoplasmic, although some reports note periplasmic or surface-associated P-rich inclusions in environmental microbes. | (achbergerova2011polyphosphatean pages 1-2, hupfer2008methodsfordetection pages 5-8) |
| Chemical/Metabolite | polyphosphate (polyP) | CHEBI:8686 | Linear polymer of orthophosphate residues linked by phosphoanhydride bonds that composes the granule core. | (iakovchuk2024extraordinaryphysiologyof pages 1-4, schoeppe2024anupdateonc pages 1-2) |
| Chemical/Metabolite | phosphate (orthophosphate; Pi) | CHEBI:43474 | Pi is the monomeric substrate taken up and polymerized into polyP and is released again during granule mobilization. | (iakovchuk2024extraordinaryphysiologyof pages 1-4, ruizhaddadUnknownyearenvironmentalscienceanda pages 1-3) |
| Chemical/Metabolite | calcium ion (Ca2+) | CHEBI:29108 | Ca2+ is a common counter-ion associated with polyP granules/acidocalcisomes and strongly affects polyP biophysical properties. | (docampo2024advancesinthe pages 1-2, schoeppe2024anupdateonb pages 2-4) |
| Chemical/Metabolite | magnesium ion (Mg2+) | CHEBI:18420 | Mg2+ is a frequent counter-ion in polyP-rich inclusions and also supports activity of some PPX enzymes. | (hupfer2008methodsfordetection pages 5-8, schoeppe2024anupdateond pages 2-4) |
| Chemical/Metabolite | potassium ion (K+) | CHEBI:29103 | K+ commonly accompanies microbial polyP inclusions as a balancing cation. | (hupfer2008methodsfordetection pages 5-8) |
| Chemical/Metabolite | iron(III)/iron | CHEBI:29033 | Iron availability modulates some polyP-linked stress pathways and Fe(III) dosing can suppress biological phosphorus cycling in EBPR communities. | (baijal2024polyphosphatekinaseregulates pages 9-11, hong2024inhibitionofphosphorus pages 1-2) |
| Chemical/Metabolite | copper(II) | CHEBI:29036 | Cu2+ stress drives polyP degradation in an archaeal model and highlights a metal-stress role for polyP turnover. | (acevedolopez2024roleofpolyphosphate pages 1-2) |
| Chemical/Metabolite | ATP | CHEBI:15422 | ATP is the canonical phosphate donor for PPK1-mediated polyP synthesis. | (baijal2024polyphosphatekinaseregulates pages 1-2, schoeppe2024anupdateond pages 2-4) |
| Chemical/Metabolite | GTP | CHEBI:15996 | GTP is produced from GDP by some PPK2 enzymes using polyP as phosphate donor and can also serve in PPK2-associated reactions. | (villard2024transcriptionalprofilingelucidates pages 12-13, schoeppe2024anupdateond pages 2-4) |
| Gene/Protein | polyphosphate kinase 1 (PPK1/PPK) | EC:2.7.4.1 | PPK1 is the principal bacterial enzyme synthesizing polyP from ATP and is required for starvation-induced accumulation in E. coli. | (baijal2024polyphosphatekinaseregulates pages 1-2, baijal2024polyphosphatekinaseregulates pages 2-3) |
| Gene/Protein | polyphosphate kinase 2 (PPK2) | EC:2.7.4.- | PPK2 participates in polyP cycling and was aerobically upregulated in EBPR biofilms, with literature supporting roles in polyP synthesis or GDP-to-GTP phosphorylation using polyP. | (villard2024transcriptionalprofilingelucidates pages 12-13, schoeppe2024anupdateond pages 2-4) |
| Gene/Protein | exopolyphosphatase (PPX) | EC:3.6.1.11 | PPX hydrolyzes polyP to Pi and is a core degradative enzyme in microbial polyP turnover. | (baijal2024polyphosphatekinaseregulates pages 1-2, acevedolopez2024roleofpolyphosphate pages 1-2) |
| Gene/Protein | Ppx1 |  | In Lacticaseibacillus paracasei, Ppx1 is unexpectedly required for polyP accumulation and appears to enhance Ppk activity despite lacking canonical catalytic motifs. | (corrales2024ppx1putativeexopolyphosphatase pages 1-6) |
| Gene/Protein | Ppx2 |  | Ppx2 in L. paracasei has in vitro exopolyphosphatase activity but is not required for cellular polyP accumulation in the tested strain. | (corrales2024ppx1putativeexopolyphosphatase pages 1-6) |
| Gene/Protein | PhoB |  | PhoB is a phosphate-starvation regulator implicated in polyP-related regulation, although some PPK-dependent outputs can persist when PhoB-dependent polyP accumulation is reduced. | (baijal2024polyphosphatekinaseregulates pages 8-9, corrales2024ppx1putativeexopolyphosphatase pages 1-6) |
| Gene/Protein | BasRS two-component system |  | BasRS is a starvation-responsive signaling system whose induction during MOPS starvation depends on PPK in E. coli. | (baijal2024polyphosphatekinaseregulates pages 8-9, baijal2024polyphosphatekinaseregulates pages 9-11, baijal2024polyphosphatekinaseregulates pages 2-3) |
| Gene/Protein | Arn proteins |  | Arn enzymes mediate lipid A aminoarabinose modification downstream of BasRS and are reduced in Δppk mutants during starvation. | (baijal2024polyphosphatekinaseregulates pages 8-9, baijal2024polyphosphatekinaseregulates pages 9-11) |
| Gene/Protein | EptA |  | EptA mediates phosphoethanolamine modification of lipid A and is part of the PPK-dependent starvation response in E. coli. | (baijal2024polyphosphatekinaseregulates pages 1-2, baijal2024polyphosphatekinaseregulates pages 2-3) |
| Gene/Protein | Lon protease |  | PolyP interacts with Lon protease in stress responses to promote selective proteolysis. | (baijal2024polyphosphatekinaseregulates pages 20-21, baijal2024polyphosphatekinaseregulates pages 1-2) |
| Gene/Protein | DnaA |  | PolyP/Lon-dependent degradation of ADP-bound DnaA links polyP accumulation to inhibition of DNA replication during stress. | (baijal2024polyphosphatekinaseregulates pages 1-2) |
| Gene/Protein | Pit phosphate transporter |  | Pit is a low-affinity phosphate transporter that is aerobically upregulated in EBPR biofilms and has also been implicated in metal-phosphate export models. | (villard2024transcriptionalprofilingelucidates pages 12-13, albi2016inorganicpolyphosphatein pages 12-15) |
| Gene/Protein | Pst phosphate transporter |  | Pst is a high-affinity phosphate transporter transcribed in EBPR biofilms and associated with phosphate uptake under limiting conditions. | (villard2024transcriptionalprofilingelucidates pages 12-13) |
| Process/Pathway | polyP granule biogenesis / polyP accumulation | GO:0071547 | Formation of visible polyP inclusions reflects polymer synthesis and physicochemical condensation into intracellular granules. | (iakovchuk2024extraordinaryphysiologyof pages 1-4, docampo2024advancesinthe pages 2-4) |
| Process/Pathway | polyP degradation / mobilization | GO:0006796 | Granule mobilization involves hydrolysis of stored polyP to release phosphate and energy equivalents under stress or anaerobic phases. | (baijal2024polyphosphatekinaseregulates pages 1-2, ruizhaddadUnknownyearenvironmentalscienceanda pages 1-3, acevedolopez2024roleofpolyphosphate pages 1-2) |
| Process/Pathway | EBPR anaerobic/aerobic cycling |  | In EBPR, anaerobic phases favor polyP hydrolysis and phosphate release, while aerobic phases favor phosphate uptake and polyP synthesis. | (ruizhaddadUnknownyearenvironmentalscienceanda pages 1-3, villard2024transcriptionalprofilingelucidates pages 12-13) |
| Process/Pathway | phosphate starvation response | GO:0016036 | Starvation is a major trigger for PPK-dependent polyP accumulation and associated survival/stress phenotypes. | (baijal2024polyphosphatekinaseregulates pages 1-2, baijal2024polyphosphatekinaseregulates pages 2-3) |
| Process/Pathway | overplus / luxury phosphate uptake |  | Re-exposure of phosphate-starved cells to phosphate can drive rapid uptake and polyP accumulation as an overplus response. | (iakovchuk2024extraordinaryphysiologyof pages 1-4) |
| Process/Pathway | glycogen-accumulating metabolism shift |  | Under chronic Fe(III) stress, EBPR communities shift from polyP-accumulating metabolism toward glycogen-centered metabolism. | (hong2024inhibitionofphosphorus pages 1-2) |
| Environmental/Experimental factor | aerobic conditions | ENVO:01000626 | Aerobic conditions promote phosphate uptake and polyP synthesis in EBPR-associated PAOs and coincide with ppk2/pit upregulation in biofilms. | (ruizhaddadUnknownyearenvironmentalscienceanda pages 1-3, villard2024transcriptionalprofilingelucidates pages 12-13) |
| Environmental/Experimental factor | anaerobic conditions | ENVO:01000635 | Anaerobic conditions promote polyP hydrolysis and phosphate release in canonical EBPR physiology. | (ruizhaddadUnknownyearenvironmentalscienceanda pages 1-3) |
| Environmental/Experimental factor | phosphate starvation |  | Phosphate limitation/starvation selects for polyP-based buffering strategies and primes overplus uptake on phosphate readdition. | (iakovchuk2024extraordinaryphysiologyof pages 1-4) |
| Environmental/Experimental factor | phosphate reintroduction / refeeding |  | Reintroduction of phosphate after starvation can trigger rapid uptake and renewed polyP storage. | (iakovchuk2024extraordinaryphysiologyof pages 1-4) |
| Environmental/Experimental factor | Fe(III) dosing |  | Ferric dosing in EBPR reactors inhibits intracellular P storage and suppresses polyP-pathway gene abundance under chronic exposure. | (hong2024inhibitionofphosphorus pages 1-2) |
| Environmental/Experimental factor | copper stress |  | Copper stress causes concentration-dependent polyP degradation and reveals a protective chaperone-like role for polyP. | (acevedolopez2024roleofpolyphosphate pages 1-2) |
| Environmental/Experimental factor | nutrient downshift / starvation in MOPS |  | Transfer from rich LB to MOPS minimal medium is an experimental starvation/downshift condition that induces PPK-dependent polyP accumulation in E. coli. | (baijal2024polyphosphatekinaseregulates pages 2-3) |
| Assay/measurement | DAPI staining / fluorometry |  | DAPI-based microscopy and fluorometric assays are widely used to visualize and quantify intracellular polyP granules, though chain-length caveats apply. | (schoeppe2024anupdateon pages 16-17, docampo2024advancesinthe pages 2-4, hupfer2008methodsfordetection pages 5-8) |
| Assay/measurement | Raman band detection (single-cell Raman) |  | Raman spectroscopy enables label-free single-cell detection and quantification of polyP accumulation directly in environmental samples. | (schoeppe2024anupdateon pages 16-17, xu2024miningrobustin pages 1-6) |
| Assay/measurement | electron microscopy with EDX/EELS |  | TEM/cryo-EM with elemental spectroscopy identifies electron-dense inclusions and confirms phosphorus-rich composition and associated cations. | (schoeppe2024anupdateon pages 16-17, hupfer2008methodsfordetection pages 5-8) |
| Assay/measurement | 31P NMR |  | 31P NMR detects condensed inorganic phosphates and supports chemical characterization of polyP-rich granules/organelles. | (docampo2024advancesinthe pages 1-2, docampo2024advancesinthe pages 29-30, rao2009inorganicpolyphosphateessential pages 4-5) |
| Assay/measurement | EcPPX binding-domain probe (EcPPXbd) |  | Fluorescently tagged E. coli PPX polyP-binding domain is a specific affinity probe for imaging long-chain polyP in situ. | (quarles2024cryosectioningandimmunofluorescence pages 1-3, schoeppe2024anupdateona pages 15-16) |


*Table: This table lists candidate TraitMech node entities for microbial polyphosphate granules, grouped by node type and annotated with suggested identifiers, concise mechanistic notes, and supporting evidence IDs. It is designed to support direct curation of a causal-graph YAML for the polyphosphate granule trait.*

## 7) Candidate evidence-backed causal edges (triples with snippets/notes)

| Subject | Predicate | Object | Suggested grounding for subject/object (CURIEs if known) | Evidence snippet (short quote or paraphrase anchored to source) | Reference (first author, year, title/journal) | DOI/URL | Evidence strength/notes |
|---|---|---|---|---|---|---|---|
| PPK1/PPK | synthesizes | polyphosphate (polyP) | PPK1: EC:2.7.4.1; polyP: CHEBI:8686 | “Polyphosphate is synthesized by polyphosphate kinase (PPK)” and “PPK rapidly synthesizes polyP using ATP as a co-substrate” (baijal2024polyphosphatekinaseregulates pages 1-2) | Baijal, 2024, *PLOS Biology* | https://doi.org/10.1371/journal.pbio.3002558 | Strong; direct enzyme-function statement in bacteria. |
| PPX | degrades | polyphosphate (polyP) | PPX: EC:3.6.1.11; polyP: CHEBI:8686 | “polyphosphate is…degraded by exopolyphosphatase PPX” (baijal2024polyphosphatekinaseregulates pages 1-2) | Baijal, 2024, *PLOS Biology* | https://doi.org/10.1371/journal.pbio.3002558 | Strong; canonical core metabolism edge. |
| starvation / nutrient downshift (LB→MOPS) | increases | PPK-dependent polyP accumulation | process; PPK1: EC:2.7.4.1 | “shifting E. coli from rich LB to MOPS minimal media triggers polyP accumulation in wild-type but not in Δppk mutants” (baijal2024polyphosphatekinaseregulates pages 2-3) | Baijal, 2024, *PLOS Biology* | https://doi.org/10.1371/journal.pbio.3002558 | Strong but condition-specific; E. coli starvation model. |
| aerobic phase in EBPR | increases | phosphate uptake and polyP synthesis | aerobic conditions: ENVO:01000626; phosphate: CHEBI:43474; polyP: CHEBI:8686 | “PAOs take up phosphate under aerobic conditions to synthesize PolyP” (ruizhaddadUnknownyearenvironmentalscienceanda pages 1-3) | Ruiz-Haddad, 2024, *Environmental Science and Ecotechnology* | source retrieved without stable DOI in context | Strong for EBPR physiology; review synthesis. |
| anaerobic phase in EBPR | increases | polyP hydrolysis and phosphate release | anaerobic conditions: ENVO:01000635; polyP: CHEBI:8686; phosphate: CHEBI:43474 | “in the anaerobic phase PolyP is hydrolyzed and phosphate is released” (ruizhaddadUnknownyearenvironmentalscienceanda pages 1-3) | Ruiz-Haddad, 2024, *Environmental Science and Ecotechnology* | source retrieved without stable DOI in context | Strong for canonical EBPR model; review synthesis. |
| phosphate reintroduction after starvation | increases | overplus phosphate uptake / polyP storage | phosphate: CHEBI:43474; polyP: CHEBI:8686 | Beggiatoa showed “rapid phosphate uptake…within the first 10 minutes” after reintroduction, consistent with overplus storage as polyP (iakovchuk2024extraordinaryphysiologyof pages 1-4) | Iakovchuk, 2024, *bioRxiv* | https://doi.org/10.1101/2024.11.22.624918 | Moderate; preprint and taxon-specific but quantitatively strong. |
| Fe(III) exposure | decreases | intracellular phosphorus storage / polyP metabolism | Fe(III): CHEBI:29033; intracellular P storage: label-only | “intracellular P storage fell to 3.11–7.67 mg P/g VSS (26.01–64.13% of control)” and polyphosphate-pathway genes decreased under chronic Fe(III) stress (hong2024inhibitionofphosphorus pages 1-2) | Hong, 2024, *Frontiers in Microbiology* | https://doi.org/10.3389/fmicb.2024.1424938 | Strong for activated sludge EBPR communities; reactor-specific. |
| Fe(III) exposure | shifts | polyphosphate-accumulating metabolism to glycogen-accumulating metabolism | polyP metabolism: label-only; glycogen metabolism: GO:0005977 | Chronic Fe(III) stress “shifted the community from polyphosphate-accumulating metabolism to glycogen-accumulating metabolism” (hong2024inhibitionofphosphorus pages 1-2) | Hong, 2024, *Frontiers in Microbiology* | https://doi.org/10.3389/fmicb.2024.1424938 | Strong in EBPR reactor context. |
| copper stress | increases | polyP degradation | Cu2+: CHEBI:29036; polyP: CHEBI:8686 | In *S. solfataricus*, “polyP degradation is directly correlated with metal concentration,” with effects at 2 mM Cu2+ (acevedolopez2024roleofpolyphosphate pages 1-2) | Acevedo-López, 2024, *Microorganisms* | https://doi.org/10.3390/microorganisms12122627 | Strong but archaeon-specific. |
| Ppx1 | enhances activity of | Ppk | Ppx1: label-only; Ppk: EC:2.7.4.1 | “assays with purified Ppk and Ppx1 evidenced that Ppx1 enhanced Ppk activity” (corrales2024ppx1putativeexopolyphosphatase pages 1-6) | Corrales, 2024, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.02290-23 | Strong, direct biochemical evidence; species-specific. |
| Ppx1 deletion | decreases | polyP accumulation | Ppx1: label-only; polyP: CHEBI:8686 | “deletion of ppx1 abolishes cellular poly-P accumulation” and restoration required ppx1 in trans (corrales2024ppx1putativeexopolyphosphatase pages 1-6) | Corrales, 2024, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.02290-23 | Strong, direct genetics; *Lacticaseibacillus paracasei*-specific. |
| Ppx2 | degrades | polyP | Ppx2: label-only; polyP: CHEBI:8686 | “Purified Ppx2 showed in vitro exopolyphosphatase activity” (corrales2024ppx1putativeexopolyphosphatase pages 1-6) | Corrales, 2024, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.02290-23 | Strong biochemical evidence; species-specific. |
| ppk deletion | decreases | BasRS induction during starvation | ppk: EC:2.7.4.1; BasRS: label-only | “MOPS induces transcription of arn, basS, and basR in wild-type cells, but this response is defective in Δppk mutants” (baijal2024polyphosphatekinaseregulates pages 8-9, baijal2024polyphosphatekinaseregulates pages 9-11) | Baijal, 2024, *PLOS Biology* | https://doi.org/10.1371/journal.pbio.3002558 | Strong; starvation/MOPS-specific in E. coli. |
| reduced BasRS induction | decreases | Arn and EptA expression | BasRS: label-only; Arn: label-only; EptA: label-only | “BasS and BasR protein levels are decreased in Δppk during starvation” and Δppk mutants show decreased Arn/EptA-related outputs (baijal2024polyphosphatekinaseregulates pages 8-9, baijal2024polyphosphatekinaseregulates pages 9-11, baijal2024polyphosphatekinaseregulates pages 2-3) | Baijal, 2024, *PLOS Biology* | https://doi.org/10.1371/journal.pbio.3002558 | Strong within the studied regulatory circuit. |
| reduced Arn/EptA expression | decreases | lipid A modification | Arn/EptA: label-only; lipid A modification: GO/label-only | Loss of ppk reduced “L-Ara4N and pEtN modifications on lipid A” through Arn/EptA pathway effects (baijal2024polyphosphatekinaseregulates pages 20-21, baijal2024polyphosphatekinaseregulates pages 9-11) | Baijal, 2024, *PLOS Biology* | https://doi.org/10.1371/journal.pbio.3002558 | Strong for E. coli starvation response. |
| decreased lipid A modification | increases | polymyxin sensitivity | lipid A modification: label-only; polymyxin sensitivity: label-only | “loss of ppk restores polymyxin sensitivity” in resistant strains, consistent with reduced Arn/EptA-mediated lipid A modification (baijal2024polyphosphatekinaseregulates pages 20-21, baijal2024polyphosphatekinaseregulates pages 1-2) | Baijal, 2024, *PLOS Biology* | https://doi.org/10.1371/journal.pbio.3002558 | Strong phenotype link; antibiotic/stress context. |
| aerobic upregulation of Pit transporter | increases | phosphate uptake | Pit: label-only; phosphate: CHEBI:43474 | In EBPR biofilms, PIT transporter was “significantly upregulated in the aerobic zones,” implying aerobic P uptake (villard2024transcriptionalprofilingelucidates pages 12-13) | Villard, 2024, *Water Science & Technology* | https://doi.org/10.2166/wst.2024.314 | Moderate; transcriptional inference rather than direct flux measurement. |
| aerobic conditions | increases | ppk2 expression | aerobic conditions: ENVO:01000626; ppk2: label-only | “ppk2 gene…was significantly upregulated aerobically” in EBPR biofilms (villard2024transcriptionalprofilingelucidates pages 12-13) | Villard, 2024, *Water Science & Technology* | https://doi.org/10.2166/wst.2024.314 | Moderate; expression edge, role in synthesis vs degradation remains context-dependent. |
| DAPI staining | detects | polyP granules | DAPI assay: label-only; polyP granule: METPO:traitmech:000068 | DAPI is cited for “visual detection of polyP granules within cells” and for quantitative DAPI-based polyP measurements (schoeppe2024anupdateon pages 16-17, docampo2024advancesinthe pages 2-4, hupfer2008methodsfordetection pages 5-8) | Schoeppe, 2024, *Biomolecules*; Hupfer, 2008, *Int Rev Hydrobiol* | https://doi.org/10.3390/biom14080937; https://doi.org/10.1002/iroh.200610935 | Strong as assay edge; note chain-length/method caveats. |
| Raman polyP band | quantifies | single-cell polyP accumulation | Raman assay: label-only; polyP: CHEBI:8686 | “label-free, quantitative single-cell detection of polyphosphate accumulation via the polyphosphate Raman band” (xu2024miningrobustin pages 1-6) | Xu, 2024, *Research Square preprint* | https://doi.org/10.21203/rs.3.rs-5292508/v1 | Moderate; powerful method but preprint status. |
| polyP granule | synonym_of | volutin/metachromatic granule | polyP granule: METPO:traitmech:000068; volutin granule: label-only; metachromatic granule: label-only | PolyP granules are “historically called volutin or metachromatic granules” (achbergerova2011polyphosphatean pages 1-2, docampo2024advancesinthe pages 2-4, rao2009inorganicpolyphosphateessential pages 4-5) | Achbergerová, 2011, *Microbial Cell Factories*; Docampo, 2024, *MMBR*; Rao, 2009, *Annu Rev Biochem* | https://doi.org/10.1186/1475-2859-10-63; https://doi.org/10.1128/mmbr.00042-23; https://doi.org/10.1146/annurev.biochem.77.083007.093039 | Strong nomenclature edge suitable for ontology mapping. |
| acidocalcisome | related_to | volutin/metachromatic granule | acidocalcisome: GO:0020015; volutin granule: label-only | Acidocalcisomes are “related to the metachromatic or volutin granules” and in some sources “equivalent” to bacterial volutin granules (moreno2013polyphosphateandits pages 1-2, docampo2024advancesinthe pages 1-2, docampo2024advancesinthe pages 2-4) | Moreno, 2013, *PLoS Pathogens*; Docampo, 2024, *MMBR* | https://doi.org/10.1371/journal.ppat.1003230; https://doi.org/10.1128/mmbr.00042-23 | Moderate; curate cautiously because some taxa have distinct acidocalcisomes vs polyP granules. |
| polyP | chelates / binds | divalent cations (Ca2+, Mg2+, Fe2+/Fe3+, Zn2+) | polyP: CHEBI:8686; Ca2+: CHEBI:29108; Mg2+: CHEBI:18420; Fe3+: CHEBI:29033 | PolyP/counter-ion biology: granules contain associated cations, and polyP can bind iron and inhibit Fenton chemistry; cation binding affects polyP biophysics (schoeppe2024anupdateonc pages 1-2, baijal2024polyphosphatekinaseregulates pages 1-2, schoeppe2024anupdateonb pages 2-4, schoeppe2024anupdateond pages 2-4) | Schoeppe, 2024, *Biomolecules*; Baijal, 2024, *PLOS Biology* | https://doi.org/10.3390/biom14080937; https://doi.org/10.1371/journal.pbio.3002558 | Strong general biochemical edge; exact cation composition varies by organism/compartment. |
| polyP accumulation | promotes | stress survival / stress response functions | polyP: CHEBI:8686; stress survival: GO/label-only | PolyP serves as phosphate/energy storage and supports “survival in stationary phase and nutrient starvation”; Δppk mutants show stress sensitivity (schoeppe2024anupdateonc pages 1-2, baijal2024polyphosphatekinaseregulates pages 1-2) | Schoeppe, 2024, *Biomolecules*; Baijal, 2024, *PLOS Biology* | https://doi.org/10.3390/biom14080937; https://doi.org/10.1371/journal.pbio.3002558 | Moderate; broad physiological edge rather than granule-specific morphology. |


*Table: This table lists curation-ready candidate causal edges for the microbial polyphosphate granule trait, with grounding suggestions, evidence snippets, and source details. It is designed to support TraitMech graph construction while flagging taxon- or condition-specific claims.*

## 8) Expert opinions and analysis (curation guidance)

**Curation stance on “granule” vs “acidocalcisome.”** Authoritative reviews frame volutin/metachromatic granules as closely related to acidocalcisomes (shared polyP/Ca2+ and acidity), but also document taxa where structures differ; for TraitMech, prefer **two nodes** (polyP granule; acidocalcisome-like organelle) with **a cautious relation edge** rather than assuming strict equivalence. (docampo2024advancesinthe pages 1-2, docampo2024advancesinthe pages 29-30, docampo2024advancesinthe pages 2-4)

**Assay caution.** Staining (e.g., DAPI) is highly useful but can be nonspecific and method-dependent; environmental samples may require confirmatory approaches (TEM+EDX/EELS, 31P NMR, or affinity probes like EcPPXbd) before curating “polyP granule present” as a validated phenotype. (hupfer2008methodsfordetection pages 5-8, schoeppe2024anupdateon pages 16-17, quarles2024cryosectioningandimmunofluorescence pages 1-3)

**Taxon-specific enzymology.** The *L. paracasei* example shows that exopolyphosphatase-labeled genes may have noncanonical functions (Ppx1 enhancing Ppk and being essential for accumulation). Curate such edges with organism constraints (NCBITaxon) or mark uncertain for general graphs. (corrales2024ppx1putativeexopolyphosphatase pages 1-6)

## 9) Warnings: claims not yet safe to curate into TraitMech

1. **Universal identity of polyP granules with acidocalcisomes:** evidence supports close relationship, but not universal equivalence; keep as *related_to* unless species-specific evidence supports identity. (docampo2024advancesinthe pages 1-2, docampo2024advancesinthe pages 29-30, docampo2024advancesinthe pages 2-4)
2. **Raman-based screening and EBPR improvement:** impactful but currently from a preprint; curate as *uncertain* until peer-reviewed, or curate method node without claiming generalizable performance. (xu2024miningrobustin pages 1-6)
3. **Broad “polyP increases stress tolerance” edges:** widely stated but not always granule-specific; prioritize edges with explicit genes/conditions/phenotypes (e.g., Δppk starvation phenotypes). (baijal2024polyphosphatekinaseregulates pages 1-2, baijal2024polyphosphatekinaseregulates pages 2-3)

## 10) DOI-first bibliography (with URLs and publication dates where available)

**2024–2023 priority**
- Docampo R. *Advances in the cellular biology, biochemistry, and molecular biology of acidocalcisomes.* **Microbiology and Molecular Biology Reviews**. 2024-03. DOI:10.1128/mmbr.00042-23. https://doi.org/10.1128/mmbr.00042-23 (docampo2024advancesinthe pages 1-2)
- Baijal K, et al. *Polyphosphate kinase regulates LPS structure and polymyxin resistance during starvation in E. coli.* **PLOS Biology**. 2024-03. DOI:10.1371/journal.pbio.3002558. https://doi.org/10.1371/journal.pbio.3002558 (baijal2024polyphosphatekinaseregulates pages 20-21)
- Hong Y, et al. *Inhibition of phosphorus removal performance in activated sludge by Fe(III) exposure: transitions in dominant metabolic pathways.* **Frontiers in Microbiology**. 2024-06. DOI:10.3389/fmicb.2024.1424938. https://doi.org/10.3389/fmicb.2024.1424938 (hong2024inhibitionofphosphorus pages 1-2)
- Villard D, et al. *Transcriptional profiling elucidates biofilm functionality in the dynamic environment of an enhanced biological phosphorus removal reactor.* **Water Science & Technology**. 2024-09. DOI:10.2166/wst.2024.314. https://doi.org/10.2166/wst.2024.314 (villard2024transcriptionalprofilingelucidates pages 12-13)
- Corrales D, et al. *Ppx1 putative exopolyphosphatase is essential for polyphosphate accumulation in Lacticaseibacillus paracasei.* **Applied and Environmental Microbiology**. 2024-05. DOI:10.1128/aem.02290-23. https://doi.org/10.1128/aem.02290-23 (corrales2024ppx1putativeexopolyphosphatase pages 1-6)
- Acevedo-López J, et al. *Role of Polyphosphate as an Inorganic Chaperone to Prevent Protein Aggregation Under Copper Stress in Saccharolobus solfataricus.* **Microorganisms**. 2024-12. DOI:10.3390/microorganisms12122627. https://doi.org/10.3390/microorganisms12122627 (acevedolopez2024roleofpolyphosphate pages 1-2)
- Xu J, et al. *Mining robust in situ phosphorus-accumulating organisms via single-cell RACS-Culture for rational ecosystem engineering.* **Research Square** (preprint). 2024-11. DOI:10.21203/rs.3.rs-5292508/v1. https://doi.org/10.21203/rs.3.rs-5292508/v1 (xu2024miningrobustin pages 1-6)
- Schoeppe R, et al. *An update on polyphosphate in vivo activities.* **Biomolecules**. 2024-08. DOI:10.3390/biom14080937. https://doi.org/10.3390/biom14080937 (schoeppe2024anupdateon pages 16-17)
- Iakovchuk N, et al. *Extraordinary physiology of polyphosphate-accumulating Beggiatoa mats suggests a key role for phosphate buffering in marine sediments.* **bioRxiv** (preprint). 2024-11. DOI:10.1101/2024.11.22.624918. https://doi.org/10.1101/2024.11.22.624918 (iakovchuk2024extraordinaryphysiologyof pages 1-4)

**Foundational/high-authority context for definitions and methods**
- Rao NN, Gómez-García MR, Kornberg A. *Inorganic polyphosphate: essential for growth and survival.* **Annual Review of Biochemistry**. 2009-06. DOI:10.1146/annurev.biochem.77.083007.093039. https://doi.org/10.1146/annurev.biochem.77.083007.093039 (rao2009inorganicpolyphosphateessential pages 4-5)
- Moreno SNJ, Docampo R. *Polyphosphate and Its Diverse Functions in Host Cells and Pathogens.* **PLoS Pathogens**. 2013-05. DOI:10.1371/journal.ppat.1003230. https://doi.org/10.1371/journal.ppat.1003230 (moreno2013polyphosphateandits pages 1-2)
- Hupfer M, et al. *Methods for Detection and Quantification of Polyphosphate and Polyphosphate Accumulating Microorganisms in Aquatic Sediments.* **International Review of Hydrobiology**. 2008-02. DOI:10.1002/iroh.200610935. https://doi.org/10.1002/iroh.200610935 (hupfer2008methodsfordetection pages 5-8)



References

1. (docampo2024advancesinthe pages 2-4): Roberto Docampo. Advances in the cellular biology, biochemistry, and molecular biology of acidocalcisomes. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00042-23, doi:10.1128/mmbr.00042-23. This article has 26 citations and is from a domain leading peer-reviewed journal.

2. (rao2009inorganicpolyphosphateessential pages 4-5): Narayana N. Rao, María R. Gómez-García, and Arthur Kornberg. Inorganic polyphosphate: essential for growth and survival. Annual review of biochemistry, 78:605-47, Jun 2009. URL: https://doi.org/10.1146/annurev.biochem.77.083007.093039, doi:10.1146/annurev.biochem.77.083007.093039. This article has 980 citations and is from a domain leading peer-reviewed journal.

3. (moreno2013polyphosphateandits pages 1-2): Silvia N. J. Moreno and Roberto Docampo. Polyphosphate and its diverse functions in host cells and pathogens. PLoS Pathogens, 9:e1003230, May 2013. URL: https://doi.org/10.1371/journal.ppat.1003230, doi:10.1371/journal.ppat.1003230. This article has 117 citations and is from a highest quality peer-reviewed journal.

4. (docampo2024advancesinthe pages 1-2): Roberto Docampo. Advances in the cellular biology, biochemistry, and molecular biology of acidocalcisomes. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00042-23, doi:10.1128/mmbr.00042-23. This article has 26 citations and is from a domain leading peer-reviewed journal.

5. (docampo2024advancesinthe pages 29-30): Roberto Docampo. Advances in the cellular biology, biochemistry, and molecular biology of acidocalcisomes. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00042-23, doi:10.1128/mmbr.00042-23. This article has 26 citations and is from a domain leading peer-reviewed journal.

6. (hupfer2008methodsfordetection pages 5-8): Michael Hupfer, Stefanie Glöss, Peter Schmieder, and Hans‐Peter Grossart. Methods for detection and quantification of polyphosphate and polyphosphate accumulating microorganisms in aquatic sediments. International Review of Hydrobiology, 93:1-30, Feb 2008. URL: https://doi.org/10.1002/iroh.200610935, doi:10.1002/iroh.200610935. This article has 93 citations and is from a peer-reviewed journal.

7. (iakovchuk2024extraordinaryphysiologyof pages 1-4): Nadezhda Iakovchuk, Jenny Fabian, Olaf Dellwig, Christiane Hassenrück, and Heide N. Schulz-Vogt. Extraordinary physiology of polyphosphate-accumulating<i>beggiatoa</i>mats suggests a key role for phosphate buffering in marine sediments. BioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624918, doi:10.1101/2024.11.22.624918. This article has 0 citations.

8. (schoeppe2024anupdateonc pages 1-2): R Schoeppe, M Waldmann, HJ Jessen, and T Renné. An update on polyphosphate in vivo activities. biomolecules 2024, 14, 937. Unknown journal, 2024.

9. (schoeppe2024anupdateonb pages 2-4): R Schoeppe, M Waldmann, HJ Jessen, and T Renné. An update on polyphosphate in vivo activities. biomolecules 2024, 14, 937. Unknown journal, 2024.

10. (schoeppe2024anupdateond pages 2-4): R Schoeppe, M Waldmann, HJ Jessen, and T Renné. An update on polyphosphate in vivo activities. biomolecules 2024, 14, 937. Unknown journal, 2024.

11. (baijal2024polyphosphatekinaseregulates pages 1-2): Kanchi Baijal, Iryna Abramchuk, Carmen M. Herrera, Thien-Fah Mah, M. Stephen Trent, Mathieu Lavallée-Adam, and Michael Downey. Polyphosphate kinase regulates lps structure and polymyxin resistance during starvation in e. coli. PLOS Biology, 22:e3002558, Mar 2024. URL: https://doi.org/10.1371/journal.pbio.3002558, doi:10.1371/journal.pbio.3002558. This article has 8 citations and is from a highest quality peer-reviewed journal.

12. (baijal2024polyphosphatekinaseregulates pages 2-3): Kanchi Baijal, Iryna Abramchuk, Carmen M. Herrera, Thien-Fah Mah, M. Stephen Trent, Mathieu Lavallée-Adam, and Michael Downey. Polyphosphate kinase regulates lps structure and polymyxin resistance during starvation in e. coli. PLOS Biology, 22:e3002558, Mar 2024. URL: https://doi.org/10.1371/journal.pbio.3002558, doi:10.1371/journal.pbio.3002558. This article has 8 citations and is from a highest quality peer-reviewed journal.

13. (corrales2024ppx1putativeexopolyphosphatase pages 1-6): Daniela Corrales, Cristina Alcántara, Manuel Zúñiga, and Vicente Monedero. Ppx1 putative exopolyphosphatase is essential for polyphosphate accumulation in <i>lacticaseibacillus paracasei</i>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.02290-23, doi:10.1128/aem.02290-23. This article has 4 citations and is from a peer-reviewed journal.

14. (ruizhaddadUnknownyearenvironmentalscienceanda pages 1-3): L Ruiz-Haddad, M Ali, M Pronk, and MCM van Loosdrecht. Environmental science and ecotechnology. Unknown journal, Unknown year.

15. (acevedolopez2024roleofpolyphosphate pages 1-2): José Acevedo-López, Gabriela González-Madrid, Claudio A. Navarro, and Carlos A. Jerez. Role of polyphosphate as an inorganic chaperone to prevent protein aggregation under copper stress in saccharolobus solfataricus. Microorganisms, 12:2627, Dec 2024. URL: https://doi.org/10.3390/microorganisms12122627, doi:10.3390/microorganisms12122627. This article has 4 citations.

16. (xu2024miningrobustin pages 1-6): Jian Xu, Jing Xiaoyan, Huihui Pan, Yanhai Gong, Yishang Ren, Liyan Wang, Runzhi Mu, Pengcheng Sun, Zhidian Diao, Yu Meng, Liming Huang, Xixian Wang, Tingbin Zhao, Jia Zhang, Yuetong Ji, Bo Ma, and Yushu Jing. Mining robust in situ phosphorus-accumulating organisms via single-cell racs-culture for rational ecosystem engineering. Unknown journal, Nov 2024. URL: https://doi.org/10.21203/rs.3.rs-5292508/v1, doi:10.21203/rs.3.rs-5292508/v1.

17. (schoeppe2024anupdateon pages 16-17): Robert Schoeppe, Moritz Waldmann, Henning J. Jessen, and Thomas Renné. An update on polyphosphate in vivo activities. Biomolecules, 14:937, Aug 2024. URL: https://doi.org/10.3390/biom14080937, doi:10.3390/biom14080937. This article has 16 citations.

18. (baijal2024polyphosphatekinaseregulates pages 20-21): Kanchi Baijal, Iryna Abramchuk, Carmen M. Herrera, Thien-Fah Mah, M. Stephen Trent, Mathieu Lavallée-Adam, and Michael Downey. Polyphosphate kinase regulates lps structure and polymyxin resistance during starvation in e. coli. PLOS Biology, 22:e3002558, Mar 2024. URL: https://doi.org/10.1371/journal.pbio.3002558, doi:10.1371/journal.pbio.3002558. This article has 8 citations and is from a highest quality peer-reviewed journal.

19. (baijal2024polyphosphatekinaseregulates pages 8-9): Kanchi Baijal, Iryna Abramchuk, Carmen M. Herrera, Thien-Fah Mah, M. Stephen Trent, Mathieu Lavallée-Adam, and Michael Downey. Polyphosphate kinase regulates lps structure and polymyxin resistance during starvation in e. coli. PLOS Biology, 22:e3002558, Mar 2024. URL: https://doi.org/10.1371/journal.pbio.3002558, doi:10.1371/journal.pbio.3002558. This article has 8 citations and is from a highest quality peer-reviewed journal.

20. (baijal2024polyphosphatekinaseregulates pages 9-11): Kanchi Baijal, Iryna Abramchuk, Carmen M. Herrera, Thien-Fah Mah, M. Stephen Trent, Mathieu Lavallée-Adam, and Michael Downey. Polyphosphate kinase regulates lps structure and polymyxin resistance during starvation in e. coli. PLOS Biology, 22:e3002558, Mar 2024. URL: https://doi.org/10.1371/journal.pbio.3002558, doi:10.1371/journal.pbio.3002558. This article has 8 citations and is from a highest quality peer-reviewed journal.

21. (hong2024inhibitionofphosphorus pages 1-2): Yiyihui Hong, Hong Cheng, Xiaoliu Huangfu, Lin Li, and Qiang He. Inhibition of phosphorus removal performance in activated sludge by fe(iii) exposure: transitions in dominant metabolic pathways. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1424938, doi:10.3389/fmicb.2024.1424938. This article has 11 citations and is from a peer-reviewed journal.

22. (achbergerova2011polyphosphatean pages 1-2): Lucia Achbergerová and Jozef Nahálka. Polyphosphate - an ancient energy source and active metabolic regulator. Microbial Cell Factories, 10:63-63, Aug 2011. URL: https://doi.org/10.1186/1475-2859-10-63, doi:10.1186/1475-2859-10-63. This article has 406 citations and is from a peer-reviewed journal.

23. (villard2024transcriptionalprofilingelucidates pages 12-13): Didrik Villard, Lars Snipen, Knut Rudi, Sverre Branders, Torgeir Saltnes, Sondre Eikås, and Wenche Johansen. Transcriptional profiling elucidates biofilm functionality in the dynamic environment of an enhanced biological phosphorus removal reactor. Water Science &amp; Technology, 90:2114-2130, Sep 2024. URL: https://doi.org/10.2166/wst.2024.314, doi:10.2166/wst.2024.314. This article has 3 citations and is from a peer-reviewed journal.

24. (albi2016inorganicpolyphosphatein pages 12-15): Tomás Albi and Aurelio Serrano. Inorganic polyphosphate in the microbial world. emerging roles for a multifaceted biopolymer. World Journal of Microbiology and Biotechnology, Jan 2016. URL: https://doi.org/10.1007/s11274-015-1983-2, doi:10.1007/s11274-015-1983-2. This article has 156 citations and is from a peer-reviewed journal.

25. (quarles2024cryosectioningandimmunofluorescence pages 1-3): Ellen Quarles, Lauren Petreanu, Anjali Narain, Aanchal Jain, Akash Rai, Joyful Wang, Bryndon J. Oleson, and Ursula Jakob. Cryosectioning and immunofluorescence of c. elegans reveals endogenous polyphosphate in intestinal endo-lysosomal organelles. Cell Reports Methods, 4:100879, Oct 2024. URL: https://doi.org/10.1016/j.crmeth.2024.100879, doi:10.1016/j.crmeth.2024.100879. This article has 4 citations.

26. (schoeppe2024anupdateona pages 15-16): R Schoeppe, M Waldmann, HJ Jessen, and T Renné. An update on polyphosphate in vivo activities. biomolecules 2024, 14, 937. Unknown journal, 2024.