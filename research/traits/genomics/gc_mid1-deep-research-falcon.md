---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:11:08.623522'
end_time: '2026-06-18T03:33:17.899089'
duration_seconds: 1329.28
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: GC mid1
  trait_identifier: METPO:1000430
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: gc_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A GC-content phenotype with genome-wide GC composition above approximately
    66.3% (the METPO `GC_>66.3` bin; note that the upstream label 'mid1' does not
    match this high-end numeric threshold, but the synonym is preserved as the authoritative
    bin definition).
  parent_traits: METPO:1000127
  synonyms: GC_>66.3
  evidence_summary: 'DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content
    evolution review supports GC-biased gene conversion as the mechanism elevating
    GC content into the high range.)'
  causal_graph_summary: 'gc_mid1_high_gc_bin: 3 nodes, 2 edges'
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
- **Trait label:** GC mid1
- **METPO identifier:** METPO:1000430
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition above approximately 66.3% (the METPO `GC_>66.3` bin; note that the upstream label 'mid1' does not match this high-end numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_>66.3
- **Existing evidence:** DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports GC-biased gene conversion as the mechanism elevating GC content into the high range.)
- **Existing causal graph summary:** gc_mid1_high_gc_bin: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **GC mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_mid1.yaml`.

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
- **Trait label:** GC mid1
- **METPO identifier:** METPO:1000430
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition above approximately 66.3% (the METPO `GC_>66.3` bin; note that the upstream label 'mid1' does not match this high-end numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_>66.3
- **Existing evidence:** DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports GC-biased gene conversion as the mechanism elevating GC content into the high range.)
- **Existing causal graph summary:** gc_mid1_high_gc_bin: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **GC mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_mid1.yaml`.

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


## Microbial Trait Causal Graph Curation Report: GC mid1 (GC_>66.3)

**Target trait:** GC mid1 (synonym **GC_>66.3**) • **METPO:** METPO:1000430 • **Category:** GENOMICS • **Definition:** genome-wide GC composition above ~66.3%.

### 1) Scope summary (trait meaning, boundaries, measurement)

**Phenotype represented.** GC mid1 represents a **high genome-wide GC fraction** phenotype (DNA base composition), intended to capture organisms whose **whole-genome %GC exceeds ~66.3%** (METPO bin threshold). This threshold sits within the upper tail of prokaryotic base-composition diversity: in a large survey of **11,083 representative bacterial genomes**, genomic GC ranged **~16%–77%** and showed a **bimodal distribution** with most genomes either **<~45%** or **>~60%** GC (leaving relatively fewer near ~50%). (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof media a14ec8d3)

**Boundary cases / nearby traits.**
- **High-GC mode vs extreme high-GC bin:** Many “high-GC” bacteria are >60% GC, but GC_>66.3 captures a **more extreme subset** within that high-GC mode (upper part of the >60% peak). (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 1-2)
- **Gene-specific GC vs genome-wide GC:** Structural RNAs (rRNA/tRNA) can show different temperature-linked GC patterns than whole genomes; curations should avoid mixing rRNA-GC traits with genome-wide GC bins. (hu2022apositivecorrelation pages 1-2, hu2022apositivecorrelation pages 10-12)
- **Assembly/annotation effects:** Whole-genome GC is typically computed from assembled genomes; contamination/mixtures can artifactually shift GC, so curation should prefer high-quality genomes for trait assignment.

**Examples at/near the GC_>66.3 boundary.**
- **Streptomyces** (Actinobacteria; **NCBITaxon:1883**) are described as **high GC (~72%)**, well within the GC_>66.3 bin. (dagva2024correctionofnonrandom pages 1-2)
- **Mycolicibacterium smegmatis** is discussed with **observed genomic GC ~65.6%**, close to but slightly below the METPO 66.3% threshold, highlighting “near-boundary” genomes. (deng2024anadditionalproofreader pages 3-4)

### 2) Key concepts and definitions (current understanding)

#### Genomic GC content
Genome-wide %GC is the proportion of G and C nucleotides across a genome; it is a stable genomic trait at the species/clade level but can shift over macroevolutionary timescales.

#### Competing/combined explanations for high GC
The literature supports multiple non-mutually exclusive drivers:
1. **Mutation bias** (e.g., typical GC→AT bias) vs observed GC; many prokaryotes show GC higher than mutation-only expectations. (weissman2019linkinghighgc pages 1-3)
2. **Selection** (direct or indirect) favoring GC in specific contexts (e.g., DNA damage environments, repair efficiency). (weissman2019linkinghighgc pages 1-3, weissman2019linkinghighgc pages 14-15)
3. **DNA replication and repair (DRR) system differences** shaping long-run mutational spectra and base composition (a major 2023–2024 emphasis). (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8)
4. **GC-biased gene conversion (gBGC)** is often invoked historically, but in the retrieved prokaryote-focused evidence here, authors argue certain GC patterns (e.g., Ku/NHEJ association) are **not explained by biased gene conversion** and do not track homologous recombination rates. (weissman2019linkinghighgc pages 14-15, weissman2019potentiallinkbetween pages 8-11)

