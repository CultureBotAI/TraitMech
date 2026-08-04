---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T12:07:19.462961'
end_time: '2026-08-04T12:27:56.859410'
duration_seconds: 1237.4
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: viable but nonculturable state
  trait_identifier: traitmech:000081
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: viable_but_nonculturable_state
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A dormancy state in which cells remain viable and minimally metabolically
    active but lose the ability to grow on routine culture media, regaining culturability
    upon resuscitation.
  parent_traits: traitmech:000080
  synonyms: VBNC state
  evidence_summary: 'DOI:10.1111/j.1574-6976.2009.00200.x:  (Oliver reviews the viable-but-nonculturable
    state, in which stressed cells stay viable yet unculturable until resuscitated.)
    | DOI:10.1038/nrmicro2504:  (Lennon & Jones frame the VBNC state within the broader
    microbial dormancy seed-bank concept.)'
  causal_graph_summary: 'vbnc_stress_induced_dormancy: 11 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 69
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** viable but nonculturable state
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000081
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A dormancy state in which cells remain viable and minimally metabolically active but lose the ability to grow on routine culture media, regaining culturability upon resuscitation.
- **Parent traits:** traitmech:000080
- **Synonyms:** VBNC state
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00200.x:  (Oliver reviews the viable-but-nonculturable state, in which stressed cells stay viable yet unculturable until resuscitated.) | DOI:10.1038/nrmicro2504:  (Lennon & Jones frame the VBNC state within the broader microbial dormancy seed-bank concept.)
- **Existing causal graph summary:** vbnc_stress_induced_dormancy: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **viable but nonculturable state** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/viable_but_nonculturable_state.yaml`.

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
- **Trait label:** viable but nonculturable state
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000081
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A dormancy state in which cells remain viable and minimally metabolically active but lose the ability to grow on routine culture media, regaining culturability upon resuscitation.
- **Parent traits:** traitmech:000080
- **Synonyms:** VBNC state
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00200.x:  (Oliver reviews the viable-but-nonculturable state, in which stressed cells stay viable yet unculturable until resuscitated.) | DOI:10.1038/nrmicro2504:  (Lennon & Jones frame the VBNC state within the broader microbial dormancy seed-bank concept.)
- **Existing causal graph summary:** vbnc_stress_induced_dormancy: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **viable but nonculturable state** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/viable_but_nonculturable_state.yaml`.

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


# Viable But Nonculturable (VBNC) State: Causal Graph Research Report

## Executive Summary

The viable but nonculturable (VBNC) state (traitmech:000081) is a widespread bacterial dormancy strategy in which cells remain alive, metabolically active, and potentially virulent yet fail to form colonies on routine culture media. This report synthesizes recent mechanistic evidence (prioritizing 2023–2024 sources) to support causal graph curation, identifying key molecular entities, environmental triggers, and resuscitation pathways suitable for YAML encoding in the TraitMech ontology.

---

## 1. Trait Scope and Definition

### 1.1 Core Definition

The VBNC state is a dormant physiological condition where bacterial cells:

- **Lose culturability** on standard laboratory media despite remaining viable and metabolically active (pazosrojas2023theviablebut pages 1-2, prosdocimi2023cellphenotypechanges pages 1-2).
- **Retain resuscitation capacity** under favorable conditions, enabling return to a culturable state (prosdocimi2023cellphenotypechanges pages 1-2).
- **Maintain high ATP levels**, distinguishing them from dead cells where ATP rapidly decreases (pazosrojas2023theviablebut pages 11-13).
- **Exhibit reduced metabolic activity** with decreased nutrient transport and respiration rates (pazosrojas2023theviablebut pages 1-2).
- **Express genes continuously**, distinguishing VBNC from spore-forming states (pazosrojas2023theviablebut pages 1-2).

Published: Pazos-Rojas et al., *Microorganisms*, December 2023, https://doi.org/10.3390/microorganisms12010039; Prosdocimi et al., *Annals of Microbiology*, January 2023, https://doi.org/10.1186/s13213-022-01703-6.

### 1.2 Boundary Conditions

**VBNC cells differ from:**

- **Dead cells**: VBNC cells retain high ATP levels, intact membranes, and DNA; dead cells rapidly lose ATP, membrane integrity, and viability (pazosrojas2023theviablebut pages 11-13).
- **Spores**: VBNC cells continuously express genes and lack specialized spore structures; spores are dormant, dehydrated structures with minimal metabolic activity (pazosrojas2023theviablebut pages 1-2).
- **Persisters**: Both share toxin-antitoxin and stringent response pathways and ATP depletion mechanisms (yang2024resuscitationofviable pages 13-13). However, VBNC cells are induced by environmental stresses (starvation, cold, oxidative damage) and require resuscitation protocols, while persisters are antibiotic-tolerant subpopulations that revert spontaneously after antibiotic removal.
- **Obligate unculturability**: VBNC is reversible through resuscitation; obligate unculturable bacteria cannot be cultured due to unknown or syntrophic nutrient requirements.

**Experimental distinction** from moribund cells: VBNC cells remain "sterile but metabolically active" and "intact" (nystrom2003nonculturablebacteriaprogrammed pages 1-2), whereas moribund cells in the death phase will eventually lose viability.

Published: Nyström, *BioEssays*, March 2003, https://doi.org/10.1002/bies.10233.

### 1.3 Phenotypic Characteristics

**Morphology:**

- **Cell dwarfing**: Size reduction (e.g., *Campylobacter jejuni* viable cells 0.5–5 µm × 0.2–0.8 µm become ~0.5 mm diameter coccoid forms) (santos2023rolesofviable pages 4-7).
- **Cell rounding**: Transition from rod/spiral to coccus-like shapes; *Francisella tularensis* LVS becomes significantly rounder at 48+ hours (p<0.001) (cantlay2024phenotypicandtranscriptional pages 5-6).
- **Loss of flagella**: Observed in *C. jejuni* and *Vibrio* spp. (santos2023rolesofviable pages 4-7, prosdocimi2023cellphenotypechanges pages 1-2).
- **Thickened cell envelopes** and more rigid cell walls with altered peptidoglycan biosynthesis (pazosrojas2023theviablebut pages 11-13, santos2023rolesofviable pages 7-9).
- **Nucleoid compaction** into nanocrystalline or liquid crystalline structures stabilized by Dps or SASP proteins (pazosrojas2023theviablebut pages 11-13).

