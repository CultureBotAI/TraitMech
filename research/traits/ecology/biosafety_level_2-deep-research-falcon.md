---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T22:47:37.776675'
end_time: '2026-08-03T23:08:35.940705'
duration_seconds: 1258.16
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: biosafety level 2
  trait_identifier: METPO:1001103
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: biosafety_level_2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biosafety level that poses moderate risk and is associated with human
    diseases present in the community.
  parent_traits: METPO:1001101
  synonyms: '2'
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports moderate-virulence community-disease pathogens
    (typically with available vaccines or therapies) as BSL-2 agents.)'
  causal_graph_summary: 'biosafety_level_2_moderate_hazard: 10 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 2
- **METPO identifier:** METPO:1001103
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses moderate risk and is associated with human diseases present in the community.
- **Parent traits:** METPO:1001101
- **Synonyms:** 2
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports moderate-virulence community-disease pathogens (typically with available vaccines or therapies) as BSL-2 agents.)
- **Existing causal graph summary:** biosafety_level_2_moderate_hazard: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **biosafety level 2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_2.yaml`.

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
- **Trait label:** biosafety level 2
- **METPO identifier:** METPO:1001103
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that poses moderate risk and is associated with human diseases present in the community.
- **Parent traits:** METPO:1001101
- **Synonyms:** 2
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports moderate-virulence community-disease pathogens (typically with available vaccines or therapies) as BSL-2 agents.)
- **Existing causal graph summary:** biosafety_level_2_moderate_hazard: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **biosafety level 2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_2.yaml`.

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


# Curation report: biosafety level 2 (METPO:1001103)

## Executive conclusion

**Biosafety level 2 (BSL-2) should not be represented as an intrinsic microbial phenotype.** It is a context-dependent containment assignment produced by an integrated risk assessment of the agent or strain, the procedure and scale, exposure routes, worker susceptibility, and available preventive or therapeutic measures. The most defensible TraitMech model is therefore an **agent–activity–host–control causal graph**, with `METPO:1001103` as the risk-management outcome rather than as a direct consequence of one gene or pathway.

BSL-2 covers work with moderate-hazard agents associated with human disease and occupational exposure through ingestion, inoculation, mucous-membrane/skin contact, or inhalation. Relative to BSL-1, it adds restricted access, agent-specific training, PPE and primary containment—especially a biological safety cabinet (BSC) for aerosol- or splash-generating work. BSL-3 is the nearby higher boundary for work whose inhalation route and potential for serious or lethal disease demand enhanced containment. Risk group and containment level are related but not interchangeable; no taxonomic label or virulence determinant alone is sufficient to assign BSL-2. (ta2018biosafetyandbiohazards pages 3-6, kimman2008evidencebasedbiosafetya pages 18-19, kimman2008evidencebasedbiosafetya pages 7-8)

## 1. Scope and boundary cases

### What the trait represents

For curation, define the trait as:

> **A laboratory containment/risk-management class appropriate to an agent–procedure combination presenting moderate individual and environmental hazard, commonly involving agents associated with human disease in the community, where standard microbiological practices plus restricted access, PPE, decontamination and primary containment can control anticipated exposures.**

This preserves the supplied METPO definition while making explicit that the observable property is an **assigned containment level**, not a physiological capacity or environmental preference.

### Boundaries

- **Versus BSL-1:** BSL-2 adds restricted access, specific training and physical containment for aerosol/splash procedures. BSL-1 organisms are generally not known consistently to cause disease in immunocompetent adults. (ta2018biosafetyandbiohazards pages 3-6)
- **Versus BSL-3:** BSL-3 addresses agents or procedures with greater inhalational risk and serious or potentially lethal disease, normally requiring all viable-agent manipulations in a BSC and additional engineering controls. (robilotti2023biosafetyandbiohazard pages 3-4)
- **Versus Risk Group 2:** risk group describes inherent agent hazard; BSL describes the controls selected for a particular activity. Strain attenuation, concentration, volume, aerosol generation, animal work or genetic modification can shift the containment required.
- **Clinical specimens:** unknown patient specimens are frequently processed under BSL-2 practices even though the eventual agent may require referral or escalation. Thus, “handled in a BSL-2 clinical laboratory” is not evidence that the recovered organism is intrinsically a BSL-2 organism. Clinical laboratories also face equipment- and workflow-specific aerosol hazards not captured by research-laboratory guidance. (cornish2021clinicallaboratorybiosafety pages 16-18)
- **Attenuated or engineered derivatives:** an attenuated derivative may warrant lower controls than its wild type, while restoration of replication competence, expanded host range, toxin expression or an antibiotic-resistance marker can increase risk. A 2016 BSL-2 incident involving an inadvertently infectious recombinant HIV-1 pseudovirus illustrates why construct-level assessment is essential. (zuo2024ahistoricalstudy pages 8-10)
- **Quantity and procedure:** containment can differ between small-dose clinical administration and bulk preparation. T-VEC, for example, may be administered as a single-dose injection using BSL-1 practices and universal precautions, while blanket BSL-2 rules are often imposed by treatment centers. (robilotti2023biosafetyandbiohazard pages 3-4)

