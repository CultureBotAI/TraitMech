---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:10:05.309870'
end_time: '2026-08-04T03:18:04.963592'
duration_seconds: 479.65
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pressure range
  trait_identifier: traitmech:000005
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: pressure_range
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pressure phenotype with numerical limits that bounds the minimum and
    maximum hydrostatic pressures supporting growth of an organism.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum,
    120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a bounded growth-supporting
    pressure span (80-140 MPa), the quantity this phenotype records.) | DOI:10.3389/fmolb.2022.1058381:
    Microorganisms adapted to HHP are usually known as piezophiles, referring to their
    preference for high pressure (Pressure-adaptation review supports the bounded
    span of growth-permissive hydrostatic pressure as a defining quantitative descriptor.)'
  causal_graph_summary: 'pressure_range_growth_bounded_span: 9 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pressure range
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000005
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits that bounds the minimum and maximum hydrostatic pressures supporting growth of an organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a bounded growth-supporting pressure span (80-140 MPa), the quantity this phenotype records.) | DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports the bounded span of growth-permissive hydrostatic pressure as a defining quantitative descriptor.)
- **Existing causal graph summary:** pressure_range_growth_bounded_span: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **pressure range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_range.yaml`.

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
- **Trait label:** pressure range
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000005
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits that bounds the minimum and maximum hydrostatic pressures supporting growth of an organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a bounded growth-supporting pressure span (80-140 MPa), the quantity this phenotype records.) | DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports the bounded span of growth-permissive hydrostatic pressure as a defining quantitative descriptor.)
- **Existing causal graph summary:** pressure_range_growth_bounded_span: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **pressure range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_range.yaml`.

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


# Curation report: microbial **pressure range**

## 1. Scope and current interpretation

**Trait:** `traitmech:000005`  
**Label:** pressure range  
**Category:** ENVIRONMENT  
**Parent:** `METPO:1000059`

This trait should represent the **experimentally observed interval between the minimum and maximum hydrostatic pressures that support net microbial growth**, under a specified temperature, medium, atmosphere, incubation time, growth phase, and measurement method. It is an organism–condition phenotype, not pressure itself.

The canonical example is *Colwellia marinimaniae* MTCD1, which grows at **80–140 MPa**, with an optimum of **120 MPa**. *Colwellia* sp. MT41 has an optimum of 103 MPa and a reported minimum near 35 MPa. These values demonstrate that the range and optimum are separate phenotypes. Comparative genomic evidence associates extreme piezophily with membrane, respiration, repair, cell-envelope, and proteome-composition features, but does not establish that each feature changes either pressure boundary (makhatadze2024modulationofelectrostatic pages 1-3, peoples2020distinctivegeneand pages 1-2).

### Boundary cases

- **Pressure optimum:** the pressure producing maximal growth rate or yield; it is a point within, but not equivalent to, the range.
- **Piezophily:** preference for elevated pressure, normally operationalized using growth-rate optima. Updated expert definitions use temperature-dependent optimum thresholds rather than a single universal cutoff; proposed optima include 7–20 MPa for piezopsychrophiles, ≥10 MPa for piezomesophiles, ≥20 MPa for piezothermophiles, and ≥50 MPa for hyper-piezopsychrophiles (scoma2021functionalgroupsin pages 5-6).
- **Piezotolerance:** ability to withstand elevated pressure while growing as well as or better at atmospheric pressure. The 2023 review explicitly distinguishes piezotolerant organisms from obligate piezophiles, which grow only under HHP (tamby2023microbialmembranelipid pages 1-2).
- **Survival or recovery after decompression:** not evidence of growth at the exposure pressure. For example, *Shewanella oneidensis* MR-1 remained metabolically active during 158-MPa exposure and some cultures grew after decompression, but this does not define a 158-MPa growth endpoint (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 5-6).
- **Activity at one pressure:** transcription, metabolism, intact cells, or biomass at one test pressure cannot by itself establish both range boundaries.
- **Isolation depth or in-situ pressure:** useful provenance, not a measured phenotype.
- **Barotolerance during stationary-phase exposure:** should not be converted into a growth range unless cell multiplication is demonstrated in situ.

Pressure ranges must be treated as **conditional**. Temperature is especially important: HHP and near-freezing temperature co-occur in most deep-sea settings and have overlapping effects on membrane order. Nutrients, electron acceptors, salinity, pH, growth phase, pressurization/decompression rate, and vessel chemistry can also shift observed limits. The literature regards separating pressure from low-temperature effects as a major methodological challenge (tamby2023microbialmembranelipid pages 1-2).

