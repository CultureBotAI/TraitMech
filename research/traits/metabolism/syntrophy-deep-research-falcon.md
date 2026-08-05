---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:01:24.330453'
end_time: '2026-08-04T07:10:16.262961'
duration_seconds: 531.93
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: Syntrophy
  trait_identifier: METPO:1002006
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: syntrophy
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which the metabolism of one species is thermodynamically
    dependent on the removal of its products by another species.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2166: Interspecies electron transfer is a
    key process (Review supports hydrogen/formate-mediated electron transfer in syntrophic
    communities.)'
  causal_graph_summary: 'syntrophy_interspecies_electron_transfer: 16 nodes, 14 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 61
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Syntrophy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1002006
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which the metabolism of one species is thermodynamically dependent on the removal of its products by another species.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2166: Interspecies electron transfer is a key process (Review supports hydrogen/formate-mediated electron transfer in syntrophic communities.)
- **Existing causal graph summary:** syntrophy_interspecies_electron_transfer: 16 nodes, 14 edges

## Research Objective

Research the microbial trait **Syntrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/syntrophy.yaml`.

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
- **Trait label:** Syntrophy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1002006
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which the metabolism of one species is thermodynamically dependent on the removal of its products by another species.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2166: Interspecies electron transfer is a key process (Review supports hydrogen/formate-mediated electron transfer in syntrophic communities.)
- **Existing causal graph summary:** syntrophy_interspecies_electron_transfer: 16 nodes, 14 edges

## Research Objective

Research the microbial trait **Syntrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/syntrophy.yaml`.

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


# Curation-focused research report: Syntrophy

## Executive summary

**Target trait:** Syntrophy  
**Trait identifier:** **METPO:1002006**  
**Category:** METABOLISM; **term kind:** CLASS; **mapping:** REVIEWED  
**Parent:** METPO:1000060

