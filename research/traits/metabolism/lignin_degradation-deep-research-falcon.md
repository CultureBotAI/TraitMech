---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:09:27.852201'
end_time: '2026-06-18T05:29:26.960683'
duration_seconds: 1199.11
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: lignin degradation
  trait_identifier: traitmech:000114
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: lignin_degradation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biopolymer-degradation metabolism in which an organism breaks down
    lignin, the recalcitrant aromatic heteropolymer of plant cell walls, using oxidative
    enzymes such as peroxidases and laccases.
  parent_traits: traitmech:000110
  synonyms: ligninolytic
  evidence_summary: 'DOI:10.1039/c1np00042j:  (Bugg et al. review pathways for degradation
    of lignin in bacteria and fungi.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et
    al. cover lignin breakdown as part of lignocellulose degradation across the tree
    of life.)'
  causal_graph_summary: 'lignin_degradation_peroxidase_laccase: 3 nodes, 2 edges'
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
- **Trait label:** lignin degradation
- **METPO identifier:** traitmech:000114
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism breaks down lignin, the recalcitrant aromatic heteropolymer of plant cell walls, using oxidative enzymes such as peroxidases and laccases.
- **Parent traits:** traitmech:000110
- **Synonyms:** ligninolytic
- **Existing evidence:** DOI:10.1039/c1np00042j:  (Bugg et al. review pathways for degradation of lignin in bacteria and fungi.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. cover lignin breakdown as part of lignocellulose degradation across the tree of life.)
- **Existing causal graph summary:** lignin_degradation_peroxidase_laccase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **lignin degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/lignin_degradation.yaml`.

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
- **Trait label:** lignin degradation
- **METPO identifier:** traitmech:000114
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism breaks down lignin, the recalcitrant aromatic heteropolymer of plant cell walls, using oxidative enzymes such as peroxidases and laccases.
- **Parent traits:** traitmech:000110
- **Synonyms:** ligninolytic
- **Existing evidence:** DOI:10.1039/c1np00042j:  (Bugg et al. review pathways for degradation of lignin in bacteria and fungi.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. cover lignin breakdown as part of lignocellulose degradation across the tree of life.)
- **Existing causal graph summary:** lignin_degradation_peroxidase_laccase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **lignin degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/lignin_degradation.yaml`.

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


## Research report: microbial trait “lignin degradation” (METPO: traitmech:000114)

### 0) Executive scope summary
“Lignin degradation” (syn. ligninolytic) is best curated as a **microbial capacity to oxidatively depolymerize and/or chemically modify polymeric lignin** (the recalcitrant aromatic heteropolymer in plant cell walls), typically via **extracellular oxidative enzymes** (laccases, class-II fungal peroxidases, bacterial DyP peroxidases) and/or **low-molecular-weight oxidants/mediators** (e.g., Mn3+ as a diffusible oxidant; hydroxyl radical ·OH), producing smaller lignin-derived aromatics that can then be funneled into central aromatic catabolism (e.g., protocatechuate/catechol pathways and the β-ketoadipate pathway). (bugg2024thechemicallogic pages 6-7, zhao2024ligninbioconversionbased pages 1-2, werner2023ligninconversionto pages 1-2)

**Boundary cases important for curation**
- **Growth on “Kraft lignin” or lignin-rich industrial streams does not necessarily prove polymer depolymerization**, because such streams can contain low-molecular-weight aromatics that are more readily catabolized; depolymerization must be demonstrated by chemistry/structure change or product profiling. (bugg2024thechemicallogic pages 6-7)
- Evidence from **model dimers** (β-O-4, β-5) is strong for enzyme capability but may not always translate to whole-polymer activity; annotate such edges as “model-substrate supported” when needed. (zhou2024sequentialpretreatmentwith pages 8-10, metz2024catabolismofβ5 pages 11-14)
- **Aromatic funneling (downstream catabolism)** (e.g., VanAB/Vdh, β-ketoadipate pathway) is mechanistically linked but should be treated as a **distinct connected module** to avoid conflating “polymer depolymerization” with “monomer utilization.” (werner2023ligninconversionto pages 1-2, wolf2024thecatabolismof pages 1-3)

### 1) Key concepts & definitions (current understanding)

#### 1.1 Lignin chemical context (what is being degraded)
Lignin is a heterogeneous polymer derived from **S (syringyl), G (guaiacyl), and H (p-hydroxyphenyl) subunits** connected by diverse interunit linkages; β-O-4 is often dominant in grasses/biomass and β-5 is typically the second most common linkage (up to ~12% depending on biomass). (metz2024catabolismofβ5 pages 1-3, zhou2024sequentialpretreatmentwith pages 8-10)

#### 1.2 Mechanistic architecture of microbial lignin degradation
**Extracellular oxidation is required for initial polymer attack**, implying secretion/export and “physical access” constraints. (bugg2024thechemicallogic pages 6-7)
Key extracellular oxidative systems include:
- **Laccases / multicopper oxidases (EC 1.10.3.2)** often use **diffusible mediators**; lignin-derived aromatics (e.g., syringaldehyde, acetosyringone) can act as mediators in vivo. (bugg2024thechemicallogic pages 6-7)
- **Class-II fungal peroxidases** (LiP EC 1.11.1.14; MnP EC 1.11.1.13; VP EC 1.11.1.16) perform one-electron oxidations; MnP generates **Mn3+** which diffuses into lignin as a mediator/oxidant. (pei2024researchprogresson pages 19-21, bugg2024thechemicallogic pages 6-7)
- **Bacterial DyP-type peroxidases (EC 1.11.1.19)** can participate in polymeric lignin oxidation, often linked to Mn2+ oxidation and sometimes Mn2+-dependent activity. (bugg2024thechemicallogic pages 6-7, gu2024bacterialtransformationof pages 12-13)
- **Reactive oxygen species**: hydroxyl radical (·OH) is a low-molecular-weight oxidant capable of attacking lignin/lignocellulose; it can arise via Fenton-like chemistry and is also discussed as produced in lignin-degrading systems. (bugg2024thechemicallogic pages 6-7, zhou2024sequentialpretreatmentwith pages 8-10)

