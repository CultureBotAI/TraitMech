---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:06:38.666417'
end_time: '2026-08-04T03:15:21.016127'
duration_seconds: 522.35
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pressure optimum
  trait_identifier: traitmech:000004
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: pressure_optimum
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pressure phenotype with numerical limits giving the hydrostatic pressure
    at which an organism grows fastest.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum,
    120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a measurable
    pressure optimum (120 MPa), the quantitative value this phenotype records.) |
    DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known
    as piezophiles, referring to their preference for high pressure (Pressure-adaptation
    review supports an organism-specific optimal growth pressure as the defining quantity
    for piezophile classification.)'
  causal_graph_summary: 'pressure_optimum_balanced_adaptation: 9 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pressure optimum
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000004
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits giving the hydrostatic pressure at which an organism grows fastest.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a measurable pressure optimum (120 MPa), the quantitative value this phenotype records.) | DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports an organism-specific optimal growth pressure as the defining quantity for piezophile classification.)
- **Existing causal graph summary:** pressure_optimum_balanced_adaptation: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **pressure optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_optimum.yaml`.

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
- **Trait label:** pressure optimum
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000004
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits giving the hydrostatic pressure at which an organism grows fastest.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a measurable pressure optimum (120 MPa), the quantitative value this phenotype records.) | DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports an organism-specific optimal growth pressure as the defining quantity for piezophile classification.)
- **Existing causal graph summary:** pressure_optimum_balanced_adaptation: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **pressure optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_optimum.yaml`.

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


# Curation-focused research report: microbial pressure optimum

## Executive assessment

**Trait:** pressure optimum  
**Trait identifier:** `traitmech:000004`  
**Category:** ENVIRONMENT  
**Term kind:** CLASS  
**Mapping status:** REVIEWED  
**Parent:** `METPO:1000059`

**Recommended interpretation.** Pressure optimum is the hydrostatic pressure at which an organism’s growth rate is maximal under a specified set of otherwise fixed conditions. Operationally, it is the argmax of a pressure–growth response curve, not merely a pressure at which growth, activity, or survival occurs. Contemporary literature likewise defines piezophiles as organisms growing optimally above atmospheric pressure, approximately 0.1 MPa. (oger2010themanyways pages 2-4, malas2024biologicalfunctionsat pages 1-2)

The strongest current model is a **balanced, multicomponent adaptation**: hydrostatic pressure perturbs membranes, macromolecular assemblies, transport, motility, translation, and division, while taxon-specific adaptations preserve these functions. No single pathway is established as a universal determinant of the numerical optimum. Recent work provides direct causal evidence for pressure-resistant FtsZ assembly and taxon-specific flagellar functions, but most membrane, osmotic, stress-response, and metabolic links remain associations with pressure tolerance rather than demonstrated shifts in pressure optimum. (oger2010themanyways pages 4-5, scheffer2023themysteryof pages 6-7, cui2024nterminusgtpasedomain pages 1-2, zheng2023mechanismsofnucleic pages 11-12)

## 1. Trait scope and boundaries

### 1.1 Included phenotype

A valid pressure-optimum measurement requires:

1. viable growth or reproduction measured at multiple hydrostatic pressures;
2. a quantitative response such as specific growth rate, generation time, biomass increase, or cell-number increase;
3. temperature, medium, salinity, pH, gas phase, electron donor/acceptor, inoculum state, and incubation time held constant or explicitly modeled;
4. a pressure series sufficiently dense to locate the maximum; and
5. preferably in situ measurements or pressure-preserving sampling because depressurization can alter physiology.

The supplied *Colwellia marinimaniae* MTCD1 observation—growth from 80–140 MPa with an optimum of 120 MPa at 6°C—is therefore an excellent trait instance: 80–140 MPa is the **growth range**, while 120 MPa is the **pressure optimum**. Other quantitative examples illustrate organism specificity: *Colwellia* MT-41 grows optimally near 70 MPa at 2°C, *Pyrococcus yayanosii* CH1 near 52 MPa at 98°C, and neither grows below 20 MPa. (oger2010themanyways pages 4-5)

### 1.2 Excluded or neighboring phenotypes

| Nearby concept | Why it is not pressure optimum |
|---|---|
| Pressure growth range | Minimum-to-maximum pressures supporting growth; does not identify the growth-rate maximum. |
| Maximum growth pressure | Upper boundary permitting growth, not the optimum. |
| Piezotolerance | Ability to grow or retain function at elevated pressure even when atmospheric pressure remains optimal. *Microbacterium sediminis* YLB-01, for example, grows from 0.1–80 MPa but has reported optimum conditions of 28°C and 0.1 MPa. (qiu2024metabolicadaptationsof pages 9-11) |
| Barotolerance or shock survival | Survival after a pressure pulse is not sustained growth under pressure. Engineered ether-lipid *E. coli* experiments explicitly measured robustness after shock. (tamby2024exploringrobustnessof pages 1-2) |
| Metabolic activity under pressure | Activity or gene expression can persist without population growth. *S. oneidensis* MR-1 remained active during 158 MPa exposure and grew after decompression, but this did not establish growth at 158 MPa or an optimum there. (malas2024biologicalfunctionsat pages 1-2) |
| Isolation depth/in situ pressure | Ecological context and useful prior, but not a laboratory growth optimum. |
| Pressure-induced transcription | A response marker, not evidence that the regulated gene raises the organism’s optimal pressure. |
| Piezophile classification | A categorical interpretation derived from an elevated optimum; the numerical pressure optimum is the underlying quantitative phenotype. |

