---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:41:10.410156'
end_time: '2026-08-04T02:48:54.639834'
duration_seconds: 464.23
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH optimum mid1
  trait_identifier: METPO:1000456
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_optimum_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH optimum phenotype with the best-growth external pH between approximately
    6 and 7, corresponding to neutrophilic physiology.
  parent_traits: METPO:1000331
  synonyms: Alkali Tolerant, Neutrophile, pHO_6_to_7
  evidence_summary: 'DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review
    supports a near-neutral external pH as the neutrophilic optimum, where cytoplasmic
    pH homeostasis operates with minimal load.)'
  causal_graph_summary: 'ph_optimum_mid1_neutrophile_setpoint: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000456
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH between approximately 6 and 7, corresponding to neutrophilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Neutrophile, pHO_6_to_7
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports a near-neutral external pH as the neutrophilic optimum, where cytoplasmic pH homeostasis operates with minimal load.)
- **Existing causal graph summary:** ph_optimum_mid1_neutrophile_setpoint: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **pH optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_mid1.yaml`.

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
- **Trait label:** pH optimum mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000456
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH between approximately 6 and 7, corresponding to neutrophilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Neutrophile, pHO_6_to_7
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports a near-neutral external pH as the neutrophilic optimum, where cytoplasmic pH homeostasis operates with minimal load.)
- **Existing causal graph summary:** ph_optimum_mid1_neutrophile_setpoint: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **pH optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_mid1.yaml`.

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


# Curation-focused research report: pH optimum mid1

## 1. Trait scope

**Trait:** pH optimum mid1  
**Identifier:** `METPO:1000456`  
**Category/kind:** ENVIRONMENT / CLASS  
**Parent:** `METPO:1000331`  
**Status:** REVIEWED

`METPO:1000456` should represent an **organism-level optimum-growth phenotype**: maximal or best growth occurs when external pH is approximately 6–7. It is therefore an assay-observed ecological/physiological preference, not merely the capacity to survive neutral pH. “Neutrophile” or `pHO_6_to_7` are appropriate synonyms. “Alkali tolerant” is potentially misleading because tolerance above pH 7 does not establish an optimum at pH 6–7.

Operational curation should require a growth-rate, biomass-yield, colony-development, or equivalent response measured across multiple controlled external-pH conditions. The pH of the medium should be measured during growth because metabolism can shift it substantially. In a 2024 *Bacillus subtilis* experiment, minimally buffered biofilms moved from approximately pH 5.5 back to 6.9, whereas standard buffering masked the dynamics (tran2024activephregulation pages 2-5).

### Boundary cases

- **Growth range is not optimum.** Growth from pH 5–9 does not by itself establish a pH 6–7 optimum.
- **Neutral-pH survival is not optimum.** Transient acid/alkali resistance and stationary-phase survival are stress phenotypes.
- **Enzyme pH optimum is not organismal pH optimum.** Purified-enzyme activity at pH 6–7 should not be annotated to this trait.
- **Biofilm microenvironment regulation is a mechanism/context**, not automatically proof that the planktonic organism has an organism-level pH optimum.
- **Mild acidophiles overlap the lower boundary.** Methanotroph examples include optima of 5.8–6.2 or 6.0–6.5, while a review groups most neutrophilic methanotrophs within a broader pH 6–8 range. Exact inclusion therefore depends on the METPO binning rule and assay uncertainty (yao2023howmethanotrophsrespond pages 4-5).
- **Alkaliphiles are outside scope.** Methanotrophs with optima around 8.5–10 are clear neighboring but distinct phenotypes (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond pages 4-5).

## 2. Current mechanistic interpretation

The trait is best modeled as a **system-level set point**, not as the product of one universal “neutrophile gene.” Near-neutral external pH reduces the energetic and kinetic burden of keeping cytoplasmic pH compatible with enzyme activity, membrane energetics, and growth. Conserved homeostasis modules include respiratory proton translocation, F-type ATP synthase, cation/proton antiport, potassium uptake, membrane permeability control, and metabolism that produces or consumes acids. However, the relative causal importance of these modules varies by taxon, lifestyle, salinity, oxygen availability, and buffer capacity.

