---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:03:32.900679'
end_time: '2026-08-04T03:14:48.132540'
duration_seconds: 675.23
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: piezotolerant
  trait_identifier: traitmech:000003
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: piezotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pressure growth preference in which an organism can grow under elevated
    hydrostatic pressure but grows at similar or faster rates at atmospheric pressure
    (0.1 MPa).
  parent_traits: METPO:1000059
  synonyms: barotolerant
  evidence_summary: 'DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP
    are usually known as piezophiles, referring to their preference for high pressure
    (Pressure-adaptation review distinguishes piezotolerant organisms, which withstand
    high hydrostatic pressure but grow at similar or faster rates at atmospheric pressure,
    from obligate piezophiles.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140
    MPa (optimum, 120 MPa) at 6 degrees C (Provides the contrasting obligate-piezophile
    reference point against which piezotolerant (atmospheric-capable) growth is defined.)'
  causal_graph_summary: 'piezotolerance_pressure_range: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 58
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** piezotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism can grow under elevated hydrostatic pressure but grows at similar or faster rates at atmospheric pressure (0.1 MPa).
- **Parent traits:** METPO:1000059
- **Synonyms:** barotolerant
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review distinguishes piezotolerant organisms, which withstand high hydrostatic pressure but grow at similar or faster rates at atmospheric pressure, from obligate piezophiles.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Provides the contrasting obligate-piezophile reference point against which piezotolerant (atmospheric-capable) growth is defined.)
- **Existing causal graph summary:** piezotolerance_pressure_range: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **piezotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/piezotolerant.yaml`.

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
- **Trait label:** piezotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism can grow under elevated hydrostatic pressure but grows at similar or faster rates at atmospheric pressure (0.1 MPa).
- **Parent traits:** METPO:1000059
- **Synonyms:** barotolerant
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review distinguishes piezotolerant organisms, which withstand high hydrostatic pressure but grow at similar or faster rates at atmospheric pressure, from obligate piezophiles.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Provides the contrasting obligate-piezophile reference point against which piezotolerant (atmospheric-capable) growth is defined.)
- **Existing causal graph summary:** piezotolerance_pressure_range: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **piezotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/piezotolerant.yaml`.

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


# Curation report: piezotolerant microbial trait

## Executive recommendation

**Trait:** piezotolerant  
**Trait identifier:** `traitmech:000003`  
**Category/kind:** ENVIRONMENT / CLASS  
**Parent:** `METPO:1000059`  
**Synonym:** barotolerant

The supplied definition is well supported: a piezotolerant organism **grows under elevated hydrostatic pressure (HHP), but grows at a similar or greater rate at atmospheric pressure, approximately 0.1 MPa**. A recent review states that microorganisms are piezotolerant when “they can withstand HHP but have similar or faster growth rates at atmospheric pressure.” In contrast, piezophiles have an elevated-pressure growth optimum, and obligate piezophiles cannot grow at atmospheric pressure. The literature occasionally spells the term “piezolerant,” but “piezotolerant” is the preferred label here. (tamby2023microbialmembranelipid pages 1-2)

The most defensible TraitMech graph should center on **pressure-supported growth**, with mechanistic branches for membrane homeostasis, oxidative-stress control, energy/respiratory reprogramming, proteostasis, and envelope/DNA maintenance. However, most available mechanistic evidence is transcriptomic or metabolomic and therefore supports pressure-response associations, not universal causal requirements. Taxon and assay qualifiers are essential.

## 1. Trait scope and boundaries

### 1.1 Positive operational criterion

A strain should be annotated as `traitmech:000003` only when a growth assay demonstrates all of the following:

1. Replication or biomass increase occurs at one or more pressures above 0.1 MPa.
2. Growth at 0.1 MPa is similar to or faster than growth at elevated pressure.
3. Pressure, temperature, medium, salinity, oxygen availability, electron acceptor, and incubation duration are reported.
4. The result reflects growth during pressurization—not merely metabolic activity, post-decompression recovery, or survival of a short pressure shock.

Pressure and temperature must be modeled jointly because growth rate and the apparent pressure optimum depend on temperature. The usual definition of piezophily is a maximum specific growth rate above 0.1 MPa, but published threshold schemes vary, and pressure–temperature growth surfaces are more informative than a single maximum-pressure value. Only 86 isolates with an elevated-pressure optimum were documented in a 2021 synthesis, illustrating the limited reference set. (scoma2021functionalgroupsin pages 5-6, scoma2021functionalgroupsin pages 1-2)

### 1.2 Nearby traits and boundary cases

