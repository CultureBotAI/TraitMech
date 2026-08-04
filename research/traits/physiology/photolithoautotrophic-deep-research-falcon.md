---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:51:44.835827'
end_time: '2026-08-04T12:00:51.906112'
duration_seconds: 547.07
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: photolithoautotrophic
  trait_identifier: METPO:1000665
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: photolithoautotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from light and carbon
    from carbon dioxide using inorganic electron donors.
  parent_traits: METPO:1000631
  synonyms: photolithoautotroph
  evidence_summary: 'DOI:10.3389/fmicb.2011.00165: oxidize sulfide (Review supports
    sulfide oxidation coupled to phototrophic central carbon and energy metabolism.)
    | DOI:10.3390/antiox10060829: reduced sulfur compounds as an electron donor (Review
    supports reduced sulfur electron donors in photolithotrophic sulfur bacteria.)
    | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation
    as the autotrophic carbon-assimilation process.)'
  causal_graph_summary: 'photolithoautotrophic_light_inorganic_donor_fixation: 15
    nodes, 13 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photolithoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000665
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from light and carbon from carbon dioxide using inorganic electron donors.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithoautotroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: oxidize sulfide (Review supports sulfide oxidation coupled to phototrophic central carbon and energy metabolism.) | DOI:10.3390/antiox10060829: reduced sulfur compounds as an electron donor (Review supports reduced sulfur electron donors in photolithotrophic sulfur bacteria.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** photolithoautotrophic_light_inorganic_donor_fixation: 15 nodes, 13 edges

## Research Objective

Research the microbial trait **photolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithoautotrophic.yaml`.

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
- **Trait label:** photolithoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000665
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from light and carbon from carbon dioxide using inorganic electron donors.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithoautotroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: oxidize sulfide (Review supports sulfide oxidation coupled to phototrophic central carbon and energy metabolism.) | DOI:10.3390/antiox10060829: reduced sulfur compounds as an electron donor (Review supports reduced sulfur electron donors in photolithotrophic sulfur bacteria.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** photolithoautotrophic_light_inorganic_donor_fixation: 15 nodes, 13 edges

## Research Objective

Research the microbial trait **photolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithoautotrophic.yaml`.

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


# Curation report: photolithoautotrophic

## Target record

- **Trait:** photolithoautotrophic
- **Identifier:** **METPO:1000665**
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** METPO:1000631
- **Recommended operational definition:** an organism can use **light as its energy source**, an **inorganic compound as electron donor**, and **CO2 or bicarbonate as the principal carbon source for biomass production**. This three-part conjunction—not any component alone—is the phenotype to represent. An authoritative review uses essentially this formulation and explains that chlorophyll-based photochemistry generates proton-motive force, ATP, and reductant for CO2 fixation. (thiel2018diversityofchlorophototrophic pages 2-3)

## 1. Scope and boundaries

The trait is a physiological capacity, usually demonstrated by growth or inorganic-carbon assimilation under illumination with an inorganic electron donor. It includes both:

1. **Oxygenic photolithoautotrophy**, principally cyanobacteria: water supplies electrons through photosystems II and I, oxygen is evolved, and carbon is generally assimilated through the Calvin–Benson–Bassham (CBB) cycle.
2. **Anoxygenic photolithoautotrophy**, including green and purple sulfur bacteria and some purple nonsulfur bacteria: donors can include H2S/HS−, S0, thiosulfate, H2, or Fe2+; oxygen is not produced; and CBB, reverse TCA, or other lineage-specific fixation pathways may operate. Reviews document at least H2S, S0, thiosulfate, H2, Fe2+, and H2O across photolithoautotrophic lineages, and CBB, reverse TCA, and 3-hydroxypropionate-bicycle-type carbon fixation. (martin2018aphysiologicalperspective pages 2-3)

### Exclusions and boundary cases

- **Photoorganoheterotrophy:** light supplies energy, but organic compounds supply electrons and usually carbon. This does not satisfy the trait.
- **Chemolithoautotrophy:** inorganic donors and CO2 are used, but energy is not derived from light. It should not be included merely because sulfur-oxidation or carbon-fixation genes are present.
- **Generic photoautotrophy:** may not identify whether the electron donor is inorganic; evidence must establish the lithotrophic component.
- **Mixotrophy:** simultaneous organic-carbon assimilation does not negate photolithoautotrophic capacity, but a mixotrophic growth observation alone does not demonstrate strict photolithoautotrophy.
- **Aerobic anoxygenic phototrophs:** many are obligate photoheterotrophs and therefore should not be assigned this trait without inorganic-carbon assimilation and inorganic-donor evidence.
- **Phototrophy inferred from pigment or reaction-center genes:** genomic potential alone is insufficient to establish growth phenotype.
- **Donor-specific phenotypes:** photoferrotrophy and photothiotrophy are subtypes or contextual realizations, not synonyms for the full class.
- **Anoxia:** appropriate for many sulfur-based anoxygenic assays, but not a universal requirement because oxygenic photolithoautotrophs produce and tolerate O2.

## 2. Mechanistic model

The minimal taxon-neutral mechanism is:

**light → pigment/antenna excitation → reaction-center charge separation → photosynthetic electron transport → proton-motive force → ATP synthesis**, while **inorganic-donor oxidation → electron supply/reductant generation**, and **ATP + reductant + CO2/HCO3− → autotrophic carbon fixation → biomass**. Chlorophototrophs can use radiation over approximately **350–1,100 nm**, reflecting substantial pigment and antenna diversity rather than a single universal wavelength response. (thiel2018diversityofchlorophototrophic pages 2-3)

This core should be separated from alternative donor-oxidation and fixation modules. In sulfur phototrophs, flavocytochrome c/FccAB can relay sulfide-derived electrons through cytochrome c to reaction centers, whereas membrane-bound SQR transfers them into the quinone pool. In *Rhodovulum sulfidophilum*, Sox enzymes oxidize thiosulfate to sulfate. These are documented mechanisms but are not universal across all photolithoautotrophs. (kushkevych2021anoxygenicphotosynthesisin pages 3-5)

## 3. Candidate nodes

### Trait and process nodes

- photolithoautotrophic — **METPO:1000665**
- photosynthesis — candidate **GO:0015979**
- light reaction / photosynthetic electron transport — candidate GO term; verify exact child term during implementation
- carbon fixation — candidate **GO:0015977**
- ATP synthesis coupled to proton transport — candidate GO term; verify exact term for the intended granularity
- anoxygenic photosynthesis — label-only unless a verified ontology term is selected
- oxygenic photosynthesis — candidate GO term
- photoferrotrophy — label-only candidate
- phototrophic sulfur oxidation — label-only candidate
- autotrophic growth / biomass production — label-only process or METPO phenotype node

### Environmental and experimental factors

- light / electromagnetic radiation — use an ENVO or radiation ontology term only after identifier verification
- illuminated condition; darkness control
- anoxic condition — relevant to many sulfur-bacterium assays, not universal
- inorganic-carbon medium
- absence of organic carbon — assay condition supporting strict autotrophy
- near-infrared illumination: *R. sulfidophilum* experiments used approximately **850 nm**, anoxic artificial seawater, and 30°C. (gupta2021photoferrotrophyandphototrophic pages 1-2)

### Chemicals and metabolites

High-priority nodes are CO2, bicarbonate, H2O, H2S/HS−, elemental sulfur, thiosulfate, sulfate, H2, Fe2+, Fe3+, pyrite (FeS2), O2, quinone/quinol, reduced ferredoxin, NAD(P)H, ADP, ATP, phosphate, and biomass/organic carbon. Use CHEBI CURIEs only after exact species and protonation states are checked; in particular, H2S and HS− should not be collapsed unintentionally.

### Complexes, proteins, and genes

- chlorophyll/bacteriochlorophyll antenna complex
- chlorosome — especially green sulfur bacteria and selected other lineages
- Type I reaction center / photosystem I
- Type II reaction center / photosystem II
- cytochrome *bc1* or related quinol-oxidizing complex
- ATP synthase
- ferredoxin and ferredoxin:NAD(P)+ oxidoreductase
- Rubisco and phosphoribulokinase for CBB-cycle branches
- reverse-TCA enzymes, including ATP citrate lyase where taxonomically appropriate
- **SQR**: sulfide:quinone oxidoreductase
- **FccAB**: flavocytochrome-c sulfide dehydrogenase
- **SoxYZ and other Sox proteins**: sulfur-substrate carrier/oxidation system
- **DsrAB** and associated sulfur-globule oxidation machinery
- **AprAB**: adenylylsulfate reductase module
- c-type and b-type cytochromes
- **EeuP**, a diheme cytochrome c implicated in phototrophic extracellular electron uptake

Gene/protein nodes should initially remain label-only or use verified UniProt/InterPro identifiers. A gene symbol is not a universal ortholog identifier, and presence of one sulfur-oxidation gene is neither necessary nor sufficient for the complete trait.

### Cellular locations

- cytoplasmic/photosynthetic membrane
- thylakoid membrane in cyanobacteria
- periplasm
- quinone pool
- chlorosome
- sulfur globule and sulfur-globule envelope in applicable sulfur bacteria
- cytoplasm, where carbon-fixation reactions occur

### Taxon/context nodes

- Cyanobacteria: water donor, PSI/PSII, oxygen evolution, typically CBB fixation
- green sulfur bacteria/Chlorobiaceae: H2S-centered anoxygenic phototrophy, chlorosomes, generally reverse-TCA fixation
- purple sulfur bacteria/Chromatiaceae: reduced-sulfur oxidation, Type II reaction centers, commonly CBB fixation
- *Allochromatium vinosum*: experimentally demonstrated pyrite-supported autotrophic growth
- *Rhodovulum sulfidophilum*: experimentally demonstrated photoferrotrophy and phototrophic extracellular electron uptake

## 4. Candidate causal edges

The following synthesis separates broad core edges from lineage- and assay-specific alternatives.

| subject | predicate | object | context/taxon | evidence strength | DOI |
|---|---|---|---|---|---|
| light | excites | photosynthetic reaction center | chlorophototrophs broadly; includes photolithoautotrophs (thiel2018diversityofchlorophototrophic pages 2-3) | strong review-level, broad | https://doi.org/10.1146/annurev-arplant-042817-040500 |
| photosynthetic reaction center electron transport | generates | proton motive force | chlorophototrophs broadly (thiel2018diversityofchlorophototrophic pages 2-3) | strong review-level, broad | https://doi.org/10.1146/annurev-arplant-042817-040500 |
| proton motive force | drives | ATP synthesis | chlorophototrophs broadly (thiel2018diversityofchlorophototrophic pages 2-3) | strong review-level, broad | https://doi.org/10.1146/annurev-arplant-042817-040500 |
| oxidation of inorganic electron donor | supplies electrons to | photosynthetic electron flux | photolithoautotrophs broadly (thiel2018diversityofchlorophototrophic pages 2-3, martin2018aphysiologicalperspective pages 2-3) | strong review-level, broad | https://doi.org/10.1146/annurev-arplant-042817-040500; https://doi.org/10.1093/femsre/fux056 |
| hydrogen sulfide (H2S) | is oxidized by | flavocytochrome c (FccAB route) | photolithotrophic sulfur bacteria; taxon-specific route (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | moderate review-level, taxon-specific | https://doi.org/10.3390/antiox10060829 |
| hydrogen sulfide (H2S) | is oxidized by | sulfide:quinone oxidoreductase (SQR route) | green and purple sulfur bacteria; taxon-specific route (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | strong review-level, taxon-specific | https://doi.org/10.3390/antiox10060829 |
| FccAB-mediated sulfide oxidation | feeds electrons to | cytochrome c / photosynthetic reaction centers | photolithotrophic sulfur bacteria; taxon-specific (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | moderate review-level, taxon-specific | https://doi.org/10.3390/antiox10060829 |
| SQR-mediated sulfide oxidation | feeds electrons to | quinone pool and photosynthetic electron transport | photolithotrophic sulfur bacteria; taxon-specific (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | strong review-level, taxon-specific | https://doi.org/10.3390/antiox10060829 |
| thiosulfate | is oxidized by | Sox enzyme system | Rhodovulum sulfidophilum; taxon-specific (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | moderate review-level, taxon-specific | https://doi.org/10.3390/antiox10060829 |
| Sox-mediated thiosulfate oxidation | produces | sulfate | Rhodovulum sulfidophilum; taxon-specific (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | moderate review-level, taxon-specific | https://doi.org/10.3390/antiox10060829 |
| CO2 / bicarbonate | is assimilated by | autotrophic carbon fixation pathway | photolithoautotrophs broadly (thiel2018diversityofchlorophototrophic pages 2-3, martin2018aphysiologicalperspective pages 2-3) | strong review-level, broad | https://doi.org/10.1146/annurev-arplant-042817-040500; https://doi.org/10.1093/femsre/fux056 |
| autotrophic carbon fixation pathway | produces | biomass / organic matter | photolithoautotrophs broadly (thiel2018diversityofchlorophototrophic pages 2-3, martin2018aphysiologicalperspective pages 2-3) | strong review-level, broad | https://doi.org/10.1146/annurev-arplant-042817-040500; https://doi.org/10.1093/femsre/fux056 |
| water (H2O) | serves as electron donor for | photosystems I and II | cyanobacteria; oxygenic photolithoautotrophy, taxon-specific (thiel2018diversityofchlorophototrophic pages 2-3) | strong review-level, taxon-specific | https://doi.org/10.1146/annurev-arplant-042817-040500 |
| photosystems I and II | support | Calvin-Benson-Bassham cycle CO2 fixation | cyanobacteria; taxon-specific (thiel2018diversityofchlorophototrophic pages 2-3) | strong review-level, taxon-specific | https://doi.org/10.1146/annurev-arplant-042817-040500 |
| hydrogen sulfide (H2S) | serves as electron donor for | anoxygenic photosynthesis | green sulfur bacteria; taxon-specific (kushkevych2024anoxygenicphotosynthesiswith pages 18-18) | strong review-level, taxon-specific | https://doi.org/10.3389/fmicb.2024.1417714 |
| reverse tricarboxylic acid cycle | assimilates | CO2 in green sulfur bacteria | green sulfur bacteria; taxon-specific (kushkevych2024anoxygenicphotosynthesiswith pages 18-18) | strong review-level, taxon-specific | https://doi.org/10.3389/fmicb.2024.1417714 |
| Fe(II) | donates electrons to | photoferrotrophic metabolism | Rhodovulum sulfidophilum; experimental, taxon-specific (gupta2021photoferrotrophyandphototrophic pages 1-2, gupta2021photoferrotrophyandphototrophic pages 8-10) | strong experimental, taxon-specific | https://doi.org/10.1038/s41396-021-01015-8 |
| EeuP diheme cytochrome c | enables | phototrophic extracellular electron uptake | Rhodovulum sulfidophilum; experimental, taxon-specific (gupta2021photoferrotrophyandphototrophic pages 8-10) | strong experimental, taxon-specific | https://doi.org/10.1038/s41396-021-01015-8 |
| pyrite (FeS2) | serves as electron and sulfur source for | autotrophic growth | Allochromatium vinosum; experimental, taxon-specific (alarcon2024evidenceforautotrophic pages 1-2) | strong experimental, taxon-specific | https://doi.org/10.1128/aem.00863-24 |
| pyrite exposure | upregulates | c- and b-type cytochromes (~200-fold) | Allochromatium vinosum; experimental, taxon-specific (alarcon2024evidenceforautotrophic pages 1-2, alarcon2024evidenceforautotrophic pages 22-24) | strong experimental, taxon-specific | https://doi.org/10.1128/aem.00863-24 |
| pyrite-dependent growth | upregulates | FccAB and SoxYZ | Allochromatium vinosum; experimental, taxon-specific (alarcon2024evidenceforautotrophic pages 1-2) | strong experimental, taxon-specific | https://doi.org/10.1128/aem.00863-24 |
| pyrite-dependent growth | downregulates | Dsr and Apr cytoplasmic sulfur oxidation proteins | Allochromatium vinosum; experimental, taxon-specific (alarcon2024evidenceforautotrophic pages 1-2) | strong experimental, taxon-specific | https://doi.org/10.1128/aem.00863-24 |
| pyrite-derived electron scavenging | may bypass portions of | canonical photosynthetic pathway to carbon fixation | Allochromatium vinosum; uncertain author interpretation (alarcon2024evidenceforautotrophic pages 22-24) | uncertain, do not over-curate | https://doi.org/10.1128/aem.00863-24 |


*Table: This table summarizes the strongest curation-ready causal edges for METPO:1000665, emphasizing broad core mechanisms plus donor- and taxon-specific variants. It also flags edges that are strong but taxon-restricted, and one pyrite-related hypothesis that should remain uncertain in TraitMech curation.*

### Supporting snippets and curation notes

| Proposed triple | Short supporting snippet or faithful source extract | Curation note |
|---|---|---|
| light — activates — chlorophyll/bacteriochlorophyll reaction center | Chlorophototrophs use chlorophylls or bacteriochlorophylls to capture light and perform light-driven redox reactions. | Broad, review-supported core edge. (thiel2018diversityofchlorophototrophic pages 2-3) |
| reaction-center electron transport — generates — proton-motive force | Light-driven redox reactions produce “proton-motive force for ATP synthesis.” | Broad core edge; reaction-center architecture differs by lineage. (thiel2018diversityofchlorophototrophic pages 2-3) |
| proton-motive force — drives — ATP synthesis | The review explicitly connects proton-motive force with ATP synthesis. | Broad core edge; ATP synthase itself may be added as mediator. (thiel2018diversityofchlorophototrophic pages 2-3) |
| inorganic electron donor oxidation — supplies — reductant for CO2 fixation | Photolithoautotrophs use inorganic compounds as electron donors and CO2/bicarbonate as carbon source; the photochemical system provides reductants for fixation. | Broad conceptual edge, but donor-to-reductant route is lineage-specific. (thiel2018diversityofchlorophototrophic pages 2-3) |
| CO2/HCO3− — substrate of — autotrophic carbon fixation | “CO2/bicarbonate” is identified as the carbon source. | Broad and curation-ready. (thiel2018diversityofchlorophototrophic pages 2-3) |
| carbon fixation — contributes to — biomass | Photolithoautotrophic metabolism converts inorganic carbon into cellular organic matter. | Broad endpoint; avoid implying one universal fixation pathway. (thiel2018diversityofchlorophototrophic pages 2-3) |
| H2S — oxidized by — FccAB | Flavocytochrome c transfers electrons “from H2S to cytochrome c and then to photosynthetic reaction centers.” | Sulfur-phototroph branch only. (kushkevych2021anoxygenicphotosynthesisin pages 3-5) |
| H2S — oxidized by — SQR | SQR is described as a membrane-bound sulfide-oxidizing enzyme operating through isoprenoid quinones. | Strong sulfur-phototroph branch. (kushkevych2021anoxygenicphotosynthesisin pages 3-5) |
| SQR — reduces/feeds — quinone pool | SQR supplies sulfide-derived electrons to photosynthetic electron flux via quinones and a Rieske/cytochrome-b complex. | Predicate should reflect electron transfer, not physical activation. (kushkevych2021anoxygenicphotosynthesisin pages 3-5) |
| thiosulfate — oxidized by Sox — sulfate | The Sox system in *R. sulfidophilum* catalyzes thiosulfate oxidation to sulfate. | Taxon-specific; do not universalize. (kushkevych2021anoxygenicphotosynthesisin pages 3-5) |
| H2O — donates electrons to — oxygenic photosystems | Cyanobacteria use PSI and PSII for oxygen-evolving photosynthesis. | Oxygenic branch only. (thiel2018diversityofchlorophototrophic pages 2-3) |
| PSI/PSII-derived energy and reductant — support — CBB fixation | Cyanobacteria fix CO2 through the CBB cycle. | Strong cyanobacterial branch. (thiel2018diversityofchlorophototrophic pages 2-3) |
| H2S — donates electrons to — green-sulfur-bacterial anoxygenic photosynthesis | The 2024 review identifies H2S as the main donor and its oxidation to elemental sulfur. | Strong but lineage-specific. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18) |
| reverse TCA cycle — assimilates — CO2 | Green sulfur bacteria are described as assimilating CO2 through reverse TCA. | Strong GSB branch, not universal. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18) |
| Fe2+ — donates electrons to — photoferrotrophic electron transport | All **15** tested *R. sulfidophilum* isolates performed photoferrotrophy. | Strong experimental result; scope limited to tested strains and conditions. (gupta2021photoferrotrophyandphototrophic pages 1-2) |
| EeuP — enables — phototrophic extracellular electron uptake | *eeuP* deletion reduced illuminated current uptake by about **76%**, from −30.66 ± 0.82 to −7.29 ± 1.87 nA cm−2. | Strong genetic evidence for pEEU, but pEEU from an electrode is not automatically equivalent to Fe2+-supported autotrophic growth. (gupta2021photoferrotrophyandphototrophic pages 8-10) |
| pyrite — supports — autotrophic growth of *A. vinosum* | The 2024 study reports the first PSB autotrophic growth using insoluble pyrite as electron and sulfur source. | Strong, recent, taxon- and assay-specific edge. (alarcon2024evidenceforautotrophic pages 1-2) |
| pyrite condition — increases expression of — c-/b-type cytochromes | Cytochrome genes were induced by up to approximately **200-fold** in pyrite cultures. | Expression supports involvement, not proof that every induced cytochrome directly contacts pyrite. (alarcon2024evidenceforautotrophic pages 1-2) |
| pyrite condition — increases expression of — FccAB/SoxYZ | Periplasmic or membrane sulfur proteins, including FccAB and SoxYZ, were upregulated. | Curate as regulation under condition, not necessarily as the sole pyrite-oxidation route. (alarcon2024evidenceforautotrophic pages 1-2) |
| pyrite condition — decreases expression of — Dsr/Apr | Cytoplasmic Dsr and Apr groups were extensively downregulated relative to sulfide control. | Direction is assay-relative; do not encode Dsr/Apr as universal inhibitors. (alarcon2024evidenceforautotrophic pages 1-2) |

## 5. Recent developments and quantitative evidence

### Pyrite as an electron and sulfur source

Alarcon and colleagues reported in July 2024 that *Allochromatium vinosum* grew autotrophically on insoluble pyrite. Growth was robust but slower than in sodium-sulfide controls. Transcriptomics showed up to approximately **200-fold** induction of c- and b-type cytochromes, induction of FccAB and SoxYZ, repression of Dsr/Apr modules, and extensive downregulation of light-harvesting and reaction-center genes. Polymeric sulfur was detected on reacted pyrite. These observations support a mineral-dependent electron-transfer phenotype, but the authors explicitly could not exclude partial bypass of conventional photosynthetic intermediates. (alarcon2024evidenceforautotrophic pages 1-2, alarcon2024evidenceforautotrophic pages 22-24)

This is therefore best represented as a taxon-specific experimental branch:

**pyrite → extracellular/periplasmic electron scavenging → cytochrome network → cellular metabolism/autotrophic growth**, with the exact connection to photosynthetic electron transport marked uncertain.

### Photoferrotrophy and extracellular electron uptake

All **15** marine *R. sulfidophilum* isolates tested oxidized Fe(II) phototrophically. In strain AB26, illuminated electrode-current uptake depended strongly on EeuP: deletion caused an approximately **76%** decrease. EeuP homologs were found in **56 sequences** across Proteobacteria and Acidobacteria, suggesting wider potential distribution, although homolog occurrence does not establish phenotype. (gupta2021photoferrotrophyandphototrophic pages 1-2, gupta2021photoferrotrophyandphototrophic pages 8-10)

### Current expert synthesis for green sulfur bacteria

A July 2024 review characterizes green sulfur bacteria as anoxygenic photolithoautotrophs using H2S, producing elemental sulfur, collecting light in chlorosomes, and fixing CO2 through reverse TCA. It highlights environmental-management and biotechnology prospects, especially H2S detoxification in anoxic waters and soils. These are credible application directions, but most should be described as developing applications rather than standardized full-scale implementations. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18)

## 6. Applications and real-world relevance

- **Hydrogen-sulfide detoxification:** phototrophic sulfur bacteria convert toxic H2S into elemental sulfur and/or more oxidized sulfur products while assimilating CO2. Reviews explicitly discuss their use in detoxifying anoxic environments. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18, kushkevych2021anoxygenicphotosynthesisin pages 3-5)
- **Wastewater and photobioreactor treatment:** sulfide removal can be coupled to biomass generation under light. Implementation remains constrained by light penetration, donor toxicity, sulfur-product handling, community stability, and reactor geometry.
- **Carbon capture and biomanufacturing:** the trait offers direct solar-to-biomass conversion using inorganic carbon. Productive use requires redirecting fixed carbon toward fuels, polymers, pigments, or chemicals without losing photochemical efficiency.
- **Iron and sulfur biogeochemistry:** photoferrotrophy and pyrite utilization connect light-driven carbon assimilation to mineral transformation and may affect sedimentary Fe/S cycles. (alarcon2024evidenceforautotrophic pages 1-2, gupta2021photoferrotrophyandphototrophic pages 1-2)
- **Bioelectrochemical systems and artificial photosynthesis:** EeuP-dependent pEEU and pyrite-associated cytochrome induction provide candidate modules for coupling extracellular electrons to photosynthetic metabolism. These are research-stage mechanisms rather than mature industrial platforms. (gupta2021photoferrotrophyandphototrophic pages 8-10, alarcon2024evidenceforautotrophic pages 22-24)

## 7. Recommended TraitMech graph architecture

Use a small universal backbone with explicit alternatives:

1. **light → reaction-center excitation**
2. **reaction-center excitation → photosynthetic electron transport**
3. **photosynthetic electron transport → proton-motive force**
4. **proton-motive force → ATP synthesis**
5. **inorganic electron donor → donor-oxidation module → electron carrier/reductant**
6. **CO2/HCO3− → taxon-specific carbon-fixation module → organic carbon/biomass**
7. **ATP + reductant → enables carbon fixation**
8. **completion of light-energy, inorganic-donor, and inorganic-carbon modules → photolithoautotrophic phenotype**

Branch the donor module into water/PSII, sulfide/FccAB, sulfide/SQR, thiosulfate/Sox, Fe2+/cytochrome-mediated photoferrotrophy, H2/hydrogenase, and pyrite-associated electron transfer. Branch carbon fixation into CBB, reverse TCA, and other validated lineage-specific routes. This avoids representing sulfur metabolism or CBB fixation as universal.

## 8. Warnings: claims not yet suitable for unqualified curation

1. **Do not curate pyrite → photosynthetic electron transport as established.** The 2024 authors state that direct coupling to carbon fixation, bypassing portions of the photosynthetic pathway, cannot be excluded. (alarcon2024evidenceforautotrophic pages 22-24)
2. **Do not infer the trait from SQR, FccAB, Sox, Dsr, Rubisco, or reaction-center genes alone.** Each module can occur in organisms lacking one of the other defining components.
3. **Do not make H2S the universal donor.** Cyanobacteria use water, and experimentally supported alternatives include Fe2+, H2, thiosulfate, sulfur, and pyrite. (martin2018aphysiologicalperspective pages 2-3)
4. **Do not make CBB the universal fixation route.** Green sulfur bacteria generally use reverse TCA; additional photolithoautotrophs use other pathways. (martin2018aphysiologicalperspective pages 2-3, kushkevych2024anoxygenicphotosynthesiswith pages 18-18)
5. **Do not equate phototrophic extracellular electron uptake with autotrophic growth.** Electrode-current uptake establishes electron acquisition; CO2-derived biomass must be independently demonstrated.
6. **Do not encode anoxia as universally necessary.** It is characteristic of many anoxygenic sulfur-phototroph assays, but incompatible with a universal graph that includes oxygenic cyanobacteria.
7. **Do not treat transcript induction as direct catalytic proof.** The approximately 200-fold cytochrome response to pyrite supports involvement but does not identify the physical electron conduit. (alarcon2024evidenceforautotrophic pages 1-2)
8. **Do not curate evolutionary reconstructions as present-day causal mechanisms.** Proposed photothioautotrophic intermediates and ancestral reaction centers are expert hypotheses, not direct phenotype evidence. (martin2018aphysiologicalperspective pages 21-21, martin2018aphysiologicalperspective pages 14-15)
9. **Verify all ontology identifiers before YAML insertion.** Exact protonation states, reaction direction, taxonomic scope, and protein-family versus gene-product granularity matter.

## DOI-first bibliography

1. Alarcon HV et al. “Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source.” *Applied and Environmental Microbiology*. **July 2024**. https://doi.org/10.1128/aem.00863-24. (alarcon2024evidenceforautotrophic pages 1-2)
2. Kushkevych I et al. “Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments.” *Frontiers in Microbiology* 15. **July 2024**. https://doi.org/10.3389/fmicb.2024.1417714. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18)
3. Gupta D et al. “Photoferrotrophy and phototrophic extracellular electron uptake is common in the marine anoxygenic phototroph *Rhodovulum sulfidophilum*.” *ISME Journal* 15:3384–3398. **May 2021**. https://doi.org/10.1038/s41396-021-01015-8. (gupta2021photoferrotrophyandphototrophic pages 1-2, gupta2021photoferrotrophyandphototrophic pages 8-10)
4. Kushkevych I et al. “Anoxygenic Photosynthesis in Photolithotrophic Sulfur Bacteria and Their Role in Detoxication of Hydrogen Sulfide.” *Antioxidants* 10:829. **May 2021**. https://doi.org/10.3390/antiox10060829. (kushkevych2021anoxygenicphotosynthesisin pages 3-5)
5. Thiel V, Tank M, Bryant DA. “Diversity of Chlorophototrophic Bacteria Revealed in the Omics Era.” *Annual Review of Plant Biology* 69:21–49. **May 2018**. https://doi.org/10.1146/annurev-arplant-042817-040500. (thiel2018diversityofchlorophototrophic pages 2-3)
6. Martin WF, Bryant DA, Beatty JT. “A physiological perspective on the origin and evolution of photosynthesis.” *FEMS Microbiology Reviews* 42:205–231. Published online **November 2017**; issue year 2018. https://doi.org/10.1093/femsre/fux056. (martin2018aphysiologicalperspective pages 2-3)
7. Tang K-H, Tang YJ, Blankenship RE. “Carbon Metabolic Pathways in Phototrophic Bacteria and Their Broader Evolutionary Implications.” *Frontiers in Microbiology* 2:165. **August 2011**. https://doi.org/10.3389/fmicb.2011.00165.
8. Berg IA. “Ecological Aspects of the Distribution of Different Autotrophic CO2 Fixation Pathways.” *Applied and Environmental Microbiology* 77:1925–1936. **March 2011**. https://doi.org/10.1128/AEM.02473-10.

**Curation conclusion:** retain the existing light–inorganic-donor–carbon-fixation backbone, but refactor it into a universal photochemical core plus donor-oxidation and carbon-fixation alternatives. The strongest novel addition is a taxon-specific pyrite branch for *A. vinosum*, with cytochrome/FccAB/SoxYZ regulation represented as experimental evidence and the proposed bypass of canonical photosynthetic electron transport retained only as an uncertain hypothesis.

References

1. (thiel2018diversityofchlorophototrophic pages 2-3): Vera Thiel, Marcus Tank, and Donald A. Bryant. Diversity of chlorophototrophic bacteria revealed in the omics era. Annual review of plant biology, 69:21-49, May 2018. URL: https://doi.org/10.1146/annurev-arplant-042817-040500, doi:10.1146/annurev-arplant-042817-040500. This article has 120 citations and is from a domain leading peer-reviewed journal.

2. (martin2018aphysiologicalperspective pages 2-3): William F Martin, Donald A Bryant, and J Thomas Beatty. A physiological perspective on the origin and evolution of photosynthesis. FEMS Microbiology Reviews, 42:205-231, Nov 2018. URL: https://doi.org/10.1093/femsre/fux056, doi:10.1093/femsre/fux056. This article has 189 citations and is from a domain leading peer-reviewed journal.

3. (kushkevych2021anoxygenicphotosynthesisin pages 3-5): Ivan Kushkevych, Veronika Bosáková, Monika Vítězová, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis in photolithotrophic sulfur bacteria and their role in detoxication of hydrogen sulfide. Antioxidants, 10:829, May 2021. URL: https://doi.org/10.3390/antiox10060829, doi:10.3390/antiox10060829. This article has 19 citations.

4. (gupta2021photoferrotrophyandphototrophic pages 1-2): Dinesh Gupta, Michael S Guzman, Karthikeyan Rengasamy, Andreea Stoica, Rajesh Singh, Tahina Onina Ranaivoarisoa, Emily J Davenport, Wei Bai, Beau McGinley, J Mark Meacham, and Arpita Bose. Photoferrotrophy and phototrophic extracellular electron uptake is common in the marine anoxygenic phototroph rhodovulum sulfidophilum. The ISME Journal, 15:3384-3398, May 2021. URL: https://doi.org/10.1038/s41396-021-01015-8, doi:10.1038/s41396-021-01015-8. This article has 31 citations.

5. (kushkevych2024anoxygenicphotosynthesiswith pages 18-18): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

6. (gupta2021photoferrotrophyandphototrophic pages 8-10): Dinesh Gupta, Michael S Guzman, Karthikeyan Rengasamy, Andreea Stoica, Rajesh Singh, Tahina Onina Ranaivoarisoa, Emily J Davenport, Wei Bai, Beau McGinley, J Mark Meacham, and Arpita Bose. Photoferrotrophy and phototrophic extracellular electron uptake is common in the marine anoxygenic phototroph rhodovulum sulfidophilum. The ISME Journal, 15:3384-3398, May 2021. URL: https://doi.org/10.1038/s41396-021-01015-8, doi:10.1038/s41396-021-01015-8. This article has 31 citations.

7. (alarcon2024evidenceforautotrophic pages 1-2): Hugo V. Alarcon, Jonathon E. Mohl, Grace W. Chong, Ana Betancourt, Yi Wang, Weinan Leng, Jason C. White, and Jie Xu. Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00863-24, doi:10.1128/aem.00863-24. This article has 6 citations and is from a peer-reviewed journal.

8. (alarcon2024evidenceforautotrophic pages 22-24): Hugo V. Alarcon, Jonathon E. Mohl, Grace W. Chong, Ana Betancourt, Yi Wang, Weinan Leng, Jason C. White, and Jie Xu. Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00863-24, doi:10.1128/aem.00863-24. This article has 6 citations and is from a peer-reviewed journal.

9. (martin2018aphysiologicalperspective pages 21-21): William F Martin, Donald A Bryant, and J Thomas Beatty. A physiological perspective on the origin and evolution of photosynthesis. FEMS Microbiology Reviews, 42:205-231, Nov 2018. URL: https://doi.org/10.1093/femsre/fux056, doi:10.1093/femsre/fux056. This article has 189 citations and is from a domain leading peer-reviewed journal.

10. (martin2018aphysiologicalperspective pages 14-15): William F Martin, Donald A Bryant, and J Thomas Beatty. A physiological perspective on the origin and evolution of photosynthesis. FEMS Microbiology Reviews, 42:205-231, Nov 2018. URL: https://doi.org/10.1093/femsre/fux056, doi:10.1093/femsre/fux056. This article has 189 citations and is from a domain leading peer-reviewed journal.