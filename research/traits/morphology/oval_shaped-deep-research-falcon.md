---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:48:48.857097'
end_time: '2026-06-18T09:00:13.633627'
duration_seconds: 684.78
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
  causal_graph_summary: 'oval_shaped_ovococcal_pg_synthesis: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** oval shaped
- **METPO identifier:** METPO:1000678
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by an ellipsoidal morphology with rounded ends, resembling an elongated sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** oval-shaped
- **Existing evidence:** DOI:10.1089/mdr.2014.0032: ovococci that are ellipsoid (Supports oval/ellipsoidal morphology as an ovococcal bacterial shape class.)
- **Existing causal graph summary:** oval_shaped_ovococcal_pg_synthesis: 6 nodes, 5 edges

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
- **METPO identifier:** METPO:1000678
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by an ellipsoidal morphology with rounded ends, resembling an elongated sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** oval-shaped
- **Existing evidence:** DOI:10.1089/mdr.2014.0032: ovococci that are ellipsoid (Supports oval/ellipsoidal morphology as an ovococcal bacterial shape class.)
- **Existing causal graph summary:** oval_shaped_ovococcal_pg_synthesis: 6 nodes, 5 edges

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


# Microbial Trait Causal Graph Curation Report: **oval shaped** (METPO:1000678)

## 0) Executive scope summary
The target trait **oval shaped** (METPO:1000678) corresponds to an **ellipsoidal/ovoid cell morphology with rounded ends** (often called *ovoid*, *ovococcal*, or *ellipsoid* in microbiology), operationalized by microscopy-based morphometrics such as **eccentricity** or **long-axis/short-axis ratio** (>1, but not as high as rods). In many Gram‑positive “ovococci” (e.g., *Streptococcus* spp.) and in *Staphylococcus aureus* (traditionally considered spherical), ovality reflects a **balance between peripheral (sidewall/“elongation”) peptidoglycan synthesis and septal peptidoglycan synthesis**, regulated by divisome/elongasome modules and associated regulators (e.g., GpsB, DivIVA). (jiang2023divivainteractswith pages 9-11, costa2024theroleof pages 1-2)

**Boundary cases / distinctions**:
- **Cocci (spherical)**: near‑unity aspect ratio; growth may be dominated by septal synthesis; *S. aureus* was long treated as a canonical sphere but is now shown to undergo **slight elongation** measurable via axis-ratio changes during the cell cycle. (costa2024theroleof pages 1-2)
- **Rods**: higher aspect ratio; typically rely on MreB-guided circumferential motion of elongation machinery; contrast explicitly drawn with MreB‑lacking cocci/ovococci. (costa2024theroleof pages 1-2)
- **Pleomorphic/filamentous morphologies**: not in scope unless they specifically adopt stable ellipsoidal morphology.

Assay context relevant for curation:
- **Super-resolution microscopy** and standard microscopy with quantitative morphometrics (eccentricity). (costa2024theroleof pages 1-2)
- **Fluorescent D‑amino acid (FDAA) labeling** (e.g., **HADA**) to spatially resolve **septum vs periphery** PG insertion. (costa2024theroleof pages 11-13)

---

## 1) Current understanding: key concepts and definitions
### 1.1 Mechanistic model (divisome vs peripheral PG synthesis)
In ovococci and related systems, a working model is that ovoid/ellipsoidal shape is produced by **temporal and spatial coordination** between:
- **Septal PG synthesis** (divisome; centered on FtsZ and late septal synthases such as **Pbp2x/FtsW/FtsQ** in pneumococcus). (nakamoto2023thedivisomebut pages 3-4)
- **Peripheral/sidewall PG synthesis** (often described as elongasome/peripheral PG complex; includes factors such as **MreC, Pbp2B, RodA** in pneumococcus; also RodA/PBP pairs in *S. aureus*). (nakamoto2023thedivisomebut pages 3-4, costa2024theroleof pages 1-2)

A concise ovococcal cell-cycle framing is provided in *Streptococcus suis* work, referencing ellipsoid division: **“the cell synthesizes peripheral PG alone for a short time to extend the cell before septal PG synthesis is initiated… and then septal and peripheral PG syntheses occur simultaneously… causing cell invagination.”** (jiang2023divivainteractswith pages 9-11)

