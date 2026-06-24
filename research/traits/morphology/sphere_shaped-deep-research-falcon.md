---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:26:08.926251'
end_time: '2026-06-18T09:41:17.412539'
duration_seconds: 908.49
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: sphere shaped
  trait_identifier: METPO:1000683
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: sphere_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a spherical or nearly spherical
    morphology with roughly equal dimensions in all directions.
  parent_traits: METPO:1000666
  synonyms: S_sphere, sphere-shaped
  evidence_summary: 'DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan
    only at the division septum (Supports spherical bacterial morphology as associated
    with septal peptidoglycan synthesis.)'
  causal_graph_summary: 'sphere_shaped_septal_peptidoglycan: 5 nodes, 4 edges'
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
- **Trait label:** sphere shaped
- **METPO identifier:** METPO:1000683
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_sphere, sphere-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports spherical bacterial morphology as associated with septal peptidoglycan synthesis.)
- **Existing causal graph summary:** sphere_shaped_septal_peptidoglycan: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **sphere shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sphere_shaped.yaml`.

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
- **Trait label:** sphere shaped
- **METPO identifier:** METPO:1000683
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_sphere, sphere-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports spherical bacterial morphology as associated with septal peptidoglycan synthesis.)
- **Existing causal graph summary:** sphere_shaped_septal_peptidoglycan: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **sphere shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sphere_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **sphere shaped** (METPO:1000683)

### 0. Scope summary (curation-oriented)
**Trait meaning.** *Sphere shaped* refers to a microbial cell morphology in which the cell body is spherical or nearly spherical (coccoid), with roughly equal dimensions in all directions (METPO:1000683). In the bacterial literature, “cocci/coccoid” is used for round-shaped/spherical cells and may include near-spherical elongated ellipsoids (“ovococci”) as a related but distinct boundary case. (pinho2013howtoget pages 1-2)

**Primary mechanistic interpretation for TraitMech.** A key mechanistic signature for **true spherical cocci** is that **new peptidoglycan (PG) is synthesized mainly/only at the division septum**, rather than along a lateral sidewall; ovococci/ellipsoids instead combine **septal** and **peripheral** PG synthesis near midcell, which produces an ovoid (non-spherical) outline. (pinho2013howtoget pages 2-3, pinho2013howtoget pages 4-5, pinho2013howtoget pages 3-4, pinho2013howtoget media 4ccf0bcc)

**Boundary cases to distinguish during curation.**
- **Ovococci / elongated ellipsoids:** may be annotated as “round/coccoid” in general descriptions but are mechanistically and phenotypically distinct because they exhibit peripheral PG insertion and measurable elongation. (pinho2013howtoget pages 4-5, ramosleon2025howdospherical pages 2-3, pinho2013howtoget media 4ccf0bcc)
- **Arrangement traits (not the same as cell shape):** diplococci, tetrads, sarcina (packaging/arrangement) can be spherical yet differ in division plane selection; treat as separate downstream traits if present in the ontology. The present evidence set focuses on single-cell geometry and PG insertion pattern rather than multicell arrangement. (ramosleon2025howdospherical pages 10-11)

**Assay-observed nature.** The trait is typically observed by microscopy and can be operationalized by segmentation metrics such as **eccentricity** (near 0 for a circle; higher for elongated shapes). A recent S. aureus morphogenesis study explicitly screened mutants for altered **cell eccentricity** as a quantitative proxy for roundness/sphericity. (costa2024theroleof pages 6-8)

---

### 1. Key concepts & definitions (current understanding)

#### 1.1 “Sphere shaped” as a cell-wall growth program
A widely used conceptual definition in cocci is that **cell shape reflects where and when PG is inserted** into the sacculus (cell wall “exoskeleton”). Spherical cocci synthesize PG at the **division septum**, and the resulting hemispherical daughter surfaces arise as septal wall is built and then split. (pinho2013howtoget pages 3-4, pinho2013howtoget pages 1-2)

Pinho et al. (Nature Reviews Microbiology, 2013) summarize this mapping explicitly: spherical cocci “synthesize cell wall mainly, if not only, at the division septum” using one main wall synthesis machinery, whereas ovococci have both septal and peripheral synthesis. (pinho2013howtoget pages 2-3)

#### 1.2 Core mechanistic modules
Key modules implicated across the evidence set:
- **Divisome / septal synthesis module:** FtsZ-based cytokinetic ring recruits septal PG synthesis machinery and organizes septum formation. (pinho2013howtoget pages 5-6)
- **SEDS–bPBP synthase pairs:** In many bacteria, paired glycosyltransferase (SEDS proteins such as FtsW or RodA) and class B PBPs execute polymerization/crosslinking; these pairs partition “division” vs “elongation” functions. (battaje2023modelsversuspathogens pages 3-4)
- **Lipid II supply & translocation:** PG precursor lipid II is a key substrate; in cocci, the septally localized flippase **FtsW** is described as flipping lipid II to the outside, enabling PBPs to synthesize septal PG. (pinho2013howtoget pages 2-3)
- **Crosslinking and remodeling:** Highly crosslinked septal PG is associated with late recruitment of enzymes such as PBP4 in S. aureus; autolysins (e.g., Atl) split septa to separate daughters. (pinho2013howtoget pages 2-3, pinho2013howtoget pages 3-4)

---

### 2. Recent developments & latest research (prioritize 2023–2024)

#### 2.1 2024: **GpsB** as a morphogenesis regulator in *Staphylococcus aureus*
A 2024 mBio study (Costa et al., **Mar 2024**, DOI: **10.1128/mbio.03235-23**) used a large-scale mutant screen and mechanistic follow-up to show that **GpsB is required for normal S. aureus morphogenesis**, acting through the **spatiotemporal regulation of PBPs**. The paper reports a screen of **~1,920 nonessential transposon mutants** for altered **cell eccentricity**, identifying known elongation factors (RodA/PBP3) and additional determinants including **GpsB**. (costa2024theroleof pages 6-8)

Mechanistically, **gpsB deletion** causes **partial delocalization of PBP2 and PBP4 from the septum toward the periphery**, with increased peripheral PG synthesis; this shift is linked to cells becoming **more spherical** (rounder) and losing mild elongation. (costa2024theroleof pages 1-2, costa2024theroleof pages 11-13)

This is directly actionable for causal graph curation because it provides experimentally supported edges connecting a regulator (GpsB) → localization of enzymatic machinery (PBP2/PBP4) → PG insertion pattern → spherical morphology. (costa2024theroleof pages 11-13)

#### 2.2 2023: Updated synthesis on **FtsZ treadmilling** organizing septal PG synthesis
A 2023 review (Battaje et al., **Feb 2023**, DOI: **10.1042/bsr20221664**) emphasizes a now-standard concept: **FtsZ treadmilling distributes septal PG synthases around the Z-ring**, thereby organizing septal PG synthesis. The review explicitly states that “FtsZ polymers undergo treadmilling around the Z-ring to distribute the PG synthases forming the septum,” and links cocci/ovococci to septum-focused PG synthesis coordinated by FtsZ. (battaje2023modelsversuspathogens pages 3-4)

This supports graph edges from FtsZ dynamics → distribution/organization of septal PG synthases → septal PG synthesis (and, in cocci, to spherical geometry). (battaje2023modelsversuspathogens pages 3-4)

#### 2.3 2024: Septal envelope microenvironments via LTA metabolism (shape link is indirect)
A 2024 mBio paper (Ibrahim et al., **Feb 2024**, DOI: **10.1128/mbio.02852-23**) dissects how **LtaS processing and its glycolipid substrate Glc2-DAG** restrict lipoteichoic acid (LTA) assembly and septal trafficking of certain surface proteins into cross-walls. The paper reports that depletion of **ltaS** or catalytically inactive **LtaS** abolishes restricted septal trafficking of YSIRK precursors to septal membranes; Glc2-DAG pathway mutants (ypfP/ltaA) similarly disrupt septal targeting. (ibrahim2024processingofltas pages 1-2, ibrahim2024processingofltas pages 2-5)

For TraitMech, these findings provide high-confidence nodes/edges for **septal envelope organization**, but the direct link to “sphere shaped” morphology is **not explicit** in the retrieved excerpts and should be marked **uncertain/indirect** for a sphere-shaped graph unless additional direct morphology/shape data are curated from the full paper. (ibrahim2024processingofltas pages 2-5)

---

### 3. Current applications & real-world implementations

1. **Antibiotic mechanism/target interpretation via morphotypes.** Because spherical cocci emphasize septal PG synthesis and divisome activity, perturbations of divisome-associated PBPs/SEDS proteins or their regulators often yield characteristic cell-wall and shape phenotypes. A practical implementation in research and diagnostics is the use of shape changes (rounding, elongation, chaining) as readouts of cell-wall-active antibiotic action or genetic perturbations of PG synthesis machinery. This connection is supported by mechanistic links among FtsZ, FtsW/SEDS pairs, PBPs, and septal PG synthesis. (battaje2023modelsversuspathogens pages 3-4, pinho2013howtoget pages 2-3)

2. **High-throughput morphogenomics.** The 2024 S. aureus work demonstrates a scalable approach: screen a mutant library for **cell eccentricity** differences (roundness) to identify determinants of near-spherical vs slightly elongated cocci; this is directly useful for trait-based genotype–phenotype mapping pipelines. (costa2024theroleof pages 6-8)

3. **Microscopy-based PG insertion mapping.** The schematic and experimental depiction of septal-only vs septal+peripheral PG insertion (including the use of fluorescent D-amino acid labeling) is a mature and widely used implementation for discriminating cocci vs ovococci growth programs. (pinho2013howtoget media 4ccf0bcc, pinho2013howtoget media a4f51ba8)

---

### 4. Expert opinions & synthesis (authoritative sources)

**“Shape follows insertion.”** Pinho et al. (Nature Reviews Microbiology) articulate a synthesis that is still widely used: in coccoid bacteria, cell geometry can often be explained by where PG synthesis occurs, and spherical cocci are characterized by septum-focused synthesis. (pinho2013howtoget pages 2-3, pinho2013howtoget pages 3-4)

**FtsZ as an organizer, not merely a scaffold.** The 2023 review frames FtsZ treadmilling as a dynamic organizer that distributes PG synthases around the division plane and thus patterns septal PG synthesis. (battaje2023modelsversuspathogens pages 3-4)

**Morphology as a regulated balance between synthesis modes in cocci.** Costa et al. (2024) provide a refined view for S. aureus: even “spherical” S. aureus can undergo mild elongation driven by RodA/PBP3, and regulators like GpsB tune PBP localization to preserve correct morphology. (costa2024theroleof pages 1-2, costa2024theroleof pages 11-13)

---

### 5. Candidate nodes for `sphere_shaped` causal graph (grouped)

#### 5.1 Phenotype nodes
- **sphere shaped** (METPO:1000683)
- label-only: **ovoid/ovococcal morphology** (boundary case; not equivalent)
- label-only: **cell eccentricity** (assay metric for roundness/sphericity) (costa2024theroleof pages 6-8)

#### 5.2 Biological process / localization nodes (GO-suggested)
- **peptidoglycan biosynthetic process** (GO:0009252) (pinho2013howtoget pages 2-3)
- label-only: **septal peptidoglycan synthesis** (subprocess of GO:0009252) (pinho2013howtoget pages 2-3)
- label-only: **peripheral peptidoglycan synthesis** (ovococci) (pinho2013howtoget pages 4-5)
- **cytokinetic ring assembly** (GO:0000921; for FtsZ Z-ring) (pinho2013howtoget pages 5-6)
- label-only: **division septum** (cellular location / process context) (pinho2013howtoget pages 5-6)
- **peptidoglycan cross-linking** (GO:0046677) (pinho2013howtoget pages 2-3)
- **peptidoglycan catabolic process** (GO:0009253) (septum splitting/autolysis) (pinho2013howtoget pages 3-4)

#### 5.3 Genes/proteins/complexes (grounding varies by taxon)
- **FtsZ** (tubulin-like division protein; UniProt varies by organism) (battaje2023modelsversuspathogens pages 3-4, pinho2013howtoget pages 5-6)
- **FtsW** (SEDS family; lipid II translocation; UniProt varies) (pinho2013howtoget pages 2-3)
- **PBPs** (penicillin-binding proteins) including:
  - *S. aureus* **PBP2** (class A; TG+TP activities) (pinho2013howtoget pages 2-3)
  - *S. aureus* **PBP1**, **PBP4** (septal-associated; PBP4 crosslinking) (pinho2013howtoget pages 2-3)
  - *S. pneumoniae* **PBP2x** (septal; inhibition elongates), **PBP2b** (peripheral; deletion yields spherical) (pinho2013howtoget pages 5-6)
- **GpsB** (*S. aureus* morphogenesis regulator) (costa2024theroleof pages 1-2, costa2024theroleof pages 11-13)
- **RodA/PBP3** (SEDS/bPBP pair implicated in elongation in S. aureus) (costa2024theroleof pages 11-13)
- **Atl** (S. aureus autolysin implicated in septum splitting) (pinho2013howtoget pages 3-4)
- **MapZ** (*S. pneumoniae* Z-ring positioning; boundary-case for ovococci) (ramosleon2025howdospherical pages 2-3)

#### 5.4 Chemical nodes (CHEBI-suggested)
- **lipid II** (CHEBI:59911) (pinho2013howtoget pages 2-3)
- label-only: **wall teichoic acids** / **teichoic acid** (CHEBI:64373) (pinho2013howtoget pages 3-4)
- label-only: **Glc2-DAG**, **phosphatidylglycerol**, **diacylglycerol**, **lipoteichoic acid** (LTA pathway; shape link uncertain) (ibrahim2024processingofltas pages 1-2, ibrahim2024processingofltas pages 2-5)

---

### 6. Evidence-backed candidate causal edges (curation-ready)
The table below is intended for direct translation into `data/traits/morphology/sphere_shaped.yaml` after curator review.

| Edge (subject—predicate—object) | Edge type | Taxon scope | Suggested node grounding | Evidence snippet | Reference (DOI + URL + year) | Evidence ID |
|---|---|---|---|---|---|---|
| septal peptidoglycan synthesis — contributes_to — sphere shaped morphology | mechanistic | cocci | GO:0009252 peptidoglycan biosynthetic process; METPO:1000683 sphere shaped | “spherical cocci synthesize peptidoglycan only at the division septum” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 3-4) |
| loss of MreB-mediated elongation machinery — causes — loss of elongation capacity | mechanistic | broad/cocci | UniProt:P0A9X4 MreB (generic bacterial homolog); GO:0007010 cytoskeleton organization | “loss of the MreB cytoskeleton is the main factor that prevents cocci from elongating into rods” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 11-11) |
| loss of elongation capacity — contributes_to — sphere shaped morphology | mechanistic | broad/cocci | label-only: loss_of_elongation_capacity; METPO:1000683 | “prevents cocci from elongating into rods” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 11-11) |
| FtsZ Z-ring assembly at mid-cell — recruits — divisome/PBPs | regulatory | broad/cocci | UniProt:P0A9A6 FtsZ (generic); GO:0000921 cytokinetic ring assembly; GO:0032153 cell division site | “cell division is initiated by FtsZ assembly into a mid-cell Z ring that recruits PBPs and divisome components” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 5-6) |
| FtsZ treadmilling — organizes — septal peptidoglycan synthesis | regulatory | broad/cocci | UniProt:P0A9A6 FtsZ; GO:0009252 | “The FtsZ polymers undergo treadmilling around the Z-ring to distribute the PG synthases forming the septum” | 10.1042/bsr20221664 · https://doi.org/10.1042/bsr20221664 · 2023 | (battaje2023modelsversuspathogens pages 3-4) |
| FtsW — flips/translocates — lipid II to outer septal face | mechanistic | cocci | UniProt:P0ABG4 FtsW (generic); CHEBI:59911 lipid II | “lipid II is flipped to the outside by the septally localized flippase FtsW” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 2-3) |
| lipid II at septum — enables substrate_for — septal PBP-mediated peptidoglycan synthesis | mechanistic | cocci | CHEBI:59911 lipid II; GO:0009252 | “PG synthesis uses lipid II as the PBP substrate” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 2-3) |
| PBP2 — catalyzes — septal peptidoglycan synthesis | mechanistic | S. aureus | label-only: PBP2_Staphylococcus_aureus; GO:0009252 | “in Staphylococcus aureus the HMM class A PBP2 provides transglycosylase and transpeptidase activities” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 2-3) |
| PBP1 — part_of — divisome-associated septal synthesis machinery | mechanistic | S. aureus | label-only: PBP1_Staphylococcus_aureus; GO:0000917 division septum assembly | “PBP1 is described as part of the divisome” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 2-3) |
| wall teichoic acid synthesis at septum — recruits — PBP4 to septum | regulatory | S. aureus | CHEBI:64373 teichoic acid; label-only: PBP4_Staphylococcus_aureus | “PBP4 is recruited later (via septal wall teichoic acid synthesis)” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 3-4) |
| PBP4 septal localization — increases — peptidoglycan crosslinking | mechanistic | S. aureus | label-only: PBP4_Staphylococcus_aureus; GO:0046677 peptidoglycan cross-linking | “PBP4 is recruited to the septum to generate highly crosslinked peptidoglycan” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 2-3) |
| Atl autolysin — mediates — septum splitting | process | S. aureus | label-only: Atl_Staphylococcus_aureus; GO:0009253 peptidoglycan catabolic process | “in S. aureus Atl is the only autolysin identified so far with a role in septum splitting” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 3-4) |
| septum splitting — enables — hemispherical daughter-cell bulging | mechanistic | cocci | label-only: septum_splitting; label-only: hemispherical_bulging | “after splitting the flat septum is pushed outward by internal osmotic pressure to form the hemispherical daughter-cell surface” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 3-4) |
| PBP2b/RodA peripheral peptidoglycan synthesis — contributes_to — ovoid/ovococcal morphology | mechanistic | ovococci/S. pneumoniae | label-only: PBP2b_Streptococcus_pneumoniae; label-only: RodA_Streptococcus_pneumoniae; GO:0009252 | “peripheral synthesis is carried out by the elongasome with the PBP2b/RodA complex” | 10.1042/bst20240956 · https://doi.org/10.1042/bst20240956 · 2025 | (ramosleon2025howdospherical pages 2-3) |
| inhibition of PBP2x (septal PBP) — causes — cell elongation | mechanistic | ovococci | label-only: PBP2x_Streptococcus_pneumoniae | “inhibition of PBP2x (a septal PBP) causes ovococci to elongate” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 5-6) |
| deletion of PBP2b (peripheral PBP) — causes — spherical cells | mechanistic | ovococci | label-only: PBP2b_Streptococcus_pneumoniae; METPO:1000683 | “deletion of PBP2b (a peripheral PBP) leads to spherical cells” | 10.1038/nrmicro3088 · https://doi.org/10.1038/nrmicro3088 · 2013 | (pinho2013howtoget pages 5-6) |
| MapZ — positions/anchors — FtsZ ring at mid-cell | regulatory | S. pneumoniae | label-only: MapZ_Streptococcus_pneumoniae; UniProt:P0A9A6 FtsZ (generic) | “MapZ rings… serving as anchors for FtsZ treadmilling and Z-ring placement” | 10.1042/bst20240956 · https://doi.org/10.1042/bst20240956 · 2025 | (ramosleon2025howdospherical pages 2-3) |
| RodA/PBP3-mediated midcell sidewall synthesis — promotes — mild elongation | mechanistic | S. aureus | label-only: RodA_Staphylococcus_aureus; label-only: PBP3_Staphylococcus_aureus | “RodA together with PBP3… mediates localized septal sidewall synthesis required for mild elongation” | 10.1128/mbio.03235-23 · https://doi.org/10.1128/mbio.03235-23 · 2024 | (costa2024theroleof pages 11-13) |
| gpsB deletion — causes — PBP2/PBP4 delocalization from septum to periphery | regulatory | S. aureus | label-only: GpsB_Staphylococcus_aureus; label-only: PBP2_Staphylococcus_aureus; label-only: PBP4_Staphylococcus_aureus | “deletion of gpsB causes partial delocalization of PBP2 and PBP4 from the septum to the peripheral wall” | 10.1128/mbio.03235-23 · https://doi.org/10.1128/mbio.03235-23 · 2024 | (costa2024theroleof pages 11-13) |
| PBP2/PBP4 delocalization to periphery — increases — peripheral peptidoglycan insertion/crosslinking | mechanistic | S. aureus | label-only: peripheral_PG_insertion; GO:0046677 peptidoglycan cross-linking | “increased peptidoglycan synthesis at the cell periphery versus septum in gpsB mutants” | 10.1128/mbio.03235-23 · https://doi.org/10.1128/mbio.03235-23 · 2024 | (costa2024theroleof pages 11-13) |
| increased peripheral PBP2/PBP4 activity in gpsB mutant — causes — more spherical cells | mechanistic | S. aureus | METPO:1000683; label-only: GpsB_Staphylococcus_aureus | “in the absence of GpsB, S. aureus cells become more spherical” | 10.1128/mbio.03235-23 · https://doi.org/10.1128/mbio.03235-23 · 2024 | (costa2024theroleof pages 1-2) |
| Glc2-DAG binding to LtaS — promotes — LtaS processing/poly(Gro-P) assembly at septum | regulatory (uncertain for shape) | S. aureus | label-only: Glc2-DAG; label-only: LtaS; label-only: lipoteichoic_acid | “Glc2-DAG binding to the enzyme couples catalysis by LtaS and the physical release of eLtaS” | 10.1128/mbio.02852-23 · https://doi.org/10.1128/mbio.02852-23 · 2024 | (ibrahim2024processingofltas pages 1-2) |
| disrupted Glc2-DAG/LtaS processing — perturbs — septal envelope microenvironment and septal trafficking | regulatory (uncertain/indirect for shape) | S. aureus | label-only: septal_envelope_microenvironment; label-only: YSIRK_precursor_trafficking | “failure to process LtaS timely… unique septal-lipid pool… is not established” | 10.1128/mbio.02852-23 · https://doi.org/10.1128/mbio.02852-23 · 2024 | (ibrahim2024processingofltas pages 1-2) |


*Table: This table compiles curation-ready candidate causal edges for the microbial morphology trait sphere shaped (METPO:1000683), with taxon scope, suggested grounding, direct evidence snippets, and source citations. It is designed to support TraitMech YAML graph construction while clearly flagging indirect or uncertain edges.*

**Visual support:** Figure 1 from Pinho et al. schematically and experimentally contrasts septal-only PG synthesis in spherical cocci vs septal+peripheral synthesis in ovococci; this is useful to justify top-level edges mapping synthesis mode → morphology. (pinho2013howtoget media 4ccf0bcc, pinho2013howtoget media a4f51ba8)

---

### 7. Statistics and quantitative data points (from retrieved sources)
- **~1,920 nonessential mutants** were screened for altered cell shape (eccentricity) in a transposon library approach to identify *S. aureus* elongation/morphogenesis determinants, with gpsB among the strongest phenotypes. (costa2024theroleof pages 6-8)
- In *S. aureus* LTA pathway experiments, **>70% of LtaS** in wild-type is reported as processed to a 55-kDa extracellular catalytic fragment (eLtaS), whereas ypfP/ltaA mutants show much more unprocessed LtaS; this is quantitative but pertains to septal envelope regulation rather than directly to sphericity. (ibrahim2024processingofltas pages 5-7)

---

### 8. Warnings / curation notes (what NOT to curate yet)
1. **Avoid conflating ovococci with “sphere shaped.”** Ovococci can be visually “round” but are mechanistically distinct because they show peripheral PG synthesis; curate ovococcal edges (PBP2b/RodA peripheral synthesis; MapZ positioning) only if your graph explicitly models boundary-case transitions or includes an “ovoid” node. (pinho2013howtoget pages 4-5, pinho2013howtoget media 4ccf0bcc)

2. **LTA/LtaS edges are indirect for sphere-shaped morphology in the current evidence set.** Ibrahim et al. (2024) strongly support LTA-dependent **septal targeting/trafficking** and lipid microenvironment formation, but the retrieved text does not directly quantify “sphere shaped” morphology outcomes. Treat these as candidate upstream envelope-organization nodes with **uncertain** relation to sphericity unless additional direct morphology evidence is curated from the full paper. (ibrahim2024processingofltas pages 2-5)

3. **Taxon specificity.** Some edges are strongly supported in *S. aureus* (PBP4 recruitment via teichoic acids; Atl for septum splitting; GpsB effects on PBP localization) and should be labeled as taxon-specific rather than universal for all cocci. (costa2024theroleof pages 1-2, pinho2013howtoget pages 3-4)

---

## DOI-first bibliography (with URLs and publication dates where available)

1. **Costa SF, et al.** *The role of GpsB in Staphylococcus aureus cell morphogenesis.* **mBio**. **Mar 2024**. DOI: **10.1128/mbio.03235-23**. https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2, costa2024theroleof pages 6-8, costa2024theroleof pages 11-13)

2. **Ibrahim AM, et al.** *Processing of LtaS restricts LTA assembly and YSIRK preprotein trafficking into Staphylococcus aureus cross-walls.* **mBio**. **Feb 2024**. DOI: **10.1128/mbio.02852-23**. https://doi.org/10.1128/mbio.02852-23 (ibrahim2024processingofltas pages 1-2, ibrahim2024processingofltas pages 5-7, ibrahim2024processingofltas pages 2-5)

3. **Battaje RR, et al.** *Models versus pathogens: how conserved is the FtsZ in bacteria?* **Bioscience Reports**. **Feb 2023**. DOI: **10.1042/bsr20221664**. https://doi.org/10.1042/bsr20221664 (battaje2023modelsversuspathogens pages 3-4)

4. **Pinho MG, Kjos M, Veening J-W.** *How to get (a)round: mechanisms controlling growth and division of coccoid bacteria.* **Nature Reviews Microbiology**. **Aug 2013**. DOI: **10.1038/nrmicro3088**. https://doi.org/10.1038/nrmicro3088 (pinho2013howtoget pages 2-3, pinho2013howtoget pages 4-5, pinho2013howtoget pages 3-4, pinho2013howtoget pages 11-11, pinho2013howtoget pages 1-2, pinho2013howtoget media 4ccf0bcc, pinho2013howtoget media a4f51ba8)

5. **Ramos-León F, Ramamurthi KS.** *How do spherical bacteria regulate cell division?* **Biochemical Society Transactions**. **Apr 2025**. DOI: **10.1042/bst20240956**. https://doi.org/10.1042/bst20240956 (used for contextual updates on ovococci and protein complexes where 2023–2024 sources were sparse in the current retrieval) (ramosleon2025howdospherical pages 5-6, ramosleon2025howdospherical pages 2-3)


References

1. (pinho2013howtoget pages 1-2): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

2. (pinho2013howtoget pages 2-3): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

3. (pinho2013howtoget pages 4-5): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

4. (pinho2013howtoget pages 3-4): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

5. (pinho2013howtoget media 4ccf0bcc): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

6. (ramosleon2025howdospherical pages 2-3): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.

7. (ramosleon2025howdospherical pages 10-11): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.

8. (costa2024theroleof pages 6-8): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

9. (pinho2013howtoget pages 5-6): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

10. (battaje2023modelsversuspathogens pages 3-4): Rachana Rao Battaje, Ravikant Piyush, Vidyadhar Pratap, and Dulal Panda. Models versus pathogens: how conserved is the ftsz in bacteria? Bioscience Reports, Feb 2023. URL: https://doi.org/10.1042/bsr20221664, doi:10.1042/bsr20221664. This article has 27 citations and is from a peer-reviewed journal.

11. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

12. (costa2024theroleof pages 11-13): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

13. (ibrahim2024processingofltas pages 1-2): Amany M. Ibrahim, Muhammad S. Azam, Olaf Schneewind, and Dominique Missiakas. Processing of ltas restricts lta assembly and ysirk preprotein trafficking into <i>staphylococcus aureus</i> cross-walls. Feb 2024. URL: https://doi.org/10.1128/mbio.02852-23, doi:10.1128/mbio.02852-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

14. (ibrahim2024processingofltas pages 2-5): Amany M. Ibrahim, Muhammad S. Azam, Olaf Schneewind, and Dominique Missiakas. Processing of ltas restricts lta assembly and ysirk preprotein trafficking into <i>staphylococcus aureus</i> cross-walls. Feb 2024. URL: https://doi.org/10.1128/mbio.02852-23, doi:10.1128/mbio.02852-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

15. (pinho2013howtoget media a4f51ba8): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

16. (pinho2013howtoget pages 11-11): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

17. (ibrahim2024processingofltas pages 5-7): Amany M. Ibrahim, Muhammad S. Azam, Olaf Schneewind, and Dominique Missiakas. Processing of ltas restricts lta assembly and ysirk preprotein trafficking into <i>staphylococcus aureus</i> cross-walls. Feb 2024. URL: https://doi.org/10.1128/mbio.02852-23, doi:10.1128/mbio.02852-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

18. (ramosleon2025howdospherical pages 5-6): Félix Ramos-León and Kumaran S. Ramamurthi. How do spherical bacteria regulate cell division? Biochemical Society Transactions, 53:447-460, Apr 2025. URL: https://doi.org/10.1042/bst20240956, doi:10.1042/bst20240956. This article has 4 citations and is from a peer-reviewed journal.