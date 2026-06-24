---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:42:49.406284'
end_time: '2026-06-18T12:52:49.464130'
duration_seconds: 600.06
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
  causal_graph_summary: 'vbnc_stress_induced_dormancy: 3 nodes, 2 edges'
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
- **Trait label:** viable but nonculturable state
- **METPO identifier:** traitmech:000081
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A dormancy state in which cells remain viable and minimally metabolically active but lose the ability to grow on routine culture media, regaining culturability upon resuscitation.
- **Parent traits:** traitmech:000080
- **Synonyms:** VBNC state
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00200.x:  (Oliver reviews the viable-but-nonculturable state, in which stressed cells stay viable yet unculturable until resuscitated.) | DOI:10.1038/nrmicro2504:  (Lennon & Jones frame the VBNC state within the broader microbial dormancy seed-bank concept.)
- **Existing causal graph summary:** vbnc_stress_induced_dormancy: 3 nodes, 2 edges

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
- **METPO identifier:** traitmech:000081
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A dormancy state in which cells remain viable and minimally metabolically active but lose the ability to grow on routine culture media, regaining culturability upon resuscitation.
- **Parent traits:** traitmech:000080
- **Synonyms:** VBNC state
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00200.x:  (Oliver reviews the viable-but-nonculturable state, in which stressed cells stay viable yet unculturable until resuscitated.) | DOI:10.1038/nrmicro2504:  (Lennon & Jones frame the VBNC state within the broader microbial dormancy seed-bank concept.)
- **Existing causal graph summary:** vbnc_stress_induced_dormancy: 3 nodes, 2 edges

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


## Curation-Focused Research Report: Viable but Nonculturable (VBNC) State (METPO: traitmech:000081)

### Scope Summary (Trait Scope)
The **viable but nonculturable (VBNC) state** is a **reversible dormancy-like physiological state** in which bacterial cells remain alive/viable but **fail to form colonies on routine culture media**, and can **regain culturability upon resuscitation**. This state is repeatedly framed as a survival strategy under stress, with cells showing **low metabolic activity** while retaining measurable viability signals (e.g., membrane integrity, residual ATP, transcripts). Recent sources reiterate that VBNC cells can remain **metabolically active** and may retain **virulence potential**, creating a detection gap for culture-based diagnostics in food, clinical, and environmental contexts. (izgordu2024understandingthetransition pages 1-2, prosdocimi2023cellphenotypechanges pages 1-2)

**Boundary cases / distinctions important for TraitMech curation**:
- **VBNC vs dead cells**: VBNC are alive by viability assays and/or resuscitation, whereas dead cells lack these signals; however, staining can misclassify some dead cells, so VBNC designation should ideally include **resuscitation** or **multi-assay confirmation**. (pazosrojas2023theviablebut pages 10-11)
- **VBNC vs persisters**: VBNC are **nonculturable** on routine media; persisters are typically described as a **culturable** subpopulation with antibiotic tolerance (the Bartonella study explicitly contrasts VBNC drug tolerance with stationary-phase/persister-rich populations). (gou2024viablebutnonculturable pages 1-2)
- **VBNC vs sporulation**: VBNC may show “resistance structures resembling spores” in some taxa, but it is not a defined developmental sporulation program; treat spore formation as a separate trait unless supported by taxon-specific evidence. (pazosrojas2023theviablebut pages 1-2)

### Key Concepts and Current Understanding (2023–2024 emphasis)
#### 1) Induction conditions (environmental and experimental)
VBNC induction is linked to diverse stresses, including:
- **Cold + starvation in seawater microcosms** (Vibrio spp.). (prosdocimi2023cellphenotypechanges pages 1-2)
- **Nutrient limitation / long-term storage** (Rhodococcus erythropolis). (polivtseva2024identificationcharacterizationand pages 2-4)
- **Oxidative stress/ROS** and stresses that elevate ROS during VBNC entry (foodborne pathogen-focused review). (zhang2023currentperspectiveson pages 4-5)
- **Temperature, metals, antibiotics, nutrient/osmotic stress** (E. coli VBNC biomarker study; broad induction contexts). (izgordu2024understandingthetransition pages 1-2)
- **Host-relevant triggers**: **fever-range temperature** and **antibiotic exposure** induced VBNC in Bartonella henselae. (gou2024viablebutnonculturable pages 1-2)

#### 2) Cellular and physiological hallmarks
Across taxa, VBNC cells commonly show:
- **Morphological miniaturization (“dwarfing”)** and changes in nucleic acid content (Vibrio). (prosdocimi2023cellphenotypechanges pages 1-2)
- Structural remodeling (review synthesis): thickened envelopes, altered membrane fatty acids, peptidoglycan changes, nucleoid compaction. (pazosrojas2023theviablebut pages 11-13)
- Metabolic shifts with **reduced nutrient transport/respiration** and altered macromolecular synthesis (review synthesis). (pazosrojas2023theviablebut pages 1-2, pazosrojas2023theviablebut pages 11-13)

#### 3) Mechanistic modules and regulatory themes
Recent synthesis and mechanistic work converge on several causal modules:
- **Stringent response / (p)ppGpp**: Foodborne VBNC review highlights that **RelA/SpoT activity increases (p)ppGpp**, supporting stress adaptation during VBNC entry. (zhang2023currentperspectiveson pages 4-5)
- **Toxin–antitoxin systems**: implicated in reducing metabolic turnover in VBNC-associated dormancy programs (review synthesis). (zhang2023currentperspectiveson pages 4-5)
- **General stress sigma factor RpoS**: Review-level evidence indicates **RpoS is expressed in VBNC and required for resuscitation** in some contexts, suggesting a candidate regulatory node for curation (taxon- and assay-dependent). (pazosrojas2023theviablebut pages 11-13)

