---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T12:19:27.175599'
end_time: '2026-08-04T12:25:37.329319'
duration_seconds: 370.15
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: phenotype
  trait_identifier: METPO:1000059
  trait_category: UPPER
  trait_category_slug: upper
  trait_slug: phenotype
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A quality that differentiates specific instances of a species from other
    instances of the same species.
  parent_traits: METPO:1000188
  synonyms: ''
  evidence_summary: 'DOI:10.1186/gb-2010-11-1-r2: entity that is observed to be affected
    (Supports phenotype representation through entity-quality descriptions.) | DOI:10.1186/gb-2010-11-1-r2:
    specific characteristic or quality of that entity affected (Supports phenotype
    as an observed quality of an entity.)'
  causal_graph_summary: 'phenotype_quality_child_context: 5 nodes, 4 edges'
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
- **Trait label:** phenotype
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000059
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that differentiates specific instances of a species from other instances of the same species.
- **Parent traits:** METPO:1000188
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/gb-2010-11-1-r2: entity that is observed to be affected (Supports phenotype representation through entity-quality descriptions.) | DOI:10.1186/gb-2010-11-1-r2: specific characteristic or quality of that entity affected (Supports phenotype as an observed quality of an entity.)
- **Existing causal graph summary:** phenotype_quality_child_context: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **phenotype** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/phenotype.yaml`.

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
- **Trait label:** phenotype
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000059
- **Trait category:** UPPER
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that differentiates specific instances of a species from other instances of the same species.
- **Parent traits:** METPO:1000188
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/gb-2010-11-1-r2: entity that is observed to be affected (Supports phenotype representation through entity-quality descriptions.) | DOI:10.1186/gb-2010-11-1-r2: specific characteristic or quality of that entity affected (Supports phenotype as an observed quality of an entity.)
- **Existing causal graph summary:** phenotype_quality_child_context: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **phenotype** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/upper/phenotype.yaml`.

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


# Curation report: microbial phenotype (`METPO:1000059`)

## Executive curation recommendation

`METPO:1000059` should remain a **broad upper-level phenotype class**, not be assigned one universal biochemical pathway. Its supplied definition—“A quality that differentiates specific instances of a species from other instances of the same species”—is compatible with entity–quality (EQ) modeling: a microbial entity, structure, or process **bears a quality** whose state differs among instances. Contemporary phenotype modeling likewise treats phenotype as an outcome of genetic endowment interacting with environmental conditions over time. (thessen2020transformingthestudy pages 8-11, thessen2020transformingthestudy pages 11-12, thessen2020transformingthestudy pages 1-2)

For `data/traits/upper/phenotype.yaml`, the safest graph is therefore a small schema-level graph connecting **biological entity → quality → phenotype representation**, with genotype, environment, and time/context as contributors. Specific genes, nutrients, pathways, drugs, and instruments belong in contextual exemplar subgraphs or narrower child traits, not as universal causes of phenotype.

## 1. Scope and boundaries

### Intended scope

The target denotes an **observable or inferable quality of a microbial instance**—cell, strain, isolate, or population—that distinguishes it from another instance of the same species. Examples include cell morphology, colony morphology, growth rate, substrate-utilization state, metabolite-production level, antimicrobial susceptibility, stress robustness, motility, and a differentiated cell state. EQ models can use anatomical entities, biological processes, or physiological entities, and can represent qualitative states or be extended with quantitative measurements. (thessen2020transformingthestudy pages 2-4, thessen2020transformingthestudy pages 8-11)

At the class level, `METPO:1000059` identifies the kind of quality. At the assertion level, a curator should record the bearer, quality/state, organism or strain, environment, assay, time point, and—when quantitative—the value and unit. This reflects the distinction between terminological classes and instance-specific assertions and the need to retain microbial origin and treatment metadata. (thessen2020transformingthestudy pages 7-8)

### Nearby concepts that should remain distinct

