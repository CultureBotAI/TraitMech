---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:33:35.938917'
end_time: '2026-08-04T07:40:24.738519'
duration_seconds: 408.8
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell length large
  trait_identifier: METPO:1000886
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_length_large
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-length phenotype in which the longer cell dimension exceeds approximately
    3 micrometers.
  parent_traits: METPO:1000881
  synonyms: L_>3
  evidence_summary: 'DOI:10.1126/science.aaa1313: cell size scales with growth rate
    (Growth-rate-dependent size law supports large cell length under fast-growth or
    division-delayed regimes.) | DOI:10.1038/nrmicro2671: directs cell division (FtsZ-divisome
    review supports division-site timing as a control point governing whether cells
    reach larger lengths before constriction.)'
  causal_graph_summary: 'cell_length_large_division_delay: 10 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length large
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000886
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension exceeds approximately 3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_>3
- **Existing evidence:** DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports large cell length under fast-growth or division-delayed regimes.) | DOI:10.1038/nrmicro2671: directs cell division (FtsZ-divisome review supports division-site timing as a control point governing whether cells reach larger lengths before constriction.)
- **Existing causal graph summary:** cell_length_large_division_delay: 10 nodes, 6 edges

## Research Objective

Research the microbial trait **cell length large** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_large.yaml`.

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
- **Trait label:** cell length large
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000886
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension exceeds approximately 3 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_>3
- **Existing evidence:** DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports large cell length under fast-growth or division-delayed regimes.) | DOI:10.1038/nrmicro2671: directs cell division (FtsZ-divisome review supports division-site timing as a control point governing whether cells reach larger lengths before constriction.)
- **Existing causal graph summary:** cell_length_large_division_delay: 10 nodes, 6 edges

## Research Objective

Research the microbial trait **cell length large** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_large.yaml`.

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


# Curation-focused research report: **cell length large**

## 1. Scope and current interpretation

**Target trait:** “cell length large”  
**Identifier:** `METPO:1000886`  
**Category:** morphology; class; reviewed  
**Operational definition:** a cell-length phenotype in which the longer cellular dimension exceeds approximately **3 µm**.

This is best represented as an **assay-observed morphology**, not as a mechanism. A cell can cross the threshold through at least two broad routes: (i) growth-associated increases in cellular dimensions under balanced growth, or (ii) continued elongation while septation or daughter-cell separation is delayed. The strongest graph-ready literature retrieved here supports the second route—FtsZ/divisome-dependent division delay.

### Boundaries

* **Not equivalent to cell volume or biomass.** “Large cell size” measurements based on volume, area, dry mass, or optical scattering do not establish a >3-µm long axis.
* **Not equivalent to increased width.** Perturbing MreB or envelope synthesis can primarily change width or shape.
* **Not automatically filamentation.** A 3–5-µm rod meets this trait definition, whereas “filamentous” often denotes much longer, incompletely septated cells. Filamentation can therefore be a severe subclass or manifestation, but should not be used as an exact synonym.
* **Not a chain unless septa are absent.** Chains of short, fully divided cells may have a long aggregate axis but do not necessarily contain individually long cells.
* **Natural filamentous taxa require separate treatment.** Filamentous reproductive programs, such as tip extension followed by simultaneous multiple fission, are normal life-cycle morphologies rather than necessarily division-defect phenotypes. A 2024 PNAS study demonstrates such a specialized program and cautions against universalizing binary-fission mechanisms (chimileski2024tipextensionand pages 5-7).
* **Threshold caution.** One quantitative physiology treatment places a critical *E. coli* length near 3.4 µm in a specific model, but this should not be interpreted as a universal biological cutoff across species or assays (jun2018fundamentalprinciplesin pages 27-28).

## 2. Mechanistic synthesis

The most defensible core path is:

**reduced or mistimed FtsZ/divisome activity → delayed constriction/septation → continued longitudinal growth → `METPO:1000886`.**

