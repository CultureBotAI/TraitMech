---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:48:50.388951'
end_time: '2026-08-04T10:56:33.840889'
duration_seconds: 463.45
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemolithoautotrophic
  trait_identifier: METPO:1000637
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemolithoautotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from oxidation of
    inorganic compounds (lithotrophy) and carbon from carbon dioxide.
  parent_traits: METPO:1000631
  synonyms: chemolithoautotroph
  evidence_summary: 'DOI:10.1146/annurev.micro.52.1.191: physiology ... of chemoautotrophic
    bacteria (Review supports chemoautotrophic bacterial CO2 fixation.) | DOI:10.1016/B978-0-12-378630-2.00219-X:
    growth-supporting reductant and energy source (Review supports inorganic reductants
    as energy sources for chemolithotrophic growth.)'
  causal_graph_summary: 'chemolithoautotrophic_energy_and_fixation: 13 nodes, 14 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemolithoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000637
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds (lithotrophy) and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: physiology ... of chemoautotrophic bacteria (Review supports chemoautotrophic bacterial CO2 fixation.) | DOI:10.1016/B978-0-12-378630-2.00219-X: growth-supporting reductant and energy source (Review supports inorganic reductants as energy sources for chemolithotrophic growth.)
- **Existing causal graph summary:** chemolithoautotrophic_energy_and_fixation: 13 nodes, 14 edges

## Research Objective

Research the microbial trait **chemolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithoautotrophic.yaml`.

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
- **Trait label:** chemolithoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000637
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds (lithotrophy) and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: physiology ... of chemoautotrophic bacteria (Review supports chemoautotrophic bacterial CO2 fixation.) | DOI:10.1016/B978-0-12-378630-2.00219-X: growth-supporting reductant and energy source (Review supports inorganic reductants as energy sources for chemolithotrophic growth.)
- **Existing causal graph summary:** chemolithoautotrophic_energy_and_fixation: 13 nodes, 14 edges

## Research Objective

Research the microbial trait **chemolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithoautotrophic.yaml`.

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


# Curation report: chemolithoautotrophic

**Trait:** chemolithoautotrophic  
**Identifier:** **METPO:1000637**  
**Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED  
**Parent:** METPO:1000631  
**Recommended interpretation:** a trophic phenotype in which oxidation of one or more inorganic electron donors supplies energy and reducing equivalents, while CO2/HCO3− supplies most or all assimilated carbon.

## 1. Scope and boundaries

Chemolithoautotrophy is best modeled as a **compound physiological capacity**, not as a single pathway. Its invariant causal architecture is:

**inorganic electron donor oxidation → electron transfer/ion-motive force → ATP and reducing equivalents → inorganic-carbon uptake and fixation → biomass.**

The interchangeable branches are the donor, terminal electron acceptor, respiratory components, and carbon-fixation pathway. Current examples include oxidation of H2, reduced sulfur compounds, Fe2+, ammonia, nitrite, and—in two unusual strict anaerobes—phosphite. Carbon assimilation may use the Calvin–Benson–Bassham (CBB), reductive TCA (rTCA), Wood–Ljungdahl (WL), 3-hydroxypropionate bicycle, 3-hydroxypropionate–4-hydroxybutyrate (3HP–4HB), or dicarboxylate–4-hydroxybutyrate pathway. DIC transport and carbonic-anhydrase systems bridge environmental CO2/HCO3− supply to these pathways. (scott2024widespreaddissolvedinorganic pages 10-13, scott2024widespreaddissolvedinorganic pages 2-4, prioretti2023carbonfixationin pages 1-2, mao2023anaerobicdissimilatoryphosphite pages 1-2)

### Boundary cases

- **Chemolithotrophy without autotrophy:** oxidation of inorganic donors is insufficient by itself; demonstrated incorporation of inorganic carbon into biomass is required.
- **Chemoorganoautotrophy:** chemical energy is retained, but an organic electron donor violates the lithotrophic component.
- **Photoautotrophy:** light, rather than oxidation of an inorganic chemical, is the principal energy source. The engineered rhodopsin/electrode system in *Cupriavidus necator* is therefore photoelectroautotrophic, not a clean natural instance of the target trait. (tu2023engineeringartificialphotosynthesis pages 1-2)
- **Electroautotrophy:** electrons supplied directly by an electrode constitute a distinct energy-input mode. *Acidithiobacillus ferrooxidans* can switch between Fe2+-dependent chemoautotrophy and electrode-dependent electroautotrophy; the latter showed slower growth and altered electron-uptake machinery. These modes should not be merged in the core trait graph. (wang2024characterizethegrowth pages 22-23)
- **Mixotrophy/facultative autotrophy:** organisms that simultaneously or alternatively assimilate organic carbon should receive the trait only when chemolithoautotrophic growth is experimentally demonstrated under the relevant condition.
- **Methane oxidation:** although CH4 is reduced and geochemically simple, it is conventionally an organic C1 substrate. Methanotrophy should not automatically be curated as lithotrophy.
- **Genomic potential:** marker genes alone establish potential, not the observed phenotype. Stable-isotope incorporation, growth with CO2 as carbon source, donor consumption, or pathway biochemistry provides stronger support.

