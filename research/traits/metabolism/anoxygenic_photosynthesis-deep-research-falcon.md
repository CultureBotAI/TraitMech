---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:03:22.582002'
end_time: '2026-06-18T04:33:11.404370'
duration_seconds: 1788.82
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: anoxygenic photosynthesis
  trait_identifier: traitmech:000035
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: anoxygenic_photosynthesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phototrophic metabolism that uses light energy with a single photosystem
    and bacteriochlorophyll, using electron donors other than water (e.g. H2S, H2,
    Fe(II), organics) and therefore not evolving oxygen. Characteristic of purple
    and green sulfur bacteria, Chloroflexi, and heliobacteria.
  parent_traits: traitmech:000038
  synonyms: bacterial photosynthesis
  evidence_summary: 'DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard describe anoxygenic
    photosynthesis across five prokaryotic phyla using bacteriochlorophyll and a single
    photosystem without O2 evolution.) | DOI:10.3389/fmicb.2024.1417714:  (Review
    of anoxygenic photosynthesis in green sulfur bacteria supports sulfide as electron
    donor and the absence of oxygen production.)'
  causal_graph_summary: 'anoxygenic_photosynthesis_sulfide_donor: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** anoxygenic photosynthesis
- **METPO identifier:** traitmech:000035
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy with a single photosystem and bacteriochlorophyll, using electron donors other than water (e.g. H2S, H2, Fe(II), organics) and therefore not evolving oxygen. Characteristic of purple and green sulfur bacteria, Chloroflexi, and heliobacteria.
- **Parent traits:** traitmech:000038
- **Synonyms:** bacterial photosynthesis
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard describe anoxygenic photosynthesis across five prokaryotic phyla using bacteriochlorophyll and a single photosystem without O2 evolution.) | DOI:10.3389/fmicb.2024.1417714:  (Review of anoxygenic photosynthesis in green sulfur bacteria supports sulfide as electron donor and the absence of oxygen production.)
- **Existing causal graph summary:** anoxygenic_photosynthesis_sulfide_donor: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **anoxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anoxygenic_photosynthesis.yaml`.

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
- **Trait label:** anoxygenic photosynthesis
- **METPO identifier:** traitmech:000035
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy with a single photosystem and bacteriochlorophyll, using electron donors other than water (e.g. H2S, H2, Fe(II), organics) and therefore not evolving oxygen. Characteristic of purple and green sulfur bacteria, Chloroflexi, and heliobacteria.
- **Parent traits:** traitmech:000038
- **Synonyms:** bacterial photosynthesis
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard describe anoxygenic photosynthesis across five prokaryotic phyla using bacteriochlorophyll and a single photosystem without O2 evolution.) | DOI:10.3389/fmicb.2024.1417714:  (Review of anoxygenic photosynthesis in green sulfur bacteria supports sulfide as electron donor and the absence of oxygen production.)
- **Existing causal graph summary:** anoxygenic_photosynthesis_sulfide_donor: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **anoxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anoxygenic_photosynthesis.yaml`.

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


# Curation-Focused Research Report: Anoxygenic Photosynthesis (TraitMech: traitmech:000035)

## Scope summary (Trait semantics)
Anoxygenic photosynthesis is a bacteriochlorophyll-based phototrophic metabolism that captures light energy without oxidizing water and therefore does **not evolve O2**. It is typically associated with a **single photochemical reaction center** (Type I or Type II depending on lineage) and uses electron donors such as **H2S** (common in green and purple sulfur bacteria), **Fe(II)** (photoferrotrophy), H2, thiosulfate, and/or organics rather than water. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, nishihara2024illuminatingthecoevolution pages 1-2)

