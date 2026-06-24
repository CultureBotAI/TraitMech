---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:11:18.160777'
end_time: '2026-06-18T05:21:07.661920'
duration_seconds: 589.5
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: manganese oxidation
  trait_identifier: traitmech:000032
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: manganese_oxidation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which bacteria oxidize soluble Mn(II) to insoluble Mn(III/IV)
    oxides, typically catalyzed by multicopper oxidases. Characteristic of organisms
    such as Bacillus sp. SG-1, Leptothrix, and Pseudomonas putida.
  parent_traits: METPO:1000060
  synonyms: Mn(II) oxidation
  evidence_summary: 'DOI:10.1016/j.tim.2005.07.009:  (Tebo et al., "Geomicrobiology
    of manganese(II) oxidation", supports bacterial Mn(II) oxidation to Mn oxides
    via a multicopper-oxidase mechanism.) | DOI:10.1146/annurev.earth.32.101802.120213:  (Tebo
    et al., "Biogenic manganese oxides", supports the formation and properties of
    bacterially produced Mn(III/IV) oxides.)'
  causal_graph_summary: 'manganese_oxidation_multicopper_oxidase: 3 nodes, 2 edges'
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
- **Trait label:** manganese oxidation
- **METPO identifier:** traitmech:000032
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which bacteria oxidize soluble Mn(II) to insoluble Mn(III/IV) oxides, typically catalyzed by multicopper oxidases. Characteristic of organisms such as Bacillus sp. SG-1, Leptothrix, and Pseudomonas putida.
- **Parent traits:** METPO:1000060
- **Synonyms:** Mn(II) oxidation
- **Existing evidence:** DOI:10.1016/j.tim.2005.07.009:  (Tebo et al., "Geomicrobiology of manganese(II) oxidation", supports bacterial Mn(II) oxidation to Mn oxides via a multicopper-oxidase mechanism.) | DOI:10.1146/annurev.earth.32.101802.120213:  (Tebo et al., "Biogenic manganese oxides", supports the formation and properties of bacterially produced Mn(III/IV) oxides.)
- **Existing causal graph summary:** manganese_oxidation_multicopper_oxidase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **manganese oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/manganese_oxidation.yaml`.

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
- **Trait label:** manganese oxidation
- **METPO identifier:** traitmech:000032
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which bacteria oxidize soluble Mn(II) to insoluble Mn(III/IV) oxides, typically catalyzed by multicopper oxidases. Characteristic of organisms such as Bacillus sp. SG-1, Leptothrix, and Pseudomonas putida.
- **Parent traits:** METPO:1000060
- **Synonyms:** Mn(II) oxidation
- **Existing evidence:** DOI:10.1016/j.tim.2005.07.009:  (Tebo et al., "Geomicrobiology of manganese(II) oxidation", supports bacterial Mn(II) oxidation to Mn oxides via a multicopper-oxidase mechanism.) | DOI:10.1146/annurev.earth.32.101802.120213:  (Tebo et al., "Biogenic manganese oxides", supports the formation and properties of bacterially produced Mn(III/IV) oxides.)
- **Existing causal graph summary:** manganese_oxidation_multicopper_oxidase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **manganese oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/manganese_oxidation.yaml`.

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


# Research Report: Microbial Trait “Manganese Oxidation” (METPO traitmech:000032)

## 0) Executive Scope Summary (Trait Scope)

**Trait definition (curation-ready):** *Microbial manganese oxidation* is the physiological capacity of a microbe (or microbial community) to catalyze the oxidation of soluble Mn(II) to insoluble Mn(III/IV) oxide minerals (“biogenic Mn oxides”, BioMnOx), typically via extracellular or cell-surface-associated oxidoreductases, commonly **multicopper oxidases (MCOs)** and, in some taxa, **heme peroxidase / catalase-peroxidase-type enzymes**. (novikova2024cryoemstructureof pages 1-2, ding2024catalaseperoxidasestkatg2from pages 1-2)

**Trait readouts:** (i) precipitation/accumulation of Mn oxides on cells/media; (ii) decrease in dissolved Mn(II); (iii) positive Mn oxide stains/analytical mineral ID (e.g., LBB stain, XRD/XPS/EPR/XANES); and in applied systems, (iv) decreased effluent dissolved Mn. (tsushima2024formationofbiogenic pages 3-5, earle2023rawwaterbiofiltration pages 1-2, fu2024biogenicmanganeseoxide pages 4-6)

**Boundary cases / nearby traits:**
- **Not** Mn uptake/assimilation (intracellular Mn homeostasis) nor Mn(IV) reduction (dissimilatory metal reduction). The trait specifically concerns oxidation and oxide mineral formation. (novikova2024cryoemstructureof pages 1-2)
- **Not** purely abiotic oxidation (which can occur at high pH or with chemical oxidants); the trait requires microbial catalysis and/or microbially produced oxidants/enzymes. Enzymatic work explicitly notes conditions where chemical oxidation can dominate (e.g., above pH ~8 in one enzyme system). (ding2024catalaseperoxidasestkatg2from pages 4-6)
- **Assay dependence warning:** different enzyme classes can mediate Mn oxidation (MCO vs peroxidase/catalase-peroxidase), and different oxidants may be used (O2 directly vs peroxide/superoxide pathways), so mechanistic nodes/edges may be clade- or assay-specific. (novikova2024cryoemstructureof pages 1-2, kurdi2023aninsilicostudy pages 24-30)

## 1) Key Concepts and Current Understanding

### 1.1 Core chemistry and ecological significance
Microbes oxidize Mn(II) to Mn(IV)-level oxides through intermediate Mn(III) species; these oxides are often poorly crystalline layered minerals (e.g., birnessite/vernadite-like) and can be highly reactive sorbents/oxidants. The Mnx system work explicitly frames microbial Mn(II) oxidation as a major driver of the global Mn cycle and as biomineralization of MnO2-type solids. (novikova2024cryoemstructureof pages 1-2, tsushima2024formationofbiogenic pages 3-5)

### 1.2 Two major mechanistic “routes” to Mn(II) oxidation

**Route A: Multicopper oxidase (MCO)-mediated oxidation using O2 directly.**
- In Bacillus sp. PL-12, the **Mnx** complex is an MCO-based enzyme system that can use **O2 directly** rather than requiring peroxide/superoxide, and the structural work supports a mechanistic pathway involving **binuclear Mn intermediates** proceeding through oxidation states II → III → IV en route to MnO2. (novikova2024cryoemstructureof pages 1-2)

**Route B: Heme peroxidase / catalase-peroxidase-mediated Mn(II) oxidation (often coupled to peroxide chemistry).**
- A catalase-peroxidase, **StKatG2** from *Salinicola tamaricis* (heterologously expressed/purified), shows measurable Mn(II)-oxidizing activity and produces **mixed-valence** Mn oxides; it also couples this chemistry to dye removal. (ding2024catalaseperoxidasestkatg2from pages 1-2, ding2024catalaseperoxidasestkatg2from pages 9-11)

## 2) Recent Developments and Latest Research (Prioritizing 2023–2024)

### 2.1 2024 structural breakthrough: Cryo-EM of the Bacillus Mnx complex (mechanism-enabling structure)
A 2024 JACS study resolved a **3.4 Å cryo-EM structure** of the **Mnx complex** from *Bacillus* sp. PL-12. The complex comprises **MnxG** (a ~138 kDa MCO) capped by an **MnxE3F3** heterohexameric ring; importantly, a **tunnel** runs through MnxG and the MnxE3F3 cap with dimensions/electrostatics compatible with proposed hydroxide-bridged binuclear Mn intermediates. (novikova2024cryoemstructureof pages 1-2)

