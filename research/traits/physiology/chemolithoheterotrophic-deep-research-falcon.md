---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:51:18.330998'
end_time: '2026-08-04T10:59:56.207857'
duration_seconds: 517.88
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemolithoheterotrophic
  trait_identifier: METPO:1000638
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemolithoheterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type characterized by the use of inorganic chemical compounds
    as electron donors for energy generation while utilizing organic compounds as
    the primary carbon source.
  parent_traits: METPO:1000631
  synonyms: chemolithoheterotroph
  evidence_summary: 'DOI:10.1038/s41598-021-81412-3: chemolithoheterotrophy (Experimental
    study supports chemolithoheterotrophy as Fe(II) oxidation for energy with glucose
    as carbon source.) | DOI:10.1128/mBio.01112-19: oxidize sulfur to fuel the uptake
    of organic compounds (Study supports sulfur oxidation coupled to organic compound
    uptake in a chemolithoheterotrophic symbiont context.)'
  causal_graph_summary: 'chemolithoheterotrophic_inorganic_energy_organic_carbon:
    16 nodes, 13 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 13
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemolithoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000638
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors for energy generation while utilizing organic compounds as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: chemolithoheterotrophy (Experimental study supports chemolithoheterotrophy as Fe(II) oxidation for energy with glucose as carbon source.) | DOI:10.1128/mBio.01112-19: oxidize sulfur to fuel the uptake of organic compounds (Study supports sulfur oxidation coupled to organic compound uptake in a chemolithoheterotrophic symbiont context.)
- **Existing causal graph summary:** chemolithoheterotrophic_inorganic_energy_organic_carbon: 16 nodes, 13 edges

## Research Objective

Research the microbial trait **chemolithoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithoheterotrophic.yaml`.

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
- **Trait label:** chemolithoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000638
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors for energy generation while utilizing organic compounds as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: chemolithoheterotrophy (Experimental study supports chemolithoheterotrophy as Fe(II) oxidation for energy with glucose as carbon source.) | DOI:10.1128/mBio.01112-19: oxidize sulfur to fuel the uptake of organic compounds (Study supports sulfur oxidation coupled to organic compound uptake in a chemolithoheterotrophic symbiont context.)
- **Existing causal graph summary:** chemolithoheterotrophic_inorganic_energy_organic_carbon: 16 nodes, 13 edges

## Research Objective

Research the microbial trait **chemolithoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithoheterotrophic.yaml`.

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


# Curation-focused research report: chemolithoheterotrophic

## 1. Trait record and scope

- **Trait label:** chemolithoheterotrophic
- **Trait identifier:** **METPO:1000638**
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** METPO:1000631
- **Synonym:** chemolithoheterotroph

### Operational definition

The trait describes a trophic strategy in which a microorganism obtains respiratory energy/electrons from oxidation of an **inorganic chemical donor**, while **organic compounds provide the primary assimilated carbon for biomass**. The strongest operational test therefore combines:

1. oxidation of an inorganic donor;
2. respiration or another demonstrated energy-conserving process;
3. uptake and assimilation of labeled organic carbon; and
4. absent or quantitatively negligible autotrophic CO2 assimilation.

*Arcobacter peruensis* provides a particularly strong assay-level example: it oxidized sulfide, completely reduced nitrate to N2, assimilated acetate, and showed negligible bicarbonate assimilation. Its genome also lacked canonical autotrophic CO2-fixation machinery (callbeck2019arcobacterperuensissp. pages 1-2, callbeck2019arcobacterperuensissp. pages 7-9, callbeck2019arcobacterperuensissp. pages 5-7).

### Boundaries with adjacent traits