A 2023 ecophysiology review describes respiratory complexes I, III, and IV as removing cytoplasmic protons, F0F1-ATPase as using returning protons for ATP synthesis, and potassium uptake as helping generate an internally positive membrane potential. These are authoritative general mechanisms, but the reviewed evidence spans acidophilic and alkaliphilic methanotrophs and does not directly demonstrate `METPO:1000456` (yao2023howmethanotrophsrespond pages 5-7).

The strongest recent direct evidence is community-level. *B. subtilis* biofilms actively altered extracellular pH toward the neutrophile range from starting pH 6–9 through a dynamic balance of acetate and acetoin metabolism; planktonic cells lacked the same behavior (tran2024activephregulation pages 5-7, tran2024activephregulation pages 1-2).

## 3. Candidate nodes grouped by type

### Trait and environmental nodes

- pH optimum mid1 — `METPO:1000456`
- external pH 6–7 / near-neutral external pH — label-only unless the project has an approved pH-range ontology term
- acidic external pH
- alkaline external pH
- minimally buffered growth medium
- buffer capacity / MOPS concentration
- biofilm microenvironment
- planktonic growth state
- salt concentration / osmotic stress

### Chemicals and ions

- proton — `CHEBI:24636`
- sodium ion — `CHEBI:29101`
- potassium ion — `CHEBI:29103`
- acetate — `CHEBI:30089`
- acetoin — `CHEBI:15688`
- pyruvate — `CHEBI:15361`
- 2-acetolactate — use only after identifier verification
- acetyl-CoA — `CHEBI:15351`
- ATP — `CHEBI:15422`
- proton motive force — process/quality node; label-only is safer than forcing a chemical identifier

### Genes, proteins, and complexes

**Direct 2024 *B. subtilis* candidates**

- `alsS` / acetolactate synthase
- `alsD` / acetolactate decarboxylase
- `ackA` / acetate kinase
- `acsA` / acetyl-CoA synthetase
- `acoA` / acetoin catabolism component—tested but not required for the observed alkalinization
- respiratory complexes represented by `ctaCD`, `qoxA`, `cydA`, and `ythB` mutants—negative evidence for any single complex being the sole source of the extracellular pH dynamic (tran2024activephregulation pages 2-5)

**Direct 2018 *Staphylococcus aureus* candidates**

- Mnh1 cation/proton antiporter complex; subunits MnhA1–MnhG1
- Mnh2 cation/proton antiporter complex; subunits MnhA2–MnhG2
- `mnhA1` and `mnhA2` knockout-tested subunits

Mnh1 catalyzed Na+/H+ antiport optimally around pH 7.5, whereas Mnh2 transported Na+ and K+ more strongly around pH 9.0. Their deletion phenotypes establish roles in salt/alkali growth rather than a universal cause of a pH 6–7 optimum (vaish2018rolesofstaphylococcus pages 6-8, vaish2018rolesofstaphylococcus pages 39-42, vaish2018rolesofstaphylococcus pages 1-3).

### Processes and functions

- intracellular/cytoplasmic pH homeostasis — `GO:0030641`
- proton transmembrane transport — `GO:1902600`
- sodium:proton antiporter activity — `GO:0015385`
- potassium:proton antiporter activity — candidate GO grounding should be checked against the current GO release
- proton motive force generation
- respiratory-chain proton pumping
- oxidative phosphorylation
- acetate biosynthesis / overflow metabolism
- acetoin biosynthesis
- extracellular acidification
- extracellular alkalinization
- biofilm formation — `GO:0042710`
- extracellular-matrix production
- growth-rate maintenance

## 4. Candidate causal edges

The compact table below separates curation-ready taxon-specific experiments from broader mechanisms that remain uncertain for this exact trait.

