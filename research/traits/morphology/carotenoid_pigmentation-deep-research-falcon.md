---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:28:20.182697'
end_time: '2026-08-04T07:37:53.071210'
duration_seconds: 572.89
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: carotenoid pigmentation
  trait_identifier: METPO:1003031
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: carotenoid_pigmentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype caused by microbial production and accumulation
    of carotenoid pigments.
  parent_traits: METPO:1003021
  synonyms: Pigment_carotenoid
  evidence_summary: 'DOI:10.1080/1040841X.2025.2526423: Carotenoids are isoprenoid
    pigments (Supports carotenoid pigmentation as a bacterial isoprenoid-pigment phenotype.)'
  causal_graph_summary: 'carotenoid_pigmentation_crt_pathway: 12 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carotenoid pigmentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003031
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype caused by microbial production and accumulation of carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_carotenoid
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: Carotenoids are isoprenoid pigments (Supports carotenoid pigmentation as a bacterial isoprenoid-pigment phenotype.)
- **Existing causal graph summary:** carotenoid_pigmentation_crt_pathway: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **carotenoid pigmentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/carotenoid_pigmentation.yaml`.

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
- **Trait label:** carotenoid pigmentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003031
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype caused by microbial production and accumulation of carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_carotenoid
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: Carotenoids are isoprenoid pigments (Supports carotenoid pigmentation as a bacterial isoprenoid-pigment phenotype.)
- **Existing causal graph summary:** carotenoid_pigmentation_crt_pathway: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **carotenoid pigmentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/carotenoid_pigmentation.yaml`.

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


# Curation report: microbial carotenoid pigmentation

## Executive scope

**Target trait:** carotenoid pigmentation  
**Identifier:** **METPO:1003031**  
**Category/kind:** MORPHOLOGY / CLASS  
**Parent:** METPO:1003021  
**Synonym:** *Pigment_carotenoid*

The trait should represent an **observable microbial pigmentation phenotype caused by endogenous production and cellular accumulation of one or more carotenoids**. The pigments are conjugated isoprenoids whose visible absorption can produce yellow, orange, red, pink, or golden colonies/cells. The core causal chain is therefore:

**isoprenoid precursors → carotenoid biosynthesis → carotenoid accumulation/localization → visible pigmentation.**

Pigmentation is not equivalent to the mere presence of a *crt* gene. Strong trait evidence combines color or spectroscopy with chemical identification, pathway perturbation, or genetic complementation. For example, a 2023 *Mycobacterium kansasii* screen recovered 204 pigmentation mutants—0.14% of approximately 150,000 transposon mutants—and mapped most characterized insertions to carotenoid synthesis, cleavage, or fatty-acid-associated loci. Loss of *crtI* or *crtB* yielded off-white colonies after illumination, whereas restoration of the complete CRT locus restored the wild-type phenotype. (janisch2023geneticunderpinningsof pages 14-15, janisch2023geneticunderpinningsof pages 4-5)

### Boundaries

**Include:**

- Constitutive or environmentally induced carotenoid coloration.
- C40 carotenes and xanthophylls, including lycopene, β-carotene, astaxanthin, deinoxanthin, spheroidene, and spirilloxanthin.
- C30 carotenoid pigmentation such as staphyloxanthin, but as a separate taxon-specific branch.
- Color changes caused by altered carotenoid composition or accumulation, if chemically or genetically supported.

**Exclude or keep separate:**

- Non-carotenoid pigments such as melanin, prodigiosin, violacein, chlorophyll, flavins, and hemes.
- Uptake of exogenous carotenoids without microbial biosynthesis, unless the intended ontology scope explicitly includes acquired pigmentation.
- Carotenoid-pathway capacity inferred only from sequence, without demonstrated production or phenotype.
- Antioxidant, photoprotective, virulence, or membrane phenotypes as definitions of pigmentation. These are possible consequences of carotenoid accumulation, not the pigmentation trait itself.
- Color assignments based only on colony appearance where mixtures of lycopene, γ-carotene, β-carotene, or unrelated pigments were not resolved.

## Current mechanistic model

The most portable bacterial module is **IPP/DMAPP → GGPP → phytoene → an unsaturated carotene → downstream colored carotenoids**. CrtE supplies GGPP; CrtB condenses two GGPP molecules into 15-cis-phytoene; and CrtI performs sequential desaturation. CrtI product specificity varies: some enzymes terminate at neurosporene, whereas four-step enzymes produce lycopene. Cyclases and modifying enzymes then determine the final pigment. (sandmann2023genesandpathway pages 5-6, sandmann2023genesandpathway pages 3-5)

This model must not be treated as universal. In the green alga *Dunaliella salina*, phytoene-to-lycopene conversion follows a plant-like PDS–ZISO–ZDS–CRTISO sequence rather than relying mainly on one bacterial-type CrtI. Heterologous reconstruction also showed that DsZISO and DsCRTISO were essential for isomerization in the tested system. (chen2023engineeringtheβcarotene pages 1-3)

## Candidate nodes

### Trait and process nodes