### Recent Developments and Latest Research (prioritizing 2023–2024)
#### A) ATP-mediated NAD+ synthesis as a resuscitation driver (primary mechanistic study, 2024)
A major 2024 mechanistic advance proposes and tests that **residual intracellular ATP fuels NAD+ synthesis during the resuscitation lag phase**, enabling restoration of redox metabolism and exit from VBNC. In E. coli O157:H7, residual ATP levels correlate with lag length and resuscitation success, and ATP depletion blocks resuscitation. (yang2024resuscitationofviable pages 9-10, yang2024resuscitationofviable pages 6-9)

Key mechanistic entities with explicit evidence:
- **ATP** as a limiting resource for resuscitation; **CCCP-mediated ATP depletion prevented resuscitation**. (yang2024resuscitationofviable pages 6-9)
- NAD+ biosynthesis via **Preiss–Handler and salvage pathways**, with upregulation of **pncB, nadD, nadE, nadR** during resuscitation. (yang2024resuscitationofviable pages 9-10)
- Proposed downstream consequences: restored **TCA cycle flux** and **oxidative phosphorylation**, and increased nascent protein synthesis. (yang2024resuscitationofviable pages 9-10)

This “ATP → NAD+ → restored energy metabolism” model is particularly actionable for a TraitMech causal graph because it provides a coherent chain of mechanistic entities and perturbation evidence. (yang2024resuscitationofviable pages 6-9, yang2024resuscitationofviable pages 9-10)

#### B) Oxidative stress control gates resuscitation (Vibrio study, 2023)
In Vibrio spp. VBNC systems, oxidative stress is not only an inducer but a resuscitation gate:
- **Hydrogen peroxide at 0.007 mM prevented resuscitation** (quantitative threshold). (prosdocimi2023cellphenotypechanges pages 1-2)
- Resuscitation/culturability could be preserved by plating with **catalase**. (prosdocimi2023cellphenotypechanges pages 1-2)
- Loss of culturability associated with decreased **KatG (periplasmic catalase) expression/activity**. (prosdocimi2023cellphenotypechanges pages 1-2)

These data support curation of oxidative-stress and catalase-related edges, with a caution that the quantitative threshold is genus-/assay-context specific. (prosdocimi2023cellphenotypechanges pages 1-2)

#### C) Resuscitation-promoting factors (Rpf) as muralytic “bacterial cytokines” (review + applied environmental study, 2024)
Two 2024 Microorganisms papers emphasize **Rpf proteins** as potent resuscitation factors:
- Rpf proteins are described as autocrine growth factors / “bacterial cytokines” with **lysozyme-like peptidoglycan hydrolase activity**, structurally consistent with a c-type lysozyme fold and conserved catalytic residues. (li2024resuscitationpromotionfactor pages 1-3)
- Rpf is described to “degrade… peptidoglycan of VBNC cells, and trigger reanimation,” and Rpf-like genes are distributed across actinobacteria (Mycobacterium, Rhodococcus, etc.). (polivtseva2024identificationcharacterizationand pages 2-4)

### Current Applications and Real-World Implementations
#### 1) Food safety: viability ddPCR with intercalating dyes to detect VBNC pathogens (2024)
A 2024 Microbiology Spectrum study demonstrates an implementation-ready detection workflow for VBNC Salmonella in flour:
- ddPCR achieved **LOD ~3 copies/µL** and **LOQ ~3×10^1 copies/µL**, outperforming qPCR (LOD 8 copies/µL; LOQ 550 copies/µL). (li2024quantitativedetectionand pages 7-9, li2024quantitativedetectionand pages 4-7)
- After pasteurization (culture-negative), ddPCR with viability dyes still detected **10^1–10^2 gene copies/µL**, supporting a VBNC/viable-signal risk in culture-negative foods. (li2024quantitativedetectionand pages 15-17)
- Quantitative survival metrics in flour include plate-count decay from **3×10^5 to 8×10^2 CFU/g**, and D values (1-log reduction time) at 4°C of **6.58 d (plate)** and **6.40 d (FDA)**; dye/ddPCR-based D values differed by temperature and dye, consistent with physiological-state shifts. (li2024quantitativedetectionand pages 11-13)
- Public-health framing: the paper notes **a 2023 flour-linked Salmonella outbreak causing 14 infections across 13 U.S. states**, and **22 recalls/outbreaks involving raw flour (2017–2022)**, highlighting why VBNC-capable detection matters in low-water-activity foods. (li2024quantitativedetectionand pages 1-2)

These results support curating “assay nodes” for VBNC detection and also provide usable quantitative statistics. (li2024quantitativedetectionand pages 7-9, li2024quantitativedetectionand pages 11-13)

#### 2) Clinical microbiology: VBNC under fever/antibiotics and diagnostic escape (2024)
Bartonella henselae, a zoonotic pathogen often difficult to culture, was shown to enter VBNC under clinically relevant conditions:
- **38.8°C induced VBNC after 19 days**; bactericidal antibiotics induced VBNC **within 4 days**. (gou2024viablebutnonculturable pages 1-2)
- VBNC confirmation used **PMA-qPCR and SYBR Green I/PI staining**, with successful resuscitation using **sheep-blood-supplemented medium**, implicating heme/iron as an important factor for revival. (gou2024viablebutnonculturable pages 1-2, gou2024viablebutnonculturable pages 8-9)
- Proteomics indicated upregulation of invasion and stress-resistance proteins, and VBNC cells showed **faster invasion of HUVECs (12–18 h)** than log-phase cells (24–30 h typical in their context). (gou2024viablebutnonculturable pages 8-9)