| Nearby trait | Energy/electron source | Primary biomass carbon | Curation distinction |
|---|---|---|---|
| **Chemolithoheterotrophy** | Inorganic donor | Organic carbon | Target trait; require evidence that inorganic oxidation benefits energy metabolism and organics supply biomass carbon. |
| **Chemolithoautotrophy** | Inorganic donor | CO2/HCO3− | Exclude when canonical carbon fixation and substantial inorganic-carbon assimilation sustain biomass. |
| **Chemoorganoheterotrophy** | Organic donor | Organic carbon | Exclude if sulfur or Fe transformations are detoxification/incidental and do not contribute energy. |
| **Mixotrophy** | Often both inorganic and organic donors | Both inorganic and organic carbon | Do not automatically merge with this trait. A facultative organism can express chemolithoheterotrophy under one condition and mixotrophy under another. |
| **Lithoheterotrophic genomic potential** | Predicted inorganic oxidation | Predicted organic uptake | Treat as uncertain unless physiology, isotope incorporation, or condition-specific expression links both modules. |

The Kentron symbionts illustrate a genome-supported boundary: they possess sulfur-based energy metabolism but lack RuBisCO and key enzymes of the canonical autotrophic pathways. Their assignment is compelling but remains less direct than pure-culture isotope physiology because organic-carbon use was reconstructed from multi-omics rather than demonstrated in an isolated growth experiment (seah2019sulfuroxidizingsymbiontswithout pages 2-4).

## 2. Current evidence and recent developments

Trait-specific mechanistic evidence remains concentrated in well-resolved 2019 studies rather than in 2023–2024 publications. The recent literature retrieved for 2023–2024 largely concerned sulfur biotechnology, genomes, or autotrophic iron oxidation and did not provide stronger direct chemolithoheterotrophic physiology. Such sources should inform pathway context, not serve as primary evidence for this trait.

A notable post-2024 development is a 2025 *Nature Communications* study of estuarine nitrate-respiring heterotrophs. DNA stable-isotope probing indicated that sulfur oxidation can augment heterotrophic denitrification: sulfide addition increased organic-carbon assimilation by **64.1% in Azoarcus** and **8.0% in Pseudomonas**. The work also reported complete denitrification and reduced N2O release in organic-rich and organic-limited conditions. This broadens chemolithoheterotrophy from exceptional isolates to potentially important estuarine functional guilds, although these effects remain taxon- and incubation-specific (shao2025versatilenitraterespiringheterotrophs pages 1-2).

Groundwater microcosm work similarly suggests that reduced-sulfur oxidation can conserve organic substrates for biosynthesis. Fifteen sulfur-oxidizing MAGs encoded cytochrome-c oxidase and respiratory-chain functions, while twelve encoded nitrate-reduction enzymes. However, that work emphasized mixotrophic communities and did not isolate chemolithoheterotrophic growth in pure culture; those edges should remain provisional (taubert2021bolsteringfitnessvia pages 15-19).

## 3. Candidate causal-graph nodes

Identifiers below are supplied only where confidence is high. Labels are deliberately retained without CURIEs when database-specific verification was unavailable; this avoids inventing identifiers.

### Trait and taxa

- **METPO:1000638** — chemolithoheterotrophic
- *Arcobacter peruensis* PSE-93 / BCCM LMG-31510 — label-only taxon node pending current NCBITaxon verification
- “Candidatus Kentron” — label-only clade node
- *Kentrophoros* host ciliates — label-only taxon node
- sulfur-stimulated groundwater microbial community — community-level node, uncertain
- estuarine nitrate-respiring heterotrophs, including *Azoarcus* and *Pseudomonas* — taxon-specific 2025 extension

### Chemicals and nutrients

- sulfide / hydrogen sulfide — inorganic electron donor
- thiosulfate — inorganic electron donor
- elemental sulfur — inorganic electron donor/intermediate
- nitrate — terminal electron acceptor
- nitrite, nitric oxide, nitrous oxide — denitrification intermediates
- dinitrogen — denitrification product
- oxygen — terminal electron acceptor in microoxic respiration
- acetate — experimentally supported organic carbon source
- amino acids and organic acids — predicted Kentron carbon substrates
- bicarbonate/CO2 — assay substrate used to test and reject substantial autotrophic assimilation
- carbon monoxide and molecular hydrogen — candidate inorganic donors in some Kentron phylotypes; uncertain and taxon-restricted

### Genes, proteins, enzymes, and complexes

