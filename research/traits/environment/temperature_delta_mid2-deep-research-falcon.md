---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:38:11.045933'
end_time: '2026-08-04T03:47:29.002791'
duration_seconds: 557.96
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature delta mid2
  trait_identifier: METPO:1000486
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_delta_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature delta phenotype with a growth-supporting temperature\
    \ breadth of approximately 20\u201330 \xB0C, characteristic of organisms with\
    \ broad thermal-tolerance breadth."
  parent_traits: METPO:1000303
  synonyms: Td_20_30
  evidence_summary: 'DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty
    acids (Membrane-adaptation review supports broad homoviscous remodeling capacity
    as the basis of eurythermal physiology.)'
  causal_graph_summary: 'temperature_delta_mid2_broad_breadth: 10 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000486
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 20–30 °C, characteristic of organisms with broad thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_20_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports broad homoviscous remodeling capacity as the basis of eurythermal physiology.)
- **Existing causal graph summary:** temperature_delta_mid2_broad_breadth: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid2.yaml`.

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
- **Trait label:** temperature delta mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000486
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 20–30 °C, characteristic of organisms with broad thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_20_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports broad homoviscous remodeling capacity as the basis of eurythermal physiology.)
- **Existing causal graph summary:** temperature_delta_mid2_broad_breadth: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_mid2.yaml`.

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


# Curation report: temperature delta mid2

## 1. Scope and operational definition

**Target:** “METPO:1000486” — *temperature delta mid2* (synonym **Td_20_30**), an environmental-class phenotype defined as a growth-supporting temperature breadth of approximately **20–30 °C**.

For curation, the phenotype should be operationalized as **ΔT = Tmax − Tmin**, where Tmin and Tmax are the lowest and highest temperatures supporting reproducible population growth under a specified medium, atmosphere, pH, salinity, incubation time, and detection threshold. It is therefore a property of the complete thermal performance curve, not simply the optimum temperature.

Important distinctions are:

- **Not temperature optimum:** organisms with identical ΔT can have very different Tmin, Topt, and Tmax.
- **Not acute thermotolerance:** survival after minutes at 55–59 °C does not establish sustained growth at those temperatures.
- **Not exclusively cold or heat response:** a 20–30 °C interval may arise from low-end adaptation, high-end adaptation, or coordinated performance at both ends.
- **Not ecological occurrence breadth:** metagenomic detection across habitats does not demonstrate growth throughout a 20–30 °C laboratory interval.
- **Boundary handling:** values near 20 or 30 °C require explicit endpoint and rounding rules. Growth/no-growth observations should not be mixed with cardinal temperatures inferred by curve fitting unless the assay method is recorded.

A useful direct analogue is *Psychrobacter arcticus* 273-4, studied from −6 to 22 °C (28 °C breadth). By contrast, *Exiguobacterium sibiricum* 255-15 grows from approximately −5 to 39 °C (44 °C breadth) and is mechanistically informative but lies outside this trait’s numerical bin (bergholz2009psychrobacterarcticus2734 pages 1-1, rodrigues2008architectureofthermal pages 1-2).

## 2. Current mechanistic understanding

Broad thermal growth is best represented as an **emergent systems phenotype**. The strongest generic mechanism is membrane homeoviscous adaptation: cooling orders the bilayer, membrane sensors activate lipid remodeling, and incorporation of unsaturated or analogous disorder-promoting fatty acids restores membrane function. In *Bacillus subtilis*, a shift from 37 to 20 °C activates the DesK/DesR system; experiments changing anteiso-branched-chain fatty-acid abundance at constant temperature show that membrane order, rather than temperature alone, controls `des` transcription (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 1-2).

Direct broad-range studies additionally support temperature-dependent isozyme exchange, RNA remodeling, stringent-response control, macromolecular preservation, metabolic flexibility, osmoprotection, and extensive transcriptional compensation. In *P. arcticus*, knockouts of `csdA`, `relA`, and `dac2` impaired low-temperature growth, while `dac1` was more important at an intermediate temperature, demonstrating division of labor across the growth interval (bergholz2009psychrobacterarcticus2734 pages 1-1, bergholz2009psychrobacterarcticus2734 pages 10-11).

