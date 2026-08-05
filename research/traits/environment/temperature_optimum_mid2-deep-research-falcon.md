---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:55:51.061540'
end_time: '2026-08-04T04:05:08.836009'
duration_seconds: 557.77
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum mid2
  trait_identifier: METPO:1000444
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ between approximately 27 and 30 \xB0C, characteristic of mesophilic physiology."
  parent_traits: METPO:1000304
  synonyms: Mesophilie, TO_27_to_30
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports a 27\u201330 \xB0C optimum as a typical\
    \ mesophile setpoint maintained by homoviscous membrane composition.)"
  causal_graph_summary: 'temperature_optimum_mid2_mesophile: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000444
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 27 and 30 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_27_to_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports a 27–30 °C optimum as a typical mesophile setpoint maintained by homoviscous membrane composition.)
- **Existing causal graph summary:** temperature_optimum_mid2_mesophile: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid2.yaml`.

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
- **Trait label:** temperature optimum mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000444
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 27 and 30 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_27_to_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports a 27–30 °C optimum as a typical mesophile setpoint maintained by homoviscous membrane composition.)
- **Existing causal graph summary:** temperature_optimum_mid2_mesophile: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid2.yaml`.

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


# Curation report: temperature optimum mid2

## Executive assessment

**Target:** `METPO:1000444` — **temperature optimum mid2**  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED  
**Parent:** `METPO:1000304`  
**Synonyms:** *Mesophilie*, `TO_27_to_30`

The trait should represent an **experimentally observed growth optimum**, not merely survival or growth somewhere between 27 and 30 °C. Operationally, an isolate qualifies when a temperature-response assay places its maximum specific growth rate, shortest doubling time, or—if rate is unavailable—maximum standardized biomass/yield at approximately 27–30 °C. The strongest general mechanistic explanation is not a single “mesophily gene,” but balance among membrane physical state, enzyme activity/stability, translation and RNA structure, and proteostasis. Current evidence most strongly supports a membrane-homeoviscosity subgraph; evidence that any individual mechanism specifically fixes an organism’s optimum within the narrow 27–30 °C interval remains limited.

## 1. Trait scope and boundaries

### Included phenotype

`METPO:1000444` denotes the location of the optimum of a microbial growth-versus-temperature response curve. Suitable observations include:

- maximum specific growth rate at 27–30 °C;
- minimum generation time in that interval;
- maximum biomass or colony-production endpoint there, provided medium, incubation duration, oxygen regime, pH, salinity, and inoculum are controlled;
- a reported optimum such as 28 °C or 30 °C, allowing the approximate interval specified by the ontology definition.

### Excluded or distinct observations

1. **Growth range:** growth at 28 °C does not establish an optimum at 28 °C.
2. **Thermotolerance or survival:** survival after heat or cold shock is not an optimum phenotype.
3. **Transient acclimation:** induction of desaturases, chaperones, or cold-shock proteins after a shift documents adaptation, not the location of the steady-state optimum.
4. **Enzyme optimum:** an isolated enzyme’s catalytic optimum is not automatically the organism’s growth optimum, although organismal growth temperature and mean enzyme optima can be strongly correlated.
5. **Host-associated performance:** infection or colonization at 26–29 °C is not equivalent to axenic growth optimum.
6. **Nearby classes:** organisms whose measured maxima fall below approximately 27 °C or above approximately 30 °C should map to the adjacent temperature-optimum class, even if broadly described as mesophiles.

The assay should ideally sample temperatures on both sides of the proposed maximum. A lone measurement at 28 or 30 °C cannot distinguish a true optimum from an assay endpoint or plateau.

## 2. Current mechanistic understanding

