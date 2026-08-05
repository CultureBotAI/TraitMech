---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:51:37.624424'
end_time: '2026-08-04T04:59:28.615838'
duration_seconds: 470.99
template_file: templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'gc_skew_replication_strand_asymmetry: 9 nodes, 8 edges'
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
- **Trait label:** GC skew
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000097
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genome-sequence property describing strand asymmetry in guanine versus cytosine content between the leading and lagging replication strands, commonly used to locate the replication origin and terminus.
- **Parent traits:** METPO:1000188
- **Synonyms:** strand compositional asymmetry
- **Existing evidence:** DOI:10.1093/oxfordjournals.molbev.a025626:  (Lobry first described asymmetric substitution patterns between the two DNA strands of bacteria, the basis of GC skew that marks replication boundaries.) | DOI:10.1016/S0378-1119(99)00297-8:  (Frank & Lobry review the mutational and selective mechanisms underlying strand compositional asymmetry.)
- **Existing causal graph summary:** gc_skew_replication_strand_asymmetry: 9 nodes, 8 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000097
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genome-sequence property describing strand asymmetry in guanine versus cytosine content between the leading and lagging replication strands, commonly used to locate the replication origin and terminus.
- **Parent traits:** METPO:1000188
- **Synonyms:** strand compositional asymmetry
- **Existing evidence:** DOI:10.1093/oxfordjournals.molbev.a025626:  (Lobry first described asymmetric substitution patterns between the two DNA strands of bacteria, the basis of GC skew that marks replication boundaries.) | DOI:10.1016/S0378-1119(99)00297-8:  (Frank & Lobry review the mutational and selective mechanisms underlying strand compositional asymmetry.)
- **Existing causal graph summary:** gc_skew_replication_strand_asymmetry: 9 nodes, 8 edges

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


# Curation-focused research report: GC skew

## Trait record and scope

- **Trait label:** GC skew
- **Trait identifier:** `traitmech:000097`
- **Category / kind / status:** GENOMICS / CLASS / REVIEWED
- **Parent:** `METPO:1000188`
- **Recommended operational definition:** a sequence-derived measure of within-strand G-versus-C asymmetry, ordinarily calculated in a window as **(G−C)/(G+C)**. In canonical circular bacterial chromosomes, replication-associated GC skew has opposite signs in the two replichores and changes sign near the replication origin and terminus; cumulative GC skew is the running sum used to make these transitions visible. (tillier2000thecontributionsof pages 1-2, arakawa2012measuresofcompositional pages 1-2, arakawa2012measuresofcompositional pages 2-3)

This is an **assay-observed genomic property and long-term evolutionary footprint**, not a physiological capacity, metabolic pathway, or immediate readout of replication activity. It integrates mutation, repair, selection, transcription, sequence acquisition, and genome rearrangement over evolutionary time. A strong skew supports replication-associated strand asymmetry, but its absence does not establish absence of replication or of a conventional origin. (arakawa2012measuresofcompositional pages 4-5, arakawa2012measuresofcompositional pages 1-2)

### Boundaries and nearby traits

1. **GC content is not GC skew.** GC content is (G+C)/total bases; GC skew compares G with C on one represented strand. A genome can have high GC content and little skew, or low GC content and marked skew. (tillier2000thecontributionsof pages 1-2)
2. **AT skew is separate:** (A−T)/(A+T). It may complement GC skew, especially in AT-rich taxa, but should not be merged into this trait. (tillier2000thecontributionsof pages 1-2, arakawa2012measuresofcompositional pages 3-4)
3. **Cumulative GC skew is an analytical transformation**, not a separate molecular mechanism. Its extrema or slope reversals are used to nominate ori/ter regions. (arakawa2012measuresofcompositional pages 1-2, arakawa2012measuresofcompositional pages 2-3)
4. **Gene strand bias (GSB) is distinct.** GSB measures the fraction or arrangement of genes on leading versus lagging strands. It can correlate with GC skew because both depend on replication orientation, but GSB is shaped strongly by selection against head-on transcription–replication collisions. (tomasch2024ontheevolution pages 2-5, tomasch2024ontheevolution pages 1-2)
5. **Transcription-associated compositional skew is a contributor/confounder**, not equivalent to replication-associated GC skew. Transcription direction, single-strand exposure, transcription-coupled repair, and codon-related selection can augment or oppose the replication signal. (tillier2000thecontributionsof pages 1-2, guo2011strandspecificcompositionbias pages 16-18)
6. **Local high nucleotide skew at an origin sequence is not necessarily chromosome-scale GC skew.** Recent work considers GC, purine/pyrimidine, and amino/keto skews in short palindromic origin segments and their melting kinetics. This is mechanistically interesting but should remain an adjacent, uncertain concept. (sahu2024highnucleotideskew pages 17-18, sahu2024highnucleotideskew pages 1-3)

