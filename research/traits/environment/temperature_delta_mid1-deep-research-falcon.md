---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:36:00.386025'
end_time: '2026-08-04T03:45:14.271283'
duration_seconds: 553.89
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature delta mid1
  trait_identifier: METPO:1000485
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_delta_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature delta phenotype with a growth-supporting temperature\
    \ breadth of approximately 10\u201320 \xB0C, characteristic of organisms with\
    \ moderate thermal-tolerance breadth."
  parent_traits: METPO:1000303
  synonyms: Td_10_20
  evidence_summary: 'DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty
    acids (Membrane-adaptation review supports moderate homoviscous remodeling capacity
    as common among generalist mesophiles.)'
  causal_graph_summary: 'temperature_delta_mid1_moderate_breadth: 11 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000485
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 10–20 °C, characteristic of organisms with moderate thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_10_20
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports moderate homoviscous remodeling capacity as common among generalist mesophiles.)
- **Existing causal graph summary:** temperature_delta_mid1_moderate_breadth: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid1.yaml`.

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
- **Trait label:** temperature delta mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000485
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 10–20 °C, characteristic of organisms with moderate thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_10_20
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports moderate homoviscous remodeling capacity as common among generalist mesophiles.)
- **Existing causal graph summary:** temperature_delta_mid1_moderate_breadth: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid1.yaml`.

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


# Curation report: temperature delta mid1

## Executive summary

**Trait:** temperature delta mid1  
**Identifier:** **METPO:1000485**  
**Synonym:** Td_10_20  
**Parent:** METPO:1000303  
**Proposed operational meaning:** a microbial strain supports measurable growth over an approximately **10–20 °C interval**, calculated as **Tmax − Tmin**, under one explicitly defined assay condition.

The literature defines thermal tolerance as “the temperature range within which a species can grow.” Accordingly, METPO:1000485 should represent a **growth-range phenotype**, not optimum temperature, environmental temperature at isolation, presence across field samples, or survival after an acute heat/cold shock (he2023highspeciationrate pages 1-2). The strongest general mechanism relevant to the lower end of such a range is homeoviscous membrane adaptation. The strongest upper-end mechanisms are protein-quality-control systems, especially GroEL/GroES and DnaK/DnaJ. However, no located study directly establishes that any single mechanism causes the specific **10–20 °C breadth class**. The final connection from endpoint mechanisms to METPO:1000485 must therefore remain an inferred graph-level hypothesis.

## 1. Trait scope and boundaries

### 1.1 Recommended phenotype definition

For curation, define:

> **temperature delta = highest tested temperature supporting growth − lowest tested temperature supporting growth**, with a value from approximately 10 through 20 °C.

“Growth supporting” should require an assay-level criterion such as a reproducible increase in optical density, biomass, cell count, colony-forming units, or substrate-linked biomass production after inoculation. Record medium, pH, salinity, oxygen status, incubation time, inoculum history, and temperature-step resolution. These variables can move apparent Tmin or Tmax and therefore alter the assigned breadth.

A 2023 hot-spring study treated thermal niche breadth as an occurrence distribution across 54.8–80 °C and classified taxa detected at one temperature as temperature-sensitive and taxa detected at at least five temperatures as resistant/generalist. This is useful ecological evidence, but it is not equivalent to axenic growth limits because abundance, dispersal, interactions, and detection thresholds affect occurrence (he2023highspeciationrate pages 2-4, he2023highspeciationrate pages 1-2).

### 1.2 Boundary cases

- **Narrower neighboring trait:** ΔT below approximately 10 °C; exclude from METPO:1000485.
- **Broader neighboring trait:** ΔT above approximately 20 °C; exclude even if the organism is a mesophile.
- **Endpoint location:** a 10–20 °C breadth can occur around cold, moderate, or warm optima. Breadth does not by itself imply mesophily.
- **Acute survival:** viability after minutes of heat or cold exposure is not growth over the temperature interval.
- **Lag-only response:** transient growth arrest after a temperature shift does not establish a new Tmin or Tmax.
- **Field occupancy:** detection at several environmental temperatures estimates realized niche breadth, not necessarily fundamental growth breadth.
- **Condition-dependent breadth:** oxygen, nutrient composition, salinity, pressure, pH, and host association must be represented as assay or environmental context rather than silently pooled.

