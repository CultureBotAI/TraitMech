---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:43:45.644432'
end_time: '2026-08-04T09:53:32.594870'
duration_seconds: 586.95
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: ring shaped
  trait_identifier: METPO:1000680
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: ring_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism forms circular or toroidal structures.
  parent_traits: METPO:1000666
  synonyms: ring, ring-shaped
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell curvature (Cell-shape
    review supports curvature-generating wall patterning as the basis for closed-ring
    morphology.)'
  causal_graph_summary: 'ring_shaped_curved_growth_closure: 15 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ring shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000680
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms circular or toroidal structures.
- **Parent traits:** METPO:1000666
- **Synonyms:** ring, ring-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell curvature (Cell-shape review supports curvature-generating wall patterning as the basis for closed-ring morphology.)
- **Existing causal graph summary:** ring_shaped_curved_growth_closure: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **ring shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/ring_shaped.yaml`.

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
- **Trait label:** ring shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000680
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms circular or toroidal structures.
- **Parent traits:** METPO:1000666
- **Synonyms:** ring, ring-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell curvature (Cell-shape review supports curvature-generating wall patterning as the basis for closed-ring morphology.)
- **Existing causal graph summary:** ring_shaped_curved_growth_closure: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **ring shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/ring_shaped.yaml`.

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


# Curation-focused research report: microbial **ring shaped** morphology

## Executive assessment

**Target trait:** `METPO:1000680` (“ring shaped”); category **MORPHOLOGY**; parent `METPO:1000666`.

The defensible scope is a **whole microbial cell whose longitudinal axis closes, or nearly closes, into a circular/toroidal form**. The clearest historical taxonomic exemplar is *Rhodocyclus purpureus*, described in 1978 as “a ring-shaped, vitamin B12-requiring” bacterium (DOI below). However, the retrieved literature contains **no direct genetic or cell-biological dissection of ring closure in a naturally ring-shaped species**. The strongest experimentally established mechanism is therefore a taxon-specific precursor pathway from *Caulobacter crescentus*: membrane-associated crescentin imposes asymmetric mechanical constraint on the cell envelope, produces differential peptidoglycan growth, and generates curvature. Extending that mechanism from an open curved rod to a closed ring is biologically plausible but presently **inferred, not demonstrated**.

The highest-priority recent result is a 2023 study of the MreB-less alphaproteobacterium *Rhodomicrobium vannielii*. It shows that bactofilins localize at active hyphal growth zones and that deleting **bacA** produces kinked or buckled hyphae. This advances understanding of localized cell-wall growth without MreB, but it neither produces nor explains a closed-ring cell and should remain comparative evidence only. The study examined 100 cells per deletion condition and found that all deletions involving **bacA** phenocopied the single deletion, whereas **bacB/bacC** loss did not appreciably deform hyphae. (richter2023interactingbactofilinsimpact pages 4-5, richter2023interactingbactofilinsimpact pages 13-15, richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 5-7)

## 1. Trait scope and boundary cases

### Included phenotype

A positive annotation should require microscopy or an authoritative taxonomic description showing that an **individual cell** forms a closed or nearly closed circle/toroid. A highly curved cell with visibly approaching ends may be admitted only if the project explicitly treats “ring-shaped” as including near-closure; otherwise it should be annotated as curved and marked as a candidate precursor.

### Excluded or separately represented phenomena

- **Curved rods/crescents:** open arcs such as ordinary *C. crescentus* cells. These supply mechanistic evidence for curvature but are not themselves `METPO:1000680`.
- **Helical or spiral cells:** curvature rotates along the longitudinal axis and does not necessarily yield a planar closed circle.
- **Intracellular Z-rings/FtsZ toroids:** division machinery inside a cell, not whole-cell morphology.
- **Ring-shaped proteins, pores, nucleoids, S-layers, or other subcellular structures:** molecular or intracellular architecture rather than organismal cell shape.
- **Annular colonies or biofilm patterns:** population-level spatial organization rather than single-cell morphology.
- **Division-stage constrictions, coccal packets, and cell chains arranged in circles:** transient or multicellular arrangements unless the individual cell body is demonstrably toroidal.

