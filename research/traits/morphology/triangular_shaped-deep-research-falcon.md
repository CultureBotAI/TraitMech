---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:22:43.684393'
end_time: '2026-08-04T10:30:23.474895'
duration_seconds: 459.79
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: triangular shaped
  trait_identifier: METPO:1000696
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: triangular_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism forms flat, triangular or wedge-shaped
    cells.
  parent_traits: METPO:1000666
  synonyms: triangular
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review supports anisotropic envelope architecture as the
    basis for non-round cell geometries such as triangles.) | DOI:10.1146/annurev-micro-090816-093703:
    archaeal cell shape (Archaeal cell-shape review supports unusual flat polygonal
    cells in halophilic archaea.)'
  causal_graph_summary: 'triangular_shaped_planar_polygonal_growth: 7 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** triangular shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000696
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, triangular or wedge-shaped cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** triangular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope architecture as the basis for non-round cell geometries such as triangles.) | DOI:10.1146/annurev-micro-090816-093703: archaeal cell shape (Archaeal cell-shape review supports unusual flat polygonal cells in halophilic archaea.)
- **Existing causal graph summary:** triangular_shaped_planar_polygonal_growth: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **triangular shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/triangular_shaped.yaml`.

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
- **Trait label:** triangular shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000696
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, triangular or wedge-shaped cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** triangular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope architecture as the basis for non-round cell geometries such as triangles.) | DOI:10.1146/annurev-micro-090816-093703: archaeal cell shape (Archaeal cell-shape review supports unusual flat polygonal cells in halophilic archaea.)
- **Existing causal graph summary:** triangular_shaped_planar_polygonal_growth: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **triangular shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/triangular_shaped.yaml`.

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


# Curation-focused research report: microbial “triangular shaped”

## Executive conclusion

**Trait:** “triangular shaped”  
**Identifier:** **METPO:1000696**  
**Definition:** a flat, triangular or wedge-shaped microbial cell.

The best-established exemplar is *Haloarcula japonica*. However, the literature currently supports the **phenotype much more strongly than a triangle-specific molecular mechanism**. Modern haloarchaeal work identifies S-layers, cytoskeletal proteins, growth phase, medium, and mechanical forces as major determinants of morphology, but direct perturbation evidence connecting a particular *H. japonica* gene or protein to triangularity was not found. Accordingly, a TraitMech graph should presently remain conservative: curate the phenotype assertion and, at most, broad envelope/growth context; retain detailed CetZ-, volactin-, or S-layer-sheet mechanisms as hypotheses or taxon-specific analogies.

## 1. Trait scope and boundaries

### Positive scope

METPO:1000696 denotes **cell geometry**, not metabolism, motility, salinity preference, aggregation, or colony shape. A positive observation should show an individual cell that is:

- flattened or plate-like;
- bounded by approximately three sides or forming a wedge;
- recognizably triangular under microscopy rather than merely irregular.

*H. japonica* is repeatedly described as triangular-shaped, and current reviews place triangles among the unusually precise, flat geometric forms produced by haloarchaea. Haloarchaeal cells usually occur in hypersaline habitats, but hypersalinity is ecological context rather than part of the morphological definition. One 2023 survey describes typical haloarchaeal habitats as approximately 3–5 M salt and notes that most species require at least 2 M NaCl; these figures should not be encoded as universal thresholds for triangularity. (wolferen2022thecellbiology pages 3-4, du2023evolutionarydevelopmentalbiology pages 1-7)

### Boundary cases

1. **Square or rectangular cells:** exclude unless a cell is explicitly triangular or wedge-shaped.
2. **Discoid/plate cells:** flatness alone is insufficient; a disk lacks the required three-sided outline.
3. **Generic polygonal cells:** polygonal is a broader parent-like morphology. Triangles qualify as polygons, but polygonal cells with four or more sides should not receive METPO:1000696.
4. **Pleomorphic or irregular cells:** do not infer triangularity from “pleomorphic.” Record the triangular class only when triangles were observed or quantitatively classified.
5. **Transient division intermediates:** a temporary wedge produced by constriction should be distinguished from a maintained cell morphology.
6. **Triangular S-layer pores:** these are nanoscale lattice features, not triangular cells.
7. **Mixed populations:** *Haloarcula hispanica* and *H. californiae* reportedly change from rods in early exponential phase to mixed rods, disks, triangles, and squares in stationary phase. Such observations support growth-dependent morphological plasticity but not a constitutive triangular phenotype. (du2023evolutionarydevelopmentalbiology pages 1-7)

