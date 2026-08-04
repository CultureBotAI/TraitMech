---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T22:54:42.974494'
end_time: '2026-08-03T23:06:10.187011'
duration_seconds: 687.21
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: biosafety level 3
  trait_identifier: METPO:1001104
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: biosafety_level_3
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biosafety level that can cause serious or potentially lethal disease
    through inhalation or other routes, requiring specialized containment facilities
    with controlled access, directional airflow, and strict safety protocols.
  parent_traits: METPO:1001101
  synonyms: 3, 3**
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162938: virulence factors
    (Virulence-factor review supports highly virulent aerosol-transmissible pathogens
    (serious or potentially lethal disease) as BSL-3 agents.)'
  causal_graph_summary: 'biosafety_level_3_serious_hazard: 10 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biosafety level 3
- **METPO identifier:** METPO:1001104
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that can cause serious or potentially lethal disease through inhalation or other routes, requiring specialized containment facilities with controlled access, directional airflow, and strict safety protocols.
- **Parent traits:** METPO:1001101
- **Synonyms:** 3, 3**
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports highly virulent aerosol-transmissible pathogens (serious or potentially lethal disease) as BSL-3 agents.)
- **Existing causal graph summary:** biosafety_level_3_serious_hazard: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **biosafety level 3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_3.yaml`.

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
- **Trait label:** biosafety level 3
- **METPO identifier:** METPO:1001104
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biosafety level that can cause serious or potentially lethal disease through inhalation or other routes, requiring specialized containment facilities with controlled access, directional airflow, and strict safety protocols.
- **Parent traits:** METPO:1001101
- **Synonyms:** 3, 3**
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162938: virulence factors (Virulence-factor review supports highly virulent aerosol-transmissible pathogens (serious or potentially lethal disease) as BSL-3 agents.)
- **Existing causal graph summary:** biosafety_level_3_serious_hazard: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **biosafety level 3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biosafety_level_3.yaml`.

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


# Curation-focused research report: biosafety level 3

## Executive curation recommendation

**Target:** biosafety level 3 (BSL-3), **METPO:1001104**, category ECOLOGY, term kind CLASS.

BSL-3 should be modeled as a **context-dependent containment/risk-management classification**, not as an intrinsic microbial phenotype. The most defensible graph has three layers:

1. **Agent hazard:** inhalational transmissibility, serious disease, low infectious dose, environmental stability, host susceptibility, and limited prophylaxis/treatment.
2. **Activity-dependent exposure:** culture, amplification, centrifugation, homogenization, animal procedures, high concentration/volume, and other aerosol-generating operations.
3. **Risk mitigation:** primary containment, directional airflow, sufficient ventilation, boundary integrity, respiratory protection, restricted access, decontamination, training, and management oversight.

A multifactorial risk assessment integrates these layers and selects BSL-3 controls. This is preferable to asserting that a gene, virulence factor, species, or Risk Group 3 designation directly and universally “causes” BSL-3 status. WHO-derived risk-assessment factors include concentration, volume, infectious dose, transmissibility, disease severity, microbial stability, procedures, and personnel behavior. Historical descriptions distinguish BSL-2 moderate hazards, BSL-3 severe respiratory hazards requiring stringent air containment, and BSL-4 high-risk lethal agents requiring maximum isolation. (zuo2024ahistoricalstudy pages 4-6, zuo2024ahistoricalstudy pages 12-13)

## 1. Trait scope and boundaries

### Operational meaning

The target denotes the containment level selected for laboratory work presenting a substantial inhalational or otherwise serious occupational hazard. Contemporary summaries associate BSL-3 with agents capable of serious or lethal disease through inhalation and with controls such as negative pressure, HEPA filtration, respiratory protection, and specialized training. (bawshkhah2024thebiosafetylevel pages 1-2)

The phenotype-like observation is therefore not simply “microbe X is BSL-3.” A more precise representation is:

> **Given agent X, procedure Y, quantity/concentration Z, host context H, and controls C, risk assessment selects BSL-3 containment.**

This distinction is important because the same agent may be handled under different conditions depending on whether work is nonpropagative, involves culture or amplification, uses attenuated rather than wild-type strains, or generates concentrated aerosols. For example, liquid-culture drug-susceptibility testing is among the highest-risk tuberculosis laboratory procedures, while molecular testing that reduces culture can reduce exposure risk. (blacksell2023thebiosafetyresearch pages 8-9, blacksell2023thebiosafetyresearch pages 15-15)

### Nearby traits and boundary cases

