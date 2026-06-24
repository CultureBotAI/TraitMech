---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:19:35.329115'
end_time: '2026-06-18T11:40:32.868388'
duration_seconds: 1257.54
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dormancy
  trait_identifier: traitmech:000080
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: dormancy
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A reversible physiological state of greatly reduced metabolic activity
    that allows a cell to survive unfavorable conditions and later resuscitate, generating
    a microbial seed bank.
  parent_traits: METPO:1000059
  synonyms: dormant state
  evidence_summary: 'DOI:10.1038/nrmicro2504:  (Lennon & Jones review microbial seed
    banks and the mechanisms by which microorganisms enter and exit dormancy; parent
    of VBNC and persister sub-variants.) | DOI:10.1038/nrmicro1557:  (Lewis links
    dormancy to persister-cell survival and infectious disease.)'
  causal_graph_summary: 'dormancy_seed_bank: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dormancy
- **METPO identifier:** traitmech:000080
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A reversible physiological state of greatly reduced metabolic activity that allows a cell to survive unfavorable conditions and later resuscitate, generating a microbial seed bank.
- **Parent traits:** METPO:1000059
- **Synonyms:** dormant state
- **Existing evidence:** DOI:10.1038/nrmicro2504:  (Lennon & Jones review microbial seed banks and the mechanisms by which microorganisms enter and exit dormancy; parent of VBNC and persister sub-variants.) | DOI:10.1038/nrmicro1557:  (Lewis links dormancy to persister-cell survival and infectious disease.)
- **Existing causal graph summary:** dormancy_seed_bank: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dormancy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/dormancy.yaml`.

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
- **Trait label:** dormancy
- **METPO identifier:** traitmech:000080
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A reversible physiological state of greatly reduced metabolic activity that allows a cell to survive unfavorable conditions and later resuscitate, generating a microbial seed bank.
- **Parent traits:** METPO:1000059
- **Synonyms:** dormant state
- **Existing evidence:** DOI:10.1038/nrmicro2504:  (Lennon & Jones review microbial seed banks and the mechanisms by which microorganisms enter and exit dormancy; parent of VBNC and persister sub-variants.) | DOI:10.1038/nrmicro1557:  (Lewis links dormancy to persister-cell survival and infectious disease.)
- **Existing causal graph summary:** dormancy_seed_bank: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dormancy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/dormancy.yaml`.

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


# Microbial Trait Causal Graph Report: Dormancy (traitmech:000080)

## 1) Scope summary (TraitMech curation target)

**Dormancy (traitmech:000080)** is best curated as a **reversible physiological state of greatly reduced metabolic activity and/or growth arrest** that enables survival during unfavorable conditions and allows later **resuscitation** (return to anabolic activity and potential replication). Contemporary literature emphasizes that dormancy is often **heterogeneous** within populations (a fraction of cells enter dormancy), and that multiple partially overlapping “dormancy-like” phenotypes exist, including **persister cells** and **VBNC (viable-but-nonculturable) cells**, which can be conceptualized as differing in “dormancy depth” and measurement modality (tolerance vs culturability). (yuan2024molecularmechanismand pages 3-6)

**Boundary cases (do not conflate):**
- **Antibiotic resistance vs tolerance/persistence:** persisters tolerate antibiotics **without elevated MIC** and can regrow after treatment ends; this differs from genetically encoded resistance. (yuan2024molecularmechanismand pages 3-6)
- **VBNC vs death:** VBNC cells are viable but fail to form colonies on standard media; nonculturability can also arise from **assay conditions** (e.g., oxidative stress in rich media) rather than irreversible loss of viability. (yuan2024molecularmechanismand pages 3-6, prosdocimi2023cellphenotypechanges pages 7-10)
- **Dormancy vs developmental differentiation (e.g., spores):** ribosome/enzyme “hibernation” is a reversible molecular strategy seen broadly across life, distinct from producing specialized dormant structures (spores), though spores also involve metabolic inactivity. (helenabueno2024ripplinglifeon pages 1-3)

## 2) Key concepts and definitions (current understanding)

### 2.1 Persisters
Persisters are defined as a **subpopulation that survives high antibiotic concentrations** and then **re-proliferates after antibiotic removal**, contributing to treatment failure and recurrence; they are characterized experimentally by **bimodal (biphasic) killing curves** in time-kill assays. (yuan2024molecularmechanismand pages 3-6, yuan2024molecularmechanismand pages 7-9)

### 2.2 VBNC (viable-but-nonculturable)
VBNC cells are described as a **near-dormant state** with **low metabolic activity** and **inability to grow on standard media**, often accompanied by increased stress tolerance; resuscitation may require specific signals/conditions (e.g., altered media, antioxidants, metabolic cues). (yuan2024molecularmechanismand pages 3-6, prosdocimi2023cellphenotypechanges pages 7-10)

### 2.3 Molecular “hibernation” as a dormancy mechanism
A major mechanistic concept emerging across 2023–2024 literature is that dormancy involves **hibernation of essential macromolecular machines** (ribosomes and RNA polymerase among others) via **hibernation factors** that disengage enzymes from substrates and protect them from damage or degradation during stress. (helenabueno2024ripplinglifeon pages 1-3)

## 3) Recent developments & latest mechanistic research (prioritizing 2023–2024)

### 3.1 Environmental dormancy/resuscitation in soil seed banks (desiccation/rewetting)
A high-resolution desert biocrust study (Nature Communications, Apr 2024) provides strong ecosystem-scale evidence that **rewetting is a dominant trigger of exit from dormancy**.

Key findings:
- **Rapid transcriptomic activation:** 85/96 populations changed transcript abundance within **15 minutes** of rehydration; early responses included increased transcripts for **DNA repair** and **energy generation** across taxa. (imminger2024survivalandrapid pages 3-4)
- **Universal, fast resuscitation:** “nearly all microbial populations resuscitate within minutes after simulated rain.” (imminger2024survivalandrapid pages 1-2)
- **Quantitative activity fractions:** after rewetting, **68.4%** of single cells were active by **3 h**, rising to **91.0%** by **12 h** and **94.6%** by **24 h** (heavy-water NanoSIMS). (imminger2024survivalandrapid pages 2-3)
- **Slow net growth despite rapid resuscitation:** inferred median replication/doubling times span **~5.6 days (heterotrophs)** and **~18.7 days (chemoautotrophs)**, with ranges from **hours to hundreds of days** depending on metabolic mode and taxa. (imminger2024survivalandrapid pages 3-4)

These results support causal edges for TraitMech curation such as **rewetting → resuscitation**, and **rewetting → DNA repair/energy generation programs**. (imminger2024survivalandrapid pages 3-4, imminger2024survivalandrapid pages 1-2)

### 3.2 Stringent response ((p)ppGpp) and dormancy regulation
A 2024 persister review summarizes that the stringent response alarmone **(p)ppGpp** is activated by nutrient/heat stresses and can “reprogram cellular life activities” such that the outcome is **slow growth or dormancy**. (yuan2024molecularmechanismand pages 6-7)

The same synthesis connects (p)ppGpp to induction of multiple **toxin–antitoxin (TA) modules** (hipAB, mazEF, mqsRA, relBE, hokB, etc.), enabling a plausible curated cascade **stress → (p)ppGpp → TA induction → translation arrest/energy downshift → dormancy/persistence** (with taxon specificity noted). (yuan2024molecularmechanismand pages 6-7)

