---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:56:43.779116'
end_time: '2026-06-18T07:05:36.382330'
duration_seconds: 532.6
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell width
  trait_identifier: METPO:1000882
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_width
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that inheres in a cell by virtue of its shorter dimension
    when viewed on a plane.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan
    synthesis (Bacterial rod-shape review identifies MreB-directed lateral wall synthesis
    as the control point governing cell width.) | DOI:10.1038/nrmicro3088: rod-shape
    is maintained (Cell-wall biosynthesis review supports lateral peptidoglycan assembly
    as the cellular machinery setting rod width.)'
  causal_graph_summary: 'cell_width_mreb_lateral_wall: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width
- **METPO identifier:** METPO:1000882
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that inheres in a cell by virtue of its shorter dimension when viewed on a plane.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Bacterial rod-shape review identifies MreB-directed lateral wall synthesis as the control point governing cell width.) | DOI:10.1038/nrmicro3088: rod-shape is maintained (Cell-wall biosynthesis review supports lateral peptidoglycan assembly as the cellular machinery setting rod width.)
- **Existing causal graph summary:** cell_width_mreb_lateral_wall: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **cell width** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width.yaml`.

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
- **Trait label:** cell width
- **METPO identifier:** METPO:1000882
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that inheres in a cell by virtue of its shorter dimension when viewed on a plane.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Bacterial rod-shape review identifies MreB-directed lateral wall synthesis as the control point governing cell width.) | DOI:10.1038/nrmicro3088: rod-shape is maintained (Cell-wall biosynthesis review supports lateral peptidoglycan assembly as the cellular machinery setting rod width.)
- **Existing causal graph summary:** cell_width_mreb_lateral_wall: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **cell width** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width.yaml`.

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


## Microbial Trait Causal Graph Report: Cell width (METPO:1000882)

### Executive scope summary
**Cell width** (METPO:1000882) is the **short-axis dimension** of a microbial cell when viewed in a plane, typically operationalized as the diameter of the cylindrical portion of a rod-shaped bacterium measured from microscopy segmentation. Mechanistically, it is largely a consequence of **lateral (sidewall) peptidoglycan (PG) insertion topology**, **cell-wall remodeling**, and **envelope mechanics** (turgor, wall stiffness/rheology). In rod-shaped bacteria, the elongasome/Rod system inserts PG circumferentially (perpendicular to the long axis), which directly affects the cell’s diameter/width. In coccoid/ovoid bacteria, “width” can be less separable from overall diameter/sphericity, so axis definitions and cell-cycle phase (pre/post septation) matter for curation. (middlemiss2024molecularmotortugofwar pages 1-2, willdigg2023adecreasein pages 1-3, costa2024theroleof pages 1-2)

Boundary cases to distinguish during curation:
- **Cell width vs cell length:** width refers to the short axis; length changes can occur independently (e.g., filamentation or elongation defects). (wilson2023anexhaustivemultiple pages 8-10)
- **Division vs elongation states:** septal constriction (divisome activity) changes local diameter and can confound “width” if measured near midcell. (kale2024mechanicsofe. pages 1-4, shlosman2023allostericactivationof pages 1-2)
- **Bulging under antibiotics:** bulges represent pathological, mechanics-driven width excursions rather than steady-state width homeostasis. (kale2024mechanicsofe. pages 1-4)
- **Cocci/ovococci:** “width” may track sphericity or axis ratio rather than a stable cylindrical diameter; in *S. aureus*, elongation is modest and occurs without MreB. (costa2024theroleof pages 1-2)

---

## 1) Key concepts & definitions (current understanding)

### 1.1 Core structural determinant: peptidoglycan architecture and insertion topology
Peptidoglycan is the primary load-bearing polymer that “determines cell shape,” so width is best treated as a cell-wall emergent property constrained by synthesis and remodeling. (shlosman2023allostericactivationof pages 1-2)

### 1.2 Two major PG-synthesis “systems” and their relationship to width
Many bacteria use:
- **SEDS–class B PBP synthases** operating in organized complexes:
  - **Rod complex/elongasome** for elongation (sidewall insertion)
  - **Divisome** for septation (midcell insertion)
- **Class A PBPs (aPBPs)** often described as fortification/repair and/or contributing to envelope robustness; their balance with elongasome influences normal dimensions. (shlosman2023allostericactivationof pages 1-2, willdigg2023adecreasein pages 1-3)

Shlosman et al. summarize Rod complex composition: “the Rod complex has a PG synthase RodA-PBP2 and accessory components MreCD and RodZ.” (shlosman2023allostericactivationof pages 1-2)

