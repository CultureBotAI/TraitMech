---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:54:49.333161'
end_time: '2026-06-18T11:13:39.451961'
duration_seconds: 1130.12
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
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
    10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemolithoheterotrophic
- **METPO identifier:** METPO:1000638
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors for energy generation while utilizing organic compounds as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: chemolithoheterotrophy (Experimental study supports chemolithoheterotrophy as Fe(II) oxidation for energy with glucose as carbon source.) | DOI:10.1128/mBio.01112-19: oxidize sulfur to fuel the uptake of organic compounds (Study supports sulfur oxidation coupled to organic compound uptake in a chemolithoheterotrophic symbiont context.)
- **Existing causal graph summary:** chemolithoheterotrophic_inorganic_energy_organic_carbon: 10 nodes, 9 edges

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
- **METPO identifier:** METPO:1000638
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of inorganic chemical compounds as electron donors for energy generation while utilizing organic compounds as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: chemolithoheterotrophy (Experimental study supports chemolithoheterotrophy as Fe(II) oxidation for energy with glucose as carbon source.) | DOI:10.1128/mBio.01112-19: oxidize sulfur to fuel the uptake of organic compounds (Study supports sulfur oxidation coupled to organic compound uptake in a chemolithoheterotrophic symbiont context.)
- **Existing causal graph summary:** chemolithoheterotrophic_inorganic_energy_organic_carbon: 10 nodes, 9 edges

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


## Chemolithoheterotrophic (METPO:1000638) – curation-focused research report

### 1) Scope summary (trait meaning, boundaries)

**Trait definition (curation target).** *Chemolithoheterotrophic* refers to organisms that conserve energy by oxidizing **inorganic** electron donors (chemolithotrophy) while relying on **organic carbon** as the primary carbon source for biomass (heterotrophy). In sulfur-oxidizing contexts, an operational definition used in recent work is that chemolithoheterotrophic sulfur oxidizers “use both reduced sulfur compounds and organic carbon as energy sources but require organic carbon for biosynthesis” (quinn2025characterizingstratifiedmicrobiala pages 20-23).

**Distinguish from nearby trophic modes (boundary cases).**
- **Chemolithoautotrophy:** energy from inorganic donors *and* carbon from CO2 fixation. In thiotrophic symbioses, some symbionts show genomic hallmarks of obligate autotrophy, e.g., “lack of organic uptake transporters” (seah2019sulfuroxidizingsymbiontswithout pages 10-12).
- **Mixotrophy:** simultaneous assimilation of **CO2 and organic carbon**. In groundwater microcosms, mixotrophs were defined as organisms “able to assimilate 13CO2 alongside organic carbon” (taubert2022bolsteringfitnessvia pages 5-6).
- **Lithoheterotrophy vs chemolithoheterotrophy:** Seah et al. use “lithoheterotrophy” for Kentron-like thiotrophs that gain energy from reduced inorganic compounds while assimilating organics (conceptually overlapping chemolithoheterotrophy) and note it is “more prevalent among those that have the Sox pathway” (seah2019sulfuroxidizingsymbiontswithout pages 10-12).
- **Exochemolithoheterotrophy (auxiliary lithotrophy):** an experimentally tractable boundary case where a heterotroph oxidizes an *auxiliary* inorganic electron donor (e.g., thiosulfate) during growth on an organic carbon substrate; defined as “an organic carbon compound supplies carbon, electrons and energy” while an “inorganic species… is simultaneously oxidized as an auxiliary electron donor” to generate Δp for ATP synthesis (hutt2021insightsintogrowth pages 1-6).

**Practical curation boundary conditions.** For TraitMech, evidence should ideally show:
1) an inorganic electron donor is oxidized to support energy conservation; 2) organic carbon assimilation supports biomass; and 3) autotrophic CO2 fixation is absent or quantitatively minor under the tested conditions. The Arcobacter peruensis case provides this “gold-standard” combination via genome content, cultivation, isotope labeling, and single-cell nanoSIMS (callbeck2019arcobacterperuensissp. pages 1-2, callbeck2019arcobacterperuensissp. pages 9-12, callbeck2019arcobacterperuensissp. media 126dcd32, callbeck2019arcobacterperuensissp. media 672097f5, callbeck2019arcobacterperuensissp. media 6db03913).

### 2) Key concepts & mechanistic entities (candidate nodes)

Below, nodes are grouped for curation; suggested groundings are given when stable identifiers are clear.

