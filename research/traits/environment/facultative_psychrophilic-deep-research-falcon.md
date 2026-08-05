---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:35:05.764914'
end_time: '2026-08-04T00:44:06.951831'
duration_seconds: 541.19
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultative psychrophilic
  trait_identifier: METPO:1000720
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultative_psychrophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A temperature preference characterized by the ability to grow at low
    temperatures (typically below 20 degrees C) while maintaining optimal growth at
    moderate temperatures.
  parent_traits: METPO:1000613
  synonyms: facultative psychrophile
  evidence_summary: "DOI:10.1111/j.1574-6941.2009.00727.x: optimum temperatures >20\
    \ \xB0C and are capable of growth around 0 \xB0C (Supports facultative psychrophiles\
    \ as cold-growing organisms with higher temperature optima.)"
  causal_graph_summary: 'facultative_psychrophilic_cold_tolerance: 13 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultative psychrophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000720
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference characterized by the ability to grow at low temperatures (typically below 20 degrees C) while maintaining optimal growth at moderate temperatures.
- **Parent traits:** METPO:1000613
- **Synonyms:** facultative psychrophile
- **Existing evidence:** DOI:10.1111/j.1574-6941.2009.00727.x: optimum temperatures >20 °C and are capable of growth around 0 °C (Supports facultative psychrophiles as cold-growing organisms with higher temperature optima.)
- **Existing causal graph summary:** facultative_psychrophilic_cold_tolerance: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **facultative psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_psychrophilic.yaml`.

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
- **Trait label:** facultative psychrophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000720
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference characterized by the ability to grow at low temperatures (typically below 20 degrees C) while maintaining optimal growth at moderate temperatures.
- **Parent traits:** METPO:1000613
- **Synonyms:** facultative psychrophile
- **Existing evidence:** DOI:10.1111/j.1574-6941.2009.00727.x: optimum temperatures >20 °C and are capable of growth around 0 °C (Supports facultative psychrophiles as cold-growing organisms with higher temperature optima.)
- **Existing causal graph summary:** facultative_psychrophilic_cold_tolerance: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **facultative psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_psychrophilic.yaml`.

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


# Curation report: facultative psychrophilic

## 1. Scope summary

**Target term:** **facultative psychrophilic**  
**Trait identifier:** **METPO:1000720**  
**Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED  
**Parent:** METPO:1000613  
**Synonym:** facultative psychrophile

### Operational meaning

The trait describes an organism that **can grow at or near 0 °C but has its growth optimum at a moderate temperature**, conventionally about **20–30 °C**, with a maximum above 20 °C. “Psychrotolerant” and “facultative psychrophile” are commonly treated as synonyms. By contrast, a conventional obligate/true psychrophile has an optimum at or below 15 °C and a maximum near or below 20 °C. These criteria agree with the supplied definition and existing evidence. (ramle2016psychrophiliclipasefrom pages 1-4, turchetti2020dnamethylationchanges pages 1-3)

The phenotype should be represented as an **experimentally demonstrated temperature-growth profile**, not merely isolation from a cold habitat, survival after cold exposure, presence of cold-response genes, or enzyme activity at low temperature. Recommended minimum evidence is reproducible biomass increase, colony formation, cell division, or positive specific growth rate near 0–5 °C, together with an optimum above 20 °C under specified medium, atmosphere, salinity, pH, and pressure.

### Boundary cases

1. **Obligate/true psychrophile:** optimum ≤15 °C and upper growth limit around ≤20 °C. Such an organism is cold adapted but does not satisfy the moderate-optimum component of this trait. (ramle2016psychrophiliclipasefrom pages 1-4, turchetti2020dnamethylationchanges pages 1-3)
2. **Psychrotroph:** often an applied food-microbiology label for organisms able to grow at refrigeration temperatures, commonly ≤7 °C. Usage overlaps with psychrotolerant and is not consistently taxonomic or mechanistic. (purwar2024adaptationsofpsychrophilic pages 1-3)
3. **Cold survival or freezing resistance:** viability after chilling/freezing does not establish growth at low temperature.
4. **Cold-shock response:** transient acclimation after a temperature downshift is not equivalent to sustained facultative psychrophilic growth.
5. **Cold-active enzyme producer:** extracellular enzyme activity at 5 °C does not prove that the producing organism grows near 0 °C.
6. **Cold-habitat isolate:** provenance alone is insufficient. Arctic isolates that grew at 27 ± 2 °C were classified as psychrotolerant only after their temperature behavior was considered. (ramle2016psychrophiliclipasefrom pages 1-4)
7. **Continuum warning:** Cavicchioli argues that fixed optimum/maximum thresholds and labels such as “psychrotolerant” can misrepresent ecological cold adaptation. Laboratory growth optima are influenced by ordinary reaction kinetics, while maximum growth temperature says little about fitness in the native cold habitat. The categories are therefore useful operational bins, not natural mechanistic boundaries. (cavicchioli2016ontheconcept pages 1-2, cavicchioli2016ontheconcept pages 2-3, cavicchioli2016ontheconcept pages 3-3)