## Current mechanistic model

Bidirectional replication partitions a circular chromosome into oppositely polarized replichores. Continuous and discontinuous synthesis, unequal single-stranded exposure, polymerase-associated errors, and strand-dependent repair generate different substitution spectra on the two strands. Over evolutionary time, this can enrich G relative to C on the represented leading strand and reverse the pattern on the opposite replichore. The origin and terminus therefore delimit regions of opposite skew. (arakawa2012measuresofcompositional pages 1-2, arakawa2012measuresofcompositional pages 2-3, guo2011strandspecificcompositionbias pages 1-3)

A frequently invoked chemical route is prolonged single-stranded exposure followed by cytosine deamination. One review reports cytosine deamination as approximately **140-fold more frequent in single-stranded than double-stranded DNA**, linking exposure to excess C→T substitutions and ultimately G/C asymmetry. This is a plausible major route, not a universal single-cause explanation: bacterial clades show different mutation spectra, and deamination alone is insufficient to account for all observed patterns. (arakawa2012measuresofcompositional pages 4-5, guo2011strandspecificcompositionbias pages 8-11)

The strongest direct experimental support comes from accelerated evolution in *Escherichia coli*. Cytosine-deaminase mutagenesis over **more than 500 generations** reproduced replication-oriented substitution asymmetry. Deleting `tus`, which encodes a replication-fork barrier protein, markedly reduced/altered terminal-region strand bias, whereas deletion of `dif` did not reproduce that effect. This supports replication and termination architecture, rather than cell division per se, as the proximate cause in that system. (kono2018acceleratedlaboratoryevolution pages 6-8)

## Candidate nodes grouped by type

### Trait and assay nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| GC skew | `traitmech:000097` | Target trait; retain identifier verbatim. |
| strand compositional asymmetry | label only | Synonym/broader descriptive node. |
| windowed GC-skew assay | label only | Formula `(G−C)/(G+C)`; record window size and strand convention. |
| cumulative GC-skew analysis | label only | Analytical transformation; not a biological process. |
| GC Skew Index | label only | Composite statistical measure; reported threshold GCSI >0.05 for bidirectional strand bias, but method-specific. (arakawa2012measuresofcompositional pages 4-5) |
| AT skew | label only | Adjacent assay; do not merge with target. |
| gene strand bias | label only | Adjacent genomic trait, not GC skew. |

### Replication structures and processes

| Candidate node | Suggested CURIE | Note |
|---|---|---|
| DNA replication | `GO:0006260` | High-confidence broad process. |
| DNA replication initiation | `GO:0006270` | Broader than bacterial oriC initiation. |
| replication origin / oriC | label only unless a verified sequence-ontology term is adopted | Genomic locus, not a protein. |
| replication terminus / ter region | label only | Avoid equating ter, Tus-binding sites, `dif`, and the observed fork-fusion point. |
| leading-strand synthesis | `GO:0006272` | Verify ontology release during implementation. |
| lagging-strand synthesis | `GO:0006273` | Verify ontology release during implementation. |
| DNA replication fork | `GO:0005657` | Cellular component/localization candidate. |
| replichore | label only | Chromosomal region with one replication polarity. |
| Okazaki fragment | label only | Product of discontinuous synthesis; avoid unsupported direct edge to GC skew. |
| replication termination | label only | Specific process grounding should be verified. |

### Molecular events and chemicals

| Candidate node | Suggested CURIE | Note |
|---|---|---|
| single-stranded DNA | `CHEBI:9160` | Verify exact ChEBI label/version before YAML insertion. |
| cytosine | `CHEBI:16040` | Substrate in spontaneous deamination model. |
| uracil | `CHEBI:17568` | Immediate deamination product; mechanistic intermediate. |
| cytosine deamination | label only | Molecular reaction; do not assign an EC because the proposed event may be spontaneous or experimentally enzyme-driven. |
| C→T substitution | label only | Evolutionary sequence event. |
| strand-asymmetric substitution pressure | label only | Aggregate mutational process directly upstream of trait. |
| DNA repair | `GO:0006281` | Broad modifier; specific strand-direction edges need stronger evidence. |
| mismatch repair | `GO:0006298` | Candidate modifier, not yet a core causal node. |