---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 2024: Single-molecule evidence linking elongasome dynamics to width regulation (*Bacillus subtilis*)
Middlemiss et al. (Nature Communications, 2024-06-xx) provide a high-resolution mechanistic picture: the elongasome moves processively around the circumference and **RodA levels regulate processivity, pausing, and reversal**, with a proposed “tug-of-war” between opposing synthase complexes on MreB filaments. They explicitly connect the RodA/bPBP machinery and MreB to circumferential insertion that reinforces the sidewall (a width-setting mechanism). (middlemiss2024molecularmotortugofwar pages 1-2, middlemiss2024molecularmotortugofwar pages 8-9)

Key conceptual advance: width may be tuned by **processivity and effective glycan strand length/density**, not only by mean enzymatic activity—potentially yielding non-linear relationships (wider at low and high synthase densities, narrower at intermediate densities) in their speculative model. (middlemiss2024molecularmotortugofwar pages 8-9)

### 2.2 2023: Allosteric activation mechanism for the essential elongation synthase RodA–PBP2
Shlosman et al. (Nature Communications, 2023-06-xx) show that RodA–PBP2 undergoes conformational exchange and that opening “couples the activation of polymerization and crosslinking and is essential in vivo.” This is a mechanistic basis for how elongation PG synthesis is initiated/coupled—upstream of width effects mediated by lateral wall synthesis. (shlosman2023allostericactivationof pages 1-2)

### 2.3 2023: Environmental switching between alternative elongasomes in *Salmonella* (pH-dependent width/shape maintenance)
Castanheira & García-del Portillo (Communications Biology, 2023-09-xx) provide evidence that *Salmonella* can deploy **two elongasomes directed by different PBP2-like synthases**: canonical PBP2 (neutral pH) vs pathogen-specific PBP2SAL (acidic conditions). They report ΔmrdA (PBP2 loss) produces “giant spherical cells” at neutral pH but can regain a “genuine rod shape” under acidic minimal conditions where PBP2SAL is functional. This is a clear environmental modulation edge relevant to width/shape preservation. (castanheira2023evidenceoftwo pages 1-2)

### 2.4 2023: Coordinating membrane synthesis with PG synthesis capacity (implications for morphology)
Willdigg et al. (mBio, published 2023-04-05) frame width/shape as dependent on balanced envelope synthesis: “Elongation… results from the balanced action of the elongasome and aPBPs” and “both aPBPs and the elongasome are necessary to maintain normal cell length and width.” They also describe regulatory compensation that increases elongasome function and results in “thinner and elongated cells.” (willdigg2023adecreasein pages 1-3)

### 2.5 2023: Quantitative genetics of hydrolases controlling width homeostasis (*B. subtilis*)
Wilson et al. (mBio, 2023-10-xx) perform an exhaustive hydrolase knockout strategy and quantify direct width changes:
- ΔcwlO cells are “13% wider” than WT (and shorter). (wilson2023anexhaustivemultiple pages 8-10)
- A Δ40 strain (lacking 40 hydrolases) is “3% wider.” (wilson2023anexhaustivemultiple pages 8-10)
- Δ40 ΔcwlO cells show impaired width control with “a 1.5× wider cell width distribution” (increased variance). (wilson2023anexhaustivemultiple pages 8-10)

This supports including cell-wall **hydrolase activity** as a width-control module (mean and variance).

### 2.6 2024: Cell morphogenesis in *S. aureus* without MreB; elongation uses RodA/PBP3 and is regulated by GpsB
Costa et al. (mBio, published 2024-02-06) show that *S. aureus* (lacking MreB) still undergoes slight elongation dependent on RodA/PBP3 and identify regulators (GpsB, SsaA, RodZ). They propose GpsB modulates morphology via spatial regulation of PBP2/PBP4 localization, where peripheral insertion/crosslinking can override RodA/PBP3-driven elongation and increase sphericity. This informs boundary-case curation where “width” is tied to axis ratio/sphericity rather than a cylinder diameter. (costa2024theroleof pages 1-2)

### 2.7 2024 (preprint): Mechanics-based width homeostasis under cytoskeletal and septation inhibition (*E. coli*)
Kale et al. (bioRxiv, 2024-11-22) quantify width dynamics and mechanical parameters under A22 (MreB inhibitor) and cephalexin (PBP3 inhibitor). They estimate turgor and growth pressures ≈0.15 MPa and ≈0.4 MPa and argue bulging/width changes correlate strongly with envelope bending rigidity. While preprint and bulge-focused, it motivates inclusion of **bending rigidity** and **turgor pressure** nodes in a causal graph. (kale2024mechanicsofe. pages 1-4)