| Nearby phenotype | Distinction from piezotolerant |
|---|---|
| **Piezophilic** | Growth is faster or optimal above 0.1 MPa. For example, *Pseudothermotoga elfii* DSM9442 has a 20 MPa optimum and 40 MPa upper limit, whereas the surface strain *P. elfii* subsp. *lettingae* is piezotolerant and grows only up to 20 MPa. (roumagnac2020responsestothe pages 1-2) |
| **Obligately piezophilic / hyperpiezophilic** | Cannot grow at atmospheric pressure; this is outside the target trait. (tamby2023microbialmembranelipid pages 1-2, scoma2021functionalgroupsin pages 5-6) |
| **Conditionally piezophilic** | Pressure preference changes with temperature, salinity, chaotropes, or another condition. *Halomonas titanicae* ANRCS81 grew from 0.1–55 MPa but had its highest measured specific growth rate, 0.082 h⁻¹, at 35 MPa and 37°C; it therefore should not be used as an unqualified piezotolerant exemplar. (li2023strategyforthe pages 2-4, li2023strategyforthe pages 10-12) |
| **Pressure/baroresistant** | Survives an acute pressure treatment but need not grow while pressurized. This includes many food-HPP experiments at 200–400 MPa and *Shewanella oneidensis* exposure at 158 MPa. (malas2024biologicalfunctionsat pages 1-2, duru2021highpressureprocessinginducedtranscriptome pages 13-14, duru2021highpressureprocessinginducedtranscriptome pages 1-2) |
| **Metabolically active under HHP** | Activity does not prove population growth. *S. oneidensis* MR-1 remained active at 158 MPa and grew after decompression, but the experiment did not show growth at 158 MPa. (malas2024biologicalfunctionsat pages 1-2) |
| **Pressure-tolerant but inhibited** | Slower growth at pressure can still qualify if growth occurs. *Schizophyllum commune* 20R-7-F01 grew more slowly and had lower viability at 15 and 35 MPa than at 0.1 MPa, but retained significant pressure tolerance. (zhao2024pressuretolerantsurvivalmechanism pages 1-2) |

### 1.3 Strong recent phenotype exemplar

*Shewanella eurypsychrophilus* YLB-09 is an especially clear candidate: its optimum is 0.1 MPa and 15°C, yet it can grow at 50 MPa. Its 2024 mechanistic experiment compared 23 MPa with 0.1 MPa, making it directly aligned with the target definition. (qiu2024metabolicadaptationsofa pages 1-2)

## 2. Current mechanistic understanding

HHP decreases intermolecular distances and perturbs lipid bilayers, multimeric proteins, nucleic acids, metabolic rates, and membrane-associated transport. Current evidence supports a distributed response rather than a single diagnostic “piezotolerance gene.” (tamby2023microbialmembranelipid pages 1-2, scoma2021functionalgroupsin pages 1-2)

### 2.1 Membrane homeostasis

Pressure generally orders lipid bilayers and decreases fluidity. Many—but not all—pressure-adapted microbes respond by increasing unsaturated, branched-chain, or shorter fatty-acyl chains. The 2023 membrane review explicitly warns that increased unsaturation and branching are **not universal**, and that low-temperature effects are difficult to separate from pressure effects. Polar-headgroup responses can even differ between strains of the same genus. (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 7-9)

In the clearest recent piezotolerant fungal study, 15 and 35 MPa upregulated *FAD2*, *SCD*, and *desC* in *S. commune*, consistent with increased unsaturated-fatty-acid synthesis. The same study upregulated the cell-wall-integrity genes *Mid*, *Rho1*, *Pkc1*, *FKS*, *CHS3*, *Bck1*, and *Slt2*. Cell walls were approximately 0.6 µm thicker at 15 MPa and 0.8 µm thicker at 35 MPa than at 0.1 MPa on day 5. These are strong pressure-response associations but not gene-knockout demonstrations. (zhao2024pressuretolerantsurvivalmechanism pages 6-8)

A 2024 engineering experiment provides intervention evidence that bacterial ether-bonded membrane lipids improve *E. coli* survival after HHP/high-temperature shock. It measures post-shock robustness rather than growth under sustained HHP, so it should inform a neighboring pressure-resistance graph rather than the core piezotolerance phenotype. (tamby2024exploringrobustnessof pages 1-2, tamby2024exploringrobustnessof pages 8-9)

### 2.2 Oxidative-stress defense

HHP-associated oxidative stress is one of the best replicated response modules. At 40 MPa, *H. titanicae* ANRCS81 upregulated antioxidant-defense genes and showed increased superoxide-dismutase activity. Pressure also increased glucose consumption, decreased CO₂ production, and increased nitrate/nitrite consumption and ammonium production. These measurements support a pressure → oxidative/energy response edge, but no antioxidant-gene deletion established necessity for growth. (li2023strategyforthe pages 1-2, li2023strategyforthe pages 10-12)

In *S. commune*, 15 and 35 MPa significantly upregulated *Yap1, MET, GLT, GSS, GST, SOD, katE, CAT, catB,* and *srpA*. The authors also observed 5.4-fold and 6.9-fold induction of the damaged-protein peptidase gene *APE* at 15 and 35 MPa, respectively. This suggests coordinated ROS detoxification, glutathione/cysteine metabolism, and removal of damaged proteins. It remains taxon-specific omics evidence. (zhao2024pressuretolerantsurvivalmechanism pages 6-8)

### 2.3 Energy metabolism and alternative respiration