- carotenoid pigmentation — **METPO:1003031**
- carotenoid biosynthetic process — **GO:0016117**
- isoprenoid biosynthetic process — GO grounding recommended after record verification
- carotenoid accumulation — label-only candidate
- photochromogenicity — label-only phenotype; condition-dependent subtype
- carotenoid degradation / cleavage — label-only process or verified GO term
- visible-light absorption — molecular/physical consequence, not itself the trait
- reactive oxygen species detoxification — downstream function; do not make obligatory

### Pathways and modules

- MEP/DOXP pathway for IPP and DMAPP
- mevalonate pathway, especially in fungi and engineered hosts
- conserved bacterial C40 carotenoid core: *crtE–crtB–crtI*
- lycopene cyclization module: *crtY* or lineage-specific cyclases
- *Dunaliella* plant-like module: GGPS–PSY–PDS–ZISO–ZDS–CRTISO–LYCB
- *Deinococcus* deinoxanthin branch: CrtLm–CruF–CrtD–CrtO–DR2473/CYP287A1
- purple-bacterial spheroidene/spirilloxanthin branches: CrtC–CrtD–CrtF–CrtA
- *S. aureus* C30 staphyloxanthin module: *crtOPQMN* plus *aldH*
- carotenoid-cleavage/apocarotenoid module: Cco1-like oxygenase

### Genes, proteins, enzymes, and regulators

- **crtE / CrtE** — geranylgeranyl-diphosphate synthase
- **crtB / CrtB** — phytoene synthase
- **crtI / CrtI** — phytoene desaturase/dehydrogenase
- **crtY, crtYc/crtYd / CrtY** — lycopene cyclase; homomeric or heteromeric forms
- **crtR / CrtR** — MarR-family repressor; function is lineage-specific
- **cco1, ccoR** — carotenoid-cleavage oxygenase and its regulator in *M. kansasii*
- **fnr1, desA3** — oleic-acid-associated functions affecting efficient pigment accumulation in *M. kansasii*
- **mmpL1/cg0722** — membrane-protein candidate associated with carotenoid loci/engineered yield; mechanistic role remains uncertain
- **PDS, ZISO, ZDS, CRTISO, LYCB** — plant-like algal enzymes
- **CrtLm, CruF, CrtD, CrtO, DR2473/CYP287A1** — deinoxanthin-pathway enzymes
- **CrtC, CrtD, CrtF, CrtA, TspO, RegA** — purple-bacterial branch enzymes/regulators
- **CrtM, CrtN, CrtO, CrtP, CrtQ** — staphyloxanthin branch enzymes

Use gene labels with a taxon qualifier. The same symbol—particularly *crtR*, *crtD*, or *crtO*—does not guarantee identical regulation or substrate specificity across organisms.

### Chemicals and metabolites

Recommended chemical nodes, with identifier verification during YAML implementation:

- isopentenyl diphosphate (IPP)
- dimethylallyl diphosphate (DMAPP)
- farnesyl diphosphate (FPP)
- geranylgeranyl diphosphate (GGPP)
- 15-cis-phytoene
- phytofluene
- neurosporene
- lycopene
- γ-carotene
- β-carotene
- zeaxanthin
- astaxanthin
- spheroidene and spheroidenone
- spirilloxanthin
- 2-deoxydeinoxanthin and deinoxanthin
- 4,4′-diapophytoene, 4,4′-diaponeurosporene, and staphyloxanthin
- apocarotenoids
- molecular oxygen, water, NAD(P)H, quinones, Mg²⁺/Mn²⁺
- oleic acid
- sodium selenite
- diphenylamine, celastrol, phosphate, and squalestatin as inhibitors or experimental factors

### Environmental and experimental nodes

- light exposure; wavelength and duration should be recorded
- ultraviolet light
- dark growth
- oxygen availability / aerobic transition
- oxidative metabolism and oxidative phosphorylation
- ROS and free-radical stress
- carbon source: lactate, dextrose/glucose, glycerol, or sucrose
- sodium selenite concentration
- temperature
- nutrient limitation
- gene deletion, transposon insertion, complementation, and overexpression
- fed-batch fermentation
- colony-color assay, absorbance spectroscopy, HPLC/LC–MS, Raman spectroscopy, and pigment extraction

### Cellular localization

Carotenoids are hydrophobic and frequently membrane-associated. A 2023 review notes that most carotenogenic enzymes studied in purple bacteria are membrane-bound, while lycopene in engineered *Corynebacterium glutamicum* was described as distributed in lipid structures. Staphyloxanthin is explicitly a membrane-bound C30 carotenoid. These statements support membrane/lipid localization nodes, but localization should remain pigment- and taxon-specific. (sandmann2023genesandpathway pages 5-6, zhan2024expandingthecrispr pages 10-12, yehia2022celastrolmitigatesstaphyloxanthin pages 1-2)

## Priority causal edges

The following shortlist combines conserved reactions with direct phenotype perturbations. The table labels engineered-host and lineage-specific findings so they are not mistaken for universal edges.

