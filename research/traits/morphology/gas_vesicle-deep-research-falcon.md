---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:28:43.737297'
end_time: '2026-08-04T08:35:28.141821'
duration_seconds: 404.4
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: gas vesicle
  trait_identifier: traitmech:000070
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: gas_vesicle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An intracellular gas-filled proteinaceous inclusion that provides buoyancy,
    allowing planktonic bacteria and archaea to position themselves in the water column.
  parent_traits: traitmech:000066
  synonyms: gas vacuole
  evidence_summary: 'DOI:10.1038/nrmicro2834:  (Pfeifer describes gas vesicles as
    intracellular gas-filled proteinaceous flotation structures in bacteria and archaea.)
    | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include gas vesicles among
    bacterial intracellular organelles.)'
  causal_graph_summary: 'gas_vesicle_buoyancy: 13 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gas vesicle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000070
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular gas-filled proteinaceous inclusion that provides buoyancy, allowing planktonic bacteria and archaea to position themselves in the water column.
- **Parent traits:** traitmech:000066
- **Synonyms:** gas vacuole
- **Existing evidence:** DOI:10.1038/nrmicro2834:  (Pfeifer describes gas vesicles as intracellular gas-filled proteinaceous flotation structures in bacteria and archaea.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include gas vesicles among bacterial intracellular organelles.)
- **Existing causal graph summary:** gas_vesicle_buoyancy: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **gas vesicle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gas_vesicle.yaml`.

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
- **Trait label:** gas vesicle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000070
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular gas-filled proteinaceous inclusion that provides buoyancy, allowing planktonic bacteria and archaea to position themselves in the water column.
- **Parent traits:** traitmech:000066
- **Synonyms:** gas vacuole
- **Existing evidence:** DOI:10.1038/nrmicro2834:  (Pfeifer describes gas vesicles as intracellular gas-filled proteinaceous flotation structures in bacteria and archaea.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include gas vesicles among bacterial intracellular organelles.)
- **Existing causal graph summary:** gas_vesicle_buoyancy: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **gas vesicle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gas_vesicle.yaml`.

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


# Curation report: gas vesicle

**Trait:** `traitmech:000070`  
**Category:** MORPHOLOGY | **Term kind:** CLASS | **Mapping:** REVIEWED  
**Parent:** `traitmech:000066`  
**Recommended primary label:** gas vesicle  
**Synonym retained with qualification:** gas vacuole

## 1. Scope and current understanding

A gas vesicle is an intracellular, gas-filled, lipid-free protein nanostructure produced by phylogenetically diverse bacteria and archaea. Its shell admits dissolved gases but excludes liquid water, thereby creating a low-density compartment that can increase cellular buoyancy. Typical vesicles are cylindrical or spindle-shaped, approximately 100–250 nm wide and up to 2 µm long; an estimated 3–10% of cell volume must be occupied by vesicles to confer buoyancy under the conditions summarized by Pfeifer. The shell consists only of protein, without lipid or carbohydrate. The principal structural subunit is usually called GvpA, although *Bacillus megaterium* pNL29 uses GvpB/GvpA2 as its major shell protein. External GvpC reinforces the shell. (feng2024advancesinthe pages 2-4, pfeifer2022recentadvancesin pages 1-2)

The curated trait should denote **presence or formation of the individual gas-vesicle organelle**, with buoyancy as its principal direct physiological consequence. Water-column positioning, access to light or oxygen, bloom formation, ultrasound contrast, and pressure-sensitive collapse are downstream functions or assay phenotypes rather than synonyms for the morphology itself.

### Boundary cases

* **Gas vesicle versus gas vacuole:** “Gas vacuole” is historically used for the optically visible aggregate of many gas vesicles and is also used loosely as a synonym. It should remain a synonym for retrieval, but curation should model an individual vesicle separately from a vesicle cluster.
* **Not a membrane vesicle:** the shell is proteinaceous and lacks a lipid bilayer. It is therefore distinct from extracellular vesicles, double-membrane vesicles, storage vacuoles, carboxysomes, and lipid bodies. (pfeifer2022recentadvancesin pages 1-2)
* **Not active gas pumping:** gases diffuse across the shell until internal and external partial pressures equilibrate. Buoyancy results from excluding liquid water, not from metabolically concentrating a specific gas. (feng2024advancesinthe pages 2-4, pfeifer2022recentadvancesin pages 1-2)
* **Collapsed vesicles:** pressure-collapsed shells no longer contain a functional gas phase and should not count as functional buoyancy-conferring vesicles, although the protein structure may remain detectable.
* **Cluster morphology:** GvpU/GvpT-dependent clustering is spatial organization of already formed vesicles, not vesicle biogenesis itself. In the pNL29 system these proteins are nonessential for particle formation. (iburg2024elucidatingtheassembly pages 13-14, jazbec2024proteingasvesicles pages 3-5)