The strongest 2024 piezotolerant bacterial model shows a pressure-dependent shift away from aerobic energy metabolism. In *S. eurypsychrophilus* YLB-09, 23 MPa downregulated the TCA cycle, pyruvate metabolism, and oxidative phosphorylation, with lower citrate, succinate, and acetate. Glycolysis/gluconeogenesis genes were generally upregulated. Concurrently, *torS, torR, torC, torA, torD,* and *torT* were significantly upregulated and TMAO was depleted, supporting activation of TMAO respiration. This is integrated transcriptomic–metabolomic evidence, but genetic disruption of the *tor* system is still needed to prove that it causes piezotolerant growth. (qiu2024metabolicadaptationsofa pages 1-2, qiu2024metabolicadaptationsofa pages 8-11)

*H. titanicae* similarly upregulated anaerobic respiration and fermentation at 40 MPa, accompanied by increased nitrate/nitrite consumption and ammonium generation. Candidate compatible solutes predicted from its genome include ectoine, glycine betaine, and glutamate, but their pressure-dependent accumulation and necessity were not established. (li2023strategyforthe pages 1-2, li2023strategyforthe pages 10-12)

Anaerobic *S. commune* apparently uses both ethanol and lactate fermentation under HHP. The proposed benefit—greater energy production—is biologically plausible but inferred from pathway activation, not directly tested by pathway disruption. (zhao2024pressuretolerantsurvivalmechanism pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8)

### 2.4 Proteostasis and transcriptional stress control

The laboratory-evolved *E. coli* AN62 strain grows up to 62 MPa. Pressure shock upregulated *rpoH, rpoE, dnaK,* and *groEL* in both AN62 and its pressure-sensitive parent. AN62 showed greater *groEL* than *dnaK* promoter induction and highly stochastic *rpoE* induction. AN62 has 17 mutations, including *rpoB* Q148H and a *rho* mutation, but the authors explicitly state that the role of *rpoB* in high-pressure growth remains to be tested. AN62 also contains 20.02% 18:1ω7c fatty acid versus 9.5% in the parent, potentially reducing pressure-induced membrane stress. (coffin2024responseandadaptation pages 1-2, coffin2024responseandadaptation pages 11-12)

Thus, chaperones and sigma-factor signaling are suitable candidate nodes, but the edges should be represented as “pressure induces expression of” rather than “causes piezotolerance” until clean allelic replacement or deletion/complementation experiments are available.

### 2.5 Cell-wall and DNA repair

In food-HPP recovery experiments, *Listeria monocytogenes* exposed to 200 or 400 MPa for 8 minutes upregulated *murG, murC,* and *pbp2A* while downregulating *divIC, divIVA, ftsE,* and *ftsX*. A *pbp2A* deletion increased HHP sensitivity, making Pbp2A-supported peptidoglycan repair one of the few genetic-intervention-supported edges in this literature. Nevertheless, the assay concerns recovery after acute food-processing pressure, not sustained environmental growth, so this edge should be placed in a reusable pressure-damage-repair module rather than asserted as a defining piezotolerance mechanism. (duru2021highpressureprocessinginducedtranscriptome pages 13-14, duru2021highpressureprocessinginducedtranscriptome pages 1-2)

*S. commune* upregulated DNA-repair pathways and cell-wall-integrity signaling under 15–35 MPa. This supports pressure → DNA-damage response and pressure → envelope-maintenance edges, but not yet a causal connection to growth. (zhao2024pressuretolerantsurvivalmechanism pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8)

## 3. Candidate graph nodes

### Environmental and experimental nodes

- **Elevated hydrostatic pressure** — label-only unless the project already has a validated ENVO/METPO term.
- **Atmospheric pressure, 0.1 MPa** — reference condition.
- **Pressure magnitude**, **temperature**, **exposure duration**, **compression/decompression rate**, **oxygen availability**, **salinity**, **growth medium**, and **electron acceptor** — assay-context nodes or qualifiers.
- **Anaerobic condition**; **low temperature** — important interacting environmental factors.
- **Pressure shock / HPP treatment** — separate from sustained elevated-pressure growth.

### Phenotype/process nodes

- Piezotolerant growth — `traitmech:000003`.
- Response to oxidative stress — `GO:0006979`.
- DNA repair — `GO:0006281`.
- Protein folding — `GO:0006457`.
- Glycolysis — `GO:0006096`.
- Oxidative phosphorylation — `GO:0006119`.
- Anaerobic respiration — `GO:0009061`.
- Peptidoglycan biosynthetic process — `GO:0009252`.
- Membrane-fluidity homeostasis, cell-wall-integrity signaling, TMAO respiration, nitrate respiration, ethanol fermentation, lactate fermentation, and compatible-solute accumulation — retain as label-only candidates until identifiers are independently validated.

### Genes and proteins

- Antioxidant module: *SOD/sod*, *katE, CAT, catB, srpA, Yap1, MET, GLT, GSS,* and *GST*.
- Membrane module: *FAD2, SCD, desC, fabH2*; OmpH as a comparative pressure-responsive outer-membrane protein.
- Cell-wall module: *Mid, Rho1, Pkc1, FKS, CHS3, Bck1, Slt2, murG, murC,* and *pbp2A*.
- Respiratory module: *torS, torR, torC, torA, torD,* and *torT*; nitrate-reductase systems as taxon-specific candidates.
- Proteostasis/regulation: *rpoH, rpoE, dnaK, groEL, APE, rpoB,* and *rho*.
- Arginine response: *argA, argB, argC, argF,* and *argR*—currently better supported for acute 158 MPa survival than sustained piezotolerant growth. (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 9-10)