#### 2.1 Chemicals / nutrients / electron donors & acceptors
- **Electron donors (examples):** sulfide (CHEBI:18421), thiosulfate (CHEBI:30087), Fe(II) (CHEBI:29033), H2 (CHEBI:18276; implied as possible donor in SOB contexts) (seah2019sulfuroxidizingsymbiontswithout pages 10-12, zhong2022metagenomicfeaturescharacterized pages 10-13).
- **Electron acceptors (examples):** oxygen (CHEBI:15379), nitrate (CHEBI:17632), nitrite (CHEBI:16301), Fe(III) (CHEBI:29034) (seah2019sulfuroxidizingsymbiontswithout pages 10-12, taubert2022bolsteringfitnessvia pages 5-6, zhong2022metagenomicfeaturescharacterized pages 10-13).
- **Carbon sources:** acetate (CHEBI:30089), other organic acids (succinate CHEBI:30031), dissolved organic matter pools (label-only) (seah2019sulfuroxidizingsymbiontswithout pages 10-12, callbeck2019arcobacterperuensissp. pages 9-12).
- **Storage / intermediates:** elemental sulfur (CHEBI:26806), sulfate (CHEBI:16189), tetrathionate (CHEBI:30926), polyhydroxyalkanoates (PHA; label-only) (seah2019sulfuroxidizingsymbiontswithout pages 10-12, trutschel2023determiningresidentmicrobial pages 10-11, rudenko2024mechanismofintracellular pages 10-12).

#### 2.2 Pathways / modules / processes
- **Sulfur oxidation:** Sox system (soxCDYZAXB; SoxXYZABCD; label-only/KEGG), Sqr-mediated sulfide oxidation (label-only), SoeABC (quinone sulfite dehydrogenase; label-only), rDsr (reverse dsrABEFH… operon; label-only), AprAB (APS reductase; EC/label), Sat (ATP sulfurylase; EC/label), TsdA (thiosulfate dehydrogenase; EC 1.8.2.2) (taubert2022bolsteringfitnessvia pages 5-6, trutschel2023determiningresidentmicrobial pages 10-11, rudenko2024mechanismofintracellular pages 10-12).
- **Denitrification / nitrate reduction:** “complete denitrification” to N2 in Arcobacter peruensis (process: GO:0055114 / nitrate reduction GO:0042128; label-only gene set in context) (callbeck2019arcobacterperuensissp. pages 9-12).
- **Iron oxidation (candidate):** Cyc2 homologs proposed to function as Fe(II) oxidases/electron transporters (label-only) (zhong2022metagenomicfeaturescharacterized pages 10-13).
- **Organic carbon uptake / assimilation:** organic uptake transporters (label-only); acetate permease (label-only); acetyl-CoA synthetase (EC 6.2.1.1) producing acetyl-CoA (CHEBI:15351) (seah2019sulfuroxidizingsymbiontswithout pages 10-12, callbeck2019arcobacterperuensissp. pages 9-12).

#### 2.3 Genes / enzymes / complexes (examples from evidence)
- **Sqr** (sulfide:quinone oxidoreductase; label-only) (trutschel2023determiningresidentmicrobial pages 10-11, rudenko2024mechanismofintracellular pages 10-12).
- **SoxXYZABCD** and/or **soxCDYZAXB** conserved gene order (label-only) (taubert2022bolsteringfitnessvia pages 5-6, trutschel2023determiningresidentmicrobial pages 10-11).
- **TsdA** (thiosulfate dehydrogenase; EC 1.8.2.2) + **SoxZ** (carrier protein; label-only) (trutschel2023determiningresidentmicrobial pages 10-11).
- **SoeABC** (label-only) (trutschel2023determiningresidentmicrobial pages 10-11).
- **PDO (persulfide dioxygenase)** (EC not resolved in provided text; label-only) proposed in endogenous sulfur oxidation in *Beggiatoa leptomitoformis* (rudenko2024mechanismofintracellular pages 10-12).
- **Cyc2** (outer-membrane Fe(II) oxidation candidate; label-only) (zhong2022metagenomicfeaturescharacterized pages 10-13).

#### 2.4 Environmental / experimental context (candidate nodes)
- **Redox structure:** oxic vs anoxic sediment zones; microoxia (e.g., cbb3-type oxidase in Kentron, indicating microoxic respiration) (seah2019sulfuroxidizingsymbiontswithout pages 10-12, seah2019sulfuroxidizingsymbiontswithout pages 2-4).
- **Geochemical drivers:** high sulfide availability (e.g., Ney Springs 430–700 mg/L sulfide) (trutschel2023determiningresidentmicrobial pages 10-11).
- **Mineral drivers:** pyrrhotite supplying Fe(II)/Fe(III) and promoting FeOB diversity (zhong2022metagenomicfeaturescharacterized pages 10-13).

#### 2.5 Assays / evidence types (for curation provenance)
- **Stable isotope labeling:** 15N labeling for denitrification; 13C labeling for carbon source assimilation.
- **nanoSIMS single-cell assimilation:** used to quantify low CO2 fixation vs acetate assimilation in Arcobacter; also sulfur content comparisons (callbeck2019arcobacterperuensissp. pages 9-12).
- **Genome-resolved SIP-metaproteomics / SIsCA:** quantifies contributions of mixotrophs vs strict autotrophs in groundwater microcosms (taubert2022bolsteringfitnessvia pages 5-6).

### 3) Recent developments (prioritizing 2023–2024)

**2023: genome-resolved sulfur-oxidation potential in serpentinizing springs.** Core community MAGs in Ney Springs include sulfur oxidation genes spanning Sqr, Sox operon components, SoeABC, and TsdA, with specific MAG-level predictions (e.g., “contains Sqr… along with SoxXYZABCD… predicted to oxidize sulfur species completely to sulfate”) and high measured sulfide at the site (430–700 mg/L) (trutschel2023determiningresidentmicrobial pages 10-11). This expands the set of environments where chemolithotrophy/chemolithoheterotrophy-related gene modules are plausibly important outside classic marine OMZ settings.