## 2. Candidate nodes

Identifiers below are deliberately conservative. Stable identifiers are supplied only where confidence is high; otherwise a label-only node is preferable to an invented or over-specific CURIE.

### Trait and biological-process nodes

- **chemolithoautotrophic** — **METPO:1000637**
- chemolithotrophy — parent or related METPO term should be resolved against the local ontology release
- carbon fixation — **GO:0015977**
- aerobic respiration — **GO:0009060**
- proton transmembrane transport — **GO:1902600**
- ATP synthesis coupled proton transport — **GO:0015986**
- nitrification — label-only unless the project’s preferred process ontology is established
- sulfur oxidation, hydrogen oxidation, ferrous-iron oxidation, phosphite oxidation — label-only process nodes pending ontology verification

### Chemicals and environmental substrates

- carbon dioxide — **CHEBI:16526**
- hydrogencarbonate/bicarbonate — **CHEBI:17544**
- dihydrogen — **CHEBI:18276**
- dioxygen — **CHEBI:15379**
- ammonia — **CHEBI:16134**
- ammonium — **CHEBI:28938**
- nitrite — **CHEBI:16301**
- nitrate — **CHEBI:17632**
- sulfide — **CHEBI:26822**
- hydrogen sulfide — **CHEBI:16136**
- thiosulfate — **CHEBI:26977**
- iron(2+) — **CHEBI:29033**
- iron(3+) — **CHEBI:29034**
- phosphite, phosphate, elemental sulfur, sulfate, NADH, NADPH, ATP, proton motive force — retain as labels until CURIEs are checked against the project’s exact ChEBI release
- environmental parameters: oxygen concentration, pH, temperature, inorganic-donor concentration, CO2/HCO3− availability, salinity, heavy metals

### Enzymes, proteins, transporters, and complexes

- ammonia monooxygenase / **amoCAB** — **EC:1.14.99.39**
- hydroxylamine oxidoreductase / **hao** — **EC:1.7.2.6**; applicable to characterized bacterial systems, not as the unresolved archaeal hydroxylamine-oxidation enzyme
- nitrite oxidoreductase / **nxrAB** — label plus EC only after reaction-direction review
- ribulose-1,5-bisphosphate carboxylase/oxygenase / **rbcL-rbcS** — **GO:0016984**; EC assignment depends on form
- carbonic anhydrase — **GO:0004089**, **EC:4.2.1.1**
- bicarbonate transporters **SbtA**, **BicA/SulP**, **CmpABCD**
- carboxysome and carboxysomal carbonic anhydrase **CsoSCA**
- pyruvate:ferredoxin oxidoreductase (**PFOR**)
- 2-oxoglutarate:ferredoxin oxidoreductase (**OGOR**)
- low-potential [4Fe–4S] ferredoxins **Fd6/Fd7**—taxon-specific proteins in *Aquifex aeolicus*
- cytochrome **Cyc2** and rusticyanin **Rus**—taxon-specific Fe2+-oxidation chain in *A. ferrooxidans*
- Sox sulfur-oxidation system; APS reductase; reverse-DSR components
- hydrogenase
- NADH:quinone oxidoreductase/respiratory complex I
- cytochrome bd ubiquinol oxidase
- F-type or A/V-type ATP synthase
- NAD+-dependent phosphorylating phosphite dehydrogenase
- carbon monoxide dehydrogenase/acetyl-CoA synthase complex of the WL pathway

### Pathways and modules

- inorganic-electron-donor oxidation module
- respiratory electron-transport chain
- proton- or sodium-motive-force generation
- ATP synthesis and reverse electron transport
- CBB cycle
- rTCA cycle
- WL/reductive acetyl-CoA pathway
- 3-hydroxypropionate bicycle
- 3HP–4HB cycle
- dicarboxylate–4-hydroxybutyrate cycle
- dissolved-inorganic-carbon uptake and carbon-concentrating mechanism

### Cellular locations