#### 1.3 Downstream aromatic catabolism (“biological funneling”)
After oxidative depolymerization releases monomers/low-MW fragments, microbes can convert mixtures to a single product (“biological funneling”). In bacteria, the **β-ketoadipate pathway** enables **convergent and atom-efficient (1 mol/mol) conversion** of various aromatic lignin-related compounds to β-ketoadipate, which can then enter the TCA cycle. (werner2023ligninconversionto pages 1-2)

### 2) Recent developments & latest research (prioritizing 2023–2024)

#### 2.1 Functional genetics for a ligninolytic bacterium (2024)
**Erwinia billingiae QL-Z3** provides a recent example linking specific enzymes to lignin degradation via genetics and enzyme assays. Under optimized conditions, QL-Z3 degraded **25.24%** of lignin at **1.5 g/L lignin** as the sole carbon source; knockouts of a laccase (ELAC_205), DyP peroxidase (EDYP_48), superoxide dismutase (ESOD_1236), and several oxygenase/catalase-related genes reduced lignin-degrading activity by **47–69%**. (zhao2024ligninbioconversionbased pages 1-2)
The same work reports fermentation-supernatant activities after optimization: **LiP 367.50 U/L**, **MnP 839.50 U/L**, **Lac 219.00 U/L**. (zhao2024ligninbioconversionbased pages 1-2)
A pathway schematic integrates LC–MS products across enzyme combinations (Figure 8). (zhao2024ligninbioconversionbased media d7af2add)

#### 2.2 Enzymology and “chemical logic” of lignin oxidation (2024)
Bugg (2024) emphasizes mechanistic constraints: initial lignin oxidation must be extracellular and often uses **diffusible oxidants/mediators**. MnP’s Mn3+ product diffuses into lignin, and laccases use small-molecule mediators; lignin-derived aromatics such as **syringaldehyde and acetosyringone** can function as mediators. (bugg2024thechemicallogic pages 6-7)
The same source warns that growth on industrial lignins may reflect utilization of contaminating low-MW aromatics rather than true polymer depolymerization. (bugg2024thechemicallogic pages 6-7)

#### 2.3 Direct β-O-4 cleavage by MnP and ROS-peroxidase synergy (2024)
A 2024 study on **Irpex lacteus** MnPs demonstrated that purified recombinant MnPs can cleave **β-O-4 linkages** in phenolic and non-phenolic lignin model dimers via **Cα hydroxyl oxidation followed by β-O-4 cleavage**. (zhou2024sequentialpretreatmentwith pages 8-10)
Sequential pretreatment of corn stover with **·OH then MnP** produced strong synergy: reducing sugars increased from **0.16 ± 0.01 mg/mL** (control) to **0.63 ± 0.04 mg/mL** (combined), a **290%** increase vs control (synergy factor **1.39**), and cellulose accessibility increased **182%** vs control. (zhou2024sequentialpretreatmentwith pages 8-10)

#### 2.4 New bacterial pathway for β-5 linked dimer catabolism (2024)
Metz et al. (mBio, 2024) elucidated a pathway for catabolism of the **β-5 linked dimer dehydrodiconiferyl alcohol (DC-A)** by **Novosphingobium aromaticivorans**, identifying enzymes that cleave this major lignin interunit linkage: **PcfL** (γ-formaldehyde lyase) opens the phenylcoumaran ring to produce a stilbene and **formaldehyde**; **LsdD** cleaves the stilbene to **vanillin + 5-formylferulate (5-FF)**; **FerD** oxidizes 5-FF to 5-carboxyferulate; **LigW** decarboxylates to **ferulic acid**. (metz2024catabolismofβ5 pages 1-3, metz2024catabolismofβ5 pages 11-14)
The engineered strain funnels DC-A-derived monomers to **PDC at ~92% yield**, illustrating a tight link between linkage cleavage and downstream funneling. (metz2024catabolismofβ5 pages 3-5)

#### 2.5 Host engineering to industrially relevant products from lignin aromatics (2023)
Werner et al. (Science Advances, 2023) engineered **Pseudomonas putida KT2440** to convert mixed lignin-related aromatics (p-coumarate/ferulate) to **β-ketoadipic acid** by tuning **O-demethylation, hydroxylation, and ring-opening** steps and deleting a global regulator. They report β-ketoadipate titers of **44.5 g/L** (model LRCs) and **25 g/L** (corn stover-derived LRCs), productivities **1.15** and **0.66 g/L·h**, and an overall yield of **0.10 g/g** corn stover-derived lignin. (werner2023ligninconversionto pages 1-2)
A technoeconomic analysis estimated a minimum selling price of **$2.01/kg**, potentially competitive with fossil-derived adipic acid. (werner2023ligninconversionto pages 1-2)

### 3) Current applications & real-world implementations

#### 3.1 Biorefineries: funneling lignin-derived mixtures to polymer precursors
The β-ketoadipate bioprocess above explicitly targets industrial relevance: titers up to **44.5 g/L** and TEA for a **100,000 MT/yr** scenario (modeling described in the paper) with an MSP of **$2.01/kg**. (werner2023ligninconversionto pages 1-2, werner2023ligninconversionto pages 10-11)

#### 3.2 Tandem chemocatalysis + microbial catabolism (emergent implementation pattern)
Wolf et al. (2024) position lignin valorization as a tandem of **chemical depolymerization** and **microbial conversion**. They show **Rhodococcus jostii RHA1** can catabolize major products of a **methylated lignin stream** (p-methoxybenzoate, veratrate, veratraldehyde) and identify enzymes required for growth and funneling, including cytochrome P450 components and VanAB/Vdh dependencies; a ΔpcaL phenotype indicates funneling via the **β-ketoadipate pathway**. (wolf2024thecatabolismof pages 1-3)