### 3.3 Toxin–antitoxin systems and energetic/translation shutdown
Recent work and reviews converge on multiple TA-linked dormancy mechanisms:

- **Membrane-targeting toxins (TisB/HokB):** summarized as inserting into the inner membrane, depolarizing it, disrupting proton-motive force, inhibiting ATP synthesis, and inducing dormancy/persister formation. (yuan2024molecularmechanismand pages 6-7)
- **HipA:** summarized mechanism is phosphorylation of glutamyl-tRNA synthetase (GltX), leading to uncharged tRNA accumulation, RelA activation, and elevated (p)ppGpp. (yuan2024molecularmechanismand pages 3-6, yuan2024molecularmechanismand pages 15-16)
- **Translation-inhibiting toxins (VapC, TacT, RelE, MazF):** summarized as cleaving rRNA/tRNA/mRNA or modifying charged tRNAs to induce translational arrest and dormancy. (yuan2024molecularmechanismand pages 3-6)

A 2024 primary study in *E. coli* directly links the type I TA toxin **TisB** to a mechanistic chain including **membrane depolarization and ATP depletion** and identifies **protein aggregation** as a consequence that correlates with **extended dormancy duration**. (leinberger2024proteinaggregationis pages 1-2)

### 3.4 Ribosome hibernation factors as a measurable molecular signature
A 2024 review highlights that dormancy involves dedicated **ribosome hibernation factors** (e.g., **RMF, HPF, RaiA**) that bind ribosomes and “turn off protein synthesis,” and that these factors can **protect ribosomes** from degradation (e.g., by blocking ribonucleases) during starvation. (helenabueno2024ripplinglifeon pages 11-12)

Quantitative “stoichiometry shift” evidence is provided for *E. coli*: upon stationary-phase entry, cells may have **~2,000 ribosomes**, while hibernation factor copies rise to **~4,000 (HPF), 11,700 (RaiA), and 3,500 (RMF)**—consistent with the possibility that hibernation factors can occupy most ribosomes in dormant/stressed cells. (helenabueno2024ripplinglifeon pages 8-9, helenabueno2024ripplinglifeon media 60e87f11)

## 4) Current applications and real-world implementations

### 4.1 Clinical relevance: antibiotic tolerance, recurrence, and therapy design
Dormancy-like phenotypes (persisters and potentially VBNC) are widely framed as drivers of **ineffective antibiotic therapy and recurrent infections**, motivating strategies that target non-growing cells, energetic states, or resuscitation pathways. (yuan2024molecularmechanismand pages 3-6)

### 4.2 Food safety / pathogen detection (VBNC resuscitation control)
VBNC states create challenges for culture-based detection. A 2024 experimental study shows VBNC *E. coli* resuscitation depends on **ATP-mediated NAD+ synthesis**; ATP depletion (CCCP) **prevents resuscitation**, highlighting potential levers to **block resuscitation** (risk control) or **promote detection** (diagnostics) depending on goal. (yang2024resuscitationofviable pages 6-9, yang2024resuscitationofviable pages 9-10)

### 4.3 Environmental microbiology and bioremediation (Rpf-enabled recovery)
Rpf proteins are described as secreted “cytokine-like” factors that can reactivate dormant cells; their use in culture media is an actionable method to increase recovery of dormant/VBNC organisms. (li2024resuscitationpromotionfactor pages 1-3)

A 2024 reservoir-sediment study emphasizes the ubiquity of **rpf-like genes** and reports application where **Rpf supplementation resuscitated Pseudomonas sp.**, restoring simultaneous nitrification/denitrification—an example of functional revival relevant to wastewater/nutrient cycling. (hou2024exploringthedistribution pages 1-2)

### 4.4 Assay design: oxidative stress confounds culturability measurements
In Vibrio VBNC experiments, very low **H2O2** concentrations (0.007 mM) prevented resuscitation/culturability, while catalase improved culturability by 100–1000× relative to untreated plating in some conditions. This supports incorporating antioxidant controls (e.g., catalase-supplemented plating) when defining dormancy using culturability readouts. (prosdocimi2023cellphenotypechanges pages 7-10)

## 5) Relevant statistics and recent quantitative data (examples for curation prioritization)

- **Rapid community-scale resuscitation after rewetting:** “resuscitate within minutes” after simulated rain. (imminger2024survivalandrapid pages 1-2)
- **Fraction of active cells after hydration:** 68.4% active by 3 h; 91.0% by 12 h; 94.6% by 24 h (heavy-water NanoSIMS). (imminger2024survivalandrapid pages 2-3)
- **Replication time estimates in desert biocrust populations:** heterotrophic median doubling time 5.6 days (range 7 h–147 d); chemoautotrophic median 18.7 days (2.1–471 d). (imminger2024survivalandrapid pages 3-4)
- **Oxidative inhibition threshold:** H2O2 as low as **0.007 mM** prevents Vibrio VBNC resuscitation/culturability; catalase can improve culturability but may not rescue irreversibly damaged cells. (prosdocimi2023cellphenotypechanges pages 7-10)

## 6) Candidate causal-graph nodes (grouped) with ontology grounding

The following node inventory is intended to be mapped into `dormancy.yaml`.

