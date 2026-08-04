---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:13:59.310232'
end_time: '2026-08-04T03:22:51.170704'
duration_seconds: 531.86
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: psychrophilic
  trait_identifier: METPO:1000614
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: psychrophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature preference in which growth is favored at low temperatures,\
    \ typically near or below ~15 \xB0C."
  parent_traits: METPO:1000613
  synonyms: ''
  evidence_summary: 'DOI:10.1038/sj.embor.7400662: growing well at temperatures around
    the freezing point of water (Supports psychrophilic growth at low temperatures.)
    | PMID:28919459: psychrophilic Arctic bacterium Psychrobacter sp. DAB_AL43B (Organism
    example: Psychrobacter sp. DAB_AL43B is described as psychrophilic.)'
  causal_graph_summary: 'psychrophilic_cold_adaptation: 13 nodes, 11 edges'
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
- **Trait label:** psychrophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000614
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at low temperatures, typically near or below ~15 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Supports psychrophilic growth at low temperatures.) | PMID:28919459: psychrophilic Arctic bacterium Psychrobacter sp. DAB_AL43B (Organism example: Psychrobacter sp. DAB_AL43B is described as psychrophilic.)
- **Existing causal graph summary:** psychrophilic_cold_adaptation: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/psychrophilic.yaml`.

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
- **Trait label:** psychrophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000614
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at low temperatures, typically near or below ~15 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Supports psychrophilic growth at low temperatures.) | PMID:28919459: psychrophilic Arctic bacterium Psychrobacter sp. DAB_AL43B (Organism example: Psychrobacter sp. DAB_AL43B is described as psychrophilic.)
- **Existing causal graph summary:** psychrophilic_cold_adaptation: 13 nodes, 11 edges

## Research Objective

Research the microbial trait **psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/psychrophilic.yaml`.

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


# Curation-focused research report: psychrophilic

## Trait record and scope

- **Trait label:** psychrophilic
- **Trait identifier:** **METPO:1000614**
- **Category / kind:** ENVIRONMENT / CLASS
- **Parent:** METPO:1000613
- **Working definition:** a temperature preference in which microbial growth is favored at low temperature, typically near or below 15 °C.

For curation, the most reproducible operational definition is the classical growth-profile criterion: growth at 0 °C, an optimum at or below 15 °C, and a maximum growth temperature at or below 20 °C. This is stronger than merely detecting survival, metabolism, or growth at refrigerator temperature. **Psychrotolerant/psychrotrophic** organisms also grow near 0–5 °C but generally have optima above 15–20 °C and upper growth limits around 20–30 °C. For example, *Pseudomonas syringae* Lz4W grows from 0 to 30 °C with an optimum at 22 °C and is therefore psychrotolerant, not psychrophilic, despite extensive cold-adaptation machinery. Likewise, *Pseudomonas fragi* D12 is explicitly described as a psychrotroph. Their mechanisms are valuable supporting models but should not by themselves establish METPO:1000614 (ramon2023ageneraloverview pages 1-2, bao2023miningofkey pages 1-2, pavankumar2021molecularinsightsinto pages 1-4).

The phenotype should be assigned from a measured growth-rate curve or equivalent quantitative assay. Survival after freezing, cold-shock induction, cold-active enzyme production, isolation from ice, or possession of an antifreeze protein is insufficient alone. Medium, salinity, pressure, oxygen, incubation duration, and whether the assay measures lag, growth rate, or final biomass should be retained as experimental qualifiers.

### Biological scope and boundary cases

Psychrophily is a systems phenotype rather than a single pathway. Cooling slows chemical reaction rates and nutrient transport, increases water and cytoplasmic viscosity, rigidifies membranes, stabilizes inhibitory RNA structures, promotes protein misfolding, and—because oxygen becomes more soluble—can increase oxidative stress. Freezing introduces additional water-activity, osmotic, and mechanical ice damage. Microbes counter these constraints through coordinated membrane, enzyme, RNA, protein-folding, cryoprotection, transport, and redox modules (purwar2024adaptationsofpsychrophilic pages 8-10, hassan2020temperaturedrivenmembrane pages 1-2, bao2023miningofkey pages 1-2, pavankumar2021molecularinsightsinto pages 1-4).

Do not conflate:

1. **Psychrophily** with psychrotolerance or transient cold-shock tolerance.
2. **Growth below 0 °C** with growth in pure water: brines and intracellular solutes depress freezing and alter water activity.
3. **Cold-active enzyme** with psychrophilic organism: a mesophile may encode or express an enzyme active at low temperature.
4. **Antifreeze/ice-binding protein** with psychrophily: IBPs occur across taxa and can mediate freezing avoidance, ice adhesion, or ice nucleation.
5. **Cold habitat association** with temperature preference: polar isolates may instead be halophilic, piezophilic, desiccation-tolerant, or psychrotolerant.

## Current mechanistic understanding