Cooling orders and thickens lipid bilayers. Bacteria commonly compensate by increasing unsaturated or branched-chain fatty acids, lowering lipid packing and restoring a fluid state needed for transport, respiration, division, and other membrane-associated processes. This is **homeoviscous adaptation**. In *Bacillus subtilis*, the canonical model is decreased fluidity/increased thickness → DesK kinase activity → DesR phosphorylation → `des` transcription → fatty-acid desaturation → restored fluidity. Importantly, membrane physical state rather than temperature alone can activate this circuit: increasing order at constant 37 °C also induces `des`. (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 1-2, mendoza2014temperaturesensingby pages 2-4)

Recent work qualifies that canonical model. A 2024 *B. subtilis* study found robust promoter activation after a mild 37→25 °C shift, but not after stronger shifts to 16 or 4 °C despite membrane rigidification. DesK partitioned into fluid domains, and `des`, `desK`, and `desR` deletions produced no detectable fluidity-adaptation phenotype under the tested conditions. Branched-chain fatty acids, reported as 80–96% of total fatty acids, appear to dominate fluidity control in this organism. Thus, the Des pathway is mechanistically real but should not be represented as the universal or sufficient determinant of mesophily. (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14)

Direct *Escherichia coli* perturbation evidence strengthens the broader membrane-to-growth link. Lowering unsaturated-fatty-acid synthesis through `fadR` disruption reduced membrane fluidity and caused growth defects around 25–30 °C in sensitized genetic backgrounds. Palmitoleic acid supplementation rescued growth, whereas saturated palmitic acid did not; increased temperature also rescued growth by increasing fluidity. The alarmone (p)ppGpp buffered cell division when fluidity fell. (singh2024(p)ppgppbufferscell pages 8-11)

At the systems level, a dataset of **21,498 nonredundant microbes** found a Pearson correlation of up to **0.89** between organismal growth temperature and mean enzyme optima. It identified **319 enzyme functions** whose occurrence changed with growth temperature and **eight enriched metabolic pathways**; the data could associate growth-temperature metadata with **43% of UniProt entries** at that time. These are valuable node-discovery statistics, but they are comparative correlations rather than causal evidence for the 27–30 °C class. (engqvist2018correlatingenzymeannotations pages 1-2)

## 3. Candidate causal-graph nodes

Identifiers below are limited to high-confidence, stable CURIEs. Label-only entries are deliberately retained where gene products are species-specific or an exact cross-reference was not verified.

### Trait and environmental/experimental nodes

| Candidate node | Suggested grounding | Role |
|---|---|---|
| temperature optimum mid2 | `METPO:1000444` | Target phenotype |
| parent temperature-optimum trait | `METPO:1000304` | Ontological parent |
| ambient/growth temperature | `ENVO:01000205` (air temperature) only when air is truly the medium; otherwise label-only “incubation temperature” is safer | Experimental/environmental input |
| 27–30 °C incubation | Label-only assay condition | Defining interval |
| decreased temperature / cold shift | Label-only process | Perturbation |
| elevated temperature / heat shift | Label-only process | Perturbation |
| specific growth rate | Label-only quantitative phenotype | Preferred assay readout |
| biomass yield / optical density | Label-only assay readout | Secondary evidence |

### Cellular structures, processes, and molecular functions

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| plasma membrane | `GO:0005886` | Core localization |
| membrane organization | `GO:0061024` | Broad process |
| response to temperature stimulus | `GO:0009266` | Broad response process |
| response to cold | `GO:0009409` | Use only for cold-shift evidence |
| response to heat | `GO:0009408` | Use only for heat-shift evidence |
| protein folding | `GO:0006457` | Proteostasis module |
| translation | `GO:0006412` | RNA/ribosome module |
| membrane fluidity | Label-only state | Central mechanistic state; do not force an inappropriate process CURIE |
| membrane order/rigidity | Label-only state | Increases during cooling |
| membrane thickness | Label-only state | DesK-proximal signal |
| lipid phase separation | Label-only process/state | Limits DesK sensing during severe rigidification |
| homeoviscous adaptation | Label-only process | Core adaptation module |

### Genes, proteins, and regulatory complexes