- **sqr** — sulfide:quinone oxidoreductase candidate
- **soxABCDXYZ** — Sox sulfur-oxidation system reported in *A. peruensis*
- reverse Dsr module — Kentron sulfur-oxidation module; individual gene grounding should be completed from the source genome annotation
- **napAB** — periplasmic nitrate reductase
- **nirS** — cytochrome-cd1 nitrite reductase
- **norBC** — nitric-oxide reductase
- **nosZ** — nitrous-oxide reductase
- acetate permease — reported high-affinity uptake function, **Km 5.4 μM**
- acetyl-CoA synthetase — acetate activation for assimilation
- cbb3-type cytochrome-c oxidase — microoxic terminal oxidase in Kentron
- F-type H+-transporting ATP synthase — energy-conserving complex
- respiratory electron-transport chain — process/module node
- RuBisCO — absent-marker node, not a positive mechanism
- canonical autotrophic CO2-fixation pathways — absent/unsupported module
- Ni-dependent carbon-monoxide dehydrogenase and Mvh [NiFe]-hydrogenase — uncertain Kentron phylotype-specific candidates

### Pathways and biological processes

- sulfide oxidation
- Sox-mediated sulfur oxidation
- reverse-Dsr sulfur oxidation
- complete denitrification
- aerobic/microoxic respiration
- proton-motive-force generation
- oxidative phosphorylation / ATP synthesis
- acetate transport
- acetate activation and assimilation
- organic-acid/amino-acid uptake
- biomass production from organic carbon
- autotrophic CO2 fixation — negative or boundary node

### Environments and experimental factors

- marine oxygen-minimum-zone redoxcline
- eutrophic, sulfidic coastal water
- marine sediment/ciliate ectosymbiosis
- microoxic condition
- anoxic nitrate-replete condition
- sulfide + nitrate + acetate medium
- isotope-labeled acetate and bicarbonate
- FISH–nanoSIMS and ^15N tracer assays
- genome and transcriptome completeness/coverage controls

## 4. Candidate causal edges

The following compact artifact captures the highest-priority graph core.