The strongest expert consensus is that cold adaptation is **multifactorial and taxon-dependent**, not a universal gene cassette. Recent reviews emphasize interacting adaptations: membrane sensing and homeoviscous remodeling, flexible enzymes, RNA chaperoning, protein quality control, compatible solutes, extracellular polymers, ice-binding proteins, antioxidant systems, and metabolic reprogramming (chauhan2023coldadaptedpseudomonas pages 3-4, purwar2024adaptationsofpsychrophilic pages 6-7, ramon2023ageneraloverview pages 1-2).

### Candidate nodes grouped by type

#### Trait and environmental nodes

- **psychrophilic — METPO:1000614**
- low temperature; growth temperature; optimum growth temperature; maximum growth temperature
- freeze–thaw cycling; extracellular ice; intracellular ice
- increased oxygen solubility; reduced nutrient diffusion; increased water/cytoplasmic viscosity
- osmotic stress; reduced water activity; oxidative stress
- cold habitats: glacier, sea ice, permafrost, polar soil, alpine soil, deep sea—use ENVO CURIEs only after exact term lookup

#### Cellular structures and localizations

- cytoplasmic/plasma membrane
- membrane phospholipid bilayer
- cytoplasm
- extracellular matrix/biofilm
- extracellular polymeric substance layer
- bacterial nucleoid, ribosome, RNA degradosome, replication fork
- cell envelope/peptidoglycan

#### Processes and pathways

- membrane homeoviscous adaptation
- fatty-acid biosynthesis — **GO:0006633**
- fatty-acid desaturation and chain branching
- protein folding — **GO:0006457**
- response to oxidative stress — **GO:0006979**
- RNA secondary-structure remodeling and RNA processing
- transcription and translation at low temperature
- DNA repair and replication-fork restart
- compatible-solute synthesis/uptake
- EPS biosynthesis and biofilm formation
- ice binding, thermal hysteresis, and ice-recrystallization inhibition
- antioxidant defense
- nutrient transport and ATP generation
- cold-active catalysis

#### Genes, proteins, enzymes, and complexes

- **des**, membrane phospholipid desaturase; **FabF**, β-ketoacyl-ACP synthase II; FabA/FabB/FabH; KAS-II/III; fatty-acid cis/trans isomerase
- cold-shock proteins/Csps, functioning as RNA chaperones
- DnaK/Hsp70, Hsc66, GroEL, GroES, and Clp proteases/chaperones
- RNase R and RNA degradosome components
- RecBCD and RuvAB DNA-repair/recombination complexes
- catalase and superoxide dismutase
- ice-binding proteins, antifreeze proteins, ice-recrystallization-inhibiting proteins
- InaZ ice-nucleating protein; *Marinomonas primoryensis* MpAFP adhesin
- cold-active α-amylases, proteases, lipases, cellulases, DNA polymerases, and other taxon-specific enzymes
- *P. syringae* Lz4W candidates: **trmE**, **aat**, **hutU**, cold-active RNA polymerase
- *P. fragi* D12 candidates: three low-temperature-upregulated pili-associated genes; exact locus identifiers should be taken from the article supplement before curation

#### Chemicals and metabolites

- unsaturated fatty acids; monounsaturated and polyunsaturated fatty acids
- cis-vaccenic acid; palmitoleoyl-ACP; branched iso- and anteiso-fatty acids; EPA and DHA
- membrane phospholipids and hopanoids
- glycine betaine, choline, glycerol, trehalose, mannitol, sorbitol, sarcosine, proline, spermidine, and putrescine
- reactive oxygen species; hydrogen peroxide; superoxide
- ATP
- carotenoids, violacein, melanin, and other protective pigments
- polyhydroxyalkanoates/polyhydroxybutyrate and phasins

Chemical CURIEs should be added only after authoritative ChEBI lookup; this report deliberately avoids guessing them.

## Candidate causal graph

The following table summarizes the proposed graph architecture. In a YAML implementation, broad mechanisms should be separated from organism-specific evidence and annotated with evidence strength.

