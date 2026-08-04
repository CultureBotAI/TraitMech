---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:59:03.015004'
end_time: '2026-08-04T03:06:16.963445'
duration_seconds: 433.95
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range very low
  trait_identifier: METPO:1000459
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_very_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH range phenotype in which growth extends to external pH at or below
    approximately 4, characteristic of extreme-acidophile physiology.
  parent_traits: METPO:1000332
  synonyms: Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile,
    Obligative acidophile, pHR_0_to_4
  evidence_summary: "DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis\
    \ review supports growth in the pH 1\u20134 range as the extreme-acidophile growth\
    \ range.)"
  causal_graph_summary: 'ph_range_very_low_extreme_acidophile: 11 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000459
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which growth extends to external pH at or below approximately 4, characteristic of extreme-acidophile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHR_0_to_4
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth in the pH 1–4 range as the extreme-acidophile growth range.)
- **Existing causal graph summary:** ph_range_very_low_extreme_acidophile: 11 nodes, 7 edges

## Research Objective

Research the microbial trait **pH range very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_very_low.yaml`.

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
- **Trait label:** pH range very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000459
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which growth extends to external pH at or below approximately 4, characteristic of extreme-acidophile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHR_0_to_4
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth in the pH 1–4 range as the extreme-acidophile growth range.)
- **Existing causal graph summary:** ph_range_very_low_extreme_acidophile: 11 nodes, 7 edges

## Research Objective

Research the microbial trait **pH range very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_very_low.yaml`.

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


# Curation report: microbial pH range very low

## Trait and scope

**Trait:** `METPO:1000459` (“pH range very low”); category **ENVIRONMENT**; term kind **CLASS**; parent `METPO:1000332`.

The recommended operational meaning is **reproducible microbial growth whose tested external-pH range reaches pH ≤ approximately 4**. This is a range phenotype, not necessarily an optimum-pH phenotype. Recent literature often calls organisms with an optimum below pH 3 “extreme acidophiles,” whereas pH 3–5 is commonly treated as moderate acidophily. Accordingly, an organism growing from pH 3.9 to 7 qualifies for this range trait even if its optimum is above pH 3; conversely, survival after a short acid shock does not establish growth at very low pH. Leptospirillum is reported to thrive at pH ≤3.5, Acidihalobacter at pH ≤3, and acidophilic sulfate reducers can maintain an internal pH near 6 while growing below external pH 3. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, vergara2020evolutionofpredicted pages 1-3, boase2022predictionandinferred pages 1-2)

**Recommended positive assay:** growth curves, biomass increase, colony formation, substrate-dependent cell production, or serial transfer in medium whose measured pH is ≤4. Record minimum, maximum, and optimum separately, together with temperature, medium, buffering, electron donor/acceptor, salinity, and whether pH changed during growth.

**Boundary cases not equivalent to this trait:**

- **Acid survival/tolerance:** viability after transient exposure without growth.
- **Weak-organic-acid resistance:** depends on permeant undissociated acids and is not equivalent to growth at low mineral-acid pH.
- **Acid production:** lowering environmental pH does not prove that growth continues at pH ≤4.
- **Ecological detection:** a sequence or taxon detected in an acidic sample is not direct growth-range evidence.
- **Intracellular acid tolerance:** acid-stable enzymes or proteins alone do not establish the whole-cell phenotype.
- **Polyextremophily:** temperature, chloride, and metal resistance should be modeled as contextual modifiers rather than intrinsic parts of `METPO:1000459`.

## Current mechanistic understanding

Very-low-pH growth is a **systems phenotype**, not a single-gene trait. External pH ≤4 creates a steep inward proton gradient. Acidophiles combine: (i) low-permeability envelopes; (ii) an unusual inside-positive membrane potential that opposes proton entry; (iii) proton export or cation/proton exchange; (iv) proton-consuming and buffering reactions; and (v) repair of acid- and oxidative-damaged macromolecules. The relative contribution varies sharply across bacteria and archaea. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9, vergara2020evolutionofpredicted pages 1-3, mccarthy2016expandingthelimits pages 1-2)

