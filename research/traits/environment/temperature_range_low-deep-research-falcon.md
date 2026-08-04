---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:15:21.334935'
end_time: '2026-08-04T04:26:11.093625'
duration_seconds: 649.76
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range low
  trait_identifier: METPO:1000449
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range spans approximately 10\u201322 \xB0C, characteristic of psychrophilic\
    \ or psychrotolerant physiology."
  parent_traits: METPO:1000306
  synonyms: Psychrophile, Psychrotolerant, TR_10_to_22
  evidence_summary: "DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile\
    \ review supports cool-temperature membrane and enzyme adaptation as the basis\
    \ of growth in the 10\u201322 \xB0C range.)"
  causal_graph_summary: 'temperature_range_low_psychrotolerant: 13 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000449
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 10–22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, Psychrotolerant, TR_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cool-temperature membrane and enzyme adaptation as the basis of growth in the 10–22 °C range.)
- **Existing causal graph summary:** temperature_range_low_psychrotolerant: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_low.yaml`.

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
- **Trait label:** temperature range low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000449
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 10–22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, Psychrotolerant, TR_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cool-temperature membrane and enzyme adaptation as the basis of growth in the 10–22 °C range.)
- **Existing causal graph summary:** temperature_range_low_psychrotolerant: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_low.yaml`.

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


# Curation report: microbial “temperature range low”

## Executive recommendation

**Trait:** temperature range low  
**Identifier:** **METPO:1000449**  
**Parent:** METPO:1000306  
**Category/kind/status:** ENVIRONMENT / CLASS / REVIEWED

The supplied trait should be represented as an **assay-observed capacity for sustained microbial growth over an approximately 10–22 °C ambient-temperature interval**, rather than as a taxonomic assertion that an organism is obligatorily psychrophilic. The best-supported causal architecture is multifactorial: low temperature perturbs membranes, RNA folding and translation, enzyme kinetics, ice/water relations, and redox balance; organisms compensate through lipid remodeling, cold-active RNA/protein machinery, cryoprotective molecules, and stress defenses. Recent work also shows that canonical mechanisms cannot automatically be treated as necessary determinants of low-temperature growth in every organism.

The strongest perturbation evidence recovered is a taxon-specific branch in *Shewanella livingstonensis* Ac10: EPA deficiency causes growth retardation and filamentous cells at 4 °C, while EPA supplementation rescues these defects. This lies below the stated 10–22 °C band, so it supports the broader mechanism of cold growth but should not alone define METPO:1000449.

## 1. Trait scope and boundary cases

### Recommended operational interpretation

METPO:1000449 denotes a **growth-range phenotype**, requiring positive evidence of growth at multiple assay temperatures sufficient to establish that the supporting interval spans approximately 10–22 °C. “Growth” should preferably mean increasing biomass, viable counts, colony formation, or another validated reproduction measure, not merely survival or metabolic activity.

A widely used physiological definition describes psychrophiles as organisms with an optimum at or below approximately 15 °C and an upper growth limit near 20 °C. Consequently, a 10–22 °C range crosses the conventional psychrophile boundary and may also describe psychrotolerant organisms. The supplied synonyms are therefore useful search labels but are not strictly interchangeable taxonomic diagnoses (purwar2024adaptationsofpsychrophilic pages 8-10).

### Exclusions and nearby traits

* **Optimum-temperature phenotype:** An optimum at 10–22 °C does not establish that the entire range is growth-supporting.
* **Minimum growth temperature:** Growth at one low temperature does not establish a range.
* **Cold-shock response:** A transient shift, such as 37→15 °C, measures acclimation and RNA/protein stress responses rather than an evolved cardinal growth range.
* **Freeze tolerance or cryosurvival:** Viability after freezing, antifreeze activity, or ice-recrystallization inhibition does not prove growth between 10 and 22 °C.
* **Psychrophily versus psychrotolerance:** These labels depend on both optimum and maximum growth temperatures; neither should be inferred from this trait alone.
* **Cold-active enzyme phenotype:** Activity of an isolated enzyme at low temperature is mechanistically relevant but insufficient to assign the organism-level growth trait.
* **Food-refrigeration growth:** Growth at 4–7 °C is relevant supporting evidence for cold adaptation, but it is outside the nominal lower boundary and should remain assay-qualified.

## 2. Current mechanistic understanding

Low temperature tends to rigidify/thicken lipid bilayers, stabilize inhibitory RNA secondary structures, reduce reaction rates, increase oxygen solubility and associated ROS pressure, and—near or below freezing—promote damaging ice formation. Current reviews emphasize that successful cold growth is not attributable to one universal “psychrophile gene”; it is an integrated systems phenotype involving membranes, transcription/translation, protein structure, osmotic balance, and redox homeostasis (purwar2024adaptationsofpsychrophilic pages 10-11, ramon2023ageneraloverview pages 21-22).

