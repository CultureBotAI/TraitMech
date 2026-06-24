---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:10:34.777768'
end_time: '2026-06-18T10:28:52.387555'
duration_seconds: 1097.61
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
  causal_graph_summary: 'tetrad_two_plane_division: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** tetrad arrangement
- **METPO identifier:** traitmech:000119
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell arrangement in which cocci divide in two perpendicular planes and remain attached as groups of four (tetrads).
- **Parent traits:** METPO:1000666
- **Synonyms:** tetrad-forming cocci
- **Existing evidence:** DOI:10.1128/MMBR.00001-06:  (Young's review treats the tetrad as a division-plane-determined coccal arrangement.) | DOI:10.1038/ncomms4842:  (Two-plane division with incomplete daughter-cell separation yields four-cell tetrads.)
- **Existing causal graph summary:** tetrad_two_plane_division: 3 nodes, 2 edges

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
- **METPO identifier:** traitmech:000119
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell arrangement in which cocci divide in two perpendicular planes and remain attached as groups of four (tetrads).
- **Parent traits:** METPO:1000666
- **Synonyms:** tetrad-forming cocci
- **Existing evidence:** DOI:10.1128/MMBR.00001-06:  (Young's review treats the tetrad as a division-plane-determined coccal arrangement.) | DOI:10.1038/ncomms4842:  (Two-plane division with incomplete daughter-cell separation yields four-cell tetrads.)
- **Existing causal graph summary:** tetrad_two_plane_division: 3 nodes, 2 edges

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


# Research Report: Microbial trait causal graph — **tetrad arrangement** (TraitMech:000119)

## Scope summary (curation-focused)
**Trait label:** tetrad arrangement (syn. tetrad-forming cocci); **category:** morphology; **kind:** class; **definition:** a cell arrangement in which cocci divide in **two perpendicular planes** and remain attached as **groups of four**. This arrangement is best treated as an emergent multicellular morphology determined by (i) **division-plane orientation** across successive cycles and (ii) **efficiency/timing of daughter-cell separation** (septal splitting). (ramosleon2025howdospherical pages 10-11, kabli2013identificationandcharacterisation pages 60-63)

### Boundary cases / related arrangements (do not conflate)
- **Diplococci / pairs:** one division event with incomplete separation → pairs. (ramosleon2025howdospherical pages 10-11)
- **Chains (streptococci):** repeated division in a **single plane** → chains. (kabli2013identificationandcharacterisation pages 60-63)
- **Clusters (staphylococci):** repeated division in (often) orthogonal or variable planes plus separation dynamics → irregular “grape-like” clusters; strict three-plane orthogonality is not always observed. (ramosleon2025howdospherical pages 5-6, saraiva2022studiesofstaphylococcus pages 126-132)
- **Sarcina packets:** division in **three orthogonal planes** → regular cuboidal packets (often 8 cells). (kabli2013identificationandcharacterisation pages 60-63)

**Curation guidance:** tetrad arrangement should be asserted when microscopy shows stable or transient **four-cell square-like units** that can be mechanistically attributed to **two-plane division plus attachment/delayed splitting**, rather than irregular clumps. (ramosleon2025howdospherical pages 10-11, gaifas2024combininglivecell pages 20-24)

## Key concepts and current understanding
### Concept 1 — Orthogonal (perpendicular) division-plane selection
A core mechanistic concept for tetrads is **consecutive orthogonal division**: one division plane is followed by a second plane approximately perpendicular to the first, yielding a 2×2 unit of cells. (ramosleon2025howdospherical pages 10-11, kabli2013identificationandcharacterisation pages 60-63)

### Concept 2 — Septation vs. splitting (daughter-cell separation)
Tetrads require not only orthogonal plane choice but also **incomplete, delayed, or otherwise regulated separation** such that the four cells remain attached as a unit long enough to be observed. In *Deinococcus radiodurans*, septation and splitting are temporally separated: septation in cycle *n* and physical splitting in cycle *n+1*, promoting transient tetrad persistence. (gaifas2024combininglivecell pages 1-4, gaifas2024combininglivecell pages 20-24)

### Concept 3 — Divisome-driven septation and hydrolase-mediated splitting
- **FtsZ** polymerizes into a Z-ring, scaffolding the **divisome** and organizing septal peptidoglycan synthesis (septation). (gaifas2024combininglivecell pages 1-4, ramosleon2025howdospherical pages 1-2)
- **Cell wall hydrolases/autolysins** cleave septal peptidoglycan to split daughters; in *Staphylococcus aureus* this splitting can occur on millisecond timescales and requires hydrolase activity. (ramosleon2025howdospherical pages 5-6)

## Recent developments and latest research (prioritize 2023–2024)
### 1) Cryo-ET + live imaging of septation in *Deinococcus radiodurans* (2024)
Gaifas et al. (bioRxiv, posted **2024-11-18**) propose a distinctive septation mechanism (“**sliding doors**”), where two septa initiate from opposite sides and fuse during closure; importantly, they explicitly connect this mode to diad→tetrad progression and **delayed splitting** across cell cycles. (gaifas2024combininglivecell pages 1-4, gaifas2024combininglivecell pages 4-6)

**Quantitative data (cell-envelope / septation ultrastructure):**
- Membrane protrusions at septal tips in **~40%** of growing septa; tapered septa observed in **40/64** septa. (gaifas2024combininglivecell pages 4-6)
- IM–OM spacing ≈ **100 nm**; peripheral PG thickness **43.9 ± 4.8 nm (n=16)**; septal PG thickness varies **12–51 nm** depending on stage. (gaifas2024combininglivecell pages 4-6)

**Visual evidence:** a schematic of the diad→tetrad cell-cycle phases and **perpendicular division planes** is provided in Figure 1A of the same work. (gaifas2024combininglivecell media 4a57e86a)

### 2) Post-translational control of division-plane “memory” via DivIVA phosphorylation (2023)
Chaudhary et al. (*Microbiology Spectrum*, **2023-04**, ASM) show that *D. radiodurans* **DivIVA (drDivIVA)** is phosphorylated by the radiation-responsive kinase **RqkA** at **T19**, and that a phosphomimetic **T19E** allele arrests normal DivIVA dynamics and alters localization patterns, consistent with DivIVA functioning as a polarity/plane-of-division determinant whose activity can be attenuated after DNA damage. (chaudhary2023divivaphosphorylationaffects pages 1-2, chaudhary2023divivaphosphorylationaffects pages 2-4)

**Quantitative imaging (DivIVA foci patterns):**
- T19E: **83.6% ± 6.364%** of cells show **two** DivIVA foci per cell.
- T19A: increased fraction with **>4** foci (**~62.5% ± 3.965%**).
- Multi-foci often juxtaposed across tetrad compartments (**~56.5% ± 3.536%**). (chaudhary2023divivaphosphorylationaffects pages 4-6)

**Mechanistic interpretation (curation note):** evidence is strong for *DivIVA phosphorylation → altered DivIVA dynamics/localization → altered division physiology*; the direct mapping to *tetrad arrangement frequency* is more inferential and should be curated with an “uncertain / taxon-specific” flag. (chaudhary2023divivaphosphorylationaffects pages 1-2, chaudhary2023divivaphosphorylationaffects pages 6-8)

## Current applications / real-world implementations
1) **Diagnostic and taxonomic microbiology (microscopy phenotype):** Coccal arrangement patterns (pairs, chains, tetrads, clusters, sarcina) remain a practical morphological discriminant used in routine microscopy and educational/clinical microbiology workflows; mechanistically, these arrangements are explicitly tied to division-plane choice and separation behavior. (kabli2013identificationandcharacterisation pages 60-63, ramosleon2025howdospherical pages 10-11)

2) **High-content microscopy + automated morphometrics:** Recent work on coccal division emphasizes quantitative imaging pipelines that measure division-plane angles and test classical orthogonal-division models; these approaches are implementable in lab workflows to link genotype/drug perturbations to arrangement outcomes. (saraiva2022studiesofstaphylococcus pages 126-132)

