---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:29:32.396538'
end_time: '2026-06-18T06:40:04.595168'
duration_seconds: 632.2
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: brown pigmented
  trait_identifier: METPO:1003023
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: brown_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    brown due to accumulation of brown pigments such as pyomelanin or other melanins.
  parent_traits: METPO:1003021
  synonyms: Pigment_brown
  evidence_summary: 'DOI:10.1128/AEM.67.8.3463-3468.2001: Brown pigments are produced
    when homogentisic acid accumulates (Supports brown microbial pigmentation as a
    homogentisic-acid/pyomelanin pathway phenotype.)'
  causal_graph_summary: 'brown_pigmented_pyomelanin_pathway: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** brown pigmented
- **METPO identifier:** METPO:1003023
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear brown due to accumulation of brown pigments such as pyomelanin or other melanins.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_brown
- **Existing evidence:** DOI:10.1128/AEM.67.8.3463-3468.2001: Brown pigments are produced when homogentisic acid accumulates (Supports brown microbial pigmentation as a homogentisic-acid/pyomelanin pathway phenotype.)
- **Existing causal graph summary:** brown_pigmented_pyomelanin_pathway: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **brown pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/brown_pigmented.yaml`.

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
- **Trait label:** brown pigmented
- **METPO identifier:** METPO:1003023
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear brown due to accumulation of brown pigments such as pyomelanin or other melanins.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_brown
- **Existing evidence:** DOI:10.1128/AEM.67.8.3463-3468.2001: Brown pigments are produced when homogentisic acid accumulates (Supports brown microbial pigmentation as a homogentisic-acid/pyomelanin pathway phenotype.)
- **Existing causal graph summary:** brown_pigmented_pyomelanin_pathway: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **brown pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/brown_pigmented.yaml`.

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


# Research report: Microbial trait “brown pigmented” (METPO:1003023)

## 0. Executive scope summary (curation-oriented)
The METPO trait **brown pigmented** denotes an **assay-observed morphology** where microbial colonies, cells, or culture supernatants appear **brown** due to accumulation of brown pigments, most commonly **pyomelanin** formed from **homogentisic acid (HGA)** in the **L-tyrosine degradation (homogentisate) pathway**. In bacteria and fungi, pyomelanin is described as a **brown, melanin-like polymer** that forms when **HGA accumulates**, is **excreted**, then **spontaneously auto-oxidizes** and **polymerizes** into pigment. (moustafa2024mutationofhmga pages 1-2, moustafa2024mutationofhmga pages 2-4, thiourmauprivez2023assessingtheeffects pages 1-5)

For curation, the trait should be treated as **phenotype-first** (brown appearance) and paired with **mechanism-specific nodes** to avoid conflation with other causes of dark/brown color, including **DOPA/eumelanin** pathways or **DHN/allomelanin** pathways (especially in fungi), and **non-melanin chemical browning** artifacts in engineered systems. (qin2024melanininfungi pages 7-8, qin2024melanininfungi pages 10-11, thomsen2023beetredfood pages 6-7)

### Boundary cases / how to distinguish from nearby traits
* **Pyomelanin vs DOPA/eumelanin:** Pyomelanin is HGA-derived and often extracellular/water soluble; DOPA/eumelanin derives from tyrosine oxidation (tyrosinase/laccase) and can also yield brown-to-black pigments. (qin2024melanininfungi pages 7-8, qin2024melanininfungi pages 10-11)
* **Pyomelanin vs DHN-melanin:** DHN-melanin is polyketide-derived and often cell-wall associated; it may produce brown/black phenotypes but implies a different gene set (PKS and DHN pathway genes). (qin2024melanininfungi pages 10-11)
* **Assay-dependent browning not due to pyomelanin:** In engineered *Yarrowia lipolytica*, medium browning at pH >4 under high buffering was hypothesized to involve **cyclo‑DOPA/L‑dopachrome decomposition** (eumelanin precursors), and browning persisted even after 4HPPD deletion—highlighting a curation pitfall where “brown” is not necessarily pyomelanin/HGA-driven. (thomsen2023beetredfood pages 6-7, thomsen2023beetredfood pages 5-6)

## 1. Key concepts and current mechanistic understanding

### 1.1 Canonical biochemical mechanism (homogentisate → pyomelanin)
A core, repeatedly supported causal chain is:
1) **L-tyrosine catabolism** generates **4-hydroxyphenylpyruvate (4-HPP)**. (thomsen2023beetredfood pages 5-6)
2) **4-hydroxyphenylpyruvate dioxygenase (HppD/HPPD; EC 1.13.11.27)** converts 4-HPP → **HGA**. (moustafa2024mutationofhmga pages 1-2, thiourmauprivez2023assessingtheeffects pages 1-5)
3) Under conditions where **HGA accumulates** (often due to impaired downstream catabolism), HGA is **excreted** and **spontaneously auto-oxidizes** to **benzoquinoneacetic acid/benzoquinone acetate**, then **self-polymerizes** into **pyomelanin**, producing an observable brown phenotype. (moustafa2024mutationofhmga pages 1-2, moustafa2024mutationofhmga pages 2-4, qin2024melanininfungi pages 7-8)
4) **Homogentisate 1,2-dioxygenase (HmgA; EC 1.13.11.5)** normally consumes HGA to **maleylacetoacetate**; thus **loss-of-function in hmgA** is a major driver of HGA accumulation and pigmentation. (moustafa2024mutationofhmga pages 1-2, moustafa2024mutationofhmga pages 2-4)

### 1.2 Gene-level determinants (cross-taxon highlights)
*Bacteria (Burkholderia):* A specific **HmgA G378R** amino-acid substitution was reported to render HmgA non-functional, stopping the pathway at HGA and resulting in pyomelanin production (pigmented phenotype). (moustafa2024mutationofhmga pages 2-4)

*Bacteria (Pseudomonas):* Pyomelanin-producing reference mutants were generated by introducing a stop codon in **hmgA**, directly linking hmgA loss to pigment production, and pyomelanin synthesis could be probed by inhibiting **HppD** with bicyclopyrone. (appella2024beyonduniformitypyomelanin’s pages 19-24)