**Metabolic:**

- High ATP retention (pazosrojas2023theviablebut pages 11-13).
- Reduced DNA quantity (flow cytometry) (prosdocimi2023cellphenotypechanges pages 1-2).
- Altered membrane permeability and fatty acid composition (pazosrojas2023theviablebut pages 11-13).

Published: Santos et al., *Frontiers in Cellular and Infection Microbiology*, March 2023, https://doi.org/10.3389/fcimb.2023.1122450; Cantlay et al., *Frontiers in Microbiology*, February 2024, https://doi.org/10.3389/fmicb.2024.1347488.

---

## 2. Candidate Causal Graph Entities

Entities are grouped by ontology class, with stable identifiers (CURIEs) where available.

### 2.1 Environmental Factors (Inducers)

| Entity Label | Candidate CURIE | Induction Evidence |
|--------------|-----------------|---------------------|
| Nutrient starvation | ENVO:01001307 | Pazos-Rojas et al. 2023 (pazosrojas2023theviablebut pages 1-2) |
| Cold stress / low temperature | ENVO:01000992 | Prosdocimi et al. 2023 (prosdocimi2023cellphenotypechanges pages 1-2) |
| Oxidative stress | GO:0006979 | Zhang et al. 2023 (zhang2023currentperspectiveson pages 4-5) |
| Osmotic stress | ENVO:3100031 | Pazos-Rojas et al. 2023 (pazosrojas2023theviablebut pages 1-2) |
| Desiccation | ENVO:01001050 | Pazos-Rojas et al. 2023 (pazosrojas2023theviablebut pages 11-13) |
| Thermal stress (heat/cold) | ENVO:01001322 | Zhang et al. 2023 (zhang2023currentperspectiveson pages 4-5) |
| Chlorine disinfection | CHEBI:29311 | Zhang et al. 2023 (zhang2023currentperspectiveson pages 10-12) |
| High-pressure CO₂ | ENVO:01000796 | Pazos-Rojas et al. 2023 (pazosrojas2023theviablebut pages 21-21) |
| White light exposure | ENVO:01001854 | Pazos-Rojas et al. 2023 (pazosrojas2023theviablebut pages 1-2) |

### 2.2 Chemicals (Effectors and Mediators)

| Entity Label | Candidate CURIE | Role in VBNC |
|--------------|-----------------|---------------|
| Reactive oxygen species (ROS) | CHEBI:26523 | Increase upon VBNC entry (zhang2023currentperspectiveson pages 4-5) |
| Hydrogen peroxide | CHEBI:16240 | Prevents resuscitation at 0.007 mM (prosdocimi2023cellphenotypechanges pages 1-2) |
| Catalase (enzyme) | EC:1.11.1.6 | Preserves culturability; detoxifies H₂O₂ (prosdocimi2023cellphenotypechanges pages 1-2) |
| Sodium pyruvate | CHEBI:16960 | Radical scavenger; inhibits VBNC production (zhang2023currentperspectiveson pages 4-5) |
| ATP | CHEBI:15422 | Mediates NAD⁺ synthesis in resuscitation (yang2024resuscitationofviable pages 1-2) |
| NAD⁺ | CHEBI:15846 | Critical for TCA cycle, electron transport, resuscitation (yang2024resuscitationofviable pages 9-10) |
| (p)ppGpp (alarmone) | CHEBI:71190 | Stringent response mediator; accumulates during VBNC entry (zhang2023currentperspectiveson pages 4-5) |
| Autoinducer-2 (AI-2) | CHEBI:67078 | Quorum-sensing molecule; triggers resuscitation in *Vibrio* (prosdocimi2023cellphenotypechanges pages 1-2) |
| cAMP | CHEBI:17489 | Proposed VBNC inducer (pazosrojas2023theviablebut pages 13-14) |

### 2.3 Genes and Proteins

| Entity Label | Candidate CURIE / Notes | Function in VBNC |
|--------------|------------------------|-------------------|
| **Stringent response genes** | | |
| *relA* | (Organism-specific; *E. coli* b2784) | (p)ppGpp synthetase I; upregulated during VBNC entry (zhang2023currentperspectiveson pages 4-5) |
| *spoT* | (Organism-specific; *E. coli* b3650) | Bifunctional (p)ppGpp synthase/hydrolase (zhang2023currentperspectiveson pages 4-5) |
| **Stress response regulators** | | |
| RpoS (σ^S) | (Organism-specific) | Essential for VBNC entry/exit; mutants lose culturability irreversibly (pazosrojas2023theviablebut pages 11-13) |
| **Toxin-antitoxin systems** | GO:0090501 | Inhibit replication, translation, ATP synthesis; drive dormancy (zhang2023currentperspectiveson pages 4-5) |
| Lon protease | (Organism-specific; *E. coli* b0439) | Upregulated; degrades misfolded proteins (zhang2023currentperspectiveson pages 4-5) |
| ClpP protease | (Organism-specific; *E. coli* b0437) | Upregulated; ATP-dependent proteolysis (zhang2023currentperspectiveson pages 4-5) |
| **Antioxidant defense** | | |
| *ahpC* | (Organism-specific; alkyl hydroperoxide reductase) | Mutants show reduced VBNC viability in *C. jejuni* (zhang2023currentperspectiveson pages 4-5) |
| *katA*, *katE*, *katG* | EC:1.11.1.6 | Catalase genes; KatG decrease during VBNC induction (prosdocimi2023cellphenotypechanges pages 1-2, zhang2023currentperspectiveson pages 4-5) |
| *sodA*, *sodB*, *sodC* | EC:1.15.1.1 | Superoxide dismutase genes; mutants show VBNC phenotype (zhang2023currentperspectiveson pages 4-5) |
| **NAD⁺ biosynthesis** | GO:0009435 | |
| *pncB* | EC:6.3.4.21 | Nicotinate phosphoribosyltransferase; upregulated in resuscitation (yang2024resuscitationofviable pages 9-10) |
| *nadD* | EC:2.7.7.18 | Nicotinate-nucleotide adenylyltransferase (yang2024resuscitationofviable pages 9-10) |
| *nadE* | EC:6.3.5.1 | NAD synthetase; aggregates in VBNC, reactivates during resuscitation (yang2024resuscitationofviable pages 10-13) |
| *nadB* | EC:1.4.1.16 | L-aspartate oxidase; aggregates in VBNC (yang2024resuscitationofviable pages 10-13) |
| *nadR* | (Transcriptional regulator) | Upregulated in resuscitating cells (yang2024resuscitationofviable pages 9-10) |
| **Resuscitation factors** | | |
| Rpf (Resuscitation-promoting factor) | (Label-only; peptidoglycan hydrolase family) | Extracellular muralytic enzyme; triggers resuscitation (pazosrojas2023theviablebut pages 4-5) |
| YeaZ protease | (Organism-specific; *V. harveyi*) | Involved in resuscitation (pazosrojas2023theviablebut pages 21-21) |
| **LPS biosynthesis** | | |
| *rfaL* | (O-antigen ligase; *E. coli*) | Deletion shortens resuscitation lag phase; redirects ATP to NAD⁺ synthesis (yang2024resuscitationofviable pages 1-2) |
| **Metabolic regulation** | | |
| RaiA | (Ribosome-associated inhibitor) | Low expression reduces translational activity in VBNC (pazosrojas2023theviablebut pages 13-14) |
| Dps | (DNA-binding protein from starved cells) | Stabilizes nucleoid compaction (pazosrojas2023theviablebut pages 11-13) |
| **Transporters** | | |
| PP_2662, PP_2676 | (Organism-specific; *P. putida* KT2440) | Upregulated; transport compatible solutes during desiccation-induced VBNC (pazosrojas2023theviablebut pages 13-14) |
| TonB-dependent receptor | (Iron acquisition) | Upregulated in *P. putida* KT2440 (pazosrojas2023theviablebut pages 13-14) |
| ABC transporters | GO:0042626 | Maintain selective permeability in VBNC (pazosrojas2023theviablebut pages 11-13) |
| **Virulence genes (taxon-specific)** | | |
| *ciaB* | (Organism-specific; *C. jejuni*) | Invasion gene; transcripts reduced but present in 59.3% VBNC strains (santos2023rolesofviable pages 7-9) |
| *p19* | (Organism-specific; *C. jejuni*) | Stress adaptation gene; transcripts maintained in 100% VBNC strains (santos2023rolesofviable pages 7-9) |