3) **Antibiotic mechanism studies via septation perturbation:** Septal peptidoglycan synthesis can be selectively inhibited (e.g., ampicillin fully inhibiting the septal machinery in *D. radiodurans*), enabling perturbation-based dissection of septation vs peripheral wall synthesis and, indirectly, of arrangement phenotypes. (gaifas2024combininglivecell pages 4-6)

## Expert opinions and authoritative synthesis
- A modern mechanistic view is that coccal multicellular morphologies arise from a combination of (i) **Z-ring placement and dynamics** and (ii) **septal splitting**, with major diversity across taxa in whether mechanisms are predominantly negative regulators (Min/nucleoid occlusion) or positive regulators (e.g., lineage-specific factors). (ramosleon2025howdospherical pages 1-2, ramosleon2025howdospherical pages 2-3)
- The “division planes determine arrangement” framing is also consistent with classic synthesis: cocci can divide in multiple planes, yielding arrangements such as tetrads or packets when division or separation are modulated. (kabli2013identificationandcharacterisation pages 60-63, young2006theselectivevalue pages 14-15)

## Candidate causal graph entities (grouped by type)
**Phenotype node**
- tetrad arrangement — METPO:traitmech:000119 (given)

**Biological processes (GO)**
- cell division — GO:0051301 (broad)
- division septum assembly / septation — GO:0000917
- cytokinetic process — GO:0000915
- peptidoglycan catabolic process (septal splitting) — GO:0009253
- (label-only) orthogonal division-plane selection
- (label-only) division-plane “memory”

