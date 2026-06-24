---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:11:34.656255'
end_time: '2026-06-18T03:38:41.405104'
duration_seconds: 1626.75
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'gc_mid2_mid_high_gc_bin: 3 nodes, 2 edges'
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
- **METPO identifier:** METPO:1000431
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 57.0% and 66.3% (the METPO `GC_57.0_66.3` bin).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_57.0_66.3
- **Existing evidence:** DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports moderate GC-biased gene conversion as the mechanism producing mid-high GC content.)
- **Existing causal graph summary:** gc_mid2_mid_high_gc_bin: 3 nodes, 2 edges

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
- **METPO identifier:** METPO:1000431
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition between approximately 57.0% and 66.3% (the METPO `GC_57.0_66.3` bin).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_57.0_66.3
- **Existing evidence:** DOI:10.1186/1471-2148-10-374: GC-biased gene conversion (Bacterial-GC-content evolution review supports moderate GC-biased gene conversion as the mechanism producing mid-high GC content.)
- **Existing causal graph summary:** gc_mid2_mid_high_gc_bin: 3 nodes, 2 edges

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


# Research Report: Microbial Trait GC mid2 (METPO:1000431)

## 1) Scope summary (trait meaning and boundaries)

**Trait definition.** GC mid2 is a *genome-wide GC-content phenotype* where the mean fraction of guanine + cytosine (G+C) across an organism’s genome falls between **~57.0% and 66.3%** (the METPO `GC_57.0_66.3` bin). Genome-wide GC% is operationally defined as the proportion of G and C nucleotides across the full genome assembly/sequence. (deka2025basesubstitutionsin pages 1-3)

**Where it sits in prokaryotic variation.** Across bacteria, genome-wide GC% is highly variable; one synthesis reports a typical bacterial range of **~13–75% GC**. (deka2025basesubstitutionsin pages 1-3)

**Boundary cases and nearby traits.** The GC mid2 bin captures organisms that are “moderately high GC” but not extreme (e.g., Actinobacteria/Actinomycetota often exceed ~55% GC in some compilations). (deka2025basesubstitutionsin pages 1-3) It should be distinguished from:
- **Lower GC bins** (e.g., many Firmicutes/Bacillota around ~43% in one synthesis), and
- **Very high GC** outliers (e.g., *Mycobacterium smegmatis* cited as ~80% GC). (deka2025basesubstitutionsin pages 1-3, radrizzani2025bacterialgene5′ pages 18-21)

**Assay/measurement considerations (important for curation).** GC% is not purely biological signal; it can be distorted by technical factors:
- **Assembly GC bias**: in simulated Illumina assemblies, sequencing depth, error rate, and PCR duplicate ratio could *inflate* GC% for low-GC genomes but *decrease* GC% for high-GC genomes, i.e., the direction of bias depends on the true GC%. (radai2024anoverlookedphenomenon pages 10-12)
- **Within-genome heterogeneity**: GC can be discussed at multiple scales (whole genome vs gene-level vs codon-position such as GC3), and recombination/selection can create regional differences even when the genome average is stable. (lassalle2015gccontentevolutionin pages 9-11)

## 2) Key concepts and current mechanistic understanding (definitions)

### 2.1 Mutation bias and chemical lesion processes
A widely discussed baseline is that many bacteria have a **mutational bias toward A/T** (excess of G/C→A/T changes), which would tend to *reduce* genomic GC over time unless countered by other forces. (lassalle2015gccontentevolutionin pages 1-4, lassalle2015gccontentevolutionin pages 4-6)

Chemical and repair-related sources that can generate compositional biases include **cytosine deamination** (C→T) and **oxidative lesions** such as guanine oxidation (e.g., 8-oxoG leading to G→T). These are often framed as pushing genomes toward A/T enrichment depending on repair and exposure. (deka2025basesubstitutionsin pages 13-15, deka2025basesubstitutionsin pages 1-3)

### 2.2 GC-biased gene conversion (gBGC)
**Definition (concept).** GC-biased gene conversion is a recombination-associated process in which the repair/conversion of mismatches in heteroduplex DNA during recombination is biased in favor of GC alleles, producing a fixation pattern similar to positive selection for GC. (lassalle2015gccontentevolutionin pages 1-4)

**Operational signal used in bacteria.** A key within-genome signature is **higher GC (especially GC3) in genes with evidence of recombination** compared with nonrecombining genes, which suggests a GC-favoring force linked to recombination rather than amino-acid level selection. (lassalle2015gccontentevolutionin pages 9-11, lassalle2015gccontentevolutionin pages 4-6)

### 2.3 DNA double-strand breaks (DSBs) and end-joining pathways
**NHEJ core factor Ku.** Across many prokaryotic genomes, the **presence of Ku** (a marker for bacterial non-homologous end joining, NHEJ) is reported to be **positively associated with higher genomic GC content**, even after controlling for phylogeny and genome length; the authors argue the association cannot be explained by mutational bias alone. (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 5-6)

