---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:47:35.032779'
end_time: '2026-08-04T03:59:16.918259'
duration_seconds: 701.89
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum mid1
  trait_identifier: METPO:1000443
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ between approximately 22 and 27 \xB0C, characteristic of mesophilic physiology."
  parent_traits: METPO:1000304
  synonyms: Mesophilie, TO_22_to_27
  evidence_summary: 'DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty
    acids (Membrane-adaptation review supports moderate-temperature optima matched
    by homoviscous lipid composition as the mesophile setpoint.)'
  causal_graph_summary: 'temperature_optimum_mid1_lower_mesophile: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000443
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 22 and 27 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_22_to_27
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports moderate-temperature optima matched by homoviscous lipid composition as the mesophile setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid1_lower_mesophile: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid1.yaml`.

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
- **Trait label:** temperature optimum mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000443
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 22 and 27 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_22_to_27
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports moderate-temperature optima matched by homoviscous lipid composition as the mesophile setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid1_lower_mesophile: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid1.yaml`.

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


# Curation report: microbial **temperature optimum mid1**

## Executive assessment

**Target trait:** `METPO:1000443`  
**Label:** temperature optimum mid1  
**Parent:** `METPO:1000304`  
**Definition supplied for curation:** best-growth ambient temperature approximately **22–27 °C**, characteristic of lower-mesophilic physiology.

The trait should be modeled primarily as an **assay-derived cardinal-temperature phenotype**, not as a single molecular mechanism. A strain qualifies when its measured specific growth rate, under explicitly stated medium, atmosphere, pH, salinity, and measurement protocol, reaches its maximum in the 22–27 °C interval. The strongest mechanistic graph presently supportable is a generic chain in which temperature affects enzyme kinetics, proteostasis, and membrane physical state; lipid remodeling then preserves a growth-compatible membrane state. However, the literature retrieved does **not** directly establish that any one lipid, gene, or pathway is sufficient to set an organism’s optimum specifically at 22–27 °C.

The most important recent advance is a 2024 quantitative *E. coli* study showing that temperature-dependent competition between FabI and FabB, counteracted by FabR transcriptional feedback, rapidly changes membrane acyl composition. This provides strong causal edges for homeoviscous adaptation, but *E. coli* itself has an optimum near 37 °C, so these edges are mechanistic support rather than direct evidence for `METPO:1000443`. (hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 3-4)

## 1. Trait scope and boundaries

### Operational meaning

`METPO:1000443` should represent the temperature at which a microorganism has its **maximum specific growth rate** or another explicitly accepted best-growth measure. Cardinal-temperature terminology separates minimum growth temperature, optimum growth temperature (`T_OPT`), and maximum growth temperature. A direct experimental-evolution study illustrates the appropriate assay logic: growth curves were measured over a temperature series, exponential rates were compared, and the temperature with the highest rate was assigned as `T_OPT`. (lehmann2023adaptivelaboratoryevolution pages 1-2, lehmann2023adaptivelaboratoryevolution pages 3-4)

Recommended annotation requirements are:

1. Record the tested temperature series and confirm that it brackets 22–27 °C.
2. Prefer maximum specific growth rate, μmax, derived from exponential growth. If yield, endpoint OD, colony size, or substrate turnover is used instead, identify the result as assay-specific.
3. Record medium composition, carbon and energy source, electron acceptor, pH, salinity/water activity, atmosphere, pressure, inoculum history, and acclimation time.
4. Where the temperature series is coarse, annotate an interval rather than an exact optimum.
5. Treat strain-level evidence as primary; do not infer the trait for every member of a species or genus.

### Boundary cases

- **Not growth range:** growth at 25 °C does not imply that 25 °C is optimal.
- **Not minimum or maximum temperature:** `T_MIN` and `T_MAX` delimit growth, whereas `T_OPT` identifies the peak of the reaction norm.
- **Not survival or tolerance:** persistence after cold or heat exposure is not equivalent to active growth, much less maximal growth.
- **Not acclimation:** lipid remodeling after a temperature shift can improve performance without changing the inherited optimum.
- **Not broad mesophily:** one recent study uses 25–45 °C as a broad mesophilic `T_OPT` category; `METPO:1000443` is a much narrower lower-mesophile bin. (lehmann2023adaptivelaboratoryevolution pages 3-4)
- **Not enzyme-activity optimum:** the temperature optimum of an isolated enzyme, such as EF-1A ligand binding, may correlate with organismal optimum but is not equivalent to measured whole-cell growth.
- **Conditional phenotype:** a strain’s apparent optimum can change with nutrients, oxygen, pH, or salinity. The *Thermoanaerobacter kivui* study explicitly tested medium dependence after detecting a shifted optimum. (lehmann2023adaptivelaboratoryevolution pages 3-4)

