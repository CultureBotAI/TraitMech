---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:24:05.026064'
end_time: '2026-08-04T05:32:57.694520'
duration_seconds: 532.67
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Aerobic respiration
  trait_identifier: METPO:1000801
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: aerobic_respiration
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A respiration in which molecular oxygen serves as the terminal electron
    acceptor in the electron transport chain, generating ATP through oxidative phosphorylation
    with water as the final product.
  parent_traits: METPO:1000800
  synonyms: Oxic respiration, Oxygen respiration
  evidence_summary: 'DOI:10.1146/annurev.biophys.27.1.329: terminal enzyme of respiratory
    chains (Review supports cytochrome c oxidase reducing molecular oxygen to water
    in aerobic respiratory chains.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound
    electron transport chain (Review supports proton-gradient energy conservation
    by prokaryotic respiratory chains.)'
  causal_graph_summary: 'aerobic_respiration_terminal_oxidase: 8 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Aerobic respiration
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000801
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration in which molecular oxygen serves as the terminal electron acceptor in the electron transport chain, generating ATP through oxidative phosphorylation with water as the final product.
- **Parent traits:** METPO:1000800
- **Synonyms:** Oxic respiration, Oxygen respiration
- **Existing evidence:** DOI:10.1146/annurev.biophys.27.1.329: terminal enzyme of respiratory chains (Review supports cytochrome c oxidase reducing molecular oxygen to water in aerobic respiratory chains.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports proton-gradient energy conservation by prokaryotic respiratory chains.)
- **Existing causal graph summary:** aerobic_respiration_terminal_oxidase: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **Aerobic respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/aerobic_respiration.yaml`.

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
- **Trait label:** Aerobic respiration
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000801
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration in which molecular oxygen serves as the terminal electron acceptor in the electron transport chain, generating ATP through oxidative phosphorylation with water as the final product.
- **Parent traits:** METPO:1000800
- **Synonyms:** Oxic respiration, Oxygen respiration
- **Existing evidence:** DOI:10.1146/annurev.biophys.27.1.329: terminal enzyme of respiratory chains (Review supports cytochrome c oxidase reducing molecular oxygen to water in aerobic respiratory chains.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports proton-gradient energy conservation by prokaryotic respiratory chains.)
- **Existing causal graph summary:** aerobic_respiration_terminal_oxidase: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **Aerobic respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/aerobic_respiration.yaml`.

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


# Curation report: microbial aerobic respiration

## Executive recommendation

**Target:** `METPO:1000801` — Aerobic respiration  
**Category:** METABOLISM · **Kind:** CLASS · **Status:** REVIEWED  
**Parent:** `METPO:1000800`

The graph should represent an **organism-level capacity for membrane-associated respiratory electron transfer in which O₂ is the terminal electron acceptor, terminal oxidases reduce O₂ to H₂O, and the resulting electrochemical ion gradient supports ATP synthesis by oxidative phosphorylation**. The safest universal causal backbone is:

**reduced electron donor → respiratory dehydrogenase → quinone/quinol pool → terminal oxidase (directly, or through complex III and cytochrome c) → O₂ reduction to H₂O → proton-motive force → F₁F₀-ATP synthase → ATP.**

This definition does **not** require a particular donor, quinone, complex III, cytochrome c, terminal-oxidase family, oxygen optimum, or obligately aerobic lifestyle. Type-A heme–copper oxidases pump protons, whereas cytochrome bd contributes to proton-motive force through vectorial chemistry without being a proton pump; these mechanisms must not be collapsed into an assertion that every terminal oxidase pumps protons. (borisov2021bacterialoxidasesof pages 1-2, wikstrom2018oxygenactivationand pages 1-2, azarkina2023interactionofterminal pages 1-2, grauel2021structureofescherichia pages 1-2)

## 1. Trait scope and boundaries

### In scope

* **Phenotype/capacity:** measurable O₂-dependent respiratory electron transport coupled to energy conservation.
* **Common assays:** O₂ consumption/oxygen-consumption rate, donor-stimulated membrane respiration, growth with O₂ as terminal acceptor, respiratory-complex activity, proton-motive-force measurements, and ATP synthesis attributable to oxidative phosphorylation.
* **Environmental range:** fully oxic and microaerobic respiration. High-affinity cytochrome bd can reduce O₂ at submicromolar concentrations, so low-O₂ respiration remains aerobic respiration. (borisov2021bacterialoxidasesof pages 1-2)
* **Physiological modes:** heterotrophic, lithotrophic, mixotrophic, and non-growing maintenance respiration, provided electrons ultimately terminate at O₂. The 2024 *Cupriavidus necator* study illustrates donor flexibility: H₂ and formate oxidation can supply reducing equivalents, while terminal-complex utilization depends on the energy source. (jahn2024theenergymetabolism pages 1-2)
* **Alternative architectures:** quinol oxidases such as bo₃ and bd, and cytochrome-c oxidases such as aa₃, ba₃, cbb₃, or caa₃. In many bacteria, complex III transfers electrons through cytochrome c to complex IV; that route is common but not universal. (brzezinski2021structureandmechanism pages 1-2, wikstrom2018oxygenactivationand pages 1-2, azarkina2023interactionofterminal pages 1-2)

### Out of scope or requiring separate traits

1. **Oxygen tolerance alone.** Catalase, superoxide dismutase, ROS detoxification, or survival in air does not establish respiratory use of O₂.
2. **An arbitrary O₂-dependent enzyme.** A 2024 evolutionary analysis mapped **365 O₂-dependent prokaryotic reactions to 792 protein families** and concluded that many initially supported substrate oxidation or O₂-tolerant biosynthesis rather than energy conservation. Thus, “uses O₂” is not equivalent to aerobic respiration. (mrnjavac2024theradicalimpact pages 1-3)
3. **Oxygenic photosynthesis.** Production of O₂ by water splitting is distinct from consuming O₂ as a respiratory acceptor, although cyanobacteria may also respire.
4. **Anaerobic respiration.** Nitrate, fumarate, sulfate, or other acceptors do not instantiate this trait unless a separate branch demonstrably ends at O₂.
5. **Fermentation and substrate-level phosphorylation.** These may coexist with aerobic respiration but are not evidence for it.
6. **Aerobic growth inferred only from taxonomy or habitat.** Capability should be supported by physiology or a sufficiently complete functional respiratory module.
7. **Oxygen preference terminology.** “Obligate aerobe,” “facultative anaerobe,” “microaerophile,” and “aerotolerant” describe ecological or growth relationships to O₂; they are related but not synonymous with the biochemical capacity.

### Recommended operational evidence rule

Strong trait evidence should show at least one of: (i) O₂-dependent respiration or growth that is lost or reduced by perturbing respiratory components; (ii) donor-stimulated O₂ consumption in cells or membranes; or (iii) a complete, expressed terminal-oxidase pathway with mechanistic validation. A terminal-oxidase gene alone is weaker because respiratory chains are redundant, conditionally expressed, and sometimes used principally for stress protection.

## 2. Candidate nodes and ontology grounding

Identifiers below are deliberately conservative. Label-only nodes are preferable where a precise family, complex, or chemical CURIE has not been verified.

### Trait, pathways, and processes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| Aerobic respiration | `METPO:1000801`; `GO:0009060` | Target trait and closely corresponding GO process. Preserve the supplied METPO CURIE verbatim. |
| Electron transport chain | `GO:0022900` | General respiratory electron-transfer process. |
| Oxidative phosphorylation | `GO:0006119` | Energy-conserving coupling of electron transport to ATP synthesis. |
| ATP synthesis coupled electron transport | `GO:0042773` | Useful mechanistic process node. |
| Electron-transfer activity | `GO:0009055` | Broad molecular-function node; use specific oxidoreductase terms where possible. |
| Proton-motive force generation | label-only candidate | Represent as an electrochemical-gradient process rather than asserting proton pumping for every oxidase. |
| ATP synthesis coupled proton transport | `GO:0015986` | Appropriate downstream process. |

### Complexes, enzymes, and genes

| Candidate node | Suggested grounding | Representative genes/components | Scope |
|---|---|---|---|
| NADH dehydrogenase I / complex I | `GO:0008137` | `nuoA–N` | Proton-translocating entry module; not universal. |
| Type-II NADH dehydrogenase | label-only candidate | `ndh`/taxon-specific homologues | Oxidizes NADH and reduces quinone without proton pumping. |
| Na⁺-translocating NADH:quinone oxidoreductase | label-only candidate | `nqrA–F` | Ion specificity can be taxon-specific; *P. aeruginosa* NQR has been reported to function as a proton pump. (hu2024identificationofcomplex pages 1-3) |
| Succinate dehydrogenase / complex II | `GO:0000104` | `sdhABCD` or variants | Donor-entry module linking succinate oxidation to quinone reduction. |
| Cytochrome bc₁/bc complex | label-only candidate | `petABC`, `qcrABC`, taxon-specific | Transfers quinol-derived electrons toward cytochrome c; architecture varies. |
| Cytochrome c | label-only candidate | `cyc` genes | Mobile/peripheral electron carrier in one major branch. |
| Cytochrome-c oxidase activity | `GO:0004129` | aa₃/caa₃ and related HCO genes | Terminal O₂ reductase; family-specific subunits should be taxon grounded. |
| Cytochrome-o ubiquinol oxidase activity | `GO:0008137` is too broad; label-only preferred | `cyoABCDE` | bo₃-type quinol oxidase. |
| Cytochrome bd ubiquinol oxidase activity | `GO:0015002` | `cydAB` plus small subunits such as `cydX/cydH`, or `appCBX` | Direct quinol-to-O₂ route; no pumped protons. |
| F₁F₀ ATP synthase | `GO:0046933`; `EC:7.1.2.2` | commonly `atpIBEFHAGDC` or variants | Uses PMF for ATP synthesis; operon organization varies. |
| Respiratory chain complex | `GO:0098803` may be considered after ontology verification | — | Do not assign all proteins to a single canonical complex architecture. |

### Chemicals, gradients, and inhibitors

| Candidate node | Suggested grounding | Role |
|---|---|---|
| Dioxygen | `CHEBI:15379` | Defining terminal electron acceptor. |
| Water | `CHEBI:15377` | Product of complete four-electron O₂ reduction. |
| NADH | `CHEBI:16908` should be independently verified before YAML use | Reduced donor to NADH dehydrogenases. |
| Succinate | `CHEBI:15741` should be independently verified | Donor to succinate dehydrogenase. |
| Ubiquinone / ubiquinol | `CHEBI:16389` / `CHEBI:17976` should be independently verified | Membrane electron-carrier couple in many taxa. |
| Menaquinone / menaquinol | label-only until exact protonation-state CURIE is verified | Alternative quinone couple, especially in many Gram-positive bacteria and archaea. |
| Proton | `CHEBI:15378` should be independently verified | Gradient-forming ion. Some prokaryotic chains can use Na⁺-based coupling, so PMF should not be forced universally where data indicate otherwise. |
| ADP | `CHEBI:16761` | ATP-synthase substrate. |
| Phosphate | `CHEBI:43474` | ATP-synthase substrate. |
| ATP | `CHEBI:15422` | Energy-conserving product. |
| Cyanide | `CHEBI:17514` should be verified | Inhibitor of many heme–copper oxidases; sensitivity is oxidase- and taxon-dependent. |
| Nitric oxide | `CHEBI:16480` should be verified | Respiratory-oxidase inhibitor/stressor with reversible effects in some bd enzymes. |
| Hydrogen sulfide | `CHEBI:16136` should be verified | Inhibitor/stressor; CIO tolerance is conditional. |
| Aurachin D | label-only candidate | Structurally observed inhibitor of *E. coli* bd-II. |
| Q203/telacebec | label-only candidate | Mycobacterial cytochrome bcc–aa₃ inhibitor. |
| Bedaquiline | label-only candidate | Mycobacterial F₁F₀-ATP-synthase inhibitor. |
| Proton-motive force | label-only candidate | Composite membrane potential and proton-activity gradient. |

### Cellular locations and environmental factors

* **Bacterial cytoplasmic membrane** — principal energy-transducing membrane.
* **Archaeal cytoplasmic membrane** — relevant where archaeal terminal oxidases and A/V-type ATP synthases are modeled; do not force bacterial F₁F₀ architecture.
* **Periplasm/extracellular positive side** and **cytoplasm/negative side** — useful orientation nodes where topology is evidenced.
* **Dissolved oxygen concentration**, **oxic environment**, and **microoxic environment** — use ENVO terms only after exact identifier verification.
* **pH, growth phase, nutrient/energy source, inhibitors, and host-derived gases** — experimental or environmental modifiers, not constitutive components of the core trait.

## 3. Evidence-backed candidate edges

The following artifact provides compact triples, source snippets, and confidence qualifications.

| subject | predicate | object | scope/confidence | best DOI evidence |
|---|---|---|---|---|
| NADH dehydrogenase / succinate dehydrogenase | transfers electrons to / reduces | quinone pool (ubiquinone or menaquinone) | Core respiratory architecture, but donor modules and quinone identity vary by taxon; high confidence for bacteria broadly | *P. aeruginosa* has dehydrogenases that “catalyze electron transfer from NADH to ubiquinone” and “Succinate dehydrogenase… provide electrons to the respiratory chain” (10.3389/fmicb.2024.1347466) (hu2024identificationofcomplex pages 1-3); *B. licheniformis* NDH-2 “catalyze[s] the oxidation of NADH and the reduction of quinone” and SDH “catalyzes the two-electron reduction of quinone by succinate” (10.1007/s10863-024-10041-y) (uriberamirez2024modificationsofthe pages 1-2) |
| quinol | donates electrons to | bd-type terminal oxidase | Core for bd-family oxidases; high confidence, family-specific | Cytochrome bd is a “ubiquinol:oxygen oxidoreductase” and “catalyzes the reduction of O2 to H2O… using quinols as physiological reducing substrates” (10.1089/ars.2020.8039) (borisov2021bacterialoxidasesof pages 1-2) |
| quinol | donates electrons to | bo3 heme-copper quinol oxidase | Core for quinol-oxidizing HCOs, not universal across all HCOs; high confidence, family-specific | A-type oxidases include “some quinol oxidases, notably cytochrome bo3 of *Escherichia coli*” (10.1021/acs.chemrev.7b00664) (wikstrom2018oxygenactivationand pages 1-2) |
| complex III (bc1 / bc) | transfers electrons via | cytochrome c | Common in many bacteria, but absent from some branches; moderate confidence for universal graph, high for bc1-containing taxa | In many bacteria, cytochrome c oxidase “receives electrons from cytochrome bc1 (complex III), via membrane-bound or water-soluble cytochrome c” (10.1021/acs.chemrev.1c00140) (brzezinski2021structureandmechanism pages 1-2); *B. licheniformis* “cytochrome bc complex donates electrons from quinol to cytochrome caa3. The two small cytochromes c… facilitate the transfer of electrons” (10.1007/s10863-024-10041-y) (uriberamirez2024modificationsofthe pages 1-2) |
| cytochrome c | donates electrons to | heme-copper terminal oxidase (cytochrome c oxidase) | Common HCO route; high confidence for cytochrome-c oxidases, not for bd oxidases | Cytochrome c oxidase catalyzes dioxygen reduction; overall reaction given as “4 ferrocytochrome c + 4H+ + O2 → 2H2O + 4 ferricytochrome c” (10.1021/acs.chemrev.7b00664) (wikstrom2018oxygenactivationand pages 1-2) |
| terminal oxidase (heme-copper oxidase or bd oxidase) | reduces | O2 to H2O | Defining core of aerobic respiration; very high confidence | CcO “catalyzes the respiratory reduction of dioxygen (O2) to water” (10.1021/acs.chemrev.7b00664) (wikstrom2018oxygenactivationand pages 1-2); cytochrome bd couples “reduction of molecular oxygen… to water” (10.1089/ars.2020.8039) (borisov2021bacterialoxidasesof pages 1-2) |
| heme-copper terminal oxidase | contributes to generation of | proton motive force | Core for HCO-mediated aerobic respiration; very high confidence | CcO “couples the O2 reduction chemistry to translocation of protons across the membrane, thus contributing to generation of the electrochemical proton gradient” (10.1021/acs.chemrev.7b00664) (wikstrom2018oxygenactivationand pages 1-2); terminal oxidase transfers electrons from cytochrome c or quinol to oxygen and this “is coupled to the generation of a proton motive force” (10.3390/ijms24076428) (azarkina2023interactionofterminal pages 1-2) |
| bd-type terminal oxidase | contributes to generation of | proton motive force by vectorial charge transfer (not proton pumping) | Core for bd-family oxidases; high confidence, mechanism-specific | bd oxidases “contribute to the generation of a protonmotive force (pmf) by a vectorial charge transfer” (10.1038/s41467-021-26835-2) (grauel2021structureofescherichia pages 1-2); cytochrome bd reaction is “not associated with a proton pumping activity” (10.1089/ars.2020.8039) (borisov2021bacterialoxidasesof pages 1-2) |
| proton motive force | drives | F1Fo-ATP synthase ATP synthesis from ADP + Pi | Core oxidative phosphorylation step; very high confidence | F1Fo couples “ATP synthesis from ADP and phosphate… to a transmembrane electrochemical gradient of protons, known as the proton motive force (pmf)” and “ADP + Pi + pmf ↔ ATP + H2O” (10.3390/ijms24065417) (zharova2023f1·foatpsynthaseatpase pages 1-2) |
| oxygen level (4.2% O2) | increases abundance of | cytochrome aa3 oxidase in *Caldalkalibacillus thermarum* | Taxon- and chemostat-specific; high confidence within assay | “The cytochrome c:oxygen aa3 oxidase… abundance was highest at 4.2% O2” (10.3389/fmicb.2024.1468929) (jong2024quantitativeproteomicsreveals pages 1-2) |
| lower oxygen level (<0.42% O2) | decreases abundance of | cytochrome ba3 oxidase in *Caldalkalibacillus thermarum* | Taxon- and chemostat-specific; high confidence within assay | “The cytochrome c:oxygen ba3 oxidase was more abundant at most other O2 levels, but its abundance started to decline below 0.42% O2” (10.3389/fmicb.2024.1468929) (jong2024quantitativeproteomicsreveals pages 1-2) |
| H2S | does not inhibit / leaves unaltered | Pseudomonas CIO (bd-type cyanide-insensitive oxidase) O2 consumption | Taxon- and assay-specific; high confidence within study; should be curated as conditional tolerance, not universal bd rule | “O2 consumption by CIO is unaltered even in the presence of high levels of H2S” (10.3390/antiox13030383) (nastasi2024cyanideinsensitiveoxidase pages 1-2) |
| NO | reversibly inhibits | Pseudomonas CIO (bd-type cyanide-insensitive oxidase) | Taxon- and assay-specific; high confidence within study | “CIO is reversibly inhibited by NO, while activity recovery after NO exhaustion is full and fast” (10.3390/antiox13030383) (nastasi2024cyanideinsensitiveoxidase pages 1-2) |
| cyanide | inhibits | mammalian cytochrome c oxidase; selects for alternative bacterial oxidases in some taxa | Inhibition of mammalian CcO is high confidence; bacterial consequences are taxon-specific | Cyanide is “a classic inhibitor of mammalian cytochrome c oxidase” while *B. licheniformis* still respires aerobically in cyanide, implying alternative terminal oxidases (10.1007/s10863-024-10041-y) (uriberamirez2024modificationsofthe pages 1-2) |
| aurachin D | binds/inhibits | *E. coli* cytochrome bd-II | Taxon- and paralog-specific; high confidence | Structure of “*Escherichia coli* cytochrome bd-II type oxidase with the bound inhibitor aurachin D” and “revealing the specific aurachin binding” (10.1038/s41467-021-26835-2) (grauel2021structureofescherichia pages 1-2) |
| Q203 | inhibits | mycobacterial cytochrome bc1/aa3 supercomplex | Taxon-specific but therapeutically validated target class; high confidence | Review notes “Q203… has moved to clinical trials” targeting the “bc1-aa3 supercomplex” (10.3389/fcimb.2020.589318) (bajeli2020terminalrespiratoryoxidases pages 1-2) |
| bedaquiline | inhibits | mycobacterial F1Fo-ATP synthase | Taxon-specific drug application; very high confidence | “ATP synthase inhibitor Bedaquiline was approved for the treatment of multi-drug resistant tuberculosis” (10.3389/fcimb.2020.589318) (bajeli2020terminalrespiratoryoxidases pages 1-2) |


*Table: This table lists compact, graph-ready causal edges for microbial aerobic respiration, separating core conserved mechanisms from taxon- or assay-specific variants. It is useful for deciding which edges belong in a general TraitMech graph versus conditional extension modules.*

### Recommended minimal core for `aerobic_respiration.yaml`

These edges are sufficiently general for the top-level graph:

1. **aerobic respiration — has terminal electron acceptor → dioxygen**  
   Evidence: cytochrome c oxidase catalyzes respiratory reduction of O₂ to water, and cytochrome bd is a quinol:oxygen oxidoreductase. (borisov2021bacterialoxidasesof pages 1-2, wikstrom2018oxygenactivationand pages 1-2)

2. **reduced electron donor — supplies electrons through → respiratory dehydrogenase**  
   Keep the donor generic in the core; instantiate NADH, succinate, H₂, formate, lactate, or malate in taxon-specific modules. *P. aeruginosa* has at least 17 predicted dehydrogenases, and recent work measured donor-specific respiratory activities, underscoring this diversity. (hu2024identificationofcomplex pages 6-7, hu2024identificationofcomplex pages 1-3)

3. **respiratory dehydrogenase — reduces → quinone pool**  
   The 2024 *B. licheniformis* study explicitly reports NDH-2 oxidation of NADH with quinone reduction and succinate-dependent quinone reduction. (uriberamirez2024modificationsofthe pages 1-2)

4. **reduced quinone pool — donates electrons to → terminal oxidase branch**  
   This may be direct for bd or bo₃, or indirect through bc₁/bc and cytochrome c. Cytochrome bd uses quinol as its physiological reducing substrate. (borisov2021bacterialoxidasesof pages 1-2, azarkina2023interactionofterminal pages 1-2)

5. **terminal oxidase — catalyzes reduction of → dioxygen** and **dioxygen reduction — produces → water**  
   This is the defining terminal chemistry. Type-A CcO’s overall reaction consumes four reduced cytochrome-c molecules and four protons per O₂ to produce two waters. (wikstrom2018oxygenactivationand pages 1-2)

6. **terminal electron transfer/O₂ reduction — generates or contributes to → proton-motive force**  
   Heme–copper oxidases combine scalar charge separation with proton pumping. Cytochrome bd instead generates PMF through spatially separated proton uptake/release and vectorial charge transfer; it is not a proton pump. (wikstrom2018oxygenactivationand pages 1-2, azarkina2023interactionofterminal pages 1-2, grauel2021structureofescherichia pages 1-2)

7. **proton-motive force — drives → ATP synthesis by F₁F₀-ATP synthase**  
   The 2023 review gives the explicit relationship `ADP + Pi + pmf ↔ ATP + H₂O` and describes bacterial F₁F₀ as a rotary molecular machine. (zharova2023f1·foatpsynthaseatpase pages 1-2)

### Conditional extension edges

* **complex III → reduces cytochrome c → terminal cytochrome-c oxidase.** Curate only where a cytochrome-c branch is demonstrated; bd and bo₃ routes bypass this carrier. (brzezinski2021structureandmechanism pages 1-2, wikstrom2018oxygenactivationand pages 1-2)
* **low O₂ → selects/regulates high-affinity oxidase.** Biologically plausible but not a universal directionality rule. In *C. thermarum*, aa₃ abundance was highest at 4.2% O₂, whereas ba₃ declined below 0.42% O₂ and expected bb₃/bd proteins were not detected. (jong2024quantitativeproteomicsreveals pages 1-2)
* **cyanide/NO/H₂S → inhibits terminal oxidase.** Curate at the specific enzyme, dose, organism, and assay level. *P. aeruginosa* CIO remained active at high H₂S but was reversibly inhibited by NO, with full and rapid recovery after NO exhaustion. (nastasi2024cyanideinsensitiveoxidase pages 1-2)
* **alternative oxidase expression → maintains respiration under stress.** Appropriate as a conditional stress-tolerance module, not as a defining edge for all aerobic respiration. (borisov2021bacterialoxidasesof pages 1-2, nastasi2024cyanideinsensitiveoxidase pages 1-2)

## 4. Recent developments and quantitative evidence, 2023–2024

### Oxygen-dependent respiratory-chain remodeling

A 2024 chemostat/proteomics study grew the obligate aerobic thermoalkaliphile *Caldalkalibacillus thermarum* TA2.A1 across **0.25–4.2% O₂**. Both type-I and type-II NADH dehydrogenases were constitutive; aa₃ oxidase abundance peaked at **4.2% O₂**, while ba₃ abundance declined below **0.42% O₂**. Neither expected bb₃ nor bd terminal oxidase was detected. This is strong evidence for condition-dependent respiratory-chain composition, but it does not establish a universal “low O₂ induces bd” rule. (jong2024quantitativeproteomicsreveals pages 1-2)

### Stationary-phase respiration in a clinically relevant medium

In 2024, *P. aeruginosa* PAO1 grown in urine-like medium showed a stationary-phase respiratory rate **3–4-fold** higher than logarithmic-phase cells. Donor-resolved assays reported NADH oxidation increasing by more than **threefold**, succinate oxidation by more than **fivefold**, and lactate and malate oxidation by approximately **fourfold**. Complex III, NQR, and succinate dehydrogenase emerged as prominent bioenergetic components and possible antibacterial targets. The study also notes that *P. aeruginosa* possesses **17 predicted dehydrogenases, five aerobic terminal oxidases, and two anaerobic terminal oxidases**, demonstrating why a single linear chain is biologically inadequate. (hu2024identificationofcomplex pages 6-7, hu2024identificationofcomplex pages 1-3)

The same report gives an application context: multidrug-resistant *P. aeruginosa* caused more than **30,000 U.S. infections in 2017**, with **10% mortality** and estimated losses of **$800 million**; it also caused over **14,000 catheter-associated urinary-tract infections**, approximately **14%** of CAUTIs during 2015–2017. These epidemiological numbers are contextual statistics cited by the study rather than new 2024 measurements. (hu2024identificationofcomplex pages 1-3)

### Respiratory flexibility and inhibitor tolerance

A 2024 oxygraphic study of *P. aeruginosa* PAO1 membranes and isogenic terminal-oxidase mutants showed that the bd-type cyanide-insensitive oxidase CIO maintained O₂ consumption in high H₂S. NO inhibited CIO reversibly, followed by full and rapid recovery after NO exhaustion. The organism contains four heme–copper oxidases—aa₃, cbb₃-1, cbb₃-2, and bo₃—and one bd-type CIO, making this a well-defined example of branched-chain robustness relevant to infection. (nastasi2024cyanideinsensitiveoxidase pages 1-2)

### Donor- and substrate-dependent use of redundant complexes

A 2024 barcoded transposon study in *Cupriavidus necator* H16 tested growth on succinate, fructose, H₂/CO₂, and formate. It found that only subsets of the organism’s **six terminal respiratory complexes** were used and that utilization depended on energy source. The genome is approximately **6.6 Mb** with about **6,600 genes**; low-level expression of unused respiratory proteins imposed measurable protein costs, providing a route for rational strain engineering. (jahn2024theenergymetabolism pages 1-2)

### Evolutionary clarification of trait boundaries

The 2024 FEBS Letters synthesis argues that oxygen’s earliest major effects were enzyme inhibition and O₂-compatible biosynthesis, with aerobic respiration arising later. Its mapping of **365 reactions and 792 protein families** is especially useful for curation: neither an O₂-dependent reaction nor an “aerobic metabolism” annotation should automatically be converted into `METPO:1000801`. (mrnjavac2024theradicalimpact pages 1-3)

### Structural and mechanistic refinement

Current expert reviews emphasize two mechanistically distinct terminal-oxidase superfamilies. Heme–copper oxidases transfer electrons from cytochrome c or quinol to O₂ and pump protons; cytochrome bd uses quinol, reduces O₂ to H₂O, and establishes PMF without pumped protons. The 3 Å cryo-EM structure of *E. coli* bd-II with aurachin D resolved AppB/AppC/AppX, the heme-d catalytic center, and inhibitor binding in the Q-loop, providing a structural basis for selective antibacterial discovery. (azarkina2023interactionofterminal pages 1-2, grauel2021structureofescherichia pages 1-2)

## 5. Applications and authoritative interpretation

### Antimicrobial development

Respiratory bioenergetics is already clinically validated in tuberculosis. Bedaquiline inhibits mycobacterial ATP synthase and was approved for multidrug-resistant TB; Q203/telacebec targets the mycobacterial cytochrome bcc–aa₃ branch and had entered clinical development at the time of the cited review. Simultaneously blocking alternative terminal oxidases can be lethal in mycobacteria, but this is a taxon-specific synthetic vulnerability rather than a universal aerobic-respiration edge. (bajeli2020terminalrespiratoryoxidases pages 1-2)

Cytochrome bd is particularly attractive because it has been identified only in prokaryotic respiratory chains, occurs in multiple pathogens, supports respiration at very low O₂, and contributes to resistance against host-associated stresses. Experts nevertheless identify unresolved questions about its exact intraprotein electron flow and the structural basis of its unusually high O₂ affinity; these uncertainties argue against overly detailed universal electron-pathway edges within the complex. (borisov2021bacterialoxidasesof pages 1-2)

### Infection biology

Branched respiratory chains allow pathogens to maintain energy and redox homeostasis across hypoxia, pH shifts, NO/H₂S exposure, stationary phase, and nutrient limitation. Recent *P. aeruginosa* studies connect this flexibility to cystic-fibrosis and urinary-tract environments and suggest respiratory complexes as targets against slow-growing or persistent cells. These are important biological applications, but “promotes virulence” should be attached only to organism- and experiment-specific evidence. (nastasi2024cyanideinsensitiveoxidase pages 1-2, hu2024identificationofcomplex pages 1-3)

### Biotechnology and environmental management

*Cupriavidus necator* can grow on H₂/CO₂/O₂ and is a platform for CO₂ fixation and polyhydroxybutyrate production; respiratory-module fitness data can inform removal of costly, unused isoenzymes. (jahn2024theenergymetabolism pages 1-2)

*Bacillus licheniformis* can respire in cyanide-containing alkaline medium and is relevant to cyanide bioremediation. The 2024 paper reports prior degradation benchmarks including **83% removal of 3 mM KCN by *Pseudomonas putida***, **99% degradation of 19.2 mM cyanide by a mixed *Bacillus* culture**, **87% degradation of 7.68 mM KCN by *B. subtilis***, and *B. licheniformis* resistance up to **57.7 mM** with **32 mM consumed**. These values are cross-study application statistics and should not be encoded as universal respiratory properties. (uriberamirez2024modificationsofthe pages 1-2)

## 6. Warnings: claims not yet suitable for general TraitMech curation

1. **Do not encode “all terminal oxidases pump protons.”** Cytochrome bd does not pump protons, despite contributing to PMF. (borisov2021bacterialoxidasesof pages 1-2, azarkina2023interactionofterminal pages 1-2, grauel2021structureofescherichia pages 1-2)
2. **Do not require complex III or cytochrome c.** Quinol oxidases bd and bo₃ accept electrons without that route. (borisov2021bacterialoxidasesof pages 1-2, wikstrom2018oxygenactivationand pages 1-2)
3. **Do not equate cytochrome bd with anaerobic respiration.** It can function at extremely low O₂, but O₂ remains its acceptor; expression under anaerobiosis does not itself prove active aerobic respiration. (borisov2021bacterialoxidasesof pages 1-2, grauel2021structureofescherichia pages 1-2)
4. **Do not generalize oxygen-regulation rules across taxa.** The direction and threshold of oxidase regulation vary with organism, medium, growth phase, and assay. (jong2024quantitativeproteomicsreveals pages 1-2)
5. **Do not treat non-detection by proteomics as genetic absence or lack of capacity.** In *C. thermarum*, bb₃ and bd were not detected under the tested chemostat conditions, but their putative presence was known from genomic analysis. (jong2024quantitativeproteomicsreveals pages 1-2)
6. **Do not infer the trait from isolated O₂-dependent enzymes, ROS defenses, or “aerobic” habitat annotations.** These can reflect O₂ tolerance or biosynthesis rather than energy-conserving respiration. (mrnjavac2024theradicalimpact pages 1-3)
7. **Do not curate inhibitor edges without enzyme and context.** Cyanide, NO, H₂S, aurachin D, Q203, and bedaquiline have distinct targets, affinities, reversibility, and lineage specificity. (bajeli2020terminalrespiratoryoxidases pages 1-2, nastasi2024cyanideinsensitiveoxidase pages 1-2, uriberamirez2024modificationsofthe pages 1-2, grauel2021structureofescherichia pages 1-2)
8. **Do not assign universal H⁺/electron or P/O ratios.** Efficiencies vary by oxidase, donor-entry module, membrane leak, ATP-synthase c-ring stoichiometry, and physiological condition. The reported 0.7 and 0.5 H⁺/electron values in the *C. thermarum* paper derive from model oxidases in other taxa and should not be transferred directly to *C. thermarum*. (jong2024quantitativeproteomicsreveals pages 1-2)
9. **Verify every CURIE before YAML insertion.** Several chemical and complex identifiers above are explicitly marked for independent verification; retaining a label-only node is safer than introducing a false identifier.
10. **Avoid making oxygen consumption alone definitive where chemical or non-respiratory O₂ sinks are plausible.** Pair oxygraphy with donor dependence, inhibitors, mutants, ATP/PMF measurements, or growth evidence.

## 7. DOI-first bibliography

1. **de Jong SI et al.** “Quantitative proteomics reveals oxygen-induced adaptations in *Caldalkalibacillus thermarum* TA2.A1 microaerobic chemostat cultures.” *Frontiers in Microbiology* 15 (published 28 October 2024). DOI: [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929). (jong2024quantitativeproteomicsreveals pages 1-2)
2. **Nastasi MR et al.** “Cyanide Insensitive Oxidase Confers Hydrogen Sulfide and Nitric Oxide Tolerance to *Pseudomonas aeruginosa* Aerobic Respiration.” *Antioxidants* 13:383 (published 21 March 2024). DOI: [10.3390/antiox13030383](https://doi.org/10.3390/antiox13030383). (nastasi2024cyanideinsensitiveoxidase pages 1-2)
3. **Hu Y et al.** “Identification of complex III, NQR, and SDH as primary bioenergetic enzymes during the stationary phase of *Pseudomonas aeruginosa* cultured in urine-like conditions.” *Frontiers in Microbiology* 15 (published 21 February 2024). DOI: [10.3389/fmicb.2024.1347466](https://doi.org/10.3389/fmicb.2024.1347466). (hu2024identificationofcomplex pages 1-3)
4. **Uribe-Ramírez D et al.** “Modifications of the respiratory chain of *Bacillus licheniformis* as an alkalophilic and cyanide-degrading microorganism.” *Journal of Bioenergetics and Biomembranes* 56:591–605 (published online 5 November 2024). DOI: [10.1007/s10863-024-10041-y](https://doi.org/10.1007/s10863-024-10041-y). (uriberamirez2024modificationsofthe pages 1-2)
5. **Jahn M et al.** “The energy metabolism of *Cupriavidus necator* in different trophic conditions.” *Applied and Environmental Microbiology* 90(10) (published 25 September 2024). DOI: [10.1128/aem.00748-24](https://doi.org/10.1128/aem.00748-24). (jahn2024theenergymetabolism pages 1-2)
6. **Mrnjavac N et al.** “The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third.” *FEBS Letters* 598:1692–1714 (2024). DOI: [10.1002/1873-3468.14906](https://doi.org/10.1002/1873-3468.14906). (mrnjavac2024theradicalimpact pages 1-3)
7. **Zharova TV, Grivennikova VG, Borisov VB.** “F₁·F₀ ATP Synthase/ATPase: Contemporary View on Unidirectional Catalysis.” *International Journal of Molecular Sciences* 24:5417 (published 12 March 2023). DOI: [10.3390/ijms24065417](https://doi.org/10.3390/ijms24065417). (zharova2023f1·foatpsynthaseatpase pages 1-2)
8. **Azarkina NV et al.** “Interaction of Terminal Oxidases with Amphipathic Molecules.” *International Journal of Molecular Sciences* 24:6428 (published 29 March 2023). DOI: [10.3390/ijms24076428](https://doi.org/10.3390/ijms24076428). (azarkina2023interactionofterminal pages 1-2)
9. **Borisov VB et al.** “Bacterial Oxidases of the Cytochrome bd Family: Redox Enzymes of Unique Structure, Function, and Utility As Drug Targets.” *Antioxidants & Redox Signaling* 34:1280–1318 (2021). DOI: [10.1089/ars.2020.8039](https://doi.org/10.1089/ars.2020.8039). (borisov2021bacterialoxidasesof pages 1-2)
10. **Brzezinski P, Moe A, Ädelroth P.** “Structure and Mechanism of Respiratory III–IV Supercomplexes in Bioenergetic Membranes.” *Chemical Reviews* 121:9644–9673 (2021). DOI: [10.1021/acs.chemrev.1c00140](https://doi.org/10.1021/acs.chemrev.1c00140). (brzezinski2021structureandmechanism pages 1-2)
11. **Grauel A et al.** “Structure of *Escherichia coli* cytochrome bd-II type oxidase with bound aurachin D.” *Nature Communications* 12:6498 (2021). DOI: [10.1038/s41467-021-26835-2](https://doi.org/10.1038/s41467-021-26835-2). (grauel2021structureofescherichia pages 1-2)
12. **Bajeli S et al.** “Terminal Respiratory Oxidases: A Targetable Vulnerability of Mycobacterial Bioenergetics?” *Frontiers in Cellular and Infection Microbiology* 10 (November 2020). DOI: [10.3389/fcimb.2020.589318](https://doi.org/10.3389/fcimb.2020.589318). (bajeli2020terminalrespiratoryoxidases pages 1-2)
13. **Wikström M, Krab K, Sharma V.** “Oxygen Activation and Energy Conservation by Cytochrome c Oxidase.” *Chemical Reviews* 118:2469–2490 (published 19 January 2018). DOI: [10.1021/acs.chemrev.7b00664](https://doi.org/10.1021/acs.chemrev.7b00664). (wikstrom2018oxygenactivationand pages 1-2)

## Final curation decision

Retain the existing terminal-oxidase graph but expand it upstream to include **electron-donor entry and the quinone pool**, and downstream to include **PMF-dependent ATP synthesis**. Model the **direct quinol-oxidase route** and the **bc₁/bc–cytochrome-c route** as alternatives. Keep oxidase-family mechanisms, oxygen-response rules, inhibitors, stress tolerance, virulence, and donor-specific growth effects in conditional taxon-specific modules. This produces a compact universal graph while preserving the defining chemistry of `METPO:1000801` and avoiding false universality.

References

1. (borisov2021bacterialoxidasesof pages 1-2): Vitaliy B. Borisov, Sergey A. Siletsky, Alessandro Paiardini, David Hoogewijs, Elena Forte, Alessandro Giuffrè, and Robert K. Poole. Bacterial oxidases of the cytochrome<i>bd</i>family: redox enzymes of unique structure, function, and utility as drug targets. Jun 2021. URL: https://doi.org/10.1089/ars.2020.8039, doi:10.1089/ars.2020.8039. This article has 149 citations and is from a domain leading peer-reviewed journal.

2. (wikstrom2018oxygenactivationand pages 1-2): Mårten Wikström, Klaas Krab, and Vivek Sharma. Oxygen activation and energy conservation by cytochrome c oxidase. Chemical Reviews, 118:2469-2490, Jan 2018. URL: https://doi.org/10.1021/acs.chemrev.7b00664, doi:10.1021/acs.chemrev.7b00664. This article has 509 citations and is from a highest quality peer-reviewed journal.

3. (azarkina2023interactionofterminal pages 1-2): Natalia V. Azarkina, Vitaliy B. Borisov, Ilya P. Oleynikov, Roman V. Sudakov, and Tatiana V. Vygodina. Interaction of terminal oxidases with amphipathic molecules. International Journal of Molecular Sciences, 24:6428, Mar 2023. URL: https://doi.org/10.3390/ijms24076428, doi:10.3390/ijms24076428. This article has 9 citations.

4. (grauel2021structureofescherichia pages 1-2): Antonia Grauel, Jan Kägi, Tim Rasmussen, Iryna Makarchuk, Sabrina Oppermann, Aurélien F. A. Moumbock, Daniel Wohlwend, Rolf Müller, Frederic Melin, Stefan Günther, Petra Hellwig, Bettina Böttcher, and Thorsten Friedrich. Structure of escherichia coli cytochrome bd-ii type oxidase with bound aurachin d. Nature Communications, Nov 2021. URL: https://doi.org/10.1038/s41467-021-26835-2, doi:10.1038/s41467-021-26835-2. This article has 68 citations and is from a highest quality peer-reviewed journal.

5. (jahn2024theenergymetabolism pages 1-2): Michael Jahn, Nick Crang, Arvid H. Gynnå, Deria Kabova, Stefan Frielingsdorf, Oliver Lenz, Emmanuelle Charpentier, and Elton P. Hudson. The energy metabolism of <i>cupriavidus necator</i> in different trophic conditions. Oct 2024. URL: https://doi.org/10.1128/aem.00748-24, doi:10.1128/aem.00748-24. This article has 41 citations and is from a peer-reviewed journal.

6. (brzezinski2021structureandmechanism pages 1-2): Peter Brzezinski, Agnes Moe, and Pia Ädelroth. Structure and mechanism of respiratory iii–iv supercomplexes in bioenergetic membranes. Chemical Reviews, 121:9644-9673, Jun 2021. URL: https://doi.org/10.1021/acs.chemrev.1c00140, doi:10.1021/acs.chemrev.1c00140. This article has 123 citations and is from a highest quality peer-reviewed journal.

7. (mrnjavac2024theradicalimpact pages 1-3): Natalia Mrnjavac, Falk S. P. Nagies, Jessica L. E. Wimmer, Nils Kapust, Michael R Knopp, Katharina Trost, L. Modjewski, Nicolas C. Bremer, Marek Mentel, Mauro Degli Esposti, Itzhak Mizrahi, John F Allen, and William F. Martin. The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third. FEBS letters, 598:1692-1714, May 2024. URL: https://doi.org/10.1002/1873-3468.14906, doi:10.1002/1873-3468.14906. This article has 16 citations and is from a peer-reviewed journal.

8. (hu2024identificationofcomplex pages 1-3): Yuyao Hu, Ming Yuan, Alexander Julian, Karina Tuz, and Oscar Juárez. Identification of complex iii, nqr, and sdh as primary bioenergetic enzymes during the stationary phase of pseudomonas aeruginosa cultured in urine-like conditions. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347466, doi:10.3389/fmicb.2024.1347466. This article has 12 citations and is from a peer-reviewed journal.

9. (uriberamirez2024modificationsofthe pages 1-2): Daniel Uribe-Ramírez, Lucero Romero-Aguilar, Héctor Vázquez-Meza, Eliseo Cristiani-Urbina, and Juan Pablo Pardo. Modifications of the respiratory chain of bacillus licheniformis as an alkalophilic and cyanide-degrading microorganism. Journal of Bioenergetics and Biomembranes, 56:591-605, Nov 2024. URL: https://doi.org/10.1007/s10863-024-10041-y, doi:10.1007/s10863-024-10041-y. This article has 1 citations and is from a peer-reviewed journal.

10. (zharova2023f1·foatpsynthaseatpase pages 1-2): Tatyana V. Zharova, Vera G. Grivennikova, and Vitaliy B. Borisov. F1·fo atp synthase/atpase: contemporary view on unidirectional catalysis. International Journal of Molecular Sciences, 24:5417, Mar 2023. URL: https://doi.org/10.3390/ijms24065417, doi:10.3390/ijms24065417. This article has 58 citations.

11. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

12. (nastasi2024cyanideinsensitiveoxidase pages 1-2): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

13. (bajeli2020terminalrespiratoryoxidases pages 1-2): Sapna Bajeli, Navin Baid, Manjot Kaur, Ganesh P. Pawar, Vinod D. Chaudhari, and Ashwani Kumar. Terminal respiratory oxidases: a targetables vulnerability of mycobacterial bioenergetics? Frontiers in Cellular and Infection Microbiology, Nov 2020. URL: https://doi.org/10.3389/fcimb.2020.589318, doi:10.3389/fcimb.2020.589318. This article has 53 citations.

14. (hu2024identificationofcomplex pages 6-7): Yuyao Hu, Ming Yuan, Alexander Julian, Karina Tuz, and Oscar Juárez. Identification of complex iii, nqr, and sdh as primary bioenergetic enzymes during the stationary phase of pseudomonas aeruginosa cultured in urine-like conditions. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347466, doi:10.3389/fmicb.2024.1347466. This article has 12 citations and is from a peer-reviewed journal.