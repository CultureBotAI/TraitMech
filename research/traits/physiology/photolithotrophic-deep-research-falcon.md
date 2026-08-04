---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:54:14.491331'
end_time: '2026-08-04T12:01:37.850679'
duration_seconds: 443.36
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: photolithotrophic
  trait_identifier: METPO:1000658
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: photolithotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism uses light as the energy source
    and inorganic compounds as electron donors, typically with carbon dioxide as the
    primary carbon source.
  parent_traits: METPO:1000631
  synonyms: photolithotroph
  evidence_summary: 'DOI:10.3390/antiox10060829: anoxygenic photosynthesis (Review
    supports light-driven oxidation of reduced sulfur compounds by photolithotrophic
    sulfur bacteria.) | DOI:10.3389/fmicb.2017.00323: light as an energy source and
    reduced iron (Review supports Fe(II) as an inorganic electron donor for photoferrotrophy.)'
  causal_graph_summary: 'photolithotrophic_inorganic_electron_donors: 14 nodes, 13
    edges'
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
- **Trait label:** photolithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000658
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses light as the energy source and inorganic compounds as electron donors, typically with carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithotroph
- **Existing evidence:** DOI:10.3390/antiox10060829: anoxygenic photosynthesis (Review supports light-driven oxidation of reduced sulfur compounds by photolithotrophic sulfur bacteria.) | DOI:10.3389/fmicb.2017.00323: light as an energy source and reduced iron (Review supports Fe(II) as an inorganic electron donor for photoferrotrophy.)
- **Existing causal graph summary:** photolithotrophic_inorganic_electron_donors: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **photolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithotrophic.yaml`.

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
- **Trait label:** photolithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000658
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses light as the energy source and inorganic compounds as electron donors, typically with carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithotroph
- **Existing evidence:** DOI:10.3390/antiox10060829: anoxygenic photosynthesis (Review supports light-driven oxidation of reduced sulfur compounds by photolithotrophic sulfur bacteria.) | DOI:10.3389/fmicb.2017.00323: light as an energy source and reduced iron (Review supports Fe(II) as an inorganic electron donor for photoferrotrophy.)
- **Existing causal graph summary:** photolithotrophic_inorganic_electron_donors: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **photolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithotrophic.yaml`.

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


# Curation report: photolithotrophic

## Record and recommendation

- **Trait:** photolithotrophic
- **Identifier:** **`METPO:1000658`**
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** `METPO:1000631`
- **Recommended graph design:** retain the trait as a high-level physiological capacity, then represent alternative, taxon-scoped mechanistic branches for sulfur photolithotrophy, photoferrotrophy, hydrogen-based photolithotrophy, and oxygenic water oxidation. The strongest evidence retrieved here supports the sulfur and Fe(II) branches.

## 1. Scope and boundaries

### Operational definition

Photolithotrophy is the capacity to use **light as the energy source** and a **reduced inorganic compound as the electron donor**. In the best-characterized microbial examples, electron transfer supports generation of ATP and reductant, while inorganic carbon is assimilated into biomass. Green sulfur bacteria (GSB) use H₂S as a principal donor, oxidize it initially to elemental sulfur, and fix CO₂ through the reductive—or reverse—TCA cycle. Photoferrotrophy uses light, Fe(II), and inorganic carbon. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, gupta2020extracellularelectronuptake pages 7-8)

The submitted definition says CO₂ is “typically” the primary carbon source. That qualification is important: **photolithotrophy describes energy and electron sources, whereas autotrophy describes carbon source**. Thus, `photolithotrophic` should not be made logically equivalent to `photolithoautotrophic`. A separate edge such as `photolithotrophic organism — may_fix — CO2` is safer than making CO₂ fixation universally necessary.

### Boundary cases