### 2.8 2024 (preprint): Turgor pressure as a pacemaker coordinating wall expansion with biomass synthesis
Basan et al. (Research Square, 2024-04-xx) propose that “turgor pressure generated by increased ribosome concentrations sets the pace of volume growth,” and that plasmolysis/vanishing turgor can stop envelope expansion. This is a broader coordination mechanism connecting growth state to envelope expansion (and thereby dimensions including width), but should be curated cautiously as preprint and not width-specific. (basan2024homeostasisofcytoplasmic pages 10-12)

---

## 3) Current applications and real-world implementations

### 3.1 Antibacterial therapy and antibiotic mechanism-of-action phenotyping
Width/shape defects are central readouts for cell-wall-targeting antibiotics because PG synthesis is a “key antibiotic target,” and uncoupling polymerization and crosslinking is linked to β-lactam lethality. (shlosman2023allostericactivationof pages 1-2)

Perturbations used as practical levers:
- **A22** to depolymerize/inhibit MreB → loss of width control (research tool; not clinical). (kale2024mechanicsofe. pages 1-4)
- **Cephalexin** (β-lactam) inhibiting **PBP3/FtsI** → bulging/shape failure in division-inhibited contexts. (kale2024mechanicsofe. pages 1-4)

### 3.2 Industrial and synthetic biology: morphology engineering
Mechanistic knobs (RodA/PBPs, hydrolases, membrane synthesis balance) are increasingly used to engineer morphology for growth robustness and processing (e.g., changes that influence downstream lysis/extraction), though the strongest direct evidence in this tool run is oriented toward core morphogenesis rather than a specific industrial case study. (willdigg2023adecreasein pages 1-3, costa2024theroleof pages 1-2)

---

## 4) Expert opinions and analysis from authoritative sources (2023–2024)

### 4.1 Authoritative synthesis: Rod complex as a conserved organized width-setting module
Shlosman et al. emphasize the organizational logic: SEDS-bPBP synthases act in “multi-protein complexes” for directed synthesis, with RodA-PBP2 as the elongation synthase and MreCD/RodZ as accessory components. This supports a causal-graph backbone where Rod activity drives sidewall PG insertion, which determines width. (shlosman2023allostericactivationof pages 1-2)

### 4.2 Balancing synthesis systems as a width homeostasis principle
Willdigg et al. explicitly state that “both aPBPs and the elongasome are necessary to maintain normal cell length and width,” and that increasing elongasome activity yields “thinner” cells—an expert-curation-friendly directional claim tying machine balance to width. (willdigg2023adecreasein pages 1-3)

### 4.3 Processivity/processive dynamics as a new “control parameter”
Middlemiss et al. articulate a mechanistic view where cell shape is controlled not only by where synthesis occurs but by the **dynamics** of elongasome complexes (processivity, pauses, reversals) regulated by RodA levels and motor tug-of-war. This suggests candidate TraitMech nodes around “elongasome processivity” and “MreB-associated motor competition.” (middlemiss2024molecularmotortugofwar pages 1-2, middlemiss2024molecularmotortugofwar pages 8-9)

---

## 5) Relevant statistics and recent data points (from included sources)

- **Hydrolase mutants in *B. subtilis*** (Wilson et al., mBio 2023):
  - ΔcwlO: **13% wider** than WT. (wilson2023anexhaustivemultiple pages 8-10)
  - Δ40 hydrolase deletion strain: **3% wider** than WT. (wilson2023anexhaustivemultiple pages 8-10)
  - Δ40 ΔcwlO: **1.5× wider width distribution** (higher width variability; CV increase). (wilson2023anexhaustivemultiple pages 8-10)

- **Mechanical model estimates in *E. coli*** (Kale et al., bioRxiv 2024):
  - Estimated turgor pressure ≈ **0.15 MPa** and growth pressure ≈ **0.4 MPa** (model-based). (kale2024mechanicsofe. pages 1-4)

---

## TraitMech curation content

### A) Candidate nodes (grouped by type) with suggested grounding

#### Trait node
- **cell width** — METPO:1000882 (given)

#### Cellular processes / pathways (GO candidates)
- **peptidoglycan biosynthetic process** (GO; label-only here—exact GO ID not retrieved in this run)
- **cell wall organization / biogenesis** (GO; label-only)
- **cell elongation** (GO; label-only)
- **cell division / septation** (GO; label-only)

#### Protein complexes and modules
- **Rod complex / elongasome** (module)
  - Core: **RodA (SEDS glycosyltransferase)** + **PBP2 (class B PBP transpeptidase)** (shlosman2023allostericactivationof pages 1-2)
  - Accessories: **MreC, MreD, RodZ** (shlosman2023allostericactivationof pages 1-2)
  - Cytoskeleton/scaffold: **MreB** (and in *B. subtilis*: **Mbl, MreBH**) (middlemiss2024molecularmotortugofwar pages 1-2)