**Genes/proteins/complexes (label-only unless mapped per taxon)**
- FtsZ (Z-ring)
- DivIVA (drDivIVA in *D. radiodurans*)
- RqkA Ser/Thr kinase (radiation responsive; phosphorylates DivIVA)
- (review-derived candidate) Min system components (MinC/MinD/MinE) and MinJ
- (review-derived candidate) Noc (nucleoid occlusion), MapZ (positive Z-ring positioning), PcdA (orthogonal plane selection in some staphylococci), GpsB, FacZ
- cell wall hydrolases/autolysins (septal splitting)

**Chemicals / inhibitors (ChEBI)**
- ampicillin — CHEBI:28971 (septal PG synthesis inhibitor context) (gaifas2024combininglivecell pages 4-6)

**Cell-envelope / structural entities**
- peptidoglycan layer (thickness and remodeling at septa) (gaifas2024combininglivecell pages 4-6)

## Candidate causal edges (evidence-backed)
The following table is designed to be directly mined into `tetrad_arrangement.yaml` as candidate edges and supporting evidence.

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet | Source | DOI/URL | Notes/uncertainty for curation |
|---|---|---|---|---|---|---|
| Consecutive orthogonal division planes (GO:0051301 cell division; label-only: orthogonal division-plane selection) | produces | tetrad arrangement (METPO:traitmech:000119) | “Tetrads arise when a spherical cell divides in one plane and then again in a plane roughly perpendicular to the first, producing four cells arranged as a square due to incomplete separation.” (ramosleon2025howdospherical pages 10-11) | Ramos-León, 2025, *Biochemical Society Transactions* | https://doi.org/10.1042/bst20240956 | Strong phenotype-level edge; broad coccal mechanism, not taxon-specific. |
| Delayed daughter-cell splitting / temporal separation of septation and splitting (GO:0000917 division septum assembly; GO:0000915 cytokinetic process) | prolongs | tetrad persistence (label-only) | In *D. radiodurans*, “septation occurs in cycle n and splitting in cycle n+1”; tetrads are formed in Phase 6 and then “rapidly split into two diads.” (gaifas2024combininglivecell pages 1-4, gaifas2024combininglivecell pages 20-24) | Gaifas, 2024, *bioRxiv* | https://doi.org/10.1101/2024.11.18.624142 | Strong for transient tetrad maintenance in *D. radiodurans*; direct persistence mechanism, but taxon-specific and from preprint. |
| DivIVA localization / inherited DivIVA foci (UniProt grounding unclear; GO:0000917 division septum assembly, label-only: division-plane memory) | guides | perpendicular division-plane orientation (label-only) | drDivIVA “marks both old and new division planes” and inherited foci may act as “memory foci” so “the next division plane is perpendicular to the previous one.” (chaudhary2023divivaphosphorylationaffects pages 11-13, chaudhary2023divivaphosphorylationaffects pages 6-8) | Chaudhary, 2023, *Microbiology Spectrum* | https://doi.org/10.1128/spectrum.03141-22 | Moderate support; mechanistically rich but from one taxon (*D. radiodurans*). Useful candidate edge for curation with taxon note. |
| RqkA kinase (label-only; Ser/Thr quinoprotein kinase) | phosphorylates | DivIVA T19 (label-only) | “RqkA phosphorylates drDivIVA at the threonine 19 (T19) residue.” Phospho-mimetic T19E “arrested” normal DivIVA dynamics and altered localization. (chaudhary2023divivaphosphorylationaffects pages 1-2, chaudhary2023divivaphosphorylationaffects pages 2-4) | Chaudhary, 2023, *Microbiology Spectrum* | https://doi.org/10.1128/spectrum.03141-22 | Strong biochemical edge in *D. radiodurans*. |
| DivIVA T19 phosphorylation / phosphomimetic T19E (label-only) | disrupts | DivIVA dynamics and division-plane memory (label-only) | T19E “showed no dynamics in time-lapse studies,” produced fewer foci, and “failed to take part in the process of cell division.” (chaudhary2023divivaphosphorylationaffects pages 11-13, chaudhary2023divivaphosphorylationaffects pages 6-8, chaudhary2023divivaphosphorylationaffects pages 8-11) | Chaudhary, 2023, *Microbiology Spectrum* | https://doi.org/10.1128/spectrum.03141-22 | Strong for altered DivIVA behavior; indirect for tetrad output. |
| Altered DivIVA dynamics / T19 phosphorylation state (label-only) | contributes to | division arrest or altered septum positioning (label-only) | The authors conclude phosphorylation “attenuates DivIVA’s function in cell polarity and the determination of the plane of cell division”; T19E replacement was not tolerated unless complemented. (chaudhary2023divivaphosphorylationaffects pages 1-2, chaudhary2023divivaphosphorylationaffects pages 4-6) | Chaudhary, 2023, *Microbiology Spectrum* | https://doi.org/10.1128/spectrum.03141-22 | Curate as uncertain/indirect for tetrad arrangement itself; evidence is stronger for cell-cycle arrest and septum-position defects. |
| FtsZ Z-ring assembly (GO:0051301 cell division; UniProt grounding taxon-specific) | initiates / scaffolds | septation (GO:0000917 division septum assembly) | “Division involves assembly of FtsZ into a Z-ring that scaffolds membrane-associated division factors… forming the divisome.” (gaifas2024combininglivecell pages 1-4); general review: FtsZ polymerizes into a Z-ring and recruits the divisome. (ramosleon2025howdospherical pages 1-2) | Gaifas, 2024, *bioRxiv*; Ramos-León, 2025, *Biochemical Society Transactions* | https://doi.org/10.1101/2024.11.18.624142 ; https://doi.org/10.1042/bst20240956 | Strong general bacterial cell-division edge; necessary context node, but not specific to tetrads. |
| Cell wall hydrolases / autolysins (GO:0009253 peptidoglycan catabolic process; label-only) | mediate | rapid daughter-cell splitting (label-only) | After septation, the cell “splits into two daughter cells… very fast (within milliseconds) and requires the actions of cell wall hydrolases.” (ramosleon2025howdospherical pages 5-6) | Ramos-León, 2025, *Biochemical Society Transactions* | https://doi.org/10.1042/bst20240956 | Strong for separation step; mainly from *S. aureus* context, but broadly plausible in cocci. |
| Ampicillin (CHEBI:28971) | inhibits | septal peptidoglycan synthesis machinery (label-only) | “Two distinct machineries mediate septal versus peripheral cell-wall synthesis; the septal machinery is fully inhibited by ampicillin.” (gaifas2024combininglivecell pages 4-6) | Gaifas, 2024, *bioRxiv* | https://doi.org/10.1101/2024.11.18.624142 | Good experimental-factor edge for septation context; not a native causal determinant of tetrads. |
| DivIVA-occupied membrane domains / DivIVA-free zones (label-only) | excludes / spatially positions | FtsZ ring placement (label-only) | “FtsZ localizes in spaces unoccupied by drDivIVA,” and FtsZ rings form in “drDivIVA-free zones.” (chaudhary2023divivaphosphorylationaffects pages 4-6, chaudhary2023divivaphosphorylationaffects pages 6-8) | Chaudhary, 2023, *Microbiology Spectrum* | https://doi.org/10.1128/spectrum.03141-22 | Moderate support for negative spatial relationship in *D. radiodurans*; mechanism likely taxon-specific. |
| Subtle morphology changes / local membrane curvature cues (label-only) | biases | orthogonal plane selection (label-only) | “Subtle cell elongation and resulting local membrane curvature act as geometric cues for selecting the next perpendicular division plane.” (ramosleon2025howdospherical pages 7-8) | Ramos-León, 2025, *Biochemical Society Transactions* | https://doi.org/10.1042/bst20240956 | Mark uncertain for tetrads: inference comes mainly from *S. aureus* orthogonal division, not direct tetrad-forming taxa. |