**2024: mechanistic insight into endogenous elemental sulfur oxidation.** Rudenko et al. propose a Beggiatoa mechanism where sulfane sulfur is processed via **SQR → PDO → sulfite**, with chemical thiosulfate formation and periplasmic branched Sox oxidation, explicitly noting this is energy-generating with thiosulfate as an electron donor (rudenko2024mechanismofintracellular pages 10-12). This provides concrete candidate nodes (PDO, unknown thiosulfate transport) and intermediate metabolites (sulfite, thiosulfate, sulfate) relevant to sulfur-based chemolithotrophic energy conservation.

**2024: broader electron-transfer framing for sulfur cycle organisms (applications-adjacent).** A 2024 review highlights roles of extracellular electron transfer (EET) components (e.g., cytochromes/pili) in sulfur-cycling consortia and situates chemolithoheterotrophs among sulfur oxidizers (zhuang2024electrontransferin pages 5-6). While not specific to chemolithoheterotrophy, it supports including EET-related nodes when chemolithoheterotrophy occurs in mineral-associated or syntrophic contexts.

### 4) Current applications & real-world implementations (evidence-supported)

**Biogeochemical cycling in productive, sulfidic coastal waters (OMZ shelves).** *Arcobacter peruensis* exemplifies how chemolithoheterotrophy can couple **sulfide oxidation** with **denitrification**, impacting sulfur and fixed nitrogen loss processes in sulfidic, organic-rich coastal waters (callbeck2019arcobacterperuensissp. pages 2-5, callbeck2019arcobacterperuensissp. pages 9-12).

**Geology-driven ecosystems: serpentinizing springs and hydrothermal vents.** Genomic evidence indicates that mineral context and sulfur intermediates shape microbial metabolism; for vents, pyrrhotite may supply iron that supports iron oxidation potentials and feedbacks between mineral dissolution and microbial iron/sulfur transformations (zhong2022metagenomicfeaturescharacterized pages 10-13). In serpentinizing springs, community shifts correlate with sulfur species and MAGs encoding sulfur oxidation modules (trutschel2023determiningresidentmicrobial pages 10-11).

**Potential “electroactive” implications (emerging, indirect).** Long-distance electron transfer and extracellular cytochromes/pili in sulfur cycling have “application prospects” in “bioelectronics materials and bioremediation technologies” (review-level claim) (zhuang2024electrontransferin pages 5-6). This is not a direct chemolithoheterotrophy implementation, but suggests a plausible applied adjacency when chemolithoheterotrophs participate in EET-enabled sulfur transformations.

### 5) Data, statistics, and quantitative constraints from studies

**Arcobacter in situ abundance and activity constraints.** In Peruvian sulfidic waters, Arcobacter populations were reported as a large fraction of the community (3–25%) at a near-shore station where sulfide exceeded 20 μM (callbeck2019arcobacterperuensissp. pages 2-5). Single-cell nanoSIMS-based CO2 assimilation by Arcobacter was too low to sustain observed densities if autotrophic, consistent with chemolithoheterotrophy (callbeck2019arcobacterperuensissp. pages 9-12). The Arcobacter strain’s acetate assimilation factor was calculated as **3.1 mol C per mol H2S oxidized**, exceeding reported ranges for chemolithoautotrophic sulfide oxidizers (0.35–0.58 mol C per mol H2S oxidized) (callbeck2019arcobacterperuensissp. pages 9-12).

**Energy economics of organic assimilation vs autotrophy (expert analysis in primary paper).** Callbeck et al. argue that for pyruvate biosynthesis, autotrophic CO2 fixation requires ~0.6–2.3 mol ATP/mol pyruvate, while acetate assimilation requires ~0.5 mol ATP/mol pyruvate, implying an energetic advantage for chemolithoheterotrophy in organic-rich settings (callbeck2019arcobacterperuensissp. pages 9-12).

**Groundwater SIP-metaproteomics: mixotrophy vs strict autotrophy (comparative boundary).** In sulfur-stimulated groundwater microcosms, **43%, 68%, and 80%** of total microbial carbon was replaced with 13C after 21, 43, and 70 days, respectively; mixotrophs comprised **>50%** of active organisms, while strict chemolithoautotrophs were **~3%** (taubert2022bolsteringfitnessvia pages 5-6). This provides a quantitative comparator for separating chemolithoheterotrophy from mixotrophy in trait models.

**Serpentinizing spring geochemistry (contextual statistic).** Ney Springs sulfide (430–700 mg/L) is orders of magnitude higher than the Lost City marine serpentinizing system (2–32 mg/L), creating strong selective pressure for sulfur oxidation modules (trutschel2023determiningresidentmicrobial pages 10-11).

**Beggiatoa sulfur storage magnitude and expression dynamics.** Intracellular sulfur can reach **up to 70% of cell dry weight** (literature-backed statement within the 2024 Beggiatoa study), and Sox gene expression increased strongly under endogenous-sulfur conditions (e.g., soxAX/soxB ~15-fold; soxY ~8.6-fold) (rudenko2024mechanismofintracellular pages 10-12).