### 1.2 What “oval shaped” means in graph terms
For TraitMech, this trait is best captured as a **morphological outcome node** that depends on:
- The **rate, location, and timing** of PG insertion and hydrolysis.
- The **subcellular localization** and **interaction network** of PG synthases (PBPs/SEDS) and regulators/scaffolds.

---

## 2) Recent developments and latest research (prioritize 2023–2024)
### 2.1 2024: GpsB as a morphogenesis regulator in *Staphylococcus aureus*
A 2024 mBio study demonstrated that *S. aureus* undergoes measurable **slight elongation** and that this depends on a **SEDS/PBP pair** (**RodA/PBP3**) (pg synthesis in the septal region sidewall), and further identified **GpsB** as a major determinant of shape maintenance. (costa2024theroleof pages 1-2)

Key mechanistic advance: **GpsB controls where PBP activities occur**. In the absence of GpsB, **PBP2 and PBP4 partially delocalize from septum to periphery**, and FDAA labeling shows the **septum:periphery PG synthesis ratio decreases**. (costa2024theroleof pages 11-13)

### 2.2 2023: DivIVA phosphorylation–MltG axis controls peripheral PG synthesis and ovoid geometry in an ovococcus
A 2023 Microbiology Spectrum study in *Streptococcus suis* provides a strongly mechanistic chain linking a regulator (DivIVA), a kinase (STK), a hydrolase (MltG), and peripheral PG synthesis to cell geometry:
- **Deletion of divIVA** causes a **“nearly complete halt in peripheral PG synthesis”** and yields **shorter, flatter** cells. (jiang2023divivainteractswith pages 9-11)
- STK **phosphorylates DivIVA** (S145/T199/T211 in this species), and phosphorylation state strongly shifts morphology (phosphodepleted longer; phosphomimetic shorter). (jiang2023divivainteractswith pages 9-11)
- **Phosphorylated DivIVA interacts with MltG, mislocalizes MltG, and terminates peripheral PG synthesis** (author model with experimental localization support). (jiang2023divivainteractswith pages 9-11)

### 2.3 2023: Pneumococcal divisome/peripheral PG factors and shape outcomes
A 2023 Nature Communications paper dissecting capsule organization also provides shape-relevant genotype–phenotype evidence in *Streptococcus pneumoniae*:
- Null mutants of **mreC, pbp2B, rodA** (enabled in a suppressor background) **“appeared smaller and more spherical.”** (nakamoto2023thedivisomebut pages 3-4)
- In contrast, **ΔgpsB** in pneumococcus **“resulted in large, elongated cells”**, a key caution for taxon-specific directionality of the same regulator. (nakamoto2023thedivisomebut pages 3-4)

### 2.4 2024 (preprint): A cell-wall “sentinel” system linking PG repair/modification to morphology and host defense
A 2024 bioRxiv preprint proposes a streptococcal cell-wall repair/modification system in which a conserved **S (Ess) protein** is septally localized and **directly interacts with PBP1a and PgdA**, and loss of S protein reduces the **fraction of circumferentially moving PBP1a molecules** and yields **altered morphologies** and increased susceptibility to antimicrobials such as LL‑37, lysozyme, and inability to persist transient penicillin treatment. (burnier2024abacterialcell pages 1-4)

---

## 3) Trait scope and boundary cases (curation guidance)
### 3.1 Trait is an observed morphology, not a metabolic capacity
Oval shaped is an **assay-observed morphological class** best annotated from:
- Microscopy images + segmentation; reported as **eccentricity** or axis ratios.
- PG insertion patterns via FDAA probes.

### 3.2 Distinguish “oval shaped” from nearby traits
- **Spherical/round**: reduced eccentricity; can arise from abortive/failed peripheral PG synthesis (e.g., divIVA deletion leading to halted peripheral PG and shorter/wider cells). (jiang2023divivainteractswith pages 9-11)
- **Elongated (rod-like)**: increased aspect ratio; can occur in pneumococcus when gpsB is deleted (large elongated). (nakamoto2023thedivisomebut pages 3-4)
- **Ovococcal (ovoid)**: moderate elongation coordinated with septation.

---

## 4) Candidate causal-graph nodes (grouped by type)