- extracellular/periplasmic donor-oxidation interface
- outer membrane and periplasm—especially Cyc2/Rus and engineered MtrCAB cases
- cytoplasmic membrane respiratory chain
- cytoplasm
- carboxysome

## 3. Candidate evidence-backed edges

The following table is the recommended starting set. “Strong” means direct physiology, biochemistry, or a well-established enzyme reaction; “conditional” indicates taxon-, pathway-, reactor-, or engineering-specific evidence.

| Subject | Predicate | Object | Scope/evidence strength | Supporting snippet | DOI |
|---|---|---|---|---|---|
| Chemolithoautotrophic metabolism | derives energy from oxidation of | inorganic compounds while fixing CO2 | Broad trait scope; strong review/physiology support | "non-photosynthetic microbes are versatile in terms of energy utilization as they can obtain energy from inorganic compounds instead of light and use it to fix carbon in metabolic pathways like the Calvin cycle, the Wood-Ljungdahl pathway (WLP), the 3-hydroxypropionate-4-hydroxybutyrate (3HP-4HB) cycle" (alvarez‐guzman2023effectofelectron pages 1-2) | 10.1111/1751-7915.14353 |
| Inorganic electron donors | support | CO2 fixation / chemolithoautotrophic growth | Broad but partly community-level; strong physiology | "Na2S, MnCl2, NaNO2, NH4Cl, Na2S2O3, and FeCl2 were used as energy source for CO2 fixation"; "Na2S the best electron donor evaluated (100% of CO2 consumption)" (alvarez‐guzman2023effectofelectron pages 1-2) | 10.1111/1751-7915.14353 |
| Fe2+ oxidation | transfers electrons via | Cyc2 → rusticyanin (Rus) | Taxon-specific to *Acidithiobacillus ferrooxidans*; strong mechanistic physiology | A. ferrooxidans "derives energy from Fe2+ or reduced inorganic sulfur compounds (RISCs) oxidation"; electron transport includes "Fe2+ oxidation to Fe3+ by outer-membrane cytochrome c (Cyc2), electron flow to rusticyanin (Rus)" (wang2024characterizethegrowth pages 1-2) | 10.3390/microorganisms12030590 |
| Ammonia monooxygenase (AMO) | oxidizes | ammonia to hydroxylamine | Broad nitrifier mechanism; strong review support | "All ammonia oxidizers generate energy by oxidizing ammonia to hydroxylamine by the enzyme ammonia monooxygenase" (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2) | 10.1128/aem.01698-23 |
| Hydroxylamine oxidation system | oxidizes | hydroxylamine to nitrite | Strong for AOB/comammox; unresolved in AOA | "Hydroxylamine gets further oxidized to nitrite by the hydroxylamine oxidoreductase and an unknown enzyme in AOB and comammox"; "In AOA, the enzymes for the oxidation of hydroxylamine to nitrite have not been identified yet" (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2) | 10.1128/aem.01698-23 |
| Nitrite oxidoreductase (NXR) | oxidizes | nitrite to nitrate | Broad nitrifier mechanism; strong review support | "NOB and comammox use the enzyme nitrite oxidoreductase to oxidize nitrite to nitrate" (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2) | 10.1128/aem.01698-23 |
| Complete ammonia oxidation (comammox) | yields | more energy per mole ammonia than partial ammonia oxidation | Comparative physiology; strong but taxon-group level | "By oxidizing ammonia all the way to nitrate, comammox can generate more energy per molecule of ammonia than AOA and AOB" (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2) | 10.1128/aem.01698-23 |
| Electron transport chain (ETC) | generates | proton motive force (PMF) | Engineered system but mechanistically explicit; moderate strength for generic edge | "extracellular electrons and GR-driven proton motive force are integrated into R. eutropha’s native electron transport chain (ETC)" (tu2023engineeringartificialphotosynthesis pages 1-2) | 10.1038/s41467-023-43524-4 |
| Proton motive force | powers | ATP synthesis | Engineered system; strong direct statement | "The light-activated proton pump - GR... powers ATP synthesis" (tu2023engineeringartificialphotosynthesis pages 1-2) | 10.1038/s41467-023-43524-4 |
| Reverse electron transport through ETC | regenerates | NADH/NADPH | Engineered system; strong direct statement | "powers ATP synthesis and reverses the ETC to regenerate NADH/NADPH, facilitating R. eutropha’s biomass synthesis from CO2" (tu2023engineeringartificialphotosynthesis pages 1-2) | 10.1038/s41467-023-43524-4 |
| Bicarbonate transporters (e.g., SbtA, BicA/SulP, CmpABCD) | import | HCO3− into the cell | Review-derived across autotrophs; strong synthesis | "Bicarbonate transporters acquire extracellular HCO3−" and "Bicarbonate transporters (SbtA, BicA/SulP, CmpABCD) work... to accumulate elevated intracellular HCO3− concentrations" (scott2024widespreaddissolvedinorganic pages 10-13, scott2024widespreaddissolvedinorganic pages 2-4) | 10.1128/aem.01557-23 |
| Carbonic anhydrase | interconverts | CO2 and HCO3− | Review-derived across autotrophs; strong synthesis | "Carbonic anhydrases (CA) catalyze rapid CO2/HCO3− interconversion" (scott2024widespreaddissolvedinorganic pages 2-4) | 10.1128/aem.01557-23 |
| Carboxysomal carbonic anhydrase | supplies | CO2 to RubisCO inside carboxysomes | Strong review support for CBB autotrophs | "HCO3− is transported into carboxysomes where carboxysomal CA converts it to CO2 for RubisCO fixation" (scott2024widespreaddissolvedinorganic pages 2-4) | 10.1128/aem.01557-23 |
| RubisCO / Calvin-Benson-Bassham cycle | fixes | CO2 into biomass | Strong review/physiology support | A. ferrooxidans "fixing atmospheric CO2 via the Calvin-Benson-Bassham (CBB) cycle" (wang2024characterizethegrowth pages 1-2) | 10.3390/microorganisms12030590 |
| Fd6/Fd7 ferredoxins | donate electrons to | PFOR and OGOR | Taxon-specific biochemical/proteomic evidence; strong | "Fd6 and Fd7... can physically interact and exchange electrons with both PFOR and OGOR, suggesting that they could be the physiological electron donors" (prioretti2023carbonfixationin pages 1-2) | 10.3390/life13030627 |
| PFOR | catalyzes | reductive carboxylation of acetyl-CoA to pyruvate | Taxon-specific biochemical evidence; strong | "PFOR... [is] responsible... for the reductive carboxylation of acetyl-CoA to pyruvate" (prioretti2023carbonfixationin pages 1-2) | 10.3390/life13030627 |
| OGOR | catalyzes | reductive carboxylation of succinyl-CoA to 2-oxoglutarate | Taxon-specific biochemical evidence; strong | "OGOR... [is] responsible... for the reductive carboxylation of... succinyl-CoA to 2-oxoglutarate" (prioretti2023carbonfixationin pages 1-2) | 10.3390/life13030627 |
| NAD+-dependent phosphite dehydrogenase | oxidizes phosphite to produce | NADH that feeds Wood-Ljungdahl CO2 fixation | Mini-review; strong mechanistic summary, anaerobe-specific | "The produced NADH is channelled into autotrophic CO2 fixation via the Wood-Ljungdahl (CO-DH) pathway" (mao2023anaerobicdissimilatoryphosphite pages 1-2) | 10.1111/1462-2920.16470 |
| Temperature and pH | constrain | taxon-specific carbon fixation activity | Taxon-specific environmental physiology; strong | "Nautiliales... carbon fixation activities... significantly increased from 45 to 65 °C under moderately acidic condition" while "Campylobacterales actively fixed carbon under both moderately and extremely acidic conditions under 30−45 °C" (deng2023strategiesofchemolithoautotrophs pages 1-2) | 10.1186/s40168-023-01712-w |


