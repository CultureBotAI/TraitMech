---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:29:54.455096'
end_time: '2026-08-04T03:38:30.558953'
duration_seconds: 516.1
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature delta
  trait_identifier: METPO:1000303
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_delta
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature phenotype with numerical limits expressing the breadth\
    \ (maximum minus minimum, in \xB0C) of ambient temperatures supporting growth\
    \ of an organism."
  parent_traits: METPO:1000533, METPO:1000534
  synonyms: ''
  evidence_summary: 'DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of
    high temperature (Thermophile-adaptation review supports the breadth of the temperature-tolerance
    span as a derived descriptor reflecting overall thermal-adaptation flexibility.)
    | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation
    review supports homoviscous remodeling capacity as the basis of broad versus narrow
    temperature tolerance.)'
  causal_graph_summary: 'temperature_delta_thermal_flexibility: 7 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000303
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits expressing the breadth (maximum minus minimum, in °C) of ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the breadth of the temperature-tolerance span as a derived descriptor reflecting overall thermal-adaptation flexibility.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous remodeling capacity as the basis of broad versus narrow temperature tolerance.)
- **Existing causal graph summary:** temperature_delta_thermal_flexibility: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **temperature delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta.yaml`.

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
- **Trait label:** temperature delta
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000303
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits expressing the breadth (maximum minus minimum, in °C) of ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the breadth of the temperature-tolerance span as a derived descriptor reflecting overall thermal-adaptation flexibility.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous remodeling capacity as the basis of broad versus narrow temperature tolerance.)
- **Existing causal graph summary:** temperature_delta_thermal_flexibility: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **temperature delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta.yaml`.

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


# Curation report: microbial temperature delta

## Executive summary

**Target:** `METPO:1000303` (“temperature delta”), an environmental class representing the numerical breadth of ambient temperatures that support microbial growth:

\[
\Delta T_{growth}=T_{max,growth}-T_{min,growth}
\]

The most defensible interpretation is an **assay-derived growth-niche breadth**, not a stress-survival phenotype. Both endpoints must be measured under specified medium, pH, atmosphere, pressure, salinity, inoculum, incubation time, and growth-detection threshold. Cardinal-temperature models treat minimum, optimum, and maximum growth temperatures as distinct parameters; the optimum is not part of the subtraction. Microbial temperature-response curves are usually asymmetric, with performance declining particularly sharply above the optimum. (noll2020modelingandexploiting pages 6-8)

Mechanistically, temperature delta is an emergent phenotype. Its lower boundary is strongly influenced by maintenance of membrane fluidity, transcription/translation at low temperature, and cold-active protein-folding systems. Its upper boundary is influenced by membrane stability, proteostasis, osmotic/ionic homeostasis, oxidative-damage control, and preservation of translation and envelope functions. The strongest direct evidence presently supports membrane-fluidity regulation and high-temperature proteostasis; many general claims about compatible solutes or cold-shock proteins concern stress survival rather than a measured change in full growth-range breadth.

## 1. Trait scope and boundary cases

### Recommended operational definition

Curate `METPO:1000303` when a study reports—or permits calculation of—the difference between the highest and lowest temperatures supporting **reproducible net growth** under the same operational criterion. Ideally, growth should be demonstrated by increasing viable counts, biomass, optical density, or another validated replication measure, rather than metabolic activity alone.

The value is conditional on the assay. A suitable evidence record should retain:

- organism and strain;
- Tmin and Tmax values and inclusivity;
- medium and nutrient composition;
- pH, salinity/water activity, oxygen or electron-acceptor conditions, and pressure;
- incubation duration and temperature resolution;
- growth threshold and replicate information;
- acclimation or evolutionary history.

The broad literature spans approximately −2 to 122°C in one cross-microbial modeling compilation, while an extremophile review describes an approximately 120°C global domain-level span. These are **across-organism envelopes**, not temperature deltas of an individual strain. (siliakus2017adaptationsofarchaeal pages 14-15, noll2020modelingandexploiting pages 6-8)

### Distinctions from nearby traits