| subject | predicate | object | taxon/context | evidence strength | DOI |
|---|---|---|---|---|---|
| CrtE | produces | geranylgeranyl pyrophosphate (GGPP) | conserved bacterial carotenoid core; review synthesis | strong review, broad but not direct trait assay (sandmann2023genesandpathway pages 5-6, janisch2023geneticunderpinningsof pages 4-5) | 10.3390/biology12101346 |
| CrtB | converts | 2 GGPP to 15-cis-phytoene | conserved bacterial carotenoid core; review synthesis | strong review, broad but not direct trait assay (sandmann2023genesandpathway pages 5-6) | 10.3390/biology12101346 |
| CrtI | desaturates | phytoene to lycopene or neurosporene, depending on pathway | conserved bacterial core with pathway-specific caveat | strong review; branch outcome taxon-specific (sandmann2023genesandpathway pages 8-10, sandmann2023genesandpathway pages 3-5) | 10.3390/biology12101346 |
| CrtY (lycopene cyclase) | cyclizes | lycopene to β-carotene | conserved bacterial cyclic-carotene branch | strong review plus organism-specific mapping (sandmann2023genesandpathway pages 5-6, janisch2023geneticunderpinningsof pages 4-5) | 10.3390/biology12101346 |
| light exposure | upregulates | crtE/crtI/crtB/crtYc/crtYd expression | Mycobacterium kansasii photochromogenicity | direct transcript/phenotype evidence (janisch2023geneticunderpinningsof pages 8-10) | 10.3390/pathogens12010086 |
| crtI loss-of-function | abolishes | light-induced carotenoid pigmentation (WW phenotype) | Mycobacterium kansasii transposon mutants | direct mutant evidence (janisch2023geneticunderpinningsof pages 14-15) | 10.3390/pathogens12010086 |
| crtB loss-of-function | abolishes | light-induced carotenoid pigmentation (WW phenotype) | Mycobacterium kansasii transposon mutants | direct mutant evidence (janisch2023geneticunderpinningsof pages 14-15) | 10.3390/pathogens12010086 |
| crtYc or crtYd disruption | shifts | yellow WT-like light phenotype toward orange intermediate pigmentation | Mycobacterium kansasii; likely impaired β-cyclization | direct mutant evidence, product identity uncertain (janisch2023geneticunderpinningsof pages 14-15) | 10.3390/pathogens12010086 |
| CrtR (MarR-type regulator) | represses | carotenogenesis genes in the dark | Mycobacterium kansasii | direct RT-qPCR and mutant phenotype evidence (janisch2023geneticunderpinningsof pages 8-10) | 10.3390/pathogens12010086 |
| ccoRMk | represses | cco1Mk carotenoid breakdown pathway | Mycobacterium kansasii | direct RT-qPCR evidence (janisch2023geneticunderpinningsof pages 17-19) | 10.3390/pathogens12010086 |
| cco1Mk overexpression | decreases | light-induced carotenoid pigmentation | Mycobacterium kansasii; inferred carotene degradation to apocarotenoids | direct regulatory/phenotype evidence, mechanism partly inferred (janisch2023geneticunderpinningsof pages 17-19) | 10.3390/pathogens12010086 |
| oleic acid supplementation | partially restores | pigment photoinduction defect | Mycobacterium kansasii fnr1/desA3 mutants | direct rescue evidence, mutant-specific (janisch2023geneticunderpinningsof pages 17-19) | 10.3390/pathogens12010086 |
| crtEb deletion plus crtR deletion | increases | lycopene accumulation and pink colony phenotype | Corynebacterium glutamicum engineering | direct engineered-host evidence (zhan2024expandingthecrispr pages 10-12, zhan2024expandingthecrispr pages 2-3) | 10.3390/microorganisms12040803 |
| cg0722 + crtB + crtI overexpression | increases | lycopene production | Corynebacterium glutamicum engineering | direct engineered-host evidence (zhan2024expandingthecrispr pages 10-12) | 10.3390/microorganisms12040803 |
| PDS + ZISO + ZDS + CRTISO | converts | phytoene to all-trans-lycopene | Dunaliella salina plant-like algal pathway | direct heterologous reconstruction evidence; algal-specific variant (chen2023engineeringtheβcarotene pages 1-3) | 10.1128/spectrum.04361-22 |
| DsLYCB | cyclizes | 7,7′,9,9′-tetra-cis-lycopene to β-carotene | Dunaliella salina heterologous reconstruction | direct algal-specific evidence (chen2023engineeringtheβcarotene pages 1-3) | 10.1128/spectrum.04361-22 |
| oxidative phosphorylation on lactate (YPLac) | increases | carotenoid production | Rhodotorula mucilaginosa | direct environmental physiology evidence (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2) | 10.3389/ffunb.2024.1378590 |
| sodium selenite (1–3 mM) | increases | total and cellular carotenoids | Rhodotorula glutinis in YPD | direct quantitative culture evidence (elfeky2024exploringthelipids pages 1-2) | 10.1186/s12866-024-03585-x |
| celastrol | inhibits | CrtM-dependent staphyloxanthin biosynthesis | Staphylococcus aureus C30 carotenoid branch | direct inhibitor/intermediate evidence; branch-specific (yehia2022celastrolmitigatesstaphyloxanthin pages 1-2) | 10.1186/s12866-022-02515-z |
| CrtLm | cyclizes | lycopene to γ-carotene | Deinococcus branch toward deinoxanthin | strong review of pathway synthesis; branch-specific (wang2024insightsintothe pages 5-6) | 10.3389/fmicb.2024.1447785 |
| CruF | hydrates | γ-carotene at C-1′,2′ | Deinococcus branch toward deinoxanthin | strong review of pathway synthesis; branch-specific (wang2024insightsintothe pages 5-6) | 10.3389/fmicb.2024.1447785 |
| CrtD | desaturates | hydroxylated monocyclic carotenoid at C-3′,4′ | Deinococcus branch toward deinoxanthin | strong review of pathway synthesis; branch-specific (wang2024insightsintothe pages 5-6) | 10.3389/fmicb.2024.1447785 |
| DR2473 (2-β-hydroxylase) | forms | deinoxanthin from 2-deoxydeinoxanthin | Deinococcus radiodurans final branch step | review-backed, based on prior primary genetics (wang2024insightsintothe pages 5-6, wang2024insightsintothe pages 12-12) | 10.3389/fmicb.2024.1447785 |
| crtB or crtI knockout | abolishes | carotenoid biosynthetic pathway and color | Deinococcus radiodurans R1 | review-backed direct primary knockout result (wang2024insightsintothe pages 12-12) | 10.3389/fmicb.2024.1447785 |


