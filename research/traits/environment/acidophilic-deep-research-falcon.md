---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:59:56.992664'
end_time: '2026-06-17T21:22:39.772401'
duration_seconds: 1362.78
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: acidophilic
  trait_identifier: METPO:1003003
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: acidophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference in which an organism grows optimally at pH values
    below 5.
  parent_traits: METPO:1003000
  synonyms: acidophil, acidophile
  evidence_summary: 'DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (Supports acidophilic
    growth at strongly acidic external pH.)'
  causal_graph_summary: 'acidophilic_ph_homeostasis: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** acidophilic
- **METPO identifier:** METPO:1003003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values below 5.
- **Parent traits:** METPO:1003000
- **Synonyms:** acidophil, acidophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (Supports acidophilic growth at strongly acidic external pH.)
- **Existing causal graph summary:** acidophilic_ph_homeostasis: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidophilic.yaml`.

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
- **Trait label:** acidophilic
- **METPO identifier:** METPO:1003003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values below 5.
- **Parent traits:** METPO:1003000
- **Synonyms:** acidophil, acidophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (Supports acidophilic growth at strongly acidic external pH.)
- **Existing causal graph summary:** acidophilic_ph_homeostasis: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/acidophilic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **acidophilic** (METPO:1003003)

### Scope summary (trait definition and boundaries)
**Target trait:** *acidophilic* (METPO:1003003) — “a pH growth preference in which an organism grows optimally at pH values below 5.”  Recent synthesis aligned with this scope defines **acidophiles** as having an optimum growth pH <5, and **extreme acidophiles** as having an optimum growth pH <3. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2)  A foundational review similarly uses **pH 1–3** for “extremely acidophilic bacteria,” emphasizing growth (not just survival) at these values. (krulwich2011molecularaspectsof pages 3-5)

**Boundary vs. acid tolerance / acid stress:**
* Acidophily is best treated as a **growth optimum** phenotype, whereas many “acid-stress response” studies test short exposures (e.g., 1 h at pH 3.0) that may not reflect an organism’s optimum. (xu2023transcriptomicandmetabolomic pages 1-2)
* “Moderately acidophilic” or “acid-tolerant” taxa can have broad pH growth ranges (e.g., reported as pH 3–7.5 with optima between pH 4 and 5 in one synthesis), overlapping METPO’s cutoff but differing in optimality and ecological niche. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2)

**Nearby traits to distinguish in curation:**
* **alkaliphilic** (growth at high pH) is mechanistically “opposite” in PMF orientation but shares the principle that Δψ and ΔpH are tuned for homeostasis; thus some nodes/edges (PMF, antiporters) are not acidophile-specific. (krulwich2011molecularaspectsof pages 3-5)
* **acid acclimation** in neutrophiles/pathogens (e.g., *Helicobacter pylori*) may employ specialized mechanisms (UreI-mediated membrane recruitment of urease) that should be curated as **taxon-specific** rather than general acidophily nodes/edges. (krulwich2011molecularaspectsof pages 11-12)

### Key concepts and current mechanistic understanding
Acidophily implies the capacity to **maintain intracellular pH (pHi) near neutral or moderately acidic** while growing in very low external pH. A recurring quantitative anchor is that acidophiles can maintain **internal pH around ~6** while growing at **external pH <3**. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, krulwich2011molecularaspectsof pages 11-12)

A unifying concept is that **pH homeostasis is governed by the two proton motive force (PMF) components**, Δψ (membrane potential) and ΔpH. Under severe pH stress, organisms can show **“reversal” of a PMF component** relative to the usual negative-inside orientation. (krulwich2011molecularaspectsof pages 3-5)

In **extreme acidophiles**, the large inside-alkaline ΔpH is supported by a **reversed (inside-positive) Δψ**, which helps oppose proton influx. (krulwich2011molecularaspectsof pages 11-12)

### Recent developments (2023–2024 prioritized)
**(1) Gene- and MAG-resolved views of acidophile homeostasis in AMD and mine-water treatment contexts.**  Metagenomics/transcriptomics in low-temperature acidic systems highlights recurring modules: K+ uptake (Kdp), Na+/H+ antiport (NhaA), proton efflux ATPases, proton-consuming decarboxylation (adi/gad), urease, and membrane lipid remodeling (hopanoid/cyclopropane fatty acids). (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

**(2) Archaeal membrane biophysics in thermoacidophiles.**  A 2024 mini-review emphasizes that bipolar tetraether lipids (GDGT/GDNT) dominate membranes of thermoacidophiles (pH ≤4; ≥65°C) and that pH-driven compositional changes (cyclopentane rings, GDNT:GDGT ratio, tetraether:diethers, glycosylation) alter membrane packing/hydrogen-bond networks, supporting **low passive proton permeability** and near-neutral pHi. (chong2024archaeamembranesin pages 1-2)

**(3) Multi-omics acid stress models in food-relevant acidophiles.**  For *Alicyclobacillus acidoterrestris* under pH 3.0 stress, integrated transcriptomics/metabolomics supports pHi homeostasis via **enhanced amino-acid decarboxylation, urea hydrolysis, and energy supply**, with additional roles for two-component systems, ABC transporters, and unsaturated fatty acid synthesis. (xu2023transcriptomicandmetabolomic pages 1-2)

**(4) Acidic nitrification ecology in anthropogenic acidic waters.**  In an acid mine lake (pH <5) with **175 mg-N/L ammonium**, nitrification potential and community genetics quantify adaptation: max nitrate production potential **70.5 μg-N/(g-dw·day)**; relative abundances among amoA genes **52% comammox *Nitrospira*** and **41% AOA**. (li2023comammoxnitrospiraand pages 1-2)

### Candidate mechanistic nodes (ontology-grounded where possible)
The node inventory below is organized for direct transfer into a TraitMech-style YAML, with grounding suggestions and supporting sources.

| Node label | Node type | Suggested ontology grounding | Brief role in acidophily | Key supporting source(s) with DOI and year |
|---|---|---|---|---|
| acidophilic growth preference (optimal growth pH <5) | process | METPO:1003003 | Core trait: growth optimum below pH 5; recent review also distinguishes extreme acidophiles with optimum pH <3. | Krulwich 2011 doi:10.1038/nrmicro2549; Dopson 2023 doi:10.3389/fmicb.2023.1149903 (krulwich2011molecularaspectsof pages 3-5, dopson2023eurypsychrophilicacidophilesfrom pages 1-2) |
| extreme acidic environment / low external pH | environmental factor | ENVO:00002009 | Environmental driver selecting for acidophile homeostasis mechanisms; examples include mine drainage and acidic lakes/soils. | Krulwich 2011 doi:10.1038/nrmicro2549; Tonietti 2024 doi:10.3390/microorganisms12122407 (krulwich2011molecularaspectsof pages 3-5, tonietti2024unveilingthebioleaching pages 1-2) |
| acid mine drainage (AMD) | environmental factor | unresolved | Canonical acidic habitat and major application context for acidophiles and aSRB. | Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019; Li 2023 doi:10.1128/aem.00047-23 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2, li2023comammoxnitrospiraand pages 1-2) |
| cytoplasmic pH homeostasis | process | GO:0006885 | Central physiological process allowing near-neutral internal pH despite acidic external pH. | Krulwich 2011 doi:10.1038/nrmicro2549; Xu 2023 doi:10.1128/spectrum.00022-23 (krulwich2011molecularaspectsof pages 3-5, xu2023transcriptomicandmetabolomic pages 1-2) |
| reversed membrane potential (inside-positive Δψ) | process | unresolved | Electrostatic strategy that helps oppose proton influx in extreme acidophiles. | Krulwich 2011 doi:10.1038/nrmicro2549; Dopson 2023 doi:10.3389/fmicb.2023.1149903 (krulwich2011molecularaspectsof pages 11-12, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| proton exclusion / reduced membrane proton permeability | process | unresolved | First-line defense limiting passive proton entry across the cell envelope. | Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019; Chong 2024 doi:10.3389/frbis.2023.1338019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, chong2024archaeamembranesin pages 1-2) |
| proton pumping respiratory chain | pathway | GO:0019646 | Primary active mechanism contributing to PMF and direct proton export/management. | Krulwich 2011 doi:10.1038/nrmicro2549; Tonietti 2024 doi:10.3390/microorganisms12122407 (krulwich2011molecularaspectsof pages 3-5, tonietti2024unveilingthebioleaching pages 1-2) |
| proton-coupled ATPase / ATP synthase | protein | GO:0046933 | Participates in PMF-linked proton translocation; acidophile-affiliated F-type ATPase noted in acidic nitrifier genome. | Krulwich 2011 doi:10.1038/nrmicro2549; Li 2023 doi:10.1128/aem.00047-23 (krulwich2011molecularaspectsof pages 3-5, li2023comammoxnitrospiraand pages 1-2) |
| F1Fo-ATP synthase | protein | GO:0045259 | Acidophile ATP synthase has unusual pH optimum and is implicated in maintaining extreme-acidophile PMF. | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 11-12) |
| cation/proton antiporter | protein | GO:0015385 | Secondary active transporter class exchanging H+ with Na+ or K+ to support pH homeostasis. | Krulwich 2011 doi:10.1038/nrmicro2549; Dopson 2023 doi:10.3389/fmicb.2023.1149903 (krulwich2011molecularaspectsof pages 3-5, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| NhaA Na+/H+ antiporter | gene/protein | unresolved | Specific sodium/proton antiporter repeatedly identified in acidophile genomes/MAGs. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| Kdp potassium uptake system | pathway | unresolved | High-affinity K+ uptake promotes inside-positive potential and K+ homeostasis under acid stress. | Dopson 2023 doi:10.3389/fmicb.2023.1149903; Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) |
| kdpABCDE / kdpDEABC | gene | unresolved | Gene cluster encoding K+-transporting ATPase/signal system enriched in acidophilic genomes and transcripts. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| Kef-type K+ transport system | protein | unresolved | K+ transport system transcribed during ferrous-iron growth in Ferrovum; implicated in pH homeostasis. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| arginine decarboxylase (Adi / speA) | gene/protein | EC:4.1.1.19 | Proton-consuming decarboxylation system that buffers cytoplasm under acid stress. | Dopson 2023 doi:10.3389/fmicb.2023.1149903; Xu 2023 doi:10.1128/spectrum.00022-23 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, xu2023transcriptomicandmetabolomic pages 1-2) |
| glutamate decarboxylase (gadB / gadABC) | gene/protein | EC:4.1.1.15 | Proton-consuming decarboxylation system associated with acid resistance in acidophile genomes. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| phosphatidylserine decarboxylase (panD listed in source) | gene/protein | unresolved | Reported as part of cytoplasmic buffering systems in Ferrovum discussion; treat cautiously because annotation/name may require verification. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| urease system (ureABCDEFGHJ) | pathway | unresolved | Urea hydrolysis consumes acid equivalents/raises pHi; a recurrent acid-homeostasis mechanism. | Dopson 2023 doi:10.3389/fmicb.2023.1149903; Xu 2023 doi:10.1128/spectrum.00022-23 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, xu2023transcriptomicandmetabolomic pages 1-2) |
| urease | protein | EC:3.5.1.5 | Major pH-homeostasis enzyme; classic acid acclimation mechanism and candidate generalizable node. | Krulwich 2011 doi:10.1038/nrmicro2549; Xu 2023 doi:10.1128/spectrum.00022-23 (krulwich2011molecularaspectsof pages 11-12, xu2023transcriptomicandmetabolomic pages 1-2) |
| UreI urea channel | protein | unresolved | Enables rapid membrane-associated urease function in H. pylori; mechanistically strong but likely not general acidophile node. | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 11-12) |
| carbonic anhydrase | protein | EC:4.2.1.1 | Supports pH chemistry in urease-linked acid acclimation system. | Krulwich 2011 doi:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 11-12) |
| cytoplasmic buffering | process | unresolved | Collective buffering by decarboxylation, urea hydrolysis, and metabolites to stabilize pHi. | Krulwich 2011 doi:10.1038/nrmicro2549; Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019 (krulwich2011molecularaspectsof pages 3-5, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) |
| hopanoid lipids | chemical | CHEBI:51963 | Membrane-rigidifying bacterial lipids associated with lower proton permeability in acidophiles. | Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019; Dopson 2023 doi:10.3389/fmicb.2023.1149903 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| squalene-hopene cyclase (shc) | gene/protein | EC:5.4.99.17 | Enzyme in hopanoid biosynthesis associated with membrane adaptation to acidity. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| hpnAIJKNHM hopanoid synthesis genes | gene | unresolved | Gene set supporting hopanoid production and membrane adaptation in acidophilic genomes. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| cyclopropane-fatty-acyl-phospholipid synthase (cfa) | gene/protein | EC:2.1.1.79 | Membrane lipid modification enzyme transcribed in acidophiles and linked to pH homeostasis. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| tetraether lipids (GDGT/GDNT) | chemical | unresolved | Dominant archaeal membrane lipids that reduce passive proton permeability in thermoacidophiles. | Chong 2024 doi:10.3389/frbis.2023.1338019 (chong2024archaeamembranesin pages 1-2) |
| archaeal membrane glycosylation / cyclopentane-ring modulation | process | unresolved | Adjusts hydrogen-bonding and packing in tetraether membranes under acidic conditions. | Chong 2024 doi:10.3389/frbis.2023.1338019 (chong2024archaeamembranesin pages 1-2) |
| Omp40 | protein | unresolved | Membrane protein cited as structural adaptation for proton exclusion. | Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) |
| PspA | protein | UniProt:P0A7K2 | Stress-associated membrane protein cited as structural adaptation for proton exclusion; taxon-specific evidence should be checked. | Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) |
| poly-gamma-glutamate polymer | chemical | CHEBI:52983 | Putative acid-stress-protective polymer found in aSRB proteome analysis. | Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) |
| spermidine | chemical | CHEBI:15729 | Polyamine implicated in acid resistance and inhibition of proton influx via porins. | Dopson 2023 doi:10.3389/fmicb.2023.1149903; Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) |
| ClpXP protease | protein complex | GO:0097038 | Proteostasis/damage-mitigation complex associated with acid resistance in acidophile genomes. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| acid-stable proteins / DNA repair | process | unresolved | Damage-mitigation layer complementing pH homeostasis under low pH and high metal stress. | Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) |
| ferrous iron oxidation pathway | pathway | unresolved | Core metabolism of many biomining acidophiles; couples energy generation to acidic niche occupation. | Tonietti 2024 doi:10.3390/microorganisms12122407; Luo 2024 doi:10.3390/microorganisms12030422 (tonietti2024unveilingthebioleaching pages 1-2, luo2024rolesandregulation pages 1-2) |
| sulfur oxidation pathway | pathway | unresolved | Generates sulfate/acid and supplies energy in bioleaching acidophiles. | Tonietti 2024 doi:10.3390/microorganisms12122407; Luo 2024 doi:10.3390/microorganisms12030422 (tonietti2024unveilingthebioleaching pages 1-2, luo2024rolesandregulation pages 1-2) |
| rusticyanin / rusA-B system | gene/protein | unresolved | Canonical electron-transfer component in ferrous iron oxidation of bioleaching acidophiles. | Luo 2024 doi:10.3390/microorganisms12030422 (luo2024rolesandregulation pages 1-2) |
| Cyc2-like outer membrane cytochrome | protein | unresolved | Ferrous-iron oxidation component repeatedly observed in acidophile genomes. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| petABC complex | gene/protein | unresolved | Electron-transfer genes present in acidophilic iron oxidizers and linked to respiratory adaptation. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| hdrABC complex | gene/protein | unresolved | Sulfur oxidation/electron transfer genes present in acidophilic genomes. | Dopson 2023 doi:10.3389/fmicb.2023.1149903; Luo 2024 doi:10.3390/microorganisms12030422 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, luo2024rolesandregulation pages 1-2) |
| tetrathionate hydrolase (tetH) | gene/protein | EC:3.12.1.1 | Sulfur metabolism enzyme in acidophilic sulfur oxidizers relevant to acidic biomining contexts. | Dopson 2023 doi:10.3389/fmicb.2023.1149903; Luo 2024 doi:10.3390/microorganisms12030422 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, luo2024rolesandregulation pages 1-2) |
| sulfide:quinone reductase (sqr) | gene/protein | EC:1.8.5.4 | Sulfur oxidation enzyme common in acidophilic sulfur oxidizers. | Dopson 2023 doi:10.3389/fmicb.2023.1149903; Luo 2024 doi:10.3390/microorganisms12030422 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, luo2024rolesandregulation pages 1-2) |
| biofilm formation | process | GO:0042710 | Enhances mineral attachment and contact leaching; important for applied acidophile consortia. | Luo 2024 doi:10.3390/microorganisms12030422 (luo2024rolesandregulation pages 1-2) |
| extracellular polymeric substances (EPS) | cellular component | GO:0045226 | Produced during surface attachment/biofilm formation; mediates mineral interaction in bioleaching. | Luo 2024 doi:10.3390/microorganisms12030422 (luo2024rolesandregulation pages 1-2) |
| quorum sensing (QS) | process | GO:0009372 | Regulates morphology, community structure, biofilm formation, and metabolism in bioleaching acidophiles. | Luo 2024 doi:10.3390/microorganisms12030422 (luo2024rolesandregulation pages 1-2) |
| two-component system | pathway | GO:0000160 | Regulatory response layer implicated in acid-stress adaptation in A. acidoterrestris. | Xu 2023 doi:10.1128/spectrum.00022-23 (xu2023transcriptomicandmetabolomic pages 1-2) |
| ABC transporters | pathway | GO:0043190 | Transport functions upregulated/implicated in acid stress responses. | Xu 2023 doi:10.1128/spectrum.00022-23 (xu2023transcriptomicandmetabolomic pages 1-2) |
| unsaturated fatty acid synthesis | pathway | GO:0006636 | Membrane remodeling response contributing to acid stress resistance. | Xu 2023 doi:10.1128/spectrum.00022-23 (xu2023transcriptomicandmetabolomic pages 1-2) |
| bicarbonate production / alkalinization | process | GO:0015701 | In aSRB and related anaerobes, can raise local pH and support persistence in acidic microenvironments. | Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) |
| biogenic sulfide production | process | unresolved | aSRB application-relevant process that precipitates metals during AMD treatment. | Valdez-Nuñez 2024 doi:10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) |
| acidophile-affiliated F-type ATPase | protein | GO:0045259 | Genomic feature associated with adaptation of comammox Nitrospira to acidic mine-lake sediment. | Li 2023 doi:10.1128/aem.00047-23 (li2023comammoxnitrospiraand pages 1-2) |
| low temperature + low pH polyextremophily | environmental factor | unresolved | Combined stress context where acidophile mechanisms interact with cold adaptation. | Dopson 2023 doi:10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 1-2, dopson2023eurypsychrophilicacidophilesfrom media 4830da3a) |
| heap bioleaching system | environmental factor | unresolved | Industrial implementation environment where acidophilic iron/sulfur oxidizers are operationally important. | Jia 2024 doi:10.3390/min14080808 (jia2024multiscaleandtransdisciplinary pages 1-2) |
| Acidithiobacillus ferrooxidans | cellular component | NCBITaxon:920 | Model acidophilic chemolithoautotroph and flagship biomining organism; useful as taxon-specific context node. | Tonietti 2024 doi:10.3390/microorganisms12122407; Krulwich 2011 doi:10.1038/nrmicro2549 (tonietti2024unveilingthebioleaching pages 1-2, krulwich2011molecularaspectsof pages 11-12) |


*Table: This table lists candidate causal-graph nodes for microbial acidophily, grouped implicitly by biological type through the node-type column. It highlights which mechanistic entities are broadly supported across acidophile literature versus those that are taxon-specific or still need grounding before curation.*

### Evidence-backed candidate causal edges (triples)
The table below proposes edge candidates (subject–predicate–object) with a supporting snippet and DOI-first reference, marking uncertainty where evidence is associative or taxon-specific.

| Subject node | Predicate | Object node | Evidence snippet | Reference | Notes/uncertainty |
|---|---|---|---|---|---|
| low external pH / acid challenge | selects for | cytoplasmic pH homeostasis | “A major unifying principle of bacterial pH homeostasis… the demands of pH homeostasis” (krulwich2011molecularaspectsof pages 3-5) | Krulwich et al., 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | General bacterial principle; applicable to acidophiles but not acidophile-exclusive. |
| primary proton pumps / respiratory chain complexes | catalyze active transport of | protons | “primary proton pumps such as the proton-pumping respiratory chain complexes” (krulwich2011molecularaspectsof pages 3-5) | Krulwich et al., 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Broad mechanism-level edge. |
| proton-coupled ATPases | catalyze active transport of | protons | “Such transporters include primary proton pumps such as… proton-coupled ATPases” (krulwich2011molecularaspectsof pages 3-5) | Krulwich et al., 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Broad mechanism-level edge. |
| cation/proton antiporters | exchange | H+ for Na+ or K+ | “cation/proton antiporters, which use the PMF… to energize active proton uptake in exchange for cytoplasmic cations such as Na+ or K+” (krulwich2011molecularaspectsof pages 3-5) | Krulwich et al., 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Broad mechanism; directionality depends on context. |
| reversed Δψ (inside-positive membrane potential) | supports | large inside-alkaline ΔpH | “The large ΔpH of extreme acidophiles… is maintained by active mechanisms and is supported by the reversed Δψ, inside-positive” (krulwich2011molecularaspectsof pages 11-12) | Krulwich et al., 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong for extreme acidophiles. |
| acidophile F1Fo-ATP synthase | has optimum at | alkaline hydrolytic pH | “An acidophile F1Fo-ATP synthase… has a pH optimum of 8.5 for its hydrolytic activity” (krulwich2011molecularaspectsof pages 11-12) | Krulwich et al., 2011, doi:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Biochemical property, not itself sufficient as a causal trait edge. |
| kdp potassium uptake system | contributes to | inversed membrane potential | “the kdp potassium uptake system” among “inversed membrane potential-related” genes (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Dopson et al., 2023, doi:10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Inferred from explicit phrasing; taxon-specific to At. ferrivorans context. |
| potassium transporting ATPase | is involved in | inside positive (inversed) membrane potential | “a potassium transporting ATPase suggested to be involved in the inside positive (inversed) membrane potential” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Dopson et al., 2023, doi:10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Taxon-specific; phrased as suggested. |
| P-type ATPase proton efflux pump | exports | protons | “a P-type ATPase proton efflux pump” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Dopson et al., 2023, doi:10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Taxon-specific genomic evidence. |
| arginine decarboxylase (adi/speA) | consumes | protons | “proton-consuming cytoplasmic buffering systems adi” and “proton-consuming speA arginine decarboxylase” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Dopson et al., 2023, doi:10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Strong mechanistic edge; taxon-specific genomes/transcripts. |
| glutamate decarboxylase (gadB/gadABC) | consumes | protons | “community RNA transcript sequencing… components of the arginine-dependent acid resistance system” and “gadABC glutamate deca…” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Dopson et al., 2023, doi:10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Strong but partly truncated snippet; taxon-specific. |
| ureABCDEFGHJ urease system | contributes to | cytoplasmic buffering | “cytoplasmic buffering systems including… the ureABCDEFGHJ urease system” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Dopson et al., 2023, doi:10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Good candidate edge; genomic/transcriptomic support. |
| hopanoid synthesis genes / hopanoid lipids | decrease | membrane proton permeability | “the membrane hopanoid squalene synthesis and associated genes hpnAIJKNHM” in acidophile adaptations; “hopanoid lipids… are structural adaptations used for proton exclusion” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Dopson et al., 2023, doi:10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903; Valdez-Nuñez et al., 2024, doi:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 | Cross-source support; partly generalized from acidophilic bacteria to candidate node. |
| cyclopropane-fatty-acyl-phospholipid synthase (cfa) | maintains | pH homeostasis | “RNA transcripts… showed maintenance of pH homeostasis including for the cyclopropane-fatty-acyl-phospholipid synthase” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Dopson et al., 2023, doi:10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Expression association, not direct perturbation evidence. |
| bipolar tetraether lipids (GDNT/GDGT) | maintain | low passive proton permeability | “As such, a low passive proton permeability and a near neutral intracellular pH can be maintained” (chong2024archaeamembranesin pages 1-2) | Chong, 2024, doi:10.3389/frbis.2023.1338019, https://doi.org/10.3389/frbis.2023.1338019 | Strong for thermoacidophilic archaea. |
| pH-driven adjustments in GDNT/GDGT ratio, cyclopentane rings, tetraether:diethers, glycosylation | alter | membrane hydrogen-bonding / packing tightness | “These structural and compositional adjustments can alter the hydrogen bond networks… and the packing tightness and rigidity” (chong2024archaeamembranesin pages 1-2) | Chong, 2024, doi:10.3389/frbis.2023.1338019, https://doi.org/10.3389/frbis.2023.1338019 | Useful intermediate mechanistic edge for archaeal branch. |
| hopanoid lipids / Omp40 / PspA | enable | proton exclusion | “hopanoid lipids… or membrane proteins such as Omp40 and PspA, are structural adaptations used for proton exclusion” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Valdez-Nuñez et al., 2024, doi:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 | Generalized from acidophilic bacteria; aSRB relevance partly inferred. |
| pumping K+ and Na+ into cytoplasm | reduces | proton influx | “can pump cations such as K+ and Na+ into the cytoplasm to reduce the influx of protons by electrostatic repulsion” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Valdez-Nuñez et al., 2024, doi:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 | Strong general acidophile mechanism. |
| A. acidoterrestris acid-stress response | enhances | amino acid decarboxylation | “maintains intracellular pH (pHi) homeostasis by enhancing amino acids decarboxylation” (xu2023transcriptomicandmetabolomic pages 1-2) | Xu et al., 2023, doi:10.1128/spectrum.00022-23, https://doi.org/10.1128/spectrum.00022-23 | Strong, but species-specific acid stress rather than broad acidophily. |
| A. acidoterrestris acid-stress response | enhances | urea hydrolysis | “maintains intracellular pH (pHi) homeostasis by enhancing… urea hydrolysis” (xu2023transcriptomicandmetabolomic pages 1-2) | Xu et al., 2023, doi:10.1128/spectrum.00022-23, https://doi.org/10.1128/spectrum.00022-23 | Species-specific acid stress response. |
| A. acidoterrestris acid-stress response | enhances | energy supply | “maintains intracellular pH (pHi) homeostasis by enhancing… energy supply” (xu2023transcriptomicandmetabolomic pages 1-2) | Xu et al., 2023, doi:10.1128/spectrum.00022-23, https://doi.org/10.1128/spectrum.00022-23 | Species-specific, but mechanistically coherent. |
| two-component systems | play crucial roles in | resisting acid stress | “two-component systems, ABC transporters, and unsaturated fatty acid synthesis also play crucial roles in resisting acid stress” (xu2023transcriptomicandmetabolomic pages 1-2) | Xu et al., 2023, doi:10.1128/spectrum.00022-23, https://doi.org/10.1128/spectrum.00022-23 | Edge is broad and response-level. |
| ABC transporters | play crucial roles in | resisting acid stress | “ABC transporters… play crucial roles in resisting acid stress” (xu2023transcriptomicandmetabolomic pages 1-2) | Xu et al., 2023, doi:10.1128/spectrum.00022-23, https://doi.org/10.1128/spectrum.00022-23 | Mechanism not further resolved in retrieved text. |
| unsaturated fatty acid synthesis | contributes to | resisting acid stress | “unsaturated fatty acid synthesis also play crucial roles in resisting acid stress” (xu2023transcriptomicandmetabolomic pages 1-2) | Xu et al., 2023, doi:10.1128/spectrum.00022-23, https://doi.org/10.1128/spectrum.00022-23 | Good membrane-remodeling candidate; species-specific. |
| acidophile-affiliated F-type ATPase | contributes to | adaptation to acidic lake conditions | “contained diverse metal resistance genes and an acidophile-affiliated F-type ATPase” (li2023comammoxnitrospiraand pages 1-2) | Li et al., 2023, doi:10.1128/aem.00047-23, https://doi.org/10.1128/aem.00047-23 | Genomic association only; causal direction inferred. |
| quorum sensing | regulates | biofilm formation | “QS has been confirmed to regulate bioleaching, including… biofilm formation” (luo2024rolesandregulation pages 1-2) | Luo et al., 2024, doi:10.3390/microorganisms12030422, https://doi.org/10.3390/microorganisms12030422 | Strong review-level statement for applied acidophiles. |
| attached bacterial cells | produce | extracellular polymers (EPS) | “Bacterial cells attached to surfaces produce extracellular polymers (EPS) associated with biofilm formation” (luo2024rolesandregulation pages 1-2) | Luo et al., 2024, doi:10.3390/microorganisms12030422, https://doi.org/10.3390/microorganisms12030422 | Good application-focused edge. |
| cell attachment to solid surfaces | initiates | bioleaching / mineralization process | “The attachment of cells to solid surfaces is an essential step in initiating bioleaching” (luo2024rolesandregulation pages 1-2) | Luo et al., 2024, doi:10.3390/microorganisms12030422, https://doi.org/10.3390/microorganisms12030422 | Application edge rather than core acidophily mechanism. |
| Acidithiobacillus ferrooxidans | generates | iron(III) ions in oxic conditions | “A. ferrooxidans catalyzes the extraction of elements by generating iron (III) ions in oxic conditions” (tonietti2024unveilingthebioleaching pages 1-2) | Tonietti et al., 2024, doi:10.3390/microorganisms12122407, https://doi.org/10.3390/microorganisms12122407 | Strong application edge for biomining. |
| iron(III) ions | react with | metal sulfides | “iron (III) ions in oxic conditions, which are able to react with metal sulfides” (tonietti2024unveilingthebioleaching pages 1-2) | Tonietti et al., 2024, doi:10.3390/microorganisms12122407, https://doi.org/10.3390/microorganisms12122407 | Central bioleaching chemistry edge. |
| acidophilic iron- and sulfur-oxidizing microbes | expanded use of | heap leaching for sulfide ores | “With the discovery of acidophilic iron- and sulfur-oxidizing microbes, heap leaching expanded to include the processing of sulfide ores” (jia2024multiscaleandtransdisciplinary pages 1-2) | Jia et al., 2024, doi:10.3390/min14080808, https://doi.org/10.3390/min14080808 | Historical/industrial application edge. |
| acidophilic sulphate-reducing bacteria | produce | biogenic sulphide | “their ability to produce biogenic sulphide and precipitate metals” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | Valdez-Nuñez et al., 2024, doi:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 | Strong application edge for AMD treatment. |
| biogenic sulphide | precipitates | metals | “produce biogenic sulphide and precipitate metals” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | Valdez-Nuñez et al., 2024, doi:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 | Mechanistically important for remediation branch. |
| bicarbonate production / alkalinization | increases | pH of microenvironment | “increasing the pH of their microenvironment through bicarbonate production (alkalinization)” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Valdez-Nuñez et al., 2024, doi:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 | Especially relevant to acidophilic SRB microenvironments. |


*Table: This table compiles evidence-backed causal edges that could seed a TraitMech graph for acidophily. It spans core pH-homeostasis mechanisms, membrane/lipid adaptations, transporters, buffering reactions, and applied biomining/AMD-remediation processes using only retrieved source text.*

### Current applications and real-world implementations (with quantitative data)

#### 1) Biomining/bioleaching (industrial and pilot)
* **Heap leaching scale:** A 2024 review states that heap leaching “accounts for approximately **20% of global copper production**.” (jia2024multiscaleandtransdisciplinary pages 1-2)
* **Core bioleaching chemistry:** *Acidithiobacillus ferrooxidans* catalyzes element extraction “by generating iron (III) ions in oxic conditions,” and Fe(III) reacts with metal sulfides—central to indirect leaching. (tonietti2024unveilingthebioleaching pages 1-2)
* **Commercial and near-commercial yields / throughput:** A 2023 critical review reports commercial bioleaching outcomes such as “up to **95% Au**” extraction; “Cu yields… up to **65%** from chalcopyrite and up to **98%** from some sulfosalts (enargite)”; and molybdenite bioleaching “around **85% Mo**” over a **six-month** timeframe using *A. ferrooxidans* and *L. ferrooxidans*. It also reports a BioCOP™ process producing “**20000 Mg/year Cu**” and typical heap operations over “a **400–600-day** period” (with “preconditioning… **1–6 weeks**”). (funari2023urbanminingof pages 20-22)
* **Process-level optimization and EPS/biofilm:** The same review links EPS/biofilms to contact leaching and stress resistance (“EPS allow contact and mineral decomposition”; “EPS and biofilm formation might also improve strain resistance”). (funari2023urbanminingof pages 20-22)  A 2024 biomining review additionally notes EPS-mediated adsorption/leaching through metal–ligand complexes. (cozma2024biorecoveryofmetals pages 10-11)
* **Example quantitative improvements (consortia/pilot):** A 2024 circularity-focused biomining review reports a consortium (*A. ferrooxidans* + *A. thiooxidans*) reaching **70%** in **35 days** vs **35%** in 35 days (context: copper removal/bioleaching comparison in that review), and notes an “**21.1% higher**” efficiency vs sulfuric-acid chemical leaching in a mixed consortium scenario. (cozma2024biorecoveryofmetals pages 10-11)  Pilot conditions and yields reported include operations at **pH 2.0** and metal extraction values such as Zn **97.08%**, Cu **79.11%** at 2.5% (w/v) pulp density over **42 days** in one pilot configuration. (cozma2024biorecoveryofmetals pages 19-20)

#### 2) AMD treatment and resource recovery with acidophilic sulfate reducers (aSRB)
* **Community shifts in acidic bioreactors:** In AMD-treatment bioreactors operating at **pH 2.5–3.5** (filled with sediments of **pH 2.0**), *Desulfosporosinus* exceeded **>55%** of the total community. In passive bioreactors treating AMD (pH **3.4–3.7**), taxa initially at **0.0025%–0.0093%** in AMD became **27.3%–87.0%** of SRB-like populations. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
* **Mechanism-to-application link:** aSRB produce **biogenic sulfide** that can **precipitate metals**, and can raise local pH via alkalinization (bicarbonate production), motivating their use in AMD treatment and circular recovery of metal sulfides/nanoparticles. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

#### 3) Acidic nitrogen cycling as an “application-adjacent” implementation (monitoring/management)
In the acid mine lake study above, the high ammonium load (**175 mg-N/L**) plus measurable nitrate production potential (**70.5 μg-N/(g-dw·day)**) and amoA distributions quantify nitrification functioning under acidic constraints relevant to mine-water monitoring and management. (li2023comammoxnitrospiraand pages 1-2)

### Expert synthesis (authoritative opinions/analysis)
Two consistent expert-level conclusions emerge across authoritative reviews:
1) Acidophily is not a single mechanism but a **systems property** combining reduced proton permeability, PMF tuning (including Δψ inversion), proton export, and proton-consuming buffering reactions—often constitutively expressed in extremophiles at energetic cost. (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 11-12)
2) In industrial bioleaching, **community behaviors** (biofilm/EPS; quorum sensing) are increasingly treated as manipulable “control knobs” for process optimization (e.g., proposals to add signaling molecules to increase leaching rates), extending beyond single-organism physiology. (luo2024rolesandregulation pages 1-2)

### Quantitative/statistical anchors for curation
* **Definitions / ranges**: acidophiles optimum pH <5; extreme acidophiles optimum pH <3; extremely acidophilic bacteria grow at pH **1–3**. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2, krulwich2011molecularaspectsof pages 3-5)
* **Trait boundary figure**: Dopson et al. Figure 3 (pH vs temperature optima/ranges for characterized eurypsychrophilic acidophiles) can be used to curate empirical pH-optimum/range constraints and to connect acidophily with polyextremophily at low temperature. (dopson2023eurypsychrophilicacidophilesfrom media 4830da3a)
* **Intracellular pH**: acidophiles maintain internal pH ~**6.0** while growing at external pH <3.0. (krulwich2011molecularaspectsof pages 11-12, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
* **Industrial scale**: heap leaching ~**20%** of global copper production. (jia2024multiscaleandtransdisciplinary pages 1-2)
* **Bioleaching performance**: up to **95% Au**; Cu up to **65%** (chalcopyrite) and **98%** (enargite); ~**85% Mo** over **6 months**; BioCOP™ **20000 Mg/year Cu**; heap duration **400–600 days**. (funari2023urbanminingof pages 20-22)
* **AMD bioreactors**: *Desulfosporosinus* shifts from rare (0.0025–0.0093%) to dominant (27.3–87.0% of SRB-like), and can reach >55% in low-pH bioreactors. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
* **Acid mine lake nitrification**: NH4+ **175 mg-N/L**; nitrate production potential **70.5 μg-N/(g-dw·day)**; amoA relative abundance **52%** comammox and **41%** AOA. (li2023comammoxnitrospiraand pages 1-2)

### Warnings / “do not curate yet” flags
1) **Taxon-specific acid acclimation modules** (e.g., *H. pylori* UreI-dependent membrane recruitment of urease and specific two-component regulators) are mechanistically strong but likely **not transferable** as general acidophily nodes/edges without additional cross-taxon evidence. (krulwich2011molecularaspectsof pages 11-12)
2) Several gene mentions in environmental genomics sources are **association/evidence-of-presence** rather than perturbation evidence (e.g., “suggested to be involved” for potassium transporting ATPase; “acidophile-affiliated” ATPase). Curate these as **uncertain edges** or as candidate nodes pending causal validation. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, li2023comammoxnitrospiraand pages 1-2)
3) Some annotations may require validation prior to ontology grounding (e.g., “panD phosphatidylserine decarboxylase” as written in one review excerpt). Treat as “label-only” until checked against genome annotation/EC mapping. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

---

## DOI-first bibliography (with URLs and publication dates)

1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology* (May 2011). DOI: **10.1038/nrmicro2549**. URL: https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 11-12)
2. Dopson M, González-Rosales C, Holmes DS, Mykytczuk N. **Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies.** *Frontiers in Microbiology* (Mar 2023). DOI: **10.3389/fmicb.2023.1149903**. URL: https://doi.org/10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom pages 1-2, dopson2023eurypsychrophilicacidophilesfrom media 4830da3a)
3. Chong PL-G. **Archaea membranes in response to extreme acidic environments.** *Frontiers in Biophysics* (Published 04 Jan 2024). DOI: **10.3389/frbis.2023.1338019**. URL: https://doi.org/10.3389/frbis.2023.1338019 (chong2024archaeamembranesin pages 1-2)
4. Valdez-Nuñez LF, Kappler A, Ayala-Muñoz D, Chávez IJ, Mansor M. **Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.** *Environmental Microbiology Reports* (Oct 2024). DOI: **10.1111/1758-2229.70019**. URL: https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
5. Xu J, Zhao N, Meng X, et al. **Transcriptomic and Metabolomic Profiling Uncovers Response Mechanisms of Alicyclobacillus acidoterrestris DSM 3922T to Acid Stress.** *Microbiology Spectrum* (Published 15 Jun 2023; corrected 22 Jun 2023). DOI: **10.1128/spectrum.00022-23**. URL: https://doi.org/10.1128/spectrum.00022-23 (xu2023transcriptomicandmetabolomic pages 1-2)
6. Li D, Ren Z, Zhou Y, et al. **Comammox Nitrospira and Ammonia-Oxidizing Archaea Are Dominant Ammonia Oxidizers in Sediments of an Acid Mine Lake Containing High Ammonium Concentrations.** *Applied and Environmental Microbiology* (Published 13 Mar 2023). DOI: **10.1128/aem.00047-23**. URL: https://doi.org/10.1128/aem.00047-23 (li2023comammoxnitrospiraand pages 1-2)
7. Luo W, Li Y, Chen S, Liang Y, Liu X. **Roles and Regulation of Quorum Sensing of Acidophiles in Bioleaching: A Review.** *Microorganisms* (Published 20 Feb 2024). DOI: **10.3390/microorganisms12030422**. URL: https://doi.org/10.3390/microorganisms12030422 (luo2024rolesandregulation pages 1-2)
8. Jia Y, Ruan R, Qu J, et al. **Multi-Scale and Trans-Disciplinary Research and Technology Developments of Heap Bioleaching.** *Minerals* (Published 10 Aug 2024). DOI: **10.3390/min14080808**. URL: https://doi.org/10.3390/min14080808 (jia2024multiscaleandtransdisciplinary pages 1-2)
9. Tonietti L, Esposito M, Cascone M, et al. **Unveiling the Bioleaching Versatility of Acidithiobacillus ferrooxidans.** *Microorganisms* (Published 23 Nov 2024). DOI: **10.3390/microorganisms12122407**. URL: https://doi.org/10.3390/microorganisms12122407 (tonietti2024unveilingthebioleaching pages 1-2)
10. Funari V, Toller S, Vitale L, Santos RM, Gomes HI. **Urban mining of municipal solid waste incineration (MSWI) residues with emphasis on bioleaching technologies: a critical review.** *Environmental Science and Pollution Research* (Apr 2023). DOI: **10.1007/s11356-023-26790-z**. URL: https://doi.org/10.1007/s11356-023-26790-z (funari2023urbanminingof pages 20-22)
11. Cozma P, Bețianu C, Hlihor R-M, Simion IM, Gavrilescu M. **Bio-Recovery of Metals through Biomining within Circularity-Based Solutions.** *Processes* (Aug 2024). DOI: **10.3390/pr12091793**. URL: https://doi.org/10.3390/pr12091793 (cozma2024biorecoveryofmetals pages 10-11, cozma2024biorecoveryofmetals pages 19-20)


References

1. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

3. (xu2023transcriptomicandmetabolomic pages 1-2): Junnan Xu, Ning Zhao, Xuemei Meng, Jun Li, Tong Zhang, Ruoyun Xu, Xinyuan Wei, and Mingtao Fan. Transcriptomic and metabolomic profiling uncovers response mechanisms of alicyclobacillus acidoterrestris dsm 3922 <sup>t</sup> to acid stress. Microbiology Spectrum, Aug 2023. URL: https://doi.org/10.1128/spectrum.00022-23, doi:10.1128/spectrum.00022-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 11-12): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

5. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

6. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

7. (chong2024archaeamembranesin pages 1-2): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 9 citations.

8. (li2023comammoxnitrospiraand pages 1-2): Deyong Li, Zhichang Ren, Yangqi Zhou, Lugao Jiang, Min Zheng, and Guoqiang Liu. Comammox <i>nitrospira</i> and ammonia-oxidizing archaea are dominant ammonia oxidizers in sediments of an acid mine lake containing high ammonium concentrations. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.00047-23, doi:10.1128/aem.00047-23. This article has 32 citations and is from a peer-reviewed journal.

9. (tonietti2024unveilingthebioleaching pages 1-2): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 45 citations.

10. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

11. (luo2024rolesandregulation pages 1-2): Wang Luo, Yiran Li, Shiqi Chen, Yili Liang, and Xue-duan Liu. Roles and regulation of quorum sensing of acidophiles in bioleaching: a review. Microorganisms, 12:422, Feb 2024. URL: https://doi.org/10.3390/microorganisms12030422, doi:10.3390/microorganisms12030422. This article has 16 citations.

12. (dopson2023eurypsychrophilicacidophilesfrom media 4830da3a): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

13. (jia2024multiscaleandtransdisciplinary pages 1-2): Yan Jia, Renman Ruan, Jingkui Qu, Qiaoyi Tan, Heyun Sun, and Xiaopeng Niu. Multi-scale and trans-disciplinary research and technology developments of heap bioleaching. Minerals, 14:808, Aug 2024. URL: https://doi.org/10.3390/min14080808, doi:10.3390/min14080808. This article has 13 citations.

14. (funari2023urbanminingof pages 20-22): Valerio Funari, Simone Toller, Laura Vitale, Rafael M. Santos, and Helena I. Gomes. Urban mining of municipal solid waste incineration (mswi) residues with emphasis on bioleaching technologies: a critical review. Environmental Science and Pollution Research, 30:59128-59150, Apr 2023. URL: https://doi.org/10.1007/s11356-023-26790-z, doi:10.1007/s11356-023-26790-z. This article has 36 citations and is from a peer-reviewed journal.

15. (cozma2024biorecoveryofmetals pages 10-11): Petronela Cozma, Camelia Bețianu, Raluca-Maria Hlihor, Isabela Maria Simion, and Maria Gavrilescu. Bio-recovery of metals through biomining within circularity-based solutions. Processes, 12:1793, Aug 2024. URL: https://doi.org/10.3390/pr12091793, doi:10.3390/pr12091793. This article has 25 citations.

16. (cozma2024biorecoveryofmetals pages 19-20): Petronela Cozma, Camelia Bețianu, Raluca-Maria Hlihor, Isabela Maria Simion, and Maria Gavrilescu. Bio-recovery of metals through biomining within circularity-based solutions. Processes, 12:1793, Aug 2024. URL: https://doi.org/10.3390/pr12091793, doi:10.3390/pr12091793. This article has 25 citations.