This distinction is important because literature searches for “ring-shaped bacterium” are dominated by ring-shaped molecular assemblies rather than whole-cell rings.

## 2. Current mechanistic understanding

### Best-supported causal model: asymmetric growth under mechanical constraint

In *C. crescentus*, CreS/crescentin forms an intermediate-filament-like structure at the inner curvature. **creS** deletion yields straight rods, and curvature emerges or disappears only as the peptidoglycan wall is remodeled during growth. (woldemeskel2017shapeshiftingtosurvive pages 5-6, woldemeskel2017shapeshiftingtosurvive pages 2-5)

The foundational 2009 study provides several mutually reinforcing experiments:

1. When crescentin detached from the envelope after mecillinam-mediated wall weakening, it collapsed into left-handed helices in **116 cells**, with pitch **1.4 ± 0.15 μm**. This supports the interpretation that envelope-associated crescentin is normally mechanically strained. (cabeen2009bacterialcellcurvature pages 2-3)
2. Disrupting crescentin with a dominant-negative variant progressively straightened growing cells, but chloramphenicol-mediated growth arrest prevented curvature loss for at least **8 h**. Thus wall growth/remodeling, rather than instantaneous elastic bending alone, is required. (cabeen2009bacterialcellcurvature pages 2-3)
3. D-cysteine pulse–chase labeling produced rectangular clearing patterns in straight Δ**creS** cells but trapezoidal patterns in hypercurved, crescentin-overproducing cells. Longer outer-curvature clearing indicated faster extension outside than at the crescentin-proximal inner face. (cabeen2009bacterialcellcurvature pages 6-7, cabeen2009bacterialcellcurvature pages 4-6)
4. Isolated sacculi retained the corresponding curvature, while muropeptide composition, wall thickness, and cross-linking did not explain the shape difference. This favors differential growth kinetics over a grossly different wall material. (cabeen2009bacterialcellcurvature pages 4-6)
5. Curved microchambers could impose stable curvature on otherwise straight cells, showing that external mechanical constraint can likewise bias cell-wall growth. Crescentin expression in *E. coli* was also sufficient to induce curvature. (cabeen2009bacterialcellcurvature pages 1-2)

The resulting expert model is:

**CreS polymerization → envelope-associated crescentin → localized compressive constraint → slower peptidoglycan extension at the inner face → circumferential growth-rate differential → cell curvature.**

A mathematical estimate discussed in the study suggested that forces on the order of **8 pN** could promote peptidoglycan cross-bridge cleavage, although this value belongs to the proposed mechanical model rather than a direct measurement of force in a naturally ring-shaped organism. (cabeen2009bacterialcellcurvature pages 9-10)

### Envelope composition as an upstream modulator

The *C. crescentus* **wbqL** locus encodes a predicted glycosyltransferase involved in O-polysaccharide/LPS biogenesis. Transposon disruption or the W138R substitution generated aberrant, predominantly shorter O-polysaccharide species and reduced curvature from approximately **0.39 μm⁻¹** in wild type to **0.11 μm⁻¹** in straight mutants. Crescentin was still produced and polymerized, but its structures became cytoplasmic/S-shaped rather than properly associated with the envelope. (cabeen2010mutationsinthe pages 7-8, cabeen2010mutationsinthe pages 5-7, cabeen2010mutationsinthe pages 3-5)

A **wbqP wbqL** double mutant lacking O-polysaccharide altogether retained curvature, arguing that the causal factor is accumulation of an aberrant product rather than simple absence of normal O-polysaccharide or S-layer attachment. The precise molecular link between aberrant O-polysaccharide and crescentin detachment remains unresolved. (cabeen2010mutationsinthe pages 1-2, cabeen2010mutationsinthe pages 5-7, sundararajan2017cytoskeletalproteinsin pages 16-17)

### Recent comparative development: MreB-independent morphogenesis

Richter and colleagues showed in 2023 that *R. vannielii* lacks MreB but has three bactofilins, BacA, BacB, and BacC. BacA localizes at hyphal tips and branch sites, coincident with discrete sites of peptidoglycan incorporation. Δ**bacA** hyphae become kinked or buckled without a major change in length or overall growth; deleting **bacB** or **bacC** alone has little detectable effect. BacA also interacts with BacC and is required for proper BacC localization. (richter2023interactingbactofilinsimpact pages 4-5, richter2023interactingbactofilinsimpact pages 13-15, richter2023interactingbactofilinsimpact pages 5-7)