**Recommended TraitMech phenotype node:** `facultative psychrophilic growth` (**METPO:1000720**), defined by both low-temperature growth and a moderate-temperature optimum. Do not reduce it to the broader node `cold tolerance`.

## 2. Current mechanistic model

Low temperature simultaneously slows enzyme kinetics, stabilizes inhibitory RNA secondary structures, impairs ribosome assembly, promotes protein misfolding, and orders membrane lipids. A plausible graph therefore has several parallel modules converging on sustained low-temperature growth:

1. **Homeoviscous membrane adaptation:** fatty-acid desaturation and altered chain/branching profiles increase the fraction of unsaturated or branched lipids, maintaining membrane fluidity and transport.
2. **RNA remodeling and translation:** cold-shock proteins and DEAD-box RNA helicases prevent or resolve stabilized RNA structures and support ribosome biogenesis, translation, and RNA turnover.
3. **Protein homeostasis:** chaperonins and other chaperones maintain folding and complex assembly.
4. **Osmotic and freezing protection:** trehalose, glycerol, proline, glycine betaine, and related compatible solutes stabilize proteins and membranes, depress freezing, and can reduce oxidative damage.
5. **Cell-envelope remodeling:** peptidoglycan enzymes and exopolysaccharides may preserve envelope function or extracellular hydration.
6. **Stress regulation and resource economy:** stringent-response and two-component systems reallocate transcription, translation, and metabolism.
7. **Oxidative-stress control:** catalases, peroxidases, and compatible solutes counter secondary reactive-oxygen stress.

Recent reviews support this multifactorial view rather than a single universal “psychrophile gene.” In particular, a 2024 synthesis identifies unsaturated and branched fatty acids, cold-shock/antifreeze proteins, compatible solutes, and polyhydroxyalkanoates as recurrent strategies, while emphasizing that much of the evidence remains compositional or transcriptomic rather than perturbational. (purwar2024adaptationsofpsychrophilic pages 10-11)

## 3. Candidate nodes grouped by type

### A. Environmental and experimental factors

- Low incubation temperature, preferably a measured series including approximately 0, 4–5, 15, 20–30 °C
- Temperature downshift / cold shock
- Freezing temperature, explicitly separated from nonfreezing cold
- Incubation time and acclimation phase
- Medium composition and carbon source
- Oxygen availability
- Salinity, pH, water activity, and hydrostatic pressure
- Growth-rate or biomass assay
- Membrane-fluidity assay
- Fatty-acid composition assay
- Knockout, complementation, or heterologous-expression intervention

These variables should be represented because apparent temperature limits depend strongly on assay conditions.

### B. Genes, proteins, and complexes

**High-priority, experimentally supported nodes**

- `cspA`, `cspB`, `cspE`, `cspG`, `cspI`: cold-shock RNA-binding proteins; keep organism-qualified
- `csdA` / `deaD`: DEAD-box RNA helicase
- `srmB`: DEAD-box RNA helicase involved in 50S assembly
- `cshA`, `cshB`, `cshC`: *Bacillus* DEAD-box helicases
- `relA`: stringent-response enzyme/regulator
- `dac2`: DD-peptidase involved in peptidoglycan remodeling
- Cpn60/Cpn10 chaperonin complex; bacterial ortholog names commonly GroEL/GroES

**Provisional nodes requiring trait-specific validation**

- Fatty-acid desaturase
- FabR or other lipid-homeostasis regulators
- RpsU / 30S ribosomal protein S21
- DnaK/Hsp70
- Catalase KatE and peroxidases
- Trehalose biosynthesis and uptake proteins
- Proline and glycine-betaine transport systems
- Exopolysaccharide biosynthesis proteins, including levansucrase
- Antifreeze or ice-binding proteins
- Two-component sensor kinase/response-regulator systems
- cAMP–PKA and ER-associated degradation components in yeasts

Exact UniProt, KEGG, or NCBI Gene identifiers must be assigned per strain; gene symbols alone are unsafe across taxa.

### C. Molecular functions and biological processes

Suggested high-confidence ontology grounding includes:

- **GO:0003724** — RNA helicase activity
- **GO:0006457** — protein folding
- **GO:0006412** — translation
- **GO:0006979** — response to oxidative stress
- `50S ribosomal subunit assembly` — retain label-only unless the curator verifies the applicable GO term/version
- `RNA secondary-structure remodeling`
- `homeoviscous adaptation`
- `membrane-fluidity maintenance`
- `compatible-solute accumulation`
- `peptidoglycan remodeling`
- `stringent response`
- `cold acclimation`

### D. Chemicals and cellular structures

High-confidence chemical candidates are:

- Glycerol — **CHEBI:17754**
- L-proline — **CHEBI:17203**
- Trehalose — **CHEBI:27082**
- Glycine betaine — **CHEBI:17750**
- Unsaturated fatty acids — use a verified class identifier during implementation rather than assigning individual fatty-acid identifiers generically
- Saturated fatty acids
- Polyunsaturated fatty acids, including EPA and DHA
- Reactive oxygen species
- Peptidoglycan
- Levan and other exopolysaccharides