FtsZ abundance is rate-limiting for division timing in *Escherichia coli*. Recent in-vivo measurements support a model in which FtsZ protofilaments promote the FtsA conformational transition and septal peptidoglycan synthesis required for constriction; excess wild-type FtsA instead inhibits division (mannik2024determiningtheratelimiting pages 8-9). This updates a simplistic “FtsN alone triggers constriction” model: the 2024 authors found that ordinary FtsN and FtsA abundance was not rate-limiting, whereas FtsZ abundance was, although high overexpression of FtsN accelerated and FtsA inhibited division (mannik2024determiningtheratelimiting pages 8-9).

The strongest direct long-cell evidence is *Acinetobacter baumannii* Aeg1 depletion. Without Aeg1 induction, **>96%** of cells were elongated to **5–10+ µm**, whereas with Aeg1 expression **>95%** remained under 5 µm; more than 300 cells were scored per sample across three experiments. FtsA, FtsB, and FtsW activation/suppressor variants bypassed Aeg1 dependence, supporting placement of Aeg1 upstream of FtsN recruitment and divisome activation (chu2024auniquecell pages 1-2, chu2024auniquecell pages 4-5).

| Perturbation / source node | Causal mechanism / intermediate | Phenotype outcome | Organism | Evidence strength / caveat |
|---|---|---|---|---|
| Increased FtsZ number / polymerization competence | FtsZ protofilaments are rate-limiting for onset of constriction; higher FtsZ supports the switch into septal peptidoglycan synthesis and division initiation (mannik2024determiningtheratelimiting pages 8-9) | Faster constriction onset is expected to limit excess length accumulation before division; converse inference is that insufficient FtsZ activity can contribute to longer cells | *Escherichia coli* | Strong recent primary evidence for rate-limiting role in constriction timing, but this is an indirect support edge for “large cell length” rather than a direct long-cell perturbation assay (mannik2024determiningtheratelimiting pages 8-9) |
| Excess FtsA | Excess FtsA inhibits division; study supports a model in which FtsZ protofilament bundling drives FtsA conformational changes needed for constriction, while too much FtsA is inhibitory (mannik2024determiningtheratelimiting pages 8-9) | Division delay / later constriction, consistent with increased cell length before septation | *Escherichia coli* | Strong recent primary evidence for inhibitory effect of FtsA overexpression on division timing; phenotype is mechanistically relevant but not reported here as a simple “>3 µm” thresholded trait (mannik2024determiningtheratelimiting pages 8-9) |
| Aeg1 depletion | Loss of Aeg1 impairs divisome assembly through an FtsN-linked pathway; suppressor mutations in FtsA/FtsB/FtsW bypass the requirement, placing Aeg1 upstream of division activation (chu2024auniquecell pages 1-2, chu2024auniquecell pages 4-5) | >96% of cells elongated to 5–10+ µm without induction, versus >95% short (<5 µm) when Aeg1 is expressed (chu2024auniquecell pages 4-5) | *Acinetobacter baumannii* | Strong 2024 primary evidence with quantitative morphology; taxon-specific divisome component, so curate as species-linked rather than universal (chu2024auniquecell pages 1-2, chu2024auniquecell pages 4-5) |
| QueE overexpression | QueE co-localizes with FtsZ at the septal site and blocks septation in an SOS-independent manner (adeleye2024queuosinebiosyntheticenzyme pages 1-5) | Long heterogeneous filaments ranging from a few microns to hundreds of microns (adeleye2024queuosinebiosyntheticenzyme pages 1-5) | *Escherichia coli*; function also seen in some Enterobacteriaceae orthologs | Moderate evidence because mechanism is direct but source is a 2024 bioRxiv preprint; likely valuable as an uncertain edge and not yet a high-confidence universal mechanism (adeleye2024queuosinebiosyntheticenzyme pages 1-5) |
| DNA damage / SOS / SulA | DNA damage activates SOS; SulA inhibits FtsZ polymerization / Z-ring assembly, coupling genome damage to division arrest (jun2018fundamentalprinciplesin pages 27-28) | Division inhibition causes elongation / filamentation rather than timely septation | Primarily *Escherichia coli* model; broadly influential concept across bacteria | Strong foundational evidence summarized in authoritative review, but this context is review-level and not a new 2023–2024 primary measurement; curate as well-established but review-backed here (jun2018fundamentalprinciplesin pages 27-28) |
| MinC | MinC negatively regulates FtsZ assembly and destabilizes/prevents Z-ring formation (jun2018fundamentalprinciplesin pages 27-28) | Inhibition of septation is consistent with elongated cells when division is misregulated | Rod-shaped bacteria including *E. coli* and *Bacillus subtilis* | Strong mechanistic support from established division biology, but the provided context is mostly review/background and not a direct quantitative long-cell assay for METPO:1000886 (jun2018fundamentalprinciplesin pages 27-28) |


