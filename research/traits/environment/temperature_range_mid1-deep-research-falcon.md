---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:18:40.549589'
end_time: '2026-08-04T04:24:44.785763'
duration_seconds: 364.24
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range mid1
  trait_identifier: METPO:1000450
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range spans approximately 22\u201327 \xB0C, characteristic of mesophilic\
    \ physiology."
  parent_traits: METPO:1000306
  synonyms: Mesophilie, TR_22_to_27
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports the 22\u201327 \xB0C range as a lower\
    \ mesophile growth range.)"
  causal_graph_summary: 'temperature_range_mid1_lower_mesophile: 13 nodes, 8 edges'
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
- **Trait label:** temperature range mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000450
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 22–27 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_22_to_27
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 22–27 °C range as a lower mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid1_lower_mesophile: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid1.yaml`.

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
- **Trait label:** temperature range mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000450
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 22–27 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_22_to_27
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 22–27 °C range as a lower mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid1_lower_mesophile: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid1.yaml`.

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


# Curation report: microbial “temperature range mid1”

## Executive curation recommendation

**Trait:** temperature range mid1  
**Identifier:** `METPO:1000450`  
**Parent:** `METPO:1000306`  
**Supplied definition:** “A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 22–27 °C, characteristic of mesophilic physiology.”  
**Synonyms:** Mesophilie; TR_22_to_27

The most defensible core mechanism is:

> **lower ambient temperature → increased membrane lipid order → DesK kinase signaling → DesR phosphorylation → `des` transcription → Δ5-desaturase activity → more cis-unsaturated membrane fatty acids → preservation of low-temperature membrane fluidity → support of cellular physiology and growth**.

This backbone is directly established in *Bacillus subtilis*. A 2026 study—not a 2023–2024 source, but uniquely aligned with the target interval—directly measured a fluidity-homeostasis regime below 26 °C and demonstrated loss of that regime in a `Δdes` mutant. Its relevance is unusually high because the experimentally resolved transition lies inside the supplied 22–27 °C interval. However, the terminal edge from membrane fluidity to the exact ontology-level phenotype remains an inference unless matched growth curves demonstrate that perturbing the mechanism changes growth across 22–27 °C. (barbotin2026twotemperaturedependentmembrane pages 1-2)

