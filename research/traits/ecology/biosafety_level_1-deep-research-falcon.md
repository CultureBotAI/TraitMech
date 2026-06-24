---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:01:38.113312'
end_time: '2026-06-17T20:12:08.454171'
duration_seconds: 630.34
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: biosafety level 1
  trait_identifier: METPO:1001102
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: biosafety_level_1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biosafety level that poses minimal potential hazard to laboratory
    workers and the environment, requiring only standard microbiological practices.
  parent_traits: METPO:1001101
  synonyms: '1'
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports the absence or low expression of virulence factors
    in BSL-1 agents (non-pathogenic to healthy adults).)'
  causal_graph_summary: 'biosafety_level_1_minimal_hazard: 3 nodes, 2 edges'
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
- **Trait label:** biosafety level 1
- **METPO identifier:** METPO:1001102
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses minimal potential hazard to laboratory workers and the environment, requiring only standard microbiological practices.
- **Parent traits:** METPO:1001101
- **Synonyms:** 1
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the absence or low expression of virulence factors in BSL-1 agents (non-pathogenic to healthy adults).)
- **Existing causal graph summary:** biosafety_level_1_minimal_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_1.yaml`.

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
- **Trait label:** biosafety level 1
- **METPO identifier:** METPO:1001102
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses minimal potential hazard to laboratory workers and the environment, requiring only standard microbiological practices.
- **Parent traits:** METPO:1001101
- **Synonyms:** 1
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the absence or low expression of virulence factors in BSL-1 agents (non-pathogenic to healthy adults).)
- **Existing causal graph summary:** biosafety_level_1_minimal_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_1.yaml`.

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


## Research report: Microbial trait “biosafety level 1” (METPO:1001102)

### Scope summary (trait meaning, boundaries, and near-neighbors)
Biosafety level 1 (BSL‑1) is best treated in TraitMech as a **risk-classification outcome** for laboratory work with microbial agents that pose **minimal hazard** and are **unlikely to cause disease in healthy adults**, typically handled using **general/standard microbiological practices** (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto pages 6-7). BSL‑1 is also described as appropriate for **basic teaching laboratories** and work with **defined and characterized strains** of viable microorganisms **not known to consistently cause disease in healthy adult humans** (siegel2022principlesofbiosafety pages 17-32, siegel2022principlesofbiosafety pages 32-44). 

Boundary conditions are not purely taxonomic; classification is **context- and activity-dependent**. Risk assessment factors that can move work outside BSL‑1 include pathogenicity, route of transmission, agent stability, infectious dose, concentration, origin, prophylaxis availability, and personnel experience (siegel2022principlesofbiosafety pages 32-44). The literature explicitly flags gray areas such as “opportunistic pathogens,” “vaccine strains,” and recombinant DNA constructs where inserted genes may encode toxins, indicating that BSL assignment is fundamentally a function of **hazard identification + exposure scenario** rather than a fixed organism label (siegel2022principlesofbiosafety pages 32-44).

Distinction from adjacent traits: BSL‑2 is consistently described as for **moderate hazard** agents or those with **moderate risk associated with human disease**, requiring additional control measures beyond BSL‑1 (e.g., protective clothing, biohazard signage) (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto pages 6-7). Thus, the key discriminant between BSL‑1 and BSL‑2 in a causal graph is not “microbe present” but “microbe/activity yields moderate vs minimal hazard,” mediated by virulence potential and exposure risks.

### Key concepts and definitions (current understanding)
**BSL as a layered control system.** Biosafety levels are commonly described as built from four elements: **standard microbiological practices, special practices, safety equipment, and laboratory facilities**, with ascending levels providing increasing protection to personnel, the environment, and the community (siegel2022principlesofbiosafety pages 17-32). 

**BSL‑1 defining criteria.** Recent synthesis sources define BSL‑1 as the level for **minimal-hazard/low-risk agents**, “unlikely to cause disease in healthy adults,” and aligned with baseline “general practices” and standard techniques (gao2024frombiosafetyto pages 5-6). A closely aligned formulation is that BSL‑1 work involves **defined/characterized strains** “not known to consistently cause disease in healthy adult humans” (siegel2022principlesofbiosafety pages 17-32, mendonca2024enhancingbiosafetymanagement pages 28-31).