### Genes, proteins, and sites

| Candidate node | Grounding | Note |
|---|---|---|
| Tus replication termination protein | label plus taxon-specific UniProt accession after strain selection | Direct experimental edge is *E. coli*-specific. |
| `tus` gene | label only pending strain-specific locus grounding | Experimental-factor node. |
| Ter/Tus fork trap | label only | Distinct from broad terminus region. |
| `dif` chromosome-dimer resolution site | label only | Correlates with skew shift points but is not necessarily the physical termination site. |
| XerC/XerD recombinases | label; add strain-specific UniProt only if needed | Relevant to `dif`, not established as GC-skew generators. |
| cytosine deaminase mutator | label only | Experimental perturbation, not necessarily the endogenous cause of natural GC skew. |

### Selection, genome organization, and confounders

| Candidate node | Suggested grounding | Note |
|---|---|---|
| transcription–replication conflict | `GO:0090543` if confirmed in current GO release | Adjacent mechanism affecting GSB and mutation; not a direct universal cause of GC skew. |
| leading-strand gene placement | label only | Selection-linked genome organization. |
| horizontal gene transfer | `GO:0044038` | Can introduce compositionally atypical segments and distort local skew. |
| chromosomal inversion | label only | Can reverse inherited local skew and generate pseudo-shift points. |
| genomic island | `SO:0000771` if confirmed | Application/confounder node rather than causal generator. |
| circular bacterial chromosome | label only | Primary scope context. |
| Bacteria | `NCBITaxon:2` | Main taxonomic scope; plasmids, archaea, viruses, and organelles need separate qualification. |
| *Escherichia coli* | `NCBITaxon:562` | Scope for direct `tus` perturbation evidence. |

## Candidate causal edges

The following compact table separates core relations from adjacent or uncertain claims.

| subject | predicate | object | evidence class | taxon/scope | DOI | curator decision |
|---|---|---|---|---|---|---|
| bidirectional chromosome replication polarity | establishes | leading strand state / lagging strand state | review / mechanistic synthesis | bacteria, especially circular chromosomes | 10.2174/138920212799034749 | curate |
| leading-strand template prolonged single-stranded exposure | increases | cytosine deamination | review with quantitative prior evidence | bacteria | 10.5772/18554 | curate |
| cytosine deamination | causes | C-to-T substitution bias | review + experimental support | bacteria; experimentally reinforced in *Escherichia coli* | 10.5772/18554, 10.1093/gbe/evy237 | curate |
| asymmetric C↔G / C→T substitution pressure between replichores | causes | GC skew | review / comparative genomics / experimental support | bacteria | 10.1007/s002399910029, 10.2174/138920212799034749, 10.1093/gbe/evy237 | curate |
| replication origin and replication terminus boundaries | correspond to | GC-skew sign switch / cumulative GC-skew extrema | review / computationally robust | bacteria | 10.2174/138920212799034749, 10.5772/18554 | curate |
| tus deletion | reduces | terminal-region strand bias / terminal GC-skew structure | direct experiment | *Escherichia coli* | 10.1093/gbe/evy237 | curate as taxon-specific / experimental-factor edge |
| transcription-replication conflicts | selects for | leading-strand gene placement / gene strand bias | recent comparative genomics, mechanistically plausible | bacteria; strong examples in Gemmatimonadota and Bacillota | 10.1128/mbio.00602-24 | do not curate into GC-skew core graph; curate only as adjacent trait link |
| horizontal gene transfer or chromosomal inversions | disrupt | local GC-skew pattern / introduce pseudo-shift points | review / computational caution | bacteria | 10.2174/138920212799034749, 10.1101/gr.5525106 | curate as confounder / warning edge |
| high-skew palindromic origin-like sequence | lowers | local DNA melting / unzipping barrier | recent computational / biophysical inference | bacteria, archaea, plasmids, mitochondria | 10.1007/s00239-024-10202-y | uncertain; hold for later curation |
| dif site position | correlates with | GC-skew shift point | computational association | 641 bacterial genomes, 16 phyla | 10.1186/1471-2164-12-19 | do not treat as causal; annotation/validation use only |
| gene strand bias peaks | co-localize with | GC-skew peaks in some chromosomes | recent comparative association | selected bacterial clades | 10.1128/mbio.00602-24 | uncertain / clade-specific; not core GC-skew mechanism |
| cumulative GC skew and nucleotide compositional anomalies | help identify | genomic islands / foreign DNA segments | applied genomics association | bacterial genome analysis | 10.3390/foods13071082 | application only; not a causal edge |


