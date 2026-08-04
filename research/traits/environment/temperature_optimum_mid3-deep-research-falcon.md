---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:55:45.858745'
end_time: '2026-08-04T04:04:27.208707'
duration_seconds: 521.35
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum mid3
  trait_identifier: METPO:1000445
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_mid3
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ between approximately 30 and 34 \xB0C, characteristic of mesophilic physiology."
  parent_traits: METPO:1000304
  synonyms: Mesophilie, TO_30_to_34
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports the 30\u201334 \xB0C optimum as a\
    \ typical mesophile setpoint near common host body temperatures.)"
  causal_graph_summary: 'temperature_optimum_mid3_upper_mesophile: 12 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid3
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000445
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 30 and 34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C optimum as a typical mesophile setpoint near common host body temperatures.)
- **Existing causal graph summary:** temperature_optimum_mid3_upper_mesophile: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **temperature optimum mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid3.yaml`.

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
- **Trait label:** temperature optimum mid3
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000445
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 30 and 34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C optimum as a typical mesophile setpoint near common host body temperatures.)
- **Existing causal graph summary:** temperature_optimum_mid3_upper_mesophile: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **temperature optimum mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid3.yaml`.

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


# Curation report: microbial “temperature optimum mid3”

## Executive assessment

**Target:** `METPO:1000445` — **temperature optimum mid3**  
**Category:** ENVIRONMENT; **term kind:** CLASS; **status:** REVIEWED  
**Parent:** `METPO:1000304`  
**Synonyms:** *Mesophilie*, `TO_30_to_34`

The trait should denote an **organism-level optimal growth temperature whose experimentally estimated optimum lies between approximately 30 and 34 °C**. Operationally, the optimum is the temperature at which a fitted thermal-performance curve, maximum specific growth rate, or suitably validated biomass-production assay reaches its maximum under stated medium, pH, oxygen, salinity, pressure, and measurement conditions. It is an upper-mesophilic sub-bin, not a mechanistic process by itself.

The principal curation conclusion is that membrane homeoviscous adaptation, metabolic rearrangement, ion/osmolyte homeostasis, translation, and proteostasis are plausible mechanistic contributors to growth around this interval. However, the retrieved literature rarely demonstrates that any one component **causes an organism’s optimum specifically to fall at 30–34 °C**. Most evidence concerns acclimation after a temperature shift, cold or heat tolerance, or broader mesophilic growth. Such edges may be curated as supporting mechanisms only when their taxonomic and assay scope is explicit.

## 1. Trait scope and boundaries

### Positive scope

A record supports `METPO:1000445` when:

1. the measured object is a microbial strain or isolate rather than an isolated enzyme or mixed community;
2. growth is evaluated at multiple temperatures that bracket the maximum, preferably including values below 30 °C, within 30–34 °C, and above 34 °C;
3. the optimum is defined from specific growth rate, doubling time, colony expansion, biomass accumulation, or another validated growth endpoint; and
4. the reported or fitted optimum is approximately 30–34 °C.

This range lies within common definitions of mesophily. For example, recent experimental-evolution literature describes mesophiles as organisms with growth-temperature optima of approximately 25–45 °C and thermophiles as having optima above 45 °C. A global thermal-performance analysis likewise treated optima up to roughly 45 °C as mesophilic (lehmann2023adaptivelaboratoryevolution pages 1-2).

### Boundary cases to exclude or qualify

