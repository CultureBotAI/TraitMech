---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:10:22.446454'
end_time: '2026-06-18T11:31:08.914539'
duration_seconds: 1246.47
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemoorganotrophic
  trait_identifier: METPO:1000663
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemoorganotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy through chemical
    oxidation of organic compounds that also serve as the carbon source for biosynthesis.
  parent_traits: METPO:1000631
  synonyms: chemoorganotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia
    chapter classifies chemotrophy by chemical rather than light energy sources.)
    | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review
    supports respiratory-chain energy conservation from redox reactions.)'
  causal_graph_summary: 'chemoorganotrophic_organic_oxidation_energy: 8 nodes, 7 edges'
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
- **Trait label:** chemoorganotrophic
- **METPO identifier:** METPO:1000663
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy through chemical oxidation of organic compounds that also serve as the carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoorganotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical rather than light energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory-chain energy conservation from redox reactions.)
- **Existing causal graph summary:** chemoorganotrophic_organic_oxidation_energy: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **chemoorganotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoorganotrophic.yaml`.

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
- **Trait label:** chemoorganotrophic
- **METPO identifier:** METPO:1000663
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy through chemical oxidation of organic compounds that also serve as the carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoorganotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical rather than light energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory-chain energy conservation from redox reactions.)
- **Existing causal graph summary:** chemoorganotrophic_organic_oxidation_energy: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **chemoorganotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoorganotrophic.yaml`.

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


# Chemoorganotrophic (METPO:1000663) — curation-focused research report

## 1. Scope summary (TraitMech curation intent)

**Trait label:** chemoorganotrophic (METPO:1000663)  
**Working scope:** A *chemotrophic* lifestyle in which **organic compounds serve as electron donors** for energy generation; in many common microbial ecology/engineering usages this largely overlaps with **chemoorganoheterotrophy** (organic electron donor *and* organic carbon source for biomass), but the trait label “chemoorganotrophic” itself is most tightly anchored to the **electron donor** (organo-) and **energy source** (chemo-) dimensions. (weissbrodt2023basicmicrobiologyand pages 16-18, weissbrodt2023basicmicrobiologyand pages 19-22)

**Core mechanistic interpretation for causal graph curation:** chemoorganotrophy is expressed through (i) organic substrate oxidation in central metabolism producing reduced electron carriers, and (ii) energy conservation via either **respiration** (external terminal electron acceptor; membrane electron transport chain → ion motive force → ATP synthase) or **fermentation** (no external terminal acceptor; electrons are redistributed to organic products; ATP largely via substrate-level phosphorylation, but may include membrane-linked contributions in some taxa). (garimella2024fromcellsto pages 4-6, weissbrodt2023basicmicrobiologyand pages 16-18, hackmann2024thevastlandscape pages 2-3)

## 2. Key concepts and definitions (current understanding)

### 2.1 Trophic nomenclature (chemo-/organo-/hetero-)
Weissbrodt et al. (2023) explicitly frame microbial trophic labels as combinations of energy source (chemo vs photo), electron donor type (organo vs litho), and carbon source (hetero vs auto). In that framework, **chemoorganotrophs use organic compounds as electron donors** (organo-) to support energy generation (chemo-). (weissbrodt2023basicmicrobiologyand pages 16-18)

### 2.2 Distinguishing respiration vs fermentation within chemoorganotrophy
A practical curatable separation is the availability and identity of **terminal electron acceptors**:

* **Respiration:** electron acceptors can range from **O2 in aerobic respiration** to **inorganic compounds in anaerobic respiration**. (weissbrodt2023basicmicrobiologyand pages 16-18)
* **Fermentation:** when **no external terminal electron acceptor is available**, electrons are “relocated onto an organic catabolic product.” (weissbrodt2023basicmicrobiologyand pages 16-18)

Hackmann (2024) emphasizes that although fermentation is often defined in contrast to respiration by ATP formation mechanism (SLP vs ETC), **electron transport chains occur in fermentative organisms**, and in at least one case ETC+ATP synthase contributed **up to ~one-third of total ATP**, arguing against overly strict mechanistic definitions. (hackmann2024thevastlandscape pages 2-3)

### 2.3 Distinguishing chemoorganotrophy from chemolithotrophy
Weissbrodt et al. (2023) contrast chemoorganoheterotrophs (organic electron donors / organic carbon for biomass) with chemolithoautotrophs (inorganic electron donors / CO2 fixation), e.g., nitrifiers. (weissbrodt2023basicmicrobiologyand pages 19-22)

Briški & Vuković Domanovac (2017) also list “chemoheterotrophs or chemoorganotrophs” as organisms using **organic compounds for energy** (and, by context, carbon), contrasting with chemolithotrophs using inorganic compounds. (briski2017environmentalmicrobiology pages 3-4)

## 3. Recent developments and latest research (prioritizing 2023–2024)

### 3.1 Expansion of known fermentative (chemoorganotrophic) diversity
Hackmann’s 2024 synthesis of thousands of organism records reports that **over one-fourth of all prokaryotes are fermentative**, using **>40 substrates** and releasing **>50 metabolic end products**, with glucose fermentation mapped in **>120 biochemical reactions**. (hackmann2024thevastlandscape pages 1-2)

Hackmann further reports curated counts of **55 end products**, **46 chemically defined substrates**, and **nearly 300 combinations** of fermentation products across ~8,300 prokaryotes, highlighting both biochemical and phenotypic diversity relevant to chemoorganotrophic expression. (hackmann2024thevastlandscape pages 2-3)

