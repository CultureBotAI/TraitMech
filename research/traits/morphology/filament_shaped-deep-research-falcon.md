---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:36:41.117316'
end_time: '2026-06-18T07:46:57.878914'
duration_seconds: 616.76
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: filament shaped
  trait_identifier: METPO:1000674
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: filament_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism grows as elongated filamentous cells
    or hypha-like structures.
  parent_traits: METPO:1000666
  synonyms: S_filament, filament, filament-shaped
  evidence_summary: 'DOI:10.1016/j.mib.2010.10.002: polar growth of Streptomyces (Supports
    filamentous Streptomyces morphology as a polar-growth cell-shape system.)'
  causal_graph_summary: 'filament_shaped_streptomyces_polar_growth: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** filament shaped
- **METPO identifier:** METPO:1000674
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism grows as elongated filamentous cells or hypha-like structures.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_filament, filament, filament-shaped
- **Existing evidence:** DOI:10.1016/j.mib.2010.10.002: polar growth of Streptomyces (Supports filamentous Streptomyces morphology as a polar-growth cell-shape system.)
- **Existing causal graph summary:** filament_shaped_streptomyces_polar_growth: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **filament shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/filament_shaped.yaml`.

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
- **Trait label:** filament shaped
- **METPO identifier:** METPO:1000674
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism grows as elongated filamentous cells or hypha-like structures.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_filament, filament, filament-shaped
- **Existing evidence:** DOI:10.1016/j.mib.2010.10.002: polar growth of Streptomyces (Supports filamentous Streptomyces morphology as a polar-growth cell-shape system.)
- **Existing causal graph summary:** filament_shaped_streptomyces_polar_growth: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **filament shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/filament_shaped.yaml`.

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


## Microbial Trait Causal Graph Report: **filament shaped** (METPO:1000674)

### 0. Scope summary (TraitMech curation focus)
The METPO trait **filament shaped** refers to an elongated, filamentous cell morphology in which growth occurs as long, continuous cells (often hypha-like), commonly with tip extension and (in some taxa) branching. In bacteria this includes (i) **developmentally programmed filamentous hyphae** in filamentous Actinomycetota (e.g., *Streptomyces*), which extend by **polar (apical) cell-wall synthesis** organized at hyphal tips, and (ii) **stress-induced filamentation** in many Gram-negative bacteria, where cells elongate because **septation is blocked** (often SOS/SulA/FtsZ mediated), yielding **non-septate filamentous cells**. Sources in this report explicitly connect filamentous morphogenesis in *Streptomyces* to polar tip growth and polarisome dynamics (bhowmick2023osmoticstressresponses pages 1-2, sen2024adispensablesepiva pages 1-2), and Gram-negative filamentation to SOS-mediated division arrest via SulA inhibition of FtsZ polymerization (yu2023plasmidscanshift pages 1-2, ruhland2024theglobalrna–rna pages 1-2).

**Boundary cases / near traits (warnings for curation):**
- **Chains of rods** (cells remain separate but attached after division) should not be curated as “filament shaped” unless evidence shows a continuous non-septate filament.
- **Aggregates/pellets/biofilms** are multicellular arrangements; do not conflate with single-cell filament morphology.
- **Branching vs non-branching**: branching is common in hypha-like systems (e.g., *Streptomyces*) and can be represented as a connected subtrait or downstream phenotype; it should not redefine the parent trait.
- **Taxon specificity** matters: a protein (e.g., SepIVA) can be essential in one actinobacterial lineage and dispensable in another; such edges should be flagged as lineage-limited (sen2024adispensablesepiva pages 1-2).

### 1. Key concepts and definitions (current understanding)
#### 1.1 Two mechanistic archetypes of “filament shaped”
1) **Filamentous hyphal growth (Actinomycetota; fungal-like bacteria):**
- Hyphal/filamentous cells extend primarily by **tip growth**, i.e., localized polar wall insertion. In streptomycetes, DivIVA-mediated polarity is central; DivIVA forms discrete tip foci and is linked to branching by polarisome splitting (bhowmick2023osmoticstressresponses pages 1-2).

2) **Filamentation by division arrest (many Gram-negatives):**
- Cells elongate because division is stalled, typically under DNA damage or antibiotic stress. One canonical route is SOS activation leading to **sulA** expression, which inhibits **FtsZ polymerization**, producing non-septate filaments (yu2023plasmidscanshift pages 1-2, ruhland2024theglobalrna–rna pages 1-2).

#### 1.2 Operationalization/assays (what the trait captures)
- Light microscopy/SEM phenotype “long, filamentous cells” can reflect either polar tip growth (hyphal systems) or blocked septation (SOS filamentation). Mechanistic curation should therefore include **assay context** (growth phase, stressor, antibiotic, host environment).