### 1.3 Important boundary conditions

Pressure and temperature jointly alter membrane state. Psychropiezophiles often shorten and desaturate lipid chains, whereas thermopiezophiles may lengthen chains and increase saturation because the thermophilic response counteracts temperature-induced fluidization. Thus, “more unsaturation raises pressure optimum” is not universally valid. (schlegel2024underpressurethe pages 118-123)

Substrate, salinity, growth phase, pressurization rate, exposure duration, and decompression also matter. Compatible solutes may respond to pressure, salinity, or temperature, so they should not be assigned uniquely to pressure without factorial controls. (scheffer2023themysteryof pages 9-10, zhong2024insightintothe pages 1-2)

## 2. Candidate causal-graph nodes

Only identifiers that can be stated confidently are proposed. Labels should remain ungrounded where strain-specific genes, lipid classes, or processes cannot be assigned safely without ontology lookup.

### 2.1 Trait, environmental, and assay nodes

- **pressure optimum** — `traitmech:000004`
- **parent pressure phenotype** — `METPO:1000059`
- hydrostatic pressure — label-only pending ENVO/PATO alignment
- atmospheric pressure, 0.1 MPa — quantitative assay condition
- growth rate — candidate `GO:0016049` only if the graph uses GO biological-process semantics; otherwise label-only quantitative outcome
- temperature; salinity; pH; nutrient medium; incubation duration; pressurization/decompression protocol — assay-context nodes
- pressure growth range; maximum growth pressure; pressure tolerance; survival after pressure shock — separate phenotype labels, not aliases

### 2.2 Organisms and taxonomic contexts

Candidate taxa should be grounded to NCBITaxon after record-level verification:

- *Colwellia marinimaniae* MTCD1 — hyperpiezophilic trait exemplar, optimum 120 MPa at 6°C
- *Shewanella benthica* DB21MT-2 — obligate piezophile, reported optimum 80 MPa (cui2024nterminusgtpasedomain pages 1-2)
- *Photobacterium profundum* SS9 — optimum approximately 20–30 MPa; pressure-regulated membrane and motility systems (scheffer2023themysteryof pages 6-7, scheffer2023themysteryof pages 9-10)
- *Pyrococcus yayanosii* CH1 — obligate thermopiezophile, optimum approximately 52 MPa at 98°C (oger2010themanyways pages 4-5)
- *Hujiaoplasma nucleasis* zrk29 — wall-less piezotolerant bacterium tested at 12 MPa (zheng2023mechanismsofnucleic pages 14-16, zheng2023mechanismsofnucleic pages 11-12)
- *Microbacterium sediminis* YLB-01 — pressure-tolerant but atmospheric-pressure optimum (qiu2024metabolicadaptationsof pages 9-11)
- *Shewanella oneidensis* MR-1 and *Escherichia coli* — pressure-sensitive experimental comparators
- *Aspergillus sydowii* DM1 — hadal fungal piezotolerance model, not yet a pressure-optimum exemplar (zhong2024insightintothe pages 1-2)

### 2.3 Cellular components, proteins, and genes

- cytoplasmic membrane — `GO:0005886`
- FtsZ — use taxon-specific UniProt accessions after sequence verification
- FtsZ N-terminal GTPase domain — label-only structural region
- Z ring — `GO:0032153`
- cell division — `GO:0051301`
- FtsZ polymerization/GTPase activity — candidate GO grounding should be selected only after checking the relevant species annotation
- omega-3 polyunsaturated-fatty-acid synthase **pfa** operon — label-only or taxon-specific gene/protein records
- delta-9 acyl-phospholipid desaturase — use taxon-specific UniProt/EC record after verification
- acyl carrier protein — taxon-specific protein; adaptive evolution implicates the encoding gene in altered pressure growth and unsaturated-fatty-acid regulation (oger2010themanyways pages 4-5)
- flagellar genes **flaB3**, **fliD**, **fliA** — taxon-specific gene nodes
- methyl-accepting chemotaxis protein and CheA/C/D proteins — taxon-specific protein nodes
- outer membrane protein OmpH — taxon-specific protein node
- cold-shock protein CspG; ArgA, ArgB, ArgC, ArgF — response candidates, not established optimum determinants (malas2024biologicalfunctionsat pages 1-2)
- HOG–MAPK pathway — fungal response candidate, uncertain for pressure optimum (zhong2024insightintothe pages 1-2)
- Hyn hydrogenase, TCA cycle, oxidative phosphorylation — energy-metabolism candidates with mainly omics-level evidence (schlegel2024underpressurethe pages 142-150, qiu2024metabolicadaptationsof pages 9-11)

### 2.4 Chemicals, metabolites, and material properties

- magnesium(2+) — `CHEBI:18420`
- potassium(1+) — `CHEBI:29103`
- sodium(1+) — `CHEBI:29101`
- L-glutamate — `CHEBI:29985`
- L-glutamine — `CHEBI:18050`
- L-aspartate — `CHEBI:29991`
- phosphatidylethanolamine — `CHEBI:16038`
- phosphatidylglycerol — `CHEBI:17517`
- cardiolipin — `CHEBI:28494`
- unsaturated fatty acid; monounsaturated fatty acid; polyunsaturated fatty acid — use appropriate CHEBI class after checking the intended abstraction level
- membrane fluidity, membrane packing, intracellular osmotic pressure — label-only physicochemical nodes
- compatible solute/piezolyte — label-only class unless a specific compound is measured

