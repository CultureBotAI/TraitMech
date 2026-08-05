---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:53:42.035611'
end_time: '2026-08-04T08:00:36.590967'
duration_seconds: 414.56
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell width very small
  trait_identifier: METPO:1000887
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_width_very_small
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-width phenotype in which the shorter cell dimension is at most
    approximately 0.5 micrometers.
  parent_traits: METPO:1000882
  synonyms: W_<=0.5
  evidence_summary: 'DOI:10.1038/ismej.2014.60: small cells and genomes (Streamlining
    review links very narrow cell widths to oligotrophic and streamlined lineages.)'
  causal_graph_summary: 'cell_width_very_small_streamlining: 11 nodes, 8 edges'
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
- **Trait label:** cell width very small
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000887
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension is at most approximately 0.5 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_<=0.5
- **Existing evidence:** DOI:10.1038/ismej.2014.60: small cells and genomes (Streamlining review links very narrow cell widths to oligotrophic and streamlined lineages.)
- **Existing causal graph summary:** cell_width_very_small_streamlining: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **cell width very small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_very_small.yaml`.

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
- **Trait label:** cell width very small
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000887
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension is at most approximately 0.5 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_<=0.5
- **Existing evidence:** DOI:10.1038/ismej.2014.60: small cells and genomes (Streamlining review links very narrow cell widths to oligotrophic and streamlined lineages.)
- **Existing causal graph summary:** cell_width_very_small_streamlining: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **cell width very small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_very_small.yaml`.

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


# Curation report: microbial “cell width very small”

## Executive assessment

**Target:** `METPO:1000887` — a morphology class describing cells whose shorter dimension is at most approximately **0.5 µm**; parent `METPO:1000882`; synonym `W_<=0.5`.

The literature supports a strong, broadly conserved mechanism in which the **MreB–RodZ–Rod complex controls rod-cell diameter through oriented peptidoglycan synthesis**. Recent work adds two upstream layers: ATP- and lipid-dependent MreB assembly, and a load-bearing role for the Gram-negative outer membrane. However, these experiments generally manipulate widths around the dimensions of model organisms and do **not** demonstrate that the same perturbations produce the threshold phenotype `METPO:1000887`. The direct connection between this molecular machinery and width ≤0.5 µm therefore remains an inference.

By contrast, widths below 0.5 µm are well represented among ultramicrobacteria. A 2024 review uses a proliferating-cell diameter below **0.3 µm**, volume below **0.1 µm³**, and genomes of approximately **0.58–3.2 Mb** as ultramicrobacterial characteristics. Its Lake Baikal survey found **7×10⁴ filterable cells/mL** at 0–50 m and an average **4.4%** contribution to total bacterial abundance. Nevertheless, passage through a 0.2-µm filter is an operational fraction, not a direct measurement of cell width. (belykh2024ultramicrobacteriaandfilterable pages 1-2)

## 1. Trait scope and boundary cases

### Included phenotype

The graph endpoint should mean an **observed geometrical width**—the shorter dimension of a vegetative microbial cell—of approximately ≤0.5 µm. For rods, this is normally diameter perpendicular to the long axis; for cocci or irregular cells, the measurement protocol must state how the shorter dimension was obtained.

### Distinctions required for curation

- **Not equivalent to small cell volume.** A long, narrow rod can satisfy the width threshold without being an ultralow-volume cell. Conversely, a short cell can have low volume but width >0.5 µm.
- **Not equivalent to ultramicrobacterium.** The reviewed operational definition—diameter <0.3 µm and volume <0.1 µm³—is stricter in one respect and incorporates volume and stable proliferation. (belykh2024ultramicrobacteriaandfilterable pages 1-2)
- **Not equivalent to filterability.** Passing a nominal 0.2-µm filter depends on cell orientation, deformability, pore-size distribution, sample processing, and noncellular particles.
- **Not equivalent to starvation-induced reductive division.** Poor media often decrease cell size and favorable conditions restore or increase it, but this does not establish constitutive narrow width or a width-specific response. (belykh2024ultramicrobacteriaandfilterable pages 1-2)
- **Not equivalent to genome streamlining or oligotrophy.** Streamlining theory links nutrient limitation, small genomes, and small cells through selection for resource efficiency, but also emphasizes counterexamples and niche dependence. (giovannoni2014implicationsofstreamlining pages 1-2, giovannoni2014implicationsofstreamlining pages 2-3)
- **Width and length should not be collapsed into total size.** A genome-wide *E. coli* perturbation study found width and length to be independently regulated, while growth rate was not a determinant of cell size across approximately 4,000 perturbations. Thus, generic “slow growth → small width” edges are not justified. (shi2017deepphenotypicmapping pages 9-10)

