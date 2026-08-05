---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:23:24.418802'
end_time: '2026-08-04T04:30:37.524619'
duration_seconds: 433.11
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range mid2
  trait_identifier: METPO:1000451
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range spans approximately 27\u201330 \xB0C, characteristic of mesophilic\
    \ physiology."
  parent_traits: METPO:1000306
  synonyms: Mesophilie, TR_27_to_30
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports the 27\u201330 \xB0C range as a typical\
    \ mesophile growth range.)"
  causal_graph_summary: 'temperature_range_mid2_baseline_mesophile: 13 nodes, 10 edges'
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
- **Trait label:** temperature range mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000451
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 27–30 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_27_to_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 27–30 °C range as a typical mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid2_baseline_mesophile: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **temperature range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid2.yaml`.

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
- **Trait label:** temperature range mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000451
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 27–30 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_27_to_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 27–30 °C range as a typical mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid2_baseline_mesophile: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **temperature range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid2.yaml`.

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


# Curation report: microbial **temperature range mid2**

## Executive assessment

**Target:** `METPO:1000451` (quoted verbatim)  
**Label:** temperature range mid2  
**Category:** ENVIRONMENT; **term kind:** CLASS; **status:** REVIEWED  
**Parent:** `METPO:1000306`  
**Synonyms:** *Mesophilie*; `TR_27_to_30`

This trait should be interpreted as an **assay-observed capacity for growth across an ambient-temperature interval whose width is approximately 27–30 °C**. It should **not** be interpreted as an optimum temperature of 27–30 °C, nor as growth exclusively between 27 and 30 °C. It is also distinct from survival after heat/cold shock, transient stress tolerance, growth rate at one temperature, or the broad informal category “mesophile.”

The strongest mechanistic graph supported by the literature is a **generic thermoadaptation module**—temperature changes membrane order, membrane sensing activates lipid remodeling, and remodeling restores physiologically useful membrane properties. However, the available evidence does **not** demonstrate that any one gene or module causes an organism’s growth-supporting interval specifically to span 27–30 °C. Consequently, mechanistic edges within the module can be curated, but the terminal edge to `METPO:1000451` should remain **uncertain/inferred** pending direct growth-range perturbation experiments.

## 1. Trait scope and boundary cases

### Positive scope

A defensible phenotype call requires growth measurements at multiple temperatures under otherwise controlled conditions. Ideally, growth-supporting lower and upper limits should be estimated using a standardized medium, atmosphere, pH, salinity, inoculum, incubation duration, and growth threshold. The approximately 27–30 °C quantity describes the **span**:

`upper growth-supporting temperature − lower growth-supporting temperature ≈ 27–30 °C`.

The exact endpoints may differ among taxa. Thus, an organism growing from 10 to 38 °C and another growing from 15 to 43 °C could both fall in this range-width class, although their optima and ecological niches differ.

### Exclusions and neighboring phenotypes

* **Temperature optimum:** a peak in growth rate or yield is not the same as the breadth of the supported interval.
* **Cardinal temperatures:** minimum, optimum, and maximum temperatures are related measurements but should be represented separately.
* **Cold/heat survival:** viability after acute exposure does not prove sustained growth.
* **Lag-phase acclimation:** recovery after a shift can reflect stress-response kinetics without changing cardinal growth limits.
* **Generic mesophily:** literature often uses “mesophilic” for optima around ordinary environmental or host temperatures; this does not establish a 27–30 °C range width.
* **Community/process temperature:** reactor performance at a “mesophilic” set point measures a community and operating regime, not necessarily a strain-level phenotype.

## 2. Current mechanistic understanding

Temperature affects membrane phase behavior, RNA structure, translation, protein folding, enzyme kinetics, and macromolecular damage. In bacteria lacking cholesterol-based thermal buffering, lower temperature promotes lipid ordering and can drive a liquid-crystalline-to-gel transition. Cis-unsaturated and anteiso-branched fatty acids disrupt tight acyl-chain packing, lower the phase-transition temperature, and support fluidity; saturated straight-chain fatty acids have the opposite tendency. This regulated remodeling is conventionally termed **homeoviscous adaptation**. (The source uses “homoviscous,” but “homeoviscous” is standard usage.) (mendoza2014temperaturesensingby pages 4-5, mendoza2014temperaturesensingby pages 2-4)