Cellular locations include the cytoplasmic membrane, cytosol, ribosome, cell wall/periplasm where applicable, and extracellular matrix. “Organelle” terminology should not be imposed uniformly across bacteria, archaea, and fungi.

### E. Pathways and modules

- Unsaturated-fatty-acid biosynthesis/desaturation
- Membrane-lipid remodeling
- RNA helicase–dependent RNA metabolism
- Ribosome biogenesis and translation
- Chaperone-mediated protein folding
- Trehalose, glycerol, and proline metabolism
- Compatible-solute transport
- Stringent response
- Peptidoglycan maturation/remodeling
- Antioxidant defense
- Exopolysaccharide biosynthesis

## 4. Candidate causal edges

The following table distinguishes intervention-backed edges from review-level and omics-only hypotheses. “Promotes” means that increasing or preserving the subject supports the object; it should not be interpreted as sufficient to produce the complete trait in every taxon.

| Proposed subject–predicate–object triple | Evidence organism/assay | Supporting quote/snippet | DOI | Evidence strength and curation note |
|---|---|---|---|---|
| low temperature → causes → membrane rigidification | General cold-adaptation review synthesis | “modulating membrane fluidity is the desaturation of fatty acids” and low temperature is discussed as altering growth kinetics and requiring membrane adaptation (purwar2024adaptationsofpsychrophilic pages 10-11, ramasamy2023comprehensiveinsightson pages 4-6) | 10.1007/s42770-023-01057-4 | Review-supported background edge; useful as upstream environmental driver, but not direct facultative-psychrophile-specific experiment. |
| fatty-acid desaturation / increased unsaturated fatty acids → increases → membrane fluidity | General cold-adaptation review; comparative genomics of cold-adapted bacteria | “membrane fluidity by changing the unsaturated fatty acid profile” (xiong2023wholegenomeanalysis pages 1-2); review notes adaptation via “unsaturated fatty acid ratio in membrane phospholipids” (ramasamy2023comprehensiveinsightson pages 4-6) | 10.1038/s41598-023-41323-x | Moderate support for mechanism; mostly review/genomic inference here, not direct mutant evidence in facultative psychrophiles. |
| increased membrane fluidity → promotes → low-temperature growth | General cold-adaptation review/comparative genomics | “maintaining membrane fluidity at low temperatures” and “membrane fluidity by changing the unsaturated fatty acid profile” (purwar2024adaptationsofpsychrophilic pages 10-11, xiong2023wholegenomeanalysis pages 1-2) | 10.37256/amtt.5220244537 | General mechanistic edge appropriate as background process; curate as broad cold-adaptation relation, not trait-exclusive. |
| E. coli CspA/CspB/CspG/CspE → promotes → growth at 15 °C | Quadruple csp deletion plus complementation in E. coli | “The quadruple-deletion strain (ΔcspA ΔcspB ΔcspG ΔcspE) exhibits cold sensitivity at 15°C, with complementation possible by overproduction of CspA, CspB, CspG, or CspI homologues” (phadtare2004genomewidetranscriptionalanalysis pages 1-2) | 10.1128/jb.186.20.7007-7014.2004 | Strong direct causal evidence from loss-of-function/complementation; mesophilic model organism, so use as transferable mechanism with taxon caveat. |
| E. coli CsdA (DEAD-box RNA helicase) → promotes → cold growth | Deletion/complementation evidence in E. coli | “CsdA deletion severely impairs growth at low temperature” and “RNase R or CspA overproduction complements csdA deletion cold sensitivity” (phadtare2010rnaremodelingand pages 5-6) | 10.4161/rna.7.6.13482 | Strong direct causal edge. Mechanistically supports RNA remodeling/translation at low temperature. |
| E. coli SrmB → promotes → 50S ribosome assembly and cold growth | Deletion phenotype in E. coli | “SrmB deletion causes slow-growth at low temperature with deficits in 50S ribosomal subunits” (phadtare2010rnaremodelingand pages 5-6) | 10.4161/rna.7.6.13482 | Strong direct evidence; good candidate for ribosome-biogenesis module. |
| Bacillus cereus CshA/CshB/CshC → collectively enables → growth at 12 °C | Single and triple DEAD-box helicase deletions in B. cereus | “Most strikingly, triple deletion ΔcshA, B and C prevented growth at 12°C” (owttrim2013rnahelicases pages 3-4) | 10.4161/rna.22638 | Strong direct causal evidence, but species-specific and collective rather than single-gene universal. |
| Psychrobacter arcticus csdA → promotes → growth at 4, 0, and −2.5 °C | Knockout mutants in P. arcticus 273-4 | “The csdA gene … showed significant growth impairment in knockout mutants at both 4°C and 0°C. At −2.5°C … csdA grew significantly slower than wild-type” (bergholz2009psychrobacterarcticus2734 pages 9-10) | 10.1128/JB.01377-08 | Strong direct causal evidence in a true cold-adapted organism; highly relevant for TraitMech. |
| Psychrobacter arcticus relA → promotes → growth at −2.5 °C | Knockout mutants in P. arcticus 273-4 | “At −2.5°C, knockout mutants of relA … grew significantly slower than wild-type” (bergholz2009psychrobacterarcticus2734 pages 9-10) | 10.1128/JB.01377-08 | Strong direct evidence for stringent-response involvement in subzero growth; likely not trait-exclusive. |
| Psychrobacter arcticus dac2 (DD-peptidase) → promotes → growth at −2.5 °C | Knockout mutants in P. arcticus 273-4 | “At −2.5°C, knockout mutants of … dac2 … grew significantly slower than wild-type” (bergholz2009psychrobacterarcticus2734 pages 9-10) | 10.1128/JB.01377-08 | Strong direct evidence for cell-wall remodeling contribution to subzero growth. |
| Oleispira antarctica Cpn60/Cpn10 expression → enables → E. coli growth at 4 °C | Heterologous expression/complementation in E. coli | “E. coli expressing psychrophilic chaperonins Cpn60/Cpn10 from Oleispira antarctica grew faster at 18-8°C and could grow at 4°C, whereas wild-type E. coli cannot grow below 7.5°C” (kuhn2012towardunderstandinglife pages 2-3) | 10.1089/ast.2012.0858 | Strong causal evidence for chaperone-mediated cold growth, but heterologous and not native facultative-psychrophile context. |
| compatible solutes (e.g., trehalose, glycine betaine, glycerol) → protects → proteins/membranes during freezing or cold stress | Review synthesis across psychrophiles/psychrotolerants | “Compatible solutes … depress freezing points, stabilize proteins/membranes, and scavenge free radicals” (purwar2024adaptationsofpsychrophilic pages 10-11) | 10.37256/amtt.5220244537 | Associative/review edge; good node family, but not direct trait-specific causal proof. |
| Metschnikowia pulcherrima glycerol/proline synthesis or transport → associated_with → −5 °C resistance | Comparative transcriptomics at 20, 5, and −5 °C | “At freezing temperature (−5°C), increased glycerol and proline synthesis/transport contributed to freezing resistance” (yuan2024investigationofcoldresistance pages 1-2) | 10.3389/fmicb.2024.1476087 | Uncertain for curation as causal edge: transcriptomic association, not genetic perturbation. |
| Pseudomonas sivasensis trehalose utilization / two-component systems / rpsU → associated_with → cold adaptation and low-temperature growth | Whole-genome analysis with growth assay | “Cold-adapted bacterium W-6 can utilize glycogen and trehalose … In addition, the cold-adapted mechanisms … included membrane fluidity … the two-component regulatory systems … the role played by rpsU genes” (xiong2023wholegenomeanalysis pages 1-2) | 10.1038/s41598-023-41323-x | Uncertain/non-causal: genomic association only. Keep as candidate nodes, not asserted causal edges, unless corroborated experimentally. |


