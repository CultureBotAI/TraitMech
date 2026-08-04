---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:21:50.630963'
end_time: '2026-08-04T10:28:09.748023'
duration_seconds: 379.12
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: tetrad arrangement
  trait_identifier: traitmech:000119
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: tetrad_arrangement
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell arrangement in which cocci divide in two perpendicular planes
    and remain attached as groups of four (tetrads).
  parent_traits: METPO:1000666
  synonyms: tetrad-forming cocci
  evidence_summary: 'DOI:10.1128/MMBR.00001-06:  (Young''s review treats the tetrad
    as a division-plane-determined coccal arrangement.) | DOI:10.1038/ncomms4842:  (Two-plane
    division with incomplete daughter-cell separation yields four-cell tetrads.)'
  causal_graph_summary: 'tetrad_two_plane_division: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** tetrad arrangement
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000119
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell arrangement in which cocci divide in two perpendicular planes and remain attached as groups of four (tetrads).
- **Parent traits:** METPO:1000666
- **Synonyms:** tetrad-forming cocci
- **Existing evidence:** DOI:10.1128/MMBR.00001-06:  (Young's review treats the tetrad as a division-plane-determined coccal arrangement.) | DOI:10.1038/ncomms4842:  (Two-plane division with incomplete daughter-cell separation yields four-cell tetrads.)
- **Existing causal graph summary:** tetrad_two_plane_division: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **tetrad arrangement** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/tetrad_arrangement.yaml`.

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
- **Trait label:** tetrad arrangement
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000119
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell arrangement in which cocci divide in two perpendicular planes and remain attached as groups of four (tetrads).
- **Parent traits:** METPO:1000666
- **Synonyms:** tetrad-forming cocci
- **Existing evidence:** DOI:10.1128/MMBR.00001-06:  (Young's review treats the tetrad as a division-plane-determined coccal arrangement.) | DOI:10.1038/ncomms4842:  (Two-plane division with incomplete daughter-cell separation yields four-cell tetrads.)
- **Existing causal graph summary:** tetrad_two_plane_division: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **tetrad arrangement** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/tetrad_arrangement.yaml`.

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


# Curation report: tetrad arrangement

## 1. Scope summary

**Trait:** `traitmech:000119` — **tetrad arrangement**  
**Category:** morphology; **term kind:** class; **mapping:** reviewed  
**Parent supplied by the template:** `METPO:1000666`  
**Operational definition:** four coccoid cells remain physically associated after two successive divisions in mutually perpendicular planes.

The trait is an **observed multicellular arrangement**, not merely spherical cell shape, cytokinesis, or the capacity to divide orthogonally. Its minimal mechanistic interpretation has two jointly necessary components:

1. **Plane program:** successive septa are formed in two orthogonal planes.
2. **Separation program:** daughter-cell separation is sufficiently delayed or incomplete that the four products remain attached and are observed as a tetrad.

In *Deinococcus radiodurans*, 3D imaging directly showed growth in alternate orthogonal planes. One side of the new septum began at the middle of the preceding septum and the other at the opposite peripheral wall, both at 90° to the previous septum. Completed tetrads persisted for about **12 minutes** before splitting into two diads; septal growth occupied approximately **two-thirds of the cell cycle**. These observations provide the clearest retrieved organism-level realization of the trait. (floc’h2019cellmorphologyand pages 9-10)

### Boundary cases

- **Diplococci:** one division followed by retention of two daughters; no demonstrated four-cell product.
- **Chains:** repeated division in parallel planes with incomplete separation, rather than two perpendicular planes. The degree of separation can vary, producing isolated cells, diplococci, or chains without changing the underlying parallel-plane program. (zapun2008thedifferentshapes pages 2-3)
- **Irregular staphylococcal clusters:** *Staphylococcus aureus* divides sequentially in three orthogonal planes, but post-fission movement and lytic separation yield irregular grape-like clusters. This is mechanistically informative but is not equivalent to stable four-cell tetrads. (turner2010peptidoglycanarchitecturecan pages 1-2, zapun2008thedifferentshapes pages 2-3)
- **Sarcina-like packets:** cubical packets of eight or more cells arise from division in three perpendicular planes plus retention; they should not be annotated as tetrads solely because four-cell intermediates can occur.
- **Transient microscopy intermediate:** a four-cell stage should count only if the curation policy includes transient arrangements. In *D. radiodurans*, tetrads are explicitly short-lived, so assay timing and growth phase matter. (floc’h2019cellmorphologyand pages 9-10)
- **Two-plane division without attachment:** this establishes the geometric capacity but not the arrangement phenotype.

## 2. Current mechanistic understanding

The strongest defensible graph is a **process-level graph**, rather than a universal gene-level graph:

`coccoid cell` → `mid-cell divisome/septal PG synthesis` → `first septum` → `orthogonal next-septum placement` → `four daughter compartments` → `delayed septal cleavage` → `tetrad arrangement`

FtsZ-dependent cell-wall synthesis is predominant in many cocci and can account for production of the new daughter hemispheres. In *S. aureus*, FtsZ depletion abolishes septum formation and delocalizes wall synthesis over the cell surface, with cells enlarging up to eightfold before lysis. This strongly supports an edge from FtsZ-dependent septal synthesis to septum formation, but it does **not** by itself prove a tetrad-specific FtsZ mechanism. (zapun2008thedifferentshapes pages 2-3)

A second mechanistic layer concerns geometric memory. In *S. aureus*, atomic-force microscopy identified peptidoglycan “piecrust” structures retained as ribs from previous divisions. Multiple bands were approximately perpendicular, and the authors modeled formation of a new piecrust in the plane of a quarter-rib, followed by splitting and inheritance of a revised rib pattern that specifies the next division. This is an authoritative structural model for orthogonal plane choice, but it remains taxon-specific and the molecular reader of the wall cue is unresolved. (turner2010peptidoglycanarchitecturecan pages 1-2, turner2010peptidoglycanarchitecturecan pages 4-6)

Separation is controlled by septal wall remodeling. Partially separated *S. aureus* sisters showed a Y-shaped split consistent with autolysis not yet extending around the entire septal disc. In *D. radiodurans*, separation was slower and progressive and was described as “most likely” catalyzed by enzymatic wall processing. The latter is an inference, not identification of a specific hydrolase. (floc’h2019cellmorphologyand pages 9-10, turner2010peptidoglycanarchitecturecan pages 4-6)

## 3. Candidate nodes grouped by type

### Trait and cellular structures

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| tetrad arrangement | `traitmech:000119` | Target node; quote identifier verbatim in YAML. |
| coccoid cell morphology | label only pending exact ontology match | Necessary context, not sufficient for tetrads. |
| four-cell tetrad | target trait or label-only intermediate | Avoid duplicating the target unless graph conventions require a phenotype-output node. |
| diad/diplococcus | label only | Precursor and post-separation state in *D. radiodurans*. |
| division septum | `GO:0000917` (division septum assembly) may ground the process; structure itself may need another ontology | Verify whether TraitMech models structure or assembly process. |
| peptidoglycan cell wall | `GO:0009274` | Stable cellular-component candidate. |
| previous septum / S−1 septum | label only | Spatial landmark in *D. radiodurans*. |
| newly growing S0 septum | label only | Current orthogonal septum. |
| inherited peptidoglycan rib/piecrust | label only | *S. aureus*-specific structural candidate. |

### Biological processes and pathways

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| bacterial-type cell division | `GO:0051301` | Broad upstream process. |
| cytokinesis | `GO:0000910` | Broad process; bacterial child term is preferable when applicable. |
| septal peptidoglycan biosynthesis | `GO:0019277` | Strong candidate for localized wall synthesis. |
| peptidoglycan biosynthetic process | `GO:0009252` | Use if septal-specific term is unsuitable. |
| cell-wall organization or biogenesis | `GO:0071555` | Broad remodeling process. |
| alternate orthogonal division-plane selection | label only | Central geometry process; do not force an imprecise GO term. |
| septum closure | label only | Directly observed “closing-door” process in *D. radiodurans*. |
| septal scission/cell separation | label only; consider an exact GO descendant after ontology verification | Distinguish physical separation from septum synthesis. |
| autolysis of septal peptidoglycan | label only pending exact term | Supported in *S. aureus*, not demonstrated as the universal tetrad determinant. |

### Genes, proteins, and complexes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| FtsZ | `UniProt` accession must be species-specific; `GO:0005525` describes GTP binding, not the protein | Strong upstream septation factor; no universal accession should be assigned. |
| Z ring | label only or appropriate GO cellular component after verification | Assembly site for divisome; direct tetrad causality was not established in retrieved papers. |
| divisome | `GO:0032153` | Candidate complex-level node. |
| peptidoglycan synthases/PBPs | species-specific UniProt or EC nodes | Mechanistically relevant but tetrad-specific perturbation evidence was not retrieved. |
| septal autolysin(s) | species-specific label/UniProt | Use only when a particular enzyme is experimentally linked to tetrad retention or release. |
| Atl | species-specific *S. aureus* UniProt after verification | Relevant to division scars/separation, but *S. aureus* clusters are not the target tetrad phenotype. |
| Min system / MinC / MinD | label or species-specific UniProt | Proposed positional machinery; direct tetrad causality remains insufficient here. |
| DivIVA | species-specific UniProt after verification | Plausible orientation regulator in *D. radiodurans*, but the retrieved full text was corrupted; withhold until the peer-reviewed article is checked directly. |

### Chemicals and molecular materials

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| peptidoglycan | `CHEBI:8005` | Verify release/version before use. |
| UDP-MurNAc/UDP-GlcNAc and lipid II | CHEBI/Rhea candidates | Generic PG precursors; no tetrad-specific edge was established. |
| fluorescent D-amino-acid probes/HADA | label only unless assay nodes are modeled | Experimental visualization reagents, not causal trait determinants. |
| fluorescent vancomycin | vancomycin has a CHEBI identifier, but this conjugate should be label-only unless exactly grounded | Assay factor used to localize nascent PG. |

### Taxa and assay context

- *Deinococcus radiodurans*: direct orthogonal-plane and transient-tetrad imaging; use a verified NCBITaxon identifier during implementation.
- *Staphylococcus aureus*: valuable model for orthogonal division, PG structural inheritance, and autolytic separation; not a clean exemplar of stable tetrads.
- *Pediococcus* and other tetrad-forming cocci: phenotype exemplars, but the retrieved evidence did not establish equivalent gene-level mechanisms.
- Microscopy factors: growth phase, image dimensionality, temporal sampling, and separation state should be recorded because they influence whether tetrads are detected.

## 4. Candidate causal edges

The following compact table summarizes the priority edges.

| subject | predicate | object | confidence/scope | DOI |
|---|---|---|---|---|
| coccoid morphology | enables | division-plane-defined multicell arrangements | high; review across cocci; tetrads arise from perpendicular planes (zapun2008thedifferentshapes pages 2-3) | 10.1111/j.1574-6976.2007.00098.x |
| FtsZ-dependent septal peptidoglycan synthesis | produces | septum and new daughter hemispheres | high; cocci/staphylococci morphology mechanism from review and depletion evidence (zapun2008thedifferentshapes pages 2-3) | 10.1111/j.1574-6976.2007.00098.x |
| alternate orthogonal septum formation | produces | four-cell tetrad | high; direct imaging in *Deinococcus radiodurans* (floc’h2019cellmorphologyand pages 9-10) | 10.1038/s41467-019-11725-5 |
| completed S0 septum closure | produces | short-lived tetrad before split into two diads | high; direct timing/phase description in *D. radiodurans* (floc’h2019cellmorphologyand pages 9-10) | 10.1038/s41467-019-11725-5 |
| progressive septal cell-wall processing | separates | tetrad into two diads | medium; *D. radiodurans*; enzymatic processing inferred by authors (floc’h2019cellmorphologyand pages 9-10) | 10.1038/s41467-019-11725-5 |
| inherited peptidoglycan piecrust/ribs | specifies | subsequent orthogonal division plane | medium; *Staphylococcus aureus* taxon-specific structural model (turner2010peptidoglycanarchitecturecan pages 4-6, turner2010peptidoglycanarchitecturecan pages 1-2) | 10.1038/ncomms1025 |
| autolysis | enables | septal scission and daughter-cell separation | high for *S. aureus* separation; mechanism direct/structural, not tetrad-specific (turner2010peptidoglycanarchitecturecan pages 4-6) | 10.1038/ncomms1025 |


*Table: This table compiles compact, evidence-backed causal edges relevant to curating the tetrad arrangement trait (traitmech:000119). It highlights which claims are broadly supported versus taxon-specific or inferred, helping prioritize edges for TraitMech inclusion.*

A more curation-specific evidence table follows. “Snippet” preserves short source wording or a close excerpt from the retrieved text.

| # | Subject — predicate → object | Evidence level | Reference | Supporting snippet | Curation notes |
|---:|---|---|---|---|---|
| 1 | FtsZ-dependent cell-wall synthesis — **causes/enables** → septum and daughter-hemisphere formation | High for coccal septation; indirect for tetrads | DOI: [10.1111/j.1574-6976.2007.00098.x](https://doi.org/10.1111/j.1574-6976.2007.00098.x) | “FtsZ-dependent cell wall synthesis is therefore predominant and determinant for morphogenesis”; FtsZ depletion caused the septum to no longer form. | Curate as an upstream generic edge, not as sufficient for tetrad arrangement. (zapun2008thedifferentshapes pages 2-3) |
| 2 | Alternate orthogonal division planes — **produce** → four-cell tetrad arrangement | High; direct imaging; *D. radiodurans* | DOI: [10.1038/s41467-019-11725-5](https://doi.org/10.1038/s41467-019-11725-5) | Cells “divide in alternate orthogonal planes”; both growing septum sides are “at a 90° angle to the S−1 septum.” | Best core geometry edge. Taxon evidence should be attached. (floc’h2019cellmorphologyand pages 9-10) |
| 3 | Previous S−1 septum — **spatially anchors/orients** → new S0 septum | High observational support; mechanism unresolved | DOI: [10.1038/s41467-019-11725-5](https://doi.org/10.1038/s41467-019-11725-5) | One side starts “precisely from the middle of the S−1 septum,” at 90° to it. | Prefer a spatial predicate; avoid claiming the previous septum molecularly signals the new site. (floc’h2019cellmorphologyand pages 9-10) |
| 4 | Progressive S0 septum closure — **produces** → newly formed tetrad | High; direct temporal morphology | DOI: [10.1038/s41467-019-11725-5](https://doi.org/10.1038/s41467-019-11725-5) | “Once the dividing S0 septum closes… the newly formed tetrads” appear. | Strong process-to-phenotype edge. (floc’h2019cellmorphologyand pages 9-10) |
| 5 | Delayed separation — **maintains** → transient tetrad arrangement | High; direct timing | DOI: [10.1038/s41467-019-11725-5](https://doi.org/10.1038/s41467-019-11725-5) | Tetrads were “short-lived, lasting for a dozen of minutes before splitting into two diads.” | Core retention edge; approximately 12 min under the reported growth conditions. (floc’h2019cellmorphologyand pages 9-10) |
| 6 | Progressive reduction of shared S−1 septum — **causes** → tetrad separation into two diads | High morphological evidence | DOI: [10.1038/s41467-019-11725-5](https://doi.org/10.1038/s41467-019-11725-5) | Increasing wall curvature reduces “the length of the shared S−1 septum, until the two diads eventually separate.” | Use for the reverse transition away from the trait. (floc’h2019cellmorphologyand pages 9-10) |
| 7 | Enzymatic cell-wall processing — **promotes** → separation into diads | Medium/uncertain | DOI: [10.1038/s41467-019-11725-5](https://doi.org/10.1038/s41467-019-11725-5) | Separation was “most likely catalysed by the enzymatic processing of the cell wall.” | Explicit author inference; no enzyme identified. Mark uncertain. (floc’h2019cellmorphologyand pages 9-10) |
| 8 | Inherited PG piecrust/ribs — **specify** → subsequent orthogonal division plane | Medium; structural evidence plus model; *S. aureus* | DOI: [10.1038/ncomms1025](https://doi.org/10.1038/ncomms1025) | “A new piecrust is formed in the plane of the quarter rib… leading to a revised rib pattern that specifies the next round of division.” | Useful comparative edge, but do not generalize to tetrad-forming taxa without direct evidence. (turner2010peptidoglycanarchitecturecan pages 1-2, turner2010peptidoglycanarchitecturecan pages 4-6) |
| 9 | Septal autolysis — **enables** → septal scission/daughter separation | High for *S. aureus*; not tetrad-specific | DOI: [10.1038/ncomms1025](https://doi.org/10.1038/ncomms1025) | A partially split Y configuration indicated “autolysis of the surface had not occurred all along the outside of the septal disc.” | Supports separation machinery, but not a specific tetrad-retention determinant. (turner2010peptidoglycanarchitecturecan pages 4-6) |
| 10 | Extensive lytic septum splitting/post-fission movement — **converts** → geometric packet into irregular cluster | Review-supported; *S. aureus* | DOI: [10.1111/j.1574-6976.2007.00098.x](https://doi.org/10.1111/j.1574-6976.2007.00098.x) | Lytic enzymes “seem to cause a postfissional movement… leading to… irregular clusters.” | Boundary/exclusion edge; useful for distinguishing tetrads from staphylococcal clusters. (zapun2008thedifferentshapes pages 2-3) |

## 5. Recommended minimal TraitMech graph

For a conservative first revision of `data/traits/morphology/tetrad_arrangement.yaml`, retain a small taxon-neutral backbone and attach taxon-specific evidence annotations:

1. `coccoid cell morphology` — **enables** → `division-plane-defined cell arrangement`
2. `FtsZ-dependent septal peptidoglycan synthesis` — **produces** → `division septum`
3. `first division septum` — **precedes** → `second division septum`
4. `second division septum` — **oriented_perpendicular_to** → `first division septum`
5. `two successive perpendicular divisions` — **produces** → `four daughter cells`
6. `delayed/incomplete daughter-cell separation` — **maintains** → `attached four-cell group`
7. `attached four-cell group` — **realizes** → `traitmech:000119`

Edges 2 and 4–7 have the strongest support. Edge 1 is contextual. Edge 3 is temporal rather than mechanistically causal. A separate *D. radiodurans* evidence branch can represent S−1/S0 geometry and transient separation, while the *S. aureus* PG-rib model should remain a comparative, taxon-qualified branch.

## 6. Recent developments and evidence gap

Targeted searches prioritizing 2023–2024 did not retrieve a direct new primary study that resolves the tetrad-specific molecular mechanism. The most informative direct study remains the 2019 3D microscopy analysis of *D. radiodurans*, while the principal geometric-wall model and coccal synthesis framework derive from 2010 and 2008–2013 literature. Consequently, “current understanding” is still dominated by advanced imaging and comparative coccal cell-biology models rather than a universal, experimentally validated tetrad gene module. (turner2010peptidoglycanarchitecturecan pages 1-2, pinho2013howtoget pages 10-11, floc’h2019cellmorphologyand pages 9-10)

The main current applications are therefore:

- **Morphological identification and taxonomy:** distinguishing two-plane tetrads from chains, clusters, and three-plane packets.
- **Automated microscopy/phenotyping:** scoring four-cell topology, septum orientation, and attachment state.
- **Cell-cycle analysis:** *D. radiodurans* provides a tractable system for studying orthogonal septation and nucleoid–division coupling.
- **Causal ontology construction:** separating geometry-generating mechanisms from separation/retention mechanisms prevents over-annotation from appearance alone.
- **Antimicrobial morphology assays:** FtsZ or PG-remodeling perturbations can alter septation and separation, although such effects are not tetrad-specific.

## 7. Claims not yet ready for TraitMech curation

1. **A universal tetrad gene set.** No retrieved source establishes one across *Deinococcus*, *Micrococcus*, *Pediococcus*, and related taxa.
2. **DivIVA → orthogonal plane → tetrad as a high-confidence chain.** A relevant peer-reviewed article exists—Chaudhary et al., *Journal of Bacteriology* (2021), DOI [10.1128/JB.00163-21](https://doi.org/10.1128/JB.00163-21)—but the available full-text retrieval was corrupted and could not be evidence-checked. Do not curate its mutation/rescue claims until the article is read directly.
3. **MinC/MinD as universal tetrad determinants.** Reviews discuss plausible geometry-sensing models, but species differ markedly in division-site systems. (pinho2013howtoget pages 10-11, pinho2013howtoget pages 9-10)
4. **PG ribs as the mechanism in all tetrad-formers.** The evidence is from *S. aureus*, which normally produces irregular clusters and divides in three sequential orthogonal planes. (turner2010peptidoglycanarchitecturecan pages 1-2, turner2010peptidoglycanarchitecturecan pages 4-6)
5. **A named hydrolase controls *D. radiodurans* tetrad lifetime.** Only inferred enzymatic wall processing was reported; the responsible enzyme was not identified. (floc’h2019cellmorphologyand pages 9-10)
6. **Environmental regulation of tetrad formation.** No retrieved study demonstrated a specific nutrient, inhibitor, temperature, oxygen, salinity, or stress condition as a causal tetrad switch.
7. **Stable species-level phenotype from a single image.** Tetrads can be transient and culture-condition dependent; time series or population statistics are preferable.
8. **Unverified ontology identifiers.** Species-specific UniProt, NCBITaxon, Rhea, and exact GO assignments should be checked against current releases before YAML insertion.

## 8. DOI-first bibliography

1. Floc’h K, Lacroix F, Servant P, et al. **Cell morphology and nucleoid dynamics in dividing *Deinococcus radiodurans*.** *Nature Communications.* Published **22 August 2019**. DOI: [10.1038/s41467-019-11725-5](https://doi.org/10.1038/s41467-019-11725-5). Direct 3D microscopy evidence for orthogonal septation, approximately 12-minute tetrad persistence, and progressive separation. (floc’h2019cellmorphologyand pages 9-10)
2. Pinho MG, Kjos M, Veening J-W. **How to get (a)round: mechanisms controlling growth and division of coccoid bacteria.** *Nature Reviews Microbiology.* Published **August 2013**. DOI: [10.1038/nrmicro3088](https://doi.org/10.1038/nrmicro3088). Authoritative review of coccal septation and division-plane positioning. (pinho2013howtoget pages 10-11, pinho2013howtoget pages 9-10)
3. Turner RD, Ratcliffe EC, Wheeler R, et al. **Peptidoglycan architecture can specify division planes in *Staphylococcus aureus*.** *Nature Communications.* Published **22 June 2010**. DOI: [10.1038/ncomms1025](https://doi.org/10.1038/ncomms1025). AFM and fluorescence evidence for inherited PG structures and orthogonal-plane memory. (turner2010peptidoglycanarchitecturecan pages 1-2, turner2010peptidoglycanarchitecturecan pages 4-6)
4. Zapun A, Vernet T, Pinho MG. **The different shapes of cocci.** *FEMS Microbiology Reviews.* Published **March 2008**. DOI: [10.1111/j.1574-6976.2007.00098.x](https://doi.org/10.1111/j.1574-6976.2007.00098.x). Foundational synthesis of coccal morphology, FtsZ-dependent wall synthesis, orthogonal planes, and cell separation. (zapun2008thedifferentshapes pages 2-3)
5. Monahan LG, Liew ATF, Bottomley AL, Harry EJ. **Division site positioning in bacteria: one size does not fit all.** *Frontiers in Microbiology.* Published **7 February 2014**. DOI: [10.3389/fmicb.2014.00019](https://doi.org/10.3389/fmicb.2014.00019). Comparative review emphasizing species-specific division-positioning mechanisms.
6. Chaudhary R, Kota S, Misra HS. **DivIVA regulates its expression and the orientation of new septum growth in *Deinococcus radiodurans*.** *Journal of Bacteriology.* Published **2021**. DOI: [10.1128/JB.00163-21](https://doi.org/10.1128/JB.00163-21). Relevant candidate source requiring direct verification before graph curation.

References

1. (floc’h2019cellmorphologyand pages 9-10): Kevin Floc’h, Françoise Lacroix, Pascale Servant, Yung-Sing Wong, Jean-Philippe Kleman, Dominique Bourgeois, and Joanna Timmins. Cell morphology and nucleoid dynamics in dividing deinococcus radiodurans. Nature Communications, Aug 2019. URL: https://doi.org/10.1038/s41467-019-11725-5, doi:10.1038/s41467-019-11725-5. This article has 59 citations and is from a highest quality peer-reviewed journal.

2. (zapun2008thedifferentshapes pages 2-3): André Zapun, Thierry Vernet, and Mariana G. Pinho. The different shapes of cocci. FEMS microbiology reviews, 32 2:345-60, Mar 2008. URL: https://doi.org/10.1111/j.1574-6976.2007.00098.x, doi:10.1111/j.1574-6976.2007.00098.x. This article has 275 citations and is from a domain leading peer-reviewed journal.

3. (turner2010peptidoglycanarchitecturecan pages 1-2): Robert D. Turner, Emma C. Ratcliffe, Richard Wheeler, Ramin Golestanian, Jamie K. Hobbs, and Simon J. Foster. Peptidoglycan architecture can specify division planes in staphylococcus aureus. Nature communications, 1:26, Jun 2010. URL: https://doi.org/10.1038/ncomms1025, doi:10.1038/ncomms1025. This article has 160 citations and is from a highest quality peer-reviewed journal.

4. (turner2010peptidoglycanarchitecturecan pages 4-6): Robert D. Turner, Emma C. Ratcliffe, Richard Wheeler, Ramin Golestanian, Jamie K. Hobbs, and Simon J. Foster. Peptidoglycan architecture can specify division planes in staphylococcus aureus. Nature communications, 1:26, Jun 2010. URL: https://doi.org/10.1038/ncomms1025, doi:10.1038/ncomms1025. This article has 160 citations and is from a highest quality peer-reviewed journal.

5. (pinho2013howtoget pages 10-11): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 383 citations and is from a highest quality peer-reviewed journal.

6. (pinho2013howtoget pages 9-10): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 383 citations and is from a highest quality peer-reviewed journal.