A key expert-level qualification comes from Sidarta and colleagues’ 2024 *Bacillus subtilis* study. The canonical DesK–DesR–Des circuit was only detectably activated by a mild shift to 25 °C after 120 min (P=0.03), not by shifts to 16 or 4 °C. Moreover, *des*, *desK*, and *desR* deletion mutants lacked detectable temperature-stress growth defects under the tested conditions. The authors concluded that phase separation can impair DesK sensing and that Des-mediated fluidity changes may be too subtle to determine growth under harsh cold shock (sidarta2024lipidphaseseparation pages 5-9, sidarta2024lipidphaseseparation pages 14-16, sidarta2024lipidphaseseparation pages 1-2). Thus, membrane remodeling remains important broadly, but individual lipid-sensing circuits must be curated as taxon- and condition-specific.

## 3. Candidate nodes

Identifiers below are deliberately conservative. Gene symbols should be stored with an organism qualifier; UniProt, EC, Rhea, KEGG, or MetaCyc accessions should be added only after strain-specific verification.

### Trait and environmental nodes

| Node | Grounding | Role |
|---|---|---|
| temperature range low | **METPO:1000449** | Target phenotype |
| parent temperature-range trait | **METPO:1000306** | Ontological parent |
| ambient temperature, approximately 10–22 °C | Label-only assay node | Exposure defining the phenotype |
| low-temperature exposure/cold shock | GO:0009409, response to cold | Mechanistic experimental exposure; not equivalent to the trait |
| freezing/ice formation | Label-only environmental process | Relevant mainly below the nominal range |

### Cellular structures and processes

| Node | Suggested grounding | Role |
|---|---|---|
| plasma/cytoplasmic membrane | GO:0005886 | Primary site of lipid compensation |
| membrane fluidity | GO:0061024, membrane organization, is a broader fallback | Phenomenon requiring careful relation modeling |
| fatty-acid desaturation | GO:0006636 | Lipid-remodeling process |
| translation | GO:0006412 | Cold-sensitive process supported by ribosomal/RNA machinery |
| RNA helicase activity | GO:0003724 | Unwinds stabilized RNA structures |
| cell division | GO:0051301 | EPA-sensitive phenotype in *Shewanella* |
| response to oxidative stress | GO:0006979 | Candidate secondary cold-stress module |
| ice binding | GO:0050825 | Molecular function of antifreeze/ice-binding proteins |

### Genes, proteins, and complexes

* **DesK**, membrane histidine kinase/thermosensor—*B. subtilis*-specific.
* **DesR**, response regulator—*B. subtilis*-specific.
* **des/Des**, Δ5 acyl-lipid desaturase—*B. subtilis*-specific.
* **FAD Δ6/Δ9/Δ12/Δ15 enzymes**, psychrophilic-yeast candidate family; retain label-only until species-specific orthology is verified.
* **pfa biosynthetic machinery**, bacterial long-chain-PUFA synthesis; strain-specific gene grounding required.
* **fadH/sl_1351**, 2,4-dienoyl-CoA reductase involved in DHA→EPA conversion in *S. livingstonensis* Ac10.
* **CsdA**, DEAD-box RNA helicase in *E. coli*.
* **RNase R** and **PNPase**, low-temperature RNA-metabolism proteins in *E. coli*.
* **Cold-shock proteins**, RNA chaperones; generic family node unless a specific paralog is experimentally tested.
* **Antifreeze/ice-binding proteins**, generic functional class.
* **Cold-active enzymes**, generic class; individual enzyme nodes are preferable.

### Chemicals and metabolites

| Node | Suggested CURIE |
|---|---|
| eicosapentaenoic acid (EPA) | CHEBI:28364 |
| docosahexaenoic acid (DHA) | CHEBI:36005 |
| linoleic acid | CHEBI:17351 |
| α-linolenic acid | CHEBI:27432 |
| trehalose | CHEBI:27082 |
| glycine betaine | CHEBI:17750 |
| glycerol | CHEBI:17754 |
| unsaturated fatty acids / polyunsaturated fatty acids | Use the appropriate CHEBI class after release-level verification |
| exopolysaccharide | Label-only class unless composition is known |
| reactive oxygen species | Use species-specific CHEBI nodes where measured |

### Organisms/taxa

Useful taxon-scoped branches include *Shewanella livingstonensis* Ac10, *Bacillus subtilis*, *Escherichia coli*, *Glaciozyma antarctica* PI12, *Pseudoalteromonas haloplanktis* TAC125, and psychrophilic yeasts more broadly. Strain-level NCBITaxon identifiers should be verified directly before YAML insertion; names alone are safer than an incorrect CURIE.

## 4. Candidate evidence-backed causal edges

The following compact prioritization separates direct perturbation evidence from association and review-level inference.

