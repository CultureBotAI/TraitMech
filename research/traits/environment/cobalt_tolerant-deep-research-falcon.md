---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:09:29.020286'
end_time: '2026-08-04T00:19:38.183040'
duration_seconds: 609.16
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: cobalt tolerant
  trait_identifier: traitmech:000015
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: cobalt_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metal tolerance in which an organism grows in the presence of elevated
    cobalt (Co2+) concentrations, typically via cation-efflux resistance systems such
    as the czc and cnr determinants.
  parent_traits: traitmech:000012
  synonyms: ''
  evidence_summary: 'DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition
    metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system
    of Cupriavidus metallidurans confers cobalt resistance.) | DOI:10.3389/fmicb.2020.00047:
    C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+
    (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and
    Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cobalt
    to a MIC of 20 mM.)'
  causal_graph_summary: 'cobalt_tolerance_czc_cnr_efflux: 11 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cobalt tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000015
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated cobalt (Co2+) concentrations, typically via cation-efflux resistance systems such as the czc and cnr determinants.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers cobalt resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cobalt to a MIC of 20 mM.)
- **Existing causal graph summary:** cobalt_tolerance_czc_cnr_efflux: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **cobalt tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/cobalt_tolerant.yaml`.

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
- **Trait label:** cobalt tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000015
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated cobalt (Co2+) concentrations, typically via cation-efflux resistance systems such as the czc and cnr determinants.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers cobalt resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cobalt to a MIC of 20 mM.)
- **Existing causal graph summary:** cobalt_tolerance_czc_cnr_efflux: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **cobalt tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/cobalt_tolerant.yaml`.

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


# TraitMech curation report: cobalt tolerant

**Trait label:** cobalt tolerant  
**Trait identifier:** `traitmech:000015`  
**Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED  
**Parent:** `traitmech:000012`

## 1. Scope summary

The trait should denote the experimentally observable capacity of a microorganism to **grow or remain viable at an elevated, bioavailable concentration of cobalt, ordinarily supplied as Co(II)**. Operational evidence includes growth curves, EC50/IC50, MIC, survival, or competitive-fitness measurements under a defined cobalt salt concentration. For example, wild-type *Rhodobacter sphaeroides* had a reported Co²⁺ EC50 of 0.8 mM, whereas an evolved strain grew without appreciable inhibition at 4 mM CoCl₂ after selection through concentrations up to 15 mM. This is a direct cobalt-tolerance phenotype, although the numerical threshold remains medium- and assay-dependent. (atay2024evolutionaryengineeringand pages 1-2)

The current mechanistic model is **regulated cobalt homeostasis rather than a single resistance reaction**. Surplus cytoplasmic Co(II) can be transferred to the periplasm by an inner-membrane exporter such as DmeF; proton-motive-force-driven CzcCBA and CnrCBA complexes then remove periplasmic cobalt across the cell envelope. This lowers cobalt exposure of sensitive cellular targets and supports growth at elevated external cobalt. (nies2016thebiologicalchemistry pages 25-25, nies2016thebiologicalchemistry pages 15-16, nies2016thebiologicalchemistry pages 19-19)

### Boundaries

Include:

- Growth, survival, or fitness under explicitly elevated Co(II).
- Genetically demonstrated cobalt efflux that increases the cobalt-resistance phenotype.
- Regulatory responses when they are causally connected to cobalt-efflux gene expression.
- Taxon-specific alternative mechanisms when independently validated.

Do not equate the trait with:

- **Normal cobalt acquisition or cobalamin metabolism.** Trace cobalt is a nutrient; uptake at nutritional concentrations is not cobalt tolerance.
- **Cobalt accumulation, adsorption, or biosorption alone.** These can accompany tolerance but do not prove growth under cobalt stress.
- **A `czc`, `cnr`, `rcnA`, or other annotation alone.** Many systems have overlapping Zn/Cd/Ni/Co specificity, and genomic presence does not establish expression or phenotype.
- **General heavy-metal tolerance.** Cross-resistance to Ni, Zn, Cd, Cu, or Fe is supporting context, not a substitute for a cobalt assay.
- **An absolute universal concentration threshold.** Cobalt salt, pH, medium ligands, inoculum, exposure time, and endpoint alter bioavailability and MIC.

## 2. Current mechanistic understanding

### Core Czc/Cnr model

In *Cupriavidus metallidurans*, CzcCBA and CnrCBA are tripartite RND-family transenvelope systems. The inner-membrane RND transporter, membrane-fusion adaptor, and outer-membrane factor form a continuous route from the periplasm to the extracellular space. RND transport is powered by the proton motive force. (galea2024linkingthetranscriptome pages 3-4, nies2016thebiologicalchemistry pages 15-16)