## 2. Candidate nodes grouped by type

### Trait and assessment nodes

- **biosafety level 2** — `METPO:1001103`
- moderate laboratory biological hazard — label-only candidate
- laboratory biosafety risk assessment — label-only candidate
- probability of exposure — label-only candidate
- consequence of exposure — label-only candidate
- laboratory-acquired infection — label-only candidate
- community-associated human disease — label-only candidate

### Agent and host properties

- virulence / disease severity — label-only candidate
- infectivity and infectious dose — label-only candidate
- transmission route
- host range
- host susceptibility / immunocompromised state
- environmental persistence
- replication competence
- viable pathogen burden or concentration
- culture volume / scale
- availability of effective vaccine
- antimicrobial or antiviral susceptibility
- antimicrobial resistance

Classification frameworks evaluate virulence, mode of transmission and host range, preventive measures and treatment together; variation among strains can alter containment needs. (kimman2008evidencebasedbiosafetya pages 7-8)

### Experimental and environmental factors

- aerosol-generating manipulation
- centrifugation
- pipetting, vortexing, blending, grinding, sonicating or opening infectious containers
- sharps use / percutaneous inoculation
- splash generation
- ingestion exposure
- skin or mucous-membrane exposure
- inhalation exposure
- high-titer culture
- large-volume handling
- animal inoculation
- fecal or dermal shedding
- environmental release

Routine operations including centrifugation, vortexing and pouring can generate aerosols containing viable bacteria or viruses. (cornish2021clinicallaboratorybiosafety pages 16-18)

### Containment and intervention nodes

- Class II biological safety cabinet
- sealed centrifuge cup or rotor
- laboratory coat or gown
- gloves
- eye/face protection
- hand hygiene
- access restriction
- worker training and competency
- vaccination
- disinfection / validated inactivation
- autoclaving
- leakproof transport container
- exposure-response procedure

BSL-2 guidance associates these controls with moderate-hazard work, particularly requiring BSCs for procedures likely to produce infectious aerosols or splashes. (ta2018biosafetyandbiohazards pages 3-6)

### Genetic and molecular nodes

**General candidates**

- attenuating mutation
- virulence factor
- toxin or secreted effector
- secretion system
- adhesin
- biofilm formation
- immune evasion
- auxotrophy / replication restriction
- antibiotic-resistance determinant
- mobile genetic element
- horizontal gene transfer
- nonconjugative plasmid
- chromosomal transgene integration

**Taxon-specific exemplars**

- *Pseudomonas aeruginosa* type III secretion system — candidate grounding: `GO:0030254` (protein secretion by the type III secretion system), subject to ontology-version verification
- ExoU phospholipase effector — use reviewed UniProt accession only after strain-level resolution
- ExoS, ExoT and ExoY effectors — strain-specific UniProt grounding required
- HSV-1 ICP34.5 neurovirulence factor — use virus/strain-specific protein accession after construct resolution
- HSV-1 ICP47
- T-VEC ICP34.5/ICP47 deletions
- *Lactococcus lactis* `thyA` replacement/auxotrophy
- engineered *Salmonella* auxotrophic mutations and hypoxia-controlled replication

## 3. Candidate causal edges

The table below gives the strongest graph core.