1. **Photoorganoheterotrophy:** light is used, but electrons and/or carbon are obtained from organic compounds. This is not photolithotrophy.
2. **Chemolithotrophy:** the donor is inorganic, but energy is obtained from chemical oxidation without light. This is not photolithotrophy.
3. **Oxygenic photolithotrophy:** cyanobacteria use water as the donor and produce O₂. It belongs within the broad trait definition, but not within an anoxygenic-sulfur-specific mechanism.
4. **Anoxygenic photolithotrophy:** H₂S, thiosulfate, H₂, or Fe(II) can replace water as donor; oxygen is not evolved. The retrieved 2024 review explicitly lists H₂S, H₂, and ferrous iron as alternative donors. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17)
5. **Mixotrophy:** some GSB can assimilate acetate while retaining light-driven lithotrophic metabolism. Conversely, inability to grow heterotrophically on glucose was reported for the reviewed GSB models. Carbon-substrate utilization therefore must not be inferred solely from the photolithotrophic label. (kushkevych2024anoxygenicphotosynthesiswith pages 13-14)
6. **Genotype-only assignments:** presence of `sqr`, `cyc2`, `pioABC`, `sox`, or photosynthesis genes is mechanistic evidence, but not by itself a demonstrated trait. For example, SQR homologues occur even in *Chlorobium ferrooxidans*, which cannot use sulfur as its sole donor. (kushkevych2021anoxygenicphotosynthesisin pages 3-5)

## 2. Current mechanistic understanding

### Sulfur-based branch

In GSB, chlorosomes collect light and transfer excitation through the Fenna–Matthews–Olson complex to a type-I reaction center. Chlorosomes are exceptionally effective under low irradiance: the 2024 review reports operation below **4 µEinstein m⁻² s⁻¹** and describes assemblies containing hundreds of thousands of bacteriochlorophyll molecules. (kushkevych2024anoxygenicphotosynthesiswith pages 4-6)

H₂S oxidation is initiated by membrane-associated sulfide:quinone oxidoreductase (SQR). SQR oxidizes sulfide while reducing menaquinone to menaquinol; flavocytochrome-c sulfide dehydrogenase can provide an alternative route. Reaction-center electron transfer proceeds through chlorophyll *a*, phylloquinone, and Fe–S centers to ferredoxin. Reduced ferredoxin and ferredoxin:NAD⁺ oxidoreductase systems provide reducing power for biosynthesis. (kushkevych2024anoxygenicphotosynthesiswith pages 9-10)

Thiosulfate use is lineage-dependent. The Sox system supports thiosulfate oxidation in organisms such as *Rhodovulum sulfidophilum*, while some GSB can oxidize thiosulfate and tetrathionate. Stored elemental sulfur and its subsequent oxidation involve additional systems, including reverse/dissimilatory sulfite-reductase machinery, but these modules are not universal among all photolithotrophs. (kushkevych2024anoxygenicphotosynthesiswith pages 9-10, kushkevych2024anoxygenicphotosynthesiswith pages 18-18, kushkevych2021anoxygenicphotosynthesisin pages 3-5)

### Photoferrotrophic branch

Photoferrotrophs couple light energy to oxidation of soluble Fe(II) or reduced iron minerals. In *Rhodopseudomonas palustris* TIE-1, PioA is a periplasmic decaheme cytochrome, PioB an outer-membrane β-barrel, and PioC a periplasmic high-potential Fe–S protein. The reviewed model transfers electrons from Fe(II) through PioAB and PioC toward the photosynthetic reaction center. PioAB-mediated uptake from solid extracellular substrates has direct support in TIE-1. (gupta2020extracellularelectronuptake pages 7-8, gupta2020extracellularelectronuptake pages 8-9)

Cyc2 homologues occur in some *Chlorobium* genomes and are candidates for extracellular Fe(II) oxidation, but the review stresses that molecular mechanisms remain incompletely resolved. Cyc2 presence should therefore be curated as a **candidate mechanism**, not as proof of photoferrotrophy. (gupta2020extracellularelectronuptake pages 7-8, gupta2020extracellularelectronuptake pages 4-5, gupta2020extracellularelectronuptake pages 8-9)

## 3. Candidate nodes

### Trait and biological-process nodes