The best-resolved bacterial circuit is the *Bacillus subtilis* Des pathway. Increased membrane order changes DesK activity; DesK autophosphorylates at His-188 and transfers phosphate to DesR Asp-54; DesR-P activates `des`; and membrane-bound Δ5-desaturase introduces cis double bonds into membrane fatty acids. Importantly, membrane physical state—not temperature alone—is the proximal signal: isoleucine limitation can reduce anteiso-branched fatty acids and induce `des` at 37 °C. (mendoza2014temperaturesensingby pages 5-6)

Cold also stabilizes inhibitory RNA secondary structures and impairs ribosome biogenesis and translation. CspA acts as an RNA chaperone, while the ATP-dependent helicase CsdA supports ribosomal function. Heat causes protein unfolding and aggregation, inducing DnaK/DnaJ/GrpE, ClpB, and proteases such as Lon and FtsH. These systems plausibly help maintain growth near temperature limits, but current sources primarily establish **stress acclimation**, not causation of an exact growth-range width. (moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 10-11, moon2023temperaturemattersbacterial pages 11-12, moon2023temperaturemattersbacterial pages 13-14)

## 3. Candidate nodes

Identifiers below are included only where confidence is high. Taxon-specific genes/proteins should ultimately be grounded to the exact strain’s UniProt or locus identifier rather than assigned a generic protein CURIE.

### Trait and environmental nodes

| Node | Suggested grounding | Role |
|---|---|---|
| temperature range mid2 | `METPO:1000451` | Target phenotype |
| parent temperature-range phenotype | `METPO:1000306` | Parent class |
| ambient temperature | label-only pending project ontology convention | Experimental/environmental variable |
| low-temperature shift | label-only | Perturbation that increases membrane order and cold responses |
| high-temperature/heat shift | label-only | Perturbation causing excess fluidity and proteotoxic stress |
| growth-supporting temperature interval | label-only | Assay-derived interval; terminal graph measurement |
| growth rate, yield, lag, viability | label-only assay nodes | Measurements needed to distinguish growth from survival |

### Cellular structures and physical states

| Node | Suggested grounding | Role |
|---|---|---|
| plasma membrane | `GO:0005886` | Site of temperature-dependent lipid-state changes and DesK/Des activity |
| membrane fluidity | label-only | Physical property; avoid equating it with growth |
| membrane lipid ordering | label-only | Proximal DesK stimulus |
| membrane phase-transition temperature | label-only | Emergent lipid-composition property |
| protein aggregate | label-only | Heat-damage substrate for chaperone/protease systems |
| RNA secondary structure | label-only | Cold-stabilized barrier to translation |
| ribosome/ribosomal subunit biogenesis | GO-grounding should be selected during implementation | Cold-sensitive translation module |

### Genes, proteins, and complexes

| Node | Grounding recommendation | Function/evidence scope |
|---|---|---|
| DesK | taxon-specific UniProt/locus | Membrane histidine kinase/phosphatase thermosensor in *B. subtilis* |
| DesR | taxon-specific UniProt/locus | Response regulator; DesR-P activates `des` |
| `des` / Des | taxon-specific gene/protein | Membrane Δ5 fatty-acid desaturase |
| DesA, DesB, DesT | taxon-specific identifiers | Desaturation enzymes/regulator discussed in *A. baumannii* |
| FabA, FabB | taxon-specific identifiers | FASII enzymes associated with unsaturated-fatty-acid synthesis in selected *A. baumannii* strains |
| branched-chain α-keto acid dehydrogenase | taxon-specific complex; EC grounding after subunit resolution | Supplies precursors for branched fatty acids |
| CspA | taxon-specific identifier | RNA chaperone |
| CsdA | taxon-specific identifier | ATP-dependent RNA helicase/ribosome-biogenesis factor |
| trigger factor | taxon-specific identifier | Cotranslational chaperone; strongly cold induced in some bacteria |
| DnaK–DnaJ–GrpE | taxon-specific complex members | Heat-stress protein folding/refolding |
| ClpB | taxon-specific identifier | Protein disaggregation |
| Lon, FtsH and other heat-shock proteases | taxon-specific identifiers | Removal of damaged proteins |
| σ32 and σE | taxon-specific identifiers | Heat-shock transcriptional regulation |