*Table: Compact curation-ready causal edges for the chemolithoautotrophic trait, limited to evidence retrieved in this conversation. The table emphasizes mechanistic entities, exact support snippets, and flags where claims are taxon-specific, review-derived, engineered, or unresolved.*

### Additional interpretation for curation

1. **Use a small universal backbone.** The safest generic edges are donor oxidation → electron flow; electron transport → ion-motive force; ion-motive force → ATP synthesis/reducing power; DIC uptake/interconversion → carbon-fixation pathway; carbon fixation → biomass. Donor-specific proteins and carbon-fixation enzymes should be represented as alternative branches, not universal requirements.

2. **Keep ammonia-oxidizer branches taxonomically explicit.** Ammonia is the preferred AMO substrate, and archaeal ammonia affinities span at least four orders of magnitude: apparent Km values exceed 12 µM in some *Nitrosocosmicus* representatives but are below 2.8 nM in some Nitrosopumilales and “Ca. Nitrosotaleales.” This is strong evidence that donor concentration is a causal ecological selector, but not a universal threshold for the trait. (wright2023nitrificationandbeyond pages 1-2)

3. **Separate pathway chemistry from taxon distributions.** AOB generally use CBB, AOA use 3HP–4HB, and comammox *Nitrospira* use rTCA. In a 2024 competition experiment, comammox *Nitrospira* BO4 outcompeted an AOA enrichment at both 50 and 500 µM initial ammonium; the authors attributed the result to complete ammonia-to-nitrate oxidation and the more energy-efficient rTCA pathway. This is valuable ecological causation but remains strain- and assay-specific. (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2)