### 3.2 Updated mechanistic view: fermentations can include membrane-linked energy conservation
Hackmann (2024) provides mechanistic cataloging of energy-conserving electron-transfer systems commonly seen in anaerobic chemoorganotrophs, including **Rnf (EC 7.2.1.2)** and **Ech (EC 7.1.1.-)** that transfer electrons away from reduced ferredoxin and couple redox flow to ion gradients that drive ATP synthase. (hackmann2024thevastlandscape pages 5-6)

### 3.3 Bioelectrochemical emphasis: bacterial ETC modularity and applied electron transport
Garimella et al. (2024) emphasize that bacterial ETCs are **branched and modular**, with electrons entering at the dehydrogenase level, quinone pool, or mobile carriers; terminal oxidases include **quinol oxidases** and **cytochrome c oxidases**, and anaerobic conditions can reorganize chains for alternative acceptors (e.g., nitrate), affecting bioenergetic yields (P/O). (garimella2024fromcellsto pages 4-6)

## 4. Current applications and real-world implementations

### 4.1 Biodegradation and bioremediation (organic oxidation as application)
Briški & Vuković Domanovac define microbial degradation broadly as **“biological oxidation of organic matter”**, and describe complete biodegradation (mineralisation) as oxidation to **CO2 and water**, yielding carbon and energy for growth, with practical relevance to remediation of pollutants including hydrocarbons, PCBs, PAHs, radionuclides and metals. (briski2017environmentalmicrobiology pages 15-16, briski2017environmentalmicrobiology pages 13-15)

### 4.2 Fermentation applications: agriculture, health, and commodity chemicals
Hackmann (2024) connects chemoorganotrophic fermentation products to livestock energy supply and human health, and highlights industrial fermentation’s role in producing biofuels and commodity chemicals; it also explicitly names manipulation approaches including **genetic engineering** and **electrofermentation**. (hackmann2024thevastlandscape pages 1-2)

### 4.3 Microbial fuel cells and bioelectrochemical systems
Garimella et al. (2024) review leveraging bacterial electron transport to enable **microbial fuel cells**, with real-world relevance to renewable energy generation and environmental applications (wastewater treatment, biosensing, bioremediation) through engineered electron transfer to electrodes. (garimella2024fromcellsto pages 4-6)

## 5. Expert opinions and analysis (authoritative framing)

### 5.1 Definitional boundaries: fermentation vs respiration is not solely “ETC present/absent”
Hackmann (2024) argues that because ETCs have long been known in fermenters and can contribute materially to ATP, fermentation should not be defined solely by the absence of ETC/ATP synthase energy conservation. This is directly relevant to curation: a chemoorganotroph may express fermentation with membrane-linked energy conservation (e.g., Rnf/Ech-driven ion gradients). (hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 5-6)

### 5.2 Environmental control: electron acceptor availability structures the metabolic mode
Weissbrodt et al. (2023) provide a clear operational vocabulary: **aerobic** (O2 present), **anoxic** (no O2 but alternative acceptors like nitrate/nitrite present), and **anaerobic** (no external terminal acceptors except CO2), mapping cleanly to trait-causal environmental nodes. (weissbrodt2023basicmicrobiologyand pages 16-18)

## 6. Relevant statistics and quantitative data (recent studies)

### 6.1 Prevalence/diversity statistics (2024)
* **>25% of prokaryotes fermentative** (from curated organism descriptions). (hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 2-3)
* **>40 substrates** used and **>50 end products** released across fermentative prokaryotes; specific curated totals include **46 chemically defined substrates** and **55 end products**. (hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 2-3)
* Glucose fermentation mapped to **>120 biochemical reactions**. (hackmann2024thevastlandscape pages 1-2)

### 6.2 Quantitative thermodynamics/cofactor balances for fermentation (2024)
Hackmann (2024) reports standard transformed Gibbs energy per ATP (kJ/mol) for glucose fermentation to various products (∆rG′°/ATP): acetate **−55.1**, lactate **−100.3**, ethanol **−118.1**, succinate **−91.5**, propionate **−105.1**, butyrate **−59.7**; and provides reduced-cofactor balances per mol glucose for reduced NAD(P) and reduced ferredoxin/formate/H2. (hackmann2024thevastlandscape pages 10-11)

### 6.3 Quantitative note on ETC contribution to ATP in a fermenter
Hackmann (2024) reports that in at least one organism, **ETC + ATP synthase contributed up to ~one-third of total ATP**, supporting causal edges that include ETC components even under fermentative classification. (hackmann2024thevastlandscape pages 2-3)

## 7. Candidate nodes (grouped) for `chemoorganotrophic.yaml`

A structured node inventory (with suggested grounding) is provided in the following artifact.