| Node | Organism/context | Function and recommendation |
|---|---|---|
| DesK | *B. subtilis* | Membrane histidine kinase/phosphatase; curate as taxon-specific |
| DesR | *B. subtilis* | Response regulator activated by phosphorylation |
| Des | *B. subtilis* | Δ5 acyl-lipid desaturase |
| DesK–DesR two-component system | *B. subtilis* | Canonical cold-responsive membrane circuit |
| FadR | *E. coli* | Fatty-acid-metabolism regulator; direct perturbation support |
| FabA | Gram-negative bacterial context | Enzyme contributing to unsaturated-fatty-acid synthesis; species-specific grounding should be added during YAML curation |
| RelA/SpoT and (p)ppGpp system | *E. coli* | Buffers division/growth when membrane fluidity is reduced |
| FtsQ/FtsA/FtsZ division module | *E. coli* | Downstream rescue module; accessory, not an optimum determinant |
| Acb1 | *Magnaporthe oryzae* | Acyl-CoA-binding protein; fungal and host-colonization-specific |
| CspL | *Bacillus coagulans* 2-6 | RNA chaperone; heterologous thermal-growth engineering evidence |
| DnaK/chaperone systems | Broad bacterial context | Plausible proteostasis module, but no retrieved evidence ties it specifically to 27–30 °C optimum |

### Chemicals and lipid classes

| Node | Suggested grounding | Role |
|---|---|---|
| unsaturated fatty acid | `CHEBI:27208` | Class-level fluidizing lipid component |
| saturated fatty acid | `CHEBI:26607` | Class-level comparator |
| palmitoleic acid (16:1) | `CHEBI:32372` | Direct rescue compound in *E. coli* experiments |
| palmitic acid (16:0) | `CHEBI:15756` | Saturated comparator that did not rescue the cited defect |
| cis-vaccenic acid (18:1) | `CHEBI:36021` | Temperature-responsive *E. coli* UFA; verify identifier during implementation if the project requires exact structure/isomer scope |
| branched-chain fatty acids | Label-only class | Dominant fluidity determinant in *B. subtilis* under some conditions |
| long-chain acyl-CoA | Label-only class | Acb1 cargo in the fungal module |
| (p)ppGpp | Label-only class or separate ppGpp/pppGpp chemical nodes | Alarmone-mediated growth buffering |

## 4. Candidate causal edges

Evidence rankings: **A**, direct perturbation/rescue; **B**, mechanistic experiments synthesized in an authoritative review; **C**, recent observational or context-specific perturbation; **D**, comparative correlation or extrapolation.

