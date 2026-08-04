---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:26:13.169663'
end_time: '2026-08-04T04:33:36.833193'
duration_seconds: 443.66
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range very low
  trait_identifier: METPO:1000448
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_very_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which growth extends to ambient temperatures\
    \ at or below approximately 10 \xB0C, characteristic of psychrophilic growth ranges."
  parent_traits: METPO:1000306
  synonyms: Psychrophile, TR_<=10
  evidence_summary: 'DOI:10.1038/sj.embor.7400662: growing well at temperatures around
    the freezing point of water (Psychrophile review supports growth at very low temperatures
    as the psychrophilic range.)'
  causal_graph_summary: 'temperature_range_very_low_psychrophile: 15 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000448
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which growth extends to ambient temperatures at or below approximately 10 °C, characteristic of psychrophilic growth ranges.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, TR_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic range.)
- **Existing causal graph summary:** temperature_range_very_low_psychrophile: 15 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature range very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_very_low.yaml`.

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
- **Trait label:** temperature range very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000448
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which growth extends to ambient temperatures at or below approximately 10 °C, characteristic of psychrophilic growth ranges.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, TR_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic range.)
- **Existing causal graph summary:** temperature_range_very_low_psychrophile: 15 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature range very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_very_low.yaml`.

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


# Curation report: microbial very-low-temperature growth

## Trait record and scope

- **Trait:** temperature range very low
- **Identifier:** **`METPO:1000448`**
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Parent:** `METPO:1000306`
- **Operational interpretation:** a growth-temperature-range phenotype in which **reproducible population growth extends to ≤10 °C**. The decisive observation should be biomass, viable-cell number, growth rate, or repeated division—not respiration alone, survival after cold shock, or activity of an isolated enzyme.

This operational scope is broader than the classical definition of an obligate or strict psychrophile. Traditional definitions generally require growth near 0 °C, an optimum around or below 15 °C, and an upper limit near 20 °C; psychrotrophs/psychrotolerant organisms also grow in the cold but have substantially higher optima or maxima. Recent reviews continue to use somewhat inconsistent numerical boundaries, making the measured growth range more reliable than the label “psychrophile.” (moyer2017psychrophilesandpsychrotrophs pages 2-3, purwar2024adaptationsofpsychrophilic pages 1-3, ramon2023ageneraloverview pages 1-2)

### Boundary cases

1. **Include:** sustained growth at 10, 4, 0, or subzero temperature, even where the organism's optimum is above 15 °C. Pseudoalteromonas sp. WY3, for example, grew at 4 °C but had predicted `Topt = 24.8 °C`; it therefore supports `METPO:1000448` under the supplied range definition but is not a classical strict psychrophile. Its measured rates were 0.0011, 0.0021, 0.0449, 0.1428, and 0.1478 h⁻¹ at 4, 8, 12, 16, and 25 °C, respectively; predicted `Tmin`, `Topt`, and `Tmax` were −1.2, 24.8, and 36.5 °C. (wang2024genomicinsightsinto pages 11-12)
2. **Exclude:** survival at −30 °C without demonstrated division; metabolic activity inferred at −40 °C; a transient cold-shock response followed by no growth; or an isolated cold-active enzyme. Reviews explicitly distinguish verified growth down to approximately −15 °C from survival or predicted metabolism at lower temperatures. (moyer2017psychrophilesandpsychrotrophs pages 2-3)
3. **Do not infer from habitat:** isolation from glacier, permafrost, Antarctic soil, refrigerated food, or deep ocean is insufficient without a growth assay.
4. **Do not infer strict psychrophily from ≤10 °C growth alone:** record optimum and maximum temperatures separately where available. Pseudarthrobacter psychrotolerans YJ56 grew best at 13 °C and failed to grow at 30 °C, which is much stronger evidence of a genuinely cold-adapted range than growth at 4 °C alone. (son2023morphologicalandphysiological pages 1-2)
5. **Separate acute and acclimated states:** cold shock, acclimation, and steady-state cold growth can activate different systems. A 2023 study deliberately compared sustained growth at 0 and 15 °C rather than an acute shock and found extensive transcriptional remodeling despite a comparatively stable central metabolome. (riccardi2023metabolicrobustnessto pages 1-2)

## Current mechanistic model