## 2. Current mechanistic understanding

The most defensible model is a **multi-constraint optimum**. At lower temperatures, biochemical reaction rates decline and membranes become more ordered. At higher temperatures, membranes become excessively fluid and proteins increasingly unfold. The observed optimum is therefore the temperature at which integrated flux through metabolism, translation, membrane transport, energy conservation, cell division, and proteostasis produces the highest net growth rate.

Membrane homeoviscous adaptation is the strongest experimentally resolved module. Cooling drives lipid bilayers toward a more ordered or gel-like state. Bacteria commonly compensate by increasing unsaturated or branched-chain fatty acids, thereby restoring membrane fluidity and the function of membrane-associated processes. (mendoza2014temperaturesensingby pages 1-2, gohrbandt2022lowmembranefluidity pages 1-2)

In *E. coli*, temperature also acts directly on fatty-acid pathway flux. FabA interconverts branch-point intermediates; FabI directs substrate toward saturated fatty acids, whereas FabB initiates the unsaturated branch and FabF can elongate C16:1-ACP to C18:1-ACP. PlsB and PlsC then incorporate acyl chains into phosphatidic acid and downstream phospholipids. FabR provides transcriptional feedback responsive to acyl-ACP pools. This pathway topology and its temperature-dependent output were directly visualized across 12–42 °C. (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic media 44b7d377, hoogerland2024atemperaturesensitivemetabolic media 68fb0e6e)

The second major module is proteostasis. A coarse-grained model calibrated with quantitative *E. coli* proteomics predicts Arrhenius-like growth-rate increases over a moderate interval, but at temperature extremes protein unfolding diverts proteome resources to chaperones at the expense of ribosomal and metabolic sectors. The paper notes experimental observations of misfolding and chaperone responses, but the allocation-to-growth edges remain primarily model-supported. (mairet2021optimalproteomeallocation pages 1-2)

## 3. Candidate nodes grouped by type

### Trait and environmental nodes

- **temperature optimum mid1** — `METPO:1000443`
- **parent temperature-optimum phenotype** — `METPO:1000304`
- ambient/growth temperature — label-only pending verified ENVO or assay ontology mapping
- cooling; warming; cold shock; heat shock — label-only experimental-factor nodes
- temperature interval 22–27 °C — literal/measurement node, not an ontology class
- specific growth rate; maximum specific growth rate; growth arrest; biomass yield; lag duration — label-only phenotype/measurement nodes

### Pathways and metabolic modules

- homeoviscous adaptation — label-only; verify GO grounding before import
- type II fatty-acid biosynthesis/FASII — pathway label; verify KEGG or MetaCyc identifier during implementation
- saturated fatty-acid synthesis branch
- unsaturated fatty-acid synthesis branch
- glycerophospholipid biosynthesis
- protein folding/refolding and heat-shock response
- proteome allocation to metabolic, ribosomal, housekeeping, and chaperone sectors

### Genes, proteins, and enzymes

The following are strong *E. coli*-specific candidates but should be linked to organism-specific gene or UniProt records only after strain/proteome verification:

- **FabA** — 3-hydroxydecanoyl-ACP dehydratase/isomerase; produces the cis-unsaturated branch-point substrate
- **FabB** — 3-oxoacyl-ACP synthase I; initiates/extends the unsaturated branch
- **FabI** — enoyl-ACP reductase; competes for branch-point substrate and supports saturated-chain synthesis
- **FabF** — 3-oxoacyl-ACP synthase II; elongates C16:1-ACP toward C18:1-ACP
- **FabR** — transcriptional repressor responsive to saturated/unsaturated acyl-ACP ligands
- **FadR** — transcriptional regulator of fatty-acid metabolism
- **PlsB** — glycerol-3-phosphate acyltransferase
- **PlsC** — 1-acylglycerol-3-phosphate acyltransferase
- acyl carrier protein/ACP
- molecular chaperones and proteases — generic nodes unless a particular system is experimentally tested

