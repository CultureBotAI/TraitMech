---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:09:47.055878'
end_time: '2026-06-18T07:18:29.549087'
duration_seconds: 522.49
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: coccobacillus shaped
  trait_identifier: METPO:1000688
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: coccobacillus_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape intermediate between spherical cocci and elongated bacilli,
    typically appearing as short or plump rods.
  parent_traits: METPO:1000666
  synonyms: coccobacillus
  evidence_summary: 'DOI:10.1128/JB.187.1.54-64.2005: changes shape, from a rod to
    coccobacillus (Supports coccobacillus morphology as a short-rod state associated
    with cell-shape control in representative bacteria.)'
  causal_graph_summary: 'coccobacillus_shaped_short_rod_morphogenesis: 5 nodes, 4
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** coccobacillus shaped
- **METPO identifier:** METPO:1000688
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape intermediate between spherical cocci and elongated bacilli, typically appearing as short or plump rods.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccobacillus
- **Existing evidence:** DOI:10.1128/JB.187.1.54-64.2005: changes shape, from a rod to coccobacillus (Supports coccobacillus morphology as a short-rod state associated with cell-shape control in representative bacteria.)
- **Existing causal graph summary:** coccobacillus_shaped_short_rod_morphogenesis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **coccobacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccobacillus_shaped.yaml`.

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
- **Trait label:** coccobacillus shaped
- **METPO identifier:** METPO:1000688
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape intermediate between spherical cocci and elongated bacilli, typically appearing as short or plump rods.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccobacillus
- **Existing evidence:** DOI:10.1128/JB.187.1.54-64.2005: changes shape, from a rod to coccobacillus (Supports coccobacillus morphology as a short-rod state associated with cell-shape control in representative bacteria.)
- **Existing causal graph summary:** coccobacillus_shaped_short_rod_morphogenesis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **coccobacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccobacillus_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **coccobacillus shaped** (METPO:1000688)

### Scope summary (TraitMech-ready)
**Trait meaning.** *Coccobacillus shaped* denotes a **cell morphology intermediate between cocci and bacilli**, operationally a **short or plump rod** (reduced length-to-width ratio vs. typical bacilli). In practice, this morphology is frequently observed as (i) a **stable taxon-associated morphology** (e.g., described for some pathogens), or (ii) a **transitional morphotype** produced by **growth-condition changes** or **perturbations to peptidoglycan (PG) synthesis and its spatiotemporal control** (elongation vs division). Direct evidence of a **rod → coccobacillus** shift is described for *Rhodobacter sphaeroides* (Slovak et al., 2005) (slovak2005localizationofmreb pages 3-3, slovak2005localizationofmreb pages 7-10). 

**Boundary cases to distinguish in curation.**
1. **True cocci/ovococci**: shape dominated by septal wall insertion and/or limited peripheral synthesis near division; a different trait from coccobacillus (pereira2016ftszdependentelongationof pages 1-2).
2. **Coccoid rounding in survival states (VBNC/LTS)**: many bacteria round up under prolonged incubation/stress; this can pass through coccobacillary intermediates but is not equivalent to genetically encoded coccobacillus morphology (cantlay2024phenotypicandtranscriptional pages 5-6, cantlay2024phenotypicandtranscriptional pages 6-8, barry2024longtermsurvivalphasecells pages 1-2).
3. **Pleomorphism**: some organisms show heterogeneous shapes (including coccobacilli) as part of a broader pleomorphic phenotype; curate cautiously as assay/condition-specific (cantlay2024phenotypicandtranscriptional pages 5-6).

---

## 1) Key concepts & mechanistic definitions (current understanding)

### 1.1 Morphogenesis framework: elongasome vs divisome
Bacterial cell shape is largely sculpted by **where PG is inserted**: **sidewall/lateral insertion for elongation** versus **mid-cell septal synthesis for division**. Rod-shaped bacteria typically use a cytoskeleton-guided **elongasome** (often MreB-associated) to insert PG along the sidewall, while division is coordinated by an **FtsZ-centered divisome** at midcell (pereira2016ftszdependentelongationof pages 1-2). Transitions toward shorter rods/coccobacilli are therefore expected when **elongation is reduced relative to septation**, or when spatial patterning of insertion is altered.

### 1.2 Coccobacillus as an intermediate state on the rod–coccus continuum
A key foundational observation is that *R. sphaeroides* “changes shape, from a rod to coccobacillus,” in work explicitly focused on MreB localization under shape-changing conditions (slovak2005localizationofmreb pages 3-3, slovak2005localizationofmreb pages 7-10). In this framework, coccobacillus can represent a **short-rod state** arising from altered elongasome function and/or growth conditions that reduce elongation.

---

## 2) Recent developments and latest research (prioritize 2023–2024)

### 2.1 Metal-dependent stability of the elongasome transpeptidase PBP2 (2023)
Micelli et al. (PNAS, 2023) identified a **conserved Zn-binding site** in *Acinetobacter baumannii* **PBP2** that is required for elongasome-directed shape maintenance; **Zn deprivation** or **carbapenem exposure** induces a **rod-to-sphere transition** that phenocopies loss of RodA–PBP2 function (micelli2023aconservedzincbinding pages 1-2). Although the endpoint is often spherical rather than coccobacillary, the study is important because it provides a **direct mechanistic handle (metal cofactor → PBP2 stability → morphogenesis)** that can be represented in causal graphs (micelli2023aconservedzincbinding pages 1-2).

### 2.2 Environmentally tuned alternative elongasomes in pathogens (acid pH; 2023)
Castanheira & García-del Portillo (Communications Biology, 2023) provided evidence that *Salmonella* can deploy **two differentially regulated elongasomes**. Under acidic conditions (PCN medium pH 4.6), canonical **PBP2** becomes dispensable while a pathogen-associated **PBP2SAL**-containing system supports rod morphogenesis; notably, ΔmrdA (PBP2-deleted) can still display “genuine rod shape” in PCN pH 4.6, whereas ΔPBP2SAL cells are shorter and frequently abnormal (“lemon-shaped”) (castanheira2023evidenceoftwo pages 2-3). This supports an **environment → PBP expression/complex assembly → morphology** causal chain (castanheira2023evidenceoftwo pages 2-3).

### 2.3 New determinants of subtle elongation in an organism historically considered spherical (2024)
Costa et al. (mBio, 2024) highlight that *Staphylococcus aureus* (long assumed strictly spherical) undergoes **slight elongation** during its cell cycle and that elongation depends on **RodA/PBP3**. They further identify **GpsB** as a major determinant: loss of gpsB partially delocalizes **PBP2 and PBP4**, increasing peripheral PG insertion/crosslinking and making cells more spherical (costa2024theroleof pages 1-2). This is a strong example of **spatiotemporal control of PG enzymes as a “morphological rheostat”** (costa2024theroleof pages 1-2).

### 2.4 Coccobacilli in stress/survival transitions (VBNC and long-term survival; 2024)
- **Francisella VBNC transition (Frontiers in Microbiology, 2024).** Cantlay et al. report that at **24 h stationary phase**, *Francisella tularensis* LVS appears as “**small pleomorphic coccobacilli**,” and with prolonged incubation (≥48 h) cells become significantly rounder (ImageJ circularity), coincident with VBNC onset around ~96 h and precipitous CFU decline (cantlay2024phenotypicandtranscriptional pages 5-6, cantlay2024phenotypicandtranscriptional pages 6-8). They report no CFU recovered after 7 days despite ~90% viability at 1 week and ~70% at 2–4 weeks (cantlay2024phenotypicandtranscriptional pages 6-8).
- **Food-safety relevant long-term survival morphotype (Frontiers in Food Science and Technology, 2024).** Barry et al. grew *Salmonella Enteritidis* for 20 h (STAT) vs 21 days (LTS) and found STAT cells “predominantly rod-shaped” while LTS cells were “coccoid,” and LTS showed substantially reduced log reductions under atmospheric cold plasma treatment (e.g., 1 min: 1.0 log10 reduction for STAT vs 0.04 for LTS in PBS) (barry2024longtermsurvivalphasecells pages 1-2).

---

## 3) Current applications & real-world implementations

1. **Clinical and diagnostic microbiology descriptors.** “Coccobacilli” remains a common morphology descriptor in microscopy-based workflows; however, the evidence here indicates morphology can be **highly condition-dependent**, which can confound interpretation if growth phase/stress is not controlled (cantlay2024phenotypicandtranscriptional pages 5-6, barry2024longtermsurvivalphasecells pages 1-2).

2. **Antimicrobial strategy relevance (shape machinery as drug target).** The elongasome/divisome PG synthases (RodA/SEDS proteins and class B PBPs such as PBP2) and their cofactor requirements (Zn) are actionable targets and influence susceptibility; carbapenems acylating PBP2 and Zn-site mutations causing rod-shape loss illustrate how inhibiting elongation can drive rounding and potentially alter fitness/drug susceptibility (micelli2023aconservedzincbinding pages 1-2).

3. **Food safety / process validation.** Cold plasma inactivation efficacy can be **morphotype- and physiological-state dependent**, with long-term survival (coccoid) cells showing markedly higher tolerance than stationary-phase rods, suggesting process validation should consider survival-state morphology (barry2024longtermsurvivalphasecells pages 1-2).

---

## 4) Candidate causal graph nodes (grouped by type)

### 4.1 Environmental and experimental factors (candidate nodes)
- **Low light intensity** (ENVO label-only candidate; experimental condition) (slovak2005localizationofmreb pages 3-3)
- **Aerobic growth** (ENVO label-only candidate) (slovak2005localizationofmreb pages 3-3)
- **Acidic pH (e.g., pH 4.6)** (ENVO label-only candidate) (castanheira2023evidenceoftwo pages 2-3)
- **Zinc deprivation / Zn limitation** (CHEBI:zinc(2+) as chemical node + “zinc-limited growth” environment) (micelli2023aconservedzincbinding pages 1-2)
- **Carbapenem exposure (β-lactam antibiotic class)** (CHEBI class-level grounding may be needed; drug node) (micelli2023aconservedzincbinding pages 1-2)
- **Stationary phase** (process node) (cantlay2024phenotypicandtranscriptional pages 5-6)
- **VBNC state transition** (process/physiological state node) (cantlay2024phenotypicandtranscriptional pages 6-8)
- **Long-term survival phase (21 days culture)** (process/physiological state node) (barry2024longtermsurvivalphasecells pages 1-2)
- **Atmospheric cold plasma treatment** (experimental intervention node) (barry2024longtermsurvivalphasecells pages 1-2)

### 4.2 Genes/proteins/complexes (candidate nodes)
(Protein nodes should be grounded to UniProt per taxon during YAML curation.)
- **mreB (MreB)** (actin-like cytoskeletal protein; elongasome-associated) (slovak2005localizationofmreb pages 7-10, slovak2005localizationofmreb pages 3-3)
- **rodA (RodA; SEDS family)** (elongasome PG polymerase partner) (slovak2005localizationofmreb pages 3-3, micelli2023aconservedzincbinding pages 1-2)
- **mrdA / PBP2** (class B PBP; elongasome transpeptidase) (micelli2023aconservedzincbinding pages 1-2, castanheira2023evidenceoftwo pages 2-3)
- **PBP2SAL (alternative PBP in Salmonella)** (castanheira2023evidenceoftwo pages 2-3)
- **PBP3 (and RodA/PBP3 pair in S. aureus)** (costa2024theroleof pages 1-2)
- **PBP4 (S. aureus)** (costa2024theroleof pages 1-2)
- **gpsB (GpsB; regulator of PBP localization)** (costa2024theroleof pages 1-2)
- **ftsZ (FtsZ; divisome organizer)** (pereira2016ftszdependentelongationof pages 1-2, pereira2016ftszdependentelongationof pages 2-3)

### 4.3 Cellular processes (candidate nodes with GO grounding suggestions)
- **Peptidoglycan biosynthetic process** (GO term to be selected during curation) (pereira2016ftszdependentelongationof pages 1-2)
- **Bacterial-type cell division** (GO) (pereira2016ftszdependentelongationof pages 1-2)
- **Cell shape determination** (GO) (pereira2016ftszdependentelongationof pages 1-2)
- **Regulation of protein localization (e.g., PBPs to septum/periphery)** (GO) (costa2024theroleof pages 1-2)

---

## 5) Evidence-backed candidate causal edges (curation table)
The following table is designed for direct translation into `data/traits/morphology/coccobacillus_shaped.yaml` as candidate edges, with confidence notes.

| Edge (subject–predicate–object) | Node types | Example taxa / assay context | Evidence snippet (verbatim short quote) | Reference (DOI + year + URL) | Notes / curation confidence |
|---|---|---|---|---|---|
| low light growth → decreases cell length → coccobacillus-like short-rod morphology | environment → phenotype | *Rhodobacter sphaeroides* grown photoheterotrophically at different light levels | "the longest cells occurred in aerobic growth while shortest cells occurred under low light"; widths "1.14 to 1.20 μm" (slovak2005localizationofmreb pages 3-3) | Slovak et al. 2005. DOI:10.1128/JB.187.1.54-64.2005. https://doi.org/10.1128/JB.187.1.54-64.2005 | Medium; direct environment–morphology association, but taxon-specific and phrased as shorter cells rather than an explicit curated coccobacillus class. |
| mreB / rodA locus → supports → rod / non-spherical cell-shape maintenance | gene/protein → process/phenotype | *R. sphaeroides* cell-shape genetics and GFP-MreB localization | "specifically amplified 'mreB and rodA'" and focused on "conditions causing changes in cell shape" (slovak2005localizationofmreb pages 3-3); "MreB is thought to be a bacterial actin homolog that defines the morphology of rod-shaped bacteria. *Rhodobacter sphaeroides* changes shape, from a rod to coccobacillus" (slovak2005localizationofmreb pages 3-3, slovak2005localizationofmreb pages 7-10) | Slovak et al. 2005. DOI:10.1128/JB.187.1.54-64.2005. https://doi.org/10.1128/JB.187.1.54-64.2005 | Medium; strong relevance to short-rod morphogenesis, but the paper links MreB to shape control rather than demonstrating a single direct causal edge to coccobacillus state. |
| zinc deprivation → induces → rod-to-sphere transition | environment → phenotype | *Acinetobacter baumannii* under Zn-limited growth | "zinc (Zn) deprivation; this phenotype resembles loss of the RodA–PBP2 elongasome" and "rod-to-sphere morphological transition" (micelli2023aconservedzincbinding pages 1-2) | Micelli et al. 2023. DOI:10.1073/pnas.2215237120. https://doi.org/10.1073/pnas.2215237120 | High for rod-to-sphere rounding; for TraitMech this is more a negative edge away from short-rod morphology than a direct cause of coccobacillus shape. |
| carbapenem exposure → inhibits PBP2 transpeptidase activity → rod-to-sphere transition | chemical/drug → protein activity → phenotype | *A. baumannii* exposed to carbapenems | "exposure to carbapenems... induces a rod-to-sphere morphological transition" and "Carbapenems preferentially acylate PBP2 in *A. baumannii*, blocking the transpeptidase activity of the RodA–PBP2 system" (micelli2023aconservedzincbinding pages 1-2) | Micelli et al. 2023. DOI:10.1073/pnas.2215237120. https://doi.org/10.1073/pnas.2215237120 | High; mechanistically specific and experimentally supported, though outcome is sphere rather than coccobacillus. |
| PBP2 Zn-binding site integrity → required for → elongasome-directed rod shape | protein structural feature → process/phenotype | *A. baumannii* PBP2 structural/genetic analysis | "identified an unexpected Zn coordination site in the transpeptidase domain that is required for protein stability" and "Mutations in this Zn-binding site lead to loss of rod shape" (micelli2023aconservedzincbinding pages 1-2) | Micelli et al. 2023. DOI:10.1073/pnas.2215237120. https://doi.org/10.1073/pnas.2215237120 | High; strong molecular candidate node for shape control, but not specific to coccobacillus intermediate state. |
| acidic pH → induces PBP2SAL-containing elongasome → supports rod shape | environment → protein complex → phenotype | *Salmonella enterica* serovar Typhimurium in PCN pH 4.6 | "PBP2 is dispensable in acidic pH, while PBP2SAL... expression is upregulated at low pH"; "ΔmrdA (PBP2-deleted) cells can exhibit genuine rod shape with polar caps in PCN pH 4.6" (castanheira2023evidenceoftwo pages 2-3) | Castanheira & García-del Portillo 2023. DOI:10.1038/s42003-023-05308-w. https://doi.org/10.1038/s42003-023-05308-w | Medium-high; direct support for alternative elongasome preserving rod morphogenesis under host-like acidity. Useful comparator edge for boundaries around short-rod/coccobacillus states. |
| loss of PBP2SAL in acidic medium → causes → shortened / lemon-shaped cells | gene/protein → phenotype | *S. Typhimurium* ΔPBP2SAL in PCN pH 4.6 | "ΔPBP2SAL cells show alterations—many appear lemon-shaped and are shorter than wild-type in PCN pH 4.6" (castanheira2023evidenceoftwo pages 2-3) | Castanheira & García-del Portillo 2023. DOI:10.1038/s42003-023-05308-w. https://doi.org/10.1038/s42003-023-05308-w | Medium; shape is intermediate/abnormal rather than explicitly coccobacillus; potentially useful as inferred short-rod edge. |
| GpsB → regulates localization of → PBP2 and PBP4 | protein → protein localization | *Staphylococcus aureus* NTML screen and deletion mutants | "a gpsB mutant shows the strongest morphological phenotype, driven by partial delocalization of PBP2 and PBP4 away from the division septum" (costa2024theroleof pages 1-2) | Costa et al. 2024. DOI:10.1128/mBio.03235-23. https://doi.org/10.1128/mbio.03235-23 | High; direct localization edge supported by genetics and morphology quantification. |
| loss of gpsB → increases peripheral PG insertion/crosslinking → more spherical cells | gene/protein → process → phenotype | *S. aureus* ΔgpsB mutants | "Increased PBP2/PBP4 at the cell periphery raises peptidoglycan insertion and crosslinking throughout the cell... impairing elongation and producing more spherical cells" (costa2024theroleof pages 1-2) | Costa et al. 2024. DOI:10.1128/mBio.03235-23. https://doi.org/10.1128/mbio.03235-23 | High for spherical shift; negative comparator for coccobacillus/elongated states. |
| RodA/PBP3-mediated elongation → increases → long/short axis ratio | protein complex → phenotype | *S. aureus* cell-cycle elongation | "This elongation depends on the SEDS/PBP pair RodA/PBP3" and is seen as an "increased ratio of long to short cell axes" (costa2024theroleof pages 1-2) | Costa et al. 2024. DOI:10.1128/mBio.03235-23. https://doi.org/10.1128/mbio.03235-23 | Medium-high; relevant positive edge for intermediate non-spherical morphogenesis, though species is ovococcoid not classically coccobacillary. |
| stationary phase (24 h) → associated with → small pleomorphic coccobacilli | process/growth phase → phenotype | *Francisella tularensis* LVS broth culture | "At 24 h (stationary phase) cells are described as 'small pleomorphic coccobacilli with even membrane staining'" (cantlay2024phenotypicandtranscriptional pages 5-6) | Cantlay et al. 2024. DOI:10.3389/fmicb.2024.1347488. https://doi.org/10.3389/fmicb.2024.1347488 | High; direct match to target morphology term, but likely assay- and taxon-specific physiological state. |
| prolonged culture / VBNC entry → increases cell rounding → more coccoid morphology | process/state transition → phenotype | *F. tularensis* LVS 48–672 h culture | "48–672 h were 'signiﬁcantly rounder than bacteria from 24-h old cultures'" and "By 96 h plating eﬃciency starts to fall" (cantlay2024phenotypicandtranscriptional pages 6-8) | Cantlay et al. 2024. DOI:10.3389/fmicb.2024.1347488. https://doi.org/10.3389/fmicb.2024.1347488 | High for rounding during VBNC transition; suggests coccobacillus can be transitional and should not be overgeneralized as a fixed morphology trait. |
| long-term survival phase (21 days) → shifts morphology to → coccoid cells | process/growth phase → phenotype | *Salmonella Enteritidis* ATCC 13076, 21-day LTS vs 20 h STAT | "The STAT cells were predominantly rod-shaped whereas LTS cells were coccoid" (barry2024longtermsurvivalphasecells pages 1-2) | Barry et al. 2024. DOI:10.3389/frfst.2024.1442761. https://doi.org/10.3389/frfst.2024.1442761 | High for phase-associated morphological shift; outcome is coccoid rather than coccobacillus, useful as boundary case. |
| long-term survival phase coccoid morphology → associated with → higher ACP tolerance | phenotype/state → assay outcome | *S. Enteritidis* exposed to atmospheric cold plasma | "reductions in LTS cells were significantly lower... 0.04, 0.06, 0.01, and 0.11" vs STAT "1.0, 0.95, 1.45, and 1.44" log10 CFU/mL (barry2024longtermsurvivalphasecells pages 1-2) | Barry et al. 2024. DOI:10.3389/frfst.2024.1442761. https://doi.org/10.3389/frfst.2024.1442761 | Medium; association between coccoid/LTS state and resistance phenotype, not a mechanism of coccobacillus formation. |
| ftsZ G193D mutation → causes → elongated / curved cells | gene/protein mutation → phenotype | *S. aureus* mutant M5 | "a specific FtsZ point mutation (G193D)... produced elongated/curved cells: length-to-width ratio was significantly increased (measurements on n=50 cells; P < 0.001)" (pereira2016ftszdependentelongationof pages 2-3) | Pereira et al. 2016. DOI:10.1128/mBio.00908-16. https://doi.org/10.1128/mbio.00908-16 | High; strong causal mutation edge showing division machinery can shift coccoid cells toward short-rod/elongated morphologies. |
| altered FtsZ filament properties → directs asymmetric/helical PG insertion → elongation from coccoid state | protein conformation/process → PG insertion pattern → phenotype | *S. aureus* ftsZG193D mutant | "altered FtsZ filaments (more twisted and shorter) direct asymmetric, helical cell-wall insertion, generating elongation" (pereira2016ftszdependentelongationof pages 1-2); "This helical pattern of wall insertion leads to elongation" (pereira2016ftszdependentelongationof pages 1-2) | Pereira et al. 2016. DOI:10.1128/mBio.00908-16. https://doi.org/10.1128/mbio.00908-16 | High; mechanistically detailed and useful for graph edges linking divisome geometry to intermediate rod-like morphology. |


*Table: This table lists candidate subject–predicate–object edges relevant to coccobacillus or short-rod morphology, with direct evidence snippets, references, and curation confidence. It is designed to support TraitMech graph curation while distinguishing direct morphology edges from boundary-case rounding or elongation transitions.*

---

## 6) Relevant statistics and quantitative data from recent studies

- **F. tularensis morphology + VBNC kinetics (2024):** cultures incubated ≥48 h became “significantly rounder” than 24 h (p < 0.001) with circularity measured in ImageJ across ≥2200 bacteria; VBNC onset around ~96 h, with CFU falling precipitously thereafter; “no CFU were recovered” after 7 days while viability remained ~90% at 1 week and ~70% at 2–4 weeks; detached outer membrane frequency increased from 1.3% (24 h) to 47.9% (336 h) (cantlay2024phenotypicandtranscriptional pages 5-6, cantlay2024phenotypicandtranscriptional pages 6-8).
- **S. Enteritidis long-term survival vs plasma tolerance (2024):** inocula ~7.0 log10 CFU/mL; ACP in PBS produced STAT reductions of 1.0–1.45 log10 CFU/mL vs LTS reductions of 0.01–0.11 over 1–4 min; times to 4- and 5-log reduction (model-based) 5.29 and 5.78 min (barry2024longtermsurvivalphasecells pages 1-2).
- **FtsZ mutation and elongation measurements (2016):** *S. aureus* ftsZG193D mutant had significantly increased length-to-width ratio (n = 50; P < 0.001) and slower growth (doubling 47 vs 25 min) (pereira2016ftszdependentelongationof pages 2-3).

---

## 7) Warnings / non-curation recommendations

1. **Do not over-curate coccoid survival morphotypes as “coccobacillus shaped.”** The 2024 survival-state examples show rounding and pleomorphism, and may involve broad physiological remodeling; these are best curated as **conditional morphology** edges (growth phase → morphology) with explicit context rather than as constitutive trait edges (cantlay2024phenotypicandtranscriptional pages 5-6, cantlay2024phenotypicandtranscriptional pages 6-8, barry2024longtermsurvivalphasecells pages 1-2).

2. **Taxon specificity is high.** Mechanistic edges involving PBP2SAL are *Salmonella*-specific; GpsB–PBP localization is supported in *S. aureus*; MreB/rodA evidence is from *R. sphaeroides*. These should be tagged as taxon-scoped unless additional cross-taxon evidence is curated (slovak2005localizationofmreb pages 3-3, castanheira2023evidenceoftwo pages 2-3, costa2024theroleof pages 1-2).

3. **Many recent mechanistic studies induce rod→sphere rather than rod→coccobacillus.** Zn limitation/carbapenems in *A. baumannii* are powerful mechanistic anchors for the elongasome but may represent a different trait endpoint; curate as negative edges (loss of elongation → rounding) and use them as mechanistic context for intermediate morphologies only when supported (micelli2023aconservedzincbinding pages 1-2).

---

## DOI-first bibliography (with dates and URLs)

1. **Micelli C, et al.** (2023-02). *A conserved zinc-binding site in Acinetobacter baumannii PBP2 required for elongasome-directed bacterial cell shape.* **PNAS**. DOI: **10.1073/pnas.2215237120**. https://doi.org/10.1073/pnas.2215237120 (micelli2023aconservedzincbinding pages 1-2)
2. **Castanheira S, García-del Portillo F.** (2023-09). *Evidence of two differentially regulated elongasomes in Salmonella.* **Communications Biology**. DOI: **10.1038/s42003-023-05308-w**. https://doi.org/10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 2-3)
3. **Costa SF, et al.** (2024-03). *The role of GpsB in Staphylococcus aureus cell morphogenesis.* **mBio**. DOI: **10.1128/mBio.03235-23**. https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2, costa2024theroleof pages 2-4)
4. **Cantlay S, et al.** (2024-02). *Phenotypic and transcriptional characterization of F. tularensis LVS during transition into a viable but non-culturable state.* **Frontiers in Microbiology**. DOI: **10.3389/fmicb.2024.1347488**. https://doi.org/10.3389/fmicb.2024.1347488 (cantlay2024phenotypicandtranscriptional pages 5-6, cantlay2024phenotypicandtranscriptional pages 6-8)
5. **Barry K, et al.** (2024-10). *Long-term-survival phase cells of Salmonella enteritidis ATCC 13076 exhibit significantly greater tolerance to atmospheric cold plasma treatment of shell eggs.* **Frontiers in Food Science and Technology**. DOI: **10.3389/frfst.2024.1442761**. https://doi.org/10.3389/frfst.2024.1442761 (barry2024longtermsurvivalphasecells pages 1-2)
6. **Slovak PM, Wadhams GH, Armitage JP.** (2005-01). *Localization of MreB in Rhodobacter sphaeroides under conditions causing changes in cell shape and membrane structure.* **Journal of Bacteriology**. DOI: **10.1128/JB.187.1.54-64.2005**. https://doi.org/10.1128/JB.187.1.54-64.2005 (slovak2005localizationofmreb pages 3-3, slovak2005localizationofmreb pages 7-10)
7. **Pereira AR, et al.** (2016-11). *FtsZ-Dependent Elongation of a Coccoid Bacterium.* **mBio**. DOI: **10.1128/mBio.00908-16**. https://doi.org/10.1128/mbio.00908-16 (pereira2016ftszdependentelongationof pages 1-2, pereira2016ftszdependentelongationof pages 2-3)



References

1. (slovak2005localizationofmreb pages 3-3): Peter M. Slovak, George H. Wadhams, and Judith P. Armitage. Localization of mreb in rhodobacter sphaeroides under conditions causing changes in cell shape and membrane structure. Journal of Bacteriology, 187:54-64, Jan 2005. URL: https://doi.org/10.1128/jb.187.1.54-64.2005, doi:10.1128/jb.187.1.54-64.2005. This article has 105 citations and is from a peer-reviewed journal.

2. (slovak2005localizationofmreb pages 7-10): Peter M. Slovak, George H. Wadhams, and Judith P. Armitage. Localization of mreb in rhodobacter sphaeroides under conditions causing changes in cell shape and membrane structure. Journal of Bacteriology, 187:54-64, Jan 2005. URL: https://doi.org/10.1128/jb.187.1.54-64.2005, doi:10.1128/jb.187.1.54-64.2005. This article has 105 citations and is from a peer-reviewed journal.

3. (pereira2016ftszdependentelongationof pages 1-2): Ana R. Pereira, Jen Hsin, Ewa Król, Andreia C. Tavares, Pierre Flores, Egbert Hoiczyk, Natalie Ng, Alex Dajkovic, Yves V. Brun, Michael S. VanNieuwenhze, Terry Roemer, Rut Carballido-Lopez, Dirk-Jan Scheffers, Kerwyn Casey Huang, and Mariana G. Pinho. Ftsz-dependent elongation of a coccoid bacterium. Nov 2016. URL: https://doi.org/10.1128/mbio.00908-16, doi:10.1128/mbio.00908-16. This article has 29 citations and is from a domain leading peer-reviewed journal.

4. (cantlay2024phenotypicandtranscriptional pages 5-6): Stuart Cantlay, Nicole L. Garrison, Rachelle Patterson, Kassey Wagner, Zoei Kirk, Jun Fan, Donald A. Primerano, Mara L. G. Sullivan, Jonathan M. Franks, Donna B. Stolz, and Joseph Horzempa. Phenotypic and transcriptional characterization of f. tularensis lvs during transition into a viable but non-culturable state. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347488, doi:10.3389/fmicb.2024.1347488. This article has 8 citations and is from a peer-reviewed journal.

5. (cantlay2024phenotypicandtranscriptional pages 6-8): Stuart Cantlay, Nicole L. Garrison, Rachelle Patterson, Kassey Wagner, Zoei Kirk, Jun Fan, Donald A. Primerano, Mara L. G. Sullivan, Jonathan M. Franks, Donna B. Stolz, and Joseph Horzempa. Phenotypic and transcriptional characterization of f. tularensis lvs during transition into a viable but non-culturable state. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347488, doi:10.3389/fmicb.2024.1347488. This article has 8 citations and is from a peer-reviewed journal.

6. (barry2024longtermsurvivalphasecells pages 1-2): Kia Barry, Aubrey Mendonça, Gregory J. Phillips, Terri Boylston, Paulo Fortes-Da-Silva, Byron Brehm-Stecher, Vijay Juneja, and Zifan Wan. Long-term-survival phase cells of salmonella enteritidis atcc 13076 exhibit significantly greater tolerance to atmospheric cold plasma treatment of shell eggs. Frontiers in Food Science and Technology, Oct 2024. URL: https://doi.org/10.3389/frfst.2024.1442761, doi:10.3389/frfst.2024.1442761. This article has 2 citations.

7. (micelli2023aconservedzincbinding pages 1-2): Carmina Micelli, Yunfei Dai, Nicole Raustad, Ralph R. Isberg, Christopher G. Dowson, Adrian J. Lloyd, Edward Geisinger, Allister Crow, and David I. Roper. A conserved zinc-binding site in acinetobacter baumannii pbp2 required for elongasome-directed bacterial cell shape. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120, doi:10.1073/pnas.2215237120. This article has 21 citations and is from a highest quality peer-reviewed journal.

8. (castanheira2023evidenceoftwo pages 2-3): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 15 citations and is from a peer-reviewed journal.

9. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

10. (pereira2016ftszdependentelongationof pages 2-3): Ana R. Pereira, Jen Hsin, Ewa Król, Andreia C. Tavares, Pierre Flores, Egbert Hoiczyk, Natalie Ng, Alex Dajkovic, Yves V. Brun, Michael S. VanNieuwenhze, Terry Roemer, Rut Carballido-Lopez, Dirk-Jan Scheffers, Kerwyn Casey Huang, and Mariana G. Pinho. Ftsz-dependent elongation of a coccoid bacterium. Nov 2016. URL: https://doi.org/10.1128/mbio.00908-16, doi:10.1128/mbio.00908-16. This article has 29 citations and is from a domain leading peer-reviewed journal.

11. (costa2024theroleof pages 2-4): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.