| Node type | Node label | Suggested ontology grounding | Brief role in chemoorganotrophy | Key supporting source |
|---|---|---|---|---|
| process/pathway | chemoorganotrophy | METPO:1000663 | Trait node: energy generation from chemical oxidation of organic compounds; commonly overlaps with chemoorganoheterotrophy when the same organics also supply biomass carbon (weissbrodt2023basicmicrobiologyand pages 16-18, weissbrodt2023basicmicrobiologyand pages 19-22, briski2017environmentalmicrobiology pages 3-4) | doi:10.2166/9781789062304_0009, 2023, https://doi.org/10.2166/9781789062304_0009 |
| process/pathway | aerobic respiration | GO:0009060 | Respiratory chemoorganotrophy branch using O2 as terminal electron acceptor during oxidation of organic electron donors (weissbrodt2023basicmicrobiologyand pages 16-18, weissbrodt2023basicmicrobiologyand pages 19-22) | doi:10.2166/9781789062304_0009, 2023, https://doi.org/10.2166/9781789062304_0009 |
| process/pathway | anaerobic respiration | GO:0009061 | Respiratory chemoorganotrophy branch using inorganic acceptors such as nitrate or nitrite while catabolizing organic electron donors (weissbrodt2023basicmicrobiologyand pages 19-22, weissbrodt2023basicmicrobiologyand pages 16-18) | doi:10.2166/9781789062304_0009, 2023, https://doi.org/10.2166/9781789062304_0009 |
| process/pathway | fermentation | GO:0006113 | Chemoorganotrophic branch in which no external terminal electron acceptor is available and electrons are relocated onto organic catabolic products (weissbrodt2023basicmicrobiologyand pages 16-18, hackmann2024thevastlandscape pages 2-3) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| process/pathway | glycolysis | GO:0006096 | Major entry route for glucose catabolism in chemoorganotrophs, producing pyruvate and reduced cofactors (hackmann2024thevastlandscape pages 5-6, weissbrodt2023basicmicrobiologyand pages 43-44) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| process/pathway | pentose phosphate pathway | GO:0006098 | Alternative glucose entry route contributing reducing power and central metabolites during organic substrate oxidation (hackmann2024thevastlandscape pages 5-6) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| process/pathway | tricarboxylic acid cycle | GO:0006099 | Central oxidative pathway for complete or partial oxidation of organic carbon in respiratory chemoorganotrophy (bettendorff2026electrontransferin pages 9-11, bettendorff2026electrontransferin pages 7-9) | doi:10.3390/biophysica6020027, 2026, https://doi.org/10.3390/biophysica6020027 |
| process/pathway | substrate-level phosphorylation | GO:0006757 | ATP-generating mechanism especially emphasized in fermentative chemoorganotrophy (hackmann2024thevastlandscape pages 1-2, briski2017environmentalmicrobiology pages 15-16) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| process/pathway | respiratory electron transport chain | GO:0022900 | Membrane-associated redox chain coupling electron flow from organic oxidation to ion-gradient generation (garimella2024fromcellsto pages 4-6, weissbrodt2023basicmicrobiologyand pages 43-44) | doi:10.1186/s13213-024-01761-y, 2024, https://doi.org/10.1186/s13213-024-01761-y |
| process/pathway | oxidative phosphorylation | GO:0006119 | ATP synthesis driven by ion motive force produced by the respiratory chain during chemoorganotrophic respiration (garimella2024fromcellsto pages 4-6, gupta2024exploringthebioenergetics pages 15-19) | doi:10.1186/s13213-024-01761-y, 2024, https://doi.org/10.1186/s13213-024-01761-y |
| process/pathway | proton motive force generation | GO:1902600 | Intermediate energetic state linking electron transport to ATP synthesis in respiratory chemoorganotrophy (garimella2024fromcellsto pages 4-6, gupta2024exploringthebioenergetics pages 15-19, weissbrodt2023basicmicrobiologyand pages 43-44) | doi:10.1186/s13213-024-01761-y, 2024, https://doi.org/10.1186/s13213-024-01761-y |
| complex/enzyme | ATP synthase | EC:7.1.2.2 / EC:7.2.2.1 | Converts ion motive force into ATP; present in both respiratory and some fermentative energy conservation schemes (hackmann2024thevastlandscape pages 5-6, garimella2024fromcellsto pages 4-6) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| complex/enzyme | pyruvate:ferredoxin oxidoreductase | EC:1.2.7.1 | Oxidizes pyruvate and generates reduced ferredoxin during anaerobic organic catabolism (hackmann2024thevastlandscape pages 5-6) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| complex/enzyme | Rnf complex (ferredoxin:NAD+ oxidoreductase) | EC:7.2.1.2 | Transfers electrons away from reduced ferredoxin and contributes to ion-gradient-linked energy conservation in anaerobic chemoorganotrophs (hackmann2024thevastlandscape pages 5-6, hackmann2024thevastlandscape pages 9-10) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| complex/enzyme | Ech (energy-converting hydrogenase) | EC:7.1.1.- | Transfers electrons away from reduced ferredoxin and supports ion-coupled energy conservation/H2 metabolism in anaerobic chemoorganotrophs (hackmann2024thevastlandscape pages 5-6) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| complex/enzyme | Nfn (ferredoxin-NAD(P) oxidoreductase) | EC:1.18.1.7 candidate | Redox-balancing enzyme linking NAD(P)H and ferredoxin pools in fermentative chemoorganotrophy (hackmann2024thevastlandscape pages 10-11, hackmann2024thevastlandscape pages 12-13) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| complex/enzyme | NADH dehydrogenase / Complex I entry function | EC:7.1.1.2 candidate | Major respiratory entry point feeding electrons from NADH into the quinone pool during oxidation of organics (garimella2024fromcellsto pages 4-6, gupta2024exploringthebioenergetics pages 15-19) | doi:10.1186/s13213-024-01761-y, 2024, https://doi.org/10.1186/s13213-024-01761-y |
| complex/enzyme | quinol oxidase / cytochrome c oxidase | GO:0015002 candidate | Terminal oxidase classes reducing O2 at the end of branched bacterial ETCs (garimella2024fromcellsto pages 4-6) | doi:10.1186/s13213-024-01761-y, 2024, https://doi.org/10.1186/s13213-024-01761-y |
| complex/enzyme | respiratory formate dehydrogenase | label-only candidate | Oxidizes formate and transfers electrons to terminal acceptors such as O2, nitrate, or fumarate in formate-respiring chemoorganotrophs (sawers2025howfocafacilitates pages 7-8, sawers2025howfocafacilitates pages 1-3) | doi:10.1128/jb.00502-24, 2025, https://doi.org/10.1128/jb.00502-24 |
| complex/enzyme | FocA formate channel | label-only candidate | Bidirectional formate translocator linking organic acid flux to respiration and fermentation in E. coli-like systems (sawers2025howfocafacilitates pages 7-8, sawers2025howfocafacilitates pages 1-3) | doi:10.1128/jb.00502-24, 2025, https://doi.org/10.1128/jb.00502-24 |
| metabolite | glucose | CHEBI:17234 | Common organic substrate entering glycolysis or PPP in chemoorganotrophic metabolism (hackmann2024thevastlandscape pages 5-6, hackmann2024thevastlandscape pages 4-5) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| metabolite | pyruvate | CHEBI:15361 | Central intermediate from sugar catabolism and branching point to lactate, acetyl-CoA, ethanol, and other products (hackmann2024thevastlandscape pages 10-11, hackmann2024thevastlandscape pages 5-6) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| metabolite | acetyl-CoA | CHEBI:15351 | Central hub linking organic oxidation to acetate, butyrate, ethanol, and biosynthetic pathways (hackmann2024thevastlandscape pages 10-11, hackmann2024thevastlandscape pages 5-6) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| metabolite | acetate | CHEBI:30089 | Common chemoorganotrophic end product and respiratory/fermentative carbon oxidation product (hackmann2024thevastlandscape pages 10-11, hackmann2024thevastlandscape pages 2-3) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| metabolite | lactate | CHEBI:24996 | Common fermentation product formed by internal redox balancing of organic catabolism (hackmann2024thevastlandscape pages 10-11, hackmann2024thevastlandscape pages 2-3) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| metabolite | ethanol | CHEBI:16236 | Common fermentation product in chemoorganotrophs and important industrial output (hackmann2024thevastlandscape pages 10-11, hackmann2024thevastlandscape pages 2-3) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| metabolite | succinate | CHEBI:15741 | Organic acid end product/intermediate in some chemoorganotrophic fermentations and respiratory pathways (hackmann2024thevastlandscape pages 10-11, bettendorff2026electrontransferin pages 7-9) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| metabolite | propionate | CHEBI:30769 | Fermentation end product of some chemoorganotrophic pathways (hackmann2024thevastlandscape pages 10-11, hackmann2024thevastlandscape pages 2-3) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| metabolite | butyrate | CHEBI:17968 | Fermentation end product connected to butanoyl-CoA/butyryl-CoA pathways (hackmann2024thevastlandscape pages 10-11, hackmann2024thevastlandscape pages 5-6) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| metabolite | formate | CHEBI:15740 | Organic electron donor/product that can be exported, re-imported, fermented, or respired depending on conditions (sawers2025howfocafacilitates pages 7-8, sawers2025howfocafacilitates pages 1-3, hackmann2024thevastlandscape pages 10-11) | doi:10.1128/jb.00502-24, 2025, https://doi.org/10.1128/jb.00502-24 |
| metabolite | hydrogen | CHEBI:18276 | Fermentation-associated redox sink and energy-linked product in some anaerobic chemoorganotrophs (hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 12-13) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| metabolite | carbon dioxide | CHEBI:16526 | Oxidation/mineralisation product of organic matter and coproduct in several chemoorganotrophic pathways (briski2017environmentalmicrobiology pages 13-15, hackmann2024thevastlandscape pages 2-3) | doi:10.1515/psr-2016-0118, 2017, https://doi.org/10.1515/psr-2016-0118 |
| redox cofactor/carrier | NAD+/NADH | CHEBI:57540 / CHEBI:57945 | Major soluble redox pair accepting electrons from organic oxidation and feeding respiration or fermentation balancing (hackmann2024thevastlandscape pages 5-6, weissbrodt2023basicmicrobiologyand pages 43-44) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| redox cofactor/carrier | NADP+/NADPH | CHEBI:58349 candidate for NADPH; label-only for NADP+ if needed | Additional redox pair contributing anabolic/reductive balancing in chemoorganotrophic metabolism (hackmann2024thevastlandscape pages 10-11, weissbrodt2023basicmicrobiologyand pages 43-44) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| redox cofactor/carrier | ferredoxin (oxidized/reduced) | CHEBI:28463 candidate or label-only | Low-potential carrier central to anaerobic organic catabolism, electron bifurcation, and Rnf/Ech-linked energy conservation (hackmann2024thevastlandscape pages 5-6, hackmann2024thevastlandscape pages 12-13) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| redox cofactor/carrier | quinone pool (ubiquinone/menaquinone) | CHEBI:16389 ubiquinone-8 candidate / label-only broader quinone pool | Membrane mobile carrier receiving electrons from dehydrogenases and delivering them to terminal oxidases in respiratory chemoorganotrophy (garimella2024fromcellsto pages 4-6, gupta2024exploringthebioenergetics pages 15-19) | doi:10.1186/s13213-024-01761-y, 2024, https://doi.org/10.1186/s13213-024-01761-y |
| redox cofactor/carrier | cytochrome c | CHEBI:29036 candidate / label-only | Mobile or periplasmic electron carrier in some branched bacterial respiratory chains (garimella2024fromcellsto pages 4-6) | doi:10.1186/s13213-024-01761-y, 2024, https://doi.org/10.1186/s13213-024-01761-y |
| electron acceptor | oxygen | CHEBI:15379 | Canonical terminal electron acceptor for aerobic respiratory chemoorganotrophy (weissbrodt2023basicmicrobiologyand pages 16-18, garimella2024fromcellsto pages 4-6) | doi:10.2166/9781789062304_0009, 2023, https://doi.org/10.2166/9781789062304_0009 |
| electron acceptor | nitrate | CHEBI:17632 | Alternative inorganic terminal electron acceptor supporting anaerobic respiratory chemoorganotrophy (weissbrodt2023basicmicrobiologyand pages 19-22, weissbrodt2023basicmicrobiologyand pages 16-18, sawers2025howfocafacilitates pages 1-3) | doi:10.2166/9781789062304_0009, 2023, https://doi.org/10.2166/9781789062304_0009 |
| electron acceptor | nitrite | CHEBI:16301 | Alternative inorganic terminal electron acceptor in anoxic respiratory chemoorganotrophy (weissbrodt2023basicmicrobiologyand pages 19-22, weissbrodt2023basicmicrobiologyand pages 16-18) | doi:10.2166/9781789062304_0009, 2023, https://doi.org/10.2166/9781789062304_0009 |
| electron acceptor | fumarate | CHEBI:18012 | Terminal electron acceptor in some formate-linked respiratory systems; useful boundary-case acceptor node (sawers2025howfocafacilitates pages 7-8) | doi:10.1128/jb.00502-24, 2025, https://doi.org/10.1128/jb.00502-24 |
| environmental factor/assay | oxic condition | ENVO:label-only candidate | Presence of O2 favors aerobic respiration and corresponding terminal oxidase use (weissbrodt2023basicmicrobiologyand pages 16-18, garimella2024fromcellsto pages 4-6) | doi:10.2166/9781789062304_0009, 2023, https://doi.org/10.2166/9781789062304_0009 |
| environmental factor/assay | anoxic condition with nitrate/nitrite | ENVO:label-only candidate | Absence of O2 but presence of alternative inorganic acceptors favors anaerobic respiration of organic substrates (weissbrodt2023basicmicrobiologyand pages 16-18) | doi:10.2166/9781789062304_0009, 2023, https://doi.org/10.2166/9781789062304_0009 |
| environmental factor/assay | no external terminal electron acceptor | label-only | Favors fermentation rather than respiration in chemoorganotrophs (weissbrodt2023basicmicrobiologyand pages 16-18) | doi:10.2166/9781789062304_0009, 2023, https://doi.org/10.2166/9781789062304_0009 |
| environmental factor/assay | membrane transport of substrates/products | GO:0055085 candidate | Transport of glucose and fermentation products can affect ATP yield and should be considered as an experimental factor (hackmann2024thevastlandscape pages 10-11) | doi:10.1093/femsre/fuae016, 2024, https://doi.org/10.1093/femsre/fuae016 |
| environmental factor/assay | organic matter biodegradation / mineralisation context | label-only | Application-relevant context in which chemoorganotrophs oxidize organic matter to CO2 and H2O during biodegradation/bioremediation (briski2017environmentalmicrobiology pages 13-15, briski2017environmentalmicrobiology pages 15-16) | doi:10.1515/psr-2016-0118, 2017, https://doi.org/10.1515/psr-2016-0118 |


