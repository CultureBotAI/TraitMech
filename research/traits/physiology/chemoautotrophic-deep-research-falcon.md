---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:47:49.786247'
end_time: '2026-08-04T10:54:26.013790'
duration_seconds: 396.23
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemoautotrophic
  trait_identifier: METPO:1000635
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemoautotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from oxidation of
    inorganic compounds and carbon from carbon dioxide.
  parent_traits: METPO:1000631
  synonyms: chemoautotroph
  evidence_summary: 'DOI:10.1146/annurev.micro.52.1.191: Carbon Dioxide Fixation in
    Chemoautotrophs (Review supports CO2 fixation as central to chemoautotrophic bacteria.)
    | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review
    supports Calvin-Benson and other microbial autotrophic CO2-fixation pathways.)'
  causal_graph_summary: 'chemoautotrophic_chemical_energy_co2_fixation: 16 nodes,
    17 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000635
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: Carbon Dioxide Fixation in Chemoautotrophs (Review supports CO2 fixation as central to chemoautotrophic bacteria.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports Calvin-Benson and other microbial autotrophic CO2-fixation pathways.)
- **Existing causal graph summary:** chemoautotrophic_chemical_energy_co2_fixation: 16 nodes, 17 edges

## Research Objective

Research the microbial trait **chemoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautotrophic.yaml`.

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
- **Trait label:** chemoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000635
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: Carbon Dioxide Fixation in Chemoautotrophs (Review supports CO2 fixation as central to chemoautotrophic bacteria.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports Calvin-Benson and other microbial autotrophic CO2-fixation pathways.)
- **Existing causal graph summary:** chemoautotrophic_chemical_energy_co2_fixation: 16 nodes, 17 edges

## Research Objective

Research the microbial trait **chemoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautotrophic.yaml`.

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


# Curation report: chemoautotrophic

**Target:** `METPO:1000635`  
**Category:** PHYSIOLOGY · **Kind:** CLASS · **Status:** REVIEWED  
**Parent:** `METPO:1000631`

## 1. Scope and current understanding

The trait denotes a trophic phenotype in which an organism obtains energy by oxidizing inorganic compounds and obtains cellular carbon primarily by fixing CO₂ or bicarbonate. The graph should therefore require two connected capacities: **(i) inorganic electron-donor oxidation coupled to energy conservation and (ii) autotrophic inorganic-carbon assimilation**. Classical donors include H₂, H₂S, thiosulfate, NH₄⁺/NH₃, NO₂⁻, and Fe²⁺; common terminal acceptors include O₂ and nitrate. Facultative chemoautotrophs may also grow heterotrophically or mixotrophically. (shively1998somethingfromalmost pages 3-5)

“Chemoautotrophic” is often used nearly interchangeably with **chemolithoautotrophic**, but the latter makes the inorganic nature of the electron donor explicit. Neither **chemolithotrophy alone** nor possession of an inorganic-substrate oxidation module is sufficient: gamma-methanotrophs examined in 2023 possessed putative thiosulfate-oxidation genes but lacked autotrophic fixation and showed no corresponding growth benefit. Conversely, an organism fixing CO₂ using light energy is photoautotrophic rather than chemoautotrophic. Methanotrophy and methylotrophy use reduced one-carbon compounds containing carbon and therefore are not automatically chemoautotrophic. (marc2023physiologicalandgenetic pages 98-103)

### Boundary rules recommended for TraitMech

- **Include:** demonstrated growth or biomass synthesis from inorganic carbon, energized predominantly by oxidation of an inorganic donor.
- **Include with qualifier:** facultative organisms when the chemoautotrophic growth mode is directly demonstrated.
- **Do not infer from donor oxidation genes alone.** Require a complete carbon-fixation module or preferably physiological/isotope evidence.
- **Do not treat mixotrophic CO₂ incorporation as equivalent to strict chemoautotrophic growth** unless inorganic energy supply and net biomass production are established.
- **Do not require the Calvin–Benson–Bassham cycle universally.** Modern environmental genomes also support rTCA and Wood–Ljungdahl implementations. In 2024 groundwater data, 60% of reconstructed MAGs encoded autotrophic pathways, dominated by CBB but including rTCA and Wood–Ljungdahl pathways. (atencio2024metabolicadaptationsunderpin pages 6-8)

## 2. Candidate nodes

