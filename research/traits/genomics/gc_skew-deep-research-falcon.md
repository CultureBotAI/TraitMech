---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:12:42.732538'
end_time: '2026-06-18T03:34:47.476585'
duration_seconds: 1324.74
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: GC skew
  trait_identifier: traitmech:000097
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: gc_skew
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A genome-sequence property describing strand asymmetry in guanine versus
    cytosine content between the leading and lagging replication strands, commonly
    used to locate the replication origin and terminus.
  parent_traits: METPO:1000188
  synonyms: strand compositional asymmetry
  evidence_summary: 'DOI:10.1093/oxfordjournals.molbev.a025626:  (Lobry first described
    asymmetric substitution patterns between the two DNA strands of bacteria, the
    basis of GC skew that marks replication boundaries.) | DOI:10.1016/S0378-1119(99)00297-8:  (Frank
    & Lobry review the mutational and selective mechanisms underlying strand compositional
    asymmetry.)'
  causal_graph_summary: 'gc_skew_replication_strand_asymmetry: 3 nodes, 2 edges'
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
- **Trait label:** GC skew
- **METPO identifier:** traitmech:000097
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genome-sequence property describing strand asymmetry in guanine versus cytosine content between the leading and lagging replication strands, commonly used to locate the replication origin and terminus.
- **Parent traits:** METPO:1000188
- **Synonyms:** strand compositional asymmetry
- **Existing evidence:** DOI:10.1093/oxfordjournals.molbev.a025626:  (Lobry first described asymmetric substitution patterns between the two DNA strands of bacteria, the basis of GC skew that marks replication boundaries.) | DOI:10.1016/S0378-1119(99)00297-8:  (Frank & Lobry review the mutational and selective mechanisms underlying strand compositional asymmetry.)
- **Existing causal graph summary:** gc_skew_replication_strand_asymmetry: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **GC skew** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_skew.yaml`.

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
- **Trait label:** GC skew
- **METPO identifier:** traitmech:000097
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genome-sequence property describing strand asymmetry in guanine versus cytosine content between the leading and lagging replication strands, commonly used to locate the replication origin and terminus.
- **Parent traits:** METPO:1000188
- **Synonyms:** strand compositional asymmetry
- **Existing evidence:** DOI:10.1093/oxfordjournals.molbev.a025626:  (Lobry first described asymmetric substitution patterns between the two DNA strands of bacteria, the basis of GC skew that marks replication boundaries.) | DOI:10.1016/S0378-1119(99)00297-8:  (Frank & Lobry review the mutational and selective mechanisms underlying strand compositional asymmetry.)
- **Existing causal graph summary:** gc_skew_replication_strand_asymmetry: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **GC skew** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_skew.yaml`.

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


## GC skew (traitmech:000097) — curation-focused research report

### Scope summary (Trait Scope)
GC skew is a genome-sequence property describing strand asymmetry in guanine versus cytosine content between the leading and lagging replication strands. It is commonly computed in windows as **(G−C)/(G+C)** and interpreted via its sign and changes along the chromosome; a **cumulative GC skew** (running sum across windows) is frequently used to more clearly detect polarity switches and locate replication boundaries (ori/ter). (grigoriev1998analyzinggenomeswith pages 1-2, mottez2023structuringeffectsof pages 1-4)

**What the trait represents.** For TraitMech curation, GC skew should be treated as (i) a **measurable sequence-derived metric** and (ii) a **proxy readout** of the combined effects of replication-associated mutational asymmetries, strand-specific repair, gene-orientation biases, and coding constraints that differ between leading and lagging strands. (mottez2023structuringeffectsof pages 1-4, paravel2026ontheorigins pages 2-3)

**Boundary cases / what it is not.** GC skew is not a universal or uniquely diagnostic marker of a single replication origin. Weak/atypical skew occurs in some taxa (e.g., many archaea/cyanobacteria), and skew signals can be confounded by multiple origins, alternative initiation (e.g., recombination-dependent replication), poorly defined termination zones, genome rearrangements/inversions, and horizontally acquired segments that locally invert or distort skew. (mottez2023structuringeffectsof pages 4-11, grigoriev1998analyzinggenomeswith pages 2-4, paravel2026ontheorigins pages 1-2)

### Key concepts and definitions (current understanding)
- **GC skew (windowed):** (G−C)/(G+C) in a sliding window. (grigoriev1998analyzinggenomeswith pages 1-2)
- **Cumulative GC skew:** running sum (“integration”) of windowed GC skew values; used to reduce noise relative to raw sliding-window plots. (grigoriev1998analyzinggenomeswith pages 1-2)
- **Interpretation rule of thumb (single-origin circular chromosomes):** cumulative GC skew global **minimum** often corresponds to **ori**, and global **maximum** often corresponds to **ter**; the extrema are commonly separated by ~50% genome length for bidirectional replication. (grigoriev1998analyzinggenomeswith pages 1-2)
- **Related nearby metrics:** AT skew, broader nucleotide-skew classes, and summary indices such as **SkewI/skewIT** (a genome-wide scalar measure) and **Div** (fitted predicted leading-strand fraction). (mottez2023structuringeffectsof pages 1-4, mottez2023structuringeffectsof pages 4-11)

### Recent developments and latest research (prioritizing 2023–2024)
#### 1) Quantitative cross-domain comparisons of skew amplitude (archaea vs bacteria)
Mottez et al. (bioRxiv, 2023) implemented SkewIT and quantified markedly lower archaeal skew than bacterial skew:
- **Archaea:** mean **SkewI = 0.27 ± 0.15 (n=807)**
- **Bacteria:** mean **SkewI = 0.82 ± 0.22 (n=15,067)**
- **Fold difference:** ~**3.42×** (bacteria:archaea)
They also report a strong correlation between C and G counts on single strands (R² ≈ 0.9997) despite measurable skew, and describe skew magnitudes as ~**7–8 excess G per 1000 bp** in archaea versus ~**23–25 excess G per 1000 bp** in bacteria (SkewDB-derived). (mottez2023structuringeffectsof pages 1-4)