### 1.3 Current interpretation

Moderate breadth is best modeled as the intersection of at least two physiological capacities:

1. **Lower-end capacity:** preservation of membrane function, RNA metabolism, translation, and enzyme activity as temperature falls.
2. **Upper-end capacity:** preservation of proteostasis, membrane/envelope integrity, translation, DNA maintenance, and redox homeostasis as temperature rises.

Thermal generalism can also entail a performance trade-off. In hot-spring communities, wide-niche taxa showed niche expansion but poorer local performance—the “jack-of-all-trades, master-of-none” pattern (he2023highspeciationrate pages 1-2). Evolved heat-resistant *E. coli* likewise reached higher maximum temperatures but had decreased fitness at 37 °C (rudolph2010evolutionofescherichia pages 4-5).

## 2. Candidate graph nodes

Identifiers below are conservative suggestions. Label-only nodes are preferable where a strain-specific protein lacks a verified database accession.

### 2.1 Trait and assay nodes

- **temperature delta mid1** — **METPO:1000485**
- temperature delta / growth-temperature breadth — parent supplied as **METPO:1000303**
- minimum growth temperature, Tmin — label-only assay endpoint
- maximum growth temperature, Tmax — label-only assay endpoint
- growth rate, biomass increase, CFU increase — assay-observed variables
- temperature downshift; temperature upshift; chronic growth temperature; acute thermal shock — separate experimental-factor nodes
- culture medium, oxygen availability, salinity, pH, pressure, incubation duration — context nodes

### 2.2 Cellular structures and biophysical states

- cytoplasmic membrane — **GO:0005886**
- membrane lipid bilayer — label or appropriate GO cellular-component term after ontology validation
- membrane fluidity; membrane order; gel-state transition; lipid-packing density; membrane thickness — label-only biophysical nodes
- protein condensate / stress granule — eukaryotic-microbial comparative node; use cautiously

### 2.3 Lipids, chemicals, and metabolites

- unsaturated fatty acid — **CHEBI:27283**
- saturated fatty acid — **CHEBI:26607**
- branched-chain fatty acid — label-only unless a specific molecule is intended
- phosphatidylethanolamine — **CHEBI:16038**
- phosphatidylcholine — **CHEBI:64482**
- trehalose — **CHEBI:27082**
- ectoine — **CHEBI:14257**
- hydroxyectoine — validate the exact ChEBI accession before use
- reactive oxygen species — **CHEBI:26523**
- hydrogen peroxide — **CHEBI:16240**
- ATP — **CHEBI:15422**

The 2024 membrane review reports that low temperature/high pressure favor unsaturated, branched, and short-chain fatty acids, which prevent fatal ordered-gel transitions. It also notes unresolved details, including the biochemical basis of cold-induced chain shortening (maiti2024extrememakeoverthe pages 3-4).

### 2.4 Genes, proteins, enzymes, and complexes

**Lower-temperature membrane module**

- DesK membrane histidine kinase — label-only unless organism-specific accession is supplied
- DesR response regulator — label-only
- des acyl-lipid desaturase — label-only; molecular function can be linked to **GO:0016717** only after checking substrate-specific applicability
- Hik33 cold-sensor kinase — cyanobacterial, taxon-specific
- branched-chain fatty-acid biosynthesis machinery — pathway/module node

**Proteostasis and upper-temperature module**

- GroEL/GroES chaperonin complex — protein-complex label; **GO:0006457** for protein folding
- DnaK/DnaJ/GrpE chaperone system — protein-complex/module label
- ClpB disaggregase — label-only protein node
- HtpG — label-only protein node
- LysU lysyl-tRNA synthetase — enzyme/protein node; organism-specific grounding recommended
- protein folding — **GO:0006457**
- response to heat — **GO:0009408**
- protein refolding — **GO:0042026**

**Cold RNA/translation candidates**