| # | Subject–predicate–object | Evidence | Reference and supporting snippet | Curation note |
|---:|---|---|---|---|
| 1 | decreased temperature → **increases** → membrane order/rigidity | B | “Lower temperatures cause membrane bilayers to undergo a reversible transition from fluid…to non-fluid (gel) state.” (mendoza2014temperaturesensingby pages 2-4) | Core physical edge; general but not specific to 27–30 °C. |
| 2 | decreased temperature → **increases** → membrane thickness | B/C | The 2024 study describes lower temperature as causing “membrane rigidification and thickening,” which activates DesK under mild shifts. (sidarta2024lipidphaseseparation pages 1-2) | Curate with DesK context; thickness can depend on lipid composition. |
| 3 | membrane order/thickness → **activates kinase state of** → DesK | B | DesK senses decreased fluidity; increasing membrane order at constant 37 °C activated the pathway, showing that physical state—not temperature per se—is the input. (mendoza2014temperaturesensingby pages 5-6) | Strong mechanistic edge, *B. subtilis*-specific. |
| 4 | active DesK → **phosphorylates** → DesR | B | “DesK undergoes autophosphorylation and transfers the phosphate to response regulator DesR.” (mendoza2014temperaturesensingby pages 5-6) | Suitable for immediate curation. |
| 5 | phosphorylated DesR → **activates transcription of** → `des` | B/C | DesR binds DNA and activates the gene encoding Δ5-desaturase; recent work confirms the Pdes regulatory architecture. (mendoza2014temperaturesensingby pages 5-6, sidarta2024lipidphaseseparation pages 1-2) | Suitable, taxon-specific. |
| 6 | Des → **increases** → fatty-acid unsaturation | B | The desaturase “introduces double bonds into saturated fatty acids.” (mendoza2014temperaturesensingby pages 5-6) | Suitable; represent substrate/product details only after checking the organism-specific reaction. |
| 7 | increased fatty-acid unsaturation → **increases** → membrane fluidity | A/B | UFAs disrupt ordered packing; in *E. coli*, palmitoleate rescued low-fluidity growth defects whereas palmitate did not. (singh2024(p)ppgppbufferscell pages 8-11, mendoza2014temperaturesensingby pages 2-4) | Core cross-taxon edge. |
| 8 | restored membrane fluidity → **supports** → growth and membrane-associated physiology | A/B | Homeoviscous adaptation “optimizes” physiological processes; *E. coli* genetic and chemical rescue directly links UFA-dependent fluidity to growth at 25–30 °C. (singh2024(p)ppgppbufferscell pages 8-11, mendoza2014temperaturesensingby pages 1-2) | Best edge connecting the membrane module toward the target phenotype. |
| 9 | FadR loss/inactivation → **decreases** → unsaturated-fatty-acid proportion | A | Inactivation of FadR reduced membrane UFA content in *E. coli*. (singh2024(p)ppgppbufferscell pages 8-11) | Curate only in the *E. coli* subgraph. |
| 10 | reduced UFA proportion → **decreases** → membrane fluidity | A | The perturbed strains exhibited reduced fluidity associated with reduced UFA content. (singh2024(p)ppgppbufferscell pages 8-11) | Direct and suitable. |
| 11 | palmitoleic acid supplementation → **rescues** → growth under low-fluidity conditions | A | 16:1 rescued ΔrelA ΔfadR at 25 °C and ΔrelA ΔspoT ΔfadR at 30 °C; 16:0 did not. (singh2024(p)ppgppbufferscell pages 8-11) | Particularly relevant because the assay includes 30 °C; still not proof of an intrinsic 27–30 °C optimum. |
| 12 | (p)ppGpp → **buffers** → cell division during decreased membrane fluidity | A | Growth and division became (p)ppGpp-dependent when UFA content was reduced; division-gene expression rescued filamentation/lysis. (singh2024(p)ppgppbufferscell pages 8-11) | Accessory edge; condition- and genotype-specific. |
| 13 | severe cold-induced lipid phase separation → **impairs** → DesK thickness sensing | C | DesK partitioned into fluid domains; 16 and 4 °C rigidified membranes without robust Pdes activation. (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14) | Important negative-regulation edge preventing an overly linear graph. |
| 14 | branched-chain fatty-acid content → **regulates** → *B. subtilis* membrane fluidity | C | Branched-chain fatty acids constituted 80–96% of total and were identified as the principal fluidity-control mechanism. (sidarta2024lipidphaseseparation pages 12-14) | Candidate node/edge; exact biosynthetic genes require additional primary evidence. |
| 15 | Acb1-mediated acyl-CoA handling → **maintains** → membrane fluidity at 22–26 °C | A/C | `ACB1` loss impaired fluidity and growth/trafficking at 22 and 26 °C but not 29 °C. (richter2024membranefluiditycontrol pages 16-18) | Fungal, temperature-conditional; curate only as a separate taxon-specific branch. |
| 16 | membrane fluidity → **supports** → vesicle trafficking and rice-cell colonization | A/C | In *M. oryzae*, defective fluidity was linked to impaired trafficking and abnormal biotrophic-interface organization at 26 °C, relieved at 29 °C. (richter2024membranefluiditycontrol pages 16-18) | Host-pathogenesis application, not an axenic optimum edge. |
| 17 | CspL RNA binding → **increases** → high-temperature microbial biomass | A | Heterologous CspL produced a 2.4-fold *E. coli* biomass increase at 45 °C, 2.6-fold in yeast at 36 °C, and 1.4-fold in *Pseudomonas putida*; an RNA-binding-defective variant failed to confer the benefit. (zhou2021acoldshock pages 1-2) | Useful engineering evidence but outside the target temperature interval; provisional only. |
| 18 | organism growth temperature → **correlates with** → mean enzyme optimum | D | Pearson correlation reached 0.89 across the large compiled dataset. (engqvist2018correlatingenzymeannotations pages 1-2) | Do not encode as a causal edge unless the graph schema explicitly permits correlations. |
| 19 | homeoviscous membrane state → **supports** → `METPO:1000444` | Inference | The membrane module supports efficient growth near mesophilic temperatures, including direct rescue at 30 °C. (singh2024(p)ppgppbufferscell pages 8-11, mendoza2014temperaturesensingby pages 1-2) | **Uncertain:** no source shows this module is sufficient to place the optimum specifically at 27–30 °C. Use a weak/inferred terminal edge if required. |

