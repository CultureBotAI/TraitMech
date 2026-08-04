---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:09:06.079710'
end_time: '2026-08-04T00:18:43.845393'
duration_seconds: 577.77
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cadmium tolerant
  trait_identifier: traitmech:000013
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: cadmium_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metal tolerance in which an organism grows in the presence of elevated
    cadmium (Cd2+) concentrations, typically via cation-efflux resistance systems
    such as the czc determinant.
  parent_traits: traitmech:000012
  synonyms: ''
  evidence_summary: 'DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition
    metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system
    of Cupriavidus metallidurans confers cadmium resistance.) | DOI:10.3389/fmicb.2020.00047:
    C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+
    (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and
    Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cadmium
    to a MIC of 2.5 mM.)'
  causal_graph_summary: 'cadmium_tolerance_czc_efflux: 8 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cadmium tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000013
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated cadmium (Cd2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers cadmium resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cadmium to a MIC of 2.5 mM.)
- **Existing causal graph summary:** cadmium_tolerance_czc_efflux: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **cadmium tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/cadmium_tolerant.yaml`.

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
- **Trait label:** cadmium tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000013
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated cadmium (Cd2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers cadmium resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cadmium to a MIC of 2.5 mM.)
- **Existing causal graph summary:** cadmium_tolerance_czc_efflux: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **cadmium tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/cadmium_tolerant.yaml`.

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


# Curation-focused research report: microbial cadmium tolerance

## Record under review

- **Trait label:** cadmium tolerant
- **Trait identifier:** `traitmech:000013`
- **Category / kind:** ENVIRONMENT / CLASS
- **Mapping status:** REVIEWED
- **Parent:** `traitmech:000012`
- **Recommended mechanistic interpretation:** growth or sustained survival during elevated, bioavailable Cd(II) exposure because cellular cadmium burden is limited by regulated export and, in some taxa, sequestration, surface exclusion, biofilm formation, or mineral precipitation.

## 1. Scope summary

### Operational phenotype

`traitmech:000013` should denote an **assay-observed capacity to grow, maintain viability, or resume growth at an elevated concentration of bioavailable Cd(II)** relative to an appropriate control or susceptible reference. The record should preserve the Cd salt, nominal concentration, medium composition, pH, inoculum density, exposure time, temperature, and endpoint—MIC, growth rate, lag time, colony formation, or survival.

This assay context is essential. In a 2024 study, phosphate in standard mineral-salts medium precipitated cadmium, while rich media also became opaque after cadmium addition. A phosphate-eliminated modified medium was therefore used. The same study found that measured MIC increased with initial cell density, showing that a nominal “cadmium MIC” is not an organism-invariant quantity (chatterjee2024multimodalcadmiumresistance pages 14-15).

### Included cases

- Reproducible growth or survival under dissolved Cd(II), including inducible tolerance.
- Mechanisms that causally lower cytoplasmic or periplasmic Cd burden and thereby preserve growth.
- Taxon-specific combinations of inner-membrane export, trans-envelope export, buffering, biofilm protection, or mineralization when linked to the growth phenotype.

### Boundary cases

1. **Resistance gene present ≠ cadmium-tolerant phenotype.** Annotation of `cadA`, `zntA`, or `czcCBA` without expression, transport, mutant, or growth evidence is insufficient.
2. **Biosorption ≠ tolerance.** Passive binding by dead biomass or cell surfaces can remove Cd from solution without supporting growth.
3. **Bioaccumulation ≠ tolerance.** Intracellular uptake may accompany detoxification, but it may also increase toxicity.
4. **Biomineralization ≠ tolerance unless growth is shown.** CdS or CdCO3 formation is a removal phenotype that should connect to `traitmech:000013` only where it improves survival or growth.
5. **Transient survival ≠ growth tolerance.** Short-term viability should be represented separately or qualified by the assay.
6. **Broad metal tolerance is not automatically cadmium tolerance.** Czc systems frequently handle Zn(II) and Co(II) as well as Cd(II); substrate and phenotype evidence must remain metal-specific.

## 2. Current mechanistic understanding

The strongest experimentally supported architecture is a **layered efflux pathway** in Gram-negative *Cupriavidus/Ralstonia metallidurans*. CadA and ZntA are PIB2-type P-type ATPases that use ATP to move surplus cytoplasmic Cd(II) into the periplasm. CzcCBA is an RND-family trans-envelope complex—CzcA pump, CzcB membrane-fusion protein, and CzcC outer-membrane factor—that exports substrate from the periplasm to the extracellular environment (legatzki2003interplayofthe pages 1-2, schulz2024theeffluxsystem pages 1-3).