### Trait-defining processes

- `METPO:1000635` — chemoautotrophic.
- Carbon fixation — `GO:0015977`.
- Generation of precursor metabolites and energy — `GO:0006091`.
- Aerobic electron-transport chain — `GO:0019646`.
- Inorganic electron-donor oxidation; chemiosmotic energy conservation; proton-motive force; ATP synthesis; NAD(P)H generation — retain as label-only candidates until exact GO terms are verified.

### Carbon sources and electron donors/acceptors

- Carbon dioxide — `CHEBI:16526`.
- H₂/bicarbonate, H₂S, sulfide, thiosulfate, NH₃/NH₄⁺, nitrite, Fe²⁺, O₂, nitrate, sulfate and elemental sulfur — ground only after identifier validation against the target ontology release.
- O₂ and nitrate are alternative acceptors in different taxa and conditions; they should not be represented as universally required. (shively1998somethingfromalmost pages 3-5)

### Carbon-fixation pathways and enzymes

- Calvin–Benson–Bassham cycle.
- RuBisCO — `EC:4.1.1.39`.
- Phosphoribulokinase — `EC:2.7.1.19`.
- Sedoheptulose-bisphosphatase.
- Reverse/reductive TCA cycle.
- Wood–Ljungdahl/reductive acetyl-CoA pathway.
- 3-hydroxypropionate-related fixation module, relevant to engineering rather than a universal core.
- Carbonic anhydrase and inorganic-carbon concentrating mechanisms.

The foundational review identifies RuBisCO, phosphoribulokinase and sedoheptulose-bisphosphatase as characteristic CBB activities and notes that some bacteria concentrate RuBisCO in carboxysomes. It also describes regulation of clustered `cbb` genes by CbbR in response to carbon and reduced-substrate availability. These are strong **CBB-branch** nodes, not universal chemoautotrophy requirements. (shively1998somethingfromalmost pages 3-5)

### Complexes, locations, and regulators

- Cytoplasmic membrane electron-transport chain.
- Proton-translocating respiratory complexes, terminal oxidases and ATP synthase.
- Carboxysome.
- CbbR and `cbb` operons.
- Sox sulfur-oxidation system; hydrogenases; ammonia monooxygenase and nitrite oxidoreductase as taxon-specific donor modules.
- Cytochrome bd and high-affinity terminal oxidases for low-oxygen or stress-adapted branches.
- MtrCAB and Gloeobacter rhodopsin only in an explicitly **engineered-system** branch.

### Environments, taxa, and assays

- Oxic–anoxic and sulfide–oxygen/nitrate interfaces; hydrothermal vents; hypoxic reservoirs; groundwater aquifers.
- Campylobacterales, Nautiliales, Halothiobacillales, Nitrospiraceae, ammonia-oxidizing archaea, sulfur oxidizers, and *Cupriavidus necator* as examples—not defining nodes.
- Strong phenotype assays: growth in inorganic-carbon mineral medium; substrate/acceptor consumption; biomass yield; ^13CO₂/^13C-bicarbonate incorporation; DNA-SIP; isotope-resolved metabolomics; respirometry.

## 3. Candidate causal edges

The table below is the proposed curation core. Its qualifications should be retained in YAML evidence notes.

