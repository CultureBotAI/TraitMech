---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:14:36.530386'
end_time: '2026-08-04T09:24:01.868469'
duration_seconds: 565.34
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: orange pigmented
  trait_identifier: METPO:1003026
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: orange_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    orange due to production and accumulation of orange pigments such as carotenoids.
  parent_traits: METPO:1003021
  synonyms: Pigment_orange
  evidence_summary: 'DOI:10.1080/1040841X.2025.2526423: orange ... pigmentation in
    bacteria (Supports orange microbial pigmentation as a bacterial carotenoid-associated
    color phenotype.)'
  causal_graph_summary: 'orange_pigmented_carotenoid_accumulation: 15 nodes, 12 edges'
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
- **Trait label:** orange pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003026
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear orange due to production and accumulation of orange pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_orange
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: orange ... pigmentation in bacteria (Supports orange microbial pigmentation as a bacterial carotenoid-associated color phenotype.)
- **Existing causal graph summary:** orange_pigmented_carotenoid_accumulation: 15 nodes, 12 edges

## Research Objective

Research the microbial trait **orange pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/orange_pigmented.yaml`.

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
- **Trait label:** orange pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003026
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear orange due to production and accumulation of orange pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_orange
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: orange ... pigmentation in bacteria (Supports orange microbial pigmentation as a bacterial carotenoid-associated color phenotype.)
- **Existing causal graph summary:** orange_pigmented_carotenoid_accumulation: 15 nodes, 12 edges

## Research Objective

Research the microbial trait **orange pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/orange_pigmented.yaml`.

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


# Curation report: microbial **orange pigmented**

## 1. Scope and recommended interpretation

**Target class:** `METPO:1003026`  
**Label:** orange pigmented  
**Category:** MORPHOLOGY  
**Parent:** `METPO:1003021`

This trait should represent an **assay-observed orange appearance of microbial colonies or cells caused by sufficient accumulation of one or more pigments**. Carotenoids are the best-supported mechanism, but the class is morphological rather than chemical: orange appearance does not identify a unique molecule, pathway, or physiological function. Carotenoids collectively span yellow, orange, red, and purple hues, and carotenoid composition, concentration, membrane environment, growth phase, illumination, and observation conditions can shift the apparent color (barreto2023biotechnologicalapplicationsof pages 7-9, barreto2023microbialpigmentsmajor pages 4-6).

A strong direct example is *Rhodotorula mucilaginosa*: lactate-grown cells contained 161 µg carotenoids/g dry cells and appeared orange, whereas glucose-grown cells contained 90 µg/g and appeared pale pink. This connects increased carotenoid abundance to the orange phenotype without implying that every carotenoid-producing strain is orange (mosquedamartinez2024inrhodotorulamucilaginosa pages 6-7). In *Sphingomonas* COS14-R2, colonies were deep yellow, but fed-batch culture became intense orange-yellow; nostoxanthin was the principal pigment. This is a useful boundary case because appearance changed with cultivation format and pigment abundance (raman2024nostoxanthinbiosynthesisby pages 1-2, raman2024nostoxanthinbiosynthesisby pages 5-8).

### Inclusion criteria

Curate an organism or experimental state as `METPO:1003026` when:

1. The source explicitly calls colonies or cells **orange**, preferably under specified culture conditions.
2. The color is cell- or colony-associated rather than merely discoloration of the extracellular medium.
3. Pigment accumulation is chemically demonstrated, or a genetic or chemical perturbation causally links pigmentation to a pathway.
4. The observation includes sufficient assay context—medium, temperature, illumination, incubation time, and growth state where available.

### Boundary cases

- **Orange-yellow or red-orange:** include only with the source’s exact color wording and an assay-context qualifier. Do not silently normalize “yellow,” “red,” “pink,” or “golden” to orange.
- **Photochromogenicity:** this is a conditional capacity to produce pigment after illumination, not necessarily constitutive orange pigmentation. In *Mycobacterium kansasii*, light predominantly induced β-carotene and intense yellow coloration; some mutants changed from white to orange, demonstrating that pathway flux can alter hue (janisch2023geneticunderpinningsof pages 1-2, janisch2023geneticunderpinningsof pages 2-4).
- **Pigment production without orange appearance:** carotenoid production alone is insufficient. The *Sphingomonas* colonies were described as deep yellow even though liquid fed-batch culture became orange-yellow (raman2024nostoxanthinbiosynthesisby pages 1-2, raman2024nostoxanthinbiosynthesisby pages 5-8).
- **Non-carotenoid orange pigments:** potentially valid instances of the morphology class, but they require independent chemical evidence and a separate mechanism branch. Red prodigiosin, Monascus pigments, and other diffusible pigments should not be included merely because reviews group them with warm-colored microbial pigments (barreto2023biotechnologicalapplicationsof pages 7-9).
- **Extract color:** an orange extract is not evidence that intact cells or colonies are orange.

## 2. Current mechanistic model

The most defensible generic mechanism is:

**isoprenoid precursor supply → GGPP → phytoene → desaturated carotene intermediates/lycopene → cyclic carotenes → oxygenated xanthophylls → cellular accumulation → orange appearance**.

CrtB/phytoene synthase forms phytoene from geranylgeranyl diphosphate; CrtI/phytoene desaturase creates conjugated carotene intermediates, commonly extending to lycopene; CrtY-type cyclases generate cyclic carotenes such as β-carotene. Hydroxylases, ketolases, desaturases, and glycosylation enzymes then generate taxon-specific xanthophylls. Recent reviews support this architecture but also emphasize substantial organism-specific variation after lycopene (barreto2023microbialpigmentsmajor pages 4-6).