**Facility/practice implications.** BSL‑1 is described as relying primarily on standard practices with minimal physical barriers; an operational summary lists basic features such as **a door, a handwashing sink, and non‑porous cleanable/decontaminable work surfaces** (mendonca2024enhancingbiosafetymanagement pages 28-31).

### Recent developments and latest research (prioritizing 2023–2024)
Recent work has emphasized (i) the **risk-assessment basis** of biosafety classification, (ii) the importance of **implementation quality** (training/adherence), and (iii) the need for evidence-based practices.

* **2024: BSL definitions and framing in the context of broader biosafety governance.** A 2024 review on biosafety laboratories reiterates the BSL‑1 definition and its contrast with BSL‑2, explicitly grounding the tiering concept in WHO guidance and the U.S. BMBL framework (gao2024frombiosafetyto pages 6-7).
* **2023: Evidence gaps and “evidence-based biosafety.”** A 2023 “Biosafety Research Road Map” effort (WOAH/WHO collaboration) frames good microbiological practices and risk assessment as foundational, and highlights evidence gaps that can lead to inappropriate or excessive controls—supporting the view that BSL‑1 classification should be tied to an explicit, defensible risk rationale rather than habit or institutional inertia (gao2025globalsafetyand pages 14-17).
* **2024: Practice implementation at scale.** A nationwide survey of China CDC microbiology laboratories (data collected 2021–2023; published Aug 2024) provides recent quantitative evidence that implementation varies by specific practice (e.g., high protocol coverage for PPE/disinfection/waste disposal, but notably lower coverage for handwashing and glassware washing), reinforcing that “BSL designation” and “effective risk reduction” can diverge in real-world settings (niu2024thestateof pages 2-3).

### Current applications and real-world implementations
BSL‑1 is widely used in **teaching and basic microbiology laboratories**, particularly for work with well-characterized, low-risk strains (siegel2022principlesofbiosafety pages 17-32, gao2024frombiosafetyto pages 5-6). Operationally, it is implemented through standard microbiological practices and basic facility provisions (handwashing sink; cleanable surfaces) (mendonca2024enhancingbiosafetymanagement pages 28-31).

**Teaching-laboratory implementation.** The ASM teaching-lab guideline update (2019) explicitly integrates risk assessment and consolidates BSL‑1/BSL‑2 guidance into a single structure spanning personal protection, physical space, stock culture requirements, standard practices, training, and documentation—underscoring that even “low-level” lab work requires systematic management and documentation (byrd2019guidelinesforbiosafety pages 1-2).

**Measured practice coverage and gaps (2023–2024 data).** In the 2024 China CDC survey, reported coverage rates for “general biosafety protocols” were high for PPE (97.17%), waste disposal (96.77%), disinfection (96.46%), and high-pressure sterilization (96.87%), but lower for hand washing (85.35%) and glassware washing (66.67%) (niu2024thestateof pages 2-3). These data are directly usable as implementation context nodes/attributes in curation.

### Mechanistic entities and candidate nodes (grouped by type; ontology grounding suggestions)
Below are candidate node sets suitable for `data/traits/ecology/biosafety_level_1.yaml`. Grounding is provided where stable CURIEs are available; otherwise, label-only nodes are recommended.

#### A) Trait / classification nodes
* **biosafety level 1** — METPO:1001102 (given)
* **biosafety level 2** — label-only candidate (near-neighbor trait for boundary edges) (gao2024frombiosafetyto pages 5-6)
* **risk group 1 agent** — label-only candidate (mapping to BSL‑1 is approximate/contextual) (siegel2022principlesofbiosafety pages 17-32)

#### B) Microbial hazard / pathogenicity nodes
* **low-risk agent** / **minimal hazard agent** — label-only candidate (gao2024frombiosafetyto pages 6-7)
* **not known to cause disease in healthy adult humans** — label-only candidate (siegel2022principlesofbiosafety pages 17-32)
* **specific virulence traits** — label-only candidate; mechanistic driver of pathogenicity (pokharel2023thediversityof pages 1-2)