*Table: This table lists candidate nodes for a chemoorganotrophic TraitMech causal graph, organized by biological type and linked to suggested ontology groundings. It is useful for converting the literature-backed trait definition into curatable graph entities with source support.*

## 8. Evidence-backed candidate causal edges (triples)

A curation-ready edge table with snippets, DOIs, and uncertainty notes is provided below.

| Edge ID | Subject node (suggested grounding) | Predicate | Object node (suggested grounding) | Evidence snippet | Source (DOI, year, URL) | Notes / uncertainty |
|---|---|---|---|---|---|---|
| CHEMOORG-01 | Organic substrate oxidation / glucose catabolism (GO:0016052 candidate; CHEBI:17234 glucose) | produces_reduced_cofactor | NADH / reduced NAD(P) (CHEBI:57945 NADH; CHEBI:58349 NADPH) | “At several points, redox cofactors (NAD and ferredoxin) accept electrons and become reduced.” (hackmann2024thevastlandscape pages 5-6) | Hackmann 2024, doi:10.1093/femsre/fuae016, https://doi.org/10.1093/femsre/fuae016 | Broad chemoorganotrophic edge; supported mainly from fermentation-centered review but generalizable to organic oxidation. |
| CHEMOORG-02 | Pyruvate:ferredoxin oxidoreductase (EC:1.2.7.1) | generates | reduced ferredoxin (CHEBI candidate: ferredoxin(red)) | “pyruvate:ferredoxin oxidoreductase (EC 1.2.7.1) generates reduced ferredoxin” (hackmann2024thevastlandscape pages 5-6) | Hackmann 2024, doi:10.1093/femsre/fuae016, https://doi.org/10.1093/femsre/fuae016 | Strong enzyme-specific edge for anaerobic chemoorganotrophic branches. |
| CHEMOORG-03 | Reduced ferredoxin (label-only candidate) | donates_electrons_to | Rnf complex (EC:7.2.1.2) | “Rnf… transfer electrons away from reduced ferredoxin” (hackmann2024thevastlandscape pages 5-6) | Hackmann 2024, doi:10.1093/femsre/fuae016, https://doi.org/10.1093/femsre/fuae016 | Strong for fermentative/anaerobic systems using Rnf. |
| CHEMOORG-04 | Reduced ferredoxin (label-only candidate) | donates_electrons_to | Ech / energy-converting hydrogenase (EC:7.1.1.-) | “Ech… transfer electrons away from reduced ferredoxin” (hackmann2024thevastlandscape pages 5-6) | Hackmann 2024, doi:10.1093/femsre/fuae016, https://doi.org/10.1093/femsre/fuae016 | Strong for taxa encoding Ech; not universal across all chemoorganotrophs. |
| CHEMOORG-05 | Rnf complex (EC:7.2.1.2) | contributes_to_formation_of | ion gradient / sodium- or proton-motive force (GO:1902600 candidate) | “These ions in turn drive ATP formation by two different ATP synthases” after Rnf/Ech electron transfer (hackmann2024thevastlandscape pages 5-6) | Hackmann 2024, doi:10.1093/femsre/fuae016, https://doi.org/10.1093/femsre/fuae016 | Inferred from quoted sentence; ion identity can vary, so mark somewhat uncertain. |
| CHEMOORG-06 | Ech complex (EC:7.1.1.-) | contributes_to_formation_of | ion gradient / proton motive force (GO:1902600 candidate) | “These ions in turn drive ATP formation by two different ATP synthases” after Rnf/Ech electron transfer (hackmann2024thevastlandscape pages 5-6) | Hackmann 2024, doi:10.1093/femsre/fuae016, https://doi.org/10.1093/femsre/fuae016 | Inferred coupling edge; direction and ion specificity depend on system. |
| CHEMOORG-07 | Ion gradient / proton motive force (GO:1902600 candidate) | drives | ATP synthase (EC:7.1.2.2 / EC:7.2.2.1) | “These ions in turn drive ATP formation by two different ATP synthases” (hackmann2024thevastlandscape pages 5-6) | Hackmann 2024, doi:10.1093/femsre/fuae016, https://doi.org/10.1093/femsre/fuae016 | Strong direct support for ion-gradient-coupled ATP synthesis. |
| CHEMOORG-08 | ATP synthase (EC:7.1.2.2 / EC:7.2.2.1) | synthesizes | ATP (CHEBI:15422) | “These ions in turn drive ATP formation by two different ATP synthases” (hackmann2024thevastlandscape pages 5-6) | Hackmann 2024, doi:10.1093/femsre/fuae016, https://doi.org/10.1093/femsre/fuae016 | Strong. |
| CHEMOORG-09 | NADH dehydrogenase / dehydrogenase level entry (EC:7.1.1.2 candidate) | feeds_electrons_to | quinone pool (CHEBI:17976 ubiquinone; menaquinone label-only) | “Electrons enter at three levels—the dehydrogenase level, the quinone pool, or the mobile carrier level—and some dehydrogenases inject electrons into the quinone pool” (garimella2024fromcellsto pages 4-6) | Garimella et al. 2024, doi:10.1186/s13213-024-01761-y, https://doi.org/10.1186/s13213-024-01761-y | Good generic ETC edge for respiratory chemoorganotrophy. |
| CHEMOORG-10 | Quinone pool (ubiquinone/menaquinone; CHEBI:17976 candidate) | transfers_electrons_to | terminal oxidase / quinol oxidase / cytochrome c oxidase (GO:0015002 candidate) | “quinoI oxidases pass electrons from ubiquinols/menaquinones to oxygen” (garimella2024fromcellsto pages 4-6) | Garimella et al. 2024, doi:10.1186/s13213-024-01761-y, https://doi.org/10.1186/s13213-024-01761-y | Strong for aerobic respiratory branches. |
| CHEMOORG-11 | Electron transport chain (GO:0022900) | generates | proton motive force (GO:1902600 candidate) | “bacterial ETCs are embedded in the plasma membrane and generate a membrane potential/proton motive force by proton-pumping complexes” (garimella2024fromcellsto pages 4-6) | Garimella et al. 2024, doi:10.1186/s13213-024-01761-y, https://doi.org/10.1186/s13213-024-01761-y | Strong core respiration edge. |
| CHEMOORG-12 | Proton motive force (GO:1902600 candidate) | powers | ATP synthase (EC:7.1.2.2 / EC:7.2.2.1) | “The proton motive force drives ATP synthesis via ATP synthase” (garimella2024fromcellsto pages 4-6) | Garimella et al. 2024, doi:10.1186/s13213-024-01761-y, https://doi.org/10.1186/s13213-024-01761-y | Strong core respiration edge. |
| CHEMOORG-13 | Oxygen present (CHEBI:15379; environmental condition) | enables | aerobic respiration mode (GO:0009060 candidate) | “electron acceptors range from O2 in aerobic respiration” (weissbrodt2023basicmicrobiologyand pages 16-18) | Weissbrodt et al. 2023, doi:10.2166/9781789062304_0009, https://doi.org/10.2166/9781789062304_0009 | Strong scope-defining edge. |
| CHEMOORG-14 | Nitrate or nitrite present (CHEBI:17632 nitrate; CHEBI:16301 nitrite) | enables | anaerobic respiration mode (GO:0009061 candidate) | “anoxic (absence of O2 but presence of alternative inorganic acceptors like nitrite/nitrate)” and organisms “catabolize an organic e-donor by respiration with an inorganic e-acceptor such as nitrite or nitrate” (weissbrodt2023basicmicrobiologyand pages 16-18, weissbrodt2023basicmicrobiologyand pages 19-22) | Weissbrodt et al. 2023, doi:10.2166/9781789062304_0009, https://doi.org/10.2166/9781789062304_0009 | Strong for denitrifying/anoxic chemoorganotrophy. |
| CHEMOORG-15 | Absence of external terminal electron acceptor (environmental condition) | leads_to | fermentation (GO:0006113) | “In fermentation, no terminal e-acceptor is available; electrons are relocated onto an organic catabolic product.” (weissbrodt2023basicmicrobiologyand pages 16-18) | Weissbrodt et al. 2023, doi:10.2166/9781789062304_0009, https://doi.org/10.2166/9781789062304_0009 | Strong distinction from respiratory chemoorganotrophy. |
| CHEMOORG-16 | Fermentation (GO:0006113) | generates_ATP_via | substrate-level phosphorylation (GO:0006757 candidate) | “Fermentation is described as… ATP is generated primarily by substrate-level phosphorylation” (hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 2-3) | Hackmann 2024, doi:10.1093/femsre/fuae016, https://doi.org/10.1093/femsre/fuae016 | Strong, though Hackmann notes exceptions with ETC contribution. |
| CHEMOORG-17 | Membrane transport of glucose / fermentation products (GO:1901264 candidate; label-only) | affects | ATP yield (label-only) | “Transport of glucose and fermentation products across the cell membrane is not represented, though this can affect the yield of ATP.” (hackmann2024thevastlandscape pages 10-11) | Hackmann 2024, doi:10.1093/femsre/fuae016, https://doi.org/10.1093/femsre/fuae016 | Valuable experimental-factor edge; quantitative direction depends on substrate/product transport stoichiometry. |
| CHEMOORG-18 | FocA-mediated formate transport (UniProt/EC grounding unresolved; label-only) | supplies_substrate_to | respiratory formate dehydrogenases reducing O2/nitrate/fumarate (EC family label-only) | “FocA… supplies formate to respiratory formate dehydrogenases that can reduce terminal electron acceptors (‘O2, nitrate, or fumarate’)” (sawers2025howfocafacilitates pages 7-8, sawers2025howfocafacilitates pages 1-3) | Sawers 2025, doi:10.1128/jb.00502-24, https://doi.org/10.1128/jb.00502-24 | Taxon-specific (E. coli) but mechanistically useful example of chemoorganotrophic formate respiration; mark uncertain for generic graph. |