A practical priority summary is below.

| Proposed module | Strongest supported causal chain | Evidence class | Curation recommendation | Main caveat |
|---|---|---|---|---|
| Membrane homeoviscosity / DesK-DesR-Des | lower temperature → increased membrane order/thickness → DesK activation → DesR phosphorylation → des expression → fatty-acid desaturation/greater unsaturation → restored membrane fluidity (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 1-2, sidarta2024lipidphaseseparation pages 1-2, mendoza2014temperaturesensingby pages 4-5) | Review synthesis + mechanistic model with partial recent in vivo testing | **High priority core module** for a general mesophile graph; curate as a canonical membrane-adaptation mechanism | Strongly grounded in *Bacillus subtilis* cold-shift studies, not specifically in a 27–30 °C optimum; 2024 work shows des activation mainly under mild shocks and limited mutant phenotypes in vivo (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14) |
| *E. coli* FadR / UFA / (p)ppGpp growth buffering | reduced FadR-dependent UFA synthesis → decreased membrane fluidity → growth defect/cell-division dependence on (p)ppGpp; exogenous palmitoleic acid rescues growth, linking UFA composition causally to mesophilic growth performance (singh2024(p)ppgppbufferscell pages 8-11) | Direct perturbation | **High priority, but mark taxon-specific**; useful as direct evidence that fluidity control affects growth around 25–30 °C | Demonstrates buffering of impaired fluidity rather than defining the trait optimum itself; mechanism established in *E. coli* genetic backgrounds, not broadly across mesophiles (singh2024(p)ppgppbufferscell pages 8-11) |
| Fungal ACB1 / acyl-CoA / membrane fluidity | ACB1-mediated acyl-CoA handling → proper fatty-acid desaturation / membrane fluidity → normal growth and host colonization at 22–26 °C; deletion phenotype relieved at 29 °C (richter2024membranefluiditycontrol pages 16-18) | Direct perturbation | **Medium priority, uncertain generality**; curate only if fungal nodes are allowed and flagged as eukaryotic/host-interaction specific | Evidence is from *Magnaporthe oryzae* pathogenic development, not a generic microbial growth-optimum assay; temperatures bracket but do not define 27–30 °C optimum (richter2024membranefluiditycontrol pages 16-18) |
| RNA chaperone CspL / thermal growth support | heterologous CspL expression → broad RNA binding → improved biomass/growth at elevated temperature, including 2.4-fold biomass increase in *E. coli* at 45 °C (and growth benefits at normal temperatures) (zhou2021acoldshock pages 1-2) | Direct perturbation | **Low-to-medium priority**; candidate accessory module for RNA homeostasis under thermal stress | Evidence concerns supraoptimal/high-temperature tolerance engineering, not natural determination of a 27–30 °C optimum; likely too indirect for core TraitMech curation (zhou2021acoldshock pages 1-2) |
| Proteome / enzyme-temperature correlation | organism growth temperature ↔ mean enzyme optima (Pearson up to 0.89); temperature-associated gain/loss of 319 enzyme functions across 21,498 microbes suggests broad metabolic adaptation to temperature (engqvist2018correlatingenzymeannotations pages 1-2) | Correlation | **Background-only / contextual**; useful for rationale and node discovery, not for direct causal edges | Large-scale comparative correlation lacks direct perturbation and does not identify a specific causal path for the 27–30 °C class (engqvist2018correlatingenzymeannotations pages 1-2) |