1. **Minimum growth temperature:** one endpoint contributing to delta; it is not itself temperature delta.
2. **Maximum growth temperature:** the other endpoint; likewise not the breadth.
3. **Optimum growth temperature:** temperature yielding maximal performance. An organism can shift Topt without broadening its niche; E. coli evolution experiments have shifted optimum performance while preserving thermal breadth. (noll2020modelingandexploiting pages 6-8)
4. **Thermal performance-curve shape:** includes growth rate, skew, peak height, and activation/deactivation slopes; delta retains only the support interval.
5. **Heat-shock or cold-shock survival:** persistence after acute exposure does not establish sustained growth at that temperature. This distinction is biologically important: 2024 work in Salmonella found that greatly increased heat-shock resistance through loss of DnaJ carried poorer growth at 37°C and above, illustrating that shock resistance can move opposite to growth performance.
6. **Thermophile/psychrophile class:** an ecological preference or cardinal-temperature classification, not necessarily a broad range. Extremophiles may be specialists with narrow deltas.
7. **Acclimation/plasticity versus evolved breadth:** short-term expression or lipid remodeling may restore growth within an existing range; a heritable endpoint shift is evidence of evolved range expansion.
8. **Dormancy, spore survival, or metabolic activity without division:** exclude unless the ontology explicitly allows non-growing persistence.

A useful concrete boundary example is *Psychromonas ingrahamii*, reported with Tmin −12°C and Topt 5°C. The difference between these two values is **not** temperature delta because Tmax is absent. (siliakus2017adaptationsofarchaeal pages 8-10)

## 2. Candidate nodes grouped by type

### Trait and assay nodes

- temperature delta — `METPO:1000303`
- minimum growth temperature — retain the supplied parent `METPO:1000533` if confirmed locally
- maximum growth temperature — retain the supplied parent `METPO:1000534` if confirmed locally
- optimum growth temperature — label-only unless an existing verified METPO identifier is available
- sustained microbial growth — candidate `GO:0040007` (growth), with organismal context
- ambient temperature — candidate `ENVO:01000207` only after confirming that its intended scope fits the project
- temperature-shock survival — label-only and explicitly separate from the target

### Cellular structures and physical states

- cytoplasmic membrane
- membrane fluidity / membrane physical state
- membrane permeability
- lipid phase separation
- protein aggregation / unfolded-protein burden
- cytoplasm
- cell envelope
- ribosome and translation machinery

The membrane is a plausible central mediator because low fluidity disrupts essential processes, whereas excessive fluidity/permeability compromises high-temperature function. Archaeal tetraether/pentacyclic lipids and bacterial changes in unsaturation, branching, and chain composition represent lineage-specific solutions. A review identifies an approximate 80°C boundary above which ester-lipid-only bacterial membranes are uncommon and ether-linked architectures become especially important; this is comparative evidence, not a universal causal threshold. (siliakus2017adaptationsofarchaeal pages 14-15, siliakus2017adaptationsofarchaeal pages 8-10)

### Genes, proteins, and complexes

**Cold/membrane module**

- DesK membrane thermosensor histidine kinase — label-only, taxon-specific
- DesR response regulator — label-only
- `des`, Δ5 acyl-lipid desaturase — label-only; an EC identifier should be added only after enzyme-specific verification
- fatty-acid biosynthesis genes such as `fabA`/`fabB` — label-only, species-specific
- cold-shock proteins CspA/CspB/CspD — label-only family nodes unless a strain-specific UniProt accession is curated
- trigger factor and PPiB peptidyl-prolyl isomerase — label-only or strain-specific UniProt

**Heat/proteostasis module**

- GroEL–GroES chaperonin complex
- DnaK–DnaJ–GrpE chaperone system
- DegP protease/chaperone
- LysU lysyl-tRNA synthetase
- protein quality-control system — candidate `GO:0006457` (protein folding) and `GO:0030163` (protein catabolic process), depending on the edge
- heat-shock response — `GO:0009408`
- response to temperature stimulus — `GO:0009266`
- response to cold — `GO:0009409`

**Ionic and signaling module**

- cyclic di-AMP signaling system
- c-di-AMP cyclase/regulatory genes — keep label-only until the causal Bacillus alleles are identified
- potassium transport/homeostasis system
- osmotic homeostasis

**Damage-control module**

- oxidative-stress response — `GO:0006979`
- DNA double-strand-break repair — `GO:0006302`
- outer-membrane organization
- tRNA modification pathways
- cell-division machinery