### 2. Recent developments and latest research (prioritize 2023–2024)
#### 2.1 Filamentous Actinomycetota (Streptomyces): polarity + wall chemistry + division positioning
- **DivIVA/polarisome dynamics and envelope-stress signaling:** AfsK phosphorylates DivIVA, and high phosphorylation is linked to **apical polarisome disassembly** and **hyperbranching**, reversed by SppA (bhowmick2023osmoticstressresponses pages 1-2). This supports a causal chain from envelope stress → DivIVA phosphorylation state → altered tip organization → branching changes.
- **Cell wall glycopolymer attachment as a shape/division determinant:** In *Streptomyces venezuelae*, the LCP-family glycopolymer ligase **CglA** localizes to wall synthesis zones; reduced glycopolymers in a **cglA** mutant cause **enlarged vegetative hyphae** and **failures in FtsZ-ring formation/positioning**, leading to misplaced septa and reduced vitality (bhowmick2024cellshapeand pages 1-2). This provides a direct mechanistic connection between wall glycopolymer chemistry and filamentous hyphal morphology/division patterning.
- **SepIVA reinterpreted in streptomycetes:** A 2024 study reports SepIVA is dispensable for growth and division in *S. venezuelae* and does not localize to septa, but accumulates at hyphal tips and is “associated with polar growth,” with DivIVA interaction (sen2024adispensablesepiva pages 1-2). This is a strong “association” edge but a weak “required for filament shape” edge.

#### 2.2 Gram-negative filamentation: SOS + alternative FtsZ shutdown mechanisms
- **Plasmids modulate antibiotic-induced filamentation via sulA/SOS differences:** In antibiotic stress, filamentation is framed as “cell division is blocked” and is mechanistically tied to DNA damage → RecA/LexA SOS → sulA → FtsZ inhibition → non-septate filaments (yu2023plasmidscanshift pages 1-2). The same work provides quantitative evidence that plasmid-free cells can elongate substantially under ciprofloxacin, while plasmid-bearing cells remain closer to wild type (yu2023plasmidscanshift pages 1-2).
- **Post-transcriptional FtsZ control in SOS response (2024 PNAS):** In *Klebsiella pneumoniae*, the Hfq-dependent sRNA **DinR** accumulates upon DNA damage and represses **ftsZ** translation; the paper explicitly notes the canonical model that “SOS response stalls cell division … by activation of SulA which interferes with FtsZ polymerization,” and positions DinR as a complementary FtsZ deactivation route that “fosters filamentation” (ruhland2024theglobalrna–rna pages 1-2).
- **ROS-linked antibiotic filamentation phenotype (2024):** Bicyclomycin treatment in *E. coli* evokes ROS and is associated with SOS-linked filamentation and impaired septum formation (prakash2024bicyclomycingeneratesros pages 1-2). This supports ROS as a correlated upstream stressor/mediator, but the SulA→FtsZ mechanistic link is more explicit in other sources.

#### 2.3 Environmental chemical cues driving hyphal branching (signal-level mechanisms)
- A 2023 preprint reports that a redox-active compound (pyrogallol) induces **hyphal branching** in *Streptomyces* and that catalase diminishes the effect, while exogenous **H2O2** phenocopies it; the authors conclude ROS/H2O2 is the inducing factor (kato2023redoxactivecompoundgenerated pages 1-7). This provides a relatively direct environment/chemical → branching edge, relevant as a downstream morphology modifier for filamentous systems.

### 3. Current applications and real-world implementations
#### 3.1 Biotechnology and industrial microbiology
- Filamentous *Streptomyces* are foundational antibiotic and specialized metabolite producers; model systems (*S. coelicolor*, *S. venezuelae*) are used to interrogate multicellular development and production biology (sen2024adispensablesepiva pages 1-2). For TraitMech, this motivates inclusion of nodes linking polar growth and wall synthesis to filament morphology that impacts culture rheology and productivity (contextual rather than directly quantified here).

#### 3.2 Infection biology and anti-virulence strategies (UPEC)
- Filamentation is framed as a conserved persistence phenotype during UTIs and a potential anti-virulence target; cranberry-derived fractions are reported to prevent **SOS-mediated, SulA-driven** filamentation in UPEC, with filament length changes quantified under inducible SulA overexpression (prinster2025cranberryconstituentsprevent pages 4-6). This is a clear real-world implementation direction: anti-filamentation as adjunct or prevention strategy.
- In macrophage interactions, filament avoidance of engulfment depends on size/shape/surface and environment; UPEC can filament independently of sulA/ymfM in some contexts, warning against over-curating SulA as universally necessary for UPEC filamentation (cassaro2024imagingofbacterial pages 108-115).

### 4. Expert opinions and analysis (authoritative synthesis, curation guidance)
1) **Do not collapse “filament shaped” into one mechanism.** The same morphology label arises from distinct causal architectures:
- **Polar-growth filament systems** (DivIVA/polarisome, wall insertion at tips, branching programs) (bhowmick2023osmoticstressresponses pages 1-2, sen2024adispensablesepiva pages 1-2).
- **Division-arrest filaments** (SOS pathways, FtsZ inhibition, reversible elongation under stress) (yu2023plasmidscanshift pages 1-2, ruhland2024theglobalrna–rna pages 1-2).

2) **Prefer “core conserved” nodes vs lineage-specific modifiers.** FtsZ-centered division control is broadly conserved, but specific regulators (DinR in *Klebsiella*, SepIVA phenotype divergence across actinobacteria) should be curated with taxon qualifiers (sen2024adispensablesepiva pages 1-2, ruhland2024theglobalrna–rna pages 1-2).

3) **Wall chemistry nodes (glycopolymers) are high-value causal anchors in filamentous actinobacteria.** The 2024 CglA work provides strong, direct phenotypic causality from glycopolymer attachment defects to hyphal width/shape and FtsZ ring patterning (bhowmick2024cellshapeand pages 1-2).