### 6) Candidate causal edges for TraitMech curation

The following table provides curation-ready triples with direct evidence snippets, references, and uncertainty notes.

| Edge (triple) | Node type(s) | Suggested ontology grounding | Evidence snippet | Reference | Notes/uncertainty |
|---|---|---|---|---|---|
| sulfide oxidation pathway — fuels → chemolithoheterotrophic growth in *Arcobacter peruensis* | pathway/chemical/trait/taxon | pathway: label-only; sulfide: CHEBI:18421; trait: METPO:1000638; taxon: *Arcobacter peruensis* (label-only) | “A. peruensis grows best by coupling dissimilatory nitrate reduction to dinitrogen with the oxidation of dissolved sulfide” (callbeck2019arcobacterperuensissp. pages 9-12) | DOI:10.1128/AEM.01344-19 (2019) https://doi.org/10.1128/AEM.01344-19 | Strong experimental support; taxon-specific exemplar rather than universal rule. |
| complete denitrification pathway — enables → nitrate reduction to dinitrogen in *A. peruensis* | pathway/chemical/taxon | denitrification: GO:0055114; nitrate: CHEBI:17632; dinitrogen: CHEBI:17997; taxon: label-only | “The genes for a complete denitrification pathway are present in the genome of A. peruensis, and the presence of this pathway was confirmed by the 15N labeling experiments.” (callbeck2019arcobacterperuensissp. pages 9-12) | DOI:10.1128/AEM.01344-19 (2019) https://doi.org/10.1128/AEM.01344-19 | Strong; combines genomics with isotope validation. |
| sulfide + nitrate + acetate availability — promotes → best growth of *A. peruensis* | chemical/environment/assay/taxon | sulfide: CHEBI:18421; nitrate: CHEBI:17632; acetate: CHEBI:30089; environment: label-only | “A. peruensis grew best on a mix of sulfide, nitrate, and acetate.” (callbeck2019arcobacterperuensissp. pages 1-2) | DOI:10.1128/AEM.01344-19 (2019) https://doi.org/10.1128/AEM.01344-19 | Strong cultivation evidence; condition-specific. |
| high-affinity acetate permease + acetyl-CoA synthetase — enables → acetate assimilation | transporter/enzyme/chemical/process | acetate permease: label-only; acetyl-CoA synthetase: EC 6.2.1.1; acetate: CHEBI:30089; acetyl-CoA: CHEBI:15351 | “A. peruensis could assimilate acetate by converting it to acetyl-CoA using the combination of the high-affinity acetate permease… and the acetyl-CoA synthetase” (callbeck2019arcobacterperuensissp. pages 9-12) | DOI:10.1128/AEM.01344-19 (2019) https://doi.org/10.1128/AEM.01344-19 | Strong for acetate assimilation in *A. peruensis*; transporter identifier not grounded here. |
| organic uptake transporters — indicate → heterotrophic assimilation in Kentron | transporter/process/taxon | organic uptake transporter: label-only; heterotrophic assimilation: label-only; taxon: “Ca. Kentron” (label-only) | “abundant presence and expression of organic uptake transporters… are a clearer marker of heterotrophic assimilation” (seah2019sulfuroxidizingsymbiontswithout pages 10-12) | DOI:10.1128/mBio.01112-19 (2019) https://doi.org/10.1128/mBio.01112-19 | Strong for Kentron; broader applicability inferred. |
| sulfide + organic acids in anoxic sediment — provide → energy and carbon sources for Kentron | chemical/environment/process/taxon | sulfide: CHEBI:18421; acetate: CHEBI:30089; succinate: CHEBI:30031; anoxic sediment: ENVO: label-only | “In anoxic sediment, both the predicted energy and carbon sources, namely, sulfide and organic acids, are produced by microbial activity” (seah2019sulfuroxidizingsymbiontswithout pages 10-12) | DOI:10.1128/mBio.01112-19 (2019) https://doi.org/10.1128/mBio.01112-19 | Mechanistic ecological model; not directly perturbed experimentally. |
| incomplete sulfide oxidation under anoxia — produces → elemental sulfur intermediate | process/chemical/environment | elemental sulfur: CHEBI:26806; sulfate: CHEBI:16189; oxygen: CHEBI:15379 | “Complete oxidation of sulfide to sulfate requires oxygen, so elemental sulfur would be the intermediate” (seah2019sulfuroxidizingsymbiontswithout pages 10-12) | DOI:10.1128/mBio.01112-19 (2019) https://doi.org/10.1128/mBio.01112-19 | Strong conceptual support in Kentron model; may be system-dependent. |
| PHA synthesis from small organic acids — functions as → electron sink for sulfide oxidation and carbon store | storage compound/process/chemical | polyhydroxyalkanoate (PHA): label-only; acetate: CHEBI:30089 | “The synthesis of PHA from small organic acids like acetate can also function as both an additional electron sink for sulfide oxidation and a carbon store.” (seah2019sulfuroxidizingsymbiontswithout pages 10-12) | DOI:10.1128/mBio.01112-19 (2019) https://doi.org/10.1128/mBio.01112-19 | Useful candidate edge, but from an ecophysiological model; curate as uncertain. |
| oxic conditions — enable → oxidation of elemental sulfur to sulfate | environment/process/chemical | oxygen: CHEBI:15379; elemental sulfur: CHEBI:26806; sulfate: CHEBI:16189 | “Under oxic conditions, elemental sulfur can be further oxidized to sulfate for energy” (seah2019sulfuroxidizingsymbiontswithout pages 10-12) | DOI:10.1128/mBio.01112-19 (2019) https://doi.org/10.1128/mBio.01112-19 | Strong for Kentron model; environmental trigger edge. |
| Sox pathway — is more prevalent in → free-living lithoheterotrophs than rDsr/Sox pathway carriers | pathway/trait | Sox pathway: KEGG label-only; rDsr/Sox pathway: label-only; trait: METPO:1000638 | “Lithoheterotrophy is not uncommon for free-living thiotrophs and appears to be more prevalent among those that have the Sox pathway” (seah2019sulfuroxidizingsymbiontswithout pages 10-12) | DOI:10.1128/mBio.01112-19 (2019) https://doi.org/10.1128/mBio.01112-19 | Comparative statement; broad but not directly causal in one organism. |
| Cyc2 homolog — may enable → Fe(II) oxidation for energy conservation | gene/protein/chemical/process | Cyc2: label-only; Fe(II): CHEBI:29033 | “it is theoretically possible that these protein products function as an iron oxidases… allowing them to access additional electron donors such as Fe(II) for energy conservation” (zhong2022metagenomicfeaturescharacterized pages 10-13) | DOI:10.1128/spectrum.00614-22 (2022) https://doi.org/10.1128/spectrum.00614-22 | Genomic inference only; authors explicitly urge caution. |
| Cyc2-containing heterotrophic MAGs lacking carbon fixation pathways — support → candidate chemolithoheterotrophic Fe oxidizers | gene/pathway/trait/taxon | Cyc2: label-only; carbon fixation pathway: GO:0015977; trait: METPO:1000638 | “The majority of novel Cyc2-like sequences were found in putative heterotrophic bacterial groups… absent of carbon fixation pathways.” (zhong2022metagenomicfeaturescharacterized pages 10-13) | DOI:10.1128/spectrum.00614-22 (2022) https://doi.org/10.1128/spectrum.00614-22 | Candidate-only; metagenomic prediction, not cultured validation. |
| nitrate/nitrite reduction genes in Cyc2 MAGs — suggest → nitrate as electron acceptor for microbial iron oxidation | gene/pathway/chemical/process | nitrate: CHEBI:17632; nitrite: CHEBI:16301; nitrate reduction: GO:0042128 | “genes involved in nitrate or nitrite reduction were also carried by these MAGs, suggesting that nitrate may serve as electron acceptors for microbial iron oxidation” (zhong2022metagenomicfeaturescharacterized pages 10-13) | DOI:10.1128/spectrum.00614-22 (2022) https://doi.org/10.1128/spectrum.00614-22 | Inferred, not directly measured. |
| pyrrhotite-derived Fe(II)/Fe(III) supply — enhances → growth of diverse FeOBs | mineral/environment/chemical/process | pyrrhotite: label-only; Fe(II): CHEBI:29033; Fe(III): CHEBI:29034; FeOB: label-only | “the augment of Fe(II) and Fe(III) supplied from pyrrhotite enhanced the growth of more diverse FeOBs” (zhong2022metagenomicfeaturescharacterized pages 10-13) | DOI:10.1128/spectrum.00614-22 (2022) https://doi.org/10.1128/spectrum.00614-22 | Environmental/mineral trigger; vent-specific inference. |
| Rhodobacteraceae core MAGs with Sqr + SoeABC + partial Sox — have potential to → oxidize sulfur species | gene/pathway/process/taxon | Sqr: label-only; SoeABC: label-only; Sox: label-only; sulfate: CHEBI:16189 | “MAGs classified as Rhodobacteraceae all contain Sqr, have varying degrees of completeness of the Sox sulfur oxidation pathway, and all contain a complete or almost complete SoeABC” (trutschel2023determiningresidentmicrobial pages 10-11) | DOI:10.3389/fmicb.2023.1182497 (2023) https://doi.org/10.3389/fmicb.2023.1182497 | Genomic potential; sulfur oxidation not directly measured for each MAG. |
| Thiomicrospira/Thioalkalimicrobium MAG with Sqr + SoxXYZABCD — predicts → complete oxidation of sulfur species to sulfate | gene/pathway/process/taxon | Sqr: label-only; SoxXYZABCD: label-only; sulfate: CHEBI:16189 | “contains Sqr… along with SoxXYZABCD… and is predicted to oxidize sulfur species completely to sulfate” (trutschel2023determiningresidentmicrobial pages 10-11) | DOI:10.3389/fmicb.2023.1182497 (2023) https://doi.org/10.3389/fmicb.2023.1182497 | Predicted from MAG; needs physiological validation. |
| Halomonas TsdA + SoxZ — produces → tetrathionate end product | gene/protein/chemical/process | TsdA: EC 1.8.2.2; SoxZ: label-only; tetrathionate: CHEBI:30926 | “does contain thiosulfate dehydrogenase (TsdA)… This pathway produces tetrathionate as an end-product” (trutschel2023determiningresidentmicrobial pages 10-11) | DOI:10.3389/fmicb.2023.1182497 (2023) https://doi.org/10.3389/fmicb.2023.1182497 | Good mechanistic candidate; taxon-specific and MAG-based. |
| soxCDYZAXB gene cluster — enables → complete oxidation of thiosulfate to sulfate without free intermediates | pathway/gene/process/chemical | Sox system: label-only; thiosulfate: CHEBI:30087; sulfate: CHEBI:16189 | “gene clusters of the conserved soxCDYZAXB gene order… facilitates the complete oxidation of thiosulfate to sulfate, without free intermediates” (taubert2022bolsteringfitnessvia pages 5-6) | DOI:10.1038/s41396-021-01163-x (2022) https://doi.org/10.1038/s41396-021-01163-x | Strong comparative sulfur-oxidation edge; not specific to chemolithoheterotrophy alone. |
| truncated soxXYZAB + reverse Dsr/Apr/Sat — mediates → branched thiosulfate oxidation with elemental sulfur intermediate | pathway/gene/process/chemical | dsrABEFHCMKLJOPNR: label-only; aprAB: EC 1.8.99.2; sat: EC 2.7.7.4; elemental sulfur: CHEBI:26806 | “used the branched thiosulfate oxidation pathway… whereby Dsr operating in reverse oxidizes the sulfane-derived sulfur atom to sulfite, with elemental sulfur as intermediate” (taubert2022bolsteringfitnessvia pages 5-6) | DOI:10.1038/s41396-021-01163-x (2022) https://doi.org/10.1038/s41396-021-01163-x | Comparative mechanistic node set; especially relevant for sulfur-storage lineages. |
| amino acid/carboxylate importers — support → organic carbon uptake in mixotrophs/heterotrophs | transporter/process/chemical | transporters: label-only; lactate: CHEBI:24996; succinate: CHEBI:30031; amino acids: CHEBI class label-only | “Gene products relevant to import systems for amino acids and carboxylic acids… were overly abundant in mixotrophs and heterotrophs” (taubert2022bolsteringfitnessvia pages 5-6) | DOI:10.1038/s41396-021-01163-x (2022) https://doi.org/10.1038/s41396-021-01163-x | Comparative support for organic-carbon dependency side of trait. |
| PDO — oxidizes → sulfane sulfur to sulfite in *Beggiatoa leptomitoformis* model | enzyme/process/chemical/taxon | persulfide dioxygenase: EC label-only; sulfite: CHEBI:18498; taxon: *Beggiatoa leptomitoformis* (label-only) | “The resulting sulfane sulfur… is metabolized to sulfite by the action of persulfide dioxygenase.” (rudenko2024mechanismofintracellular pages 10-12) | DOI:10.3390/ijms252010962 (2024) https://doi.org/10.3390/ijms252010962 | Strong mechanistic proposal in one species; pathway reconstruction includes analogy to another bacterium. |
| sulfite + sulfane sulfur — chemically forms → thiosulfate | chemical reaction/process | sulfite: CHEBI:18498; thiosulfate: CHEBI:30087; sulfane sulfur: label-only | “sulfite is able to chemically react with sulfane sulfur to form thiosulfate” (rudenko2024mechanismofintracellular pages 10-12) | DOI:10.3390/ijms252010962 (2024) https://doi.org/10.3390/ijms252010962 | Chemical step supporting sulfur intermediate routing; organism-specific context. |
| thiosulfate transport to periplasm + branched Sox system — generates → energy metabolism in *Beggiatoa* | transporter/pathway/process/chemical | thiosulfate: CHEBI:30087; periplasm: GO:0042597; Sox system: label-only | “thiosulfate is then probably transported into the periplasm… oxidation by the branched Sox-system… the latter reaction… is an energy-generating reaction where thiosulfate is an electron donor” (rudenko2024mechanismofintracellular pages 10-12) | DOI:10.3390/ijms252010962 (2024) https://doi.org/10.3390/ijms252010962 | Includes “probably”; curate as uncertain/inferred. |
| colorless sulfur-oxidizing bacteria — include → chemolithoheterotrophs | trait/classification | sulfur-oxidizing bacteria: label-only; trait: METPO:1000638 | “colorless sulfur-oxidizing bacteria include chemolithoheterotrophs” (zhuang2024electrontransferin pages 5-6) | DOI:10.3390/life14050591 (2024) https://doi.org/10.3390/life14050591 | Background classification from review; low mechanistic specificity. |