*Fungi (Aspergillus fumigatus):* A six-gene cluster is described as responsible for pyomelanin synthesis: **hppD, hmgX, hmgA, fahA, maiA, hmgR**. Disruption of **hppD** results in a light-color phenotype attributed to absence of HGA, and **hmgX** influences production. (qin2024melanininfungi pages 7-8)

## 2. Candidate causal-graph entities (nodes) with ontology grounding
The following node inventory is designed to translate into `data/traits/morphology/brown_pigmented.yaml`.

| Node label | Type | Suggested grounding | Notes (incl. taxa where reported) | Key supporting sources |
|---|---|---|---|---|
| brown pigmented | Phenotype | METPO:1003023 | Trait-level visible brown colony/culture phenotype; often assay-observed and frequently explained by pyomelanin accumulation, but should not be equated with all melanin types without mechanism-specific evidence. | (moustafa2024mutationofhmga pages 1-2, thiourmauprivez2023assessingtheeffects pages 1-5, qin2024melanininfungi pages 7-8) |
| pyomelanin production | Phenotype | label only | Brown melanin-like pigment phenotype; typically extracellular/water-soluble in fungi and observed as brown culture supernatant or colonies in bacteria/yeast. | (moustafa2024mutationofhmga pages 1-2, qin2024melanininfungi pages 7-8, thomsen2023beetredfood pages 5-6) |
| light-color / non-pigmented phenotype | Phenotype | label only | Negative/contrast phenotype when pyomelanin pathway is disrupted, e.g., hppD disruption in Aspergillus fumigatus or functional HmgA in Burkholderia/Pseudomonas contexts. | (qin2024melanininfungi pages 7-8, moustafa2024mutationofhmga pages 2-4, appella2024beyonduniformitypyomelanin’s pages 19-24) |
| tyrosine degradation pathway | Pathway/Process | GO:0006570 | Core upstream process generating 4-hydroxyphenylpyruvate and homogentisate; directly linked to pyomelanin in fungi, bacteria, and yeast. | (moustafa2024mutationofhmga pages 1-2, qin2024melanininfungi pages 7-8, thomsen2023beetredfood pages 5-6) |
| homogentisate pathway | Pathway/Process | label only | Mechanistic pathway label useful for graphing brown pigmentation due to HGA accumulation; explicitly invoked in Pseudomonas pyomelanin studies. | (appella2024beyonduniformitypyomelanin’s pages 19-24, moustafa2024mutationofhmga pages 1-2) |
| homogentisate catabolic process | Pathway/Process | GO:0019474 | Downstream HGA degradation branch; interruption favors pigment formation by causing HGA buildup. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2) |
| pyomelanin biosynthetic process | Pathway/Process | label only | Process node for HGA accumulation, excretion, auto-oxidation, and polymerization into brown pigment. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2, qin2024melanininfungi pages 10-11) |
| oxidation of homogentisic acid | Pathway/Process | label only | HGA spontaneously oxidizes after excretion; oxidation precedes polymerization and visible browning. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2, qin2024melanininfungi pages 7-8) |
| polymerization of homogentisic acid derivatives to pyomelanin | Pathway/Process | label only | Final pigment-forming step; described as self-polymerization after benzoquinoneacetic acid/benzoquinone acetate formation. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2, qin2024melanininfungi pages 7-8) |
| 4-hydroxyphenylpyruvate dioxygenase activity | Pathway/Process | GO:0016702 | Enzymatic activity converting 4-hydroxyphenylpyruvate to homogentisate; a key positive mechanistic node for pyomelanin-linked brown pigmentation. | (thiourmauprivez2023assessingtheeffects pages 1-5, moustafa2024mutationofhmga pages 2-4, qin2024melanininfungi pages 10-11) |
| homogentisate 1,2-dioxygenase activity | Pathway/Process | GO:0004411 | Enzymatic activity consuming HGA to maleylacetoacetate; loss of activity promotes pigmentation. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2, qin2024melanininfungi pages 7-8) |
| hppD | Genes/Proteins/Enzymes | label only | Gene encoding HppD; essential positive determinant of HGA formation and pyomelanin production across Burkholderia, Aspergillus, Pseudomonas, and Yarrowia-related contexts. | (moustafa2024mutationofhmga pages 2-4, qin2024melanininfungi pages 7-8, thomsen2023beetredfood pages 5-6) |
| HppD / HPPD / 4-hydroxyphenylpyruvate dioxygenase | Genes/Proteins/Enzymes | EC:1.13.11.27 | Converts 4-hydroxyphenylpyruvate to HGA; targeted by β-triketone herbicides and bicyclopyrone in inhibition assays. | (thiourmauprivez2023assessingtheeffects pages 1-5, thiourmauprivez2023assessingtheeffects pages 5-8, appella2024beyonduniformitypyomelanin’s pages 19-24) |
| hmgA | Genes/Proteins/Enzymes | label only | Gene encoding homogentisate 1,2-dioxygenase; loss-of-function or damaging mutation is a major causal node for HGA accumulation and brown pigmentation. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2, appella2024beyonduniformitypyomelanin’s pages 19-24) |
| HmgA / homogentisate 1,2-dioxygenase | Genes/Proteins/Enzymes | EC:1.13.11.5 | Converts HGA to maleylacetoacetate; nonfunctional HmgA causes pathway arrest at HGA and pyomelanin production. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2) |
| hmgX | Genes/Proteins/Enzymes | label only | Cofactor-associated gene influencing HppD-dependent pyomelanin production in Aspergillus fumigatus; likely taxon-specific. | (qin2024melanininfungi pages 7-8) |
| fahA | Genes/Proteins/Enzymes | label only | Member of A. fumigatus six-gene tyrosine degradation/pyomelanin cluster; supports fungal mechanistic context but specific edge to brown pigmentation is less directly evidenced here. | (qin2024melanininfungi pages 7-8) |
| maiA | Genes/Proteins/Enzymes | label only | Member of A. fumigatus pyomelanin-associated cluster; candidate downstream catabolic node. | (qin2024melanininfungi pages 7-8) |
| hmgR | Genes/Proteins/Enzymes | label only | Regulatory gene in A. fumigatus pyomelanin cluster; useful as a context-specific regulator node. | (qin2024melanininfungi pages 7-8) |
| YlARO8 | Genes/Proteins/Enzymes | label only | Yarrowia tyrosine aminotransferase contributing to 4-hydroxyphenylpyruvate formation upstream of HGA and browning. | (thomsen2023beetredfood pages 5-6) |
| YlARO9 | Genes/Proteins/Enzymes | label only | Second Yarrowia tyrosine aminotransferase in the same upstream conversion step. | (thomsen2023beetredfood pages 5-6) |
| Yl4HPPD | Genes/Proteins/Enzymes | label only | Yarrowia 4-hydroxyphenylpyruvate dioxygenase; deletion increases red product formation and reduces pyomelanin-linked diversion, though browning can persist for other reasons. | (thomsen2023beetredfood pages 5-6) |
| HmgA G378R variant | Genes/Proteins/Enzymes | label only | Specific Burkholderia cenocepacia amino-acid substitution rendering HmgA nonfunctional and associated with pigmented phenotype; taxon/allele-specific. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2) |
| L-tyrosine | Metabolites/Chemicals | CHEBI:17895 | Precursor/substrate feeding the pathway; supplementation commonly used to elicit pyomelanin and brown pigment in assays. | (thiourmauprivez2023assessingtheeffects pages 1-5, thiourmauprivez2023assessingtheeffects pages 5-8, thomsen2023beetredfood pages 5-6) |
| 4-hydroxyphenylpyruvate | Metabolites/Chemicals | CHEBI:58083 | Immediate substrate of HPPD/HppD in HGA formation. | (thiourmauprivez2023assessingtheeffects pages 1-5, moustafa2024mutationofhmga pages 2-4, thomsen2023beetredfood pages 5-6) |
| homogentisic acid (HGA) | Metabolites/Chemicals | CHEBI:44747 | Central causal metabolite; accumulation, excretion, and oxidation/polymerization produce pyomelanin and visible browning. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2, thomsen2023beetredfood pages 5-6) |
| benzoquinoneacetic acid / benzoquinone acetate | Metabolites/Chemicals | label only | Oxidized intermediate formed after HGA auto-oxidation prior to polymerization; naming varies across sources. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2, qin2024melanininfungi pages 7-8) |
| maleylacetoacetate | Metabolites/Chemicals | CHEBI:87684 | Product of HmgA-catalyzed HGA cleavage; node useful for representing the non-pigmented branch of the pathway. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2) |
| pyomelanin | Metabolites/Chemicals | label only | Brown melanin-like polymer/end product; extracellular and water-soluble in several fungal/bacterial contexts. | (moustafa2024mutationofhmga pages 1-2, qin2024melanininfungi pages 7-8, elzawawy2024bioproductionandoptimization pages 1-2) |
| sulcotrione | Metabolites/Chemicals | CHEBI:138291 | β-triketone HPPD inhibitor used to perturb pigment formation; strain-specific reduction of HPPD-linked pyomelanin readout. | (thiourmauprivez2023assessingtheeffects pages 1-5, thiourmauprivez2023assessingtheeffects pages 5-8) |
| mesotrione | Metabolites/Chemicals | CHEBI:68433 | β-triketone HPPD inhibitor used in whole-cell pyomelanin assays. | (thiourmauprivez2023assessingtheeffects pages 1-5, thiourmauprivez2023assessingtheeffects pages 5-8) |
| tembotrione | Metabolites/Chemicals | CHEBI:79945 | β-triketone HPPD inhibitor; reported as strongest inhibitory effect among tested herbicides in one study. | (thiourmauprivez2023assessingtheeffects pages 1-5) |
| bicyclopyrone | Metabolites/Chemicals | CHEBI:134157 | Specific HppD inhibitor used in Pseudomonas cultures; abolished pigment production in the study context. | (appella2024beyonduniformitypyomelanin’s pages 19-24) |
| L-tyrosine-supplemented medium | Environmental/Experimental factors | label only | Common experimental condition for revealing brown pyomelanin phenotype on plates or in broth. | (thiourmauprivez2023assessingtheeffects pages 1-5, thiourmauprivez2023assessingtheeffects pages 5-8) |
| extracellular environment / cell-free supernatant | Environmental/Experimental factors | GO:0005576 | Location where HGA accumulates and pyomelanin is often measured spectrophotometrically; useful localization node. | (moustafa2024mutationofhmga pages 2-4, thomsen2023beetredfood pages 5-6, elzawawy2024bioproductionandoptimization pages 1-2) |
| buffered medium at pH ~5–6 | Environmental/Experimental factors | label only | In Yarrowia, associated with browning; however, source indicates this may reflect non-pyomelanin browning in some engineered strains, so use cautiously. | (thomsen2023beetredfood pages 5-6) |
| artificial sputum medium (ASM) | Environmental/Experimental factors | label only | Infection-mimicking medium used for pyomelanin production analysis in Pseudomonas aeruginosa. | (appella2024beyonduniformitypyomelanin’s pages 19-24) |
| β-triketone herbicide exposure | Environmental/Experimental factors | label only | Perturbation class reducing HPPD-linked pigment output in a strain- and molecule-dependent manner. | (thiourmauprivez2023assessingtheeffects pages 1-5, thiourmauprivez2023assessingtheeffects pages 5-8) |
| UVC irradiation | Environmental/Experimental factors | ENVO:01001027 | Experimental stressor used to test protective effects of purified pyomelanin; relevant as downstream phenotype context, not core pigment-causation node. | (appella2024beyonduniformitypyomelanin’s pages 19-24) |
| Burkholderia cenocepacia | Organism contexts | NCBITaxon:95486 | Strong peer-reviewed bacterial model linking HmgA dysfunction to pyomelanin-associated brown pigmentation. | (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2) |
| Pseudomonas aeruginosa | Organism contexts | NCBITaxon:287 | Important pyomelanin producer including engineered hmgA mutants and chronic-infection isolates. | (appella2024beyonduniformitypyomelanin’s pages 19-24) |
| Aspergillus fumigatus | Organism contexts | NCBITaxon:746128 | Fungal pyomelanin model with six-gene cluster and hppD disruption causing light-color phenotype. | (qin2024melanininfungi pages 7-8) |
| Yarrowia lipolytica | Organism contexts | NCBITaxon:4952 | Yeast context showing HGA/pyomelanin-related flux and browning, but also key boundary case where some browning persisted after HPPD deletion. | (thomsen2023beetredfood pages 5-6) |
| Streptomyces djakartensis NSS-3 | Organism contexts | label only | Reported extracellular dark-brown pyomelanin producer with optimization and application data; mechanism less gene-resolved in the provided context. | (elzawawy2024bioproductionandoptimization pages 1-2) |
| Shewanella oneidensis MR-1 | Organism contexts | NCBITaxon:211586 | Environmental bacterium used in HPPD inhibition assay with pyomelanin OD430 readout; sensitive to β-triketone inhibition. | (thiourmauprivez2023assessingtheeffects pages 1-5, thiourmauprivez2023assessingtheeffects pages 5-8) |
| Pseudomonas fluorescens F113 | Organism contexts | NCBITaxon:294 | Environmental bacterium with HPPD activity not inhibited by tested β-triketones in the cited assay. | (thiourmauprivez2023assessingtheeffects pages 1-5, thiourmauprivez2023assessingtheeffects pages 5-8) |