CzcCBA is assembled from CzcA, the inner-membrane RND transporter; CzcB, the membrane-fusion component; and CzcC, the outer-membrane exit factor. Complementation evidence is especially useful for graph curation: CzcA alone provided some cobalt resistance, CzcBA provided only low cobalt resistance, and addition of CzcC restored full resistance to cobalt, zinc, and cadmium toward wild-type levels. This supports a causal complex-assembly path rather than treating each subunit as an independently sufficient cobalt exporter. (grosse2022lossofmobile pages 18-19)

CnrCBA also exports Co(II), although it is principally associated with nickel resistance. An authoritative transportome synthesis attributes an approximately 300-fold increase in cobalt resistance to RND-mediated Cnr/Czc-level protection and identifies CnrCBA as an in-vivo cobalt exporter. The magnitude is useful but should be curated as organism- and experimental-context-specific, not universal. (nies2016thebiologicalchemistry pages 19-19)

### Regulation and homeostatic control

The 2023 analysis of Czc regulation showed that the response regulator CzcR is required for upregulation of `czcN` and `czcP`, while cross-talk among CzcRS, CzcR2S2, and AgrRS tunes expression according to metal concentration. This indicates that cobalt tolerance is embedded in a regulatory network designed to avoid both metal toxicity and harmful over-export of essential metal ions. (grosse2023interplaybetweentwocomponent pages 3-4)

A 2024 proteomic study provides contemporary expression-level support. Following a mixed-metal shock, CzcA and CzcB increased about 10-fold, CzcC about 23-fold, and CzcR about 8.5-fold; CzcS, CzcP, and CzcE were also detected in stressed cells. Because the challenge was a metal mixture, these are strong edges for “metal stress induces Czc machinery,” but only indirect support for a cobalt-specific induction edge. (galea2024linkingthetranscriptome pages 3-4)

CzcD is a CDF-family inner-membrane secondary metal exporter, whereas CzcP is a P-type ATPase associated with transition-metal export. CzcD is mechanistically plausible as an accessory cobalt-homeostasis node, but mutant-fitness effects can be weak. In *Pseudomonas stutzeri*, `czcD` had a cobalt fitness effect around −0.2, while `czcICBA` genes were around −0.8 and were substantially more important under zinc stress. These data argue against assigning every Czc-family component an equally strong cobalt-specific edge. (vaccaro2016novelmetalcation pages 4-5)

## 3. Candidate nodes grouped by type

### Trait and phenotype nodes

- `traitmech:000015` — cobalt tolerant.
- Growth in elevated Co(II).
- Cobalt resistance/tolerance phenotype.
- Cobalt-dependent growth inhibition.
- Co(II) EC50, IC50, or MIC — assay-result nodes; retain concentration, medium, salt, and exposure metadata.
- Cross-resistance to Ni(II), Zn(II), Cd(II), Fe(II), or other stressors — contextual rather than defining nodes.

### Chemicals and environmental factors

- cobalt(2+) / Co(II) — **CHEBI:48828** is a candidate grounding; verify against the ontology release used by TraitMech before committing.
- cobalt dichloride / CoCl₂ — candidate chemical-exposure node; salt and hydration state should be preserved where reported.
- extracellular cobalt, periplasmic cobalt, cytoplasmic cobalt — compartment-qualified chemical pools.
- proton motive force — energy source for RND-family transenvelope export.
- elevated cobalt concentration — label-only environmental/experimental factor unless a suitable METPO or ENVO term is verified.
- medium composition, pH, exposure duration, biomass/inoculum, and aerobic or phototrophic condition — assay modifiers.

### Transport systems and proteins

- CzcCBA complex — label-only complex unless a taxon-specific stable complex identifier is available.
  - CzcA — inner-membrane RND transporter.
  - CzcB — membrane-fusion/adaptor protein.
  - CzcC — outer-membrane factor.
- CnrCBA complex — cobalt/nickel RND transenvelope efflux system.
  - CnrA, CnrB, CnrC — corresponding RND, adaptor, and outer-membrane components.
- DmeF — CDF-family inner-membrane exporter implicated in moving surplus cytoplasmic Co(II) into the periplasm.
- CzcD — CDF-family secondary exporter/accessory homeostasis protein.
- CzcP — PIB4-type ATPase; cobalt export is supported in the transportome literature, but cobalt-specific mutant values should be recovered from the primary 2009 paper before assigning a high-confidence quantitative edge.
- CzcE — periplasmic metal-binding/accessory protein.
- CzcI — negative modulator that may prevent excessive CzcCBA activity.
- NimCB — candidate accessory/heteromeric cobalt-resistance components; presently uncertain.
- RcnA/NCC-related exporters — candidates in other taxa, requiring cobalt-specific functional validation.