A 2023 evolved *T. kivui* line carried a **FabG P216L** substitution, a **SigH G28V** substitution, and other regulatory mutations, but causality for the shifted optimum was not established. These should remain candidate or provenance nodes, not causal determinants. (lehmann2023adaptivelaboratoryevolution pages 6-7)

### Chemicals and metabolites

Use verified ChEBI records at implementation; do not assign identifiers from memory.

- saturated fatty acids
- unsaturated fatty acids
- branched-chain fatty acids
- palmitoyl-ACP/C16:0-ACP
- palmitoleoyl-ACP/C16:1-ACP
- oleoyl-ACP/C18:1-ACP
- glycerol 3-phosphate
- lysophosphatidic acid
- phosphatidic acid
- phosphatidylethanolamine
- phosphatidylglycerol
- plasmalogens
- triclosan — FabI inhibitor in the 2024 pathway perturbation
- cerulenin — FabB inhibitor in that study

### Cellular structures, functions, and processes

- cytoplasmic membrane/lipid bilayer — verify GO cellular-component mapping
- outer membrane and lipooligosaccharide — relevant only for Gram-negative taxon-specific subgraphs
- membrane fluidity/viscosity
- membrane lipid phase separation
- membrane-protein lateral diffusion and segregation
- membrane potential maintenance
- cytokinesis
- cell-envelope expansion
- chromosome replication and segregation
- protein unfolding, refolding, and degradation
- ribosome-mediated translation and metabolic enzyme activity

### Taxon/context nodes

- *Escherichia coli* — `NCBITaxon:562`
- *Bacillus subtilis* — `NCBITaxon:1423`
- *Acinetobacter baumannii* — `NCBITaxon:470`
- *Thermoanaerobacter kivui* — verify current NCBITaxon record before import

## 4. Candidate causal edges

The compact prioritization table below summarizes the strongest graph skeleton.

| subject | predicate | object | evidence class/taxon | DOI | confidence/curation decision |
|---|---|---|---|---|---|
| decreased environmental temperature (cooling) | causes | membrane rigidification / reduced membrane fluidity | Review-level, bacteria broadly; homeoviscous adaptation framework (mendoza2014temperaturesensingby pages 1-2, gohrbandt2022lowmembranefluidity pages 1-2) | 10.1146/annurev-micro-091313-103612 | **High, curate as general mechanism** for temperature-optimum traits, but not specific to 22–27 °C |
| cooling (37→13 °C shock) | decreases flux through | FabI saturated-fatty-acid branch | Direct experiment, *Escherichia coli* (hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 3-4) | 10.1038/s41467-024-53677-5 | **High, curate with taxon-specific note** |
| reduced FabI activity relative to FabB | reallocates flux toward | unsaturated-fatty-acid branch | Direct experiment + model, *E. coli* (hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 3-4) | 10.1038/s41467-024-53677-5 | **High, curate with taxon-specific note** |
| FabB | positively regulates / catalyzes | unsaturated fatty acid synthesis | Direct experiment, *E. coli* overexpression and pathway analysis (hoogerland2024atemperaturesensitivemetabolic pages 3-4) | 10.1038/s41467-024-53677-5 | **High, curate** |
| unsaturated fatty acids and branched-chain fatty acids | increase / maintain | membrane fluidity | Review + experimental framing in bacteria broadly; direct consequences studied in *E. coli* and *Bacillus subtilis* (gohrbandt2022lowmembranefluidity pages 1-2) | 10.15252/embj.2021109800 | **High, curate as broad mechanism** |
| low membrane fluidity | triggers | lipid phase separation | Direct experiment, *E. coli* and *B. subtilis* (gohrbandt2022lowmembranefluidity pages 10-11, gohrbandt2022lowmembranefluidity pages 12-14) | 10.15252/embj.2021109800 | **High, curate** |
| low membrane fluidity | interferes with | cytokinesis, envelope expansion, chromosome replication/segregation, membrane-potential maintenance | Direct experiment, *E. coli* and *B. subtilis* (gohrbandt2022lowmembranefluidity pages 1-2) | 10.15252/embj.2021109800 | **High, curate** |
| low membrane fluidity | causes | growth arrest / minimal fluidity threshold for growth | Direct experiment, *E. coli* and *B. subtilis* (gohrbandt2022lowmembranefluidity pages 1-2, gohrbandt2022lowmembranefluidity pages 10-11) | 10.15252/embj.2021109800 | **High, curate** |
| extreme temperatures | increase | protein unfolding / denaturation | Coarse-grained model with literature grounding, calibrated to *E. coli* proteomics (mairet2021optimalproteomeallocation pages 1-2) | 10.1038/s41540-021-00172-y | **Moderate, model-supported; curate cautiously** |
| protein unfolding at extreme temperatures | increases allocation to | chaperone-mediated stress responses | Coarse-grained model, *E. coli*-calibrated (mairet2021optimalproteomeallocation pages 1-2) | 10.1038/s41540-021-00172-y | **Moderate, model-only; mark uncertain** |
| increased chaperone allocation | reduces allocation to | metabolic and ribosomal growth functions | Coarse-grained model, *E. coli*-calibrated (mairet2021optimalproteomeallocation pages 1-2) | 10.1038/s41540-021-00172-y | **Moderate, model-only; mark uncertain** |
| adaptive laboratory evolution at suboptimal temperature | shifts | optimal growth temperature (TOPT) downward | Direct evolution experiment, *Thermoanaerobacter kivui*; 66→60 °C shift after ~180 generations (lehmann2023adaptivelaboratoryevolution pages 3-4, lehmann2023adaptivelaboratoryevolution pages 1-2) | 10.3389/fmicb.2023.1265216 | **Moderate, retain as general support only**; **do not curate as direct mechanism for METPO:1000443** |
| increased unsaturated GPL species at lower temperature | supports acclimation to | lower-temperature growth/survival | Direct lipidomics, *Acinetobacter baumannii* at 37 vs 18 °C (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 2-4) | 10.1128/spectrum.00757-24 | **Moderate, curate only as taxon-specific supporting edge** |