*Table: This table compiles candidate causal edges for facultative psychrophily/psychrotolerance, separating strong direct genetic evidence from review-based or omics-only associations. It is useful for deciding which relations are ready for TraitMech curation and which should remain provisional.*

### Recommended graph core

The most defensible initial graph is:

`low temperature` → `increased RNA secondary-structure stability / impaired ribosome assembly` → `reduced translation` → `reduced low-temperature growth`, with parallel rescue paths through cold-shock proteins and DEAD-box helicases. Direct deletion evidence supports Csp paralogs, CsdA/DeaD, SrmB, and CshA/B/C, while *Psychrobacter arcticus* provides especially relevant evidence at 4, 0, and −2.5 °C. (phadtare2010rnaremodelingand pages 5-6, owttrim2013rnahelicases pages 3-4, bergholz2009psychrobacterarcticus2734 pages 9-10, owttrim2013rnahelicases pages 5-6, phadtare2004genomewidetranscriptionalanalysis pages 1-2)

A second strong module is:

`Cpn60/Cpn10 chaperonin activity` → `protein folding/homeostasis at low temperature` → `low-temperature growth`. Heterologous expression of *Oleispira antarctica* Cpn60/Cpn10 allowed *E. coli* to grow at 4 °C, below the wild-type minimum of 7.5 °C. This is strong intervention evidence, although it is heterologous rather than a native facultative-psychrophile knockout. (kuhn2012towardunderstandinglife pages 2-3)

The membrane module is biologically compelling but less directly established in the retrieved facultative-psychrophile literature:

`fatty-acid desaturation` → `increased unsaturated-fatty-acid fraction` → `maintained membrane fluidity` → `transport and membrane function at low temperature` → `low-temperature growth`.

This should be curated with a lower confidence than the helicase/chaperonin edges unless a strain-specific desaturase knockout or complementation paper is attached. Recent work on *Pseudomonas sivasensis* linked its cold phenotype to an altered unsaturated-fatty-acid profile, but the study was primarily genomic/physiological rather than a causal gene perturbation. (purwar2024adaptationsofpsychrophilic pages 10-11, xiong2023wholegenomeanalysis pages 1-2)