This establishes that a static cytoskeletal scaffold can organize localized wall growth and shape in an MreB-less alphaproteobacterium. It does **not** establish that bactofilins generate rings, nor that *R. purpureus* uses homologous machinery.

## 3. Candidate nodes grouped by type

### Trait and shape states

- **ring-shaped whole cell** — `METPO:1000680`
- **curved cell / increased longitudinal curvature** — candidate intermediate; retain the established METPO term if available rather than inventing a CURIE
- **straight rod** — comparison/negative phenotype; ontology grounding should be resolved against METPO
- **closed-ring formation / ring closure** — label-only biological process pending a suitable ontology term

### Genes and proteins

- **creS / crescentin (CreS)** — taxon-specific *C. crescentus* cytoskeletal protein; stable gene/protein CURIE should be resolved against the exact strain record before curation
- **wbqL (cc_0631)** — predicted glycosyltransferase in O-polysaccharide biosynthesis; strain-specific identifier should be verified
- **wbqP** — O-polysaccharide-pathway gene used in epistasis/double-mutant evidence
- **bacA, bacB, bacC / BacA, BacB, BacC** of *R. vannielii* — bactofilins; comparative rather than ring-specific nodes
- **MreB** — actin-like cytoskeletal protein; informative absence in *R. vannielii*, but no direct ring-shape edge was recovered

### Structures and cellular locations

- crescentin filament/structure
- cytoplasmic membrane
- cell envelope
- inner/concave cell face
- outer/convex cell face
- peptidoglycan sacculus
- hyphal tip and branch growth zone

Suggested GO grounding, subject to curator validation:

- **peptidoglycan biosynthetic process** — `GO:0009252`
- **cell-wall organization or biogenesis** — `GO:0071554`
- **cytoplasmic membrane** and **cell wall** — use the taxonomically appropriate GO cellular-component terms after checking the target organism’s envelope architecture

### Chemicals and experimental factors

- peptidoglycan — chemical/polymer node; verify the preferred ChEBI representation
- lipopolysaccharide and O-polysaccharide — verify exact ChEBI terms because the experimentally implicated species is an aberrant biosynthetic product, not generic LPS
- D-cysteine — pulse–chase label for wall insertion, assay factor rather than endogenous causal requirement
- mecillinam — wall-weakening perturbation used to detach crescentin
- chloramphenicol — growth-arrest perturbation; `CHEBI:17698`
- curved microchamber / external mechanical confinement — experimental factor

### Biological and mechanical processes

- crescentin polymerization
- crescentin–envelope attachment
- localized compressive force/mechanical strain
- peptidoglycan insertion and remodeling
- differential inner-versus-outer sidewall elongation
- longitudinal cell growth
- cell curvature generation
- hypothetical progressive curvature to ring closure
- O-polysaccharide biosynthesis
- bactofilin-directed localization of hyphal growth

## 4. Candidate causal graph

The compact curation scaffold is shown below.

