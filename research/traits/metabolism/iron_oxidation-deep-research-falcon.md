---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:17:10.239056'
end_time: '2026-08-04T06:27:12.608854'
duration_seconds: 602.37
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: iron oxidation
  trait_identifier: traitmech:000107
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: iron_oxidation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which an organism oxidizes ferrous iron (Fe2+) to ferric
    iron (Fe3+) to conserve energy, at acidic or circumneutral pH and under aerobic
    or anaerobic conditions.
  parent_traits: METPO:1000060
  synonyms: ferrous iron oxidation
  evidence_summary: 'DOI:10.1146/annurev.micro.112408.134208:  (Emerson, Fleming &
    McBeth review iron-oxidizing bacteria from an environmental and genomic perspective.)
    | DOI:10.1099/mic.0.045344-0:  (Hedrich, Schlomann & Johnson review the iron-oxidizing
    proteobacteria and their energy metabolism.)'
  causal_graph_summary: 'iron_oxidation_ferrous_to_ferric: 12 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** iron oxidation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000107
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes ferrous iron (Fe2+) to ferric iron (Fe3+) to conserve energy, at acidic or circumneutral pH and under aerobic or anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** ferrous iron oxidation
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134208:  (Emerson, Fleming & McBeth review iron-oxidizing bacteria from an environmental and genomic perspective.) | DOI:10.1099/mic.0.045344-0:  (Hedrich, Schlomann & Johnson review the iron-oxidizing proteobacteria and their energy metabolism.)
- **Existing causal graph summary:** iron_oxidation_ferrous_to_ferric: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **iron oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/iron_oxidation.yaml`.

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
- **Trait label:** iron oxidation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000107
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes ferrous iron (Fe2+) to ferric iron (Fe3+) to conserve energy, at acidic or circumneutral pH and under aerobic or anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** ferrous iron oxidation
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134208:  (Emerson, Fleming & McBeth review iron-oxidizing bacteria from an environmental and genomic perspective.) | DOI:10.1099/mic.0.045344-0:  (Hedrich, Schlomann & Johnson review the iron-oxidizing proteobacteria and their energy metabolism.)
- **Existing causal graph summary:** iron_oxidation_ferrous_to_ferric: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **iron oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/iron_oxidation.yaml`.

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


# TraitMech curation report: microbial iron oxidation

## Record and scope

