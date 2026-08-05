---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:05:54.526298'
end_time: '2026-08-04T10:12:24.133065'
duration_seconds: 389.61
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: square shaped
  trait_identifier: METPO:1000694
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: square_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism forms flat, square or rectangular
    cells.
  parent_traits: METPO:1000666
  synonyms: square
  evidence_summary: 'DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Haloquadratum
    walsbyi description supports flat square cell morphology in halophilic archaea.)
    | DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined
    (Cell-shape review supports anisotropic envelope growth as the basis for non-round
    cell geometries.)'
  causal_graph_summary: 'square_shaped_planar_anisotropic_growth: 10 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** square shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000694
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, square or rectangular cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** square
- **Existing evidence:** DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Haloquadratum walsbyi description supports flat square cell morphology in halophilic archaea.) | DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope growth as the basis for non-round cell geometries.)
- **Existing causal graph summary:** square_shaped_planar_anisotropic_growth: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **square shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/square_shaped.yaml`.

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
- **Trait label:** square shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000694
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, square or rectangular cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** square
- **Existing evidence:** DOI:10.1099/ijs.0.65431-0: flat square or disc-shaped cells (Haloquadratum walsbyi description supports flat square cell morphology in halophilic archaea.) | DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope growth as the basis for non-round cell geometries.)
- **Existing causal graph summary:** square_shaped_planar_anisotropic_growth: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **square shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/square_shaped.yaml`.

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


# Curation-focused research report: microbial “square shaped” morphology

## Executive assessment

**Target trait:** “square shaped”  
**Identifier:** **METPO:1000694**  
**Category:** morphology; class; mapping status reviewed  
**Definition:** a cell shape in which an organism forms flat, square or rectangular cells.

The best-characterized exemplar is the extreme halophilic archaeon *Haloquadratum walsbyi*. Its phenotype is an **ultrathin, planar square or rectangle**, typically **2–5 µm wide and 0.1–0.2 µm thick**, rather than a cuboid. Cells contain gas vesicles and polyhydroxyalkanoate granules and may appear folded or irregular when large cells do not lie flat during microscopy. Thus, “flatness” and approximately orthogonal planar edges are essential scope criteria. (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 2-3)

The central curation conclusion is conservative: **no gene, protein, pathway, or perturbation has yet been demonstrated to cause the square geometry of *H. walsbyi*.** The strongest model is an envelope-centered one involving a mechanically stabilizing S-layer and possibly an external capsule, operating in a high-salt environment. However, the square-specific causal steps remain inferred rather than genetically or biochemically established. (kugelgen2021completeatomicstructure pages 1-3, saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8, martincuadrado2015diversityofthe pages 1-2)

## 1. Trait scope and boundary cases

### Included phenotype

METPO:1000694 should cover individual microbial cells that are:

- **Flat and plate-like**, with thickness much smaller than width.
- **Square or rectangular in plan view**, including unequal side lengths when the underlying phenotype remains a flat orthogonal plate.
- Exemplified by *H. walsbyi*, whose cells were described as “square or rectangular” and measured at **2–5 µm wide by 0.1–0.2 µm thick**. A documented unusually large cell measured approximately **10 × 10 µm**. (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 2-3)

### Boundary cases to exclude or annotate separately

1. **Discoid cells:** Flat circular or pleomorphic haloarchaeal cells are not square shaped merely because they are thin. *Haloferax volcanii*, for example, commonly produces discoid and rod forms rather than the *Haloquadratum* phenotype. (cooper2023archaealtubulinlikeproteins pages 1-2)
2. **Cuboidal cells or packets:** Three-dimensional cubes and cubical arrangements should not be mapped to this term; the defining phenotype is a two-dimensional plate.
3. **Rectangular rods:** A conventional cylindrical rod with a rectangular two-dimensional projection is not a flat rectangular cell.
4. **Multicellular sheets or “postage-stamp” arrays:** Cell arrangement should be represented separately from individual-cell shape. An array of round cells is not square shaped, while square cells may occur singly or in sheets.
5. **Folded cells and preparation artifacts:** Large *H. walsbyi* cells can fold at corners and appear irregular. This does not negate the underlying square trait, but image-based annotation should examine unfolded regions or multiple cells. (saponetti2011morphologicalandstructural pages 2-3)
6. **Disc-shaped descriptions in historical sources:** A “flat square or disc-shaped” observation is insufficient by itself to assign square shape unless the square/rectangular state is explicitly resolved.

