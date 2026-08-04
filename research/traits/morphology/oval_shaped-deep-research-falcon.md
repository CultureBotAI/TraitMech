---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:22:30.691494'
end_time: '2026-08-04T09:30:16.425484'
duration_seconds: 465.73
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: oval shaped
  trait_identifier: METPO:1000678
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: oval_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape characterized by an ellipsoidal morphology with rounded
    ends, resembling an elongated sphere.
  parent_traits: METPO:1000666
  synonyms: oval-shaped
  evidence_summary: 'DOI:10.1089/mdr.2014.0032: ovococci that are ellipsoid (Supports
    oval/ellipsoidal morphology as an ovococcal bacterial shape class.)'
  causal_graph_summary: 'oval_shaped_ovococcal_pg_synthesis: 10 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** oval shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000678
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by an ellipsoidal morphology with rounded ends, resembling an elongated sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** oval-shaped
- **Existing evidence:** DOI:10.1089/mdr.2014.0032: ovococci that are ellipsoid (Supports oval/ellipsoidal morphology as an ovococcal bacterial shape class.)
- **Existing causal graph summary:** oval_shaped_ovococcal_pg_synthesis: 10 nodes, 11 edges

## Research Objective

Research the microbial trait **oval shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/oval_shaped.yaml`.

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
- **Trait label:** oval shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000678
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by an ellipsoidal morphology with rounded ends, resembling an elongated sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** oval-shaped
- **Existing evidence:** DOI:10.1089/mdr.2014.0032: ovococci that are ellipsoid (Supports oval/ellipsoidal morphology as an ovococcal bacterial shape class.)
- **Existing causal graph summary:** oval_shaped_ovococcal_pg_synthesis: 10 nodes, 11 edges

## Research Objective

Research the microbial trait **oval shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/oval_shaped.yaml`.

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


# Curation-focused research report: bacterial **oval shaped** morphology

## 1. Trait scope

**Trait:** oval shaped  
**Identifier:** **METPO:1000678**  
**Category:** morphology; **term kind:** class; **mapping status:** reviewed  
**Parent:** METPO:1000666  
**Synonym:** oval-shaped

For TraitMech, this class should represent a reproducible **ovoid/prolate-ellipsoidal cell morphology with rounded poles and a measurable long axis**, not merely any approximately round microscopic profile. Ovococci are described as elongated ellipsoids that divide in successive parallel planes perpendicular to the long axis. In the best-developed model, *Streptococcus pneumoniae*, septal peptidoglycan (sPG) constructs the daughter-cell cross-wall, whereas concurrent peripheral peptidoglycan (pPG) synthesis elongates daughters from midcell to generate the ovoid shape. Both processes occur at midcell rather than along the entire lateral wall. (tan2021streptococcussuismsmk pages 1-2, perez2021organizationofpeptidoglycan pages 1-5)

### Boundary cases

* **Spherical cocci:** should not be included merely because an oval cell becomes round in one projection. Spherical cocci such as *Staphylococcus aureus* primarily construct a transverse septum and undergo a much shorter elongation stage; ovococci require substantial peripheral as well as septal wall growth. (tan2021streptococcussuismsmk pages 1-2, briggs2021thepneumococcaldivisome pages 2-3)
* **Rods:** rods have a cylindrical sidewall and generally use an MreB-organized elongasome distributed over the cell body. Most ovococci lack MreB; their elongasome and divisome remain near midcell. Inhibiting septal growth can make ovococci rod-like, but that perturbational phenotype is not the native oval trait. (tan2021streptococcussuismsmk pages 1-2, trouve2021nanoscaledynamicsof pages 1-3)
* **Round mutants of ovococci:** loss of peripheral growth—for example, deletion of *divIVA*, *mltG*, or *msmK* in *S. suis*—produces shorter, lower-aspect-ratio cells. These are mechanistically informative loss-of-trait states, not instances of **METPO:1000678**. (tan2021streptococcussuismsmk pages 8-11, jiang2023divivainteractswith pages 1-2, jiang2023divivainteractswith pages 9-11)
* **Chains/diplococci:** chaining is an arrangement or separation phenotype, orthogonal to individual-cell shape. An oval cell may occur singly, as a diplococcus, or in chains. The graph should model these separately.
* **Transient cell-cycle stages:** newly divided, constricting, or predivisional cells have different outlines. Curate the population-level or cell-cycle-normalized shape rather than a single optical section.
* **Other ovoid mechanisms:** budding ovoid planctomycetes and non-streptococcal ovoid cells may use different machinery. The graph below is principally an **ovococcal Firmicute mechanism**, especially *S. pneumoniae*, *S. suis*, and *Lactococcus lactis*.

## 2. Current mechanistic synthesis

The strongest model is a balance between two spatially adjacent wall-building activities. The **RodA–PBP2b elongasome arm** supports pPG synthesis and longitudinal extension, while the **FtsW–PBP2x divisome arm** supports sPG synthesis and invagination. FtsZ provides the midcell scaffold; MapZ helps position future equatorial rings. Early in division, the activities occupy one annular region and then resolve into an outer pPG ring and inner sPG ring. Contrary to an older strict “peripheral first, septal second” switch model, nanoscale imaging indicates that septal synthesis begins early, both modes overlap, and peripheral synthesis can persist after septal closure. (xiang2019regulationofcell pages 19-24, briggs2021thepneumococcaldivisome pages 2-3, trouve2021nanoscaledynamicsof pages 1-3, perez2021organizationofpeptidoglycan pages 1-5)