These findings motivate curation of “host fever temperature” and “antibiotic exposure” as VBNC induction factors in host-associated pathogens, with explicit induction times and assay definitions. (gou2024viablebutnonculturable pages 1-2, gou2024viablebutnonculturable pages 2-3)

#### 3) Environmental biotechnology/bioremediation: resuscitating dormant degraders with Rpf (2024)
Rpf-mediated resuscitation is also presented as a tool to recover functional degraders:
- Rpf addition/resuscitation has been associated with enhanced biodegradation performance (expanded phenolic substrate range; increased oil degradation; enrichment of naphthalene degraders), suggesting potential “biostimulation” strategies in polluted environments. (polivtseva2024identificationcharacterizationand pages 2-4, polivtseva2024identificationcharacterizationand pages 15-16)

### Expert Opinions and Analytical Synthesis (authoritative views)
- Reviews emphasize VBNC as both **underestimated and controversial**, with strong consensus on “culture-negative but viable” phenotypes but continuing uncertainty on **universal genetic determinants** and the fact that **no single definitive VBNC assay exists**, requiring multi-modal evidence. (pazosrojas2023theviablebut pages 10-11, pazosrojas2023theviablebut pages 14-15)
- Food-safety reviews emphasize VBNC as a driver of **false negatives** in culture-based monitoring and highlight oxidative stress and global stress-response networks ((p)ppGpp, TA systems) as recurring mechanistic themes. (zhang2023currentperspectiveson pages 4-5)
- Mechanistic primary work (ATP/NAD+) suggests a tractable strategy to **block resuscitation** by targeting metabolic restart processes, with direct implications for interventions that seek to prevent “revival” in foods. (yang2024resuscitationofviable pages 6-9, yang2024resuscitationofviable pages 9-10)

### Candidate Nodes (grouped for TraitMech causal graph)

#### Trait node
- **VBNC state** — METPO: **traitmech:000081** (given)

#### Environmental / experimental factors (ENVO or label-only)
- Cold temperature; starvation/nutrient limitation; osmotic stress; oxidative stress / ROS; disinfectants/chlorination; UV exposure; antibiotics; fever-range temperature (38.8°C). (prosdocimi2023cellphenotypechanges pages 1-2, polivtseva2024identificationcharacterizationand pages 2-4, izgordu2024understandingthetransition pages 1-2, gou2024viablebutnonculturable pages 1-2)

#### Genes / proteins / complexes (NCBI Gene/UniProt grounding should be taxon-specific)
- **relA, spoT** (stringent response); **rpoS**; **katG**; **pncB, nadD, nadE, nadR**; **rfaL/waaL** (O-antigen ligase; LPS synthesis); **DnaK–ClpB** disaggregation system; **Rpf family proteins**. (zhang2023currentperspectiveson pages 4-5, prosdocimi2023cellphenotypechanges pages 1-2, yang2024resuscitationofviable pages 9-10, yang2024resuscitationofviable pages 6-9, yang2024resuscitationofviable pages 2-4, li2024resuscitationpromotionfactor pages 1-3)

#### Pathways / processes (GO/KEGG/MetaCyc candidates)
- Stringent response / (p)ppGpp metabolism; quorum sensing (AI-2); oxidative stress response; NAD+ biosynthesis (Preiss–Handler, salvage); TCA cycle; oxidative phosphorylation; protein disaggregation/proteostasis; peptidoglycan remodeling/hydrolysis. (zhang2023currentperspectiveson pages 4-5, prosdocimi2023cellphenotypechanges pages 1-2, yang2024resuscitationofviable pages 9-10, li2024resuscitationpromotionfactor pages 1-3)

#### Chemicals / metabolites (CHEBI candidates)
- ATP (CHEBI:15422), NAD+ (CHEBI:15846), hydrogen peroxide (CHEBI:16240), sodium pyruvate (CHEBI:15361), CCCP (CHEBI:68553). (yang2024resuscitationofviable pages 6-9, yang2024resuscitationofviable pages 9-10, prosdocimi2023cellphenotypechanges pages 1-2, zhang2023currentperspectiveson pages 4-5)

#### Assays / observational nodes (OBI candidates or label-only)
- Plate counts (CFU), PMA-qPCR, ddPCR (invA), SYBR Green I/PI staining, flow cytometry, CTC reduction, DFA-DVC, ATR-FTIR biomarkers (995 cm−1 RNA band), TBARS lipid peroxidation. (li2024quantitativedetectionand pages 7-9, gou2024viablebutnonculturable pages 1-2, prosdocimi2023cellphenotypechanges pages 1-2, izgordu2024understandingthetransition pages 1-2)

### Evidence-Backed Candidate Causal Edges (Triples)
The following artifact table provides candidate subject–predicate–object edges, with supporting snippets, DOIs, URLs, and curation notes (including uncertainty flags).