## 2. Candidate graph nodes

Identifiers below are conservative; label-only nodes are preferable to uncertain mappings.

### Trait and environmental/experimental nodes

- pressure range — `traitmech:000005`
- parent pressure phenotype — `METPO:1000059`
- hydrostatic pressure — label-only candidate
- minimum growth-supporting pressure — label-only
- maximum growth-supporting pressure — label-only
- optimum growth pressure — label-only; model separately from range
- high hydrostatic pressure exposure — label-only
- atmospheric pressure control, typically 0.1 MPa — label-only
- temperature, incubation time, medium composition, oxygen status, growth phase, decompression, infrared irradiation — assay-context nodes
- deep sea — `ENVO:00000232`
- marine sediment — `ENVO:00002113`

### Cellular structures and processes

- plasma membrane — `GO:0005886`
- cell wall — `GO:0005618`
- peptidoglycan biosynthetic process — `GO:0009252`
- cell division — `GO:0051301`
- DNA repair — `GO:0006281`
- response to oxidative stress — `GO:0006979`
- MAPK cascade — `GO:0000165`
- cell-wall integrity signaling cascade — label-only unless a taxon-specific GO mapping is verified
- membrane fluidity/homeoviscous adaptation — label-only candidate
- intracellular osmotic pressure/homeostasis — label-only candidate
- fermentation, carbohydrate metabolism, amino-acid metabolism, respiration, protein folding/proteostasis — pathway-level candidates

### Chemicals and molecular classes

- sodium ion — `CHEBI:29101`
- potassium ion — `CHEBI:29103`
- magnesium ion — `CHEBI:18420`
- calcium ion — `CHEBI:29108`
- reactive oxygen species — `CHEBI:26523`
- glutamate — `CHEBI:29985`
- glutamine — `CHEBI:18050`
- aspartate — `CHEBI:29991`
- UDP-glucose — `CHEBI:18066`
- phosphatidylethanolamine — `CHEBI:16038`
- phosphatidylglycerol — `CHEBI:17517`
- phosphatidylcholine — `CHEBI:64482`
- unsaturated fatty acid and unsaturated membrane phospholipid — class-level candidates; verify exact CHEBI terms during implementation
- glutathione, cysteine, lactate, acetate, trehalose, ATP and GTP — candidate metabolite nodes

### Genes, proteins, and complexes

Taxon-qualified gene nodes are essential because names and functions are not universally interchangeable.

- cation transport: metal ABC transporters, heavy-metal-translocating P-type ATPase, calcium/sodium antiporter
- unsaturated-fatty-acid synthesis: **FAD2**, **SCD**, **desC**
- fungal antioxidant response: **Yap1**, **MET**, **GLT**, **GSS**, **GST**, **SOD**, **katE/CAT/catB**, **srpA**
- fungal cell-wall integrity pathway: **Mid**, **Rho1**, **Pkc1**, **FKS**, **CHS3**, **Bck1**, **Slt2**, **SWI6**
- pressure-responsive stress/arginine genes in *S. oneidensis*: **cspG**, **argA**, **argB**, **argC**, **argF**
- cell division/cell envelope: **FtsZ**, peptidoglycan-synthesis machinery
- Colwellia comparative candidates: NADH dehydrogenase I (**nuo**) complex, Tad pilus, D-Ala–D-Ala ligase, alanine dehydrogenase, SAM-dependent tRNA methyltransferase
- HOG-MAPK components and stress proteins in *Aspergillus sydowii* DM1

Gene identifiers should be assigned from the exact strain annotation or UniProt proteome. Generic UniProt accessions should not be guessed.

## 3. Candidate evidence-backed causal edges

The following table is a compact set of candidate mechanistic edges. “Strong” means the immediate response was measured, not that the edge has been shown to move the minimum or maximum growth-pressure boundary.