## 2. Current mechanistic model

In rod-shaped bacteria, MreB assemblies align circumferentially and orient cell-wall enzymes so that new peptidoglycan strands are inserted in radial hoops perpendicular to the long axis. RodZ and the membrane proteins MreC/MreD couple this cytoskeletal organization to the RodA–PBP2 synthase. MreC-mediated conformational activation of PBP2 is proposed to activate RodA, shifting the Rod complex into an active state. The resulting balance and orientation of lateral wall insertion determine diameter and preserve rod shape. (morgenstein2015rodzlinksmreb pages 6-6, fivenson2023arolefor pages 1-2, mao2023ontherole pages 1-2)

A surface-area-to-volume model adds that peptidoglycan precursor flux may govern the balance between constrained Rod-complex insertion and more expansive class-A PBP activity. In that model, high precursor availability recruits more MreB and favors narrowing, whereas low precursor availability permits widening. The source explicitly treats this as a hypothesis requiring additional testing, so these precursor-flux edges should remain provisional. (harris2018surfaceareato pages 9-12)

### Recent developments, 2023–2024

1. **MreB biochemical assembly:** *Geobacillus stearothermophilus* MreB formed paired protofilaments on lipid surfaces with ATP or GTP, but not ADP, GDP, or nonhydrolysable ATP analogues. Polymerization on lipid monolayers occurred above approximately **0.55 µM**, with a theoretical critical concentration near **0.45 µM**. ATP and membrane lipids therefore provide experimentally supported upstream inputs to MreB assembly, although the assay was in vitro and did not measure cell width. (mao2023ontherole pages 7-8, mao2023ontherole pages 1-2)
2. **Outer-membrane morphogenesis:** Strengthening lipopolysaccharide synthesis or outer-membrane load-bearing capacity restored elongated shape to *E. coli mreC* hypomorphs and restored MreB-guided wall insertion. This establishes that Gram-negative shape is jointly supported by peptidoglycan synthesis and outer-membrane mechanics. (fivenson2023arolefor pages 2-3, fivenson2023arolefor pages 1-2)
3. **Ecological evidence:** Lake Baikal femtoplankton included abundant and taxonomically diverse cells passing 0.2-µm filters. The work supports real-world prevalence of ultra-small microorganisms but does not identify genes that causally set their widths. (belykh2024ultramicrobacteriaandfilterable pages 1-2)
4. **Proteome trade-offs:** A 2024 synthesis emphasizes that slow-growing oligotrophs invest in survival, adaptation, and nutrient acquisition rather than maximal growth. It also describes (p)ppGpp–DksA and cAMP–CRP as nutrient-responsive proteome-allocation systems. These are plausible ecological context nodes, but the review does not establish a direct causal route from either regulator to ≤0.5-µm width. (zhu2024shapingofmicrobial pages 1-2)

## 3. Candidate nodes grouped by type

### Trait and quantitative phenotype

- **cell width very small** — `METPO:1000887`
- **parent phenotype** — `METPO:1000882`
- Cell width/diameter measurement
- Cell volume; ultramicrobacterial cell volume <0.1 µm³
- Surface-area-to-volume ratio
- Cell-wall surface synthesis rate

### Genes and proteins

- **MreB** — bacterial actin-like cytoskeletal protein; use taxon-specific UniProt identifiers only after strain selection.
- **RodZ** — membrane linker coupling MreB and wall-synthesis machinery.
- **MreC**, **MreD** — Rod-complex membrane proteins; MreC has evidence for activation of PBP2, whereas MreD function remains less clear. (fivenson2023arolefor pages 1-2)
- **PBP2 / MrdA** — class-B penicillin-binding transpeptidase.
- **RodA / MrdB** — SEDS-family peptidoglycan glycosyltransferase.
- **LpxC** — UDP-3-O-acyl-N-acetylglucosamine deacetylase; controls the first committed step of LPS synthesis.
- **FtsH**, **LapB/YciM**, **YejM/PbgA/LapC** — LpxC turnover and LPS-homeostasis factors.
- **Class-A PBPs** — alternative bifunctional peptidoglycan synthases.
- **FtsZ** — useful division/size covariate, but not presently a supported direct cause of very small width.

### Complexes and cellular structures