- **Divisome** (module)
  - Core: **FtsW–FtsI/PBP3**, organized by **FtsZ** (shlosman2023allostericactivationof pages 1-2, kale2024mechanicsofe. pages 1-4)

#### Enzymes: cell-wall remodeling
- **CwlO** (D,L-endopeptidase complex component; functionally essential hydrolase context) (wilson2023anexhaustivemultiple pages 8-10)
- **LytE** (hydrolase; essential/redundant with CwlO in growth contexts; implicated in elongasome-associated remodeling) (wilson2023anexhaustivemultiple pages 8-10, willdigg2023adecreasein pages 1-3)
- **MltG** (lytic transglycosylase; membrane-proximal PG metabolism; not width-specific in the quoted snippet but mechanistically relevant to PG strand processing) (wilson2023anexhaustivemultiple pages 8-10)

#### Regulatory pathways / factors
- **σI-dependent pathway** (incl. ecsA, rasP, sigI) regulating **mreBH and lytE** (willdigg2023adecreasein pages 1-3)
- **FapR** (fatty acid synthesis transcriptional regulator; FapR* super-repressor) (willdigg2023adecreasein pages 1-3)
- **GpsB** (spatiotemporal regulator affecting PBP localization in *S. aureus*) (costa2024theroleof pages 1-2)

#### Environmental / experimental factors (ENVO candidates; label-only)
- **pH (acidic vs neutral)** (activates alternative elongasomes in *Salmonella*) (castanheira2023evidenceoftwo pages 1-2)
- **nutrient richness / growth condition** (e.g., LB vs minimal PCN) (castanheira2023evidenceoftwo pages 1-2)
- **osmotic/turgor state; plasmolysis** (basan2024homeostasisofcytoplasmic pages 10-12)

#### Physical/biophysical nodes
- **turgor pressure** (basan2024homeostasisofcytoplasmic pages 10-12, kale2024mechanicsofe. pages 1-4)
- **cell envelope bending rigidity** (kale2024mechanicsofe. pages 1-4)
- **cell wall viscoelastic rheology (Maxwell-like)** (basan2024homeostasisofcytoplasmic pages 10-12)

#### Chemicals/inhibitors (CHEBI candidates; label-only)
- **A22** (MreB polymerization inhibitor) (kale2024mechanicsofe. pages 1-4)
- **cephalexin** (β-lactam; PBP3 inhibitor) (kale2024mechanicsofe. pages 1-4)
- **cerulenin** (fatty acid synthesis inhibitor) (willdigg2023adecreasein pages 1-3)
- **β-lactams** (class) (shlosman2023allostericactivationof pages 1-2, willdigg2023adecreasein pages 1-3)

---

### B) Candidate causal edges (curation table)