## 2. Candidate graph nodes

### Trait and structural nodes

* `traitmech:000070` — gas vesicle.
* Gas-vesicle shell — label-only candidate complex/cellular structure.
* Gas-vesicle cylindrical body; conical cap; rib; polarity-inversion region — label-only structural subcomponents.
* Gas-vesicle cluster — label-only aggregate; keep distinct from the individual organelle.
* Intracellular localization — use a verified ontology term during implementation rather than assigning an unverified CURIE here.

### Genes and proteins

* **GvpA / GvpB (GvpA2):** major rib-forming shell protein. Taxon-specific nomenclature must be retained.
* **GvpC:** exterior, hydrophilic shell-reinforcement protein; also an engineering handle.
* **GvpN:** AAA+ ATPase associated with maturation from bicone/spindle intermediates to elongated cylinders.
* **GvpF, GvpL:** interacting assembly factors. Haloarchaeal evidence supports GvpF–GvpA binding and GvpL as a platform for several accessory proteins. (pfeifer2022recentadvancesin pages 10-12, feng2024advancesinthe pages 4-5)
* **GvpJ, GvpM:** GvpA-related accessory proteins. GvpJ is essential in the *B. megaterium* construct and tightly associates with the cylindrical region, but its proposed elongation function remains inferred. (pfeifer2022recentadvancesin pages 4-5, jazbec2024proteingasvesicles pages 5-6)
* **GvpG, GvpK, GvpS, GvpO/R, GvpP, GvpQ:** candidate assembly or chaperoning factors; functions and necessity vary among operons.
* **GvpE:** transcriptional activator in haloarchaea; reported to activate relevant promoters and increase `gvpACN` expression approximately tenfold. (pfeifer2022recentadvancesin pages 4-5)
* **GvpD:** negative regulator of gas-vesicle formation in haloarchaeal regulatory systems; do not generalize without a taxon qualifier. (feng2024advancesinthe pages 4-5)
* **GvpU, GvpT:** nonessential spatial-organization/clustering factors in the pNL29 system. (iburg2024elucidatingtheassembly pages 13-14)

Because Gvp proteins are short, divergent, paralogous, and named differently among taxa, **do not assign a single UniProt identifier to a generic Gvp node**. The YAML should either use label-only protein classes or organism-specific UniProt accessions verified directly against the strain and operon.

### Chemicals and physical factors

* ATP — candidate `CHEBI:15422`; substrate/energy source for GvpN ATPase.
* ADP — candidate `CHEBI:16761`; anticipated ATP-hydrolysis product, but the graph should use a biochemical reaction edge only where directly documented for the selected GvpN.
* Water — candidate `CHEBI:15377`; excluded from the vesicle lumen as bulk liquid.
* Gas molecules / dissolved atmospheric gases — label-only collective node; avoid specifying oxygen or nitrogen unless the experiment establishes that gas.
* Hydrostatic pressure; acoustic pressure/ultrasound; water depth — physical/environmental nodes, preferably grounded to verified PATO/ENVO terms during implementation.
* Light availability, oxygen availability, nutrients — ecological downstream factors rather than universal inputs to vesicle biogenesis.

### Processes and functions

* Gas-vesicle assembly/biogenesis — label-only candidate process.
* Shell nucleation, rib assembly, bicone formation, cylindrical enlargement, shell reinforcement, clustering.
* Passive gas diffusion; liquid-water exclusion; buoyancy generation; vertical water-column positioning.
* Pressure-induced buckling/collapse.
* Ultrasound scattering and nonlinear acoustic contrast — assay/application processes, not defining morphology.

## 3. Candidate causal edges

The following matrix summarizes the most defensible graph core.