### 3) Recent developments & latest research (prioritizing 2023–2024)

#### 3.1 DRR-system model of bacterial GC bimodality (2023)
A major recent advance is the proposal that **bacterial genomic GC bimodality and long-term GC “states”** are strongly associated with the **composition of DNA replication and repair pathways**. In the 11,083-genome analysis, a linear model using **DRR-related KEGG orthologs** reportedly explained up to **88% of genomic GC variance** (multiple correlation coefficient ~0.94). (teng2023genomiclegaciesof pages 2-5)

The same study reports gene/pathway correlations consistent with distinct “repair/replication regimes,” including:
- **Positive GC correlates:** **DnaE2** (error-prone TLS polymerase; strongest positive correlate), and NHEJ components **Ku** and **LigD**. (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8)
- **Negative GC correlates:** **MutS2** (strongest negative correlate), and other MMR/HR proteins (**MutS, MutL, RecJ, RecU**). (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8)

This supports a causal-graph approach where **presence/absence or activity of DRR modules** acts upstream of (or co-determines) stable high/low GC phenotypes. (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8, teng2023genomiclegaciesof media 54826e7b, teng2023genomiclegaciesof media 56b8bf08)

#### 3.2 Mechanistic non-canonical mismatch repair in high-GC Streptomyces (2024)
Dagva et al. (2024) experimentally detail the Actinobacteria/archaea **NucS/EndoMS** pathway as a **non-canonical MMR** mechanism that cleaves mismatched DNA (generating DSBs in vitro) and is stimulated by the **β-clamp**. NucS is described as specifically tasked with eliminating **G/T mismatches** generated during replication. (dagva2024correctionofnonrandom pages 1-2, dagva2024correctionofnonrandom pages 10-11)

In **high-GC Streptomyces (~72% GC)**, nucS loss produced a hypermutable phenotype and a strongly transition-biased spectrum (e.g., transitions ~97.3% of base substitutions in nucS lines), with implications for base-composition dynamics. (dagva2024correctionofnonrandom pages 1-2, dagva2024correctionofnonrandom pages 9-10)

#### 3.3 Additional proofreading that counteracts AT-biased mutation in mycobacteria (2024)
Deng et al. (2024) show that mycobacterial **DnaQ** functions as an additional proofreader cooperating with the replicative polymerase proofreading domain. Deleting dnaQ increases mutation rate and yields an **AT-biased** spectrum (increased G:C→A:T changes). (deng2024anadditionalproofreader pages 1-2, deng2024anadditionalproofreader pages 2-3)

They also provide a quantitative illustration of mutation-bias vs composition in a GC-rich lineage: **expected GC ~55.8% vs observed genomic GC ~65.6%** (in M. smegmatis), consistent with proofreading/repair affecting long-run base composition. (deng2024anadditionalproofreader pages 3-4)

#### 3.4 Niche-associated mutational spectra and GC relationships (2023)
Ruis et al. (2023) connect **mutational spectra** to **replication niche**, with GC content associated with specific mutation-type proportions (e.g., higher GC negatively correlating with some C>A and C>T proportions and positively with C>G proportions). They also report niche-related differences in mutation profiles (e.g., elevated C>A and C>T in lung bacteria; more T>C in environmental bacteria), consistent with different mutagens/repair contexts. (ruis2023mutationalspectraare pages 2-3, ruis2023mutationalspectraare pages 4-5)

### 4) Current applications / real-world implementations

1. **Ecological inference and genome quality control.** GC content is used in metagenomics and comparative genomics as a coarse feature for **binning**, **contamination detection**, and ecological association studies (not itself mechanistic, but operationally important).

2. **Trait-based microbial ecology.** GC content associates with habitats that may impose specific DNA damage regimes (e.g., soils, aerobiosis/ROS, desiccation/sporulation), supporting its use in trait-based environmental models. (weissman2019linkinghighgc pages 1-3, weissman2019linkinghighgc pages 5-6)

3. **Mechanism-guided curation/prediction.** The DRR-system framework implies practical predictors: presence of **NHEJ genes (Ku/LigD)**, **TLS polymerase DnaE2**, or absence of certain **MMR/HR** components could be used as mechanistic features when annotating “high-GC state” clades. (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8, teng2023genomiclegaciesof media 56b8bf08)

### 5) Candidate causal graph nodes (grouped; include grounding where possible)

#### Trait node
- **High genomic GC content >66.3%**: METPO:1000430 (synonym GC_>66.3)