#### 3.3 Biomass pretreatment for saccharification: leveraging ROS and ligninolytic enzymes
The sequential **·OH → MnP** pretreatment of corn stover provides a recent demonstration of enhanced saccharification and accessibility, supporting an application pathway for “biological pretreatment” to lower recalcitrance. (zhou2024sequentialpretreatmentwith pages 8-10)

#### 3.4 Process optimization: metal supplementation to boost ligninolytic enzyme activities
A 2024 review summarizes that **Cu addition (0.5–1 mM)** can increase laccase activity by up to **100%**, and **Mn addition (1–18.2 mM)** can improve MnP activity. These are experimental levers often used in enzyme-production or pretreatment pipelines. (benavides2024enhancinglaccaseand pages 1-2)

### 4) Expert opinions & analysis (authoritative sources)
- **Extracellular access and mediation are central constraints**: Mn3+ diffusion and laccase mediators are highlighted as strategies for physical/chemical access to polymeric lignin, and the need for extracellular oxidation is emphasized. (bugg2024thechemicallogic pages 6-7)
- **Caution in interpreting “growth on lignin”**: growth on Kraft lignin does not necessarily prove polymer breakdown because of low-MW aromatics present; therefore, curation should privilege evidence such as product profiling, polymer-size change, or bond-cleavage demonstrations. (bugg2024thechemicallogic pages 6-7)
- **Bacterial pathways for non-β-O-4 linkages are expanding**: the β-5 pathway discovery (PcfL/LsdD/FerD/LigW) exemplifies new linkage-cleavage mechanisms beyond the historically dominant β-O-4 focus, supporting expansion of causal graph coverage. (metz2024catabolismofβ5 pages 11-14)

### 5) Relevant statistics and data (recent studies)
- **Erwinia billingiae QL-Z3**: 25.24% lignin degradation at 1.5 g/L; gene disruptions reduced activity 47–69%; optimized enzyme activities LiP 367.5 U/L, MnP 839.5 U/L, Lac 219.0 U/L. (zhao2024ligninbioconversionbased pages 1-2)
- **Pseudomonas putida** β-ketoadipate production: titers 44.5 g/L (model LRCs) and 25 g/L (corn stover LRCs); productivities 1.15 and 0.66 g/L·h; yield 0.10 g/g lignin; TEA MSP $2.01/kg. (werner2023ligninconversionto pages 1-2)
- **Irpex lacteus pretreatment**: combined ·OH+MnP gave 0.63 ± 0.04 mg/mL reducing sugars vs 0.16 ± 0.01 mg/mL control (290% increase) with synergy factor 1.39; cellulose accessibility 2.19 ± 0.14 vs 0.78 ± 0.02 control (182% improvement). (zhou2024sequentialpretreatmentwith pages 8-10)
- **Novosphingobium aromaticivorans**: β-5 dimer DC-A funneling to PDC at ~92% yield; defined enzyme steps for linkage cleavage and monomer release. (metz2024catabolismofβ5 pages 3-5, metz2024catabolismofβ5 pages 11-14)
- **Metal effects**: Cu 0.5–1 mM up to 100% higher laccase; Mn 1–18.2 mM improved MnP activity (reviewed). (benavides2024enhancinglaccaseand pages 1-2)

---

## TraitMech curation deliverables

### A) Candidate nodes grouped by type (with grounding suggestions)

#### A1) Trait/process nodes
- Lignin degradation (METPO: traitmech:000114) (given)
- Lignin depolymerization (label-only; connected sub-process)
- Biological funneling of aromatics to a convergent product (label-only concept) (werner2023ligninconversionto pages 1-2)
- β-ketoadipate pathway (label-only pathway node; strongly evidenced as downstream funnel) (werner2023ligninconversionto pages 1-2, wolf2024thecatabolismof pages 1-3)

#### A2) Enzymes / proteins / genes
Extracellular oxidative enzymes:
- Laccase (EC 1.10.3.2) (zhao2024ligninbioconversionbased pages 1-2)
- Lignin peroxidase (LiP, EC 1.11.1.14) (zhao2024ligninbioconversionbased pages 1-2)
- Manganese peroxidase (MnP, EC 1.11.1.13) (zhao2024ligninbioconversionbased pages 1-2)
- Versatile peroxidase (VP, EC 1.11.1.16) (zhao2024ligninbioconversionbased pages 1-2)
- DyP-type peroxidase (EC 1.11.1.19) (zhao2024ligninbioconversionbased pages 1-2)

Auxiliary / redox enzymes (supporting oxidative system):
- Superoxide dismutase (SOD; EC 1.15.1.1) (zhao2024ligninbioconversionbased pages 1-2)

Downstream aromatic catabolic enzymes (examples with strong recent evidence):
- VanAB (vanillate O-demethylase; label-only) (wolf2024thecatabolismof pages 1-3)
- Vdh (vanillin dehydrogenase; label-only) (wolf2024thecatabolismof pages 1-3)
- PcfL (γ-formaldehyde lyase; label-only) (metz2024catabolismofβ5 pages 1-3)
- LsdD (lignostilbene dioxygenase; label-only) (metz2024catabolismofβ5 pages 1-3)
- FerD (aldehyde dehydrogenase; label-only) (metz2024catabolismofβ5 pages 11-14)
- LigW (aromatic decarboxylase; label-only) (metz2024catabolismofβ5 pages 11-14)

Strain-specific nodes useful for curation (keep label-only unless curated later):
- ELAC_205 (laccase; E. billingiae QL-Z3) (zhao2024ligninbioconversionbased pages 1-2)
- EDYP_48 (DyP; E. billingiae QL-Z3) (zhao2024ligninbioconversionbased pages 1-2)
- ESOD_1236 (SOD; E. billingiae QL-Z3) (zhao2024ligninbioconversionbased pages 1-2)