*Table: This table summarizes compact candidate causal and adjacent edges for curating the GC skew trait graph, with evidence class, scope, DOI, and suggested curator action. It separates core mechanistic edges from confounders, applications, and recent but still-uncertain hypotheses.*

### Edge-level evidence with supporting snippets

| Subject–predicate–object triple | Reference | Supporting snippet | Interpretation and curation status |
|---|---|---|---|
| **Bidirectional replication — establishes — oppositely polarized replichores** | DOI [10.2174/138920212799034749](https://doi.org/10.2174/138920212799034749), March 2012 | “two replichores with opposite polarity” and GC-skew graphs change sign at their junctions | **Curate.** Foundational architecture connecting replication to strand labels. (arakawa2012measuresofcompositional pages 1-2, arakawa2012measuresofcompositional pages 2-3) |
| **Leading-strand-associated ssDNA exposure — increases — cytosine deamination** | DOI [10.5772/18554](https://doi.org/10.5772/18554), August 2011 | leading strand is “exposed longer in single-stranded state”; deamination is reported as “140× more frequent in single-stranded DNA” | **Curate with mechanism qualifier.** Review-level synthesis; orientation terminology can vary with whether template or newly synthesized strand is being named, so YAML notes must state the strand convention. (guo2011strandspecificcompositionbias pages 8-11) |
| **Cytosine deamination — increases — C→T substitutions** | DOI [10.5772/18554](https://doi.org/10.5772/18554), August 2011; DOI [10.1093/gbe/evy237](https://doi.org/10.1093/gbe/evy237), October 2018 | deamination “leads to C→T mutations”; accelerated evolution quantified substitutions induced by cytosine deamination | **Curate.** Chemical edge is strong; natural effect size remains taxon-dependent. (guo2011strandspecificcompositionbias pages 8-11, kono2018acceleratedlaboratoryevolution pages 6-8) |
| **Strand-asymmetric substitution pressure — causes — GC skew** | DOI [10.1007/s002399910029](https://doi.org/10.1007/s002399910029), March 2000; DOI [10.1093/gbe/evy237](https://doi.org/10.1093/gbe/evy237), October 2018 | replication-associated mutations affect leading and lagging synthesis asymmetrically; laboratory evolution “demonstrat[ed] replication machinery’s causal role” | **Curate as the central edge.** This is better supported and more general than assigning GC skew solely to deamination. (tillier2000thecontributionsof pages 1-2, kono2018acceleratedlaboratoryevolution pages 6-8) |
| **Replication origin/terminus boundaries — produce/correspond to — GC-skew sign switches** | DOI [10.2174/138920212799034749](https://doi.org/10.2174/138920212799034749), March 2012 | graphs “shifting sign at replication origin and terminus junctions” | **Curate**, but predicate should distinguish biological generation from observational correspondence. For a conservative ontology graph, use `associated_with` or `determines_spatial_boundary_of`. (arakawa2012measuresofcompositional pages 1-2, arakawa2012measuresofcompositional pages 2-3) |
| **`tus` deletion — reduces/alters — terminal-region strand bias** | DOI [10.1093/gbe/evy237](https://doi.org/10.1093/gbe/evy237), October 2018 | deletion “drastically altered GC skew in terminal regions by reducing mutation bias” | **Curate as direct experimental, taxon-specific evidence** for *E. coli*. Do not generalize Tus to bacteria lacking the Tus–Ter system. (kono2018acceleratedlaboratoryevolution pages 6-8) |
| **`dif` deletion — does not materially alter — replication-driven substitution pattern** | DOI [10.1093/gbe/evy237](https://doi.org/10.1093/gbe/evy237), October 2018 | `dif` deletion showed “similar substitution patterns to wild-type” | **Useful negative/control edge**, but only if TraitMech supports negated relations. Otherwise retain in evidence notes. (kono2018acceleratedlaboratoryevolution pages 6-8) |
| **`dif` position — correlates with — GC-skew shift point** | DOI [10.1186/1471-2164-12-19](https://doi.org/10.1186/1471-2164-12-19), January 2011 | identified in **641 organisms across 16 phyla**, with **97.64%** identification in single-chromosome strains; positions strongly correlated with skew shift points | **Do not encode as causal.** The same study warns termination does not occur strictly at `dif`; in *E. coli*, fork arrest occurs at Tus sites. (kono2011comprehensivepredictionof pages 1-2) |
| **Transcription–replication conflict — selects for — leading-strand placement of highly expressed/essential genes** | DOI [10.1128/mbio.00602-24](https://doi.org/10.1128/mbio.00602-24), June 2024 | head-on collisions cause transcription slowdown and detrimental mutations; a **600-kb** region near ter contains almost all genes on leading strands | **Adjacent graph only.** This is a GSB mechanism, not sufficient evidence for a direct conflict→GC-skew edge. (tomasch2024ontheevolution pages 1-2) |
| **Transcription orientation — modifies — replication-associated composition asymmetry** | DOI [10.1007/s002399910029](https://doi.org/10.1007/s002399910029), March 2000; DOI [10.5772/18554](https://doi.org/10.5772/18554), August 2011 | transcription effects can “increase or decrease replication-associated strand asymmetries” | **Curate as modifier/confounder**, not as a universal directionally signed edge. (tillier2000thecontributionsof pages 1-2, guo2011strandspecificcompositionbias pages 16-18) |
| **Horizontal transfer/inversion — disrupts — local GC-skew continuity** | DOI [10.2174/138920212799034749](https://doi.org/10.2174/138920212799034749), March 2012 | weak bias, inversions, and horizontal transfer can introduce “pseudo-shift points” | **Curate as a confounder edge.** It supports interpretation and QC rather than trait generation. (arakawa2012measuresofcompositional pages 4-5) |
| **High-skew palindromic sequence — lowers — local DNA-unzipping barrier** | DOI [10.1007/s00239-024-10202-y](https://doi.org/10.1007/s00239-024-10202-y), September 2024 | high-skew RY/MK palindromes had “lower kinetic barriers” and faster local unzipping near melting temperature | **Uncertain/hold.** Recent model-based biophysical inference; it concerns local origin sequence properties and should not be merged with chromosome-scale GC skew without an explicit bridge. (sahu2024highnucleotideskew pages 17-18, sahu2024highnucleotideskew pages 1-3) |

## Recent developments, applications, and quantitative evidence

### 2024 research

**Origin-sequence biophysics.** Sahu and colleagues modeled direction-dependent DNA unzipping and analyzed **227,532 bacterial origin sequences** from DoriC, with mean length **413 nt**, together with 801 archaeal, 851 plasmid, and 5,686 mitochondrial origins. High-skew palindromes showed lower kinetic barriers to local melting. This is an important mechanistic hypothesis for why skewed sequence organization can occur at origins, but it does not prove that chromosome-scale GC skew causes origin firing. (sahu2024highnucleotideskew pages 17-18, sahu2024highnucleotideskew pages 1-3)

**Chromosome architecture and GSB.** Tomasch and colleagues reported bacterial gene strand preference ranging from about **50% to 85%** across phyla. In Gemmatimonadota, they found a conserved approximately **600-kb** high-strand-bias region around ter containing rRNA clusters and highly expressed/core genes. Their analysis used five closed genomes and 61 curated MAGs; *Bacillus subtilis* had **78% of windows with strand-bias score >0.9**, whereas *E. coli* had nearly none. This demonstrates that GC-skew-aligned genome organization is heterogeneous and that nucleoid organization and evolutionary history may add to replication-related effects. (tomasch2024ontheevolution pages 2-5, tomasch2024ontheevolution pages 1-2)

### Current applications

1. **oriC and terminus nomination.** Sign changes in windowed skew and extrema in cumulative skew remain widely used to identify candidate replication boundaries. Predictions are strongest when combined with origin-associated genes/motifs, synteny, DnaA-box evidence, and experimental origin databases. (arakawa2012measuresofcompositional pages 1-2, arakawa2012measuresofcompositional pages 2-3)
2. **Replichore assignment.** Once ori/ter are nominated, GC skew helps assign leading and lagging replichores for studying mutation, codon usage, and gene orientation. (guo2011strandspecificcompositionbias pages 16-18, guo2011strandspecificcompositionbias pages 1-3)
3. **Termination-region annotation.** GC-skew shift points can help localize `dif` and terminus neighborhoods, but `dif` must not be treated as the exact fork-fusion site. The 641-genome study’s 97.64% `dif` identification rate illustrates utility while explicitly rejecting strict equivalence. (kono2011comprehensivepredictionof pages 1-2)
4. **Genome assembly and annotation QC.** Unexpected additional sign switches, broken cumulative trajectories, or displaced ori/ter can flag inversions, rearrangements, horizontally acquired sequence, incorrect circularization, or assembly problems. This is a diagnostic clue rather than proof because genuine biology can produce the same signatures. (arakawa2012measuresofcompositional pages 4-5)
5. **Comparative and evolutionary genomics.** Quantitative measures such as ΔGC skew, GCSI, Fourier/wavelet analyses, and strand-bias statistics compare replication-linked asymmetry among taxa. A reported **GCSI >0.05** indicates detectable bidirectional strand bias in that method, but it is not a universal biological threshold. (arakawa2012measuresofcompositional pages 4-5, arakawa2012measuresofcompositional pages 3-4)
6. **Genomic-island screening.** Local departures in cumulative skew can complement GC%, codon usage, and mobility-gene evidence to identify foreign regions. GC skew alone is not sufficiently specific. (arakawa2012measuresofcompositional pages 4-5)

## Expert synthesis for `gc_skew.yaml`

The most defensible core graph is:

**bidirectional chromosome replication → opposite replichore polarity → strand-differential ssDNA exposure/error/repair → asymmetric substitution spectrum → G-versus-C compositional asymmetry → `traitmech:000097`**, with **ori/ter boundaries → spatial sign transition**.

This formulation reflects the expert consensus that GC skew is a composite evolutionary outcome. It avoids overcommitting to cytosine deamination as the sole mechanism and keeps selection, transcription, HGT, inversions, and termination-system differences as modifiers. Experimental *E. coli* evidence supports replication causality, while broad comparative work establishes that the exact mutation spectrum and skew strength vary among clades. (arakawa2012measuresofcompositional pages 4-5, arakawa2012measuresofcompositional pages 1-2, kono2018acceleratedlaboratoryevolution pages 6-8)

## Warnings: claims not yet ready for TraitMech curation

- **Do not curate “cytosine deamination is the universal cause of GC skew.”** It is plausible and experimentally tractable, but clade-specific mutation and repair spectra show that no single mechanism explains every genome. (arakawa2012measuresofcompositional pages 4-5)
- **Do not equate skew extrema with experimentally verified oriC/ter.** Weak skew, multiple origins, linear replicons, recombination-dependent replication, inversion, HGT, and assembly error can shift or multiply extrema. (arakawa2012measuresofcompositional pages 4-5)
- **Do not equate `dif` with the precise replication-termination site.** Positional correlation is strong, but termination can occur at Tus–Ter fork traps and varies by taxon. (kono2011comprehensivepredictionof pages 1-2)
- **Do not merge gene strand bias into GC skew.** Their locations can correlate, but their measurements and proximal causes differ. (tomasch2024ontheevolution pages 2-5, tomasch2024ontheevolution pages 1-2)
- **Do not curate a direct high-skew-palindrome→genome-wide-GC-skew edge.** The 2024 result is computational/biophysical and addresses local origin melting. (sahu2024highnucleotideskew pages 17-18, sahu2024highnucleotideskew pages 1-3)
- **Do not assign universal directionality without recording strand convention.** “Leading strand” can refer to template, daughter strand, or the reference sequence copied continuously; inconsistent conventions can reverse an apparently causal statement.
- **Do not treat GCSI >0.05 as a universal phenotype cutoff.** It is a method-specific statistical threshold. (arakawa2012measuresofcompositional pages 4-5)
- **Avoid unverified CURIEs.** Confirm every GO/CHEBI/SO identifier against the ontology release used by the repository; use label-only nodes where grounding remains ambiguous.

## DOI-first bibliography

1. Sahu P, Barik S, Ghosh K, Subramanian H. “High Nucleotide Skew Palindromic DNA Sequences Function as Potential Replication Origins due to their Unzipping Propensity.” *Journal of Molecular Evolution*. Published September 2024. DOI: [10.1007/s00239-024-10202-y](https://doi.org/10.1007/s00239-024-10202-y). (sahu2024highnucleotideskew pages 17-18)
2. Tomasch J, et al. “On the evolution of chromosomal regions with high gene strand bias in bacteria.” *mBio* 15. Published June 2024. DOI: [10.1128/mbio.00602-24](https://doi.org/10.1128/mbio.00602-24). (tomasch2024ontheevolution pages 2-5, tomasch2024ontheevolution pages 1-2)
3. Kono N, Tomita M, Arakawa K. “Accelerated Laboratory Evolution Reveals the Influence of Replication on the GC Skew in *Escherichia coli*.” *Genome Biology and Evolution* 10:3110–3117. Published October 2018. DOI: [10.1093/gbe/evy237](https://doi.org/10.1093/gbe/evy237). (kono2018acceleratedlaboratoryevolution pages 6-8)
4. Arakawa K, Tomita M. “Measures of Compositional Strand Bias Related to Replication Machinery and its Applications.” *Current Genomics* 13:4–15. Published March 2012. DOI: [10.2174/138920212799034749](https://doi.org/10.2174/138920212799034749). (arakawa2012measuresofcompositional pages 4-5, arakawa2012measuresofcompositional pages 1-2)
5. Kono N, Arakawa K, Tomita M. “Comprehensive prediction of chromosome dimer resolution sites in bacterial genomes.” *BMC Genomics* 12:19. Published January 2011. DOI: [10.1186/1471-2164-12-19](https://doi.org/10.1186/1471-2164-12-19). (kono2011comprehensivepredictionof pages 1-2)
6. Guo F-B, Ning L-W. “Strand-specific Composition Bias in Bacterial Genomes.” Published August 2011. DOI: [10.5772/18554](https://doi.org/10.5772/18554). (guo2011strandspecificcompositionbias pages 16-18, guo2011strandspecificcompositionbias pages 8-11)
7. Rocha EPC, Touchon M, Feil EJ. “Similar compositional biases are caused by very different mutational effects.” *Genome Research* 16:1537–1547. Published December 2006. DOI: [10.1101/gr.5525106](https://doi.org/10.1101/gr.5525106).
8. Tillier ERM, Collins RA. “The Contributions of Replication Orientation, Gene Direction, and Signal Sequences to Base-Composition Asymmetries in Bacterial Genomes.” *Journal of Molecular Evolution* 50:249–257. Published March 2000. DOI: [10.1007/s002399910029](https://doi.org/10.1007/s002399910029). (tillier2000thecontributionsof pages 1-2)
9. Mrázek J, Karlin S. “Strand compositional asymmetry in bacterial and large viral genomes.” *PNAS* 95:3720–3725. Published March 1998. DOI: [10.1073/pnas.95.7.3720](https://doi.org/10.1073/pnas.95.7.3720).
10. Frank AC, Lobry JR. “Asymmetric substitution patterns: a review of possible underlying mutational or selective mechanisms.” *Gene* 238:65–77. Published September 1999. DOI: [10.1016/S0378-1119(99)00297-8](https://doi.org/10.1016/S0378-1119(99)00297-8).

**Recommended curation decision:** retain the existing replication-strand-asymmetry graph as the core, add explicit intermediate nodes for strand-differential ssDNA exposure and asymmetric substitution pressure, add the *E. coli* `tus` perturbation as taxon-specific experimental support, encode HGT/inversion and transcription as modifiers, and keep GSB, `dif`, and local high-skew-origin melting outside the core causal chain.

References

1. (tillier2000thecontributionsof pages 1-2): Elisabeth R.M. Tillier and Richard A. Collins. The contributions of replication orientation, gene direction, and signal sequences to base-composition asymmetries in bacterial genomes. Journal of Molecular Evolution, 50:249-257, Mar 2000. URL: https://doi.org/10.1007/s002399910029, doi:10.1007/s002399910029. This article has 223 citations and is from a peer-reviewed journal.

2. (arakawa2012measuresofcompositional pages 1-2): Kazuharu Arakawa and Masaru Tomita. Measures of compositional strand bias related to replication machinery and its applications. Current Genomics, 13:4-15, Mar 2012. URL: https://doi.org/10.2174/138920212799034749, doi:10.2174/138920212799034749. This article has 23 citations and is from a peer-reviewed journal.

3. (arakawa2012measuresofcompositional pages 2-3): Kazuharu Arakawa and Masaru Tomita. Measures of compositional strand bias related to replication machinery and its applications. Current Genomics, 13:4-15, Mar 2012. URL: https://doi.org/10.2174/138920212799034749, doi:10.2174/138920212799034749. This article has 23 citations and is from a peer-reviewed journal.

4. (arakawa2012measuresofcompositional pages 4-5): Kazuharu Arakawa and Masaru Tomita. Measures of compositional strand bias related to replication machinery and its applications. Current Genomics, 13:4-15, Mar 2012. URL: https://doi.org/10.2174/138920212799034749, doi:10.2174/138920212799034749. This article has 23 citations and is from a peer-reviewed journal.

5. (arakawa2012measuresofcompositional pages 3-4): Kazuharu Arakawa and Masaru Tomita. Measures of compositional strand bias related to replication machinery and its applications. Current Genomics, 13:4-15, Mar 2012. URL: https://doi.org/10.2174/138920212799034749, doi:10.2174/138920212799034749. This article has 23 citations and is from a peer-reviewed journal.

6. (tomasch2024ontheevolution pages 2-5): Jürgen Tomasch, Karel Kopejtka, Sahana Shivaramu, Izabela Mujakić, and Michal Koblížek. On the evolution of chromosomal regions with high gene strand bias in bacteria. Jun 2024. URL: https://doi.org/10.1128/mbio.00602-24, doi:10.1128/mbio.00602-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

7. (tomasch2024ontheevolution pages 1-2): Jürgen Tomasch, Karel Kopejtka, Sahana Shivaramu, Izabela Mujakić, and Michal Koblížek. On the evolution of chromosomal regions with high gene strand bias in bacteria. Jun 2024. URL: https://doi.org/10.1128/mbio.00602-24, doi:10.1128/mbio.00602-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

8. (guo2011strandspecificcompositionbias pages 16-18): Feng-Biao Guo and Lu-Wen Ning. Strand-specific composition bias in bacterial genomes. ArXiv, Aug 2011. URL: https://doi.org/10.5772/18554, doi:10.5772/18554. This article has 8 citations.

9. (sahu2024highnucleotideskew pages 17-18): Parthasarathi Sahu, Sashikanta Barik, Koushik Ghosh, and Hemachander Subramanian. High nucleotide skew palindromic dna sequences function as potential replication origins due to their unzipping propensity. Sep 2024. URL: https://doi.org/10.1007/s00239-024-10202-y, doi:10.1007/s00239-024-10202-y. This article has 5 citations and is from a peer-reviewed journal.

10. (sahu2024highnucleotideskew pages 1-3): Parthasarathi Sahu, Sashikanta Barik, Koushik Ghosh, and Hemachander Subramanian. High nucleotide skew palindromic dna sequences function as potential replication origins due to their unzipping propensity. Sep 2024. URL: https://doi.org/10.1007/s00239-024-10202-y, doi:10.1007/s00239-024-10202-y. This article has 5 citations and is from a peer-reviewed journal.

11. (guo2011strandspecificcompositionbias pages 1-3): Feng-Biao Guo and Lu-Wen Ning. Strand-specific composition bias in bacterial genomes. ArXiv, Aug 2011. URL: https://doi.org/10.5772/18554, doi:10.5772/18554. This article has 8 citations.

12. (guo2011strandspecificcompositionbias pages 8-11): Feng-Biao Guo and Lu-Wen Ning. Strand-specific composition bias in bacterial genomes. ArXiv, Aug 2011. URL: https://doi.org/10.5772/18554, doi:10.5772/18554. This article has 8 citations.

13. (kono2018acceleratedlaboratoryevolution pages 6-8): Nobuaki Kono, Masaru Tomita, and Kazuharu Arakawa. Accelerated laboratory evolution reveals the influence of replication on the gc skew in escherichia coli. Genome Biology and Evolution, 10:3110-3117, Oct 2018. URL: https://doi.org/10.1093/gbe/evy237, doi:10.1093/gbe/evy237. This article has 27 citations and is from a domain leading peer-reviewed journal.

14. (kono2011comprehensivepredictionof pages 1-2): Nobuaki Kono, Kazuharu Arakawa, and Masaru Tomita. Comprehensive prediction of chromosome dimer resolution sites in bacterial genomes. BMC Genomics, 12:19-19, Jan 2011. URL: https://doi.org/10.1186/1471-2164-12-19, doi:10.1186/1471-2164-12-19. This article has 93 citations and is from a peer-reviewed journal.