| Node label | Node type (environmental factor, process, gene/protein, pathway/module, metabolite/chemical, assay/measurement) | Suggested ontology grounding (CURIEs where available) | Evidence support (short snippet) | Key references (DOI, year, URL) |
|---|---|---|---|---|
| dormancy | process | METPO:traitmech:000080; GO:0097305? (label only if uncertain) | “slow cell growth or dormancy”; “cells enter states of dormancy or hibernation” (yuan2024molecularmechanismand pages 6-7, helenabueno2024ripplinglifeon pages 1-3) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3; 10.3389/fmicb.2024.1386179 (2024) https://doi.org/10.3389/fmicb.2024.1386179 |
| persister cell | process | label only; child/boundary case of dormancy | “Persisters are a bacterial subpopulation that tolerate antibiotics” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| VBNC state | process | label only; boundary case of dormancy | “VBNC are bacteria in a near-dormant state that cannot grow on standard media” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| resuscitation | process | GO:0009993? (label only if uncertain) | “resuscitate within minutes after simulated rain”; “reactivate dormant bacteria” (imminger2024survivalandrapid pages 1-2, li2024resuscitationpromotionfactor pages 1-3) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6; 10.3390/microorganisms12081528 (2024) https://doi.org/10.3390/microorganisms12081528 |
| desiccation / dry phase | environmental factor | ENVO:01001307? desiccation (label if uncertain) | “During the dry phase, transcripts for ROS protection… were abundant” (imminger2024survivalandrapid pages 7-8) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| rewetting / rain pulse / hydration | environmental factor | ENVO:00000027 rainfall; label: rewetting | “simulated rain”; “rehydration acts as a rapid environmental trigger” (imminger2024survivalandrapid pages 3-4, imminger2024survivalandrapid pages 1-2) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| nutrient limitation / starvation | environmental factor | ENVO:nutrient limitation (label only) | “nutrient limitation and starvation” trigger dormancy/stress responses (leinberger2024proteinaggregationis pages 1-2, yuan2024molecularmechanismand pages 6-7) | 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24; 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| oxidative stress | process | GO:0006979 response to oxidative stress | “oxidative stress strongly affects Vibrio VBNC induction and resuscitation” (prosdocimi2023cellphenotypechanges pages 1-2) | 10.1186/s13213-022-01703-6 (2023) https://doi.org/10.1186/s13213-022-01703-6 |
| hydrogen peroxide | metabolite/chemical | CHEBI:16240 | “0.007 mM… prevented the resuscitation (culturability) of VBNC cells” (prosdocimi2023cellphenotypechanges pages 7-10) | 10.1186/s13213-022-01703-6 (2023) https://doi.org/10.1186/s13213-022-01703-6 |
| antibiotics | metabolite/chemical | CHEBI:33281 antibiotic | “antibiotic exposure… can induce dormancy”; persisters survive treatment (yuan2024molecularmechanismand pages 3-6, leinberger2024proteinaggregationis pages 1-2) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3; 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24 |
| fluoroquinolone antibiotic | metabolite/chemical | CHEBI:35222 fluoroquinolone antibiotic | “DNA damage mediated by the fluoroquinolone antibiotic ciprofloxacin” (leinberger2024proteinaggregationis pages 1-2) | 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24 |
| ciprofloxacin | metabolite/chemical | CHEBI:100241 | “ciprofloxacin in E. coli wild-type cells” induces TisB-linked aggregation/dormancy context (leinberger2024proteinaggregationis pages 1-2) | 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24 |
| (p)ppGpp | metabolite/chemical | CHEBI:63939 | “(p)ppGpp… will result in slow cell growth or dormancy” (yuan2024molecularmechanismand pages 6-7) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| stringent response | pathway/module | GO:0009269 response to desiccation?; label: stringent response | “The stringent response mediated by (p)ppGpp” (yuan2024molecularmechanismand pages 6-7) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| RelA | gene/protein | UniProt:P0AG20? (strain-specific, tentative) | “activating RelA and elevating (p)ppGpp” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| SpoT | gene/protein | UniProt:P0AGB3? (strain-specific, tentative) | “(p)ppGpp… is produced by RelA or SpoT” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| toxin–antitoxin systems | pathway/module | GO:0044828 toxin-antitoxin system | “TA systems… closely associated with persister formation” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| HipA | gene/protein | UniProt:P23882? (tentative) | “HipA… phosphorylates GltX” (yuan2024molecularmechanismand pages 3-6, yuan2024molecularmechanismand pages 15-16) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| HipBA module | pathway/module | label only | “It is part of the hipBA Type II toxin antitoxin (TA) module” (yuan2024molecularmechanismand pages 3-6, yuan2024molecularmechanismand pages 15-16) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| TisB | gene/protein | UniProt:P0ACF0? (tentative) | “TisB… targets the inner membrane, resulting in depolarization and ATP depletion” (leinberger2024proteinaggregationis pages 1-2) | 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24 |
| IstR-1 | gene/protein | label only | “translation controlled… and inhibited by the RNA antitoxin IstR-1” (leinberger2024proteinaggregationis pages 1-2) | 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24 |
| HokB | gene/protein | label only | “TisB, HokB… depolarize the inner membrane” (yuan2024molecularmechanismand pages 6-7) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| MazF | gene/protein | label only | “MazF… underlie dormancy” / inhibits translation (yuan2024molecularmechanismand pages 3-6, yuan2024molecularmechanismand pages 15-16) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| RelE | gene/protein | label only | “RelE… inhibit translation” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| VapC | gene/protein | label only | “VapC… inhibit translation by cleaving rRNA/tRNA/mRNA” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| TacT | gene/protein | label only | “TacT… inhibit translation” (yuan2024molecularmechanismand pages 3-6) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| MqsRAC | pathway/module | label only | “MqsR/MqsA/MqsC inhibited T2 phage… evidence of persistence includes… reduced metabolism” (fernandezgarcia2024toxinantitoxinsystemsinduce pages 13-14) | 10.1128/spectrum.03388-23 (2024) https://doi.org/10.1128/spectrum.03388-23 |
| membrane depolarization | process | GO:0051899 membrane depolarization | “resulting in depolarization” (leinberger2024proteinaggregationis pages 1-2) | 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24 |
| proton-motive force (PMF) | process | GO:0015985 energy coupled proton transport, down electrochemical gradient | “disrupt… proton-motive force” (yuan2024molecularmechanismand pages 6-7) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| ATP depletion | process | GO:0006091 generation of precursor metabolites and energy (label-only process) | “ATP depletion”; “lower ATP… increased persister frequency” (leinberger2024proteinaggregationis pages 1-2, yuan2024molecularmechanismand pages 6-7) | 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24; 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3 |
| protein aggregation | process | GO:0070207 protein homooligomerization? (label only if uncertain) | “TisB provokes protein aggregation”; “correlates with an extended dormancy duration” (leinberger2024proteinaggregationis pages 1-2) | 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24 |
| IbpA/IbpB | gene/protein | label only | “including the chaperone genes ibpAB” (leinberger2024proteinaggregationis pages 1-2) | 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24 |
| Spy | gene/protein | label only | “including… spy” (leinberger2024proteinaggregationis pages 1-2) | 10.1128/msystems.01060-24 (2024) https://doi.org/10.1128/msystems.01060-24 |
| RMF | gene/protein | UniProt:P0A7G2? (tentative) | “RMF… trigger 100S formation” (helenabueno2024ripplinglifeon pages 3-4) | 10.3389/fmicb.2024.1386179 (2024) https://doi.org/10.3389/fmicb.2024.1386179 |
| HPF | gene/protein | label only | “HPF… hibernation factors directly block ribonucleases” (helenabueno2024ripplinglifeon pages 6-8, helenabueno2024ripplinglifeon pages 11-12) | 10.3389/fmicb.2024.1386179 (2024) https://doi.org/10.3389/fmicb.2024.1386179 |
| RaiA | gene/protein | label only | “RaiA has been shown structurally to occupy small-subunit active sites” (helenabueno2024ripplinglifeon pages 3-4) | 10.3389/fmicb.2024.1386179 (2024) https://doi.org/10.3389/fmicb.2024.1386179 |
| 100S ribosome / ribosome dimerization | pathway/module | GO:0005840 ribosome; label: 100S ribosome | “100S ribosomes—ribosome dimers” (helenabueno2024ripplinglifeon pages 3-4) | 10.3389/fmicb.2024.1386179 (2024) https://doi.org/10.3389/fmicb.2024.1386179 |
| DNA repair | process | GO:0006281 | “significant increases in transcripts for DNA repair” (imminger2024survivalandrapid pages 3-4) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| double-strand break repair | process | GO:0006302 | “notably repair of double-stranded DNA breaks” (imminger2024survivalandrapid pages 3-4) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| terminal oxidases (cytochrome bd / cytochrome c oxidases) | pathway/module | GO:0015002 heme-copper terminal oxidase activity; GO:0004129 cytochrome-c oxidase activity | “Many populations upregulated terminal oxidases (cytochrome c, cytochrome bd)” (imminger2024survivalandrapid pages 3-4) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| KatG catalase | gene/protein | UniProt:P0A5N4? KatG (tentative); EC:1.11.1.6 | “KatG removes ROS in the phase of high metabolic activity” (imminger2024survivalandrapid pages 8-9) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| catalase supplementation | assay/measurement | EC:1.11.1.6 catalase | “Addition of catalase… greatly improved the culturability” (prosdocimi2023cellphenotypechanges pages 7-10) | 10.1186/s13213-022-01703-6 (2023) https://doi.org/10.1186/s13213-022-01703-6 |
| Rpf proteins | gene/protein | label: resuscitation-promoting factor (Rpf) | “reactivate dormant bacteria at very low concentrations” (li2024resuscitationpromotionfactor pages 1-3) | 10.3390/microorganisms12081528 (2024) https://doi.org/10.3390/microorganisms12081528 |
| LysM domain | gene/protein | PFAM/InterPro label only | “Several Rpfs also carry an N-terminal LysM domain reported to bind peptidoglycan” (li2024resuscitationpromotionfactor pages 1-3) | 10.3390/microorganisms12081528 (2024) https://doi.org/10.3390/microorganisms12081528 |
| NAD+ | metabolite/chemical | CHEBI:57540 | “ATP mainly participated in synthesizing NAD+ to prompt VBNC cell resuscitation” (yang2024resuscitationofviable pages 9-10) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 |
| nadR | gene/protein | label only | “elevated expression of nadR, nadD, pncB and nadE” (yang2024resuscitationofviable pages 9-10) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 |
| nadD | gene/protein | label only | “elevated expression of nadR, nadD, pncB and nadE” (yang2024resuscitationofviable pages 9-10) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 |
| pncB | gene/protein | label only | “elevated expression of nadR, nadD, pncB and nadE” (yang2024resuscitationofviable pages 9-10) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 |
| nadE | gene/protein | label only | “elevated expression of nadR, nadD, pncB and nadE” (yang2024resuscitationofviable pages 9-10) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 |
| Preiss-Handler pathway | pathway/module | MetaCyc/KEGG label only | “ATP consumption… attributed to activation of the Preiss-Handler… pathways” (yang2024resuscitationofviable pages 9-10) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 |
| NAD salvage pathway | pathway/module | MetaCyc/KEGG label only | “activation of the… salvage pathways” (yang2024resuscitationofviable pages 9-10) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 |
| CCCP | metabolite/chemical | CHEBI:3423 | “Chemical depletion of ATP with CCCP reduced ATP levels and prevented resuscitation” (yang2024resuscitationofviable pages 6-9) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 |
| PHA storage / polyhydroxyalkanoate metabolism | pathway/module | CHEBI:53331 poly(3-hydroxyalkanoate); MetaCyc label only | “transcripts for polyhydroxy-alkanoate (PHA) metabolism increased” (imminger2024survivalandrapid pages 3-4) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| atmospheric H2 oxidation | pathway/module | GO:0044718?; label only | “H2 uptake in dry biocrusts was detected” (imminger2024survivalandrapid pages 8-9) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| group 1h [NiFe]-hydrogenase | gene/protein | EC:1.12.99.6?; label only | “group 1h [NiFe]-hydrogenases are more highly expressed in the dry state” (imminger2024survivalandrapid pages 8-9) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| group 1l [NiFe]-hydrogenase | gene/protein | EC:1.12.99.6?; label only | “group 1l [NiFe]-hydrogenases more active in hydrated states” (imminger2024survivalandrapid pages 8-9) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| NanoSIMS heavy-water activity assay | assay/measurement | label only | “heavy-water (2H2O) microcosm incubations combined with NanoSIMS imaging to track anabolic activity” (imminger2024survivalandrapid pages 11-12) | 10.1038/s41467-024-46920-6 (2024) https://doi.org/10.1038/s41467-024-46920-6 |
| culturability / plating assay | assay/measurement | label only | “cannot grow on standard media”; “culturability of VBNC cells” (yuan2024molecularmechanismand pages 3-6, prosdocimi2023cellphenotypechanges pages 7-10) | 10.1186/s12866-024-03628-3 (2024) https://doi.org/10.1186/s12866-024-03628-3; 10.1186/s13213-022-01703-6 (2023) https://doi.org/10.1186/s13213-022-01703-6 |