| subject | predicate | object | evidence context/taxon | confidence |
|---|---|---|---|---|
| low temperature | decreases | membrane fluidity / causes membrane rigidification | General bacterial cold stress; reviews and glacier isolates (purwar2024adaptationsofpsychrophilic pages 8-10, hassan2020temperaturedrivenmembrane pages 1-2, pavankumar2021molecularinsightsinto pages 1-4) | High |
| fatty-acid desaturase (`des`); fatty-acid biosynthetic process (GO:0006633) | increases | unsaturated fatty acids | Mechanistic review citing *Bacillus subtilis* desaturase system and cold-induced unsaturation (ramon2023ageneraloverview pages 4-5) | High |
| unsaturated fatty acids | maintains | membrane fluidity | General psychrophile/psychrotolerant mechanism; *Pseudomonas syringae* Lz4W and glacial isolates (hassan2020temperaturedrivenmembrane pages 1-2, pavankumar2021molecularinsightsinto pages 1-4, ramon2023ageneraloverview pages 4-5) | High |
| branched fatty acids | maintains | membrane fluidity | Glacial psychrophilic bacteria; branched FAs >70% of analyzed FAs, temperature-responsive (hassan2020temperaturedrivenmembrane pages 1-2) | High |
| low temperature | induces | cold-shock proteins / RNA chaperones | General cold response in bacteria (purwar2024adaptationsofpsychrophilic pages 6-7, ramon2023ageneraloverview pages 1-2, pavankumar2021molecularinsightsinto pages 7-10) | High |
| cold-shock proteins / RNA chaperones | promotes | transcription/translation at low temperature | *Pseudomonas fragi* D12 and *Pseudomonas syringae* Lz4W; restoration of transcription/translation and mRNA structure handling (bao2023miningofkey pages 1-2, pavankumar2021molecularinsightsinto pages 7-10) | High |
| molecular chaperones; protein folding (GO:0006457) | promotes | protein folding/stabilization during cold stress | Hsc66/Hsp70-family and GroEL/DnaK/GroES/Clp evidence in reviews and *P. fragi* low-temperature response (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 6-7, bao2023miningofkey pages 1-2) | High |
| cold-adapted enzyme flexibility | increases | catalytic activity at low temperature | General psychrophilic enzyme mechanism; lower activation enthalpy and shifted temperature optimum (chauhan2023coldadaptedpseudomonas pages 3-4, ramon2023ageneraloverview pages 7-8) | High |
| cold-adapted enzyme flexibility | trades off with | thermal stability / earlier inactivation at higher temperature | General psychrophilic enzyme tradeoff from mechanistic review (ramon2023ageneraloverview pages 7-8) | High |
| compatible solutes | protects against | freezing / ice damage / osmotic stress | Glycine, betaine, choline, glycerol, trehalose, mannitol, sorbitol in cold-tolerant microbes (purwar2024adaptationsofpsychrophilic pages 10-11, bao2023miningofkey pages 1-2) | High |
| extracellular polymeric substances (EPS) | promotes | cryoprotection / adhesion / biofilm formation | *P. fragi* D12 and general reviews; EPS lower freezing point around cells and support biofilm (bao2023miningofkey pages 1-2, yang2023insightintothe pages 1-2) | High |
| ice-binding proteins / antifreeze proteins | inhibits | ice recrystallization / damaging ice crystal growth | General IBP/AFP mechanism across microbes (purwar2024adaptationsofpsychrophilic pages 6-7, białkowska2020icebindingproteins pages 3-5, ramon2023ageneraloverview pages 12-14) | High |
| low temperature / increased oxygen solubility | increases | reactive oxygen species | General cold-stress mechanism in reviews and *P. fragi* context (purwar2024adaptationsofpsychrophilic pages 10-11, bao2023miningofkey pages 1-2) | High |
| catalase / superoxide dismutase | reduces | oxidative damage; response to oxidative stress (GO:0006979) | General antioxidant defense in cold-tolerant microbes and *P. fragi* genome summary (bao2023miningofkey pages 1-2, bao2023miningofkey pages 6-7) | High |
| RecBCD and RuvAB | enables | replication fork reestablishment / DNA repair at low temperature | *Pseudomonas syringae* Lz4W review (pavankumar2021molecularinsightsinto pages 1-4) | Moderate-High |
| RNaseR | promotes | RNA processing at low temperature | *Pseudomonas syringae* Lz4W review; efficient degradosome/RNaseR activity in cold (pavankumar2021molecularinsightsinto pages 1-4) | Moderate-High |
| METPO:1000614 psychrophilic | associated with | membrane, RNA, enzyme, cryoprotectant, and oxidative-stress adaptations | Trait-level synthesis from recent reviews (purwar2024adaptationsofpsychrophilic pages 8-10, ramon2023ageneraloverview pages 1-2) | High |
| *Pseudomonas fragi* D12 | upregulates | pili-associated genes under low temperature | 124 candidate cold-adaptation genes; 19 unique; 3 pili genes significantly upregulated (bao2023miningofkey pages 1-2) | Moderate |
| *Pseudomonas fragi* D12 | responds to 30°C→15°C by increasing | membrane-fluidity maintenance, EPS, compatible solutes, ROS reduction | Temperature-step-specific transcriptomic/genomic interpretation (bao2023miningofkey pages 1-2) | High |
| *Pseudomonas fragi* D12 | responds to 15°C→4°C by increasing | molecular chaperones and transcription factors | Temperature-step-specific adaptation restoring normal transcription/translation (bao2023miningofkey pages 1-2) | High |
| *Bacillus simplex* H-b | increases | unsaturated fatty-acid proportion at low temperature | 5°C, 20°C, 30°C transcriptomics/physiology (yang2023insightintothe pages 1-2) | High |
| *Bacillus simplex* H-b | accumulates | ATP and EPS at 5°C | Cold-adaptation during aerobic denitrification; supports survival and nitrogen removal (yang2023insightintothe pages 1-2) | High |
| *Bacillus simplex* H-b | shifts nitrogen use toward | assimilation over dissimilation at low temperature | Low-temperature denitrification physiology at 5°C (yang2023insightintothe pages 1-2) | Moderate |
| *Bacillus simplex* H-b | achieves | 27.22% nitrogen removal at 5°C | Application-linked quantitative phenotype in wastewater context (yang2023insightintothe pages 1-2) | High |