These results support the curation warning that **archaeal GC skew is often low amplitude** and may reflect a different mixture of causal contributors than bacteria (e.g., greater contribution from coding constraints and gene density/orientation). (mottez2023structuringeffectsof pages 4-11)

#### 2) 2024 oriC prediction incorporating GC-skew-related disparities (real-world implementation)
Van Meel & Baaijens introduced **ORCA** (bioRxiv, March 2024), a Python tool to predict bacterial oriC sites by combining nucleotide-disparity curves (including GC-disparity/GC-skew visualization), **dnaA-box density**, and proximity to **indicator genes** (dnaA, dnaN), followed by a **Random Forest classifier** for confidence scoring. (meel2024orcapredictingreplication pages 1-4, meel2024orcapredictingreplication pages 4-6)

Key quantitative performance (DoriC 12.0 downloaded May 16, 2023; exp-set of 32 organisms with 37 validated origins): with a confidence threshold 0.50, ORCA reports **precision/recall = 0.98/0.93** on a 30% held-out set and **1.00/0.93** on the experimentally validated set (true positive defined as within 2% of chromosome length from the true origin). (meel2024orcapredictingreplication pages 4-6)

#### 3) 2023 GC-skew visualization automation
**GenoVi** (PLOS Comput Biol, April 2023) is a command-line pipeline for automated circular genome maps that explicitly calculates and plots GC skew, describing GC skew as an “over or under abundance of G or C between the leading and lagging DNA strands frequently used to identify the origin and terminus of replication.” GenoVi computes GC skew using **SkewIT** (user-settable window size; default 1,000 bp) and integrates other annotation layers for publication-ready figures. (cumsille2023genovianopensource pages 1-2, cumsille2023genovianopensource pages 2-4)

#### 4) Mechanistic refinement: sequence unzipping propensity and skewed palindromes
Sahu et al. (Journal of Molecular Evolution, Sep 2024) propose that **high-nucleotide-skew palindromic sequences** can function as potential replication origins due to **low kinetic barriers for local melting** and faster unzipping near melting temperatures; they report such sequences occur within/near origins across bacteria and archaea (and other replicons). This is a mechanistic hypothesis emphasizing **unzip kinetics** rather than purely thermodynamic stability. (sahu2024highnucleotideskew pages 1-3)

### Mechanistic entities (candidate nodes) and ontology grounding
The following table is a curator-facing starting set of candidate nodes, with suggested grounding where stable identifiers are available.