| subject | predicate | object | taxon/context | evidence strength | DOI |
|---|---|---|---|---|---|
| Acetate biosynthesis / transient acetate accumulation | causes | extracellular acidification during biofilm development | *Bacillus subtilis* NCIB 3610 biofilms in minimally buffered MSgg; ΔackAΔacsA reduced acidification rate by ~48% vs WT (tran2024activephregulation pages 2-5) | strong, direct, taxon-specific | 10.1128/mbio.03387-23 |
| AlsS-dependent acetoin biosynthesis | causes | extracellular alkalinization | *B. subtilis* NCIB 3610 biofilms; ΔalsS retained acidification but lost alkalinization phase; acidic start pH increased AlsS use (tran2024activephregulation pages 5-7) | strong, direct, taxon-specific | 10.1128/mbio.03387-23 |
| AlsD-dependent acetoin biosynthesis | causes | extracellular alkalinization | *B. subtilis* NCIB 3610 biofilms; ΔalsD retained acidification but lost alkalinization phase (tran2024activephregulation pages 5-7) | strong, direct, taxon-specific | 10.1128/mbio.03387-23 |
| Acetoin biosynthesis | consumes protons and thereby causes | alkalinization | *B. subtilis* biofilm context; each enzymatic step in acetoin pathway consumes a proton (tran2024activephregulation pages 5-7) | strong, direct for pathway mechanism, taxon-specific | 10.1128/mbio.03387-23 |
| Alkalinization phase | maintains | extracellular pH near 6.9 / neutrophile range | *B. subtilis* NCIB 3610 biofilms; pH dropped to ~5.5 then returned to 6.9; biofilms across starting pH 6–9 conditioned local pH to preferred neutrophile range (tran2024activephregulation pages 2-5, tran2024activephregulation pages 5-7) | strong, direct, taxon-specific | 10.1128/mbio.03387-23 |
| Neutral-pH regulation via acetoin biosynthesis | supports | biofilm cell count and matrix development in minimally buffered medium | *B. subtilis* NCIB 3610; ΔalsS showed lower CFU and altered wrinkle/matrix phenotype only in minimally buffered conditions (tran2024activephregulation pages 5-7, tran2024activephregulation pages 7-9) | strong, direct, taxon-specific | 10.1128/mbio.03387-23 |
| Mnh1 Na+/H+ antiport | supports | growth / halotolerance at pH 7.5 | *Staphylococcus aureus*; significant Na+/H+ exchange at pH 7.5; ΔmnhA1 reduced growth under elevated salt from pH 7.5–9 (vaish2018rolesofstaphylococcus pages 1-3, vaish2018rolesofstaphylococcus pages 3-6) | strong, direct, taxon-specific | 10.1128/JB.00611-17 |
| Mnh2 Na+/H+ and K+/H+ antiport | supports | alkaline and salt tolerance | *S. aureus*; significant Na+/H+ and K+/H+ exchange especially at pH 8.5–9.0; ΔmnhA2 affected growth mainly at pH 8.5–9.5 (vaish2018rolesofstaphylococcus pages 1-3, vaish2018rolesofstaphylococcus pages 6-8) | strong, direct, taxon-specific | 10.1128/JB.00611-17 |
| Respiratory proton pumps | contribute to | cytoplasmic/extracellular pH homeostasis | general methanotroph/microbial review context, not trait-specific; primary proton pumps remove protons from cytoplasm (yao2023howmethanotrophsrespond pages 5-7) | uncertain, review-supported, broad inference | 10.3389/fmicb.2022.1034164 |
| Potassium uptake transporters | contribute to | pH homeostasis via internal positive membrane potential | general methanotroph/microbial review context, not trait-specific (yao2023howmethanotrophsrespond pages 5-7) | uncertain, review-supported, broad inference | 10.3389/fmicb.2022.1034164 |


*Table: This table compiles compact, curation-ready candidate causal edges for METPO:1000456, separating strong taxon-specific experimental evidence from broader review-based mechanisms that should be marked uncertain.*

### Supporting snippets and curation notes

1. **Acetate metabolism → extracellular acidification.** The 2024 study reports that the `ΔackAΔacsA` mutant had an acidification rate “approximately 48% less” than wild type. This is a strong causal perturbation, although residual acidification shows that acetate is not the sole source (tran2024activephregulation pages 2-5).

