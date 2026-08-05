---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:35:06.125087'
end_time: '2026-08-04T06:45:43.890499'
duration_seconds: 637.77
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: Oxidative phosphorylation
  trait_identifier: METPO:1000803
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: oxidative_phosphorylation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism that generates ATP through the transfer of electrons from
    electron donors to electron acceptors via redox reactions, coupled to the pumping
    of protons across a membrane to create an electrochemical gradient.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1038/191144a0: phosphorylation to electron and hydrogen
    transfer (Mitchell''s chemiosmotic proposal supports coupling electron transfer
    to phosphorylation.) | DOI:10.1038/s41598-019-38564-0: energized by the proton
    motive force (Supports proton motive force-driven ATP synthesis by F1Fo ATP synthase.)'
  causal_graph_summary: 'oxidative_phosphorylation_chemiosmotic_coupling: 16 nodes,
    12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 60
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Oxidative phosphorylation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000803
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that generates ATP through the transfer of electrons from electron donors to electron acceptors via redox reactions, coupled to the pumping of protons across a membrane to create an electrochemical gradient.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/191144a0: phosphorylation to electron and hydrogen transfer (Mitchell's chemiosmotic proposal supports coupling electron transfer to phosphorylation.) | DOI:10.1038/s41598-019-38564-0: energized by the proton motive force (Supports proton motive force-driven ATP synthesis by F1Fo ATP synthase.)
- **Existing causal graph summary:** oxidative_phosphorylation_chemiosmotic_coupling: 16 nodes, 12 edges

## Research Objective

Research the microbial trait **Oxidative phosphorylation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/oxidative_phosphorylation.yaml`.

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
- **Trait label:** Oxidative phosphorylation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000803
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that generates ATP through the transfer of electrons from electron donors to electron acceptors via redox reactions, coupled to the pumping of protons across a membrane to create an electrochemical gradient.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/191144a0: phosphorylation to electron and hydrogen transfer (Mitchell's chemiosmotic proposal supports coupling electron transfer to phosphorylation.) | DOI:10.1038/s41598-019-38564-0: energized by the proton motive force (Supports proton motive force-driven ATP synthesis by F1Fo ATP synthase.)
- **Existing causal graph summary:** oxidative_phosphorylation_chemiosmotic_coupling: 16 nodes, 12 edges

## Research Objective

Research the microbial trait **Oxidative phosphorylation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/oxidative_phosphorylation.yaml`.

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


# Curation report: microbial oxidative phosphorylation

## Trait record and scope

- **Trait label:** Oxidative phosphorylation
- **Trait identifier:** **`METPO:1000803`**
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1000060`

### Operational definition

For TraitMech, this trait should mean the **physiological capacity to conserve energy by coupling a membrane-associated respiratory electron-transfer chain to formation of an electrochemical ion gradient, followed by ATP synthesis from ADP and inorganic phosphate through an ion-driven rotary ATP synthase**. In the canonical bacterial pathway, reducing equivalents enter through primary dehydrogenases, electrons pass through a membrane quinone pool to terminal oxidases or reductases, proton motive force (PMF) is generated, and F-type ATP synthase consumes that PMF to make ATP. Recent reviews describe the same core sequence: respiratory complexes convert NADH or FADH₂ energy into a proton electrochemical gradient, and that gradient drives ATP synthase. (tsviklist2022thecpxstress pages 1-2, zharova2023f1·foatpsynthaseatpase pages 1-2)

The trait is **not synonymous with aerobic respiration**. Oxygen is one terminal acceptor, but anaerobic respiratory chains using nitrate or other acceptors can also conserve energy through an ion gradient. Respiratory nitrate reductase Nar, for example, receives electrons from quinol and can support membrane-potential maintenance under oxygen limitation, although the demonstrated *Streptomyces coelicolor* case sustains survival rather than anaerobic growth. (sawers2019anaerobicnitraterespiration pages 1-2)

### Inclusion criteria

A positive mechanistic graph should normally contain evidence for all three modules:

1. **Respiratory redox module:** oxidation of an electron donor and reduction of a terminal acceptor through a membrane-associated chain.
2. **Chemiosmotic module:** generation or maintenance of an H⁺ or, in a defined microbial variant, Na⁺ electrochemical gradient across an energy-transducing membrane.
3. **ATP-synthesis module:** gradient-driven ATP formation by F-type or archaeal/prokaryotic A/V-type ATP synthase.

### Boundary cases

- **Substrate-level phosphorylation** is outside scope because ATP is formed by direct phosphoryl transfer rather than through a respiratory ion gradient.
- **Fermentation alone** is outside scope. Fermentative metabolism may supply respiratory donors, but fermentation does not establish this trait unless an ion-motive respiratory chain and ATP synthase are also demonstrated.
- **Photophosphorylation** is a neighboring but distinct trait: photosystem II and cytochrome b₆f use light-driven electron transfer to generate the gradient. The respiratory bc₁/bcc complexes belong here; photosynthetic b₆f should not be imported into this graph merely because it uses a homologous Q-cycle. (kao2022quinonebindingsites pages 1-3)
- **Flavin-based electron bifurcation alone** is not oxidative phosphorylation. It directly couples exergonic and endergonic redox reactions in a soluble complex and “is not coupled to ATP synthesis”; it can nevertheless be an upstream donor-generating module when reduced ferredoxin subsequently feeds an ion-motive respiratory chain. (muller2018electronbifurcationa pages 1-2)
- **ATP hydrolysis-driven maintenance of PMF** is the reverse activity of an ATPase, not evidence of oxidative phosphorylation unless net gradient-driven ATP synthesis is shown. Some bacterial and archaeal enzymes are physiologically unidirectional or strongly regulated. (zharova2023f1·foatpsynthaseatpase pages 1-2)
- **Presence of respiratory genes alone** establishes genomic potential, not an observed phenotype. This is especially important for MAG-derived reconstructions.

## Candidate nodes

Identifiers below are conservative. Where exact cross-ontology grounding is uncertain or taxon-dependent, a label-only node is preferable to an invented or overly broad CURIE.

### Trait, pathways, and processes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| Oxidative phosphorylation | `METPO:1000803` | Root trait node; quote identifier verbatim. |
| Respiratory electron-transport chain | GO term to be selected after ontology lookup; otherwise label-only | Should encompass primary dehydrogenase → quinone → terminal reductase/oxidase. |
| Chemiosmotic coupling | Label-only, or reviewed GO term | Mechanistic bridge between redox chemistry and ATP synthesis. |
| Proton motive force | Label-only; do not equate automatically with a proton-transport GO process | PMF contains electrical and chemical components. |
| Sodium motive force | Label-only | Valid alternative in particular bacteria and archaea, not universal. |
| ATP synthesis coupled to ion translocation | EC/GO term after validation | Product-level endpoint of the graph. |
| Aerobic respiration | GO-groundable neighboring process | A subtype/context, not equivalent to the target trait. |
| Anaerobic respiration | GO-groundable neighboring process | Include only when an alternative acceptor supports ion-gradient energy conservation. |

### Complexes, enzymes, genes, and proteins

| Candidate node | Suggested grounding | Representative genes or subunits | Notes |
|---|---|---|---|
| Proton-translocating NADH:quinone oxidoreductase, complex I/NDH-1 | `EC:7.1.1.2` | bacterial `nuoA–N`; mycobacterial `nuoABCDEFGHIJKLMN` | Oxidizes NADH, reduces quinone, translocates four H⁺ per NADH/2 e⁻ in the canonical enzyme. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, bajeli2020terminalrespiratoryoxidases pages 1-2) |
| Type II NADH dehydrogenase, NDH-2 | Label-only pending exact EC confirmation | `ndh`, `ndhA` in *M. tuberculosis* | Feeds electrons to quinone but is non-proton-pumping in the cited mycobacterial system. (bajeli2020terminalrespiratoryoxidases pages 1-2) |
| Succinate dehydrogenase, complex II | `EC:1.3.5.1` | `sdhABCD` family | Connects the TCA cycle to the quinone pool; generally not a primary PMF generator. (borisov2023cytochromebdas pages 1-3, tsviklist2022thecpxstress pages 1-2) |
| Na⁺-translocating NADH:quinone oxidoreductase | Label-only; validate EC/KEGG module before import | `nqrA–F` | Variant primary sodium pump; should be a conditional branch. (mulkidjanian2008thepastand pages 1-2) |
| Cytochrome bc₁ complex | Label-only complex node | `petABC`/taxon-specific nomenclature | Quinol oxidation and Q-cycle proton translocation. |
| Cytochrome bcc–aa₃ supercomplex | Label-only complex node | `qcrABC`, `cta` genes, taxon-specific | Important actinobacterial/mycobacterial branch. |
| Heme-copper terminal oxidase | Label-only superclass | `cyoABCD`, `cox/cta` families | Reduces O₂; pumping stoichiometry varies by family. |
| Cytochrome bd oxidase | Label-only complex; ground subunits separately if needed | `cydAB`; accessory `cydX`, `cydH/Y`; *E. coli* `appCBX` | Generates PMF through scalar chemistry/charge separation but does not classically pump vectorial protons; also contributes to stress defense. (borisov2023cytochromebdas pages 1-3, bajeli2020terminalrespiratoryoxidases pages 1-2) |
| Respiratory nitrate reductase Nar | `EC:1.7.5.1` as a candidate, verify against enzyme record | `narGHI`, transport/regulatory genes separately | Quinolfed nitrate-to-nitrite branch; energetic outcome is species- and state-dependent. (sawers2019anaerobicnitraterespiration pages 1-2) |
| F-type H⁺-transporting ATP synthase | `EC:7.1.2.2` | `atpIBEFHAGDC` or taxon-specific operon | Canonical bacterial ATP-producing rotary complex. |
| A-type/A/V-type ATP synthase | Label-only until exact family term is validated | archaeal/prokaryotic `atp` operons | Common in archaea and some bacteria; may use H⁺ or Na⁺. |
| Cpx envelope-stress system | Label-only or component-level protein grounding | `cpxA`, `cpxR` | Optional regulatory module: affects respiratory-complex biogenesis/turnover in *E. coli*, not a universal trait determinant. (tsviklist2022thecpxstress pages 1-2) |

### Chemicals and energetic intermediates

| Node | Suggested CURIE |
|---|---|
| NADH | `CHEBI:16908` |
| NAD⁺ | `CHEBI:15846` |
| Succinate | `CHEBI:15741` |
| Fumarate | `CHEBI:18012` |
| Ubiquinone | `CHEBI:16389` |
| Ubiquinol | `CHEBI:17976` |
| Menaquinone / menaquinol | Validate exact ChEBI records before YAML import |
| Oxygen | `CHEBI:15379` |
| Water | `CHEBI:15377` |
| Nitrate | `CHEBI:17632` |
| Nitrite | `CHEBI:16301` |
| Proton | `CHEBI:15378` |
| Sodium ion | `CHEBI:29101` |
| ATP | `CHEBI:15422` |
| ADP | `CHEBI:16761` |
| Phosphate | `CHEBI:18367` |
| Reduced ferredoxin | Label-only until a chemically appropriate class is selected |

Quinones are both electron and proton carriers in prokaryotic membranes: their ring accepts two electrons and two protons to form quinol, while the hydrophobic tail retains them in the membrane. (kao2022quinonebindingsites pages 1-3)

### Cellular locations

- **Bacterial cytoplasmic/inner membrane:** principal coupling membrane containing dehydrogenases, quinones, terminal complexes, and F₀/A₀ sectors. The *E. coli* complex-I membrane arm lies in the lipid bilayer while its NADH-oxidizing peripheral arm extends into the cytoplasm. (tsviklist2022thecpxstress pages 1-2)
- **Cytoplasm:** side bearing bacterial F₁ catalytic heads in the standard orientation. (frasch2022f1foatpsynthase pages 1-2)
- **Periplasm or extracellular-positive side:** proton-accumulating side in many diderm bacteria; topology terminology must be adapted for monoderms and archaea.
- **Archaeal cytoplasmic membrane:** energy-transducing membrane for A/A-V ATP synthases; do not use mitochondrial localization for a microbial graph unless microbial eukaryotes are explicitly in scope.

### Environmental and experimental factors

- Oxygen availability; hypoxia; anoxia.
- Availability of nitrate or another terminal acceptor.
- Electron-donor identity and concentration: NADH-generating carbon source, succinate, H₂, reduced sulfur compound, reduced ferredoxin.
- External pH, salinity, and Na⁺ availability; these can select H⁺ versus Na⁺ energetics. Sodium cycling is not restricted to extremophiles and also occurs in marine bacteria and pathogens. (mulkidjanian2008thepastand pages 1-2)
- Membrane integrity and proton/ion permeability.
- Growth, dormancy, stationary phase, and nonreplicating persistence.
- Respiratory inhibitors and uncouplers: complex-specific inhibitors, ATP-synthase inhibitors, and protonophores must be represented separately because their causal effects differ.

### Assay-observed nodes

Recommended evidence nodes include oxygen-consumption rate, nitrate-to-nitrite reduction, donor-dependent quinone reduction, membrane potential, ΔpH, PMF-sensitive dye response, cellular ATP or ATP/ADP ratio, growth yield, inhibitor-sensitive respiration, and genetic complementation or knockout phenotype. Oxygen consumption alone is insufficient to infer ATP coupling: increased respiration can result from PMF collapse, increased electron supply, or altered chain regulation. (harrison2024remissionspectroscopyresolves pages 1-4)

## Candidate causal edges

The table prioritizes edges suitable for direct translation into YAML. “Core” denotes broad mechanistic support; “conditional” denotes taxon-, environment-, or assay-specific branches.

| # | Subject — predicate — object | Reference and supporting snippet | Curation notes |
|---:|---|---|---|
| 1 | **NADH — is oxidized by — complex I/NDH-1** | DOI [10.3390/ijms252413421](https://doi.org/10.3390/ijms252413421), published 14 Dec 2024: “complex I … catalyzes the oxidation of NADH by ubiquinone.” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | **Core.** Do not apply to NDH-2 without a separate edge. |
| 2 | **complex I — reduces — ubiquinone to ubiquinol** | Same source gives the reaction `NADH + Q … ↔ NAD+ + QH2`. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | **Core** for quinone-using complex I; use the organism’s actual quinone, often menaquinone in Gram-positive lineages. |
| 3 | **complex I — translocates — four H⁺ across the coupling membrane** | “vectorial transmembrane transfer of four H+ ions”; the abstract likewise states “transmembrane transfer of four protons.” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | **Core with stoichiometric qualifier:** 4 H⁺ per NADH/2 e⁻ for canonical complex I. |
| 4 | **complex-I proton translocation — contributes to — PMF** | The same 2024 review states this produces “energy conservation in the form of an electrochemical gradient … (proton motive force, pmf).” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | **Core.** Keep gradient generation separate from ATP synthesis. |
| 5 | **succinate — is oxidized by — succinate dehydrogenase** | The 2023 *E. coli* review states: “SDH oxidizes succinate by ubiquinone.” (borisov2023cytochromebdas pages 1-3) | **Core entry branch**, but organism-specific substrate/quinone identity must be checked. |
| 6 | **succinate dehydrogenase — reduces — quinone** | “Succinate dehydrogenase (SDH) transfers electrons from succinate to ubiquinone/menaquinone.” (borisov2023cytochromebdas pages 1-3) | **Core.** |
| 7 | **succinate dehydrogenase — does not directly generate — PMF** | Figure text: “NDH-2 and SDH do not produce proton motive force.” (borisov2023cytochromebdas pages 1-3) | **Negative mechanistic constraint**, well supported for the cited *E. coli* architecture; avoid treating SDH as a proton pump. |
| 8 | **primary dehydrogenases — feed electrons into — quinone pool** | “The respiratory chain is composed of primary dehydrogenases and terminal oxidases coupled by the quinone pool.” (tsviklist2022thecpxstress pages 1-2) | **Core architecture.** A useful abstraction above individual donors. |
| 9 | **quinone — accepts two electrons and two protons to become — quinol** | Quinone’s ring “accepts two electrons and two protons to become the fully reduced quinol.” (kao2022quinonebindingsites pages 1-3) | **Core chemical edge.** |
| 10 | **cytochrome bc₁/bcc Q-cycle — translocates protons and contributes to — PMF** | Cytochrome bc complexes use “the same Mitchellian Q cycle mechanism, with which they accomplish proton translocation and thus contribute to the generation of proton motive force.” (kao2022quinonebindingsites pages 1-3) | **Core for bc/bcc-containing chains.** Do not require this node in lineages lacking bc complexes. |
| 11 | **cytochrome bc₁ — transfers electrons through cytochrome c to — cytochrome-c oxidase** | Complex III “oxidises quinol and transfer[s] the electrons to cytochrome c oxidase … via … cytochrome c.” (kao2022quinonebindingsites pages 1-3) | **Conditional architecture.** Many bacterial chains use direct quinol oxidases instead. |
| 12 | **terminal oxidase — reduces — O₂ to water** | “bd-I, bd-II, and bo3 oxidize ubiquinol and/or menaquinol by O2”; heme d reduces O₂ by four electrons to two waters. (borisov2023cytochromebdas pages 1-3) | **Aerobic branch.** Ground individual oxidase family where known. |
| 13 | **cytochrome bd — couples quinol oxidation/O₂ reduction to — PMF generation** | Cytochrome bd “couples the oxidation of ubiquinol or menaquinol by molecular oxygen to the generation of proton motive force.” (borisov2023cytochromebdas pages 1-3) | **Core for bd-positive taxa**, but phrase as scalar proton chemistry/charge separation, not proton pumping. |
| 14 | **cytochrome bd — does not pump — vectorial protons** | Mycobacterial review: cytochrome bd “does not pump out the vectoral protons and is energetically less efficient.” (bajeli2020terminalrespiratoryoxidases pages 1-2) | **Taxon-supported mechanistic constraint.** Compatible with edge 13. |
| 15 | **cytochrome bd — promotes — oxidative/chemical stress tolerance** | The 2023 review describes H₂O₂ elimination and adaptation to antibiotics, sulfide, NO, peroxynitrite, ammonia, and cyanide. (borisov2023cytochromebdas pages 1-3) | **Conditional accessory edge**, not required to define OxPhos. Antioxidant generalization beyond tested taxa is uncertain. |
| 16 | **respiratory nitrate reductase Nar — reduces — nitrate to nitrite** | Nar is a “membrane-associated heterotrimeric molybdoenzyme” catalyzing the “2-electron reduction of NO3− to NO2−.” (sawers2019anaerobicnitraterespiration pages 1-2) | **Anaerobic branch.** |
| 17 | **quinol — donates electrons to — Nar** | Nar “typically receiv[es] its electrons directly from quinol.” (sawers2019anaerobicnitraterespiration pages 1-2) | **Broad Nar mechanism**, but verify the donor quinone in each taxon. |
| 18 | **nitrate respiration — maintains — ion gradient/membrane potential under O₂ limitation** | Three Nar enzymes “contribute to maintenance of a membrane potential” in hypoxic/anoxic *S. coelicolor*; activity was insufficient for growth but supported survival. (sawers2019anaerobicnitraterespiration pages 1-2) | **Uncertain/taxon-specific.** Curate with organism and physiological-state qualifiers. |
| 19 | **respiratory-chain electron transfer — generates — proton electrochemical gradient** | ETC complexes “convert the energy of reducing equivalents … into a proton electrochemical gradient across the membrane.” (tsviklist2022thecpxstress pages 1-2) | **Core summary edge.** |
| 20 | **Na⁺ primary pumps — generate — sodium motive force** | Some bacteria possess “primary generators of the transmembrane electrochemical gradient of Na+.” (mulkidjanian2008thepastand pages 1-2) | **Conditional sodium branch.** Assign Na⁺-NQR only with direct gene/biochemical evidence. |
| 21 | **PMF or sodium motive force — drives — rotary ATP synthase** | F₁F₀ complexes use a “proton gradient (or Na+ gradient in some organisms)” to drive the ATP/ADP·Pi ratio from equilibrium. (frasch2022f1foatpsynthase pages 1-2) | **Core H⁺ edge; conditional Na⁺ variant.** |
| 22 | **transmembrane proton flow through F₀ — rotates — c-ring/γ rotor** | Proton flow driven by a pH gradient rotates the c-ring, which drives γ rotation. (frasch2022f1foatpsynthase pages 1-2) | **Core mechanochemical edge.** |
| 23 | **rotor rotation — drives — ATP synthesis in F₁** | The same source says c-ring-driven γ rotation “force[s] ATP synthesis in F1.” (frasch2022f1foatpsynthase pages 1-2) | **Core.** |
| 24 | **ATP synthase — converts — ADP + Pi + PMF to ATP + H₂O** | The 2023 review gives `ADP + Pi + pmf ↔ ATP + H2O`. (zharova2023f1·foatpsynthaseatpase pages 1-2) | **Core reaction edge.** Direction should be ATP synthesis for this trait. |
| 25 | **proton-impermeable coupling membrane — enables — chemiosmotic coupling** | ATP synthase is embedded in a “proton-tight coupling membrane”; intact membrane vesicles are required to preserve PMF experimentally. (junge2015atpsynthase. pages 1-2, harrison2024remissionspectroscopyresolves pages 1-4) | **Core structural prerequisite.** |
| 26 | **protonophore/uncoupler — collapses — PMF** | The 2024 study defines uncoupler activity as proton leakage that “collapses the PMF.” (harrison2024remissionspectroscopyresolves pages 1-4) | **Assay/perturbation edge.** Use CCCP or another named compound only when tested. |
| 27 | **PMF collapse — uncouples — respiration from ATP synthesis** | The live-cell study notes that increased oxygen consumption can arise from PMF collapse and therefore cannot alone diagnose productive OxPhos. (harrison2024remissionspectroscopyresolves pages 1-4) | **Assay interpretation edge.** |
| 28 | **bedaquiline — inhibits — mycobacterial ATP synthase** | Bedaquiline “binds to ATP synthase of the oxidative phosphorylation system”; resistance maps to `AtpE`, and structural maps identify its c-ring binding site. (harrison2024remissionspectroscopyresolves pages 1-4) | **Application, taxon-specific.** The 2024 source is a preprint. |
| 29 | **bedaquiline treatment — redirects — electron flux toward cytochrome bd** | Live-cell remission spectroscopy observed “sub-second redirection of electron flux to the cytochrome bd oxidase.” (harrison2024remissionspectroscopyresolves pages 1-4) | **Recent but provisional:** preprint, mycobacterial context, assay-specific. |
| 30 | **simultaneous loss/inhibition of bc₁–aa₃ and cytochrome bd — causes — rapid mycobacterial death** | Genetic or pharmacological ablation of both terminal oxidases “leads to the rapid death of the mycobacterial cells.” (bajeli2020terminalrespiratoryoxidases pages 1-2) | **Therapeutic conditional edge.** Do not generalize to all bacteria. |
| 31 | **respiratory electron exchange with electrodes — supports — bioelectrochemical applications** | Electrode–bacterium interactions are used for electricity generation, wastewater treatment, bioremediation, and valuable-product production. (kracke2015microbialelectrontransport pages 1-2) | **Application edge**, not part of the minimal intracellular graph. |
| 32 | **Cpx envelope-stress response — regulates — respiratory-complex biogenesis/turnover** | In *E. coli*, Cpx affects NDH-I stability and SDH activity and serves as a “sentry of inner membrane protein biogenesis.” (tsviklist2022thecpxstress pages 1-2) | **Regulatory, taxon-specific.** Keep outside the minimal core unless the graph supports contextual regulation. |

The compact core suitable for initial YAML implementation is summarized below.

| subject | predicate | object | suggested grounding | evidence class/caveat |
|---|---|---|---|---|
| NADH | donates electrons to via | respiratory complex I, reducing quinone to quinol and translocating 4 H+ across the membrane | NADH: CHEBI:16908; respiratory complex I / NDH-1: EC 7.1.1.2; ubiquinone: CHEBI:16389; ubiquinol: CHEBI:17976; proton: CHEBI:15378 | Review-based, broad bacteria/mitochondria evidence; 4 H+ stoichiometry explicit in 2024 review (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) |
| succinate | donates electrons to via | succinate dehydrogenase, reducing quinone | succinate: CHEBI:15741; succinate dehydrogenase: EC 7.1.1.2 not appropriate / use label-only + EC 1.3.5.1; quinone: CHEBI:16389 or label-only isoprenoid quinone | Review-based; broad bacterial ETC architecture; SDH usually not PMF-generating itself (borisov2023cytochromebdas pages 1-3, tsviklist2022thecpxstress pages 1-2, kao2022quinonebindingsites pages 1-3) |
| quinol | is oxidized by | cytochrome bc1/bcc complex Q-cycle, contributing to proton motive force | quinol: CHEBI:17976 or label-only quinol; cytochrome bc1/bcc complex: GO:0008121 not exact, prefer label-only; proton motive force: GO:0015990 | Review-based; mechanistic support for Mitchellian Q-cycle and proton translocation; exact complex composition varies by taxon (kao2022quinonebindingsites pages 1-3) |
| quinol | is oxidized by terminal oxidase, reducing | O2 to H2O and contributing to proton motive force | oxygen: CHEBI:15379; water: CHEBI:15377; terminal oxidase: label-only; proton motive force: GO:0015990 | Broad respiratory evidence; terminal oxidase identity varies (bo3, aa3, bd). For bd, PMF generation occurs without classical proton pumping in some descriptions, so keep mechanism-general (borisov2023cytochromebdas pages 1-3, bajeli2020terminalrespiratoryoxidases pages 1-2) |
| quinol | donates electrons to via | respiratory nitrate reductase (Nar), reducing nitrate to nitrite and helping maintain an ion gradient | nitrate: CHEBI:17632; nitrite: CHEBI:16301; respiratory nitrate reductase: EC 7.1.1.1 not appropriate / prefer EC 1.7.5.1; Nar: label-only | Taxon-specific, often non-growth maintenance role; supported in Streptomyces and mycobacterial review context; ion-gradient maintenance may be indirect/supercomplex-linked (sawers2019anaerobicnitraterespiration pages 1-2, bajeli2020terminalrespiratoryoxidases pages 1-2) |
| Na+-translocating NADH:quinone oxidoreductase (Na+-NQR) | generates | sodium-motive force | Na+-NQR: label-only; sodium ion: CHEBI:29101; sodium-motive force: label-only | Variant pathway, not universal OxPhos core; review evidence from sodium energetics and downstream drug-target synthesis, conservative grounding only (mulkidjanian2008thepastand pages 1-2, sorescu2025breakthroughsinthe pages 24-25) |
| H+ motive force or Na+ motive force | drives | F-type ATP synthase or A/V-type ATP synthase to synthesize ATP from ADP + Pi | ATP: CHEBI:15422; ADP: CHEBI:16761; phosphate: CHEBI:18367; F-type ATP synthase: EC 7.1.2.2; A/V-type ATP synthase: label-only | Strong review evidence; proton-coupled core is broad, Na+-coupled forms are valid microbial variants; A/V-type ATP synthase especially relevant in archaea/some bacteria (zharova2023f1·foatpsynthaseatpase pages 1-2, frasch2022f1foatpsynthase pages 1-2, mulkidjanian2008thepastand pages 1-2) |
| uncoupler | collapses | proton motive force | uncoupler: label-only; CCCP: CHEBI:34908; proton motive force: GO:0015990 | Experimental/assay factor rather than native trait mechanism; supported by bedaquiline-mechanism discussion and standard inhibitor logic (harrison2024remissionspectroscopyresolves pages 1-4) |
| bedaquiline | inhibits | mycobacterial ATP synthase | bedaquiline: CHEBI:67511; ATP synthase: EC 7.1.2.2 | Drug/application edge; mycobacteria-specific, clinically important; supported by 2024 live-cell spectroscopy preprint and 2020 review (harrison2024remissionspectroscopyresolves pages 1-4, bajeli2020terminalrespiratoryoxidases pages 1-2) |


*Table: This table summarizes compact, curation-ready core edges for microbial oxidative phosphorylation, restricted to the main respiratory sequence, ion-gradient coupling, and high-value perturbation edges. It is useful as a conservative starting point for TraitMech node and edge selection, with caveats marking variant, taxon-specific, or assay-specific claims.*

## Recent developments and quantitative evidence

### Complex I mechanism, 2024

A December 2024 review consolidates bacterial and eukaryotic structural work and explicitly assigns **four translocated H⁺ per NADH oxidized** to canonical complex I. It further estimates that complex I supplies approximately **40% of total energy storage** during NADH-to-O₂ electron transfer in the canonical complex-I/III/IV chain. The first value is appropriate as a stoichiometric edge qualifier; the 40% figure is system-level and should not be generalized across diverse microbial chains. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)

### ATP-synthase mechanism and diversity, 2022–2023

F-type ATP synthase is a rotary motor with F₀ embedded in the coupling membrane and F₁ carrying three catalytic sites. In the *E. coli* c₁₀-ring system, single-molecule work summarized in 2022 reported pauses every **36°**, including an approximately **11° proton-translocation-dependent step** followed by a **25° electrostatic step**. These are valuable mechanistic annotations but are not universal stoichiometries because c-ring size is species-specific. (frasch2022f1foatpsynthase pages 1-2)

The 2023 review describes bacterial F₁F₀ complexes as larger than **500 kDa**, composed in the canonical bacterial form of eight subunit types, with c-ring stoichiometry ranging from **8 to 17** among species. It also emphasizes that some bacterial enzymes, especially mycobacterial F₁F₀, synthesize ATP efficiently but show little or no ATP-hydrolysis activity, arguing against a simplistic fully reversible edge for every organism. (zharova2023f1·foatpsynthaseatpase pages 1-2)

### Cytochrome bd, 2023

Current synthesis treats cytochrome bd as both an energy-conserving terminal oxidase and a stress-defense enzyme. In *E. coli*, the two characterized bd systems are encoded by `cydAB` and `appCB`; the cited review reports endogenous H₂O₂ production rates of **9–22 μM s⁻¹** in exponentially growing cells while discussing bd-associated peroxide removal. That quantitative rate concerns ROS context, not ATP yield. (borisov2023cytochromebdas pages 1-3)

### Living-cell drug mechanism, 2024

A December 2024 preprint combined remission spectroscopy with oxygen-consumption measurements in living mycobacteria. It found no evidence that bedaquiline acts predominantly as a protonophore or ionophore, but observed electron-flux redirection to cytochrome bd on a **sub-second/second timescale** and concluded that the dominant cellular action resembles ATP-synthase jamming by oligomycin. The paper also reports that ATP depletion begins within hours whereas killing can take approximately a week, consistent with transient metabolic adaptation. These conclusions should remain **provisional until peer reviewed**. (harrison2024remissionspectroscopyresolves pages 1-4)

### Environmental genomics, 2024

A restored-mangrove study reconstructed **11 MAGs from six bacterial phyla** and inferred complementary carbon, sulfur, and energy-metabolism routes under fluctuating oxygen, salinity, sulfate, and nutrient conditions. It identified pathway combinations relevant to wastewater and organic-effluent treatment. This demonstrates a real environmental application for respiratory-module annotation, but MAG pathway presence and flux-balance predictions are not direct biochemical proof of oxidative phosphorylation in an individual organism. (laux2024livinginmangroves pages 1-2)

## Current applications and implementations

1. **Tuberculosis treatment.** Bedaquiline validates mycobacterial ATP synthesis as a clinically actionable vulnerability. Q203/telacebec-class compounds target the bc₁–aa₃ branch, while cytochrome-bd inhibitors are being investigated to prevent respiratory bypass. The 2020 review reports that Q203 had advanced to clinical trials and that combined inhibition of both terminal branches causes rapid killing in experimental mycobacterial systems. (bajeli2020terminalrespiratoryoxidases pages 1-2)
2. **Live-cell mechanism-of-action profiling.** Remission spectroscopy resolves cytochrome redox occupancy while oxygen-consumption rate is measured, allowing ATP-synthase inhibition, uncoupling, and terminal-oxidase switching to be distinguished more directly than by oxygen consumption alone. (harrison2024remissionspectroscopyresolves pages 1-4)
3. **Bioelectrochemical systems.** Microbial respiratory and extracellular electron-transfer networks are exploited in microbial fuel cells, microbial electrolysis/electrosynthesis, wastewater treatment, and contaminant bioremediation. Process performance depends on where electrode-derived or electrode-destined electrons enter the quinone, cytochrome, flavin, or ferredoxin network and how that transfer changes ATP yield. (kracke2015microbialelectrontransport pages 1-2)
4. **Environmental metabolic reconstruction.** Genome-resolved models use respiratory modules to predict syntrophy and energy conservation under tidal redox oscillations, although they require physiological validation. (laux2024livinginmangroves pages 1-2)
5. **Dormancy and persistence research.** Low-level nitrate respiration can maintain membrane potential without supporting growth, illustrating that the phenotype may manifest as viability or persistence rather than biomass increase. (sawers2019anaerobicnitraterespiration pages 1-2)

## Expert interpretation for TraitMech

The most defensible graph is **modular rather than a fixed mitochondrial “complex I–V” chain**. Authoritative bacterial work emphasizes branched respiratory architecture: multiple primary dehydrogenases and terminal oxidases are connected through a shared quinone pool, and individual branches differ in energetic efficiency and environmental function. (tsviklist2022thecpxstress pages 1-2, borisov2023cytochromebdas pages 1-3)

Accordingly, the YAML should contain:

- a **minimal invariant spine**: donor oxidation → membrane electron transport → ion-gradient generation → ATP synthase → ATP;
- **alternative donor-entry branches** such as complex I, NDH-2, SDH, hydrogenase, or sulfur oxidoreductase;
- **alternative terminal branches** such as heme-copper oxidase, cytochrome bd, Nar, or other terminal reductases;
- an explicit **coupling-ion branch**, H⁺ by default and Na⁺ only when supported;
- separate representations of **capacity**, **activity**, and **inhibition**.

This avoids two common errors: requiring every bacterium to possess mitochondrial complexes I–IV, and treating every detected respiratory enzyme as a direct proton pump.

## Warnings: claims not yet ready for curation

1. **Do not curate a universal five-complex pathway.** Many bacteria and archaea lack one or more canonical complexes or use unrelated alternatives.
2. **Do not assert that NDH-2 or SDH pumps protons.** The cited *E. coli* and mycobacterial evidence identifies them as electron-entry enzymes but not direct PMF generators. (borisov2023cytochromebdas pages 1-3, bajeli2020terminalrespiratoryoxidases pages 1-2)
3. **Do not encode cytochrome bd as a classical proton pump.** It contributes to PMF but does not pump vectorial protons in the mycobacterial evidence. (bajeli2020terminalrespiratoryoxidases pages 1-2)
4. **Do not infer oxidative phosphorylation from oxygen consumption alone.** Respiration may be uncoupled, may support redox balancing, or may be redirected between terminal oxidases. (harrison2024remissionspectroscopyresolves pages 1-4)
5. **Do not infer active phenotype from gene presence or a MAG reconstruction alone.** Require transcript, protein, flux, electrochemical, ATP, growth, or inhibitor evidence for an observed trait.
6. **Do not use nitrate reduction as a universal growth-supporting edge.** In *S. coelicolor*, nitrate respiration maintained an ion gradient during non-growth; Nar1 coupling to the bcc–aa₃ Q-cycle was proposed rather than conclusively demonstrated. (sawers2019anaerobicnitraterespiration pages 1-2)
7. **Do not generalize Na⁺ coupling.** Na⁺-NQR and Na⁺-coupled ATP synthases require organism-specific evidence; external alkalinity alone does not prove sodium energetics. (mulkidjanian2008thepastand pages 1-2)
8. **Do not merge photophosphorylation with respiratory oxidative phosphorylation.** Homologous Q-cycle chemistry does not erase the difference between light-driven and respiratory electron input. (kao2022quinonebindingsites pages 1-3)
9. **Do not curate the 2024 bedaquiline flux-redirection result as settled consensus.** It is a valuable live-cell result but was retrieved as a preprint. (harrison2024remissionspectroscopyresolves pages 1-4)
10. **Validate ontology identifiers before import.** In particular, PMF, respiratory-chain complexes, A/V-type ATP synthases, menaquinone species, and sodium-motive force should remain label-only if exact ontology records have not been checked. EC identifiers describe catalytic activities and should not be used as substitutes for complex or process ontology terms.

## DOI-first bibliography

1. **Grivennikova VG et al.** “Proton-Translocating NADH–Ubiquinone Oxidoreductase: Interaction with Artificial Electron Acceptors, Inhibitors, and Potential Medicines.” *International Journal of Molecular Sciences* 25, 13421. **Published 14 December 2024.** DOI: [10.3390/ijms252413421](https://doi.org/10.3390/ijms252413421). (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)
2. **Harrison SH et al.** “Remission spectroscopy resolves the mode of action of bedaquiline within living mycobacteria.” *bioRxiv*. **December 2024; preprint.** DOI: [10.1101/2024.12.03.626386](https://doi.org/10.1101/2024.12.03.626386). (harrison2024remissionspectroscopyresolves pages 1-4)
3. **Laux M et al.** “Living in mangroves: a syntrophic scenario unveiling a resourceful microbiome.” *BMC Microbiology* 24, 228. **Published June 2024.** DOI: [10.1186/s12866-024-03390-6](https://doi.org/10.1186/s12866-024-03390-6). (laux2024livinginmangroves pages 1-2)
4. **Zharova TV, Grivennikova VG, Borisov VB.** “F1·Fo ATP Synthase/ATPase: Contemporary View on Unidirectional Catalysis.” *International Journal of Molecular Sciences* 24, 5417. **Published 12 March 2023.** DOI: [10.3390/ijms24065417](https://doi.org/10.3390/ijms24065417). (zharova2023f1·foatpsynthaseatpase pages 1-2)
5. **Borisov VB, Nastasi MR, Forte E.** “Cytochrome bd as Antioxidant Redox Enzyme.” *Molecular Biology* 57, 1077–1084. **Accepted 1 June 2023; published 2023.** DOI: [10.1134/S0026893323060031](https://doi.org/10.1134/S0026893323060031). (borisov2023cytochromebdas pages 1-3)
6. **Frasch WD, Bukhari ZA, Yanagisawa S.** “F1FO ATP synthase molecular motor mechanisms.” *Frontiers in Microbiology* 13, 965620. **Published 23 August 2022.** DOI: [10.3389/fmicb.2022.965620](https://doi.org/10.3389/fmicb.2022.965620). (frasch2022f1foatpsynthase pages 1-2)
7. **Kao W-C, Hunte C.** “Quinone binding sites of cyt bc complexes analysed by X-ray crystallography and cryogenic electron microscopy.” *Biochemical Society Transactions* 50, 877–893. **Published 31 March 2022.** DOI: [10.1042/BST20190963](https://doi.org/10.1042/BST20190963). (kao2022quinonebindingsites pages 1-3)
8. **Tsviklist V, Guest RL, Raivio TL.** “The Cpx Stress Response Regulates Turnover of Respiratory Chain Proteins at the Inner Membrane of Escherichia coli.” *Frontiers in Microbiology* 12, 732288. **Published 28 January 2022.** DOI: [10.3389/fmicb.2021.732288](https://doi.org/10.3389/fmicb.2021.732288). (tsviklist2022thecpxstress pages 1-2)
9. **Bajeli S et al.** “Terminal Respiratory Oxidases: A Targetable Vulnerability of Mycobacterial Bioenergetics?” *Frontiers in Cellular and Infection Microbiology* 10, 589318. **Published 23 November 2020.** DOI: [10.3389/fcimb.2020.589318](https://doi.org/10.3389/fcimb.2020.589318). (bajeli2020terminalrespiratoryoxidases pages 1-2)
10. **Sawers RG, Fischer M, Falke D.** “Anaerobic nitrate respiration in the aerobe Streptomyces coelicolor A3(2): helping maintain a proton gradient during dormancy.” *Environmental Microbiology Reports* 11, 645–650. **Published 2019.** DOI: [10.1111/1758-2229.12781](https://doi.org/10.1111/1758-2229.12781). (sawers2019anaerobicnitraterespiration pages 1-2)
11. **Kühlbrandt W.** “Structure and Mechanisms of F-Type ATP Synthases.” *Annual Review of Biochemistry* 88, 515–549. **Published 2019.** DOI: [10.1146/annurev-biochem-013118-110903](https://doi.org/10.1146/annurev-biochem-013118-110903). (kuhlbrandt2019structureandmechanisms pages 1-2)
12. **Müller V, Chowdhury NP, Basen M.** “Electron Bifurcation: A Long-Hidden Energy-Coupling Mechanism.” *Annual Review of Microbiology* 72, 331–353. **Published 2018.** DOI: [10.1146/annurev-micro-090816-093440](https://doi.org/10.1146/annurev-micro-090816-093440). (muller2018electronbifurcationa pages 1-2)
13. **Kracke F, Vassilev I, Krömer JO.** “Microbial electron transport and energy conservation—the foundation for optimizing bioelectrochemical systems.” *Frontiers in Microbiology* 6, 575. **Published 11 June 2015.** DOI: [10.3389/fmicb.2015.00575](https://doi.org/10.3389/fmicb.2015.00575). (kracke2015microbialelectrontransport pages 1-2)
14. **Junge W, Nelson N.** “ATP Synthase.” *Annual Review of Biochemistry* 84, 631–657. **Published 2015.** DOI: [10.1146/annurev-biochem-060614-034124](https://doi.org/10.1146/annurev-biochem-060614-034124). (junge2015atpsynthase. pages 1-2)
15. **Mulkidjanian AY, Dibrov P, Galperin MY.** “The past and present of sodium energetics: May the sodium-motive force be with you.” *Biochimica et Biophysica Acta—Bioenergetics* 1777, 985–992. **Available online 27 April 2008.** DOI: [10.1016/j.bbabio.2008.04.028](https://doi.org/10.1016/j.bbabio.2008.04.028). (mulkidjanian2008thepastand pages 1-2)

## Recommended minimal graph

For the first revision of `data/traits/metabolism/oxidative_phosphorylation.yaml`, the safest minimal causal path is:

**electron donor → primary dehydrogenase → quinone/quinol pool → terminal oxidase or reductase → transmembrane H⁺/Na⁺ electrochemical gradient → F-type or A/V-type ATP synthase → ATP**.

Add complex I, SDH, bc/bcc, cytochrome bd, heme-copper oxidase, Nar, and Na⁺-NQR as optional mechanistic branches with taxon and environmental qualifiers. Keep inhibitor, assay, stress-response, and biotechnology nodes in contextual subgraphs rather than in the invariant trait spine.

References

1. (tsviklist2022thecpxstress pages 1-2): Valeria Tsviklist, Randi L. Guest, and Tracy L. Raivio. The cpx stress response regulates turnover of respiratory chain proteins at the inner membrane of escherichia coli. Frontiers in Microbiology, Jan 2022. URL: https://doi.org/10.3389/fmicb.2021.732288, doi:10.3389/fmicb.2021.732288. This article has 33 citations and is from a peer-reviewed journal.

2. (zharova2023f1·foatpsynthaseatpase pages 1-2): Tatyana V. Zharova, Vera G. Grivennikova, and Vitaliy B. Borisov. F1·fo atp synthase/atpase: contemporary view on unidirectional catalysis. International Journal of Molecular Sciences, 24:5417, Mar 2023. URL: https://doi.org/10.3390/ijms24065417, doi:10.3390/ijms24065417. This article has 58 citations.

3. (sawers2019anaerobicnitraterespiration pages 1-2): R. Gary Sawers, Marco Fischer, and Dörte Falke. Anaerobic nitrate respiration in the aerobe streptomyces coelicolor a3(2): helping maintain a proton gradient during dormancy. Environmental microbiology reports, 11:645-650, Oct 2019. URL: https://doi.org/10.1111/1758-2229.12781, doi:10.1111/1758-2229.12781. This article has 24 citations and is from a peer-reviewed journal.

4. (kao2022quinonebindingsites pages 1-3): Wei-Chun Kao and Carola Hunte. Quinone binding sites of cyt bc complexes analysed by x-ray crystallography and cryogenic electron microscopy. Biochemical Society Transactions, 50:877-893, Mar 2022. URL: https://doi.org/10.1042/bst20190963, doi:10.1042/bst20190963. This article has 24 citations and is from a peer-reviewed journal.

5. (muller2018electronbifurcationa pages 1-2): Volker Müller, Nilanjan Pal Chowdhury, and Mirko Basen. Electron bifurcation: a long-hidden energy-coupling mechanism. Annual review of microbiology, 72:331-353, Sep 2018. URL: https://doi.org/10.1146/annurev-micro-090816-093440, doi:10.1146/annurev-micro-090816-093440. This article has 186 citations and is from a peer-reviewed journal.

6. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 10 citations.

7. (bajeli2020terminalrespiratoryoxidases pages 1-2): Sapna Bajeli, Navin Baid, Manjot Kaur, Ganesh P. Pawar, Vinod D. Chaudhari, and Ashwani Kumar. Terminal respiratory oxidases: a targetables vulnerability of mycobacterial bioenergetics? Frontiers in Cellular and Infection Microbiology, Nov 2020. URL: https://doi.org/10.3389/fcimb.2020.589318, doi:10.3389/fcimb.2020.589318. This article has 53 citations.

8. (borisov2023cytochromebdas pages 1-3): V. B. Borisov, M. R. Nastasi, and E. Forte. Cytochrome bd as antioxidant redox enzyme. Molecular Biology, 57:1077-1084, Sep 2023. URL: https://doi.org/10.1134/s0026893323060031, doi:10.1134/s0026893323060031. This article has 18 citations and is from a peer-reviewed journal.

9. (mulkidjanian2008thepastand pages 1-2): Armen Y. Mulkidjanian, Pavel Dibrov, and Michael Y. Galperin. The past and present of sodium energetics: may the sodium-motive force be with you. Biochimica et biophysica acta, 1777 7-8:985-92, Jul 2008. URL: https://doi.org/10.1016/j.bbabio.2008.04.028, doi:10.1016/j.bbabio.2008.04.028. This article has 213 citations.

10. (frasch2022f1foatpsynthase pages 1-2): Wayne D. Frasch, Zain A. Bukhari, and Seiga Yanagisawa. F1fo atp synthase molecular motor mechanisms. Frontiers in Microbiology, Aug 2022. URL: https://doi.org/10.3389/fmicb.2022.965620, doi:10.3389/fmicb.2022.965620. This article has 45 citations and is from a peer-reviewed journal.

11. (harrison2024remissionspectroscopyresolves pages 1-4): Suzanna H. Harrison, Rowan C Walters, Chen-Yi Cheung, Roger J Springett, Gregory M. Cook, Morwan M. Osman, and J. N. Blaza. Remission spectroscopy resolves the mode of action of bedaquiline within living mycobacteria. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.03.626386, doi:10.1101/2024.12.03.626386. This article has 1 citations.

12. (junge2015atpsynthase. pages 1-2): Wolfgang Junge and Nathan Nelson. Atp synthase. Annual review of biochemistry, 84:631-57, Jun 2015. URL: https://doi.org/10.1146/annurev-biochem-060614-034124, doi:10.1146/annurev-biochem-060614-034124. This article has 514 citations and is from a domain leading peer-reviewed journal.

13. (kracke2015microbialelectrontransport pages 1-2): Frauke Kracke, Igor Vassilev, and Jens O. KrÃ¶mer. Microbial electron transport and energy conservation – the foundation for optimizing bioelectrochemical systems. Frontiers in Microbiology, Jun 2015. URL: https://doi.org/10.3389/fmicb.2015.00575, doi:10.3389/fmicb.2015.00575. This article has 892 citations and is from a peer-reviewed journal.

14. (sorescu2025breakthroughsinthe pages 24-25): Jennifer M. Sorescu, Martín A. González-Montalvo, Ming Yuan, Joseph De Paolo-Boisvert, Corina Diana Ceapă, Rodolfo Garcia-Contreras, Oscar Flores-Herrera, Michael E. Shea, Karina Tuz, and Oscar X. Juárez. Breakthroughs in the development of antibiotics, antifungals and antiparasitics targeting the pathogens’ respiratory chain. Critical Reviews in Biochemistry and Molecular Biology, 60(4-6):141-174, Aug 2025. URL: https://doi.org/10.1080/10409238.2025.2545785, doi:10.1080/10409238.2025.2545785. This article has 7 citations and is from a peer-reviewed journal.

15. (laux2024livinginmangroves pages 1-2): Marcele Laux, Luciane Prioli Ciapina, Fabíola Marques de Carvalho, Alexandra Lehmkuhl Gerber, Ana Paula C. Guimarães, Moacir Apolinário, Jorge Eduardo Santos Paes, Célio Roberto Jonck, and Ana Tereza R. de Vasconcelos. Living in mangroves: a syntrophic scenario unveiling a resourceful microbiome. BMC Microbiology, Jun 2024. URL: https://doi.org/10.1186/s12866-024-03390-6, doi:10.1186/s12866-024-03390-6. This article has 17 citations and is from a peer-reviewed journal.

16. (kuhlbrandt2019structureandmechanisms pages 1-2): Werner Kühlbrandt. Structure and mechanisms of f-type atp synthases. Annual review of biochemistry, 88:515-549, Jun 2019. URL: https://doi.org/10.1146/annurev-biochem-013118-110903, doi:10.1146/annurev-biochem-013118-110903. This article has 524 citations and is from a domain leading peer-reviewed journal.