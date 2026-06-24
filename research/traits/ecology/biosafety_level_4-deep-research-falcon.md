---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:01:47.139327'
end_time: '2026-06-17T20:16:29.762567'
duration_seconds: 882.62
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: biosafety level 4
  trait_identifier: METPO:1001105
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: biosafety_level_4
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biosafety level that poses extreme risk of life-threatening disease
    through aerosol transmission with no available treatment.
  parent_traits: METPO:1001101
  synonyms: '4'
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports the extreme virulence and absence of countermeasures
    characteristic of BSL-4 agents.)'
  causal_graph_summary: 'biosafety_level_4_extreme_hazard: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 4
- **METPO identifier:** METPO:1001105
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses extreme risk of life-threatening disease through aerosol transmission with no available treatment.
- **Parent traits:** METPO:1001101
- **Synonyms:** 4
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the extreme virulence and absence of countermeasures characteristic of BSL-4 agents.)
- **Existing causal graph summary:** biosafety_level_4_extreme_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_4.yaml`.

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
- **Trait label:** biosafety level 4
- **METPO identifier:** METPO:1001105
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses extreme risk of life-threatening disease through aerosol transmission with no available treatment.
- **Parent traits:** METPO:1001101
- **Synonyms:** 4
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports the extreme virulence and absence of countermeasures characteristic of BSL-4 agents.)
- **Existing causal graph summary:** biosafety_level_4_extreme_hazard: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **biosafety level 4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_4.yaml`.

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


## Microbial trait causal-graph research report: **Biosafety level 4** (METPO:1001105)

### Trait metadata
- **Trait label:** biosafety level 4 (BSL-4)
- **METPO identifier:** METPO:1001105
- **Trait category:** ECOLOGY (containment ecology / lab-handling ecology)
- **Template definition (given):** “A biosafety level that poses extreme risk of life-threatening disease through aerosol transmission with no available treatment.”

---

## 1) Scope summary (what this trait represents)

### Current understanding / key definition
BSL-4 is best curated as a **laboratory containment requirement** assigned to work with pathogens/toxins that pose **maximum hazard**, particularly those with **high individual/community risk**, potentially including **high risk of aerosol-transmitted laboratory infection** and for which **effective prevention and/or treatment are not usually available** (kaufer2020laboratorybiosafetymeasures pages 4-5, kaufer2020laboratorybiosafetymeasures pages 3-4). In practice, BSL-4 maps to “maximum containment” facilities and procedures (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto media 73d2b0be).

A highly specific definition used in laboratory biosafety literature is that BSL-4/PC-4 laboratories are for agents that “pose a high risk of aerosol-transmitted laboratory infections with no vaccine or therapy” (kaufer2020laboratorybiosafetymeasures pages 4-5). This aligns closely with the METPO definition supplied in the prompt.

### Boundary cases and distinctions from nearby traits
- **BSL-3 vs BSL-4:** BSL-3 is described for agents “that can be transmitted by air and cause potentially lethal infection through respiratory transmission,” with controls such as directional airflow and respirator use when required (kaufer2020laboratorybiosafetymeasures pages 4-5). BSL-4 adds *maximum containment* measures and is reserved for the most dangerous agents, often lacking countermeasures, and/or with very high aerosol lab-infection risk (kaufer2020laboratorybiosafetymeasures pages 4-5, gao2024frombiosafetyto pages 6-7).
- **Risk Group 4 (RG4) vs BSL-4:** Risk groups classify organisms by hazard, while BSL classifies containment. A quoted RG4 definition states RG4 organisms “cause life-threatening disease,” are “readily transmissible,” and “effective prevention and/or treatment are not usually available” (kaufer2020laboratorybiosafetymeasures pages 3-4). Curationally, RG4 is a strong upstream “hazard classification” node that often drives a BSL-4 decision.

**Curation warning on scope:** BSL-4 is a *property of required containment for laboratory work*, not an intrinsic metabolic pathway/physiology. A TraitMech graph should therefore focus on **hazard determinants** (e.g., aerosol infectivity risk, severity, countermeasure absence) and **contextual containment factors** (engineering controls), and treat pathogen-specific molecular mechanisms as **supporting exemplars** rather than universal prerequisites.

---

## 2) Candidate causal-graph entities (grouped by type)

