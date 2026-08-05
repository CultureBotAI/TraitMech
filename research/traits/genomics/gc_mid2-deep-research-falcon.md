---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:50:56.962139'
end_time: '2026-08-04T04:59:45.625251'
duration_seconds: 528.66
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: GC mid2
  trait_identifier: METPO:1000431
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: gc_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A GC-content phenotype with genome-wide GC composition between approximately
    57.0% and 66.3% (the METPO `GC_57.0_66.3` bin).
  parent_traits: METPO:1000127
  synonyms: GC_57.0_66.3
  evidence_summary: 'DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content
    evolution review supports moderate GC-biased gene conversion as the mechanism
    producing mid-high GC content.)'
  causal_graph_summary: 'gc_mid2_mid_high_gc_bin: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000431
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 57.0% and 66.3% (the METPO `GC_57.0_66.3` bin).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_57.0_66.3
- **Existing evidence:** DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports moderate GC-biased gene conversion as the mechanism producing mid-high GC content.)
- **Existing causal graph summary:** gc_mid2_mid_high_gc_bin: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **GC mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_mid2.yaml`.

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
- **Trait label:** GC mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000431
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 57.0% and 66.3% (the METPO `GC_57.0_66.3` bin).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_57.0_66.3
- **Existing evidence:** DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports moderate GC-biased gene conversion as the mechanism producing mid-high GC content.)
- **Existing causal graph summary:** gc_mid2_mid_high_gc_bin: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **GC mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_mid2.yaml`.

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


# Curation-focused research report: GC mid2

## Executive assessment

**Target trait:** GC mid2  
**Trait CURIE:** `METPO:1000431`  
**Category / kind:** GENOMICS / CLASS  
**Operational definition supplied:** genome-wide GC composition of approximately **57.0–66.3%**, corresponding to `GC_57.0_66.3`.

GC mid2 is best modeled as an **assembly-level compositional phenotype**, not as a physiological activity, environmental preference, or single-gene phenotype. Genomic GC content is the fraction of called DNA bases that are guanine or cytosine, normally calculated as `(G+C)/(A+T+G+C) × 100`. It is a slowly evolving outcome of mutation spectra, DNA replication and repair, recombination-associated fixation bias, selection, drift, and genome history. Recent large-scale work emphasizes strong phylogenetic inertia: among 11,083 representative bacterial genomes, genomic GC ranged from about 16% to 77%, had a bimodal distribution, and more than 60% of variance was explained at the phylum level; Blomberg’s K was 1.47 and Pagel’s λ was 0.998. Most genomes clustered below 45% or above 60%, placing much of GC mid2 within the lower portion of the high-GC mode rather than at a universal biological threshold. (teng2023genomiclegaciesof pages 2-5)

The most defensible core graph is therefore:

> **DNA damage/replication errors → nucleotide-specific mutation spectrum → G/C-versus-A/T mutation pressure**, opposed by **homologous recombination → GC-biased gene conversion → preferential fixation of G/C alleles**, with DNA-replication/repair-system state modifying these rates. Long-term balance among these processes can produce a genome in the 57.0–66.3% bin. (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 8-10, lassalle2015gccontentevolutionin pages 4-6)

No study identified a mechanism uniquely producing the **57.0–66.3% interval**. The bin is an ontology discretization of a continuous variable. Mechanistic edges should consequently terminate in “increased/decreased genomic GC content” before a final threshold-classification edge to `METPO:1000431`.

## 1. Trait scope and boundary cases

### Included phenotype

The trait represents the **whole-genome or assembly-wide nucleotide fraction** lying between approximately 57.0% and 66.3% GC. Coding-sequence GC can be used as a proxy only when whole-genome GC is unavailable: in a 2023 compilation of 49,783 prokaryotes, coding-sequence and genomic GC were nearly identical at population scale (`Spearman r=0.99`, adjusted `p<9×10⁻²⁰⁰`). That study found a total prokaryotic range of 16–77%, with 90% between 33% and 71%. (aliperti2023rkselectionof pages 3-6, aliperti2023rkselectionof pages 1-3)

### Exclusions and neighboring properties