*Table: This table lists candidate subject–predicate–object edges for curating a chemolithoheterotrophic TraitMech graph, grounded in the available experimental, genomic, and review evidence. It highlights which edges are strong exemplars versus comparative or inferred candidates that need cautious curation.*

### 7) Visual evidence (recommended for curator verification)

Key visuals from *Arcobacter peruensis* demonstrate the mechanistic profile expected for chemolithoheterotrophy: pathway summary (sulfide oxidation + denitrification + acetate metabolism; lack of canonical autotrophic fixation) and isotope-labeling comparisons showing acetate assimilation vs negligible bicarbonate fixation, plus a quantitative rates table (callbeck2019arcobacterperuensissp. media 126dcd32, callbeck2019arcobacterperuensissp. media 672097f5, callbeck2019arcobacterperuensissp. media 6db03913).

### 8) Warnings / “do-not-curate-yet” items (uncertainty flags)

1) **Cyc2 → Fe(II) oxidation edges** are currently **genomic/inferential** in hydrothermal-vent MAGs; the authors explicitly note functional understanding is limited and caution is needed when linking Cyc2 homologs to biotic iron oxidation (zhong2022metagenomicfeaturescharacterized pages 10-13). Curate as *candidate* nodes/edges with low confidence until experimentally validated.
2) **Kentron ecophysiological storage-buffer model (PHA, S0 cycling)** is mechanistically plausible and well-argued but remains partly a **model** linking redox oscillations to storage compound dynamics; curate those edges as uncertain unless supported by direct perturbation data (seah2019sulfuroxidizingsymbiontswithout pages 10-12).
3) **Sox/rDsr prevalence statements** (e.g., lithoheterotrophy more prevalent with Sox pathway) are comparative generalizations; useful for priors but not deterministic causal rules for all taxa (seah2019sulfuroxidizingsymbiontswithout pages 10-12).
4) **Beggiatoa PDO-centered pathway** contains several “probably/indirectly confirms” statements and relies on analogy to other bacteria; curate PDO edges with appropriate uncertainty tags and organism scope (rudenko2024mechanismofintracellular pages 10-12).