*Table: This table lists candidate nodes for a causal graph of the microbial brown-pigmented trait centered on the pyomelanin/homogentisate pathway. It highlights phenotype, pathway, gene, metabolite, environmental, and organism-context nodes with suggested ontology grounding and source-backed support.*

## 3. Evidence-backed candidate causal edges (triples)
The table below provides candidate **subject–predicate–object** edges for a TraitMech causal graph, with verbatim snippets, DOI-first references, and curation notes.

| Edge (S–P–O) | Evidence snippet (verbatim short quote) | Reference (authors, year, DOI, URL) | Notes for curation (strength/uncertainty, taxa, assay context) | Suggested grounding for S and O |
|---|---|---|---|---|
| L-tyrosine catabolism — produces — 4-hydroxyphenylpyruvate | “tyrosine aminotransferases (YlARO8, YlARO9) convert l-tyrosine into 4-hydroxyphenylpyruvate” (thomsen2023beetredfood pages 5-6) | Thomsen et al., 2023, doi:10.1038/s41564-023-01517-5, https://doi.org/10.1038/s41564-023-01517-5 | Strong for yeast upstream pathway; taxon-specific gene names (Yarrowia lipolytica) but biochemically generalizable as precursor step. | S: CHEBI:17895; O: CHEBI:58083 |
| 4-hydroxyphenylpyruvate dioxygenase (HppD/HPPD) — converts — homogentisic acid | “The hppD gene codes for a protein that is responsible for the conversion of 4-hydroxyphenylpyruvate to HGA.” (moustafa2024mutationofhmga pages 1-2) | Moustafa et al., 2024, doi:10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | Strong, direct causal statement; peer-reviewed bacterial source. | S: EC:1.13.11.27; O: CHEBI:44747 |
| 4-hydroxyphenylpyruvate dioxygenase activity — part_of / enables — homogentisate pathway brown pigmentation | “This enzyme is a non-heme iron enzyme involved in the second reaction of the tyrosine catabolism pathway by converting 4-hydroxyphenylpyruvate (HPP) in homogentisate (HGA)” (thiourmauprivez2023assessingtheeffects pages 1-5) | Thiour-Mauprivez et al., 2023, doi:10.1007/s11356-022-22801-7, https://doi.org/10.1007/s11356-022-22801-7 | Strong biochemical support; useful generic edge for pathway representation. | S: GO:0016702; O: CHEBI:44747 |
| homogentisate 1,2-dioxygenase (HmgA) — converts — maleylacetoacetate | “Homogentisate 1,2-dioxygenase, encoded by the hmgA gene, converts HGA to maleylacetoacetate.” (moustafa2024mutationofhmga pages 1-2) | Moustafa et al., 2024, doi:10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | Strong, direct causal statement; core negative branch away from pigment formation. | S: EC:1.13.11.5; O: CHEBI:87684 |
| hmgA loss-of-function / nonfunctional HmgA — causes accumulation of — homogentisic acid | “The G378R change renders HmgA non-functional, and the pathway stops at the intermediate molecule HGA” (moustafa2024mutationofhmga pages 2-4) | Moustafa et al., 2024, doi:10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | Strong but allele-specific in Burkholderia cenocepacia; curate generic loss-of-function edge and note taxon-specific variant separately. | S: label only (hmgA loss of function); O: CHEBI:44747 |
| homogentisic acid — auto-oxidizes to form — benzoquinoneacetic acid | “HGA is excreted and spontaneously auto-oxidizes to form benzoquinoneacetic acid” (moustafa2024mutationofhmga pages 1-2) | Moustafa et al., 2024, doi:10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | Strong direct statement; wording varies across sources (“benzoquinone acetate” vs “benzoquinoneacetic acid”). | S: CHEBI:44747; O: label only (benzoquinoneacetic acid/benzoquinone acetate) |
| benzoquinoneacetic acid — self-polymerizes to produce — pyomelanin | “followed by self-polymerization to produce pyomelanin” (moustafa2024mutationofhmga pages 1-2) | Moustafa et al., 2024, doi:10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | Strong direct statement; together with prior row supports multi-step pigment mechanism. | S: label only (benzoquinoneacetic acid/benzoquinone acetate); O: label only (pyomelanin) |
| homogentisic acid accumulation — leads_to — pyomelanin / brown melanin-like pigment | “Pyomelanin is a pigment that is commonly found in many systems of life… Pyomelanin is a natural polymer of homogentisic acid (HGA)” (moustafa2024mutationofhmga pages 1-2) | Moustafa et al., 2024, doi:10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | Strong generic mechanism; suitable central TraitMech edge. | S: CHEBI:44747; O: label only (pyomelanin) |
| hppD disruption — causes — light-color / reduced pyomelanin phenotype | “Disrupting the expression of hppD in A. fumigatus can result in a light color phenotype, attributed to the absence of HGA.” (qin2024melanininfungi pages 7-8) | Qin & Xia, 2024, doi:10.1186/s12934-024-02614-8, https://doi.org/10.1186/s12934-024-02614-8 | Strong review statement summarizing fungal primary evidence; taxon-specific to Aspergillus fumigatus. | S: label only (hppD disruption); O: label only (light-color phenotype) |
| L-tyrosine-supplemented medium — promotes / reveals — pyomelanin production | “This brown pigment is easily observable on culture media supplemented with L-tyrosine” (thiourmauprivez2023assessingtheeffects pages 1-5) | Thiour-Mauprivez et al., 2023, doi:10.1007/s11356-022-22801-7, https://doi.org/10.1007/s11356-022-22801-7 | Moderate-to-strong assay-context edge; best curated as experimental factor enabling observation/production. | S: CHEBI:17895; O: label only (pyomelanin/brown pigment) |
| β-triketone herbicide exposure — inhibits — HPPD activity | “responses to herbicides are strain-dependent with Pseudomonas fluorescens F113 HPPD activity not inhibited by any of the herbicide tested; when all three β-triketone herbicides inhibited HPPD in Bacillus cereus ATCC14579 and Shewanella oneidensis MR-1” (thiourmauprivez2023assessingtheeffects pages 1-5) | Thiour-Mauprivez et al., 2023, doi:10.1007/s11356-022-22801-7, https://doi.org/10.1007/s11356-022-22801-7 | Strong but strain-specific; curate with uncertainty/assay qualifier because inhibition varies by herbicide and taxon. | S: label only (β-triketone herbicide exposure); O: GO:0016702 |
| increasing sulcotrione dose — decreases — HPPD-linked pigment signal | “HPPD activity clearly decreased with increasing doses of sulcotrione, with a decrease of, at least, 31 % at 1×RfD, and of, at least, 74 % at 10×RfD.” (thiourmauprivez2023assessingtheeffects pages 8-11) | Thiour-Mauprivez et al., 2023, doi:10.1007/s11356-022-22801-7, https://doi.org/10.1007/s11356-022-22801-7 | Strong quantitative assay support; OD430 pigment proxy in whole-cell assay. | S: CHEBI:138291; O: label only (pyomelanin OD430 signal / HPPD activity proxy) |
| bicyclopyrone — inhibits — HppD | “bicyclopyrone… was used to analyze the relevance of HppD.” (appella2024beyonduniformitypyomelanin’s pages 19-24) | Appella et al., 2024, doi:10.1101/2024.04.11.589128, https://doi.org/10.1101/2024.04.11.589128 | Moderate; preprint, but useful perturbation evidence. | S: CHEBI:134157; O: EC:1.13.11.27 |
| bicyclopyrone inhibition of HppD — abolishes — pigment production | “Different concentrations (0.1 mM, 1 mM, and 10 mM) of this inhibitor were added… Bacterial growth and culture coloration were recorded to analyze the pyomelanin production.” and “indicating the inhibition of HppD and the involvement of the homogentisate pathway in melanin production.” (appella2024beyonduniformitypyomelanin’s pages 19-24) | Appella et al., 2024, doi:10.1101/2024.04.11.589128, https://doi.org/10.1101/2024.04.11.589128 | Moderate; preprint and coloration-based readout, but directly relevant to causal graph. | S: CHEBI:134157; O: label only (pyomelanin/brown pigment production) |
| Yl4HPPD deletion — increases — redder colonies / reduced pyomelanin diversion | “Upon deletion of Yl4HPPD, we noticed that the resulting colonies (ST12376) were redder” (thomsen2023beetredfood pages 5-6) | Thomsen et al., 2023, doi:10.1038/s41564-023-01517-5, https://doi.org/10.1038/s41564-023-01517-5 | Moderate; informative as support that HPPD diverts flux to HGA/pyomelanin, but phenotype is in engineered yeast, not generic brown trait. | S: label only (Yl4HPPD deletion); O: label only (reduced browning / redder colony phenotype) |
| buffered medium at ~pH 5–6 — associated_with — browning (boundary case) | “In cultivations with pH maintained at ~5–6, the medium turned brown” (thomsen2023beetredfood pages 5-6) | Thomsen et al., 2023, doi:10.1038/s41564-023-01517-5, https://doi.org/10.1038/s41564-023-01517-5 | Boundary-case only; do not over-curate as pyomelanin causation because the same study found alternative explanation for browning. | S: label only (buffered medium pH ~5–6); O: label only (brown medium phenotype) |
| pH > 4 / enhanced buffering — may cause — non-pyomelanin browning | “browning was ‘exclusively observed in media with enhanced buffering capacity’ and is hypothesized to arise from eumelanin formation via ‘cyclo-DOPA and l-dopachrome decomposition at pH > 4.’” (thomsen2023beetredfood pages 6-7) | Thomsen et al., 2023, doi:10.1038/s41564-023-01517-5, https://doi.org/10.1038/s41564-023-01517-5 | Important exclusion edge; weak/hypothesis and specific to engineered betanin-producing Yarrowia. Use as warning, not core TraitMech edge. | S: label only (pH >4 / enhanced buffering); O: label only (non-pyomelanin browning) |
| pyomelanin — increases survival under — UVC irradiation | “UVC (254 nm) tolerance in wild-type and pyomelanin-producing mutant cells was evaluated” and cells were tested “with 0.15 mg mL-1 purified pyomelanin” (appella2024beyonduniformitypyomelanin’s pages 19-24) | Appella et al., 2024, doi:10.1101/2024.04.11.589128, https://doi.org/10.1101/2024.04.11.589128 | Moderate; downstream effect, preprint. Relevant as consequence node, not defining pigmentation mechanism. | S: label only (pyomelanin); O: ENVO:01001027 |
| pyomelanin-producing strains — are associated with — oxidative stress protection in some taxa | “Some Bcc strains are known to naturally produce pyomelanin, a brown melanin-like pigment known for scavenging free radicals” (moustafa2024mutationofhmga pages 1-2) | Moustafa et al., 2024, doi:10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | Moderate and context-dependent; same paper found no effect on H2O2/NO in tested isogenic strains, so curate as taxon/assay-variable downstream effect. | S: label only (pyomelanin); O: label only (oxidative stress protection) |