| subject | predicate | object | proposed grounding | evidence DOI/year | short supporting snippet | confidence/qualification |
|---|---|---|---|---|---|---|
| Reduced inorganic compounds (H2, sulfide, thiosulfate, NH4+, NO2-, Fe2+) | enables | generation of precursor metabolites and energy | subject: H2 label-only; sulfide label-only; thiosulfate label-only; NH4+ label-only; NO2- label-only; Fe2+ label-only; object: GO:0006091 | 10.1146/annurev.micro.52.1.191 / 1998 | “key inorganic electron donors including H2, reduced sulfur compounds (H2S, S2O3²⁻), reduced nitrogen (NH4⁺, NO2⁻), and ferrous iron (Fe2⁺)” (shively1998somethingfromalmost pages 3-5) | High for broad trait scope; donor list is review-based and not universal to every taxon. |
| Oxygen | acts_as_terminal_electron_acceptor_for | aerobic electron transport chain | subject: label-only oxygen; object: GO:0019646 | 10.1146/annurev.micro.52.1.191 / 1998 | “Primary electron acceptors are oxygen and nitrate” (shively1998somethingfromalmost pages 3-5) | High for many chemoautotrophs; general review statement. |
| Nitrate | acts_as_terminal_electron_acceptor_for | nitrate-respiring energy metabolism | subject: label-only nitrate; object: label-only nitrate respiration | 10.1146/annurev.micro.52.1.191 / 1998 | “Primary electron acceptors are oxygen and nitrate” (shively1998somethingfromalmost pages 3-5) | Moderate; broad review support, but pathway modules are taxon-specific. |
| Inorganic electron oxidation | provides_reducing_power_for | carbon fixation | subject: label-only inorganic electron oxidation; object: GO:0015977 | 10.1186/s40168-023-01712-w / 2023 | “Chemolithoautotrophs convert CO2 to organic carbon via oxidation of reduced compounds” (deng2023strategiesofchemolithoautotrophs pages 1-2) | High for trait definition; mechanistic coupling exact route varies by lineage. |
| Ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCO) | participates_in | carbon fixation | subject: EC:4.1.1.39; object: GO:0015977 | 10.1146/annurev.micro.52.1.191 / 1998 | “The cycle is characterized by three unique enzymatic activities: ribulose bisphosphate carboxylase/oxygenase, phosphoribulokinase...” (shively1998somethingfromalmost pages 3-5) | High for CBB-based chemoautotrophs only; not universal across all chemoautotrophs. |
| Phosphoribulokinase | participates_in | carbon fixation | subject: EC:2.7.1.19; object: GO:0015977 | 10.1146/annurev.micro.52.1.191 / 1998 | “The cycle is characterized by three unique enzymatic activities: ribulose bisphosphate carboxylase/oxygenase, phosphoribulokinase...” (shively1998somethingfromalmost pages 3-5) | High for CBB-based chemoautotrophs only. |
| Carboxysome | localizes/concentrates | RuBisCO for carbon fixation | subject: label-only carboxysome; object: EC:4.1.1.39 | 10.1146/annurev.micro.52.1.191 / 1998 | “a number of bacteria package much of the enzyme into polyhedral organelles, the carboxysomes” (shively1998somethingfromalmost pages 3-5) | Moderate; strong for taxa with carboxysomes, absent from many others. |
| Calvin-Benson-Bassham cycle | realizes | carbon fixation | subject: label-only Calvin-Benson-Bassham cycle; object: GO:0015977 | 10.1146/annurev.micro.52.1.191 / 1998 | “CO2 fixation in the chemoautotroph occurs via the Calvin-Benson-Bassham cycle” (shively1998somethingfromalmost pages 3-5) | Moderate for historical/general framing; not exclusive because modern studies also show rTCA and Wood-Ljungdahl in some communities. |
| Reverse tricarboxylic acid cycle (rTCA) | realizes | carbon fixation | subject: label-only reverse TCA cycle; object: GO:0015977 | 10.1186/s40168-023-01712-w / 2023 | “Nautiliales... use NAD(H)-linked glutamate dehydrogenase to boost the reverse tricarboxylic acid (rTCA) cycle” (deng2023strategiesofchemolithoautotrophs pages 1-2) | High but taxon-specific to studied hydrothermal lineages. |
| NAD(H)-linked glutamate dehydrogenase | promotes | reverse tricarboxylic acid cycle | subject: label-only NAD(H)-linked glutamate dehydrogenase; object: label-only reverse TCA cycle | 10.1186/s40168-023-01712-w / 2023 | “Nautiliales were found to lack the Sox sulfur oxidation system and instead use NAD(H)-linked glutamate dehydrogenase to boost the reverse tricarboxylic acid (rTCA) cycle” (deng2023strategiesofchemolithoautotrophs pages 1-2) | Moderate; mechanistic and taxon-specific. |
| Sulfides (∑S2-) | serves_as_electron_donor_for | autotrophic denitrification | subject: label-only sulfides; object: label-only autotrophic denitrification | 10.1021/acs.est.4c00248 / 2024 | “Sulfide-driven denitrification relied on ∑S2- as the primary electron donor” (yang2024metagenomicsandstable pages 1-2) | High for this ecosystem process; reservoir-specific and supported by isotopes plus metagenomics, not pure-culture biochemistry. |
| Sulfide oxidation potential | positively_correlates_with | denitrification potential | subject: label-only sulfide oxidation; object: label-only denitrification | 10.1021/acs.est.4c00248 / 2024 | “a robust positive correlation between the metabolic potential of bacterial sulfide oxidation and denitrification (p < 0.05)” (yang2024metagenomicsandstable pages 1-2) | Moderate; correlation, not direct causal proof. |
| Campylobacterales | fixes | CO2 under 30-45 °C and very low pH | subject: label-only Campylobacterales; object: CHEBI:16526 | 10.1186/s40168-023-01712-w / 2023 | “Campylobacterales actively fixed carbon under both moderately and extremely acidic conditions under 30−45 °C” (deng2023strategiesofchemolithoautotrophs pages 1-2) | High but taxon- and assay-specific (13C-bicarbonate SIP incubations). |
| Increasing temperature to 45-65 °C at moderate acidity | increases | carbon fixation activity of Nautiliales | subject: label-only 45-65 °C moderate acidity; object: label-only carbon fixation activity | 10.1186/s40168-023-01712-w / 2023 | “carbon fixation activities of Nautiliales... significantly increased from 45 to 65 °C under moderately acidic condition” (deng2023strategiesofchemolithoautotrophs pages 1-2) | High but environmental-context specific. |
| Extreme acidity (pH 2.2) | reduces | heat tolerance of Nautiliales | subject: label-only acidic environment; object: label-only heat tolerance | 10.1186/s40168-023-01712-w / 2023 | “their heat tolerance was reduced under extremely acidic conditions” (deng2023strategiesofchemolithoautotrophs pages 1-2) | Moderate; adaptive phenotype in one hydrothermal system. |
| Reduced sulfur / ammonia / nitrite oxidation genes | indicates | chemoautotrophic carbon fixation potential | subject: label-only donor oxidation genes; object: GO:0015977 | 10.1038/s41598-024-68868-9 / 2024 | “Evidence shows inorganic electron donors (reduced sulfur, ammonia, nitrite) and acceptors (O₂, nitrate) support carbon fixation” (atencio2024metabolicadaptationsunderpin pages 6-8) | Moderate; metagenomic inference rather than direct physiology. |
| Calvin-Benson-Bassham / rTCA / Wood-Ljungdahl pathway genes | indicates | autotrophic capacity | subject: label-only autotrophic pathway genes; object: GO:0015977 | 10.1038/s41598-024-68868-9 / 2024 | “Sixty percent of MAGs encoded autotrophic carbon fixation genes, predominantly via the Calvin–Benson–Bassham (CBB) cycle, with some encoding reductive Krebs (rTCA) and Wood–Ljungdahl pathways” (atencio2024metabolicadaptationsunderpin pages 6-8) | Moderate; community MAG-based inference. |
| Extracellular electrons from electrode | regenerates | NADH/NADPH | subject: label-only extracellular electrons; object: label-only NADH/NADPH | 10.1038/s41467-023-43524-4 / 2023 | “NADH/NADPH regeneration from electrode-supplied electrons as the reducing power source” (tu2023engineeringartificialphotosynthesis pages 10-11) | High for engineered Cupriavidus system only. |
| Rhodopsin-driven proton motive force | powers | ATP synthesis | subject: label-only rhodopsin-driven proton motive force; object: label-only ATP synthesis | 10.1038/s41467-023-43524-4 / 2023 | “The light-activated proton pump - GR... powers ATP synthesis” (tu2023engineeringartificialphotosynthesis pages 10-11) | High for engineered system; not native trait mechanism. |
| MtrCAB-mediated extracellular electron uptake plus rhodopsin proton pumping | facilitates | CO2 fixation/biomass synthesis | subject: label-only MtrCAB+GR system; object: GO:0015977 | 10.1038/s41467-023-43524-4 / 2023 | “Employing GR and the outer-membrane conduit MtrCAB... facilitating R. eutropha’s biomass synthesis from CO2” (tu2023engineeringartificialphotosynthesis pages 10-11) | High for engineered proof-of-concept; not generalizable to native chemoautotrophs. |
| 13C-bicarbonate incorporation assay | evidences | active chemoautotrophic carbon fixation phenotype | subject: label-only 13C-bicarbonate incorporation assay; object: METPO:1000635 | 10.1186/s40168-023-01712-w / 2023 | “Combining the DNA-stable isotope probing technique... we identified active chemolithoautotrophs” (deng2023strategiesofchemolithoautotrophs pages 1-2) | High for phenotype evidence in environmental samples; activity assay, not isolate-level minimal definition. |
| Presence of inorganic electron-donor oxidation without autotrophic CO2 fixation | does_not_imply | chemoautotrophic phenotype | subject: label-only sulfur oxidation capacity; object: METPO:1000635 | 10.7939/r3-3c5n-dn16 / 2023 | “dissimilatory sulfur oxidation growth benefits were not observed, attributed to lack of autotrophic carbon fixation ability” (marc2023physiologicalandgenetic pages 98-103) | High as boundary-case warning; thesis source and methylotroph-specific. |