- `METPO:1000658` — photolithotrophic
- `GO:0015979` — photosynthesis
- `GO:0015977` — carbon fixation
- Anoxygenic photosynthesis — verify the current GO identifier before YAML insertion
- Photoferrotrophy — label-only candidate
- Sulfide-dependent photolithotrophy — label-only candidate
- Thiosulfate-dependent photolithotrophy — label-only candidate
- Reverse/reductive TCA cycle — pathway node; verify pathway CURIE against the target ontology release
- Calvin–Benson–Bassham cycle — pathway node; applies to selected photoferrotrophs and oxygenic phototrophs, not GSB generally

### Chemicals and physical factors

- `CHEBI:16136` — hydrogen sulfide
- `CHEBI:16526` — carbon dioxide
- `CHEBI:15377` — water
- `CHEBI:15379` — dioxygen
- `CHEBI:29033` — iron(2+)
- Thiosulfate, tetrathionate, elemental sulfur, sulfate, menaquinone, menaquinol, phylloquinone, ferredoxin, NAD⁺/NADH, proton or sodium electrochemical gradient, ATP, and fluoroacetate — verify exact ChEBI records before insertion
- Light availability, wavelength, irradiance, anoxia, reducing redox potential, temperature, sulfide concentration — experimental/environmental-factor nodes

### Structures, proteins, and complexes

- Chlorosome; FMO complex; photosynthetic reaction center; LH1/LH2; bacteriochlorophyll; Fe–S centers FX/FA/FB
- Sulfide:quinone oxidoreductase (SQR)
- Flavocytochrome-c sulfide dehydrogenase
- Sox multienzyme system
- Reverse-Dsr sulfur-oxidation system
- PioA, PioB, PioC, PioABC complex
- Cyc2
- Ferredoxin:NAD⁺ oxidoreductase/RNF complex
- Aconitase
- ATP synthase: biologically plausible downstream node, but direct coupling evidence should be added before making it a core edge in this graph

Protein CURIEs should be strain-specific UniProt accessions. Because no single accession represents SQR, PioABC, Cyc2, or FMO across all photolithotrophs, label-only nodes are preferable until the graph’s taxonomic scope is fixed.

### Taxonomic and habitat/context nodes

- Green sulfur bacteria/Chlorobiaceae
- Purple sulfur bacteria/Chromatiaceae
- Purple nonsulfur phototrophs, including *R. palustris* TIE-1
- *Chlorobaculum tepidum*, *Chlorobium limicola*, *Chlorobium ferrooxidans*, *Allochromatium vinosum*
- Anoxic illuminated water, sediment photic–anoxic interfaces, euxinic waters, ferruginous water columns, meromictic-lake chemoclines, illuminated anaerobic reactors

NCBI Taxonomy and ENVO identifiers should be resolved using the exact accepted taxon and habitat labels at curation time rather than inferred from family names.

## 4. Candidate causal edges

The compact curation table is provided below; expanded evidence notes follow.