## 3. Candidate nodes grouped by type

### Trait and experimental nodes

- **temperature delta mid2** — “METPO:1000486”
- minimum growth temperature; maximum growth temperature; optimum growth temperature — label-only pending verified ontology mapping
- environmental temperature; temperature downshift; temperature upshift
- sustained population growth; maximum specific growth rate; thermal performance curve
- medium composition, salinity/osmolarity, pH, oxygen availability, incubation duration, and growth-detection threshold — essential assay covariates
- acute heat-shock survival — retain as a separate comparator phenotype

### Cellular components and processes

- membrane — **GO:0016020**
- fatty-acid biosynthetic process — **GO:0006633**
- lipid metabolic process — **GO:0006629**
- response to cold — **GO:0009409**
- response to heat — **GO:0009408**
- protein folding/proteostasis — **GO:0006457**
- membrane fluidity/homeoviscous adaptation — label-only candidates
- transcriptomic buffering; central-metabolic robustness; isozyme exchange; potassium homeostasis; osmoadaptation — label-only candidates

### Genes, proteins, and complexes

- **DesK/DesR** two-component membrane-fluidity sensor and regulator; `des` fatty-acid desaturase
- cold-growth candidates: `csdA`, `relA`, `dac1`, `dac2`, Psyc_0943
- proteostasis machinery: DnaJ, DnaK, ClpB, HtpG, ClpX, Hsp33, GroEL/GroES
- c-di-AMP synthesis/regulation candidates: DisA, CdaA, CdaR, CdaS
- Gene symbols should remain **label-only or taxon-scoped** until organism-specific UniProt/NCBI Gene accessions are verified.

### Chemicals and metabolites

- 3′,5′-cyclic di-AMP — **CHEBI:57604**
- potassium ion — **CHEBI:29103**
- glycine betaine — **CHEBI:17684**
- L-proline — **CHEBI:17203**
- phosphoenolpyruvate — **CHEBI:44897**
- unsaturated fatty acids, anteiso-branched-chain fatty acids, teichoic acids, glycerol, glucose, methionine, and tryptophan — use class-level or compound-specific identifiers only after exact chemical identity is established

### Taxon-context nodes

- *Escherichia coli* — **NCBITaxon:562**
- *Bacillus subtilis* — **NCBITaxon:1423**
- *Legionella pneumophila* — **NCBITaxon:446**
- *Psychrobacter arcticus* — **NCBITaxon:259536**
- *Exiguobacterium sibiricum* 255-15 — **NCBITaxon:262543**

## 4. Candidate causal edges