| Subject node | Predicate (causal) | Object node | Taxon/context | Evidence snippet | Reference | Publication date | Notes/uncertainty |
|---|---|---|---|---|---|---|---|
| MreB-guided lateral peptidoglycan synthesis | helps determine | cell width (METPO:1000882) | Rod-shaped bacteria; foundational mechanism | “MreB-directed peptidoglycan synthesis” is identified as “the control point governing cell width” in rod-shape review context; recent review also states Rod and aPBP systems “act oppositely to set *B. subtilis* cell diameter” (galinier2023recentadvancesin pages 15-16) | Galinier A, et al. *Biomolecules* (review), DOI:10.3390/biom13050720, https://doi.org/10.3390/biom13050720 | 2023-04 | Broad, high-confidence mechanism; review-supported rather than a single direct experiment in this source. |
| RodA–PBP2 (Rod complex core synthase) activation/open state | activates/couples | peptidoglycan polymerization and crosslinking required for elongation-based width control | Conserved Rod complex; bacterial elongation | “an essential PG synthase (RodA-PBP2) responsible for bacterial elongation undergoes dynamic exchange between closed and open states. Structural opening couples the activation of polymerization and crosslinking and is essential in vivo.” (shlosman2023allostericactivationof pages 1-2) | Shlosman I, et al. *Nature Communications*, DOI:10.1038/s41467-023-39037-9, https://doi.org/10.1038/s41467-023-39037-9 | 2023-06 | Strong for Rod-complex activation; width effect is mechanistically inferred through elongation/lateral wall synthesis rather than directly measured in this paper. |
| Rod complex accessory proteins MreC/MreD/RodZ | regulate | RodA–PBP2 activity and thus lateral wall synthesis affecting width | Conserved Rod complex | “the Rod complex has a PG synthase RodA-PBP2 and accessory components MreCD and RodZ” and genetic studies “implicated… MreC, as potential regulators of enzymatic activity” (shlosman2023allostericactivationof pages 1-2) | Shlosman I, et al. *Nature Communications*, DOI:10.1038/s41467-023-39037-9, https://doi.org/10.1038/s41467-023-39037-9 | 2023-06 | Good mechanistic support for upstream regulation; direct width phenotype not quantified here. |
| RodA abundance | regulates | elongasome processivity, pausing, reversal, and thereby cell width | *Bacillus subtilis* | “cellular levels of RodA regulate elongasome processivity, reversal and pausing” and tug-of-war “likely also regulates the cell shape via modulation of elongasome processivity” (middlemiss2024molecularmotortugofwar pages 1-2, middlemiss2024molecularmotortugofwar pages 8-9) | Middlemiss S, et al. *Nature Communications*, DOI:10.1038/s41467-024-49785-x, https://doi.org/10.1038/s41467-024-49785-x | 2024-06 | Strong recent mechanistic study. Width is linked by model and single-molecule dynamics. |
| Low elongasome synthase concentration (e.g., RodA limitation) | increases | cell width | *Bacillus subtilis* model | “At low concentrations of active elongasome synthases… resulting in a weaker, wider cell wall.” (middlemiss2024molecularmotortugofwar pages 8-9) | Middlemiss S, et al. *Nature Communications*, DOI:10.1038/s41467-024-49785-x, https://doi.org/10.1038/s41467-024-49785-x | 2024-06 | Model-based statement in figure legend; useful but should be curated with uncertainty flag. |
| High elongasome synthase concentration / frequent tug-of-war | increases | cell width | *Bacillus subtilis* model | “At high concentrations of active elongasome synthases… frequent tug-of-war… resulting in a weaker, wider cell wall.” (middlemiss2024molecularmotortugofwar pages 8-9) | Middlemiss S, et al. *Nature Communications*, DOI:10.1038/s41467-024-49785-x, https://doi.org/10.1038/s41467-024-49785-x | 2024-06 | Also model-based and potentially non-monotonic; curate as speculative/uncertain. |
| Intermediate elongasome synthase concentration | decreases/optimizes | cell width | *Bacillus subtilis* model | “At intermediate concentrations… resulting in a narrow, optimally strong cell wall.” (middlemiss2024molecularmotortugofwar pages 8-9) | Middlemiss S, et al. *Nature Communications*, DOI:10.1038/s41467-024-49785-x, https://doi.org/10.1038/s41467-024-49785-x | 2024-06 | Supports non-linear relationship between elongasome activity and width; speculative model. |
| Canonical PBP2 elongasome | maintains | rod width/rod shape at neutral pH | *Salmonella enterica* serovar Typhimurium | “The PBP2-elongasome responds to neutral pH” and ΔmrdA cells “appear at neutral pH as giant spherical cells with larger size” (castanheira2023evidenceoftwo pages 1-2) | Castanheira S, García-del Portillo F. *Communications Biology*, DOI:10.1038/s42003-023-05308-w, https://doi.org/10.1038/s42003-023-05308-w | 2023-09 | Strong taxon-specific evidence that loss of canonical elongasome widens/rounds cells in neutral pH. |
| Acidic pH | activates/selects | PBP2SAL elongasome that preserves rod morphology | *Salmonella enterica* serovar Typhimurium | “The PBP2SAL-elongasome assembles in acidic conditions” and in minimal PCN pH 4.6 ΔmrdA cells “exhibiting a genuine rod shape” (castanheira2023evidenceoftwo pages 1-2) | Castanheira S, García-del Portillo F. *Communications Biology*, DOI:10.1038/s42003-023-05308-w, https://doi.org/10.1038/s42003-023-05308-w | 2023-09 | Strong environmental edge; taxon-specific alternative elongasome. |
| Balanced action of elongasome and class A PBPs | maintains | normal cell length and width | *Bacillus subtilis* | “Elongation of the rod-shaped *B. subtilis* cell results from the balanced action of the elongasome and aPBPs” and “both aPBPs and the elongasome are necessary to maintain normal cell length and width” (willdigg2023adecreasein pages 1-3) | Willdigg JR, et al. *mBio*, DOI:10.1128/mbio.00475-23, https://doi.org/10.1128/mbio.00475-23 | 2023-04-05 | Strong curation-ready statement, though not a single-gene edge. |
| Upregulated elongasome activity | decreases | cell width | *Bacillus subtilis* PG-limited cells | “Increased elongasome activity leads to thinner and elongated cells” (willdigg2023adecreasein pages 1-3) | Willdigg JR, et al. *mBio*, DOI:10.1128/mbio.00475-23, https://doi.org/10.1128/mbio.00475-23 | 2023-04-05 | Strong directional edge; could map to σI / RodA / MreBH-LytE regulatory path. |
| σI-regulated mreBH and lytE upregulation | promotes | compensatory elongasome function affecting width | *Bacillus subtilis* | “ecsA, rasP, sigI pathway… increases expression of mreBH and lytE. Increased elongasome activity leads to thinner and elongated cells” (willdigg2023adecreasein pages 1-3) | Willdigg JR, et al. *mBio*, DOI:10.1128/mbio.00475-23, https://doi.org/10.1128/mbio.00475-23 | 2023-04-05 | Multi-step regulatory edge; direct width effect mediated through elongasome/hydrolases. |
| CwlO loss | increases | mean cell width | *Bacillus subtilis* hydrolase mutants | “∆cwlO cells were 13% wider and 18% shorter than WT cells” (wilson2023anexhaustivemultiple pages 8-10) | Wilson SA, et al. *mBio*, DOI:10.1128/mbio.01760-23, https://doi.org/10.1128/mbio.01760-23 | 2023-10 | Strong direct phenotype with quantitative statistic. |
| Δ40 hydrolase background | slightly increases | mean cell width | *Bacillus subtilis* | “∆40 cells had a WT cell length and were 3% wider” (wilson2023anexhaustivemultiple pages 8-10) | Wilson SA, et al. *mBio*, DOI:10.1128/mbio.01760-23, https://doi.org/10.1128/mbio.01760-23 | 2023-10 | Direct quantitative edge, but effect size is small. |
| CwlO loss in Δ40 background | increases variability of | cell width control | *Bacillus subtilis* | “∆40 ∆cwlO cells were less able to control their width… having a 1.5× wider cell width distribution” (wilson2023anexhaustivemultiple pages 8-10) | Wilson SA, et al. *mBio*, DOI:10.1128/mbio.01760-23, https://doi.org/10.1128/mbio.01760-23 | 2023-10 | Best curated as width homeostasis/variance rather than mean width alone. |
| RodA/PBP3 elongation system | promotes | elongation that increases long-axis/short-axis ratio rather than pure sphericity | *Staphylococcus aureus* | “S. aureus cells were recently shown to elongate… dependent on the… RodA/PBP3” and these proteins “result in slight cell elongation” (costa2024theroleof pages 1-2) | Costa SF, et al. *mBio*, DOI:10.1128/mbio.03235-23, https://doi.org/10.1128/mbio.03235-23 | 2024-02-06 | Important boundary-case evidence: in coccoid/ovoid cells, width trait is axis-dependent. |
| GpsB loss | increases sphericity / reduces elongation relative to width | cell morphology | *Staphylococcus aureus* | “Consequently, in the absence of GpsB, S. aureus cells become more spherical.” (costa2024theroleof pages 1-2) | Costa SF, et al. *mBio*, DOI:10.1128/mbio.03235-23, https://doi.org/10.1128/mbio.03235-23 | 2024-02-06 | Useful for nearby trait edges, but width-specific interpretation is less direct because morphology is ovococcoid. |
| GpsB | spatially regulates | PBP2/PBP4 localization, affecting peripheral PG insertion and morphology | *Staphylococcus aureus* | “The gpsB mutant showed the strongest phenotype, mediated by the partial delocalization… of PBP2 and PBP4… Increased levels of these PBPs at the cell periphery… impairing elongation.” (costa2024theroleof pages 1-2) | Costa SF, et al. *mBio*, DOI:10.1128/mbio.03235-23, https://doi.org/10.1128/mbio.03235-23 | 2024-02-06 | Mechanistic upstream edge to include with uncertainty for direct width effect. |
| Increased ribosome-driven turgor pressure | sets pace of | cell wall expansion that determines cell dimensions including width | *Escherichia coli* / general bacteria | “cell wall expansion is… coupled with biomass synthesis, as turgor pressure generated by increased ribosome concentrations sets the pace of volume growth” (basan2024homeostasisofcytoplasmic pages 10-12) | Basan M, et al. *Research Square*, DOI:10.21203/rs.3.rs-4138690/v1, https://doi.org/10.21203/rs.3.rs-4138690/v1 | 2024-04 | Preprint. Strong mechanistic proposal for envelope expansion; width-specific effect should be curated cautiously. |
| Plasmolysis / vanishing turgor | stops | cell envelope expansion | *Escherichia coli* / starvation context | “Plasmolysis is a state with vanishing turgor pressure and… vanishing turgor is required to stop the expansion of the cell envelope.” (basan2024homeostasisofcytoplasmic pages 10-12) | Basan M, et al. *Research Square*, DOI:10.21203/rs.3.rs-4138690/v1, https://doi.org/10.21203/rs.3.rs-4138690/v1 | 2024-04 | Mechanistic physical edge; indirect for width but relevant to width homeostasis under osmotic stress. |
| A22 (MreB polymerization inhibitor) | disrupts/increases loss of control of | cell width | *Escherichia coli* | “A22, an MreB polymerization inhibitor… resulting in loss of width control and cell shape change” (kale2024mechanicsofe. pages 1-4) | Kale T, et al. *bioRxiv*, DOI:10.1101/2024.11.22.624946, https://doi.org/10.1101/2024.11.22.624946 | 2024-11-22 | Preprint; strong perturbational evidence. |
| Cephalexin (PBP3/FtsI inhibitor) | induces | bulging and width increase when envelope rigidity drops | *Escherichia coli* | “cephalexin, a PBP3 inhibitor… low concentrations of both inhibitors result in bulge formation” and “width increases and saturates primarily under the control of envelope bending rigidity” (kale2024mechanicsofe. pages 1-4) | Kale T, et al. *bioRxiv*, DOI:10.1101/2024.11.22.624946, https://doi.org/10.1101/2024.11.22.624946 | 2024-11-22 | Preprint; bulging is partly a pathological width phenotype rather than steady-state width. |
| Cell envelope bending rigidity | constrains | cell width homeostasis | *Escherichia coli* mechanical model | “bulge expansion correlates most prominently with a change in bending rigidity” and “width increases and saturates primarily under the control of envelope bending rigidity” (kale2024mechanicsofe. pages 1-4) | Kale T, et al. *bioRxiv*, DOI:10.1101/2024.11.22.624946, https://doi.org/10.1101/2024.11.22.624946 | 2024-11-22 | Preprint; high value for including biophysical node in graph. |
| Turgor pressure (~0.15 MPa) and growth pressure (~0.4 MPa) | contribute to | bulging/width dynamics under perturbation | *Escherichia coli* mechanical model | “we estimate the turgor and growth pressures… as ≈0.15 MPa and ≈0.4 MPa” (kale2024mechanicsofe. pages 1-4) | Kale T, et al. *bioRxiv*, DOI:10.1101/2024.11.22.624946, https://doi.org/10.1101/2024.11.22.624946 | 2024-11-22 | Quantitative physical parameters; model-derived, not direct molecular edges. |