### A. High-level hazard determinants (trait-defining or near-defining)
- **High risk of aerosol-transmitted laboratory infection** (label-only node; aligns with “aerosol transmission” clause) (kaufer2020laboratorybiosafetymeasures pages 4-5)
- **Life-threatening disease severity** (label-only node) (kaufer2020laboratorybiosafetymeasures pages 3-4, gao2024frombiosafetyto pages 6-7)
- **Readily transmissible / high community risk** (label-only node) (kaufer2020laboratorybiosafetymeasures pages 3-4)
- **No vaccine or therapy / lack of effective prevention or treatment** (label-only node) (kaufer2020laboratorybiosafetymeasures pages 4-5, kaufer2020laboratorybiosafetymeasures pages 3-4)

### B. Containment environment / experimental factors (BSL-4 implementation nodes)
- **Maximum containment facility** (label-only node) (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto media 73d2b0be)
- **Class III biological safety cabinet (BSC)** (label-only node) (kaufer2020laboratorybiosafetymeasures pages 4-5)
- **Positive-pressure, air-supplied suit** (PPE node; “suit lab”) (kaufer2020laboratorybiosafetymeasures pages 4-5, gao2024frombiosafetyto pages 3-5)
- **Isolated and restricted zone** (facility access-control node) (kaufer2020laboratorybiosafetymeasures pages 4-5)
- **Dedicated supply and exhaust air** (engineering control node) (kaufer2020laboratorybiosafetymeasures pages 4-5)
- **Airlocks** (facility feature) (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto media 73d2b0be)
- **Showers upon exiting / decontamination shower** (procedure/facility feature) (kaufer2020laboratorybiosafetymeasures pages 4-5, gao2024frombiosafetyto pages 5-6)
- **Specialized waste disposal** (procedure/facility feature) (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto media 73d2b0be)
- **Material decontamination before exit** (procedure) (kaufer2020laboratorybiosafetymeasures pages 4-5)

### C. Pathogen exemplar nodes (taxon-specific mechanistic entities; useful to justify hazard determinants)
The evidence corpus contains strong mechanistic details for **Nipah virus (NiV)** as an exemplar BSL-4 agent.
- **Taxon:** Nipah henipavirus (suggested grounding: `NCBITaxon:12110`) (fauscotino2024nipahvirusa pages 1-3)
- **Host receptor usage:** ephrin-B2 / ephrin-B3 (candidate grounding: human genes `EFNB2` / `EFNB3`—not provided as CURIE in evidence) (mehnaz2024thecurrentpathogenicity pages 2-3, anish2024pandemicpotentialof pages 2-3)
- **Tropism/clinical syndrome:** respiratory involvement; central nervous system involvement/encephalitis (hassan2024nipahvirusdisease pages 1-4, fauscotino2024nipahvirusa pages 1-3)
- **Immune evasion / IFN antagonism:** NiV V and W inhibit interferon production; V/W with P interfere with interferon signaling (fauscotino2024nipahvirusa pages 1-3)
- **Environmental persistence (exposure ecology):** survival in bat urine and date palm sap (fauscotino2024nipahvirusa pages 5-7)

### D. Governance/ethics context nodes (real-world implementation drivers; optional for TraitMech)
- **Risk assessment (with uncertainty, proportionality principle)** (resnik2024biosafetybiosecurityand pages 13-16)
- **Democratic governance / stakeholder engagement in biosafety oversight** (resnik2024biosafetybiosecurityand pages 23-25)
- **Biosecurity (protection/control/accountability for high-consequence agents)** (resnik2024biosafetybiosecurityand pages 1-3)

---

## 3) Candidate evidence-backed causal edges (curation-ready)

The table below emphasizes edges that can be directly curated into a TraitMech-style graph. General trait-defining edges come first, followed by NiV exemplar mechanistic edges.

