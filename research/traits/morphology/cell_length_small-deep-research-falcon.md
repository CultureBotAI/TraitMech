---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:38:29.705705'
end_time: '2026-08-04T07:45:39.248528'
duration_seconds: 429.54
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell length small
  trait_identifier: METPO:1000884
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_length_small
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-length phenotype in which the longer cell dimension lies approximately
    between 1.3 and 2 micrometers.
  parent_traits: METPO:1000881
  synonyms: L_1.3_2
  evidence_summary: 'DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount
    between divisions (Adder-model paper supports a defined inter-divisional length
    increment that produces a narrow length distribution at standard growth conditions.)'
  causal_graph_summary: 'cell_length_small_size_setpoint: 15 nodes, 9 edges'
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
- **Trait label:** cell length small
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000884
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 1.3 and 2 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_1.3_2
- **Existing evidence:** DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount between divisions (Adder-model paper supports a defined inter-divisional length increment that produces a narrow length distribution at standard growth conditions.)
- **Existing causal graph summary:** cell_length_small_size_setpoint: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **cell length small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_small.yaml`.

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
- **Trait label:** cell length small
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000884
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 1.3 and 2 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_1.3_2
- **Existing evidence:** DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount between divisions (Adder-model paper supports a defined inter-divisional length increment that produces a narrow length distribution at standard growth conditions.)
- **Existing causal graph summary:** cell_length_small_size_setpoint: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **cell length small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_small.yaml`.

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


# Curation report: microbial **cell length small**

## Executive assessment

The target is the reviewed morphology class **“METPO:1000884”**, defined as a cell-length phenotype in which the longer cellular dimension is approximately **1.3–2 µm**; its stated parent is **METPO:1000881** and synonym is **L_1.3_2**. This is an **absolute, assay-observed length bin**, not simply “smaller than wild type,” low volume, slow growth, or reduced width.

The strongest mechanistic graph is a division-timing module:

**environment/nutrient state → metabolic or divisome regulator → FtsZ/FtsN-dependent divisome activation → time or elongation before septation → final cell length.**

However, most available studies establish **relative shortening or size reduction without reporting that cells actually fall between 1.3 and 2 µm**. Accordingly, the mechanisms below are good candidates for a general *cell-length set-point* graph, but only a subset should be connected directly to **“METPO:1000884”** without additional strain- and assay-level measurements.

## 1. Trait scope and boundaries

### In scope

* The longer axis of an individual microbial cell measured by calibrated microscopy or equivalent image analysis.
* A population phenotype only when the statistic is specified—preferably median or mean length, with distribution and sample size—and lies approximately within **1.3–2 µm**.
* Vegetative cells under explicitly recorded taxon, strain, medium, temperature, pH, growth phase, and imaging conditions.
* Mechanisms that alter division timing relative to longitudinal growth, especially FtsZ-ring formation and septal activation.

### Boundary cases

1. **Relative “small-cell” phenotypes are insufficient.** Acidic pH reduced *E. coli* projected area to approximately 75% of the neutral-pH value, and alkaline pH increased it to approximately 120%, but the retrieved evidence did not give an absolute 1.3–2 µm length. The pH effect primarily involved length, making it mechanistically relevant but not sufficient for direct membership in this METPO class. (mueller2020phdependentactivationof pages 2-3)
2. **Volume and area are not length.** A pH-dependent reduction in division volume or projected area should not automatically be represented as reduced length unless length was separately quantified.
3. **Width is independently regulated.** Central-carbon perturbations can alter width through cAMP–CRP/BolA pathways, whereas FtsZ-associated effects more directly concern length. A “small size” phenotype combining both dimensions should not be collapsed into this length-only class. (westfall2018comprehensiveanalysisof pages 17-18)
4. **Adder behavior is not an absolute length state.** An adder adds an approximately fixed size between birth and division; it produces homeostasis around a condition-dependent set point but does not itself specify a 1.3–2 µm endpoint. Under poor medium, *E. coli* can instead exhibit more sizer-like behavior. Thus, the supplied 2014 adder reference supports homeostasis, not the absolute METPO interval.
5. **Minicells, spores, cocci, pleomorphic cells, and filaments require separate treatment.** A minicell may be short because of polar misdivision rather than a normal small-size set point. For cocci, “longer dimension” is weakly distinguishable from diameter. Filamentation is the opposite phenotype.