| subject | predicate | object | evidence tier | taxon/assay | DOI |
|---|---|---|---|---|---|
| CreS (crescentin) polymerization | enables formation of | crescentin filament/structure | direct | *Caulobacter crescentus*; genetics, microscopy (sundararajan2017cytoskeletalproteinsin pages 16-17, cabeen2009bacterialcellcurvature pages 1-2) | 10.1038/emboj.2009.61; 10.1007/978-3-319-53047-5\_4 |
| crescentin membrane/envelope attachment | causes | localized compressive constraint on cell envelope | direct | *C. crescentus*; membrane detachment and morphology assays (cabeen2009bacterialcellcurvature pages 2-3, cabeen2010mutationsinthe pages 1-2) | 10.1038/emboj.2009.61; 10.1128/jb.01371-09 |
| localized compressive constraint at inner curvature | reduces | inner-side peptidoglycan insertion/elongation rate | direct | *C. crescentus*; D-Cys pulse-chase PG labeling (cabeen2009bacterialcellcurvature pages 6-7, cabeen2009bacterialcellcurvature pages 4-6) | 10.1038/emboj.2009.61 |
| circumferential differential peptidoglycan growth | causes | cell curvature | direct | *C. crescentus*; sacculus analysis, PG labeling, modeling (cabeen2009bacterialcellcurvature pages 6-7, cabeen2009bacterialcellcurvature pages 4-6, cabeen2009bacterialcellcurvature pages 9-10) | 10.1038/emboj.2009.61 |
| continued longitudinal growth of a curved cell | may culminate in | whole-cell ring closure | inferred/uncertain | generalized morphogenetic extrapolation from curvature mechanism; not directly shown for closed toroids (cabeen2009bacterialcellcurvature pages 6-7, cabeen2009bacterialcellcurvature pages 4-6) | 10.1038/emboj.2009.61 |
| creS deletion | results in | straight rods / loss of curvature | direct | *C. crescentus*; mutant phenotype (woldemeskel2017shapeshiftingtosurvive pages 5-6, woldemeskel2017shapeshiftingtosurvive pages 2-5) | 10.1016/j.tim.2017.03.006 |
| chloramphenicol treatment / growth arrest | blocks | curvature change after crescentin disruption | direct | *C. crescentus*; dominant-negative crescentin plus growth arrest assay (cabeen2009bacterialcellcurvature pages 2-3) | 10.1038/emboj.2009.61 |
| wbqL mutation | causes | aberrant O-polysaccharide | direct | *C. crescentus*; LPS pathway mutant analysis (cabeen2010mutationsinthe pages 1-2, cabeen2010mutationsinthe pages 5-7, cabeen2010mutationsinthe pages 3-5) | 10.1128/jb.01371-09 |
| aberrant O-polysaccharide | causes | crescentin-envelope dissociation/mislocalization | direct | *C. crescentus*; envelope association phenotype (cabeen2010mutationsinthe pages 1-2, cabeen2010mutationsinthe pages 7-8, cabeen2010mutationsinthe pages 5-7) | 10.1128/jb.01371-09 |
| crescentin-envelope dissociation | reduces | cell curvature | direct | *C. crescentus*; curvature loss in *wbqL* mutants (cabeen2010mutationsinthe pages 1-2, cabeen2010mutationsinthe pages 7-8) | 10.1128/jb.01371-09 |
| BacA localization at hyphal growth zones | associates with | site-specific peptidoglycan growth/hyphal morphogenesis | direct, indirect for ring trait | *Rhodomicrobium vannielii*; localization and PG incorporation (richter2023interactingbactofilinsimpact pages 13-15, richter2023interactingbactofilinsimpact pages 1-2) | 10.1371/journal.pgen.1010788 |
| bacA deletion | results in | kinked/buckled hyphae | direct, indirect for ring trait | *R. vannielii*; deletion phenotype (richter2023interactingbactofilinsimpact pages 5-7) | 10.1371/journal.pgen.1010788 |


*Table: This table summarizes candidate TraitMech causal edges relevant to whole-cell ring-shaped morphology, emphasizing directly supported curvature mechanisms and clearly flagging inferred or indirect edges. It is useful as a compact curation scaffold for deciding which nodes and edges are ready for inclusion versus which remain uncertain.*

### Edge-level evidence notes and supporting snippets