### 5. Relevant recent statistics/data
- **Quantitative elongation under antibiotic stress (2023):** In *Pseudomonas alloputida* exposed to ciprofloxacin, plasmid-free cells elongated from **2.9 ± 0.5 μm to 7.7 ± 6.1 μm**, while plasmid-bearing cells retained near-wildtype length; the study also reports that **<50%** of cells became filamentous under antibiotic exposure (yu2023plasmidscanshift pages 1-2).
- **Clinical isolate observation (UPEC, 2025):** “Analysis of **42 clinical isolates** of uropathogenic *E. coli* (UPEC) revealed” filamentation as a conserved phenotype in response to host-derived antimicrobials; filamentation properties differ by clinical syndrome (febrile vs non-febrile) (prinster2025cranberryconstituentsprevent pages 4-6).
- **Population-level cell-length dynamics under TMP (2024 dissertation):** Single-cell length dynamics were measured on **500–1500 cells per experiment**; filamentation could be reduced/abolished by thymidine supplementation in some media, and some length changes were “limited to **2-fold**” under certain conditions (cassaro2024imagingofbacterial pages 108-115).
- **Public health context used to motivate filamentation-as-persistence (2023):** UTIs were stated to affect **≈4 million women annually in the U.S.** in the context of recurrent infections where filamentation may contribute to persistence (yu2023plasmidscanshift pages 1-2).

---

## 6. Candidate nodes (grouped by type) for `data/traits/morphology/filament_shaped.yaml`
The following table is intended for direct curation triage (grounded IDs when available; label-only otherwise).