### Chemicals and lipid classes

| Node | Grounding recommendation | Role |
|---|---|---|
| unsaturated fatty acids | ChEBI class after identifier verification | Increase acyl-chain disorder and generally support low-temperature fluidity |
| saturated straight-chain fatty acids | ChEBI class after verification | Promote tighter packing and higher phase-transition temperature |
| anteiso-branched-chain fatty acids | label-only unless exact molecular species is specified | Lower transition temperature and support cold growth |
| palmitoleic acid (C16:1) | ChEBI identifier after verification | Increased at 18 °C in five *A. baumannii* strains |
| oleic acid (C18:1) | ChEBI identifier after verification | Preferentially increased in strain ABVal2 at 18 °C |
| phosphatidylethanolamine | ChEBI class after verification | Temperature-remodeled glycerophospholipid class |
| phosphatidylglycerol | ChEBI class after verification | Temperature-remodeled glycerophospholipid class |
| phosphatidylcholine | ChEBI class after verification | Increased relative to PE in some cold-adaptation systems |
| isoleucine | ChEBI identifier after verification | Precursor-related experimental control of anteiso-fatty-acid abundance |

### Processes and modules

* Homeoviscous adaptation / membrane-lipid remodeling.
* Fatty-acid desaturation and FASII unsaturated-fatty-acid synthesis.
* Branched-chain fatty-acid biosynthesis.
* Two-component phosphorelay signaling.
* Cold-shock RNA remodeling and ribosome biogenesis.
* Heat-shock protein folding, disaggregation, and proteolysis.
* Temperature-dependent growth assay and cardinal-temperature estimation.

## 4. Evidence-backed candidate edges

“Snippet” is a short quotation or tightly bounded extracted statement from the retrieved source. **Core** means the edge itself is suitable for a mechanistic subgraph; it does not mean the edge is proven to determine `METPO:1000451`.