- **BSL-2:** moderate-risk work; less stringent facility-level air containment. BSL-2 is not appropriate merely because an agent can cause disease if the protocol-specific inhalation and consequence risks remain moderate. (zuo2024ahistoricalstudy pages 4-6)
- **BSL-4:** maximum containment for agents presenting very high individual risk, frequently severe/lethal disease and limited countermeasures. Disease fatality alone does not cleanly separate BSL-3 from BSL-4; risk assessment includes transmissibility, procedure, dose, and countermeasures. SARS-CoV-2 was argued to fit Risk Group 3 despite reported early-pandemic mortality substantially below that of Ebola. (kaufer2020laboratorybiosafetymeasures pages 1-3)
- **Risk Group 3 versus BSL-3:** risk group characterizes an agent’s hazard, whereas biosafety level describes the controls applied to a particular activity. They are related but should not be represented as equivalent classes.
- **Attenuated versus wild-type virus:** influenza aerosol HID50 estimates of 0.6–3.0 TCID50 came largely from attenuated strains and may not reflect wild-type infectious dose. This is a major boundary condition for curation. (blacksell2023thebiosafetyresearch pages 4-5)
- **Nonpropagative versus propagative work:** culture, amplification, and drug-susceptibility testing increase organism quantity, handling time, and aerosol opportunity. Simplified molecular testing can partly remove this pathway. (blacksell2023thebiosafetyresearch pages 8-9, blacksell2023thebiosafetyresearch pages 15-15)
- **Animal and agricultural work:** containment may be driven by environmental or economic consequences even when human disease risk is limited. ASFV laboratories use BSL-3 containment to prevent release into susceptible animal populations; this is not equivalent to a human inhalational-disease phenotype. (pavone2024biologicalcontainmentfor pages 3-5)
- **Eradicated pathogens:** poliovirus containment is tightened to prevent reintroduction into communities after eradication, demonstrating that population immunity and public-health consequences can drive enhanced containment independently of intrinsic virulence. (ottendorfer2024establishmentofa pages 1-2)

## 2. Candidate graph nodes

### Target and assessment nodes

- **biosafety level 3** — METPO:1001104
- protocol-specific biorisk assessment — label-only
- acceptable residual risk — label-only
- serious or potentially lethal disease — label-only
- inhalational occupational hazard — label-only
- laboratory-acquired infection — label-only
- accidental environmental release — label-only
- population susceptibility / community immunity — label-only
- availability of effective prophylaxis or treatment — label-only

### Agent and taxon nodes

- *Mycobacterium tuberculosis* — NCBITaxon:1773
- influenza A virus — NCBITaxon:11320
- SARS-CoV-2 — NCBITaxon:2697049
- African swine fever virus — NCBITaxon:10497
- viruses — NCBITaxon:10239
- zoonotic avian influenza virus — label-only unless strain-specific taxon is recorded
- wild-type pathogen; attenuated strain; eradicated pathogen — label-only contextual nodes

### Hazard properties and biological processes

- aerosol transmissibility
- lower-respiratory-tract deposition/initiation of infection
- low infectious dose
- disease severity
- environmental persistence
- fomite transmission opportunity
- broad or susceptible host range
- resistance/susceptibility to chemical inactivation
- resistance/susceptibility to thermal inactivation
- pathogen amplification in culture

These should remain label-only unless exact ontology matches are validated during YAML curation. **GO:0019076, viral release from host cell**, is valid but is not directly supported as a determinant of BSL-3 assignment in the reviewed evidence and should not be added merely because the graph concerns viruses.

### Experimental and environmental factors

- liquid culture
- drug-susceptibility testing
- centrifugation, pipetting, homogenization, autopsy/frozen-section preparation
- animal infection procedure
- organism concentration and volume
- aerosol-generating procedure
- air-exchange rate
- directional inward airflow / negative pressure
- room boundary leakage
- temperature, humidity, ultraviolet radiation, and surface material

Aerosols below approximately 5–10 μm can penetrate into the lungs, whereas very large droplets are principally short-range hazards; HVAC ventilation rate and airflow direction affect indoor transmission. This is general airborne-transmission evidence rather than a BSL-3-specific threshold. (argyropoulos2023airbornetransmissionof pages 21-22)

### Control nodes

- biological safety cabinet / primary containment
- directional airflow or negative-pressure ventilation
- HEPA-filtered exhaust
- adequate air exchanges per hour
- tested containment boundary
- controlled access
- respirator / respiratory protection
- protective clothing and other PPE
- validated disinfection
- autoclaving or thermal inactivation
- waste and effluent treatment
- competency-based training
- incident reporting, audit, emergency response, and occupational-health surveillance

