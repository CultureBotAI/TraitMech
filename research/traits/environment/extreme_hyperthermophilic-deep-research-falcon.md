---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:46:29.001886'
end_time: '2026-06-17T22:03:55.764077'
duration_seconds: 1046.76
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: extreme hyperthermophilic
  trait_identifier: METPO:1000721
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: extreme_hyperthermophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature preference that grows optimally at temperatures above\
    \ 90\xB0C."
  parent_traits: METPO:1000613
  synonyms: extreme hyperthermophile, extremely hyperthermophilic
  evidence_summary: 'DOI:10.1007/s007920050010: It grew at between 90 degrees C and
    113 degrees C (Organism example: Pyrolobus fumarii grows in the extreme hyperthermophilic
    range.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation
    at high temperatures (Thermostable-protein review supports extreme protein and
    membrane stability as the basis of hyperthermophile physiology.)'
  causal_graph_summary: 'extreme_hyperthermophilic_archaeal_adaptation: 5 nodes, 4
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** extreme hyperthermophilic
- **METPO identifier:** METPO:1000721
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference that grows optimally at temperatures above 90°C.
- **Parent traits:** METPO:1000613
- **Synonyms:** extreme hyperthermophile, extremely hyperthermophilic
- **Existing evidence:** DOI:10.1007/s007920050010: It grew at between 90 degrees C and 113 degrees C (Organism example: Pyrolobus fumarii grows in the extreme hyperthermophilic range.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports extreme protein and membrane stability as the basis of hyperthermophile physiology.)
- **Existing causal graph summary:** extreme_hyperthermophilic_archaeal_adaptation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **extreme hyperthermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/extreme_hyperthermophilic.yaml`.

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
- **Trait label:** extreme hyperthermophilic
- **METPO identifier:** METPO:1000721
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference that grows optimally at temperatures above 90°C.
- **Parent traits:** METPO:1000613
- **Synonyms:** extreme hyperthermophile, extremely hyperthermophilic
- **Existing evidence:** DOI:10.1007/s007920050010: It grew at between 90 degrees C and 113 degrees C (Organism example: Pyrolobus fumarii grows in the extreme hyperthermophilic range.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports extreme protein and membrane stability as the basis of hyperthermophile physiology.)
- **Existing causal graph summary:** extreme_hyperthermophilic_archaeal_adaptation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **extreme hyperthermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/extreme_hyperthermophilic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **Extreme hyperthermophilic** (METPO:1000721)

### Scope summary (TraitMech curation intent)
**Trait definition (current understanding).** The METPO trait **extreme hyperthermophilic** (METPO:1000721) denotes microbes with **optimal growth temperatures >90 °C**. It is a subset of broader **hyperthermophily** (often defined as growth above ~80 °C in the microbiology literature) and represents a temperature preference/physiological capacity rather than a specific assay output. A canonical exemplar is the archaeon *Pyrolobus fumarii*, described as having “an upper temperature limit for growth of 113 °C, and it cannot grow below 90 °C,” placing it squarely in the extreme hyperthermophilic range (irwin2004extremophilesandtheir pages 1-2).

**Boundary cases and distinctions.** The causal graph should explicitly represent threshold behavior around ~90–95 °C. In one hyperthermophile, removal of reverse gyrase still allowed growth at **90 °C**, but growth defects worsened as temperature increased and no growth was observed at **93 °C** during a 49 h test, suggesting reverse gyrase is not universally required at 90 °C (atomi2004reversegyraseis pages 3-5). In contrast, in *Pyrococcus furiosus* reverse gyrase deletion is lethal at **95–100 °C**, supporting a mechanistic “extreme” threshold (lipscomb2017reversegyraseis pages 1-2).

### Key concepts and definitions
- **Thermophile vs hyperthermophile vs extreme hyperthermophile.** A recent review discusses thermophiles thriving in “hyperthermal environments (>80 °C)” and notes some tolerate “temperatures higher than 100 °C,” situating extreme hyperthermophily as the upper tail of thermal life (takemata2024howdothermophiles pages 1-2). The *METPO:1000721* boundary of **Topt >90 °C** is best treated as a curatable operational cutoff.
- **Core selective pressures at extreme temperature.** High temperature destabilizes biomacromolecules, including DNA helix melting/chemical damage and protein denaturation, requiring integrated adaptations in **DNA topology/repair**, **membrane stability**, and **proteostasis** (takemata2024howdothermophiles pages 1-2, irwin2004extremophilesandtheir pages 2-3).

### Recent developments and latest research (prioritizing 2023–2024)
**Genome organization and DNA topology at high temperature (2024).** A 2024 review synthesizes that thermophile genomes are characterized by **reverse gyrase**, a unique topoisomerase introducing positive supercoils, proposed to maintain genome integrity by “limiting DNA melting and mediating DNA repair” (takemata2024howdothermophiles pages 1-2). It additionally notes that “heat shock increases positive supercoils in plasmid DNA,” linking temperature upshift to altered DNA topology (takemata2024howdothermophiles pages 1-2). The same review highlights multi-scale genome organization contributions from nucleoid-associated proteins (NAPs), histones, SMC proteins, and polyamines (takemata2024howdothermophiles pages 1-2).

**Membrane lipid remodeling and terpenoid saturation (2024).** A 2024 *Extremophiles* review connects archaeal membrane adaptation to terpenoid chemistry and reports that **hyperthermophilic methanogens increase membrane-spanning GDGT content at higher temperatures**, suggesting temperature-dependent remodeling toward more stable membrane architectures (rao2024unravelingthemultiplicity pages 2-4). It also states that **cyclized GDGTs** (introduced by **GrsA/GrsB**) “increase membrane packing and stability,” an explicit mechanistic edge that is particularly relevant for a thermoadaptation causal graph (rao2024unravelingthemultiplicity pages 1-2).

**Polyphosphate as an inorganic chaperone in thermophilic archaea (2024).** A 2024 experimental study in *Saccharolobus solfataricus* provides evidence that **polyphosphate (polyP)** can act as an inorganic chaperone: polyP presence correlated with reduced protein precipitation under stress and was associated with upregulation of measured chaperonins; the work explicitly discusses protein-hand-off pathways involving prefoldins and the **thermosome** (Group II chaperonin) (acevedolopez2024roleofpolyphosphate pages 1-2). Although the studied stressor is copper rather than temperature alone, the organism is thermophilic and the mechanism maps to proteostasis constraints exacerbated at high temperatures.

**Community and gene-centric views of thermal adaptation (2024).** A 2024 metagenomic study of a boiling (85 °C) vent-water system reports enrichment of genes for “heat shock proteins, molecular chaperones, and chaperonin complexes,” plus systems modulating DNA gyrase and other stress proteins—evidence useful for environmental-factor nodes and stress-response modules in the graph (mondal2024aquificaeovercomescompetition pages 1-2). While not specific to >90 °C optima, it supports the broader ecological embedding of thermoadaptation gene modules.

### Current applications and real-world implementations
**PCR and molecular diagnostics.** Thermostable DNA polymerases are a mature, real-world implementation of thermophile biomolecules: thermostable polymerases (e.g., Taq; also Pfu with higher fidelity) enable routine PCR workflows, and PCR-based diagnostics are described as “a mainstay” supported by thermostable polymerases (irwin2004extremophilesandtheir pages 3-5, irwin2004extremophilesandtheir pages 5-6). These are relevant as downstream applications of thermostability rather than direct causes of growth at >90 °C.

**Industrial enzymes and economic scale.** A 2023 chapter survey reports broad industrial use of extremozymes across detergent, food, feed, starch, textile, leather, pulp and paper, and pharmaceuticals (ali2023extremophilesandlimits pages 3-4). It also provides market-scale statistics for industrial enzymes (e.g., estimates reaching ~$7.0 billion by 2023) to contextualize economic implementation of thermostable biocatalysts (ali2023extremophilesandlimits pages 1-3).

**Thermo-enzymes with quantitative performance (2023).** A 2023 review of thermo-L-asparaginases reports quantitative data consistent with high-temperature functionality (e.g., optima ~85–90 °C; retention of high activity for extended times at 90 °C in some enzymes), illustrating the translation of hyperthermophile enzyme stability into candidate industrial/biomedical enzymes (dumina2023thermolasparaginasesfromthe pages 2-4).

**Engineering thermophilic archaea as production hosts (2024).** A 2024 paper demonstrates tool-building for *Sulfolobus acidocaldarius* biotechnology: adding 5′-UTRs to plasmid expression constructs produced a **four-fold increase in soluble and active protein yield** for a reporter esterase, illustrating a concrete implementation pathway for producing thermostable archaeal enzymes (kuschmierz20245′untranslatedregionsequences pages 1-2).

### Expert synthesis / analysis from authoritative sources
**Reverse gyrase as a mechanistic hallmark with nuance.** Reviews emphasize reverse gyrase as a characteristic thermophile/hyperthermophile genome feature and hypothesize it prevents DNA thermal denaturation via positive supercoiling (takemata2024howdothermophiles pages 1-2). Primary experimental evidence supports a high-temperature threshold: in *P. furiosus*, reverse gyrase deletion is lethal at **≥95 °C**, consistent with the notion that extreme hyperthermophily (>90 °C) may require additional DNA-topology protection (lipscomb2017reversegyraseis pages 1-2). However, counterevidence exists at ~90 °C in another archaeon: cells deprived of reverse gyrase could still grow at **90 °C**, though were increasingly compromised at higher temperatures (atomi2004reversegyraseis pages 3-5). For curation, this argues for an edge model that is **temperature-thresholded and taxon-dependent**, rather than absolute.

**Membrane stabilization via archaeal lipids.** A foundational review notes archaeal membranes have ether linkages and include tetraether and diether lipids, which are linked to stability at high temperature; an S-layer can also contribute to structural integrity (irwin2004extremophilesandtheir pages 2-3). Recent work adds specificity by highlighting GDGT remodeling and GDGT cyclization enzymes (GrsA/GrsB) as stability mechanisms (rao2024unravelingthemultiplicity pages 2-4, rao2024unravelingthemultiplicity pages 1-2).

### Relevant statistics and data points (recent studies prioritized)
- *Pyrolobus fumarii* thermal range example: “cannot grow below 90 °C” and upper growth limit “113 °C” (irwin2004extremophilesandtheir pages 1-2).
- Reverse gyrase threshold evidence: *P. furiosus* reverse gyrase deletion is lethal at 95–100 °C (lipscomb2017reversegyraseis pages 1-2); separate work shows growth possible at 90 °C without reverse gyrase but not conclusively above 90 °C (atomi2004reversegyraseis pages 3-5).
- Polyphosphate and proteostasis: polyP presence correlates with reduced protein precipitation and chaperonin upregulation in *S. solfataricus* under stress (acevedolopez2024roleofpolyphosphate pages 1-2).
- Biotech implementation metric: 5′-UTR engineering yields ~4× increase in soluble/active protein in *S. acidocaldarius* (kuschmierz20245′untranslatedregionsequences pages 1-2).
- Enzyme performance examples: thermo-L-asparaginases can show optima ~85–90 °C and long activity retention at high temperature (dumina2023thermolasparaginasesfromthe pages 2-4).
- Industrial enzyme market estimates through 2023 (economic implementation context) (ali2023extremophilesandlimits pages 1-3).

### Candidate nodes grouped by type
| Node label | Node type (gene/protein, process, molecule, structure, environment, assay/measurement) | Suggested ontology grounding (CURIEs if available; otherwise 'label-only') | Role in trait (1 phrase) | Key supporting source (DOI/year/URL) |
|---|---|---|---|---|
| extreme hyperthermophilic | environment | METPO:1000721 | target trait: optimal growth above 90°C | 10.1186/2046-0481-57-6-348 / 2004 / https://doi.org/10.1186/2046-0481-57-6-348 (irwin2004extremophilesandtheir pages 1-2) |
| optimal growth temperature >90°C | assay/measurement | label-only | operational boundary defining extreme hyperthermophily | 10.1007/s007920050010 / 1997 / https://doi.org/10.1007/s007920050010; supported by summary evidence in 10.1186/2046-0481-57-6-348 / 2004 / https://doi.org/10.1186/2046-0481-57-6-348 (irwin2004extremophilesandtheir pages 1-2) |
| reverse gyrase | gene/protein | label-only | hallmark DNA-protective topoisomerase of hyperthermophiles | 10.1264/jsme2.me23087 / 2024 / https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2) |
| TopR1 | gene/protein | label-only | heat-responsive reverse gyrase paralog linked to high-temperature growth | 10.1264/jsme2.me23087 / 2024 / https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2) |
| TopR2 | gene/protein | label-only | reverse gyrase paralog maintained across temperatures in Sulfolobus | 10.1264/jsme2.me23087 / 2024 / https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2) |
| positive DNA supercoiling | process | label-only | stabilizes DNA topology at high temperature | 10.1264/jsme2.me23087 / 2024 / https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2) |
| DNA thermal denaturation | process | label-only | major damage pressure countered by thermoadaptation | 10.1264/jsme2.me23087 / 2024 / https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2) |
| DNA breaks | process | label-only | lesion type protected from thermo-degradation | 10.3390/ijms18071340 / 2017 / https://doi.org/10.3390/ijms18071340 (lipscomb2017reversegyraseis pages 1-2) |
| Holliday junction resolution | process | GO:0006310 | proposed reverse gyrase-associated genome maintenance activity | 10.1007/s00792-017-0929-z / 2017 / https://doi.org/10.1007/s00792-017-0929-z (lipscomb2017reversegyraseis pages 2-4) |
| heat shock / temperature upshift | environment | label-only | environmental trigger increasing positive supercoils | 10.1264/jsme2.me23087 / 2024 / https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2) |
| archaeal ether lipids | molecule | label-only | chemically stable membrane lipids for high-temperature survival | 10.1186/2046-0481-57-6-348 / 2004 / https://doi.org/10.1186/2046-0481-57-6-348 (irwin2004extremophilesandtheir pages 2-3) |
| tetraether/diether lipids | structure | label-only | support membrane integrity under membrane-destabilizing heat | 10.1186/2046-0481-57-6-348 / 2004 / https://doi.org/10.1186/2046-0481-57-6-348 (irwin2004extremophilesandtheir pages 2-3) |
| GDGT | molecule | label-only | membrane-spanning archaeal lipid enriched at higher temperatures | 10.1007/s00792-023-01330-2 / 2024 / https://doi.org/10.1007/s00792-023-01330-2 (rao2024unravelingthemultiplicity pages 2-4) |
| cyclized GDGT | molecule | label-only | increases membrane packing and stability | 10.1007/s00792-023-01330-2 / 2024 / https://doi.org/10.1007/s00792-023-01330-2 (rao2024unravelingthemultiplicity pages 1-2) |
| GrsA | gene/protein | label-only | GDGT cyclization enzyme supporting membrane stabilization | 10.1007/s00792-023-01330-2 / 2024 / https://doi.org/10.1007/s00792-023-01330-2 (rao2024unravelingthemultiplicity pages 1-2) |
| GrsB | gene/protein | label-only | GDGT cyclization enzyme supporting membrane stabilization | 10.1007/s00792-023-01330-2 / 2024 / https://doi.org/10.1007/s00792-023-01330-2 (rao2024unravelingthemultiplicity pages 1-2) |
| geranylgeranyl reductase (GGR) | gene/protein | label-only | saturates isoprenoid chains in archaeal phospholipids | 10.1007/s00792-023-01330-2 / 2024 / https://doi.org/10.1007/s00792-023-01330-2 (rao2024unravelingthemultiplicity pages 1-2) |
| chaperone / thermosome | gene/protein | label-only | preserves protein conformation near upper thermal limit | 10.1186/2046-0481-57-6-348 / 2004 / https://doi.org/10.1186/2046-0481-57-6-348 (irwin2004extremophilesandtheir pages 2-3) |
| heat shock proteins | gene/protein | label-only | broad proteostasis support in hot environments | 10.1371/journal.pone.0310595 / 2024 / https://doi.org/10.1371/journal.pone.0310595 (mondal2024aquificaeovercomescompetition pages 1-2) |
| molecular chaperones/chaperonins | process | GO:0006457 | refold or protect proteins during thermal stress | 10.1371/journal.pone.0310595 / 2024 / https://doi.org/10.1371/journal.pone.0310595 (mondal2024aquificaeovercomescompetition pages 1-2) |
| polyphosphate | molecule | CHEBI:18367 | inorganic chaperone reducing protein aggregation in thermophilic archaeon | 10.3390/microorganisms12122627 / 2024 / https://doi.org/10.3390/microorganisms12122627 (acevedolopez2024roleofpolyphosphate pages 1-2) |
| polyamines | molecule | CHEBI:88061 | nucleic-acid stabilizers implicated in DNA thermostability | 10.1264/jsme2.me23087 / 2024 / https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2) |
| nucleoid-associated proteins (NAPs) | gene/protein | label-only | genome organizers implicated in DNA thermostability | 10.1264/jsme2.me23087 / 2024 / https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2) |
| S-layer | structure | GO:0030111 | external structural support for cells at extreme temperature | 10.1186/2046-0481-57-6-348 / 2004 / https://doi.org/10.1186/2046-0481-57-6-348 (irwin2004extremophilesandtheir pages 2-3) |
| membrane permeability | process | GO:0005215 related; label-only | membrane property tuned to remain functional at high temperature | 10.1007/s00792-017-0929-z / 2017 / https://doi.org/10.1007/s00792-017-0929-z (lipscomb2017reversegyraseis pages 2-4) |
| Pyrolobus fumarii | environment | NCBITaxon:43335 | exemplar archaeon defining the >90°C growth range | 10.1186/2046-0481-57-6-348 / 2004 / https://doi.org/10.1186/2046-0481-57-6-348 (irwin2004extremophilesandtheir pages 1-2) |
| Pyrococcus furiosus | environment | NCBITaxon:2261 | model extreme hyperthermophile for reverse gyrase essentiality at 95–100°C | 10.1007/s00792-017-0929-z / 2017 / https://doi.org/10.1007/s00792-017-0929-z (lipscomb2017reversegyraseis pages 1-2) |
| Thermococcus kodakarensis | environment | NCBITaxon:69014 | boundary-case hyperthermophile showing reduced but not abolished growth without reverse gyrase near 90°C | 10.1007/s00792-017-0929-z / 2017 / https://doi.org/10.1007/s00792-017-0929-z (lipscomb2017reversegyraseis pages 1-2) |
| Sulfolobus / Saccharolobus solfataricus | environment | NCBITaxon:2287 | model thermoacidophilic archaeon for TopR1/TopR2 and polyphosphate-chaperone biology | 10.1264/jsme2.me23087 / 2024 / https://doi.org/10.1264/jsme2.me23087; 10.3390/microorganisms12122627 / 2024 / https://doi.org/10.3390/microorganisms12122627 (takemata2024howdothermophiles pages 1-2, acevedolopez2024roleofpolyphosphate pages 1-2) |
| hyperthermophilic methanogens | environment | label-only | exemplar lineage showing higher-temperature increase in membrane-spanning GDGTs | 10.1007/s00792-023-01330-2 / 2024 / https://doi.org/10.1007/s00792-023-01330-2 (rao2024unravelingthemultiplicity pages 2-4) |


*Table: This table lists candidate nodes for a causal graph of the extreme hyperthermophilic trait, spanning phenotype definition, DNA topology, membrane adaptation, proteostasis, and exemplar taxa. It is useful for TraitMech-style curation because it pairs each node with a suggested grounding, a concise mechanistic role, and an evidence source.*

### Candidate causal edges (evidence-backed triples)
| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet (quote) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Reverse gyrase (GO:0003918 candidate) | introduces positive supercoils into | DNA positive supercoiling (GO:0006265 related; label-only) | “reverse gyrase… introduces positive supercoils into DNA” (takemata2024howdothermophiles pages 1-2) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087 | Strong review-supported mechanistic edge; GO grounding for exact activity may need curator verification. |
| DNA positive supercoiling (label-only) | decreases risk of | DNA thermal denaturation/melting (GO:0006260 related; label-only) | “reverse gyrase prevents the thermal denaturation of DNA by introducing positive DNA supercoiling” (takemata2024howdothermophiles pages 1-2) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087 | Curate as mechanistic hypothesis widely accepted in review literature. |
| Reverse gyrase | has heat-protective chaperone activity on | nicked/thermally damaged DNA (label-only) | “Reverse gyrase has heat-protective DNA chaperone activity independent of supercoiling” (mondal2024aquificaeovercomescompetition pages 35-36); “reduce double-stranded DNA breakage ~8-fold at 90 C” (kampmann2004reversegyrasehas pages 1-2) | 10.1093/nar/gkh683, 2004, https://doi.org/10.1093/nar/gkh683 | Strong experimental support; distinct from positive-supercoiling mechanism. |
| Reverse gyrase | protects | DNA breaks from thermo-degradation (label-only) | “TopR1 probably facilitates genome integrity maintenance by protecting DNA breaks from thermo-degradation in vivo” (lipscomb2017reversegyraseis pages 1-2) | 10.3390/ijms18071340, 2017, https://doi.org/10.3390/ijms18071340 | Specific to Sulfolobus TopR1; curate with taxon-specific note. |
| Reverse gyrase deletion (rgy knockout) | causes loss of growth at | 95–100 °C growth condition (ENVO:01000215 hot environment candidate; label-only) | “Deletion of the reverse gyrase gene in Pyrococcus furiosus… is lethal at 95 °C and 100 °C” (lipscomb2017reversegyraseis pages 1-2) | 10.1007/s00792-017-0929-z, 2017, https://doi.org/10.1007/s00792-017-0929-z | Strong causal evidence for extreme hyperthermophily threshold in P. furiosus. |
| Reverse gyrase deletion (rgy knockout) | reduces growth rate at | 90 °C growth condition | “a hyperthermophilic cell deprived of reverse gyrase is still capable of growth at 90°C” and growth-rate ratio declines at higher temperatures (atomi2004reversegyraseis pages 3-5) | 10.1128/jb.186.14.4829-4833.2004, 2004, https://doi.org/10.1128/jb.186.14.4829-4833.2004 | Important boundary case: reverse gyrase not universally essential at 90 °C. Mark as taxon-specific and temperature-threshold dependent. |
| Heat shock / temperature up-shift | increases | positive supercoils in plasmid DNA (label-only) | “heat shock increases positive supercoils in plasmid DNA” (takemata2024howdothermophiles pages 1-2) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087 | Evidence from Sulfolobus; supports environmental-factor node. |
| TopR1 reverse gyrase | mediates response to | heat shock-induced positive supercoiling (label-only) | increase in positive supercoils “coincides with the augmented activity of TopR1 upon the temperature up-shift” (takemata2024howdothermophiles pages 1-2) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087 | Taxon-specific paralog edge for Sulfolobus. |
| Archaeal ether/tetraether lipids (CHEBI grounding unclear; label-only) | maintain | membrane integrity at high temperature (GO:0016020 related; label-only) | archaeal membranes have “ether linkages” and “contain tetraethers and diethers,” linked to ability to withstand “membrane-destroying temperatures” (irwin2004extremophilesandtheir pages 2-3) | 10.1186/2046-0481-57-6-348, 2004, https://doi.org/10.1186/2046-0481-57-6-348 | Broad but classic mechanism; exact lipid classes should be grounded later. |
| Higher growth temperature | increases proportion of | membrane-spanning GDGTs (label-only) | “hyperthermophilic methanogens increase membrane-spanning GDGT content at higher temperatures” (rao2024unravelingthemultiplicity pages 2-4) | 10.1007/s00792-023-01330-2, 2024, https://doi.org/10.1007/s00792-023-01330-2 | Good membrane-remodeling edge; taxon scope currently methanogens. |
| GrsA/GrsB cyclization enzymes | increase | membrane packing and stability (label-only) | “cyclized GDGTs (introduced by GrsA/GrsB) increase membrane packing and stability” (rao2024unravelingthemultiplicity pages 1-2) | 10.1007/s00792-023-01330-2, 2024, https://doi.org/10.1007/s00792-023-01330-2 | Strong mechanistic membrane edge; gene/protein IDs still needed. |
| Geranylgeranyl reductase (GGR) | saturates | isoprene chains of phospholipids (label-only) | “GGRs… are responsible for saturation of isoprene chains of phospholipids” (rao2024unravelingthemultiplicity pages 1-2) | 10.1007/s00792-023-01330-2, 2024, https://doi.org/10.1007/s00792-023-01330-2 | Mechanistic biosynthesis edge; direct causal link to extreme hyperthermophily is inferred rather than experimentally shown here. |
| Thermosome / chaperone complex (GO:0005832 chaperonin-containing T-complex-like candidate) | supports | protein folding/conformation at upper growth limit (GO:0006457) | in Pyrodictium occultum, “~80% of soluble protein is a chaperone complex” near upper growth limit; thermosome “maintains protein conformation” (irwin2004extremophilesandtheir pages 2-3) | 10.1186/2046-0481-57-6-348, 2004, https://doi.org/10.1186/2046-0481-57-6-348 | Strong but organism-specific and older evidence. |
| Polyphosphate (CHEBI:18367) | prevents | protein aggregation / precipitation (GO:0035966 related; label-only) | “polyP functioning as an inorganic molecular chaperone… reduced protein precipitation under copper stress” (acevedolopez2024roleofpolyphosphate pages 1-2) | 10.3390/microorganisms12122627, 2024, https://doi.org/10.3390/microorganisms12122627 | Strong evidence, but under copper stress rather than heat alone; relevance to thermophily is indirect. |
| Polyphosphate (CHEBI:18367) | supports upregulation of | chaperonins (label-only) | “upregulation of all measured chaperonins when polyP is present” (acevedolopez2024roleofpolyphosphate pages 1-2) | 10.3390/microorganisms12122627, 2024, https://doi.org/10.3390/microorganisms12122627 | Stress-response edge in thermophilic archaeon; assay-specific. |
| Nucleoid-associated proteins / polyamines (label-only) | enhance | DNA thermostability (label-only) | “NAPs and polyamines… have been implicated in enhancing DNA thermostability” (takemata2024howdothermophiles pages 1-2) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087 | Broad review claim; should be marked uncertain until more direct primary evidence is added. |
| Polyamines (CHEBI:88061 class) | stabilize | DNA and RNA (CHEBI:16991, CHEBI:33697) | “polyamine molecule… performs various cellular functions, such as DNA and RNA stabilization” and “thermospermine are found in thermophiles that survive at extremely high…” (carbonaroUnknownyearextremophilesasmicrobial pages 12-17) | 10.3390/molecules28083446, 2023, https://doi.org/10.3390/molecules28083446 | Indirect review-context support; not specific to one hyperthermophile experiment. Mark uncertain. |
| Extreme hyperthermophilic growth range (METPO:1000721) | exemplified by | Pyrolobus fumarii (NCBITaxon:43335 candidate) | “Pyrolobus fumarii has ‘an upper temperature limit for growth of 113°C, and it cannot grow below 90°C’” (irwin2004extremophilesandtheir pages 1-2) | 10.1186/2046-0481-57-6-348, 2004, https://doi.org/10.1186/2046-0481-57-6-348 | Phenotype-defining edge for trait scope, not a mechanism per se. |


*Table: This table compiles candidate mechanistic and phenotype-defining causal edges for the extreme hyperthermophilic trait using only available cited context IDs. It is designed to support TraitMech curation by pairing each proposed edge with a quote, source, and uncertainty note.*

### Warnings / curation cautions (do not over-curate)
1. **Reverse gyrase essentiality is not universal at 90 °C.** Primary data show growth at 90 °C without reverse gyrase in one hyperthermophile (atomi2004reversegyraseis pages 3-5), while other data show lethal phenotypes at ≥95 °C (lipscomb2017reversegyraseis pages 1-2). Curate edges with explicit temperature qualifiers or as taxon-scoped.
2. **Polyphosphate evidence is stress-context specific.** The 2024 polyP study is under copper stress; relevance to thermal stress is mechanistically plausible but indirect (acevedolopez2024roleofpolyphosphate pages 1-2). Mark edges as “stress-proteostasis” rather than “heat-only.”
3. **Polyamines/NAPs edges are broad.** The 2024 review implicates NAPs and polyamines in DNA thermostability (takemata2024howdothermophiles pages 1-2) but the provided evidence here is review-level; mark as uncertain until direct primary evidence in extreme hyperthermophiles is added.
4. **Membrane lipid identifiers need grounding.** GDGT and cyclized GDGT are mechanistically supported (rao2024unravelingthemultiplicity pages 2-4, rao2024unravelingthemultiplicity pages 1-2) but require careful chemical ontology mapping before final YAML curation.

### DOI-first bibliography (with publication date and URL)
- Takemata N. (2024-06). *How Do Thermophiles Organize Their Genomes?* **Microbes and Environments**. DOI: 10.1264/jsme2.me23087. URL: https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles media 3c170b13)
- Rao A, Driessen AJM. (2024-01). *Unraveling the multiplicity of geranylgeranyl reductases in Archaea: potential roles in saturation of terpenoids.* **Extremophiles**. DOI: 10.1007/s00792-023-01330-2. URL: https://doi.org/10.1007/s00792-023-01330-2 (rao2024unravelingthemultiplicity pages 2-4, rao2024unravelingthemultiplicity pages 1-2)
- Acevedo-López J, González-Madrid G, Navarro CA, Jerez CA. (2024-12). *Role of Polyphosphate as an Inorganic Chaperone to Prevent Protein Aggregation Under Copper Stress in Saccharolobus solfataricus.* **Microorganisms**. DOI: 10.3390/microorganisms12122627. URL: https://doi.org/10.3390/microorganisms12122627 (acevedolopez2024roleofpolyphosphate pages 1-2)
- Mondal N et al. (2024-10). *Aquificae overcomes competition… to dominate the boiling vent-water…* **PLOS ONE**. DOI: 10.1371/journal.pone.0310595. URL: https://doi.org/10.1371/journal.pone.0310595 (mondal2024aquificaeovercomescompetition pages 1-2, mondal2024aquificaeovercomescompetition pages 35-36)
- Kuschmierz L et al. (2024-11). *5′-untranslated region sequences enhance plasmid-based protein production in Sulfolobus acidocaldarius.* **Frontiers in Microbiology**. DOI: 10.3389/fmicb.2024.1443342. URL: https://doi.org/10.3389/fmicb.2024.1443342 (kuschmierz20245′untranslatedregionsequences pages 1-2)
- Ali N, Nughman M, Shah SM. (2023-05). *Extremophiles and Limits of Life in a Cosmic Perspective.* (Book chapter). DOI: 10.5772/intechopen.110471. URL: https://doi.org/10.5772/intechopen.110471 (ali2023extremophilesandlimits pages 1-3, ali2023extremophilesandlimits pages 3-4)
- Dumina M, Zhgun A. (2023-01). *Thermo-L-Asparaginases…* **International Journal of Molecular Sciences**. DOI: 10.3390/ijms24032674. URL: https://doi.org/10.3390/ijms24032674 (dumina2023thermolasparaginasesfromthe pages 2-4)

Foundational / mechanistic (older but directly causal)
- Lipscomb GL et al. (2017-03). *Reverse gyrase is essential for microbial growth at 95 °C.* **Extremophiles**. DOI: 10.1007/s00792-017-0929-z. URL: https://doi.org/10.1007/s00792-017-0929-z (lipscomb2017reversegyraseis pages 1-2, lipscomb2017reversegyraseis pages 2-4)
- Kampmann M, Stock D. (2004-07). *Reverse gyrase has heat-protective DNA chaperone activity independent of supercoiling.* **Nucleic Acids Research**. DOI: 10.1093/nar/gkh683. URL: https://doi.org/10.1093/nar/gkh683 (kampmann2004reversegyrasehas pages 1-2)
- Atomi H et al. (2004-07). *Reverse gyrase is not a prerequisite for hyperthermophilic life.* **Journal of Bacteriology**. DOI: 10.1128/jb.186.14.4829-4833.2004. URL: https://doi.org/10.1128/jb.186.14.4829-4833.2004 (atomi2004reversegyraseis pages 3-5)
- Irwin JA, Baird AW. (2004-06). *Extremophiles and their application to veterinary medicine.* **Irish Veterinary Journal**. DOI: 10.1186/2046-0481-57-6-348. URL: https://doi.org/10.1186/2046-0481-57-6-348 (irwin2004extremophilesandtheir pages 1-2, irwin2004extremophilesandtheir pages 2-3, irwin2004extremophilesandtheir pages 5-6, irwin2004extremophilesandtheir pages 3-5)

### Notes for YAML curation (mapping to `data/traits/environment/extreme_hyperthermophilic.yaml`)
- Represent the trait as **Topt >90 °C**, with optional measured properties: Tmin/Tmax boundaries where available (e.g., *P. fumarii* Tmin 90 °C; Tmax 113 °C) (irwin2004extremophilesandtheir pages 1-2).
- Prioritize mechanistic modules with direct causal evidence in extreme ranges: **reverse gyrase → growth at ≥95 °C** (lipscomb2017reversegyraseis pages 1-2) and **reverse gyrase → DNA protection at 90 °C independent of supercoiling** (kampmann2004reversegyrasehas pages 1-2).
- Include membrane stabilization nodes/edges with recent mechanistic specificity (GDGT proportion shifts; GrsA/GrsB cyclization) (rao2024unravelingthemultiplicity pages 2-4, rao2024unravelingthemultiplicity pages 1-2).
- Add proteostasis nodes/edges (thermosome; polyP) with stress-context annotation (irwin2004extremophilesandtheir pages 2-3, acevedolopez2024roleofpolyphosphate pages 1-2).


References

1. (irwin2004extremophilesandtheir pages 1-2): Jane A Irwin and Alan W Baird. Extremophiles and their application to veterinary medicine. Irish Veterinary Journal, 57:348-354, Jun 2004. URL: https://doi.org/10.1186/2046-0481-57-6-348, doi:10.1186/2046-0481-57-6-348. This article has 69 citations and is from a peer-reviewed journal.

2. (atomi2004reversegyraseis pages 3-5): Haruyuki Atomi, Rie Matsumi, and Tadayuki Imanaka. Reverse gyrase is not a prerequisite for hyperthermophilic life. Journal of Bacteriology, 186:4829-4833, Jul 2004. URL: https://doi.org/10.1128/jb.186.14.4829-4833.2004, doi:10.1128/jb.186.14.4829-4833.2004. This article has 164 citations and is from a peer-reviewed journal.

3. (lipscomb2017reversegyraseis pages 1-2): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 43 citations and is from a peer-reviewed journal.

4. (takemata2024howdothermophiles pages 1-2): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

5. (irwin2004extremophilesandtheir pages 2-3): Jane A Irwin and Alan W Baird. Extremophiles and their application to veterinary medicine. Irish Veterinary Journal, 57:348-354, Jun 2004. URL: https://doi.org/10.1186/2046-0481-57-6-348, doi:10.1186/2046-0481-57-6-348. This article has 69 citations and is from a peer-reviewed journal.

6. (rao2024unravelingthemultiplicity pages 2-4): Alka Rao and Arnold J. M. Driessen. Unraveling the multiplicity of geranylgeranyl reductases in archaea: potential roles in saturation of terpenoids. Extremophiles, Jan 2024. URL: https://doi.org/10.1007/s00792-023-01330-2, doi:10.1007/s00792-023-01330-2. This article has 3 citations and is from a peer-reviewed journal.

7. (rao2024unravelingthemultiplicity pages 1-2): Alka Rao and Arnold J. M. Driessen. Unraveling the multiplicity of geranylgeranyl reductases in archaea: potential roles in saturation of terpenoids. Extremophiles, Jan 2024. URL: https://doi.org/10.1007/s00792-023-01330-2, doi:10.1007/s00792-023-01330-2. This article has 3 citations and is from a peer-reviewed journal.

8. (acevedolopez2024roleofpolyphosphate pages 1-2): José Acevedo-López, Gabriela González-Madrid, Claudio A. Navarro, and Carlos A. Jerez. Role of polyphosphate as an inorganic chaperone to prevent protein aggregation under copper stress in saccharolobus solfataricus. Microorganisms, 12:2627, Dec 2024. URL: https://doi.org/10.3390/microorganisms12122627, doi:10.3390/microorganisms12122627. This article has 4 citations.

9. (mondal2024aquificaeovercomescompetition pages 1-2): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19(10):e0310595, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 11 citations and is from a peer-reviewed journal.

10. (irwin2004extremophilesandtheir pages 3-5): Jane A Irwin and Alan W Baird. Extremophiles and their application to veterinary medicine. Irish Veterinary Journal, 57:348-354, Jun 2004. URL: https://doi.org/10.1186/2046-0481-57-6-348, doi:10.1186/2046-0481-57-6-348. This article has 69 citations and is from a peer-reviewed journal.

11. (irwin2004extremophilesandtheir pages 5-6): Jane A Irwin and Alan W Baird. Extremophiles and their application to veterinary medicine. Irish Veterinary Journal, 57:348-354, Jun 2004. URL: https://doi.org/10.1186/2046-0481-57-6-348, doi:10.1186/2046-0481-57-6-348. This article has 69 citations and is from a peer-reviewed journal.

12. (ali2023extremophilesandlimits pages 3-4): Nawab Ali, Muhammad Nughman, and Syed Majid Shah. Extremophiles and limits of life in a cosmic perspective. Life in Extreme Environments - Diversity, Adaptability and Valuable Resources of Bioactive Molecules, May 2023. URL: https://doi.org/10.5772/intechopen.110471, doi:10.5772/intechopen.110471. This article has 13 citations.

13. (ali2023extremophilesandlimits pages 1-3): Nawab Ali, Muhammad Nughman, and Syed Majid Shah. Extremophiles and limits of life in a cosmic perspective. Life in Extreme Environments - Diversity, Adaptability and Valuable Resources of Bioactive Molecules, May 2023. URL: https://doi.org/10.5772/intechopen.110471, doi:10.5772/intechopen.110471. This article has 13 citations.

14. (dumina2023thermolasparaginasesfromthe pages 2-4): M. Dumina and A. Zhgun. Thermo-l-asparaginases: from the role in the viability of thermophiles and hyperthermophiles at high temperatures to a molecular understanding of their thermoactivity and thermostability. International Journal of Molecular Sciences, Jan 2023. URL: https://doi.org/10.3390/ijms24032674, doi:10.3390/ijms24032674. This article has 25 citations.

15. (kuschmierz20245′untranslatedregionsequences pages 1-2): Laura Kuschmierz, Alexander Wagner, Christian Schmerling, Tobias Busche, Jörn Kalinowski, Christopher Bräsen, and Bettina Siebers. 5′-untranslated region sequences enhance plasmid-based protein production in sulfolobus acidocaldarius. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1443342, doi:10.3389/fmicb.2024.1443342. This article has 6 citations and is from a peer-reviewed journal.

16. (lipscomb2017reversegyraseis pages 2-4): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 43 citations and is from a peer-reviewed journal.

17. (mondal2024aquificaeovercomescompetition pages 35-36): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19(10):e0310595, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 11 citations and is from a peer-reviewed journal.

18. (kampmann2004reversegyrasehas pages 1-2): M. Kampmann and D. Stock. Reverse gyrase has heat-protective dna chaperone activity independent of supercoiling. Nucleic acids research, 32 12:3537-45, Jul 2004. URL: https://doi.org/10.1093/nar/gkh683, doi:10.1093/nar/gkh683. This article has 108 citations and is from a highest quality peer-reviewed journal.

19. (carbonaroUnknownyearextremophilesasmicrobial pages 12-17): M Carbonaro. Extremophiles as microbial tools to face environmental problems associated to anthropogenic activities. Unknown journal, Unknown year.

20. (takemata2024howdothermophiles media 3c170b13): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.