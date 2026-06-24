---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:29:43.285102'
end_time: '2026-06-18T04:42:26.546616'
duration_seconds: 763.26
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: denitrification
  trait_identifier: traitmech:000104
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: denitrification
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which nitrate is reduced stepwise
    to gaseous dinitrogen via nitrite, nitric oxide, and nitrous oxide, removing fixed
    nitrogen from the system as gas.
  parent_traits: METPO:1000802
  synonyms: denitrifying
  evidence_summary: 'DOI:10.1128/mmbr.61.4.533-616.1997:  (Zumft reviews the cell
    biology and molecular basis of denitrification, the stepwise respiratory reduction
    of nitrate to dinitrogen.) | DOI:10.1038/nrmicro.2018.9:  (Kuypers et al. place
    denitrification as a nitrogen-loss branch of the microbial nitrogen-cycling network.)'
  causal_graph_summary: 'denitrification_stepwise_nitrate_to_n2: 4 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** denitrification
- **METPO identifier:** traitmech:000104
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which nitrate is reduced stepwise to gaseous dinitrogen via nitrite, nitric oxide, and nitrous oxide, removing fixed nitrogen from the system as gas.
- **Parent traits:** METPO:1000802
- **Synonyms:** denitrifying
- **Existing evidence:** DOI:10.1128/mmbr.61.4.533-616.1997:  (Zumft reviews the cell biology and molecular basis of denitrification, the stepwise respiratory reduction of nitrate to dinitrogen.) | DOI:10.1038/nrmicro.2018.9:  (Kuypers et al. place denitrification as a nitrogen-loss branch of the microbial nitrogen-cycling network.)
- **Existing causal graph summary:** denitrification_stepwise_nitrate_to_n2: 4 nodes, 2 edges

## Research Objective