| subject | predicate | object | taxonomic scope | evidence strength | DOI |
|---|---|---|---|---|---|
| light | powers | photosynthetic reaction center electron transfer | broad photolithotrophs; direct review support strongest for anoxygenic sulfur phototrophs | strong | 10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 9-10, kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| chlorosome | enables | low-light light capture | GSB-specific | strong | 10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 4-6, kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| hydrogen sulfide (H2S) | is oxidized by | sulfide:quinone oxidoreductase (SQR) | sulfur photolithotrophs; strongest direct support in GSB | strong | 10.3389/fmicb.2024.1417714; 10.3390/antiox10060829 (kushkevych2024anoxygenicphotosynthesiswith pages 9-10, kushkevych2021anoxygenicphotosynthesisin pages 3-5) |
| sulfide:quinone oxidoreductase (SQR) | reduces | menaquinone to menaquinol | GSB-specific direct support | strong | 10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 9-10) |
| thiosulfate | is oxidized by | Sox enzyme system | taxon-specific; demonstrated in some sulfur phototrophs, not universal for all photolithotrophs | moderate | 10.3390/antiox10060829 (kushkevych2021anoxygenicphotosynthesisin pages 3-5) |
| photosynthetic reaction center | transfers electrons to | ferredoxin | GSB-specific direct support | strong | 10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 9-10) |
| reduced ferredoxin | supports | reverse TCA cycle CO2 fixation | GSB-specific direct support | strong | 10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 9-10, kushkevych2024anoxygenicphotosynthesiswith pages 13-14, kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| Fe(II) | donates electrons via | PioAB/PioC electron uptake pathway | photoferrotrophic purple bacteria; strongest support in Rhodopseudomonas palustris TIE-1 | moderate | 10.1007/s10295-020-02309-0 (gupta2020extracellularelectronuptake pages 7-8, gupta2020extracellularelectronuptake pages 8-9) |
| PioC | transfers electrons to | photosynthetic reaction center | R. palustris TIE-1 model; mechanism summarized in review | moderate | 10.1007/s10295-020-02309-0 (gupta2020extracellularelectronuptake pages 8-9) |
| anoxic conditions | enable | anoxygenic photolithotrophic growth/photosynthesis | broad anoxygenic sulfur phototrophs | strong | 10.3390/antiox10060829; 10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 16-17, kushkevych2021anoxygenicphotosynthesisin pages 3-5) |
| light availability | enables | sulfide detoxification and photolithotrophic growth | sulfur photolithotrophs; reactor/cultivation evidence available | strong | 10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 13-14, kushkevych2024anoxygenicphotosynthesiswith pages 16-17, kushkevych2024anoxygenicphotosynthesiswith pages 15-16) |
| fluoroacetate | inhibits | aconitase | GSB-specific experimental condition | moderate | 10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 13-14) |
| Cyc2 homolog | may mediate | Fe(II) oxidation/electron uptake | some Chlorobium/photoferrotroph genomes; genotype-to-phenotype link unresolved | uncertain | 10.1007/s10295-020-02309-0; 10.3389/fmicb.2017.00323 (kushkevych2024anoxygenicphotosynthesiswith pages 4-6, gupta2020extracellularelectronuptake pages 7-8) |


*Table: This table summarizes concise, curation-ready candidate causal edges for the photolithotrophic trait, with taxonomic scope, evidence strength, and DOI/context citations. It highlights which edges are broadly supported versus lineage-specific or still uncertain.*