The genetic evidence shows that these layers cooperate rather than act as interchangeable standalone explanations. In plasmid-free strain AE104, deleting either `cadA` or `zntA` had only moderate effects, whereas double disruption reduced cadmium resistance approximately **350-fold**. Supplying CzcCBA only partially restored cadmium resistance to the double mutant, indicating that full detoxification requires CzcCBA plus at least one cytoplasm-to-periplasm P-type ATPase (legatzki2003interplayofthe pages 1-2). The associated MIC table reports 350 µM Cd for plasmid-free AE104 and 3,000 µM after introduction of `czcCBAD` or `czcCBADRS`; the complete wild-type resistance complement was described as operating in the millimolar range (legatzki2003interplayofthe pages 3-4, legatzki2003interplayofthe pages 1-2).

Recent work refines this into an **adaptively layered metal-homeostasis network**. In *C. metallidurans*, CadA is regulated by CadR, while ZntA is regulated by ZntR. ZntA and CadA transport Zn(II) and Cd(II) with similar in-vitro kinetic parameters and can partially substitute for one another. The adjacent CDF-family protein CdfX is induced by zinc and cadmium through ZntR, but direct isotope pulse–chase evidence in that study established CdfX as a **zinc** exporter; the authors conclude that the `cdfX-cadA` region backs up ZntA with CdfX exporting zinc and CadA exporting cadmium (schulz2024theeffluxsystem pages 1-3). CdfX should therefore not be curated as a Cd exporter.

The strongest core chain is summarized below.

| Subject | Predicate | Object | Evidence strength | Key qualification |
|---|---|---|---|---|
| Elevated extracellular Cd(II) | induces expression of | cadA | Strong | In *Ralstonia/Cupriavidus metallidurans*, “expression of **cadA was induced by cadmium but not by zinc**”; induction shifts in the absence of *zntA*, so regulation is context-dependent (legatzki2003interplayofthe pages 1-2) |
| Elevated extracellular Cd(II) | induces expression of | zntA | Strong | In *R./C. metallidurans*, “**expression of zntA was induced by both zinc and cadmium**” (legatzki2003interplayofthe pages 1-2) |
| CadA | decreases cellular Cd(II) by exporting | cytoplasmic Cd(II) to the periplasm | Strong | Primary transport direction supported by mechanistic description that “**P-type ATPases hydrolyze ATP**” and “**transport their substrates from the cytoplasm to the periplasm**”; CadA/ZntA expression in *E. coli* also “**decreased the cellular content of…cadmium**” (legatzki2003interplayofthe pages 1-2, schulz2024theeffluxsystem pages 1-3) |
| ZntA | decreases cellular Cd(II) by exporting | cytoplasmic Cd(II) to the periplasm | Strong | Same directional support as above; 2024 work states “**The PIB2-type ATPases ZntA and CadA transport Zn(II) and Cd(II) in vitro with similar kinetic parameters and substitute each other**” (legatzki2003interplayofthe pages 1-2, schulz2024theeffluxsystem pages 1-3) |
| CzcCBA efflux complex | exports | periplasmic Cd(II) to the extracellular medium | Strong | Foundational and 2024 sources agree that CzcCBA is a transenvelope exporter: “**required to transport substrate directly to the extracellular medium**” and “**export their substrate cations from the periplasm to the environment outside of the cell**” (legatzki2003interplayofthe pages 1-2, schulz2024theeffluxsystem pages 1-3) |
| CadA/ZntA | functionally cooperate with | CzcCBA | Strong | Genetic interaction evidence: “**needs both CzcCBA and at least one P-type ATPase for an effective detoxification of cadmium**”; CzcCBA only partially restores cadmium resistance in the *cadA zntA* double mutant (legatzki2003interplayofthe pages 1-2) |
| Reduced intracellular Cd(II) burden via CadA/ZntA plus CzcCBA | supports | cadmium-tolerant growth | Strong | Supported by mutant/MIC evidence: in plasmid-free *R./C. metallidurans* single deletions had moderate effects, but “**cadmium resistance decreased 350-fold in double deletion strains**”; with full plasmid determinants, wild-type cadmium MICs were in the mM range while double mutants were far lower (legatzki2003interplayofthe pages 1-2, legatzki2003interplayofthe pages 3-4) |


*Table: This table summarizes the most strongly supported causal edges for microbial cadmium tolerance, prioritizing primary experimental genetics and transport evidence. It is useful as a compact starting point for TraitMech curation because it separates high-confidence transport steps from broader or more speculative regulatory details.*

## 3. Candidate nodes grouped by type

### Trait and assay nodes

| Candidate node | Proposed grounding | Curation note |
|---|---|---|
| cadmium tolerant | `traitmech:000013` | Target phenotype; quote the CURIE exactly. |
| elevated bioavailable Cd(II) exposure | **CHEBI:48775** candidate for cadmium(2+); environmental-exposure node otherwise label-only | Validate the ChEBI release before committing. Record Cd salt and speciation separately. |
| growth in elevated Cd(II) | Label-only assay/process node | Prefer measured growth or MIC over “resistant” in prose. |
| cadmium MIC | Label-only measurement node | Store medium, pH, inoculum, duration, and endpoint as qualifiers. |
| reduced intracellular Cd burden | Label-only state node | Useful mediator between transport and growth tolerance. |