#### Pathways / modules (KEGG)
- **Base excision repair (BER):** KEGG:ko03410 (teng2023genomiclegaciesof pages 10-12)
- **Nucleotide excision repair (NER):** KEGG:ko03420 (teng2023genomiclegaciesof pages 10-12)
- **Mismatch repair (MMR):** KEGG:ko03430 (teng2023genomiclegaciesof pages 10-12)
- **Homologous recombination (HR):** KEGG:ko03440 (teng2023genomiclegaciesof pages 10-12)
- **Non-homologous end joining (NHEJ):** KEGG:ko03450 (teng2023genomiclegaciesof pages 10-12)
- **Translesion synthesis / error-prone polymerases (TLS):** (label-only; discussed within DRR set) (teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 5-8)

#### Genes/proteins (label-only nodes; grounding depends on taxon/protein family)
- **Ku** (NHEJ factor; canonical marker of NHEJ presence) (weissman2019linkinghighgc pages 3-5, weissman2019linkinghighgc pages 5-6)
- **LigD** (bacterial NHEJ ligase) (teng2023genomiclegaciesof pages 5-8)
- **DnaE2** (error-prone polymerase; TLS) (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8)
- **MutS2** (MutS family homolog; negative correlate of GC) (teng2023genomiclegaciesof pages 2-5)
- **MutS, MutL** (MMR proteins; negative correlates in the DRR association analysis) (teng2023genomiclegaciesof pages 5-8)
- **RecJ, RecU** (recombination/repair proteins; negative correlates) (teng2023genomiclegaciesof pages 5-8)
- **NucS/EndoMS** (non-canonical MMR endonuclease) (dagva2024correctionofnonrandom pages 1-2, wozniak2022bacterialdnaexcision pages 10-11)
- **β-clamp / DnaN** (sliding clamp; stimulates EndoMS/NucS, binds DnaQ) (dagva2024correctionofnonrandom pages 10-11, wozniak2022bacterialdnaexcision pages 10-11)
- **DnaQ** (additional proofreader in mycobacteria; reduces AT-biased mutations) (deng2024anadditionalproofreader pages 1-2, deng2024anadditionalproofreader pages 2-3)

#### Environmental / experimental factors (ENVO label-only candidates)
- **Soil habitat** (linked to DSB-inducing conditions like desiccation/spores) (weissman2019linkinghighgc pages 1-3)
- **Aerobic environment / ROS exposure** (DSB induction context) (weissman2019linkinghighgc pages 1-3)
- **UV exposure** (historical factor linked to GC patterns) (weissman2019linkinghighgc pages 1-3, hu2022apositivecorrelation pages 1-2)
- **Growth temperature / thermophily** (weak positive association with genome GC) (hu2022apositivecorrelation pages 12-13, hu2022apositivecorrelation pages 13-15)

#### Taxa
- **Streptomyces**: NCBITaxon:1883 (high-GC example; NucS study system) (dagva2024correctionofnonrandom pages 1-2)

### 6) Candidate causal edges (evidence-backed triples)

The table below is designed for direct translation into `gc_mid1.yaml` with uncertainty annotations and can be split into a smaller “core” set of high-confidence edges.