| Section | Node label | Node type | Suggested CURIE/ID | Notes |
|---|---|---|---|---|
| Candidate nodes for filament-shaped trait graph | **Morphogenesis / polarity** |  |  |  |
| Candidate nodes for filament-shaped trait graph | DivIVA | protein | UniProt:P0A3U0 | Essential polar growth determinant in streptomycetes; forms tip-localized foci/polarisomes that guide apical growth and branching; Wag31 is the Corynebacteriales homolog, so keep as family-related but taxon-distinct node if needed (bhowmick2023osmoticstressresponses pages 1-2, sen2024adispensablesepiva pages 1-2) |
| Candidate nodes for filament-shaped trait graph | Wag31 | protein | UniProt:P9WPE5 | DivIVA-family polar growth protein in mycobacteria/corynebacteria; pole-localized scaffold regulating polar elongation and cell wall metabolism; taxon-specific homolog rather than universal synonym of Streptomyces DivIVA (sen2024adispensablesepiva pages 1-2, martinez2023eukaryoticlikegephyrinand pages 10-12) |
| Candidate nodes for filament-shaped trait graph | Scy | protein |  | Large coiled-coil apical growth/polarity protein in *Streptomyces*; part of the tip organizing complex/polarisome; implicated in branch emergence and links to division factors (bhowmick2023osmoticstressresponses pages 1-2, cassettari2023akeycomponent pages 1-7) |
| Candidate nodes for filament-shaped trait graph | FilP | protein |  | Intermediate filament-like coiled-coil protein associated with apical growth in streptomycetes; considered part of the filamentous tip growth machinery (bhowmick2023osmoticstressresponses pages 1-2, sen2024adispensablesepiva pages 1-2) |
| Candidate nodes for filament-shaped trait graph | SepIVA | protein |  | DivIVA-like coiled-coil protein; in *Streptomyces venezuelae* accumulates at vegetative hyphal tips and is associated with polar growth, but is dispensable and not supported as a core division factor there (sen2024adispensablesepiva pages 1-2) |
| Candidate nodes for filament-shaped trait graph | polarisome / TIPOC | complex |  | Tip-organizing polarity complex at hyphal tips; includes DivIVA and associated proteins such as Scy/FilP; candidate label-only node for trait graph (bhowmick2023osmoticstressresponses pages 1-2, cassettari2023akeycomponent pages 1-7) |
| Candidate nodes for filament-shaped trait graph | peptidoglycan synthesis at tips | process | GO:0009252 | Apical cell-wall synthesis process underlying filamentous hyphal extension in actinobacteria; keep as process node distinct from generic peptidoglycan biosynthesis (sen2024adispensablesepiva pages 1-2, letek2012cytoskeletalproteinsof pages 2-3) |
| Candidate nodes for filament-shaped trait graph | **Division / septation** |  |  |  |
| Candidate nodes for filament-shaped trait graph | SepF | protein | UniProt:Q8NNN6 | Early divisome component required for cytokinetic ring formation in *Streptomyces*; directly links polar growth and cell division through interaction with Scy (cassettari2023akeycomponent pages 1-7) |
| Candidate nodes for filament-shaped trait graph | FtsZ | protein | UniProt:P0A9A6 | Conserved tubulin-like cytokinetic protein; polymerizes into Z-rings/filaments to drive septation; inhibition commonly yields elongated non-septate filaments (cassettari2023akeycomponent pages 1-7, letek2012cytoskeletalproteinsof pages 2-3, ruhland2024theglobalrna–rna pages 1-2) |
| Candidate nodes for filament-shaped trait graph | **Regulators of polar growth / envelope stress** |  |  |  |
| Candidate nodes for filament-shaped trait graph | AfsK | protein kinase |  | Ser/Thr kinase that phosphorylates DivIVA in *Streptomyces* during envelope stress; high phosphorylation is linked to polarisome disassembly and hyperbranching (bhowmick2023osmoticstressresponses pages 1-2) |
| Candidate nodes for filament-shaped trait graph | SppA | phosphatase |  | Phosphatase that reverses DivIVA phosphorylation downstream of AfsK-regulated polarity control (bhowmick2023osmoticstressresponses pages 1-2) |
| Candidate nodes for filament-shaped trait graph | DisA | protein |  | Diadenylate cyclase producing c-di-AMP; part of osmotic stress and developmental regulation in *Streptomyces*; use label if precise accession is not curated yet (bhowmick2024cellshapeand pages 1-2, bhowmick2023osmoticstressresponses pages 1-2) |
| Candidate nodes for filament-shaped trait graph | c-di-AMP | chemical | CHEBI:15996 | Bacterial second messenger linked to osmotic stress adaptation and cell differentiation; physiologically linked to cell-wall glycopolymer decoration in *Streptomyces* (bhowmick2024cellshapeand pages 1-2, bhowmick2023osmoticstressresponses pages 1-2) |
| Candidate nodes for filament-shaped trait graph | CglA | protein |  | LCP/LytR-C family glycopolymer ligase in *Streptomyces venezuelae*; localizes to cell-wall biosynthesis zones and is required for normal hyphal width and FtsZ-ring positioning (bhowmick2024cellshapeand pages 1-2) |
| Candidate nodes for filament-shaped trait graph | glycopolymers / WTAs | chemical |  | Cell-wall glycopolymer pool attached to peptidoglycan; label-only node because exact chemistry varies; reduction in glycopolymer content perturbs shape and division (bhowmick2024cellshapeand pages 1-2) |
| Candidate nodes for filament-shaped trait graph | **Oxidative / chemical drivers of branching or filamentation** |  |  |  |
| Candidate nodes for filament-shaped trait graph | ROS | chemical | CHEBI:26523 | Reactive oxygen species; in streptomycetes low ROS generated by redox-active compounds can induce hyphal branching; in Gram-negatives ROS can accompany SOS-associated filamentation (kato2023redoxactivecompoundgenerated pages 1-7, prakash2024bicyclomycingeneratesros pages 1-2) |
| Candidate nodes for filament-shaped trait graph | hydrogen peroxide | chemical | CHEBI:16240 | Specific ROS shown to induce hyphal branching in *Streptomyces*; catalase-sensitive signal in coculture-derived morphology changes (kato2023redoxactivecompoundgenerated pages 1-7) |
| Candidate nodes for filament-shaped trait graph | catalase | protein | EC:1.11.1.6 | Enzyme that degrades H2O2; used experimentally to suppress pyrogallol-induced branching, supporting causal involvement of peroxide (kato2023redoxactivecompoundgenerated pages 1-7) |
| Candidate nodes for filament-shaped trait graph | bicyclomycin | chemical | CHEBI:3225 | Antibiotic/Rho inhibitor that generates ROS and is associated with SOS-linked cell filamentation in *E. coli* (prakash2024bicyclomycingeneratesros pages 1-2) |
| Candidate nodes for filament-shaped trait graph | ciprofloxacin | chemical | CHEBI:100241 | DNA-damaging fluoroquinolone commonly inducing SOS-associated filamentation and sulA expression in Gram-negatives (yu2023plasmidscanshift pages 1-2) |
| Candidate nodes for filament-shaped trait graph | cephalexin | chemical | CHEBI:34750 | Cell-wall targeting β-lactam associated with filamentation under antibiotic stress in Gram-negatives (yu2023plasmidscanshift pages 1-2) |
| Candidate nodes for filament-shaped trait graph | **DNA damage checkpoint / Gram-negative filamentation** |  |  |  |
| Candidate nodes for filament-shaped trait graph | DNA damage | process | GO:0006974 | Upstream stress state that activates the SOS response and drives division arrest-associated filamentation (yu2023plasmidscanshift pages 1-2, ruhland2024theglobalrna–rna pages 1-2, prakash2024bicyclomycingeneratesros pages 1-2) |
| Candidate nodes for filament-shaped trait graph | RecA | protein | UniProt:P0A7G6 | ssDNA-responsive recombinase/co-protease that promotes LexA cleavage during SOS induction; upstream node for stress-induced filamentation (ruhland2024theglobalrna–rna pages 1-2, prakash2024bicyclomycingeneratesros pages 1-2) |
| Candidate nodes for filament-shaped trait graph | LexA | protein | UniProt:P0A7C2 | SOS repressor; autoproteolysis derepresses SOS genes after RecA activation (ruhland2024theglobalrna–rna pages 1-2) |
| Candidate nodes for filament-shaped trait graph | SOS response | process | GO:0009432 | DNA damage response pathway that arrests division until repair; major mechanistic route to stress-induced filamentous morphology in Enterobacterales (yu2023plasmidscanshift pages 1-2, ruhland2024theglobalrna–rna pages 1-2, prakash2024bicyclomycingeneratesros pages 1-2) |
| Candidate nodes for filament-shaped trait graph | SulA | protein | UniProt:P0A802 | SOS-induced division inhibitor that interferes with FtsZ polymerization/assembly, producing non-septate cellular filamentation (yu2023plasmidscanshift pages 1-2, ruhland2024theglobalrna–rna pages 1-2, aguilarluviano2025conditionalfilamentationenhances pages 1-3) |
| Candidate nodes for filament-shaped trait graph | Lon protease | protein | UniProt:P0A9M0 | ATP-dependent protease that degrades SulA; relevant for reversibility/control of filamentation and for inducible UPEC anti-filamentation assays (prinster2025cranberryconstituentsprevent pages 4-6, prakash2024bicyclomycingeneratesros pages 1-2) |
| Candidate nodes for filament-shaped trait graph | DinR sRNA | process |  | Hfq-dependent small RNA in *Klebsiella pneumoniae* that represses *ftsZ* translation during DNA damage and fosters filamentation; label-only because stable RNA accession not yet assigned here (ruhland2024theglobalrna–rna pages 1-2) |
| Candidate nodes for filament-shaped trait graph | Hfq | protein | UniProt:P0A6X3 | RNA chaperone required for DinR-dependent post-transcriptional regulation of *ftsZ* in *K. pneumoniae* (ruhland2024theglobalrna–rna pages 1-2) |
| Candidate nodes for filament-shaped trait graph | **Environmental stress / osmoadaptation** |  |  |  |
| Candidate nodes for filament-shaped trait graph | hyperosmotic stress / high salt | environmental factor | ENVO:01001800 | Environmental driver affecting filamentous actinobacteria; linked to c-di-AMP physiology and growth defects/rescue relationships involving cell-wall glycopolymer decoration (bhowmick2024cellshapeand pages 1-2, bhowmick2023osmoticstressresponses pages 1-2) |
| Candidate nodes for filament-shaped trait graph | compatible solutes | chemical |  | Aggregate node for osmoprotectants accumulated after osmotic upshift; helpful parent node if individual compounds are also represented (bhowmick2023osmoticstressresponses pages 1-2) |
| Candidate nodes for filament-shaped trait graph | trehalose | chemical | CHEBI:18198 | Compatible solute accumulated during osmotic stress in *Streptomyces* (bhowmick2023osmoticstressresponses pages 1-2) |
| Candidate nodes for filament-shaped trait graph | ectoine | chemical | CHEBI:27689 | Compatible solute/osmoprotectant reported in osmoadaptation context (bhowmick2023osmoticstressresponses pages 1-2) |
| Candidate nodes for filament-shaped trait graph | proline | chemical | CHEBI:17203 | Compatible solute/amino acid accumulated during osmotic upshift (bhowmick2023osmoticstressresponses pages 1-2) |
| Candidate nodes for filament-shaped trait graph | potassium ion (K+) | chemical | CHEBI:29103 | Early osmotic response ion accumulated to maintain turgor after osmotic upshift (bhowmick2023osmoticstressresponses pages 1-2) |
| Candidate nodes for filament-shaped trait graph | **Mobile genetic elements / modulators of stress filamentation** |  |  |  |
| Candidate nodes for filament-shaped trait graph | plasmid | complex |  | Extrachromosomal element that can reduce antibiotic-triggered filamentation by altering DNA damage, efflux, and sulA expression; context-specific modulator rather than universal trait determinant (yu2023plasmidscanshift pages 1-2) |
| Candidate nodes for filament-shaped trait graph | parDE toxin-antitoxin module | complex |  | Plasmid-borne toxin-antitoxin system implicated in stress-response differences between plasmid-bearing and plasmid-free cells under ciprofloxacin/cephalexin exposure (yu2023plasmidscanshift pages 1-2) |