| Node label | Type | Brief description | Suggested grounding CURIE | Key supporting source(s) with DOI+year |
|---|---|---|---|---|
| GC skew | Trait/metric | Strand compositional asymmetry in G versus C content, typically computed per window as (G−C)/(G+C); used to mark leading/lagging strand transitions and infer ori/ter in many prokaryotic chromosomes. (mottez2023structuringeffectsof pages 1-4, grigoriev1998analyzinggenomeswith pages 1-2) | METPO:traitmech:000097 | 10.1101/2023.11.15.567178 (2023); 10.1093/nar/26.10.2286 (1998) |
| Cumulative GC skew | Trait/metric | Running sum of per-window GC skew values across the genome; global minima/maxima often correspond to replication origin/terminus in single-origin circular chromosomes. (grigoriev1998analyzinggenomeswith pages 1-2) |  | 10.1093/nar/26.10.2286 (1998); 10.1101/2023.11.15.567178 (2023) |
| SkewI / skewIT | Trait/metric | Genome-wide scalar index of GC imbalance used for comparative analysis of chromosomes and plasmids; lower on average in archaea than bacteria. (mottez2023structuringeffectsof pages 1-4, paravel2026ontheorigins pages 3-4) |  | 10.1101/2023.11.15.567178 (2023); 10.3389/fmicb.2026.1727296 (2026) |
| Div | Trait/metric | Fitted fraction of the chromosome predicted to be leading strand from GC-skew modeling; useful for assessing single-origin-like versus complex architectures. (mottez2023structuringeffectsof pages 4-11, paravel2026ontheorigins pages 2-3) |  | 10.1101/2023.11.15.567178 (2023); 10.3389/fmicb.2026.1727296 (2026) |
| GSB (gene strand bias) | Trait/metric | Cumulative measure of excess genes on one DNA strand; complementary to GC-skew analysis for genome organization and replication orientation. (paravel2026ontheorigins pages 2-3) |  | 10.3389/fmicb.2026.1727296 (2026) |
| Leading strand | Replication structures | Replication strand usually enriched for G over C in many bacterial genomes; central structural concept for interpreting GC skew. (grigoriev1998analyzinggenomeswith pages 1-2, mclean1998basecompositionskews pages 1-2) | GO:0006269 | 10.1093/nar/26.10.2286 (1998); 10.1007/pl00006428 (1998) |
| Lagging strand | Replication structures | Replication strand synthesized discontinuously; transient ssDNA exposure is implicated in skew-generating mutational asymmetry. (mottez2023structuringeffectsof pages 1-4, paravel2026ontheorigins pages 6-7) | GO:0006268 | 10.1101/2023.11.15.567178 (2023); 10.3389/fmicb.2026.1727296 (2026) |
| oriC / replication origin | Replication structures | Chromosomal origin of replication; often inferred from cumulative GC-skew minima and auxiliary sequence/gene features. (grigoriev1998analyzinggenomeswith pages 1-2, meel2024orcapredictingreplication pages 4-6) | GO:0003688 | 10.1093/nar/26.10.2286 (1998); 10.1101/2024.03.28.587133 (2024) |
| Replication terminus | Replication structures | Genomic region where opposing replication forks meet; often near cumulative GC-skew maxima in bidirectionally replicated chromosomes. (grigoriev1998analyzinggenomeswith pages 1-2) |  | 10.1093/nar/26.10.2286 (1998) |
| Cytosine deamination | Processes | Strand-biased mutational process proposed to contribute to GC skew, especially on lagging-strand ssDNA at replication forks. (mottez2023structuringeffectsof pages 1-4, paravel2026ontheorigins pages 6-7) | GO:0006307 | 10.1101/2023.11.15.567178 (2023); 10.3389/fmicb.2026.1727296 (2026) |
| Single-stranded DNA exposure | Processes | Unequal residence time in ssDNA during replication can increase damage/mutation asymmetry and thereby compositional skew. (grigoriev1998analyzinggenomeswith pages 4-4, mottez2023structuringeffectsof pages 1-4) | GO:0003697 | 10.1093/nar/26.10.2286 (1998); 10.1101/2023.11.15.567178 (2023) |
| Okazaki fragments | Processes | Discontinuous lagging-strand replication intermediates; archaeal short Okazaki fragments are hypothesized to reduce ssDNA exposure and skew amplitude. (mottez2023structuringeffectsof pages 4-11, paravel2026ontheorigins pages 6-7) | GO:0006268 | 10.1101/2023.11.15.567178 (2023); 10.3389/fmicb.2026.1727296 (2026) |
| DNA replication | Processes | Core process creating leading/lagging strand asymmetry and a primary mechanistic source of GC skew. (mottez2023structuringeffectsof pages 1-4, paravel2026ontheorigins pages 2-3) | GO:0006260 | 10.1101/2023.11.15.567178 (2023); 10.3389/fmicb.2026.1727296 (2026) |
| DNA repair | Processes | Broad category including strand-biased repair activities that can shape nucleotide asymmetry and skew amplitude. (paravel2026ontheorigins pages 6-7, paravel2026ontheorigins pages 1-2) | GO:0006281 | 10.3389/fmicb.2026.1727296 (2026) |
| Mismatch repair (MMR) | Processes | Strand-discriminating repair process implicated in bacterial skew generation; contrasted with likely non-strand-specific archaeal NucS/EndoMS systems. (paravel2026ontheorigins pages 6-7) | GO:0006298 | 10.3389/fmicb.2026.1727296 (2026) |
| Transcription-coupled nucleotide excision repair | Processes | Repair pathway proposed to contribute to strand compositional asymmetry alongside replication-linked mutation biases. (paravel2026ontheorigins pages 6-7, grigoriev1998analyzinggenomeswith pages 4-4) | GO:0006283 | 10.3389/fmicb.2026.1727296 (2026); 10.1093/nar/26.10.2286 (1998) |
| Recombination-dependent replication | Processes | Alternative initiation mode, especially relevant in archaea, that can weaken canonical oriC/ter GC-skew signatures. (paravel2026ontheorigins pages 1-2, mottez2023structuringeffectsof pages 1-4) | GO:0006310 | 10.3389/fmicb.2026.1727296 (2026); 10.1101/2023.11.15.567178 (2023) |
| Replication–transcription collision avoidance | Processes | Selective pressure favoring co-orientation of replication and transcription, contributing to gene strand bias and indirectly to GC skew. (mottez2023structuringeffectsof pages 4-11, mottez2023structuringeffectsof pages 1-4) | GO:0006260 | 10.1101/2023.11.15.567178 (2023) |
| Gene orientation / gene strand bias | Processes | Enrichment of genes on the leading strand is a major contributor to strand compositional asymmetry in many microbes. (mottez2023structuringeffectsof pages 4-11, mclean1998basecompositionskews pages 1-2) |  | 10.1101/2023.11.15.567178 (2023); 10.1007/pl00006428 (1998) |
| Translational selection / codon-position bias | Processes | Coding-sequence and codon-position effects, especially first- and third-position contributions, shape observed GC-skew patterns. (mottez2023structuringeffectsof pages 4-11, paravel2026ontheorigins pages 1-2) | GO:0006412 | 10.1101/2023.11.15.567178 (2023); 10.3389/fmicb.2026.1727296 (2026) |
| DnaA | Genes/proteins | Bacterial replication initiator protein; proximity to candidate origins is used by ORCA and other oriC inference frameworks. (meel2024orcapredictingreplication pages 4-6, mottez2023structuringeffectsof pages 11-12) | UniProt:P03004 | 10.1101/2024.03.28.587133 (2024) |
| DnaN | Genes/proteins | DNA polymerase III beta sliding clamp gene used by ORCA as an origin-proximal indicator gene. (meel2024orcapredictingreplication pages 1-4, meel2024orcapredictingreplication pages 4-6) | UniProt:P0A988 | 10.1101/2024.03.28.587133 (2024) |
| Orc1 | Genes/proteins | Archaeal origin-recognition/initiation protein associated with replication origins and linked to replication, repair, and transcriptional organization. (mottez2023structuringeffectsof pages 4-11) | UniProt:Q9Y805 | 10.1101/2023.11.15.567178 (2023) |
| PCNA | Genes/proteins | DNA sliding clamp in archaea; part of origin-associated replication/repair networks discussed in relation to skew-linked chromosome organization. (mottez2023structuringeffectsof pages 4-11, mottez2023structuringeffectsof pages 11-12) | GO:0031261 | 10.1101/2023.11.15.567178 (2023) |
| RadA | Genes/proteins | Archaeal recombinase implicated in recombination-associated DNA synthesis and alternative replication initiation. (mottez2023structuringeffectsof pages 1-4, paravel2026ontheorigins pages 1-2) | UniProt:Q9Y7A1 | 10.1101/2023.11.15.567178 (2023); 10.3389/fmicb.2026.1727296 (2026) |
| PolD | Genes/proteins | Archaeal DNA polymerase participating in recombination-associated DNA synthesis and replication. (mottez2023structuringeffectsof pages 1-4, paravel2026ontheorigins pages 1-2) |  | 10.1101/2023.11.15.567178 (2023); 10.3389/fmicb.2026.1727296 (2026) |
| PolB | Genes/proteins | Archaeal family-B DNA polymerase participating in recombination-associated DNA synthesis and replication. (mottez2023structuringeffectsof pages 1-4, paravel2026ontheorigins pages 1-2) |  | 10.1101/2023.11.15.567178 (2023); 10.3389/fmicb.2026.1727296 (2026) |
| Hel308 | Genes/proteins | Archaeal helicase mentioned among origin-associated repair/replication factors potentially linked to genome organization and skew. (mottez2023structuringeffectsof pages 4-11) |  | 10.1101/2023.11.15.567178 (2023) |
| EndoV | Genes/proteins | DNA repair endonuclease discussed among archaeal origin-associated factors. (mottez2023structuringeffectsof pages 4-11) |  | 10.1101/2023.11.15.567178 (2023) |
| NucS / EndoMS | Genes/proteins | Non-canonical archaeal mismatch-repair factor likely lacking strand-specific bias, proposed to reduce repair-driven GC skew. (paravel2026ontheorigins pages 6-7, mottez2023structuringeffectsof pages 4-11) |  | 10.3389/fmicb.2026.1727296 (2026); 10.1101/2023.11.15.567178 (2023) |
| MutS | Genes/proteins | Canonical bacterial mismatch repair protein implicated in strand-specific repair contributions to skew. (paravel2026ontheorigins pages 6-7) | GO:0006298 | 10.3389/fmicb.2026.1727296 (2026) |
| MutL | Genes/proteins | Canonical bacterial mismatch repair protein implicated in strand-specific repair contributions to skew. (paravel2026ontheorigins pages 6-7) | GO:0006298 | 10.3389/fmicb.2026.1727296 (2026) |
| dnaA boxes | DNA features/motifs | Short origin-associated sequence motifs enriched near bacterial oriC; counted by ORCA for ori prediction. (meel2024orcapredictingreplication pages 1-4, meel2024orcapredictingreplication pages 4-6) | SO:0000704 | 10.1101/2024.03.28.587133 (2024) |
| High-skew palindromic DNA | DNA features/motifs | Sequence class proposed to have low local unzipping barriers and to occur near replication origins in bacteria, archaea, plasmids, and mitochondria. (sahu2024highnucleotideskew pages 1-3, sahu2024highnucleotideskewa pages 17-18) | SO:0000444 | 10.1007/s00239-024-10202-y (2024); 10.48550/arXiv.2407.13260 (2024) |
| Genome rearrangement / inversion | DNA features/motifs | Structural events that distort local cumulative GC-skew profiles and can confound ori/ter inference. (grigoriev1998analyzinggenomeswith pages 2-4, grigoriev1998analyzinggenomeswith pages 1-2) | SO:1000036 | 10.1093/nar/26.10.2286 (1998) |
| Horizontally transferred / foreign DNA segment | DNA features/motifs | Integrated foreign DNA can produce local skew anomalies that mimic replication-linked extrema. (grigoriev1998analyzinggenomeswith pages 2-4) |  | 10.1093/nar/26.10.2286 (1998) |
| ORCA | Tools/resources | 2024 open-source Python tool for circular prokaryotic oriC prediction using GC disparity/GC-skew-related curves, dnaA boxes, and indicator genes. (meel2024orcapredictingreplication pages 1-4, meel2024orcapredictingreplication pages 4-6) |  | 10.1101/2024.03.28.587133 (2024) |
| GenoVi | Tools/resources | 2023 automated circular genome visualizer that computes and plots GC skew for bacterial and archaeal genomes. (cumsille2023genovianopensource pages 2-4, cumsille2023genovianopensource pages 1-2) |  | 10.1371/journal.pcbi.1010998 (2023) |
| SkewDB | Tools/resources | Large comparative database of precomputed nucleotide and cumulative skews across bacterial and archaeal replicons. (paravel2026ontheorigins pages 3-4, mottez2023structuringeffectsof pages 1-4) |  | 10.3389/fmicb.2026.1727296 (2026); 10.1101/2023.11.15.567178 (2023) |