4. **DIC-toolkit edges need graded evidence.** Carbonic anhydrase directly catalyzes CO2/HCO3− interconversion, and established bicarbonate transporters import HCO3−. Carboxysomal CA supplies concentrated CO2 to RubisCO and raises the CO2:O2 ratio, favoring carboxylation. By contrast, inferred coupling of transporter/CA genes to non-CBB pathways is mostly comparative-genomic and should be marked uncertain. (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 4-7, scott2024widespreaddissolvedinorganic pages 15-18)

## 4. Recent developments and quantitative evidence

### Direct biochemical resolution of rTCA electron delivery

Prioretti et al. showed biochemically and proteomically that obligately chemolithoautotrophic *A. aeolicus* uses abundant pentameric PFOR and OGOR complexes. Fd6 and Fd7 had redox potentials of −440 and −460 mV and physically interacted and exchanged electrons with both enzymes. PFOR fixes CO2 by reductively carboxylating acetyl-CoA to pyruvate; OGOR carboxylates succinyl-CoA to 2-oxoglutarate. This is among the strongest recent sources for explicit molecular edges linking reducing power to carbon fixation. Published 23 February 2023. (prioretti2023carbonfixationin pages 14-16, prioretti2023carbonfixationin pages 1-2)

### DIC supply is broader than classical carboxysomes

A 2024 synthesis found bicarbonate transporters and carbonic anhydrases across organisms using all six recognized autotrophic pathways and habitats spanning approximately pH 1–11. It argues that DIC acquisition—not only the catalytic fixation cycle—can constrain autotrophy. Yet many non-CBB assignments remain predictions from gene occurrence and neighborhood rather than biochemical demonstrations. Published February 2024. (scott2024widespreaddissolvedinorganic pages 10-13, scott2024widespreaddissolvedinorganic pages 4-7, scott2024widespreaddissolvedinorganic pages 18-19)

### Multi-donor vent chemolithoautotrophy

Three 2024 *Hydrogenovibrio* isolates oxidized sulfur, H2, and Fe(II). Reported ^14C-fixation rates were 4×10−7 to 20×10−7 mmol C mL−1 h−1. Vent-scale maximum estimates for one strain were 10, 24, and 952 mmol h−1 for iron, hydrogen, and thiosulfate oxidation and 0.3, 1, and 84 mmol CO2 h−1, respectively. No recognized Fe(II)-oxidation genes were detected, so the responsible pathway remains unknown and should not be assigned to a named enzyme. Published 2024. (laufermeiser2024oxidationofsulfur pages 9-10)

### Temperature–pH interactions

DNA-stable-isotope probing in acidic shallow vents showed increased *Nautiliales* fixation from 45 to 65°C at pH 5.6, whereas *Campylobacterales* fixed carbon at 30–45°C under both pH 5.6 and pH 2.2. *Nautiliales* lacked Sox genes and showed evidence for rTCA support through NAD(H)-linked glutamate dehydrogenase; proton-export, K+ accumulation, membrane-barrier, and transport functions were associated with extreme-acid adaptation in *Campylobacterales*. These are environmental and taxon-specific branches, not defining requirements. Published December 2023. (deng2023strategiesofchemolithoautotrophs pages 1-2)

### Rare phosphite-driven autotrophy

Only two pure cultures were reported to use phosphite dissimilatorily under strict anoxia: *Phosphitispora fastidiosa* and *Desulfotignum phosphitoxidans*. Phosphite oxidation occurs at an unusually low redox potential, approximately −690 mV at pH 7; a phosphorylating NAD+-dependent phosphite dehydrogenase produces NADH, which is directed into WL carbon fixation, allowing nearly complete incorporation of substrate electrons into biomass. Published August 2023. (mao2023anaerobicdissimilatoryphosphite pages 1-2)

## 5. Applications and real-world implementation

### Industrial flue-gas carbon capture