*Table: This table summarizes the strongest source-backed mechanistic paths that can support curation of METPO:1000886, emphasizing division timing and FtsZ-centered regulation. It highlights which claims are strong enough for curation now and which should remain uncertain because they are review-derived, indirect, taxon-specific, or preprint-only.*

## 3. Candidate nodes grouped by type

### Trait and morphology nodes

| Node | Suggested grounding | Curation note |
|---|---|---|
| cell length large | `METPO:1000886` | Target node; quote identifier verbatim. |
| parent morphology | `METPO:1000881` | Supplied parent; retain relationship from source ontology. |
| filamentous-cell phenotype | Label only pending verified ontology mapping | Use as a more severe manifestation, not a synonym. |
| increased cell width | Label only | Exclude from this graph unless an experiment independently establishes increased length. |

### Proteins and complexes

| Node | Type and role | Grounding recommendation |
|---|---|---|
| FtsZ | Tubulin-family GTPase; Z-ring scaffold and organizer of septal synthesis | Use a species-specific UniProt CURIE when taxon is known; molecular function may use `GO:0005525` (GTP binding), but verify annotation before YAML insertion. |
| Z-ring | Supramolecular division structure | `GO:0000940` is a candidate; verify against the current GO release. |
| divisome | Cell-division complex | `GO:0032153` is a candidate; verify before curation. |
| FtsA | Membrane-associated FtsZ partner and late-divisome hub | Species-specific UniProt preferred. |
| FtsN | Late divisome protein/activation factor in Gram-negative models | Species-specific UniProt; not universal. |
| FtsB–FtsQ–FtsL complex | Divisome regulatory module | Individual species-specific UniProt entries; label complex if no suitable stable complex CURIE is confirmed. |
| FtsW–FtsI | Septal peptidoglycan synthase module | Species-specific UniProt; use Rhea/EC only after confirming the exact catalytic reaction and protein. |
| Aeg1 | *A. baumannii* divisome component upstream of FtsN-linked activation | Species-specific protein identifier required; **taxon-specific**. |
| SulA | SOS-induced FtsZ inhibitor in *E. coli* | Species-specific UniProt. |
| MinC/MinD | Spatial inhibitor and membrane-associated regulator of FtsZ assembly | Species-specific UniProt; effects depend on localization and dosage. |
| QueE | Queuosine-biosynthesis enzyme with proposed moonlighting division-regulator activity | Species-specific UniProt; division role remains **preprint-supported**. |
| EzrA, GpsB, YtxG, YrrS | Candidate division/envelope regulators from *B. subtilis* CRISPRi genetics | Retain as provisional species-specific candidates, not universal large-length causes. |

### Processes and localizations

| Node | Suggested grounding/status |
|---|---|
| bacterial-type cell division | GO term candidate; verify current exact CURIE. |
| FtsZ polymerization / protofilament assembly | Label plus appropriate GO term after validation. |
| Z-ring assembly | GO process candidate; verify. |
| onset of constriction | Label-only process is acceptable. |
| septal peptidoglycan synthesis | GO process candidate; verify exact term. |
| septation / cytokinesis | GO process candidate; distinguish septum synthesis from physical daughter separation. |
| midcell / division site | GO cellular-component candidate; verify. |
| cytoplasmic membrane | `GO:0005886` may be used where appropriate. |
| SOS response to DNA damage | GO process candidate; verify exact bacterial annotation. |