## 2. Current biological understanding

### Environmental setting

*H. walsbyi* inhabits salt lakes and solar-saltern crystallizer ponds, often near NaCl saturation. Growth requires at least **14% w/v salt**, more than four times seawater salinity, and higher cell densities have been reported in media containing **>1 M MgCl₂**. At saturation, the organism can account for approximately **80% of the microbial population**; a later population-genomic study likewise reported up to **80% of cells in NaCl-saturated brines worldwide**. (dyallsmith2011haloquadratumwalsbyi pages 1-2, martincuadrado2015diversityofthe pages 1-2)

A 2024 authoritative review operationally defined hypersaline habitats as containing **>100–150 g/L dissolved salts** and highlighted *Haloquadratum* as a major archaeal genus for which metagenomics has clarified biogeography. These recent developments strengthen the ecological context but do not resolve the shape mechanism. (oren2024novelinsightsinto pages 1-2)

### Envelope architecture

AFM under near-physiological conditions detected a regular surface corrugation with **16–20 nm periodicity**, attributed to the S-layer protein lattice. Archaeal S-layers are proteinaceous two-dimensional arrays that can stabilize membranes and preserve cell shape generally. Yet the *H. walsbyi* study did not disrupt the S-layer or show conversion from square to another shape; therefore, S-layer → square geometry is a plausible but unproven causal edge. (kugelgen2021completeatomicstructure pages 1-3, saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8)

Envelope architecture also varies between isolates. C23T has a conventional membrane plus external S-layer, whereas HBSQ001 was reported to have an atypical triple-layered wall. Both nevertheless exhibit the square phenotype, arguing that gross wall-layer number is not, by itself, a sufficient square-shape determinant. (dyallsmith2011haloquadratumwalsbyi pages 1-2)

### Capsule and halomucin

Drying-series AFM directly observed a soft external film that progressively tore, collapsed, and uncovered an underlying layer as water was lost. The genome encodes a giant **9,159-amino-acid** secreted protein called halomucin, proposed to create an aqueous shield and protect against desiccation. However, the microscopy study stated only that the capsule **might correspond** to halomucin. Neither biochemical identification nor gene deletion established this identity or a square-shape function. (dyallsmith2011haloquadratumwalsbyi pages 1-2, saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8)

### Gas vesicles, light exposure, and planar orientation

Gas vesicles are directly visible in square cells. They confer buoyancy and are proposed to position cells near and parallel to the water surface, improving light capture by photoactive retinal proteins. This is a credible physiological adaptation that may favor an ultrathin planar architecture, but it does not demonstrate that gas vesicles generate square edges. It should therefore connect to buoyancy and surface orientation, not directly to METPO:1000694. (saponetti2011morphologicalandstructural pages 2-3, saponetti2011morphologicalandstructural pages 3-5)

### Storage granules

PHA/PHB granules are common intracellular features. They store carbon and energy and may reduce metabolically active cytosolic volume, potentially lowering ionic-homeostasis costs. These are adaptations associated with the cells, not demonstrated morphogenetic entities. (dyallsmith2011haloquadratumwalsbyi pages 1-2, saponetti2011morphologicalandstructural pages 5-8)

## 3. Candidate nodes grouped by type

### Trait and taxon nodes

- **square-shaped cell:** **METPO:1000694**
- **parent morphology:** **METPO:1000666**
- ***Haloquadratum walsbyi*:** use the current NCBITaxon record after identifier verification during implementation; do not infer the numeric CURIE from memory.
- ***Haloferax volcanii*:** comparator taxon only, not evidence for the target trait.

### Environmental and experimental nodes