- Rod complex / elongasome — preferably retain as a label-only candidate unless the project has an approved complex ontology.
- MreB filament/protofilament assembly
- Cytoplasmic membrane
- Peptidoglycan cell wall
- Gram-negative outer membrane
- Lipopolysaccharide layer

### Chemicals and materials

- **ATP** — `CHEBI:15422`
- **GTP** — `CHEBI:15996`
- ADP, GDP, and nonhydrolysable ATP analogues—negative/control states in the MreB assay.
- Peptidoglycan
- Lipopolysaccharide
- Membrane lipids
- Potassium chloride/cation concentration—potential regulator of MreB or membrane mechanics, but demonstrated only in vitro and not connected to width ≤0.5 µm. (mao2023ontherole pages 7-8)
- A22—MreB inhibitor; useful experimental-factor node, not an ecological mechanism.

### Processes and functions

- MreB polymerization and membrane binding
- Circumferential MreB alignment
- Oriented peptidoglycan insertion
- Peptidoglycan glycan polymerization and peptide cross-linking
- Rod-shaped cell elongation
- Outer-membrane fortification/load bearing
- LPS biosynthesis and LpxC proteolysis
- Genome/cellular streamlining
- Nutrient uptake and transporter investment
- Reductive division under nutrient limitation

### Environmental and experimental factors

- Nutrient-poor/oligotrophic aquatic environment
- Poor versus enriched cultivation medium
- Large effective population size and chronic nutrient limitation—streamlining-theory variables
- In vitro lipid monolayer/liposome system
- Osmotic/turgor load
- Rich versus minimal medium

### Taxa and contexts

- *Escherichia coli* — direct RodZ, MreB/PBP2 mutant, and outer-membrane evidence.
- *Geobacillus stearothermophilus* — MreB polymerization biochemistry.
- *Bacillus subtilis* — foundational MreB/curvature model; taxon-specific machinery differs from *E. coli*.
- Pelagibacterales/SAR11, *Prochlorococcus*, OM43, SAR86, and small marine Actinobacteria — streamlining examples rather than direct width-mechanism experiments. Streamlined Pelagibacter cells were reported at approximately **0.01 µm³**, with **67%** of cellular protein allocated to transport functions; SAR432 cell volume was approximately **0.013 µm³**. (giovannoni2014implicationsofstreamlining pages 3-4)
- Lake Baikal femtobacterioplankton — environmental occurrence evidence.

## 4. Candidate causal edges

The table below separates graph-ready molecular mechanisms from ecological associations and threshold extrapolations.