| # | Subject — predicate — object | Reference and supporting snippet | Evidence assessment and curation note |
|---|---|---|---|
| 1 | decreasing environmental temperature — **decreases** — membrane fluidity | de Mendoza 2014: cooling drives the bilayer toward an ordered/gel state (mendoza2014temperaturesensingby pages 1-2). | **High confidence, generic.** Curate as the initiating physical edge. |
| 2 | decreased membrane fluidity — **activates** — DesK/DesR signaling | In *B. subtilis*, reduced anteiso-BCFA content increased membrane order and activated `des` transcription even at constant 37 °C (mendoza2014temperaturesensingby pages 5-6). | **High confidence, taxon-instantiated.** The generic sensor edge is broadly plausible, but DesK/DesR is not universal. |
| 3 | activated DesR — **increases expression of** — `des` | A 37→20 °C shift induced UFA synthesis through DesK/DesR; phosphorylated DesR activates `des` (mendoza2014temperaturesensingby pages 5-6). | **High confidence in B. subtilis.** Curate with taxon context. |
| 4 | increased unsaturated-fatty-acid biosynthesis — **restores** — membrane fluidity/function at low temperature | “When membrane fluidity is restored through UFA synthesis, `des` transcription is shut off”; increased UFAs optimize membrane function after cooling (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 1-2). | **High confidence.** Strongest core mechanism connecting environmental temperature to broad physiological performance. |
| 5 | `csdA` RNA helicase — **positively affects** — low-temperature growth | In *P. arcticus*, a `csdA` knockout “grew slower at low temperature” (bergholz2009psychrobacterarcticus2734 pages 1-1). | **High confidence but taxon-specific.** Direct perturbation/growth evidence; do not claim it alone creates a 20–30 °C breadth. |
| 6 | `relA` stringent-response controller — **positively affects** — subzero growth | `relA` knockout decreased growth rates below 0 °C (bergholz2009psychrobacterarcticus2734 pages 10-11). | **High confidence but taxon-specific.** Curate as low-end support. |
| 7 | `dac2` carboxypeptidase — **positively affects** — low-temperature growth | `dac2` mutants grew more slowly at low temperature; `dac1` was important at 17 °C, supporting temperature-dependent isozyme exchange (bergholz2009psychrobacterarcticus2734 pages 1-1). | **High confidence in P. arcticus.** Preserve temperature and strain context. |
| 8 | temperature variation within the growth range — **induces** — transcriptomic reprogramming | In the 2023 marine-bacterium study, hundreds of genes changed between 0 and 15 °C despite overlapping central-metabolite profiles (riccardi2023metabolicrobustnessto pages 10-12, riccardi2023metabolicrobustnessto pages 1-2). | **Moderate confidence, taxon-specific.** This is a regulatory association, not a single-gene causal perturbation. |
| 9 | transcriptomic reprogramming — **buffers** — central metabolism across temperatures | Authors interpret extensive expression changes with stable metabolite profiles as “transcriptomic buffering” (riccardi2023metabolicrobustnessto pages 1-2). | **Moderate confidence.** Curate as a module-level edge with “inferred from multi-omics” qualifier. |
| 10 | low-temperature growth — **increases** — phosphoenolpyruvate level and fatty-acid-biosynthesis flux | At 0 °C, PEP increased, TCA flux was redirected toward PEP, and fatty-acid biosynthesis flux increased; about 90% of 51 metabolites remained positively correlated between temperatures (riccardi2023metabolicrobustnessto pages 10-12). | **Moderate, direction carefully stated.** Data establish temperature→metabolic-state effects; the reverse claim that PEP causes breadth remains unproven. |
| 11 | c-di-AMP — **regulates** — potassium homeostasis/osmotic balance | The 2024 *Bacillus* study associated convergent mutations in c-di-AMP synthesis genes with thermal adaptation and describes c-di-AMP control of potassium transport (hurtadobautista2024thermalplasticityand pages 16-17, hurtadobautista2024thermalplasticityand pages 1-2). | **Moderate/uncertain.** Curate regulation, but not a direct c-di-AMP→mid2-breadth edge without allele reconstruction or complementation. |
| 12 | potassium/osmotic homeostasis — **increases** — upper-temperature tolerance | High-osmolarity/potassium effects were associated with elevated upper growth-temperature limits and lethal-temperature survival (hurtadobautista2024thermalplasticityand pages 16-17). | **Uncertain and Bacillus-specific.** Growth-limit and survival outcomes are mixed. |
| 13 | glycine betaine or proline — **protects against** — heat stress | Compatible solutes are described as heat protectants in *B. subtilis* (hurtadobautista2024thermalplasticityand pages 16-17). | **Moderate for protection; weak for breadth.** Curate only with an uncertainty qualifier and a heat-tolerance object, not directly to “METPO:1000486.” |
| 14 | chloramphenicol resistance — **decreases** — thermal niche breadth | Resistant *E. coli* had disproportionately greater growth costs at 32 and 42 °C than at 37 °C; resistance×temperature interaction: F₁,₉₇₄=13.8, p<0.001 (herren2022decreasedthermalniche pages 3-4, herren2022decreasedthermalniche pages 1-1). | **High confidence trade-off, context-specific.** Useful negative modifier, but not an intrinsic mechanism defining the trait. |
| 15 | DnaJ/DnaK/ClpB/HtpG/ClpX variants — **alter** — transient heat-shock survival | Evolved *L. pneumophila* survived short exposure to 59 °C and carried mutations in these chaperone/protease systems; DnaK alleles reduced population loss at 55 °C (liang2023developmentofheatshock pages 1-2, liang2023developmentofheatshock pages 7-9, liang2023developmentofheatshock pages 14-16). | **Strong acute-survival evidence, not growth breadth. Do not curate as a direct trait edge.** |