- Hypersaline water / NaCl-saturated brine — candidate **ENVO** grounding should be selected against the exact environmental context.
- Sodium chloride — **CHEBI:26710**.
- Magnesium chloride — **CHEBI:6636**.
- High potassium chloride cytoplasm / salt-in osmoadaptation — candidate process node; exact GO or METPO grounding should be verified.
- Solar-saltern crystallizer pond — label plus an ENVO term after ontology lookup.
- Desiccation / drying — **GO:0009269** (“response to desiccation”) applies only if representing the biological response, not the experimental treatment itself.
- Light exposure and aerobic culture — experimental-context nodes, not square-shape causes.

### Cellular structures and localizations

- S-layer / surface-layer lattice — label-only unless a verified ontology term is selected.
- Cell envelope — **GO:0030313**.
- Plasma membrane — **GO:0005886**.
- External capsule / extracellular aqueous shield — label-only pending precise grounding.
- Gas vesicle — **GO:0031411**.
- PHA/PHB storage granule — label-only or an appropriate GO cellular-component term after verification.
- Cell surface — **GO:0009986**.

### Genes and proteins

- **Halomucin**, a predicted 9,159-aa secreted mucin-like protein — protein/gene label should be linked to the strain-specific UniProt or locus identifier only after database verification.
- **S-layer glycoprotein(s)** — strain-specific products; genomic-island annotations are largely putative.
- **GI1 cell-wall-associated genomic island** — genomic-region node; contains putative S-layer, surface-glycoprotein, and envelope-formation genes.
- **BopI/BopII bacteriorhodopsins** — candidate proteins for light-driven proton transport; peripheral to square morphogenesis.
- **FtsZ1/FtsZ2 and CetZ proteins** — hypothesis-generating comparator nodes. In *H. volcanii*, deletion experiments alter morphology, but no retrieved evidence assigns them square-shape control in *H. walsbyi*. (cooper2023archaealtubulinlikeproteins pages 1-2)

### Biological processes and molecular functions

- S-layer assembly.
- Cell-envelope organization — **GO:0045229**.
- Maintenance of cell shape — **GO:0030011**.
- Buoyancy — label-only biological process unless a validated GO term is found.
- Positioning parallel to the water surface — ecological/behavioral process, label-only.
- Desiccation protection / water retention.
- Light-driven proton transport — use a verified GO molecular-function/process term if Bop proteins enter the graph.
- Cell division — **GO:0051301**; no square-specific division geometry is established here.

## 4. Candidate causal edges

The following table is the recommended high-level triage for TraitMech curation.