**Mechanistic hypothesis (repair efficiency selection).** A proposed mechanism is that **GC-rich microhomologies/overhangs** stabilize end-pairing (more hydrogen bonds), which could improve the efficiency/accuracy of **Ku-dependent NHEJ** or **microhomology-mediated end joining**, thereby generating selection for higher GC in DSB-prone contexts. (weissman2019linkinghighgc pages 14-15)

**Local GC elevation around DSB-prone loci.** GC can be locally elevated near putative DSB-prone loci such as **restriction sites**; restriction enzymes also tend to have recognition sequences with higher GC content than genomic background in one analysis. (weissman2019linkinghighgc pages 15-17)

## 3) Recent developments and latest research (priority 2023–2024)

### 3.1 2024: Quantified assembly/measurement bias affecting GC% estimation
A 2024 study of bacterial de novo genome assembly quality emphasizes that **GC% bias in assemblies depends on technical parameters** (depth, error rate, PCR duplicates) and *interacts* with the true underlying genome GC%. This is directly relevant to trait-binning curation because MAG/assembly pipelines can shift genomes across GC bins. (Jan 2024; DOI:10.1186/s12864-023-09910-4; https://doi.org/10.1186/s12864-023-09910-4) (radai2024anoverlookedphenomenon pages 10-12)

### 3.2 2024: DNA repair/mismatch repair nodes connecting replication error spectra to DSB processing
A 2024 Nucleic Acids Research paper describes the non-canonical mismatch repair endonuclease **NucS/EndoMS**, which cleaves mismatched DNA (notably **G/T mismatches**) and can generate **double-strand breaks** as part of mismatch processing, with downstream repair potentially involving HR or NHEJ depending on organism/context. This provides concrete mechanistic nodes (NucS, replication clamp interaction, DSB generation) that can be linked (with caution) to long-term mutation spectra shaping base composition. (Mar 2024; DOI:10.1093/nar/gkae132; https://doi.org/10.1093/nar/gkae132) (dagva2024correctionofnonrandom pages 1-2, dagva2024correctionofnonrandom pages 12-13)

### 3.3 2023: Reviews of “genomic signatures” and within-genome compositional structure
A 2023 review emphasizes that genome composition (including GC content) behaves as a species-level “signature,” often stable enough that relatively small fragments can approximate whole-genome composition, while still acknowledging within-genome heterogeneity driven by variables like recombination and gene structure. (Feb 2023; DOI:10.3390/biology12020322; https://doi.org/10.3390/biology12020322) (fuente2023genomicsignaturein pages 13-15)

## 4) Current applications and real-world implementations

### 4.1 Practical use of GC% as a genomic QC and ecological descriptor
- **Assembly/QC and binning:** Because assembly parameters can bias GC%, GC bins like GC mid2 should be curated with metadata about genome quality, sequencing platform, and assembly approach where possible; bias can move genomes across bin boundaries. (radai2024anoverlookedphenomenon pages 10-12)
- **Comparative genomics:** GC% is routinely used to contextualize genomes in phylogenomics, codon usage studies, and detection of horizontally transferred regions (which can differ in GC from host background). (fuente2023genomicsignaturein pages 13-15, deka2025basesubstitutionsin pages 1-3)

### 4.2 Interactions with genome editing and guide design (implementation-relevant note)
Although not a direct causal driver, GC content is used as a practical feature in many computational genomics contexts (e.g., “GC content” as a feature in bacterial sgRNA activity prediction models), and GC-rich genomes can pose specific PCR/sequencing challenges. This reinforces the need to record assay context in trait curation rather than treating GC% as purely biological. (radai2024anoverlookedphenomenon pages 10-12)

## 5) Expert opinions and authoritative analysis (debate mapping)

**gBGC vs selection vs mutation bias remains contested.** Two widely cited lines of evidence are important for curation:
1) **Within-genome recombination–GC correlations**: evidence that recombining genes have elevated GC (strongest at GC3) supports a gBGC-like force operating locally in many bacterial clades. (lassalle2015gccontentevolutionin pages 9-11, lassalle2015gccontentevolutionin pages 4-6)
2) **Ku/NHEJ–GC association and repair-selection hypothesis**: comparative genomics reports a strong association between Ku presence and elevated GC, alongside a mechanistic argument that high GC could facilitate end-joining repair. However, the authors also report that between-genome Ku incidence does *not* simply track inferred homologous recombination rates, and they treat parts of the causal story as requiring experimental confirmation. (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 10-11, weissman2019linkinghighgc pages 14-15)

For TraitMech curation, this implies:
- gBGC-related edges (recombination → gBGC → increased GC, especially at synonymous positions) can often be curated with **moderate-to-high confidence** where supported by within-genome comparisons. (lassalle2015gccontentevolutionin pages 9-11, lassalle2015gccontentevolutionin pages 4-6)
- Ku/NHEJ associations with high GC should often be encoded as **association edges** or **uncertain causal edges** unless additional mechanistic evidence for a specific lineage/environment is provided. (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 14-15)

## 6) Relevant statistics and data points (recently cited)

- **Bacterial genome-wide GC range:** ~13–75% in one synthesis. (deka2025basesubstitutionsin pages 1-3)
- **Ku/NHEJ prevalence and dataset scale:** A large comparative analysis used **104,297** RefSeq genomes; **21,389** contained Ku (Pfam PF02735). (weissman2019linkinghighgc pages 15-17)
- **Association strength example:** one excerpt reports Pearson **r ≈ 0.54** for Ku presence vs genomic GC distribution shift (highly significant), emphasizing Ku is not the sole predictor. (weissman2019linkinghighgc pages 5-6)

## 7) Candidate nodes and causal edges for `gc_mid2.yaml`

The following artifact provides curation-ready candidate nodes (with suggested ontology grounding) and evidence-backed candidate causal edges (triples) with snippets, DOI/URLs, and confidence levels.

| Node label | Node type (process/gene/protein/environment/assay) | Suggested CURIE/ID (if known) | Brief definition | Key supporting sources (citation IDs) |
|---|---|---|---|---|
| Genome-wide GC content 57.0–66.3% (GC mid2) | assay | METPO:1000431 | Genome-average fraction of G+C bases falling in the reviewed mid-high GC bin 57.0–66.3%. | (deka2025basesubstitutionsin pages 1-3, weissman2019linkinghighgc pages 15-17) |
| GC-biased gene conversion | process | GO:0006298 | Recombination-associated biased fixation favoring G/C alleles over A/T during repair/conversion. | (lassalle2015gccontentevolutionin pages 9-11, lassalle2015gccontentevolutionin pages 1-4, lassalle2015gccontentevolutionin pages 4-6) |
| Homologous recombination | process | GO:0000724 | Template-directed exchange/repair pathway proposed to elevate GC locally or genome-wide via gBGC or by increasing efficacy of selection. | (torrance2025homologousrecombinationshapes pages 1-4, lassalle2015gccontentevolutionin pages 9-11, weissman2019linkinghighgc pages 15-17) |
| Recombining genes | assay | label-only candidate | Genes with evidence of intra-genic recombination; often show elevated GC, especially GC3, within genomes. | (lassalle2015gccontentevolutionin pages 4-6, lassalle2015gccontentevolutionin pages 9-11) |
| GC3 (third codon position GC) | assay | label-only candidate | GC fraction at synonymous-prone third codon positions; strongest recombination-associated GC signal in several studies. | (lassalle2015gccontentevolutionin pages 9-11, lassalle2015gccontentevolutionin pages 4-6) |
| Non-homologous end joining | process | GO:0006303 | DSB repair pathway used when homologous template is unavailable; associated with elevated genomic GC in prokaryotes. | (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 14-15) |
| Ku protein | protein | PFAM:PF02735 | Core NHEJ DNA end-binding protein; presence is strongly associated with higher genomic GC across prokaryotes. | (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 5-6) |
| LigD | protein | UniProtKB family label-only candidate | Bacterial NHEJ ligase commonly paired with Ku for end joining of DSBs. | (dagva2024correctionofnonrandom pages 12-13, dagva2024correctionofnonrandom pages 1-2) |
| DNA double-strand break repair | process | GO:0006302 | Cellular repair of double-strand breaks by HR, NHEJ, or alternative routes; central candidate driver of elevated/local GC. | (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 14-15) |
| DNA double-strand break rate | environment | label-only candidate | Frequency of DSB formation in a lineage/environment; hypothesized to increase selection for GC-rich repair-favorable sequences. | (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 14-15, weissman2019linkinghighgc pages 5-6) |
| Restriction–modification system / restriction sites | process | GO:0009307 | Endogenous source of DSB-prone loci; recognition sites and flanks show GC enrichment in some analyses. | (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 14-15) |
| Local GC enrichment near DSB-prone loci | assay | label-only candidate | Elevated GC in sequence windows around break-prone sites, proposed as repair-associated selection signal. | (weissman2019linkinghighgc pages 15-17) |
| Mutation bias toward AT | process | label-only candidate | Net excess of G/C→A/T mutations observed broadly in bacteria, acting against maintenance of high genomic GC. | (deka2025basesubstitutionsin pages 3-5, deka2025basesubstitutionsin pages 1-3, lassalle2015gccontentevolutionin pages 1-4) |
| Cytosine deamination | process | GO:0006307 | Spontaneous/chemically promoted C→T transition source contributing to AT enrichment. | (deka2025basesubstitutionsin pages 3-5, deka2025basesubstitutionsin pages 13-15, hale2025elevatedratesand pages 14-17) |
| Guanine oxidation / 8-oxoG-associated damage | process | GO:0006979 | Oxidative lesion process yielding G→T/C→A transversions and contributing to compositional bias. | (deka2025basesubstitutionsin pages 3-5, deka2025basesubstitutionsin pages 13-15, hale2025elevatedratesand pages 14-17) |
| DNA repair efficiency | process | label-only candidate | Efficiency/specificity of repair pathways affecting which mutational biases are fixed over time. | (deka2025basesubstitutionsin pages 13-15, deka2025basesubstitutionsin pages 1-3, radrizzani2025bacterialgene5′ pages 18-21) |
| NucS / EndoMS | protein | UniProtKB family label-only candidate | Non-canonical mismatch repair endonuclease in actinobacteria/archaea that cleaves mismatches to generate DSBs. | (dagva2024correctionofnonrandom pages 12-13, dagva2024correctionofnonrandom pages 1-2) |
| Non-canonical mismatch repair (NucS-dependent) | process | GO:0006298 | Alternative MMR pathway that removes replication mismatches via NucS-generated DSBs and downstream repair. | (dagva2024correctionofnonrandom pages 12-13, dagva2024correctionofnonrandom pages 1-2) |
| Replication clamp (β-clamp/PCNA) | protein complex | GO:0030896 | Clamp that recruits/stimulates NucS and links mismatch processing to replication. | (dagva2024correctionofnonrandom pages 12-13, dagva2024correctionofnonrandom pages 1-2) |
| G/T mismatch | assay | label-only candidate | Replication mismatch preferentially processed by NucS in Streptomyces-related systems. | (dagva2024correctionofnonrandom pages 12-13, dagva2024correctionofnonrandom pages 1-2) |
| Oxygen exposure / aerobiosis | environment | ENVO:01001017 | Environmental/physiological context linked to oxidative DNA damage and historically associated with GC variation. | (hale2025elevatedratesand pages 14-17, weissman2019linkinghighgc pages 21-24) |
| Fermentative growth / acidic conditions | environment | label-only candidate | Conditions proposed to increase spontaneous deamination and shape mutation spectra in LAB. | (hale2025elevatedratesand pages 14-17) |
| Soil habitat / DSB-prone habitats | environment | ENVO:00001998 | Example habitat class repeatedly associated with high-GC microbes; may proxy higher DNA damage stress. | (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 5-6) |
| Sequencing/assembly GC bias | assay | label-only candidate | Technical bias where observed assembly GC shifts with original GC%, depth, error rate, and duplicates. | (radai2024anoverlookedphenomenon pages 10-12) |

| Subject | Predicate | Object | Evidence snippet (short quote) | Reference (DOI + URL + year) | Confidence (high/medium/uncertain) | Notes for YAML curation |
|---|---|---|---|---|---|---|
| Homologous recombination | positively influences | GC-biased gene conversion | “gBGC… recombination tends to increase fixation of AT→GC mutations” | 10.1101/011023 — https://doi.org/10.1101/011023 — 2015 | high | Foundational mechanism; process-level edge appropriate. (lassalle2015gccontentevolutionin pages 1-4) |
| GC-biased gene conversion | positively influences | genome-wide GC content 57.0–66.3% | “recombining genes tend to have higher GC-content” and effect is “stronger at third codon positions (GC3)” | 10.1101/011023 — https://doi.org/10.1101/011023 — 2015 | medium | Supports elevated GC generally, not specific to exact 57–66.3% bin; curate as contributing mechanism to mid-high GC. (lassalle2015gccontentevolutionin pages 9-11, lassalle2015gccontentevolutionin pages 4-6) |
| Recombining genes | has increased attribute | GC3 | “effect strongest at third codon positions (GC3)” | 10.1101/011023 — https://doi.org/10.1101/011023 — 2015 | high | Useful as an intermediate assay node; within-genome comparative evidence. (lassalle2015gccontentevolutionin pages 4-6) |
| Ku protein | part of | non-homologous end joining | “presence of the NHEJ pathway (Ku)” | 10.1371/journal.pgen.1008493 — https://doi.org/10.1371/journal.pgen.1008493 — 2019 | high | Straightforward composition edge. (weissman2019linkinghighgc pages 15-17) |
| Ku protein | positively associated with | genome-wide GC content 57.0–66.3% | “strong positive association between presence of the NHEJ pathway (Ku) and genomic GC content” | 10.1371/journal.pgen.1008493 — https://doi.org/10.1371/journal.pgen.1008493 — 2019 | medium | Association is robust across genomes, but mechanism debated; curate as association or uncertain causal edge. (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 5-6) |
| DNA double-strand break rate | positively influences | selection for high GC content | “high rates of DSB formation… are linked to elevated local and genome-level GC content” | 10.1371/journal.pgen.1008493 — https://doi.org/10.1371/journal.pgen.1008493 — 2019 | medium | Mechanistic hypothesis from comparative genomics; likely curation-worthy with uncertainty flag. (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 14-15) |
| High GC overhangs/microhomologies | positively influences | end joining efficiency/accuracy | “High GC content increases hydrogen bonding… stabilizing end-pairing” and “increases efficiency/accuracy of NHEJ” | 10.1371/journal.pgen.1008493 — https://doi.org/10.1371/journal.pgen.1008493 — 2019 | medium | Mechanistic rationale for DSB→GC selection; object may be label-only candidate node. (weissman2019linkinghighgc pages 14-15) |
| Restriction–modification system / restriction sites | associated with | local GC enrichment near DSB-prone loci | “restriction enzymes tend to have higher-GC recognition sequences than genomic background” and flanks are “GC-enriched” | 10.1371/journal.pgen.1008493 — https://doi.org/10.1371/journal.pgen.1008493 — 2019 | medium | Good local, not whole-genome, signal; curate as local repair-associated edge. (weissman2019linkinghighgc pages 15-17) |
| Mutation bias toward AT | negatively influences | genome-wide GC content 57.0–66.3% | “universal excess of G/C→A/T mutations” and mutation is “universally biased towards AT” | 10.1101/011023 — https://doi.org/10.1101/011023 — 2015 | high | Strong broad background edge; explains why added GC-promoting forces are needed. (lassalle2015gccontentevolutionin pages 1-4, lassalle2015gccontentevolutionin pages 4-6) |
| Cytosine deamination | positively influences | mutation bias toward AT | “cytosine deamination (C→T)” drives “A+T enrichment” | 10.63635/mrj.v1i4.188 — https://doi.org/10.63635/mrj.v1i4.188 — 2025 | medium | Recent but lower-authority review; acceptable as mechanistic chemistry edge, not specific to mid2. (deka2025basesubstitutionsin pages 13-15, deka2025basesubstitutionsin pages 1-3) |
| Guanine oxidation / 8-oxoG-associated damage | positively influences | mutation bias toward AT | “guanine oxidation to 8-oxo-guanine (G→T)” | 10.63635/mrj.v1i4.188 — https://doi.org/10.63635/mrj.v1i4.188 — 2025 | medium | Chemistry-based edge; may remain label-only if GO grounding too broad. (deka2025basesubstitutionsin pages 3-5, deka2025basesubstitutionsin pages 13-15) |
| Oxygen exposure / aerobiosis | positively influences | oxidative DNA damage | cited literature implicates “oxygen/aerobiosis and oxygen metabolism” and “oxidative DNA damage” as lesion sources | 10.1371/journal.pgen.1008493 — https://doi.org/10.1371/journal.pgen.1008493 — 2019 | medium | Indirect summary from cited literature within review/discussion; better as uncertain environmental edge. (weissman2019linkinghighgc pages 21-24) |
| Fermentative growth / acidic conditions | positively influences | cytosine deamination | “fermentative metabolism and acidic byproducts… promote spontaneous deamination” | 10.1128/mbio.03054-25 — https://doi.org/10.1128/mbio.03054-25 — 2025 | medium | Taxon-specific to LAB context; mark uncertain/taxon-specific. (hale2025elevatedratesand pages 14-17) |
| NucS / EndoMS | part of | non-canonical mismatch repair (NucS-dependent) | “NucS/EndoMS… non-canonical MMR endonuclease” | 10.1093/nar/gkae132 — https://doi.org/10.1093/nar/gkae132 — 2024 | high | Good protein-to-process edge. (dagva2024correctionofnonrandom pages 1-2) |
| NucS / EndoMS | acts on | G/T mismatch | “specifically eliminates G/T replication errors” | 10.1093/nar/gkae132 — https://doi.org/10.1093/nar/gkae132 — 2024 | high | Strong mechanistic edge, though relevance to whole-genome GC is indirect. (dagva2024correctionofnonrandom pages 1-2) |
| NucS / EndoMS | produces | DNA double-strand break | “cleaves both strands to create double-strand breaks (DSBs)” | 10.1093/nar/gkae132 — https://doi.org/10.1093/nar/gkae132 — 2024 | high | Strong mechanistic edge; useful for DSB-centered subgraph. (dagva2024correctionofnonrandom pages 1-2) |
| Replication clamp (β-clamp/PCNA) | positively regulates | NucS / EndoMS | “interacts with and stimulates NucS/EndoMS” | 10.1093/nar/gkae132 — https://doi.org/10.1093/nar/gkae132 — 2024 | high | Specific mechanistic edge; downstream relevance to GC remains indirect. (dagva2024correctionofnonrandom pages 1-2) |
| DNA repair efficiency | influences | genome-wide GC content 57.0–66.3% | “variations in DNA repair efficiency influence fixation of nucleotide changes and thus long-term G+C content” | 10.63635/mrj.v1i4.188 — https://doi.org/10.63635/mrj.v1i4.188 — 2025 | medium | Broad but useful umbrella edge; lower-authority review. (deka2025basesubstitutionsin pages 1-3) |
| Sequencing/assembly GC bias | can distort measurement of | genome-wide GC content 57.0–66.3% | “in low GC% genomes… inflate GC-content of the assembly, whereas for high-GC% genomes these factors will decrease GC content” | 10.1186/s12864-023-09910-4 — https://doi.org/10.1186/s12864-023-09910-4 — 2024 | high | Assay/measurement caution edge; useful metadata rather than biology. (radai2024anoverlookedphenomenon pages 10-12) |
| Homologous recombination | may increase efficacy of | selection for GC-rich alleles | recombination “influences GC-content by increasing the effectiveness of selection rather than via GC-biased gene conversion” | 10.1093/nar/gkae1265 — https://doi.org/10.1093/nar/gkae1265 — 2025 | uncertain | Recent synthesis challenges classic gBGC-only interpretation; do not over-curate without primary 2024 PNAS analysis. (torrance2025homologousrecombinationshapes pages 1-4) |
| Soil habitat / DSB-prone habitats | associated with | high genomic GC content | “Some environments (e.g. soils) are associated with a high genomic GC content of their inhabitants” | 10.1371/journal.pgen.1008493 — https://doi.org/10.1371/journal.pgen.1008493 — 2019 | medium | Environmental association only; avoid direct causal curation without stronger mechanistic evidence. (weissman2019linkinghighgc pages 15-17) |


*Table: This artifact provides curation-ready tables of candidate nodes and evidence-backed causal edges for the GC mid2 microbial trait. It is designed to support YAML graph assembly by separating stronger mechanistic edges from broader or uncertain associations.*

## 8) Visual evidence (figures/tables)

- **Ku (NHEJ) vs genomic GC content:** Figure panels showing that Ku-encoding microbes tend to have higher genomic GC content, and the phylogenetic distribution of Ku, were extracted from the PLOS Genetics study. (weissman2019linkinghighgc media 6f627d2b)
- **Restriction site GC enrichment:** Figure panels showing higher-GC recognition sequences and elevated GC in flanking bases around AT-rich restriction sites were extracted from the same study. (weissman2019linkinghighgc media 76601217)

## 9) Warnings / claims not yet safe to curate into TraitMech

1) **Do not treat “Ku causes high GC” as settled.** The Ku–GC relationship is robust as an association, but mechanistic directionality (selection for GC to aid repair vs correlated ecology vs recombination/BGC) remains partly speculative in the cited work. Curate as *uncertain* causal or *association* edges unless additional causal evidence is added. (weissman2019linkinghighgc pages 15-17, weissman2019linkinghighgc pages 14-15)