The mechanistic model includes (i) a cooperative step yielding **Mn(III)(OH)Mn(III)** that can be stabilized/translocated in a negatively charged region, and (ii) **disproportionation** forming **Mn(IV)(O)Mn(IV)**, with hypothesized deprotonation/condensation and nanoparticle release through the MnxE3F3 pore. (novikova2024cryoemstructureof pages 7-8)

**Expert-analysis value for curation:** This paper provides unusually concrete *mechanistic entities* (protein complex architecture; tunnel; intermediate species) that can be captured as TraitMech nodes/edges with higher confidence than older purely genetic associations. (novikova2024cryoemstructureof pages 1-2, novikova2024cryoemstructureof pages 7-8)

### 2.2 2024 materials/catalysis advance: Mnx-generated BioMnOx can catalyze oxygen evolution
A 2024 ACS Catalysis study produced **biogenic MnOx materials** by aerobic Mn(II) oxidation using purified **MnxE3F3G** and showed these BioMnOx can catalyze the **oxygen evolution reaction (OER)**.

Key quantitative data:
- BioMnOx morphology and mineralogy varied with Mn(II)/Mnx ratio and time (e.g., rods ~100 × 20 nm for one condition). (fu2024biogenicmanganeseoxide pages 2-4)
- BioMnOx-II showed **η ≈ 700 mV at 8.3 A/g·cm²** (≈60 mV lower than synthetic monoclinic birnessite) and a stabilized current density **≈6 A/g·cm² at 1.6 V** (≈2 A/g·cm² higher than birnessite). (fu2024biogenicmanganeseoxide pages 2-4)
- Surface-accessible Mn(III) (EPR/XPS/pyrophosphate extraction) correlated with higher OER activity. (fu2024biogenicmanganeseoxide pages 4-6, fu2024biogenicmanganeseoxide pages 6-8)

**Curation relevance:** While OER is an application property (not the microbe’s primary phenotype), the work strengthens the “downstream function” edges from BioMnOx composition/state (e.g., Mn(III) surface sites) to oxidative reactivity. (fu2024biogenicmanganeseoxide pages 4-6, fu2024biogenicmanganeseoxide pages 2-4)

### 2.3 2024 microbial genetics development: Cold-tolerant manganese-oxidizing Pseudomonas isolates
A 2024 Applied and Environmental Microbiology study isolated cold-tolerant Mn-oxidizing *Pseudomonas* strains that oxidize Mn at **4°C** and carry homologs of several Mn oxidation-associated genes known from *Pseudomonas putida* GB-1, including **mnxG, mcoA, mnxS1, mnxS2, and mnxR**. (jones2024isolationcharacterizationand pages 1-2)

**Curation relevance:** Supports nodes/edges linking a regulatory two-component system to expression/operation of Mn oxidation modules, and adds an environmental factor edge (low temperature) affecting trait expression. (jones2024isolationcharacterizationand pages 1-2)

### 2.4 2024 enzyme biochemistry: Catalase-peroxidase StKatG2 as a Mn(II) oxidase with pollutant removal
A 2024 Frontiers in Microbiology paper reports kinetic and operational parameters for recombinant **StKatG2** Mn(II) oxidation:
- **Km = 2.529 mM**, **Vmax = 10.07 μM·min⁻1**, **kcat = 2.82 min⁻1**. (ding2024catalaseperoxidasestkatg2from pages 3-4)
- Optimum conditions: **pH 7.5**, **55°C**; retains **45.1% activity after 8 h at 80°C**. (ding2024catalaseperoxidasestkatg2from pages 1-2, ding2024catalaseperoxidasestkatg2from pages 4-6)
- Chelation and metals modulate activity (e.g., EDTA suppresses; Fe3+ inhibits; low Cu2+/Mg2+/Zn2+ can enhance). (ding2024catalaseperoxidasestkatg2from pages 6-9)

The same enzyme system achieved **malachite green decolorization** of **73.38% (20 mg/L)** and **60.08% (50 mg/L)**. (ding2024catalaseperoxidasestkatg2from pages 1-2, ding2024catalaseperoxidasestkatg2from pages 6-9)

**Curation relevance:** Provides a well-quantified alternative enzymatic mechanism (peroxidase family) for Mn oxidation that can be curated as a separate subgraph/module, with explicit environmental and inhibitor edges. (ding2024catalaseperoxidasestkatg2from pages 1-2, ding2024catalaseperoxidasestkatg2from pages 6-9)

### 2.5 2024 fungal Mn oxidation: localized Mn oxide nodules on hyphae and candidate laccases
A 2024 Microbes and Environments study isolated a Mn(II)-oxidizing fungus (*Periconia* sp. TS-2) that forms discrete Mn oxide nodules on hyphae and contains multiple predicted laccase/multicopper oxidase genes.

Quantitative data:
- Dissolved Mn(II) decreased to **~58% of initial after 10 days**. (tsushima2024formationofbiogenic pages 3-5)
- TS-2 BMOs enabled Cu(II) removal (50 μM initial) to **~57% of initial after 14 days**, with co-localization of Mn and Cu in precipitates. (tsushima2024formationofbiogenic pages 3-5)

**Curation relevance:** Expands trait taxonomic scope beyond bacteria and supports localization nodes (hyphal surface) and downstream heavy-metal immobilization edges, but gene-to-function remains candidate-level. (tsushima2024formationofbiogenic pages 3-5)

## 3) Current Applications and Real-World Implementations

### 3.1 Drinking-water manganese control via biofiltration (pilot-scale surface water)
A 2023 Scientific Reports study demonstrated raw-water biofiltration (anthracite/sand columns) for manganese control without conventional pre-treatments, emphasizing aeration/DO as a performance driver.

Key performance statistics:
- Aerated-influent biofilters produced effluent dissolved Mn **<10 μg/L** while treating influent dissolved Mn **>120 μg/L**. (earle2023rawwaterbiofiltration pages 1-2)
- After destratification, influent dissolved Mn was **107 ± 58 μg/L**, and effluent concentrations appeared to approach a lower limit of **~6–10 μg/L**; aerated filters achieved **>80% Mn removal** after acclimation. (earle2023rawwaterbiofiltration pages 4-7, earle2023rawwaterbiofiltration pages 9-10)
- DO and effluent Mn were moderately negatively correlated (**ρ = −0.58**). (earle2023rawwaterbiofiltration pages 7-9)
- When ATP (biomass proxy) exceeded **300 ng tATP/cm³**, the probability of effluent Mn **<20 μg/L** was **0.75**. (earle2023rawwaterbiofiltration pages 7-9)

**Implementation note:** The authors argue biofiltration can outperform a permanganate-driven full-scale process under the tested conditions, suggesting operational relevance for sustainable Mn control. (earle2023rawwaterbiofiltration pages 1-2)

### 3.2 Biogenic Mn oxides as catalysts/oxidants for pollutant transformation
- **Enzyme-mediated Mn oxidation + pollutant removal:** StKatG2 couples Mn(II) oxidation/BioMnOx generation with malachite green decolorization (up to ~73%). (ding2024catalaseperoxidasestkatg2from pages 1-2)
- **BioMnOx as electrocatalyst:** Mnx-derived BioMnOx can show OER performance comparable to or better than synthetic birnessite under tested electrochemical conditions (e.g., lower overpotential at a given mass-normalized current). (fu2024biogenicmanganeseoxide pages 2-4)
- **Metal immobilization:** Fungal BMOs adsorbed/immobilized aqueous Cu(II) in co-precipitates. (tsushima2024formationofbiogenic pages 3-5)