| subject | predicate | object | evidence tier | taxon | curation decision |
|---|---|---|---|---|---|
| NaCl-saturated / hypersaline medium | enables growth of | *Haloquadratum walsbyi* | Direct growth observation: cells require at least 14% w/v salt for growth; ecology consistent with dominance in saturated brines (dyallsmith2011haloquadratumwalsbyi pages 1-2, martincuadrado2015diversityofthe pages 1-2) | *Haloquadratum walsbyi* | **Curate** as environmental prerequisite supporting occurrence of square-shaped cells, but **not** as a direct shape-determinant edge |
| MgCl2 (>1 M in medium) | increases | *H. walsbyi* cell density | Direct physiological observation in comparative genomics paper (dyallsmith2011haloquadratumwalsbyi pages 1-2) | *Haloquadratum walsbyi* | **Curate with caution** as environmental factor improving growth/yield; **do not** curate as direct cause of square geometry |
| S-layer protein lattice (16–20 nm corrugation) | mechanically stabilizes | archaeal cell envelope / cell wall | Mixed evidence: direct AFM detection of S-layer periodicity in *H. walsbyi* plus general authoritative review that S-layers preserve cell shape and stabilize membranes, but square-specific causality remains inferred (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8, kugelgen2021completeatomicstructure pages 1-3) | *Haloquadratum walsbyi*; comparator *Haloferax volcanii* | **Curate as uncertain**: envelope support/stabilization is well supported; **do not overstate** as demonstrated determinant of square shape |
| External capsule / putative halomucin layer | retains water during drying | cell surface / extracellular aqueous shield | AFM drying experiment directly shows a soft external capsule that tears/collapses with water loss; assignment to halomucin is explicitly tentative from genome prediction (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8, dyallsmith2011haloquadratumwalsbyi pages 1-2) | *Haloquadratum walsbyi* | **Curate as uncertain** for capsule → water-retention/desiccation protection; **do not** assert confirmed halomucin identity without stronger evidence |
| Gas vesicles | confer buoyancy and aid positioning parallel to water surface | light-exposed surface orientation | Morphology paper describes gas vesicles and states they aid buoyancy and surface-parallel positioning; presence is directly observed, orientation function is biologically plausible but not a direct square-shape mechanism (saponetti2011morphologicalandstructural pages 2-3, saponetti2011morphologicalandstructural pages 3-5, dyallsmith2011haloquadratumwalsbyi pages 1-2) | *Haloquadratum walsbyi* | **Curate with caution** as physiology/ecology edge; **not** a direct causal edge to square shape |
| Cell-wall associated genomic island (GI1) | encodes putative | S-layer / cell-surface glycoprotein / envelope formation genes | Direct comparative metagenomic evidence; functions are largely putative, with strain wall-structure differences noted but not experimentally linked to square morphology (martincuadrado2015diversityofthe pages 1-2, dyallsmith2011haloquadratumwalsbyi pages 1-2) | *Haloquadratum walsbyi* | **Curate as uncertain genetic contributor to envelope variation**; **do not** curate as proven square-shape determinant |
| Direct square-shape determinant | demonstrated in | *H. walsbyi* | No direct perturbation or mutant evidence identified in retrieved sources (dyallsmith2011haloquadratumwalsbyi pages 1-2, saponetti2011morphologicalandstructural pages 1-2, martincuadrado2015diversityofthe pages 1-2) | *Haloquadratum walsbyi* | **Do not curate** any single gene/protein as established cause of METPO:1000694 at present |
| CetZ/FtsZ tubulin-like proteins | modify cell shape in biofilms | archaeal morphology | Direct deletion evidence exists only in comparator haloarchaeon *Haloferax volcanii*, not in *H. walsbyi* (cooper2023archaealtubulinlikeproteins pages 1-2) | comparator *Haloferax volcanii* | **Comparator-only / not curate** for *H. walsbyi* square shape; may inform hypothesis generation only |


*Table: This table summarizes the strongest candidate causal edges and near-edge relationships relevant to METPO:1000694 square-shaped morphology. It separates direct environmental and structural evidence from uncertain or comparator-only claims, helping prevent over-curation.*

More explicit source-backed triples are given below.