- **Trait/character:** the dimension being compared, such as growth rate or cell length. A **phenotype** is the state manifested by an instance, such as reduced growth rate or elongated cells.
- **Physiological capacity:** a potential ability, such as growth using cellobiose. It becomes an observed phenotype only under stated conditions and an appropriate assay.
- **Environmental preference:** a pattern of comparatively better occurrence or performance across environments. Presence in one environment does not by itself establish preference.
- **Assay result or measurement value:** an information artifact about a phenotype, not the phenotype itself. Measurement models should preserve who, how, when, and where the observation was made. (thessen2020transformingthestudy pages 5-7, thessen2020transformingthestudy pages 12-14)
- **Fitness:** performance or reproductive success in a specified environment. In yeast phenomics, fitness was explicitly distinguished from robustness. (trivellin2024robustnessquantificationof pages 1-2)
- **Robustness:** stability of one or more phenotypes across perturbations, rather than the value of a phenotype in one environment. It can be high even when absolute fitness is low. (trivellin2024robustnessquantificationof pages 1-2, trivellin2024robustnessquantificationof pages 10-11)
- **Genotype or gene presence:** a possible determinant or predictor, not itself a phenotype. Incomplete penetrance and environmental dependence preclude automatically converting genotype associations into phenotype-causation edges. (yu2024decipheringcomplexantibiotic pages 1-2)

### Boundary cases

Population-average phenotypes can conceal distinct states among genetically identical cells. A 2024 review notes that bacterial populations often contain mixtures of phenotypic responses and identifies transcriptional heterogeneity as a principal driver of distinct cell states. Consequently, population, subpopulation, and single-cell phenotypes should not be merged without an aggregation qualifier. (walls2024bacterialphenotypicheterogeneity pages 1-2)

Similarly, morphology, Raman spectrum, optical density, colony size, and MIC are not interchangeable. Morphology is a quality; a Raman spectrum is an assay output reflecting biomolecular composition; colony size is a measurement proxy; and MIC is an operational susceptibility endpoint defined by a protocol.

## 2. Candidate nodes grouped by type

### Core ontology/schema nodes

| Node | Suggested grounding | Curation role |
|---|---|---|
| phenotype | `METPO:1000059` | Target class; quote exactly in YAML. |
| parent trait | `METPO:1000188` | Supplied parent; retain unless ontology review indicates otherwise. |
| biological entity / microbial bearer | Label-only unless the bearer is specified | The cell, strain, isolate, population, structure, or process bearing the quality. |
| quality | PATO candidate; exact child CURIE should be selected for each concrete quality | EQ quality component. Do not force one PATO term onto the upper class. |
| phenotype observation | Label-only candidate | Observation event linking bearer, quality, assay, and context. |
| measurement datum | Label-only candidate | Value/unit output; distinct from phenotype. |
| genotype | Label-only candidate | Contributing biological context. |
| environment | ENVO candidate, selected per experiment | Contributing context; use precise medium, habitat, temperature, oxygen, pH, or exposure nodes when known. |
| developmental/growth phase and time point | Label-only candidates | Essential temporal context. |

### Genes, proteins, and complexes

- **MET28** and the **CBF1–MET4–MET28 transcription-factor complex**: yeast-specific candidates regulating sulfur metabolism. The 2024 study found that `met28` deletion produced the largest robustness increase but substantially reduced fitness; this is a trade-off, not a universally beneficial effect. (trivellin2024robustnessquantificationof pages 10-11)
- **TIR3, WWM1, BCH1**: candidate yeast robustness modifiers, but their effects varied with perturbation space and some mechanistic assignments remain incomplete. (trivellin2024robustnessquantificationof pages 1-2, trivellin2024robustnessquantificationof pages 10-11)
- **AMR-associated variants/loci**: use only when a study establishes the exact organism, allele, drug, and assay. The retrieved *H. pylori* study shows that multivariant models can outperform individual known sites, warning against simplistic single-locus causation. (yu2024decipheringcomplexantibiotic pages 1-2)

No UniProt accession should be assigned without specifying species and protein record; gene symbols alone are safer at this upper level.

### Pathways, modules, and biological processes

- Gene expression and transcriptional regulation.
- Transcriptional heterogeneity and cell-state differentiation.
- Sulfur metabolism and glutathione-associated stress response in *Saccharomyces cerevisiae*.
- Central carbon catabolism/glycolysis and carbon-source utilization.
- Cell-envelope, DNA, cytoplasmic, and protein synthesis processes affected by antibiotics.
- Growth, fermentation, stress response, apoptosis/metacaspase-associated processes, and antimicrobial response.

GO, KEGG, MetaCyc, EC, and Rhea identifiers should be added only after the exact process or reaction is selected. “Central carbon metabolism” and “stress response” are too broad to ground safely to one identifier here.

### Chemicals, nutrients, drugs, and environmental factors