#### C) Risk assessment factor nodes (determinants of BSL assignment)
* **pathogenicity**, **route of transmission**, **agent stability**, **infectious dose**, **agent concentration**, **agent origin**, **availability of prophylaxis/therapy**, **personnel experience** — label-only candidates (siegel2022principlesofbiosafety pages 32-44)
* **toxin-encoding inserted gene (rDNA/synthetic nucleic acid construct)** — label-only candidate (borderline trigger) (siegel2022principlesofbiosafety pages 32-44)

#### D) Operational practice and facility nodes (BSL‑1 enabling conditions)
* **standard microbiological practices** — label-only candidate (mendonca2024enhancingbiosafetymanagement pages 28-31)
* **hand washing** — label-only candidate (sarwar2022amodifiedhand pages 1-2)
* **handwashing sink** — label-only candidate (mendonca2024enhancingbiosafetymanagement pages 28-31, sarwar2022amodifiedhand pages 1-2)
* **cleanable non-porous work surfaces** — label-only candidate (mendonca2024enhancingbiosafetymanagement pages 28-31)

#### E) Implementation metrics (real-world operationalization)
* **biosafety training prior to work** — label-only candidate (niu2024thestateof pages 2-3)
* **protocol coverage: PPE, disinfection, waste disposal, hand washing, glassware washing** — label-only candidates/attributes (niu2024thestateof pages 2-3)

### Evidence-backed candidate causal edges (triples)
The following table provides curation-ready candidate edges with evidence snippets and notes.