A non-photosynthetic microbial community treated model cement flue gas containing CO2/O2/N2 at 4.2:13.5:82.3% v/v. After 45 days of acclimation it reached 100% CO2 removal. Among Na2S, MnCl2, NaNO2, NH4Cl, Na2S2O3, and FeCl2, Na2S gave 100% CO2 consumption and FeCl2 28%; a continuous Na2S-fed biotrickling filter reached 77%. Acetate and propionate were major products, and pathway inference implicated 3HP–4HB and WL. Because this was a mixed community and pathway identity was inferred, curate the reactor-level donor → CO2-removal edge, but not organism-specific pathway edges. Accepted 25 September 2023. (alvarez‐guzman2023effectofelectron pages 1-2)

### Biomining and metal recovery

*A. ferrooxidans* couples Fe2+ or reduced-sulfur oxidation to CBB carbon fixation and is used for bioleaching copper and other sulfide ores and for processing electronic waste. It grows optimally near pH 2 and 30°C. In its Fe2+ chain, Cyc2 transfers electrons toward rusticyanin, with approximately 95% entering the downhill respiratory branch. These edges are appropriate only for the *A. ferrooxidans*/acidophilic iron-oxidizer subgraph. (wang2024characterizethegrowth pages 1-2)

### Wastewater nitrogen removal

Chemolithoautotrophic nitrifiers operate in drinking-water, wastewater, tertiary-treatment, and aquaculture systems. AMO, HAO-associated bacterial hydroxylamine oxidation, and NXR provide direct mechanistic nodes for converting ammonia through nitrite to nitrate. Environmental controls include ammonium availability, oxygen, pH, salinity, temperature, organic matter, metals, light, and inhibitors. AOA and comammox often dominate oligotrophic settings, but competitive outcomes are strain- and reactor-dependent. (wright2023nitrificationandbeyond pages 1-2, ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2)

### Engineered carbon fixation and electrosynthesis

In engineered *C. necator*, MtrCAB enabled extracellular electron uptake; Gloeobacter rhodopsin generated proton motive force; that force powered ATP synthesis and reverse electron transport to NADH/NADPH; and carbonic-anhydrase overexpression enhanced fixation. This is an authoritative proof-of-concept for engineering individual energy/fixation modules, but its light-plus-electrode energy supply places it outside strict natural chemolithoautotrophy. Published December 2023. (tu2023engineeringartificialphotosynthesis pages 1-2)

## 6. Expert synthesis for the TraitMech graph

The literature supports a **modular graph rather than a taxon-independent gene signature**. The most defensible central graph is:

1. inorganic donor availability enables donor-specific oxidation;
2. oxidation injects electrons into a membrane or soluble redox chain;
3. electron transfer supports terminal-acceptor reduction and generates an ion gradient;
4. the gradient drives ATP synthesis and, where necessary, reverse electron transport for NAD(P)H or reduced ferredoxin;
5. transporters and carbonic anhydrases establish usable intracellular DIC;
6. one of several fixation pathways converts DIC into central metabolites;
7. ATP and reductant support biomass synthesis.

No single donor, acceptor, fixation cycle, oxygen requirement, or enzyme is universal. The graph should therefore use **OR branches** or taxon/condition-qualified subgraphs. The strongest recent molecular branch is Fd6/Fd7 → PFOR/OGOR → rTCA carboxylation in *A. aeolicus*. The strongest process-scale demonstration is sulfide-supported cement-flue-gas CO2 removal. The most important unresolved areas are archaeal hydroxylamine oxidation, *Hydrogenovibrio* Fe(II) oxidation, and the functions of many non-CBB DIC-toolkit genes. (laufermeiser2024oxidationofsulfur pages 9-10, scott2024widespreaddissolvedinorganic pages 4-7, prioretti2023carbonfixationin pages 1-2, ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2)

## 7. Warnings: claims not yet suitable for unqualified curation

- Do **not** encode CH4 as a generic inorganic electron donor.
- Do **not** make oxygen a required acceptor; nitrate and other acceptors support anaerobic branches.
- Do **not** assert that all chemolithoautotrophs use CBB/RubisCO, carboxysomes, Sox, reverse DSR, hydrogenases, or complex I.
- Do **not** assign a known Fe(II)-oxidation enzyme to the 2024 *Hydrogenovibrio* strains; the pathway was explicitly unresolved. (laufermeiser2024oxidationofsulfur pages 9-10)
- Do **not** assign bacterial HAO as the archaeal hydroxylamine-to-nitrite catalyst; the responsible AOA enzymes remain unidentified. (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2)
- Treat non-CBB carbonic-anhydrase/transporter coupling as **genome-inferred** unless supported by physiology or genetics. (scott2024widespreaddissolvedinorganic pages 4-7, scott2024widespreaddissolvedinorganic pages 15-18)
- Treat the flue-gas 3HP–4HB and WL pathway assignments as **community-level inferred pathways**, not verified organism-specific mechanisms. (alvarez‐guzman2023effectofelectron pages 1-2)
- Treat the *C. necator* MtrCAB/rhodopsin chain as **engineered photoelectroautotrophy**, useful mechanistically but outside the strict core phenotype. (tu2023engineeringartificialphotosynthesis pages 1-2)
- Do not infer the phenotype from carbon-fixation genes alone; heterotrophs may possess anaplerotic or partial pathways.
- Preserve condition qualifiers for pH, temperature, oxygen, donor concentration, and growth medium.