| # | Subject–predicate–object | Evidence and snippet | Curation note |
|---:|---|---|---|
| 1 | low ambient temperature → **increases** membrane lipid order | de Mendoza 2014: low temperature drives bilayers from fluid toward nonfluid/gel states. (mendoza2014temperaturesensingby pages 2-4) | **Core, review-supported.** Generic bacterial membrane physics; magnitude depends on lipid composition. |
| 2 | unsaturated fatty acids → **decrease** lipid packing/order | “incorporation of proportionally more unsaturated fatty acids…as growth temperature decreases” disrupts bilayer order and optimizes physiological processes. (mendoza2014temperaturesensingby pages 4-5) | **Core.** Do not infer an exact growth range from lipid composition alone. |
| 3 | anteiso-branched fatty acids → **decrease** membrane transition temperature | UFAs and anteiso-BCFAs decrease transition temperature by disrupting ordered packing. (mendoza2014temperaturesensingby pages 2-4) | **Core, review-supported**; lipid-species and taxon dependent. |
| 4 | increased membrane order → **activates kinase mode of** DesK | Membrane fluidity/order rather than temperature per se is described as the signal governing the Des pathway. (mendoza2014temperaturesensingby pages 5-6) | **Core for *B. subtilis***; not universal across bacteria. |
| 5 | DesK-His188 phosphorylation → **phosphorylates** DesR-Asp54 | DesK autophosphorylates at His-188 and transfers phosphate to DesR at Asp-54. (mendoza2014temperaturesensingby pages 5-6) | **Core, taxon-specific.** Preserve residue detail only for the referenced protein. |
| 6 | DesR-P → **activates transcription of** `des` | “Phosphorylated DesR-P binds DNA to activate des expression.” (mendoza2014temperaturesensingby pages 5-6) | **Core for the *B. subtilis* circuit.** |
| 7 | Des Δ5-desaturase → **introduces cis double bonds into** membrane fatty acids | Des is described as a membrane-bound enzyme introducing cis double bonds into saturated fatty acids. (mendoza2014temperaturesensingby pages 5-6) | **Core.** Substrate/product species should be refined if the YAML requires chemical specificity. |
| 8 | shift 37→20 °C → **induces** UFA synthesis | *B. subtilis* makes primarily saturated fatty acids at 37 °C and induces UFA synthesis after transfer to 20 °C. (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 4-5) | **Strong observational/shift evidence**, but far outside the exact target-range definition. |
| 9 | growth at 23 °C → **increases** Δ5 desaturation relative to 30 °C | In *B. megaterium*, palmitate was “almost completely desaturated” at 23 °C, whereas desaturation at 30 °C was negligible. (mendoza2014temperaturesensingby pages 4-5) | **Quantitative, taxon-specific.** Useful evidence that the response is sharply temperature dependent. |
| 10 | isoleucine limitation → **reduces** anteiso-BCFAs → **increases** membrane order → **induces** `des` | Isoleucine limitation triggered `des` at constant 37 °C by reducing a-BCFAs and increasing order. (mendoza2014temperaturesensingby pages 5-6) | **Especially valuable mechanistic evidence:** separates membrane state from temperature as causal signal. |
| 11 | 18 °C growth → **increases** C16:1/C18:1-containing PE and PG | Six *A. baumannii* strains were compared at 18 versus 37 °C; five increased C16:1, ABVal2 preferentially increased C18:1, and total unsaturated content reached approximately 60–80%. (dessenne2024lipidomicanalysesreveal pages 8-12) | **Strong quantitative lipidomics**, corroborated by Laurdan/permeation assays; no gene deletion was performed. |
| 12 | `fabA`/`fabB` genomic insertion → **is associated with** UFA-synthesis capacity | ABVal2 and ABVal3 contained an approximately 20-gene insertion including `fabA` and `fabB`, absent from the reference strain. (dessenne2024lipidomicanalysesreveal pages 8-12) | **Uncertain causal edge.** Genomic association without perturbation; do not encode as sufficient for the trait. |
| 13 | cold shift → **induces** CspA → **reduces inhibitory** RNA secondary structure | CspA is summarized as an “RNA chaperone preventing secondary structure formation.” (moon2023temperaturemattersbacterial pages 7-9) | **Contextual cold-acclimation edge.** No direct evidence for the 27–30 °C range span. |
| 14 | cold shift → **induces** CsdA → **supports** ribosome function/biogenesis | CsdA is an ATP-dependent RNA helicase enabling ribosome function under cold shock. (moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 11-12) | **Contextual.** Taxon and assay should accompany curation. |
| 15 | low temperature → **strongly induces** trigger factor → **supports** protein folding | Trigger factor was reported at approximately 40-fold overexpression under low-temperature conditions. (moon2023temperaturemattersbacterial pages 7-9) | **Contextual/statistical observation.** Overexpression can be harmful at approximately 4 °C, so avoid a monotonic “more is better” edge. |
| 16 | heat stress → **induces** DnaK/DnaJ/GrpE and ClpB → **promotes** refolding/disaggregation | The 2023 review identifies DnaK as a network hub and describes DnaK/ClpB-mediated protein quality control. (moon2023temperaturemattersbacterial pages 10-11, moon2023temperaturemattersbacterial pages 13-14) | **Contextual heat-acclimation module**, not an exact range determinant. |
| 17 | heat stress → **induces** Lon/FtsH/Clp-family proteolysis → **removes** damaged proteins | Heat-shock proteases are summarized as degrading damaged or aggregated proteins. (moon2023temperaturemattersbacterial pages 13-14, moon2023temperaturemattersbacterial pages 12-13) | **Contextual.** Gene-specific perturbation evidence is needed before connecting to the trait. |
| 18 | Des activity → **maintains** low-temperature membrane-fluidity regime | A 2026 TIR-FCS study across 20–37 °C found constant fluidity below approximately 26 °C, linear increase above it, and loss of low-temperature constancy in a `Δdes` mutant. (barbotin2026twotemperaturedependentmembrane pages 1-2) | **Direct perturbation but post-priority window.** Valuable update that challenges the simplistic constant-fluidity model. |
| 19 | membrane homeostasis → **supports** growth across temperature variation | Reviews state that membrane remodeling optimizes many physiological processes at the new temperature. (mendoza2014temperaturesensingby pages 4-5, wu2023molecularmechanismsof pages 3-5) | **Plausible but nonspecific.** Curate as “contributes to,” not “determines.” |
| 20 | membrane homeostasis → **causes** `METPO:1000451` | No retrieved study directly measured how disrupting this module changes the width of a strain’s growth-supporting interval to or from 27–30 °C. | **Do not curate as established. Mark inferred/uncertain.** |