*Table: This table lists curation-ready candidate causal edges for the microbial trait tetrad arrangement, with suggested node grounding, evidence snippets, and curation notes. It focuses on mechanistic links most directly supported by the available literature and flags taxon-specific or indirect claims.*

## Relevant statistics and data (recent studies)
- *D. radiodurans* septation ultrastructure includes septal-tip protrusions in **~40%** of growing septa, and tapered septa in **40/64** septa; peripheral PG thickness **43.9 ± 4.8 nm (n=16)**, septal PG thickness **12–51 nm**, IM–OM spacing **~100 nm**. (gaifas2024combininglivecell pages 4-6)
- DivIVA foci distributions in phosphorylation mutants (T19E vs T19A) quantify the extent of DivIVA spatial reorganization, including **83.6% ± 6.364%** (two foci in T19E) and **~62.5% ± 3.965%** (>4 foci in T19A). (chaudhary2023divivaphosphorylationaffects pages 4-6)
- Quantitative divisome-angle measurements in *S. aureus* show substantial deviation from strict orthogonal-plane models: >**85%** of sister pairs had divisome angles >15° (n=77) and a majority had >15° in a larger dataset (n=307), spanning 0–90°. (saraiva2022studiesofstaphylococcus pages 126-132)

## Warnings / claims that should not yet be curated as general TraitMech edges
1) **Generalizing *D. radiodurans* DivIVA/RqkA regulation to all tetrad-forming cocci:** strong within-taxon evidence exists, but cross-taxon conservation for tetrad arrangement is not established in the provided sources. Curate with NCBITaxon scoping or mark uncertain. (chaudhary2023divivaphosphorylationaffects pages 1-2, chaudhary2023divivaphosphorylationaffects pages 6-8)