## 5. Recent developments, 2023–2024

### Whole-genome analysis of *Pseudomonas sivasensis* W-6 — 2023

W-6 had a 6,109,123-bp genome, 59.5% GC content, 5,360 predicted protein-coding sequences, 70 tRNAs, 24 genomic islands, and two CRISPR regions. It grew from 4 to 30 °C with an optimum at 15 °C. Thus, despite discussion of “psychrotolerant” mechanisms, its measured optimum places it closer to the conventional psychrophile boundary than to the target trait. Trehalose/glycogen use, unsaturated-fatty-acid profiles, two-component systems, antisense transcription, and `rpsU` were proposed as mechanisms, but these are genomic or physiological associations, not validated causal edges. (xiong2023wholegenomeanalysis pages 1-2)

### *Paenibacillus antarcticus* IPAC21 — 2023

This explicitly psychrotolerant Antarctic strain has a roughly 5.5-Mb genome with 40.5% GC content and genes encoding cold-shock proteins, chaperones, exopolysaccharide functions, levansucrase, phosphotransferase-system transporters, and the 2,3-butanediol pathway. Their genomic presence is useful for node discovery but does not show that they cause cold growth. IPAC21 produced a bioemulsifier with an emulsification index above 50% against hexadecane, kerosene, and diesel when grown at 28 °C; the product remained stable under low temperature, varied salinity, and varied pH, supporting petroleum-processing applications. (lemos2023molecularcharacterizationof pages 1-2)

### Antarctic adaptation and biotechnology synthesis — 2023

A broad 2023 review emphasized chaperones, cold-shock proteins, osmolytes, membrane-lipid adaptation, and cold-active enzymes. It reported that recombinant *Shewanella* DnaK facilitated *E. coli* growth at 15 °C and highlighted β-galactosidase and DyP peroxidase activities at 5 °C. These observations support biotechnology and protein-homeostasis nodes but should remain organism- and assay-qualified. (ramasamy2023comprehensiveinsightson pages 4-6)

### *Metschnikowia pulcherrima* MS612 transcriptomics — 2024

RNA-seq identified 6,018 genes and 374 differentially expressed genes at greater than twofold change with *p* < 0.05. Growth at 5 °C was associated with enhanced energy metabolism, sterol synthesis, ion homeostasis, and transport. At −5 °C, glycerol/proline synthesis or transport, cAMP–PKA signaling, and ER-associated degradation were implicated. Because these findings are differential-expression associations rather than knockouts or complementation, they are candidate nodes and `associated_with` edges, not established causes of facultative psychrophily. (yuan2024investigationofcoldresistance pages 1-2)

### State of genomic resources — 2024

A 2024 review reported 83 complete or permanent-draft psychrophile genomes and 102 targeted or incomplete genomes in the cited GOLD snapshot. It also noted recurring cold-active α-amylases, proteases, lipases, DNA polymerases, and cellulases. These figures concern broadly defined psychrophiles and should not be interpreted as counts of organisms proven to possess **METPO:1000720**. (purwar2024adaptationsofpsychrophilic pages 3-4)

## 6. Applications and real-world implementations

1. **Refrigerated-food microbiology:** facultative psychrophiles can grow during refrigeration while retaining moderate-temperature growth, making the trait relevant to spoilage and foodborne-pathogen risk. Presence in food at low temperature is nevertheless an ecological observation; growth curves remain necessary for trait assignment. (purwar2024adaptationsofpsychrophilic pages 1-3, purwar2024adaptationsofpsychrophilic pages 3-4)
2. **Low-temperature biocatalysis:** cold-active lipases, proteases, cellulases, β-galactosidases, peroxidases, and polymerases can reduce heating requirements and permit processing of heat-sensitive substrates. Enzyme cold activity must not be conflated with the organism-level trait. (ramasamy2023comprehensiveinsightson pages 4-6, purwar2024adaptationsofpsychrophilic pages 3-4)
3. **Petroleum and bioremediation processes:** the IPAC21 bioemulsifier’s greater-than-50% emulsification index and stability under low temperature, salt, and pH variation make it a concrete candidate for petroleum handling or remediation. (lemos2023molecularcharacterizationof pages 1-2)
4. **Cold-climate agriculture:** psychrotolerant bacteria have been developed as plant-growth-promoting inoculants because they remain metabolically active under chilling conditions. This is a downstream application, not a core mechanistic edge for microbial cold growth.
5. **Synthetic biology:** cold-active chaperonins can extend a host’s lower growth range; *Oleispira* Cpn60/Cpn10 enabling *E. coli* growth at 4 °C is a direct proof of concept. (kuhn2012towardunderstandinglife pages 2-3)
6. **Cryoprotection and biomaterials:** compatible solutes, polyunsaturated lipids, exopolysaccharides, antifreeze proteins, and ice-binding proteins are candidates for frozen-food, biomedical, and industrial formulations, although production and trait mechanisms must be curated separately. (purwar2024adaptationsofpsychrophilic pages 10-11)