### Regulators and processes

- CzcR — DNA-binding response regulator.
- CzcS — sensory histidine kinase.
- CzcRS two-component system.
- CzcR2S2 and AgrRS — regulatory cross-talk systems.
- `czcN` and `czcP` expression.
- cobalt ion transmembrane transport — candidate GO grounding should be checked in the current GO release rather than inferred from a generic transporter annotation.
- metal-ion homeostasis, response to metal ion, transmembrane efflux, and regulation of transcription — use GO identifiers only after record-level verification.

### Compartments

- extracellular region.
- outer membrane.
- periplasmic space.
- cytoplasmic/inner membrane.
- cytoplasm.

Generic GO cellular-component terms are preferable to invented taxon-specific identifiers; exact GO CURIEs should be validated during YAML implementation.

### Organisms

- *Cupriavidus metallidurans* CH34 — principal mechanistic model; use NCBITaxon grounding after strain-level record verification.
- *Pseudomonas stutzeri* RCH2 — transposon-fitness evidence.
- *Rhodobacter sphaeroides* evolved strain G7 — recent ALE phenotype and accumulation evidence.
- *Brevundimonas vesicularis* USM1 and *Pseudomonas putida* USM4 — recent phenotypic/genomic observations, but limited functional validation.

## 4. Candidate causal edges

The compact table below lists the strongest edges and evidence classes.

| subject | predicate | object | organism/context | evidence strength | DOI |
|---|---|---|---|---|---|
| elevated external Co(II) | inhibits growth of | wild-type cells | *Rhodobacter sphaeroides*; wild-type EC50 ≈ 0.8 mM Co2+; reference strain inhibited at 4 mM CoCl2 (atay2024evolutionaryengineeringand pages 1-2) | direct phenotype | 10.3389/fmicb.2024.1412294 |
| surplus cytoplasmic Co(II) | is moved to periplasm by | DmeF | *Cupriavidus metallidurans* transportome model (nies2016thebiologicalchemistry pages 25-25) | review-synthesized | 10.1039/c5mt00320b |
| CzcCBA | exports | periplasmic Co(II) to outside | *C. metallidurans*; transenvelope RND efflux in vivo (nies2016thebiologicalchemistry pages 25-25, nies2016thebiologicalchemistry pages 19-19) | review-synthesized | 10.1039/c5mt00320b |
| CnrCBA | exports | Co(II) to outside | *C. metallidurans*; RND efflux, especially under high cobalt conditions (nies2016thebiologicalchemistry pages 19-19) | review-synthesized | 10.1039/c5mt00320b |
| CnrCBA-mediated efflux | increases | cobalt resistance by ~300-fold | *C. metallidurans* (nies2016thebiologicalchemistry pages 19-19) | review-synthesized | 10.1039/c5mt00320b |
| proton motive force | powers | RND-driven metal efflux | *C. metallidurans* RND systems including Czc/Cnr (nies2016thebiologicalchemistry pages 15-16) | review-synthesized | 10.1039/c5mt00320b |
| CzcA | is RND transporter component of | CzcCBA tripartite complex | *C. metallidurans*; inner-membrane transporter role (galea2024linkingthetranscriptome pages 3-4, nies2016thebiologicalchemistry pages 15-16) | direct/review-combined | 10.1093/mtomcs/mfae058; 10.1039/c5mt00320b |
| CzcB | is membrane-fusion component of | CzcCBA tripartite complex | *C. metallidurans*; adapter/periplasmic connector role (galea2024linkingthetranscriptome pages 3-4, nies2016thebiologicalchemistry pages 15-16) | direct/review-combined | 10.1093/mtomcs/mfae058; 10.1039/c5mt00320b |
| CzcC | is outer-membrane factor component of | CzcCBA tripartite complex | *C. metallidurans*; outer-membrane exit channel role (galea2024linkingthetranscriptome pages 3-4, nies2016thebiologicalchemistry pages 15-16) | direct/review-combined | 10.1093/mtomcs/mfae058; 10.1039/c5mt00320b |
| metal shock | increases abundance of | CzcA/CzcB/CzcC proteins | *C. metallidurans* CH34 proteome; CzcA and CzcB ~10-fold, CzcC ~23-fold (galea2024linkingthetranscriptome pages 3-4) | direct proteomic | 10.1093/mtomcs/mfae058 |
| metal shock | increases abundance of | CzcR | *C. metallidurans* CH34 proteome; CzcR ~8.5-fold (galea2024linkingthetranscriptome pages 3-4) | direct proteomic | 10.1093/mtomcs/mfae058 |
| CzcR | upregulates expression of | czcN and czcP | *C. metallidurans* regulatory cross-talk study (grosse2023interplaybetweentwocomponent pages 3-4) | direct regulatory | 10.1128/jb.00343-22 |
| adaptive laboratory evolution | produces | cobalt-tolerant strain G7 | *R. sphaeroides*; 64 passages across 0.1–15 mM CoCl2 (atay2024evolutionaryengineeringand pages 1-2) | direct evolutionary phenotype | 10.3389/fmicb.2024.1412294 |
| strain G7 | accumulates more | cobalt than reference strain | *R. sphaeroides*; 12.82 mg/g CDW vs 0.57 mg/g CDW at 4 mM CoCl2 (atay2024evolutionaryengineeringand pages 9-10) | direct phenotype/application | 10.3389/fmicb.2024.1412294 |