| Proposed triple | Supporting source snippet | Curation note |
|---|---|---|
| light — **powers** → photosynthetic reaction-center electron transfer | The 2024 review describes FMO-to-reaction-center light transfer and subsequent electron transfer through chlorophyll, phylloquinone, and Fe–S centers. (kushkevych2024anoxygenicphotosynthesiswith pages 9-10) | Strong, but instantiate separately for type-I GSB and type-II purple-bacterial systems. |
| chlorosome — **enables** → low-light photon capture | Chlorosomes are described as highly efficient antennas functional below 4 µEinstein m⁻² s⁻¹. (kushkevych2024anoxygenicphotosynthesiswith pages 4-6) | Strong; GSB-specific, not a universal photolithotrophy edge. |
| H₂S — **electron_donor_for** → anoxygenic photosynthesis | GSB are described as anaerobic phototrophs using reduced sulfur compounds, principally H₂S, as electron donors. (kushkevych2024anoxygenicphotosynthesiswith pages 4-6, kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | Strong for sulfur phototrophs. |
| H₂S — **is_oxidized_by** → SQR | “SQR” is identified as the membrane enzyme initiating sulfide oxidation. (kushkevych2021anoxygenicphotosynthesisin pages 3-5, kushkevych2024anoxygenicphotosynthesiswith pages 9-10) | Strong; allow flavocytochrome-c sulfide dehydrogenase as an alternative branch. |
| SQR — **reduces** → menaquinone | The 2024 synthesis states that SQR oxidation of H₂S reduces menaquinone to menaquinol. (kushkevych2024anoxygenicphotosynthesiswith pages 9-10) | Strong in GSB; do not generalize the quinone species to every lineage. |
| thiosulfate — **is_oxidized_by** → Sox system | The Sox system catalyzes thiosulfate oxidation in *R. sulfidophilum*. (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | Strong but taxon-specific; not all sulfur phototrophs possess a complete Sox pathway. |
| reaction center — **reduces** → ferredoxin | Electrons pass via chlorophyll *a*, phylloquinone, FX/FA/FB to ferredoxin. (kushkevych2024anoxygenicphotosynthesiswith pages 9-10) | Strong for type-I GSB reaction centers. |
| reduced ferredoxin — **supplies_reductant_to** → reductive TCA CO₂ fixation | GSB use reduced ferredoxin-associated metabolism and fix CO₂ through the reverse TCA cycle. (kushkevych2024anoxygenicphotosynthesiswith pages 9-10, kushkevych2024anoxygenicphotosynthesiswith pages 13-14, kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | Strong at pathway level; avoid asserting one direct enzyme reaction without primary biochemical evidence. |
| Fe(II) — **electron_donor_for** → photoferrotrophy | *R. palustris* TIE-1 oxidizes soluble Fe(II) and reduced iron minerals using light. (gupta2020extracellularelectronuptake pages 7-8) | Strong phenotype edge. |
| Fe(II) — **donates_electrons_via** → PioAB/PioC | PioA/PioB conduct extracellular electrons and PioC passes them toward the photosynthetic reaction center. (gupta2020extracellularelectronuptake pages 7-8, gupta2020extracellularelectronuptake pages 8-9) | Moderate-to-strong for TIE-1; taxon-specific. |
| pio operon — **is_required_for** → phototrophic Fe(II) oxidation | The review identifies genetic evidence that the pio operon is essential for phototrophic Fe(II) oxidation. (gupta2020extracellularelectronuptake pages 11-12) | Promising causal edge, but the retrieved passage is bibliography-level; attach the primary knockout paper before final curation. |
| anoxic conditions — **enable** → anoxygenic sulfur photolithotrophy | Sulfur photolithotrophy is described as occurring without molecular oxygen; GSB occupy anaerobic, reducing habitats. (kushkevych2024anoxygenicphotosynthesiswith pages 4-6, kushkevych2021anoxygenicphotosynthesisin pages 3-5) | Strong for obligately anaerobic GSB; oxygen tolerance varies across anoxygenic phototrophs. |
| light availability — **enables** → phototrophic sulfide removal | Reactor sulfide removal stopped when illumination was removed. (kushkevych2024anoxygenicphotosynthesiswith pages 15-16) | Strong application-specific intervention evidence. |
| fluoroacetate — **inhibits** → aconitase | Fluoroacetate inhibition of aconitase is reported in the reviewed GSB metabolic experiments. (kushkevych2024anoxygenicphotosynthesiswith pages 13-14) | Assay- and taxon-specific; useful as validation evidence, not a trait-defining edge. |
| Cyc2 — **may_enable** → phototrophic Fe(II) oxidation | Cyc2 homologues occur in *Chlorobium* genomes, but the mechanistic link remains incompletely demonstrated. (gupta2020extracellularelectronuptake pages 7-8, gupta2020extracellularelectronuptake pages 4-5) | **Uncertain; do not curate as established causation.** |

## 5. Recent research, applications, and quantitative evidence

### 2024 synthesis and genomic expansion

Kushkevych and colleagues’ July 2024 review integrates physiology and genomics of GSB. Its survey covers **509 genomes**, with reported genome sizes of approximately **1.9–3.3 Mbp** and roughly **87% coding sequence**. The review highlights conserved carbon-fixation capacity, sulfur-oxidation genes, nitrogenase genes, and possible iron-related electron-transfer systems. These data broaden the comparative context, but gene presence should remain distinct from experimentally verified donor use. (kushkevych2024anoxygenicphotosynthesiswith pages 4-6)

### Low-light specialization

GSB chlorosomes support photosynthesis at irradiances below **4 µEinstein m⁻² s⁻¹**, explaining occupation of deep, shaded, or sediment-associated photic–anoxic interfaces. GSB tolerate lower light than purple sulfur bacteria but are generally more sensitive to oxidizing conditions. (kushkevych2024anoxygenicphotosynthesiswith pages 4-6, kushkevych2024anoxygenicphotosynthesiswith pages 1-2)

### H₂S detoxification and sulfur recovery

Reported phototrophic reactor results include:

- **81–95% H₂S removal** in column systems;
- **92–95% conversion to elemental sulfur** in tube systems;
- tolerance of approximately **100–150 mg L⁻¹ H₂S**;
- complete desulfurization after **7 days** in one summarized study;
- an optimum around **1% H₂S** in a reviewed setup;
- **10 kLx** supporting better *C. limicola* growth than **25 kLx** under the tested conditions;
- consumption of about **one-third of the CO₂** during photosynthetic biogas upgrading. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17, kushkevych2024anoxygenicphotosynthesiswith pages 15-16)

These implementations are relevant to illuminated anaerobic wastewater treatment, biogas desulfurization, sulfur recovery, and simultaneous CO₂ capture. Elemental sulfur is particularly attractive because it is insoluble and more readily separated than sulfate. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 15-16)

### Bioelectrochemical applications

GSB-containing consortia have been investigated in microbial electrochemical systems. One summarized experiment produced **118 ± 16 µA in darkness versus 61 ± 11 µA in light**, showing that current production in a mixed consortium does not necessarily report photolithotrophic activity directly. Such results should be treated as reactor-level observations, not organism-level trait evidence. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17)