### 2.4 Biological Processes and Pathways

| Process Label | Candidate CURIE | Role in VBNC |
|---------------|-----------------|---------------|
| Stringent response | GO:0006950 | (p)ppGpp accumulation triggers VBNC entry (zhang2023currentperspectiveson pages 4-5) |
| Toxin-antitoxin system | GO:0090501 | Inhibits core metabolism to conserve energy (zhang2023currentperspectiveson pages 4-5) |
| Oxidative stress response | GO:0006979 | ROS accumulation promotes VBNC entry (zhang2023currentperspectiveson pages 4-5) |
| NAD⁺ biosynthesis | GO:0009435 | Preiss-Handler, salvage, and de novo pathways restore NAD⁺ in resuscitation (yang2024resuscitationofviable pages 9-10) |
| Glyoxylate cycle | GO:0006097 | Activated for stress resistance (pazosrojas2023theviablebut pages 13-14) |
| Protein aggregation | GO:0070841 | NadB and NadE aggregate in VBNC; disaggregated by DnaK-ClpB during resuscitation (yang2024resuscitationofviable pages 10-13) |
| Quorum sensing | GO:0009372 | AI-2 triggers resuscitation in *Vibrio* spp. (prosdocimi2023cellphenotypechanges pages 1-2) |
| Ribosome dimerization | (Label-only) | Facilitates VBNC transition (pazosrojas2023theviablebut pages 13-14) |

---

## 3. Evidence-Backed Causal Edges

The following table summarizes candidate causal edges for YAML curation.

| Subject | Predicate | Object | Organism | Evidence Certainty | Reference (DOI/URL) | Quote/Snippet | Notes |
|---|---|---|---|---|---|---|---|
| Stringent response (GO:0006950) | positively_regulates | Viable but nonculturable state (traitmech:000081) | Foodborne pathogens | High | 10.3390/foods12061179 (zhang2023currentperspectiveson pages 4-5) | "(p)ppGpp alarmone synthesis triggered by environmental stress... enhancing stress resistance during VBNC entry." | Accumulation of alarmones like (p)ppGpp via relA and spoT drives entry into the state. |
| Toxin-antitoxin systems (GO:0090501) | positively_regulates | Viable but nonculturable state (traitmech:000081) | Foodborne pathogens | High | 10.3390/foods12061179 (zhang2023currentperspectiveson pages 4-5) | "TA system inhibits DNA replication, translation... driving entry into dormant VBNC state" | Downregulates core metabolic processes to conserve energy under stress. |
| Oxidative stress (GO:0006979) / Reactive oxygen species | positively_regulates | Viable but nonculturable state (traitmech:000081) | Foodborne pathogens | High | 10.3390/foods12061179 (zhang2023currentperspectiveson pages 4-5) | "ROS production... increases upon VBNC entry" | Triggered by environmental stress, leading to morphological changes and dormancy. |
| Hydrogen peroxide (CHEBI:16240) | negatively_regulates | Resuscitation from VBNC | *Vibrio* spp. | High | 10.1186/s13213-022-01703-6 (prosdocimi2023cellphenotypechanges pages 1-2) | "Hydrogen peroxide at 0.007 mM concentration prevented resuscitation" | Maintains the VBNC state or causes irreversible oxidative damage at low doses. |
| Catalase (EC 1.11.1.6) | positively_regulates | Resuscitation from VBNC | *Vibrio* spp. | High | 10.1186/s13213-022-01703-6 (prosdocimi2023cellphenotypechanges pages 1-2) | "Catalase addition preserved culturability of VBNC cells" | Decomposes hydrogen peroxide, alleviating oxidative stress that blocks culturability. |
| Autoinducer-2 (CHEBI:67078) | positively_regulates | Resuscitation from VBNC | *Vibrio* spp. | Medium | 10.1186/s13213-022-01703-6 (prosdocimi2023cellphenotypechanges pages 1-2) | "Quorum-sensing molecule AI-2 triggers resuscitation." | QS signaling is sufficient to exit dormancy in specific populations. |
| Sodium pyruvate (CHEBI:16960) | negatively_regulates | Viable but nonculturable state (traitmech:000081) | *Salmonella* | Medium | 10.3390/foods12061179 (zhang2023currentperspectiveson pages 4-5) | "sodium pyruvate radical scavenger pretreatment before thermal sonication inhibited VBNC production." | Acts as a radical scavenger to prevent oxidative stress-induced entry. |
| RNA polymerase sigma factor RpoS | positively_regulates | Viable but nonculturable state (traitmech:000081) | Beneficial bacteria | High | 10.3390/microorganisms12010039 (pazosrojas2023theviablebut pages 11-13) | "RpoS sigma factor (with ppGpp as positive regulator) is essential for VBNC entry/exit" | Global stress regulator; mutants lose cultivability irreversibly. |
| Resuscitation-promoting factor (Rpf) | positively_regulates | Resuscitation from VBNC | *Arthrobacter albidus* | Medium | 10.3390/microorganisms12010039 (pazosrojas2023theviablebut pages 4-5) | "absence of resuscitation promoting factor (Rpf) protein in culture medium as an induction condition" | Extracellular muralytic enzymes that wake dormant cells. |
| YeaZ protease | positively_regulates | Resuscitation from VBNC | *Vibrio harveyi* | Medium | 10.3390/microorganisms12010039 (pazosrojas2023theviablebut pages 21-21) | "YeaZ protease involvement in Vibrio harveyi resuscitation from VBNC state" | Proteolytic processing is linked to exiting dormancy. |
| NAD+ biosynthetic process (GO:0009435) | positively_regulates | Resuscitation from VBNC | General | Medium | 10.3390/microorganisms12010039 (pazosrojas2023theviablebut pages 21-21) | "ATP-mediated NAD+ synthesis promoting resuscitation" | Energy and redox balance restoration is required for exit. |
| KatG / Periplasmic catalase | negatively_regulates | Viable but nonculturable state (traitmech:000081) | *Vibrio* spp. | High | 10.1186/s13213-022-01703-6 (prosdocimi2023cellphenotypechanges pages 1-2) | "decreased periplasmic catalase KatG expression during induction, reducing catalase activity" | Loss of KatG activity allows oxidative stress to accumulate and force entry into VBNC. |