### Chemicals and lipid classes

- unsaturated fatty acids — `CHEBI:27283`
- saturated fatty acids — `CHEBI:26607`
- potassium ion — `CHEBI:29103`
- trehalose — `CHEBI:27082`
- glycine betaine — `CHEBI:17750`
- L-proline — `CHEBI:17203`
- ectoine and hydroxyectoine — add CHEBI identifiers only after direct registry verification
- cyclic di-AMP — add a CHEBI identifier only after direct registry verification
- branched-chain fatty acids, archaeal diether lipids, glycerol-dialkyl-nonitol tetraethers, and pentacyclic tetraethers — label-only class nodes unless the precise chemical species is known
- reactive oxygen species — `CHEBI:26523`

## 3. Candidate causal edges

The following matrix identifies the highest-priority edges. “Direct” means a perturbation, knockout, complementation, or experimental-evolution result; it does not imply universal validity across taxa.

| Candidate causal edge (subject → predicate → object) | Evidence organism/assay | Quantitative result | Evidence strength | DOI |
|---|---|---|---|---|
| minimum growth temperature + maximum growth temperature → determine → temperature delta (METPO:1000303) | Cardinal-temperature framework and compiled microbial growth-range literature; sustained growth boundaries, not shock survival | Reported microbial span across characterized taxa is ~124°C from about −2 to 122°C; temperature delta is operationally Tmax−Tmin (noll2020modelingandexploiting pages 6-8, siliakus2017adaptationsofarchaeal pages 8-10) | **Strong, trait-definitional**; cross-taxon but framework-level rather than single perturbation | 10.3390/pr8010121; 10.1007/s00792-017-0939-x |
| low membrane fluidity → activates → DesK/DesR two-component system | *Bacillus subtilis* membrane-fluidity perturbation and transcriptional assays at constant temperature and after cooling (mendoza2014temperaturesensingby pages 5-6) | Shift from 37°C to 20°C induces UFA synthesis; isoleucine limitation at constant temperature increases membrane order and activates **des** via DesK/DesR, showing the sensed variable is fluidity rather than temperature per se (mendoza2014temperaturesensingby pages 5-6) | **Strong, direct, taxon-specific** | 10.1146/annurev-micro-091313-103612 |
| DesK/DesR activation → increases transcription of → **des** (Δ5 acyl-lipid desaturase) | *B. subtilis* regulatory genetics and membrane-sensing studies (mendoza2014temperaturesensingby pages 5-6) | **des** encodes the Δ5 desaturase responsible for introducing cis double bonds into saturated fatty acids during cold adaptation (mendoza2014temperaturesensingby pages 5-6) | **Strong, direct, taxon-specific** | 10.1146/annurev-micro-091313-103612 |
| **des** / unsaturated fatty-acid synthesis → helps maintain → low-temperature growth-permissive membrane state | Comparative membrane-adaptation literature across bacteria/archaea; psychrophile-focused lipid data (siliakus2017adaptationsofarchaeal pages 14-15, siliakus2017adaptationsofarchaeal pages 8-10, mendoza2014temperaturesensingby pages 5-6) | Psychrophilic bacteria increase unsaturation / alter BCFAs to maintain fluidity at low temperature; evidence supports contribution to Tmin and thus broader temperature delta when plasticity is high (siliakus2017adaptationsofarchaeal pages 14-15, siliakus2017adaptationsofarchaeal pages 8-10, mendoza2014temperaturesensingby pages 5-6) | **Moderate-to-strong, partly indirect for trait breadth; taxon-generalized** | 10.1007/s00792-017-0939-x; 10.1146/annurev-micro-091313-103612 |
| GroEL/GroES + LysU → enable → sustained high-temperature growth | *Escherichia coli* experimental evolution for growth at extreme temperature over >600 generations (rudolph2010evolutionofescherichia pages 1-2) | Thermoresistant cells achieved growth at **48.5°C**, ~**3°C** above wild-type maximum in LB; GroEL/GroES rose to **16-fold** above wild type; **lysU** deletion rendered thermoresistant cells thermosensitive (rudolph2010evolutionofescherichia pages 1-2) | **Strong, direct, sustained-growth, taxon-specific** | 10.1074/jbc.m110.103374 |
| DnaK/DnaJ → supports → growth at critical high temperature | *E. coli* genome-wide single-gene knockout screen for growth at critical high temperature (CHT) (murata2011molecularstrategyfor pages 4-5, murata2011molecularstrategyfor pages 1-2) | Among genes indispensable for growth at **46–47°C**, **dnaJ** and **dnaK** were the key overlap with heat-induced genes; supports sustained growth at CHT rather than mere shock survival (murata2011molecularstrategyfor pages 4-5, murata2011molecularstrategyfor pages 1-2) | **Strong, direct, taxon-specific** | 10.1371/journal.pone.0020063 |
| DegP protease → supports → growth at critical high temperature | *E. coli* CHT knockout screen and functional grouping of thermotolerant genes (murata2011molecularstrategyfor pages 4-5) | DegP identified as required at **46°C**; interpreted as removal of damaged proteins accumulated at high temperature during growth (murata2011molecularstrategyfor pages 4-5) | **Strong, direct, taxon-specific** | 10.1371/journal.pone.0020063 |
| c-di-AMP / potassium-homeostasis mutations → raise → upper growth limit | *Bacillus* experimental evolution under gradual warming; reaction norms and genome analysis (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17) | One *B. subtilis* lineage expanded its thermal niche by about **4°C** above baseline; convergent mutations implicated c-di-AMP and K+ homeostasis in increased high-temperature growth capacity (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17) | **Moderate-to-strong, direct evolutionary evidence, taxon-specific** | 10.3390/biology13121088 |
| oxidative-stress resistance systems → overlaps with → critical-high-temperature growth mechanisms | *E. coli* CHT mutant set cross-compared with H2O2 sensitivity phenotypes (murata2011molecularstrategyfor pages 4-5, murata2011molecularstrategyfor pages 1-2) | **More than half** of thermotolerant-gene mutants were also H2O2-sensitive at 30°C, indicating partial mechanistic overlap between oxidative defense and growth at **47°C** (murata2011molecularstrategyfor pages 1-2) | **Moderate, indirect overlap rather than single-edge mechanism; taxon-specific** | 10.1371/journal.pone.0020063 |