| Priority | Candidate mechanism | Best-supported organism/temperature | Evidence strength | Curation recommendation |
|---|---|---|---|---|
| 1 | DesK/DesR → **des** (Δ5 desaturase) → increased unsaturated fatty acids → maintenance of membrane fluidity at low temperature | *Bacillus subtilis*; direct membrane-fluidity measurements across **20–37 °C**, with fluidity maintained **<26 °C**; cold shift **37→20 °C** and FA analysis after **45 min at 22 °C** (barbotin2026twotemperaturedependentmembrane pages 1-2, mendoza2014temperaturesensingby pages 5-6) | **Strong, direct, mechanistic** | **Curate now as core graph backbone** for lower-mesophile adaptation; note organism is Gram-positive and temperature window is inferred to cover **22–25 °C**, not all 27 °C. |
| 2 | Reduced anteiso-branched-chain fatty acids increases membrane order, which activates DesK/DesR and **des** transcription | *B. subtilis*; isoleucine limitation and **37 °C isothermal** manipulations affecting α-BCFAs; review of cold adaptation and long-term membrane remodeling (mendoza2014temperaturesensingby pages 5-6, barbotin2026twotemperaturedependentmembrane pages 1-2) | **Moderate, mechanistic but indirect for trait range** | **Curate with caution** as an upstream membrane-order input to DesK/DesR; mark **not directly tested at 22–27 °C** and partly inferred from composition-perturbation experiments. |
| 3 | Homeoviscous lipid remodeling with increased C16:1/C18:1 in phospholipids during cooler growth | *Acinetobacter baumannii* clinical strains; **18 °C vs 37 °C**; five of six strains increased **C16:1** at 18 °C, one strain increased **C18:1**; total UFA **60–80%** at 18 °C (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 4-8, dessenne2024lipidomicanalysesreveal pages 8-12, dessenne2024lipidomicanalysesreveal pages 2-4) | **Moderate, direct but taxon/temperature specific** | **Curate as supporting general membrane-adaptation evidence**, not as universal node logic; mark **Gram-negative, strain-specific, and outside direct 22–27 °C testing**. |
| 4 | CspA/CsdA RNA chaperone and helicase functions relieve low-temperature RNA secondary structure, support translation/ribosome recovery | *Escherichia coli*; cold-shock response literature, not trait-specific; CspA can reach **~15% of total protein synthesis** after cold shock; CsdA supports ribosome maintenance under cold shock (moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 7-9) | **Moderate for cold stress, weak for METPO:1000450 specificity** | **Do not make core causal edge to 22–27 °C growth yet**; keep as **candidate auxiliary module** for transition into lower temperatures, flagged **cold-shock/assay-specific**. |
| 5 | Trigger factor / PPIase-assisted protein folding at low temperature | Primarily *E. coli* cold-response literature; trigger factor reported **~40-fold overexpression at low temperatures**; PPIases overexpressed to accelerate slow proline isomerization (moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 5-6) | **Weak-to-moderate, indirect** | **Hold for later curation** unless a taxon with direct 22–27 °C growth phenotype is found; mark **not directly tested at 22–27 °C** and largely **general low-temperature adaptation**. |
| 6 | Trehalose accumulation via **otsAB** contributes to cold tolerance | *E. coli*; low-temperature response, with **otsA** mutant showing cold-shock sensitivity (moon2023temperaturemattersbacterial pages 5-6) | **Weak for this trait** | **Do not curate into core TraitMech graph yet**; possible environmental-stress support node only, clearly **cold-shock specific** and **not demonstrated for mesophilic 22–27 °C growth range**. |
| 7 | Heat-shock proteostasis network (DnaK/DnaJ, GroEL/ES, ClpB, Lon, ClpXP, FtsH, RpoH/RpoE) supports growth at elevated temperatures | *E. coli* and broad bacterial review evidence; several claims centered on **>30 °C**, heat shock, or **23–42 °C** translation behavior (moon2023temperaturemattersbacterial pages 6-7, moon2023temperaturemattersbacterial pages 5-6) | **Strong for heat stress, poor match to trait window** | **Exclude from core METPO:1000450 graph for now** except possibly as a boundary-case note distinguishing lower mesophiles from warmer mesophiles; mark **temperature-mismatch**. |
| 8 | Membrane fluidity itself as proximal physiological mediator of lower-mesophile growth | *B. subtilis* direct TIR-FCS fluidity data **20–37 °C** and general membrane-sensing review evidence (barbotin2026twotemperaturedependentmembrane pages 1-2, mendoza2014temperaturesensingby pages 5-6) | **Strong** | **Curate as central physiological state node** linking ambient temperature to cellular performance; supported as a general mediator, though exact growth-rate consequences at each point in **22–27 °C** remain partly inferred. |


*Table: This table ranks candidate mechanisms for curating METPO:1000450 by how directly they support growth in the lower-mesophile temperature window. It highlights which mechanisms are ready for core curation and which remain taxon-specific, assay-specific, or outside direct 22–27 °C testing.*

## 1. Trait scope and boundaries

### Operational interpretation

`METPO:1000450` should represent an **assay-observed temperature-range phenotype**: an organism can sustain measurable growth under the specified medium, atmosphere, pH, pressure, and incubation conditions at temperatures spanning approximately 22–27 °C. It should not automatically assert:

- that the organism’s optimum temperature is within 22–27 °C;
- that 22 °C and 27 °C are exact cardinal minimum and maximum temperatures;
- that growth is equally rapid throughout the interval;
- that transient survival following a temperature shift constitutes growth;
- or that every organism assigned the trait uses the same mechanism.

The interval straddles a mechanistically interesting boundary. Direct measurements in *B. subtilis*, *Streptococcus pneumoniae*, and *Staphylococcus aureus* found membrane fluidity maintained below 26 °C but increasing with temperature above that threshold. Thus, 22–25 °C may engage active low-temperature fluidity control, whereas 26–27 °C may fall near or above the transition in the tested Gram-positive organisms. This argues against treating the entire interval as a single uniform molecular state. (barbotin2026twotemperaturedependentmembrane pages 1-2)

### Boundary cases