In *M. kansasii*, a 2023 transposon study supplied unusually strong causal evidence. Approximately 150,000 mutants were screened, yielding 204 abnormal-pigmentation mutants. Of 124 mapped mutants, 116 insertions—94%—fell in three loci associated with carotenoid biosynthesis, carotenoid cleavage, or monounsaturated-fatty-acid biosynthesis (janisch2023geneticunderpinningsof pages 4-5, janisch2023geneticunderpinningsof pages 2-4). The principal CRT locus contains `crtE`, `crtI`, `crtB`, `crtYc`, and `crtYd`; transfer of the complete locus to nonpigmented *M. smegmatis* conferred light-dependent pigmentation, demonstrating pathway sufficiency in a heterologous host (janisch2023geneticunderpinningsof pages 10-12, janisch2023geneticunderpinningsof pages 1-2).

The visible trait is therefore best modeled as an endpoint downstream of **pigment abundance and composition**, with separate branches for precursor supply, biosynthesis, degradation, regulation, environmental induction, and cellular retention.

## 3. Candidate graph nodes

### Trait and observable nodes

- `METPO:1003026` — orange pigmented
- orange colony pigmentation — label-only assay-observed state
- orange cell pigmentation — label-only assay-observed state
- orange-yellow pigmentation — label-only boundary state
- photochromogenic pigmentation — label-only conditional phenotype
- colorless/white pigmentation mutant — label-only negative phenotype

### Pathways and processes

- carotenoid biosynthetic process — `GO:0016117`
- isoprenoid precursor biosynthesis
- methylerythritol-phosphate pathway
- mevalonate pathway
- carotene biosynthesis
- xanthophyll biosynthesis
- carotenoid cleavage/apocarotenoid formation
- carotenoid accumulation
- reactive-oxygen-species detoxification
- oxidative phosphorylation
- light-induced transcription

The MEP-versus-MVA assignment should be made per organism rather than asserted universally. The reviewed literature describes both routes into carotenoid precursor supply (barreto2023biotechnologicalapplicationsof pages 7-9, barreto2023microbialpigmentsmajor pages 4-6).

### Chemicals and metabolites

- geranylgeranyl diphosphate (GGPP)
- phytoene
- lycopene
- γ-carotene
- β-carotene — `CHEBI:17579`
- nostoxanthin
- zeaxanthin
- lutein
- torulene
- torularhodin
- deinoxanthin
- 2-deoxydeinoxanthin
- apocarotenoids
- reactive oxygen species
- hydrogen peroxide — `CHEBI:16240`
- superoxide
- hydroxyl radical
- lactate — `CHEBI:24996` is the class-level candidate; use an appropriate stereospecific child if the medium composition is known
- glucose — `CHEBI:17234`
- oleic acid — `CHEBI:16196`
- diphenylamine — inhibitor; verify the exact ChEBI record before YAML insertion
- menadione — ROS-generating experimental factor

Only identifiers checked with high confidence are supplied above. Remaining chemicals should remain label-only until validated against the current ontology release.

### Genes, proteins, and modules

**Core bacterial pathway**

- `crtE` — geranylgeranyl-diphosphate synthase
- `crtB` — phytoene synthase
- `crtI` — phytoene desaturase
- `crtY`, `crtYc`, `crtYd` — lycopene cyclases
- `crtG`, `crtZ` — hydroxylation branch toward nostoxanthin in *Sphingomonas*
- `mmpL1` — CRT-locus-associated membrane protein in *M. kansasii*; exact pigment-transport role remains unresolved

**Regulation and degradation**

- `crtR` — MarR-type negative regulator in *M. kansasii*
- `ccoR` — TetR/AcrR-type regulator of carotenoid cleavage
- `cco1` — carotenoid cleavage oxygenase/degradation enzyme
- `sigF` — pigmentation-associated sigma factor in *M. smegmatis*
- `rsbW`/`MSMEG_1803` — anti-SigF factor

**Deinoxanthin branch**

- `crtLm` — lycopene cyclase
- `cruF` — carotene hydratase
- `crtD` — carotenoid desaturase
- `crtO` — carotene ketolase
- `dr2473`/`CYP287A1` — carotenoid 2-β-hydroxylase
- `dxs` — 1-deoxy-D-xylulose-5-phosphate synthase

**Physiological coupling**

- `fnr1` — ferredoxin–NADP(H) reductase in the *M. kansasii* FD locus
- `desA3` — fatty-acid desaturase associated with oleate synthesis

Gene symbols are not globally unique. YAML nodes should carry organism context and, where possible, verified NCBI Gene, UniProt, or locus-tag identifiers rather than treating a symbol such as `crtR` as one universal entity. In particular, `crtR` denotes unrelated regulator or reductase functions in different taxa.

### Environmental and experimental factors

- visible-light exposure
- dark incubation
- oxygen availability/respiratory metabolism
- oxidative stress
- carbon source: lactate versus glucose/dextrose
- temperature
- pH
- carbon:nitrogen ratio
- carotenoid-pathway inhibition by diphenylamine
- ionizing radiation, UV, hydrogen peroxide, and menadione challenge

### Taxonomic/context nodes

- *Mycobacterium kansasii*
- *Mycobacterium smegmatis*
- *Rhodotorula mucilaginosa*
- *Sphingomonas* sp. COS14-R2
- *Deinococcus radiodurans*

NCBITaxon CURIEs should be added only after checking the exact species/strain record; COS14-R2 may require a strain label rather than a species-level identifier.

## 4. Candidate causal edges

The table below prioritizes experimentally manipulated edges. “Moderate” entries are useful mechanistic hypotheses but should be checked against the cited original article before production curation.