| Subject node | Predicate | Object node | Node type tags | Ontology grounding suggestions | Evidence snippet | Source | DOI | URL | Publication date/month | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| low-risk agent | qualifies_for | biosafety level 1 | microbial property; biosafety classification | subject: label-only candidate; object: METPO:1001102 | “BSL-1 is described as the level for ‘low-risk agents unlikely to cause disease in healthy adults’” (gao2024frombiosafetyto pages 6-7) | Gao et al., 2024, *From Biosafety to National Security: The Evolution and Challenges of Biosafety Laboratories* | 10.3390/laboratories1030013 | https://doi.org/10.3390/laboratories1030013 | 2024-12 | Strong scope-defining edge for curation. Captures minimal-hazard classification basis for BSL-1. |
| not known to cause disease in healthy adult humans | qualifies_for | biosafety level 1 | microbial property; pathogenicity criterion; biosafety classification | subject: label-only candidate; object: METPO:1001102 | “defined and characterized strains of viable microorganisms not known to consistently cause disease in healthy adult humans” (siegel2022principlesofbiosafety pages 17-32) | Siegel, 2022, *Principles of Biosafety Course #31701* | 10.2172/1887109 | https://doi.org/10.2172/1887109 | 2022-09 | Strong definition-based edge. Good candidate node label for “low pathogenicity/nonpathogenic to healthy adults.” |
| defined and characterized strain | qualifies_for_work_at | biosafety level 1 | microbial property; strain characterization; biosafety classification | subject: label-only candidate; object: METPO:1001102 | “BSL-1 is described as appropriate for ‘High school and college labs, work with defined and characterized strains of viable microorganisms’” (siegel2022principlesofbiosafety pages 17-32) | Siegel, 2022, *Principles of Biosafety Course #31701* | 10.2172/1887109 | https://doi.org/10.2172/1887109 | 2022-09 | Strong but assay/context-specific: applies to laboratory use of defined strains, not an intrinsic trait of all taxa. |
| standard microbiological practices | enables_containment_at | biosafety level 1 | lab practice; containment practice; biosafety classification | subject: label-only candidate; object: METPO:1001102 | “BSL-1… represents a basic level of containment relying on standard microbiological best practices and procedures” (mendonca2024enhancingbiosafetymanagement pages 28-31) | Mendonça, 2024, *Enhancing Biosafety Management and Governance: A Comprehensive Assessment of High-Containment Biological Laboratories in Brazil* | 10.47328/ufvbbt.2024.220 | https://doi.org/10.47328/ufvbbt.2024.220 | 2024 | Strong operational edge, but note this is a containment/practice requirement rather than a microbial mechanism. |
| handwashing sink | supports | standard microbiological practices | facility feature; lab practice; engineering control | subject: label-only candidate; object: label-only candidate | “a door, a sink for handwashing, and non-porous work surfaces that are cleanable and easy to decontaminate” (mendonca2024enhancingbiosafetymanagement pages 28-31) | Mendonça, 2024, *Enhancing Biosafety Management and Governance: A Comprehensive Assessment of High-Containment Biological Laboratories in Brazil* | 10.47328/ufvbbt.2024.220 | https://doi.org/10.47328/ufvbbt.2024.220 | 2024 | Strong for BSL-1 facility support. Could be modeled as facility prerequisite rather than direct microbial-causal node. |
| cleanable non-porous work surface | supports | decontamination | facility feature; decontamination support | subject: label-only candidate; object: GO:0042737? (drug/cellular component decontamination not exact); better label-only | “non-porous work surfaces that are cleanable and easy to decontaminate” (mendonca2024enhancingbiosafetymanagement pages 28-31) | Mendonça, 2024, *Enhancing Biosafety Management and Governance: A Comprehensive Assessment of High-Containment Biological Laboratories in Brazil* | 10.47328/ufvbbt.2024.220 | https://doi.org/10.47328/ufvbbt.2024.220 | 2024 | Strong facility-to-process edge. Ontology grounding unclear; likely label-only for now. |
| hand washing | is_good_microbiological_practice | risk control measure | lab practice; GMPP; risk reduction | subject: label-only candidate; object: label-only candidate | “Among GMPP, one of the best practices is hand washing” (sarwar2022amodifiedhand pages 1-2) | Sarwar et al., 2022, *A Modified Hand Washing Method for Resource Limited Settings* | 10.3389/fpubh.2022.965853 | https://doi.org/10.3389/fpubh.2022.965853 | 2022-08 | Strong general biosafety edge; not BSL-1-specific but directly relevant to standard practices that underpin BSL-1. |
| handwashing sink | is_core_requirement_for | laboratory biosafety practice | facility feature; engineering control; biosafety infrastructure | subject: label-only candidate; object: label-only candidate | “handwashing sink, which is an engineering control, is also one of the core requirements for a laboratory” (sarwar2022amodifiedhand pages 1-2) | Sarwar et al., 2022, *A Modified Hand Washing Method for Resource Limited Settings* | 10.3389/fpubh.2022.965853 | https://doi.org/10.3389/fpubh.2022.965853 | 2022-08 | Useful infrastructure edge; can support BSL-1 facility node set. |
| modified handwashing method | increases | handwashing compliance | intervention; lab practice; implementation outcome | subject: label-only candidate; object: label-only candidate | “Eighty three percentage reported that this modified method of hand washing raised their hand washing compliance” (sarwar2022amodifiedhand pages 1-2) | Sarwar et al., 2022, *A Modified Hand Washing Method for Resource Limited Settings* | 10.3389/fpubh.2022.965853 | https://doi.org/10.3389/fpubh.2022.965853 | 2022-08 | Empirical implementation edge; uncertain for TraitMech because it is intervention-specific, small n=12, and BSL-2 veterinary labs rather than BSL-1. |
| risk assessment factors (pathogenicity, route of transmission, agent stability, infectious dose, concentration, origin, prophylaxis availability, personnel experience) | determine | biosafety level selection | risk assessment factor; decision factor; biosafety classification | subject: label-only candidate set; object: label-only candidate | “risk assessment criteria explicitly list pathogenicity, route of transmission, agent stability, infectious dose, concentration, origin, availability of prophylaxis, and experience of personnel as factors that determine risk and therefore biosafety level” (siegel2022principlesofbiosafety pages 32-44) | Siegel, 2022, *Principles of Biosafety Course #31701* | 10.2172/1887109 | https://doi.org/10.2172/1887109 | 2022-09 | Strong edge for graphing decision logic around BSL assignment. These are not microbial-only nodes, but highly relevant causal/assessment entities. |
| risk group 1 agent | aligns_with | biosafety level 1 | microbial property; risk group; biosafety classification | subject: label-only candidate; object: METPO:1001102 | “Risk Group 1: ‘Agents that are not associated with disease in healthy adult humans.’” with BSL-1 described for such work (siegel2022principlesofbiosafety pages 17-32) | Siegel, 2022, *Principles of Biosafety Course #31701* | 10.2172/1887109 | https://doi.org/10.2172/1887109 | 2022-09 | Reasonable alignment edge, but Risk Group and BSL are not strictly identical in all frameworks; curate with note that mapping is approximate/contextual. |
| toxin-encoding inserted gene | increases_risk_of | higher biosafety level selection | genetic feature; virulence determinant; risk assessment factor | subject: label-only candidate; object: label-only candidate | “Does the inserted gene encode a known toxin or a relatively uncharacterized toxin?” tying “genetic features directly to risk evaluation” (siegel2022principlesofbiosafety pages 32-44) | Siegel, 2022, *Principles of Biosafety Course #31701* | 10.2172/1887109 | https://doi.org/10.2172/1887109 | 2022-09 | Uncertain/inferred edge: snippet supports toxin genes as a risk assessment question, but does not explicitly state a required shift from BSL-1 to a specific higher level. |
| specific virulence traits | enable | disease causation | genetic feature; virulence factor; pathogenicity determinant | subject: label-only candidate; object: label-only candidate | “some E. coli strains… encode specific virulence traits that render them capable of causing disease” (pokharel2023thediversityof pages 1-2) | Pokharel et al., 2023, *The Diversity of Escherichia coli Pathotypes and Vaccination Strategies against This Versatile Bacterial Pathogen* | 10.3390/microorganisms11020344 | https://doi.org/10.3390/microorganisms11020344 | 2023-01 | Strong pathogen-mechanism edge, but not directly a BSL-1 classification statement. Useful as supporting rationale for why absence of virulence traits is compatible with BSL-1. |
| phylogroup A E. coli | tends_to_be | non-pathogenic | taxon-specific microbial property; pathogenicity | subject: NCBITaxon:562? plus strain/phylogroup label-only; object: label-only candidate | “Group A mostly represents non-pathogenic E. coli” (pokharel2023thediversityof pages 1-2) | Pokharel et al., 2023, *The Diversity of Escherichia coli Pathotypes and Vaccination Strategies against This Versatile Bacterial Pathogen* | 10.3390/microorganisms11020344 | https://doi.org/10.3390/microorganisms11020344 | 2023-01 | Taxon-specific and not a general BSL-1 rule; should be curated only if building example organism subgraphs. |
| biosafety training before laboratory work | supports | adherence to biosafety practices | training factor; implementation factor | subject: label-only candidate; object: label-only candidate | “Biosafety training prior to lab work reached 98.69%” and protocol coverage was high for several practices (niu2024thestateof pages 2-3, niu2024thestateof pages 1-2) | Niu et al., 2024, *The State of Biosafety Across China's CDC Microbiology Laboratories: Insights from a Nationwide Survey (2021–2023)* | 10.3389/fpubh.2024.1436503 | https://doi.org/10.3389/fpubh.2024.1436503 | 2024-08 | Supported at implementation level, but correlation/causation is not directly established in snippet; curate as supportive/operational, uncertain causal direction. |
| hand washing protocol coverage | indicates | incomplete implementation of biosafety practices | implementation metric; compliance metric | subject: label-only candidate; object: label-only candidate | “lower for hand washing (85.35%), lab cleaning/sanitation (82.42%), and glassware washing (66.67%)” (niu2024thestateof pages 2-3) | Niu et al., 2024, *The State of Biosafety Across China's CDC Microbiology Laboratories: Insights from a Nationwide Survey (2021–2023)* | 10.3389/fpubh.2024.1436503 | https://doi.org/10.3389/fpubh.2024.1436503 | 2024-08 | Descriptive implementation edge, not a mechanistic microbial edge. Useful for real-world practice context. |
| biosafety labeling deficiencies | may_compromise | compliant biosafety management | compliance factor; labeling; management practice | subject: label-only candidate; object: label-only candidate | “low for… biosafety labeling (52.05%)” (cong2025analysisofcompliance pages 1-2) | Cong et al., 2025, *Analysis of Compliance Issues and Influencing Factors in the Management of BSL-2 Laboratories for Pathogenic Microorganisms in Lishui, China* | 10.3389/fbioe.2025.1637056 | https://doi.org/10.3389/fbioe.2025.1637056 | 2025-08 | Useful real-world compliance edge; uncertain and not BSL-1-specific. Better as operational warning/background than core TraitMech edge. |
| access control management system | supports | compliant biosafety management | facility/administrative control; compliance factor | subject: label-only candidate; object: label-only candidate | “low pass rates were reported for the access control management system (85.94%)” (cong2025analysisofcompliance pages 1-2) | Cong et al., 2025, *Analysis of Compliance Issues and Influencing Factors in the Management of BSL-2 Laboratories for Pathogenic Microorganisms in Lishui, China* | 10.3389/fbioe.2025.1637056 | https://doi.org/10.3389/fbioe.2025.1637056 | 2025-08 | Operationally relevant but derived from BSL-2 lab management, not specific to BSL-1 minimal containment. Uncertain for direct curation. |