2) **Assuming strict three-plane orthogonal division in staphylococci as a universal rule:** quantitative measurements indicate broad angle distributions and frequent departures from the canonical model, suggesting arrangement outcomes may be strain- and condition-dependent. (saraiva2022studiesofstaphylococcus pages 126-132, saraiva2022studiesofstaphylococcus pages 121-126)

3) **Using antibiotic inhibition edges as endogenous determinants:** ampicillin is a useful experimental perturbation of septation but should be encoded as an experimental factor, not a native causal node for tetrad arrangement. (gaifas2024combininglivecell pages 4-6)

---

# DOI-first bibliography (with dates and URLs)
1) Gaifas L, et al. **Combining live cell fluorescence imaging with in situ cryo electron tomography sheds light on the septation process in *Deinococcus radiodurans***. *bioRxiv* (posted **2024-11-18**). DOI: **10.1101/2024.11.18.624142**. URL: https://doi.org/10.1101/2024.11.18.624142 (gaifas2024combininglivecell pages 1-4, gaifas2024combininglivecell pages 4-6, gaifas2024combininglivecell media 4a57e86a, gaifas2024combininglivecell pages 20-24)

2) Chaudhary R, Kota S, Misra HS. **DivIVA phosphorylation affects its dynamics and cell cycle in radioresistant *Deinococcus radiodurans***. *Microbiology Spectrum* (**2023-04**). DOI: **10.1128/spectrum.03141-22**. URL: https://doi.org/10.1128/spectrum.03141-22 (chaudhary2023divivaphosphorylationaffects pages 1-2, chaudhary2023divivaphosphorylationaffects pages 4-6, chaudhary2023divivaphosphorylationaffects pages 6-8)