A useful assay record should therefore include taxon/strain, growth phase or OD, medium and salinity, temperature, imaging method, pressure or confinement, and the fraction of cells classified as triangular.

## 2. Candidate graph nodes

### Trait and taxon

- **METPO:1000696** — triangular shaped.
- **METPO:1000666** — supplied parent trait; quote exactly in the YAML.
- *Haloarcula japonica* — label-only taxon candidate unless its verified NCBITaxon CURIE is imported from an authoritative ontology service.
- *Haloarcula hispanica* and *Haloarcula californiae* — contextual taxa with reported stationary-phase mixtures containing triangles.
- *Haloferax volcanii* — experimentally tractable **analogy taxon**, not direct evidence for triangularity.
- *Methylomirabilis lanthanidiphila* — cross-domain polygonal-shape analogy only.

### Cellular structures and localizations

- archaeal S-layer / glycoprotein surface lattice;
- cell envelope;
- cytoplasmic membrane;
- cell edge or perimeter;
- division plane;
- rigid overlapping S-layer sheets — bacterial analogy only.

Most archaea possess an S-layer assembled from one or two protein subunits into a paracrystalline lattice. Reviews regard the S-layer as important for structural integrity, but how its subunits are inserted during growth—and whether cytoskeletal proteins direct that insertion—remains unresolved. (liao2018archaealcellbiology pages 1-5, bissonfilho2018archaealimagingleading pages 2-3, wolferen2022thecellbiology pages 3-4)

### Genes and proteins

**Directly relevant *H. japonica* candidates, but not yet causal:**

- *H. japonica* cell-surface glycoprotein/S-layer protein — candidate based on envelope biology; no retrieved triangle-loss perturbation evidence.
- FtsZ1 — a division candidate, not demonstrated as a triangular-shape determinant.
- CetZ-family homologues — plausible shape-control candidates by homology, but no direct *H. japonica* evidence retrieved.

**Experimentally supported only in *H. volcanii*:**

- CetZ1, locus **HVO_2204**;
- CetZ2, locus **HVO_0745**;
- RdfA, **HVO_2174**;
- Sph3, **HVO_2175**;
- DdfA, **HVO_2176**;
- volactin/VolA, **HVO_2015**.

CetZ1 is required for the plate-to-rod transition and swimming morphology in *H. volcanii*, whereas recent work indicates that CetZ2 promotes stationary-phase plate maintenance. RdfA and DdfA are associated respectively with rod and disk formation, and volactin participates in disk morphogenesis. None has yet been shown to generate triangles. (duggin2015cetztubulinlikeproteins pages 1-2, brown2024archaealtubulinlikeproteins pages 1-5, patro2023“influenceofplasmids pages 2-3, schiller2024identificationofstructural pages 5-6)

**Cross-domain analogy:**

- **mela_00855**, a 316-aa, approximately 31.6-kDa S-layer protein from *M. lanthanidiphila*.

### Processes and functions

- cell-shape determination;
- S-layer assembly and turnover;
- cell-envelope remodeling;
- cytoskeletal polymerization/depolymerization;
- growth-phase-dependent morphological transition;
- spatial control of local growth;
- division-plane placement;
- mechanical deformation.

### Environmental and experimental factors

- growth phase;
- nutrient medium and trace-metal availability;
- hypersalinity;
- external mechanical force, pressure, or confinement;
- plasmid presence and selectable-marker background;
- microscopy and segmentation criteria.