*Table: This table lists candidate entities for a TraitMech causal graph of microbial dormancy, grouped across environments, processes, molecules, pathways, and assays. It is useful as a node inventory with preliminary ontology grounding and direct evidence support from the cited sources.*

## 7) Evidence-backed candidate causal edges (SPO triples)

The following edges are proposed for curation; each row includes a supporting snippet and DOI-first reference.

| Edge (subject–predicate–object) | Node grounding suggestions (CURIEs where possible) | Evidence snippet (short quote) | Reference (include DOI, year, URL) | Notes/limitations |
|---|---|---|---|---|
| ENVO:desiccation/low water availability → induces → microbial dormancy-like low-activity state | ENVO:desiccation; label: dry soil phase; METPO:traitmech:000080 | “During the dry phase, transcripts for ROS protection and inorganic-energy-oriented processes were abundant” (imminger2024survivalandrapid pages 7-8) | Imminger et al. 2024, DOI:10.1038/s41467-024-46920-6, https://doi.org/10.1038/s41467-024-46920-6 | Community-level evidence from desert biocrusts; supports protective low-activity state, not direct single-gene causation. |
| rewetting/hydration → triggers resuscitation of → dormant soil microbial populations | ENVO:rainfall; ENVO:rehydration; GO:0009651 response to salt stress?; label: resuscitation | “nearly all microbial populations resuscitate within minutes after simulated rain” (imminger2024survivalandrapid pages 1-2) | Imminger et al. 2024, DOI:10.1038/s41467-024-46920-6, https://doi.org/10.1038/s41467-024-46920-6 | Strong primary evidence; community-wide and not species-specific. |
| rewetting/hydration → increases transcripts for → DNA repair | GO:0006281 DNA repair; label: double-strand break repair | “Early transcriptional responses included significant increases in transcripts for DNA repair” (imminger2024survivalandrapid pages 3-4) | Imminger et al. 2024, DOI:10.1038/s41467-024-46920-6, https://doi.org/10.1038/s41467-024-46920-6 | Good mechanistic support for early exit-from-dormancy repair program; pathway-level rather than gene-level. |
| rewetting/hydration → increases → energy generation pathways | GO:0006091 generation of precursor metabolites and energy; label: terminal oxidases; CHEBI:15339 oxygen | “Early transcriptional responses included significant increases in transcripts for… energy generation” (imminger2024survivalandrapid pages 3-4) | Imminger et al. 2024, DOI:10.1038/s41467-024-46920-6, https://doi.org/10.1038/s41467-024-46920-6 | Community-level transcript evidence. |
| (p)ppGpp stringent response → causes → slow growth or dormancy | CHEBI:63939 guanosine tetraphosphate; GO:0006950 response to stress; METPO:traitmech:000080 | “(p)ppGpp… can reprogram cellular life activities... and these changes will result in slow cell growth or dormancy” (yuan2024molecularmechanismand pages 6-7) | Yuan et al. 2024, DOI:10.1186/s12866-024-03628-3, https://doi.org/10.1186/s12866-024-03628-3 | Review synthesis, not one primary experiment; still useful as broad edge. |
| nutrient limitation/heat stress → activates → (p)ppGpp stringent response | ENVO:nutrient limitation; CHEBI:63939; label: amino acid starvation | “The stringent response mediated by (p)ppGpp is activated by nutrient/heat stresses” (yuan2024molecularmechanismand pages 6-7) | Yuan et al. 2024, DOI:10.1186/s12866-024-03628-3, https://doi.org/10.1186/s12866-024-03628-3 | Broad regulatory edge from review. |
| (p)ppGpp → upregulates → toxin–antitoxin modules | CHEBI:63939; GO:0044828 toxin-antitoxin system; label: hipAB/dinJ-yafQ/mazEF/mqsRA/relBE/hokB | “(p)ppGpp upregulates multiple TA modules (hipAB, dinJ/yafQ, mazEF, mqsRA, relBE, yafNO and hokB)” (yuan2024molecularmechanismand pages 6-7) | Yuan et al. 2024, DOI:10.1186/s12866-024-03628-3, https://doi.org/10.1186/s12866-024-03628-3 | Strong review summary; exact regulation may differ by taxon. |
| HipA toxin → phosphorylates/inhibits → GltX | UniProt:P0A9K7? HipA (label-only acceptable); UniProt:P04805 GltX?; EC:6.1.1.17 | “HipA causes antibiotic persistence via phosphorylation of glutamyl-tRNA-synthetase” (yuan2024molecularmechanismand pages 15-16) | Yuan et al. 2024, DOI:10.1186/s12866-024-03628-3, https://doi.org/10.1186/s12866-024-03628-3 | Grounding for exact accession may be strain-specific; mechanism is widely cited but summarized here in review form. |
| HipA activity → activates → RelA/(p)ppGpp pathway via uncharged tRNA accumulation | HipA; RelA; CHEBI:63939; label: uncharged tRNA | “HipA… phosphorylates GltX causing uncharged tRNA accumulation, activating RelA and elevating (p)ppGpp” (yuan2024molecularmechanismand pages 3-6) | Yuan et al. 2024, DOI:10.1186/s12866-024-03628-3, https://doi.org/10.1186/s12866-024-03628-3 | Review-derived mechanistic chain; strong literature consensus but not from a single experiment here. |
| TisB toxin → depolarizes → inner membrane | UniProt:P0ACF0? TisB label-only; GO:0005886 plasma membrane; label: proton motive force | “TisB… targets the inner membrane, resulting in depolarization” (leinberger2024proteinaggregationis pages 1-2) | Leinberger et al. 2024, DOI:10.1128/msystems.01060-24, https://doi.org/10.1128/msystems.01060-24 | Strong primary evidence in E. coli; taxon-specific. |
| TisB toxin → depletes → ATP | TisB; CHEBI:15422 ATP | “TisB… targets the inner membrane, resulting in depolarization and ATP depletion” (leinberger2024proteinaggregationis pages 1-2) | Leinberger et al. 2024, DOI:10.1128/msystems.01060-24, https://doi.org/10.1128/msystems.01060-24 | Strong primary evidence; specific to TisB-producing E. coli context. |
| TisB toxin → induces → dormancy/persister state | TisB; METPO:traitmech:000080; label: persister cell | “Toxins from chromosomal toxin-antitoxin systems have the potential to halt cell growth, induce dormancy, and eventually promote a stress-tolerant persister state” (leinberger2024proteinaggregationis pages 1-2) | Leinberger et al. 2024, DOI:10.1128/msystems.01060-24, https://doi.org/10.1128/msystems.01060-24 | Strong framing, but generalized from toxin-induction experiments. |
| HokB/TisB membrane toxins → inhibit ATP synthesis via PMF disruption → induce dormancy/persister formation | HokB; TisB; GO:0015986 ATP synthesis coupled proton transport; label: PMF | “TisB, HokB… depolarize the inner membrane, disrupt… proton-motive force that inhibits ATP synthesis, and induces bacterial dormancy and persister formation” (yuan2024molecularmechanismand pages 6-7) | Yuan et al. 2024, DOI:10.1186/s12866-024-03628-3, https://doi.org/10.1186/s12866-024-03628-3 | Review-level synthesis; supports a grouped toxin edge. |
| RelE/MazF/VapC/TacT toxins → inhibit → translation | RelE; MazF; VapC; TacT; GO:0006412 translation | “Toxins (VapC, TacT, RelE, MazF) inhibit translation by cleaving rRNA/tRNA/mRNA or modifying charged tRNAs” (yuan2024molecularmechanismand pages 3-6) | Yuan et al. 2024, DOI:10.1186/s12866-024-03628-3, https://doi.org/10.1186/s12866-024-03628-3 | Multi-toxin grouped edge from review; some mechanisms are family/member-specific. |
| TisB toxin → causes → protein aggregation | TisB; GO:0070207 protein homooligomerization?; label: protein aggregation | “Here, we show that TisB provokes protein aggregation” (leinberger2024proteinaggregationis pages 1-2) | Leinberger et al. 2024, DOI:10.1128/msystems.01060-24, https://doi.org/10.1128/msystems.01060-24 | Strong primary evidence. |
| protein aggregation → extends → dormancy duration | label: protein aggregates; METPO:traitmech:000080 | “protein aggregation… correlates with an extended dormancy duration” (leinberger2024proteinaggregationis pages 1-2) | Leinberger et al. 2024, DOI:10.1128/msystems.01060-24, https://doi.org/10.1128/msystems.01060-24 | Correlative wording; causal direction supported by study interpretation but still somewhat model-dependent. |
| RMF/HPF/RaiA hibernation factors → turn off → protein synthesis | RMF; HPF; RaiA; GO:0006412 translation; GO:0003735 structural constituent of ribosome | “Classical ribosome hibernation factors (RMF, HPF, YfiA) are documented to ‘turn off protein synthesis’” (helenabueno2024ripplinglifeon pages 11-12) | Helena-Bueno et al. 2024, DOI:10.3389/fmicb.2024.1386179, https://doi.org/10.3389/fmicb.2024.1386179 | Review but directly states mechanism. RaiA is discussed elsewhere in same review as part of HPF/RaiA family. |
| RMF/HPF/RaiA binding to ribosomes → protects → ribosomes from degradation | RMF; HPF; RaiA; GO:0005840 ribosome | “Hibernation factors directly block ribonucleases from entering the ribosome in response to starvation” (helenabueno2024ripplinglifeon pages 11-12) | Helena-Bueno et al. 2024, DOI:10.3389/fmicb.2024.1386179, https://doi.org/10.3389/fmicb.2024.1386179 | Review-level statement; protection documented across several taxa. |
| ribosome hibernation factor deletion → accelerates → rRNA decay | HPF; RaiA; RMF; GO:0006401 RNA catabolic process | “their deletion accelerates rRNA decay in dormant cells” (helenabueno2024ripplinglifeon pages 6-8) | Helena-Bueno et al. 2024, DOI:10.3389/fmicb.2024.1386179, https://doi.org/10.3389/fmicb.2024.1386179 | Negative-perturbation edge; cross-taxon summary. |
| ATP → powers → NAD+ synthesis during VBNC resuscitation | CHEBI:15422 ATP; CHEBI:57540 NAD(+); label: VBNC resuscitation | “ATP mainly participated in synthesizing NAD+ to prompt VBNC cell resuscitation” (yang2024resuscitationofviable pages 9-10) | Yang et al. 2024, DOI:10.1016/j.jare.2023.08.002, https://doi.org/10.1016/j.jare.2023.08.002 | Strong primary evidence in VBNC E. coli. |
| Preiss-Handler and salvage NAD+ pathways → promote → VBNC resuscitation | KEGG/MetaCyc label: Preiss-Handler pathway; label: NAD salvage pathway; genes: nadR, nadD, pncB, nadE | “ATP consumption during resuscitation is attributed to activation of the Preiss-Handler and salvage pathways” (yang2024resuscitationofviable pages 9-10) | Yang et al. 2024, DOI:10.1016/j.jare.2023.08.002, https://doi.org/10.1016/j.jare.2023.08.002 | Pathway-level edge with gene support; bacterial species-specific experiment. |
| CCCP-mediated ATP depletion → prevents → VBNC resuscitation | CHEBI:3423 CCCP; CHEBI:15422 ATP; label: VBNC resuscitation | “Chemical depletion of ATP with CCCP reduced ATP levels and prevented resuscitation” (yang2024resuscitationofviable pages 6-9) | Yang et al. 2024, DOI:10.1016/j.jare.2023.08.002, https://doi.org/10.1016/j.jare.2023.08.002 | Strong perturbation evidence; useful inhibitor edge. |
| hydrogen peroxide → prevents → VBNC resuscitation/culturability | CHEBI:16240 hydrogen peroxide; label: VBNC resuscitation; label: culturability | “0.007 mM… is enough to prevent cell growth” and “prevented the resuscitation (culturability) of VBNC cells” (prosdocimi2023cellphenotypechanges pages 7-10) | Prosdocimi et al. 2023, DOI:10.1186/s13213-022-01703-6, https://doi.org/10.1186/s13213-022-01703-6 | Strong primary evidence in Vibrio; strain dependence noted. |
| catalase supplementation → improves → culturability of VBNC cells | EC:1.11.1.6 catalase; CHEBI:16240 hydrogen peroxide; label: culturability | “Addition of catalase… greatly improved the culturability of the cells” (prosdocimi2023cellphenotypechanges pages 7-10) | Prosdocimi et al. 2023, DOI:10.1186/s13213-022-01703-6, https://doi.org/10.1186/s13213-022-01703-6 | Strong assay/application edge, but effect incomplete and strain-specific. |
| Rpf proteins → have → c-type lysozyme-like fold / peptidoglycan hydrolase activity | label: Rpf; LysM domain; GO:0003796 lysozyme activity?; GO:0009252 peptidoglycan biosynthetic process? | “the conserved Rpf domain adopts a c-type lysozyme fold” and “support the view that Rpfs function as peptidoglycan hydrolases” (li2024resuscitationpromotionfactor pages 1-3) | Li et al. 2024, DOI:10.3390/microorganisms12081528, https://doi.org/10.3390/microorganisms12081528 | Mechanistic inference is strong but still partly structural/biochemical hypothesis in review framing. |
| Rpf proteins → promote → resuscitation of dormant/VBNC bacteria | label: Rpf; label: dormant cell; label: VBNC state | “reactivate dormant bacteria at very low concentrations” (li2024resuscitationpromotionfactor pages 1-3) | Li et al. 2024, DOI:10.3390/microorganisms12081528, https://doi.org/10.3390/microorganisms12081528 | Strong review statement based on accumulated studies. |
| Rpf supplementation → enables isolation/recovery of → dormant or VBNC bacteria | label: Rpf supplementation; label: isolation/cultivation; label: VBNC bacteria | “adding Rpf to culture media to induce resuscitation prior to cultivation” (li2024resuscitationpromotionfactor pages 1-3) | Li et al. 2024, DOI:10.3390/microorganisms12081528, https://doi.org/10.3390/microorganisms12081528 | Practical application edge; useful for assay/experimental-factor nodes. |
| Rpf or rpf-like genes/application → enhances → bioremediation functionality | label: Rpf; label: bioremediation; label: nitrification/denitrification | “Rpf supplementation resuscitated Pseudomonas sp. SSPR1, restoring simultaneous nitrification and denitrification” (hou2024exploringthedistribution pages 1-2) | Hou et al. 2024, DOI:10.3389/fmicb.2024.1433046, https://doi.org/10.3389/fmicb.2024.1433046 | Applied edge; may be ecosystem- and taxon-specific. |