*Table: This table summarizes compact, high-priority causal edges for curating carotenoid pigmentation, emphasizing conserved pathway steps and the strongest organism-specific regulatory or perturbational evidence. It is useful as a first-pass TraitMech edge shortlist while keeping taxon-specific branches and engineered-host findings clearly labeled.*

### Additional edge-level evidence and curation notes

| Proposed triple | Supporting source wording | Curation assessment |
|---|---|---|
| CrtE — produces → GGPP | “The reaction catalysed by CrtE provides geranylgeranyl pyrophosphate (GGPP).” | Strong biochemical review support. Curate as a core reaction, not a direct pigmentation edge. (sandmann2023genesandpathway pages 5-6) |
| CrtB — converts → 2 GGPP to 15-cis-phytoene | “CrtB…converts two molecules of GGPP to 15-cis phytoene.” | Strong core reaction. The cited enzyme characterization was from *Erwinia/Pantoea*-type material, so avoid claiming every CrtB has identical cofactor properties. (sandmann2023genesandpathway pages 5-6) |
| phosphate or squalestatin — inhibits → CrtB activity | CrtB was described as ATP- and Mn²⁺/Mg²⁺-dependent and “inhibited by phosphate ions and squalestatin.” | Biochemical, enzyme-specific edge; suitable only with source-organism/context qualifiers. (sandmann2023genesandpathway pages 5-6) |
| *crtI* disruption — causes → phytoene accumulation | “Analysis of crtI-deficient mutants that accumulated phytoene revealed that this gene encodes a phytoene desaturase.” | Strong direct genetics in *Rhodobacter capsulatus*. (sandmann2023genesandpathway pages 3-5) |
| light and oxygen — increase → carotenoid-pathway transcription | “Light and oxygen are the dominating regulatory factors”; the *crtI-crtB* operon was upregulated by oxygen. | Strong for *Rhodobacter* spp.; not universal. (sandmann2023genesandpathway pages 3-5) |
| TspO — negatively regulates → *crtA* and *crtI* | A *tspO* deletion produced higher *crtA* and *crtI* transcript levels than wild type. | Direct regulatory genetics, purple-bacteria branch only. (sandmann2023genesandpathway pages 3-5) |
| *crtI* or *crtB* disruption — abolishes → light-induced pigmentation | Insertions led to the “WW phenotype” regardless of transposon orientation; the complete CRT locus restored wild-type coloration. | Among the strongest trait-defining edges for *M. kansasii*. (janisch2023geneticunderpinningsof pages 14-15) |
| *crtYc/crtYd* disruption — changes → yellow-to-orange coloration | Mutants shifted toward orange after light; complementation shifted them toward wild-type yellow. | Direct color phenotype, but γ-carotene versus pigment-mixture identity remains unresolved. Mark product explanation uncertain. (janisch2023geneticunderpinningsof pages 14-15) |
| loss of CrtR — increases → dark carotenogenesis | *crtR* disruption drastically upregulated *crtE*, *mmpL1*, and *fni* and produced constitutive pigmentation. | Strong direct regulatory evidence in *M. kansasii*. (janisch2023geneticunderpinningsof pages 8-10) |
| loss of CcoR — increases → *cco1* expression | Loss of *ccoR* caused approximately 100-fold *cco1* upregulation. | Strong transcript edge. The further chain to carotene degradation is biologically persuasive but partly inferred. (janisch2023geneticunderpinningsof pages 17-19) |
| Cco1-dependent cleavage — decreases → carotenoid pigmentation | Authors attribute absent light-induced pigmentation to exacerbated Cco1-dependent degradation and apocarotenoid production. | Curate as **uncertain/proposed** unless direct carotenoid/apocarotenoid chemistry is added. (janisch2023geneticunderpinningsof pages 17-19) |
| oleic acid — partially restores → photoinduction in *fnr1/desA3* mutants | Supplementation “partially corrected the pigment photoinduction defect.” | Direct rescue but mutant- and condition-specific; oleic acid is not generally required for carotenogenesis. (janisch2023geneticunderpinningsof pages 17-19) |
| PDS–ZISO–ZDS–CRTISO — converts → phytoene to all-trans-lycopene | *D. salina* reconstruction showed plant-like conversion and essential isomerization roles for DsZISO and DsCRTISO. | Strong heterologous functional evidence; curate only under an algal branch. (chen2023engineeringtheβcarotene pages 1-3) |
| lactate-supported oxidative metabolism — increases → carotenoid production | Lactate supported “high respiratory activity and carotenoid production,” whereas dextrose supported low oxygen consumption and low carotenoid expression. | Direct physiology in *R. mucilaginosa*; the proposed ROS-mediated induction is plausible but not fully causal. (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2) |
| diphenylamine — inhibits → phytoene desaturation/carotenoid production | The study states that DPA blocks sequential phytoene desaturation and used it to unmask ROS. | Useful inhibitor edge, but based partly on prior literature and not necessarily CrtI-specific in every organism. (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2) |
| sodium selenite — increases → carotenoid accumulation | In YPD, 1 and 3 mM selenite increased carotenoids by 22.8% and 48.7%, respectively. | Direct quantitative edge in *R. glutinis* under defined media; not a general environmental preference. (elfeky2024exploringthelipids pages 1-2) |
| celastrol — inhibits → CrtM-dependent staphyloxanthin synthesis | LC–MS/intermediate measurements showed pigment inhibition with FPP accumulation. | Strong experimental inhibitor evidence, but C30 staphyloxanthin-specific. (yehia2022celastrolmitigatesstaphyloxanthin pages 1-2) |
| CrtM — converts → 2 FPP to 4,4′-diapophytoene | “Condensation of two molecules of farnesyl diphosphate to form 4,4′-diapophytoene…is catalyzed by…CrtM.” | Strong C30 pathway edge. Keep separate from the C40 CrtB reaction. (yehia2022celastrolmitigatesstaphyloxanthin pages 1-2) |
| CrtN — converts → 4,4′-diapophytoene to 4,4′-diaponeurosporene | The precursor “undergoes dehydrogenation by…CrtN.” | Strong pathway edge, *S. aureus* branch. (yehia2022celastrolmitigatesstaphyloxanthin pages 1-2) |