The following decision matrix condenses those recommendations:

| Candidate edge (subject–predicate–object) | Evidence class | Taxon/assay | Curation recommendation | Key DOI |
|---|---|---|---|---|
| low environmental temperature → increases membrane lipid ordering / decreases membrane fluidity | review synthesis | Bacteria broadly; membrane adaptation review | contextual only | 10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 2-4) |
| increased membrane lipid ordering → activates DesK histidine kinase activity | review synthesis | *Bacillus subtilis* DesK/DesR membrane-sensing model | contextual only | 10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 5-6) |
| DesK kinase activity → phosphorylates DesR (DesR-P) | review synthesis | *Bacillus subtilis* two-component signaling model | contextual only | 10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 5-6) |
| DesR-P → activates des expression | review synthesis | *Bacillus subtilis* promoter regulation model | contextual only | 10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 5-6) |
| des expression / Des Δ5-desaturase activity → increases unsaturated fatty acids | review synthesis | *Bacillus subtilis* and *Bacillus megaterium*; temperature-shift studies summarized in review | contextual only | 10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 4-5) |
| increased unsaturated fatty acids → increases membrane fluidity | quantitative observation | *Acinetobacter baumannii* lipidomics at 18°C vs 37°C; Laurdan/permeation support | curate core | 10.1128/spectrum.00757-24 (dessenne2024lipidomicanalysesreveal pages 8-12) |
| des deletion / loss of Des function → loss of low-temperature membrane-fluidity homeostasis | direct perturbation | Gram-positive bacteria, especially *Bacillus subtilis*; direct fluidity quantification across 20–37°C | contextual only | 10.1128/msphere.00095-26 (barbotin2026twotemperaturedependentmembrane pages 1-2) |
| anteiso-branched-chain fatty acids → lower membrane phase transition temperature / promote fluidity | review synthesis | Bacteria broadly; membrane biophysics review | curate core | 10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 2-4) |
| low temperature → increases anteiso-/branched-chain fatty acid usage during adaptation | review synthesis | Gram-positive bacteria broadly; cold lipid adaptation review | contextual only | 10.3390/cells12101353 (wu2023molecularmechanismsof pages 3-5, wu2023molecularmechanismsof pages 16-17) |
| cold temperature shift → induces CspA RNA chaperone functions that limit inhibitory RNA secondary structures | review synthesis | Bacteria broadly, with strong *E. coli* representation | contextual only | 10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 11-12) |
| cold temperature shift → induces CsdA RNA helicase functions supporting ribosome/translation at low temperature | review synthesis | Bacteria broadly, with strong *E. coli* representation | contextual only | 10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 11-12) |
| heat stress → induces DnaK/ClpB/proteases for protein quality control | review synthesis | Bacteria broadly, with strong *E. coli* representation | contextual only | 10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 10-11, moon2023temperaturemattersbacterial pages 13-14, moon2023temperaturemattersbacterial pages 12-13) |
| membrane fluidity homeostasis → supports growth across a mesophilic temperature interval | review synthesis | Bacteria broadly | uncertain/do not connect to trait | 10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 4-5) |
| membrane fluidity / homeoviscous adaptation → METPO:1000451 | review synthesis | Trait-level inference only; no direct exact 27–30°C range experiment | uncertain/do not connect to trait | 10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 4-5), 10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 7-9), 10.1128/spectrum.00757-24 (dessenne2024lipidomicanalysesreveal pages 8-12) |