## 4) Expert Opinions / Authoritative Analysis (Evidence-grounded)

### 4.1 Mechanistic consensus and divergence
Recent authoritative primary research supports that **multiple mechanistic solutions** exist for Mn(II) oxidation across microbes:
- Some systems use **MCOs** that couple one-electron steps to **O2 reduction** (Mnx complex). (novikova2024cryoemstructureof pages 1-2)
- Others employ **peroxidase-family enzymes** or require reactive oxygen species (peroxide/superoxide), consistent with the statement that some microbes require peroxide/superoxide whereas others can use O2 directly. (novikova2024cryoemstructureof pages 1-2, kurdi2023aninsilicostudy pages 24-30)

From a TraitMech perspective, this argues for modeling manganese oxidation as a *trait class with mechanistic subclasses/modules* rather than a single universal gene. (jones2024isolationcharacterizationand pages 1-2, novikova2024cryoemstructureof pages 1-2)

### 4.2 Structure-guided mechanistic inference is now possible
The 2024 cryo-EM structure enables explicit causal modeling from **protein architecture → intermediate stabilization/translocation → oxide nanoparticle formation**, with specific hypothesized intermediate species. (novikova2024cryoemstructureof pages 7-8, novikova2024cryoemstructureof pages 1-2)

### 4.3 Systems-level implementation relies on environmental control
Biofilter data indicate **dissolved oxygen availability** and **biofilm accumulation** are operationally important for manganese removal, consistent with a causal edge **aeration → increased DO → improved Mn removal**. (earle2023rawwaterbiofiltration pages 7-9, earle2023rawwaterbiofiltration pages 2-3)

## 5) Candidate Nodes (Grouped by Type) for `manganese_oxidation.yaml`

The table below is a curation-oriented node inventory grounded in the retrieved evidence.

| Node label | Node type | Suggested ontology CURIE(s) | Notes/justification |
|---|---|---|---|
| manganese oxidation | process | GO:0016702 | Core trait process: Mn(II) to Mn(III/IV) oxides (novikova2024cryoemstructureof pages 1-2) |
| biomineralization of manganese oxide | process | GO:0110142 | Product-forming biomineralization step (novikova2024cryoemstructureof pages 7-8, novikova2024cryoemstructureof pages 1-2) |
| biogenic manganese oxide (BioMnOx) | chemical | CHEBI:25517 | Insoluble product of microbial Mn oxidation (ding2024catalaseperoxidasestkatg2from pages 1-2, fu2024biogenicmanganeseoxide pages 1-2) |
| birnessite / vernadite-like Mn oxide | chemical |  | Common poorly crystalline Mn oxide product (tsushima2024formationofbiogenic pages 3-5, fu2024biogenicmanganeseoxide pages 4-6) |
| Mn(II) | chemical | CHEBI:29035 | Soluble substrate for oxidation (ding2024catalaseperoxidasestkatg2from pages 3-4, novikova2024cryoemstructureof pages 1-2) |
| Mn(III) surface species | chemical | CHEBI:29036 | Proposed intermediate/active surface state (fu2024biogenicmanganeseoxide pages 4-6, fu2024biogenicmanganeseoxide pages 6-8) |
| Mn(IV) oxide / MnO2 | chemical | CHEBI:46719 | Final oxidized mineral product (novikova2024cryoemstructureof pages 7-8, novikova2024cryoemstructureof pages 1-2) |
| O2 | chemical | CHEBI:15379 | Direct oxidant for MCO-mediated systems (novikova2024cryoemstructureof pages 1-2) |
| H2O2 | chemical | CHEBI:16240 | Cofactor/oxidant in peroxidase-linked assays (ding2024catalaseperoxidasestkatg2from pages 2-3, ding2024catalaseperoxidasestkatg2from pages 9-11) |
| NADH | chemical | CHEBI:16908 | Included in StKatG2 assay buffer (ding2024catalaseperoxidasestkatg2from pages 2-3) |
| heme | chemical | CHEBI:30413 | Required cofactor for heme peroxidase activity (kurdi2023aninsilicostudy pages 30-33, ding2024catalaseperoxidasestkatg2from pages 2-3) |
| pyrophosphate-chelated Mn(III) | chemical | CHEBI:18361 | Used to detect accessible Mn(III) species (fu2024biogenicmanganeseoxide pages 6-8) |
| MnxG | gene/protein |  | Canonical Mn-oxidizing multicopper oxidase (jones2024isolationcharacterizationand pages 1-2, novikova2024cryoemstructureof pages 1-2) |
| McoA | gene/protein |  | Pseudomonas multicopper oxidase linked to Mn oxidation (jones2024isolationcharacterizationand pages 1-2, kurdi2023aninsilicostudy pages 1-6) |
| MopA | gene/protein |  | Animal heme peroxidase-family Mn oxidase (jones2024isolationcharacterizationand pages 1-2, kurdi2023aninsilicostudy pages 9-12) |
| StKatG2 | gene/protein |  | Catalase-peroxidase with Mn(II)-oxidizing activity (ding2024catalaseperoxidasestkatg2from pages 1-2, ding2024catalaseperoxidasestkatg2from pages 6-9) |
| fungal laccase / multicopper oxidase | gene/protein | GO:0005507 | Candidate fungal Mn oxidases in Periconia TS-2 (tsushima2024formationofbiogenic pages 3-5) |
| MnxE | gene/protein |  | Accessory subunit of Bacillus Mnx complex (novikova2024cryoemstructureof pages 1-2) |
| MnxF | gene/protein |  | Accessory subunit of Bacillus Mnx complex (novikova2024cryoemstructureof pages 1-2) |
| MnxR | gene/protein |  | σ54-dependent regulator linked to Mn oxidation genes (jones2024isolationcharacterizationand pages 1-2) |
| MnxS1 | gene/protein |  | Sensor kinase in Mn oxidation regulatory system (jones2024isolationcharacterizationand pages 1-2) |
| MnxS2 | gene/protein |  | Sensor kinase in Mn oxidation regulatory system (jones2024isolationcharacterizationand pages 1-2) |
| FleQ | gene/protein |  | Lifestyle regulator affecting oxidation state/biofilm context (jones2024isolationcharacterizationand pages 1-2) |
| Mnx complex (MnxE3F3G) | enzyme complex |  | Structural Mn oxidase complex with tunnel architecture (novikova2024cryoemstructureof pages 1-2) |
| multicopper oxidase activity | process | GO:0005507 | Enzymatic function class repeatedly implicated (kurdi2023aninsilicostudy pages 30-33, novikova2024cryoemstructureof pages 1-2) |
| heme peroxidase activity | process | GO:0004497 | Alternative enzymatic mechanism for Mn oxidation (kurdi2023aninsilicostudy pages 30-33, ding2024catalaseperoxidasestkatg2from pages 1-2) |
| two-electron Mn oxidation | process |  | Full Mn(II) to Mn(IV) oxidation by Mnx system (kurdi2023aninsilicostudy pages 9-12, novikova2024cryoemstructureof pages 7-8) |
| dissolved oxygen availability | environmental factor | ENVO:3100031 | Higher DO improves biofilter Mn removal (earle2023rawwaterbiofiltration pages 7-9, earle2023rawwaterbiofiltration pages 4-7) |
| aeration | environmental factor |  | Experimental factor increasing DO and Mn removal (earle2023rawwaterbiofiltration pages 7-9, earle2023rawwaterbiofiltration pages 1-2) |
| low temperature (4°C growth/oxidation) | environmental factor |  | Cold-tolerant Mn oxidation in novel Pseudomonas strains (jones2024isolationcharacterizationand pages 1-2) |
| neutral to slightly alkaline pH | environmental factor |  | Favored StKatG2 activity around pH 7.5 (ding2024catalaseperoxidasestkatg2from pages 1-2, ding2024catalaseperoxidasestkatg2from pages 6-9) |
| high Mn(II) concentration | environmental factor |  | Substrate level shapes mineral morphology and assay behavior (ding2024catalaseperoxidasestkatg2from pages 3-4, fu2024biogenicmanganeseoxide pages 2-4) |
| iron(III) inhibition | environmental factor | CHEBI:18248 | Fe3+ inhibits StKatG2 Mn oxidation (ding2024catalaseperoxidasestkatg2from pages 6-9) |
| EDTA inhibition | environmental factor | CHEBI:42191 | Chelation suppresses StKatG2 activity (ding2024catalaseperoxidasestkatg2from pages 6-9) |
| ATP biomass signal | assay/measurement |  | Biofilter maturity/performance proxy for Mn removal (earle2023rawwaterbiofiltration pages 7-9, earle2023rawwaterbiofiltration pages 9-10) |
| LBB assay | assay/measurement |  | Colorimetric detection of Mn(III/IV) oxides (ding2024catalaseperoxidasestkatg2from pages 3-4, tsushima2024formationofbiogenic pages 3-5) |
| XPS Mn oxidation-state analysis | assay/measurement |  | Confirms mixed Mn valence in products (ding2024catalaseperoxidasestkatg2from pages 4-6, fu2024biogenicmanganeseoxide pages 4-6) |
| EPR Mn(III) detection | assay/measurement |  | Detects accessible surface Mn(III) species (fu2024biogenicmanganeseoxide pages 4-6, fu2024biogenicmanganeseoxide pages 6-8) |
| cryo-EM structure | assay/measurement |  | Revealed Mnx tunnel and subunit arrangement (novikova2024cryoemstructureof pages 1-2) |
| biofilter effluent dissolved Mn | assay/measurement |  | Operational phenotype readout in water treatment (earle2023rawwaterbiofiltration pages 1-2, earle2023rawwaterbiofiltration pages 4-7) |
| exosporium / spore coat | cellular location | GO:0042600 | Bacillus-associated localization of Mnx-generated MnOx (fu2024biogenicmanganeseoxide pages 1-2, kurdi2023aninsilicostudy pages 9-12) |
| hyphal surface | cellular location | GO:0042306 | Fungal Mn oxide nodules localized on hyphae (tsushima2024formationofbiogenic pages 3-5) |
| extracellular space | cellular location | GO:0005576 | Many Mn oxidases/products are extracellularly deployed (kurdi2023aninsilicostudy pages 30-33, tsushima2024formationofbiogenic pages 3-5) |
| Bacillus sp. PL-12 | organism/taxon | NCBITaxon: | Source of structurally resolved Mnx complex; exact taxon ID unclear (novikova2024cryoemstructureof pages 1-2) |
| Bacillus sp. SG-1 | organism/taxon | NCBITaxon: | Classical spore-associated Mn oxidizer (fu2024biogenicmanganeseoxide pages 1-2) |
| Pseudomonas putida GB-1 | organism/taxon | NCBITaxon: | Model bacterium with mnxG/mcoA/mopA system (jones2024isolationcharacterizationand pages 1-2, kurdi2023aninsilicostudy pages 1-6) |
| Pseudomonas sp. DSV-1 | organism/taxon | NCBITaxon: | Cold-tolerant Mn oxidizer with GB-1-like genes (jones2024isolationcharacterizationand pages 1-2) |
| Pseudomonas sp. MS-1 | organism/taxon | NCBITaxon: | Cold-tolerant Mn oxidizer with GB-1-like genes (jones2024isolationcharacterizationand pages 1-2) |
| Salinicola tamaricis F01 | organism/taxon | NCBITaxon: | Source of StKatG2 Mn oxidase (ding2024catalaseperoxidasestkatg2from pages 1-2) |
| Periconia sp. TS-2 | organism/taxon | NCBITaxon: | Fungal Mn oxidizer forming BMO nodules (tsushima2024formationofbiogenic pages 3-5) |
| biological activated carbon / granular biofilter community | organism/taxon | ENVO:01001871 | Real-world biofilm consortium implementing Mn removal (earle2023rawwaterbiofiltration pages 1-2, larasati2024productionofbirnessitetype pages 11-13) |