2) **Avoid overgeneralizing taxon-specific mutation spectrum results.** Mutation-spectrum studies in specific organisms/environments (e.g., anaerobic lactic acid bacteria) provide plausible mechanistic nodes (deamination, replication-associated biases) but may not generalize to all GC mid2 taxa. Mark such edges as taxon/context-dependent. (hale2025elevatedratesand pages 14-17)

3) **GC% bin assignment can be technically confounded.** Genome assembly conditions can bias GC% estimates in a direction dependent on true GC%; for metagenome-assembled genomes and short-read assemblies, include quality/coverage metadata where possible. (radai2024anoverlookedphenomenon pages 10-12)

## 10) DOI-first bibliography (with publication dates and URLs)

**Priority recent sources (2023–2024):**
- Rádai Z, et al. *An overlooked phenomenon: complex interactions of potential error sources on the quality of bacterial de novo genome assemblies.* **BMC Genomics** (Jan 2024). DOI: **10.1186/s12864-023-09910-4**. URL: https://doi.org/10.1186/s12864-023-09910-4 (radai2024anoverlookedphenomenon pages 10-12)
- Dagva O, et al. *Correction of non-random mutational biases along a linear bacterial chromosome by the mismatch repair endonuclease NucS.* **Nucleic Acids Research** (Mar 2024). DOI: **10.1093/nar/gkae132**. URL: https://doi.org/10.1093/nar/gkae132 (dagva2024correctionofnonrandom pages 1-2)
- de la Fuente R, et al. *Genomic Signature in Evolutionary Biology: A Review.* **Biology** (Feb 2023). DOI: **10.3390/biology12020322**. URL: https://doi.org/10.3390/biology12020322 (fuente2023genomicsignaturein pages 13-15)

