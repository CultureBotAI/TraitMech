---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:33:19.593890'
end_time: '2026-06-18T03:47:20.574546'
duration_seconds: 840.98
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pangenome openness
  trait_identifier: traitmech:000102
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: pangenome_openness
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A genomics trait describing the structure of a species' pangenome \u2014\
    \ the balance of core versus accessory genes and whether the pangenome is open\
    \ (continually acquiring new genes across genomes) or closed."
  parent_traits: METPO:1000188
  synonyms: open pangenome
  evidence_summary: 'DOI:10.1073/pnas.0506758102:  (Tettelin et al. introduced the
    microbial pan-genome concept, distinguishing core and dispensable genes and open
    versus closed pangenomes.) | DOI:10.1038/nmicrobiol.2017.40:  (McInerney, McNally
    & O''Connell review why prokaryotes have pangenomes and what drives their openness.)'
  causal_graph_summary: 'pangenome_openness_hgt: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pangenome openness
- **METPO identifier:** traitmech:000102
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing the structure of a species' pangenome — the balance of core versus accessory genes and whether the pangenome is open (continually acquiring new genes across genomes) or closed.
- **Parent traits:** METPO:1000188
- **Synonyms:** open pangenome
- **Existing evidence:** DOI:10.1073/pnas.0506758102:  (Tettelin et al. introduced the microbial pan-genome concept, distinguishing core and dispensable genes and open versus closed pangenomes.) | DOI:10.1038/nmicrobiol.2017.40:  (McInerney, McNally & O'Connell review why prokaryotes have pangenomes and what drives their openness.)
- **Existing causal graph summary:** pangenome_openness_hgt: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pangenome openness** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/pangenome_openness.yaml`.

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
- **Trait label:** pangenome openness
- **METPO identifier:** traitmech:000102
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing the structure of a species' pangenome — the balance of core versus accessory genes and whether the pangenome is open (continually acquiring new genes across genomes) or closed.
- **Parent traits:** METPO:1000188
- **Synonyms:** open pangenome
- **Existing evidence:** DOI:10.1073/pnas.0506758102:  (Tettelin et al. introduced the microbial pan-genome concept, distinguishing core and dispensable genes and open versus closed pangenomes.) | DOI:10.1038/nmicrobiol.2017.40:  (McInerney, McNally & O'Connell review why prokaryotes have pangenomes and what drives their openness.)
- **Existing causal graph summary:** pangenome_openness_hgt: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pangenome openness** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/pangenome_openness.yaml`.

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


# Research Report: Microbial trait “pangenome openness” (TraitMech: traitmech:000102)

## 1) Scope summary (trait definition, boundaries, and distinctions)

**Trait definition (operational):** *Pangenome openness* describes whether a species’ pangenome continues to expand as additional genomes are sampled (open) or whether it approaches saturation (closed). It is fundamentally about the **rate of discovery of novel genes/gene families** with increasing sampling, not simply the number of genes already observed. (parmigiani2024revisitingpangenomeopenness pages 5-7, carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12)

**Key boundary distinctions:**

- **Openness ≠ total pangenome size.** A taxon can have a large pangenome but a comparatively slower discovery rate (less open) and vice versa; recent discussion explicitly notes that species with similar genome/gene-family counts can differ substantially in openness. (parmigiani2024revisitingpangenomeopenness pages 5-7, carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12)
- **Openness is a population-level property** of a sampled gene pool and depends on sampling design and diversity: the growth trajectory used to estimate openness depends on genome ordering and is typically averaged over permutations or combinations. (parmigiani2024revisitingpangenomeopenness pages 1-3)
- **Binary “open vs closed” labels are often unstable** in practice due to sampling and methodological effects; recent work highlights that the binary classification is debated and sensitive to fitting choices and tool parameters. (parmigiani2024revisitingpangenomeopenness pages 1-3, parmigiani2024revisitingpangenomeopenness pages 12-14)

**Near-by traits that should not be conflated in curation:**

- **Accessory genome fraction / rare gene fraction:** correlates with openness but is not identical (proxy rather than definition). (wang2024comparativegenomicsunveils pages 12-15)
- **Horizontal gene transfer (HGT) rate / gene gain–loss rates:** mechanistic drivers that influence openness; they are candidate upstream causal entities, not the trait itself. (tonkinhill2023challengesinprokaryote pages 4-6, tonkinhill2023robustanalysisof pages 1-2)

## 2) Current understanding: concepts and quantification

### 2.1 Core vs accessory genes and “new gene discovery”
A pangenome is commonly defined as the **union** of items (usually gene families) across genomes, partitioned into **core** (present in all/most genomes) and **dispensable/accessory** components. Openness focuses on how many **new** items appear as genomes are added. (parmigiani2024revisitingpangenomeopenness pages 1-3)

### 2.2 Quantitative models (Heaps’ law / power-law growth)
Modern openness estimation typically models the number of new items discovered at the *m*-th genome, \(f_{new}(m)\), using Heaps’ law:
\[
 f_{new}(m) = K m^{-\alpha}
\]
with openness interpreted from \(\alpha\):
- **\(\alpha < 1\)**: cumulative pangenome grows without bound with sample size → *open pangenome*.
- **\(\alpha > 1\)**: cumulative pangenome approaches a constant → *closed pangenome*.
Equivalently, cumulative size can be written with \(\gamma = 1-\alpha\) so \(f_{tot} \sim C + m^{\gamma}\). (parmigiani2024revisitingpangenomeopenness pages 5-7, parmigiani2024revisitingpangenomeopenness pages 12-14)

A 2024 methods chapter describes an alternative/common parameterization for cumulative growth \(n = k\times N^{\gamma}\), interpreting **\(\gamma>0\)** as open. (carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12)

### 2.3 Recent methodological cautions (2023–2024)
Recent sources emphasize several issues that should be treated as **confounders** for TraitMech curation:

- **Fitting choices strongly affect \(\alpha\):** the chosen starting point \(m_0\) for fitting can change estimates and the tail often fits better than early genomes; the choice depends on whether one is estimating “openness” or predicting new discoveries. (parmigiani2024revisitingpangenomeopenness pages 10-12)
- **Tool and parameter dependence:** gene-homology thresholds and whether tools fit all permutation points vs medians/means can change reported \(\alpha\). (parmigiani2024revisitingpangenomeopenness pages 10-12)
- **Genome ordering/permutation averaging:** openness is inferred from a growth trajectory that is order-dependent (unlike the final union), hence permutation strategy matters. (parmigiani2024revisitingpangenomeopenness pages 1-3)
- **Closed pangenome definitions can be mathematically problematic:** a 2024 re-analysis points out that the original Tettelin-style formulation (with \(C=0\)) leads to contradictions that can make a closed pangenome mathematically impossible under that definition. (parmigiani2024revisitingpangenomeopenness pages 5-7)

## 3) Recent developments and latest research (prioritizing 2023–2024)

### 3.1 2023: “Challenges in prokaryote pangenomics” (Tonkin-Hill et al.)
This review highlights that **HGT and gene gain/loss dynamics** are central to pangenome variation and openness, but that **presence/absence inference is error-prone**, with errors arising from contamination, misassembly, fragmented drafts, inconsistent gene calling, and clustering/annotation differences. These errors propagate and can confound downstream inference about gene flux and openness. (tonkinhill2023challengesinprokaryote pages 1-2, tonkinhill2023challengesinprokaryote pages 4-6)

### 3.2 2023: Panstripe—robust gene gain/loss modeling and error sensitivity
Tonkin-Hill et al. (Genome Research 2023) demonstrate that classical accumulation-curve approaches can be misleading because they can reflect **temporal sampling diversity** rather than true differences in HGT dynamics. They explicitly show by simulation that **annotation error can misclassify** whether a pangenome is open or closed: “higher rates of annotation error can lead to incorrect estimates of whether a pangenome is open or closed.” (tonkinhill2023robustanalysisof pages 1-2, tonkinhill2023robustanalysisof pages 16-17)

They propose **Panstripe**, a GLM framework that models gain/loss along a core-genome phylogeny to reduce sensitivity to population structure and errors in gene presence/absence matrices. (tonkinhill2023robustanalysisof pages 1-2)

### 3.3 2024: Revisiting openness with k-mers (Parmigiani et al.)
Parmigiani et al. (Peer Community Journal 2024) reframe openness as discovery of new “items,” showing that openness can be estimated from **genes** or directly from **k-mers**, the latter avoiding homology/annotation steps and offering major computational advantages. They provide explicit guidance on **fitting choices** (e.g., starting point \(m_0\)), k selection, and how tool choices alter \(\alpha\) estimates. (parmigiani2024revisitingpangenomeopenness pages 10-12, parmigiani2024revisitingpangenomeopenness pages 1-3)

### 3.4 2024: Empirical “drivers” of openness in the Bacillus subtilis group (Wang et al.)
A 2024 comparative study explicitly relates openness to “genome stability” and mobile-element proxies. It reports strong correlations between openness and (i) core/rare gene fractions and (ii) counts/distribution of integrases, prophages, transfer mobile elements, recombinases, and repair-system genes. (wang2024comparativegenomicsunveils pages 15-17, wang2024comparativegenomicsunveils pages 12-15)

## 4) Real-world applications and implementations

### 4.1 Antimicrobial resistance (AMR) surveillance and One Health genomics
A 2024 One Health genomics perspective highlights widespread practical use of NGS/WGS for AMR surveillance and emphasizes that long-read metagenomics and improved assembly enable characterization of plasmids and genomic contexts around AMR genes—biological substrates of accessory genome turnover that underpin pangenome openness and gene flux tracking. (liu2024integrativegenomicswould pages 7-8)

Quantitative performance figures reported include **genomic AMR prediction >87% sensitivity and >98% specificity**, and **95–99% genotype–phenotype concordance** in a Campylobacter study, with WGS identifying **18 AMR genes** in that example. (liu2024integrativegenomicswould pages 7-8)

### 4.2 Marker discovery, pathogen detection, and comparative pathogen genomics
A 2024 pangenome review describes practical workflows and tools used to identify **unique regions/SNPs** (e.g., Panseq), annotate AMR/virulence (e.g., VFDB/ResFinder integration), and visualize/cluster isolates for outbreak-style comparisons. (golchha2024bacterialpangenomea pages 5-6)

### 4.3 Pan-GWAS / genotype–phenotype association on accessory genes
The same review describes **Pyseer** (a SEER reimplementation) for modeling k-mers vs phenotype and notes ML-based prediction of traits from sequences—typical implementations of pan-GWAS that implicitly depend on pangenome openness (availability of variable accessory content). (golchha2024bacterialpangenomea pages 6-7)

### 4.4 Scalable pangenome construction for large collections
Le et al. (Genome Biology 2024) present **PanTA**, a progressive pangenome construction approach intended to handle rapidly growing genome collections. They also document construction of large reference pangenomes with QC filters (e.g., E. coli RefSeq subset) and release software and pangenomes publicly. (le2024efficientinferenceof pages 14-15)

## 5) Expert synthesis and analysis (authoritative viewpoints)

### 5.1 Mechanistic interpretation: openness as gene flux through MGEs
Across 2023–2024 sources, openness is most consistently interpretable as a **statistical signature of gene flux** driven by HGT and gene gain/loss, often mediated by mobile genetic elements (plasmids, phages/prophages, ICEs/IMEs, transposons/IS). (tonkinhill2023challengesinprokaryote pages 1-2, tonkinhill2023challengesinprokaryote pages 4-6)

### 5.2 Why “openness” is difficult to curate as a purely biological trait
Multiple authoritative sources emphasize that openness is strongly influenced by:
- **Sampling design:** temporal sampling diversity and population structure can make pangenomes appear more open without any mechanistic change in HGT rate. (tonkinhill2023robustanalysisof pages 1-2, tonkinhill2023challengesinprokaryote pages 4-6)
- **Technical error:** annotation and gene clustering errors distort presence/absence matrices and can change open/closed calls. (tonkinhill2023robustanalysisof pages 16-17, tonkinhill2023challengesinprokaryote pages 1-2)

Thus, causal graphs should include explicit nodes for **measurement/estimation pipeline factors** to prevent over-curation of artefacts as biology.

## 6) Candidate nodes for curation (grouped by type)

The following curated candidate node inventory emphasizes ontology grounding where straightforward (GO processes) and otherwise label-only candidates suitable for later grounding.

| Node group | Candidate node label | Suggested grounding / CURIE | Node type | Why it is relevant to pangenome openness | Evidence citation |
|---|---|---|---|---|---|
| Trait/phenotype measure | pangenome openness | METPO:traitmech:000102 | trait | Target trait: degree to which new genes continue to be discovered as genomes are added | (parmigiani2024revisitingpangenomeopenness pages 5-7, parmigiani2024revisitingpangenomeopenness pages 1-3) |
| Trait/phenotype measure | Heaps' law exponent alpha | label-only | quantitative measure | Common openness parameter fit from new-gene discovery curves; alpha < 1 usually interpreted as open | (parmigiani2024revisitingpangenomeopenness pages 5-7, parmigiani2024revisitingpangenomeopenness pages 12-14) |
| Trait/phenotype measure | Heaps' law exponent gamma | label-only | quantitative measure | Alternate parameterization of pangenome growth; positive gamma indicates continued growth/open behavior | (carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12) |
| Trait/phenotype measure | new gene discovery rate | label-only | quantitative measure | Immediate operational readout of openness: number of newly observed genes added per genome | (parmigiani2024revisitingpangenomeopenness pages 5-7, parmigiani2024revisitingpangenomeopenness pages 7-8) |
| Trait/phenotype measure | rarefaction / pangenome accumulation curve | label-only | assay/summary measure | Standard empirical curve used to estimate openness from sequentially added genomes | (carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12, tonkinhill2023robustanalysisof pages 1-2) |
| Trait/phenotype measure | total pangenome size | label-only | genomic summary | Related but distinct from openness; should be modeled separately to avoid conflation | (parmigiani2024revisitingpangenomeopenness pages 5-7, carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12) |
| Biological process | horizontal gene transfer | GO:0015114 | biological process | Central mechanism adding accessory genes and increasing openness | (tonkinhill2023challengesinprokaryote pages 4-6, tonkinhill2023robustanalysisof pages 1-2) |
| Biological process | DNA recombination | GO:0006310 | biological process | Recombination contributes to gene exchange and diversification linked to openness | (wang2024comparativegenomicsunveils pages 15-17, wang2024comparativegenomicsunveils pages 1-2) |
| Biological process | DNA repair | GO:0006281 | biological process | Repair-system gene repertoires correlate with openness proxies in Bacillus subtilis group | (wang2024comparativegenomicsunveils pages 15-17, wang2024comparativegenomicsunveils pages 1-2) |
| Biological process | transposition | GO:0032196 | biological process | Transposon/IS movement can mobilize genes and reshape accessory genome content | (tonkinhill2023challengesinprokaryote pages 1-2) |
| Biological process | viral process / prophage-mediated gene transfer | GO:0016032 | biological process | Phages/prophages are listed among mobile elements mediating gain/loss and HGT | (tonkinhill2023challengesinprokaryote pages 1-2, tonkinhill2023robustanalysisof pages 7-8) |
| Biological process | gene gain | label-only | evolutionary process | Openness operationally reflects continuing gene gain across sampled genomes | (tonkinhill2023challengesinprokaryote pages 4-6, tonkinhill2023robustanalysisof pages 1-2) |
| Biological process | gene loss | label-only | evolutionary process | Gain/loss balance shapes accumulation curves and open/closed classifications | (golchha2024bacterialpangenomea pages 1-2, tonkinhill2023robustanalysisof pages 1-2) |
| Mobile genetic element | plasmid | label-only | mobile genetic element | Major vector of HGT and accessory gene acquisition | (tonkinhill2023challengesinprokaryote pages 1-2) |
| Mobile genetic element | prophage | label-only | mobile genetic element | Correlates with openness and contributes to recent gain/loss dynamics | (wang2024comparativegenomicsunveils pages 15-17, tonkinhill2023robustanalysisof pages 7-8) |
| Mobile genetic element | bacteriophage / phage | label-only | mobile genetic element | Included among mobile elements mediating HGT in pangenome evolution | (tonkinhill2023challengesinprokaryote pages 1-2) |
| Mobile genetic element | integrative and conjugative element (ICE) | label-only | mobile genetic element | Explicitly named as mediator of gene gain/loss and HGT | (tonkinhill2023challengesinprokaryote pages 1-2) |
| Mobile genetic element | integrative and mobilizable element (IME) | label-only | mobile genetic element | Named among chromosomal mobile elements affecting gene flux | (tonkinhill2023challengesinprokaryote pages 1-2) |
| Mobile genetic element | transposon | label-only | mobile genetic element | Causes genome content changes and presence/absence differences | (tonkinhill2023challengesinprokaryote pages 1-2) |
| Mobile genetic element | insertion sequence (IS element) | label-only | mobile genetic element | Named among mobile elements contributing to accessory genome dynamics | (tonkinhill2023challengesinprokaryote pages 1-2) |
| Mobile genetic element | integrase | label-only | protein/gene family proxy | Integrase abundance/distribution correlates with openness in recent empirical study | (wang2024comparativegenomicsunveils pages 15-17, wang2024comparativegenomicsunveils pages 12-15) |
| Mobile genetic element | transfer mobile elements | label-only | mobile genetic element class | Counts significantly correlate with openness in Bacillus subtilis group | (wang2024comparativegenomicsunveils pages 15-17, wang2024comparativegenomicsunveils pages 1-2) |
| Genomic feature proxy | core gene fraction | label-only | genomic proportion | Strong inverse correlation with openness; lower core proportion implies more open pangenome | (wang2024comparativegenomicsunveils pages 12-15) |
| Genomic feature proxy | rare gene fraction | label-only | genomic proportion | Positive correlation with openness; more rare genes imply greater openness | (wang2024comparativegenomicsunveils pages 12-15) |
| Genomic feature proxy | accessory genome fraction | label-only | genomic proportion | Open pangenomes are enriched in accessory genes/newly acquired content | (parmigiani2024revisitingpangenomeopenness pages 1-3, tonkinhill2023robustanalysisof pages 1-2) |
| Genomic feature proxy | genome stability factors | label-only | composite genomic factor | Broad class used in 2024 empirical work to explain openness variation | (wang2024comparativegenomicsunveils pages 15-17, wang2024comparativegenomicsunveils pages 1-2) |
| Genomic feature proxy | endonuclease gene count | label-only | genomic count proxy | One of the genome-stability-related factors correlated with openness | (wang2024comparativegenomicsunveils pages 15-17, wang2024comparativegenomicsunveils pages 1-2) |
| Genomic feature proxy | recombinase gene count | label-only | genomic count proxy | Correlated with openness in comparative Bacillus analysis | (wang2024comparativegenomicsunveils pages 15-17) |
| Genomic feature proxy | repair-system gene count | label-only | genomic count proxy | Correlated with openness in comparative Bacillus analysis | (wang2024comparativegenomicsunveils pages 15-17) |
| Genomic feature proxy | toxin-antitoxin system distribution | label-only | genomic organization proxy | Reported as associated with openness patterns in Bacillus subtilis group | (wang2024comparativegenomicsunveils pages 1-2) |
| Experimental/computational factor | assembly error | label-only | technical factor | Distorts presence/absence matrices and can bias openness estimation | (tonkinhill2023challengesinprokaryote pages 1-2, carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12) |
| Experimental/computational factor | annotation error | label-only | technical factor | Explicitly shown to distort accumulation curves and open/closed calls | (tonkinhill2023robustanalysisof pages 16-17, tonkinhill2023robustanalysisof pages 1-2) |
| Experimental/computational factor | gene clustering / homology threshold | label-only | technical factor | Different clustering cutoffs and homology definitions alter inferred openness | (parmigiani2024revisitingpangenomeopenness pages 10-12, carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12) |
| Experimental/computational factor | presence/absence matrix error | label-only | technical factor | Direct source of bias in gain/loss and openness analyses | (tonkinhill2023robustanalysisof pages 16-17, tonkinhill2023robustanalysisof pages 10-11) |
| Experimental/computational factor | sampling bias | label-only | study-design factor | Can make openness reflect sampled diversity rather than biological gene flux | (tonkinhill2023challengesinprokaryote pages 4-6, tonkinhill2023robustanalysisof pages 1-2) |
| Experimental/computational factor | population structure | label-only | study-design factor | Important confounder of gene accumulation/open-closed classification | (tonkinhill2023challengesinprokaryote pages 4-6, tonkinhill2023robustanalysisof pages 1-2) |
| Experimental/computational factor | temporal sampling diversity | label-only | study-design factor | Can mislead accumulation-curve comparisons if not accounted for | (tonkinhill2023robustanalysisof pages 1-2) |
| Experimental/computational factor | number of sampled genomes | label-only | study-design factor | Sample size strongly affects rarefaction behavior and classification stability | (parmigiani2024revisitingpangenomeopenness pages 12-14, carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12) |
| Experimental/computational factor | fitting start point (m0) | label-only | analytical factor | Choice of fitting region strongly affects alpha estimation | (parmigiani2024revisitingpangenomeopenness pages 10-12) |
| Experimental/computational factor | genome ordering / permutation averaging | label-only | analytical factor | Growth trajectory depends on genome order, requiring permutations/combinations | (parmigiani2024revisitingpangenomeopenness pages 1-3) |
| Environmental/ecological factor | ecological niche breadth | label-only | ecological factor | Suggested as influencing openness variation across taxa | (wang2024comparativegenomicsunveils pages 15-17, golchha2024bacterialpangenomea pages 1-2) |
| Environmental/ecological factor | community living / sympatry | label-only | ecological factor | Review notes sympatric community-associated taxa tend to have larger, open pangenomes | (golchha2024bacterialpangenomea pages 1-2) |
| Environmental/ecological factor | host/environmental heterogeneity | label-only | ecological factor | Broader ecological heterogeneity increases opportunity for distinct gene pools and accessory content | (tonkinhill2023robustanalysisof pages 1-2, tonkinhill2023robustanalysisof pages 7-8) |


*Table: This table lists candidate nodes for a TraitMech-style causal graph of microbial pangenome openness, grouped into measurable traits, biological processes, mobile elements, genomic proxies, technical confounders, and ecological drivers. It is useful as a starting node inventory for YAML curation and ontology grounding.*

## 7) Evidence-backed candidate causal edges (triples)

The table below provides curation-ready candidate edges with snippets, DOIs/URLs, and uncertainty levels.

| Edge triple | Mechanism / interpretation | Strength / uncertainty | Supporting snippet quote | DOI / URL | Year |
|---|---|---|---|---|---|
| horizontal gene transfer -> increases -> pangenome openness | Continued acquisition of horizontally transferred genes expands accessory gene repertoire and sustains discovery of new genes as genomes are added | strong | “HGT and the rates of gene gain and loss are central determinants of pangenome openness” (tonkinhill2023challengesinprokaryote pages 4-6) | https://doi.org/10.1099/mgen.0.001021 | 2023 |
| gene gain and loss dynamics -> shapes -> pangenome openness | Open/closed behavior reflects balance of ongoing gain versus loss across sampled lineages | strong | “Horizontal gene transfer (HGT) and the resultant gene gain and loss dynamics are central drivers of pangenome composition” (tonkinhill2023robustanalysisof pages 1-2) | https://doi.org/10.1101/2022.04.23.489244 | 2023 |
| plasmid -> enables -> horizontal gene transfer | Plasmids are mobile vehicles for accessory genes, increasing opportunity for gene acquisition | moderate | “gene gain and loss mediated by mobile genetic elements (ISs, transposons, ICEs, IMEs, plasmids, phages)” (tonkinhill2023challengesinprokaryote pages 1-2) | https://doi.org/10.1099/mgen.0.001021 | 2023 |
| prophage -> promotes -> pangenome openness | Prophage-associated gene flux contributes to recent gain/loss and accessory genome expansion | moderate | “gene counts for… prophages, integrases, and transfer/mobile elements were identified as the main drivers of pangenome openness” (wang2024comparativegenomicsunveils pages 15-17) | https://doi.org/10.3390/microorganisms12050986 | 2024 |
| bacteriophage / phage -> enables -> horizontal gene transfer | Phage-mediated movement of genes contributes to accessory genome turnover | moderate | “mobile genetic elements (ISs, transposons, ICEs, IMEs, plasmids, phages)” (tonkinhill2023challengesinprokaryote pages 1-2) | https://doi.org/10.1099/mgen.0.001021 | 2023 |
| integrative and conjugative element (ICE) -> enables -> horizontal gene transfer | ICEs mediate transfer of genomic cargo between cells, increasing gene exchange potential | moderate | “mobile genetic elements (ISs, transposons, ICEs, IMEs, plasmids, phages)” (tonkinhill2023challengesinprokaryote pages 1-2) | https://doi.org/10.1099/mgen.0.001021 | 2023 |
| integrative and mobilizable element (IME) -> enables -> horizontal gene transfer | IMEs contribute to mobile accessory-gene exchange | moderate | “mobile genetic elements (ISs, transposons, ICEs, IMEs, plasmids, phages)” (tonkinhill2023challengesinprokaryote pages 1-2) | https://doi.org/10.1099/mgen.0.001021 | 2023 |
| transposon / insertion sequence -> promotes -> gene gain/loss dynamics | Transposition changes gene content and mobilizes accessory loci, indirectly increasing openness | moderate | “mobile genetic elements (ISs, transposons, ICEs, IMEs, plasmids, phages)” (tonkinhill2023challengesinprokaryote pages 1-2) | https://doi.org/10.1099/mgen.0.001021 | 2023 |
| integrase abundance/distribution -> positively associated with -> pangenome openness | Integrases are markers/effectors of gene integration and mobile-element activity linked to openness | strong | “integrase gene positions significantly correlated with λ (integrase Spearman = 0.689” (wang2024comparativegenomicsunveils pages 12-15) | https://doi.org/10.3390/microorganisms12050986 | 2024 |
| transfer mobile element abundance -> positively associated with -> pangenome openness | More mobile transfer machinery implies more frequent accessory-gene movement | strong | “transfer, prophages, and other mobile elements… was significantly correlated with the openness coefficient” (wang2024comparativegenomicsunveils pages 15-17) | https://doi.org/10.3390/microorganisms12050986 | 2024 |
| recombinase gene count -> positively associated with -> pangenome openness | Recombination-related capacity tracks with greater gene flux and accessory diversification | strong | “endonucleases, recombinases, repair systems, prophages, integrases, and transfer/mobile elements were identified as the main drivers” (wang2024comparativegenomicsunveils pages 15-17) | https://doi.org/10.3390/microorganisms12050986 | 2024 |
| DNA repair-system gene count -> positively associated with -> pangenome openness | Repair/recombination machinery correlates with genome plasticity and openness in Bacillus | strong | “repair-system-related genes… was the main driver of the openness” (wang2024comparativegenomicsunveils pages 15-17) | https://doi.org/10.3390/microorganisms12050986 | 2024 |
| endonuclease gene count -> positively associated with -> pangenome openness | Genome-instability/defense-associated nuclease repertoires correlate with openness | moderate | “endonucleases… were identified as the main drivers of pangenome openness” (wang2024comparativegenomicsunveils pages 15-17) | https://doi.org/10.3390/microorganisms12050986 | 2024 |
| core gene fraction -> negatively associated with -> pangenome openness | Larger conserved core leaves less flexible accessory fraction; empirically anticorrelated with openness | strong | “Strong inverse correlation exists between core gene percentage and λ (corr = -0.910” (wang2024comparativegenomicsunveils pages 12-15) | https://doi.org/10.3390/microorganisms12050986 | 2024 |
| rare gene fraction -> positively associated with -> pangenome openness | Higher proportion of rare genes indicates continued acquisition/non-saturation | strong | “a positive correlation between rare gene percentage and λ (corr = 0.742)” (wang2024comparativegenomicsunveils pages 12-15) | https://doi.org/10.3390/microorganisms12050986 | 2024 |
| sampling bias -> biases estimate of -> apparent pangenome openness | Apparent openness can reflect which genomes were sampled rather than true HGT dynamics | strong | “gene accumulation curves… can be misleading because they may reflect… sampling temporal/diversity bias” (tonkinhill2023robustanalysisof pages 1-2) | https://doi.org/10.1101/2022.04.23.489244 | 2023 |
| population structure -> biases estimate of -> apparent pangenome openness | Uneven lineage structure changes rare-gene counts and accumulation curves independent of mechanism | strong | “sampling bias and population structure also distort core-genome definitions and openness classification” (tonkinhill2023challengesinprokaryote pages 4-6) | https://doi.org/10.1099/mgen.0.001021 | 2023 |
| temporal sampling diversity -> biases estimate of -> apparent pangenome openness | Datasets spanning more evolutionary time accumulate more unique exchanges and may look more open | moderate | “may reflect the underlying diversity in the temporal sampling of genomes rather than a difference in the dynamics of HGT” (tonkinhill2023robustanalysisof pages 1-2) | https://doi.org/10.1101/2022.04.23.489244 | 2023 |
| annotation error -> biases estimate of -> pangenome openness | Misannotation inflates or deflates presence/absence calls and can misclassify open/closed status | strong | “higher rates of annotation error can lead to incorrect estimates of whether a pangenome is open or closed” (tonkinhill2023robustanalysisof pages 16-17) | https://doi.org/10.1101/2022.04.23.489244 | 2023 |
| presence/absence matrix error -> biases estimate of -> pangenome openness | Erroneous gene calls distort rare-gene counts, gain/loss inference, and alpha estimates | strong | “errors in the gene presence/absence matrix” can affect the “tip” signal and dynamics estimates (tonkinhill2023robustanalysisof pages 10-11) | https://doi.org/10.1101/2022.04.23.489244 | 2023 |
| assembly / clustering / ortholog-threshold differences -> biases estimate of -> pangenome openness | Different pipelines and thresholds yield different gene families and therefore different openness values | strong | “different pangenome reconstruction tools can produce different estimates because of disparate ortholog identification methods” (carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12) | https://doi.org/10.1007/978-1-0716-3838-5_5 | 2024 |
| fitting start point (m0) -> changes -> estimated alpha | Heaps’ law exponent depends on which part of the curve is fit, especially tail vs early genomes | strong | “the choice of the starting point m0 strongly affects the fit” (parmigiani2024revisitingpangenomeopenness pages 10-12) | https://doi.org/10.24072/pcjournal.415 | 2024 |
| tool parameters / homology definition -> changes -> estimated alpha | Openness estimates vary across software and clustering rules even on similar data | strong | “Tool and parameter differences can change reported α” (parmigiani2024revisitingpangenomeopenness pages 10-12) | https://doi.org/10.24072/pcjournal.415 | 2024 |
| genome ordering / permutation strategy -> changes -> growth trajectory used for openness | Growth curve is order-dependent, so permutation/combination strategy affects estimated openness | moderate | “the growth trajectory (used to assess openness) is not [order-independent]” (parmigiani2024revisitingpangenomeopenness pages 1-3) | https://doi.org/10.24072/pcjournal.415 | 2024 |
| ecological niche breadth -> increases -> pangenome openness | Broader or more heterogeneous niches may expose taxa to larger gene pools and more accessory diversity | uncertain | “this phenomenon was due to the Bs group members occupying significantly different ecological niches” (wang2024comparativegenomicsunveils pages 15-17) | https://doi.org/10.3390/microorganisms12050986 | 2024 |
| community living / sympatry -> increases -> pangenome openness | Community-associated lifestyles may enlarge gene pools and favor open pangenomes | uncertain | “sympatric species that live in communities tend to have larger genomes and open pangenomes” (golchha2024bacterialpangenomea pages 1-2) | https://doi.org/10.47852/bonviewmedin42022496 | 2024 |


*Table: This table compiles candidate subject–predicate–object edges for a TraitMech causal graph of pangenome openness, with short evidence snippets, uncertainty labels, and source links. It is designed to help prioritize which mechanistic relationships are strong enough for curation and which should remain tentative.*

## 8) Recent statistics and data points (2023–2024)

### 8.1 Openness parameter examples and performance statistics
- **Closed/open thresholds (formal):** \(f_{new}(m)=Km^{-\alpha}\), with **\(\alpha<1\)** implying indefinite growth (open) and **\(\alpha>1\)** implying saturation (closed). (parmigiani2024revisitingpangenomeopenness pages 5-7)
- **Coccolitovirus example:** \(\alpha=1.21\) computed from a published pan-matrix (and 1.22 in the referenced study); Pangrowth computed \(\alpha=1.94\) with \(R^2\approx0.94\), illustrating method sensitivity even in a “closed” case. (parmigiani2024revisitingpangenomeopenness pages 14-16)
- **Human autosome-only dataset:** openness-like estimate reported as ~0.789 in a k-mer-based analysis (illustrating cross-domain applicability of the concept). (parmigiani2024revisitingpangenomeopenness pages 14-16)
- **Computation scale:** histogram-based pangenome growth on **8000 E. coli genomes** can be computed in **<1 second** and **<4 MB** memory in the reported implementation, contrasting with gene-based pipelines. (parmigiani2024revisitingpangenomeopenness pages 12-14)

### 8.2 Example bacterial pangenome composition and openness estimate
A 2024 methods chapter illustrates estimation on **14 Salmonella enterica Typhimurium genomes** with:
- pangenome size **5,978 gene families**,
- core ~**70% (4,210 genes)**,
- accessory ~**30% (1,768 genes)**,
- **Heaps’ law \(\gamma=0.097\)** interpreted as open. (carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12)

### 8.3 Large-scale pangenome sizes and core sizes (example genus)
A 2023 Frontiers in Microbiology study analyzed ~**1,940 Xanthomonas genomes** and reported:
- genus-wide pangenome **38,914 orthologous gene families**,
- “hard-core” of **52 genes**,
- “soft-core” **1,913 genes** (stabilizing after ~100 genomes),
- per-genome gene counts ~**3,139–5,263**. (agarwal2023pangenomeinsightsinto pages 4-5)

### 8.4 Correlations linking openness proxies to mobile-element/genome stability factors
In the Bacillus subtilis group study, openness (\(\lambda\)) showed:
- strong **inverse** correlation with core gene percentage (**corr = −0.910**, p < 2.44×10−6),
- **positive** correlation with rare gene percentage (**corr = 0.742**),
- integrase position correlation (**Spearman = 0.689**, p = 4.47×10−3),
- and “6/9” genome-stability factors significantly correlated with \(\lambda\). (wang2024comparativegenomicsunveils pages 12-15, wang2024comparativegenomicsunveils pages 15-17)

## 9) Warnings / claims not yet ready for TraitMech curation

1. **Do not curate “open vs closed” as a stable binary** without recording the estimation model, fitting strategy (e.g., \(m_0\)), and pipeline/tooling. Multiple sources show these change conclusions. (parmigiani2024revisitingpangenomeopenness pages 10-12, parmigiani2024revisitingpangenomeopenness pages 12-14)
2. **Treat openness estimates as conditional on sampling and technical quality.** Population structure, temporal sampling diversity, and presence/absence errors can create apparent openness differences not caused by biological mechanisms. (tonkinhill2023robustanalysisof pages 1-2, tonkinhill2023robustanalysisof pages 16-17, tonkinhill2023challengesinprokaryote pages 4-6)
3. **Ecological claims (niche breadth/community living → openness) should be curated as uncertain** unless supported by direct comparative tests in the target taxon/context; current evidence here is interpretive or review-level. (wang2024comparativegenomicsunveils pages 15-17, golchha2024bacterialpangenomea pages 1-2)

## 10) DOI-first bibliography (with URLs and publication dates)

- Tonkin-Hill G, Corander J, Parkhill J. **Challenges in prokaryote pangenomics.** *Microbial Genomics.* May 2023. DOI: **10.1099/mgen.0.001021**. https://doi.org/10.1099/mgen.0.001021 (tonkinhill2023challengesinprokaryote pages 4-6, tonkinhill2023challengesinprokaryote pages 1-2)
- Tonkin-Hill G, et al. **Robust analysis of prokaryotic pangenome gene gain and loss rates with Panstripe.** *Genome Research.* 2023 (Sep). DOI: **10.1101/2022.04.23.489244**. https://doi.org/10.1101/2022.04.23.489244 (tonkinhill2023robustanalysisof pages 1-2, tonkinhill2023robustanalysisof pages 16-17)
- Parmigiani L, Wittler R, Stoye J. **Revisiting pangenome openness with k-mers.** *Peer Community Journal.* Apr 2024. DOI: **10.24072/pcjournal.415**. https://doi.org/10.24072/pcjournal.415 (parmigiani2024revisitingpangenomeopenness pages 5-7, parmigiani2024revisitingpangenomeopenness pages 10-12)
- Carhuaricra-Huaman D, Setubal JC. **Step-by-step bacterial genome comparison.** *Methods in Molecular Biology.* Jan 2024. DOI: **10.1007/978-1-0716-3838-5_5**. https://doi.org/10.1007/978-1-0716-3838-5_5 (carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12)
- Wang T, Shi Y, Zheng M, Zheng J. **Comparative genomics unveils functional diversity, pangenome openness, and underlying biological drivers among Bacillus subtilis group.** *Microorganisms.* May 2024. DOI: **10.3390/microorganisms12050986**. https://doi.org/10.3390/microorganisms12050986 (wang2024comparativegenomicsunveils pages 15-17, wang2024comparativegenomicsunveils pages 12-15)
- Le DQ, et al. **Efficient inference of large prokaryotic pangenomes with PanTA.** *Genome Biology.* Aug 2024. DOI: **10.1186/s13059-024-03362-z**. https://doi.org/10.1186/s13059-024-03362-z (le2024efficientinferenceof pages 14-15)
- Golchha NC, Nighojkar A, Nighojkar S. **Bacterial Pangenome: A Review on the Current Strategies, Tools and Applications.** *Medinformatics.* Jun 2024. DOI: **10.47852/bonviewmedin42022496**. https://doi.org/10.47852/bonviewmedin42022496 (golchha2024bacterialpangenomea pages 1-2, golchha2024bacterialpangenomea pages 5-6)
- Liu CSC, Pandey R. **Integrative genomics would strengthen AMR understanding through ONE health approach.** *Heliyon.* Jul 2024. DOI: **10.1016/j.heliyon.2024.e34719**. https://doi.org/10.1016/j.heliyon.2024.e34719 (liu2024integrativegenomicswould pages 7-8)
- Agarwal V, Stubits R, Nassrullah Z, Dillon MM. **Pangenome insights into the diversification and disease specificity of worldwide Xanthomonas outbreaks.** *Frontiers in Microbiology.* Jul 2023. DOI: **10.3389/fmicb.2023.1213261**. https://doi.org/10.3389/fmicb.2023.1213261 (agarwal2023pangenomeinsightsinto pages 4-5)


References

1. (parmigiani2024revisitingpangenomeopenness pages 5-7): Luca Parmigiani, Roland Wittler, and Jens Stoye. Revisiting pangenome openness with k-mers. Peer Community Journal, Apr 2024. URL: https://doi.org/10.24072/pcjournal.415, doi:10.24072/pcjournal.415. This article has 12 citations and is from a peer-reviewed journal.

2. (carhuaricrahuaman2024stepbystepbacterialgenome pages 9-12): Dennis Carhuaricra-Huaman and João Carlos Setubal. Step-by-step bacterial genome comparison. Methods in molecular biology, 2802:107-134, Jan 2024. URL: https://doi.org/10.1007/978-1-0716-3838-5\_5, doi:10.1007/978-1-0716-3838-5\_5. This article has 5 citations and is from a peer-reviewed journal.

3. (parmigiani2024revisitingpangenomeopenness pages 1-3): Luca Parmigiani, Roland Wittler, and Jens Stoye. Revisiting pangenome openness with k-mers. Peer Community Journal, Apr 2024. URL: https://doi.org/10.24072/pcjournal.415, doi:10.24072/pcjournal.415. This article has 12 citations and is from a peer-reviewed journal.

4. (parmigiani2024revisitingpangenomeopenness pages 12-14): Luca Parmigiani, Roland Wittler, and Jens Stoye. Revisiting pangenome openness with k-mers. Peer Community Journal, Apr 2024. URL: https://doi.org/10.24072/pcjournal.415, doi:10.24072/pcjournal.415. This article has 12 citations and is from a peer-reviewed journal.

5. (wang2024comparativegenomicsunveils pages 12-15): Taiquan Wang, Yiling Shi, Mengzhuo Zheng, and Jinshui Zheng. Comparative genomics unveils functional diversity, pangenome openness, and underlying biological drivers among bacillus subtilis group. Microorganisms, 12:986, May 2024. URL: https://doi.org/10.3390/microorganisms12050986, doi:10.3390/microorganisms12050986. This article has 16 citations.

6. (tonkinhill2023challengesinprokaryote pages 4-6): Gerry Tonkin-Hill, Jukka Corander, and Julian Parkhill. Challenges in prokaryote pangenomics. Microbial Genomics, May 2023. URL: https://doi.org/10.1099/mgen.0.001021, doi:10.1099/mgen.0.001021. This article has 39 citations and is from a peer-reviewed journal.

7. (tonkinhill2023robustanalysisof pages 1-2): Gerry Tonkin-Hill, Rebecca A Gladstone, Anna K Pöntinen, Sergio Arredondo-Alonso, Stephen D Bentley, and Jukka Corander. Robust analysis of prokaryotic pangenome gene gain and loss rates with panstripe. Genome Research, 33:129-140, Sep 2023. URL: https://doi.org/10.1101/2022.04.23.489244, doi:10.1101/2022.04.23.489244. This article has 62 citations and is from a highest quality peer-reviewed journal.

8. (parmigiani2024revisitingpangenomeopenness pages 10-12): Luca Parmigiani, Roland Wittler, and Jens Stoye. Revisiting pangenome openness with k-mers. Peer Community Journal, Apr 2024. URL: https://doi.org/10.24072/pcjournal.415, doi:10.24072/pcjournal.415. This article has 12 citations and is from a peer-reviewed journal.

9. (tonkinhill2023challengesinprokaryote pages 1-2): Gerry Tonkin-Hill, Jukka Corander, and Julian Parkhill. Challenges in prokaryote pangenomics. Microbial Genomics, May 2023. URL: https://doi.org/10.1099/mgen.0.001021, doi:10.1099/mgen.0.001021. This article has 39 citations and is from a peer-reviewed journal.

10. (tonkinhill2023robustanalysisof pages 16-17): Gerry Tonkin-Hill, Rebecca A Gladstone, Anna K Pöntinen, Sergio Arredondo-Alonso, Stephen D Bentley, and Jukka Corander. Robust analysis of prokaryotic pangenome gene gain and loss rates with panstripe. Genome Research, 33:129-140, Sep 2023. URL: https://doi.org/10.1101/2022.04.23.489244, doi:10.1101/2022.04.23.489244. This article has 62 citations and is from a highest quality peer-reviewed journal.

11. (wang2024comparativegenomicsunveils pages 15-17): Taiquan Wang, Yiling Shi, Mengzhuo Zheng, and Jinshui Zheng. Comparative genomics unveils functional diversity, pangenome openness, and underlying biological drivers among bacillus subtilis group. Microorganisms, 12:986, May 2024. URL: https://doi.org/10.3390/microorganisms12050986, doi:10.3390/microorganisms12050986. This article has 16 citations.

12. (liu2024integrativegenomicswould pages 7-8): Chinky Shiu Chen Liu and Rajesh Pandey. Integrative genomics would strengthen amr understanding through one health approach. Heliyon, 10:e34719, Jul 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e34719, doi:10.1016/j.heliyon.2024.e34719. This article has 22 citations.

13. (golchha2024bacterialpangenomea pages 5-6): Nikita Chordia Golchha, Anand Nighojkar, and Sadhana Nighojkar. Bacterial pangenome: a review on the current strategies, tools and applications. Medinformatics, Jun 2024. URL: https://doi.org/10.47852/bonviewmedin42022496, doi:10.47852/bonviewmedin42022496. This article has 7 citations.

14. (golchha2024bacterialpangenomea pages 6-7): Nikita Chordia Golchha, Anand Nighojkar, and Sadhana Nighojkar. Bacterial pangenome: a review on the current strategies, tools and applications. Medinformatics, Jun 2024. URL: https://doi.org/10.47852/bonviewmedin42022496, doi:10.47852/bonviewmedin42022496. This article has 7 citations.

15. (le2024efficientinferenceof pages 14-15): Duc Quang Le, Tien Anh Nguyen, Son Hoang Nguyen, Tam Thi Nguyen, Canh Hao Nguyen, Huong Thanh Phung, Tho Huu Ho, Nam S. Vo, Trang Nguyen, Hoang Anh Nguyen, and Minh Duc Cao. Efficient inference of large prokaryotic pangenomes with panta. Genome Biology, Aug 2024. URL: https://doi.org/10.1186/s13059-024-03362-z, doi:10.1186/s13059-024-03362-z. This article has 14 citations and is from a highest quality peer-reviewed journal.

16. (parmigiani2024revisitingpangenomeopenness pages 7-8): Luca Parmigiani, Roland Wittler, and Jens Stoye. Revisiting pangenome openness with k-mers. Peer Community Journal, Apr 2024. URL: https://doi.org/10.24072/pcjournal.415, doi:10.24072/pcjournal.415. This article has 12 citations and is from a peer-reviewed journal.

17. (wang2024comparativegenomicsunveils pages 1-2): Taiquan Wang, Yiling Shi, Mengzhuo Zheng, and Jinshui Zheng. Comparative genomics unveils functional diversity, pangenome openness, and underlying biological drivers among bacillus subtilis group. Microorganisms, 12:986, May 2024. URL: https://doi.org/10.3390/microorganisms12050986, doi:10.3390/microorganisms12050986. This article has 16 citations.

18. (tonkinhill2023robustanalysisof pages 7-8): Gerry Tonkin-Hill, Rebecca A Gladstone, Anna K Pöntinen, Sergio Arredondo-Alonso, Stephen D Bentley, and Jukka Corander. Robust analysis of prokaryotic pangenome gene gain and loss rates with panstripe. Genome Research, 33:129-140, Sep 2023. URL: https://doi.org/10.1101/2022.04.23.489244, doi:10.1101/2022.04.23.489244. This article has 62 citations and is from a highest quality peer-reviewed journal.

19. (golchha2024bacterialpangenomea pages 1-2): Nikita Chordia Golchha, Anand Nighojkar, and Sadhana Nighojkar. Bacterial pangenome: a review on the current strategies, tools and applications. Medinformatics, Jun 2024. URL: https://doi.org/10.47852/bonviewmedin42022496, doi:10.47852/bonviewmedin42022496. This article has 7 citations.

20. (tonkinhill2023robustanalysisof pages 10-11): Gerry Tonkin-Hill, Rebecca A Gladstone, Anna K Pöntinen, Sergio Arredondo-Alonso, Stephen D Bentley, and Jukka Corander. Robust analysis of prokaryotic pangenome gene gain and loss rates with panstripe. Genome Research, 33:129-140, Sep 2023. URL: https://doi.org/10.1101/2022.04.23.489244, doi:10.1101/2022.04.23.489244. This article has 62 citations and is from a highest quality peer-reviewed journal.

21. (parmigiani2024revisitingpangenomeopenness pages 14-16): Luca Parmigiani, Roland Wittler, and Jens Stoye. Revisiting pangenome openness with k-mers. Peer Community Journal, Apr 2024. URL: https://doi.org/10.24072/pcjournal.415, doi:10.24072/pcjournal.415. This article has 12 citations and is from a peer-reviewed journal.

22. (agarwal2023pangenomeinsightsinto pages 4-5): Viplav Agarwal, Rachel Stubits, Zain Nassrullah, and Marcus M. Dillon. Pangenome insights into the diversification and disease specificity of worldwide xanthomonas outbreaks. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1213261, doi:10.3389/fmicb.2023.1213261. This article has 17 citations and is from a peer-reviewed journal.