*Table: This table lists candidate nodes for a TraitMech-style causal graph of microbial manganese oxidation, grouped across molecular, process, chemical, environmental, assay, localization, and taxon levels. It highlights entities most directly supported by recent mechanistic and application-focused literature.*

## 6) Candidate Evidence-Backed Causal Edges (Triples) with Snippets and Notes

The table below proposes candidate edges spanning enzymatic mechanisms, intermediates, environmental factors, products, and applied outcomes.

| Subject node | Predicate (causal verb) | Object node | Evidence snippet (short quote) | Reference (DOI + URL + year) | Notes/uncertainty |
|---|---|---|---|---|---|
| Mnx complex (MnxE3F3G) | catalyzes | Mn(II) oxidation to Mn(IV) oxide | “Mnx can use O2 directly” and supports “successive binuclear Mn complexes in oxidation states II → III → IV en route to MnO2” (novikova2024cryoemstructureof pages 1-2) | 10.1021/jacs.3c06537; https://doi.org/10.1021/jacs.3c06537; 2024 | Strong mechanistic support from structure/mechanism paper. |
| O2 | enables | Mnx-mediated Mn(II) oxidation | “some microbes…use peroxide or superoxide as oxidants, but others can use O2 directly, via multicopper oxidase (MCO) enzymes” (novikova2024cryoemstructureof pages 1-2) | 10.1021/jacs.3c06537; https://doi.org/10.1021/jacs.3c06537; 2024 | Strong for Mnx/MCO systems; not universal for all Mn oxidases. |
| MnxG | is catalytic subunit of | Mnx complex | “The key enzyme is MnxG…isolated as a complex…with…MnxE and MnxF” and “MnxG multicopper oxidase enzyme capped by…MnxE and MnxF” (novikova2024cryoemstructureof pages 1-2) | 10.1021/jacs.3c06537; https://doi.org/10.1021/jacs.3c06537; 2024 | Strong structural support. |
| MnxE | forms accessory cap on | MnxG | “capped by a heterohexameric ring of alternating MnxE and MnxF subunits” (novikova2024cryoemstructureof pages 1-2) | 10.1021/jacs.3c06537; https://doi.org/10.1021/jacs.3c06537; 2024 | Strong structural support. |
| MnxF | forms accessory cap on | MnxG | “capped by a heterohexameric ring of alternating MnxE and MnxF subunits” (novikova2024cryoemstructureof pages 1-2) | 10.1021/jacs.3c06537; https://doi.org/10.1021/jacs.3c06537; 2024 | Strong structural support. |
| MnxG tunnel entrance residues | bind/co-ordinate | Mn(II) substrate | “identifies likely coordinating groups for the Mn(II) substrate, at the entrance to the tunnel” (novikova2024cryoemstructureof pages 1-2) | 10.1021/jacs.3c06537; https://doi.org/10.1021/jacs.3c06537; 2024 | Mechanistic inference from structural comparison; curate with moderate confidence. |
| Mn(II) oxidation | produces | Mn(III)(OH)Mn(III) intermediate | “a cooperative two-electron step producing a Mn(III)(OH)Mn(III) intermediate” (novikova2024cryoemstructureof pages 7-8) | 10.1021/jacs.3c06537; https://doi.org/10.1021/jacs.3c06537; 2024 | Strong mechanistic hypothesis from cryo-EM model; still intermediate-level inference. |
| Mn(III)(OH)Mn(III) intermediate | disproportionates to form | Mn(IV)(O)Mn(IV) | “disproportionation of two Mn(III)(OH)Mn(III) species to form Mn(IV)(O)Mn(IV)” (novikova2024cryoemstructureof pages 7-8) | 10.1021/jacs.3c06537; https://doi.org/10.1021/jacs.3c06537; 2024 | Mechanistic model; good but inferred rather than directly observed in vivo. |
| Mn(IV)(O)Mn(IV) | condenses into | MnO2 nanoparticles | “Mn(IV)(O)Mn(IV) is…en route to MnO2” and “release of MnO2 nanoparticles” (novikova2024cryoemstructureof pages 7-8) | 10.1021/jacs.3c06537; https://doi.org/10.1021/jacs.3c06537; 2024 | Mechanistic model; nanoparticle release is hypothesized. |
| Mnx complex | biomineralizes | biogenic MnOx | “Biogenic MnOx materials were produced by aerobic oxidation of Mn2+ by the Mnx complex” (fu2024biogenicmanganeseoxide pages 6-8) | 10.1021/acscatal.3c06119; https://doi.org/10.1021/acscatal.3c06119; 2024 | Strong experimental support. |
| High Mn(II)/Mnx ratio and mineralization time | shape | MnOx morphology/mineral phase | “progression of morphologies depending on Mn(II)/Mnx ratio and mineralization time” (fu2024biogenicmanganeseoxide pages 2-4) | 10.1021/acscatal.3c06119; https://doi.org/10.1021/acscatal.3c06119; 2024 | Strong for in vitro biomineralization conditions. |
| Surface-accessible Mn(III) | correlates with | higher OER activity of BioMnOx | “surface-accessible Mn(III) correlates with OER activity” (fu2024biogenicmanganeseoxide pages 4-6) | 10.1021/acscatal.3c06119; https://doi.org/10.1021/acscatal.3c06119; 2024 | Correlative, not definitive causation. |
| BioMnOx-II / BioMnOx-III | catalyze | oxygen evolution reaction | “show comparable (or higher) OER activity relative to synthetic monoclinic birnessite” (fu2024biogenicmanganeseoxide pages 4-6) | 10.1021/acscatal.3c06119; https://doi.org/10.1021/acscatal.3c06119; 2024 | Application/property edge; not part of core microbial physiology but relevant downstream product function. |
| biogenic MnOx on Bacillus spores | localizes to | exosporium / spore surface | “TEM showing biogenic MnOx formed on the exosporium of Bacillus sp. SG-1 spores” (fu2024biogenicmanganeseoxide pages 1-2) | 10.1021/acscatal.3c06119; https://doi.org/10.1021/acscatal.3c06119; 2024 | Taxon-specific localization. |
| Pseudomonas putida GB-1 mnxG | contributes to | Mn oxidation | “three Mn oxidase genes are implicated: two multi-copper oxidases (mnxG and mcoA) and an animal heme peroxidase (MopA)” (jones2024isolationcharacterizationand pages 1-2) | 10.1128/aem.00510-24; https://doi.org/10.1128/aem.00510-24; 2024 | Strong for GB-1 and close relatives; gene-level contribution, not single-enzyme sufficiency. |
| Pseudomonas putida GB-1 mcoA | contributes to | Mn oxidation | “three Mn oxidase genes are implicated: two multi-copper oxidases (mnxG and mcoA)” (jones2024isolationcharacterizationand pages 1-2) | 10.1128/aem.00510-24; https://doi.org/10.1128/aem.00510-24; 2024 | Strong for GB-1 and relatives. |
| Pseudomonas putida GB-1 MopA | contributes to | Mn oxidation | “three Mn oxidase genes are implicated… and an animal heme peroxidase (MopA)” (jones2024isolationcharacterizationand pages 1-2) | 10.1128/aem.00510-24; https://doi.org/10.1128/aem.00510-24; 2024 | Strong in GB-1 context; enzyme family diversity warning. |
| MnxS1/MnxS2/MnxR regulatory system | regulates | Mn oxidation in Pseudomonas | “Mn oxidation in GB-1 requires a two-component regulatory system (sensor kinases MnxS1 and MnxS2 and σ54-dependent regulator MnxR)” (jones2024isolationcharacterizationand pages 1-2) | 10.1128/aem.00510-24; https://doi.org/10.1128/aem.00510-24; 2024 | Strong, but presently taxon/system specific. |
| Pseudomonas sp. DSV-1 and MS-1 homologs of mnxG/mcoA/mnxS1/mnxS2/mnxR | support | cold-tolerant Mn oxidation | “contain homologs… and oxidize Mn down to 4°C” (jones2024isolationcharacterizationand pages 1-2) | 10.1128/aem.00510-24; https://doi.org/10.1128/aem.00510-24; 2024 | Moderate; homolog presence plus phenotype, but direct gene knockout evidence not shown here. |
| StKatG2 catalase-peroxidase | catalyzes | Mn(II) oxidation | “StKatG2…shows measurable Mn(II)-oxidizing enzymatic activity” (ding2024catalaseperoxidasestkatg2from pages 1-2) | 10.3389/fmicb.2024.1478305; https://doi.org/10.3389/fmicb.2024.1478305; 2024 | Strong biochemical support; likely taxon/enzyme specific. |
| Neutral/slightly alkaline pH (~7.5) | increases | StKatG2 Mn(II)-oxidizing activity | “Optimal catalytic conditions were pH 7.5” (ding2024catalaseperoxidasestkatg2from pages 1-2) | 10.3389/fmicb.2024.1478305; https://doi.org/10.3389/fmicb.2024.1478305; 2024 | Assay-specific enzyme edge. |
| Elevated temperature (55°C optimum) | increases | StKatG2 Mn(II)-oxidizing activity | “optimal catalytic conditions were…55°C” (ding2024catalaseperoxidasestkatg2from pages 1-2) | 10.3389/fmicb.2024.1478305; https://doi.org/10.3389/fmicb.2024.1478305; 2024 | Assay-specific; not generalizable to all Mn oxidizers. |
| EDTA | inhibits | StKatG2 Mn(II)-oxidizing activity | “EDTA significantly suppresses Mn(II)-oxidizing activity” (ding2024catalaseperoxidasestkatg2from pages 6-9) | 10.3389/fmicb.2024.1478305; https://doi.org/10.3389/fmicb.2024.1478305; 2024 | Strong assay-specific inhibition edge. |
| Fe3+ | inhibits | StKatG2 Mn(II)-oxidizing activity | “Fe3+ (0.1 mM) inhibits activity” (ding2024catalaseperoxidasestkatg2from pages 6-9) | 10.3389/fmicb.2024.1478305; https://doi.org/10.3389/fmicb.2024.1478305; 2024 | Assay-specific inhibition edge. |
| Low Cu2+/Mg2+/Zn2+ | enhances | StKatG2 Mn(II)-oxidizing activity | “low-level Cu2+, Mg2+, Zn2+…enhance activity” (ding2024catalaseperoxidasestkatg2from pages 6-9) | 10.3389/fmicb.2024.1478305; https://doi.org/10.3389/fmicb.2024.1478305; 2024 | Assay-specific modulation. |
| High Cu2+/Zn2+ | inhibits | StKatG2 Mn(II)-oxidizing activity | “high concentrations…nearly abolish activity” (ding2024catalaseperoxidasestkatg2from pages 6-9) | 10.3389/fmicb.2024.1478305; https://doi.org/10.3389/fmicb.2024.1478305; 2024 | Assay-specific modulation. |
| StKatG2 Mn oxidation | produces | mixed-valence biogenic Mn oxides | “display mixed-valence manganese species (Mn(II), Mn(III), Mn(IV), Mn(VII))” (ding2024catalaseperoxidasestkatg2from pages 1-2) | 10.3389/fmicb.2024.1478305; https://doi.org/10.3389/fmicb.2024.1478305; 2024 | Strong product characterization. |
| StKatG2-generated BioMnOx/peroxidase system | decolorizes | malachite green | “achieving 73.38% decolorization for 20 mg/L MG and 60.08% for 50 mg/L MG” (ding2024catalaseperoxidasestkatg2from pages 1-2) | 10.3389/fmicb.2024.1478305; https://doi.org/10.3389/fmicb.2024.1478305; 2024 | Application edge; pollutant removal is enzyme-system specific. |
| Periconia sp. TS-2 | oxidizes | dissolved Mn(II) | “strain TS-2…was confirmed to oxidize dissolved Mn(II)” (tsushima2024formationofbiogenic pages 3-5) | 10.1264/jsme2.me23102; https://doi.org/10.1264/jsme2.me23102; 2024 | Strong phenotype support, fungal rather than bacterial. |
| Periconia sp. TS-2 Mn oxidation | forms | biogenic Mn oxide nodules on hyphae | “form discrete biogenic Mn oxide (BMO) nodules…localized on hyphae” (tsushima2024formationofbiogenic pages 3-5) | 10.1264/jsme2.me23102; https://doi.org/10.1264/jsme2.me23102; 2024 | Strong localization/product support. |
| Fungal laccase/multicopper oxidase genes | may mediate | Mn(II) oxidation in TS-2 | “14 putative laccase/multicopper oxidase…genes, implicating…candidate Mn(II)-oxidizing enzymes” (tsushima2024formationofbiogenic pages 3-5) | 10.1264/jsme2.me23102; https://doi.org/10.1264/jsme2.me23102; 2024 | Uncertain/inferred; candidate genes only. |
| TS-2-produced BMOs | adsorb/immobilize | Cu(II) | “BMOs…enabled Cu(II) removal…to ~57% of initial” (tsushima2024formationofbiogenic pages 3-5) | 10.1264/jsme2.me23102; https://doi.org/10.1264/jsme2.me23102; 2024 | Strong downstream product-function edge. |
| Dissolved oxygen availability | increases | biofilter Mn removal | “DO and effluent Mn were moderately negatively correlated (ρ = −0.58)” and aeration improved removal (earle2023rawwaterbiofiltration pages 7-9) | 10.1038/s41598-023-36348-1; https://doi.org/10.1038/s41598-023-36348-1; 2023 | Strong real-world application support. |
| Aeration | increases | dissolved oxygen availability | “Aeration of influent…achieving near-saturation DO” (earle2023rawwaterbiofiltration pages 2-3) | 10.1038/s41598-023-36348-1; https://doi.org/10.1038/s41598-023-36348-1; 2023 | Operational edge in water-treatment systems. |
| Aeration | improves | biological dissolved Mn removal in biofilters | “aeration…produced significantly lower effluent Mn” and filters “approach complete removal” (earle2023rawwaterbiofiltration pages 7-9) | 10.1038/s41598-023-36348-1; https://doi.org/10.1038/s41598-023-36348-1; 2023 | Strong application edge. |
| Biofilm biomass (ATP) | associates with increased | Mn removal performance | “when ATP >300 ng… probability of effluent Mn <20 µg/L was 0.75” (earle2023rawwaterbiofiltration pages 7-9) | 10.1038/s41598-023-36348-1; https://doi.org/10.1038/s41598-023-36348-1; 2023 | Correlative, not direct causation. |
| Manganese-oxide-containing biofilms | adsorb and catalyze oxidation of | dissolved Mn | “manganese-oxides can adsorb and catalyze oxidation of dissolved manganese” (earle2023rawwaterbiofiltration pages 9-10) | 10.1038/s41598-023-36348-1; https://doi.org/10.1038/s41598-023-36348-1; 2023 | Strong process/product-function edge in filters. |
| Biological raw-water biofiltration | removes | dissolved Mn to <10 µg/L effluent | “aerated-influent biofilters produced effluent Mn <10 µg/L while treating influent dissolved Mn >120 µg/L” (earle2023rawwaterbiofiltration pages 1-2) | 10.1038/s41598-023-36348-1; https://doi.org/10.1038/s41598-023-36348-1; 2023 | Application outcome; system-level rather than single-organism mechanism. |
| Multicopper oxidases / heme peroxidases | accelerate | Mn oxidation relative to abiotic rates | “Biological oxidation accelerates Mn oxidation rates up to ~5 orders of magnitude versus abiotic processes” (kurdi2023aninsilicostudy pages 1-6) | 10.21203/rs.3.rs-2451893/v1; https://doi.org/10.21203/rs.3.rs-2451893/v1; 2023 | Useful broad edge, but preprint/review-like synthesis; mark uncertain for direct curation. |
| MopA heme peroxidase | performs one-electron oxidation of | Mn(II) to Mn(III) | “MopA performs a one-electron oxidation producing Mn3+” (kurdi2023aninsilicostudy pages 9-12) | 10.21203/rs.3.rs-2451893/v1; https://doi.org/10.21203/rs.3.rs-2451893/v1; 2023 | Mechanistic but from preprint synthesis; curate cautiously. |
| Extracellular heme peroxidases | can mediate | Mn oxidation via superoxide | “extracellular haem peroxidases can mediate oxidation via superoxide” (kurdi2023aninsilicostudy pages 24-30) | 10.21203/rs.3.rs-2451893/v1; https://doi.org/10.21203/rs.3.rs-2451893/v1; 2023 | Uncertain/generalized from compiled literature; preprint context. |