### Genes, proteins, and complexes

| Node | Type and role | Recommended status |
|---|---|---|
| `cadA` / CadA | PIB2-type P-type ATPase; predominantly Cd-exporting inner-membrane transporter | **Core** |
| `zntA` / ZntA | PIB2-type ATPase with Zn/Cd transport; partially redundant with CadA | **Core but taxon-qualified** |
| `cadR` / CadR | MerR-family regulator controlling `cadA` | **Core in organisms where experimentally established** |
| `zntR` / ZntR | MerR-family regulator controlling `zntA`; also controls `cdfX` in *C. metallidurans* | Supporting node |
| `czcA` / CzcA | RND-family inner-membrane cation/proton antiporter component | **Core** |
| `czcB` / CzcB | Periplasm-spanning membrane-fusion/adaptor component | **Core** |
| `czcC` / CzcC | Outer-membrane factor | **Core** |
| CzcCBA complex | Trans-envelope Co/Zn/Cd efflux complex | **Core** |
| `czcD` / CzcD | CDF-family inner-membrane transporter and regulatory contributor | Optional; function and direction are system-dependent |
| `czcS` / CzcS | Sensor histidine kinase in CzcRS | Taxon-specific; Cd-sensing edge is uncertain in strain CD3 |
| `czcR` / CzcR | Response regulator activating `czcCBA` transcription | Taxon-specific |
| `bfmS`, `bfmR` | Biofilm-associated two-component system proposed to coordinate biofilm and Czc responses in *P. aeruginosa* CD3 | **Do not place in the generic core graph yet** |
| `cdfX` / CdfX | CDF-family zinc exporter induced by Zn/Cd | Do not curate as Cd export |
| metallothionein / cysteine-rich proteins | Intracellular Cd-binding or buffering proteins | Mechanism class; require protein-specific evidence |

### Chemicals, energy, and molecular functions

- Cd(II), Zn(II), Co(II), ATP, ADP, phosphate, protons/proton motive force, glutathione, polyphosphate, thiolate-bound cadmium, CdS, and CdCO3/otavite.
- ATP hydrolysis drives CadA/ZntA transport, whereas the RND pump uses chemiosmotic coupling; foundational evidence explicitly distinguishes ATP-driven P-type ATPases from gradient-driven CDF/RND transport (legatzki2003interplayofthe pages 1-2).
- Cytoplasmic glutathione and polyphosphate contribute to metal buffering and homeostatic flow, but a direct cadmium-tolerance edge should be added only with Cd-specific perturbation evidence (schulz2024theeffluxsystem pages 1-3).

### Cellular locations

- Extracellular environment
- Outer membrane
- Periplasm
- Inner/cytoplasmic membrane
- Cytoplasm
- Cell surface, extracellular polymeric substance, and biofilm matrix

Because the retrieved papers provide labels rather than formal ontology accessions, these nodes should remain label-only until GO/ontology identifiers are checked against a current release. This is preferable to introducing an unverified CURIE (sharma2024mechanismsofmicrobial pages 12-13, olaya‐abril2024bacterialtoleranceand pages 9-10).

### Organisms and taxonomic scope

- *Cupriavidus metallidurans* CH34, formerly *Ralstonia metallidurans*: strongest causal-genetic foundation.
- *Pseudomonas aeruginosa* strain CD3: recent quantitative and multimodal case study.
- Other *Pseudomonas*, *Staphylococcus*, and engineered *Escherichia coli*: useful supporting systems, but edges should retain their taxon and construct context.

## 4. Candidate causal edges

Predicates below are intentionally simple and YAML-friendly. “Strong” denotes direct transport, expression, mutant, complementation, or quantitative physiological evidence; “moderate” denotes a supported mechanism lacking a clean perturbation-to-phenotype chain; “uncertain” denotes a proposed model or generalization.