## 2. Current mechanistic understanding

### Nutrient sensing through UDP-glucose

Carbon-rich growth raises UDP-glucose signaling. In *E. coli*, UDP-glucose-bound OpgH exposes an FtsZ-interacting region, sequesters or antagonizes FtsZ, delays cytokinetic-ring maturation, and increases size. Biochemically, the OpgH N-terminal domain reduced FtsZ GTPase activity by **25–84%** across tested protein ratios and increased apparent FtsZ critical concentration from **0.69 to 4.08 µM** at 10 µM OpgH fragment. Low UDP-glucose relieves this inhibition, providing a plausible route to earlier division and shorter cells. (buske2013thecterminus pages 225-230)

The analogous *Bacillus subtilis* regulator is UgtP. Defects in OpgH, UgtP, or associated UDP-glucose pathway proteins reduce cell size by approximately **15–30%** with little growth-rate effect, supporting a signaling mechanism rather than size being merely a passive consequence of slow growth. This is authoritative review-level synthesis; direct linkage to the 1.3–2 µm bin remains unproven. (westfall2017bacterialcellsize pages 9-11)

### FtsZ accumulation and ring assembly

FtsZ polymerizes into the cytokinetic Z ring. Its effective abundance and assembly state regulate when division becomes possible. Recent work indicates that FtsZ molecule number is rate-limiting for *E. coli* division, whereas physiological FtsN and FtsA levels are not generally rate-limiting; very high FtsN expression can accelerate division, while high FtsA can inhibit it. This updates overly simple models in which FtsN arrival alone is the unique checkpoint.

FtsZ inhibition generally delays division and produces longer or filamentous cells. Therefore, FtsZ inhibitors are **counterevidence**, not interventions expected to generate METPO:1000884. Conversely, enhanced effective FtsZ assembly can shorten cells, but excessive FtsZ or altered FtsZ:FtsA stoichiometry may cause abnormal septation; the relation is not safely monotonic.

### Extracellular pH and FtsN

In *E. coli*, acidic extracellular pH increases septal FtsN accumulation, promotes cytokinesis at reduced length, and decreases division size. At pH 4.5, cell area was approximately **75%** of that at pH 7.0; pH 8.5 increased it to approximately **120%**. Alkaline pH increased division size by more than **40%** in the reported comparison. FtsN overexpression was itself sufficient to reduce division volume. These observations support the direct path **acidic pH → septal FtsN recruitment → earlier divisome activation → reduced length**. (mueller2020phdependentactivationof pages 11-13, mueller2020phdependentactivationof pages 2-3)

The effect is not unique to *E. coli*: *Staphylococcus aureus* volume was approximately **48% lower** at pH 5.5 than at pH 8.0. This supports evolutionary breadth of pH-sensitive size regulation but not conservation of the exact FtsN mechanism or the METPO length interval. (mueller2020phdependentactivationof pages 2-3)

### Min-system spatial regulation

MinCDE prevents inappropriate polar FtsZ-ring formation and contributes to when a stable ring can bind the membrane. A 2023 single-cell study found that *E. coli* **minE overexpression delayed FtsZ-ring initiation and increased cell size** as cells approached a new steady state. Smaller-born cells grew more before ring assembly, and, after stable ring formation, cells added an approximately fixed amount before division. Thus, Min-system balance belongs in a general length-control graph, but **minE overexpression is an opposite-direction boundary case**, not evidence for small length. (vashistha2023bacterialcellsizechanges pages 1-2, vashistha2023bacterialcellsizechanges pages 8-9)

### Starvation and central metabolism

Amino-acid starvation and ppGpp accumulation reduce both length and width. Because both dimensions and global biosynthesis change, this is a moderate-confidence upstream route to smaller morphology, not yet a length-specific direct mechanism. (westfall2017bacterialcellsize pages 9-11)

Central-carbon screens found that perturbations of acetate/acetyl-CoA-associated genes, including *aceE*, *ackA*, and *pta*, can strongly reduce growth and cell size; possible mediators include fatty-acid synthesis and ppGpp. These are valuable candidate nodes, but the mechanistic route to absolute small length remains unresolved. (westfall2018comprehensiveanalysisof pages 17-18)