#### A3) Chemicals / cofactors / mediators
- Hydrogen peroxide (H2O2; CHEBI:16240) (cuebas‐irizarry2024streptomycesspp.as pages 9-10)
- Hydroxyl radical (·OH; CHEBI:16247) (zhou2024sequentialpretreatmentwith pages 8-10)
- Mn2+ (CHEBI:29035); Mn3+ (CHEBI:29036) (pei2024researchprogresson pages 19-21, bugg2024thechemicallogic pages 6-7)
- Fe2+ (CHEBI:29033) as Fenton reagent in pretreatment context (zhou2024sequentialpretreatmentwith pages 3-4)
- Syringaldehyde (label-only; mediator) and acetosyringone (label-only; mediator) (bugg2024thechemicallogic pages 6-7)
- Formaldehyde (CHEBI:16842) released in β-5 cleavage via PcfL (metz2024catabolismofβ5 pages 1-3)
- Vanillin / vanillic acid / ferulic acid / 5-formylferulate / 5-carboxyferulate (label-only) (metz2024catabolismofβ5 pages 11-14)

#### A4) Environmental/experimental factor nodes
- Copper supplementation (0.5–1 mM) (benavides2024enhancinglaccaseand pages 1-2)
- Manganese supplementation (1–18.2 mM) (benavides2024enhancinglaccaseand pages 1-2)
- Sequential pretreatment order: ·OH then MnP (zhou2024sequentialpretreatmentwith pages 8-10)

### B) Evidence-backed causal edges (curation-ready)
The following table is provided as a curation starting point and contains subject–predicate–object triples with supporting snippets and notes.

