---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:23:06.306186'
end_time: '2026-06-18T02:38:10.149730'
duration_seconds: 903.84
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range high
  trait_identifier: METPO:1000454
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range extends above approximately 40 \xB0C, characteristic of thermophilic\
    \ physiology."
  parent_traits: METPO:1000306
  synonyms: Thermophile, TR_>40
  evidence_summary: "DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of\
    \ high temperature (Thermophile-adaptation review supports growth ranges extending\
    \ above 40 \xB0C as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001:\
    \ resistant to irreversible inactivation at high temperatures (Thermostable-protein\
    \ review supports thermostability as the mechanism extending growth into thermophilic\
    \ temperatures.)"
  causal_graph_summary: 'temperature_range_high_thermophile: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range high
- **METPO identifier:** METPO:1000454
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range extends above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Thermophile, TR_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports growth ranges extending above 40 °C as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostability as the mechanism extending growth into thermophilic temperatures.)
- **Existing causal graph summary:** temperature_range_high_thermophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_high.yaml`.

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
- **Trait label:** temperature range high
- **METPO identifier:** METPO:1000454
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range extends above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Thermophile, TR_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports growth ranges extending above 40 °C as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostability as the mechanism extending growth into thermophilic temperatures.)
- **Existing causal graph summary:** temperature_range_high_thermophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_high.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **temperature range high** (METPO:1000454)

### Scope summary (trait meaning, boundaries, operationalization)

**Trait definition (curation-ready):** *Temperature range high* represents a growth-temperature phenotype in which an organism can sustain growth at elevated temperatures such that the growth-supporting ambient temperature range extends above ~40–45 °C (thermophilic physiology), typically characterized using **cardinal temperatures**: minimal (TMIN), optimal (TOPT), and maximal (TMAX) growth temperatures. (lehmann2023adaptivelaboratoryevolution pages 1-2, rasul2024thermophiliccyanobacteria—excitingyet pages 3-4)

**Common quantitative cutoffs in recent sources (2023–2024):**
- Thermophiles are often defined as organisms that **thrive above 45 °C** (growth/TOPT >45 °C), with hyperthermophiles **proliferating above 80 °C**. (valenzuela2024isolationofthermophilic pages 1-2)
- A practical boundary used in cyanobacteria literature: **continuous growth ≥45 °C** is regarded as a “borderline” thermophilic criterion. (rasul2024thermophiliccyanobacteria—excitingyet pages 3-4)
- Another 2023 definition stratifies: *thermotolerant* (survive above 45 °C), *moderate thermophile* (optimal 45–65 °C), *strict thermophile* (optimal 65–80 °C), *hyperthermophile* (grow above 80 °C). (rekadwad2023extremophilesthespecies pages 2-4)

**Distinguishing nearby traits / boundary cases:**
- **Thermotolerant vs thermophilic:** thermotolerant organisms may survive transiently above 45 °C without an elevated TOPT, whereas thermophiles have an elevated TOPT and can actively grow and reproduce at high temperature. (rekadwad2023extremophilesthespecies pages 2-4, gallo2024theundeniablepotential pages 1-3)
- **Thermophilic vs hyperthermophilic:** hyperthermophiles have TOPT >80 °C and include taxa with growth up to >100 °C (e.g., *Methanopyrus kandleri* up to 122 °C noted in a 2023 review). (rekadwad2023extremophilesthespecies pages 2-4)

**Assay/measurement framing for curation:** the trait is most cleanly grounded in **growth curves across a temperature series** (to infer TMIN/TOPT/TMAX) rather than single-point “survival” assays. (lehmann2023adaptivelaboratoryevolution pages 1-2, valenzuela2024isolationofthermophilic pages 2-4)

---

## 1) Key concepts and definitions (current understanding)

### Conceptual model: what “temperature range high” captures
Thermophily is a systems phenotype reflecting that multiple cellular subsystems remain functional under heat stress, including:
1) **Genome stability** (DNA topology/repair/packaging). (takemata2024howdothermophiles pages 1-2)
2) **Proteostasis** (protein folding, disaggregation, and degradation). (moon2023temperaturemattersbacterial pages 6-7)
3) **Membrane integrity and permeability control** (lipid composition, packing, proton permeability). (chong2024archaeamembranesin pages 1-2)
4) **Metabolic and respiratory robustness** at high temperature in specific ecophysiologies (e.g., chemolithoautotrophy in vents). (deng2023strategiesofchemolithoautotrophs pages 1-2)

These are not alternative explanations but partially redundant/interactive mechanisms; the trait is best represented as a **causal graph** rather than a single “thermostability gene.” (takemata2024howdothermophiles pages 1-2)

---

## 2) Recent developments and latest research (priority 2023–2024)

### Genome organization and reverse gyrase as a thermophile signature (2024)
A 2024 review highlights **reverse gyrase** (TopR/rgy) as a hallmark of thermophilic genomes and describes its mechanistic role in maintaining genome integrity at high temperature by introducing **positive DNA supercoils**, limiting thermal melting and supporting repair. (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3)

**Visual evidence (recommended for curator review):** Figure/summary panels in the 2024 genome-organization review depict reverse gyrase functions (positive supercoiling, reannealing, nicked-DNA protection, Holliday-junction resolution) and compare its presence across thermophilic vs mesophilic archaea. (takemata2024howdothermophiles media ec31065d, takemata2024howdothermophiles media d0f585be)

### Multi-omics of hyperthermophile thermal stress response (2023)
Integrated RNA-seq/proteomics in *Pyrococcus furiosus* (hyperthermophile) shows that heat shock triggers rapid transcriptome reprogramming governed by the transcriptional regulator **Phr**, and that some heat-shock signature genes return to baseline at the RNA level while proteins remain persistently upregulated—suggesting a “rapid but sustained” response architecture. (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 19-21)

### Membrane adaptation mechanisms in thermoacidophilic archaea (2024)
A 2024 membrane-focused review details how thermoacidophilic archaea dominated by **bipolar tetraether lipids** (GDGT/GDNT) vary cyclopentane ring content, tetraether:diether ratio, and headgroup glycosylation to tune membrane packing/rigidity. These adjustments reduce temperature sensitivity and help maintain low passive proton permeability and near-neutral intracellular pH, supporting protein activity at elevated temperature. (chong2024archaeamembranesin pages 1-2)

### Systems framing of bacterial temperature responses (2023)
A 2023 review synthesizes that bacterial high-temperature response is centrally mediated by chaperone systems (DnaK-DnaJ; GroEL-GroES) and ATP-dependent disaggregation/degradation systems (ClpB/ClpG, Lon, Clp, HslUV, FtsH), linking thermal stress to protein denaturation/aggregation management. (moon2023temperaturemattersbacterial pages 6-7)

---

## 3) Current applications and real-world implementations (with data)

### High-temperature biomanufacturing / “bioreactive distillation” (2023)
A 2023 study engineered the hyperthermophilic archaeon *Pyrococcus furiosus* to synthesize ethanol at **95 °C**; the paper notes prior temperature records for biological ethanol production (native producer 72 °C; engineered 85 °C) and argues that high-temperature fermentations can reduce contamination risk and enable direct distillation of volatile products. *P. furiosus* is also noted to grow optimally near **100 °C** with a rapid doubling time (~37 min). (lipscomb2023manipulatingfermentationpathways pages 1-2)

### Thermozymes and screening/bioprospecting (2024)
A 2024 review of hot-spring thermophile mining reports thermophilic microorganisms surviving **50–120 °C** and enzyme activities observed across **−10 to 120 °C**, emphasizing modern sequence-based discovery expanding beyond classical isolate-based screening. (burkhardt2024miningthermophilesfor pages 1-2)

### Thermophilic cyanobacteria as chassis (2024)
A 2024 biotechnology-focused review reports thermophilic cyanobacteria growth between **45–73 °C** and emphasizes light-harvesting components and thermostable complexes as key biotechnological parts, while highlighting ongoing limitations in genetic tool availability. (rasul2024thermophiliccyanobacteria—excitingyet pages 1-3)

### Thermophiles in industrial processes (2024 review synthesis)
A 2024 industrial review compiles thermophilic hydrogen production at **60 °C** with reported maximum H2 yield of **760 mL/L**, and discusses thermophilic conditions improving biodegradability of some plastics and reducing methane lag time in co-digestion settings (values reported within the review). (gallo2024theundeniablepotential pages 4-5)

---

## 4) Expert opinions / analysis from authoritative sources

### “Thermophily is multifactorial, not single-mechanism”
Recent reviews frame thermophily as emerging from coordinated stabilization of **DNA/RNA**, **proteins**, and **membranes**, alongside regulated stress responses; reverse gyrase is emphasized as a genomic signature but not the only determinant. (grunberger2023uncoveringthetemporal pages 1-2, takemata2024howdothermophiles pages 1-2)

### Practical curation guidance: trait vs mechanism
- **Trait curation** (METPO:1000454) should be anchored to measured growth above ~40–45 °C (ideally via cardinal temperatures). (lehmann2023adaptivelaboratoryevolution pages 1-2, rasul2024thermophiliccyanobacteria—excitingyet pages 3-4)
- **Mechanism curation** should avoid overgeneralizing taxon-specific solutions (e.g., archaeal tetraether lipid cyclization) to bacteria, and should annotate environmental coupling (e.g., combined high temperature + low pH effects). (chong2024archaeamembranesin pages 1-2)

---

## 5) Candidate causal-graph entities (curation-oriented)

A structured node inventory with suggested ontology grounding is provided here:

| Node label | Node type | Suggested ontology grounding | Key evidence citation IDs supporting relevance |
|---|---|---|---|
| reverse gyrase (TopR/rgy) | gene/protein | EC:5.6.2.4 | (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3, deng2023strategiesofchemolithoautotrophs pages 1-2) |
| DNA positive supercoiling | process/function | GO:0006265 | (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3) |
| DNA melting limitation | process/function | label-only | (takemata2024howdothermophiles pages 1-2, grunberger2023uncoveringthetemporal pages 24-26) |
| DNA repair | process/function | GO:0006281 | (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3, deng2023strategiesofchemolithoautotrophs pages 20-20) |
| nucleoid-associated proteins (NAPs) | gene/protein | GO:0008301 | (takemata2024howdothermophiles pages 1-2, grunberger2023uncoveringthetemporal pages 19-21, takemata2024howdothermophiles pages 2-3) |
| archaeal histones | gene/protein | GO:0031491 | (takemata2024howdothermophiles pages 1-2, grunberger2023uncoveringthetemporal pages 19-21, takemata2024howdothermophiles pages 2-3) |
| SMC proteins | gene/protein | GO:0098649 | (takemata2024howdothermophiles pages 1-2) |
| polyamines | chemical | CHEBI:88061 | (lehmann2023adaptivelaboratoryevolution pages 1-2, takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3) |
| DnaK | gene/protein | UniProtKB:P0A6Y8 | (moon2023temperaturemattersbacterial pages 6-7, grunberger2023uncoveringthetemporal pages 1-2) |
| DnaJ | gene/protein | UniProtKB:P08622 | (moon2023temperaturemattersbacterial pages 6-7) |
| GroEL | gene/protein | UniProtKB:P0A6F5 | (moon2023temperaturemattersbacterial pages 6-7, grunberger2023uncoveringthetemporal pages 1-2) |
| GroES | gene/protein | UniProtKB:P0A6F9 | (moon2023temperaturemattersbacterial pages 6-7) |
| HtpG | gene/protein | UniProtKB:P0A6Z3 | (moon2023temperaturemattersbacterial pages 6-7) |
| ClpB | gene/protein | UniProtKB:P63284 | (moon2023temperaturemattersbacterial pages 6-7) |
| ClpG | gene/protein | label-only | (moon2023temperaturemattersbacterial pages 6-7) |
| Lon protease | gene/protein | EC:3.4.21.53 | (moon2023temperaturemattersbacterial pages 6-7) |
| Clp proteases | gene/protein | GO:0009840 | (moon2023temperaturemattersbacterial pages 6-7) |
| HslUV protease complex | gene/protein | label-only | (moon2023temperaturemattersbacterial pages 6-7) |
| FtsH protease | gene/protein | EC:3.4.24.- | (moon2023temperaturemattersbacterial pages 6-7) |
| heat shock regulator Phr | gene/protein | label-only | (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 19-21, grunberger2023uncoveringthetemporal pages 23-24, grunberger2023uncoveringthetemporal pages 24-26) |
| archaeal tetraether lipids | chemical | CHEBI:36615 | (chong2024archaeamembranesin pages 1-2) |
| GDGT (glycerol dialkyl glycerol tetraether) | chemical | label-only | (chong2024archaeamembranesin pages 1-2) |
| GDNT (glycerol dialkyl calditol tetraether) | chemical | label-only | (chong2024archaeamembranesin pages 1-2) |
| cyclopentane rings in tetraether lipids | structure | label-only | (chong2024archaeamembranesin pages 1-2) |
| polar headgroup glycosylation | process/function | GO:0006486 | (chong2024archaeamembranesin pages 1-2) |
| ether-linked phospholipids | chemical | CHEBI:64716 | (rekadwad2023extremophilesthespecies pages 2-4, chong2024archaeamembranesin pages 1-2) |
| passive proton permeability | process/function | GO:1902600 | (chong2024archaeamembranesin pages 1-2) |
| intracellular pH homeostasis | process/function | GO:0006885 | (chong2024archaeamembranesin pages 1-2) |
| membrane packing tightness/rigidity | structure | label-only | (chong2024archaeamembranesin pages 1-2) |
| membrane fluidity | phenotype | GO:0016042 | (maiti2024extrememakeoverthe pages 2-3, chong2024archaeamembranesin pages 1-2) |
| homeoviscous adaptation | process/function | label-only | (maiti2024extrememakeoverthe pages 2-3) |
| osmolytes | chemical | CHEBI:15377 | (maiti2024extrememakeoverthe pages 2-3) |
| osmolyte-mediated adaptation | process/function | label-only | (maiti2024extrememakeoverthe pages 2-3) |
| cytochrome bd ubiquinol oxidase | gene/protein | EC:7.1.1.7 | (deng2023strategiesofchemolithoautotrophs pages 1-2) |
| hydrogen oxidation | process/function | GO:0015671 | (deng2023strategiesofchemolithoautotrophs pages 1-2) |
| reverse TCA cycle (rTCA cycle) | pathway/module | KEGG:M00173 | (deng2023strategiesofchemolithoautotrophs pages 1-2) |
| NAD(H)-linked glutamate dehydrogenase | gene/protein | EC:1.4.1.2 | (deng2023strategiesofchemolithoautotrophs pages 1-2) |
| high-temperature growth / thermophily | phenotype | METPO:1000454 | (lehmann2023adaptivelaboratoryevolution pages 1-2, valenzuela2024isolationofthermophilic pages 1-2, gallo2024theundeniablepotential pages 1-3, moon2023temperaturemattersbacterial pages 1-3) |
| hyperthermophily | phenotype | label-only | (lehmann2023adaptivelaboratoryevolution pages 1-2, valenzuela2024isolationofthermophilic pages 1-2, gallo2024theundeniablepotential pages 1-3, rekadwad2023extremophilesthespecies pages 2-4) |
| incubation temperature | environment/assay factor | PATO:0000146 | (valenzuela2024isolationofthermophilic pages 2-4, deng2023strategiesofchemolithoautotrophs pages 1-2) |
| external pH | environment/assay factor | PATO:0000196 | (chong2024archaeamembranesin pages 1-2, deng2023strategiesofchemolithoautotrophs pages 1-2) |
| hydrothermal vent / hot spring environment | environment/assay factor | ENVO:00000213 | (deng2023strategiesofchemolithoautotrophs pages 1-2, burkhardt2024miningthermophilesfor pages 1-2, rekadwad2023extremophilesthespecies pages 2-4) |


*Table: This table lists candidate nodes for a TraitMech-style causal graph of temperature range high (thermophily), organized by node type with tentative ontology grounding. It is useful for curation because it maps reported mechanisms from recent literature to graph-ready entities and highlights where grounding remains label-only.*

---

## 6) Evidence-backed candidate causal edges (triples)

A curation-ready edge table (with snippets and uncertainty notes) is provided here:

| Proposed edge (subject–predicate–object) | Evidence citation id(s) | Supporting snippet / quote | Notes |
|---|---|---|---|
| reverse gyrase (TopR/rgy) → introduces → positive DNA supercoils | (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3, deng2023strategiesofchemolithoautotrophs pages 1-2) | "reverse gyrase, a unique topoisomerase that introduces positive supercoils into DNA" | Strong, repeatedly supported; broadly applicable to many thermophiles/hyperthermophiles, especially archaea. |
| positive DNA supercoiling → limits → DNA melting | (takemata2024howdothermophiles pages 1-2, grunberger2023uncoveringthetemporal pages 24-26) | "maintain the genome integrity of thermophiles by limiting DNA melting" | Strong mechanistic edge; general for reverse-gyrase-bearing thermophiles. |
| reverse gyrase (TopR/rgy) → maintains → genome integrity at high temperature | (takemata2024howdothermophiles pages 1-2, deng2023strategiesofchemolithoautotrophs pages 1-2) | "rgy gene plays a critical role... by maintaining DNA stability at high temperature" | Strong; one source is taxon-specific (Nautiliales), but consistent with broader review evidence. |
| reverse gyrase → enables → growth at ~95°C / very high temperature | (grunberger2023uncoveringthetemporal pages 24-26) | "Reverse gyrase is explicitly reported as essential for growth at ~95°C" | Strong but strongest direct evidence is hyperthermophile-specific; curate as high-confidence for hyperthermophiles, moderate for broader thermophily. |
| polyamines → stabilizes → DNA at elevated temperature | (lehmann2023adaptivelaboratoryevolution pages 1-2, takemata2024howdothermophiles pages 1-2) | "DNA stabilization mechanisms cited include protection by positively charged polyamines" | Moderate strength; general mechanism, but direct growth-phenotype linkage is partly inferred. |
| histones / nucleoid-associated proteins (NAPs) → stabilizes / packages → thermophile genomes | (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3) | "NAPs and polyamines" and "histones... are implicated in folding and stabilizing genomes" | Strong for archaeal thermophiles; taxon bias toward Archaea. |
| tetraether lipids (GDGT/GDNT) → increases → membrane packing tightness / rigidity | (chong2024archaeamembranesin pages 1-2) | "increase packing tightness and rigidity in the membrane hydrophobic core" | Strong for thermoacidophilic archaea; lipid chemistry is archaeal-specific. |
| cyclopentane rings in tetraether lipids → alters / increases → membrane rigidity and low temperature sensitivity | (chong2024archaeamembranesin pages 1-2) | "varying the number of cyclopentane rings" and "retain low membrane volume fluctuations and their low sensitivity to temperature" | Strong but mainly in archaeal tetraether membranes; taxon-specific. |
| tetraether:diether ratio / headgroup glycosylation changes → modulates → hydrogen-bond network and membrane packing | (chong2024archaeamembranesin pages 1-2) | "the ratio of tetraethers to diethers, and the level of glycosylation... alter the hydrogen bond networks" | Strong for archaeal membrane adaptation; more specific to thermoacidophiles. |
| increased membrane packing / rigidity → decreases → passive proton permeability | (chong2024archaeamembranesin pages 1-2) | "a low passive proton permeability... can be maintained" | Strong for archaeal thermoacidophile membranes; mechanism may not generalize to all bacteria. |
| decreased proton permeability → maintains → near-neutral intracellular pH | (chong2024archaeamembranesin pages 1-2) | "a low passive proton permeability and a near neutral intracellular pH can be maintained" | Strong but mainly relevant where external acidity co-occurs with high temperature. |
| near-neutral intracellular pH → preserves → optimal soluble and membrane protein activity at elevated temperature | (chong2024archaeamembranesin pages 1-2) | "as a result, optimal activities of soluble and membrane-bound proteins... can be retained" | Strong in thermoacidophile context; high-temperature relevance is direct but pH-coupled. |
| DnaK-DnaJ → assists → ATP-dependent folding of nascent/unfolded proteins | (moon2023temperaturemattersbacterial pages 6-7) | "DnaK-DnaJ... assist ATP-dependent folding of nascent and unfolded peptides" | Strong, bacterial heat/high-temperature response; more heat-stress/proteostasis than exclusive thermophile determinant. |
| GroEL-GroES / HtpG → assists → protein folding under heat stress | (moon2023temperaturemattersbacterial pages 6-7, grunberger2023uncoveringthetemporal pages 1-2) | "GroEL-GroES, HtpG" and heat shock genes encoding chaperones "such as DnaK and GroEL" | Strong general heat-response edge; likely broadly relevant but not uniquely thermophile-specific. |
| DnaK-DnaJ → recruits / activates → ClpB disaggregase | (moon2023temperaturemattersbacterial pages 6-7) | "DnaK-DnaJ... recruit and activate the disaggregase ClpB via direct interaction" | Strong, bacterial and mechanistically specific. |
| ClpB / ClpG → promotes → protein disaggregation | (moon2023temperaturemattersbacterial pages 6-7) | "enabling ATP-dependent disaggregation" and "ClpG can act as a standalone potent disaggregase" | Strong; bacterial, stress-response focused. |
| Lon / Clp / HslUV / FtsH proteases → degrades → misfolded or damaged proteins | (moon2023temperaturemattersbacterial pages 6-7) | "Proteases (Lon, Clp proteases, HslUV, FtsH) are induced to remove misfolded/damaged/aggregated proteins" | Strong, bacterial heat-response edge. |
| chaperones / proteases / disaggregases → maintains → proteostasis at high temperature | (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 6-7) | "protein denaturation, aggregation, and loss of function during heat shock" and refolding/degradation systems counter these | Strong general mechanism; link to thermophile trait is indirect but biologically central. |
| proteostasis at high temperature → supports → survival / growth at high temperature | (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 6-7) | "supporting thermophile survival at high temperature" | Moderate-to-strong; often inferred from stress-response physiology rather than direct trait assays. |
| Phr regulator → induces → heat shock gene expression / transcriptome reprogramming | (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 19-21) | "heat shock elicits rapid transcriptome reprogramming driven by the transcriptional regulator Phr" | Strong, archaeal and especially Pyrococcus furiosus-specific. |
| Phr-regulated heat shock response → causes → sustained protein-level upregulation after heat shock | (grunberger2023uncoveringthetemporal pages 19-21) | "classic HS-protective genes rapidly upregulated at RNA and maintained at the protein level" | Moderate strength; strong in P. furiosus, uncertain as universal thermophile mechanism. |
| sustained heat-shock protein upregulation → supports → heat-shock adaptation | (grunberger2023uncoveringthetemporal pages 19-21, grunberger2023uncoveringthetemporal pages 24-26) | "small heat shock protein" and "heat shock response in archaea" | Moderate; taxon-specific and best curated as archaeal heat adaptation rather than universal thermophily. |


*Table: This table lists candidate curation-ready causal edges for the trait temperature range high (thermophile), with short supporting quotes and notes on confidence, scope, and taxon specificity. It is designed to help translate recent literature into TraitMech graph assertions.*

In addition, Figure-based evidence for reverse gyrase roles (positive supercoiling, reannealing, nick protection, Holliday junction handling) is visually summarized in the 2024 genome-organization review. (takemata2024howdothermophiles media ec31065d, takemata2024howdothermophiles media d0f585be)

---

## 7) Warnings / do-not-curate-yet items (risk flags)

1) **pH-coupled membrane mechanisms:** Many detailed tetraether-lipid → proton permeability → intracellular pH edges come from thermoacidophile context; curate with explicit environmental qualifiers (high temperature + low pH). (chong2024archaeamembranesin pages 1-2)
2) **Heat-shock response vs thermophily:** Chaperone/protease networks are central to surviving transient heat shock across bacteria, but not all heat-shock components are determinants of a stable thermophilic TOPT; treat as “supports high-temperature survival/tolerance” unless linked to growth-range shifts. (moon2023temperaturemattersbacterial pages 6-7)
3) **GC-content correlations:** GC enrichment is mentioned as one mechanism in some thermophiles but is not obligatory; avoid curating a universal edge “high GC → thermophily” without clade-specific support. (takemata2024howdothermophiles pages 1-2)
4) **Reverse gyrase universality:** reverse gyrase is strongly associated with high-temperature life, and some sources describe it as essential at ~95 °C; however, the degree of necessity may vary by lineage and temperature regime—use uncertainty tags if generalizing beyond hyperthermophiles. (grunberger2023uncoveringthetemporal pages 24-26, takemata2024howdothermophiles pages 2-3)

---

## DOI-first bibliography (publication date + URL)

**2024**
- Takemata N. *How Do Thermophiles Organize Their Genomes?* **Microbes and Environments** (Jun 2024). DOI: **10.1264/jsme2.me23087**. https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2)
- Chong PL-G. *Archaea membranes in response to extreme acidic environments.* **Frontiers in Biophysics** (Jan 2024; article DOI year 2023). DOI: **10.3389/frbis.2023.1338019**. https://doi.org/10.3389/frbis.2023.1338019 (chong2024archaeamembranesin pages 1-2)
- Maiti A, Erimban S, Daschakraborty S. *Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.* **Chemical Communications** (Aug 2024). DOI: **10.1039/d4cc03114h**. https://doi.org/10.1039/d4cc03114h (maiti2024extrememakeoverthe pages 2-3)
- Rasul F, You D, Jiang Y, Liu X, Daroch M. *Thermophilic cyanobacteria—exciting, yet challenging biotechnological chassis.* **Applied Microbiology and Biotechnology** (Mar 2024). DOI: **10.1007/s00253-024-13082-w**. https://doi.org/10.1007/s00253-024-13082-w (rasul2024thermophiliccyanobacteria—excitingyet pages 3-4, rasul2024thermophiliccyanobacteria—excitingyet pages 1-3)
- Valenzuela B, Solís-Cornejo F, Araya R, Zamorano P. *Isolation of thermophilic bacteria from extreme environments in northern Chile.* **Microorganisms** (Feb 2024). DOI: **10.3390/microorganisms12030473**. https://doi.org/10.3390/microorganisms12030473 (valenzuela2024isolationofthermophilic pages 1-2, valenzuela2024isolationofthermophilic pages 2-4)
- Burkhardt C et al. *Mining thermophiles for biotechnologically relevant enzymes…* **Extremophiles** (Nov 2024). DOI: **10.1007/s00792-023-01321-3**. https://doi.org/10.1007/s00792-023-01321-3 (burkhardt2024miningthermophilesfor pages 1-2)
- Gallo G, Imbimbo P, Aulitto M. *The Undeniable Potential of Thermophiles in Industrial Processes.* **IJMS** (Jul 2024). DOI: **10.3390/ijms25147685**. https://doi.org/10.3390/ijms25147685 (gallo2024theundeniablepotential pages 1-3, gallo2024theundeniablepotential pages 9-11, gallo2024theundeniablepotential pages 4-5)

**2023**
- Lehmann M et al. *Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.* **Frontiers in Microbiology** (Oct 2023). DOI: **10.3389/fmicb.2023.1265216**. https://doi.org/10.3389/fmicb.2023.1265216 (lehmann2023adaptivelaboratoryevolution pages 1-2)
- Moon S et al. *Temperature Matters: Bacterial Response to Temperature Change.* **Journal of Microbiology** (Mar 2023). DOI: **10.1007/s12275-023-00031-x**. https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 6-7)
- Grünberger F et al. *Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics.* **mBio** (Dec 2023). DOI: **10.1128/mbio.02174-23**. https://doi.org/10.1128/mbio.02174-23 (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 19-21, grunberger2023uncoveringthetemporal pages 23-24, grunberger2023uncoveringthetemporal pages 24-26)
- Deng W et al. *Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions…* **Microbiome** (Dec 2023). DOI: **10.1186/s40168-023-01712-w**. https://doi.org/10.1186/s40168-023-01712-w (deng2023strategiesofchemolithoautotrophs pages 1-2)
- Lipscomb GL et al. *Manipulating fermentation pathways in the hyperthermophilic archaeon Pyrococcus furiosus for ethanol production up to 95°C…* **Applied and Environmental Microbiology** (Jun 2023). DOI: **10.1128/aem.00012-23**. https://doi.org/10.1128/aem.00012-23 (lipscomb2023manipulatingfermentationpathways pages 1-2)
- Rekadwad BN et al. *Extremophiles: the species that evolve and survive under hostile conditions.* **3 Biotech** (Aug 2023). DOI: **10.1007/s13205-023-03733-6**. https://doi.org/10.1007/s13205-023-03733-6 (rekadwad2023extremophilesthespecies pages 2-4)


References

1. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

2. (rasul2024thermophiliccyanobacteria—excitingyet pages 3-4): Faiz Rasul, Dawei You, Ying Jiang, Xiangjian Liu, and Maurycy Daroch. Thermophilic cyanobacteria—exciting, yet challenging biotechnological chassis. Applied Microbiology and Biotechnology, Mar 2024. URL: https://doi.org/10.1007/s00253-024-13082-w, doi:10.1007/s00253-024-13082-w. This article has 16 citations and is from a domain leading peer-reviewed journal.

3. (valenzuela2024isolationofthermophilic pages 1-2): Bernardita Valenzuela, Francisco Solís-Cornejo, Rubén Araya, and Pedro Zamorano. Isolation of thermophilic bacteria from extreme environments in northern chile. Microorganisms, 12:473, Feb 2024. URL: https://doi.org/10.3390/microorganisms12030473, doi:10.3390/microorganisms12030473. This article has 17 citations.

4. (rekadwad2023extremophilesthespecies pages 2-4): Bhagwan Narayan Rekadwad, Wen-Jun Li, Juan M. Gonzalez, Rekha Punchappady Devasya, Arun Ananthapadmanabha Bhagwath, Ruchi Urana, and Khalid Parwez. Extremophiles: the species that evolve and survive under hostile conditions. 3 Biotech, Aug 2023. URL: https://doi.org/10.1007/s13205-023-03733-6, doi:10.1007/s13205-023-03733-6. This article has 49 citations and is from a peer-reviewed journal.

5. (gallo2024theundeniablepotential pages 1-3): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 21 citations.

6. (valenzuela2024isolationofthermophilic pages 2-4): Bernardita Valenzuela, Francisco Solís-Cornejo, Rubén Araya, and Pedro Zamorano. Isolation of thermophilic bacteria from extreme environments in northern chile. Microorganisms, 12:473, Feb 2024. URL: https://doi.org/10.3390/microorganisms12030473, doi:10.3390/microorganisms12030473. This article has 17 citations.

7. (takemata2024howdothermophiles pages 1-2): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

8. (moon2023temperaturemattersbacterial pages 6-7): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

9. (chong2024archaeamembranesin pages 1-2): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 9 citations.

10. (deng2023strategiesofchemolithoautotrophs pages 1-2): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 14 citations and is from a highest quality peer-reviewed journal.

11. (takemata2024howdothermophiles pages 2-3): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

12. (takemata2024howdothermophiles media ec31065d): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

13. (takemata2024howdothermophiles media d0f585be): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

14. (grunberger2023uncoveringthetemporal pages 1-2): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

15. (grunberger2023uncoveringthetemporal pages 19-21): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

16. (lipscomb2023manipulatingfermentationpathways pages 1-2): Gina L. Lipscomb, Alexander T. Crowley, Diep M. N. Nguyen, Matthew W. Keller, Hailey C. O’Quinn, Tania N. N. Tanwee, Jason L. Vailionis, Ke Zhang, Ying Zhang, Robert M. Kelly, and Michael W. W. Adams. Manipulating fermentation pathways in the hyperthermophilic archaeon <i>pyrococcus furiosus</i> for ethanol production up to 95°c driven by carbon monoxide oxidation. Applied and Environmental Microbiology, Jun 2023. URL: https://doi.org/10.1128/aem.00012-23, doi:10.1128/aem.00012-23. This article has 13 citations and is from a peer-reviewed journal.

17. (burkhardt2024miningthermophilesfor pages 1-2): Christin Burkhardt, Leon Baruth, Neele Meyer-Heydecke, Barbara Klippel, Armine Margaryan, Ani Paloyan, Hovik H. Panosyan, and Garabed Antranikian. Mining thermophiles for biotechnologically relevant enzymes: evaluating the potential of european and caucasian hot springs. Extremophiles, Nov 2024. URL: https://doi.org/10.1007/s00792-023-01321-3, doi:10.1007/s00792-023-01321-3. This article has 38 citations and is from a peer-reviewed journal.

18. (rasul2024thermophiliccyanobacteria—excitingyet pages 1-3): Faiz Rasul, Dawei You, Ying Jiang, Xiangjian Liu, and Maurycy Daroch. Thermophilic cyanobacteria—exciting, yet challenging biotechnological chassis. Applied Microbiology and Biotechnology, Mar 2024. URL: https://doi.org/10.1007/s00253-024-13082-w, doi:10.1007/s00253-024-13082-w. This article has 16 citations and is from a domain leading peer-reviewed journal.

19. (gallo2024theundeniablepotential pages 4-5): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 21 citations.

20. (grunberger2023uncoveringthetemporal pages 24-26): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

21. (deng2023strategiesofchemolithoautotrophs pages 20-20): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 14 citations and is from a highest quality peer-reviewed journal.

22. (grunberger2023uncoveringthetemporal pages 23-24): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

23. (maiti2024extrememakeoverthe pages 2-3): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

24. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

25. (gallo2024theundeniablepotential pages 9-11): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 21 citations.