*Table: This table compiles candidate nodes for a filament-shaped microbial trait graph, grouped by functional type and annotated with suggested identifiers and curation notes. It is useful for selecting broadly supported versus taxon-specific entities before YAML graph construction.*

---

## 7. Candidate causal edges (evidence-backed triples)
The table below proposes candidate directed edges suitable for inclusion in a TraitMech causal graph, with explicit snippets and curation notes.

| Edge (subject–predicate–object) | Evidence snippet (verbatim short quote) | Taxon/context | Strength/uncertainty | Source (DOI, year, URL, citation id) |
|---|---|---|---|---|
| DivIVA/polarisome → enables → polar hyphal growth | “Hyphal growth occurs at the tips of the filamentous cells … this polar growth is mediated by DivIVA” | *Streptomyces* developmental hyphae | Strong; review summary, broad for streptomycetes | 10.1128/jb.00153-23, 2023, https://doi.org/10.1128/jb.00153-23 (sen2024adispensablesepiva pages 1-2) |
| DivIVA foci/polarisome splitting → promotes → branch emergence | “DivIVA forms discrete foci at growing tips” and “splitting of polarisomes at tips produces daughter polarisomes that coordinate emergence of new branches” | *Streptomyces* vegetative branching | Strong; mechanistic review | 10.1093/femsml/uqad020, 2023, https://doi.org/10.1093/femsml/uqad020 (bhowmick2023osmoticstressresponses pages 1-2) |
| SepIVA → associated_with → polar growth | “mNeonGreen-SepIVA was accumulated at the tips of growing vegetative hyphae” and “The results suggest that it is associated with polar growth” | *Streptomyces venezuelae* | Strong for association; uncertain for necessity because deletion had no phenotype | 10.1186/s12866-024-03625-6, 2024, https://doi.org/10.1186/s12866-024-03625-6 (sen2024adispensablesepiva pages 1-2) |
| SepIVA → not_involved_in → cell division/septation | “found that sepIVA is dispensable for growth, cell division and sporulation” and “did not localize at division septa” | *Streptomyces venezuelae* | Strong negative edge; useful warning for curation | 10.1186/s12866-024-03625-6, 2024, https://doi.org/10.1186/s12866-024-03625-6 (sen2024adispensablesepiva pages 1-2) |
| CglA → mediates → cell-wall glycopolymer attachment | “identified the LCP-LytR_C domain protein CglA … as a key glycopolymer ligase” | *Streptomyces venezuelae* cell wall biogenesis | Strong | 10.1128/mbio.01492-24, 2024, https://doi.org/10.1128/mbio.01492-24 (bhowmick2024cellshapeand pages 1-2) |
| cglA loss → causes → enlarged hyphae / loss of cell shape | “Reduced amount of glycopolymers in the cglA mutant results in enlarged vegetative hyphae” | *Streptomyces venezuelae* vegetative mycelium | Strong | 10.1128/mbio.01492-24, 2024, https://doi.org/10.1128/mbio.01492-24 (bhowmick2024cellshapeand pages 1-2) |
| cglA loss → disrupts → FtsZ-ring formation and positioning | “failures in FtsZ-rings formation and positioning” | *Streptomyces venezuelae* sporulation/division | Strong | 10.1128/mbio.01492-24, 2024, https://doi.org/10.1128/mbio.01492-24 (bhowmick2024cellshapeand pages 1-2) |
| AfsK phosphorylation of DivIVA → causes → polarisome disassembly | “AfsK … phosphorylates DivIVA” and “high DivIVA phosphorylation by AfsK causes disassembly of the apical polarisome” | Cell-envelope stress response in *Streptomyces* | Strong; pathway summarized in review | 10.1093/femsml/uqad020, 2023, https://doi.org/10.1093/femsml/uqad020 (bhowmick2023osmoticstressresponses pages 1-2) |
| DivIVA hyperphosphorylation → stimulates → hyperbranching | “stimulates formation of multiple new polarisomes leading to hyperbranching” | *Streptomyces* branching morphogenesis | Strong | 10.1093/femsml/uqad020, 2023, https://doi.org/10.1093/femsml/uqad020 (bhowmick2023osmoticstressresponses pages 1-2) |
| cglA deletion → rescues under → high-salt growth of disA mutant | “deletion of cglA restores growth of the S. venezuelae disA mutant at high salt” | c-di-AMP / osmotic stress physiology in *Streptomyces* | Moderate; links osmotic stress signaling to wall decoration rather than filament shape directly | 10.1128/mbio.01492-24, 2024, https://doi.org/10.1128/mbio.01492-24 (bhowmick2024cellshapeand pages 1-2) |
| ROS/H2O2 → induces → hyphal branching | “the pyrogallol activity was diminished by adding catalase, which broke down H2O2” and “H2O2 was tested and similar activity which induced hyphal branching was observed” | *Streptomyces* species; interspecies chemical crosstalk | Strong for branching; note branching is a subtrait of filament morphology | 10.1101/2023.01.12.523877, 2023, https://doi.org/10.1101/2023.01.12.523877 (kato2023redoxactivecompoundgenerated pages 1-7) |
| RecA/LexA SOS response → induces → SulA-mediated division arrest | “DNA damage activates the RecA/LexA SOS response, leading to expression of sulA” | Gram-negative antibiotic stress | Strong | 10.1002/advs.202203260, 2023, https://doi.org/10.1002/advs.202203260 (yu2023plasmidscanshift pages 1-2) |
| SulA → inhibits → FtsZ polymerization | “a cell division inhibitor, sulA, blocks FtsZ” / “SulA which interferes with FtsZ polymerization” | *E. coli* / Enterobacterales SOS filamentation | Strong | 10.1002/advs.202203260, 2023, https://doi.org/10.1002/advs.202203260 (yu2023plasmidscanshift pages 1-2); 10.1073/pnas.2317322121, 2024, https://doi.org/10.1073/pnas.2317322121 (ruhland2024theglobalrna–rna pages 1-2) |
| FtsZ inhibition / blocked septation → causes → filamentation | “contributes to non-septate cellular filamentation” | Gram-negative stress-induced filamentation | Strong | 10.1002/advs.202203260, 2023, https://doi.org/10.1002/advs.202203260 (yu2023plasmidscanshift pages 1-2) |
| DinR sRNA → inhibits → ftsZ translation → filamentation | “DinR … represses ftsZ translation by occupying the ribosome binding site” and “fosters filamentation of K. pneumoniae” | *Klebsiella pneumoniae* DNA-damage response | Strong; taxon-specific alternative/additional SOS branch | 10.1073/pnas.2317322121, 2024, https://doi.org/10.1073/pnas.2317322121 (ruhland2024theglobalrna–rna pages 1-2) |
| Plasmid carriage / parDE → reduces → sulA-linked filamentation under antibiotics | “Significantly higher expression of sulA is observed in plasmid-free cells, compared to plasmid-bearing cells” | Plasmid effects on ciprofloxacin/cephalexin stress | Moderate; mechanism includes reduced DNA damage and stronger efflux, not solely parDE | 10.1002/advs.202203260, 2023, https://doi.org/10.1002/advs.202203260 (yu2023plasmidscanshift pages 1-2) |
| Bicyclomycin → generates → ROS/SOS-associated filamentation | “BCM evoked the generation of ROS in E. coli cells” and “bicyclomycin-dependent cell filamentation is associated with SOS response” | *Escherichia coli* antibiotic response | Moderate-strong; SOS association explicit, SulA/FtsZ step less direct in this source | 10.1371/journal.pone.0293858, 2024, https://doi.org/10.1371/journal.pone.0293858 (prakash2024bicyclomycingeneratesros pages 1-2) |