| Edge (S–P–O) | Node type (S/O) | Suggested identifiers/CURIEs | Evidence snippet | Reference (DOI + URL + publication date) | Notes (mechanistic interpretation & curation suitability) | Certainty |
|---|---|---|---|---|---|---|
| laccase — participates_in — extracellular lignin depolymerization | protein → process | EC:1.10.3.2 / label-only lignin depolymerization | “LME includes lignin peroxidase (LiP, EC 1.11.1.14), manganese peroxidase (MnP, EC 1.11.1.13), versatile peroxidase (EC 1.11.1.16), laccase (Lac, EC 1.10.3.2) … participated in the depolymerization of large lignin polymers” (zhao2024ligninbioconversionbased pages 1-2) | 10.1186/s13068-024-02470-z; https://doi.org/10.1186/s13068-024-02470-z; 2024-02 | Good high-level trait edge for oxidative attack; broad across taxa. | high |
| DyP-type peroxidase — participates_in — lignin depolymerization | protein → process | EC:1.11.1.19 / label-only lignin depolymerization | “Dyp-decolorizing peroxidase (EC 1.11.1.19) … participated in the depolymerization of large lignin polymers” (zhao2024ligninbioconversionbased pages 1-2) | 10.1186/s13068-024-02470-z; https://doi.org/10.1186/s13068-024-02470-z; 2024-02 | Broad mechanistic node already aligned with bacterial ligninolysis. | high |
| lignin peroxidase — requires — hydrogen peroxide | protein → chemical | EC:1.11.1.14 / CHEBI:16240 (hydrogen peroxide) | “peroxidases … ‘require hydrogen peroxide (H2O2) or organic hydroperoxides (R-OOH) to oxidize reducing substrates’” (cuebas‐irizarry2024streptomycesspp.as pages 9-10) | 10.1111/1751-7915.14258; https://doi.org/10.1111/1751-7915.14258; 2024-04 | Support is general for peroxidases including LiP-class enzymes; curate as enzyme-class level unless narrowed. | medium |
| manganese peroxidase — oxidizes — Mn2+ | protein → chemical | EC:1.11.1.13 / CHEBI:29035 (Mn2+) | “manganese peroxidase oxidizes Mn2+ to Mn3+” (pei2024researchprogresson pages 19-21) | 10.3390/polym16172388; https://doi.org/10.3390/polym16172388; 2024-08 | Canonical MnP mechanism; suitable core edge. | high |
| Mn3+ — acts_as — diffusible oxidant/mediator in lignin | chemical → role/process | CHEBI:29036 (Mn3+) / label-only mediator role | “the Mn3+ oxidation product diffuses into the lignin … structure, acting as a diffusible oxidant or mediator” (bugg2024thechemicallogic pages 6-7) | 10.1039/d3cc05298b; https://doi.org/10.1039/d3cc05298b; 2024-01 | Important causal intermediary linking MnP to polymer attack. | high |
| laccase — uses — small-molecule mediators | protein → chemical class | EC:1.10.3.2 / label-only mediator | “Laccases or multi-copper oxidases can also utilise small molecule mediators” (bugg2024thechemicallogic pages 6-7) | 10.1039/d3cc05298b; https://doi.org/10.1039/d3cc05298b; 2024-01 | Broad edge; useful for fungal and some bacterial systems. | high |
| syringaldehyde — acts_as — laccase mediator | chemical → protein/process | CHEBI candidate label-only / EC:1.10.3.2 | “lignin-derived compounds such as syringaldehyde and acetosyringone are also efficient laccase mediators” (bugg2024thechemicallogic pages 6-7) | 10.1039/d3cc05298b; https://doi.org/10.1039/d3cc05298b; 2024-01 | Specific mediator example; likely curate as optional chemical node. | medium |
| acetosyringone — acts_as — laccase mediator | chemical → protein/process | CHEBI candidate label-only / EC:1.10.3.2 | “syringaldehyde and acetosyringone are also efficient laccase mediators” (bugg2024thechemicallogic pages 6-7) | 10.1039/d3cc05298b; https://doi.org/10.1039/d3cc05298b; 2024-01 | Same as above; specific in vivo-plausible mediator. | medium |
| hydroxyl radical — attacks — lignocellulosic surface structure | chemical → structure/process | CHEBI:16247 (hydroxyl radical) / label-only lignocellulosic surface | “⋅OH pretreatment could significantly enhance enzymatic saccharification by disrupting the smooth surface structure of corn stover” (zhou2024sequentialpretreatmentwith pages 8-10) | 10.1186/s13068-024-02583-5; https://doi.org/10.1186/s13068-024-02583-5; 2024-11 | Useful environmental/mechanistic edge; assay-specific to pretreatment but biologically meaningful. | high |
| Fenton-like system (FeSO4 + H2O2) — generates — hydroxyl radical | process/chemical system → chemical | CHEBI:29033 (Fe2+), CHEBI:16240 (H2O2), CHEBI:16247 (·OH) | “⋅OH pretreatment used a biomimetic Fenton-like system with FeSO4 … and H2O2” (zhou2024sequentialpretreatmentwith pages 3-4) | 10.1186/s13068-024-02583-5; https://doi.org/10.1186/s13068-024-02583-5; 2024-11 | Inferred generation step from experimental setup; curate as experimental-factor edge, not native microbial enzyme edge. | medium |
| sequential ·OH pretreatment then MnP treatment — increases — enzymatic saccharification of corn stover | process → process/outcome | label-only sequential pretreatment / label-only saccharification | “Sequential pretreatment … increased reducing-sugar yields … 0.63 ± 0.04 mg/mL … 290% vs control” (zhou2024sequentialpretreatmentwith pages 8-10) | 10.1186/s13068-024-02583-5; https://doi.org/10.1186/s13068-024-02583-5; 2024-11 | Valuable application edge; likely too assay/process-specific for core trait graph but useful in notes. | medium |
| sequential ·OH pretreatment then MnP treatment — increases — cellulose accessibility | process → process/property | label-only sequential pretreatment / label-only cellulose accessibility | “cellulose accessibility … was 1.33 … 1.03 … and 2.19 … corresponding to … 182%” (zhou2024sequentialpretreatmentwith pages 8-10) | 10.1186/s13068-024-02583-5; https://doi.org/10.1186/s13068-024-02583-5; 2024-11 | Strong process evidence; probably application layer rather than canonical trait edge. | medium |
| MnP — cleaves — β-O-4 bond | protein → bond/process | EC:1.11.1.13 / label-only β-O-4 bond cleavage | “MnPs from the white rot fungus I. lacteus could cleave the β-O-4 bond in phenolic and non-phenolic lignin model dimers” (zhou2024sequentialpretreatmentwith pages 8-10) | 10.1186/s13068-024-02583-5; https://doi.org/10.1186/s13068-024-02583-5; 2024-11 | Strong direct mechanistic edge from purified enzymes. | high |
| DyPB — cleaves — β-O-4 aryl ether bond | protein → bond/process | DyPB label-only / label-only β-O-4 bond cleavage | “DyPB decomposes lignin into low molecular weight lignin-derived compounds, which leads to the cleavage of aryl ether bonds such as β-O-4 and α-O-4” (gu2024bacterialtransformationof pages 12-13) | 10.1186/s13068-023-02447-4; https://doi.org/10.1186/s13068-023-02447-4; 2024-01 | Good bacterial edge; taxon-specific to DyPB examples. | high |
| DyPB — cleaves — β-5 C–C bond | protein → bond/process | DyPB label-only / label-only β-5 bond cleavage | “DyPB decomposes lignin … leads to the cleavage of … C–C bonds such as β-5 and β–β” (gu2024bacterialtransformationof pages 12-13) | 10.1186/s13068-023-02447-4; https://doi.org/10.1186/s13068-023-02447-4; 2024-01 | Important evidence that bacterial DyP can attack non-ether interunit bonds. | medium |
| lignin peroxidase — cleaves — Cα–Cβ bond | protein → bond/process | EC:1.11.1.14 / label-only Cα–Cβ bond cleavage | “ALiP-P3 … Break the Cα-Cβ bond of the β-O-4 model compound” (gu2024bacterialtransformationof pages 12-13) | 10.1186/s13068-023-02447-4; https://doi.org/10.1186/s13068-023-02447-4; 2024-01 | Strong but model-compound based; suitable as enzyme capability edge. | high |
| laccase ELAC_205 — positively_regulates — lignin degradation activity in Erwinia billingiae QL-Z3 | gene/protein → process | NCBITaxon:?? (Erwinia billingiae label-only) / ELAC_205 / EC:1.10.3.2 | “Disruption of the gene for ELAC_205 (laccase) … significantly reduced the lignin-degrading activity of QL-Z3 by 47–69%” (zhao2024ligninbioconversionbased pages 1-2) | 10.1186/s13068-024-02470-z; https://doi.org/10.1186/s13068-024-02470-z; 2024-02 | Strong functional-genetic evidence, but strain-specific. | high |
| Dyp-type peroxidase EDYP_48 — positively_regulates — lignin degradation activity in Erwinia billingiae QL-Z3 | gene/protein → process | EDYP_48 / EC:1.11.1.19 | “Disruption of … EDYP_48 (Dyp-type peroxidase) … significantly reduced the lignin-degrading activity of QL-Z3 by 47–69%” (zhao2024ligninbioconversionbased pages 1-2) | 10.1186/s13068-024-02470-z; https://doi.org/10.1186/s13068-024-02470-z; 2024-02 | Strong strain-specific causality; good optional edge. | high |
| superoxide dismutase ESOD_1236 — positively_regulates — lignin degradation activity in Erwinia billingiae QL-Z3 | gene/protein → process | EC:1.15.1.1 / ESOD_1236 | “Disruption of … ESOD_1236 (superoxide dismutase) … significantly reduced the lignin-degrading activity of QL-Z3 by 47–69%” (zhao2024ligninbioconversionbased pages 1-2) | 10.1186/s13068-024-02470-z; https://doi.org/10.1186/s13068-024-02470-z; 2024-02 | Useful auxiliary-enzyme edge; likely indirect via ROS handling. | high |
| manganese superoxide dismutase — causes — aryl-Cα and Cα–Cβ oxidative cleavage | protein → bond/process | EC:1.15.1.1 / label-only bond cleavage | “MnSOD … oxidative cleavage and o-demethylation of aryl-cα and Cα-Cβ bonds” (gu2024bacterialtransformationof pages 12-13) | 10.1186/s13068-023-02447-4; https://doi.org/10.1186/s13068-023-02447-4; 2024-01 | Evidence from enzyme table/review; suitable as lower-confidence broad edge. | medium |
| VanAB (vanillate O-demethylase) — O-demethylates — vanillate | protein/complex → chemical | VanAB label-only / vanillate label-only | “Veratraldehyde and veratrate catabolism required both vanillin dehydrogenase (Vdh) and vanillate O-demethylase (VanAB)” (wolf2024thecatabolismof pages 1-3) | 10.1128/aem.02155-23; https://doi.org/10.1128/aem.02155-23; 2024-02 | Direct support for demethylation node in downstream funneling. | high |
| Vdh (vanillin dehydrogenase) — oxidizes — vanillin to vanillate | protein → chemical | Vdh label-only / vanillin label-only / vanillate label-only | “FerD is … able to oxidize … vanillin to vanillic acid” (metz2024catabolismofβ5 pages 11-14) | 10.1128/mbio.01718-24; https://doi.org/10.1128/mbio.01718-24; 2024-07 | Current context gives strongest explicit oxidation edge for FerD; Vdh requirement is indirect in Wolf. Use vanillin→vanillate broadly but note mixed enzyme support. | medium |
| PcfL — opens — β-5 phenylcoumaran ring to stilbene + formaldehyde | protein → reaction/product | PcfL label-only / formaldehyde CHEBI:16842 | “PcfL opens the phenylcoumaran ring to form a stilbene and formaldehyde” (metz2024catabolismofβ5 pages 1-3) | 10.1128/mbio.01718-24; https://doi.org/10.1128/mbio.01718-24; 2024-07 | Excellent direct edge for β-5 dimer catabolism. | high |
| LsdD — cleaves — lignostilbene to vanillin + 5-formylferulate | protein → chemicals | LsdD label-only / vanillin label-only / 5-formylferulate label-only | “LsdD … cleaves the stilbene to generate the aromatic monomers vanillin and 5-formylferulate (5-FF)” (metz2024catabolismofβ5 pages 1-3) | 10.1128/mbio.01718-24; https://doi.org/10.1128/mbio.01718-24; 2024-07 | Strong causal step for oligomer-to-monomer release. | high |
| FerD — oxidizes — 5-formylferulate to 5-carboxyferulate | protein → chemical | FerD label-only / 5-FF label-only / 5-CF label-only | “5-FF is oxidized to 5-CF by FerD” (metz2024catabolismofβ5 pages 11-14) | 10.1128/mbio.01718-24; https://doi.org/10.1128/mbio.01718-24; 2024-07 | Strong step in downstream funneling. | high |
| LigW — decarboxylates — 5-carboxyferulate to ferulate | protein → chemical | LigW label-only / ferulate label-only | “LigW decarboxylates 5-CF to ferulic acid” (metz2024catabolismofβ5 pages 11-14) | 10.1128/mbio.01718-24; https://doi.org/10.1128/mbio.01718-24; 2024-07 | Strong direct edge. | high |
| ΔpcaL phenotype — indicates_catabolism_through — β-ketoadipate pathway | genotype/marker → pathway | pcaL label-only / β-ketoadipate pathway label-only | “A ΔpcaL strain grew on neither p-MBA nor veratrate, indicating they are catabolized through the β-ketoadipate pathway” (wolf2024thecatabolismof pages 1-3) | 10.1128/aem.02155-23; https://doi.org/10.1128/aem.02155-23; 2024-02 | Good pathway-level funneling edge from genetic evidence. | high |
| copper supplementation — increases — laccase activity | chemical/environmental factor → process | CHEBI:28694 (copper cation) / EC:1.10.3.2 | “copper addition is associated with increased laccase activity … up to 100% at doses between 0.5–1 mM” (benavides2024enhancinglaccaseand pages 1-2) | 10.3390/agronomy14112562; https://doi.org/10.3390/agronomy14112562; 2024-10 | Environmental modulation edge; useful as assay factor, not intrinsic mechanism. | high |
| manganese supplementation — increases — MnP activity | chemical/environmental factor → process | CHEBI:29035 (Mn2+) / EC:1.11.1.13 | “manganese addition improves MnP activity across a broad range (1–18.2 mM Mn)” (benavides2024enhancinglaccaseand pages 1-2) | 10.3390/agronomy14112562; https://doi.org/10.3390/agronomy14112562; 2024-10 | Strong assay-factor edge; may be curated as environmental factor. | high |