| Subject | Predicate | Object | Reference and supporting snippet | Curation notes |
|---|---|---|---|---|
| High environmental salt concentration | enables growth of | *H. walsbyi* square cells | DOI 10.1371/journal.pone.0020968: “Cell growth requires salt concentrations of at least 14% w/v.” (dyallsmith2011haloquadratumwalsbyi pages 1-2) | **Strong for growth**, not direct geometry. Curate as an environmental prerequisite or context edge rather than `causes square shaped`.
| MgCl₂ >1 M | increases | *H. walsbyi* cell density | DOI 10.1371/journal.pone.0020968: “it achieves higher cell densities in media with >1 M MgCl₂.” (dyallsmith2011haloquadratumwalsbyi pages 1-2) | **Direct physiological association**; not a shape edge.
| S-layer glycoprotein lattice | forms part of | *H. walsbyi* cell envelope | DOI 10.1371/journal.pone.0018653: AFM “demonstrate[s]” a corrugation of “16–20 nm attributed to the…S-layer protein lattice.” (saponetti2011morphologicalandstructural pages 1-2) | **Direct structural evidence.** Appropriate for an envelope graph.
| S-layer | mechanically stabilizes | archaeal cell envelope | DOI 10.1371/journal.pone.0018653: in many archaea the S-layer “provides…a mechanical stabilizing function.” (saponetti2011morphologicalandstructural pages 5-8) | **General mechanistic knowledge**, not square-specific perturbation evidence.
| S-layer lattice | contributes to maintenance of | square-shaped morphology | Combined AFM observation and general S-layer function. (kugelgen2021completeatomicstructure pages 1-3, saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8) | **Uncertain/inferred.** Curate only with an uncertainty qualifier such as `contributes_to` or `hypothesized_to_maintain`; do not use a strong `causes` predicate.
| External capsule | retains/provides reservoir for | cell-associated water during drying | Drying AFM showed loss of capsule and declining cell volume with water loss. (saponetti2011morphologicalandstructural pages 5-8) | **Moderate evidence** for a physical water-associated layer; function inferred from dynamics.
| Halomucin | forms | external capsule | DOI 10.1371/journal.pone.0018653: capsule “might correspond to the giant protein halomucin.” (saponetti2011morphologicalandstructural pages 1-2) | **Weak, explicitly tentative.** Do not curate as an asserted identity.
| Halomucin | protects against | desiccation | DOI 10.1371/journal.pone.0020968: a 9,159-aa secreted protein that “probably protects against cell desiccation.” (dyallsmith2011haloquadratumwalsbyi pages 1-2) | **Predicted/inferred**, without knockout or purified-protein evidence.
| Gas vesicles | confer | buoyancy | DOI 10.1371/journal.pone.0018653: “Gas vesicles…confer buoyancy.” (saponetti2011morphologicalandstructural pages 3-5) | **Biologically established but not experimentally isolated in this study.** Curatable as physiology.
| Gas-vesicle-mediated buoyancy | aids | positioning near and parallel to water surface | Same source: vesicles “aid cells to position themselves close and parallel to the water surface.” (saponetti2011morphologicalandstructural pages 3-5) | **Plausible functional edge**, not square morphogenesis.
| Surface-parallel positioning | increases opportunity for | absorption by photoactive retinal proteins | Same source: positioning thereby “optimizing light absorption by the photoactive retinal proteins.” (saponetti2011morphologicalandstructural pages 3-5) | **Adaptive interpretation.** Useful in an ecological mechanism branch; uncertain if no direct light-uptake experiment is represented.
| GI1 cell-wall-associated island | contains genes putatively involved in | S-layer biosynthesis, surface glycoproteins, and envelope formation | DOI 10.1186/s12864-015-1794-8: islands “predominantly contained genes putatively involved in biosynthesis of surface layer…cell surface glycoproteins…and envelope formation.” (martincuadrado2015diversityofthe pages 1-2) | **Direct sequence content, putative function.** Curate gene-content edges with annotation qualifiers.
| GI1 variation | associated with | differences in wall-layer architecture | HBSQ001 is triple-layered and C23 two-layered; the difference was hypothesized to result from GI1 content and “remains to be established experimentally.” (dyallsmith2011haloquadratumwalsbyi pages 1-2, martincuadrado2015diversityofthe pages 1-2) | **Do not assert causality.** Association/hypothesis only.
| FtsZ/CetZ proteins | modify | haloarchaeal cell morphology | In *H. volcanii*, deletion of all eight tubulin-like genes significantly affected biofilm morphology. (cooper2023archaealtubulinlikeproteins pages 1-2) | **Direct but wrong taxon and phenotype.** Keep in a hypothesis section, not the *H. walsbyi* causal graph.

## 5. Recommended minimal graph for `square_shaped.yaml`

A defensible initial graph should separate **phenotype-supporting context** from the unresolved square-shape determinant:

1. `NaCl-saturated brine —enables_growth_of→ Haloquadratum walsbyi`
2. `Haloquadratum walsbyi —has_cellular_component→ S-layer lattice`
3. `S-layer lattice —mechanically_stabilizes→ cell envelope`
4. `cell-envelope mechanical stabilization —contributes_to [UNCERTAIN]→ METPO:1000694`
5. `Haloquadratum walsbyi —has_cellular_component→ external capsule`
6. `external capsule —contributes_to [UNCERTAIN]→ water retention during drying`
7. `halomucin —forms [UNCERTAIN]→ external capsule`
8. `gas vesicle —enables→ buoyancy`
9. `buoyancy —promotes [UNCERTAIN]→ surface-parallel positioning`
10. `surface-parallel positioning —promotes [UNCERTAIN]→ retinal-protein light exposure`