*Table: This table lists curator-facing candidate nodes for a TraitMech causal graph of GC skew, organized by node type and linked to supporting evidence. It is useful for selecting graph entities that are mechanistically relevant, computationally measurable, and citable.*

### Evidence-backed candidate causal edges (triples)
Edges below include both (i) **biological causal contributors** and (ii) **analysis/inference edges** (e.g., extrema → ori/ter calls), which are often essential for TraitMech curation but should be tagged appropriately as “computational inference” rather than “biophysical causation.”

| Edge (subject–predicate–object) | Strength | Evidence snippet | Source (DOI + year + URL) | Notes for curation |
|---|---|---|---|---|
| DNA replication fork strand asymmetry → contributes_to → GC skew | strong | “GC skew… used to map leading/lagging strand transitions”; strand compositional asymmetry is linked to “strand-specific biases in DNA replication.” (mottez2023structuringeffectsof pages 1-4, paravel2026ontheorigins pages 2-3) | 10.1101/2023.11.15.567178 (2023) https://doi.org/10.1101/2023.11.15.567178; 10.3389/fmicb.2026.1727296 (2026) https://doi.org/10.3389/fmicb.2026.1727296 | Core high-level edge for the trait. Mechanistic but broad; applies most strongly to circular bacterial chromosomes with clear leading/lagging strand polarity. |
| Lagging-strand single-stranded DNA exposure → increases → cytosine deamination | medium | The lagging strand is “exposed as ssDNA, increasing cytosine-to-thymine mutations and thus contributing to GC skew.” (mottez2023structuringeffectsof pages 1-4) | 10.1101/2023.11.15.567178 (2023) https://doi.org/10.1101/2023.11.15.567178 | Good mechanistic edge, especially for bacteria; evidence in archaeal discussion is inferential rather than a direct perturbation experiment. |
| Cytosine deamination at replication forks → contributes_to → GC skew | medium | “Cytosine deamination at the replication fork is explicitly implicated in generating GC skew.” (paravel2026ontheorigins pages 6-7) | 10.3389/fmicb.2026.1727296 (2026) https://doi.org/10.3389/fmicb.2026.1727296 | Useful mechanistic edge, but cite as cross-domain/general model; stronger in bacterial literature than archaeal systems. |
| Short archaeal Okazaki fragments → decreases → strand-specific cytosine deamination | uncertain | “The relatively short size of Okazaki fragments in archaea… may limit strand-specific cytosine deamination.” (mottez2023structuringeffectsof pages 4-11) | 10.1101/2023.11.15.567178 (2023) https://doi.org/10.1101/2023.11.15.567178 | Hypothesis-level edge; should be flagged uncertain and likely archaeal-specific. |
| Short archaeal Okazaki fragments → weakens → GC skew amplitude | uncertain | Short Okazaki fragments “may limit strand-specific cytosine deamination at forks, reducing replication-driven skew.” (mottez2023structuringeffectsof pages 4-11) | 10.1101/2023.11.15.567178 (2023) https://doi.org/10.1101/2023.11.15.567178 | Downstream inferred edge from prior mechanism; useful as explanatory note, but probably not ready for strong curation. |
| Co-orientation of replication and transcription → reduces → head-on replisome–RNA polymerase collisions | strong | “Co-orientation of replication and transcription reduces head-on replisome–RNA polymerase collisions.” (mottez2023structuringeffectsof pages 4-11) | 10.1101/2023.11.15.567178 (2023) https://doi.org/10.1101/2023.11.15.567178 | Strong biological-process edge; not GC-skew-specific by itself but relevant to strand bias mechanisms. |
| Selection to avoid replication–transcription collisions → enriches_on_leading_strand → gene orientation bias | medium | Origins may help prevent “head-to-head collisions,” and preferred leading-strand gene location evolved “to reduce conflicts between replication and transcription.” (mottez2023structuringeffectsof pages 1-4, mottez2023structuringeffectsof pages 4-11) | 10.1101/2023.11.15.567178 (2023) https://doi.org/10.1101/2023.11.15.567178 | Curate as gene strand bias / collision avoidance, not as a direct physical causation on GC skew alone. |
| Leading-strand gene density / gene strand bias → contributes_to → GC skew | strong | “Biased gene density on leading vs lagging strands is highlighted as a major contributor” to skew. (mottez2023structuringeffectsof pages 4-11) | 10.1101/2023.11.15.567178 (2023) https://doi.org/10.1101/2023.11.15.567178 | Strong candidate edge, especially for archaeal genomes where coding bias can dominate weak replication mutational effects. |
| Translational selection and genetic code constraints → contribute_to → asymmetric G/C distributions | medium | “Translational selection and the nature of the genetic code are universal determinants of asymmetric G/C distributions.” (paravel2026ontheorigins pages 1-2) | 10.3389/fmicb.2026.1727296 (2026) https://doi.org/10.3389/fmicb.2026.1727296 | Broad evolutionary claim; strong comparative support but less direct than a molecular perturbation. |
| First-codon-position G excess → increases → coding-region GC skew | medium | There is a “strong excess of G at the first codon position” and codon-position biases contribute to skew. (mottez2023structuringeffectsof pages 4-11) | 10.1101/2023.11.15.567178 (2023) https://doi.org/10.1101/2023.11.15.567178 | Codon-position-specific edge; probably best modeled as coding-sequence contribution rather than whole-genome universal rule. |
| Third-codon-position mutational bias → contributes_to → strand compositional asymmetry | medium | Mutation-related variation is “detectable at the third degenerate codon position” and third-position skews “probably reflect mutational biases.” (paravel2026ontheorigins pages 2-3, mclean1998basecompositionskews pages 1-2) | 10.3389/fmicb.2026.1727296 (2026) https://doi.org/10.3389/fmicb.2026.1727296; 10.1007/pl00006428 (1998) https://doi.org/10.1007/pl00006428 | Useful because it separates mutational from protein-coding constraints. |
| Strand-specific DNA repair (MutSL-dependent mismatch repair / transcription-coupled NER) → contributes_to → GC skew | medium | “Strand-specific DNA repair pathways (MutSL-dependent MMR, transcription-coupled nucleotide excision repair) contribute to asymmetry.” (paravel2026ontheorigins pages 6-7) | 10.3389/fmicb.2026.1727296 (2026) https://doi.org/10.3389/fmicb.2026.1727296 | Strong conceptual edge, but evidence summary is comparative/review-like; direct causal experiments are outside the cited excerpt. |
| Archaeal NucS/EndoMS mismatch repair → lacks → strand-specific repair bias | uncertain | Archaeal “NucS/EndoMS-based MMR is non-canonical and likely not strand-specific, potentially reducing repair-driven skew.” (paravel2026ontheorigins pages 6-7) | 10.3389/fmicb.2026.1727296 (2026) https://doi.org/10.3389/fmicb.2026.1727296 | Taxon-specific and hedged (“likely”); should be curated only with uncertainty. |
| Reduced strand-specific mutation/repair in archaea → decreases → GC skew amplitude | medium | Archaea show a “reduced ability to create strand-specific mutations or repair,” corresponding to lower skew amplitude. (paravel2026ontheorigins pages 1-2, mottez2023structuringeffectsof pages 1-4) | 10.3389/fmicb.2026.1727296 (2026) https://doi.org/10.3389/fmicb.2026.1727296; 10.1101/2023.11.15.567178 (2023) https://doi.org/10.1101/2023.11.15.567178 | Comparative domain-level edge; good explanatory note for weak archaeal GC skew. |
| Cumulative GC skew global minimum → indicates → replication origin (ori) | strong | “The global minimum” of cumulative GC skew “tends to mark the origin.” (grigoriev1998analyzinggenomeswith pages 1-2) | 10.1093/nar/26.10.2286 (1998) https://doi.org/10.1093/nar/26.10.2286 | Canonical inference edge; describes assay/analysis interpretation rather than a biological mechanism. |
| Cumulative GC skew global maximum → indicates → replication terminus (ter) | strong | “The global maximum generally maps to the terminus.” (grigoriev1998analyzinggenomeswith pages 1-2) | 10.1093/nar/26.10.2286 (1998) https://doi.org/10.1093/nar/26.10.2286 | Same caution as above: robust analysis edge, especially for single-origin circular chromosomes. |
| Multiple replication origins / alternative initiation / poorly defined termination zones → weakens → GC-skew-based ori/ter inference | strong | Many archaea and cyanobacteria exhibit “multiple replication origins, alternative replication initiation mechanism and/or poorly defined replication termination zones,” which confound inference. (mottez2023structuringeffectsof pages 4-11) | 10.1101/2023.11.15.567178 (2023) https://doi.org/10.1101/2023.11.15.567178 | Important negative/boundary-case edge; essential warning for curation. |
| Genome rearrangements / inversions / foreign DNA integration → distorts → cumulative GC skew extrema | strong | Local extrema can reflect “inversions, translocations… or foreign DNA integration,” producing local distortions in cumulative plots. (grigoriev1998analyzinggenomeswith pages 2-4, grigoriev1998analyzinggenomeswith pages 1-2) | 10.1093/nar/26.10.2286 (1998) https://doi.org/10.1093/nar/26.10.2286 | Important confounder edge for trait interpretation; better treated as caution than intrinsic mechanism. |
| dnaA-box density near candidate loci → supports_inference_of → oriC | medium | ORCA assigns a D-score from the count of “dnaA-boxes” (default motif TTATNCACA) around candidate sites. (meel2024orcapredictingreplication pages 1-4, meel2024orcapredictingreplication pages 4-6) | 10.1101/2024.03.28.587133 (2024) https://doi.org/10.1101/2024.03.28.587133 | Computational inference edge, not universal biological causation; strongest in bacteria with DnaA-based oriC organization. |
| Proximity of indicator genes dnaA and dnaN to candidate loci → supports_inference_of → oriC | medium | ORCA uses a G-score based on proximity to “indicator genes dnaA and dnaN.” (meel2024orcapredictingreplication pages 1-4, meel2024orcapredictingreplication pages 4-6) | 10.1101/2024.03.28.587133 (2024) https://doi.org/10.1101/2024.03.28.587133 | Another inference edge; useful for annotation pipelines, but not a direct mechanistic cause of GC skew. |