Key distinctions and boundary cases:
- **Oxygenic photosynthesis** (cyanobacteria) uses water as the electron donor and produces O2; anoxygenic phototrophs use other donors such as sulfide, and are often found deeper in water columns below oxygenic phototrophs. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- **Aerobic anoxygenic phototrophs (AAPs)** are a boundary case: they retain anoxygenic photosystems/pigments but rely on aerobic respiration (definition not curated here as a separate trait but relevant for exclusions). (yurkov2025phenomenaldiversityof pages 1-3)
- **Novel evolutionary boundary cases** exist where reaction-center class is atypical for a lineage, e.g., a Chloroflexota phototroph with a **Type I reaction center** despite other Chloroflexota phototrophs typically using Type II. (tsuji2024anoxygenicphototrophof pages 1-2, tsuji2024anoxygenicphototrophof pages 2-3)

## Current understanding: key concepts and mechanistic definitions
### Reaction center types
- **Type I reaction centers (RCI; Fe–S/ferredoxin-reducing)** occur in heliobacteria and green sulfur bacteria; recent high-resolution structures show homodimeric cores (PshA or PscA) with cofactors supporting electron transfer via [4Fe–4S] clusters (FX, FA/FB) and special pairs (P800/P840). (niederman2024whatweare pages 1-2)
- **Type II reaction centers (RCII; quinone-reducing)** are characteristic of purple bacteria and are mechanistically distinct from homodimeric Type I systems (contrast explicitly discussed in the Type I RC-PS review). (niederman2024whatweare pages 1-2)

### Light-harvesting structures
Green sulfur bacteria (GSB) possess **chlorosomes**, lipid-monolayer vesicles housing photosynthetic pigments and functioning as light-harvesting antennas, enabling growth under low light. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)

### Electron donors and products
- In sulfur-based anoxygenic photosynthesis, **H2S serves as a principal electron donor** and is oxidized to **elemental sulfur (S0)** (especially in GSB). (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- In photoferrotrophy, **Fe(II)** oxidation is coupled to anoxygenic photosynthesis, a metabolism proposed to have been important in early ferruginous oceans. (nikeleit2024inhibitionofphototrophic pages 1-2)

### Carbon fixation coupling
Anoxygenic photosynthesis often couples to autotrophy; rTCA is explicitly associated with GSB carbon assimilation, and CBB cycle genes/enzymes occur in some newly described phototroph lineages, indicating multiple evolutionary/physiological routes to phototrophic autotrophy. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, li2023globallydistributedmyxococcota pages 7-8)

## Recent developments (prioritizing 2023–2024)
### 1) New phototrophic diversity and reaction-center evolution (Nature 2024)
A cultivated Chloroflexota phototroph (“Candidatus Chlorohelix allophototropha”) uses a **Type I reaction center** and **chlorosomes** (absorbance peak at 749 nm; electron-transparent spherical chlorosome-like structures), and contains multiple bacteriochlorophyll c species plus bacteriochlorophyll a as a reaction-center pigment. This provides a mechanistically grounded boundary case for curation: **reaction-center class (RCI) + chlorosome architecture** within a phylum known for RCII phototrophy. (tsuji2024anoxygenicphototrophof pages 2-3, tsuji2024anoxygenicphototrophof pages 1-2)

### 2) Structural resolution of homodimeric Type I RC-photosystems (Biomolecules 2024)
Recent cryo-EM/X-ray structures clarify subunit composition and electron transfer architecture of Type I RC-PS complexes across heliobacteria, green sulfur bacteria, and chloracidobacteria, including key subunits (PscA core; PscC cytochromes; PscB containing FA/FB; PscD/PscZ; and antenna proteins such as FMO connecting chlorosomes to the RC). (niederman2024whatweare pages 1-2)

### 3) Mechanistic electron transfer within GSB reaction centers (Photosynthesis Research 2024)
A targeted mechanistic study in *Chlorobaculum tepidum* supports the causal step that **P840+ is rapidly reduced by electron transfer from PscC** (cytochrome cZ), with the (PscA)2–(PscC)2 complex forming an electron-transfer pathway; FMO is described as an interconnecting antenna mediating excitation transfer from chlorosomes to the RC. (lyratzakis2024thesynergybetween pages 1-2)

