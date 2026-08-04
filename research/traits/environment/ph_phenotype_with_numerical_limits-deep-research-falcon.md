---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:44:45.417832'
end_time: '2026-08-04T02:55:04.933942'
duration_seconds: 619.52
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH phenotype with numerical limits
  trait_identifier: METPO:1000531
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by specific pH values or ranges that define
    growth or activity limits.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports
    external pH as the quantitative axis underlying acidophile, neutrophile, and alkaliphile
    classification.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis
    review supports the proton motive force across the cell envelope as the physical
    link between external pH and microbial growth physiology.)'
  causal_graph_summary: 'ph_phenotype_numerical_axis: 15 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000531
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific pH values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports external pH as the quantitative axis underlying acidophile, neutrophile, and alkaliphile classification.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force across the cell envelope as the physical link between external pH and microbial growth physiology.)
- **Existing causal graph summary:** ph_phenotype_numerical_axis: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **pH phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** pH phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000531
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific pH values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports external pH as the quantitative axis underlying acidophile, neutrophile, and alkaliphile classification.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force across the cell envelope as the physical link between external pH and microbial growth physiology.)
- **Existing causal graph summary:** ph_phenotype_numerical_axis: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **pH phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_phenotype_with_numerical_limits.yaml`.

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


# Curation report: microbial “pH phenotype with numerical limits”

## Executive summary

**Target trait:** **“METPO:1000531”** — pH phenotype with numerical limits  
**Category:** ENVIRONMENT | **Kind:** CLASS | **Mapping:** REVIEWED  
**Parent:** METPO:1000059

The most defensible interpretation is an **experimentally observed quantitative response norm to external pH**: the minimum, optimum, and/or maximum pH at which a defined microbial entity exhibits a specified endpoint, normally growth or metabolic activity. It is not simply a qualitative label such as acidophile, neutrophile, or alkaliphile. It is also not synonymous with intracellular pH, acid-shock survival, proton-motive force (PMF), or microbial alteration of medium pH.

The causal backbone best supported across taxa is:

> **external pH → transmembrane ΔpH/Δψ and proton stress → cytoplasmic-pH homeostasis and energetic cost → growth/activity response → observed numerical pH limit**.

Mechanistic branches include proton-translocating ATPases, Na+/H+ and K+/H+ antiporters, the Mrp complex, amino-acid decarboxylation systems such as GadBC, membrane and cell-surface adaptations, and metabolic production or consumption of acids/bases. These mechanisms are not universal: directionality can reverse between acid and alkaline conditions, ATPases may synthesize ATP or hydrolyze it to expel H+, and the importance of individual modules is strongly taxon- and assay-dependent (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 3-5).

## 1. Trait scope and curation model

### 1.1 Recommended operational definition

For TraitMech, represent **“METPO:1000531”** as:

> An assay-conditioned phenotype characterized by one or more numerical external-pH values—minimum, optimum, maximum, or tested growth/activity range—at which a specified microorganism, strain, or microbial community meets a defined growth or activity criterion.

A complete observation should carry:

1. organism or community identity;
2. minimum, optimum, and/or maximum pH;
3. endpoint—growth rate, biomass, colony formation, methane oxidation, nitrification, product formation, etc.;
4. threshold used to define a limit;
5. medium, buffer, carbon and energy sources, salinity, temperature, oxygen/aeration, and incubation time;
6. whether pH was initial, continuously controlled, or measured after microbial modification;
7. planktonic, biofilm, chemostat, batch, or environmental context.

This conditioning is essential. Carbon source can determine whether cultures acidify or alkalinize their medium, and buffering can materially alter the trajectory. Thus, an initial-pH treatment is not necessarily the pH actually experienced throughout growth (sanchezclemente2020carbonsourceinfluence pages 1-3).

### 1.2 Minimum, optimum, and maximum

* **Minimum growth/activity pH:** lowest tested or modeled external pH meeting a prespecified endpoint.
* **Optimum pH:** pH giving the maximal value of the stated endpoint under the stated conditions.
* **Maximum growth/activity pH:** highest pH meeting that endpoint.
* **Tested range:** interval over which growth or activity was observed; it should not automatically be treated as the physiological minimum–maximum range if more extreme values were not tested.

The trait should preserve whether a value is an exact observation, an interval, or a censored limit such as “growth below pH 4” or “no growth at the next tested pH.” Genome-derived predictions should be separate evidence objects, not equivalent to measured limits. A 2024 amino-acid-composition model was useful at broad scale but had lower performance for pH than for several other conditions and greater error at extremes; independently predicted minimum, optimum, and maximum values could also be internally inconsistent (barnum2024predictingmicrobialgrowth pages 14-16).

### 1.3 Boundary cases

| Nearby concept | Relationship to target trait | Curation recommendation |
|---|---|---|
| Acidophile/neutrophile/alkaliphile | Qualitative ecological class inferred from a quantitative axis | Do not substitute for numerical limits; derive only when a controlled vocabulary supplies explicit rules. |
| Intracellular pH | Homeostatic state mediating external-pH tolerance | Mechanistic node, not the target phenotype. Neutralophiles can maintain cytoplasmic pH around 7.5–7.7 across a much wider external range (krulwich2011molecularaspectsof pages 1-3). |
| Acid or alkali survival | Viability without growth | Separate phenotype unless the target endpoint explicitly allows survival. *E. coli* survival at gastric pH is not evidence of growth at that pH (krulwich2011molecularaspectsof pages 1-3). |
| pH optimum of an isolated enzyme | Biochemical property of a molecule | Exclude unless linked experimentally to organismal growth/activity limits. |
| Organism-driven pH change | Effect of metabolism on the environment | Curate as a causal input to experienced pH, not as the organism’s pH limit (sanchezclemente2020carbonsourceinfluence pages 1-3). |
| Community abundance along a field pH gradient | Ecological association | Useful supporting evidence but not a direct organismal growth limit. |
| Acid resistance after adaptation | History-dependent stress response | Record preconditioning, exposure time, and endpoint; do not merge automatically with steady-state growth range. |

## 2. Current mechanistic understanding

External pH alters both components of the PMF: the chemical gradient, ΔpH, and electrical potential, Δψ. Acidophiles resist proton influx and often maintain a positive-inside potential; alkaliphiles must capture scarce external protons and use a large negative Δψ, cation/proton antiport, and proton-retaining surfaces. These processes stabilize cytoplasmic pH and preserve transport, ATP production, macromolecular stability, and enzyme function (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5).

Quantitatively, the foundational review reports that many neutralophiles grow over approximately external pH 5.5–9 while maintaining cytoplasmic pH near 7.5–7.7. *Acidithiobacillus ferrooxidans* can grow around pH 2, whereas *Bacillus pseudofirmus* OF4 grows at external pH 10.5 while maintaining internal pH about 8.3 (krulwich2011molecularaspectsof pages 1-3). These are exemplars, not universal class cutoffs.

In alkaliphilic *Bacillus*, Mrp-mediated Na+/H+ antiport is especially strong causal evidence: mutation of **mrpA** in *B. halodurans* C-125 eliminates alkaline-pH homeostasis and the alkaliphilic phenotype. Alkaliphile-adapted ATP synthase also takes up protons during ATP synthesis; replacing characteristic subunit motifs impairs activity particularly at pH 10.5 and compromises high-pH growth (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23).

At low pH, neutralophiles use several nonexclusive routes. ATP hydrolysis can drive H+ extrusion; respiratory proton pumps can increase; membranes can become less proton-permeable; and proton-consuming reactions can buffer the cytoplasm. GadB converts glutamate to γ-aminobutyrate while consuming a proton, while GadC exchanges extracellular glutamate for intracellular GABA. This mechanism is highly effective in organisms carrying the system but should not be generalized to all microbes (krulwich2011molecularaspectsof pages 5-6).

## 3. Candidate graph nodes

CURIEs below are conservative candidates. Database release and term semantics should be checked during YAML validation; where a stable identifier was not established from the evidence, a label-only node is preferable.

### 3.1 Trait and environmental/experimental nodes

* **“METPO:1000531”** — pH phenotype with numerical limits.
* **METPO:1000059** — supplied parent trait.
* External pH; initial pH; time-resolved pH; buffered pH; minimum growth pH; optimum growth pH; maximum growth pH — **label-only candidates**.
* Growth rate, biomass yield, survival, metabolic-activity rate, product titer, washout — label-only endpoint nodes.
* Medium composition, buffer capacity, carbon source, temperature, salinity, oxygen availability, aeration, incubation time, and biofilm state — experimental-context nodes.

### 3.2 Chemicals and electrochemical entities

* **CHEBI:15378** — proton.
* **CHEBI:29101** — sodium ion.
* **CHEBI:29103** — potassium ion.
* **CHEBI:29985** — L-glutamate.
* **CHEBI:16865** — γ-aminobutyric acid/GABA.
* **CHEBI:17148** — putrescine.
* **CHEBI:15422** — ATP.
* Proton motive force, transmembrane ΔpH, membrane potential/Δψ, buffer capacity — retain as labels unless the target ontology set supplies validated terms.

### 3.3 Cellular locations and structures

* **GO:0005737** — cytoplasm.
* **GO:0016020** — membrane.
* Cell envelope, extracellular medium, S-layer, acidic secondary cell-wall polymers, teichuronic acid/teichuronopeptide, membrane-bound cytochrome c, and biofilm matrix — label-only where exact grounding remains uncertain.

### 3.4 Genes, proteins, and complexes

* Proton-transporting F-type ATPase/ATP synthase; candidate complex grounding **GO:0045259**.
* V-type sodium/proton-translocating ATPase — label-only pending organism-specific complex identification.
* **NhaA**, **NhaB**, and related Na+/H+ or K+/H+ antiporters.
* **MrpA–MrpG** multiple-resistance-and-pH antiporter complex.
* **GadB** glutamate decarboxylase and **GadC** glutamate/GABA antiporter.
* Respiratory-chain proton pumps; hydrogenase-3; potassium-uptake transporters; urease; arginine-deiminase pathway; carbonic anhydrase; acid-sensing two-component systems.
* Membrane fatty-acid remodeling enzymes and cyclopropane-fatty-acid synthesis machinery.

Gene nodes should be tied to a taxon-specific identifier such as UniProt only after the strain is fixed. A generic gene symbol should not be assigned a single cross-taxon UniProt CURIE.

### 3.5 Processes and modules

* Cytoplasmic-pH homeostasis.
* Proton transmembrane transport.
* Oxidative phosphorylation.
* Glutamate-dependent acid resistance/GadBC cycle.
* GABA metabolism.
* Cation/proton antiport.
* Proton retention at the cell surface.
* Membrane-lipid remodeling and reduction of proton permeability.
* Ammonia-generating acid neutralization.
* Organic-acid production/consumption and medium acidification/alkalinization.

## 4. Candidate evidence-backed causal edges

The compact high-confidence edge set is summarized here:

| subject | predicate | object | context/taxon | evidence strength | DOI |
|---|---|---|---|---|---|
| external pH | shapes | transmembrane ΔpH and proton motive force (PMF) | broad bacteria; foundational pH-homeostasis model | strong, broad review-supported (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) | 10.1038/nrmicro2549 |
| transmembrane ΔpH and PMF | contribute to maintenance of | cytoplasmic pH homeostasis | broad bacteria | strong, broad review-supported (krulwich2011molecularaspectsof pages 1-3) | 10.1038/nrmicro2549 |
| cytoplasmic pH homeostasis | enables | growth at external pH extremes | broad bacteria; e.g. alkaliphiles and acidophiles | strong, broad review-supported (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 1-3) | 10.1038/nrmicro2549 |
| F1F0-ATPase / ATP synthase | translocates protons and supports | pH homeostasis and growth under acidic or alkaline conditions | taxon-specific across bacteria; acid-stressed *Clostridium thermocellum* and alkaliphilic *Bacillus* | strong, but context-dependent (whitham2018clostridiumthermocellumll1210 pages 1-2, krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6) | 10.1186/s13068-018-1095-y; 10.1038/nrmicro2549 |
| low external pH | upregulates | F1F0-ATPase expression | *Clostridium thermocellum* LL1210 chemostat cultures near pH 6.24 | strong, taxon- and assay-specific (whitham2018clostridiumthermocellumll1210 pages 1-2) | 10.1186/s13068-018-1095-y |
| Na+/H+ antiporter NhaA | imports protons in exchange for Na+ and thereby supports | alkaline pH homeostasis | neutralophilic/alkaline-stressed bacteria; exemplar from review | moderate to strong, transporter-specific but not universal (krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 |
| Mrp cation/proton antiporter | is central to | alkaline pH homeostasis | alkaliphilic *Bacillus* spp. and diverse bacteria/archaea | strong for alkaliphiles, taxon-specific (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23) | 10.1038/nrmicro2549; 10.3389/fmicb.2017.02325 |
| mrpA mutation / loss of Mrp function | abolishes | alkaliphilic phenotype and alkaline pH homeostasis | *Bacillus halodurans* C-125 | strong, causal mutant evidence but taxon-specific (krulwich2011molecularaspectsof pages 12-14) | 10.1038/nrmicro2549 |
| glutamate decarboxylase GadB | consumes | cytoplasmic protons during glutamate decarboxylation to GABA | acid-stressed neutralophilic bacteria; exemplar *E. coli* | strong, mechanism well established but taxon-specific distribution (krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 |
| GadC glutamate/GABA antiporter | couples | glutamate import with GABA export in acid resistance | acid-resistant bacteria carrying gadBC | moderate to strong, operon-specific (krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 |
| acidic secondary cell wall polymers / negatively charged cell surface | retain protons near cell surface and support | growth at high external pH | alkaliphilic *Bacillus* and related alkaliphiles | strong for alkaliphiles, taxon-specific (krulwich2011molecularaspectsof pages 12-14, goto2022differencesinbioenergetic pages 1-2) | 10.1038/nrmicro2549; 10.3389/fmicb.2022.842785 |
| membrane lipid remodeling | alters | proton permeability and pH-stress tolerance | methanotrophs across acidic vs alkaline habitats | moderate, comparative/ecophysiological evidence (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond pages 1-2) | 10.3389/fmicb.2022.1034164 |
| saturated or remodeled membrane lipids | reduce | proton permeability under acidic stress | acidophilic methanotrophs | moderate, taxon-specific review evidence (yao2023howmethanotrophsrespond pages 5-7) | 10.3389/fmicb.2022.1034164 |
| exogenous putrescine | enhances | glutamate-based acid resistance and GABA metabolic pathway | activated-sludge biofilm communities under acidic stress | moderate, community-level and condition-specific (jiang2024exogenousputrescineplays pages 12-14) | 10.1128/aem.00569-24 |
| exogenous putrescine | stimulates | ATPase expression and H+ transmembrane transport | activated-sludge biofilm communities under acidic stress | moderate, community-level and condition-specific (jiang2024exogenousputrescineplays pages 12-14) | 10.1128/aem.00569-24 |
| medium composition / carbon source | modulates observed | extracellular pH trajectory and apparent pH phenotype | aerobic cultures of *E. coli*, *Pseudomonas putida*, *P. pseudoalcaligenes* | strong for assay dependence, not a universal homeostasis mechanism (sanchezclemente2020carbonsourceinfluence pages 1-3) | 10.3390/genes11111292 |


*Table: This table summarizes the most curation-ready causal edges linking external pH to microbial growth limits and homeostasis mechanisms for METPO:1000531. It emphasizes broad mechanisms first, then clearly labels taxon- or assay-specific edges that should be curated with scope constraints.*

The following expanded table supplies curation-oriented snippets and qualifications. Snippets are intentionally short; quotation marks indicate wording closely matching the retrieved source.

| Proposed subject–predicate–object triple | Reference and supporting snippet | Curation note |
|---|---|---|
| external pH → alters → transmembrane ΔpH and Δψ | Krulwich et al.: PMF comprises “transmembrane pH gradient (ΔpH) and electrical potential (Δψ)” (krulwich2011molecularaspectsof pages 1-3) | **Strong/general.** Core physical edge; retain direction-specific state in acid versus alkali. |
| ΔpH + Δψ → support → cytoplasmic-pH homeostasis | Same review: external-pH extremes are handled through PMF-dependent homeostasis (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) | **Strong/general**, but not sufficient alone to specify a numerical limit. |
| cytoplasmic-pH homeostasis → enables → growth across external-pH range | Neutralophiles maintain pH 7.5–7.7 while growing across roughly external pH 5.5–9; *B. pseudofirmus* grows at pH 10.5 with cytoplasm at 8.3 (krulwich2011molecularaspectsof pages 1-3) | **Strong mechanistic synthesis.** Quantitative examples are taxon-specific. |
| low external pH → increases expression of → F1F0-ATPase | *C. thermocellum* LL1210: “F1F0-ATPase gene expression was upregulated” near the low-pH limit (whitham2018clostridiumthermocellumll1210 pages 1-2) | **Direct but taxon/assay-specific.** Expression is not proof that the ATPase alone shifts the limit. |
| F1F0-ATPase activity → supports → acidic-pH homeostasis | LL1210 was growth-limited below pH 6.24 at dilution 0.1 h−1, with ATPase upregulation and reduced ATP-consuming functions (whitham2018clostridiumthermocellumll1210 pages 1-2) | **Moderate causal interpretation.** Curate with chemostat, strain, and pH qualifiers. |
| low pH → reallocates ATP away from motility and biosynthesis → maintenance | At pH 6.24, ATPase increased while flagellar, chemotaxis, fatty-acid synthesis, and other ATP-consuming pathways decreased (whitham2018clostridiumthermocellumll1210 pages 1-2) | **Direct systems response**, not necessarily a universal mechanism. |
| Mrp Na+/H+ antiport → imports H+ and supports → alkaline-pH homeostasis | Mrp is described as central to alkaline homeostasis; all subunits are generally needed for activity (krulwich2011molecularaspectsof pages 12-14) | **Strong for alkaliphilic Bacillaceae;** broader occurrence does not establish equal phenotypic importance in every taxon. |
| loss of mrpA → abolishes → alkaline homeostasis/alkaliphilic phenotype | “mrpA mutations…eliminate alkaliphilic phenotype and alkaline pH homeostasis” in *B. halodurans* C-125 (krulwich2011molecularaspectsof pages 12-14) | **High-confidence causal edge**, explicitly taxon-specific. |
| NhaA Na+/H+ antiport → increases H+ entry → supports growth at alkaline pH | Under alkaline conditions, electrogenic antiporters such as NhaA exchange approximately 2 H+/1 Na+ and are upregulated (krulwich2011molecularaspectsof pages 5-6) | **Strong mechanism**, but transporter identity and stoichiometry must be organism-specific. |
| alkaliphile-adapted ATP synthase → captures protons → supports ATP synthesis/high-pH growth | Motif substitutions impair ATP-synthase activity more at pH 10.5 than 7.5 and correlate with failed high-pH growth (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 22-23) | **Strong causal structure–function evidence** in alkaliphilic *Bacillus*. |
| GadB glutamate decarboxylation → consumes cytoplasmic H+ → increases acid resistance | GadB is activated during acid stress and converts glutamate to GABA while consuming a proton (krulwich2011molecularaspectsof pages 5-6) | **Strong biochemical mechanism; taxon-restricted.** Acid survival must not automatically become growth-range evidence. |
| GadC exchange → replenishes glutamate/exports GABA → sustains GadB cycle | GadBC is the glutamate-dependent acid-resistance module (krulwich2011molecularaspectsof pages 5-6) | **Mechanistically strong**, but the retrieved evidence is review-level. |
| acidic/negatively charged cell surface → retains H+ near membrane → supports high-pH bioenergetics | Acidic secondary wall components attract H+ and repel OH−; alkaliphile surfaces function as local proton collectors (goto2022differencesinbioenergetic pages 1-2) | **Strong for studied alkaliphiles**, not universal. |
| low aeration → increases membrane-bound cytochrome c → enhances local H+ retention | *Evansella clarkii* produced 2.5–6.3-fold more membrane-bound cytochrome c at low aeration; proposed as an “H+ capacitor” (goto2022differencesinbioenergetic pages 1-2) | **Taxon-specific; partly mechanistic interpretation.** Curate as uncertain unless backed by perturbation data. |
| aeration → alters → membrane potential supporting high-pH growth | *E. clarkii* Δψ was about −170 mV at high aeration versus approximately −140 mV at low aeration (goto2022differencesinbioenergetic pages 1-2) | **Quantitative association**, not a generic pH-limit edge. |
| membrane-lipid remodeling → decreases proton permeability → supports acidic-pH tolerance | Acidophilic methanotrophs use saturated/remodeled lipids, while acidic and alkaline groups alter phospholipid composition (yao2023howmethanotrophsrespond pages 5-7) | **Moderate, taxon-specific review evidence.** Exact lipid–phenotype edges require primary perturbation studies. |
| exogenous putrescine under low pH → enhances Gad/GABA metabolism and ATPase expression → improves biofilm acid adaptation | Putrescine “consumed intracellular H+” through glutamate-based resistance/GABA metabolism and stimulated ATPase-linked H+ transport (jiang2024exogenousputrescineplays pages 12-14) | **Community- and condition-specific.** At alkaline pH the effect reverses, so never curate as an unconditional positive regulator. |
| carbon source → changes extracellular pH trajectory → changes experienced pH/growth | Glucose and related substrates acidified cultures, whereas citrate and other oxidized substrates alkalinized them (sanchezclemente2020carbonsourceinfluence pages 1-3) | **Strong assay-confounder edge.** Distinguish “pH phenotype” from “pH modification phenotype.” |
| genome amino-acid composition → predicts, but does not cause → optimum pH | Sequence model errors were larger at extreme pH; predicted limits may be internally inconsistent (barnum2024predictingmicrobialgrowth pages 14-16) | **Do not curate as causal.** Prediction is evidence provenance only. |

## 5. Recent developments, quantitative findings, and applications

### 5.1 Community engineering and wastewater biofilms

A 2024 activated-sludge study showed that putrescine has a switch-like pH-dependent effect: protonated putrescine supported glutamate/GABA-mediated proton consumption and ATPase-associated proton transport under acidity, while under alkaline conditions continued intracellular H+ consumption worsened alkali stress. Acidophilic taxa were especially active below pH 4. This suggests a practical route to promote or suppress biofilm formation, but dosing and pH context are inseparable (jiang2024exogenousputrescineplays pages 12-14).

### 5.2 Methane cycling and climate-relevant microbiology

A 2023 review updates the old view that methanotrophs mainly prefer pH 6.6–7.5: both strongly acidophilic and alkaliphilic methanotrophs are now known. Their adaptations include membrane remodeling, cation/proton transport, altered membrane potential, and negatively charged S-layers. Because methanotrophs regulate terrestrial methane flux, quantitative pH niches affect both community assembly and methane-cycle models (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond pages 1-2).

### 5.3 Industrial fermentation and strain engineering

In *C. thermocellum* LL1210, growth became limiting below pH 6.24 at a chemostat dilution rate of 0.1 h−1. Glutamate abundance increased 267-fold at pH 6.24 relative to pH 6.98, while ATP-consuming functions were suppressed. These values illustrate why pH limits should be stored with growth regime and rate: the reported threshold is not a context-free species constant (whitham2018clostridiumthermocellumll1210 pages 1-2).

Low-pH operation can reduce contamination and buffering costs and can enable compatible co-cultures. A 2024 FEMS review identifies acid tolerance as a key industrial strain-screening criterion and describes applications in food preservation, fermentation, bioremediation, crop protection, chemical production, and adaptive laboratory evolution by progressively lowering pH (atasoy2024exploitationofmicrobial pages 2-3). The review also stresses that low pH can inhibit pathogens and spoilage organisms, while organic acids made by lactic-acid bacteria can provide biological preservation (atasoy2024exploitationofmicrobial pages 2-3).

### 5.4 High-pH bioenergetics and alkaline biotechnology

Alkaliphiles solve a severe proton-scarcity problem through high Δψ, Na+/H+ antiport, cell-surface proton retention, and specialized ATP synthases. In *E. clarkii*, intracellular pH is about 8.1, Δψ varies from approximately −170 to −140 mV with aeration, and membrane-bound cytochrome c increases 2.5–6.3-fold under low aeration (goto2022differencesinbioenergetic pages 1-2). These mechanisms are relevant to alkaline-waste treatment, high-pH bioconversion, and robust industrial enzymes, but the *E. clarkii* values must not be generalized to all alkaliphiles.

### 5.5 Cultivation prediction and genome-to-phenotype modeling

A 2024 perspective argues that quantitative environmental preferences are known for only a narrow fraction of bacterial diversity. Better pH-preference models could guide cultivation, probiotic design, and forecasts of community change, but complex pH homeostasis cannot reliably be inferred from one marker gene (ramoneda2024leveraginggenomicinformation pages 1-2). A 2024 preprint trained models on 15,596 bacterial and archaeal genomes and reported pH prediction around R² = 0.48, lower than salinity (R² = 0.81) and optimum temperature (R² = 0.73). Protein-localization information improved pH prediction, but precision remained inadequate for laboratory optimization and poorer at extremes (barnum2024predictingmicrobialgrowth pages 14-16). These predictions are useful for candidate prioritization, not reviewed numerical trait assertions.

## 6. Expert assessment for the TraitMech graph

### Recommended high-confidence backbone

1. external pH **alters** ΔpH and Δψ;
2. ΔpH/Δψ **create energetic and proton stress**;
3. pH-homeostasis modules **modify** cytoplasmic pH;
4. cytoplasmic-pH stability and energetic cost **modulate** growth/activity;
5. measured growth/activity across a pH series **determines** minimum, optimum, and maximum values;
6. assay factors **condition** every reported numerical limit.

### Recommended modular branches

* **Acid branch:** membrane proton exclusion; ATP-driven H+ extrusion; GadBC and other decarboxylases; ammonia-producing reactions; stress regulation.
* **Alkaline branch:** electrogenic Na+/H+ or K+/H+ antiport; Mrp; high Δψ; proton-capturing cell surfaces; adapted ATP synthase.
* **Environmental-feedback branch:** metabolism changes medium pH, which feeds back on activity and the observed limit.
* **Measurement branch:** buffer, substrate, aeration, temperature, salinity, growth mode, endpoint, and time modify the numerical observation.

The graph should therefore model the trait as the output of a **conditional causal system**, not as a direct gene-presence phenotype.

## 7. Claims that should not yet be curated as general TraitMech edges

1. **Presence of gadBC, mrp, nhaA, or an ATPase guarantees a particular pH range.** Gene presence does not establish expression, direction of transport, energetic state, or a numerical limit.
2. **A field abundance–pH association equals a growth limit.** Community interactions, dispersal, nutrients, and covarying geochemistry can produce the association.
3. **Survival at pH 2 equals growth at pH 2.** Acid challenge and sustained replication are different endpoints (krulwich2011molecularaspectsof pages 1-3).
4. **An endpoint measured at initial pH represents constant exposure.** Microbial metabolism may substantially change pH, especially in poorly buffered medium (sanchezclemente2020carbonsourceinfluence pages 1-3).
5. **All F1F0-ATPases affect pH in the same direction.** Depending on physiology, they can synthesize ATP using proton entry or hydrolyze ATP to expel protons (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6).
6. **Putrescine universally improves pH tolerance.** Its effect reverses between acidic and alkaline activated-sludge conditions (jiang2024exogenousputrescineplays pages 12-14).
7. **Cytochrome-c accumulation is a universally proven H+ capacitor.** Current evidence is compelling but species- and aeration-specific (goto2022differencesinbioenergetic pages 1-2).
8. **Membrane lipid signatures alone causally determine pH limits.** The methanotroph evidence is comparative and several proposed alkaline proton-transfer steps remain uncertain (yao2023howmethanotrophsrespond pages 5-7).
9. **Genome-predicted pH limits can be entered as reviewed phenotype values.** Current pH models have moderate accuracy and known errors at extremes (barnum2024predictingmicrobialgrowth pages 14-16).
10. **Broad class ranges are hard ontology cutoffs.** Values such as acidophile pH 1–3 or alkaliphile pH 10–13 are useful summaries, not universal definitional boundaries (krulwich2011molecularaspectsof pages 3-5).

## 8. DOI-first bibliography

1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology*. Published May 2011. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). Foundational synthesis of external pH, PMF, ATPases, antiporters, and cytoplasmic-pH homeostasis (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 1-3).
2. Whitham JM et al. **Clostridium thermocellum LL1210 pH homeostasis mechanisms informed by transcriptomics and metabolomics.** *Biotechnology for Biofuels*. Published April 2018. DOI: [10.1186/s13068-018-1095-y](https://doi.org/10.1186/s13068-018-1095-y) (whitham2018clostridiumthermocellumll1210 pages 1-2).
3. Goto T et al. **Differences in bioenergetic metabolism of obligately alkaliphilic Bacillaceae under high pH depend on the aeration conditions.** *Frontiers in Microbiology*. Published March 2022. DOI: [10.3389/fmicb.2022.842785](https://doi.org/10.3389/fmicb.2022.842785) (goto2022differencesinbioenergetic pages 1-2).
4. Yao X, Wang J, Hu B. **How methanotrophs respond to pH: a review of ecophysiology.** *Frontiers in Microbiology*. Published January 2023. DOI: [10.3389/fmicb.2022.1034164](https://doi.org/10.3389/fmicb.2022.1034164) (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond pages 1-2).
5. Ramoneda J et al. **Leveraging genomic information to predict environmental preferences of bacteria.** *The ISME Journal*. Published 2024. DOI: [10.1093/ismejo/wrae195](https://doi.org/10.1093/ismejo/wrae195) (ramoneda2024leveraginggenomicinformation pages 1-2).
6. Jiang G et al. **Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.** *Applied and Environmental Microbiology*. Published July 2024. DOI: [10.1128/aem.00569-24](https://doi.org/10.1128/aem.00569-24) (jiang2024exogenousputrescineplays pages 12-14).
7. Atasoy M et al. **Exploitation of microbial activities at low pH to enhance planetary health.** *FEMS Microbiology Reviews*. Published 2024. DOI: [10.1093/femsre/fuad062](https://doi.org/10.1093/femsre/fuad062) (atasoy2024exploitationofmicrobial pages 2-3).
8. Barnum TP et al. **Predicting microbial growth conditions from amino acid composition.** *bioRxiv* preprint. Posted March 2024. DOI: [10.1101/2024.03.22.586313](https://doi.org/10.1101/2024.03.22.586313). Treat as non-peer-reviewed unless a journal version is identified (barnum2024predictingmicrobialgrowth pages 14-16).
9. Sánchez-Clemente R et al. **Carbon source influence on extracellular pH changes along bacterial cell-growth.** *Genes*. Published October 2020. DOI: [10.3390/genes11111292](https://doi.org/10.3390/genes11111292) (sanchezclemente2020carbonsourceinfluence pages 1-3).

## Curation conclusion

For `data/traits/environment/ph_phenotype_with_numerical_limits.yaml`, the safest immediate expansion is a compact, conserved backbone from external pH through electrochemical stress and cytoplasmic-pH homeostasis to growth/activity, supplemented by explicitly scoped modules for Mrp/Nha antiport, ATPases, GadBC, and cell-envelope adaptation. Numerical values must remain attached to organism, endpoint, medium, and assay. Taxon-specific perturbation evidence—especially **mrpA** loss in alkaliphilic *Bacillus*—can support direct causal edges; transcriptomic, comparative, community-level, and genome-prediction results should be marked as contextual, uncertain, or non-causal rather than promoted to universal mechanisms.

References

1. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

4. (sanchezclemente2020carbonsourceinfluence pages 1-3): Rubén Sánchez-Clemente, M. Isabel Guijo, Juan Nogales, and Rafael Blasco. Carbon source influence on extracellular ph changes along bacterial cell-growth. Genes, 11:1292, Oct 2020. URL: https://doi.org/10.3390/genes11111292, doi:10.3390/genes11111292. This article has 76 citations.

5. (barnum2024predictingmicrobialgrowth pages 14-16): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

6. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

7. (krulwich2011molecularaspectsof pages 22-23): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

8. (whitham2018clostridiumthermocellumll1210 pages 1-2): Jason M. Whitham, Ji-Won Moon, Miguel Rodriguez, Nancy L. Engle, Dawn M. Klingeman, Thomas Rydzak, Malaney M. Abel, Timothy J. Tschaplinski, Adam M. Guss, and Steven D. Brown. Clostridium thermocellum ll1210 ph homeostasis mechanisms informed by transcriptomics and metabolomics. Biotechnology for Biofuels, Apr 2018. URL: https://doi.org/10.1186/s13068-018-1095-y, doi:10.1186/s13068-018-1095-y. This article has 27 citations.

9. (goto2022differencesinbioenergetic pages 1-2): Toshitaka Goto, Shinichi Ogami, Kazuaki Yoshimume, and Isao Yumoto. Differences in bioenergetic metabolism of obligately alkaliphilic bacillaceae under high ph depend on the aeration conditions. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.842785, doi:10.3389/fmicb.2022.842785. This article has 6 citations and is from a peer-reviewed journal.

10. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 79 citations and is from a peer-reviewed journal.

11. (yao2023howmethanotrophsrespond pages 1-2): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 79 citations and is from a peer-reviewed journal.

12. (jiang2024exogenousputrescineplays pages 12-14): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

13. (atasoy2024exploitationofmicrobial pages 2-3): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 104 citations and is from a domain leading peer-reviewed journal.

14. (ramoneda2024leveraginggenomicinformation pages 1-2): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 30 citations.