1. **Not GC3:** GC at synonymous third-codon positions is a related but distinct measurement and can respond more strongly to recombination, codon selection, and mutation bias. It must not be substituted for genome-wide GC. In bacterial comparative data, recombinant genes often showed a larger GC difference at GC3 than across all codon positions. (lassalle2015gccontentevolutionin pages 4-6)
2. **Not local GC enrichment:** Individual genomic islands, horizontally acquired genes, recombination tracts, restriction sites, or high-GC genes do not establish the assembly-level trait.
3. **Not merely “high GC”:** The interval includes moderately high through high-GC genomes but excludes genomes above approximately 66.3%. For example, the reported 66.61% GC of *Deinococcus radiodurans* lies just above the supplied upper boundary, whereas *Pseudomonas fluorescens* at 60.50% is within it. (long2018specificityofthe pages 1-2)
4. **Boundary uncertainty:** The METPO source should be checked to determine whether 57.0 and 66.3 are inclusive and how rounding is handled. A genome reported as 56.96%, 57.04%, 66.29%, or 66.34% can change class under one-decimal rounding.
5. **Assembly bias:** Contaminated, incomplete, plasmid-enriched, or metagenome-assembled genomes can have biased GC estimates. Curators should record assembly scope and calculate GC from comparable nucleotide classes.
6. **Organellar and viral sequences:** Unless METPO explicitly says otherwise, plasmids, phages, mitochondria, chloroplasts, and other replicons should not be pooled indiscriminately with the principal microbial chromosome.

### Recommended terminal graph representation

- `genomic GC content` — **has quantitative value** → `57.0–66.3 percent`
- `microbial genome` — **has trait** → `METPO:1000431`
- `increased genomic GC content` — **may result in threshold membership** → `METPO:1000431`

The last edge should be interpreted as classification, not biological causation.

## 2. Current mechanistic understanding

### Mutation pressure

Comparative bacterial work reports a pervasive excess of **G/C→A/T mutations**, even in high-GC genomes. Mutation pressure alone would therefore generally pull genomes toward lower equilibrium GC, requiring an opposing fixation process to explain observed compositions substantially above the mutation-only equilibrium. (lassalle2015gccontentevolutionin pages 1-4, lassalle2015gccontentevolutionin pages 4-6)

Relevant chemical routes include cytosine deamination, which converts a GC-base-pair state toward an AT state if unrepaired, and oxidation of guanine to 8-oxo-guanine, which can mispair with adenine during replication. The 2023 synthesis explicitly states that cytosine deamination “reduces the GC content” and that oxidized guanine produces A–8OG mispairing. (teng2023genomiclegaciesof pages 8-10)

Mismatch repair is a major modifier of mutation rate and spectrum rather than a universal “GC-raising enzyme.” In mutation-accumulation experiments, deleting `mutS` increased the *P. fluorescens* base-substitution rate approximately 309-fold, while deleting `mutL` increased it approximately 278-fold. Repair specificity also depends on neighboring base composition. These experiments establish that MMR strongly changes mutational input, but they do not establish that MMR always drives genomes into or out of GC mid2. (long2018specificityofthe pages 1-2)

### Recombination and GC-biased gene conversion

In bacteria, homologous recombination can produce gene conversion, a unidirectional transfer from donor to homologous recipient. GC-biased gene conversion (gBGC) denotes preferential transmission or fixation of G/C over A/T alleles during resolution of mismatches in recombination tracts. Unlike adaptive selection, gBGC can increase GC even if the G/C allele has no fitness advantage. (lassalle2015gccontentevolutionin pages 1-4, lassalle2015gccontentevolutionin pages 4-6)

Across 20 bacterial groups and one archaeal group, seven groups were too clonal for informative analysis because fewer than 2% of tested core genes showed recombination. In 11 of the remaining 14 groups, recombinant genes had significantly higher total GC and/or GC3; the effect was consistently stronger at GC3. Exceptions included *Helicobacter pylori* and the *Bacillus anthracis/cereus* group. This is substantial comparative support for bacterial gBGC, but it remains indirect and is not evidence that gBGC alone fixes a genome specifically in the GC-mid2 interval. (lassalle2015gccontentevolutionin pages 4-6)

### DNA replication and repair system architecture

The most important recent mechanistic-development paper is Teng et al. (February 2023). In 11,083 representative bacterial genomes, a phylogenetically controlled model based on 217 DNA-replication-and-repair KEGG orthologs explained up to **88% of total GC variance**, with multiple correlation coefficient 0.94. DnaE2, an error-prone translesion-synthesis polymerase, had the strongest positive association, whereas MutS2 had the strongest negative association. Positively associated proteins were enriched in base-excision repair, NHEJ, translesion synthesis, and nucleotide-excision repair; several MMR, homologous-recombination, and replication proteins were negatively associated. (teng2023genomiclegaciesof pages 5-8, teng2023genomiclegaciesof pages 2-5)