| # | Subject–predicate–object triple | Evidence | Supporting snippet | Curation note |
|---:|---|---|---|---|
| 1 | elevated Cd(II) — **induces expression of** → `cadA` | Strong; *R./C. metallidurans* | “expression of cadA was induced by cadmium but not by zinc” (legatzki2003interplayofthe pages 1-2) | Curate with taxon. Induction specificity changes when `zntA` is absent. |
| 2 | elevated Cd(II) — **induces expression of** → `zntA` | Strong; *R./C. metallidurans* | “expression of zntA was induced by both zinc and cadmium” (legatzki2003interplayofthe pages 1-2) | Curate as cross-metal regulation, not Cd specificity. |
| 3 | CadR — **regulates expression of** → `cadA` | Strong/recent synthesis of established system | “Expression of the cadA gene is under the control of the MerR-type regulator CadR” (schulz2024theeffluxsystem pages 1-3) | Suitable for the *C. metallidurans* subgraph. |
| 4 | ATP hydrolysis by CadA — **drives transport of** → cytoplasmic Cd(II) to periplasm | Strong | P-type ATPases “hydrolyze ATP as their driving force” and transport substrates “from the cytoplasm to the periplasm” (legatzki2003interplayofthe pages 1-2) | Core directional edge. |
| 5 | CadA — **decreases** → cellular Cd content | Strong, heterologous transport | CadA/ZntA expression “decreased the cellular content of zinc or cadmium” (legatzki2003interplayofthe pages 1-2) | Connect to tolerance through the mutant evidence below. |
| 6 | ZntA — **transports** → Cd(II) from cytoplasm to periplasm | Strong | ZntA and CadA “transport Zn(II) and Cd(II) in vitro with similar kinetic parameters and substitute each other” (schulz2024theeffluxsystem pages 1-3) | Taxon-qualified; ZntA is often predominantly a Zn exporter. |
| 7 | CzcCBA — **exports** → periplasmic Cd(II) to extracellular environment | Strong | CzcCBA complexes “export their substrate cations from the periplasm to the environment outside of the cell” (schulz2024theeffluxsystem pages 1-3) | Core trans-envelope step. |
| 8 | CzcA — **uses cation/proton antiport to drive** → CzcCBA efflux | Strong mechanistic support | CzcA is described as the central RND cation/proton antiporter; RND complexes span the Gram-negative envelope (legatzki2003interplayofthe pages 6-7, legatzki2003interplayofthe pages 1-2) | Represent at complex level unless component-level detail is required. |
| 9 | CzcCBA activity — **decreases** → cytoplasmic Cd/Zn signal | Strong reporter evidence | CzcCBA diminished `cadA` and `zntA` induction, indicating that it “efficiently decreased cytoplasmic cadmium and zinc concentrations” (legatzki2003interplayofthe pages 1-2) | Useful feedback edge; mechanism may involve early periplasmic interception. |
| 10 | CadA or ZntA — **cooperates with** → CzcCBA | Strong genetic interaction | Full Cd resistance requires CzcCBA and at least one P-type ATPase; CzcCBA only partially elevated resistance in the double mutant (legatzki2003interplayofthe pages 6-7, legatzki2003interplayofthe pages 1-2) | Core systems-level edge. |
| 11 | deletion of `cadA` and `zntA` — **decreases** → cadmium tolerance | Strong mutant evidence | “cadmium resistance decreased 350-fold in double deletion strains” (legatzki2003interplayofthe pages 1-2) | Strongest genotype-to-trait edge. |
| 12 | reduced intracellular Cd burden — **enables** → growth at elevated Cd(II) | Strong composite inference | Transporters lower cellular Cd, and loss of both P-type ATPases sharply lowers resistance (legatzki2003interplayofthe pages 1-2) | Curatable as the bridge to `traitmech:000013`; note it is a synthesis across results. |
| 13 | low-dose Cd pre-exposure — **induces** → faster growth upon high-dose Cd challenge | Moderate; *P. aeruginosa* CD3 | Pre-exposed cells entered logarithmic growth earlier after transfer to 1.5 mM Cd (chatterjee2024multimodalcadmiumresistance pages 14-15) | Assay-specific inducible-tolerance edge. |
| 14 | 0.25 mM Zn pre-exposure — **reduces** → lag during subsequent Cd challenge | Moderate; CD3 | Zn induction had a larger effect than equal Cd on lag-phase reduction (chatterjee2024multimodalcadmiumresistance pages 14-15) | Cross-induction; avoid presenting Zn as a universal Cd-tolerance enhancer. |
| 15 | active efflux — **decreases** → intracellular Cd in CD3 | Moderate-to-strong physiological evidence | AAS measured 85.33 ppm extracellular and 13 ppm intracellular Cd after exposure (chatterjee2024multimodalcadmiumresistance pages 15-16, chatterjee2024multimodalcadmiumresistance pages 14-15) | AAS supports net export but not a specific pump by itself. |
| 16 | biofilm formation — **supports** → growth at ≤0.75 mM CdCl2·H2O | Moderate; CD3 | “Formation of biofilm enabled CD3 cells to resist up to 0.75 mM” (chatterjee2024multimodalcadmiumresistance pages 1-2) | Taxon-, dose-, and assay-specific. |
| 17 | Cd stress >1 mM — **increases dependence on** → efflux | Moderate-to-strong; CD3 | “Survival and growth…in presence of >1 mM…was dependent on efflux mechanism” (chatterjee2024multimodalcadmiumresistance pages 1-2) | Suitable as an experimental-condition edge. |
| 18 | periplasmic Cd — **activates** → CzcS→CzcR→`czcCBA` | **Uncertain**; CD3 model | The authors label the pathway “a hypothesized model”; CzcS autophosphorylation and subsequent steps were proposed in Figure 10 (chatterjee2024multimodalcadmiumresistance pages 17-19) | Do not place in the generic reviewed graph without direct phosphotransfer/expression evidence. |
| 19 | BfmR phosphorylation — **shifts resource allocation from** → biofilm to Czc efflux | **Uncertain** | Proposed low-Cd/high-Cd scenarios in the “hypothesized model” (chatterjee2024multimodalcadmiumresistance pages 17-19) | Not ready for TraitMech curation. |
| 20 | metallothionein binding of Cd — **reduces** → free cytoplasmic Cd | Moderate mechanism class | Cysteine-rich metallothioneins sequester Cd and lower free-ion quantities (chatterjee2024multimodalcadmiumresistance pages 1-2) | Require a named protein and perturbation before adding to the core graph. |
| 21 | EPS/biofilm — **promotes precipitation of** → CdS or CdCO3 | Moderate review-level evidence | Recent synthesis describes CdS granules/nanoparticles and otavite associated with biofilm/EPS (olaya‐abril2024bacterialtoleranceand pages 9-10) | Curate into a remediation/mineralization graph, not automatically into growth tolerance. |