*Table: This table ranks candidate mechanistic modules for curating the temperature optimum mid2 trait, emphasizing which pathways have direct causal support versus broader contextual evidence. It is useful for deciding which edges are suitable for immediate TraitMech inclusion and which should remain provisional.*

## 5. Recommended minimal YAML expansion

The safest immediate expansion of the existing 9-node/8-edge graph is a **taxon-qualified membrane module**, rather than a universal gene list:

1. decreased incubation temperature → increased membrane order/thickness;
2. increased order/thickness → DesK kinase activation (*B. subtilis* context);
3. DesK → phosphorylated DesR;
4. phosphorylated DesR → increased `des` transcription;
5. Des → increased fatty-acid unsaturation;
6. increased fatty-acid unsaturation → increased/restored membrane fluidity;
7. restored membrane fluidity → supported membrane-associated physiology and growth;
8. lipid phase separation → impaired DesK sensing under severe rigidification;
9. reduced FadR-dependent UFA synthesis → reduced fluidity → impaired growth (*E. coli* context);
10. palmitoleate → rescued growth near 25–30 °C in the sensitized *E. coli* backgrounds.

The terminal connection to `METPO:1000444` should carry an **inferred/uncertain** qualifier unless a source directly compares an organism with a documented 27–30 °C optimum against a mechanistic mutant and demonstrates a shifted optimum.

## 6. Recent developments, applications, and expert interpretation

### 2024 developments

- **DesK model refinement:** Sidarta and colleagues showed that the sensor behaves well under mild cooling but can fail during severe rigidification because phase separation spatially separates it from rigid domains. Their deletion experiments also found no obvious temperature-growth phenotype, arguing against treating DesK–DesR–Des as the sole homeoviscous controller. Published June 2024. (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14)
- **Growth buffering by (p)ppGpp:** Singh and Harinarayanan connected reduced UFA content to division failure and showed genetic and lipid rescue near the target interval. Published October 2024. (singh2024(p)ppgppbufferscell pages 8-11)
- **Thermal range of fungal infection:** Richter and colleagues showed that an acyl-CoA-binding protein controls membrane fluidity, trafficking, and rice colonization at 22–26 °C, while its requirement was relieved at 29 °C. Published November 2024. This demonstrates how membrane composition can set a biologically consequential thermal range, though not necessarily an axenic OGT. (richter2024membranefluiditycontrol pages 16-18)

### Real-world applications

1. **Industrial fermentation:** RNA-chaperone engineering with CspL increased biomass at elevated process temperatures—2.4-fold in *E. coli* at 45 °C and 2.6-fold in *S. cerevisiae* at 36 °C—illustrating how thermal-growth mechanisms can be engineered to reduce cooling demands or contamination risk. This is an application of thermal tolerance, not direct evidence for `METPO:1000444`. (zhou2021acoldshock pages 1-2)
2. **Plant disease forecasting:** The *M. oryzae* result indicates that pathogen membrane-fluidity machinery can govern whether host colonization succeeds at agriculturally relevant temperatures. Such mechanisms may improve temperature-aware rice-blast models or identify temperature-conditional fungicide targets. (richter2024membranefluiditycontrol pages 16-18)
3. **Antimicrobial design:** Membrane thickness/fluidity affects antimicrobial activity and resistance, motivating sensors and compounds that disrupt homeoviscous adaptation. However, the 2024 DesK study cautions that simple reporter assumptions may fail during phase separation. (sidarta2024lipidphaseseparation pages 1-2)
4. **Genome-to-phenotype prediction:** The 21,498-organism dataset and 319 temperature-associated enzyme functions provide a basis for predicting OGT from genomes, but such predictions require phylogenetic controls and experimental validation. (engqvist2018correlatingenzymeannotations pages 1-2)