| Edge (Subject —predicate→ Object) | Node type(s) | Suggested ontology grounding | Evidence snippet (verbatim/near-verbatim) | Source (DOI + year) and URL | Curation notes (strength/limitations, taxon-specific, assay-specific) |
|---|---|---|---|---|---|
| Low temperature + starvation in seawater —induces→ VBNC state | environmental factor → trait | ENVO:cold environment?; starvation (label-only); METPO:traitmech:000081 | “VBNC state, as a consequence of starvation in seawater at low temperatures” (prosdocimi2023cellphenotypechanges pages 1-2) | 10.1186/s13213-022-01703-6 (2023) https://doi.org/10.1186/s13213-022-01703-6 | Strong induction evidence in Vibrio spp.; taxon-specific but broadly consistent with VBNC literature. |
| Nutrient limitation —induces→ VBNC state | environmental factor → trait | nutrient limitation (label-only); METPO:traitmech:000081 | “form viable but nonculturable (VBNC) forms during long-term storage under nutrient limitation” (polivtseva2024identificationcharacterizationand pages 2-4) | 10.3390/microorganisms12122662 (2024) https://doi.org/10.3390/microorganisms12122662 | Strong for Rhodococcus erythropolis 7Ba; long-term storage context may be assay-specific. |
| Oxidative stress / ROS increase —promotes→ VBNC entry | process/chemical stress → trait | GO:0006979 response to oxidative stress; reactive oxygen species CHEBI:26523; METPO:traitmech:000081 | “Oxidative stress is a major trigger: ROS… increase during VBNC entry” (zhang2023currentperspectiveson pages 4-5) | 10.3390/foods12061179 (2023) https://doi.org/10.3390/foods12061179 | Review-level synthesis across foodborne pathogens; mechanistically broad, not one single taxon. |
| Disinfectants / chlorination / preservatives —induce→ VBNC state | chemical treatment → trait | sodium hypochlorite CHEBI:32146; hydrogen peroxide CHEBI:16240; chlorination (label-only); METPO:traitmech:000081 | “anthropogenic inducers cited include… wastewater chlorination, and food preservatives” (pazosrojas2023theviablebut pages 1-2) | 10.3390/microorganisms12010039 (2023/2024 issue) https://doi.org/10.3390/microorganisms12010039 | Review evidence; curate as broad environmental/experimental trigger, but chemical-specific edges may need primary-source confirmation. |
| relA/spoT activity —increases→ (p)ppGpp accumulation | genes → metabolite/process | relA (label-only); spoT (label-only); (p)ppGpp CHEBI:120092? | “elevated activity of the relA and spoT genes upon entry into the VBNC state leads to the accumulation of (p)ppGpp” (zhang2023currentperspectiveson pages 4-5) | 10.3390/foods12061179 (2023) https://doi.org/10.3390/foods12061179 | Good mechanistic review edge; gene grounding may be taxon-specific orthologs. |
| (p)ppGpp accumulation —enhances→ stress resistance | metabolite/process → process | (p)ppGpp CHEBI candidate; stress resistance (label-only) | “accumulation of (p)ppGpp, enhancing stress resistance” (zhang2023currentperspectiveson pages 4-5) | 10.3390/foods12061179 (2023) https://doi.org/10.3390/foods12061179 | Supports regulatory layer upstream of VBNC maintenance; indirect edge to VBNC. |
| Toxin–antitoxin systems —reduce→ metabolic turnover | regulatory module → process | toxin-antitoxin system GO:0106003? label-only safer | “Toxin–antitoxin (TA) systems contribute by reducing metabolic turnover” (zhang2023currentperspectiveson pages 4-5) | 10.3390/foods12061179 (2023) https://doi.org/10.3390/foods12061179 | Review evidence; broad and likely species-dependent. |
| RpoS —required_for→ resuscitation from VBNC | sigma factor → process | rpoS (label-only); GO:0009408 response to heat?; resuscitation (label-only) | “RpoS… is expressed in VBNC cells and is required for resuscitation with current methods; RpoS mutants lose cultivability and fail to resuscitate” (pazosrojas2023theviablebut pages 11-13) | 10.3390/microorganisms12010039 (2023/2024 issue) https://doi.org/10.3390/microorganisms12010039 | Useful candidate edge; comes from review summarizing primary studies, so mark as supported but context-dependent. |
| Decreased KatG/catalase activity —associates_with→ loss of culturability / VBNC | enzyme → trait/process | katG (label-only); catalase EC:1.11.1.6 | “loss of culturability are associated with a ‘decrease in the expression of the periplasmic catalase KatG and of catalase activity’” (prosdocimi2023cellphenotypechanges pages 1-2) | 10.1186/s13213-022-01703-6 (2023) https://doi.org/10.1186/s13213-022-01703-6 | Strong in Vibrio microcosms; association close to causation but still taxon-specific. |
| Hydrogen peroxide —prevents→ resuscitation from VBNC | chemical → process | CHEBI:16240 | “Hydrogen peroxide at concentrations as low as 0.007 mM prevented resuscitation” (prosdocimi2023cellphenotypechanges pages 1-2) | 10.1186/s13213-022-01703-6 (2023) https://doi.org/10.1186/s13213-022-01703-6 | Strong experimental edge with quantitative threshold; Vibrio-specific conditions. |
| Catalase addition —preserves/restores→ culturability of VBNC cells | enzyme/treatment → process | catalase EC:1.11.1.6 | “the potential of culturability of VBNC cells could be preserved… by plating the cells in the presence of catalase” (prosdocimi2023cellphenotypechanges pages 1-2) | 10.1186/s13213-022-01703-6 (2023) https://doi.org/10.1186/s13213-022-01703-6 | Assay-specific restoration edge; suitable as resuscitation-support factor. |
| Sodium pyruvate —inhibits→ VBNC production under oxidative/thermal stress | chemical → trait/process | CHEBI:15361 | “pretreatment of Salmonella with sodium pyruvate radical scavenger before thermal sonication reportedly inhibited VBNC production” (zhang2023currentperspectiveson pages 4-5) | 10.3390/foods12061179 (2023) https://doi.org/10.3390/foods12061179 | Review evidence from Salmonella study; likely via ROS scavenging. |
| Sodium pyruvate —promotes→ resuscitation from VBNC | chemical → process | CHEBI:15361 | “small molecules such as sodium pyruvate… implicated” in resuscitation; “low temperature induces a sodium-pyruvate-recoverable VBNC state” (pazosrojas2023theviablebut pages 14-15, pazosrojas2023theviablebut pages 21-21) | 10.3390/microorganisms12010039 (2023/2024 issue) https://doi.org/10.3390/microorganisms12010039 | Supported by review synthesis; curate as uncertain/broad until taxon-specific primary evidence is attached. |
| Quorum sensing / AI-2 —restores→ catalase expression and culturable state | signaling process → enzyme/trait | AI-2 CHEBI:? label-only; quorum sensing GO:0009372 | “Quorum sensing signal AI-2… implicated in restoring catalase (katG) and the culturable state” (prosdocimi2023cellphenotypechanges pages 1-2) | 10.1186/s13213-022-01703-6 (2023) https://doi.org/10.1186/s13213-022-01703-6 | Mechanistically attractive but evidence summarized in Vibrio-focused paper; taxon-specific. |
| ATP availability —promotes→ VBNC resuscitation efficiency | metabolite → process | ATP CHEBI:15422 | “higher ATP levels… correlated with higher resuscitation efficiency” (yang2024resuscitationofviable pages 1-2) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 | Strong primary mechanistic evidence in E. coli O157:H7. |
| ATP depletion by CCCP —prevents→ resuscitation from VBNC | chemical treatment → process | CCCP CHEBI:68553 | “Artificial ATP depletion with CCCP reduced ATP levels and prevented resuscitation even after 28 h” (yang2024resuscitationofviable pages 6-9) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 | Strong causal perturbation edge; taxon-specific to E. coli system tested. |
| Residual ATP —drives→ NAD+ synthesis during resuscitating lag phase | metabolite → pathway/process | ATP CHEBI:15422; NAD+ CHEBI:15846; Preiss-Handler pathway (label-only); salvage pathway (label-only) | “part of cellular ATP is consumed during the lag phase to synthesize NAD+” (yang2024resuscitationofviable pages 9-10) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 | High-value mechanistic edge directly suitable for graph curation. |
| pncB / nadD / nadE / nadR upregulation —increases→ NAD+ biosynthesis during resuscitation | genes/pathway enzymes → metabolite | pncB, nadD, nadE, nadR (label-only); NAD+ CHEBI:15846 | “Elevated expression of nadR, nadD, pncB and nadE was observed in resuscitating DrfaL cells” (yang2024resuscitationofviable pages 9-10) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 | Strong gene-to-process evidence; primary data in E. coli O157:H7. |
| NAD+ synthesis —restores→ TCA cycle flux and oxidative phosphorylation | pathway/metabolite → metabolic processes | NAD+ CHEBI:15846; TCA cycle GO:0006099; oxidative phosphorylation GO:0006119 | “ATP-mediated NAD+ synthesis increases NAD+ availability, restoring TCA cycle flux… and drive oxidative phosphorylation” (yang2024resuscitationofviable pages 9-10) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 | Strong mechanistic proposal from metabolomics + gene expression; some steps are inferred rather than directly enzymatically proven. |
| DnaK-ClpB disaggregation system —restores→ proteostasis during resuscitation | chaperone complex → process | DnaK (label-only); ClpB (label-only); protein disaggregation GO:0016236 | “The ATP-fueled DnaK-ClpB bichaperone system can disaggregate these protein aggregates, restore proteostasis” (yang2024resuscitationofviable pages 2-4) | 10.1016/j.jare.2023.08.002 (2024) https://doi.org/10.1016/j.jare.2023.08.002 | Mechanistic inference from cited literature within primary paper; useful but should be marked uncertain unless primary direct demonstration is added. |
| Rpf protein —hydrolyzes→ peptidoglycan | secreted protein/enzyme → cell wall polymer | Rpf family (label-only/UniProt varies); peptidoglycan GO:0009273 | “Rpf ‘acts on the bacterial cell wall, degrades the cell wall peptidoglycan of VBNC cells, and triggers reanimation’” (polivtseva2024identificationcharacterizationand pages 2-4) | 10.3390/microorganisms12122662 (2024) https://doi.org/10.3390/microorganisms12122662 | Strong review/secondary statement with supporting lineage; broadly applicable in GC-rich Gram-positives. |
| Rpf peptidoglycan hydrolase activity —triggers→ reanimation / resuscitation | enzymatic activity → process | peptidoglycan hydrolase activity GO:0009253; resuscitation (label-only) | “lysozyme-like peptidoglycan hydrolases that can resuscitate dormant bacteria” (li2024resuscitationpromotionfactor pages 1-3) | 10.3390/microorganisms12081528 (2024) https://doi.org/10.3390/microorganisms12081528 | Strong mechanistic review; exact downstream signal may vary by taxon. |
| PMA / DyeTox13 / EMA coupled to ddPCR —detects→ viable/VBNC Salmonella when plate counts fail | assay reagent + assay → assay-observed property | PMA CHEBI: label-only; EMA CHEBI: label-only; ddPCR (label-only) | “could quantify viable cells at low concentrations when the plate counting method failed to detect them post-inactivation” (li2024quantitativedetectionand pages 1-2) | 10.1128/spectrum.00249-24 (2024) https://doi.org/10.1128/spectrum.00249-24 | Detection edge, not biology edge; useful for TraitMech assay metadata rather than causal mechanism. |
| Flow cytometry —tracks→ phenotype changes during VBNC induction/resuscitation | assay → assay-observed property | flow cytometry OBI:0000716 | “used ‘flow cytometry in microcosm experiments’ alongside plating to follow phenotype and resuscitation” (prosdocimi2023cellphenotypechanges pages 1-2) | 10.1186/s13213-022-01703-6 (2023) https://doi.org/10.1186/s13213-022-01703-6 | Assay edge only; good for scope and evidence model, not a causal biological relation. |