*Table: This table lists evidence-backed candidate subject–predicate–object edges for curating a microbial dormancy TraitMech graph. It emphasizes recent mechanistic evidence, grounding suggestions, and limitations so curators can prioritize robust versus context-specific claims.*

## 8) Expert interpretation & analysis (authoritative synthesis)

### 8.1 Dormancy as “energy allocation + machinery protection”
Across recent sources, dormancy can be framed as coordinated control over: (i) **energetic state** (ATP availability, PMF, NAD/NADH), (ii) **translation/transcription competence** (ribosome and RNAP hibernation), and (iii) **damage control** (DNA repair, ROS detox). Environmental triggers (desiccation/rewetting) appear to elicit a stereotyped early response emphasizing **repair and energy generation** rather than immediate division, consistent with a seed-bank strategy. (imminger2024survivalandrapid pages 3-4, imminger2024survivalandrapid pages 1-2, helenabueno2024ripplinglifeon pages 1-3)

### 8.2 Dormancy depth and assay dependence (persister vs VBNC)
The persister/VBNC review explicitly notes that VBNC and persisters may reflect **different dormancy depths** and that culturability can be suppressed by environmental/assay factors (e.g., oxidative stress), suggesting that TraitMech edges should represent both **physiological state** and **measurement context** (culturability assays; antioxidant supplementation). (yuan2024molecularmechanismand pages 3-6, prosdocimi2023cellphenotypechanges pages 7-10)