*Table: This table lists evidence-backed candidate subject-predicate-object edges for a chemoorganotrophic TraitMech graph, emphasizing organic oxidation, respiratory/fermentative energy conservation, and environmental determinants. It is useful as a curation-ready starting point because each edge includes a short supporting quote, source, and uncertainty note.*

## 9. Ontology grounding notes (practical curation guidance)

* **Prefer stable identifiers already present in evidence**: EC numbers for Rnf (EC 7.2.1.2), ATP synthase variants (EC 7.1.2.2 / 7.2.2.1), pyruvate:ferredoxin oxidoreductase (EC 1.2.7.1) are explicitly cited and strong candidates. (hackmann2024thevastlandscape pages 5-6)
* **GO process nodes** are appropriate for: glycolysis, PPP, TCA cycle, respiratory electron transport chain, oxidative phosphorylation, fermentation, substrate-level phosphorylation. (garimella2024fromcellsto pages 4-6, hackmann2024thevastlandscape pages 5-6)
* **CHEBI** can anchor common metabolites/e-acceptors (O2, nitrate, nitrite, glucose, acetate, etc.), but where exact CHEBI IDs are uncertain from the provided snippets, label-only nodes should be used during curation. (weissbrodt2023basicmicrobiologyand pages 16-18, hackmann2024thevastlandscape pages 10-11)

