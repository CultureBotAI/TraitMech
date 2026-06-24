---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:22:44.539638'
end_time: '2026-06-17T21:46:24.131235'
duration_seconds: 1419.59
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cadmium tolerant
  trait_identifier: traitmech:000013
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: cadmium_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metal tolerance in which an organism grows in the presence of elevated
    cadmium (Cd2+) concentrations, typically via cation-efflux resistance systems
    such as the czc determinant.
  parent_traits: traitmech:000012
  synonyms: ''
  evidence_summary: 'DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition
    metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system
    of Cupriavidus metallidurans confers cadmium resistance.) | DOI:10.3389/fmicb.2020.00047:
    C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+
    (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and
    Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cadmium
    to a MIC of 2.5 mM.)'
  causal_graph_summary: 'cadmium_tolerance_czc_efflux: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cadmium tolerant
- **METPO identifier:** traitmech:000013
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated cadmium (Cd2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers cadmium resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cadmium to a MIC of 2.5 mM.)
- **Existing causal graph summary:** cadmium_tolerance_czc_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cadmium tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/cadmium_tolerant.yaml`.

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
- **Trait label:** cadmium tolerant
- **METPO identifier:** traitmech:000013
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated cadmium (Cd2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers cadmium resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cadmium to a MIC of 2.5 mM.)
- **Existing causal graph summary:** cadmium_tolerance_czc_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cadmium tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/cadmium_tolerant.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **cadmium tolerant** (METPO: traitmech:000013)

### 0) Scope summary (curation-ready)
**Trait meaning (operational phenotype):** “Cadmium tolerant” denotes an experimentally observed **capacity for microbial growth and survival in the presence of elevated Cd(II)**, typically quantified as a **minimum inhibitory concentration (MIC)** or **maximum tolerable concentration (MTC)** under specified assay conditions. In *Pseudomonas aeruginosa* strain CD3, cadmium tolerance was explicitly measured by MIC in a modified chemically defined medium and by growth curves/CFU kinetics; importantly, biofilm-associated tolerance allowed survival at lower concentrations than planktonic efflux-dependent growth at higher concentrations. (chatterjee2024multimodalcadmiumresistance pages 1-2, chatterjee2024multimodalcadmiumresistance pages 3-4, chatterjee2024multimodalcadmiumresistance pages 6-7)

**What this trait is not (boundary cases):**
1. **Apparent tolerance due to high inoculum density** (collective “dilution” of cadmium per cell) can inflate MIC estimates; CD3 showed strong inoculum dependence and the authors emphasize controlling inoculum size. (chatterjee2024multimodalcadmiumresistance pages 3-4, chatterjee2024multimodalcadmiumresistance pages 6-7)
2. **Passive biosorption/adsorption** (e.g., cadmium bound to dead or heat-killed biomass) should not be curated as “tolerance” unless paired with evidence of growth/viability; CD3 experiments explicitly used heat-killed controls and EDTA wash steps to distinguish surface-bound Cd from intracellular Cd and active efflux. (chatterjee2024multimodalcadmiumresistance pages 3-4, chatterjee2024multimodalcadmiumresistance pages 6-7)
3. **General multi-metal tolerance** should not automatically be mapped to cadmium tolerance without cadmium-specific evidence; CD3 is multi-metal tolerant, but cadmium tolerance was shown to depend on efflux at >1 mM Cd. (chatterjee2024multimodalcadmiumresistance pages 1-2)

**Assay/metric landscape (definitions used in 2023–2024 sources):**
- **MIC (minimum inhibitory concentration):** operationally the lowest Cd concentration that inhibits growth in the assay (turbidity/OD, CFU, or visible growth depending on protocol). (chatterjee2024pseudomonasaeruginosastrain pages 4-7, chatterjee2024multimodalcadmiumresistance pages 6-7)
- **MTC (maximum tolerable concentration):** defined as “the highest concentration of a metal or toxic substance at which microorganisms can still grow and exhibit normal metabolic activity” using stepwise plating; if no growth occurs at a concentration, MTC is taken as the previous concentration. (hovorukha2024metalresistanceof pages 2-3)

### 1) Key concepts & current mechanistic understanding (2023–2024 emphasized)
Cadmium tolerance is largely implemented through **metal homeostasis and detoxification networks** that limit cytosolic Cd(II) activity by:

1) **Efflux/export (dominant for high-level tolerance):**
- **RND-type CBA trans-envelope efflux** (e.g., **CzcCBA**) is presented as a principal system enabling expulsion of Cd(II), under control of a two-component system (CzcRS) in Gram-negative contexts. (chatterjee2024multimodalcadmiumresistance pages 14-15, sharma2024mechanismsofmicrobial pages 12-13)
- **P-type ATPases** (e.g., **CadA/CadD**) export Cd(II) from cytoplasm toward periplasm/extracellular space and can provide strong resistance phenotypes. (sharma2024mechanismsofmicrobial pages 12-13, zhu2024thecaddxoperon pages 1-2)

2) **Sequestration and binding (adjunct, often lower-level or supportive):**
- **Metallothioneins / thiol-rich proteins** bind Cd(II) and can contribute to tolerance, particularly as a buffering mechanism. (chatterjee2024multimodalcadmiumresistance pages 15-16, sharma2024mechanismsofmicrobial pages 12-13)

3) **Community-state protection:**
- **Biofilm formation/EPS** can protect cells at lower Cd by reducing effective exposure or increasing retention outside the cytoplasm; in CD3, biofilm enabled resistance up to 0.75 mM CdCl2·H2O. (chatterjee2024multimodalcadmiumresistance pages 1-2, chatterjee2024multimodalcadmiumresistance media 9453c781)

4) **Inducibility and cross-metal regulation:**
- Cadmium tolerance can be **inducible**, and **Zn(II)/Co(II)** exposure can cross-induce cadmium resistance programs (e.g., shortened lag, increased tolerance during challenge). (chatterjee2024multimodalcadmiumresistance pages 6-7, chatterjee2024multimodalcadmiumresistance pages 14-15)

### 2) Recent developments & latest research highlights (2023–2024)

#### 2.1 Multimodal cadmium resistance in *Pseudomonas aeruginosa* CD3 (2024)
A 2024 peer-reviewed study provides one of the clearest modern, multi-assay characterizations of cadmium tolerance as a phenotype plus a mechanistic network:
- **Phenotype:** CD3 demonstrated “cadmium resistance (up to 3 mM CdCl2·H2O)” (MIC context) and **biofilm-enabled tolerance up to 0.75 mM**. (chatterjee2024multimodalcadmiumresistance pages 1-2)
- **Mechanism:** survival/growth above 1 mM depended on efflux; **AAS partitioning** supported strong export with high extracellular Cd and lower intracellular Cd. (chatterjee2024multimodalcadmiumresistance pages 1-2, chatterjee2024multimodalcadmiumresistance pages 15-16)
- **Regulation:** the authors link Cd response to a regulatory network involving **BfmR/BfmS** with **CzcR/CzcS** and **CadR**, consistent with a switch between biofilm-based protection and efflux-based detoxification at higher Cd. (chatterjee2024multimodalcadmiumresistance pages 17-19, chatterjee2024multimodalcadmiumresistance pages 12-14)

#### 2.2 Mobile cadmium resistance operon cadDX in zoonotic streptococci (2024)
A 2024 Veterinary Research paper reports a mechanistically defined and mobile cadmium-resistance module:
- **cadDX contributes to cadmium resistance**, oxidative stress resistance, and virulence; the operon encodes **CadD (P-type ATPase efflux)** and **CadX (repressor)**. (zhu2024thecaddxoperon pages 1-2, zhu2024thecaddxoperon pages 3-5)
- **CadX represses cadD** by promoter binding, and **horizontal transfer** into *Streptococcus agalactiae* transfers similar phenotypes (cadmium/oxidative-stress resistance and increased virulence). (zhu2024thecaddxoperon pages 1-2)

#### 2.3 Quantitative trait metrics formalization (MTC) (2024)
A 2024 Sustainability study provides explicit MTC operationalization and example Cd tolerance values (Cd up to 200 ppm for two soil strains), useful for trait definition and assay design in curation contexts. (hovorukha2024metalresistanceof pages 2-3)

### 3) Current applications & real-world implementations

#### 3.1 Engineered microbe + crop-root colonization to reduce cadmium uptake (2024)
A 2024 study engineered *Deinococcus radiodurans* to display two metal-binding domains (PbBD and MTT5) on the cell surface (fusion with Lpp-OmpA), generating strain **LOPM** with enhanced adsorption and remediation performance:
- **Cd adsorption increased 4.9-fold** vs wild-type. (wang2024surfacedisplayof pages 1-2)
- In solution, after 48 h, **LOPM removed 84.9% Cd** (vs 72.3% for wild-type) under their assay conditions. (wang2024surfacedisplayof pages 2-5)
- When LOPM colonized rice roots, **plant Cd content decreased to 47.0% (root) and 43.4% (shoot)** relative to metal exposure without treatment, indicating a practical phytoremediation-adjacent approach. (wang2024surfacedisplayof pages 1-2)

**Curation note:** these edges represent *application/engineering* rather than naturally evolved tolerance; they may be curated as a separate “implementation” subgraph or excluded from a minimal natural-trait causal graph depending on TraitMech scope. (wang2024surfacedisplayof pages 1-2, wang2024surfacedisplayof pages 2-5)

### 4) Candidate causal graph entities (nodes), grouped by type

#### 4.1 Phenotype/trait nodes
- cadmium tolerant (METPO:traitmech:000013)
- cadmium resistance (label-level; often used interchangeably with “tolerance” in microbiology operationally) (chatterjee2024multimodalcadmiumresistance pages 1-2, zhu2024thecaddxoperon pages 3-5)
- inducible cadmium resistance (label-level) (chatterjee2024multimodalcadmiumresistance pages 1-2, chatterjee2024multimodalcadmiumresistance pages 6-7)

#### 4.2 Chemical/environment nodes
- cadmium(2+) (CHEBI:22977)
- zinc(2+) (CHEBI:29105) — cross-inducer / regulator input (chatterjee2024multimodalcadmiumresistance pages 14-15, sharma2024mechanismsofmicrobial pages 12-13)
- cobalt(2+) (CHEBI:27638) — cross-inducer (chatterjee2024multimodalcadmiumresistance pages 6-7)
- hydrogen peroxide (CHEBI:16240) — oxidative stress input affecting cadDX regulation (zhu2024thecaddxoperon pages 1-2)
- pH (label-level) — modulates growth kinetics under Cd stress (chatterjee2024multimodalcadmiumresistance pages 15-16, chatterjee2024multimodalcadmiumresistance pages 6-7)

#### 4.3 Genes/proteins/complexes (mechanistic)
**Efflux/export**
- CzcCBA efflux system (label-level; RND-type CBA) (chatterjee2024multimodalcadmiumresistance pages 14-15, sharma2024mechanismsofmicrobial pages 12-13)
- CzcR/CzcS two-component system (label-level) (chatterjee2024multimodalcadmiumresistance pages 14-15, sharma2024mechanismsofmicrobial pages 12-13)
- CadA (P-type ATPase; label-level) (sharma2024mechanismsofmicrobial pages 12-13, chatterjee2024multimodalcadmiumresistance pages 16-17)
- CadR (label-level regulator) (chatterjee2024multimodalcadmiumresistance pages 17-19, chatterjee2024multimodalcadmiumresistance pages 12-14)
- cadDX operon (label-level)
- CadD (P-type ATPase efflux) (zhu2024thecaddxoperon pages 1-2)
- CadX (ArsR-family repressor) (zhu2024thecaddxoperon pages 1-2)

**Sequestration/binding**
- metallothionein / thiol-rich proteins (label-level) (chatterjee2024multimodalcadmiumresistance pages 15-16, sharma2024mechanismsofmicrobial pages 12-13)

**Community/physiology**
- biofilm formation (GO:0042710) (chatterjee2024multimodalcadmiumresistance pages 1-2, chatterjee2024multimodalcadmiumresistance media 9453c781)
- extracellular polymeric substances (EPS; label-level) (sharma2024mechanismsofmicrobial pages 12-13)

#### 4.4 Experimental/assay nodes
- MIC determination (broth/defined medium; OD/turbidity; CFU) (chatterjee2024multimodalcadmiumresistance pages 3-4, chatterjee2024pseudomonasaeruginosastrain pages 4-7)
- MTC determination (stepwise plating) (hovorukha2024metalresistanceof pages 2-3)
- atomic absorption spectroscopy (AAS/FAAS) Cd partitioning (extracellular vs surface vs intracellular) (chatterjee2024multimodalcadmiumresistance pages 3-4, chatterjee2024multimodalcadmiumresistance pages 6-7)
- inoculum density (label-level experimental factor) (chatterjee2024multimodalcadmiumresistance pages 3-4, chatterjee2024multimodalcadmiumresistance pages 6-7)

### 5) Evidence-backed candidate causal edges (triples)
The following table is intended to be directly curatable into a TraitMech causal graph (with uncertainty flagged where evidence is review- or model-derived rather than direct perturbation/biochemical proof).

| Node 1 (label + CURIE) | Predicate | Node 2 (label + CURIE) | Evidence snippet | Reference | Notes |
|---|---|---|---|---|---|
| CzcR/CzcS two-component system (GO:0000160 for phosphorelay signal transduction, label-level for CzcR/CzcS) | activates transcription of | CzcCBA efflux system (label-level; RND trans-envelope efflux complex) | “Zn2+ binding to the CzcS periplasmic adapter activates CzcR and transcription of the czcCBA operon” (chatterjee2024multimodalcadmiumresistance pages 14-15, chatterjee2024pseudomonasaeruginosastrain pages 21-23) | Chatterjee et al. 2024, doi:10.1038/s41598-024-80754-y, https://doi.org/10.1038/s41598-024-80754-y | Taxon-specific to *Pseudomonas aeruginosa* CD3; assay context includes comparative genomics and physiological induction experiments. |
| CzcCBA efflux system (label-level; RND trans-envelope efflux complex) | expels | cadmium(2+) (CHEBI:22977) | “stimulates the transcription of the czcCBA operon, facilitating the expulsion of Cd2+ ions from the cytoplasm and periplasm” (chatterjee2024multimodalcadmiumresistance pages 14-15, chatterjee2024multimodalcadmiumresistance pages 15-16) | Chatterjee et al. 2024, doi:10.1038/s41598-024-80754-y, https://doi.org/10.1038/s41598-024-80754-y | Supported by AAS partitioning showing high extracellular Cd and lower intracellular Cd in live cells; strong candidate edge. |
| CzcCBA efflux system (label-level) | confers resistance to | cadmium tolerance (METPO:traitmech:000013) | “the CzcCBA complex from *Pseudomonas aeruginosa* ‘confers resistance to Cd2+’” (sharma2024mechanismsofmicrobial pages 12-13) | Sharma et al. 2024, doi:10.1007/s40201-023-00887-6, https://doi.org/10.1007/s40201-023-00887-6 | Review-derived summary of prior primary literature; UNCERTAIN for direct curation unless backstopped by primary mechanistic paper. |
| zinc(2+) (CHEBI:29105) | induces | CzcRS/CzcCBA-mediated cadmium resistance program (label-level) | “expression is induced by zinc and copper”; “cells induced by 0.25 mM zinc have a greater impact on cadmium resistance” (sharma2024mechanismsofmicrobial pages 12-13, chatterjee2024multimodalcadmiumresistance pages 14-15) | Sharma et al. 2024, doi:10.1007/s40201-023-00887-6, https://doi.org/10.1007/s40201-023-00887-6; Chatterjee et al. 2024, doi:10.1038/s41598-024-80754-y, https://doi.org/10.1038/s41598-024-80754-y | Mixed evidence from review plus CD3 induction assay; useful as environmental induction edge. |
| cobalt(2+) (CHEBI:27638) | cross-induces | cadmium tolerance (METPO:traitmech:000013) | “Zn2+ and Co2+ cross-induce resistance (Zn stronger)” (chatterjee2024multimodalcadmiumresistance pages 6-7) | Chatterjee et al. 2024, doi:10.1038/s41598-024-80754-y, https://doi.org/10.1038/s41598-024-80754-y | Assay-specific to pre-exposure/lag-phase shortening in *P. aeruginosa* CD3; mechanism likely regulatory, not yet fully resolved. |
| CadA P-type ATPase (label-level; cadmium-translocating ATPase) | transports | cadmium(2+) from cytoplasm to periplasm (CHEBI:22977) | “P-type (P1B) ATPases (CadCA/CadA)… use ATP to pump Cd(II) from cytoplasm to periplasm” (sharma2024mechanismsofmicrobial pages 12-13) | Sharma et al. 2024, doi:10.1007/s40201-023-00887-6, https://doi.org/10.1007/s40201-023-00887-6 | Review-derived but mechanistically specific; UNCERTAIN unless paired with organism-specific primary evidence. |
| CadA/CadR system (label-level) | contributes to | cadmium tolerance (METPO:traitmech:000013) | “CadA–CadR system is reported to expel cadmium to the periplasmic space, offering an additional defense” (chatterjee2024multimodalcadmiumresistance pages 16-17) | Chatterjee et al. 2024, doi:10.1038/s41598-024-80754-y, https://doi.org/10.1038/s41598-024-80754-y | Supported in CD3 by genome/network analysis and physiological context; exact direct biochemical assay of CadA in CD3 not shown, so moderately certain. |
| CadR (label-level; MerR-family/CadR regulator) | activates | CadA-mediated efflux response (label-level) | “under high Cd, CadR binds four Cd ions to activate CadA” (chatterjee2024multimodalcadmiumresistance pages 17-19) | Chatterjee et al. 2024, doi:10.1038/s41598-024-80754-y, https://doi.org/10.1038/s41598-024-80754-y | Proposed model from regulatory-network interpretation in CD3; UNCERTAIN/model-derived. |
| cadDX operon (label-level) | increases | cadmium tolerance (METPO:traitmech:000013) | “cadDX protects *S. suis* against cadmium stress”; “contributes to cadmium resistance” (zhu2024thecaddxoperon pages 3-5, zhu2024thecaddxoperon pages 1-2) | Zhu et al. 2024, doi:10.1186/s13567-024-01371-1, https://doi.org/10.1186/s13567-024-01371-1 | Strong primary evidence in Gram-positive zoonotic streptococci; taxon-specific but causal. |
| CadX (label-level; ArsR-family transcriptional repressor) | represses | cadD / CadD expression (label-level) | “CadX directly represses cadD by binding the cadDX promoter” (zhu2024thecaddxoperon pages 1-2) | Zhu et al. 2024, doi:10.1186/s13567-024-01371-1, https://doi.org/10.1186/s13567-024-01371-1 | Strong regulatory edge in *Streptococcus suis*; useful separate module from Czc-based Gram-negative tolerance. |
| CadD P-type ATPase (label-level) | effluxes | cadmium(2+) (CHEBI:22977) | “cadDX encodes CadD (a P-type ATPase efflux pump)” (zhu2024thecaddxoperon pages 1-2) | Zhu et al. 2024, doi:10.1186/s13567-024-01371-1, https://doi.org/10.1186/s13567-024-01371-1 | Primary source; taxon-specific to streptococci and related MGEs. |
| hydrogen peroxide stress (CHEBI:16240) | activates via internal promoter | cadX response module (label-level) | “cadX also contains an additional promoter that responds to H2O2 stress” (zhu2024thecaddxoperon pages 1-2) | Zhu et al. 2024, doi:10.1186/s13567-024-01371-1, https://doi.org/10.1186/s13567-024-01371-1 | Relevant because oxidative-stress integration modulates cadmium-resistance operon behavior. |
| cadDX operon (label-level) | increases | oxidative stress resistance (GO:0006979) | “cadDX contributes to cadmium resistance, oxidative stress resistance, and virulence” (zhu2024thecaddxoperon pages 1-2, zhu2024thecaddxoperon pages 3-5) | Zhu et al. 2024, doi:10.1186/s13567-024-01371-1, https://doi.org/10.1186/s13567-024-01371-1 | Not a direct cadmium-tolerance edge, but relevant adjacent mechanism; curate only if cross-trait links are allowed. |
| horizontal transfer of cadDX (label-level) | confers | cadmium tolerance (METPO:traitmech:000013) | “horizontal transfer into *Streptococcus agalactiae* confers analogous cadmium/oxidative-stress resistance” (zhu2024thecaddxoperon pages 1-2) | Zhu et al. 2024, doi:10.1186/s13567-024-01371-1, https://doi.org/10.1186/s13567-024-01371-1 | Strong MGE-linked acquisition edge; taxon-specific but valuable for graph extensions involving HGT. |
| biofilm formation (GO:0042710) | increases tolerance to | cadmium(2+) exposure (CHEBI:22977) | “biofilm enabled resistance up to 0.75 mM CdCl2·H2O” (chatterjee2024multimodalcadmiumresistance pages 1-2); “Biofilm production peaks at 0.75 mM” (chatterjee2024multimodalcadmiumresistance media 9453c781) | Chatterjee et al. 2024, doi:10.1038/s41598-024-80754-y, https://doi.org/10.1038/s41598-024-80754-y | Strong phenotype edge in CD3; may represent protective community state rather than intrinsic single-cell tolerance. |
| BfmR/BfmS regulatory system (label-level) | promotes | biofilm formation (GO:0042710) | “BfmR/BfmS/EFhP linked to biofilm development/maturation” (chatterjee2024multimodalcadmiumresistance pages 12-14); “BfmR playing a crucial role… essential for biofilm formation” (chatterjee2024pseudomonasaeruginosastrain pages 1-4) | Chatterjee et al. 2024, doi:10.1038/s41598-024-80754-y, https://doi.org/10.1038/s41598-024-80754-y | Network-inference supported more than direct mutation assay; UNCERTAIN/model-supported. |
| extracellular polymeric substances / EPS (label-level) | sequester or sorb | cadmium(2+) (CHEBI:22977) | “biopolymeric matrices/EPS-based strategies” and “bio-sorption/biofilms are highlighted” (sharma2024mechanismsofmicrobial pages 12-13) | Sharma et al. 2024, doi:10.1007/s40201-023-00887-6, https://doi.org/10.1007/s40201-023-00887-6 | Review-derived community-level mechanism; UNCERTAIN for direct curation without primary organism-specific support. |
| metallothionein / thiol-rich proteins (GO:0030001 metal ion binding as broad grounding; label-level for MT) | sequester | cadmium(2+) (CHEBI:22977) | “metallothioneins… bind Cd(II)” and CD3 genome shows “metallothionein, and thiol-rich proteins for sequestration” (sharma2024mechanismsofmicrobial pages 12-13, chatterjee2024multimodalcadmiumresistance pages 15-16) | Sharma et al. 2024, doi:10.1007/s40201-023-00887-6, https://doi.org/10.1007/s40201-023-00887-6; Chatterjee et al. 2024, doi:10.1038/s41598-024-80754-y, https://doi.org/10.1038/s41598-024-80754-y | Good mechanistic candidate, but in CD3 evidence is genomic inference rather than functional knockout; moderate certainty. |
| CzcR regulator (label-level) | controls | CzcCBA efflux pump expression (label-level) | “the CzcR regulator controls the CzcCBA efflux pump that provides resistance to Zn, Cd, and Co” (hovorukha2024metalresistanceof pages 2-3) | Hovorukha et al. 2024, doi:10.3390/su16229655, https://doi.org/10.3390/su16229655 | Review/secondary framing within an experimental paper; useful support for generalized metal-homeostasis node. UNCERTAIN as direct primary cadmium assay link in that paper. |
| CzcCBA efflux pump (label-level) | provides resistance to | zinc(2+)/cadmium(2+)/cobalt(2+) (CHEBI:29105/CHEBI:22977/CHEBI:27638) | “CzcCBA efflux pump that provides resistance to Zn, Cd, and Co” (hovorukha2024metalresistanceof pages 2-3) | Hovorukha et al. 2024, doi:10.3390/su16229655, https://doi.org/10.3390/su16229655 | General metal-resistance edge, useful for nearby-trait distinction; secondary statement in 2024 source. UNCERTAIN. |
| surface-displayed metal-binding domains PbBD+MTT5 on Lpp-OmpA (label-level engineered construct) | increase | cadmium adsorption (label-level) | “LOPM showed a 4.9-fold increase in Cd adsorption” and “accumulated 2.6–2.9× more Cd” (wang2024surfacedisplayof pages 1-2, wang2024surfacedisplayof pages 2-5) | Wang et al. 2024, doi:10.3390/ijms252312570, https://doi.org/10.3390/ijms252312570 | Application edge in engineered *Deinococcus radiodurans*; not natural trait mechanism but highly relevant implementation. |
| engineered *Deinococcus radiodurans* LOPM (NCBITaxon:1299 for species) | removes | cadmium from medium (CHEBI:22977) | “After 48 h LOPM removed 84.9% Cd” (wang2024surfacedisplayof pages 2-5) | Wang et al. 2024, doi:10.3390/ijms252312570, https://doi.org/10.3390/ijms252312570 | Applied bioremediation phenotype under 100 µM CdCl2 exposure. |
| engineered *Deinococcus radiodurans* LOPM colonizing rice roots (label-level) | reduces | rice cadmium accumulation (label-level) | “Cd content fell to 47.0% in root and 43.4% in shoot” (wang2024surfacedisplayof pages 1-2) | Wang et al. 2024, doi:10.3390/ijms252312570, https://doi.org/10.3390/ijms252312570 | Application/implementation edge in phytoremediation context; not direct natural microbial tolerance mechanism. |
| live-cell metal efflux activity (label-level) | increases | extracellular cadmium pool (CHEBI:22977) | “significant extracellular Cd2+ accumulation (85.33 ppm)” with lower intracellular Cd (13 ppm) (chatterjee2024multimodalcadmiumresistance pages 14-15, chatterjee2024multimodalcadmiumresistance pages 15-16) | Chatterjee et al. 2024, doi:10.1038/s41598-024-80754-y, https://doi.org/10.1038/s41598-024-80754-y | Strong assay-supported physiological edge from AAS partitioning in CD3. |


*Table: This table compiles candidate TraitMech subject-predicate-object edges for microbial cadmium tolerance, with direct evidence snippets, DOI-first references, and curation notes. It emphasizes mechanistic transport/regulatory modules, community-level protection, inducible responses, and recent applied engineering examples.*

### 6) Quantitative statistics & data points (recent studies)

**6.1 Cadmium tolerance levels (examples; assay-dependent)**
- *P. aeruginosa* CD3: **MIC/resistance up to 3 mM CdCl2·H2O** in a modified chemically defined medium; **biofilm enabled resistance up to 0.75 mM**; efflux required for growth above ~1 mM. (chatterjee2024multimodalcadmiumresistance pages 1-2)
- Screening yield: **26 cadmium-resistant isolates** were obtained; 10 grew on 15 mM plates, but in liquid MSM only five sustained growth up to 9 mM, and under stricter MIC conditions CD3 was the standout at 3 mM. (chatterjee2024multimodalcadmiumresistance pages 5-6)
- Inoculum effect (CD3): turbidity/growth thresholds shift strongly across ~10^5–10^2 CFU/mL starting inoculum; this is a major source of variability for MIC calls. (chatterjee2024multimodalcadmiumresistance pages 6-7, chatterjee2024multimodalcadmiumresistance media 9453c781)
- Soil isolates (USM1/USM4): **Cd2+ resistance up to 200 ppm** using MTC plating definition. (hovorukha2024metalresistanceof pages 2-3)

**6.2 Physiological evidence consistent with efflux**
- AAS partitioning in CD3 after Cd exposure showed **extracellular Cd ~85.33 ppm**, **intracellular ~13 ppm**, and **surface-bound ~9 ppm**, consistent with strong export and limited intracellular accumulation in live cells. (chatterjee2024multimodalcadmiumresistance pages 6-7, chatterjee2024multimodalcadmiumresistance media 186e4542)

**6.3 Engineered implementation metrics**
- Engineered *D. radiodurans* LOPM: **4.9-fold higher Cd adsorption** than wild-type, **84.9% Cd removal** after 48 h (under their conditions), and **rice Cd reduced to 47% (root) and 43.4% (shoot)** after colonization. (wang2024surfacedisplayof pages 1-2, wang2024surfacedisplayof pages 2-5)

### 7) Expert/authoritative analysis (cautionary notes for curation)

1) **Assay dependence is not a nuisance—it's causal context.** The CD3 work demonstrates that medium chemistry and inoculum density shift measured MIC materially; therefore nodes for **“assay medium composition”** and **“inoculum density”** may be needed as experimental modifiers (or at least as curation metadata) to avoid over-generalizing tolerance values. (chatterjee2024multimodalcadmiumresistance pages 3-4, chatterjee2024multimodalcadmiumresistance pages 6-7)

2) **Separate two mechanistic regimes:** 
- Low/moderate Cd where **biofilm/EPS-associated protection** contributes (community state), versus 
- Higher Cd where **active efflux systems dominate** (single-cell transport capacity). (chatterjee2024multimodalcadmiumresistance pages 1-2, chatterjee2024multimodalcadmiumresistance media 9453c781)

3) **Avoid over-curating review-only edges.** Some mechanistic assertions (e.g., broad claims about CzcCBA induction by Zn/Cu across taxa) are summarized in reviews and should ideally be backstopped by primary, system-specific studies for TraitMech curation. (sharma2024mechanismsofmicrobial pages 12-13)

4) **Mobile genetic elements matter.** The cadDX operon being carried on integrative/mobilizable elements implies that “cadmium tolerant” can be an **acquired trait**; including HGT edges may be appropriate for causal graphs intended to capture evolutionary acquisition. (zhu2024thecaddxoperon pages 1-2)

### 8) Visual evidence (figures/tables)
For CD3, the following panels were retrieved and support quantitative assertions:
- **Table 2:** inoculum-dependent Cd growth/turbidity thresholds (MIC-like readout). (chatterjee2024multimodalcadmiumresistance media 9453c781)
- **Figure 2:** AAS-based Cd partitioning (extracellular vs surface-bound vs intracellular; live vs heat-killed). (chatterjee2024multimodalcadmiumresistance media 186e4542)
- **Figure 3b:** biofilm quantification peaking around 0.75 mM CdCl2·H2O. (chatterjee2024multimodalcadmiumresistance media 9546d5cd)

### 9) DOI-first bibliography (with URLs; publication date where available)
1. Chatterjee S, Barman P, Barman C, Majumdar S, Chakraborty R. **Multimodal cadmium resistance and its regulatory networking in *Pseudomonas aeruginosa* strain CD3.** *Scientific Reports* (2024-12). DOI: **10.1038/s41598-024-80754-y**. https://doi.org/10.1038/s41598-024-80754-y (chatterjee2024multimodalcadmiumresistance pages 1-2)
2. Zhu X, Liang Z, Ma J, et al. **The cadDX operon contributes to cadmium resistance, oxidative stress resistance, and virulence in zoonotic streptococci.** *Veterinary Research* (2024-09). DOI: **10.1186/s13567-024-01371-1**. https://doi.org/10.1186/s13567-024-01371-1 (zhu2024thecaddxoperon pages 1-2)
3. Sharma M, Sharma S, Paavan, et al. **Mechanisms of microbial resistance against cadmium – a review.** *Journal of Environmental Health Science & Engineering* (2024-12 issue; online 2023). DOI: **10.1007/s40201-023-00887-6**. https://doi.org/10.1007/s40201-023-00887-6 (sharma2024mechanismsofmicrobial pages 12-13)
4. Hovorukha V, Moliszewska E, Havryliuk O, et al. **Metal Resistance of Microorganisms as a Crucial Factor for Their Homeostasis and Sustainable Environment.** *Sustainability* (2024-11). DOI: **10.3390/su16229655**. https://doi.org/10.3390/su16229655 (hovorukha2024metalresistanceof pages 2-3)
5. Wang L, Wang Y, Dai S, Wang B. **Surface Display of Multiple Metal-Binding Domains in *Deinococcus radiodurans* Alleviates Cadmium and Lead Toxicity in Rice.** *International Journal of Molecular Sciences* (2024-11). DOI: **10.3390/ijms252312570**. https://doi.org/10.3390/ijms252312570 (wang2024surfacedisplayof pages 1-2)

### 10) Warnings (do-not-curate-yet items)
- **BfmR/BfmS → biofilm → cadmium tolerance** is supported primarily by bioinformatic network inference and phenotypic correlation in CD3; without targeted knockouts/perturbations it should be curated as **UNCERTAIN**. (chatterjee2024multimodalcadmiumresistance pages 12-14, chatterjee2024pseudomonasaeruginosastrain pages 1-4)
- **CadR binds four Cd ions to activate CadA** appears in a proposed regulatory model in CD3; treat as **UNCERTAIN/model-derived** unless primary biochemical evidence is added. (chatterjee2024multimodalcadmiumresistance pages 17-19)
- **EPS-mediated cadmium sequestration** is review-supported but not demonstrated with organism-specific causal tests in the provided evidence; curate cautiously or require primary support. (sharma2024mechanismsofmicrobial pages 12-13)

---

### Appendix: TraitMech alignment note
The provided TraitMech definition emphasizes “cation-efflux resistance systems such as the czc determinant.” The recent evidence strongly supports including **CzcRS→CzcCBA** as a core module for Gram-negative cadmium tolerance graphs, while **cadDX/CadD/CadX** is a strong Gram-positive module that may be added as a parallel mechanism branch. (chatterjee2024multimodalcadmiumresistance pages 14-15, zhu2024thecaddxoperon pages 1-2)

References

1. (chatterjee2024multimodalcadmiumresistance pages 1-2): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

2. (chatterjee2024multimodalcadmiumresistance pages 3-4): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

3. (chatterjee2024multimodalcadmiumresistance pages 6-7): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

4. (chatterjee2024pseudomonasaeruginosastrain pages 4-7): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, Ranadhir Chakraborty, and Ranadhir Chakraborty. Pseudomonas aeruginosa strain cd3 implements cadmium resistance through multimodal systems and its regulatory networking. Unknown journal, Aug 2024. URL: https://doi.org/10.21203/rs.3.rs-4733845/v1, doi:10.21203/rs.3.rs-4733845/v1.

5. (hovorukha2024metalresistanceof pages 2-3): Vira Hovorukha, Ewa Moliszewska, Olesia Havryliuk, Iryna Bida, and Oleksandr Tashyrev. Metal resistance of microorganisms as a crucial factor for their homeostasis and sustainable environment. Sustainability, 16:9655, Nov 2024. URL: https://doi.org/10.3390/su16229655, doi:10.3390/su16229655. This article has 8 citations.

6. (chatterjee2024multimodalcadmiumresistance pages 14-15): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

7. (sharma2024mechanismsofmicrobial pages 12-13): Monu Sharma, Sonu Sharma, Paavan, Mahiti Gupta, Soniya Goyal, Daizee Talukder, Mohd. Sayeed Akhtar, Raman Kumar, Ahmad Umar, Abdulrab Ahmed M. Alkhanjaf, and Sotirios Baskoutas. Mechanisms of microbial resistance against cadmium - a review. Journal of environmental health science & engineering, 22 1:13-30, Dec 2024. URL: https://doi.org/10.1007/s40201-023-00887-6, doi:10.1007/s40201-023-00887-6. This article has 53 citations.

8. (zhu2024thecaddxoperon pages 1-2): Xinchi Zhu, Zijing Liang, Jiale Ma, Jinhu Huang, Liping Wang, Huochun Yao, and Zongfu Wu. The caddx operon contributes to cadmium resistance, oxidative stress resistance, and virulence in zoonotic streptococci. Veterinary Research, Sep 2024. URL: https://doi.org/10.1186/s13567-024-01371-1, doi:10.1186/s13567-024-01371-1. This article has 4 citations and is from a highest quality peer-reviewed journal.

9. (chatterjee2024multimodalcadmiumresistance pages 15-16): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

10. (chatterjee2024multimodalcadmiumresistance media 9453c781): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

11. (chatterjee2024multimodalcadmiumresistance pages 17-19): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

12. (chatterjee2024multimodalcadmiumresistance pages 12-14): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

13. (zhu2024thecaddxoperon pages 3-5): Xinchi Zhu, Zijing Liang, Jiale Ma, Jinhu Huang, Liping Wang, Huochun Yao, and Zongfu Wu. The caddx operon contributes to cadmium resistance, oxidative stress resistance, and virulence in zoonotic streptococci. Veterinary Research, Sep 2024. URL: https://doi.org/10.1186/s13567-024-01371-1, doi:10.1186/s13567-024-01371-1. This article has 4 citations and is from a highest quality peer-reviewed journal.

14. (wang2024surfacedisplayof pages 1-2): Liangyan Wang, Yudong Wang, Shang Dai, and Binqiang Wang. Surface display of multiple metal-binding domains in deinococcus radiodurans alleviates cadmium and lead toxicity in rice. International Journal of Molecular Sciences, 25:12570, Nov 2024. URL: https://doi.org/10.3390/ijms252312570, doi:10.3390/ijms252312570. This article has 9 citations.

15. (wang2024surfacedisplayof pages 2-5): Liangyan Wang, Yudong Wang, Shang Dai, and Binqiang Wang. Surface display of multiple metal-binding domains in deinococcus radiodurans alleviates cadmium and lead toxicity in rice. International Journal of Molecular Sciences, 25:12570, Nov 2024. URL: https://doi.org/10.3390/ijms252312570, doi:10.3390/ijms252312570. This article has 9 citations.

16. (chatterjee2024multimodalcadmiumresistance pages 16-17): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

17. (chatterjee2024pseudomonasaeruginosastrain pages 21-23): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, Ranadhir Chakraborty, and Ranadhir Chakraborty. Pseudomonas aeruginosa strain cd3 implements cadmium resistance through multimodal systems and its regulatory networking. Unknown journal, Aug 2024. URL: https://doi.org/10.21203/rs.3.rs-4733845/v1, doi:10.21203/rs.3.rs-4733845/v1.

18. (chatterjee2024pseudomonasaeruginosastrain pages 1-4): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, Ranadhir Chakraborty, and Ranadhir Chakraborty. Pseudomonas aeruginosa strain cd3 implements cadmium resistance through multimodal systems and its regulatory networking. Unknown journal, Aug 2024. URL: https://doi.org/10.21203/rs.3.rs-4733845/v1, doi:10.21203/rs.3.rs-4733845/v1.

19. (chatterjee2024multimodalcadmiumresistance pages 5-6): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

20. (chatterjee2024multimodalcadmiumresistance media 186e4542): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

21. (chatterjee2024multimodalcadmiumresistance media 9546d5cd): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.