### Chemical nodes

- hypochlorous acid — CHEBI:29222
- hydrogen peroxide — CHEBI:16240
- ethanol — CHEBI:16236
- sodium hypochlorite — retain label-only unless the exact intended chemical species is resolved
- phenol, glutaraldehyde, potassium monopersulfate — use label-only pending identifier verification

No electron donors, electron acceptors, nutrient pathways, metabolic modules, organelles, transporters, or enzyme complexes emerged as general determinants of BSL-3. Their inclusion would conflate organism-specific pathogenesis with containment classification.

## 3. Evidence-backed candidate causal edges

The strongest curation candidates are summarized below. The table deliberately separates general decision edges from taxon- and assay-specific mechanistic evidence.

| subject | predicate | object | evidence/value | scope/uncertainty | DOI |
|---|---|---|---|---|---|
| aerosol transmission route | enables | lower respiratory infection / inhalational hazard | “Many, possibly most, natural influenza infections occur by the aerosol route and that the lower respiratory tract may be the preferred site of initiation of the infection.” (blacksell2023thebiosafetyresearch pages 4-5) | Taxon-specific to influenza/ZAI; supports inhalational-hazard logic for BSL-3, not a universal mechanism | 10.1089/apb.2022.0038 |
| low infectious dose | increases | occupational infection hazard | For *Mycobacterium tuberculosis*, “HID50 estimated at <10 bacilli” and it is “in the top percentile of LAIs worldwide” (blacksell2023thebiosafetyresearch pages 8-9) | Strong but taxon-specific; supports hazard severity/likelihood rather than direct BSL assignment alone | 10.1089/apb.2022.0038 |
| culture / drug susceptibility testing (DST) | increases | TB infection risk | “Direct antimicrobial susceptibility testing (DST) using liquid cultures… is considered the highest risk in the tuberculosis laboratory”; relative risk for DST technicians was “21.5” (95% CI) (blacksell2023thebiosafetyresearch pages 8-9, blacksell2023thebiosafetyresearch pages 10-12) | Strong, procedure-specific, mainly *M. tuberculosis* | 10.1089/apb.2022.0038 |
| higher air exchange rate / ventilation | reduces | TB conversion risk | Workers exposed to lower air exchange rates “16.7 vs 32.5 exchanges/hour” had higher tuberculin conversion; labs with ~32.5 exchanges/hour had no seroconversions in cited evidence (blacksell2023thebiosafetyresearch pages 10-12, blacksell2023thebiosafetyresearch pages 9-10) | Taxon- and setting-specific; observational occupational evidence | 10.1089/apb.2022.0038 |
| respirator use | reduces | transmission risk | Transmission risk is “reduced when staff wear respirators” (blacksell2023thebiosafetyresearch pages 15-15) | Qualitative and not effect-size quantified; respiratory-pathogen focused | 10.1089/apb.2022.0038 |
| environmental persistence on surfaces / at low temperature | increases | release / transmission opportunity | Influenza transmission via fomites could occur “for 2–8 hr via stainless steel surfaces”; H5N1 “remained viable for more than 100 days at 4 C” (blacksell2023thebiosafetyresearch pages 4-5, blacksell2023thebiosafetyresearch pages 8-9) | Taxon-specific to avian influenza; persistence does not itself define BSL-3 | 10.1089/apb.2022.0038 |
| hypochlorous acid (50 ppm) | inactivates | avian influenza virus | “50 ppm could reduce the titer of an ordinary AIV (H7N1) from 10^7.7 TCID50/ml to lower than the detectable limit within 5 sec” (blacksell2023thebiosafetyresearch pages 4-5) | Strong but assay- and taxon-specific disinfectant edge | 10.1089/apb.2022.0038 |
| heat treatment | inactivates | avian influenza virus | “56 C to 60 C for 60 min would inactivate” H5/H7/H9; H7N7 >10^5 PFU/mL inactivated at “63 C in 2 min” (blacksell2023thebiosafetyresearch pages 8-9) | Strong but taxon-specific thermal inactivation edge | 10.1089/apb.2022.0038 |
| boundary integrity testing | reduces | potential aerosolized-agent release | Primary objective: “To minimize the potential for release of aerosolized infectious agents”; recommended two-step leak testing with 55% rooms meeting proposed criterion and ARS acceptance criterion 0.139 L/s/m² at 250 Pa (ziegler2024boundaryintegritytesting pages 1-2, ziegler2024boundaryintegritytesting pages 7-9) | Engineering-control edge for CL3 facility performance, not a microbial mechanism | 10.1089/apb.2023.0017 |
| multifactor risk assessment | selects / justifies | BSL-3 containment level | Risk factors include microorganism “concentration, volume, infectious dose, transmissibility, severity, stability” plus procedures/personnel; BSL system includes “BSL-3 for severe respiratory pathogens necessitating stringent air containment” (zuo2024ahistoricalstudy pages 12-13, zuo2024ahistoricalstudy pages 4-6) | Best curated as decision/assessment edge; BSL-3 is context-dependent and not equivalent to an intrinsic microbial trait | 10.3390/laboratories1020007 |