## 3. Candidate nodes grouped by type

### Trait and taxon nodes

| Node | Suggested grounding | Curation note |
|---|---|---|
| cell length small | **METPO:1000884** | Preserve CURIE verbatim; target class |
| parent cell-length class | **METPO:1000881** | Given parent |
| *Escherichia coli* | **NCBITaxon:562** | Strain-level child should be recorded where known |
| *Bacillus subtilis* | **NCBITaxon:1423** | UgtP and pyruvate-linked evidence |
| *Staphylococcus aureus* | **NCBITaxon:1280** | Cross-species pH/size evidence only |

### Genes, proteins, and complexes

* **FtsZ** — tubulin-like GTPase; Z-ring scaffold. Suggested GO grounding: **GO:0000917** for division-site formation is a process candidate; use taxon-specific UniProt identifiers only after strain confirmation.
* **FtsN** — late divisome protein and activator of septal peptidoglycan synthesis in *E. coli*.
* **FtsA** — membrane-associated divisome hub linking FtsZ to late division proteins.
* **OpgH** — *E. coli* glucosyltransferase and nutrient-dependent FtsZ antagonist.
* **UgtP** — *B. subtilis* glucosyltransferase and FtsZ regulator.
* **MinC, MinD, MinE / MinCDE system** — spatial inhibitor and reaction–diffusion system controlling polar exclusion of FtsZ.
* **Pgm, GalU** — UDP-glucose pathway candidates upstream of OpgH/UgtP; retain gene labels until taxon-specific identifiers are selected.
* **AceE/PdhA, AckA, Pta, PykA** — central-carbon candidates; mechanistic confidence varies by taxon.
* **AspC and DnaA** — plausible amino-acid-metabolism/replication-initiation branch from prior literature, but not sufficiently supported in the retrieved evidence for direct connection to METPO:1000884.

### Chemicals and environmental factors

| Node | Suggested grounding | Role |
|---|---|---|
| UDP-glucose | **CHEBI:18066** | Carbon-status signal activating OpgH/UgtP size-control branch |
| GTP | **CHEBI:15996** | FtsZ polymerization/GTPase substrate |
| pyruvate | **CHEBI:15361** | Candidate glycolysis-to-division signal in *B. subtilis* |
| extracellular proton activity / acidic pH | Label plus assay value | Increased FtsN septal recruitment in *E. coli* |
| carbon-rich medium | ENVO or medium ontology term after exact medium is known | Raises UDP-glucose and division inhibition |
| carbon-poor medium | Exact medium-specific identifier preferred | Relieves OpgH/UgtP inhibition |
| amino-acid starvation | GO/process or experimental-condition term | ppGpp-associated reduction in dimensions |
| (p)ppGpp | Ground exact chemical species separately | Stringent-response effector; avoid treating mixed species as one molecule if chemical precision is required |

### Processes and localizations

* FtsZ polymerization and Z-ring assembly.
* Midcell localization and polar exclusion.
* Septal FtsN recruitment.
* Divisome activation.
* Septal peptidoglycan synthesis.
* Cytokinesis and septation timing.
* Longitudinal cell-envelope growth.
* UDP-glucose biosynthesis.
* Glycolysis, pyruvate production, and acetyl-CoA/acetate metabolism.
* Stringent response.
* Relevant locations: cytoplasm, inner membrane, midcell/septum, periplasm in diderm bacteria, and cell wall.

## 4. Candidate causal edges

The compact edge inventory below distinguishes direct results from inferred inverse paths and counterexamples.