### 8.3 Curation-relevant modularity
The evidence supports at least three reusable mechanistic modules:
1. **Stress → (p)ppGpp → TA induction → translation arrest/ATP downshift → dormancy** (broad but context-specific). (yuan2024molecularmechanismand pages 6-7, yuan2024molecularmechanismand pages 3-6)
2. **Membrane toxin (TisB/HokB) → PMF collapse → ATP depletion → dormancy/persistence** (strong in *E. coli* and review-supported). (leinberger2024proteinaggregationis pages 1-2, yuan2024molecularmechanismand pages 6-7)
3. **Resuscitation module:** (a) **rewetting → rapid repair/energy generation** (soil) and (b) **ATP → NAD+ synthesis (Preiss-Handler/salvage) → VBNC resuscitation** (lab VBNC *E. coli*). (imminger2024survivalandrapid pages 3-4, yang2024resuscitationofviable pages 9-10)

## 9) Warnings / claims to treat as uncertain (not yet curate or curate with qualifiers)

1. **Taxon specificity:** Many TA and hibernation-factor effects are strain- and species-dependent; edges like “(p)ppGpp upregulates TA modules” should be curated as broadly conserved **only with qualifiers** (bacteria; many taxa; not universal). (yuan2024molecularmechanismand pages 6-7, yuan2024molecularmechanismand pages 7-9)
2. **Rpf biochemical mechanism:** Rpf’s lysozyme-like fold and catalytic features support a peptidoglycan hydrolase model, but some parts remain **mechanistic inference** and may require direct biochemical confirmation in the target taxa before asserting specific bond-cleavage reactions. (li2024resuscitationpromotionfactor pages 1-3, li2024resuscitationpromotionfactor pages 3-6)
3. **Protein aggregation causality:** Leinberger et al. show aggregation correlates with extended dormancy duration in TisB contexts; treat “aggregation → extended dormancy” as **supported but still partially model-dependent** (correlation vs necessity/sufficiency across taxa). (leinberger2024proteinaggregationis pages 1-2)
4. **VBNC vs persister conceptual mapping:** The “dormancy depth” continuum is a useful framing, but it is not universally operationalized; curate cross-links between VBNC and persisters with care. (yuan2024molecularmechanismand pages 3-6)