*Table: This table summarizes the strongest candidate causal edges for curating the chemoautotrophic trait METPO:1000635, with compact evidence snippets, grounding suggestions, and confidence qualifiers. It is designed to help prioritize graph edges that are directly supported versus those that are taxon-specific, inferred, or engineered.*

### Recommended minimal graph architecture

A taxon-neutral graph should encode:

1. **inorganic electron donor → oxidation module → electron transport**,  
2. **terminal acceptor → permits electron-transfer completion**,  
3. **electron transport → proton-motive force → ATP synthesis**,  
4. **electron flow/reverse electron transport → NADH or NADPH**,  
5. **ATP + reducing power + CO₂/HCO₃⁻ → carbon-fixation pathway**, and  
6. **carbon fixation → organic intermediates → biomass/growth → `METPO:1000635`**.

Donor-specific and fixation-pathway-specific mechanisms should be modeled as alternative branches rather than jointly necessary components.

## 4. Recent research, statistics, and applications

### Environmental chemoautotrophy

A 2023 hydrothermal-vent study used ^13C-bicarbonate DNA-SIP and metagenomics to identify active taxa. Nautiliales fixation increased at 45–65 °C under moderately acidic conditions, whereas Campylobacterales fixed carbon at 30–45 °C at both pH 5.6 and pH 2.2. Nautiliales lacked Sox in the reported reconstruction and instead showed an NAD(H)-linked glutamate-dehydrogenase association with rTCA metabolism. These findings support separate, explicitly taxon- and environment-qualified branches. (deng2023strategiesofchemolithoautotrophs pages 1-2)