The curation priorities are summarized below.

| module | candidate edge (subject—predicate—object) | evidence class | curation recommendation |
|---|---|---|---|
| Membrane homeoviscous adaptation | decreased environmental temperature—decreases—membrane fluidity; decreased membrane fluidity—activates—increased unsaturated-fatty-acid biosynthesis; increased unsaturated fatty acids—restores—membrane fluidity/function (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 1-2) | High; mechanistic review with experimental support in Bacillus membrane thermosensing | Curate as core generic breadth mechanism |
| Cold-growth genes | csdA—positively affects—low-temperature growth; relA—positively affects—subzero growth; dac2—positively affects—low-temperature growth (bergholz2009psychrobacterarcticus2734 pages 1-1, bergholz2009psychrobacterarcticus2734 pages 10-11) | High for Psychrobacter; knockout/growth-rate evidence | Curate as taxon-specific positive edges, flagged Psychrobacter-specific |
| Transcriptomic/metabolic buffering | temperature shift within growth range—induces—transcriptomic buffering; transcriptomic buffering—maintains—central metabolic robustness; increased phosphoenolpyruvate/fatty-acid flux—supports—growth at low temperature (riccardi2023metabolicrobustnessto pages 10-12, riccardi2023metabolicrobustnessto pages 1-2) | Moderate; direct multi-omics evidence in one cold-adapted marine bacterium | Curate cautiously as taxon-specific/module-level edges; avoid overgeneralizing PEP as universal node |
| Osmotic/ion homeostasis | c-di-AMP—regulates—potassium homeostasis; potassium/compatible solutes (glycine betaine, proline)—increase—high-temperature tolerance (hurtadobautista2024thermalplasticityand pages 16-17) | Moderate/uncertain; Bacillus-focused, linked to upper-temperature limit and survival | Curate only as tentative breadth contributors with uncertainty notes |
| Heat-shock chaperone/protease mutations | dnaJ/dnaK/clpB/htpG/clpX mutations—increase—transient heat-shock survival (liang2023developmentofheatshock pages 1-2, liang2023developmentofheatshock pages 7-9, liang2023developmentofheatshock pages 14-16) | Strong for acute survival; not growth-range evidence | Do not curate as direct breadth edges for METPO:1000486; keep as contextual non-breadth evidence |
| Trade-off context | chloramphenicol resistance—narrows—thermal niche breadth / reduces growth at novel temperatures (herren2022decreasedthermalniche pages 3-4, herren2022decreasedthermalniche pages 1-1, herren2022decreasedthermalniche pages 4-5) | High for trade-off context in E. coli | Do not curate as intrinsic mechanism of breadth; useful as warning/context node only |


*Table: This table prioritizes candidate mechanisms and edges for curating temperature delta mid2, separating broadly supported breadth mechanisms from taxon-specific, acute-survival, and trade-off evidence. It helps decide what should enter the causal graph now versus what should remain contextual or uncertain.*

## 5. Recent developments and quantitative findings

### 2023: metabolic buffering rather than metabolome replacement