| Proposed triple | Supporting source snippet or result | Curation note |
|---|---|---|
| **creS deletion → causes → straight-cell phenotype** | Review evidence: cells with a **creS** deletion “grow as straight rods.” | **Curate for curvature**, taxon-specific to *C. crescentus*; do not map directly to loss of a closed ring. (woldemeskel2017shapeshiftingtosurvive pages 5-6) |
| **CreS polymerization → enables → crescentin structure** | Nonpolymerizing variants fail to assemble in vivo and yield straight cells. | Direct genetic/assembly evidence. (sundararajan2017cytoskeletalproteinsin pages 16-17) |
| **crescentin-envelope attachment → enables → curvature generation** | A membrane-dissociated CreSΔN27 variant polymerizes but cells remain straight; detached native structures collapse into helices. | Strong direct evidence that polymerization alone is insufficient. (sundararajan2017cytoskeletalproteinsin pages 16-17, cabeen2009bacterialcellcurvature pages 2-3) |
| **envelope-associated crescentin → imposes → localized mechanical constraint** | Detached crescentin adopted a helix with pitch **1.4 ± 0.15 μm** in **n=116** cells. | Mechanical interpretation is strongly supported, though force was not directly measured in ring-shaped cells. (cabeen2009bacterialcellcurvature pages 2-3) |
| **localized constraint → reduces → inner-face PG growth** | D-cysteine pulse–chase patterns were shortest at the crescentin-bearing inner curvature and longest outside. | Strong direct assay evidence. (cabeen2009bacterialcellcurvature pages 6-7, cabeen2009bacterialcellcurvature pages 4-6) |
| **differential PG growth → causes → cell curvature** | Curved sacculi retained shape without corresponding gross changes in PG composition, thickness, or cross-linking. | Strong mechanistic edge in *C. crescentus*. (cabeen2009bacterialcellcurvature pages 4-6) |
| **longitudinal growth → required_for → curvature remodeling** | After dominant-negative CreS disruption, growing cells straightened, whereas chloramphenicol-treated cells did not change curvature over **8 h**. | Curate growth dependence; chloramphenicol is an experimental inhibitor, not a natural determinant. (cabeen2009bacterialcellcurvature pages 2-3) |
| **external curved confinement → promotes → curved growth** | Straight cells grown in curved microchambers acquired and maintained curvature. | Assay-specific evidence that mechanical force can substitute for an intrinsic scaffold. (sundararajan2017cytoskeletalproteinsin pages 16-17, cabeen2009bacterialcellcurvature pages 1-2) |
| **wbqL mutation → produces → aberrant O-polysaccharide** | W138R or disruptive mutations caused heterogeneous, predominantly shorter O-polysaccharide. | Direct, *C. crescentus*-specific. (cabeen2010mutationsinthe pages 5-7, cabeen2010mutationsinthe pages 3-5) |
| **aberrant O-polysaccharide → disrupts → crescentin-envelope association** | Crescentin remained expressed and polymerized but formed cytoplasmic/S-shaped structures; an O-polysaccharide-null double mutant retained curvature. | Curate with an uncertainty qualifier because the molecular intermediary is unknown. (cabeen2010mutationsinthe pages 1-2, cabeen2010mutationsinthe pages 7-8, cabeen2010mutationsinthe pages 5-7) |
| **crescentin detachment → reduces → curvature** | **wbqL** mutants fell from about **0.39 to 0.11 μm⁻¹** curvature. | Strong phenotype association, but not ring-specific. (cabeen2010mutationsinthe pages 7-8, cabeen2010mutationsinthe pages 3-5) |
| **BacA → localizes_at → hyphal PG-growth zones** | BacA appears at tips and branch sites coincident with discrete PG incorporation. | Direct 2023 result; comparative node only. (richter2023interactingbactofilinsimpact pages 13-15, richter2023interactingbactofilinsimpact pages 1-2) |
| **bacA deletion → causes → kinked/buckled hyphae** | Δ**bacA** and every combination containing Δ**bacA** were deformed; hyphal length remained normal; **100 cells/condition** were analyzed. | Direct but not evidence for closed-ring morphology. (richter2023interactingbactofilinsimpact pages 5-7) |
| **progressive asymmetric growth → causes → ring closure** | No retrieved study directly observed this transition in a naturally ring-shaped species. | **Do not curate as established.** At most encode as `inferred` or `hypothesized`, with the 2009 curvature mechanism as indirect support. |

## 5. Recommended YAML-level graph policy

### Suitable for curation now

A conservative `ring_shaped.yaml` may include the following as a **generic precursor module**, while explicitly recording the evidence organism:

1. crescentin structure — `located_at/attached_to` → cell envelope;
2. crescentin structure — `imposes` → localized mechanical constraint;
3. localized mechanical constraint — `decreases` → inner-face peptidoglycan extension;
4. inner/outer differential peptidoglycan extension — `causes` → cell curvature;
5. cell growth/peptidoglycan remodeling — `required_for` → curvature development.

The phenotype terminal should preferably remain **curvature**, not `METPO:1000680`, unless the final edge is explicitly marked as inferred. The **wbqL** branch may be included as negative/modulatory evidence, with a note that aberrant O-polysaccharide—not total O-polysaccharide absence—disrupts crescentin-envelope association.