- **Growth at 30–34 °C is not sufficient.** The organism must grow best there relative to bracketing temperatures.
- **Maximum growth temperature is not optimum growth temperature.** Survival or weak growth above 34 °C does not move the optimum.
- **Thermotolerance and heat-shock survival are separate traits.** The 2024 *Bacillus* evolution study chiefly concerns expansion of upper thermal limits and stress tolerance, not placement of the optimum at 30–34 °C (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17).
- **Cold adaptation is not a mid3 optimum.** Increased unsaturated lipids or retained activity at 5 °C supports a general temperature-adaptation mechanism, not this particular optimum (yang2023insightintothe pages 1-2).
- **Enzyme activity optima, membrane transitions, and EF-1A binding optima are proxies**, not organismal OGTs, unless independently calibrated and validated.
- **Community/process optima**—for anaerobic digesters, compost, or wastewater consortia—must not be assigned directly to an organismal phenotype.
- **Assay dependence matters.** Medium, oxygen availability, pH, salinity, pressure, inoculum history, growth phase, and temperature increment can shift the apparent optimum.
- A broad plateau spanning, for example, 28–37 °C is not necessarily a precise 30–34 °C optimum. Record the uncertainty or interval rather than forcing a bin.

## 2. Current mechanistic understanding

### 2.1 Membrane homeoviscous adaptation

The strongest, most mature causal module is the *Bacillus subtilis* Des pathway. Cooling increases bilayer order. The membrane histidine kinase DesK senses this physical state, phosphorylates the response regulator DesR, and thereby activates transcription of `des`, encoding a Δ5 acyl-lipid desaturase. Desaturation increases unsaturated fatty acids and restores membrane fluidity. Crucially, isothermal manipulation of branched-chain fatty-acid synthesis showed that increased membrane order can induce the pathway without a temperature change, supporting **membrane physical state**, rather than temperature alone, as the proximate signal (mendoza2014temperaturesensingby pages 5-6).

The review’s concise statement is that bacteria incorporate “proportionally more unsaturated fatty acids … as growth temperature decreases,” thereby disrupting lipid order and optimizing physiological performance at the new temperature (mendoza2014temperaturesensingby pages 5-6). This directly supports a homeostatic mechanism but was characterized using a 37→20 °C cold-shift model, not a 30–34 °C optimum assay.

Recent evidence remains consistent with the module. At 5 °C, *Bacillus simplex* H-b showed a higher unsaturated-fatty-acid proportion alongside altered transport, ATP/EPS accumulation, cofactor and vitamin synthesis, and stress responses (yang2023insightintothe pages 1-2). Conversely, perturbing the fatty-acid regulator `fabR` in *Escherichia coli* delayed recovery after a 27→37 °C upshift; after a shift to 44 °C, Δ`fabR` cells stopped growing and died within 30–40 min while wild type retained growth and morphology (knapp2025metabolicrearrangementenables pages 23-24). These findings support membrane composition as a contributor to thermal performance but not as a universal determinant of a 30–34 °C optimum.

### 2.2 Metabolic rearrangement and temperature memory

A high-quality recent study found that *E. coli* growth between approximately 25 and 37 °C follows Arrhenius-like behavior and adapts to temperature shifts through **metabolome rearrangement within an autocatalytic enzyme network**. The reported activation energy was about 13 kcal mol⁻¹ for *E. coli*, with approximately 10–15 kcal mol⁻¹ across tested strains and organisms. Following a 27→37 °C upshift, growth initially spiked and then approached steady state over about 35 min; the overall adaptation timescale was approximately 1.5 doublings (knapp2025metabolicrearrangementenables pages 1-2, knapp2025metabolicrearrangementenables pages 3-4).

The authors found the proteome largely invariant over 25–37 °C. Ribosomal-protein fractions tracked growth rate and medium rather than temperature itself. Cells exposed to a 37→25 °C downshift for 10 min recovered after return to 37 °C in under 10 min, whereas a steady-state 25→37 °C upshift required roughly 40 min. This asymmetry indicates metabolic temperature memory and slower resource reallocation after sustained growth at the lower temperature (knapp2025metabolicrearrangementenables pages 4-5). The evidence argues against a graph in which transcriptional reprogramming alone controls all near-mesophilic thermal adaptation.

### 2.3 Proteostasis, translation, and heat-shock systems