Riccardi and colleagues integrated transcriptomics, metabolomics, and genome-scale modeling for a cold-adapted marine bacterium grown at 0 and 15 °C. Approximately **90% of 51 measured metabolites**—34 intracellular and 17 extracellular—were positively correlated across temperatures, whereas **more than 600 genes** were differentially expressed. Increased PEP and fatty-acid synthesis flux at 0 °C support a model in which regulatory and flux reallocation buffers central metabolism rather than producing wholly different metabolic states (riccardi2023metabolicrobustnessto pages 10-12, riccardi2023metabolicrobustnessto pages 1-2).

### 2024: limited evolvability and c-di-AMP convergence in Bacillus

Experimental evolution of *B. subtilis* and *B. cereus* found convergent changes involving c-di-AMP synthesis genes, implicating potassium/osmotic regulation in thermal adaptation. Nevertheless, adaptation was constrained: only one *B. subtilis* strain achieved a reported **4 °C** increase above its natural range, and the study reports failure of the tested groups to grow sustainably at only about **3 °C above** their natural ranges. This argues against treating broad thermal breadth as a readily acquired single-locus trait (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 2-3).

### 2023: heat-survival evolution has operational consequences but is a different phenotype

After **70 selection cycles**, *L. pneumophila* populations became insensitive to 55 °C treatment and survived short exposures to 59 °C. Mutations occurred repeatedly in DnaJ/DnaK/ClpB, HtpG, and ClpX, and heat-shock genes remained more highly expressed during cooler freshwater incubation. These findings are relevant to superheat-and-flush control of hot-water systems, but the assay measured transient survival rather than sustained high-temperature growth (liang2023developmentofheatshock pages 1-2, liang2023developmentofheatshock pages 7-9).

### 2022: thermal breadth reveals hidden resistance costs

In 24 *E. coli* lineages evolved through 14 chloramphenicol concentrations—**336 populations**—growth was measured at 32, 37, and 42 °C. Increasing resistance strongly reduced growth overall (F₁,₉₇₄=988.2, p<0.001), with significantly larger costs at the novel temperatures. In competition, sensitive strains grew about **1.3-fold larger** against highly resistant strains at 32/37 °C but **threefold larger** at 42 °C. This demonstrates why a standard single-temperature assay can miss a major fitness cost (herren2022decreasedthermalniche pages 3-4, herren2022decreasedthermalniche pages 4-5, herren2022decreasedthermalniche pages 3-3).

## 6. Applications and expert interpretation

- **Strain selection and bioprocess design:** thermal-performance curves, rather than single-temperature growth rates, can identify robust production, food, or environmental strains. Membrane composition and metabolic buffering are candidate biomarkers, but must be validated in the production medium.
- **Cold-environment biotechnology:** RNA helicases, stringent-response control, isozyme exchange, and flexible fatty-acid metabolism may support low-temperature biocatalysis. The strongest gene-level evidence remains organism-specific (bergholz2009psychrobacterarcticus2734 pages 1-1, riccardi2023metabolicrobustnessto pages 10-12).
- **Water-system pathogen control:** incomplete heat disinfection may select improved acute survival in *L. pneumophila*. This supports validated eradication protocols, but does not imply expansion of the organism’s sustained growth range (liang2023developmentofheatshock pages 1-2, liang2023developmentofheatshock pages 14-16).
- **Antimicrobial-resistance ecology:** resistance costs may emerge principally away from the historical assay temperature; thermal breadth can therefore be a more sensitive fitness phenotype than growth at 37 °C alone (herren2022decreasedthermalniche pages 3-4, herren2022decreasedthermalniche pages 1-1).
- **Climate-response prediction:** the 2024 *Bacillus* work indicates strong genetic-background effects and constrained adaptation. Recent expert analysis therefore favors polygenic, systems-level models over universal “thermotolerance genes” (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 2-3).

## 7. Recommended minimal graph architecture

For `temperature_delta_mid2.yaml`, the defensible core is:

1. temperature decrease → reduced membrane fluidity;
2. reduced membrane fluidity → membrane-fluidity sensing;
3. membrane-fluidity sensing → increased unsaturated/branch-equivalent fatty-acid synthesis;
4. lipid remodeling → restored membrane physiological function;
5. restored membrane function → supports growth at the lower thermal boundary;
6. temperature-dependent regulatory reprogramming → central-metabolic buffering;
7. central-metabolic buffering → supports growth across temperature variation;
8. cold-growth effectors (`csdA`, `relA`, `dac2`) → support low-temperature growth, each explicitly scoped to *P. arcticus*;
9. optional uncertain branch: c-di-AMP → potassium/osmotic homeostasis → upper-temperature tolerance;
10. trait assertion only when observed ΔT falls within the defined 20–30 °C interval.

This architecture avoids equating isolated stress resistance with the complete breadth phenotype.

## 8. Claims not ready for TraitMech curation

1. **Do not assert that any single gene causes “METPO:1000486.”** Existing evidence generally concerns one thermal boundary or one taxon.
2. **Do not connect Legionella chaperone mutations directly to growth breadth.** The phenotype was 15–30-minute heat survival, not replication at 55–59 °C (liang2023developmentofheatshock pages 7-9, liang2023developmentofheatshock pages 14-16).
3. **Do not reverse omics associations.** Increased PEP or fatty-acid flux at 0 °C does not prove that experimentally increasing PEP expands ΔT (riccardi2023metabolicrobustnessto pages 10-12).
4. **Do not universalize DesK/DesR.** Homeoviscous adaptation is broad, but the sensing machinery and lipid solution differ among bacteria and especially archaea.
5. **Do not treat c-di-AMP mutations as mechanistically resolved.** Multiple concurrent mutations and incomplete intergenic coverage prevented definitive allele-to-phenotype attribution (hurtadobautista2024thermalplasticityand pages 16-17).
6. **Do not use *E. sibiricum* as a positive instance of mid2.** Its reported −5 to 39 °C range exceeds the 20–30 °C class, although its mechanisms remain useful comparative evidence (rodrigues2008architectureofthermal pages 1-2).
7. **Do not omit assay context.** Nutrient source, osmolarity, oxygen, pH, inoculum, incubation time, and growth threshold can move apparent Tmin and Tmax.
8. **Do not conflate maximum growth rate with breadth.** The 2022 resistance study explicitly shows these are separable fitness dimensions (herren2022decreasedthermalniche pages 7-8, herren2022decreasedthermalniche pages 1-2).

## 9. DOI-first bibliography