Very-low-temperature growth is a systems phenotype rather than a single pathway. Cooling rigidifies membranes, stabilizes inhibitory RNA structures, slows enzyme catalysis and macromolecular turnover, perturbs protein folding, raises oxidative stress through greater oxygen solubility, and can impose freeze-concentration/osmotic stress. Successful organisms combine homeoviscous membrane remodeling, RNA and ribosome maintenance, protein-quality control, cold-active catalysis, redox protection, compatible-solute/EPS production, and regulatory or metabolic buffering. Recent authoritative analysis emphasizes that the exact combination is strongly taxon- and temperature-transition-specific. (bao2023miningofkey pages 1-2, ramon2023ageneraloverview pages 1-2, riccardi2023metabolicrobustnessto pages 1-2)

## Candidate nodes grouped by type

### Phenotype, environment, and assay nodes

- `METPO:1000448` — temperature range very low.
- Low growth temperature: **10, 4, 0, or subzero °C**; retain the exact assay temperature as evidence metadata.
- Sustained low-temperature population growth; growth rate; lag duration; biomass/OD; viable count.
- Cold shock, cold acclimation, and steady-state cold growth as separate experimental-condition nodes.
- Freeze–thaw exposure and extracellular ice as separate stressors, not synonyms of low-temperature growth.
- Candidate environments: glacier ice, permafrost, Antarctic marine water, Antarctic soil, and refrigerated environments. Assign ENVO CURIEs only after checking the exact sampled habitat.

### Cellular structures and processes

- Cell membrane / plasma membrane — **GO:0005886**.
- Membrane lipid remodeling and homeoviscous adaptation — label-only pending exact ontology review.
- Membrane fluidity, permeability, and transport competence.
- Ribosome — **GO:0005840**; 50S ribosomal subunit — **GO:0005842**.
- Translation — **GO:0006412**; protein folding — **GO:0006457**.
- RNA secondary-structure remodeling / RNA helicase activity.
- Cell wall remodeling; peptidoglycan turnover.
- Oxidative-stress response — **GO:0006979**.
- Biofilm formation — **GO:0042710**.
- Central-carbon metabolic homeostasis and transcriptomic buffering.

### Genes, proteins, enzymes, and complexes

**Higher-priority, functionally supported candidates**

- **csdA**: cold-associated DEAD-box RNA helicase; knockout reduces low-temperature growth in Psychrobacter arcticus 273-4.
- **relA**: stringent-response enzyme; knockout reduces low-temperature growth in the same strain.
- **dac2**: cold-upregulated DD-peptidase/carboxypeptidase; knockout reduces low-temperature growth.
- **GroEL**: chaperonin; heterologous expression of the Rhodococcus sp. RCBS9 protein improved E. coli growth at 10 °C.
- **Dps**: DNA-binding ferritin-like stress protein; RCBS9 Dps expression improved E. coli growth at 10 °C.
- **USP-2**: universal stress protein; RCBS9 USP-2 expression improved E. coli growth at 10 °C.

**Mechanistically plausible but mostly expression/genomic-association candidates**

- **rbfA, nusA, nusB**, translation initiation factor **IF-2**.
- **rimJ**, ribosomal protein **L29**, and 50S assembly proteins.
- **DnaJ, DnaK, GrpE, ClpB, ClpP, ClpX, HtpG, trigger factor**, peptidyl-prolyl isomerases.
- **FabF** (β-ketoacyl-ACP synthase II), **Des** fatty-acid desaturase, and putative hopanoid desaturases.
- **BetS**/betaine uptake systems and other osmolyte transporters.
- **KatE/catalase**, superoxide dismutase, peroxiredoxin **PrxQ**, Dps.
- Two-component cold sensors such as **DesK/DesR** or RCBS9 **DesK-like** signaling components; retain as taxon-specific hypotheses unless directly tested.
- Pili-associated proteins reported as cold-upregulated in Pseudomonas fragi D12; keep label-only until locus identities and function are resolved.

Gene symbols are not globally unique. TraitMech records should include strain-specific locus tags or UniProt accessions after sequence verification rather than assigning a generic UniProt CURIE.

### Chemicals and molecular classes