*Table: This table lists the strongest curation-ready causal edges for microbial cobalt tolerance from the gathered evidence. It separates direct experimental support from review-synthesized and correlative evidence to help prioritize TraitMech curation.*

Additional edge-level curation notes follow.

| Subject | Predicate | Object | Supporting snippet or result | Reference | Curation note |
|---|---|---|---|---|---|
| Elevated external Co(II) | inhibits | microbial growth | “EC50 of Co2+ = 0.8 mM” for the reference *R. sphaeroides*; 4 mM inhibited the reference strain | DOI:10.3389/fmicb.2024.1412294 | **Direct, assay-specific.** Curate with salt, medium, and strain. (atay2024evolutionaryengineeringand pages 1-2) |
| DmeF | exports | surplus cytoplasmic Co(II) to periplasm | “Surplus cobalt is removed by DmeF at low concentrations to the periplasm” | DOI:10.1039/c5mt00320b | **Review-synthesized.** Useful mechanistic edge; ideally attach the underlying primary experiment. (nies2016thebiologicalchemistry pages 25-25) |
| CzcCBA | exports | periplasmic Co(II) outside cell | Co(II) is exported “from the periplasm to the outside” by CzcCBA | DOI:10.1039/c5mt00320b | **Strong model/review support.** Taxon-specific to the characterized system. (nies2016thebiologicalchemistry pages 25-25) |
| CnrCBA | exports | periplasmic Co(II) outside cell | CnrCBA exports Co(II) in vivo and contributes approximately 300-fold cobalt resistance | DOI:10.1039/c5mt00320b | **Strong but review-synthesized.** Do not generalize the fold change. (nies2016thebiologicalchemistry pages 19-19) |
| Proton motive force | powers | Czc/Cnr RND efflux | RND complexes operate by a “peristaltic pump mechanism driven by proton-motive force” | DOI:10.1039/c5mt00320b | **Mechanistically strong;** applies to RND transporter step, not CzcP ATPase. (nies2016thebiologicalchemistry pages 15-16) |
| CzcA | forms component of | CzcCBA | CzcA is the central RND transporter | DOI:10.1093/mtomcs/mfae058 | **Direct protein identification.** (galea2024linkingthetranscriptome pages 3-4) |
| CzcB | forms component of | CzcCBA | CzcB is the membrane-fusion protein | DOI:10.1093/mtomcs/mfae058 | **Direct protein identification.** (galea2024linkingthetranscriptome pages 3-4) |
| CzcC | forms component of | CzcCBA | CzcC is the outer-membrane factor | DOI:10.1093/mtomcs/mfae058 | **Direct protein identification.** (galea2024linkingthetranscriptome pages 3-4) |
| CzcA alone | increases | cobalt resistance above baseline | CzcA alone mediated “some cobalt resistance and efflux” | DOI:10.1128/aem.02048-21 | **Direct complementation evidence.** Do not represent CzcA as sufficient for full wild-type resistance. (grosse2022lossofmobile pages 18-19) |
| Complete CzcCBA assembly | increases | cobalt resistance to wild-type level | CzcBA gave low cobalt resistance; adding CzcC restored full resistance | DOI:10.1128/aem.02048-21 | **High-priority causal edge.** Supports complex completeness → phenotype. (grosse2022lossofmobile pages 18-19) |
| Metal shock | increases abundance of | CzcA and CzcB | approximately 10-fold increases | DOI:10.1093/mtomcs/mfae058 | **Direct proteomic, mixed-metal challenge.** Do not label cobalt-specific. (galea2024linkingthetranscriptome pages 3-4) |
| Metal shock | increases abundance of | CzcC | approximately 23-fold increase | DOI:10.1093/mtomcs/mfae058 | **Direct proteomic, mixed-metal challenge.** (galea2024linkingthetranscriptome pages 3-4) |
| Metal shock | increases abundance of | CzcR | approximately 8.5-fold increase | DOI:10.1093/mtomcs/mfae058 | **Direct proteomic, mixed-metal challenge.** (galea2024linkingthetranscriptome pages 3-4) |
| CzcR | positively regulates | `czcN` expression | `czcN` cannot be upregulated without CzcR | DOI:10.1128/jb.00343-22 | **Direct reporter/regulatory evidence.** Metal-specific context must be retained. (grosse2023interplaybetweentwocomponent pages 3-4) |
| CzcR | positively regulates | `czcP` expression | `czcP` cannot be upregulated without CzcR | DOI:10.1128/jb.00343-22 | **Direct reporter/regulatory evidence.** (grosse2023interplaybetweentwocomponent pages 3-4) |
| CzcI | inhibits/modulates | CzcCBA activity | CzcI was described as quenching CzcCBA to prevent overpumping of essential cations including Co(II) | DOI:10.1128/jb.00343-22 | **Homeostatic regulatory edge;** effect on cobalt-tolerance endpoint is indirect. (grosse2023interplaybetweentwocomponent pages 3-4) |
| `czcICBA` disruption | decreases | cobalt fitness | cobalt fitness values around −0.8 in *P. stutzeri* | DOI:10.1128/AEM.01845-16 | **Direct pooled-mutant fitness, modest and taxon/assay-specific.** System was more important for zinc. (vaccaro2016novelmetalcation pages 4-5) |
| `czcD` disruption | slightly decreases | cobalt fitness | cobalt fitness around −0.2 | DOI:10.1128/AEM.01845-16 | **Weak direct evidence.** Avoid a strong cobalt-resistance assertion. (vaccaro2016novelmetalcation pages 4-5) |
| ALE under increasing CoCl₂ | produces | cobalt-tolerant G7 population/strain | 64 passages at 0.1–15 mM CoCl₂ | DOI:10.3389/fmicb.2024.1412294 | **Direct evolutionary edge.** (atay2024evolutionaryengineeringand pages 1-2) |
| G7 genotype | associated with | cobalt tolerance | 23 SNPs in regulators, transport-related proteins, NifB-family and other genes | DOI:10.3389/fmicb.2024.1412294 | **Association only.** No individual SNP is yet a curation-ready causal node. (atay2024evolutionaryengineeringand pages 1-2, atay2024evolutionaryengineeringand pages 12-14) |
| G7 cobalt tolerance | co-occurs with | increased cobalt accumulation | 12.82 mg/g CDW versus 0.57 mg/g CDW at 4 mM CoCl₂ | DOI:10.3389/fmicb.2024.1412294 | **Direct phenotype, but direction of mechanism unresolved:** adsorption, uptake, sequestration, or combined processes. (atay2024evolutionaryengineeringand pages 9-10) |