| Candidate causal edges for GC_>66.3 (GC mid1) | Predicate | Object node (with CURIE if available) | Evidence snippet (verbatim/near-verbatim) | Reference (DOI + URL + year) | Notes/uncertainty |
|---|---|---|---|---|---|
| Ku / bacterial NHEJ pathway (Ku, LigD; label-only candidate, KEGG ko03450 for NHEJ pathway) | positively_correlated_with | high genomic GC content >66.3% (METPO:1000430) | “We find a strong association between Ku presence and elevated GC content...” and genomes with Ku have a “dramatically shifted GC content”; Pearson correlation between GC content and Ku “r = 0.54 (p < 2.2×10−16)” (weissman2019linkinghighgc pages 3-5, weissman2019linkinghighgc pages 5-6) | 10.1371/journal.pgen.1008493 https://doi.org/10.1371/journal.pgen.1008493 2019 | Strong comparative association, but not direct causation. Good candidate edge if predicate is marked correlational. |
| high double-strand break rate / DNA damage (label-only candidate; GO:0006302 DNA double-strand break repair as related process) | selects_for | high genomic GC content >66.3% (METPO:1000430) | “Perhaps, then, the unifying driver of GC content is the rate of DSB formation...” and sites experiencing higher DSB rates are “under selection for increased GC content relative to the genomic background” (weissman2019linkinghighgc pages 3-5, weissman2019linkinghighgc pages 1-3) | 10.1371/journal.pgen.1008493 https://doi.org/10.1371/journal.pgen.1008493 2019 | Mechanistic hypothesis with supporting comparative evidence; still partly inferential. Environmental contexts linked to DSBs include soils, aerobicity, desiccation/sporulation, UV (weissman2019linkinghighgc pages 1-3). |
| high genomic GC content (METPO:1000430) | may_increase | NHEJ end-joining efficiency / microhomology stabilization (label-only candidate) | “high GC content may promote DNA repair...” and “Any factor that stabilizes the interaction (e.g., high GC via an increased number of hydrogen bonds) may thus increase the efficiency of NHEJ repair” by stabilizing short overhangs or microhomologies (weissman2019linkinghighgc pages 14-15, weissman2019potentiallinkbetween pages 8-11) | 10.1371/journal.pgen.1008493 https://doi.org/10.1371/journal.pgen.1008493 2019 | Causal mechanism proposed, not directly demonstrated in bacteria in retrieved papers; curate as uncertain. Intermediate node could be “stabilized short overhang/microhomology pairing.” |
| DNA replication and repair (DRR) system composition (BER/NER/MMR/HR/NHEJ/TLS; KEGG ko03410/ko03420/ko03430/ko03440/ko03450) | strongly_correlated_with | genomic GC content / high-GC state (METPO:1000430) | “A linear model using 217 DRR-related KEGG orthologs (KOs) explains up to 88% of variance (multiple correlation coefficient 0.94)” and “multiple pathways correlate with the genomic GC” (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 1-2) | 10.1128/spectrum.02145-22 https://doi.org/10.1128/spectrum.02145-22 2023 | Broad systems-level association; useful parent edge for pathway-level nodes. Correlational rather than directly causal. |
| DnaE2 / translesion synthesis polymerase (label-only candidate; gene/protein DnaE2) | positively_correlated_with | high genomic GC content / high-GC state (METPO:1000430) | “DnaE2... shows the highest positive correlation with GC” and positively correlated pathways include “TLS (DnaE2, ImuB)” (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8) | 10.1128/spectrum.02145-22 https://doi.org/10.1128/spectrum.02145-22 2023 | Correlational evidence only. Could be represented as DnaE2 presence/activity influencing mutational bias toward GC in some clades. |
| Ku/LigD NHEJ components (label-only candidate; Ku, LigD) | positively_correlated_with | high genomic GC content / high-GC state (METPO:1000430) | Positively correlated DRR pathways include “NHEJ (Ku, LigD)” (teng2023genomiclegaciesof pages 5-8) | 10.1128/spectrum.02145-22 https://doi.org/10.1128/spectrum.02145-22 2023 | Supports decomposing the broad NHEJ pathway node into gene components. Correlational. |
| MutS2 (label-only candidate; MutS family homolog) | negatively_correlated_with | high genomic GC content / high-GC state (METPO:1000430) | “MutS2... shows the highest negative correlation” with GC; genomes tend to selectively retain “DnaE2 or MutS2 according to genomic GC” (teng2023genomiclegaciesof pages 2-5) | 10.1128/spectrum.02145-22 https://doi.org/10.1128/spectrum.02145-22 2023 | Good negative edge candidate. Specific mechanism unclear; retain as association. |
| MutS / MutL / RecJ / RecU and related MMR-HR proteins (label-only candidates; GO/KEGG mismatch repair and homologous recombination) | negatively_correlated_with | high genomic GC content / high-GC state (METPO:1000430) | Negatively correlated groups include “MMR and HR proteins such as MutS, MutL, RecJ, RecU, and MutS2” (teng2023genomiclegaciesof pages 5-8) | 10.1128/spectrum.02145-22 https://doi.org/10.1128/spectrum.02145-22 2023 | Correlational, clade-structured signal; do not overinterpret as universal causal inhibition of high GC. |
| higher growth temperature / optimal growth temperature (ENVO label-only candidate) | weakly_positively_correlated_with | genomic GC content / high-GC state (METPO:1000430) | “positive correlations between genome GC metrics... and growth temperatures in bacteria” and the effect sizes are small; higher-temperature bacterial ranks average “~1.43% more GC” (hu2022apositivecorrelation pages 12-13) | 10.1186/s12864-022-08353-7 https://doi.org/10.1186/s12864-022-08353-7 2022 | Weak but recent large-scale comparative support. Better curated as environmental association than core mechanism. |
| NucS / EndoMS non-canonical mismatch repair (label-only candidate; EndoMS/NucS) | eliminates | G/T mismatches (CHEBI not applicable; label-only mismatch node) | “the specific task of NucS-dependent MMR is to eliminate G/T mismatches generated by the DNA polymerase during replication” (dagva2024correctionofnonrandom pages 1-2) | 10.1093/nar/gkae132 https://doi.org/10.1093/nar/gkae132 2024 | Strong mechanistic edge, especially for Actinobacteria/Streptomyces. |
| NucS / EndoMS non-canonical mismatch repair (label-only candidate; EndoMS/NucS) | prevents | transition accumulation / transition-biased mutational spectrum (label-only candidate) | Loss of NucS causes a “drastic increase in spontaneous mutation rate,” a “transition-shifted mutational spectrum,” and nucS lines accumulate “far more transitions” (dagva2024correctionofnonrandom pages 1-2, dagva2024correctionofnonrandom pages 10-11) | 10.1093/nar/gkae132 https://doi.org/10.1093/nar/gkae132 2024 | Mechanistic and experimentally supported, but taxon-specific to NucS-bearing clades. |
| NucS / EndoMS non-canonical mismatch repair (label-only candidate; EndoMS/NucS) | modulates | GC-content dynamics in high-GC Streptomyces (NCBITaxon:1883) | Streptomyces has “high genomic GC content (~72%)” and the authors “propose that the non-canonical MMR helps prevent GC accumulation in already GC-rich Streptomyces genomes” (dagva2024correctionofnonrandom pages 1-2, dagva2024correctionofnonrandom pages 10-11) | 10.1093/nar/gkae132 https://doi.org/10.1093/nar/gkae132 2024 | Important but taxon-specific and interpretive; curate with uncertainty flag. Effect direction may be to constrain further GC increase. |
| DnaQ proofreading exonuclease in mycobacteria (label-only candidate; DnaQ) | prevents | AT-biased mutations (label-only candidate) | DnaQ “preferentially prevents AT-biased substitutions and indels” and deletion of dnaQ “results in a mutational bias for AT” (deng2024anadditionalproofreader pages 1-2, deng2024anadditionalproofreader pages 2-2) | 10.1073/pnas.2322938121 https://doi.org/10.1073/pnas.2322938121 2024 | Strong mechanistic evidence in mycobacteria. |
| DnaQ proofreading exonuclease in mycobacteria (label-only candidate; DnaQ) | helps_maintain | GC-rich genomic composition / higher genomic GC (METPO:1000430) | Loss of DnaQ causes a pronounced mutation bias toward AT; the authors report an “expected GC of 55.8% versus an observed genomic GC of 65.6%” and conclude DnaQ helps maintain GC-rich composition by limiting AT-biased substitutions (deng2024anadditionalproofreader pages 3-4, deng2024anadditionalproofreader pages 2-3) | 10.1073/pnas.2322938121 https://doi.org/10.1073/pnas.2322938121 2024 | Useful causal edge, but presently supported in mycobacteria rather than broadly across prokaryotes. |
| GC-biased gene conversion (gBGC; label-only candidate) | hypothesized_to_increase | genomic GC content / high-GC state (METPO:1000430) | Retrieved prokaryote-focused evidence instead emphasizes that BGC “cannot explain this association” between Ku/NHEJ and GC, and “We saw no positive association between Ku incidence and inferred rates of homologous recombination” (weissman2019linkinghighgc pages 14-15, weissman2019potentiallinkbetween pages 8-11) | 10.1371/journal.pgen.1008493 https://doi.org/10.1371/journal.pgen.1008493 2019 | Keep as warning/hypothesis node only. Existing trait evidence cites gBGC, but retrieved prokaryote papers here do not provide direct support for curating a strong bacterial gBGC→high GC edge. |