Only edge 4 should connect the envelope branch to the target morphology, and it must remain explicitly uncertain. Gas-vesicle, light-harvesting, PHB, and desiccation branches explain ecological success or associated physiology, not the square outline itself.

## 6. Recent developments and expert analysis

### 2023: archaeal cytoskeletal morphology mechanisms

Deletion analysis in *H. volcanii* showed that FtsZ1/FtsZ2 and six CetZ homologs affect morphology during early biofilm development. Different deletions yielded longer, rounder, filamentous, or flat amorphous cells. This establishes that archaeal tubulin-like proteins can be causal morphology regulators, but the result is taxon- and condition-specific and does not identify a square-cell program. It supplies a strong experimental template for future *H. walsbyi* work: inducible depletion, CRISPR interference, or heterologous reconstruction of candidate division/cytoskeletal genes. Published 25 September 2023. (cooper2023archaealtubulinlikeproteins pages 1-2)

### 2024: ecological and taxonomic context

Oren’s 2024 review emphasized rapid expansion of knowledge from cultivation-independent methods and identified *Haloquadratum* as a major genus in hypersaline-biogeography studies. Cui and colleagues reported that, as of December 2023, Halobacteria comprised **two orders, nine families, 82 genera, and 357 validly named species** and recommended phylogenomics and genome-relatedness metrics for taxonomic description. These sources demonstrate an increasingly mature ecological and taxonomic framework, while square-shape causality remains a conspicuous mechanistic gap. Published March and August 2024, respectively. (cui2024proposedminimalstandards pages 1-2, oren2024novelinsightsinto pages 1-2)

### Expert interpretation

The available evidence favors an **anisotropic envelope-growth/stabilization model**, consistent with the supplied foundational cell-shape review, but it does not reveal how four approximately orthogonal edges are generated. A square S-layer lattice should not automatically be treated as the geometric template: protein-lattice symmetry and whole-cell outline are different organizational scales, and HBSQ001 and C23 retain square morphology despite different wall-layer architecture. The highest-value unresolved questions are where new S-layer is inserted, how division planes are selected, whether corners are stable growth zones or mechanical singularities, and whether cytoskeletal proteins pattern envelope expansion.

## 7. Applications and real-world relevance

There is no established industrial application of square cell shape itself. Current relevance is primarily:

- **Model-system biology:** an extreme example for testing physical and genetic principles of archaeal cell shape.
- **Hypersaline ecosystem monitoring:** the distinctive morphology and frequent high abundance make *H. walsbyi* recognizable in crystallizer communities, although modern monitoring should combine imaging with molecular identification.
- **Astrobiology and limits-of-life research:** ultrathin haloarchaea provide models for survival at low water activity and extreme ionic strength. The morphological trait should not itself be treated as a biosignature without taxonomic and chemical corroboration.
- **Biotechnology-adjacent components:** gas vesicles are being developed broadly as genetically encodable imaging and therapeutic platforms, but that application concerns the organelle and does not depend on square morphology.
- **Biopolymer research:** abundant PHB granules have potential relevance to biodegradable-polymer production, but *H. walsbyi* cultivation difficulty and lack of demonstrated shape-dependent productivity limit direct implementation. (saponetti2011morphologicalandstructural pages 5-8)

## 8. Warnings: claims not ready for TraitMech curation

