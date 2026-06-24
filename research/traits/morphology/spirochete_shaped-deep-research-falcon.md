---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:40:27.058755'
end_time: '2026-06-18T09:56:18.611630'
duration_seconds: 951.55
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: spirochete shaped
  trait_identifier: METPO:1000693
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: spirochete_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has an elongated, tightly coiled helical
    morphology with periplasmic flagella (endoflagella) located between the cell wall
    and outer membrane.
  parent_traits: METPO:1000666
  synonyms: spirochete
  evidence_summary: 'DOI:10.1073/pnas.200221797: periplasmic flagella ... confer in
    part its flat-wave morphology (Supports spirochete morphology as a cell-cylinder
    and periplasmic-flagella interaction.)'
  causal_graph_summary: 'spirochete_shaped_periplasmic_flagella: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spirochete shaped
- **METPO identifier:** METPO:1000693
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated, tightly coiled helical morphology with periplasmic flagella (endoflagella) located between the cell wall and outer membrane.
- **Parent traits:** METPO:1000666
- **Synonyms:** spirochete
- **Existing evidence:** DOI:10.1073/pnas.200221797: periplasmic flagella ... confer in part its flat-wave morphology (Supports spirochete morphology as a cell-cylinder and periplasmic-flagella interaction.)
- **Existing causal graph summary:** spirochete_shaped_periplasmic_flagella: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **spirochete shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spirochete_shaped.yaml`.

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
- **Trait label:** spirochete shaped
- **METPO identifier:** METPO:1000693
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated, tightly coiled helical morphology with periplasmic flagella (endoflagella) located between the cell wall and outer membrane.
- **Parent traits:** METPO:1000666
- **Synonyms:** spirochete
- **Existing evidence:** DOI:10.1073/pnas.200221797: periplasmic flagella ... confer in part its flat-wave morphology (Supports spirochete morphology as a cell-cylinder and periplasmic-flagella interaction.)
- **Existing causal graph summary:** spirochete_shaped_periplasmic_flagella: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **spirochete shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spirochete_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **spirochete shaped** (METPO:1000693)

### 0) Scope summary (TraitMech curation focus)
**Trait definition (given):** “A cell shape in which an organism has an elongated, tightly coiled helical morphology with periplasmic flagella (endoflagella) located between the cell wall and outer membrane.”

**Interpretation for causal-graph curation:** *spirochete shaped* is best curated as a **morphology class** that emerges from **mechanical coupling between a cell cylinder/envelope and internally located periplasmic flagella**. The trait is therefore not just “helical cell shape,” but **helical/wavy/flat-wave forms that depend on endoflagellar architecture and its interaction with the envelope/periplasm** (lynch2023lysinoalaninecrosslinkingis pages 1-2, thomasUnknownyearthedesignof pages 57-59, abe2023machinelearningbasedmotion pages 1-2).

**Boundary cases / nearby traits (avoid over-curation):**
- **Generic helical rods** without periplasmic flagella should not be mapped to this trait solely based on “helical” appearance; METPO:1000693 explicitly requires periplasmic endoflagella (lynch2023lysinoalaninecrosslinkingis pages 1-2, abe2023machinelearningbasedmotion pages 1-2).
- **Pleomorphs** (round bodies/blebs/biofilms) in *Borrelia* are morphotypes distinct from the canonical spirochetal waveform and may involve different mechanisms (not sufficiently evidenced in the retrieved excerpts for curation here).
- **Wall-less helical bacteria (e.g., Spiroplasma)** can be helical via MreB-based ribbons; mechanistically relevant as a contrast but not the same trait (not a spirochete/endoflagella mechanism) (農研機構Unknownyeardp10102p1002 pages 7-8).

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Periplasmic flagella/endoflagella as a shape-determining cytoskeleton
A central mechanistic concept is that **spirochetal flagella are enclosed in the periplasm** and **their rotation and geometry distort/push the cell body**, meaning the flagella are both a propulsion system and an internal “shape actuator” (lynch2023lysinoalaninecrosslinkingis pages 1-2). A 2024 review of flagellar motors explicitly notes spirochetal periplasmic flagella “serve as a cytoskeleton to maintain a spiral-…” (nakamura2024structureanddynamics pages 17-18).

### 1.2 Morphological variants within “spirochete shaped”: corkscrew vs flat-wave
The retrieved comparative morphology description ties **endoflagella number/overlap/arrangement** to whether cells appear **flat-wave** (e.g., *Borrelia* with overlapping ribbons) versus **corkscrew** (e.g., *Leptospira* with fewer/non-overlapping filaments) (thomasUnknownyearthedesignof pages 57-59).

### 1.3 Envelope/periplasm as the physical context for shaping
The periplasm (GO:0042597) and the diderm envelope (outer membrane GO:0019867, peptidoglycan layer) constrain how endoflagella can wrap, supercoil, and transmit forces to bend the cell cylinder. A strong mechanistic boundary-case example is that **ectopic periplasmic filament formation** in a Gram-negative context can **mislocalize peptidoglycan-synthesis machinery** and change curvature, showing how **periplasmic filaments can reshape cells via envelope-growth processes** (halte2024flhefunctionsas pages 2-3).

---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 2024: FlgV as a spirochete flagellar assembly modulator with morphology consequences
A major 2024 development is the identification/characterization of **FlgV (bb0268)** as a **basal-body-associated structural component** that **modulates flagellar filament synthesis** in *Borrelia burgdorferi* (Nature Communications, 2024-11-??; DOI:10.1038/s41467-024-54806-w; https://doi.org/10.1038/s41467-024-54806-w) (zambacampero2024broadlyconservedflgv pages 1-2, zambacampero2024broadlyconservedflgv pages 7-10). Importantly, quantitative cryo-ET-based counts show that altering FlgV changes filament numbers (WT mean 8.2; ΔflgV mean 6.7; overexpression mean 4.2; all n values and details in excerpt) (zambacampero2024broadlyconservedflgv pages 7-10). The same work reports **growth and division phenotypes** (e.g., longer spirochetes, conjoined cells, septa) linking flagellar assembly to whole-cell morphology/division (zambacampero2024broadlyconservedflgv pages 4-6, zambacampero2024broadlyconservedflgv pages 13-14).

### 2.2 2023: Hook post-translational chemistry (lysinoalanine crosslink) as a conserved requirement for spirochete motility
Lynch et al. (PNAS Nexus, 2023-10; DOI:10.1093/pnasnexus/pgad349; https://doi.org/10.1093/pnasnexus/pgad349) showed that **lysinoalanine (Lal) crosslinking in FlgE (hook protein)** is conserved across spirochetes and **required for motility** in representative pathogens (lynch2023lysinoalaninecrosslinkingis pages 1-2). This supports a mechanistic view that **hook mechanical integrity** is important for transmitting motor forces through periplasmic filaments that deform the body (lynch2023lysinoalaninecrosslinkingis pages 1-2).

### 2.3 2023: Quantitative, label-free analysis linking periplasmic flagella-driven rolling to host-surface crawling
Abe et al. (Nature Communications, 2023-12; DOI:10.1038/s41467-023-43366-0; https://doi.org/10.1038/s41467-023-43366-0) describe that **Leptospira spp. possess two periplasmic flagella** and that their rotation beneath the outer membrane **drives rolling of the spiral cell body** for swimming and crawling (abe2023machinelearningbasedmotion pages 1-2). This work also focuses on the **mechanical interface between spiral-body rotation and adhesion** during crawling on host cells (abe2023machinelearningbasedmotion pages 4-5, abe2023machinelearningbasedmotion pages 1-2).

### 2.4 2024 (non-spirochete but mechanistically informative): periplasmic filament formation can rewire peptidoglycan-growth localization
Halte et al. (Nature Communications, 2024-07; DOI:10.1038/s41467-024-50278-0; https://doi.org/10.1038/s41467-024-50278-0) show that loss of **FlhE** permits periplasmic filament assembly and that this **mislocalizes divisome and elongasome complexes required for peptidoglycan synthesis**, producing altered curvature and occasional lysis (halte2024flhefunctionsas pages 2-3). While not a spirochete system, it is strong causal evidence that **periplasmic filament structures can drive cell-shape changes via envelope-growth machinery**, which is conceptually relevant to spirochetal body plan constraints.

---

## 3) Current applications and real-world implementations

### 3.1 Pathogenesis/virulence phenotypes depend on spirochetal motility and thus on endoflagella mechanics
The 2024 FlgV study explicitly links a flagellar assembly factor to **attenuated dissemination/infection in mice** (in vivo implementation of motility-linked phenotype), reinforcing that periplasmic-flagella-associated morphology/motility traits are clinically relevant (zambacampero2024broadlyconservedflgv pages 1-2, zambacampero2024broadlyconservedflgv pages 14-15).

### 3.2 Quantitative motility phenotyping on host cells without genetic manipulation
Abe et al. provides a **label-free machine-learning motion tracking** method for leptospiral motility on cultured cells; while this is primarily a motility assay, it directly measures the functional consequences of spiral-body rolling and adhesion on crawling performance (abe2023machinelearningbasedmotion pages 4-5, abe2023machinelearningbasedmotion pages 1-2).

---

## 4) Expert opinions / authoritative synthesis

### 4.1 Flagellar motor reviews emphasize mechanical design variables that plausibly tune spirochetal waveform
Nakamura & Minamino (Biomolecules, 2024-11; DOI:10.3390/biom14121488; https://doi.org/10.3390/biom14121488) synthesize current understanding that **hook flexibility/length control torque transmission and filament orientation** and that hook length is genetically controlled (FliK/FlhB) and “optimized” for bundle stability (nakamura2024structureanddynamics pages 17-18). While not spirochete-specific, this provides authoritative context for curating edges that connect **hook properties → filament geometry → cell-level waveform**.

### 4.2 Spirochetal waveform depends on endoflagella arrangement
The comparative description (Borrelia flat-wave with overlapping periplasmic flagella ribbon vs Leptospira corkscrew with single/non-overlapping flagellum) is an expert-style synthesis linking architecture to gross morphology (thomasUnknownyearthedesignof pages 57-59). Because the bibliographic metadata is incomplete in the retrieved record, this should support but not anchor high-confidence curation.

---

## 5) Relevant statistics and data points from recent studies

- **Flagellar filament counts in *B. burgdorferi* as a function of FlgV levels (cryo-ET):** WT mean 8.2 filaments; ΔflgV mean 6.7 (n=21); complemented mean 8.5; FlgV overexpression mean 4.2 (n=18) (zambacampero2024broadlyconservedflgv pages 7-10). These are directly useful quantitative edges for “FlgV → filament assembly/number.”
- **Growth/division statistic (ΔflgV vs WT):** ΔflgV doubling time 8.5 h vs WT 4.6 h (zambacampero2024broadlyconservedflgv pages 4-6).
- **Motility conversion efficiency example values (context for mechanical modeling in Leptospira crawling vs swimming):** *Vibrio alginolyticus* ≃0.07; *Leptospira biflexa* ≃0.2 (swimming) and ≃1 (crawling), with λ ≃0.6 μm (abe2023machinelearningbasedmotion pages 4-5). This supports environmental/mechanical nodes (drag, adhesivity) in the causal graph.

---

## 6) Candidate nodes (grouped by type)

### 6.1 Trait node
- **spirochete shaped** (METPO:1000693)

### 6.2 Cellular structures / localizations
- Periplasm (GO:0042597)
- Outer membrane (GO:0019867)
- Periplasmic flagellum / endoflagellum (GO:0009288)
- Flagellar hook (GO:0009289)
- Flagellar basal body (GO:0009420)
- Divisome (label-only; can be mapped later to a GO complex term)
- Elongasome (label-only)

### 6.3 Biological processes / phenotypes
- Motility (GO:0048870)
- Cell division (GO:0051301)
- Peptidoglycan biosynthetic process (GO:0009252)
- Cell lysis (GO:0001893)
- Crawling motility on host surfaces (label-only)

### 6.4 Genes/proteins (label-only pending UniProt/NCBI Gene grounding)
- **FlgV (bb0268)** (Borrelia)
- **FlgE** (flagellar hook protein)
- **FlhE** (periplasmic filament-preventing factor; boundary-case mechanism)
- **FcpA / FcpB / FlaA2** (Leptospira sheath/curvature factors; evidence currently from abstract-like sources in this corpus)

### 6.5 Chemicals / PTMs / mechanical/environment nodes
- Lysinoalanine crosslink (Lal) (label-only; CHEBI mapping may be possible but should be verified)
- Viscous drag / viscosity (ENVO/PATO terms to be added if needed; supported mechanistically in modeling context) (abe2023machinelearningbasedmotion pages 4-5)
- Adhesion/adhesivity to host cells (process node; impacts crawling) (abe2023machinelearningbasedmotion pages 4-5, abe2023machinelearningbasedmotion pages 1-2)

---

## 7) Candidate causal edges (evidence-backed)
The table below is intended for direct translation into a TraitMech YAML edge list.

| Edge (subject–predicate–object) | Entity type(s) | Suggested grounding (CURIEs where known; otherwise label-only) | Evidence snippet (verbatim/near-verbatim) | Reference (with DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Periplasmic flagella ribbon with 7–11 overlapping flagella per pole — associated with — flat-wave cell morphology in *Borrelia burgdorferi* | cellular structure → morphology | periplasmic flagellum [GO:0009288]; *Borrelia burgdorferi* [NCBITaxon:139]; flat-wave morphology [label-only] | “*Borrelia burgdorferi* exhibits a flat-wave morphology and has seven to eleven flagella per pole that overlap in the centre” (thomasUnknownyearthedesignof pages 57-59) | Thomas, *The design of bacterial flagella: part 2—flagellar diversity across bacterial species*, unknown year, URL unavailable in retrieved metadata | Good comparative morphology statement; source metadata incomplete, so use cautiously for curation. |
| Single non-overlapping periplasmic flagellum at each pole — associated with — corkscrew morphology in *Leptospira illini* | cellular structure → morphology | periplasmic flagellum [GO:0009288]; *Leptospira illini* [label-only]; corkscrew morphology [label-only] | “*Leptospira illini* shows a corkscrew morphology with a single non-overlapping flagellum at each pole” (thomasUnknownyearthedesignof pages 57-59) | Thomas, *The design of bacterial flagella: part 2—flagellar diversity across bacterial species*, unknown year, URL unavailable in retrieved metadata | Comparative edge; useful boundary distinction versus Borrelia flat-wave form. |
| Periplasmic flagella enclosed in the periplasm — distort/push — the cell body | cellular structure → biological process/mechanics | periplasmic flagellum [GO:0009288]; periplasm [GO:0042597]; cell body distortion [label-only] | “spirochete flagella are enclosed in the periplasmic space and … the filaments distort and push the cell body by action of the flagellar motors” (lynch2023lysinoalaninecrosslinkingis pages 1-2) | Lynch et al., *PNAS Nexus*, 2023, DOI:10.1093/pnasnexus/pgad349, https://doi.org/10.1093/pnasnexus/pgad349 | Strong direct mechanistic statement linking endoflagella to body deformation. |
| Rotation of two periplasmic flagella beneath the outer membrane — drives — rolling of the spiral cell body in *Leptospira* | cellular structure/process → morphology/motility | periplasmic flagellum [GO:0009288]; outer membrane [GO:0019867]; *Leptospira* [NCBITaxon:171] | “Leptospira spp. possess two periplasmic flagella whose rotation beneath the outer membrane drives rolling of the spiral cell body” (abe2023machinelearningbasedmotion pages 1-2) | Abe et al., *Nature Communications*, 2023, DOI:10.1038/s41467-023-43366-0, https://doi.org/10.1038/s41467-023-43366-0 | Strong taxon-specific support for spiral-body rolling mechanics. |
| Periplasmic flagella — contribute to maintaining — planar-wave/spirochete morphology | cellular structure → morphology | periplasmic flagellum [GO:0009288]; planar-wave morphology [label-only] | “flagella are located in the periplasmic space between the inner and outer membrane where they contribute to maintaining the planar wave morphology of spirochetes” (thomasUnknownyearthedesignof pages 57-59) | Čorak et al., *Int J Mol Sci.*, 2023, DOI:10.3390/ijms24065594, https://doi.org/10.3390/ijms24065594 | Secondary/summary wording in retrieval output; suitable as supporting context, but direct full-text quote should be checked before final curation. |
| FlaA2 — directs localization of — FcpA/FcpB on leptospiral periplasmic flagella | protein → protein localization/assembly | FlaA2 [label-only]; FcpA [label-only]; FcpB [label-only]; periplasmic flagellum [GO:0009288] | “FlaA2 directs localization of FcpA and FcpB to generate curved PFs” (農研機構Unknownyeardp10102p1002 pages 7-8) | conference abstract metadata in retrieved corpus (農研機構Unknownyeardp10102p1002 pages 7-8) | Mechanistically valuable but source is not a standard peer-reviewed paper in retrieved metadata; mark uncertain until primary article is pinned. |
| Asymmetric FcpA localization — causes — periplasmic flagellum curvature/coiling | protein localization → morphology/mechanics | FcpA [label-only]; flagellar filament [GO:0009288 or label-only for PF filament]; curvature [PATO label-only] | “asymmetric FcpA localization produces flagellar coiling, identifying FcpA as a key coiling protein” (農研機構Unknownyeardp10102p1002 pages 7-8) | conference abstract metadata in retrieved corpus (農研機構Unknownyeardp10102p1002 pages 7-8) | Strong mechanistic wording but provisional due to source status. |
| FcpB — reinforces — periplasmic flagellum stiffness | protein → mechanical property | FcpB [label-only]; flagellar filament stiffness [label-only] | “modeling predicts reduced stiffness for FcpB-deficient filaments, implying FcpB functions as a wedge to reinforce flagellar stiffness” (農研機構Unknownyeardp10102p1002 pages 7-8) | conference abstract metadata in retrieved corpus (農研機構Unknownyeardp10102p1002 pages 7-8) | Inference from modeling and mutant phenotype; curate as uncertain/taxon-specific. |
| Coiled leptospiral flagella — are indispensable for — bending of cell ends | cellular structure → morphology | leptospiral periplasmic flagellum [label-only]; bent cell end [label-only] | “isolated Leptospira flagella ‘exhibit a coiled shape ... indispensable for bending cell ends’” (大熊盛也Unknownyearp1001dp10101 pages 13-14) | conference abstract metadata in retrieved corpus (大熊盛也Unknownyearp1001dp10101 pages 13-14) | Useful direct shape edge; verify against primary peer-reviewed source before final TraitMech commit. |
| FlgE lysinoalanine cross-link — stabilizes — the flagellar hook | post-translational modification → complex stability | FlgE [label-only]; lysinoalanine [CHEBI:73703 if accepted, otherwise label-only]; flagellar hook [GO:0009289] | “Lal is required for motility of Td, presumably due to the stabilizing effect of the crosslink” (lynch2023lysinoalaninecrosslinkingis pages 1-2) | Lynch et al., *PNAS Nexus*, 2023, DOI:10.1093/pnasnexus/pgad349, https://doi.org/10.1093/pnasnexus/pgad349 | Hook stabilization is phrased as “presumably,” so this specific stabilization edge should be marked inferred/uncertain. |
| Conserved FlgE lysinoalanine cross-link — required for — spirochete motility | post-translational modification → phenotype | FlgE [label-only]; lysinoalanine [CHEBI:73703 if accepted, otherwise label-only]; motility [GO:0048870] | “a mutant strain of the Lyme disease pathogen *Borreliella burgdorferi* unable to form the crosslink has impaired motility” and “cells incapable of forming the crosslink are non-motile” (lynch2023lysinoalaninecrosslinkingis pages 1-2) | Lynch et al., *PNAS Nexus*, 2023, DOI:10.1093/pnasnexus/pgad349, https://doi.org/10.1093/pnasnexus/pgad349 | Strong direct phenotype edge; morphology consequence is indirect via loss of functional PF mechanics. |
| FlhE — prevents — ectopic periplasmic filament assembly | protein → biological process inhibition | FlhE [label-only]; periplasmic flagellar filament assembly [label-only] | “FlhE is a periplasmic, Sec-translocated protein … that prevents ectopic assembly of flagellar filaments in the periplasm” (halte2024flhefunctionsas pages 2-3) | Halte et al., *Nature Communications*, 2024, DOI:10.1038/s41467-024-50278-0, https://doi.org/10.1038/s41467-024-50278-0 | Boundary-case control from Gram-negative bacteria, not native spirochete shaping mechanism; still informative mechanistically. |
| Ectopic periplasmic filament assembly — mislocalizes — divisome and elongasome complexes required for peptidoglycan synthesis | aberrant structure → cellular process | periplasmic filament assembly [label-only]; divisome [GO:0009274-related label-only]; elongasome [label-only]; peptidoglycan synthesis [GO:0009252] | “Loss of FlhE permits periplasmic filament assembly, which causally mis-localizes divisome and elongasome complexes required for peptidoglycan synthesis” (halte2024flhefunctionsas pages 2-3) | Halte et al., *Nature Communications*, 2024, DOI:10.1038/s41467-024-50278-0, https://doi.org/10.1038/s41467-024-50278-0 | Excellent process edge for envelope-shape coupling; boundary-case rather than canonical spirochete mechanism. |
| Mislocalized divisome/elongasome during ectopic periplasmic filament assembly — causes — altered curvature/loss of rod morphology and lysis | cellular process defect → morphology/envelope integrity | divisome/elongasome mislocalization [label-only]; cell curvature [PATO label-only]; rod morphology [METPO parent label-only]; cell lysis [GO:0001893] | “producing altered cell curvature/loss of rod morphology and infrequent cell lysis” (halte2024flhefunctionsas pages 2-3) | Halte et al., *Nature Communications*, 2024, DOI:10.1038/s41467-024-50278-0, https://doi.org/10.1038/s41467-024-50278-0 | Very useful negative-control edge showing how periplasmic filaments can reshape cells via envelope-growth machinery. |
| FlgV localized at the basal body — modulates — periplasmic flagellar filament assembly | protein/complex → assembly process | FlgV [label-only]; flagellar basal body [GO:0009420]; periplasmic flagellar filament [label-only] | “FlgV localizes to the flagellar basal body” and “the authors conclude that altering FlgV levels profoundly impacts filament assembly” (zambacampero2024broadlyconservedflgv pages 7-10) | Zamba-Campero et al., *Nature Communications*, 2024, DOI:10.1038/s41467-024-54806-w, https://doi.org/10.1038/s41467-024-54806-w | Strong recent mechanistic gene node for Borrelia PF assembly. |
| flgV deletion — decreases — flagellar filament number/length | gene perturbation → morphology of organelle | flgV [label-only]; periplasmic flagellar filament [label-only] | “Deletion of flgV … reduces the average number of flagellar filaments … relative to WT … and is rescued by complementation” (zambacampero2024broadlyconservedflgv pages 7-10) | Zamba-Campero et al., *Nature Communications*, 2024, DOI:10.1038/s41467-024-54806-w, https://doi.org/10.1038/s41467-024-54806-w | Direct quantitative assembly edge. |
| FlgV overproduction — severely reduces — filament number/length | protein abundance perturbation → organelle morphology | FlgV [label-only]; periplasmic flagellar filament [label-only] | “Overexpression of FlgV produces a more pronounced phenotype: a marked reduction in filaments” (zambacampero2024broadlyconservedflgv pages 7-10) | Zamba-Campero et al., *Nature Communications*, 2024, DOI:10.1038/s41467-024-54806-w, https://doi.org/10.1038/s41467-024-54806-w | Demonstrates dosage sensitivity; useful regulation edge. |
| Reduced/aberrant FlgV levels — cause — motility defects | protein abundance perturbation → phenotype | FlgV [label-only]; motility [GO:0048870] | “These structural defects correlate with functional phenotypes: ΔflgV formed smaller motility rings and overexpression strains showed similar motility defects” (zambacampero2024broadlyconservedflgv pages 6-7) | Zamba-Campero et al., *Nature Communications*, 2024, DOI:10.1038/s41467-024-54806-w, https://doi.org/10.1038/s41467-024-54806-w | Direct phenotype edge, strong support. |
| Reduced/aberrant FlgV levels — perturb — cell division and cell morphology | protein abundance perturbation → phenotype | FlgV [label-only]; cell division [GO:0051301]; cell morphology [GO:0008360] | “ΔflgV mutants exhibit defects in cell division and motility, including an abundance of conjoined spirochetes and visible septa” and “Overproduction of FlgV leads to cell elongation” (zambacampero2024broadlyconservedflgv pages 13-14) | Zamba-Campero et al., *Nature Communications*, 2024, DOI:10.1038/s41467-024-54806-w, https://doi.org/10.1038/s41467-024-54806-w | Strong edge linking PF assembly regulator to whole-cell shape/division. |
| Outer membrane proteins (reduced OMPs) — decrease adhesion and increase — crawling mobility on host cells | envelope component → behavior | outer membrane protein [GO:0019867-related label-only]; adhesion [GO:0007155]; crawling motility [label-only] | “mutants lacking outer membrane proteins (OMPs) tend to exhibit faster mobility and reduced adherence on cultured kidney cells” (abe2023machinelearningbasedmotion pages 1-2) | Abe et al., *Nature Communications*, 2023, DOI:10.1038/s41467-023-43366-0, https://doi.org/10.1038/s41467-023-43366-0 | Strong recent application-oriented edge, but this is motility mode rather than core shape determination. |
| Stronger adhesion to host cells — suppresses — crawling by decelerating cell rotation | environmental/host interaction → behavior/mechanics | adhesion to host cell [GO:0007155-related label-only]; crawling motility [label-only]; cell rotation [label-only] | “stronger adhesion to host cells suppresses crawling by decelerating cell rotation” (abe2023machinelearningbasedmotion pages 4-5) | Abe et al., *Nature Communications*, 2023, DOI:10.1038/s41467-023-43366-0, https://doi.org/10.1038/s41467-023-43366-0 | Behavioral/mechanical edge relevant to how spiral-body rotation couples to substrate interaction; indirect for shape curation. |


*Table: This table compiles candidate causal edges for curating the spirochete-shaped trait, emphasizing periplasmic flagella, hook and sheath components, envelope-growth coupling, and motility-associated regulators. It highlights which claims are strongly supported versus provisional or boundary-case evidence.*

---

## 8) Central visual evidence (for curation packages)
Halte et al. (2024) includes microscopy and super-resolution images showing **morphology defects** and **periplasmic filaments** when FlhE is absent, plus a model schematic of the mechanism; these are useful as a “mechanistic sanity check” that periplasmic filament formation can drive curvature via envelope-growth mislocalization (halte2024flhefunctionsas media 82922252, halte2024flhefunctionsas media bd76a29d, halte2024flhefunctionsas media df9e3f66).

---

## 9) Warnings / claims not ready for TraitMech curation
1. **Leptospira sheath/curvature claims (FcpA/FcpB/FlaA2)** are mechanistically compelling in the excerpts but appear to come from conference-abstract-like documents with incomplete bibliographic metadata in this corpus (農研機構Unknownyeardp10102p1002 pages 7-8, 大熊盛也Unknownyearp1001dp10101 pages 13-14). These should be treated as **provisional** until backed by a peer-reviewed primary article with DOI and stable quotes.
2. The “flagella contribute to maintaining planar wave morphology” statement appears in retrieval output but should be verified against full text before being used as a primary anchor edge (thomasUnknownyearthedesignof pages 57-59).
3. The comparative “flat-wave vs corkscrew” morphology linkage is valuable but originates from a document with **unknown year/journal metadata** in this corpus; use it as **supporting** context rather than the sole evidence for a high-confidence edge (thomasUnknownyearthedesignof pages 57-59).
4. Hook-crosslink → hook stabilization is described with “presumably,” so the stabilization edge should be labeled inferred, while the Lal → motility requirement is stronger (lynch2023lysinoalaninecrosslinkingis pages 1-2).

---

## 10) DOI-first bibliography (with URLs and publication dates where available)

1. Zamba-Campero M, Soliman D, Yu H, et al. **Broadly conserved FlgV controls flagellar assembly and *Borrelia burgdorferi* dissemination in mice**. *Nature Communications*. **2024-11**. DOI: **10.1038/s41467-024-54806-w**. URL: https://doi.org/10.1038/s41467-024-54806-w (zambacampero2024broadlyconservedflgv pages 1-2, zambacampero2024broadlyconservedflgv pages 7-10)
2. Halte M, Andrianova EP, Goosmann C, et al. **FlhE functions as a chaperone to prevent formation of periplasmic flagella in Gram-negative bacteria**. *Nature Communications*. **2024-07**. DOI: **10.1038/s41467-024-50278-0**. URL: https://doi.org/10.1038/s41467-024-50278-0 (halte2024flhefunctionsas pages 2-3, halte2024flhefunctionsas media 82922252)
3. Nakamura S, Minamino T. **Structure and Dynamics of the Bacterial Flagellar Motor Complex**. *Biomolecules*. **2024-11**. DOI: **10.3390/biom14121488**. URL: https://doi.org/10.3390/biom14121488 (nakamura2024structureanddynamics pages 17-18)
4. Abe K, Koizumi N, Nakamura S. **Machine learning-based motion tracking reveals an inverse correlation between adhesivity and surface motility of the leptospirosis spirochete**. *Nature Communications*. **2023-12**. DOI: **10.1038/s41467-023-43366-0**. URL: https://doi.org/10.1038/s41467-023-43366-0 (abe2023machinelearningbasedmotion pages 1-2, abe2023machinelearningbasedmotion pages 4-5)
5. Lynch MJ, Deshpande M, Kurniyati K, et al. **Lysinoalanine cross-linking is a conserved post-translational modification in the spirochete flagellar hook**. *PNAS Nexus*. **2023-10**. DOI: **10.1093/pnasnexus/pgad349**. URL: https://doi.org/10.1093/pnasnexus/pgad349 (lynch2023lysinoalaninecrosslinkingis pages 1-2)

---

## 11) Minimal YAML-curation guidance (what to commit now vs later)
**High-confidence nodes/edges to curate now:**
- Periplasmic flagella in periplasm drive distortion/pushing of cell body; two PF rotation drives rolling of spiral body (lynch2023lysinoalaninecrosslinkingis pages 1-2, abe2023machinelearningbasedmotion pages 1-2).
- FlgV dosage affects filament number/assembly and impacts division/morphology (zambacampero2024broadlyconservedflgv pages 7-10, zambacampero2024broadlyconservedflgv pages 13-14).
- FlgE Lal crosslink required for motility (lynch2023lysinoalaninecrosslinkingis pages 1-2).

**Hold for later (needs better primary sources in this corpus):**
- FcpA/FcpB/FlaA2 edges (農研機構Unknownyeardp10102p1002 pages 7-8, 大熊盛也Unknownyearp1001dp10101 pages 13-14).
- Flat-wave vs corkscrew comparative edges if relying solely on incomplete-metadata document (thomasUnknownyearthedesignof pages 57-59).


References

1. (lynch2023lysinoalaninecrosslinkingis pages 1-2): Michael J Lynch, Maithili Deshpande, Kurni Kurniyati, Kai Zhang, Milinda James, Michael Miller, Sheng Zhang, Felipe J Passalia, Elsio A Wunder, Nyles W Charon, Chunhao Li, and Brian R Crane. Lysinoalanine cross-linking is a conserved post-translational modification in the spirochete flagellar hook. PNAS Nexus, Oct 2023. URL: https://doi.org/10.1093/pnasnexus/pgad349, doi:10.1093/pnasnexus/pgad349. This article has 4 citations and is from a peer-reviewed journal.

2. (thomasUnknownyearthedesignof pages 57-59): D Thomas. The design of bacterial flagella: part 2—flagellar diversity across bacterial species. Unknown journal, Unknown year.

3. (abe2023machinelearningbasedmotion pages 1-2): Keigo Abe, Nobuo Koizumi, and Shuichi Nakamura. Machine learning-based motion tracking reveals an inverse correlation between adhesivity and surface motility of the leptospirosis spirochete. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43366-0, doi:10.1038/s41467-023-43366-0. This article has 11 citations and is from a highest quality peer-reviewed journal.

4. (農研機構Unknownyeardp10102p1002 pages 7-8): 馬田貴史， 梅田麻美， 児玉彬， 高松大輔， 農研機構. Dp1-01-02/p1-002. Unknown journal, Unknown year.

5. (nakamura2024structureanddynamics pages 17-18): Shuichi Nakamura and Tohru Minamino. Structure and dynamics of the bacterial flagellar motor complex. Biomolecules, 14:1488, Nov 2024. URL: https://doi.org/10.3390/biom14121488, doi:10.3390/biom14121488. This article has 26 citations.

6. (halte2024flhefunctionsas pages 2-3): Manuel Halte, Ekaterina P. Andrianova, Christian Goosmann, Fabienne F. V. Chevance, Kelly T. Hughes, Igor B. Zhulin, and Marc Erhardt. Flhe functions as a chaperone to prevent formation of periplasmic flagella in gram-negative bacteria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50278-0, doi:10.1038/s41467-024-50278-0. This article has 9 citations and is from a highest quality peer-reviewed journal.

7. (zambacampero2024broadlyconservedflgv pages 1-2): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

8. (zambacampero2024broadlyconservedflgv pages 7-10): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

9. (zambacampero2024broadlyconservedflgv pages 4-6): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

10. (zambacampero2024broadlyconservedflgv pages 13-14): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

11. (abe2023machinelearningbasedmotion pages 4-5): Keigo Abe, Nobuo Koizumi, and Shuichi Nakamura. Machine learning-based motion tracking reveals an inverse correlation between adhesivity and surface motility of the leptospirosis spirochete. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43366-0, doi:10.1038/s41467-023-43366-0. This article has 11 citations and is from a highest quality peer-reviewed journal.

12. (zambacampero2024broadlyconservedflgv pages 14-15): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

13. (大熊盛也Unknownyearp1001dp10101 pages 13-14): 坂本光央， 久富敦， 大熊盛也. P1-001/dp1-01-01. Unknown journal, Unknown year.

14. (zambacampero2024broadlyconservedflgv pages 6-7): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

15. (halte2024flhefunctionsas media 82922252): Manuel Halte, Ekaterina P. Andrianova, Christian Goosmann, Fabienne F. V. Chevance, Kelly T. Hughes, Igor B. Zhulin, and Marc Erhardt. Flhe functions as a chaperone to prevent formation of periplasmic flagella in gram-negative bacteria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50278-0, doi:10.1038/s41467-024-50278-0. This article has 9 citations and is from a highest quality peer-reviewed journal.

16. (halte2024flhefunctionsas media bd76a29d): Manuel Halte, Ekaterina P. Andrianova, Christian Goosmann, Fabienne F. V. Chevance, Kelly T. Hughes, Igor B. Zhulin, and Marc Erhardt. Flhe functions as a chaperone to prevent formation of periplasmic flagella in gram-negative bacteria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50278-0, doi:10.1038/s41467-024-50278-0. This article has 9 citations and is from a highest quality peer-reviewed journal.

17. (halte2024flhefunctionsas media df9e3f66): Manuel Halte, Ekaterina P. Andrianova, Christian Goosmann, Fabienne F. V. Chevance, Kelly T. Hughes, Igor B. Zhulin, and Marc Erhardt. Flhe functions as a chaperone to prevent formation of periplasmic flagella in gram-negative bacteria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50278-0, doi:10.1038/s41467-024-50278-0. This article has 9 citations and is from a highest quality peer-reviewed journal.