Chaperones and heat-shock proteins stabilize cellular components when temperatures exceed the preferred range. The 2024 *Bacillus* study describes heat-shock response activation but also shows strong evolutionary constraint: *B. subtilis* expanded its thermal niche by at most 4 °C, whereas tested *B. cereus* strains did not adapt successfully to the imposed warming despite higher mutation rates (hurtadobautista2024thermalplasticityand pages 1-2). These are useful **upper-bound/tolerance** mechanisms, but no direct evidence establishes a causal path from a specific chaperone to OGT 30–34 °C.

Translation and protein stability remain plausible limiting modules, especially near upper thermal limits. Nevertheless, the near-mesophilic *E. coli* results caution that stable proteome composition can coexist with substantial growth-rate adaptation through metabolite redistribution (knapp2025metabolicrearrangementenables pages 1-2, knapp2025metabolicrearrangementenables pages 4-5). TraitMech should distinguish **proteome composition**, **protein folding/stability**, **ribosome activity**, and **metabolic state** rather than collapsing them into one node.

### 2.4 c-di-AMP, potassium, and osmolyte homeostasis

Experimental evolution in *Bacillus* produced convergent mutations in diadenylate-cyclase-associated genes—`cdaR` in *B. subtilis* and `disA` in *B. cereus*. The implicated c-di-AMP network regulates potassium transport and osmotic balance. Glycine betaine and proline are also described as heat protectants (hurtadobautista2024thermalplasticityand pages 16-17). This supports a taxon-specific path from c-di-AMP signaling through ion/osmolyte homeostasis to heat tolerance.

It does **not** yet justify a universal edge from c-di-AMP to `METPO:1000445`: c-di-AMP is absent from many microbial lineages, and the experiments address upper thermal tolerance rather than optimum placement.

## 3. Candidate graph nodes

### Trait and environmental/assay nodes

- **temperature optimum mid3** — `METPO:1000445`
- **parent temperature-optimum phenotype** — `METPO:1000304`
- ambient temperature, 30–34 °C — label-only interval node; optionally represent temperature quantity using the project’s standard measurement schema
- temperature decrease / temperature upshift — experimental-factor nodes
- growth medium composition; carbon source; oxygen availability; pH; salinity; pressure; inoculum thermal history; incubation duration
- maximum specific growth rate; doubling time; biomass yield; thermal-performance curve

### Cellular components and locations

- plasma/cytoplasmic membrane — `GO:0005886`
- membrane lipid bilayer — `GO:0005886` may be used only if the project accepts the plasma-membrane proxy; otherwise retain label-only
- cytoplasm — `GO:0005737`
- ribosome — `GO:0005840`
- proteome; metabolome — label-only candidates

### Genes, proteins, and complexes

- DesK membrane histidine kinase — label-only unless a taxon-specific UniProt accession is selected
- DesR response regulator — label-only
- `des` / Δ5 acyl-lipid desaturase — label-only; enzyme grounding should be checked against the exact substrate and reaction
- `fabR`, fatty-acid-responsive transcriptional regulator — label-only
- c-di-AMP cyclases/regulators: `cdaR`, `disA` — label-only or taxon-specific UniProt
- potassium transport systems — Ktr/KimA family; select taxon-specific accessions only
- molecular chaperones/heat-shock proteins — use individual proteins where evidence is available rather than an undifferentiated universal node
- ribosomal proteins and translation apparatus — `GO:0006412` for translation

### Chemicals and molecular states

- unsaturated fatty acid — `CHEBI:27208`
- fatty acid — `CHEBI:35366`
- potassium ion — `CHEBI:29103`
- cyclic di-AMP — use a verified ChEBI accession during implementation; retain label-only here rather than risk an incorrect identifier
- glycine betaine — `CHEBI:17750`
- L-proline — `CHEBI:17203`
- membrane fluidity / membrane lipid order — label-only physical-state nodes
- ATP — `CHEBI:15422`
- extracellular polymeric substances — label-only collective material
- plasmalogens and short-chain fatty acids — ground only when exact molecular species are known

### Processes and pathways