**Foundational, highly relevant sources for mechanisms:**
- Weissman JL, Fagan WF, Johnson PLF. *Linking high GC content to the repair of double strand breaks in prokaryotic genomes.* **PLOS Genetics** (Nov 2019). DOI: **10.1371/journal.pgen.1008493**. URL: https://doi.org/10.1371/journal.pgen.1008493 (weissman2019linkinghighgc pages 15-17)
- Lassalle F, et al. *GC-content evolution in bacterial genomes: the biased gene conversion hypothesis expands.* **bioRxiv** (Nov 2015). DOI: **10.1101/011023**. URL: https://doi.org/10.1101/011023 (lassalle2015gccontentevolutionin pages 1-4)

**Additional supporting context used for bounds/mechanism framing:**
- Radrizzani S, et al. *Bacterial gene 5′ ends have unusual mutation rates that can mislead tests of selection.* **PLOS Biology** (Dec 2025). DOI: **10.1371/journal.pbio.3003569**. URL: https://doi.org/10.1371/journal.pbio.3003569 (radrizzani2025bacterialgene5′ pages 18-21)
- Torrance EL, et al. *Homologous recombination shapes the architecture and evolution of bacterial genomes.* **Nucleic Acids Research** (Dec 2025). DOI: **10.1093/nar/gkae1265**. URL: https://doi.org/10.1093/nar/gkae1265 (torrance2025homologousrecombinationshapes pages 1-4)
- Hale OF, et al. *Elevated rates and biased spectra of mutations in anaerobically cultured lactic acid bacteria.* **mBio** (Dec 2025). DOI: **10.1128/mbio.03054-25**. URL: https://doi.org/10.1128/mbio.03054-25 (hale2025elevatedratesand pages 14-17)
- Deka N, et al. *Base substitutions in genomes due to deamination and oxidation of DNA bases, favoring genome compositional biases.* (Dec 2025). DOI: **10.63635/mrj.v1i4.188**. URL: https://doi.org/10.63635/mrj.v1i4.188 (deka2025basesubstitutionsin pages 1-3)