- Carbon sources: cellobiose, raffinose, lactose, arabinose, arbutin, glucose, galactose, and fructose. In the MASS study, substrate-predictor patterns were mapped to glycolytic entry points, but this was largely a predictive/pathway-interpretation analysis rather than direct causal intervention on every pathway step. (herbst2024multiattributesubsetselection pages 3-4)
- Organic acids, peptides, amino acids, amino sugars, temperature, and fermentation perturbation spaces.
- Antibiotic class, compound, and concentration; these must be represented with exposure duration and organism.
- Oxygen, pH, medium composition, inoculum, growth phase, and incubation time as essential experimental-context candidates.

CHEBI identifiers are appropriate for individually specified compounds, but none should be guessed from class labels or ambiguous names.

### Assays and instruments

- Biolog Phenotype MicroArrays, robotic screens, microfluidics, imaging systems, and multiplexed bioreactors are established microbial phenomics platforms. (herbst2024multiattributesubsetselection pages 1-2)
- High-content microscopy plus machine learning for antimicrobial-susceptibility prediction. (tran2024combiningmachinelearning pages 1-2)
- Raman spectroscopy plus machine learning for rapid mycobacterial resistance phenotyping. (ogunlade2024rapidantibioticincubationfree pages 1-4)
- Whole-genome sequencing plus supervised learning for genotype-to-AMR-phenotype prediction. (yu2024decipheringcomplexantibiotic pages 1-2)
- Multipad Agarose Plate imaging and MOR50 morphology-based susceptibility estimation; this evidence is currently a preprint. (kals2024antibioticschangethe pages 1-3, kals2024antibioticschangethe pages 12-14)

## 3. Candidate causal and observational edges

The following table separates broadly curatable relations from contextual examples.