| subject | predicate | object | taxon/context | evidence snippet | DOI/date | confidence and curation note |
|---|---|---|---|---|---|---|
| geranylgeranyl diphosphate (GGPP) | is substrate for / upstream of | phytoene synthase CrtB producing phytoene | generalized carotenoid pathway; supported in Sphingomonas and haloarchaeal engineering contexts | “The reaction from geranylgeranyl-PP to phytoene catalyzed by phytoene synthase (CrtB)” and COS14-R2 contains “crtB (phytoene synthase)” (raman2024nostoxanthinbiosynthesisby pages 1-2, raman2024nostoxanthinbiosynthesisby pages 2-4) | 10.1007/s00284-024-03956-7 (2024-11); 10.3389/fmicb.2018.02893 (2018-11) | **High for pathway node**, but direct orange-phenotype linkage is indirect; curate as core biosynthetic edge rather than trait-specific edge. |
| phytoene desaturase CrtI | enables conversion of | phytoene to lycopene/carotene intermediates | generalized carotenoid pathway; M. kansasii CRT locus and Sphingomonas pathway | COS14-R2 contains “crtI (phytoene desaturase)” and the CRT locus in M. kansasii includes “crtI (phytoene desaturase)” (raman2024nostoxanthinbiosynthesisby pages 1-2, janisch2023geneticunderpinningsof pages 4-5) | 10.1007/s00284-024-03956-7 (2024-11); 10.3390/pathogens12010086 (2023-01) | **High for pathway**, but exact product state can be taxon-specific; use object label like “lycopene/carotene intermediates” if avoiding over-assertion. |
| lycopene beta-cyclase CrtY | converts | lycopene to β-carotene | Sphingomonas sp. COS14-R2; broader bacterial carotenoid pathway | pathway involves “CrtE, CrtB, CrtI, and CrtY for β-carotene production” (raman2024nostoxanthinbiosynthesisby pages 2-4) | 10.1007/s00284-024-03956-7 (2024-11) | **High**; suitable core edge. |
| β-carotene | is branch-point precursor for | nostoxanthin biosynthesis via CrtG/CrtZ | Sphingomonas sp. COS14-R2 | “β-carotene production, which serves as a branch point for nostoxanthin synthesis via CrtG enzyme”; gene clusters “crtB, crtG, crtI, crtY, and crtZ were identified as responsible for nostoxanthin biosynthesis” (raman2024nostoxanthinbiosynthesisby pages 8-10, raman2024nostoxanthinbiosynthesisby pages 2-4) | 10.1007/s00284-024-03956-7 (2024-11) | **High** for this taxon; mark taxon-specific. |
| carotenoid accumulation | contributes to | orange / orange-yellow cell or culture phenotype | Rhodotorula mucilaginosa; fed-batch Sphingomonas culture | “YPLac-grown cells contained 161 µg/g… carotenoids versus only 90 µg/g in YPD cells. Visually, YPLac-grown cells were orange” and Sphingomonas culture “changed to intense orange-yellow” (mosquedamartinez2024inrhodotorulamucilaginosa pages 6-7, raman2024nostoxanthinbiosynthesisby pages 5-8) | 10.3389/ffunb.2024.1378590 (2024-09); 10.1007/s00284-024-03956-7 (2024-11) | **High** phenotypic edge; strongest direct support for METPO:1003026. |
| light exposure | positively regulates | CRT locus expression / photochromogenicity | Mycobacterium kansasii | “Light exposure induces CRT locus gene expression including crtE, crtI, and crtR” and transfer of CRT locus to M. smegmatis “conferred photochromogenicity” (janisch2023geneticunderpinningsof pages 5-8, janisch2023geneticunderpinningsof pages 10-12) | 10.3390/pathogens12010086 (2023-01) | **High**; useful regulatory edge for orange/yellow carotenoid pigmentation under assay conditions. |
| CrtR | negatively regulates | carotenogenesis / crtE expression | Mycobacterium kansasii | “crtR overexpression… suppressed carotenogenesis” and caused “≥500-fold downregulation of crtE expression under light” (janisch2023geneticunderpinningsof pages 10-12) | 10.3390/pathogens12010086 (2023-01) | **High**; taxon-specific regulator edge. |
| CRT locus transfer | causes | photochromogenic pigmentation in non-pigmented host | M. kansasii CRT locus in Mycobacterium smegmatis | “Transfer of the complete CRT locus to Mycobacterium smegmatis conferred photochromogenicity, with light-induced yellow pigmentation” (janisch2023geneticunderpinningsof pages 10-12) | 10.3390/pathogens12010086 (2023-01) | **High** functional sufficiency evidence; phenotype is yellow rather than explicitly orange, so use as mechanistic support not strict trait-defining proof. |
| CcoR | negatively regulates | cco1Mk carotene-degradation gene expression | Mycobacterium kansasii | “CcoRMk acts as a negative regulator of cco1Mk expression” (janisch2023geneticunderpinningsof pages 17-19) | 10.3390/pathogens12010086 (2023-01) | **High**; taxon-specific. |
| cco1Mk carotene degradation activity | decreases | carotenoid pigmentation via apocarotenoid production | Mycobacterium kansasii | loss of CcoR caused “100-fold cco1Mk upregulation leading to pigment loss through apocarotenoid production” (janisch2023geneticunderpinningsof pages 17-19) | 10.3390/pathogens12010086 (2023-01) | **High**; strong negative edge relevant to loss of orange/yellow pigmentation. |
| lactate-supported oxidative metabolism / OxPhos | increases | ROS | Rhodotorula mucilaginosa grown in YPLac | “YPLac-grown cells… supports oxidative phosphorylation” and baseline ROS was “1.4 nmol H2O2/µg protein compared to YPD-cells below 1.0” (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2, mosquedamartinez2024inrhodotorulamucilaginosa pages 7-8) | 10.3389/ffunb.2024.1378590 (2024-09) | **High**; curate as environmental/physiological driver edge. |
| increased ROS | induces / is associated with increased | carotenoid accumulation | Rhodotorula mucilaginosa | “lactate-dependent oxidative metabolism induces higher ROS production, triggering compensatory carotenoid accumulation” (mosquedamartinez2024inrhodotorulamucilaginosa pages 7-8) | 10.3389/ffunb.2024.1378590 (2024-09) | **High** within this experiment; association plus mechanistic interpretation. |
| increased carotenoid accumulation | causes / accompanies | orange cells | Rhodotorula mucilaginosa | “YPLac-grown cells contained 161 µg/g… carotenoids… Visually, YPLac-grown cells were orange while YPD cells were pale pink” (mosquedamartinez2024inrhodotorulamucilaginosa pages 6-7) | 10.3389/ffunb.2024.1378590 (2024-09) | **High**; one of the most direct orange-trait edges. |
| diphenylamine (DPA) | inhibits | carotenoid production | Rhodotorula mucilaginosa | “DPA inhibited carotenoid production in a dose-dependent manner: at 15 mM DPA, production was inhibited by 80%, and at 40 mM DPA, it was completely inhibited (100%)” (mosquedamartinez2024inrhodotorulamucilaginosa pages 4-6) | 10.3389/ffunb.2024.1378590 (2024-09) | **High**, but check unit consistency during curation because ROS experiments were described in µM; retain note on possible reporting inconsistency. |
| DPA inhibition of carotenoid synthesis | increases / unmasks | ROS | Rhodotorula mucilaginosa | “ROS in YPLac-cells increased dramatically to 6.3 nmol H2O2/µg protein at 40 µM DPA” (mosquedamartinez2024inrhodotorulamucilaginosa pages 7-8) | 10.3389/ffunb.2024.1378590 (2024-09) | **High** for protective role of pigments; use with DPA-as-experimental-factor annotation. |
| crtB knockout or crtI knockout | causes | colorless phenotype | Deinococcus radiodurans | “Knockout experiments with crtB and crtI genes produced colorless mutants” (wang2024insightsintothe pages 8-9) | 10.3389/fmicb.2024.1447785 (2024-07 review citing original knockout work); original DOI reported in review: 10.1007/s00203-007-0262-5 | **Moderate-High** because this statement comes via review; ideal to verify against original knockout paper before final TraitMech curation. |
| crtB/crtI-dependent carotenoid biosynthesis | promotes | resistance to oxidative/radiation stress | Deinococcus radiodurans | colorless mutants showed “100-fold greater H2O2 sensitivity than wild-type” and reduced survival after irradiation (yang2021crucialrolesof pages 1-4, wang2024insightsintothe pages 8-9) | 10.1101/2021.05.26.445811 (2021-05 preprint); 10.3389/fmicb.2024.1447785 (2024-07 review) | **Moderate** for curation due to preprint/review dependence, but mechanistically compelling. |
| CrtLm | converts | lycopene to γ-carotene | Deinococcus radiodurans deinoxanthin pathway | “lycopene cyclase (CrtLm) cyclizes lycopene to γ-carotene” (wang2024insightsintothe pages 5-6) | 10.3389/fmicb.2024.1447785 (2024-07) | **Moderate**; review-derived pathway edge, taxon-specific. |
| CruF | hydroxylates | γ-carotene derivative at C-1′ | Deinococcus radiodurans deinoxanthin pathway | “C-1′,2′-hydratase (CruF) adds a hydroxyl group at C-1′” (wang2024insightsintothe pages 5-6) | 10.3389/fmicb.2024.1447785 (2024-07) | **Moderate**; review-derived, taxon-specific. |
| CrtD | desaturates | carotenoid intermediate at C-3′,4′ | Deinococcus radiodurans deinoxanthin pathway | “C-3′,4′-desaturase (CrtD) introduces a double bond at C-3′,4′” (wang2024insightsintothe pages 5-6) | 10.3389/fmicb.2024.1447785 (2024-07) | **Moderate**; review-derived. |
| CrtO | ketolates | γ-carotene derivative toward ketolated deinoxanthin precursor | Deinococcus radiodurans | “carotene ketolase (CrtO) adds a keto group at C-4”; crtO deletion caused “increased sensitivity to hydrogen peroxide-induced oxidative stress” (wang2024insightsintothe pages 5-6) | 10.3389/fmicb.2024.1447785 (2024-07) | **Moderate**; strong function claim but still review-mediated in current evidence set. |
| DR2473 / CYP287A1 | hydroxylates | 2-deoxydeinoxanthin to deinoxanthin | Deinococcus radiodurans | “2-β-hydroxylase (encoded by dr2473/CYP287A1)… adds a hydroxyl group… to generate deinoxanthin” (wang2024insightsintothe pages 6-8) | 10.3389/fmicb.2024.1447785 (2024-07); original DOI reported in review: 10.1007/s00253-015-6910-9 | **Moderate-High**; review cites knockout evidence and original DOI is available. |
| overexpression of crtB and dxs | increases | deinoxanthin production | Deinococcus radiodurans engineering | “Overexpression of crtB and dxs genes increased deinoxanthin production to 394 ± 17.6 mg/L” (wang2024insightsintothe pages 6-8) | 10.3389/fmicb.2024.1447785 (2024-07) | **Moderate**; useful application edge, but not directly orange-specific. |
| optimized culture conditions (35°C, pH 7.5, 40 g/L glucose, 5 g/L yeast extract, dark incubation) | increase | nostoxanthin yield | Sphingomonas sp. COS14-R2 | “highest concentration of nostoxanthin was recorded at 35 °C, pH of 7.5, glucose concentration of 40 g L−1, and a yeast extract concentration of 5 g L−1 during dark incubation” (raman2024nostoxanthinbiosynthesisby pages 1-2) | 10.1007/s00284-024-03956-7 (2024-11) | **High**; clear experimental environmental-factor edge. |
| optimized fed-batch fermentation | yields | 217.22 ± 9.60 mg/L nostoxanthin | Sphingomonas sp. COS14-R2 | “Fed-batch fermentation yielded nostoxanthin at 217.22 ± 9.60 mg/L with 72.32% selectivity” (raman2024nostoxanthinbiosynthesisby pages 1-2) | 10.1007/s00284-024-03956-7 (2024-11) | **High**; implementation/statistics edge, not direct trait edge. |
| carotenoids | protect against / scavenge | ROS | generalized microbial pigment function; direct experiments in Rhodotorula and Deinococcus | carotenoids “function to inactivate excess ROS” and major Deinococcus carotenoids “effectively scavenge reactive oxygen species including superoxide anion and hydroxyl radicals” (mosquedamartinez2024inrhodotorulamucilaginosa pages 7-8, yang2021crucialrolesof pages 1-4) | 10.3389/ffunb.2024.1378590 (2024-09); 10.1101/2021.05.26.445811 (2021-05) | **Moderate-High**; broad functional edge explaining why orange carotenoid phenotypes are selected under stress. |