*Table: This table summarizes the strongest source-backed causal edges that could inform a TraitMech graph for BSL-3, emphasizing procedure, transmission, environmental, and containment factors rather than universal molecular mechanisms. It is useful for curators because it separates strong taxon-specific evidence from broader risk-assessment and engineering-control edges.*

### Additional implementation and management edges

| Subject | Predicate | Object | Supporting snippet | Curation note |
|---|---|---|---|---|
| Restricted authorization | reduces | unauthorized entry/material access | NUS BSL-3 operations required that access be “restricted” and PINs issued “only [to] authorized individuals.” (joseph2021managementsystemapproach pages 2-4) | Curatable as a biosecurity/administrative-control edge, not a microbial mechanism. |
| Demonstrated proficiency and training | reduces | unsafe work practices | Personnel had to “demonstrate proficiency in safe laboratory practices before work” with biological agents. (joseph2021managementsystemapproach pages 2-4) | Plausible and operationally important, but no effect size was reported. |
| Risk assessment before work and after change | identifies | required preventive measures | ASF guidance states that assessment must occur before activity and when procedures, risks, facilities, equipment, or agents change; it was used to identify preventive measures and reduce risk to an acceptable level. (pavone2024biologicalcontainmentfor pages 3-5) | Strong decision-process edge; ASF implementation is context-specific. |
| Aerosol-generating laboratory procedures | increase | respiratory exposure opportunity | Pipetting and centrifugation can disperse infectious particles; autopsy, frozen-section preparation, and liquid culture are identified aerosolization settings. (blacksell2023thebiosafetyresearch pages 9-10, haider2024exploringthefactors pages 1-3) | Procedure-specific. The Qeios source is weaker than the peer-reviewed tuberculosis evidence. |
| Molecular testing replacing culture | reduces | culture-associated LAI risk | GeneXpert substantially reduces the need for prolonged in-vitro culture and associated exposure, although cultures may still be required. (blacksell2023thebiosafetyresearch pages 8-9, blacksell2023thebiosafetyresearch pages 15-15) | Strongly relevant for TB; not universally applicable. |
| Organic material / specimen matrix | modifies | disinfectant efficacy | Sodium hypochlorite activity is inhibited by organic material; 70% ethanol was effective in suspension but not in sputum. (blacksell2023thebiosafetyresearch pages 4-5, blacksell2023thebiosafetyresearch pages 10-12) | Important assay-condition modifier; avoid universal “chemical kills organism” assertions. |

## 4. Recent developments, applications, and statistics

### Evidence-based biosafety research

The 2023 Biosafety Research Road Map emphasized that major data gaps remain even for canonical BSL-3 respiratory pathogens. For *M. tuberculosis*, definitive measurements of aerosolization during diagnostic procedures remain inadequate, while influenza infectious-dose estimates may derive from attenuated strains. The expert implication is that control selection should disclose evidence uncertainty rather than imply precise universal thresholds. (blacksell2023thebiosafetyresearch pages 2-4, blacksell2023thebiosafetyresearch pages 4-5)

Recent quantitative observations include:

- *M. tuberculosis* HID50 was estimated at **<10 bacilli**. Historical reviews found **194 laboratory-acquired cases and four deaths during 1930–1979**, followed by **255 reported LAIs and no fatalities during 1979–2015**. (blacksell2023thebiosafetyresearch pages 8-9)
- Tuberculosis culture/DST technicians had a reported relative risk of **21.5** (95% CI **4.5–102.5**) compared with non-laboratory workers, versus about **1.4** for microscopy technicians. (blacksell2023thebiosafetyresearch pages 10-12)
- Lower ventilation—approximately **16.7–17 air exchanges/hour**, versus **32.5 exchanges/hour**—was associated with significantly more tuberculin conversion in the cited occupational setting. This is observational, not a universal prescriptive threshold. (blacksell2023thebiosafetyresearch pages 10-12, blacksell2023thebiosafetyresearch pages 9-10)
- Influenza aerosol HID50 was **0.6–3.0 TCID50**, compared with **127–320 TCID50** for intranasal drops, but the underlying attenuated-strain evidence limits extrapolation to wild-type zoonotic influenza. (blacksell2023thebiosafetyresearch pages 4-5)
- H5N1 remained viable for **>100 days at 4°C** in one cited study; potential fomite transmission persisted **2–8 hours on stainless steel** under heavy contamination. (blacksell2023thebiosafetyresearch pages 8-9, blacksell2023thebiosafetyresearch pages 4-5)