Thermoacidophilic archaea are a distinct mechanistic branch. Their bipolar tetraether-rich membranes alter cyclopentane-ring number, tetraether:diether ratio, glycosylation, and GDNT:GDGT composition in response to pH. These changes tighten packing and preserve low passive proton permeability. This is supported by biophysical membrane work and is stronger than gene-presence inference alone. (chong2024archaeamembranesin pages 7-7)

In bacterial acidophiles, hopanoids, branched-chain lipids, cyclopropanated fatty acids, surface-layer proteins, and porin changes are proposed to reduce proton entry. Kdp, Trk, Kch, and Kef-family K⁺ systems are repeatedly associated with accumulation of positive charge and an inside-positive potential. However, many organism-specific links remain genomic or transcriptomic predictions rather than knockout/complementation demonstrations. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9, vergara2020evolutionofpredicted pages 1-3, boase2022predictionandinferred pages 2-3)

## Candidate graph nodes

### Trait, environment, and assay nodes

- `METPO:1000459` — pH range very low.
- `METPO:1000332` — supplied parent trait.
- External pH ≤4 — label-only threshold node; retain the approximate boundary in the definition.
- Proton concentration / proton — **CHEBI:15378**.
- Acid mine drainage — **ENVO:00000020**.
- Growth at pH ≤4; minimum growth pH; optimum growth pH; acid-shock survival — label-only assay/process nodes until an exact ontology match is verified.
- Chloride stress; temperature; salinity; metal load; medium buffer capacity; electron donor and acceptor — contextual nodes.

### Cellular structures and physicochemical states

- Cytoplasm — **GO:0005737**.
- Plasma membrane — **GO:0005886**.
- Cell envelope — **GO:0030313**.
- Proton-motive force — **GO:0015984**.
- Inside-positive/reversed membrane potential — label-only candidate.
- Transmembrane proton gradient — label-only candidate.
- Low passive proton permeability — label-only candidate.
- Archaeal bipolar tetraether membrane / GDGT / GDNT / tetraether-linked monolayer — label-only candidates pending lipid-specific identifier verification.
- Hopanoid-rich membrane; branched-chain fatty-acid-rich membrane; cyclopropanated membrane — label-only candidates.

### Genes, proteins, and transport modules

- Kdp system: `kdpA`, `kdpB`, `kdpC`, `kdpD`, `kdpE`.
- Trk-family and Kch potassium transporters; Kef-type K⁺ transport systems.
- Na⁺/H⁺ antiporters: `nhaA` and NhaP-type proteins.
- P-type ATPase proton-efflux pump — label-only unless a strain-specific accession is added.
- Chloride/proton antiporter `clcA`.
- Glutamate decarboxylase module: `gadA/gadB`, `gadC`.
- Arginine decarboxylase module: `speA`, `adi`.
- Urease module: `ureABCDEFGHJ` as reported in comparative genomes.
- Hopanoid synthesis: `hpnA`, `shc` and the broader `hpn` cluster.
- Cyclopropane-fatty-acyl-phospholipid synthase.
- Surface-layer/Slp proteins; Omp40; PspA.
- ClpXP/Clp protease quality-control module.

These gene symbols should not be assigned universal UniProt identifiers: accessions are strain-specific and must be added only after selecting a reference genome.

### Chemicals and metabolic modules

- Potassium ion — **CHEBI:29103**.
- Sodium ion — **CHEBI:29101**.
- Chloride — **CHEBI:17996**.
- L-glutamate — **CHEBI:29985**.
- L-arginine — **CHEBI:29016**.
- Spermidine — **CHEBI:16610**.
- Poly-γ-glutamate; hopanoids; sulfate-reduction module; respiratory proton export; cytoplasmic buffering — label-only candidates unless exact database mappings are verified during YAML preparation.

### Representative taxonomic contexts