*Table: This table summarizes candidate mechanistic edges for the temperature range mid2 trait and classifies each by evidence strength, assay/taxon scope, and whether it is ready for TraitMech curation. It is useful for separating well-supported membrane adaptation mechanisms from broader stress-response processes that should remain contextual or uncertain for this exact temperature-range phenotype.*

## 5. Recent developments, 2023–2024

### Integrated temperature-response model (2023)

Moon and colleagues synthesized bacterial responses spanning membrane remodeling, RNA chaperones/helicases, ribosome function, chaperone networks, protein disaggregation, proteolysis, and regulatory sigma factors. The review reinforces that temperature adaptation is distributed across cellular systems rather than controlled by one “mesophile gene.” It also notes non-monotonic effects: excessive chaperone expression at about 4 °C can be harmful, cautioning against graph edges that imply every stress-response increase necessarily improves growth. Published March 2023. (moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 10-11, moon2023temperaturemattersbacterial pages 12-13)

### Lipid-metabolic adaptation review (2023)

Wu et al. highlighted UFA, short-chain-fatty-acid and branched-chain-fatty-acid enrichment; DesK and cyanobacterial Hik33 sensing; and taxon-specific phospholipid remodeling. The authors emphasize that membrane-fluidity maintenance is central to cold survival but that sensor mechanisms and the functions of some remodeled lipids remain incompletely resolved. Published May 2023. (wu2023molecularmechanismsof pages 3-5, wu2023molecularmechanismsof pages 16-17)

### Strain-resolved lipidomics (2024)

Dessenne et al. showed substantial heterogeneity among six clinical *A. baumannii* strains. At 18 °C, five strains preferentially accumulated C16:1 while ABVal2 accumulated C18:1; unsaturated lipid content reached approximately 60–80%. Identical DesA sequences did not predict identical phenotypes, implicating post-transcriptional regulation, electron-transfer capacity, or additional desaturases. This is a strong warning against inferring thermal phenotype from one annotated desaturase. Published October 2024. (dessenne2024lipidomicanalysesreveal pages 8-12)

### Updated membrane-adaptation perspective (2024)

Maiti et al. reviewed homeoviscous and osmolyte-mediated membrane adaptation. One summarized cold experiment reported saturated fatty acids falling from about 70% under the standard 15 °C condition to below 15% at 4 °C, while UFAs rose above 85%; these are striking but system-specific values, not universal thresholds. Published August 2024. (maiti2024extrememakeoverthe pages 4-5)

### Important later conceptual revision

Although outside the requested 2023–2024 priority, direct TIR-FCS measurements published in 2026 found two regimes in three Gram-positive species: fluidity was controlled below approximately 26 °C but increased linearly from that threshold through 37 °C. A `Δdes` mutant lost the low-temperature plateau. This argues against encoding “constant membrane fluidity across the full growth range” as a universal bacterial rule. (barbotin2026twotemperaturedependentmembrane pages 1-2)

## 6. Applications and real-world relevance