*Table: This table summarizes the strongest candidate subject-predicate-object edges for a psychrophilic TraitMech graph, emphasizing mechanisms with direct experimental or review support. It is useful as a compact starting point for curation because it separates broadly supported trait-level edges from organism-specific edges and confidence levels.*

### Detailed evidence-backed triples

| Proposed subject–predicate–object triple | Reference and supporting snippet | Curation note |
|---|---|---|
| low temperature → **decreases** → membrane fluidity | Hassan et al. report “decreased cell membrane fluidity” among the challenges of cold and experimentally cultured 42 glacier isolates at 5, 15, 25, and 35 °C (published 14 May 2020; DOI: [10.3389/fmicb.2020.00824](https://doi.org/10.3389/fmicb.2020.00824)) (hassan2020temperaturedrivenmembrane pages 1-2) | Strong general physical edge; environmental conditions should qualify it. |
| low temperature → **induces** → membrane fatty-acid remodeling | In 42 glacial isolates, straight-chain monounsaturated and branched fatty acids comprised more than 70% of analyzed fatty acids; branched-fatty-acid abundance changed significantly with temperature, and PUFAs occurred only at lower temperatures (hassan2020temperaturedrivenmembrane pages 1-2). | Strong experimental association across isolates, but not proof that every psychrophile uses the same lipid class. |
| des / fatty-acid desaturase → **increases** → membrane unsaturation | A 2023 mechanistic review states that *B. subtilis* **des** encodes its membrane fatty-acid desaturase and introduces unsaturation into existing saturated fatty acids (published July 2023; DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4)) (ramon2023ageneraloverview pages 4-5). | High-confidence mechanism, but *B. subtilis* is a model for cold response rather than an obligate psychrophile. |
| FabF → **increases** → cis-vaccenic acid | The same review identifies FabF as the key enzyme catalyzing elongation of palmitoleoyl-ACP toward cis-vaccenoyl-ACP; rapid cis-vaccenic-acid increase occurs after cooling (ramon2023ageneraloverview pages 4-5). | Curate as a taxon/context-specific membrane edge, not a universal psychrophile requirement. |
| unsaturated/anteiso-branched fatty acids → **increase or maintain** → membrane fluidity | Cold adaptation in *B. subtilis* includes switching from iso- to lower-melting anteiso-fatty acids; anteiso-C15:0 is also reported as beneficial in Antarctic bacteria (ramon2023ageneraloverview pages 4-5). | Strong biochemical rationale; medium isoleucine can control branching, so retain nutrient context. |
| reduced membrane fluidity → **activates** → membrane cold-sensing/two-component signaling | Cooling increases membrane rigidity and thickness; membrane mismatch changes sensor conformation and initiates adaptive signaling, including the DesK/DesR paradigm (ramon2023ageneraloverview pages 4-5). | Mechanistically strong but taxon-specific. A generic “membrane cold sensor” node is safer at trait level. |
| localized enzyme flexibility / reduced activation enthalpy → **increases** → low-temperature catalytic rate | Psychrophilic enzymes have reduced activation enthalpy and more negative activation entropy than mesophilic orthologues, making activity less temperature-dependent; a cited psychrophilic α-amylase had maximal catalytic efficiency at 20 °C versus 60 °C for its mesophilic counterpart (ramon2023ageneraloverview pages 7-8). | Strong general enzyme-level mechanism. Avoid asserting that whole-protein global flexibility is always causal; active-site-localized flexibility is more precise. |
| cold-active enzyme flexibility → **reduces** → thermal stability | Psychrophilic enzymes have lower temperature optima and stability, and many lose activity before global unfolding because the active site is comparatively labile (ramon2023ageneraloverview pages 7-8). | Curate as an activity–stability tradeoff, not an absolute rule without enzyme-specific measurements. |
| cold-shock proteins → **remodel** → structured RNA | Csps are described as RNA chaperones that destabilize cold-stabilized secondary structures, supporting expression at low temperature (pavankumar2021molecularinsightsinto pages 7-10). | Strong process-level edge; individual Csp paralog functions require organism-specific evidence. |
| low temperature → **increases** → molecular chaperone/protein-quality-control activity | GroEL, DnaK, GroES, and Clp proteins are reported as continuously upregulated at low temperature; in *P. fragi* D12, cooling from 15 to 4 °C increased chaperones and transcription factors, restoring transcription and translation (purwar2024adaptationsofpsychrophilic pages 6-7, bao2023miningofkey pages 1-2). | Strong for D12; broader edge supported mainly by synthesis literature. |
| compatible-solute accumulation → **reduces** → freezing/osmotic/ice-crystal damage | Glycine, betaine, choline, glycerol, trehalose, mannitol, and sorbitol can accumulate without disrupting cellular activity and alter ice-crystal microstructure (bao2023miningofkey pages 1-2). | Strong protective mechanism, but identity and dominant function vary by taxon and salinity. |
| EPS → **reduces** → extracellular freezing damage | EPS are described as cryoprotectants that reduce the local freezing point, promote adhesion/aggregation/biofilm formation, and protect extracellular enzymes from cold deformation (bao2023miningofkey pages 1-2). | Good process edge; “reduces freezing point” can be concentration- and composition-dependent. |
| AFP/IBP → **inhibits** → ice growth and recrystallization | AFP thermal hysteresis lowers the freezing point, while ice-recrystallization inhibition prevents larger damaging crystals; together these activities keep crystals “small and non-lethal” (published February 2020; DOI: [10.3390/biom10020274](https://doi.org/10.3390/biom10020274)) (białkowska2020icebindingproteins pages 3-5). | High-confidence molecular function. Do not treat all IBPs as AFPs: ice-nucleating proteins have the opposite proximal effect. |
| MpAFP-mediated ice adhesion → **maintains** → access to oxygen and nutrients | The 1.5-MDa Ca²⁺-dependent *M. primoryensis* adhesin anchors the bacterium to ice while projecting it away from incorporation, keeping it near oxygen- and nutrient-rich water (białkowska2020icebindingproteins pages 3-5). | Strong, striking, but highly taxon-specific. |
| InaZ → **promotes** → extracellular ice nucleation | *P. syringae* InaZ orders water into an ice lattice; ice nucleation can damage plant tissue and provide nutrient access (ramon2023ageneraloverview pages 12-14). | Do **not** curate as a generic psychrophily mechanism; this is also a virulence/ecological trait. |
| low temperature / increased oxygen solubility → **increases** → ROS burden | Recent synthesis states that oxygen solubility and ROS concentration rise at low temperature, causing oxidative damage (purwar2024adaptationsofpsychrophilic pages 10-11, bao2023miningofkey pages 1-2). | Plausible broad edge, but ROS should ideally be supported by direct measurements in each curated taxon. |
| catalase and superoxide dismutase → **decrease** → oxidative damage | Cold-tolerant microorganisms produce catalase and SOD to counter cold-associated ROS; *P. fragi* D12 showed ROS reduction during the 30→15 °C response (bao2023miningofkey pages 1-2). | Enzyme-to-ROS edge is strong; link to psychrophilic growth remains context dependent. |
| RecBCD and RuvAB → **enable** → replication-fork reestablishment at low temperature | The *P. syringae* Lz4W synthesis identifies “RecBCD- and RuvAB-dependent reestablishment of replication fork” as part of cold function (published November 2021; DOI: [10.1111/1462-2920.15304](https://doi.org/10.1111/1462-2920.15304)) (pavankumar2021molecularinsightsinto pages 1-4). | Moderate-to-high confidence, explicitly psychrotolerant and strain-specific. |
| RNase R/degradosome activity → **supports** → RNA processing at low temperature | Efficient degradosome machinery and hydrolytic RNase R processing are identified in *P. syringae* Lz4W (pavankumar2021molecularinsightsinto pages 1-4). | Useful taxon-specific subgraph; avoid universalization. |
| trmE expression → **supports** → low-temperature tRNA function | In Lz4W, **trmE**, encoding a tRNA-modification GTPase, is upregulated at low temperature; its reported optimum is 12–18 °C versus approximately 30 °C in mesophilic bacteria (pavankumar2021molecularinsightsinto pages 7-10). | Candidate edge, but psychrotolerant model and indirect phenotype support. |
| aat → **is required for** → cold growth | Aspartate aminotransferase gene **aat** is described as essential for Lz4W cold growth (pavankumar2021molecularinsightsinto pages 7-10). | Potentially curatable after checking the original knockout study cited by the review. |
| low temperature → **increases** → hutU expression | **hutU** expression increased 14-fold at 4 °C relative to 22 °C in Lz4W, potentially supporting histidine utilization (pavankumar2021molecularinsightsinto pages 7-10). | Mark uncertain: expression and proposed carbon-use role do not prove causality for psychrophily. |
| cooling 30→15 °C in *P. fragi* D12 → **increases** → membrane adaptation, EPS, compatible solutes, and ROS control | The primary study explicitly reports these coordinated responses (published 6 July 2023; DOI: [10.3389/fmicb.2023.1215837](https://doi.org/10.3389/fmicb.2023.1215837)) (bao2023miningofkey pages 1-2). | Strong temperature-step evidence, but D12 is psychrotrophic. |
| cooling 15→4 °C in *P. fragi* D12 → **increases** → chaperones and transcription factors | The same study reports increased expression “enabling the bacteria to restore normal transcription and translation” (bao2023miningofkey pages 1-2). | Strong transcriptomic interpretation; individual regulators require locus-level extraction. |
| low temperature → **upregulates** → three pili-associated genes in *P. fragi* D12 | Genome/transcriptome analysis identified 124 candidate cold-adaptation genes, 19 unique candidates, and three unique pili-associated genes significantly upregulated under cold conditions (bao2023miningofkey pages 1-2). | **Uncertain causal edge:** upregulation is association, and authors use “may be the key.” Do not curate as necessary/sufficient without mutants. |
| low temperature in *Bacillus simplex* H-b → **increases** → unsaturated fatty acids, ATP, and EPS | Experiments at 5, 20, and 30 °C found a higher unsaturated-fatty-acid proportion and ATP/EPS accumulation at low temperature (published 19 January 2023; DOI: [10.1128/aem.01928-22](https://doi.org/10.1128/aem.01928-22)) (yang2023insightintothe pages 1-2). | Strong physiological association; the strain grows over 5–37 °C and should not automatically be assigned strict psychrophily. |
| coordinated cold adaptation in *B. simplex* H-b → **supports** → nitrogen removal at 5 °C | H-b achieved 27.22% nitrogen removal at 5 °C, with nitrogen shifted toward assimilation rather than dissimilatory transformation (yang2023insightintothe pages 1-2). | Application-linked, strain- and assay-specific; not a core psychrophily-defining edge. |

## Recent developments and quantitative findings

1. **Temperature-stage-specific adaptation.** The 2023 *P. fragi* D12 study indicates that “cold adaptation” is not one response: moderate cooling from 30 to 15 °C favored membrane/EPS/solute/redox adjustments, whereas 15 to 4 °C emphasized chaperones and transcriptional regulation. Its genome yielded 124 candidate cold-adaptation genes, including 19 designated unique candidates, but only three pili-associated genes were highlighted as significantly upregulated (bao2023miningofkey pages 1-2, bao2023miningofkey pages 6-7).

2. **Cold denitrification as a systems phenotype.** At 5 °C, *B. simplex* H-b retained growth and 27.22% nitrogen removal. Transcriptomic and physiological observations implicated unsaturated lipids, EPS, ATP, membrane transport, cofactors/vitamins, nucleotide precursors, translation, and oxidative/temperature-stress responses rather than a single “psychrophile gene” (yang2023insightintothe pages 1-2).

3. **Membrane lipid diversity beyond unsaturation.** In 42 non-polar glacier isolates, monounsaturated and branched fatty acids jointly represented more than 70% of measured fatty acids; PUFAs appeared only at lower temperatures. A separate synthesis reports that unsaturated hopanoids in *Methylovulum psychrotolerans* increased from 27% at 20 °C to 49% at 4 °C (hassan2020temperaturedrivenmembrane pages 1-2, ramon2023ageneraloverview pages 4-5).

4. **Mechanistic refinement of cold-active enzymes.** The current view is not simply “more flexible proteins.” Reduced activation enthalpy and local active-site flexibility preserve catalysis at low temperature, while increased lability commonly lowers thermal stability. This creates an exploitable activity–stability tradeoff but complicates industrial formulation (ramon2023ageneraloverview pages 7-8).

5. **Omics produces hypotheses, not automatically causal edges.** Recent genome and transcriptome studies greatly expand candidate lists, but gene enrichment or differential expression rarely demonstrates necessity or sufficiency. Mutant complementation, controlled lipid manipulation, purified-enzyme kinetics, or rescue experiments remain necessary for high-confidence gene-to-trait edges.

## Applications and real-world implementation

- **Cold wastewater treatment:** H-b removed nitrate, nitrite, and ammonium at 5 °C and provides a candidate for winter/cold-region nitrogen treatment, although the reported 27.22% removal indicates room for process optimization (yang2023insightintothe pages 1-2).
- **Low-temperature biocatalysis:** cold-active proteases, lipases, amylases, cellulases, β-galactosidases, and polymerases can support food processing, cold-water detergents, molecular biology, textiles, wastewater processing, and bioremediation while reducing heating demand. Their low thermal stability can also permit inexpensive post-process inactivation (chauhan2023coldadaptedpseudomonas pages 3-4, ramon2023ageneraloverview pages 7-8).
- **Bioremediation:** cold-adapted *Pseudomonas* strains combine low-temperature metabolism with extracellular enzymes and xenobiotic-degradation potential; *P. fragi* D12 contained many metabolism and xenobiotic-related annotations, though genomic potential does not guarantee field performance (chauhan2023coldadaptedpseudomonas pages 3-4, bao2023miningofkey pages 6-7).
- **Agriculture:** psychrophilic/psychrotolerant phosphate-solubilizing and plant-growth-promoting bacteria are candidates for cold soils and high-altitude agriculture. Field persistence, host specificity, biosafety, and formulation stability remain limiting factors.
- **Cryopreservation and food:** AFP/IBP ice-recrystallization inhibition can protect frozen foods, cells, tissues, and biologics. Ice-nucleating proteins require separate risk/use assessment because they promote rather than suppress nucleation (pathania2021adaptationtocold pages 109-111, białkowska2020icebindingproteins pages 3-5).
- **Astrobiology:** cold-active RNA polymerase, repair, RNA processing, solute, and membrane systems in Lz4W illustrate how metabolism can persist near 0 °C, but terrestrial brines and nutrient-rich laboratory media should not be treated as direct analogues of extraterrestrial habitability (pavankumar2021molecularinsightsinto pages 1-4).

## Recommended TraitMech graph structure

A conservative first graph should use a central environmental chain:

**low temperature → membrane rigidification / slow catalysis / structured RNA / protein misfolding / freezing-osmotic stress / ROS → adaptive modules → maintenance of cellular functions → growth near or below 15 °C → METPO:1000614**.

The most defensible core modules are:

1. fatty-acid remodeling → membrane fluidity;
2. cold-active enzyme kinetics → metabolic flux at low temperature;
3. Csps/RNA processing → transcription and translation;
4. molecular chaperones → protein folding;
5. compatible solutes and EPS → cryo/osmoprotection;
6. AFP/IBP activity → control of ice growth/recrystallization;
7. catalase/SOD → oxidative-stress control;
8. DNA repair/replication restart → genome maintenance.

Species-specific genes should sit in subordinate evidence branches, not directly under the trait node, unless loss- and gain-of-function evidence establishes a causal path to the measured growth-temperature phenotype.

## Warnings: claims not yet ready for TraitMech curation

- Do not assign **METPO:1000614** to *P. fragi* D12, *P. syringae* Lz4W, or *B. simplex* H-b solely from the studies summarized here; they are psychrotrophic or have broad temperature ranges.
- Do not curate the three D12 pili genes as causal for psychrophily. They are significantly upregulated candidates, not validated determinants.
- Do not treat a genomic inventory of desaturases, chaperones, IBPs, or compatible-solute genes as phenotype evidence.
- Do not make “all psychrophiles increase unsaturated fatty acids” universal. Some taxa rely heavily on chain shortening, branching, ether-lipid changes, pigments, hopanoids, or other strategies.
- Do not merge AFPs with ice-nucleating proteins. AFPs inhibit damaging ice growth/recrystallization; INPs initiate ice formation and can contribute to virulence.
- Do not curate glycerol synthesis in Lz4W as established; the source explicitly presents it as speculation (pavankumar2021molecularinsightsinto pages 1-4).
- Do not use reduced enzyme stability as a universal defining property; it is a frequent tradeoff requiring enzyme-specific kinetic and unfolding measurements.
- Avoid causal predicates such as “causes psychrophily” for transcriptomic or comparative-genomic findings. Prefer “associated with,” “upregulated during,” or “candidate contributor to.”
- Validate all ontology identifiers against the current authoritative release before YAML insertion. Label-only nodes are preferable to invented or approximate CURIEs.

## DOI-first bibliography

1. Purwar S, Srivastava S. **Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.** *Applied Microbiology: Theory & Technology*. Published October 2024. DOI: [10.37256/amtt.5220244537](https://doi.org/10.37256/amtt.5220244537) (purwar2024adaptationsofpsychrophilic pages 3-4, purwar2024adaptationsofpsychrophilic pages 8-10).
2. Ramón A, Esteves A, Villadóniga C, Chalar C, Castro-Sowinski S. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology* 54:2259–2287. Published July 2023. DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4) (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 12-14, ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 7-8).
3. Bao C et al. **Mining of key genes for cold adaptation from Pseudomonas fragi D12 and analysis of its cold-adaptation mechanism.** *Frontiers in Microbiology* 14:1215837. Published 6 July 2023. DOI: [10.3389/fmicb.2023.1215837](https://doi.org/10.3389/fmicb.2023.1215837) (bao2023miningofkey pages 1-2, bao2023miningofkey pages 6-7).
4. Yang Q et al. **Insight into the Cold Adaptation Mechanism of an Aerobic Denitrifying Bacterium: Bacillus simplex H-b.** *Applied and Environmental Microbiology* 89(2). Published 19 January 2023; issue February 2023. DOI: [10.1128/aem.01928-22](https://doi.org/10.1128/aem.01928-22) (yang2023insightintothe pages 1-2).
5. Chauhan M, Kimothi A, Sharma A, Pandey A. **Cold adapted Pseudomonas: ecology to biotechnology.** *Frontiers in Microbiology* 14. Published July 2023. DOI: [10.3389/fmicb.2023.1218708](https://doi.org/10.3389/fmicb.2023.1218708) (chauhan2023coldadaptedpseudomonas pages 3-4).
6. Hassan N et al. **Temperature Driven Membrane Lipid Adaptation in Glacial Psychrophilic Bacteria.** *Frontiers in Microbiology* 11:824. Published 14 May 2020. DOI: [10.3389/fmicb.2020.00824](https://doi.org/10.3389/fmicb.2020.00824) (hassan2020temperaturedrivenmembrane pages 1-2).
7. Pavankumar TL, Mittal P, Hallsworth JE. **Molecular insights into the ecology of a psychrotolerant Pseudomonas syringae.** *Environmental Microbiology* 23:3665–3681. Published November 2021. DOI: [10.1111/1462-2920.15304](https://doi.org/10.1111/1462-2920.15304) (pavankumar2021molecularinsightsinto pages 7-10, pavankumar2021molecularinsightsinto pages 1-4).
8. Białkowska A, Majewska E, Olczak A, Twarda-Clapa A. **Ice Binding Proteins: Diverse Biological Roles and Applications in Different Types of Industry.** *Biomolecules* 10:274. Published February 2020. DOI: [10.3390/biom10020274](https://doi.org/10.3390/biom10020274) (białkowska2020icebindingproteins pages 3-5).
9. Pathania S et al. **Adaptation to Cold Environment: The Survival Strategy of Psychrophiles.** In *Survival Strategies in Cold-adapted Microorganisms*, pp. 87–111. Published December 2021. DOI: [10.1007/978-981-16-2625-8_4](https://doi.org/10.1007/978-981-16-2625-8_4) (pathania2021adaptationtocold pages 109-111).

References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

2. (bao2023miningofkey pages 1-2): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

3. (pavankumar2021molecularinsightsinto pages 1-4): Theetha L. Pavankumar, Pragya Mittal, and John E. Hallsworth. Molecular insights into the ecology of a psychrotolerant <i>pseudomonas syringae</i>. Environmental Microbiology, 23:3665-3681, Nov 2021. URL: https://doi.org/10.1111/1462-2920.15304, doi:10.1111/1462-2920.15304. This article has 35 citations and is from a domain leading peer-reviewed journal.

4. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

5. (hassan2020temperaturedrivenmembrane pages 1-2): Noor Hassan, Alexandre M. Anesio, Muhammad Rafiq, Jens Holtvoeth, Ian Bull, Abdul Haleem, Aamer Ali Shah, and Fariha Hasan. Temperature driven membrane lipid adaptation in glacial psychrophilic bacteria. Frontiers in Microbiology, May 2020. URL: https://doi.org/10.3389/fmicb.2020.00824, doi:10.3389/fmicb.2020.00824. This article has 129 citations and is from a peer-reviewed journal.

6. (chauhan2023coldadaptedpseudomonas pages 3-4): Mansi Chauhan, Ayushi Kimothi, Avinash Sharma, and Anita Pandey. Cold adapted pseudomonas: ecology to biotechnology. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1218708, doi:10.3389/fmicb.2023.1218708. This article has 83 citations and is from a peer-reviewed journal.

7. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

8. (ramon2023ageneraloverview pages 4-5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

9. (pavankumar2021molecularinsightsinto pages 7-10): Theetha L. Pavankumar, Pragya Mittal, and John E. Hallsworth. Molecular insights into the ecology of a psychrotolerant <i>pseudomonas syringae</i>. Environmental Microbiology, 23:3665-3681, Nov 2021. URL: https://doi.org/10.1111/1462-2920.15304, doi:10.1111/1462-2920.15304. This article has 35 citations and is from a domain leading peer-reviewed journal.

10. (ramon2023ageneraloverview pages 7-8): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

11. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.

12. (yang2023insightintothe pages 1-2): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Applied and Environmental Microbiology, Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 19 citations and is from a peer-reviewed journal.

13. (białkowska2020icebindingproteins pages 3-5): Aneta Białkowska, Edyta Majewska, Aleksandra Olczak, and Aleksandra Twarda-Clapa. Ice binding proteins: diverse biological roles and applications in different types of industry. Biomolecules, 10:274, Feb 2020. URL: https://doi.org/10.3390/biom10020274, doi:10.3390/biom10020274. This article has 121 citations.

14. (ramon2023ageneraloverview pages 12-14): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

15. (bao2023miningofkey pages 6-7): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

16. (pathania2021adaptationtocold pages 109-111): Shruti Pathania, Preeti Solanki, Chayanika Putatunda, Ravi Kant Bhatia, and Abhishek Walia. Adaptation to cold environment: the survival strategy of psychrophiles. Survival Strategies in Cold-adapted Microorganisms, pages 87-111, Dec 2021. URL: https://doi.org/10.1007/978-981-16-2625-8\_4, doi:10.1007/978-981-16-2625-8\_4. This article has 27 citations.

17. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 6 citations.