*Table: This table lists source-backed subject–predicate–object edges for curating the brown-pigmented microbial trait around the homogentisate/pyomelanin mechanism. It emphasizes direct biochemical causation, perturbation evidence, and important boundary cases that should be curated cautiously.*

## 4. Recent developments and latest research (prioritizing 2023–2024)

### 4.1 2024: Genotype-to-phenotype mapping of hmgA variants in an opportunistic pathogen
A 2024 *Microbiology Spectrum* study explicitly ties **pyomelanin (brown pigment)** in *Burkholderia cenocepacia* to **HmgA dysfunction**, including a defined amino-acid change that renders HmgA nonfunctional and leads to accumulation at HGA (and thus pigmentation). (moustafa2024mutationofhmga pages 2-4)

Notably, this work also emphasizes that pyomelanin’s impact on pathogenesis can be **context-dependent**: although pyomelanin is described as a free-radical scavenger (moustafa2024mutationofhmga pages 1-2), the allelic-exchange pigmented/non-pigmented isogenic comparisons found no significant change in oxidative stress resistance or in vivo virulence in their CGD mouse lung infection model. (moustafa2024mutationofhmga pages 1-2)

### 4.2 2023: Environmental chemical perturbation of HPPD and brown pigment readouts
A 2023 *Environmental Science and Pollution Research* paper establishes a **96-well whole-cell colorimetric assay** where pyomelanin-associated absorbance (~OD430) is used as a proxy readout linked to **HPPD activity**, and shows strain-dependent inhibition by **β-triketone herbicides** at agronomical dose multiples. (thiourmauprivez2023assessingtheeffects pages 5-8, thiourmauprivez2023assessingtheeffects pages 1-5)