### Expert synthesis

The authoritative membrane-sensing review treats homeoviscous adaptation as a broadly conserved solution: as temperature falls, microbes increase UFAs or analogous lipids to preserve a mostly fluid bilayer and optimize cellular functions. (mendoza2014temperaturesensingby pages 1-2, mendoza2014temperaturesensingby pages 2-4) The more recent experimental literature supports the principle but emphasizes **redundancy, context, and nonlinear sensing**: different taxa use UFAs, branched-chain fatty acids, acyl-CoA handling, or other lipid systems; a canonical sensor may operate only over a limited perturbation range. (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14, richter2024membranefluiditycontrol pages 16-18) Therefore, a TraitMech graph should represent `METPO:1000444` as an emergent phenotype supported by several modules, not as the output of one universal pathway.

## 7. Claims not ready for TraitMech curation

- **Do not assert that increased UFAs cause an OGT of exactly 27–30 °C.** Evidence shows they preserve fluidity and growth, but not that they uniquely set this narrow optimum.
- **Do not equate mesophily with `METPO:1000444`.** Mesophily is broader than the ontology’s 27–30 °C bin.
- **Do not add DesK, DesR, or Des as universal microbial nodes.** They describe a *Bacillus* implementation; other bacteria, archaea, and fungi use different systems.
- **Do not make Des essential for cold adaptation.** The 2024 deletion study found no detectable phenotype under its tested conditions, and branched-chain fatty acids dominated *B. subtilis* membrane composition. (sidarta2024lipidphaseseparation pages 12-14)
- **Do not curate CspL as a natural determinant of this trait.** Its strongest evidence is heterologous engineering at 36–45 °C. (zhou2021acoldshock pages 1-2)
- **Do not convert the enzyme-temperature correlation into causation.** The 0.89 correlation and 319 associated functions are powerful comparative evidence but cannot establish directionality. (engqvist2018correlatingenzymeannotations pages 1-2)
- **Do not treat host colonization as growth optimum.** The *M. oryzae* ACB1 phenotype includes host membranes, immunity, and developmental state. (richter2024membranefluiditycontrol pages 16-18)
- **Do not assign exact CURIEs from gene symbols alone.** UniProt accessions must be selected for the exact strain/protein used in each study.
- **Do not use an air-temperature ENVO term for liquid culture incubation.** Retain “incubation temperature” as label-only unless an appropriate environmental ontology term is verified.

## 8. DOI-first bibliography