| subject | predicate | object | organism/context | evidence strength/uncertainty |
|---|---|---|---|---|
| elevated hydrostatic pressure | inhibits | septal peptidoglycan synthesis | *Tepidibacter hydrothermalis* SWIR-1 under HHP; authors monitored cell-wall synthesis and reported pressure-dependent blockage of septal synthesis (dai2024illuminatingabacterial pages 1-3) | Strong for assay phenotype; organism-specific; mechanism observed directly in microscopy/cell-wall synthesis assay |
| elevated hydrostatic pressure | inhibits | cell division | *Tepidibacter hydrothermalis* SWIR-1; HHP produced filamentous cells and division defects while elongation/chromosome processes were less affected (dai2024illuminatingabacterial pages 1-3) | Strong for assay phenotype; organism-specific |
| 880 nm infrared irradiation | restores/enables | septal peptidoglycan synthesis | *Tepidibacter hydrothermalis* SWIR-1 under HHP; IR “initiated septal synthesis and alleviated the obstruction” (dai2024illuminatingabacterial pages 1-3) | Strong for assay context; conditional on IR + HHP; not a general pressure-range mechanism |
| high hydrostatic pressure | upregulates | cation transporters | *Hujiaoplasma nucleasis* zrk29 at 12 MPa vs 0.1 MPa; metal ABC transporters, P-type ATPase, Ca/Na antiporter upregulated (zheng2023mechanismsofnucleic pages 7-11) | Moderate-strong; transcriptomic association with supporting ion measurements |
| cation transport | increases | intracellular osmotic pressure | *Hujiaoplasma nucleasis* zrk29; intracellular Mg2+, K+, Na+ were ~4–8× higher at 12 MPa, interpreted as osmotic counterpressure (zheng2023mechanismsofnucleic pages 7-11) | Moderate; mechanistic inference supported by quantitative metabolite/ion data, not genetic perturbation |
| high hydrostatic pressure | increases | intracellular cation concentrations | *Hujiaoplasma nucleasis* zrk29; Mg2+, K+, Na+ increased approximately four- to eightfold at 12 MPa (zheng2023mechanismsofnucleic pages 7-11) | Strong for measured response; causal link to pressure tolerance inferred |
| high hydrostatic pressure | increases | phospholipids with unsaturated fatty acid chains | *Hujiaoplasma nucleasis* zrk29 at 12 MPa; unsaturated phospholipid proportion rose ~2–3× and specific PE/PG/PC/PS species increased (zheng2023mechanismsofnucleic pages 7-11) | Strong for measured response |
| increased unsaturated membrane lipids | increases | membrane fluidity | Supported in zrk29 model and broader marine pressure-adaptation review (zheng2023mechanismsofnucleic pages 7-11, tamby2023microbialmembranelipid pages 1-2) | Moderate; direct fluidity not measured in zrk29 here, but well-supported inference/review consensus |
| high hydrostatic pressure | induces | oxidoreductase/antioxidant response pathways | *Schizophyllum commune* 20R-7-F01 at 15 and 35 MPa vs 0.1 MPa; ROS-defense genes/pathways upregulated (Yap1, MET, GLT, GSS, GST, SOD, katE, CAT, catB, srpA) (zhao2024pressuretolerantsurvivalmechanism pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8) | Moderate; transcriptomic/metabolomic association, no perturbation |
| oxidoreductase and hydrolase pathways | detoxify/mitigate | intracellular reactive oxygen species | *Schizophyllum commune* 20R-7-F01 under HHP; authors explicitly interpret antioxidant and peptide-hydrolysis pathways as ROS-protective (zhao2024pressuretolerantsurvivalmechanism pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8) | Moderate; inferred from pathway activation and prior literature |
| high hydrostatic pressure | upregulates | unsaturated-fatty-acid synthesis genes | *Schizophyllum commune* 20R-7-F01; FAD2, SCD, desC upregulated under HHP (zhao2024pressuretolerantsurvivalmechanism pages 6-8) | Moderate; transcriptomic association |
| unsaturated-fatty-acid synthesis | increases | membrane fluidity | *Schizophyllum commune* 20R-7-F01; authors infer adaptation via membrane composition/structure remodeling, supported by prior fungal literature (zhao2024pressuretolerantsurvivalmechanism pages 6-8, tamby2023microbialmembranelipid pages 1-2) | Moderate-weak; inferred, not directly measured |
| high hydrostatic pressure | induces | cell-wall integrity / integral membrane pathway genes | *Schizophyllum commune* 20R-7-F01; Mid, Rho1, Pkc1, FKS, CHS3, Bck1, Slt2 upregulated (zhao2024pressuretolerantsurvivalmechanism pages 6-8) | Moderate; transcriptomic association |
| cell-wall integrity signaling | maintains | cell wall structural stability | *Schizophyllum commune* 20R-7-F01; authors interpret CWI-cascade activation and thicker walls under HHP as stability-maintaining response (zhao2024pressuretolerantsurvivalmechanism pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8) | Moderate; partly inferred from known pathway function plus TEM phenotype |
| high hydrostatic pressure | increases | cell wall thickness | *Schizophyllum commune* 20R-7-F01; wall thickness at day 5 was ~0.6 μm thicker at 15 MPa and ~0.8 μm thicker at 35 MPa than at 0.1 MPa (zhao2024pressuretolerantsurvivalmechanism pages 6-8) | Strong for phenotype; mechanistic mediation still inferred |
| high-pressure treatment | alters | amino acid metabolism | *Microbacterium sediminis* YLB-01 at 30 MPa, 4°C for 7 days; multiple amino acids increased and related pathways shifted (qiu2024metabolicadaptationsof pages 1-2, qiu2024metabolicadaptationsof pages 7-9) | Moderate; metabolomic/proteomic association |
| high-pressure treatment | alters | carbohydrate metabolism | *Microbacterium sediminis* YLB-01 at 30 MPa, 4°C; glycolysis/gluconeogenesis, pyruvate, glyoxylate/dicarboxylate pathways affected (qiu2024metabolicadaptationsof pages 1-2, qiu2024metabolicadaptationsof pages 7-9) | Moderate; metabolomic/proteomic association |
| high-pressure treatment | increases | UDP-glucose accumulation | *Microbacterium sediminis* YLB-01 under 30 MPa, 4°C; UDP-glucose elevated under HPLT vs NPLT (qiu2024metabolicadaptationsof pages 1-2, qiu2024metabolicadaptationsof pages 7-9) | Strong for measured metabolite change |
| UDP-glucose accumulation | supports | cell wall formation | *Microbacterium sediminis* YLB-01; authors describe UDP-glucose as “a critical factor in cell wall formation” under HP (qiu2024metabolicadaptationsof pages 1-2) | Moderate; biologically grounded but not directly perturbed in this study |
| high-pressure treatment | stimulates | cell division | *Microbacterium sediminis* YLB-01; authors state HP stimulated cell division and changed proteins related to division/peptidoglycan biosynthesis (qiu2024metabolicadaptationsof pages 1-2, qiu2024metabolicadaptationsof pages 7-9) | Moderate; summary-level claim with omics support, limited direct morphology data in excerpt |
| high hydrostatic pressure | bounds/selects | growth-supporting pressure range | Trait-level summary from piezophile definitions and Colwellia examples; e.g., *Colwellia marinimaniae* MTCD1 grows from 80–140 MPa with optimum 120 MPa (peoples2020distinctivegeneand pages 1-2, scoma2021functionalgroupsin pages 5-6) | Strong for trait scope; not a mechanistic intracellular edge |