*Table: This table lists candidate subject–predicate–object edges for the GC_>66.3 microbial trait, with supporting snippets, references, and uncertainty notes. It is designed for TraitMech-style curation and distinguishes mechanistic edges from broad correlational associations.*

### 7) Expert interpretation / analysis for curation

1. **High-confidence mechanistic anchors for GC mid1** (suitable for TraitMech edges)
   - **NHEJ marker Ku ↔ high GC association** is unusually strong and quantified (r=0.54, p<2.2×10−16), with a plausible mechanistic link via DSB repair regimes. This supports inclusion of **DSB repair/NHEJ** as a major upstream causal module. (weissman2019linkinghighgc pages 5-6, weissman2019linkinghighgc pages 3-5)
   - **DRR-system composition → GC “state”** is a modern, large-scale framework with unusually high explanatory power (reported 88% variance explained), and provides many gene candidates (DnaE2, MutS2, Ku/LigD, MutS/MutL/Rec genes) that can become graph nodes with mostly correlational edges. (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8)
   - **NucS/EndoMS and DnaQ** provide experimentally detailed, pathway-level mechanisms that explicitly modify mutational spectra and (by extension) base-composition trajectories, but they are likely **taxon-restricted** (Actinobacteria/mycobacteria). (dagva2024correctionofnonrandom pages 1-2, deng2024anadditionalproofreader pages 2-3)