These results support a system-level model in which ancient adaptation changes the replication/repair repertoire, which changes mutation spectra and eventually genomic GC. They do **not** demonstrate that possession of every positively correlated protein directly raises GC. The study itself notes that pathway enzymes have diverse effects and that a specific molecular mechanism cannot be assigned from inventory correlations alone. (teng2023genomiclegaciesof pages 8-10)

### Genome reduction and endosymbiosis

Loss of replication and repair genes, strong drift, relaxed selection, and recurrent transmission bottlenecks can expose the common AT-biased mutation spectrum in obligate endosymbionts. Direct duplex sequencing of co-resident insect endosymbionts found that rapidly evolving *Nasuia* had a higher variant frequency and a mutation spectrum potentially even more AT-biased than its **83.1% AT** genome. The authors state that missing replication/repair genes can allow AT bias to drive AT content above 75% in many endosymbionts. This is a strong opposing mechanism to GC mid2, but it is taxon- and lifestyle-specific. GC-rich reduced-genome exceptions exist, including *Candidatus Tremblaya princeps* at 58.8% GC and *Candidatus Hodgkinia cicadicola* at 58.4% GC. (waneka2021mutationalpressuredrives pages 1-2)

## 3. Candidate nodes grouped by type

### Trait and quantitative nodes

- **GC mid2** — `METPO:1000431`
- **Parent trait** — `METPO:1000127`
- **Genomic GC content** — label-only candidate if no verified ontology term is available
- **57.0–66.3% genomic GC interval** — literal/measurement node
- **GC3 content** — label-only comparator; explicitly not equivalent to the target
- **Mutation-equilibrium GC content** — label-only latent quantitative node

### Biological processes and modules

Stable GO grounding can be used for broad process nodes:

- Homologous recombination — `GO:0035825` or the project’s preferred verified GO recombination term; validate before insertion
- DNA mismatch repair — `GO:0006298`
- Base-excision repair — `GO:0006284`
- Nucleotide-excision repair — `GO:0006289`
- DNA ligation involved in NHEJ / nonhomologous end joining — use the project’s verified GO term; do not infer a CURIE from the label alone
- Translesion synthesis — `GO:0019985`
- DNA replication — `GO:0006260`
- Cytosine deamination — label-only unless the exact reaction context is specified
- GC-biased gene conversion — label-only candidate; no stable identifier was verified here
- Genome reduction / genome streamlining — label-only candidates
- Horizontal gene transfer — label-only unless a verified project ontology term is selected

### Genes and proteins

- **DnaE2:** error-prone DNA polymerase III α-family translesion polymerase; positive genome-wide association with GC in Teng et al.
- **ImuB:** TLS-associated protein; positive association in the same analysis.
- **MutS2:** MutS-family protein; strongest negative GC association in Teng et al.
- **MutS and MutL:** canonical mismatch-repair proteins; experimental deletion strongly elevates mutation rates.
- **MutM and Nei:** DNA glycosylases involved in base-excision repair of oxidative lesions.
- **MutT/MutT1:** sanitization of oxidized nucleotide pools.
- **Ku and LigD:** principal bacterial NHEJ components.
- **RecJ and RecU:** homologous-recombination/repair proteins negatively associated with GC in the 2023 comparative analysis.
- **DnaE, PolC:** replicative polymerase-system candidates associated with lineage-level compositional differences in older comparative work.

Gene/protein identifiers should be assigned taxon by taxon. A bare symbol such as `mutS` cannot safely receive a single UniProt CURIE across all bacteria.

### Chemicals and lesions

- Cytosine — `CHEBI:16040`
- Guanine — `CHEBI:16235`
- Adenine — `CHEBI:16708`
- Thymine — `CHEBI:17821`
- 8-oxo-guanine / oxidized guanine — label-only until the exact CHEBI entity and nucleobase-versus-nucleoside context are verified
- dATP, dTTP, dGTP, dCTP — candidate nucleotide-pool nodes; verify CHEBI CURIEs before curation
- G/C allele and A/T allele — label-only population-genetic states
- DNA double-strand break — lesion/process node; verify preferred ontology grounding

### Environmental and ecological candidates