1. **Psychrophile or psychrotolerant:** growth at 22 °C alone does not distinguish lower mesophily from broad cold tolerance. Cardinal-temperature or multi-point growth data are needed.
2. **Canonical mesophile with a warmer optimum:** an organism optimized at 30–37 °C may still grow at 22–27 °C. The trait describes supported range, not optimum.
3. **Cold-shock survival:** induction after a 37→20/22 °C shift supports an adaptation mechanism but is not by itself evidence of sustained growth across the complete interval.
4. **Dormancy or maintenance metabolism:** viability, respiration, or ATP maintenance without biomass increase should not satisfy a growth-range class.
5. **Assay dependence:** medium composition, oxygen, pH, inoculum history, and incubation duration can move apparent growth boundaries. The assay context should accompany the annotation.

## 2. Candidate graph nodes

### Environmental and experimental nodes

- ambient temperature, 22–27 °C — label-only range node linked to `METPO:1000450`;
- downward temperature shift / cold shock — experimental factor, not equivalent to the trait;
- ambient temperature, 20 °C, 22 °C, 26 °C, 27 °C, and 37 °C — literal measurement nodes or assay attributes;
- isoleucine availability — `CHEBI:24898` is a candidate grounding for L-isoleucine only after checking the intended ChEBI entity;
- membrane physical state: increased lipid order / reduced fluidity — label-only physiological-state node;
- growth medium, oxygen, pH, pressure, and incubation time — assay-context nodes.

### Cellular structures and processes

- plasma membrane — `GO:0005886`;
- membrane organization — `GO:0061024`;
- membrane fluidity homeostasis / homeoviscous adaptation — label-only unless the project has a preferred process ontology term;
- fatty-acid desaturation — candidate GO process, identifier should be ontology-verified before insertion;
- phospholipid metabolic process — `GO:0006644`;
- translation — `GO:0006412`;
- protein folding — `GO:0006457`;
- ribosome biogenesis — `GO:0042254`;
- response to cold — `GO:0009409`.

### Genes, proteins, enzymes, and complexes

**Core, *B. subtilis*-specific**

- DesK, membrane histidine kinase/cold sensor — label-only or organism-specific UniProt entry after strain selection;
- DesR, response regulator;
- DesR-P, phosphorylated active response regulator;
- `des`, desaturase gene;
- Des/Δ5-desaturase, polytopic membrane protein introducing a cis double bond at the Δ5 position;
- branched-chain keto-acid dehydrogenase, BKDH;
- LipA, lipoate synthase-associated input to BKDH function.

**Supporting or provisional modules**

- FabA and FabB, type-II unsaturated-fatty-acid biosynthesis proteins;
- CspA, cold-shock RNA chaperone;
- CsdA, ATP-dependent RNA helicase;
- RNase R;
- trigger factor, ribosome-associated chaperone/PPIase;
- DnaK–DnaJ, GroEL–GroES, ClpB, Lon, ClpXP, FtsH;
- RpoS, DsrA, RprA, and OtsAB.

Because protein identifiers are strain-specific, UniProt CURIEs should be assigned only after the graph specifies the source organism and strain.

### Chemicals and lipid classes

- unsaturated fatty acids — class node; do not collapse all species into one chemically exact molecule;
- saturated fatty acids;
- anteiso-branched-chain fatty acids (a-BCFAs);
- palmitoleic acid (C16:1) — ChEBI grounding should distinguish free acid from acyl-chain residue;
- oleic acid (C18:1) — `CHEBI:16196` is a candidate for the free acid, subject to verification;
- cis-vaccenic acid — ontology verification required;
- palmitic acid — `CHEBI:15756` is a candidate for the free acid, subject to verification;
- phosphatidylethanolamine and phosphatidylglycerol — class nodes rather than single molecular species;
- ferredoxin or flavodoxin — electron donors for Δ5-desaturase;
- ATP;
- trehalose — `CHEBI:27082` is a candidate, subject to verification.

### Taxa

- *Bacillus subtilis* — `NCBITaxon:1423` at species level;
- *Escherichia coli* — `NCBITaxon:562`;
- *Acinetobacter baumannii* — `NCBITaxon:470`;
- *Staphylococcus aureus* — `NCBITaxon:1280`;
- *Streptococcus pneumoniae* — `NCBITaxon:1313`.

## 3. Candidate causal edges