### Not suitable for direct curation yet

- **crescentin causes ring-shaped morphology**: demonstrated only for curvature.
- **bactofilins cause ring-shaped morphology**: 2023 evidence concerns hyphal straightness and localized growth.
- **MreB absence causes rings**: absence in one complex-shaped species is not causal evidence.
- **Rhodocyclus ring formation requires vitamin B12**: the species was described as B12-requiring, but nutritional requirement and shape have not been causally linked.
- **FtsZ/Z-ring assembly causes whole-cell rings**: category error between division machinery and cell morphology.
- Any precise gene assignment to *R. purpureus* without genome-level orthology and perturbation evidence.

## 6. Evidence gaps and research priorities

1. Obtain time-lapse, three-dimensional microscopy of a verified ring-forming isolate to determine whether rings arise by progressive bending, end-to-end fusion, incomplete separation, or another developmental route.
2. Map spatial peptidoglycan insertion using fluorescent D-amino acids across open arcs and closed rings.
3. Sequence and perturb candidate cytoskeletal genes, bactofilins, envelope anchors, PG synthases, and hydrolases in the natural ring-forming taxon.
4. Quantify curvature, contour length, endpoint distance, closure frequency, growth rate, and cell-wall insertion asymmetry under controlled nutrients and physical confinement.
5. Test whether closed rings are stable vegetative cells, transient developmental states, stress morphologies, or microscopy/projection artifacts.

No 2023–2024 paper retrieved here directly answers those questions. The recent literature improves the general model of cytoskeleton-directed and MreB-independent morphogenesis, but the terminal ring-closure step remains an important evidence gap.

## 7. DOI-first bibliography

