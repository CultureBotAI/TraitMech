---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:14:34.468112'
end_time: '2026-08-04T02:21:26.514329'
duration_seconds: 412.05
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: oxygen preference
  trait_identifier: METPO:1000601
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: oxygen_preference
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that is relating to an organism's oxygen requirements or
    tolerance for growth.
  parent_traits: METPO:1000059
  synonyms: Physiology and metabolism.oxygen tolerance.oxygen tolerance, metabolism
  evidence_summary: 'PMID:21413255: aerobes require molecular oxygen as a terminal
    electron acceptor (Medical Microbiology chapter supports molecular oxygen as the
    environmental axis defining oxygen-preference phenotypes.) | DOI:10.1016/j.bbabio.2011.06.016:
    respiratory quinol:O2 oxidoreductase (Aerobic respiration review supports terminal
    oxidases as the enzymatic interface between cells and ambient O2.)'
  causal_graph_summary: 'oxygen_preference_o2_availability_axis: 14 nodes, 11 edges'
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
- **Trait label:** oxygen preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000601
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's oxygen requirements or tolerance for growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.oxygen tolerance.oxygen tolerance, metabolism
- **Existing evidence:** PMID:21413255: aerobes require molecular oxygen as a terminal electron acceptor (Medical Microbiology chapter supports molecular oxygen as the environmental axis defining oxygen-preference phenotypes.) | DOI:10.1016/j.bbabio.2011.06.016: respiratory quinol:O2 oxidoreductase (Aerobic respiration review supports terminal oxidases as the enzymatic interface between cells and ambient O2.)
- **Existing causal graph summary:** oxygen_preference_o2_availability_axis: 14 nodes, 11 edges

## Research Objective

Research the microbial trait **oxygen preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/oxygen_preference.yaml`.

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
- **Trait label:** oxygen preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000601
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's oxygen requirements or tolerance for growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.oxygen tolerance.oxygen tolerance, metabolism
- **Existing evidence:** PMID:21413255: aerobes require molecular oxygen as a terminal electron acceptor (Medical Microbiology chapter supports molecular oxygen as the environmental axis defining oxygen-preference phenotypes.) | DOI:10.1016/j.bbabio.2011.06.016: respiratory quinol:O2 oxidoreductase (Aerobic respiration review supports terminal oxidases as the enzymatic interface between cells and ambient O2.)
- **Existing causal graph summary:** oxygen_preference_o2_availability_axis: 14 nodes, 11 edges

## Research Objective

Research the microbial trait **oxygen preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/oxygen_preference.yaml`.

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


# Curation-focused research report: microbial oxygen preference

## 1. Scope and recommended interpretation

**Target trait:** oxygen preference  
**Identifier:** **METPO:1000601**  
**Category/kind:** ENVIRONMENT / CLASS  
**Reviewed definition:** “A phenotype that is relating to an organism's oxygen requirements or tolerance for growth.”

For TraitMech, oxygen preference should be modeled primarily as an **observed growth phenotype along an environmental O2-availability/concentration axis**, rather than as the mere presence of an O2-reactive enzyme. Operational states include obligate aerobic, microaerophilic, facultatively anaerobic, aerotolerant anaerobic, and obligately anaerobic growth. The phenotype is conditional on O2 concentration, exposure duration, medium, electron donors and alternative acceptors, redox state, temperature, pressure, and growth phase.

The central mechanistic balance is:

1. **Benefit:** O2 serves as a high-potential terminal electron acceptor, enabling respiratory energy conservation.
2. **Cost:** O2 directly damages oxygen-labile enzymes and indirectly produces reactive oxygen species (ROS).
3. **Adaptation:** terminal oxidases, oxygen sensors, metabolic switching, O2-reducing enzymes, and ROS-defense systems alter the O2 range over which growth remains possible.

This framing is preferable to a strict aerobic/anaerobic binary. Microorganisms can respire O2 at nanomolar concentrations, and aerobic and anaerobic respiration can coexist up to at least 25 µM O2. The estimated theoretical lower limit for aerobic respiration ranges from approximately 0.1 nM to several hundred nanomolar depending on cell size and growth efficiency. High-affinity oxidases are preferentially expressed below roughly 1–10 µM O2. (berg2022howlowcan pages 5-7)

### Boundary cases