1. Sidarta M, et al. **Lipid phase separation impairs membrane thickness sensing by the *Bacillus subtilis* sensor kinase DesK.** *Microbiology Spectrum*. Published June 2024. DOI: [10.1128/spectrum.03925-23](https://doi.org/10.1128/spectrum.03925-23). (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14)
2. Singh V, Harinarayanan R. **(p)ppGpp buffers cell division when membrane fluidity decreases in *Escherichia coli*.** *Molecular Microbiology* 122:847–865. Published October 2024. DOI: [10.1111/mmi.15323](https://doi.org/10.1111/mmi.15323). (singh2024(p)ppgppbufferscell pages 8-11)
3. Richter M, et al. **Membrane fluidity control by the *Magnaporthe oryzae* acyl-CoA binding protein sets the thermal range for host rice cell colonization.** *PLOS Pathogens* 20:e1012738. Published November 2024. DOI: [10.1371/journal.ppat.1012738](https://doi.org/10.1371/journal.ppat.1012738). (richter2024membranefluiditycontrol pages 16-18)
4. de Mendoza D. **Temperature sensing by membranes.** *Annual Review of Microbiology* 68:101–116. Published September 2014. DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 1-2, mendoza2014temperaturesensingby pages 2-4, mendoza2014temperaturesensingby pages 4-5)
5. Zhou Z, et al. **A cold shock protein promotes high-temperature microbial growth through binding to diverse RNA species.** *Cell Discovery* 7. Published March 2021. DOI: [10.1038/s41421-021-00246-5](https://doi.org/10.1038/s41421-021-00246-5). (zhou2021acoldshock pages 1-2)
6. Engqvist MKM. **Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures.** *BMC Microbiology* 18. Published November 2018. DOI: [10.1186/s12866-018-1320-7](https://doi.org/10.1186/s12866-018-1320-7). Dataset DOI: [10.5281/zenodo.1175608](https://doi.org/10.5281/zenodo.1175608). (engqvist2018correlatingenzymeannotations pages 1-2)

## Curation conclusion

The most defensible graph for `METPO:1000444` is a layered model in which **27–30 °C incubation permits a membrane physical state compatible with transport, energy transduction, division, translation, and enzyme function**, while homeoviscous regulation preserves that state during modest deviations. The DesK–DesR–Des and FadR/UFA/(p)ppGpp branches provide concrete mechanistic implementations. Nevertheless, their connection to the exact 27–30 °C optimum should remain qualified as inferred until a documented mid2 organism is subjected to targeted perturbation and its complete growth-temperature curve demonstrably shifts.

References

1. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

2. (mendoza2014temperaturesensingby pages 1-2): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

3. (mendoza2014temperaturesensingby pages 2-4): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

4. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 6 citations and is from a domain leading peer-reviewed journal.

5. (sidarta2024lipidphaseseparation pages 12-14): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 6 citations and is from a domain leading peer-reviewed journal.

6. (singh2024(p)ppgppbufferscell pages 8-11): Vani Singh and Rajendran Harinarayanan. (p)<scp>ppgpp</scp> buffers cell division when membrane fluidity decreases in <i>escherichia coli</i>. Molecular Microbiology, 122:847-865, Oct 2024. URL: https://doi.org/10.1111/mmi.15323, doi:10.1111/mmi.15323. This article has 6 citations and is from a domain leading peer-reviewed journal.

7. (engqvist2018correlatingenzymeannotations pages 1-2): Martin K. M. Engqvist. Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures. BMC Microbiology, Nov 2018. URL: https://doi.org/10.1186/s12866-018-1320-7, doi:10.1186/s12866-018-1320-7. This article has 103 citations and is from a peer-reviewed journal.

8. (richter2024membranefluiditycontrol pages 16-18): Michael Richter, Lauren M. Segal, Raquel O. Rocha, Nisha Rokaya, Aline R. de Queiroz, Wayne R. Riekhof, Rebecca L. Roston, and Richard A. Wilson. Membrane fluidity control by the magnaporthe oryzae acyl-coa binding protein sets the thermal range for host rice cell colonization. PLOS Pathogens, 20:e1012738, Nov 2024. URL: https://doi.org/10.1371/journal.ppat.1012738, doi:10.1371/journal.ppat.1012738. This article has 7 citations and is from a highest quality peer-reviewed journal.

9. (zhou2021acoldshock pages 1-2): Zikang Zhou, Hongzhi Tang, Weiwei Wang, Lige Zhang, Fei Su, Yuanting Wu, Linquan Bai, Sicong Li, Yuhui Sun, Fei Tao, and Ping Xu. A cold shock protein promotes high-temperature microbial growth through binding to diverse rna species. Cell Discovery, Mar 2021. URL: https://doi.org/10.1038/s41421-021-00246-5, doi:10.1038/s41421-021-00246-5. This article has 45 citations and is from a peer-reviewed journal.

10. (mendoza2014temperaturesensingby pages 4-5): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.