| candidate subject | predicate | object | evidence strength | taxon/assay restriction | DOI |
|---|---|---|---|---|---|
| GvpA / GvpB | forms shell of | gas vesicle | strong | GvpA broadly supported across bacteria/archaea; GvpB is the major shell protein in *Bacillus megaterium* nomenclature (feng2024advancesinthe pages 2-4, jazbec2024proteingasvesicles pages 3-5) | 10.3390/life12091455; 10.1021/acsnano.4c01498 |
| GvpC | reinforces | gas vesicle shell | strong | surface-associated reinforcement; collapse resistance quantified in multiple taxa/applications (pfeifer2022recentadvancesin pages 12-14, jazbec2024proteingasvesicles pages 5-6) | 10.3390/life12091455; 10.1021/acsnano.4c01498 |
| gas vesicle shell | permits diffusion of | gas molecules | strong | structural/biophysical property of GV shell, not taxon-limited in reviewed evidence (feng2024advancesinthe pages 2-4, pfeifer2022recentadvancesin pages 1-2) | 10.1186/s13036-024-00426-3; 10.3390/life12091455 |
| gas vesicle shell | excludes | liquid water | strong | hydrophobic GV interior and permeability-selective shell; review-level mechanistic consensus (feng2024advancesinthe pages 2-4, pfeifer2022recentadvancesin pages 1-2) | 10.1186/s13036-024-00426-3; 10.3390/life12091455 |
| gas vesicle volume | promotes | buoyancy / water-column positioning | strong | buoyancy requires substantial GV occupancy; downstream ecological positioning effect (feng2024advancesinthe pages 2-4, pfeifer2022recentadvancesin pages 1-2) | 10.1186/s13036-024-00426-3; 10.3390/life12091455 |
| hydrostatic or acoustic pressure | collapses | gas vesicles | strong | collapse pressures reported across taxa; acoustic collapse also exploited in imaging/engineering assays (pfeifer2022recentadvancesin pages 12-14, pfeifer2022recentadvancesin pages 14-15) | 10.3390/life12091455 |
| GvpN (AAA-ATPase) | enables cylindrical enlargement of | gas vesicle | strong | deletion/perturbation gives small spindle-shaped/bicone vesicles in haloarchaea and *B. megaterium* tagging study (pfeifer2022recentadvancesin pages 4-5, jazbec2024proteingasvesicles pages 5-6) | 10.3390/life12091455; 10.1021/acsnano.4c01498 |
| GvpF | binds | GvpA | moderate | strongest direct support is haloarchaeal interaction/assembly analysis; may not generalize identically across taxa (pfeifer2022recentadvancesin pages 10-12, feng2024advancesinthe pages 4-5) | 10.3390/life12091455; 10.1186/s13036-024-00426-3 |
| GvpL | acts as assembly platform for | multiple Gvp proteins | moderate | mainly haloarchaeal interaction model; label as assembly-platform inference for broader TraitMech use (pfeifer2022recentadvancesin pages 10-12, feng2024advancesinthe pages 4-5) | 10.3390/life12091455; 10.1186/s13036-024-00426-3 |
| GvpJ | associated with | gas vesicle elongation | weak / uncertain | *B. megaterium* cryo-EM tagging localized GvpJ near polarity inversional point; functional role inferred, not proven directly (jazbec2024proteingasvesicles pages 5-6) | 10.1021/acsnano.4c01498 |
| GvpU / GvpT | mediates clustering of | gas vesicles | moderate / taxon-specific | nonessential spatial-organization role linked mainly to pNL29/*B. megaterium* and recent clustering work; curate with taxon restriction (iburg2024elucidatingtheassembly pages 13-14, jazbec2024proteingasvesicles pages 3-5) | 10.1038/s44318-024-00178-2; 10.1021/acsnano.4c01498 |
| GvpE | activates transcription of | gvp genes / core gas vesicle proteins | strong | strongest mechanistic evidence from haloarchaea; ~10-fold activation reported in review synthesis (pfeifer2022recentadvancesin pages 4-5, feng2024advancesinthe pages 4-5) | 10.3390/life12091455; 10.1186/s13036-024-00426-3 |
| GvpD | negatively regulates | gas vesicle formation | moderate | regulatory evidence summarized in review literature, strongest in haloarchaea; mechanism may be taxon-specific (feng2024advancesinthe pages 4-5) | 10.1186/s13036-024-00426-3 |


*Table: This table summarizes the strongest candidate causal edges for curating traitmech:000070 gas vesicle. It prioritizes structurally and genetically supported relationships, while clearly flagging inferred, interaction-assay, and taxon-specific claims.*

More detailed curation evidence follows.

| Proposed subject–predicate–object | Reference | Supporting snippet | Curation note |
|---|---|---|---|
| GvpA **forms major structural component of** gas-vesicle shell | [Pfeifer 2022](https://doi.org/10.3390/life12091455) | “GvpA (8-kDa protein) forms the major shell constituent” and is arranged in ribs. | **Strong.** Generic edge is appropriate, while *B. megaterium* GvpB should be represented as a taxon-specific equivalent. (pfeifer2022recentadvancesin pages 1-2) |
| GvpC **reinforces** gas-vesicle shell | [Pfeifer 2022](https://doi.org/10.3390/life12091455) | Removal with 6 M urea decreased collapse pressure threefold. | **Strong**, but magnitude is preparation- and taxon-specific. (pfeifer2022recentadvancesin pages 4-5) |
| Gas-vesicle shell **permits passive diffusion of** gas molecules | [Feng et al. 2024](https://doi.org/10.1186/s13036-024-00426-3) | “Gas can freely penetrate the shell,” producing internal–external gas balance. | **Strong review-level edge.** Do not encode active gas transport. (feng2024advancesinthe pages 2-4) |
| Hydrophobic shell interior **excludes** liquid water | [Pfeifer 2022](https://doi.org/10.3390/life12091455) | “Gas molecules permeate freely through small holes while the hydrophobic interior repels water.” | **Strong biophysical edge.** “Repels” should be normalized as exclusion of bulk liquid water. (pfeifer2022recentadvancesin pages 1-2) |
| Gas-vesicle accumulation **increases** cellular buoyancy | [Pfeifer 2022](https://doi.org/10.3390/life12091455) | Approximately 3–10% of cell volume must contain gas vesicles for buoyancy. | **Strong**, with the percentage treated as contextual rather than universal. (pfeifer2022recentadvancesin pages 1-2) |
| Increased buoyancy **enables** vertical water-column positioning | [Feng et al. 2024](https://doi.org/10.1186/s13036-024-00426-3) | Vesicles enable photosynthetic bacteria to rise toward light and haloarchaea to escape oxygen-poor conditions. | **Moderate/ecological.** Direction and advantage depend on taxon and environment. (feng2024advancesinthe pages 2-4) |
| Hydrostatic or acoustic pressure **causes collapse of** gas vesicle | [Feng et al. 2024](https://doi.org/10.1186/s13036-024-00426-3); [Pfeifer 2022](https://doi.org/10.3390/life12091455) | Critical pressure varies from 0.09 to 1 MPa among microorganisms; one halobacterial preparation collapsed at 98 kPa under the reported ultrasound condition. | **Strong phenomenon; quantitative values are taxon/assay-specific.** (pfeifer2022recentadvancesin pages 12-14, feng2024advancesinthe pages 2-4) |
| GvpN ATPase **promotes** cylindrical enlargement | [Pfeifer 2022](https://doi.org/10.3390/life12091455); [Jazbec et al. 2024](https://doi.org/10.1021/acsnano.4c01498) | `gvpN` deletion yielded tiny structures; N-terminal tagging produced spindle-shaped vesicles lacking an elongated cylindrical region. | **Strong but taxon-specific.** Encode ATPase activity separately from the inferred mechanochemical step. (pfeifer2022recentadvancesin pages 4-5, jazbec2024proteingasvesicles pages 5-6) |
| GvpF **binds** GvpA | [Pfeifer 2022](https://doi.org/10.3390/life12091455) | GvpF and GvpO bind monomeric GvpA before incorporation. | **Moderate.** Strongest evidence is haloarchaeal; do not universalize to every operon. (pfeifer2022recentadvancesin pages 10-12) |
| GvpL **organizes/binds** multiple accessory Gvp proteins | [Pfeifer 2022](https://doi.org/10.3390/life12091455) | GvpL was described as a major platform binding most Gvps except GvpA. | **Moderate, model-based.** Prefer “interacts with” for direct graph edges and reserve “assembly platform” for annotation. (pfeifer2022recentadvancesin pages 10-12) |
| GvpJ **promotes** shell elongation | [Jazbec et al. 2024](https://doi.org/10.1021/acsnano.4c01498) | GvpJ remained tightly associated after urea treatment and localized near the cylindrical polarity-inversion region; authors proposed involvement in adding GvpB units. | **Uncertain/inferred.** Curate localization/binding, not elongation causality, until direct perturbation resolves the mechanism. (jazbec2024proteingasvesicles pages 5-6) |
| GvpU and GvpT **promote** gas-vesicle clustering | [Iburg et al. 2024](https://doi.org/10.1038/s44318-024-00178-2) | “GvpU and, to a lesser extent, GvpT mediate the clustering of GVs”; both are nonessential in pNL29. | **Taxon-specific and partly conflicting.** Jazbec et al. could not confirm an individual GvpU clustering effect. (iburg2024elucidatingtheassembly pages 13-14, jazbec2024proteingasvesicles pages 5-6) |
| GvpE **activates transcription of** gas-vesicle genes | [Pfeifer 2022](https://doi.org/10.3390/life12091455) | GvpE activated PpA/PpD and produced approximately tenfold activation of `gvpACN`. | **Strong for the haloarchaeal system**, not a universal bacterial edge. (pfeifer2022recentadvancesin pages 4-5) |
| GvpD **negatively regulates** gas-vesicle formation | [Feng et al. 2024](https://doi.org/10.1186/s13036-024-00426-3) | Review synthesis states that GvpD has an inhibitory effect on formation. | **Moderate/review-derived and haloarchaea-biased.** Verify the primary study before YAML inclusion. (feng2024advancesinthe pages 4-5) |
| GvpR, GvpT and GvpU **are dispensable for** functional pNL29 vesicle formation | [Jazbec et al. 2024](https://doi.org/10.1021/acsnano.4c01498) | Electron microscopy confirmed vesicles in ΔGvpR, ΔGvpT and ΔGvpU, whereas ΔGvpN had no vesicles. | **Strong for heterologous pNL29 expression in *E. coli*.** Absence of necessity is not a universal biological function. (jazbec2024proteingasvesicles pages 3-5) |
| Deletion of GvpR/T/U **reduces** vesicle diameter | [Jazbec et al. 2024](https://doi.org/10.1021/acsnano.4c01498) | ΔRTU vesicles averaged 42 ± 7 nm versus 48 ± 8 nm for wild type. | **Strong assay-specific morphology edge.** Useful as a strain/construct-qualified edge. (jazbec2024proteingasvesicles pages 3-5) |

## 4. Recent developments and applications

### Assembly mechanism and spatial organization

Iburg et al. systematically assayed all 11 proteins in the *B. megaterium* pNL29 operon using an in-vivo split-NanoLuc interaction assay across more than 968 conditions. The resulting network indicates that initiation, growth, chaperoning, and clustering are interconnected rather than cleanly sequential stages. However, the authors explicitly characterize the network as semiquantitative and warn that fusion proteins, overexpression, degradation, aggregation, and the heterologous *E. coli* host can produce false-positive or false-negative interactions. Consequently, interaction edges are useful hypotheses but should not automatically become mechanistic causal edges. (iburg2024elucidatingtheassembly pages 1-2, iburg2024elucidatingtheassembly pages 13-14)

Jazbec et al. minimized the same operon and found GvpR, GvpT, and GvpU dispensable, while GvpN remained essential under their heterologous-expression assay. The ΔRTU construct produced narrower particles, averaging 42 ± 7 nm compared with 48 ± 8 nm for wild-type vesicles; observed lengths ranged from 40 nm to 2 µm. Their tagging experiments further showed tight GvpJ association with the cylindrical region, whereas several other accessory proteins were weakly bound or absent from mature isolated shells. (jazbec2024proteingasvesicles pages 3-5, jazbec2024proteingasvesicles pages 5-6)

### Acoustic reporter engineering

Hurt et al. developed high-throughput acoustic screening and evolved the major shell proteins of *Anabaena flos-aquae* and *B. megaterium*. The leading GvpA-T6A-L40A, GvpA-T6A-I48V, and GvpB-S9G-R31L-R85L variants generated 5.32-, 5.37-, and 13.93-fold more nonlinear acoustic signal than their respective parents. TEM indicated that the dominant explanation was increased or more uniform vesicle abundance per cell, although altered shell mechanics could contribute. This is important for curation: stronger ultrasound signal is not necessarily evidence of a fundamentally different natural gas-vesicle trait. (hurt2024directedevolutionof pages 7-8)

Howells et al. implemented drug-selectable, doxycycline-inducible mammalian acoustic reporter genes in HEK293T cells. After 72 hours of induction, mixed selected populations reached an average 18.5 dB signal-to-noise ratio—80% above non-induced reporter cells and 500% above wild-type HEK293T controls. After prolonged drug selection, induced and non-induced populations reached 29 and 6.6 dB, respectively. The system eliminated fluorescence-activated sorting and single-cell cloning, but low-level uninduced expression remained. (howells2024adrug‐selectableacoustic pages 5-7)

### Sonogenetic actuation

Jazbec et al. attached *B. megaterium* vesicles to HEK293-cell integrins using engineered *A. flos-aquae* GvpC carrying an integrin-binding peptide. With 1-MHz pulsed ultrasound, membrane-associated vesicles increased calcium influx and enhanced an NFAT-linked luciferase response. This demonstrates a real-world synthetic-biological use, but it is an engineered mammalian-cell application and should not be incorporated into the microbial trait’s core natural causal graph. (jazbec2024proteingasvesicles pages 5-6)

### In-vivo blood interactions

Ling et al. showed that gas-vesicle behavior in blood is not that of an inert freely circulating particle. At approximately 0.2 nM vesicles and 4% hematocrit, mixing with red blood cells increased amplitude-modulation signal from 17.89 ± 0.42 to 23.85 ± 0.53 arbitrary units; after removal of unbound particles, 7.74 ± 0.11 units remained. RBC fluorescence rose from 0.53 ± 0.01 to 1.17 ± 0.09, although only 0.5% of RBCs showed substantial binding. Serum proteins also promoted aggregation, while 10-kDa mPEG passivation reduced RBC adsorption and extended circulation. These results are directly relevant to biomedical implementation but not to native microbial vesicle biogenesis. (ling2023gasvesicle–bloodinteractions pages 2-5)

## 5. Recommended minimal TraitMech graph

A conservative core suitable for `gas_vesicle.yaml` is:

1. GvpA/GvpB → **forms structural component of** → gas-vesicle shell.
2. GvpC → **reinforces** → gas-vesicle shell.
3. GvpN ATPase activity → **promotes** → cylindrical gas-vesicle maturation.
4. Gas-vesicle shell → **permits passive diffusion of** → gas molecules.
5. Gas-vesicle shell → **excludes bulk liquid** → water.
6. Gas-filled vesicle volume → **decreases** → effective cellular density.
7. Decreased cellular density → **increases** → buoyancy.
8. Increased hydrostatic/acoustic pressure → **causes** → gas-vesicle collapse.
9. Gas-vesicle collapse → **decreases** → buoyancy.

Edges 6 and 9 are physically compelling but should be connected to direct primary evidence in the curation record rather than supported only by review synthesis. GvpF/GvpL interactions, GvpE/GvpD regulation, GvpJ elongation, and GvpU/GvpT clustering are best placed in taxon-qualified extensions.

## 6. Claims not yet ready for unrestricted curation

* **Do not treat every `gvp` gene as universally essential.** Gene content and nomenclature differ markedly among cyanobacteria, heterotrophic bacteria, and haloarchaea. The pNL29 ΔRTU result is construct- and host-specific. (jazbec2024proteingasvesicles pages 3-5, feng2024advancesinthe pages 4-5)
* **Do not curate GvpJ → elongation as established causality.** Current evidence is localization plus mechanistic interpretation. (jazbec2024proteingasvesicles pages 5-6)
* **Do not generalize GvpU-mediated clustering.** One 2024 analysis supports it, while another could not reproduce an individual GvpU effect. (iburg2024elucidatingtheassembly pages 13-14, jazbec2024proteingasvesicles pages 5-6)
* **Do not infer natural environmental regulation from engineered expression systems.** Doxycycline induction, arabinose control, ultrasound actuation, and mammalian expression are experimental factors.
* **Do not encode a universal critical collapse pressure.** Reported values span approximately 0.09–1 MPa and depend on vesicle width, shell composition, taxon, medium, and pressure protocol. (feng2024advancesinthe pages 2-4)
* **Do not model the lumen as oxygen-filled by default.** The shell is permeable to gases and equilibrates with the surrounding dissolved-gas composition.
* **Do not equate stronger acoustic signal with more vesicles without measurement.** Signal depends on abundance, dimensions, clustering, shell mechanics, collapse threshold, imaging sequence, and blood interactions. (hurt2024directedevolutionof pages 7-8, ling2023gasvesicle–bloodinteractions pages 2-5)
* **Verify ontology identifiers before YAML insertion.** Generic Gvp labels should remain label-only until strain-specific protein accessions are checked; no identifiers should be inferred from protein names alone.

## 7. DOI-first bibliography

1. Iburg M, Anderson AP, Wong VT, et al. **Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis.** *EMBO Journal* 43:4156–4172. Published September 2024. DOI: [10.1038/s44318-024-00178-2](https://doi.org/10.1038/s44318-024-00178-2). (iburg2024elucidatingtheassembly pages 1-2, iburg2024elucidatingtheassembly pages 13-14)
2. Jazbec V, Varda N, Šprager E, et al. **Protein Gas Vesicles of Bacillus megaterium as Enhancers of Ultrasound-Induced Transcriptional Regulation.** *ACS Nano* 18:16692–16700. Published June 2024. DOI: [10.1021/acsnano.4c01498](https://doi.org/10.1021/acsnano.4c01498). (jazbec2024proteingasvesicles pages 3-5, jazbec2024proteingasvesicles pages 5-6)
3. Hurt RC, Jin Z, Soufi M, et al. **Directed Evolution of Acoustic Reporter Genes Using High-Throughput Acoustic Screening.** *ACS Synthetic Biology* 13:2215–2226. Published July 2024. DOI: [10.1021/acssynbio.4c00283](https://doi.org/10.1021/acssynbio.4c00283). (hurt2024directedevolutionof pages 7-8)
4. Howells AR, Welch PJ, Kim J, et al. **A drug-selectable acoustic reporter gene system for human cell ultrasound imaging.** *Bioengineering & Translational Medicine* 9. Published August 2024. DOI: [10.1002/btm2.10584](https://doi.org/10.1002/btm2.10584). (howells2024adrug‐selectableacoustic pages 5-7)
5. Feng R, Lan J, Goh MC, Du M, Chen Z. **Advances in the application of gas vesicles in medical imaging and disease treatment.** *Journal of Biological Engineering* 18:41. Published July 2024. DOI: [10.1186/s13036-024-00426-3](https://doi.org/10.1186/s13036-024-00426-3). (feng2024advancesinthe pages 2-4, feng2024advancesinthe pages 4-5)
6. Ling B, Ko JH, Stordy BP, et al. **Gas Vesicle–Blood Interactions Enhance Ultrasound Imaging Contrast.** *Nano Letters* 23:10748–10757. Published November 2023. DOI: [10.1021/acs.nanolett.3c02780](https://doi.org/10.1021/acs.nanolett.3c02780). (ling2023gasvesicle–bloodinteractions pages 2-5)
7. Pfeifer F. **Recent Advances in the Study of Gas Vesicle Proteins and Application of Gas Vesicles in Biomedical Research.** *Life* 12:1455. Published September 2022. DOI: [10.3390/life12091455](https://doi.org/10.3390/life12091455). (pfeifer2022recentadvancesin pages 4-5, pfeifer2022recentadvancesin pages 1-2, pfeifer2022recentadvancesin pages 10-12)

The strongest immediate curation strategy is therefore a compact, taxon-neutral structural–biophysical core, supplemented by separate organism-qualified modules for haloarchaeal transcriptional control, pNL29 assembly and clustering, and engineered acoustic applications.

References

1. (feng2024advancesinthe pages 2-4): Renjie Feng, Jie Lan, Meei Chyn Goh, Meng Du, and Zhiyi Chen. Advances in the application of gas vesicles in medical imaging and disease treatment. Journal of Biological Engineering, Jul 2024. URL: https://doi.org/10.1186/s13036-024-00426-3, doi:10.1186/s13036-024-00426-3. This article has 17 citations and is from a peer-reviewed journal.

2. (pfeifer2022recentadvancesin pages 1-2): Felicitas Pfeifer. Recent advances in the study of gas vesicle proteins and application of gas vesicles in biomedical research. Life, 12:1455, Sep 2022. URL: https://doi.org/10.3390/life12091455, doi:10.3390/life12091455. This article has 26 citations.

3. (iburg2024elucidatingtheassembly pages 13-14): Manuel Iburg, Andrew P Anderson, Vivian T. Wong, Erica D. Anton, Art He, and George J. Lu. Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis. Sep 2024. URL: https://doi.org/10.1038/s44318-024-00178-2, doi:10.1038/s44318-024-00178-2. This article has 11 citations.

4. (jazbec2024proteingasvesicles pages 3-5): Vid Jazbec, Nina Varda, Ernest Šprager, Maja Meško, Sara Vidmar, Rok Romih, Marjetka Podobnik, Andreja Kežar, Roman Jerala, and Mojca Benčina. Protein gas vesicles of <i>bacillus megaterium</i> as enhancers of ultrasound-induced transcriptional regulation. ACS Nano, 18:16692-16700, Jun 2024. URL: https://doi.org/10.1021/acsnano.4c01498, doi:10.1021/acsnano.4c01498. This article has 10 citations and is from a highest quality peer-reviewed journal.

5. (pfeifer2022recentadvancesin pages 10-12): Felicitas Pfeifer. Recent advances in the study of gas vesicle proteins and application of gas vesicles in biomedical research. Life, 12:1455, Sep 2022. URL: https://doi.org/10.3390/life12091455, doi:10.3390/life12091455. This article has 26 citations.

6. (feng2024advancesinthe pages 4-5): Renjie Feng, Jie Lan, Meei Chyn Goh, Meng Du, and Zhiyi Chen. Advances in the application of gas vesicles in medical imaging and disease treatment. Journal of Biological Engineering, Jul 2024. URL: https://doi.org/10.1186/s13036-024-00426-3, doi:10.1186/s13036-024-00426-3. This article has 17 citations and is from a peer-reviewed journal.

7. (pfeifer2022recentadvancesin pages 4-5): Felicitas Pfeifer. Recent advances in the study of gas vesicle proteins and application of gas vesicles in biomedical research. Life, 12:1455, Sep 2022. URL: https://doi.org/10.3390/life12091455, doi:10.3390/life12091455. This article has 26 citations.

8. (jazbec2024proteingasvesicles pages 5-6): Vid Jazbec, Nina Varda, Ernest Šprager, Maja Meško, Sara Vidmar, Rok Romih, Marjetka Podobnik, Andreja Kežar, Roman Jerala, and Mojca Benčina. Protein gas vesicles of <i>bacillus megaterium</i> as enhancers of ultrasound-induced transcriptional regulation. ACS Nano, 18:16692-16700, Jun 2024. URL: https://doi.org/10.1021/acsnano.4c01498, doi:10.1021/acsnano.4c01498. This article has 10 citations and is from a highest quality peer-reviewed journal.

9. (pfeifer2022recentadvancesin pages 12-14): Felicitas Pfeifer. Recent advances in the study of gas vesicle proteins and application of gas vesicles in biomedical research. Life, 12:1455, Sep 2022. URL: https://doi.org/10.3390/life12091455, doi:10.3390/life12091455. This article has 26 citations.

10. (pfeifer2022recentadvancesin pages 14-15): Felicitas Pfeifer. Recent advances in the study of gas vesicle proteins and application of gas vesicles in biomedical research. Life, 12:1455, Sep 2022. URL: https://doi.org/10.3390/life12091455, doi:10.3390/life12091455. This article has 26 citations.

11. (iburg2024elucidatingtheassembly pages 1-2): Manuel Iburg, Andrew P Anderson, Vivian T. Wong, Erica D. Anton, Art He, and George J. Lu. Elucidating the assembly of gas vesicles by systematic protein-protein interaction analysis. Sep 2024. URL: https://doi.org/10.1038/s44318-024-00178-2, doi:10.1038/s44318-024-00178-2. This article has 11 citations.

12. (hurt2024directedevolutionof pages 7-8): Robert C. Hurt, Zhiyang Jin, Mohamed Soufi, Katie K. Wong, Daniel P. Sawyer, Hao K. Shen, Przemysław Dutka, Ramya Deshpande, Ruby Zhang, David R. Mittelstein, and Mikhail G. Shapiro. Directed evolution of acoustic reporter genes using high-throughput acoustic screening. ACS Synthetic Biology, 13:2215-2226, Jul 2024. URL: https://doi.org/10.1021/acssynbio.4c00283, doi:10.1021/acssynbio.4c00283. This article has 15 citations and is from a domain leading peer-reviewed journal.

13. (howells2024adrug‐selectableacoustic pages 5-7): Alessandro R. Howells, Phoebe J. Welch, John Kim, Craig R. Forest, Chengzhi Shi, and Xiaojun Lance Lian. A drug‐selectable acoustic reporter gene system for human cell ultrasound imaging. Bioengineering & Translational Medicine, Aug 2024. URL: https://doi.org/10.1002/btm2.10584, doi:10.1002/btm2.10584. This article has 4 citations.

14. (ling2023gasvesicle–bloodinteractions pages 2-5): Bill Ling, Jeong Hoon Ko, Benjamin P Stordy, Yuwei Zhang, Tighe F. Didden, Dina Malounda, Margaret B. Swift, Warren C. W. Chan, and Mikhail G. Shapiro. Gas vesicle–blood interactions enhance ultrasound imaging contrast. Nano Letters, 23:10748-10757, Nov 2023. URL: https://doi.org/10.1021/acs.nanolett.3c02780, doi:10.1021/acs.nanolett.3c02780. This article has 16 citations and is from a highest quality peer-reviewed journal.