2. **Where to be cautious (don’t over-curate):**
   - **gBGC as a bacterial mechanism**: while gBGC is widely cited historically, the retrieved evidence here specifically argues that biased gene conversion does not explain Ku–GC patterns and does not co-vary with inferred homologous recombination. Curate gBGC edges as **hypothesis/weak** unless you add additional bacterial-specific primary evidence beyond the current retrieval set. (weissman2019linkinghighgc pages 14-15, weissman2019potentiallinkbetween pages 8-11)
   - **Temperature → GC**: positive correlations exist at scale, but reported effect sizes are small and sensitive to sampling; best curated as an **environmental association** rather than a strong mechanistic determinant. (hu2022apositivecorrelation pages 12-13, hu2022apositivecorrelation pages 1-2)
   - **DRR gene correlations vs causation**: DRR genes may be correlated with GC because they co-evolve under shared selection pressures; unless experimental or strong comparative causal analysis is provided, represent as correlational edges or use intermediate nodes (e.g., “mutational spectrum shift”). (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8)

### 8) Statistics and data highlights (for trait documentation)

- **Bacterial genomic GC range and bimodality:** ~16%–77% GC; genomes cluster mainly **<~45%** or **>~60%** GC in a dataset of **11,083** representative genomes. (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof media a14ec8d3)
- **NHEJ–GC association:** Ku presence associated with elevated GC; reported Pearson **r=0.54** (p<2.2×10−16). (weissman2019linkinghighgc pages 5-6)
- **High-GC exemplar:** Streptomyces described as **~72% GC**. (dagva2024correctionofnonrandom pages 1-2)
- **Mutation bias vs composition example:** in M. smegmatis, **expected GC ~55.8% vs observed GC ~65.6%**. (deng2024anadditionalproofreader pages 3-4)
- **NucS-deficient mutational spectrum:** transitions ~**97.3%** of base substitutions in nucS lines (Streptomyces). (dagva2024correctionofnonrandom pages 9-10)
- **Temperature association effect size:** higher-temperature bacterial ranks average **~1.43% more GC** (small effect). (hu2022apositivecorrelation pages 12-13)

### 9) DOI-first bibliography (with URLs; publication dates where available)

1. **Teng W, Liao B, Chen M, Shu W.** *Genomic Legacies of Ancient Adaptation Illuminate GC-Content Evolution in Bacteria.* **Microbiology Spectrum** (Feb 2023). DOI: **10.1128/spectrum.02145-22**. https://doi.org/10.1128/spectrum.02145-22 (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8)
2. **Dagva O, Thibessard A, Lorenzi J-N, et al.** *Correction of non-random mutational biases along a linear bacterial chromosome by the mismatch repair endonuclease NucS.* **Nucleic Acids Research** (Mar 2024). DOI: **10.1093/nar/gkae132**. https://doi.org/10.1093/nar/gkae132 (dagva2024correctionofnonrandom pages 1-2, dagva2024correctionofnonrandom pages 10-11)
3. **Deng M-Z, Liu Q, Cui S-J, et al.** *An additional proofreader contributes to DNA replication fidelity in mycobacteria.* **PNAS** (Aug 2024). DOI: **10.1073/pnas.2322938121**. https://doi.org/10.1073/pnas.2322938121 (deng2024anadditionalproofreader pages 2-3, deng2024anadditionalproofreader pages 3-4)
4. **Ruis C, Weimann A, Tonkin-Hill G, et al.** *Mutational spectra are associated with bacterial niche.* (Nov 2023). DOI: **10.17863/cam.102279**. https://doi.org/10.17863/cam.102279 (ruis2023mutationalspectraare pages 2-3, ruis2023mutationalspectraare pages 4-5)
5. **Weissman JL, Fagan WF, Johnson PLF.** *Linking high GC content to the repair of double strand breaks in prokaryotic genomes.* **PLOS Genetics** (Nov 2019). DOI: **10.1371/journal.pgen.1008493**. https://doi.org/10.1371/journal.pgen.1008493 (weissman2019linkinghighgc pages 5-6, weissman2019linkinghighgc pages 14-15)
6. **Hu E-Z, Lan X-R, Liu Z-L, Gao J, Niu D-K.** *A positive correlation between GC content and growth temperature in prokaryotes.* **BMC Genomics** (Feb 2022). DOI: **10.1186/s12864-022-08353-7**. https://doi.org/10.1186/s12864-022-08353-7 (hu2022apositivecorrelation pages 12-13)
7. **Wozniak KJ, Simmons LA.** *Bacterial DNA excision repair pathways.* **Nature Reviews Microbiology** (Feb 2022). DOI: **10.1038/s41579-022-00694-0**. https://doi.org/10.1038/s41579-022-00694-0 (wozniak2022bacterialdnaexcision pages 10-11)

### 10) Warnings / “do not curate yet” items