A 2024 survey of ancient groundwater reconstructed 140 bacterial and eight archaeal MAGs. Approximately **60%** encoded autotrophic pathway genes, while measured chemosynthetic productivity ranged from **0.55 ± 0.06 to 0.82 ± 0.07 μg C L⁻¹ d⁻¹**. This supports an important subsurface-carbon-cycling role, but MAG content remains potential rather than isolate-level proof. (atencio2024metabolicadaptationsunderpin pages 6-8)

In a seasonally hypoxic reservoir, sulfide was identified as the principal donor supporting autotrophic denitrification. Sulfide-oxidation and denitrification potentials were positively correlated (**p < 0.05**), and the nitrate isotope-fractionation ratio ^15εNO3/^18εNO3 was **0.60**. The strongest defensible graph statement is ecosystem-specific coupling supported by isotope and metagenomic evidence—not direct proof of every intervening molecular edge. (yang2024metagenomicsandstable pages 1-2)

### Engineered carbon fixation

Tu et al. engineered *C. necator* with MtrCAB-mediated extracellular electron uptake and a light-driven proton-pumping rhodopsin. Electrode electrons supplied reducing equivalents, while rhodopsin-supported proton motive force supplied ATP; the design thereby drove CO₂-dependent biomass synthesis. Experiments included an electrode potential of −500 mV versus Ag/AgCl, approximately 150 μmol photons m⁻² s⁻¹ illumination, and 100 μM CCCP perturbation. This is a mechanistically informative implementation but should be stored outside the native trait core. (tu2023engineeringartificialphotosynthesis pages 10-11)

Li et al. engineered *C. necator* to produce one succinate from one acetyl-CoA plus two CO₂ through part of the 3-hydroxypropionate cycle. Isotope evidence indicated that **50% of succinate carbon** came from CO₂. ATP/NADPH and metabolic-burden optimization produced **3.6 g L⁻¹**, a **159%** improvement over the starting strain; at 2-L scale the yield was **0.24 g g⁻¹ fatty acid**, only **10.12%** of the calculated theoretical maximum. This demonstrates practical CO₂ incorporation but is not pure chemoautotrophic growth because fatty acid supplies substantial carbon and energy. (li2024productionofsuccinate pages 10-11, li2024productionofsuccinate pages 1-2)