### Facility engineering and validation

A 2024 study comparing CL3 facilities reported that only **55%** of rooms built using typical methods met the proposed leakage criterion. The authors described the USDA ARS value of **0.139 L/s/m² at 250 Pa** as challenging but achievable and recommended qualitative leak detection followed by quantitative testing. For primary-containment rooms, they highlighted the more stringent German VDI value of **0.03620 L/s/m² at 250 Pa**. These are proposed or jurisdictional engineering criteria, not universal BSL-3 biological requirements. (ziegler2024boundaryintegritytesting pages 7-9, ziegler2024boundaryintegritytesting pages 1-2)

### Poliovirus containment implementation

The U.S. National Authority for Containment conducted **27 site visits at 18 facilities**, covering 20 laboratories: **65% A/BSL-2, 20% A/BSL-3, and 15% storage-only**. Improvement areas included primary containment, decontamination, hand hygiene, security, emergency response, training, and immunization. Sixteen applications were endorsed to pursue certification, while four facilities withdrew. This is a useful real-world example of risk-based, audited containment extending beyond nominal BSL labels. Published 27 January 2024. (ottendorfer2024establishmentofa pages 1-2)

### African swine fever containment

The Italian National Reference Laboratory developed a BSL-3 containment and audit framework covering infected samples, waste, animal infections, unauthorized entry, wastewater, utility interruption, and emergency conditions. Its risk model combined event likelihood with consequence severity and required reassessment after changes to agents, procedures, equipment, or facilities. This illustrates an environmental/agricultural BSL-3 boundary in which preventing pathogen escape into animal populations is central. (pavone2024biologicalcontainmentfor pages 3-5)

### Demonstrated inactivation controls

For avian influenza, **50 ppm hypochlorous acid** reduced H7N1 from **10^7.7 TCID50/mL to below detection within 5 seconds** under the reported conditions. Heat at **56–60°C for 60 minutes** inactivated H5/H7/H9, while **63°C for two minutes** inactivated HPAI H7N7 at >10^5 PFU/mL. These are useful validation edges but must retain strain, matrix, concentration, contact-time, and assay annotations. (blacksell2023thebiosafetyresearch pages 8-9, blacksell2023thebiosafetyresearch pages 4-5)

## 5. Expert analysis for TraitMech design

A compact graph should use **“risk assessment selects BSL-3 containment”** as the terminal decision edge rather than **“virulence causes BSL-3.”** Agent-level virulence is only one input. The strongest intermediate causal chain is:

**aerosol-generating activity + viable airborne pathogen + sufficiently low infectious dose → inhalational exposure/infection risk → serious occupational consequence → selection of BSL-3 controls.**

A parallel mitigation chain is:

**primary containment + directional airflow/ventilation + tested boundary + respirator + access control + validated decontamination + trained personnel → reduced exposure/release probability → acceptable residual risk.**

This formulation accommodates divergent cases: human respiratory pathogens, agricultural agents such as ASFV, eradicated poliovirus, attenuated strains, and nonpropagative diagnostic procedures. It also avoids claiming that every BSL-3 organism shares a molecular pathway.

## 6. Warnings: claims not ready for curation