References

1. (deka2025basesubstitutionsin pages 1-3): Nishita Deka, Pratyush Kumar Beura, Monika Jain, Najima Ahmed, Ramesh Chandra Deka, Siddhartha Shankar Satapathy, and Suvendra Kumar Ray. Base substitutions in genomes due to deamination and oxidation of dna bases, favoring genome compositional biases. Multidisciplinary Research Journal, pages 21-37, Dec 2025. URL: https://doi.org/10.63635/mrj.v1i4.188, doi:10.63635/mrj.v1i4.188. This article has 1 citations.

2. (radrizzani2025bacterialgene5′ pages 18-21): Sofia Radrizzani, Juan Rivas-Santisteban, Namshik Han, and Laurence D. Hurst. Bacterial gene 5′ ends have unusual mutation rates that can mislead tests of selection. PLOS Biology, 23(12):e3003569, Dec 2025. URL: https://doi.org/10.1371/journal.pbio.3003569, doi:10.1371/journal.pbio.3003569. This article has 1 citations and is from a highest quality peer-reviewed journal.

3. (radai2024anoverlookedphenomenon pages 10-12): Zoltán Rádai, Alex Váradi, Péter Takács, Nikoletta Andrea Nagy, Nicholas Schmitt, Eszter Prépost, Gábor Kardos, and Levente Laczkó. An overlooked phenomenon: complex interactions of potential error sources on the quality of bacterial de novo genome assemblies. BMC Genomics, Jan 2024. URL: https://doi.org/10.1186/s12864-023-09910-4, doi:10.1186/s12864-023-09910-4. This article has 3 citations and is from a peer-reviewed journal.