## 7. Expert analysis and curation priorities

### Edges ready for curation

The highest-confidence edges are those backed by deletion or complementation:

- CspA-family proteins → promote low-temperature growth
- CsdA/DeaD and SrmB → promote RNA/ribosome function and low-temperature growth
- CshA/CshB/CshC collectively → enable growth at 12 °C in *B. cereus*
- *P. arcticus* CsdA, RelA, and Dac2 → promote growth at 0 to −2.5 °C
- Cpn60/Cpn10 → promote protein homeostasis and extend low-temperature growth

These mechanisms are not unique to facultative psychrophiles. They should connect to the trait through intermediate processes rather than imply that one gene is sufficient for **METPO:1000720**. (phadtare2010rnaremodelingand pages 5-6, owttrim2013rnahelicases pages 3-4, bergholz2009psychrobacterarcticus2734 pages 9-10, kuhn2012towardunderstandinglife pages 2-3, phadtare2004genomewidetranscriptionalanalysis pages 1-2)

### Edges suitable only as provisional hypotheses

- Fatty-acid desaturase → facultative psychrophilic growth
- Trehalose, glycerol, proline, or glycine betaine → facultative psychrophilic growth
- Two-component systems or `rpsU` → facultative psychrophilic growth
- Exopolysaccharide or antifreeze-protein production → facultative psychrophilic growth
- cAMP–PKA or ERAD → facultative psychrophilic growth

For these, the retrieved evidence is predominantly review synthesis, genome annotation, metabolite association, or differential expression. Curate candidate nodes now, but withhold direct `causes`/`enables` edges until perturbation and rescue data are available. (purwar2024adaptationsofpsychrophilic pages 10-11, lemos2023molecularcharacterizationof pages 1-2, xiong2023wholegenomeanalysis pages 1-2, yuan2024investigationofcoldresistance pages 1-2)

## 8. Warnings: claims not yet ready for TraitMech

- **Do not curate habitat origin as phenotype evidence.** Antarctic, Arctic, alpine, deep-sea, or refrigerated-food origin is not sufficient.
- **Do not treat survival as growth.** A viable count after freezing does not demonstrate replication near 0 °C.
- **Do not infer the trait from a genome.** Cold-shock proteins, helicases, desaturases, chaperones, and compatible-solute pathways also occur in mesophiles.
- **Do not assign W-6 uncritically to the target.** Its optimum was 15 °C, making it conventionally psychrophilic rather than clearly facultatively psychrophilic. (xiong2023wholegenomeanalysis pages 1-2)
- **Do not turn transcriptomic associations into causal edges.** The 374-gene *M. pulcherrima* response provides candidates, not proof that individual genes or metabolites are necessary or sufficient. (yuan2024investigationofcoldresistance pages 1-2)
- **Do not generalize organism-specific paralogs.** Csp and DEAD-box helicase redundancy differs among taxa.
- **Do not omit assay context.** Medium, oxygen, salinity, pressure, inoculum history, acclimation, and duration can shift apparent minimum and optimum temperatures.
- **Do not overstate membrane evidence.** Homeoviscous adaptation is well established generally, but a facultative-psychrophile-specific perturbation should support each gene-level edge.
- **Do not invent CURIEs.** Use label-only nodes until the exact gene product, strain, chemical stereochemistry, pathway, or ontology release has been verified.
- **Do not encode the temperature classes as absolute biological boundaries.** Expert critique supports a continuum model and cautions that laboratory optimum and maximum temperatures can misrepresent ecological adaptation. (cavicchioli2016ontheconcept pages 1-2, cavicchioli2016ontheconcept pages 2-3)

## 9. DOI-first bibliography