- **Oxygen utilization is not automatically oxygen preference.** Anaerobes may express O2-reducing enzymes solely for detoxification.
- **Oxygen tolerance is not aerobic growth.** Survival after air exposure, ROS resistance, or reversible inhibition should not be curated as growth in O2 unless biomass increase or cell division was measured.
- **Microaerophily is not simply possession of cytochrome bd or cbb3 oxidase.** High-affinity oxidases support low-O2 respiration, but their genes also occur in facultative organisms and may serve stress-defense functions.
- **Aerotolerance differs from facultative anaerobiosis.** Aerotolerant organisms survive or grow fermentatively in O2 without using it as the terminal acceptor; facultative anaerobes can switch between aerobic and anaerobic energy metabolism.
- **Obligate anaerobiosis is graded.** Some nominal obligate anaerobes grow at low O2 or endure substantial transient exposure. Reported examples range from a 0.02–0.04% O2 preference in *Desulfovibrio vulgaris* to microoxic growth or tolerance at considerably higher concentrations in selected clostridia and archaea. (lu2021whenanaerobesencounter pages 3-4)
- **Assay atmosphere is not dissolved O2.** Headspace percentage, dissolved concentration, redox potential, and diffusion geometry must be stored separately.

## 2. Candidate causal-graph nodes

### A. Trait and phenotype nodes

- oxygen preference — **METPO:1000601**
- obligate aerobic growth — label-only pending verified phenotype CURIE
- microaerophilic growth — label-only
- facultative anaerobic growth — label-only
- aerotolerant anaerobic growth — label-only
- obligate anaerobic growth — label-only
- oxygen tolerance/survival — label-only; keep separate from growth preference
- oxygen-inhibited metabolic activity — label-only

### B. Environmental and experimental factors

- dioxygen — **CHEBI:15379**
- O2 availability; dissolved O2 concentration; O2 partial pressure — label-only measurement/context nodes
- oxic, microoxic/hypoxic, and anoxic environment — use ENVO terms only after identifier verification
- duration and periodicity of O2 exposure
- medium redox potential
- electron-donor availability
- alternative electron acceptors: nitrate, fumarate, sulfate and related compounds; ground individual chemicals only after validation
- temperature, pH, hydrostatic pressure, agitation, gas-transfer rate, biofilm diffusion, cell density, and growth phase
- inhibitors: cyanide, carbon monoxide, sulfide, nitric oxide; context modifiers rather than universal determinants

### C. Chemicals and metabolites

- water — **CHEBI:15377**
- superoxide — **CHEBI:18421**
- hydrogen peroxide — **CHEBI:16240**
- hydroxyl radical — label/CHEBI grounding to verify
- quinol/quinone pool — label-only unless the specific ubiquinone or menaquinone species is known
- NADH/NAD+ redox pair — individual CHEBI identifiers should be verified during YAML curation
- ATP and proton-motive force — label-only here

### D. Pathways and biological processes

- aerobic respiration — **GO:0009060**
- anaerobic respiration — **GO:0009061**
- fermentation — GO identifier should be verified for the intended granularity
- oxidative phosphorylation
- electron-transport chain
- proton-motive-force generation
- ROS detoxification/oxidative-stress response
- repair of oxidized proteins and damaged Fe–S clusters
- metabolic switching between respiration and fermentation

Aerobic respiration is energetically favorable: the reviewed estimate for glucose oxidation is −2,870 kJ mol−1, with an illustrative 50% energy-conservation assumption, compared with 30% for denitrification. These values explain selection for O2 scavenging but are modeling assumptions, not universal cellular yields. (berg2022howlowcan pages 5-7)

### E. Complexes, enzymes, and molecular functions

**Respiratory/O2-reducing systems**

- cytochrome bd quinol oxidase; CydA/CydB and taxon-specific accessory subunits
- cbb3-type cytochrome-c oxidase; CcoNOQP
- aa3-type and bo3-type terminal oxidases
- cytochrome-c oxidase activity — **GO:0004129**
- rubredoxin:oxygen oxidoreductase
- flavodiiron proteins (Fdp)
- rubrerythrins and reverse rubrerythrins
- NADH dehydrogenases and quinone pool
- ATP synthase

**O2/ROS-sensitive metabolic enzymes**

- pyruvate:ferredoxin oxidoreductase (PFOR)
- pyruvate formate-lyase (PFL)
- fumarase and other labile Fe–S enzymes
- oxygen-sensitive ribonucleotide reductases
- nitrogenase and methanogenesis enzymes where taxonomically relevant