## 10) DOI-first bibliography (with dates/URLs where available)

- Imminger S, Meier DV, Schintlmeister A, et al. **Survival and rapid resuscitation permit limited productivity in desert microbial communities.** *Nature Communications.* **Apr 2024**. DOI:10.1038/s41467-024-46920-6. https://doi.org/10.1038/s41467-024-46920-6 (imminger2024survivalandrapid pages 3-4, imminger2024survivalandrapid pages 2-3, imminger2024survivalandrapid pages 1-2)
- Yuan S, Shen Y, Quan Y, et al. **Molecular mechanism and application of emerging technologies in study of bacterial persisters.** *BMC Microbiology.* **Nov 2024**. DOI:10.1186/s12866-024-03628-3. https://doi.org/10.1186/s12866-024-03628-3 (yuan2024molecularmechanismand pages 3-6, yuan2024molecularmechanismand pages 6-7)
- Leinberger FH, Cassidy L, Edelmann D, et al. **Protein aggregation is a consequence of the dormancy-inducing membrane toxin TisB in *Escherichia coli*.** *mSystems.* **Nov 2024**. DOI:10.1128/msystems.01060-24. https://doi.org/10.1128/msystems.01060-24 (leinberger2024proteinaggregationis pages 1-2)
- Helena-Bueno K, Chan LI, Melnikov SV. **Rippling life on a dormant planet: hibernation of ribosomes, RNA polymerases, and other essential enzymes.** *Frontiers in Microbiology.* **May 2024**. DOI:10.3389/fmicb.2024.1386179. https://doi.org/10.3389/fmicb.2024.1386179 (helenabueno2024ripplinglifeon pages 11-12, helenabueno2024ripplinglifeon media 60e87f11)
- Yang D, Wang W, Zhao L, Rao L, Liao X. **Resuscitation of viable but nonculturable bacteria promoted by ATP-mediated NAD+ synthesis.** *Journal of Advanced Research.* **Jun 2024**. DOI:10.1016/j.jare.2023.08.002. https://doi.org/10.1016/j.jare.2023.08.002 (yang2024resuscitationofviable pages 6-9, yang2024resuscitationofviable pages 9-10)
- Li X, Ren Q, Sun Z, Wu Y, Pan H. **Resuscitation Promotion Factor: A Pronounced Bacterial Cytokine in Propelling Bacterial Resuscitation.** *Microorganisms.* **Jul 2024**. DOI:10.3390/microorganisms12081528. https://doi.org/10.3390/microorganisms12081528 (li2024resuscitationpromotionfactor pages 1-3)
- Hou A, Fu H, Liu L, et al. **Exploring the distribution and co-occurrence of rpf-like genes and nitrogen-cycling genes in water reservoir sediments.** *Frontiers in Microbiology.* **Jul 2024**. DOI:10.3389/fmicb.2024.1433046. https://doi.org/10.3389/fmicb.2024.1433046 (hou2024exploringthedistribution pages 1-2)
- Prosdocimi EM, Arioli S, Mapelli F, et al. **Cell phenotype changes and oxidative stress response in Vibrio spp. induced into viable but non-culturable (VBNC) state.** *Annals of Microbiology.* **Jan 2023**. DOI:10.1186/s13213-022-01703-6. https://doi.org/10.1186/s13213-022-01703-6 (prosdocimi2023cellphenotypechanges pages 7-10)

---

## Figure/table evidence (for curator validation)

A supporting quantitative table for ribosome hibernation factor copy numbers (active vs stationary phase in *E. coli*) was extracted from the ribosome-hibernation review. (helenabueno2024ripplinglifeon media 60e87f11)


References

1. (yuan2024molecularmechanismand pages 3-6): Shuo Yuan, Yamin Shen, Yingying Quan, Shuji Gao, Jing Zuo, Wenjie Jin, Rishun Li, Li Yi, Yuxin Wang, and Yang Wang. Molecular mechanism and application of emerging technologies in study of bacterial persisters. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03628-3, doi:10.1186/s12866-024-03628-3. This article has 20 citations and is from a peer-reviewed journal.

2. (prosdocimi2023cellphenotypechanges pages 7-10): Erica M. Prosdocimi, Stefania Arioli, Francesca Mapelli, Zahraa Zeaiter, Marco Fusi, Daniele Daffonchio, Sara Borin, and Elena Crotti. Cell phenotype changes and oxidative stress response in vibrio spp. induced into viable but non-culturable (vbnc) state. Annals of Microbiology, 73:1-13, Jan 2023. URL: https://doi.org/10.1186/s13213-022-01703-6, doi:10.1186/s13213-022-01703-6. This article has 10 citations and is from a peer-reviewed journal.

3. (helenabueno2024ripplinglifeon pages 1-3): Karla Helena-Bueno, Lewis I. Chan, and Sergey V. Melnikov. Rippling life on a dormant planet: hibernation of ribosomes, rna polymerases, and other essential enzymes. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1386179, doi:10.3389/fmicb.2024.1386179. This article has 22 citations and is from a peer-reviewed journal.

4. (yuan2024molecularmechanismand pages 7-9): Shuo Yuan, Yamin Shen, Yingying Quan, Shuji Gao, Jing Zuo, Wenjie Jin, Rishun Li, Li Yi, Yuxin Wang, and Yang Wang. Molecular mechanism and application of emerging technologies in study of bacterial persisters. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03628-3, doi:10.1186/s12866-024-03628-3. This article has 20 citations and is from a peer-reviewed journal.

5. (imminger2024survivalandrapid pages 3-4): Stefanie Imminger, Dimitri V. Meier, Arno Schintlmeister, Anton Legin, Jörg Schnecker, Andreas Richter, Osnat Gillor, Stephanie A. Eichorst, and Dagmar Woebken. Survival and rapid resuscitation permit limited productivity in desert microbial communities. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46920-6, doi:10.1038/s41467-024-46920-6. This article has 47 citations and is from a highest quality peer-reviewed journal.

6. (imminger2024survivalandrapid pages 1-2): Stefanie Imminger, Dimitri V. Meier, Arno Schintlmeister, Anton Legin, Jörg Schnecker, Andreas Richter, Osnat Gillor, Stephanie A. Eichorst, and Dagmar Woebken. Survival and rapid resuscitation permit limited productivity in desert microbial communities. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46920-6, doi:10.1038/s41467-024-46920-6. This article has 47 citations and is from a highest quality peer-reviewed journal.

7. (imminger2024survivalandrapid pages 2-3): Stefanie Imminger, Dimitri V. Meier, Arno Schintlmeister, Anton Legin, Jörg Schnecker, Andreas Richter, Osnat Gillor, Stephanie A. Eichorst, and Dagmar Woebken. Survival and rapid resuscitation permit limited productivity in desert microbial communities. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46920-6, doi:10.1038/s41467-024-46920-6. This article has 47 citations and is from a highest quality peer-reviewed journal.