Use strain-level NCBITaxon identifiers only after verifying the exact isolate. High-value contexts include *Acidithiobacillus ferrivorans* SS3/YL15, *Ferrovum* JA12, *Leptospirillum ferriphilum*, *Acidihalobacter* spp., *Sulfolobus solfataricus*, *Sulfolobus acidocaldarius*, *Picrophilus oshimae*, *Ferroplasma* spp., and acidophilic sulfate-reducing *Desulfosporosinus*, *Thermodesulfobium*, and *Acididesulfobacillus*.

## Candidate causal edges

The following compact table gives the proposed graph backbone. “Uncertain” means that the relationship is supported principally by comparative genomics, transcript abundance, or review synthesis and should not be represented as a universal direct mechanism.

| Subject | Predicate | Object | Evidence strength | Taxon/context | DOI |
|---|---|---|---|---|---|
| external pH <=4 | causes | steep transmembrane proton gradient | strong review synthesis (general acidophile physiology) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, mccarthy2016expandingthelimits pages 1-2) | acidophiles; thermoacidophilic archaea; acidophilic sulfate-reducing bacteria | 10.1111/1758-2229.70019; 10.1128/aem.03225-15 |
| tetraether lipid-rich membrane | decreases | passive proton permeability | strong experimental/review synthesis (chong2024archaeamembranesin pages 7-7, mccarthy2016expandingthelimits pages 1-2) | thermoacidophilic archaea including Sulfolobus/Picrophilus context | 10.3389/frbis.2023.1338019; 10.1128/aem.03225-15 |
| hopanoid synthesis / hopanoid-rich membrane | decreases | proton permeability | moderate; genomic plus review synthesis, uncertain for general curation (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9, vergara2020evolutionofpredicted pages 1-3, boase2022predictionandinferred pages 2-3) | Acidithiobacillus, Ferrovum, Leptospirillum, acidophilic sulfate reducers | 10.1111/1758-2229.70019; 10.3389/fmicb.2023.1149903; 10.3390/genes11040389; 10.3389/fmicb.2022.848410 |
| K+ uptake systems (kdp, trk, kch, Kef-type) | increases | inside-positive membrane potential | moderate; genomic/transcriptomic, uncertain (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, vergara2020evolutionofpredicted pages 1-3, boase2022predictionandinferred pages 1-2) | Acidithiobacillus ferrivorans, Ferrovum spp., Leptospirillum, Acidihalobacter | 10.3389/fmicb.2023.1149903; 10.3390/genes11040389; 10.3389/fmicb.2022.848410 |
| inside-positive membrane potential | decreases | proton influx | moderate review/genomic synthesis, uncertain (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, vergara2020evolutionofpredicted pages 1-3, boase2022predictionandinferred pages 2-3) | acidophilic sulfate reducers; Leptospirillum; Acidihalobacter | 10.1111/1758-2229.70019; 10.3390/genes11040389; 10.3389/fmicb.2022.848410 |
| P-type ATPase proton efflux pump | increases | proton efflux | moderate; genomic/transcriptomic, uncertain (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Acidithiobacillus ferrivorans SS3 | 10.3389/fmicb.2023.1149903 |
| Na+/H+ antiporter (nhaA / NhaP-type) | increases | proton efflux via cation exchange | moderate; genomic prediction/transcriptomic support, uncertain (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, vergara2020evolutionofpredicted pages 1-3, vergara2020evolutionofpredicted pages 16-17) | Acidithiobacillus ferrivorans, Leptospirillum | 10.3389/fmicb.2023.1149903; 10.3390/genes11040389 |
| glutamate decarboxylase system (gadABC / gadB / GadC) | consumes | cytoplasmic protons | moderate; genomic prediction, uncertain (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, boase2022predictionandinferred pages 1-2, vergara2020evolutionofpredicted pages 16-17) | Acidithiobacillus ferrivorans, Ferrovum, Acidihalobacter, Leptospirillum | 10.3389/fmicb.2023.1149903; 10.3389/fmicb.2022.848410; 10.3390/genes11040389 |
| arginine decarboxylase system (speA / adi) | consumes | cytoplasmic protons | moderate; genomic prediction, uncertain (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, boase2022predictionandinferred pages 1-2) | Acidithiobacillus ferrivorans, Acidihalobacter | 10.3389/fmicb.2023.1149903; 10.3389/fmicb.2022.848410 |
| dissimilatory sulfate reduction | consumes | protons | moderate review synthesis (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | acidophilic sulfate-reducing bacteria; AMD treatment systems | 10.1111/1758-2229.70019 |
| poly-gamma-glutamate / spermidine buffering systems | increases | cytoplasmic buffering capacity | moderate review synthesis, uncertain (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, vergara2020evolutionofpredicted pages 1-3) | acidophilic sulfate reducers; Leptospirillum prediction for spermidine | 10.1111/1758-2229.70019; 10.3390/genes11040389 |
| chloride stress / NaCl | decreases | cytoplasmic pH homeostasis | strong experimental for inhibitor boundary case (vergara2020evolutionofpredicted pages 1-3) | Leptospirillum ferriphilum exposed to NaCl; intracellular pH dropped from 6.7 to 5.5 | 10.3389/fmicb.2019.02455 |
| combined acid-homeostasis mechanisms | enables | growth at very low pH | strong review synthesis; mechanism bundle rather than single edge (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9, mccarthy2016expandingthelimits pages 1-2) | extreme acidophiles including aSRB, Acidithiobacillus, thermoacidophilic archaea | 10.1111/1758-2229.70019; 10.3389/fmicb.2023.1149903; 10.1128/aem.03225-15 |


*Table: This table lists concise candidate TraitMech edges for the microbial trait METPO:1000459, emphasizing mechanisms of pH homeostasis and clearly marking uncertain genomic-prediction or review-synthesis claims. It is useful as a starting edge set for curation into a causal graph.*

### Evidence snippets and curation notes

1. **Tetraether membrane → decreased proton permeability.** Supporting snippet: the 2024 review states that archaeal membrane adjustments allow “a low passive proton permeability and a near neutral intracellular pH” to be maintained. This is appropriate as a thermoacidophilic-archaea-specific edge, supported by model-membrane biophysics; do not generalize it to bacteria. Published January 2024. (chong2024archaeamembranesin pages 7-7)

2. **Hopanoid-rich envelope → decreased proton permeability.** Supporting synthesis: acidophilic sulfate reducers use “hopanoid lipids” and altered AEG/branched-chain lipids for proton exclusion; bacterial comparative studies also recover `hpnA`/`shc`. A prior deletion phenotype is summarized as impaired low-pH growth, but the retrieved evidence does not provide a strain-specific primary experiment. Curate as **moderate/uncertain**, preferably taxon-scoped. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9, vergara2020evolutionofpredicted pages 1-3)

3. **K⁺ uptake → inside-positive potential → reduced proton influx.** Supporting snippet: the Leptospirillum synthesis describes a “chemiosmotic barrier that inhibits positively charged protons from crossing the membrane.” Kch, Kdp, Trk, and Kef systems recur across acidophile genomes; K⁺ removal has been reported to lower acid resistance. The physical direction is well established, but individual transporter-to-trait assignments are often predicted. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, vergara2020evolutionofpredicted pages 1-3)