*Table: This table lists candidate causal and inference edges relevant to GC skew curation in TraitMech, with evidence, citations, and caveats. It is designed to help prioritize which relationships are strong enough for curation and which should remain uncertain or assay-specific.*

### Current applications and real-world implementations
1. **Genome annotation and replication boundary inference:** cumulative GC skew extrema are used to propose ori/ter locations; classic evidence shows extrema align closely with known/putative boundaries across multiple microbes, with Table 1 and Figure panels demonstrating this correspondence. (grigoriev1998analyzinggenomeswith media 5fbe1148, grigoriev1998analyzinggenomeswith media 0dfe1e90)
2. **High-throughput origin prediction pipelines:** ORCA operationalizes GC-disparity/GC-skew signals together with dnaA-box density and indicator genes, providing precision/recall metrics on DoriC and an experimentally validated set. (meel2024orcapredictingreplication pages 4-6)
3. **Visualization for comparative genomics:** GenoVi offers standardized GC-skew computation and circular visualization for complete and draft genomes, intended for single-genome and comparative studies. (cumsille2023genovianopensource pages 1-2, cumsille2023genovianopensource pages 2-4)

### Expert opinions / synthesis from authoritative sources
- **GC skew is multi-causal.** Recent comparative analyses emphasize that GC skew can reflect replication-associated mutation/repair biases, but also gene density/orientation, transcription/translation constraints, and codon-position effects—especially in archaea where skew amplitude is lower and may be dominated by coding-related signals. (mottez2023structuringeffectsof pages 4-11, paravel2026ontheorigins pages 1-2)
- **Archaea are a key boundary case.** Multiple origins, alternative initiation, and reduced strand-specific mutation/repair can weaken canonical bacterial-like GC-skew signals and complicate ori/ter inference; cumulative approaches can help but should be combined with other evidence (origin-binding proteins, motif enrichment, marker genes). (mottez2023structuringeffectsof pages 4-11, paravel2026ontheorigins pages 1-2)

