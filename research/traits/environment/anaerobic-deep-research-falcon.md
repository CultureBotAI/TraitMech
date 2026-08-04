---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:06:26.971635'
end_time: '2026-08-04T00:14:50.605557'
duration_seconds: 503.63
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: anaerobic
  trait_identifier: METPO:1000603
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: anaerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference in which growth occurs in the absence of molecular\
    \ oxygen (O\u2082)."
  parent_traits: METPO:1000601
  synonyms: Ox_anaerobic, anaerobe
  evidence_summary: 'PMID:21413255: Anaerobes, on the other hand, cannot grow in the
    presence of oxygen (Supports anaerobic growth as growth without molecular oxygen.)
    | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides
    fragilis is described as an anaerobic organism.)'
  causal_graph_summary: 'anaerobic_trait_oxygen_exclusion: 10 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000603
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth occurs in the absence of molecular oxygen (O₂).
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_anaerobic, anaerobe
- **Existing evidence:** PMID:21413255: Anaerobes, on the other hand, cannot grow in the presence of oxygen (Supports anaerobic growth as growth without molecular oxygen.) | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides fragilis is described as an anaerobic organism.)
- **Existing causal graph summary:** anaerobic_trait_oxygen_exclusion: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/anaerobic.yaml`.

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
- **Trait label:** anaerobic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000603
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference in which growth occurs in the absence of molecular oxygen (O₂).
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_anaerobic, anaerobe
- **Existing evidence:** PMID:21413255: Anaerobes, on the other hand, cannot grow in the presence of oxygen (Supports anaerobic growth as growth without molecular oxygen.) | PMID:22778399: obligate anaerobe Bacteroides fragilis (Organism example: Bacteroides fragilis is described as an anaerobic organism.)
- **Existing causal graph summary:** anaerobic_trait_oxygen_exclusion: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/anaerobic.yaml`.

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


# Curation report: microbial trait **anaerobic**

## Executive curation recommendation

**Trait label:** anaerobic  
**Trait identifier:** **METPO:1000603**  
**Category:** ENVIRONMENT  
**Term kind:** CLASS  
**Mapping status:** REVIEWED  
**Parent:** METPO:1000601

The trait should represent **demonstrated microbial growth in the absence of molecular oxygen**, not merely survival after oxygen exposure, residence in an anoxic habitat, possession of anaerobic-metabolism genes, or performance of one oxygen-sensitive reaction. Its most defensible core causal chain is:

> absence/depletion of O₂ → availability and use of non-O₂ electron-disposal routes → redox-carrier regeneration and/or energy conservation → biomass growth under anoxic conditions.

Two mechanistic branches should be represented separately: **anaerobic respiration**, in which an electron-transport chain terminates at a non-O₂ acceptor, and **fermentation**, in which redox balance is maintained without an external respiratory acceptor. For obligate anaerobes, an additional inhibitory branch is well supported: O₂ exposure → direct inactivation of oxygen-labile enzymes plus formation of reactive oxygen species (ROS) → metabolic damage → growth arrest or loss of viability. Oxygen-scavenging and ROS-defense systems modify tolerance but do not, by themselves, establish the anaerobic-growth phenotype. (little2024dietaryandhostderived pages 1-3, sun2023anodeassistedelectrofermentationwith pages 1-2, khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 9-11)

## 1. Trait scope and boundary cases

### 1.1 Positive scope

METPO:1000603 is appropriately assigned when an organism **grows under an experimentally anoxic condition**—that is, in the absence of measurable O₂. A 2024 methodological review explicitly separates the environmental term *anoxic* from metabolism: anoxic denotes an environment or culture setting that is oxygen-free or below the detection limit, whereas anaerobic describes metabolism conducted without measurable oxygen. This distinction is important because an organism isolated from an anoxic environment is not necessarily an anaerobe. (keating2024microbialsinglecellapplications pages 1-2)

The assay should record, where available:

- medium and electron donor;
- terminal electron acceptor, if any;
- headspace composition and reducing agent;
- measured dissolved O₂ or detection limit;
- inoculum form, because aggregates and coexisting aerobes can consume or shield against O₂;
- evidence of growth, such as cell counts, optical density, protein, colony formation, or serial transfer—not substrate turnover alone.

Okabe and colleagues warned that biofilms, aggregates, or coexisting aerobes can make anaerobic organisms appear more oxygen tolerant than planktonic cells, illustrating why assay configuration belongs in evidence metadata. (okabe2023oxygentoleranceand pages 1-2)

### 1.2 Nearby traits that must remain distinct

| Nearby term | Distinction from METPO:1000603 |
|---|---|
| **Obligate/strict anaerobe** | An organism-level dependency: O₂ blocks growth. It is a narrower phenotype than simply being capable of anaerobic growth. |
| **Facultative anaerobe** | Grows both with and without O₂, switching among aerobic respiration, anaerobic respiration, and/or fermentation. *Bacillus subtilis* is a documented example. (sun2023anodeassistedelectrofermentationwith pages 1-2) |
| **Aerotolerant anaerobe** | Does not use O₂ for growth but survives exposure through scavenging, detoxification, repair, or community shielding. Survival is not equivalent to growth. |
| **Microaerophile** | Requires or preferentially grows at low, but nonzero, O₂. This should not be curated as anaerobic unless growth at zero measurable O₂ is independently demonstrated. |
| **Anoxic environment** | An environmental state, not an organismal metabolic phenotype. (keating2024microbialsinglecellapplications pages 1-2) |
| **Anaerobic respiration** | A mechanism supporting anaerobic growth: an electron-transport chain uses a terminal acceptor other than O₂. |
| **Fermentation** | A separate mechanism: internal organic intermediates dispose of electrons without a respiratory terminal acceptor. (little2024dietaryandhostderived pages 1-3, sun2023anodeassistedelectrofermentationwith pages 1-2) |
| **Oxygen tolerance** | Capacity to remain viable or active during O₂ exposure. Strict anaerobes may possess substantial tolerance without growing aerobically. |
| **Dormant spore survival in air** | Does not demonstrate anaerobic growth or vegetative oxygen tolerance. |

