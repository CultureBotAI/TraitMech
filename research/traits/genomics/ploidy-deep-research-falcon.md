---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:34:48.607074'
end_time: '2026-06-18T03:49:11.092833'
duration_seconds: 862.49
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: ploidy
  trait_identifier: traitmech:000100
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: ploidy
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A genomics trait describing the number of complete genome copies per
    cell; many bacteria and archaea are polyploid, maintaining many chromosome copies
    that support survival, repair, and large cell size.
  parent_traits: METPO:1000188
  synonyms: polyploidy
  evidence_summary: 'DOI:10.1159/000368855:  (Soppa reviews polyploidy in archaea
    and bacteria and its links to desiccation resistance, giant cell size, and long-term
    survival.) | DOI:10.1073/pnas.0707522105:  (Mendell et al. document extreme polyploidy
    (tens of thousands of genome copies) in the large bacterium Epulopiscium.)'
  causal_graph_summary: 'ploidy_repair_survival: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ploidy
- **METPO identifier:** traitmech:000100
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing the number of complete genome copies per cell; many bacteria and archaea are polyploid, maintaining many chromosome copies that support survival, repair, and large cell size.
- **Parent traits:** METPO:1000188
- **Synonyms:** polyploidy
- **Existing evidence:** DOI:10.1159/000368855:  (Soppa reviews polyploidy in archaea and bacteria and its links to desiccation resistance, giant cell size, and long-term survival.) | DOI:10.1073/pnas.0707522105:  (Mendell et al. document extreme polyploidy (tens of thousands of genome copies) in the large bacterium Epulopiscium.)
- **Existing causal graph summary:** ploidy_repair_survival: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **ploidy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/ploidy.yaml`.

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
- **Trait label:** ploidy
- **METPO identifier:** traitmech:000100
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing the number of complete genome copies per cell; many bacteria and archaea are polyploid, maintaining many chromosome copies that support survival, repair, and large cell size.
- **Parent traits:** METPO:1000188
- **Synonyms:** polyploidy
- **Existing evidence:** DOI:10.1159/000368855:  (Soppa reviews polyploidy in archaea and bacteria and its links to desiccation resistance, giant cell size, and long-term survival.) | DOI:10.1073/pnas.0707522105:  (Mendell et al. document extreme polyploidy (tens of thousands of genome copies) in the large bacterium Epulopiscium.)
- **Existing causal graph summary:** ploidy_repair_survival: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **ploidy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/ploidy.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **Ploidy** (METPO: traitmech:000100)

### Executive scope summary
**Ploidy** (syn. **polyploidy** in this template) is a **genomics trait** describing the **number of complete genome copies per cell** in microbes. In prokaryotes, ploidy spans **monoploidy**, **oligoploidy** (∼2–10 copies), **polyploidy** (>10–∼100), and **hyperpolyploidy** (>100) and can be **highly dynamic**, changing with growth phase and environment (e.g., phosphate availability). (bruck2023oneadvantageof pages 1-2, bruck2023ploidyinvibrio pages 1-2)

Boundary cases important for TraitMech curation:
- **Mero-oligoploidy / multifork replication**: high **origin/terminus** ratios during rapid growth can mimic increased “copy number” near origins without stable whole-genome polyploidy; marker-frequency approaches disentangle this. (bruck2023ploidyinvibrio pages 1-2)
- **Replicon copy number vs chromosomal ploidy**: plasmids can be multicopy independently of chromosomal ploidy; causal statements must specify the replicon type. (garona2023segregationaldrifthinders pages 2-3)
- **Aneuploidy/CNV** (common in fungi and some microbial eukaryotes) is conceptually distinct from whole-genome copy number and should not be curated as “ploidy” in this bacterial/archaeal-focused trait unless explicitly framed as whole-genome equivalents.

### Key concepts & current understanding (definitions + assays)
#### Definitions (prokaryotes)
- Polyploid microbes maintain multiple genome copies; categories (oligoploid/polyploid/hyperpolyploid) are explicitly defined in recent prokaryote-focused work. (bruck2023oneadvantageof pages 1-2, bruck2023ploidyinvibrio pages 1-2)

#### How ploidy is measured in microbes
Common assay classes supported in the retrieved evidence include:
1. **qPCR-based copy-number inference** of origins and termini and/or multiple chromosomal loci (including in phosphate-starvation experiments). (bruck2023ploidyinvibrio pages 1-2, bruck2023oneadvantageof pages 10-13)
2. **Marker frequency analysis** (genome-wide abundance of sites) to distinguish replication-associated copy gradients from stable polyploidy. (bruck2023ploidyinvibrio pages 1-2)
3. **Fluorescence-based locus counting** (noted as a method to determine ploidy by counting fluorescently marked genomic sites). (bruck2023oneadvantageof pages 15-16)
4. **Single-cell PCR-based gene copy-number assays** in giant bacteria (Epulopiscium), combined with genomic DNA quantification. (mendell2008extremepolyploidyin pages 2-4)

### Recent developments and latest research (prioritizing 2023–2024)
#### 1) Environmental modulation: phosphate starvation drives ploidy reduction
A 2023 experimental study across multiple polyploid bacteria and archaea shows that **phosphate starvation** can trigger **reduction of chromosome copy number per cell**, enabling limited growth even without external phosphate. (bruck2023oneadvantageof pages 1-2, bruck2023oneadvantageof pages 10-13, bruck2023oneadvantageof pages 13-15)
- This positions **DNA itself as a phosphate reservoir**, reframing ploidy as a resource-storage trait under nutrient limitation. (bruck2023oneadvantageof pages 13-15)

#### 2) Genome-copy equalization in haloarchaea: gene conversion as a ploidy-maintenance process
In 2024, Özer et al. dissected **intermolecular gene conversion** in the polyploid haloarchaeon **Haloferax volcanii** (~20 chromosomal copies), identifying a large set of proteins required for efficient conversion and showing essential roles for **radA** and **radB**. (ozer2024intermoleculargeneconversion pages 1-2)
- Additional mechanistic entities implicated in gene conversion include **Hjc** (Holliday junction resolvase), **Hef** (helicase-associated endonuclease), **NucS/EndoMS** (noncanonical mismatch repair endonuclease), and **MutS/MutL** components; SMC-like **Sph** proteins are also functionally important in their assay contexts. (ozer2024intermoleculargeneconversion pages 16-17, ozer2024intermoleculargeneconversion pages 17-18)

#### 3) Evolutionary genetics: polyploid replicons and antibiotic resistance establishment
In 2023, Garoña et al. showed that in multicopy replicons, stochastic allele segregation (“**segregational drift**”) leads to **frequent loss of beneficial resistance alleles** relative to monoploid elements, affecting resistance evolution and implying pathogen ploidy is clinically relevant to resistance emergence. (garona2023segregationaldrifthinders pages 1-2)

#### 4) Engineering around polyploidy: vectors that bypass segregation constraints
Polyploidy is increasingly treated as an actionable engineering constraint in cyanobacterial biotechnology:
- 2023 work emphasizes that chromosomal editing requires segregation of modifications across multiple chromosomes: “all chromosomes must be segregated to stably retain the genetically modified constructs in polyploid cyanobacteria,” motivating use of **self-replicating plasmids** and cyanobacterial Rep proteins (e.g., CyRepA2) for expression vectors. (sakamaki2023characterizationofa pages 1-2)
- A 2024 preprint in Synechococcus sp. PCC 7002 explicitly states repeated restreaking with increasing antibiotic concentration is required for full segregation, and that this can be bypassed by **replicating episomal plasmids**; the work reports plasmid copy-number ranges and improved transformation via plasmid multimers. (kamoku2024deliveryofnovel pages 1-5)

#### 5) Giant bacteria and hyperpolyploidy (2023 perspective + classic quantitative evidence)
- A 2023 perspective synthesizes evidence that giant bacteria can contain **hundreds to tens of thousands** of chromosomes; for **Candidatus Thiomargarita magnifica**, it cites estimates approaching **~1,000,000 chromosomes** in a 2-cm cell. (ionescu2023genomicmysteriesof pages 8-8, ionescu2023genomicmysteriesof pages 6-7)
- Classic single-cell quantification in Epulopiscium demonstrates extreme gene copy numbers (e.g., **recA median ~120,000 copies/cell**; **16S median ~368,000 copies/cell**). (mendell2008extremepolyploidyin pages 2-4)

### Current applications and real-world implementations
1. **Cyanobacterial metabolic engineering / synthetic biology**: Rep-based self-replicating vectors can raise expression and shorten engineering timelines in polyploid cyanobacteria (e.g., reported 10-fold higher expression than chromosome-based system in one vector context). (sakamaki2023characterizationofa pages 1-2)
2. **Transformation and strain construction in polyploid cyanobacteria**: Episomal plasmids and optimized DNA delivery (e.g., multimeric plasmids improving transformation efficiency) are practical implementations to circumvent segregation barriers. (kamoku2024deliveryofnovel pages 1-5)
3. **Functional genomics in multiploid extremophiles**: CRISPR interference (type I–E Cascade) is deployed to knock down genes in multiploid Deinococcus radiodurans, explicitly addressing the challenge of “up to 10” genome copies. (misra2023effectivegenesilencing pages 1-2)
4. **Antibiotic resistance risk modeling**: population-genetic models integrating segregational drift provide an analytical framework to interpret how multicopy replicons alter establishment probability of resistance alleles. (garona2023segregationaldrifthinders pages 1-2)

### Expert opinion & analysis (authoritative sources in evidence)
- **Ploidy is dynamic and regulated**, not a fixed organism property; in Vibrio natriegens, origin/terminus ratios shift rapidly across growth phases, illustrating the need to separate replication-state effects from stable ploidy. (bruck2023ploidyinvibrio pages 1-2)
- **Polyploidy has tradeoffs**: it can buffer nutrient limitation (phosphate) but also changes allele dynamics (segregational drift) and complicates genetic manipulation (segregation burden). (bruck2023oneadvantageof pages 13-15, garona2023segregationaldrifthinders pages 1-2, kamoku2024deliveryofnovel pages 1-5)
- **Genome homogenization mechanisms matter**: in polyploid haloarchaea, gene conversion can rapidly equalize genome copies, influencing how “heterozygosity” and allele fixation should be interpreted in experiments and evolution. (ozer2024intermoleculargeneconversion pages 1-2, bruck2023oneadvantageof pages 15-16)

### Recent statistics and quantitative data (curation-ready)
The following table consolidates curation-useful quantitative copy-number values and measurement contexts.

| Organism / taxon | Reported genome or chromosome copy number | Condition / context | Measurement method | Citation |
|---|---:|---|---|---|
| *Haloferax volcanii* | ~20 copies of the major chromosome per cell | Baseline polyploid haloarchaeon; discussed in context of highly efficient intermolecular gene conversion that equalizes genome copies | Gene-conversion assay context; chromosome copy number reported from study background/reviewed measurements | (ozer2024intermoleculargeneconversion pages 1-2) |
| *Halobacterium salinarum* | ~32.5 copies/cell in inoculum; ~10 copies in phosphate-replete growth; ~7.1 copies under phosphate starvation | Growth with vs. without external phosphate; copy number decreases as cells grow without environmental phosphate | qPCR of four chromosomal sites | (bruck2023oneadvantageof pages 10-13) |
| *Azotobacter vinelandii* | ~20.6 copies/cell in exponential phase; ~19.6 in stationary phase; transient increase to ~40 at onset of exponential growth | Medium- and growth-phase-dependent dynamics; high transient copy number during growth onset | Chromosome copy-number quantification summarized in study/reviewed measurements | (bruck2023oneadvantageof pages 15-16, bruck2023oneadvantageof pages 16-18) |
| *Synechococcus* sp. PCC 7002 | 5–12 chromosome copies per cell | Polyploidy creates a segregation barrier during chromosomal engineering; motivates use of episomal plasmids | Reported strain property in engineering study | (kamoku2024deliveryofnovel pages 1-5) |
| *Synechococcus elongatus* PCC 7942 | 3–4 chromosome copies per cell | Example cyanobacterium used in segregational-drift analysis; ploidy affects allele establishment on multicopy replicons | Reported strain property in experimental/theoretical study | (garona2023segregationaldrifthinders pages 2-3, garona2023segregationaldrifthinders pages 1-2) |
| *Deinococcus radiodurans* | Up to 10 genome copies | Multiploid, radiation-resistant bacterium; multiploidy noted as an additional challenge for molecular tools | Reported background estimate in CRISPRi study | (misra2023effectivegenesilencing pages 1-2) |
| *Vibrio natriegens* | No single fixed ploidy value; origin copy number and origin/terminus ratios for both chromosomes increase from lag to early exponential phase, then decrease during exponential growth | Highly dynamic chromosome-copy regulation across the growth curve, correlated with cell volume changes | qPCR of origins and termini plus marker frequency analysis | (bruck2023ploidyinvibrio pages 1-2) |
| *Epulopiscium* sp. type B | recA median ~120,000 copies per cell (range 60,300–205,000); 16S rRNA gene median ~368,000 copies (range 241,000–737,000); ~230 genome equivalents inherited (~1% of cell DNA) | Giant bacterium with extreme polyploidy; copy number scales with cell volume | Single-cell amplification / PCR-based gene copy-number assays, genomic DNA quantification, clone sequence analysis | (mendell2008extremepolyploidyin pages 2-4, mendell2008extremepolyploidyin media 0cb4f37f) |
| *Candidatus Thiomargarita magnifica* | ~1,000,000 nearly identical chromosomes in a 2-cm cell; smaller giant-bacterium cells may have only a few hundred chromosomes | Giant bacterium / hyperpolyploidy perspective; chromosome number linked to exceptional cell size | Perspective synthesis of published genomic and cell-biological estimates | (ionescu2023genomicmysteriesof pages 8-8, ionescu2023genomicmysteriesof pages 6-7) |


*Table: This table compiles the main quantitative ploidy values and measurement contexts requested for bacteria and archaea, including dynamic and extreme cases. It is useful as a curation-ready snapshot of organism-level copy-number ranges, environmental modulation, and assay types.*

### Candidate causal graph entities (nodes)
Grouped by type for `data/traits/genomics/ploidy.yaml`.

#### Trait / state nodes
- **ploidy / genome copy number per cell** (METPO: traitmech:000100)
- oligoploidy; polyploidy; hyperpolyploidy (label-level subclasses; prokaryote usage) (bruck2023oneadvantageof pages 1-2, bruck2023ploidyinvibrio pages 1-2)
- heterozygosity / heteropolyploidy (within-cell allele diversity across copies; label-level) (garona2023segregationaldrifthinders pages 2-3)

#### Environmental / experimental factor nodes
- **phosphate starvation / phosphate limitation** (ENVO label-level); phosphate repletion (bruck2023oneadvantageof pages 10-13, bruck2023oneadvantageof pages 13-15)
- growth phase (lag, exponential, stationary) (bruck2023ploidyinvibrio pages 1-2, bruck2023oneadvantageof pages 10-13)
- antibiotic selection / restreaking intensity (engineering factor) (kamoku2024deliveryofnovel pages 1-5)

#### Biological process nodes (ontology suggestions)
- homologous recombination (GO:0035825) (ozer2024intermoleculargeneconversion pages 1-2)
- DNA repair (GO:0006281) (ozer2024intermoleculargeneconversion pages 16-17)
- gene conversion (GO:0000725) (ozer2024intermoleculargeneconversion pages 1-2)
- Holliday junction resolution (GO:0048476) (ozer2024intermoleculargeneconversion pages 16-17)
- mismatch repair (GO:0006298) / noncanonical mismatch repair via NucS/EndoMS (label-level) (ozer2024intermoleculargeneconversion pages 16-17, ozer2024intermoleculargeneconversion pages 17-18)
- chromosome segregation (GO:0007059) (engineering relevance) (sakamaki2023characterizationofa pages 1-2)

#### Molecular entity nodes (genes/proteins; label-only unless curated with UniProt)
- **radA**, **radB** (essential for gene conversion in H. volcanii) (ozer2024intermoleculargeneconversion pages 1-2)
- **rad25** paralogs (rad25a–d; paralog-specific effects) (ozer2024intermoleculargeneconversion pages 1-2)
- **hjc** (Holliday junction resolvase), **hef** (helicase/endonuclease), **nucS/EndoMS** (mismatch endonuclease), **mutS**, **mutL**, **sph1–sph4** (SMC-like) (ozer2024intermoleculargeneconversion pages 16-17, ozer2024intermoleculargeneconversion pages 17-18)

#### Chemical nodes
- phosphate (CHEBI:43474)
- DNA (CHEBI:16991) (as phosphate storage polymer concept) (bruck2023oneadvantageof pages 13-15)

#### Taxon / system nodes (NCBITaxon label-level)
- *Haloferax volcanii* (haloarchaeon) (ozer2024intermoleculargeneconversion pages 1-2)
- *Halobacterium salinarum* (haloarchaeon) (bruck2023oneadvantageof pages 10-13)
- *Synechococcus elongatus* PCC 7942; *Synechococcus* sp. PCC 7002 (cyanobacteria) (garona2023segregationaldrifthinders pages 2-3, kamoku2024deliveryofnovel pages 1-5)
- *Deinococcus radiodurans* (radiation-resistant bacterium) (misra2023effectivegenesilencing pages 1-2)
- *Vibrio natriegens* (fast-growing bacterium) (bruck2023ploidyinvibrio pages 1-2)
- *Epulopiscium* sp. type B; *Candidatus Thiomargarita magnifica* (giant bacteria) (mendell2008extremepolyploidyin pages 2-4, ionescu2023genomicmysteriesof pages 8-8)

### Evidence-backed candidate causal edges (curation table)

| Subject node | Predicate | Object node | Edge strength | Evidence snippet/quote | Reference (DOI, year, URL) | Notes on scope/limitations |
|---|---|---|---|---|---|---|
| phosphate starvation | decreases | genome copy number per cell | strong | “all five polyploid prokaryotic species that have been characterized until now can grow in the absence of environmental phosphate by reducing their genome copy numbers” (bruck2023oneadvantageof pages 1-2, bruck2023oneadvantageof pages 13-15) | 10.3390/microorganisms11092267, 2023, https://doi.org/10.3390/microorganisms11092267 | Supported across five polyploid bacteria/archaea; applies to chromosomal copy number, not necessarily plasmids. |
| polyploidy / high genome copy number | enables growth in absence of environmental phosphate via | consumption of genome copies / DNA as phosphate store | strong | “multiple polyploid prokaryotes… can grow without external phosphate by reducing intracellular genome copy number, indicating genomic DNA acts as a phosphate storage polymer” (bruck2023oneadvantageof pages 13-15); monoploid *E. coli* “did not exhibit any growth in the absence of phosphate” (bruck2023oneadvantageof pages 1-2) | 10.3390/microorganisms11092267, 2023, https://doi.org/10.3390/microorganisms11092267 | Strong functional link, but mechanism may coexist with other phosphate sources (ribosomes/phospholipids) in some taxa. |
| polyploidy in *Haloferax volcanii* | enables | intermolecular gene conversion that equalizes genome copies | strong | “*Haloferax volcanii* is polyploid (~20 chromosomal copies) where ‘highly efficient intermolecular gene conversion’ equalizes genome copies” (ozer2024intermoleculargeneconversion pages 1-2) | 10.3390/genes15070861, 2024, https://doi.org/10.3390/genes15070861 | Specific to *H. volcanii* and closely related haloarchaea; not yet generalized across bacteria. |
| radA | essential for | intermolecular gene conversion in *Haloferax volcanii* | strong | “single deletions showed only radA and radB to be essential” (ozer2024intermoleculargeneconversion pages 1-2) | 10.3390/genes15070861, 2024, https://doi.org/10.3390/genes15070861 | Strong gene-level evidence from deletion analysis in one archaeal model. |
| radB | essential for | intermolecular gene conversion in *Haloferax volcanii* | strong | “single deletions showed only radA and radB to be essential” (ozer2024intermoleculargeneconversion pages 1-2) | 10.3390/genes15070861, 2024, https://doi.org/10.3390/genes15070861 | Same scope limitation as radA: direct evidence in *H. volcanii*. |
| deletion of rad25a / rad25c / rad25d | decreases | gene conversion efficiency in *Haloferax volcanii* | moderate | “∆rad25b no phenotype but ∆rad25a/c/d highly compromised” (ozer2024intermoleculargeneconversion pages 1-2) | 10.3390/genes15070861, 2024, https://doi.org/10.3390/genes15070861 | Family-paralog specific; qualitative severity reported in summary, not exact effect sizes here. |
| polyploid replicons / higher ploidy | increases | segregational drift | strong | “alleles on polyploid replicons segregate stochastically during cell division, a process termed ‘segregational drift’” (garona2023segregationaldrifthinders pages 2-3) | 10.1371/journal.pgen.1010829, 2023, https://doi.org/10.1371/journal.pgen.1010829 | Mechanistic population-genetic effect shown with experiments and modeling. |
| segregational drift on polyploid replicons | increases loss of | beneficial resistance alleles | strong | “resistance alleles in polyploid elements are lost frequently in comparison to alleles in monoploid elements due to segregational drift” (garona2023segregationaldrifthinders pages 1-2) | 10.1371/journal.pgen.1010829, 2023, https://doi.org/10.1371/journal.pgen.1010829 | Strong for beneficial resistance alleles on multicopy replicons; dependence on copy number and selection context noted. |
| cyanobacterial polyploidy | increases time required to obtain | homozygous segregants / fully segregated engineered chromosomes | strong | “all chromosomes must be segregated to stably retain the genetically modified constructs in polyploid cyanobacteria” (sakamaki2023characterizationofa pages 1-2); PCC 7002 engineering requires a “lengthy process of repeated restreaking on plates with increasing antibiotic concentrations” (kamoku2024deliveryofnovel pages 1-5) | 10.3389/fmicb.2023.1111979, 2023, https://doi.org/10.3389/fmicb.2023.1111979; 10.1101/2024.07.31.606084, 2024, https://doi.org/10.1101/2024.07.31.606084 | Strong practical engineering effect; one source is a preprint for PCC 7002. |
| replicating plasmids / episomal vectors | bypass | chromosomal segregation barrier in polyploid cyanobacteria | strong | segregation burden “could be bypassed via the use of replicating episomal plasmids” (kamoku2024deliveryofnovel pages 1-5); self-replicating plasmids are maintained autonomously and enabled higher expression than chromosome-based systems (sakamaki2023characterizationofa pages 1-2) | 10.1101/2024.07.31.606084, 2024, https://doi.org/10.1101/2024.07.31.606084; 10.3389/fmicb.2023.1111979, 2023, https://doi.org/10.3389/fmicb.2023.1111979 | Useful implementation edge for biotechnology; preprint evidence should be curated cautiously. |
| giant bacterial large cell size | associated with | hyperpolyploidy / very high chromosome copy number | uncertain | giant bacteria show chromosome counts “ranging from tens… to hundreds… up to very large numbers in *Thiomargarita* and *Epulopiscium*” (ionescu2023genomicmysteriesof pages 6-7); a 2-cm *Ca. Thiomargarita magnifica* cell “may contain almost a million nearly identical chromosomes” (ionescu2023genomicmysteriesof pages 8-8); Epulopiscium contains “tens of thousands of copies” (mendell2008extremepolyploidyin pages 2-4) | 10.1093/gbe/evad163, 2023, https://doi.org/10.1093/gbe/evad163; 10.1073/pnas.0707522105, 2008, https://doi.org/10.1073/pnas.0707522105 | Correlation is strong, but causal direction is not resolved; best curated as association unless stronger mechanistic evidence is added. |


*Table: This table lists evidence-backed candidate causal edges for microbial ploidy/polyploidy, emphasizing mechanistic links, environmental modulation, and engineering implications. It is formatted for TraitMech-style curation and highlights where claims are strong versus taxon-specific or uncertain.*

### Warnings / curation cautions (do not over-curate)
1. **Giant cell size ↔ hyperpolyploidy** is strongly associated in the literature synthesis, but causal direction/mechanism is not resolved in the provided evidence; curate as association or mark uncertain. (ionescu2023genomicmysteriesof pages 8-8, ionescu2023genomicmysteriesof pages 6-7)
2. **Dynamic replication-state effects** (origin/terminus ratios; multifork replication) can confound ploidy interpretation; ensure assay definition distinguishes replication gradients from whole-genome equivalents. (bruck2023ploidyinvibrio pages 1-2)
3. **Preprint evidence**: PCC 7002 replicating vectors paper is a 2024 bioRxiv preprint; edges supported by it should be tagged as “provisional” until peer-reviewed. (kamoku2024deliveryofnovel pages 1-5)
4. **UniProt/NCBITaxon identifiers** for specific genes and some taxa were not directly retrievable from the current evidence; curate gene nodes as label-only unless cross-validated.

---

## DOI-first bibliography (with dates and URLs)

1. Brück P, Wasser D, Soppa J. **One Advantage of Being Polyploid: Prokaryotes of Various Phylogenetic Groups Can Grow in the Absence of an Environmental Phosphate Source at the Expense of Their High Genome Copy Numbers.** *Microorganisms*. **2023-09**. DOI: **10.3390/microorganisms11092267**. URL: https://doi.org/10.3390/microorganisms11092267 (bruck2023oneadvantageof pages 1-2, bruck2023oneadvantageof pages 10-13, bruck2023oneadvantageof pages 13-15)

2. Brück P, Wasser D, Soppa J. **Ploidy in Vibrio natriegens: Very Dynamic and Rapidly Changing Copy Numbers of Both Chromosomes.** *Genes*. **2023-07**. DOI: **10.3390/genes14071437**. URL: https://doi.org/10.3390/genes14071437 (bruck2023ploidyinvibrio pages 1-2)

3. Özer H, Wasser D, Sandner L, Soppa J. **Intermolecular Gene Conversion for the Equalization of Genome Copies in the Polyploid Haloarchaeon Haloferax volcanii: Identification of Important Proteins.** *Genes*. **2024-07**. DOI: **10.3390/genes15070861**. URL: https://doi.org/10.3390/genes15070861 (ozer2024intermoleculargeneconversion pages 1-2, ozer2024intermoleculargeneconversion pages 16-17, ozer2024intermoleculargeneconversion pages 17-18)

4. Garoña A, Santer M, Hülter NF, Uecker H, Dagan T. **Segregational drift hinders the evolution of antibiotic resistance on polyploid replicons.** *PLOS Genetics*. **2023-02**. DOI: **10.1371/journal.pgen.1010829**. URL: https://doi.org/10.1371/journal.pgen.1010829 (garona2023segregationaldrifthinders pages 1-2)

5. Sakamaki Y, Maeda K, Nimura-Matsune K, Chibazakura T, Watanabe S. **Characterization of a cyanobacterial rep protein with broad-host range and its utilization for expression vectors.** *Frontiers in Microbiology*. **2023-03**. DOI: **10.3389/fmicb.2023.1111979**. URL: https://doi.org/10.3389/fmicb.2023.1111979 (sakamaki2023characterizationofa pages 1-2)

6. Misra CS, Pandey N, Appukuttan D, Rath D. **Effective gene silencing using type I–E CRISPR system in the multiploid, radiation-resistant bacterium Deinococcus radiodurans.** *Microbiology Spectrum*. **2023-10** (article metadata indicates published 2023-09-06 in excerpt). DOI: **10.1128/spectrum.05204-22**. URL: https://doi.org/10.1128/spectrum.05204-22 (misra2023effectivegenesilencing pages 1-2)

7. Ionescu D, Volland J-M, Contarini P-E, Gros O. **Genomic Mysteries of Giant Bacteria: Insights and Implications.** *Genome Biology and Evolution*. **2023-09**. DOI: **10.1093/gbe/evad163**. URL: https://doi.org/10.1093/gbe/evad163 (ionescu2023genomicmysteriesof pages 8-8, ionescu2023genomicmysteriesof pages 6-7)

8. Kamoku C, Cooper C, Straub A, Miller N, Nielsen DR. **Delivery of novel replicating vectors to Synechococcus sp. PCC 7002 via natural transformation of plasmid multimers.** *bioRxiv* (preprint). **2024-07**. DOI: **10.1101/2024.07.31.606084**. URL: https://doi.org/10.1101/2024.07.31.606084 (kamoku2024deliveryofnovel pages 1-5)

9. Mendell JE, Clements KD, Choat JH, Angert ER. **Extreme polyploidy in a large bacterium.** *PNAS*. **2008-05**. DOI: **10.1073/pnas.0707522105**. URL: https://doi.org/10.1073/pnas.0707522105 (mendell2008extremepolyploidyin pages 2-4, mendell2008extremepolyploidyin media 0cb4f37f)


References

1. (bruck2023oneadvantageof pages 1-2): Patrik Brück, Daniel Wasser, and Jörg Soppa. One advantage of being polyploid: prokaryotes of various phylogenetic groups can grow in the absence of an environmental phosphate source at the expense of their high genome copy numbers. Microorganisms, 11:2267, Sep 2023. URL: https://doi.org/10.3390/microorganisms11092267, doi:10.3390/microorganisms11092267. This article has 7 citations.

2. (bruck2023ploidyinvibrio pages 1-2): Patrik Brück, Daniel Wasser, and Jörg Soppa. Ploidy in vibrio natriegens: very dynamic and rapidly changing copy numbers of both chromosomes. Genes, 14:1437, Jul 2023. URL: https://doi.org/10.3390/genes14071437, doi:10.3390/genes14071437. This article has 4 citations.

3. (garona2023segregationaldrifthinders pages 2-3): Ana Garoña, Mario Santer, Nils F. Hülter, Hildegard Uecker, and Tal Dagan. Segregational drift hinders the evolution of antibiotic resistance on polyploid replicons. PLOS Genetics, Feb 2023. URL: https://doi.org/10.1371/journal.pgen.1010829, doi:10.1371/journal.pgen.1010829. This article has 18 citations and is from a domain leading peer-reviewed journal.

4. (bruck2023oneadvantageof pages 10-13): Patrik Brück, Daniel Wasser, and Jörg Soppa. One advantage of being polyploid: prokaryotes of various phylogenetic groups can grow in the absence of an environmental phosphate source at the expense of their high genome copy numbers. Microorganisms, 11:2267, Sep 2023. URL: https://doi.org/10.3390/microorganisms11092267, doi:10.3390/microorganisms11092267. This article has 7 citations.

5. (bruck2023oneadvantageof pages 15-16): Patrik Brück, Daniel Wasser, and Jörg Soppa. One advantage of being polyploid: prokaryotes of various phylogenetic groups can grow in the absence of an environmental phosphate source at the expense of their high genome copy numbers. Microorganisms, 11:2267, Sep 2023. URL: https://doi.org/10.3390/microorganisms11092267, doi:10.3390/microorganisms11092267. This article has 7 citations.

6. (mendell2008extremepolyploidyin pages 2-4): Jennifer E. Mendell, Kendall D. Clements, J. Howard Choat, and Esther R. Angert. Extreme polyploidy in a large bacterium. Proceedings of the National Academy of Sciences, 105:6730-6734, May 2008. URL: https://doi.org/10.1073/pnas.0707522105, doi:10.1073/pnas.0707522105. This article has 189 citations and is from a highest quality peer-reviewed journal.

7. (bruck2023oneadvantageof pages 13-15): Patrik Brück, Daniel Wasser, and Jörg Soppa. One advantage of being polyploid: prokaryotes of various phylogenetic groups can grow in the absence of an environmental phosphate source at the expense of their high genome copy numbers. Microorganisms, 11:2267, Sep 2023. URL: https://doi.org/10.3390/microorganisms11092267, doi:10.3390/microorganisms11092267. This article has 7 citations.

8. (ozer2024intermoleculargeneconversion pages 1-2): Hanna Özer, Daniel Wasser, Lara Sandner, and Jörg Soppa. Intermolecular gene conversion for the equalization of genome copies in the polyploid haloarchaeon haloferax volcanii: identification of important proteins. Genes, 15:861, Jul 2024. URL: https://doi.org/10.3390/genes15070861, doi:10.3390/genes15070861. This article has 5 citations.

9. (ozer2024intermoleculargeneconversion pages 16-17): Hanna Özer, Daniel Wasser, Lara Sandner, and Jörg Soppa. Intermolecular gene conversion for the equalization of genome copies in the polyploid haloarchaeon haloferax volcanii: identification of important proteins. Genes, 15:861, Jul 2024. URL: https://doi.org/10.3390/genes15070861, doi:10.3390/genes15070861. This article has 5 citations.

10. (ozer2024intermoleculargeneconversion pages 17-18): Hanna Özer, Daniel Wasser, Lara Sandner, and Jörg Soppa. Intermolecular gene conversion for the equalization of genome copies in the polyploid haloarchaeon haloferax volcanii: identification of important proteins. Genes, 15:861, Jul 2024. URL: https://doi.org/10.3390/genes15070861, doi:10.3390/genes15070861. This article has 5 citations.

11. (garona2023segregationaldrifthinders pages 1-2): Ana Garoña, Mario Santer, Nils F. Hülter, Hildegard Uecker, and Tal Dagan. Segregational drift hinders the evolution of antibiotic resistance on polyploid replicons. PLOS Genetics, Feb 2023. URL: https://doi.org/10.1371/journal.pgen.1010829, doi:10.1371/journal.pgen.1010829. This article has 18 citations and is from a domain leading peer-reviewed journal.

12. (sakamaki2023characterizationofa pages 1-2): Yutaka Sakamaki, Kaisei Maeda, Kaori Nimura-Matsune, Taku Chibazakura, and Satoru Watanabe. Characterization of a cyanobacterial rep protein with broad-host range and its utilization for expression vectors. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1111979, doi:10.3389/fmicb.2023.1111979. This article has 12 citations and is from a peer-reviewed journal.

13. (kamoku2024deliveryofnovel pages 1-5): Cody Kamoku, Cheyanna Cooper, Ashley Straub, Nathan Miller, and David R. Nielsen. Delivery of novel replicating vectors to synechococcus sp. pcc 7002 via natural transformation of plasmid multimers. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.31.606084, doi:10.1101/2024.07.31.606084. This article has 2 citations.

14. (ionescu2023genomicmysteriesof pages 8-8): Danny Ionescu, Jean-Marie Volland, Paul-Emile Contarini, and Olivier Gros. Genomic mysteries of giant bacteria: insights and implications. Genome Biology and Evolution, Sep 2023. URL: https://doi.org/10.1093/gbe/evad163, doi:10.1093/gbe/evad163. This article has 10 citations and is from a domain leading peer-reviewed journal.

15. (ionescu2023genomicmysteriesof pages 6-7): Danny Ionescu, Jean-Marie Volland, Paul-Emile Contarini, and Olivier Gros. Genomic mysteries of giant bacteria: insights and implications. Genome Biology and Evolution, Sep 2023. URL: https://doi.org/10.1093/gbe/evad163, doi:10.1093/gbe/evad163. This article has 10 citations and is from a domain leading peer-reviewed journal.

16. (misra2023effectivegenesilencing pages 1-2): Chitra S. Misra, Neha Pandey, Deepti Appukuttan, and Devashish Rath. Effective gene silencing using type i–e crispr system in the multiploid, radiation-resistant bacterium <i>deinococcus radiodurans</i>. Oct 2023. URL: https://doi.org/10.1128/spectrum.05204-22, doi:10.1128/spectrum.05204-22. This article has 6 citations and is from a domain leading peer-reviewed journal.

17. (bruck2023oneadvantageof pages 16-18): Patrik Brück, Daniel Wasser, and Jörg Soppa. One advantage of being polyploid: prokaryotes of various phylogenetic groups can grow in the absence of an environmental phosphate source at the expense of their high genome copy numbers. Microorganisms, 11:2267, Sep 2023. URL: https://doi.org/10.3390/microorganisms11092267, doi:10.3390/microorganisms11092267. This article has 7 citations.

18. (mendell2008extremepolyploidyin media 0cb4f37f): Jennifer E. Mendell, Kendall D. Clements, J. Howard Choat, and Esther R. Angert. Extreme polyploidy in a large bacterium. Proceedings of the National Academy of Sciences, 105:6730-6734, May 2008. URL: https://doi.org/10.1073/pnas.0707522105, doi:10.1073/pnas.0707522105. This article has 189 citations and is from a highest quality peer-reviewed journal.