### Statistics and data highlights (recent)
- **Skew amplitude differences:** archaeal SkewI 0.27±0.15 (n=807) vs bacterial SkewI 0.82±0.22 (n=15,067); bacteria show ~3.42× higher SkewI; archaeal skew magnitude ~7–8 excess G/1000 bp vs bacterial ~23–25 excess G/1000 bp (SkewDB-derived). (mottez2023structuringeffectsof pages 1-4)
- **Genome-scale dataset sizes in skew studies:** bacterial comparison set of 15,067 genomes representing 4,471 species and 1,148 genera (Mottez 2023). (mottez2023structuringeffectsof pages 4-11)
- **ORCA prediction accuracy:** precision/recall 0.98/0.93 (held-out) and 1.00/0.93 (experimentally validated) using DoriC 12.0 (downloaded May 16, 2023) and a definition of TP within 2% chromosome length of true origin. (meel2024orcapredictingreplication pages 4-6)

### Warnings (claims not yet ready for strong curation)
1. **Okazaki fragment length → cytosine deamination → skew amplitude** is presented as a plausible mechanistic explanation for lower archaeal skew, but is explicitly hedged (e.g., “may limit”) and should be curated as **uncertain** unless additional primary experimental evidence is added. (mottez2023structuringeffectsof pages 4-11)
2. **High-skew palindromic sequences as universal origin determinants** is an interesting 2024 hypothesis but currently better curated as a **candidate contributing DNA feature** rather than a broadly causal, necessary origin mechanism (not necessary/sufficient across taxa). (sahu2024highnucleotideskew pages 1-3)
3. **Inference edges (extrema → ori/ter)** should be tagged as **computational/assay interpretation** rather than biological mechanism, and restricted to appropriate genome architectures (single-origin circular chromosomes). (grigoriev1998analyzinggenomeswith pages 1-2, mottez2023structuringeffectsof pages 4-11)