4. **P-type ATPase → increased proton efflux.** A P-type ATPase proton-efflux pump is reported in *A. ferrivorans* SS3. Because the retrieved support is genomic/transcriptomic rather than a targeted perturbation, curate with organism and evidence qualifiers. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

5. **NhaA/NhaP Na⁺/H⁺ antiporter → proton/cation exchange.** `nhaA` and NhaP-type systems occur in *A. ferrivorans* and *Leptospirillum*. Directionality as proton export is biologically plausible but can depend on electrochemical conditions; therefore avoid an unconditional universal “exports proton” edge. Prefer “participates in proton/cation homeostasis.” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, vergara2020evolutionofpredicted pages 16-17)

6. **Glutamate or arginine decarboxylation → cytoplasmic proton consumption.** `gadABC/gadB/GadC` and `speA/adi` are identified across *Acidithiobacillus*, *Ferrovum*, *Acidihalobacter*, and *Leptospirillum*. These systems are chemically capable of consuming protons, but the acidophile-specific trait link is primarily genome-based. Curate as uncertain and taxon-specific until mutant or flux evidence is attached. *S. solfataricus* explicitly lacks these decarboxylase systems, demonstrating that they are not universal. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, boase2022predictionandinferred pages 1-2, mccarthy2016expandingthelimits pages 1-2, vergara2020evolutionofpredicted pages 16-17)