3) Floc’h K, et al. **Cell morphology and nucleoid dynamics in dividing *Deinococcus radiodurans***. *Nature Communications* (**2019-08**). DOI: **10.1038/s41467-019-11725-5**. URL: https://doi.org/10.1038/s41467-019-11725-5 (ramosleon2025howdospherical pages 9-10)

4) Young KD. **The Selective Value of Bacterial Shape**. *Microbiology and Molecular Biology Reviews* (**2006-09**). DOI: **10.1128/MMBR.00001-06**. URL: https://doi.org/10.1128/MMBR.00001-06 (young2006theselectivevalue pages 14-15)

5) Ramos-León F, Ramamurthi KS. **How do spherical bacteria regulate cell division?** *Biochemical Society Transactions* (**2025-04**). DOI: **10.1042/bst20240956**. URL: https://doi.org/10.1042/bst20240956 (ramosleon2025howdospherical pages 10-11, ramosleon2025howdospherical pages 5-6, ramosleon2025howdospherical pages 6-7, ramosleon2025howdospherical pages 2-3)

6) Saraiva BMS. **Studies of *Staphylococcus aureus*’ cell cycle: New approaches for automated analysis**. (dissertation/thesis; **2022**; DOI not available in retrieved evidence). Quantitative divisome-angle statistics and discussion of orthogonal-plane models. (saraiva2022studiesofstaphylococcus pages 126-132, saraiva2022studiesofstaphylococcus pages 121-126)

7) Kabli A. **Identification and Characterisation of Cell Division Proteins in *Staphylococcus aureus***. (thesis; **2013**; DOI not available in retrieved evidence). Includes explicit arrangement definitions (tetrads vs chains vs sarcina vs clusters) and examples. (kabli2013identificationandcharacterisation pages 60-63)

References

1. (ramosleon2025howdospherical pages 10-11): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.

2. (kabli2013identificationandcharacterisation pages 60-63): A Kabli. Identification and characterisation of cell division proteins in staphylococcus aureus. Unknown journal, 2013.

3. (ramosleon2025howdospherical pages 5-6): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.

4. (saraiva2022studiesofstaphylococcus pages 126-132): BMS Saraiva. Studies of staphylococcus aureus' cell cycle: new approaches for automated analysis. Unknown journal, 2022.

5. (gaifas2024combininglivecell pages 20-24): L. Gaifas, J.P. Kleman, F. Lacroix, E. Schexnaydre, J. Trouve, C. Morlot, L. Sandblad, I. Gutsche, and J. Timmins. Combining live cell fluorescence imaging with in situ cryo electron tomography sheds light on the septation process in deinococcus radiodurans. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.18.624142, doi:10.1101/2024.11.18.624142. This article has 0 citations.

6. (gaifas2024combininglivecell pages 1-4): L. Gaifas, J.P. Kleman, F. Lacroix, E. Schexnaydre, J. Trouve, C. Morlot, L. Sandblad, I. Gutsche, and J. Timmins. Combining live cell fluorescence imaging with in situ cryo electron tomography sheds light on the septation process in deinococcus radiodurans. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.18.624142, doi:10.1101/2024.11.18.624142. This article has 0 citations.

7. (ramosleon2025howdospherical pages 1-2): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.