| Subject | Predicate | Object | Evidence snippet | Reference | Curation note |
|---|---|---|---|---|---|
| Decreased ambient temperature | increases | membrane lipid order / reduces fluidity | “Typically, a reduction in temperature causes a less fluid and thus more viscous, membrane.” | 10.1128/msphere.00095-26 | **Core physical edge.** General, but the magnitude depends on lipid composition. (barbotin2026twotemperaturedependentmembrane pages 1-2) |
| Membrane fluidity below 26 °C | is maintained by | active homeostatic feedback | “membrane fluidity was constant below 26°C and evolved linearly with temperature above this temperature” | 10.1128/msphere.00095-26 | **Direct, highly relevant.** Tested over 20–37 °C in three Gram-positive bacteria; do not generalize universally. (barbotin2026twotemperaturedependentmembrane pages 1-2) |
| `des` deletion | disrupts | low-temperature membrane-fluidity homeostasis | “Fluidity was no longer constant below 26°C… confirming the role of Des” | 10.1128/msphere.00095-26 | **Direct causal perturbation; curate.** *B. subtilis*-specific. (barbotin2026twotemperaturedependentmembrane pages 1-2) |
| Cold exposure at 22 °C | causes via Des | appearance of unsaturated fatty acids | “appearance of unsaturated FA exclusively in wild-type cells after cold exposure” | 10.1128/msphere.00095-26 | **Direct and in-range at 22 °C.** Comparison was WT versus `Δdes` after cold shock. (barbotin2026twotemperaturedependentmembrane pages 1-2) |
| 37→20 °C shift | induces | UFA synthesis | “when a culture grown at 37°C is transferred to 20°C, the synthesis of UFAs is induced” | 10.1146/annurev-micro-091313-103612 | Strong historical mechanism, but 20 °C is just below the target interval. (mendoza2014temperaturesensingby pages 5-6) |
| DesK autophosphorylation | phosphorylates | DesR | “Autophosphorylated DesK… transfers the phosphoryl group to… DesR” | 10.1146/annurev-micro-091313-103612 | **Core signaling edge.** *B. subtilis*. (mendoza2014temperaturesensingby pages 5-6) |
| DesR-P | activates transcription of | `des` | “DesR-P… binds DNA, promoting expression of the des gene” | 10.1146/annurev-micro-091313-103612 | **Core signaling edge.** (mendoza2014temperaturesensingby pages 5-6) |
| `des` | encodes | membrane-bound Δ5-desaturase | “The des gene encodes a polytopic membrane-bound desaturase” | 10.1146/annurev-micro-091313-103612 | **Core gene-product edge.** (mendoza2014temperaturesensingby pages 5-6) |
| Δ5-desaturase | introduces | cis double bonds into saturated fatty acids | It “catalyzes the introduction of a cis double bond at the Δ5 position of a wide range of saturated fatty acids” | 10.1146/annurev-micro-091313-103612 | **Core biochemical edge.** Ferredoxin or flavodoxin supplies electrons. (mendoza2014temperaturesensingby pages 5-6) |
| More cis-UFAs | increases | membrane fluidity | Unsaturated chains pack less tightly; increasing their abundance increases membrane fluidity | 10.1007/s12275-023-00031-x | Broadly supported review edge; exact effect depends on lipid species and headgroups. (moon2023temperaturemattersbacterial pages 7-9) |
| Isoleucine limitation | decreases | anteiso-BCFAs | “Limiting the supply of isoleucine dramatically reduces the amount of a-BCFAs” | 10.1146/annurev-micro-091313-103612 | **Direct upstream manipulation**, but tested isothermally rather than as the target phenotype. (mendoza2014temperaturesensingby pages 5-6) |
| Reduced a-BCFAs | increases | membrane lipid order | Reduced a-BCFAs resulted “in ordered membrane lipids” | 10.1146/annurev-micro-091313-103612 | Curate as *B. subtilis*-specific membrane-composition edge. (mendoza2014temperaturesensingby pages 5-6) |
| Increased membrane order | activates | DesK/DesR-dependent `des` transcription | Isoleucine-free growth activated `des` “under isothermal conditions, using a DesK/DesR-dependent mechanism” | 10.1146/annurev-micro-091313-103612 | Important evidence that membrane state, not temperature alone, is the sensed variable. (mendoza2014temperaturesensingby pages 5-6) |
| Restored membrane fluidity | inhibits | phosphate flux from DesK to DesR | “when membrane fluidity is restored the transcription of des is shut off” | 10.1146/annurev-micro-091313-103612 | **Negative-feedback edge; curate.** (mendoza2014temperaturesensingby pages 5-6) |
| Growth at 18 °C | increases | C16:1 in five *A. baumannii* strains | Five strains increased palmitoleic acid at 18 °C | 10.1128/spectrum.00757-24 | Direct 2024 evidence but below target range and strain-specific. (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12) |
| Growth at 18 °C | increases in ABVal2 | C18:1 | ABVal2 “uniquely elevated oleic acid (C18:1)” | 10.1128/spectrum.00757-24 | **Uncertain/generalization prohibited.** Single-strain pattern. (dessenne2024lipidomicanalysesreveal pages 8-12) |
| FabA/FabB insertion | may contribute to | strain-specific UFA remodeling | ABVal2 and ABVal3 contained a ∼20-gene insertion including FabA and FabB | 10.1128/spectrum.00757-24 | **Do not encode as proven causation:** genomic association without gene perturbation. (dessenne2024lipidomicanalysesreveal pages 8-12) |
| Low temperature | stabilizes | RNA secondary structure | Cold-stabilized RNA structures can prevent ribosome binding and alter turnover/transcription | 10.1007/s12275-023-00031-x | General cold-response edge; not demonstrated specifically at 22–27 °C. (moon2023temperaturemattersbacterial pages 3-5) |
| CspA | reduces | inhibitory RNA secondary structure | CspA “acts as an RNA chaperone that prevents secondary structure formation of RNA” | 10.1007/s12275-023-00031-x | Candidate auxiliary edge; mostly *E. coli* cold-shock evidence. (moon2023temperaturemattersbacterial pages 7-9) |
| CsdA | supports | cold-adapted ribosome function/resynthesis | CsdA binds ribosomes and transforms them into a translation-capable cold-shock form | 10.1007/s12275-023-00031-x | Auxiliary, taxon- and shock-specific; not yet a core trait edge. (moon2023temperaturemattersbacterial pages 7-9) |
| Low temperature | increases | trigger-factor abundance | Trigger factor shows “~40-fold overexpression at low temperatures” | 10.1007/s12275-023-00031-x | Quantitative but not tied to 22–27 °C; hold as provisional. (moon2023temperaturemattersbacterial pages 7-9) |
| OtsAB-derived trehalose | supports | cold-shock tolerance | *E. coli* accumulates trehalose at low temperatures and an `otsA` mutant is cold-shock sensitive | 10.1007/s12275-023-00031-x | **Weak for this trait:** survival evidence, not growth-range causation. (moon2023temperaturemattersbacterial pages 5-6) |
| Appropriate membrane fluidity | supports | `METPO:1000450` | Membrane fluidity governs protein function, respiration, and antibiotic uptake; Des-dependent control operates around 22–26 °C | 10.1128/msphere.00095-26 | **Inferred terminal edge.** Curate only with an uncertainty flag until growth-rate rescue/knockout data in the complete interval are available. (barbotin2026twotemperaturedependentmembrane pages 1-2) |