1. **The supplied DOI is mischaracterized.** DOI **10.1146/annurev.micro.62.081307.162938** is *Regulation and Function of Ag43 (Flu)*, an *Escherichia coli* Antigen 43 review—not a general virulence-factor review establishing BSL-3 status. It discusses an outer-membrane autotransporter, aggregation, phase variation, pathogenic/commensal alleles, and biofilm-related biology. It provides no direct evidence that Ag43 causes a BSL-3 hazard or assignment. It should be removed from the BSL-3 graph unless a separate, taxon-specific causal chain is documented. (woude2008regulationandfunction pages 1-2)
2. **Do not equate RG3 with BSL-3.** Risk group is an agent-hazard category; containment level is selected for a protocol and facility context.
3. **Do not curate genes, proteins, virulence factors, pathways, or metabolic modules as universal BSL-3 causes.** No cross-taxon molecular mechanism was identified.
4. **Do not generalize influenza or tuberculosis measurements to all BSL-3 agents.** Infectious dose, persistence, aerosol behavior, and control susceptibility are taxon- and assay-specific.
5. **Do not treat historical LAI counts as current incidence.** Reporting requirements and ascertainment changed over time; underreporting is documented as an evidence limitation. (blacksell2023thebiosafetyresearch pages 8-9)
6. **Do not convert observational ventilation findings into a universal ACH requirement.** The 16.7/32.5 ACH comparison is setting-specific evidence supporting the direction of effect.
7. **Do not represent absence of reported LAIs as proof of zero risk.** No published ZAI LAIs were found, but reporting and attribution limitations remain. (blacksell2023thebiosafetyresearch pages 2-4)
8. **Do not curate HEPA filtration, negative pressure, BSC use, PPE, or training as quantitatively effective unless the edge permits qualitative evidence.** Recent sources support their use, but organism- and procedure-specific effect sizes are often unavailable. (bawshkhah2024thebiosafetylevel pages 1-2, blacksell2023thebiosafetyresearch pages 15-15)
9. **Avoid unverified CURIEs.** Aerosol-generating procedure, infectious dose, directional airflow, BSC, risk assessment, and containment boundary should remain label-only until exact ontology terms are confirmed.

## 7. DOI-first bibliography

1. **10.1089/apb.2022.0038** — Blacksell SD et al. “The Biosafety Research Road Map: The Search for Evidence to Support Practices in the Laboratory—Zoonotic Avian Influenza and *Mycobacterium tuberculosis*.” *Applied Biosafety* 28:135–151. Published September 2023. https://doi.org/10.1089/apb.2022.0038 (blacksell2023thebiosafetyresearch pages 8-9)
2. **10.1089/apb.2023.0017** — Ziegler C, Tremblay G. “Boundary Integrity Testing of Containment Level 3 (Biological Safety Level 3) Laboratories.” *Applied Biosafety* 29:10–18. Published March 2024. https://doi.org/10.1089/apb.2023.0017 (ziegler2024boundaryintegritytesting pages 1-2)
3. **10.3390/laboratories1020007** — Zuo K et al. “A Historical Study on the Scientific Attribution of Biosafety Risk Assessment in Real Cases of Laboratory-Acquired Infections.” *Laboratories* 1:87–102. Published June 2024. https://doi.org/10.3390/laboratories1020007 (zuo2024ahistoricalstudy pages 12-13)
4. **10.3390/pathogens13020116** — Ottendorfer C et al. “Establishment of a Poliovirus Containment Program and Containment Certification Process for Poliovirus-Essential Facilities, United States 2017–2022.” *Pathogens* 13:116. Published 27 January 2024. https://doi.org/10.3390/pathogens13020116 (ottendorfer2024establishmentofa pages 1-2)
5. **10.3390/ani14030454** — Pavone S et al. “Biological Containment for African Swine Fever Laboratories and Animal Facilities.” *Animals* 14:454. Published January 2024. https://doi.org/10.3390/ani14030454 (pavone2024biologicalcontainmentfor pages 3-5)
6. **10.1007/s11869-022-01286-w** — Argyropoulos C et al. “Airborne Transmission of Biological Agents within the Indoor Built Environment: A Multidisciplinary Review.” *Air Quality, Atmosphere & Health* 16:477–533. Published 2023. https://doi.org/10.1007/s11869-022-01286-w (argyropoulos2023airbornetransmissionof pages 21-22)
7. **10.1016/j.pathol.2020.09.006** — Kaufer AM et al. “Laboratory Biosafety Measures Involving SARS-CoV-2 and Classification as a Risk Group 3 Biological Agent.” *Pathology* 52:790–795. Published December 2020. https://doi.org/10.1016/j.pathol.2020.09.006 (kaufer2020laboratorybiosafetymeasures pages 1-3)
8. **10.1089/apb.2021.0007** — Joseph T. “Management System Approach for Addressing Biosafety and Biosecurity of Emerging Pathogens in a Biosafety Level-3 Core Facility.” *Applied Biosafety* 26:210–220. Published December 2021. https://doi.org/10.1089/apb.2021.0007 (joseph2021managementsystemapproach pages 2-4)
9. **10.1146/annurev.micro.62.081307.162938** — van der Woude MW, Henderson IR. “Regulation and Function of Ag43 (Flu).” *Annual Review of Microbiology* 62:153–169. Published October 2008. https://doi.org/10.1146/annurev.micro.62.081307.162938. **Not direct BSL-3 evidence.** (woude2008regulationandfunction pages 1-2)