- Unsaturated fatty acid — **CHEBI:27208**.
- Saturated fatty acid — **CHEBI:26607**.
- Palmitoleic acid — **CHEBI:32372**.
- cis-Vaccenic acid — ontology identifier should be verified before curation.
- Branched-chain and anteiso fatty acids; polyunsaturated fatty acids.
- Hopanoids and carotenoid membrane pigments.
- Glycine betaine — **CHEBI:17750**.
- Trehalose — **CHEBI:27082**.
- Proline — **CHEBI:17203**.
- Glycine — **CHEBI:15428**.
- Mannitol — **CHEBI:16899**.
- Sorbitol — **CHEBI:17924**.
- Extracellular polymeric substances/exopolysaccharide and biofilm matrix.
- Reactive oxygen species — **CHEBI:26523**.
- Phosphoenolpyruvate — **CHEBI:18021**.

## Candidate causal edges

The most compact set of evidence-graded candidate edges is below. “Strong” means direct genetic perturbation or heterologous gain of function; “moderate” means replicated physiological/omics response with mechanistic coherence; “uncertain” means the source interprets an association causally but did not perturb the mediator.

| subject | predicate | object | evidence grade | organism/assay | DOI |
|---|---|---|---|---|---|
| relA knockout | reduces | low-temperature growth | strong | *Psychrobacter arcticus* 273-4; mutant phenotype during subzero/low-temperature growth assays (bergholz2009psychrobacterarcticus2734 pages 1-1) | 10.1128/JB.01377-08 |
| csdA (DEAD-box RNA helicase) knockout | reduces | low-temperature growth | strong | *Psychrobacter arcticus* 273-4; mutant phenotype during subzero/low-temperature growth assays (bergholz2009psychrobacterarcticus2734 pages 1-1, bergholz2009psychrobacterarcticus2734 pages 8-9) | 10.1128/JB.01377-08 |
| dac2 (DD-peptidase) knockout | reduces | low-temperature growth | strong | *Psychrobacter arcticus* 273-4; mutant phenotype during subzero/low-temperature growth assays (bergholz2009psychrobacterarcticus2734 pages 1-1, bergholz2009psychrobacterarcticus2734 pages 8-9) | 10.1128/JB.01377-08 |
| DPS overexpression | improves | *E. coli* growth at 10 °C | strong | recombinant *E. coli* BL21 expressing RCBS9 target protein; OD600 peak ~1.4 at 4 h vs control ~1.0–1.1 (li2024mechanismsunderlyingthe pages 12-13) | 10.3389/fmicb.2024.1465627 |
| GroEL overexpression | improves | *E. coli* growth at 10 °C | strong | recombinant *E. coli* BL21 expressing RCBS9 target protein; OD600 peak ~1.4 at 4 h vs control ~1.0–1.1 (li2024mechanismsunderlyingthe pages 12-13) | 10.3389/fmicb.2024.1465627 |
| USP-2 overexpression | improves | *E. coli* growth at 10 °C | strong | recombinant *E. coli* BL21 expressing RCBS9 target protein; OD600 peak ~1.4 at 4 h vs control ~1.0–1.1 (li2024mechanismsunderlyingthe pages 12-13) | 10.3389/fmicb.2024.1465627 |
| RCBS9 low-temperature-induced target proteins (other 3 validated proteins; names not recoverable in available excerpt) overexpression | improves | *E. coli* growth at 10 °C | moderate | recombinant *E. coli* BL21 expressing six RCBS9 proteins; all differed significantly from vector control (li2024mechanismsunderlyingthe pages 1-3, li2024mechanismsunderlyingthe pages 12-13) | 10.3389/fmicb.2024.1465627 |
| low temperature (10 °C vs 25 °C) | increases | unsaturated fatty acid abundance | moderate | *Rhodococcus* sp. RCBS9; methyl (E)-9-octadecenoate increased ~11-fold (li2024mechanismsunderlyingthe pages 5-7) | 10.3389/fmicb.2024.1465627 |
| increased unsaturated fatty acids | may help maintain | membrane fluidity / limited membrane permeability increase | uncertain | *Rhodococcus* sp. RCBS9; authors interpret lipid shift as adaptive, but causality not directly perturbed (li2024mechanismsunderlyingthe pages 5-7) | 10.3389/fmicb.2024.1465627 |
| low temperature | induces | transcriptomic reprogramming of hundreds of metabolic genes | moderate | cold-adapted marine bacterium grown at 0 vs 15 °C; multi-omics comparison (riccardi2023metabolicrobustnessto pages 1-2) | 10.1128/msystems.01124-22 |
| transcriptomic reprogramming | is interpreted to buffer | central-metabolome robustness at 0 °C | uncertain | cold-adapted marine bacterium; metabolome robust despite transcriptome shifts (riccardi2023metabolicrobustnessto pages 1-2) | 10.1128/msystems.01124-22 |
| low temperature | upregulates | ribosome/RNA factors (rbfA, nusA, nusB, IF-2; cold-active helicase isozyme csdA) | moderate | *Psychrobacter arcticus* transcriptomics at 0/−6 °C vs 17/22 °C (bergholz2009psychrobacterarcticus2734 pages 8-9) | 10.1128/JB.01377-08 |
| ribosome/RNA factors | support | low-temperature translation and growth | moderate | *Psychrobacter arcticus*; strengthened by csdA knockout phenotype, but most factors are expression associations (bergholz2009psychrobacterarcticus2734 pages 1-1, bergholz2009psychrobacterarcticus2734 pages 8-9) | 10.1128/JB.01377-08 |
| low temperature | upregulates | chaperones/protein-folding factors (e.g., DnaJ, ClpB, HtpG, trigger factor, PpiC) | moderate | *Psychrobacter arcticus* transcriptomics/proteomics (bergholz2009psychrobacterarcticus2734 pages 8-9) | 10.1128/JB.01377-08 |
| low temperature | increases | relative biofilm content | moderate | *Rhodococcus* sp. RCBS9 in LB at 10 °C vs 25 °C (li2024mechanismsunderlyingthe pages 5-7) | 10.3389/fmicb.2024.1465627 |
| increased biofilm production | may contribute to | low-temperature tolerance | uncertain | *Rhodococcus* sp. RCBS9; authors interpret as adaptive protection, no direct perturbation (li2024mechanismsunderlyingthe pages 5-7) | 10.3389/fmicb.2024.1465627 |
| low temperature | is associated with increased | chaperones and transcription factors | moderate | *Pseudomonas fragi* D12; 15 °C→4 °C response (bao2023miningofkey pages 1-2) | 10.3389/fmicb.2023.1215837 |
| low temperature | is associated with increased | membrane-fluidity maintenance / compatible solutes / extracellular polymers / reduced ROS | moderate | *Pseudomonas fragi* D12; 30 °C→15 °C response (bao2023miningofkey pages 1-2) | 10.3389/fmicb.2023.1215837 |