*Table: This table summarizes the strongest curation-ready causal edges relevant to METPO:1000443, emphasizing membrane homeoviscous adaptation, flux control in fatty-acid synthesis, and growth-limiting consequences of low membrane fluidity. It also flags which edges are taxon-specific or model-only so they can be curated cautiously.*

The following expanded table supplies source snippets and curation notes.

| Proposed subject–predicate–object triple | Reference | Supporting snippet | Interpretation and curation status |
|---|---|---|---|
| decreased growth temperature → **decreases** → membrane fluidity | 10.1146/annurev-micro-091313-103612 | “Cooling…triggers membrane rigidification through a reversible phase transition from fluid…to rigid…state.” | Foundational review synthesis. **Curate as a broad physical mechanism**, not as proof of a 22–27 °C optimum. (mendoza2014temperaturesensingby pages 1-2) |
| decreased growth temperature → **increases proportion of** → unsaturated fatty acids | 10.1146/annurev-micro-091313-103612 | Bacteria incorporate “proportionally more unsaturated fatty acids…as growth temperature decreases.” | Strong review-level consensus. The supplied existing evidence is valid, but this is acclimation rather than direct optimum-setting evidence. (mendoza2014temperaturesensingby pages 1-2) |
| unsaturated or branched-chain fatty acids → **promote/maintain** → membrane fluidity | 10.15252/embj.2021109800 | Organisms alter “fluidity-promoting unsaturated fatty acids (UFA) or branched chain fatty acids (BCFA)” versus fluidity-reducing SFA. | Broad mechanism supported by experiments and prior literature. **Curate**, but preserve taxon context because organisms use different lipid strategies. (gohrbandt2022lowmembranefluidity pages 1-2) |
| cold shock, 37→13 °C → **decreases** → C16:0-ACP abundance | 10.1038/s41467-024-53677-5 | “Within 5 min…C16:0 ACP decreased approximately 5-fold, while C18:1 ACP remained stable.” | Direct, quantitative *E. coli* experiment. **High-confidence taxon-specific edge.** It demonstrates rapid remodeling, not a changed `T_OPT`. (hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| cooling → **reduces activity of** → FabI | 10.1038/s41467-024-53677-5 | “FabI exhibits approximately 2-fold less activity at 27 °C” than at 37 °C. | Direct in-vitro enzyme evidence aligned with cellular perturbations. **Curate for *E. coli***; especially relevant because 27 °C touches the upper trait boundary, but it does not show optimum at 27 °C. (hoogerland2024atemperaturesensitivemetabolic pages 5-6) |
| reduced FabI activity relative to FabB → **redirects fatty-acid flux toward** → unsaturated branch | 10.1038/s41467-024-53677-5 | “Cold temperatures restrict saturated fatty acid synthesis by decreasing…reduction by FabI relative to…elongation by FabB.” | Direct perturbation plus pathway modeling. Triclosan phenocopied cold shock and cerulenin phenocopied heat shock. **High-confidence *E. coli* edge.** (hoogerland2024atemperaturesensitivemetabolic pages 5-6) |
| FabB abundance/activity → **increases** → unsaturated fatty-acid production | 10.1038/s41467-024-53677-5 | “FabB overexpression increases unsaturated acyl chains.” | Direct overexpression evidence. **Curate taxon-specifically.** (hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| FabR–unsaturated acyl-ACP complex → **represses** → fabB expression | 10.1038/s41467-024-53677-5 | The model places FabB “under control of a modelled FabR, which represses FabB when bound to the unsaturated precursor.” | Regulatory mechanism is experimentally informed, but this excerpt combines established biochemistry with model implementation. **Curate with evidence qualifier.** (hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| FabI/FabB temperature-sensitive valve + FabR feedback → **accelerates restoration of** → temperature-adapted phospholipid composition | 10.1038/s41467-024-53677-5 | The system adapts membrane composition “within a single cell cycle”; steady-state phospholipids were reached within about 8 h, close to one 7-h doubling at 12 °C. | Strong integrated mechanism with time courses, inhibitors, knockouts, overexpression, and modeling. **Curate as an *E. coli* module.** (hoogerland2024atemperaturesensitivemetabolic pages 1-2, hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| increased temperature → **increases** → saturated sn-1 phospholipid fraction | 10.1038/s41467-024-53677-5 | “C16:0 ACP and 16:0 sn-1 phospholipids increase with temperature, while C18:1…decrease.” | Direct LC–MS across five temperatures from 12–42 °C; pathway figure corroborates this relationship. **Curate taxon-specifically.** (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic media 68fb0e6e) |
| low membrane fluidity → **causes** → lipid phase separation | 10.15252/embj.2021109800 | “Very low membrane fluidity…trigger[s] large-scale lipid phase separation and protein segregation.” | Direct experiments in *E. coli* and *B. subtilis*. Approximate phase-separation compositions were ~80% SFA in manipulated *E. coli* versus ~50% wild type and ~20% SFA in manipulated *B. subtilis* versus 5–7% wild type. **High confidence.** (gohrbandt2022lowmembranefluidity pages 1-2, gohrbandt2022lowmembranefluidity pages 12-14) |
| low membrane fluidity → **interferes with** → cytokinesis, envelope expansion, chromosome replication/segregation, and membrane-potential maintenance | 10.15252/embj.2021109800 | “Inadequate in vivo membrane fluidity interferes with…cytokinesis, envelope expansion, chromosome replication/segregation and maintenance of membrane potential.” | Direct living-cell evidence in two model bacteria. **Curate as downstream consequences**, preferably as separate edges. (gohrbandt2022lowmembranefluidity pages 1-2) |
| low membrane fluidity → **causes** → growth arrest | 10.15252/embj.2021109800 | “Too low membrane fluidity results in growth arrest in both organisms.” | Strong direct evidence. This is the best bridge from membrane state to growth, although it establishes a lower fluidity threshold rather than the exact optimum. (gohrbandt2022lowmembranefluidity pages 1-2) |
| lower temperature, 18 versus 37 °C → **increases** → palmitoleic acid/C16:1 in membrane lipids | 10.1128/spectrum.00757-24 | Five of six *A. baumannii* strains increased C16:1 at 18 °C; ABVal2 instead showed a distinctive C18:1-rich response. | Direct lipidomics across six clinical strains. **Curate only with strain/taxon qualifiers** because substantial within-species heterogeneity was observed. (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 2-4) |
| temperature extremes → **increase** → protein unfolding | 10.1038/s41540-021-00172-y | Model includes “temperature-sensitive protein unfolding and chaperone-assisted (re)folding”; heat stress accumulates misfolded proteins. | Mechanistically plausible and literature-grounded, but the graph edge in this source is partly model-based. **Mark uncertain/model-supported.** (mairet2021optimalproteomeallocation pages 1-2) |
| protein unfolding → **increases allocation to** → chaperone-mediated stress response | 10.1038/s41540-021-00172-y | “At extreme temperatures resources are diverted away from growth to chaperone-mediated stress responses.” | *E. coli*-calibrated optimization model. **Do not present as direct proof for `METPO:1000443`.** (mairet2021optimalproteomeallocation pages 1-2) |
| increased chaperone allocation → **decreases allocation to** → metabolic and ribosomal sectors | 10.1038/s41540-021-00172-y | Chaperone content increases “at the expense of metabolic and ribosomal proteins.” | Model-supported resource trade-off. **Candidate uncertain edge.** (mairet2021optimalproteomeallocation pages 1-2) |
| repeated growth at suboptimal temperature → **can shift** → inherited `T_OPT` downward | 10.3389/fmicb.2023.1265216 | After ~180 generations/67 transfers at 45 °C, *T. kivui* shifted from 66 to 60 °C. | Direct evidence that `T_OPT` is evolvable. The evolved strain grew at 0.523 versus 0.391 h⁻¹ at 60 °C and 0.360 versus 0.297 h⁻¹ at 55 °C, but not faster at 45 °C. **Context only; not a direct edge for 22–27 °C.** (lehmann2023adaptivelaboratoryevolution pages 3-4) |
| FabG P216L / increased plasmalogens → **associated with** → reduced `T_OPT` | 10.3389/fmicb.2023.1265216 | The evolved line carried a FabG P216L mutation and had increased plasmalogens. | Association within one evolved lineage; 67 SNPs were present. **Do not curate as causal without reconstruction or complementation.** (lehmann2023adaptivelaboratoryevolution pages 6-7) |

## 5. Recommended minimal graph for YAML curation

A conservative graph should emphasize only well-supported general mechanisms:

1. **decreased growth temperature** → decreases → **membrane fluidity**
2. **decreased membrane fluidity** → activates/elicits → **homeoviscous adaptation**
3. **homeoviscous adaptation** → increases → **fluidity-promoting membrane lipids**
4. **fluidity-promoting membrane lipids** → maintain → **growth-compatible membrane fluidity**
5. **growth-compatible membrane fluidity** → enables → **membrane-associated cellular processes**
6. **membrane-associated cellular processes** → contribute to → **specific growth rate**
7. **specific growth rate reaches maximum at 22–27 °C** → realizes → `METPO:1000443`

An optional *E. coli*-specific subgraph may add:

- cooling → decreases FabI activity relative to FabB
- reduced FabI/FabB activity ratio → redirects flux to unsaturated fatty-acid synthesis
- FabB → increases unsaturated acyl-ACP production
- FabR–unsaturated acyl-ACP → represses fabB
- PlsB/PlsC substrate pools → determine phospholipid acyl composition
- increased unsaturated phospholipid fraction → supports temperature-adapted membrane fluidity

The final edge from these mechanisms to `METPO:1000443` should be expressed as **contributes_to**, not **causes**, unless a study directly shifts the organismal optimum into or out of 22–27 °C through a defined perturbation.

## 6. Recent developments, applications, and expert analysis

### Recent research

- **Quantitative control architecture (2024):** Hoogerland et al. integrated targeted proteomics, acyl-ACP and phospholipid LC–MS, temperature shocks, enzyme inhibitors, overexpression, knockout strains, and differential-equation modeling. The principal advance is that homeoviscous adaptation is not merely slow transcriptional remodeling: a temperature-sensitive metabolic valve acts immediately, while FabR feedback corrects overshoot. (hoogerland2024atemperaturesensitivemetabolic pages 6-7, hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 3-4)
- **Strain-level heterogeneity (2024):** six *A. baumannii* clinical strains differed in their 18 °C lipid response. Five increased C16:1, whereas ABVal2 displayed a distinct baseline and response, including candidate desaturases. This argues against universal gene-to-trait rules even within one species. (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 2-4)
- **Experimental evolution of `T_OPT` (2023):** the *T. kivui* study showed that an optimum can shift after ~180 generations, but selection at 45 °C produced a peak at 60 °C rather than improved growth at the selection temperature. This cautions that the genetic architecture of temperature optima is indirect and constrained. (lehmann2023adaptivelaboratoryevolution pages 3-4)

### Real-world uses

Mechanistic prediction of temperature optima and thermal reaction norms has applications in fermentation temperature selection, starter-culture design, cold-chain spoilage control, pathogen persistence outside hosts, bioreactor robustness, ecological growth-rate modeling, and adaptive laboratory evolution of production strains. The proteome-allocation study specifically warns that ribosome or RNA content can be misleading as an ecological growth proxy when temperature varies. (mairet2021optimalproteomeallocation pages 1-2)

For curation and machine learning, the immediate application is **feature selection**: membrane-lipid remodeling genes, fatty-acid profiles, chaperone capacity, and cardinal-temperature growth curves are informative features. They should not, however, be treated as deterministic markers of the 22–27 °C class.

### Expert synthesis

The evidence supports membrane fluidity as a necessary homeostatic variable, not a unique “mesophile switch.” The optimum is emergent from several interacting constraints. Lipid composition is also taxon- and strain-specific: Gram-negative bacteria, Gram-positive bacteria, fungi, and archaea deploy different acyl chains, headgroups, and ether-lipid architectures. The 2024 *E. coli* mechanism is therefore best represented as a taxon-scoped mechanistic exemplar nested under a more general homeoviscous-adaptation graph.

## 7. Claims that should not yet be curated

1. **“More unsaturated fatty acids cause a 22–27 °C optimum.”** Evidence shows that unsaturation helps compensate for cooling; it does not establish the location of the organismal optimum.
2. **FabI, FabB, or FabR as universal determinants.** The mechanism is strong in *E. coli*, but other taxa use desaturases, branched-chain lipids, chain-length changes, headgroup remodeling, carotenoids, sterols, or archaeal ether lipids.
3. **FabG P216L causes a lower optimum.** The evolved *T. kivui* strain contained 67 SNPs, and no allele reconstruction established causality. (lehmann2023adaptivelaboratoryevolution pages 6-7)
4. **A single optimum independent of assay conditions.** Medium, oxygen, pH, salinity, pressure, substrate, and acclimation can shift the measured thermal curve.
5. **Growth at 22–27 °C implies `METPO:1000443`.** The rate must be maximal there relative to temperatures on both sides.
6. **Cold-shock induction equals low-temperature preference.** Acute shock responses demonstrate tolerance/acclimation, not an inherited optimum.
7. **Chaperone allocation directly sets this trait.** Current retrieved evidence is model-supported and not specific to 22–27 °C. (mairet2021optimalproteomeallocation pages 1-2)
8. **Species-wide propagation from one strain.** The six-strain *A. baumannii* lipidomics study demonstrates meaningful within-species heterogeneity. (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 2-4)
9. **Unverified CURIEs.** Gene products, chemicals, reactions, and pathways should remain label-only until UniProt, ChEBI, Rhea, KEGG, MetaCyc, EC, or GO records are checked against the exact taxon and molecular role.

## DOI-first bibliography

1. **Hoogerland L, et al.** “A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in *Escherichia coli*.” *Nature Communications* 15, 9386. Published October 2024. DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5). (hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 3-4)
2. **Dessenne C, et al.** “Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of *Acinetobacter baumannii*.” *Microbiology Spectrum* 12. Published October 2024. DOI: [10.1128/spectrum.00757-24](https://doi.org/10.1128/spectrum.00757-24). (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 2-4)
3. **Lehmann M, et al.** “Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.” *Frontiers in Microbiology* 14. Published October 2023. DOI: [10.3389/fmicb.2023.1265216](https://doi.org/10.3389/fmicb.2023.1265216). (lehmann2023adaptivelaboratoryevolution pages 3-4)
4. **Gohrbandt M, et al.** “Low membrane fluidity triggers lipid phase separation and protein segregation in living bacteria.” *The EMBO Journal* 41:e109800. Published January 17, 2022. DOI: [10.15252/embj.2021109800](https://doi.org/10.15252/embj.2021109800). (gohrbandt2022lowmembranefluidity pages 12-14, gohrbandt2022lowmembranefluidity pages 1-2)
5. **Mairet F, Gouzé J-L, de Jong H.** “Optimal proteome allocation and the temperature dependence of microbial growth laws.” *npj Systems Biology and Applications* 7:14. Published March 2021. DOI: [10.1038/s41540-021-00172-y](https://doi.org/10.1038/s41540-021-00172-y). (mairet2021optimalproteomeallocation pages 1-2)
6. **de Mendoza D.** “Temperature sensing by membranes.” *Annual Review of Microbiology* 68:101–116. Published September 2014. DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). (mendoza2014temperaturesensingby pages 1-2)

## Curation recommendation

For `data/traits/environment/temperature_optimum_mid1.yaml`, retain a small generic graph centered on temperature-dependent membrane state and growth-compatible homeostasis, then add the FabI–FabB–FabR mechanism as a clearly labeled *E. coli*-specific evidence module. Mark all edges connecting those molecular mechanisms directly to `METPO:1000443` as **contributes_to/uncertain** until a strain with a measured 22–27 °C optimum is perturbed genetically or chemically and its full cardinal-temperature curve shifts reproducibly.

References

1. (hoogerland2024atemperaturesensitivemetabolic pages 5-6): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

2. (hoogerland2024atemperaturesensitivemetabolic pages 3-4): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

3. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

4. (lehmann2023adaptivelaboratoryevolution pages 3-4): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

5. (mendoza2014temperaturesensingby pages 1-2): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

6. (gohrbandt2022lowmembranefluidity pages 1-2): Marvin Gohrbandt, André Lipski, James W Grimshaw, Jessica A Buttress, Zunera Baig, Brigitte Herkenhoff, Stefan Walter, Rainer Kurre, Gabriele Deckers‐Hebestreit, and Henrik Strahl. Low membrane fluidity triggers lipid phase separation and protein segregation in living bacteria. The EMBO Journal, Jan 2022. URL: https://doi.org/10.15252/embj.2021109800, doi:10.15252/embj.2021109800. This article has 147 citations.

7. (hoogerland2024atemperaturesensitivemetabolic media 44b7d377): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

8. (hoogerland2024atemperaturesensitivemetabolic media 68fb0e6e): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

9. (mairet2021optimalproteomeallocation pages 1-2): Francis Mairet, Jean-Luc Gouzé, and Hidde de Jong. Optimal proteome allocation and the temperature dependence of microbial growth laws. npj Systems Biology and Applications, Mar 2021. URL: https://doi.org/10.1038/s41540-021-00172-y, doi:10.1038/s41540-021-00172-y. This article has 47 citations.

10. (lehmann2023adaptivelaboratoryevolution pages 6-7): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

11. (gohrbandt2022lowmembranefluidity pages 10-11): Marvin Gohrbandt, André Lipski, James W Grimshaw, Jessica A Buttress, Zunera Baig, Brigitte Herkenhoff, Stefan Walter, Rainer Kurre, Gabriele Deckers‐Hebestreit, and Henrik Strahl. Low membrane fluidity triggers lipid phase separation and protein segregation in living bacteria. The EMBO Journal, Jan 2022. URL: https://doi.org/10.15252/embj.2021109800, doi:10.15252/embj.2021109800. This article has 147 citations.

12. (gohrbandt2022lowmembranefluidity pages 12-14): Marvin Gohrbandt, André Lipski, James W Grimshaw, Jessica A Buttress, Zunera Baig, Brigitte Herkenhoff, Stefan Walter, Rainer Kurre, Gabriele Deckers‐Hebestreit, and Henrik Strahl. Low membrane fluidity triggers lipid phase separation and protein segregation in living bacteria. The EMBO Journal, Jan 2022. URL: https://doi.org/10.15252/embj.2021109800, doi:10.15252/embj.2021109800. This article has 147 citations.

13. (dessenne2024lipidomicanalysesreveal pages 1-2): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

14. (dessenne2024lipidomicanalysesreveal pages 2-4): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

15. (hoogerland2024atemperaturesensitivemetabolic pages 1-2): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

16. (hoogerland2024atemperaturesensitivemetabolic pages 6-7): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.