Regulation is layered onto this core. DivIVA promotes peripheral growth; StkP/STK-dependent phosphorylation changes DivIVA behavior and its interaction with the hydrolase MltG; GpsB constrains elongation and supports StkP localization; and MsmK couples FtsZ organization to peripheral wall synthesis in *S. suis*. The resulting oval shape is therefore an emergent outcome of **PG polymerization, cross-linking, hydrolysis/remodeling, spatial positioning, and cell-cycle timing**, rather than the product of one shape gene. (tan2021streptococcussuismsmk pages 1-2, jiang2023divivainteractswith pages 9-11, fleurie2014interplayofthe pages 1-2)

## 3. Candidate nodes grouped by type

### Trait and taxonomic context

* **oval shaped** — **METPO:1000678**
* Parent morphology class — **METPO:1000666**
* *Streptococcus pneumoniae* — label plus NCBITaxon grounding should be added during strain-specific curation.
* *Streptococcus suis* — label plus NCBITaxon grounding should be added during strain-specific curation.
* *Lactococcus lactis* — label plus NCBITaxon grounding should be added during strain-specific curation.

Taxon identifiers should be resolved together with the exact experimental strain; strain background materially changes the essentiality and phenotypes of proteins such as GpsB and MreC/MreD. (fleurie2014interplayofthe pages 10-11)

### Processes and pathways

* Peptidoglycan biosynthetic process — **GO:0009252**
* Cell-wall organization or biogenesis — **GO:0071555**
* Cell division — **GO:0051301**
* Cell cycle — **GO:0007049**
* Peripheral peptidoglycan synthesis — label-only child process pending an appropriate specific ontology term
* Septal peptidoglycan synthesis — label-only child process pending an appropriate specific ontology term
* Peptidoglycan hydrolysis/remodeling — retain label-only unless a verified specific GO term is selected
* Cell elongation, septation, cytokinesis, septum splitting, daughter-cell separation — candidate process nodes
* Capsule biosynthesis and complement evasion — downstream application/virulence branch, not required for the minimal oval-shape graph

### Cellular structures and localizations

* Peptidoglycan-based cell wall — **GO:0009274**
* Plasma membrane — **GO:0005886**
* Integral component of plasma membrane — **GO:0005887**
* Midcell, division septum, septal annulus, future equator, cell pole
* FtsZ/Z-ring
* Elongasome/Rod complex
* Divisome
* Outer peripheral-PG ring and inner septal-PG ring

### Genes, proteins, enzymes, and complexes

Use gene-symbol/label nodes until taxon- and strain-specific UniProt accessions are verified:

* **RodA–PBP2b complex:** peripheral glycan polymerization/transpeptidation arm
* **FtsW–PBP2x complex:** septal glycan polymerization/transpeptidation arm
* **FtsZ:** Z-ring scaffold
* **MapZ/LocZ:** equatorial-positioning factor
* **FtsA, EzrA:** FtsZ-associated division proteins
* **MreC, MreD:** elongasome regulators; despite their names, ovococci generally lack MreB
* **DivIVA:** peripheral-growth regulator
* **StkP/STK:** serine/threonine kinase regulating morphogenesis
* **GpsB:** DivIVA/StkP-associated division regulator
* **MltG/MpgA:** membrane-associated PG hydrolase/muramidase and elongasome-associated factor
* **MsmK:** ATPase/GTPase and FtsZ-interacting shape-maintenance protein in *S. suis*
* **PBP1a:** class A PBP implicated in compensatory relationships with MreC/MreD/MltG
* **FtsX/PcsB:** candidate peripheral-remodeling module
* **CpsC/CpsD, CpsA, CpsH, glycosyltransferases, CpsJ:** optional envelope/capsule branch

### Chemicals and experimental factors

* Peptidoglycan; lipid II; glycan strands; peptide cross-links
* N-acetylglucosamine and N-acetylmuramic acid — ground only after CHEBI verification
* ATP and GTP — required for kinase/MsmK/FtsZ mechanisms; add verified CHEBI identifiers during implementation
* β-lactam antibiotic — **CHEBI:35627**
* Methicillin — label-only here pending identifier verification
* Fluorescent D-amino acids HADA/TADA and azido-D-Ala-D-Ala — **assay probes**, not endogenous causal nodes
* Gene deletion/depletion, phospho-null DivIVA3A, phosphomimetic DivIVA3E, β-lactam exposure — experimental-factor nodes or evidence qualifiers rather than biological graph entities

## 4. Candidate causal edges

The following table prioritizes direct perturbation or high-resolution localization evidence. “High” denotes a directly observed species-specific result; “medium” commonly denotes a well-supported model or review-derived edge; “low-medium” denotes an explicit mechanistic hypothesis.