- **gBGC → high GC in bacteria:** Not sufficiently supported by the retrieved prokaryote-specific evidence in this run; additionally, authors explicitly argue Ku–GC patterns are not explained by biased gene conversion and do not track inferred HR. Treat gBGC as a hypothesis node unless additional bacterial primary evidence is added. (weissman2019linkinghighgc pages 14-15, weissman2019potentiallinkbetween pages 8-11)
- **DRR gene presence → GC as a universal causal rule:** Many DRR associations are strong but remain correlational; curate with appropriate predicates (e.g., *positively_correlated_with*) or insert intermediate nodes (mutational spectrum shifts) when claiming causality. (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 5-8)
- **Temperature → GC as primary mechanism:** effect sizes are small and confounded by phylogeny and other factors; curate as weak/uncertain environmental association rather than a deterministic driver. (hu2022apositivecorrelation pages 12-13)


References

1. (teng2023genomiclegaciesof pages 2-5): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

2. (teng2023genomiclegaciesof pages 1-2): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

3. (teng2023genomiclegaciesof media a14ec8d3): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

4. (hu2022apositivecorrelation pages 1-2): En-Ze Hu, Xin-Ran Lan, Zhi-Ling Liu, Jie Gao, and Deng-Ke Niu. A positive correlation between gc content and growth temperature in prokaryotes. BMC Genomics, Feb 2022. URL: https://doi.org/10.1186/s12864-022-08353-7, doi:10.1186/s12864-022-08353-7. This article has 165 citations and is from a peer-reviewed journal.

5. (hu2022apositivecorrelation pages 10-12): En-Ze Hu, Xin-Ran Lan, Zhi-Ling Liu, Jie Gao, and Deng-Ke Niu. A positive correlation between gc content and growth temperature in prokaryotes. BMC Genomics, Feb 2022. URL: https://doi.org/10.1186/s12864-022-08353-7, doi:10.1186/s12864-022-08353-7. This article has 165 citations and is from a peer-reviewed journal.

6. (dagva2024correctionofnonrandom pages 1-2): Oyut Dagva, Annabelle Thibessard, Jean-Noël Lorenzi, Victor Labat, Emilie Piotrowski, Nicolas Rouhier, Hannu Myllykallio, Pierre Leblond, and Claire Bertrand. Correction of non-random mutational biases along a linear bacterial chromosome by the mismatch repair endonuclease nucs. Nucleic Acids Research, 52:5033-5047, Mar 2024. URL: https://doi.org/10.1093/nar/gkae132, doi:10.1093/nar/gkae132. This article has 7 citations and is from a highest quality peer-reviewed journal.

7. (deng2024anadditionalproofreader pages 3-4): Ming-Zhi Deng, Qingyun Liu, Shu-Jun Cui, Yi-Xin Wang, Guoliang Zhu, Han Fu, Mingyu Gan, Yuan-Yuan Xu, Xia Cai, Sheng Wang, Wei Sha, Guo-Ping Zhao, Sarah M. Fortune, and Liang-Dong Lyu. An additional proofreader contributes to dna replication fidelity in mycobacteria. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2322938121, doi:10.1073/pnas.2322938121. This article has 7 citations and is from a highest quality peer-reviewed journal.

8. (weissman2019linkinghighgc pages 1-3): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.

9. (weissman2019linkinghighgc pages 14-15): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.

10. (teng2023genomiclegaciesof pages 5-8): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

11. (weissman2019potentiallinkbetween pages 8-11): Jake L. Weissman, William F. Fagan, and Philip L.F. Johnson. Potential link between selection for high gc content and repair of double strand breaks in prokaryotic genomes. Unknown journal, Feb 2019. URL: https://doi.org/10.1101/544924, doi:10.1101/544924.

12. (teng2023genomiclegaciesof media 54826e7b): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

13. (teng2023genomiclegaciesof media 56b8bf08): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

14. (dagva2024correctionofnonrandom pages 10-11): Oyut Dagva, Annabelle Thibessard, Jean-Noël Lorenzi, Victor Labat, Emilie Piotrowski, Nicolas Rouhier, Hannu Myllykallio, Pierre Leblond, and Claire Bertrand. Correction of non-random mutational biases along a linear bacterial chromosome by the mismatch repair endonuclease nucs. Nucleic Acids Research, 52:5033-5047, Mar 2024. URL: https://doi.org/10.1093/nar/gkae132, doi:10.1093/nar/gkae132. This article has 7 citations and is from a highest quality peer-reviewed journal.