*Table: This table lists the strongest candidate causal triples for curating the microbial pressure-range trait, emphasizing directly measured responses and clearly marking transcriptomic or inferred edges. It is useful as a compact starting set for TraitMech graph curation and uncertainty triage.*

### Additional evidence notes and source snippets

1. **Pressure → cation accumulation → putative osmotic counterpressure.** In *Hujiaoplasma nucleasis* zrk29, growth rates at 12 and 0.1 MPa were similar. At 12 MPa, genes encoding metal ABC transporters, a P-type ATPase, and a calcium/sodium antiporter were upregulated; intracellular Mg²⁺, K⁺, and Na⁺ were approximately **4–8-fold higher**. The authors propose that ion import increases intracellular osmotic pressure to counter HHP. This is unusually strong multi-omic evidence, but there was no transporter knockout or direct demonstration that the mechanism expands a pressure boundary (zheng2023mechanismsofnucleic pages 7-11).

2. **Pressure → membrane unsaturation.** In the same organism, membrane phospholipids with unsaturated fatty-acid chains increased approximately **2–3-fold** at 12 MPa. Unsaturated PE, PG, PC, and PS species were reported at approximately **231-, 22-, 12-, and 16-fold** greater relative abundance, respectively. The inferred downstream increase in membrane fluidity is biologically plausible but was not directly measured in that experiment (zheng2023mechanismsofnucleic pages 7-11). Across piezophiles, increasing unsaturated or branched-chain lipids with pressure is common but explicitly **not universal** (tamby2023microbialmembranelipid pages 1-2).