- fatty-acid biosynthetic process — `GO:0006633`
- unsaturated-fatty-acid biosynthetic process — `GO:0006636`
- signal transduction — `GO:0007165`
- two-component signal transduction — retain label-only unless the intended GO term is verified in the curation environment
- response to heat — `GO:0009408`
- response to cold — `GO:0009409`
- protein folding — `GO:0006457`
- potassium-ion transport — `GO:0006813`
- cellular potassium-ion homeostasis — `GO:0030007`
- metabolic rearrangement; thermal memory; proteome reallocation — label-only candidate processes

## 4. Candidate evidence-backed edges

The compact edge set below separates well-established mechanistic steps from inferred links to the target phenotype.

| subject | predicate | object | evidence strength/status | organism/context | DOI |
|---|---|---|---|---|---|
| ambient temperature decrease | increases | membrane lipid order / decreased membrane fluidity | strong, direct; stress-response; taxon-generalized from Bacillus model (mendoza2014temperaturesensingby pages 5-6) | *Bacillus subtilis* cold-shift model | 10.1146/annurev-micro-091313-103612 |
| increased membrane order | activates | DesK histidine kinase | strong, direct; taxon-specific (mendoza2014temperaturesensingby pages 5-6) | *B. subtilis* membrane thermosensor | 10.1146/annurev-micro-091313-103612 |
| DesK | phosphorylates | DesR | strong, direct; taxon-specific (mendoza2014temperaturesensingby pages 5-6) | *B. subtilis* two-component signaling | 10.1146/annurev-micro-091313-103612 |
| DesR | positively regulates transcription of | des (Δ5 desaturase gene) | strong, direct; taxon-specific (mendoza2014temperaturesensingby pages 5-6) | *B. subtilis* cold-response regulon | 10.1146/annurev-micro-091313-103612 |
| Des acyl-lipid desaturase | increases synthesis of | unsaturated fatty acids | strong, direct; taxon-specific (mendoza2014temperaturesensingby pages 5-6) | *B. subtilis* membrane remodeling | 10.1146/annurev-micro-091313-103612 |
| unsaturated fatty acids | increase | membrane fluidity | strong, direct; broad microbial principle (mendoza2014temperaturesensingby pages 5-6, yang2023insightintothe pages 1-2) | membrane homeoviscous adaptation; also observed in cold-adapted denitrifier | 10.1146/annurev-micro-091313-103612 |
| temperature range 25–37 °C | induces adaptation by | metabolic rearrangement | moderate, direct; not optimum-specific; Arrhenius-range evidence (knapp2025metabolicrearrangementenables pages 1-2, knapp2025metabolicrearrangementenables pages 3-4) | *Escherichia coli* and comparative microbial systems | 10.1038/s41564-024-01841-4 |
| metabolic rearrangement | enables | growth-rate adaptation after temperature shifts | moderate, direct; not optimum-specific (knapp2025metabolicrearrangementenables pages 1-2, knapp2025metabolicrearrangementenables pages 4-5) | *E. coli* upshift/downshift dynamics | 10.1038/s41564-024-01841-4 |
| fabR perturbation | delays | thermal recovery after upshift | moderate, direct; membrane-linked; genotype-specific (knapp2025metabolicrearrangementenables pages 23-24) | *E. coli* ΔfabR after 27→37 °C upshift | 10.1038/s41564-024-01841-4 |
| c-di-AMP synthesis / potassium homeostasis | contributes to | heat tolerance | moderate, direct but stress-response; taxon-specific (hurtadobautista2024thermalplasticityand pages 16-17) | evolved *Bacillus subtilis* / *B. cereus* | 10.3390/biology13121088 |
| compatible solutes (e.g., glycine betaine, proline) | provide | thermoprotection / increased heat tolerance | moderate, stress-response; taxon-focused review evidence (hurtadobautista2024thermalplasticityand pages 16-17) | *Bacillus* heat/osmotic stress context | 10.3390/biology13121088 |
| temperature regime | shapes | microbial community composition | moderate, direct; process/community-level, not organismal OGT (wu2024effectoftemperature pages 1-2) | anaerobic digestion inoculum preservation and 55→37 °C transition | 10.3390/agronomy14122991 |
| microbial community composition | affects | process performance | moderate, direct; process/community-level (wu2024effectoftemperature pages 1-2) | mesophilic anaerobic digestion startup and methane-associated stability | 10.3390/agronomy14122991 |
| temperature decrease to 5 °C | increases | unsaturated fatty acid proportion | moderate, direct; cold-adaptation; taxon-specific (yang2023insightintothe pages 1-2) | *Bacillus simplex* H-b during aerobic denitrification | 10.1128/AEM.01928-22 |
| elevated unsaturated fatty acid proportion | supports | survival / activity under cold conditions | moderate, direct; denitrification application context, not OGT-setting (yang2023insightintothe pages 1-2) | wastewater denitrifier at 5, 20, 30 °C | 10.1128/AEM.01928-22 |
| membrane adaptation + metabolic rearrangement + ion/osmolyte homeostasis | may contribute to | temperature optimum mid3 (30–34 °C) | inferred/uncertain; should not be curated as a direct universal determinant without trait-matched assays (mendoza2014temperaturesensingby pages 5-6, knapp2025metabolicrearrangementenables pages 1-2, wu2024effectoftemperature pages 1-2) | upper-mesophile trait synthesis across taxa | multiple |