*Table: This table lists candidate causal edges for microbial cell width (METPO:1000882), linking genes, protein complexes, physical factors, and environmental conditions to width control. It is designed to support TraitMech curation by pairing each proposed edge with a short evidence snippet, DOI-first reference, date, and uncertainty notes.*

---

## Warnings / curation notes (what should not yet be curated as “high-confidence”)

1. **Model-based width claims in Middlemiss 2024 Fig. 5** (non-linear “wide at low/high synthase concentration”) are explicitly described as “speculative model” in the figure legend; these should be curated as **UNCERTAIN** until corroborated by direct width measurements across synthase concentration titrations. (middlemiss2024molecularmotortugofwar pages 8-9)

2. **Preprints** (Kale 2024; Basan 2024) provide valuable mechanistic/quantitative hypotheses but should be curated with **UNCERTAIN/PREPRINT** flags, especially where width-specific effects are inferred from general envelope expansion models. (kale2024mechanicsofe. pages 1-4, basan2024homeostasisofcytoplasmic pages 10-12)

3. **Coccus/ovoid organisms** (e.g., *S. aureus*) require careful trait mapping: edges often describe “more spherical” or “elongation” rather than a direct change in “cell width” as defined for rods; include with **ASSAY/GEOMETRY-DEPENDENT** caution. (costa2024theroleof pages 1-2)