1. Hurtado-Bautista E, et al. **Thermal Plasticity and Evolutionary Constraints in Bacillus: Implications for Climate Change Adaptation.** *Biology*. Published December 2024. DOI: [10.3390/biology13121088](https://doi.org/10.3390/biology13121088) (hurtadobautista2024thermalplasticityand pages 1-2).
2. Riccardi C, et al. **Metabolic Robustness to Growth Temperature of a Cold-Adapted Marine Bacterium.** *mSystems*. Published April 2023. DOI: [10.1128/msystems.01124-22](https://doi.org/10.1128/msystems.01124-22) (riccardi2023metabolicrobustnessto pages 10-12, riccardi2023metabolicrobustnessto pages 1-2).
3. Liang J, Cameron G, Faucher SP. **Development of heat-shock resistance in Legionella pneumophila modeled by experimental evolution.** *Applied and Environmental Microbiology*. Published September 2023. DOI: [10.1128/aem.00666-23](https://doi.org/10.1128/aem.00666-23) (liang2023developmentofheatshock pages 1-2).
4. Herren CM, Baym M. **Decreased thermal niche breadth as a trade-off of antibiotic resistance.** *ISME Journal*. Published April 2022. DOI: [10.1038/s41396-022-01235-6](https://doi.org/10.1038/s41396-022-01235-6) (herren2022decreasedthermalniche pages 3-4).
5. de Mendoza D. **Temperature sensing by membranes.** *Annual Review of Microbiology*. Published September 2014. DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612) (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 1-2).
6. Bergholz PW, Bakermans C, Tiedje JM. **Psychrobacter arcticus 273-4 Uses Resource Efficiency and Molecular Motion Adaptations for Subzero Temperature Growth.** *Journal of Bacteriology*. Published April 2009. DOI: [10.1128/JB.01377-08](https://doi.org/10.1128/JB.01377-08) (bergholz2009psychrobacterarcticus2734 pages 1-1).
7. Rodrigues DF, et al. **Architecture of thermal adaptation in an Exiguobacterium sibiricum strain isolated from 3 million year old permafrost: a genome and transcriptome approach.** *BMC Genomics*. Published November 18, 2008. DOI: [10.1186/1471-2164-9-547](https://doi.org/10.1186/1471-2164-9-547) (rodrigues2008architectureofthermal pages 1-2, rodrigues2008architectureofthermal pages 6-8).

References

1. (bergholz2009psychrobacterarcticus2734 pages 1-1): Peter W. Bergholz, Corien Bakermans, and James M. Tiedje. <i>psychrobacter arcticus</i> 273-4 uses resource efficiency and molecular motion adaptations for subzero temperature growth. Apr 2009. URL: https://doi.org/10.1128/jb.01377-08, doi:10.1128/jb.01377-08. This article has 126 citations and is from a peer-reviewed journal.

2. (rodrigues2008architectureofthermal pages 1-2): Debora F Rodrigues, Natalia Ivanova, Zhili He, Marianne Huebner, Jizhong Zhou, and James M Tiedje. Architecture of thermal adaptation in an exiguobacterium sibiricum strain isolated from 3 million year old permafrost: a genome and transcriptome approach. BMC Genomics, 9:547-547, Nov 2008. URL: https://doi.org/10.1186/1471-2164-9-547, doi:10.1186/1471-2164-9-547. This article has 183 citations and is from a peer-reviewed journal.

3. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

4. (mendoza2014temperaturesensingby pages 1-2): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

5. (bergholz2009psychrobacterarcticus2734 pages 10-11): Peter W. Bergholz, Corien Bakermans, and James M. Tiedje. <i>psychrobacter arcticus</i> 273-4 uses resource efficiency and molecular motion adaptations for subzero temperature growth. Apr 2009. URL: https://doi.org/10.1128/jb.01377-08, doi:10.1128/jb.01377-08. This article has 126 citations and is from a peer-reviewed journal.

6. (riccardi2023metabolicrobustnessto pages 10-12): Christopher Riccardi, Marzia Calvanese, Veronica Ghini, Tania Alonso-Vásquez, Elena Perrin, Paola Turano, Giorgio Giurato, Alessandro Weisz, Ermenegilda Parrilli, Maria Luisa Tutino, and Marco Fondi. Metabolic robustness to growth temperature of a cold- adapted marine bacterium. mSystems, Apr 2023. URL: https://doi.org/10.1128/msystems.01124-22, doi:10.1128/msystems.01124-22. This article has 21 citations and is from a peer-reviewed journal.

7. (riccardi2023metabolicrobustnessto pages 1-2): Christopher Riccardi, Marzia Calvanese, Veronica Ghini, Tania Alonso-Vásquez, Elena Perrin, Paola Turano, Giorgio Giurato, Alessandro Weisz, Ermenegilda Parrilli, Maria Luisa Tutino, and Marco Fondi. Metabolic robustness to growth temperature of a cold- adapted marine bacterium. mSystems, Apr 2023. URL: https://doi.org/10.1128/msystems.01124-22, doi:10.1128/msystems.01124-22. This article has 21 citations and is from a peer-reviewed journal.

8. (hurtadobautista2024thermalplasticityand pages 16-17): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

9. (hurtadobautista2024thermalplasticityand pages 1-2): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

10. (herren2022decreasedthermalniche pages 3-4): Cristina M Herren and Michael Baym. Decreased thermal niche breadth as a trade-off of antibiotic resistance. The ISME Journal, 16:1843-1852, Apr 2022. URL: https://doi.org/10.1038/s41396-022-01235-6, doi:10.1038/s41396-022-01235-6. This article has 46 citations.

11. (herren2022decreasedthermalniche pages 1-1): Cristina M Herren and Michael Baym. Decreased thermal niche breadth as a trade-off of antibiotic resistance. The ISME Journal, 16:1843-1852, Apr 2022. URL: https://doi.org/10.1038/s41396-022-01235-6, doi:10.1038/s41396-022-01235-6. This article has 46 citations.

12. (liang2023developmentofheatshock pages 1-2): Jeffrey Liang, Gillian Cameron, and Sébastien P. Faucher. Development of heat-shock resistance in <i>legionella pneumophila</i> modeled by experimental evolution. Applied and Environmental Microbiology, Sep 2023. URL: https://doi.org/10.1128/aem.00666-23, doi:10.1128/aem.00666-23. This article has 19 citations and is from a peer-reviewed journal.

13. (liang2023developmentofheatshock pages 7-9): Jeffrey Liang, Gillian Cameron, and Sébastien P. Faucher. Development of heat-shock resistance in <i>legionella pneumophila</i> modeled by experimental evolution. Applied and Environmental Microbiology, Sep 2023. URL: https://doi.org/10.1128/aem.00666-23, doi:10.1128/aem.00666-23. This article has 19 citations and is from a peer-reviewed journal.

14. (liang2023developmentofheatshock pages 14-16): Jeffrey Liang, Gillian Cameron, and Sébastien P. Faucher. Development of heat-shock resistance in <i>legionella pneumophila</i> modeled by experimental evolution. Applied and Environmental Microbiology, Sep 2023. URL: https://doi.org/10.1128/aem.00666-23, doi:10.1128/aem.00666-23. This article has 19 citations and is from a peer-reviewed journal.

15. (herren2022decreasedthermalniche pages 4-5): Cristina M Herren and Michael Baym. Decreased thermal niche breadth as a trade-off of antibiotic resistance. The ISME Journal, 16:1843-1852, Apr 2022. URL: https://doi.org/10.1038/s41396-022-01235-6, doi:10.1038/s41396-022-01235-6. This article has 46 citations.

16. (hurtadobautista2024thermalplasticityand pages 2-3): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

17. (herren2022decreasedthermalniche pages 3-3): Cristina M Herren and Michael Baym. Decreased thermal niche breadth as a trade-off of antibiotic resistance. The ISME Journal, 16:1843-1852, Apr 2022. URL: https://doi.org/10.1038/s41396-022-01235-6, doi:10.1038/s41396-022-01235-6. This article has 46 citations.

18. (herren2022decreasedthermalniche pages 7-8): Cristina M Herren and Michael Baym. Decreased thermal niche breadth as a trade-off of antibiotic resistance. The ISME Journal, 16:1843-1852, Apr 2022. URL: https://doi.org/10.1038/s41396-022-01235-6, doi:10.1038/s41396-022-01235-6. This article has 46 citations.

19. (herren2022decreasedthermalniche pages 1-2): Cristina M Herren and Michael Baym. Decreased thermal niche breadth as a trade-off of antibiotic resistance. The ISME Journal, 16:1843-1852, Apr 2022. URL: https://doi.org/10.1038/s41396-022-01235-6, doi:10.1038/s41396-022-01235-6. This article has 46 citations.

20. (rodrigues2008architectureofthermal pages 6-8): Debora F Rodrigues, Natalia Ivanova, Zhili He, Marianne Huebner, Jizhong Zhou, and James M Tiedje. Architecture of thermal adaptation in an exiguobacterium sibiricum strain isolated from 3 million year old permafrost: a genome and transcriptome approach. BMC Genomics, 9:547-547, Nov 2008. URL: https://doi.org/10.1186/1471-2164-9-547, doi:10.1186/1471-2164-9-547. This article has 183 citations and is from a peer-reviewed journal.