8. (gaifas2024combininglivecell pages 4-6): L. Gaifas, J.P. Kleman, F. Lacroix, E. Schexnaydre, J. Trouve, C. Morlot, L. Sandblad, I. Gutsche, and J. Timmins. Combining live cell fluorescence imaging with in situ cryo electron tomography sheds light on the septation process in deinococcus radiodurans. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.18.624142, doi:10.1101/2024.11.18.624142. This article has 0 citations.

9. (gaifas2024combininglivecell media 4a57e86a): L. Gaifas, J.P. Kleman, F. Lacroix, E. Schexnaydre, J. Trouve, C. Morlot, L. Sandblad, I. Gutsche, and J. Timmins. Combining live cell fluorescence imaging with in situ cryo electron tomography sheds light on the septation process in deinococcus radiodurans. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.18.624142, doi:10.1101/2024.11.18.624142. This article has 0 citations.

10. (chaudhary2023divivaphosphorylationaffects pages 1-2): Reema Chaudhary, Swathi Kota, and Hari S. Misra. Diviva phosphorylation affects its dynamics and cell cycle in radioresistant deinococcus radiodurans. Apr 2023. URL: https://doi.org/10.1128/spectrum.03141-22, doi:10.1128/spectrum.03141-22. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (chaudhary2023divivaphosphorylationaffects pages 2-4): Reema Chaudhary, Swathi Kota, and Hari S. Misra. Diviva phosphorylation affects its dynamics and cell cycle in radioresistant deinococcus radiodurans. Apr 2023. URL: https://doi.org/10.1128/spectrum.03141-22, doi:10.1128/spectrum.03141-22. This article has 8 citations and is from a domain leading peer-reviewed journal.

12. (chaudhary2023divivaphosphorylationaffects pages 4-6): Reema Chaudhary, Swathi Kota, and Hari S. Misra. Diviva phosphorylation affects its dynamics and cell cycle in radioresistant deinococcus radiodurans. Apr 2023. URL: https://doi.org/10.1128/spectrum.03141-22, doi:10.1128/spectrum.03141-22. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (chaudhary2023divivaphosphorylationaffects pages 6-8): Reema Chaudhary, Swathi Kota, and Hari S. Misra. Diviva phosphorylation affects its dynamics and cell cycle in radioresistant deinococcus radiodurans. Apr 2023. URL: https://doi.org/10.1128/spectrum.03141-22, doi:10.1128/spectrum.03141-22. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (ramosleon2025howdospherical pages 2-3): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.

15. (young2006theselectivevalue pages 14-15): Kevin D. Young. The selective value of bacterial shape. Microbiology and Molecular Biology Reviews, 70:660-703, Sep 2006. URL: https://doi.org/10.1128/mmbr.00001-06, doi:10.1128/mmbr.00001-06. This article has 1284 citations and is from a domain leading peer-reviewed journal.

16. (chaudhary2023divivaphosphorylationaffects pages 11-13): Reema Chaudhary, Swathi Kota, and Hari S. Misra. Diviva phosphorylation affects its dynamics and cell cycle in radioresistant deinococcus radiodurans. Apr 2023. URL: https://doi.org/10.1128/spectrum.03141-22, doi:10.1128/spectrum.03141-22. This article has 8 citations and is from a domain leading peer-reviewed journal.

17. (chaudhary2023divivaphosphorylationaffects pages 8-11): Reema Chaudhary, Swathi Kota, and Hari S. Misra. Diviva phosphorylation affects its dynamics and cell cycle in radioresistant deinococcus radiodurans. Apr 2023. URL: https://doi.org/10.1128/spectrum.03141-22, doi:10.1128/spectrum.03141-22. This article has 8 citations and is from a domain leading peer-reviewed journal.

18. (ramosleon2025howdospherical pages 7-8): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.

19. (saraiva2022studiesofstaphylococcus pages 121-126): BMS Saraiva. Studies of staphylococcus aureus' cell cycle: new approaches for automated analysis. Unknown journal, 2022.

20. (ramosleon2025howdospherical pages 9-10): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.

21. (ramosleon2025howdospherical pages 6-7): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.