7. **Sulfate reduction → proton consumption / local pH increase.** Acidophilic sulfate reducers couple low-pH persistence to proton-consuming sulfate reduction and sulfide production. This pathway is mechanistically and applicationally relevant, but it is restricted to the sulfate-reducing guild rather than a core acidophile mechanism. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

8. **Chloride stress → impaired pH homeostasis.** In *L. ferriphilum* exposed to NaCl, intracellular pH fell significantly from **6.7 to 5.5**, oxygen consumption and reactive oxygen species increased, and `kdpC/kdpD`, compatible-solute, peroxidase, and thioredoxin responses were induced. This is a useful inhibitory/context edge and illustrates that low-pH growth cannot be inferred independently of salinity. (vergara2020evolutionofpredicted pages 1-3)

9. **Combined homeostasis modules → very-low-pH growth.** Adaptive evolution of *S. solfataricus* produced a reported **178-fold increase in thermoacidophily** and growth at **pH 0.8 and 80°C after 29 passages**, accompanied by altered membrane biogenesis and energy/reductant programs. This strongly supports the trait as evolvable and multigenic, but it does not identify a single sufficient mutation or pathway. (mccarthy2016expandingthelimits pages 1-2)

## Recent developments, applications, and quantitative evidence

### 2023–2024 research

The 2023 synthesis of eurypsychrophilic acidophiles integrates genomes, metagenome-assembled genomes, and transcripts from acid mine drainage and treatment systems. It places `kdp`, Kef-type transporters, `nhaA`, P-type ATPases, hopanoid synthesis, cyclopropane-fatty-acid synthesis, amino-acid decarboxylases, urease, and Clp proteases into a low-pH/low-temperature adaptation framework. The authors emphasize that low-temperature and low-pH adaptations may be synergistic or antagonistic, so trait edges require environmental qualifiers. Published March 2023. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

A 2024 review expands attention beyond aerobic iron/sulfur oxidizers to anaerobic acidophilic sulfate reducers. It reports **seven isolated aSRB species**, all Firmicutes, with pH ranges spanning approximately **2.9–7.0**, and describes maintenance of internal pH around 6 during growth below external pH 3. The review also stresses that pure-culture mechanistic studies remain scarce. Published October 2024. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

The 2024 archaeal-membrane analysis identifies bipolar tetraether lipids as dominant in thermoacidophiles inhabiting **pH ≤4 and temperatures ≥65°C**, and links pH-dependent lipid remodeling to membrane packing, proton permeability, and preservation of protein activity. Published January 2024. (chong2024archaeamembranesin pages 7-7)

### Real-world implementations

- **Acid-mine-drainage treatment:** sulfate reducers produce sulfide that precipitates dissolved metals as metal sulfides while proton-consuming metabolism can mitigate acidity. Acidophilic *Thermodesulfobium* and *Desulfosporosinus* were enriched in pH **3.2–3.3** pit-lake microcosms and pH **2.5–3.5** AMD bioreactors; *Desulfosporosinus* exceeded **55% relative abundance** in one treatment context. Community abundance is implementation evidence, not proof that every detected cell grew at the minimum pH. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- **Biomining and low-temperature bioleaching:** *Acidithiobacillus*, *Ferrovum*, *Leptospirillum*, and chloride-tolerant *Acidihalobacter* oxidize iron or reduced sulfur compounds under acidic conditions, supporting metal dissolution. The Acidihalobacter analysis specifically connects its acid/chloride adaptations with copper bioleaching from chalcopyrite. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, boase2022predictionandinferred pages 1-2)
- **Process constraint:** chloride can collapse pH homeostasis and induce secondary oxidative stress, limiting the use of conventional acidophiles with saline water or chloride-bearing ores. The measured intracellular-pH decline from 6.7 to 5.5 provides a quantitative process-relevant phenotype. (vergara2020evolutionofpredicted pages 1-3)