*Table: This table compiles the strongest curation-ready causal edges for METPO:1003026 orange pigmented, emphasizing direct experimental evidence from 2023–2024 studies and clearly flagging taxon-specific or review-derived claims.*

### Highest-priority minimal graph

For a compact extension of the existing 15-node/12-edge graph, the most defensible additions are:

1. `lactate-supported oxidative metabolism` **increases** `ROS generation`.
2. `ROS generation` **induces/associates with increased** `carotenoid accumulation`.
3. `carotenoid accumulation` **causes or contributes to** `METPO:1003026` in *R. mucilaginosa* under YPLac conditions.
4. `diphenylamine` **inhibits** `carotenoid biosynthesis`.
5. `carotenoid biosynthesis` **decreases** `cellular ROS burden`.
6. `light exposure` **induces** the *M. kansasii* CRT locus.
7. `CrtR` **represses** CRT-locus expression/carotenogenesis.
8. `Cco1` **degrades** carotenes to apocarotenoids and thereby **decreases** pigmentation.
9. `crtB/crtI function` **enables** carotenoid accumulation; disruption **causes** a colorless phenotype in *D. radiodurans*.
10. `optimized temperature/pH/carbon/nitrogen/darkness` **increases** nostoxanthin accumulation and can shift *Sphingomonas* culture toward orange-yellow.