The literature no longer supports the simplistic rule that obligate anaerobes merely lack catalase or superoxide dismutase. Obligate anaerobiosis can instead arise from oxygen-labile, low-potential metal centers and radical enzymes that are indispensable to central metabolism, while the same organism may retain multiple O₂- and ROS-detoxification systems. (khademian2020doreactiveoxygen pages 1-2, khademian2021howmicrobesevolved pages 1-3)

## 2. Candidate nodes grouped by type

Identifiers below are limited to high-confidence mappings; uncertain entities are deliberately left label-only rather than assigned invented CURIEs.

### Trait and environmental nodes

- **anaerobic** — `METPO:1000603`
- **anoxic environment/culture** — label-only pending exact ENVO assay-context selection
- **hypoxic environment** — label-only; do not conflate with anoxia
- **oxic–anoxic interface** — label-only
- **absence of measurable molecular oxygen** — experimental-factor node
- **oxygen concentration / dissolved oxygen** — quantitative experimental factor

### Chemicals, oxidants, donors, and acceptors

- molecular oxygen — `CHEBI:15379`
- hydrogen peroxide — `CHEBI:16240`
- superoxide — `CHEBI:18421`
- nitrate — `CHEBI:17632`
- sulfate — `CHEBI:16189`
- fumarate — `CHEBI:29806`
- carbon dioxide — `CHEBI:16526`
- ammonium — `CHEBI:28938`
- nitrite — label/CHEBI mapping should be validated in the target ontology release
- Fe(III), Mn(IV), dimethyl sulfoxide, trimethylamine N-oxide, itaconate, resveratrol, phenazine-1-carboxylate, pyruvate, formate, H₂, NADH, and NAD⁺ — candidate chemical nodes; validate exact protonation-state CURIEs before YAML entry
- poised anode/cathode — experimental device/electron-sink node, not a chemical

### Processes and metabolic modules

- anaerobic respiration — `GO:0009061`
- fermentation — `GO:0006113`
- electron-transport chain — label or validated GO term
- anaerobic ammonium oxidation (anammox) — label or validated GO term
- dissimilatory sulfate reduction — label or validated GO/MetaCyc pathway
- nitrate respiration, fumarate respiration, sulfur-compound respiration, methanogenesis, acetogenesis, and Stickland fermentation — pathway candidates
- oxygen reduction, ROS detoxification, oxidized-protein repair, redox-carrier regeneration, ATP generation, and biomass growth — process nodes

### Enzymes, proteins, regulators, and complexes

**Oxygen/ROS defense:** flavodiiron proteins; FdpA/CD1157; FdpF/CD1623; rubrerythrin; reverse rubrerythrins revRbr1/CD1474 and revRbr2/CD1524; superoxide reductase; superoxide dismutase; catalase; catalase-peroxidase KatG; alkyl hydroperoxide reductase Ahp; cytochrome-c peroxidase; rubredoxin:oxygen oxidoreductase Roo/NorV; cytochrome-bd oxidase CydAB; thioredoxin TrxA/TrxB; methionine-sulfoxide reductase MsrA; and ClpB–DnaK/GroLS repair systems. (botin2023thetoleranceof pages 1-2, dyksma2024growthofsulfatereducing pages 1-2, caulat2024physiologicalroleand pages 1-2)

**Regulation:** σB, σA, OseR (Spx-family oxygen-sensitive regulator), Rex, FNR, ArcAB, OxyR, PerR, and SoxRS. The C. difficile regulatory edges are experimentally supported; FNR/ArcAB should be treated as facultative-anaerobe modules rather than universal anaerobe nodes. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 13-15)

**Anaerobic respiratory modules:** nitrate reductases NarGHI/Nap, fumarate reductase, DMSO/TMAO reductases, respiratory molybdopterin/flavin reductases, and quinones. Little et al. detected respiratory-reductase families across more than 1,533 gut prokaryotic species and experimentally identified 22 electron-acceptor metabolites in three bacterial families. (little2024dietaryandhostderived pages 9-11, little2024dietaryandhostderived pages 1-3)

**Sulfate reduction:** sulfate adenylyltransferase Sat; APS reductase AprAB; dissimilatory sulfite reductase DsrAB; DsrC; electron-transfer complexes QmoAB(C) and DsrMK(JOP); and regulator/activator DsrD. (dyksma2024growthofsulfatereducing pages 1-2)

**Oxygen-sensitive metabolic targets:** pyruvate:formate lyase (PFL), pyruvate:ferredoxin oxidoreductase (PFOR), fumarase, aconitase, isopropylmalate isomerase, low-potential ferredoxins, glycyl-radical enzymes, and [4Fe–4S] dehydratases. (khademian2020doreactiveoxygen pages 1-2, imlay2013themolecularmechanisms pages 6-8, lu2021whenanaerobesencounter pages 9-11, lu2021whenanaerobesencounter pages 8-9)

### Taxon-context nodes