- cold-shock proteins/Csp family — label-only family node
- CsdA/DEAD-box RNA helicase — label-only unless accession is specified
- trigger factor/Tig — label-only
- RNA secondary-structure remodeling; ribosome biogenesis; RNA degradation — process nodes

RNA helicases plausibly support cold growth by resolving stabilized RNA structures and contributing to cold-adapted ribosomes and degradosomes, but the retrieved evidence did not directly connect these proteins to a measured 10–20 °C breadth. Keep them provisional.

**Compatible-solute candidates**

- OtsA/OtsB trehalose-biosynthesis module
- EctA/EctB/EctC ectoine-biosynthesis module
- EctD hydroxyectoine synthesis
- EctT compatible-solute transporter

These are credible temperature-stress protectants, but much of the evidence concerns viability, osmotic interaction, or individual thermal endpoints rather than measured breadth.

### 2.5 Biological processes and pathways

- homeoviscous adaptation — label-only pathway/process node
- unsaturated-fatty-acid biosynthesis — **GO:0006636**
- two-component signal transduction — **GO:0000160**
- response to cold — **GO:0009409**
- response to oxidative stress — **GO:0006979**
- cellular redox homeostasis — **GO:0045454**
- protein-quality control — label or validated GO term
- compatible-solute accumulation — label-only process
- growth at low temperature; growth at critical high temperature — phenotype/process nodes

## 3. Candidate causal edges

The table below separates directly supported mechanisms from associations and breadth-level inference.