### 4.1 Biological processes / modules
- **Peptidoglycan biosynthetic process** (peripheral vs septal patterns). (jiang2023divivainteractswith pages 9-11, costa2024theroleof pages 11-13)
- **Divisome (septal PG synthesis module)**: FtsZ-centered; late divisome factors include Pbp2x/FtsW/FtsQ (pneumococcus). (nakamoto2023thedivisomebut pages 3-4)
- **Peripheral PG synthesis / “elongasome-like” module in ovococci**: includes MreC, Pbp2B, RodA; also RodA/PBP3 in *S. aureus* midcell sidewall synthesis. (nakamoto2023thedivisomebut pages 3-4, costa2024theroleof pages 1-2)
- **Cell wall repair/modification** coupled to host defense (PBP1a, PgdA; Ess/S protein). (burnier2024abacterialcell pages 1-4)

### 4.2 Genes/proteins/complexes (candidate nodes)
**Core PG synthases and organizers**
- RodA (SEDS)
- FtsW (SEDS)
- PBP3 (class B PBP; *S. aureus*)
- PBP2, PBP4 (*S. aureus*)
- Pbp2B, Pbp2x (*S. pneumoniae*)
- PBP1a (class A PBP; pneumococcus) (burnier2024abacterialcell pages 1-4)

**Regulators/scaffolds / spatial organizers**
- GpsB (Firmicute regulator of PBPs; morphogenesis determinant) (costa2024theroleof pages 11-13, nakamoto2023thedivisomebut pages 3-4)
- DivIVA (elongation/peripheral PG regulator in *S. suis*) (jiang2023divivainteractswith pages 9-11)
- STK serine/threonine kinase (DivIVA phosphorylation) (jiang2023divivainteractswith pages 9-11)
- MapZ, LocZ (division site markers; review-supported) (battaje2023modelsversuspathogens pages 20-21)
- EzrA (divisome regulator; pneumococcus capsule study context) (nakamoto2023thedivisomebut pages 2-3)

**Hydrolases / modifiers**
- MltG (cell wall hydrolase; DivIVA-linked localization; elongation-associated) (jiang2023divivainteractswith pages 9-11)
- PgdA (PG deacetylase; Ess-linked system) (burnier2024abacterialcell pages 1-4)
- SsaA (autolysin amidase; hypothesized role in relaxation) (costa2024theroleof pages 11-13)

### 4.3 Chemicals / environmental and experimental factors
- **HADA** (FDAA probe for PG insertion; used to quantify septum:periphery PG synthesis ratio). (costa2024theroleof pages 11-13)
- **Host antibacterial factors**: LL‑37, lysozyme (effects on survival and resistance in Ess mutant context). (burnier2024abacterialcell pages 1-4)
- **Penicillin treatment** (transient penicillin persistence; Ess mutant unable to persist). (burnier2024abacterialcell pages 1-4)

---

## 5) Candidate evidence-backed causal edges (triples)
The following table is designed to be directly curatable into `oval_shaped.yaml` as candidate nodes/edges, with explicit uncertainty flags.

