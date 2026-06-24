---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:40:38.352041'
end_time: '2026-06-18T08:55:43.581707'
duration_seconds: 905.23
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: non motile
  trait_identifier: METPO:1000703
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: non_motile
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A motility in which an organism lacks the ability to move independently
    under its own power.
  parent_traits: METPO:1000701
  synonyms: no, non-motile
  evidence_summary: 'DOI:10.3389/fmicb.2025.1514643: They are Gram-negative, non-motile
    rods (Organism example: Klebsiella pneumoniae is described as non-motile.) | DOI:10.1146/annurev.micro.57.030502.090832:
    flagellum (Bacterial flagellum review supports the absence or non-expression of
    the flagellar apparatus as the basis for non-motile phenotypes.)'
  causal_graph_summary: 'non_motile_absent_motility_apparatus: 4 nodes, 3 edges'
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
- **Trait label:** non motile
- **METPO identifier:** METPO:1000703
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism lacks the ability to move independently under its own power.
- **Parent traits:** METPO:1000701
- **Synonyms:** no, non-motile
- **Existing evidence:** DOI:10.3389/fmicb.2025.1514643: They are Gram-negative, non-motile rods (Organism example: Klebsiella pneumoniae is described as non-motile.) | DOI:10.1146/annurev.micro.57.030502.090832: flagellum (Bacterial flagellum review supports the absence or non-expression of the flagellar apparatus as the basis for non-motile phenotypes.)
- **Existing causal graph summary:** non_motile_absent_motility_apparatus: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **non motile** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/non_motile.yaml`.

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
- **Trait label:** non motile
- **METPO identifier:** METPO:1000703
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism lacks the ability to move independently under its own power.
- **Parent traits:** METPO:1000701
- **Synonyms:** no, non-motile
- **Existing evidence:** DOI:10.3389/fmicb.2025.1514643: They are Gram-negative, non-motile rods (Organism example: Klebsiella pneumoniae is described as non-motile.) | DOI:10.1146/annurev.micro.57.030502.090832: flagellum (Bacterial flagellum review supports the absence or non-expression of the flagellar apparatus as the basis for non-motile phenotypes.)
- **Existing causal graph summary:** non_motile_absent_motility_apparatus: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **non motile** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/non_motile.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **non motile** (METPO:1000703)

### 0) Trait summary (scope for curation)
**Trait label:** non motile (METPO:1000703)

**Operational definition (curation-ready):** An assay-observed phenotype in which an organism lacks self-propelled movement under its own power, typically assessed by migration/spread in semi-solid (soft-agar) swimming assays or on surfaces (swarming/spreading assays). (carter2024conditionalexpressionof pages 1-2, ranta2024fenkokae01isa pages 1-2)

**Key boundary cases (must be explicitly handled in curation):**
1. **Nonflagellated ≠ non-motile:** Genome-based inference of “nonflagellated” does not guarantee non-motility because some taxa move by **non-flagellar mechanisms** (e.g., gliding). Therefore, absence of flagellar genes should be curated as “absence of flagellar motility apparatus” rather than absolute “non motile,” unless confirmed phenotypically. (ramoneda2024ecologicalrelevanceof pages 5-6, ramoneda2024ecologicalrelevanceof pages 2-3)
2. **Chemotaxis defects can mimic non-motility in some assays:** A strain can possess flagella but show impaired migration in soft agar if chemotaxis/rotation bias is altered; this is mechanistically distinct from absence of the motility apparatus. (liu2024counterclockwiserotationof pages 1-2, wang2024argrregulatesmotility pages 1-2)
3. **Environment- and medium-dependent motility:** Some isolates scored “non-motile” in one condition can become motile under different media/supplements, so curations should encode assay context (medium, temperature, growth state) when possible. (carter2024conditionalexpressionof pages 1-2)

### 1) Key concepts & current understanding (mechanistic decomposition)
Non-motility can arise from multiple mechanistic classes:

**A. Structural loss or disruption of the motility apparatus (high-confidence causal route)**
- Loss-of-function mutations/deletions in **flagellar structural genes** (e.g., filament/hook/basal body components) or **motor/stator proteins** can directly yield a non-motile phenotype. Examples include engineered disruptive flagellin-domain mutants that are non-motile despite expressing variant FliC protein, supporting “function loss” rather than “expression loss.” (esteves2023phagesonfilaments pages 9-11)
- Non-motility may also arise from disruption of specialized structural features (e.g., basal disk components) with occasional residual rotation, highlighting assay-dependence (migration readout vs microscopic rotation). (cohen2023evolutionofa pages 9-12)

**B. Regulatory repression of motility programs (motile-to-sessile switching)**
- **c-di-GMP** is a central second messenger that inversely couples motility and biofilm/sessility programs in many bacteria; at high c-di-GMP, transcriptional programs can shift away from flagellar genes. (oladosu2024fliptheswitch pages 4-7)
- Specific **c-di-GMP effector proteins** can directly repress flagellar biogenesis, e.g., STM0435 in *Salmonella*, which binds c-di-GMP and inhibits flagellar biogenesis/motility. (dai2024acdigmpbinding pages 1-2, dai2024acdigmpbinding pages 8-10)

**C. Environmental and experimental factors (contextual determinants)**
- Motility phenotypes can be conditional on nutrient conditions or environmental supplements (e.g., richer medium or complex environmental water) that activate expression or functionality of motility systems. (carter2024conditionalexpressionof pages 1-2)
- Metal-responsive regulation can modulate motility gene transcription, exemplified by Cu(II) inhibiting binding of the motility repressor CdsR to promoters. (zhang2024anovelregulator pages 1-2)

### 2) Recent developments and latest research (prioritized 2023–2024)

#### 2.1 c-di-GMP effectors and mechanistic switching (2024)
- **Pseudomonas FleQ as a c-di-GMP-dependent transcriptional switch:** A 2024 review synthesizes evidence that at high c-di-GMP, FleQ no longer activates flagellar genes and shifts regulation toward matrix/biofilm genes. A curated-ready summary table (Table 1) explicitly lists many flagellar genes as activated at low c-di-GMP and repressed at high c-di-GMP. (oladosu2024fliptheswitch pages 4-7, oladosu2024fliptheswitch media 9db214e5)
- **Salmonella STM0435 as a newly characterized c-di-GMP binding inhibitor of flagellar biogenesis:** STM0435 binds c-di-GMP (Kd reported) and deletion of stm0435 increases expression of core flagellar genes (flhD, fliA, fliC) and motility; motility phenotypes depend on c-di-GMP binding and cellular c-di-GMP modulation. (dai2024acdigmpbinding pages 1-2, dai2024acdigmpbinding pages 8-10)
- **Local c-di-GMP signaling linked to flagellar localization factors:** Deletion of *P. aeruginosa* **flhF** yields a non-motile mutant with elevated c-di-GMP-linked biofilm phenotypes; FlhF interacts with HsbR, and HsbR interacts with WspR, connecting flagellar localization machinery to c-di-GMP production/localization. (guan2024flhfaffectsthe pages 1-2, guan2024flhfaffectsthe pages 2-6)

#### 2.2 Comparative genomics and community-level statistics (2024)
A large 2024 ISME Journal study developed and validated a **genome-based classifier** using presence/absence of **21 flagellar genes** to infer flagellar motility potential across **26,192 genomes** spanning **12 phyla**, and then applied it to metagenomes across soil carbon gradients. (ramoneda2024ecologicalrelevanceof pages 5-6, ramoneda2024ecologicalrelevanceof pages 2-3)

Key quantitative results for “flagellar motility potential” prevalence by phylum (useful contextual statistics, but not identical to METPO:1000703):
- Spirochaetota **93.2%**, Proteobacteria **78.3%**, Firmicutes **54.6%**, Actinobacteriota **15.9%**, Bacteroidota **0.7%**, and Deinococcota/Mycoplasmatota approximately **0%** (as reported in the evidence excerpt). (ramoneda2024ecologicalrelevanceof pages 5-6)

Model performance statistic relevant to curation of “absence of flagellar apparatus” nodes:
- Correctly called **nonflagellated taxa in 94.5% of cases** among experimentally classified nonflagellated taxa. (ramoneda2024ecologicalrelevanceof pages 5-6)

### 3) Current applications and real-world implementations

**A. Phage therapy and phage resistance via non-motility (2024)**
A 2024 study of a flagellum-specific jumbo phage (fENko-Kae01) showed that phage selection yields resistant mutants in *Klebsiella aerogenes*, and whole-genome sequencing implicated disrupted flagellum biogenesis in multiple mutants; the phage failed to adsorb to non-motile mutants, identifying the flagellum as receptor. This provides a real-world selection context in which “non-motile” becomes an adaptive phenotype under phage pressure. (ranta2024fenkokae01isa pages 1-2)

**B. Environmental microbiome trait inference (2024)**
The genome/metagenome approach described above enables estimation of the prevalence of “flagellar motility potential” from metagenomes, allowing ecological studies to relate community-level motility potential to environmental gradients (e.g., soil carbon availability). This is increasingly used as a trait-based ecology implementation for motility-relevant inference. (ramoneda2024ecologicalrelevanceof pages 2-3)

**C. Pathogenesis and host interaction contexts (2023–2024)**
Several studies reinforce that motility state is intertwined with host colonization and biofilm initiation; for example, *H. pylori* work shows biofilm initiation correlates with flagellar rotational bias (chemotaxis mutants) and that motor/flagellar gene disruptions reduce biofilm outcomes, highlighting non-motility as functionally consequential for infection-related phenotypes. (liu2024counterclockwiserotationof pages 1-2)

### 4) Expert opinions and authoritative synthesis (as represented in 2024 review sources)
- The FleQ-focused review in *Journal of Bacteriology* (2024) explicitly frames FleQ as a regulator mediating transition between free-living (flagella-associated) and sessile (biofilm-associated) modes, emphasizing sigma factors and c-di-GMP in inverse regulation of motility vs biofilm genes, and provides a gene-level summary table suitable for curation. (oladosu2024fliptheswitch pages 4-7, oladosu2024fliptheswitch media 9db214e5)
- A 2024 review/meta-analysis of response regulators in *Salmonella Enteritidis* highlights two-component system response regulators as key determinants of motility phenotypes and cites EnvZ–OmpR control of the flagellar master operon flhDC in Enterobacteriaceae. (hu2024rolesofresponse pages 1-2)

### 5) Candidate causal graph nodes (grouped by type; ontology grounding suggestions)

#### 5.1 Phenotype and process nodes
- **non motile**: METPO:1000703 (given)
- **bacterial-type flagellum-dependent cell motility**: GO:0009288 (candidate)
- **bacterial-type flagellum organization / biogenesis**: (GO terms likely; keep label if uncertain)
- **chemotaxis signaling / flagellar rotation bias**: (label; keep mechanistic separation from motility apparatus) (liu2024counterclockwiserotationof pages 1-2, wang2024argrregulatesmotility pages 1-2)

#### 5.2 Structural apparatus nodes (genes/proteins; ground where possible)
- Flagellar master/regulatory module: **flhDC** (label; master operon in Enterobacteriaceae) (dai2024acdigmpbinding pages 5-8, zhang2024anovelregulator pages 1-2)
- Flagellar structural/assembly genes (labels; curate as gene families/operons when taxon-agnostic): **flhA, flhB, flhC, flhD**, **fliC**, **flgP/flgQ**, etc. (cohen2023evolutionofa pages 9-12, esteves2023phagesonfilaments pages 9-11, carter2024conditionalexpressionof pages 1-2)
- Motor/stator: **MotAB** / **MotB** (label; stator complex) (liu2024counterclockwiserotationof pages 1-2)
- Flagellar localization: **FlhF** (label) (guan2024flhfaffectsthe pages 1-2)

#### 5.3 Regulatory nodes
- **c-di-GMP**: (CHEBI grounding not confirmed in evidence; keep label) (dai2024acdigmpbinding pages 1-2, oladosu2024fliptheswitch pages 4-7)
- c-di-GMP effectors and enzymes:
  - **STM0435 (YajQ family)** (label) (dai2024acdigmpbinding pages 1-2, dai2024acdigmpbinding pages 8-10)
  - **WspR** (diguanylate cyclase) (label) (guan2024flhfaffectsthe pages 1-2)
- Transcription factors / regulators:
  - **FleQ** (flagellar/biofilm transcriptional regulator, *Pseudomonas*) (oladosu2024fliptheswitch pages 4-7, oladosu2024fliptheswitch media 9db214e5)
  - **CdsR** (motility repressor in *Bacillus thuringiensis*) (zhang2024anovelregulator pages 1-2, zhang2024anovelregulator pages 4-6)
  - **ArgR** (motility/virulence regulator in *Aeromonas veronii*) (wang2024argrregulatesmotility pages 1-2)
  - **OmpR** (response regulator; repression of flhDC described as precedent) (zhang2024anovelregulator pages 1-2, hu2024rolesofresponse pages 1-2)

#### 5.4 Environmental / experimental factor nodes
- **Cu(II)**: CHEBI:23367 copper(2+) ion (supported) (zhang2024anovelregulator pages 1-2)
- **Medium composition** nodes (labels): LB; 5% TSB; pond water + 10% pigeon droppings (carter2024conditionalexpressionof pages 1-2)
- **Assays** (labels): soft-agar swimming; surface swarming/spreading; adsorption assays (ranta2024fenkokae01isa pages 1-2, esteves2023phagesonfilaments pages 9-11)

### 6) Evidence-backed candidate causal edges (curation table)
The following artifact consolidates candidate edges as subject–predicate–object triples with direct snippets, DOI-first references, and curation notes.

| Edge (subject–predicate–object) | Mechanistic entity types (S/O types) | Suggested ontology grounding (CURIEs when available; otherwise labels) | Evidence (paper citation with DOI, year, URL) | Supporting snippet (short quote) | Notes on certainty/scope (taxon/assay/regulatory vs structural) |
|---|---|---|---|---|---|
| deletion of **flhABCD** → causes reduced/absent motility → **non-motile phenotype** | gene set → phenotype | flhA/flhB/flhC/flhD (labels); GO:0044781 bacterial-type flagellum organization; METPO:1000703 | Carter et al., 2024, *Frontiers in Microbiology*, DOI:10.3389/fmicb.2024.1456637, https://doi.org/10.3389/fmicb.2024.1456637 | “Additional deletion of motility genes **flhABCD** and motBC was identified in several E. albertii strains.” | Structural inference from natural strain variation; phenotype is condition-dependent in *E. albertii*, so curate as likely/strain-specific rather than universal. (carter2024conditionalexpressionof pages 1-2) |
| deletion of **motBC** → impairs flagellar motor function → **non-motile phenotype** | motor/stator genes → phenotype | motB/motC (labels); GO:0009288 bacterial-type flagellum-dependent cell motility; METPO:1000703 | Carter et al., 2024, *Frontiers in Microbiology*, DOI:10.3389/fmicb.2024.1456637, https://doi.org/10.3389/fmicb.2024.1456637 | “Additional deletion of motility genes flhABCD and **motBC** was identified in several E. albertii strains.” | Likely causal because Mot proteins power rotation, but excerpt gives genotype-phenotype association across isolates rather than a clean knockout test. (carter2024conditionalexpressionof pages 1-2) |
| disruptive mutation in **fliC D2/D3 domains** → causes loss of flagellar function → **non-motile phenotype** | structural protein domain variant → phenotype | fliC (label); GO:0009288; METPO:1000703 | Esteves et al., 2023, *PLOS Pathogens*, DOI:10.1371/journal.ppat.1011537, https://doi.org/10.1371/journal.ppat.1011537 | “Several chimeric and domain-deletion mutants were **non-motile**… yet immunoblots show these strains still produce variant FliC proteins.” | Strong direct mutational evidence; taxon-specific to *Salmonella enterica* flagellin-domain engineering. (esteves2023phagesonfilaments pages 9-11, esteves2023phagesonfilaments pages 16-18) |
| deletion of **flgPQ** (basal disk components) → causes motility defect/non-motility → **non-motile phenotype** | assembly/structural genes → phenotype | flgP/flgQ (labels); GO:0044781; METPO:1000703 | Cohen et al., 2023, bioRxiv, DOI:10.1101/2023.09.08.556628, https://doi.org/10.1101/2023.09.08.556628 | “deletion of **flgPQ** produces a **non-motile phenotype** on motility agar” | Strong experimental evidence in Campylobacterota motor architecture; occasional residual rotating flagella means assay readout is migration/non-migration, not absolute absence of rotation. (cohen2023evolutionofa pages 9-12) |
| knockout of **pseG** → disrupts flagellar glycosylation/assembly → **non-motile phenotype** | glycosylation gene → phenotype | pseG (label); GO:0044781; METPO:1000703 | Cohen et al., 2023, bioRxiv, DOI:10.1101/2023.09.08.556628, https://doi.org/10.1101/2023.09.08.556628 | “A **pseG knockout is non-motile**” | Strong direct evidence; mechanism likely via altered O-glycosylation of flagellar structures. Taxon-specific. (cohen2023evolutionofa pages 9-12) |
| deletion of **flhF** → mislocalizes flagella / elevates c-di-GMP network output → diminished motility or **non-motile phenotype** | GTPase/localization factor → phenotype | flhF (label); GO:0044781; METPO:1000703 | Guan et al., 2024, *Applied and Environmental Microbiology*, DOI:10.1128/aem.01548-23, https://doi.org/10.1128/aem.01548-23 | “its deletion yields lateral flagella, ‘**diminished motility**,’ and a **non-motile ΔflhF mutant** with elevated biofilm” | Strong direct evidence in *Pseudomonas aeruginosa*; mixed structural/regulatory mechanism. (guan2024flhfaffectsthe pages 1-2, guan2024flhfaffectsthe pages 2-6) |
| mutations disrupting **flagellum biogenesis** → abolish flagellar function → **non-motile, phage-resistant phenotype** | flagellar biogenesis loci → phenotype | bacterial flagellum biogenesis (label); GO:0044780; METPO:1000703 | Ranta et al., 2024, *BMC Microbiology*, DOI:10.1186/s12866-024-03387-1, https://doi.org/10.1186/s12866-024-03387-1 | “flagellum biogenesis was affected in four mutants and the lack of functional flagellum was confirmed in motility assays” | Strong selection experiment in *Klebsiella aerogenes*; good evidence for loss-of-function flagellar mutations causing non-motility. Gene-level identity not supplied in excerpt. (ranta2024fenkokae01isa pages 1-2) |
| high intracellular **c-di-GMP** → represses flagellar genes/motility → **reduced motility / non-motile state** | second messenger → phenotype | CHEBI: not confirmed; cyclic di-GMP (label); GO:0009288; METPO:1000703 | Oladosu et al., 2024, *Journal of Bacteriology*, DOI:10.1128/jb.00365-23, https://doi.org/10.1128/jb.00365-23 | “At high c-di-GMP, FleQ ceases to activate flagellar genes” | Broad regulatory mechanism, especially strong in *Pseudomonas aeruginosa*; usually yields reduced motility rather than necessarily absolute non-motility. (oladosu2024fliptheswitch pages 4-7, oladosu2024fliptheswitch pages 3-4, oladosu2024fliptheswitch media 9db214e5) |
| **STM0435** binds **c-di-GMP** → inhibits flagellar biogenesis → reduced motility | c-di-GMP effector protein → process | STM0435 (label); cyclic di-GMP (label); flagellar biogenesis (label) | Dai et al., 2024, *Virulence*, DOI:10.1080/21505594.2024.2331265, https://doi.org/10.1080/21505594.2024.2331265 | “STM0435 binds c-di-GMP… indicating that the binding of c-di-GMP to STM0435 promotes its inhibitory effect on Salmonella flagellar biogenesis.” | Strong direct mechanistic evidence; taxon-specific to *Salmonella*. Suitable regulatory edge. (dai2024acdigmpbinding pages 1-2, dai2024acdigmpbinding pages 8-10) |
| overexpression/activity of **WspR** diguanylate cyclase → increases **c-di-GMP** → represses motility | enzyme activity → second messenger | WspR (label); cyclic di-GMP (label) | Guan et al., 2024, *Applied and Environmental Microbiology*, DOI:10.1128/aem.01548-23, https://doi.org/10.1128/aem.01548-23 | “WspR… ‘produces c-di-GMP when phosphorylated’” and high c-di-GMP “represses motility.” | Indirect but strong pathway evidence in *P. aeruginosa*; curate as regulatory cascade rather than direct non-motile edge. (guan2024flhfaffectsthe pages 1-2, guan2024flhfaffectsthe pages 2-6) |
| **ArgR** represses diguanylate cyclase expression → lowers **c-di-GMP** → increases motility | transcription factor → enzyme expression / phenotype | ArgR (label); diguanylate cyclase (label); cyclic di-GMP (label) | Wang et al., 2024, *Communications Biology*, DOI:10.1038/s42003-024-07392-y, https://doi.org/10.1038/s42003-024-07392-y | “ArgR inhibited the expression of diguanylate cyclase, leading to reduced c-di-GMP levels” | Positive-control edge for motility; useful inverse logic for non-motile graph because loss of ArgR can shift toward low motility. Taxon-specific to *Aeromonas veronii*. (wang2024argrregulatesmotility pages 1-2) |
| **CdsR** represses **motAB1 / che / fla** operons → decreases motility | transcriptional regulator → operons/process | CdsR (label); motAB1, cheY-yrhK, cheV-mogR, hag1/hag2, yjbJ-flgG (labels) | Zhang et al., 2024, *Scientific Reports*, DOI:10.1038/s41598-024-76694-2, https://doi.org/10.1038/s41598-024-76694-2 | “Mutation of cdsR results in increase of cell mobility” and CdsR “directly regulates the motAB1… cheV-mogR… hag1… hag2…” | Strong direct regulatory evidence; represses multiple motility loci in *Bacillus thuringiensis*. Degree of effect may be reduced motility rather than fully non-motile. (zhang2024anovelregulator pages 1-2, zhang2024anovelregulator pages 4-6) |
| **Cu(II)** inhibits **CdsR** promoter binding → derepresses motility genes → increases motility potential | metal ion → regulator activity | CHEBI:23367 copper(2+) ion; CdsR (label) | Zhang et al., 2024, *Scientific Reports*, DOI:10.1038/s41598-024-76694-2, https://doi.org/10.1038/s41598-024-76694-2 | “CdsR is a metalloregulator and the binding to promoter can be inhibited by **Cu (II) ions**.” | Strong biochemical evidence; phenotype effect is inferred through direct promoter-binding inhibition plus known negative regulatory role of CdsR. (zhang2024anovelregulator pages 1-2) |
| **OmpR** represses **flhDC** transcription → decreases flagellar gene expression / motility | response regulator → master regulator operon | OmpR (label); flhDC (label) | Zhang et al., 2024, *Scientific Reports* (citing prior work), DOI:10.1038/s41598-024-76694-2, https://doi.org/10.1038/s41598-024-76694-2; Hu et al., 2024, *Foods*, DOI:10.3390/foods13223709, https://doi.org/10.3390/foods13223709 | “OmpR… binds to specific sequences in the **flhDC operon promoter and represses** transcription in *E. coli*.” | Good mechanistic precedent, but evidence here is partly review/citation of earlier work rather than a 2024 direct experiment; curate as background regulator edge with moderate certainty. (zhang2024anovelregulator pages 1-2, hu2024rolesofresponse pages 1-2) |
| medium **5% TSB** → induces swimming motility in some *E. albertii* strains → reverses apparent non-motile assay outcome | environmental factor → phenotype | 5% TSB (label); METPO:1000703 | Carter et al., 2024, *Frontiers in Microbiology*, DOI:10.3389/fmicb.2024.1456637, https://doi.org/10.3389/fmicb.2024.1456637 | “when grown in **5% TSB**… an additional four strains became motile” | Important assay/environment boundary case: absence of motility in LB may not be constitutive non-motility. (carter2024conditionalexpressionof pages 1-2) |
| **pond water + 10% pigeon droppings** → induces swimming motility in some *E. albertii* strains → reverses apparent non-motile assay outcome | environmental factor → phenotype | pond water supplemented with pigeon droppings (label); METPO:1000703 | Carter et al., 2024, *Frontiers in Microbiology*, DOI:10.3389/fmicb.2024.1456637, https://doi.org/10.3389/fmicb.2024.1456637 | “in the **pond water-supplemented with 10% pigeon droppings**, an additional four strains became motile” | Strong evidence that “non-motile” can be medium-specific and should not be over-curated as absolute. (carter2024conditionalexpressionof pages 1-2) |
| absence of **21 core flagellar genes** → predicts **nonflagellated** state (proxy for non-motile) | genome content signature → trait class | core flagellar genes incl. FlaE, FliL, Flg_bbr_C, Flg_bb_rod, FliG_C, FlgD, Flg_hook, FliD_C, FliE, YscJ_FliF_C (labels) | Ramoneda et al., 2024, *The ISME Journal*, DOI:10.1093/ismejo/wrae067, https://doi.org/10.1093/ismejo/wrae067 | “presence/absence of 21 genes… correctly called **nonflagellated taxa in 94.5% of cases**” | Useful comparative-genomics proxy, but not equivalent to non-motile because some nonflagellated taxa use other motility modes. Curate cautiously. (ramoneda2024ecologicalrelevanceof pages 5-6, ramoneda2024ecologicalrelevanceof pages 2-3) |
| **nonflagellated state** ≠ **non-motile phenotype** because alternative motility exists | trait-class distinction → trait-class distinction | nonflagellated (label); non-motile (METPO:1000703); gliding motility (label) | Ramoneda et al., 2024, *The ISME Journal*, DOI:10.1093/ismejo/wrae067, https://doi.org/10.1093/ismejo/wrae067 | “nonflagellated does not equal nonmotile (e.g., **gliding in Bacteroidota**)” | Boundary/negative curation edge; important warning against overusing absence of flagellar genes as definitive non-motile evidence. Prevalence context in same study: predicted flagellar capacity across 26,192 genomes, including Bacteroidota 0.7% and Proteobacteria 78.3%. (ramoneda2024ecologicalrelevanceof pages 5-6, ramoneda2024ecologicalrelevanceof pages 2-3) |


*Table: This table compiles candidate causal edges for the non-motile microbial trait, covering structural gene disruptions, regulatory pathways, environmental modulation, and comparative-genomic proxies. It is designed to support TraitMech curation by linking each edge to recent evidence and scope notes.*

### 7) Curation warnings (do-not-curate yet / curate with uncertainty flags)
1. **Avoid equating “nonflagellated” with METPO:1000703:** The 2024 comparative genomics framework explicitly warns that nonflagellated does not equal nonmotile (gliding motility in Bacteroidota), so “absence of flagellar genes” should be curated as “absence of flagellar motility apparatus” (or “nonflagellated”) unless phenotype is directly observed. (ramoneda2024ecologicalrelevanceof pages 5-6)
2. **Environment-dependent motility requires assay qualifiers:** Some *E. albertii* strains scored non-motile in LB but became motile in 5% TSB or pond water + droppings; curations should be conditional (assay medium, temperature, etc.) when evidence indicates conditionality. (carter2024conditionalexpressionof pages 1-2)
3. **Regulatory edges often imply reduced motility, not absolute non-motility:** c-di-GMP/FleQ regulation and transcriptional repressors (e.g., CdsR) frequently describe repression/defects rather than complete non-motility; represent these as quantitative/conditional where possible. (oladosu2024fliptheswitch pages 4-7, zhang2024anovelregulator pages 4-6)
4. **Some sources are preprints:** e.g., Cohen et al. 2023 is bioRxiv; keep uncertainty flag or corroborate with peer-reviewed follow-up before promoting to “high confidence,” especially for novel structural interpretations. (cohen2023evolutionofa pages 9-12)

---

## DOI-first bibliography (with publication dates and URLs where available)
- Zhang X. et al. (2024-10). *A novel regulator CdsR negatively regulates cell motility in Bacillus thuringiensis.* Scientific Reports. DOI:10.1038/s41598-024-76694-2. https://doi.org/10.1038/s41598-024-76694-2 (zhang2024anovelregulator pages 1-2, zhang2024anovelregulator pages 4-6)
- Dai Y. et al. (2024-03). *A c-di-GMP binding effector STM0435 modulates flagellar motility and pathogenicity in Salmonella.* Virulence. DOI:10.1080/21505594.2024.2331265. https://doi.org/10.1080/21505594.2024.2331265 (dai2024acdigmpbinding pages 1-2, dai2024acdigmpbinding pages 8-10)
- Guan C. et al. (2024-01). *FlhF affects the subcellular clustering of WspR through HsbR in Pseudomonas aeruginosa.* Applied and Environmental Microbiology. DOI:10.1128/aem.01548-23. https://doi.org/10.1128/aem.01548-23 (guan2024flhfaffectsthe pages 1-2, guan2024flhfaffectsthe pages 2-6)
- Oladosu V.I. et al. (2024-03). *Flip the switch: the role of FleQ in modulating the transition between the free-living and sessile mode of growth in Pseudomonas aeruginosa.* Journal of Bacteriology. DOI:10.1128/jb.00365-23. https://doi.org/10.1128/jb.00365-23 (oladosu2024fliptheswitch pages 4-7, oladosu2024fliptheswitch media 9db214e5)
- Carter M.Q. et al. (2024-09). *Conditional expression of flagellar motility, curli fimbriae, and biofilms in Shiga toxin-producing Escherichia albertii.* Frontiers in Microbiology. DOI:10.3389/fmicb.2024.1456637. https://doi.org/10.3389/fmicb.2024.1456637 (carter2024conditionalexpressionof pages 1-2)
- Ranta K. et al. (2024-07). *fENko-Kae01 is a flagellum-specific jumbo phage infecting Klebsiella aerogenes.* BMC Microbiology. DOI:10.1186/s12866-024-03387-1. https://doi.org/10.1186/s12866-024-03387-1 (ranta2024fenkokae01isa pages 1-2)
- Ramoneda J. et al. (2024-01). *Ecological relevance of flagellar motility in soil bacterial communities.* The ISME Journal. DOI:10.1093/ismejo/wrae067. https://doi.org/10.1093/ismejo/wrae067 (ramoneda2024ecologicalrelevanceof pages 5-6, ramoneda2024ecologicalrelevanceof pages 2-3)
- Liu X. et al. (2024-06). *Counterclockwise rotation of the flagellum promotes biofilm initiation in Helicobacter pylori.* mBio. DOI:10.1128/mbio.00440-24. https://doi.org/10.1128/mbio.00440-24 (liu2024counterclockwiserotationof pages 1-2)
- Esteves N.C. et al. (2023-08). *Phages on filaments: A genetic screen elucidates the complex interactions between Salmonella enterica flagellin and bacteriophage Chi.* PLOS Pathogens. DOI:10.1371/journal.ppat.1011537. https://doi.org/10.1371/journal.ppat.1011537 (esteves2023phagesonfilaments pages 9-11, esteves2023phagesonfilaments pages 16-18)
- Cohen E.J. et al. (2023-09). *Evolution of a large periplasmic disk in Campylobacterota flagella facilitated efficient motility alongside autoagglutination.* bioRxiv. DOI:10.1101/2023.09.08.556628. https://doi.org/10.1101/2023.09.08.556628 (cohen2023evolutionofa pages 9-12)
- Hu M. et al. (2024-11). *Roles of Response Regulators in the Two-Component System in the Formation of Stress Tolerance, Motility and Biofilm in Salmonella Enteritidis.* Foods. DOI:10.3390/foods13223709. https://doi.org/10.3390/foods13223709 (hu2024rolesofresponse pages 1-2)
- Wang Z. et al. (2024-12). *ArgR regulates motility and virulence through positive control of flagellar genes and inhibition of diguanylate cyclase expression in Aeromonas veronii.* Communications Biology. DOI:10.1038/s42003-024-07392-y. https://doi.org/10.1038/s42003-024-07392-y (wang2024argrregulatesmotility pages 1-2)


References

1. (carter2024conditionalexpressionof pages 1-2): Michelle Qiu Carter, Diana Carychao, and Rebecca L. Lindsey. Conditional expression of flagellar motility, curli fimbriae, and biofilms in shiga toxin- producing escherichia albertii. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1456637, doi:10.3389/fmicb.2024.1456637. This article has 8 citations and is from a peer-reviewed journal.

2. (ranta2024fenkokae01isa pages 1-2): Kira Ranta, Mikael Skurnik, and Saija Kiljunen. Fenko-kae01 is a flagellum-specific jumbo phage infecting klebsiella aerogenes. BMC Microbiology, Jul 2024. URL: https://doi.org/10.1186/s12866-024-03387-1, doi:10.1186/s12866-024-03387-1. This article has 6 citations and is from a peer-reviewed journal.

3. (ramoneda2024ecologicalrelevanceof pages 5-6): Josep Ramoneda, Kunkun Fan, Jane M Lucas, Haiyan Chu, Andrew Bissett, Michael S Strickland, and Noah Fierer. Ecological relevance of flagellar motility in soil bacterial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae067, doi:10.1093/ismejo/wrae067. This article has 37 citations.

4. (ramoneda2024ecologicalrelevanceof pages 2-3): Josep Ramoneda, Kunkun Fan, Jane M Lucas, Haiyan Chu, Andrew Bissett, Michael S Strickland, and Noah Fierer. Ecological relevance of flagellar motility in soil bacterial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae067, doi:10.1093/ismejo/wrae067. This article has 37 citations.

5. (liu2024counterclockwiserotationof pages 1-2): Xiaolin Liu, Paphavee Lertsethtakarn, Vanessa T. Mariscal, Fitnat Yildiz, and Karen M. Ottemann. Counterclockwise rotation of the flagellum promotes biofilm initiation in <i>helicobacter pylori</i>. Jun 2024. URL: https://doi.org/10.1128/mbio.00440-24, doi:10.1128/mbio.00440-24. This article has 22 citations and is from a domain leading peer-reviewed journal.

6. (wang2024argrregulatesmotility pages 1-2): Zucheng Wang, Yanqiong Tang, Hong Li, Juanjuan Li, Xue Chi, Xiang Ma, and Zhu Liu. Argr regulates motility and virulence through positive control of flagellar genes and inhibition of diguanylate cyclase expression in aeromonas veronii. Communications Biology, Dec 2024. URL: https://doi.org/10.1038/s42003-024-07392-y, doi:10.1038/s42003-024-07392-y. This article has 5 citations and is from a peer-reviewed journal.

7. (esteves2023phagesonfilaments pages 9-11): Nathaniel C. Esteves, Danielle N. Bigham, and Birgit E. Scharf. Phages on filaments: a genetic screen elucidates the complex interactions between salmonella enterica flagellin and bacteriophage chi. PLOS Pathogens, 19:e1011537, Aug 2023. URL: https://doi.org/10.1371/journal.ppat.1011537, doi:10.1371/journal.ppat.1011537. This article has 11 citations and is from a highest quality peer-reviewed journal.

8. (cohen2023evolutionofa pages 9-12): Eli J. Cohen, Tina Drobnič, Deborah A. Ribardo, Aoba Yoshioka, Trishant Umrekar, Xuefei Guo, Jose-Jesus Fernandez, Emma Brock, Laurence Wilson, Daisuke Nakane, David R. Hendrixson, and Morgan Beeby. Evolution of a large periplasmic disk in campylobacterota flagella facilitated efficient motility alongside autoagglutination. bioRxiv, Sep 2023. URL: https://doi.org/10.1101/2023.09.08.556628, doi:10.1101/2023.09.08.556628. This article has 1 citations.

9. (oladosu2024fliptheswitch pages 4-7): Victoria I. Oladosu, Soyoung Park, and Karin Sauer. Flip the switch: the role of fleq in modulating the transition between the free-living and sessile mode of growth in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Mar 2024. URL: https://doi.org/10.1128/jb.00365-23, doi:10.1128/jb.00365-23. This article has 27 citations and is from a peer-reviewed journal.

10. (dai2024acdigmpbinding pages 1-2): Yuanji Dai, Ruirui Liu, Ying-ying Yue, Nannan Song, Haihong Jia, Zhongrui Ma, Xueyan Gao, Min Zhang, Xilu Yuan, Qing Liu, Xiaoyu Liu, Bingqing Li, and Weiwei Wang. A c-di-gmp binding effector stm0435 modulates flagellar motility and pathogenicity in salmonella. Virulence, Mar 2024. URL: https://doi.org/10.1080/21505594.2024.2331265, doi:10.1080/21505594.2024.2331265. This article has 8 citations and is from a peer-reviewed journal.

11. (dai2024acdigmpbinding pages 8-10): Yuanji Dai, Ruirui Liu, Ying-ying Yue, Nannan Song, Haihong Jia, Zhongrui Ma, Xueyan Gao, Min Zhang, Xilu Yuan, Qing Liu, Xiaoyu Liu, Bingqing Li, and Weiwei Wang. A c-di-gmp binding effector stm0435 modulates flagellar motility and pathogenicity in salmonella. Virulence, Mar 2024. URL: https://doi.org/10.1080/21505594.2024.2331265, doi:10.1080/21505594.2024.2331265. This article has 8 citations and is from a peer-reviewed journal.

12. (zhang2024anovelregulator pages 1-2): Xin Zhang, Yuhan Chen, Yabin Liu, Lili Gang, Tinglu Yan, Hengjie Wang, Qi Peng, Jie Li, and Fuping Song. A novel regulator cdsr negatively regulates cell motility in bacillus thuringiensis. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-76694-2, doi:10.1038/s41598-024-76694-2. This article has 2 citations and is from a peer-reviewed journal.

13. (oladosu2024fliptheswitch media 9db214e5): Victoria I. Oladosu, Soyoung Park, and Karin Sauer. Flip the switch: the role of fleq in modulating the transition between the free-living and sessile mode of growth in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Mar 2024. URL: https://doi.org/10.1128/jb.00365-23, doi:10.1128/jb.00365-23. This article has 27 citations and is from a peer-reviewed journal.

14. (guan2024flhfaffectsthe pages 1-2): Congcong Guan, Yi Huang, Yun Zhou, Yuqian Han, Shuhui Liu, Shimin Liu, Weina Kong, Tietao Wang, and Yani Zhang. Flhf affects the subcellular clustering of wspr through hsbr in <i>pseudomonas aeruginosa</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01548-23, doi:10.1128/aem.01548-23. This article has 13 citations and is from a peer-reviewed journal.

15. (guan2024flhfaffectsthe pages 2-6): Congcong Guan, Yi Huang, Yun Zhou, Yuqian Han, Shuhui Liu, Shimin Liu, Weina Kong, Tietao Wang, and Yani Zhang. Flhf affects the subcellular clustering of wspr through hsbr in <i>pseudomonas aeruginosa</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01548-23, doi:10.1128/aem.01548-23. This article has 13 citations and is from a peer-reviewed journal.

16. (hu2024rolesofresponse pages 1-2): Mengjun Hu, Zhuoan Zhou, Chenqi Liu, Zeqiang Zhan, Yan Cui, Shoukui He, and Xianming Shi. Roles of response regulators in the two-component system in the formation of stress tolerance, motility and biofilm in salmonella enteritidis. Foods, 13:3709, Nov 2024. URL: https://doi.org/10.3390/foods13223709, doi:10.3390/foods13223709. This article has 6 citations.

17. (dai2024acdigmpbinding pages 5-8): Yuanji Dai, Ruirui Liu, Ying-ying Yue, Nannan Song, Haihong Jia, Zhongrui Ma, Xueyan Gao, Min Zhang, Xilu Yuan, Qing Liu, Xiaoyu Liu, Bingqing Li, and Weiwei Wang. A c-di-gmp binding effector stm0435 modulates flagellar motility and pathogenicity in salmonella. Virulence, Mar 2024. URL: https://doi.org/10.1080/21505594.2024.2331265, doi:10.1080/21505594.2024.2331265. This article has 8 citations and is from a peer-reviewed journal.

18. (zhang2024anovelregulator pages 4-6): Xin Zhang, Yuhan Chen, Yabin Liu, Lili Gang, Tinglu Yan, Hengjie Wang, Qi Peng, Jie Li, and Fuping Song. A novel regulator cdsr negatively regulates cell motility in bacillus thuringiensis. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-76694-2, doi:10.1038/s41598-024-76694-2. This article has 2 citations and is from a peer-reviewed journal.

19. (esteves2023phagesonfilaments pages 16-18): Nathaniel C. Esteves, Danielle N. Bigham, and Birgit E. Scharf. Phages on filaments: a genetic screen elucidates the complex interactions between salmonella enterica flagellin and bacteriophage chi. PLOS Pathogens, 19:e1011537, Aug 2023. URL: https://doi.org/10.1371/journal.ppat.1011537, doi:10.1371/journal.ppat.1011537. This article has 11 citations and is from a highest quality peer-reviewed journal.

20. (oladosu2024fliptheswitch pages 3-4): Victoria I. Oladosu, Soyoung Park, and Karin Sauer. Flip the switch: the role of fleq in modulating the transition between the free-living and sessile mode of growth in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Mar 2024. URL: https://doi.org/10.1128/jb.00365-23, doi:10.1128/jb.00365-23. This article has 27 citations and is from a peer-reviewed journal.