## 4. Recent findings and quantitative data

### 2024 strain-resolved lipidomics

Dessenne and colleagues compared six clinical *A. baumannii* strains at 18 and 37 °C. At 18 °C, total UFAs accounted for approximately **60–80%** of measured fatty acids. Five strains increased C16:1, whereas ABVal2 showed a distinct C18:1-centered response. PE and PG were the principal phospholipid classes accommodating the UFA changes. This is important evidence that “more UFA at lower temperature” is not one uniform chemical program: both the chain species and phospholipid context vary by strain. (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12)

Growth also slowed strongly at 18 °C. ABVal2 doubled in **162 min at 18 °C versus 29 min at 37 °C**; AB5075 doubled in **109 min versus 25 min**, respectively. No tested strain displayed twitching motility at 18 °C, while biofilm responses differed among strains. These data demonstrate that membrane remodeling accompanies substantial changes in growth and behavior, but they do not prove that a particular lipid species causes the growth difference. (dessenne2024lipidomicanalysesreveal pages 12-13, dessenne2024lipidomicanalysesreveal pages 4-8)

### 2023 synthesis of temperature responses

The 2023 review reports that, in mesophilic bacteria, a 10 °C decrease commonly reduces enzyme activity **two- to fourfold**, while cooling from 37 to 0 °C can reduce activity **20- to 250-fold**. It also notes that CspA may constitute approximately **15% of total protein synthesis** after cold shock and that trigger factor can be induced approximately **40-fold** at low temperature. These values establish the scale of translational and folding responses, but they derive from heterogeneous studies and should not be entered as universal parameters for `METPO:1000450`. (moon2023temperaturemattersbacterial pages 6-7, moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 7-9)