*Table: This table summarizes the strongest curatable edges for microbial temperature delta, emphasizing sustained-growth evidence and clearly separating direct mechanistic support from indirect or taxon-specific findings. It is useful as a compact screening artifact for deciding which nodes and edges are mature enough for TraitMech curation.*

### Additional edges for consideration

| Subject | Predicate | Object | Reference and supporting snippet | Curation assessment |
|---|---|---|---|---|
| cooling / increased membrane order | activates | DesK–DesR signaling | At 37°C *B. subtilis* primarily synthesizes saturated fatty acids, whereas transfer to 20°C induces unsaturated-fatty-acid synthesis. Constant-temperature manipulation of branched-chain precursors showed that membrane order, rather than temperature itself, activates the system. DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612), published September 2014. (mendoza2014temperaturesensingby pages 5-6) | **Curate**, but taxon-specific. The immediate stimulus is membrane physical state. |
| DesR-P | increases transcription of | `des` | The source describes phosphorylated DesR as the activator of `des`; `des` encodes a membrane Δ5 desaturase introducing cis double bonds into saturated fatty acids. (mendoza2014temperaturesensingby pages 5-6) | **Curate** as a molecular edge in *B. subtilis*. |
| unsaturated-fatty-acid synthesis | maintains | growth-permissive membrane fluidity at low temperature | Reviews report that psychrophilic bacteria increase unsaturation and alter branched-chain-fatty-acid composition to prevent excessive membrane packing at low temperature. DOI: [10.1007/s00792-017-0939-x](https://doi.org/10.1007/s00792-017-0939-x), published May 2017. (siliakus2017adaptationsofarchaeal pages 14-15, siliakus2017adaptationsofarchaeal pages 8-10) | **Curate cautiously**. Strong mechanism, but an explicit effect on whole temperature delta is usually inferred through Tmin. |
| archaeal tetraether/pentacyclic lipid remodeling | decreases | high-temperature membrane permeability | Pentacycle incorporation improves chain packing and lowers permeability; tetraether/diether composition varies with temperature. (siliakus2017adaptationsofarchaeal pages 8-10) | **Taxon-specific/indirect** unless paired with growth-boundary perturbation data. |
| GroEL–GroES overproduction | enables | evolved upper-temperature growth | Evolved *E. coli* grew at 48.5°C—about 3°C above wild-type Tmax—with GroEL/GroES approximately 16-fold above wild type; growth persisted for more than 600 generations. DOI: [10.1074/jbc.M110.103374](https://doi.org/10.1074/jbc.M110.103374), published June 2010. (rudolph2010evolutionofescherichia pages 1-2) | **High-priority direct edge** affecting Tmax. |
| LysU | is required for | GroEL/GroES-supported high-temperature growth | Deleting `lysU` rendered evolved thermoresistant cells thermosensitive. (rudolph2010evolutionofescherichia pages 1-2) | **Curate**, taxon- and background-specific. Avoid claiming LysU alone broadens delta. |
| DnaK–DnaJ | supports | growth at 46–47°C | In an *E. coli* genome-wide screen, `dnaK` and `dnaJ` were indispensable for critical-high-temperature growth and were among the few required genes also transcriptionally induced. DOI: [10.1371/journal.pone.0020063](https://doi.org/10.1371/journal.pone.0020063), published June 2011. (murata2011molecularstrategyfor pages 4-5, murata2011molecularstrategyfor pages 1-2) | **Curate** as high-temperature-growth support. |
| DegP-mediated damaged-protein removal | supports | growth at 46°C | DegP was required in the critical-high-temperature screen and interpreted as removing damaged proteins. (murata2011molecularstrategyfor pages 4-5) | **Curate cautiously**; direct essentiality, with mechanism assigned from protein function. |
| c-di-AMP/potassium-homeostasis mutations | increase | Bacillus upper growth boundary | Experimental evolution found convergent changes involving c-di-AMP and potassium homeostasis; one *B. subtilis* lineage extended its niche by 4°C. DOI: [10.3390/biology13121088](https://doi.org/10.3390/biology13121088), published December 2024. (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17) | **Promising recent edge**, but curate the exact mutated gene/allele from the primary study rather than a generic c-di-AMP node. |
| compatible solutes | protect | high-temperature growth/proteostasis | The 2024 Bacillus study discusses glycine betaine and proline as heat protectants in connection with osmotic protection. (hurtadobautista2024thermalplasticityand pages 16-17) | **Uncertain for delta**. Add only when a defined transporter or biosynthetic mutation demonstrably shifts Tmin/Tmax. |
| cold-shock proteins | support | cold growth | Cold-shock reviews describe Csp proteins, trigger factor, and PPiB as preserving transcription, translation, or folding; some deletion phenotypes are cold-sensitive. Trehalose-null *E. coli* grew normally at 16°C but had reduced viability at 4°C. DOI: [10.3184/003685003783238707](https://doi.org/10.3184/003685003783238707), published February 2003. (weber2003bacterialcoldshock pages 36-38) | **Do not yet connect directly to temperature delta** without endpoint growth data. The trehalose result is primarily viability, not Tmin shift. |
| oxidative-stress defenses | contribute to | critical-high-temperature growth | Of 51 genes required for *E. coli* growth at 47°C, more than half of corresponding mutants were also H2O2-sensitive at 30°C. (murata2011molecularstrategyfor pages 1-2) | **Indirect module-level edge**. The statistic supports overlap, not a single linear mechanism. |

## 4. Recent developments and quantitative findings

### Bacillus thermal evolution, 2024

Experimental evolution across seven strains from two Bacillus groups found strong evolutionary constraints. Mesophilic strains ordinarily grew around 27–40°C; one *B. subtilis* strain expanded its upper thermal niche by approximately 4°C, but neither group generally evolved robust growth only 3°C above its natural range. Convergent changes implicated c-di-AMP-mediated potassium and osmotic homeostasis. The authors relate this limited adaptive capacity to projected warming of approximately 2–4°C. These results support a graph in which ionic homeostasis and membrane stabilization influence Tmax, while genetic background modifies the strength of those edges. (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17)

### Growth and shock-resistance trade-offs, 2024

Repeated heat shock in *Salmonella Typhimurium* selected loss-of-function `dnaJ` mutants with greatly elevated shock resistance but attenuated growth at 37°C and higher temperatures. This is especially important for ontology curation: **acute heat resistance must not be used as a proxy for temperature delta**. It also argues against unconditional edges such as “DnaJ loss increases temperature tolerance”; the phenotype depends on whether tolerance means survival or sustained growth.

### Modern thermal-performance modeling

A 2024 comparative analysis fitted 83 models to 2,739 thermal-performance datasets and found no universally best mathematical form across traits and taxa. Although not microbial-only, the result reinforces the need to retain raw endpoint definitions and model uncertainty rather than treating inferred Tmin/Tmax as assay-independent constants. DOI: [10.1038/s41467-024-53046-2](https://doi.org/10.1038/s41467-024-53046-2), published October 2024.

### Mechanistic statistics from established perturbation studies

- Evolved *E. coli*: Tmax increased by approximately 3°C to 48.5°C; GroEL/GroES reached approximately 16-fold wild-type abundance; adaptation was maintained for more than 600 generations. (rudolph2010evolutionofescherichia pages 1-2)
- *E. coli* critical-temperature screen: 51 genes were required for growth at 47°C; more than half of mutants were also H2O2-sensitive at 30°C. (murata2011molecularstrategyfor pages 1-2)
- Plant-pathogenic bacteria: a review reports that *Pseudomonas cichorii* `dnaJ` deletion reduced growth by 20% at 40°C and 60% at 60°C; an *Xanthomonas campestris* `hspA` disruption caused a tenfold growth reduction at 37°C under osmotic stress. These are useful supporting phenotypes but are conditioned by taxon and co-stressor. DOI: [10.3390/ijms26020528](https://doi.org/10.3390/ijms26020528), published January 2025. (figaj2025theroleof pages 8-10)

## 5. Current applications and real-world relevance

1. **Industrial fermentation and synthetic biology.** Temperature-response models are used to select operating temperatures and could support dynamic temperature control, although a 2020 review concluded that temperature remains underused as an active bioprocess-control variable. A broader engineered delta could reduce cooling demand and improve resilience to reactor gradients. DOI: [10.3390/pr8010121](https://doi.org/10.3390/pr8010121), published January 2020. (noll2020modelingandexploiting pages 6-8)
2. **Food safety.** Growth-range endpoints determine whether pathogens can proliferate during refrigeration, processing, or temperature abuse. Shock-survival selection may produce unexpected trade-offs in pathogen growth and virulence, as shown by the 2024 Salmonella study.
3. **Climate-risk forecasting.** Thermal delta and reaction norms constrain persistence under warming and variability. The Bacillus evolution work suggests that some soil bacteria may not readily evolve growth only a few degrees above present limits. (hurtadobautista2024thermalplasticityand pages 1-2)
4. **Extremophile biotechnology.** Membrane and proteostasis modules are engineering targets for robust enzymes, whole-cell catalysts, high-temperature bioleaching, and biomass conversion. However, transfer of one module rarely guarantees a wider delta because the growth boundary is systems-level.
5. **Culture design and microbial ecology.** Temperature delta can help predict establishment across seasonal regimes, but observed distributions also reflect pH, salinity, pressure, nutrient availability, competition, and dispersal.

## 6. Recommended minimal TraitMech graph

A conservative first revision could retain approximately 10–12 nodes and the following core structure:

1. minimum growth temperature → **defines lower bound of** → `METPO:1000303`
2. maximum growth temperature → **defines upper bound of** → `METPO:1000303`
3. low membrane fluidity → **activates** → DesK–DesR
4. DesK–DesR → **increases expression of** → `des`
5. Des/Δ5-desaturase → **increases** → unsaturated-fatty-acid content
6. unsaturated-fatty-acid content → **maintains** → low-temperature membrane fluidity
7. low-temperature membrane fluidity → **supports** → growth near Tmin
8. GroEL–GroES proteostasis → **supports** → growth near Tmax
9. LysU → **is required for** → evolved GroEL–GroES-dependent high-temperature growth
10. DnaK–DnaJ and DegP protein quality control → **supports** → growth near Tmax
11. c-di-AMP-regulated potassium homeostasis → **supports** → Bacillus high-temperature growth
12. growth near Tmin + growth near Tmax → **determines** → temperature delta

Edges 3–7 should carry a *B. subtilis*/bacterial qualifier; edges 8–10 an *E. coli* qualifier; edge 11 a Bacillus and experimental-evolution qualifier. A generic cross-taxon graph should connect these as alternative mechanisms rather than implying that every microbe possesses every module.

## 7. Warnings: claims not yet ready for curation

- **Do not curate heat- or cold-shock survival as a direct increase in `METPO:1000303`.** Require sustained net growth or an explicitly shifted cardinal endpoint.
- **Do not infer breadth from a single Tmin, Topt, or Tmax.** Two endpoints are required.
- **Do not treat induction as causation.** Heat-induced `groEL`, `dnaK`, antioxidant, or lipid genes are candidate mechanisms unless perturbation changes growth boundaries.
- **Do not generalize taxon-specific systems.** DesK/DesR is not a universal bacterial thermosensor; archaeal membrane adaptation uses different chemistry.
- **Compatible-solute edges remain conditional.** Trehalose, glycine betaine, proline, ectoine, and hydroxyectoine often improve stress survival, but relatively few studies measure a full delta shift.
- **Oxidative defense is currently a module-level association.** The >50% overlap among high-temperature and H2O2-sensitive mutants does not identify one universal causal chain. (murata2011molecularstrategyfor pages 1-2)
- **Membrane composition correlations are insufficient by themselves.** Prefer genetic, chemical, or supplementation experiments that shift a growth endpoint.
- **Do not encode the ~80°C lipid boundary as a universal law.** It is a comparative pattern with exceptions. (siliakus2017adaptationsofarchaeal pages 8-10)
- **Avoid unverified ontology identifiers.** Use label-only nodes for c-di-AMP, ectoine derivatives, DesK/DesR, and taxon-specific proteins until CHEBI/UniProt/EC records are checked directly.
- **Record environmental interactions.** Pressure, pH, salinity, oxygen, water activity, and medium can change both endpoints and therefore the observed delta.

## DOI-first bibliography

1. Hurtado-Bautista E. et al. “Thermal Plasticity and Evolutionary Constraints in Bacillus: Implications for Climate Change Adaptation.” *Biology* 13, 1088. Published December 2024. [https://doi.org/10.3390/biology13121088](https://doi.org/10.3390/biology13121088). (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17)
2. Kontopoulos D-G. et al. “No universal mathematical model for thermal performance curves across traits and taxonomic groups.” *Nature Communications* 15. Published October 2024. [https://doi.org/10.1038/s41467-024-53046-2](https://doi.org/10.1038/s41467-024-53046-2).
3. Berdejo D. et al. “Evolutionary trade-off between heat shock resistance, growth at high temperature, and virulence expression in Salmonella Typhimurium.” *mBio* 15. Published March 2024. [https://doi.org/10.1128/mbio.03105-23](https://doi.org/10.1128/mbio.03105-23).
4. Siliakus MF, van der Oost J, Kengen SWM. “Adaptations of archaeal and bacterial membranes to variations in temperature, pH and pressure.” *Extremophiles* 21:651–670. Published May 2017. [https://doi.org/10.1007/s00792-017-0939-x](https://doi.org/10.1007/s00792-017-0939-x). (siliakus2017adaptationsofarchaeal pages 14-15, siliakus2017adaptationsofarchaeal pages 8-10)
5. de Mendoza D. “Temperature sensing by membranes.” *Annual Review of Microbiology* 68:101–116. Published September 2014. [https://doi.org/10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). (mendoza2014temperaturesensingby pages 5-6)
6. Murata M. et al. “Molecular Strategy for Survival at a Critical High Temperature in Escherichia coli.” *PLoS ONE* 6:e20063. Published June 2011. [https://doi.org/10.1371/journal.pone.0020063](https://doi.org/10.1371/journal.pone.0020063). (murata2011molecularstrategyfor pages 4-5, murata2011molecularstrategyfor pages 1-2)
7. Rudolph B. et al. “Evolution of Escherichia coli for Growth at High Temperatures.” *Journal of Biological Chemistry* 285:19029–19034. Published June 2010. [https://doi.org/10.1074/jbc.M110.103374](https://doi.org/10.1074/jbc.M110.103374). (rudolph2010evolutionofescherichia pages 1-2)
8. Noll P. et al. “Modeling and Exploiting Microbial Temperature Response.” *Processes* 8:121. Published January 2020. [https://doi.org/10.3390/pr8010121](https://doi.org/10.3390/pr8010121). (noll2020modelingandexploiting pages 6-8)
9. Weber MHW, Marahiel MA. “Bacterial Cold Shock Responses.” *Science Progress* 86. Published February 2003. [https://doi.org/10.3184/003685003783238707](https://doi.org/10.3184/003685003783238707). (weber2003bacterialcoldshock pages 36-38)
10. Figaj D. “The Role of Heat Shock Protein Chaperones in Environmental Stress Adaptation and Virulence of Plant Pathogenic Bacteria.” *International Journal of Molecular Sciences* 26:528. Published January 2025. [https://doi.org/10.3390/ijms26020528](https://doi.org/10.3390/ijms26020528). (figaj2025theroleof pages 8-10)

**Overall curation judgment:** The trait is suitable for TraitMech, but the graph should represent temperature delta as the combined outcome of two growth boundaries. The most mature mechanistic branches are membrane homeoviscous adaptation at the lower boundary and protein-quality-control/ionic-homeostasis mechanisms at the upper boundary. Direct edges from generic “thermotolerance” or “stress survival” to `METPO:1000303` should be excluded until an actual Tmin or Tmax shift is demonstrated.

References

1. (noll2020modelingandexploiting pages 6-8): Philipp Noll, Lars Lilge, Rudolf Hausmann, and Marius Henkel. Modeling and exploiting microbial temperature response. ArXiv, 8:121, Jan 2020. URL: https://doi.org/10.3390/pr8010121, doi:10.3390/pr8010121. This article has 73 citations.

2. (siliakus2017adaptationsofarchaeal pages 14-15): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

3. (siliakus2017adaptationsofarchaeal pages 8-10): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

4. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

5. (rudolph2010evolutionofescherichia pages 1-2): Birgit Rudolph, Katharina M. Gebendorfer, Johannes Buchner, and Jeannette Winter. Evolution of escherichia coli for growth at high temperatures. Journal of Biological Chemistry, 285:19029-19034, Jun 2010. URL: https://doi.org/10.1074/jbc.m110.103374, doi:10.1074/jbc.m110.103374. This article has 200 citations and is from a domain leading peer-reviewed journal.

6. (murata2011molecularstrategyfor pages 4-5): Masayuki Murata, Hiroko Fujimoto, Kaori Nishimura, Kannikar Charoensuk, Hiroshi Nagamitsu, Satish Raina, Tomoyuki Kosaka, Taku Oshima, Naotake Ogasawara, and Mamoru Yamada. Molecular strategy for survival at a critical high temperature in eschierichia coli. PLoS ONE, 6:e20063, Jun 2011. URL: https://doi.org/10.1371/journal.pone.0020063, doi:10.1371/journal.pone.0020063. This article has 119 citations and is from a peer-reviewed journal.

7. (murata2011molecularstrategyfor pages 1-2): Masayuki Murata, Hiroko Fujimoto, Kaori Nishimura, Kannikar Charoensuk, Hiroshi Nagamitsu, Satish Raina, Tomoyuki Kosaka, Taku Oshima, Naotake Ogasawara, and Mamoru Yamada. Molecular strategy for survival at a critical high temperature in eschierichia coli. PLoS ONE, 6:e20063, Jun 2011. URL: https://doi.org/10.1371/journal.pone.0020063, doi:10.1371/journal.pone.0020063. This article has 119 citations and is from a peer-reviewed journal.

8. (hurtadobautista2024thermalplasticityand pages 1-2): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

9. (hurtadobautista2024thermalplasticityand pages 16-17): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

10. (weber2003bacterialcoldshock pages 36-38): Michael H.W. Weber and Mohamed A. Marahiel. Bacterial cold shock responses. Science Progress, 86:75-9, Feb 2003. URL: https://doi.org/10.3184/003685003783238707, doi:10.3184/003685003783238707. This article has 253 citations.

11. (figaj2025theroleof pages 8-10): Donata Figaj. The role of heat shock protein (hsp) chaperones in environmental stress adaptation and virulence of plant pathogenic bacteria. International Journal of Molecular Sciences, 26:528, Jan 2025. URL: https://doi.org/10.3390/ijms26020528, doi:10.3390/ijms26020528. This article has 33 citations.