1. **10.1038/ismej.2015.160** — Cavicchioli R. “On the concept of a psychrophile.” *ISME Journal*. Published September 2015 online / 2016 issue. https://doi.org/10.1038/ismej.2015.160 (cavicchioli2016ontheconcept pages 1-2, cavicchioli2016ontheconcept pages 2-3)
2. **10.3390/microorganisms8020296** — Turchetti B. et al. “DNA Methylation Changes Induced by Cold in Psychrophilic and Psychrotolerant *Naganishia* Yeast Species.” *Microorganisms*. February 2020. https://doi.org/10.3390/microorganisms8020296 (turchetti2020dnamethylationchanges pages 1-3)
3. **10.1007/s42770-023-01057-4** — Ramón A. et al. “A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.” *Brazilian Journal of Microbiology*. July 2023. https://doi.org/10.1007/s42770-023-01057-4
4. **10.1038/s41598-023-41323-x** — Xiong L. et al. “Whole genome analysis and cold adaptation strategies of *Pseudomonas sivasensis* W-6.” *Scientific Reports*. August 2023. https://doi.org/10.1038/s41598-023-41323-x (xiong2023wholegenomeanalysis pages 1-2)
5. **10.3389/fmicb.2023.1142582** — de Lemos E.A. et al. “Molecular characterization of *Paenibacillus antarcticus* IPAC21, a bioemulsifier producer isolated from Antarctic soil.” *Frontiers in Microbiology*. March 2023. https://doi.org/10.3389/fmicb.2023.1142582 (lemos2023molecularcharacterizationof pages 1-2)
6. **10.3389/fmicb.2023.1197797** — Ramasamy K.P. et al. “Comprehensive insights on environmental adaptation strategies in Antarctic bacteria and biotechnological applications of cold adapted molecules.” *Frontiers in Microbiology*. June 2023. https://doi.org/10.3389/fmicb.2023.1197797 (ramasamy2023comprehensiveinsightson pages 4-6)
7. **10.3389/fmicb.2024.1476087** — Yuan Z. et al. “Investigation of cold-resistance mechanisms in cryophylactic yeast *Metschnikowia pulcherrima* based on comparative transcriptome analysis.” *Frontiers in Microbiology*. September 2024. https://doi.org/10.3389/fmicb.2024.1476087 (yuan2024investigationofcoldresistance pages 1-2)
8. **10.37256/amtt.5220244537** — Purwar S., Srivastava S. “Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.” *Applied Microbiology: Theory & Technology*. October 2024. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 10-11, purwar2024adaptationsofpsychrophilic pages 3-4)
9. **10.1128/JB.01377-08** — Bergholz P.W., Bakermans C., Tiedje J.M. “*Psychrobacter arcticus* 273-4 Uses Resource Efficiency and Molecular Motion Adaptations for Subzero Temperature Growth.” *Journal of Bacteriology*. April 2009. https://doi.org/10.1128/JB.01377-08 (bergholz2009psychrobacterarcticus2734 pages 9-10)
10. **10.1128/JB.186.20.7007-7014.2004** — Phadtare S., Inouye M. “Genome-Wide Transcriptional Analysis of the Cold Shock Response in Wild-Type and Cold-Sensitive, Quadruple-csp-Deletion Strains of *Escherichia coli*.” *Journal of Bacteriology*. October 2004. https://doi.org/10.1128/JB.186.20.7007-7014.2004 (phadtare2004genomewidetranscriptionalanalysis pages 1-2)
11. **10.4161/rna.7.6.13482** — Phadtare S., Severinov K. “RNA remodeling and gene regulation by cold shock proteins.” *RNA Biology*. November 2010. https://doi.org/10.4161/rna.7.6.13482 (phadtare2010rnaremodelingand pages 5-6)
12. **10.4161/rna.22638** — Owttrim G.W. “RNA helicases.” *RNA Biology*. January 2013. https://doi.org/10.4161/rna.22638 (owttrim2013rnahelicases pages 3-4, owttrim2013rnahelicases pages 5-6)
13. **10.1089/ast.2012.0858** — Kuhn E. “Toward understanding life under subzero conditions: the significance of exploring psychrophilic ‘cold-shock’ proteins.” *Astrobiology*. November 2012. https://doi.org/10.1089/ast.2012.0858 (kuhn2012towardunderstandinglife pages 2-3)
14. **10.21315/tlsr2016.27.3.21** — Ramle Z., Abdul Rahim R. “Psychrophilic Lipase from Arctic Bacterium.” *Tropical Life Sciences Research*. November 2016. https://doi.org/10.21315/tlsr2016.27.3.21 (ramle2016psychrophiliclipasefrom pages 1-4)

## Curation conclusion

The existing 13-node/11-edge graph should be expanded primarily around **RNA remodeling/ribosome biogenesis, chaperonin-mediated protein homeostasis, membrane-fluidity maintenance, stringent response, and cell-wall remodeling**. Direct genetic evidence is strongest for the RNA-helicase, cold-shock-protein, chaperonin, `relA`, and `dac2` branches. Membrane lipids, compatible solutes, two-component systems, antioxidants, and exopolysaccharides are important candidate modules, but most retrieved 2023–2024 evidence supports them only at the review, genomic, or transcriptomic level. The graph should therefore preserve explicit evidence-strength and taxon/assay qualifiers rather than presenting all cold-response mechanisms as universal causes of **METPO:1000720**.

References

1. (ramle2016psychrophiliclipasefrom pages 1-4): Zakiah Ramle and Rashidah Abdul Rahim. Psychrophilic lipase from arctic bacterium. Tropical life sciences research, 27 supp1:151-157, Nov 2016. URL: https://doi.org/10.21315/tlsr2016.27.3.21, doi:10.21315/tlsr2016.27.3.21. This article has 11 citations.

2. (turchetti2020dnamethylationchanges pages 1-3): Benedetta Turchetti, Gianpiero Marconi, Ciro Sannino, Pietro Buzzini, and Emidio Albertini. Dna methylation changes induced by cold in psychrophilic and psychrotolerant naganishia yeast species. Microorganisms, 8:296, Feb 2020. URL: https://doi.org/10.3390/microorganisms8020296, doi:10.3390/microorganisms8020296. This article has 19 citations.

