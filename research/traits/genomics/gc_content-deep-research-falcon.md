---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:00:49.556140'
end_time: '2026-06-18T03:11:32.970808'
duration_seconds: 643.41
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: GC content
  trait_identifier: METPO:1000127
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: gc_content
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A quality that is describing the percentage of guanine and cytosine
    nucleotides in genomic DNA, calculated as the ratio of GC base pairs to total
    base pairs.
  parent_traits: METPO:1000188
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports
    GC content as a fundamental genome-composition descriptor varying widely across
    prokaryotic lineages.) | DOI:10.1186/1471-2148-10-374: GC-biased gene conversion
    (Bacterial-GC-content evolution review supports GC-biased gene conversion and
    mutation bias as the mechanistic drivers of genomic GC composition.)'
  causal_graph_summary: 'gc_content_composition_drivers: 9 nodes, 8 edges'
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
- **Trait label:** GC content
- **METPO identifier:** METPO:1000127
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that is describing the percentage of guanine and cytosine nucleotides in genomic DNA, calculated as the ratio of GC base pairs to total base pairs.
- **Parent traits:** METPO:1000188
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports GC content as a fundamental genome-composition descriptor varying widely across prokaryotic lineages.) | DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports GC-biased gene conversion and mutation bias as the mechanistic drivers of genomic GC composition.)
- **Existing causal graph summary:** gc_content_composition_drivers: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **GC content** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_content.yaml`.

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
- **Trait label:** GC content
- **METPO identifier:** METPO:1000127
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A quality that is describing the percentage of guanine and cytosine nucleotides in genomic DNA, calculated as the ratio of GC base pairs to total base pairs.
- **Parent traits:** METPO:1000188
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports GC content as a fundamental genome-composition descriptor varying widely across prokaryotic lineages.) | DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports GC-biased gene conversion and mutation bias as the mechanistic drivers of genomic GC composition.)
- **Existing causal graph summary:** gc_content_composition_drivers: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **GC content** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_content.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Genomic GC content (METPO:1000127)

### 1) Scope summary (trait definition, boundaries, assays)

**Trait definition (curation target).** Microbial genomic **GC content** is the percentage (or fraction) of guanine and cytosine nucleotides in genomic DNA; in comparative genomics it is treated as a stable genome trait with wide interspecies variation. Across prokaryotes, GC content spans **~16–77%** in large compilations (and bacterial genomic GC shows a bimodal distribution in one large bacterial survey). (aliperti2023rkselectionof pages 1-3, teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 2-5)

**What the trait represents.** For TraitMech curation, **GC content should be interpreted as a genome-composition descriptor** (genome-wide %GC) that reflects (i) long-term mutational biases and DNA replication/repair systems, and (ii) selective/ecological constraints that couple nucleotide composition to codon usage and amino-acid usage. (teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 2-5, aliperti2023rkselectionof pages 3-6)

**Assay/measurement variants and boundary cases.** Recent work highlights that “GC content” is operationalized in multiple ways:
- **Whole-genome GC (GCw)**, GC in **chromosomal** sequence, **plasmid** sequence, **core vs accessory genes**, and **structural RNA genes** (tRNAs/rRNAs) may behave differently in correlations with environment. (hu2022apositivecorrelation pages 1-2)
- GC can be measured specifically in **protein-coding sequences (GCp)**, at **third codon positions (GC3)**, and at **four-fold degenerate sites** as a proxy for “silent-site” composition. (hu2022apositivecorrelation pages 13-15)
- In bacteria, GC can also be separated into **coding vs noncoding GC** (GCCDS vs GCNCS), and further decomposed into GC attributable to **amino-acid usage vs synonymous codon usage** (useful for mechanistic graphs linking GC↔proteome). (teng2023genomiclegaciesof pages 12-13)

**Practical curation note (proxy use).** Coding-sequence GC content is often used when whole-genome GC is unavailable; a large compilation found CDS-GC closely tracks genome-wide GC (**Spearman r = 0.99**), supporting proxy use in cross-study harmonization. (aliperti2023rkselectionof pages 1-3)

### 2) Current understanding: key concepts and mechanistic hypotheses

**(A) Mutation bias and DNA replication/repair (DRR) as mechanistic drivers.** A 2023 large-scale bacterial analysis argues that GC variation is well explained by differences in **DNA replication, damage, and repair (DRR)**, framing a model in which ancient lineage-specific adaptation reshaped DRR systems and thereby altered long-term mutational spectra that determine genomic GC. (teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 2-5)

Mechanistic processes explicitly linked to GC shifts in that work include:
- **Cytosine deamination** lowering GC content (C→T transitions). (teng2023genomiclegaciesof pages 10-12)
- **Oxidative guanine lesions (8-oxoG)** causing mispairing (A:8-oxoG), affecting mutation spectra. (teng2023genomiclegaciesof pages 8-10, teng2023genomiclegaciesof pages 10-12)
- **Error-prone polymerases / translesion synthesis (TLS)** proposed to increase genomic GC in the authors’ model, with specific polymerases and repair genes (e.g., **DnaE2**, **MutS2**) strongly correlated with GC across genomes. (teng2023genomiclegaciesof pages 10-12, teng2023genomiclegaciesof pages 2-5)

**(B) Selection/ecology-mediated mechanisms (resource costs; proteome coupling).** GC content is tightly coupled to codon usage and thus amino-acid usage, creating routes for selection via proteome cost and nutrient stoichiometry. In a 2023 prokaryote-wide analysis, GC-rich codons were reported to encode cheaper amino acids more often, and the authors observed an extremely strong negative association between **average amino-acid metabolic cost** and GC across tens of thousands of prokaryotes. (aliperti2023rkselectionof pages 3-6)

In soil systems, a 2023 metagenomic study proposes **resource-driven selection on nucleotide composition**: because **AT base pairs have higher C:N (10:7 ≈ 1.42) than GC (9:8 ≈ 1.13)**, carbon limitation could favor higher GC content and select against carbon-richer AT composition. (chuckran2023edaphiccontrolson pages 1-6)

**(C) Environmental correlations (temperature, pH, soil C:N).** A phylogenetic comparative analysis of hundreds to thousands of prokaryotes found a positive association between **optimal growth temperature (Topt)** and multiple GC measures, including bacterial whole-genome GC; however, effects differed by domain (bacteria vs archaea) and by GC measure (e.g., structural RNAs vs silent sites). The authors discuss thermal stability as one possible explanation and propose (speculatively) that increased DNA repair efficiency under heat mutagenesis could have GC-increasing byproducts. (hu2022apositivecorrelation pages 1-2, hu2022apositivecorrelation pages 13-15)

### 3) Recent developments and latest research emphasis (2023–2024 priority)

**2023 (microbes; most directly curation-relevant in current evidence set):**
- **DRR-centered evolutionary model for bacterial GC**: a 2023 Microbiology Spectrum paper emphasizes DRR pathway composition as a strong predictor of genomic GC, including gene-level associations (e.g., DnaE2 positive; MutS2 negative). (teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 2-5)
- **Ecological/strategy framing**: a 2023 Environmental Microbiology paper integrates GC content into an r/K-selection perspective with extensive trait correlations, including strong links between GC and proteome amino-acid cost. (aliperti2023rkselectionof pages 1-3, aliperti2023rkselectionof pages 3-6)
- **Soil metagenome evidence linking edaphic factors to GC**: a 2023 bioRxiv preprint (398 soil metagenomes) reports that soil pH and extractable C:N predict community-average GC and ties these patterns to codon and amino-acid compositional shifts; it also provides model performance metrics for random forest predictions (R2 ~0.66 in one model). (chuckran2023edaphiccontrolson pages 1-6, chuckran2023edaphiccontrolson pages 16-23)
- **Peer-reviewed soil pH gradient**: a 2023 Nature Communications study reports GC% increasing with soil pH (R2 = 0.146; P = 0.012). (wang2023bacterialgenomesize pages 2-3)

**2024 (note on coverage limitation).** In the tool-retrieved corpus for this run, 2024 papers were largely not directly focused on *microbial genomic GC content drivers* (many were broader codon-usage or non-microbial GC topics). Consequently, this report’s mechanistic claims prioritize **2023 microbial-focused sources** plus a widely cited 2022 prokaryote temperature analysis. (hu2022apositivecorrelation pages 1-2, hu2022apositivecorrelation pages 13-15, teng2023genomiclegaciesof pages 1-2, chuckran2023edaphiccontrolson pages 1-6, wang2023bacterialgenomesize pages 2-3)

### 4) Current applications and real-world implementations

**A. Microbial ecology and trait-based metagenomics.** GC content is used as a community-weighted genomic trait in metagenomic surveys to relate microbial community structure to soil edaphic gradients (pH, nutrient ratios) and to infer ecological strategies. The soil studies above explicitly compute community-average GC and use machine learning to identify environmental predictors. (chuckran2023edaphiccontrolson pages 1-6, chuckran2023edaphiccontrolson pages 16-23, wang2023bacterialgenomesize pages 2-3)

**B. Comparative genomics and evolutionary inference.** GC content, and its decomposition into coding/noncoding and amino-acid vs codon components, is used to assess evolutionary constraints and to evaluate mechanistic hypotheses (DRR-driven mutational spectra; indirect selection). (teng2023genomiclegaciesof pages 12-13, teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 2-5)

**C. Genome annotation and quality-control contexts (implementation detail).** Some ecological and comparative studies estimate GC% from assemblies/contigs using common genomics software (e.g., Quast in soil metagenome workflows), underscoring that GC can be assay- and pipeline-dependent at the community level. (wang2023bacterialgenomesize pages 2-3)

### 5) Candidate causal-graph nodes (grouped) with suggested grounding

**Trait node**
- *GC content* — METPO:1000127 (given)

**Molecular processes (GO; candidate nodes)**
- DNA replication — GO:0006260 (teng2023genomiclegaciesof pages 1-2)
- DNA repair (general) — GO:0006281 (teng2023genomiclegaciesof pages 1-2)
- Base-excision repair (BER) — GO:0006284 (teng2023genomiclegaciesof pages 1-2)
- Nucleotide-excision repair (NER) — GO:0006289 (teng2023genomiclegaciesof pages 1-2)
- Mismatch repair (MMR) — GO:0006298 (teng2023genomiclegaciesof pages 1-2)
- Translesion DNA synthesis (TLS) — GO:0019985 (teng2023genomiclegaciesof pages 10-12)
- Oxidative stress (response to) — GO:0006979 (teng2023genomiclegaciesof pages 10-12)

**Genes/proteins (grounding often via UniProt/KEGG; label-only here due to source granularity)**
- dnaE2 (error-prone polymerase) — label-only (candidate UniProt/KEGG) (teng2023genomiclegaciesof pages 2-5)
- mutS2 (MMR-related homolog) — label-only (candidate UniProt/KEGG) (teng2023genomiclegaciesof pages 2-5)
- dinB / Pol V (TLS polymerases referenced in text) — label-only (teng2023genomiclegaciesof pages 10-12)

**Chemicals / lesions (CHEBI; candidate nodes)**
- 8-oxoG / 8-oxo-2′-deoxyguanosine — CHEBI candidate (label-only if uncertain) (teng2023genomiclegaciesof pages 10-12)

**Environmental/edaphic factors (ENVO; candidate nodes)**
- Soil environment — ENVO:00001998 (context for pH/C:N) (chuckran2023edaphiccontrolson pages 1-6)
- Soil pH — label-only (environmental variable) (chuckran2023edaphiccontrolson pages 6-10, wang2023bacterialgenomesize pages 2-3)
- Soil extractable C:N (Cextr:Nextr) — label-only (chuckran2023edaphiccontrolson pages 1-6)
- High temperature / optimal growth temperature (Topt) — label-only ENVO candidate (hu2022apositivecorrelation pages 1-2, hu2022apositivecorrelation pages 13-15)
- Carbon limitation — label-only (resource constraint) (chuckran2023edaphiccontrolson pages 1-6)

**Higher-level ecological strategy nodes (label-only)**
- r/K strategy / resource opportunism — label-only (aliperti2023rkselectionof pages 6-9, aliperti2023rkselectionof pages 3-6)
- Proteome amino-acid metabolic cost — label-only (aliperti2023rkselectionof pages 3-6)

### 6) Candidate causal edges (evidence-backed)

The table below lists candidate edges (including some measurement/confounder edges) that are suitable starting points for a TraitMech curation graph, with confidence notes.

| Edge (subject–predicate–object) | Node type(s) | Suggested ontology grounding | Evidence snippet | Reference (DOI, year, URL) | Curation notes |
|---|---|---|---|---|---|
| Cytosine deamination — decreases — genomic GC content | process → trait | GO:0006307 DNA deamination? / label only; METPO:1000127 | “cytosine deamination reduces the GC content” (teng2023genomiclegaciesof pages 10-12) | 10.1128/spectrum.02145-22, 2023, https://doi.org/10.1128/spectrum.02145-22 | Strong mechanistic statement from bacterial comparative study; curate as general mutation-bias edge. Grounding for exact lesion process may remain label-only if GO specificity is uncertain. |
| Guanine oxidation (8-oxoG formation/mispairing) — alters mutational spectrum toward AT — genomic GC content | process/chemical → trait | GO:0006979 response to oxidative stress; CHEBI:44605 8-oxo-2'-deoxyguanosine or label only; METPO:1000127 | “guanine oxidation (8OG) causes A mis-pairing” (teng2023genomiclegaciesof pages 8-10, teng2023genomiclegaciesof pages 10-12) | 10.1128/spectrum.02145-22, 2023, https://doi.org/10.1128/spectrum.02145-22 | Mechanistically plausible and source-backed, but direction to long-term genome-wide GC is inferred through mutation bias; mark moderate confidence. |
| DNA replication and repair (DRR) system change — drives — genomic GC content evolution | process → trait | GO:0006281 DNA repair; GO:0006260 DNA replication; METPO:1000127 | “ancient adaptations transformed the DRR system, producing mutational biases that shaped GC-content evolution” (teng2023genomiclegaciesof pages 1-2) | 10.1128/spectrum.02145-22, 2023, https://doi.org/10.1128/spectrum.02145-22 | Core graph edge; broad but directly stated. Best as high-level parent edge for downstream pathway/gene edges. |
| Base excision repair / nucleotide excision repair / mismatch repair / homologous recombination — modulate — genomic GC content | pathway set → trait | GO:0006284 BER; GO:0006289 NER; GO:0006298 MMR; GO:0035825 HR? / label only; KEGG pathway labels | “multiple DRR pathways (BER, NER, NHEJ, MMR, HR)… can alter mutational spectra” (teng2023genomiclegaciesof pages 1-2) | 10.1128/spectrum.02145-22, 2023, https://doi.org/10.1128/spectrum.02145-22 | Good pathway-level candidate nodes, but individual edge polarity is not always uniform; curate with uncertainty or as generic modulatory edges. |
| Error-prone translesion synthesis (TLS) — increases — genomic GC content | process → trait | GO:0019985 translesion synthesis; METPO:1000127 | “error-prone polymerases (TLS/HR) can increase genomic GC” (teng2023genomiclegaciesof pages 8-10); “Error-prone polymerases… are causally linked to increases in genomic GC” (teng2023genomiclegaciesof pages 10-12) | 10.1128/spectrum.02145-22, 2023, https://doi.org/10.1128/spectrum.02145-22 | Stronger than many pathway edges because direction is explicit. Still comparative/inferential, not direct perturbation. |
| DnaE2 presence — positively associated with — high genomic GC content | gene/protein → trait | KEGG ortholog / UniProt label only: dnaE2 | “DnaE2 (error-prone TLS polymerase) positively… correlated with genomic GC” (teng2023genomiclegaciesof pages 2-5) | 10.1128/spectrum.02145-22, 2023, https://doi.org/10.1128/spectrum.02145-22 | Association robust in large comparative dataset; useful gene node, but causal direction remains inferred from pathway role. |
| MutS2 presence — negatively associated with — genomic GC content | gene/protein → trait | KEGG ortholog / UniProt label only: mutS2 | “MutS2 (MMR homologue) negatively correlated with genomic GC” (teng2023genomiclegaciesof pages 2-5) | 10.1128/spectrum.02145-22, 2023, https://doi.org/10.1128/spectrum.02145-22 | Association-based and may be lineage-specific; curate as uncertain or comparative-only edge. |
| Environmental stress — induces/upregulates — error-prone polymerases (Pol V/DinB/DnaE2) | environment/process → gene/process | GO:0006950 response to stress; UniProt/label only for Pol V, DinB, DnaE2 | “Error-prone polymerases… can be upregulated under environmental stress” (teng2023genomiclegaciesof pages 10-12) | 10.1128/spectrum.02145-22, 2023, https://doi.org/10.1128/spectrum.02145-22 | Useful mechanistic bridge from environment to mutation spectrum. Stress type not always resolved; keep broad. |
| Heat mutagenesis / high growth temperature — positively associated with — genomic GC content | environment → trait | ENVO:01000243 high temperature environment? / label only; METPO:1000127 | “positive correlations between Topt and GC content… in bacterial whole genome sequences” (hu2022apositivecorrelation pages 1-2); “Prokaryotes growing in high temperatures have higher GC contents” (hu2022apositivecorrelation pages 1-2) | 10.1186/s12864-022-08353-7, 2022, https://doi.org/10.1186/s12864-022-08353-7 | Strong phylogenetic comparative evidence, especially in bacteria. Not uniformly supported across all archaea; annotate domain-specific uncertainty. |
| Elevated DNA repair efficiency in response to heat mutagenesis — may increase — genomic GC content | process → trait | GO:0006281 DNA repair; METPO:1000127 | “elevated efficiency of DNA repair in response to heat mutagenesis might have the by-product of increasing GC content” (hu2022apositivecorrelation pages 1-2) | 10.1186/s12864-022-08353-7, 2022, https://doi.org/10.1186/s12864-022-08353-7 | Explicitly speculative (“might”); retain as warning/uncertain edge, not yet high-confidence TraitMech curation. |
| Soil pH — positively associated with — community-average bacterial GC content | environment → trait | ENVO:00001998 soil; CHEBI: not applicable; label only: soil pH | “soil pH was the strongest predictor… low-pH soils tended to host communities with lower GC content” (chuckran2023edaphiccontrolson pages 6-10); “GC% increases with soil pH, R2 = 0.146, P = 0.012” (wang2023bacterialgenomesize pages 2-3) | 10.1101/2021.11.17.469016, 2023, https://doi.org/10.1101/2021.11.17.469016; 10.1038/s41467-023-43297-w, 2023, https://doi.org/10.1038/s41467-023-43297-w | Good environmental edge for soil communities; community-average metagenomic trait, not single-isolate phenotype. Preprint plus peer-reviewed support. |
| Low soil pH — associated with — larger genomes and lower GC content | environment → trait pair | ENVO:00001998 soil; METPO:1000127; label only for genome size trait | “low-pH soils… larger genomes and lower GC content” (chuckran2023edaphiccontrolson pages 1-6, chuckran2023edaphiccontrolson pages 6-10) | 10.1101/2021.11.17.469016, 2023, https://doi.org/10.1101/2021.11.17.469016 | Useful contextual edge if graph includes genome size; strongest in metagenomic community averages. |
| Soil extractable C:N — negatively associated with — community-average bacterial GC content | environment/resource ratio → trait | label only: soil extractable C:N; ENVO:00001998 soil; METPO:1000127 | “GC content was negatively correlated with soil Cextr:Nextr (p < 0.001)” (chuckran2023edaphiccontrolson pages 1-6) | 10.1101/2021.11.17.469016, 2023, https://doi.org/10.1101/2021.11.17.469016 | Strong statistical association in 398 soil metagenomes; mechanistic direction interpreted via resource stoichiometry. Community-level only. |
| Carbon limitation — selects for — higher genomic GC content | environment/process → trait | GO/ENVO label only: carbon limitation; METPO:1000127 | “carbon limitation may select for GC-rich genomes and against carbon-rich ATs” (chuckran2023edaphiccontrolson pages 1-6) | 10.1101/2021.11.17.469016, 2023, https://doi.org/10.1101/2021.11.17.469016 | Mechanistic interpretation rather than direct manipulation; useful but should be flagged as inferred from stoichiometric argument and environmental correlations. |
| AT base pairs (higher C:N cost) — are selected against under carbon limitation — relative to GC base pairs | chemical/composition → process | CHEBI label only: AT base pair; GC base pair | “AT base pairs have higher C:N (10:7 = 1.42) than GC (9:8 = 1.13)” (chuckran2023edaphiccontrolson pages 1-6) | 10.1101/2021.11.17.469016, 2023, https://doi.org/10.1101/2021.11.17.469016 | Mechanistic stoichiometric edge supporting carbon-limitation hypothesis; not a direct observational causal test. |
| Higher GC codon usage — shifts — amino-acid usage toward lower metabolic cost | process/composition → process | label only: GC-rich codons; GO:0006412 translation? | “GC-rich codons tend to encode amino acids with lower metabolic cost” and average amino-acid metabolic cost is strongly negatively correlated with GC (r = -0.88) (aliperti2023rkselectionof pages 3-6) | 10.1111/1462-2920.16511, 2023, https://doi.org/10.1111/1462-2920.16511 | Strong comparative support for resource-driven mechanism. Better represented as GC ↔ proteome-cost coupling rather than direct molecular pathway. |
| Resource opportunism / r-strategy traits — positively associated with — high genomic GC content | ecological strategy → trait | label only | “High GC content correlates with resource opportunism” and more utilizable carbon substrates (aliperti2023rkselectionof pages 6-9, aliperti2023rkselectionof pages 3-6) | 10.1111/1462-2920.16511, 2023, https://doi.org/10.1111/1462-2920.16511 | Ecological association, not direct molecular mechanism. Useful higher-level phenotype node if TraitMech includes environment/strategy layer. |
| Phylum-level phylogenetic history — explains variance in — genomic GC content | phylogenetic factor → trait | NCBITaxon:2 Bacteria; label only: phylogenetic inertia | “>60% of variance is explained at the phylum level” and “strong phylogenetic inertia” (teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 2-5) | 10.1128/spectrum.02145-22, 2023, https://doi.org/10.1128/spectrum.02145-22 | Important confounder/modifier, not a mechanistic biochemical cause. Include as cautionary node/annotation rather than causal driver edge if schema permits. |
| Coding-sequence GC content — is a proxy for — whole-genome GC content | assay/measurement → trait | label only: coding-sequence GC; label only: whole-genome GC | “coding-sequence GC closely tracks whole-genome GC (Spearman r = 0.99)” (aliperti2023rkselectionof pages 1-3) | 10.1111/1462-2920.16511, 2023, https://doi.org/10.1111/1462-2920.16511 | Measurement edge, not biological causation. Valuable for assay harmonization and integrating studies using CDS GC versus GCw. |


*Table: This table lists candidate causal and supporting measurement/confounder edges for microbial genomic GC content, grounded in the cited comparative and metagenomic literature. It is designed to help curate which edges are strong enough for TraitMech and which should remain uncertain or assay-contextual.*

### 7) Visual evidence (figures/tables)

The relationships between soil extractable C:N and bacterial GC%, and between soil pH and GC% (including random forest model importance/performance), are captured in figure extractions from Chuckran et al. (bioRxiv 2023). These images can be used as curation-supporting visual evidence for environment→GC associations at the community level. (chuckran2023edaphiccontrolson media 5ffaf4ba, chuckran2023edaphiccontrolson media ead137c2, chuckran2023edaphiccontrolson media 9f69dcb9)

### 8) Warnings / claims not yet ready for strong curation

1. **Correlation vs causation for environment→GC.** Temperature–GC associations are based on comparative correlations; authors explicitly discuss causal uncertainty and multiple mechanisms (thermal stability, DNA repair efficiency, mutational/selection processes). Curate temperature edges as *association/modifier* unless supported by direct experimental evolution or mechanistic perturbation in the target taxa. (hu2022apositivecorrelation pages 13-15)

2. **Speculative mechanistic links.** The “DNA repair efficiency under heat mutagenesis might increase GC” statement is explicitly speculative (“might”) and should be marked uncertain. (hu2022apositivecorrelation pages 1-2)

3. **Metagenome community-average traits vs isolate traits.** Soil GC% results are community-averaged and pipeline-dependent; they may not translate directly to a single-organism trait without additional modeling of community composition. Curate with an explicit “community-weighted metagenomic trait” context. (chuckran2023edaphiccontrolson pages 1-6, wang2023bacterialgenomesize pages 2-3)

4. **Phylogenetic inertia/confounding.** Strong phylum-level inertia (>60% variance explained at phylum level) means some associations may be confounded by lineage history; edges should include modifiers/controls or be restricted to within-clade analyses where possible. (teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 2-5)

5. **Missing gBGC/recombination and HGT evidence in this run.** Although gBGC and recombination are central to many GC-evolution discussions, the retrieved evidence set here did not provide direct, microbial-focused gBGC causal statements suitable for robust curation. These should be added only after obtaining direct microbial evidence (e.g., recombination rate↔GC with mechanistic interpretation in bacteria). (No curated edge here due to insufficient evidence in current context.)

---

## DOI-first bibliography (with dates and URLs)

1. **Teng W, Liao B, Chen M, Shu W.** *Genomic Legacies of Ancient Adaptation Illuminate GC-Content Evolution in Bacteria.* **Microbiology Spectrum**. **2023-02**. DOI: **10.1128/spectrum.02145-22**. URL: https://doi.org/10.1128/spectrum.02145-22 (teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 2-5)

2. **Aliperti L, Aptekmann AA, Farfañuk G, Couso LL, Soler-Bistué A, Sánchez IE.** *r/K selection of GC content in prokaryotes.* **Environmental Microbiology**. **2023-10**. DOI: **10.1111/1462-2920.16511**. URL: https://doi.org/10.1111/1462-2920.16511 (aliperti2023rkselectionof pages 1-3, aliperti2023rkselectionof pages 6-9, aliperti2023rkselectionof pages 3-6)

3. **Wang C, Yu Q-Y, Ji N-N, et al.** *Bacterial genome size and gene functional diversity negatively correlate with taxonomic diversity along a pH gradient.* **Nature Communications**. **2023-11**. DOI: **10.1038/s41467-023-43297-w**. URL: https://doi.org/10.1038/s41467-023-43297-w (wang2023bacterialgenomesize pages 2-3)

4. **Chuckran PF, Flagg C, Propster J, et al.** *Edaphic controls on genome size and GC content of bacteria in soil microbial communities.* **bioRxiv**. **2023-11** (preprint posted; DOI persists from 2021 submission). DOI: **10.1101/2021.11.17.469016**. URL: https://doi.org/10.1101/2021.11.17.469016 (chuckran2023edaphiccontrolson pages 1-6, chuckran2023edaphiccontrolson pages 16-23)

5. **Hu E-Z, Lan X-R, Liu Z-L, Gao J, Niu D-K.** *A positive correlation between GC content and growth temperature in prokaryotes.* **BMC Genomics**. **2022-02**. DOI: **10.1186/s12864-022-08353-7**. URL: https://doi.org/10.1186/s12864-022-08353-7 (hu2022apositivecorrelation pages 1-2, hu2022apositivecorrelation pages 13-15)


References

1. (aliperti2023rkselectionof pages 1-3): Lucio Aliperti, Ariel A. Aptekmann, Gonzalo Farfañuk, Luciana L. Couso, Alfonso Soler‐Bistué, and Ignacio E. Sánchez. <scp>r/k</scp> selection of <scp>gc</scp> content in prokaryotes. Environmental Microbiology, 25:3255-3268, Oct 2023. URL: https://doi.org/10.1111/1462-2920.16511, doi:10.1111/1462-2920.16511. This article has 22 citations and is from a domain leading peer-reviewed journal.

2. (teng2023genomiclegaciesof pages 1-2): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

3. (teng2023genomiclegaciesof pages 2-5): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

4. (aliperti2023rkselectionof pages 3-6): Lucio Aliperti, Ariel A. Aptekmann, Gonzalo Farfañuk, Luciana L. Couso, Alfonso Soler‐Bistué, and Ignacio E. Sánchez. <scp>r/k</scp> selection of <scp>gc</scp> content in prokaryotes. Environmental Microbiology, 25:3255-3268, Oct 2023. URL: https://doi.org/10.1111/1462-2920.16511, doi:10.1111/1462-2920.16511. This article has 22 citations and is from a domain leading peer-reviewed journal.

5. (hu2022apositivecorrelation pages 1-2): En-Ze Hu, Xin-Ran Lan, Zhi-Ling Liu, Jie Gao, and Deng-Ke Niu. A positive correlation between gc content and growth temperature in prokaryotes. BMC Genomics, Feb 2022. URL: https://doi.org/10.1186/s12864-022-08353-7, doi:10.1186/s12864-022-08353-7. This article has 165 citations and is from a peer-reviewed journal.

6. (hu2022apositivecorrelation pages 13-15): En-Ze Hu, Xin-Ran Lan, Zhi-Ling Liu, Jie Gao, and Deng-Ke Niu. A positive correlation between gc content and growth temperature in prokaryotes. BMC Genomics, Feb 2022. URL: https://doi.org/10.1186/s12864-022-08353-7, doi:10.1186/s12864-022-08353-7. This article has 165 citations and is from a peer-reviewed journal.

7. (teng2023genomiclegaciesof pages 12-13): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

8. (teng2023genomiclegaciesof pages 10-12): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

9. (teng2023genomiclegaciesof pages 8-10): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

10. (chuckran2023edaphiccontrolson pages 1-6): Peter F. Chuckran, Cody Flagg, Jeffrey Propster, William A. Rutherford, Ella Sieradzki, Steven J. Blazewicz, Bruce Hungate, Jennifer Pett-Ridge, Egbert Schwartz, and Paul Dijkstra. Edaphic controls on genome size and gc content of bacteria in soil microbial communities. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2021.11.17.469016, doi:10.1101/2021.11.17.469016. This article has 62 citations.

11. (chuckran2023edaphiccontrolson pages 16-23): Peter F. Chuckran, Cody Flagg, Jeffrey Propster, William A. Rutherford, Ella Sieradzki, Steven J. Blazewicz, Bruce Hungate, Jennifer Pett-Ridge, Egbert Schwartz, and Paul Dijkstra. Edaphic controls on genome size and gc content of bacteria in soil microbial communities. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2021.11.17.469016, doi:10.1101/2021.11.17.469016. This article has 62 citations.

12. (wang2023bacterialgenomesize pages 2-3): Cong Wang, Qing-Yi Yu, Niu-Niu Ji, Yong Zheng, John W. Taylor, Liang-Dong Guo, and Cheng Gao. Bacterial genome size and gene functional diversity negatively correlate with taxonomic diversity along a ph gradient. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43297-w, doi:10.1038/s41467-023-43297-w. This article has 135 citations and is from a highest quality peer-reviewed journal.

13. (chuckran2023edaphiccontrolson pages 6-10): Peter F. Chuckran, Cody Flagg, Jeffrey Propster, William A. Rutherford, Ella Sieradzki, Steven J. Blazewicz, Bruce Hungate, Jennifer Pett-Ridge, Egbert Schwartz, and Paul Dijkstra. Edaphic controls on genome size and gc content of bacteria in soil microbial communities. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2021.11.17.469016, doi:10.1101/2021.11.17.469016. This article has 62 citations.

14. (aliperti2023rkselectionof pages 6-9): Lucio Aliperti, Ariel A. Aptekmann, Gonzalo Farfañuk, Luciana L. Couso, Alfonso Soler‐Bistué, and Ignacio E. Sánchez. <scp>r/k</scp> selection of <scp>gc</scp> content in prokaryotes. Environmental Microbiology, 25:3255-3268, Oct 2023. URL: https://doi.org/10.1111/1462-2920.16511, doi:10.1111/1462-2920.16511. This article has 22 citations and is from a domain leading peer-reviewed journal.

15. (chuckran2023edaphiccontrolson media 5ffaf4ba): Peter F. Chuckran, Cody Flagg, Jeffrey Propster, William A. Rutherford, Ella Sieradzki, Steven J. Blazewicz, Bruce Hungate, Jennifer Pett-Ridge, Egbert Schwartz, and Paul Dijkstra. Edaphic controls on genome size and gc content of bacteria in soil microbial communities. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2021.11.17.469016, doi:10.1101/2021.11.17.469016. This article has 62 citations.

16. (chuckran2023edaphiccontrolson media ead137c2): Peter F. Chuckran, Cody Flagg, Jeffrey Propster, William A. Rutherford, Ella Sieradzki, Steven J. Blazewicz, Bruce Hungate, Jennifer Pett-Ridge, Egbert Schwartz, and Paul Dijkstra. Edaphic controls on genome size and gc content of bacteria in soil microbial communities. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2021.11.17.469016, doi:10.1101/2021.11.17.469016. This article has 62 citations.

17. (chuckran2023edaphiccontrolson media 9f69dcb9): Peter F. Chuckran, Cody Flagg, Jeffrey Propster, William A. Rutherford, Ella Sieradzki, Steven J. Blazewicz, Bruce Hungate, Jennifer Pett-Ridge, Egbert Schwartz, and Paul Dijkstra. Edaphic controls on genome size and gc content of bacteria in soil microbial communities. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2021.11.17.469016, doi:10.1101/2021.11.17.469016. This article has 62 citations.