### New conceptual refinement

The direct TIR-FCS work published in 2026 challenges the traditional formulation that bacteria maintain one constant membrane fluidity across all temperatures. In the three Gram-positive species tested, homeostatic constancy applied below 26 °C, whereas fluidity rose above that threshold. Direct measurements also suggested that *B. subtilis* membranes at 20–23 °C were approximately **twofold less fluid than at 37 °C**. Thus, “homeoviscous adaptation” is better curated as **regulated maintenance within a low-temperature operating regime**, not absolute temperature-invariant fluidity. (barbotin2026twotemperaturedependentmembrane pages 1-2)

## 5. Applications and real-world relevance

- **Clinical persistence:** the 2024 *A. baumannii* work links temperature-dependent lipid remodeling with strain-dependent growth, motility, and biofilm behavior, relevant to persistence outside hosts and transmission through cooler healthcare environments. The lipid mechanism should not, however, be treated as a direct virulence mechanism without intervention data. (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 12-13)
- **Food and environmental microbiology:** predicting growth at room-like temperatures requires distinguishing active growth from survival and accounting for membrane adaptation, medium composition, and prior temperature history.
- **Bioprocessing:** lower-temperature cultivation can reduce protein aggregation but slows enzymatic and translational processes; membrane and RNA-chaperone modules identify possible engineering targets.
- **Antimicrobial susceptibility:** membrane fluidity influences permeability, respiration, and antibiotic uptake. This supports studying DesK/DesR or lipid synthesis as context-dependent intervention points, but no evidence reviewed here establishes them as validated antimicrobial targets for this trait. (barbotin2026twotemperaturedependentmembrane pages 1-2)
- **Trait prediction from genomes:** presence of `des`, `desK/desR`, `fabA/fabB`, or cold-shock genes may support a mechanistic hypothesis, but it cannot alone assign a 22–27 °C growth-range phenotype. Expression, lipid composition, and growth assays remain necessary.

## 6. Expert interpretation for TraitMech

The strongest expert model is that temperature is sensed indirectly through a **membrane physical state**. The isothermal isoleucine-depletion experiments are especially informative: reducing anteiso-BCFAs increased membrane order and activated `des` through DesK/DesR even without changing temperature. This separates the proximal signal—membrane order—from the distal environmental variable—temperature. (mendoza2014temperaturesensingby pages 5-6)

For the existing 13-node/8-edge graph, the best expansion is therefore not a broad collection of generic stress proteins. It is a compact feedback circuit:

1. 22–26 °C ambient temperature increases membrane order relative to warmer conditions.
2. Increased order biases DesK toward kinase output.
3. DesK phosphorylates DesR.
4. DesR-P activates `des` transcription.
5. Des introduces cis double bonds into membrane fatty-acid chains.
6. UFAs increase fluidity.
7. Restored fluidity suppresses DesK→DesR phosphate flux.
8. Appropriate membrane physical properties support respiration, membrane-protein function, transport, and ultimately growth.

BCFA synthesis can be included as a parallel membrane-fluidity input. CspA/CsdA, trigger factor, PPIases, and trehalose are better represented as optional auxiliary modules pending direct phenotype evidence in the target interval.

## 7. Claims not yet suitable for definitive curation