4. **Bulging phenotypes under antibiotics** are not equivalent to steady-state width setpoints. Curate bulging-related edges as **stress/perturbation mode** rather than baseline width control. (kale2024mechanicsofe. pages 1-4)

---

## DOI-first bibliography (with URLs and publication dates where available)

1. Middlemiss S, et al. “Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in *Bacillus subtilis*.” *Nature Communications* (2024-06). DOI: 10.1038/s41467-024-49785-x. URL: https://doi.org/10.1038/s41467-024-49785-x (middlemiss2024molecularmotortugofwar pages 1-2)

2. Costa SF, et al. “The role of GpsB in *Staphylococcus aureus* cell morphogenesis.” *mBio* (Published 2024-02-06). DOI: 10.1128/mbio.03235-23. URL: https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2)

3. Shlosman I, et al. “Allosteric activation of cell wall synthesis during bacterial growth.” *Nature Communications* (2023-06). DOI: 10.1038/s41467-023-39037-9. URL: https://doi.org/10.1038/s41467-023-39037-9 (shlosman2023allostericactivationof pages 1-2)

4. Willdigg JR, Patel Y, Helmann JD. “A Decrease in Fatty Acid Synthesis Rescues Cells with Limited Peptidoglycan Synthesis Capacity.” *mBio* (Published 2023-04-05). DOI: 10.1128/mbio.00475-23. URL: https://doi.org/10.1128/mbio.00475-23 (willdigg2023adecreasein pages 1-3)