| Subject | Predicate | Object | Scope/confidence | Key evidence |
|---|---|---|---|---|
| Aerosol-generating manipulation | increases | inhalation exposure | Direct, high | Aerosol/splash-generating procedures include “pipetting, centrifuging, grinding, blending, shaking, sonicating, or opening containers of infectious materials,” creating BSL-2 occupational risk via inhalation; historical LAI analyses also link centrifugation and aerosols to infection (ta2018biosafetyandbiohazards pages 3-6, zuo2024ahistoricalstudy pages 8-10) |
| Biological safety cabinet use | decreases | aerosol/splash exposure | Direct, high | BSL-2 guidance requires BSC use for procedures that may create infectious aerosols or splashes; containment studies found closed BSCs prevented microorganism escape and higher airflow reduced escape (ta2018biosafetyandbiohazards pages 3-6, kimman2008evidencebasedbiosafetya pages 12-13) |
| Personal protective equipment | decreases | skin/mucous membrane contact exposure | Direct, high | BSL-2 adds protective lab coats/gowns and gloves; exposure-minimization principles explicitly include gloves and masks to reduce contact and droplet/aerosol exposure (ta2018biosafetyandbiohazards pages 3-6, kimman2008evidencebasedbiosafetya pages 4-5) |
| Decontamination/inactivation | decreases | viable pathogen burden | Direct, high | BSL-2 requires decontamination protocols; evidence-based biosafety reviews describe validated BSC decontamination and formaldehyde inactivation, supporting reduction of viable organisms (ta2018biosafetyandbiohazards pages 3-6, kimman2008evidencebasedbiosafetya pages 12-13) |
| Attenuating mutation | decreases | virulence / replication competence | Direct, high | Risk assessment for gene-modified bacteria must consider “attenuating mutations affecting virulence, replication competency”; biosafety principles also favor highly attenuated variants where available (gulig2024areviewof pages 1-2, kimman2008evidencebasedbiosafetya pages 18-19) |
| Antimicrobial resistance | increases | consequence of infection by limiting treatment options | Contextual, high | Classification considers availability of treatment; examples include extremely drug-resistant *M. tuberculosis* needing higher risk categorization, and recent risk-assessment reviews emphasize antibiotic susceptibility as a key determinant of consequence (kimman2008evidencebasedbiosafetya pages 7-8, gulig2024areviewof pages 1-2) |
| *Pseudomonas aeruginosa* V1 virulotype (exoU+/exoS−/exoT+/exoY+) | increases | severe outcome / mortality | Taxon-specific, high | In 336 pediatric isolates, V1 had “almost four-fold greater” death risk than V3; ExoU is a potent phospholipase linked to acute tissue damage and early mortality (nolascoromero2024theexosexot pages 1-2, nolascoromero2024theexosexot pages 2-3) |
| HSV-1 ICP34.5 deletion | decreases | replication in normal tissue | Taxon-specific, high | Genetically modified HSV-1 oncolytic viruses with ICP34.5 alterations “prevent effective replication in normal tissue,” supporting attenuation relative to wild type (robilotti2023biosafetyandbiohazard pages 3-4) |
| Replication competence / environmental persistence | increases | biosafety risk | Direct, high | Recent clinical-trial biosafety review states risk assessment for bacterial/phage products must give greater consideration to “replication competency… and persistence in the environment” (gulig2024areviewof pages 1-2) |
| Integrated risk assessment | determines | BSL-2 containment assignment | Contextual, very high | Modern biosafety sources emphasize BSL assignment is not caused by any single microbial feature; it depends on combined factors such as virulence, transmission, infectious dose, host susceptibility, procedures, and available vaccines/treatments, and “referring only to risk groups is not” sufficient (kimman2008evidencebasedbiosafetya pages 18-19, kimman2008evidencebasedbiosafetya pages 7-8, zuo2024ahistoricalstudy pages 1-2) |


*Table: This table compiles the strongest, most curation-ready causal edges relevant to a BSL-2 TraitMech graph. It prioritizes direct evidence for exposure pathways and controls, while clearly flagging contextual versus taxon-specific mechanistic claims.*

Additional curation-ready or conditionally ready triples follow.