| Candidate triple | Evidence grade | Taxon/assay | Key quantitative support | Curation action |
|---|---|---|---|---|
| eicosapentaenoic acid (EPA) availability **positively regulates** growth at 4 °C | High | *Shewanella livingstonensis* Ac10; mutant/supplementation at 4 °C vs 18 °C | EPA-less mutant shows growth retardation at 4 °C but normal phenotype at 18 °C; EPA supplementation suppresses cold-sensitive phenotype (ogawa2020bioconversionfromdocosahexaenoic pages 1-2, yoshida2016bacteriallongchainpolyunsaturated pages 9-10) | Curate as high-confidence, taxon-scoped edge |
| EPA availability **positively regulates** normal cell division / normal cell length at 4 °C | High | *S. livingstonensis* Ac10 ΔEPA/sl_1351; microscopy/cell-length distribution at 4 °C | With EPA, ~90% of cells are 2–4 µm (avg 3.0 ± 0.8 µm); with DHA only ~50% are 2–4 µm and 43% are 4–6 µm (avg 4.3 ± 1.7 µm), showing partial but inferior rescue (ogawa2020bioconversionfromdocosahexaenoic pages 9-11, ogawa2020bioconversionfromdocosahexaenoic media cbc63530) | Curate as high-confidence morphology-linked edge |
| fadH / DHA→EPA conversion capacity **positively regulates** EPA production under DHA-supplemented conditions | High | *S. livingstonensis* Ac10; gene disruption and biochemical conversion assay | *fadH* disruption impaired EPA production; estimated DHA→EPA conversion rate decreased by 86% vs parent strain (ogawa2020bioconversionfromdocosahexaenoic pages 1-2) | Curate as high-confidence gene→metabolite edge, but not as universal cold-growth mechanism |
| low temperature / cold exposure **decreases** membrane fluidity (increases rigidification/thickening) | Moderate | Broad bacteria/yeasts; mechanistic synthesis plus DesK model | Repeatedly described as the initiating physical stress requiring compensation; recent in vivo DesK work supports only subtle sensing under mild shifts and limited contribution under harsh stress (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 5-9, ramon2023ageneraloverview pages 21-22) | Curate as broad mechanistic edge with general-scope note |
| DesK **positively regulates** DesR phosphorylation/signaling, which **positively regulates** des expression during mild cold adaptation | Moderate | *Bacillus subtilis*; temperature-shift reporter assays and prior model | 2024 study found significant Pdes increase only after 120 min at 25 °C (P=0.03), with no significant activation at 16 °C or 4 °C; deletion mutants showed no temperature sensitivity under tested harsh conditions (sidarta2024lipidphaseseparation pages 5-9, sidarta2024lipidphaseseparation pages 1-2) | Curate only as mild-cold regulatory edge with explicit negative-result warning |
| fatty acid desaturase genes (FAD; Δ6/Δ9/Δ12/Δ15) **positively regulate** C18 unsaturated/PUFA synthesis | Moderate | Psychrophilic yeasts; comparative genomics and transcript patterns | 9 psychrophilic vs 3 mesophilic yeast genomes; psychrophiles retain diverse FAD genes and can synthesize C18:2/C18:3/C18:4, whereas mesophiles lost most of these genes (liu2023psychrophilicyeastsinsights pages 1-2, liu2023psychrophilicyeastsinsights pages 4-5, liu2023psychrophilicyeastsinsights pages 5-7) | Curate as genomic/transcriptomic inference, not direct perturbation |
| C18 unsaturated fatty acids / PUFAs **positively regulate** membrane fluidity | Moderate | Psychrophilic yeasts and broader cold-adapted microbes | Reviews and comparative genomics consistently infer PUFA enrichment maintains transport and membrane-protein-associated reactions at low temperature; direct perturbation is limited outside specific taxa (liu2023psychrophilicyeastsinsights pages 4-5, liu2023psychrophilicyeastsinsights pages 5-7, ramon2023ageneraloverview pages 21-22) | Curate as conservative metabolite→process edge with inference tag |
| CsdA RNA helicase **positively regulates** low-temperature RNA metabolism / translation competence | Moderate | *Escherichia coli*; 37→15 °C cold-shift, deletion/overexpression transcriptomics | CsdA is required specifically at low temperature; helicase activity is necessary for mRNA degradation function; RNase R can substitute partly via helicase activity, whereas PNPase cannot (phadtare2012escherichiacolicold‐shock pages 1-2) | Curate as low-temperature RNA-metabolism edge, assay-scoped to cold shock/15 °C |
| antifreeze proteins / ice-binding proteins **negatively regulate** ice crystal growth | Moderate | Antarctic bacteria/yeasts; biochemical and review evidence | Recent reviews summarize AFP-mediated thermal hysteresis and ice recrystallization inhibition; psychrophilic yeasts reported to carry multiple antifreezing genes, but causal linkage to the 10–22 °C growth band is indirect (ramasamy2023comprehensiveinsightson pages 3-4, liu2023psychrophilicyeastsinsights pages 5-7, ramon2023ageneraloverview pages 12-14) | Curate only as optional environment-specific protection edge, not core growth-range determinant |
| compatible solutes (e.g., trehalose, glycine betaine, glycerol) **positively regulate** protein/membrane stability during cold stress | Uncertain | Broad psychrophiles/psychrotolerants; review-level evidence | Reviews report accumulation to high levels and roles in freezing-point depression, protein stabilization, osmotic balance, and free-radical scavenging, but direct perturbation tied to this trait is sparse (purwar2024adaptationsofpsychrophilic pages 10-11, ramasamy2023comprehensiveinsightson pages 3-4, ramon2023ageneraloverview pages 21-22) | Hold for later unless primary mutant or supplementation evidence is added |
| oxidative-stress response pathways **positively regulate** cold adaptation / low-temperature survival | Uncertain | Psychrophilic yeasts and broad cold-adapted microbes; omics/review evidence | Comparative yeast genomics found enrichment of glutathione/peroxisome metabolism; reviews note increased oxygen solubility and ROS at low temperature, but direct trait-level causality remains indirect (liu2023psychrophilicyeastsinsights pages 4-5, purwar2024adaptationsofpsychrophilic pages 10-11) | Do not yet curate into core graph without primary perturbation support |