*Table: This table compiles candidate subject–predicate–object edges for the filament-shaped trait with short supporting quotes, taxonomic context, and source details. It is useful for prioritizing which mechanisms are strong enough for TraitMech curation and which are context-specific or indirect.*

---

## 8. Warnings / claims not yet ready for TraitMech curation
1) **SepIVA essentiality is lineage-dependent.** In *S. venezuelae*, SepIVA is dispensable and not septum-localized; curate as “associated with polar growth” (tip localization) rather than “required for filament shape” unless additional taxon/condition evidence is added (sen2024adispensablesepiva pages 1-2).
2) **SulA is not universally required for infection-associated filamentation.** Experimental evidence indicates filamentation can occur independently of sulA/ymfM in UPEC under some conditions; a “SulA→filamentation” edge should be marked **contextual** (DNA damage/SOS-dependent filamentation) rather than universal for all filamentation phenotypes (cassaro2024imagingofbacterial pages 108-115).
3) **ROS→filamentation vs ROS→branching are distinct.** In *Streptomyces*, H2O2 is evidenced as a branching inducer (kato2023redoxactivecompoundgenerated pages 1-7). In *E. coli* bicyclomycin generates ROS and is associated with SOS/filamentation (prakash2024bicyclomycingeneratesros pages 1-2), but a direct curated edge ROS→SOS→SulA→FtsZ inhibition should rely on sources that explicitly connect those steps (yu2023plasmidscanshift pages 1-2, ruhland2024theglobalrna–rna pages 1-2).