| Subject | Predicate | Object | Evidence strength/context | DOI/date | Supporting snippet | Curation note |
|---|---|---|---|---|---|---|
| ATP | facilitates | MreB polymerization on lipid surfaces | **Direct molecular/biochemical**; *Geobacillus stearothermophilus* MreB in vitro; width-general, not <=0.5 µm-specific (mao2023ontherole pages 1-2, mao2023ontherole pages 7-8) | 10.7554/eLife.84505 (2023-10-11) | “*Geobacillus stearothermophilus* MreB forms straight pairs of protofilaments on lipid surfaces in the presence of ATP or GTP, but not in the presence of ADP, GDP or non-hydrolysable ATP analogs.” / “polymerization is strongly enhanced by both ATP and lipids.” (mao2023ontherole pages 1-2, mao2023ontherole pages 7-8) | Good candidate edge: **ATP positively_regulates MreB filament assembly**. Does not by itself establish very small width. |
| membrane lipids | facilitate | MreB polymerization / membrane-bound protofilaments | **Direct molecular/biochemical**; *G. stearothermophilus* MreB in vitro; width-general (mao2023ontherole pages 1-2, mao2023ontherole pages 7-8) | 10.7554/eLife.84505 (2023-10-11) | “both lipids and ATP are facilitators of MreB polymerization” / “On a lipid monolayer, polymers were observed…” (mao2023ontherole pages 1-2, mao2023ontherole pages 7-8) | Good candidate edge: **membrane lipid binding enables/promotes MreB polymerization**. Upstream mechanistic node. |
| MreB filament orientation | directs/orients | circumferential peptidoglycan insertion | **Direct mechanistic model with strong experimental support**; rod-shaped bacteria; not trait-specific to <=0.5 µm (mao2023ontherole pages 1-2) | 10.7554/eLife.84505 (2023-10-11) | “MreB assemblies self-align circumferentially… The current model is that self-aligned MreB filaments restrict the diffusion of CW biosynthetic proteins in the membrane and orient their motion to insert new peptidoglycan strands in radial hoops perpendicular to the long axis of the cell” (mao2023ontherole pages 1-2) | Curatable as **MreB organization positively_regulates oriented cell-wall elongation**; note this is a general width-control mechanism. |
| RodZ | links | MreB to cell-wall synthesis | **Direct experimental**; *E. coli* morphogenesis; width-general (morgenstein2015rodzlinksmreb pages 6-6) | 10.1073/pnas.1509610112 (2015-09) | “RodZ links MreB to cell wall synthesis to mediate MreB rotation and robust morphogenesis” (morgenstein2015rodzlinksmreb pages 6-6) | Strong edge for Gram-negative rods. Taxon/context should be noted. |
| MreB helical pitch angle | determines | cell diameter / width | **Direct experimental**; *E. coli*; quantitative diameter control, not <=0.5 µm-specific (morgenstein2015rodzlinksmreb pages 6-6) | 10.1073/pnas.1509610112 (2015-09) | “they establish that MreB helical pitch angle determines cell diameter in *E. coli*” (morgenstein2015rodzlinksmreb pages 6-6) | Strong width-control edge. Curate as general bacterial width determinant with organism note. |
| MreC | activates | PBP2 | **Direct mechanistic interpretation from genetics/structure/cytology**; *E. coli* Rod complex (fivenson2023arolefor pages 1-2) | 10.1073/pnas.2301987120 (2023-08-22) | “Genetic, structural, and cytological evidence suggests that MreC activates the complex by inducing a conformational change in PBP2” (fivenson2023arolefor pages 1-2) | Good candidate edge; activation phrasing is source-supported. |
| activated PBP2 | activates | RodA | **Direct mechanistic interpretation**; *E. coli* Rod complex (fivenson2023arolefor pages 1-2) | 10.1073/pnas.2301987120 (2023-08-22) | “which in turn activates RodA, shifting the complex from an inactive to an active state” (fivenson2023arolefor pages 1-2) | Curate as Rod-complex activation logic; still general width/shape control rather than very small-width specific. |
| RodA-PBP2 / Rod complex | promotes | cell elongation and rod shape determination | **Direct experimental/current understanding**; conserved rod-shape system in Gram-negative bacteria (fivenson2023arolefor pages 1-2) | 10.1073/pnas.2301987120 (2023-08-22) | “The SEDS-bPBP complexes RodA-PBP2… play essential roles in rod shape determination… The rod shape-determining system is called the Rod complex… It promotes the elongation of bacilli and maintains their characteristic rod shape.” (fivenson2023arolefor pages 1-2) | Strong general morphogenesis edge; suitable backbone node for width graph. |
| increased LPS synthesis / OM fortification | restores | rod shape in *mreC* hypomorphs | **Direct experimental suppression**; *E. coli*; envelope mechanics effect on width/shape (fivenson2023arolefor pages 2-3, fivenson2023arolefor pages 1-2) | 10.1073/pnas.2301987120 (2023-08-22) | “these suppressors function by increasing the production of LPS” / “Overproduction of LpxC indeed promoted the growth of mreC(R292H) and mreC(G156D) mutants on LB and restored an elongated rod-like shape” (fivenson2023arolefor pages 2-3) | Curate as **increased LPS synthesis/OM stiffness compensates for defective Rod-complex morphogenesis**; suppression edge, context-specific. |
| nutrient-poor selection | favors | cell-size minimization | **Ecological/theoretical association**; streamlining theory; not direct manipulation (giovannoni2014implicationsofstreamlining pages 1-2) | 10.1038/ismej.2014.60 (2014-04-17) | “streamlining theory attributes small cells and genomes to selection for efficient use of nutrients in populations where… nutrients limit growth” / “ ‘streamlining’ refers more generally to selection that favors minimization of cell size and complexity.” (giovannoni2014implicationsofstreamlining pages 1-2) | Useful ecological edge, but mark **inferred/theoretical** rather than direct mechanistic proof. |
| smaller cell size | increases | surface-to-volume ratio and nutrient transport advantage | **Authoritative review/theoretical**; ecological rationale, not direct width experiment (giovannoni2014implicationsofstreamlining pages 1-2) | 10.1038/ismej.2014.60 (2014-04-17) | “cell size reduction can be a result of the same selective pressure, with smaller cells in principle benefitting not just by reduced replication costs, but also by higher surface-to-volume ratios that confer superior nutrient transport properties” (giovannoni2014implicationsofstreamlining pages 1-2) | Good ecological node/edge. Mark as **general principle** not exclusive to <=0.5 µm. |
| oligotrophic / poor-medium cultivation | decreases | cell size | **Observational/reviewed evidence**; ultramicrobacteria literature summary; not direct width-only measure (belykh2024ultramicrobacteriaandfilterable pages 1-2) | 10.31951/2658-3518-2024-A-4-795 (2024-08-30) | “In the cultivation on ‘poor’ media, most bacteria usually show a decrease in cell size. When the cells are transferred to more favorable conditions, the size is restored or increased.” (belykh2024ultramicrobacteriaandfilterable pages 1-2) | Candidate environmental edge, but broad “cell size” rather than width. Mark uncertain for width-specific curation. |
| genome streamlining | associated_with | very small cells | **Association/review**; not direct causal mechanism (giovannoni2014implicationsofstreamlining pages 1-2, giovannoni2014implicationsofstreamlining pages 3-4) | 10.1038/ismej.2014.60 (2014-04-17) | “streamlining theory attributes small cells and genomes…” / “Streamlined marine bacteria include some of the world’s smallest organisms… raising the possibility that increased surface-to-volume ratios might also drive streamlining in some cases.” (giovannoni2014implicationsofstreamlining pages 1-2, giovannoni2014implicationsofstreamlining pages 3-4) | Keep as **association only**. Do not over-curate as direct cause of <=0.5 µm width without lineage-specific evidence. |