- Oxidative stress
- Heat stress
- Low temperature / psychrophilic conditions
- Nutrient limitation / oligotrophic environment
- Low oxygen / anaerobic conditions
- DNA-damaging environment
- Unstable environment
- Intracellular endosymbiotic lifestyle
- Transmission bottleneck
- Reduced effective population size

These are mostly distal or contextual nodes. None is sufficiently universal to serve as a direct cause of GC mid2 without an intervening replication/repair or evolutionary-process node.

## 4. Candidate evidence-backed edges

The following table distinguishes graph-ready mechanisms from association-only findings.

| Subject | Predicate | Object | Evidence strength | DOI | Verbatim supporting snippet | Curation note |
|---|---|---|---|---|---|---|
| G/C→A/T mutation bias | decreases | genomic GC content | Strong, broad comparative and mutation-accumulation support | https://doi.org/10.1101/011023 | “in virtually all Bacteria, independently of their genomic GC-content, there is an excess of G/C→A/T mutations” (lassalle2015gccontentevolutionin pages 4-6) | Graph-ready upstream pressure lowering GC; mechanistic direction is clear, though net genomic GC also depends on opposing processes. |
| Homologous recombination | enables | bacterial gene conversion | Strong mechanistic background; indirect for GC-mid2 bin | https://doi.org/10.1101/011023 | “In Bacteria, recombination occurs in the form of gene conversion (i.e. unidirectional transfer of genetic material from a donor sequence towards a homologous recipient sequence).” (lassalle2015gccontentevolutionin pages 4-6) | Reasonable graph edge for bacterial recombination mechanism. Not bin-specific. |
| GC-biased gene conversion | favors fixation of | G/C alleles | Strong comparative inference; bacterial evidence indirect but substantial | https://doi.org/10.1101/011023 | “an unknown process, selective or neutral, is opposing this universal mutational bias by favouring the fixation of G/C alleles” (lassalle2015gccontentevolutionin pages 4-6) | Use as qualified edge; source argues this process is gBGC in bacteria, but direct experimental bacterial proof remains limited. |
| Favored fixation of G/C alleles | increases | genomic GC content | Strong conceptual/mechanistic inference | https://doi.org/10.1101/011023 | “genomic regions undergoing high recombination rates will also acquire a high GC-content” (lassalle2015gccontentevolutionin pages 4-6) | Good downstream edge from gBGC to higher genomic GC. Applies to movement toward/matching mid-high GC bins, not uniquely to GC mid2. |
| DnaE2 (TLS polymerase) | positively associated with | genomic GC content | Moderate; large-scale association only | https://doi.org/10.1128/spectrum.02145-22 | “Among these, DnaE2, an error-prone TLS polymerase, and MutS2… have the highest positive and negative correlation, respectively” (teng2023genomiclegaciesof pages 2-5) | Association-only node/edge from Teng 2023; do not overstate as direct causal determinant. |
| MutS2 | negatively associated with | genomic GC content | Moderate; large-scale association only | https://doi.org/10.1128/spectrum.02145-22 | “Among these, DnaE2, an error-prone TLS polymerase, and MutS2… have the highest positive and negative correlation, respectively” (teng2023genomiclegaciesof pages 2-5) | Association-only; likely useful as a candidate opposing node. |
| BER/NHEJ/TLS/NER modules | positively associated with | genomic GC content | Moderate; pathway-level association only | https://doi.org/10.1128/spectrum.02145-22 | “the positively correlated proteins are mainly involved in BER… NHEJ… TLS… NER” (teng2023genomiclegaciesof pages 5-8) | Keep as module-level association edges only; not proof that each pathway raises GC in every lineage. |
| MMR/HR/DR modules | negatively associated with | genomic GC content | Moderate; pathway-level association only | https://doi.org/10.1128/spectrum.02145-22 | “some of the MMR- and HR-related proteins… are negatively correlated with genomic GC… positively correlated BER, TLS, NHEJ, and NER versus negatively correlated DR, HR, and MMR” (teng2023genomiclegaciesof pages 5-8) | Association-only and potentially counterintuitive; curate cautiously with taxonomic caveat. |
| Cytosine deamination | decreases | genomic GC content | Moderate mechanistic review/comparative support | https://doi.org/10.1128/spectrum.02145-22 | “the deamination of DNA cytosine residues, which is more frequently in the leading and coding strand, reduces the GC content” (teng2023genomiclegaciesof pages 8-10) | Graph-ready chemical mechanism; source is synthetic/comparative rather than direct experiment in one organism. |
| Guanine oxidation / 8-oxoG-associated mispairing | decreases | genomic GC content | Moderate mechanistic review/comparative support | https://doi.org/10.1128/spectrum.02145-22 | “the oxidation of DNA guanine residues results in mis-pairing of A with 8OG (oxidized guanine) during replication” (teng2023genomiclegaciesof pages 8-10) | Supports an upstream mutational-bias edge lowering GC. The exact quantitative impact varies by lineage. |
| Loss/streamlining of DNA replication-repair genes | permits / amplifies | AT-biased mutation and GC loss in endosymbionts | Strong in endosymbiont context; taxon-specific | https://doi.org/10.1093/gbe/evaa254 | “Missing DNA replication and repair genes… allow the AT mutation bias… to drive AT content to levels above 75% in many endosymbionts” (waneka2021mutationalpressuredrives pages 1-2) | Valuable cautionary opposing mechanism; taxon-specific to reduced endosymbiont genomes, not a general explanation for GC mid2. |
| DNA double-strand break exposure / NHEJ presence | associated with higher | genomic GC content | Moderate association; causal direction speculative | https://doi.org/10.1371/journal.pgen.1008493 | “We found a strong positive association between the presence of the NHEJ pathway on a genome and genomic GC content” and “at this point largely speculative” (weissman2019linkinghighgc pages 15-17) | Do not curate as a firm causal edge without uncertainty flag; best as DSB/NHEJ ↔ high GC hypothesis. |
| High genomic GC content | associated with | cheaper encoded proteomes / resource opportunism | Moderate but correlational only | https://doi.org/10.1111/1462-2920.16511 | “Figure 2B shows a strong negative correlation between average amino acid metabolic cost and GC content… (r -0.88)” and “resource opportunism in prokaryotes correlates with higher GC content” (aliperti2023rkselectionof pages 3-6) | Useful for applications/ecology notes, but not a direct mechanistic edge causing GC mid2. Keep out of core TraitMech unless modeling downstream consequences/associations. |


