---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:41:44.500127'
end_time: '2026-08-04T04:51:35.794980'
duration_seconds: 591.29
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: GC high
  trait_identifier: METPO:1000432
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: gc_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A GC-content phenotype with genome-wide GC composition at or below approximately
    42.65% (the METPO `GC_<=42.65` bin; note that the upstream label 'high' does not
    match this numeric threshold, but the synonym is preserved as the authoritative
    bin definition).
  parent_traits: METPO:1000127
  synonyms: GC_<=42.65
  evidence_summary: 'DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports
    the lower end of GC content as a distinct genomic-composition phenotype.)'
  causal_graph_summary: 'gc_high_low_gc_bin: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000432
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition at or below approximately 42.65% (the METPO `GC_<=42.65` bin; note that the upstream label 'high' does not match this numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_<=42.65
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the lower end of GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_high_low_gc_bin: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **GC high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_high.yaml`.

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
- **Trait label:** GC high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000432
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition at or below approximately 42.65% (the METPO `GC_<=42.65` bin; note that the upstream label 'high' does not match this numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_<=42.65
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the lower end of GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_high_low_gc_bin: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **GC high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_high.yaml`.

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


# Curation report: microbial genomic low-GC phenotype

## Executive summary

The trait identifier must be quoted exactly as **METPO:1000432**. Despite its upstream label, **“GC high,”** the authoritative synonym and numerical definition describe the opposite phenotype: **whole-genome GC content ≤ approximately 42.65% (`GC_<=42.65`)**. For `data/traits/genomics/gc_high.yaml`, the numeric bin should control interpretation, while the misleading label should be retained only as provenance.

This is a **genome-composition class**, not a physiological activity. The strongest causal route supported by experiments is:

> spontaneous cytosine deamination and guanine oxidation → GC-to-AT/TA substitutions; loss of the corresponding repair capacity amplifies these substitutions → long-term decline in genome-wide GC.

The broader literature supports a systems-level model in which the composition of DNA replication and repair (DRR) machinery, phylogenetic history, mutation bias, recombination-associated GC-biased gene conversion, drift, and selection jointly determine genomic GC. Direct environmental adaptation to low GC is not established as a universal mechanism.

## 1. Trait scope and current understanding

### 1.1 Operational definition

**Recommended curation definition:** “A microbial genome-composition phenotype in which G+C bases constitute no more than approximately 42.65% of the complete or representative genome sequence.”

The phenotype should be calculated as:

\[
GC\% = 100\times\frac{G+C}{A+T+G+C}
\]

preferably over a complete, high-quality whole-genome assembly. The bin is somewhat stricter than the broad “low-GC” grouping used in recent comparative work, where most low-mode genomes occur below 45%. In 11,083 representative bacterial genomes, GC ranged from about 16% to 77% and was bimodal, with most genomes below 45% or above 60%; more than 60% of variance was explained at phylum level, with Blomberg’s K=1.47 and Pagel’s λ=0.998. Thus, 42.65% is an ontology-specific discretization, not a universal biological breakpoint (teng2023genomiclegaciesof pages 2-5).

### 1.2 Boundaries and nearby traits

The trait is **not equivalent to**:

- **GC3:** GC fraction at third codon positions. GC3 is especially responsive to synonymous substitution and codon usage and can differ substantially from whole-genome GC. Recombination studies often analyze GC3 rather than genomic GC (lassalle2015gccontentevolutionin pages 11-14).
- **Coding-sequence GC, noncoding GC, or local GC windows:** these can identify islands, horizontally transferred regions, or strand effects but do not alone establish the whole-genome bin. Teng et al. explicitly separated whole-genome GC, coding GC, noncoding GC, amino-acid-contributed GC, and codon-contributed GC (teng2023genomiclegaciesof pages 2-5).
- **GC skew:** strand asymmetry such as `(G−C)/(G+C)`; this concerns replication/transcription asymmetry rather than total composition. Whole bacterial genomes can be compositionally homogeneous while retaining strand-specific biases (lind2008wholegenomemutationalbiases pages 1-1).
- **An AT-biased mutation spectrum:** mutation bias is an upstream process. A currently high-GC genome may have AT-biased new mutations because equilibrium composition changes over long evolutionary periods (teng2023genomiclegaciesof pages 8-10, lassalle2015gccontentevolutionin pages 11-14).
- **Genome reduction:** reduced genomes are frequently AT-rich, especially in endosymbionts, but genome size and GC percentage are separate traits. Neither implies the other universally.
- **Low-GC Gram-positive bacteria:** an historical taxonomic description, not a mechanistic or phylogenetically exclusive class. Low-GC clades occur in multiple bacterial groups (teng2023genomiclegaciesof pages 2-5).

### 1.3 Expert synthesis

Recent authoritative analysis favors **indirect evolution through replication/repair systems and historical contingency**, rather than a single adaptive advantage of low GC. A phylogenetically informed model based on 217 DRR-related KEGG orthologs explained 88% of observed GC variance (multiple correlation 0.94); however, this is predictive comparative evidence, not proof that each correlated gene causes the phenotype (teng2023genomiclegaciesof pages 2-5). Figure 3 of that study shows the model fit and opposing associations of DnaE2 and MutS2, as well as pathway-level correlations involving BER, MMR, replication, recombination, and translesion synthesis (teng2023genomiclegaciesof media 5c6ce460).

## 2. Candidate graph nodes

### Trait and measurement nodes

- **Low whole-genome GC content:** **METPO:1000432**
- Parent trait: **METPO:1000127**
- Whole-genome GC percentage — label-only assay/measurement node
- GC3, coding-sequence GC, noncoding-sequence GC, local GC, and GC skew — label-only boundary/measurement nodes

### Genes, proteins, and complexes

- **MutM/Fpg DNA glycosylase**, **MutY adenine glycosylase** — repair oxidized guanine-associated lesions
- **Ung** and **Mug** uracil-DNA glycosylases — remove uracil arising from cytosine deamination
- **Vsr endonuclease** — very-short-patch repair of G:T mismatches
- **MutS/MutL mismatch-repair system** — canonical MMR; direction of compositional effect is taxon dependent
- **MutS2** — MutS homologue; do not conflate automatically with canonical MutS-directed MMR
- **NucS/EndoMS** — noncanonical mismatch-repair endonuclease in certain archaea and actinobacteria; potentially relevant but presently not supported as a universal low-GC determinant
- **DnaE/Pol III α**, **PolC**, **DnaE2**, **DinB/Pol IV**, and **Pol V** — replicative or error-prone/translesion polymerases
- **RecA/RuvC and homologous-recombination machinery** — candidates connecting recombination and gene conversion

### Biological-process and pathway nodes

Conservative ontology grounding includes:

- DNA replication — **GO:0006260**
- DNA repair — **GO:0006281**
- Base-excision repair — **GO:0006284**
- DNA mismatch repair — **GO:0006298**
- Homologous recombination — use a reviewed GO term selected during implementation; do not assign a guessed CURIE
- Translesion synthesis, nucleotide-excision repair, nonhomologous end joining, cytosine deamination, oxidative DNA damage, mutation accumulation, genetic drift, genome reduction, and GC-biased gene conversion — retain as label-only nodes until identifiers are ontology-verified

### Chemical and lesion nodes

- Cytosine — **CHEBI:16040**
- Uracil — **CHEBI:17568**
- Guanine — **CHEBI:16235**
- 5-methylcytosine, 8-oxo-7,8-dihydroguanine/8-oxoG, dATP, and dTTP — label-only pending identifier validation
- Reactive oxygen species/oxidative stress — label-only environmental/process node pending exact intended scope

### Ecological and evolutionary nodes

- Oligotrophic environment, low temperature/cold adaptation, intracellular endosymbiotic lifestyle, transmission bottleneck, reduced effective population size, relaxed selection, and reduced homologous recombination — candidate contextual nodes. These should not be treated as universally sufficient causes of low GC.

## 3. Candidate causal edges

The quoted snippets below are kept short and faithful to the retrieved source text. “High” confidence denotes direct mutation-accumulation or biochemical mechanism; “medium” generally denotes comparative association or a causal interpretation requiring evolutionary extrapolation.

| Subject | Predicate | Object | Evidence and supporting snippet | Curation note |
|---|---|---|---|---|
| Cytosine deamination | produces | C→U or 5-meC→T lesions | Lind & Andersson: “deamination of C→U and 5-meC→T” and deamination-associated GC-to-AT transitions (DOI 10.1073/pnas.0804445105; published 18 Nov 2008) (lind2008wholegenomemutationalbiases pages 1-1) | **High.** Curate as a molecular lesion edge. |
| Cytosine deamination | increases | GC→AT transition mutations | In repair-deficient *Salmonella*, 7% of 943 substitutions were GC-to-AT transitions “commonly associated with…deamination-induced damages” (lind2008wholegenomemutationalbiases pages 1-1) | **High but assay-specific.** Direct whole-genome mutation accumulation over 5,000 generations. |
| Guanine oxidation to 8-oxoG | increases | GC→TA transversion mutations | Of 943 substitutions, 91% were GC-to-TA transversions associated with 8-oxoG damage (lind2008wholegenomemutationalbiases pages 1-1) | **High in the tested repair-deficient background.** |
| MutM | repairs | 8-oxoG:C lesions | “MutM is a glycosylase that excises 8-oxoG paired with C…initiating base excision repair that restores the GC base pair” (lind2008wholegenomemutationalbiases pages 1-1) | **High.** Curate enzyme→repair-process and repair-process→preserved-GC edges. |
| MutY | repairs | 8-oxoG:A-associated mispairs | Failure to remove 8-oxoG before replication permits pairing with A; MutY removes the adenine and permits repair synthesis (lind2008wholegenomemutationalbiases pages 1-1) | **High.** Mechanistically specific. |
| Loss of MutM/MutY and deamination-repair capacity | increases | AT-biased substitutions | Repair-deficient *Salmonella* accumulated 98% GC-losing substitutions; authors conclude a genome lacking relevant repair systems could “very rapidly reduce its GC content” (lind2008wholegenomemutationalbiases pages 1-1) | **High-priority graph branch.** The exact mutant genotype and taxon should be recorded. |
| AT-biased substitutions | decreases over evolutionary time | whole-genome GC percentage | The experimental spectrum overwhelmingly converted GC base pairs toward AT/TA, supporting directional compositional change (lind2008wholegenomemutationalbiases pages 1-1) | **High mechanistic plausibility; medium for timescale extrapolation.** |
| Streamlined DNA replication/repair system | promotes | AT-rich genome composition | Teng et al.: “a streamlined DRR system…leads to AT-richness” (DOI 10.1128/spectrum.02145-22; Jan–Feb 2023) (teng2023genomiclegaciesof pages 8-10) | **Medium-high.** Broad synthesis, but “streamlined DRR” is a composite node. |
| DRR-system composition | predicts | genomic GC percentage | A 217-KO model explained 88% of variance, adjusted R²=0.88, P<0.01 (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof media 5c6ce460) | **Medium.** Curate as `associated_with` or `predicts`, not a simple causal edge. |
| DnaE2 presence | positively associated with | genomic GC percentage | DnaE2 had the strongest positive KO-level association in the 11,083-genome analysis (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof media 5c6ce460) | **Uncertain causal direction.** Do not use as a cause of low GC; absence may be considered only as an inferred candidate. |
| MutS2 presence | negatively associated with | genomic GC percentage | MutS2 had the strongest negative KO-level association (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof media 5c6ce460) | **Uncertain.** MutS2 is not interchangeable with canonical MutS. |
| Homologous recombination/gBGC | favors fixation of | G/C alleles | Across 14 species, 11 had positive GC–recombination correlations, R² 0.24–0.68, mean 0.43; *S. pyogenes* binned GC3–recombination R²=0.60 (DOI 10.1101/011023; preprint posted 4 Nov 2014) (lassalle2015gccontentevolutionin pages 11-14) | **Medium/uncertain.** Correlation supports gBGC but does not prove it universally. |
| Reduced long-term recombination/gBGC | permits | AT-rich genome composition | Endosymbiotic bacteria with effectively null long-term recombination “generally have very AT-rich genomes” (lassalle2015gccontentevolutionin pages 11-14) | **Uncertain and indirect.** Endosymbiosis, drift, repair loss, and genome reduction confound this relationship. |
| Low genomic GC | alters | synonymous codon usage | Whole-genome GC and codon-contributed GC were strongly correlated; the authors argue DRR synchronously influences genomic GC and codon usage (teng2023genomiclegaciesof pages 2-5) | **Medium-high downstream consequence.** |
| Low genomic GC | alters | amino-acid composition | Genomic GC influenced amino-acid usage even in conserved ribosomal proteins (teng2023genomiclegaciesof pages 8-10) | **Medium.** Avoid asserting a universal fitness direction. |
| Cold/oligotrophic ancestral adaptation | contributes to | repair-gene loss and GC reduction | Low-GC ancestors showed parallel stress/repair-gene losses; cold-adapted species had a skewed bimodal distribution, “hinting at a possible link” (teng2023genomiclegaciesof pages 8-10) | **Weak-to-medium.** Hypothesis only; do not curate as an unqualified direct edge. |

A compact prioritization is provided below.

| Proposed edge | Evidence class | Confidence | Taxon/assay limitation | Curation recommendation |
|---|---|---|---|---|
| Cytosine deamination -> GC-to-AT transition mutation | Direct experiment + mechanistic interpretation | High | Supported by genome-wide mutation-accumulation in repair-deficient *Salmonella* and comparative synthesis; mutation-spectrum edge, not by itself a whole-genome trait edge (lind2008wholegenomemutationalbiases pages 1-1, teng2023genomiclegaciesof pages 8-10) | Curate as upstream mutational-pressure edge feeding low-GC evolution |
| Guanine oxidation / 8-oxoG lesion -> GC-to-TA transversion mutation | Direct experiment + mechanistic interpretation | High | Strongest direct support from repair-deficient *Salmonella* serial passage; lesion-to-substitution mechanism is broad, but exact quantitative effect may vary by repair background (lind2008wholegenomemutationalbiases pages 1-1, teng2023genomiclegaciesof pages 8-10) | Curate as upstream mutational-pressure edge feeding low-GC evolution |
| Loss of MutM/MutY/Ung/Mug/Vsr repair -> AT-biased substitutions -> lower genomic GC | Direct experiment | High | Directly shown under reduced-selection experimental evolution in *Salmonella typhimurium* lacking major repair systems; long-term genome-composition inference extrapolates from 5,000-generation assay (lind2008wholegenomemutationalbiases pages 1-1) | High-priority curation candidate |
| Streamlined DNA replication and repair system -> AT-rich / low-GC genome | Comparative association with mechanistic synthesis | Medium-High | Broad bacterial comparative model across 11,083 genomes; explains variance strongly but is not a single intervention experiment; pathway composition is composite rather than one gene (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 8-10, teng2023genomiclegaciesof media 5c6ce460) | Curate as higher-level systems edge, marked comparative/inferred |
| DnaE2 presence -> higher genomic GC | Comparative association | Medium | Strong phylogenetic comparative association; DnaE2 is an error-prone TLS polymerase and not demonstrated alone to raise whole-genome GC in a universal intervention study (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 8-10) | Curate with uncertainty flag |
| MutS2 presence -> lower genomic GC | Comparative association | Medium | Strong negative correlation in broad bacterial dataset; MutS2 is a MutS homologue, not equivalent to canonical MutS/MMR in all taxa; causal direction remains inferred (teng2023genomiclegaciesof pages 2-5) | Curate with uncertainty flag and careful node labeling |
| Recombination / gBGC -> increased GC content | Comparative association / hypothesis with quantitative support | Medium | Evidence is correlation-based across species and bins; authors explicitly discuss time-scale mismatch between extant recombination estimates and long-term GC evolution; strongest as explanatory hypothesis, not universal proof (lassalle2015gccontentevolutionin pages 11-14) | Curate cautiously; good for opposing/alternative branch where reduced recombination permits low GC |
| Genomic low GC -> altered codon usage and amino-acid usage | Comparative association | Medium-High | Broad comparative signal; effect reflects genome-wide coding-density consequences and may be partly constrained by codon averages rather than direct selection on GC itself (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 8-10) | Curate as downstream consequence edge, not primary cause |
| **Do not universalize:** *Bacillus subtilis* mutS deletion -> GC-biased mutation spectrum | Direct experiment, taxon-specific counterexample | High for the specific assay; Low as universal low-GC mechanism | In *B. subtilis*, mutS deletion caused a 100-fold mutation increase and a GC-biased transition spectrum (dominant A->G changes), opposite to a generic low-GC edge; explicitly strain/assay specific (akashi2013relevanceofgc pages 2-3) | Do **not** curate as a universal edge for METPO:1000432; keep only as warning/counterexample |
| Canonical MutS/MMR loss -> changed mutation spectrum -> genome GC shifts | Direct experiment in some taxa, mixed direction across taxa | Medium | *P. fluorescens* mutS/mutL knockouts greatly raise mutation rate, but directionality differs across taxa; *D. radiodurans* ΔmutS is GC-biased; therefore not a simple universal low-GC edge (long2018specificityofthe pages 2-3, long2018specificityofthe pages 5-6, akashi2013relevanceofgc pages 2-3) | Curate only at generic “MMR loss alters mutation spectrum” level unless taxon-scoped |


*Table: This table prioritizes candidate causal edges for METPO:1000432 using direct experiments first, then comparative and hypothesis-level evidence. It is useful for deciding which mechanisms are robust enough to curate now and which require taxon-specific caution or uncertainty flags.*

## 4. Critical counterexamples and warnings

1. **Canonical MMR loss does not have a universal compositional direction.** In *Bacillus subtilis* 168, deletion of `mutS` increased mutation frequency 100-fold, but the resulting spectrum was GC-biased: 86% A→G and 14% C→T among sampled rifampicin-resistant mutants. This is the opposite of a generic `mutS loss → low GC` edge and derives from a targeted `rpoB` resistance assay rather than whole-genome accumulation (akashi2013relevanceofgc pages 2-3).

2. Taxon dependence is also evident in mutation-accumulation data. *Pseudomonas fluorescens* `mutS` and `mutL` knockouts increased mutation rates 309- and 278-fold, respectively, while *Deinococcus radiodurans* Δ`mutS` showed significantly greater A/T→G/C than G/C→A/T mutation rates. MMR loss can therefore be safely curated as **altering mutation rate and spectrum**, but not as universally lowering GC (long2018specificityofthe pages 2-3).

3. **Do not convert correlations into directed causal edges.** DnaE2, MutS2, BER, MMR, and other DRR components are strong predictors in comparative models, but phylogenetic co-inheritance, ecological history, and correlated gene loss remain alternatives (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof media 5c6ce460).

4. **Do not curate “cold environment → low GC” or “oligotrophy → low GC” as settled mechanisms.** The 2023 study explicitly uses language such as “hinting at a possible link,” and its ancient-environment reconstruction is inferential (teng2023genomiclegaciesof pages 8-10).

5. **Do not equate genome reduction with low GC.** Repair loss, elevated mutation, drift, recombination loss, and deletion bias can co-occur during symbiosis, but the graph should represent them as separable processes.

6. **NucS should not yet be inserted as a low-GC determinant.** The 2024 *Streptomyces* study demonstrates that NucS corrects specific mismatches and strongly affects mutation rate/spectrum, but the retrieved evidence does not establish `NucS → METPO:1000432`. It is best retained as a candidate mechanism for future taxon-scoped curation.

7. **Assembly quality matters.** Whole-genome GC estimated from contaminated, incomplete, or compositionally biased MAGs may be misleading. A threshold edge should require an explicit quality/coverage policy and should not be inferred from one gene, amplicon, or local contig.

## 5. Applications and real-world relevance

- **Genome and metagenome characterization:** GC composition and oligonucleotide frequencies are routinely useful for comparing contigs, identifying compositional outliers, and supporting genome binning. They must be combined with coverage, taxonomy, and marker-gene quality rather than used alone.
- **Microbial taxonomy and comparative genomics:** Strong phylogenetic inertia makes genomic GC informative as a descriptive feature, but not diagnostic of species identity by itself. More than 60% of variance was attributable at phylum level in the 11,083-genome analysis (teng2023genomiclegaciesof pages 2-5).
- **Evolutionary forecasting:** Mutation spectra and repair-system inventories can indicate whether a lineage is under GC-losing or GC-gaining mutational pressure. Mutation bias is increasingly viewed as capable of shaping adaptive outcomes, but present composition may lag current mutation bias by long evolutionary intervals.
- **Synthetic biology and heterologous expression:** Host genomic GC and codon preferences inform codon optimization, but genome-wide GC should not substitute for expression-specific codon-demand, tRNA, mRNA-structure, or protein-folding analyses.
- **Endosymbiont and pathogen genomics:** Extremely AT-rich genomes can flag long-term genome degeneration, bottlenecks, reduced recombination, and repair loss, but these processes must be demonstrated independently rather than inferred solely from GC.

## 6. Recommended minimal TraitMech graph

The most defensible initial graph is:

1. `cytosine deamination` → **produces** → `uracil/5-methylcytosine-derived mismatch`
2. `guanine oxidation` → **produces** → `8-oxoG lesion`
3. `MutM/MutY/Ung/Mug/Vsr-mediated repair` → **repairs** → `GC-losing DNA lesions`
4. `loss or reduction of lesion-repair capacity` → **increases** → `GC→AT/TA substitutions`
5. `GC→AT/TA substitution bias` → **decreases over evolutionary time** → `whole-genome GC percentage`
6. `whole-genome GC percentage ≤42.65%` → **has phenotype** → **METPO:1000432**
7. **METPO:1000432** → **influences** → `codon usage composition`
8. **METPO:1000432** → **influences** → `amino-acid usage composition`

Add `DRR-system streamlining`, `reduced recombination/gBGC`, `cold adaptation`, `oligotrophy`, drift, and endosymbiosis only in explicitly uncertain or taxon-scoped branches.

## 7. DOI-first bibliography

1. **Teng W, Liao B, Chen M, Shu W.** “Genomic Legacies of Ancient Adaptation Illuminate GC-Content Evolution in Bacteria.” *Microbiology Spectrum* 11(1). Published January–February 2023. DOI: [10.1128/spectrum.02145-22](https://doi.org/10.1128/spectrum.02145-22). Large comparative analysis of 11,083 bacterial genomes (teng2023genomiclegaciesof pages 2-5, teng2023genomiclegaciesof pages 8-10).
2. **Lind PA, Andersson DI.** “Whole-genome mutational biases in bacteria.” *PNAS* 105:17878–17883. Published 18 November 2008. DOI: [10.1073/pnas.0804445105](https://doi.org/10.1073/pnas.0804445105). Direct whole-genome mutation-accumulation evidence (lind2008wholegenomemutationalbiases pages 1-1).
3. **Long H, Miller SF, Williams E, Lynch M.** “Specificity of the DNA Mismatch Repair System (MMR) and Mutagenesis Bias in Bacteria.” *Molecular Biology and Evolution* 35:2414–2421. Published 2018. DOI: [10.1093/molbev/msy134](https://doi.org/10.1093/molbev/msy134) (long2018specificityofthe pages 2-3, long2018specificityofthe pages 3-3).
4. **Akashi M, Yoshikawa H.** “Relevance of GC content to the conservation of DNA polymerase III/mismatch repair system in Gram-positive bacteria.” *Frontiers in Microbiology* 4:266. Published September 2013. DOI: [10.3389/fmicb.2013.00266](https://doi.org/10.3389/fmicb.2013.00266) (akashi2013relevanceofgc pages 2-3).
5. **Wu H, Zhang Z, Hu S, Yu J.** “On the molecular mechanism of GC content variation among eubacterial genomes.” *Biology Direct* 7:2. Published January 2012. DOI: [10.1186/1745-6150-7-2](https://doi.org/10.1186/1745-6150-7-2). Comparative polymerase/repair model across 364 genomes (wu2012onthemolecular pages 1-2).
6. **Lassalle F, et al.** “GC-content evolution in bacterial genomes: the biased gene conversion hypothesis expands.” bioRxiv preprint. Posted November 2014; indexed version 2015. DOI: [10.1101/011023](https://doi.org/10.1101/011023). Treat as preprint-level evidence (lassalle2015gccontentevolutionin pages 11-14).
7. **Dagva O, et al.** “Correction of non-random mutational biases along a linear bacterial chromosome by the mismatch repair endonuclease NucS.” *Nucleic Acids Research* 52:5033–5047. Published March 2024. DOI: [10.1093/nar/gkae132](https://doi.org/10.1093/nar/gkae132). Relevant to noncanonical MMR, but not yet a direct low-GC edge.
8. **Horton JS, Taylor TB.** “Mutation bias and adaptation in bacteria.” *Microbiology* 169. Published November 2023. DOI: [10.1099/mic.0.001404](https://doi.org/10.1099/mic.0.001404). Recent expert review of causes and evolutionary consequences of bacterial mutation bias.

## Curation conclusion

For **METPO:1000432**, curate the phenotype according to the numeric definition **GC ≤42.65%**, not the contradictory label “GC high.” The direct lesion/repair/mutation pathway is sufficiently supported for inclusion. DRR-system composition, recombination/gBGC, ecological adaptation, endosymbiosis, and drift are biologically important contextual mechanisms, but most should remain marked **comparative, taxon-specific, or uncertain** until an intervention or lineage-resolved study demonstrates a directional effect on whole-genome GC.

References

1. (teng2023genomiclegaciesof pages 2-5): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 52 citations and is from a domain leading peer-reviewed journal.

2. (lassalle2015gccontentevolutionin pages 11-14): Florent Lassalle, Séverine Périan, Thomas Bataillon, Xavier Nesme, Laurent Duret, and Vincent Daubin. Gc-content evolution in bacterial genomes: the biased gene conversion hypothesis expands. ArXiv, Nov 2015. URL: https://doi.org/10.1101/011023, doi:10.1101/011023. This article has 278 citations.

3. (lind2008wholegenomemutationalbiases pages 1-1): Peter A. Lind and Dan I. Andersson. Whole-genome mutational biases in bacteria. Proceedings of the National Academy of Sciences, 105:17878-17883, Nov 2008. URL: https://doi.org/10.1073/pnas.0804445105, doi:10.1073/pnas.0804445105. This article has 244 citations and is from a highest quality peer-reviewed journal.

4. (teng2023genomiclegaciesof pages 8-10): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 52 citations and is from a domain leading peer-reviewed journal.

5. (teng2023genomiclegaciesof media 5c6ce460): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 52 citations and is from a domain leading peer-reviewed journal.

6. (akashi2013relevanceofgc pages 2-3): Motohiro Akashi and Hirofumi Yoshikawa. Relevance of gc content to the conservation of dna polymerase iii/mismatch repair system in gram-positive bacteria. Frontiers in Microbiology, Jul 2013. URL: https://doi.org/10.3389/fmicb.2013.00266, doi:10.3389/fmicb.2013.00266. This article has 16 citations and is from a peer-reviewed journal.

7. (long2018specificityofthe pages 2-3): Hongan Long, Samuel F Miller, Emily Williams, and Michael Lynch. Specificity of the dna mismatch repair system (mmr) and mutagenesis bias in bacteria. Molecular Biology and Evolution, 35:2414–2421, Jun 2018. URL: https://doi.org/10.1093/molbev/msy134, doi:10.1093/molbev/msy134. This article has 67 citations and is from a highest quality peer-reviewed journal.

8. (long2018specificityofthe pages 5-6): Hongan Long, Samuel F Miller, Emily Williams, and Michael Lynch. Specificity of the dna mismatch repair system (mmr) and mutagenesis bias in bacteria. Molecular Biology and Evolution, 35:2414–2421, Jun 2018. URL: https://doi.org/10.1093/molbev/msy134, doi:10.1093/molbev/msy134. This article has 67 citations and is from a highest quality peer-reviewed journal.

9. (long2018specificityofthe pages 3-3): Hongan Long, Samuel F Miller, Emily Williams, and Michael Lynch. Specificity of the dna mismatch repair system (mmr) and mutagenesis bias in bacteria. Molecular Biology and Evolution, 35:2414–2421, Jun 2018. URL: https://doi.org/10.1093/molbev/msy134, doi:10.1093/molbev/msy134. This article has 67 citations and is from a highest quality peer-reviewed journal.

10. (wu2012onthemolecular pages 1-2): Hao Wu, Zhang Zhang, Songnian Hu, and Jun Yu. On the molecular mechanism of gc content variation among eubacterial genomes. Biology Direct, 7:2-2, Jan 2012. URL: https://doi.org/10.1186/1745-6150-7-2, doi:10.1186/1745-6150-7-2. This article has 169 citations and is from a peer-reviewed journal.