*Table: This table summarizes source-backed candidate causal and associational edges relevant to microbial very small cell width (METPO:1000887). It separates direct molecular width-control mechanisms from broader ecological inferences and highlights where evidence does not specifically establish widths of <=0.5 µm.*

### Recommended graph architecture

A conservative TraitMech graph should contain two evidence layers:

1. **Direct width-control backbone:** ATP/lipid environment → MreB assembly → MreB orientation; RodZ/MreC/PBP2/RodA → oriented peptidoglycan synthesis → cell-width control. MreB and PBP2 mutations causally tune *E. coli* width, including measured wider mutants of **1.34±0.06 µm** and **1.16±0.06 µm**, versus **0.94±0.04 µm** wild type. These data establish width control but not the ≤0.5-µm endpoint. (shi2017deepphenotypicmapping pages 1-3, shi2017deepphenotypicmapping pages 3-3)
2. **Ecological/adaptive layer:** nutrient limitation → selection for streamlining/smaller cells → increased surface-area-to-volume ratio → nutrient-acquisition advantage. This layer should use predicates such as `associated_with`, `may_favor`, or an uncertainty annotation—not unconditional molecular causation. (giovannoni2014implicationsofstreamlining pages 1-2, giovannoni2014implicationsofstreamlining pages 3-4)

The final edge from “cell-width control/narrowing” to `METPO:1000887` should be marked **inferred** until a study reports an intervention that moves a measured organism across the approximately 0.5-µm threshold.

## 5. Applications and real-world implementation

- **Environmental size fractionation:** 0.2-µm filtration, microscopy, and 16S sequencing are used to quantify femtoplankton. In Lake Baikal, the <0.2-µm fraction averaged 4.4% of total bacteria in the sampled upper water column. This is an implementation for community surveillance, not a direct phenotype assay. (belykh2024ultramicrobacteriaandfilterable pages 1-2)
- **Quantitative morphology screens:** High-throughput imaging and mutant libraries can resolve width-specific genetic effects independently of length and growth rate. Such screens are appropriate for finding perturbations that cross the METPO threshold. (shi2017deepphenotypicmapping pages 9-10, shi2017deepphenotypicmapping pages 3-3)
- **Antimicrobial target discovery:** MreB, PBP2, RodA, and envelope biogenesis are attractive morphogenesis targets; A22 and PBP2 inhibition cause rounding and loss of viability. However, antimicrobial perturbations generally destroy rod-shape maintenance rather than generate viable, stably very narrow cells. (shi2018howtobuild pages 7-9, shi2017deepphenotypicmapping pages 1-3)
- **Cultivation of the uncultured majority:** Streamlined organisms may lack common regulatory or biosynthetic systems, helping explain culture dependence and community interdependence. Low-nutrient, dilution-to-extinction, and filtration–dilution–acclimatization methods are therefore relevant practical strategies. (belykh2024ultramicrobacteriaandfilterable pages 1-2, giovannoni2014implicationsofstreamlining pages 1-2)