| Subject node | Predicate | Object node | Evidence snippet (quoted) | Reference (DOI, year, URL) | Notes / uncertainty | Suggested grounding CURIEs |
|---|---|---|---|---|---|---|
| DivIVA | positively regulates | peripheral peptidoglycan synthesis | “Deletion of divIVA caused a nearly complete halt in peripheral PG synthesis, resulting in noticeably shorter and flatter cells.” (jiang2023divivainteractswith pages 9-11) | Jiang et al. 2023, doi:10.1128/spectrum.04750-22, https://doi.org/10.1128/spectrum.04750-22 | Strong, direct in *Streptococcus suis*; morphology consequence supports oval/elongated state. | DivIVA: label-only candidate; peripheral PG synthesis: GO:0009252; NCBITaxon:1307 |
| peripheral peptidoglycan synthesis | positively influences | oval shaped morphology | “the cell synthesizes peripheral PG alone for a short time to extend the cell before septal PG synthesis is initiated” (jiang2023divivainteractswith pages 9-11) | Jiang et al. 2023, doi:10.1128/spectrum.04750-22, https://doi.org/10.1128/spectrum.04750-22 | Mechanistic inference from ovococcal division model; curate as process-to-trait edge with note. | GO:0009252; METPO:1000678 |
| STK serine/threonine kinase | phosphorylates | DivIVA | “in S. suis, STK phosphorylates DivIVA at S145, T199, and T211” (jiang2023divivainteractswith pages 9-11) | Jiang et al. 2023, doi:10.1128/spectrum.04750-22, https://doi.org/10.1128/spectrum.04750-22 | Strong, direct; kinase identity species-specific. | STK: label-only candidate; DivIVA: label-only candidate; GO:0016310 |
| DivIVA phosphorylation | negatively regulates | peripheral peptidoglycan synthesis | “DivIVA phosphorylation affects cell morphology by regulating the synthesis of peripheral PG, and we infer that DivIVA may terminate the peripheral PG synthesis after being phosphorylated by STK.” (jiang2023divivainteractswith pages 9-11) | Jiang et al. 2023, doi:10.1128/spectrum.04750-22, https://doi.org/10.1128/spectrum.04750-22 | Explicitly partly inferred by authors (“we infer”); mark uncertain. | DivIVA phosphorylation: GO:0016310; peripheral PG synthesis: GO:0009252 |
| phosphorylated DivIVA | interacts with / mislocalizes | MltG | “When DivIVA is phosphorylated, it interacts with MltG, causing abnormal localization of MltG and terminating the synthesis of peripheral PG.” (jiang2023divivainteractswith pages 9-11) | Jiang et al. 2023, doi:10.1128/spectrum.04750-22, https://doi.org/10.1128/spectrum.04750-22 | Strong in *S. suis* phosphomimetic context; interaction state-specific. | DivIVA: label-only candidate; MltG: label-only candidate |
| MltG mislocalization | negatively regulates | peripheral peptidoglycan synthesis | “the MltG protein localized at the center of the wild-type cell septum was significantly mislocalized in the ΔdivIVA and DivIVA3E strains… after the DivIVA protein is phosphorylated… [it] mislocaliz[es] MltG, terminating peripheral PG synthesis” (jiang2023divivainteractswith pages 9-11) | Jiang et al. 2023, doi:10.1128/spectrum.04750-22, https://doi.org/10.1128/spectrum.04750-22 | Direct but model-based wording in final clause; species-specific. | MltG: label-only candidate; GO:0009252 |
| MltG loss | negatively influences | oval shaped morphology | “both ΔmltG and DivIVA3E cells were significantly shorter and wider” (jiang2023divivainteractswith pages 9-11) | Jiang et al. 2023, doi:10.1128/spectrum.04750-22, https://doi.org/10.1128/spectrum.04750-22 | Strong phenotype edge; shorter/wider = reduced ovoid aspect ratio. | MltG: label-only candidate; METPO:1000678 |
| GpsB | positively regulates localization of | PBP2 to septum | “both PBP2… partially delocalize from the septum to the peripheral wall in the absence of GpsB.” (costa2024theroleof pages 11-13) | Costa et al. 2024, doi:10.1128/mbio.03235-23, https://doi.org/10.1128/mbio.03235-23 | Strong, direct in *Staphylococcus aureus*. | GpsB: label-only candidate; PBP2: label-only candidate; septum: GO:0045190 |
| GpsB | positively regulates localization of | PBP4 to septum | “both PBP2… and PBP4 partially delocalize from the septum to the peripheral wall in the absence of GpsB.” (costa2024theroleof pages 11-13) | Costa et al. 2024, doi:10.1128/mbio.03235-23, https://doi.org/10.1128/mbio.03235-23 | Strong, direct in *S. aureus*. | GpsB: label-only candidate; PBP4: label-only candidate; septum: GO:0045190 |
| GpsB loss | decreases | septum:periphery peptidoglycan synthesis ratio | “the ratio between peptidoglycan synthesis at the septum versus the cell periphery decreases in the absence of GpsB” (costa2024theroleof pages 11-13) | Costa et al. 2024, doi:10.1128/mbio.03235-23, https://doi.org/10.1128/mbio.03235-23 | Strong, direct HADA-based assay edge. | GpsB: label-only candidate; HADA: ChEBI candidate unavailable; GO:0009252 |
| increased peripheral PBP2/PBP4 activity | negatively influences | oval shaped morphology | “This increased peripheral synthesis may increase the stiffness of the peripheral wall and/or override the RodA/PBP3-mediated synthesis… resulting in rounder cells in the gpsB mutants.” (costa2024theroleof pages 11-13) | Costa et al. 2024, doi:10.1128/mbio.03235-23, https://doi.org/10.1128/mbio.03235-23 | Mechanistic interpretation by authors; mark semi-direct. | PBP2: label-only candidate; PBP4: label-only candidate; METPO:1000678 |
| RodA/PBP3 peptidoglycan synthesis at midcell | positively influences | cell elongation / oval shape | “Together, these proteins catalyze peptidoglycan synthesis, including at the sidewall of the septal region, resulting in slight cell elongation.” (costa2024theroleof pages 1-2) | Costa et al. 2024, doi:10.1128/mbio.03235-23, https://doi.org/10.1128/mbio.03235-23 | Strong in *S. aureus*; trait mapping from elongation to oval/ellipsoidal morphology is appropriate. | RodA: label-only candidate; PBP3: label-only candidate; GO:0009252; METPO:1000678 |
| mreC loss | negatively influences | oval shaped morphology | “cells lacking mreC, pbp2B, and rodA appeared smaller and more spherical” (nakamoto2023thedivisomebut pages 3-4) | Nakamoto et al. 2023, doi:10.1038/s41467-023-38904-9, https://doi.org/10.1038/s41467-023-38904-9 | Strong, direct in *Streptococcus pneumoniae* null background enabled by suppressor context. | MreC: label-only candidate; NCBITaxon:1313; METPO:1000678 |
| pbp2B loss | negatively influences | oval shaped morphology | “cells lacking mreC, pbp2B, and rodA appeared smaller and more spherical” (nakamoto2023thedivisomebut pages 3-4) | Nakamoto et al. 2023, doi:10.1038/s41467-023-38904-9, https://doi.org/10.1038/s41467-023-38904-9 | Strong, direct in pneumococcus. | Pbp2B: label-only candidate; NCBITaxon:1313; METPO:1000678 |
| rodA loss | negatively influences | oval shaped morphology | “cells lacking mreC, pbp2B, and rodA appeared smaller and more spherical” (nakamoto2023thedivisomebut pages 3-4) | Nakamoto et al. 2023, doi:10.1038/s41467-023-38904-9, https://doi.org/10.1038/s41467-023-38904-9 | Strong, direct in pneumococcus. | RodA: label-only candidate; NCBITaxon:1313; METPO:1000678 |
| GpsB loss | positively influences | elongated morphology | “ΔgpsB resulted in large, elongated cells” (nakamoto2023thedivisomebut pages 3-4) | Nakamoto et al. 2023, doi:10.1038/s41467-023-38904-9, https://doi.org/10.1038/s41467-023-38904-9 | Opposite direction from *S. aureus*; strong evidence for taxon-specific effect; do not overgeneralize. | GpsB: label-only candidate; NCBITaxon:1313 |
| Pbp2x | positively regulates recruitment of | CpsC to septum | “CpsC-sfGFP was delocalized after pbp2X, ftsW, and ftsQ depletion… Thus, CpsC recruitment requires late divisome proteins in the divisome.” (nakamoto2023thedivisomebut pages 3-4) | Nakamoto et al. 2023, doi:10.1038/s41467-023-38904-9, https://doi.org/10.1038/s41467-023-38904-9 | Direct for capsule-complex recruitment, indirect for shape; useful network edge but not trait-core. | Pbp2x: label-only candidate; CpsC: label-only candidate; septum: GO:0045190 |
| FtsW | positively regulates recruitment of | CpsC to septum | “CpsC-sfGFP was delocalized after pbp2X, ftsW, and ftsQ depletion… Thus, CpsC recruitment requires late divisome proteins in the divisome.” (nakamoto2023thedivisomebut pages 3-4) | Nakamoto et al. 2023, doi:10.1038/s41467-023-38904-9, https://doi.org/10.1038/s41467-023-38904-9 | Direct for divisome organization; trait relevance indirect. | FtsW: label-only candidate; CpsC: label-only candidate; septum: GO:0045190 |
| FtsQ | positively regulates recruitment of | CpsC to septum | “CpsC-sfGFP was delocalized after pbp2X, ftsW, and ftsQ depletion… Thus, CpsC recruitment requires late divisome proteins in the divisome.” (nakamoto2023thedivisomebut pages 3-4) | Nakamoto et al. 2023, doi:10.1038/s41467-023-38904-9, https://doi.org/10.1038/s41467-023-38904-9 | Direct for divisome organization; trait relevance indirect. | FtsQ: label-only candidate; CpsC: label-only candidate; septum: GO:0045190 |
| S protein (Ess/SPV1429) | directly interacts with | PBP1a | “the pneumococcal S protein directly interacts with a PG synthase, class A penicillin binding protein PBP1a” (burnier2024abacterialcell pages 1-4) | Burnier et al. 2024, doi:10.1101/2024.11.08.622053, https://doi.org/10.1101/2024.11.08.622053 | Preprint; direct interaction evidence but morphology mechanism still emerging. | Ess/S protein: label-only candidate; PBP1a: label-only candidate; NCBITaxon:1313 |
| S protein (Ess/SPV1429) | directly interacts with | PgdA | “the pneumococcal S protein directly interacts with… the PG deacetylase PgdA” (burnier2024abacterialcell pages 1-4) | Burnier et al. 2024, doi:10.1101/2024.11.08.622053, https://doi.org/10.1101/2024.11.08.622053 | Preprint; direct interaction. | Ess/S protein: label-only candidate; PgdA: label-only candidate |
| S protein loss | decreases circumferential movement fraction of | PBP1a | “Single-molecule experiments reveal that the fraction of circumferentially moving PBP1a molecules is reduced in the absence of S protein.” (burnier2024abacterialcell pages 1-4) | Burnier et al. 2024, doi:10.1101/2024.11.08.622053, https://doi.org/10.1101/2024.11.08.622053 | Preprint; direct dynamic phenotype, likely relevant to peripheral/repair PG insertion. | Ess/S protein: label-only candidate; PBP1a: label-only candidate |
| S protein loss | negatively influences | normal ovoid morphology | “streptococci lacking S protein exhibit increased susceptibility to cell wall targeting antibiotics and altered cell morphologies.” (burnier2024abacterialcell pages 1-4) | Burnier et al. 2024, doi:10.1101/2024.11.08.622053, https://doi.org/10.1101/2024.11.08.622053 | Preprint; morphology change not specified as rounder/elongated in snippet, so curate cautiously. | Ess/S protein: label-only candidate; METPO:1000678 |
| MapZ / LocZ | positively regulates | correct septum placement / division site marking | “MapZ and LocZ are reported as proteins that mark division sites and ensure correct septum placement, respectively” (battaje2023modelsversuspathogens pages 20-21) | Battaje et al. 2023, doi:10.1042/bsr20221664, https://doi.org/10.1042/bsr20221664 | Review-based, less direct; useful background node but weaker than primary experimental studies. | MapZ: label-only candidate; LocZ: label-only candidate; GO:0000921 |
| FtsZ ring depletion | negatively regulates | CpsC septal localization | “Depletion of FtsZ dispersed CpsC-sfGFP, indicating the FtsZ ring is required for CpsC localization” (nakamoto2023thedivisomebut pages 2-3) | Nakamoto et al. 2023, doi:10.1038/s41467-023-38904-9, https://doi.org/10.1038/s41467-023-38904-9 | Direct but capsule/divisome edge rather than direct shape edge; still mechanistically central. | FtsZ: label-only candidate; CpsC: label-only candidate; GO:0045190 |


