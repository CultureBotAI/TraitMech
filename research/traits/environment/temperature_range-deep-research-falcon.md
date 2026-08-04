---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:10:42.014346'
end_time: '2026-08-04T04:23:20.286926'
duration_seconds: 758.27
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range
  trait_identifier: METPO:1000306
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A temperature phenotype with numerical limits that bounds the minimum
    and maximum ambient temperatures supporting growth of an organism.
  parent_traits: METPO:1000533, METPO:1000535
  synonyms: ''
  evidence_summary: 'DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of
    high temperature (Thermophile-adaptation review supports the bounded ambient-temperature
    span over which membrane, enzyme, and bioenergetic adaptations sustain growth
    as the basis of the temperature-range phenotype.) | DOI:10.1038/sj.embor.7400662:
    decreased membrane fluidity (Psychrophile review supports cold-end membrane stress
    as a lower-bound growth constraint that low-temperature tolerance must overcome.)'
  causal_graph_summary: 'temperature_range_bounded_adaptation: 11 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 89
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000306
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that bounds the minimum and maximum ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the bounded ambient-temperature span over which membrane, enzyme, and bioenergetic adaptations sustain growth as the basis of the temperature-range phenotype.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as a lower-bound growth constraint that low-temperature tolerance must overcome.)
- **Existing causal graph summary:** temperature_range_bounded_adaptation: 11 nodes, 12 edges

## Research Objective

Research the microbial trait **temperature range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range.yaml`.

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
- **Trait label:** temperature range
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000306
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that bounds the minimum and maximum ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the bounded ambient-temperature span over which membrane, enzyme, and bioenergetic adaptations sustain growth as the basis of the temperature-range phenotype.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as a lower-bound growth constraint that low-temperature tolerance must overcome.)
- **Existing causal graph summary:** temperature_range_bounded_adaptation: 11 nodes, 12 edges

## Research Objective

Research the microbial trait **temperature range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range.yaml`.

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


# Curation report: microbial temperature range

## 1. Scope summary

**Target trait:** `METPO:1000306` (**temperature range**; ENVIRONMENT; CLASS; REVIEWED).

