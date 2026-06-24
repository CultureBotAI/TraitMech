---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:13:18.138697'
end_time: '2026-06-18T08:29:57.410943'
duration_seconds: 999.27
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: helical shaped
  trait_identifier: METPO:1000676
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: helical_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a corkscrew-like helical cell
    body with curvature and twist along its long axis.
  parent_traits: METPO:1000666
  synonyms: helical-shaped
  evidence_summary: 'DOI:10.1016/j.cell.2010.03.046: coordinated action of multiple
    proteins relaxes peptidoglycan crosslinking (Supports a mechanistic basis for
    helical bacterial cell curvature and twist in Helicobacter pylori.)'
  causal_graph_summary: 'helical_shaped_pg_relaxation: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** helical shaped
- **METPO identifier:** METPO:1000676
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a corkscrew-like helical cell body with curvature and twist along its long axis.
- **Parent traits:** METPO:1000666
- **Synonyms:** helical-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2010.03.046: coordinated action of multiple proteins relaxes peptidoglycan crosslinking (Supports a mechanistic basis for helical bacterial cell curvature and twist in Helicobacter pylori.)
- **Existing causal graph summary:** helical_shaped_pg_relaxation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **helical shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/helical_shaped.yaml`.

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
- **Trait label:** helical shaped
- **METPO identifier:** METPO:1000676
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a corkscrew-like helical cell body with curvature and twist along its long axis.
- **Parent traits:** METPO:1000666
- **Synonyms:** helical-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2010.03.046: coordinated action of multiple proteins relaxes peptidoglycan crosslinking (Supports a mechanistic basis for helical bacterial cell curvature and twist in Helicobacter pylori.)
- **Existing causal graph summary:** helical_shaped_pg_relaxation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **helical shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/helical_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **helical shaped** (METPO:1000676)

### Executive scope summary
The trait **helical shaped** (METPO:1000676) refers to bacterial cells whose morphology includes **both curvature and twist** along the long axis, yielding a corkscrew-like body with a characteristic **helical pitch**; it can be conceptualized as the sum of **elongation + curvature + twist**. In well-studied helical pathogens such as *Helicobacter pylori*, genetic perturbations that disrupt the helical program frequently convert cells to **curved rods (vibrioid)**—i.e., curvature without a stable twist—implicating a specific morphogenetic program beyond general curvature. Mechanistically, the best-supported causal substrate for helicity in *H. pylori* and *Campylobacter jejuni* is **peptidoglycan (PG) architecture**, especially peptide crosslinking and peptide-stem trimming, which is encoded in the PG sacculus and persists in isolated sacculi. (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)

**Boundary cases / near traits to distinguish**
- **Curved rod (vibrioid)**: curvature without helical twist; commonly observed in *H. pylori* csd or ccmA mutants (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation media fa339022).
- **Spirochetes / Spiroplasma**: helicity may depend on periplasmic flagella (spirochetes) or a wall-less cytoskeletal ribbon (Spiroplasma), representing different mechanisms than PG remodeling (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2).
- **Stress/age-related pleomorphy** (e.g., filamented helical rods, coccoid forms): may reflect conditional morphology rather than the constitutive “helical shaped” trait; *C. jejuni* can adopt filamented helical rod and coccoid forms under stress (frirdich2023multiplecampylobacterjejuni pages 1-2).

### Current understanding: key mechanistic concepts (definition-level)
1. **PG sacculus as the shape-encoding structure**: PG is a meshwork of glycan strands joined by peptide crosslinks; it is required to maintain bacterial shape and isolated sacculi retain cell morphology (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2).
2. **Helical shape as PG crosslink “relaxation/remodeling”**: In *H. pylori*, multiple proteins act coordinately to **relax PG crosslinking**, enabling curvature and twist (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2).
3. **Two-pathway model (review synthesis)**: Expert review describes a *H. pylori* “shapesome” including multiple PG hydrolases (endopeptidases and carboxypeptidases) plus scaffolds/cytoskeletal elements that together create **spatially organized asymmetric cell-wall growth** required for a regular helix (salama2020cellmorphologyas pages 1-2).

### Recent developments (priority 2023–2024)
#### 2023: Expanded *Campylobacter jejuni* morphogenesis gene set and dose effects
Frirdich et al. (2023) identified additional *C. jejuni* gene products implicated in helical curvature control beyond the canonical PG hydrolases Pgp1/Pgp2, including a **putative bactofilin (1104)** and **M23 peptidase-domain proteins (0166, 1105, 1228)**. Deletions yielded varying curved-rod phenotypes with altered muropeptide profiles; overexpression of 1104/1105 also altered morphology and muropeptides, consistent with **dose-dependent control** of PG architecture and curvature. (Publication date: 18 Apr 2023; https://doi.org/10.3389/fmicb.2023.1162806) (frirdich2023multiplecampylobacterjejuni pages 1-2)

#### 2024: Conserved bactofilin–M23 module as a curvature control principle
Pöhl et al. (2024; eLife; https://doi.org/10.7554/eLife.86577.2) provide mechanistic support for a conserved module where **bactofilin polymers** cooperate with an **M23-family peptidoglycan endopeptidase** (LmdC) to shape morphologically complex bacteria. In *Hyphomonas neptunium*, bacA is adjacent to lmdC (overlapping by 17 bp), and loss of BacA causes severe morphogenesis defects; LmdC’s M23 domain retains Zn2+-binding residues and shows **DD-endopeptidase activity** in vitro by HPLC muropeptide profiling. While not directly in *Helicobacter*/*Campylobacter*, this work strengthens the plausibility of bactofilin–M23 modules (e.g., CcmA with M23 peptidases) as a general mechanism for curvature/helicity programs and provides curatable mechanistic nodes/edges as comparative evidence. (Jan 2024; https://doi.org/10.7554/eLife.86577.2) (pohl2024adynamicbactofilin pages 3-4, pohl2024adynamicbactofilin pages 12-13)

### Current applications / real-world implementations
1. **Virulence and colonization biology (anti-virulence rationale)**
   - *H. pylori*: the csd/ccmA-dependent shape pathway is required for robust stomach colonization even when directional motility is normal, supporting a role for helical shape (or a tightly linked PG property) in mucosal colonization (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10).
   - *C. jejuni*: PG remodeling genes affecting helical shape also affect host colonization and inflammatory signaling (see quantitative data below), supporting morphology and PG composition as actionable phenotypes for pathogenesis research and potentially anti-virulence strategies (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2, frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7).
2. **Quantitative morphology phenotyping pipelines**
   - *H. pylori* work quantified cell curvature and pitch by algorithmic extraction of a central axis and curvature from polygonal outlines, enabling higher-throughput genotype–phenotype mapping for shape programs (sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5).
3. **Biochemical assays and structural biology for PG hydrolases**
   - Pöhl et al. use HPLC muropeptide profiles to assign M23 enzyme activity (DD-endopeptidase) for LmdC, demonstrating a reusable assay strategy for assigning catalytic directionality to putative shape enzymes (pohl2024adynamicbactofilin pages 12-13).

### Expert opinions and authoritative analysis
- Salama (2020) frames helical morphology as a **virulence determinant** and emphasizes that *H. pylori*’s “shapesome” includes **PG modification enzymes, precursor synthesis enzymes, a cytoskeletal element, and scaffolds/regulators** that drive enhanced asymmetric wall growth; this perspective supports representing helical shape as an emergent property of a multi-component network rather than a single enzyme. (Apr 2020; https://doi.org/10.1016/j.mib.2019.12.002) (salama2020cellmorphologyas pages 1-2)
- Sycuro et al. (2010) highlight that the **coordinated action of multiple proteins** relaxes PG crosslinking, enabling curvature and twist, and that isolated sacculi retain altered shapes, supporting a PG-centric causal graph. (28 May 2010; https://doi.org/10.1016/j.cell.2010.03.046) (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2)

### Relevant statistics and quantitative data (recent and classical anchors)
- *H. pylori* csd mutants show quantifiable PG crosslink changes: csd/ccmA mutants exhibit a **20–50% increase in tetrapentapeptide crosslinking**; the csd3 mutant additionally shows **~30% decreases** in tetratetrapeptide and tetratripeptide crosslinking (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10).
- *C. jejuni* pgp1 deletion has a strong in vivo effect: a **2.9-log decrease** in average chick colonization compared to wild type (p = 0.0009) (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7).
- Pöhl et al. quantify morphological abnormality proportions in bac mutants with **n = 100 cells per strain** for key phenotyping (pohl2024adynamicbactofilin pages 3-4).

### Trait scope (curation guidance)
- **Trait represents**: a stable, genetically encoded cell-body morphology with corkscrew-like curvature+twist, typically measured by microscopy (phase-contrast, DIC, TEM) and/or computational morphology metrics (sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5, sycuro2010peptidoglycancrosslinkingrelaxation media fa339022).
- **Exclude / flag as conditional**: stress-induced filamentation or coccoid transition in *C. jejuni*; *H. pylori* “shape-shifting” states may be environmental/physiological rather than constitutive; curate as separate traits if needed (frirdich2023multiplecampylobacterjejuni pages 1-2).

---

## Candidate causal graph nodes (grouped by type)

### A) Phenotype node
- **Helical shaped** — METPO:1000676 (given)

### B) Core cellular structures & processes
- **Peptidoglycan sacculus / peptidoglycan crosslinking** — label-only (PG is described as glycan strands crosslinked by peptide bridges) (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2)
- **PG muropeptide profile** — label-only (HPLC profiles used to assess tripeptide/dipeptide and crosslinked dimers) (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7, pohl2024adynamicbactofilin pages 12-13)
- **Asymmetric cell wall growth / localized PG hydrolysis and synthesis** — label-only (review framing for helical morphogenesis) (salama2020cellmorphologyas pages 1-2)

Suggested GO candidates (if used in curation; verify exact GO term mapping):
- GO:0009252 (peptidoglycan biosynthetic process) — candidate for pathway node

### C) Genes/proteins (mechanistic entities)
#### *Helicobacter pylori* shape program (direct helical evidence)
- **csd1–csd3** (LytM/M23 peptidase homologs) — label-only (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2)
- **ccmA** (bactofilin homolog) — label-only (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2)

Additional *H. pylori* shapesome components (review-level support)
- **Csd2** (heterodimerizes/stabilizes Csd1; lacks key catalytic residues) — label-only (salama2020cellmorphologyas pages 1-2)
- **Csd4** (M14 D,L-carboxypeptidase; tripeptide→dipeptide) — label-only (salama2020cellmorphologyas pages 1-2)
- **Csd5** (single-pass inner membrane scaffold) — label-only (salama2020cellmorphologyas pages 1-2)

#### *Campylobacter jejuni* (direct helical evidence)
- **pgp1 (Pgp1)** — novel PG DL-carboxypeptidase; helical-shape determinant (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2, frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7)
- **pgp2 (Pgp2)** — referenced as a helical-shape PG hydrolase in 2023 study (mechanistic details not in excerpt) (frirdich2023multiplecampylobacterjejuni pages 1-2)

2023 candidate factors affecting degree of helical curvature
- **1104** (putative bactofilin) — label-only (frirdich2023multiplecampylobacterjejuni pages 1-2)
- **0166, 1105, 1228** (M23 peptidase-domain proteins) — label-only (frirdich2023multiplecampylobacterjejuni pages 1-2)

#### Comparative 2024 curvature module (cross-taxon; supports general mechanism)
- **bacA/bacD** (bactofilins) — label-only (pohl2024adynamicbactofilin pages 3-4)
- **lmdC** (M23 peptidase; DD-endopeptidase activity) — label-only (pohl2024adynamicbactofilin pages 12-13)

### D) Chemicals / cofactors
- **ZnCl2 / Zn2+** — required for metal-dependent PG peptidase activity in Pgp1 assays; and Zn2+-binding residues in M23 peptidases like LmdC (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7, pohl2024adynamicbactofilin pages 12-13)
- **EDTA** — chelator used to eliminate metal-dependent activity (assay factor) (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7)

### E) Environmental / experimental factors
- **Mouse stomach colonization model** (host environment) (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)
- **Chick colonization model** (host environment) (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7)
- **Soft agar motility assays** (assay factor) (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)
- **HPLC muropeptide profiling** (assay factor) (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7, pohl2024adynamicbactofilin pages 12-13)

---

## Candidate causal edges (curation-ready)
The following table lists evidence-backed edges with snippets, references, and uncertainty notes.

| Edge (subject–predicate–object) | Taxon/Context | Suggested grounding (CURIEs where possible; otherwise label) | Evidence snippet (short quote) | Reference (DOI, publication year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| csd1 activity → relaxes peptidoglycan crosslinking → helical cell shape | *Helicobacter pylori* G27 morphology pathway | csd1 gene/protein [label]; GO:0009252 peptidoglycan biosynthetic process; METPO:1000676 helical shaped | “four genes required for helical shape… three LytM peptidoglycan endopeptidase homologs (csd1–3)… mutants lacking any single csd gene… formed curved rods and showed increased peptidoglycan crosslinking” (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2) | DOI:10.1016/j.cell.2010.03.046 (2010) https://doi.org/10.1016/j.cell.2010.03.046 | Strong but gene-specific biochemical activity for Csd1 is elaborated more fully in review summaries; direct causality to helical shape is solid, exact reaction localization remains unresolved. |
| csd2 loss → increased PG crosslinking → curved-rod/nonhelical morphology | *H. pylori* | csd2 [label]; peptidoglycan crosslinking [label]; curved rod morphology [label] | “mutants lacking any single csd gene or ccmA formed curved rods and showed increased peptidoglycan crosslinking” (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2) | DOI:10.1016/j.cell.2010.03.046 (2010) https://doi.org/10.1016/j.cell.2010.03.046 | Strong phenotype link; Csd2 may be regulatory/accessory rather than catalytic. Taxon-specific. |
| csd3 loss → altered PG crosslink profile → loss of helical pitch/abnormal curvature | *H. pylori* | csd3 [label]; tetrapeptide crosslinks [label]; METPO:1000676 | “csd3 mutant was unique in that it showed 30% decreases in tetratetrapeptide and tetratripeptide crosslinking in addition to the 20%–50% increase in tetrapentapeptide crosslinking” (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10) | DOI:10.1016/j.cell.2010.03.046 (2010) https://doi.org/10.1016/j.cell.2010.03.046 | Strong quantitative support. Mutant is highly curved/coiled, so edge is to abnormal noncanonical morphology rather than simply rod shape. |
| ccmA loss → increased tetrapentapeptide crosslinks → curved-rod morphology | *H. pylori* | ccmA bactofilin [label]; tetrapentapeptide crosslinked dimer [label]; METPO:1000676 | “four genes (csd1–3 and ccmA)… all four proteins influence peptide crosslinking within the peptidoglycan sacculus” (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10) | DOI:10.1016/j.cell.2010.03.046 (2010) https://doi.org/10.1016/j.cell.2010.03.046 | Strong phenotype association; mechanism likely via spatial organization/scaffolding, not direct hydrolysis. |
| increased tetrapentapeptide crosslinking → opposes helical curvature/twist → curved-rod morphology | *H. pylori* PG sacculus | tetrapentapeptide crosslinked dimer [label]; METPO:1000676 | “formed curved rods and showed increased peptidoglycan crosslinking” and “20%–50% increase in tetrapentapeptide crosslinking evident in all of the mutants” (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10) | DOI:10.1016/j.cell.2010.03.046 (2010) https://doi.org/10.1016/j.cell.2010.03.046 | Strong central TraitMech edge. Good candidate for a high-level pathway node. |
| localized PG crosslink hydrolysis/relaxation → generates curvature and twist → helical shape | *H. pylori* mechanistic model | peptidoglycan crosslink hydrolysis [label]; METPO:1000676 | “coordinated action of multiple proteins relaxes peptidoglycan crosslinking, enabling helical cell curvature and twist” (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2) | DOI:10.1016/j.cell.2010.03.046 (2010) https://doi.org/10.1016/j.cell.2010.03.046 | Mechanistic model strongly supported by genetics + muropeptides, but spatial localization pattern is inferred rather than directly visualized. |
| loss of helical shape (csd/ccmA mutants) → reduces stomach colonization | *H. pylori* mouse infection | METPO:1000676; stomach colonization [label]; ENVO:00001639 stomach | “This pathway is required for robust colonization of the stomach” and “three cell shape mutants were each attenuated for stomach colonization” (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10) | DOI:10.1016/j.cell.2010.03.046 (2010) https://doi.org/10.1016/j.cell.2010.03.046 | Strong phenotype edge, but could reflect shape and/or other PG-related property. Mark as phenotype consequence, not morphogenesis mechanism. |
| Pgp1 DL-carboxypeptidase activity → converts monomeric tripeptides to dipeptides → supports helical shape | *Campylobacter jejuni* 81-176 | pgp1 [label]; DL-carboxypeptidase [label]; monomeric tripeptide [label]; dipeptide [label]; METPO:1000676 | “Pgp1 as a novel peptidoglycan DL-carboxypeptidase cleaving monomeric tripeptides to dipeptides” (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2, frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7) | DOI:10.1371/journal.ppat.1002602 (2012) https://doi.org/10.1371/journal.ppat.1002602 | Strong biochemical and genetic support. Excellent direct edge for curation. |
| pgp1 deletion → rod-shaped morphology → loss of helical shape | *C. jejuni* 81-176 | pgp1 [label]; rod-shaped morphology [label]; METPO:1000676 | “Deletion of pgp1 resulted in a striking, rod-shaped morphology” (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | DOI:10.1371/journal.ppat.1002602 (2012) https://doi.org/10.1371/journal.ppat.1002602 | Strong direct phenotype edge. |
| pgp1 deletion → ~2.9-log lower chick colonization → impaired host colonization | *C. jejuni* chick model | pgp1 [label]; colonization [label]; NCBITaxon:197 chick not applicable/label | “Dpgp1 mutant exhibited a statistically significant… 2.9-log decrease in average levels of colonization” (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7) | DOI:10.1371/journal.ppat.1002602 (2012) https://doi.org/10.1371/journal.ppat.1002602 | Strong consequence edge, but connects gene/shape to fitness rather than shape-generation itself. |
| pgp1 overexpression → straight or kinked cells → reduced motility and biofilm formation | *C. jejuni* | pgp1 [label]; motility [GO:0048870]; biofilm formation [GO:0042710] | “pgp1 overexpressing strain – which similarly produced straight or kinked cells – exhibited biofilm and motility defects” (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | DOI:10.1371/journal.ppat.1002602 (2012) https://doi.org/10.1371/journal.ppat.1002602 | Useful phenotype edge; overexpression is assay-specific and may reflect dosage imbalance. |
| C. jejuni 1104 (putative bactofilin) deletion → curved-rod morphology → altered degree of helical curvature | *C. jejuni* 2023 candidate shape factor | 1104 [label]; bactofilin [label]; curved rod morphology [label] | “the putative bactofilin 1104… Deletions in the corresponding genes resulted in varying curved rod morphologies” (frirdich2023multiplecampylobacterjejuni pages 1-2) | DOI:10.3389/fmicb.2023.1162806 (2023) https://doi.org/10.3389/fmicb.2023.1162806 | Moderate support; grounding unresolved; effect size not specified in excerpt. |
| C. jejuni 1105 (M23-domain protein) deletion → curved-rod morphology and altered muropeptides | *C. jejuni* 2023 candidate shape factor | 1105 [label]; M23 peptidase domain protein [label]; muropeptide profile [label] | “the M23 peptidase domain-containing proteins 0166, 1105, and 1228… Deletions… resulted in varying curved rod morphologies with changes in their PG muropeptide profiles” (frirdich2023multiplecampylobacterjejuni pages 1-2) | DOI:10.3389/fmicb.2023.1162806 (2023) https://doi.org/10.3389/fmicb.2023.1162806 | Moderate support; biochemical activity not directly shown in excerpt. |
| C. jejuni 1228 deletion → curved-rod morphology and altered muropeptides | *C. jejuni* 2023 candidate shape factor | 1228 [label]; M23 peptidase domain protein [label] | “0166, 1105, and 1228… Deletions… resulted in varying curved rod morphologies with changes in their PG muropeptide profiles” (frirdich2023multiplecampylobacterjejuni pages 1-2) | DOI:10.3389/fmicb.2023.1162806 (2023) https://doi.org/10.3389/fmicb.2023.1162806 | Moderate support; exact reaction and directionality not specified. |
| C. jejuni 0166 deletion → curved-rod morphology and altered muropeptides | *C. jejuni* 2023 candidate shape factor | 0166 [label]; M23 peptidase domain protein [label] | “0166, 1105, and 1228… Deletions… resulted in varying curved rod morphologies with changes in their PG muropeptide profiles” (frirdich2023multiplecampylobacterjejuni pages 1-2) | DOI:10.3389/fmicb.2023.1162806 (2023) https://doi.org/10.3389/fmicb.2023.1162806 | Moderate support; direct enzymatic role remains uncertain. |
| overexpression of 1104 or 1105 → changes morphology/muropeptide profile → dose-sensitive shape control | *C. jejuni* 2023 candidate shape factors | 1104 [label]; 1105 [label]; muropeptide profile [label] | “Overexpression of 1104 and 1105 also resulted in changes in the morphology and in the muropeptide profiles, suggesting that the dose of these two gene products influences these characteristics” (frirdich2023multiplecampylobacterjejuni pages 1-2) | DOI:10.3389/fmicb.2023.1162806 (2023) https://doi.org/10.3389/fmicb.2023.1162806 | Moderate support; dosage effects can be pleiotropic, so curate cautiously. |
| bacA bactofilin → localizes/acts with lmdC M23 peptidase → controls local cell-wall growth and curvature | *Hyphomonas neptunium* / generalizable bactofilin–M23 module | bacA [label]; lmdC [label]; M23 peptidase [label]; bactofilin [label] | “bacA forms a putative bicistronic operon with lmdC” and “interaction between bactofilins and M23 peptidases… important for the control of cell growth” (pohl2024adynamicbactofilin pages 3-4, pohl2024adynamicbactofilin pages 12-13) | DOI:10.7554/eLife.86577.2 (2024) https://doi.org/10.7554/eLife.86577.2 | Strong for a conserved curvature module, but not directly shown in *Helicobacter*/*Campylobacter*. Mark as comparative/inferred for TraitMech. |
| LmdC DD-endopeptidase activity → peptidoglycan hydrolysis → modulation of cell curvature | *H. neptunium* / comparative morphology | lmdC [label]; DD-endopeptidase [label]; peptidoglycan hydrolase activity [GO:0009253-like label] | “LmdC is a peptidoglycan hydrolase with DD-endopeptidase activity” (pohl2024adynamicbactofilin pages 12-13) | DOI:10.7554/eLife.86577.2 (2024) https://doi.org/10.7554/eLife.86577.2 | Strong biochemical support in another taxon; useful comparative module, but indirect for METPO helical-shaped class. |
| bactofilin–M23 module localization → localized changes in PG biosynthesis → curvature modulation | *Rhodospirillum rubrum* / comparative spiral bacterium | bactofilin [label]; M23 peptidase [label]; peptidoglycan biosynthesis [GO:0009252] | “bactofilin and LmdC homologs co-localize at the inner curve… modulating the degree of cell curvature” (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 21-22) | DOI:10.7554/eLife.86577.2 (2024) https://doi.org/10.7554/eLife.86577.2 | Comparative evidence for a broader morphogenesis principle; taxon transfer to Helicobacter/Campylobacter should be flagged uncertain. |


*Table: This table compiles candidate subject–predicate–object edges for curating a TraitMech causal graph of the microbial trait 'helical shaped'. It emphasizes direct genetic and peptidoglycan-remodeling evidence from Helicobacter and Campylobacter, plus carefully flagged comparative module evidence from 2024 bactofilin–M23 studies.*

### Visual evidence (morphology phenotypes)
Sycuro et al. (2010) provide microscopy panels comparing wild-type helical *H. pylori* to csd/ccmA mutant curved-rod and highly curved/coiled morphologies, supporting the phenotype definition and key gene→shape edges (sycuro2010peptidoglycancrosslinkingrelaxation media fa339022, sycuro2010peptidoglycancrosslinkingrelaxation media 18376c7b).

---

## Curation warnings / “do not yet curate” notes
1. **Spatial localization model is partly inferred**: The hypothesis that localized crosslink hydrolysis on specific axes generates curvature and twist is mechanistically plausible and consistent with muropeptide changes, but the spatial distribution of enzymatic activities is not directly established in the provided evidence; curate as a model edge with uncertainty if included (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10).
2. **Cross-taxon transfer requires caution**: The 2024 bactofilin–M23 module is strong evidence for a conserved curvature mechanism, but direct equivalence to *H. pylori* CcmA + Csd M23 proteins is inferential in this context; curate as comparative support or “candidate conserved module,” not as a confirmed *H. pylori* edge (pohl2024adynamicbactofilin pages 3-4, pohl2024adynamicbactofilin pages 12-13).
3. **Dose/overexpression effects may be pleiotropic**: Overexpression phenotypes (pgp1; 1104/1105) are informative but may not reflect physiological mechanisms; mark as assay-conditional and consider using them primarily to support directionality (too much/too little activity disrupts helicity) (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2, frirdich2023multiplecampylobacterjejuni pages 1-2).
4. **Shape vs PG property confounding**: Colonization defects in helical-shape mutants may be mediated by shape itself, altered PG chemistry, or immune recognition; represent downstream edges as phenotype consequences with uncertainty (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10, frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7).

---

## DOI-first bibliography (with URLs and publication dates where available)
1. Sycuro LK, Pincus Z, Gutierrez KD, et al. **Peptidoglycan Crosslinking Relaxation Promotes *Helicobacter pylori*’s Helical Shape and Stomach Colonization.** *Cell.* **28 May 2010.** DOI:10.1016/j.cell.2010.03.046. URL: https://doi.org/10.1016/j.cell.2010.03.046 (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)
2. Frirdich E, Biboy J, Adams C, et al. **Peptidoglycan-Modifying Enzyme Pgp1 Is Required for Helical Cell Shape and Pathogenicity Traits in *Campylobacter jejuni*.** *PLoS Pathogens.* **22 Mar 2012.** DOI:10.1371/journal.ppat.1002602. URL: https://doi.org/10.1371/journal.ppat.1002602 (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2, frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7)
3. Frirdich E, Vermeulen J, Biboy J, Vollmer W, Gaynor EC. **Multiple *Campylobacter jejuni* proteins affecting the peptidoglycan structure and the degree of helical cell curvature.** *Frontiers in Microbiology.* **18 Apr 2023.** DOI:10.3389/fmicb.2023.1162806. URL: https://doi.org/10.3389/fmicb.2023.1162806 (frirdich2023multiplecampylobacterjejuni pages 1-2)
4. Pöhl S, Osorio-Valeriano M, Cserti E, et al. **A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis.** *eLife* (versioned preprint / eLife). **Jan 2024.** DOI:10.7554/eLife.86577.2. URL: https://doi.org/10.7554/eLife.86577.2 (pohl2024adynamicbactofilin pages 3-4, pohl2024adynamicbactofilin pages 12-13)
5. Salama NR. **Cell morphology as a virulence determinant: lessons from *Helicobacter pylori*.** *Current Opinion in Microbiology.* **Apr 2020.** DOI:10.1016/j.mib.2019.12.002. URL: https://doi.org/10.1016/j.mib.2019.12.002 (salama2020cellmorphologyas pages 1-2)

---

## Notes for `data/traits/morphology/helical_shaped.yaml`
- A practical TraitMech causal graph for **helical shaped** should prioritize PG-centric nodes (crosslinking, muropeptide composition) and genetically supported hydrolases/scaffolds (csd1–3, ccmA; pgp1; candidate M23/bactofilin factors) with explicit taxon scoping and uncertainty flags for inferred spatial models and cross-taxon modules. (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2, frirdich2023multiplecampylobacterjejuni pages 1-2)

References

1. (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 360 citations and is from a highest quality peer-reviewed journal.

2. (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 360 citations and is from a highest quality peer-reviewed journal.

3. (sycuro2010peptidoglycancrosslinkingrelaxation media fa339022): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 360 citations and is from a highest quality peer-reviewed journal.

4. (frirdich2023multiplecampylobacterjejuni pages 1-2): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 10 citations and is from a peer-reviewed journal.

5. (salama2020cellmorphologyas pages 1-2): Nina R Salama. Cell morphology as a virulence determinant: lessons from helicobacter pylori. Apr 2020. URL: https://doi.org/10.1016/j.mib.2019.12.002, doi:10.1016/j.mib.2019.12.002. This article has 45 citations and is from a peer-reviewed journal.

6. (pohl2024adynamicbactofilin pages 3-4): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

7. (pohl2024adynamicbactofilin pages 12-13): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

8. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2): Emilisa Frirdich, Jacob Biboy, Calvin Adams, Jooeun Lee, Jeremy Ellermeier, Lindsay Davis Gielda, Victor J. DiRita, Stephen E. Girardin, Waldemar Vollmer, and Erin C. Gaynor. Peptidoglycan-modifying enzyme pgp1 is required for helical cell shape and pathogenicity traits in campylobacter jejuni. PLoS Pathogens, 8:e1002602, Mar 2012. URL: https://doi.org/10.1371/journal.ppat.1002602, doi:10.1371/journal.ppat.1002602. This article has 140 citations and is from a highest quality peer-reviewed journal.

9. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 4-7): Emilisa Frirdich, Jacob Biboy, Calvin Adams, Jooeun Lee, Jeremy Ellermeier, Lindsay Davis Gielda, Victor J. DiRita, Stephen E. Girardin, Waldemar Vollmer, and Erin C. Gaynor. Peptidoglycan-modifying enzyme pgp1 is required for helical cell shape and pathogenicity traits in campylobacter jejuni. PLoS Pathogens, 8:e1002602, Mar 2012. URL: https://doi.org/10.1371/journal.ppat.1002602, doi:10.1371/journal.ppat.1002602. This article has 140 citations and is from a highest quality peer-reviewed journal.

10. (sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 360 citations and is from a highest quality peer-reviewed journal.

11. (pohl2024adynamicbactofilin pages 1-2): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

12. (pohl2024adynamicbactofilin pages 21-22): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

13. (sycuro2010peptidoglycancrosslinkingrelaxation media 18376c7b): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 360 citations and is from a highest quality peer-reviewed journal.