3. **Pressure → cell-division bottleneck.** In *Tepidibacter hydrothermalis* SWIR-1, elevated pressure inhibited septal peptidoglycan synthesis and cell division more strongly than elongation, chromosome replication, or segregation. The paper reports that 880-nm infrared irradiation “initiated septal synthesis and alleviated the obstruction,” providing an experimental rescue edge. The result is compelling but specific to a hydrothermal-vent/IR assay and should not be generalized to pressure range across microbes (dai2024illuminatingabacterial pages 1-3).

4. **Pressure → fungal ROS, membrane, wall, and repair programs.** At 15 and 35 MPa, *Schizophyllum commune* 20R-7-F01 grew more slowly and had lower viability than at 0.1 MPa. Omics implicated ethanol/lactate fermentation, oxidoreductase and hydrolase pathways, unsaturated-fatty-acid synthesis, cell-wall-integrity signaling, and DNA repair (zhao2024pressuretolerantsurvivalmechanism pages 1-2). The APE peptidase transcript increased **5.4-fold at 15 MPa** and **6.9-fold at 35 MPa**. At day 5, walls were approximately **0.6 μm thicker at 15 MPa** and **0.8 μm thicker at 35 MPa** than at 0.1 MPa. These are pressure-response/tolerance edges, not demonstrated range-expansion edges; several pathway interpretations rely on known functions from other fungi (zhao2024pressuretolerantsurvivalmechanism pages 6-8).

5. **Pressure → metabolic and envelope remodeling.** *Microbacterium sediminis* YLB-01 was first grown at 28°C to stationary phase and then exposed for seven days to 30 MPa at 4°C. The design therefore measures survival/adaptation after a temperature shift rather than a conventional pressure growth range. Nevertheless, 379 proteins met differential-expression criteria—150 upregulated and 229 downregulated—and UDP-glucose increased from **0.077 ± 0.013 to 0.104 ± 0.019** in normalized units. Lactate and acetate increased, whereas trehalose fell from **1.691 ± 0.233 to 0.401 ± 0.048**. The authors associate these changes with cell division, peptidoglycan synthesis, membrane fluidity, and pressure adaptation (qiu2024metabolicadaptationsof pages 1-2, qiu2024metabolicadaptationsof pages 7-9).

6. **Acute extreme-pressure response is not a growth range.** At 158 MPa, *S. oneidensis* MR-1 regulated **264 of 1,204 tested genes (22%)** after 15 minutes: 195 were upregulated and 69 downregulated. Two of three 2-hour replicates recovered growth after decompression, while the third appeared nonviable. This heterogeneity and the absence of demonstrated multiplication during exposure make the study unsuitable for asserting a 158-MPa growth limit. It is suitable for uncertain stress-response edges involving arginine biosynthesis, membrane reconfiguration, CspG, antioxidant defense, ion transport, repair, and ribosomal suppression (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 5-6).

7. **Comparative-genomic candidates.** Extremely piezophilic *Colwellia* have more basic and hydrophobic proteomes and enrichment in replication/recombination/repair, membrane/cell-wall biogenesis, and motility genes. Variants affecting unsaturated-fatty-acid production and respiration, along with piezophile-associated **nuo** and Tad-pilus operons, are plausible upstream determinants. Because these are comparative associations rather than perturbation results, they should enter a graph as uncertain or hypothesis-level edges (peoples2020distinctivegeneand pages 1-2).

## 4. Proposed core graph architecture

A defensible graph should separate **proximal physical damage**, **adaptive response**, and the final trait:

1. high hydrostatic pressure → increases membrane ordering / perturbs membrane proteins
2. membrane unsaturation remodeling → increases or maintains membrane fluidity
3. maintained membrane function → supports transport, respiration, and growth under HHP
4. high hydrostatic pressure → inhibits septal peptidoglycan synthesis
5. inhibited septal synthesis → inhibits cell division
6. cell-wall synthesis/CWI signaling → maintains envelope integrity
7. high hydrostatic pressure → increases protein, oxidative, and DNA stress
8. chaperone/antioxidant/DNA-repair responses → reduce macromolecular damage
9. cation transport + compatible solutes → maintain intracellular physicochemical homeostasis
10. fermentation/respiration remodeling → maintains ATP and redox balance
11. combined maintenance of membrane, envelope, proteostasis, genome, and energy metabolism → supports growth at a tested pressure
12. demonstrated growth across multiple pressures → defines `traitmech:000005`