## 10. Warnings / claims not ready for curation

1. **Avoid equating “chemoorganotrophic” with “aerobic”**: chemoorganotrophs can be aerobic respirers, anaerobic respirers (e.g., denitrifiers), or fermenters depending on electron acceptors. (weissbrodt2023basicmicrobiologyand pages 19-22, weissbrodt2023basicmicrobiologyand pages 16-18)
2. **Do not treat “absence of ETC” as a defining feature of fermentation**: Hackmann documents ETC contributions in fermenters (up to ~1/3 ATP in one case), so a causal graph should permit ETC-related nodes for some fermentative chemoorganotrophs but mark them as conditional/taxon-specific. (hackmann2024thevastlandscape pages 2-3)
3. **E. coli formate edges are taxon-specific**: FocA/formate dehydrogenase examples are useful mechanistically but should be curated as *example subgraph* or marked uncertain for general chemoorganotrophy. (sawers2025howfocafacilitates pages 7-8, sawers2025howfocafacilitates pages 1-3)

## 11. DOI-first bibliography (with publication dates and URLs)

1. **Hackmann, T.J.** (2024-05). *The vast landscape of carbohydrate fermentation in prokaryotes.* **FEMS Microbiology Reviews** 48. DOI: **10.1093/femsre/fuae016**. URL: https://doi.org/10.1093/femsre/fuae016 (hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 10-11)
2. **Weissbrodt, D.G., Laureni, M., van Loosdrecht, M.C.M., Comeau, Y.** (2023-05). *Basic microbiology and metabolism.* In: **Biological Wastewater Treatment** (IWA Publishing). DOI: **10.2166/9781789062304_0009**. URL: https://doi.org/10.2166/9781789062304_0009 (weissbrodt2023basicmicrobiologyand pages 16-18, weissbrodt2023basicmicrobiologyand pages 19-22)
3. **Garimella, S.S.S., Rachakonda, S.V., Pratapa, S.S., Mannem, G.D., Mahidhara, G.** (2024-06). *From cells to power cells: harnessing bacterial electron transport for microbial fuel cells (MFCs).* **Annals of Microbiology** 74:1-15. DOI: **10.1186/s13213-024-01761-y**. URL: https://doi.org/10.1186/s13213-024-01761-y (garimella2024fromcellsto pages 4-6)
4. **Briški, F., Vuković Domanovac, M.** (2017-10). *Environmental microbiology.* **Physical Sciences Reviews** 2(11). DOI: **10.1515/psr-2016-0118**. URL: https://doi.org/10.1515/psr-2016-0118 (briski2017environmentalmicrobiology pages 15-16, briski2017environmentalmicrobiology pages 13-15)
5. **Sawers, R.G.** (2025-02). *How FocA facilitates fermentation and respiration of formate by Escherichia coli.* **Journal of Bacteriology** 207(2). DOI: **10.1128/jb.00502-24**. URL: https://doi.org/10.1128/jb.00502-24 (sawers2025howfocafacilitates pages 1-3)