*Table: This table prioritizes the most curation-ready causal edges for METPO:1000449, distinguishing direct experimental support from broader review-based inference. It is useful for selecting conservative graph edges while flagging mechanisms that remain taxon-specific or insufficiently causal.*

### Expanded edge notes and supporting snippets

| # | Subject–predicate–object | Evidence and supporting snippet | Curation note |
|---|---|---|---|
| 1 | **low temperature → decreases → membrane fluidity** | Reviews describe cold-induced membrane rigidity and compensatory enrichment of short-chain, branched, cis-unsaturated lipids (purwar2024adaptationsofpsychrophilic pages 8-10, ramon2023ageneraloverview pages 21-22). | Broadly credible, but represent temperature and membrane state separately; avoid implying identical magnitude across taxa. |
| 2 | **DesK → activates → DesR signaling** | The accepted model is that cold-induced membrane thickening changes DesK kinase activity, leading to DesR activation (sidarta2024lipidphaseseparation pages 1-2). | Moderate; *B. subtilis*-specific. The 2024 in-vivo results restrict it to subtle/mild shifts. |
| 3 | **DesR signaling → increases → des transcription** | “Cold-induced membrane thickening normally activates DesK…leading to DesR phosphorylation and des expression” (sidarta2024lipidphaseseparation pages 1-2). | Curate as a regulatory edge, not as a necessary direct cause of METPO:1000449. |
| 4 | **Des activity → increases → membrane unsaturation** | Des introduces double bonds into membrane phospholipid acyl chains; this is the canonical compensatory response summarized in recent reviews (pathania2021adaptationtocold pages 220-223, ramon2023ageneraloverview pages 12-14). | Mechanistically sound in the model organism, but downstream growth benefit was not detected in Sidarta 2024. |
| 5 | **psychrophilic-yeast FAD genes → increase → C18 PUFA synthesis** | In nine psychrophilic versus three mesophilic yeast genomes, Δ6/Δ9/Δ12/Δ15 FAD genes were diverse and broadly retained in psychrophiles, while mesophiles had lost most; *G. antarctica* FAD expression changed at 15, 0 and −12 °C (liu2023psychrophilicyeastsinsights pages 5-7, liu2023psychrophilicyeastsinsights pages 1-2). | Moderate association/transcript evidence; label uncertain until gene-specific perturbation is available. |
| 6 | **C18 PUFAs → increase → membrane fluidity at low temperature** | The yeast study states that altered PUFA content may maintain fluidity needed for nutrient transport and membrane-protein reactions (liu2023psychrophilicyeastsinsights pages 4-5). | Inferred. Preserve “may” and do not elevate comparative genomics to direct causality. |
| 7 | **EPA deficiency → decreases → growth at 4 °C** | “EPA-less mutants grow normally at 18°C but show significantly inhibited growth at 4°C”; exogenous EPA-containing phospholipid rescues growth (ogawa2020bioconversionfromdocosahexaenoic pages 1-2, yoshida2016bacteriallongchainpolyunsaturated pages 9-10). | High-confidence, direct mutant/rescue edge; explicitly *S. livingstonensis* Ac10 and 4 °C. |
| 8 | **EPA availability → promotes → normal cell division/cell length at 4 °C** | EPA supplementation returned approximately 90% of cells to 2–4 µm, mean 3.0 ± 0.8 µm. DHA gave only partial rescue: about 50% were 2–4 µm and 43% were 4–6 µm, mean 4.3 ± 1.7 µm (ogawa2020bioconversionfromdocosahexaenoic pages 9-11). Figure 5 independently shows the growth and cell-length distributions and sample sizes (ogawa2020bioconversionfromdocosahexaenoic media cbc63530). | Highest-value causal edge. It may involve specific membrane functions, not merely bulk fluidity. |
| 9 | **fadH/sl_1351 activity → enables → DHA-to-EPA conversion** | Gene disruption reduced the estimated conversion rate by **86%**; recombinant FadH acted on the DHA-derived 2,4-dienoyl-CoA intermediate (ogawa2020bioconversionfromdocosahexaenoic pages 1-2). | High-confidence biochemical edge. Link onward to cold growth only through EPA availability and with taxon scope. |
| 10 | **CsdA helicase activity → supports → low-temperature RNA metabolism** | Following a 37→15 °C shift, CsdA was required specifically at low temperature; helicase activity was required for its mRNA-degradation role. RNase R could substitute through helicase activity, whereas PNPase could not (phadtare2012escherichiacolicold‐shock pages 1-2). | Moderate/high for the molecular process; cold-shock assay does not by itself prove the 10–22 °C range phenotype. |
| 11 | **cold-induced RNA helicases/RNA chaperones → promote → translation competence** | At 4 °C, approximately 30% of upregulated proteins reported for *P. haloplanktis* were ribosomal proteins or RNA chaperones; helicases were interpreted as relieving stable RNA structures (purwar2024adaptationsofpsychrophilic pages 4-6). | Omics/review support only; curate as uncertain unless tied to a perturbation study. |
| 12 | **antifreeze proteins → inhibit → ice-crystal growth/recrystallization** | AFPs bind ice, inhibit crystal growth, and generate thermal hysteresis; recent Antarctic reviews also report ice-recrystallization inhibition (ramasamy2023comprehensiveinsightson pages 3-4, ramon2023ageneraloverview pages 12-14). | Molecular edge is credible; connection to growth at 10–22 °C is weak because ice is generally absent. Optional peripheral branch only. |
| 13 | **compatible solutes → stabilize → proteins and membranes during cold/freezing stress** | Glycine betaine, trehalose, glycerol, sucrose and polyols are reported to stabilize proteins/membranes, balance osmotic stress, and scavenge radicals (purwar2024adaptationsofpsychrophilic pages 10-11, ramasamy2023comprehensiveinsightson pages 3-4). | Review-level, chemically heterogeneous; hold unless a primary perturbation is added. |
| 14 | **increased catalytic-region flexibility → increases → low-temperature enzyme activity** | Cold-adapted enzymes are described as having greater structural flexibility and high activity down to very low temperature; psychrophilic *P. syringae* RNase R has an activity optimum of 22 °C versus 37 °C for the *E. coli* enzyme (garcialopez2021identificationofbiomolecules pages 4-6, pathania2021adaptationtocold pages 220-223). | Useful mechanistic module, but “flexibility” must be attached to a specific protein and assay before curation. |
| 15 | **cold-associated ROS pressure → induces/supports → antioxidant pathways** | Recent reviews link higher oxygen solubility to ROS stress, while psychrophilic-yeast comparative genomics found enrichment in glutathione and peroxisome pathways (purwar2024adaptationsofpsychrophilic pages 10-11, liu2023psychrophilicyeastsinsights pages 4-5). | Association only; no direct mutant evidence recovered. Do not place in the core graph yet. |

