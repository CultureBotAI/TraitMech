---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:47:13.979994'
end_time: '2026-08-04T04:56:17.820511'
duration_seconds: 543.84
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: GC low
  trait_identifier: METPO:1000429
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: gc_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A GC-content phenotype with genome-wide GC composition between approximately
    42.65% and 57.0% (the METPO `GC_42.65_57.0` bin; note that the upstream label
    'low' does not match this mid-range numeric threshold, but the synonym is preserved
    as the authoritative bin definition).
  parent_traits: METPO:1000127
  synonyms: GC_42.65_57.0
  evidence_summary: 'DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports
    the mid-range GC content as a distinct genomic-composition phenotype.)'
  causal_graph_summary: 'gc_low_mid_low_gc_bin: 8 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000429
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 42.65% and 57.0% (the METPO `GC_42.65_57.0` bin; note that the upstream label 'low' does not match this mid-range numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_42.65_57.0
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the mid-range GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_low_mid_low_gc_bin: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **GC low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_low.yaml`.

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
- **Trait label:** GC low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000429
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 42.65% and 57.0% (the METPO `GC_42.65_57.0` bin; note that the upstream label 'low' does not match this mid-range numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_42.65_57.0
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the mid-range GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_low_mid_low_gc_bin: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **GC low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_low.yaml`.

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


# Curation report: microbial trait **GC low**

## Executive curation recommendation

The identifier must be recorded verbatim as **`METPO:1000429`**, with parent **`METPO:1000127`** and synonym **GC_42.65_57.0**. Despite the upstream label “GC low,” the supplied authoritative definition is a **mid-range whole-genome GC-content bin of approximately 42.65–57.0%**. It is therefore an assay/computational genomic-composition class, not a physiological capacity or environmental preference.

The best-supported TraitMech graph is not a direct pathway ending uniquely in this interval. Rather, it is an evolutionary chain:

**DNA damage and replication errors → DNA-repair/replication machinery → mutation spectrum → fixation through drift, selection, and recombination/gene conversion → continuous genome-wide GC content → bin assignment to `METPO:1000429`.**

Direct experimental evidence is strongest for oxidative lesions, cytosine deamination, and corresponding base-excision/very-short-patch repair systems. Evidence connecting environmental conditions, polymerase inventories, or recombination directly to this particular numeric bin is comparative and should be marked uncertain.

## 1. Trait scope and boundaries

### Operational definition

Genome-wide GC content is the fraction of genomic DNA bases that are guanine or cytosine, normally computed as `(G+C)/(A+T+G+C) × 100`. For this trait, the measured value is classified as `METPO:1000429` when it lies approximately between **42.65% and 57.0%**. Endpoint inclusion should follow the METPO implementation; it should not be inferred from the rounded prose definition.

Across bacteria, reported genome-wide GC values span approximately 13–77%. A recent analysis of **11,083 representative bacterial genomes** reported a 16–77% range and a phylogenetically constrained bimodal distribution, with peaks below 45% and above 60%. Thus, the METPO interval occupies much of the intermediate region between those modes rather than a universally “low-GC” state. More than 60% of GC variance in that study was explained at phylum level, demonstrating strong phylogenetic inertia. (teng2023genomiclegaciesof pages 1-2)

### Boundary cases to exclude

* **True low-GC/AT-rich genomes:** values below approximately 42.65% are outside this class, even though the textual label might suggest otherwise.
* **Values above 57.0%:** these are also outside the class.
* **Local GC content:** a genomic island, gene, codon position, or sliding window may lie in the interval while the whole genome does not.
* **GC3:** GC at third codon positions is strongly affected by synonymous codon usage and is not equivalent to whole-genome GC.
* **GC skew:** `(G−C)/(G+C)` measures strand asymmetry, not total GC fraction.
* **Equilibrium GC:** a value inferred from a mutation spectrum is an evolutionary expectation and need not equal observed GC.
* **Assembly artifacts:** contamination, incomplete metagenome-assembled genomes, untrimmed plasmids, and biased sequencing can shift the calculated value.
* **Within-genome heterogeneity:** horizontally acquired and accessory regions may differ from the core genome; bin assignment should use the declared whole-genome measurement protocol.

## 2. Current mechanistic understanding

Mutation is broadly biased toward AT in bacteria, but observed genomes frequently contain more GC than mutation bias alone predicts. Consequently, present understanding invokes several interacting forces: mutation generated by replication and DNA damage; repair-system specificity; selection on coding and regulatory functions; genetic drift; homologous recombination and possible GC-biased gene conversion; and lineage history. A review reports mutation-accumulation rates of approximately **0.001 mutations/genome/generation in *Escherichia coli*** and **0.008 in *Mesoplasma florum***, illustrating that both mutation rate and spectrum are lineage dependent. Mismatch-repair-deficient *E. coli* can also reverse the wild-type direction of mutation bias, indicating that repair machinery is mechanistically upstream of long-term nucleotide composition. (hershberg2015mutation—theengineof pages 6-7)

The most recent directly relevant large-scale synthesis is Teng et al. (February 2023). Its analysis of 11,083 genomes supports a model in which ancient environmental adaptation changed DNA replication and repair inventories, whose resulting mutation biases subsequently shaped GC evolution. Associated modules included base-excision repair, nucleotide-excision repair, mismatch repair, homologous recombination, nonhomologous end joining, and translesion synthesis. This is an **indirect-selection model**, not evidence that contemporary environments rapidly force genomes into a defined GC bin. (teng2023genomiclegaciesof pages 8-10, teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 10-12)

## 3. Candidate causal-graph nodes

### Trait and measurement nodes

* **Genome-wide GC-content phenotype:** `METPO:1000429`
* **Parent genomic-composition trait:** `METPO:1000127`
* **Continuous genome-wide GC percentage:** label-only candidate; retain the numerical value and calculation method as evidence metadata.
* **GC_42.65_57.0 binning process:** label-only assay/computational node.
* **AT-biased mutation spectrum**, **GC-biased mutation spectrum**, **GC→TA transversion**, and **GC→AT transition:** label-only molecular-event nodes.

### Genes, proteins, and complexes

Taxon-independent gene symbols should remain label-only until a species-specific locus or protein accession is selected.

* **mutM** — formamidopyrimidine-DNA glycosylase; removes 8-oxoG paired with C.
* **mutY** — adenine DNA glycosylase; removes A opposite 8-oxoG.
* **mutT** — oxidized-purine nucleotide sanitizer; hydrolyses 8-oxo-dGTP and can affect mutation direction.
* **ung** — uracil-DNA glycosylase.
* **mug** — mismatch-specific uracil-DNA glycosylase.
* **vsr** — very-short-patch repair endonuclease.
* **dnaE2** — error-prone/SOS-associated DNA polymerase III alpha-subunit homolog.
* **polC** — replicative DNA polymerase III alpha subunit in specific bacterial lineages.
* **Pol V** and **DinB/Pol IV** — translesion polymerases; label-only pending taxon-specific grounding.
* **Mismatch-repair machinery** — MutS/MutL-centered system; individual components should be grounded per taxon.
* **Ku/NHEJ machinery** — candidate for DNA-double-strand-break-associated GC patterns, but not a direct cause of this bin.

### Biological processes and pathways

* DNA replication — `GO:0006260`
* DNA repair — `GO:0006281`
* Base-excision repair — `GO:0006284`
* DNA mismatch repair — `GO:0006298`
* DNA recombination — `GO:0006310`
* Cellular response to DNA-damage stimulus — `GO:0006974`
* Nucleotide-excision repair, homologous recombination, nonhomologous end joining, translesion synthesis, SOS response, cytosine deamination, guanine oxidation, mutation fixation, genetic drift, purifying selection, and GC-biased gene conversion — retain label-only unless identifiers are validated during YAML implementation.

### Chemicals and lesions

* Dioxygen — `CHEBI:15379`
* Hydrogen peroxide — `CHEBI:16240`
* Water — `CHEBI:15377`
* Reactive oxygen species, 8-oxo-7,8-dihydroguanine/8-oxoG, 8-oxo-dGTP, uracil in DNA, and G:T or 8-oxoG:A mismatches — label-only pending exact ChEBI validation.

### Taxa and environments

* Bacteria — `NCBITaxon:2`
* *Salmonella* — `NCBITaxon:590`; use a strain-level identifier for the LT2 experiment if validated.
* Oxic environment, oligotrophic environment, aquatic environment, terrestrial environment, host-associated/endosymbiotic environment, high temperature, and low temperature — environmental candidate nodes, but no ENVO CURIE should be assigned without validating the exact intended class.

No organelle is required for the core bacterial mechanism. The relevant localization is chromosomal/genomic DNA and associated replication or repair machinery.

## 4. Candidate evidence-backed edges

The following table prioritizes direct mechanistic edges and then separates comparative or inferred relationships.

| subject | predicate | object | evidence tier | key quantitative/snippet evidence | DOI | curation qualification |
|---|---|---|---|---|---|---|
| loss of **mutM**/**mutY** function | increases | GC→TA transversion burden | direct experimental | In *Salmonella enterica* repair-defective lineages propagated ~5,000 generations, the quintuple mutant accumulated **943** substitutions, with **856 (91%) GC-to-TA transversions**; “inactivation of **mutM** and **mutY** increased GC-to-TA transversions” (lind2008wholegenomemutationalbiases pages 1-2, lind2008wholegenomemutationalbiases pages 3-4) | https://doi.org/10.1073/pnas.0804445105 | **Curatable, strong.** Mechanism alters continuous genome GC downward over time; does **not** specifically imply entry into the 42.65–57.0% bin. |
| loss of **ung**/**vsr**/**mug** function | increases | GC→AT transition burden | direct experimental | Same *Salmonella* mutation-accumulation experiment: **65 (7%) GC-to-AT transitions** in the quintuple mutant; “inactivation of **ung, vsr, and mug** increased GC-to-AT transitions (attributed to deamination)” (lind2008wholegenomemutationalbiases pages 1-2) | https://doi.org/10.1073/pnas.0804445105 | **Curatable, strong.** Downward effect on GC is mechanistically supported, but bin membership is not directly tested. |
| guanine oxidation / **8-oxoG** damage | causes | GC→TA mutational bias | direct experimental / mechanistic | Lind & Andersson found the dominant source of substitutions in repair-defective *Salmonella* was oxidative damage; “**91% of mutations resulted from oxidation of guanine**” (lind2008wholegenomemutationalbiases pages 3-4) | https://doi.org/10.1073/pnas.0804445105 | **Curatable, strong.** General DNA-damage mechanism affecting base composition continuously. |
| cytosine deamination | causes | GC→AT transition bias | direct experimental / mechanistic | In the same experiment, GC→AT transitions increased when uracil/G:T repair functions were removed; “inactivation of **ung, vsr, and mug** increased GC-to-AT transitions (attributed to **deamination**)” (lind2008wholegenomemutationalbiases pages 1-2) | https://doi.org/10.1073/pnas.0804445105 | **Curatable, strong.** Mechanistic but not bin-specific. |
| **MutM** (formamidopyrimidine-DNA glycosylase) | repairs / counteracts | 8-oxoG:C lesions, restoring GC base pairs | direct mechanistic | “**MutM glycosylase excises 8-oxoG paired with C to restore GC base pairs**” (lind2008wholegenomemutationalbiases pages 1-1) | https://doi.org/10.1073/pnas.0804445105 | **Curatable, strong.** Prefer gene/protein-level node plus DNA repair process node. |
| **MutY** adenine glycosylase | repairs / counteracts | 8-oxoG:A mispairs, enabling restoration of GC | direct mechanistic | “**MutY removes adenine from 8-oxoG-A mispairs** allowing DNA repair synthesis” (lind2008wholegenomemutationalbiases pages 1-1) | https://doi.org/10.1073/pnas.0804445105 | **Curatable, strong.** Supports oxidative-damage repair branch. |
| bacterial spontaneous mutation spectrum | is biased toward | AT enrichment / GC loss | broad comparative + review | Across bacteria, mutation is described as “**universally AT-biased**”; genomic GC spans “**<25% to 75%**” and mutation-accumulation studies support excess GC→AT pressure (hershberg2015mutation—theengineof pages 6-7, lassalle2015gccontentevolutionin pages 1-4) | https://doi.org/10.1101/cshperspect.a018077 | **Curatable, moderate.** Good high-level edge for trait graph, but not sufficient alone to explain a mid-range GC bin. |
| intragenic recombination / gBGC | is associated with increased | gene GC content | comparative association | In **11 of 14** bacterial groups with signal, genes with recombination evidence had significantly higher GC, especially GC3; authors argue “**gBGC is probably at work in most if not all bacterial species**” (lassalle2015gccontentevolutionin pages 4-6, lassalle2015gccontentevolutionin pages 1-4) | https://doi.org/10.1101/011023 | **Association only; curate as uncertain.** Strongly relevant for GC evolution, but not direct experimental causation and not bin-specific. |
| evolution of DNA replication and repair (DRR) systems | shapes | long-term bacterial genomic GC content | large comparative genomics | Analysis of **11,083 genomes** concluded that “multiple pathways correlate with genomic GC” and that “ancient adaptations have transformed the DRR system,” producing mutational biases that drive GC variation (teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 10-12) | https://doi.org/10.1128/spectrum.02145-22 | **Curatable, moderate.** Useful parent/process edge; mechanism is evolutionary and indirect. |
| **DnaE2**-containing replication/mutagenesis background | is associated with higher | genomic GC content | comparative association | In **364** eubacterial genomes, dnaE-based groups differed strongly in GC (**F=153.7, P<0.0001**); “**dnaE2 ... correlates with high GC content**” (wu2012onthemolecular pages 2-4, wu2012onthemolecular pages 1-2) | https://doi.org/10.1186/1745-6150-7-2 | **Association only; curate as uncertain.** Comparative signal, not direct perturbation of bin membership. |
| **PolC**-containing replication background | is associated with lower | genomic GC content | comparative association | Wu et al. report “**polC correlates with low GC**”; polymerase-grouping explains substantial GC structure across 364 genomes (wu2012onthemolecular pages 2-4, wu2012onthemolecular pages 1-2) | https://doi.org/10.1186/1745-6150-7-2 | **Association only; curate as uncertain.** Taxon-structured comparative claim, not direct causal proof. |
| oxidative/heat stress and other ancient environmental pressures | select for changes in | DRR gene inventory, indirectly shifting GC trajectories | recent synthesis / comparative | Teng et al. argue stress-related, especially DRR-related, genes were differentially conserved, and environmental stresses correlate with GC through their effects on repair and mutation systems (teng2023genomiclegaciesof pages 8-10, teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 10-12) | https://doi.org/10.1128/spectrum.02145-22 | **Indirect, uncertain.** Best represented as environment → DRR system → mutation spectrum → genomic GC, not direct environment → METPO:1000429. |
| temperature | is associated with | genomic GC content | comparative association | Wu et al. found thermophiles showed higher GC than non-thermophiles across groups (**F=154.4, P<0.0001**), but other reviews note temperature alone is not a sufficient universal explanation (wu2012onthemolecular pages 2-4, hershberg2015mutation—theengineof pages 6-7) | https://doi.org/10.1186/1745-6150-7-2 | **Association only; curate as uncertain.** Confounded and not bin-specific. |
| oxygen requirement | has inconsistent association with | genomic GC content | comparative association | Wu et al. report contradictory patterns and “overall two-way ANOVA did not support oxygen requirement as a primary GC driver (**P=0.852**)” (wu2012onthemolecular pages 2-4) | https://doi.org/10.1186/1745-6150-7-2 | **Do not curate as direct causal edge** without stronger evidence. |
| nutrient limitation (carbon/nitrogen) | may influence | GC-related genome composition trends | model / comparative association | Recent comparative/modeling literature links nutrient economy to GC-related genome properties, but evidence is largely indirect relative to whole-genome GC class assignment (teng2023genomiclegaciesof pages 1-2) | https://doi.org/10.1128/spectrum.02145-22 | **Weak/indirect.** Keep as background note unless trait graph expands to stoichiogenomic ecology. |


*Table: This table summarizes the strongest source-backed candidate edges for curating a causal graph around microbial genomic GC content, emphasizing direct mutation/repair mechanisms first and broader evolutionary associations second. It also notes that most supported mechanisms shift continuous GC over evolutionary time rather than specifically causing membership in the METPO:1000429 mid-range bin.*

### Recommended minimal graph

A conservative first expansion of the existing graph would add these high-confidence triples:

1. **guanine oxidation — produces → 8-oxoG lesion**;
2. **8-oxoG lesion — increases → GC→TA transversion**;
3. **MutM — repairs → 8-oxoG:C lesion**;
4. **MutY — repairs → 8-oxoG:A mismatch**;
5. **cytosine deamination — produces → uracil in DNA / G:U mismatch**;
6. **UNG/MUG/Vsr-mediated repair — decreases → GC→AT transition burden**;
7. **GC→TA transversion burden — decreases over evolutionary time → genome-wide GC content**;
8. **GC→AT transition burden — decreases over evolutionary time → genome-wide GC content**;
9. **genome-wide GC content of 42.65–57.0% — classified as → `METPO:1000429`**.

The experimental anchor is the *Salmonella* mutation-accumulation study. Twelve independent lineages for wild type and each repair-deficient background underwent repeated single-cell bottlenecks for about **5,000 generations**. The quintuple `ung vsr mug mutM mutY` mutant accumulated **943 substitutions**, of which **856 (91%) were GC→TA** and **65 (7%) were GC→AT**; wild type accumulated only 15 mutations without the same bias. Loss of `mutM/mutY` increased oxidative-damage-associated transversions, whereas loss of `ung/vsr/mug` increased deamination-associated transitions. This is strong evidence for lesion/repair→mutation-spectrum edges, although the experiment did not demonstrate movement into the METPO interval itself. (lind2008wholegenomemutationalbiases pages 1-1, lind2008wholegenomemutationalbiases pages 1-2, lind2008wholegenomemutationalbiases pages 3-4, lind2008wholegenomemutationalbiases pages 5-6)

## 5. Recent developments and expert interpretation

### 2023 large-scale “ancient adaptation” model

Teng et al. found that bacterial GC is phylogenetically bimodal and that multiple replication/repair pathways covary with it. Their interpretation is that environmental adaptation historically altered repair machinery; those changes then modified mutation spectra and left long-lived genomic-composition legacies. Low-GC clades showed loss of stress-response and repair functions, with cold, low-oxygen, and oligotrophic settings proposed as ancestral contexts. However, the work is comparative: it supports a structured causal hypothesis but does not experimentally show an environmental exposure changing whole-genome GC. (teng2023genomiclegaciesof pages 8-10, teng2023genomiclegaciesof pages 1-2)

The study further discusses cytosine deamination and guanine oxidation as GC-reducing sources, and reports opposing effects associated with different oxidative-damage repair defects: `mutM` loss is linked to AT bias, whereas `mutT` loss can produce GC bias. Error-prone polymerases such as Pol V, DinB, and DnaE2 can alter mutation spectra, particularly under stress. These observations caution against treating “less repair” as a uniformly GC-lowering mechanism. (teng2023genomiclegaciesof pages 10-12)

### Polymerase-system hypothesis

Wu et al. analyzed **364 eubacterial genomes**, divided into `dnaE1|polV` (n=173), `dnaE1|dnaE2` (n=115), and `dnaE3|polV` (n=76) groups. GC differed strongly among groups (**F=153.7, P<0.0001**), with `dnaE2` associated with higher GC and `polC` with lower GC. Because taxonomy and polymerase inventory are deeply coupled, these should be represented as uncertain associations, not universal gene→trait edges. (wu2012onthemolecular pages 1-2, wu2012onthemolecular pages 2-4)

### Recombination and biased gene conversion

A bacterial gBGC analysis evaluated 20 bacterial and one archaeal group. Among 14 groups with sufficient recombination signal, **11** showed significantly higher GC in recombining genes, especially at third codon positions; flanking intergenic regions showed a similar pattern. The authors argue that gBGC can mimic positive selection and may oppose universal AT-biased mutation. Nevertheless, recombination–GC covariation does not itself prove molecular conversion bias, and the source is a preprint DOI. Curate as uncertain. (lassalle2015gccontentevolutionin pages 4-6, lassalle2015gccontentevolutionin pages 1-4)

### Environmental relationships

Temperature showed a strong comparative association in Wu et al. (**F=154.4, P<0.0001**), but broader reviews find mixed results and reject temperature as a sole universal driver. Oxygen is even weaker: the same analysis found no overall primary effect (**P=0.852**). Environmental nodes should therefore connect through repair-system evolution or DNA-damage exposure, not directly to `METPO:1000429`. (wu2012onthemolecular pages 2-4, hershberg2015mutation—theengineof pages 6-7)

## 6. Applications and real-world implementations

Genome-wide GC content is routinely used in microbial genome annotation, assembly quality control, detection of anomalous genomic islands or horizontal transfer, codon-optimization planning, primer and probe design, DNA melting-condition selection, and taxonomic description. For TraitMech, the principal implementation is reproducible phenotype assignment from an assembled genome: calculate whole-genome GC under a documented protocol, retain assembly completeness and replicon handling, and map the continuous value to the METPO bin.

Mechanistic graph information also improves interpretation of comparative genomics. Repair-gene loss can explain directional mutation spectra; recombination can confound selection scans; and GC composition predicts broad codon-usage and amino-acid-composition effects because microbial genomes have high coding density. Core and accessory regions should be treated separately when identifying local deviations, but those analyses must not replace the whole-genome value used for this trait. (teng2023genomiclegaciesof pages 1-2, lassalle2015gccontentevolutionin pages 1-4)

## 7. Warnings: claims not yet ready for TraitMech curation

1. **Do not encode “low GC” as below 42.65%.** The identifier’s authoritative numeric bin controls despite the misleading label.
2. **Do not assert that any identified mechanism specifically causes `METPO:1000429`.** Most evidence concerns directional change in continuous GC, not entry into this interval.
3. **Do not curate oxygen requirement → GC content as causal.** The reported overall test was nonsignificant.
4. **Do not curate temperature → GC as a universal direct edge.** Comparative effects are phylogenetically confounded and inconsistent across studies.
5. **Treat `dnaE2`→high GC and `polC`→low GC as uncertain.** These are taxonomically structured associations.
6. **Treat recombination→higher GC through gBGC as uncertain.** The evidence is strong association but not direct bacterial molecular demonstration.
7. **Do not equate repair-gene absence with lower GC in every context.** Different lesions and enzymes can drive mutation spectra in opposite directions; `mutT` illustrates this complexity.
8. **Do not infer genome-wide GC from GC3, ribosomal genes, 16S rRNA, core genes, or a single replicon.**
9. **Do not assign cross-species UniProt identifiers to gene symbols.** Ground `mutM`, `mutY`, `mutT`, `ung`, `mug`, `vsr`, `dnaE2`, and `polC` only after the taxon is fixed.
10. **Endosymbiosis, genome reduction, drift, carbon limitation, nitrogen economy, and DNA-double-strand-break exposure are biologically plausible modifiers but lack sufficient evidence here for direct edges to this exact bin.**

## DOI-first bibliography

1. Teng W, Liao B, Chen M, Shu W. **Genomic Legacies of Ancient Adaptation Illuminate GC-Content Evolution in Bacteria.** *Microbiology Spectrum*. Published February 2023. DOI: [10.1128/spectrum.02145-22](https://doi.org/10.1128/spectrum.02145-22). Large comparative analysis of 11,083 genomes and the principal recent source for the DRR-legacy model. (teng2023genomiclegaciesof pages 8-10, teng2023genomiclegaciesof pages 1-2, teng2023genomiclegaciesof pages 10-12)
2. Lind PA, Andersson DI. **Whole-genome mutational biases in bacteria.** *Proceedings of the National Academy of Sciences*. Published November 2008;105:17878–17883. DOI: [10.1073/pnas.0804445105](https://doi.org/10.1073/pnas.0804445105). Direct mutation-accumulation evidence in repair-deficient *Salmonella*. (lind2008wholegenomemutationalbiases pages 1-1, lind2008wholegenomemutationalbiases pages 4-5, lind2008wholegenomemutationalbiases pages 1-2, lind2008wholegenomemutationalbiases pages 3-4, lind2008wholegenomemutationalbiases pages 5-6)
3. Wu H, Zhang Z, Hu S, Yu J. **On the molecular mechanism of GC content variation among eubacterial genomes.** *Biology Direct*. Published January 2012;7:2. DOI: [10.1186/1745-6150-7-2](https://doi.org/10.1186/1745-6150-7-2). Comparative polymerase-system, temperature, oxygen, and habitat analysis of 364 genomes. (wu2012onthemolecular pages 1-2, wu2012onthemolecular pages 2-4)
4. Hershberg R. **Mutation—The Engine of Evolution: Studying Mutation and Its Role in the Evolution of Bacteria.** *Cold Spring Harbor Perspectives in Biology*. Published September 2015;7:a018077. DOI: [10.1101/cshperspect.a018077](https://doi.org/10.1101/cshperspect.a018077). Authoritative synthesis of bacterial mutation rates, AT bias, repair effects, selection, and gBGC. (hershberg2015mutation—theengineof pages 6-7)
5. Lassalle F, Périan S, Bataillon T, et al. **GC-content evolution in bacterial genomes: the biased gene conversion hypothesis expands.** Preprint posted November 2014/revised 2015. DOI: [10.1101/011023](https://doi.org/10.1101/011023). Comparative recombination–GC analysis; use with preprint and association-only qualification. (lassalle2015gccontentevolutionin pages 4-6, lassalle2015gccontentevolutionin pages 1-4)

## Bottom line for `data/traits/genomics/gc_low.yaml`

Curate the numeric classification edge and the experimentally established lesion–repair–mutation-spectrum pathway first. Represent environmental factors, polymerase inventories, and gBGC as uncertain upstream modifiers. Every mechanistic path should terminate in a **continuous genome-wide GC-content node**, followed by an explicit computational binning edge to **`METPO:1000429`**; it should not terminate directly at the trait from an environmental or gene node.

References

1. (teng2023genomiclegaciesof pages 1-2): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 52 citations and is from a domain leading peer-reviewed journal.

2. (hershberg2015mutation—theengineof pages 6-7): Ruth Hershberg. Mutation—the engine of evolution: studying mutation and its role in the evolution of bacteria: figure 1. Cold Spring Harbor Perspectives in Biology, 7:a018077, Sep 2015. URL: https://doi.org/10.1101/cshperspect.a018077, doi:10.1101/cshperspect.a018077. This article has 128 citations and is from a peer-reviewed journal.

3. (teng2023genomiclegaciesof pages 8-10): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 52 citations and is from a domain leading peer-reviewed journal.

4. (teng2023genomiclegaciesof pages 10-12): Wenkai Teng, Bin Liao, Mengyun Chen, and Wensheng Shu. Genomic legacies of ancient adaptation illuminate gc-content evolution in bacteria. Feb 2023. URL: https://doi.org/10.1128/spectrum.02145-22, doi:10.1128/spectrum.02145-22. This article has 52 citations and is from a domain leading peer-reviewed journal.

5. (lind2008wholegenomemutationalbiases pages 1-2): Peter A. Lind and Dan I. Andersson. Whole-genome mutational biases in bacteria. Proceedings of the National Academy of Sciences, 105:17878-17883, Nov 2008. URL: https://doi.org/10.1073/pnas.0804445105, doi:10.1073/pnas.0804445105. This article has 244 citations and is from a highest quality peer-reviewed journal.

6. (lind2008wholegenomemutationalbiases pages 3-4): Peter A. Lind and Dan I. Andersson. Whole-genome mutational biases in bacteria. Proceedings of the National Academy of Sciences, 105:17878-17883, Nov 2008. URL: https://doi.org/10.1073/pnas.0804445105, doi:10.1073/pnas.0804445105. This article has 244 citations and is from a highest quality peer-reviewed journal.

7. (lind2008wholegenomemutationalbiases pages 1-1): Peter A. Lind and Dan I. Andersson. Whole-genome mutational biases in bacteria. Proceedings of the National Academy of Sciences, 105:17878-17883, Nov 2008. URL: https://doi.org/10.1073/pnas.0804445105, doi:10.1073/pnas.0804445105. This article has 244 citations and is from a highest quality peer-reviewed journal.

8. (lassalle2015gccontentevolutionin pages 1-4): Florent Lassalle, Séverine Périan, Thomas Bataillon, Xavier Nesme, Laurent Duret, and Vincent Daubin. Gc-content evolution in bacterial genomes: the biased gene conversion hypothesis expands. ArXiv, Nov 2015. URL: https://doi.org/10.1101/011023, doi:10.1101/011023. This article has 278 citations.

9. (lassalle2015gccontentevolutionin pages 4-6): Florent Lassalle, Séverine Périan, Thomas Bataillon, Xavier Nesme, Laurent Duret, and Vincent Daubin. Gc-content evolution in bacterial genomes: the biased gene conversion hypothesis expands. ArXiv, Nov 2015. URL: https://doi.org/10.1101/011023, doi:10.1101/011023. This article has 278 citations.

10. (wu2012onthemolecular pages 2-4): Hao Wu, Zhang Zhang, Songnian Hu, and Jun Yu. On the molecular mechanism of gc content variation among eubacterial genomes. Biology Direct, 7:2-2, Jan 2012. URL: https://doi.org/10.1186/1745-6150-7-2, doi:10.1186/1745-6150-7-2. This article has 169 citations and is from a peer-reviewed journal.

11. (wu2012onthemolecular pages 1-2): Hao Wu, Zhang Zhang, Songnian Hu, and Jun Yu. On the molecular mechanism of gc content variation among eubacterial genomes. Biology Direct, 7:2-2, Jan 2012. URL: https://doi.org/10.1186/1745-6150-7-2, doi:10.1186/1745-6150-7-2. This article has 169 citations and is from a peer-reviewed journal.

12. (lind2008wholegenomemutationalbiases pages 5-6): Peter A. Lind and Dan I. Andersson. Whole-genome mutational biases in bacteria. Proceedings of the National Academy of Sciences, 105:17878-17883, Nov 2008. URL: https://doi.org/10.1073/pnas.0804445105, doi:10.1073/pnas.0804445105. This article has 244 citations and is from a highest quality peer-reviewed journal.

13. (lind2008wholegenomemutationalbiases pages 4-5): Peter A. Lind and Dan I. Andersson. Whole-genome mutational biases in bacteria. Proceedings of the National Academy of Sciences, 105:17878-17883, Nov 2008. URL: https://doi.org/10.1073/pnas.0804445105, doi:10.1073/pnas.0804445105. This article has 244 citations and is from a highest quality peer-reviewed journal.