4. (lassalle2015gccontentevolutionin pages 9-11): Florent Lassalle, Séverine Périan, Thomas Bataillon, Xavier Nesme, Laurent Duret, and Vincent Daubin. Gc-content evolution in bacterial genomes: the biased gene conversion hypothesis expands. ArXiv, Nov 2015. URL: https://doi.org/10.1101/011023, doi:10.1101/011023. This article has 271 citations.

5. (lassalle2015gccontentevolutionin pages 1-4): Florent Lassalle, Séverine Périan, Thomas Bataillon, Xavier Nesme, Laurent Duret, and Vincent Daubin. Gc-content evolution in bacterial genomes: the biased gene conversion hypothesis expands. ArXiv, Nov 2015. URL: https://doi.org/10.1101/011023, doi:10.1101/011023. This article has 271 citations.

6. (lassalle2015gccontentevolutionin pages 4-6): Florent Lassalle, Séverine Périan, Thomas Bataillon, Xavier Nesme, Laurent Duret, and Vincent Daubin. Gc-content evolution in bacterial genomes: the biased gene conversion hypothesis expands. ArXiv, Nov 2015. URL: https://doi.org/10.1101/011023, doi:10.1101/011023. This article has 271 citations.

7. (deka2025basesubstitutionsin pages 13-15): Nishita Deka, Pratyush Kumar Beura, Monika Jain, Najima Ahmed, Ramesh Chandra Deka, Siddhartha Shankar Satapathy, and Suvendra Kumar Ray. Base substitutions in genomes due to deamination and oxidation of dna bases, favoring genome compositional biases. Multidisciplinary Research Journal, pages 21-37, Dec 2025. URL: https://doi.org/10.63635/mrj.v1i4.188, doi:10.63635/mrj.v1i4.188. This article has 1 citations.