References

1. (weissbrodt2023basicmicrobiologyand pages 16-18): David G. Weissbrodt, Michele Laureni, Mark C.M. van Loosdrecht, and Yves Comeau. Basic microbiology and metabolism. Biological Wastewater Treatment, pages 9-74, May 2023. URL: https://doi.org/10.2166/9781789062304\_0009, doi:10.2166/9781789062304\_0009. This article has 20 citations.

2. (weissbrodt2023basicmicrobiologyand pages 19-22): David G. Weissbrodt, Michele Laureni, Mark C.M. van Loosdrecht, and Yves Comeau. Basic microbiology and metabolism. Biological Wastewater Treatment, pages 9-74, May 2023. URL: https://doi.org/10.2166/9781789062304\_0009, doi:10.2166/9781789062304\_0009. This article has 20 citations.

3. (garimella2024fromcellsto pages 4-6): Sri Sathya Sandilya Garimella, Sai Vennela Rachakonda, Sai Sowmya Pratapa, Gnana Divya Mannem, and Ganesh Mahidhara. From cells to power cells: harnessing bacterial electron transport for microbial fuel cells (mfcs). Annals of Microbiology, 74:1-15, Jun 2024. URL: https://doi.org/10.1186/s13213-024-01761-y, doi:10.1186/s13213-024-01761-y. This article has 25 citations and is from a peer-reviewed journal.