| Edge (subject—predicate—object) | Node type(s) | Suggested ontology grounding (CURIEs) for subject / object | Evidence (citation id) | Supporting snippet (verbatim or near-verbatim) | Notes/curation confidence |
|---|---|---|---|---|---|
| life-threatening disease — requires containment level — biosafety level 4 | disease phenotype → containment class | subject: label-only candidate `life-threatening disease`; object: `METPO:1001105` | (kaufer2020laboratorybiosafetymeasures pages 3-4, gao2024frombiosafetyto pages 6-7) | “Organisms that cause life-threatening disease in a healthy host…”; “BSL-4 as the highest containment level for the most dangerous, life-threatening agents” | Strong, general. Trait-level criterion, but wording comes from RG4/BSL-4 definitions rather than a single ontology source. |
| lack of effective prevention or treatment — requires containment level — biosafety level 4 | clinical countermeasure status → containment class | subject: label-only candidate `absence of effective prevention/treatment`; object: `METPO:1001105` | (kaufer2020laboratorybiosafetymeasures pages 3-4, gao2024frombiosafetyto pages 6-7) | “effective prevention and/or treatment are not usually available”; “BSL-4 representing maximum containment for agents posing severe risks and no available treatments” | Strong, general. Matches supplied trait definition closely. |
| high risk of aerosol-transmitted laboratory infection — requires containment level — biosafety level 4 | transmission risk property → containment class | subject: label-only candidate `high risk of aerosol-transmitted laboratory infections`; object: `METPO:1001105` | (kaufer2020laboratorybiosafetymeasures pages 4-5) | “pose a high risk of aerosol-transmitted laboratory infections with no vaccine or therapy” | Strong, general. Best direct support for aerosol-specific BSL-4 criterion. |
| biosafety level 4 containment — necessitates use of — positive-pressure air-supplied suit | containment class → PPE | subject: `METPO:1001105`; object: label-only candidate `full body positive-pressure air-supplied suit` | (kaufer2020laboratorybiosafetymeasures pages 4-5, gao2024frombiosafetyto pages 3-5) | “wearing a full body, positive pressure, air supplied suit”; “High-containment ‘suit lab’ facilities… adopted positive pressure suits as a hallmark advanced containment strategy” | Strong, general. Direct operational feature of BSL-4 labs. |
| biosafety level 4 containment — requires — airlocks | containment class → facility feature | subject: `METPO:1001105`; object: label-only candidate `airlock` | (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto media 73d2b0be) | “requires airlocks, showers, and specialized waste disposal”; “Maximum Containment… requiring specialized measures such as airlocks” | Strong, general. Facility-level engineering control, not microbial mechanism. |
| biosafety level 4 containment — requires — showers | containment class → facility feature | subject: `METPO:1001105`; object: label-only candidate `decontamination shower` | (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto media 73d2b0be) | “requires airlocks, showers, and specialized waste disposal” | Strong, general. Engineering/procedural control. |
| biosafety level 4 containment — requires — specialized waste disposal | containment class → facility feature/process | subject: `METPO:1001105`; object: label-only candidate `specialized waste disposal` | (gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto media 73d2b0be) | “requires airlocks, showers, and specialized waste disposal” | Strong, general. Engineering/procedural control. |
| Nipah virus — has required containment level — biosafety level 4 | taxon/pathogen → containment class | subject: `NCBITaxon:12110` (Nipah henipavirus); object: `METPO:1001105` | (fauscotino2024nipahvirusa pages 1-3, saha2024recentadvancesof pages 1-2, mehnaz2024thecurrentpathogenicity pages 1-2) | “Nipah virus (NiV) is classified as a Biosafety Level 4 agent”; “NiV is handled as a BSL-4 agent”; “can only be done in Biosafety Level 4 (BSL-4) labs” | Strong, taxon-specific. Appropriate as exemplar support for a BSL-4 pathogen, not as universal mechanism for all BSL-4 agents. |
| Nipah virus V protein — inhibits — interferon production/signaling | viral protein → host immune process | subject: label-only candidate `NiV V protein`; object: `GO:0060337` or label-only `interferon signaling / interferon production` | (fauscotino2024nipahvirusa pages 1-3) | “viral proteins V and W inhibit interferon production and, together with P, interfere with interferon signaling” | Moderate, taxon-specific. GO grounding uncertain because source conflates production and signaling. Curate cautiously. |
| Nipah virus W protein — inhibits — interferon production/signaling | viral protein → host immune process | subject: label-only candidate `NiV W protein`; object: `GO:0060337` or label-only `interferon signaling / interferon production` | (fauscotino2024nipahvirusa pages 1-3) | “viral proteins V and W inhibit interferon production and, together with P, interfere with interferon signaling” | Moderate, taxon-specific. Same caution as above. |
| Nipah virus P protein — interferes with — interferon signaling | viral protein → host immune process | subject: label-only candidate `NiV P protein`; object: `GO:0060337` or label-only `interferon signaling` | (fauscotino2024nipahvirusa pages 1-3) | “viral proteins V and W inhibit interferon production and, together with P, interfere with interferon signaling” | Moderate, taxon-specific. Mechanistically relevant but extracted from review summary. |
| inhibition of interferon pathways — contributes to — immune evasion | host immune process perturbation → pathogenic process | subject: label-only candidate `interferon pathway inhibition`; object: label-only candidate `immune evasion` | (fauscotino2024nipahvirusa pages 1-3, mehnaz2024thecurrentpathogenicity pages 2-3) | “Mechanistic determinants linked to high consequence include… immune evasion”; “henipaviruses encode accessory proteins that aid immune evasion” | Moderate, inferred-but-well-supported. Useful mechanistic bridge; wording is summary-level rather than direct causal experiment in this conversation. |
| immune evasion — increases — disease severity/high consequence | pathogenic process → disease severity | subject: label-only candidate `immune evasion`; object: label-only candidate `increased disease severity` | (fauscotino2024nipahvirusa pages 1-3, hassan2024nipahvirusdisease pages 1-4) | “Mechanistic determinants linked to high consequence include…”; “rapidly progressive illness that affects the respiratory and central nervous systems” | Uncertain/inferred. High biological plausibility, but direct experimental causality not quoted here; do not overstate. |
| Nipah virus respiratory involvement — facilitates — person-to-person airway transmission | disease manifestation/tropism → transmission mode | subject: label-only candidate `respiratory involvement`; object: label-only candidate `person-to-person airway transmission` | (fauscotino2024nipahvirusa pages 1-3, fauscotino2024nipahvirusa pages 5-7, hassan2024nipahvirusdisease pages 1-4) | “respiratory involvement and interhuman airway spread”; “primarily via airway transmission (aerosols/droplets) with close contact”; “affects the respiratory… systems” | Strong, taxon-specific. Good mechanistic epidemiology edge for NiV. |
| ephrin-B2/B3 receptor usage — enables — broad host range | receptor interaction → host range property | subject: label-only candidate `ephrin-B2/B3 receptor usage`; object: label-only candidate `broad host range` | (mehnaz2024thecurrentpathogenicity pages 2-3, anish2024pandemicpotentialof pages 2-3) | “G and F glycoproteins mediating attachment and fusion via ephrin-B2/B3 receptors”; “use of an evolutionarily conserved, widely expressed receptor… broad host species tropism” | Strong, taxon-specific. Good mechanistic edge if receptor node can be grounded later (e.g., ephrin-B2/EFNB2, ephrin-B3/EFNB3). |
| broad host range — increases — spillover risk | host range property → ecological risk | subject: label-only candidate `broad host range`; object: label-only candidate `spillover risk` | (fauscotino2024nipahvirusa pages 1-3, fauscotino2024nipahvirusa pages 7-9, anish2024pandemicpotentialof pages 2-3) | “wide geographic range underlying recurrent spillovers”; “wide host range and demonstrated capacity of interspecies… transmission”; “broad host species tropism… factors increasing transmissibility and pandemic threat” | Strong, taxon-specific. Ecological edge suitable for TraitMech if represented as pathogen-specific exemplar, not universal BSL-4 rule. |