*Table: This table lists candidate mechanistic causal edges for the microbial trait 'oval shaped' using only the specified evidence set. It highlights direct experimental edges, taxon-specific contradictions such as GpsB effects in different species, and weaker review-based background edges for cautious curation.*

**Visual evidence note**: Costa et al. 2024 provide figure-based quantification linking **ΔgpsB → decreased eccentricity (more spherical)** and **PBP2/PBP4 delocalization + decreased septum:periphery HADA ratio** (Figures 1 and 3). (costa2024theroleof media af068b94, costa2024theroleof media bac4c253)

---

## 6) Quantitative/statistical highlights from recent studies
- *S. aureus* morphogenesis study analyzed **eccentricity** across **11 non-essential gene deletions**; the “remaining three mutants” (including gpsB) had eccentricity reduced by **“close to 10%.”** (costa2024theroleof pages 11-13)
- In pneumococcus capsule/divisome study, demograph analysis for recruitment hierarchy used **three biologically independent experiments (n = 500)**. (nakamoto2023thedivisomebut pages 3-4)
- In *S. aureus*, elongation is described as an **increase in long-axis/short-axis ratio** during the cell cycle, enabled by super-resolution microscopy on ~1 µm cells. (costa2024theroleof pages 1-2)
- In the Ess/S protein preprint: **single-molecule experiments** report that the **fraction of circumferentially moving PBP1a molecules is reduced** in the absence of S protein (directional/kinetic statistic stated, but numerical value not provided in retrieved pages). (burnier2024abacterialcell pages 1-4)