*Table: This table lists candidate causal edges linking molecular entities and environmental factors to the induction or resuscitation of the viable but nonculturable (VBNC) state, extracted from recent literature for causal graph curation.*

### 3.1 Additional Mechanistic Edges from 2024 Studies

**ATP → NAD⁺ → Resuscitation Pathway (Yang et al. 2024, *J. Adv. Res.*, DOI:10.1016/j.jare.2023.08.002):**

- **Edge 1:** ATP consumption → activates *nadR*, *nadD*, *pncB*, *nadE* gene expression (yang2024resuscitationofviable pages 9-10).
- **Edge 2:** NAD⁺ synthesis via Preiss-Handler and salvage pathways → restores TCA cycle and electron transport chain → generates NADH and ATP (yang2024resuscitationofviable pages 9-10).
- **Edge 3:** ATP-dependent protein disaggregation (DnaK-ClpB chaperones) → deaggregates NadB and NadE enzymes → enables NAD⁺ biosynthesis (yang2024resuscitationofviable pages 10-13).
- **Edge 4:** NAD⁺ restoration → translation activity recovery → macromolecule biosynthesis → DNA replication, septum formation, cell division (yang2024resuscitationofviable pages 10-13).
- **Edge 5:** Deletion of *rfaL* (LPS synthesis) → higher residual ATP → shorter resuscitation lag phase (yang2024resuscitationofviable pages 1-2).

**Certainty:** High (direct genetic knockout and metabolomic validation in *E. coli* O157:H7).

Published: Yang et al., *Journal of Advanced Research*, June 2024, https://doi.org/10.1016/j.jare.2023.08.002.

**Transcriptomic Changes in *F. tularensis* LVS (Cantlay et al. 2024, *Front. Microbiol.*, DOI:10.3389/fmicb.2024.1347488):**

- VBNC cells (336 h): 145 genes upregulated, 203 downregulated (cantlay2024phenotypicandtranscriptional pages 9-10).
- Upregulated: carbohydrate/amino acid transport/metabolism, transposases (~50% of upregulated loci).
- Downregulated: translation, energy metabolism (consistent with dormancy).
- VBNC cells retain erythrocyte attachment/invasion capability (10.7% attachment, 9.3% invasion) comparable to culturable cells (10.4%, 11.5%) (cantlay2024phenotypicandtranscriptional pages 9-10).
- Gentamicin insensitivity: VBNC cells show no OD600 or fluorescence change with 100 µg/ml gentamicin; culturable cells lyse (cantlay2024phenotypicandtranscriptional pages 10-12).

**Certainty:** High (RNA-seq, flow cytometry, infection assays).

Published: Cantlay et al., *Frontiers in Microbiology*, February 2024, https://doi.org/10.3389/fmicb.2024.1347488.

**Metabolomic Shifts in *C. jejuni* (Santos et al. 2023, *Front. Cell. Infect. Microbiol.*, DOI:10.3389/fcimb.2023.1122450):**

- 315 metabolites identified; 169 unique to VBNC (santos2023rolesofviable pages 7-9).
- VBNC-enriched: squalene, 2,4-di-tert-butylphenol, acetic acid, palmitic acid, palmitoleic acid (protective mechanisms) (santos2023rolesofviable pages 7-9).
- Volatile organic precursors (octadecanoid acid, hexanoic acid, tetradecanoic acid) indicate metabolic interruption (santos2023rolesofviable pages 7-9).
- Downregulated *ciaB* and *p19* transcripts in VBNC (mean 15.7 and 11.2 ng/µL vs. 54.2 and 43.9 ng/µL in cultivable) (santos2023rolesofviable pages 7-9).

**Certainty:** Medium (metabolomic associations, not mechanistic interventions).

Published: Santos et al., *Frontiers in Cellular and Infection Microbiology*, March 2023, https://doi.org/10.3389/fcimb.2023.1122450.

---

## 4. Current Applications and Real-World Implications

### 4.1 Food Safety

**VBNC foodborne pathogens** (*Salmonella*, *E. coli* O157:H7, *L. monocytogenes*, *C. jejuni*, *V. parahaemolyticus*) remain infectious after chlorination, pasteurization, or refrigeration (pazosrojas2023theviablebut pages 1-2, zhang2023currentperspectiveson pages 7-9). Standard plate counts underestimate pathogen loads, risking false-negative results in food safety testing (pazosrojas2023theviablebut pages 1-2).