Edges 1–10 are mechanistic candidates. Edge 11 is a systems-level inference. Edge 12 is the phenotype-construction rule. At present, very few studies directly show that perturbing one mechanism shifts the measured minimum or maximum pressure, so the graph should not imply that all adaptive responses are proven determinants of range width.

## 5. Recent developments, applications, and expert analysis

### Developments in 2023–2024

Recent work has moved from descriptive taxonomy toward integrated metabolomics, transcriptomics, proteomics, ion quantification, lipidomics, and microscopy. Particularly valuable advances include the quantitative ion/lipid model in wall-less *H. nucleasis*, fungal studies at 15–35 MPa, direct visualization of pressure-impaired septal synthesis, and extreme-pressure transcriptomics relevant to icy ocean worlds (dai2024illuminatingabacterial pages 1-3, zheng2023mechanismsofnucleic pages 7-11, malas2024biologicalfunctionsat pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 1-2, qiu2024metabolicadaptationsof pages 1-2).

The field’s consensus remains that there is no universal single mechanism. Membrane remodeling is recurrent, but its direction and lipid species vary by lineage; low temperature creates substantial cross-adaptation and confounding. Expert reviews therefore recommend explicit pressure–temperature matrices and better methods for cultivating slow-growing obligate piezophiles (tamby2023microbialmembranelipid pages 1-2). Updated ecological definitions likewise emphasize pressure–temperature dependence and competitive growth rather than merely surviving above an arbitrary pressure threshold (scoma2021functionalgroupsin pages 5-6).

### Current and prospective applications

- **Deep-ocean cultivation and biogeochemistry:** pressure-resolved growth ranges improve cultivation of otherwise missed deep-biosphere organisms and interpretation of carbon, nitrogen, sulfur, and nucleic-acid turnover.
- **Astrobiology:** Titan’s modeled upper-ocean pressure is ≥150 MPa, while the currently demonstrated microbial growth ceiling cited in recent literature is 140 MPa. Acute survival at 158 MPa informs habitability hypotheses but does not erase the distinction between survival and reproduction (malas2024biologicalfunctionsat pages 1-2).
- **High-pressure food processing:** cell-division, membrane, ribosome, proteostasis, and recovery mechanisms can inform pressure-treatment schedules and explain sublethal recovery. Survival data should remain separate from ecological growth ranges.
- **Industrial biotechnology:** pressure can alter fermentation, redox balance, membrane permeability, and metabolite production, potentially enabling high-pressure bioprocessing or selection of robust chassis.
- **Biosignatures and environmental monitoring:** membrane-lipid profiles may indicate pressure adaptation, although temperature and phylogeny prevent simple one-lipid/one-trait interpretation (tamby2023microbialmembranelipid pages 1-2).
- **Microfluidics and high-pressure microscopy:** continuous in-situ growth measurements can avoid decompression artifacts and more accurately locate both range boundaries.

## 6. Curation recommendations and warnings

### Suitable now

- Curate the MTCD1 pressure range as **80–140 MPa at 6°C**, with optimum pressure represented separately.
- Attach temperature, medium, atmosphere, duration, and growth metric to every range assertion.
- Curate direct response edges such as pressure → increased unsaturated phospholipids, pressure → increased intracellular cations, and pressure → inhibited septal synthesis with organism and assay qualifiers.
- Represent omics-derived mechanisms with an uncertainty/evidence code such as `associated_with`, `upregulates`, or `inferred_to_support`, rather than an unqualified `causes pressure range`.

### Do not yet curate as established range determinants

- Survival or post-decompression regrowth at 158 MPa as growth at 158 MPa.
- A single positive-growth pressure as a complete bounded range.
- Isolation depth as minimum, optimum, or maximum growth pressure.
- Transcript abundance alone as proof that a pathway expands the pressure range.
- Unsaturated-fatty-acid increase as universal across piezophiles.
- Fungal genes inferred from *Saccharomyces* functions as experimentally validated mechanisms in *Schizophyllum*.
- The 2024 electrostatic-interaction study as definitive until peer-reviewed; it is a bioRxiv preprint (makhatadze2024modulationofelectrostatic pages 1-3).
- Generic gene nodes without strain-specific locus or protein identifiers.
- Conflation of hydrostatic pressure with osmotic pressure; in the zrk29 model, osmotic pressure is a proposed intracellular counter-response, not the environmental variable.