*Table: This table lists evidence-backed candidate subject–predicate–object edges for curating a TraitMech causal graph of microbial lignin degradation. It emphasizes extracellular oxidative attack, bond cleavage chemistry, auxiliary enzymes, aromatic funneling, and experimentally supported modulation by metals and pretreatment conditions.*

### C) Visual evidence from a primary source
A pathway schematic integrating LC–MS-detected products with the actions of ELAC_205 (laccase), EDYP_48 (DyP), and ESOD_1236 (SOD) in *Erwinia billingiae* QL-Z3 is available as Figure 8 in Zhao et al. (2024). (zhao2024ligninbioconversionbased media d7af2add)

---

## Warnings / claims not yet ready for curation
1. **Peroxidase “requires H2O2”** is strongly correct at class level, but in the provided evidence it is stated generally for peroxidases; curate at the correct enzyme-class granularity unless you have LiP/MnP-specific wording in the future. (cuebas‐irizarry2024streptomycesspp.as pages 9-10)
2. **Some edges in review tables** (e.g., DyPB cleavage of multiple bond types; MnSOD bond cleavage) are synthesized from multiple cited works; treat as “review-supported” unless primary data are added to evidence. (gu2024bacterialtransformationof pages 12-13)
3. **Fenton-like ·OH pretreatment** is an experimental process; do not treat FeSO4/H2O2-driven ·OH generation as an intrinsic microbial node unless you have evidence for enzymatic iron reduction and in situ Fenton chemistry attributable to the organism in the curated context. (zhou2024sequentialpretreatmentwith pages 3-4)
4. **Pathway identifiers (KEGG/MetaCyc/Rhea) and UniProt IDs** were not provided in the evidence; keep nodes as label-only until grounded with stable database records.

---

## DOI-first bibliography (with URLs and publication dates)