## Recent developments, applications, and statistics

### 2023–2024 mechanistic developments

1. **Direct genetic resolution of photochromogenicity.** The 2023 *M. kansasii* study connected biosynthesis, degradation, regulation, and fatty-acid metabolism to light-dependent colony color. Light increased RNA-seq read counts approximately 160-fold for *crtE*, 161-fold for *crtI*, 141-fold for *crtB*, 221-fold for *crtYc*, and 334-fold for *crtYd* under the reported comparison. These are transcript changes, not equivalent increases in pigment concentration. (janisch2023geneticunderpinningsof pages 8-10)

2. **Algal pathway clarification.** Functional reconstruction demonstrated that *D. salina* uses a plant-like multi-enzyme route from phytoene to lycopene. The species can accumulate β-carotene to as much as approximately 10% of dry weight under the cited conditions, illustrating that an algal branch can produce an especially strong pigmentation phenotype. (chen2023engineeringtheβcarotene pages 1-3)

3. **Stress-responsive red-yeast systems.** In *Xanthophyllomyces dendrorhous*, 2024 transcriptomics found that light primarily upregulated terpenoid biosynthesis through *crtI*, whereas oxidative stress upregulated several pathway genes. The study produced 26 characterized promoter elements, including one promoter with ninefold activation under UV, providing tools for controlled carotenoid engineering. (tobin2024omicsdrivenonboardingof pages 1-2)

4. **Physiology rather than sequence alone.** A 2024 *R. mucilaginosa* study linked lactate-supported oxidative phosphorylation, increased ROS, and increased carotenoid synthesis. It also cautioned that carotenoids exposed to strong radical chemistry may be inactivated or become pro-oxidant. Thus, the edge “ROS increases pigmentation” should remain conditional rather than universal. (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2)

### Industrial and real-world implementation

Microbial carotenoids are used or being developed as food/feed colorants, antioxidants, cosmetic ingredients, nutraceuticals, and pharmaceutical intermediates. Engineering commonly increases precursor supply, removes competing branches, balances *crt* expression, and optimizes oxygen, carbon source, temperature, and fermentation.

A 2024 *C. glutamicum* implementation illustrates the distinction between pigmentation biology and production engineering. Deleting *crtEb* and *crtR* and overexpressing *cg0722-crtB-crtI* increased lycopene, shifted colonies from light yellow toward pink, and produced 405.02 mg/L—9.52 mg/g dry-cell weight—at 96 h in a 5-L fed-batch process. The engineered strain reached OD600 228. These results provide strong causal perturbation evidence, but the large titer is not a natural-trait baseline. (zhan2024expandingthecrispr pages 10-12, zhan2024expandingthecrispr pages 2-3)

In *R. glutinis*, low-dose sodium selenite offers a feed-biotechnology example: 1 mM and 3 mM in YPD increased total/cellular carotenoids to 646.7 µg/L and 32.12 µg/g, and 783.3 µg/L and 36.43 µg/g, respectively. At high concentration, however, selenite damaged organelles and membranes, demonstrating a dose-dependent boundary. (elfeky2024exploringthelipids pages 1-2)