## 5. Recent developments, applications, and statistics

### 2023–2024 mechanistic advances

1. **Regulatory network refinement (April 2023).** Große and colleagues showed that Czc regulation is not a simple linear CzcS→CzcR switch. CzcRS, CzcR2S2, and AgrRS cross-talk controls `czcN` and `czcP`, demonstrating system-level tuning of metal efflux and homeostasis. This supports adding regulatory nodes while discouraging an oversimplified “cobalt directly activates every czc gene” graph. (grosse2023interplaybetweentwocomponent pages 3-4)

2. **Proteome-level validation (November 2024).** In metal-shocked *C. metallidurans*, 3,540 proteins changed in presence or abundance across shock/starvation comparisons; plasmid-encoded resistance determinants, especially CzcCBA, were prominent. CzcA/B increased about 10-fold, CzcC 23-fold, and CzcR 8.5-fold. This connects transcriptional regulation to production of the physical efflux machinery. (galea2024linkingthetranscriptome pages 3-4)

3. **Adaptive evolution of a distinct cobalt-tolerance solution (June 2024).** *R. sphaeroides* G7 was generated without prior mutagenesis by 64 serial passages through 0.1–15 mM CoCl₂. Wild-type EC50 was 0.8 mM; G7 growth was unaffected at 4 mM, and G7 accumulated 12.82 mg cobalt/g dry biomass compared with 0.57 mg/g in the reference strain—approximately a 22.5-fold difference. Twenty-three SNPs were found, but reverse engineering and omics validation remain outstanding. (atay2024evolutionaryengineeringand pages 9-10, atay2024evolutionaryengineeringand pages 12-14, atay2024evolutionaryengineeringand pages 1-2)