1. **Do not curate halomucin as the confirmed capsule protein.** The source uses “might correspond.”
2. **Do not curate halomucin as a demonstrated square-shape determinant.** Its proposed role is desiccation protection, without perturbation evidence.
3. **Do not curate the 16–20 nm S-layer lattice as sufficient to create square geometry.** Presence and periodicity are directly observed; shape causality is not.
4. **Do not infer that a square lattice at the nanometer scale necessarily produces a square cell at the micrometer scale.**
5. **Do not curate gas vesicles, PHB/PHA granules, bacteriorhodopsins, or glycerol metabolism as direct causes of square shape.** They are associated physiological features.
6. **Do not transfer FtsZ/CetZ deletion phenotypes from *H. volcanii* to *H. walsbyi*.** They are comparator evidence only. (cooper2023archaealtubulinlikeproteins pages 1-2)
7. **Do not treat high salt as a direct shape-inducing signal.** The evidence establishes a growth requirement, not a salt-dependent square-to-round transition.
8. **Do not assert GI1 causes wall-layer number or square shape.** The published link to wall architecture explicitly remains to be established experimentally. (martincuadrado2015diversityofthe pages 1-2)
9. **Do not equate ecological dominance with adaptive proof for square shape.** Up to 80% abundance is striking but does not isolate the fitness contribution of geometry.
10. **Avoid unverified CURIEs.** Strain-specific genes, proteins, and environmental terms should remain label-only until checked in UniProt, NCBITaxon, GO, and ENVO.

## 9. DOI-first bibliography