| candidate subject | predicate | object | representative taxon/system | evidence tier | key support |
|---|---|---|---|---|---|
| METPO:1000638 chemolithoheterotrophic | operationally defined by | inorganic sulfur oxidation for energy plus organic carbon assimilation for biomass, not canonical autotrophic CO2 fixation | Arcobacter peruensis PSE-93 | strong assay + genome | Grew best on sulfide + nitrate + acetate; isotope labeling verified acetate assimilation and no substantial CO2 fixation; genome lacked autotrophic CO2 fixation genes (callbeck2019arcobacterperuensissp. pages 1-2, callbeck2019arcobacterperuensissp. pages 5-7) |
| sulfide | is oxidized via | Sqr and Sox pathway (soxABCDXYZ) | Arcobacter peruensis PSE-93 | strong genome + physiology | Genome encoded sqr and soxABCDXYZ; physiology showed optimal activity with dissolved sulfide, including sulfide oxidation 6.6 ± 0.67 μM h⁻¹ under sulfide + nitrate + acetate conditions (callbeck2019arcobacterperuensissp. pages 7-9, callbeck2019arcobacterperuensissp. pages 5-7) |
| napAB/nirS/norBC/nosZ | enable | complete denitrification to N2 during sulfur-driven growth | Arcobacter peruensis PSE-93 | strong genome + isotope assay | Complete denitrification genes were identified, and isotope labeling verified complete nitrate reduction to N2 while coupling to sulfide oxidation (callbeck2019arcobacterperuensissp. pages 1-2, callbeck2019arcobacterperuensissp. pages 5-7) |
| acetate assimilation | supplies biomass carbon for | sulfur-driven chemolithoheterotrophic growth | Arcobacter peruensis PSE-93 | strong assay + genome | Growth was best on sulfide + nitrate + acetate; acetate assimilation measured at 1.55 ± 0.19 fmol C cell⁻¹ day⁻¹; organic carbon transporter capacity including acetate uptake was reported (callbeck2019arcobacterperuensissp. pages 9-12, callbeck2019arcobacterperuensissp. pages 5-7) |
| absence of canonical autotrophic CO2 fixation genes | supports classification as | chemolithoheterotrophic rather than chemolithoautotrophic | Arcobacter peruensis PSE-93 | strong genome + isotope assay | Rubisco/rTCA genes were absent, and single-cell measurements showed negligible CO2 assimilation (~0.03 ± 0.01 fmol CO2 cell⁻¹ day⁻¹) (callbeck2019arcobacterperuensissp. pages 7-9, callbeck2019arcobacterperuensissp. pages 5-7) |
| reduced sulfur compounds (thiosulfate, elemental sulfur, sulfide) | feed electrons into | hybrid Sox-reverse Dsr sulfur oxidation system | Kentron sulfur-oxidizing symbionts of Kentrophoros | strong genome/reconstruction | Seah et al. reconstructed a hybrid Sox-reverse Dsr pathway using reduced sulfur compounds as electron donors in a nonautotrophic sulfur symbiont clade (seah2019sulfuroxidizingsymbiontswithout pages 2-4) |
| electron transport chain / FoF1 ATP synthase / cbb3-type cytochrome c oxidase | couple sulfur oxidation to | respiratory energy conservation under microoxic conditions | Kentron sulfur-oxidizing symbionts of Kentrophoros | strong genome + transcript support | Kentron encoded a complete ETC and FoF1 ATP synthase; cbb3-type cytochrome c oxidase was the sole terminal oxygen reductase expressed under microoxic conditions (seah2019sulfuroxidizingsymbiontswithout pages 2-4) |
| absence of RuBisCO and other canonical autotrophic pathway genes | supports classification as | chemolithoheterotrophic with organic substrate dependence | Kentron sulfur-oxidizing symbionts of Kentrophoros | strong genome + transcript support | Metagenomic/transcriptomic analysis found no key genes for known autotrophic CO2 fixation pathways, while metabolic features were consistent with organic carbon uptake and heterotrophic growth (seah2019sulfuroxidizingsymbiontswithout pages 2-4) |
| sulfur oxidation potential plus organic carbon uptake | may support | chemolithoheterotrophic or mixotrophic fitness strategy | sulfur-stimulated groundwater mixotroph community | uncertain, community genomic/proteomic inference | Groundwater MAGs encoded sulfur oxidation and respiration functions and were interpreted as using reduced sulfur for energy while taking up organics, but evidence was community-level and not pure-culture trait confirmation (taubert2021bolsteringfitnessvia pages 15-19) |


*Table: This compact table summarizes candidate causal edges for METPO:1000638 centered on strongly supported sulfur-driven examples from Arcobacter peruensis and Kentron. It is useful for deciding which nodes and edges are ready for TraitMech curation versus which remain uncertain and community-inferred.*

### Expanded edge table with source snippets