*Table: This table lists evidence-backed subject–predicate–object edges for a TraitMech-style causal graph of microbial manganese oxidation. It spans core enzymatic mechanisms, environmental controls, biomineral products, and practical outcomes in bioremediation and drinking-water biofiltration.*

## 7) Ontology Grounding Notes

- **CHEBI grounding** is straightforward for core chemicals (O2, H2O2, Mn(II), MnO2, heme, NADH), and is included where confident. (ding2024catalaseperoxidasestkatg2from pages 1-2, novikova2024cryoemstructureof pages 1-2)
- **GO grounding** is reliable for broad processes/localizations (extracellular space, hyphal surface, spore coat/exosporium, biomineralization), but specific Mn-oxidation GO terms may not perfectly align with the microbial biomineralization context; treat GO mappings as “best-effort” labels. (tsushima2024formationofbiogenic pages 3-5, fu2024biogenicmanganeseoxide pages 1-2)
- **NCBITaxon IDs** for some strains (e.g., Bacillus sp. PL-12) were not explicit in the extracted text; these should be resolved during curation from the full paper/supplement. (novikova2024cryoemstructureof pages 1-2)

## 8) Warnings: Claims That Should Not Yet Be Curated (or Should Be Marked Uncertain)

1. **Preprint / synthesis risk:** The in-silico distribution study (Research Square) includes broad mechanistic assertions (e.g., relative acceleration magnitude; superoxide/peroxidase generalizations) that are useful for hypothesis generation but should be curated with an “uncertain/inferred” flag unless corroborated by primary biochemical genetics in the target taxa. (kurdi2023aninsilicostudy pages 1-6, kurdi2023aninsilicostudy pages 24-30)
2. **Candidate genes without functional validation:** Fungal TS-2 laccase/multicopper oxidase genes are “predicted” and “potentially responsible” but not experimentally knocked out/validated; gene→trait edges should be uncertain. (tsushima2024formationofbiogenic pages 3-5)
3. **Mechanistic intermediates are model-derived:** The Mn(III)(OH)Mn(III) and Mn(IV)(O)Mn(IV) steps and nanoparticle release are strongly motivated by structure/electrostatics but still mechanistic hypotheses; curate intermediate nodes with a “mechanistic model” provenance. (novikova2024cryoemstructureof pages 7-8)
4. **Application edges vs core trait:** OER performance and dye decolorization are downstream properties of BioMnOx/enzyme systems; include them as application subgraphs, not as defining edges of the trait itself. (fu2024biogenicmanganeseoxide pages 2-4, ding2024catalaseperoxidasestkatg2from pages 1-2)