## 6. Warnings: claims not yet ready for TraitMech

1. **Do not curate “MreB causes `METPO:1000887`” as established.** MreB causally controls width, but retrieved intervention studies do not demonstrate a transition to ≤0.5 µm.
2. **Do not use filter passage as proof of width.** Require microscopy or another calibrated dimensional assay.
3. **Do not encode small genome → very small width as causal.** Streamlining supplies evolutionary theory and correlations; symbionts can also have tiny genomes through drift, and successful organisms can be large and genomically complex. (giovannoni2014implicationsofstreamlining pages 1-2, giovannoni2014implicationsofstreamlining pages 2-3)
4. **Do not encode oligotrophy or slow growth as sufficient.** Poor medium can decrease cell size, but oligotrophy, growth strategy, and width are separable traits. (zhu2024shapingofmicrobial pages 1-2, belykh2024ultramicrobacteriaandfilterable pages 1-2)
5. **Do not generalize Gram-negative LPS edges to Gram-positive taxa.** The outer-membrane mechanism is specific to diderm envelopes. (fivenson2023arolefor pages 1-2)
6. **Keep ATP/lipid → MreB → width taxon- and assay-qualified.** The 2023 evidence is in vitro with *G. stearothermophilus* MreB; the authors explicitly conclude that assembly dynamics can vary among organisms. (mao2023ontherole pages 1-2)
7. **Treat precursor-flux narrowing as provisional.** The surface-to-volume review presents the mechanism as a hypothesis requiring validation. (harris2018surfaceareato pages 9-12)
8. **Avoid unverified CURIEs.** Use label-only nodes for the Rod complex, MreB organizational states, streamlining, and taxon-specific proteins until identifiers are checked against the project’s ontology release.

## 7. DOI-first bibliography