Staphyloxanthin is a different application domain: it is a membrane-bound virulence-associated carotenoid that gives *S. aureus* its golden-yellow appearance. In one study, 94 of 100 clinical isolates exceeded the authors’ OD465 pigmentation threshold. Celastrol suppressed CrtM-dependent pigment formation and increased susceptibility to environmental stress, blood killing, and membrane-targeting antibiotics, making pigmentation enzymes potential anti-virulence targets. (yehia2022celastrolmitigatesstaphyloxanthin pages 4-5, yehia2022celastrolmitigatesstaphyloxanthin pages 1-2)

For *Deinococcus*, carotenoid engineering is being explored for natural antioxidants, stress-tolerant cell factories, and possible radiation-related applications. A 2024 review reported engineered deinoxanthin production of 256.5 ± 13.8 mg/L at 37°C—290% above wild type—and 394 ± 17.6 mg/L after replacing glucose with sucrose—446% above wild type. These values derive from engineering studies summarized by the review and should be cited as secondary evidence. (wang2024insightsintothe pages 8-9)

## Recommended graph architecture

A robust YAML graph should separate a **small shared core** from taxon-specific extensions:

1. **Core precursor layer:** MEP or MVA pathway → IPP/DMAPP → GGPP.
2. **Core C40 layer:** CrtE → GGPP; CrtB → phytoene; CrtI or lineage-equivalent enzymes → colored acyclic carotene.
3. **Diversification layer:** cyclization, hydroxylation, ketolation, glycosylation, esterification, and cleavage.
4. **Accumulation layer:** hydrophobic pigment associates with membrane/lipid structures → visible absorption → METPO:1003031.
5. **Conditional regulation layer:** light, oxygen, oxidative metabolism, carbon source, nutrient state, and regulators.
6. **Taxon modules:** mycobacterial photochromogenic, algal plant-like, purple-bacterial, deinoxanthin, fungal/yeast, and staphyloxanthin branches.

The graph should not encode “carotenoids → oxidative-stress resistance → pigmentation.” Antioxidant protection is generally a downstream consequence parallel to visible coloration.

## Ontology-grounding guidance

- Use **METPO:1003031** verbatim for the trait.
- **GO:0016117** is an appropriate candidate for carotenoid biosynthetic process.
- Ground individual metabolites to ChEBI only after exact stereochemistry/protonation is selected. “Phytoene,” “lycopene,” and “β-carotene” may have separate records for generic versus specific isomers.
- Use EC/Rhea identifiers only after the precise substrate/product reaction and enzyme form are verified. CrtI reactions differ in the number of desaturations, and CrtY enzymes differ in ring number and substrate scope.
- Ground organisms to NCBITaxon at strain level where possible because the strongest evidence is strain-specific.
- Retain *M. kansasii* locus tags such as MKAN_RS10020 (*crtE*) and MKAN_RS10025 (*crtI*) when curating that experiment; do not transfer them to other taxa. (janisch2023geneticunderpinningsof pages 8-10)
- Label-only nodes are preferable to uncertain or invented CURIEs.

## Warnings: claims not yet ready for unqualified curation

1. **Do not make light obligatory.** It is causal for photochromogenic *M. kansasii*, but many microbes pigment constitutively or respond differently to wavelength and intensity.
2. **Do not equate orange color with γ-carotene.** The *crtYc/crtYd* mutant interpretation explicitly allows mixtures of lycopene, γ-carotene, and β-carotene. (janisch2023geneticunderpinningsof pages 14-15)
3. **Do not universalize CrtI → lycopene.** Some CrtI proteins terminate at neurosporene, and algae can use PDS/ZISO/ZDS/CRTISO. (chen2023engineeringtheβcarotene pages 1-3, sandmann2023genesandpathway pages 3-5)
4. **Do not universalize CrtR.** MarR-family regulators with the same label can control different loci and have organism-specific effects.
5. **Mark Cco1-mediated loss of pigmentation as partly inferred.** The approximately 100-fold transcriptional effect is direct, but the proposed carotene-to-apocarotenoid flux requires stronger chemical confirmation. (janisch2023geneticunderpinningsof pages 17-19)
6. **Keep ROS induction conditional.** In red yeast, increased carotenoids correlated with oxidative metabolism, while oxidized carotenoid extracts could inhibit growth. (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2)
7. **Do not merge staphyloxanthin with the C40 CrtE/B/I/Y core.** It is a C30 FPP-derived pathway initiated by CrtM and CrtN. (yehia2022celastrolmitigatesstaphyloxanthin pages 1-2)
8. **Do not treat engineered titers as natural phenotype prevalence.** They support causal pathway capacity and applications, not wild-type trait magnitude.
9. **Do not infer pigmentation from antioxidant function alone.** A carotenoid can be functionally detected without establishing an assay-visible morphology.
10. **The supplied 2025 review is useful background but outside the requested 2023–2024 priority window.** Its statement that carotenoids are isoprenoid pigments supports the class definition but does not replace primary mechanistic evidence.

## DOI-first bibliography