1. **Richter P, Melzer B, Müller FD.** “Interacting bactofilins impact cell shape of the MreB-less multicellular *Rhodomicrobium vannielii*.” *PLOS Genetics*. **May 2023**. DOI: [10.1371/journal.pgen.1010788](https://doi.org/10.1371/journal.pgen.1010788). (richter2023interactingbactofilinsimpact pages 4-5, richter2023interactingbactofilinsimpact pages 13-15, richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 5-7)
2. **Barrows JM, Goley ED.** “Synchronized Swarmers and Sticky Stalks: *Caulobacter crescentus* as a Model for Bacterial Cell Biology.” *Journal of Bacteriology* 205. **February 2023**. DOI: [10.1128/jb.00384-22](https://doi.org/10.1128/jb.00384-22). Recent authoritative context; no direct closed-ring mechanism was recovered.
3. **Cabeen MT et al.** “Bacterial cell curvature through mechanical control of cell growth.” *EMBO Journal* 28:1208–1219. **May 2009**. DOI: [10.1038/emboj.2009.61](https://doi.org/10.1038/emboj.2009.61). (cabeen2009bacterialcellcurvature pages 6-7, cabeen2009bacterialcellcurvature pages 4-6, cabeen2009bacterialcellcurvature pages 2-3, cabeen2009bacterialcellcurvature pages 1-2, cabeen2009bacterialcellcurvature pages 9-10)
4. **Cabeen MT et al.** “Mutations in the lipopolysaccharide biosynthesis pathway interfere with crescentin-mediated cell curvature in *Caulobacter crescentus*.” *Journal of Bacteriology* 192:3368–3378. **July 2010**. DOI: [10.1128/JB.01371-09](https://doi.org/10.1128/JB.01371-09). (cabeen2010mutationsinthe pages 1-2, cabeen2010mutationsinthe pages 7-8, cabeen2010mutationsinthe pages 5-7, cabeen2010mutationsinthe pages 3-5)
5. **Woldemeskel SA, Goley ED.** “Shapeshifting to Survive: Shape Determination and Regulation in *Caulobacter crescentus*.” *Trends in Microbiology* 25:673–687. **August 2017**. DOI: [10.1016/j.tim.2017.03.006](https://doi.org/10.1016/j.tim.2017.03.006). (woldemeskel2017shapeshiftingtosurvive pages 5-6, woldemeskel2017shapeshiftingtosurvive pages 2-5)
6. **Sundararajan K, Goley ED.** “Cytoskeletal Proteins in *Caulobacter crescentus*: Spatial Orchestrators of Cell Cycle Progression, Development, and Cell Shape.” *Subcellular Biochemistry* 84:103–137. **2017**. DOI: [10.1007/978-3-319-53047-5_4](https://doi.org/10.1007/978-3-319-53047-5_4). (sundararajan2017cytoskeletalproteinsin pages 16-17)
7. **Typas A, Banzhaf M, Gross CA, Vollmer W.** “From the regulation of peptidoglycan synthesis to bacterial growth and morphology.” *Annual Review of Cell and Developmental Biology* 28. **2012**. DOI: [10.1146/annurev-cellbio-101011-155745](https://doi.org/10.1146/annurev-cellbio-101011-155745). Supplied existing evidence; relevant as a broad wall-growth/shape review, not direct proof of ring closure.
8. **Pfennig N.** “*Rhodocyclus purpureus* gen. nov. and sp. nov., a ring-shaped, vitamin B12-requiring member of the family Rhodospirillaceae.” *International Journal of Systematic Bacteriology* 28:283–288. **April 1978**. DOI: [10.1099/00207713-28-2-283](https://doi.org/10.1099/00207713-28-2-283). This is the key phenotype-level taxonomic reference, but full-text mechanistic evidence was not available in the retrieved corpus.

## Final curation judgment

`METPO:1000680` is a valid, narrow morphology class, but its natural molecular mechanism remains underdetermined. The most defensible TraitMech graph should represent **mechanically biased peptidoglycan growth as a curvature-generating precursor**, retain *C. crescentus* and *R. vannielii* taxon qualifiers, and mark the final **curvature → closed-ring morphology** edge as uncertain. A direct natural-ring study is required before that terminal edge, crescentin, bactofilins, MreB status, or vitamin B12 dependence can be asserted as causal for the trait itself.

References

1. (richter2023interactingbactofilinsimpact pages 4-5): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

2. (richter2023interactingbactofilinsimpact pages 13-15): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (richter2023interactingbactofilinsimpact pages 1-2): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

4. (richter2023interactingbactofilinsimpact pages 5-7): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

5. (woldemeskel2017shapeshiftingtosurvive pages 5-6): Selamawit Abi Woldemeskel and Erin D. Goley. Shapeshifting to survive: shape determination and regulation in caulobacter crescentus. Trends in microbiology, 25 8:673-687, Aug 2017. URL: https://doi.org/10.1016/j.tim.2017.03.006, doi:10.1016/j.tim.2017.03.006. This article has 59 citations and is from a domain leading peer-reviewed journal.

6. (woldemeskel2017shapeshiftingtosurvive pages 2-5): Selamawit Abi Woldemeskel and Erin D. Goley. Shapeshifting to survive: shape determination and regulation in caulobacter crescentus. Trends in microbiology, 25 8:673-687, Aug 2017. URL: https://doi.org/10.1016/j.tim.2017.03.006, doi:10.1016/j.tim.2017.03.006. This article has 59 citations and is from a domain leading peer-reviewed journal.

7. (cabeen2009bacterialcellcurvature pages 2-3): Matthew T Cabeen, Godefroid Charbon, Waldemar Vollmer, Petra Born, Nora Ausmees, Douglas B Weibel, and Christine Jacobs-Wagner. Bacterial cell curvature through mechanical control of cell growth. The EMBO Journal, 28:1208-1219, May 2009. URL: https://doi.org/10.1038/emboj.2009.61, doi:10.1038/emboj.2009.61. This article has 203 citations.

8. (cabeen2009bacterialcellcurvature pages 6-7): Matthew T Cabeen, Godefroid Charbon, Waldemar Vollmer, Petra Born, Nora Ausmees, Douglas B Weibel, and Christine Jacobs-Wagner. Bacterial cell curvature through mechanical control of cell growth. The EMBO Journal, 28:1208-1219, May 2009. URL: https://doi.org/10.1038/emboj.2009.61, doi:10.1038/emboj.2009.61. This article has 203 citations.

9. (cabeen2009bacterialcellcurvature pages 4-6): Matthew T Cabeen, Godefroid Charbon, Waldemar Vollmer, Petra Born, Nora Ausmees, Douglas B Weibel, and Christine Jacobs-Wagner. Bacterial cell curvature through mechanical control of cell growth. The EMBO Journal, 28:1208-1219, May 2009. URL: https://doi.org/10.1038/emboj.2009.61, doi:10.1038/emboj.2009.61. This article has 203 citations.

10. (cabeen2009bacterialcellcurvature pages 1-2): Matthew T Cabeen, Godefroid Charbon, Waldemar Vollmer, Petra Born, Nora Ausmees, Douglas B Weibel, and Christine Jacobs-Wagner. Bacterial cell curvature through mechanical control of cell growth. The EMBO Journal, 28:1208-1219, May 2009. URL: https://doi.org/10.1038/emboj.2009.61, doi:10.1038/emboj.2009.61. This article has 203 citations.

11. (cabeen2009bacterialcellcurvature pages 9-10): Matthew T Cabeen, Godefroid Charbon, Waldemar Vollmer, Petra Born, Nora Ausmees, Douglas B Weibel, and Christine Jacobs-Wagner. Bacterial cell curvature through mechanical control of cell growth. The EMBO Journal, 28:1208-1219, May 2009. URL: https://doi.org/10.1038/emboj.2009.61, doi:10.1038/emboj.2009.61. This article has 203 citations.

12. (cabeen2010mutationsinthe pages 7-8): Matthew T. Cabeen, Michelle A. Murolo, Ariane Briegel, N. Khai Bui, Waldemar Vollmer, Nora Ausmees, Grant J. Jensen, and Christine Jacobs-Wagner. Mutations in the lipopolysaccharide biosynthesis pathway interfere with crescentin-mediated cell curvature in <i>caulobacter crescentus</i>. Journal of Bacteriology, 192:3368-3378, Jul 2010. URL: https://doi.org/10.1128/jb.01371-09, doi:10.1128/jb.01371-09. This article has 35 citations and is from a peer-reviewed journal.

13. (cabeen2010mutationsinthe pages 5-7): Matthew T. Cabeen, Michelle A. Murolo, Ariane Briegel, N. Khai Bui, Waldemar Vollmer, Nora Ausmees, Grant J. Jensen, and Christine Jacobs-Wagner. Mutations in the lipopolysaccharide biosynthesis pathway interfere with crescentin-mediated cell curvature in <i>caulobacter crescentus</i>. Journal of Bacteriology, 192:3368-3378, Jul 2010. URL: https://doi.org/10.1128/jb.01371-09, doi:10.1128/jb.01371-09. This article has 35 citations and is from a peer-reviewed journal.

14. (cabeen2010mutationsinthe pages 3-5): Matthew T. Cabeen, Michelle A. Murolo, Ariane Briegel, N. Khai Bui, Waldemar Vollmer, Nora Ausmees, Grant J. Jensen, and Christine Jacobs-Wagner. Mutations in the lipopolysaccharide biosynthesis pathway interfere with crescentin-mediated cell curvature in <i>caulobacter crescentus</i>. Journal of Bacteriology, 192:3368-3378, Jul 2010. URL: https://doi.org/10.1128/jb.01371-09, doi:10.1128/jb.01371-09. This article has 35 citations and is from a peer-reviewed journal.

15. (cabeen2010mutationsinthe pages 1-2): Matthew T. Cabeen, Michelle A. Murolo, Ariane Briegel, N. Khai Bui, Waldemar Vollmer, Nora Ausmees, Grant J. Jensen, and Christine Jacobs-Wagner. Mutations in the lipopolysaccharide biosynthesis pathway interfere with crescentin-mediated cell curvature in <i>caulobacter crescentus</i>. Journal of Bacteriology, 192:3368-3378, Jul 2010. URL: https://doi.org/10.1128/jb.01371-09, doi:10.1128/jb.01371-09. This article has 35 citations and is from a peer-reviewed journal.

16. (sundararajan2017cytoskeletalproteinsin pages 16-17): Kousik Sundararajan and Erin D. Goley. Cytoskeletal proteins in caulobacter crescentus: spatial orchestrators of cell cycle progression, development, and cell shape. Sub-cellular biochemistry, 84:103-137, Jan 2017. URL: https://doi.org/10.1007/978-3-319-53047-5\_4, doi:10.1007/978-3-319-53047-5\_4. This article has 25 citations.