## 5. Recent developments, 2023–2024

1. **Comparative psychrophilic-yeast genomics (January 2023).** Analysis of nine psychrophilic and three mesophilic yeast genomes highlighted diverse Δ6/Δ9/Δ12/Δ15 desaturases and antifreeze-protein repertoires. The authors explicitly used cautious language—PUFA synthesis “may” improve membrane fluidity—and noted unresolved mechanisms, so these results generate candidates rather than prove organism-level causation (liu2023psychrophilicyeastsinsights pages 5-7, liu2023psychrophilicyeastsinsights pages 4-5, liu2023psychrophilicyeastsinsights pages 1-2).

2. **Multifactorial rather than single-pathway models (July 2023).** Ramón and colleagues synthesized membrane remodeling, cold-shock proteins, antifreeze proteins, compatible solutes, transport, enzyme adaptation and nucleic-acid chaperoning into an integrated model, warning implicitly against a single universal cold-adaptation determinant (ramon2023ageneraloverview pages 21-22).

3. **Antarctic bacterial systems and applications (June 2023).** Ramasamy and colleagues emphasized ice-binding proteins, compatible osmolytes, stress proteins, pigments, omics and enzyme engineering. Their synthesis is authoritative for candidate discovery but remains mainly review-level evidence (ramasamy2023comprehensiveinsightson pages 3-4).