4. (hackmann2024thevastlandscape pages 2-3): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

5. (briski2017environmentalmicrobiology pages 3-4): Felicita Briški and Marija Vuković Domanovac. Environmental microbiology. Physical Sciences Reviews, Oct 2017. URL: https://doi.org/10.1515/psr-2016-0118, doi:10.1515/psr-2016-0118. This article has 32 citations and is from a peer-reviewed journal.

6. (hackmann2024thevastlandscape pages 1-2): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

7. (hackmann2024thevastlandscape pages 5-6): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

8. (briski2017environmentalmicrobiology pages 15-16): Felicita Briški and Marija Vuković Domanovac. Environmental microbiology. Physical Sciences Reviews, Oct 2017. URL: https://doi.org/10.1515/psr-2016-0118, doi:10.1515/psr-2016-0118. This article has 32 citations and is from a peer-reviewed journal.

9. (briski2017environmentalmicrobiology pages 13-15): Felicita Briški and Marija Vuković Domanovac. Environmental microbiology. Physical Sciences Reviews, Oct 2017. URL: https://doi.org/10.1515/psr-2016-0118, doi:10.1515/psr-2016-0118. This article has 32 citations and is from a peer-reviewed journal.

10. (hackmann2024thevastlandscape pages 10-11): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

11. (weissbrodt2023basicmicrobiologyand pages 43-44): David G. Weissbrodt, Michele Laureni, Mark C.M. van Loosdrecht, and Yves Comeau. Basic microbiology and metabolism. Biological Wastewater Treatment, pages 9-74, May 2023. URL: https://doi.org/10.2166/9781789062304\_0009, doi:10.2166/9781789062304\_0009. This article has 20 citations.

12. (bettendorff2026electrontransferin pages 9-11): Lucien Bettendorff. Electron transfer in biological systems. Biophysica, 6:27, Mar 2026. URL: https://doi.org/10.3390/biophysica6020027, doi:10.3390/biophysica6020027. This article has 16 citations.

13. (bettendorff2026electrontransferin pages 7-9): Lucien Bettendorff. Electron transfer in biological systems. Biophysica, 6:27, Mar 2026. URL: https://doi.org/10.3390/biophysica6020027, doi:10.3390/biophysica6020027. This article has 16 citations.

14. (gupta2024exploringthebioenergetics pages 15-19): P Gupta. Exploring the bioenergetics of bacterial spore germination using bacillus megaterium. Unknown journal, 2024.

15. (hackmann2024thevastlandscape pages 9-10): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

16. (hackmann2024thevastlandscape pages 12-13): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

17. (sawers2025howfocafacilitates pages 7-8): R. Gary Sawers. How foca facilitates fermentation and respiration of formate by <i>escherichia coli</i>. Feb 2025. URL: https://doi.org/10.1128/jb.00502-24, doi:10.1128/jb.00502-24. This article has 14 citations and is from a peer-reviewed journal.

18. (sawers2025howfocafacilitates pages 1-3): R. Gary Sawers. How foca facilitates fermentation and respiration of formate by <i>escherichia coli</i>. Feb 2025. URL: https://doi.org/10.1128/jb.00502-24, doi:10.1128/jb.00502-24. This article has 14 citations and is from a peer-reviewed journal.

19. (hackmann2024thevastlandscape pages 4-5): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.