### Chemicals and cellular structures

- Hydrogen peroxide — `CHEBI:16240`.
- Dioxygen — `CHEBI:15379`.
- Water — `CHEBI:15377`.
- ATP — `CHEBI:15422`.
- NADH — `CHEBI:16411`.
- Carbon dioxide — `CHEBI:16526`.
- TMAO, nitrate, nitrite, ammonium, glucose, lactate, ethanol, citrate, succinate, acetate, ectoine, glycine betaine, glutamate, cysteine, glutathione, unsaturated fatty acids, branched-chain fatty acids, and phosphatidylethanolamine — label-only here because exact CURIEs were not independently verified in this run.
- Cytoplasmic membrane, outer membrane, periplasm, cell wall, peptidoglycan, and fungal chitin/β-1,3-glucan layer — candidate localization/structure nodes.

## 4. Candidate causal edges

The table below prioritizes curation-ready triples while explicitly distinguishing interventions from associations.

| subject | predicate | object | taxon/assay | evidence grade | DOI |
|---|---|---|---|---|---|
| elevated high hydrostatic pressure (40 MPa) | induces/upregulates | antioxidant defense, including increased SOD activity | *Halomonas titanicae* ANRCS81; growth under 0.1–55 MPa, transcriptomics + enzyme assay at 40 MPa | measured physiology + omics association; taxon-specific (li2023strategyforthe pages 1-2, li2023strategyforthe pages 10-12) | 10.1128/AEM.01304-22 |
| elevated high hydrostatic pressure | upregulates | *torS*, *torR*, *torC*, *torA*, *torD*, *torT* | *Shewanella eurypsychrophilus* YLB-09; pressure-tolerant strain, 23 MPa vs 0.1 MPa transcriptomics | omics association; taxon/assay-specific (qiu2024metabolicadaptationsofa pages 1-2, qiu2024metabolicadaptationsofa pages 8-11) | 10.3389/fmicb.2024.1467153 |
| upregulated *torS/torR/torC/torA/torD/torT* under elevated pressure | associated with activation of | TMAO respiration | *Shewanella eurypsychrophilus* YLB-09; transcriptomics plus TMAO substrate depletion under high pressure | omics + metabolite association; moderate causal support, not intervention (qiu2024metabolicadaptationsofa pages 8-11) | 10.3389/fmicb.2024.1467153 |
| elevated high hydrostatic pressure | downregulates | TCA cycle and oxidative phosphorylation | *Shewanella eurypsychrophilus* YLB-09; 23 MPa vs 0.1 MPa, integrated transcriptomics/metabolomics | omics association; taxon-specific (qiu2024metabolicadaptationsofa pages 1-2, qiu2024metabolicadaptationsofa pages 8-11) | 10.3389/fmicb.2024.1467153 |
| elevated high hydrostatic pressure | upregulates | glycolysis/gluconeogenesis | *Shewanella eurypsychrophilus* YLB-09; 23 MPa vs 0.1 MPa transcriptomics | omics association; taxon-specific (qiu2024metabolicadaptationsofa pages 8-11) | 10.3389/fmicb.2024.1467153 |
| elevated high hydrostatic pressure | upregulates | ROS-defense genes (*Yap1, MET, GLT, GSS, GST, SOD, katE, CAT, catB, srpA*) | *Schizophyllum commune* 20R-7-F01; 15 and 35 MPa vs 0.1 MPa, anaerobic transcriptomics | omics association; taxon-specific (zhao2024pressuretolerantsurvivalmechanism pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8) | 10.3389/fmars.2024.1471465 |
| elevated high hydrostatic pressure | upregulates | unsaturated-fatty-acid synthesis genes (*FAD2, SCD, desC*) | *Schizophyllum commune* 20R-7-F01; 15 and 35 MPa vs 0.1 MPa transcriptomics | omics association; inferred membrane-fluidity role with caveat (zhao2024pressuretolerantsurvivalmechanism pages 6-8) | 10.3389/fmars.2024.1471465 |
| elevated high hydrostatic pressure | upregulates | cell-wall-integrity pathway genes (*Mid, Rho1, Pkc1, FKS, CHS3, Bck1, Slt2*) | *Schizophyllum commune* 20R-7-F01; 15 and 35 MPa vs 0.1 MPa transcriptomics, thicker walls by TEM | omics association + morphology; taxon-specific (zhao2024pressuretolerantsurvivalmechanism pages 6-8) | 10.3389/fmars.2024.1471465 |
| elevated high hydrostatic pressure | activates/upregulates | DNA repair pathway | *Schizophyllum commune* 20R-7-F01; 15 and 35 MPa vs 0.1 MPa transcriptomics | omics association; taxon-specific (zhao2024pressuretolerantsurvivalmechanism pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8) | 10.3389/fmars.2024.1471465 |
| pressure shock | upregulates | *rpoH*, *rpoE*, *dnaK*, *groEL* | laboratory-evolved piezotolerant *Escherichia coli* AN62 and parental MG1655; GFP promoter fusions after pressure shock | direct transcriptional reporter evidence; pressure-shock survival/growth-adaptation context, not deep-sea growth assay (coffin2024responseandadaptation pages 1-2) | 10.3389/fmicb.2024.1470617 |
| increased unsaturated/branched fatty acids | supports | membrane fluidity under elevated pressure | review across piezophiles/piezotolerant microbes; comparative membrane literature | review-level comparative support; not universal, curate as uncertain/generalized (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 7-9) | 10.3389/fmolb.2022.1058381 |
| *pbp2A* | supports | HPP resistance | *Listeria monocytogenes* during recovery after 200/400 MPa HPP at 8°C; deletion mutant more sensitive | intervention/genetic evidence; HPP recovery trait, not environmental piezotolerant growth (duru2021highpressureprocessinginducedtranscriptome pages 1-2) | 10.1186/s12864-021-07407-6 |
| bacterial ether-bonded membrane lipids | increase | post-shock robustness under HHP | engineered *E. coli*; survival after 50 MPa shock and/or high temperature | intervention/engineering evidence for shock robustness, not growth under elevated pressure (tamby2024exploringrobustnessof pages 1-2, tamby2024exploringrobustnessof pages 8-9) | 10.3389/fmicb.2024.1470844 |