| Subject | Predicate | Object | Supporting snippet | Reference | Curation note |
|---|---|---|---|---|---|
| Infectious aerosol generation | increases | inhalation exposure probability | Procedures such as centrifugation, vortexing and pouring generate aerosols containing live microorganisms. | Cornish et al., 2021, DOI 10.1128/CMR.00126-18 (cornish2021clinicallaboratorybiosafety pages 16-18) | **Strong, general.** Do not assert that aerosol generation by itself determines BSL-2. |
| Class II BSC use | decreases | escape of infectious aerosols | Closed BSCs with adequate airflow prevented microorganism escape; escape declined as airflow increased. | Kimman et al., 2008, DOI 10.1128/CMR.00014-08 (kimman2008evidencebasedbiosafetya pages 12-13) | **Strong control edge.** Effect depends on correct cabinet type, certification and technique. |
| PPE use | decreases | operator contamination/contact exposure | Double gloving substantially reduced, but did not eliminate, contamination. | Cornish et al., 2021, DOI 10.1128/CMR.00126-18 (cornish2021clinicallaboratorybiosafety pages 16-18) | **Strong but not absolute.** Model as `decreases`, not `prevents`. |
| Validated decontamination | decreases | viable pathogen burden | BSC decontamination and formaldehyde-based inactivation were evaluated using biological validation approaches. | Kimman et al., 2008, DOI 10.1128/CMR.00014-08 (kimman2008evidencebasedbiosafetya pages 12-13) | **General edge; protocol-specific efficacy.** Matrix, concentration and contact time should be separate context nodes if available. |
| Effective vaccination | decreases | consequence of occupational exposure | Vaccination is described as a measure reducing exposure consequences and one factor in risk classification. | Kimman et al., 2008, DOI 10.1128/CMR.00014-08 (kimman2008evidencebasedbiosafetya pages 4-5, kimman2008evidencebasedbiosafetya pages 7-8) | **Contextual.** Vaccine availability does not automatically imply BSL-2. |
| Antimicrobial resistance | decreases | effective treatment availability | Antibiotic susceptibility is a key risk-assessment attribute; highly resistant organisms can warrant higher categorization. | Kimman et al., 2008; Gulig et al., 2024 (kimman2008evidencebasedbiosafetya pages 7-8, gulig2024areviewof pages 1-2) | **Strong conceptual edge.** Consequence depends on disease, drug and resistance phenotype. |
| Attenuating mutation | decreases | virulence and/or replication competence | Current assessment of engineered microbes requires analysis of “attenuating mutations affecting virulence [and] replication competency.” | Gulig et al., 2024, DOI 10.1089/apb.2024.0002 (gulig2024areviewof pages 1-2) | **Strong general relationship, construct-specific direction must be demonstrated experimentally.** |
| Replication competence | increases | potential exposure duration and shedding | Risk assessment of microbial investigational products gives special consideration to replication competence and environmental persistence. | Gulig et al., 2024 (gulig2024areviewof pages 1-2) | **Contextual/inferred causal chain.** Prefer `contributes_to risk` unless quantitative evidence exists. |
| Horizontal gene transfer | increases | dissemination of resistance or virulence determinants | Transformation and phage-mediated transduction can spread DNA; nonconjugative plasmids and chromosomal integration reduce unintended transfer concerns. | Gulig et al., 2024 (gulig2024areviewof pages 8-10) | **Conditional.** Do not curate without a mobile element, recipient and demonstrated or plausible transfer route. |
| HSV-1 ICP34.5 deletion | decreases | replication in normal tissue | ICP34.5-altered oncolytic HSV-1 products “prevent effective replication in normal tissue.” | Robilotti et al., 2023, DOI 10.3389/fmolb.2023.1178382 (robilotti2023biosafetyandbiohazard pages 3-4) | **Strong but construct/taxon-specific.** Not a universal BSL-2 mechanism. |
| *P. aeruginosa* T3SS | injects | ExoS/ExoT/ExoU/ExoY into host cells | T3SS “presents the ability to inject four effectors into the host cell.” | Nolasco-Romero et al., 2024, DOI 10.3390/pathogens13121030 (nolascoromero2024theexosexot pages 1-2) | **Strong taxon-specific mechanistic edge.** |
| ExoU | damages | host-cell plasma membrane | ExoU is a potent phospholipase that induces rapid destruction of host-cell plasma membranes. | Nolasco-Romero et al., 2024 (nolascoromero2024theexosexot pages 2-3) | **Strong taxon-specific edge.** Ground to strain-specific protein accession before YAML insertion. |
| V1 virulotype (exoU+/exoS−/exoT+/exoY+) | increases | pediatric mortality risk relative to V3 | V1 had nearly fourfold higher death risk than V3; RR 3.690, 95% CI 1.259–10.82. | Nolasco-Romero et al., 2024 (nolascoromero2024theexosexot pages 6-8, nolascoromero2024theexosexot pages 1-2) | **Clinical association, not proof of direct causality. Mark `associated_with` or uncertain.** |
| Integrated agent–procedure risk assessment | determines | containment selection | Risk assessment considers transmission, infectivity, virulence, strain, procedure and consequences rather than a single feature. | Kimman et al., 2008; Zuo et al., 2024 (kimman2008evidencebasedbiosafetya pages 18-19, zuo2024ahistoricalstudy pages 1-2) | **Highest-level graph edge.** This should be the immediate parent of BSL-2 assignment. |

## 4. Recent research, implementations and quantitative evidence

### Risk-based rather than list-based governance

Recent expert analysis favors case-by-case assessment over assigning controls solely from taxonomic lists. This is especially important for engineered strains, where attenuation, replication competence, antibiotic susceptibility, shedding and persistence may differ sharply from the parental organism. (robilotti2023biosafetyandbiohazard pages 9-10, gulig2024areviewof pages 1-2)

### Engineered microbial therapeutics

Gulig et al. reported rapidly growing clinical use of genetically modified bacteria and phages and argued that institutional biosafety committees must assess attenuating mutations, replication competence, antibiotic susceptibility and environmental persistence. Applications include engineered *L. lactis* delivering IL-10, trefoil factor or proinsulin; *Bifidobacterium longum* delivering cytosine deaminase or IL-12; and replication-controlled *Salmonella* constructs for tumor targeting. Poor intestinal colonization, auxotrophy, chromosomal integration and avoidance of transferable antibiotic markers are practical risk-reduction strategies. (gulig2024areviewof pages 13-15, gulig2024areviewof pages 8-10, gulig2024areviewof pages 1-2)