| # | Subject — predicate — object | Supporting source snippet | Evidence and curation note |
|---|---|---|---|
| 1 | sulfide — **is oxidized by** — Sqr/Sox sulfur-oxidation machinery | “genes for … Sox pathway (soxAB-CDXYZ) and sulfide-quinone reductase (sqr)” | Strong for *A. peruensis*: genome plus measured sulfide oxidation. Curate as taxon-specific, not universal (callbeck2019arcobacterperuensissp. pages 5-7). |
| 2 | sulfide oxidation — **provides electrons to** — nitrate respiration | “optimal growth on sulfide+nitrate+acetate”; sulfide oxidation **6.60 ± 0.67 μM h−1** and nitrate reduction **6.20 ± 1.69 μM h−1** | Strong coupled-physiology edge in *A. peruensis* (callbeck2019arcobacterperuensissp. pages 7-9, callbeck2019arcobacterperuensissp. pages 5-7). |
| 3 | napAB/nirS/norBC/nosZ — **enable** — complete denitrification to N2 | “complete denitrification (napAB, nirS, norBC, nosZ)” and isotope labeling verified nitrate-to-N2 reduction | Strong gene-to-process edge supported by genome and ^15N assay (callbeck2019arcobacterperuensissp. pages 1-2, callbeck2019arcobacterperuensissp. pages 5-7). |
| 4 | acetate permease — **imports** — acetate | “high-affinity acetate permease (Km = 5.4 μM)” | Strong genomic functional candidate; direct transporter knockout evidence is absent (callbeck2019arcobacterperuensissp. pages 9-12). |
| 5 | acetyl-CoA synthetase — **activates** — acetate for assimilation | Acetate permease and acetyl-CoA synthetase were present; acetate was incorporated into cells | Strong pathway-consistent edge, but enzyme-specific causality was not genetically tested (callbeck2019arcobacterperuensissp. pages 9-12). |
| 6 | acetate assimilation — **supplies carbon to** — biomass production | acetate assimilation **1.55 ± 0.19 fmol C cell−1 day−1** | Strong single-cell isotope support under sulfide-oxidizing conditions (callbeck2019arcobacterperuensissp. pages 5-7). |
| 7 | sulfide oxidation — **increases** — chemolithoheterotrophic growth rate | doubling rates were approximately twofold lower without dissolved sulfide | Strong condition-comparison edge for *A. peruensis*; do not generalize across taxa (callbeck2019arcobacterperuensissp. pages 9-12). |
| 8 | sulfide + nitrate + acetate — **supports** — maximal *A. peruensis* growth | up to **4 × 10^6 cells mL−1** and **1.4–1.8 doublings day−1** | Strong assay-observed composite environmental factor (callbeck2019arcobacterperuensissp. pages 5-7). |
| 9 | absence of canonical CO2-fixation genes — **constrains** — chemolithoautotrophic growth | Rubisco/rTCA machinery absent; autotrophic cultures remained below **9 × 10^4 cells mL−1** | Strong boundary evidence, although absence should be represented as a constraint/negative evidence annotation rather than a biochemical reaction (callbeck2019arcobacterperuensissp. pages 5-7). |
| 10 | bicarbonate/CO2 — **is negligibly assimilated by** — *A. peruensis* | **0.03 ± 0.01 fmol CO2 cell−1 day−1**; less than 1% of environmental dark fixation despite 25% community abundance | Strong nanoSIMS evidence against meaningful autotrophy (callbeck2019arcobacterperuensissp. pages 7-9). |
| 11 | thiosulfate / elemental sulfur / sulfide — **are oxidized through** — hybrid Sox–reverse-Dsr pathway | Kentron had “a hybrid Sox-reverse Dsr pathway” capable of using these reduced sulfur compounds | Strong genomic reconstruction, but individual donor use was not established by isolated growth assays (seah2019sulfuroxidizingsymbiontswithout pages 2-4). |
| 12 | hybrid Sox–reverse-Dsr pathway — **feeds electrons into** — respiratory electron transport | Kentron encoded a complete electron-transport chain | Mechanistically well supported by genome reconstruction; direct flux remains inferred (seah2019sulfuroxidizingsymbiontswithout pages 2-4). |
| 13 | cbb3-type cytochrome-c oxidase — **reduces** — oxygen during microoxic respiration | it was the “sole terminal oxygen reductase expressed under microoxic conditions” | Strong genome/transcript evidence, specific to Kentron (seah2019sulfuroxidizingsymbiontswithout pages 2-4). |
| 14 | respiratory electron transport — **drives** — F-type ATP synthase-dependent energy conservation | complete electron-transport chain and FoF1 ATP synthase were encoded | Curatable as a pathway-level edge; proton-motive-force direction was mechanistically inferred rather than directly measured (seah2019sulfuroxidizingsymbiontswithout pages 2-4). |
| 15 | abundant organic-compound transporters — **support uptake of** — organic acids and amino acids | metabolic features were consistent with growth on “especially organic and amino acids,” with abundant uptake transporters | Moderate: genomic/transcriptomic support, but substrate-specific uptake assays were absent (seah2019sulfuroxidizingsymbiontswithout pages 2-4). |
| 16 | lack of canonical CO2-fixation pathways — **shifts primary carbon acquisition toward** — organic substrates | no RuBisCO or key enzymes of all six canonical fixation pathways | Strong negative genomic evidence; the causal wording should remain conservative because absence does not identify the actual imported carbon by itself (seah2019sulfuroxidizingsymbiontswithout pages 2-4). |
| 17 | sulfur oxidation — **increases** — organic-carbon assimilation by nitrate-respiring heterotrophs | sulfide increased labeled-organic-carbon assimilation by **64.1% in Azoarcus** and **8.0% in Pseudomonas** | Current 2025 experimental extension. Curate only with taxon, sediment-incubation, and condition qualifiers (shao2025versatilenitraterespiringheterotrophs pages 1-2). |
| 18 | sulfur-supported heterotrophic denitrification — **decreases** — N2O emissions | study reports complete denitrification with mitigation in organic-rich and organic-limited incubations | Application-relevant but community/assay-specific; do not encode as a universal trait consequence (shao2025versatilenitraterespiringheterotrophs pages 1-2). |
| 19 | reduced-sulfur oxidation potential — **may conserve** — organic carbon for biosynthesis | described as an opportunistic strategy in sulfur-stimulated groundwater communities | Uncertain: MAG/proteome-level community inference rather than pure-culture causal demonstration (taubert2021bolsteringfitnessvia pages 15-19). |