*Table: This table compiles evidence-backed candidate causal graph edges for the trait biosafety level 1, emphasizing definitional criteria, enabling practices, infrastructure, and implementation factors. It is useful for deciding which edges are strong enough for TraitMech curation and which should be marked uncertain or kept as operational context.*

### Expert opinions / authoritative analysis (from retrieved sources)
* **Risk-based tiering is foundational.** Recent reviews emphasize that biosafety levels are chosen based on the **biohazard level of the pathogens being processed**, and that each level defines measures to protect staff, the environment, and the public (gao2024frombiosafetyto pages 6-7).
* **BSL assignment depends on multiple risk indices, not only organism identity.** Risk assessment criteria enumerating pathogenicity, transmission route, stability, infectious dose, concentration, prophylaxis availability, and personnel experience provide an explicit framework for deciding whether work fits BSL‑1 vs higher containment (siegel2022principlesofbiosafety pages 32-44).
* **Evidence gaps can yield inappropriate controls.** The 2023 Biosafety Research Road Map frames a key challenge as insufficient evidence for some biosafety practices, which can result in “inappropriate or excessive” strategies—supporting cautious curation of edges that are often asserted but weakly evidenced (gao2025globalsafetyand pages 14-17).

### Relevant statistics and data from recent studies (2023–2024 prioritized)
**Nationwide biosafety practice survey (China CDC microbiology labs; data 2021–2023; published 2024).**
* Respondents: 990 valid responses (niu2024thestateof pages 1-2).
* Presence of BSL‑2 labs: 98.69%; presence of BSL‑3 labs: 24.14% (niu2024thestateof pages 2-3).
* Biosafety training before lab work: 98.69% (niu2024thestateof pages 2-3).
* General protocol coverage: PPE 97.17%, waste disposal 96.77%, disinfection 96.46%, high-pressure sterilization 96.87% (niu2024thestateof pages 2-3).
* Lower coverage items: hand washing 85.35%, lab cleaning/sanitation 82.42%, glassware washing 66.67% (niu2024thestateof pages 2-3).