*Table: This table summarizes compact, curation-focused candidate causal edges relevant to METPO:1000445, separating direct mechanistic evidence from stress-response, taxon-specific, and community-level evidence. It is useful for deciding which edges are mature enough for TraitMech curation and which should remain inferred or uncertain.*

### Recommended first-pass graph architecture

A conservative YAML graph could contain three evidence modules without yet forcing all of them into a direct universal path to the target:

1. **Membrane module:**  
   `temperature decrease → increased membrane order → DesK activation → DesR phosphorylation → des transcription → UFA synthesis → increased membrane fluidity → supports growth after cooling`.

2. **Metabolic module:**  
   `temperature shift within 25–37 °C → temperature-sensitive enzyme kinetics → metabolome rearrangement → transient thermal memory → growth-rate adaptation`.

3. **Ion/stress module, Bacillus-specific:**  
   `c-di-AMP network perturbation → altered potassium/osmolyte homeostasis → altered heat tolerance`.

The final links from these modules to `METPO:1000445` should initially be `contributes_to` or `associated_with`, marked uncertain, unless a study measures the complete thermal-performance curve and demonstrates a shifted optimum into or out of 30–34 °C after genetic or chemical intervention.

## 5. Recent developments, statistics, and applications

### Experimental evolution

A 2023 adaptive-laboratory-evolution experiment offers unusually direct proof that OGT itself can evolve. *Thermoanaerobacter kivui* began with `TOPT = 66 °C` and `TMIN = 39 °C`. After 67 transfers—approximately 180 generations—at 45 °C, its optimum shifted to 60 °C. The evolved genome had 67 SNPs across 2.397 Mbp; membrane changes included increased plasmalogens and reduced lipid-chain length at lower temperature, and a `fabG` P216L mutation was proposed as a contributor (lehmann2023adaptivelaboratoryevolution pages 1-2, lehmann2023adaptivelaboratoryevolution pages 6-7). This is strong evidence for evolvability of OGT and membrane involvement, but the organism remained thermophilic and the individual mutations were not established as causal.

### Wastewater denitrification

*B. simplex* H-b retained 27.22% nitrogen removal at 5 °C. Transcriptomes were compared at 5, 20, and 30 °C, revealing increased unsaturated lipids, ATP and EPS accumulation, transport changes, and cofactor/vitamin and stress-response adjustments. Most aerobic denitrifiers discussed in the study perform efficiently at approximately 25–37 °C, making the cold-active strain useful for winter wastewater treatment (yang2023insightintothe pages 1-2). This application validates temperature-adaptation modules but does not establish a 30–34 °C optimum.

