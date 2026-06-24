---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:01:03.006006'
end_time: '2026-06-18T03:19:32.812590'
duration_seconds: 1109.81
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
  causal_graph_summary: 'gc_high_low_gc_bin: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC high
- **METPO identifier:** METPO:1000432
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition at or below approximately 42.65% (the METPO `GC_<=42.65` bin; note that the upstream label 'high' does not match this numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_<=42.65
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the lower end of GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_high_low_gc_bin: 3 nodes, 2 edges

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
- **METPO identifier:** METPO:1000432
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A GC-content phenotype with genome-wide GC composition at or below approximately 42.65% (the METPO `GC_<=42.65` bin; note that the upstream label 'high' does not match this numeric threshold, but the synonym is preserved as the authoritative bin definition).
- **Parent traits:** METPO:1000127
- **Synonyms:** GC_<=42.65
- **Existing evidence:** DOI:10.1038/nrg2358: GC content (Bacterial-genome review supports the lower end of GC content as a distinct genomic-composition phenotype.)
- **Existing causal graph summary:** gc_high_low_gc_bin: 3 nodes, 2 edges

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


# Microbial Trait Causal Graph Curation Report: **GC high** (METPO:1000432; synonym **GC_<=42.65**)

## 0. Executive scope summary
The METPO trait labeled **“GC high”** is, by its authoritative synonym and definition, a **genome-wide low-GC / AT-rich bin**: **GC ≤ ~42.65%** (“GC_<=42.65”). This should be curated as a **genomic-composition phenotype** (whole-genome base composition), not as GC skew, codon-position GC, or local sequence composition. Empirically, the bin includes both (i) moderately low-GC free-living lineages and (ii) extreme boundary cases such as obligate endosymbionts with **~14–18% GC** (far inside the bin) (yasuda2024highlyreducedcomplementary pages 1-2).

Mechanistically, the strongest evidence in the retrieved 2023–2024 corpus ties AT enrichment / low GC to **mutational biases** amplified by **loss or inefficiency of base-excision repair (BER)** and related damage-control systems, which can produce **hypermutator phenotypes** and **GC-eroding substitution spectra**, often coupled to **genome reduction** and (in host-restricted lineages) **drift-driven accumulation of mildly deleterious mutations** (moncadas2026deepbranchingchloroflexotalineages pages 6-7, moncadas2026deepbranchingchloroflexotalineages pages 8-9, yasuda2024highlyreducedcomplementary pages 1-2). Ultra-reduced endosymbionts also show linked functional thresholds at ~**400 kb** (loss of autonomous envelope biogenesis) and **<200 kb** (erosion of translation machinery), indicating a reductive-evolution regime where extreme compositional bias is common (mccutcheon2024howdobacterial pages 4-5, mccutcheon2024howdobacterial pages 3-4, mccutcheon2024howdobacterial media 5bb83dea, mccutcheon2024howdobacterial media 1429c695).

## 1. Trait scope (what METPO:1000432 represents)
### 1.1 Definition and intended measurement
- **Phenotype:** Genome-wide **G+C fraction** (overall genomic base composition) falling into the METPO bin **GC_<=42.65**.
- **What it is not:**
  - Not **GC skew** (strand asymmetry) or replication-associated nucleotide skews.
  - Not **GC3** (3rd codon position) per se, although GC3 shifts can be a proximate mechanism contributing to whole-genome GC changes (moncadas2026deepbranchingchloroflexotalineages pages 9-10).
  - Not codon usage bias as an endpoint, though codon usage can be a downstream consequence or modulator.

### 1.2 Boundary cases and nearby traits
- **Extreme low-GC boundary cases (endosymbionts):** Psyllid bacteriome symbionts include Carsonella lineages described as **“AT-rich (14.0–17.9% GC)”** and other symbionts at **~16–18.6% GC** (yasuda2024highlyreducedcomplementary pages 1-2). These are not merely “low GC”; they represent an extreme AT-enriched regime.
- **Genome reduction thresholds relevant for boundary interpretation:**
  - Envelope autonomy often lost below **~400 kb** genomes (mccutcheon2024howdobacterial pages 4-5).
  - Translation machinery erosion begins below **~200 kb** genomes (“tipping-point endosymbionts”) (mccutcheon2024howdobacterial pages 4-5, mccutcheon2024howdobacterial pages 3-4).
  - A related figure set in McCutcheon et al. visually supports these thresholds and links compositional bias to GC content (mccutcheon2024howdobacterial media 5bb83dea, mccutcheon2024howdobacterial media 1429c695).
- **Free-living low-GC:** Low-GC can also arise outside host association; repair-loss hypermutator dynamics and genome reduction during habitat shifts can precede/drive GC decline (moncadas2026deepbranchingchloroflexotalineages pages 9-10).

## 2. Key concepts and definitions (current understanding)
### 2.1 “AT-rich / low-GC genomes”
- Quantitatively, McCutcheon et al. frame prokaryotic GC composition as spanning roughly **~75% GC** (GC-rich) down to **~13% GC** (extreme AT-rich) (mccutcheon2024howdobacterial pages 5-7).
- In host-associated endosymbionts, “AT-rich” can be concretely **~14–18% GC** (yasuda2024highlyreducedcomplementary pages 1-2).

### 2.2 Primary mechanistic hypothesis classes
1. **Mutation pressure / mutational bias:** Chemical lesions (e.g., cytosine deamination → uracil; oxidative damage) create biased base substitutions that, if not corrected, can erode GC (moncadas2026deepbranchingchloroflexotalineages pages 6-7, deka2025basesubstitutionsin pages 3-5).
2. **DNA repair pathway loss or reduction:** Loss of BER glycosylases and nucleotide-sanitizing enzymes can amplify lesion persistence and biased substitutions, causing GC erosion and hypermutation (moncadas2026deepbranchingchloroflexotalineages pages 6-7, moncadas2026deepbranchingchloroflexotalineages pages 8-9).
3. **Genome reduction and deletional processes:** Genome reduction can precede GC decline; deletions may outpace point-mutation accumulation during ecological transitions (moncadas2026deepbranchingchloroflexotalineages pages 8-9).
4. **Host restriction + drift:** In obligate host-restricted lineages, accumulation of mildly deleterious mutations and reduced selection efficacy contribute to drastic genome reduction; these regimes often co-occur with extreme AT-richness (yasuda2024highlyreducedcomplementary pages 1-2).
5. **Countervailing processes:** Purifying selection and GC-biased gene conversion can oppose AT bias (deka2025basesubstitutionsin pages 3-5), and biochemical constraints may create a lower bound on GC needed to encode amino-acid diversity (hale2025elevatedratesand pages 14-17).

## 3. Recent developments / latest research (emphasis on 2024)
### 3.1 2024: Extreme AT-rich symbiont genomes quantified
Yasuda et al. (May 2024) provide explicit, curation-friendly statistics for extreme low-GC genomes in psyllid symbionts, including:
- Carsonella lineages: **158–174 kb** genomes and **“AT-rich (14.0–17.9% GC)”** (yasuda2024highlyreducedcomplementary pages 1-2).
- Secondary symbiont Secondary_AM: **229,822 bp, 17.3% GC**; Carsonella_AM: **169,120 bp, 16.2% GC**; related Psyllophila genomes: **221–237 kb, 17.3–18.6% GC** (yasuda2024highlyreducedcomplementary pages 1-2).
These values supply strong empirical anchors for the low-GC trait and support a boundary-case “extreme AT-rich endosymbiont” node.

### 3.2 2024: Genome-size thresholds for reductive evolution
McCutcheon et al. (Apr 2024) synthesize comparative patterns across many severely reduced endosymbionts:
- **~400 kb threshold:** “complete loss of the ability to autonomously make a cell envelope (fatty acids, phospholipids, cell wall) occurs in bacteria with genomes smaller than about 400 kb” (mccutcheon2024howdobacterial pages 4-5).
- **<200 kb tipping point:** “Genomes less than 200 kb start to lose a significant number of ribosomal proteins, tRNAs, and amino acyl-tRNA synthetases,” i.e., translation erosion (mccutcheon2024howdobacterial pages 4-5, mccutcheon2024howdobacterial pages 3-4).
- These patterns are summarized visually in their figures showing gene loss vs genome size and proteome compositional bias driven by GC (mccutcheon2024howdobacterial media 5bb83dea, mccutcheon2024howdobacterial media 1429c695).

### 3.3 Evidence base limitations for 2023–2024 free-living low-GC
Within the retrieved corpus, the most explicit 2023–2024 quantitative low-GC measurements are concentrated in **host-associated symbionts**, not in free-living taxa. Mechanistic evidence for repair-loss-driven GC erosion is strong but was retrieved primarily from outside 2024 in this run (notably a 2026 Nature Communications paper) (moncadas2026deepbranchingchloroflexotalineages pages 6-7, moncadas2026deepbranchingchloroflexotalineages pages 8-9, moncadas2026deepbranchingchloroflexotalineages pages 9-10). This does not invalidate the mechanism; it indicates additional targeted 2023–2024 searches could further strengthen “free-living low-GC” edges.

## 4. Current applications and real-world implementations
### 4.1 Trait usage in microbial genomics
- **Genome classification/annotation:** Whole-genome GC% is routinely used in quality control, taxonomic description, and comparative genomics; here it is operationalized as a bin (≤42.65%).
- **Endosymbiont biology and minimal-genome inference:** Genome size and compositional bias thresholds (e.g., <200 kb “tipping-point endosymbionts”) provide practical heuristics for identifying deeply host-dependent bacteria and anticipating missing cellular modules (envelope biogenesis, translation components) (mccutcheon2024howdobacterial pages 4-5, mccutcheon2024howdobacterial pages 3-4, mccutcheon2024howdobacterial media 5bb83dea).

### 4.2 Translational/biotech relevance (mechanism-informed)
- **Genome stability engineering:** Repair-loss / hypermutator states are relevant to adaptive laboratory evolution and strain engineering, but direct applied 2023–2024 sources were not captured in this run; curation should therefore remain focused on mechanistic graph edges supported by the present evidence.

## 5. Expert synthesis and interpretation (authoritative sources)
- **Endosymbiont reductive evolution as a regime:** McCutcheon et al. emphasize convergence and threshold-like transitions in functional gene loss during extreme genome reduction (mccutcheon2024howdobacterial pages 4-5, mccutcheon2024howdobacterial pages 3-4).
- **Mutation + repair loss as mechanistic route to AT enrichment:** Evidence links BER degradation and loss of specific repair/sanitizing functions to GC-eroding substitution spectra and mutator phenotypes, offering a causal pathway from repair-gene loss to AT-enriched composition (moncadas2026deepbranchingchloroflexotalineages pages 6-7, moncadas2026deepbranchingchloroflexotalineages pages 8-9).
- **Host restriction and drift:** Yasuda et al. describe obligately host-restricted symbiont genomes suffering “accumulating mildly deleterious mutations,” consistent with drift-driven reductive evolution that co-occurs with extreme AT-richness (yasuda2024highlyreducedcomplementary pages 1-2).

## 6. Candidate causal-graph nodes (grouped by type)
| Group | Node label | Brief definition | Evidence / context snippet | Suggested ontology CURIEs |
|---|---|---|---|---|
| A. Mutational processes / lesions | Cytosine deamination | Spontaneous conversion of cytosine to uracil, creating AT-enriching mutation pressure when unrepaired | “Spontaneous cytosine deamination… produces U·G/U·A pairs; unrepaired uracil is read as thymine during replication, causing G → A transitions” (moncadas2026deepbranchingchloroflexotalineages pages 6-7) | CHEBI:17172 (cytosine); CHEBI:17821 (uracil); GO:0006281 |
| A. Mutational processes / lesions | Guanine oxidation / oxidized base damage | Oxidative base damage that can drive GC→TA or related substitutions contributing to GC erosion | “guanine oxidation (8-oxo-guanine → G→T transversions)” and “particular substitutions (C→T/G→A and G→T/C→A) are more common” (deka2025basesubstitutionsin pages 3-5) | CHEBI:44605 (8-oxo-dGTP, related oxidized guanine pool lesion); GO:0006281 |
| A. Mutational processes / lesions | Oxidized pyrimidine accumulation | Build-up of oxidized pyrimidine lesions when repair is impaired, causing transversions | “Lack of Nei permits oxidized pyrimidine accumulation, yielding G·C → T·A transversions” (moncadas2026deepbranchingchloroflexotalineages pages 6-7) | GO:0006284; CHEBI:27568 |
| A. Mutational processes / lesions | AT-biased mutation spectrum | Net mutation bias favoring A/T over G/C across the genome | “mutation spectra biased toward GC-eroding changes” and “the text also notes that purifying selection and biased gene conversion (BGC) can counteract AT bias” (moncadas2026deepbranchingchloroflexotalineages pages 8-9, deka2025basesubstitutionsin pages 3-5) | label-only candidate; GO:0006259 |
| A. Mutational processes / lesions | Third-codon-position AT enrichment | Preferential replacement of GC-rich synonymous codons by AT-rich codons | “substitution of third codon positions with AT-rich nucleotides as a principal driver of decreased GC” (moncadas2026deepbranchingchloroflexotalineages pages 9-10) | label-only candidate |
| A. Mutational processes / lesions | Hypermutator state | Elevated genome-wide mutation rate produced by repair-gene loss, accelerating GC erosion and gene loss | “10- to 10^4-fold mutator phenotypes… providing a mechanistic path to AT-enrichment and gene loss” (moncadas2026deepbranchingchloroflexotalineages pages 8-9) | label-only candidate |
| B. DNA repair genes / pathways | Base-excision repair (BER) | DNA repair pathway removing damaged or inappropriate bases; degradation of BER is linked to GC decline | “loss-of-function mutations in DNA repair genes… degraded BER pathways, producing a hypermutator state that accelerated GC erosion” (moncadas2026deepbranchingchloroflexotalineages pages 9-10) | GO:0006284 |
| B. DNA repair genes / pathways | Uracil-DNA glycosylase (UDG family) | Repair enzyme removing uracil from DNA after cytosine deamination or dUMP misincorporation | “Absence of DNA glycosylases… compromises repair of… deaminated cytosine (uracil)” (moncadas2026deepbranchingchloroflexotalineages pages 6-7) | EC:3.2.2.27; GO:0006284 |
| B. DNA repair genes / pathways | Tag / AlkA / MPG glycosylases | BER glycosylases involved in repair of alkylated or damaged bases; loss associated with GC-eroding mutation pressure | “concerted loss of specific DNA-repair and sanitizing enzymes (Tag/AlkA/MPG, UDG, Nei, MutT)” (moncadas2026deepbranchingchloroflexotalineages pages 8-9) | label-only candidate; GO:0006284 |
| B. DNA repair genes / pathways | Nei glycosylase | BER enzyme repairing oxidized pyrimidines; loss permits GC-eroding transversions | “Lack of Nei permits oxidized pyrimidine accumulation” (moncadas2026deepbranchingchloroflexotalineages pages 6-7) | label-only candidate; GO:0006284 |
| B. DNA repair genes / pathways | MutT nucleotide-pool sanitization | Enzymatic removal of oxidized nucleotides from the dNTP pool; loss contributes to mutational dysregulation | “concerted loss of… MutT… removed defenses against common small-base lesions” (moncadas2026deepbranchingchloroflexotalineages pages 8-9) | label-only candidate; GO:0006281 |
| C. Genome architecture / size states | Genome reduction | Reductive evolution with cumulative gene loss; in some lineages it temporally precedes GC decline | “genome reduction precedes the decline in GC content, implying deletions outpace mutation accumulation” (moncadas2026deepbranchingchloroflexotalineages pages 8-9) | label-only candidate |
| C. Genome architecture / size states | Deletional bias / cumulative deletions | Preferential DNA loss during reductive evolution, potentially preceding compositional change | “elevated mutation rates facilitate gene inactivation and cumulative deletions, driving genome shrinkage” (moncadas2026deepbranchingchloroflexotalineages pages 6-7) | label-only candidate |
| C. Genome architecture / size states | Sub-megabase reduced genome | Strongly reduced bacterial genome state, usually host-associated in the most extreme cases | “genomes <1 Mb are almost exclusively host-associated” (mccutcheon2024howdobacterial pages 1-3) | label-only candidate |
| C. Genome architecture / size states | Tipping-point endosymbiont (<200 kb) | Ultra-reduced genome state where translation-related systems begin to erode | “Genomes less than 200 kb start to lose a significant number of ribosomal proteins, tRNAs, and amino acyl-tRNA synthetases” (mccutcheon2024howdobacterial pages 4-5, mccutcheon2024howdobacterial pages 3-4) | label-only candidate |
| C. Genome architecture / size states | Extreme AT-rich endosymbiont genome | Boundary-case low-GC genome far below the METPO cutoff, typical of long-term obligate symbionts | “AT-rich (14.0–17.9% GC)” and “17.3% GC… 16.2% GC… 17.3–18.6% GC” (yasuda2024highlyreducedcomplementary pages 1-2) | label-only candidate |
| D. Ecological contexts | Host-associated obligate endosymbiosis | Intracellular, vertically transmitted lifestyle repeatedly associated with genome reduction and very low GC | “current highly reduced, AT-rich genomes are characteristic of long-term host-associated obligate symbionts” (yasuda2024highlyreducedcomplementary pages 1-2) | ENVO:01000922 (host-associated habitat, candidate) |
| D. Ecological contexts | Obligate host restriction | Ecological dependence on host environment associated with reduced effective population size and reductive evolution | “The genomes of obligately host-restricted bacteria suffer from accumulating mildly deleterious mutations” (yasuda2024highlyreducedcomplementary pages 1-2) | ENVO:01000922 (candidate) |
| D. Ecological contexts | Genetic drift / fixation of mildly deleterious mutations | Population-genetic regime favoring accumulation of slightly deleterious changes and gene loss in host-restricted lineages | “suffer from accumulating mildly deleterious mutations, resulting in a drastic size reduction” (yasuda2024highlyreducedcomplementary pages 1-2) | label-only candidate |
| E. Cellular functional modules | Cell envelope biogenesis | Biosynthesis of fatty acids, phospholipids, and cell wall; autonomous capacity is often lost in ultra-reduced genomes | “complete loss of the ability to autonomously make a cell envelope (fatty acids, phospholipids, cell wall) occurs in bacteria with genomes smaller than about 400 kb” (mccutcheon2024howdobacterial pages 4-5) | GO:0008610; GO:0009273; GO:0005886 |
| E. Cellular functional modules | Envelope transport / insertion systems | BAM/Sec and related membrane-associated systems that are lost alongside envelope simplification | “These envelope losses coincide with losses in the ability to transport macromolecules across (BAM complex, sec translocon) or insert into… lipid bilayers” (mccutcheon2024howdobacterial pages 4-5, mccutcheon2024howdobacterial pages 3-4) | GO:0017038; GO:0006605 |
| E. Cellular functional modules | Translation machinery | Ribosomal proteins, tRNAs, and aminoacyl-tRNA synthetases that erode in the smallest genomes | “Genomes less than 200 kb start to lose a significant number of ribosomal proteins, tRNAs, and amino acyl-tRNA synthetases” (mccutcheon2024howdobacterial pages 4-5) | GO:0006412; GO:0005840; GO:0004812 |
| E. Cellular functional modules | Proteome compositional bias driven by GC content | Amino-acid composition of proteins shifts systematically with genome GC, especially in AT-rich endosymbionts | “endosymbiont and organelle genomes are often very AT rich and that this AT bias alters amino acid composition of their proteomes” (mccutcheon2024howdobacterial pages 5-7) | label-only candidate |


*Table: This table groups candidate nodes for a GC_<=42.65 causal graph into mutational, repair, genome-state, ecological, and cellular-function categories. It is useful for curation because it links each proposed node to a concise evidence snippet and provisional ontology grounding.*

## 7. Candidate evidence-backed causal edges (triples)
| Subject node label | Predicate | Object node label | Evidence snippet / quote | Reference details | DOI URL | Notes / uncertainty and suggested ontology CURIEs |
|---|---|---|---|---|---|---|
| Cytosine deamination | contributes_to | GC_<=42.65 (low-GC / AT-rich genome) | “Spontaneous cytosine deamination or uracil misincorporation produces U·G/U·A pairs; unrepaired uracil is read as thymine during replication, causing G → A transitions.” (moncadas2026deepbranchingchloroflexotalineages pages 6-7) | Moncadas et al., 2026, *Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization* | https://doi.org/10.1038/s41467-026-71228-y | Strong mechanistic support for AT-enriching substitutions; curate as proximate mutational process, not a dedicated gene node. Suggested CURIEs: GO:0006281 DNA repair; CHEBI:17172 cytosine; CHEBI:17821 uracil. |
| Guanine oxidation / oxidized pyrimidine lesions | contributes_to | GC_<=42.65 (low-GC / AT-rich genome) | “Lack of Nei permits oxidized pyrimidine accumulation, yielding G·C → T·A transversions.” (moncadas2026deepbranchingchloroflexotalineages pages 6-7) | Moncadas et al., 2026, *Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization* | https://doi.org/10.1038/s41467-026-71228-y | Supports oxidative-damage route to GC erosion. Suggested CURIEs: GO:0006284 base-excision repair; GO:0000703 oxidation-related DNA repair (broadly related); CHEBI:27568 DNA base lesion. |
| 8-oxo-dGTP accumulation | contributes_to | GC_<=42.65 (low-GC / AT-rich genome) | “absence of MutT allows 8-oxo-dGTP incorporation, producing A·T → C·G transversions.” (moncadas2026deepbranchingchloroflexotalineages pages 6-7) | Moncadas et al., 2026, *Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization* | https://doi.org/10.1038/s41467-026-71228-y | Mechanistically relevant oxidative nucleotide-pool damage; direction is not always GC-lowering in this isolated step, so curate cautiously as part of broader repair-loss mutational dysregulation. Suggested CURIEs: CHEBI:44605 8-oxo-dGTP; GO:0006281 DNA repair. |
| Loss of uracil DNA glycosylase (UDG-family) | causally_promotes | GC_<=42.65 (low-GC / AT-rich genome) | “Absence of DNA glycosylases… and MutT compromises repair of… deaminated cytosine (uracil)… unrepaired uracil is read as thymine during replication, causing G → A transitions.” (moncadas2026deepbranchingchloroflexotalineages pages 6-7) | Moncadas et al., 2026, *Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization* | https://doi.org/10.1038/s41467-026-71228-y | Good edge from repair-loss to GC erosion; gene family grounding may vary by taxon. Suggested CURIEs: GO:0006284 base-excision repair; UniProt family label-only: uracil-DNA glycosylase; EC 3.2.2.27. |
| Loss of BER glycosylases (Tag/AlkA/MPG/Nei) | causally_promotes | GC_<=42.65 (low-GC / AT-rich genome) | “concerted loss of specific DNA-repair and sanitizing enzymes (Tag/AlkA/MPG, UDG, Nei, MutT) removed defenses against common small-base lesions… mutation spectra biased toward GC-eroding changes” (moncadas2026deepbranchingchloroflexotalineages pages 8-9) | Moncadas et al., 2026, *Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization* | https://doi.org/10.1038/s41467-026-71228-y | Strong composite mechanism; may be best modeled as a pathway/process node if exact orthologs differ. Suggested CURIEs: GO:0006284 base-excision repair; UniProt/EC label-only for Tag, AlkA, MPG, Nei. |
| Loss of MutT nucleotide-sanitizing enzyme | causally_promotes | GC_<=42.65 (low-GC / AT-rich genome) | “concerted loss of specific DNA-repair and sanitizing enzymes… MutT… removed defenses against common small-base lesions” and lab analogues showed “mutation spectra biased toward GC-eroding changes” (moncadas2026deepbranchingchloroflexotalineages pages 8-9) | Moncadas et al., 2026, *Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization* | https://doi.org/10.1038/s41467-026-71228-y | Strong but composite evidence; useful node if TraitMech captures nucleotide-pool sanitization. Suggested CURIEs: GO:0006281 DNA repair; UniProt label-only: MutT family hydrolase; EC 3.6.1.-. |
| Hypermutator phenotype | causally_promotes | GC_<=42.65 (low-GC / AT-rich genome) | “Laboratory analogues lacking these activities show 10- to 10^4-fold mutator phenotypes and mutation spectra biased toward GC-eroding changes… providing a mechanistic path to AT-enrichment” (moncadas2026deepbranchingchloroflexotalineages pages 8-9) | Moncadas et al., 2026, *Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization* | https://doi.org/10.1038/s41467-026-71228-y | Strong process-level edge; phenotype/process node rather than gene node. Suggested CURIEs: label-only candidate “hypermutator state”; GO:0006259 DNA metabolic process. |
| Third-codon-position substitution toward AT-rich codons | contributes_to | GC_<=42.65 (low-GC / AT-rich genome) | “The authors identify substitution of third codon positions with AT-rich nucleotides as a principal driver of decreased GC” (moncadas2026deepbranchingchloroflexotalineages pages 9-10) | Moncadas et al., 2026, *Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization* | https://doi.org/10.1038/s41467-026-71228-y | Useful if graph includes codon-position composition nodes; genome-wide GC trait should remain separate from GC3-specific subtraits. Suggested CURIEs: label-only candidate “third codon position AT enrichment”. |
| Genome reduction / deletion bias | precedes_and_promotes | GC_<=42.65 (low-GC / AT-rich genome) | “genome reduction precedes the decline in GC content, implying deletions outpace mutation accumulation during habitat transitions” (moncadas2026deepbranchingchloroflexotalineages pages 8-9) | Moncadas et al., 2026, *Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization* | https://doi.org/10.1038/s41467-026-71228-y | Strong for temporal ordering, but exact predicate may be “precedes” rather than direct causal promotion. Suggested CURIEs: label-only candidate “genome reduction”; GO:0006310 DNA recombination not specific enough; keep label-only if needed. |
| Elevated mutation pressure during genome shrinkage | causally_promotes | GC_<=42.65 (low-GC / AT-rich genome) | “The authors propose that these mutational biases reduce GC content and that elevated mutation rates facilitate gene inactivation and cumulative deletions, driving genome shrinkage (streamlining).” (moncadas2026deepbranchingchloroflexotalineages pages 6-7) | Moncadas et al., 2026, *Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization* | https://doi.org/10.1038/s41467-026-71228-y | Integrative process edge; may overlap with hypermutator node. Suggested CURIEs: label-only candidate “elevated mutation pressure”. |
| Host-associated obligate endosymbiosis | associated_with | GC_<=42.65 (low-GC / AT-rich genome) | “Carsonella lineages are described as ‘AT-rich (14.0–17.9% GC)’… these genomes result from the accumulation of mildly deleterious mutations and marked size reductions… characteristic of long-term host-associated obligate symbionts” (yasuda2024highlyreducedcomplementary pages 1-2) | Yasuda et al., 2024, *Highly Reduced Complementary Genomes of Dual Bacterial Symbionts in the Mulberry Psyllid Anomoneura mori* | https://doi.org/10.1264/jsme2.me24041 | Strong association, but mechanistic direction partly inferred through drift/reduction; mark as ecology/context edge. Suggested CURIEs: ENVO label-only “host-associated habitat”; NCBITaxon label-only for endosymbiont clades where needed. |
| Genetic drift / fixation of mildly deleterious mutations | causally_promotes | GC_<=42.65 (low-GC / AT-rich genome) | “The genomes of obligately host-restricted bacteria suffer from accumulating mildly deleterious mutations, resulting in a drastic size reduction.” (yasuda2024highlyreducedcomplementary pages 1-2) | Yasuda et al., 2024, *Highly Reduced Complementary Genomes of Dual Bacterial Symbionts in the Mulberry Psyllid Anomoneura mori* | https://doi.org/10.1264/jsme2.me24041 | Supports drift-driven reductive evolution context for extreme AT-richness; GC effect is indirect but consistent. Suggested CURIEs: label-only candidate “genetic drift”; GO not ideal. |
| Genome size <1 Mb / strong host association | associated_with | GC_<=42.65 (low-GC / AT-rich genome) | “genomes <1 Mb are almost exclusively host-associated” and reduced endosymbiont genomes show “extreme compositional biases” (mccutcheon2024howdobacterial pages 1-3) | McCutcheon et al., 2024, *How do bacterial endosymbionts work with so few genes?* | https://doi.org/10.1371/journal.pbio.3002577 | Good contextual edge linking severe reduction and host association to compositional bias; does not alone prove low GC. Suggested CURIEs: label-only “reduced genome”; ENVO label-only “host-associated”. |
| Cell envelope biosynthesis loss threshold (<400 kb genomes) | associated_with | GC_<=42.65 (low-GC / AT-rich genome) | “complete loss of the ability to autonomously make a cell envelope… occurs in bacteria with genomes smaller than about 400 kb” (mccutcheon2024howdobacterial pages 4-5) | McCutcheon et al., 2024, *How do bacterial endosymbionts work with so few genes?* | https://doi.org/10.1371/journal.pbio.3002577 | Important threshold for boundary cases among ultra-reduced endosymbionts; link to low-GC is indirect, so mark uncertain. Suggested CURIEs: GO:0008610 lipid biosynthetic process; GO:0009273 peptidoglycan-based cell wall biogenesis; GO:0005886 plasma membrane. |
| Translation machinery erosion threshold (<200 kb genomes) | associated_with | GC_<=42.65 (low-GC / AT-rich genome) | “Genomes less than 200 kb start to lose a significant number of ribosomal proteins, tRNAs, and amino acyl-tRNA synthetases,” defining “tipping-point endosymbionts” (mccutcheon2024howdobacterial pages 4-5, mccutcheon2024howdobacterial pages 3-4) | McCutcheon et al., 2024, *How do bacterial endosymbionts work with so few genes?* | https://doi.org/10.1371/journal.pbio.3002577 | Useful for extreme boundary cases, not for the general GC<=42.65 bin; indirect association with AT-richness via severe reductive evolution. Suggested CURIEs: GO:0006412 translation; GO:0005840 ribosome; GO:0004812 aminoacyl-tRNA ligase activity. |
| Extremely AT-rich genome composition | subclass_of / extreme_example_of | GC_<=42.65 (low-GC / AT-rich genome) | “AT-rich (14.0–17.9% GC)” and “17.3% GC… 16.2% GC… 17.3–18.6% GC” for reduced symbionts (yasuda2024highlyreducedcomplementary pages 1-2) | Yasuda et al., 2024, *Highly Reduced Complementary Genomes of Dual Bacterial Symbionts in the Mulberry Psyllid Anomoneura mori* | https://doi.org/10.1264/jsme2.me24041 | Not a causal edge but valuable calibration row showing that endosymbiont examples sit far inside the METPO GC<=42.65 bin; include only if graph supports exemplar subclasses. Suggested CURIEs: METPO:1000432 target trait. |
| AT-mutational equilibrium / selection-maintained higher GC floor | opposes_full_shift_to | GC_<=42.65 (low-GC / AT-rich genome) | In LAB, “Selectional pressures… and biochemical constraints (minimum GC ~20–25% to encode all amino acids) are noted as opposing forces maintaining higher observed GC than mutation equilibrium predicts.” (hale2025elevatedratesand pages 14-17) | Hale et al., 2025, *Elevated rates and biased spectra of mutations in anaerobically cultured lactic acid bacteria* | https://doi.org/10.1128/mbio.03054-25 | Useful counter-edge: AT-biased mutation pushes lower GC, while selection/constraints can resist further decline. Suggested CURIEs: label-only “biochemical constraint on minimal GC”; GO:0006412 translation. |
| Purifying selection and biased gene conversion | opposes | GC_<=42.65 (low-GC / AT-rich genome) | “the text also notes that purifying selection and biased gene conversion (BGC) can counteract AT bias, especially in GC-rich organisms” (deka2025basesubstitutionsin pages 3-5) | Deka et al., 2025, *Base substitutions in genomes due to deamination and oxidation of DNA bases, favoring genome compositional biases* | https://doi.org/10.63635/mrj.v1i4.188 | Countervailing process; probably not a positive causal edge for this trait, but useful warning in graph notes. Suggested CURIEs: GO:0000018 regulation of DNA recombination (broad), label-only “GC-biased gene conversion”. |


*Table: This table lists candidate subject-predicate-object edges for curating the GC_<=42.65 microbial genome trait, emphasizing evidence-backed mechanisms such as mutational bias, DNA repair loss, genome reduction, and host-associated reductive evolution. It is useful for selecting which nodes and edges are strong enough for TraitMech curation and which should remain uncertain or contextual.*

## 8. Visual evidence (figures)
McCutcheon et al. include figures showing (i) gene loss patterns across genome-size thresholds (~400 kb envelope autonomy loss; <200 kb translation erosion) and (ii) proteome compositional bias driven by genomic GC content (mccutcheon2024howdobacterial media 5bb83dea, mccutcheon2024howdobacterial media 1429c695).

## 9. Warnings / claims not ready for curation
1. **2023–2024 free-living low-GC ecological drivers:** In this run, explicit 2023–2024 sources quantifying free-living low-GC genomes and directly tying them to specific environments (temperature, nutrients, oxygen) were not retrieved. Any such edges should be marked **uncertain** until supported by targeted sources.
2. **Biased gene conversion (BGC) as a driver (vs counter-driver):** The present evidence more strongly supports BGC as a **counteracting** process to AT bias rather than a direct cause of low GC; model as a modulator unless additional low-GC-promoting BGC evidence is obtained (deka2025basesubstitutionsin pages 3-5).
3. **Some repair-loss steps have mixed GC-directionality:** For example, the MutT-related step described includes an A·T→C·G effect in isolation (moncadas2026deepbranchingchloroflexotalineages pages 6-7); it should be curated as part of a **broader repair-loss mutational dysregulation** rather than as a standalone “GC decreases” edge.
4. **Label mismatch (“GC high” vs low-GC bin):** Curation should preserve the **authoritative numeric bin** (GC_<=42.65) as primary meaning, documenting the mismatch explicitly in trait metadata.

## 10. DOI-first bibliography (with URLs and publication dates)
- McCutcheon JP, Garber AI, Spencer N, Warren JM. **How do bacterial endosymbionts work with so few genes?** *PLOS Biology*. **2024-04**. DOI: **10.1371/journal.pbio.3002577**. https://doi.org/10.1371/journal.pbio.3002577 (mccutcheon2024howdobacterial pages 1-3, mccutcheon2024howdobacterial pages 4-5, mccutcheon2024howdobacterial pages 3-4, mccutcheon2024howdobacterial pages 5-7, mccutcheon2024howdobacterial media 5bb83dea, mccutcheon2024howdobacterial media 1429c695)
- Yasuda Y, Inoue H, Hirose Y, Nakabachi A. **Highly Reduced Complementary Genomes of Dual Bacterial Symbionts in the Mulberry Psyllid Anomoneura mori.** *Microbes and Environments*. **2024-05**. DOI: **10.1264/jsme2.me24041**. https://doi.org/10.1264/jsme2.me24041 (yasuda2024highlyreducedcomplementary pages 1-2)
- Moncadas LS, Shakurova A, Hofer C, Andrei A-S. **Deep-branching Chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization.** *Nature Communications*. **2026-04**. DOI: **10.1038/s41467-026-71228-y**. https://doi.org/10.1038/s41467-026-71228-y (moncadas2026deepbranchingchloroflexotalineages pages 6-7, moncadas2026deepbranchingchloroflexotalineages pages 8-9, moncadas2026deepbranchingchloroflexotalineages pages 9-10)
- Deka N, Beura PK, Jain M, Ahmed N, Deka RC, Satapathy SS, Ray SK. **Base Substitutions in Genomes Due to Deamination and Oxidation of DNA Bases, Favoring Genome Compositional Biases.** *Multidisciplinary Research Journal*. **2025-12**. DOI: **10.63635/mrj.v1i4.188**. https://doi.org/10.63635/mrj.v1i4.188 (deka2025basesubstitutionsin pages 3-5, deka2025basesubstitutionsin pages 13-15)
- Hale OF, Yin M, Behringer MG. **Elevated rates and biased spectra of mutations in anaerobically cultured lactic acid bacteria.** *mBio*. **2025-12**. DOI: **10.1128/mbio.03054-25**. https://doi.org/10.1128/mbio.03054-25 (hale2025elevatedratesand pages 14-17)

---

## Curation-ready takeaway (for `data/traits/genomics/gc_high.yaml`)
- Treat METPO:1000432 as **GC_<=42.65 (low GC / AT-rich)** and document the label mismatch.
- Strong candidate causal modules for the graph: **BER degradation (GO:0006284)**, **uracil excision repair (UDG; EC 3.2.2.27)**, **oxidative damage and lesion repair**, **hypermutator state**, **genome reduction / deletional bias**, and **host-associated endosymbiosis with drift** (moncadas2026deepbranchingchloroflexotalineages pages 6-7, moncadas2026deepbranchingchloroflexotalineages pages 8-9, yasuda2024highlyreducedcomplementary pages 1-2).
- Include boundary-case evidence: **Carsonella and related psyllid symbionts at ~14–18% GC** (yasuda2024highlyreducedcomplementary pages 1-2) and size thresholds for functional collapse (<400 kb envelope; <200 kb translation) (mccutcheon2024howdobacterial pages 4-5, mccutcheon2024howdobacterial pages 3-4, mccutcheon2024howdobacterial media 5bb83dea).

References

1. (yasuda2024highlyreducedcomplementary pages 1-2): Yuka Yasuda, Hiromitsu Inoue, Yuu Hirose, and Atsushi Nakabachi. Highly reduced complementary genomes of dual bacterial symbionts in the mulberry psyllid anomoneura mori. Microbes and Environments, 39:n/a, May 2024. URL: https://doi.org/10.1264/jsme2.me24041, doi:10.1264/jsme2.me24041. This article has 6 citations and is from a peer-reviewed journal.

2. (moncadas2026deepbranchingchloroflexotalineages pages 6-7): Lucas Serra Moncadas, Alisa Shakurova, Cyrill Hofer, and Adrian-Stefan Andrei. Deep-branching chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization. Nature Communications, Apr 2026. URL: https://doi.org/10.1038/s41467-026-71228-y, doi:10.1038/s41467-026-71228-y. This article has 0 citations and is from a highest quality peer-reviewed journal.

3. (moncadas2026deepbranchingchloroflexotalineages pages 8-9): Lucas Serra Moncadas, Alisa Shakurova, Cyrill Hofer, and Adrian-Stefan Andrei. Deep-branching chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization. Nature Communications, Apr 2026. URL: https://doi.org/10.1038/s41467-026-71228-y, doi:10.1038/s41467-026-71228-y. This article has 0 citations and is from a highest quality peer-reviewed journal.

4. (mccutcheon2024howdobacterial pages 4-5): John P. McCutcheon, Arkadiy I. Garber, Noah Spencer, and Jessica M. Warren. How do bacterial endosymbionts work with so few genes? PLOS Biology, 22:e3002577, Apr 2024. URL: https://doi.org/10.1371/journal.pbio.3002577, doi:10.1371/journal.pbio.3002577. This article has 32 citations and is from a highest quality peer-reviewed journal.

5. (mccutcheon2024howdobacterial pages 3-4): John P. McCutcheon, Arkadiy I. Garber, Noah Spencer, and Jessica M. Warren. How do bacterial endosymbionts work with so few genes? PLOS Biology, 22:e3002577, Apr 2024. URL: https://doi.org/10.1371/journal.pbio.3002577, doi:10.1371/journal.pbio.3002577. This article has 32 citations and is from a highest quality peer-reviewed journal.

6. (mccutcheon2024howdobacterial media 5bb83dea): John P. McCutcheon, Arkadiy I. Garber, Noah Spencer, and Jessica M. Warren. How do bacterial endosymbionts work with so few genes? PLOS Biology, 22:e3002577, Apr 2024. URL: https://doi.org/10.1371/journal.pbio.3002577, doi:10.1371/journal.pbio.3002577. This article has 32 citations and is from a highest quality peer-reviewed journal.

7. (mccutcheon2024howdobacterial media 1429c695): John P. McCutcheon, Arkadiy I. Garber, Noah Spencer, and Jessica M. Warren. How do bacterial endosymbionts work with so few genes? PLOS Biology, 22:e3002577, Apr 2024. URL: https://doi.org/10.1371/journal.pbio.3002577, doi:10.1371/journal.pbio.3002577. This article has 32 citations and is from a highest quality peer-reviewed journal.

8. (moncadas2026deepbranchingchloroflexotalineages pages 9-10): Lucas Serra Moncadas, Alisa Shakurova, Cyrill Hofer, and Adrian-Stefan Andrei. Deep-branching chloroflexota lineages illuminate the eco-evolutionary foundation of cross-ecosystem colonization. Nature Communications, Apr 2026. URL: https://doi.org/10.1038/s41467-026-71228-y, doi:10.1038/s41467-026-71228-y. This article has 0 citations and is from a highest quality peer-reviewed journal.

9. (mccutcheon2024howdobacterial pages 5-7): John P. McCutcheon, Arkadiy I. Garber, Noah Spencer, and Jessica M. Warren. How do bacterial endosymbionts work with so few genes? PLOS Biology, 22:e3002577, Apr 2024. URL: https://doi.org/10.1371/journal.pbio.3002577, doi:10.1371/journal.pbio.3002577. This article has 32 citations and is from a highest quality peer-reviewed journal.

10. (deka2025basesubstitutionsin pages 3-5): Nishita Deka, Pratyush Kumar Beura, Monika Jain, Najima Ahmed, Ramesh Chandra Deka, Siddhartha Shankar Satapathy, and Suvendra Kumar Ray. Base substitutions in genomes due to deamination and oxidation of dna bases, favoring genome compositional biases. Multidisciplinary Research Journal, pages 21-37, Dec 2025. URL: https://doi.org/10.63635/mrj.v1i4.188, doi:10.63635/mrj.v1i4.188. This article has 1 citations.

11. (hale2025elevatedratesand pages 14-17): Owen F. Hale, Michelle Yin, and Megan G. Behringer. Elevated rates and biased spectra of mutations in anaerobically cultured lactic acid bacteria. mBio, Dec 2025. URL: https://doi.org/10.1128/mbio.03054-25, doi:10.1128/mbio.03054-25. This article has 0 citations and is from a domain leading peer-reviewed journal.

12. (mccutcheon2024howdobacterial pages 1-3): John P. McCutcheon, Arkadiy I. Garber, Noah Spencer, and Jessica M. Warren. How do bacterial endosymbionts work with so few genes? PLOS Biology, 22:e3002577, Apr 2024. URL: https://doi.org/10.1371/journal.pbio.3002577, doi:10.1371/journal.pbio.3002577. This article has 32 citations and is from a highest quality peer-reviewed journal.

13. (deka2025basesubstitutionsin pages 13-15): Nishita Deka, Pratyush Kumar Beura, Monika Jain, Najima Ahmed, Ramesh Chandra Deka, Siddhartha Shankar Satapathy, and Suvendra Kumar Ray. Base substitutions in genomes due to deamination and oxidation of dna bases, favoring genome compositional biases. Multidisciplinary Research Journal, pages 21-37, Dec 2025. URL: https://doi.org/10.63635/mrj.v1i4.188, doi:10.63635/mrj.v1i4.188. This article has 1 citations.