| subject | predicate | object | taxon/context | evidence strength | DOI |
|---|---|---|---|---|---|
| acidic extracellular pH | increases | septal FtsN recruitment | *Escherichia coli*; pH-dependent division control; smaller division size/length reported relative to neutral or alkaline conditions, not absolute 1.3–2 µm (mueller2020phdependentactivationof pages 11-13, mueller2020phdependentactivationof pages 2-3) | Direct | 10.1371/journal.pgen.1008685 |
| increased septal FtsN recruitment | promotes | earlier cytokinesis / reduced cell length at division | *E. coli*; acidic pH enriches FtsN at septum and activates division at reduced cell length (mueller2020phdependentactivationof pages 11-13, mueller2020phdependentactivationof pages 2-3) | Direct | 10.1371/journal.pgen.1008685 |
| alkaline extracellular pH | decreases | septal FtsN recruitment | *E. coli*; boundary/opposite condition with increased size at division (mueller2020phdependentactivationof pages 11-13, mueller2020phdependentactivationof pages 2-3) | Direct | 10.1371/journal.pgen.1008685 |
| carbon-rich conditions / high UDP-glucose | activates | OpgH/UgtP nutrient-sensing division inhibition pathway | *E. coli* OpgH and *Bacillus subtilis* UgtP; nutrient-rich growth increases size through division delay (buske2013thecterminus pages 225-230, westfall2017bacterialcellsize pages 7-9, westfall2017bacterialcellsize pages 9-11) | Direct for pathway role; cross-taxon synthesis partly review-backed | 10.1371/journal.pgen.1003663; 10.1146/annurev-micro-090816-093803 |
| OpgH (UDP-glucose-bound) | inhibits assembly of | FtsZ ring / FtsZ polymers | *E. coli*; OpgH antagonizes FtsZ assembly and delays division in nutrient-rich conditions (buske2013thecterminus pages 225-230, westfall2017bacterialcellsize pages 9-11) | Direct | 10.1371/journal.pgen.1003663 |
| inhibited FtsZ assembly | delays | division / cytokinetic ring maturation | *E. coli*; nutrient-dependent size control via OpgH-FtsZ interaction (buske2013thecterminus pages 225-230, westfall2017bacterialcellsize pages 9-11) | Direct | 10.1371/journal.pgen.1003663 |
| delayed division | increases | cell length / cell size | Rod-shaped bacteria including *E. coli*; relative increase only (buske2013thecterminus pages 225-230, westfall2017bacterialcellsize pages 7-9, westfall2017bacterialcellsize pages 9-11) | Direct | 10.1371/journal.pgen.1003663; 10.1146/annurev-micro-090816-093803 |
| low-carbon conditions / low UDP-glucose | reduces activity of | OpgH/UgtP-mediated FtsZ inhibition | *E. coli*, *B. subtilis*; apo-state or low signal relieves division inhibition (buske2013thecterminus pages 225-230, westfall2017bacterialcellsize pages 9-11) | Inferred inverse edge from direct nutrient-rich mechanism | 10.1371/journal.pgen.1003663; 10.1146/annurev-micro-090816-093803 |
| relief of OpgH/UgtP-mediated FtsZ inhibition | permits earlier assembly of | FtsZ ring | *E. coli*, *B. subtilis*; supports smaller cells under poorer carbon conditions, but not absolute 1.3–2 µm (buske2013thecterminus pages 225-230, westfall2017bacterialcellsize pages 9-11) | Inferred inverse edge | 10.1371/journal.pgen.1003663; 10.1146/annurev-micro-090816-093803 |
| increased FtsZ abundance | is rate-limiting for / accelerates | cell division timing | *E. coli*; cell divisions are rate-limited by FtsZ numbers (mueller2020phdependentactivationof pages 11-13) | Direct | 10.1038/s41467-024-54242-w |
| reduced effective FtsZ abundance or assembly | delays | division and increases length | General bacterial size-control framing; supported by FtsZ-limitation logic and nutrient/pH pathways (mueller2020phdependentactivationof pages 11-13, westfall2017bacterialcellsize pages 9-11) | Direct for principle, indirect for specific small-length class | 10.1038/s41467-024-54242-w; 10.1146/annurev-micro-090816-093803 |
| MinE overexpression | delays initiation of | FtsZ ring formation | *E. coli*; altered MinE/MinD ratio studied in single cells (vashistha2023bacterialcellsizechanges pages 1-2, vashistha2023bacterialcellsizechanges pages 8-9) | Direct | 10.1038/s41467-023-41487-0 |
| delayed FtsZ ring formation after MinE overexpression | increases | cell size / cell length | *E. coli*; negative boundary/counterexample because perturbation makes cells larger, not smaller (vashistha2023bacterialcellsizechanges pages 1-2) | Direct | 10.1038/s41467-023-41487-0 |
| amino-acid starvation / ppGpp accumulation | reduces | cell length and width | Review synthesis across bacteria; starvation-associated size reduction, but not specific absolute 1.3–2 µm lengths (westfall2017bacterialcellsize pages 9-11) | Review-backed, moderate | 10.1146/annurev-micro-090816-093803 |
| central carbon metabolism defects in acetate/pyruvate-linked nodes | associated with reduced | cell size | *E. coli*; metabolic perturbations can reduce size, but mechanism to absolute small-length class remains unresolved (westfall2018comprehensiveanalysisof pages 17-18) | Moderate / associative | 10.1371/journal.pgen.1007205 |