### 4) Environmental inhibition of photoferrotrophy by reactive nitrogen species (Nature Geoscience 2024)
Microbial incubations and modelling show that nitrate-reducing Fe(II) oxidizers can both **outcompete photoferrotrophs for dissolved Fe(II)** and **inhibit photoferrotrophy via toxic intermediates**, including nitric oxide; susceptibility occurs across multiple photoferrotroph strains despite genomic NO detoxification capacity. This is directly relevant for causal edges connecting nitrogen cycling to suppression of anoxygenic phototrophic Fe(II) oxidation. (nikeleit2024inhibitionofphototrophic pages 1-2)

### 5) Genomic expansion of anoxygenic phototrophy beyond classic taxa (Nature Communications 2023)
Myxococcota metagenome-assembled genomes contain photosynthesis gene clusters (PGCs) and show diverse carotenoid gene complements; some genomes contain complete/near-complete CBB cycles (RuBisCO form I and PRK), supporting potential phototrophic autotrophy and/or mixotrophy in unexpected lineages. This is promising but requires biochemical validation for TraitMech curation (see warnings). (li2023globallydistributedmyxococcota pages 7-8)

## Candidate nodes (grouped) and ontology grounding
A consolidated node list (with suggested CURIEs where clear) is provided in the curation table below.

| Node Type | Node Label | Suggested CURIE | Evidence Citation |
|---|---|---|---|
| Process / Pathway | Anoxygenic photosynthesis | GO:0015979 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, nishihara2024illuminatingthecoevolution pages 1-2) |
| Process / Pathway | Photoferrotrophy | - | (nikeleit2024inhibitionofphototrophic pages 1-2) |
| Process / Pathway | Reverse tricarboxylic acid (rTCA) cycle | KEGG:M00173 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, ogola2025thiocapsalutimaribacterand pages 18-20) |
| Process / Pathway | Calvin-Benson-Bassham (CBB) cycle | KEGG:M00165 | (li2023globallydistributedmyxococcota pages 7-8) |
| Process / Pathway | Sulfide oxidation | GO:0004138 | (ogola2025thiocapsalutimaribacterand pages 18-20) |
| Complex | Type I reaction center (RCI) | GO:0055038 | (tsuji2024anoxygenicphototrophof pages 1-2, niederman2024whatweare pages 1-2) |
| Complex | Type II reaction center (RCII) | GO:0055039 | (tsuji2024anoxygenicphototrophof pages 1-2, niederman2024whatweare pages 1-2) |
| Complex | Chlorosome | GO:0046858 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, tsuji2024anoxygenicphototrophof pages 1-2) |
| Complex | Fenna-Matthews-Olson (FMO) protein | - | (lyratzakis2024thesynergybetween pages 1-2, niederman2024whatweare pages 1-2) |
| Gene / Protein | pscA/B/C/D (RCI subunits) | - | (lyratzakis2024thesynergybetween pages 1-2, niederman2024whatweare pages 1-2) |
| Gene / Protein | pufL/pufM (RCII subunits) | - | (ogola2025thiocapsalutimaribacterand pages 18-20, yurkov2025phenomenaldiversityof pages 12-14) |
| Gene / Protein | bch (Bacteriochlorophyll synthesis genes) | - | (ogola2025thiocapsalutimaribacterand pages 18-20, yurkov2025phenomenaldiversityof pages 12-14) |
| Gene / Protein | sqr (Sulfide quinone oxidoreductase) | EC:1.8.5.4 | (ogola2025thiocapsalutimaribacterand pages 18-20) |
| Metabolite / Chemical | Hydrogen sulfide (H2S) | CHEBI:16136 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, nishihara2024illuminatingthecoevolution pages 1-2) |
| Metabolite / Chemical | Elemental sulfur (S0) | CHEBI:29346 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, ye2024comparativestudyof pages 1-2) |
| Metabolite / Chemical | Fe(II) / Ferrous iron | CHEBI:29033 | (tsuji2024anoxygenicphototrophof pages 1-2, nishihara2024illuminatingthecoevolution pages 1-2) |
| Metabolite / Chemical | Nitric oxide (NO) | CHEBI:16480 | (nikeleit2024inhibitionofphototrophic pages 1-2) |
| Environmental Factor | Light (radiant energy) | ENVO:01001021 | (tsuji2024anoxygenicphototrophof pages 1-2, ye2024comparativestudyof pages 1-2) |
| Taxa | Green sulfur bacteria (GSB) | NCBITaxon:191412 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, niederman2024whatweare pages 1-2) |
| Taxa | Purple sulfur bacteria (PSB) | NCBITaxon:1053 | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, ogola2025thiocapsalutimaribacterand pages 18-20) |