### Expert assessment

The current literature supports a modular rather than universal mechanism. Sulfur phototrophs and photoferrotrophs share light-driven energy conservation but differ in donor-oxidation machinery, reaction-center architecture, quinones, carbon-fixation pathways, and oxygen tolerance. Reviews of extracellular electron uptake explicitly caution that many proposed Fe(II)-oxidation routes still lack complete genetic and biochemical confirmation. (gupta2020extracellularelectronuptake pages 7-8, gupta2020extracellularelectronuptake pages 4-5, gupta2020extracellularelectronuptake pages 8-9)

## 6. Warnings: claims not yet ready for TraitMech

1. **Do not define photolithotrophy as obligatorily CO₂-fixing.** Model carbon source independently.
2. **Do not make anoxia universal.** It is central to the GSB/sulfur branch but not to oxygenic cyanobacterial photolithotrophy.
3. **Do not make H₂S the universal donor.** Water, Fe(II), H₂, thiosulfate, and other inorganic donors define separate branches.
4. **Do not infer phenotype from `sqr`, `sox`, `cyc2`, or `pioABC` alone.** SQR can have detoxification roles, and Cyc2-to-photoferrotrophy links remain incompletely validated. (kushkevych2021anoxygenicphotosynthesisin pages 3-5, gupta2020extracellularelectronuptake pages 7-8)
5. **Do not generalize GSB reverse-TCA fixation to purple bacteria or cyanobacteria.** Selected purple photoferrotrophs use the CBB cycle, whereas GSB characteristically use reductive TCA. (kushkevych2024anoxygenicphotosynthesiswith pages 13-14, gupta2020extracellularelectronuptake pages 8-9)
6. **Do not curate “SQR produces elemental sulfur” as a single universal stoichiometric edge** without specifying enzyme class, organism, and subsequent sulfur chemistry.
7. **Do not yet curate RNF/Na⁺ gradient → ATP synthesis as a direct universal edge.** The review documents sodium-gradient and ferredoxin:NAD⁺ oxidoreductase involvement, but direct ATP-coupling detail was insufficient in the retrieved evidence. (kushkevych2024anoxygenicphotosynthesiswith pages 9-10)
8. **Nitrite as a photolithotrophic donor requires stronger validation.** The retrieved study reports oxidation by selected sulfur bacteria, but unusual donor claims should receive independent physiological and isotope/electron-balance confirmation before inclusion.
9. **Reactor efficiencies are not intrinsic trait constants.** Light geometry, sulfide loading, community composition, gas transfer, and reactor design strongly condition the reported values.
10. **Verify all ontology releases before YAML commit.** In particular, pathway, habitat, enzyme-class, and strain-specific protein identifiers should be resolved programmatically rather than copied from secondary literature.