## 5. Quantitative evidence and recent developments

### 2024 *P. aeruginosa* CD3 study

The study screened **26 cadmium-resistant isolates** and identified strain CD3 as capable of resistance up to **3 mM CdCl2·H2O** in the headline phenotype. Biofilm-associated protection extended to **0.75 mM**, whereas growth above **1 mM** depended on active efflux. Resistance was inducible at ≥1.0 mM CdCl2·H2O (chatterjee2024multimodalcadmiumresistance pages 1-2).

Under a modified phosphate-eliminated medium, five isolates tolerated nominal concentrations as high as **9 mM**, illustrating how medium chemistry and inoculum density can produce values different from the headline 3 mM result. This discrepancy should be preserved as assay metadata, not collapsed into one canonical MIC (chatterjee2024multimodalcadmiumresistance pages 14-15).

AAS measurements after exposure found **85.33 ppm extracellular Cd** and **13 ppm intracellular Cd**, consistent with active export. Nevertheless, the authors explicitly state that real-time efflux was not measured and that pump selectivity and much of the proposed regulatory network remain unresolved (chatterjee2024multimodalcadmiumresistance pages 15-16, chatterjee2024multimodalcadmiumresistance pages 17-19).

### 2024 *C. metallidurans* transporter study

Deletion and isotope pulse–chase experiments identified CdfX as residual Zn exporter activity in a strain lacking `zntA`, `cadA`, `dmeF`, and `fieF`. Cadmium induced `cdfX`, but the direct transport result was zinc efflux. The main Cd-relevant update is therefore regulatory and architectural: when Zn/Cd competition impairs ZntA, CadA provides a Cd-exporting backup while CdfX handles zinc (schulz2024theeffluxsystem pages 1-3).

### Foundational quantitative genetics

The 2003 study remains the strongest causal evidence for graph construction. Plasmid-free AE104 had a Cd MIC of approximately **350 µM**; provision of the Czc determinant raised it to **3,000 µM**. Double disruption of `cadA` and `zntA` reduced Cd resistance approximately **350-fold**, and CzcCBA could only partially compensate (legatzki2003interplayofthe pages 3-4, legatzki2003interplayofthe pages 1-2).

## 6. Applications and real-world implementation status

### Bioremediation and immobilization

Cadmium-tolerant microbes are being investigated for biosorption, intracellular sequestration, biofilm/EPS capture, and precipitation as CdS or CdCO3. These processes can reduce dissolved or bioavailable Cd, but their graph should be separated from the growth-tolerance graph unless improved growth is demonstrated (olaya‐abril2024bacterialtoleranceand pages 9-10).

### Engineered bioaccumulation

A 2023 synthetic-biology review reports engineered *E. coli* expressing trimeric human metallothionein-1A at **6.36 mg Cd²⁺ per g dry cell weight**, with co-expression of MntA producing a reported **25-fold enhancement**. These are engineered laboratory systems and should not be generalized to natural cadmium-tolerant taxa (thai2023syntheticbacteriafor pages 15-17).

### Whole-cell biosensors

Laboratory platforms include cadmium-responsive `cadR` promoters linked to fluorescent output, artificial `cad` operons, indigoidine reporters, dual Cd/Hg sensors, and engineered Cd chemotaxis. A *P. putida* design combined a `cadR` promoter–GFP sensor with a surface-displayed CadR Cd-binding domain for linked detection and capture (olaya‐abril2024bacterialtoleranceand pages 13-14, thai2023syntheticbacteriafor pages 19-19).

### Plant-associated remediation