---

## 9. DOI-first bibliography (publication date and URL where available)
- **Bhowmick S. et al.** (Oct 2024). *Cell shape and division septa positioning in filamentous Streptomyces require a functional cell wall glycopolymer ligase CglA.* mBio. DOI: **10.1128/mbio.01492-24**. https://doi.org/10.1128/mbio.01492-24 (bhowmick2024cellshapeand pages 1-2)
- **Sen B.C. et al.** (Nov 2024). *A dispensable SepIVA orthologue in Streptomyces venezuelae is associated with polar growth and not cell division.* BMC Microbiology. DOI: **10.1186/s12866-024-03625-6**. https://doi.org/10.1186/s12866-024-03625-6 (sen2024adispensablesepiva pages 1-2)
- **Bhowmick S. et al.** (Apr 2023). *Osmotic stress responses and the biology of the second messenger c-di-AMP in Streptomyces.* microLife. DOI: **10.1093/femsml/uqad020**. https://doi.org/10.1093/femsml/uqad020 (bhowmick2023osmoticstressresponses pages 1-2)
- **Yu Z. et al.** (Nov 2023). *Plasmids Can Shift Bacterial Morphological Response against Antibiotic Stress.* Advanced Science. DOI: **10.1002/advs.202203260**. https://doi.org/10.1002/advs.202203260 (yu2023plasmidscanshift pages 1-2)
- **Ruhland E. et al.** (Feb 2024). *The global RNA–RNA interactome of Klebsiella pneumoniae unveils a small RNA regulator of cell division.* PNAS. DOI: **10.1073/pnas.2317322121**. https://doi.org/10.1073/pnas.2317322121 (ruhland2024theglobalrna–rna pages 1-2)
- **Prakash A., Dutta D.** (Mar 2024). *Bicyclomycin generates ROS and blocks cell division in Escherichia coli.* PLOS ONE. DOI: **10.1371/journal.pone.0293858**. https://doi.org/10.1371/journal.pone.0293858 (prakash2024bicyclomycingeneratesros pages 1-2)
- **Kato M. et al.** (Jan 2023). *Redox-active compound generated by bacterial crosstalk induces hypha branching in Streptomyces species.* bioRxiv. DOI: **10.1101/2023.01.12.523877**. https://doi.org/10.1101/2023.01.12.523877 (kato2023redoxactivecompoundgenerated pages 1-7)
- **Prinster T. et al.** (May 2025). *Cranberry constituents prevent SOS-mediated filamentation of uropathogenic Escherichia coli.* Infection and Immunity. DOI: **10.1128/iai.00600-24**. https://doi.org/10.1128/iai.00600-24 (prinster2025cranberryconstituentsprevent pages 4-6)
- **Cassaro C.** (Jan 2024). *Imaging of bacterial responses to DNA damage caused by antibacterial agents.* University of Oxford dissertation. DOI: **10.5287/ora-amngwxnk0**. https://doi.org/10.5287/ora-amngwxnk0 (cassaro2024imagingofbacterial pages 108-115)



References