*Table: This table compiles the strongest curation-ready causal edges relevant to the microbial trait METPO:1000884, emphasizing whether evidence is direct or inferred. It is useful for separating high-confidence division-control mechanisms from boundary cases and for avoiding unsupported claims about absolute 1.3–2 µm cell length.*

### Recommended high-confidence triples

| Subject–predicate–object | Supporting snippet | Reference and interpretation |
|---|---|---|
| acidic extracellular pH **increases** septal FtsN recruitment | “Acidic environments lead to enrichment of FtsN at the septum” | Direct *E. coli* experiment; DOI [10.1371/journal.pgen.1008685](https://doi.org/10.1371/journal.pgen.1008685), published March 2020. (mueller2020phdependentactivationof pages 1-2, mueller2020phdependentactivationof pages 11-13) |
| increased septal FtsN recruitment **promotes** earlier cytokinesis | Acid pH caused “activation of division at a reduced cell length” | Direct, taxon-specific. (mueller2020phdependentactivationof pages 1-2, mueller2020phdependentactivationof pages 11-13) |
| earlier cytokinesis **reduces** cell length at division | pH 4.5 yielded approximately 75% of neutral-pH area; primary shape effect was length | Direct relative effect, but **uncertain for absolute 1.3–2 µm**. (mueller2020phdependentactivationof pages 2-3) |
| high UDP-glucose **activates/enables** OpgH-mediated FtsZ antagonism | UDP-glucose binding exposes an FtsZ-interaction site | Direct biochemical/genetic mechanism in *E. coli*. (buske2013thecterminus pages 225-230) |
| OpgH **inhibits** FtsZ assembly | OpgH fragment reduced FtsZ GTPase activity 25–84% and increased critical concentration 0.69→4.08 µM | Strong biochemical support; DOI [10.1371/journal.pgen.1003663](https://doi.org/10.1371/journal.pgen.1003663), published July 2013. (buske2013thecterminus pages 225-230) |
| inhibited FtsZ assembly **delays** division | OpgH obstructs cytokinetic-ring assembly and maturation | Strong mechanistic support. (buske2013thecterminus pages 225-230, westfall2017bacterialcellsize pages 9-11) |
| delayed division **increases** length/size | OpgH overexpression increased length as much as fivefold in the retrieved evidence | Direct opposite-direction edge useful for graph polarity. (strydom2017analysisofgenes pages 33-36) |
| low UDP-glucose **relieves** OpgH/UgtP inhibition of FtsZ | Under poor carbon, OpgH does not productively bind FtsZ; apo-UgtP is sequestered | Biologically well supported but expressed as an inverse edge; annotate as such. (buske2013thecterminus pages 225-230, westfall2017bacterialcellsize pages 9-11) |
| amino-acid starvation/(p)ppGpp response **reduces** length and width | Review reports reduction in both dimensions | Moderate, global-growth response; not length-specific. (westfall2017bacterialcellsize pages 9-11) |

### Recent mechanistic boundary edges

| Triple | Evidence and curation consequence |
|---|---|
| MinE overexpression **delays** stable FtsZ-ring formation | Direct 2023 single-cell *E. coli* evidence. (vashistha2023bacterialcellsizechanges pages 1-2) |
| delayed FtsZ-ring formation **increases** cell size | This produces larger cells and therefore should be represented as an opposite branch, not as support for METPO:1000884. (vashistha2023bacterialcellsizechanges pages 1-2) |
| FtsZ abundance **rate-limits** division | A 2024 quantitative study identified FtsZ number, but not normal FtsN/FtsA abundance, as rate-limiting. This supports FtsZ accumulation as a central control node, although no absolute 1.3–2 µm endpoint was established. |

## 5. Recent developments, expert interpretation, and applications

### 2023–2024 developments

* **Min-system dosage (2023):** Vashistha and colleagues showed that relative Min-protein expression changes the onset of Z-ring assembly and steady-state cell size. The result argues that Min dynamics participate in size control rather than serving only as a division-site positioning system. DOI [10.1038/s41467-023-41487-0](https://doi.org/10.1038/s41467-023-41487-0), published September 2023. (vashistha2023bacterialcellsizechanges pages 1-2, vashistha2023bacterialcellsizechanges pages 8-9)
* **Rate-limiting division processes (2024):** Quantitative upregulation and stochastic modeling indicate that FtsZ numbers are rate-limiting, whereas ordinary FtsN and FtsA levels are not. This refines the model of divisome activation and cautions against treating a single FtsN-arrival event as the sole size checkpoint. DOI [10.1038/s41467-024-54242-w](https://doi.org/10.1038/s41467-024-54242-w), published November 2024.
* **Slow-growth control (2024):** Modeling of slow-growing *E. coli* found that no single degradation, nonlinear-accumulation, or commitment-size model explained all datasets. Degradation models performed better for larger cells, whereas size-dependent models better described smaller cells. DOI [10.1038/s41540-024-00383-z](https://doi.org/10.1038/s41540-024-00383-z), published May 2024. This is a warning against encoding one universal “adder mechanism.”

### Expert analysis

The authoritative synthesis is that bacterial size is **multifactorial**: nutrient signaling, biosynthetic capacity, replication, envelope synthesis, and division all contribute. Nutrient-rich *Salmonella* can be up to **three times larger** than nutrient-poor cells, yet growth rate alone does not determine cell size. UDP-glucose-dependent OpgH/UgtP signaling provides one of the clearest direct molecular links from nutrient status to division machinery. (westfall2017bacterialcellsize pages 7-9, westfall2017bacterialcellsize pages 9-11, westfall2018comprehensiveanalysisof pages 17-18)

For TraitMech, the graph should therefore distinguish:

1. **set-point mechanisms** that alter septation timing;
2. **homeostatic strategies** such as adder or sizer-like behavior;
3. **global growth effects** that change both length and width; and
4. the final **measurement assertion** that length is 1.3–2 µm.

Only the fourth establishes membership in **METPO:1000884**.

### Real-world applications

* **Antibacterial mechanism profiling:** FtsZ inhibitors prevent normal Z-ring formation and produce elongated cells; quantitative cell and nucleoid-length profiles can classify inhibitor mechanisms. This is useful for drug discovery, but the resulting phenotype is generally the opposite of “cell length small.”
* **Morphology engineering:** Modulating division-protein expression or nutrient-signaling branches can tune microbial size for microscopy, synthetic biology, and potentially production phenotypes. Such applications require balancing division, envelope synthesis, and viability.
* **Environmental interpretation:** pH- and nutrient-dependent size shifts can confound taxonomic or ecological microscopy. Trait annotation should record the culture or environmental condition rather than treating length as immutable.
* **Phenotypic screens:** Genome-wide imaging and metabolic-knockout screens can identify candidate length-control genes, but associations need targeted rescue or epistasis experiments before causal graph inclusion.

## 6. Warnings—claims not yet suitable for direct TraitMech curation

1. **Do not curate “nutrient limitation → METPO:1000884” directly** unless the source reports calibrated cell lengths within 1.3–2 µm. Existing evidence mainly reports ratios or percentage reductions.
2. **Do not convert smaller area or volume into smaller length.** Preserve the measured quantity.
3. **Do not use MinE overexpression as a small-cell cause.** It delayed ring formation and increased size. (vashistha2023bacterialcellsizechanges pages 1-2)
4. **Do not use FtsZ inhibitors as small-cell causes.** Division inhibition usually elongates or filaments cells.
5. **Treat low-UDP-glucose → earlier FtsZ assembly as an inverse-inferred edge** unless a source directly perturbed UDP-glucose and measured both assembly and absolute length.
6. **Keep UgtP and OpgH taxon-specific.** They are functionally analogous but nonhomologous and need separate nodes.
7. **Do not generalize the *E. coli* FtsN mechanism to all bacteria.** Divisome composition differs, and some bacteria lack FtsZ.
8. **Retain AspC/aspartate, PykA/pyruvate/PdhA, fatty-acid synthesis, cAMP–CRP/BolA, and individual acetate-metabolism genes as provisional branches** until direct length-specific evidence and exact assay values are verified.
9. **Avoid invented ontology identifiers.** Taxon-specific UniProt, KEGG, MetaCyc, Rhea, and EC identifiers should be added only after strain and biochemical reaction are confirmed.
10. **Do not equate adder behavior with the small-length class.** It explains convergence around a set point but not the value of that set point.

## 7. DOI-first bibliography

1. Vashistha H, et al. “Bacterial cell-size changes resulting from altering the relative expression of Min proteins.” *Nature Communications* 14 (September 2023). DOI: [10.1038/s41467-023-41487-0](https://doi.org/10.1038/s41467-023-41487-0). (vashistha2023bacterialcellsizechanges pages 1-2, vashistha2023bacterialcellsizechanges pages 8-9)
2. Männik J, et al. “Determining the rate-limiting processes for cell division in *Escherichia coli*.” *Nature Communications* 15 (November 2024). DOI: [10.1038/s41467-024-54242-w](https://doi.org/10.1038/s41467-024-54242-w).
3. Nieto C, et al. “Mechanisms of cell size regulation in slow-growing *Escherichia coli* cells: discriminating models beyond the adder.” *npj Systems Biology and Applications* 10 (May 2024). DOI: [10.1038/s41540-024-00383-z](https://doi.org/10.1038/s41540-024-00383-z).
4. Mueller EA, Westfall CS, Levin PA. “pH-dependent activation of cytokinesis modulates *Escherichia coli* cell size.” *PLOS Genetics* 16 (March 2020). DOI: [10.1371/journal.pgen.1008685](https://doi.org/10.1371/journal.pgen.1008685). (mueller2020phdependentactivationof pages 1-2, mueller2020phdependentactivationof pages 11-13, mueller2020phdependentactivationof pages 2-3)
5. Hill NS, Buske PJ, Shi Y, Levin PA. “A Moonlighting Enzyme Links *Escherichia coli* Cell Size with Central Metabolism.” *PLOS Genetics* 9 (July 2013). DOI: [10.1371/journal.pgen.1003663](https://doi.org/10.1371/journal.pgen.1003663). (buske2013thecterminus pages 225-230)
6. Westfall CS, Levin PA. “Comprehensive analysis of central carbon metabolism illuminates connections between nutrient availability, growth rate, and cell morphology in *Escherichia coli*.” *PLOS Genetics* 14 (February 2018). DOI: [10.1371/journal.pgen.1007205](https://doi.org/10.1371/journal.pgen.1007205). (westfall2018comprehensiveanalysisof pages 17-18)
7. Westfall CS, Levin PA. “Bacterial Cell Size: Multifactorial and Multifaceted.” *Annual Review of Microbiology* 71 (September 2017): 499–517. DOI: [10.1146/annurev-micro-090816-093803](https://doi.org/10.1146/annurev-micro-090816-093803). (westfall2017bacterialcellsize pages 7-9, westfall2017bacterialcellsize pages 9-11)
8. Monahan LG, et al. “Coordinating Bacterial Cell Division with Nutrient Availability: a Role for Glycolysis.” *mBio* 5 (July 2014). DOI: [10.1128/mBio.00935-14](https://doi.org/10.1128/mBio.00935-14).
9. Liu F, et al. “AspC-Mediated Aspartate Metabolism Coordinates the *Escherichia coli* Cell Cycle.” *PLOS ONE* 9 (March 2014). DOI: [10.1371/journal.pone.0092229](https://doi.org/10.1371/journal.pone.0092229).
10. Si F, et al. “Mechanistic Origin of Cell-Size Control and Homeostasis in Bacteria.” *Current Biology* 29 (June 2019): 1760–1770.e7. DOI: [10.1016/j.cub.2019.04.062](https://doi.org/10.1016/j.cub.2019.04.062).

## Curation recommendation

A defensible first expansion of `cell_length_small.yaml` should add a **contextual upstream mechanism** centered on low carbon/low UDP-glucose, relieved OpgH or UgtP inhibition, FtsZ assembly, and earlier septation, plus a separately supported acidic-pH/FtsN branch for *E. coli*. The terminal edge to **“METPO:1000884”** should remain **uncertain or conditional** until a source reports an absolute 1.3–2 µm length under the same perturbation. The existing adder edge should be retained as a homeostasis mechanism, not treated as proof of the absolute small-size class.

References

1. (mueller2020phdependentactivationof pages 2-3): Elizabeth A. Mueller, Corey S. Westfall, and Petra Anne Levin. Ph-dependent activation of cytokinesis modulates escherichia coli cell size. Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008685, doi:10.1371/journal.pgen.1008685. This article has 46 citations and is from a domain leading peer-reviewed journal.

2. (westfall2018comprehensiveanalysisof pages 17-18): Corey S. Westfall and Petra Anne Levin. Comprehensive analysis of central carbon metabolism illuminates connections between nutrient availability, growth rate, and cell morphology in escherichia coli. PLOS Genetics, 14:e1007205, Feb 2018. URL: https://doi.org/10.1371/journal.pgen.1007205, doi:10.1371/journal.pgen.1007205. This article has 79 citations and is from a domain leading peer-reviewed journal.

3. (buske2013thecterminus pages 225-230): Paul J. Buske. The c terminus of ftsz regulates ftsz assembly dynamics and is required for bacillus subtilis cell division. ArXiv, Jan 2013. URL: https://doi.org/10.7936/k7668b61, doi:10.7936/k7668b61. This article has 0 citations.

4. (westfall2017bacterialcellsize pages 9-11): Corey S. Westfall and Petra Anne Levin. Bacterial cell size: multifactorial and multifaceted. Annual review of microbiology, 71:499-517, Sep 2017. URL: https://doi.org/10.1146/annurev-micro-090816-093803, doi:10.1146/annurev-micro-090816-093803. This article has 96 citations and is from a peer-reviewed journal.

5. (mueller2020phdependentactivationof pages 11-13): Elizabeth A. Mueller, Corey S. Westfall, and Petra Anne Levin. Ph-dependent activation of cytokinesis modulates escherichia coli cell size. Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008685, doi:10.1371/journal.pgen.1008685. This article has 46 citations and is from a domain leading peer-reviewed journal.

6. (vashistha2023bacterialcellsizechanges pages 1-2): Harsh Vashistha, Joanna Jammal-Touma, Kulveer Singh, Yitzhak Rabin, and Hanna Salman. Bacterial cell-size changes resulting from altering the relative expression of min proteins. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41487-0, doi:10.1038/s41467-023-41487-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

7. (vashistha2023bacterialcellsizechanges pages 8-9): Harsh Vashistha, Joanna Jammal-Touma, Kulveer Singh, Yitzhak Rabin, and Hanna Salman. Bacterial cell-size changes resulting from altering the relative expression of min proteins. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41487-0, doi:10.1038/s41467-023-41487-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

8. (westfall2017bacterialcellsize pages 7-9): Corey S. Westfall and Petra Anne Levin. Bacterial cell size: multifactorial and multifaceted. Annual review of microbiology, 71:499-517, Sep 2017. URL: https://doi.org/10.1146/annurev-micro-090816-093803, doi:10.1146/annurev-micro-090816-093803. This article has 96 citations and is from a peer-reviewed journal.

9. (mueller2020phdependentactivationof pages 1-2): Elizabeth A. Mueller, Corey S. Westfall, and Petra Anne Levin. Ph-dependent activation of cytokinesis modulates escherichia coli cell size. Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008685, doi:10.1371/journal.pgen.1008685. This article has 46 citations and is from a domain leading peer-reviewed journal.

10. (strydom2017analysisofgenes pages 33-36): L. Strydom, John F. Jewell, Michael A. Meier, Gavin M. George, B. Pfister, S. Zeeman, J. Kossmann, and J. Lloyd. Analysis of genes involved in glycogen degradation in escherichia coli. FEMS Microbiology Letters, 364:&NA;, Feb 2017. URL: https://doi.org/10.1093/femsle/fnx016, doi:10.1093/femsle/fnx016. This article has 16 citations and is from a peer-reviewed journal.