| candidate subject | predicate | object | scope/status | DOI | supporting source snippet | curator note |
|---|---|---|---|---|---|---|
| genetic endowment + environmental conditions over lifetime | contributes to | phenotype | broad schema; curation candidate | 10.1371/journal.pcbi.1008376 | “organism phenotype as the product of interactions between genetic endowment and environmental conditions over lifetime” (thessen2020transformingthestudy pages 1-2) | Best high-level causal framing for METPO:1000059; broad and not microbe-specific. |
| biological entity | bears | quality | broad schema; curation candidate | 10.1371/journal.pcbi.1008376 | “The EQ Formalism… combines anatomy ontology terms (entities) with phenotype ontology terms (qualities) to represent phenotypes” (thessen2020transformingthestudy pages 11-12, thessen2020transformingthestudy pages 8-11) | Aligns with existing METPO evidence and entity-quality phenotype representation. |
| assay / measurement process | measures / reveals | phenotype | broad schema; curation candidate | 10.1371/journal.pcbi.1008376 | “The Measurement-Based quantitative phenotypes model extends the EQ Formalism to accommodate individual specimen measurements… [with] metadata about measurement processes” (thessen2020transformingthestudy pages 12-14) | Keep distinct from phenotype itself: assay output is evidence about phenotype, not the phenotype class. |
| transcriptional heterogeneity | drives | distinct cell states / phenotypic responses | exemplar 2024; mechanistic but general microbiology | 10.1080/21541264.2024.2334110 | “there is often a mixture of phenotypic responses within a bacterial population, where distinct cell types arise. A primary phenomenon driving these distinct cell states is transcriptional heterogeneity.” (walls2024bacterialphenotypicheterogeneity pages 1-2) | Good microbial exemplar edge; probably too specific to assert as universal parent of all phenotypes. |
| carbon source availability | enables / shapes | fermentation or growth phenotype under tested conditions | exemplar 2024; inferred, condition-specific | 10.1038/s42003-024-06093-w | “amino sugars are well predicted… The respective predictor conditions contain ‘neutral sugars’, ‘peptides’, and ‘amino acids’. This suggests potential overlaps in metabolic pathways for the utilization of these carbon sources.” (herbst2024multiattributesubsetselection pages 3-4) | Use cautiously: MASS primarily shows predictive structure; pathway link is inferred from substrate-to-glycolysis mapping, not directly causal proof for all microbes. |
| central carbon metabolism entry points (glycolysis-linked substrate utilization) | mediates | carbon-source-dependent phenotype patterns | exemplar 2024; inferred, condition-specific | 10.1038/s42003-024-06093-w | “We mapped the fermented carbon sources to their respective monomers… and highlighted their entries into glycolysis as part of the central carbon catabolism” (herbst2024multiattributesubsetselection pages 3-4) | Candidate mechanism node for lower-level trait graphs, not necessarily for upper-level phenotype.yaml. |
| MET28 deletion | affects | yeast robustness phenotype | exemplar 2024; taxon- and perturbation-specific | 10.1186/s12934-024-02490-2 | “We identified genes associated with increased robustness such as MET28, linked to sulfur metabolism” (trivellin2024robustnessquantificationof pages 1-2) | Specific to Saccharomyces cerevisiae and robustness phenotyping across perturbation spaces. |
| CBF1-MET4-MET28 sulfur metabolism context | influences | robustness / fitness tradeoff | exemplar 2024; taxon-specific, nuanced | 10.1186/s12934-024-02490-2 | “Met28 is part of a transcription factor complex (CBF1-MET4-MET28) that regulates sulfur metabolism… met28 caused the highest increase in robustness, but it also resulted in a substantial drop in fitness.” (trivellin2024robustnessquantificationof pages 10-11) | Important warning: deletion increased robustness while reducing fitness; do not simplify to universally beneficial effect. |
| antibiotic exposure | alters | growth-rate heterogeneity phenotype | exemplar 2024; preprint, assay-specific | 10.1101/2024.08.27.609914 | “as the drug dose approaches the MIC… a consistent increase in growth rate heterogeneity. Remarkably, drugs that affect protein synthesis consistently show the opposite trend” (kals2024antibioticschangethe pages 1-3) | Useful phenotype mechanism edge, but source is a preprint and effect depends on antibiotic class, dose, species, and assay timepoint. |
| antibiotic exposure | alters | bacterial morphology phenotype | exemplar 2024; preprint, assay-specific | 10.1101/2024.08.27.609914 | “For all of the antibiotics and species tested, we also find a striking and non-trivial correlation between morphological alterations and growth inhibition.” (kals2024antibioticschangethe pages 1-3) | Strong observational support for morphology as phenotype readout under perturbation; still context-bound and preprint. |
| Raman spectroscopy | detects | biomolecular-composition-linked phenotype signatures | exemplar 2024 application; detection edge | 10.1073/pnas.2315670121 | “Different bacterial phenotypes are characterized by unique biomolecular compositions, leading to subtle differences in their corresponding Raman spectra.” (ogunlade2024rapidantibioticincubationfree pages 1-4) | Detection/measurement edge, not causal generation of phenotype. Good application node for assay-observed phenotypes. |
| genomic variants from WGS | predict | AMR phenotype | exemplar 2024; predictive, not necessarily causal | 10.3389/fcimb.2023.1306368 | “predictive modeling using supervised learning algorithms with feature selection can yield diagnostic models with higher predictive power compared to models relying on single single-nucleotide polymorphism (SNP) sites.” (yu2024decipheringcomplexantibiotic pages 1-2) | Keep as predicts/associated with, not causes. The paper explicitly frames incomplete penetration of mutations in dictating phenotypes. |
| known resistance loci alone | do not fully determine | AMR phenotype | exemplar 2024; cautionary edge | 10.3389/fcimb.2023.1306368 | “The inaccuracy of predicting antibiotic resistance was partially attributable to incomplete penetration of mutations in dictating phenotypes.” (yu2024decipheringcomplexantibiotic pages 1-2) | Strong warning against over-curating single-variant causal edges at the upper phenotype level. |


*Table: This table summarizes broad schema-level and exemplar 2024 microbial edges relevant to curating METPO:1000059 phenotype. It is designed to help distinguish curation-ready upper-level relations from narrower, taxon-specific, assay-specific, inferred, or merely predictive claims.*

### Recommended minimal upper-level graph

1. **microbial biological entity — bears — quality**  
   This formalizes the existing entity–quality evidence and the target definition. EQ modeling is a standard computable representation for phenotypes. (thessen2020transformingthestudy pages 8-11, thessen2020transformingthestudy pages 11-12)

2. **quality of microbial biological entity — represented_as — phenotype**  
   This should be interpreted as a representation relation rather than a biochemical causal claim.

3. **genetic endowment — contributes_to — phenotype**  
   Curate together with—not independently from—environment and temporal context. Phenotype is described as the product of genotype–environment interaction over the lifetime. (thessen2020transformingthestudy pages 1-2)

4. **environmental conditions — modulate — phenotype**  
   Include medium, nutrient, drug, physical conditions, and biotic context. This is a broad causal relation, but each concrete assertion needs an organism and assay context. (thessen2020transformingthestudy pages 1-2, herbst2024multiattributesubsetselection pages 1-2)