1. **Phenotype prediction and strain selection.** Lipidomics, membrane-fluidity measurements, and temperature-resolved growth curves can jointly distinguish strains that acclimate to temperature shifts from strains with genuinely broad growth ranges. The strain heterogeneity observed in *A. baumannii* demonstrates why gene presence alone is insufficient. (dessenne2024lipidomicanalysesreveal pages 8-12)
2. **Bioprocess control.** Anaerobic digestion, fermentation, food production, and wastewater treatment routinely use mesophilic operating regimes. For TraitMech, reactor temperature should remain an environmental/process node rather than being mistaken for an intrinsic strain trait.
3. **Food safety and pathogen persistence.** Cold-induced UFA remodeling, RNA chaperones, and biofilm-associated temperature responses can support persistence during refrigeration or environmental transmission. These applications concern survival and acclimation and therefore require careful separation from sustained-growth limits. (dessenne2024lipidomicanalysesreveal pages 8-12, moon2023temperaturemattersbacterial pages 7-9)
4. **Synthetic biology.** DesK/DesR-like membrane-state sensors and lipid-remodeling enzymes are candidate modules for engineering temperature-responsive expression or membrane robustness. The new two-regime fluidity measurements suggest that engineering objectives should target a desired membrane-state window rather than assume perfect homeoviscous constancy. (barbotin2026twotemperaturedependentmembrane pages 1-2, mendoza2014temperaturesensingby pages 5-6)
5. **Antimicrobial susceptibility and membrane permeability.** Temperature-dependent lipid composition can alter permeability and membrane-protein performance. Such consequences are downstream phenotypes and should not be represented as defining `METPO:1000451`. (barbotin2026twotemperaturedependentmembrane pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12)

## 7. Recommended TraitMech graph architecture

A conservative YAML graph should have three layers:

**Layer A—assay definition**

`temperature series` → `growth measured at each temperature` → `lower and upper growth-supporting limits estimated` → `range width approximately 27–30 °C` → `METPO:1000451`.

This is the only defensible direct route to the target trait.

**Layer B—curatable mechanistic subgraph**

`decreased ambient temperature` → `increased membrane order` → `DesK kinase state` → `DesR-P` → `des transcription` → `Des activity` → `increased UFA abundance` → `reduced membrane order / altered fluidity` → `membrane physiological function`.

Add a parallel branch:

`isoleucine availability` → `anteiso-BCFA abundance` → `membrane transition temperature/order`.

**Layer C—contextual boundary-support modules**

* Cold: `CspA/CsdA/trigger factor` → `RNA remodeling/ribosome biogenesis/protein folding` → `cold acclimation`.
* Heat: `σ32/σE` → `DnaK–DnaJ–GrpE/ClpB/proteases` → `protein quality control` → `heat acclimation`.

Edges from Layers B or C to `METPO:1000451` should use a predicate such as **contributes_to** and carry an uncertainty qualifier until a perturbation study measures changes in the complete temperature-growth curve.

## 8. Claims that should not yet be curated

* **Do not assert** that “more unsaturated fatty acids causes a 27–30 °C growth range.” Available data establish membrane remodeling, not the exact interval width.
* **Do not treat 27–30 °C as the organism’s optimum.** In this term definition it is the approximate range span.
* **Do not make DesK/DesR universal.** It is a well-resolved *Bacillus* mechanism; other taxa use different sensors or lipid pathways.
* **Do not infer phenotype from `des`, `fabA`, or `fabB` presence alone.** The 2024 *A. baumannii* study found marked strain-level differences not explained by identical DesA sequences. (dessenne2024lipidomicanalysesreveal pages 8-12)
* **Do not encode perfect fluidity constancy across all temperatures.** Direct measurements indicate a low-temperature homeostatic regime and a higher-temperature nonconstant regime in the tested Gram-positive species. (barbotin2026twotemperaturedependentmembrane pages 1-2)
* **Do not conflate cold/heat-shock expression with sustained growth.** Expression, survival, lag recovery, and range boundaries are separate phenotypes.
* **Do not generalize quantitative lipid percentages** across taxa, media, or analytical methods.
* **Do not assign unverified CURIEs.** Use label-only nodes until exact chemical species, strain proteins, reactions, and ontology releases are checked.
* **Do not use the existing review as evidence that 27–30 °C is a universal mesophile growth interval.** It supports a membrane-adaptation mechanism, not that exact trait boundary.

## DOI-first bibliography