## 9) DOI-first Bibliography (with URLs and publication dates)

1. **Novikova IV, Soldatova AV, et al.** *Cryo-EM Structure of the Mnx Protein Complex Reveals a Tunnel Framework for the Mechanism of Manganese Biomineralization.* **Journal of the American Chemical Society**. **2024-07**. DOI: **10.1021/jacs.3c06537**. URL: https://doi.org/10.1021/jacs.3c06537 (novikova2024cryoemstructureof pages 1-2, novikova2024cryoemstructureof pages 7-8)
2. **Fu W, Hyler FP, et al.** *Biogenic Manganese Oxide Synthesized by a Marine Bacterial Multicopper Oxidase MnxG Reveals Oxygen Evolution Activity.* **ACS Catalysis**. **2024-04**. DOI: **10.1021/acscatal.3c06119**. URL: https://doi.org/10.1021/acscatal.3c06119 (fu2024biogenicmanganeseoxide pages 2-4, fu2024biogenicmanganeseoxide pages 4-6)
3. **Jones I, Vermillion D, et al.** *Isolation, characterization, and genetic manipulation of cold-tolerant, manganese-oxidizing Pseudomonas sp. strains.* **Applied and Environmental Microbiology**. **2024-09**. DOI: **10.1128/aem.00510-24**. URL: https://doi.org/10.1128/aem.00510-24 (jones2024isolationcharacterizationand pages 1-2)
4. **Ding M, Wang W, et al.** *Catalase-peroxidase StKatG2 from Salinicola tamaricis: a versatile Mn(II) oxidase that decolorizes malachite green.* **Frontiers in Microbiology**. **2024-11**. DOI: **10.3389/fmicb.2024.1478305**. URL: https://doi.org/10.3389/fmicb.2024.1478305 (ding2024catalaseperoxidasestkatg2from pages 1-2, ding2024catalaseperoxidasestkatg2from pages 3-4)
5. **Tsushima S, Nishi Y, et al.** *Formation of Biogenic Manganese Oxide Nodules on Hyphae of a New Fungal Isolate of Periconia That Immobilizes Aqueous Copper.* **Microbes and Environments**. **2024-06**. DOI: **10.1264/jsme2.me23102**. URL: https://doi.org/10.1264/jsme2.me23102 (tsushima2024formationofbiogenic pages 3-5)
6. **Earle MR, Stoddart AK, Gagnon GA.** *Raw water biofiltration for surface water manganese control.* **Scientific Reports**. **2023-06**. DOI: **10.1038/s41598-023-36348-1**. URL: https://doi.org/10.1038/s41598-023-36348-1 (earle2023rawwaterbiofiltration pages 1-2, earle2023rawwaterbiofiltration pages 7-9)
7. **Kurdi MZ, Olichney J, Geszvain K.** *An in-Silico Study of the Distribution of Mn Oxidation Proteins in Sequenced Bacterial Genomes.* **Research Square (preprint)**. **2023-01**. DOI: **10.21203/rs.3.rs-2451893/v1**. URL: https://doi.org/10.21203/rs.3.rs-2451893/v1 (kurdi2023aninsilicostudy pages 1-6, kurdi2023aninsilicostudy pages 9-12)