**Detection methods** (Zhang et al. 2023): propidium monoazide qPCR (PMA-qPCR), direct viable count (DVC), SYTO 9/propidium iodide flow cytometry, and CTC redox assays distinguish VBNC from dead cells in lettuce, milk, chicken, and process wash water (zhang2023currentperspectiveson pages 7-9, zhang2023currentperspectiveson pages 13-14, zhang2023currentperspectiveson pages 14-15, zhang2023currentperspectiveson pages 5-7).

**Control strategies:** Chlorine at 20–25 mg/L effectively inactivates VBNC *L. monocytogenes* and *E. coli* O157:H7 in wash water (zhang2023currentperspectiveson pages 10-12).

Published: Zhang et al., *Foods*, March 2023, https://doi.org/10.3390/foods12061179.

### 4.2 Water and Wastewater

Chlorination and UV disinfection induce VBNC in *E. coli*, *Vibrio cholerae*, and antibiotic-resistant bacteria in hospital wastewater, freshwater, and drinking water distribution systems (zhang2023currentperspectiveson pages 13-14, prosdocimi2023cellphenotypechanges pages 1-2). Resuscitated cells can re-introduce pathogens and resistance genes into agricultural reuse water (prosdocimi2023cellphenotypechanges pages 1-2).

### 4.3 Clinical Microbiology

VBNC *Vibrio* spp. retain virulence upon resuscitation (prosdocimi2023cellphenotypechanges pages 1-2). Climate change-driven sea surface temperature increases correlate with Vibrio-related disease incidence (prosdocimi2023cellphenotypechanges pages 1-2). VBNC *C. jejuni* and *F. tularensis* retain invasion capacity and antibiotic tolerance, complicating infection control and diagnostics (cantlay2024phenotypicandtranscriptional pages 9-10, santos2023rolesofviable pages 7-9).

### 4.4 Beneficial Bacteria and Agriculture

Bacterial inoculants (*Pseudomonas putida* KT2440, *Cupriavidus metallidurans*) can enter VBNC during desiccation or freeze-drying but resuscitate in the plant rhizosphere or upon rehydration with gluconate (pazosrojas2023theviablebut pages 7-8, pazosrojas2023theviablebut pages 13-14). VBNC formulation extends shelf life and reduces production costs for biofertilizers and biocontrol agents (pazosrojas2023theviablebut pages 15-17).

Published: Pazos-Rojas et al., *Microorganisms*, December 2023, https://doi.org/10.3390/microorganisms12010039.

### 4.5 Bioremediation

*Cupriavidus metallidurans* converts gold chloride into 24-carat gold during VBNC state (pazosrojas2023theviablebut pages 7-8). *Pseudomonas* species degrade xenobiotics and aromatic compounds while in VBNC, contributing to environmental persistence in contaminated sites (pazosrojas2023theviablebut pages 7-8).

---

## 5. Detection and Viability Assays

### 5.1 Molecular Techniques

- **PMA-qPCR:** Propidium monoazide penetrates dead cells, cross-links DNA, inhibits PCR amplification; viable VBNC DNA is amplified (zhang2023currentperspectiveson pages 7-9, zhang2023currentperspectiveson pages 13-14).
- **PMA-LAMP:** Faster isothermal amplification alternative (zhang2023currentperspectiveson pages 14-15).
- **RT-qPCR:** Detects mRNA expression to confirm metabolic activity (zhang2023currentperspectiveson pages 5-7, pazosrojas2023theviablebut pages 10-11).

### 5.2 Metabolic Detection

- **CTC/INT redox dyes:** Respiratory chain enzymes reduce dyes to fluorescent formazan; detected by flow cytometry (zhang2023currentperspectiveson pages 7-9, zhang2023currentperspectiveson pages 5-7). Limitation: CTC toxicity may underestimate active cells (zhang2023currentperspectiveson pages 5-7).
- **ATP measurements:** VBNC cells retain high ATP; dead cells do not (pazosrojas2023theviablebut pages 11-13).

### 5.3 Staining Techniques

- **SYTO 9 / Propidium iodide (BacLight Live/Dead Kit):** VBNC cells fluoresce green (intact membranes); dead cells fluoresce red (compromised membranes) (zhang2023currentperspectiveson pages 7-9, pazosrojas2023theviablebut pages 10-11).
- **Flow cytometry parameters:** Forward scatter (FSC-A, cell size) and green fluorescence (FL1-A, DNA quantity) decrease in VBNC; propidium iodide green fluorescence increases in dwarf populations (prosdocimi2023cellphenotypechanges pages 5-7).

### 5.4 Direct Viable Count (DVC)

DNA gyrase inhibitors (nalidixic acid, ciprofloxacin) block division; viable VBNC cells elongate, visible by acridine orange microscopy (zhang2023currentperspectiveson pages 7-9).

### 5.5 Resuscitation Assays

- **Temperature shift:** Incubation at 30°C overnight restores culturability in *Vibrio* spp. (prosdocimi2023cellphenotypechanges pages 5-7).
- **Catalase supplementation:** Catalase in agar preserves VBNC culturability by detoxifying H₂O₂ (prosdocimi2023cellphenotypechanges pages 5-7).
- **Rpf addition:** Exogenous resuscitation-promoting factor wakes dormant cells (pazosrojas2023theviablebut pages 4-5).

Published: Zhang et al., *Foods*, March 2023, https://doi.org/10.3390/foods12061179; Pazos-Rojas et al., *Microorganisms*, December 2023, https://doi.org/10.3390/microorganisms12010039; Prosdocimi et al., *Annals of Microbiology*, January 2023, https://doi.org/10.1186/s13213-022-01703-6.

---

## 6. Ontology Grounding Recommendations

### 6.1 High-Confidence CURIEs

- **Trait:** traitmech:000081 (viable but nonculturable state) — given in template.
- **Parent trait:** traitmech:000080 (dormancy) — given in template.
- **Environmental stresses:** ENVO:01001307 (nutrient limitation), ENVO:01000992 (cold stress), ENVO:01001050 (desiccation), GO:0006979 (oxidative stress).
- **Chemicals:** CHEBI:16240 (hydrogen peroxide), CHEBI:15422 (ATP), CHEBI:15846 (NAD⁺), CHEBI:71190 ((p)ppGpp), CHEBI:67078 (autoinducer-2), CHEBI:16960 (sodium pyruvate).
- **Enzymes:** EC:1.11.1.6 (catalase), EC:1.15.1.1 (superoxide dismutase), EC:6.3.4.21 (nicotinate phosphoribosyltransferase).
- **Processes:** GO:0006950 (stringent response), GO:0090501 (toxin-antitoxin system), GO:0009435 (NAD⁺ biosynthetic process), GO:0009372 (quorum sensing).