*Table: This table compiles graph-ready and carefully qualified edges for the microbial genomic GC mid2 trait, prioritizing mechanism-backed claims and clearly separating association-only findings. It is useful for deciding which edges are suitable for direct TraitMech curation versus which require uncertainty flags.*

### Recommended minimal core for `gc_mid2.yaml`

A conservative graph can be kept close to the existing nine-node/eight-edge size:

1. `cytosine deamination` — **increases** → `G/C→A/T mutation rate`
2. `guanine oxidation / 8-oxoG mispairing` — **increases** → `G/C→A/T mutation rate`
3. `G/C→A/T mutation bias` — **decreases** → `genomic GC content`
4. `homologous recombination` — **enables** → `gene conversion`
5. `gene conversion with GC-biased mismatch resolution` — **causes** → `preferential fixation of G/C alleles`
6. `preferential fixation of G/C alleles` — **increases** → `genomic GC content`
7. `DNA-replication/repair-system state` — **modulates** → `mutation spectrum`
8. `genomic GC content between 57.0% and 66.3%` — **classifies as** → `METPO:1000431`

Edges 1–3 and 6 are directionally strong. Edges 4–5 are strong mechanistic candidates but bacterial gBGC should retain an evidence qualifier because the broad bacterial support is comparative rather than direct experimental demonstration. (teng2023genomiclegaciesof pages 8-10, lassalle2015gccontentevolutionin pages 4-6)

## 5. Recent developments, applications, and expert interpretation

### 2023 replication/repair legacy model

Teng et al. shifted emphasis from a single universal selective force toward **ancient, phylogenetically persistent changes in DNA replication and repair**. Their large sample, 88% explained variance, and strong phylogenetic signal support DRR repertoire as a powerful predictor. Their interpretation is that ancient environmental adaptation altered repair systems, whose mutation biases then constrained later GC evolution. This is authoritative comparative evidence but not gene-by-gene experimental causality. (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 8-10)

### 2023 ecological r/K model

Aliperti et al. analyzed 49,783 prokaryotes and proposed that GC covaries with an ecological r/K axis. High GC correlated with lower average amino-acid metabolic cost (`r=-0.88`, n=49,783), smaller cell volume (`r=-0.10`, n=1,278), motility/flagella (n=3,623), bacillus rather than coccus morphology (n=3,445), resource opportunism (`r=0.12`, over 800 organisms), larger functional repertoires (`r=0.47–0.54`), and more defense genes (`r=0.28`). Doubling time did not correlate with GC (`r≈0`, n=21,873). These are useful ecological predictions and downstream annotations, not established causes of GC mid2. (aliperti2023rkselectionof pages 9-11, aliperti2023rkselectionof pages 3-6, aliperti2023rkselectionof pages 6-9)