References

1. (novikova2024cryoemstructureof pages 1-2): Irina V. Novikova, Alexandra V. Soldatova, Trevor H. Moser, Stephanie M. Thibert, Christine A. Romano, Mowei Zhou, Bradley M. Tebo, James E. Evans, and Thomas G. Spiro. Cryo-em structure of the mnx protein complex reveals a tunnel framework for the mechanism of manganese biomineralization. Journal of the American Chemical Society, 146:22950-22958, Jul 2024. URL: https://doi.org/10.1021/jacs.3c06537, doi:10.1021/jacs.3c06537. This article has 7 citations and is from a highest quality peer-reviewed journal.

2. (ding2024catalaseperoxidasestkatg2from pages 1-2): Mengyao Ding, Wenjing Wang, Zhenkun Lu, Yuhui Sun, Xinzhen Qiao, Meixue Dai, and Guoyan Zhao. Catalase-peroxidase stkatg2 from salinicola tamaricis: a versatile mn(ii) oxidase that decolorizes malachite green. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1478305, doi:10.3389/fmicb.2024.1478305. This article has 2 citations and is from a peer-reviewed journal.

3. (tsushima2024formationofbiogenic pages 3-5): Shihori Tsushima, Yuma Nishi, Ryo Suzuki, Masaru Tachibana, Robert A. Kanaly, and Jiro F. Mori. Formation of biogenic manganese oxide nodules on hyphae of a new fungal isolate of periconia that immobilizes aqueous copper. Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23102, doi:10.1264/jsme2.me23102. This article has 4 citations and is from a peer-reviewed journal.

4. (earle2023rawwaterbiofiltration pages 1-2): Martin R. Earle, Amina K. Stoddart, and Graham A. Gagnon. Raw water biofiltration for surface water manganese control. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36348-1, doi:10.1038/s41598-023-36348-1. This article has 16 citations and is from a peer-reviewed journal.

5. (fu2024biogenicmanganeseoxide pages 4-6): Wen Fu, Forrest P. Hyler, Joel Sanchez, Thomas F. Jaramillo, Jesús M. Velázquez, Lizhi Tao, and R. David Britt. Biogenic manganese oxide synthesized by a marine bacterial multicopper oxidase mnxg reveals oxygen evolution activity. ACS Catalysis, 14:7232-7242, Apr 2024. URL: https://doi.org/10.1021/acscatal.3c06119, doi:10.1021/acscatal.3c06119. This article has 4 citations and is from a highest quality peer-reviewed journal.

6. (ding2024catalaseperoxidasestkatg2from pages 4-6): Mengyao Ding, Wenjing Wang, Zhenkun Lu, Yuhui Sun, Xinzhen Qiao, Meixue Dai, and Guoyan Zhao. Catalase-peroxidase stkatg2 from salinicola tamaricis: a versatile mn(ii) oxidase that decolorizes malachite green. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1478305, doi:10.3389/fmicb.2024.1478305. This article has 2 citations and is from a peer-reviewed journal.

7. (kurdi2023aninsilicostudy pages 24-30): M. Zakaria Kurdi, Jacob Olichney, and Kati Geszvain. An in-silico study of the distribution of mn oxidation proteins in sequenced bacterial genomes. Unknown journal, Jan 2023. URL: https://doi.org/10.21203/rs.3.rs-2451893/v1, doi:10.21203/rs.3.rs-2451893/v1.