## Recommended minimal graph core

For an initial revision of `data/traits/ecology/biosafety_level_3.yaml`, prioritize these high-level nodes and edges:

- agent/procedure risk factors → **inform** → protocol-specific biorisk assessment;
- aerosol-generating procedure → **increases** → inhalational exposure opportunity;
- low infectious dose → **increases** → infection likelihood conditional on exposure;
- serious disease consequence → **increases** → risk severity;
- biorisk assessment → **selects** → METPO:1001104;
- primary containment / directional airflow / ventilation / respirator / access control / decontamination / training → **reduces** → exposure or release probability;
- validated controls → **reduce** → residual risk.

Keep the quantitative influenza, tuberculosis, ASFV, and poliovirus subgraphs as explicitly taxon-specific evidence modules rather than universal parents of BSL-3.

References

1. (zuo2024ahistoricalstudy pages 4-6): Kunlan Zuo, Zongzhen Wu, Chihong Zhao, and Huan Liu. A historical study on the scientific attribution of biosafety risk assessment in real cases of laboratory-acquired infections. Laboratories, 1:87-102, Jun 2024. URL: https://doi.org/10.3390/laboratories1020007, doi:10.3390/laboratories1020007. This article has 3 citations.

2. (zuo2024ahistoricalstudy pages 12-13): Kunlan Zuo, Zongzhen Wu, Chihong Zhao, and Huan Liu. A historical study on the scientific attribution of biosafety risk assessment in real cases of laboratory-acquired infections. Laboratories, 1:87-102, Jun 2024. URL: https://doi.org/10.3390/laboratories1020007, doi:10.3390/laboratories1020007. This article has 3 citations.

3. (bawshkhah2024thebiosafetylevel pages 1-2): Mohammed Ahmed Bawshkhah, Mohammad Yousef Issa Alshabi, Yazeed Saad Alharthi, Tariq Abdullah AlShamrani, Mohammed labiad Almaliki, Manar Abdulaziz Almazroua, Haifa Ayedh Alzayedi, Mohammed Mansour Ahmed Hazzazi, Mohammed Hasan Alhazemi, and Manal Abdulaziz AlManshi. The biosafety level 3 (bsl-3) laboratory readiness for emerging pathogens: a review study. Saudi Journal of Medicine and Public Health, 1:392-399, Dec 2024. URL: https://doi.org/10.64483/jmph-115, doi:10.64483/jmph-115. This article has 2 citations.

4. (blacksell2023thebiosafetyresearch pages 8-9): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—zoonotic avian influenza and <i>mycobacterium tuberculosis</i>. Applied Biosafety, 28:135-151, Sep 2023. URL: https://doi.org/10.1089/apb.2022.0038, doi:10.1089/apb.2022.0038. This article has 6 citations.

5. (blacksell2023thebiosafetyresearch pages 15-15): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—zoonotic avian influenza and <i>mycobacterium tuberculosis</i>. Applied Biosafety, 28:135-151, Sep 2023. URL: https://doi.org/10.1089/apb.2022.0038, doi:10.1089/apb.2022.0038. This article has 6 citations.

6. (kaufer2020laboratorybiosafetymeasures pages 1-3): Alexa M. Kaufer, Torsten Theis, Katherine A. Lau, Joanna L. Gray, and William D. Rawlinson. Laboratory biosafety measures involving sars-cov-2 and the classification as a risk group 3 biological agent. Pathology, 52:790-795, Dec 2020. URL: https://doi.org/10.1016/j.pathol.2020.09.006, doi:10.1016/j.pathol.2020.09.006. This article has 103 citations and is from a peer-reviewed journal.

7. (blacksell2023thebiosafetyresearch pages 4-5): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—zoonotic avian influenza and <i>mycobacterium tuberculosis</i>. Applied Biosafety, 28:135-151, Sep 2023. URL: https://doi.org/10.1089/apb.2022.0038, doi:10.1089/apb.2022.0038. This article has 6 citations.

8. (pavone2024biologicalcontainmentfor pages 3-5): Silvia Pavone, Carmen Iscaro, Monica Giammarioli, Maria Serena Beato, Cecilia Righi, Stefano Petrini, Silva Costarelli, and Francesco Feliziani. Biological containment for african swine fever (asf) laboratories and animal facilities: the italian challenge in bridging the present regulatory gap and enhancing biosafety and biosecurity measures. Animals, 14:454, Jan 2024. URL: https://doi.org/10.3390/ani14030454, doi:10.3390/ani14030454. This article has 9 citations and is from a peer-reviewed journal.