The same review notes FDA approval of a fecal microbiota transplant product in 2022 and the first orally administered fecal-microbiota capsule in April 2023; as of 2020, five deaths had been associated with fecal microbiota transplants. These examples show why viable microbial therapeutics require product-specific screening and biosafety assessment. (gulig2024areviewof pages 1-2)

### Oncolytic HSV-1 in real-world care

T-VEC provides a strong boundary case. It contains deletions in `ICP34.5` and `ICP47`; ICP34.5 alteration restricts effective replication in normal tissue. Single-dose administration—1 mL vials, up to 4 mL administered—can use BSL-1 practices with universal precautions, yet blanket BSL-2 policies are often applied and can limit facility and staff availability. Robilotti and colleagues found no evidence of spread to healthcare workers or other patients during or after administration and recommended agent-specific reassessment rather than automatic inheritance of wild-type-virus controls. (robilotti2023biosafetyandbiohazard pages 9-10, robilotti2023biosafetyandbiohazard pages 3-4)

### Virulome-informed hazard characterization

In a November 2024 pediatric study, 336 *P. aeruginosa* isolates—55 from cystic-fibrosis samples and 281 from bloodstream infections—were grouped into 11 T3SS virulotypes. V3 represented 64.28%, V1 and V2 each 11.60%, and 15 of 100 patients died. V1, containing `exoU`, had approximately fourfold greater relative risk of death than V3 and was associated with pandrug resistance. This demonstrates how virulome and resistance data can refine **consequence assessment**, but it does not establish a direct mapping from an `exo` genotype to BSL-2. (nolascoromero2024theexosexot pages 1-2)

### Laboratory-acquired infection burden

A 2024 historical synthesis reports more than 4,000 LAIs documented from 1949–1974, with 4.1% mortality, and cites a 2018 estimate of approximately 1–5 LAIs per 1,000 U.S. laboratory employees annually. These values are historical or modeled and reporting is incomplete, so they should not be interpreted as a current BSL-2-specific incidence rate. The same review records 16 of 23 reported LAIs in 1915 as attributable to mouth pipetting, illustrating the strong influence of procedure on risk. (zuo2024ahistoricalstudy pages 1-2)

## 5. Recommended causal-graph architecture

A compact graph suitable for `biosafety_level_2.yaml` would use this structure:

1. **Agent/strain determinants**—infectivity, virulence, infectious dose, host range, replication competence, resistance and persistence.
2. **Activity determinants**—volume, concentration, aerosol generation, sharps, centrifugation and animal work.
3. **Host determinants**—immunity, pregnancy, vaccination and comorbidity.
4. **Exposure pathways**—inhalation, ingestion, percutaneous and mucocutaneous exposure.
5. **Controls**—BSC, sealed rotor, PPE, training, restricted access, disinfection and vaccination.
6. **Intermediate outcomes**—exposure probability and exposure consequence.
7. **Assessment node**—integrated laboratory biosafety risk assessment.
8. **Outcome**—BSL-2 containment assignment (`METPO:1001103`).

Recommended immediate causal chain:

`agent hazard + activity hazard + host susceptibility − effective controls → residual exposure risk → integrated risk assessment → BSL-2 assignment`

This architecture avoids the false implication that a virulence gene “causes BSL-2.”

## 6. Ontology-grounding recommendations

- Retain **`METPO:1001103`** for the target trait and the supplied parent **`METPO:1001101`**.
- Use **NCBITaxon** identifiers only after species/strain resolution; containment can differ among strains.
- Use **UniProt** accessions only for the exact strain or engineered construct. Do not assign one generic accession to ExoU, ExoS or viral ICP proteins across strains.
- Candidate GO grounding for type III secretion is **`GO:0030254`**, but verify against the ontology release used by TraitMech.
- Use **CHEBI** identifiers for disinfectants, antibiotics or metabolites only when the chemical identity is explicit in the evidence.
- BSC, PPE, restricted access, containment level, culture volume and risk assessment are better represented by OBI/ENVO or label-only nodes after checking the project’s accepted ontologies.
- Keep “moderate hazard,” “residual exposure risk,” “availability of treatment,” “environmental persistence” and “replication competence” label-only if no reviewed project-compatible CURIE is confirmed.

## 7. Warnings: claims not yet suitable for direct curation