## 5. Recent developments and quantitative evidence

### 2023: causal genetics of photochromogenicity

The *M. kansasii* screen resolved pigmentation control at unusually high scale: 204 abnormal-color mutants were recovered from approximately 150,000 mutants. Phenotypes included 58 constitutively yellow, 25 constitutively red, 98 persistently white, and 23 white-to-orange mutants after illumination (janisch2023geneticunderpinningsof pages 2-4). CrtR overexpression suppressed pigment production and produced at least a 500-fold decrease in light-induced `crtE` expression; transfer of the full CRT locus conferred photochromogenicity on *M. smegmatis* (janisch2023geneticunderpinningsof pages 10-12). These data support explicit regulatory and sufficiency edges rather than merely co-occurrence.

### 2024: oxidative metabolism explains an orange yeast state

In *R. mucilaginosa*, lactate-grown cells consumed oxygen at 15–23 versus 8–15 natgO min⁻¹ mg wet cells⁻¹ on dextrose and accumulated 161 versus 90 µg carotenoids/g dry cells. The lactate-grown cells were orange; glucose-grown cells were pale pink (mosquedamartinez2024inrhodotorulamucilaginosa pages 6-7). Baseline ROS reached approximately 1.4 nmol H₂O₂/µg protein in lactate-grown cells but remained below 1.0 in glucose-grown cells. With 40 µM diphenylamine, ROS rose to 6.3 versus 1.8 nmol H₂O₂/µg protein, supporting a carotenoid-dependent antioxidant effect (mosquedamartinez2024inrhodotorulamucilaginosa pages 7-8). The source reports torularhodin, β-carotene, and torulene, with torularhodin commonly comprising 60–80% and β-carotene 10–20% under the described minimal-medium context (mosquedamartinez2024inrhodotorulamucilaginosa pages 9-10, mosquedamartinez2024inrhodotorulamucilaginosa pages 4-6).

### 2024: culture engineering and orange-yellow nostoxanthin production

*Sphingomonas* COS14-R2 produced maximal nostoxanthin at 35°C, pH 7.5, 40 g/L glucose, 5 g/L yeast extract, and dark incubation. Fed-batch production reached 217.22 ± 9.60 mg/L, with 72.32% selectivity; the culture became intense orange-yellow (raman2024nostoxanthinbiosynthesisby pages 1-2, raman2024nostoxanthinbiosynthesisby pages 5-8). The reported secondary products at 84 h included β-carotene at 3.01 ± 0.03 mg/L, lutein at 4.47 ± 0.05 mg/L, and zeaxanthin at 1.31 ± 0.01 mg/L (raman2024nostoxanthinbiosynthesisby pages 5-8). This supports condition-to-pigment edges, but because colonies themselves were described as yellow, it should be represented as an orange-yellow culture-state boundary case rather than an unconditional orange-colony annotation.