*Table: This table lists candidate subject-predicate-object edges for curating a causal graph of the viable but nonculturable state, spanning induction triggers, regulatory systems, oxidative stress defenses, resuscitation pathways, and assay linkages. It is useful for prioritizing strongly supported versus uncertain or taxon-specific edges for TraitMech curation.*

### Relevant Statistics and Quantitative Data (recent)
- **Hydrogen peroxide threshold for blocking resuscitation**: 0.007 mM prevented resuscitation in Vibrio VBNC experiments. (prosdocimi2023cellphenotypechanges pages 1-2)
- **VBNC Bartonella induction timing**: VBNC after 19 days at 38.8°C; within 4 days with bactericidal antibiotics. (gou2024viablebutnonculturable pages 1-2)
- **ddPCR analytical performance** in VBNC Salmonella workflow: LOD ~3 copies/µL; LOQ ~3×10^1 copies/µL; qPCR LOQ 550 copies/µL. (li2024quantitativedetectionand pages 7-9, li2024quantitativedetectionand pages 4-7)
- **Salmonella survival kinetics in flour**: plate counts declined 3×10^5→8×10^2 CFU/g; D values at 4°C: 6.58 d (plate) and 6.40 d (FDA). (li2024quantitativedetectionand pages 11-13)
- **Public-health context**: flour-linked Salmonella outbreak (2023) with 14 infections across 13 U.S. states; 22 recalls/outbreaks involving raw flour (2017–2022). (li2024quantitativedetectionand pages 1-2)