### Real-world applications

- **Genome-quality control:** expected lineage GC and within-genome homogeneity help identify contamination, mis-binning, or horizontally acquired regions.
- **Comparative genomics:** GC, GC3, recombination, and repair repertoires help separate mutation/gBGC signatures from natural selection.
- **Synthetic biology:** host GC and codon composition inform heterologous-gene design, although codon optimization should use expression and tRNA data rather than genome GC alone.
- **Microbial ecology:** genomic GC is used as a coarse correlate of genome size, resource-use breadth, motility, stress defenses, and environmental stability, but phylogenetic correction is essential.
- **Evolutionary prediction:** mutation spectra and DNA-repair state can help estimate compositional trajectories and explain why observed GC differs from mutation-only equilibrium.

## 6. Claims that should not yet be curated as firm TraitMech causation

1. **“Moderate gBGC produces exactly 57.0–66.3% GC.”** No retrieved source establishes a bin-specific dose-response.
2. **DnaE2 → GC mid2.** DnaE2 had the strongest positive association in a large comparative study, but presence/absence is not direct causal proof. Curate as `positively_associated_with`, not `causes`. (teng2023genomiclegaciesof pages 5-8, teng2023genomiclegaciesof pages 2-5)
3. **MutS2/MMR → low GC.** The negative inventory association does not imply that canonical mismatch repair universally lowers GC. Mutation-accumulation data instead show that MMR strongly and context-dependently alters mutation rates and spectra. (long2018specificityofthe pages 1-2, teng2023genomiclegaciesof pages 5-8)
4. **NHEJ or double-strand breaks cause high GC.** Among 104,297 prokaryotic genomes, 21,389 contained Ku, and Ku/NHEJ presence had a strong phylogenetically controlled positive GC association. However, the authors explicitly called the GC-tethering mechanism “largely speculative”; high-GC *D. radiodurans* also lacks Ku. (weissman2019linkinghighgc pages 15-17)
5. **Temperature directly determines genomic GC.** Recent datasets do not support a simple universal DNA-thermostability rule. Aliperti et al. found a weak negative correlation between GC and growth temperature (`r=-0.19`, n=6,695), while older subgroup analyses reported positive effects in selected lineages. These are incompatible with a universal edge. (wu2012onthemolecular pages 2-4, aliperti2023rkselectionof pages 3-6)
6. **High GC causes r-strategy, flagella, rod shape, or resource opportunism.** These are correlations confounded by ancestry, genome size, functional repertoire, and ecology. (aliperti2023rkselectionof pages 9-11, aliperti2023rkselectionof pages 6-9)
7. **Genome reduction always causes low GC.** This is common in endosymbionts but has GC-rich exceptions around 58–59%, directly within GC mid2. (waneka2021mutationalpressuredrives pages 1-2)
8. **GC3 or coding GC is interchangeable with genome GC.** They are correlated but mechanistically and operationally distinct.
9. **Horizontal transfer causes the organism-level bin.** Atypical mobile regions can alter local GC and modestly shift small genomes, but local composition is primarily a measurement/confounding node unless genome-scale replacement is demonstrated.

## 7. Critical reference correction

The supplied “existing evidence” DOI **10.1186/1471-2148-10-374 is not a bacterial GC-content paper**. It resolves to Janssen et al., *Conservation, loss, and redeployment of Wnt ligands in protostomes*, published December 2010. It concerns Wnt gene evolution and animal segmentation and must not be retained as evidence for GC-biased gene conversion or bacterial genomic GC. The existing graph citation should be removed or replaced.

The likely relevant foundational literature includes the bacterial gBGC analysis with DOI **10.1101/011023**, but this is a bioRxiv preprint and should be labeled accordingly. Its evidence supports a recombination–GC relationship, not a mechanism calibrated specifically to the GC-mid2 bin. (lassalle2015gccontentevolutionin pages 4-6)

## 8. DOI-first bibliography