1. **Do not curate `virulence factor → BSL-2`.** Virulence affects consequence, but containment follows integrated assessment.
2. **Do not treat BSL-2 as a taxonomic property.** A species name is insufficient without strain, construct, activity and jurisdiction.
3. **Do not equate Risk Group 2 with BSL-2.** Risk group informs, but does not determine, the operational containment level.
4. **Do not generalize taxon-specific mechanisms.** ExoU, ICP34.5 deletion, `thyA` auxotrophy and particular engineered constructs should remain in organism-specific subgraphs.
5. **Treat V1–mortality as association.** The *P. aeruginosa* study supports prognostic association, not isolation of V1 as the sole causal determinant. (nolascoromero2024theexosexot pages 6-8)
6. **Do not curate resistance as necessarily increasing infectivity or virulence.** Its strongest general edge is reduced treatment availability/increased consequence.
7. **Do not claim PPE or BSCs eliminate risk.** Their supported direction is risk reduction; effectiveness depends on selection, maintenance and technique. (cornish2021clinicallaboratorybiosafety pages 16-18, kimman2008evidencebasedbiosafetya pages 12-13)
8. **Do not use historical LAI statistics as present-day BSL-2 incidence.** Reporting is incomplete and the cited totals span multiple containment contexts. (zuo2024ahistoricalstudy pages 1-2)
9. **Do not infer pathway nodes merely because an organism is BSL-2.** No universal metabolic pathway, electron donor/acceptor, nutrient or organelle defines this containment category.
10. **Verify regulatory status locally.** BSL assignments can differ by jurisdiction, institutional review, volume and procedure.

## DOI-first bibliography