1. **Moon S, et al.** “Temperature Matters: Bacterial Response to Temperature Change.” *Journal of Microbiology* 61, 343–357. **Published March 2023.** DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x). (moon2023temperaturemattersbacterial pages 7-9)
2. **Wu G, Baumeister R, Heimbucher T.** “Molecular Mechanisms of Lipid-Based Metabolic Adaptation Strategies in Response to Cold.” *Cells* 12, 1353. **Published May 2023.** DOI: [10.3390/cells12101353](https://doi.org/10.3390/cells12101353). (wu2023molecularmechanismsof pages 3-5)
3. **Dessenne C, et al.** “Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of *Acinetobacter baumannii*.” *Microbiology Spectrum* 12. **Published October 2024.** DOI: [10.1128/spectrum.00757-24](https://doi.org/10.1128/spectrum.00757-24). (dessenne2024lipidomicanalysesreveal pages 8-12)
4. **Maiti A, Erimban S, Daschakraborty S.** “Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.” *Chemical Communications* 60, 10280–10294. **Published August 2024.** DOI: [10.1039/D4CC03114H](https://doi.org/10.1039/D4CC03114H). (maiti2024extrememakeoverthe pages 4-5)
5. **de Mendoza D.** “Temperature sensing by membranes.” *Annual Review of Microbiology* 68, 101–116. **Published September 2014.** DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). (mendoza2014temperaturesensingby pages 4-5, mendoza2014temperaturesensingby pages 5-6)
6. **Barbotin A, Juillot D, Wongdontree P, Carballido-López R.** “Two temperature-dependent membrane fluidity regimes in gram-positive bacteria.” *mSphere* 11. **Published June 2026; included as a post-2024 conceptual update.** DOI: [10.1128/msphere.00095-26](https://doi.org/10.1128/msphere.00095-26). (barbotin2026twotemperaturedependentmembrane pages 1-2)

## Bottom-line curation recommendation

Retain the existing baseline membrane-adaptation graph, but revise its interpretation: **UFA/branched-fatty-acid remodeling is a mechanism supporting membrane function under temperature change, not direct evidence for an exact 27–30 °C growth-range span.** Curate the well-supported DesK→DesR→`des`→UFA and lipid-physics edges with *Bacillus*-specific qualifiers; add RNA and protein-quality-control branches only as contextual acclimation modules; and connect all mechanistic branches to `METPO:1000451` only with an explicit **uncertain/contributes_to** relation until complete temperature-growth curves are measured in perturbation strains.

References

1. (mendoza2014temperaturesensingby pages 4-5): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

2. (mendoza2014temperaturesensingby pages 2-4): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

3. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

4. (moon2023temperaturemattersbacterial pages 7-9): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

5. (moon2023temperaturemattersbacterial pages 10-11): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

6. (moon2023temperaturemattersbacterial pages 11-12): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

7. (moon2023temperaturemattersbacterial pages 13-14): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

8. (dessenne2024lipidomicanalysesreveal pages 8-12): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

9. (moon2023temperaturemattersbacterial pages 12-13): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

10. (barbotin2026twotemperaturedependentmembrane pages 1-2): Aurélien Barbotin, Dimitri Juillot, Paprapach Wongdontree, and Rut Carballido-López. Two temperature-dependent membrane fluidity regimes in gram-positive bacteria. mSphere, Jun 2026. URL: https://doi.org/10.1128/msphere.00095-26, doi:10.1128/msphere.00095-26. This article has 0 citations and is from a peer-reviewed journal.

11. (wu2023molecularmechanismsof pages 3-5): Gang Wu, Ralf Baumeister, and Thomas Heimbucher. Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold. Cells, 12:1353, May 2023. URL: https://doi.org/10.3390/cells12101353, doi:10.3390/cells12101353. This article has 102 citations.

12. (wu2023molecularmechanismsof pages 16-17): Gang Wu, Ralf Baumeister, and Thomas Heimbucher. Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold. Cells, 12:1353, May 2023. URL: https://doi.org/10.3390/cells12101353, doi:10.3390/cells12101353. This article has 102 citations.

13. (maiti2024extrememakeoverthe pages 4-5): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 17 citations and is from a domain leading peer-reviewed journal.