## DOI-first bibliography

1. **10.1128/aem.01557-23** — Scott KM, Payne RR, Gahramanova A. “Widespread dissolved inorganic carbon-modifying toolkits…” *Applied and Environmental Microbiology*. Published February 2024. https://doi.org/10.1128/aem.01557-23 (scott2024widespreaddissolvedinorganic pages 10-13)
2. **10.1093/ismejo/wrae173** — Laufer-Meiser K et al. “Oxidation of sulfur, hydrogen, and iron by metabolically versatile *Hydrogenovibrio*…” *The ISME Journal*. 2024. https://doi.org/10.1093/ismejo/wrae173 (laufermeiser2024oxidationofsulfur pages 9-10)
3. **10.3390/microorganisms12030590** — Wang Q et al. “Characterize the Growth and Metabolism of *Acidithiobacillus ferrooxidans* under Electroautotrophic and Chemoautotrophic Conditions.” *Microorganisms*. Published March 2024. https://doi.org/10.3390/microorganisms12030590 (wang2024characterizethegrowth pages 1-2, wang2024characterizethegrowth pages 22-23)
4. **10.1128/aem.01698-23** — Ghimire-Kafle S et al. “Competition between ammonia-oxidizing archaea and complete ammonia oxidizers…” *Applied and Environmental Microbiology*. Published 13 February 2024. https://doi.org/10.1128/aem.01698-23 (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2)
5. **10.1186/s40168-023-01712-w** — Deng W et al. “Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions…” *Microbiome*. Published December 2023. https://doi.org/10.1186/s40168-023-01712-w (deng2023strategiesofchemolithoautotrophs pages 1-2)
6. **10.3390/life13030627** — Prioretti L et al. “Carbon Fixation in the Chemolithoautotrophic Bacterium *Aquifex aeolicus*…” *Life*. Published 23 February 2023. https://doi.org/10.3390/life13030627 (prioretti2023carbonfixationin pages 1-2)
7. **10.1038/s41396-023-01467-0** — Wright CL, Lehtovirta-Morley LE. “Nitrification and beyond: metabolic versatility of ammonia oxidising archaea.” *The ISME Journal*. Published 14 July 2023. https://doi.org/10.1038/s41396-023-01467-0 (wright2023nitrificationandbeyond pages 1-2)
8. **10.1111/1462-2920.16470** — Mao Z et al. “Anaerobic dissimilatory phosphite oxidation…” *Environmental Microbiology*. Published August 2023. https://doi.org/10.1111/1462-2920.16470 (mao2023anaerobicdissimilatoryphosphite pages 1-2)
9. **10.1111/1751-7915.14353** — Alvarez-Guzmán CL et al. “Effect of electron donors on CO2 fixation from a model cement industry flue gas…” *Microbial Biotechnology*. Accepted 25 September 2023; volume 16, 2387–2400. https://doi.org/10.1111/1751-7915.14353 (alvarez‐guzman2023effectofelectron pages 1-2)
10. **10.1038/s41467-023-43524-4** — Tu W et al. “Engineering artificial photosynthesis based on rhodopsin for CO2 fixation.” *Nature Communications*. Accepted 11 November 2023; published December 2023. https://doi.org/10.1038/s41467-023-43524-4 (tu2023engineeringartificialphotosynthesis pages 1-2)
11. **10.3389/fmars.2018.00531** — Le Bris N et al. “Hydrothermal Energy Transfer and Organic Carbon Production at the Deep Seafloor.” *Frontiers in Marine Science*. Published January 2019. https://doi.org/10.3389/fmars.2018.00531 (bris2019hydrothermalenergytransfer pages 5-6)

References

1. (scott2024widespreaddissolvedinorganic pages 10-13): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 8 citations and is from a peer-reviewed journal.

2. (scott2024widespreaddissolvedinorganic pages 2-4): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 8 citations and is from a peer-reviewed journal.