## Recommended initial graph design

Use a small conserved physicochemical core:

`external pH ≤4 → steep proton gradient → increased proton-influx pressure → cytoplasmic acidification → reduced growth`

Add protective branches:

1. `low-permeability membrane → decreased passive proton influx`;
2. `K⁺ accumulation → inside-positive membrane potential → decreased proton influx`;
3. `proton/cation transport → restored cytoplasmic pH`;
4. `proton-consuming reactions/buffering → reduced cytoplasmic proton activity`;
5. `protein/DNA/oxidative-stress repair → reduced downstream damage`;
6. all branches jointly `enable → METPO:1000459`.

Represent bacterial hopanoids, archaeal tetraethers, individual antiporters, amino-acid decarboxylases, urease, and sulfate reduction as **taxon-specific implementations** of these general modules rather than mandatory universal nodes.

## Warnings: claims not yet ready for unqualified TraitMech curation

1. **Do not equate gene presence with phenotype.** Most `kdp`, `nhaA`, `gad`, `speA/adi`, urease, hopanoid, Slp, and porin claims are comparative-genomic predictions without gene deletion, complementation, or direct proton-flux measurements. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, boase2022predictionandinferred pages 1-2, vergara2020evolutionofpredicted pages 16-17)
2. **Do not make amino-acid decarboxylation universal.** *S. solfataricus* reaches extreme acid growth without these systems. (mccarthy2016expandingthelimits pages 1-2)
3. **Do not assert that every Na⁺/H⁺ antiporter exports protons under every condition.** Direction depends on ion gradients and membrane potential.
4. **Do not merge Donnan potential and all inside-positive membrane potentials without qualification.** The terminology is inconsistently applied across reviews, and direct measurements are sparse.
5. **Do not infer growth range from metagenomic detection, transcript detection, or community abundance alone.** These support ecological relevance, not the minimum growth pH of a taxon.
6. **Do not curate pH ≤4 as a strict natural-kind cutoff.** It is an operational boundary; the supplied definition correctly says “approximately 4.”
7. **Do not infer a direct edge from sulfate reduction to the general trait outside sulfate-reducing taxa.** It is a guild-specific proton-consuming metabolism.
8. **Do not assign unverified CURIEs.** Gene symbols require organism-specific UniProt/NCBI accessions; GDGT/GDNT, hopanoid classes, and assay states should remain label-only until checked against the target ontology release.

## DOI-first bibliography