| Edge (Subject–Predicate–Object) | Evidence Snippet | Source | Notes / Uncertainty | Suggested Node Groundings |
|---|---|---|---|---|
| Hydrogen sulfide `is_electron_donor_for` Anoxygenic photosynthesis | "hydrogen sulfide (H2S) is used as the main electron donor, which differs from plants or cyanobacteria where water is the main source" | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | Defining mechanism for green and purple sulfur bacteria. | CHEBI:16136, GO:0015979 |
| Fe(II) `is_electron_donor_for` Anoxygenic photosynthesis | "enabled extraction of electrons from previously inaccessible electron donors, exemplified by H2O, H2S, and Fe2+" | (nishihara2024illuminatingthecoevolution pages 1-2) | Defines photoferrotrophy; ecologically significant in Archean environments. | CHEBI:29033, GO:0015979 |
| Anoxygenic photosynthesis `produces` Elemental sulfur | "GSB oxidize H2S to elemental sulfur." | (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | Heavily utilized in photobioreactors for sulfide detoxification. | GO:0015979, CHEBI:29346 |
| Type I reaction center `enables` Anoxygenic photosynthesis | "an anoxygenic phototroph... uses a type I reaction centre (RCI) for light energy conversion" | (tsuji2024anoxygenicphototrophof pages 1-2, tsuji2024anoxygenicphototrophof pages 2-3) | Homodimeric RC core utilized by GSB, heliobacteria, and a newly discovered Chloroflexota lineage. | GO:0055038, GO:0015979 |
| Type II reaction center `enables` Anoxygenic photosynthesis | "catalyze the transmembrane charge separations resulting in the respective reduction of [4Fe-4S] centers and Q molecules" | (niederman2024whatweare pages 1-2) | Heterodimeric RC utilized by purple bacteria and most Chloroflexota. | GO:0055039, GO:0015979 |
| pscC `transfers_electrons_to` pscA | "P840+ is rapidly reduced by electron transfer from one of the two PscC subunits... mediate the transfer of electrons... to P840 special pair" | (lyratzakis2024thesynergybetween pages 1-2) | Mechanistic protein-protein interactions specific to GSB electron transport. | None, None |
| sqr `enables` Sulfide oxidation | "sqr gene encodes sulfide quinone oxidoreductase... crucial role in energy production for sulfur-oxidizing bacteria" | (ogola2025thiocapsalutimaribacterand pages 18-20) | Mechanistic linkage linking phototrophy to the sulfur cycle. | EC:1.8.5.4, GO:0004138 |
| Nitric oxide `inhibits` Photoferrotrophy | "nitrate-reducing Fe(II) oxidizers inhibit photoferrotrophy via the production of toxic intermediates... nitric oxide" | (nikeleit2024inhibitionofphototrophic pages 1-2) | Strong toxicity observed across 4 strains despite genomic detoxification capabilities. | CHEBI:16480, traitmech:000035 |
| Light `increases` Sulfate removal | "effluent pH value of the photoreactor were significantly higher... accumulation of PSB under light conditions made the system more stable" | (ye2024comparativestudyof pages 4-6) | System stabilization via PSB-mediated oxidation of toxic sulfide intermediate. | ENVO:01001021, GO:0019343 |


*Table: Candidate nodes and causal edges for TraitMech curation of anoxygenic photosynthesis, highlighting mechanistic components (reaction centers), environmental constraints, and specific biochemical transformations.*

## Evidence-backed candidate causal edges (curation-ready)
The edge table in the artifact provides draft triples with snippets and sources. Key edges supported by primary/review evidence include:
- **H2S → electron donor for anoxygenic photosynthesis → S0 production** in GSB/PSB systems. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- **RCI enables anoxygenic photosynthesis** in diverse phyla; **RCII** in purple bacteria; Type I structure/function clarified by new RC-PS structures. (tsuji2024anoxygenicphototrophof pages 1-2, niederman2024whatweare pages 1-2)
- **PscC donates electrons to P840 special pair in PscA** (GSB mechanistic electron transfer). (lyratzakis2024thesynergybetween pages 1-2)
- **Nitrate-reducing Fe(II) oxidizers produce toxic intermediates (NO) that inhibit photoferrotrophy**. (nikeleit2024inhibitionofphototrophic pages 1-2)

### Additional gene-centered edges strongly supported by 2025 ecosystem genomics (use with caution)
In a sulfidic spring system, gene markers link anoxygenic phototrophic taxa to functional modules:
- In water column taxa, gene sets for light absorption (**pufLM, pucAB, crt**), electron transport (**cycA, petA/B/C**), and carbon fixation (**cbbL/S, cbbP/A**) co-occur with sulfur-oxidation genes (e.g., **soxABCD**), consistent with sulfur-driven anoxygenic photosynthesis coupled to carbon fixation. (ogola2025thiocapsalutimaribacterand pages 18-20)
- In sediment taxa consistent with GSB, Type I reaction-center and pigment synthesis markers (**psaA/B/C/D/E, bch, crt, fmoA**) co-occur with rTCA markers (**aclA/B**) under low-light anoxic sulfide conditions. (ogola2025thiocapsalutimaribacterand pages 18-20)
These are excellent for proposing candidate nodes/edges but may be **inference from marker genes** rather than direct physiological measurement.

## Current applications and real-world implementations (with statistics)
### 1) H2S detoxification and sulfur recovery using anoxygenic phototrophs (2024 review synthesis)
Biotechnological removal of H2S via microbial oxidation is positioned as an alternative to physico-chemical gas cleaning, with elemental sulfur as a separable product. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)