5. Wilson SA, et al. “An exhaustive multiple knockout approach to understanding cell wall hydrolase function in *Bacillus subtilis*.” *mBio* (2023-10). DOI: 10.1128/mbio.01760-23. URL: https://doi.org/10.1128/mbio.01760-23 (wilson2023anexhaustivemultiple pages 8-10)

6. Castanheira S, García-del Portillo F. “Evidence of two differentially regulated elongasomes in *Salmonella*.” *Communications Biology* (2023-09). DOI: 10.1038/s42003-023-05308-w. URL: https://doi.org/10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 1-2)

7. Galinier A, et al. “Recent Advances in Peptidoglycan Synthesis and Regulation in Bacteria.” *Biomolecules* (2023-04). DOI: 10.3390/biom13050720. URL: https://doi.org/10.3390/biom13050720 (galinier2023recentadvancesin pages 14-15)

8. Basan M, et al. “Homeostasis of cytoplasmic crowding by cell wall fluidization and ribosomal counterions.” *Research Square* (2024-04). DOI: 10.21203/rs.3.rs-4138690/v1. URL: https://doi.org/10.21203/rs.3.rs-4138690/v1 (basan2024homeostasisofcytoplasmic pages 10-12)

9. Kale T, et al. “Mechanics of *E. coli* cell width homeostasis and bulging dynamics from MreB and septum inhibition.” *bioRxiv* (2024-11-22). DOI: 10.1101/2024.11.22.624946. URL: https://doi.org/10.1101/2024.11.22.624946 (kale2024mechanicsofe. pages 1-4)


References

1. (middlemiss2024molecularmotortugofwar pages 1-2): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 20 citations and is from a highest quality peer-reviewed journal.

2. (willdigg2023adecreasein pages 1-3): Jessica R. Willdigg, Yesha Patel, and John D. Helmann. A decrease in fatty acid synthesis rescues cells with limited peptidoglycan synthesis capacity. mBio, Apr 2023. URL: https://doi.org/10.1128/mbio.00475-23, doi:10.1128/mbio.00475-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

4. (wilson2023anexhaustivemultiple pages 8-10): Sean A. Wilson, Raveen K. J. Tank, Jamie K. Hobbs, Simon J. Foster, and Ethan C. Garner. An exhaustive multiple knockout approach to understanding cell wall hydrolase function in <i>bacillus subtilis</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.01760-23, doi:10.1128/mbio.01760-23. This article has 37 citations and is from a domain leading peer-reviewed journal.

5. (kale2024mechanicsofe. pages 1-4): Tanvi Kale, Ryth Dasgupta, Mandar M. Inamdar, and Chaitanya A. Athale. Mechanics of e. coli cell width homeostasis and bulging dynamics from mreb and septum inhibition. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946, doi:10.1101/2024.11.22.624946. This article has 0 citations.

6. (shlosman2023allostericactivationof pages 1-2): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 44 citations and is from a highest quality peer-reviewed journal.

7. (middlemiss2024molecularmotortugofwar pages 8-9): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 20 citations and is from a highest quality peer-reviewed journal.

8. (castanheira2023evidenceoftwo pages 1-2): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 15 citations and is from a peer-reviewed journal.

9. (basan2024homeostasisofcytoplasmic pages 10-12): Markus Basan, Avik Mukherjee, Yanqing Huang, Seungeun Oh, Carlos Sanchez, Yu-Fang Chang, Xili Liu, Gary Bradshaw, Nina Benites, Johan Paulsson, Marc Kirschner, Yongjin Sung, and Jens Elgeti. Homeostasis of cytoplasmic crowding by cell wall fluidization and ribosomal counterions. Research Square, Apr 2024. URL: https://doi.org/10.21203/rs.3.rs-4138690/v1, doi:10.21203/rs.3.rs-4138690/v1. This article has 2 citations.

10. (galinier2023recentadvancesin pages 15-16): Anne Galinier, Clémentine Delan-Forino, Elodie Foulquier, Hakima Lakhal, and Frédérique Pompeo. Recent advances in peptidoglycan synthesis and regulation in bacteria. Biomolecules, 13:720, Apr 2023. URL: https://doi.org/10.3390/biom13050720, doi:10.3390/biom13050720. This article has 68 citations.

11. (galinier2023recentadvancesin pages 14-15): Anne Galinier, Clémentine Delan-Forino, Elodie Foulquier, Hakima Lakhal, and Frédérique Pompeo. Recent advances in peptidoglycan synthesis and regulation in bacteria. Biomolecules, 13:720, Apr 2023. URL: https://doi.org/10.3390/biom13050720, doi:10.3390/biom13050720. This article has 68 citations.