*Table: This table lists compact, curation-ready candidate causal edges for microbial piezotolerance and closely related pressure-response phenotypes. It highlights which edges are backed by intervention versus omics association, helping prioritize what is strongest for TraitMech curation.*

### Recommended first-pass YAML core

The highest-confidence environmental-growth backbone is:

1. **elevated hydrostatic pressure — permits growth of → piezotolerant organism**, qualified by strain, pressure, temperature, medium, and growth rate.
2. **atmospheric pressure — supports equal-or-faster growth of → piezotolerant organism**.
3. **elevated hydrostatic pressure — decreases → membrane fluidity**; this is a well-established physicochemical effect, but its biological magnitude is membrane-dependent. (tamby2023microbialmembranelipid pages 1-2, malas2024biologicalfunctionsat pages 9-10)
4. **elevated hydrostatic pressure — induces → oxidative-stress response** in named strains. (li2023strategyforthe pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8)
5. **elevated hydrostatic pressure — induces → membrane-lipid remodeling** in named strains, marked non-universal. (tamby2023microbialmembranelipid pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8)
6. **elevated hydrostatic pressure — induces → alternative respiratory/fermentative energy metabolism** in named strains. (li2023strategyforthe pages 1-2, qiu2024metabolicadaptationsofa pages 8-11)
7. **elevated hydrostatic pressure — induces → proteostasis and macromolecular-repair responses** in named strains. (coffin2024responseandadaptation pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 1-2)

Do not collapse these into a universal linear pathway. A better graph topology is parallel pressure-response modules converging on membrane integrity, redox balance, ATP conservation, proteome maintenance, and ultimately growth under HHP.

## 5. Recent developments and applications

### 5.1 2023–2024 research advances

Recent work has expanded the field beyond classical deep-sea bacteria:

- A 2024 hadal-fungus study implicated HOG-MAPK signaling, cell-cycle arrest, cell-wall remodeling, unsaturated fatty acids, amino-acid metabolism, heat-shock proteins, and DNA repair in *Aspergillus sydowii* DM1. However, growth remained poor under HHP despite active metabolism, so several proposed mechanisms remain transcriptomic interpretations. (zhong2024insightintothe pages 15-17)
- The 2024 *S. commune* study integrated viability, biomass, TEM, transcriptomics, and metabolomics, providing unusually broad evidence for fungal piezotolerance at 15 and 35 MPa. (zhao2024pressuretolerantsurvivalmechanism pages 1-2, zhao2024pressuretolerantsurvivalmechanism pages 6-8)
- The 2024 YLB-09 study linked actual piezotolerant growth to TMAO-respiratory reprogramming at 23 MPa. (qiu2024metabolicadaptationsofa pages 1-2, qiu2024metabolicadaptationsofa pages 8-11)
- Single-cell promoter measurements in 2024 distinguished the heat-shock response of laboratory-evolved AN62 from its parental *E. coli*, generating testable hypotheses about RpoE membrane sensing and altered RNA-polymerase function. (coffin2024responseandadaptation pages 1-2, coffin2024responseandadaptation pages 11-12)
- Extreme-pressure astrobiology experiments found 264 differentially expressed genes after 15 minutes at 158 MPa in *S. oneidensis*; *argA, argB, argC,* and *argF* had log₂-fold changes of 2.7, 4.6, 4.5, and 4.0. This informs acute survival at modeled Titan-ocean pressures, not the target growth trait. (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 9-10)

### 5.2 Real-world applications