### 2024: pathway engineering and stress protection in *Deinococcus*

A recent authoritative review organizes the deinoxanthin branch as CrtLm-mediated γ-carotene formation, followed by CruF hydration, CrtD desaturation, CrtO ketolation, and CYP287A1/DR2473 hydroxylation (wang2024insightsintothe pages 6-8, wang2024insightsintothe pages 5-6). Overexpression of `crtB` and `dxs` reportedly raised deinoxanthin production to 394 ± 17.6 mg/L (wang2024insightsintothe pages 6-8). Review-summarized knockout evidence indicates that `crtB` or `crtI` disruption produces colorless mutants and that these mutants can be approximately 100-fold more sensitive than wild type to 5 mM H₂O₂ (wang2024insightsintothe pages 8-9). These findings strongly connect pigmentation to antioxidant physiology, but *D. radiodurans* is commonly described as red-pigmented; use it to support the carotenoid mechanism, not as an automatic orange-trait instance.

## 6. Applications and expert assessment

The immediate applications are microbial production of natural colorants, antioxidants, carotenoid feed or nutraceutical ingredients, and engineered stress-tolerant production hosts. Recent reviews also identify food, cosmetics, pharmaceuticals, active packaging, and—in the specific case of *Deinococcus* pigments—radiation protection and space-biology applications as promising areas (barreto2023microbialpigmentsmajor pages 4-6, wang2024insightsintothe pages 6-8). These are applications of the underlying pigments, not of the morphology term itself.

The strongest current expert interpretation is that carotenoid coloration is often a **functional stress-response phenotype**, not decorative pigmentation. Direct experiments support ROS scavenging in *R. mucilaginosa* and link pigment loss to oxidative sensitivity in *M. smegmatis* and *D. radiodurans* (mosquedamartinez2024inrhodotorulamucilaginosa pages 7-8, yang2021crucialrolesof pages 1-4, singh2015characterizationofmycobacterium pages 1-2). Nevertheless, antioxidant function should not be inferred from color alone: pigment identity, concentration, oxidation state, and cellular context matter. The yeast study even found that carotenoid extracts from strongly oxidative conditions could lose protective behavior or become growth-inhibitory, indicating possible pro-oxidant chemistry after radical exposure (mosquedamartinez2024inrhodotorulamucilaginosa pages 8-9).

Industrial translation remains constrained by cultivation cost, pigment extraction, purification, stability, formulation, and regulatory acceptance. Metabolic engineering and use of low-cost by-products are viewed as important routes to lower production cost, but recent reviews still describe large-scale commercialization as a bottleneck (barreto2023microbialpigmentsmajor pages 4-6).

## 7. Warnings: claims not yet ready for TraitMech curation

1. **Do not equate carotenoid production with orange pigmentation.** β-Carotene, torularhodin, nostoxanthin, deinoxanthin, and mixed carotenoid pools can produce yellow, orange, pink, red, or intermediate phenotypes.
2. **Do not curate yellow or red organisms as orange without explicit wording.** *D. radiodurans* and light-induced *M. kansasii* are excellent mechanistic sources but weak direct instances of `METPO:1003026`.
3. **Keep pathway branches taxon-specific.** The nostoxanthin, deinoxanthin, torularhodin, and β-carotene branches are not interchangeable.
4. **Do not treat `crtR` as one conserved function.** In *M. kansasii* it is a transcriptional repressor; in some yeasts similarly named genes encode cytochrome-P450 reductases.
5. **Mark membrane localization as uncertain.** A source proposes that phytoene synthase, phytoene desaturase, and lycopene cyclase form a membrane-associated complex, but this should not become a universal localization edge without direct organism-specific evidence (janisch2023geneticunderpinningsof pages 19-20).
6. **Do not assign `mmpL1` a pigment transporter function yet.** Its CRT-locus association is clear, but transport direction and substrate remain insufficiently established.
7. **Verify diphenylamine units from the primary paper.** Retrieved passages describe ROS experiments at 15–40 µM but one summary reports inhibition at 15–40 mM; this inconsistency should be resolved before encoding concentration-qualified edges (mosquedamartinez2024inrhodotorulamucilaginosa pages 7-8, mosquedamartinez2024inrhodotorulamucilaginosa pages 4-6).
8. **Review-derived Deinococcus edges require original-paper verification.** In particular, CrtO and CYP287A1 reaction details should be checked against the original experiments before final YAML insertion.
9. **Avoid universal MVA/MEP assertions.** Route usage varies among bacteria, archaea, fungi, and phototrophs.
10. **Do not infer health benefits from colony color.** Industrial or biomedical claims concern isolated, characterized compounds and require their own efficacy and safety evidence.

## 8. DOI-first bibliography