## 5. Expert synthesis for curation

The strongest contemporary interpretation is modular rather than pathway-essentialist. Chemoautotrophy is an emergent physiological state produced by coupling an inorganic redox module to one of several autotrophic carbon-assimilation modules. RuBisCO or `cbb` genes are excellent markers for the CBB implementation, but absence of CBB does not exclude the trait; conversely, carbon-fixation genes without donor oxidation and energy-conservation evidence do not establish chemoautotrophy. Direct isotope incorporation combined with growth and donor/acceptor turnover is the preferred evidence standard. (deng2023strategiesofchemolithoautotrophs pages 1-2, atencio2024metabolicadaptationsunderpin pages 6-8, shively1998somethingfromalmost pages 3-5)

## 6. Warnings—claims not yet suitable for unqualified curation

1. **Do not encode CBB as the sole universal fixation route.** The older review emphasizes CBB, whereas current environmental genomics identifies rTCA and Wood–Ljungdahl alternatives. (atencio2024metabolicadaptationsunderpin pages 6-8, shively1998somethingfromalmost pages 3-5)
2. **Do not infer phenotype from MAGs or marker genes alone.** MAG results support metabolic potential, not demonstrated flux or growth.
3. **Do not infer chemoautotrophy from Sox, hydrogenase, `amo`, or `nxr` alone.** Inorganic donor oxidation can occur without autotrophic fixation; the Methylococcales boundary case demonstrates this explicitly. (marc2023physiologicalandgenetic pages 98-103)
4. **Do not convert correlation into a molecular causal edge.** The reservoir sulfide–denitrification association is strong but ecosystem-level. (yang2024metagenomicsandstable pages 1-2)
5. **Do not universalize environmental optima.** pH and temperature responses in Campylobacterales and Nautiliales are lineage- and incubation-specific. (deng2023strategiesofchemolithoautotrophs pages 1-2)
6. **Keep engineered modules separate.** MtrCAB, rhodopsin, electrode potential, and the partial 3HP succinate pathway are implementations, not natural requirements. (tu2023engineeringartificialphotosynthesis pages 10-11, li2024productionofsuccinate pages 1-2)
7. **Avoid asserting strict autotrophy from partial CO₂ incorporation.** Anaplerotic fixation or mixotrophic product synthesis can incorporate labeled CO₂ without satisfying the trait definition.
8. **Validate all ontology identifiers before YAML insertion.** Label-only nodes are preferable to invented or obsolete CURIEs.

## DOI-first bibliography