## 7. DOI-first bibliography

1. Zheng R. et al. “Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium.” *mBio* 14. **Published 8 August 2023.** DOI: [10.1128/mbio.00958-23](https://doi.org/10.1128/mbio.00958-23) (zheng2023mechanismsofnucleic pages 1-3, zheng2023mechanismsofnucleic pages 7-11).
2. Tamby A., Sinninghe Damsté J.S., Villanueva L. “Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment.” *Frontiers in Molecular Biosciences* 9. **Published 6 January 2023.** DOI: [10.3389/fmolb.2022.1058381](https://doi.org/10.3389/fmolb.2022.1058381) (tamby2023microbialmembranelipid pages 1-2).
3. Zhong M. et al. “Insight into the adaptation mechanisms of high hydrostatic pressure in physiology and metabolism of hadal fungi from the deepest ocean sediment.” *mSystems* 9. **January 2024.** DOI: [10.1128/msystems.01085-23](https://doi.org/10.1128/msystems.01085-23) (zhong2024insightintothe pages 1-2).
4. Qiu X. et al. “Metabolic adaptations of *Microbacterium sediminis* YLB-01 in deep-sea high-pressure environments.” *Applied Microbiology and Biotechnology* 108:170. **Published 24 January 2024.** DOI: [10.1007/s00253-023-12906-5](https://doi.org/10.1007/s00253-023-12906-5) (qiu2024metabolicadaptationsof pages 1-2, qiu2024metabolicadaptationsof pages 7-9).
5. Malas J. et al. “Biological functions at high pressure: transcriptome response of *Shewanella oneidensis* MR-1 to hydrostatic pressure relevant to Titan and other icy ocean worlds.” *Frontiers in Microbiology* 15. **Published 13 February 2024.** DOI: [10.3389/fmicb.2024.1293928](https://doi.org/10.3389/fmicb.2024.1293928) (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 5-6).
6. Dai J. et al. “Illuminating a bacterial adaptation mechanism: infrared-driven cell division in deep-sea hydrothermal vent environments.” *The Innovation Geoscience* 2:100050. **Published online 21 February 2024.** DOI: [10.59717/j.xinn-geo.2024.100050](https://doi.org/10.59717/j.xinn-geo.2024.100050) (dai2024illuminatingabacterial pages 1-3).
7. Zhao M. et al. “Pressure-tolerant survival mechanism of *Schizophyllum commune* 20R-7-F01 isolated from deep sediments 2 kilometers below the seafloor.” *Frontiers in Marine Science* 11. **Published 11 November 2024.** DOI: [10.3389/fmars.2024.1471465](https://doi.org/10.3389/fmars.2024.1471465) (zhao2024pressuretolerantsurvivalmechanism pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8).
8. Peoples L.M. et al. “Distinctive gene and protein characteristics of extremely piezophilic *Colwellia*.” *BMC Genomics* 21. **October 2020.** DOI: [10.1186/s12864-020-07102-y](https://doi.org/10.1186/s12864-020-07102-y) (peoples2020distinctivegeneand pages 1-2).
9. Scoma A. “Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature.” *ISME Journal* 15:1871–1878. **March 2021.** DOI: [10.1038/s41396-021-00930-0](https://doi.org/10.1038/s41396-021-00930-0) (scoma2021functionalgroupsin pages 5-6).
10. Kusube M. et al. “*Colwellia marinimaniae* sp. nov., a hyperpiezophilic species isolated from an amphipod within the Challenger Deep, Mariana Trench.” *International Journal of Systematic and Evolutionary Microbiology* 67:824–831. **April 2017.** DOI: [10.1099/ijsem.0.001671](https://doi.org/10.1099/ijsem.0.001671). The MTCD1 range is independently summarized in the comparative-genomics evidence (peoples2020distinctivegeneand pages 1-2).
11. Makhatadze G.I. “Modulation of Electrostatic Interactions as a Mechanism of Cryptic Adaptation of *Colwellia* to High Hydrostatic Pressure.” bioRxiv. **July 2024; preprint.** DOI: [10.1101/2024.07.28.605522](https://doi.org/10.1101/2024.07.28.605522) (makhatadze2024modulationofelectrostatic pages 1-3).

References

1. (makhatadze2024modulationofelectrostatic pages 1-3): George I. Makhatadze. Modulation of electrostatic interactions as a mechanism of cryptic adaptation of colwellia to high hydrostatic pressure. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.28.605522, doi:10.1101/2024.07.28.605522. This article has 1 citations.

2. (peoples2020distinctivegeneand pages 1-2): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 56 citations and is from a peer-reviewed journal.

3. (scoma2021functionalgroupsin pages 5-6): Alberto Scoma. Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. The ISME Journal, 15:1871-1878, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00930-0, doi:10.1038/s41396-021-00930-0. This article has 18 citations.

4. (tamby2023microbialmembranelipid pages 1-2): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 52 citations.

5. (malas2024biologicalfunctionsat pages 1-2): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 9 citations and is from a peer-reviewed journal.

6. (malas2024biologicalfunctionsat pages 5-6): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 9 citations and is from a peer-reviewed journal.

7. (dai2024illuminatingabacterial pages 1-3): Jie Dai, Xue-Gong Li, Tian-Yuan Zhang, Hong Chen, Wei-Jia Zhang, Denghui Li, Jia Liu, Jianwei Chen, Yuan Lu, and Long-Fei Wu. Illuminating a bacterial adaptation mechanism: infrared-driven cell division in deep-sea hydrothermal vent environments. The Innovation Geoscience, 2:100050, Jan 2024. URL: https://doi.org/10.59717/j.xinn-geo.2024.100050, doi:10.59717/j.xinn-geo.2024.100050. This article has 5 citations and is from a peer-reviewed journal.

8. (zheng2023mechanismsofnucleic pages 7-11): Rikuan Zheng, Chong Wang, Ruining Cai, Yeqi Shan, and Chaomin Sun. Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.00958-23, doi:10.1128/mbio.00958-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

9. (zhao2024pressuretolerantsurvivalmechanism pages 1-2): Mengshi Zhao, Dongxu Li, Jie Liu, Jiasong Fang, and Changhong Liu. Pressure-tolerant survival mechanism of schizophyllum commune 20r-7-f01 isolated from deep sediments 2 kilometers below the seafloor. Frontiers in Marine Science, Nov 2024. URL: https://doi.org/10.3389/fmars.2024.1471465, doi:10.3389/fmars.2024.1471465. This article has 6 citations.

10. (zhao2024pressuretolerantsurvivalmechanism pages 6-8): Mengshi Zhao, Dongxu Li, Jie Liu, Jiasong Fang, and Changhong Liu. Pressure-tolerant survival mechanism of schizophyllum commune 20r-7-f01 isolated from deep sediments 2 kilometers below the seafloor. Frontiers in Marine Science, Nov 2024. URL: https://doi.org/10.3389/fmars.2024.1471465, doi:10.3389/fmars.2024.1471465. This article has 6 citations.

11. (qiu2024metabolicadaptationsof pages 1-2): Xu Qiu, Xiao-Min Hu, Xi-Xiang Tang, Cai-Hua Huang, Hua-Hua Jian, and Dong-Hai Lin. Metabolic adaptations of microbacterium sediminis ylb-01 in deep-sea high-pressure environments. Applied Microbiology and Biotechnology, 108:1-15, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12906-5, doi:10.1007/s00253-023-12906-5. This article has 11 citations and is from a domain leading peer-reviewed journal.

12. (qiu2024metabolicadaptationsof pages 7-9): Xu Qiu, Xiao-Min Hu, Xi-Xiang Tang, Cai-Hua Huang, Hua-Hua Jian, and Dong-Hai Lin. Metabolic adaptations of microbacterium sediminis ylb-01 in deep-sea high-pressure environments. Applied Microbiology and Biotechnology, 108:1-15, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12906-5, doi:10.1007/s00253-023-12906-5. This article has 11 citations and is from a domain leading peer-reviewed journal.

13. (zheng2023mechanismsofnucleic pages 1-3): Rikuan Zheng, Chong Wang, Ruining Cai, Yeqi Shan, and Chaomin Sun. Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.00958-23, doi:10.1128/mbio.00958-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

14. (zhong2024insightintothe pages 1-2): Maosheng Zhong, Yongqi Li, Ludan Deng, Jiasong Fang, and Xi Yu. Insight into the adaptation mechanisms of high hydrostatic pressure in physiology and metabolism of hadal fungi from the deepest ocean sediment. Jan 2024. URL: https://doi.org/10.1128/msystems.01085-23, doi:10.1128/msystems.01085-23. This article has 17 citations and is from a peer-reviewed journal.