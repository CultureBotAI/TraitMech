---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:51:23.141941'
end_time: '2026-06-18T09:06:15.013783'
duration_seconds: 891.87
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: ovoid shaped
  trait_identifier: METPO:1000677
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: ovoid_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has an oval morphology, rounded at
    both ends with one end often slightly broader than the other.
  parent_traits: METPO:1000666
  synonyms: S_ovoid, ovoid-shaped
  evidence_summary: 'DOI:10.1016/j.cub.2021.04.041: ovoid bacterium Streptococcus
    pneumoniae (Supports ovoid bacterial morphology as a recognized ovococcal shape.)'
  causal_graph_summary: 'ovoid_shaped_midcell_pg_assembly: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ovoid shaped
- **METPO identifier:** METPO:1000677
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an oval morphology, rounded at both ends with one end often slightly broader than the other.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_ovoid, ovoid-shaped
- **Existing evidence:** DOI:10.1016/j.cub.2021.04.041: ovoid bacterium Streptococcus pneumoniae (Supports ovoid bacterial morphology as a recognized ovococcal shape.)
- **Existing causal graph summary:** ovoid_shaped_midcell_pg_assembly: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **ovoid shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/ovoid_shaped.yaml`.

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
- **Trait label:** ovoid shaped
- **METPO identifier:** METPO:1000677
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an oval morphology, rounded at both ends with one end often slightly broader than the other.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_ovoid, ovoid-shaped
- **Existing evidence:** DOI:10.1016/j.cub.2021.04.041: ovoid bacterium Streptococcus pneumoniae (Supports ovoid bacterial morphology as a recognized ovococcal shape.)
- **Existing causal graph summary:** ovoid_shaped_midcell_pg_assembly: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **ovoid shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/ovoid_shaped.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **ovoid shaped** (METPO:1000677)

## 0. Executive scope summary
The trait **ovoid shaped** (METPO:1000677) denotes a **non-spherical, slightly elongated coccoid** morphology (often described as “ovococcal/ovococcoid”), typically observed in streptococci and related low-GC Gram-positive bacteria. In current mechanistic understanding, ovococcal “ovoidness” is tightly linked to **dual spatial programs of peptidoglycan (PG) insertion**—**septal (division) PG synthesis** plus a distinct **peripheral/midcell (elongation-like) PG synthesis** program—rather than the **sidewall elongation** program of rods (which is often MreB-scaffolded). This distinguishes ovococci from (i) **true cocci** where PG insertion is described as largely septal and (ii) **rods** that elongate by MreB-directed sidewall synthesis. (costa2024theroleof pages 1-2, costa2023newapproachesto pages 205-209, kumar2024insightsintothe pages 4-6, battaje2023modelsversuspathogens pages 4-5)

**Operational curation boundary** for METPO:1000677: include microbes whose **cell body is oval/egg-like** in microscopy/assays or whose morphogenesis is explicitly described as **ovococcal/ovoid**; exclude (a) perfectly spherical cocci unless a measurable long-axis/short-axis elongation is present, and (b) rods/filaments where length≫width and elongation is sidewall-dominated. Boundary cases and pleiomorphy exist (e.g., taxa described as bacilli but “resembling spheres” in broth), so curation should require assay context (growth phase/media) when possible. (abdulhadi2024grampositivebacteria pages 7-8)

## 1. Key concepts and definitions (current understanding)
### 1.1 Phenotype definition (trait scope)
* **Observed morphology:** Streptococcus spp. are “typically spherical or ovoid in shape” and occur in pairs/chains in many contexts, indicating that “ovoid” is a common and accepted morphology descriptor in authoritative microbiology reviews. (kumar2024insightsintothe pages 4-6)
* **Mechanistic definition (ovococci vs cocci):** Ovococci are distinguished from strictly spherical cocci by **additional midcell/peripheral PG synthesis that produces measurable elongation** along one axis (long axis/short axis ratio increases), whereas classic cocci were historically characterized as synthesizing PG primarily at the septum. (costa2024theroleof pages 1-2, costa2023newapproachesto pages 205-209)
* **Core mechanistic hallmark:** in *Streptococcus pneumoniae*, septal and peripheral PG synthesis machineries assemble at midcell as **concentric rings** (inner septal ring and outer peripheral ring), enabling the ovoid morphology. (battaje2023modelsversuspathogens pages 4-5)

### 1.2 Boundary cases and nearby traits
* **Near neighbors:** spherical/coccoid, ellipsoid, short rods. Since “ovoid” can be used loosely in narrative descriptions, a curation-safe boundary is to require either (i) explicit “ovoid/ovococcal/ovococcoid” labeling, or (ii) quantitative shape metrics (e.g., aspect ratio/eccentricity) showing a consistent long-axis bias.
* **Taxon caution:** Some oral microbiology texts call certain streptococci “cocci” without clarifying ovoidness, while other authoritative sources explicitly include “ovoid” for streptococci. Treat these as **context-dependent** and avoid over-generalizing across species/conditions. (abdulhadi2024grampositivebacteria pages 8-10, kumar2024insightsintothe pages 4-6)

## 2. Recent developments and latest research (prioritizing 2023–2024)
### 2.1 2024 authoritative review context for “ovoid” streptococci
A 2024 *Microbiology and Molecular Biology Reviews* article (Jun 2024) frames streptococci as Gram-positive chain-formers that are “typically spherical or ovoid,” supporting the ontology-level assertion that ovoid morphology is a recognized and commonly used descriptor for this genus. (kumar2024insightsintothe pages 4-6)

### 2.2 2023–2024 mechanistic advances relevant to ovococcal/ovoid morphogenesis
**Dual-mode PG synthesis and concentric ring organization (ovococci):** A 2023 review synthesizes evidence that *S. pneumoniae* uses two distinct spatial modes of PG synthesis (septal and peripheral) and that these machineries assemble at midcell into concentric rings. (battaje2023modelsversuspathogens pages 4-5)

**Phosphoregulation of peripheral PG synthesis via DivIVA–MltG (ovococci):** In *Streptococcus suis* (Jun 2023), DivIVA was experimentally linked to peripheral PG synthesis and ovoid morphology: deletion of divIVA caused abortive peripheral PG synthesis and decreased aspect ratio; additionally, DivIVA phosphorylation state modulated interaction with the cell wall hydrolase MltG and affected MltG localization, with phosphomimetic mutants yielding shorter/rounder cells. (jiang2023divivainteractswith pages 9-11)

**Adaptor-mediated switching between septal vs peripheral synthesis via GpsB and phosphorylation systems:** In *S. pneumoniae* (Jul 2023), GpsB is described as an adaptor that links PG synthases to scaffold proteins and is required for normal StkP-mediated phosphorylation; PG precursor enzymes MurZ/MurA genetically suppress ΔgpsB/ΔstkP phenotypes, suggesting a key regulatory output of phosphorylation is control of early PG precursor synthesis capacity. (tsui2023negativeregulationof pages 3-4, tsui2023negativeregulationof pages 1-3)

**2024 experimental evidence of GpsB-controlled PBP localization and PG synthesis redistribution (real-world implementation of measurement):** In *Staphylococcus aureus* (mBio, Mar 2024), deletion of gpsB partially delocalized PBP2 and PBP4 from septum to periphery and decreased the HADA septum-to-periphery ratio, demonstrating an experimentally tractable “switch” mechanism that redistributes where PG is inserted—directly relevant as an analogous mechanism for ovococcoid systems. (costa2024theroleof pages 11-13, costa2024theroleof media b704100a, costa2024theroleof media d2422b21)

## 3. Current applications and real-world implementations
1. **Antibiotic target discovery and MoA interpretation:** The ovoid/ovococcal shape program is built on essential cell-wall enzymes and division proteins (e.g., FtsZ, FtsW–PBP2x, RodA–PBP2b, PBPs, regulators like GpsB/StkP). These components are routinely discussed as antibacterial targets or as determinants of antibiotic sensitivity because they govern septal/peripheral PG synthesis and thus cell integrity and morphogenesis. (battaje2023modelsversuspathogens pages 4-5, tsui2023negativeregulationof pages 1-3)
2. **Microscopy-based phenotyping pipelines for morphogenesis:** Real implementations include (i) fluorescent D-amino acid labeling (e.g., HADA) to map new PG insertion, (ii) septum-to-periphery fluorescence ratio metrics for PBP localization and PG synthesis, and (iii) aspect ratio/eccentricity as quantitative morphology outputs to tie genetic perturbations to “ovoidness.” (jiang2023divivainteractswith pages 9-11, costa2023theroleof pages 12-14, costa2024theroleof media b704100a)
3. **Systems genetics for cell-shape networks:** Genome-scale interaction mapping approaches (e.g., CRISPRi–TnSeq in *S. pneumoniae*) are now being used to reveal hidden redundancies and coupling between essential cell-wall synthesis/division genes, offering a practical route to discover new ovoid-shape determinants for graph expansion (though the evidence retrieved here is general rather than ovoid-specific). (tsui2023chromosomalduplicationsof pages 55-57)

## 4. Candidate causal graph nodes (curation inventory)
Below are candidate node lists for `data/traits/morphology/ovoid_shaped.yaml`, grounded where feasible.

### 4.1 Phenotype / trait nodes
* **METPO:1000677** ovoid shaped (trait)
* Related morphology nodes (label-only unless METPO IDs known): spherical/coccoid; ovococcal/ovococcoid; rod-shaped/bacillary

### 4.2 Biological processes / pathways (GO-suggested grounding)
* **Peptidoglycan biosynthetic process** (GO label; candidate grounding: GO:0009252)
* **Cell division** (GO:0051301)
* **Septal peptidoglycan synthesis** (label-only; can map as part of PG biosynthesis localized to divisome)
* **Peripheral/midcell peptidoglycan synthesis (elongation-like)** (label-only)
* **Z-ring assembly / FtsZ ring formation** (label-only; can map under cell division)
* **Protein phosphorylation (Ser/Thr)** (GO:0006468)

### 4.3 Protein/complex nodes (label-only unless curated to UniProt later)
**Divisome / division-site selection and regulation**
* FtsZ (tubulin-like GTPase)
* FtsA (FtsZ membrane anchor/partner)
* EzrA (FtsZ-associated regulator)
* ZapA, ZapJ (FtsZ regulators)
* **FtsW–PBP2x complex** (septal PG synthase pair) (battaje2023modelsversuspathogens pages 4-5)
* MapZ (LocZ) (division-site marker positioning FtsZ) (battaje2023modelsversuspathogens pages 4-5)
* CcrZ (regulator coupling replication to Z-ring initiation) (battaje2023modelsversuspathogens pages 4-5)

**Elongasome / peripheral PG synthesis**
* **RodA–PBP2b pair** (peripheral PG synthesis driver) (battaje2023modelsversuspathogens pages 4-5)
* CozE
* MreC, MreD
* RodZ (battaje2023modelsversuspathogens pages 4-5)

**Regulators linking synthesis modes**
* GpsB (adaptor; regulator of phosphorylation networks) (tsui2023negativeregulationof pages 1-3)
* StkP / STK (serine/threonine kinase; “STK” in *S. suis*) (jiang2023divivainteractswith pages 9-11, tsui2023negativeregulationof pages 3-4)
* PhpP (phosphatase; suppressor context) (tsui2023negativeregulationof pages 3-4)
* DivIVA (phosphoregulated morphogen) (jiang2023divivainteractswith pages 9-11)

**PG remodeling enzyme**
* MltG (cell wall hydrolase; elongation-linked; localization regulated by DivIVA phosphorylation) (jiang2023divivainteractswith pages 9-11)

**PG precursor synthesis / suppressor genetics**
* MurZ, MurA (PG precursor pathway enzymes; dosage suppresses ΔgpsB/ΔstkP phenotypes) (tsui2023negativeregulationof pages 1-3)

### 4.4 Chemicals / experimental probes (ChEBI-suggested)
* **HADA** (fluorescent D-amino acid PG labeling probe; label-only here) (costa2024theroleof media b704100a)
* PG precursors/metabolites (label-only; e.g., lipid II—ChEBI grounding possible during curation)

### 4.5 Environmental/experimental factors
* Gene deletions: ΔdivIVA, ΔgpsB
* Phospho-mutants: DivIVA3A (phospho-dead), DivIVA3E (phosphomimetic)
* Imaging modalities: fluorescent D-amino acid labeling; septum/periphery fluorescence ratio; aspect ratio measurements (jiang2023divivainteractswith pages 9-11, costa2024theroleof media b704100a)

## 5. Evidence-backed candidate causal edges (curation table)
The following table is designed for direct translation into TraitMech causal-graph edges (with confidence notes and taxon constraints).

| Edge (subject—predicate—object) | Entity types (S/P/O) | Taxon/context | Evidence snippet | Reference (DOI + year + URL) | Confidence/notes |
|---|---|---|---|---|---|
| Ovoid/ovococcal growth — has_component_process — septal peptidoglycan synthesis | morphology process / has_component_process / biological process | *Streptococcus pneumoniae* ovococci | “there are two spatially distinct modes of peptidoglycan (PG) synthesis during the cell cycle: septal and peripheral” (battaje2023modelsversuspathogens pages 4-5) | 10.1042/BSR20221664 (2023) https://doi.org/10.1042/BSR20221664 | High; direct review synthesis for pneumococcus |
| Ovoid/ovococcal growth — has_component_process — peripheral peptidoglycan synthesis | morphology process / has_component_process / biological process | *S. pneumoniae* ovococci | “there are two spatially distinct modes of peptidoglycan (PG) synthesis during the cell cycle: septal and peripheral” (battaje2023modelsversuspathogens pages 4-5) | 10.1042/BSR20221664 (2023) https://doi.org/10.1042/BSR20221664 | High; direct review synthesis for pneumococcus |
| FtsZ treadmilling — drives — septal PG synthesis | protein process / drives / biological process | *S. pneumoniae* | “FtsZ treadmilling drives septal PG synthesis together with the FtsW–PBP2x complex” (battaje2023modelsversuspathogens pages 4-5) | 10.1042/BSR20221664 (2023) https://doi.org/10.1042/BSR20221664 | High; core mechanistic edge |
| FtsW–PBP2x complex — synthesizes — septal peptidoglycan | protein complex / synthesizes / biological process | *S. pneumoniae* divisome | “septal PG synthesis is driven by… the FtsW-PBP2x complex to synthesize the division septum” (battaje2023modelsversuspathogens pages 4-5) | 10.1042/BSR20221664 (2023) https://doi.org/10.1042/BSR20221664 | High; direct statement |
| RodA–PBP2b elongasome — drives — peripheral peptidoglycan synthesis | protein complex / drives / biological process | *S. pneumoniae* elongasome | “this peripheral (elongation) activity is carried out by the elongasome complex, driven by the RodA-PBP2b pair” (battaje2023modelsversuspathogens pages 4-5) | 10.1042/BSR20221664 (2023) https://doi.org/10.1042/BSR20221664 | High; direct statement |
| MreC — required_for — peripheral peptidoglycan synthesis | protein / required_for / biological process | ovococci, esp. *S. pneumoniae* | “MreC and MreD described as necessary and responsible for directing peripheral PGN synthesis” (costa2023newapproachesto pages 205-209) | source text summarized from 2023 review context; no standalone DOI in excerpt beyond dissertation/review context | Medium; review-level, wording from secondary source |
| MreD — required_for — peripheral peptidoglycan synthesis | protein / required_for / biological process | ovococci, esp. *S. pneumoniae* | “MreC and MreD described as necessary and responsible for directing peripheral PGN synthesis” (costa2023newapproachesto pages 205-209) | source text summarized from 2023 review context; no standalone DOI in excerpt beyond dissertation/review context | Medium; review-level, wording from secondary source |
| CozE/MreCD complex — directs — cell elongation | protein complex / directs / biological process | *S. pneumoniae* | “CozE is described as part of the MreCD complex that directs cell elongation” (galinier2023recentadvancesin pages 14-15) | 10.3390/biom13050720 (2023) https://doi.org/10.3390/biom13050720 | Medium; cited within review, useful candidate node |
| MapZ — positions — FtsZ ring | protein / positions / protein structure/process | *S. pneumoniae* division-site selection | “MapZ is described as a mid-cell–anchored protein… that guides movement of FtsZ and associated proteins from the septal ring to the equatorial ring” (battaje2023modelsversuspathogens pages 4-5) | 10.1042/BSR20221664 (2023) https://doi.org/10.1042/BSR20221664 | High; spatial landmark role well supported |
| CcrZ — regulates — FtsZ/Z-ring initiation | protein / regulates / protein structure/process | *S. pneumoniae* | “CcrZ is reported to regulate DNA replication and to regulate FtsZ and the Z-ring at division initiation” (battaje2023modelsversuspathogens pages 4-5) | 10.1042/BSR20221664 (2023) https://doi.org/10.1042/BSR20221664 | Medium-high; regulatory role summarized in review |
| STK (StkP-like kinase) — phosphorylates — DivIVA | protein kinase / phosphorylates / protein | *Streptococcus suis* ovococci | “The eukaryotic-type serine/threonine kinase STK phosphorylates DivIVA at S145, T199, and T211” (jiang2023divivainteractswith pages 9-11) | 10.1128/SPECTRUM.04750-22 (2023) https://doi.org/10.1128/spectrum.04750-22 | High; direct experimental evidence but taxon-specific |
| DivIVA phosphorylation state — modulates — DivIVA–MltG interaction | protein state / modulates / protein-protein interaction | *S. suis* | “DivIVA phosphorylation alters the DivIVA–MltG interaction” (jiang2023divivainteractswith pages 9-11) | 10.1128/SPECTRUM.04750-22 (2023) https://doi.org/10.1128/spectrum.04750-22 | High; direct experimental evidence |
| DivIVA phosphorylation state — alters_localization_of — MltG | protein state / alters_localization_of / protein localization | *S. suis* | “mislocalizes MltG (mislocalization in ΔdivIVA and DivIVA3E; normal localization in DivIVA3A)” (jiang2023divivainteractswith pages 9-11) | 10.1128/SPECTRUM.04750-22 (2023) https://doi.org/10.1128/spectrum.04750-22 | High; direct experimental evidence |
| MltG localization — enables — peripheral peptidoglycan synthesis | protein localization / enables / biological process | *S. suis* | “both ΔmltG and DivIVA3E cells formed significantly rounder cells,” with “DivIVA deletion caused abortive peripheral PG synthesis” (jiang2023divivainteractswith pages 9-11) | 10.1128/SPECTRUM.04750-22 (2023) https://doi.org/10.1128/spectrum.04750-22 | Medium-high; causal chain inferred from linked experiments |
| Peripheral peptidoglycan synthesis — maintains — ovoid aspect ratio | biological process / maintains / morphology | *S. suis* ovococci | “DivIVA deletion caused abortive peripheral PG synthesis, resulting in a decreased aspect ratio” (jiang2023divivainteractswith pages 9-11) | 10.1128/SPECTRUM.04750-22 (2023) https://doi.org/10.1128/spectrum.04750-22 | High; direct morphology readout |
| GpsB — acts_as_adaptor_for — PG synthases/localization complexes | protein / acts_as_adaptor_for / protein complexes | *S. pneumoniae* | “GpsB functions as a major regulator of peptidoglycan (PG) synthesis by linking PG synthases to other proteins and acting as an adaptor” (tsui2023negativeregulationof pages 1-3) | 10.1111/MMI.15122 (2023) https://doi.org/10.1111/mmi.15122 | High; direct statement in primary paper |
| GpsB — required_for — StkP substrate phosphorylation | protein / required_for / protein phosphorylation process | *S. pneumoniae* | “phosphorylation of StkP and other StkP substrates is significantly reduced in ΔgpsB mutants” (tsui2023negativeregulationof pages 3-4) | 10.1111/MMI.15122 (2023) https://doi.org/10.1111/mmi.15122 | High; direct primary evidence |
| ΔgpsB — causes_delocalization_of — PBP2/PBP4 from septum to periphery | genotype / causes_delocalization_of / protein localization | *Staphylococcus aureus* analogous ovococcal-like support | “deletion of gpsB causes the partial delocalization of PBP2 and PBP4 from the division septum to the cell periphery” (costa2024theroleof media b704100a, costa2023theroleof pages 21-24) | 10.1128/mBio.03235-23 (2024) https://doi.org/10.1128/mbio.03235-23 | Medium; analogous support from *S. aureus*, not direct ovococcal pneumococcus |
| ΔgpsB — increases — peripheral peptidoglycan synthesis | genotype / increases / biological process | *S. aureus* analogous support | “lower HADA septum-to-periphery fluorescence ratio (HADA FR) in gpsB mutants” and “increased PG synthesis at the periphery” (costa2024theroleof media b704100a, costa2024theroleof pages 11-13) | 10.1128/mBio.03235-23 (2024) https://doi.org/10.1128/mbio.03235-23 | Medium; strong experiment, analogous taxon |
| Increased peripheral-vs-septal PG synthesis in ΔgpsB — results_in — more spherical cells | biological process imbalance / results_in / morphology | *S. aureus* analogous support | “loss of GpsB shifts PG synthesis toward the peripheral wall… producing more spherical cells” (costa2024theroleof pages 11-13) | 10.1128/mBio.03235-23 (2024) https://doi.org/10.1128/mbio.03235-23 | Medium; analogous evidence for morphology outcome |
| Increased MurZ/MurA dosage — suppresses — ΔgpsB/ΔstkP phenotypes | gene dosage / suppresses / mutant phenotype | *S. pneumoniae* | “overproduction of MurZ or MurA… can suppress defects caused by loss of gpsB or stkP” (tsui2023negativeregulationof pages 1-3) | 10.1111/MMI.15122 (2023) https://doi.org/10.1111/mmi.15122 | High; direct genetic suppression evidence |
| GpsB/Pbp2x — required_for — septal ring closure | protein complex/function / required_for / biological process | *S. pneumoniae* | “the excerpt specifically notes the essentiality of Pbp2x and GpsB for septal ring closure” (tsui2023chromosomalduplicationsof pages 57-59) | 10.1101/2023.03.26.534294 (2023) https://doi.org/10.1101/2023.03.26.534294 | Medium; preprint/summary-level evidence |
| Septal and peripheral PG synthesis machineries — assemble_as — concentric midcell rings | protein machineries / assemble_as / cellular localization pattern | *S. pneumoniae* | “septal and peripheral PG-synthesis machineries assemble at mid-cell into concentric rings (inner septal, outer peripheral)” (battaje2023modelsversuspathogens pages 4-5) | 10.1042/BSR20221664 (2023) https://doi.org/10.1042/BSR20221664 | High; useful organizational edge for graph topology |


*Table: This table lists candidate causal edges for curation of the microbial trait 'ovoid shaped' (METPO:1000677), emphasizing mechanistic determinants of ovococcal morphology in Streptococcus pneumoniae and Streptococcus suis, with Staphylococcus aureus included as analogous support. It highlights peptidoglycan synthesis modes, divisome/elongasome components, regulatory phosphorylation, and morphology-linked perturbation phenotypes.*

### Figure-based evidence supporting a key edge (GpsB→PBP localization→PG redistribution)
A key implementation detail for curation is that **GpsB deletion changes PBP localization and shifts PG insertion from septum toward periphery**, which provides an experimentally measurable bridge between molecular mechanism and cell-shape outcome. This is shown in a cropped Figure 3 from a 2024 mBio paper. (costa2024theroleof media b704100a, costa2024theroleof media d2422b21)

## 6. Relevant quantitative statistics / data points (from retrieved evidence)
* **FtsZ dynamics (quantitative):** In *S. aureus*, FtsZ treadmilling speeds were essentially unchanged by gpsB deletion (parental 58.7±7.7 nm/s; ΔgpsB 59.6±7.6 nm/s), supporting the interpretation that gpsB-driven morphology changes can act through **PBP localization/PG insertion** rather than via altering FtsZ treadmilling speed. (costa2023theroleof pages 12-14)
* **Aspect ratio as a morphology readout:** In *S. suis*, divIVA deletion caused “abortive peripheral PG synthesis, resulting in a decreased aspect ratio,” and DivIVA phosphomimetic vs phospho-dead mutants were described as significantly shorter vs longer, linking peripheral PG synthesis to ovoidness. (jiang2023divivainteractswith pages 9-11)
* **Septum-to-periphery synthesis ratios (quantitative framework):** In *S. aureus*, gpsB deletion decreased the septum:periphery fluorescence ratios for PBP localization and HADA incorporation (qualitatively described as lower FR), i.e., increased peripheral PG synthesis relative to septal. (costa2024theroleof media b704100a, costa2024theroleof pages 11-13)

## 7. Expert opinions / authoritative synthesis
* An authoritative synthesis of ovococcal morphogenesis emphasizes that *S. pneumoniae* lacks canonical Min/Noc/MreB systems and instead organizes septal and peripheral synthesis at midcell with dedicated protein sets, including MapZ-mediated division-site control and paired SEDS/bPBP synthase complexes for septal vs peripheral synthesis. (battaje2023modelsversuspathogens pages 4-5)
* A mechanistic regulatory view emerging from 2023 primary work is that **phosphorylation networks (StkP/PhpP and related kinases) and adaptors (GpsB)** exert essential control by modulating PG precursor enzymes (MurZ/MurA) and/or coordinating the activity/localization of PG synthases, thereby determining whether growth proceeds in a way that maintains ovococcal shape. (tsui2023negativeregulationof pages 3-4, tsui2023negativeregulationof pages 1-3)

## 8. Warnings / items not yet ready for curation
1. **Taxon transfer risk:** Several strong mechanistic edges are from *S. pneumoniae* (ovococcal) and *S. suis* (ovococcal), but some quantitative localization/ratio evidence is from *S. aureus* (historically coccus but now recognized to elongate slightly). Use *S. aureus* edges as **analogous support** unless independently confirmed in pneumococcus/streptococci. (costa2024theroleof pages 11-13, costa2024theroleof media b704100a)
2. **Edge granularity vs review-level evidence:** Some elongasome composition/requirements (e.g., “MreC/MreD necessary”) are asserted in secondary sources; for high-confidence TraitMech curation, confirm with primary pneumococcal papers when possible. (costa2023newapproachesto pages 205-209)
3. **Ontology grounding gaps:** UniProt accessions, EC numbers, and ChEBI IDs are not present in the retrieved excerpts; curating those should be done by direct database lookup during YAML implementation (do not invent identifiers).

## 9. DOI-first bibliography (with URLs and publication dates where available)
* Costa SF, et al. **The role of GpsB in *Staphylococcus aureus* cell morphogenesis**. *mBio*. **Mar 2024**. DOI: **10.1128/mbio.03235-23**. https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2, costa2024theroleof pages 11-13, costa2024theroleof media b704100a)
* Kumar S.S., Johnson M.D.L., Wilson J.E. **Insights into the enigma of oral streptococci in carcinogenesis**. *Microbiology and Molecular Biology Reviews*. **Jun 2024**. DOI: **10.1128/mmbr.00095-23**. https://doi.org/10.1128/mmbr.00095-23 (kumar2024insightsintothe pages 4-6)
* Battaje R.R., et al. **Models versus pathogens: how conserved is the FtsZ in bacteria?** *Bioscience Reports*. **Feb 2023**. DOI: **10.1042/BSR20221664**. https://doi.org/10.1042/BSR20221664 (battaje2023modelsversuspathogens pages 4-5)
* Jiang Q., et al. **DivIVA Interacts with the Cell Wall Hydrolase MltG To Regulate Peptidoglycan Synthesis in *Streptococcus suis***. *Microbiology Spectrum*. **Jun 2023**. DOI: **10.1128/spectrum.04750-22**. https://doi.org/10.1128/spectrum.04750-22 (jiang2023divivainteractswith pages 9-11)
* Tsui H.-C.T., et al. **Negative regulation of MurZ and MurA underlies the essentiality of GpsB- and StkP-mediated protein phosphorylation in *Streptococcus pneumoniae* D39**. *Molecular Microbiology*. **Jul 2023**. DOI: **10.1111/mmi.15122**. https://doi.org/10.1111/mmi.15122 (tsui2023negativeregulationof pages 3-4, tsui2023negativeregulationof pages 1-3)
* Galinier A., et al. **Recent Advances in Peptidoglycan Synthesis and Regulation in Bacteria**. *Biomolecules*. **Apr 2023**. DOI: **10.3390/biom13050720**. https://doi.org/10.3390/biom13050720 (galinier2023recentadvancesin pages 14-15)

(Additional background sources retrieved but lower priority/less direct mechanistic support for the ovoid trait definition were not emphasized in the main evidence table.)


References

1. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

2. (costa2023newapproachesto pages 205-209): S Francisco Da Costa. New approaches to study staphylococcus aureus elongation and division. Unknown journal, 2023.

3. (kumar2024insightsintothe pages 4-6): Sangeetha Senthil Kumar, Michael D. L. Johnson, and Justin E. Wilson. Insights into the enigma of oral streptococci in carcinogenesis. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00095-23, doi:10.1128/mmbr.00095-23. This article has 20 citations and is from a domain leading peer-reviewed journal.

4. (battaje2023modelsversuspathogens pages 4-5): Rachana Rao Battaje, Ravikant Piyush, Vidyadhar Pratap, and Dulal Panda. Models versus pathogens: how conserved is the ftsz in bacteria? Bioscience Reports, Feb 2023. URL: https://doi.org/10.1042/bsr20221664, doi:10.1042/bsr20221664. This article has 27 citations and is from a peer-reviewed journal.

5. (abdulhadi2024grampositivebacteria pages 7-8): Ali M Hussein Abdulhadi, Iqbal Amer, and Mariam Khalil Mohammed. Gram positive bacteria and their distributions according anatomical site in oral cavity and effects on oral health. International journal of health sciences, 8:180-193, Aug 2024. URL: https://doi.org/10.53730/ijhs.v8n2.15005, doi:10.53730/ijhs.v8n2.15005. This article has 8 citations and is from a peer-reviewed journal.

6. (abdulhadi2024grampositivebacteria pages 8-10): Ali M Hussein Abdulhadi, Iqbal Amer, and Mariam Khalil Mohammed. Gram positive bacteria and their distributions according anatomical site in oral cavity and effects on oral health. International journal of health sciences, 8:180-193, Aug 2024. URL: https://doi.org/10.53730/ijhs.v8n2.15005, doi:10.53730/ijhs.v8n2.15005. This article has 8 citations and is from a peer-reviewed journal.

7. (jiang2023divivainteractswith pages 9-11): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 12 citations and is from a domain leading peer-reviewed journal.

8. (tsui2023negativeregulationof pages 3-4): Ho‐Ching Tiffany Tsui, Merrin Joseph, Jiaqi J. Zheng, Amilcar J. Perez, Irfan Manzoor, Britta E. Rued, John D. Richardson, Pavel Branny, Linda Doubravová, Orietta Massidda, and Malcolm E. Winkler. Negative regulation of murz and mura underlies the essentiality of gpsb‐ and stkp‐mediated protein phosphorylation in streptococcus pneumoniae d39. Molecular Microbiology, 120:351-383, Jul 2023. URL: https://doi.org/10.1111/mmi.15122, doi:10.1111/mmi.15122. This article has 15 citations and is from a domain leading peer-reviewed journal.

9. (tsui2023negativeregulationof pages 1-3): Ho‐Ching Tiffany Tsui, Merrin Joseph, Jiaqi J. Zheng, Amilcar J. Perez, Irfan Manzoor, Britta E. Rued, John D. Richardson, Pavel Branny, Linda Doubravová, Orietta Massidda, and Malcolm E. Winkler. Negative regulation of murz and mura underlies the essentiality of gpsb‐ and stkp‐mediated protein phosphorylation in streptococcus pneumoniae d39. Molecular Microbiology, 120:351-383, Jul 2023. URL: https://doi.org/10.1111/mmi.15122, doi:10.1111/mmi.15122. This article has 15 citations and is from a domain leading peer-reviewed journal.

10. (costa2024theroleof pages 11-13): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

11. (costa2024theroleof media b704100a): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

12. (costa2024theroleof media d2422b21): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

13. (costa2023theroleof pages 12-14): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in cell morphogenesis of staphylococcus aureus. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.16.545294, doi:10.1101/2023.06.16.545294. This article has 4 citations.

14. (tsui2023chromosomalduplicationsof pages 55-57): Ho-Ching Tiffany Tsui, Merrin Joseph, Jiaqi J. Zheng, Amilcar J. Perez, Irfan Manzoor, Britta E. Rued, John D. Richardson, Pavel Branny, Linda Doubravová, Orietta Massidda, and Malcolm E. Winkler. Chromosomal duplications of murz (mura2) or mura (mura1), amino acid substitutions in murz (mura2), and absence of khpab obviate the requirement for protein phosphorylation in streptococcus pneumoniae d39. bioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.03.26.534294, doi:10.1101/2023.03.26.534294. This article has 1 citations.

15. (galinier2023recentadvancesin pages 14-15): Anne Galinier, Clémentine Delan-Forino, Elodie Foulquier, Hakima Lakhal, and Frédérique Pompeo. Recent advances in peptidoglycan synthesis and regulation in bacteria. Biomolecules, 13:720, Apr 2023. URL: https://doi.org/10.3390/biom13050720, doi:10.3390/biom13050720. This article has 68 citations.

16. (costa2023theroleof pages 21-24): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in cell morphogenesis of staphylococcus aureus. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.16.545294, doi:10.1101/2023.06.16.545294. This article has 4 citations.

17. (tsui2023chromosomalduplicationsof pages 57-59): Ho-Ching Tiffany Tsui, Merrin Joseph, Jiaqi J. Zheng, Amilcar J. Perez, Irfan Manzoor, Britta E. Rued, John D. Richardson, Pavel Branny, Linda Doubravová, Orietta Massidda, and Malcolm E. Winkler. Chromosomal duplications of murz (mura2) or mura (mura1), amino acid substitutions in murz (mura2), and absence of khpab obviate the requirement for protein phosphorylation in streptococcus pneumoniae d39. bioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.03.26.534294, doi:10.1101/2023.03.26.534294. This article has 1 citations.