---

## DOI-first bibliography (with URLs and publication dates where available)
- Mottez C, Puech R, Flament D, Myllykallio H. *Structuring effects of archaeal replication origins.* bioRxiv (Nov 2023). https://doi.org/10.1101/2023.11.15.567178 (mottez2023structuringeffectsof pages 1-4)
- van Meel Z, Baaijens JA. *ORCA: Predicting replication origins in circular prokaryotic chromosomes.* bioRxiv (Mar 2024). https://doi.org/10.1101/2024.03.28.587133 (meel2024orcapredictingreplication pages 1-4, meel2024orcapredictingreplication pages 4-6)
- Cumsille A, Durán RE, Rodríguez-Delherbe A, et al. *GenoVi, an open-source automated circular genome visualizer for bacteria and archaea.* PLOS Computational Biology (Apr 2023). https://doi.org/10.1371/journal.pcbi.1010998 (cumsille2023genovianopensource pages 1-2, cumsille2023genovianopensource pages 2-4)
- Sahu P, Barik S, Ghosh K, Subramanian H. *High Nucleotide Skew Palindromic DNA Sequences Function as Potential Replication Origins due to their Unzipping Propensity.* Journal of Molecular Evolution 92(6):761–775 (Sep 2024). https://doi.org/10.1007/s00239-024-10202-y (sahu2024highnucleotideskew pages 1-3)
- Grigoriev A. *Analyzing genomes with cumulative skew diagrams.* Nucleic Acids Research 26(10):2286–2290 (May 1998). https://doi.org/10.1093/nar/26.10.2286 (grigoriev1998analyzinggenomeswith pages 1-2, grigoriev1998analyzinggenomeswith media 5fbe1148)

## Notes for TraitMech YAML drafting
The artifacts above are intended to be transcribed into `data/traits/genomics/gc_skew.yaml` as candidate nodes/edges with explicit tags for (i) mechanistic causation versus (ii) computational inference. Where edges are hedged (“may,” “likely”), they should be marked **uncertain** and/or restricted by taxon (e.g., archaea) and genome architecture (single-origin circular vs multi-origin).


References

1. (grigoriev1998analyzinggenomeswith pages 1-2): A. Grigoriev. Analyzing genomes with cumulative skew diagrams. Nucleic acids research, 26 10:2286-90, May 1998. URL: https://doi.org/10.1093/nar/26.10.2286, doi:10.1093/nar/26.10.2286. This article has 550 citations and is from a highest quality peer-reviewed journal.

2. (mottez2023structuringeffectsof pages 1-4): Clémence Mottez, Romain Puech, Didier Flament, and Hannu Myllykallio. Structuring effects of archaeal replication origins. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.15.567178, doi:10.1101/2023.11.15.567178. This article has 1 citations.

3. (paravel2026ontheorigins pages 2-3): Adrien Paravel, Clémence Mottez, Romain Puech, Didier Flament, Hubert F. Becker, and Hannu Myllykallio. On the origins and variation of nucleotide skews of archaeal genomes. Frontiers in Microbiology, Mar 2026. URL: https://doi.org/10.3389/fmicb.2026.1727296, doi:10.3389/fmicb.2026.1727296. This article has 0 citations and is from a peer-reviewed journal.

4. (mottez2023structuringeffectsof pages 4-11): Clémence Mottez, Romain Puech, Didier Flament, and Hannu Myllykallio. Structuring effects of archaeal replication origins. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.15.567178, doi:10.1101/2023.11.15.567178. This article has 1 citations.

5. (grigoriev1998analyzinggenomeswith pages 2-4): A. Grigoriev. Analyzing genomes with cumulative skew diagrams. Nucleic acids research, 26 10:2286-90, May 1998. URL: https://doi.org/10.1093/nar/26.10.2286, doi:10.1093/nar/26.10.2286. This article has 550 citations and is from a highest quality peer-reviewed journal.