5. **phenotype assay — measures/reveals — phenotype**  
   This is an epistemic/observational edge, not a mechanism that generates the phenotype. Measurement-based models explicitly retain process and provenance metadata. (thessen2020transformingthestudy pages 5-7, thessen2020transformingthestudy pages 12-14)

6. **phenotype observation — has context — environment/time/assay/bearer**  
   This prevents a conditional phenotype from being incorrectly treated as an intrinsic, context-free property.

### Strong contextual exemplar edges

- **Transcriptional heterogeneity — drives — distinct bacterial cell states.** The source states: “A primary phenomenon driving these distinct cell states is transcriptional heterogeneity.” This is suitable as a microbial exemplar, but not as the mechanism of every phenotype. (walls2024bacterialphenotypicheterogeneity pages 1-2)
- **MET28 deletion — affects — yeast robustness and fitness.** The effect is explicitly bidirectional in value: increased robustness accompanied by reduced fitness, and it varies by perturbation space. (trivellin2024robustnessquantificationof pages 1-2, trivellin2024robustnessquantificationof pages 10-11)
- **Antibiotic exposure — alters — bacterial morphology and growth-rate heterogeneity.** Across three species, 13 antibiotics, 11 concentrations, and 24 organism–drug combinations, effects depended on drug class, dose, species, and active growth; protein-synthesis inhibitors showed the opposite heterogeneity trend from most other drugs. This remains preprint evidence. (kals2024antibioticschangethe pages 1-3, kals2024antibioticschangethe pages 3-5, kals2024antibioticschangethe pages 7-10)

### Predictive or observational edges—not causal edges

- **Carbon-source phenotypes — predict — other substrate phenotypes.** MASS analyzed three microbial datasets; the BacDive subset contained 637 species and 46 carbon sources. Selected conditions were biologically interpretable through central-carbon pathway entry points, but predictive selection is not direct proof that one phenotype causes another. (herbst2024multiattributesubsetselection pages 1-2, herbst2024multiattributesubsetselection pages 3-4)
- **High-content image features — predict — ciprofloxacin susceptibility.** Clinical *Salmonella Typhimurium* isolates could be classified without prior ciprofloxacin exposure, demonstrating a diagnostic association rather than showing that morphology causes resistance. (tran2024combiningmachinelearning pages 1-2)
- **Raman spectral features — classify — resistance phenotype.** More than 25,000 cells were analyzed; reported accuracy was >98% for resistant-versus-susceptible classification in dried samples and approximately 79% in patient sputum, using a portable Raman microscope costing under US$5,000. The spectrum detects phenotype-linked biomolecular composition but does not cause resistance. (ogunlade2024rapidantibioticincubationfree pages 1-4)
- **WGS feature set — predicts — *H. pylori* AMR phenotype.** Among 52 strains tested against five antibiotics, models reached 66% sensitivity/100% specificity for amoxicillin resistance and 100%/100% for clarithromycin resistance. Known single sites had sensitivities of 22.2% and 87%, respectively, illustrating incomplete single-variant determination. (yu2024decipheringcomplexantibiotic pages 1-2)

## 4. Recent developments and current applications

### Condition-reducing microbial phenomics

Herbst and colleagues introduced MASS in April 2024 to identify small sets of environmental conditions that predict phenotypes under other conditions. The approach may reduce experimental burden in microbial identification and metabolic-capability mapping, addressing the continued high cost and labor of phenotype measurement relative to genome sequencing. The authors also emphasize that phenotype data support gene annotation and mechanistic-model testing. (herbst2024multiattributesubsetselection pages 1-2, herbst2024multiattributesubsetselection pages 3-4)

### Single-cell resolution

The 2024 single-cell transcriptomics review argues that bulk measurements average away rare physiological programs such as sporulation. Because bacterial mRNAs are short-lived, the transcriptome provides a near-term snapshot of cell physiology; single-cell methods can therefore resolve differentiation, ecological interactions, and isogenic phenotypic heterogeneity. (walls2024bacterialphenotypicheterogeneity pages 1-2)

### Industrial strain engineering