4. **Environmental-isolate studies remain largely predictive.** A 2024 study reported concentration-dependent Co(II) inhibition and a lag phase reaching 26 hours at 25 ppm in *Brevundimonas vesicularis* USM1, while genome annotation identified CzcD and nickel–cobalt–cadmium resistance candidates. Because no knockout, complementation, or direct efflux measurement was performed, these genes should remain candidate rather than causal nodes. (hovorukha2024metalresistanceof pages 7-9)

### Current and prospective applications

- **Bioremediation and cobalt recovery.** Strains that remain viable while binding or accumulating cobalt could be used in treatment of mining or industrial waters. G7’s high cell-associated cobalt makes it a candidate biosorbent/bioaccumulator, but the study demonstrates laboratory potential rather than a field deployment. (atay2024evolutionaryengineeringand pages 9-10, atay2024evolutionaryengineeringand pages 12-14)
- **Engineering robust microbial cell factories.** ALE offers a non-transgenic route to stabilize cobalt tolerance in organisms exposed to metal-containing feedstocks. The G7 study demonstrates phenotype generation but does not yet identify a validated engineering target. (atay2024evolutionaryengineeringand pages 1-2)
- **Environmental surveillance.** `czc`/`cnr` abundance may indicate metal-selection pressure, but metagenomic detection must be paired with host assignment, expression, and cobalt phenotype. Expert reviews warn that metal/antibiotic co-selection is frequently inferred from correlation and requires functional confirmation.
- **Biosensor design.** Czc/Cnr regulatory systems are potential cobalt-responsive modules, although their cross-reactivity with Zn, Cd, and Ni limits cobalt specificity.

## 6. Recommended minimal graph extension

For `data/traits/environment/cobalt_tolerant.yaml`, a conservative core graph could contain:

1. elevated extracellular Co(II) → **inhibits** → microbial growth;
2. DmeF → **exports** → cytoplasmic Co(II) into periplasm;
3. proton motive force → **powers** → CzcCBA/CnrCBA RND transport;
4. CzcA + CzcB + CzcC → **assemble into** → CzcCBA;
5. CzcCBA → **exports** → periplasmic Co(II) outside cell;
6. CnrCBA → **exports** → periplasmic Co(II) outside cell;
7. cobalt efflux → **decreases** → intracellular/periplasmic cobalt burden;
8. decreased cobalt burden → **reduces** → cobalt-dependent growth inhibition;
9. CzcR → **positively regulates** → `czcN` and `czcP` expression;
10. complete CzcCBA complex → **increases** → cobalt tolerance.

Edges 1, 4, 5, 6, 9, and 10 have the best curation value. Edge 7 is mechanistically logical but should be linked to a direct accumulation/efflux experiment where possible. DmeF and CzcP should be retained as taxon-specific accessory branches rather than universally required components.

## 7. Warnings: claims not ready for TraitMech curation

- **Do not curate individual G7 SNPs as causes of cobalt tolerance.** The 23 variants are associated with an evolved phenotype but have not been reconstructed individually or in combination. (atay2024evolutionaryengineeringand pages 1-2, atay2024evolutionaryengineeringand pages 12-14)
- **Do not treat higher cobalt accumulation as proof of efflux.** G7 accumulated more cobalt despite greater tolerance; extracellular adsorption, sequestration, altered envelope binding, and intracellular accumulation remain unresolved. (atay2024evolutionaryengineeringand pages 9-10, atay2024evolutionaryengineeringand pages 1-2)
- **Do not infer cobalt tolerance from gene annotation alone.** CzcD/NCCN calls in recent isolate genomes lack functional validation. (hovorukha2024metalresistanceof pages 7-9)
- **Do not use mixed-metal induction as cobalt-specific regulation.** The 2024 proteome experiment strongly supports metal-stress induction of Czc machinery but cannot identify cobalt as the sole inducing ion. (galea2024linkingthetranscriptome pages 3-4)
- **Do not assume every `czc` determinant has equal Co/Zn/Cd specificity.** *P. stutzeri* mutant fitness showed a substantially stronger zinc than cobalt contribution. (vaccaro2016novelmetalcation pages 4-5)
- **Treat CorB/CorC cautiously.** Mutants showed increased rather than decreased cobalt resistance in the fitness study, suggesting an indirect or complex relationship rather than a simple “CorBC causes tolerance” edge. (vaccaro2016novelmetalcation pages 4-5)
- **Do not universalize the 300-fold Cnr/Czc resistance estimate or a 20 mM MIC.** Such values are strain-, medium-, and assay-specific. The supplied 20 mM *C. metallidurans* BS1 value was not independently recovered in the gathered full-text evidence and should remain attached to DOI:10.3389/fmicb.2020.00047 rather than generalized.
- **Do not assign unverified ontology CURIEs.** Label-only nodes are preferable for Czc/Cnr complexes and specialized transport processes until the relevant GO, UniProt, Rhea, KEGG, or MetaCyc records are checked directly.