4. **Important negative evidence for a canonical pathway (June 2024).** Sidarta and colleagues found that harsh cold induced membrane phase separation but not robust Des-system reporter activation; DesK colocalized with fluid domains at approximately 40–80% under cold shock, compared with about 20% under heat shock. *des/desK/desR* deletion strains had no detectable cold-growth phenotype under the conditions tested (sidarta2024lipidphaseseparation pages 5-9, sidarta2024lipidphaseseparation pages 14-16). This is the most consequential recent result for curation: **DesK–DesR–Des should not be encoded as a universal necessary route to low-temperature growth.**

5. **Current data limitation.** Much 2023–2024 literature remains comparative-genomic, transcriptomic, or review-based. Direct CRISPR/deletion-rescue studies that measure cardinal growth temperatures or the complete 10–22 °C growth range remain uncommon.

## 6. Applications and real-world relevance

Cold-adapted enzymes and organisms are used or investigated for refrigerated food processing, detergents that operate at low wash temperatures, lignocellulosic biomass conversion, cold-region hydrocarbon bioremediation, bioethanol production, textile processing, and agricultural nutrient cycling. Cold catalysis can lower process energy demand and reduce unwanted heat-dependent reactions (garcialopez2021identificationofbiomolecules pages 4-6, purwar2024adaptationsofpsychrophilic pages 13-15).

Specific biomolecule opportunities include cold-active lipases, amylases, proteases, cellulases and β-galactosidases; EPA/DHA biosynthesis and conversion are also relevant to nutritional biotechnology. The *Shewanella* FadH result provides a concrete engineering target: disrupting *fadH* reduced DHA→EPA conversion by 86%, demonstrating pathway leverage, although production optimization is distinct from assigning METPO:1000449 (ogawa2020bioconversionfromdocosahexaenoic pages 1-2).

Cold-growth mechanisms also have risk-management applications. Psychrotolerant food-spoilage organisms and pathogens can grow under refrigeration, making accurate distinction between growth range, survival and cold-shock response important for predictive microbiology (purwar2024adaptationsofpsychrophilic pages 3-4).

## 7. Recommended minimal TraitMech graph

A conservative first revision should prioritize nodes and edges that are either general physical relationships or directly tested:

1. **low ambient temperature → decreases → membrane fluidity**;
2. **fatty-acid desaturation → increases → unsaturated membrane lipids**;
3. **unsaturated membrane lipids → increase → membrane functional competence at low temperature** *(moderate/inferred)*;
4. ***S. livingstonensis* pfa/EPA biosynthetic capacity → increases → EPA availability** *(taxon-specific)*;
5. **EPA availability → promotes → low-temperature growth** *(taxon-specific, direct)*;
6. **EPA availability → promotes → normal cell division at low temperature** *(taxon-specific, direct)*;
7. **fadH activity → enables → DHA-to-EPA conversion** *(taxon-specific, direct)*;
8. **CsdA helicase activity → supports → low-temperature RNA metabolism** *(assay-specific)*;
9. **low-temperature RNA metabolism/translation competence → supports → growth at low temperature** *(mechanistically plausible but indirect)*;
10. **cold-active enzyme catalysis → supports → metabolic flux at low temperature** *(protein-specific evidence required)*.

Keep AFP, EPS, compatible-solute and oxidative-stress branches outside the minimal core until trait-matched perturbation evidence is attached.

## 8. Warnings: claims not yet ready for TraitMech

* Do **not** equate “psychrophile,” “psychrotolerant,” and METPO:1000449 without cardinal-temperature data.
* Do **not** infer a 10–22 °C growth range from one growth point, cold-shock transcription, enzyme activity, or freeze survival.
* Do **not** curate DesK–DesR–Des as necessary for cold growth. The 2024 deletion and reporter results provide explicit counterevidence under harsh cold-shock conditions (sidarta2024lipidphaseseparation pages 5-9, sidarta2024lipidphaseseparation pages 1-2).
* Do **not** generalize EPA dependence from *S. livingstonensis* to all bacteria. In this organism, EPA appears to support particular membrane-associated functions and cell division; long-chain PUFA effects need not operate solely through global membrane fluidity (ogawa2020bioconversionfromdocosahexaenoic pages 9-11, yoshida2016bacteriallongchainpolyunsaturated pages 9-10).
* Do **not** treat FAD-gene enrichment in psychrophilic yeasts as perturbation-proven causality. It is comparative-genomic and transcript-level evidence (liu2023psychrophilicyeastsinsights pages 5-7, liu2023psychrophilicyeastsinsights pages 1-2).
* Do **not** connect antifreeze proteins directly to growth at 10–22 °C unless ice-containing assay conditions are documented.
* Do **not** curate generic “enzyme flexibility” without a named enzyme, structural measurement, activity assay and taxon.
* Do **not** add unverified UniProt, EC, Rhea, KEGG, MetaCyc or strain-level NCBITaxon identifiers. Label-only nodes are preferable to incorrect grounding.
* The supplied existing evidence, DOI **10.1038/sj.embor.7400662**, is appropriate as a broad review anchor for membrane and enzyme adaptation, but its phrasing should be corrected conceptually: cold **decreases** membrane fluidity, whereas adaptive lipid remodeling counteracts that decrease.