For TraitMech purposes, syntrophy should be modeled as a **community-dependent metabolic capacity**, not simply metabolite exchange. Its defining feature is that one organism’s reaction is thermodynamically feasible only because another organism removes products or accepts electrons. In classical methanogenic syntrophy, bacteria oxidize fatty acids or alcohols to acetate, H₂, and/or formate, while methanogens maintain sufficiently low H₂/formate activities and convert the products to CH₄ and CO₂. This is consistent with the supplied definition and the foundational interspecies-electron-transfer interpretation of DOI [10.1038/nrmicro2166](https://doi.org/10.1038/nrmicro2166). Recent literature recognizes both mediated interspecies electron transfer through H₂/formate and direct interspecies electron transfer (DIET). (muller2010syntrophicbutyrateand pages 1-2, nozhevnikova2020syntrophyandinterspecies pages 1-2, jin2023syntrophicpropionateoxidation pages 1-2)

The most defensible core graph is therefore:

> **partner consumption of H₂/formate or electrons → lower product activity/redox constraint → favorable syntroph reaction energetics → substrate oxidation and partner growth → methane or other terminal-reduction products.**

## 1. Trait scope and boundary cases

### 1.1 Included phenotype

The trait denotes the capacity to participate in a tightly coupled metabolism in which:

1. a **producer/oxidizer** carries out an otherwise endergonic or marginally exergonic reaction;
2. a **partner** continuously consumes a reaction product or directly accepts electrons;
3. product removal changes Gibbs energy sufficiently to permit energy conservation and growth; and
4. the coupled community accomplishes a conversion that the individual partners cannot accomplish under the same conditions.

Recent expert framing describes syntrophy as an “energetically limited mutualistic interaction” in which exchanged H₂ and formate must remain low. Known syntrophs characteristically grow slowly and inhabit the “rare biosphere” because reactions operate close to the minimum energy required for ATP synthesis. (jin2023syntrophicpropionateoxidation pages 1-2)

### 1.2 Obligately versus facultatively syntrophic organisms

**Obligate syntrophs** cannot perform the focal conversion without a product-scavenging partner. *Pelotomaculum schinkii*, for example, cannot grow on propionate alone. **Facultative syntrophs** perform the conversion syntrophically under methanogenic conditions but may grow independently through fermentation or respiration when sulfate, fumarate, or another acceptor is available. Among ten cultivated propionate-oxidizing species summarized in 2023, only a minority were obligate syntrophs; many could use sulfate or fumarate in pure culture. (muller2018syntrophyinmethanogenic pages 14-16, jin2023syntrophicpropionateoxidation pages 1-2)

The trait can consequently be asserted at different levels:

- **organism-level capacity:** demonstrated growth or activity in a defined syntrophic coculture;
- **community phenotype:** coupled substrate conversion requiring two or more populations;
- **conditional capacity:** syntrophy only under specified electron-acceptor, product-concentration, pH, or temperature conditions.

### 1.3 Excluded or separate nearby phenomena

Do **not** equate syntrophy with:

- generic cross-feeding in which both reactions remain independently favorable;
- ordinary mutualism, commensalism, coaggregation, or community co-occurrence;
- a fermenter producing a metabolite that another organism happens to consume without demonstrated thermodynamic dependence;
- respiratory propionate oxidation by a facultative syntroph using sulfate or fumarate in pure culture;
- intracellular hydrogen cycling within one organism;
- long-distance electron transport within a cable bacterium, which is an intracellular/multicellular electron-conduction phenotype rather than interspecies syntrophy;
- DIET inferred solely from addition of a conductive material or enrichment of electroactive taxa.

Anaerobic methane oxidation by ANME archaea and sulfate-reducing bacteria is within the broad trait only when partner dependence is demonstrated. Its mechanism may be DIET, diffusible shuttles, or interspecies sulfur transfer and should be represented as mechanism-specific subgraphs rather than collapsed into classical H₂/formate syntrophy. (zhuang2024electrontransferin pages 6-8, zhuang2024electrontransferin pages 5-6)

## 2. Candidate graph nodes grouped by type

Identifiers below are deliberately conservative. Labels without a CURIE require ontology lookup during YAML curation.

### 2.1 Trait and biological-process nodes

- Syntrophy — **METPO:1002006**
- Interspecies hydrogen transfer
- Interspecies formate transfer
- Direct interspecies electron transfer (DIET)
- Flavin-based electron bifurcation/confurcation (FBEB/C)
- Reverse electron transport
- Syntrophic propionate oxidation
- Syntrophic butyrate oxidation
- Syntrophic acetate oxidation
- Hydrogenotrophic methanogenesis
- Acetoclastic methanogenesis
- Anaerobic oxidation of methane
- Sulfate reduction
- Homoacetogenesis
- Anaerobic digestion

### 2.2 Pathways and metabolic modules

- Methylmalonyl-CoA (MMC) propionate-oxidation pathway
- C6 dismutation/*Smithella* pathway
- β-oxidation module for butyrate
- Wood–Ljungdahl pathway and its reverse in syntrophic acetate oxidation
- Methanogenesis pathway
- Quinone/menaquinone-linked electron-transport module
- Rnf ferredoxin:NAD⁺ oxidoreductase module
- HydABC electron-bifurcating hydrogenase module
- EtfAB–acyl-CoA dehydrogenase module

The C6 route produces approximately one H₂ per propionate, versus three H₂/formate equivalents for the MMC reaction, and is consequently modeled as less sensitive to H₂ accumulation. However, the enzyme catalyzing formation of the initial C6 intermediate remains unknown. (jin2023syntrophicpropionateoxidation pages 5-7, jin2023syntrophicpropionateoxidation pages 9-10)

### 2.3 Chemicals, substrates, carriers, products, and inhibitors

- Hydrogen — **CHEBI:15378**
- Formate — **CHEBI:15740**
- Propionate; butyrate; acetate; succinate; fumarate; malate; oxaloacetate
- Carbon dioxide; methane; water; protons
- NAD⁺/NADH; NADP⁺/NADPH
- Oxidized/reduced ferredoxin
- Menaquinone/menaquinol
- Coenzyme A and acyl-CoA intermediates
- Sulfate; sulfide; nitrate
- Ammonia/ammonium
- Conductive materials: magnetite, activated carbon, graphene, biochar, magnetic biochar
- Artificial electron shuttles such as AQDS and humic substances

### 2.4 Genes, proteins, enzymes, and complexes

- **HydABC**, electron-bifurcating [FeFe]-hydrogenase
- [FeFe]-, [NiFe]-, and [Fe]-hydrogenases
- Formate dehydrogenases: FDH1–FDH4; **fdhA**, **fdhB** where taxonomically appropriate
- **EtfAB**, electron-transferring flavoprotein
- Butyryl-CoA dehydrogenase
- Rnf complex
- Succinate dehydrogenase/fumarate reductase components **SdhA/SdhB**
- Fumarate reductase-like **TfrA/TfrB**
- Malate dehydrogenase and malate:quinone oxidoreductase, **mdh/mqo**
- Periplasmic cytochrome b:quinone oxidoreductase and cytochrome c₃
- Multiheme c-type cytochromes
- PilA/electrically conductive pili or nanowires
- Methyl-coenzyme M reductase, **mcr**
- Carbon monoxide dehydrogenase/acetyl-CoA synthase and **cdh**-associated functions
- Formyltetrahydrofolate synthetase

HydABC is supported by 2023 cryo-EM, mutagenesis, spectroscopy, functional assays, and molecular simulation. It uses an FMN-centered kinetic gate to couple exergonic NAD(P)⁺ reduction with endergonic ferredoxin reduction. This is strong evidence for the molecular feasibility of electron bifurcation, but the experiment used acetogens *Acetobacterium woodii* and *Thermoanaerobacter kivui*, not a canonical syntrophic coculture; it therefore supports the mechanism rather than the syntrophy trait by itself. (katsyv2023molecularbasisof pages 1-2)

### 2.5 Organisms and partner roles

**Propionate/butyrate oxidizers:**

- *Syntrophobacter/Syntrophobacterium fumaroxidans*
- *Syntrophobacter wolinii*
- *Smithella propionica*
- *Pelotomaculum schinkii*
- *Pelotomaculum thermopropionicum*
- *Syntrophomonas wolfei*
- *Syntrophus aciditrophicus*

A 2023 review recognized only **10 cultivated bacterial species** capable of syntrophic propionate oxidation, distributed among six genera, underscoring how sparse direct physiological evidence remains. (jin2023syntrophicpropionateoxidation pages 1-2)

**Methanogenic partners:**

- *Methanobacterium formicicum*
- *Methanoculleus* spp.
- *Methanospirillum hungatei*
- *Methanothrix* spp.
- *Methanosarcina* spp.

**DIET/sulfur-cycle examples:**

- ANME-1 or ANME-2 archaea with sulfate-reducing bacteria
- *Candidatus Desulfofervidus auxilii* (HotSeep-1)
- *Candidatus Syntrophoarchaeum*
- *Candidatus Ethanoperedens thermophilum*
- *Geobacter sulfurreducens* with *Prosthecochloris aestuarii*

These should be grounded to NCBITaxon only after confirming the current accepted taxon and identifier.

### 2.6 Environmental and experimental nodes

- Anoxic/anaerobic environment
- Hydrogen partial pressure
- Formate concentration
- Neutral to weakly alkaline pH
- Temperature
- Sulfate concentration
- Carbon-dioxide activity
- Ammonia concentration
- Organic loading rate
- Granule/biofilm spatial structure and interspecies distance
- Conductive-material amendment
- Coculture versus monoculture
- DNA/RNA stable-isotope probing and SIP-metagenomics

## 3. Candidate causal edges

The following table provides curation-ready triples, evidence type, DOI, supporting snippet, and scope warnings.

| Subject (CURIE/label) | Predicate | Object (CURIE/label) | Evidence strength/scope | DOI | Short supporting snippet | Curation notes/uncertainty |
|---|---|---|---|---|---|---|
| Syntrophy (METPO:1002006) | requires removal of | CHEBI:15378 hydrogen; CHEBI:15740 formate | Strong; foundational reviews, broad across methanogenic syntrophy | 10.1111/j.1758-2229.2010.00147.x; 10.1128/aem.00384-23 | “intermediates they exchanged must be kept at a low level for efficient cooperation”; oxidation becomes feasible only when methanogens maintain low H2/formate | Core defining edge for trait scope; broad and curatable at class level (muller2010syntrophicbutyrateand pages 1-2, jin2023syntrophicpropionateoxidation pages 1-2) |
| Low hydrogen/formate concentration | enables | syntrophic propionate oxidation via methylmalonyl-CoA pathway | Strong; review consensus | 10.1007/978-3-319-98836-8_9; 10.1128/aem.00384-23 | “all propionate degraders use the methylmalonyl-CoA pathway”; reoxidation to H2/formate “requires that H2 or formate be kept at sufficiently low concentrations” | Use pathway-level node if gene-level grounding is incomplete (muller2018syntrophyinmethanogenic pages 14-16, jin2023syntrophicpropionateoxidation pages 5-7) |
| Low hydrogen/formate concentration | enables | syntrophic butyrate oxidation | Strong; review consensus | 10.1111/j.1758-2229.2010.00147.x; 10.1111/1758-2229.12524 | butyrate oxidation is endergonic under standard conditions and needs low H2/formate; habitat H2 partial pressures of “10^-4 to 10^-5 atm” are relevant | Good class-level edge; quantitative threshold varies by system (muller2010syntrophicbutyrateand pages 1-2, schink2017hydrogenorformate pages 7-10) |
| Syntrophic propionate oxidation | proceeds via | methylmalonyl-CoA pathway | Strong; 2023 review plus foundational review | 10.1128/aem.00384-23; 10.1007/978-3-319-98836-8_9 | “Most of these organisms utilize either the methylmalonyl-CoA (MMC) pathway or the C6 dismutation pathway” | Broad but mainly established for known SPOB taxa, not necessarily all syntrophs (jin2023syntrophicpropionateoxidation pages 1-2, muller2018syntrophyinmethanogenic pages 14-16) |
| Syntrophic propionate oxidation | can proceed via | C6 dismutation pathway | Strong; review, pathway accepted but first step unresolved | 10.1128/aem.00384-23 | “Most of these organisms utilize either the methylmalonyl-CoA (MMC) pathway or the C6 dismutation pathway”; “formation of the C6 intermediate… remains unknown” | Curate pathway existence, but avoid enzyme for first C6-forming step until identified (jin2023syntrophicpropionateoxidation pages 1-2, jin2023syntrophicpropionateoxidation pages 9-10) |
| Methanogens | consume | hydrogen/formate produced by syntrophs | Strong; broad reviews | 10.1007/978-3-319-98836-8_9; 10.3390/w16243551 | “H2 and formate, as electron carriers, were continuously consumed by the methanogens to keep the oxidation of the VFAs going” | Central cross-partner edge; applies especially to hydrogenotrophic methanogens (muller2018syntrophyinmethanogenic pages 1-4, li2024promotingorinhibiting pages 1-2) |
| Reversed electron transport | enables | H2/formate production during syntrophic butyrate/propionate oxidation | Strong; foundational mechanistic reviews | 10.1111/j.1758-2229.2010.00147.x; 10.1007/978-3-319-98836-8_9 | “requiring energy-dependent reversed electron transport”; “reversed electron transport as a universal feature of syntrophically fermenting bacteria” | Mechanistic edge is robust; exact complexes differ by taxon (muller2010syntrophicbutyrateand pages 1-2, muller2018syntrophyinmethanogenic pages 6-9) |
| Flavin-based electron bifurcation/confurcation | facilitates | low-potential H2/formate formation under syntrophic conditions | Strong; 2023 review, broad inference from genomes/biochemistry | 10.1128/aem.00384-23 | “FBEB/C systems have been proposed to help solve the thermodynamic dilemma during the formation of the low-potential products H2 and formate” | Curate as enabling mechanism; some evidence is genomic/proposed, not always biochemically confirmed in each SPOB (jin2023syntrophicpropionateoxidation pages 1-2, jin2023syntrophicpropionateoxidation pages 5-7) |
| HydABC ([FeFe]-hydrogenase complex) | performs | electron bifurcation linking H2 with ferredoxin and NAD(P)+ redox | Strong experimental structural biochemistry, but from acetogens rather than canonical SPOB | 10.1021/jacs.2c11683 | “the electron-bifurcating [FeFe]-hydrogenase HydABC… reduces low-potential ferredoxins by oxidizing hydrogen gas (H2)” | Mechanistically valuable support for FBEB node; taxon scope broader anaerobes, not direct proof of syntrophy phenotype alone (katsyv2023molecularbasisof pages 1-2) |
| HydABC ([FeFe]-hydrogenase complex) | is part of | hydrogen cycling in anoxic ecosystems | Strong experimental/introductory statement | 10.1021/jacs.2c11683 | “Hydrogen cycling in anoxic ecosystems is essential for the complete breakdown of organic matter” | Supportive background edge; indirect for TraitMech unless tied to specific syntrophic taxa (katsyv2023molecularbasisof pages 1-2) |
| Syntrophobacter fumaroxidans FDH/Hyd genes | decreased expression under | high formate stress (50 mM) | Strong experimental, taxon-specific | 10.3390/w16243551 | “all four formate dehydrogenases… were down-regulated under formate stress… hydrogenases… showed down-regulated expression” | Good taxon-specific edges for S. fumaroxidans; mark uncertain for broad generalization to all syntrophs (li2024promotingorinhibiting pages 12-13) |
| Formate concentration 5–10 mM | promotes | more stable syntrophic propionate degradation | Strong experimental, assay-specific | 10.3390/w16243551 | “The propionate showed more stable degradation when formate dosage ranged from 5 to 10 mM” | Useful environmental-factor edge, but highly system-specific to this sludge/co-culture setup (li2024promotingorinhibiting pages 1-2) |
| Formate concentration 50 mM | inhibits | syntrophic propionate oxidation / MMC pathway | Strong experimental, assay-specific | 10.3390/w16243551 | “when the formate dosage reached 50 mM… propionate metabolism was significantly inhibited”; “The methylmalonyl-CoA (MMC) pathway was inhibited under formate stress” | Curate as experimental edge with strong uncertainty note on general threshold (li2024promotingorinhibiting pages 1-2, li2024promotingorinhibiting pages 12-13) |
| Succinate dehydrogenase (label-only; SdhA/SdhB) | supports | propionate degradation through MMC pathway | Moderate; inferred from pathway/function analysis under formate perturbation | 10.3390/w16243551 | “succinate to fumarate… were thermodynamically constrained steps… The abundance of Sdh (A, B) decreased significantly in group D” | Gene-level edge is plausible but based on PICRUSt/pathway inference, not direct enzyme assay (li2024promotingorinhibiting pages 10-12) |
| Fumarate reductase-like TfrA/TfrB | opposes | fumarate-forming direction in MMC oxidation | Moderate; pathway interpretation, assay-specific | 10.3390/w16243551 | “the increase of Tfr (A, B) is not favorable to the reaction in the direction of fumarate formation” | Probably too specific/inferred for core TraitMech unless taxon-specific annotation desired (li2024promotingorinhibiting pages 10-12) |
| DIET (direct interspecies electron transfer) | can mediate | syntrophic coupling | Strong for specific consortia; broader relevance supported by reviews | 10.1134/s0026261720020101; 10.3390/life14050591 | “two types of interspecies electron transfer (IIET and DIET)”; thermophilic AOM enrichment “supported the notion that the process occurs via DIET” | Curate as alternative mechanism to H2/formate transfer; scope depends on taxa/community (nozhevnikova2020syntrophyandinterspecies pages 1-2, zhuang2024electrontransferin pages 5-6) |
| pilA / pili-like nanowires | support | DIET between syntrophic partners | Moderate-strong; specific sulfur/alkane consortia, experimental/genomic | 10.3390/life14050591 | “HotSeep-1 genome contains pilA… highly expressed… dense network of pili-like structures connecting HotSeep-1 to ANME-1 cells” | Strong for those consortia; not universal across syntrophy, so mark taxon-specific (zhuang2024electrontransferin pages 5-6) |
| Multiheme c-type cytochromes | support | DIET between syntrophic partners | Strong for ANME-SRB consortia; experimental/genomic | 10.3390/life14050591 | “large multiheme cytochromes could be involved in DIET between ANMEs and SRBs” | Curate as DIET machinery with taxon-specific scope (zhuang2024electrontransferin pages 5-6) |
| Conductive materials (activated carbon, graphene, magnetite, biochar) | stimulate | DIET | Moderate-strong; mostly review synthesis across AD studies | 10.3390/molecules28093883 | “Conductive materials… stimulate direct interspecies electron transfer (DIET)” | Strong application edge, but not direct proof of intrinsic organismal trait; better as environmental factor in engineered systems (mu2023emergingstrategiesfor pages 13-14) |
| Magnetite-loaded / magnetic biochar | increases | methane production in anaerobic digestion | Moderate-strong; multiple applied studies summarized in 2024 review | 10.1007/s42773-024-00354-x | “increased daily methane yields by 157%”; “highest methane yield… 62.61% increase”; “139.0% increase in methane yield” | Application-focused, mixed-study review; curate cautiously as engineering intervention rather than core natural syntrophy edge (zhou2024exploringmagneticnanomaterials pages 13-14) |
| Magnetite-loaded biochar | facilitates | DIET | Moderate-strong; applied AD review | 10.1007/s42773-024-00354-x | “By facilitating the DIET process, it increased daily methane yields by 157%” | Good engineered-environment edge; underlying causality often inferred from community shifts (zhou2024exploringmagneticnanomaterials pages 13-14) |
| Sulfate availability | shifts/competes with | syntrophic propionate oxidation toward sulfate-reducing respiration | Strong; 2023 review, thermodynamic comparison | 10.1128/aem.00384-23 | “Propionate oxidization coupled to sulfate reduction is thermodynamically more favorable than syntrophic propionate oxidation” | Important boundary-case edge: facultative SPOB may respire sulfate instead of engaging in syntrophy (jin2023syntrophicpropionateoxidation pages 9-10) |
| Elevated ammonia | inhibits | syntrophic propionate oxidation | Strong; 2023 review | 10.1128/aem.00384-23 | “ammonia toxicity selectively suppresses propionate oxidation more than butyrate oxidation” | Good environmental inhibitor edge; threshold depends on reactor/ecosystem (jin2023syntrophicpropionateoxidation pages 10-12) |
| Higher temperature | promotes | propionate degradation / SPOB activity | Strong; 2023 review | 10.1128/aem.00384-23 | “higher temperatures favor faster degradation” | Broad but not universally monotonic across all consortia; context dependent (jin2023syntrophicpropionateoxidation pages 10-12) |
| Neutral to weakly alkaline pH | promotes | SPOB abundance and propionate degradation | Strong; 2023 review | 10.1128/aem.00384-23 | “neutral/weakly alkaline pH favors SPOB abundance and degradation rates” | Good environmental preference edge for propionate-oxidizing syntrophy; likely subtrait-specific (jin2023syntrophicpropionateoxidation pages 10-12) |
| Elevated CO2 | restricts | propionate oxidation | Moderate-strong; 2023 review | 10.1128/aem.00384-23 | “elevated CO2 restricts oxidation” | Mechanistically plausible via thermodynamics; quantitative thresholds not fixed (jin2023syntrophicpropionateoxidation pages 10-12) |
| High hydrogen partial pressure (>1.5 × 10^-4 atm in OFMSW AD perspective) | inhibits | acetogenesis of 3–5 carbon VFAs / destabilizes AD | Moderate; 2024 perspective, engineering-focused | 10.1007/s11783-024-1812-7 | “The high pH2 (usually higher than 1.5 × 10−4 atm) prevents the acetogenesis of 3–5-carbon VFAs” | Perspective article, not primary mechanistic experiment; useful but should be marked proposal/application-focused (chen2024electronicregulationto pages 2-4) |
| Electron surplus in AD | increases | hydrogen partial pressure | Moderate; 2024 perspective | 10.1007/s11783-024-1812-7 | electrons “tends to bond with protons… to form H2, which significantly increases the partial pressure of hydrogen” | Engineering systems concept; not a direct organismal edge (chen2024electronicregulationto pages 2-4) |
| Methanogenic archaea (e.g., Methanothrix, Methanoculleus, Methanobacterium) | are critical partners in | anaerobic digestion syntrophic networks | Strong; metagenomic survey + experimental review | 10.1186/s40793-023-00545-2; 10.3390/w16243551 | “methanogenic archaea are subject to intense selective pressure”; Methanobacterium became dominant at high formate | Good partner nodes; role varies by substrate and formate/H2 regime (centurion2024aunifiedcompendium pages 1-2, li2024promotingorinhibiting pages 10-12) |
| Methanobacterium | tolerates/uses | higher formate than acetoclastic methanogens | Strong experimental, community-specific | 10.3390/w16243551 | “Methanobacterium was more tolerant, and even enjoyed the high concentration formate environment” | Useful taxon-specific edge, not class-wide methanogen rule (li2024promotingorinhibiting pages 10-12) |
| Smithella-like SPOB | are less sensitive to | H2 accumulation than MMC-pathway SPOB | Moderate; 2023 review and modeling synthesis | 10.1128/aem.00384-23 | C6 pathway produces only “one H2 molecule… in comparison with three H2 or formate molecules in the MMC pathway” and is “less sensitive to H2 accumulation” | Valuable comparative edge; mostly thermodynamic inference rather than direct head-to-head experiments (jin2023syntrophicpropionateoxidation pages 5-7) |


*Table: This table compiles the strongest source-backed causal edges relevant to microbial syntrophy (METPO:1002006), emphasizing mechanistic processes, environmental controls, DIET, and anaerobic digestion applications. It is designed to support cautious TraitMech curation by separating broad class-level edges from taxon-specific, assay-specific, or review-derived claims.*

### Recommended minimal core for `syntrophy.yaml`

The highest-confidence, broadly portable edges are:

1. **methanogenic partner — consumes → H₂/formate**;
2. **H₂/formate consumption — decreases → H₂ partial pressure/formate activity**;
3. **low H₂/formate activity — makes thermodynamically favorable → syntroph substrate oxidation**;
4. **syntrophic propionate oxidation — produces → acetate + CO₂ + H₂/formate**;
5. **syntrophic butyrate oxidation — produces → acetate + H₂/formate**;
6. **reverse electron transport — enables → unfavorable electron transfer to H⁺/CO₂**;
7. **FBEB/C — couples → favorable and unfavorable redox reactions**;
8. **syntroph substrate oxidation + methanogenesis — jointly enables → community growth and methane formation**.

Under standard conditions, propionate and butyrate oxidation to acetate plus H₂/formate are endergonic by approximately **+76.0 and +48.3 kJ mol⁻¹**, respectively. Partner-mediated product removal is therefore not incidental; it is the causal thermodynamic mechanism. (muller2010syntrophicbutyrateand pages 1-2)

For propionate, the 2023 review reported an in-situ energy range of approximately **−5 to −15 kJ mol⁻¹ propionate** in the source’s typeset notation, close to the estimated **15–25 kJ** energy quantum generally needed for cellular ATP synthesis. Propionate may account for **15–30% of methane formation** in paddy soils, lake sediments, and anaerobic reactors. These values explain why propionate oxidation is frequently rate limiting, but exact Gibbs energies should always be recalculated for the specified temperature, pH, gas pressure, and solute activities. (jin2023syntrophicpropionateoxidation pages 1-2)

## 4. Recent developments, 2023–2024

### 4.1 Propionate ecophysiology and biogeography

Jin and Lu’s 2023 synthesis established syntrophic propionate oxidizers as rare, slow-growing, environmentally sensitive organisms. In a survey covering **113 paddy soils**, abundance and methanogenic potential were greater at warm, low latitudes; temperature and sulfate were major structuring factors. *Smithella*-type C6 metabolism was relatively important in cooler high-latitude soils, whereas MMC-associated *Syntrophobacter* and *Pelotomaculum* were more prominent at middle latitudes. This is authoritative review synthesis, not proof that latitude directly causes pathway selection. (jin2023syntrophicpropionateoxidation pages 10-12)

DNA/RNA-SIP can enrich rare active populations, but SPOB lack a universal marker gene and ordinary metagenomics often yields poor genome resolution because of low abundance. SIP itself can generate false positives through downstream cross-feeding; approximately **20% incorporation of a ¹³C substrate into DNA** may be required for reliable density separation, creating a trade-off between adequate labeling and excessive incubation. (jin2023syntrophicpropionateoxidation pages 9-10)

### 4.2 Experimental formate concentration response

Li et al., published **10 December 2024**, tested anaerobic sludge and an *S. fumaroxidans–M. formicicum* coculture. Formate at **5–10 mM** was associated with more stable propionate degradation, while **50 mM** caused significant inhibition. In sludge, inhibition appeared above roughly **30 mM** and was severe at 50 mM. At 50 mM, transcription of four FDHs and most tested hydrogenases decreased; **fdh1** was significantly lower than the control and 5-mM treatment. These results support edges from high formate to reduced FDH/Hyd expression and impaired MMC flux, but the numerical thresholds are assay-specific and should not be generalized as universal biological constants. (li2024promotingorinhibiting pages 12-13, li2024promotingorinhibiting pages 1-2)

The same experiment found that *Methanobacterium*, *Methanosaeta*, and *Methanosarcina* represented **77.62–92.54%** of archaeal reads. Above about 30 mM formate, *Methanobacterium* replaced *Methanosaeta* as the dominant methanogen, consistent with complete formate-dehydrogenase and hydrogenase systems in formate-utilizing *Methanobacterium*. Community functions were partly predicted with PICRUSt, so gene-abundance claims from that component are weaker than measured RNA expression in the coculture. (li2024promotingorinhibiting pages 10-12)

### 4.3 Molecular mechanism of electron bifurcation

Katsyv et al. (published **22 February 2023**) resolved HydABC as a homodimer of heterotrimers of approximately **306 kDa** in *A. woodii* and **348 kDa** in *T. kivui*. A single FMN cofactor and iron–sulfur-cluster-dependent changes in NAD(P)⁺ affinity form a redox-driven kinetic gate that prevents electron backflow. The study supplies direct molecular support for HydABC-mediated coupling of favorable and unfavorable redox branches under anoxic conditions. (katsyv2023molecularbasisof pages 1-2)

### 4.4 DIET and alternative syntrophic mechanisms

A 2024 sulfur-cycle review summarized evidence for DIET between ANME archaea and sulfate-reducing partners: highly expressed extracellular cytochromes, **pilA**, pili-like intercellular networks, heme staining, and conductive aggregate behavior. It also described a *G. sulfurreducens–P. aestuarii* coculture in which deletion of the *Geobacter* trans-outer-membrane porin–cytochrome complex abolished partner growth, providing stronger causal evidence than simple gene co-occurrence. Nevertheless, some hydrocarbon-oxidizing consortia may use an interspecies sulfur cycle rather than DIET. (zhuang2024electrontransferin pages 6-8, zhuang2024electrontransferin pages 5-6)

### 4.5 Large-scale microbiome resources

A 2024 anaerobic-digestion compendium integrated **314 metagenomes**, recovered **11,831 MAGs** representing **4,568 nonredundant species**, and identified **76 archaeal genomes** with active phage interactions. The scale demonstrates the complexity of real digesters and the importance of methanogenic partners, but genome occurrence, SNVs, or functional annotations do not establish a syntrophic causal edge without activity, flux, or coculture evidence. (centurion2024aunifiedcompendium pages 1-2)

## 5. Applications and real-world implementation

### 5.1 Anaerobic digestion and biogas

Syntrophic acetogenesis links acidogenesis to methanogenesis in municipal, agricultural, food-waste, and sludge digesters. Propionate accumulation is a practical warning of imbalance because its oxidation is energetically constrained. Operational interventions include reducing organic loading, buffering pH, removing dissolved H₂, bioaugmentation, adding trace metals, and introducing conductive materials. A 2024 engineering perspective proposed an “electron surplus” model in which H₂ partial pressure above approximately **1.5 × 10⁻⁴ atm** inhibits acetogenesis of three- to five-carbon VFAs. This threshold is useful for process hypotheses but comes from a perspective synthesis rather than a universal controlled experiment. (chen2024electronicregulationto pages 2-4)

### 5.2 Conductive materials

Activated carbon, graphene, magnetite, and biochar are being tested as electron conduits and biofilm supports. A 2024 magnetic-biochar review reported individual studies with methane-yield increases of **62.61%, 139%, and 157%**, alongside inhibition at excessive amendment levels. These interventions are promising for high-ammonia or VFA-stressed reactors, but “facilitates DIET” is frequently inferred from conductivity, community enrichment, and methane output rather than directly measured interspecies electron flux. The outcomes are material-, dose-, feedstock-, and reactor-specific. (zhou2024exploringmagneticnanomaterials pages 13-14)

A 2023 review likewise found conductive amendments promising but explicitly noted limited direct evidence for propionate metabolism via DIET. Nitrate, sulfate, or azo dyes may accelerate propionate removal by providing alternative electron sinks, but they can reduce methane yield or alter product quality; these interventions should not be represented as unqualified enhancement of methanogenic syntrophy. (mu2023emergingstrategiesfor pages 13-14)

### 5.3 Environmental carbon and sulfur cycling

Syntrophic propionate, butyrate, and acetate oxidation controls anaerobic carbon turnover and methane formation in wetlands, rice paddies, sediments, landfills, animal guts, and subsurface environments. ANME–sulfate-reducer consortia couple methane oxidation to sulfate reduction and are central to marine methane control. Electron transfer between hydrocarbon-oxidizing archaea and sulfate reducers similarly links carbon and sulfur cycling. (jin2023syntrophicpropionateoxidation pages 10-12, zhuang2024electrontransferin pages 5-6)

## 6. Expert assessment for TraitMech curation

The literature strongly supports thermodynamic product removal as the **defining causal axis**. Hydrogen, formate, and DIET should be represented as alternative mechanisms, not treated as synonyms for syntrophy. Formate may dominate transfer in some cocultures, and both carriers can operate simultaneously. Likewise, syntrophic acetate, propionate, butyrate, aromatic-compound, methane, and alkane metabolisms require separate pathway subgraphs because they use different enzymes and partner roles. (muller2018syntrophyinmethanogenic pages 14-16, schink2017hydrogenorformate pages 7-10)

A useful graph architecture is:

- a **general syntrophy core** containing thermodynamic dependence, partner product removal, and interspecies electron transfer;
- **mechanism branches** for H₂-mediated transfer, formate-mediated transfer, DIET, and possible sulfur-shuttle transfer;
- **substrate modules** for propionate/MMC, propionate/C6, butyrate/β-oxidation, acetate/reverse Wood–Ljungdahl, and ANME-mediated methane oxidation;
- **context nodes** recording taxon, coculture, temperature, pH, electron acceptors, product concentrations, and reactor conditions.

## 7. Claims not yet suitable for unqualified curation

1. **A universal H₂ or formate threshold.** Values such as 10⁻⁴–10⁻⁵ atm H₂, 1 µM theoretical formate, 30–50 mM experimental formate, or 1.5 × 10⁻⁴ atm reactor H₂ are condition- and assay-dependent. Preserve the measurement context. (schink2017hydrogenorformate pages 7-10, li2024promotingorinhibiting pages 1-2, chen2024electronicregulationto pages 2-4)
2. **HydABC as universally required for syntrophy.** HydABC’s mechanism is experimentally established, but its necessity has not been demonstrated across all syntrophs. (katsyv2023molecularbasisof pages 1-2)
3. **All conductive-material responses as DIET.** Increased methane, conductivity, or enrichment of *Geobacter*, *Methanothrix*, or *Methanosarcina* is insufficient without direct electron-transfer evidence. (mu2023emergingstrategiesfor pages 13-14, zhou2024exploringmagneticnanomaterials pages 13-14)
4. **The unidentified first enzyme of C6 dismutation.** No enzyme identifier should be invented for condensation of two propionates into the C6 intermediate. (jin2023syntrophicpropionateoxidation pages 5-7, jin2023syntrophicpropionateoxidation pages 9-10)
5. **PICRUSt-inferred gene changes as measured expression.** In Li et al., pathway-prediction results should be distinguished from RNA measurements of FDH/Hyd genes. (li2024promotingorinhibiting pages 12-13, li2024promotingorinhibiting pages 10-12)
6. **Metagenomic co-occurrence as causality.** MAGs, pathway completeness, or proximity identify candidates, not thermodynamic dependence. Stable-isotope flux, partner-removal experiments, defined cocultures, electrochemical measurements, or targeted knockouts provide stronger evidence. (jin2023syntrophicpropionateoxidation pages 9-10, centurion2024aunifiedcompendium pages 1-2)
7. **DIET as universal in ANME–SRB consortia.** Some consortia may use cytochromes/pili, while others may use soluble shuttles or interspecies sulfur transfer. (zhuang2024electrontransferin pages 5-6)
8. **Engineering outcomes as organismal traits.** Magnetic biochar, azo dyes, nitrate, or sulfate are environmental interventions and should not become intrinsic nodes of an organism’s syntrophy phenotype without qualification. (mu2023emergingstrategiesfor pages 13-14, zhou2024exploringmagneticnanomaterials pages 13-14)

## 8. DOI-first bibliography

- Li Y. et al. **Promoting or Inhibiting: New Insights into the Role of Formate in Syntrophic Propionate Metabolism.** *Water* 16, 3551. Published 10 December 2024. [https://doi.org/10.3390/w16243551](https://doi.org/10.3390/w16243551). (li2024promotingorinhibiting pages 1-2)
- Zhuang X., Wang S., Wu S. **Electron Transfer in the Biogeochemical Sulfur Cycle.** *Life* 14, 591. Published May 2024. [https://doi.org/10.3390/life14050591](https://doi.org/10.3390/life14050591). (zhuang2024electrontransferin pages 6-8, zhuang2024electrontransferin pages 5-6)
- Chen Y. et al. **Electronic regulation to achieve efficient anaerobic digestion of OFMSW.** *Frontiers of Environmental Science & Engineering* 18. Published January 2024. [https://doi.org/10.1007/s11783-024-1812-7](https://doi.org/10.1007/s11783-024-1812-7). (chen2024electronicregulationto pages 2-4)
- Zhou W. et al. **Exploring magnetic nanomaterials with a focus on magnetic biochar in anaerobic digestion.** *Biochar* 6. Published June 2024. [https://doi.org/10.1007/s42773-024-00354-x](https://doi.org/10.1007/s42773-024-00354-x). (zhou2024exploringmagneticnanomaterials pages 13-14)
- Centurion V.B. et al. **A unified compendium of prokaryotic and viral genomes from over 300 anaerobic digestion microbiomes.** *Environmental Microbiome* 19, 1. Published January 2024. [https://doi.org/10.1186/s40793-023-00545-2](https://doi.org/10.1186/s40793-023-00545-2). (centurion2024aunifiedcompendium pages 1-2)
- Jin Y., Lu Y. **Syntrophic Propionate Oxidation: One of the Rate-Limiting Steps of Organic Matter Decomposition in Anoxic Environments.** *Applied and Environmental Microbiology* 89. Published 25 April 2023. [https://doi.org/10.1128/aem.00384-23](https://doi.org/10.1128/aem.00384-23). (jin2023syntrophicpropionateoxidation pages 5-7, jin2023syntrophicpropionateoxidation pages 1-2)
- Katsyv A. et al. **Molecular Basis of the Electron Bifurcation Mechanism in the [FeFe]-Hydrogenase Complex HydABC.** *Journal of the American Chemical Society* 145, 5696–5709. Published 22 February 2023. [https://doi.org/10.1021/jacs.2c11683](https://doi.org/10.1021/jacs.2c11683). (katsyv2023molecularbasisof pages 1-2)
- Mu L. et al. **Emerging Strategies for Enhancing Propionate Conversion in Anaerobic Digestion.** *Molecules* 28, 3883. Published May 2023. [https://doi.org/10.3390/molecules28093883](https://doi.org/10.3390/molecules28093883). (mu2023emergingstrategiesfor pages 13-14)
- Westerholm M., Calusinska M., Dolfing J. **Syntrophic propionate-oxidizing bacteria in methanogenic systems.** *FEMS Microbiology Reviews* 46. Published 2022. [https://doi.org/10.1093/femsre/fuab057](https://doi.org/10.1093/femsre/fuab057).
- Nozhevnikova A.N. et al. **Syntrophy and Interspecies Electron Transfer in Methanogenic Microbial Communities.** *Microbiology* 89, 129–147. Published March 2020. [https://doi.org/10.1134/S0026261720020101](https://doi.org/10.1134/S0026261720020101). (nozhevnikova2020syntrophyandinterspecies pages 1-2)
- Müller N. et al. **Syntrophic butyrate and propionate oxidation processes: from genomes to reaction mechanisms.** *Environmental Microbiology Reports* 2, 489–499. Published August 2010. [https://doi.org/10.1111/j.1758-2229.2010.00147.x](https://doi.org/10.1111/j.1758-2229.2010.00147.x). (muller2010syntrophicbutyrateand pages 1-2)
- Stams A.J.M., Plugge C.M. **Electron transfer in syntrophic communities of anaerobic bacteria and archaea.** *Nature Reviews Microbiology* 7, 568–577. Published August 2009. [https://doi.org/10.1038/nrmicro2166](https://doi.org/10.1038/nrmicro2166).

References

1. (muller2010syntrophicbutyrateand pages 1-2): Nicolai Müller, Petra Worm, Bernhard Schink, Alfons J. M. Stams, and Caroline M. Plugge. Syntrophic butyrate and propionate oxidation processes: from genomes to reaction mechanisms. Environmental microbiology reports, 2 4:489-99, Aug 2010. URL: https://doi.org/10.1111/j.1758-2229.2010.00147.x, doi:10.1111/j.1758-2229.2010.00147.x. This article has 389 citations and is from a peer-reviewed journal.

2. (nozhevnikova2020syntrophyandinterspecies pages 1-2): A. N. Nozhevnikova, Yu. I. Russkova, Yu. V. Litti, S. N. Parshina, E. A. Zhuravleva, and A. A. Nikitina. Syntrophy and interspecies electron transfer in methanogenic microbial communities. Microbiology, 89:129-147, Mar 2020. URL: https://doi.org/10.1134/s0026261720020101, doi:10.1134/s0026261720020101. This article has 144 citations and is from a peer-reviewed journal.

3. (jin2023syntrophicpropionateoxidation pages 1-2): Yidan Jin and Yahai Lu. Syntrophic propionate oxidation: one of the rate-limiting steps of organic matter decomposition in anoxic environments. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00384-23, doi:10.1128/aem.00384-23. This article has 54 citations and is from a peer-reviewed journal.

4. (muller2018syntrophyinmethanogenic pages 14-16): Nicolai Müller, Peer Timmers, Caroline M. Plugge, Alfons J. M. Stams, and Bernhard Schink. Syntrophy in methanogenic degradation. Microbiology Monographs, pages 153-192, Jan 2018. URL: https://doi.org/10.1007/978-3-319-98836-8\_9, doi:10.1007/978-3-319-98836-8\_9. This article has 18 citations.

5. (zhuang2024electrontransferin pages 6-8): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 25 citations.

6. (zhuang2024electrontransferin pages 5-6): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 25 citations.

7. (jin2023syntrophicpropionateoxidation pages 5-7): Yidan Jin and Yahai Lu. Syntrophic propionate oxidation: one of the rate-limiting steps of organic matter decomposition in anoxic environments. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00384-23, doi:10.1128/aem.00384-23. This article has 54 citations and is from a peer-reviewed journal.

8. (jin2023syntrophicpropionateoxidation pages 9-10): Yidan Jin and Yahai Lu. Syntrophic propionate oxidation: one of the rate-limiting steps of organic matter decomposition in anoxic environments. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00384-23, doi:10.1128/aem.00384-23. This article has 54 citations and is from a peer-reviewed journal.

9. (katsyv2023molecularbasisof pages 1-2): Alexander Katsyv, Anuj Kumar, Patricia Saura, Maximilian C. Pöverlein, Sven A. Freibert, Sven T. Stripp, Surbhi Jain, Ana P. Gamiz-Hernandez, Ville R. I. Kaila, Volker Müller, and Jan M. Schuller. Molecular basis of the electron bifurcation mechanism in the [fefe]-hydrogenase complex hydabc. Journal of the American Chemical Society, 145:5696-5709, Feb 2023. URL: https://doi.org/10.1021/jacs.2c11683, doi:10.1021/jacs.2c11683. This article has 78 citations and is from a highest quality peer-reviewed journal.

10. (schink2017hydrogenorformate pages 7-10): Bernhard Schink, Dominik Montag, Anja Keller, and Nicolai Müller. Hydrogen or formate: alternative key players in methanogenic degradation. Environmental Microbiology Reports, 9:189–202, Jun 2017. URL: https://doi.org/10.1111/1758-2229.12524, doi:10.1111/1758-2229.12524. This article has 99 citations and is from a peer-reviewed journal.

11. (muller2018syntrophyinmethanogenic pages 1-4): Nicolai Müller, Peer Timmers, Caroline M. Plugge, Alfons J. M. Stams, and Bernhard Schink. Syntrophy in methanogenic degradation. Microbiology Monographs, pages 153-192, Jan 2018. URL: https://doi.org/10.1007/978-3-319-98836-8\_9, doi:10.1007/978-3-319-98836-8\_9. This article has 18 citations.

12. (li2024promotingorinhibiting pages 1-2): Yanlin Li, Guanjing Cai, Xiaofang Pan, Nan Lv, Lin Feng, Gefu Zhu, Zunjing Lv, and Zhilong Ye. Promoting or inhibiting: new insights into the role of formate in syntrophic propionate metabolism. Water, 16:3551, Dec 2024. URL: https://doi.org/10.3390/w16243551, doi:10.3390/w16243551. This article has 9 citations.

13. (muller2018syntrophyinmethanogenic pages 6-9): Nicolai Müller, Peer Timmers, Caroline M. Plugge, Alfons J. M. Stams, and Bernhard Schink. Syntrophy in methanogenic degradation. Microbiology Monographs, pages 153-192, Jan 2018. URL: https://doi.org/10.1007/978-3-319-98836-8\_9, doi:10.1007/978-3-319-98836-8\_9. This article has 18 citations.

14. (li2024promotingorinhibiting pages 12-13): Yanlin Li, Guanjing Cai, Xiaofang Pan, Nan Lv, Lin Feng, Gefu Zhu, Zunjing Lv, and Zhilong Ye. Promoting or inhibiting: new insights into the role of formate in syntrophic propionate metabolism. Water, 16:3551, Dec 2024. URL: https://doi.org/10.3390/w16243551, doi:10.3390/w16243551. This article has 9 citations.

15. (li2024promotingorinhibiting pages 10-12): Yanlin Li, Guanjing Cai, Xiaofang Pan, Nan Lv, Lin Feng, Gefu Zhu, Zunjing Lv, and Zhilong Ye. Promoting or inhibiting: new insights into the role of formate in syntrophic propionate metabolism. Water, 16:3551, Dec 2024. URL: https://doi.org/10.3390/w16243551, doi:10.3390/w16243551. This article has 9 citations.

16. (mu2023emergingstrategiesfor pages 13-14): Lan Mu, Yifan Wang, Fenglian Xu, Jinhe Li, Junyu Tao, Yunan Sun, Yingjin Song, Zhaodan Duan, Siyi Li, and Guanyi Chen. Emerging strategies for enhancing propionate conversion in anaerobic digestion: a review. Molecules, 28:3883, May 2023. URL: https://doi.org/10.3390/molecules28093883, doi:10.3390/molecules28093883. This article has 50 citations.

17. (zhou2024exploringmagneticnanomaterials pages 13-14): Wenneng Zhou, Mahmoud Mazarji, Mengtong Li, Aohua Li, Yajing Wang, Yadong Yang, Jonathan T. E. Lee, Eldon R. Rene, Xiangzhou Yuan, and Junting Pan. Exploring magnetic nanomaterials with a focus on magnetic biochar in anaerobic digestion: from synthesis to application. Biochar, 6:1-21, Jun 2024. URL: https://doi.org/10.1007/s42773-024-00354-x, doi:10.1007/s42773-024-00354-x. This article has 29 citations.

18. (jin2023syntrophicpropionateoxidation pages 10-12): Yidan Jin and Yahai Lu. Syntrophic propionate oxidation: one of the rate-limiting steps of organic matter decomposition in anoxic environments. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00384-23, doi:10.1128/aem.00384-23. This article has 54 citations and is from a peer-reviewed journal.

19. (chen2024electronicregulationto pages 2-4): Yongdong Chen, Hong Wang, Parisa Ghofrani-Isfahani, Li Gu, Xiaoguang Liu, and Xiaohu Dai. Electronic regulation to achieve efficient anaerobic digestion of organic fraction of municipal solid waste (ofmsw): strategies, challenges and potential solutions. Frontiers of Environmental Science &amp; Engineering, Jan 2024. URL: https://doi.org/10.1007/s11783-024-1812-7, doi:10.1007/s11783-024-1812-7. This article has 24 citations and is from a peer-reviewed journal.

20. (centurion2024aunifiedcompendium pages 1-2): Victor Borin Centurion, Alessandro Rossi, Esteban Orellana, Gabriele Ghiotto, Balázs Kakuk, Maria Silvia Morlino, Arianna Basile, Guido Zampieri, Laura Treu, and Stefano Campanaro. A unified compendium of prokaryotic and viral genomes from over 300 anaerobic digestion microbiomes. Environmental Microbiome, Jan 2024. URL: https://doi.org/10.1186/s40793-023-00545-2, doi:10.1186/s40793-023-00545-2. This article has 36 citations and is from a peer-reviewed journal.