A 2024 yeast study analyzed phenotyping data from over 4,000 mutants, then tested 14 engineered deletions in three industrially relevant perturbation spaces. The source dataset included 4,429 unique mutants across 14 conditions. Sulfur metabolism emerged as a candidate contributor to robustness, but gene effects did not transfer uniformly between perturbation spaces. This is directly relevant to engineering stable cell factories while demonstrating why phenotype claims require environmental scope. (trivellin2024robustnessquantificationof pages 1-2, trivellin2024robustnessquantificationof pages 10-11)

### Clinical antimicrobial susceptibility testing

Recent phenotyping systems combine imaging, spectroscopy, or morphology with machine learning to shorten susceptibility testing. High-content imaging can infer ciprofloxacin susceptibility in *S. Typhimurium* isolates; Raman phenotyping offers few-to-single-cell testing without antibiotic incubation; and morphology-based MOR50 was reported to estimate MIC from a single image after 2.5 hours. The last result is promising but should remain flagged as preprint evidence. (kals2024antibioticschangethe pages 12-14, tran2024combiningmachinelearning pages 1-2, ogunlade2024rapidantibioticincubationfree pages 1-4)

## 5. Expert synthesis

The authoritative phenotype-informatics literature supports three principles for TraitMech:

1. **Phenotypes are relational and contextual.** They emerge from genetic, environmental, and temporal interactions rather than from genotype alone. (thessen2020transformingthestudy pages 1-2)
2. **Phenotype and evidence must be separated.** A quality borne by an organism is distinct from the measurement, image, spectrum, or classifier used to infer it. (thessen2020transformingthestudy pages 7-8, thessen2020transformingthestudy pages 12-14)
3. **Computability requires provenance and semantics.** Terminological ambiguity, variable granularity, heterogeneous data types, nomenclature drift, and specimen-versus-population aggregation remain major integration barriers. Formal ontologies help, but they do not compensate for missing assay, specimen, error, and environmental metadata. (thessen2020transformingthestudy pages 5-7, thessen2020transformingthestudy pages 4-5)

Accordingly, `phenotype.yaml` should function primarily as an **upper-level semantic scaffold**. Rich mechanistic chains should be curated under concrete child traits—for example, antimicrobial susceptibility, cell morphology, substrate utilization, growth rate, or robustness—where organism, exposure, pathway, and assay can be made explicit.

## 6. Warnings: claims not yet suitable for TraitMech curation

- Do not assert any individual gene, pathway, nutrient, or antibiotic as a universal cause of `METPO:1000059`.
- Do not encode **predicts**, **correlates with**, or machine-learning feature importance as **causes**.
- Do not treat assay outputs—Raman peaks, images, optical density, colony scatter, classifier labels—as phenotypes without linking them to the biological quality measured.
- Do not collapse single-cell states into population phenotype or vice versa.
- Do not curate “environmental preference” from growth in one tested condition; preference requires comparative evidence across conditions.
- Do not interpret high robustness as high fitness. The `met28` example shows increased robustness with substantially reduced fitness. (trivellin2024robustnessquantificationof pages 10-11)
- Keep the antibiotic–morphology/MOR50 edges uncertain until peer review because DOI `10.1101/2024.08.27.609914` is a bioRxiv preprint. (kals2024antibioticschangethe pages 1-3)
- Treat MASS pathway explanations as inferred: the paper maps predictive carbon sources to glycolytic entry points but does not experimentally establish every proposed mediating edge. (herbst2024multiattributesubsetselection pages 3-4)
- Do not assign UniProt, GO, CHEBI, EC, Rhea, KEGG, MetaCyc, or ENVO identifiers unless the exact species, compound, process, reaction, or environment has been verified. Label-only nodes are preferable to invented or overbroad CURIEs.
- The supplied existing DOI `10.1186/gb-2010-11-1-r2` supports EQ-style phenotype representation, but it should not be interpreted as evidence for a specific microbial biochemical mechanism.

## DOI-first bibliography