A 2023 study showed that plasmids, auxotrophic backgrounds, and especially Δ*hdrB*/*hdrB* selection can alter *H. volcanii* morphology. An earlier cited example changed rod frequency from about 20% without a plasmid to 90–100% with one. These are important confounders for shape genetics, but they do not establish triangularity. (patro2023“influenceofplasmids pages 1-2, patro2023“influenceofplasmids pages 2-3)

## 3. Candidate causal and contextual edges

The table below provides a high-level disposition; detailed snippets and qualifications follow.

| subject | predicate | object | evidence class/directness | taxon | recommended curation disposition |
|---|---|---|---|---|---|
| Haloarcula japonica | has_morphology | METPO:1000696 | Direct phenotype observation; triangular-shaped cells explicitly reported (wolferen2022thecellbiology pages 3-4, du2023evolutionarydevelopmentalbiology pages 1-7) | Haloarcula japonica | Curate as core trait assertion |
| Haloarcula spp. | can_transition_during_growth_phase_to | mixed rods/disks/triangles/squares | Contextual, genus-level growth-phase observation; indirect for H. japonica specifically (du2023evolutionarydevelopmentalbiology pages 1-7) | Haloarcula hispanica, Haloarcula californiae; contextual for Haloarcula genus | Curate only as contextual environmental/assay note, not as core mechanism for H. japonica triangularity |
| archaeal S-layer | contributes_to | cell structural integrity and morphology | General archaeal review evidence; indirect for triangular cells (bissonfilho2018archaealimagingleading pages 2-3, wolferen2022thecellbiology pages 3-4, du2023evolutionarydevelopmentalbiology pages 1-7) | Archaea | Curate cautiously as broad background edge if TraitMech allows high-level envelope support |
| mechanical forces / slight pressure | alters | haloarchaeal cell shape | Contextual environmental effect; indirect for triangular shape (wolferen2022thecellbiology pages 3-4, patro2023“influenceofplasmids pages 2-3) | Haloarchaea | Context only; do not curate as triangular-specific mechanism |
| growth phase | influences | haloarchaeal cell shape | Direct in haloarchaea generally; indirect for H. japonica triangular trait (patro2023“influenceofplasmids pages 1-2, wolferen2022thecellbiology pages 3-4, du2023evolutionarydevelopmentalbiology pages 1-7) | Haloarchaea | Curate as contextual factor only |
| CetZ1 | required_for | rod formation | Experimental gene-function evidence, analog only; not triangular-specific (duggin2015cetztubulinlikeproteins pages 1-2, patro2023“influenceofplasmids pages 2-3, brown2024archaealtubulinlikeproteins pages 1-5) | Haloferax volcanii | Do not curate into triangular graph except as analogy/possible upstream shape-control candidate |
| CetZ2 | promotes_maintenance_of | plate cell shape | Experimental gene-function evidence, analog only; stationary phase plate maintenance (brown2024archaealtubulinlikeproteins pages 1-5) | Haloferax volcanii | Analog only; do not curate as triangular mechanism |
| rdfA (HVO_2174) | important_for | rod formation | Experimental gene-function evidence, analog only (patro2023“influenceofplasmids pages 2-3) | Haloferax volcanii | Analog only; exclude from core triangular graph unless future Haloarcula evidence appears |
| ddfA (HVO_2176) | important_for | plate formation | Experimental gene-function evidence, analog only (patro2023“influenceofplasmids pages 2-3) | Haloferax volcanii | Analog only; exclude from core triangular graph unless future Haloarcula evidence appears |
| Sph3 (HVO_2175) | disruption_leads_to | rod-only phenotype | Experimental mutant phenotype, analog only (patro2023“influenceofplasmids pages 2-3, schiller2024identificationofstructural pages 5-6) | Haloferax volcanii | Analog only; not triangular-specific |
| volactin | plays_role_in | disk-shape morphogenesis | Experimental structural evidence, analog only (patro2023“influenceofplasmids pages 2-3, schiller2024identificationofstructural pages 9-10) | Haloferax volcanii | Analog only; not triangular-specific |
| mela_00855 | is_S-layer_protein_associated_with | polygonal cell shape | Experimental identification/localization, cross-domain analogy only (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 7-9) | Methylomirabilis lanthanidiphila | Do not curate into archaeal triangular graph except as structural analogy |
| overlapping rigid S-layer sheets | give_rise_to | polygonal cell shape | Experimental structural mechanism, cross-domain analogy only (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 7-9) | Methylomirabilis lanthanidiphila | Analog only; useful hypothesis seed, not curatable for METPO:1000696 |
| CetZ/FtsZ/other cytoskeletal filaments | may_control | local S-layer insertion / envelope remodeling | Mechanistic hypothesis from review; indirect and uncertain (bissonfilho2018archaealimagingleading pages 2-3, liao2018archaealcellbiology pages 1-5) | Archaea / Haloferax model | Do not curate yet; insufficient direct evidence for triangular shape |


*Table: This table summarizes candidate causal and contextual triples relevant to METPO:1000696, separating direct trait evidence from broader archaeal context and analog-only mechanisms. It is useful for deciding which claims are curatable now versus which should remain as hypotheses or background notes.*

### Detailed evidence ledger

| Candidate triple | Reference | Supporting snippet | Curation assessment |
|---|---|---|---|
| *Haloarcula japonica* — **has morphology** → METPO:1000696 | 10.1038/s41564-022-01215-8; 10.48617/etd.674 | “flat squares … and triangles”; “triangular-shaped *Haloarcula japonica*” | **Curate.** This is direct phenotype evidence, although the thesis is secondary confirmation rather than the original species description. (wolferen2022thecellbiology pages 3-4, du2023evolutionarydevelopmentalbiology pages 1-7) |
| growth phase — **influences** → haloarchaeal shape distribution | 10.3389/fmicb.2023.1270665; 10.48617/etd.674 | Shapes “vary with growth stages”; *Haloarcula* species shift from rods to “a mixture of rods, disks, triangles, and squares” | **Contextual edge only.** Strong for haloarchaeal plasticity, but not demonstrated specifically as the cause of *H. japonica* triangularity. (patro2023“influenceofplasmids pages 1-2, du2023evolutionarydevelopmentalbiology pages 1-7) |
| mechanical force/slight pressure — **alters** → haloarchaeal cell shape | 10.1038/s41564-022-01215-8 | Shape changes “are accentuated by slight pressure” | **Uncertain/context only.** Do not encode as producing triangles without a triangle-specific assay. (wolferen2022thecellbiology pages 3-4) |
| archaeal S-layer — **supports/maintains** → cell morphology | 10.1091/mbc.e17-10-0603; 10.1042/ETLS20180026 | “S-layer is essential for cell morphology”; most archaea have a “glycoprotein lattice S-layer” rather than peptidoglycan | **Broadly defensible but not triangle-specific.** If included, use a weak/high-level predicate and annotate taxonomic generality. (liao2018archaealcellbiology pages 1-5, bissonfilho2018archaealimagingleading pages 2-3) |
| CetZ1 — **required for** → rod formation | 10.1038/nature13983 | “CetZ1 was required for differentiation of the irregular plate-shaped cells into a rod-shaped cell type” | **Do not connect to METPO:1000696.** Direct experiment, wrong taxon and wrong terminal morphology. Useful only as a haloarchaeal shape-control analogy. (duggin2015cetztubulinlikeproteins pages 1-2) |
| CetZ2 — **promotes maintenance of** → stationary-phase plate shape | 10.1101/2024.10.29.620987 | CetZ2 “promotes the maintenance of plate cell shape” and counteracts CetZ1-based rod development | **Hypothesis-generating only.** 2024 preprint, *H. volcanii*, and not triangular. (brown2024archaealtubulinlikeproteins pages 1-5) |
| RdfA — **required/important for** → rod formation | 10.1038/s41467-024-45196-0 | RdfA was identified as “important for rod formation” | **Analog only.** Exclude from the core triangular graph. (patro2023“influenceofplasmids pages 2-3) |
| DdfA — **required/important for** → disk formation | 10.1038/s41467-024-45196-0 | DdfA was identified as “important for plate formation” | **Analog only.** Potential upstream candidate for flatness, but no evidence for three-sided geometry. (patro2023“influenceofplasmids pages 2-3) |
| disruption of Sph3 — **causes** → rod-only morphology | 10.1038/s41467-024-45196-0 | Sph3 disruption “led the cells to only form rods” | **Analog only.** Not triangle-specific. (patro2023“influenceofplasmids pages 2-3, schiller2024identificationofstructural pages 5-6) |
| volactin — **participates in** → disk-shape morphogenesis | 10.1038/s41467-024-45196-0 | An actin homologue “plays a role in disk-shape morphogenesis” | **Analog only.** A candidate for planar morphology, but transfer to *H. japonica* would be speculative. (patro2023“influenceofplasmids pages 2-3, schiller2024identificationofstructural pages 9-10) |
| mela_00855-containing S-layer sheets — **produce/define** → polygonal morphology | 10.3389/fmicb.2021.766527 | Planar S-layer sheets “intersected at sharp ridges, thereby likely defining the polygonal shape” | **Do not curate into the archaeal triangular graph.** Strong structural analogy from a bacterium; neither taxon nor exact geometry matches. (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 7-9) |
| CetZ/FtsZ cytoskeleton — **directs** → local S-layer insertion | 10.1091/mbc.e17-10-0603; 10.1042/ETLS20180026 | CetZ “may control where the cell adds new S-layer material”; activity “may involve” directed S-layer insertion | **Do not curate as causal.** Explicitly framed as a hypothesis. (liao2018archaealcellbiology pages 1-5, bissonfilho2018archaealimagingleading pages 2-3) |

## 4. Recent developments and quantitative findings

### 2024: regulatory and structural shape determinants

The peer-reviewed 2024 *Nature Communications* study used genetics, proteomics, and live-cell imaging in *H. volcanii*. It established distinct rod- and disk-determining factors and described dynamic volactin as a disk-morphogenesis protein. This significantly advances archaeal morphogenesis but does **not** resolve triangular-cell development. (patro2023“influenceofplasmids pages 2-3, schiller2024identificationofstructural pages 9-10, schiller2024identificationofstructural pages 5-6)

A December 2024 preprint reported antagonistic CetZ paralog functions: CetZ1 supports rod development, whereas CetZ2 is strongly upregulated in stationary phase and maintains plate morphology. CetZ2 structures moved directionally around the cell edge, and their dynamics depended on CetZ1/CetZ2 and GTPase activity. Because this is a preprint and concerns plates rather than triangles, it should inform candidate selection rather than support a curated triangle edge. (brown2024archaealtubulinlikeproteins pages 1-5)

### 2023: experimental confounding and reproducibility

The 2023 plasmid/auxotrophy study demonstrated that genotype construction itself can alter morphology. Cells were classified using circularity: 0.8–1.0 as plates, >0.6–<0.8 as intermediate, and ≤0.6 as rods. These thresholds do not classify triangles and should not be reused for METPO:1000696 without a dedicated triangle descriptor such as polygon vertex count, solidity, angularity, and three-corner persistence. (patro2023“influenceofplasmids pages 2-3)

### Structural benchmark from polygonal bacteria

Cryo-electron tomography of *M. lanthanidiphila* showed an S-layer approximately 11 nm above the outer membrane. Its planar sheets overlapped at sharp ridges; the cytoplasmic membrane and peptidoglycan did not share the polygonal contour, and isolated peptidoglycan sacculi were round. The S-layer unit cell measured about 11.9 × 11.6 nm at 60°, and mela_00855 was 316 aa/31.6 kDa. This is unusually strong evidence that a protein surface lattice can impose polygonal geometry, but it remains an analogy rather than evidence for *H. japonica*. (gambelli2021thepolygonalcell pages 7-9)

## 5. Current applications and real-world relevance

There is no established industrial or clinical application of the triangular phenotype itself. Current implementations are primarily research-oriented:

- haloarchaea as live-cell models for cytoskeletal evolution and envelope morphogenesis;
- high-resolution microscopy of large, flattened cells;
- studies of growth-dependent differentiation and motility;
- S-layer nanostructure research and biomimetic materials;
- morphological biosignatures in environmental microbiology.

The most immediate practical application is **experimental design**: shape studies must control growth phase, medium, trace metals, plasmid burden, selectable markers, and mechanical confinement. Otherwise, morphology attributed to a gene may instead be an assay artifact. (liao2018archaealcellbiology pages 1-5, patro2023“influenceofplasmids pages 1-2, patro2023“influenceofplasmids pages 2-3)

## 6. Ontology grounding recommendations

Use only verified identifiers during YAML construction.

| Node | Recommended grounding |
|---|---|
| triangular shaped | **METPO:1000696** |
| supplied parent | **METPO:1000666** |
| *H. japonica* and other taxa | Resolve through NCBITaxon before curation; do not infer numeric IDs from memory |
| S-layer, cell envelope, membrane, cell-shape determination | Map through GO only after confirming exact term scope; label-only is safer than an unverified CURIE |
| CetZ1/2, RdfA, DdfA, Sph3, volactin | Preserve species-specific locus tags; add UniProt CURIEs only after database verification |
| growth phase, hypersaline environment, pressure/confinement | Resolve using ENVO or experimental-condition ontology where exact matches exist |
| GTP | CHEBI grounding is appropriate in principle, but verify the exact CHEBI record before insertion |

No metabolic pathway, electron donor, electron acceptor, transporter, enzyme, KEGG module, MetaCyc pathway, Rhea reaction, or EC number has a demonstrated causal relationship to triangularity. Such node classes should not be added merely to fill the template.

## 7. Recommended minimal graph

A defensible current graph is smaller than the supplied seven-node/seven-edge summary:

1. *Haloarcula japonica* — **has morphology** → **METPO:1000696**.
2. archaeal S-layer — **contributes to structural integrity/morphology** → cell shape, annotated **general and not triangle-specific**.
3. growth phase — **modulates observed shape distribution** → haloarchaeal morphology, annotated **genus-level/contextual**.
4. mechanical environment — **modulates** → haloarchaeal morphology, annotated **uncertain and not triangle-specific**.

If TraitMech requires every edge to terminate in the target trait through direct experimental evidence, retain only edge 1 and place the others in comments or an evidence-candidate section.

## 8. Claims that should not yet be curated

- CetZ1, CetZ2, FtsZ1, RdfA, DdfA, Sph3, or volactin **causes triangular shape**.
- Localized S-layer insertion **creates triangle vertices**.
- Hexagonal or triangular S-layer pores determine whole-cell triangular geometry.
- The *Methylomirabilis* overlapping-sheet mechanism operates in *H. japonica*.
- Stationary phase universally induces triangular *H. japonica* cells.
- Hypersalinity specifically causes triangularity rather than merely enabling haloarchaeal growth.
- Triangular morphology improves nutrient uptake, flotation, motility, or ecological fitness; these remain plausible adaptive interpretations without direct tests.
- FtsZ-dependent asymmetric division propagates triangularity; division proteins have been studied, but triangle-specific loss-of-function evidence was not retrieved.

## DOI-first bibliography

1. Schiller H. et al. **Identification of structural and regulatory cell-shape determinants in *Haloferax volcanii*.** *Nature Communications* 15, 1414. Published February 2024. DOI: [10.1038/s41467-024-45196-0](https://doi.org/10.1038/s41467-024-45196-0). (schiller2024identificationofstructural pages 9-10, schiller2024identificationofstructural pages 5-6)
2. Brown H.J., Duggin I.G. **Archaeal tubulin-like proteins CetZ1 and CetZ2 have opposing effects on cell morphology during the growth cycle of *Haloferax volcanii*.** bioRxiv preprint, December 2024. DOI: [10.1101/2024.10.29.620987](https://doi.org/10.1101/2024.10.29.620987). (brown2024archaealtubulinlikeproteins pages 1-5)
3. Patro M. et al. **Influence of plasmids, selection markers and auxotrophic mutations on *Haloferax volcanii* cell shape plasticity.** *Frontiers in Microbiology* 14. Published 29 September 2023. DOI: [10.3389/fmicb.2023.1270665](https://doi.org/10.3389/fmicb.2023.1270665). (patro2023“influenceofplasmids pages 1-2, patro2023“influenceofplasmids pages 2-3)
4. Du Z. **Evolutionary Developmental Biology in Haloarchaea.** Brandeis University MSc thesis, May 2023. DOI: [10.48617/etd.674](https://doi.org/10.48617/etd.674). (du2023evolutionarydevelopmentalbiology pages 1-7)
5. van Wolferen M. et al. **The Cell Biology of Archaea.** *Nature Microbiology* 7, 1744–1755. Published October 2022. DOI: [10.1038/s41564-022-01215-8](https://doi.org/10.1038/s41564-022-01215-8). (wolferen2022thecellbiology pages 3-4)
6. Gambelli L. et al. **The Polygonal Cell Shape and Surface Protein Layer of Anaerobic Methane-Oxidizing *Methylomirabilis lanthanidiphila* Bacteria.** *Frontiers in Microbiology* 12. Published 1 December 2021. DOI: [10.3389/fmicb.2021.766527](https://doi.org/10.3389/fmicb.2021.766527). (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 7-9)
7. Liao Y. et al. **Archaeal cell biology: diverse functions of tubulin-like cytoskeletal proteins at the cell envelope.** *Emerging Topics in Life Sciences* 2, 547–559. Published December 2018. DOI: [10.1042/ETLS20180026](https://doi.org/10.1042/ETLS20180026). (liao2018archaealcellbiology pages 1-5)
8. Bisson-Filho A.W., Zheng J., Garner E.C. **Archaeal imaging: leading the hunt for new discoveries.** *Molecular Biology of the Cell* 29, 1675–1681. Published July 2018. DOI: [10.1091/mbc.e17-10-0603](https://doi.org/10.1091/mbc.e17-10-0603). (bissonfilho2018archaealimagingleading pages 2-3)
9. Duggin I.G. et al. **CetZ tubulin-like proteins control archaeal cell shape.** *Nature* 519, 362–365. Published 19 March 2015. DOI: [10.1038/nature13983](https://doi.org/10.1038/nature13983). (duggin2015cetztubulinlikeproteins pages 1-2)

**Foundational records identified but not used as primary mechanistic support because full-text evidence was unavailable:** Takashina et al., *Haloarcula japonica* sp. nov., DOI [10.1016/S0723-2020(11)80165-7](https://doi.org/10.1016/S0723-2020(11)80165-7) (May 1990); Nishiyama et al., cell-wall ultrastructure, DOI [10.1016/0378-1097(92)90285-V](https://doi.org/10.1016/0378-1097(92)90285-V) (November 1992); Horikoshi et al., triangular *H. japonica* TR-1, DOI [10.1007/BF01955151](https://doi.org/10.1007/BF01955151) (1993); and Wakai et al., cell-surface glycoprotein gene, DOI [10.1007/s007920050012](https://doi.org/10.1007/s007920050012) (1997).

Overall, **METPO:1000696 is ready for phenotype-level curation, but not yet for a detailed, gene-resolved triangular-shape mechanism**. The key next experiment is a genetic and live-cell imaging study in *H. japonica* that perturbs its S-layer, CetZ homologues, and division machinery while quantitatively scoring triangle formation and maintenance.

References

1. (wolferen2022thecellbiology pages 3-4): Marleen van Wolferen, Andre Arashiro Pulschen, Buzz Baum, Simonetta Gribaldo, and Sonja-Verena Albers. The cell biology of archaea. Nature microbiology, 7:1744-1755, Oct 2022. URL: https://doi.org/10.1038/s41564-022-01215-8, doi:10.1038/s41564-022-01215-8. This article has 141 citations and is from a highest quality peer-reviewed journal.

2. (du2023evolutionarydevelopmentalbiology pages 1-7): Zhantao Du. Evolutionary developmental biology in haloarchaea. Text, Jan 2023. URL: https://doi.org/10.48617/etd.674, doi:10.48617/etd.674. This article has 0 citations and is from a peer-reviewed journal.

3. (liao2018archaealcellbiology pages 1-5): Yan Liao, Solenne Ithurbide, Roshali T. de Silva, Susanne Erdmann, and Iain G. Duggin. Archaeal cell biology: diverse functions of tubulin-like cytoskeletal proteins at the cell envelope. Emerging topics in life sciences, 2 4:547-559, Dec 2018. URL: https://doi.org/10.1042/etls20180026, doi:10.1042/etls20180026. This article has 19 citations.

4. (bissonfilho2018archaealimagingleading pages 2-3): Alexandre W. Bisson-Filho, Jenny Zheng, and Ethan C. Garner. Archaeal imaging: leading the hunt for new discoveries. Molecular Biology of the Cell, 29:1675-1681, Jul 2018. URL: https://doi.org/10.1091/mbc.e17-10-0603, doi:10.1091/mbc.e17-10-0603. This article has 42 citations and is from a domain leading peer-reviewed journal.

5. (duggin2015cetztubulinlikeproteins pages 1-2): Iain G. Duggin, Christopher H. S. Aylett, James C. Walsh, Katharine A. Michie, Qing Wang, Lynne Turnbull, Emma M. Dawson, Elizabeth J. Harry, Cynthia B. Whitchurch, Linda A. Amos, and Jan Löwe. Cetz tubulin-like proteins control archaeal cell shape. Nature, 519:362-365, Dec 2015. URL: https://doi.org/10.1038/nature13983, doi:10.1038/nature13983. This article has 184 citations and is from a highest quality peer-reviewed journal.

6. (brown2024archaealtubulinlikeproteins pages 1-5): Hannah J. Brown and Iain G. Duggin. Archaeal tubulin-like proteins cetz1 and cetz2 have opposing effects on cell morphology during the growth cycle of haloferax volcanii. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.10.29.620987, doi:10.1101/2024.10.29.620987. This article has 1 citations.

7. (patro2023“influenceofplasmids pages 2-3): Megha Patro, Iain G. Duggin, Sonja-Verena Albers, and Solenne Ithurbide. “influence of plasmids, selection markers and auxotrophic mutations on haloferax volcanii cell shape plasticity”. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1270665, doi:10.3389/fmicb.2023.1270665. This article has 8 citations and is from a peer-reviewed journal.

8. (schiller2024identificationofstructural pages 5-6): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

9. (patro2023“influenceofplasmids pages 1-2): Megha Patro, Iain G. Duggin, Sonja-Verena Albers, and Solenne Ithurbide. “influence of plasmids, selection markers and auxotrophic mutations on haloferax volcanii cell shape plasticity”. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1270665, doi:10.3389/fmicb.2023.1270665. This article has 8 citations and is from a peer-reviewed journal.

10. (schiller2024identificationofstructural pages 9-10): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

11. (gambelli2021thepolygonalcell pages 1-2): Lavinia Gambelli, Rob Mesman, Wouter Versantvoort, Christoph A. Diebolder, Andreas Engel, Wiel Evers, Mike S. M. Jetten, Martin Pabst, Bertram Daum, and Laura van Niftrik. The polygonal cell shape and surface protein layer of anaerobic methane-oxidizing methylomirabilis lanthanidiphila bacteria. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.766527, doi:10.3389/fmicb.2021.766527. This article has 3 citations and is from a peer-reviewed journal.

12. (gambelli2021thepolygonalcell pages 7-9): Lavinia Gambelli, Rob Mesman, Wouter Versantvoort, Christoph A. Diebolder, Andreas Engel, Wiel Evers, Mike S. M. Jetten, Martin Pabst, Bertram Daum, and Laura van Niftrik. The polygonal cell shape and surface protein layer of anaerobic methane-oxidizing methylomirabilis lanthanidiphila bacteria. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.766527, doi:10.3389/fmicb.2021.766527. This article has 3 citations and is from a peer-reviewed journal.