*Table: This table compiles the strongest and most curation-ready causal edges for the very-low-temperature growth trait, prioritizing direct perturbation evidence and clearly marking correlations as uncertain. It is useful as a compact starting point for TraitMech edge selection and evidence grading.*

### Additional edge-level evidence and snippets

| Proposed subject–predicate–object triple | Reference and supporting snippet | Curation assessment |
|---|---|---|
| **low temperature → increases → unsaturated-fatty-acid abundance** | RCBS9 at 10 versus 25 °C: “the content and proportions of unsaturated fatty acids strongly increased,” and methyl (E)-9-octadecenoate increased **11-fold**; fatty-acid species fell from 19 to 14 and saturated-fatty-acid content declined. DOI: [10.3389/fmicb.2024.1465627](https://doi.org/10.3389/fmicb.2024.1465627), November 2024. (li2024mechanismsunderlyingthe pages 5-7) | Curatable as a temperature-response edge in RCBS9. Do not convert directly to “causes psychrophily.” |
| **unsaturated-fatty-acid enrichment → supports → membrane fluidity at low temperature** | Authors state that unsaturated fatty acids have superior capacity “to maintain…cell membrane fluidity at low temperatures” and interpret the RCBS9 lipid shift as contributing to permeability recovery. (li2024mechanismsunderlyingthe pages 5-7) | Mechanistically well established, but the RCBS9 experiment did not inhibit desaturation; mark **inferred/uncertain** for this strain. |
| **FabF activity → increases → cis-vaccenic acid during cooling** | Recent review: “The key enzyme in the increase of cis-vaccenic acid is FabF,” catalyzing elongation of palmitoleoyl-ACP to cis-vaccenoyl-ACP precursors. DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4), July 2023. (ramon2023ageneraloverview pages 4-5) | Useful pathway edge, but species context must be recovered from the cited primary paper before asserting a broad trait edge. |
| **decreasing temperature from 20 to 4 °C → increases → unsaturated hopanoids** | In Methylovulum psychrotolerans, unsaturated hopanoids increased from **27% to 49%**. (ramon2023ageneraloverview pages 4-5) | Curatable as a taxon-specific measured response; the putative hopanoid-desaturase genes remain unvalidated. |
| **csdA / relA / dac2 function → enables → low-temperature growth** | Knockout mutants of all three had reduced low-temperature growth in P. arcticus 273-4, which grew over −6 to 22 °C. DOI: [10.1128/JB.01377-08](https://doi.org/10.1128/JB.01377-08), April 2009. (bergholz2009psychrobacterarcticus2734 pages 1-1) | Among the strongest TraitMech-ready evidence. Encode separate edges with strain and mutant-assay provenance. |
| **low temperature → increases → RNA/ribosome-support factors** | At −6 °C relative to 17 °C, **rbfA 1.8-fold, nusB 1.7-fold, nusA 2.6-fold, and IF-2 1.8-fold**; the cold-associated helicase isozyme and cold-active DD-peptidase isozyme were preferentially expressed. (bergholz2009psychrobacterarcticus2734 pages 8-9) | Curatable as expression-response edges. Only csdA/dac2 have direct growth evidence in this source. |
| **low temperature → increases → protein-folding machinery** | In P. arcticus at −6 °C versus 17 °C, DnaJ was 2.33-fold, HtpG 2.41-fold, trigger factor 2.22-fold, ClpB 1.93-fold, and PpiC 1.67-fold higher. (bergholz2009psychrobacterarcticus2734 pages 8-9) | Expression associations; do not assert necessity without mutants. |
| **RCBS9 Dps/GroEL/USP-2 expression → increases → E. coli growth at 10 °C** | Vector control remained approximately **OD600 1.0–1.1**; Dps-, GroEL-, and USP-2-expressing strains reached approximately **1.4 at 4 h**. All six tested proteins significantly altered growth relative to control. DOI: [10.3389/fmicb.2024.1465627](https://doi.org/10.3389/fmicb.2024.1465627), November 2024. (li2024mechanismsunderlyingthe pages 12-13) | Strong gain-of-function evidence. Curate Dps, GroEL, and USP-2 individually; recover the other three names from Figure 7/supplement before curation. |
| **0 °C growth → induces → transcriptomic reprogramming** | Multi-omics comparison at 0 and 15 °C found changes in hundreds of metabolic genes while main central metabolites remained strongly overlapping. DOI: [10.1128/msystems.01124-22](https://doi.org/10.1128/msystems.01124-22), published February 27, 2023. (riccardi2023metabolicrobustnessto pages 1-2) | Curatable as a temperature-response edge. “Transcriptomic buffering causes metabolome robustness” is the authors' systems-level interpretation, not a perturbation result. |
| **low temperature → increases → biofilm production** | RCBS9 relative biofilm content in LB was “consistently higher at 10 °C than at 25 °C.” Under combined nutrient limitation plus cold, however, relative biofilm decreased, showing context dependence. (li2024mechanismsunderlyingthe pages 5-7) | Curate only with medium and stress context. The edge biofilm → cold growth remains uncertain without a biofilm-deficient mutant. |
| **13 °C growth → increases → 50S assembly/L29 proteins** | P. psychrotolerans YJ56 had OD600 >1 at 13 °C, could not grow at 30 °C, and showed increased 50S assembly and L29 proteins at 13 °C. It also had expanded rimJ copy number. DOI: [10.1038/s41598-023-42179-x](https://doi.org/10.1038/s41598-023-42179-x), September 2023. (son2023morphologicalandphysiological pages 1-2, son2023morphologicalandphysiological pages 3-4) | Useful cold-adapted-ribosome hypothesis, but copy number and abundance are correlational. Moreover, 13 °C is above the target threshold, so use as mechanistic context rather than direct `METPO:1000448` evidence unless ≤10 °C growth is documented elsewhere. |
| **30→15 °C cooling → increases → compatible solutes/EPS and decreases ROS; 15→4 °C cooling → increases → chaperones/transcription factors** | P. fragi D12 exhibited stage-specific responses; 124 candidate genes and 19 unique genes were reported. DOI: [10.3389/fmicb.2023.1215837](https://doi.org/10.3389/fmicb.2023.1215837), July 2023. (bao2023miningofkey pages 1-2) | Curate as taxon- and transition-specific response edges, not universal necessities. No knockout validation was reported in the retrieved evidence. |

## Recent developments, applications, and quantitative findings

### 2023–2024 research advances

- Recent work increasingly replaces single-gene narratives with **temperature-resolved multi-omics**. The 0-versus-15 °C marine-bacterium study found an unexpectedly stable central metabolome despite deep metabolic-transcriptome remodeling, suggesting that regulatory changes buffer pathway output rather than simply maximizing every cold-response metabolite. (riccardi2023metabolicrobustnessto pages 1-2)
- The 2024 RCBS9 study combined membrane assays, lipid profiling, RNA-seq, and heterologous validation. It detected **2,012 upregulated and 1,926 downregulated genes at 10 versus 25 °C**, with upregulated functions enriched in transport, energy production, amino-acid metabolism, and fatty-acid degradation, while many ribosomal genes were downregulated. This cautions against treating increased ribosome abundance as a universal cold mechanism. (li2024mechanismsunderlyingthe pages 5-7)
- Organisms may use markedly different mechanisms at different parts of the temperature range. P. fragi D12 emphasized membrane/EPS/osmolyte/redox responses from 30→15 °C, then chaperone and transcriptional responses from 15→4 °C. (bao2023miningofkey pages 1-2)
- Genome-only evidence remains common. Pseudoalteromonas WY3 carries cold-shock, oxidoreductase, osmotic-stress, and RNA/protein-synthesis candidates, but its measured growth curve does not functionally connect those genes to cold growth. (wang2024genomicinsightsinto pages 11-12)

### Real-world relevance

- **Cold bioremediation:** RCBS9 maintains 17β-estradiol degradation under cold conditions, motivating treatment of estrogen-contaminated cold environments; its validated stress proteins are engineering candidates, although field performance has not been established in the retrieved study. (li2024mechanismsunderlyingthe pages 1-3, li2024mechanismsunderlyingthe pages 12-13)
- **Low-energy industrial biocatalysis:** cold-active enzymes can operate at mild temperature and are rapidly heat-inactivated. Their enhanced low-temperature activity is commonly achieved through increased conformational flexibility and reduced stabilizing interactions, often trading stability or substrate affinity for catalytic motion. Reviews report activities up to roughly an order of magnitude above mesophilic homologs at low temperature. This is an enzyme-property branch, not by itself evidence for whole-cell `METPO:1000448`. (moyer2017psychrophilesandpsychrotrophs pages 2-3)
- **Food systems:** psychrotrophs such as Pseudomonas can grow during refrigeration and are important spoilage organisms. Conversely, cold-active proteases, lipases, glycosidases, and other enzymes are candidates for food processing with lower heating requirements.
- **Agriculture and waste treatment:** cold-tolerant phosphate-solubilizing microbes and psychrophilic anaerobic digestion are proposed for cold soils and low-temperature biomethanation, but application evidence should be curated separately from the cellular growth mechanism.
- **Climate and ecosystem modeling:** cold-adapted marine microbes experience Southern Ocean temperatures of approximately −2 to 10 °C; understanding regulatory buffering is relevant to predicting responses to seasonal warming and sea-ice change. (riccardi2023metabolicrobustnessto pages 1-2)

## Recommended initial graph structure

A conservative first expansion of the existing 15-node/8-edge graph should prioritize three mechanistic arms:

1. **RNA/cell-envelope arm:** `csdA`, `dac2`, and `relA` → sustained low-temperature growth, supported by mutant phenotypes.
2. **Protein/redox arm:** RCBS9 `GroEL`, `Dps`, and `USP-2` → improved growth at 10 °C, supported by heterologous gain of function.
3. **Membrane arm:** ≤10 °C exposure → increased unsaturated-fatty-acid abundance → maintained membrane fluidity → transport and growth. The first edge is measured; the latter two should initially be marked inferred unless a desaturase perturbation is attached.

Secondary branches can include RNA/ribosome factors, chaperone systems, compatible solutes, EPS/biofilm, ROS defenses, hopanoid remodeling, and central-metabolism buffering, but should carry taxon- and assay-specific qualifiers.

## Warnings: claims not yet ready for unqualified TraitMech curation

1. **Do not equate gene presence with causality.** WY3 genome annotations, YJ56 gene-copy expansions, and D12 candidate genes are hypotheses unless linked to perturbation phenotypes.
2. **Do not treat differential expression as necessity or sufficiency.** Most chaperone, transporter, compatible-solute, and ribosome edges are associations.
3. **Avoid universal directionality.** Some organisms increase translation machinery in the cold, whereas RCBS9 downregulated many ribosomal genes, apparently conserving energy. (bergholz2009psychrobacterarcticus2734 pages 8-9, li2024mechanismsunderlyingthe pages 5-7)
4. **Membrane adaptation is not uniformly “more unsaturation.”** Branching, chain length, hopanoids, carotenoids, and pre-existing desaturase activity can dominate in particular taxa. In Bacillus subtilis, long-term adaptation prominently involves a switch from iso- to anteiso-branched fatty acids; in M. psychrotolerans, unsaturated hopanoids changed substantially. (ramon2023ageneraloverview pages 4-5)
5. **Compatible solutes and EPS are pleiotropic.** Their induction may reflect osmotic, nutrient, freezing, or biofilm stress rather than low temperature alone.
6. **The RCBS9 heterologous assay demonstrates improved 10 °C growth in E. coli, not that each protein is necessary in native RCBS9.** Only Dps, GroEL, and USP-2 names were recoverable with quantitative values; the remaining three should not be entered by guessed identity. (li2024mechanismsunderlyingthe pages 12-13)
7. **Cold-active enzyme flexibility is not sufficient for the organism-level trait.** It belongs in the graph only when connected to a native essential pathway and whole-cell growth evidence.
8. **Preserve exact strain, medium, oxygenation, salinity, temperature, and exposure duration.** These variables can reverse apparent effects, as illustrated by RCBS9 biofilm formation under cold alone versus combined cold and nutrient limitation. (li2024mechanismsunderlyingthe pages 5-7)
9. **Verify all ontology accessions before YAML commit.** The common GO/CHEBI mappings above are candidate groundings; strain-specific proteins require sequence-resolved UniProt or locus identifiers.

## DOI-first bibliography

1. Li Q. et al. “Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain Rhodococcus sp. RCBS9.” *Frontiers in Microbiology* 15. **November 2024.** DOI: [10.3389/fmicb.2024.1465627](https://doi.org/10.3389/fmicb.2024.1465627). (li2024mechanismsunderlyingthe pages 12-13, li2024mechanismsunderlyingthe pages 5-7)
2. Wang Y. et al. “Genomic insights into the cold adaptation and secondary metabolite potential of Pseudoalteromonas sp. WY3 from Antarctic krill.” *Frontiers in Microbiology* 15. **November 2024.** DOI: [10.3389/fmicb.2024.1459716](https://doi.org/10.3389/fmicb.2024.1459716). (wang2024genomicinsightsinto pages 11-12)
3. Bao C. et al. “Mining of key genes for cold adaptation from Pseudomonas fragi D12 and analysis of its cold-adaptation mechanism.” *Frontiers in Microbiology* 14. **July 2023.** DOI: [10.3389/fmicb.2023.1215837](https://doi.org/10.3389/fmicb.2023.1215837). (bao2023miningofkey pages 1-2)
4. Ramón A. et al. “A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.” *Brazilian Journal of Microbiology* 54:2259–2287. **July 2023.** DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4). (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 4-5)
5. Son Y. et al. “Morphological and physiological adaptations of psychrophilic Pseudarthrobacter psychrotolerans YJ56 under temperature stress.” *Scientific Reports* 13. **September 2023.** DOI: [10.1038/s41598-023-42179-x](https://doi.org/10.1038/s41598-023-42179-x). (son2023morphologicalandphysiological pages 1-2, son2023morphologicalandphysiological pages 3-4)
6. Riccardi C. et al. “Metabolic Robustness to Growth Temperature of a Cold-Adapted Marine Bacterium.” *mSystems* 8(2). **Published February 27, 2023.** DOI: [10.1128/msystems.01124-22](https://doi.org/10.1128/msystems.01124-22). (riccardi2023metabolicrobustnessto pages 1-2)
7. Bergholz P.W., Bakermans C., Tiedje J.M. “Psychrobacter arcticus 273-4 Uses Resource Efficiency and Molecular Motion Adaptations for Subzero Temperature Growth.” *Journal of Bacteriology* 191:2340–2352. **April 2009.** DOI: [10.1128/JB.01377-08](https://doi.org/10.1128/JB.01377-08). (bergholz2009psychrobacterarcticus2734 pages 1-1, bergholz2009psychrobacterarcticus2734 pages 8-9)
8. Moyer C.L., Collins R.E., Morita R.Y. “Psychrophiles and Psychrotrophs.” *Reference Module in Life Sciences*. **January 2017.** DOI: [10.1016/B978-0-12-809633-8.02282-2](https://doi.org/10.1016/B978-0-12-809633-8.02282-2). (moyer2017psychrophilesandpsychrotrophs pages 2-3, moyer2017psychrophilesandpsychrotrophs pages 3-5)
9. D’Amico S. et al. “Psychrophilic microorganisms: challenges for life.” *EMBO Reports* 7:385–389. **April 2006.** DOI: [10.1038/sj.embor.7400662](https://doi.org/10.1038/sj.embor.7400662). This is the supplied existing evidence and remains appropriate for the broad phenotype concept.

References

1. (moyer2017psychrophilesandpsychrotrophs pages 2-3): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 187 citations.

2. (purwar2024adaptationsofpsychrophilic pages 1-3): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

3. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

4. (wang2024genomicinsightsinto pages 11-12): Yuanyuan Wang, Jinxuan Xie, Zhengqi Feng, Linbo Ma, Wenbo Wu, Changjun Guo, and Jianguo He. Genomic insights into the cold adaptation and secondary metabolite potential of pseudoalteromonas sp. wy3 from antarctic krill. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1459716, doi:10.3389/fmicb.2024.1459716. This article has 6 citations and is from a peer-reviewed journal.

5. (son2023morphologicalandphysiological pages 1-2): Yongjun Son, Jihyeon Min, Yoonjae Shin, and Woojun Park. Morphological and physiological adaptations of psychrophilic pseudarthrobacter psychrotolerans yj56 under temperature stress. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42179-x, doi:10.1038/s41598-023-42179-x. This article has 17 citations and is from a peer-reviewed journal.

6. (riccardi2023metabolicrobustnessto pages 1-2): Christopher Riccardi, Marzia Calvanese, Veronica Ghini, Tania Alonso-Vásquez, Elena Perrin, Paola Turano, Giorgio Giurato, Alessandro Weisz, Ermenegilda Parrilli, Maria Luisa Tutino, and Marco Fondi. Metabolic robustness to growth temperature of a cold- adapted marine bacterium. mSystems, Apr 2023. URL: https://doi.org/10.1128/msystems.01124-22, doi:10.1128/msystems.01124-22. This article has 21 citations and is from a peer-reviewed journal.

7. (bao2023miningofkey pages 1-2): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

8. (bergholz2009psychrobacterarcticus2734 pages 1-1): Peter W. Bergholz, Corien Bakermans, and James M. Tiedje. <i>psychrobacter arcticus</i> 273-4 uses resource efficiency and molecular motion adaptations for subzero temperature growth. Apr 2009. URL: https://doi.org/10.1128/jb.01377-08, doi:10.1128/jb.01377-08. This article has 126 citations and is from a peer-reviewed journal.

9. (bergholz2009psychrobacterarcticus2734 pages 8-9): Peter W. Bergholz, Corien Bakermans, and James M. Tiedje. <i>psychrobacter arcticus</i> 273-4 uses resource efficiency and molecular motion adaptations for subzero temperature growth. Apr 2009. URL: https://doi.org/10.1128/jb.01377-08, doi:10.1128/jb.01377-08. This article has 126 citations and is from a peer-reviewed journal.

10. (li2024mechanismsunderlyingthe pages 12-13): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 9 citations and is from a peer-reviewed journal.

11. (li2024mechanismsunderlyingthe pages 1-3): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 9 citations and is from a peer-reviewed journal.

12. (li2024mechanismsunderlyingthe pages 5-7): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 9 citations and is from a peer-reviewed journal.

13. (ramon2023ageneraloverview pages 4-5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

14. (son2023morphologicalandphysiological pages 3-4): Yongjun Son, Jihyeon Min, Yoonjae Shin, and Woojun Park. Morphological and physiological adaptations of psychrophilic pseudarthrobacter psychrotolerans yj56 under temperature stress. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42179-x, doi:10.1038/s41598-023-42179-x. This article has 17 citations and is from a peer-reviewed journal.

15. (moyer2017psychrophilesandpsychrotrophs pages 3-5): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 187 citations.