1. **Do not equate UFA abundance with the trait universally.** Archaea, Gram-positive bacteria, Gram-negative bacteria, fungi, and individual strains use different lipids and regulatory systems.
2. **Do not assert that 22–27 °C is an optimum.** The supplied definition concerns a growth-supporting range.
3. **Do not use a cold-shock expression response as proof of sustained growth.** Many cited experiments involve abrupt 37→20/22 °C shifts.
4. **Do not make FabA/FabB or candidate desaturases causally responsible in *A. baumannii*.** The 2024 evidence is genomic and correlational without knockout or complementation. (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12)
5. **Do not generalize the 26 °C transition to all microbes.** It was directly demonstrated in three Gram-positive species and may shift with species, medium, and membrane composition. (barbotin2026twotemperaturedependentmembrane pages 1-2)
6. **Do not curate heat-shock chaperones as core lower-mesophile determinants.** DnaK is reported as essential above 30 °C in *E. coli*, while trigger factor and DnaK are dispensable for survival at 20 °C in one cited context. These relationships do not directly establish growth-range causality at 22–27 °C. (moon2023temperaturemattersbacterial pages 6-7, moon2023temperaturemattersbacterial pages 5-6)
7. **Avoid invented ontology IDs.** Verify ChEBI entities for free fatty acids versus membrane acyl residues and use strain-specific UniProt identifiers only after the strain is fixed.
8. **The terminal phenotype edge remains uncertain.** A rigorous study should measure growth rates throughout 22–27 °C in wild type, pathway mutants, and complemented strains while simultaneously measuring lipid composition and membrane fluidity.

## DOI-first bibliography

1. Barbotin A, Juillot D, Wongdontree P, Carballido-López R. **Two temperature-dependent membrane fluidity regimes in gram-positive bacteria.** *mSphere*. Published **11 June 2026**. DOI: [10.1128/msphere.00095-26](https://doi.org/10.1128/msphere.00095-26). Direct TIR-FCS study across 20–37 °C; most range-specific evidence. (barbotin2026twotemperaturedependentmembrane pages 1-2)
2. Dessenne C, Ménart B, Acket S, et al. **Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of Acinetobacter baumannii.** *Microbiology Spectrum*. Published **October 2024**. DOI: [10.1128/spectrum.00757-24](https://doi.org/10.1128/spectrum.00757-24). Six-strain lipidomics, growth, motility, and biofilm comparison at 18 versus 37 °C. (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 4-8, dessenne2024lipidomicanalysesreveal pages 8-12)
3. Moon S, Ham S, Jeong J, et al. **Temperature Matters: Bacterial Response to Temperature Change.** *Journal of Microbiology*. Published **March 2023**; 61:343–357. DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x). Recent synthesis of membrane, nucleic-acid, translation, chaperone, and proteolysis responses. (moon2023temperaturemattersbacterial pages 6-7, moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 7-9)
4. de Mendoza D. **Temperature sensing by membranes.** *Annual Review of Microbiology*. Published **September 2014**; 68:101–116. DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). Foundational expert review of the DesK/DesR–Des feedback circuit and membrane-state sensing. (mendoza2014temperaturesensingby pages 5-6)

**Bottom line:** curate the *B. subtilis* membrane-order/DesK/DesR/Des/UFA feedback loop as the principal taxon-scoped mechanism, with membrane fluidity as the proximal physiological mediator. Represent the final link to `METPO:1000450` as supported but inferred, and retain RNA-chaperone, folding, trehalose, and *A. baumannii* lipid-species edges as provisional or taxon-specific until perturbation studies directly measure growth throughout 22–27 °C.

References

1. (barbotin2026twotemperaturedependentmembrane pages 1-2): Aurélien Barbotin, Dimitri Juillot, Paprapach Wongdontree, and Rut Carballido-López. Two temperature-dependent membrane fluidity regimes in gram-positive bacteria. mSphere, Jun 2026. URL: https://doi.org/10.1128/msphere.00095-26, doi:10.1128/msphere.00095-26. This article has 0 citations and is from a peer-reviewed journal.

2. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

3. (dessenne2024lipidomicanalysesreveal pages 1-2): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

4. (dessenne2024lipidomicanalysesreveal pages 4-8): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

5. (dessenne2024lipidomicanalysesreveal pages 8-12): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

6. (dessenne2024lipidomicanalysesreveal pages 2-4): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

8. (moon2023temperaturemattersbacterial pages 7-9): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

9. (moon2023temperaturemattersbacterial pages 5-6): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

10. (moon2023temperaturemattersbacterial pages 6-7): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

11. (dessenne2024lipidomicanalysesreveal pages 12-13): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.