Quantitative performance examples compiled in the 2024 Frontiers review include:
- **81–95% desulfurization** in a reported system. (kushkevych2024anoxygenicphotosynthesiswith pages 15-16)
- **100% H2S removal** with **92–95% conversion to elemental sulfur** at influent loads up to **286 mg L−1 h−1** in another reported system. (kushkevych2024anoxygenicphotosynthesiswith pages 15-16)
- Reported strain/time performance: *Allochromatium vinosum* achieved **100% removal in 2 days**, and *Chlorobium limicola* up to **90% in 5 days**, while an abiotic control removed ~**33%** by absorption. (kushkevych2024anoxygenicphotosynthesiswith pages 15-16)

Implementation details (useful for experimental-factor nodes):
- Photobioreactor configurations include a **concentric-column photobioreactor with a 40 W tungsten bulb** and **tubular photobioreactors**, with tubular arrangements reported as more efficient. Biofilms were formed on **Tygon tubes** (transparent, oxygen-impermeable), with circulation for **3 days** for adhesion and wastewater flow of **72–288 h**. (kushkevych2024anoxygenicphotosynthesiswith pages 15-16)
- **Light intensity effects**: desulfurization reported as more effective at **10 kLx** than at **25 kLx**, and wavelength selection reported around **720–780 nm**. (kushkevych2024anoxygenicphotosynthesiswith pages 15-16, kushkevych2024anoxygenicphotosynthesiswith pages 16-17)