### Environmental and experimental factors

| Node | Role | Grounding/status |
|---|---|---|
| DNA damage | Activates SOS and division arrest | Use an appropriate stress/exposure ontology term after verification. |
| antimicrobial-peptide stress | Proposed PhoQ/PhoP–QueE context | ENVO/CHEBI depends on the specific peptide; broad label otherwise. |
| nutrient-rich/fast-growth condition | May alter cellular size under balanced growth | Environmental/assay label; do not assert length >3 µm without direct length data. |
| CRISPR interference | Experimental knockdown | `EFO:0005092` is a candidate mapping for CRISPR interference; verify current ontology. |
| gene depletion/overexpression | Experimental perturbation | Represent as intervention nodes or edge qualifiers rather than constitutive biology. |

## 4. Candidate causal edges

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| increased FtsZ abundance | promotes | onset of constriction | Männik et al. 2024: FtsZ numbers were “rate-limiting for cell divisions”; the proposed mechanism is FtsZ-protofilament-driven activation of FtsA and septal synthesis (mannik2024determiningtheratelimiting pages 8-9). | **Strong**, *E. coli*. Positive division edge; do not translate directly to large length without an intermediate inverse relationship. |
| reduced FtsZ abundance/activity | delays | onset of constriction | Converse of the directly tested rate-limiting relationship (mannik2024determiningtheratelimiting pages 8-9). | **Inferred/uncertain** as phrased; curate only if inverse perturbation data are attached. |
| excess FtsA | inhibits | cell division | High FtsA abundance inhibited divisions, whereas FtsZ protofilaments were implicated in the productive conformational switch (mannik2024determiningtheratelimiting pages 8-9). | **Strong but dosage-specific**; ordinary FtsA function should not be labeled inhibitory. |
| division delay | promotes | cell length large | Continued growth without timely septation is the mechanistic bridge used across elongation experiments (mannik2024determiningtheratelimiting pages 8-9, chu2024auniquecell pages 4-5). | Strong conceptual edge, but ideally attach experiment-specific growth and timing evidence. |
| Aeg1 | promotes | FtsN-linked divisome assembly | Aeg1 interacts with division proteins and is proposed to recruit FtsN; FtsA/FtsB/FtsW suppressors bypass Aeg1 loss (chu2024auniquecell pages 1-2, chu2024auniquecell pages 4-5). | **Strong, taxon-specific** to *A. baumannii*. |
| Aeg1 depletion | causes | cell length large | “>96%” of depleted cells were elongated to “5–10+ µm,” versus >95% under 5 µm with Aeg1 expression (chu2024auniquecell pages 4-5). | **Highest-priority direct edge**; quantitative and threshold-compatible. |
| QueE overexpression | inhibits | septation | QueE co-localized with FtsZ at septa and blocked division independently of SOS (adeleye2024queuosinebiosyntheticenzyme pages 1-5). | **Uncertain/preprint**, *E. coli*. Moonlighting mechanism should not be merged with canonical queuosine biosynthesis. |
| QueE overexpression | causes | filamentous-cell phenotype | Reported heterogeneous filaments from a few micrometers to hundreds of micrometers (adeleye2024queuosinebiosyntheticenzyme pages 1-5). | Direct phenotype but preprint; species/ortholog specificity is substantial. |
| DNA damage | activates | SOS response | Authoritative physiology review summarizes the established damage-response pathway (jun2018fundamentalprinciplesin pages 27-28). | Established but review-backed in this evidence set. |
| SOS response | induces | SulA | SulA is described as the DNA-damage-responsive division regulator (jun2018fundamentalprinciplesin pages 27-28). | Strong in *E. coli*; homologous systems differ across taxa. |
| SulA | inhibits | FtsZ polymerization/Z-ring assembly | Review explicitly identifies SulA as an inhibitor of FtsZ polymerization (jun2018fundamentalprinciplesin pages 27-28). | Strong foundational mechanism; attach original primary DOI in production curation if required. |
| FtsZ inhibition | delays | septation | FtsZ is central to division and septal synthesis; division inhibitors act by preventing productive Z-ring function (mannik2024determiningtheratelimiting pages 8-9, jun2018fundamentalprinciplesin pages 27-28). | Strong general mechanism for many bacteria, not all microbes. |
| MinC | inhibits | FtsZ assembly | MinC is identified as a negative regulator of FtsZ assembly associated with MinD at the membrane (jun2018fundamentalprinciplesin pages 27-28). | Strong spatial-control mechanism; **overexpression or mislocalization**, not normal MinC activity, is the relevant route to global division arrest. |
| gpsB deletion or ytxG deletion | increases | cell length | The 2024 *B. subtilis* preprint reports median lengths approximately **19%** and **37%** longer, respectively, in the search record; CRISPRi figures quantify elongation backgrounds (koo2024comprehensivedoublemutantanalysis pages 46-47, koo2024comprehensivedoublemutantanalysis pages 32-35). | **Do not yet curate as definitive**: preprint, incomplete numerical extraction, and possible CRISPRi polar effects. |