---

## DOI-first bibliography (with dates and URLs)

1) **Callbeck CM et al.** (Dec 2019). *Arcobacter peruensis* sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off Peru. **Applied and Environmental Microbiology**. DOI: **10.1128/AEM.01344-19**. https://doi.org/10.1128/AEM.01344-19 (callbeck2019arcobacterperuensissp. pages 1-2, callbeck2019arcobacterperuensissp. pages 2-5, callbeck2019arcobacterperuensissp. pages 9-12, callbeck2019arcobacterperuensissp. media 126dcd32, callbeck2019arcobacterperuensissp. media 672097f5, callbeck2019arcobacterperuensissp. media 6db03913)

2) **Seah BKB et al.** (May/Jun 2019). Sulfur-oxidizing symbionts without canonical genes for autotrophic CO2 fixation. **mBio**. DOI: **10.1128/mBio.01112-19**. https://doi.org/10.1128/mBio.01112-19 (seah2019sulfuroxidizingsymbiontswithout pages 2-4, seah2019sulfuroxidizingsymbiontswithout pages 10-12)

3) **Trutschel LR et al.** (Jun 2023). Determining resident microbial community members and their correlations with geochemistry in a serpentinizing spring. **Frontiers in Microbiology**. DOI: **10.3389/fmicb.2023.1182497**. https://doi.org/10.3389/fmicb.2023.1182497 (trutschel2023determiningresidentmicrobial pages 10-11)