Quantitatively, increasing sulcotrione dose was reported to reduce the HPPD-linked activity/pigment readout by **≥31% at 1× recommended field dose** and **≥74% at 10×** in their dataset (with strain dependence noted). (thiourmauprivez2023assessingtheeffects pages 8-11)

### 4.3 2024: Consolidation of fungal pyomelanin pathway genes and production engineering concepts
A 2024 review (Microbial Cell Factories) consolidates mechanistic distinctions between DHN-, DOPA-, and pyomelanin, and provides a pyomelanin pathway description from **4-HPP → HGA via HPPD** followed by polymerization. (qin2024melanininfungi pages 10-11, qin2024melanininfungi pages 7-8)

It also reports an engineering example: overexpression of **F. kingsejongi HPPD** in *E. coli* yielding **3.76 ± 0.30 g/L melanin**, positioning HPPD as an engineering lever for soluble melanin/pyomelanin production. (qin2024melanininfungi pages 10-11)

### 4.4 2023: Industrial biotechnology context (engineered yeast) and a cautionary “browning” confounder
A 2023 *Nature Microbiology* study on engineered *Yarrowia lipolytica* clearly describes tyrosine catabolism to HGA and states that once extracellular HGA accumulates, it autoxidizes/polymerizes to pyomelanin, associated with browning. (thomsen2023beetredfood pages 5-6)