## 5. Latest research and applications

### Recent mechanistic developments, 2023–2024

1. **Division initiation is quantitatively FtsZ-limited.** The 2024 *Nature Communications* study argues that FtsZ protofilaments, rather than ordinary FtsN abundance, are rate-limiting for the onset of constriction in *E. coli*. This supports a graph in which FtsZ assembly controls the transition into active septal synthesis (mannik2024determiningtheratelimiting pages 8-9).
2. **A new taxon-specific divisome component links directly to long cells.** Aeg1 depletion in *A. baumannii* generated a penetrant 5–10+ µm phenotype and was bypassed by activation variants in downstream divisome proteins (chu2024auniquecell pages 1-2, chu2024auniquecell pages 4-5).
3. **Metabolic enzymes may moonlight in morphology control.** QueE overexpression reportedly blocks septation through FtsZ-associated localization, but this remains a preprint claim and was conserved only among some close enterobacterial orthologs (adeleye2024queuosinebiosyntheticenzyme pages 1-5).
4. **High-throughput combinatorial genetics is exposing division-envelope interactions.** Double-CRISPRi in *B. subtilis* identified elongation phenotypes and genetic interactions involving EzrA, GpsB, YtxG, YrrS and other envelope genes, but polar effects and preprint status limit immediate graph confidence (koo2024comprehensivedoublemutantanalysis pages 46-47, koo2024comprehensivedoublemutantanalysis pages 32-35).
5. **Natural filamentation is mechanistically diverse.** Tip growth and simultaneous multiple fission in a filamentous oral bacterium illustrate that long cells can be a regulated developmental state rather than failed binary fission (chimileski2024tipextensionand pages 5-7).

### Real-world and experimental applications

* **Antibacterial discovery:** FtsZ, FtsA/FtsN-linked activation and septal synthases are attractive intervention points because blocking division produces elongation/filamentation before loss of proliferation. Morphological profiling can therefore serve as a mechanism-of-action readout.
* **Pathogenesis:** Uropathogenic and other bacteria can filament during host-associated stress. However, host-induced filamentation should be curated with the specific organism, host compartment, and trigger rather than treated as a universal large-length program.
* **Synthetic biology:** Programmable repression of division genes can deliberately control filamentation and cellular morphology. Such edges are intervention-specific and should carry CRISPRi/induction qualifiers.
* **Bioprocessing:** Enlarged or filamentous production strains can alter product accumulation, settling, oxygen transfer and downstream recovery. These are applications of morphology engineering, not evidence that large length intrinsically improves production.

## 6. Recommended graph architecture

A conservative extension of `cell_length_large_division_delay` should prioritize two modules:

**Core conserved module**

`FtsZ polymerization` → promotes → `Z-ring/divisome activation`  
`Z-ring/divisome activation` → promotes → `septal peptidoglycan synthesis`  
`septal peptidoglycan synthesis` → promotes → `constriction/septation`  
`delayed constriction/septation` → promotes → `METPO:1000886`

**Regulatory/perturbation branches**