4) **Rudenko TS et al.** (Oct 2024). Mechanism of intracellular elemental sulfur oxidation in *Beggiatoa leptomitoformis*, where persulfide dioxygenase plays a key role. **International Journal of Molecular Sciences**. DOI: **10.3390/ijms252010962**. https://doi.org/10.3390/ijms252010962 (rudenko2024mechanismofintracellular pages 10-12)

5) **Zhuang X et al.** (May 2024). Electron Transfer in the Biogeochemical Sulfur Cycle. **Life**. DOI: **10.3390/life14050591**. https://doi.org/10.3390/life14050591 (zhuang2024electrontransferin pages 5-6)

6) **Zhong Y-W et al.** (Nov/Dec 2022). Metagenomic features characterized with microbial iron oxidoreduction and mineral interaction in Southwest Indian Ridge. **Microbiology Spectrum**. DOI: **10.1128/spectrum.00614-22**. https://doi.org/10.1128/spectrum.00614-22 (zhong2022metagenomicfeaturescharacterized pages 10-13)

7) **Taubert M et al.** (Dec 2022 issue; online 2021 per DOI record). Bolstering fitness via CO2 fixation and organic carbon uptake: mixotrophs in modern groundwater. **The ISME Journal**. DOI: **10.1038/s41396-021-01163-x**. https://doi.org/10.1038/s41396-021-01163-x (taubert2022bolsteringfitnessvia pages 5-6)

8) **Hutt LP et al.** (Sep 2021). Insights into growth kinetics… during exochemolithoheterotrophic growth… **Archives of Microbiology**. DOI: **10.1007/s00203-020-02028-1**. https://doi.org/10.1007/s00203-020-02028-1 (hutt2021insightsintogrowth pages 1-6)


References

1. (quinn2025characterizingstratifiedmicrobiala pages 20-23): MW Quinn. Characterizing stratified microbial communities and a novel polyextremophilic chemolithoautotroph from hypersaline cold sulfur springs in the canadian high arctic. Unknown journal, 2025.