Candidate exemplars include *Clostridioides difficile*, *Bacteroides thetaiotaomicron*, *Faecalibacterium* spp., *Fusobacterium nucleatum*, marine “Candidatus Scalindua,” freshwater *Brocadia*, *Jettenia*, and *Kuenenia*, sulfate-reducing Desulfobacterota/Bacillota, and facultative *Bacillus subtilis*. Exact `NCBITaxon` identifiers should be resolved against the strain or species named in each source rather than inferred at genus level.

## 3. Evidence-backed candidate causal edges

The following are the recommended high-value edges for curation. Quoted snippets are kept short and source-faithful.

| Subject–predicate–object triple | Reference | Supporting snippet | Curation note |
|---|---|---|---|
| **absence of measurable O₂ — enables — anaerobic metabolism** | Keating et al., 2024, DOI [10.1128/aem.01321-24](https://doi.org/10.1128/aem.01321-24), published 30 Sep 2024 | “anaerobic (conducted in the absence of measurable oxygen)” | **Strong scope edge.** Environment/process definition, not sufficient alone to prove organismal growth. (keating2024microbialsinglecellapplications pages 1-2) |
| **anaerobic respiration — uses — non-O₂ terminal electron acceptor** | Sun et al., 2023, DOI [10.1186/s13068-022-02253-4](https://doi.org/10.1186/s13068-022-02253-4) | “nitrate, sulphate, fumarate, iron (III), manganese (IV) or CO₂ are used as the terminal electron acceptor” | **Strong general edge.** Individual acceptor use remains taxon-specific. (sun2023anodeassistedelectrofermentationwith pages 1-2) |
| **fermentation — is mechanistically distinct from — anaerobic respiration** | Little et al., 2024, DOI [10.1038/s41564-023-01560-2](https://doi.org/10.1038/s41564-023-01560-2) | respiratory metabolism transfers electrons “through an electron transport chain to terminal acceptors” | **Strong distinction.** Do not require a respiratory reductase for all anaerobic growth. (little2024dietaryandhostderived pages 1-3) |
| **molecular O₂ — directly inactivates — PFL and PFOR** | Khademian & Imlay, 2020, DOI [10.1111/mmi.14516](https://doi.org/10.1111/mmi.14516) | “PFL and PFOR…lose activity upon aeration”; PFOR damage was unaffected by superoxide or peroxide | **Strong but taxon-demonstrated in B. thetaiotaomicron.** Supports a direct-O₂ injury branch distinct from ROS. (khademian2020doreactiveoxygen pages 1-2) |
| **superoxide/H₂O₂ — oxidatively damage — [4Fe–4S] enzymes** | Imlay, 2013, DOI [10.1038/nrmicro3032](https://doi.org/10.1038/nrmicro3032) | superoxide “directly inactivates [4Fe-4S] clusters in dehydratases” | **Strong foundational mechanism.** Broadly relevant, but specific damaged enzymes vary by taxon. (imlay2013themolecularmechanisms pages 6-8) |
| **reduced flavins/low-potential centers + O₂ — generate — ROS** | Lu & Imlay, 2021, DOI [10.1038/s41579-021-00583-y](https://doi.org/10.1038/s41579-021-00583-y) | anaerobes generate ROS by electron transfer “from reduced flavins and metal centers to O₂” | **Strong mechanistic review edge.** Do not equate all O₂ toxicity with ROS. (lu2021whenanaerobesencounter pages 9-11) |
| **FdpA — reduces O₂ and supports tolerance at — approximately 0.4–1% O₂** | Caulat et al., 2024, DOI [10.1128/mbio.01591-24](https://doi.org/10.1128/mbio.01591-24), published 27 Aug 2024 | “FdpA [acts at] low and intermediate O₂ tensions (0.4%–1%)” | **Strong, C. difficile-specific.** Purified-enzyme activity plus mutant phenotype; not universal. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) |
| **revRbr2 — reduces O₂ and supports tolerance at — <0.4% O₂** | Caulat et al., 2024, same DOI | “revRbr2 is specific to low O₂ tensions (<0.4%)” | **Strong, C. difficile-specific.** Context depends on growth mode and σA/σB regulation. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 13-15) |
| **revRbr1 — supports tolerance across — 0.1–4% O₂** | Caulat et al., 2024, same DOI | “revRbr1 has a wider spectrum of activity (0.1%–4%)” | **Strong, C. difficile-specific.** At 4% O₂, the revRbr1 mutant had a larger survival loss than wild type. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) |
| **FdpF — reduces O₂ and supports tolerance to — >4% O₂ and air** | Caulat et al., 2024, same DOI | “FdpF is more specific to tensions >4% and air”; “FdpF is the main O₂-reductase in air” | **Strong, C. difficile-specific.** The fdpF mutant showed reduced survival and O₂-reductase activity. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) |
| **σB — activates expression of — C. difficile O₂-reductase genes** | Caulat et al., 2024, same DOI | “All genes encoding O₂-reductases…are controlled by…σB” | **Strong regulatory edge**, with promoter-specific exceptions: fdpA and revrbr2 also have σA control. (caulat2024physiologicalroleand pages 13-15) |
| **OseR — represses in anaerobiosis / permits O₂ induction of — fdp and revrbr genes** | Caulat et al., 2024, same DOI | “OseR seems to act as a repressor…in anaerobiosis, while this repression is released…at 1% O₂” | **Moderate; curate as taxon-specific and model-supported.** Whether OseR directly senses O₂, ROS, or redox state remains unresolved. (caulat2024physiologicalroleand pages 13-15) |
| **Rex — represses — fdpF expression** | Caulat et al., 2024, same DOI | “fdpF expression is repressed by Rex, a redox regulator that senses the NADH/NAD+ ratio” | **Strong direct regulatory edge.** The proposed role of FdpF in NAD⁺ regeneration is plausible but should remain uncertain. (caulat2024physiologicalroleand pages 13-15) |
| **SOD plus catalase activity — increases/associates with — anammox O₂ tolerance** | Okabe et al., 2023, DOI [10.1038/s43705-023-00251-7](https://doi.org/10.1038/s43705-023-00251-7), accepted 19 Apr 2023 | “This Sod-Cat dependent detoxification system could be responsible for the higher O₂ tolerance of Scalindua” | **Moderate causal interpretation.** Comparative association, not a knockout demonstration. (okabe2023oxygentoleranceand pages 1-2) |
| **marine ‘Ca. Scalindua’ — exhibits — IC₅₀ 18.0 µM O₂ and DOmax 51.6 µM** | Okabe et al., 2023, same DOI | “IC50 = 18.0 µM and DOmax = 51.6 µM” | **Strong quantitative phenotype.** Assay used highly enriched planktonic cells; do not generalize to all anammox bacteria. (okabe2023oxygentoleranceand pages 1-2) |
| **freshwater anammox taxa — exhibit — IC₅₀ 2.7–4.2 µM and DOmax 10.9–26.6 µM** | Okabe et al., 2023, same DOI | “freshwater species (IC50 = 2.7–4.2 µM and DOmax = 10.9–26.6 µM)” | **Strong quantitative comparison.** Demonstrates that “anaerobic” is not a single O₂-tolerance threshold. (okabe2023oxygentoleranceand pages 1-2) |
| **Sat → AprAB → DsrAB/DsrC module — carries out — dissimilatory sulfate reduction** | Dyksma & Pester, 2024, DOI [10.1186/s40168-024-01909-7](https://doi.org/10.1186/s40168-024-01909-7) | pathway “encompasses…Sat…AprAB…DsrAB…and…DsrC” | **Strong pathway-membership edges.** Applicable to sulfate reducers, not anaerobes generally. (dyksma2024growthofsulfatereducing pages 1-2) |
| **periodic 133 µM O₂ exposure — induces/selects oxygen-defense programs while permitting — SRB population growth** | Dyksma & Pester, 2024, same DOI | populations grew “despite weekly periods of oxygen exposures at 133 µM”; most transcribed genes for oxygen consumption, ROS detoxification, and repair | **Strong ecological/bioreactor evidence, but not growth on O₂.** The reactor alternated one oxic week with four anoxic weeks for >200 days. (dyksma2024growthofsulfatereducing pages 1-2) |
| **respiratory reductases — use — dietary/host metabolites as anaerobic electron acceptors** | Little et al., 2024, DOI [10.1038/s41564-023-01560-2](https://doi.org/10.1038/s41564-023-01560-2) | “discover 22 metabolites used as respiratory electron acceptors” | **Strong, species-specific substrate edges.** The tested taxa were S. wadsworthensis, E. lenta, and H. filiformis. (little2024dietaryandhostderived pages 9-11, little2024dietaryandhostderived pages 1-3) |
| **limited O₂ plus poised anode — increases — acetoin yield in B. subtilis** | Sun et al., 2023, DOI [10.1186/s13068-022-02253-4](https://doi.org/10.1186/s13068-022-02253-4) | yield was “0.78 ± 0.04 molproduct/molglucose,” versus “0.39 ± 0.08” without poised potential | **Strong application edge but not a core anaerobic-trait mechanism.** Nitrate or anode alone under strict anoxia caused immediate lysis and limited glucose use. (sun2023anodeassistedelectrofermentationwith pages 1-2) |

A compact cross-check of the principal edges is provided below.

| subject | predicate | object | scope/taxon | evidence strength | DOI |
|---|---|---|---|---|---|
| absence of molecular oxygen | enables | anaerobic metabolism | general anaerobes; trait scope | strong (review definition) (keating2024microbialsinglecellapplications pages 1-2, little2024dietaryandhostderived pages 1-3) | 10.1128/aem.01321-24; 10.1038/s41564-023-01560-2 |
| anaerobic respiration | requires terminal electron acceptor other than oxygen | alternative electron acceptors | general microbes | strong (review/research) (keating2024microbialsinglecellapplications pages 1-2, sun2023anodeassistedelectrofermentationwith pages 1-2) | 10.1128/aem.01321-24; 10.1186/s13068-022-02253-4 |
| fermentation | is distinct from | respiration via electron transport chain | general gut bacteria / general microbes | strong (conceptual distinction) (little2024dietaryandhostderived pages 1-3, sun2023anodeassistedelectrofermentationwith pages 1-2) | 10.1038/s41564-023-01560-2; 10.1186/s13068-022-02253-4 |
| molecular oxygen | inhibits | growth of obligate anaerobes | general obligate anaerobes | strong (review) (botin2023thetoleranceof pages 1-2, lu2021whenanaerobesencounter pages 9-11) | 10.1128/aem.00606-23; 10.1038/s41579-021-00583-y |
| molecular oxygen | damages | pyruvate:formate lyase (PFL) | Bacteroides thetaiotaomicron / obligate anaerobes | strong (direct mechanistic) (khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 8-9) | 10.1111/mmi.14516; 10.1038/s41579-021-00583-y |
| molecular oxygen | damages | pyruvate:ferredoxin oxidoreductase (PFOR) | Bacteroides thetaiotaomicron / obligate anaerobes | strong (direct mechanistic) (khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 8-9) | 10.1111/mmi.14516; 10.1038/s41579-021-00583-y |
| superoxide / hydrogen peroxide | inactivate | Fe-S cluster enzymes | broad bacteria; relevant to anaerobes | strong (foundational mechanism) (imlay2013themolecularmechanisms pages 6-8, lu2021whenanaerobesencounter pages 9-11) | 10.1038/nrmicro3032; 10.1038/s41579-021-00583-y |
| O2-reducing enzymes | support tolerance to low oxygen tensions | anaerobic survival under O2 exposure | Clostridioides difficile | strong (experimental) (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24 |
| revRbr2 | reduces | O2 | Clostridioides difficile; <0.4% O2 range | strong (purified enzyme + phenotype range) (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24 |
| FdpA | reduces | O2 | Clostridioides difficile; 0.4%–1% O2 range | strong (purified enzyme + phenotype range) (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) | 10.1128/mbio.01591-24 |
| revRbr1 | reduces | O2 | Clostridioides difficile; 0.1%–4% O2 range | strong (purified enzyme + phenotype range) (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) | 10.1128/mbio.01591-24 |
| FdpF | reduces | O2 | Clostridioides difficile; >4% O2 and air | strong (purified enzyme + phenotype range) (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 5-7) | 10.1128/mbio.01591-24 |
| revRbr1 | supports tolerance to | 1% O2 | Clostridioides difficile | strong (mutant phenotype) (caulat2024physiologicalroleand pages 5-7) | 10.1128/mbio.01591-24 |
| revRbr1 | supports tolerance to | 4% O2 | Clostridioides difficile | strong (mutant phenotype) (caulat2024physiologicalroleand pages 5-7) | 10.1128/mbio.01591-24 |
| FdpF | supports tolerance to | 4% O2 and air | Clostridioides difficile | strong (mutant phenotype) (caulat2024physiologicalroleand pages 5-7) | 10.1128/mbio.01591-24 |
| sigma B | activates expression of | fdpF / revrbr1 / revrbr2 (and contributes to fdpA control) | Clostridioides difficile | strong (regulatory genetics) (caulat2024physiologicalroleand pages 13-15) | 10.1128/mbio.01591-24 |
| sigma A | activates expression of | revrbr2 and fdpA | Clostridioides difficile | moderate-strong (promoter evidence) (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 13-15) | 10.1128/mbio.01591-24 |
| OseR (Spx-family regulator) | represses in anaerobiosis / contributes to induction upon O2 exposure of | fdp and revrbr genes | Clostridioides difficile | moderate-strong (regulatory model) (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 13-15) | 10.1128/mbio.01591-24 |
| Rex | represses expression of | fdpF | Clostridioides difficile | strong (regulatory genetics) (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 13-15) | 10.1128/mbio.01591-24 |
| high superoxide dismutase activity plus catalase activity | is associated with | higher oxygen tolerance | marine anammox “Ca. Scalindua sp.” | strong (quantitative comparative evidence) (okabe2023oxygentoleranceand pages 1-2) | 10.1038/s43705-023-00251-7 |
| “Ca. Scalindua sp.” | has oxygen tolerance metrics | IC50 18.0 µM; DOmax 51.6 µM | marine anammox | strong (quantitative) (okabe2023oxygentoleranceand pages 1-2) | 10.1038/s43705-023-00251-7 |
| freshwater anammox species | have oxygen tolerance metrics | IC50 2.7–4.2 µM; DOmax 10.9–26.6 µM | Brocadia/Jettenia/Kuenenia spp. | strong (quantitative) (okabe2023oxygentoleranceand pages 1-2) | 10.1038/s43705-023-00251-7 |
| sulfate adenylyltransferase (Sat) | participates in | dissimilatory sulfate reduction | sulfate-reducing bacteria | strong (pathway definition) (dyksma2024growthofsulfatereducing pages 1-2) | 10.1186/s40168-024-01909-7 |
| adenylyl phosphosulfate reductase (AprAB) | participates in | dissimilatory sulfate reduction | sulfate-reducing bacteria | strong (pathway definition) (dyksma2024growthofsulfatereducing pages 1-2) | 10.1186/s40168-024-01909-7 |
| dissimilatory sulfite reductase (DsrAB) | participates in | dissimilatory sulfate reduction | sulfate-reducing bacteria | strong (pathway definition) (dyksma2024growthofsulfatereducing pages 1-2) | 10.1186/s40168-024-01909-7 |
| DsrC | participates in | sulfide-releasing step of sulfate reduction | sulfate-reducing bacteria | strong (pathway definition) (dyksma2024growthofsulfatereducing pages 1-2) | 10.1186/s40168-024-01909-7 |
| periodic oxygen stress (133 µM; 50% air saturation) | selects for populations maintaining | oxygen defense gene expression | sulfate-reducing Desulfobacterota and Bacillota | strong (bioreactor transcriptomics) (dyksma2024growthofsulfatereducing pages 1-2) | 10.1186/s40168-024-01909-7 |
| gut bacterial respiratory reductases | reduce | dietary- and host-derived metabolites as anaerobic electron acceptors | Sutterella wadsworthensis, Eggerthella lenta, Holdemania filiformis | strong (2024 discovery) (little2024dietaryandhostderived pages 9-11, little2024dietaryandhostderived pages 1-3) | 10.1038/s41564-023-01560-2 |
| nitrate / fumarate / sulfate / Fe(III) / Mn(IV) / CO2 | can serve as terminal electron acceptors in | anaerobic respiration | general microbes | moderate-strong (general physiology) (sun2023anodeassistedelectrofermentationwith pages 1-2) | 10.1186/s13068-022-02253-4 |


*Table: This table compiles the strongest candidate subject-predicate-object edges for curating the microbial anaerobic trait, emphasizing direct mechanistic support, quantitative oxygen ranges, and clearly taxon-scoped claims. It is useful as a compact starting point for TraitMech edge selection and uncertainty triage.*

## 4. Current understanding and expert analysis

### Oxygen exclusion is necessary context, not a complete mechanism

Anaerobic growth requires a route to dispose of electrons and conserve energy when O₂ cannot serve as terminal acceptor. The route may be respiration, fermentation, syntrophy, methanogenesis, acetogenesis, or combinations thereof. Consequently, a universal graph should stop at abstract nodes such as **alternative electron disposal**, **redox-carrier regeneration**, and **energy conservation**, while nitrate, sulfate, fumarate, and specific fermentation pathways should be taxon-scoped child branches. (little2024dietaryandhostderived pages 1-3, sun2023anodeassistedelectrofermentationwith pages 1-2)

### Obligate anaerobiosis reflects vulnerable metabolic design

Authoritative mechanistic work distinguishes two injury routes. Molecular O₂ directly attacks radical enzymes and some low-potential metal centers; independently, adventitious electron transfer to O₂ forms superoxide and H₂O₂, which damage iron–sulfur and mononuclear iron enzymes. In *B. thetaiotaomicron*, PFL and PFOR support pyruvate dissimilation but lose activity during aeration; PFOR injury persisted regardless of superoxide or peroxide abundance, demonstrating direct O₂ toxicity. Thus, “ROS causes anaerobiosis” is too broad for curation. (khademian2020doreactiveoxygen pages 1-2, lu2021whenanaerobesencounter pages 8-9)

### Oxygen defense modifies phenotype severity

Recent work shows layered, range-specific defenses. *C. difficile* deploys four overlapping O₂ reductases under σB, σA, OseR, and Rex control. Different enzymes dominate at <0.4%, 0.4–1%, 0.1–4%, or >4%/air, providing unusually precise causal edges between protein function and exposure regime. Nevertheless, these systems support transient survival and niche adaptation; they do not convert *C. difficile* into an aerobic organism. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 13-15, caulat2024physiologicalroleand pages 5-7)

Likewise, 2024 peat-biome experiments showed that nominally strict sulfate reducers maintained populations through repeated 133 µM O₂ episodes, partly through constitutive or inducible oxygen consumption, ROS detoxification, and repair. This challenges binary oxygen-tolerance labels but does not alter their anaerobic energy metabolism. (dyksma2024growthofsulfatereducing pages 1-2)

## 5. Recent developments and real-world applications, 2023–2024

1. **Gut anaerobe physiology and infection.** The 2024 *C. difficile* study mapped O₂-reductase activity onto physiologically relevant gut gradients: approximately 4–5% O₂ in the small intestine, 0.1–0.4% in the colonic lumen, 1–2% near mucus, and about 5% near tissue. This supplies exposure-specific mechanisms relevant to colonization and infection. (caulat2024physiologicalroleand pages 1-2)

2. **Next-generation probiotics.** Oxygen sensitivity limits cultivation and deployment of health-associated *Faecalibacterium*. A 2023 study found substantial strain-to-strain differences and identified flavodiiron proteins, rubrerythrins, reverse rubrerythrins, superoxide reductases, and alkyl peroxidase as candidate defenses; O₂/H₂O₂ induced different detoxification programs in *F. longum* L2-6. These findings support strain-specific manufacturing and formulation rather than genus-wide oxygen-tolerance assumptions. (botin2023thetoleranceof pages 1-2)

3. **Anammox wastewater and marine nitrogen-cycle models.** The marked difference between marine *Scalindua* and freshwater anammox oxygen thresholds affects reactor control and estimates of nitrogen loss in oxygen-minimum zones. Oxygen-minimum zones defined at ≤5 µM occupy about **0.1% of ocean volume** but account for an estimated **20–40% of oceanic nitrogen loss**; oxygen-tolerance assumptions therefore have disproportionate biogeochemical consequences. (okabe2023oxygentoleranceand pages 1-2)

4. **Expanded gut anaerobic respiration.** The discovery of 22 dietary/host electron acceptors, together with respiratory-reductase inventories spanning more than 1,533 gut prokaryotic species, shows that anaerobic respiration extends far beyond canonical nitrate or fumarate reduction and directly transforms bioactive compounds such as itaconate and resveratrol. (little2024dietaryandhostderived pages 9-11, little2024dietaryandhostderived pages 1-3)

5. **Anoxic single-cell platforms.** A 2024 review identifies oxygen-compatible microfluidics, viable-cell sorting, live imaging, oxygen-independent fluorescent probes, and downstream single-cell omics as priorities. Current anaerobic culture still relies heavily on Hungate/Balch methods and expensive chambers, while batch culture obscures cell-level heterogeneity and causal interactions. (keating2024microbialsinglecellapplications pages 1-2)

6. **Electro-fermentation.** Under limited aeration, a 0.7-V versus standard hydrogen electrode anode doubled *B. subtilis* acetoin yield from 0.39 ± 0.08 to 0.78 ± 0.04 mol/mol glucose. However, anode or nitrate alone did not sustain healthy strictly anaerobic growth, illustrating why oxygen limitation cannot automatically be coded as anaerobiosis. (sun2023anodeassistedelectrofermentationwith pages 1-2)

## 6. Recommended minimal TraitMech graph

A compact, broadly valid graph should contain approximately the following backbone:

1. `absence of measurable O2` **enables** `anaerobic metabolic routing`.
2. `anaerobic metabolic routing` **includes** `fermentation` and/or `anaerobic respiration`.
3. `fermentation` **regenerates** `oxidized redox carriers`.
4. `alternative terminal electron acceptor` **enables** `anaerobic respiration`.
5. `anaerobic respiration` **generates** `ion motive force/ATP`.
6. `redox-carrier regeneration and ATP production` **support** `growth without O2`.
7. `molecular O2` **inhibits** `oxygen-sensitive anaerobic enzymes`.
8. `O2 exposure` **generates** `superoxide/H2O2` through adventitious electron transfer.
9. `superoxide/H2O2` **damage** `Fe–S and iron-dependent enzymes`.
10. `O2-reduction, ROS detoxification, and repair systems` **increase** `oxygen tolerance`, thereby modifying—but not defining—the anaerobic phenotype.

Taxon-specific subgraphs should then attach nitrate, fumarate, sulfate, anammox, methanogenesis, Stickland fermentation, or the *C. difficile* Fdp/revRbr network. This is preferable to making one pathway appear necessary for every anaerobe.

## 7. Warnings: claims not ready for unqualified curation

- **Do not curate “anaerobes cannot survive oxygen.”** The trait concerns growth; many strict anaerobes survive substantial or reversible O₂ exposure. *C. difficile*, anammox bacteria, and sulfate reducers provide direct counterexamples. (okabe2023oxygentoleranceand pages 1-2, dyksma2024growthofsulfatereducing pages 1-2, caulat2024physiologicalroleand pages 5-7)
- **Do not curate absence of catalase or SOD as the cause of obligate anaerobiosis.** Some anaerobes possess these enzymes, and direct O₂ injury to PFL/PFOR or low-potential centers can remain decisive. (okabe2023oxygentoleranceand pages 1-2, khademian2020doreactiveoxygen pages 1-2)
- **Do not universalize the C. difficile Fdp/revRbr/OseR/Rex network.** It is a strong exemplar but taxon-specific; even closely related anaerobes differ in enzyme complements and regulation.
- **Treat OseR direct sensing as uncertain.** The source explicitly leaves open whether it senses O₂, ROS, or redox state. (caulat2024physiologicalroleand pages 13-15)
- **Treat SOD–catalase causality in marine anammox as uncertain/moderate.** Enzyme activity correlates with higher tolerance, but genetic necessity and sufficiency were not demonstrated. (okabe2023oxygentoleranceand pages 1-2)
- **Do not infer phenotype from gene presence alone.** Respiratory reductases are often uncharacterized, and substrate specificity is species-specific. (little2024dietaryandhostderived pages 9-11, little2024dietaryandhostderived pages 1-3)
- **Do not equate substrate turnover, transcription, or ATP increase with growth.** Require biomass increase or serial propagation when curating METPO:1000603.
- **Do not mix percentages, headspace O₂, and dissolved O₂ without metadata.** Temperature, pressure, medium, geometry, and biomass aggregation affect conversion and biological exposure.
- **Do not assign exact ontology CURIEs from memory where protonation state, strain, complex, or pathway version is ambiguous.** Label-only nodes are safer until validated against the target ontology release.
- **Do not use the electro-fermentation result as evidence that B. subtilis grows strictly anaerobically on an anode.** The study observed immediate lysis when anode or nitrate was the sole acceptor under anoxia. (sun2023anodeassistedelectrofermentationwith pages 1-2)

## DOI-first bibliography

1. Caulat LC et al. **Physiological role and complex regulation of O₂-reducing enzymes in the obligate anaerobe *Clostridioides difficile*.** *mBio* 15, 2024. Published 27 August 2024. DOI: [10.1128/mbio.01591-24](https://doi.org/10.1128/mbio.01591-24). (caulat2024physiologicalroleand pages 1-2)
2. Dyksma S, Pester M. **Growth of sulfate-reducing Desulfobacterota and Bacillota at periodic oxygen stress of 50% air-O₂ saturation.** *Microbiome* 12:191, 2024. DOI: [10.1186/s40168-024-01909-7](https://doi.org/10.1186/s40168-024-01909-7). (dyksma2024growthofsulfatereducing pages 1-2)
3. Little AS et al. **Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration.** *Nature Microbiology* 9:55–69, 2024. DOI: [10.1038/s41564-023-01560-2](https://doi.org/10.1038/s41564-023-01560-2). (little2024dietaryandhostderived pages 1-3)
4. Keating C et al. **Microbial single-cell applications under anoxic conditions.** *Applied and Environmental Microbiology* 90, 2024. Published 30 September 2024. DOI: [10.1128/aem.01321-24](https://doi.org/10.1128/aem.01321-24). (keating2024microbialsinglecellapplications pages 1-2)
5. Okabe S et al. **Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing bacteria.** *ISME Communications* 3, 2023. Received 26 January; accepted 19 April 2023. DOI: [10.1038/s43705-023-00251-7](https://doi.org/10.1038/s43705-023-00251-7). (okabe2023oxygentoleranceand pages 1-2)
6. Botin T et al. **The tolerance of gut commensal *Faecalibacterium* to oxidative stress is strain dependent and relies on detoxifying enzymes.** *Applied and Environmental Microbiology* 89, July 2023. DOI: [10.1128/aem.00606-23](https://doi.org/10.1128/aem.00606-23). (botin2023thetoleranceof pages 1-2)
7. Sun Y, Kokko M, Vassilev I. **Anode-assisted electro-fermentation with *Bacillus subtilis* under oxygen-limited conditions.** *Biotechnology for Biofuels and Bioproducts* 16:6, 2023. DOI: [10.1186/s13068-022-02253-4](https://doi.org/10.1186/s13068-022-02253-4). (sun2023anodeassistedelectrofermentationwith pages 1-2)
8. Lu Z, Imlay JA. **When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence.** *Nature Reviews Microbiology* 19:774–785, 2021. DOI: [10.1038/s41579-021-00583-y](https://doi.org/10.1038/s41579-021-00583-y). (lu2021whenanaerobesencounter pages 9-11)
9. Khademian M, Imlay JA. **Do reactive oxygen species or does oxygen itself confer obligate anaerobiosis? The case of *Bacteroides thetaiotaomicron*.** *Molecular Microbiology* 114:333–347, 2020. DOI: [10.1111/mmi.14516](https://doi.org/10.1111/mmi.14516). (khademian2020doreactiveoxygen pages 1-2)
10. Imlay JA. **The molecular mechanisms and physiological consequences of oxidative stress: lessons from a model bacterium.** *Nature Reviews Microbiology* 11:443–454, 2013. DOI: [10.1038/nrmicro3032](https://doi.org/10.1038/nrmicro3032). (imlay2013themolecularmechanisms pages 6-8)

References

1. (little2024dietaryandhostderived pages 1-3): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.

2. (sun2023anodeassistedelectrofermentationwith pages 1-2): Yu Sun, Marika Kokko, and Igor Vassilev. Anode-assisted electro-fermentation with bacillus subtilis under oxygen-limited conditions. Biotechnology for Biofuels and Bioproducts, Jan 2023. URL: https://doi.org/10.1186/s13068-022-02253-4, doi:10.1186/s13068-022-02253-4. This article has 29 citations and is from a domain leading peer-reviewed journal.

3. (khademian2020doreactiveoxygen pages 1-2): Maryam Khademian and James A. Imlay. Do reactive oxygen species or does oxygen itself confer obligate anaerobiosis? the case of <i>bacteroides thetaiotaomicron</i>. Molecular Microbiology, 114:333-347, May 2020. URL: https://doi.org/10.1111/mmi.14516, doi:10.1111/mmi.14516. This article has 42 citations and is from a domain leading peer-reviewed journal.

4. (lu2021whenanaerobesencounter pages 9-11): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

5. (keating2024microbialsinglecellapplications pages 1-2): Ciara Keating, Kerstin Fiege, Martijn Diender, Diana Z. Sousa, and Laura Villanueva. Microbial single-cell applications under anoxic conditions. Nov 2024. URL: https://doi.org/10.1128/aem.01321-24, doi:10.1128/aem.01321-24. This article has 5 citations and is from a peer-reviewed journal.

6. (okabe2023oxygentoleranceand pages 1-2): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 71 citations and is from a peer-reviewed journal.

7. (khademian2021howmicrobesevolved pages 1-3): Maryam Khademian and James A. Imlay. How microbes evolved to tolerate oxygen. May 2021. URL: https://doi.org/10.1016/j.tim.2020.10.001, doi:10.1016/j.tim.2020.10.001. This article has 125 citations and is from a domain leading peer-reviewed journal.

8. (botin2023thetoleranceof pages 1-2): Tatiana Botin, Luis Ramirez-Chamorro, Jasmina Vidic, Philippe Langella, Isabelle Martin-Verstraete, Jean-Marc Chatel, and Sandrine Auger. The tolerance of gut commensal <i>faecalibacterium</i> to oxidative stress is strain dependent and relies on detoxifying enzymes. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00606-23, doi:10.1128/aem.00606-23. This article has 20 citations and is from a peer-reviewed journal.

9. (dyksma2024growthofsulfatereducing pages 1-2): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 56 citations and is from a highest quality peer-reviewed journal.

10. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (caulat2024physiologicalroleand pages 13-15): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

12. (little2024dietaryandhostderived pages 9-11): Alexander S. Little, Isaac T. Younker, Matthew S. Schechter, Paola Nol Bernardino, Raphaël Méheust, Joshua Stemczynski, Kaylie Scorza, Michael W. Mullowney, Deepti Sharan, Emily Waligurski, Rita Smith, Ramanujam Ramanswamy, William Leiter, David Moran, Mary McMillin, Matthew A. Odenwald, Anthony T. Iavarone, Ashley M. Sidebottom, Anitha Sundararajan, Eric G. Pamer, Murat A. Eren, and Samuel H. Light. Dietary- and host-derived metabolites are used by diverse gut bacteria for anaerobic respiration. Nature microbiology, 9:55-69, Nov 2024. URL: https://doi.org/10.1038/s41564-023-01560-2, doi:10.1038/s41564-023-01560-2. This article has 81 citations and is from a highest quality peer-reviewed journal.

13. (imlay2013themolecularmechanisms pages 6-8): James A. Imlay. The molecular mechanisms and physiological consequences of oxidative stress: lessons from a model bacterium. Nature Reviews Microbiology, 11:443-454, May 2013. URL: https://doi.org/10.1038/nrmicro3032, doi:10.1038/nrmicro3032. This article has 2007 citations and is from a highest quality peer-reviewed journal.

14. (lu2021whenanaerobesencounter pages 8-9): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

15. (caulat2024physiologicalroleand pages 5-7): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.