9. (ottendorfer2024establishmentofa pages 1-2): Christy Ottendorfer, Bryan Shelby, Cecelia A. Sanders, Anna Llewellyn, Christy Myrick, Christye Brown, Suganthi Suppiah, Kortney Gustin, and Lia Haynes Smith. Establishment of a poliovirus containment program and containment certification process for poliovirus-essential facilities, united states 2017–2022. Pathogens, 13:116, Jan 2024. URL: https://doi.org/10.3390/pathogens13020116, doi:10.3390/pathogens13020116. This article has 7 citations.

10. (argyropoulos2023airbornetransmissionof pages 21-22): C. Argyropoulos, V. Skoulou, G. Efthimiou, and A. Michopoulos. Airborne transmission of biological agents within the indoor built environment: a multidisciplinary review. Air Quality, Atmosphere, & Health, 16:477-533, Nov 2023. URL: https://doi.org/10.1007/s11869-022-01286-w, doi:10.1007/s11869-022-01286-w. This article has 54 citations.

11. (blacksell2023thebiosafetyresearch pages 10-12): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—zoonotic avian influenza and <i>mycobacterium tuberculosis</i>. Applied Biosafety, 28:135-151, Sep 2023. URL: https://doi.org/10.1089/apb.2022.0038, doi:10.1089/apb.2022.0038. This article has 6 citations.

12. (blacksell2023thebiosafetyresearch pages 9-10): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—zoonotic avian influenza and <i>mycobacterium tuberculosis</i>. Applied Biosafety, 28:135-151, Sep 2023. URL: https://doi.org/10.1089/apb.2022.0038, doi:10.1089/apb.2022.0038. This article has 6 citations.

13. (ziegler2024boundaryintegritytesting pages 1-2): Cory Ziegler and Gilles Tremblay. Boundary integrity testing of containment level 3 (biological safety level 3) laboratories. Applied Biosafety, 29:10-18, Mar 2024. URL: https://doi.org/10.1089/apb.2023.0017, doi:10.1089/apb.2023.0017. This article has 1 citations.

14. (ziegler2024boundaryintegritytesting pages 7-9): Cory Ziegler and Gilles Tremblay. Boundary integrity testing of containment level 3 (biological safety level 3) laboratories. Applied Biosafety, 29:10-18, Mar 2024. URL: https://doi.org/10.1089/apb.2023.0017, doi:10.1089/apb.2023.0017. This article has 1 citations.

15. (joseph2021managementsystemapproach pages 2-4): Tessy Joseph. Management system approach for addressing biosafety and biosecurity of emerging pathogens in a biosafety level-3 core facility. Dec 2021. URL: https://doi.org/10.1089/apb.2021.0007, doi:10.1089/apb.2021.0007. This article has 13 citations.

16. (haider2024exploringthefactors pages 1-3): Ali Haider, Fatima Khizar, Tehreem Javed, Muhammad Wajid, and Saira Sattar. Exploring the factors aggravating disease transmission in healthcare environments: strategies for mitigation. Qeios, Feb 2024. URL: https://doi.org/10.32388/lb0dky, doi:10.32388/lb0dky. This article has 0 citations.

17. (blacksell2023thebiosafetyresearch pages 2-4): Stuart D. Blacksell, Sandhya Dhawan, Marina Kusumoto, Kim Khanh Le, Kathrin Summermatter, Joseph O'Keefe, Joseph Kozlovac, Salama Suhail Almuhairi, Indrawati Sendow, Christina M. Scheel, Anthony Ahumibe, Zibusiso M. Masuku, Allan M. Bennett, Kazunobu Kojima, David R. Harper, and Keith Hamilton. The biosafety research road map: the search for evidence to support practices in the laboratory—zoonotic avian influenza and <i>mycobacterium tuberculosis</i>. Applied Biosafety, 28:135-151, Sep 2023. URL: https://doi.org/10.1089/apb.2022.0038, doi:10.1089/apb.2022.0038. This article has 6 citations.

18. (woude2008regulationandfunction pages 1-2): Marjan W. van der Woude and Ian R. Henderson. Regulation and function of ag43 (flu). Oct 2008. URL: https://doi.org/10.1146/annurev.micro.62.081307.162938, doi:10.1146/annurev.micro.62.081307.162938. This article has 217 citations and is from a peer-reviewed journal.