---

## 7) Current applications and real-world implementations
### 7.1 Infection biology and pathogenesis (shape as a functional trait)
In *S. aureus*, mild elongation/deformation can be functionally important in certain infection settings. The 2024 mBio study notes that in osteomyelitis, *S. aureus* cells have been observed as **“submicron rod-shaped bacteria within the canaliculi of live cortical bone,”** consistent with a requirement for deformation/elongation to migrate in bone microchannels. (costa2024theroleof pages 11-13)

### 7.2 Antibiotic target rationale and host defense relevance
Because ovality depends on PG synthesis localization and dynamics, genes controlling peripheral vs septal PG synthesis (SEDS/bPBP pairs; PBPs; regulators like GpsB/DivIVA; hydrolases like MltG) are directly relevant as **antibacterial target axes**. The Ess/S protein preprint frames a coordinated PG repair/modification system required to resist LL‑37 and lysozyme and to persist penicillin exposure, linking envelope robustness to survival. (burnier2024abacterialcell pages 1-4)

### 7.3 Experimental/diagnostic implementations
- **FDAA labeling (HADA)** is an established approach for mapping PG insertion patterns and deriving mechanistic shape explanations via septum/periphery ratios. (costa2024theroleof pages 11-13)
- **Two-hybrid and localization assays** provide evidence for regulator–PBP wiring (GpsB–PBP2 interaction shown via bacterial two-hybrid). (costa2024theroleof pages 11-13)