| subject | predicate | object | evidence class | taxon/context | DOI | short exact or near-exact supporting snippet | curation recommendation |
|---|---|---|---|---|---|---|---|
| temperature downshift | increases | membrane ordering / nonfluid state | direct mechanism | bacteria, review synthesis with Bacillus examples | 10.1146/annurev-micro-091313-103612 | "When temperature decreases, membrane lipids shift from a fluid to nonfluid state" (mendoza2014temperaturesensingby pages 6-8) | Curate as generic mechanism node/edge for low-temperature adaptation; not specific to breadth bin alone |
| membrane ordering / reduced fluidity | activates | DesK sensor kinase | direct mechanism | *Bacillus subtilis* DesK/DesR system | 10.1146/annurev-micro-091313-103612 | "membrane fluidity, not temperature per se, controls des transcription" and ordered membranes activate des expression even at 37°C (mendoza2014temperaturesensingby pages 5-6) | Curate, but mark taxon-specific to DesK-bearing lineages |
| DesK | phosphorylates | DesR | direct mechanism | *Bacillus subtilis* | 10.1146/annurev-micro-091313-103612 | "DesK autophosphorylation ... phosphorylates the response regulator DesR" (mendoza2014temperaturesensingby pages 6-8) | Curate for DesK/DesR module; taxon-specific |
| DesR-P | activates expression of | des desaturase gene | direct mechanism | *Bacillus subtilis* | 10.1146/annurev-micro-091313-103612 | "Phosphorylated DesR-P binds DNA and activates des gene expression" (mendoza2014temperaturesensingby pages 5-6) | Curate for organisms with demonstrated DesR-controlled des |
| acyl-lipid desaturase / des | increases abundance of | unsaturated fatty acids | direct mechanism | bacteria; *Bacillus* examples | 10.1146/annurev-micro-091313-103612 | "desaturase enzymes ... introduce double bonds into saturated fatty acids to create unsaturated fatty acids (UFAs)" (mendoza2014temperaturesensingby pages 4-5) | Curate |
| unsaturated fatty acids | increase | membrane fluidity / decrease packing order | direct mechanism | broad microbial membrane adaptation | 10.1146/annurev-micro-091313-103612 | "incorporation of proportionally more unsaturated fatty acids ... disrupt the order of the lipid bilayer" (mendoza2014temperaturesensingby pages 1-2) | Curate |
| branched-chain fatty acids | support | membrane fluidity at low temperature | direct mechanism | *Bacillus subtilis* and related bacteria | 10.1146/annurev-micro-091313-103612 | "Both α-branched chain fatty acids and unsaturated fatty acids are required for cell growth at low temperatures" (mendoza2014temperaturesensingby pages 6-8) | Curate, but wording should reflect support of low-temp growth via fluidity homeostasis |
| membrane fluidity homeostasis | supports | low-temperature physiological performance / growth | direct mechanism | broad bacterial adaptation | 10.1146/annurev-micro-091313-103612 | HVA "optimizes the performance of a large array of cellular physiological processes at the new temperature" (mendoza2014temperaturesensingby pages 1-2) | Curate as higher-level process edge; breadth relevance still indirect |
| GroEL/GroES | enables | high-temperature growth | direct growth | thermoresistant *Escherichia coli* evolved to 48.5°C | 10.1074/jbc.M110.103374 | "only exquisitely high GroEL/GroES levels are essential for growth at 48.5 °C" (rudolph2010evolutionofescherichia pages 1-2) | Curate with upper-temperature-growth context; not breadth-specific |
| lysU | required for | thermoresistant growth at high temperature | direct growth | thermoresistant *Escherichia coli* evolved to 48.5°C | 10.1074/jbc.M110.103374 | "deletion of lysU rendered thermoresistant cells thermosensitive" (rudolph2010evolutionofescherichia pages 1-2) | Curate with strong taxon/context qualifier |
| DnaK/DnaJ | required for | growth at critical high temperature (47°C) | direct growth | *Escherichia coli* knockout screen | 10.1371/journal.pone.0020063 | "dnaJ and dnaK ... were indispensable for growth at 47°C" (murata2011molecularstrategyfor pages 1-2) | Curate for upper-end tolerance module |
| oxidative-stress resistance | associated with | critical-high-temperature growth | correlative | *Escherichia coli* thermotolerant gene set | 10.1371/journal.pone.0020063 | "More than half of the mutants of the thermotolerant genes were found to be sensitive to H2O2 at 30°C" (murata2011molecularstrategyfor pages 1-2) | Curate only as uncertain/association; not a direct causal breadth edge |
| Pab1 condensation threshold / adaptive biomolecular condensation | correlates with | species thermal niche | correlative | three budding yeasts adapted to different thermal niches | 10.1038/s41467-024-47355-9 | "Pab1 from each species condensed at a temperature ... correlated with both the optimal and maximum growth temperatures" (kik2024anadaptivebiomolecular pages 5-6) | Do not curate into bacterial TraitMech core unless explicitly allowing broad microbial/eukaryotic comparative evidence |
| heat-shock-triggered protein condensation | is tuned to | adapted temperature niche | correlative | budding yeasts | 10.1038/s41467-024-47355-9 | "condensation is not only conserved ... but it is tuned to their adapted temperature niche" (kik2024anadaptivebiomolecular pages 5-6) | Keep as contextual expert-analysis evidence, not core bacterial mechanism |
| combined lower-end membrane/RNA/proteostasis modules and upper-end chaperone/oxidative-stress modules | contributes to | temperature breadth of ~10–20°C | inferred | cross-taxon synthesis for METPO:1000485 | 10.1146/annurev-micro-091313-103612; 10.1074/jbc.M110.103374; 10.1371/journal.pone.0020063; 10.1038/s41467-024-47355-9 | Near-exact support is distributed across sources; no source directly tests the 10–20°C breadth bin itself (mendoza2014temperaturesensingby pages 1-2, rudolph2010evolutionofescherichia pages 1-2, murata2011molecularstrategyfor pages 1-2, kik2024anadaptivebiomolecular pages 5-6) | Do not curate directly as a single edge; use only as graph-design hypothesis |
| thermal tolerance | defined as | temperature range within which a species can grow | direct definition | microbial thermal niche ecology | 10.1038/s41396-023-01447-4 | "thermal tolerance (the temperature range within which a species can grow)" (he2023highspeciationrate pages 1-2) | Use for trait scope metadata, not causal graph edge |


*Table: This table summarizes candidate mechanistic and correlative edges relevant to METPO:1000485, with direct supporting snippets and curation recommendations. It is designed to separate curatable mechanism from broader, uncertain, or breadth-level inferences.*

### 3.1 Recommended core subgraph

A defensible first-pass core is:

1. **temperature downshift → increases → membrane ordering**
2. **membrane ordering → activates → DesK**
3. **DesK → phosphorylates → DesR**
4. **DesR-P → activates expression of → des**
5. **Des desaturase → increases → unsaturated fatty acids**
6. **unsaturated fatty acids → increase → membrane fluidity**
7. **membrane-fluidity homeostasis → supports → low-temperature growth/physiological performance**
8. **GroEL/GroES → supports → upper-temperature growth**
9. **DnaK/DnaJ → supports → upper-temperature growth**

In *Bacillus subtilis*, a 37→20 °C shift induces UFA synthesis; DesK autophosphorylation rises approximately 50-fold, DesR activates des, and restored membrane fluidity shuts down signaling through DesK phosphatase activity. Ordered membranes can activate des even at constant 37 °C, demonstrating that the proximate signal is membrane physical state rather than temperature alone (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 4-5, mendoza2014temperaturesensingby pages 6-8).

The lipid output has substantial quantitative support. *Bacillus megaterium* palmitate was almost completely desaturated at 23 °C but negligibly desaturated at 30 °C. In a cold/freeze–thaw membrane example summarized in 2024, cultures shifted from an initial composition of about 70% saturated and 30% unsaturated fatty acids to more than 85% unsaturated fatty acids (mendoza2014temperaturesensingby pages 4-5, maiti2024extrememakeoverthe pages 4-5).

For the upper endpoint, evolved *E. coli* achieved sustained growth at 48.5 °C, 3 °C above the wild-type maximum in LB. GroEL/GroES levels were approximately 16-fold above baseline and essential; deletion of lysU reversed thermoresistance (rudolph2010evolutionofescherichia pages 1-2). A separate genome-wide screen identified 51 genes required for growth at 47 °C, including dnaK and dnaJ, and implicated envelope organization, DNA repair, tRNA modification, protein quality control, translation control, and cell division (murata2011molecularstrategyfor pages 1-2).

### 3.2 Optional contextual subgraph

A 2024 yeast study found that proteome-scale biomolecular condensation and purified Pab1 condensation thresholds tracked species-specific thermal niches, optimum growth temperatures, and maximum growth temperatures. The response appears adaptive and evolutionarily tuned, but it is correlational for niche breadth and belongs to eukaryotic microbes, not the bacterial DesK graph (kik2024anadaptivebiomolecular pages 5-6, kik2024anadaptivebiomolecular pages 1-2). It should be retained as comparative context rather than merged into a universal microbial core.

## 4. Recent developments and applications

### 4.1 Recent research, 2023–2024

- **Thermal niche ecology (2023):** Hot-spring communities spanning 54.8–80 °C showed distinct specialist/generalist evolutionary dynamics. Broad occurrence was associated with niche expansion but high extinction and poorer local performance, emphasizing that breadth has ecological costs (he2023highspeciationrate pages 1-2).
- **Membrane adaptation synthesis (2024):** Current analysis emphasizes both fluidity and lipid-packing density as possible sensed variables. The review regards homeoviscous adaptation as broadly conserved but states that how sensors collaborate to maintain membrane physicochemical properties remains incompletely resolved (maiti2024extrememakeoverthe pages 3-4).
- **Adaptive protein condensation (2024):** Across three budding yeasts, thermal-niche-specific growth, transcription, and protein condensation responses were coordinated. Pab1 temperature sensitivity was substantially encoded by protein sequence (kik2024anadaptivebiomolecular pages 5-6, kik2024anadaptivebiomolecular pages 1-2).
- **Trade-offs in thermal adaptation (2024):** Selection for severe heat-shock survival in *Salmonella* can favor dnaJ loss-of-function, but this reduces growth at 37 °C and above. This reinforces the crucial distinction between acute shock resistance and sustained high-temperature growth.

### 4.2 Real-world relevance