## 5. Quantitative evidence and ecological relevance

### *Arcobacter peruensis*

- *Arcobacter* constituted **3–25%** of the community in Peruvian coastal waters containing more than **20 μM sulfide**; abundance exceeded **10^6 cells mL−1** at the chemocline (callbeck2019arcobacterperuensissp. pages 1-2, callbeck2019arcobacterperuensissp. pages 2-5).
- Field denitrification reached **6.5 ± 0.4 μM N day−1** at the redoxcline, versus **0.9 ± 0.1 μM N day−1** in deeper sulfidic water. These are community rates and must not be assigned exclusively to *A. peruensis* (callbeck2019arcobacterperuensissp. pages 2-5).
- Dark carbon fixation was **2.8 ± 0.2 μM C day−1**, but nanoSIMS showed the abundant *Arcobacter* population contributed less than 1% of that fixation—an important demonstration that abundance of a sulfide oxidizer does not imply autotrophy (callbeck2019arcobacterperuensissp. pages 7-9, callbeck2019arcobacterperuensissp. pages 2-5).
- The genome was approximately **2.8 Mbp**, with **27.8% GC** and **2,697 genes** (callbeck2019arcobacterperuensissp. pages 2-5).

### Kentron symbionts

Kentron occurs as an ectosymbiont of *Kentrophoros* ciliates from Mediterranean, Caribbean, and Baltic marine sediments. The ciliate engulfs its ectosymbionts, making chemolithoheterotrophic sulfur oxidation part of a nutritional symbiosis rather than a free-living culture phenotype (seah2019sulfuroxidizingsymbiontswithout pages 2-4).

### Broader environmental implementation

The main real-world significance is ecological rather than commercial:

1. **Sulfide detoxification and fixed-nitrogen loss.** Sulfide oxidation coupled to complete denitrification can remove both toxic sulfide and bioavailable nitrogen in eutrophic, oxygen-depleted coastal waters (callbeck2019arcobacterperuensissp. pages 1-2, callbeck2019arcobacterperuensissp. pages 12-13).
2. **N2O mitigation potential.** The 2025 estuarine study suggests sulfur can help nitrate-respiring heterotrophs complete denitrification and curtail N2O accumulation. Translation to engineered reactors requires strain stability and rate/yield validation (shao2025versatilenitraterespiringheterotrophs pages 1-2).
3. **Symbiotic nutrition.** Kentron demonstrates that thiotrophic symbionts need not be primary producers; inorganic sulfur energy may instead support conversion of environmental organic matter into symbiont biomass consumed by the host (seah2019sulfuroxidizingsymbiontswithout pages 2-4).
4. **Groundwater carbon cycling.** Community data indicate that lithotrophic energy modules and organic uptake coexist broadly, but isotope-resolved flux and isolate studies are needed before assigning METPO:1000638 to individual MAGs (taubert2021bolsteringfitnessvia pages 15-19).