### Anaerobic digestion

In a 2024 continuous-reactor study, inoculum stored at 35 °C retained greater bacterial diversity than inoculum stored at 15 °C and supported stable mesophilic digester startup. A 55→37 °C transition maintained bacterial richness and archaeal diversity and favored hydrogenotrophic methanogens. Increased Coriobacteriaceae and Prevotellaceae correlated with propionate and butyrate accumulation and reduced operational capacity (wu2024effectoftemperature pages 1-2). These are process- and community-level causal candidates; they must not be assigned directly to an isolate’s OGT.

### Vinegar fermentation

A 2024 authoritative review reports that acetic-acid fermentation can exceed 40 °C, while growth of most acetic-acid bacteria is severely inhibited above 34 °C. Thermotolerant strains capable of functioning at 37–42 °C can reduce cooling requirements. Relevant mechanisms include membrane-composition changes, membrane-bound enzymes, efflux systems, and molecular chaperones. Ethanol above 4% and acetic acid above 5 g L⁻¹ add interacting stresses, illustrating why temperature optima must be recorded with chemical conditions (hua2024regulatorymechanismsof pages 1-3).

## 6. Expert interpretation for TraitMech

The literature supports a **systems-level** model rather than a single “temperature-optimum gene.” At moderate temperatures, reaction kinetics can accelerate growth, but membrane state, metabolite allocation, translation, ion balance, and protein stability impose different constraints as temperature moves away from the optimum. The observed optimum is therefore an emergent maximum of a thermal-performance curve.

Two expert-level cautions are particularly important:

- Membrane adaptation is strongly causal for maintaining function after cooling, but the canonical DesK/DesR evidence comes from *B. subtilis* and a 37→20 °C perturbation. It should not be generalized across all bacteria, archaea, or fungi (mendoza2014temperaturesensingby pages 5-6).
- Near the mesophilic range, *E. coli* adaptation can occur largely through metabolome rearrangement without major proteome-composition changes. A graph that assumes every thermal response is mediated by altered gene expression would conflict with current evidence (knapp2025metabolicrearrangementenables pages 1-2, knapp2025metabolicrearrangementenables pages 4-5).

## 7. Claims not yet ready for curation

1. **Do not curate:** “more unsaturated fatty acids cause an optimum of 30–34 °C.” The evidence supports fluidity restoration after cooling, not a bin-specific optimum.
2. **Do not curate universally:** “DesK senses temperature.” More precisely, in *B. subtilis*, DesK senses temperature-dependent membrane state; isothermal membrane ordering can activate the system (mendoza2014temperaturesensingby pages 5-6).
3. **Do not equate heat tolerance with OGT.** c-di-AMP, potassium, compatible solutes, chaperones, and HSPs chiefly support stress resistance in the cited experiments (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17).
4. **Do not infer organismal OGT from community reactors.** The 35–37 °C anaerobic-digestion results concern succession and process stability (wu2024effectoftemperature pages 1-2).
5. **Do not treat an isolated-enzyme optimum as organismal OGT** without a validated calibration.
6. **Do not assign causal status to ALE SNPs individually.** The 67 mutations in evolved *T. kivui*, including `fabG` P216L and a subpopulation carrying sigma-factor-H G28V, remain candidates rather than validated causes (lehmann2023adaptivelaboratoryevolution pages 6-7).
7. **Do not create unsupported ontology IDs.** Keep DesK, DesR, thermal memory, membrane order, and collective lipid classes as label-only nodes until exact species, sequence, substrate, and reaction are known.
8. The supplied statement that the 30–34 °C optimum is “near common host body temperatures” is contextually plausible but not universal: 30–34 °C is below the approximately 37 °C core temperature of many mammalian hosts and may better match ectothermic hosts, peripheral tissues, or environmental niches.

## 8. DOI-first bibliography