## 3. Evidence-backed candidate edges

The following triples distinguish direct interventions from associations. “Supports optimum” means evidence connects a mechanism to the numerical growth optimum; very few studies meet that standard.

| Subject | Predicate | Object | Evidence and supporting snippet | Curation note |
|---|---|---|---|---|
| Increasing hydrostatic pressure | decreases | membrane fluidity | Review evidence: pressure “reduces membrane fluidity by increasing lipid packing”; transport and membrane functions are consequently impaired. DOI: [10.1016/j.resmic.2010.09.017](https://doi.org/10.1016/j.resmic.2010.09.017), Dec 2010. (oger2010themanyways pages 4-5, oger2010themanyways pages 2-4) | **Moderate confidence, general background.** Mechanistically plausible and broadly supported, but not a direct determinant of an organism’s optimum. Temperature-dependent exceptions must be represented. |
| Increased membrane-lipid unsaturation | increases/maintains | membrane fluidity under HHP | The 2023 review reports that pressure compacts fatty-acid chains and that cells compensate by increasing unsaturated fatty acids; *P. profundum* uses the **pfa** operon, while piezophilic *Colwellia* possess delta-9 acyl-phospholipid-desaturase genes. DOI: [10.3390/microorganisms11071629](https://doi.org/10.3390/microorganisms11071629), Jun 2023. (scheffer2023themysteryof pages 6-7) | **Moderate, taxon-conditional.** Mostly comparative or expression evidence; do not assert that it raises pressure optimum universally. |
| pfa operon | promotes | omega-3 PUFA production | Review snippet: “*Photobacterium profundum* increases ω-3 polyunsaturated fatty acids via the pfa operon.” DOI above. (scheffer2023themysteryof pages 6-7) | **Moderate for product formation; uncertain for optimum.** Prefer a primary pfa perturbation paper before connecting to `traitmech:000004`. |
| FtsZ from *S. benthica* DB21MT-2 | maintains | Z-ring formation under HHP | “HHP hardly affected the Z-ring formation of FtsZSb,” whereas the pressure-sensitive homolog was disrupted. *S. benthica* has a reported optimum of 80 MPa. DOI: [10.3389/fmicb.2024.1441398](https://doi.org/10.3389/fmicb.2024.1441398), 16 Aug 2024. (cui2024nterminusgtpasedomain pages 1-2) | **High confidence for component function; indirect for optimum.** Direct comparative in vivo evidence, but no whole-organism optimum shift was measured. |
| FtsZSb N-terminal GTPase domain | promotes | FtsZ-filament/Z-ring stability at 50 MPa | Replacing this region with the pressure-sensitive homolog reduced Z-ring-like cells from 10.2±4.5% at 0.1 MPa to 5.8±1.4% at 50 MPa. At 50 MPa, only three FtsZSo bundles were found over nine grids versus 20 FtsZSb bundles over ten grids. (cui2024nterminusgtpasedomain pages 7-9) | **High-confidence direct perturbation.** Suitable graph edge if represented as preservation of cell division under pressure, not directly as “increases pressure optimum.” |
| FtsZSb residues S54, T57, L80, E152, S232 | support | Z-ring maintenance at 50 MPa | Point mutation caused >2-fold reductions in Z-ring-like fluorescence; L80A and E152A fell from about 5% at atmospheric pressure to <1% at 50 MPa. DOI above. (cui2024nterminusgtpasedomain pages 9-10) | **High-confidence, residue- and assay-specific.** Curate only if TraitMech accepts fine-grained protein-region nodes. |
| Functional flagellar genes flaB3/fliD/fliA | promote | high-pressure growth in *Desulfovibrio alaskensis* | Deletion mutants were nonmotile and had reduced high-pressure growth rates. DOI of review: [10.3390/microorganisms11071629](https://doi.org/10.3390/microorganisms11071629). (scheffer2023themysteryof pages 6-7) | **Moderate-to-high, taxon-specific.** Review-level snippet reports direct mutants; retrieve the primary mutant paper before final YAML curation. |
| HHP exposure | increases | intracellular Mg2+, K+, Na+ and organic anions in *H. nucleasis* zrk29 | At 12 versus 0.1 MPa for seven days, cations and aspartate, glutamate, and glutamine were “all significantly upregulated.” DOI: [10.1128/mbio.00958-23](https://doi.org/10.1128/mbio.00958-23), Aug 2023. (zheng2023mechanismsofnucleic pages 14-16, zheng2023mechanismsofnucleic pages 11-12) | **Moderate association.** “Upregulated” here includes measured concentration changes; no transporter perturbation established causality. |
| Cation plus organic-anion accumulation | increases | intracellular osmotic pressure | Authors infer that zrk29 “responds to HHP by upregulating its intracellular osmotic pressure.” (zheng2023mechanismsofnucleic pages 11-12) | **Uncertain/inferred.** Curate only with an inference qualifier. The prior observation that Mg2+ supplementation increased a community’s maximum growth pressure is promising but concerns a community and a maximum, not an optimum. |
| HHP exposure | increases | unsaturated phospholipid chains in zrk29 | “The proportion of unsaturated fatty acid chains in phospholipids…under HHP were higher than…atmospheric pressure.” DOI above. (zheng2023mechanismsofnucleic pages 11-12) | **Moderate association, 12 MPa assay.** Supports membrane remodeling and tolerance, not a pressure-optimum shift. |
| HHP at 158 MPa | regulates | 264 genes in *S. oneidensis* MR-1 | Following a 15-min exposure, 264 genes were regulated, mostly upward; argA/B/C/F, membrane-reconfiguration genes, cspG, and antioxidant genes were implicated. DOI: [10.3389/fmicb.2024.1293928](https://doi.org/10.3389/fmicb.2024.1293928), 13 Feb 2024. (malas2024biologicalfunctionsat pages 1-2) | **Low for causal graph.** This is a shock-response transcriptome in a non-piezophile, not growth at 158 MPa and not an optimum assay. |
| HHP at 30 MPa and 4°C | alters | amino-acid, carbohydrate, lipid, TCA and oxidative-phosphorylation pathways in YLB-01 | Integrated proteomics/metabolomics identified altered pathways, but both pressure and low temperature reduced growth and the strain’s reported optimum remained 0.1 MPa. DOI: [10.1007/s00253-023-12906-5](https://doi.org/10.1007/s00253-023-12906-5), Jan 2024. (qiu2024metabolicadaptationsof pages 9-11) | **Low/omics association.** Useful contextual processes, but unsuitable as direct pressure-optimum edges. |
| Bacterial ether-bonded membrane lipids | increase | post-shock HHP robustness in engineered *E. coli* | Engineered cells with bacterial ether lipids were more robust, while archaeal ether lipids had no effect under tested conditions. DOI: [10.3389/fmicb.2024.1470844](https://doi.org/10.3389/fmicb.2024.1470844), 14 Nov 2024. (tamby2024exploringrobustnessof pages 1-2) | **Direct for survival, not optimum.** A 50 MPa shock and morphology endpoint must not be converted into a growth-optimum edge. |
| Combined 50 MPa and 47°C shock | impairs | cell division/morphology in engineered *E. coli* | Occasional cells >20 μm were observed; authors caution that frequency was too low for a representative ratio and imaging was delayed. (tamby2024exploringrobustnessof pages 8-9) | **Do not curate.** Assay limitations and combined stress prevent a strong causal edge. |
| Hadal origin of *A. sydowii* DM1 | associates with | fungal piezotolerance | DM1 showed greater pressure resistance; transcriptomic changes involved membrane permeability, hyphal morphology, septa, amino-acid/carbohydrate metabolism, and proposed HOG–MAPK/stress responses. DOI: [10.1128/msystems.01085-23](https://doi.org/10.1128/msystems.01085-23), published 20 Dec 2023/Jan 2024 issue. (zhong2024insightintothe pages 1-2) | **Uncertain for optimum.** Comparative phenotype plus transcriptomic speculation; retain as eukaryotic context. |

The graph-prioritization matrix below summarizes which findings are currently graph-ready.

| Candidate mechanism/edge | Strongest evidence type | Taxa/assay | Curation recommendation |
|---|---|---|---|
| hydrostatic pressure → reduced membrane fluidity / increased membrane packing | Broad physiological and review evidence; pressure perturbs membranes and transport, but usually not tied to measured optimum shift (oger2010themanyways pages 4-5, oger2010themanyways pages 2-4) | General microbial physiology; multiple taxa summarized under elevated hydrostatic pressure | **Curate as background environmental edge** supporting component constraints on growth under pressure; **does not by itself support pressure optimum** |
| increased unsaturated fatty acids → increased membrane fluidity under pressure | Repeated observational evidence across piezophiles and pressure-response studies; some engineered/adaptive contexts, but mostly correlation with tolerance rather than direct optimum mapping (scheffer2023themysteryof pages 6-7, zheng2023mechanismsofnucleic pages 11-12, tamby2024exploringrobustnessof pages 1-2) | Photobacterium profundum, Halomonas spp., Hujiaoplasma nucleasis zrk29, engineered E. coli, other deep-sea taxa | **Curate cautiously as adaptation/tolerance edge** with taxon notes; **mark uncertain for pressure optimum** unless linked to actual growth-rate curve shift |
| FtsZ N-terminal GTPase domain → Z-ring stability at 50 MPa | **Direct experimental causality** via chimeras and point mutants; in vivo localization and in vitro filament stability under 50 MPa (cui2024nterminusgtpasedomain pages 1-2, cui2024nterminusgtpasedomain pages 7-9, cui2024nterminusgtpasedomain pages 9-10) | Shewanella benthica DB21MT-2 FtsZ vs Shewanella oneidensis MR-1; GFP-tagged FtsZ, 0.1 vs 50 MPa; optimum of S. benthica noted as 80 MPa | **High-priority curation** as component-function edge: FtsZ N-terminal GTPase domain supports cell division under pressure; **supports tolerance/component function more directly than whole-organism pressure optimum** |
| flagellar genes / motility systems → high-pressure growth | Mixed evidence: strongest direct causality from deletion mutants in Desulfovibrio alaskensis; otherwise comparative genomics/transcriptomics in piezophiles (scheffer2023themysteryof pages 6-7, oger2010themanyways pages 4-5) | Desulfovibrio alaskensis mutant studies; Photobacterium profundum SS9 comparative gene clusters and expression | **Curate with moderate confidence** for taxa with mutant evidence; **mark taxon-specific and not yet a generic pressure-optimum determinant** |
| cation accumulation + organic-anion accumulation → increased intracellular osmotic pressure under pressure | Primary-study quantitative response evidence, but mechanistic inference rather than targeted perturbation (zheng2023mechanismsofnucleic pages 11-12) | Hujiaoplasma nucleasis zrk29 cultured 0.1 vs 12 MPa for 7 days; Mg2+, K+, Na+ and aspartate/glutamate/glutamine increased | **Curate as inferred tolerance mechanism** with uncertainty flag; **does not establish shift in pressure optimum** |
| pressure-responsive membrane reconfiguration / arginine biosynthesis / cold-shock and antioxidant response pathways → survival or activity at extreme pressure | Transcriptomic inference only; no direct causal intervention and no growth-optimum assay (malas2024biologicalfunctionsat pages 1-2) | Shewanella oneidensis MR-1 exposed to 158 MPa for 15 min or 2 h; 264 genes regulated | **Do not curate as direct causal edges for pressure optimum yet**; keep as supporting context for tolerance/survival under shock exposure |
| amino acid metabolism / carbohydrate metabolism / TCA / oxidative phosphorylation changes → adaptation to high pressure | Omics-based association under designed high-pressure/low-temperature comparison; not direct intervention, and strain optimum remained atmospheric in cited background (qiu2024metabolicadaptationsof pages 9-11) | Microbacterium sediminis YLB-01 under HPLT 30 MPa at 4°C vs NPLT 0.1 MPa at 4°C; prior optimum 28°C and 0.1 MPa noted | **Low-priority for graph curation**; useful as context nodes/processes, but **supports acclimation/tolerance rather than pressure optimum** |
| cell membrane permeability / hyphal morphology / septal quantities / HOG-MAPK and stress proteins → fungal piezotolerance | Phenotyping plus transcriptomics/speculation; no direct optimum edge and focused on piezotolerance (zhong2024insightintothe pages 1-2) | Aspergillus sydowii isolates from terrestrial, shallow, and hadal sources under elevated pressure | **Do not curate as causal pressure-optimum edges yet**; retain as eukaryotic comparative context only |
| bacterial ether-bonded membrane lipids → greater robustness after HHP shock | Engineered functional test, but endpoint is robustness/survival after shock, not growth optimum (tamby2024exploringrobustnessof pages 1-2, tamby2024exploringrobustnessof pages 8-9) | Engineered E. coli with bacterial or archaeal ether-bonded lipids; 50 MPa shock and temperature combinations | **Do not use as pressure-optimum edge**; at most curate as experimental support that membrane chemistry can alter pressure robustness |
| organism-specific optimum growth pressure defines piezophile classification | Definition/classification evidence plus quantitative examples; not mechanistic (oger2010themanyways pages 2-4, malas2024biologicalfunctionsat pages 1-2) | General piezophile literature; examples include obligate piezophiles and high-pressure specialists | **Use for scope and trait definition only**; not a causal graph edge |
| measured optimum pressure values (e.g., obligate piezophile examples) → trait instance data | Quantitative phenotype evidence, including S. benthica optimum 80 MPa and supplied Colwellia example with optimum 120 MPa metadata support (cui2024nterminusgtpasedomain pages 1-2) | Shewanella benthica DB21MT-2; supplied Colwellia marinimaniae MTCD1 evidence external to contexts | **Curate as trait-instance phenotype evidence** for traitmech:000004, separate from mechanistic edges |
| ribosome / translation vulnerability under pressure → reduced growth | Foundational physiological evidence, largely from older work and reviews; limited direct modern causal mapping to optimum (oger2010themanyways pages 4-5, oger2010themanyways pages 2-4) | General bacteria; pressure effects on protein/nucleic-acid synthesis and ribosome stability | **Curate only as broad background constraint** unless paired with direct gene/protein perturbation evidence |
| pressure optimum emerges from balanced adaptation across membrane, division, motility, osmotic, and metabolic systems | Integrative inference across reviews and primary studies; no single decisive mechanism universal across taxa (oger2010themanyways pages 4-5, scheffer2023themysteryof pages 6-7, malas2024biologicalfunctionsat pages 1-2, zheng2023mechanismsofnucleic pages 11-12) | Cross-taxon synthesis | **Best current graph summary:** represent as a multi-factor, taxon-conditional trait; avoid overcommitting any single pathway as the universal driver of pressure optimum |


*Table: This table prioritizes candidate mechanisms for curating the microbial pressure optimum trait and distinguishes direct causal evidence from broader tolerance or transcriptomic associations. It is useful for deciding which edges are graph-ready now versus which should remain flagged as uncertain or contextual.*

## 4. Recommended graph architecture

A conservative graph should retain the existing “balanced adaptation” concept but avoid a direct shortcut from every response mechanism to pressure optimum.

### 4.1 Core mechanistic chain

1. **elevated hydrostatic pressure → increased membrane packing / reduced membrane fluidity**
2. **reduced membrane fluidity → impaired membrane transport and membrane-associated processes**
3. **unsaturated-fatty-acid enrichment → maintenance of membrane fluidity under pressure**
4. **elevated hydrostatic pressure → destabilization of pressure-sensitive FtsZ filaments**
5. **pressure-adapted FtsZ N-terminal GTPase domain → maintenance of Z-ring assembly at HHP**
6. **maintained Z-ring assembly → maintained cell division under HHP**
7. **maintained membrane, division, translation, motility, osmotic, and energy functions → improved growth under a specified HHP condition**
8. **growth-rate response over a pressure series → pressure optimum**

Edges 1–6 have component-level support. Edge 7 is integrative and should be qualified as inferred. Edge 8 is a measurement/derivation relation rather than a molecular causal edge.

### 4.2 Context modifiers

Temperature, salinity, medium composition, electron donor and acceptor, growth phase, exposure time, and decompression protocol should modify the growth-response relationship rather than sit upstream as universal positive or negative causes. For example, at 20 MPa one piezophilic vent isolate’s generation time reportedly fell from 86 to approximately 16 min and yield rose from 7.9×10^8 to 1.7×10^9 cells/mL, while a pressure-sensitive comparator’s yield fell from 3.1×10^8 to 1.4×10^8 cells/mL. The divergent responses illustrate why pressure effects must be organism- and assay-specific. (schlegel2024underpressurethe pages 142-150)

## 5. Recent developments, applications, and expert interpretation

### 5.1 2023–2024 developments

- **Protein-level causality:** The 2024 FtsZ study is the clearest recent mechanistic advance. Chimeras and site-directed mutants localized pressure adaptation to an N-terminal GTPase domain and five residues, using both in vivo Z-ring localization and in vitro filament stability. (cui2024nterminusgtpasedomain pages 1-2, cui2024nterminusgtpasedomain pages 7-9, cui2024nterminusgtpasedomain pages 9-10)
- **Pressure-survival transcriptomics:** A 2024 study found 264 pressure-responsive genes after 15 min at 158 MPa in *S. oneidensis* MR-1, extending pressure biology to icy-ocean-world analog conditions. Its importance is mechanistic hypothesis generation, not evidence of an optimum at 158 MPa. (malas2024biologicalfunctionsat pages 1-2)
- **Wall-less bacterial adaptation:** The 2023 zrk29 study integrated growth assays, transcriptomics, metabolomics, cation measurements, and lipid analysis at 12 MPa, highlighting osmotic balance and membrane unsaturation. (zheng2023mechanismsofnucleic pages 14-16, zheng2023mechanismsofnucleic pages 11-12)
- **Fungal pressure biology:** The 2024 *A. sydowii* work established a multi-endpoint platform for pressure resistance in filamentous fungi and identified candidate HOG–MAPK, membrane, morphology, and metabolic responses. (zhong2024insightintothe pages 1-2)
- **Membrane engineering:** Engineered bacterial ether lipids improved *E. coli* robustness after HHP shock, demonstrating that membrane chemistry is experimentally manipulable, although the endpoint was survival rather than growth optimum. (tamby2024exploringrobustnessof pages 1-2)

### 5.2 Current applications

1. **Deep-ocean cultivation and biogeochemistry.** Pressure-preserving cultivation can recover activities lost after decompression and can improve estimates of carbon, sulfur, methane, and organic-matter turnover. This is an immediate application of pressure-optimum measurements to environmental microbiology.
2. **Astrobiology.** Pressure-response data constrain habitability of subsurface oceans. Titan’s modeled ocean pressure is at least 150 MPa, compared with approximately 110 MPa at Challenger Deep and a reported microbial growth limit of 140 MPa; however, short-term survival at 158 MPa must not be treated as growth. (malas2024biologicalfunctionsat pages 1-2)
3. **Food and biotechnology.** HHP is used for microbial inactivation and biomolecule processing. Understanding FtsZ, membrane, ribosome, and growth-phase sensitivity can improve process design or reveal routes to resistance.
4. **Synthetic biology.** Adaptive evolution and engineered lipids demonstrate that pressure robustness can be modified. The stronger future test is whether engineering shifts the full growth-rate-versus-pressure curve and its optimum, rather than merely improving survival.
5. **Deep-subsurface and reservoir management.** Pressure-conditioned growth affects souring, corrosion, biofilms, hydrocarbon turnover, and bioremediation. Numerical pressure optima can improve predictive ecological models, but they must be measured alongside salinity, temperature, and substrate effects.

### 5.3 Expert synthesis

Authoritative reviews emphasize that membrane adaptation is common but not universal, and that pressure effects are difficult to separate from low temperature. They also caution that the prevalence of unsaturated lipids in deep-sea organisms historically exceeded the available direct mutant evidence. (oger2010themanyways pages 4-5, scheffer2023themysteryof pages 6-7)

Accordingly, the expert-level curation conclusion is:

> `traitmech:000004` should be modeled as an emergent quantitative phenotype produced by preservation and balancing of several pressure-sensitive functions, not as the direct output of a single “piezophile pathway.”

## 6. Claims that should not yet be curated into TraitMech

- Do **not** equate maximum survived pressure, maximum growth pressure, or pressure range with pressure optimum.
- Do **not** infer an optimum from isolation depth.
- Do **not** connect a transcript’s pressure induction directly to increased pressure optimum without knockout, complementation, allele replacement, or engineered expression followed by a pressure-growth curve.
- Do **not** make “increased lipid unsaturation → increased pressure optimum” universal; thermopiezophiles and hybrid lipid responses can differ. (schlegel2024underpressurethe pages 142-150, schlegel2024underpressurethe pages 118-123)
- Do **not** curate the 158 MPa *S. oneidensis* experiment as growth at 158 MPa; viable growth was observed after exposure. (malas2024biologicalfunctionsat pages 1-2)
- Do **not** curate ether-bonded lipids as raising pressure optimum from a shock-survival assay. (tamby2024exploringrobustnessof pages 1-2)
- Do **not** curate HOG–MAPK, arginine biosynthesis, antioxidant defenses, TCA-cycle activation, or compatible-solute pathways as causal optimum determinants based only on omics enrichment.
- Do **not** generalize *Desulfovibrio* flagellar-mutant results across all piezophiles without taxon qualifiers.
- Do **not** assign CURIEs to strain-specific proteins or poorly matched physicochemical concepts without accession verification.

## 7. Recommended evidence needed for decisive curation

The ideal study would engineer a candidate allele or pathway in isogenic strains, then measure replicate growth-rate curves across at least 6–10 pressure points while holding temperature and chemistry constant. A causal pressure-optimum edge should require a statistically supported displacement of the fitted optimum, with complementation restoring the original curve. Simultaneous membrane-state, division, translation, and metabolite measurements would identify the mediator rather than merely the endpoint.

For immediate curation, the best-supported additions are therefore component edges involving pressure-adapted FtsZ and Z-ring maintenance, plus general pressure-to-membrane constraints. The numerical trait instances for *C. marinimaniae* MTCD1 and *S. benthica* DB21MT-2 should remain separate from mechanistic edges.

## DOI-first bibliography

1. Cui X-H et al. **N-terminus GTPase domain of the cytoskeleton protein FtsZ plays a critical role in its adaptation to high hydrostatic pressure.** *Frontiers in Microbiology*. Published 16 Aug 2024. DOI: [10.3389/fmicb.2024.1441398](https://doi.org/10.3389/fmicb.2024.1441398). (cui2024nterminusgtpasedomain pages 1-2)
2. Malas J et al. **Biological functions at high pressure: transcriptome response of Shewanella oneidensis MR-1 to hydrostatic pressure relevant to Titan and other icy ocean worlds.** *Frontiers in Microbiology*. Published 13 Feb 2024. DOI: [10.3389/fmicb.2024.1293928](https://doi.org/10.3389/fmicb.2024.1293928). (malas2024biologicalfunctionsat pages 1-2)
3. Tamby A, Sahonero-Canavesi DX, Villanueva L. **Exploring robustness of hybrid membranes under high hydrostatic pressure and temperature.** *Frontiers in Microbiology*. Published 14 Nov 2024. DOI: [10.3389/fmicb.2024.1470844](https://doi.org/10.3389/fmicb.2024.1470844). (tamby2024exploringrobustnessof pages 1-2)
4. Qiu X et al. **Metabolic adaptations of Microbacterium sediminis YLB-01 in deep-sea high-pressure environments.** *Applied Microbiology and Biotechnology*. Jan 2024. DOI: [10.1007/s00253-023-12906-5](https://doi.org/10.1007/s00253-023-12906-5). (qiu2024metabolicadaptationsof pages 9-11)
5. Zhong M et al. **Insight into the adaptation mechanisms of high hydrostatic pressure in physiology and metabolism of hadal fungi from the deepest ocean sediment.** *mSystems*. Published 20 Dec 2023; 2024 issue. DOI: [10.1128/msystems.01085-23](https://doi.org/10.1128/msystems.01085-23). (zhong2024insightintothe pages 1-2)
6. Zheng R et al. **Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium.** *mBio*. Aug 2023. DOI: [10.1128/mbio.00958-23](https://doi.org/10.1128/mbio.00958-23). (zheng2023mechanismsofnucleic pages 11-12)
7. Scheffer G, Gieg LM. **The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface.** *Microorganisms*. Jun 2023. DOI: [10.3390/microorganisms11071629](https://doi.org/10.3390/microorganisms11071629). (scheffer2023themysteryof pages 6-7)
8. Tamby A, Sinninghe Damsté JS, Villanueva L. **Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment.** *Frontiers in Molecular Biosciences*. Published Jan 2023. DOI: [10.3389/fmolb.2022.1058381](https://doi.org/10.3389/fmolb.2022.1058381).
9. Kusube M et al. **Colwellia marinimaniae sp. nov., a hyperpiezophilic species isolated from an amphipod within the Challenger Deep, Mariana Trench.** *International Journal of Systematic and Evolutionary Microbiology*. Apr 2017. DOI: [10.1099/ijsem.0.001671](https://doi.org/10.1099/ijsem.0.001671).
10. Michoud G, Jebbar M. **High hydrostatic pressure adaptive strategies in an obligate piezophile Pyrococcus yayanosii.** *Scientific Reports*. Jun 2016. DOI: [10.1038/srep27289](https://doi.org/10.1038/srep27289).
11. Marietou A et al. **Adaptive laboratory evolution of Escherichia coli K-12 MG1655 for growth at high hydrostatic pressure.** *Frontiers in Microbiology*. Jan 2015. DOI: [10.3389/fmicb.2014.00749](https://doi.org/10.3389/fmicb.2014.00749).
12. Meersman F et al. **High-Pressure Biochemistry and Biophysics.** *Reviews in Mineralogy and Geochemistry*. 2013. DOI: [10.2138/rmg.2013.75.19](https://doi.org/10.2138/rmg.2013.75.19).
13. Oger PM, Jebbar M. **The many ways of coping with pressure.** *Research in Microbiology*. Dec 2010. DOI: [10.1016/j.resmic.2010.09.017](https://doi.org/10.1016/j.resmic.2010.09.017). (oger2010themanyways pages 4-5, oger2010themanyways pages 2-4)

References

1. (oger2010themanyways pages 2-4): Philippe M. Oger and Mohamed Jebbar. The many ways of coping with pressure. Research in microbiology, 161 10:799-809, Dec 2010. URL: https://doi.org/10.1016/j.resmic.2010.09.017, doi:10.1016/j.resmic.2010.09.017. This article has 277 citations and is from a peer-reviewed journal.

2. (malas2024biologicalfunctionsat pages 1-2): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 9 citations and is from a peer-reviewed journal.

3. (oger2010themanyways pages 4-5): Philippe M. Oger and Mohamed Jebbar. The many ways of coping with pressure. Research in microbiology, 161 10:799-809, Dec 2010. URL: https://doi.org/10.1016/j.resmic.2010.09.017, doi:10.1016/j.resmic.2010.09.017. This article has 277 citations and is from a peer-reviewed journal.

4. (scheffer2023themysteryof pages 6-7): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 33 citations.

5. (cui2024nterminusgtpasedomain pages 1-2): Xue-Hua Cui, Yu-Chen Wei, Xue-Gong Li, Xiao-Qing Qi, Long-Fei Wu, and Wei-Jia Zhang. N-terminus gtpase domain of the cytoskeleton protein ftsz plays a critical role in its adaptation to high hydrostatic pressure. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1441398, doi:10.3389/fmicb.2024.1441398. This article has 1 citations and is from a peer-reviewed journal.

6. (zheng2023mechanismsofnucleic pages 11-12): Rikuan Zheng, Chong Wang, Ruining Cai, Yeqi Shan, and Chaomin Sun. Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.00958-23, doi:10.1128/mbio.00958-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

7. (qiu2024metabolicadaptationsof pages 9-11): Xu Qiu, Xiao-Min Hu, Xi-Xiang Tang, Cai-Hua Huang, Hua-Hua Jian, and Dong-Hai Lin. Metabolic adaptations of microbacterium sediminis ylb-01 in deep-sea high-pressure environments. Applied Microbiology and Biotechnology, 108:1-15, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12906-5, doi:10.1007/s00253-023-12906-5. This article has 11 citations and is from a domain leading peer-reviewed journal.

8. (tamby2024exploringrobustnessof pages 1-2): Anandi Tamby, Diana X. Sahonero-Canavesi, and Laura Villanueva. Exploring robustness of hybrid membranes under high hydrostatic pressure and temperature. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1470844, doi:10.3389/fmicb.2024.1470844. This article has 1 citations and is from a peer-reviewed journal.

9. (schlegel2024underpressurethe pages 118-123): Ian Jeremy Schlegel. Under pressure: the diversity and physiology of the hydrothermal vent microbiome. Text, Jan 2024. URL: https://doi.org/10.7282/t3-b8zr-e148, doi:10.7282/t3-b8zr-e148. This article has 0 citations and is from a peer-reviewed journal.

10. (scheffer2023themysteryof pages 9-10): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 33 citations.

11. (zhong2024insightintothe pages 1-2): Maosheng Zhong, Yongqi Li, Ludan Deng, Jiasong Fang, and Xi Yu. Insight into the adaptation mechanisms of high hydrostatic pressure in physiology and metabolism of hadal fungi from the deepest ocean sediment. Jan 2024. URL: https://doi.org/10.1128/msystems.01085-23, doi:10.1128/msystems.01085-23. This article has 17 citations and is from a peer-reviewed journal.

12. (zheng2023mechanismsofnucleic pages 14-16): Rikuan Zheng, Chong Wang, Ruining Cai, Yeqi Shan, and Chaomin Sun. Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.00958-23, doi:10.1128/mbio.00958-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

13. (schlegel2024underpressurethe pages 142-150): Ian Jeremy Schlegel. Under pressure: the diversity and physiology of the hydrothermal vent microbiome. Text, Jan 2024. URL: https://doi.org/10.7282/t3-b8zr-e148, doi:10.7282/t3-b8zr-e148. This article has 0 citations and is from a peer-reviewed journal.

14. (cui2024nterminusgtpasedomain pages 7-9): Xue-Hua Cui, Yu-Chen Wei, Xue-Gong Li, Xiao-Qing Qi, Long-Fei Wu, and Wei-Jia Zhang. N-terminus gtpase domain of the cytoskeleton protein ftsz plays a critical role in its adaptation to high hydrostatic pressure. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1441398, doi:10.3389/fmicb.2024.1441398. This article has 1 citations and is from a peer-reviewed journal.

15. (cui2024nterminusgtpasedomain pages 9-10): Xue-Hua Cui, Yu-Chen Wei, Xue-Gong Li, Xiao-Qing Qi, Long-Fei Wu, and Wei-Jia Zhang. N-terminus gtpase domain of the cytoskeleton protein ftsz plays a critical role in its adaptation to high hydrostatic pressure. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1441398, doi:10.3389/fmicb.2024.1441398. This article has 1 citations and is from a peer-reviewed journal.

16. (tamby2024exploringrobustnessof pages 8-9): Anandi Tamby, Diana X. Sahonero-Canavesi, and Laura Villanueva. Exploring robustness of hybrid membranes under high hydrostatic pressure and temperature. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1470844, doi:10.3389/fmicb.2024.1470844. This article has 1 citations and is from a peer-reviewed journal.