---

## 8) Expert opinions / authoritative interpretations (as stated in sources)
- Authors of the *S. aureus* mBio 2024 study interpret the gpsB phenotype through spatial regulation of PBPs: increased peripheral PBP activity may **“override the RodA/PBP3-mediated synthesis”** or **stiffen the peripheral wall**, “resulting in rounder cells.” (costa2024theroleof pages 11-13)
- Authors of the *S. suis* 2023 study explicitly highlight that “precise regulation of PG synthesis to produce the ovoid shape is… unanswered,” and propose a regulatory mechanism where DivIVA phosphorylation affects MltG localization to time peripheral PG synthesis termination. (jiang2023divivainteractswith pages 9-11)
- Pneumococcal Nat Commun 2023 data emphasize that the same regulator (GpsB) can have opposite morphological effects across taxa/contexts, implying that **network context** (and suppressor backgrounds) matter for curation decisions. (nakamoto2023thedivisomebut pages 3-4)

---

## 9) Warnings / curation cautions (do not yet curate without qualifiers)
1. **Taxon-specific directionality**: gpsB deletion causes **more spherical cells in *S. aureus*** (costa2024theroleof pages 1-2, costa2024theroleof media af068b94) but **large elongated cells in *S. pneumoniae*** (nakamoto2023thedivisomebut pages 3-4). This should be encoded with taxon constraints or marked uncertain for general (species-agnostic) edges.
2. **Inferred edges**: Several mechanistic steps are framed as inference (e.g., “we infer” DivIVA phosphorylation terminates peripheral PG synthesis). These edges should be flagged **UNCERTAIN** unless corroborated by additional primary sources. (jiang2023divivainteractswith pages 9-11)
3. **Preprint evidence**: Burnier et al. 2024 is a **bioRxiv preprint**; edges involving Ess/S protein, PBP1a dynamics, and morphology should be flagged as **PREPRINT/PROVISIONAL** until peer review. (burnier2024abacterialcell pages 1-4)
4. **Review-only claims**: MapZ/LocZ summary is from a review excerpt; do not treat as definitive causal evidence without primary-source confirmation. (battaje2023modelsversuspathogens pages 20-21)

---