### Warnings / Claims Not Yet Ready for TraitMech Curation
1. **Over-generalizing regulatory requirements** (e.g., “RpoS is required for resuscitation”) should be curated as **taxon-specific** unless primary evidence is attached for the target taxon; current support here is largely review synthesis. (pazosrojas2023theviablebut pages 11-13)
2. **Single-assay VBNC calls are risky**: membrane-integrity stains and some viability assays can misclassify dead cells; VBNC designation should ideally require **resuscitation evidence** or convergent assays. (pazosrojas2023theviablebut pages 10-11)
3. **Rpf applicability across Gram-negative taxa**: some sources claim broad cross-phyla resuscitation, but mechanistic enzymology and necessity/sufficiency vary; curate Rpf edges with explicit taxon context and avoid universal claims without primary data per lineage. (polivtseva2024identificationcharacterizationand pages 2-4, li2024resuscitationpromotionfactor pages 1-3)
4. **Metabolic pathway edges inferred from omics** (e.g., NAD+ restoring TCA/OXPHOS) are plausible but may involve inference; they should be marked “mechanistic model” unless direct flux/enzymology evidence is extracted. (yang2024resuscitationofviable pages 9-10)

---

## DOI-First Bibliography (2023–2024 prioritized; with URLs and publication dates where available)

1. **Yang D, Wang W, Zhao L, Rao L, Liao X.** Resuscitation of viable but nonculturable bacteria promoted by ATP-mediated NAD+ synthesis. *Journal of Advanced Research.* **Jun 2024**. DOI: **10.1016/j.jare.2023.08.002**. URL: https://doi.org/10.1016/j.jare.2023.08.002 (yang2024resuscitationofviable pages 9-10)

2. **Li L, Bae S.** Quantitative detection and survival analysis of VBNC *Salmonella* Typhimurium in flour using droplet digital PCR and DNA-intercalating dyes. *Microbiology Spectrum.* **Aug 2024**. DOI: **10.1128/spectrum.00249-24**. URL: https://doi.org/10.1128/spectrum.00249-24 (li2024quantitativedetectionand pages 11-13)

3. **Gou Y-P, et al.** Viable but nonculturable state in the zoonotic pathogen *Bartonella henselae* induced by low-grade fever temperature and antibiotic treatment. *Frontiers in Cellular and Infection Microbiology.* **Nov 2024**. DOI: **10.3389/fcimb.2024.1486426**. URL: https://doi.org/10.3389/fcimb.2024.1486426 (gou2024viablebutnonculturable pages 1-2)

4. **Cantlay S, et al.** Phenotypic and transcriptional characterization of *F. tularensis* LVS during transition into a viable but non-culturable state. *Frontiers in Microbiology.* **Feb 2024**. DOI: **10.3389/fmicb.2024.1347488**. URL: https://doi.org/10.3389/fmicb.2024.1347488 (cantlay2024phenotypicandtranscriptional pages 2-3)

5. **Li X, Ren Q, Sun Z, Wu Y, Pan H.** Resuscitation Promotion Factor: A Pronounced Bacterial Cytokine in Propelling Bacterial Resuscitation. *Microorganisms.* **Jul 2024**. DOI: **10.3390/microorganisms12081528**. URL: https://doi.org/10.3390/microorganisms12081528 (li2024resuscitationpromotionfactor pages 1-3)