### 6.2 Label-Only Entities (No Stable CURIE Available)

- Rpf (resuscitation-promoting factor) — peptidoglycan hydrolase family; no universal CURIE.
- YeaZ protease — organism-specific (*Vibrio harveyi*); use species-specific gene identifiers.
- *rfaL*, *relA*, *spoT*, *rpoS*, *pncB*, *nadD*, *nadE*, *nadB*, *nadR* — organism-specific gene loci; annotate by NCBIGene or UniProt per organism.
- Ribosome dimerization, protein aggregation (context-specific) — GO:0070841 (protein aggregation) is available but broad.

**Recommendation:** Use organism-qualified labels (e.g., "RpoS (*E. coli*)") and defer to NCBI Gene, UniProt, or EcoCyc identifiers for specific loci in YAML curation.

---

## 7. Warnings and Curation Notes

### 7.1 Taxon-Specific Claims

- **Rpf role in resuscitation** is best documented in Actinobacteria (*Micrococcus*, *Arthrobacter*) and some Vibrio species but not universal (pazosrojas2023theviablebut pages 4-5).
- **Virulence gene transcripts** (*ciaB*, *p19*) are *Campylobacter jejuni*-specific; generalization to other VBNC bacteria is not supported (santos2023rolesofviable pages 7-9).
- **AI-2 quorum sensing** triggers resuscitation in *Vibrio* spp. but may not apply to other genera (prosdocimi2023cellphenotypechanges pages 1-2).

### 7.2 Assay-Specific and Methodological Limitations

- **CTC toxicity** may underestimate active cell counts (zhang2023currentperspectiveson pages 5-7).
- **Resuscitation protocols** (temperature, catalase, medium composition) vary by organism and strain (prosdocimi2023cellphenotypechanges pages 5-7, prosdocimi2023cellphenotypechanges pages 1-2).
- **No single definitive test** for VBNC viability; multiple methodologies recommended (pazosrojas2023theviablebut pages 10-11).

### 7.3 Mechanism Uncertainty

- **Universal VBNC mechanism:** No single pathway is fully elucidated across all bacteria (pazosrojas2023theviablebut pages 13-14).
- **RpoS essentiality:** Evidence from *P. putida* KT2440 shows RpoS mutants lose culturability irreversibly, but this has not been validated across all VBNC-capable species (pazosrojas2023theviablebut pages 11-13).
- **ATP-mediated NAD⁺ synthesis:** Demonstrated in *E. coli* O157:H7 with genetic knockout and metabolomics, but generalizability to Gram-positive or obligate intracellular bacteria is unclear (yang2024resuscitationofviable pages 1-2, yang2024resuscitationofviable pages 10-13, yang2024resuscitationofviable pages 9-10).
- **H₂O₂ threshold:** The 0.007 mM concentration blocking resuscitation in *Vibrio* spp. is low; strain and species variation likely (prosdocimi2023cellphenotypechanges pages 1-2).

### 7.4 Do Not Curate as Universal Edges

- **cAMP as inducer:** Proposed but not mechanistically validated (pazosrojas2023theviablebut pages 13-14).
- **Metabolite correlations in *C. jejuni*:** Metabolomic associations (squalene, palmitic acid, volatile organics) are descriptive, not causal (santos2023rolesofviable pages 7-9).
- **Transposome upregulation in *F. tularensis*:** ~50% of upregulated genes are transposases; this is an annotation artifact or genome-specific instability, not a general VBNC mechanism (cantlay2024phenotypicandtranscriptional pages 9-10).

### 7.5 Evidence Strength Hierarchy

1. **High confidence (direct causal experiments):** *rfaL* deletion → ATP availability → NAD⁺ synthesis → resuscitation (yang2024resuscitationofviable pages 1-2, yang2024resuscitationofviable pages 10-13); H₂O₂ exposure → blocked resuscitation (prosdocimi2023cellphenotypechanges pages 1-2); catalase addition → preserved culturability (prosdocimi2023cellphenotypechanges pages 1-2).
2. **Medium confidence (genetic association, gene expression):** RpoS mutants → irreversible loss of culturability (pazosrojas2023theviablebut pages 11-13); antioxidant gene mutants → reduced viability (zhang2023currentperspectiveson pages 4-5); AI-2 triggers resuscitation (prosdocimi2023cellphenotypechanges pages 1-2).
3. **Low confidence (review synthesis, correlation):** cAMP as inducer (pazosrojas2023theviablebut pages 13-14); metabolomic profiles (santos2023rolesofviable pages 7-9); glyoxylate cycle activation (pazosrojas2023theviablebut pages 13-14).

---

## 8. Bibliography (DOI-First)