## 10) DOI-first bibliography (with dates/URLs)
1. Costa SF, et al. **“The role of GpsB in Staphylococcus aureus cell morphogenesis.”** *mBio* (published 6 Feb 2024; issue March 2024). DOI: **10.1128/mbio.03235-23**. URL: https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2)
2. Jiang Q, et al. **“DivIVA Interacts with the Cell Wall Hydrolase MltG To Regulate Peptidoglycan Synthesis in Streptococcus suis.”** *Microbiology Spectrum* (Jun 2023). DOI: **10.1128/spectrum.04750-22**. URL: https://doi.org/10.1128/spectrum.04750-22 (jiang2023divivainteractswith pages 9-11)
3. Nakamoto R, et al. **“The divisome but not the elongasome organizes capsule synthesis in Streptococcus pneumoniae.”** *Nature Communications* (Jun 2023). DOI: **10.1038/s41467-023-38904-9**. URL: https://doi.org/10.1038/s41467-023-38904-9 (nakamoto2023thedivisomebut pages 3-4)
4. Burnier J, et al. **“A bacterial cell wall repair and modification system to resist host antibacterial factors.”** *bioRxiv* (posted 9 Nov 2024). DOI: **10.1101/2024.11.08.622053**. URL: https://doi.org/10.1101/2024.11.08.622053 (burnier2024abacterialcell pages 1-4)
5. Battaje RR, et al. **“Models versus pathogens: how conserved is the FtsZ in bacteria?”** *Bioscience Reports* (Feb 2023). DOI: **10.1042/bsr20221664**. URL: https://doi.org/10.1042/bsr20221664 (battaje2023modelsversuspathogens pages 20-21)

---

## 11) Notes for `data/traits/morphology/oval_shaped.yaml`
For TraitMech curation, a robust minimal causal subgraph supported by primary evidence in this retrieval set can center on:
- **(DivIVA → peripheral PG synthesis → ovoid/oval morphology)** with modulation by **STK phosphorylation** and **MltG localization** (*S. suis*). (jiang2023divivainteractswith pages 9-11)
- **(GpsB → PBP2/PBP4 septal localization → higher septum:periphery PG synthesis ratio → maintenance of mild elongation/ovoidness)** (*S. aureus*). (costa2024theroleof pages 11-13, costa2024theroleof media af068b94)
- **(MreC/Pbp2B/RodA peripheral PG system → less spherical/more ovoid)** (*S. pneumoniae*). (nakamoto2023thedivisomebut pages 3-4)

These should be curated with explicit **NCBITaxon constraints** where directionality differs (notably gpsB). (nakamoto2023thedivisomebut pages 3-4, costa2024theroleof pages 1-2)

References

1. (jiang2023divivainteractswith pages 9-11): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 12 citations and is from a domain leading peer-reviewed journal.

2. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

3. (costa2024theroleof pages 11-13): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

4. (nakamoto2023thedivisomebut pages 3-4): Rei Nakamoto, Sarp Bamyaci, Karin Blomqvist, Staffan Normark, Birgitta Henriques-Normark, and Lok-To Sham. The divisome but not the elongasome organizes capsule synthesis in streptococcus pneumoniae. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38904-9, doi:10.1038/s41467-023-38904-9. This article has 13 citations and is from a highest quality peer-reviewed journal.

5. (burnier2024abacterialcell pages 1-4): Jessica Burnier, Clement Gallay, Kevin Bruce, Elisabet Bjånes, Louise Martin, Kinki Jim, Ho-Ching Tiffany Tsui, Amelieke Cremers, Johann Mignolet, Daniela Vollmer, Jacob Biboy, Victor Nizet, Waldemar Vollmer, Malcolm E. Winkler, and Jan-Willem Veening. A bacterial cell wall repair and modification system to resist host antibacterial factors. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.08.622053, doi:10.1101/2024.11.08.622053. This article has 1 citations.

6. (battaje2023modelsversuspathogens pages 20-21): Rachana Rao Battaje, Ravikant Piyush, Vidyadhar Pratap, and Dulal Panda. Models versus pathogens: how conserved is the ftsz in bacteria? Bioscience Reports, Feb 2023. URL: https://doi.org/10.1042/bsr20221664, doi:10.1042/bsr20221664. This article has 27 citations and is from a peer-reviewed journal.

7. (nakamoto2023thedivisomebut pages 2-3): Rei Nakamoto, Sarp Bamyaci, Karin Blomqvist, Staffan Normark, Birgitta Henriques-Normark, and Lok-To Sham. The divisome but not the elongasome organizes capsule synthesis in streptococcus pneumoniae. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38904-9, doi:10.1038/s41467-023-38904-9. This article has 13 citations and is from a highest quality peer-reviewed journal.

8. (costa2024theroleof media af068b94): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

9. (costa2024theroleof media bac4c253): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.