- **Industrial fermentation:** Membrane remodeling and chaperone capacity affect process robustness during imperfect temperature control. The graph may guide strain selection or engineering, but optimization at one endpoint can reduce performance near the optimum.
- **Food safety:** Acute heat resistance does not necessarily predict growth at warm temperatures. Assays used to assess processing survival should not be used directly to annotate growth-temperature breadth.
- **Wastewater biotechnology:** Temperature adaptation of specialized organisms such as anammox bacteria can determine reactor operating envelopes; recent work links high-temperature adaptation with chaperone induction and membrane-lipid remodeling, although such mechanisms are taxon-specific.
- **Climate-response modeling:** Growth-range phenotypes are more informative than single optimum temperatures when forecasting persistence under variable thermal regimes. Field occurrence nevertheless remains confounded by dispersal and biotic interactions.
- **Astrobiology and bioprospecting:** Homeoviscous and osmolyte-mediated adaptation are used as mechanistic models for persistence under environmental extremes and for identifying robust enzymes or cellular chassis (maiti2024extrememakeoverthe pages 1-2).

## 5. Expert assessment

The evidence supports a **modular rather than single-gene explanation**. Membrane remodeling is a strong lower-temperature mechanism, whereas chaperone-mediated proteostasis and other quality-control systems support the upper endpoint. A moderate breadth probably emerges when these modules cover overlapping temperatures without the energetic or performance costs required for extreme generalism.

The 10–20 °C category is nevertheless a discretization imposed on a continuous thermal-performance curve. A graph should avoid implying that DesK, des, GroEL, or DnaK specifically produces the “mid1” bin. These mechanisms can shift Tmin or Tmax in multiple breadth classes. The trait assignment should be made from measured growth endpoints; mechanism nodes explain those endpoints only after strain- and assay-specific validation.

## 6. Curation warnings

1. **Do not curate** `homeoviscous adaptation → causes → METPO:1000485` as a direct edge. It supports low-temperature function but does not establish the exact breadth bin.
2. **Do not equate shock survival with growth.** Trehalose restored low-temperature viability in an *E. coli* otsA context, but the mutant grew normally at 16 °C and the principal defect was viability at 4 °C; this is endpoint survival evidence (weber2003bacterialcoldshock pages 36-38).
3. **Do not generalize DesK/DesR universally.** It is a well-resolved *Bacillus* mechanism; other taxa use different sensors, including cyanobacterial Hik33 (mendoza2014temperaturesensingby pages 6-8).
4. **Do not assume all chaperone increases are beneficial at all temperatures.** Artificial GroEL/GroES enhancement can reduce low-temperature viability, while high concentrations support extreme high-temperature growth (weber2003bacterialcoldshock pages 36-38, rudolph2010evolutionofescherichia pages 1-2).
5. **Treat oxidative stress as linked but not proven upstream.** More than half of the critical-high-temperature gene mutants were H2O2-sensitive, demonstrating overlap rather than a single causal direction (murata2011molecularstrategyfor pages 1-2).
6. **Keep adaptive condensation taxon-qualified.** Strong 2024 evidence comes from budding yeasts and should not be transferred automatically to bacteria (kik2024anadaptivebiomolecular pages 5-6).
7. **Do not infer breadth from one endpoint.** A mutation raising Tmax by 2–3 °C may leave Tmin unchanged, narrow the lower side, or impose a growth-rate cost. Mesophile evolution experiments indicate only approximately 2–3 °C improvement and limited adaptive strategies in tested strains (kosaka2019capacityforsurvival pages 1-2).
8. **Validate ontology accessions before YAML insertion.** Particularly validate protein-specific UniProt accessions, hydroxyectoine, membrane-fluidity terms, and any organism-specific `des`, `desK`, or `desR` identifiers.
9. **Do not merge environmental occurrence and axenic growth assays.** Preserve evidence type and assay provenance.
10. **Record temperature resolution.** A 5 °C assay grid cannot distinguish, for example, a 9 °C breadth from an 11 °C breadth reliably.

## 7. DOI-first bibliography