8. (weissman2019linkinghighgc pages 15-17): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. PLOS Genetics, 15:e1008493, Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.

9. (weissman2019linkinghighgc pages 5-6): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. PLOS Genetics, 15:e1008493, Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.

10. (weissman2019linkinghighgc pages 14-15): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. PLOS Genetics, 15:e1008493, Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.

11. (dagva2024correctionofnonrandom pages 1-2): Oyut Dagva, Annabelle Thibessard, Jean-Noël Lorenzi, Victor Labat, Emilie Piotrowski, Nicolas Rouhier, Hannu Myllykallio, Pierre Leblond, and Claire Bertrand. Correction of non-random mutational biases along a linear bacterial chromosome by the mismatch repair endonuclease nucs. Nucleic Acids Research, 52:5033-5047, Mar 2024. URL: https://doi.org/10.1093/nar/gkae132, doi:10.1093/nar/gkae132. This article has 7 citations and is from a highest quality peer-reviewed journal.

12. (dagva2024correctionofnonrandom pages 12-13): Oyut Dagva, Annabelle Thibessard, Jean-Noël Lorenzi, Victor Labat, Emilie Piotrowski, Nicolas Rouhier, Hannu Myllykallio, Pierre Leblond, and Claire Bertrand. Correction of non-random mutational biases along a linear bacterial chromosome by the mismatch repair endonuclease nucs. Nucleic Acids Research, 52:5033-5047, Mar 2024. URL: https://doi.org/10.1093/nar/gkae132, doi:10.1093/nar/gkae132. This article has 7 citations and is from a highest quality peer-reviewed journal.