1. Thessen AE et al. **Transforming the study of organisms: Phenomic data models and knowledge bases.** *PLoS Computational Biology*. Published November 2020. DOI: [10.1371/journal.pcbi.1008376](https://doi.org/10.1371/journal.pcbi.1008376). (thessen2020transformingthestudy pages 2-4)
2. Herbst K et al. **Multi-Attribute Subset Selection enables prediction of representative phenotypes across microbial populations.** *Communications Biology*. Published April 2024. DOI: [10.1038/s42003-024-06093-w](https://doi.org/10.1038/s42003-024-06093-w). (herbst2024multiattributesubsetselection pages 1-2)
3. Walls AW, Rosenthal AZ. **Bacterial phenotypic heterogeneity through the lens of single-cell RNA sequencing.** *Transcription*. Published March 2024; accepted 19 March 2024. DOI: [10.1080/21541264.2024.2334110](https://doi.org/10.1080/21541264.2024.2334110). (walls2024bacterialphenotypicheterogeneity pages 1-2)
4. Trivellin C, Pianale LT, Olsson L. **Robustness quantification of a mutant library screen revealed key genetic markers in yeast.** *Microbial Cell Factories*. Published August 2024. DOI: [10.1186/s12934-024-02490-2](https://doi.org/10.1186/s12934-024-02490-2). (trivellin2024robustnessquantificationof pages 1-2)
5. Tran T-A et al. **Combining machine learning with high-content imaging to infer ciprofloxacin susceptibility in isolates of Salmonella Typhimurium.** *Nature Communications*. Accepted 5 June 2024. DOI: [10.1038/s41467-024-49433-4](https://doi.org/10.1038/s41467-024-49433-4). (tran2024combiningmachinelearning pages 1-2)
6. Ogunlade B et al. **Rapid, antibiotic incubation-free determination of tuberculosis drug resistance using machine learning and Raman spectroscopy.** *Proceedings of the National Academy of Sciences*. Published June 2024. DOI: [10.1073/pnas.2315670121](https://doi.org/10.1073/pnas.2315670121). (ogunlade2024rapidantibioticincubationfree pages 1-4)
7. Yu J et al. **Deciphering complex antibiotic resistance patterns in Helicobacter pylori through whole genome sequencing and machine learning.** *Frontiers in Cellular and Infection Microbiology*. Published 4 January 2024. DOI: [10.3389/fcimb.2023.1306368](https://doi.org/10.3389/fcimb.2023.1306368). (yu2024decipheringcomplexantibiotic pages 1-2)
8. Kals M et al. **Antibiotics Change the Growth Rate Heterogeneity and Morphology of Bacteria.** *bioRxiv* preprint. Published August 2024. DOI: [10.1101/2024.08.27.609914](https://doi.org/10.1101/2024.08.27.609914). (kals2024antibioticschangethe pages 1-3)

References

1. (thessen2020transformingthestudy pages 8-11): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.

2. (thessen2020transformingthestudy pages 11-12): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.

3. (thessen2020transformingthestudy pages 1-2): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.

4. (thessen2020transformingthestudy pages 2-4): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.

5. (thessen2020transformingthestudy pages 7-8): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.

6. (thessen2020transformingthestudy pages 5-7): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.

7. (thessen2020transformingthestudy pages 12-14): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.

8. (trivellin2024robustnessquantificationof pages 1-2): Cecilia Trivellin, Luca Torello Pianale, and Lisbeth Olsson. Robustness quantification of a mutant library screen revealed key genetic markers in yeast. Microbial Cell Factories, Aug 2024. URL: https://doi.org/10.1186/s12934-024-02490-2, doi:10.1186/s12934-024-02490-2. This article has 1 citations and is from a peer-reviewed journal.

9. (trivellin2024robustnessquantificationof pages 10-11): Cecilia Trivellin, Luca Torello Pianale, and Lisbeth Olsson. Robustness quantification of a mutant library screen revealed key genetic markers in yeast. Microbial Cell Factories, Aug 2024. URL: https://doi.org/10.1186/s12934-024-02490-2, doi:10.1186/s12934-024-02490-2. This article has 1 citations and is from a peer-reviewed journal.

10. (yu2024decipheringcomplexantibiotic pages 1-2): Jianwei Yu, Yan Jia, Qichao Yu, Lan Lin, Chao Li, Bowang Chen, Pingyu Zhong, Xueqing Lin, Huilan Li, Yinping Sun, Xuejing Zhong, Yuqi He, Xiaoyun Huang, Shuangming Lin, and Yuanming Pan. Deciphering complex antibiotic resistance patterns in helicobacter pylori through whole genome sequencing and machine learning. Frontiers in Cellular and Infection Microbiology, Jan 2024. URL: https://doi.org/10.3389/fcimb.2023.1306368, doi:10.3389/fcimb.2023.1306368. This article has 12 citations.

11. (walls2024bacterialphenotypicheterogeneity pages 1-2): Alex W. Walls and Adam Z. Rosenthal. Bacterial phenotypic heterogeneity through the lens of single-cell rna sequencing. Transcription, 15:48-62, Mar 2024. URL: https://doi.org/10.1080/21541264.2024.2334110, doi:10.1080/21541264.2024.2334110. This article has 16 citations and is from a peer-reviewed journal.

12. (herbst2024multiattributesubsetselection pages 3-4): Konrad Herbst, Taiyao Wang, Elena J. Forchielli, Meghan Thommes, Ioannis Ch. Paschalidis, and Daniel Segrè. Multi-attribute subset selection enables prediction of representative phenotypes across microbial populations. Communications Biology, Apr 2024. URL: https://doi.org/10.1038/s42003-024-06093-w, doi:10.1038/s42003-024-06093-w. This article has 4 citations and is from a peer-reviewed journal.

13. (herbst2024multiattributesubsetselection pages 1-2): Konrad Herbst, Taiyao Wang, Elena J. Forchielli, Meghan Thommes, Ioannis Ch. Paschalidis, and Daniel Segrè. Multi-attribute subset selection enables prediction of representative phenotypes across microbial populations. Communications Biology, Apr 2024. URL: https://doi.org/10.1038/s42003-024-06093-w, doi:10.1038/s42003-024-06093-w. This article has 4 citations and is from a peer-reviewed journal.

14. (tran2024combiningmachinelearning pages 1-2): Tuan-Anh Tran, Sushmita Sridhar, Stephen T. Reece, Octavie Lunguya, Jan Jacobs, Sandra Van Puyvelde, Florian Marks, Gordon Dougan, Nicholas R. Thomson, Binh T. Nguyen, Pham The Bao, and Stephen Baker. Combining machine learning with high-content imaging to infer ciprofloxacin susceptibility in isolates of salmonella typhimurium. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49433-4, doi:10.1038/s41467-024-49433-4. This article has 22 citations and is from a highest quality peer-reviewed journal.

15. (ogunlade2024rapidantibioticincubationfree pages 1-4): Babatunde Ogunlade, Loza F. Tadesse, Hongquan Li, Nhat Vu, Niaz Banaei, Amy K. Barczak, Amr A. E. Saleh, Manu Prakash, and Jennifer A. Dionne. Rapid, antibiotic incubation-free determination of tuberculosis drug resistance using machine learning and raman spectroscopy. Proceedings of the National Academy of Sciences, Jun 2024. URL: https://doi.org/10.1073/pnas.2315670121, doi:10.1073/pnas.2315670121. This article has 37 citations and is from a highest quality peer-reviewed journal.

16. (kals2024antibioticschangethe pages 1-3): Morten Kals, Emma Kals, Jurij Kotar, Allen Donald, Leonardo Mancini, and Pietro Cicuta. Antibiotics change the growth rate heterogeneity and morphology of bacteria. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.27.609914, doi:10.1101/2024.08.27.609914. This article has 1 citations.

17. (kals2024antibioticschangethe pages 12-14): Morten Kals, Emma Kals, Jurij Kotar, Allen Donald, Leonardo Mancini, and Pietro Cicuta. Antibiotics change the growth rate heterogeneity and morphology of bacteria. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.27.609914, doi:10.1101/2024.08.27.609914. This article has 1 citations.

18. (kals2024antibioticschangethe pages 3-5): Morten Kals, Emma Kals, Jurij Kotar, Allen Donald, Leonardo Mancini, and Pietro Cicuta. Antibiotics change the growth rate heterogeneity and morphology of bacteria. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.27.609914, doi:10.1101/2024.08.27.609914. This article has 1 citations.

19. (kals2024antibioticschangethe pages 7-10): Morten Kals, Emma Kals, Jurij Kotar, Allen Donald, Leonardo Mancini, and Pietro Cicuta. Antibiotics change the growth rate heterogeneity and morphology of bacteria. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.27.609914, doi:10.1101/2024.08.27.609914. This article has 1 citations.

20. (thessen2020transformingthestudy pages 4-5): Anne E. Thessen, Ramona L. Walls, Lars Vogt, Jessica Singer, Robert Warren, Pier Luigi Buttigieg, James P. Balhoff, Christopher J. Mungall, Deborah L. McGuinness, Brian J. Stucky, Matthew J. Yoder, and Melissa A. Haendel. Transforming the study of organisms: phenomic data models and knowledge bases. PLoS Computational Biology, Nov 2020. URL: https://doi.org/10.1371/journal.pcbi.1008376, doi:10.1371/journal.pcbi.1008376. This article has 16 citations and is from a highest quality peer-reviewed journal.