## 7. DOI-first bibliography

1. **Kushkevych I, Procházka V, Vítězová M, et al.** “Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments.” *Frontiers in Microbiology* 15. **Published July 2024.** DOI: [10.3389/fmicb.2024.1417714](https://doi.org/10.3389/fmicb.2024.1417714). Principal recent source for GSB physiology, genomics, electron transfer, cultivation, and applications. (kushkevych2024anoxygenicphotosynthesiswith pages 4-6, kushkevych2024anoxygenicphotosynthesiswith pages 9-10, kushkevych2024anoxygenicphotosynthesiswith pages 13-14, kushkevych2024anoxygenicphotosynthesiswith pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 15-16)
2. **Kushkevych I, Bosáková V, Vítězová M, Rittmann SK-MR.** “Anoxygenic Photosynthesis in Photolithotrophic Sulfur Bacteria and Their Role in Detoxication of Hydrogen Sulfide.” *Antioxidants* 10:829. **Published May 2021.** DOI: [10.3390/antiox10060829](https://doi.org/10.3390/antiox10060829). Key source for SQR, Sox, sulfur donors, and H₂S detoxification. (kushkevych2021anoxygenicphotosynthesisin pages 3-5)
3. **Gupta D, Guzman MS, Bose A.** “Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications.” *Journal of Industrial Microbiology and Biotechnology* 47:863–876. **Published October 2020.** DOI: [10.1007/s10295-020-02309-0](https://doi.org/10.1007/s10295-020-02309-0). Key source for PioABC, Cyc2, extracellular electron uptake, and mechanistic uncertainty in photoferrotrophy. (gupta2020extracellularelectronuptake pages 7-8, gupta2020extracellularelectronuptake pages 4-5, gupta2020extracellularelectronuptake pages 8-9)
4. **Camacho A, Walter XA, Picazo A, Zopfi J.** “Photoferrotrophy: Remains of an Ancient Photosynthesis in Modern Environments.” *Frontiers in Microbiology* 8. **Published March 2017.** DOI: [10.3389/fmicb.2017.00323](https://doi.org/10.3389/fmicb.2017.00323). Foundational review defining light-driven Fe(II) oxidation coupled to inorganic-carbon fixation.

## Final curation judgment

`METPO:1000658` is suitable for a TraitMech graph, but the YAML should be organized as a **disjunctive modular graph**, not one linear pathway. The most defensible first release should contain a shared light-dependent core plus two evidence-rich alternatives: **(i) H₂S/SQR/quinone/type-I reaction-center/ferredoxin/reductive-TCA metabolism in GSB**, and **(ii) Fe(II)/PioABC/photosynthetic-reaction-center metabolism in *R. palustris* TIE-1**. Oxygenic water oxidation, hydrogen oxidation, Sox-mediated thiosulfate use, reverse-Dsr sulfur processing, and Cyc2-mediated photoferrotrophy should be added only as separately scoped branches with appropriate evidence and uncertainty annotations.

References

1. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

2. (gupta2020extracellularelectronuptake pages 7-8): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

3. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

4. (kushkevych2024anoxygenicphotosynthesiswith pages 13-14): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

5. (kushkevych2021anoxygenicphotosynthesisin pages 3-5): Ivan Kushkevych, Veronika Bosáková, Monika Vítězová, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis in photolithotrophic sulfur bacteria and their role in detoxication of hydrogen sulfide. Antioxidants, 10:829, May 2021. URL: https://doi.org/10.3390/antiox10060829, doi:10.3390/antiox10060829. This article has 19 citations.

6. (kushkevych2024anoxygenicphotosynthesiswith pages 4-6): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

7. (kushkevych2024anoxygenicphotosynthesiswith pages 9-10): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

8. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

9. (gupta2020extracellularelectronuptake pages 8-9): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

10. (gupta2020extracellularelectronuptake pages 4-5): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

11. (kushkevych2024anoxygenicphotosynthesiswith pages 15-16): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

12. (gupta2020extracellularelectronuptake pages 11-12): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.