Rhizosphere and endophytic metal-tolerant bacteria are proposed as inoculants that combine metal detoxification with plant-growth promotion. For TraitMech, however, plant-growth promotion, Cd mobilization for phytoextraction, and Cd immobilization for crop protection are distinct downstream outcomes. A bacterium that improves plant growth does not thereby demonstrate its own `traitmech:000013` phenotype.

### Implementation maturity and expert assessment

The retrieved recent reviews describe few practical synthetic-biology deployments and emphasize that most demonstrations remain laboratory-scale. Major obstacles include biosensor cross-reactivity and false positives, interference from complex environmental matrices, unpredictable scale-up of living systems, limited genetic toolkits for environmentally adapted non-model organisms, and ethical/legal restrictions on releasing engineered microbes. Reviews also suggest that natural or designed consortia may outperform single isolates in chemically complex waste streams, but that proposition is not yet a generic causal edge (thai2023syntheticbacteriafor pages 15-17, olaya‐abril2024bacterialtoleranceand pages 13-14).

No robust field-scale implementation of an engineered cadmium-tolerant strain was established in the retrieved evidence. The most defensible current application statement is therefore **laboratory-validated and environmentally promising, but not broadly field-deployed**.

## 7. Recommended graph architecture

### Minimal reviewed core

1. elevated bioavailable Cd(II)
2. Cd-responsive regulation (`cadR`/CadR and, where supported, `zntR`/ZntR)
3. increased CadA/ZntA abundance or activity
4. cytoplasmic Cd(II) → periplasmic Cd(II)
5. CzcCBA-mediated periplasmic Cd(II) → extracellular Cd(II)
6. reduced intracellular Cd burden
7. preserved growth at elevated Cd(II)
8. `traitmech:000013`

This core is preferable to a single “Czc determinant causes tolerance” edge because the genetic data show that CzcCBA and the P-type ATPases are functionally interdependent for full cadmium resistance (legatzki2003interplayofthe pages 6-7, legatzki2003interplayofthe pages 1-2).

### Optional taxon-specific branches

- **CD3 biofilm branch:** low/moderate Cd → biofilm → protection up to 0.75 mM.
- **CD3 inducible-efflux branch:** sublethal Cd or Zn pre-exposure → shorter lag during subsequent Cd challenge.
- ***C. metallidurans* adaptive-layering branch:** Zn/Cd competition at ZntA → activation of CadA/CdfX backup functions.
- **Sequestration branch:** metallothionein/thiol binding → lower free cytoplasmic Cd.
- **Biomineralization branch:** sulfur or carbonate metabolism → CdS/CdCO3 precipitation → lower dissolved Cd.

Only the first three have sufficiently specific recent evidence for provisional taxon-qualified edges; sequestration and mineralization require source-specific genes, perturbations, and growth outcomes.

## 8. Warnings: claims not yet ready for TraitMech

1. **Do not curate the full BfmS/BfmR–CzcS/CzcR cascade as established.** The CD3 paper explicitly calls it a hypothesized model and states that regulation across cadmium doses remains unknown (chatterjee2024multimodalcadmiumresistance pages 17-19).
2. **Do not curate CdfX as a cadmium exporter.** Cd regulates its expression, but isotope evidence supports Zn export; CadA is the Cd-specialized member of the backup region (schulz2024theeffluxsystem pages 1-3).
3. **Do not use a universal MIC.** Reported values depend strongly on medium precipitation, phosphate, pH, inoculum density, incubation conditions, and whether the endpoint is growth, survival, or induction (chatterjee2024multimodalcadmiumresistance pages 1-2, chatterjee2024multimodalcadmiumresistance pages 14-15).
4. **Do not infer mechanism from gene presence alone.** Genomic identification of `cadA`, `zntA`, `czc`, metallothionein, or EPS genes is weaker than deletion, complementation, expression, transport, or physiological evidence.
5. **Do not equate extracellular Cd with active efflux without controls.** Biosorption, precipitation, lysis, and medium chemistry can all raise the extracellular or cell-associated fraction.
6. **Do not merge tolerance with remediation efficiency.** A strain can tolerate Cd while exporting it back into solution and therefore remove little total Cd; conversely, dead biomass can remove Cd without being tolerant.
7. **Do not generalize Gram-negative compartment logic to Gram-positive organisms.** A periplasm-to-exterior CzcCBA step requires the Gram-negative envelope architecture.
8. **Do not treat Zn/Co induction as evidence of Cd specificity.** Cross-metal regulation is common and may reflect homeostatic competition rather than a dedicated Cd response.
9. **Do not claim field deployment from laboratory biosensor or batch-removal experiments.** Recent authoritative reviews emphasize scale-up, matrix, containment, and regulatory barriers (thai2023syntheticbacteriafor pages 15-17, olaya‐abril2024bacterialtoleranceand pages 13-14).

## 9. DOI-first bibliography