15. (dagva2024correctionofnonrandom pages 9-10): Oyut Dagva, Annabelle Thibessard, Jean-Noël Lorenzi, Victor Labat, Emilie Piotrowski, Nicolas Rouhier, Hannu Myllykallio, Pierre Leblond, and Claire Bertrand. Correction of non-random mutational biases along a linear bacterial chromosome by the mismatch repair endonuclease nucs. Nucleic Acids Research, 52:5033-5047, Mar 2024. URL: https://doi.org/10.1093/nar/gkae132, doi:10.1093/nar/gkae132. This article has 7 citations and is from a highest quality peer-reviewed journal.

16. (deng2024anadditionalproofreader pages 1-2): Ming-Zhi Deng, Qingyun Liu, Shu-Jun Cui, Yi-Xin Wang, Guoliang Zhu, Han Fu, Mingyu Gan, Yuan-Yuan Xu, Xia Cai, Sheng Wang, Wei Sha, Guo-Ping Zhao, Sarah M. Fortune, and Liang-Dong Lyu. An additional proofreader contributes to dna replication fidelity in mycobacteria. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2322938121, doi:10.1073/pnas.2322938121. This article has 7 citations and is from a highest quality peer-reviewed journal.

17. (deng2024anadditionalproofreader pages 2-3): Ming-Zhi Deng, Qingyun Liu, Shu-Jun Cui, Yi-Xin Wang, Guoliang Zhu, Han Fu, Mingyu Gan, Yuan-Yuan Xu, Xia Cai, Sheng Wang, Wei Sha, Guo-Ping Zhao, Sarah M. Fortune, and Liang-Dong Lyu. An additional proofreader contributes to dna replication fidelity in mycobacteria. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2322938121, doi:10.1073/pnas.2322938121. This article has 7 citations and is from a highest quality peer-reviewed journal.

18. (ruis2023mutationalspectraare pages 2-3): Christopher Ruis, Aaron Weimann, Gerry Tonkin-Hill, Arun Prasad Pandurangan, Marta Matuszewska, Gemma GR Murray, Roger C Lévesque, Tom L Blundell, R Andres Floto, and Julian Parkhill. Mutational spectra are associated with bacterial niche. JournalArticle, Nov 2023. URL: https://doi.org/10.17863/cam.102279, doi:10.17863/cam.102279. This article has 15 citations.

19. (ruis2023mutationalspectraare pages 4-5): Christopher Ruis, Aaron Weimann, Gerry Tonkin-Hill, Arun Prasad Pandurangan, Marta Matuszewska, Gemma GR Murray, Roger C Lévesque, Tom L Blundell, R Andres Floto, and Julian Parkhill. Mutational spectra are associated with bacterial niche. JournalArticle, Nov 2023. URL: https://doi.org/10.17863/cam.102279, doi:10.17863/cam.102279. This article has 15 citations.

20. (weissman2019linkinghighgc pages 5-6): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.

21. (teng2023genomiclegaciesof pages 10-12): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 47 citations and is from a domain leading peer-reviewed journal.

22. (weissman2019linkinghighgc pages 3-5): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.

23. (wozniak2022bacterialdnaexcision pages 10-11): Katherine J. Wozniak and Lyle A. Simmons. Bacterial dna excision repair pathways. Nature Reviews Microbiology, 20:465-477, Feb 2022. URL: https://doi.org/10.1038/s41579-022-00694-0, doi:10.1038/s41579-022-00694-0. This article has 105 citations and is from a highest quality peer-reviewed journal.

24. (hu2022apositivecorrelation pages 12-13): En-Ze Hu, Xin-Ran Lan, Zhi-Ling Liu, Jie Gao, and Deng-Ke Niu. A positive correlation between gc content and growth temperature in prokaryotes. BMC Genomics, Feb 2022. URL: https://doi.org/10.1186/s12864-022-08353-7, doi:10.1186/s12864-022-08353-7. This article has 165 citations and is from a peer-reviewed journal.

25. (hu2022apositivecorrelation pages 13-15): En-Ze Hu, Xin-Ran Lan, Zhi-Ling Liu, Jie Gao, and Deng-Ke Niu. A positive correlation between gc content and growth temperature in prokaryotes. BMC Genomics, Feb 2022. URL: https://doi.org/10.1186/s12864-022-08353-7, doi:10.1186/s12864-022-08353-7. This article has 165 citations and is from a peer-reviewed journal.

26. (deng2024anadditionalproofreader pages 2-2): Ming-Zhi Deng, Qingyun Liu, Shu-Jun Cui, Yi-Xin Wang, Guoliang Zhu, Han Fu, Mingyu Gan, Yuan-Yuan Xu, Xia Cai, Sheng Wang, Wei Sha, Guo-Ping Zhao, Sarah M. Fortune, and Liang-Dong Lyu. An additional proofreader contributes to dna replication fidelity in mycobacteria. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2322938121, doi:10.1073/pnas.2322938121. This article has 7 citations and is from a highest quality peer-reviewed journal.