1. Janisch N, Levendosky K, Budell WC, Quadri LEN. “Genetic Underpinnings of Carotenogenesis and Light-Induced Transcriptome Remodeling in the Opportunistic Pathogen *Mycobacterium kansasii*.” *Pathogens*. Published January 2023. DOI: [10.3390/pathogens12010086](https://doi.org/10.3390/pathogens12010086). Primary experimental study. (janisch2023geneticunderpinningsof pages 10-12, janisch2023geneticunderpinningsof pages 2-4)
2. Mosqueda-Martínez E, et al. “In *Rhodotorula mucilaginosa*, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species.” *Frontiers in Fungal Biology*. Published September 2024. DOI: [10.3389/ffunb.2024.1378590](https://doi.org/10.3389/ffunb.2024.1378590). Primary experimental study. (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2, mosquedamartinez2024inrhodotorulamucilaginosa pages 6-7)
3. Raman J, Kim J-S, Ko Y-J, Kim S-J. “Nostoxanthin Biosynthesis by *Sphingomonas* Species (COS14-R2): Isolation, Identification, and Optimization of Culture Conditions.” *Current Microbiology*. Published November 2024. DOI: [10.1007/s00284-024-03956-7](https://doi.org/10.1007/s00284-024-03956-7). Primary fermentation and characterization study. (raman2024nostoxanthinbiosynthesisby pages 1-2, raman2024nostoxanthinbiosynthesisby pages 5-8)
4. Wang Y, et al. “Insights into the synthesis, engineering, and functions of microbial pigments in *Deinococcus* bacteria.” *Frontiers in Microbiology*. Published July 2024. DOI: [10.3389/fmicb.2024.1447785](https://doi.org/10.3389/fmicb.2024.1447785). Recent authoritative review. (wang2024insightsintothe pages 6-8, wang2024insightsintothe pages 5-6)
5. de Oliveira Barreto JV, et al. “Microbial Pigments: Major Groups and Industrial Applications.” *Microorganisms*. Published December 2023. DOI: [10.3390/microorganisms11122920](https://doi.org/10.3390/microorganisms11122920). Review. (barreto2023microbialpigmentsmajor pages 4-6)
6. Sandmann G. “Genes and Pathway Reactions Related to Carotenoid Biosynthesis in Purple Bacteria.” *Biology*. Published October 2023. DOI: [10.3390/biology12101346](https://doi.org/10.3390/biology12101346). Pathway review.
7. Singh AK, et al. “Characterization of *Mycobacterium smegmatis sigF* mutant and its regulon…” *MicrobiologyOpen*. Published October 2015. DOI: [10.1002/mbo3.288](https://doi.org/10.1002/mbo3.288). Primary regulatory and oxidative-stress study. (singh2015characterizationofmycobacterium pages 1-2)
8. Zhang L, et al. “Knockout of *crtB* or *crtI* gene blocks the carotenoid biosynthetic pathway in *Deinococcus radiodurans* R1…” *Archives of Microbiology*. Published 2007. DOI: [10.1007/s00203-007-0262-5](https://doi.org/10.1007/s00203-007-0262-5). Foundational knockout study, identified through the 2024 review (wang2024insightsintothe pages 12-12).
9. Zhou Z, et al. “CYP287A1 is a carotenoid 2-β-hydroxylase required for deinoxanthin biosynthesis in *Deinococcus radiodurans* R1.” *Applied Microbiology and Biotechnology*. Published 2015. DOI: [10.1007/s00253-015-6910-9](https://doi.org/10.1007/s00253-015-6910-9). Foundational enzyme study, identified through the 2024 review (wang2024insightsintothe pages 6-8, wang2024insightsintothe pages 12-12).

**Curation recommendation:** use *R. mucilaginosa* YPLac growth as the strongest direct environmental-to-orange phenotype branch; use *M. kansasii* as the strongest recent genetic-regulatory branch; use *Sphingomonas* COS14-R2 as a condition-dependent orange-yellow production branch; and retain *Deinococcus* primarily as a taxon-specific carotenoid-function module rather than a direct orange-phenotype exemplar.

References

1. (barreto2023biotechnologicalapplicationsof pages 7-9): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis Mansur, and Alane Beatriz Vermelho. Biotechnological applications of microbial pigments. Unknown journal, Oct 2023. URL: https://doi.org/10.20944/preprints202310.0121.v1, doi:10.20944/preprints202310.0121.v1.

2. (barreto2023microbialpigmentsmajor pages 4-6): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 102 citations.

3. (mosquedamartinez2024inrhodotorulamucilaginosa pages 6-7): Edson Mosqueda-Martínez, Natalia Chiquete-Félix, Paulina Castañeda-Tamez, Carolina Ricardez-García, Manuel Gutiérrez-Aguilar, Salvador Uribe-Carvajal, and Ofelia Mendez-Romero. In rhodotorula mucilaginosa, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species. Frontiers in Fungal Biology, Sep 2024. URL: https://doi.org/10.3389/ffunb.2024.1378590, doi:10.3389/ffunb.2024.1378590. This article has 24 citations.

4. (raman2024nostoxanthinbiosynthesisby pages 1-2): Jegadeesh Raman, Jeong-Seon Kim, Young-Joon Ko, and Soo-Jin Kim. Nostoxanthin biosynthesis by sphingomonas species (cos14-r2): isolation, identification, and optimization of culture conditions. Current Microbiology, Nov 2024. URL: https://doi.org/10.1007/s00284-024-03956-7, doi:10.1007/s00284-024-03956-7. This article has 6 citations and is from a peer-reviewed journal.

5. (raman2024nostoxanthinbiosynthesisby pages 5-8): Jegadeesh Raman, Jeong-Seon Kim, Young-Joon Ko, and Soo-Jin Kim. Nostoxanthin biosynthesis by sphingomonas species (cos14-r2): isolation, identification, and optimization of culture conditions. Current Microbiology, Nov 2024. URL: https://doi.org/10.1007/s00284-024-03956-7, doi:10.1007/s00284-024-03956-7. This article has 6 citations and is from a peer-reviewed journal.

6. (janisch2023geneticunderpinningsof pages 1-2): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

7. (janisch2023geneticunderpinningsof pages 2-4): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

8. (janisch2023geneticunderpinningsof pages 4-5): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

9. (janisch2023geneticunderpinningsof pages 10-12): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

10. (raman2024nostoxanthinbiosynthesisby pages 2-4): Jegadeesh Raman, Jeong-Seon Kim, Young-Joon Ko, and Soo-Jin Kim. Nostoxanthin biosynthesis by sphingomonas species (cos14-r2): isolation, identification, and optimization of culture conditions. Current Microbiology, Nov 2024. URL: https://doi.org/10.1007/s00284-024-03956-7, doi:10.1007/s00284-024-03956-7. This article has 6 citations and is from a peer-reviewed journal.

11. (raman2024nostoxanthinbiosynthesisby pages 8-10): Jegadeesh Raman, Jeong-Seon Kim, Young-Joon Ko, and Soo-Jin Kim. Nostoxanthin biosynthesis by sphingomonas species (cos14-r2): isolation, identification, and optimization of culture conditions. Current Microbiology, Nov 2024. URL: https://doi.org/10.1007/s00284-024-03956-7, doi:10.1007/s00284-024-03956-7. This article has 6 citations and is from a peer-reviewed journal.

12. (janisch2023geneticunderpinningsof pages 5-8): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

13. (janisch2023geneticunderpinningsof pages 17-19): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

14. (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2): Edson Mosqueda-Martínez, Natalia Chiquete-Félix, Paulina Castañeda-Tamez, Carolina Ricardez-García, Manuel Gutiérrez-Aguilar, Salvador Uribe-Carvajal, and Ofelia Mendez-Romero. In rhodotorula mucilaginosa, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species. Frontiers in Fungal Biology, Sep 2024. URL: https://doi.org/10.3389/ffunb.2024.1378590, doi:10.3389/ffunb.2024.1378590. This article has 24 citations.

15. (mosquedamartinez2024inrhodotorulamucilaginosa pages 7-8): Edson Mosqueda-Martínez, Natalia Chiquete-Félix, Paulina Castañeda-Tamez, Carolina Ricardez-García, Manuel Gutiérrez-Aguilar, Salvador Uribe-Carvajal, and Ofelia Mendez-Romero. In rhodotorula mucilaginosa, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species. Frontiers in Fungal Biology, Sep 2024. URL: https://doi.org/10.3389/ffunb.2024.1378590, doi:10.3389/ffunb.2024.1378590. This article has 24 citations.

16. (mosquedamartinez2024inrhodotorulamucilaginosa pages 4-6): Edson Mosqueda-Martínez, Natalia Chiquete-Félix, Paulina Castañeda-Tamez, Carolina Ricardez-García, Manuel Gutiérrez-Aguilar, Salvador Uribe-Carvajal, and Ofelia Mendez-Romero. In rhodotorula mucilaginosa, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species. Frontiers in Fungal Biology, Sep 2024. URL: https://doi.org/10.3389/ffunb.2024.1378590, doi:10.3389/ffunb.2024.1378590. This article has 24 citations.

17. (wang2024insightsintothe pages 8-9): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 18 citations and is from a peer-reviewed journal.

18. (yang2021crucialrolesof pages 1-4): Qiao Yang. Crucial roles of carotenoids as bacterial endogenous defense system for bacterial radioresistance of deinococcus radiodurans. bioRxiv, May 2021. URL: https://doi.org/10.1101/2021.05.26.445811, doi:10.1101/2021.05.26.445811. This article has 6 citations.

19. (wang2024insightsintothe pages 5-6): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 18 citations and is from a peer-reviewed journal.

20. (wang2024insightsintothe pages 6-8): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 18 citations and is from a peer-reviewed journal.

21. (mosquedamartinez2024inrhodotorulamucilaginosa pages 9-10): Edson Mosqueda-Martínez, Natalia Chiquete-Félix, Paulina Castañeda-Tamez, Carolina Ricardez-García, Manuel Gutiérrez-Aguilar, Salvador Uribe-Carvajal, and Ofelia Mendez-Romero. In rhodotorula mucilaginosa, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species. Frontiers in Fungal Biology, Sep 2024. URL: https://doi.org/10.3389/ffunb.2024.1378590, doi:10.3389/ffunb.2024.1378590. This article has 24 citations.

22. (singh2015characterizationofmycobacterium pages 1-2): Anirudh K. Singh, Debashis Dutta, Vandana Singh, Vishal Srivastava, Rajesh K. Biswas, and Bhupendra N. Singh. Characterization of mycobacterium smegmatis sigf mutant and its regulon: overexpression of sigf antagonist (msmeg_1803) in m. smegmatis mimics sigf mutant phenotype, loss of pigmentation, and sensitivity to oxidative stress. MicrobiologyOpen, 4:896-916, Oct 2015. URL: https://doi.org/10.1002/mbo3.288, doi:10.1002/mbo3.288. This article has 43 citations and is from a peer-reviewed journal.

23. (mosquedamartinez2024inrhodotorulamucilaginosa pages 8-9): Edson Mosqueda-Martínez, Natalia Chiquete-Félix, Paulina Castañeda-Tamez, Carolina Ricardez-García, Manuel Gutiérrez-Aguilar, Salvador Uribe-Carvajal, and Ofelia Mendez-Romero. In rhodotorula mucilaginosa, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species. Frontiers in Fungal Biology, Sep 2024. URL: https://doi.org/10.3389/ffunb.2024.1378590, doi:10.3389/ffunb.2024.1378590. This article has 24 citations.

24. (janisch2023geneticunderpinningsof pages 19-20): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

25. (wang2024insightsintothe pages 12-12): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 18 citations and is from a peer-reviewed journal.