1. Valdez-Nuñez LF, et al. **Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.** *Environmental Microbiology Reports*. Published October 2024. DOI: [10.1111/1758-2229.70019](https://doi.org/10.1111/1758-2229.70019). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
2. Chong PL-G. **Archaea membranes in response to extreme acidic environments.** *Frontiers in Biophysics*. Published January 2024. DOI: [10.3389/frbis.2023.1338019](https://doi.org/10.3389/frbis.2023.1338019). (chong2024archaeamembranesin pages 7-7)
3. Dopson M, González-Rosales C, Holmes DS, Mykytczuk N. **Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies.** *Frontiers in Microbiology*. Published March 2023. DOI: [10.3389/fmicb.2023.1149903](https://doi.org/10.3389/fmicb.2023.1149903). (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
4. Boase K, et al. **Prediction and inferred evolution of acid tolerance genes in the biotechnologically important Acidihalobacter genus.** *Frontiers in Microbiology*. Published April 2022. DOI: [10.3389/fmicb.2022.848410](https://doi.org/10.3389/fmicb.2022.848410). (boase2022predictionandinferred pages 1-2, boase2022predictionandinferred pages 2-3)
5. Vergara E, et al. **Evolution of predicted acid resistance mechanisms in the extremely acidophilic Leptospirillum genus.** *Genes*. Published April 2020. DOI: [10.3390/genes11040389](https://doi.org/10.3390/genes11040389). (vergara2020evolutionofpredicted pages 1-3, vergara2020evolutionofpredicted pages 16-17)
6. Rivera-Araya J, et al. **Osmotic imbalance, cytoplasm acidification and oxidative stress induction support the high toxicity of chloride in acidophilic bacteria.** *Frontiers in Microbiology*. Published October 2019. DOI: [10.3389/fmicb.2019.02455](https://doi.org/10.3389/fmicb.2019.02455). (vergara2020evolutionofpredicted pages 1-3)
7. McCarthy S, et al. **Expanding the limits of thermoacidophily in the archaeon Sulfolobus solfataricus by adaptive evolution.** *Applied and Environmental Microbiology*. Published February 2016. DOI: [10.1128/AEM.03225-15](https://doi.org/10.1128/AEM.03225-15). (mccarthy2016expandingthelimits pages 1-2)

**Curation priority:** begin with the physicochemical edges for low proton permeability and inside-positive potential, retain chloride as a contextual inhibitor, and add gene-level implementations only with explicit taxon and evidence-strength qualifiers.

References

1. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 18 citations and is from a peer-reviewed journal.

2. (vergara2020evolutionofpredicted pages 1-3): Eva Vergara, Gonzalo Neira, Carolina González, Diego Cortez, Mark Dopson, and David S. Holmes. Evolution of predicted acid resistance mechanisms in the extremely acidophilic leptospirillum genus. Genes, 11:389, Apr 2020. URL: https://doi.org/10.3390/genes11040389, doi:10.3390/genes11040389. This article has 40 citations.

3. (boase2022predictionandinferred pages 1-2): Katelyn Boase, Carolina González, Eva Vergara, Gonzalo Neira, David Holmes, and Elizabeth Watkin. Prediction and inferred evolution of acid tolerance genes in the biotechnologically important acidihalobacter genus. Frontiers in Microbiology, Apr 2022. URL: https://doi.org/10.3389/fmicb.2022.848410, doi:10.3389/fmicb.2022.848410. This article has 22 citations and is from a peer-reviewed journal.

4. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 22 citations and is from a peer-reviewed journal.

5. (mccarthy2016expandingthelimits pages 1-2): Samuel McCarthy, T. Johnson, Benjamin J. Pavlik, Sophie Payne, Wendy S. Schackwitz, Joel A. Martin, A. Lipzen, Erica C. Keffeler, and P. Blum. Expanding the limits of thermoacidophily in the archaeon sulfolobus solfataricus by adaptive evolution. Applied and Environmental Microbiology, 82:857-867, Feb 2016. URL: https://doi.org/10.1128/aem.03225-15, doi:10.1128/aem.03225-15. This article has 42 citations and is from a peer-reviewed journal.

6. (chong2024archaeamembranesin pages 7-7): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

7. (boase2022predictionandinferred pages 2-3): Katelyn Boase, Carolina González, Eva Vergara, Gonzalo Neira, David Holmes, and Elizabeth Watkin. Prediction and inferred evolution of acid tolerance genes in the biotechnologically important acidihalobacter genus. Frontiers in Microbiology, Apr 2022. URL: https://doi.org/10.3389/fmicb.2022.848410, doi:10.3389/fmicb.2022.848410. This article has 22 citations and is from a peer-reviewed journal.

8. (vergara2020evolutionofpredicted pages 16-17): Eva Vergara, Gonzalo Neira, Carolina González, Diego Cortez, Mark Dopson, and David S. Holmes. Evolution of predicted acid resistance mechanisms in the extremely acidophilic leptospirillum genus. Genes, 11:389, Apr 2020. URL: https://doi.org/10.3390/genes11040389, doi:10.3390/genes11040389. This article has 40 citations.