| subject | predicate | object | taxon/assay | DOI | exact supporting snippet | confidence/curation note |
|---|---|---|---|---|---|---|
| Peripheral peptidoglycan (pPG) synthesis | contributes to / elongates into | ovoid/oval cell shape | *Streptococcus pneumoniae*; 3D-SIM, FDAA labeling, cell-cycle analysis | 10.1111/mmi.14659 | “concurrent pPG synthesis elongates daughter cells from midcell to form ovoid-shaped cells” (perez2021organizationofpeptidoglycan pages 1-5) | High. Strong direct morphology statement in pneumococcus; curate as ovococcal mechanism, not all bacteria. |
| Septal peptidoglycan (sPG) synthesis | produces | cross wall separating daughter cells | *Streptococcus pneumoniae*; 3D-SIM/reviewed localization model | 10.1111/mmi.14659 | “sPG synthesis produces the cross wall that separates daughter cells” (perez2021organizationofpeptidoglycan pages 1-5) | High. Direct role statement. |
| RodA–PBP2b complex | is core enzyme for | peripheral peptidoglycan synthesis | Ovococci/*S. pneumoniae* model summarized in *S. suis* paper | 10.1128/spectrum.04750-22 | “It has been suggested that in *Streptococcus pneumoniae*, the RodA-PBP2b complex is the core enzyme for peripheral PG synthesis” (jiang2023divivainteractswith pages 1-2) | Medium. Mechanistic claim is presented as suggested/model-based in review framing within primary paper; taxon-specific to pneumococcus/ovococci. |
| FtsW–PBP2x complex | is responsible for | septal peptidoglycan synthesis / cell invagination | Ovococci/*S. pneumoniae* model summarized in *S. suis* paper | 10.1128/spectrum.04750-22 | “the FtsW-PBP2x complex is responsible for the PG synthesis at the septum leading to cell invagination” (jiang2023divivainteractswith pages 1-2) | Medium. Strongly plausible and widely supported, but quoted here as model summary; curate with taxon specificity. |
| DivIVA deletion | causes | abortive / nearly complete halt of peripheral PG synthesis | *Streptococcus suis*; HADA probing, 3D-SIM | 10.1128/spectrum.04750-22 | “DivIVA deletion caused abortive peripheral PG synthesis” (jiang2023divivainteractswith pages 1-2); “Deletion of divIVA caused a nearly complete halt in peripheral PG synthesis” (jiang2023divivainteractswith pages 9-11) | High. Direct perturbation evidence in *S. suis*. |
| DivIVA deletion | decreases aspect ratio / causes rounding | shorter, flatter, rounder cells | *Streptococcus suis*; morphology microscopy | 10.1128/spectrum.04750-22 | “DivIVA deletion caused abortive peripheral PG synthesis, resulting in a decreased aspect ratio” (jiang2023divivainteractswith pages 1-2); “resulting in noticeably shorter and flatter cells” (jiang2023divivainteractswith pages 9-11) | High. Direct phenotype evidence; species-specific. |
| STK phosphorylation of DivIVA | regulates | peripheral PG synthesis | *Streptococcus suis*; phosphomutants DivIVA3A/DivIVA3E, HADA pulse/chase | 10.1128/spectrum.04750-22 | “The results suggest that DivIVA phosphorylation does regulate the peripheral PG synthesis.” (jiang2023divivainteractswith pages 4-6) | High. Direct mutant evidence. |
| Phosphomimetic DivIVA3E / DivIVA phosphorylation state | alters interaction with / mislocalizes | MltG | *Streptococcus suis*; co-IP, BTH, localization | 10.1128/spectrum.04750-22 | “the phosphorylation state of DivIVA affects its interaction with MltG” and “MltG protein localized at the center of the wild-type cell septum was significantly mislocalized in the ΔdivIVA and DivIVA3E strains” (jiang2023divivainteractswith pages 9-11) | High for interaction/localization change. |
| DivIVA phosphorylation | terminates | peripheral PG synthesis before septal PG synthesis begins | *Streptococcus suis*; discussion/model inference | 10.1128/spectrum.04750-22 | “We hypothesize that after the DivIVA protein is phosphorylated by STK in vivo, it interacts with MltG, mislocalizing MltG, terminating peripheral PG synthesis before septal PG synthesis begins” (jiang2023divivainteractswith pages 9-11) | Low-Medium. Explicitly a hypothesis; do not curate as firm mechanistic edge without qualifier. |
| ΔmltG | impairs | peripheral PG synthesis | *Streptococcus suis*; HADA staining | 10.1128/spectrum.04750-22 | “Imaging of nascent PG synthesis by HADA staining further revealed that ΔmltG and DivIVA3E cells undertook impaired peripheral PG synthesis” (jiang2023divivainteractswith pages 9-11) | High. Direct perturbation evidence. |
| ΔmltG | causes | shorter/wider/rounder cells | *Streptococcus suis*; morphology microscopy | 10.1128/spectrum.04750-22 | “both ΔmltG and DivIVA3E cells were significantly shorter and wider” and “both ΔmltG and DivIVA3E cells formed significantly rounder cells” (jiang2023divivainteractswith pages 9-11, jiang2023divivainteractswith pages 1-2) | High. Direct morphology evidence. |
| MsmK | interacts with / colocalizes with | FtsZ at division site | *Streptococcus suis*; in vivo pulldown, immunofluorescence, 3D microscopy | 10.1128/msphere.00119-21 | “MsmK could form complexes with FtsZ in vivo” and “MsmK-GFP colocalized with the ring of FtsZ throughout the cell cycle” (tan2021streptococcussuismsmk pages 8-11, tan2021streptococcussuismsmk pages 1-2) | High. Direct interaction/localization evidence. |
| ΔmsmK | causes | disturbed cell elongation and peripheral PG synthesis, but normal septal PG walls | *Streptococcus suis*; superresolution microscopy | 10.1128/msphere.00119-21 | “the lack of MsmK in cells leads to normal septal peptidoglycan walls in mother cells but disturbed cell elongation and peripheral peptidoglycan synthesis” (tan2021streptococcussuismsmk pages 1-2) | High. Direct perturbation evidence. |
| ΔmsmK | shortens / rounds | cells; lower aspect ratio | *Streptococcus suis*; TEM/morphometry | 10.1128/msphere.00119-21 | “On average, the cells lacking MsmK were significantly shorter (0.896 ± 0.20 μm) than the WT cells (1.056 ± 0.14 μm)” and “the length-to-width ratio in mutants (1.356 ± 0.28) was significantly lower than that in WT cells (1.586 ± 0.21)” (tan2021streptococcussuismsmk pages 8-11) | High. Quantitative direct phenotype; strong candidate edge for oval-shape maintenance. |
| GpsB deletion | triggers | cell elongation with helical FtsZ / PG synthesis patterns | *Streptococcus pneumoniae*; fluorescence microscopy | 10.1371/journal.pgen.1004275 | “the absence of GpsB resulted in hampered cell division and triggered cell elongation” and “ΔgpsB elongated cells exhibited a helical FtsZ pattern instead of a Z-ring, accompanied by helical patterns for DivIVA and peptidoglycan synthesis” (fleurie2014interplayofthe pages 1-2) | High. Direct perturbation evidence in pneumococcus. |
| DivIVA deletion | suppresses | ΔgpsB elongated phenotype | *Streptococcus pneumoniae*; double mutant morphology | 10.1371/journal.pgen.1004275 | “divIVA deletion suppressed the elongated phenotype of ΔgpsB cells” (fleurie2014interplayofthe pages 1-2) | High. Useful regulatory edge; taxon-specific. |
| Methicillin / PBP2x inhibition | causes | cell elongation | Streptococci/ovococci review synthesis | 10.21775/cimb.032.259 | “PBP2x inhibition by β-lactam antibiotics (methicillin) causes cell elongation” (xiang2019regulationofcell pages 19-24) | Medium. From review summary rather than quoted primary result; useful as perturbational edge with caution. |
| MapZ | positions / guides migration of | FtsZ rings at future equators | *Streptococcus pneumoniae*; cell-cycle localization synthesis | 10.1111/mmi.14659 | “Some FtsZ and associated proteins EzrA and FtsA move outward continuously with MapZ from the septal ring toward the positions of the future equatorial rings in daughter cells” (perez2021organizationofpeptidoglycan pages 1-5) | Medium-High. Strong localization statement; curate as positioning role in pneumococcus. |
| MapZ | stabilizes / anchors | Z-ring / FtsZ | Streptococci review | 10.21775/cimb.032.259 | “MapZ, a transmembrane protein, localizes as rings at division sites and serves as a molecular beacon, with its cytoplasmic domain anchoring FtsZ” (xiang2019regulationofcell pages 19-24) | Medium. Review-derived summary; good candidate but prefer primary MapZ paper if curating definitive edge. |
| New PG / TP activity at midcell | separates into | concentric outer peripheral ring and inner septal ring | *Streptococcus pneumoniae*; 3D-SIM vertical imaging | 10.1111/mmi.14659 | “areas of new transpeptidase (TP) activity catalyzed by penicillin-binding proteins (PBPs) separate into a pair of concentric rings early in division, representing peripheral PG (pPG) synthesis (outer ring) and the leading-edge (inner ring) of septal PG (sPG) synthesis” (perez2021organizationofpeptidoglycan pages 1-5) | High. Strong spatial organization edge supporting oval-shape mechanism. |
| Septal and peripheral PG syntheses | start together / proceed separately in space | ovococcal morphogenesis program | *Streptococcus pneumoniae*; dSTORM and modeling | 10.1016/j.cub.2021.04.041 | “septal and peripheral peptidoglycan syntheses first occur within a single annular region that later separates in two concentric regions” (trouve2021nanoscaledynamicsof pages 1-3) | High. Strong recent mechanistic evidence. |
| Septal PG synthesis | begins from start of cell cycle and is remodeled | throughout cell cycle | *Streptococcus pneumoniae*; dSTORM and modeling | 10.1016/j.cub.2021.04.041 | “septal peptidoglycan is synthesized from the beginning of the cell cycle and is constantly remodeled” (trouve2021nanoscaledynamicsof pages 1-3) | High. Supports dynamic morphogenesis edges, though remodeling agent identities may need separate evidence. |


*Table: This table compiles the strongest curation-ready causal edges for ovococcal/oval bacterial morphology, emphasizing peptidoglycan synthesis, divisome/elongasome organization, and regulator perturbations. It preserves species specificity and flags inferred mechanisms that need caution before TraitMech curation.*

### Recommended minimal graph backbone

For a conservative first revision of `oval_shaped.yaml`, the strongest backbone is:

1. **RodA–PBP2b complex → enables → peripheral PG synthesis**.
2. **Peripheral PG synthesis → promotes → longitudinal cell elongation**.
3. **FtsW–PBP2x complex → enables → septal PG synthesis**.
4. **Septal PG synthesis → produces → daughter-cell cross-wall/invagination**.
5. **Balanced, concurrent pPG and sPG synthesis at midcell → produces/maintains → METPO:1000678**.
6. **FtsZ ring → organizes → midcell wall-synthesis machinery**.
7. **MapZ → positions → FtsZ/future equatorial rings**.
8. **DivIVA → promotes → peripheral PG synthesis**.
9. **MltG → supports → peripheral PG synthesis/cell elongation**.
10. **Loss of peripheral PG synthesis → decreases → aspect ratio**, yielding rounder cells.

Edges 1 and 3 should be qualified as pneumococcal/ovococcal rather than universal. The spatial separation into outer pPG and inner sPG rings is directly supported by 3D-SIM, while dSTORM supports simultaneous early activity and continued peripheral synthesis after septal completion. (trouve2021nanoscaledynamicsof pages 9-10, trouve2021nanoscaledynamicsof pages 1-3, perez2021organizationofpeptidoglycan pages 1-5)

## 5. Recent developments, applications, and quantitative evidence

### 2023–2024 developments

The most important 2023 mechanistic advance was the demonstration in *S. suis* that DivIVA phosphorylation regulates pPG synthesis through an interaction/localization axis involving MltG. DivIVA deletion nearly halted peripheral synthesis; phospho-null DivIVA3A produced longer peripheral PG and longer cells, whereas phosphomimetic DivIVA3E produced shorter peripheral PG and shorter/wider cells. STK-dependent sites reported for *S. suis* DivIVA were S145, T199, and T211. The authors directly established phosphorylation-dependent interaction and localization effects, but the final proposition that phosphorylation actively terminates pPG synthesis before septal synthesis is a hypothesis and should remain uncertain. (jiang2023divivainteractswith pages 1-2, jiang2023divivainteractswith pages 4-6, jiang2023divivainteractswith pages 9-11)

A separate 2023 study connected morphogenesis to envelope assembly: the pneumococcal divisome, rather than the elongasome, recruits the capsule-synthesis complex. Re-routing CpsC to poles redirected capsule production and exposed the septal region to complement deposition. This is useful as a downstream real-world/virulence branch—**divisome organization → septal capsule placement → complement evasion**—but it is not evidence that capsule itself causes oval shape. (nakamoto2023thedivisomebut pages 6-7, nakamoto2023thedivisomebut pages 1-2)

A June 2024 PNAS report, **“Elongasome core proteins and class A PBP1a display zonal, processive movement at the midcell of *Streptococcus pneumoniae*,”** DOI [10.1073/pnas.2401831121](https://doi.org/10.1073/pnas.2401831121), is highly relevant to updating movement/processivity edges. Its full text was not available in this retrieval, so detailed claims from it should not yet be added solely from metadata.

### Quantitative findings

In *S. suis*, deleting *msmK* reduced mean length from **1.056 ± 0.14 μm** to **0.896 ± 0.20 μm** and reduced length-to-width ratio from **1.586 ± 0.21** to **1.356 ± 0.28**, while width did not significantly change. Cells below 0.8 μm constituted **26.99%** of the mutant but **0%** of wild type. Chains of at least three cells increased from **4.8% (14/290)** to **28.9% (108/374)**. These data strongly support `MsmK → peripheral PG synthesis/cell elongation → oval shape`, although MsmK should presently be treated as an *S. suis*-specific contributor. (tan2021streptococcussuismsmk pages 8-11)

In pneumococcal Δ*gpsB* cells, **25.2%** displayed zig-zag/helical FtsZ localization, while DivIVA had a helical pattern in **20.1%** and EzrA in **19.9%** of elongated mutant cells. The Δ*divIVA* Δ*gpsB* double mutant resembled the rounded Δ*divIVA* phenotype in **97.9%** of cells, supporting the conclusion that DivIVA-driven elongation is epistatic to the elongated Δ*gpsB* phenotype. (fleurie2014interplayofthe pages 4-7)

The nanoscale PG study analyzed radial septal-labeling widths in two pneumococcal backgrounds, including **238 R800** and **171 D39Δcps** cells, and supported a model in which septal and peripheral synthesis begin early and later become spatially separated. These measurements argue against curating a simple obligatory temporal switch as the sole ovococcal mechanism. (trouve2021nanoscaledynamicsof pages 9-10, trouve2021nanoscaledynamicsof pages 1-3)

### Applications and expert interpretation

* **Antimicrobial target discovery:** PG synthases, SEDS–PBP pairs, FtsZ organization, StkP signaling, and MltG-mediated remodeling are attractive targets because disrupting their balance causes elongation, rounding, failed septation, or nonviability. β-Lactam inhibition of PBP2x produces elongation and is a useful chemical-genetic probe, although β-lactams have multiple context-dependent targets. (xiang2019regulationofcell pages 19-24, jiang2023divivainteractswith pages 1-2)
* **Diagnostic morphometry:** aspect ratio, long-axis length, chaining, and FDAA incorporation can serve as quantitative phenotypes in antimicrobial screens. Shape alone is insufficient to identify the molecular lesion.
* **Virulence research:** PG architecture affects surface display, chaining, colonization, and capsule coverage. The 2023 capsule study shows that spatially correct septal capsule synthesis protects vulnerable envelope regions from complement. (nakamoto2023thedivisomebut pages 6-7, nakamoto2023thedivisomebut pages 1-2, perez2021organizationofpeptidoglycan pages 1-5)
* **Expert consensus:** current evidence favors overlapping, dynamically separating pPG and sPG programs, not a universal binary switch. The exact balance, essentiality, and regulatory wiring are strain dependent. (trouve2021nanoscaledynamicsof pages 1-3, fleurie2014interplayofthe pages 10-11)

## 6. Curation warnings

1. **Do not generalize streptococcal mechanisms to every oval bacterium.** The proposed graph should carry taxon constraints such as *S. pneumoniae*, *S. suis*, or ovococcal Firmicutes.
2. **Do not curate “DivIVA phosphorylation terminates pPG synthesis through MltG mislocalization” as established fact.** Interaction and mislocalization are direct; termination is explicitly hypothesized. (jiang2023divivainteractswith pages 9-11)
3. **Do not treat localization as sufficient proof of catalytic causation.** PBP2b/FtsX outer-ring and PBP2x/FtsZ inner-ring observations strongly assign function but should be combined with depletion/inhibition evidence. (perez2021organizationofpeptidoglycan pages 1-5)
4. **Do not encode an obligatory sequential pPG→sPG switch.** dSTORM indicates early concomitant synthesis, later concentric separation, and persistent elongation after septal completion. (trouve2021nanoscaledynamicsof pages 1-3)
5. **Do not merge chaining with shape.** Separation defects can increase chains without directly changing individual-cell ovality.
6. **Do not use FDAA probes as native metabolites in the causal graph.** They are assay reagents reporting nascent PG incorporation.
7. **Do not assign protein CURIEs without strain resolution.** Gene names recur across taxa, and experimental strains can differ in suppressor alleles and essentiality.
8. **Treat methicillin→PBP2x→elongation as medium confidence until linked to the primary dose/target experiment.** The retrieved support is review-level. (xiang2019regulationofcell pages 19-24)
9. **Exclude capsule from the minimal shape mechanism.** Capsule organization is an important downstream implementation but the 2023 study did not show that capsule determines ovality. (nakamoto2023thedivisomebut pages 6-7)
10. **Do not curate detailed 2024 processivity edges from title/metadata alone.** Obtain and review the full PNAS article first.

## 7. DOI-first bibliography

1. **Jiang Q. et al.** “DivIVA Interacts with the Cell Wall Hydrolase MltG To Regulate Peptidoglycan Synthesis in *Streptococcus suis*.” *Microbiology Spectrum* 11, published **22 May 2023**. DOI: [10.1128/spectrum.04750-22](https://doi.org/10.1128/spectrum.04750-22). (jiang2023divivainteractswith pages 1-2)
2. **Nakamoto R. et al.** “The divisome but not the elongasome organizes capsule synthesis in *Streptococcus pneumoniae*.” *Nature Communications* 14:3170, accepted **16 May 2023**, published June 2023. DOI: [10.1038/s41467-023-38904-9](https://doi.org/10.1038/s41467-023-38904-9). (nakamoto2023thedivisomebut pages 1-2)
3. **Perez A.J. et al.** “Elongasome core proteins and class A PBP1a display zonal, processive movement at the midcell of *Streptococcus pneumoniae*.” *PNAS*, **June 2024**. DOI: [10.1073/pnas.2401831121](https://doi.org/10.1073/pnas.2401831121). Full text not evaluated here.
4. **Trouve J. et al.** “Nanoscale dynamics of peptidoglycan assembly during the cell cycle of *Streptococcus pneumoniae*.” *Current Biology* 31, published **12 July 2021**. DOI: [10.1016/j.cub.2021.04.041](https://doi.org/10.1016/j.cub.2021.04.041). (trouve2021nanoscaledynamicsof pages 1-3)
5. **Perez A.J. et al.** “Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of *Streptococcus pneumoniae*.” *Molecular Microbiology* 115:1152–1169, **2021**. DOI: [10.1111/mmi.14659](https://doi.org/10.1111/mmi.14659). (perez2021organizationofpeptidoglycan pages 1-5)
6. **Tan M.-F. et al.** “*Streptococcus suis* MsmK: Novel Cell Division Protein Interacting with FtsZ and Maintaining Cell Shape.” *mSphere* 6, published **17 March 2021**. DOI: [10.1128/mSphere.00119-21](https://doi.org/10.1128/mSphere.00119-21). (tan2021streptococcussuismsmk pages 1-2)
7. **Briggs N.S. et al.** “The Pneumococcal Divisome: Dynamic Control of *Streptococcus pneumoniae* Cell Division.” *Frontiers in Microbiology* 12, **October 2021**. DOI: [10.3389/fmicb.2021.737396](https://doi.org/10.3389/fmicb.2021.737396). (briggs2021thepneumococcaldivisome pages 2-3)
8. **Xiang Z. et al.** “Regulation of Cell Division in Streptococci: Comparing with the Model Rods.” *Current Issues in Molecular Biology* 32:259–326, **June 2019**. DOI: [10.21775/cimb.032.259](https://doi.org/10.21775/cimb.032.259). (xiang2019regulationofcell pages 19-24)
9. **David B. et al.** “PBP2b plays a key role in both peripheral growth and septum positioning in *Lactococcus lactis*.” *PLOS ONE* 13:e0198014, **May 2018**. DOI: [10.1371/journal.pone.0198014](https://doi.org/10.1371/journal.pone.0198014). (david2018pbp2bplaysa pages 1-2, david2018pbp2bplaysa pages 18-19)
10. **Fleurie A. et al.** “Interplay of the Serine/Threonine-Kinase StkP and the Paralogs DivIVA and GpsB in Pneumococcal Cell Elongation and Division.” *PLOS Genetics* 10:e1004275, published **10 April 2014**. DOI: [10.1371/journal.pgen.1004275](https://doi.org/10.1371/journal.pgen.1004275). (fleurie2014interplayofthe pages 1-2)
11. **Tsui H.-C.T. et al.** “Pbp2x localizes separately from Pbp2b and other peptidoglycan synthesis proteins during later stages of cell division of *Streptococcus pneumoniae* D39.” *Molecular Microbiology* 94:21–40, **October 2014**. DOI: [10.1111/mmi.12745](https://doi.org/10.1111/mmi.12745).

**Curation recommendation:** retain the existing 10-node/11-edge synthesis as a compact backbone, but update it to represent (i) concurrent and spatially separating pPG/sPG activities, (ii) the high-confidence DivIVA–MltG regulatory branch from 2023, and (iii) the *S. suis*-specific MsmK branch. Keep phosphorylation-triggered shutdown, capsule coupling, and 2024 processive-movement claims in an uncertain or extension layer until their exact causal scope is verified.

References

1. (tan2021streptococcussuismsmk pages 1-2): Mei-Fang Tan, Qiao Hu, Zhe Hu, Chun-Yan Zhang, Wan-Quan Liu, Ting Gao, Liang-Sheng Zhang, Lun Yao, Hai-Qin Li, Yan-Bin Zeng, and Rui Zhou. Streptococcus suis msmk: novel cell division protein interacting with ftsz and maintaining cell shape. mSphere, Apr 2021. URL: https://doi.org/10.1128/msphere.00119-21, doi:10.1128/msphere.00119-21. This article has 7 citations and is from a peer-reviewed journal.

2. (perez2021organizationofpeptidoglycan pages 1-5): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

3. (briggs2021thepneumococcaldivisome pages 2-3): Nicholas S. Briggs, Kevin E. Bruce, Souvik Naskar, Malcolm E. Winkler, and David I. Roper. The pneumococcal divisome: dynamic control of streptococcus pneumoniae cell division. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.737396, doi:10.3389/fmicb.2021.737396. This article has 42 citations and is from a peer-reviewed journal.

4. (trouve2021nanoscaledynamicsof pages 1-3): Jennyfer Trouve, André Zapun, Christopher Arthaud, Claire Durmort, Anne Marie Di Guilmi, Bill Söderström, Anais Pelletier, Christophe Grangeasse, Dominique Bourgeois, Yung-Sing Wong, and Cecile Morlot. Nanoscale dynamics of peptidoglycan assembly during the cell cycle of streptococcus pneumoniae. Current Biology, 31:2844-2856.e6, Jul 2021. URL: https://doi.org/10.1016/j.cub.2021.04.041, doi:10.1016/j.cub.2021.04.041. This article has 46 citations and is from a highest quality peer-reviewed journal.

5. (tan2021streptococcussuismsmk pages 8-11): Mei-Fang Tan, Qiao Hu, Zhe Hu, Chun-Yan Zhang, Wan-Quan Liu, Ting Gao, Liang-Sheng Zhang, Lun Yao, Hai-Qin Li, Yan-Bin Zeng, and Rui Zhou. Streptococcus suis msmk: novel cell division protein interacting with ftsz and maintaining cell shape. mSphere, Apr 2021. URL: https://doi.org/10.1128/msphere.00119-21, doi:10.1128/msphere.00119-21. This article has 7 citations and is from a peer-reviewed journal.

6. (jiang2023divivainteractswith pages 1-2): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 14 citations and is from a domain leading peer-reviewed journal.

7. (jiang2023divivainteractswith pages 9-11): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 14 citations and is from a domain leading peer-reviewed journal.

8. (xiang2019regulationofcell pages 19-24): Zhenting Xiang, Zongbo Li, Jumei Zeng, Yuqing Li, and Jiyao Li. Regulation of cell division in streptococci: comparing with the model rods. Current issues in molecular biology, 32:259-326, Jun 2019. URL: https://doi.org/10.21775/cimb.032.259, doi:10.21775/cimb.032.259. This article has 3 citations.

9. (fleurie2014interplayofthe pages 1-2): Aurore Fleurie, Sylvie Manuse, Chao Zhao, Nathalie Campo, Caroline Cluzel, Jean-Pierre Lavergne, Céline Freton, Christophe Combet, Sébastien Guiral, Boumediene Soufi, Boris Macek, Erkin Kuru, Michael S. VanNieuwenhze, Yves V. Brun, Anne-Marie Di Guilmi, Jean-Pierre Claverys, Anne Galinier, and Christophe Grangeasse. Interplay of the serine/threonine-kinase stkp and the paralogs diviva and gpsb in pneumococcal cell elongation and division. PLoS Genetics, 10:e1004275, Apr 2014. URL: https://doi.org/10.1371/journal.pgen.1004275, doi:10.1371/journal.pgen.1004275. This article has 205 citations and is from a domain leading peer-reviewed journal.

10. (fleurie2014interplayofthe pages 10-11): Aurore Fleurie, Sylvie Manuse, Chao Zhao, Nathalie Campo, Caroline Cluzel, Jean-Pierre Lavergne, Céline Freton, Christophe Combet, Sébastien Guiral, Boumediene Soufi, Boris Macek, Erkin Kuru, Michael S. VanNieuwenhze, Yves V. Brun, Anne-Marie Di Guilmi, Jean-Pierre Claverys, Anne Galinier, and Christophe Grangeasse. Interplay of the serine/threonine-kinase stkp and the paralogs diviva and gpsb in pneumococcal cell elongation and division. PLoS Genetics, 10:e1004275, Apr 2014. URL: https://doi.org/10.1371/journal.pgen.1004275, doi:10.1371/journal.pgen.1004275. This article has 205 citations and is from a domain leading peer-reviewed journal.

11. (jiang2023divivainteractswith pages 4-6): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 14 citations and is from a domain leading peer-reviewed journal.

12. (trouve2021nanoscaledynamicsof pages 9-10): Jennyfer Trouve, André Zapun, Christopher Arthaud, Claire Durmort, Anne Marie Di Guilmi, Bill Söderström, Anais Pelletier, Christophe Grangeasse, Dominique Bourgeois, Yung-Sing Wong, and Cecile Morlot. Nanoscale dynamics of peptidoglycan assembly during the cell cycle of streptococcus pneumoniae. Current Biology, 31:2844-2856.e6, Jul 2021. URL: https://doi.org/10.1016/j.cub.2021.04.041, doi:10.1016/j.cub.2021.04.041. This article has 46 citations and is from a highest quality peer-reviewed journal.

13. (nakamoto2023thedivisomebut pages 6-7): Rei Nakamoto, Sarp Bamyaci, Karin Blomqvist, Staffan Normark, Birgitta Henriques-Normark, and Lok-To Sham. The divisome but not the elongasome organizes capsule synthesis in streptococcus pneumoniae. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38904-9, doi:10.1038/s41467-023-38904-9. This article has 14 citations and is from a highest quality peer-reviewed journal.

14. (nakamoto2023thedivisomebut pages 1-2): Rei Nakamoto, Sarp Bamyaci, Karin Blomqvist, Staffan Normark, Birgitta Henriques-Normark, and Lok-To Sham. The divisome but not the elongasome organizes capsule synthesis in streptococcus pneumoniae. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38904-9, doi:10.1038/s41467-023-38904-9. This article has 14 citations and is from a highest quality peer-reviewed journal.

15. (fleurie2014interplayofthe pages 4-7): Aurore Fleurie, Sylvie Manuse, Chao Zhao, Nathalie Campo, Caroline Cluzel, Jean-Pierre Lavergne, Céline Freton, Christophe Combet, Sébastien Guiral, Boumediene Soufi, Boris Macek, Erkin Kuru, Michael S. VanNieuwenhze, Yves V. Brun, Anne-Marie Di Guilmi, Jean-Pierre Claverys, Anne Galinier, and Christophe Grangeasse. Interplay of the serine/threonine-kinase stkp and the paralogs diviva and gpsb in pneumococcal cell elongation and division. PLoS Genetics, 10:e1004275, Apr 2014. URL: https://doi.org/10.1371/journal.pgen.1004275, doi:10.1371/journal.pgen.1004275. This article has 205 citations and is from a domain leading peer-reviewed journal.

16. (david2018pbp2bplaysa pages 1-2): Blandine David, Marie-Clémence Duchêne, Gabrielle Laurie Haustenne, Daniel Pérez-Núñez, Marie-Pierre Chapot-Chartier, Xavier De Bolle, Eric Guédon, Pascal Hols, and Bernard Hallet. Pbp2b plays a key role in both peripheral growth and septum positioning in lactococcus lactis. PLOS ONE, 13:e0198014, May 2018. URL: https://doi.org/10.1371/journal.pone.0198014, doi:10.1371/journal.pone.0198014. This article has 15 citations and is from a peer-reviewed journal.

17. (david2018pbp2bplaysa pages 18-19): Blandine David, Marie-Clémence Duchêne, Gabrielle Laurie Haustenne, Daniel Pérez-Núñez, Marie-Pierre Chapot-Chartier, Xavier De Bolle, Eric Guédon, Pascal Hols, and Bernard Hallet. Pbp2b plays a key role in both peripheral growth and septum positioning in lactococcus lactis. PLOS ONE, 13:e0198014, May 2018. URL: https://doi.org/10.1371/journal.pone.0198014, doi:10.1371/journal.pone.0198014. This article has 15 citations and is from a peer-reviewed journal.