1. **High-pressure food processing.** Pressure-tolerant pathogens can recover after HPP, making envelope repair, proteostasis, and strain heterogeneity important for process validation. In *Listeria*, HPP recovery activated SigB, PTS transport, protein folding, cobalamin synthesis, and cell-wall repair; *pbp2A* deletion increased sensitivity. (duru2021highpressureprocessinginducedtranscriptome pages 13-14, duru2021highpressureprocessinginducedtranscriptome pages 1-2)
2. **Deep-sea biogeochemistry.** Pressure-driven changes in nitrate, TMAO, DMSO, and fermentative metabolism can alter carbon and nitrogen fluxes. The ANRCS81 and YLB-09 studies directly connect HHP to nitrate/nitrite turnover and TMAO depletion, respectively. (li2023strategyforthe pages 1-2, qiu2024metabolicadaptationsofa pages 8-11)
3. **High-pressure biotechnology.** Pressure-stable enzymes, membranes, and production organisms could support bioprocesses under conditions that improve gas solubility or suppress contaminants. Current mechanistic understanding remains too taxon-specific for a universal engineering recipe.
4. **Astrobiology.** Survival and transcription at 158 MPa indicate that modeled icy-ocean pressures may not be intrinsically sterilizing, although post-pressure growth is not evidence of in situ proliferation. (malas2024biologicalfunctionsat pages 1-2)

## 6. Warnings: claims not ready for TraitMech curation

- **Do not equate survival with piezotolerance.** Acute 50–400 MPa shock studies and growth after decompression belong to pressure resistance unless in-pressure growth is demonstrated. (tamby2024exploringrobustnessof pages 1-2, malas2024biologicalfunctionsat pages 1-2, duru2021highpressureprocessinginducedtranscriptome pages 1-2)
- **Do not use maximum tolerated pressure alone.** The defining comparison is the growth-rate relationship between elevated pressure and 0.1 MPa.
- **Do not curate ANRCS81 as unqualified piezotolerant.** Its measured optimum was 35 MPa under the reported condition, making “conditional piezophile” more accurate. (li2023strategyforthe pages 2-4)
- **Do not assert that unsaturated fatty acids universally cause piezotolerance.** Lipid responses differ among taxa, and cold adaptation is a major confounder. (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 7-9)
- **Do not treat differential expression as necessity or sufficiency.** Most *tor*, antioxidant, fermentation, HOG-MAPK, cell-wall, and DNA-repair edges lack targeted deletion and complementation.
- **Do not curate the *rpoB* Q148H mutation as causal.** Its role in AN62 pressure growth is explicitly hypothetical and awaits testing. (coffin2024responseandadaptation pages 11-12)
- **Do not curate arginine biosynthesis as a proven piezotolerance mechanism.** The 158 MPa study measured short exposure, and metabolite-level accumulation and function remain unverified. (malas2024biologicalfunctionsat pages 9-10)
- **Do not generalize fungal mechanisms to bacteria or archaea.** Fungal walls, organelles, signaling, and fermentation architecture warrant taxon-specific graph branches.
- **Account for decompression artifacts.** Membrane composition and expression can change during sample recovery; fixation or sampling under pressure is preferable. (tamby2023microbialmembranelipid pages 7-9)

## 7. DOI-first bibliography