1. Janisch N, Levendosky K, Budell WC, Quadri LEN. **Genetic Underpinnings of Carotenogenesis and Light-Induced Transcriptome Remodeling in the Opportunistic Pathogen *Mycobacterium kansasii*.** *Pathogens*. Published January 2023. DOI: [10.3390/pathogens12010086](https://doi.org/10.3390/pathogens12010086). (janisch2023geneticunderpinningsof pages 17-19, janisch2023geneticunderpinningsof pages 14-15, janisch2023geneticunderpinningsof pages 8-10)
2. Sandmann G. **Genes and Pathway Reactions Related to Carotenoid Biosynthesis in Purple Bacteria.** *Biology*. Published October 2023. DOI: [10.3390/biology12101346](https://doi.org/10.3390/biology12101346). (sandmann2023genesandpathway pages 5-6, sandmann2023genesandpathway pages 8-10, sandmann2023genesandpathway pages 3-5)
3. Chen H-H et al. **Engineering the β-Carotene Metabolic Pathway of Microalgae *Dunaliella* to Confirm Its Carotenoid Synthesis Pattern in Comparison to Bacteria and Plants.** *Microbiology Spectrum*. Published January 31, 2023. DOI: [10.1128/spectrum.04361-22](https://doi.org/10.1128/spectrum.04361-22). (chen2023engineeringtheβcarotene pages 1-3)
4. Zhan Z et al. **Expanding the CRISPR Toolbox for Engineering Lycopene Biosynthesis in *Corynebacterium glutamicum*.** *Microorganisms*. Published April 2024. DOI: [10.3390/microorganisms12040803](https://doi.org/10.3390/microorganisms12040803). (zhan2024expandingthecrispr pages 10-12, zhan2024expandingthecrispr pages 2-3)
5. Mosqueda-Martínez E et al. **In *Rhodotorula mucilaginosa*, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species.** *Frontiers in Fungal Biology*. Published September 6, 2024. DOI: [10.3389/ffunb.2024.1378590](https://doi.org/10.3389/ffunb.2024.1378590). (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2)
6. Elfeky N, Rizk A, Gharieb MM. **Exploring the lipids, carotenoids, and vitamins content of *Rhodotorula glutinis* with selenium supplementation.** *BMC Microbiology*. Published November 2024. DOI: [10.1186/s12866-024-03585-x](https://doi.org/10.1186/s12866-024-03585-x). (elfeky2024exploringthelipids pages 1-2)
7. Tobin EE et al. **Omics-driven onboarding of the carotenoid producing red yeast *Xanthophyllomyces dendrorhous* CBS 6938.** *Applied Microbiology and Biotechnology*. Accepted December 6, 2024. DOI: [10.1007/s00253-024-13379-w](https://doi.org/10.1007/s00253-024-13379-w). (tobin2024omicsdrivenonboardingof pages 1-2)
8. Wang Y et al. **Insights into the synthesis, engineering, and functions of microbial pigments in *Deinococcus* bacteria.** *Frontiers in Microbiology*. Published July 2024. DOI: [10.3389/fmicb.2024.1447785](https://doi.org/10.3389/fmicb.2024.1447785). (wang2024insightsintothe pages 8-9, wang2024insightsintothe pages 5-6)
9. Yehia FAA, Yousef N, Askoura M. **Celastrol mitigates staphyloxanthin biosynthesis and biofilm formation in *Staphylococcus aureus*.** *BMC Microbiology*. Published April 2022. DOI: [10.1186/s12866-022-02515-z](https://doi.org/10.1186/s12866-022-02515-z). (yehia2022celastrolmitigatesstaphyloxanthin pages 4-5, yehia2022celastrolmitigatesstaphyloxanthin pages 1-2)
10. Saini RK, Keum Y-S. **Microbial platforms to produce commercially vital carotenoids at industrial scale: an updated review of critical issues.** *Journal of Industrial Microbiology & Biotechnology*. Published May 2019. DOI: [10.1007/s10295-018-2104-7](https://doi.org/10.1007/s10295-018-2104-7). This is older, secondary evidence useful mainly for industrial context. (saini2019microbialplatformsto pages 11-13)

References

1. (janisch2023geneticunderpinningsof pages 14-15): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

2. (janisch2023geneticunderpinningsof pages 4-5): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

3. (sandmann2023genesandpathway pages 5-6): Gerhard Sandmann. Genes and pathway reactions related to carotenoid biosynthesis in purple bacteria. Biology, 12:1346, Oct 2023. URL: https://doi.org/10.3390/biology12101346, doi:10.3390/biology12101346. This article has 17 citations.

4. (sandmann2023genesandpathway pages 3-5): Gerhard Sandmann. Genes and pathway reactions related to carotenoid biosynthesis in purple bacteria. Biology, 12:1346, Oct 2023. URL: https://doi.org/10.3390/biology12101346, doi:10.3390/biology12101346. This article has 17 citations.

5. (chen2023engineeringtheβcarotene pages 1-3): Hao-Hong Chen, Ming-Hua Liang, Zhi-Wei Ye, Yue-Hui Zhu, and Jian-Guo Jiang. Engineering the β-carotene metabolic pathway of microalgae <i>dunaliella</i> to confirm its carotenoid synthesis pattern in comparison to bacteria and plants. Microbiology Spectrum, Apr 2023. URL: https://doi.org/10.1128/spectrum.04361-22, doi:10.1128/spectrum.04361-22. This article has 37 citations and is from a domain leading peer-reviewed journal.

6. (zhan2024expandingthecrispr pages 10-12): Zhimin Zhan, Xiong Chen, Zhifang Ye, Ming Zhao, Cheng Li, Shipeng Gao, Anthony J. Sinskey, Lan Yao, Jun Dai, Yiming Jiang, and Xueyun Zheng. Expanding the crispr toolbox for engineering lycopene biosynthesis in corynebacterium glutamicum. Microorganisms, 12:803, Apr 2024. URL: https://doi.org/10.3390/microorganisms12040803, doi:10.3390/microorganisms12040803. This article has 9 citations.

7. (yehia2022celastrolmitigatesstaphyloxanthin pages 1-2): Fatma Al-zahraa A. Yehia, Nehal Yousef, and Momen Askoura. Celastrol mitigates staphyloxanthin biosynthesis and biofilm formation in staphylococcus aureus via targeting key regulators of virulence; in vitro and in vivo approach. BMC Microbiology, Apr 2022. URL: https://doi.org/10.1186/s12866-022-02515-z, doi:10.1186/s12866-022-02515-z. This article has 41 citations and is from a peer-reviewed journal.

8. (sandmann2023genesandpathway pages 8-10): Gerhard Sandmann. Genes and pathway reactions related to carotenoid biosynthesis in purple bacteria. Biology, 12:1346, Oct 2023. URL: https://doi.org/10.3390/biology12101346, doi:10.3390/biology12101346. This article has 17 citations.

9. (janisch2023geneticunderpinningsof pages 8-10): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

10. (janisch2023geneticunderpinningsof pages 17-19): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

11. (zhan2024expandingthecrispr pages 2-3): Zhimin Zhan, Xiong Chen, Zhifang Ye, Ming Zhao, Cheng Li, Shipeng Gao, Anthony J. Sinskey, Lan Yao, Jun Dai, Yiming Jiang, and Xueyun Zheng. Expanding the crispr toolbox for engineering lycopene biosynthesis in corynebacterium glutamicum. Microorganisms, 12:803, Apr 2024. URL: https://doi.org/10.3390/microorganisms12040803, doi:10.3390/microorganisms12040803. This article has 9 citations.

12. (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2): Edson Mosqueda-Martínez, Natalia Chiquete-Félix, Paulina Castañeda-Tamez, Carolina Ricardez-García, Manuel Gutiérrez-Aguilar, Salvador Uribe-Carvajal, and Ofelia Mendez-Romero. In rhodotorula mucilaginosa, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species. Frontiers in Fungal Biology, Sep 2024. URL: https://doi.org/10.3389/ffunb.2024.1378590, doi:10.3389/ffunb.2024.1378590. This article has 24 citations.

13. (elfeky2024exploringthelipids pages 1-2): Nora Elfeky, Aya Rizk, and Mohamed M. Gharieb. Exploring the lipids, carotenoids, and vitamins content of rhodotorula glutinis with selenium supplementation under lipid accumulating and growth proliferation conditions. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03585-x, doi:10.1186/s12866-024-03585-x. This article has 8 citations and is from a peer-reviewed journal.

14. (wang2024insightsintothe pages 5-6): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 18 citations and is from a peer-reviewed journal.

15. (wang2024insightsintothe pages 12-12): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 18 citations and is from a peer-reviewed journal.

16. (tobin2024omicsdrivenonboardingof pages 1-2): Emma E. Tobin, Joseph H. Collins, Celeste B. Marsan, Gillian T. Nadeau, Kim Mori, Anna Lipzen, Stephen Mondo, Igor V. Grigoriev, and Eric M. Young. Omics-driven onboarding of the carotenoid producing red yeast xanthophyllomyces dendrorhous cbs 6938. Dec 2024. URL: https://doi.org/10.1007/s00253-024-13379-w, doi:10.1007/s00253-024-13379-w. This article has 6 citations and is from a domain leading peer-reviewed journal.

17. (yehia2022celastrolmitigatesstaphyloxanthin pages 4-5): Fatma Al-zahraa A. Yehia, Nehal Yousef, and Momen Askoura. Celastrol mitigates staphyloxanthin biosynthesis and biofilm formation in staphylococcus aureus via targeting key regulators of virulence; in vitro and in vivo approach. BMC Microbiology, Apr 2022. URL: https://doi.org/10.1186/s12866-022-02515-z, doi:10.1186/s12866-022-02515-z. This article has 41 citations and is from a peer-reviewed journal.

18. (wang2024insightsintothe pages 8-9): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 18 citations and is from a peer-reviewed journal.

19. (saini2019microbialplatformsto pages 11-13): Ramesh Kumar Saini and Young-Soo Keum. Microbial platforms to produce commercially vital carotenoids at industrial scale: an updated review of critical issues. Journal of Industrial Microbiology & Biotechnology, 46:657-674, May 2019. URL: https://doi.org/10.1007/s10295-018-2104-7, doi:10.1007/s10295-018-2104-7. This article has 189 citations and is from a peer-reviewed journal.