### 2) Wastewater sulfate removal and sulfide control in light-assisted UASB photoreactors (Ye et al., 2024)
A 4.8-L UASB photoreactor using 18 W fluorescent illumination (photoreactors #1–2; dark controls #3–4) achieved after start-up (28 days) **85–90% COD removal** and **>90% sulfate removal** at influent COD 1000 mg/L and sulfate 250 mg/L (COD/SO4 = 4), with HRT = 16 h (5 mL/min). (ye2024comparativestudyof pages 1-2)

Mechanistic interpretation in the study connects improved stability to light-dependent enrichment of photosynthetic sulfur bacteria (PSB), which reduce sulfide toxicity; the time-course figure and accompanying text describe higher effluent pH and improved COD removal in photoreactors consistent with sulfide removal under light. (ye2024comparativestudyof pages 4-6, ye2024comparativestudyof media fa5f0fd8)

The paper also reports that **photosynthetic sulfur bacteria and elemental sulfur were detected in the photoreactor**, and that light exposure improved sludge/community stability by degrading inhibitory substances such as H2S. (ye2024comparativestudyof pages 9-12)

## Expert opinions and analysis (authoritative interpretations)
- The 2024 Type I RC-PS structural review argues that newly resolved homodimeric Type I RC-PS structures inform both mechanism and evolution (relationships among anoxygenic Type I RC-PS and oxygenic PSI/PSII architectures). This supports mechanistic node definitions (subunits/cofactors) and also flags that RC evolution is actively being revised by new structural evidence. (niederman2024whatweare pages 1-2)
- The Nature Geoscience 2024 study provides a strong ecological/evolutionary interpretation that reactive nitrogen species produced during nitrate-dependent Fe(II) oxidation could have inhibited photoferrotroph activity in ancient oceans, affecting BIF precipitation mechanisms—an example of environmental-factor-to-trait inhibition causality. (nikeleit2024inhibitionofphototrophic pages 1-2)

## Warnings / claims not yet ready for curation
1) **Marker gene inference vs phenotype**: Ecosystem genomic studies linking pufLM/psa/bch/fmoA/cbb/acl genes to anoxygenic photosynthesis provide strong hypotheses, but absence of direct cultivation/physiology can make edges uncertain; curate as “inferred” unless validated. (ogola2025thiocapsalutimaribacterand pages 18-20, li2023globallydistributedmyxococcota pages 7-8)
2) **AAPs and mixed phototrophy**: Aerobic anoxygenic phototrophs and dual systems (e.g., rhodopsin + BChl systems) complicate trait boundaries; avoid folding rhodopsin phototrophy into this trait without explicit definition. (yurkov2025phenomenaldiversityof pages 1-3, li2023globallydistributedmyxococcota pages 7-8)
3) **Quantitative NO inhibition**: The NO/photoferrotrophy inhibition mechanism is well supported, but numeric thresholds (NO concentrations, inhibition constants) were not extractable from the available text excerpts; refrain from curating numeric parameter nodes without full data extraction. (nikeleit2024inhibitionofphototrophic pages 1-2)