8. (yuan2024molecularmechanismand pages 6-7): Shuo Yuan, Yamin Shen, Yingying Quan, Shuji Gao, Jing Zuo, Wenjie Jin, Rishun Li, Li Yi, Yuxin Wang, and Yang Wang. Molecular mechanism and application of emerging technologies in study of bacterial persisters. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03628-3, doi:10.1186/s12866-024-03628-3. This article has 20 citations and is from a peer-reviewed journal.

9. (yuan2024molecularmechanismand pages 15-16): Shuo Yuan, Yamin Shen, Yingying Quan, Shuji Gao, Jing Zuo, Wenjie Jin, Rishun Li, Li Yi, Yuxin Wang, and Yang Wang. Molecular mechanism and application of emerging technologies in study of bacterial persisters. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03628-3, doi:10.1186/s12866-024-03628-3. This article has 20 citations and is from a peer-reviewed journal.

10. (leinberger2024proteinaggregationis pages 1-2): Florian H. Leinberger, Liam Cassidy, Daniel Edelmann, Nicole E. Schmid, Markus Oberpaul, Patrick Blumenkamp, Sebastian Schmidt, Ana Natriashvili, Maximilian H. Ulbrich, Andreas Tholey, Hans-Georg Koch, and Bork A. Berghoff. Protein aggregation is a consequence of the dormancy-inducing membrane toxin tisb in <i>escherichia coli</i>. Nov 2024. URL: https://doi.org/10.1128/msystems.01060-24, doi:10.1128/msystems.01060-24. This article has 14 citations and is from a peer-reviewed journal.

11. (helenabueno2024ripplinglifeon pages 11-12): Karla Helena-Bueno, Lewis I. Chan, and Sergey V. Melnikov. Rippling life on a dormant planet: hibernation of ribosomes, rna polymerases, and other essential enzymes. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1386179, doi:10.3389/fmicb.2024.1386179. This article has 22 citations and is from a peer-reviewed journal.

12. (helenabueno2024ripplinglifeon pages 8-9): Karla Helena-Bueno, Lewis I. Chan, and Sergey V. Melnikov. Rippling life on a dormant planet: hibernation of ribosomes, rna polymerases, and other essential enzymes. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1386179, doi:10.3389/fmicb.2024.1386179. This article has 22 citations and is from a peer-reviewed journal.

13. (helenabueno2024ripplinglifeon media 60e87f11): Karla Helena-Bueno, Lewis I. Chan, and Sergey V. Melnikov. Rippling life on a dormant planet: hibernation of ribosomes, rna polymerases, and other essential enzymes. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1386179, doi:10.3389/fmicb.2024.1386179. This article has 22 citations and is from a peer-reviewed journal.

14. (yang2024resuscitationofviable pages 6-9): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

15. (yang2024resuscitationofviable pages 9-10): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

16. (li2024resuscitationpromotionfactor pages 1-3): Xinxin Li, Qing Ren, Zhanbin Sun, Yanan Wu, and Hanxu Pan. Resuscitation promotion factor: a pronounced bacterial cytokine in propelling bacterial resuscitation. Microorganisms, 12:1528, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081528, doi:10.3390/microorganisms12081528. This article has 10 citations.

17. (hou2024exploringthedistribution pages 1-2): Aiqin Hou, Huayi Fu, Leilei Liu, Xiaomei Su, Shusheng Zhang, J.J.L. Lai., and Faqian Sun. Exploring the distribution and co-occurrence of rpf-like genes and nitrogen-cycling genes in water reservoir sediments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1433046, doi:10.3389/fmicb.2024.1433046. This article has 9 citations and is from a peer-reviewed journal.

18. (imminger2024survivalandrapid pages 7-8): Stefanie Imminger, Dimitri V. Meier, Arno Schintlmeister, Anton Legin, Jörg Schnecker, Andreas Richter, Osnat Gillor, Stephanie A. Eichorst, and Dagmar Woebken. Survival and rapid resuscitation permit limited productivity in desert microbial communities. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46920-6, doi:10.1038/s41467-024-46920-6. This article has 47 citations and is from a highest quality peer-reviewed journal.

19. (prosdocimi2023cellphenotypechanges pages 1-2): Erica M. Prosdocimi, Stefania Arioli, Francesca Mapelli, Zahraa Zeaiter, Marco Fusi, Daniele Daffonchio, Sara Borin, and Elena Crotti. Cell phenotype changes and oxidative stress response in vibrio spp. induced into viable but non-culturable (vbnc) state. Annals of Microbiology, 73:1-13, Jan 2023. URL: https://doi.org/10.1186/s13213-022-01703-6, doi:10.1186/s13213-022-01703-6. This article has 10 citations and is from a peer-reviewed journal.

20. (fernandezgarcia2024toxinantitoxinsystemsinduce pages 13-14): Laura Fernández-García, Sooyeon Song, Joy Kirigo, Michael E. Battisti, Maiken E. Petersen, María Tomás, and Thomas K. Wood. Toxin/antitoxin systems induce persistence and work in concert with restriction/modification systems to inhibit phage. Jan 2024. URL: https://doi.org/10.1128/spectrum.03388-23, doi:10.1128/spectrum.03388-23. This article has 25 citations and is from a domain leading peer-reviewed journal.

21. (helenabueno2024ripplinglifeon pages 3-4): Karla Helena-Bueno, Lewis I. Chan, and Sergey V. Melnikov. Rippling life on a dormant planet: hibernation of ribosomes, rna polymerases, and other essential enzymes. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1386179, doi:10.3389/fmicb.2024.1386179. This article has 22 citations and is from a peer-reviewed journal.

22. (helenabueno2024ripplinglifeon pages 6-8): Karla Helena-Bueno, Lewis I. Chan, and Sergey V. Melnikov. Rippling life on a dormant planet: hibernation of ribosomes, rna polymerases, and other essential enzymes. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1386179, doi:10.3389/fmicb.2024.1386179. This article has 22 citations and is from a peer-reviewed journal.

23. (imminger2024survivalandrapid pages 8-9): Stefanie Imminger, Dimitri V. Meier, Arno Schintlmeister, Anton Legin, Jörg Schnecker, Andreas Richter, Osnat Gillor, Stephanie A. Eichorst, and Dagmar Woebken. Survival and rapid resuscitation permit limited productivity in desert microbial communities. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46920-6, doi:10.1038/s41467-024-46920-6. This article has 47 citations and is from a highest quality peer-reviewed journal.

24. (imminger2024survivalandrapid pages 11-12): Stefanie Imminger, Dimitri V. Meier, Arno Schintlmeister, Anton Legin, Jörg Schnecker, Andreas Richter, Osnat Gillor, Stephanie A. Eichorst, and Dagmar Woebken. Survival and rapid resuscitation permit limited productivity in desert microbial communities. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46920-6, doi:10.1038/s41467-024-46920-6. This article has 47 citations and is from a highest quality peer-reviewed journal.

25. (li2024resuscitationpromotionfactor pages 3-6): Xinxin Li, Qing Ren, Zhanbin Sun, Yanan Wu, and Hanxu Pan. Resuscitation promotion factor: a pronounced bacterial cytokine in propelling bacterial resuscitation. Microorganisms, 12:1528, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081528, doi:10.3390/microorganisms12081528. This article has 10 citations.