*Table: This table compiles curation-ready candidate causal edges for the trait biosafety level 4, using only evidence available in the conversation. It separates general BSL-4 defining criteria from Nipah virus-specific mechanistic exemplars and flags confidence and curation caveats.*

**Note on graph modularization:** In YAML, it may be helpful to separate (i) a **core “BSL-4 determinants” subgraph** (aerosol lab-infection risk, severity, countermeasure absence → BSL-4), from (ii) **implementation/control subgraph** (BSL-4 → suits/airlocks/showers/waste disposal), and (iii) **exemplar pathogen subgraph** (NiV molecular mechanisms → severity/transmission determinants → BSL-4).

---

## 4) Recent developments and latest research (prioritize 2023–2024)

### 4.1 Updated framing: biosafety labs as part of national security / governance systems
A 2024 historical review emphasizes the co-evolution of biosafety laboratories with social needs, public health demands, and **national security considerations**, positioning high-containment labs as part of biodefense and preparedness systems (Gao et al., 2024-12; https://doi.org/10.3390/laboratories1030013) (gao2024frombiosafetyto pages 12-15).

### 4.2 Ethics and expert analysis: BSL-4 decisions are not purely technical
A 2024 bioethics analysis argues that biosafety decisions (including what BSL to use) implicate ethical questions around **risk assessment, risk management, and risk distribution**, noting that expert risk estimates often diverge because of **deep uncertainty and limited/inconsistent data**; it also advocates for democratic oversight mechanisms (Resnik, 2024-07; https://doi.org/10.1007/s40592-024-00204-3) (resnik2024biosafetybiosecurityand pages 13-16, resnik2024biosafetybiosecurityand pages 23-25).

### 4.3 High-consequence pathogen updates relevant to BSL-4: Nipah virus (2024)
Recent 2024 reviews synthesize why NiV remains a canonical BSL-4 agent: it is explicitly classified as BSL-4 (Faus-Cotino et al., 2024-01; https://doi.org/10.3390/v16020179) (fauscotino2024nipahvirusa pages 1-3) and is associated with severe disease affecting respiratory/CNS systems and ongoing concern about person-to-person transmission (Hassan et al., 2024-07; https://doi.org/10.1016/S1473-3099(23)00707-7) (hassan2024nipahvirusdisease pages 1-4). These reviews also document mechanistic determinants linked to immune evasion and transmission (fauscotino2024nipahvirusa pages 1-3, fauscotino2024nipahvirusa pages 5-7).

---

## 5) Current applications and real-world implementations

### 5.1 BSL-4 facility operations (engineering + procedural controls)
Concrete operational controls repeatedly cited for BSL-4 include: all work in Class III BSC or using a “full body, positive pressure, air supplied suit,” work in an “isolated and restricted zone,” dedicated supply/exhaust air, changing clothing before entry, showering on exit, and decontaminating materials before exiting (kaufer2020laboratorybiosafetymeasures pages 4-5). A 2024 review summarizes core maximum-containment facility features as including **airlocks, showers, and specialized waste disposal** (gao2024frombiosafetyto pages 5-6), with visual evidence from a table summarizing BSL-4 requirements (gao2024frombiosafetyto media 73d2b0be).

### 5.2 Public-health preparedness: BSL-4 as enabling platform for countermeasure R&D
While BSL-4 implies that licensed countermeasures may be absent, BSL-4 labs are a real-world platform for developing them. For NiV specifically, a 2024 Lancet Infectious Diseases review states “Currently, there are no approved vaccine or therapies available for NiV disease” and discusses the need to improve patient care (Hassan et al., 2024-07; https://doi.org/10.1016/S1473-3099(23)00707-7) (hassan2024nipahvirusdisease pages 1-4). A 2024 systematic review (preprint) also frames prioritization of candidate therapeutics and notes recognized pandemic potential and high CFR (Chan et al., 2024-03; https://doi.org/10.1101/2024.03.11.24304091) (hassan2024nipahvirusdisease pages 1-4).

---

## 6) Relevant statistics and data (recent)

### 6.1 U.S. registered entity statistics (FSAP 2024 annual report; 2023 data)
The Federal Select Agent Program annual statistics report that, in 2023, **3% of entities were approved to work in a BSL-4/ABSL-4 laboratory**, corresponding to **8 entities** in Table 4 (FSAP 2024 annual report; publication year not captured in the extracted metadata, but report titled “2024 annual report | key statistics”) (wereUnknownyearfederalselectagenta pages 14-16, wereUnknownyearfederalselectagent pages 14-16). These 8 entities were all registered for Tier 1 BSAT in that table (wereUnknownyearfederalselectagenta pages 14-16).

### 6.2 High-consequence disease outcome statistics (NiV example, 2024)
Recent summaries of NiV outbreaks report very high and variable case fatality, e.g., Malaysia ~40%, Bangladesh ~70%, India ~68%, with specific Bangladesh outbreak CFRs reported as 71% (10 deaths/14 cases) in one account (Hassan et al., 2024-07; https://doi.org/10.1016/S1473-3099(23)00707-7) (hassan2024nipahvirusdisease pages 1-4). A 2024 review reports median mortality of 75% in Bangladesh outbreaks and notes person-to-person airway transmission in Bangladesh and India (Faus-Cotino et al., 2024-01; https://doi.org/10.3390/v16020179) (fauscotino2024nipahvirusa pages 1-3).

---

## 7) Ontology grounding suggestions (non-exhaustive)

### Confirmed / provided
- **Trait:** `METPO:1001105` (biosafety level 4)

### Strong candidates (grounding not fully supported by provided sources; label-only acceptable)
- **BSL-4 determinant nodes:**
  - “high risk of aerosol-transmitted laboratory infection” (label-only)
  - “life-threatening disease” (label-only)
  - “no vaccine or therapy” / “no effective prevention or treatment” (label-only)
- **NiV taxon exemplar:** suggested `NCBITaxon:12110` (NiV) (grounding suggested in artifact; taxon CURIE not explicitly quoted in evidence)
- **Immune process:** interferon signaling (candidate GO term such as `GO:0060337`, but the evidence does not provide a GO CURIE; curate as label-only unless a GO-grounded source is added) (fauscotino2024nipahvirusa pages 1-3)
- **Receptor usage:** ephrin-B2/B3 (candidate grounding: gene/protein identifiers for EFNB2/EFNB3; not provided in evidence) (mehnaz2024thecurrentpathogenicity pages 2-3, anish2024pandemicpotentialof pages 2-3)

---

## 8) Warnings: claims that should not yet be curated (or should be marked uncertain)

1. **Do not treat BSL-4 as an intrinsic microbial physiology trait.** It is a *containment requirement* derived from hazard determinants and regulatory frameworks. Treat it as an ecology/handling trait and explicitly represent the decision context in the graph.

2. **Avoid over-generalizing pathogen-specific molecular mechanisms.** For example, NiV interferon antagonism (V/W/P) and ephrin receptor usage are strong mechanistic determinants for that taxon (fauscotino2024nipahvirusa pages 1-3, mehnaz2024thecurrentpathogenicity pages 2-3) but are not universal causes of BSL-4 designation across all RG4 agents.

3. **Countermeasure absence is context-dependent.** “No vaccine or therapy” can change over time (e.g., after approvals). Curate it as a time-indexed or evidence-scoped node/edge where possible.

4. **Aerosol terminology varies.** One key definition uses “aerosol-transmitted laboratory infections” as a criterion (kaufer2020laboratorybiosafetymeasures pages 4-5), while other definitions emphasize general transmissibility and high hazard (kaufer2020laboratorybiosafetymeasures pages 3-4). If aerosol is required in your trait definition, prioritize sources that explicitly mention aerosol.

---

## DOI-first bibliography (with dates/URLs where available)

1. **Gao W, et al.** *From Biosafety to National Security: The Evolution and Challenges of Biosafety Laboratories.* **Laboratories** (2024-12). DOI: **10.3390/laboratories1030013**. URL: https://doi.org/10.3390/laboratories1030013 (gao2024frombiosafetyto pages 6-7, gao2024frombiosafetyto pages 5-6, gao2024frombiosafetyto media 73d2b0be, gao2024frombiosafetyto pages 12-15)

2. **Resnik DB.** *Biosafety, biosecurity, and bioethics.* **Monash Bioethics Review** (2024-07). DOI: **10.1007/s40592-024-00204-3**. URL: https://doi.org/10.1007/s40592-024-00204-3 (resnik2024biosafetybiosecurityand pages 13-16, resnik2024biosafetybiosecurityand pages 23-25, resnik2024biosafetybiosecurityand pages 1-3)

3. **Hassan MZ, et al.** *Nipah virus disease: what can we do to improve patient care?* **The Lancet Infectious Diseases** (2024-07). DOI: **10.1016/S1473-3099(23)00707-7**. URL: https://doi.org/10.1016/S1473-3099(23)00707-7 (hassan2024nipahvirusdisease pages 1-4)

4. **Faus-Cotino J, Reina G, Pueyo J.** *Nipah Virus: A Multidimensional Update.* **Viruses** (2024-01). DOI: **10.3390/v16020179**. URL: https://doi.org/10.3390/v16020179 (fauscotino2024nipahvirusa pages 1-3, fauscotino2024nipahvirusa pages 5-7)

5. **Saha S, et al.** *Recent Advances of Nipah Virus Disease: Pathobiology to Treatment and Vaccine Advancement.* **Journal of Microbiology** (2024-09). DOI: **10.1007/s12275-024-00168-3**. URL: https://doi.org/10.1007/s12275-024-00168-3 (saha2024recentadvancesof pages 1-2)

6. **Mendonça AO, et al.** *Comparison of Brazilian High- and Maximum-Containment Laboratories…* **Applied Biosafety** (2024-03). DOI: **10.1089/apb.2023.0005**. URL: https://doi.org/10.1089/apb.2023.0005 (mendonca2024comparisonofbrazilian pages 7-8)

7. **Kaufer AM, et al.** *Laboratory biosafety measures involving SARS-CoV-2 and the classification as a Risk Group 3 biological agent.* **Pathology** (2020-12). DOI: **10.1016/j.pathol.2020.09.006**. URL: https://doi.org/10.1016/j.pathol.2020.09.006 (used here specifically for a precise BSL-4 definition including aerosol + no therapy/vaccine, and BSL-3 comparison) (kaufer2020laboratorybiosafetymeasures pages 4-5, kaufer2020laboratorybiosafetymeasures pages 3-4)

8. **Chan XHS, et al.** *Nipah Virus Therapeutics: A Systematic Review to Support Prioritisation for Clinical Trials.* **medRxiv** (2024-03). DOI: **10.1101/2024.03.11.24304091**. URL: https://doi.org/10.1101/2024.03.11.24304091 (preprint) (contextual support for NiV therapeutic landscape; see also NiV CFR statement in abstract) (hassan2024nipahvirusdisease pages 1-4)

9. **Federal Select Agent Program (FSAP).** *2024 Annual Report | Key Statistics* (report date not captured in extracted metadata). (wereUnknownyearfederalselectagenta pages 14-16, wereUnknownyearfederalselectagent pages 14-16)

---

### Curation-ready takeaways for `data/traits/ecology/biosafety_level_4.yaml`
- Core definitional causal drivers: **aerosol-lab infection risk**, **life-threatening disease severity**, and **absence of vaccine/therapy** → **BSL-4 designation** (kaufer2020laboratorybiosafetymeasures pages 4-5, kaufer2020laboratorybiosafetymeasures pages 3-4).
- Implementation edges (BSL-4 → suit/airlock/shower/waste disposal) can be represented as environmental/experimental control nodes (kaufer2020laboratorybiosafetymeasures pages 4-5, gao2024frombiosafetyto media 73d2b0be).
- Use **NiV** as an exemplar to attach mechanistic determinants (IFN antagonism; receptor usage; respiratory/CNS tropism) to hazard nodes, but mark these as taxon-specific (fauscotino2024nipahvirusa pages 1-3, anish2024pandemicpotentialof pages 2-3).

References

1. (kaufer2020laboratorybiosafetymeasures pages 4-5): Alexa M. Kaufer, Torsten Theis, Katherine A. Lau, Joanna L. Gray, and William D. Rawlinson. Laboratory biosafety measures involving sars-cov-2 and the classification as a risk group 3 biological agent. Pathology, 52:790-795, Dec 2020. URL: https://doi.org/10.1016/j.pathol.2020.09.006, doi:10.1016/j.pathol.2020.09.006. This article has 106 citations and is from a peer-reviewed journal.

2. (kaufer2020laboratorybiosafetymeasures pages 3-4): Alexa M. Kaufer, Torsten Theis, Katherine A. Lau, Joanna L. Gray, and William D. Rawlinson. Laboratory biosafety measures involving sars-cov-2 and the classification as a risk group 3 biological agent. Pathology, 52:790-795, Dec 2020. URL: https://doi.org/10.1016/j.pathol.2020.09.006, doi:10.1016/j.pathol.2020.09.006. This article has 106 citations and is from a peer-reviewed journal.

3. (gao2024frombiosafetyto pages 5-6): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

4. (gao2024frombiosafetyto media 73d2b0be): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

5. (gao2024frombiosafetyto pages 6-7): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

6. (gao2024frombiosafetyto pages 3-5): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

7. (fauscotino2024nipahvirusa pages 1-3): Javier Faus-Cotino, Gabriel Reina, and Javier Pueyo. Nipah virus: a multidimensional update. Viruses, 16:179, Jan 2024. URL: https://doi.org/10.3390/v16020179, doi:10.3390/v16020179. This article has 45 citations.

8. (mehnaz2024thecurrentpathogenicity pages 2-3): Samiha Mehnaz, Ramisa Anjum, Fatema Rahman Mithila, Syed Masudur Rahman Dewan, and Md. Rabiul Islam. The current pathogenicity and potential risk assessment of nipah virus as potential cause of “disease x”: a narrative review. Health Science Reports, Dec 2024. URL: https://doi.org/10.1002/hsr2.70241, doi:10.1002/hsr2.70241. This article has 8 citations and is from a peer-reviewed journal.

9. (anish2024pandemicpotentialof pages 2-3): Thekkumkara Surendran Anish, Reghukumar Aravind, Chandni Radhakrishnan, Nivedita Gupta, Pragya D. Yadav, Jerin Jose Cherian, Rima Sahay, Shubin Chenayil, Anoop Kumar A. S., Anitha Puduvail Moorkoth, Ashadevi, Velichapat Ramakrishnan Lathika, Shamsudeen Moideen, Sekhar Lukose Kuriakose, Kalathil Joseph Reena, and Thomas Mathew. Pandemic potential of the nipah virus and public health strategies adopted during outbreaks: lessons from kerala, india. PLOS Global Public Health, 4:e0003926, Dec 2024. URL: https://doi.org/10.1371/journal.pgph.0003926, doi:10.1371/journal.pgph.0003926. This article has 22 citations and is from a peer-reviewed journal.

10. (hassan2024nipahvirusdisease pages 1-4): Md Zakiul Hassan, Tahmina Shirin, Syed M Satter, Mohammed Z Rahman, Josephine Bourner, Ashleigh Cheyne, Els Torreele, Peter Horby, and Piero Olliaro. Nipah virus disease: what can we do to improve patient care? The Lancet Infectious Diseases, 24:e463-e471, Jul 2024. URL: https://doi.org/10.1016/s1473-3099(23)00707-7, doi:10.1016/s1473-3099(23)00707-7. This article has 24 citations and is from a highest quality peer-reviewed journal.

11. (fauscotino2024nipahvirusa pages 5-7): Javier Faus-Cotino, Gabriel Reina, and Javier Pueyo. Nipah virus: a multidimensional update. Viruses, 16:179, Jan 2024. URL: https://doi.org/10.3390/v16020179, doi:10.3390/v16020179. This article has 45 citations.

12. (resnik2024biosafetybiosecurityand pages 13-16): David B. Resnik. Biosafety, biosecurity, and bioethics. Monash Bioethics Review, 42:137-167, Jul 2024. URL: https://doi.org/10.1007/s40592-024-00204-3, doi:10.1007/s40592-024-00204-3. This article has 25 citations and is from a peer-reviewed journal.

13. (resnik2024biosafetybiosecurityand pages 23-25): David B. Resnik. Biosafety, biosecurity, and bioethics. Monash Bioethics Review, 42:137-167, Jul 2024. URL: https://doi.org/10.1007/s40592-024-00204-3, doi:10.1007/s40592-024-00204-3. This article has 25 citations and is from a peer-reviewed journal.

14. (resnik2024biosafetybiosecurityand pages 1-3): David B. Resnik. Biosafety, biosecurity, and bioethics. Monash Bioethics Review, 42:137-167, Jul 2024. URL: https://doi.org/10.1007/s40592-024-00204-3, doi:10.1007/s40592-024-00204-3. This article has 25 citations and is from a peer-reviewed journal.

15. (saha2024recentadvancesof pages 1-2): Sagnik Saha, Manojit Bhattacharya, Sang-Soo Lee, and Chiranjib Chakraborty. Recent advances of nipah virus disease: pathobiology to treatment and vaccine advancement. Journal of microbiology, 62:811-828, Sep 2024. URL: https://doi.org/10.1007/s12275-024-00168-3, doi:10.1007/s12275-024-00168-3. This article has 7 citations and is from a peer-reviewed journal.

16. (mehnaz2024thecurrentpathogenicity pages 1-2): Samiha Mehnaz, Ramisa Anjum, Fatema Rahman Mithila, Syed Masudur Rahman Dewan, and Md. Rabiul Islam. The current pathogenicity and potential risk assessment of nipah virus as potential cause of “disease x”: a narrative review. Health Science Reports, Dec 2024. URL: https://doi.org/10.1002/hsr2.70241, doi:10.1002/hsr2.70241. This article has 8 citations and is from a peer-reviewed journal.

17. (fauscotino2024nipahvirusa pages 7-9): Javier Faus-Cotino, Gabriel Reina, and Javier Pueyo. Nipah virus: a multidimensional update. Viruses, 16:179, Jan 2024. URL: https://doi.org/10.3390/v16020179, doi:10.3390/v16020179. This article has 45 citations.

18. (gao2024frombiosafetyto pages 12-15): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 12 citations.

19. (wereUnknownyearfederalselectagenta pages 14-16): E WERE. Federal select agent program 2024 annual report| key statistics. Unknown journal, Unknown year.

20. (wereUnknownyearfederalselectagent pages 14-16): E WERE. Federal select agent program 2024 annual report| key statistics. Unknown journal, Unknown year.

21. (mendonca2024comparisonofbrazilian pages 7-8): André de Oliveira Mendonça, Kurt Allen Zuelke, Melissa M. Kahl-Mcdonagh, and Claudio Mafra. Comparison of brazilian high- and maximum-containment laboratories biosafety and biosecurity regulations to legal frameworks in the united states and other countries: gaps and opportunities. Applied Biosafety, 29:45-56, Mar 2024. URL: https://doi.org/10.1089/apb.2023.0005, doi:10.1089/apb.2023.0005. This article has 7 citations.