## DOI-first bibliography (publication date, URL)
- Kushkevych I. et al. (11 Jul 2024). *Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments.* Frontiers in Microbiology 15. DOI:10.3389/fmicb.2024.1417714. https://doi.org/10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 15-16)
- Tsuji J.M. et al. (28 Mar 2024). *Anoxygenic phototroph of the Chloroflexota uses a type I reaction centre.* Nature 627:915–922. DOI:10.1038/s41586-024-07180-y. https://doi.org/10.1038/s41586-024-07180-y (tsuji2024anoxygenicphototrophof pages 2-3)
- Niederman R.A. (6 Mar 2024). *What We Are Learning from the Diverse Structures of the Homodimeric Type I Reaction Center-Photosystems of Anoxygenic Phototropic Bacteria.* Biomolecules 14:311. DOI:10.3390/biom14030311. https://doi.org/10.3390/biom14030311 (niederman2024whatweare pages 1-2)
- Lyratzakis A. et al. (16 Apr 2024). *The synergy between the PscC subunits for electron transfer to the P840 special pair in Chlorobaculum tepidum.* Photosynthesis Research 160:87–96. DOI:10.1007/s11120-024-01093-7. https://doi.org/10.1007/s11120-024-01093-7 (lyratzakis2024thesynergybetween pages 1-2)
- Nishihara A. et al. (Jun 2024). *Illuminating the coevolution of photosynthesis and Bacteria.* PNAS 121. DOI:10.1073/pnas.2322120121. https://doi.org/10.1073/pnas.2322120121 (nishihara2024illuminatingthecoevolution pages 1-2)
- Nikeleit V. et al. (4 Oct 2024). *Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments.* Nature Geoscience 17:1169–1174. DOI:10.1038/s41561-024-01560-9. https://doi.org/10.1038/s41561-024-01560-9 (nikeleit2024inhibitionofphototrophic pages 1-2)
- Ye Y. et al. (May 2024). *Comparative study of the removal of sulfate by UASB in light and dark environment.* Bioprocess and Biosystems Engineering 47:943–955. DOI:10.1007/s00449-024-03024-1. https://doi.org/10.1007/s00449-024-03024-1 (ye2024comparativestudyof pages 1-2, ye2024comparativestudyof pages 4-6, ye2024comparativestudyof pages 9-12, ye2024comparativestudyof media fa5f0fd8)
- Li L. et al. (Oct 2023). *Globally distributed Myxococcota with photosynthesis gene clusters illuminate the origin and evolution of a potentially chimeric lifestyle.* Nature Communications 14. DOI:10.1038/s41467-023-42193-7. https://doi.org/10.1038/s41467-023-42193-7 (li2023globallydistributedmyxococcota pages 7-8)
- Ogola H.J.O. et al. (May 2025). *Thiocapsa, Lutimaribacter, and Delftia... coupling of sulfur oxidation and nutrient recycling...* Biology 14:503. DOI:10.3390/biology14050503. https://doi.org/10.3390/biology14050503 (ogola2025thiocapsalutimaribacterand pages 18-20)


References

1. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

2. (nishihara2024illuminatingthecoevolution pages 1-2): Arisa Nishihara, Yusuke Tsukatani, Chihiro Azai, and Masaru K. Nobu. Illuminating the coevolution of photosynthesis and bacteria. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2322120121, doi:10.1073/pnas.2322120121. This article has 33 citations and is from a highest quality peer-reviewed journal.

3. (yurkov2025phenomenaldiversityof pages 1-3): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

4. (tsuji2024anoxygenicphototrophof pages 1-2): J. M. Tsuji, N. A. Shaw, S. Nagashima, J. J. Venkiteswaran, S. L. Schiff, T. Watanabe, M. Fukui, S. Hanada, M. Tank, and J. D. Neufeld. Anoxygenic phototroph of the chloroflexota uses a type i reaction centre. Nature, 627:915-922, Mar 2024. URL: https://doi.org/10.1038/s41586-024-07180-y, doi:10.1038/s41586-024-07180-y. This article has 29 citations and is from a highest quality peer-reviewed journal.

5. (tsuji2024anoxygenicphototrophof pages 2-3): J. M. Tsuji, N. A. Shaw, S. Nagashima, J. J. Venkiteswaran, S. L. Schiff, T. Watanabe, M. Fukui, S. Hanada, M. Tank, and J. D. Neufeld. Anoxygenic phototroph of the chloroflexota uses a type i reaction centre. Nature, 627:915-922, Mar 2024. URL: https://doi.org/10.1038/s41586-024-07180-y, doi:10.1038/s41586-024-07180-y. This article has 29 citations and is from a highest quality peer-reviewed journal.

6. (niederman2024whatweare pages 1-2): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

7. (nikeleit2024inhibitionofphototrophic pages 1-2): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

8. (li2023globallydistributedmyxococcota pages 7-8): Liuyang Li, Danyue Huang, Yaoxun Hu, Nicola M. Rudling, Daniel P. Canniffe, Fengping Wang, and Yinzhao Wang. Globally distributed myxococcota with photosynthesis gene clusters illuminate the origin and evolution of a potentially chimeric lifestyle. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42193-7, doi:10.1038/s41467-023-42193-7. This article has 73 citations and is from a highest quality peer-reviewed journal.