## 8. DOI-first bibliography

1. Atay G, Holyavkin C, Can H, et al. **Evolutionary engineering and molecular characterization of cobalt-resistant *Rhodobacter sphaeroides*.** *Frontiers in Microbiology*. Published June 2024. DOI: [10.3389/fmicb.2024.1412294](https://doi.org/10.3389/fmicb.2024.1412294). (atay2024evolutionaryengineeringand pages 1-2, atay2024evolutionaryengineeringand pages 9-10)
2. Galea D, Herzberg M, Dobritzsch D, Fuszard M, Nies DH. **Linking the transcriptome to physiology: response of the proteome of *Cupriavidus metallidurans* to changing metal availability.** *Metallomics*. Published November 2024. DOI: [10.1093/mtomcs/mfae058](https://doi.org/10.1093/mtomcs/mfae058). (galea2024linkingthetranscriptome pages 3-4)
3. Große C, Scherer J, Schleuder G, Nies DH. **Interplay between two-component regulatory systems is involved in control of *Cupriavidus metallidurans* metal resistance genes.** *Journal of Bacteriology*. Published April 2023. DOI: [10.1128/jb.00343-22](https://doi.org/10.1128/jb.00343-22). (grosse2023interplaybetweentwocomponent pages 3-4)
4. Große C, Kohl TA, Niemann S, Herzberg M, Nies DH. **Loss of mobile genomic islands in metal-resistant, hydrogen-oxidizing *Cupriavidus metallidurans*.** *Applied and Environmental Microbiology*. Published February 2022. DOI: [10.1128/aem.02048-21](https://doi.org/10.1128/aem.02048-21). (grosse2022lossofmobile pages 18-19)
5. Nies DH. **The biological chemistry of the transition metal “transportome” of *Cupriavidus metallidurans*.** *Metallomics*. Published May 2016. DOI: [10.1039/c5mt00320b](https://doi.org/10.1039/c5mt00320b). (nies2016thebiologicalchemistry pages 25-25, nies2016thebiologicalchemistry pages 15-16, nies2016thebiologicalchemistry pages 19-19)
6. Vaccaro BJ, Lancaster WA, Thorgersen MP, et al. **Novel metal cation resistance systems from mutant fitness analysis of denitrifying *Pseudomonas stutzeri*.** *Applied and Environmental Microbiology*. Published October 2016. DOI: [10.1128/AEM.01845-16](https://doi.org/10.1128/AEM.01845-16). (vaccaro2016novelmetalcation pages 4-5)
7. Scherer J, Nies DH. **CzcP is a novel efflux system contributing to transition metal resistance in *Cupriavidus metallidurans* CH34.** *Molecular Microbiology*. Published August 2009. DOI: [10.1111/j.1365-2958.2009.06792.x](https://doi.org/10.1111/j.1365-2958.2009.06792.x). This is the primary source supplied for CzcP-mediated Zn(II), Cd(II), and Co(II) export; its full text was not recovered here, so quantitative primary edges should be checked before YAML entry.
8. Hovorukha V, Moliszewska E, Havryliuk O, Bida I, Tashyrev O. **Metal resistance of microorganisms as a crucial factor for their homeostasis and sustainable environment.** *Sustainability*. Published November 2024. DOI: [10.3390/su16229655](https://doi.org/10.3390/su16229655). (hovorukha2024metalresistanceof pages 7-9)

References

1. (atay2024evolutionaryengineeringand pages 1-2): Güneş Atay, Can Holyavkin, Hanay Can, Mevlüt Arslan, Alican Topaloğlu, Massimo Trotta, and Zeynep Petek Çakar. Evolutionary engineering and molecular characterization of cobalt-resistant rhodobacter sphaeroides. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1412294, doi:10.3389/fmicb.2024.1412294. This article has 3 citations and is from a peer-reviewed journal.

2. (nies2016thebiologicalchemistry pages 25-25): Dietrich H. Nies. The biological chemistry of the transition metal "transportome" of cupriavidus metallidurans. Metallomics : integrated biometal science, 8 5:481-507, May 2016. URL: https://doi.org/10.1039/c5mt00320b, doi:10.1039/c5mt00320b. This article has 73 citations.

3. (nies2016thebiologicalchemistry pages 15-16): Dietrich H. Nies. The biological chemistry of the transition metal "transportome" of cupriavidus metallidurans. Metallomics : integrated biometal science, 8 5:481-507, May 2016. URL: https://doi.org/10.1039/c5mt00320b, doi:10.1039/c5mt00320b. This article has 73 citations.

4. (nies2016thebiologicalchemistry pages 19-19): Dietrich H. Nies. The biological chemistry of the transition metal "transportome" of cupriavidus metallidurans. Metallomics : integrated biometal science, 8 5:481-507, May 2016. URL: https://doi.org/10.1039/c5mt00320b, doi:10.1039/c5mt00320b. This article has 73 citations.

5. (galea2024linkingthetranscriptome pages 3-4): Diana Galea, Martin Herzberg, Dirk Dobritzsch, Matt Fuszard, and Dietrich H Nies. Linking the transcriptome to physiology: response of the proteome of cupriavidus metallidurans to changing metal availability. Metallomics: Integrated Biometal Science, Nov 2024. URL: https://doi.org/10.1093/mtomcs/mfae058, doi:10.1093/mtomcs/mfae058. This article has 9 citations.

6. (grosse2022lossofmobile pages 18-19): Cornelia Große, Thomas A. Kohl, Stefan Niemann, Martin Herzberg, and Dietrich H. Nies. Loss of mobile genomic islands in metal-resistant, hydrogen-oxidizing cupriavidus metallidurans. Feb 2022. URL: https://doi.org/10.1128/aem.02048-21, doi:10.1128/aem.02048-21. This article has 18 citations and is from a peer-reviewed journal.

7. (grosse2023interplaybetweentwocomponent pages 3-4): Cornelia Große, Judith Scherer, Grit Schleuder, and Dietrich H. Nies. Interplay between two-component regulatory systems is involved in control of cupriavidus metallidurans metal resistance genes. Journal of Bacteriology, Apr 2023. URL: https://doi.org/10.1128/jb.00343-22, doi:10.1128/jb.00343-22. This article has 15 citations and is from a peer-reviewed journal.

8. (vaccaro2016novelmetalcation pages 4-5): Brian J. Vaccaro, W. Andrew Lancaster, Michael P. Thorgersen, Grant M. Zane, Adam D. Younkin, Alexey E. Kazakov, Kelly M. Wetmore, Adam Deutschbauer, Adam P. Arkin, Pavel S. Novichkov, Judy D. Wall, and Michael W. W. Adams. Novel metal cation resistance systems from mutant fitness analysis of denitrifying pseudomonas stutzeri. Applied and Environmental Microbiology, 82:6046-6056, Oct 2016. URL: https://doi.org/10.1128/aem.01845-16, doi:10.1128/aem.01845-16. This article has 31 citations and is from a peer-reviewed journal.

9. (atay2024evolutionaryengineeringand pages 9-10): Güneş Atay, Can Holyavkin, Hanay Can, Mevlüt Arslan, Alican Topaloğlu, Massimo Trotta, and Zeynep Petek Çakar. Evolutionary engineering and molecular characterization of cobalt-resistant rhodobacter sphaeroides. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1412294, doi:10.3389/fmicb.2024.1412294. This article has 3 citations and is from a peer-reviewed journal.

10. (atay2024evolutionaryengineeringand pages 12-14): Güneş Atay, Can Holyavkin, Hanay Can, Mevlüt Arslan, Alican Topaloğlu, Massimo Trotta, and Zeynep Petek Çakar. Evolutionary engineering and molecular characterization of cobalt-resistant rhodobacter sphaeroides. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1412294, doi:10.3389/fmicb.2024.1412294. This article has 3 citations and is from a peer-reviewed journal.

11. (hovorukha2024metalresistanceof pages 7-9): Vira Hovorukha, Ewa Moliszewska, Olesia Havryliuk, Iryna Bida, and Oleksandr Tashyrev. Metal resistance of microorganisms as a crucial factor for their homeostasis and sustainable environment. Sustainability, 16:9655, Nov 2024. URL: https://doi.org/10.3390/su16229655, doi:10.3390/su16229655. This article has 9 citations.