2. (seah2019sulfuroxidizingsymbiontswithout pages 10-12): Brandon K. B. Seah, Chakkiath Paul Antony, Bruno Huettel, Jan Zarzycki, Lennart Schada von Borzyskowski, Tobias J. Erb, Angela Kouris, Manuel Kleiner, Manuel Liebeke, Nicole Dubilier, and Harald R. Gruber-Vodicka. Sulfur-oxidizing symbionts without canonical genes for autotrophic co <sub>2</sub> fixation. mBio, Jun 2019. URL: https://doi.org/10.1128/mbio.01112-19, doi:10.1128/mbio.01112-19. This article has 32 citations and is from a domain leading peer-reviewed journal.

3. (taubert2022bolsteringfitnessvia pages 5-6): Martin Taubert, Will A Overholt, Beatrix M Heinze, Georgette Azemtsop Matanfack, Rola Houhou, Nico Jehmlich, Martin von Bergen, Petra Rösch, Jürgen Popp, and Kirsten Küsel. Bolstering fitness via co2 fixation and organic carbon uptake: mixotrophs in modern groundwater. The ISME Journal, 16:1153-1162, Dec 2022. URL: https://doi.org/10.1038/s41396-021-01163-x, doi:10.1038/s41396-021-01163-x. This article has 67 citations.

4. (hutt2021insightsintogrowth pages 1-6): Lee P. Hutt, Glenn M. Harper, A. John Moody, and Rich Boden. Insights into growth kinetics and roles of enzymes of krebs’ cycle and sulfur oxidation during exochemolithoheterotrophic growth of achromobacter aegrifaciens nccb 38021 on succinate with thiosulfate as the auxiliary electron donor. Archives of Microbiology, 203:561-578, Sep 2021. URL: https://doi.org/10.1007/s00203-020-02028-1, doi:10.1007/s00203-020-02028-1. This article has 7 citations and is from a peer-reviewed journal.

5. (callbeck2019arcobacterperuensissp. pages 1-2): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 60 citations and is from a peer-reviewed journal.

6. (callbeck2019arcobacterperuensissp. pages 9-12): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 60 citations and is from a peer-reviewed journal.

7. (callbeck2019arcobacterperuensissp. media 126dcd32): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 60 citations and is from a peer-reviewed journal.

8. (callbeck2019arcobacterperuensissp. media 672097f5): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 60 citations and is from a peer-reviewed journal.

9. (callbeck2019arcobacterperuensissp. media 6db03913): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 60 citations and is from a peer-reviewed journal.

10. (zhong2022metagenomicfeaturescharacterized pages 10-13): Ying-Wen Zhong, Peng Zhou, Hong Cheng, Ya-Dong Zhou, Jie Pan, Lin Xu, Meng Li, Chun-Hui Tao, Yue-Hong Wu, and Xue-Wei Xu. Metagenomic features characterized with microbial iron oxidoreduction and mineral interaction in southwest indian ridge. Microbiology Spectrum, Dec 2022. URL: https://doi.org/10.1128/spectrum.00614-22, doi:10.1128/spectrum.00614-22. This article has 19 citations and is from a domain leading peer-reviewed journal.

11. (trutschel2023determiningresidentmicrobial pages 10-11): Leah R. Trutschel, Brittany R. Kruger, Joshua D. Sackett, Grayson L. Chadwick, and Annette R. Rowe. Determining resident microbial community members and their correlations with geochemistry in a serpentinizing spring. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1182497, doi:10.3389/fmicb.2023.1182497. This article has 11 citations and is from a peer-reviewed journal.

12. (rudenko2024mechanismofintracellular pages 10-12): Tatyana S. Rudenko, Liubov I. Trubitsina, Vasily V. Terentyev, Ivan V. Trubitsin, Valentin I. Borshchevskiy, Svetlana V. Tishchenko, Azat G. Gabdulkhakov, Alexey A. Leontievsky, and Margarita Yu. Grabovich. Mechanism of intracellular elemental sulfur oxidation in beggiatoa leptomitoformis, where persulfide dioxygenase plays a key role. International Journal of Molecular Sciences, 25:10962, Oct 2024. URL: https://doi.org/10.3390/ijms252010962, doi:10.3390/ijms252010962. This article has 6 citations.

13. (seah2019sulfuroxidizingsymbiontswithout pages 2-4): Brandon K. B. Seah, Chakkiath Paul Antony, Bruno Huettel, Jan Zarzycki, Lennart Schada von Borzyskowski, Tobias J. Erb, Angela Kouris, Manuel Kleiner, Manuel Liebeke, Nicole Dubilier, and Harald R. Gruber-Vodicka. Sulfur-oxidizing symbionts without canonical genes for autotrophic co <sub>2</sub> fixation. mBio, Jun 2019. URL: https://doi.org/10.1128/mbio.01112-19, doi:10.1128/mbio.01112-19. This article has 32 citations and is from a domain leading peer-reviewed journal.

14. (zhuang2024electrontransferin pages 5-6): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

15. (callbeck2019arcobacterperuensissp. pages 2-5): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 60 citations and is from a peer-reviewed journal.