1. **Maiti A, Erimban S, Daschakraborty S.** “Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.” *Chemical Communications* 60:10280–10294. **Published/accepted August 2024.** DOI: [10.1039/D4CC03114H](https://doi.org/10.1039/D4CC03114H). Current synthesis of homeoviscous and osmolyte-mediated adaptation (maiti2024extrememakeoverthe pages 1-2, maiti2024extrememakeoverthe pages 3-4).
2. **Kik SK et al.** “An adaptive biomolecular condensation response is conserved across environmentally divergent species.” *Nature Communications* 15:3127. **Published April 2024; accepted 27 March 2024.** DOI: [10.1038/s41467-024-47355-9](https://doi.org/10.1038/s41467-024-47355-9) (kik2024anadaptivebiomolecular pages 5-6, kik2024anadaptivebiomolecular pages 1-2).
3. **He Q et al.** “High speciation rate of niche specialists in hot springs.” *ISME Journal* 17:1303–1314. **Published 7 June 2023.** DOI: [10.1038/s41396-023-01447-4](https://doi.org/10.1038/s41396-023-01447-4) (he2023highspeciationrate pages 1-2).
4. **de Mendoza D.** “Temperature sensing by membranes.” *Annual Review of Microbiology* 68:101–116. **Published September 2014.** DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). Authoritative DesK/DesR and homeoviscous-adaptation review (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 2-4).
5. **Murata M et al.** “Molecular strategy for survival at a critical high temperature in *Escherichia coli*.” *PLoS ONE* 6:e20063. **Published June 2011.** DOI: [10.1371/journal.pone.0020063](https://doi.org/10.1371/journal.pone.0020063) (murata2011molecularstrategyfor pages 1-2).
6. **Rudolph B et al.** “Evolution of *Escherichia coli* for growth at high temperatures.” *Journal of Biological Chemistry* 285:19029–19034. **Published June 2010.** DOI: [10.1074/jbc.M110.103374](https://doi.org/10.1074/jbc.M110.103374) (rudolph2010evolutionofescherichia pages 1-2, rudolph2010evolutionofescherichia pages 4-5).
7. **Kosaka T et al.** “Capacity for survival in global warming: Adaptation of mesophiles to the temperature upper limit.” *PLoS ONE* 14:e0215614. **Published 7 May 2019.** DOI: [10.1371/journal.pone.0215614](https://doi.org/10.1371/journal.pone.0215614) (kosaka2019capacityforsurvival pages 1-2).
8. **Weber MHW, Marahiel MA.** “Bacterial cold shock responses.” *Science Progress* 86:75–95. **Published 2003.** DOI: [10.3184/003685003783238707](https://doi.org/10.3184/003685003783238707) (weber2003bacterialcoldshock pages 36-38).

## Bottom-line recommendation

Curate the **DesK/DesR–desaturase–UFA–membrane-fluidity** chain and the **GroEL/GroES plus DnaK/DnaJ–upper-temperature-growth** edges as taxon-qualified mechanistic modules. Represent their connection to **METPO:1000485** through measured Tmin and Tmax endpoint nodes. Do **not** curate a direct claim that any module uniquely causes a 10–20 °C breadth until a study measures both endpoints under matched conditions and perturbs the proposed mechanism.

References

1. (he2023highspeciationrate pages 1-2): Qing He, Shang Wang, Kai Feng, Sean T Michaletz, Weiguo Hou, Wenhui Zhang, Fangru Li, Yidi Zhang, Danrui Wang, Xi Peng, Xingsheng Yang, and Ye Deng. High speciation rate of niche specialists in hot springs. The ISME Journal, 17:1303-1314, Jun 2023. URL: https://doi.org/10.1038/s41396-023-01447-4, doi:10.1038/s41396-023-01447-4. This article has 71 citations.

2. (he2023highspeciationrate pages 2-4): Qing He, Shang Wang, Kai Feng, Sean T Michaletz, Weiguo Hou, Wenhui Zhang, Fangru Li, Yidi Zhang, Danrui Wang, Xi Peng, Xingsheng Yang, and Ye Deng. High speciation rate of niche specialists in hot springs. The ISME Journal, 17:1303-1314, Jun 2023. URL: https://doi.org/10.1038/s41396-023-01447-4, doi:10.1038/s41396-023-01447-4. This article has 71 citations.

3. (rudolph2010evolutionofescherichia pages 4-5): Birgit Rudolph, Katharina M. Gebendorfer, Johannes Buchner, and Jeannette Winter. Evolution of escherichia coli for growth at high temperatures. Journal of Biological Chemistry, 285:19029-19034, Jun 2010. URL: https://doi.org/10.1074/jbc.m110.103374, doi:10.1074/jbc.m110.103374. This article has 200 citations and is from a domain leading peer-reviewed journal.

4. (maiti2024extrememakeoverthe pages 3-4): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 17 citations and is from a domain leading peer-reviewed journal.

5. (mendoza2014temperaturesensingby pages 6-8): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

6. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

7. (mendoza2014temperaturesensingby pages 4-5): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

8. (mendoza2014temperaturesensingby pages 1-2): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

9. (rudolph2010evolutionofescherichia pages 1-2): Birgit Rudolph, Katharina M. Gebendorfer, Johannes Buchner, and Jeannette Winter. Evolution of escherichia coli for growth at high temperatures. Journal of Biological Chemistry, 285:19029-19034, Jun 2010. URL: https://doi.org/10.1074/jbc.m110.103374, doi:10.1074/jbc.m110.103374. This article has 200 citations and is from a domain leading peer-reviewed journal.

10. (murata2011molecularstrategyfor pages 1-2): Masayuki Murata, Hiroko Fujimoto, Kaori Nishimura, Kannikar Charoensuk, Hiroshi Nagamitsu, Satish Raina, Tomoyuki Kosaka, Taku Oshima, Naotake Ogasawara, and Mamoru Yamada. Molecular strategy for survival at a critical high temperature in eschierichia coli. PLoS ONE, 6:e20063, Jun 2011. URL: https://doi.org/10.1371/journal.pone.0020063, doi:10.1371/journal.pone.0020063. This article has 119 citations and is from a peer-reviewed journal.

11. (kik2024anadaptivebiomolecular pages 5-6): Samantha Keyport Kik, Dana Christopher, Hendrik Glauninger, Caitlin Wong Hickernell, J. Bard, Kyle M Lin, Allison H Squires, Michael Ford, Tobin S Sosnick, and Allan Drummond. An adaptive biomolecular condensation response is conserved across environmentally divergent species. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47355-9, doi:10.1038/s41467-024-47355-9. This article has 38 citations and is from a highest quality peer-reviewed journal.

12. (maiti2024extrememakeoverthe pages 4-5): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 17 citations and is from a domain leading peer-reviewed journal.

13. (kik2024anadaptivebiomolecular pages 1-2): Samantha Keyport Kik, Dana Christopher, Hendrik Glauninger, Caitlin Wong Hickernell, J. Bard, Kyle M Lin, Allison H Squires, Michael Ford, Tobin S Sosnick, and Allan Drummond. An adaptive biomolecular condensation response is conserved across environmentally divergent species. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47355-9, doi:10.1038/s41467-024-47355-9. This article has 38 citations and is from a highest quality peer-reviewed journal.

14. (maiti2024extrememakeoverthe pages 1-2): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 17 citations and is from a domain leading peer-reviewed journal.

15. (weber2003bacterialcoldshock pages 36-38): Michael H.W. Weber and Mohamed A. Marahiel. Bacterial cold shock responses. Science Progress, 86:75-9, Feb 2003. URL: https://doi.org/10.3184/003685003783238707, doi:10.3184/003685003783238707. This article has 253 citations.

16. (kosaka2019capacityforsurvival pages 1-2): Tomoyuki Kosaka, Yasuyuki Nakajima, Ayana Ishii, Maiko Yamashita, Saki Yoshida, Masayuki Murata, Kunpei Kato, Yuki Shiromaru, Shun Kato, Yu Kanasaki, Hirofumi Yoshikawa, Minenosuke Matsutani, Pornthap Thanonkeo, and Mamoru Yamada. Capacity for survival in global warming: adaptation of mesophiles to the temperature upper limit. PLoS ONE, 14:e0215614, May 2019. URL: https://doi.org/10.1371/journal.pone.0215614, doi:10.1371/journal.pone.0215614. This article has 32 citations and is from a peer-reviewed journal.

17. (mendoza2014temperaturesensingby pages 2-4): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.