2. **AlsS/AlsD acetoin biosynthesis → proton consumption → alkalinization.** The authors state that AlsS and AlsD each catalyze a step “consuming a proton”; both deletion mutants retained acidification but “completely lost the alkalinization phase.” Complementation restored it, while adding acetoin itself did not, supporting the biosynthetic reactions rather than the product as the proximal cause (tran2024activephregulation pages 5-7).

3. **Acetoin biosynthesis → return to the neutrophile range.** Starting from pH 6, alkalinization proceeded at 0.03 pH units per hour for 36.6 ± 0.4 h, versus 31.2 ± 0.5 h under neutral starting conditions. `ΔalsS` biofilms failed to maintain the preferred range, and AlsS overexpression shortened return time (tran2024activephregulation pages 5-7).

4. **Neutral extracellular pH regulation → biofilm development.** In minimally buffered medium, `ΔalsS` biofilms had altered morphology and significantly fewer cells (P < 0.001); 16 of 18 known matrix-associated genes were downregulated. The defect was not observed equivalently under fully buffered conditions, supporting an environment-dependent causal chain (tran2024activephregulation pages 5-7, tran2024activephregulation pages 7-9).

5. **Mnh1 Na+/H+ antiport → growth under salt at near-neutral-to-alkaline pH.** Mnh1 showed a pH optimum of 7.5 for Na+/H+ exchange; `mnhA1` deletion reduced growth under elevated salt from pH 7.5–9. This is direct evidence for homeostasis and tolerance, but it should not be encoded as causing the species’ pH-optimum class without a full growth-optimum assay (vaish2018rolesofstaphylococcus pages 39-42, vaish2018rolesofstaphylococcus pages 1-3).

6. **Mnh2 Na+/H+ and K+/H+ antiport → alkaline/salt tolerance.** Mnh2 was most active around pH 9.0, with reported Na+/H+ and K+/H+ activities of 36 ± 1% and 39 ± 1% fluorescence dequenching, respectively. `mnhA2` loss affected growth mainly at pH 8.5–9.5; this is primarily a neighboring alkali-tolerance mechanism (vaish2018rolesofstaphylococcus pages 39-42, vaish2018rolesofstaphylococcus pages 1-3).

## 5. Quantitative findings and recent developments

The principal 2024 advance is evidence that extracellular pH homeostasis can be an **emergent biofilm behavior** rather than only a cell-autonomous transporter response. In minimally buffered MSgg, *B. subtilis* biofilms underwent 15.0 ± 0.3 h of acidification to approximately pH 5.5 at 0.06 ± 0.0008 pH units/h, followed by 31.2 ± 0.5 h of alkalinization to pH 6.9 at 0.03 ± 0.0005 pH units/h (n = 42). A planktonic `ΔsinI` strain did not return to neutral (P < 0.000001) (tran2024activephregulation pages 2-5).

This study also demonstrates a major assay issue: reducing MOPS from 100 mM to 1 mM exposed pH dynamics that were hidden in standard medium. Thus, measured optimum and inferred mechanism can depend strongly on buffer strength, culture architecture, diffusion, and metabolic phase (tran2024activephregulation pages 2-5).

The methanotroph literature illustrates phenotype diversity: most neutrophilic methanotrophs are reported across approximately pH 6–8, while individual mildly acidophilic taxa have optima near 5.0–6.5 and alkaliphilic taxa near 8.5–10. These data support treating pH optimum as a continuous reaction norm discretized into ontology bins, rather than a sharp universal physiological boundary (yao2023howmethanotrophsrespond pages 4-5).

## 6. Applications and real-world implications