The trait should represent the **closed or operationally estimated interval of ambient temperatures supporting net microbial population growth under specified conditions**, conventionally bounded by minimum and maximum cardinal growth temperatures, *T*min and *T*max. In cardinal-temperature models, growth rate is zero below *T*min and above *T*max, while *T*opt is the temperature producing the maximum growth rate; therefore, *T*opt is a related parameter but is not the range itself. Rosso et al. explicitly model growth as zero for *T* < *T*min or *T* > *T*max. [DOI, published February 1995](https://doi.org/10.1128/aem.61.2.610-616.1995) (rosso1995convenientmodelto pages 1-2)

### Included

- Sustained vegetative or reproductive growth across a tested temperature series.
- Experimentally estimated *T*min and *T*max, including model-derived cardinal values when observations adequately bracket the boundaries.
- Genetically or physiologically mediated changes that expand, contract, or shift either growth boundary.
- Mechanisms that maintain membrane function, protein/RNA homeostasis, transport, bioenergetics, and redox balance sufficiently to permit growth near a boundary.

### Boundary cases and exclusions

1. **Not optimal growth temperature.** A change in *T*opt does not necessarily change range width or either boundary. In *Thermoanaerobacter kivui*, approximately 180 generations at 45°C shifted *T*opt from 66°C to 60°C, but the molecular basis and effects on the complete growth range remained unresolved. [DOI, published October 2023](https://doi.org/10.3389/fmicb.2023.1265216) (lehmann2023adaptivelaboratoryevolution pages 6-7, lehmann2023adaptivelaboratoryevolution pages 7-8)
2. **Not acute thermal survival.** Heat-shock resistance can be mechanistically opposed to growth at high temperature. Loss of `dnaJ` increased acute survival by 1,000–100,000-fold yet prevented sustained growth above 43°C in *Salmonella Typhimurium* and above 41°C in *E. coli*. [DOI, published 13 February 2024](https://doi.org/10.1128/mbio.03105-23) (berdejo2024evolutionarytradeoffbetween pages 8-10, berdejo2024evolutionarytradeoffbetween pages 1-2)
3. **Not dormancy or persistence.** A persister-like cell surviving heat without division does not establish that the organism grows at that temperature.
4. **Not metabolic activity alone.** Maintenance metabolism, substrate turnover, transcription, or viability without net population increase should be modeled separately.
5. **Not habitat temperature or isolation source.** Recovery from a hot spring, permafrost, or heated process is ecological evidence, not a measured growth range.
6. **Assay-conditioned phenotype.** Medium composition, pH, salinity, water activity, oxygen, pressure, substrate/loading rate, inoculum physiology, acclimation, observation duration, and detection threshold can alter an apparent boundary. Pressure is especially important above water’s normal boiling point; nutrient and osmotic conditions are likewise coupled to cold growth. Psychrophile literature emphasizes that pressure, salinity, oxidative stress, and nutrient availability interact with temperature. (damico2006psychrophilicmicroorganismschallenges pages 1-2)

**Recommended graph interpretation:** model *T*min and *T*max as two terminal boundary outcomes feeding the composite phenotype `METPO:1000306`, rather than treating “thermophile,” “psychrophile,” *T*opt, and heat-shock survival as interchangeable nodes.

## 2. Current mechanistic synthesis

Temperature range is an emergent systems phenotype. At the cold boundary, reduced reaction rates, membrane rigidification, impaired transport, stable inhibitory RNA structures, slow transcription/translation, protein folding defects, and possible ice formation jointly constrain growth. At the hot boundary, excess membrane fluidity/permeability, protein unfolding and aggregation, RNA/translation damage, redox imbalance, and loss of bioenergetic coupling become limiting. The authoritative psychrophile review lists “reduced enzyme activity,” “decreased membrane fluidity,” altered nutrient/waste transport, reduced transcription/translation/cell division, protein cold denaturation, inappropriate folding, and intracellular ice as cold-growth barriers. [DOI, published April 2006](https://doi.org/10.1038/sj.embor.7400662) (damico2006psychrophilicmicroorganismschallenges pages 1-2)

The strongest current graph architecture is therefore:

**ambient temperature → physicochemical damage/constraint → compensatory homeostasis module → retained cellular function → growth near boundary → temperature range.**

Recent research reinforces that no single universal mechanism determines the range. In 2024, a comparison of 2,739 thermal-performance datasets fitted to 83 models found no universal best mathematical model across traits and taxa, supporting explicit assay and taxon annotation rather than a universal curve assumption. [DOI, published October 2024](https://doi.org/10.1038/s41467-024-53046-2)

## 3. Candidate nodes grouped by type

### A. Trait and experimental nodes

- **temperature range** — `METPO:1000306`
- minimum growth temperature (*T*min) — retain label-only unless an approved METPO child is confirmed
- maximum growth temperature (*T*max) — label-only pending confirmed grounding
- optimal growth temperature (*T*opt) — related comparator, not part of the range definition
- ambient temperature; temperature upshift; temperature downshift; acute heat shock
- net population growth; maximum specific growth rate; doubling time; colony formation
- acclimation/pre-incubation, exposure duration, growth medium, pH, salinity, water activity, oxygen availability, hydrostatic pressure, nutrient/loading rate
- heat response — `GO:0009408`
- cold response — `GO:0009409`

### B. Membrane and lipid nodes

- plasma membrane — `GO:0005886`
- membrane fluidity/homeoviscous adaptation — label-only for the physical state/process unless a project-approved ontology term is available
- lipid metabolic process — `GO:0006629`
- fatty-acid biosynthetic process — `GO:0006633`
- saturated and unsaturated acyl-ACP pools
- phosphatidic acid, phosphatidylethanolamine, phosphatidylglycerol
- FabA, FabB, FabF, FabI, FabR, FadR, PlsB, PlsC — taxon-specific label nodes; add UniProt accessions only after strain selection
- glycerol dibiphytanyl glycerol tetraethers (GDGTs), cyclopentane rings, GrsA, GrsB
- ladderane lipids and ladderane cyclization
- plasmalogens, ether lipids, branched-chain and unsaturated fatty acids

### C. Proteostasis and translation nodes

- protein folding — `GO:0006457`
- translation — `GO:0006412`
- protein misfolding, aggregation, disaggregation, proteolysis
- DnaK/Hsp70, DnaJ, GrpE, GroEL/GroES, ClpB/ClpG, Hsf1, σ32/RpoH, FtsH
- Pab1 and temperature-triggered biomolecular condensates/stress granules
- VapC4 RNase and VapB4 antitoxin
- mRNA, rRNA, ribosome, stable RNA secondary structure, RNA thermometers, cold-shock proteins and RNA helicases

### D. Redox, ion, and compatible-solute nodes

- antioxidant activity — `GO:0016209`
- superoxide — `CHEBI:18421`
- hydrogen peroxide — `CHEBI:16240`
- dioxygen — `CHEBI:15379`
- mitochondrial manganese superoxide dismutase/Sod2
- potassium ion — `CHEBI:29103`
- magnesium ion — `CHEBI:18420`
- cyclic di-3′,5′-adenylate (c-di-AMP) — `CHEBI:49537`
- CdaA, CdaR, CdaS, DisA; potassium transport and osmotic homeostasis
- mannosylglycerate, di-myo-inositol phosphate, trehalose, ectoine/hydroxyectoine — candidate thermoprotectants, but temperature-range causality is generally weaker than osmotic-stress evidence

### E. Taxon nodes requiring later strain-level grounding

- *Escherichia coli* NCM3722
- *Salmonella enterica* serovar Typhimurium LT2/SL1344
- *Sulfolobus acidocaldarius*
- *Saccharolobus islandicus* REY15A
- *Cryptococcus neoformans* H99
- *Thermoanaerobacter kivui*
- *Lactococcus lactis* MG1363/TM29
- *Exiguobacterium sibiricum* 255-15
- “Candidatus Brocadia” enrichment

NCBITaxon CURIEs should be added from an authoritative taxonomy lookup during YAML implementation; they are deliberately not guessed here.

## 4. Curation-priority overview

The table below separates growth-boundary evidence from acute-survival and association-only evidence.

| module | candidate triple | evidence class | recommended curation status | key taxon/source |
|---|---|---|---|---|
| Scope / environmental driver | elevated temperature -> decreases membrane fluidity homeostasis unless lipid composition is remodeled | association | curate as general upstream driver | *Escherichia coli* homeoviscous adaptation study; broad microbial principle (hoogerland2024atemperaturesensitivemetabolic pages 1-2, hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| Scope / environmental driver | low temperature -> constrains enzyme activity, membrane fluidity, nutrient/waste transport, transcription, translation, and cell division | association | curate as high-level constraint node set, not a single mechanistic edge | psychrophile review across microbes (damico2006psychrophilicmicroorganismschallenges pages 1-2) |
| Membrane homeoviscous adaptation | FabI/FabB branchpoint activity ratio -> saturated vs unsaturated acyl-ACP flux | direct growth-at-temperature | curate | *E. coli*; temperature-sensitive metabolic valve in fatty-acid synthesis (hoogerland2024atemperaturesensitivemetabolic pages 1-2, hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| Membrane homeoviscous adaptation | C18:1 acyl-ACP–FabR feedback -> fabB repression/relief | direct growth-at-temperature | curate | *E. coli*; FabR negative feedback on membrane adaptation system (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 7-8) |
| Membrane homeoviscous adaptation | FabR-mediated transcriptional feedback -> accelerates homeoviscous adaptation after temperature shift | direct growth-at-temperature | curate with assay note: adaptation speed after shock, not boundary itself | *E. coli* ΔfabR cold-shock comparison (hoogerland2024atemperaturesensitivemetabolic pages 7-8) |
| Growth-upper-bound / proteostasis tradeoff | loss of dnaJ -> decreases maximum growth temperature | direct growth-at-temperature | curate | *Salmonella Typhimurium* and *E. coli* heat-evolution study showing inability to sustain growth above 43/41°C after dnaJ loss (berdejo2024evolutionarytradeoffbetween pages 1-2, berdejo2024evolutionarytradeoffbetween pages 8-10) |
| Heat survival vs range warning | loss of dnaJ -> increases acute heat-shock survival | survival-only | do not use alone for temperature-range edge; keep separate stress-survival branch | *Salmonella Typhimurium* repeated heat-shock selection (berdejo2024evolutionarytradeoffbetween pages 1-2, berdejo2024evolutionarytradeoffbetween pages 8-10) |
| Oxidative defense | Sod2 activity -> high-temperature growth | direct growth-at-temperature | curate | *Cryptococcus neoformans*; sod2 mutants show poor growth at elevated temperature, complementation rescues (giles2005cryptococcusneoformansmitochondrial pages 1-2) |
| Archaeal membrane adaptation | grsB -> highly cyclized GDGT formation | association | curate with uncertainty on phenotype linkage | *Saccharolobus islandicus* cold/acid stress omics; grsB expression tracks some high-ring GDGT changes but transcript not predictive alone (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 13-14) |
| Archaeal membrane adaptation | lower temperature -> lower GDGT cyclization | direct growth-at-temperature | curate as taxon-specific membrane-response edge | *Saccharolobus islandicus* under cold stress (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 13-14) |
| Translation / heat-stress persistence | VapC4 RNase activity -> mRNA/rRNA cleavage -> translation inhibition | survival-only | curate outside core range graph unless linked to growth boundary by stronger evidence | *Sulfolobus acidocaldarius* biochemical and genetic evidence (bhowmick2024roleofvapbc4 pages 1-2, bhowmick2024roleofvapbc4 pages 14-16) |
| Heat-stress persistence | VapC4 -> heat-stress survival / persister-like cell formation | survival-only | do not equate with temperature range; keep as auxiliary survival mechanism | *Sulfolobus acidocaldarius* 85°C heat-stress viability assays (bhowmick2024roleofvapbc4 pages 1-2, bhowmick2024roleofvapbc4 pages 14-16) |
| Ion/osmotic homeostasis | c-di-AMP synthesis pathway -> upper growth limit / thermal tolerance | association | uncertain; hold for review | Experimental evolution in *Bacillus* found convergent DAC-gene mutations and limited niche expansion (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17, hurtadobautista2024thermalplasticityand pages 2-3) |
| Membrane lipid remodeling / experimental evolution | altered membrane lipid synthesis (e.g., CDP-diglyceride synthase, plasmalogen/fatty-acid remodeling) -> improved growth at elevated or shifted temperatures | direct growth-at-temperature | curate as taxon-specific candidate edges | *Lactococcus lactis* ALE; *Thermoanaerobacter kivui* ALE associations (chen2015adaptationoflactococcus pages 1-2, lehmann2023adaptivelaboratoryevolution pages 6-7, lehmann2023adaptivelaboratoryevolution pages 7-8) |
| Thermal niche tuning / eukaryotic stress response | species-specific biomolecular condensation threshold -> tracks thermal niche | association | do not yet curate into microbial temperature-range graph without direct boundary perturbation | budding yeasts; condensation tuned to optimal/max growth temperatures (kik2024anadaptivebiomolecular pages 1-2, kik2024anadaptivebiomolecular pages 5-6) |


*Table: This table prioritizes candidate causal edges for curating microbial temperature range (METPO:1000306), separating strong growth-related mechanisms from survival-only or association evidence. It is useful for deciding which nodes and triples are ready for TraitMech curation versus which should remain provisional.*

## 5. Candidate causal edges with evidence

| Proposed subject–predicate–object triple | Reference | Supporting snippet | Curation interpretation |
|---|---|---|---|
| low ambient temperature → **decreases** → membrane fluidity | DOI: [10.1038/sj.embor.7400662](https://doi.org/10.1038/sj.embor.7400662) | “decreased membrane fluidity” is listed among the key barriers to cold proliferation. | **Curate.** General physical constraint on the lower boundary; source is a review rather than a single perturbation. (damico2006psychrophilicmicroorganismschallenges pages 1-2) |
| low ambient temperature → **reduces** → enzyme activity | DOI: [10.1038/sj.embor.7400662](https://doi.org/10.1038/sj.embor.7400662) | “reduced enzyme activity” and enzymes that “rigidify when the temperature drops.” | **Curate as high-level edge.** Avoid linking one enzyme family universally to *T*min. (damico2006psychrophilicmicroorganismschallenges pages 1-2) |
| low ambient temperature → **impairs** → nutrient and waste transport | DOI: [10.1038/sj.embor.7400662](https://doi.org/10.1038/sj.embor.7400662) | “altered transport of nutrients and waste products”; membrane permeability is affected. | **Curate.** Likely mediated by membrane state and transporter kinetics. (damico2006psychrophilicmicroorganismschallenges pages 1-2) |
| low ambient temperature → **reduces** → transcription, translation, and cell-division rates | DOI: [10.1038/sj.embor.7400662](https://doi.org/10.1038/sj.embor.7400662) | “decreased rates of transcription, translation and cell division.” | **Curate as a grouped constraint only if TraitMech permits parallel process nodes.** Review-level evidence. (damico2006psychrophilicmicroorganismschallenges pages 1-2) |
| temperature → **changes** → membrane lipid packing/fluidity | DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5) | “low temperatures reduce membrane fluidity by increasing the packing of membrane lipids.” | **Curate.** Strong modern mechanistic framing. (hoogerland2024atemperaturesensitivemetabolic pages 1-2) |
| FabI/FabB branchpoint activity → **allocates flux between** → saturated and unsaturated fatty-acid synthesis | DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5) | The system contains “a temperature-sensitive metabolic valve” acting “via the branchpoint enzymes FabI and FabB.” | **Curate, taxon-specific to *E. coli*.** Direct pathway quantification and modeling across 12–42°C. (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 1-2) |
| increased temperature → **increases** → C16:0 acyl-ACP and saturated sn-1 phospholipids | DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5) | “C16:0 ACP and 16:0 sn-1 phospholipids increase with temperature.” | **Curate, *E. coli*-specific.** Measured by LC–MS across five growth temperatures. (hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| decreased temperature → **increases relative abundance of** → C18:1 acyl-ACP and unsaturated phospholipids | DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5) | After 37→13°C shock, C16:0 ACP decreased about fivefold within 5 min while C18:1 ACP remained stable and became the dominant PlsB substrate. | **Curate as response mechanism**, not proof that it shifts *T*min. (hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| C18:1 acyl-ACP/FabR feedback → **regulates** → `fabB` expression | DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5) | C16:0 and C18:1 ACP compete for FabR; C18:1 ACP–FabR mediates repression. | **Curate, taxon-specific.** The detailed ligand/regulator relation should be represented separately from the phenotype edge. (hoogerland2024atemperaturesensitivemetabolic pages 7-8, hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| FabR feedback → **accelerates** → homeoviscous adaptation after temperature shift | DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5) | Wild type achieved “90% adaptation within 1 generation”; Δ`fabR` lacked overshoot and required more than one generation. | **Curate.** Direct knockout evidence for adaptation speed, but not yet a demonstrated shift in *T*min/*T*max. (hoogerland2024atemperaturesensitivemetabolic pages 7-8) |
| cold stress → **decreases** → average GDGT cyclization | DOI: [10.3389/fmicb.2023.1219779](https://doi.org/10.3389/fmicb.2023.1219779) | Cold stress caused “impaired growth” and “lower average GDGT cyclization.” | **Curate as taxon-specific response** in *S. islandicus*. It is association with impaired growth, not a causal range test. (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 13-14) |
| `grsB` expression → **promotes formation of** → GDGTs with ≥5 rings | DOI: [10.3389/fmicb.2023.1219779](https://doi.org/10.3389/fmicb.2023.1219779) | GrsB “forms highly cyclized GDGTs with ≥5 ring moieties”; cold downregulated `grsB` alongside fewer ≥5-ring GDGTs. | **Curate with uncertainty.** The study warns that transcription alone did not always predict lipid composition. (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 13-14) |
| increased ladderane cyclization → **associates with** → adaptation of anammox enrichment to 40°C | DOI: [10.1101/2024.07.23.604647](https://doi.org/10.1101/2024.07.23.604647) | Adaptation included “doubled ladderane cyclization” (*p*=0.005) and chaperone upregulation. | **Do not curate as definitive causal edge yet.** 2024 preprint, enrichment culture, no genetic perturbation, and process loading had to be reduced by at least half. (christina2024mechanismsofanammox pages 1-5) |
| DnaJ function → **supports** → sustained growth at high temperature | DOI: [10.1128/mbio.03105-23](https://doi.org/10.1128/mbio.03105-23) | Loss of DnaJ coincided with “an inability to sustain growth” above 43°C in *Salmonella* or 41°C in *E. coli*. | **High-priority curate.** Direct gene loss and growth-at-temperature evidence supports an upper-bound edge. (berdejo2024evolutionarytradeoffbetween pages 8-10) |
| loss of `dnaJ` → **increases** → acute heat-shock survival | DOI: [10.1128/mbio.03105-23](https://doi.org/10.1128/mbio.03105-23) | Heat resistance increased 1,000–100,000-fold, depending on strain and temperature. | **Keep outside core range path.** This is the clearest warning that heat resistance and *T*max are distinct. (berdejo2024evolutionarytradeoffbetween pages 8-10, berdejo2024evolutionarytradeoffbetween pages 1-2) |
| GroES/GroEL or DnaK overexpression → **increases** → growth/thermal tolerance at elevated temperature | DOI: [10.1038/srep14199](https://doi.org/10.1038/srep14199) | GroES–GroEL overexpression improved thermal tolerance; heterologous DnaK allowed *L. lactis* growth at a higher temperature. | **Curate as taxon- and construct-specific**, ideally from the primary overexpression reports cited by this study. (chen2015adaptationoflactococcus pages 1-2) |
| Sod2 antioxidant activity → **enables** → high-temperature growth | DOI: [10.1128/EC.4.1.46-54.2005](https://doi.org/10.1128/EC.4.1.46-54.2005) | `sod2` mutants had “poor growth at elevated temperatures”; reconstitution restored the temperature-sensitive phenotype, and anaerobic incubation rescued viability. | **High-priority curate, fungal-specific.** Reverse genetics, complementation, and oxygen dependence establish a mechanistic redox link. (giles2005cryptococcusneoformansmitochondrial pages 1-2) |
| temperature-triggered Pab1 condensation threshold → **tracks** → species thermal niche | DOI: [10.1038/s41467-024-47355-9](https://doi.org/10.1038/s41467-024-47355-9) | Purified Pab1 condensation temperatures correlated with species’ optimal and maximum growth temperatures. | **Uncertain/association.** Strong biophysical evidence in three budding yeasts, but no direct demonstration that shifting condensation changes *T*max. (kik2024anadaptivebiomolecular pages 5-6, kik2024anadaptivebiomolecular pages 1-2) |
| heat stress → **induces** → VapC4 RNase-dependent translation inhibition | DOI: [10.1128/mbio.02753-24](https://doi.org/10.1128/mbio.02753-24) | VapC4 cleaves mRNA/rRNA, “ultimately leading to the inhibition of translation”; VapB4 binds VapC4 with *K*d ≈40±2 nM. | **Curate as a mechanistic stress-response branch**, not directly as a range-expansion edge. (bhowmick2024roleofvapbc4 pages 14-16, bhowmick2024roleofvapbc4 pages 1-2) |
| VapC4 → **increases** → survival at 85°C through persister-like formation | DOI: [10.1128/mbio.02753-24](https://doi.org/10.1128/mbio.02753-24) | Δ`vapC4` and Δ`vapBC4` were impaired at 85°C; complementation restored resilience. | **Survival-only; do not map directly to `METPO:1000306`.** No difference occurred at the 75°C optimal growth condition. (bhowmick2024roleofvapbc4 pages 14-16) |
| c-di-AMP synthesis-pathway variation → **modulates** → upper-temperature growth tolerance | DOI: [10.3390/biology13121088](https://doi.org/10.3390/biology13121088) | Convergent mutations occurred in `cdaR`/`disA` and related DAC genes; one *B. subtilis* strain expanded its niche by 4°C, whereas most lines failed. | **Uncertain candidate.** Parallel evolution implicates the pathway, probably through K⁺/osmotic homeostasis, but individual mutations require reconstruction. (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17, hurtadobautista2024thermalplasticityand pages 2-3) |
| adaptive membrane/proteostasis mutations → **increase** → *L. lactis* upper growth temperature | DOI: [10.1038/srep14199](https://doi.org/10.1038/srep14199) | Evolved TM29 grew well to 39°C and continuously at 40°C after pre-incubation; mutations affected a chaperone, riboflavin transporter, RNA polymerase, and CDP-diglyceride synthase. | **Curate only reconstructed individual effects.** The composite evolved genotype is causal, but not every mutation should receive an independent edge. (chen2015adaptationoflactococcus pages 1-2) |

## 6. Recent developments and quantitative findings, 2023–2024

1. **Quantitative membrane control in one generation.** Hoogerland et al. resolved an *E. coli* temperature-sensitive FabI/FabB metabolic valve plus FabR feedback. A 37→13°C shift reduced C16:0 ACP approximately fivefold within 5 min; wild-type membranes reached 90% adaptation within one generation, while Δ`fabR` required longer. This is among the strongest recent mechanistic studies for a graph connecting temperature sensing to membrane state. [DOI, accepted 17 October 2024](https://doi.org/10.1038/s41467-024-53677-5) (hoogerland2024atemperaturesensitivemetabolic pages 7-8, hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 1-2)
2. **Growth and acute survival were experimentally decoupled.** Recurrent 55°C, 20-min heat shocks selected `dnaJ` loss-of-function mutants in all six *S. Typhimurium* lineages. Survival rose more than 1,000-fold, but maximum sustainable growth temperature fell. This is a decisive curation lesson: “thermal tolerance” must be predicate- and assay-specific. [DOI, published 13 February 2024](https://doi.org/10.1128/mbio.03105-23) (berdejo2024evolutionarytradeoffbetween pages 8-10, berdejo2024evolutionarytradeoffbetween pages 1-2)
3. **Evolutionary constraints on range expansion.** Across experimental evolution of six wild *Bacillus* strains, only one *B. subtilis* strain achieved a 4°C niche expansion; most strains could not establish robust growth even 3°C above their original range. Convergent mutations implicated c-di-AMP synthesis/K⁺ homeostasis, but genetic background strongly constrained outcomes. [DOI, published December 2024](https://doi.org/10.3390/biology13121088) (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17)
4. **Archaeal lipid response is not inferable from transcripts alone.** *S. islandicus* cold stress impaired growth, reduced average GDGT cyclization, and downregulated `grsB`, but acid stress showed that `grsB` upregulation did not necessarily yield more highly cyclized GDGTs. Multi-omic edges should therefore stop at the measured molecular phenotype unless genetically validated. [DOI, published 15 August 2023](https://doi.org/10.3389/fmicb.2023.1219779) (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 13-14)
5. **Thermal niche tuning of biomolecular condensation.** Three budding yeasts diverged by up to 100 million years showed species-specific condensation thresholds that tracked growth and transcriptional responses; purified Pab1 retained niche-tuned condensation. This is a compelling candidate mechanism for eukaryotic microbes, but remains insufficient for a direct range edge. [DOI, accepted 27 March 2024](https://doi.org/10.1038/s41467-024-47355-9) (kik2024anadaptivebiomolecular pages 5-6, kik2024anadaptivebiomolecular pages 1-2)
6. **Broad-range exemplar.** *E. sibiricum* grows from approximately −5°C to 39–40°C. Relative to 28°C, 27%, 3.2%, and 5.2% of assayed coding sequences were differentially expressed at −2.5°C, 10°C, and 39°C, respectively, illustrating that boundary growth recruits much broader stress remodeling than growth within the central range. [DOI, published 18 November 2008](https://doi.org/10.1186/1471-2164-9-547) (rodrigues2008architectureofthermal pages 1-2)

## 7. Applications and real-world implementation

- **Dairy fermentation:** ALE-derived *L. lactis* TM29 grew to 39°C and, after lower-temperature pre-incubation, continuously at 40°C. At 38°C it grew 33% faster and had a 12% higher specific lactate-production rate than its parent. Because cheese curd temperatures can approach or exceed 40°C, this is a direct industrial implementation path for thermally robust, non-GMO starter strains. The paper notes that more than 100 million tonnes of milk annually are inoculated with *L. lactis*. [DOI, published 21 September 2015](https://doi.org/10.1038/srep14199) (chen2015adaptationoflactococcus pages 1-2)
- **High-temperature wastewater nitrogen removal:** A 2024 anammox preprint adapted a “Ca. Brocadia” enrichment from 30°C to 40°C, but successful operation required at least halving the initial loading rate. Chaperone induction and doubled ladderane cyclization (*p*=0.005) provide process biomarkers, not yet validated engineering targets. [Preprint DOI, posted July 2024](https://doi.org/10.1101/2024.07.23.604647) (christina2024mechanismsofanammox pages 1-5)
- **Food safety:** The `dnaJ` result shows that repeated lethal heating may select organisms with much greater acute heat survival but poorer high-temperature growth. Predictive food microbiology should therefore estimate growth boundaries and inactivation kinetics separately. (berdejo2024evolutionarytradeoffbetween pages 8-10, berdejo2024evolutionarytradeoffbetween pages 1-2)
- **Biomanufacturing:** Controlled temperature can improve recombinant protein folding and alter product formation. A review reports lower-temperature cultivation improving folding and reducing degradation, and a temperature-optimized steroid bioconversion reaching 95% conversion, illustrating why temperature is both a trait-defining environment and a process-control variable. [DOI, published January 2020](https://doi.org/10.3390/pr8010121) (noll2020modelingandexploiting pages 22-23)
- **Climate-response forecasting:** The limited *Bacillus* niche expansion under gradual warming challenges assumptions that short microbial generation times guarantee rapid adaptation to 2–4°C climate warming. This conclusion is taxon- and experiment-specific, but it supports representing adaptive capacity as constrained rather than automatic. (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 2-3)

## 8. Recommended initial TraitMech graph

A conservative first revision could contain approximately 15–20 nodes in two converging branches:

### Lower-bound branch

`low ambient temperature` → decreases `membrane fluidity` → impairs `membrane transport/bioenergetics` → decreases `net population growth near Tmin`

`low ambient temperature` → stabilizes RNA structures / slows enzyme activity and translation → decreases `net population growth near Tmin`

`FabI/FabB/FabR-controlled unsaturated-fatty-acid remodeling` → restores `membrane fluidity` → supports `growth near Tmin` → lowers `Tmin` **[last edge inferred; mark uncertain until direct boundary perturbation]**

### Upper-bound branch

`high ambient temperature` → increases `protein misfolding/aggregation` → increases demand for `DnaK–DnaJ–GrpE/GroEL–GroES proteostasis` → supports `growth near Tmax`

`high ambient temperature + aerobic respiration` → increases `ROS burden` → requires `Sod2 antioxidant activity` → supports `growth near Tmax` → raises `Tmax` **[direct in *C. neoformans*]**

`high ambient temperature` → perturbs `membrane fluidity/permeability` → induces lipid saturation/cyclization remodeling → supports `growth near Tmax` **[mechanism strong; direct boundary edge usually uncertain]**

### Composite trait

`Tmin` + `Tmax` → define → `METPO:1000306`

Use evidence qualifiers on every edge: `direct_genetic`, `direct_biochemical`, `growth_at_temperature`, `acute_survival`, `omics_association`, `review_synthesis`, `taxon_specific`, and `assay_specific`.

## 9. Claims that should not yet be curated

1. **Do not assert that any heat-shock-survival gene expands temperature range.** `dnaJ` loss proves the opposite can occur. (berdejo2024evolutionarytradeoffbetween pages 8-10)
2. **Do not connect VapC4 directly to increased *T*max.** The evidence concerns 85°C viability/persistence, not sustained division. (bhowmick2024roleofvapbc4 pages 14-16)
3. **Do not assign `grsB` expression directly to wider range.** GrsB’s lipid product is supported, but transcript abundance is not reliably predictive of GDGT composition or growth boundaries. (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 13-14)
4. **Do not treat c-di-AMP genes as validated universal heat-tolerance determinants.** The 2024 evidence is convergent evolutionary association and strongly lineage-dependent. (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17)
5. **Do not curate every ALE mutation as causal.** The 67 SNPs in cold-adapted *T. kivui*—including `fabG`, `sigH`, `kdpC`, and regulatory mutations—are candidates until reconstructed individually. (lehmann2023adaptivelaboratoryevolution pages 6-7, lehmann2023adaptivelaboratoryevolution pages 7-8)
6. **Do not use genomic GC content as a causal node.** Its correlation with optimal growth temperature is broad and phylogenetically complex; it does not establish a mechanism controlling range boundaries.
7. **Do not infer growth range from environmental sequencing, isolation temperature, enzyme optima, or community abundance.** These measure realized habitat, component performance, or ecological filtering rather than organismal cardinal growth limits.
8. **Do not universalize bacterial lipid rules to Archaea.** Bacterial ester-bilayer remodeling and archaeal ether-linked GDGT cyclization are mechanistically distinct solutions.
9. **Do not curate compatible solutes as temperature-range determinants without perturbation.** For example, mannosylglycerate can accumulate under thermal stress, yet deletion may only slightly affect growth; thermoprotection and range expansion are not equivalent.
10. **Treat the 2024 anammox ladderane study as provisional.** It is a preprint using a mixed enrichment and operational co-interventions. (christina2024mechanismsofanammox pages 1-5)

## 10. DOI-first bibliography

### Priority 2023–2024 sources

1. Hoogerland L. et al. “A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in *Escherichia coli*.” *Nature Communications* 15, 9386. Accepted 17 October 2024. DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5). (hoogerland2024atemperaturesensitivemetabolic pages 7-8, hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 1-2)
2. Berdejo D. et al. “Evolutionary trade-off between heat shock resistance, growth at high temperature, and virulence expression in *Salmonella* Typhimurium.” *mBio* 15. Published 13 February 2024. DOI: [10.1128/mbio.03105-23](https://doi.org/10.1128/mbio.03105-23). (berdejo2024evolutionarytradeoffbetween pages 8-10, berdejo2024evolutionarytradeoffbetween pages 1-2)
3. Bhowmick A. et al. “Role of VapBC4 toxin-antitoxin system of *Sulfolobus acidocaldarius* in heat stress adaptation.” *mBio* 15. Published 13 November 2024. DOI: [10.1128/mbio.02753-24](https://doi.org/10.1128/mbio.02753-24). (bhowmick2024roleofvapbc4 pages 14-16, bhowmick2024roleofvapbc4 pages 1-2)
4. Kik S.K. et al. “An adaptive biomolecular condensation response is conserved across environmentally divergent species.” *Nature Communications* 15, 3127. Accepted 27 March 2024. DOI: [10.1038/s41467-024-47355-9](https://doi.org/10.1038/s41467-024-47355-9). (kik2024anadaptivebiomolecular pages 5-6, kik2024anadaptivebiomolecular pages 1-2)
5. Hurtado-Bautista E. et al. “Thermal Plasticity and Evolutionary Constraints in *Bacillus*.” *Biology* 13, 1088. December 2024. DOI: [10.3390/biology13121088](https://doi.org/10.3390/biology13121088). (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17, hurtadobautista2024thermalplasticityand pages 2-3)
6. Maiti A. et al. “Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.” *Chemical Communications* 60, 10280–10294. Accepted 20 August 2024. DOI: [10.1039/D4CC03114H](https://doi.org/10.1039/D4CC03114H). (maiti2024extrememakeoverthe pages 1-2)
7. Karmann C. et al. “Mechanisms of Anammox Adaptation to High Temperatures.” bioRxiv, July 2024. DOI: [10.1101/2024.07.23.604647](https://doi.org/10.1101/2024.07.23.604647). **Preprint.** (christina2024mechanismsofanammox pages 1-5)
8. Chiu B.K. et al. “Membrane lipid and expression responses of *Saccharolobus islandicus* REY15A to acid and cold stress.” *Frontiers in Microbiology* 14. Published 15 August 2023. DOI: [10.3389/fmicb.2023.1219779](https://doi.org/10.3389/fmicb.2023.1219779). (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 13-14)
9. Lehmann M. et al. “Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.” *Frontiers in Microbiology* 14. October 2023. DOI: [10.3389/fmicb.2023.1265216](https://doi.org/10.3389/fmicb.2023.1265216). (lehmann2023adaptivelaboratoryevolution pages 6-7, lehmann2023adaptivelaboratoryevolution pages 7-8, lehmann2023adaptivelaboratoryevolution pages 2-3)

### Foundational mechanistic and scope sources

10. Rosso L. et al. “Convenient Model To Describe the Combined Effects of Temperature and pH on Microbial Growth.” *Applied and Environmental Microbiology* 61, 610–616. February 1995. DOI: [10.1128/AEM.61.2.610-616.1995](https://doi.org/10.1128/AEM.61.2.610-616.1995). (rosso1995convenientmodelto pages 1-2)
11. D’Amico S. et al. “Psychrophilic microorganisms: challenges for life.” *EMBO Reports* 7, 385–389. April 2006. DOI: [10.1038/sj.embor.7400662](https://doi.org/10.1038/sj.embor.7400662). (damico2006psychrophilicmicroorganismschallenges pages 1-2)
12. Giles S.S. et al. “*Cryptococcus neoformans* Mitochondrial Superoxide Dismutase: an Essential Link between Antioxidant Function and High-Temperature Growth.” *Eukaryotic Cell* 4, 46–54. January 2005. DOI: [10.1128/EC.4.1.46-54.2005](https://doi.org/10.1128/EC.4.1.46-54.2005). (giles2005cryptococcusneoformansmitochondrial pages 1-2)
13. Rodrigues D.F. et al. “Architecture of thermal adaptation in an *Exiguobacterium sibiricum* strain.” *BMC Genomics* 9, 547. Published 18 November 2008. DOI: [10.1186/1471-2164-9-547](https://doi.org/10.1186/1471-2164-9-547). (rodrigues2008architectureofthermal pages 1-2)
14. Chen J. et al. “Adaptation of *Lactococcus lactis* to high growth temperature leads to a dramatic increase in acidification rate.” *Scientific Reports* 5, 14199. Published 21 September 2015. DOI: [10.1038/srep14199](https://doi.org/10.1038/srep14199). (chen2015adaptationoflactococcus pages 1-2)
15. Noll P. et al. “Modeling and Exploiting Microbial Temperature Response.” *Processes* 8, 121. January 2020. DOI: [10.3390/pr8010121](https://doi.org/10.3390/pr8010121). (noll2020modelingandexploiting pages 6-8, noll2020modelingandexploiting pages 22-23)
16. Tolner B., Poolman B., Konings W.N. “Adaptation of microorganisms and their transport systems to high temperatures.” *Comparative Biochemistry and Physiology A* 118, 423–428. November 1997. DOI: [10.1016/S0300-9629(97)00003-0](https://doi.org/10.1016/S0300-9629(97)00003-0).

References

1. (rosso1995convenientmodelto pages 1-2): L Rosso, J R Lobry, S Bajard, and J P Flandrois. Convenient model to describe the combined effects of temperature and ph on microbial growth. Applied and Environmental Microbiology, 61:610-616, Feb 1995. URL: https://doi.org/10.1128/aem.61.2.610-616.1995, doi:10.1128/aem.61.2.610-616.1995. This article has 777 citations and is from a peer-reviewed journal.

2. (lehmann2023adaptivelaboratoryevolution pages 6-7): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

3. (lehmann2023adaptivelaboratoryevolution pages 7-8): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

4. (berdejo2024evolutionarytradeoffbetween pages 8-10): Daniel Berdejo, Julien Mortier, Alexander Cambré, Malgorzata Sobota, Ronald Van Eyken, Tom Dongmin Kim, Kristof Vanoirbeek, Diego García Gonzalo, Rafael Pagán, Médéric Diard, and Abram Aertsen. Evolutionary trade-off between heat shock resistance, growth at high temperature, and virulence expression in <i>salmonella</i> typhimurium. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03105-23, doi:10.1128/mbio.03105-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

5. (berdejo2024evolutionarytradeoffbetween pages 1-2): Daniel Berdejo, Julien Mortier, Alexander Cambré, Malgorzata Sobota, Ronald Van Eyken, Tom Dongmin Kim, Kristof Vanoirbeek, Diego García Gonzalo, Rafael Pagán, Médéric Diard, and Abram Aertsen. Evolutionary trade-off between heat shock resistance, growth at high temperature, and virulence expression in <i>salmonella</i> typhimurium. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03105-23, doi:10.1128/mbio.03105-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

6. (damico2006psychrophilicmicroorganismschallenges pages 1-2): Salvino D'Amico, Tony Collins, Jean‐Claude Marx, Georges Feller, Charles Gerday, and Charles Gerday. Psychrophilic microorganisms: challenges for life. EMBO reports, 7:385-389, Apr 2006. URL: https://doi.org/10.1038/sj.embor.7400662, doi:10.1038/sj.embor.7400662. This article has 1141 citations and is from a highest quality peer-reviewed journal.

7. (hoogerland2024atemperaturesensitivemetabolic pages 1-2): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

8. (hoogerland2024atemperaturesensitivemetabolic pages 3-4): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

9. (hoogerland2024atemperaturesensitivemetabolic pages 7-8): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

10. (giles2005cryptococcusneoformansmitochondrial pages 1-2): Steven S. Giles, Ines Batinić-Haberle, John R. Perfect, and Gary M. Cox. Cryptococcus neoformans mitochondrial superoxide dismutase: an essential link between antioxidant function and high-temperature growth. Eukaryotic Cell, 4:46-54, Jan 2005. URL: https://doi.org/10.1128/ec.4.1.46-54.2005, doi:10.1128/ec.4.1.46-54.2005. This article has 141 citations and is from a peer-reviewed journal.

11. (chiu2023membranelipidand pages 1-2): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

12. (chiu2023membranelipidand pages 13-14): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

13. (bhowmick2024roleofvapbc4 pages 1-2): Arghya Bhowmick, Alejandra Recalde, Chandrima Bhattacharyya, Ankita Banerjee, Jagriti Das, Ulises E. Rodriguez-Cruz, Sonja-Verena Albers, and Abhrajyoti Ghosh. Role of vapbc4 toxin-antitoxin system of <i>sulfolobus acidocaldarius</i> in heat stress adaptation. Dec 2024. URL: https://doi.org/10.1128/mbio.02753-24, doi:10.1128/mbio.02753-24. This article has 10 citations and is from a domain leading peer-reviewed journal.

14. (bhowmick2024roleofvapbc4 pages 14-16): Arghya Bhowmick, Alejandra Recalde, Chandrima Bhattacharyya, Ankita Banerjee, Jagriti Das, Ulises E. Rodriguez-Cruz, Sonja-Verena Albers, and Abhrajyoti Ghosh. Role of vapbc4 toxin-antitoxin system of <i>sulfolobus acidocaldarius</i> in heat stress adaptation. Dec 2024. URL: https://doi.org/10.1128/mbio.02753-24, doi:10.1128/mbio.02753-24. This article has 10 citations and is from a domain leading peer-reviewed journal.

15. (hurtadobautista2024thermalplasticityand pages 1-2): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

16. (hurtadobautista2024thermalplasticityand pages 16-17): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

17. (hurtadobautista2024thermalplasticityand pages 2-3): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

18. (chen2015adaptationoflactococcus pages 1-2): Jun Chen, Jing Shen, Lars Ingvar Hellgren, Peter Ruhdal Jensen, and Christian Solem. Adaptation of lactococcus lactis to high growth temperature leads to a dramatic increase in acidification rate. Scientific Reports, Sep 2015. URL: https://doi.org/10.1038/srep14199, doi:10.1038/srep14199. This article has 116 citations and is from a peer-reviewed journal.

19. (kik2024anadaptivebiomolecular pages 1-2): Samantha Keyport Kik, Dana Christopher, Hendrik Glauninger, Caitlin Wong Hickernell, J. Bard, Kyle M Lin, Allison H Squires, Michael Ford, Tobin S Sosnick, and Allan Drummond. An adaptive biomolecular condensation response is conserved across environmentally divergent species. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47355-9, doi:10.1038/s41467-024-47355-9. This article has 38 citations and is from a highest quality peer-reviewed journal.

20. (kik2024anadaptivebiomolecular pages 5-6): Samantha Keyport Kik, Dana Christopher, Hendrik Glauninger, Caitlin Wong Hickernell, J. Bard, Kyle M Lin, Allison H Squires, Michael Ford, Tobin S Sosnick, and Allan Drummond. An adaptive biomolecular condensation response is conserved across environmentally divergent species. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47355-9, doi:10.1038/s41467-024-47355-9. This article has 38 citations and is from a highest quality peer-reviewed journal.

21. (christina2024mechanismsofanammox pages 1-5): Karmann Christina, Navrátilová Klára, Behner Adam, Noor Tayyaba, Danner Stella, Majchrzak Anastasia, Šantrůček Jiří, Podzimek Tomáš, Marin Lopez Marco A., Hajšlová Jana, Lipovová Petra, Bartáček Jan, and Kouba Vojtěch. Mechanisms of anammox adaptation to high temperatures: increased cyclization of ladderane lipids and proteomic insights. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.23.604647, doi:10.1101/2024.07.23.604647. This article has 1 citations.

22. (rodrigues2008architectureofthermal pages 1-2): Debora F Rodrigues, Natalia Ivanova, Zhili He, Marianne Huebner, Jizhong Zhou, and James M Tiedje. Architecture of thermal adaptation in an exiguobacterium sibiricum strain isolated from 3 million year old permafrost: a genome and transcriptome approach. BMC Genomics, 9:547-547, Nov 2008. URL: https://doi.org/10.1186/1471-2164-9-547, doi:10.1186/1471-2164-9-547. This article has 183 citations and is from a peer-reviewed journal.

23. (noll2020modelingandexploiting pages 22-23): Philipp Noll, Lars Lilge, Rudolf Hausmann, and Marius Henkel. Modeling and exploiting microbial temperature response. ArXiv, 8:121, Jan 2020. URL: https://doi.org/10.3390/pr8010121, doi:10.3390/pr8010121. This article has 73 citations.

24. (maiti2024extrememakeoverthe pages 1-2): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 17 citations and is from a domain leading peer-reviewed journal.

25. (lehmann2023adaptivelaboratoryevolution pages 2-3): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

26. (noll2020modelingandexploiting pages 6-8): Philipp Noll, Lars Lilge, Rudolf Hausmann, and Marius Henkel. Modeling and exploiting microbial temperature response. ArXiv, 8:121, Jan 2020. URL: https://doi.org/10.3390/pr8010121, doi:10.3390/pr8010121. This article has 73 citations.