However, the same work provides strong caution for trait curation: browning in buffered media was hypothesized to arise from **cyclo‑DOPA/L‑dopachrome decomposition at pH > 4** (eumelanin precursors) and in some conditions was not eliminated by 4HPPD disruption, emphasizing that brown color can have multiple chemical origins even within one organism/assay. (thomsen2023beetredfood pages 6-7, thomsen2023beetredfood pages 5-6)

## 5. Current applications and real-world implementations

### 5.1 Pyomelanin as a functional biomaterial (photoprotection, redox, antimicrobial)
A 2024 study characterizing extracellular dark-brown pyomelanin from *Streptomyces djakartensis* reports multiple application-relevant quantitative metrics: optimized production to **118.73 mg/10 mL**, antioxidant activity (**IC50 18.03 µg/mL**), sunscreen potential (**in vitro SPF = 18.5**), anticancer activity (IC50 values reported across cancer cell lines), and antimicrobial activity against MDR strains (MICs **6.25 µg/mL** and **25 µg/mL** for two strains). (elzawawy2024bioproductionandoptimization pages 1-2)

### 5.2 Environmental and agricultural relevance: herbicide impacts on microbial protective pigmentation
Because HPPD is a known target of β-triketone herbicides in plants and is widespread in microbes, the 2023 study explicitly motivates ecological concern that altering microbial HPPD activity could change pyomelanin production (a protective pigment in multiple microbes), potentially affecting soil microbiota balance and ecosystem services. (thiourmauprivez2023assessingtheeffects pages 1-5)

### 5.3 UV/sterilization-relevant function (emerging evidence)
A 2024 preprint reports experimental designs where purified pyomelanin was added to bacterial suspensions and **UVC (254 nm)** tolerance was evaluated, positioning pyomelanin as a potential modifier of UV disinfection outcomes (though this is preprint evidence and should be curated as “downstream effect; uncertain”). (appella2024beyonduniformitypyomelanin’s pages 19-24)

## 6. Expert opinions and authoritative synthesis (from retrieved authoritative sources)