1. Werner AZ, et al. *Lignin conversion to β-ketoadipic acid by Pseudomonas putida via metabolic engineering and bioprocess development.* Science Advances. **2023-09-06**. DOI: **10.1126/sciadv.adj0053**. URL: https://doi.org/10.1126/sciadv.adj0053 (werner2023ligninconversionto pages 1-2)
2. Bugg TDH. *The chemical logic of enzymatic lignin degradation.* Chemical Communications. **2024-01**. DOI: **10.1039/d3cc05298b**. URL: https://doi.org/10.1039/d3cc05298b (bugg2024thechemicallogic pages 6-7)
3. Zhao S, et al. *Lignin bioconversion based on genome mining for ligninolytic genes in Erwinia billingiae QL-Z3.* Biotechnology for Biofuels and Bioproducts. **2024-02**. DOI: **10.1186/s13068-024-02470-z**. URL: https://doi.org/10.1186/s13068-024-02470-z (zhao2024ligninbioconversionbased pages 1-2)
4. Wolf ME, et al. *The catabolism of lignin-derived p-methoxylated aromatic compounds by Rhodococcus jostii RHA1.* Applied and Environmental Microbiology. **2024-02-21**. DOI: **10.1128/aem.02155-23**. URL: https://doi.org/10.1128/aem.02155-23 (wolf2024thecatabolismof pages 1-3)
5. Metz F, et al. *Catabolism of β-5 linked aromatics by Novosphingobium aromaticivorans.* mBio. **2024-07-16** (published online per article). DOI: **10.1128/mbio.01718-24**. URL: https://doi.org/10.1128/mbio.01718-24 (metz2024catabolismofβ5 pages 1-3)
6. Zhou M, et al. *Sequential pretreatment with hydroxyl radical and manganese peroxidase for the efficient enzymatic saccharification of corn stover.* Biotechnology for Biofuels and Bioproducts. **2024-11**. DOI: **10.1186/s13068-024-02583-5**. URL: https://doi.org/10.1186/s13068-024-02583-5 (zhou2024sequentialpretreatmentwith pages 8-10)
7. Benavides V, et al. *Enhancing Laccase and Manganese Peroxidase Activity in White-Rot Fungi: The Role of Copper, Manganese, and Lignocellulosic Substrates.* Agronomy. **2024-10-31**. DOI: **10.3390/agronomy14112562**. URL: https://doi.org/10.3390/agronomy14112562 (benavides2024enhancinglaccaseand pages 1-2)
8. Gu J, et al. *Bacterial transformation of lignin: key enzymes and high-value products.* Biotechnology for Biofuels and Bioproducts. **2024-01**. DOI: **10.1186/s13068-023-02447-4**. URL: https://doi.org/10.1186/s13068-023-02447-4 (gu2024bacterialtransformationof pages 12-13)
9. Pei Z, et al. *Research progress on lignin depolymerization strategies: a review.* Polymers. **2024-08**. DOI: **10.3390/polym16172388**. URL: https://doi.org/10.3390/polym16172388 (pei2024researchprogresson pages 19-21)
10. Cuebas-Irizarry MF, Grunden AM. *Streptomyces spp. as biocatalyst sources in pulp and paper and textile industries: biodegradation, bioconversion and valorization of waste.* Microbial Biotechnology. **2024-04**. DOI: **10.1111/1751-7915.14258**. URL: https://doi.org/10.1111/1751-7915.14258 (cuebas‐irizarry2024streptomycesspp.as pages 9-10)


References

1. (bugg2024thechemicallogic pages 6-7): Timothy D. H. Bugg. The chemical logic of enzymatic lignin degradation. Chemical Communications, 60:804-814, Jan 2024. URL: https://doi.org/10.1039/d3cc05298b, doi:10.1039/d3cc05298b. This article has 76 citations and is from a domain leading peer-reviewed journal.

2. (zhao2024ligninbioconversionbased pages 1-2): Shuting Zhao, Dongtao Deng, Tianzheng Wan, Jie Feng, Lei Deng, Qianyi Tian, Jiayu Wang, Umm E. Aiman, Balym Mukhaddi, Xiaofeng Hu, Shaolin Chen, Ling Qiu, Lili Huang, and Yahong Wei. Lignin bioconversion based on genome mining for ligninolytic genes in erwinia billingiae ql-z3. Biotechnology for Biofuels and Bioproducts, Feb 2024. URL: https://doi.org/10.1186/s13068-024-02470-z, doi:10.1186/s13068-024-02470-z. This article has 20 citations and is from a domain leading peer-reviewed journal.

3. (werner2023ligninconversionto pages 1-2): Allison Z. Werner, William T. Cordell, Ciaran W. Lahive, Bruno C. Klein, Christine A. Singer, Eric C. D. Tan, Morgan A. Ingraham, Kelsey J. Ramirez, Dong Hyun Kim, Jacob Nedergaard Pedersen, Christopher W. Johnson, Brian F. Pfleger, Gregg T. Beckham, and Davinia Salvachúa. Lignin conversion to β-ketoadipic acid by <i>pseudomonas putida</i> via metabolic engineering and bioprocess development. Science Advances, Sep 2023. URL: https://doi.org/10.1126/sciadv.adj0053, doi:10.1126/sciadv.adj0053. This article has 89 citations and is from a highest quality peer-reviewed journal.

4. (zhou2024sequentialpretreatmentwith pages 8-10): Man Zhou, Yaru Wang, Yuan Wang, Tao Tu, Jie Zhang, Xiaolu Wang, Guijie Zhang, Huo-qing Huang, Bin Yao, Huiying Luo, and Xing Qin. Sequential pretreatment with hydroxyl radical and manganese peroxidase for the efficient enzymatic saccharification of corn stover. Biotechnology for Biofuels and Bioproducts, Nov 2024. URL: https://doi.org/10.1186/s13068-024-02583-5, doi:10.1186/s13068-024-02583-5. This article has 6 citations and is from a domain leading peer-reviewed journal.