**Defense functions**

- superoxide dismutase activity — **GO:0004784**
- catalase activity — **GO:0004096**
- peroxidase activity
- superoxide reductase
- thioredoxin/peroxiredoxin systems
- protein and Fe–S-cluster repair systems

### F. Regulators and sensors

Candidate regulatory nodes include FNR-family [4Fe–4S] O2 sensors, FixLJ heme-based O2 sensing, ArcAB respiratory/redox sensing, OxyR peroxide sensing, Rex NADH/NAD+ sensing, Spx-family oxidative-stress regulation, and alternative sigma factors such as σB. These should initially be curated as **taxon-specific regulatory branches**, not universal components. Evidence supports FNR-mediated anaerobic-respiration control and pathogen-specific relationships between oxygen availability, respiratory-chain composition, and colonization. (andre2021theselectiveadvantage pages 7-8)

## 3. Priority causal structure

The following compact table summarizes the graph backbone.

| subject | predicate | object | evidence strength/scope |
|---|---|---|---|
| CHEBI:15379 dioxygen (O2) availability | enables | GO:0009060 aerobic respiration | Strong, broad across microbes; trait-defining axis for aerobes vs anaerobes (berg2022howlowcan pages 5-7) |
| terminal oxidases (e.g., cytochrome bd, heme-copper oxidases) | reduces | CHEBI:15379 dioxygen (O2) to CHEBI:15377 water | Strong, broad but enzyme-class level; foundational respiratory mechanism (lu2021whenanaerobesencounter pages 16-17) |
| terminal oxidases | contributes_to | proton motive force generation | Moderate, broad; mechanism varies by oxidase architecture and chain context (lu2021whenanaerobesencounter pages 4-6) |
| low O2 / microoxic conditions | increases use/expression of | high-affinity terminal oxidases | Strong, broad ecological pattern; high-affinity oxidases enriched/transcribed under low O2 (berg2022howlowcan pages 5-7) |
| CHEBI:15379 dioxygen (O2) exposure | inhibits | pyruvate:ferredoxin oxidoreductase (PFOR) | Strong, but taxon/enzyme-context specific for anaerobes; concentration-dependent inactivation reported (lu2021whenanaerobesencounter pages 8-9) |
| CHEBI:15379 dioxygen (O2) exposure | inactivates | pyruvate formate-lyase (PFL) | Strong, broad for radical PFL-containing anaerobes; direct O2 toxicity mechanism (lu2021whenanaerobesencounter pages 4-6) |
| reactive oxygen species (ROS) | damages | DNA, RNA, proteins, and lipids | Strong, broad; canonical oxidative-stress mechanism affecting growth/tolerance (berg2022howlowcan pages 5-7) |
| GO:0004784 superoxide dismutase activity | detoxifies | CHEBI:18421 superoxide | Strong, broad; in recent anammox comparison, higher SOD associated with greater O2 tolerance (taxon-specific quantitative support) (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 11-12) |
| GO:0004096 catalase activity / peroxidase activity | detoxifies | CHEBI:16240 hydrogen peroxide | Strong, broad at functional level; recent anammox data support Cat contribution with SOD-Cat system (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 11-12) |
| Clostridioides difficile FdpA | promotes tolerance to | 0.4-1% O2 | Strong, taxon-specific experimental evidence; range-specific role in an obligate anaerobe (caulat2024physiologicalroleand pages 1-2) |
| Clostridioides difficile revRbr1 / revRbr2 / FdpF | promotes tolerance to | distinct O2 ranges (<0.4%, 0.1-4%, >4%/air respectively) | Strong, taxon-specific experimental evidence; range partitioning of O2 defense functions (caulat2024physiologicalroleand pages 1-2) |
| GO:0009061 anaerobic respiration / fermentation | enables | growth under anoxic conditions | Strong, broad; central route for anaerobes when O2 is absent, with coexistence of anaerobic and aerobic processes in low-O2 systems (berg2022howlowcan pages 5-7, lu2021whenanaerobesencounter pages 4-6) |


*Table: This table lists the highest-priority candidate causal edges for curating microbial oxygen preference, emphasizing broad mechanisms first and clearly flagging taxon-specific edges. It is useful as a compact starting set for TraitMech graph construction and evidence triage.*