These statistics are useful as **implementation-context annotations**, particularly for nodes representing “hand washing practice” and “training,” which are frequently treated as assumed rather than measured.

### Warnings / non-curatable (yet) claims
1. **Primary manual text not directly retrieved.** Although multiple sources explicitly attribute the BSL framework to WHO guidance and the U.S. BMBL, the current evidence base here relies on secondary summaries (reviews/technical reports) rather than direct quotations from the BMBL 6th edition or WHO LBM4. Curate edges conservatively, and consider adding primary-document citations during final YAML review. (gao2024frombiosafetyto pages 6-7, mendonca2024enhancingbiosafetymanagement pages 28-31)
2. **Do not overinterpret Risk Group ↔ BSL equivalence.** Mapping RG1 to BSL‑1 is often directionally correct but not universally identical across jurisdictions/activities; retain an “aligns_with” or “often corresponds_to” relation rather than strict equivalence. (siegel2022principlesofbiosafety pages 17-32)
3. **Toxin gene → higher BSL is suggested but not explicit.** The presence of a toxin-encoding inserted gene is clearly presented as a risk assessment question, but the specific containment consequence is not stated in the snippet; mark this as uncertain/inferred until primary guidance is cited. (siegel2022principlesofbiosafety pages 32-44)
4. **Intervention evidence (handwashing method) is BSL‑2 and small n.** The Sarwar et al. handwashing compliance improvement (83% self-reported) is valuable as an implementation example, but may not be generalizable to BSL‑1 classification or broad biosafety performance. (sarwar2022amodifiedhand pages 1-2)