`DNA damage` → activates → `SOS response` → induces → `SulA` → inhibits → `FtsZ polymerization`  
`excess/mislocalized MinC` → inhibits → `FtsZ assembly`  
`Aeg1 depletion` → impairs → `FtsN-linked divisome activation` → delays → `septation`  
`QueE overexpression` → inhibits → `septation` (**uncertain; preprint**)  
`excess FtsA` → inhibits → `division onset` (**dosage-specific**)

## 7. Warnings: claims not ready for TraitMech

1. **Do not encode “fast growth causes cell length >3 µm” as universal.** Nutrient growth laws frequently concern volume or average size, and the retrieved evidence does not establish the thresholded long-axis phenotype across taxa.
2. **Do not encode ordinary FtsA or MinC activity as causing large length.** Only excess FtsA is inhibitory in the cited experiment; normally localized MinC prevents polar division rather than globally blocking cytokinesis (mannik2024determiningtheratelimiting pages 8-9, jun2018fundamentalprinciplesin pages 27-28).
3. **Do not universalize Aeg1.** It is presently a species-linked *A. baumannii* mechanism (chu2024auniquecell pages 1-2, chu2024auniquecell pages 4-5).
4. **Keep QueE edges uncertain.** The division-regulator role is preprint-supported, overexpression-dependent, and absent from more distant orthologs (adeleye2024queuosinebiosyntheticenzyme pages 1-5).
5. **Do not yet curate GpsB/YtxG/YrrS as direct causes without checking the final article and figures.** Available evidence is preprint-level and includes CRISPRi polar-effect concerns (koo2024comprehensivedoublemutantanalysis pages 46-47, koo2024comprehensivedoublemutantanalysis pages 32-35).
6. **Do not equate filaments, hyphae and chains.** Natural filamentous growth and multiple fission require separate developmental graphs (chimileski2024tipextensionand pages 5-7).
7. **Validate every ontology CURIE before committing YAML.** Species-specific proteins should generally use UniProt accessions; no accession should be inferred solely from a gene name.

## 8. DOI-first bibliography