3. (prioretti2023carbonfixationin pages 1-2): Laura Prioretti, Giulia D'Ermo, Pascale Infossi, Arlette Kpebe, Régine Lebrun, Marielle Bauzan, Elisabeth Lojou, Bruno Guigliarelli, Marie-Thérèse Giudici-Orticoni, and Marianne Guiral. Carbon fixation in the chemolithoautotrophic bacterium aquifex aeolicus involves two low-potential ferredoxins as partners of the pfor and ogor enzymes. Life, 13:627, Feb 2023. URL: https://doi.org/10.3390/life13030627, doi:10.3390/life13030627. This article has 8 citations.

4. (mao2023anaerobicdissimilatoryphosphite pages 1-2): Zhuqing Mao, Nicolai Müller, Sabrina Borusak, David Schleheck, and Bernhard Schink. Anaerobic dissimilatory phosphite oxidation, an extremely efficient concept of microbial electron economy. Environmental microbiology, 25:2068-2074, Aug 2023. URL: https://doi.org/10.1111/1462-2920.16470, doi:10.1111/1462-2920.16470. This article has 5 citations and is from a domain leading peer-reviewed journal.

5. (tu2023engineeringartificialphotosynthesis pages 1-2): Weiming Tu, Jiabao Xu, Ian P. Thompson, and Wei E. Huang. Engineering artificial photosynthesis based on rhodopsin for co2 fixation. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43524-4, doi:10.1038/s41467-023-43524-4. This article has 76 citations and is from a highest quality peer-reviewed journal.

6. (wang2024characterizethegrowth pages 22-23): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 11 citations.

7. (alvarez‐guzman2023effectofelectron pages 1-2): Cecilia Lizeth Alvarez‐Guzmán, Karla María Muñoz‐Páez, and Idania Valdez‐Vazquez. Effect of electron donors on co2 fixation from a model cement industry flue gas by non‐photosynthetic microbial communities in batch and continuous reactors. Microbial Biotechnology, 16:2387-2400, Oct 2023. URL: https://doi.org/10.1111/1751-7915.14353, doi:10.1111/1751-7915.14353. This article has 7 citations and is from a peer-reviewed journal.

8. (wang2024characterizethegrowth pages 1-2): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 11 citations.

9. (ghimirekafle2024competitionbetweenammoniaoxidizing pages 1-2): Sabita Ghimire-Kafle, Matt E. Weaver, Madisen P. Kimbrel, and Annette Bollmann. Competition between ammonia-oxidizing archaea and complete ammonia oxidizers from freshwater environments. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01698-23, doi:10.1128/aem.01698-23. This article has 18 citations and is from a peer-reviewed journal.

10. (deng2023strategiesofchemolithoautotrophs pages 1-2): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 17 citations and is from a highest quality peer-reviewed journal.

11. (wright2023nitrificationandbeyond pages 1-2): Chloe L Wright and Laura E Lehtovirta-Morley. Nitrification and beyond: metabolic versatility of ammonia oxidising archaea. The ISME Journal, 17:1358-1368, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01467-0, doi:10.1038/s41396-023-01467-0. This article has 157 citations.

12. (scott2024widespreaddissolvedinorganic pages 4-7): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 8 citations and is from a peer-reviewed journal.

13. (scott2024widespreaddissolvedinorganic pages 15-18): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 8 citations and is from a peer-reviewed journal.

14. (prioretti2023carbonfixationin pages 14-16): Laura Prioretti, Giulia D'Ermo, Pascale Infossi, Arlette Kpebe, Régine Lebrun, Marielle Bauzan, Elisabeth Lojou, Bruno Guigliarelli, Marie-Thérèse Giudici-Orticoni, and Marianne Guiral. Carbon fixation in the chemolithoautotrophic bacterium aquifex aeolicus involves two low-potential ferredoxins as partners of the pfor and ogor enzymes. Life, 13:627, Feb 2023. URL: https://doi.org/10.3390/life13030627, doi:10.3390/life13030627. This article has 8 citations.

15. (scott2024widespreaddissolvedinorganic pages 18-19): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 8 citations and is from a peer-reviewed journal.

16. (laufermeiser2024oxidationofsulfur pages 9-10): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.

17. (bris2019hydrothermalenergytransfer pages 5-6): Nadine Le Bris, Mustafa Yücel, Anindita Das, Stefan M. Sievert, PonnaPakkam LokaBharathi, and Peter R. Girguis. Hydrothermal energy transfer and organic carbon production at the deep seafloor. Frontiers in Marine Science, Jan 2019. URL: https://doi.org/10.3389/fmars.2018.00531, doi:10.3389/fmars.2018.00531. This article has 52 citations.