## DOI-first bibliography

1. Sidarta M, et al. **Lipid phase separation impairs membrane thickness sensing by the *Bacillus subtilis* sensor kinase DesK.** *Microbiology Spectrum*. Published June 2024. DOI: [10.1128/spectrum.03925-23](https://doi.org/10.1128/spectrum.03925-23). Primary study; crucial negative evidence (sidarta2024lipidphaseseparation pages 5-9, sidarta2024lipidphaseseparation pages 1-2).
2. Purwar S, Srivastava S. **Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.** *Applied Microbiology: Theory & Technology*. Published October 2024. DOI: [10.37256/amtt.5220244537](https://doi.org/10.37256/amtt.5220244537) (purwar2024adaptationsofpsychrophilic pages 10-11, purwar2024adaptationsofpsychrophilic pages 8-10).
3. Liu H, et al. **Psychrophilic Yeasts: Insights into Their Adaptability to Extremely Cold Environments.** *Genes*. Published January 2023;14:158. DOI: [10.3390/genes14010158](https://doi.org/10.3390/genes14010158) (liu2023psychrophilicyeastsinsights pages 5-7, liu2023psychrophilicyeastsinsights pages 1-2).
4. Ramón A, et al. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology*. Published July 2023;54:2259–2287. DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4) (ramon2023ageneraloverview pages 21-22, ramon2023ageneraloverview pages 12-14).
5. Ramasamy KP, et al. **Comprehensive insights on environmental adaptation strategies in Antarctic bacteria and biotechnological applications of cold adapted molecules.** *Frontiers in Microbiology*. Published June 2023;14:1197797. DOI: [10.3389/fmicb.2023.1197797](https://doi.org/10.3389/fmicb.2023.1197797) (ramasamy2023comprehensiveinsightson pages 3-4).
6. Ogawa T, et al. **Bioconversion From Docosahexaenoic Acid to Eicosapentaenoic Acid in the Marine Bacterium *Shewanella livingstonensis* Ac10.** *Frontiers in Microbiology*. Published May 26, 2020;11:1104. DOI: [10.3389/fmicb.2020.01104](https://doi.org/10.3389/fmicb.2020.01104) (ogawa2020bioconversionfromdocosahexaenoic pages 1-2, ogawa2020bioconversionfromdocosahexaenoic media cbc63530).
7. Yoshida K, et al. **Bacterial Long-Chain Polyunsaturated Fatty Acids: Their Biosynthetic Genes, Functions, and Practical Use.** *Marine Drugs*. Published May 2016;14:94. DOI: [10.3390/md14050094](https://doi.org/10.3390/md14050094) (yoshida2016bacteriallongchainpolyunsaturated pages 9-10).
8. Phadtare S. **Escherichia coli cold-shock gene profiles in response to over-expression/deletion of CsdA, RNase R and PNPase and relevance to low-temperature RNA metabolism.** *Genes to Cells*. Published October 2012;17:850–874. DOI: [10.1111/gtc.12002](https://doi.org/10.1111/gtc.12002) (phadtare2012escherichiacolicold‐shock pages 1-2).
9. Garcia-Lopez E, Alcazar P, Cid C. **Identification of Biomolecules Involved in the Adaptation to the Environment of Cold-Loving Microorganisms and Metabolic Pathways for Their Production.** *Biomolecules*. Published August 2021;11:1155. DOI: [10.3390/biom11081155](https://doi.org/10.3390/biom11081155) (garcialopez2021identificationofbiomolecules pages 4-6).
10. Pathania S, et al. **Adaptation to Cold Environment: The Survival Strategy of Psychrophiles.** Published December 2021. DOI: [10.1007/978-981-16-2625-8_4](https://doi.org/10.1007/978-981-16-2625-8_4) (pathania2021adaptationtocold pages 220-223).

References

1. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

2. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

3. (ramon2023ageneraloverview pages 21-22): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

4. (sidarta2024lipidphaseseparation pages 5-9): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 6 citations and is from a domain leading peer-reviewed journal.

5. (sidarta2024lipidphaseseparation pages 14-16): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 6 citations and is from a domain leading peer-reviewed journal.

6. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 6 citations and is from a domain leading peer-reviewed journal.

7. (ogawa2020bioconversionfromdocosahexaenoic pages 1-2): Takuya Ogawa, Kazuki Hirose, Yustina Yusuf, Jun Kawamoto, and Tatsuo Kurihara. Bioconversion from docosahexaenoic acid to eicosapentaenoic acid in the marine bacterium shewanella livingstonensis ac10. Frontiers in Microbiology, May 2020. URL: https://doi.org/10.3389/fmicb.2020.01104, doi:10.3389/fmicb.2020.01104. This article has 10 citations and is from a peer-reviewed journal.

8. (yoshida2016bacteriallongchainpolyunsaturated pages 9-10): Kiyohito Yoshida, Mikako Hashimoto, Ryuji Hori, Takumi Adachi, Hidetoshi Okuyama, Yoshitake Orikasa, Tadashi Nagamine, Satoru Shimizu, Akio Ueno, and Naoki Morita. Bacterial long-chain polyunsaturated fatty acids: their biosynthetic genes, functions, and practical use. Marine Drugs, 14:94, May 2016. URL: https://doi.org/10.3390/md14050094, doi:10.3390/md14050094. This article has 142 citations.

9. (ogawa2020bioconversionfromdocosahexaenoic pages 9-11): Takuya Ogawa, Kazuki Hirose, Yustina Yusuf, Jun Kawamoto, and Tatsuo Kurihara. Bioconversion from docosahexaenoic acid to eicosapentaenoic acid in the marine bacterium shewanella livingstonensis ac10. Frontiers in Microbiology, May 2020. URL: https://doi.org/10.3389/fmicb.2020.01104, doi:10.3389/fmicb.2020.01104. This article has 10 citations and is from a peer-reviewed journal.

10. (ogawa2020bioconversionfromdocosahexaenoic media cbc63530): Takuya Ogawa, Kazuki Hirose, Yustina Yusuf, Jun Kawamoto, and Tatsuo Kurihara. Bioconversion from docosahexaenoic acid to eicosapentaenoic acid in the marine bacterium shewanella livingstonensis ac10. Frontiers in Microbiology, May 2020. URL: https://doi.org/10.3389/fmicb.2020.01104, doi:10.3389/fmicb.2020.01104. This article has 10 citations and is from a peer-reviewed journal.

11. (liu2023psychrophilicyeastsinsights pages 1-2): Haisheng Liu, Guiliang Zheng, Zhongwei Chen, Xiaoya Ding, Jinran Wu, Haili Zhang, and Shulei Jia. Psychrophilic yeasts: insights into their adaptability to extremely cold environments. Genes, 14:158, Jan 2023. URL: https://doi.org/10.3390/genes14010158, doi:10.3390/genes14010158. This article has 24 citations.

12. (liu2023psychrophilicyeastsinsights pages 4-5): Haisheng Liu, Guiliang Zheng, Zhongwei Chen, Xiaoya Ding, Jinran Wu, Haili Zhang, and Shulei Jia. Psychrophilic yeasts: insights into their adaptability to extremely cold environments. Genes, 14:158, Jan 2023. URL: https://doi.org/10.3390/genes14010158, doi:10.3390/genes14010158. This article has 24 citations.

13. (liu2023psychrophilicyeastsinsights pages 5-7): Haisheng Liu, Guiliang Zheng, Zhongwei Chen, Xiaoya Ding, Jinran Wu, Haili Zhang, and Shulei Jia. Psychrophilic yeasts: insights into their adaptability to extremely cold environments. Genes, 14:158, Jan 2023. URL: https://doi.org/10.3390/genes14010158, doi:10.3390/genes14010158. This article has 24 citations.

14. (phadtare2012escherichiacolicold‐shock pages 1-2): Sangita Phadtare. Escherichia coli cold‐shock gene profiles in response to over‐expression/deletion of csda, rnase r and pnpase and relevance to low‐temperature rna metabolism. Genes to Cells, 17:850-874, Oct 2012. URL: https://doi.org/10.1111/gtc.12002, doi:10.1111/gtc.12002. This article has 44 citations and is from a peer-reviewed journal.

15. (ramasamy2023comprehensiveinsightson pages 3-4): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 75 citations and is from a peer-reviewed journal.

16. (ramon2023ageneraloverview pages 12-14): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

17. (pathania2021adaptationtocold pages 220-223): Shruti Pathania, Preeti Solanki, Chayanika Putatunda, Ravi Kant Bhatia, and Abhishek Walia. Adaptation to cold environment: the survival strategy of psychrophiles. Survival Strategies in Cold-adapted Microorganisms, pages 87-111, Dec 2021. URL: https://doi.org/10.1007/978-981-16-2625-8\_4, doi:10.1007/978-981-16-2625-8\_4. This article has 27 citations.

18. (purwar2024adaptationsofpsychrophilic pages 4-6): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

19. (garcialopez2021identificationofbiomolecules pages 4-6): Eva Garcia-Lopez, Paula Alcazar, and Cristina Cid. Identification of biomolecules involved in the adaptation to the environment of cold-loving microorganisms and metabolic pathways for their production. Biomolecules, 11:1155, Aug 2021. URL: https://doi.org/10.3390/biom11081155, doi:10.3390/biom11081155. This article has 25 citations.

20. (purwar2024adaptationsofpsychrophilic pages 13-15): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

21. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.