- **Biofilm control:** AlsS/AlsD-dependent pH regulation is a potential intervention point for unwanted *B. subtilis*-like biofilms in poorly buffered environments. The evidence is proof-of-mechanism, not yet a validated industrial antimicrobial strategy (tran2024activephregulation pages 1-2, tran2024activephregulation pages 7-9).
- **Bioprocess design:** Buffer concentration can conceal metabolic acidification and produce misleadingly stable cultures. Monitoring extracellular pH dynamically is relevant to fermentation, wastewater biofilms, and engineered microbial consortia (tran2024activephregulation pages 2-5).
- **Trait prediction:** Genomic detection of antiporters, ATP synthase, or respiratory complexes can support mechanistic hypotheses but is insufficient to assign `METPO:1000456`; these systems occur in neutrophiles, acidophiles, and alkaliphiles (yao2023howmethanotrophsrespond pages 5-7).
- **Environmental modeling:** Because pH affects methane oxidizer distribution and activity, experimentally grounded pH optima are useful in methane-cycle models. Broad pH-homeostasis genes alone cannot resolve the optimum class (yao2023howmethanotrophsrespond pages 4-5).
- **Pathogenesis and food microbiology:** Mnh antiporters contribute to *S. aureus* stress fitness, and `mnhA1` deletion markedly reduced virulence in a mouse model. This supports transporter relevance in real environments but remains indirect for the target optimum trait (vaish2018rolesofstaphylococcus pages 1-3, vaish2018rolesofstaphylococcus pages 3-6).

## 7. Expert assessment for TraitMech

A robust graph should distinguish three layers:

1. **Set point:** external pH approximately 6–7 (`METPO:1000456`).
2. **Proximal physiological state:** cytoplasmic pH homeostasis, sustainable proton motive force, and compatible enzyme activity.
3. **Taxon/context-specific effectors:** antiporters, respiratory proton pumps, potassium uptake, membrane composition, and acid-producing or proton-consuming metabolism.

The most defensible extension of the existing 10-node/9-edge graph is the *B. subtilis* branch:

`acetate biosynthesis → extracellular acidification → increased pH-homeostasis load`  
`alsS/alsD-dependent acetoin biosynthesis → proton consumption → extracellular alkalinization → pH ≈6.9 → supported biofilm growth/matrix development`

This branch has direct genetic perturbation, complementation, metabolite measurements, dynamic pH measurements, and quantitative developmental phenotypes. It should nevertheless carry `taxon: Bacillus subtilis NCIB 3610`, `lifestyle: biofilm`, and `assay: minimally buffered MSgg, 30°C` qualifiers (tran2024activephregulation pages 5-7, tran2024activephregulation pages 2-5).

## 8. Claims not yet ready for unqualified curation

- Do not curate **“Mnh1/Mnh2 causes pH optimum 6–7.”** The experiments establish salt/alkali tolerance and transporter activity, not the organismal optimum.
- Do not treat **“alkali tolerant” as equivalent to neutrophile** without an optimum-growth curve.
- Do not generalize the *B. subtilis* acetoin mechanism to all neutrophiles; it is biofilm- and taxon-specific.
- Do not assert that acetoin itself alkalinizes the environment. The 2024 experiment supports proton consumption during biosynthesis, and exogenous acetoin up to 50 mM did not reproduce the effect (tran2024activephregulation pages 5-7).
- Do not assign causality from the presence of ATP synthase, respiratory-chain, potassium-transport, or antiporter genes alone.
- Do not curate individual ETC complexes as necessary for the *B. subtilis* pH dynamic: deletion of each of five tested proton-pumping complexes did not significantly alter it, suggesting redundancy or a different dominant source (tran2024activephregulation pages 2-5).
- Do not merge intracellular pH, extracellular pH, medium starting pH, and terminal pH into one node.
- Do not infer an organismal trait from purified-enzyme pH optima.
- Verify all ontology identifiers against current releases before YAML insertion; label-only nodes are preferable to uncertain CURIEs.

## 9. DOI-first bibliography