### DOI-first bibliography (with URLs and dates)
| Citation (APA-ish short) | Publication date | DOI | URL | Source type | Key contribution to BSL-1 trait graph |
|---|---|---|---|---|---|
| Gao, Wu, Zuo, Xiang, Zhang, Chen, Tan, & Liu (2024) | 2024-12 | 10.3390/laboratories1030013 | https://doi.org/10.3390/laboratories1030013 | Review | Summarizes WHO/BMBL-aligned definitions of BSL-1 as minimal-hazard/low-risk work with agents unlikely to cause disease in healthy adults and contrasts BSL-1 with BSL-2 containment expectations. (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto pages 6-7) |
| de Oliveira Mendonça (2024) | 2024 | 10.47328/ufvbbt.2024.220 | https://doi.org/10.47328/ufvbbt.2024.220 | Technical report / assessment | Provides practical BSL-1 facility and practice features—standard microbiological practices, a door, a handwashing sink, and cleanable non-porous surfaces—useful for operational nodes and edges. (mendonca2024enhancingbiosafetymanagement pages 28-31) |
| Niu, Sun, Zhang, Zhao, Tian, Cheng, Zheng, Guo, Zhang, Ma, & Wang (2024) | 2024-08 | 10.3389/fpubh.2024.1436503 | https://doi.org/10.3389/fpubh.2024.1436503 | Nationwide survey | Supplies recent real-world biosafety implementation statistics, including training prevalence and protocol coverage for handwashing, disinfection, PPE, and other practices relevant to BSL implementation context. (niu2024thestateof pages 2-3, niu2024thestateof pages 1-2) |
| Siegel (2022) | 2022-09 | 10.2172/1887109 | https://doi.org/10.2172/1887109 | Technical course/report | Defines BSL-1 as appropriate for defined, characterized strains not known to consistently cause disease in healthy adults and lists risk-assessment determinants that drive biosafety-level selection. (siegel2022principlesofbiosafety pages 17-32, siegel2022principlesofbiosafety pages 32-44) |
| Sarwar, Muhammad, & Shahzad (2022) | 2022-08 | 10.3389/fpubh.2022.965853 | https://doi.org/10.3389/fpubh.2022.965853 | Intervention study / technical report | Supports handwashing as a core good microbiological practice and provides empirical evidence that a modified handwashing method improved reported compliance in resource-limited labs. (sarwar2022amodifiedhand pages 1-2) |
| Cong, Li, Lou, Zhu, Zhang, Cheng, & Chen (2025) | 2025-08 | 10.3389/fbioe.2025.1637056 | https://doi.org/10.3389/fbioe.2025.1637056 | Compliance study | Adds recent compliance metrics for biosafety management, labeling, access control, and wash/shower infrastructure, informing cautionary operational context for lab biosafety implementation. (cong2025analysisofcompliance pages 1-2) |
| Pokharel, Dhakal, & Dozois (2023) | 2023-01 | 10.3390/microorganisms11020344 | https://doi.org/10.3390/microorganisms11020344 | Review | Links pathogenicity to specific virulence traits in E. coli, supporting the mechanistic rationale that absence of such determinants is compatible with low-risk/BSL-1 classification. (pokharel2023thediversityof pages 1-2) |
| Byrd, Emmert, Maxwell, & Townsend (2019) | 2019-01 | 10.1128/jmbe.v20i3.1975 | https://doi.org/10.1128/jmbe.v20i3.1975 | Guideline / teaching-lab manual | Highlights teaching-lab biosafety structure, including risk assessment, personal protection, physical space, standard practices, and training/documentation relevant to BSL-1 educational settings. (byrd2019guidelinesforbiosafety pages 1-2) |
| Blacksell, Dhawan, Kusumoto, Le, Summermatter, O'Keefe, Kozlovac, Almuhairi, Sendow, Scheel, Ahumibe, Masuku, Bennett, Kojima, Harper, & Hamilton (2023) | 2023-06 | 10.1089/apb.2022.0040 | https://doi.org/10.1089/apb.2022.0040 | Review / roadmap | Provides broader biosafety evidence context by emphasizing good microbiological practices and risk-based biosafety decision-making, useful as supporting framework context for BSL-1 curation. (gao2025globalsafetyand pages 14-17) |


*Table: This table compiles the DOI-first bibliography for sources used to build the BSL-1 trait causal graph report. It highlights each source's publication details, source type, and specific contribution to defining BSL-1 scope, mechanisms, practices, and implementation context.*