* Männik J, Kar P, Amarasinghe CI, Amir A, Männik J. **Determining the rate-limiting processes for cell division in *Escherichia coli*.** *Nature Communications*. Published November 2024. DOI: [10.1038/s41467-024-54242-w](https://doi.org/10.1038/s41467-024-54242-w) (mannik2024determiningtheratelimiting pages 8-9).
* Chu X, Wang L, Zhu Y, et al. **A unique cell division protein critical for the assembly of the bacterial divisome.** *eLife*. Published October 2024. DOI/version: [10.7554/eLife.87922.4](https://doi.org/10.7554/elife.87922.4) (chu2024auniquecell pages 1-2, chu2024auniquecell pages 4-5).
* Adeleye SA, Yadavalli SS. **Queuosine biosynthetic enzyme, QueE moonlights as a cell division regulator.** *bioRxiv*. Updated November 2024. DOI: [10.1101/2023.10.31.565030](https://doi.org/10.1101/2023.10.31.565030) (adeleye2024queuosinebiosyntheticenzyme pages 1-5).
* Koo B-M, Todor H, Sun J, et al. **Comprehensive double-mutant analysis of the *Bacillus subtilis* envelope using double-CRISPRi.** *bioRxiv*. Published August 2024. DOI: [10.1101/2024.08.14.608006](https://doi.org/10.1101/2024.08.14.608006) (koo2024comprehensivedoublemutantanalysis pages 46-47, koo2024comprehensivedoublemutantanalysis pages 32-35).
* Chimileski S, Borisy GG, Dewhirst FE, Mark Welch JL. **Tip extension and simultaneous multiple fission in a filamentous bacterium.** *PNAS*. Published September 2024. DOI: [10.1073/pnas.2408654121](https://doi.org/10.1073/pnas.2408654121) (chimileski2024tipextensionand pages 5-7).
* Jun S, Si F, Pugatch R, Scott M. **Fundamental principles in bacterial physiology—history, recent progress, and the future with focus on cell size control: a review.** *Reports on Progress in Physics*. Published February 2018. DOI: [10.1088/1361-6633/aaa628](https://doi.org/10.1088/1361-6633/aaa628) (jun2018fundamentalprinciplesin pages 27-28).

The best immediate YAML addition is therefore the quantitative, taxon-qualified branch **Aeg1 depletion → impaired divisome activation → delayed septation → `METPO:1000886`**, while the FtsZ-centered core should remain the conserved mechanistic backbone. QueE and the *B. subtilis* CRISPRi candidates should enter only as explicitly uncertain evidence records.

References

1. (chimileski2024tipextensionand pages 5-7): Scott Chimileski, Gary G. Borisy, Floyd E. Dewhirst, and Jessica L. Mark Welch. Tip extension and simultaneous multiple fission in a filamentous bacterium. Proceedings of the National Academy of Sciences of the United States of America, Sep 2024. URL: https://doi.org/10.1073/pnas.2408654121, doi:10.1073/pnas.2408654121. This article has 12 citations and is from a highest quality peer-reviewed journal.

2. (jun2018fundamentalprinciplesin pages 27-28): Suckjoon Jun, Fangwei Si, Rami Pugatch, and Matthew Scott. Fundamental principles in bacterial physiology—history, recent progress, and the future with focus on cell size control: a review. Reports on Progress in Physics, 81:056601, Feb 2018. URL: https://doi.org/10.1088/1361-6633/aaa628, doi:10.1088/1361-6633/aaa628. This article has 254 citations and is from a highest quality peer-reviewed journal.

3. (mannik2024determiningtheratelimiting pages 8-9): Jaan Männik, Prathitha Kar, Chathuddasie I. Amarasinghe, Ariel Amir, and Jaan Männik. Determining the rate-limiting processes for cell division in escherichia coli. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54242-w, doi:10.1038/s41467-024-54242-w. This article has 11 citations and is from a highest quality peer-reviewed journal.

4. (chu2024auniquecell pages 1-2): Xiao Chu, Lidong Wang, Yiheng Zhu, Zhengshan Feng, Qingtian Guan, Lei Song, and Zhaoqing Luo. A unique cell division protein critical for the assembly of the bacterial divisome. Oct 2024. URL: https://doi.org/10.7554/elife.87922.4, doi:10.7554/elife.87922.4. This article has 4 citations and is from a domain leading peer-reviewed journal.

5. (chu2024auniquecell pages 4-5): Xiao Chu, Lidong Wang, Yiheng Zhu, Zhengshan Feng, Qingtian Guan, Lei Song, and Zhaoqing Luo. A unique cell division protein critical for the assembly of the bacterial divisome. Oct 2024. URL: https://doi.org/10.7554/elife.87922.4, doi:10.7554/elife.87922.4. This article has 4 citations and is from a domain leading peer-reviewed journal.

6. (adeleye2024queuosinebiosyntheticenzyme pages 1-5): Samuel A. Adeleye and Srujana S. Yadavalli. Queuosine biosynthetic enzyme, quee moonlights as a cell division regulator. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2023.10.31.565030, doi:10.1101/2023.10.31.565030. This article has 13 citations.

7. (koo2024comprehensivedoublemutantanalysis pages 46-47): Byoung-Mo Koo, Horia Todor, Jiawei Sun, Jordi van Gestel, John S. Hawkins, Cameron C. Hearne, Amy B. Banta, Kerwyn Casey Huang, Jason M. Peters, and Carol Gross. Comprehensive double-mutant analysis of the bacillus subtilis envelope using double-crispri. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.14.608006, doi:10.1101/2024.08.14.608006. This article has 14 citations.

8. (koo2024comprehensivedoublemutantanalysis pages 32-35): Byoung-Mo Koo, Horia Todor, Jiawei Sun, Jordi van Gestel, John S. Hawkins, Cameron C. Hearne, Amy B. Banta, Kerwyn Casey Huang, Jason M. Peters, and Carol Gross. Comprehensive double-mutant analysis of the bacillus subtilis envelope using double-crispri. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.14.608006, doi:10.1101/2024.08.14.608006. This article has 14 citations.