1. Saponetti MS, Bobba F, Salerno G, Scarfato A, Corcelli A, Cucolo A. “Morphological and Structural Aspects of the Extremely Halophilic Archaeon *Haloquadratum walsbyi*.” *PLoS ONE* 6:e18653. **Published 29 April 2011.** DOI: [10.1371/journal.pone.0018653](https://doi.org/10.1371/journal.pone.0018653). Primary AFM source for dimensions, S-layer periodicity, gas vesicles, and capsule observations. (saponetti2011morphologicalandstructural pages 1-2, saponetti2011morphologicalandstructural pages 5-8, saponetti2011morphologicalandstructural pages 2-3, saponetti2011morphologicalandstructural pages 3-5)
2. Dyall-Smith ML et al. “*Haloquadratum walsbyi*: Limited Diversity in a Global Pond.” *PLoS ONE* 6:e20968. **Published 20 June 2011.** DOI: [10.1371/journal.pone.0020968](https://doi.org/10.1371/journal.pone.0020968). Comparative genomics, salinity requirement, MgCl₂ response, abundance, wall architecture, and halomucin prediction. (dyallsmith2011haloquadratumwalsbyi pages 1-2)
3. Martin-Cuadrado A-B, Pašić L, Rodriguez-Valera F. “Diversity of the cell-wall associated genomic island of the archaeon *Haloquadratum walsbyi*.” *BMC Genomics* 16:603. **Published August 2015.** DOI: [10.1186/s12864-015-1794-8](https://doi.org/10.1186/s12864-015-1794-8). Cell-wall genomic-island diversity and putative envelope genes. (martincuadrado2015diversityofthe pages 1-2)
4. von Kügelgen A, Alva V, Bharat TAM. “Complete atomic structure of a native archaeal cell surface.” *Cell Reports* 37:110052. **Published 23 November 2021.** DOI: [10.1016/j.celrep.2021.110052](https://doi.org/10.1016/j.celrep.2021.110052). Authoritative structural evidence for general archaeal S-layer organization and functions in comparator *H. volcanii*. (kugelgen2021completeatomicstructure pages 1-3)
5. Cooper A, Makkay AM, Papke RT. “Archaeal Tubulin-like Proteins Modify Cell Shape in *Haloferax volcanii* during Early Biofilm Development.” *Genes* 14:1861. **Published 25 September 2023.** DOI: [10.3390/genes14101861](https://doi.org/10.3390/genes14101861). Direct comparator evidence for FtsZ/CetZ-dependent morphology. (cooper2023archaealtubulinlikeproteins pages 1-2)
6. Cui H-L et al. “Proposed minimal standards for description of new taxa of the class Halobacteria.” *International Journal of Systematic and Evolutionary Microbiology* 74:006290. **Published March 2024.** DOI: [10.1099/ijsem.0.006290](https://doi.org/10.1099/ijsem.0.006290). Current authoritative taxonomy and characterization standards. (cui2024proposedminimalstandards pages 1-2)
7. Oren A. “Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems.” *npj Biodiversity* 3:18. **Published August 2024.** DOI: [10.1038/s44185-024-00050-w](https://doi.org/10.1038/s44185-024-00050-w). Recent expert review of hypersaline diversity, ecology, and *Haloquadratum* biogeography. (oren2024novelinsightsinto pages 1-2)

## Final curation recommendation

Retain **METPO:1000694** as a clearly defined planar morphology and build the initial graph around **hypersaline growth context → S-layer/cell-envelope architecture → uncertain mechanical maintenance of square geometry**. Represent capsule/halomucin, gas vesicles, retinal proteins, and PHA granules as associated adaptation branches. The graph should explicitly encode that the decisive morphogenetic machinery—particularly anisotropic envelope insertion, corner formation, and division-plane control—remains unknown.

References

1. (saponetti2011morphologicalandstructural pages 1-2): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

2. (saponetti2011morphologicalandstructural pages 2-3): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

3. (kugelgen2021completeatomicstructure pages 1-3): Andriko von Kügelgen, Vikram Alva, and Tanmay A.M. Bharat. Complete atomic structure of a native archaeal cell surface. Cell Reports, 37:110052, Nov 2021. URL: https://doi.org/10.1016/j.celrep.2021.110052, doi:10.1016/j.celrep.2021.110052. This article has 61 citations and is from a highest quality peer-reviewed journal.

4. (saponetti2011morphologicalandstructural pages 5-8): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

5. (martincuadrado2015diversityofthe pages 1-2): Ana-Belen Martin-Cuadrado, Lejla Pašić, and Francisco Rodriguez-Valera. Diversity of the cell-wall associated genomic island of the archaeon haloquadratum walsbyi. BMC Genomics, Aug 2015. URL: https://doi.org/10.1186/s12864-015-1794-8, doi:10.1186/s12864-015-1794-8. This article has 26 citations and is from a peer-reviewed journal.

6. (cooper2023archaealtubulinlikeproteins pages 1-2): Alexei Cooper, Andrea M. Makkay, and R. Thane Papke. Archaeal tubulin-like proteins modify cell shape in haloferax volcanii during early biofilm development. Genes, 14:1861, Sep 2023. URL: https://doi.org/10.3390/genes14101861, doi:10.3390/genes14101861. This article has 1 citations.

7. (dyallsmith2011haloquadratumwalsbyi pages 1-2): Mike L. Dyall-Smith, Friedhelm Pfeiffer, Kathrin Klee, Peter Palm, Karin Gross, Stephan C. Schuster, Markus Rampp, and Dieter Oesterhelt. Haloquadratum walsbyi : limited diversity in a global pond. PLoS ONE, 6:e20968, Jun 2011. URL: https://doi.org/10.1371/journal.pone.0020968, doi:10.1371/journal.pone.0020968. This article has 141 citations and is from a peer-reviewed journal.

8. (oren2024novelinsightsinto pages 1-2): Aharon Oren. Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems. npj Biodiversity, Aug 2024. URL: https://doi.org/10.1038/s44185-024-00050-w, doi:10.1038/s44185-024-00050-w. This article has 73 citations and is from a peer-reviewed journal.

9. (saponetti2011morphologicalandstructural pages 3-5): Matilde Sublimi Saponetti, Fabrizio Bobba, Grazia Salerno, Alessandro Scarfato, Angela Corcelli, and Annamaria Cucolo. Morphological and structural aspects of the extremely halophilic archaeon haloquadratum walsbyi. PLoS ONE, 6:e18653, Apr 2011. URL: https://doi.org/10.1371/journal.pone.0018653, doi:10.1371/journal.pone.0018653. This article has 23 citations and is from a peer-reviewed journal.

10. (cui2024proposedminimalstandards pages 1-2): Heng-Lin Cui, Jing Hou, Mohammad Ali Amoozegar, Mike L. Dyall-Smith, Rafael R. de la Haba, Hiroaki Minegishi, Rafael Montalvo-Rodriguez, Aharon Oren, Cristina Sanchez-Porro, Antonio Ventosa, and Russell H. Vreeland. Proposed minimal standards for description of new taxa of the class halobacteria. Mar 2024. URL: https://doi.org/10.1099/ijsem.0.006290, doi:10.1099/ijsem.0.006290. This article has 49 citations and is from a peer-reviewed journal.