### 6.1 Review synthesis: melanin classes and pathway modularity
The 2024 fungal melanin review frames melanins as chemically diverse (DOPA-, DHN-, pyomelanin) and emphasizes that pigment phenotype depends on enzyme activities (tyrosinase, PKS, laccase, HPPD) and regulatory networks; for pyomelanin, it explicitly anchors a concise route: **4-HPP --(HPPD)--> HGA → oxidative polymerization → pyomelanin**. (qin2024melanininfungi pages 10-11, qin2024melanininfungi pages 7-8)

### 6.2 Pathogenesis-related synthesis: “pyomelanin is not always a virulence factor”
The 2024 *Microbiology Spectrum* study provides an expert caution relevant to TraitMech downstream edges: while pyomelanin is commonly described as ROS-scavenging and beneficial against oxidative burst, the authors’ isogenic comparisons in *B. cenocepacia* suggest that pigment production did **not** significantly alter H2O2/NO resistance or mouse infection outcome in their model, implying that “pyomelanin → increased virulence/oxidative-stress resistance” should be curated with uncertainty and context qualifiers. (moustafa2024mutationofhmga pages 1-2)

## 7. Recent statistics and quantitative data (from retrieved studies)

* **Herbicide inhibition magnitudes:** HPPD-linked activity/pigment readout decreased with increasing sulcotrione dose by **≥31% at 1× RfD** and **≥74% at 10× RfD** (assay- and strain-dependent). (thiourmauprivez2023assessingtheeffects pages 8-11)
* **Pigment assay specifications (high-throughput):** Whole-cell 96-well assay quantified pyomelanin at **OD430** after 48 h incubation; herbicide concentrations ranged up to **15× RfD** (µM ranges specified). (thiourmauprivez2023assessingtheeffects pages 5-8)
* **Pathogenesis model context:** CGD mouse infection experiments used an intratracheal dose of **1 × 10^3 CFU**; in this model, all mice infected with one strain succumbed by day 4 while another strain showed delayed mortality starting day 9 (context for interpreting pigment vs virulence). (moustafa2024mutationofhmga pages 2-4)
* **Bioprocess metrics (pyomelanin biomaterial):** Optimized melanin production **118.73 mg/10 mL** in *S. djakartensis* with reported antioxidant, SPF, MIC, and anticancer IC50 values. (elzawawy2024bioproductionandoptimization pages 1-2)
* **Engineering yield (reviewed):** HPPD overexpression in *E. coli* reported yield **3.76 ± 0.30 g/L melanin**. (qin2024melanininfungi pages 10-11)

## 8. Warnings / “do not curate yet” items
1) **Do not equate all browning with pyomelanin.** The engineered *Y. lipolytica* system provides direct evidence that brown color can persist after 4HPPD deletion and may be driven by pH-dependent decomposition of other pathway intermediates. Curate such edges as *boundary-case* or *hypothesis*, not as core TraitMech causation. (thomsen2023beetredfood pages 6-7, thomsen2023beetredfood pages 5-6)
2) **Downstream benefit edges (UV shielding, oxidative stress resistance, virulence) are context-dependent.** Evidence for UVC protection is from a preprint and should be tagged uncertain; oxidative-stress/virulence effects vary even within a genus and should not be made universal trait consequences. (appella2024beyonduniformitypyomelanin’s pages 19-24, moustafa2024mutationofhmga pages 1-2)
3) **Preprint evidence:** Pseudomonas UV shielding/structural diversity results are currently from bioRxiv in the retrieved text; treat as provisional until peer-reviewed. (appella2024beyonduniformitypyomelanin’s pages 19-24)

## 9. DOI-first bibliography (with publication dates and URLs)

1) **Moustafa DA, Wu L, Ivey M, Fankhauser SC, Goldberg JB.** *Mutation of hmgA, encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of Burkholderia cenocepacia in a chronic granulomatous disease mouse lung infection.* **Microbiology Spectrum**. Published **29 May 2024** (Issue July 2024). DOI: **10.1128/spectrum.00410-24**. URL: https://doi.org/10.1128/spectrum.00410-24 (moustafa2024mutationofhmga pages 1-2, moustafa2024mutationofhmga pages 2-4)

2) **Qin Y, Xia Y.** *Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering.* **Microbial Cell Factories**. **Dec 2024**. DOI: **10.1186/s12934-024-02614-8**. URL: https://doi.org/10.1186/s12934-024-02614-8 (qin2024melanininfungi pages 7-8, qin2024melanininfungi pages 10-11)

3) **Thiour-Mauprivez C, Dayan FE, Terol H, Devers-Lamrani M, Calvayrac C, Martin-Laurent F, Barthelmebs L.** *Assessing the effects of β-triketone herbicides on HPPD from environmental bacteria using a combination of in silico and microbiological approaches.* **Environmental Science and Pollution Research**. **Sep 2023**. DOI: **10.1007/s11356-022-22801-7**. URL: https://doi.org/10.1007/s11356-022-22801-7 (thiourmauprivez2023assessingtheeffects pages 1-5, thiourmauprivez2023assessingtheeffects pages 5-8, thiourmauprivez2023assessingtheeffects pages 8-11)

4) **Thomsen PT, Meramo S, Ninivaggi L, et al.** *Beet red food colourant can be produced more sustainably with engineered Yarrowia lipolytica.* **Nature Microbiology**. **Nov 2023**. DOI: **10.1038/s41564-023-01517-5**. URL: https://doi.org/10.1038/s41564-023-01517-5 (thomsen2023beetredfood pages 5-6, thomsen2023beetredfood pages 6-7)

5) **El‑Zawawy NA, Kenawy E‑R, Ahmed S, El‑Sapagh S.** *Bioproduction and optimization of newly characterized melanin pigment from Streptomyces djakartensis NSS‑3 with its anticancer, antimicrobial, and radioprotective properties.* **Microbial Cell Factories**. **Jan 2024**. DOI: **10.1186/s12934-023-02276-y**. URL: https://doi.org/10.1186/s12934-023-02276-y (elzawawy2024bioproductionandoptimization pages 1-2)