Research the microbial trait **denitrification** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/denitrification.yaml`.

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
- **Trait label:** denitrification
- **METPO identifier:** traitmech:000104
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which nitrate is reduced stepwise to gaseous dinitrogen via nitrite, nitric oxide, and nitrous oxide, removing fixed nitrogen from the system as gas.
- **Parent traits:** METPO:1000802
- **Synonyms:** denitrifying
- **Existing evidence:** DOI:10.1128/mmbr.61.4.533-616.1997:  (Zumft reviews the cell biology and molecular basis of denitrification, the stepwise respiratory reduction of nitrate to dinitrogen.) | DOI:10.1038/nrmicro.2018.9:  (Kuypers et al. place denitrification as a nitrogen-loss branch of the microbial nitrogen-cycling network.)
- **Existing causal graph summary:** denitrification_stepwise_nitrate_to_n2: 4 nodes, 2 edges

## Research Objective

Research the microbial trait **denitrification** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/denitrification.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Denitrification (traitmech:000104)

### Scope summary (TraitMech target)
Denitrification is an anaerobic respiratory metabolism in which fixed nitrogen is reduced stepwise from nitrate to dinitrogen gas via nitrite, nitric oxide, and nitrous oxide (NO3− → NO2− → NO → N2O → N2). Recent literature emphasizes that denitrification is frequently **modular** in complex environments, where organisms may encode complete or partial sets of denitrification enzymes, and community structure therefore influences intermediate accumulation (notably N2O) and net N loss (sennett2024determininghowoxygen pages 1-2, schacksen2024unravelingthegenetic pages 1-2, bano2024soilpropertiesdrive pages 1-2).

**Trait boundary cases important for curation:**
1) **Nitrate reduction alone** (nap/nar) is not strictly diagnostic of denitrification because NO3−→NO2− occurs in other metabolisms; a denitrification trait call should require downstream steps (nir and/or nor and/or nosZ), depending on the intended strictness (schacksen2024unravelingthegenetic pages 1-2, sennett2024determininghowoxygen pages 1-2).
2) **Non-denitrifying N2O reducers**: organisms may encode **nosZ** but lack upstream nirK/nirS and norB/norC, making them N2O sinks without full denitrification capacity (schacksen2024unravelingthegenetic pages 1-2, intrator2024aquaticnitrousoxide pages 1-2).
3) **Aerobic denitrification**: heterotrophic denitrification can proceed under high dissolved oxygen in dynamic oxic/anoxic regimes; this is best modeled as a context-dependent phenotype (roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 8-9).

### Key concepts and definitions (current understanding)
**Canonical denitrification enzymes/genes** used as mechanistic entities in curation:
- Nitrate reductases: Nar (narG) and Nap (napA) (sennett2024determininghowoxygen pages 1-2, xiang2023denitrificationcontributesto pages 1-2)
- Nitrite reductases producing NO: NirK and NirS (pold2024phylogeneticsandenvironmental pages 1-2, xiang2023denitrificationcontributesto pages 2-3)
- Nitric oxide reductases producing N2O: Nor (e.g., norB; multiple biochemical families exist) (xiang2023denitrificationcontributesto pages 2-3, murali2024diversityandevolution pages 2-4)
- Nitrous oxide reductase producing N2: NosZ (nosZ clades I and II) (intrator2024aquaticnitrousoxide pages 1-2, schacksen2024unravelingthegenetic pages 1-2)

**Modularity / partial denitrification:** Soil and other complex environments host networks of facultative anaerobes that “either have a complete or partial set of denitrification enzymes,” which influences “transient accumulation of the intermediates” (sennett2024determininghowoxygen pages 1-2). Incomplete/truncated denitrifiers “can contribute to significant N2O emissions” (bano2024soilpropertiesdrive pages 1-2), and “partial denitrifiers… contribute to variations in the net N2O emission or consumption” depending on community genetic potential and constraints (schacksen2024unravelingthegenetic pages 1-2).

**nosZ clades and ecological interpretation:** In aquatic datasets, clade I nosZ is often found with genes for complete denitrification, whereas clade II organisms “typically lack one or more of the other denitrification enzymes” and are often termed incomplete denitrifiers (intrator2024aquaticnitrousoxide pages 1-2). In soils, O2 legacy can select for clade I vs clade II strategies (sennett2024determininghowoxygen pages 1-2).

### Recent developments and latest research (prioritizing 2023–2024)
#### 1) Oxygen legacy and redox dynamics reshape denitrification phenotypes (soil)
Sennett et al. (Nature Communications, Aug 2024) experimentally demonstrate that denitrifier community behavior depends on prior oxygenation history (“O2 legacy”). They frame O2 as a “superordinate repressor of denitrification” and connect cyclic oxic/anoxic exposure to selection on enzyme persistence and community coordination (sennett2024determininghowoxygen pages 1-2). They report that long anoxic spells favored “canonical denitrifiers carrying nosZ clade I,” whereas constant oxic conditions favored “nosZ clade II-carrying partial- or non-denitrifiers,” suggesting community partnering of steps (sennett2024determininghowoxygen pages 1-2). Their discussion explicitly links persistence differences among reductases (NOS intact vs NirS damage) to intermediate accumulation dynamics (sennett2024determininghowoxygen pages 1-2).

#### 2) Aerobic denitrification can be quantitatively important under high DO (engineered microbiomes)
Roothans et al. (ISME Journal, June 2024 online; issue Jan 2024) provide quantitative evidence that heterotrophic denitrification can contribute to aerobic N turnover and N2O under high oxygen. They report: “Over a third of the influent organic substrate was respired with nitrate as electron acceptor at high oxygen concentrations (>6.5 mg/L). N2O accounted for up to one-quarter of the nitrate reduced under oxic conditions” (roothans2024aerobicdenitrificationas pages 1-2). In reactor analysis, they estimate “on average 12% (R4) and 24% (R32) of NO3− was emitted as N2O during aeration” (roothans2024aerobicdenitrificationas pages 8-9). They attribute this to residual activity of anaerobically expressed enzymes and metabolic preparedness under rapid O2 cycling (roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 8-9).

#### 3) nosZ clade II dominance and non-denitrifying N2O reducers in wastewater MAGs
Schacksen & Nielsen (Applied and Environmental Microbiology, Published 13 Aug 2024) analyzed 1,083 high-quality MAGs from 23 full-scale WWTPs and found 48.7% harbored nosZ; among nosZ genes, clade II dominated (93.7%) (schacksen2024unravelingthegenetic pages 1-2). They explicitly define nosZ-only reducers: “NosZ-containing non-denitrifying organisms are characterized by the absence of genes required for converting NO2− to gaseous nitric oxide (NO) (nirK/S) and subsequent NO to N2O (norB/C)” (schacksen2024unravelingthegenetic pages 1-2). This supports modeling N2O reduction as a separable trait module from canonical denitrification.

#### 4) nirK vs nirS: ecology, nitrifier associations, and implications for denitrification inference
Pold et al. (ISME Communications, Advance access 2 Feb 2024) show that NirK and NirS are “evolutionarily unrelated” but often treated as redundant; they emphasize that nitrifiers are a “sizeable proportion” of the nitrite-reducing community “especially for NirK in marine waters and dry soils” (pold2024phylogeneticsandenvironmental pages 1-2). Large-scale metagenome analysis found strong biome differences: nirK is often much more abundant than nirS (median 19× across terrestrial biomes), while soil moisture and redox state correlate with relative prevalence (pold2024phylogeneticsandenvironmental pages 8-11). Importantly for curation: presence of nirK (or nirS) alone does not guarantee downstream capacity; their discussion notes that assemblies with NirS more commonly encode downstream processing “into the greenhouse gas nitrous oxide by nitric oxide reductase and eventually to N2 by NosZ,” while nirK assemblies often have lower prevalence of nosZ (pold2024phylogeneticsandenvironmental pages 12-13).

#### 5) Expanded diversity of nitric oxide reductases (NORs) and experimental validation
Murali et al. (PNAS, Jun 2024) expands the known diversity of NO reductases (enzymes converting NO → N2O). They describe classical cNOR and qNOR and discuss reclassification of qCuANOR to bNOR, which includes a conserved proton channel and was “electrogenic,” and they identify additional families (eNOR, sNOR, nNOR, gNOR) likely performing NO reduction (murali2024diversityandevolution pages 2-4). They validate an eNOR in Rhodothermus marinus and show complete aerobic denitrification (NO3−→N2) under microoxic conditions; acetylene blockage of NosZ caused N2O accumulation, implying a NOR-mediated source (murali2024diversityandevolution pages 2-4). This supports inclusion of Nor-type diversity as candidate mechanistic nodes/edges, but many families remain newly described and may require careful grounding.

### Current applications and real-world implementations
1) **Agricultural soils and mitigation of N2O emissions:** Soil physicochemical properties shape denitrifier guilds and N2O product ratios. In a cross-inoculation design, Bano et al. (Environmental Microbiome, Nov 2024) found recipient soil controlled gas kinetics and N2O/(N2O+N2): “significantly higher N2O/(N2O + N2) ratios in BS compared to FS, regardless of the inoculum type,” with differing nir/nosZ ratios (nirS/nosZ higher in FS; nirK/nosZ higher in BS) (bano2024soilpropertiesdrive pages 1-2). This supports applications where pH/soil type management aims to favor complete denitrification and reduce N2O accumulation.
2) **Wastewater treatment plants (WWTPs):** Genome-resolved surveys suggest engineering levers could include enriching nosZ-containing taxa (including clade II non-denitrifying reducers) and improving detection/monitoring via primers for near-full-length nosZ (schacksen2024unravelingthegenetic pages 1-2). Aeration regime design (e.g., limiting aerobic denitrification-derived N2O or enhancing N2O reduction) is an actionable operational parameter highlighted by the aerobic denitrification work (roothans2024aerobicdenitrificationas pages 8-9, roothans2024aerobicdenitrificationas pages 1-2).
3) **Aquatic systems and OMZs:** Intrator et al. (Frontiers in Microbiology, May 2024) emphasize that “One-third of atmospheric N2O originates in aquatic environments” and that nosZ-containing organisms are the “only known biological sinks of N2O” (intrator2024aquaticnitrousoxide pages 1-2). Their habitat-separation findings between nosZ clades support community-based modeling of N2O sources/sinks in OMZs and sediments.

### Expert opinions / authoritative interpretations (from cited sources)
- **O2 as a dominant control:** Denitrification is “intricately controlled by O2” and O2 is a “superordinate repressor of denitrification” (sennett2024determininghowoxygen pages 1-2). This supports including O2 availability and cycling as high-level environmental nodes upstream of pathway activity.
- **Community structure and modularity as essential explanatory variables:** Soil denitrification is mediated by a “diverse network” with “complete or partial set of denitrification enzymes,” and this modularity affects phenotypes and intermediate accumulation (sennett2024determininghowoxygen pages 1-2). This supports modeling denitrification as a networked process rather than a single-organism pathway in many natural settings.
- **Caution in functional inference from single markers:** nirK/nirS presence is not synonymous with full denitrification capacity; nitrifiers contribute substantially to NirK pools (pold2024phylogeneticsandenvironmental pages 1-2), and nirK-associated assemblies can lack Nor and NosZ (pold2024phylogeneticsandenvironmental pages 12-13). Similarly, nap/nar genes alone are not “strictly denitrifying genes” (schacksen2024unravelingthegenetic pages 1-2).

### Recent statistics and quantitative data (2023–2024)
- **Paddy soil denitrification product partitioning:** Xiang et al. (Frontiers in Microbiology, Jun 2023) report potential N2O emission rates of “0.51 ± 0.20 μmol·N·kg−1·h−1,” comprising “2.16 ± 0.85% of the denitrification end-products,” and N2O production enzyme activity “2.77–8.94 times” N2O reduction activity (xiang2023denitrificationcontributesto pages 1-2).
- **Aerobic denitrification under high DO:** Roothans et al. report “Over a third” of influent organic substrate respired with nitrate at “>6.5 mg/L” O2 and “N2O accounted for up to one-quarter of the nitrate reduced under oxic conditions” (roothans2024aerobicdenitrificationas pages 1-2). They further estimate “12%… and 24%… of NO3− was emitted as N2O during aeration” in two regimes (roothans2024aerobicdenitrificationas pages 8-9).
- **Wastewater nosZ prevalence:** In Danish WWTP MAGs, 48.7% of MAGs harbored nosZ and 93.7% of nosZ genes were clade II (schacksen2024unravelingthegenetic pages 1-2).
- **Soil-type control of N2O product ratio:** Bano et al. report significantly higher N2O/(N2O+N2) in black soil than fluvo-aquic soil regardless of inoculum, coupled to nir/nosZ ratios (bano2024soilpropertiesdrive pages 1-2).

---

## Candidate causal-graph nodes (grouped)
The following table provides curation-ready candidate nodes spanning pathway, enzymes, metabolites, environmental factors, and observables, with suggested grounding and citations.

| Node type | Candidate node | Description / curation note | Suggested grounding | Key supporting citations |
|---|---|---|---|---|
| Trait/phenotype | denitrification | Anaerobic respiratory metabolism reducing nitrate/nitrite to gaseous N products, often ending in N2; core TraitMech target node | METPO: traitmech:000104; GO:0019646 (denitrification) | (sennett2024determininghowoxygen pages 1-2, bano2024soilpropertiesdrive pages 1-2, intrator2024aquaticnitrousoxide pages 1-2) |
| Trait/phenotype | complete denitrification | Capacity to perform the full NO3- → NO2- → NO → N2O → N2 pathway in one organism | label-only; GO:0019646 related | (schacksen2024unravelingthegenetic pages 1-2, bano2024soilpropertiesdrive pages 1-2, intrator2024aquaticnitrousoxide pages 1-2) |
| Trait/phenotype | partial / truncated denitrification | Organisms lacking one or more denitrification steps; important boundary case because communities may complete the pathway collectively | label-only | (sennett2024determininghowoxygen pages 1-2, schacksen2024unravelingthegenetic pages 1-2, bano2024soilpropertiesdrive pages 1-2) |
| Trait/phenotype | aerobic denitrification | Simultaneous O2 respiration and denitrification under oxic conditions; should be modeled as a contextual subtype / condition-dependent phenotype | label-only | (roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 8-9) |
| Trait/phenotype | N2O reduction only / non-denitrifying N2O reducer | nosZ-containing organisms lacking upstream nir/nor; important not to over-curate as denitrifiers | label-only | (schacksen2024unravelingthegenetic pages 1-2, intrator2024aquaticnitrousoxide pages 1-2) |
| Pathway/module | canonical denitrification pathway | Stepwise nitrate reduction to dinitrogen via nitrite, nitric oxide, nitrous oxide | KEGG Module: M00529; MetaCyc: DENITRIFICATION-PWY | (sennett2024determininghowoxygen pages 1-2, bano2024soilpropertiesdrive pages 1-2, xiang2023denitrificationcontributesto pages 1-2) |
| Pathway/module | nitrate reduction branch (NO3- → NO2-) | First respiratory step; may be shared with other nitrate-reducing metabolisms, so boundary with denitrification is important | GO:0042128 (nitrate assimilation/reduction terms not exact); KEGG orthology group label-only | (sennett2024determininghowoxygen pages 1-2, schacksen2024unravelingthegenetic pages 1-2, bano2024soilpropertiesdrive pages 1-2) |
| Pathway/module | nitrite reduction to nitric oxide | Distinguishing denitrification step catalyzed by NirK/NirS | GO:0042121 (nitrite reduction); label-only | (pold2024phylogeneticsandenvironmental pages 1-2, xiang2023denitrificationcontributesto pages 2-3) |
| Pathway/module | nitric oxide reduction to nitrous oxide | N2O-producing step; major emission-relevant module | GO:0019670 (nitric oxide metabolic process related); label-only | (xiang2023denitrificationcontributesto pages 2-3, murali2024diversityandevolution pages 2-4) |
| Pathway/module | nitrous oxide reduction to dinitrogen | Terminal N2O sink step; critical for emission mitigation | GO:0055114 related redox; label-only | (schacksen2024unravelingthegenetic pages 1-2, intrator2024aquaticnitrousoxide pages 1-2) |
| Pathway/module | modular community denitrification | Community-level completion of pathway by cooperating taxa carrying different steps | label-only | (sennett2024determininghowoxygen pages 1-2, schacksen2024unravelingthegenetic pages 1-2, xiang2023denitrificationcontributesto pages 1-2) |
| Enzymes/complexes | respiratory nitrate reductase NarGHI | Membrane-bound nitrate reductase; frequently detected in denitrifiers, including oxic/anoxic cycling enrichments | EC:1.7.5.1; gene marker: narG | (sennett2024determininghowoxygen pages 1-2, roothans2024aerobicdenitrificationas pages 8-9, bano2024soilpropertiesdrive pages 1-2) |
| Enzymes/complexes | periplasmic nitrate reductase NapAB | Periplasmic nitrate reductase; present in many denitrifiers but not exclusive to denitrification | EC:1.9.6.1; gene marker: napA | (sennett2024determininghowoxygen pages 1-2, schacksen2024unravelingthegenetic pages 1-2, xiang2023denitrificationcontributesto pages 1-2) |
| Enzymes/complexes | copper nitrite reductase NirK | Multicopper nitrite reductase producing NO; ecologically distinct from NirS and common in nitrifier-associated lineages | EC:1.7.2.1; gene marker: nirK | (pold2024phylogeneticsandenvironmental pages 1-2, pold2024phylogeneticsandenvironmental pages 8-11, xiang2023denitrificationcontributesto pages 2-3) |
| Enzymes/complexes | cytochrome cd1 nitrite reductase NirS | Heme cd1 nitrite reductase producing NO; more often linked to complete denitrifiers | EC:1.7.2.1; gene marker: nirS | (pold2024phylogeneticsandenvironmental pages 1-2, pold2024phylogeneticsandenvironmental pages 12-13, xiang2023denitrificationcontributesto pages 2-3) |
| Enzymes/complexes | cytochrome c-dependent nitric oxide reductase cNor | Canonical NO reductase often associated with denitrification | EC:1.7.2.5; gene markers: norB/norC | (pold2024phylogeneticsandenvironmental pages 12-13, murali2024diversityandevolution pages 2-4, xiang2023denitrificationcontributesto pages 2-3) |
| Enzymes/complexes | quinol-dependent nitric oxide reductase qNor | Alternative NO reductase, often linked to NO detoxification / broader ecological roles | EC:1.7.2.5; gene marker: qnor/norZ label-only | (pold2024phylogeneticsandenvironmental pages 12-13, murali2024diversityandevolution pages 2-4, sennett2024determininghowoxygen pages 6-7) |
| Enzymes/complexes | nitrous oxide reductase NosZ clade I | Clade I nosZ commonly associated with canonical / complete denitrifiers | EC:1.7.2.4; gene marker: nosZ; accessory nosR often associated | (schacksen2024unravelingthegenetic pages 1-2, intrator2024aquaticnitrousoxide pages 1-2, sennett2024determininghowoxygen pages 1-2) |
| Enzymes/complexes | nitrous oxide reductase NosZ clade II | Clade II nosZ often found in partial or non-denitrifying N2O reducers; broad environmental distribution | EC:1.7.2.4; gene marker: nosZ | (schacksen2024unravelingthegenetic pages 1-2, intrator2024aquaticnitrousoxide pages 1-2, sennett2024determininghowoxygen pages 1-2) |
| Enzymes/complexes | accessory Nos proteins | Accessory factors relevant to NosZ maturation / export (e.g., nosB, nosR) | gene markers: nosB, nosR; label-only | (schacksen2024unravelingthegenetic pages 1-2) |
| Metabolites/electron acceptors/donors | nitrate | Initial terminal electron acceptor in denitrification | CHEBI:17632 | (sennett2024determininghowoxygen pages 1-2, bano2024soilpropertiesdrive pages 1-2, xiang2023denitrificationcontributesto pages 1-2) |
| Metabolites/electron acceptors/donors | nitrite | Intermediate and electron acceptor; reduction often rate-limiting | CHEBI:16301 | (xiang2023denitrificationcontributesto pages 2-3, xiang2023denitrificationcontributesto pages 1-2) |
| Metabolites/electron acceptors/donors | nitric oxide | Reactive intermediate/product of Nir, substrate of Nor | CHEBI:16480 | (xiang2023denitrificationcontributesto pages 2-3, murali2024diversityandevolution pages 2-4) |
| Metabolites/electron acceptors/donors | nitrous oxide | Greenhouse-gas intermediate; substrate for NosZ and key observable output | CHEBI:33101 | (intrator2024aquaticnitrousoxide pages 1-2, xiang2023denitrificationcontributesto pages 1-2, roothans2024aerobicdenitrificationas pages 8-9) |
| Metabolites/electron acceptors/donors | dinitrogen | Final gaseous end product of complete denitrification | CHEBI:17997 | (sennett2024determininghowoxygen pages 1-2, intrator2024aquaticnitrousoxide pages 1-2) |
| Metabolites/electron acceptors/donors | molecular oxygen | Superordinate repressor / competing electron acceptor controlling denitrification dynamics | CHEBI:15379 | (sennett2024determininghowoxygen pages 1-2, roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 8-9) |
| Metabolites/electron acceptors/donors | organic carbon / electron donor | Carbon substrate fueling heterotrophic denitrification | CHEBI:label-only (heterogeneous pool) | (roothans2024aerobicdenitrificationas pages 1-2, sennett2024determininghowoxygen pages 1-2) |
| Environmental/exposure factors | anoxic conditions | Core environmental context favoring canonical denitrification | ENVO: label-only (anoxic environment) | (bano2024soilpropertiesdrive pages 1-2, sennett2024determininghowoxygen pages 1-2) |
| Environmental/exposure factors | oxic/anoxic cycling | Dynamic exposure regime selecting for aerobic denitrification / O2-legacy effects | label-only | (roothans2024aerobicdenitrificationas pages 1-2, sennett2024determininghowoxygen pages 1-2, roothans2024aerobicdenitrificationas pages 8-9) |
| Environmental/exposure factors | oxygen legacy | Prior O2 exposure history shaping denitrifier community structure and N2O outcomes | label-only | (sennett2024determininghowoxygen pages 1-2, sennett2024determininghowoxygen pages 6-7) |
| Environmental/exposure factors | soil pH | Key distal driver; low pH can constrain Nos activity and alter guild composition | ENVO:00001998 (soil); pH label-only | (bano2024soilpropertiesdrive pages 1-2, pold2024phylogeneticsandenvironmental pages 8-11) |
| Environmental/exposure factors | soil moisture / water-logged soil | Low-redox condition associated with denitrification in paddy and wet soils | ENVO:00002224 (paddy field, if used), ENVO:00010671 (soil) label-only | (xiang2023denitrificationcontributesto pages 1-2, pold2024phylogeneticsandenvironmental pages 8-11) |
| Environmental/exposure factors | dissolved oxygen concentration | Quantitative exposure variable controlling aerobic vs anaerobic denitrification | label-only | (roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 8-9) |
| Environmental/exposure factors | nitrate amendment / NO3- availability | Experimental factor stimulating denitrification genes and rates | label-only | (sennett2024determininghowoxygen pages 1-2, sennett2024determininghowoxygen pages 6-7) |
| Environmental/exposure factors | copper availability / limitation | Mechanistically relevant to Cu enzymes (NirK, NosZ); Cu limitation can alter N-oxide accumulation | CHEBI:28694; label-only environmental factor | (intrator2024aquaticnitrousoxide pages 12-12, pold2024phylogeneticsandenvironmental pages 8-11) |
| Environmental/exposure factors | marine oxygen minimum zone | Aquatic low-O2 habitat with elevated N2O and nosZ ecological differentiation | ENVO:01000065? label-only if uncertain | (intrator2024aquaticnitrousoxide pages 1-2) |
| Environmental/exposure factors | agricultural soil / paddy soil | Important real-world denitrification habitat and assay matrix | ENVO:00001998 (soil); ENVO:00002224 (paddy field) | (xiang2023denitrificationcontributesto pages 1-2, bano2024soilpropertiesdrive pages 1-2) |
| Assays/observables | N2O/(N2O+N2) ratio | Standard denitrification product ratio / propensity-to-emit metric | label-only observable | (bano2024soilpropertiesdrive pages 1-2, xiang2023denitrificationcontributesto pages 1-2) |
| Assays/observables | potential N2O emission rate | Measured output in incubations; direct phenotype readout | label-only observable | (xiang2023denitrificationcontributesto pages 1-2) |
| Assays/observables | N2O production vs N2O reduction enzyme activity | Functional imbalance metric relevant to emission phenotype | label-only observable | (xiang2023denitrificationcontributesto pages 1-2) |
| Assays/observables | nir:nosZ gene abundance ratio | Frequently used genomic proxy for imbalance between N2O production and reduction capacity | label-only observable | (xiang2023denitrificationcontributesto pages 2-3, xiang2023denitrificationcontributesto pages 1-2) |
| Assays/observables | nirS/nosZ ratio | Soil/guild-specific proxy associated with lower N2O accumulation in FS in one study | label-only observable | (bano2024soilpropertiesdrive pages 1-2) |
| Assays/observables | nirK/nosZ ratio | Soil/guild-specific proxy associated with higher N2O accumulation in BS in one study | label-only observable | (bano2024soilpropertiesdrive pages 1-2) |
| Assays/observables | nosZ clade I : clade II relative abundance | Community-structure observable linked to canonical vs partial/non-denitrifier strategies | label-only observable | (sennett2024determininghowoxygen pages 1-2, sennett2024determininghowoxygen pages 6-7, intrator2024aquaticnitrousoxide pages 1-2) |
| Assays/observables | denitrification gene/transcript abundance | Metagenomic / metatranscriptomic evidence for pathway potential and activity | label-only observable | (sennett2024determininghowoxygen pages 6-7, bano2024soilpropertiesdrive pages 9-13) |
| Assays/observables | dissolved N2O concentration / flux | Environmental readout for in situ denitrification contribution | label-only observable | (xiang2023denitrificationcontributesto pages 2-3, xiang2023denitrificationcontributesto pages 1-2) |


*Table: This table organizes curation-ready candidate nodes for a denitrification TraitMech graph across phenotype, pathway, enzyme, metabolite, environment, and assay layers. It highlights suggested ontology grounding and cites the context passages supporting each node's inclusion.*

---

## Candidate causal edges (evidence-backed triples)
The following table lists candidate edges for denitrification.yaml curation, each with a supporting verbatim snippet, DOI/URL/date, and uncertainty notes.

| Subject node | Predicate | Object node | Evidence snippet (verbatim quote) | Citation context ID | Reference DOI / URL / date | Notes on scope / uncertainty |
|---|---|---|---|---|---|---|
| respiratory nitrate reductase NarGHI | enables | nitrate reduction to nitrite | “narG (NO3⁻ reductase)” | (bano2024soilpropertiesdrive pages 1-2) | DOI:10.1186/s40793-024-00643-9 · https://doi.org/10.1186/s40793-024-00643-9 · 2024-11 | Supports canonical first step; gene marker rather than direct enzyme assay. |
| periplasmic nitrate reductase NapAB | enables | nitrate reduction to nitrite | “The napA gene encodes NO3− reductase, which catalyzes the reduction of NO3− to NO2−” | (xiang2023denitrificationcontributesto pages 1-2) | DOI:10.3389/fmicb.2023.1218207 · https://doi.org/10.3389/fmicb.2023.1218207 · 2023-06 | nap/nar are not strictly denitrification-specific boundary markers. |
| copper nitrite reductase NirK | enables | nitrite reduction to nitric oxide | “NO2− reduction is catalyzed by NO2− reductases, including the nirS gene-encoded copper-containing NO2− reductase and the nirK gene-encoded cytochrome cd1-containing NO2− reductase” | (xiang2023denitrificationcontributesto pages 2-3) | DOI:10.3389/fmicb.2023.1218207 · https://doi.org/10.3389/fmicb.2023.1218207 · 2023-06 | Source appears to have nirK/nirS descriptors swapped versus canonical literature; curate reaction-level claim only, not metal/cofactor wording. |
| cytochrome cd1 nitrite reductase NirS | enables | nitrite reduction to nitric oxide | “In denitrification, the major route of N loss from the biosphere to the atmosphere, nitrite is reduced to gaseous nitric oxide (NO) by one of two evolutionarily distinct nitrite reductases… the heme-coordinating cytochrome cd1 NirS and the multicopper-oxidase NirK.” | (pold2024phylogeneticsandenvironmental pages 1-2) | DOI:10.1093/ismeco/ycae020 · https://doi.org/10.1093/ismeco/ycae020 · 2024-02 | Strong general mechanistic support. |
| nitric oxide reductase Nor | enables | nitric oxide reduction to nitrous oxide | “The NO reductase (NOR), encoded by the norB gene, is responsible for the reduction of NO to N2O” | (xiang2023denitrificationcontributesto pages 2-3) | DOI:10.3389/fmicb.2023.1218207 · https://doi.org/10.3389/fmicb.2023.1218207 · 2023-06 | Canonical N2O-producing step. |
| nitrous oxide reductase NosZ | enables | nitrous oxide reduction to dinitrogen | “The N2O reductase (NOS) catalyzes the reduction of N2O, converting the greenhouse gas N2O into relatively harmless N2” | (xiang2023denitrificationcontributesto pages 2-3) | DOI:10.3389/fmicb.2023.1218207 · https://doi.org/10.3389/fmicb.2023.1218207 · 2023-06 | Canonical terminal step; important sink function. |
| nitrous oxide reductase NosZ | part_of | denitrification | “Reduction of N2O to dinitrogen gas (N2) requires the nitrous oxide reductase enzyme, which is encoded by the gene nosZ.” | (intrator2024aquaticnitrousoxide pages 1-2) | DOI:10.3389/fmicb.2024.1407573 · https://doi.org/10.3389/fmicb.2024.1407573 · 2024-05 | Supports inclusion of NosZ as final-step denitrification component. |
| denitrification pathway modularity | causes | transient accumulation of intermediates | “This modular nature of the denitrification pathway affects soil denitrification phenotypes… and the transient accumulation of the intermediates” | (sennett2024determininghowoxygen pages 1-2) | DOI:10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024-08 | Community-level causal effect; good TraitMech edge for modularity. |
| partial / truncated denitrifiers | positively_regulates | N2O emissions | “organisms lacking one or more of these genes are called truncated or incomplete denitrifiers and can contribute to significant N2O emissions” | (bano2024soilpropertiesdrive pages 1-2) | DOI:10.1186/s40793-024-00643-9 · https://doi.org/10.1186/s40793-024-00643-9 · 2024-11 | Strong review-style claim within primary paper; community/taxon-general. |
| partial denitrifiers lacking one or more denitrifying genes | causes | variation in net N2O emission or consumption | “These partial denitrifiers, defined as lacking one or more denitrifying genes, contribute to variations in the net N2O emission or consumption” | (schacksen2024unravelingthegenetic pages 1-2) | DOI:10.1128/aem.02177-23 · https://doi.org/10.1128/aem.02177-23 · 2024-08 | Strong for boundary cases; applies beyond canonical denitrifiers. |
| nir:nosZ gene abundance ratio | positively_regulates | N2O emission extent | “the ratio of nir to nosZ can partly determine the extent of N2O emission in soils” | (xiang2023denitrificationcontributesto pages 2-3) | DOI:10.3389/fmicb.2023.1218207 · https://doi.org/10.3389/fmicb.2023.1218207 · 2023-06 | Proxy/association edge; likely should be marked observational. |
| higher enzymatic activity for N2O production than reduction | causes | imbalance favoring N2O emission | “The enzymatic activity for N2O production was 2.77–8.94 times than that for N2O reduction, indicating an imbalance between N2O production and reduction.” | (xiang2023denitrificationcontributesto pages 1-2) | DOI:10.3389/fmicb.2023.1218207 · https://doi.org/10.3389/fmicb.2023.1218207 · 2023-06 | Quantitative support from paddy soils; assay-specific. |
| oxygen (O2) | negatively_regulates | denitrification | “O2… acts as a superordinate repressor of denitrification” | (sennett2024determininghowoxygen pages 1-2) | DOI:10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024-08 | Strong mechanistic regulation statement. |
| oxygen (O2) | inhibits | denitrifying enzyme activity | “Oxygen is known to regulate the expression and inhibit the activity of denitrifying enzymes” | (roothans2024aerobicdenitrificationas pages 1-2) | DOI:10.1093/ismejo/wrae116 · https://doi.org/10.1093/ismejo/wrae116 · 2024-06 | Broad literature-backed claim in recent review/introduction context. |
| preservation of intact denitrification enzymes throughout oxic episodes | positively_regulates | subsequent denitrification rates | “These extant enzymes are ready to be used during subsequent anoxic episodes, representing an ‘anoxic legacy’ that enhances denitrification rates.” | (sennett2024determininghowoxygen pages 1-2) | DOI:10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024-08 | Strong mechanistic edge for O2 legacy. |
| repeated exposure to anoxic episodes | causes | accumulation of intact NOS but not NIR | “This implies that repeated exposure to anoxic episodes will lead to an accumulation of intact NOS, but not NIR” | (sennett2024determininghowoxygen pages 1-2) | DOI:10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024-08 | Mechanistic inference from cited strain studies; suitable with caution. |
| accumulation of intact NOS but not NIR | negatively_regulates | transient N2O accumulation | “resulting in a gradual reduction of the transient N2O accumulation.” | (sennett2024determininghowoxygen pages 1-2) | DOI:10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024-08 | Inferred second half of same mechanistic chain; curate as conditional. |
| nosZ clade I | positively_regulates | canonical / complete denitrification association | “Clade I organisms are often found to also contain genes encoding the enzymes for complete denitrification.” | (intrator2024aquaticnitrousoxide pages 1-2) | DOI:10.3389/fmicb.2024.1407573 · https://doi.org/10.3389/fmicb.2024.1407573 · 2024-05 | Ecological/genomic association, not absolute rule. |
| nosZ clade II | positively_regulates | partial / incomplete denitrifier association | “Clade II organisms typically lack one or more of the other denitrification enzymes and are therefore often referred to as ‘incomplete denitrifiers’” | (intrator2024aquaticnitrousoxide pages 1-2) | DOI:10.3389/fmicb.2024.1407573 · https://doi.org/10.3389/fmicb.2024.1407573 · 2024-05 | Strong clade-level ecological association; not universal. |
| constant oxic conditions / Ox oxygen legacy | positively_regulates | nosZ clade II-carrying partial- or non-denitrifiers | “Ox instead favors nosZ clade II-carrying partial- or non-denitrifiers” | (sennett2024determininghowoxygen pages 1-2) | DOI:10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024-08 | Experimental community-selection effect in soil microcosms. |
| long anoxic spells / LA oxygen legacy | positively_regulates | nosZ clade I canonical denitrifiers | “LA favors canonical denitrifiers carrying nosZ clade I.” | (sennett2024determininghowoxygen pages 1-2) | DOI:10.1038/s41467-024-51688-w · https://doi.org/10.1038/s41467-024-51688-w · 2024-08 | Experimental community-selection effect. |
| low soil pH (<6) | inhibits | nitrous oxide reductase activity | “when pH value was lower than 6 the activity of nitrous oxide reductase enzyme would be ultimately constrained” | (bano2024soilpropertiesdrive pages 1-2) | DOI:10.1186/s40793-024-00643-9 · https://doi.org/10.1186/s40793-024-00643-9 · 2024-11 | Important environmental control; wording from introduction citing prior work. |
| constrained nitrous oxide reductase activity | positively_regulates | N2O accumulation | “resulting in” | (bano2024soilpropertiesdrive pages 1-2) | DOI:10.1186/s40793-024-00643-9 · https://doi.org/10.1186/s40793-024-00643-9 · 2024-11 | Evidence phrase truncated in available excerpt; causal direction is standard but should be curated cautiously unless full sentence checked. |
| high dissolved oxygen with oxic/anoxic cycling | enables | aerobic denitrification | “Significant denitrification occurred at high oxygen concentrations” | (roothans2024aerobicdenitrificationas pages 8-9) | DOI:10.1093/ismejo/wrae116 · https://doi.org/10.1093/ismejo/wrae116 · 2024-06 | Strong evidence for context-dependent aerobic denitrification. |
| aerobic denitrification | positively_regulates | aerobic N2O emissions | “we estimated that on average 12% (R4) and 24% (R32) of NO3− was emitted as N2O during aeration” | (roothans2024aerobicdenitrificationas pages 8-9) | DOI:10.1093/ismejo/wrae116 · https://doi.org/10.1093/ismejo/wrae116 · 2024-06 | Quantitative, engineered enrichment cultures; strong but system-specific. |
| dynamic O2 conditions | positively_regulates | selection of bacteria capable of denitrifying under oxic conditions | “dynamic O2 conditions as key to select for bacteria capable of denitrifying under oxic conditions” | (roothans2024aerobicdenitrificationas pages 1-2) | DOI:10.1093/ismejo/wrae116 · https://doi.org/10.1093/ismejo/wrae116 · 2024-06 | Ecological selection effect, not direct biochemical mechanism. |
| recipient soil properties | causes | formation of different denitrifying guilds | “the recipient soil dictates the formation of different denitrifying guilds” | (bano2024soilpropertiesdrive pages 1-2) | DOI:10.1186/s40793-024-00643-9 · https://doi.org/10.1186/s40793-024-00643-9 · 2024-11 | Strong community-assembly effect in cross-inoculation experiment. |
| BS environment | positively_regulates | nirK-based denitrifiers such as Rhodanobacter | “the BS environment fosters nirK-based denitrifiers like Rhodanobacter, contributing to higher N₂O accumulation” | (bano2024soilpropertiesdrive pages 1-2) | DOI:10.1186/s40793-024-00643-9 · https://doi.org/10.1186/s40793-024-00643-9 · 2024-11 | Soil-specific ecological association. |
| FS environment | positively_regulates | complete denitrification and lower N2O emissions | “FS supports a diverse array of denitrifiers, including Pseudomonas and Stutzerimonas, associated with complete denitrification and lower N₂O emissions.” | (bano2024soilpropertiesdrive pages 1-2) | DOI:10.1186/s40793-024-00643-9 · https://doi.org/10.1186/s40793-024-00643-9 · 2024-11 | Association at community level; may not generalize across all soils. |
| nitrifiers | positively_regulates | nirK-bearing nitrite-reducing community | “Nitrifiers make up a sizeable proportion of the nitrite-reducing community, especially for NirK in marine waters and dry soils.” | (pold2024phylogeneticsandenvironmental pages 1-2) | DOI:10.1093/ismeco/ycae020 · https://doi.org/10.1093/ismeco/ycae020 · 2024-02 | Important boundary case: nirK presence does not necessarily imply canonical denitrification. |


*Table: This table compiles candidate subject-predicate-object edges for a TraitMech denitrification graph, each supported by verbatim evidence from recent sources. It covers core reaction steps, modularity, oxygen regulation, nosZ clade ecology, environmental controls, and major boundary cases relevant for curation.*

---

## Ontology grounding notes (practical)
- **Core process grounding:** GO:0019646 (denitrification) is appropriate for the pathway-level process node; TraitMech uses METPO traitmech:000104.
- **Metabolites:** Use CHEBI for nitrate, nitrite, NO, N2O, N2, O2 (see artifact-00).
- **Environmental context:** ENVO grounding is feasible for “soil” and habitat types (e.g., agricultural soil, paddy field), but “oxygen legacy” and “oxic/anoxic cycling” may remain label-only until a stable term is chosen.
- **nosZ clade terms:** These are phylogenetic/functional groupings rather than a single gene ontology term; represent as separate nodes tied to nosZ with “has_variant/clade” style relations (label-only).

---

## Warnings / claims that should be curated with caution
1) **NirK vs NirS descriptors in one excerpt:** Xiang et al. describe nirS as “copper-containing” and nirK as “cytochrome cd1-containing,” which is reversed relative to standard biochemical descriptions; the evidence is still valid for the higher-level claim that both NirK and NirS catalyze NO2− reduction to NO and are functionally distinct/rarely co-occur (xiang2023denitrificationcontributesto pages 2-3, pold2024phylogeneticsandenvironmental pages 1-2). Prefer curation of reaction role with separate evidence for cofactor type.
2) **Low-pH → Nos constraint → N2O accumulation:** The Bano et al. excerpt includes “when pH value was lower than 6 the activity of nitrous oxide reductase enzyme would be ultimately constrained, resulting in” but the downstream clause is truncated in the available text chunk (bano2024soilpropertiesdrive pages 1-2). The mechanistic consequence is plausible but should be re-checked in full text before asserting a strong causal edge.
3) **nir:nosZ ratios are proxies:** nir:nosZ is often used as a proxy for imbalance, but is not itself mechanistic; treat as an observational edge linking genomic potential to emission propensity (xiang2023denitrificationcontributesto pages 2-3).
4) **Aerobic denitrification generalization:** Quantitative aerobic denitrification results are from enrichment reactors with nitrification inhibited; generalization to soils/aquatic systems should be marked context-dependent (roothans2024aerobicdenitrificationas pages 1-2, roothans2024aerobicdenitrificationas pages 8-9).
5) **New NOR families:** Murali et al. identify multiple novel NOR families and propose functions based on structure/context; curation should separate experimentally validated (eNOR) vs predicted families (murali2024diversityandevolution pages 2-4).

---

## DOI-first bibliography (with URLs and publication dates where available)
- 10.1038/s41467-024-51688-w — Sennett LB et al. *Determining how oxygen legacy affects trajectories of soil denitrifier community dynamics and N2O emissions*. **Nature Communications**. Accepted 15 Aug 2024; published Aug 2024. https://doi.org/10.1038/s41467-024-51688-w (sennett2024determininghowoxygen pages 1-2)
- 10.1093/ismejo/wrae116 — Roothans N et al. *Aerobic denitrification as an N2O source from microbial communities*. **The ISME Journal**. Advance access 24 Jun 2024; issue Jan 2024. https://doi.org/10.1093/ismejo/wrae116 (roothans2024aerobicdenitrificationas pages 1-2)
- 10.1128/aem.02177-23 — Schacksen PS, Nielsen JL. *Unraveling the genetic potential of nitrous oxide reduction in wastewater treatment: insights from metagenome-assembled genomes*. **Applied and Environmental Microbiology**. Published 13 Aug 2024. https://doi.org/10.1128/aem.02177-23 (schacksen2024unravelingthegenetic pages 1-2)
- 10.3389/fmicb.2024.1407573 — Intrator N, Jayakumar A, Ward BB. *Aquatic nitrous oxide reductase gene (nosZ) phylogeny and environmental distribution*. **Frontiers in Microbiology**. Published 21 May 2024. https://doi.org/10.3389/fmicb.2024.1407573 (intrator2024aquaticnitrousoxide pages 1-2)
- 10.1093/ismeco/ycae020 — Pold G et al. *Phylogenetics and environmental distribution of nitric oxide-forming nitrite reductases reveal their distinct functional and ecological roles*. **ISME Communications**. Advance access 2 Feb 2024. https://doi.org/10.1093/ismeco/ycae020 (pold2024phylogeneticsandenvironmental pages 1-2)
- 10.1073/pnas.2316422121 — Murali R et al. *Diversity and evolution of nitric oxide reduction in bacteria and archaea*. **PNAS**. Jun 2024. https://doi.org/10.1073/pnas.2316422121 (murali2024diversityandevolution pages 2-4)
- 10.1186/s40793-024-00643-9 — Bano S et al. *Soil properties drive nitrous oxide accumulation patterns by shaping denitrifying bacteriomes*. **Environmental Microbiome**. Nov 2024. https://doi.org/10.1186/s40793-024-00643-9 (bano2024soilpropertiesdrive pages 1-2)
- 10.3389/fmicb.2023.1218207 — Xiang H et al. *Denitrification contributes to N2O emission in paddy soils*. **Frontiers in Microbiology**. Published 16 Jun 2023. https://doi.org/10.3389/fmicb.2023.1218207 (xiang2023denitrificationcontributesto pages 1-2)


References

1. (sennett2024determininghowoxygen pages 1-2): Louise B. Sennett, Constance A. Roco, Natalie Y. N. Lim, Joseph B. Yavitt, Peter Dörsch, Lars R. Bakken, James P. Shapleigh, and Åsa Frostegård. Determining how oxygen legacy affects trajectories of soil denitrifier community dynamics and n2o emissions. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51688-w, doi:10.1038/s41467-024-51688-w. This article has 53 citations and is from a highest quality peer-reviewed journal.

2. (schacksen2024unravelingthegenetic pages 1-2): Patrick Skov Schacksen and Jeppe Lund Nielsen. Unraveling the genetic potential of nitrous oxide reduction in wastewater treatment: insights from metagenome-assembled genomes. Sep 2024. URL: https://doi.org/10.1128/aem.02177-23, doi:10.1128/aem.02177-23. This article has 18 citations and is from a peer-reviewed journal.

3. (bano2024soilpropertiesdrive pages 1-2): Saira Bano, Qiaoyu Wu, Siyu Yu, Xinhui Wang, and Xiaojun Zhang. Soil properties drive nitrous oxide accumulation patterns by shaping denitrifying bacteriomes. Environmental Microbiome, Nov 2024. URL: https://doi.org/10.1186/s40793-024-00643-9, doi:10.1186/s40793-024-00643-9. This article has 19 citations and is from a peer-reviewed journal.

4. (intrator2024aquaticnitrousoxide pages 1-2): Naomi Intrator, Amal Jayakumar, and Bess B. Ward. Aquatic nitrous oxide reductase gene (nosz) phylogeny and environmental distribution. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1407573, doi:10.3389/fmicb.2024.1407573. This article has 19 citations and is from a peer-reviewed journal.

5. (roothans2024aerobicdenitrificationas pages 1-2): Nina Roothans, Minke Gabriëls, Thomas Abeel, Martin Pabst, Mark C M van Loosdrecht, and Michele Laureni. Aerobic denitrification as an n2o source from microbial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae116, doi:10.1093/ismejo/wrae116. This article has 34 citations.

6. (roothans2024aerobicdenitrificationas pages 8-9): Nina Roothans, Minke Gabriëls, Thomas Abeel, Martin Pabst, Mark C M van Loosdrecht, and Michele Laureni. Aerobic denitrification as an n2o source from microbial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae116, doi:10.1093/ismejo/wrae116. This article has 34 citations.

7. (xiang2023denitrificationcontributesto pages 1-2): Hua Xiang, Yiguo Hong, Jiapeng Wu, Yu Wang, Fei Ye, Jiaqi Ye, Jing Lu, and Aimin Long. Denitrification contributes to n2o emission in paddy soils. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1218207, doi:10.3389/fmicb.2023.1218207. This article has 41 citations and is from a peer-reviewed journal.

8. (pold2024phylogeneticsandenvironmental pages 1-2): Grace Pold, Germán Bonilla-Rosso, Aurélien Saghaï, Marc Strous, Christopher M Jones, and Sara Hallin. Phylogenetics and environmental distribution of nitric oxide-forming nitrite reductases reveal their distinct functional and ecological roles. ISME Communications, Jan 2024. URL: https://doi.org/10.1093/ismeco/ycae020, doi:10.1093/ismeco/ycae020. This article has 29 citations and is from a peer-reviewed journal.

9. (xiang2023denitrificationcontributesto pages 2-3): Hua Xiang, Yiguo Hong, Jiapeng Wu, Yu Wang, Fei Ye, Jiaqi Ye, Jing Lu, and Aimin Long. Denitrification contributes to n2o emission in paddy soils. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1218207, doi:10.3389/fmicb.2023.1218207. This article has 41 citations and is from a peer-reviewed journal.

10. (murali2024diversityandevolution pages 2-4): Ranjani Murali, Laura A. Pace, Robert A. Sanford, L. M. Ward, Mackenzie M. Lynes, Roland Hatzenpichler, Usha F. Lingappa, Woodward W. Fischer, Robert B. Gennis, and James Hemp. Diversity and evolution of nitric oxide reduction in bacteria and archaea. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2316422121, doi:10.1073/pnas.2316422121. This article has 34 citations and is from a highest quality peer-reviewed journal.

11. (pold2024phylogeneticsandenvironmental pages 8-11): Grace Pold, Germán Bonilla-Rosso, Aurélien Saghaï, Marc Strous, Christopher M Jones, and Sara Hallin. Phylogenetics and environmental distribution of nitric oxide-forming nitrite reductases reveal their distinct functional and ecological roles. ISME Communications, Jan 2024. URL: https://doi.org/10.1093/ismeco/ycae020, doi:10.1093/ismeco/ycae020. This article has 29 citations and is from a peer-reviewed journal.

12. (pold2024phylogeneticsandenvironmental pages 12-13): Grace Pold, Germán Bonilla-Rosso, Aurélien Saghaï, Marc Strous, Christopher M Jones, and Sara Hallin. Phylogenetics and environmental distribution of nitric oxide-forming nitrite reductases reveal their distinct functional and ecological roles. ISME Communications, Jan 2024. URL: https://doi.org/10.1093/ismeco/ycae020, doi:10.1093/ismeco/ycae020. This article has 29 citations and is from a peer-reviewed journal.

13. (sennett2024determininghowoxygen pages 6-7): Louise B. Sennett, Constance A. Roco, Natalie Y. N. Lim, Joseph B. Yavitt, Peter Dörsch, Lars R. Bakken, James P. Shapleigh, and Åsa Frostegård. Determining how oxygen legacy affects trajectories of soil denitrifier community dynamics and n2o emissions. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51688-w, doi:10.1038/s41467-024-51688-w. This article has 53 citations and is from a highest quality peer-reviewed journal.

14. (intrator2024aquaticnitrousoxide pages 12-12): Naomi Intrator, Amal Jayakumar, and Bess B. Ward. Aquatic nitrous oxide reductase gene (nosz) phylogeny and environmental distribution. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1407573, doi:10.3389/fmicb.2024.1407573. This article has 19 citations and is from a peer-reviewed journal.

15. (bano2024soilpropertiesdrive pages 9-13): Saira Bano, Qiaoyu Wu, Siyu Yu, Xinhui Wang, and Xiaojun Zhang. Soil properties drive nitrous oxide accumulation patterns by shaping denitrifying bacteriomes. Environmental Microbiome, Nov 2024. URL: https://doi.org/10.1186/s40793-024-00643-9, doi:10.1186/s40793-024-00643-9. This article has 19 citations and is from a peer-reviewed journal.