9. (lyratzakis2024thesynergybetween pages 1-2): Alexandros Lyratzakis, Vangelis Daskalakis, Hao Xie, and Georgios Tsiotis. The synergy between the pscc subunits for electron transfer to the p840 special pair in chlorobaculum tepidum. Photosynthesis Research, 160:87-96, Apr 2024. URL: https://doi.org/10.1007/s11120-024-01093-7, doi:10.1007/s11120-024-01093-7. This article has 1 citations and is from a peer-reviewed journal.

10. (ogola2025thiocapsalutimaribacterand pages 18-20): Henry Joseph Oduor Ogola, Ramganesh Selvarajan, Somandla Ncube, and Lawrence Madikizela. Thiocapsa, lutimaribacter, and delftia are major bacterial taxa facilitating the coupling of sulfur oxidation and nutrient recycling in the sulfide-rich isinuka spring in south africa. Biology, 14:503, May 2025. URL: https://doi.org/10.3390/biology14050503, doi:10.3390/biology14050503. This article has 4 citations.

11. (yurkov2025phenomenaldiversityof pages 12-14): Vladimir Yurkov and Katia Messner. Phenomenal diversity of the photosynthetic apparatus evolved in aerobic anoxygenic phototrophs. Microorganisms, 13:2446, Oct 2025. URL: https://doi.org/10.3390/microorganisms13112446, doi:10.3390/microorganisms13112446. This article has 2 citations.

12. (ye2024comparativestudyof pages 1-2): Yuanyao Ye, Xueyi Yan, Hui Luo, Jianxiong Kang, Dongqi Liu, Yongzheng Ren, Huu Hao Ngo, Wenshan Guo, Dongle Cheng, and Wei Jiang. Comparative study of the removal of sulfate by uasb in light and dark environment. Bioprocess and biosystems engineering, 47:943-955, May 2024. URL: https://doi.org/10.1007/s00449-024-03024-1, doi:10.1007/s00449-024-03024-1. This article has 0 citations and is from a peer-reviewed journal.

13. (ye2024comparativestudyof pages 4-6): Yuanyao Ye, Xueyi Yan, Hui Luo, Jianxiong Kang, Dongqi Liu, Yongzheng Ren, Huu Hao Ngo, Wenshan Guo, Dongle Cheng, and Wei Jiang. Comparative study of the removal of sulfate by uasb in light and dark environment. Bioprocess and biosystems engineering, 47:943-955, May 2024. URL: https://doi.org/10.1007/s00449-024-03024-1, doi:10.1007/s00449-024-03024-1. This article has 0 citations and is from a peer-reviewed journal.

14. (kushkevych2024anoxygenicphotosynthesiswith pages 15-16): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

15. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

16. (ye2024comparativestudyof media fa5f0fd8): Yuanyao Ye, Xueyi Yan, Hui Luo, Jianxiong Kang, Dongqi Liu, Yongzheng Ren, Huu Hao Ngo, Wenshan Guo, Dongle Cheng, and Wei Jiang. Comparative study of the removal of sulfate by uasb in light and dark environment. Bioprocess and biosystems engineering, 47:943-955, May 2024. URL: https://doi.org/10.1007/s00449-024-03024-1, doi:10.1007/s00449-024-03024-1. This article has 0 citations and is from a peer-reviewed journal.

17. (ye2024comparativestudyof pages 9-12): Yuanyao Ye, Xueyi Yan, Hui Luo, Jianxiong Kang, Dongqi Liu, Yongzheng Ren, Huu Hao Ngo, Wenshan Guo, Dongle Cheng, and Wei Jiang. Comparative study of the removal of sulfate by uasb in light and dark environment. Bioprocess and biosystems engineering, 47:943-955, May 2024. URL: https://doi.org/10.1007/s00449-024-03024-1, doi:10.1007/s00449-024-03024-1. This article has 0 citations and is from a peer-reviewed journal.