1. Tamby A, Sinninghe Damsté JS, Villanueva L. **Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment.** *Frontiers in Molecular Biosciences*. Published 6 January 2023. DOI: [10.3389/fmolb.2022.1058381](https://doi.org/10.3389/fmolb.2022.1058381). (tamby2023microbialmembranelipid pages 1-2)
2. Qiu X, Tang X. **Metabolic adaptations of *Shewanella eurypsychrophilus* YLB-09 for survival in the high-pressure environment of the deep sea.** *Frontiers in Microbiology*. Published 17 October 2024. DOI: [10.3389/fmicb.2024.1467153](https://doi.org/10.3389/fmicb.2024.1467153). (qiu2024metabolicadaptationsofa pages 1-2)
3. Zhao M et al. **Pressure-tolerant survival mechanism of *Schizophyllum commune* 20R-7-F01 isolated from deep sediments 2 kilometers below the seafloor.** *Frontiers in Marine Science*. Published 11 November 2024. DOI: [10.3389/fmars.2024.1471465](https://doi.org/10.3389/fmars.2024.1471465). (zhao2024pressuretolerantsurvivalmechanism pages 1-2)
4. Li J, Xiao X, Zhou M, Zhang Y. **Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain *Halomonas titanicae* ANRCS81.** *Applied and Environmental Microbiology*. Published March 2023. DOI: [10.1128/AEM.01304-22](https://doi.org/10.1128/AEM.01304-22). (li2023strategyforthe pages 1-2)
5. Zhong M et al. **Insight into the adaptation mechanisms of high hydrostatic pressure in physiology and metabolism of hadal fungi from the deepest ocean sediment.** *mSystems*. Published January 2024. DOI: [10.1128/msystems.01085-23](https://doi.org/10.1128/msystems.01085-23). (zhong2024insightintothe pages 15-17)
6. Coffin CH et al. **Response and adaptation of the transcriptional heat shock response to pressure.** *Frontiers in Microbiology*. Published 18 November 2024. DOI: [10.3389/fmicb.2024.1470617](https://doi.org/10.3389/fmicb.2024.1470617). (coffin2024responseandadaptation pages 1-2)
7. Malas J et al. **Biological functions at high pressure: transcriptome response of *Shewanella oneidensis* MR-1 to hydrostatic pressure relevant to Titan and other icy ocean worlds.** *Frontiers in Microbiology*. Published 13 February 2024. DOI: [10.3389/fmicb.2024.1293928](https://doi.org/10.3389/fmicb.2024.1293928). (malas2024biologicalfunctionsat pages 1-2)
8. Tamby A, Sahonero-Canavesi DX, Villanueva L. **Exploring robustness of hybrid membranes under high hydrostatic pressure and temperature.** *Frontiers in Microbiology*. Published 14 November 2024. DOI: [10.3389/fmicb.2024.1470844](https://doi.org/10.3389/fmicb.2024.1470844). (tamby2024exploringrobustnessof pages 1-2)
9. Scheffer G, Gieg LM. **The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface.** *Microorganisms*. Published June 2023. DOI: [10.3390/microorganisms11071629](https://doi.org/10.3390/microorganisms11071629). (scheffer2023themysteryof pages 7-9)
10. Scoma A. **Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature.** *ISME Journal*. Published 29 March 2021. DOI: [10.1038/s41396-021-00930-0](https://doi.org/10.1038/s41396-021-00930-0). (scoma2021functionalgroupsin pages 1-2)
11. Roumagnac M et al. **Responses to the hydrostatic pressure of surface and subsurface strains of *Pseudothermotoga elfii*.** *Frontiers in Microbiology*. Published December 2020. DOI: [10.3389/fmicb.2020.588771](https://doi.org/10.3389/fmicb.2020.588771). (roumagnac2020responsestothe pages 1-2)
12. Duru IC et al. **High-pressure processing-induced transcriptome response during recovery of *Listeria monocytogenes*.** *BMC Genomics*. Published February 2021. DOI: [10.1186/s12864-021-07407-6](https://doi.org/10.1186/s12864-021-07407-6). (duru2021highpressureprocessinginducedtranscriptome pages 1-2)

## Curation conclusion

`traitmech:000003` is ready for a **modular, taxon-qualified causal graph**, but not for a universal gene signature. The best immediate additions are phenotype-assay nodes that encode growth at elevated pressure relative to 0.1 MPa, followed by strain-specific pressure-response modules for membrane remodeling, antioxidant defense, alternative respiration/fermentation, proteostasis, and cell-envelope/DNA repair. Only intervention-supported edges—such as Pbp2A promoting HPP resistance—should use strong causal predicates, and even those must be segregated when the assay measures acute shock recovery rather than environmental piezotolerant growth.

References

1. (tamby2023microbialmembranelipid pages 1-2): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 52 citations.

2. (scoma2021functionalgroupsin pages 5-6): Alberto Scoma. Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. The ISME Journal, 15:1871-1878, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00930-0, doi:10.1038/s41396-021-00930-0. This article has 18 citations.

3. (scoma2021functionalgroupsin pages 1-2): Alberto Scoma. Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. The ISME Journal, 15:1871-1878, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00930-0, doi:10.1038/s41396-021-00930-0. This article has 18 citations.

4. (roumagnac2020responsestothe pages 1-2): Marie Roumagnac, Nathalie Pradel, Manon Bartoli, Marc Garel, Aaron A. Jones, Fabrice Armougom, Romain Fenouil, Christian Tamburini, Bernard Ollivier, Zarath M. Summers, and Alain Dolla. Responses to the hydrostatic pressure of surface and subsurface strains of pseudothermotoga elfii revealing the piezophilic nature of the strain originating from an oil-producing well. Frontiers in Microbiology, Dec 2020. URL: https://doi.org/10.3389/fmicb.2020.588771, doi:10.3389/fmicb.2020.588771. This article has 21 citations and is from a peer-reviewed journal.

5. (li2023strategyforthe pages 2-4): Jiakang Li, Xiang Xiao, Meng Zhou, and Yu Zhang. Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain halomonas titanicae anrcs81. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01304-22, doi:10.1128/aem.01304-22. This article has 17 citations and is from a peer-reviewed journal.

6. (li2023strategyforthe pages 10-12): Jiakang Li, Xiang Xiao, Meng Zhou, and Yu Zhang. Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain halomonas titanicae anrcs81. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01304-22, doi:10.1128/aem.01304-22. This article has 17 citations and is from a peer-reviewed journal.

7. (malas2024biologicalfunctionsat pages 1-2): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 9 citations and is from a peer-reviewed journal.

8. (duru2021highpressureprocessinginducedtranscriptome pages 13-14): Ilhan Cem Duru, Florentina Ionela Bucur, Margarita Andreevskaya, Bahareh Nikparvar, Anne Ylinen, Leontina Grigore-Gurgu, Tone Mari Rode, Peter Crauwels, Pia Laine, Lars Paulin, Trond Løvdal, Christian U. Riedel, Nadav Bar, Daniela Borda, Anca Ioana Nicolau, and Petri Auvinen. High-pressure processing-induced transcriptome response during recovery of listeria monocytogenes. BMC Genomics, Feb 2021. URL: https://doi.org/10.1186/s12864-021-07407-6, doi:10.1186/s12864-021-07407-6. This article has 51 citations and is from a peer-reviewed journal.

9. (duru2021highpressureprocessinginducedtranscriptome pages 1-2): Ilhan Cem Duru, Florentina Ionela Bucur, Margarita Andreevskaya, Bahareh Nikparvar, Anne Ylinen, Leontina Grigore-Gurgu, Tone Mari Rode, Peter Crauwels, Pia Laine, Lars Paulin, Trond Løvdal, Christian U. Riedel, Nadav Bar, Daniela Borda, Anca Ioana Nicolau, and Petri Auvinen. High-pressure processing-induced transcriptome response during recovery of listeria monocytogenes. BMC Genomics, Feb 2021. URL: https://doi.org/10.1186/s12864-021-07407-6, doi:10.1186/s12864-021-07407-6. This article has 51 citations and is from a peer-reviewed journal.

10. (zhao2024pressuretolerantsurvivalmechanism pages 1-2): Mengshi Zhao, Dongxu Li, Jie Liu, Jiasong Fang, and Changhong Liu. Pressure-tolerant survival mechanism of schizophyllum commune 20r-7-f01 isolated from deep sediments 2 kilometers below the seafloor. Frontiers in Marine Science, Nov 2024. URL: https://doi.org/10.3389/fmars.2024.1471465, doi:10.3389/fmars.2024.1471465. This article has 6 citations.

11. (qiu2024metabolicadaptationsofa pages 1-2): Xu Qiu and Xixiang Tang. Metabolic adaptations of shewanella eurypsychrophilus ylb-09 for survival in the high-pressure environment of the deep sea. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1467153, doi:10.3389/fmicb.2024.1467153. This article has 2 citations and is from a peer-reviewed journal.

12. (tamby2023microbialmembranelipid pages 7-9): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 52 citations.

13. (zhao2024pressuretolerantsurvivalmechanism pages 6-8): Mengshi Zhao, Dongxu Li, Jie Liu, Jiasong Fang, and Changhong Liu. Pressure-tolerant survival mechanism of schizophyllum commune 20r-7-f01 isolated from deep sediments 2 kilometers below the seafloor. Frontiers in Marine Science, Nov 2024. URL: https://doi.org/10.3389/fmars.2024.1471465, doi:10.3389/fmars.2024.1471465. This article has 6 citations.

14. (tamby2024exploringrobustnessof pages 1-2): Anandi Tamby, Diana X. Sahonero-Canavesi, and Laura Villanueva. Exploring robustness of hybrid membranes under high hydrostatic pressure and temperature. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1470844, doi:10.3389/fmicb.2024.1470844. This article has 1 citations and is from a peer-reviewed journal.

15. (tamby2024exploringrobustnessof pages 8-9): Anandi Tamby, Diana X. Sahonero-Canavesi, and Laura Villanueva. Exploring robustness of hybrid membranes under high hydrostatic pressure and temperature. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1470844, doi:10.3389/fmicb.2024.1470844. This article has 1 citations and is from a peer-reviewed journal.

16. (li2023strategyforthe pages 1-2): Jiakang Li, Xiang Xiao, Meng Zhou, and Yu Zhang. Strategy for the adaptation to stressful conditions of the novel isolated conditional piezophilic strain halomonas titanicae anrcs81. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.01304-22, doi:10.1128/aem.01304-22. This article has 17 citations and is from a peer-reviewed journal.

17. (qiu2024metabolicadaptationsofa pages 8-11): Xu Qiu and Xixiang Tang. Metabolic adaptations of shewanella eurypsychrophilus ylb-09 for survival in the high-pressure environment of the deep sea. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1467153, doi:10.3389/fmicb.2024.1467153. This article has 2 citations and is from a peer-reviewed journal.

18. (coffin2024responseandadaptation pages 1-2): Carleton H. Coffin, Luke A. Fisher, Sara Crippen, Phoebe Demers, Douglas H. Bartlett, and Catherine A. Royer. Response and adaptation of the transcriptional heat shock response to pressure. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1470617, doi:10.3389/fmicb.2024.1470617. This article has 3 citations and is from a peer-reviewed journal.

19. (coffin2024responseandadaptation pages 11-12): Carleton H. Coffin, Luke A. Fisher, Sara Crippen, Phoebe Demers, Douglas H. Bartlett, and Catherine A. Royer. Response and adaptation of the transcriptional heat shock response to pressure. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1470617, doi:10.3389/fmicb.2024.1470617. This article has 3 citations and is from a peer-reviewed journal.

20. (malas2024biologicalfunctionsat pages 9-10): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 9 citations and is from a peer-reviewed journal.

21. (zhong2024insightintothe pages 15-17): Maosheng Zhong, Yongqi Li, Ludan Deng, Jiasong Fang, and Xi Yu. Insight into the adaptation mechanisms of high hydrostatic pressure in physiology and metabolism of hadal fungi from the deepest ocean sediment. mSystems, Jan 2024. URL: https://doi.org/10.1128/msystems.01085-23, doi:10.1128/msystems.01085-23. This article has 17 citations and is from a peer-reviewed journal.

22. (scheffer2023themysteryof pages 7-9): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 33 citations.