6. (paravel2026ontheorigins pages 1-2): Adrien Paravel, Clémence Mottez, Romain Puech, Didier Flament, Hubert F. Becker, and Hannu Myllykallio. On the origins and variation of nucleotide skews of archaeal genomes. Frontiers in Microbiology, Mar 2026. URL: https://doi.org/10.3389/fmicb.2026.1727296, doi:10.3389/fmicb.2026.1727296. This article has 0 citations and is from a peer-reviewed journal.

7. (meel2024orcapredictingreplication pages 1-4): Zoya van Meel and Jasmijn A. Baaijens. Orca: predicting replication origins in circular prokaryotic chromosomes. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.28.587133, doi:10.1101/2024.03.28.587133. This article has 0 citations.

8. (meel2024orcapredictingreplication pages 4-6): Zoya van Meel and Jasmijn A. Baaijens. Orca: predicting replication origins in circular prokaryotic chromosomes. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.28.587133, doi:10.1101/2024.03.28.587133. This article has 0 citations.

9. (cumsille2023genovianopensource pages 1-2): Andrés Cumsille, Roberto E. Durán, Andrea Rodríguez-Delherbe, Vicente Saona-Urmeneta, Beatriz Cámara, Michael Seeger, Mauricio Araya, Nicolás Jara, and Carlos Buil-Aranda. Genovi, an open-source automated circular genome visualizer for bacteria and archaea. Apr 2023. URL: https://doi.org/10.1371/journal.pcbi.1010998, doi:10.1371/journal.pcbi.1010998. This article has 125 citations and is from a highest quality peer-reviewed journal.

10. (cumsille2023genovianopensource pages 2-4): Andrés Cumsille, Roberto E. Durán, Andrea Rodríguez-Delherbe, Vicente Saona-Urmeneta, Beatriz Cámara, Michael Seeger, Mauricio Araya, Nicolás Jara, and Carlos Buil-Aranda. Genovi, an open-source automated circular genome visualizer for bacteria and archaea. Apr 2023. URL: https://doi.org/10.1371/journal.pcbi.1010998, doi:10.1371/journal.pcbi.1010998. This article has 125 citations and is from a highest quality peer-reviewed journal.

11. (sahu2024highnucleotideskew pages 1-3): Parthasarathi Sahu, Sashikanta Barik, Koushik Ghosh, and Hemachander Subramanian. High nucleotide skew palindromic dna sequences function as potential replication origins due to their unzipping propensity. Sep 2024. URL: https://doi.org/10.1007/s00239-024-10202-y, doi:10.1007/s00239-024-10202-y. This article has 4 citations and is from a peer-reviewed journal.

12. (paravel2026ontheorigins pages 3-4): Adrien Paravel, Clémence Mottez, Romain Puech, Didier Flament, Hubert F. Becker, and Hannu Myllykallio. On the origins and variation of nucleotide skews of archaeal genomes. Frontiers in Microbiology, Mar 2026. URL: https://doi.org/10.3389/fmicb.2026.1727296, doi:10.3389/fmicb.2026.1727296. This article has 0 citations and is from a peer-reviewed journal.

13. (mclean1998basecompositionskews pages 1-2): Michael J. McLean, Kenneth H. Wolfe, and Kevin M. Devine. Base composition skews, replication orientation, and gene orientation in 12 prokaryote genomes. Journal of Molecular Evolution, 47:691-696, Dec 1998. URL: https://doi.org/10.1007/pl00006428, doi:10.1007/pl00006428. This article has 369 citations and is from a peer-reviewed journal.

14. (paravel2026ontheorigins pages 6-7): Adrien Paravel, Clémence Mottez, Romain Puech, Didier Flament, Hubert F. Becker, and Hannu Myllykallio. On the origins and variation of nucleotide skews of archaeal genomes. Frontiers in Microbiology, Mar 2026. URL: https://doi.org/10.3389/fmicb.2026.1727296, doi:10.3389/fmicb.2026.1727296. This article has 0 citations and is from a peer-reviewed journal.

15. (grigoriev1998analyzinggenomeswith pages 4-4): A. Grigoriev. Analyzing genomes with cumulative skew diagrams. Nucleic acids research, 26 10:2286-90, May 1998. URL: https://doi.org/10.1093/nar/26.10.2286, doi:10.1093/nar/26.10.2286. This article has 550 citations and is from a highest quality peer-reviewed journal.

16. (mottez2023structuringeffectsof pages 11-12): Clémence Mottez, Romain Puech, Didier Flament, and Hannu Myllykallio. Structuring effects of archaeal replication origins. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.15.567178, doi:10.1101/2023.11.15.567178. This article has 1 citations.

17. (sahu2024highnucleotideskewa pages 17-18): Parthasarathi Sahu, Sashikanta Barik, Koushik Ghosh, and Hemachander Subramanian. High nucleotide skew palindromic dna sequences function as replication origins due to their unzipping propensity. Preprint, Jan 2024. URL: https://doi.org/10.48550/arxiv.2407.13260, doi:10.48550/arxiv.2407.13260. This article has 0 citations.

18. (grigoriev1998analyzinggenomeswith media 5fbe1148): A. Grigoriev. Analyzing genomes with cumulative skew diagrams. Nucleic acids research, 26 10:2286-90, May 1998. URL: https://doi.org/10.1093/nar/26.10.2286, doi:10.1093/nar/26.10.2286. This article has 550 citations and is from a highest quality peer-reviewed journal.

19. (grigoriev1998analyzinggenomeswith media 0dfe1e90): A. Grigoriev. Analyzing genomes with cumulative skew diagrams. Nucleic acids research, 26 10:2286-90, May 1998. URL: https://doi.org/10.1093/nar/26.10.2286, doi:10.1093/nar/26.10.2286. This article has 550 citations and is from a highest quality peer-reviewed journal.