1. **Tran P, Lander SM, Prindle A.** “Active pH regulation facilitates *Bacillus subtilis* biofilm development in a minimally buffered environment.” *mBio* 15(3), published 13 February 2024; March 2024 issue. DOI: [10.1128/mbio.03387-23](https://doi.org/10.1128/mbio.03387-23). Direct genetic, metabolomic, pH-dynamic, and developmental evidence (tran2024activephregulation pages 1-2, tran2024activephregulation pages 5-7, tran2024activephregulation pages 2-5).

2. **Yao X, Wang J, Hu B.** “How methanotrophs respond to pH: A review of ecophysiology.” *Frontiers in Microbiology* 13, published January 2023. DOI: [10.3389/fmicb.2022.1034164](https://doi.org/10.3389/fmicb.2022.1034164). Comparative pH-optimum ranges and general homeostasis mechanisms (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond pages 4-5).

3. **Vaish M, et al.** “Roles of *Staphylococcus aureus* Mnh1 and Mnh2 antiporters in salt tolerance, alkali tolerance, and pathogenesis.” *Journal of Bacteriology* 200(5), March 2018; accepted manuscript posted 20 December 2017. DOI: [10.1128/JB.00611-17](https://doi.org/10.1128/JB.00611-17). Direct vesicle transport assays and knockout growth phenotypes (vaish2018rolesofstaphylococcus pages 1-3, vaish2018rolesofstaphylococcus pages 39-42).

4. **Krulwich TA, Sachs G, Padan E.** “Molecular aspects of bacterial pH sensing and homeostasis.” *Nature Reviews Microbiology* 9, 330–343, 2011. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). Foundational source supplied with the trait; supports the general near-neutral cytoplasmic set-point/homeostasis framework, but should not alone be used to assert each taxon-specific edge.

References

1. (tran2024activephregulation pages 2-5): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.

2. (yao2023howmethanotrophsrespond pages 4-5): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 79 citations and is from a peer-reviewed journal.

3. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 79 citations and is from a peer-reviewed journal.

4. (tran2024activephregulation pages 5-7): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.

5. (tran2024activephregulation pages 1-2): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.

6. (vaish2018rolesofstaphylococcus pages 6-8): Manisha Vaish, Alexa Price-Whelan, Tamara Reyes-Robles, Jun Liu, Amyeo Jereen, Stephanie Christie, Francis Alonzo, Meredith A. Benson, Victor J. Torres, and Terry A. Krulwich. Roles of staphylococcus aureus mnh1 and mnh2 antiporters in salt tolerance, alkali tolerance, and pathogenesis. Journal of Bacteriology, Mar 2018. URL: https://doi.org/10.1128/jb.00611-17, doi:10.1128/jb.00611-17. This article has 58 citations and is from a peer-reviewed journal.

7. (vaish2018rolesofstaphylococcus pages 39-42): Manisha Vaish, Alexa Price-Whelan, Tamara Reyes-Robles, Jun Liu, Amyeo Jereen, Stephanie Christie, Francis Alonzo, Meredith A. Benson, Victor J. Torres, and Terry A. Krulwich. Roles of staphylococcus aureus mnh1 and mnh2 antiporters in salt tolerance, alkali tolerance, and pathogenesis. Journal of Bacteriology, Mar 2018. URL: https://doi.org/10.1128/jb.00611-17, doi:10.1128/jb.00611-17. This article has 58 citations and is from a peer-reviewed journal.

8. (vaish2018rolesofstaphylococcus pages 1-3): Manisha Vaish, Alexa Price-Whelan, Tamara Reyes-Robles, Jun Liu, Amyeo Jereen, Stephanie Christie, Francis Alonzo, Meredith A. Benson, Victor J. Torres, and Terry A. Krulwich. Roles of staphylococcus aureus mnh1 and mnh2 antiporters in salt tolerance, alkali tolerance, and pathogenesis. Journal of Bacteriology, Mar 2018. URL: https://doi.org/10.1128/jb.00611-17, doi:10.1128/jb.00611-17. This article has 58 citations and is from a peer-reviewed journal.

9. (tran2024activephregulation pages 7-9): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.

10. (vaish2018rolesofstaphylococcus pages 3-6): Manisha Vaish, Alexa Price-Whelan, Tamara Reyes-Robles, Jun Liu, Amyeo Jereen, Stephanie Christie, Francis Alonzo, Meredith A. Benson, Victor J. Torres, and Terry A. Krulwich. Roles of staphylococcus aureus mnh1 and mnh2 antiporters in salt tolerance, alkali tolerance, and pathogenesis. Journal of Bacteriology, Mar 2018. URL: https://doi.org/10.1128/jb.00611-17, doi:10.1128/jb.00611-17. This article has 58 citations and is from a peer-reviewed journal.