3. (purwar2024adaptationsofpsychrophilic pages 1-3): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

4. (cavicchioli2016ontheconcept pages 1-2): Ricardo Cavicchioli. On the concept of a psychrophile. The ISME Journal, 10:793-795, Sep 2016. URL: https://doi.org/10.1038/ismej.2015.160, doi:10.1038/ismej.2015.160. This article has 131 citations.

5. (cavicchioli2016ontheconcept pages 2-3): Ricardo Cavicchioli. On the concept of a psychrophile. The ISME Journal, 10:793-795, Sep 2016. URL: https://doi.org/10.1038/ismej.2015.160, doi:10.1038/ismej.2015.160. This article has 131 citations.

6. (cavicchioli2016ontheconcept pages 3-3): Ricardo Cavicchioli. On the concept of a psychrophile. The ISME Journal, 10:793-795, Sep 2016. URL: https://doi.org/10.1038/ismej.2015.160, doi:10.1038/ismej.2015.160. This article has 131 citations.

7. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

8. (ramasamy2023comprehensiveinsightson pages 4-6): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 75 citations and is from a peer-reviewed journal.

9. (xiong2023wholegenomeanalysis pages 1-2): Lingling Xiong, Yanmei Li, Hang Yu, Yunlin Wei, Haiyan Li, and Xiuling Ji. Whole genome analysis and cold adaptation strategies of pseudomonas sivasensis w-6 isolated from the napahai plateau wetland. Scientific Reports, Aug 2023. URL: https://doi.org/10.1038/s41598-023-41323-x, doi:10.1038/s41598-023-41323-x. This article has 13 citations and is from a peer-reviewed journal.

10. (phadtare2004genomewidetranscriptionalanalysis pages 1-2): Sangita Phadtare and Masayori Inouye. Genome-wide transcriptional analysis of the cold shock response in wild-type and cold-sensitive, quadruple-csp-deletion strains of escherichia coli. Journal of Bacteriology, 186:7007-7014, Oct 2004. URL: https://doi.org/10.1128/jb.186.20.7007-7014.2004, doi:10.1128/jb.186.20.7007-7014.2004. This article has 265 citations and is from a peer-reviewed journal.

11. (phadtare2010rnaremodelingand pages 5-6): Sangita Phadtare and Konstantin Severinov. Rna remodeling and gene regulation by cold shock proteins. RNA Biology, 7:788-795, Nov 2010. URL: https://doi.org/10.4161/rna.7.6.13482, doi:10.4161/rna.7.6.13482. This article has 225 citations and is from a peer-reviewed journal.

12. (owttrim2013rnahelicases pages 3-4): George W. Owttrim. Rna helicases. RNA Biology, 10:96-110, Jan 2013. URL: https://doi.org/10.4161/rna.22638, doi:10.4161/rna.22638. This article has 133 citations and is from a peer-reviewed journal.

13. (bergholz2009psychrobacterarcticus2734 pages 9-10): Peter W. Bergholz, Corien Bakermans, and James M. Tiedje. <i>psychrobacter arcticus</i> 273-4 uses resource efficiency and molecular motion adaptations for subzero temperature growth. Apr 2009. URL: https://doi.org/10.1128/jb.01377-08, doi:10.1128/jb.01377-08. This article has 126 citations and is from a peer-reviewed journal.

14. (kuhn2012towardunderstandinglife pages 2-3): Emanuele Kuhn. Toward understanding life under subzero conditions: the significance of exploring psychrophilic "cold-shock" proteins. Astrobiology, 12 11:1078-86, Nov 2012. URL: https://doi.org/10.1089/ast.2012.0858, doi:10.1089/ast.2012.0858. This article has 43 citations and is from a peer-reviewed journal.

15. (yuan2024investigationofcoldresistance pages 1-2): Zaizhu Yuan, Zhengkai Ge, Qingquan Fu, Fangfang Wang, Qingling Wang, Xuewei Shi, and Bin Wang. Investigation of cold-resistance mechanisms in cryophylactic yeast metschnikowia pulcherrima based on comparative transcriptome analysis. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1476087, doi:10.3389/fmicb.2024.1476087. This article has 5 citations and is from a peer-reviewed journal.

16. (owttrim2013rnahelicases pages 5-6): George W. Owttrim. Rna helicases. RNA Biology, 10:96-110, Jan 2013. URL: https://doi.org/10.4161/rna.22638, doi:10.4161/rna.22638. This article has 133 citations and is from a peer-reviewed journal.

17. (lemos2023molecularcharacterizationof pages 1-2): Ericka Arregue de Lemos, Luciano Procópio, Fabio Faria da Mota, Diogo Jurelevicius, Alexandre Soares Rosado, and Lucy Seldin. Molecular characterization of paenibacillus antarcticus ipac21, a bioemulsifier producer isolated from antarctic soil. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1142582, doi:10.3389/fmicb.2023.1142582. This article has 11 citations and is from a peer-reviewed journal.

18. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.