References

1. (gao2024frombiosafetyto pages 5-6): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

2. (gao2024frombiosafetyto pages 6-7): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

3. (siegel2022principlesofbiosafety pages 17-32): Dina Siegel. Principles of biosafety course # 31701. ArXiv, Sep 2022. URL: https://doi.org/10.2172/1887109, doi:10.2172/1887109. This article has 0 citations.

4. (siegel2022principlesofbiosafety pages 32-44): Dina Siegel. Principles of biosafety course # 31701. ArXiv, Sep 2022. URL: https://doi.org/10.2172/1887109, doi:10.2172/1887109. This article has 0 citations.

5. (mendonca2024enhancingbiosafetymanagement pages 28-31): André de Oliveira Mendonça. Enhancing biosafety management and governance: a comprehensive assessment of high-containment biological laboratories in brazil. ArXiv, 2024. URL: https://doi.org/10.47328/ufvbbt.2024.220, doi:10.47328/ufvbbt.2024.220. This article has 2 citations.

6. (gao2025globalsafetyand pages 14-17): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. Global safety and health: the history of high-level biosafety laboratories toward large scientific facilities. Laboratories, 2:3, Jan 2025. URL: https://doi.org/10.3390/laboratories2010003, doi:10.3390/laboratories2010003. This article has 2 citations.

7. (niu2024thestateof pages 2-3): Peihua Niu, Zhenlu Sun, Ruiqing Zhang, Yiming Zhao, Fengyu Tian, Ping Cheng, Hongmei Zheng, Jianqiang Guo, Meng Zhang, Xuejun Ma, and Ji Wang. The state of biosafety across china's cdc microbiology laboratories: insights from a nationwide survey (2021–2023). Frontiers in Public Health, Aug 2024. URL: https://doi.org/10.3389/fpubh.2024.1436503, doi:10.3389/fpubh.2024.1436503. This article has 5 citations.

8. (byrd2019guidelinesforbiosafety pages 1-2): Jeffrey J. Byrd, Elizabeth Emmert, Robert Maxwell, and Heather Townsend. Guidelines for biosafety in teaching laboratories version 2.0: a revised and updated manual for 2019. Journal of Microbiology & Biology Education, Jan 2019. URL: https://doi.org/10.1128/jmbe.v20i3.1975, doi:10.1128/jmbe.v20i3.1975. This article has 30 citations and is from a peer-reviewed journal.

9. (pokharel2023thediversityof pages 1-2): Pravil Pokharel, S. Dhakal, and C. Dozois. The diversity of escherichia coli pathotypes and vaccination strategies against this versatile bacterial pathogen. Microorganisms, Jan 2023. URL: https://doi.org/10.3390/microorganisms11020344, doi:10.3390/microorganisms11020344. This article has 286 citations.

10. (sarwar2022amodifiedhand pages 1-2): Samreen Sarwar, Javed Muhammad, and Faheem Shahzad. A modified hand washing method for resource limited settings. Frontiers in Public Health, Aug 2022. URL: https://doi.org/10.3389/fpubh.2022.965853, doi:10.3389/fpubh.2022.965853. This article has 5 citations.

11. (niu2024thestateof pages 1-2): Peihua Niu, Zhenlu Sun, Ruiqing Zhang, Yiming Zhao, Fengyu Tian, Ping Cheng, Hongmei Zheng, Jianqiang Guo, Meng Zhang, Xuejun Ma, and Ji Wang. The state of biosafety across china's cdc microbiology laboratories: insights from a nationwide survey (2021–2023). Frontiers in Public Health, Aug 2024. URL: https://doi.org/10.3389/fpubh.2024.1436503, doi:10.3389/fpubh.2024.1436503. This article has 5 citations.

12. (cong2025analysisofcompliance pages 1-2): Ying Cong, Jinkai Li, Dingshuo Lou, Jianliang Zhu, Deyong Zhang, Dongqing Cheng, and Xiuying Chen. Analysis of compliance issues and influencing factors in the management of bsl-2 laboratories for pathogenic microorganisms in lishui, china. Frontiers in Bioengineering and Biotechnology, Aug 2025. URL: https://doi.org/10.3389/fbioe.2025.1637056, doi:10.3389/fbioe.2025.1637056. This article has 2 citations.