6. **Polivtseva VN, et al.** Identification, Characterization, and Ultrastructure Analysis of the Phenol-Degrading *Rhodococcus erythropolis* 7Ba and Its Viable but Nonculturable Forms. *Microorganisms.* **Dec 2024**. DOI: **10.3390/microorganisms12122662**. URL: https://doi.org/10.3390/microorganisms12122662 (polivtseva2024identificationcharacterizationand pages 2-4)

7. **İzgördü ÖK, Gurbanov R, Darcan C.** Understanding the transition to viable but non-culturable state in *Escherichia coli* W3110: a comprehensive analysis of potential spectrochemical biomarkers. *World Journal of Microbiology & Biotechnology.* **May 2024**. DOI: **10.1007/s11274-024-04019-6**. URL: https://doi.org/10.1007/s11274-024-04019-6 (izgordu2024understandingthetransition pages 1-2)

8. **Prosdocimi EM, et al.** Cell phenotype changes and oxidative stress response in *Vibrio* spp. induced into viable but non-culturable (VBNC) state. *Annals of Microbiology.* **Jan 2023**. DOI: **10.1186/s13213-022-01703-6**. URL: https://doi.org/10.1186/s13213-022-01703-6 (prosdocimi2023cellphenotypechanges pages 1-2)

9. **Zhang J, et al.** Current perspectives on viable but non-culturable foodborne pathogenic bacteria: a review. *Foods.* **Mar 2023**. DOI: **10.3390/foods12061179**. URL: https://doi.org/10.3390/foods12061179 (zhang2023currentperspectiveson pages 4-5)

10. **Pazos-Rojas LA, et al.** The Viable but Non-Culturable (VBNC) State, a Poorly Explored Aspect of Beneficial Bacteria. *Microorganisms.* **Dec 2023** (issue **2024**, vol 12(1) per journal numbering). DOI: **10.3390/microorganisms12010039**. URL: https://doi.org/10.3390/microorganisms12010039 (pazosrojas2023theviablebut pages 11-13)


References

1. (izgordu2024understandingthetransition pages 1-2): Özge Kaygusuz İzgördü, Rafig Gurbanov, and Cihan Darcan. Understanding the transition to viable but non-culturable state in escherichia coli w3110: a comprehensive analysis of potential spectrochemical biomarkers. World Journal of Microbiology & Biotechnology, May 2024. URL: https://doi.org/10.1007/s11274-024-04019-6, doi:10.1007/s11274-024-04019-6. This article has 8 citations and is from a peer-reviewed journal.

2. (prosdocimi2023cellphenotypechanges pages 1-2): Erica M. Prosdocimi, Stefania Arioli, Francesca Mapelli, Zahraa Zeaiter, Marco Fusi, Daniele Daffonchio, Sara Borin, and Elena Crotti. Cell phenotype changes and oxidative stress response in vibrio spp. induced into viable but non-culturable (vbnc) state. Annals of Microbiology, 73:1-13, Jan 2023. URL: https://doi.org/10.1186/s13213-022-01703-6, doi:10.1186/s13213-022-01703-6. This article has 10 citations and is from a peer-reviewed journal.

3. (pazosrojas2023theviablebut pages 10-11): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 83 citations.

4. (gou2024viablebutnonculturable pages 1-2): Yu-Ping Gou, Dongxia Liu, Yuxian Xin, Ting Wang, Jiaxing Li, Yiwen Xi, Xiaoling Zheng, Tuanjie Che, Ying Zhang, Tingting Li, and Jie Feng. Viable but nonculturable state in the zoonotic pathogen bartonella henselae induced by low-grade fever temperature and antibiotic treatment. Frontiers in Cellular and Infection Microbiology, Nov 2024. URL: https://doi.org/10.3389/fcimb.2024.1486426, doi:10.3389/fcimb.2024.1486426. This article has 5 citations.

5. (pazosrojas2023theviablebut pages 1-2): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 83 citations.

6. (polivtseva2024identificationcharacterizationand pages 2-4): Valentina N. Polivtseva, Anton N. Zvonarev, Olesya I. Sazonova, Yanina A. Delegan, Yulia N. Kocharovskaya, Alexander G. Bogun, and Nataliya E. Suzina. Identification, characterization, and ultrastructure analysis of the phenol-degrading rhodococcus erythropolis 7ba and its viable but nonculturable forms. Microorganisms, 12:2662, Dec 2024. URL: https://doi.org/10.3390/microorganisms12122662, doi:10.3390/microorganisms12122662. This article has 4 citations.

7. (zhang2023currentperspectiveson pages 4-5): Jiawen Zhang, Haoqing Yang, Jing Li, Jiamiao Hu, Guanyuan Lin, Bee K. Tan, and Shaoling Lin. Current perspectives on viable but non-culturable foodborne pathogenic bacteria: a review. Foods, 12:1179, Mar 2023. URL: https://doi.org/10.3390/foods12061179, doi:10.3390/foods12061179. This article has 47 citations.

8. (pazosrojas2023theviablebut pages 11-13): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 83 citations.

9. (yang2024resuscitationofviable pages 9-10): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

10. (yang2024resuscitationofviable pages 6-9): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

11. (li2024resuscitationpromotionfactor pages 1-3): Xinxin Li, Qing Ren, Zhanbin Sun, Yanan Wu, and Hanxu Pan. Resuscitation promotion factor: a pronounced bacterial cytokine in propelling bacterial resuscitation. Microorganisms, 12:1528, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081528, doi:10.3390/microorganisms12081528. This article has 10 citations.