1. Zuo K, Wu Z, Zhao C, Liu H. **A Historical Study on the Scientific Attribution of Biosafety Risk Assessment in Real Cases of Laboratory-Acquired Infections.** *Laboratories*. Published June 30, 2024. DOI: [10.3390/laboratories1020007](https://doi.org/10.3390/laboratories1020007). (zuo2024ahistoricalstudy pages 1-2)
2. Gulig P, Swindle S, Fields M, Eisenman D. **A Review of Clinical Trials Involving Genetically Modified Bacteria, Bacteriophages and Their Associated Risk Assessments.** *Applied Biosafety*. Published December 2024. DOI: [10.1089/apb.2024.0002](https://doi.org/10.1089/apb.2024.0002). (gulig2024areviewof pages 1-2)
3. Nolasco-Romero CG, et al. **The exoS, exoT, exoU and exoY Virulotypes of the Type 3 Secretion System in Multidrug Resistant Pseudomonas aeruginosa as a Death Risk Factor in Pediatric Patients.** *Pathogens*. Published November 22, 2024. DOI: [10.3390/pathogens13121030](https://doi.org/10.3390/pathogens13121030). (nolascoromero2024theexosexot pages 1-2)
4. Gao W, et al. **From Biosafety to National Security: The Evolution and Challenges of Biosafety Laboratories.** *Laboratories*. Published December 2024. DOI: [10.3390/laboratories1030013](https://doi.org/10.3390/laboratories1030013). Historical evidence on aerosols, BSCs and laboratory barriers is summarized in the retrieved text. (gao2024frombiosafetyto pages 2-3)
5. Robilotti E, Zeitouni NC, Orloff M. **Biosafety and Biohazard Considerations of HSV-1–Based Oncolytic Viral Immunotherapy.** *Frontiers in Molecular Biosciences*. Published September 2023. DOI: [10.3389/fmolb.2023.1178382](https://doi.org/10.3389/fmolb.2023.1178382). (robilotti2023biosafetyandbiohazard pages 3-4)
6. Zuo K, Wu Z, Zhao C, Liu H. **Risk and Countermeasure of Laboratory-Acquired Infection Based on Pathogen Transmission Routes.** *Biosafety and Health*. Published June 2023. DOI: [10.1016/j.bsheal.2023.04.006](https://doi.org/10.1016/j.bsheal.2023.04.006).
7. Cornish NE, et al. **Clinical Laboratory Biosafety Gaps: Lessons Learned from Past Outbreaks Reveal a Path to a Safer Future.** *Clinical Microbiology Reviews*. Published June 2021. DOI: [10.1128/CMR.00126-18](https://doi.org/10.1128/CMR.00126-18). (cornish2021clinicallaboratorybiosafety pages 16-18)
8. Kimman TG, Smit E, Klein MR. **Evidence-Based Biosafety: A Review of the Principles and Effectiveness of Microbiological Containment Measures.** *Clinical Microbiology Reviews*. Published July 2008. DOI: [10.1128/CMR.00014-08](https://doi.org/10.1128/CMR.00014-08). This foundational source is especially relevant because it is the supplied existing evidence. (kimman2008evidencebasedbiosafetya pages 18-19, kimman2008evidencebasedbiosafetya pages 4-5, kimman2008evidencebasedbiosafetya pages 12-13, kimman2008evidencebasedbiosafetya pages 7-8)
9. Ta L, Gosa L, Nathanson DA. **Biosafety and Biohazards: Understanding Biosafety Levels and Meeting Safety Requirements of a Biobank.** Published December 2018. DOI: [10.1007/978-1-4939-8935-5_19](https://doi.org/10.1007/978-1-4939-8935-5_19). (ta2018biosafetyandbiohazards pages 3-6)

References

1. (ta2018biosafetyandbiohazards pages 3-6): Lisa Ta, Laura Gosa, and David A. Nathanson. Biosafety and biohazards: understanding biosafety levels and meeting safety requirements of a biobank. Biobanking, 1897:213-225, Dec 2018. URL: https://doi.org/10.1007/978-1-4939-8935-5\_19, doi:10.1007/978-1-4939-8935-5\_19. This article has 71 citations.

2. (kimman2008evidencebasedbiosafetya pages 18-19): Tjeerd G. Kimman, Eric Smit, and Michèl R. Klein. Evidence-based biosafety: a review of the principles and effectiveness of microbiological containment measures. Clinical Microbiology Reviews, 21:403-425, Jul 2008. URL: https://doi.org/10.1128/cmr.00014-08, doi:10.1128/cmr.00014-08. This article has 209 citations and is from a highest quality peer-reviewed journal.

3. (kimman2008evidencebasedbiosafetya pages 7-8): Tjeerd G. Kimman, Eric Smit, and Michèl R. Klein. Evidence-based biosafety: a review of the principles and effectiveness of microbiological containment measures. Clinical Microbiology Reviews, 21:403-425, Jul 2008. URL: https://doi.org/10.1128/cmr.00014-08, doi:10.1128/cmr.00014-08. This article has 209 citations and is from a highest quality peer-reviewed journal.

4. (robilotti2023biosafetyandbiohazard pages 3-4): Elizabeth Robilotti, Nathalie C. Zeitouni, and Marlana Orloff. Biosafety and biohazard considerations of hsv-1–based oncolytic viral immunotherapy. Frontiers in Molecular Biosciences, Sep 2023. URL: https://doi.org/10.3389/fmolb.2023.1178382, doi:10.3389/fmolb.2023.1178382. This article has 10 citations.

5. (cornish2021clinicallaboratorybiosafety pages 16-18): Nancy E. Cornish, Nancy L. Anderson, Diego G. Arambula, Matthew J. Arduino, Andrew Bryan, Nancy C. Burton, Bin Chen, Beverly A. Dickson, Judith G. Giri, Natasha K. Griffith, Michael A. Pentella, Reynolds M. Salerno, Paramjit Sandhu, James W. Snyder, Christopher A. Tormey, Elizabeth A. Wagar, Elizabeth G. Weirich, and Sheldon Campbell. Clinical laboratory biosafety gaps: lessons learned from past outbreaks reveal a path to a safer future. Jun 2021. URL: https://doi.org/10.1128/cmr.00126-18, doi:10.1128/cmr.00126-18. This article has 109 citations and is from a highest quality peer-reviewed journal.

6. (zuo2024ahistoricalstudy pages 8-10): Kunlan Zuo, Zongzhen Wu, Chihong Zhao, and Huan Liu. A historical study on the scientific attribution of biosafety risk assessment in real cases of laboratory-acquired infections. Laboratories, 1:87-102, Jun 2024. URL: https://doi.org/10.3390/laboratories1020007, doi:10.3390/laboratories1020007. This article has 3 citations.

7. (kimman2008evidencebasedbiosafetya pages 12-13): Tjeerd G. Kimman, Eric Smit, and Michèl R. Klein. Evidence-based biosafety: a review of the principles and effectiveness of microbiological containment measures. Clinical Microbiology Reviews, 21:403-425, Jul 2008. URL: https://doi.org/10.1128/cmr.00014-08, doi:10.1128/cmr.00014-08. This article has 209 citations and is from a highest quality peer-reviewed journal.

8. (kimman2008evidencebasedbiosafetya pages 4-5): Tjeerd G. Kimman, Eric Smit, and Michèl R. Klein. Evidence-based biosafety: a review of the principles and effectiveness of microbiological containment measures. Clinical Microbiology Reviews, 21:403-425, Jul 2008. URL: https://doi.org/10.1128/cmr.00014-08, doi:10.1128/cmr.00014-08. This article has 209 citations and is from a highest quality peer-reviewed journal.

9. (gulig2024areviewof pages 1-2): Paul Gulig, Scott Swindle, Mark Fields, and Daniel Eisenman. A review of clinical trials involving genetically modified bacteria, bacteriophages and their associated risk assessments. Dec 2024. URL: https://doi.org/10.1089/apb.2024.0002, doi:10.1089/apb.2024.0002. This article has 13 citations.

10. (nolascoromero2024theexosexot pages 1-2): Carolina G. Nolasco-Romero, Francisco-Javier Prado-Galbarro, Rodolfo Norberto Jimenez-Juarez, Uriel Gomez-Ramirez, Juan Carlos Cancino-Díaz, Beatriz López-Marceliano, Magali Reyes Apodaca, Mónica Anahí Aguayo-Romero, Gerardo E. Rodea, Lilia Pichardo-Villalon, Israel Parra-Ortega, Fortino Solórzano Santos, Mónica Moreno-Galván, and Norma Velázquez-Guadarrama. The exos, exot, exou and exoy virulotypes of the type 3 secretion system in multidrug resistant pseudomonas aeruginosa as a death risk factor in pediatric patients. Pathogens, 13:1030, Nov 2024. URL: https://doi.org/10.3390/pathogens13121030, doi:10.3390/pathogens13121030. This article has 15 citations.

11. (nolascoromero2024theexosexot pages 2-3): Carolina G. Nolasco-Romero, Francisco-Javier Prado-Galbarro, Rodolfo Norberto Jimenez-Juarez, Uriel Gomez-Ramirez, Juan Carlos Cancino-Díaz, Beatriz López-Marceliano, Magali Reyes Apodaca, Mónica Anahí Aguayo-Romero, Gerardo E. Rodea, Lilia Pichardo-Villalon, Israel Parra-Ortega, Fortino Solórzano Santos, Mónica Moreno-Galván, and Norma Velázquez-Guadarrama. The exos, exot, exou and exoy virulotypes of the type 3 secretion system in multidrug resistant pseudomonas aeruginosa as a death risk factor in pediatric patients. Pathogens, 13:1030, Nov 2024. URL: https://doi.org/10.3390/pathogens13121030, doi:10.3390/pathogens13121030. This article has 15 citations.

12. (zuo2024ahistoricalstudy pages 1-2): Kunlan Zuo, Zongzhen Wu, Chihong Zhao, and Huan Liu. A historical study on the scientific attribution of biosafety risk assessment in real cases of laboratory-acquired infections. Laboratories, 1:87-102, Jun 2024. URL: https://doi.org/10.3390/laboratories1020007, doi:10.3390/laboratories1020007. This article has 3 citations.

13. (gulig2024areviewof pages 8-10): Paul Gulig, Scott Swindle, Mark Fields, and Daniel Eisenman. A review of clinical trials involving genetically modified bacteria, bacteriophages and their associated risk assessments. Dec 2024. URL: https://doi.org/10.1089/apb.2024.0002, doi:10.1089/apb.2024.0002. This article has 13 citations.

14. (nolascoromero2024theexosexot pages 6-8): Carolina G. Nolasco-Romero, Francisco-Javier Prado-Galbarro, Rodolfo Norberto Jimenez-Juarez, Uriel Gomez-Ramirez, Juan Carlos Cancino-Díaz, Beatriz López-Marceliano, Magali Reyes Apodaca, Mónica Anahí Aguayo-Romero, Gerardo E. Rodea, Lilia Pichardo-Villalon, Israel Parra-Ortega, Fortino Solórzano Santos, Mónica Moreno-Galván, and Norma Velázquez-Guadarrama. The exos, exot, exou and exoy virulotypes of the type 3 secretion system in multidrug resistant pseudomonas aeruginosa as a death risk factor in pediatric patients. Pathogens, 13:1030, Nov 2024. URL: https://doi.org/10.3390/pathogens13121030, doi:10.3390/pathogens13121030. This article has 15 citations.

15. (robilotti2023biosafetyandbiohazard pages 9-10): Elizabeth Robilotti, Nathalie C. Zeitouni, and Marlana Orloff. Biosafety and biohazard considerations of hsv-1–based oncolytic viral immunotherapy. Frontiers in Molecular Biosciences, Sep 2023. URL: https://doi.org/10.3389/fmolb.2023.1178382, doi:10.3389/fmolb.2023.1178382. This article has 10 citations.

16. (gulig2024areviewof pages 13-15): Paul Gulig, Scott Swindle, Mark Fields, and Daniel Eisenman. A review of clinical trials involving genetically modified bacteria, bacteriophages and their associated risk assessments. Dec 2024. URL: https://doi.org/10.1089/apb.2024.0002, doi:10.1089/apb.2024.0002. This article has 13 citations.

17. (gao2024frombiosafetyto pages 2-3): Wanying Gao, Zongzhen Wu, Kunlan Zuo, Qiangyu Xiang, Lu Zhang, Xiaoya Chen, Feng Tan, and Huan Liu. From biosafety to national security: the evolution and challenges of biosafety laboratories. Laboratories, 1:158-173, Dec 2024. URL: https://doi.org/10.3390/laboratories1030013, doi:10.3390/laboratories1030013. This article has 11 citations.