## 6. Recommended TraitMech graph architecture

A defensible initial YAML graph should be narrower than the biological definition and centered on the experimentally resolved sulfur/nitrate/acetate route:

**Core chain**

`sulfide → Sqr/Sox sulfur oxidation → respiratory electron transfer → complete denitrification → energy conservation → acetate uptake/activation → organic-carbon-derived biomass → METPO:1000638`

**Boundary branch**

`absence of canonical CO2-fixation machinery + negligible bicarbonate incorporation → excludes substantial chemolithoautotrophic carbon acquisition`

**Optional Kentron extension**

`reduced sulfur compounds → hybrid Sox/reverse-Dsr → electron-transport chain → cbb3 oxidase under microoxia → F-type ATP synthase`, accompanied by an uncertain organic-acid/amino-acid uptake branch.

The phenotype node should not be caused solely by `sqr`, `sox`, or `dsr` presence. It should require conjunction of an inorganic-energy branch and an organic-carbon assimilation branch, plus evidence that autotrophic fixation is absent, negligible, or not the principal carbon source.

## 7. Warnings: claims not yet ready for unqualified curation

1. **Seed DOI 10.1038/s41598-021-81412-3 was not recovered in usable full text in this search.** Its reported Fe(II)-plus-glucose phenotype should remain in existing evidence, but no new Fe(II)-specific gene or protein edge should be added from this report. In particular, do not assign Cyc2 or another Fe oxidase without checking the paper directly.
2. **Do not universalize sulfur machinery.** Sqr/Sox in *A. peruensis* and hybrid Sox/reverse-Dsr in Kentron are alternative, taxon-specific implementations—not defining components of every chemolithoheterotroph.
3. **Gene presence is insufficient.** Sulfur-oxidation genes plus organic transporters establish potential, not the expressed trait. MAG-only groundwater assignments should be annotated `uncertain` (taubert2021bolsteringfitnessvia pages 15-19).
4. **Absence of RuBisCO alone is insufficient.** All recognized autotrophic pathways must be assessed, and genome completeness must be adequate. Seah et al. explicitly evaluated key enzymes across canonical pathways, making that case unusually strong (seah2019sulfuroxidizingsymbiontswithout pages 2-4).
5. **Do not equate organic uptake with primary carbon supply.** Mixotrophs may assimilate both CO2 and organics. Quantitative isotope partitioning is needed to determine which source is primary.
6. **Do not assign field process rates to a single species.** The Peruvian denitrification and dark-carbon-fixation rates were community measurements even though *Arcobacter* was abundant (callbeck2019arcobacterperuensissp. pages 2-5).
7. **CO and H2 branches in Kentron are phylotype-specific genomic predictions.** They should remain uncertain until donor-dependent respiration or growth is measured (seah2019sulfuroxidizingsymbiontswithout pages 2-4).
8. **The N2O-mitigation edge is not constitutive.** It derives from 2025 estuarine enrichments and should carry taxon, substrate, and incubation qualifiers (shao2025versatilenitraterespiringheterotrophs pages 1-2).
9. **Recent-source limitation.** The retrieved 2023–2024 literature did not provide a direct replacement for the 2019 pure-culture and symbiont studies. Recency should not outweigh mechanistic specificity.

## 8. DOI-first bibliography