6) **Appella MND, Kolender A, Oppezzo OJ, López NI, Tribelli PM.** *Beyond uniformity: Pyomelanin’s structural complexity impacts on UV shielding in Pseudomonas species with different lifestyles.* **bioRxiv** (preprint). **Apr 2024**. DOI: **10.1101/2024.04.11.589128**. URL: https://doi.org/10.1101/2024.04.11.589128 (appella2024beyonduniformitypyomelanin’s pages 19-24)


References

1. (moustafa2024mutationofhmga pages 1-2): Dina A. Moustafa, Linda Wu, Melissa Ivey, Sarah C. Fankhauser, and Joanna B. Goldberg. Mutation of <i>hmga</i> , encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of <i>burkholderia cenocepacia</i> in a chronic granulomatous disease mouse lung infection. Jul 2024. URL: https://doi.org/10.1128/spectrum.00410-24, doi:10.1128/spectrum.00410-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

2. (moustafa2024mutationofhmga pages 2-4): Dina A. Moustafa, Linda Wu, Melissa Ivey, Sarah C. Fankhauser, and Joanna B. Goldberg. Mutation of <i>hmga</i> , encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of <i>burkholderia cenocepacia</i> in a chronic granulomatous disease mouse lung infection. Jul 2024. URL: https://doi.org/10.1128/spectrum.00410-24, doi:10.1128/spectrum.00410-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

3. (thiourmauprivez2023assessingtheeffects pages 1-5): Clémence Thiour-Mauprivez, Franck Emmanuel Dayan, Hugo Terol, Marion Devers, Christophe Calvayrac, Fabrice Martin-Laurent, and Lise Barthelmebs. Assessing the effects of β-triketone herbicides on hppd from environmental bacteria using a combination of in silico and microbiological approaches. Environmental Science and Pollution Research, 30:9932-9944, Sep 2023. URL: https://doi.org/10.1007/s11356-022-22801-7, doi:10.1007/s11356-022-22801-7. This article has 5 citations and is from a peer-reviewed journal.

4. (qin2024melanininfungi pages 7-8): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 54 citations and is from a peer-reviewed journal.

5. (qin2024melanininfungi pages 10-11): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 54 citations and is from a peer-reviewed journal.

6. (thomsen2023beetredfood pages 6-7): Philip Tinggaard Thomsen, Samir Meramo, Lorenzo Ninivaggi, Eleonora Pasutto, Mahsa Babaei, Paulo Marcelo Avila-Neto, Marc Cernuda Pastor, Peyman Sabri, Daniela Rago, Tanmay Utsav Parekh, Sara Hunding, Laura Emilie Jul Christiansen, Sumesh Sukumara, and Irina Borodina. Beet red food colourant can be produced more sustainably with engineered yarrowia lipolytica. Nature Microbiology, 8:2290-2303, Nov 2023. URL: https://doi.org/10.1038/s41564-023-01517-5, doi:10.1038/s41564-023-01517-5. This article has 59 citations and is from a highest quality peer-reviewed journal.

7. (thomsen2023beetredfood pages 5-6): Philip Tinggaard Thomsen, Samir Meramo, Lorenzo Ninivaggi, Eleonora Pasutto, Mahsa Babaei, Paulo Marcelo Avila-Neto, Marc Cernuda Pastor, Peyman Sabri, Daniela Rago, Tanmay Utsav Parekh, Sara Hunding, Laura Emilie Jul Christiansen, Sumesh Sukumara, and Irina Borodina. Beet red food colourant can be produced more sustainably with engineered yarrowia lipolytica. Nature Microbiology, 8:2290-2303, Nov 2023. URL: https://doi.org/10.1038/s41564-023-01517-5, doi:10.1038/s41564-023-01517-5. This article has 59 citations and is from a highest quality peer-reviewed journal.

8. (appella2024beyonduniformitypyomelanin’s pages 19-24): Mateo N. Diaz Appella, Adriana Kolender, Oscar J. Oppezzo, Nancy I. López, and Paula M. Tribelli. Beyond uniformity: pyomelanin’s structural complexity impacts on uv shielding in<i>pseudomonas</i>species with different lifestyles. BioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.11.589128, doi:10.1101/2024.04.11.589128. This article has 0 citations.

9. (thiourmauprivez2023assessingtheeffects pages 5-8): Clémence Thiour-Mauprivez, Franck Emmanuel Dayan, Hugo Terol, Marion Devers, Christophe Calvayrac, Fabrice Martin-Laurent, and Lise Barthelmebs. Assessing the effects of β-triketone herbicides on hppd from environmental bacteria using a combination of in silico and microbiological approaches. Environmental Science and Pollution Research, 30:9932-9944, Sep 2023. URL: https://doi.org/10.1007/s11356-022-22801-7, doi:10.1007/s11356-022-22801-7. This article has 5 citations and is from a peer-reviewed journal.

10. (elzawawy2024bioproductionandoptimization pages 1-2): Nessma A. El-Zawawy, El-Refaie Kenawy, Sara Ahmed, and Shimaa El-Sapagh. Bioproduction and optimization of newly characterized melanin pigment from streptomyces djakartensis nss-3 with its anticancer, antimicrobial, and radioprotective properties. Microbial Cell Factories, Jan 2024. URL: https://doi.org/10.1186/s12934-023-02276-y, doi:10.1186/s12934-023-02276-y. This article has 47 citations and is from a peer-reviewed journal.

11. (thiourmauprivez2023assessingtheeffects pages 8-11): Clémence Thiour-Mauprivez, Franck Emmanuel Dayan, Hugo Terol, Marion Devers, Christophe Calvayrac, Fabrice Martin-Laurent, and Lise Barthelmebs. Assessing the effects of β-triketone herbicides on hppd from environmental bacteria using a combination of in silico and microbiological approaches. Environmental Science and Pollution Research, 30:9932-9944, Sep 2023. URL: https://doi.org/10.1007/s11356-022-22801-7, doi:10.1007/s11356-022-22801-7. This article has 5 citations and is from a peer-reviewed journal.