1. **Teng W, Liao B, Chen M, Shu W.** “Genomic Legacies of Ancient Adaptation Illuminate GC-Content Evolution in Bacteria.” *Microbiology Spectrum* 11(1). **Published February 2023.** DOI: [10.1128/spectrum.02145-22](https://doi.org/10.1128/spectrum.02145-22). Principal recent source for 11,083-genome phylogenetic and replication/repair analysis. (teng2023genomiclegaciesof pages 2-5)
2. **Aliperti L, et al.** “r/K selection of GC content in prokaryotes.” *Environmental Microbiology* 25:3255–3268. **Published October 2023.** DOI: [10.1111/1462-2920.16511](https://doi.org/10.1111/1462-2920.16511). Principal recent ecological-association study. (aliperti2023rkselectionof pages 1-3, aliperti2023rkselectionof pages 9-11)
3. **Lassalle F, et al.** “GC-content evolution in bacterial genomes: the biased gene conversion hypothesis expands.” bioRxiv. **Version posted November 4, 2014; indexed as 2015.** DOI: [10.1101/011023](https://doi.org/10.1101/011023). Broad comparative evidence for bacterial gBGC; preprint status must be retained. (lassalle2015gccontentevolutionin pages 4-6)
4. **Weissman JL, Fagan WF, Johnson PLF.** “Linking high GC content to the repair of double strand breaks in prokaryotic genomes.” *PLOS Genetics* 15:e1008493. **Published November 2019.** DOI: [10.1371/journal.pgen.1008493](https://doi.org/10.1371/journal.pgen.1008493). NHEJ/Ku and DSB-associated GC hypothesis, explicitly partly speculative. (weissman2019linkinghighgc pages 15-17)
5. **Long H, Miller SF, Williams E, Lynch M.** “Specificity of the DNA Mismatch Repair System (MMR) and Mutagenesis Bias in Bacteria.” *Molecular Biology and Evolution* 35:2414–2421. **Advance publication June 25, 2018.** DOI: [10.1093/molbev/msy134](https://doi.org/10.1093/molbev/msy134). Mutation-accumulation evidence for MMR effects on mutation rate and spectrum. (long2018specificityofthe pages 1-2)
6. **Waneka G, Vasquez YM, Bennett GM, Sloan DB.** “Mutational Pressure Drives Differential Genome Conservation in Two Bacterial Endosymbionts of Sap-Feeding Insects.” *Genome Biology and Evolution* 13. **Published online December 4, 2020; issue 2021.** DOI: [10.1093/gbe/evaa254](https://doi.org/10.1093/gbe/evaa254). Direct low-frequency-variant evidence for strong AT-biased mutagenesis in an endosymbiont. (waneka2021mutationalpressuredrives pages 1-2)
7. **Wu H, Zhang Z, Hu S, Yu J.** “On the molecular mechanism of GC content variation among eubacterial genomes.” *Biology Direct* 7:2. **Published January 2012.** DOI: [10.1186/1745-6150-7-2](https://doi.org/10.1186/1745-6150-7-2). Older comparative analysis of polymerase systems, replication/repair, and GC. (wu2012onthemolecular pages 2-4, wu2012onthemolecular pages 1-2)

## Curation recommendation

Retain `METPO:1000431` as a thresholded **genomic measurement phenotype**. The strongest causal backbone is mutation chemistry and mutation bias opposed by recombination-associated preferential G/C fixation. Represent DnaE2, MutS2, repair pathways, NHEJ, environmental stress, genome streamlining, and r/K traits as qualified modifier or association nodes unless organism-specific experimental evidence is added. Replace the erroneous DOI immediately, and do not encode any pathway as uniquely sufficient for the 57.0–66.3% bin.

References

1. (teng2023genomiclegaciesof pages 2-5): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 52 citations and is from a domain leading peer-reviewed journal.

2. (teng2023genomiclegaciesof pages 8-10): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 52 citations and is from a domain leading peer-reviewed journal.

3. (lassalle2015gccontentevolutionin pages 4-6): Florent Lassalle, Séverine Périan, Thomas Bataillon, Xavier Nesme, Laurent Duret, and Vincent Daubin. Gc-content evolution in bacterial genomes: the biased gene conversion hypothesis expands. ArXiv, Nov 2015. URL: https://doi.org/10.1101/011023, doi:10.1101/011023. This article has 278 citations.

4. (aliperti2023rkselectionof pages 3-6): Lucio Aliperti, Ariel A. Aptekmann, Gonzalo Farfañuk, Luciana L. Couso, Alfonso Soler‐Bistué, and Ignacio E. Sánchez. <scp>r/k</scp> selection of <scp>gc</scp> content in prokaryotes. Environmental Microbiology, 25:3255-3268, Oct 2023. URL: https://doi.org/10.1111/1462-2920.16511, doi:10.1111/1462-2920.16511. This article has 23 citations and is from a domain leading peer-reviewed journal.

5. (aliperti2023rkselectionof pages 1-3): Lucio Aliperti, Ariel A. Aptekmann, Gonzalo Farfañuk, Luciana L. Couso, Alfonso Soler‐Bistué, and Ignacio E. Sánchez. <scp>r/k</scp> selection of <scp>gc</scp> content in prokaryotes. Environmental Microbiology, 25:3255-3268, Oct 2023. URL: https://doi.org/10.1111/1462-2920.16511, doi:10.1111/1462-2920.16511. This article has 23 citations and is from a domain leading peer-reviewed journal.

6. (long2018specificityofthe pages 1-2): Hongan Long, Samuel F Miller, Emily Williams, and Michael Lynch. Specificity of the dna mismatch repair system (mmr) and mutagenesis bias in bacteria. Molecular Biology and Evolution, 35:2414–2421, Jun 2018. URL: https://doi.org/10.1093/molbev/msy134, doi:10.1093/molbev/msy134. This article has 67 citations and is from a highest quality peer-reviewed journal.

7. (lassalle2015gccontentevolutionin pages 1-4): Florent Lassalle, Séverine Périan, Thomas Bataillon, Xavier Nesme, Laurent Duret, and Vincent Daubin. Gc-content evolution in bacterial genomes: the biased gene conversion hypothesis expands. ArXiv, Nov 2015. URL: https://doi.org/10.1101/011023, doi:10.1101/011023. This article has 278 citations.

8. (teng2023genomiclegaciesof pages 5-8): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 52 citations and is from a domain leading peer-reviewed journal.

9. (waneka2021mutationalpressuredrives pages 1-2): Gus Waneka, Yumary M Vasquez, Gordon M. Bennett, and Daniel B. Sloan. Mutational pressure drives differential genome conservation in two bacterial endosymbionts of sap-feeding insects. Genome Biology and Evolution, Dec 2021. URL: https://doi.org/10.1093/gbe/evaa254, doi:10.1093/gbe/evaa254. This article has 23 citations and is from a domain leading peer-reviewed journal.

10. (weissman2019linkinghighgc pages 15-17): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 82 citations and is from a domain leading peer-reviewed journal.

11. (aliperti2023rkselectionof pages 9-11): Lucio Aliperti, Ariel A. Aptekmann, Gonzalo Farfañuk, Luciana L. Couso, Alfonso Soler‐Bistué, and Ignacio E. Sánchez. <scp>r/k</scp> selection of <scp>gc</scp> content in prokaryotes. Environmental Microbiology, 25:3255-3268, Oct 2023. URL: https://doi.org/10.1111/1462-2920.16511, doi:10.1111/1462-2920.16511. This article has 23 citations and is from a domain leading peer-reviewed journal.

12. (aliperti2023rkselectionof pages 6-9): Lucio Aliperti, Ariel A. Aptekmann, Gonzalo Farfañuk, Luciana L. Couso, Alfonso Soler‐Bistué, and Ignacio E. Sánchez. <scp>r/k</scp> selection of <scp>gc</scp> content in prokaryotes. Environmental Microbiology, 25:3255-3268, Oct 2023. URL: https://doi.org/10.1111/1462-2920.16511, doi:10.1111/1462-2920.16511. This article has 23 citations and is from a domain leading peer-reviewed journal.

13. (wu2012onthemolecular pages 2-4): Hao Wu, Zhang Zhang, Songnian Hu, and Jun Yu. On the molecular mechanism of gc content variation among eubacterial genomes. Biology Direct, 7:2-2, Jan 2012. URL: https://doi.org/10.1186/1745-6150-7-2, doi:10.1186/1745-6150-7-2. This article has 169 citations and is from a peer-reviewed journal.

14. (wu2012onthemolecular pages 1-2): Hao Wu, Zhang Zhang, Songnian Hu, and Jun Yu. On the molecular mechanism of gc content variation among eubacterial genomes. Biology Direct, 7:2-2, Jan 2012. URL: https://doi.org/10.1186/1745-6150-7-2, doi:10.1186/1745-6150-7-2. This article has 169 citations and is from a peer-reviewed journal.