8. (ding2024catalaseperoxidasestkatg2from pages 9-11): Mengyao Ding, Wenjing Wang, Zhenkun Lu, Yuhui Sun, Xinzhen Qiao, Meixue Dai, and Guoyan Zhao. Catalase-peroxidase stkatg2 from salinicola tamaricis: a versatile mn(ii) oxidase that decolorizes malachite green. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1478305, doi:10.3389/fmicb.2024.1478305. This article has 2 citations and is from a peer-reviewed journal.

9. (novikova2024cryoemstructureof pages 7-8): Irina V. Novikova, Alexandra V. Soldatova, Trevor H. Moser, Stephanie M. Thibert, Christine A. Romano, Mowei Zhou, Bradley M. Tebo, James E. Evans, and Thomas G. Spiro. Cryo-em structure of the mnx protein complex reveals a tunnel framework for the mechanism of manganese biomineralization. Journal of the American Chemical Society, 146:22950-22958, Jul 2024. URL: https://doi.org/10.1021/jacs.3c06537, doi:10.1021/jacs.3c06537. This article has 7 citations and is from a highest quality peer-reviewed journal.

10. (fu2024biogenicmanganeseoxide pages 2-4): Wen Fu, Forrest P. Hyler, Joel Sanchez, Thomas F. Jaramillo, Jesús M. Velázquez, Lizhi Tao, and R. David Britt. Biogenic manganese oxide synthesized by a marine bacterial multicopper oxidase mnxg reveals oxygen evolution activity. ACS Catalysis, 14:7232-7242, Apr 2024. URL: https://doi.org/10.1021/acscatal.3c06119, doi:10.1021/acscatal.3c06119. This article has 4 citations and is from a highest quality peer-reviewed journal.

11. (fu2024biogenicmanganeseoxide pages 6-8): Wen Fu, Forrest P. Hyler, Joel Sanchez, Thomas F. Jaramillo, Jesús M. Velázquez, Lizhi Tao, and R. David Britt. Biogenic manganese oxide synthesized by a marine bacterial multicopper oxidase mnxg reveals oxygen evolution activity. ACS Catalysis, 14:7232-7242, Apr 2024. URL: https://doi.org/10.1021/acscatal.3c06119, doi:10.1021/acscatal.3c06119. This article has 4 citations and is from a highest quality peer-reviewed journal.

12. (jones2024isolationcharacterizationand pages 1-2): Ian Jones, Duncan Vermillion, Chase Tracy, Robert Denton, Rick Davis, and Kati Geszvain. Isolation, characterization, and genetic manipulation of cold-tolerant, manganese-oxidizing <i>pseudomonas</i> sp. strains. Sep 2024. URL: https://doi.org/10.1128/aem.00510-24, doi:10.1128/aem.00510-24. This article has 4 citations and is from a peer-reviewed journal.

13. (ding2024catalaseperoxidasestkatg2from pages 3-4): Mengyao Ding, Wenjing Wang, Zhenkun Lu, Yuhui Sun, Xinzhen Qiao, Meixue Dai, and Guoyan Zhao. Catalase-peroxidase stkatg2 from salinicola tamaricis: a versatile mn(ii) oxidase that decolorizes malachite green. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1478305, doi:10.3389/fmicb.2024.1478305. This article has 2 citations and is from a peer-reviewed journal.

14. (ding2024catalaseperoxidasestkatg2from pages 6-9): Mengyao Ding, Wenjing Wang, Zhenkun Lu, Yuhui Sun, Xinzhen Qiao, Meixue Dai, and Guoyan Zhao. Catalase-peroxidase stkatg2 from salinicola tamaricis: a versatile mn(ii) oxidase that decolorizes malachite green. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1478305, doi:10.3389/fmicb.2024.1478305. This article has 2 citations and is from a peer-reviewed journal.

15. (earle2023rawwaterbiofiltration pages 4-7): Martin R. Earle, Amina K. Stoddart, and Graham A. Gagnon. Raw water biofiltration for surface water manganese control. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36348-1, doi:10.1038/s41598-023-36348-1. This article has 16 citations and is from a peer-reviewed journal.

16. (earle2023rawwaterbiofiltration pages 9-10): Martin R. Earle, Amina K. Stoddart, and Graham A. Gagnon. Raw water biofiltration for surface water manganese control. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36348-1, doi:10.1038/s41598-023-36348-1. This article has 16 citations and is from a peer-reviewed journal.

17. (earle2023rawwaterbiofiltration pages 7-9): Martin R. Earle, Amina K. Stoddart, and Graham A. Gagnon. Raw water biofiltration for surface water manganese control. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36348-1, doi:10.1038/s41598-023-36348-1. This article has 16 citations and is from a peer-reviewed journal.

18. (earle2023rawwaterbiofiltration pages 2-3): Martin R. Earle, Amina K. Stoddart, and Graham A. Gagnon. Raw water biofiltration for surface water manganese control. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36348-1, doi:10.1038/s41598-023-36348-1. This article has 16 citations and is from a peer-reviewed journal.

19. (fu2024biogenicmanganeseoxide pages 1-2): Wen Fu, Forrest P. Hyler, Joel Sanchez, Thomas F. Jaramillo, Jesús M. Velázquez, Lizhi Tao, and R. David Britt. Biogenic manganese oxide synthesized by a marine bacterial multicopper oxidase mnxg reveals oxygen evolution activity. ACS Catalysis, 14:7232-7242, Apr 2024. URL: https://doi.org/10.1021/acscatal.3c06119, doi:10.1021/acscatal.3c06119. This article has 4 citations and is from a highest quality peer-reviewed journal.

20. (ding2024catalaseperoxidasestkatg2from pages 2-3): Mengyao Ding, Wenjing Wang, Zhenkun Lu, Yuhui Sun, Xinzhen Qiao, Meixue Dai, and Guoyan Zhao. Catalase-peroxidase stkatg2 from salinicola tamaricis: a versatile mn(ii) oxidase that decolorizes malachite green. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1478305, doi:10.3389/fmicb.2024.1478305. This article has 2 citations and is from a peer-reviewed journal.

21. (kurdi2023aninsilicostudy pages 30-33): M. Zakaria Kurdi, Jacob Olichney, and Kati Geszvain. An in-silico study of the distribution of mn oxidation proteins in sequenced bacterial genomes. Unknown journal, Jan 2023. URL: https://doi.org/10.21203/rs.3.rs-2451893/v1, doi:10.21203/rs.3.rs-2451893/v1.

22. (kurdi2023aninsilicostudy pages 1-6): M. Zakaria Kurdi, Jacob Olichney, and Kati Geszvain. An in-silico study of the distribution of mn oxidation proteins in sequenced bacterial genomes. Unknown journal, Jan 2023. URL: https://doi.org/10.21203/rs.3.rs-2451893/v1, doi:10.21203/rs.3.rs-2451893/v1.

23. (kurdi2023aninsilicostudy pages 9-12): M. Zakaria Kurdi, Jacob Olichney, and Kati Geszvain. An in-silico study of the distribution of mn oxidation proteins in sequenced bacterial genomes. Unknown journal, Jan 2023. URL: https://doi.org/10.21203/rs.3.rs-2451893/v1, doi:10.21203/rs.3.rs-2451893/v1.

24. (larasati2024productionofbirnessitetype pages 11-13): Amanda Larasati, Olga Bernadet, Gert Jan W. Euverink, H. Pieter J. van Veelen, and Maria Cristina Gagliano. Production of birnessite-type manganese oxides by biofilms from oxygen-supplemented biological activated carbon (bac) filters. Environmental Science: Water Research &amp; Technology, 10:2844-2857, Jan 2024. URL: https://doi.org/10.1039/d4ew00208c, doi:10.1039/d4ew00208c. This article has 3 citations.