1. **Callbeck CM et al.** “*Arcobacter peruensis* sp. nov., a Chemolithoheterotroph Isolated from Sulfide- and Organic-Rich Coastal Waters off Peru.” *Applied and Environmental Microbiology*. **December 2019**. DOI: **10.1128/AEM.01344-19**. https://doi.org/10.1128/AEM.01344-19 (callbeck2019arcobacterperuensissp. pages 1-2, callbeck2019arcobacterperuensissp. pages 5-7)
2. **Seah BKB et al.** “Sulfur-Oxidizing Symbionts without Canonical Genes for Autotrophic CO2 Fixation.” *mBio*. **June 2019**. DOI: **10.1128/mBio.01112-19**. https://doi.org/10.1128/mBio.01112-19 (seah2019sulfuroxidizingsymbiontswithout pages 2-4)
3. **Taubert M et al.** “Bolstering fitness via CO2 fixation and organic carbon uptake: mixotrophs in modern groundwater.” *The ISME Journal*. Published online **December 2021**; volume issue 2022. DOI: **10.1038/s41396-021-01163-x**. https://doi.org/10.1038/s41396-021-01163-x. The retrieved detailed evidence also included its bioRxiv version, DOI **10.1101/2021.01.26.428071** (taubert2021bolsteringfitnessvia pages 15-19).
4. **Shao B et al.** “Versatile nitrate-respiring heterotrophs are previously concealed contributors to sulfur cycle.” *Nature Communications*. **January 2025**. DOI: **10.1038/s41467-025-56588-1**. https://doi.org/10.1038/s41467-025-56588-1 (shao2025versatilenitraterespiringheterotrophs pages 1-2)
5. **Existing but not independently re-extracted here:** DOI **10.1038/s41598-021-81412-3**. https://doi.org/10.1038/s41598-021-81412-3. Retain its Fe(II)-oxidation/glucose evidence provisionally, but verify full text before adding molecular edges.

References

1. (callbeck2019arcobacterperuensissp. pages 1-2): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 61 citations and is from a peer-reviewed journal.

2. (callbeck2019arcobacterperuensissp. pages 7-9): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 61 citations and is from a peer-reviewed journal.

3. (callbeck2019arcobacterperuensissp. pages 5-7): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 61 citations and is from a peer-reviewed journal.

4. (seah2019sulfuroxidizingsymbiontswithout pages 2-4): Brandon K. B. Seah, Chakkiath Paul Antony, Bruno Huettel, Jan Zarzycki, Lennart Schada von Borzyskowski, Tobias J. Erb, Angela Kouris, Manuel Kleiner, Manuel Liebeke, Nicole Dubilier, and Harald R. Gruber-Vodicka. Sulfur-oxidizing symbionts without canonical genes for autotrophic co <sub>2</sub> fixation. mBio, Jun 2019. URL: https://doi.org/10.1128/mbio.01112-19, doi:10.1128/mbio.01112-19. This article has 34 citations and is from a domain leading peer-reviewed journal.

5. (shao2025versatilenitraterespiringheterotrophs pages 1-2): Bo Shao, Yuan-Guo Xie, Long Zhang, Yang Ruan, Bin Liang, Ruochen Zhang, Xijun Xu, Wei Wang, Zhengda Lin, Xuanyuan Pei, Xueting Wang, Lei Zhao, Xu Zhou, Xiaohui Wu, Defeng Xing, Aijie Wang, Duu-Jong Lee, Nanqi Ren, Donald E. Canfield, Brian P. Hedlund, Zheng-Shuang Hua, and Chuan Chen. Versatile nitrate-respiring heterotrophs are previously concealed contributors to sulfur cycle. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56588-1, doi:10.1038/s41467-025-56588-1. This article has 33 citations and is from a highest quality peer-reviewed journal.

6. (taubert2021bolsteringfitnessvia pages 15-19): Martin Taubert, Will A. Overholt, Beatrix M. Heinze, Georgette Azemtsop Matanfack, Rola Houhou, Nico Jehmlich, Martin von Bergen, Petra Rösch, Jürgen Popp, and Kirsten Küsel. Bolstering fitness via opportunistic co2 fixation: mixotroph dominance in modern groundwater. bioRxiv, Jan 2021. URL: https://doi.org/10.1101/2021.01.26.428071, doi:10.1101/2021.01.26.428071. This article has 4 citations.

7. (callbeck2019arcobacterperuensissp. pages 9-12): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 61 citations and is from a peer-reviewed journal.

8. (callbeck2019arcobacterperuensissp. pages 2-5): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 61 citations and is from a peer-reviewed journal.

9. (callbeck2019arcobacterperuensissp. pages 12-13): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 61 citations and is from a peer-reviewed journal.