1. (bhowmick2023osmoticstressresponses pages 1-2): Sukanya Bhowmick, Mary L. Shenouda, and Natalia Tschowri. Osmotic stress responses and the biology of the second messenger c-di-amp in streptomyces. microLife, Apr 2023. URL: https://doi.org/10.1093/femsml/uqad020, doi:10.1093/femsml/uqad020. This article has 17 citations and is from a peer-reviewed journal.

2. (sen2024adispensablesepiva pages 1-2): Beer Chakra Sen, Parminder Singh Mavi, Oihane Irazoki, Susmita Datta, Sebastian Kaiser, Felipe Cava, and Klas Flärdh. A dispensable sepiva orthologue in streptomyces venezuelae is associated with polar growth and not cell division. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03625-6, doi:10.1186/s12866-024-03625-6. This article has 6 citations and is from a peer-reviewed journal.

3. (yu2023plasmidscanshift pages 1-2): Zhigang Yu, Emily C. A. Goodall, Ian R. Henderson, and Jianhua Guo. Plasmids can shift bacterial morphological response against antibiotic stress. Advanced Science, Nov 2023. URL: https://doi.org/10.1002/advs.202203260, doi:10.1002/advs.202203260. This article has 21 citations and is from a peer-reviewed journal.

4. (ruhland2024theglobalrna–rna pages 1-2): Eric Ruhland, Malte Siemers, Ruman Gerst, Felix Späth, Laura Nicole Vogt, Marc Thilo Figge, Kai Papenfort, and Kathrin Sophie Fröhlich. The global rna–rna interactome of klebsiella pneumoniae unveils a small rna regulator of cell division. Proceedings of the National Academy of Sciences of the United States of America, Feb 2024. URL: https://doi.org/10.1073/pnas.2317322121, doi:10.1073/pnas.2317322121. This article has 28 citations and is from a highest quality peer-reviewed journal.

5. (bhowmick2024cellshapeand pages 1-2): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

6. (prakash2024bicyclomycingeneratesros pages 1-2): Anand Prakash and Dipak Dutta. Bicyclomycin generates ros and blocks cell division in escherichia coli. PLOS ONE, 19:e0293858, Mar 2024. URL: https://doi.org/10.1371/journal.pone.0293858, doi:10.1371/journal.pone.0293858. This article has 7 citations and is from a peer-reviewed journal.

7. (kato2023redoxactivecompoundgenerated pages 1-7): Manami Kato, Shumpei Asamizu, and Hiroyasu Onaka. Redox-active compound generated by bacterial crosstalk induces hypha branching in streptomyces species. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.12.523877, doi:10.1101/2023.01.12.523877. This article has 0 citations.

8. (prinster2025cranberryconstituentsprevent pages 4-6): Tracy Prinster, Alistair Harrison, Christopher Dick, Dennis J. Horvath, Birong Li, Grace Sievers, Revanth Madamsetty, Jingwen Zhang, Kevin M. Mason, Christina Khoo, and Sheryl S. Justice. Cranberry constituents prevent sos-mediated filamentation of uropathogenic <i>escherichia coli</i>. May 2025. URL: https://doi.org/10.1128/iai.00600-24, doi:10.1128/iai.00600-24. This article has 1 citations and is from a peer-reviewed journal.

9. (cassaro2024imagingofbacterial pages 108-115): Imaging of bacterial responses to DNA damage caused by antibacterial agents This article has 1 citations.

10. (martinez2023eukaryoticlikegephyrinand pages 10-12): M. Martinez, J. Petit, A. Leyva, A. Sogues, D. Megrian, A. Rodriguez, Q. Gaday, M. Ben Assaya, M. Portela, A. Haouz, A. Ducret, C. Grangeasse, P. M. Alzari, R. Durán, and A. Wehenkel. Eukaryotic-like gephyrin and cognate membrane receptor coordinate corynebacterial cell division and polar elongation. bioRxiv, Feb 2023. URL: https://doi.org/10.1101/2023.02.01.526586, doi:10.1101/2023.02.01.526586. This article has 17 citations.

11. (cassettari2023akeycomponent pages 1-7): Gemma Cassettari, Xiao Tan, Pak Lau, Daniel Moye, Stefan Harper, Bertrand Lézé, Lucy Burrows, Emily Alcock, Kavana Bywater-Brenna, Benjamin Bone, Dovile Jonylaite, and Gabriella Kelemen. A key component of the early divisome, sepf, integrates spatial cues and directly links polar growth and cell division in streptomyces. Unknown journal, Mar 2023. URL: https://doi.org/10.21203/rs.3.rs-2647660/v1, doi:10.21203/rs.3.rs-2647660/v1.

12. (letek2012cytoskeletalproteinsof pages 2-3): Michal Letek, María Fiuza, A. F. Villadangos, L. M. Mateos, and J. Gil. Cytoskeletal proteins of actinobacteria. International Journal of Cell Biology, Feb 2012. URL: https://doi.org/10.1155/2012/905832, doi:10.1155/2012/905832. This article has 18 citations and is from a peer-reviewed journal.

13. (aguilarluviano2025conditionalfilamentationenhances pages 1-3): O. B. Aguilar-Luviano, F. Santos-Escobar, S. Orozco-Barrera, and R. Peña-Miller. Conditional filamentation enhances bacterial survival in toxic environments. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.13.653778, doi:10.1101/2025.05.13.653778. This article has 1 citations.