12. (li2024quantitativedetectionand pages 7-9): Liyan Li and Sungwoo Bae. Quantitative detection and survival analysis of vbnc <i>salmonella</i> typhimurium in flour using droplet digital pcr and dna-intercalating dyes. Aug 2024. URL: https://doi.org/10.1128/spectrum.00249-24, doi:10.1128/spectrum.00249-24. This article has 6 citations and is from a domain leading peer-reviewed journal.

13. (li2024quantitativedetectionand pages 4-7): Liyan Li and Sungwoo Bae. Quantitative detection and survival analysis of vbnc <i>salmonella</i> typhimurium in flour using droplet digital pcr and dna-intercalating dyes. Aug 2024. URL: https://doi.org/10.1128/spectrum.00249-24, doi:10.1128/spectrum.00249-24. This article has 6 citations and is from a domain leading peer-reviewed journal.

14. (li2024quantitativedetectionand pages 15-17): Liyan Li and Sungwoo Bae. Quantitative detection and survival analysis of vbnc <i>salmonella</i> typhimurium in flour using droplet digital pcr and dna-intercalating dyes. Aug 2024. URL: https://doi.org/10.1128/spectrum.00249-24, doi:10.1128/spectrum.00249-24. This article has 6 citations and is from a domain leading peer-reviewed journal.

15. (li2024quantitativedetectionand pages 11-13): Liyan Li and Sungwoo Bae. Quantitative detection and survival analysis of vbnc <i>salmonella</i> typhimurium in flour using droplet digital pcr and dna-intercalating dyes. Aug 2024. URL: https://doi.org/10.1128/spectrum.00249-24, doi:10.1128/spectrum.00249-24. This article has 6 citations and is from a domain leading peer-reviewed journal.

16. (li2024quantitativedetectionand pages 1-2): Liyan Li and Sungwoo Bae. Quantitative detection and survival analysis of vbnc <i>salmonella</i> typhimurium in flour using droplet digital pcr and dna-intercalating dyes. Aug 2024. URL: https://doi.org/10.1128/spectrum.00249-24, doi:10.1128/spectrum.00249-24. This article has 6 citations and is from a domain leading peer-reviewed journal.

17. (gou2024viablebutnonculturable pages 8-9): Yu-Ping Gou, Dongxia Liu, Yuxian Xin, Ting Wang, Jiaxing Li, Yiwen Xi, Xiaoling Zheng, Tuanjie Che, Ying Zhang, Tingting Li, and Jie Feng. Viable but nonculturable state in the zoonotic pathogen bartonella henselae induced by low-grade fever temperature and antibiotic treatment. Frontiers in Cellular and Infection Microbiology, Nov 2024. URL: https://doi.org/10.3389/fcimb.2024.1486426, doi:10.3389/fcimb.2024.1486426. This article has 5 citations.

18. (gou2024viablebutnonculturable pages 2-3): Yu-Ping Gou, Dongxia Liu, Yuxian Xin, Ting Wang, Jiaxing Li, Yiwen Xi, Xiaoling Zheng, Tuanjie Che, Ying Zhang, Tingting Li, and Jie Feng. Viable but nonculturable state in the zoonotic pathogen bartonella henselae induced by low-grade fever temperature and antibiotic treatment. Frontiers in Cellular and Infection Microbiology, Nov 2024. URL: https://doi.org/10.3389/fcimb.2024.1486426, doi:10.3389/fcimb.2024.1486426. This article has 5 citations.

19. (polivtseva2024identificationcharacterizationand pages 15-16): Valentina N. Polivtseva, Anton N. Zvonarev, Olesya I. Sazonova, Yanina A. Delegan, Yulia N. Kocharovskaya, Alexander G. Bogun, and Nataliya E. Suzina. Identification, characterization, and ultrastructure analysis of the phenol-degrading rhodococcus erythropolis 7ba and its viable but nonculturable forms. Microorganisms, 12:2662, Dec 2024. URL: https://doi.org/10.3390/microorganisms12122662, doi:10.3390/microorganisms12122662. This article has 4 citations.

20. (pazosrojas2023theviablebut pages 14-15): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 83 citations.

21. (yang2024resuscitationofviable pages 2-4): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

22. (pazosrojas2023theviablebut pages 21-21): Laura Abisaí Pazos-Rojas, Alma Cuellar-Sánchez, Ana Laura Romero-Cerón, América Rivera-Urbalejo, Pieter Van Dillewijn, Diego Armando Luna-Vital, Jesús Muñoz-Rojas, Yolanda Elizabeth Morales-García, and María del Rocío Bustillos-Cristales. The viable but non-culturable (vbnc) state, a poorly explored aspect of beneficial bacteria. Microorganisms, 12:39, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010039, doi:10.3390/microorganisms12010039. This article has 83 citations.

23. (yang2024resuscitationofviable pages 1-2): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

24. (cantlay2024phenotypicandtranscriptional pages 2-3): Stuart Cantlay, Nicole L. Garrison, Rachelle Patterson, Kassey Wagner, Zoei Kirk, Jun Fan, Donald A. Primerano, Mara L. G. Sullivan, Jonathan M. Franks, Donna B. Stolz, and Joseph Horzempa. Phenotypic and transcriptional characterization of f. tularensis lvs during transition into a viable but non-culturable state. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347488, doi:10.3389/fmicb.2024.1347488. This article has 8 citations and is from a peer-reviewed journal.