1. **de Mendoza D.** “Temperature sensing by membranes.” *Annual Review of Microbiology* 68, 101–116. **Published September 2014.** DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). Foundational membrane-fluidity and DesK/DesR review. (mendoza2014temperaturesensingby pages 5-6)
2. **Knapp BD et al.** “Metabolic rearrangement enables adaptation of microbial growth rate to temperature shifts.” *Nature Microbiology* 10, 185–201. DOI published online under **2024**, issue publication **2025**. DOI: [10.1038/s41564-024-01841-4](https://doi.org/10.1038/s41564-024-01841-4). (knapp2025metabolicrearrangementenables pages 1-2, knapp2025metabolicrearrangementenables pages 23-24, knapp2025metabolicrearrangementenables pages 4-5, knapp2025metabolicrearrangementenables pages 3-4)
3. **Hurtado-Bautista E et al.** “Thermal Plasticity and Evolutionary Constraints in Bacillus: Implications for Climate Change Adaptation.” *Biology* 13, 1088. **Published December 2024.** DOI: [10.3390/biology13121088](https://doi.org/10.3390/biology13121088). (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17)
4. **Lehmann M et al.** “Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.” *Frontiers in Microbiology* 14. **Published October 2023.** DOI: [10.3389/fmicb.2023.1265216](https://doi.org/10.3389/fmicb.2023.1265216). (lehmann2023adaptivelaboratoryevolution pages 1-2, lehmann2023adaptivelaboratoryevolution pages 6-7)
5. **Yang Q et al.** “Insight into the Cold Adaptation Mechanism of an Aerobic Denitrifying Bacterium: Bacillus simplex H-b.” *Applied and Environmental Microbiology* 89. **Published February 2023.** DOI: [10.1128/AEM.01928-22](https://doi.org/10.1128/AEM.01928-22). (yang2023insightintothe pages 1-2)
6. **Wu J et al.** “Effect of Temperature on the Inocula Preservation, Mesophilic Anaerobic Digestion Start-Up, and Microbial Community Dynamics.” *Agronomy* 14, 2991. **Published December 2024.** DOI: [10.3390/agronomy14122991](https://doi.org/10.3390/agronomy14122991). (wu2024effectoftemperature pages 1-2)
7. **Hua S et al.** “Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production.” *Microbial Cell Factories* 23. **Published November 2024.** DOI: [10.1186/s12934-024-02602-y](https://doi.org/10.1186/s12934-024-02602-y). (hua2024regulatorymechanismsof pages 1-3)
8. **Price PB, Sowers T.** “Temperature dependence of metabolic rates for microbial growth, maintenance, and survival.” *PNAS* 101, 4631–4636. **Published March 2004.** DOI: [10.1073/pnas.0400522101](https://doi.org/10.1073/pnas.0400522101). The reported growth:maintenance:survival metabolic-rate ratio was approximately 10⁶:10³:1, illustrating that metabolic activity or survival cannot be treated as equivalent to growth (price2004temperaturedependenceof pages 1-1).

## Final curation recommendation

Retain `METPO:1000445` as an assay-defined organismal phenotype. Expand the existing graph first with the well-supported **membrane-sensing and homeoviscous-adaptation chain**, a separate **temperature-dependent metabolic-rearrangement module**, and a taxon-qualified **c-di-AMP/potassium/osmolyte module**. Connect each module to “growth under temperature perturbation” with direct evidence. Connect it to the exact 30–34 °C optimum only through explicitly uncertain `contributes_to` edges until knockout, supplementation, lipid-manipulation, or evolution experiments demonstrate a statistically supported shift of the complete growth optimum into or out of this interval.

References

1. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

2. (hurtadobautista2024thermalplasticityand pages 1-2): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

3. (hurtadobautista2024thermalplasticityand pages 16-17): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

4. (yang2023insightintothe pages 1-2): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 19 citations and is from a peer-reviewed journal.

5. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

6. (knapp2025metabolicrearrangementenables pages 23-24): Benjamin D. Knapp, Lisa Willis, Carlos Gonzalez, Harsh Vashistha, Joanna Jammal-Touma, Mikhail Tikhonov, Jeffrey Ram, Hanna Salman, Josh E. Elias, and Kerwyn Casey Huang. Metabolic rearrangement enables adaptation of microbial growth rate to temperature shifts. Nature microbiology, 10:185-201, Dec 2025. URL: https://doi.org/10.1038/s41564-024-01841-4, doi:10.1038/s41564-024-01841-4. This article has 47 citations and is from a highest quality peer-reviewed journal.

7. (knapp2025metabolicrearrangementenables pages 1-2): Benjamin D. Knapp, Lisa Willis, Carlos Gonzalez, Harsh Vashistha, Joanna Jammal-Touma, Mikhail Tikhonov, Jeffrey Ram, Hanna Salman, Josh E. Elias, and Kerwyn Casey Huang. Metabolic rearrangement enables adaptation of microbial growth rate to temperature shifts. Nature microbiology, 10:185-201, Dec 2025. URL: https://doi.org/10.1038/s41564-024-01841-4, doi:10.1038/s41564-024-01841-4. This article has 47 citations and is from a highest quality peer-reviewed journal.

8. (knapp2025metabolicrearrangementenables pages 3-4): Benjamin D. Knapp, Lisa Willis, Carlos Gonzalez, Harsh Vashistha, Joanna Jammal-Touma, Mikhail Tikhonov, Jeffrey Ram, Hanna Salman, Josh E. Elias, and Kerwyn Casey Huang. Metabolic rearrangement enables adaptation of microbial growth rate to temperature shifts. Nature microbiology, 10:185-201, Dec 2025. URL: https://doi.org/10.1038/s41564-024-01841-4, doi:10.1038/s41564-024-01841-4. This article has 47 citations and is from a highest quality peer-reviewed journal.

9. (knapp2025metabolicrearrangementenables pages 4-5): Benjamin D. Knapp, Lisa Willis, Carlos Gonzalez, Harsh Vashistha, Joanna Jammal-Touma, Mikhail Tikhonov, Jeffrey Ram, Hanna Salman, Josh E. Elias, and Kerwyn Casey Huang. Metabolic rearrangement enables adaptation of microbial growth rate to temperature shifts. Nature microbiology, 10:185-201, Dec 2025. URL: https://doi.org/10.1038/s41564-024-01841-4, doi:10.1038/s41564-024-01841-4. This article has 47 citations and is from a highest quality peer-reviewed journal.

10. (wu2024effectoftemperature pages 1-2): Jingwei Wu, Huan Zhang, Ye Zhao, Xufeng Yuan, and Zongjun Cui. Effect of temperature on the inocula preservation, mesophilic anaerobic digestion start-up, and microbial community dynamics. Agronomy, 14:2991, Dec 2024. URL: https://doi.org/10.3390/agronomy14122991, doi:10.3390/agronomy14122991. This article has 11 citations and is from a peer-reviewed journal.

11. (lehmann2023adaptivelaboratoryevolution pages 6-7): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

12. (hua2024regulatorymechanismsof pages 1-3): Shengkai Hua, Yuqin Wang, Leyi Wang, Qinxuan Zhou, Zhitao Li, Peng Liu, Ke Wang, Yuanyuan Zhu, Dong Han, and Yongjian Yu. Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02602-y, doi:10.1186/s12934-024-02602-y. This article has 52 citations and is from a peer-reviewed journal.

13. (price2004temperaturedependenceof pages 1-1): P. Buford Price and Todd Sowers. Temperature dependence of metabolic rates for microbial growth, maintenance, and survival. Proceedings of the National Academy of Sciences of the United States of America, 101 13:4631-6, Mar 2004. URL: https://doi.org/10.1073/pnas.0400522101, doi:10.1073/pnas.0400522101. This article has 1034 citations and is from a highest quality peer-reviewed journal.