13. (fuente2023genomicsignaturein pages 13-15): Rebeca de la Fuente, Wladimiro Díaz-Villanueva, Vicente Arnau, and Andrés Moya. Genomic signature in evolutionary biology: a review. Biology, 12:322, Feb 2023. URL: https://doi.org/10.3390/biology12020322, doi:10.3390/biology12020322. This article has 31 citations.

14. (weissman2019linkinghighgc pages 10-11): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. PLOS Genetics, 15:e1008493, Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.

15. (torrance2025homologousrecombinationshapes pages 1-4): Ellis L. Torrance, Awa Diop, and Louis-Marie Bobay. Homologous recombination shapes the architecture and evolution of bacterial genomes. Nucleic Acids Research, Dec 2025. URL: https://doi.org/10.1093/nar/gkae1265, doi:10.1093/nar/gkae1265. This article has 13 citations and is from a highest quality peer-reviewed journal.

16. (deka2025basesubstitutionsin pages 3-5): Nishita Deka, Pratyush Kumar Beura, Monika Jain, Najima Ahmed, Ramesh Chandra Deka, Siddhartha Shankar Satapathy, and Suvendra Kumar Ray. Base substitutions in genomes due to deamination and oxidation of dna bases, favoring genome compositional biases. Multidisciplinary Research Journal, pages 21-37, Dec 2025. URL: https://doi.org/10.63635/mrj.v1i4.188, doi:10.63635/mrj.v1i4.188. This article has 1 citations.

17. (hale2025elevatedratesand pages 14-17): Owen F. Hale, Michelle Yin, and Megan G. Behringer. Elevated rates and biased spectra of mutations in anaerobically cultured lactic acid bacteria. mBio, Dec 2025. URL: https://doi.org/10.1128/mbio.03054-25, doi:10.1128/mbio.03054-25. This article has 0 citations and is from a domain leading peer-reviewed journal.

18. (weissman2019linkinghighgc pages 21-24): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. PLOS Genetics, 15:e1008493, Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.

19. (weissman2019linkinghighgc media 6f627d2b): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. PLOS Genetics, 15:e1008493, Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.

20. (weissman2019linkinghighgc media 76601217): JL Weissman, William F. Fagan, and Philip L. F. Johnson. Linking high gc content to the repair of double strand breaks in prokaryotic genomes. PLOS Genetics, 15:e1008493, Nov 2019. URL: https://doi.org/10.1371/journal.pgen.1008493, doi:10.1371/journal.pgen.1008493. This article has 74 citations and is from a domain leading peer-reviewed journal.