5. (metz2024catabolismofβ5 pages 11-14): Fletcher Metz, Abigail M. Olsen, Fachuang Lu, Kevin S. Myers, Marco N. Allemann, Joshua K. Michener, Daniel R. Noguera, and Timothy J. Donohue. Catabolism of β-5 linked aromatics by <i>novosphingobium aromaticivorans</i>. Aug 2024. URL: https://doi.org/10.1128/mbio.01718-24, doi:10.1128/mbio.01718-24. This article has 20 citations and is from a domain leading peer-reviewed journal.

6. (wolf2024thecatabolismof pages 1-3): Megan E. Wolf, Anne T. Lalande, Brianne L. Newman, Alissa C. Bleem, Chad T. Palumbo, Gregg T. Beckham, and Lindsay D. Eltis. The catabolism of lignin-derived p-methoxylated aromatic compounds by rhodococcus jostii rha1. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.02155-23, doi:10.1128/aem.02155-23. This article has 18 citations and is from a peer-reviewed journal.

7. (metz2024catabolismofβ5 pages 1-3): Fletcher Metz, Abigail M. Olsen, Fachuang Lu, Kevin S. Myers, Marco N. Allemann, Joshua K. Michener, Daniel R. Noguera, and Timothy J. Donohue. Catabolism of β-5 linked aromatics by <i>novosphingobium aromaticivorans</i>. Aug 2024. URL: https://doi.org/10.1128/mbio.01718-24, doi:10.1128/mbio.01718-24. This article has 20 citations and is from a domain leading peer-reviewed journal.

8. (pei2024researchprogresson pages 19-21): Zhengfei Pei, Xiaofang Liu, Jiasheng Chen, Huan Wang, and Hu Li. Research progress on lignin depolymerization strategies: a review. Polymers, 16:2388, Aug 2024. URL: https://doi.org/10.3390/polym16172388, doi:10.3390/polym16172388. This article has 36 citations.

9. (gu2024bacterialtransformationof pages 12-13): Jinming Gu, Qing Qiu, Yue Yu, Xuejian Sun, Kejian Tian, Menghan Chang, Yibing Wang, Fenglin Zhang, and Hongliang Huo. Bacterial transformation of lignin: key enzymes and high-value products. Biotechnology for Biofuels and Bioproducts, Jan 2024. URL: https://doi.org/10.1186/s13068-023-02447-4, doi:10.1186/s13068-023-02447-4. This article has 84 citations and is from a domain leading peer-reviewed journal.

10. (zhao2024ligninbioconversionbased media d7af2add): Shuting Zhao, Dongtao Deng, Tianzheng Wan, Jie Feng, Lei Deng, Qianyi Tian, Jiayu Wang, Umm E. Aiman, Balym Mukhaddi, Xiaofeng Hu, Shaolin Chen, Ling Qiu, Lili Huang, and Yahong Wei. Lignin bioconversion based on genome mining for ligninolytic genes in erwinia billingiae ql-z3. Biotechnology for Biofuels and Bioproducts, Feb 2024. URL: https://doi.org/10.1186/s13068-024-02470-z, doi:10.1186/s13068-024-02470-z. This article has 20 citations and is from a domain leading peer-reviewed journal.

11. (metz2024catabolismofβ5 pages 3-5): Fletcher Metz, Abigail M. Olsen, Fachuang Lu, Kevin S. Myers, Marco N. Allemann, Joshua K. Michener, Daniel R. Noguera, and Timothy J. Donohue. Catabolism of β-5 linked aromatics by <i>novosphingobium aromaticivorans</i>. Aug 2024. URL: https://doi.org/10.1128/mbio.01718-24, doi:10.1128/mbio.01718-24. This article has 20 citations and is from a domain leading peer-reviewed journal.

12. (werner2023ligninconversionto pages 10-11): Allison Z. Werner, William T. Cordell, Ciaran W. Lahive, Bruno C. Klein, Christine A. Singer, Eric C. D. Tan, Morgan A. Ingraham, Kelsey J. Ramirez, Dong Hyun Kim, Jacob Nedergaard Pedersen, Christopher W. Johnson, Brian F. Pfleger, Gregg T. Beckham, and Davinia Salvachúa. Lignin conversion to β-ketoadipic acid by <i>pseudomonas putida</i> via metabolic engineering and bioprocess development. Science Advances, Sep 2023. URL: https://doi.org/10.1126/sciadv.adj0053, doi:10.1126/sciadv.adj0053. This article has 89 citations and is from a highest quality peer-reviewed journal.

13. (benavides2024enhancinglaccaseand pages 1-2): Viviana Benavides, Gustavo Ciudad, Fernanda Pinto-Ibieta, Tatiana Robledo, Olga Rubilar, and Antonio Serrano. Enhancing laccase and manganese peroxidase activity in white-rot fungi: the role of copper, manganese, and lignocellulosic substrates. Agronomy, 14:2562, Oct 2024. URL: https://doi.org/10.3390/agronomy14112562, doi:10.3390/agronomy14112562. This article has 32 citations and is from a peer-reviewed journal.

14. (cuebas‐irizarry2024streptomycesspp.as pages 9-10): Mara F. Cuebas‐Irizarry and Amy M. Grunden. Streptomyces spp. as biocatalyst sources in pulp and paper and textile industries: biodegradation, bioconversion and valorization of waste. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14258, doi:10.1111/1751-7915.14258. This article has 25 citations and is from a peer-reviewed journal.

15. (zhou2024sequentialpretreatmentwith pages 3-4): Man Zhou, Yaru Wang, Yuan Wang, Tao Tu, Jie Zhang, Xiaolu Wang, Guijie Zhang, Huo-qing Huang, Bin Yao, Huiying Luo, and Xing Qin. Sequential pretreatment with hydroxyl radical and manganese peroxidase for the efficient enzymatic saccharification of corn stover. Biotechnology for Biofuels and Bioproducts, Nov 2024. URL: https://doi.org/10.1186/s13068-024-02583-5, doi:10.1186/s13068-024-02583-5. This article has 6 citations and is from a domain leading peer-reviewed journal.