1. **Yang, D., Wang, W., Zhao, L., Rao, L., & Liao, X.** (2024). Resuscitation of viable but nonculturable bacteria promoted by ATP-mediated NAD+ synthesis. *Journal of Advanced Research*, 60, 27–39. DOI:[10.1016/j.jare.2023.08.002](https://doi.org/10.1016/j.jare.2023.08.002)

2. **Cantlay, S., Garrison, N. L., Patterson, R., Wagner, K., Kirk, Z., Fan, J., Primerano, D. A., Sullivan, M. L. G., Franks, J. M., Stolz, D. B., & Horzempa, J.** (2024). Phenotypic and transcriptional characterization of F. tularensis LVS during transition into a viable but non-culturable state. *Frontiers in Microbiology*, 15. DOI:[10.3389/fmicb.2024.1347488](https://doi.org/10.3389/fmicb.2024.1347488)

3. **Pazos-Rojas, L. A., Cuellar-Sánchez, A., Romero-Cerón, A. L., Rivera-Urbalejo, A., Van Dillewijn, P., Luna-Vital, D. A., Muñoz-Rojas, J., Morales-García, Y. E., & Bustillos-Cristales, M. del R.** (2023). The viable but non-culturable (VBNC) state, a poorly explored aspect of beneficial bacteria. *Microorganisms*, 12(1), 39. DOI:[10.3390/microorganisms12010039](https://doi.org/10.3390/microorganisms12010039)

4. **Zhang, J., Yang, H., Li, J., Hu, J., Lin, G., Tan, B. K., & Lin, S.** (2023). Current perspectives on viable but non-culturable foodborne pathogenic bacteria: A review. *Foods*, 12(6), 1179. DOI:[10.3390/foods12061179](https://doi.org/10.3390/foods12061179)

5. **Prosdocimi, E. M., Arioli, S., Mapelli, F., Zeaiter, Z., Fusi, M., Daffonchio, D., Borin, S., & Crotti, E.** (2023). Cell phenotype changes and oxidative stress response in Vibrio spp. induced into viable but non-culturable (VBNC) state. *Annals of Microbiology*, 73, 1–13. DOI:[10.1186/s13213-022-01703-6](https://doi.org/10.1186/s13213-022-01703-6)

6. **Santos, L. S., Rossi, D. A., Braz, R. F., Fonseca, B. B., Guidotti-Takeuchi, M., Alves, R. N., Beletti, M. E., Almeida-Souza, H. O., Maia, L. P., de Souza Santos, P., de Souza, J. B., & de Melo, R. T.** (2023). Roles of viable but non-culturable state in the survival of Campylobacter jejuni. *Frontiers in Cellular and Infection Microbiology*, 13. DOI:[10.3389/fcimb.2023.1122450](https://doi.org/10.3389/fcimb.2023.1122450)

7. **Riffaud, C. M., Rucks, E. A., & Ouellette, S. P.** (2023). Persistence of obligate intracellular pathogens: alternative strategies to overcome host-specific stresses. *Frontiers in Cellular and Infection Microbiology*, 13. DOI:[10.3389/fcimb.2023.1185571](https://doi.org/10.3389/fcimb.2023.1185571)

8. **Fernández-García, L., Song, S., Kirigo, J., Battisti, M. E., Petersen, M. E., Tomás, M., & Wood, T. K.** (2024). Toxin/antitoxin systems induce persistence and work in concert with restriction/modification systems to inhibit phage. *Microbiology Spectrum*, 12(1). DOI:[10.1128/spectrum.03388-23](https://doi.org/10.1128/spectrum.03388-23)

9. **Nyström, T.** (2003). Nonculturable bacteria: programmed survival forms or cells at death's door? *BioEssays*, 25(3), 204–211. DOI:[10.1002/bies.10233](https://doi.org/10.1002/bies.10233)

10. **Kędzierska, B., & Hayes, F.** (2016). Emerging roles of toxin-antitoxin modules in bacterial pathogenesis. *Molecules*, 21(6), 790. DOI:[10.3390/molecules21060790](https://doi.org/10.3390/molecules21060790)

11. **LeRoux, M., Culviner, P. H., Liu, Y. J., Littlehale, M. L., & Laub, M. T.** (2020). Stress can induce transcription of toxin-antitoxin systems without activating toxin. *Molecular Cell*, 79(2), 280–292.e8. DOI:[10.1016/j.molcel.2020.05.028](https://doi.org/10.1016/j.molcel.2020.05.028)

12. **Makarova, K. S., Wolf, Y. I., & Koonin, E. V.** (2009). Comprehensive comparative-genomic analysis of Type 2 toxin-antitoxin systems and related mobile stress response systems in prokaryotes. *Biology Direct*, 4, 19. DOI:[10.1186/1745-6150-4-19](https://doi.org/10.1186/1745-6150-4-19)

13. **Ostyn, E., Augagneur, Y., & Pinel-Marie, M.-L.** (2025). Insight into the environmental cues modulating the expression of bacterial toxin–antitoxin systems. *FEMS Microbiology Reviews*, 49. DOI:[10.1093/femsre/fuaf007](https://doi.org/10.1093/femsre/fuaf007)

---

## 9. Conclusion

The VBNC state (traitmech:000081) is a complex, reversible dormancy phenotype driven by environmental stress, oxidative damage, stringent response, and toxin-antitoxin systems. Recent mechanistic advances (2023–2024) highlight the central role of ATP-mediated NAD⁺ biosynthesis in resuscitation, oxidative stress modulation via catalase and pyruvate, and quorum-sensing signaling in *Vibrio* species. The proposed causal graph integrates entities from GO, CHEBI, ENVO, and EC ontologies, with organism-specific genes annotated by label pending NCBI Gene or UniProt mapping. Caution is advised for taxon-specific edges (Rpf, AI-2, virulence genes), assay-dependent claims (CTC toxicity), and metabolomic associations lacking mechanistic validation. Future curation should prioritize experimentally validated edges (genetic knockouts, resuscitation assays) and flag uncertain or review-only claims for further validation.

References

1. (pazosrojas2023theviablebut pages 1-2): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 91 citations.

2. (prosdocimi2023cellphenotypechanges pages 1-2): Erica M. Prosdocimi, Stefania Arioli, Francesca Mapelli, Zahraa Zeaiter, Marco Fusi, Daniele Daffonchio, Sara Borin, and Elena Crotti. Cell phenotype changes and oxidative stress response in vibrio spp. induced into viable but non-culturable (vbnc) state. Annals of Microbiology, 73:1-13, Jan 2023. URL: https://doi.org/10.1186/s13213-022-01703-6, doi:10.1186/s13213-022-01703-6. This article has 13 citations and is from a peer-reviewed journal.

3. (pazosrojas2023theviablebut pages 11-13): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 91 citations.

4. (yang2024resuscitationofviable pages 13-13): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

5. (nystrom2003nonculturablebacteriaprogrammed pages 1-2): Thomas Nyström. Nonculturable bacteria: programmed survival forms or cells at death's door? BioEssays, 25:204-211, Mar 2003. URL: https://doi.org/10.1002/bies.10233, doi:10.1002/bies.10233. This article has 134 citations and is from a peer-reviewed journal.

6. (santos2023rolesofviable pages 4-7): Leticia Silva Santos, Daise Aparecida Rossi, Raquelline Figueiredo Braz, Belchiolina Beatriz Fonseca, Micaela Guidotti–Takeuchi, Rosiane Nascimento Alves, Marcelo Emílio Beletti, Hebreia Oliveira Almeida-Souza, Larissa Prado Maia, Paula de Souza Santos, Jéssica Brito de Souza, and Roberta Torres de Melo. Roles of viable but non-culturable state in the survival of campylobacter jejuni. Frontiers in Cellular and Infection Microbiology, Mar 2023. URL: https://doi.org/10.3389/fcimb.2023.1122450, doi:10.3389/fcimb.2023.1122450. This article has 28 citations.

7. (cantlay2024phenotypicandtranscriptional pages 5-6): Stuart Cantlay, Nicole L. Garrison, Rachelle Patterson, Kassey Wagner, Zoei Kirk, Jun Fan, Donald A. Primerano, Mara L. G. Sullivan, Jonathan M. Franks, Donna B. Stolz, and Joseph Horzempa. Phenotypic and transcriptional characterization of f. tularensis lvs during transition into a viable but non-culturable state. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347488, doi:10.3389/fmicb.2024.1347488. This article has 8 citations and is from a peer-reviewed journal.

8. (santos2023rolesofviable pages 7-9): Leticia Silva Santos, Daise Aparecida Rossi, Raquelline Figueiredo Braz, Belchiolina Beatriz Fonseca, Micaela Guidotti–Takeuchi, Rosiane Nascimento Alves, Marcelo Emílio Beletti, Hebreia Oliveira Almeida-Souza, Larissa Prado Maia, Paula de Souza Santos, Jéssica Brito de Souza, and Roberta Torres de Melo. Roles of viable but non-culturable state in the survival of campylobacter jejuni. Frontiers in Cellular and Infection Microbiology, Mar 2023. URL: https://doi.org/10.3389/fcimb.2023.1122450, doi:10.3389/fcimb.2023.1122450. This article has 28 citations.

9. (zhang2023currentperspectiveson pages 4-5): Jiawen Zhang, Haoqing Yang, Jing Li, Jiamiao Hu, Guanyuan Lin, Bee K. Tan, and Shaoling Lin. Current perspectives on viable but non-culturable foodborne pathogenic bacteria: a review. Foods, 12:1179, Mar 2023. URL: https://doi.org/10.3390/foods12061179, doi:10.3390/foods12061179. This article has 54 citations.

10. (zhang2023currentperspectiveson pages 10-12): Jiawen Zhang, Haoqing Yang, Jing Li, Jiamiao Hu, Guanyuan Lin, Bee K. Tan, and Shaoling Lin. Current perspectives on viable but non-culturable foodborne pathogenic bacteria: a review. Foods, 12:1179, Mar 2023. URL: https://doi.org/10.3390/foods12061179, doi:10.3390/foods12061179. This article has 54 citations.

11. (pazosrojas2023theviablebut pages 21-21): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 91 citations.

12. (yang2024resuscitationofviable pages 1-2): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

13. (yang2024resuscitationofviable pages 9-10): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

14. (pazosrojas2023theviablebut pages 13-14): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 91 citations.

15. (yang2024resuscitationofviable pages 10-13): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

16. (pazosrojas2023theviablebut pages 4-5): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 91 citations.

17. (cantlay2024phenotypicandtranscriptional pages 9-10): Stuart Cantlay, Nicole L. Garrison, Rachelle Patterson, Kassey Wagner, Zoei Kirk, Jun Fan, Donald A. Primerano, Mara L. G. Sullivan, Jonathan M. Franks, Donna B. Stolz, and Joseph Horzempa. Phenotypic and transcriptional characterization of f. tularensis lvs during transition into a viable but non-culturable state. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347488, doi:10.3389/fmicb.2024.1347488. This article has 8 citations and is from a peer-reviewed journal.

18. (cantlay2024phenotypicandtranscriptional pages 10-12): Stuart Cantlay, Nicole L. Garrison, Rachelle Patterson, Kassey Wagner, Zoei Kirk, Jun Fan, Donald A. Primerano, Mara L. G. Sullivan, Jonathan M. Franks, Donna B. Stolz, and Joseph Horzempa. Phenotypic and transcriptional characterization of f. tularensis lvs during transition into a viable but non-culturable state. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347488, doi:10.3389/fmicb.2024.1347488. This article has 8 citations and is from a peer-reviewed journal.

19. (zhang2023currentperspectiveson pages 7-9): Jiawen Zhang, Haoqing Yang, Jing Li, Jiamiao Hu, Guanyuan Lin, Bee K. Tan, and Shaoling Lin. Current perspectives on viable but non-culturable foodborne pathogenic bacteria: a review. Foods, 12:1179, Mar 2023. URL: https://doi.org/10.3390/foods12061179, doi:10.3390/foods12061179. This article has 54 citations.

20. (zhang2023currentperspectiveson pages 13-14): Jiawen Zhang, Haoqing Yang, Jing Li, Jiamiao Hu, Guanyuan Lin, Bee K. Tan, and Shaoling Lin. Current perspectives on viable but non-culturable foodborne pathogenic bacteria: a review. Foods, 12:1179, Mar 2023. URL: https://doi.org/10.3390/foods12061179, doi:10.3390/foods12061179. This article has 54 citations.

21. (zhang2023currentperspectiveson pages 14-15): Jiawen Zhang, Haoqing Yang, Jing Li, Jiamiao Hu, Guanyuan Lin, Bee K. Tan, and Shaoling Lin. Current perspectives on viable but non-culturable foodborne pathogenic bacteria: a review. Foods, 12:1179, Mar 2023. URL: https://doi.org/10.3390/foods12061179, doi:10.3390/foods12061179. This article has 54 citations.

22. (zhang2023currentperspectiveson pages 5-7): Jiawen Zhang, Haoqing Yang, Jing Li, Jiamiao Hu, Guanyuan Lin, Bee K. Tan, and Shaoling Lin. Current perspectives on viable but non-culturable foodborne pathogenic bacteria: a review. Foods, 12:1179, Mar 2023. URL: https://doi.org/10.3390/foods12061179, doi:10.3390/foods12061179. This article has 54 citations.

23. (pazosrojas2023theviablebut pages 7-8): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 91 citations.

24. (pazosrojas2023theviablebut pages 15-17): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 91 citations.

25. (pazosrojas2023theviablebut pages 10-11): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 91 citations.

26. (prosdocimi2023cellphenotypechanges pages 5-7): Erica M. Prosdocimi, Stefania Arioli, Francesca Mapelli, Zahraa Zeaiter, Marco Fusi, Daniele Daffonchio, Sara Borin, and Elena Crotti. Cell phenotype changes and oxidative stress response in vibrio spp. induced into viable but non-culturable (vbnc) state. Annals of Microbiology, 73:1-13, Jan 2023. URL: https://doi.org/10.1186/s13213-022-01703-6, doi:10.1186/s13213-022-01703-6. This article has 13 citations and is from a peer-reviewed journal.