1. **Belykh OI et al.** “Ultramicrobacteria and filterable bacteria in the plankton of Lake Baikal.” *Limnology and Freshwater Biology* (published **30 August 2024**). DOI: [10.31951/2658-3518-2024-A-4-795](https://doi.org/10.31951/2658-3518-2024-A-4-795). (belykh2024ultramicrobacteriaandfilterable pages 1-2)
2. **Zhu M, Dai X.** “Shaping of microbial phenotypes by trade-offs.” *Nature Communications* 15, 4238 (accepted **6 May 2024**). DOI: [10.1038/s41467-024-48591-9](https://doi.org/10.1038/s41467-024-48591-9). (zhu2024shapingofmicrobial pages 1-2)
3. **Mao W et al.** “On the role of nucleotides and lipids in the polymerization of the actin homolog MreB from a Gram-positive bacterium.” *eLife* 12:e84505 (published **11 October 2023**). DOI: [10.7554/eLife.84505](https://doi.org/10.7554/eLife.84505). (mao2023ontherole pages 7-8, mao2023ontherole pages 1-2)
4. **Fivenson EM et al.** “A role for the Gram-negative outer membrane in bacterial shape determination.” *PNAS* 120:e2301987120 (published **22 August 2023**). DOI: [10.1073/pnas.2301987120](https://doi.org/10.1073/pnas.2301987120). (fivenson2023arolefor pages 2-3, fivenson2023arolefor pages 1-2)
5. **Harris LK, Theriot JA.** “Surface Area to Volume Ratio: A Natural Variable for Bacterial Morphogenesis.” *Trends in Microbiology* 26:815–832 (**October 2018**). DOI: [10.1016/j.tim.2018.04.008](https://doi.org/10.1016/j.tim.2018.04.008). (harris2018surfaceareato pages 9-12)
6. **Shi H et al.** “How to Build a Bacterial Cell: MreB as the Foreman of *E. coli* Construction.” *Cell* 172:1294–1305 (**March 2018**). DOI: [10.1016/j.cell.2018.02.050](https://doi.org/10.1016/j.cell.2018.02.050). (shi2018howtobuild pages 7-9)
7. **Hussain S et al.** “MreB filaments align along greatest principal membrane curvature to orient cell wall synthesis.” *eLife* 7:e32471 (**February 2018**). DOI: [10.7554/eLife.32471](https://doi.org/10.7554/eLife.32471).
8. **Shi H et al.** “Deep Phenotypic Mapping of Bacterial Cytoskeletal Mutants Reveals Physiological Robustness to Cell Size.” *Current Biology* 27:3419–3429.e4 (**November 2017**). DOI: [10.1016/j.cub.2017.09.065](https://doi.org/10.1016/j.cub.2017.09.065). (shi2017deepphenotypicmapping pages 9-10, shi2017deepphenotypicmapping pages 1-3, shi2017deepphenotypicmapping pages 3-3)
9. **Morgenstein RM et al.** “RodZ links MreB to cell wall synthesis to mediate MreB rotation and robust morphogenesis.” *PNAS* 112:12510–12515 (**September 2015**). DOI: [10.1073/pnas.1509610112](https://doi.org/10.1073/pnas.1509610112). (morgenstein2015rodzlinksmreb pages 6-6)
10. **Giovannoni SJ, Thrash JC, Temperton B.** “Implications of streamlining theory for microbial ecology.” *ISME Journal* 8:1553–1565 (published online **17 April 2014**). DOI: [10.1038/ismej.2014.60](https://doi.org/10.1038/ismej.2014.60). (giovannoni2014implicationsofstreamlining pages 1-2, giovannoni2014implicationsofstreamlining pages 2-3, giovannoni2014implicationsofstreamlining pages 3-4)

## Curation conclusion

The most defensible YAML expansion is a **general width-control subgraph** centered on MreB/RodZ/MreC/PBP2/RodA and oriented peptidoglycan synthesis, linked only provisionally to `METPO:1000887`. A separate ecological branch can capture nutrient limitation, streamlining, surface-area-to-volume advantage, and ultrasmall environmental cells, but these edges should be explicitly marked associational or inferred. Direct threshold-specific evidence—preferably genetic or environmental perturbation with calibrated width measurements before and after treatment—is the principal missing evidence.

References

1. (belykh2024ultramicrobacteriaandfilterable pages 1-2): O.I. Belykh, A.Yu. Krasnopeev, S.A. Potapov, D.I. Gutnik, E.G. Sorokovikova, T.V. Butina, and I.V. Tikhonova. Ultramicrobacteria and filterable bacteria in the plankton of lake baikal. Limnology and Freshwater Biology, pages 795-820, Jan 2024. URL: https://doi.org/10.31951/2658-3518-2024-a-4-795, doi:10.31951/2658-3518-2024-a-4-795. This article has 2 citations.

2. (giovannoni2014implicationsofstreamlining pages 1-2): Stephen J Giovannoni, J Cameron Thrash, and Ben Temperton. Implications of streamlining theory for microbial ecology. The ISME Journal, 8:1553-1565, Apr 2014. URL: https://doi.org/10.1038/ismej.2014.60, doi:10.1038/ismej.2014.60. This article has 956 citations.

3. (giovannoni2014implicationsofstreamlining pages 2-3): Stephen J Giovannoni, J Cameron Thrash, and Ben Temperton. Implications of streamlining theory for microbial ecology. The ISME Journal, 8:1553-1565, Apr 2014. URL: https://doi.org/10.1038/ismej.2014.60, doi:10.1038/ismej.2014.60. This article has 956 citations.

4. (shi2017deepphenotypicmapping pages 9-10): Handuo Shi, Alexandre Colavin, Marty Bigos, Carolina Tropini, Russell D. Monds, and Kerwyn Casey Huang. Deep phenotypic mapping of bacterial cytoskeletal mutants reveals physiological robustness to cell size. Current Biology, 27:3419-3429.e4, Nov 2017. URL: https://doi.org/10.1016/j.cub.2017.09.065, doi:10.1016/j.cub.2017.09.065. This article has 83 citations and is from a highest quality peer-reviewed journal.

5. (morgenstein2015rodzlinksmreb pages 6-6): Randy M. Morgenstein, Benjamin P. Bratton, Jeffrey P. Nguyen, Nikolay Ouzounov, Joshua W. Shaevitz, and Zemer Gitai. Rodz links mreb to cell wall synthesis to mediate mreb rotation and robust morphogenesis. Proceedings of the National Academy of Sciences, 112:12510-12515, Sep 2015. URL: https://doi.org/10.1073/pnas.1509610112, doi:10.1073/pnas.1509610112. This article has 162 citations and is from a highest quality peer-reviewed journal.

6. (fivenson2023arolefor pages 1-2): Elayne M. Fivenson, Patricia D. A. Rohs, Andrea Vettiger, Marios F. Sardis, Grasiela Torres, Alison Forchoh, and Thomas G. Bernhardt. A role for the gram-negative outer membrane in bacterial shape determination. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2301987120, doi:10.1073/pnas.2301987120. This article has 98 citations and is from a highest quality peer-reviewed journal.

7. (mao2023ontherole pages 1-2): Wei Mao, Lars D Renner, Charlène Cornilleau, Ines Li de la Sierra-Gallay, Sana Afensiss, Sarah Benlamara, Yoan Ah-Seng, Herman Van Tilbeurgh, Sylvie Nessler, Aurélie Bertin, Arnaud Chastanet, and Rut Carballido-Lopez. On the role of nucleotides and lipids in the polymerization of the actin homolog mreb from a gram-positive bacterium. eLife, Oct 2023. URL: https://doi.org/10.7554/elife.84505, doi:10.7554/elife.84505. This article has 12 citations and is from a domain leading peer-reviewed journal.

8. (harris2018surfaceareato pages 9-12): Leigh K. Harris and Julie A. Theriot. Surface area to volume ratio: a natural variable for bacterial morphogenesis. Trends in microbiology, 26 10:815-832, Oct 2018. URL: https://doi.org/10.1016/j.tim.2018.04.008, doi:10.1016/j.tim.2018.04.008. This article has 184 citations and is from a domain leading peer-reviewed journal.

9. (mao2023ontherole pages 7-8): Wei Mao, Lars D Renner, Charlène Cornilleau, Ines Li de la Sierra-Gallay, Sana Afensiss, Sarah Benlamara, Yoan Ah-Seng, Herman Van Tilbeurgh, Sylvie Nessler, Aurélie Bertin, Arnaud Chastanet, and Rut Carballido-Lopez. On the role of nucleotides and lipids in the polymerization of the actin homolog mreb from a gram-positive bacterium. eLife, Oct 2023. URL: https://doi.org/10.7554/elife.84505, doi:10.7554/elife.84505. This article has 12 citations and is from a domain leading peer-reviewed journal.

10. (fivenson2023arolefor pages 2-3): Elayne M. Fivenson, Patricia D. A. Rohs, Andrea Vettiger, Marios F. Sardis, Grasiela Torres, Alison Forchoh, and Thomas G. Bernhardt. A role for the gram-negative outer membrane in bacterial shape determination. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2301987120, doi:10.1073/pnas.2301987120. This article has 98 citations and is from a highest quality peer-reviewed journal.

11. (zhu2024shapingofmicrobial pages 1-2): Manlu Zhu and Xiongfeng Dai. Shaping of microbial phenotypes by trade-offs. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48591-9, doi:10.1038/s41467-024-48591-9. This article has 121 citations and is from a highest quality peer-reviewed journal.

12. (giovannoni2014implicationsofstreamlining pages 3-4): Stephen J Giovannoni, J Cameron Thrash, and Ben Temperton. Implications of streamlining theory for microbial ecology. The ISME Journal, 8:1553-1565, Apr 2014. URL: https://doi.org/10.1038/ismej.2014.60, doi:10.1038/ismej.2014.60. This article has 956 citations.

13. (shi2017deepphenotypicmapping pages 1-3): Handuo Shi, Alexandre Colavin, Marty Bigos, Carolina Tropini, Russell D. Monds, and Kerwyn Casey Huang. Deep phenotypic mapping of bacterial cytoskeletal mutants reveals physiological robustness to cell size. Current Biology, 27:3419-3429.e4, Nov 2017. URL: https://doi.org/10.1016/j.cub.2017.09.065, doi:10.1016/j.cub.2017.09.065. This article has 83 citations and is from a highest quality peer-reviewed journal.

14. (shi2017deepphenotypicmapping pages 3-3): Handuo Shi, Alexandre Colavin, Marty Bigos, Carolina Tropini, Russell D. Monds, and Kerwyn Casey Huang. Deep phenotypic mapping of bacterial cytoskeletal mutants reveals physiological robustness to cell size. Current Biology, 27:3419-3429.e4, Nov 2017. URL: https://doi.org/10.1016/j.cub.2017.09.065, doi:10.1016/j.cub.2017.09.065. This article has 83 citations and is from a highest quality peer-reviewed journal.

15. (shi2018howtobuild pages 7-9): Handuo Shi, Benjamin P. Bratton, Zemer Gitai, and Kerwyn Casey Huang. How to build a bacterial cell: mreb as the foreman of e. coli construction. Cell, 172:1294-1305, Mar 2018. URL: https://doi.org/10.1016/j.cell.2018.02.050, doi:10.1016/j.cell.2018.02.050. This article has 225 citations and is from a highest quality peer-reviewed journal.