- **Trait:** iron oxidation
- **Trait identifier:** **`traitmech:000107`**
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1000060`
- **Preferred mechanistic definition:** energy-conserving, dissimilatory oxidation of ferrous iron, Fe(II), to ferric iron, Fe(III), by a microorganism. Electrons enter an extracellular/periplasmic respiratory chain and ultimately support generation of proton motive force, ATP, and—where autotrophy occurs—reducing power for carbon fixation. Current comparative work recognizes multiple, non-universal molecular pathways rather than one conserved “iron oxidase.” (li2023sequencesimilaritynetwork pages 1-2, li2023sequencesimilaritynetwork pages 2-4)

The trait includes aerobic acidophilic oxidation, microaerobic circumneutral oxidation, anoxygenic phototrophic Fe(II) oxidation (“photoferrotrophy”), and experimentally demonstrated anaerobic oxidation coupled to acceptors such as nitrate. Its defining phenotype is biological Fe(II) disappearance with corresponding Fe(III) formation linked to energy conservation or growth—not merely possession of a candidate gene.

### Boundaries and nearby traits

**Include:**

1. Fe(II) used as an electron donor and converted to Fe(III).
2. Soluble and mineral-bound Fe(II), provided biological oxidation is demonstrated.
3. Chemolithoautotrophic, mixotrophic, or phototrophic organisms when Fe(II) oxidation contributes electrons to metabolism.
4. Acidic and circumneutral systems, including aerobic, microaerobic, phototrophic-anoxic, and nitrate-associated conditions.

**Exclude or model separately:**

- Assimilatory iron uptake, iron storage, siderophore production, and iron homeostasis.
- Fe(III) reduction. For example, *Acidithiobacillus ferrooxidans* can oxidize Fe(II) aerobically but can also reduce Fe(III) anaerobically with reduced sulfur compounds; these are opposite traits and must not share a causal edge merely because the same organism performs both. (wang2024characterizethegrowth pages 1-2)
- Abiotic Fe(II) oxidation by O₂, reactive oxygen species, nitrite, or mineral surfaces unless a biological contribution is experimentally separated.
- Electrode-dependent extracellular electron uptake. A 2024 study showed that electroautotrophy and Fe(II)-based chemoautotrophy in *A. ferrooxidans* have different expression and mineral-deposition phenotypes; electrode uptake is therefore an adjacent, not equivalent, trait. (wang2024characterizethegrowth pages 1-2)
- Sulfur oxidation, nitrite oxidation, Mn(II) oxidation, and organotrophy, even when co-occurring in an Fe oxidizer. *Candidatus Nitrotoga*, for example, belongs to Gallionellaceae but lacks established iron-oxidation physiology and canonical Fe-oxidation markers. (hoover2023gallionellaceaepangenomicanalysis pages 15-17, hoover2023gallionellaceaepangenomicanalysis pages 4-8)
- A `cyc2` hit alone. Cluster 1 Cyc2 has strong functional support, whereas a divergent Cluster 2 homolog in *Ca. Nitrotoga* lacked sufficient physiological and genomic context for assignment as an iron oxidase. (hoover2023gallionellaceaepangenomicanalysis pages 4-8)

## Candidate graph nodes

### Chemicals, donors, acceptors, and products

| Candidate node | Suggested grounding | Curation role |
|---|---|---|
| ferrous ion / Fe(II) | `CHEBI:29033` | Electron donor and oxidized substrate. Verify identifier during ontology build. |
| ferric ion / Fe(III) | `CHEBI:29034` | Primary oxidation product. Verify identifier during ontology build. |
| dioxygen | `CHEBI:15379` | Terminal acceptor in aerobic pathways. |
| water | `CHEBI:15377` | Product of terminal O₂ reduction. |
| proton | `CHEBI:15378` | Coupled to proton motive force and O₂-to-water chemistry. |
| NADH / NAD⁺ | CHEBI grounding recommended after release validation | Reducing-power pair in reverse electron transport. |
| ATP / ADP | CHEBI grounding recommended after release validation | Energy-conservation output. |
| carbon dioxide | `CHEBI:16526` | Carbon source in chemolithoautotrophs. |
| nitrate / nitrite / nitric oxide | CHEBI grounding recommended | Potential anaerobic acceptor chain; not universal and often consortium-dependent. |
| Fe(II)-smectite | Label-only candidate | Mineral-bound Fe(II) substrate associated with MtoA. |
| ferric oxyhydroxide / jarosite | Mineral-specific label candidates | Extracellular products; mineral identity depends strongly on pH and medium chemistry. |

### Environmental and experimental factors

- acidic environment; acid mine drainage; metal-sulfide ore
- circumneutral redox transition zone
- oxic condition; microoxic condition; anoxic condition
- light availability for photoferrotrophy
- nitrate availability for nitrate-associated Fe(II) oxidation
- aqueous versus mineral-bound Fe(II)
- pH, oxygen concentration, sulfate, and other redox-active metals
- electrode as sole electron source—**experimental comparator, not an iron-oxidation substrate**

The activity of c-type cytochrome systems is reported to vary with oxygen concentration, pH, and other redox-active metals. At neutral pH, rapid Fe(III) precipitation creates both kinetic and cellular-encrustation constraints; extracellular oxidation helps keep precipitating Fe(III) out of the cytoplasm. (li2023sequencesimilaritynetwork pages 16-17, li2023sequencesimilaritynetwork pages 2-4)

### Pathways and modules

1. **Acidithiobacillus Cyc2–Rus pathway:** Fe(II) → Cyc2 → rusticyanin, followed by a downhill O₂-reducing branch and an uphill reducing-power branch.
2. **Gallionellaceae Cyc2 pathway:** especially associated with dissolved Fe(II).
3. **MtoAB porin–multiheme-cytochrome pathway:** associated particularly with extracellular or mineral-bound Fe(II).
4. **PioABC photoferrotrophic pathway:** *Rhodopseudomonas* lineage; PioA is a decaheme cytochrome, PioB an outer-membrane protein, and PioC a high-potential Fe–S protein.
5. **Leptospirillum Cyc572 pathway:** Cyc572, Cyc579, cytochrome bc₁, and cbb₃-type terminal oxidase.
6. **Other taxon-specific modules:** FoxEYZ in *Rhodobacter*, Cyc2-PV1/Mob in *Mariprofundus*, Fox proteins and multicopper oxidase in *Metallosphaera*, and sulfocyanin/caa₃ oxidase in *Ferroplasma*. These are useful extension nodes but should not be put into a universal core graph without organism-specific evidence. The 2023 canonical-pathway table supports the taxon/protein assignments. (li2023sequencesimilaritynetwork pages 2-4, li2023sequencesimilaritynetwork media 0f1522cd)

### Genes, proteins, and complexes

- `cyc2` / Cyc2, outer-membrane fused porin–monoheme cytochrome
- `rus` / rusticyanin, periplasmic blue-copper electron carrier
- `cyc1` / Cyc1, cytochrome c₄
- `coxBACD`, aa₃-type cytochrome oxidase complex
- `petABC`, cytochrome bc₁ complex; quinone pool; NADH dehydrogenase complex I
- `mtoA`, decaheme c-type cytochrome; `mtoB`, outer-membrane porin; MtoD and CymA
- `pioA`, decaheme c-type cytochrome; `pioB`, outer-membrane protein; `pioC`, high-potential Fe–S protein
- Cyc572, Cyc579, cbb₃-type cytochrome-c oxidase
- RuBisCO and Calvin–Benson–Bassham-cycle module for carbon fixation
- c-type cytochrome maturation machinery, where explicitly demonstrated

Use **label-only nodes or taxon-specific UniProt accessions** for these proteins until the exact strain is known. A generic UniProt CURIE would obscure major paralog, cluster, and functional differences.

### Cellular locations and functions

Suggested GO candidates, requiring release-time verification, include outer membrane, periplasmic space, plasma/cytoplasmic membrane, respiratory electron-transport chain, cytochrome-c activity, oxidoreductase activity, proton transmembrane transport, ATP synthesis coupled to electron transport, and carbon fixation. The mechanistic literature places initial Fe(II) oxidation at the cell exterior, outer membrane, or periplasm, thereby reducing intracellular Fe(III) precipitation and Fenton-type oxidative stress. (li2023sequencesimilaritynetwork pages 1-2, li2023sequencesimilaritynetwork pages 2-4)

## Candidate causal edges

The following compact graph summarizes the principal edge set before detailed evidence notes.

| subject | predicate | object | representative taxon/context | evidence strength/qualifier |
|---|---|---|---|---|
| Fe(II) | donates electrons to | Cyc2 | *Acidithiobacillus ferrooxidans* aerobic acidophilic Fe(II) oxidation | strong; directly stated canonical pathway; taxon-specific to acidophilic pathway (wang2024characterizethegrowth pages 1-2, li2023sequencesimilaritynetwork pages 2-4) |
| Cyc2 | transfers electrons to | rusticyanin (Rus) | *A. ferrooxidans* periplasmic branch point | strong; directly stated canonical pathway; taxon-specific (wang2024characterizethegrowth pages 1-2, li2023sequencesimilaritynetwork pages 2-4) |
| rusticyanin (Rus) | transfers electrons to | Cyc1 | *A. ferrooxidans* downhill branch | strong; directly stated canonical pathway; taxon-specific (li2023sequencesimilaritynetwork pages 2-4) |
| Cyc1 | transfers electrons to | aa3-type cytochrome oxidase complex (CoxBACD) | *A. ferrooxidans* aerobic respiration | strong; directly stated canonical pathway; taxon-specific (li2023sequencesimilaritynetwork pages 2-4) |
| aa3-type cytochrome oxidase complex | reduces | O2 to H2O | *A. ferrooxidans* aerobic respiration | strong; directly stated canonical pathway (li2023sequencesimilaritynetwork pages 2-4) |
| rusticyanin (uphill branch) | supports electron transfer to | NADH-generating pathway via bc1 complex, quinones, and proton motive force | *A. ferrooxidans* reverse electron transport | moderate; mechanistically described in review-style synthesis; taxon-specific and partially inferred as a composite edge (li2023sequencesimilaritynetwork pages 2-4) |
| Fe(II) | is oxidized extracellularly by | MtoAB complex | *Sideroxydans lithotrophicus* / Gallionellaceae, especially mineral-bound Fe(II) | strong for FeOB role; strongest for MtoA/MtoB involvement, especially mineral-bound Fe(II); extracellular localization/function inferred from porin-cytochrome architecture (hoover2023gallionellaceaepangenomicanalysis pages 1-2, hoover2023gallionellaceaepangenomicanalysis pages 15-17, hoover2023gallionellaceaepangenomicanalysis pages 4-8) |
| dissolved Fe(II) | is oxidized by | Cyc2 | Gallionellaceae neutrophilic FeOB | strong; supported by pangenomics plus prior biochemical/transcript/proteomic validation cited in source; lineage-specific (hoover2023gallionellaceaepangenomicanalysis pages 15-17, hoover2023gallionellaceaepangenomicanalysis pages 4-8) |
| Fe(II) | donates electrons to | PioABC pathway | *Rhodopseudomonas* spp. photoferrotrophy | moderate; canonical pathway table support, but trait edge is taxon-specific and relies on prior experimental literature summarized in review (li2023sequencesimilaritynetwork pages 2-4, li2023sequencesimilaritynetwork media 0f1522cd) |
| light | enables | PioABC-mediated Fe(II) oxidation | *Rhodopseudomonas* spp. photoferrotrophy | moderate; pathway is explicitly phototrophic in canonical table, but this compact edge is contextual/inferred from pathway class (li2023sequencesimilaritynetwork pages 2-4, li2023sequencesimilaritynetwork media 0f1522cd) |
| Fe(II) | donates electrons to | Cyc572 | *Leptospirillum* spp. acidophilic Fe(II) oxidation | moderate; canonical pathway support from synthesis table; taxon-specific (li2023sequencesimilaritynetwork pages 2-4, li2023sequencesimilaritynetwork media 0f1522cd) |
| Cyc572 | transfers electrons to | Cyc579 | *Leptospirillum* spp. | moderate; canonical pathway table support; taxon-specific (li2023sequencesimilaritynetwork pages 2-4, li2023sequencesimilaritynetwork media 0f1522cd) |
| Cyc579 | transfers electrons to | cytochrome bc1 complex | *Leptospirillum* spp. | moderate; canonical pathway table support; taxon-specific (li2023sequencesimilaritynetwork pages 2-4, li2023sequencesimilaritynetwork media 0f1522cd) |
| cytochrome bc1 complex | transfers electrons to | cbb3-type cytochrome c oxidase | *Leptospirillum* spp. | moderate; canonical pathway table support; taxon-specific (li2023sequencesimilaritynetwork pages 2-4, li2023sequencesimilaritynetwork media 0f1522cd) |
| microbial Fe(II) oxidation | produces | Fe(III) | broad iron-oxidizer trait scope | strong; definitional across sources (li2023sequencesimilaritynetwork pages 1-2, tonietti2024unveilingthebioleaching pages 1-2) |
| Fe(III) production during Fe(II) oxidation | promotes | mineral precipitation outside the cell | especially neutrophilic environments; jarosite in acidic *A. ferrooxidans* Fe(II)-grown cultures | moderate; precipitation risk/mechanistic rationale strong, but mineral form depends on pH/context; jarosite observation is assay-specific (wang2024characterizethegrowth pages 1-2, li2023sequencesimilaritynetwork pages 2-4) |
| Fe(II) oxidation electron transport | drives | ATP generation | broad dissimilatory Fe(II)-oxidizer metabolism | moderate; strong as general bioenergetic claim from synthesis, but not tied to one universally conserved chain (li2023sequencesimilaritynetwork pages 1-2, wang2024characterizethegrowth pages 1-2) |
| Fe(II) oxidation electron transport | supplies reducing power for | carbon fixation / CO2 fixation | *A. ferrooxidans* and Gallionellaceae FeOB | moderate; supported by autotrophic physiology and carbon-fixation gene/pathway presence; lineage/context-specific (hoover2023gallionellaceaepangenomicanalysis pages 1-2, wang2024characterizethegrowth pages 1-2) |


*Table: This table lists compact, curation-ready candidate causal edges for microbial iron oxidation, emphasizing the strongest mechanistic links and clearly flagging taxon-specific or inferred relationships. It is useful as a starting point for TraitMech edge selection and uncertainty review.*

### Evidence table for proposed triples

| # | Subject–predicate–object | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|
| 1 | **Fe(II) —is oxidized to→ Fe(III)** | Li et al., 2023, DOI 10.1128/msystems.00720-23 | “dissimilatory ferrous iron oxidation” is described as a microbial energy-generation strategy. | **Core edge; strong.** Require phenotype evidence linking conversion to metabolism. (li2023sequencesimilaritynetwork pages 1-2) |
| 2 | **Fe(II) —donates electrons to→ Cyc2** | Wang et al., 2024, DOI 10.3390/microorganisms12030590 | “*A. ferrooxidans* oxidizes Fe2+ to Fe3+ with outer-membrane cytochrome c (Cyc2).” | **Strong but taxon-specific.** Suitable for an *A. ferrooxidans* subgraph. (wang2024characterizethegrowth pages 1-2) |
| 3 | **Cyc2 —transfers electrons to→ rusticyanin** | Li et al., 2023 | “electrons are initially extracted from extracellular Fe(II) by…Cyc2 and then transferred to…rusticyanin.” | **Strong; taxon-specific.** (li2023sequencesimilaritynetwork pages 2-4) |
| 4 | **rusticyanin —transfers electrons through→ Cyc1** | Li et al., 2023 | Electrons flow downstream “via cytochrome c4 Cyc1 and the aa3-type cytochrome oxidase complex.” | **Strong; downhill aerobic branch.** (li2023sequencesimilaritynetwork pages 2-4) |
| 5 | **aa₃ oxidase —reduces→ O₂ to H₂O** | Li et al., 2023 | Downstream flow is described as “reducing O2 to water.” | **Strong terminal-reaction edge.** (li2023sequencesimilaritynetwork pages 2-4) |
| 6 | **downhill electron transport —supports→ ATP synthesis** | Wang et al., 2024 | “it is necessary to synthesize sufficient ATP through the downhill pathway”; approximately 95% of electrons were reported to enter that branch. | **Moderate.** The 95% figure is a cited model-system estimate, not a universal flux. (wang2024characterizethegrowth pages 1-2) |
| 7 | **rusticyanin branch —supports→ reverse electron transport / NADH generation** | Li et al., 2023 | Electrons can flow “upstream, utilizing the proton motive force…to…transfer electrons to the NADH1 complex.” | **Strong for pathway architecture; taxon-specific.** Avoid encoding the prose as one universal direct molecular edge. (li2023sequencesimilaritynetwork pages 2-4) |
| 8 | **Cyc2 —oxidizes→ dissolved Fe(II)** | Hoover et al., 2023, DOI 10.1128/msystems.00038-23 | “Cyc2 has been shown to oxidize dissolved Fe(II).” | **Strong for Cluster 1 Cyc2 in Gallionellaceae.** (hoover2023gallionellaceaepangenomicanalysis pages 15-17, hoover2023gallionellaceaepangenomicanalysis pages 4-8) |
| 9 | **MtoA/MtoAB —enables oxidation of→ mineral-bound Fe(II)** | Hoover et al., 2023 | “MtoA has been shown to play roles in the oxidation of mineral-bound Fe(II), specifically Fe(II) smectite clay.” | **Strong but substrate- and lineage-specific.** Prefer “enables/contributes to,” not an unqualified universal “catalyzes.” (hoover2023gallionellaceaepangenomicanalysis pages 15-17) |
| 10 | **outer-membrane c-type cytochromes —transfer electrons across→ outer membrane** | Hoover et al., 2023 | “Both Cyc2 and MtoA are c-type cytochromes that transport electrons across the outer membrane.” | **Strong localization/process edge.** (hoover2023gallionellaceaepangenomicanalysis pages 4-8) |
| 11 | **PioABC —enables→ phototrophic Fe(II) oxidation** | Li et al., 2023 | Canonical table assigns PioA, PioB, and PioC to neutrophilic Fe(II)-oxidizing *Rhodopseudomonas*. | **Moderate in this evidence set; taxon-specific.** Curate only with the original mutant/biochemical study attached. (li2023sequencesimilaritynetwork pages 2-4, li2023sequencesimilaritynetwork media 0f1522cd) |
| 12 | **Cyc572 pathway —enables→ Fe(II) oxidation** | Li et al., 2023 | Canonical *Leptospirillum* module contains outer-membrane Cyc572, periplasmic Cyc579, bc₁, and cbb₃ oxidase. | **Moderate; taxon-specific synthesis.** Do not assume each consecutive direct physical interaction without primary evidence. (li2023sequencesimilaritynetwork pages 2-4, li2023sequencesimilaritynetwork media 0f1522cd) |
| 13 | **Fe(II)-oxidation respiration —provides energy/reducing power for→ CO₂ fixation** | Wang et al., 2024; Hoover et al., 2023 | *A. ferrooxidans* uses O₂ as acceptor and fixes CO₂ by the CBB cycle; Gallionellaceae FeOB encode reverse electron transport and carbon-fixation machinery. | **Moderate-to-strong in autotrophic taxa; not universal.** (hoover2023gallionellaceaepangenomicanalysis pages 1-2, wang2024characterizethegrowth pages 1-2) |
| 14 | **Fe(III) generation —promotes→ extracellular mineral precipitation** | Wang et al., 2024; Li et al., 2023 | Jarosite accumulated during Fe(II)-supported growth; extracellular organization prevents Fe(III) precipitation in the neutral cytoplasm. | **Context-specific.** Mineral identity depends on pH, sulfate, oxygen, and medium. (wang2024characterizethegrowth pages 1-2, li2023sequencesimilaritynetwork pages 2-4) |
| 15 | **Fe(III) —oxidizes/dissolves→ metal sulfides** | Tonietti et al., 2024, DOI 10.3390/microorganisms12122407 | *A. ferrooxidans* generates Fe(III) under oxic conditions, and these ions react with metal sulfides. | **Strong application-level edge**, but indirect bioleaching rather than a cell-internal edge. (tonietti2024unveilingthebioleaching pages 1-2) |

## Recent developments, 2023–2024

### Comparative genomics and structural evolution

Li et al. reported at least eight recognized Fe(II)-oxidation pathways and used sequence-similarity networks plus RoseTTAFold modeling to compare components with low sequence identity. Their analysis supported wide taxonomic dispersal and possible horizontal transfer of iron-oxidation modules, while also showing that structural similarity does not itself establish catalytic function. This argues for a family of taxon-specific subgraphs beneath one trait node rather than a single universal chain. Published October 2023. (li2023sequencesimilaritynetwork pages 16-17, li2023sequencesimilaritynetwork pages 1-2)

Hoover et al. analyzed **103 Gallionellaceae genomes**. Among Fe-oxidizer genomes, **83% contained `cyc2`, 41% contained `mtoA`, 37% contained both, and 89% contained at least one** of these markers. Fe oxidizers averaged **1.5-fold more CXXCH-containing proteins** than nitrite oxidizers, and only Fe-oxidizer genomes encoded proteins with at least ten such heme-binding motifs. These statistics support Cyc2 and MtoA as high-priority candidate nodes, but the missing 11% and the presence of uncharacterized multiheme cytochromes show that neither marker is necessary in every incomplete or divergent genome. Published December 2023. (hoover2023gallionellaceaepangenomicanalysis pages 4-8)

The same study’s interpretation is substrate-aware: Cyc2 is the simpler and more prevalent system for aqueous Fe(II), whereas MtoA is implicated in mineral-bound Fe(II), including Fe(II)-smectite. The authors also emphasize potential reversibility and functional ambiguity among homologous Mto/Mtr systems, making direction of electron flow a key curation qualifier. (hoover2023gallionellaceaepangenomicanalysis pages 15-17, hoover2023gallionellaceaepangenomicanalysis pages 4-8)

### Electroautotrophy versus Fe(II)-based chemoautotrophy

Wang et al. compared electrode-supported and Fe(II)-supported growth of *A. ferrooxidans*. Fe(II) growth produced jarosite, whereas electrode growth caused negligible mineral deposition and more pili/EPS. They detected **493 differentially expressed genes: 297 downregulated and 196 upregulated** in electroautotrophic versus chemoautotrophic conditions. This is evidence that extracellular electron uptake is mechanistically related but not synonymous with iron oxidation. Published 15 March 2024. (wang2024characterizethegrowth pages 1-2)

### Expert synthesis

The strongest current expert view is that Fe oxidation is mechanistically plural. Outer-membrane or periplasmic oxidation solves a common physiological problem—capturing electrons while keeping poorly soluble Fe(III) outside—but organisms use distinct Cyc2, Mto, Pio, Cyc572, Fox, and archaeal systems. Genomic marker calls should therefore be evidence-weighted by protein cluster, genomic neighborhood, expression, biochemistry, substrate, and observed Fe(II)/Fe(III) chemistry. (li2023sequencesimilaritynetwork pages 16-17, hoover2023gallionellaceaepangenomicanalysis pages 4-8, li2023sequencesimilaritynetwork pages 2-4)

## Applications and implementations

### Biomining and bioleaching

The mature real-world application is acidic biomining. *A. ferrooxidans* regenerates Fe(III), which chemically attacks metal sulfides and allows continued metal solubilization. A 2024 article states that microbiome-mediated bioleaching accounts for **over 30% of global copper production from low-grade ores**; this is a field-scale contextual estimate, not an *A. ferrooxidans*-only attribution. (wang2024characterizethegrowth pages 1-2)

The 2024 review lists mobilization or recovery involving Li, P, V, Cr, Fe, Ni, Cu, Zn, Ga, As, Mo, W, Pb, and U. It reports approximately **30% average vanadium recovery** in the reviewed systems and describes Fe(III)-mediated oxidation of U(IV) to soluble U(VI). These values are application-specific and should not become trait-level performance properties. (tonietti2024unveilingthebioleaching pages 1-2, tonietti2024unveilingthebioleaching pages 12-13)

Applications include low-grade ores, mine tailings, electronic and LED wastes, municipal-waste ash, uranium-contaminated mine water, and prospective space biomining. Evidence for extraterrestrial use remains experimental or prospective; it is not yet an operational implementation of the trait. (tonietti2024unveilingthebioleaching pages 27-28, tonietti2024unveilingthebioleaching pages 21-23)

### Environmental consequences and treatment potential

Biogenic Fe(III) minerals can sorb or co-precipitate metals and metalloids, making Fe oxidizers relevant to water treatment and contaminant immobilization. Conversely, acidic iron/sulfur oxidation can generate or intensify acid mine drainage. The November 2024 review therefore frames *A. ferrooxidans* as both a sustainable extraction agent and an environmental risk requiring monitoring of acidic releases. (tonietti2024unveilingthebioleaching pages 1-2)

### Carbon capture and bioproduct platforms

Autotrophic Fe oxidizers connect inorganic electron donors to CO₂ fixation. This supports interest in engineered chemolithoautotrophic production, but direct Fe(II)-powered product yields were not established by the retrieved 2023–2024 evidence. Electroautotrophic and *Rhodopseudomonas* bioplastic studies are adjacent platform research and should not be represented as direct applications of Fe(II) oxidation without an Fe(II)-fed production experiment. (wang2024characterizethegrowth pages 26-26, wang2024characterizethegrowth pages 1-2)

## Recommended initial YAML architecture

Use a small universal core plus contextual subgraphs:

1. **Core:** Fe(II) → extracellular/periplasmic iron-oxidation system → electron-transport chain → terminal acceptor; Fe(II) → Fe(III); electron transport → proton motive force/ATP.
2. **Acidithiobacillus aerobic subgraph:** Cyc2 → Rus → Cyc1 → aa₃ oxidase → O₂/H₂O; Rus → reverse electron transport → reducing power → CBB carbon fixation.
3. **Gallionellaceae circumneutral subgraph:** dissolved Fe(II) → Cluster 1 Cyc2; mineral-bound Fe(II) → MtoAB; periplasmic carriers → respiratory chain.
4. **Phototrophic subgraph:** light + Fe(II) + PioABC → photosynthetic electron transport/carbon fixation.
5. **Leptospirillum subgraph:** Cyc572 → Cyc579 → bc₁/cbb₃ respiratory module.
6. **Application subgraph:** Fe(II) oxidation → Fe(III) regeneration → metal-sulfide oxidation → metal solubilization.

Predicates should distinguish **directly catalyzes**, **transfers electrons to**, **enables**, **associated with**, and **produces**. Do not collapse all evidence into a generic `causes` relation.

## Warnings: claims not yet ready for curation

1. **Do not infer the trait from arbitrary `cyc2` homologs.** Cluster 2 and other remote homologs require biochemical, expression, or strong contextual support. (hoover2023gallionellaceaepangenomicanalysis pages 4-8)
2. **Do not encode Mto/Mtr direction from homology alone.** Electron transfer can be reversible, and MtoA/MtrA may be difficult to distinguish computationally. (hoover2023gallionellaceaepangenomicanalysis pages 4-8)
3. **Do not make nitrate a universal terminal acceptor.** Nitrate reduction is rare in Gallionellaceae and may require community cooperation; assign it only to the tested isolate or consortium. (hoover2023gallionellaceaepangenomicanalysis pages 15-17)
4. **Do not equate gene presence with phenotype.** The 2023 pangenome study included MAGs and explicitly used marker inference; physiological confirmation is stronger.
5. **Do not universalize PioABC or Cyc572.** Both are lineage-specific modules.
6. **Do not curate light as a requirement for all Fe oxidation.** It is specific to photoferrotrophy.
7. **Do not curate jarosite as the universal product.** It was observed in a particular acidic, sulfate-containing *A. ferrooxidans* experiment. (wang2024characterizethegrowth pages 1-2)
8. **Do not conflate electrode uptake with Fe(II) oxidation.** Their transcriptomic, EPS, pili, and precipitation phenotypes differ. (wang2024characterizethegrowth pages 1-2)
9. **Treat broad biomining efficiencies cautiously.** “Over 30% of low-grade copper production” is a sector estimate, while ~30% vanadium recovery summarizes particular reviewed systems; neither is an intrinsic trait parameter. (tonietti2024unveilingthebioleaching pages 12-13, wang2024characterizethegrowth pages 1-2)
10. **Validate all ontology identifiers against the target release.** Protein nodes should normally use strain-specific UniProt accessions; label-only nodes are safer than invented or overgeneralized CURIEs.

## DOI-first bibliography

1. Li L, Liu Z, Meng D, et al. **Sequence similarity network and protein structure prediction offer insights into the evolution of microbial pathways for ferrous iron oxidation.** *mSystems*. Published October 2023. https://doi.org/10.1128/msystems.00720-23. (li2023sequencesimilaritynetwork pages 1-2)
2. Hoover RL, Keffer JL, Polson SW, Chan CS. **Gallionellaceae pangenomic analysis reveals insight into phylogeny, metabolic flexibility, and iron oxidation mechanisms.** *mSystems* 8(6). Published December 2023. https://doi.org/10.1128/msystems.00038-23. (hoover2023gallionellaceaepangenomicanalysis pages 1-2)
3. Wang Q, Long H, Wang H, Lau Vetter MCY. **Characterize the Growth and Metabolism of Acidithiobacillus ferrooxidans under Electroautotrophic and Chemoautotrophic Conditions.** *Microorganisms* 12:590. Published 15 March 2024. https://doi.org/10.3390/microorganisms12030590. (wang2024characterizethegrowth pages 1-2)
4. Tonietti L, Esposito M, Cascone M, et al. **Unveiling the Bioleaching Versatility of Acidithiobacillus ferrooxidans.** *Microorganisms* 12:2407. Published 23 November 2024. https://doi.org/10.3390/microorganisms12122407. (tonietti2024unveilingthebioleaching pages 1-2)
5. Huang Y-M, Straub D, Blackwell N, Kappler A, Kleindienst S. **Meta-omics Reveal Gallionellaceae and Rhodanobacter Species as Interdependent Key Players for Fe(II) Oxidation and Nitrate Reduction in the Autotrophic Enrichment Culture KS.** *Applied and Environmental Microbiology* 87(15). Published July 2021. https://doi.org/10.1128/AEM.00496-21.
6. Emerson D, Fleming EJ, McBeth JM. **Iron-oxidizing bacteria: an environmental and genomic perspective.** *Annual Review of Microbiology*. Published October 2010. https://doi.org/10.1146/annurev.micro.112408.134208.
7. Hedrich S, Schlömann M, Johnson DB. **The iron-oxidizing proteobacteria.** *Microbiology*. 2011. https://doi.org/10.1099/mic.0.045344-0.

**Curation priority:** the highest-confidence immediate expansion of the existing 12-node/7-edge graph is the *A. ferrooxidans* Cyc2–Rus bifurcation plus separate Gallionellaceae Cyc2 and MtoAB substrate-specific branches. PioABC, Cyc572, nitrate-associated oxidation, and novel multiheme systems should remain explicitly taxon- or assay-qualified until their primary experimental evidence is attached.

References

1. (li2023sequencesimilaritynetwork pages 1-2): Liangzhi Li, Zhenghua Liu, Delong Meng, Yongjun Liu, Tianbo Liu, Chengying Jiang, and Huaqun Yin. Sequence similarity network and protein structure prediction offer insights into the evolution of microbial pathways for ferrous iron oxidation. Oct 2023. URL: https://doi.org/10.1128/msystems.00720-23, doi:10.1128/msystems.00720-23. This article has 8 citations and is from a peer-reviewed journal.

2. (li2023sequencesimilaritynetwork pages 2-4): Liangzhi Li, Zhenghua Liu, Delong Meng, Yongjun Liu, Tianbo Liu, Chengying Jiang, and Huaqun Yin. Sequence similarity network and protein structure prediction offer insights into the evolution of microbial pathways for ferrous iron oxidation. Oct 2023. URL: https://doi.org/10.1128/msystems.00720-23, doi:10.1128/msystems.00720-23. This article has 8 citations and is from a peer-reviewed journal.

3. (wang2024characterizethegrowth pages 1-2): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 11 citations.

4. (hoover2023gallionellaceaepangenomicanalysis pages 15-17): Rene L. Hoover, Jessica L. Keffer, Shawn W. Polson, and Clara S. Chan. Gallionellaceae pangenomic analysis reveals insight into phylogeny, metabolic flexibility, and iron oxidation mechanisms. Dec 2023. URL: https://doi.org/10.1128/msystems.00038-23, doi:10.1128/msystems.00038-23. This article has 31 citations and is from a peer-reviewed journal.

5. (hoover2023gallionellaceaepangenomicanalysis pages 4-8): Rene L. Hoover, Jessica L. Keffer, Shawn W. Polson, and Clara S. Chan. Gallionellaceae pangenomic analysis reveals insight into phylogeny, metabolic flexibility, and iron oxidation mechanisms. Dec 2023. URL: https://doi.org/10.1128/msystems.00038-23, doi:10.1128/msystems.00038-23. This article has 31 citations and is from a peer-reviewed journal.

6. (li2023sequencesimilaritynetwork pages 16-17): Liangzhi Li, Zhenghua Liu, Delong Meng, Yongjun Liu, Tianbo Liu, Chengying Jiang, and Huaqun Yin. Sequence similarity network and protein structure prediction offer insights into the evolution of microbial pathways for ferrous iron oxidation. Oct 2023. URL: https://doi.org/10.1128/msystems.00720-23, doi:10.1128/msystems.00720-23. This article has 8 citations and is from a peer-reviewed journal.

7. (li2023sequencesimilaritynetwork media 0f1522cd): Liangzhi Li, Zhenghua Liu, Delong Meng, Yongjun Liu, Tianbo Liu, Chengying Jiang, and Huaqun Yin. Sequence similarity network and protein structure prediction offer insights into the evolution of microbial pathways for ferrous iron oxidation. Oct 2023. URL: https://doi.org/10.1128/msystems.00720-23, doi:10.1128/msystems.00720-23. This article has 8 citations and is from a peer-reviewed journal.

8. (hoover2023gallionellaceaepangenomicanalysis pages 1-2): Rene L. Hoover, Jessica L. Keffer, Shawn W. Polson, and Clara S. Chan. Gallionellaceae pangenomic analysis reveals insight into phylogeny, metabolic flexibility, and iron oxidation mechanisms. Dec 2023. URL: https://doi.org/10.1128/msystems.00038-23, doi:10.1128/msystems.00038-23. This article has 31 citations and is from a peer-reviewed journal.

9. (tonietti2024unveilingthebioleaching pages 1-2): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 57 citations.

10. (tonietti2024unveilingthebioleaching pages 12-13): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 57 citations.

11. (tonietti2024unveilingthebioleaching pages 27-28): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 57 citations.

12. (tonietti2024unveilingthebioleaching pages 21-23): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 57 citations.

13. (wang2024characterizethegrowth pages 26-26): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 11 citations.