1. **Chatterjee S, et al.** “Multimodal cadmium resistance and its regulatory networking in *Pseudomonas aeruginosa* strain CD3.” *Scientific Reports* 14, 31689. **Published 18 December 2024.** DOI: [10.1038/s41598-024-80754-y](https://doi.org/10.1038/s41598-024-80754-y). Primary recent phenotype, AAS, induction, biofilm, genome, and proposed regulatory model (chatterjee2024multimodalcadmiumresistance pages 17-19, chatterjee2024multimodalcadmiumresistance pages 1-2).
2. **Schulz V, et al.** “The efflux system CdfX exports zinc that cannot be transported by ZntA in *Cupriavidus metallidurans*.” *Journal of Bacteriology* 206(11). **Published 30 October 2024.** DOI: [10.1128/jb.00299-24](https://doi.org/10.1128/jb.00299-24). Primary deletion, reporter, and isotope pulse–chase study (schulz2024theeffluxsystem pages 1-3).
3. **Olaya-Abril A, et al.** “Bacterial tolerance and detoxification of cyanide, arsenic and heavy metals: Holistic approaches applied to bioremediation of industrial complex wastes.” *Microbial Biotechnology* 17(1). **Published January 2024.** DOI: [10.1111/1751-7915.14399](https://doi.org/10.1111/1751-7915.14399). Authoritative synthesis of efflux, sequestration, mineralization, consortia, and synthetic biology (olaya‐abril2024bacterialtoleranceand pages 9-10, olaya‐abril2024bacterialtoleranceand pages 13-14).
4. **Sharma M, et al.** “Mechanisms of microbial resistance against cadmium—a review.” *Journal of Environmental Health Science and Engineering* 22:13–30. **2024 issue; DOI registered 2023.** DOI: [10.1007/s40201-023-00887-6](https://doi.org/10.1007/s40201-023-00887-6). Cadmium-specific synthesis (sharma2024mechanismsofmicrobial pages 12-13).
5. **Thai TD, Lim W, Na D.** “Synthetic bacteria for the detection and bioremediation of heavy metals.” *Frontiers in Bioengineering and Biotechnology* 11. **Published April 2023.** DOI: [10.3389/fbioe.2023.1178680](https://doi.org/10.3389/fbioe.2023.1178680). Synthetic biosensors, engineered accumulation, biosafety, and scale-up limitations (thai2023syntheticbacteriafor pages 15-17, thai2023syntheticbacteriafor pages 19-19).
6. **Legatzki A, Grass G, Anton A, Rensing C, Nies DH.** “Interplay of the Czc system and two P-type ATPases in conferring metal resistance to *Ralstonia metallidurans*.” *Journal of Bacteriology* 185:4354–4361. **Published August 2003.** DOI: [10.1128/JB.185.15.4354-4361.2003](https://doi.org/10.1128/JB.185.15.4354-4361.2003). Foundational mutant, complementation, reporter, cellular-metal, and MIC evidence (legatzki2003interplayofthe pages 3-4, legatzki2003interplayofthe pages 1-2).
7. **Scherer J, Nies DH.** “CzcP is a novel efflux system contributing to transition metal resistance in *Cupriavidus metallidurans* CH34.” *Molecular Microbiology* 73:601–621. **Published August 2009.** DOI: [10.1111/j.1365-2958.2009.06792.x](https://doi.org/10.1111/j.1365-2958.2009.06792.x). Relevant foundational source for the existing CzcP branch; the full paper was not independently extracted here, so new CzcP edges should retain the pre-existing evidence status rather than being expanded from secondary citation alone.

## Curation conclusion

The best-supported candidate graph for `traitmech:000013` is a compartment-resolved efflux chain centered on **CadR/CadA or ZntR/ZntA, followed by CzcCBA**, with reduced intracellular cadmium as the immediate physiological mediator of growth. The 2003 double-mutant and complementation results provide the strongest causal genotype-to-phenotype evidence, while 2024 studies add adaptive transporter layering, inducible tolerance, quantitative Cd partitioning, biofilm-associated protection, and a provisional regulatory model. Biofilm, metallothionein, EPS, and biomineralization branches should remain taxon- and assay-specific until direct perturbation evidence links them to growth under elevated Cd(II).

References

1. (chatterjee2024multimodalcadmiumresistance pages 14-15): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

2. (legatzki2003interplayofthe pages 1-2): Antje Legatzki, Gregor Grass, Andreas Anton, Christopher Rensing, and Dietrich H. Nies. Interplay of the czc system and two p-type atpases in conferring metal resistance to ralstonia metallidurans. Journal of Bacteriology, 185:4354-4361, Aug 2003. URL: https://doi.org/10.1128/jb.185.15.4354-4361.2003, doi:10.1128/jb.185.15.4354-4361.2003. This article has 190 citations and is from a peer-reviewed journal.

3. (schulz2024theeffluxsystem pages 1-3): Vladislava Schulz, Diana Galea, Grit Schleuder, Philipp Strohmeyer, Cornelia Große, Martin Herzberg, and Dietrich H. Nies. The efflux system cdfx exports zinc that cannot be transported by znta in <i>cupriavidus metallidurans</i>. Nov 2024. URL: https://doi.org/10.1128/jb.00299-24, doi:10.1128/jb.00299-24. This article has 8 citations and is from a peer-reviewed journal.

4. (legatzki2003interplayofthe pages 3-4): Antje Legatzki, Gregor Grass, Andreas Anton, Christopher Rensing, and Dietrich H. Nies. Interplay of the czc system and two p-type atpases in conferring metal resistance to ralstonia metallidurans. Journal of Bacteriology, 185:4354-4361, Aug 2003. URL: https://doi.org/10.1128/jb.185.15.4354-4361.2003, doi:10.1128/jb.185.15.4354-4361.2003. This article has 190 citations and is from a peer-reviewed journal.

5. (sharma2024mechanismsofmicrobial pages 12-13): Monu Sharma, Sonu Sharma, Paavan, Mahiti Gupta, Soniya Goyal, Daizee Talukder, Mohd. Sayeed Akhtar, Raman Kumar, Ahmad Umar, Abdulrab Ahmed M. Alkhanjaf, and Sotirios Baskoutas. Mechanisms of microbial resistance against cadmium - a review. Journal of environmental health science & engineering, 22 1:13-30, Dec 2024. URL: https://doi.org/10.1007/s40201-023-00887-6, doi:10.1007/s40201-023-00887-6. This article has 53 citations.

6. (olaya‐abril2024bacterialtoleranceand pages 9-10): Alfonso Olaya‐Abril, Karolina Biełło, Gema Rodríguez‐Caballero, Purificación Cabello, Lara P. Sáez, Conrado Moreno‐Vivián, Víctor Manuel Luque‐Almagro, and María Dolores Roldán. Bacterial tolerance and detoxification of cyanide, arsenic and heavy metals: holistic approaches applied to bioremediation of industrial complex wastes. Microbial Biotechnology, Jan 2024. URL: https://doi.org/10.1111/1751-7915.14399, doi:10.1111/1751-7915.14399. This article has 42 citations and is from a peer-reviewed journal.

7. (legatzki2003interplayofthe pages 6-7): Antje Legatzki, Gregor Grass, Andreas Anton, Christopher Rensing, and Dietrich H. Nies. Interplay of the czc system and two p-type atpases in conferring metal resistance to ralstonia metallidurans. Journal of Bacteriology, 185:4354-4361, Aug 2003. URL: https://doi.org/10.1128/jb.185.15.4354-4361.2003, doi:10.1128/jb.185.15.4354-4361.2003. This article has 190 citations and is from a peer-reviewed journal.

8. (chatterjee2024multimodalcadmiumresistance pages 15-16): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

9. (chatterjee2024multimodalcadmiumresistance pages 1-2): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

10. (chatterjee2024multimodalcadmiumresistance pages 17-19): Soumya Chatterjee, Partha Barman, Chandan Barman, Sukanta Majumdar, and Ranadhir Chakraborty. Multimodal cadmium resistance and its regulatory networking in pseudomonas aeruginosa strain cd3. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80754-y, doi:10.1038/s41598-024-80754-y. This article has 21 citations and is from a peer-reviewed journal.

11. (thai2023syntheticbacteriafor pages 15-17): Thi Duc Thai, Wonseop Lim, and Dokyun Na. Synthetic bacteria for the detection and bioremediation of heavy metals. Frontiers in Bioengineering and Biotechnology, Apr 2023. URL: https://doi.org/10.3389/fbioe.2023.1178680, doi:10.3389/fbioe.2023.1178680. This article has 91 citations.

12. (olaya‐abril2024bacterialtoleranceand pages 13-14): Alfonso Olaya‐Abril, Karolina Biełło, Gema Rodríguez‐Caballero, Purificación Cabello, Lara P. Sáez, Conrado Moreno‐Vivián, Víctor Manuel Luque‐Almagro, and María Dolores Roldán. Bacterial tolerance and detoxification of cyanide, arsenic and heavy metals: holistic approaches applied to bioremediation of industrial complex wastes. Microbial Biotechnology, Jan 2024. URL: https://doi.org/10.1111/1751-7915.14399, doi:10.1111/1751-7915.14399. This article has 42 citations and is from a peer-reviewed journal.

13. (thai2023syntheticbacteriafor pages 19-19): Thi Duc Thai, Wonseop Lim, and Dokyun Na. Synthetic bacteria for the detection and bioremediation of heavy metals. Frontiers in Bioengineering and Biotechnology, Apr 2023. URL: https://doi.org/10.3389/fbioe.2023.1178680, doi:10.3389/fbioe.2023.1178680. This article has 91 citations.