## 4. Evidence-backed candidate edges

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| O2 availability | enables | aerobic respiration | Berg et al.: O2 respiration occurs over a wide concentration range and can persist at nanomolar O2. DOI: [10.1093/femsre/fuac006](https://doi.org/10.1093/femsre/fuac006). (berg2022howlowcan pages 5-7) | **Strong/general.** Add assay/context qualifiers rather than a universal concentration threshold. |
| terminal oxidase | catalyzes reduction of | O2 to water | Lu and Imlay describe cytochrome bd and rubredoxin oxidases as O2-reducing systems; membrane electron-transport chains can generate proton motive force. DOI: [10.1038/s41579-021-00583-y](https://doi.org/10.1038/s41579-021-00583-y). (lu2021whenanaerobesencounter pages 16-17, lu2021whenanaerobesencounter pages 4-6) | **Strong/general at class level.** Distinguish quinol versus cytochrome-c donors and oxidase family. |
| low O2 concentration | promotes expression/use of | high-affinity terminal oxidases | “High-affinity terminal oxidases … are more highly transcribed in low-O2 environments (<1–10 μmol O2 L−1).” (berg2022howlowcan pages 5-7) | **Strong ecological association.** “Promotes expression” may require regulator-specific experiments; otherwise use `associated_with_increased_expression`. |
| high-affinity terminal oxidase | enables | respiration under microoxic/apparently anoxic conditions | Respiration at extremely low O2 is widespread; theoretical minima span 0.1 to several hundred nM. (berg2022howlowcan pages 5-7) | **Strong but context-dependent.** Do not assign one affinity threshold to all bd or cbb3 enzymes. |
| terminal-oxidase electron transport | generates | proton motive force | Membrane-bound O2-directed chains generate proton motive force through conventional charge translocation. (lu2021whenanaerobesencounter pages 4-6) | **Strong pathway edge.** Exact coupling stoichiometry is oxidase/chain dependent. |
| O2 exposure | directly inactivates | PFL | PFL is inactivated “in seconds” because O2 reacts with its glycyl radical, producing peroxyl-radical chemistry and protein-backbone cleavage. (lu2021whenanaerobesencounter pages 4-6) | **Strong mechanistic edge** for radical PFL-containing organisms. |
| O2 concentration | increases inactivation of | PFOR | In *Bacteroides thetaiotaomicron*, aeration blocks fermentation; PFOR shows little loss at ≤5% O2 but requires tens of minutes for full inactivation at higher O2. (lu2021whenanaerobesencounter pages 8-9) | **Taxon/enzyme-specific.** Do not generalize the numerical threshold. |
| O2-dependent PFOR/PFL/fumarase inhibition | decreases | fermentative growth | Aeration stopped glucose consumption and growth in *B. thetaiotaomicron*; growth resumed after anoxia was restored. (lu2021whenanaerobesencounter pages 8-9) | **Strong, reversible, taxon-specific causal chain.** |
| ROS | damages | nucleic acids, proteins, lipids and redox-sensitive enzymes | Unprotected O2 exposure causes ROS damage and damages redox-sensitive anaerobic enzymes. (berg2022howlowcan pages 5-7) | **Strong/general**, but keep direct O2 damage distinct from ROS-mediated damage. |
| superoxide dismutase | converts/detoxifies | superoxide | Marine “Ca. *Scalindua* sp.” had SOD activity of 22.6 ± 1.9 U mg-protein−1 and greater O2 tolerance than freshwater anammox taxa lacking SOD activity. DOI: [10.1038/s43705-023-00251-7](https://doi.org/10.1038/s43705-023-00251-7). (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 11-12) | **Biochemistry strong; phenotype link correlational/taxon-specific.** Avoid asserting SOD alone is sufficient. |
| catalase/peroxidase | detoxifies | hydrogen peroxide | *Scalindua* had catalase activity of 1.6 ± 0.7 U mg-protein−1; the authors proposed a SOD–catalase system contributing to higher tolerance. (okabe2023oxygentoleranceand pages 1-2) | **Moderate phenotype edge.** No knockout confirmation in this study. |
| SOD–catalase defense | increases | anammox O2 tolerance | *Scalindua*: IC50 18.0 µM and DOmax 51.6 µM; freshwater taxa: IC50 2.7–4.2 µM and DOmax 10.9–26.6 µM. (okabe2023oxygentoleranceand pages 1-2) | **Uncertain causal attribution.** Quantitative association across taxa, not direct genetic perturbation. |
| FdpA | promotes | *C. difficile* growth/tolerance at 0.4–1% O2 | An `fdpA` mutant had reduced growth specifically at 0.4% O2; FdpA acts across approximately 0.4–1% O2. DOI: [10.1128/mbio.01591-24](https://doi.org/10.1128/mbio.01591-24). (caulat2024physiologicalroleand pages 1-2) | **Strong, taxon-specific perturbation.** Suitable for a *C. difficile* subgraph. |
| revRbr2 | promotes | *C. difficile* tolerance below 0.4% O2 | revRbr2 was reported as specific to low O2 tensions below 0.4%. (caulat2024physiologicalroleand pages 1-2) | **Strong/taxon-specific**, but retain assay conditions. |
| revRbr1 | promotes | *C. difficile* tolerance across 0.1–4% O2 | revRbr1 showed a wider activity spectrum of approximately 0.1–4% O2. (caulat2024physiologicalroleand pages 1-2) | **Strong/taxon-specific.** |
| FdpF | promotes | *C. difficile* tolerance above 4% O2 and in air | FdpF was most relevant above 4% O2 and in air; its mutant was not impaired below 0.4%. (caulat2024physiologicalroleand pages 1-2) | **Strong/taxon-specific.** Do not elevate to a universal Fdp property. |
| alternative anaerobic respiration/fermentation | enables | anoxic growth | Anaerobic nitrate and sulfate reduction may coexist with aerobic respiration up to at least 25 µM O2. (berg2022howlowcan pages 5-7) | **Strong/general concept.** Ground each acceptor pathway separately in taxon-specific graphs. |
| O2-directed respiratory/detoxification systems | increases | low-O2 growth or survival of selected anaerobes | Anaerobes including *Bacteroides*, *Desulfovibrio*, and *Moorella* possess soluble or membrane O2-reduction systems; cytochrome bd can enhance low-O2 growth. (lu2021whenanaerobesencounter pages 3-4, lu2021whenanaerobesencounter pages 4-6) | **Moderate/generalized from multiple taxa.** Presence alone is insufficient for phenotype assignment. |

## 5. Recent developments, quantitative findings, and applications

### 5.1 Range-partitioned O2 defense in an obligate anaerobe (2024)

The most directly curatable recent mechanism is the division of labor among four O2-reducing enzymes in *Clostridioides difficile*: revRbr2 below 0.4% O2, FdpA around 0.4–1%, revRbr1 across approximately 0.1–4%, and FdpF above 4% and in air. The `fdpA` mutant growth defect at 0.4% O2 provides perturbational evidence, not merely genomic association. This suggests that oxygen preference graphs may require **concentration-binned enzyme activity edges**, rather than a single generic “oxygen detoxification” node. (caulat2024physiologicalroleand pages 1-2)

### 5.2 Species-level variation among anammox bacteria (2023)

Marine “Ca. *Scalindua* sp.” was substantially more tolerant than freshwater anammox taxa: IC50 18.0 versus 2.7–4.2 µM and DOmax 51.6 versus 10.9–26.6 µM. It exhibited 22.6 ± 1.9 U mg-protein−1 SOD and 1.6 ± 0.7 U mg-protein−1 catalase activity. Oxygen inhibition could be reversible after 12–24 h air exposure, but recovery differed sharply among taxa; after 12 h at 21% O2, “Ca. *Brocadia sinica*” recovered 80 ± 15%, “Ca. *Jettenia caeni*” 42 ± 2%, whereas “Ca. *Kuenenia stuttgartiensis*” did not recover. (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 7-8)

These results are directly relevant to low-dissolved-oxygen wastewater processes. However, enzyme activities were correlated with tolerance rather than genetically manipulated, and transcriptomic/proteomic confirmation of the proposed causal mechanism was absent. (okabe2023oxygentoleranceand pages 7-8, okabe2023oxygentoleranceand pages 2-3)

### 5.3 Ecological interpretation of apparent anoxia

Environmental metatranscriptomic evidence indicates that O2 respiration is common in habitats classified as anoxic by conventional sensors. High-affinity oxidases permit activity at O2 concentrations below routine detection, while microscale production, diffusion, and consumption generate steep gradients. This is relevant to oxygen-minimum zones, sediments, biofilms, gut mucus, activated sludge, and engineered bioreactors. (berg2022howlowcan pages 5-7)

### 5.4 Genome-based phenotype prediction

A 2024 mSystems study reported approximately 80% accuracy for ternary prediction of microbial dioxygen utilization from genomes, including annotation-free amino-acid-trimer models. The authors also found quantitative correspondence between Black Sea community predictions and the local O2:sulfide ratio. This is useful for prioritizing isolates or metagenome-assembled genomes for testing, but model predictions should be represented as **computational evidence**, not causal edges or reviewed phenotype assertions. DOI: [10.1128/msystems.00763-24](https://doi.org/10.1128/msystems.00763-24), published October 2024.

### 5.5 Medical and antimicrobial relevance

High-affinity terminal oxidases help pathogens respire in hypoxic host niches, and bacterial-specific cytochrome bd is under investigation as an antimicrobial target. Oxygen-responsive metabolic flexibility also supports colonization by facultative anaerobes; eight of twelve organisms on the cited WHO antibiotic-resistant priority-pathogen list were facultative anaerobes. This is an ecological/clinical association, not proof that facultative metabolism alone causes antimicrobial resistance. DOI: [10.1111/cmi.13338](https://doi.org/10.1111/cmi.13338), published April 2021. (andre2021theselectiveadvantage pages 7-8)

## 6. Recommended YAML graph architecture

A robust TraitMech graph should separate four layers:

1. **Environmental input:** O2 concentration/availability, exposure duration, spatial gradient.
2. **Sensing and regulation:** FNR/FixLJ/ArcAB or taxon-specific regulators.
3. **Mechanistic balance:** respiratory energy gain versus direct O2 toxicity and ROS damage, modified by oxidases and defense enzymes.
4. **Observed output:** growth rate/yield, growth/no growth, optimum O2, IC50, DOmax, survival, or recovery.

Recommended backbone:

`O2 availability → terminal oxidase activity → O2 reduction → proton-motive force → ATP production → growth under O2`

with competing branches:

`O2 exposure → direct inactivation of oxygen-labile enzymes → reduced central metabolism → reduced growth`

and

`O2 exposure → ROS → macromolecular/Fe–S damage → reduced growth or survival`

counteracted by:

`O2-reducing and ROS-detoxification systems → lower intracellular O2/ROS burden → increased tolerance → expanded permissible O2 range`.

## 7. Warnings: claims not yet suitable for unqualified curation

1. **Do not infer oxygen preference from a terminal-oxidase gene alone.** Paralogs differ in affinity, coupling, stress function, expression, and assembly requirements.
2. **Do not equate O2 consumption with growth-supporting respiration.** Flavodiiron proteins, rubrerythrins, and some oxidases may consume O2 primarily for detoxification.
3. **Do not generalize taxon-specific concentration ranges.** The *C. difficile* Fdp/revRbr ranges and anammox IC50/DOmax values are assay- and organism-specific.
4. **Do not convert correlations into causal gene edges.** The anammox SOD–catalase comparison lacked gene deletion/overexpression; curate as `associated_with` or mark uncertain.
5. **Do not merge direct O2 toxicity with ROS toxicity.** PFL and PFOR can be damaged directly by molecular O2, whereas other damage is mediated by superoxide, H2O2, or hydroxyl radicals. (lu2021whenanaerobesencounter pages 8-9, lu2021whenanaerobesencounter pages 4-6)
6. **Do not use “strict anaerobe” as an absolute zero-tolerance statement.** Growth, metabolic activity, transient survival, and recovery are distinct endpoints. (lu2021whenanaerobesencounter pages 3-4)
7. **Do not assign a universal microaerophile threshold.** Report dissolved O2, headspace O2, vessel geometry, and duration as evidence qualifiers.
8. **FNR, ArcAB, FixLJ, OxyR, Rex, Spx, and σB should not appear in one universal pathway.** Their presence and regulatory targets vary by lineage.
9. **Genome-prediction output is not reviewed phenotype evidence.** The approximately 80% classifier accuracy implies a meaningful error rate.
10. **Ontology identifiers for phenotype subclasses, environmental oxygen regimes, individual oxidase complexes, and fermentation should be verified before YAML insertion.** Label-only nodes are safer than invented CURIEs.

## 8. DOI-first bibliography

1. **Caulat LC et al.** “Physiological role and complex regulation of O2-reducing enzymes in the obligate anaerobe *Clostridioides difficile*.” *mBio* 15 (October 2024). DOI: [10.1128/mbio.01591-24](https://doi.org/10.1128/mbio.01591-24). (caulat2024physiologicalroleand pages 1-2)
2. **Flamholz AI et al.** “Annotation-free prediction of microbial dioxygen utilization.” *mSystems* 9 (October 2024). DOI: [10.1128/msystems.00763-24](https://doi.org/10.1128/msystems.00763-24).
3. **Okabe S et al.** “Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing bacteria.” *ISME Communications* 3 (May 2023). DOI: [10.1038/s43705-023-00251-7](https://doi.org/10.1038/s43705-023-00251-7). (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 11-12, okabe2023oxygentoleranceand pages 7-8)
4. **Berg JS et al.** “How low can they go? Aerobic respiration by microorganisms under apparent anoxia.” *FEMS Microbiology Reviews* 46 (2022; online January 2022). DOI: [10.1093/femsre/fuac006](https://doi.org/10.1093/femsre/fuac006). (berg2022howlowcan pages 5-7)
5. **Lu Z, Imlay JA.** “When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence.” *Nature Reviews Microbiology* 19:774–785 (June 2021). DOI: [10.1038/s41579-021-00583-y](https://doi.org/10.1038/s41579-021-00583-y). (lu2021whenanaerobesencounter pages 3-4, lu2021whenanaerobesencounter pages 8-9, lu2021whenanaerobesencounter pages 4-6)
6. **Price EE, Román-Rodríguez F, Boyd JM.** “Bacterial approaches to sensing and responding to respiration and respiration metabolites.” *Molecular Microbiology* 116:1009–1021 (August 2021). DOI: [10.1111/mmi.14795](https://doi.org/10.1111/mmi.14795).
7. **André AC, Debande L, Marteyn BS.** “The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection.” *Cellular Microbiology* 23 (April 2021). DOI: [10.1111/cmi.13338](https://doi.org/10.1111/cmi.13338). (andre2021theselectiveadvantage pages 7-8)
8. **Borisov VB et al.** “ROS Defense Systems and Terminal Oxidases in Bacteria.” *Antioxidants* 10:839 (May 2021). DOI: [10.3390/antiox10060839](https://doi.org/10.3390/antiox10060839).
9. **Barth C et al.** “Origin and phylogenetic relationships of [4Fe–4S]-containing O2 sensors of bacteria.” *Environmental Microbiology* 20:4567–4586 (October 2018). DOI: [10.1111/1462-2920.14411](https://doi.org/10.1111/1462-2920.14411).

**Curation priority:** implement the general O2-respiration/energy and O2-damage/defense backbone first; add the 2024 *C. difficile* concentration-resolved Fdp/revRbr branch as a clearly taxon-specific subgraph; retain cross-species SOD–catalase-to-tolerance edges as uncertain until perturbational evidence is available.

References

1. (berg2022howlowcan pages 5-7): Jasmine S Berg, Soeren Ahmerkamp, Petra Pjevac, Bela Hausmann, Jana Milucka, and Marcel M M Kuypers. How low can they go? aerobic respiration by microorganisms under apparent anoxia. FEMS Microbiology Reviews, Jan 2022. URL: https://doi.org/10.1093/femsre/fuac006, doi:10.1093/femsre/fuac006. This article has 85 citations and is from a domain leading peer-reviewed journal.

2. (lu2021whenanaerobesencounter pages 3-4): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

3. (andre2021theselectiveadvantage pages 7-8): Antonin C. André, Lorine Debande, and Benoit S. Marteyn. The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection. Cellular Microbiology, Apr 2021. URL: https://doi.org/10.1111/cmi.13338, doi:10.1111/cmi.13338. This article has 110 citations and is from a peer-reviewed journal.

4. (lu2021whenanaerobesencounter pages 16-17): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

5. (lu2021whenanaerobesencounter pages 4-6): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

6. (lu2021whenanaerobesencounter pages 8-9): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 360 citations and is from a highest quality peer-reviewed journal.

7. (okabe2023oxygentoleranceand pages 1-2): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 71 citations and is from a peer-reviewed journal.

8. (okabe2023oxygentoleranceand pages 11-12): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 71 citations and is from a peer-reviewed journal.

9. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

10. (okabe2023oxygentoleranceand pages 7-8): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 71 citations and is from a peer-reviewed journal.

11. (okabe2023oxygentoleranceand pages 2-3): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 71 citations and is from a peer-reviewed journal.