- Deng W. et al. “Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem.” *Microbiome* (December 2023). DOI: [10.1186/s40168-023-01712-w](https://doi.org/10.1186/s40168-023-01712-w). (deng2023strategiesofchemolithoautotrophs pages 1-2)
- Tu W. et al. “Engineering artificial photosynthesis based on rhodopsin for CO₂ fixation.” *Nature Communications* (December 2023). DOI: [10.1038/s41467-023-43524-4](https://doi.org/10.1038/s41467-023-43524-4). (tu2023engineeringartificialphotosynthesis pages 10-11)
- Yang M. et al. “Metagenomics and Stable Isotopes Uncover the Augmented Sulfide-Driven Autotrophic Denitrification in a Seasonally Hypoxic, Sulfate-Abundant Reservoir.” *Environmental Science & Technology* 58, 14225–14236 (July 2024). DOI: [10.1021/acs.est.4c00248](https://doi.org/10.1021/acs.est.4c00248). (yang2024metagenomicsandstable pages 1-2)
- Atencio B. et al. “Metabolic adaptations underpin high productivity rates in relict subsurface water.” *Scientific Reports* (August 2024). DOI: [10.1038/s41598-024-68868-9](https://doi.org/10.1038/s41598-024-68868-9). (atencio2024metabolicadaptationsunderpin pages 6-8)
- Li L. et al. “Production of succinate with two CO₂ fixation reactions from fatty acids in *Cupriavidus necator* H16.” *Microbial Cell Factories* (July 2024). DOI: [10.1186/s12934-024-02470-6](https://doi.org/10.1186/s12934-024-02470-6). (li2024productionofsuccinate pages 7-10, li2024productionofsuccinate pages 10-11, li2024productionofsuccinate pages 1-2)
- Waddingham M. “Physiological and Genetic Investigations into Putative Sulfur Oxidation Systems of Methylococcales.” University of Alberta thesis (2023). DOI: [10.7939/r3-3c5n-dn16](https://doi.org/10.7939/r3-3c5n-dn16). (marc2023physiologicalandgenetic pages 98-103)
- Shively J.M., van Keulen G., Meijer W.G. “Something from almost nothing: carbon dioxide fixation in chemoautotrophs.” *Annual Review of Microbiology* 52, 191–230 (October 1998). DOI: [10.1146/annurev.micro.52.1.191](https://doi.org/10.1146/annurev.micro.52.1.191). (shively1998somethingfromalmost pages 3-5)

References

1. (shively1998somethingfromalmost pages 3-5): Jessup M. Shively, Geertje van Keulen, and Wim G. Meijer. Something from almost nothing: carbon dioxide fixation in chemoautotrophs. Annual review of microbiology, 52:191-230, Oct 1998. URL: https://doi.org/10.1146/annurev.micro.52.1.191, doi:10.1146/annurev.micro.52.1.191. This article has 357 citations and is from a peer-reviewed journal.

2. (marc2023physiologicalandgenetic pages 98-103): Marc Waddingham. Physiological and genetic investigations into putative sulfur oxidation systems of methylococcales. Text, 2023. URL: https://doi.org/10.7939/r3-3c5n-dn16, doi:10.7939/r3-3c5n-dn16. This article has 0 citations and is from a peer-reviewed journal.

3. (atencio2024metabolicadaptationsunderpin pages 6-8): Betzabe Atencio, Eyal Geisler, Maxim Rubin-Blum, Edo Bar-Zeev, Eilon M. Adar, Roi Ram, and Zeev Ronen. Metabolic adaptations underpin high productivity rates in relict subsurface water. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-68868-9, doi:10.1038/s41598-024-68868-9. This article has 3 citations and is from a peer-reviewed journal.

4. (deng2023strategiesofchemolithoautotrophs pages 1-2): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 17 citations and is from a highest quality peer-reviewed journal.

5. (yang2024metagenomicsandstable pages 1-2): Mengdi Yang, Qianli Luo, Zhongya Fan, Fantang Zeng, Lu Huang, Shiyuan Ding, Gaoyang Cui, Dongli Li, Gangjian Wei, Cong-Qiang Liu, and Xiao-Dong Li. Metagenomics and stable isotopes uncover the augmented sulfide-driven autotrophic denitrification in a seasonally hypoxic, sulfate-abundant reservoir. Environmental science & technology, 58:14225-14236, Jul 2024. URL: https://doi.org/10.1021/acs.est.4c00248, doi:10.1021/acs.est.4c00248. This article has 23 citations and is from a domain leading peer-reviewed journal.

6. (tu2023engineeringartificialphotosynthesis pages 10-11): Weiming Tu, Jiabao Xu, Ian P. Thompson, and Wei E. Huang. Engineering artificial photosynthesis based on rhodopsin for co2 fixation. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43524-4, doi:10.1038/s41467-023-43524-4. This article has 76 citations and is from a highest quality peer-reviewed journal.

7. (li2024productionofsuccinate pages 10-11): Linqing Li, Xiuyuan Zhou, Zhuoao Gao, Peng Xiong, and Xiutao Liu. Production of succinate with two co2 fixation reactions from fatty acids in cupriavidus necator h16. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02470-6, doi:10.1186/s12934-024-02470-6. This article has 13 citations and is from a peer-reviewed journal.

8. (li2024productionofsuccinate pages 1-2): Linqing Li, Xiuyuan Zhou, Zhuoao Gao, Peng Xiong, and Xiutao Liu. Production of succinate with two co2 fixation reactions from fatty acids in cupriavidus necator h16. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02470-6, doi:10.1186/s12934-024-02470-6. This article has 13 citations and is from a peer-reviewed journal.

9. (li2024productionofsuccinate pages 7-10): Linqing Li, Xiuyuan Zhou, Zhuoao Gao, Peng Xiong, and Xiutao Liu. Production of succinate with two co2 fixation reactions from fatty acids in cupriavidus necator h16. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02470-6, doi:10.1186/s12934-024-02470-6. This article has 13 citations and is from a peer-reviewed journal.