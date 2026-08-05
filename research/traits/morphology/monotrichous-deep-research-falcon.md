---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:00:14.237117'
end_time: '2026-08-04T09:08:31.747316'
duration_seconds: 497.51
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: monotrichous
  trait_identifier: traitmech:000057
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: monotrichous
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagellar arrangement with a single flagellum, typically located at
    one pole of the cell.
  parent_traits: traitmech:000056
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe single-flagellum
    (monotrichous, polar) flagellation as one regular flagellation pattern.) | DOI:10.3390/biom9070279:  (Flagellum
    review supports a single helical flagellar filament as a locomotory organelle.)'
  causal_graph_summary: 'monotrichous_single_polar_flagellum: 10 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** monotrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000057
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a single flagellum, typically located at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe single-flagellum (monotrichous, polar) flagellation as one regular flagellation pattern.) | DOI:10.3390/biom9070279:  (Flagellum review supports a single helical flagellar filament as a locomotory organelle.)
- **Existing causal graph summary:** monotrichous_single_polar_flagellum: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **monotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/monotrichous.yaml`.

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
- **Trait label:** monotrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000057
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a single flagellum, typically located at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe single-flagellum (monotrichous, polar) flagellation as one regular flagellation pattern.) | DOI:10.3390/biom9070279:  (Flagellum review supports a single helical flagellar filament as a locomotory organelle.)
- **Existing causal graph summary:** monotrichous_single_polar_flagellum: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **monotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/monotrichous.yaml`.

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


# Curation report: monotrichous (`traitmech:000057`)

## Executive summary

**Recommended scope.** The trait denotes the morphological state in which a bacterial cell bears **one flagellum at one cell pole**. A direct literature definition contrasts peritrichous *Salmonella/E. coli* with *Vibrio/Pseudomonas* cells possessing “a single flagellum at one of the cell poles (monotrichous flagellum).” The defining variables are therefore **number = 1**, **position = polar**, and presence of the assembled appendage—not swimming performance alone (terashima2020assemblymechanismof pages 2-4).

The strongest currently supported causal module is:

**FipA + HubP/FimV → polar recruitment/activation of FlhF → capture of polar-system FliG → recruitment and assembly of FliF into the MS-ring → progressive polar flagellum assembly**, opposed by **FlhG/FleN**, which stimulates FlhF GTPase activity and limits repeated initiation. The clearest direct molecular dissection was published in 2024 for *Shewanella putrefaciens*, while comparative 2024 work supports a conserved but quantitatively variable FipA–FlhF mechanism in *Vibrio parahaemolyticus*, *Pseudomonas putida*, and *S. putrefaciens* (arroyoperez2024aconservedcellpole pages 14-15, arroyoperez2024aconservedcellpole pages 2-3, dornes2024polarconfinementof pages 1-2).

| subject | predicate | object | organism scope | confidence |
|---|---|---|---|---|
| FipA | interacts with and promotes polar membrane recruitment of | FlhF | Polar-flagellated γ-proteobacteria studied: *Vibrio parahaemolyticus*, *Pseudomonas putida*, *Shewanella putrefaciens* (arroyoperez2024aconservedcellpole pages 1-2, arroyoperez2024aconservedcellpole pages 14-15, arroyoperez2024aconservedcellpole pages 2-3) | high |
| HubP/FimV | recruits or anchors at pole | FlhF | Strongest direct evidence in *S. putrefaciens*; cooperative role with FipA across *Vibrio/Pseudomonas/Shewanella* (arroyoperez2024aconservedcellpole pages 14-15, dornes2024polarconfinementof pages 4-6, dornes2024polarconfinementof pages 1-2) | high |
| FlhF | binds | FliG | Direct biochemical and Y2H evidence in *S. putrefaciens* polar flagellar system (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 1-2) | high |
| FlhF-bound FliG | captures | FliF | Direct mechanistic model and pulldown-supported interaction sequence in *S. putrefaciens*; supported by Vibrio MS-ring initiation studies (arroyoperez2024aconservedcellpole pages 2-3, dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 4-6, dornes2024polarconfinementof pages 1-2) | high |
| FliF | assembles into | MS-ring | Strong direct evidence in *Vibrio*; general bacterial flagellar initiation step (terashima2020assemblymechanismof pages 1-2, terashima2020assemblymechanismof pages 4-6, dornes2024polarconfinementof pages 1-2) | high |
| FlhG | stimulates GTPase activity of | FlhF | Polar-flagellated bacteria; direct mechanistic statement and review-supported conserved role (arroyoperez2024aconservedcellpole pages 14-15, terashima2020assemblymechanismof pages 2-4, dornes2024polarconfinementof pages 1-2) | high |
| FlhG-stimulated FlhF inactivation | limits additional initiation of | polar flagellum assembly events | Best supported in *Vibrio* and *Shewanella*; conserved control of flagellar number/location (arroyoperez2024aconservedcellpole pages 2-3, arroyoperez2024aconservedcellpole pages 14-15, terashima2020assemblymechanismof pages 2-4, dornes2024polarconfinementof pages 1-2) | high |
| assembled polar flagellar motor and filament | realizes | traitmech:000057 | Monotrichous bacteria with one polar flagellum; trait outcome distinct from motility alone (arroyoperez2024aconservedcellpole pages 1-2, terashima2020assemblymechanismof pages 2-4, dornes2024polarconfinementof pages 1-2) | medium-high |


*Table: This table summarizes the highest-confidence mechanistic edges for a candidate monotrichous TraitMech graph. It condenses the core FlhF-FlhG-HubP/FimV-FipA-FliG-FliF pathway into curator-ready subject-predicate-object statements with organism scope and confidence.*

## 1. Trait scope and boundaries

### 1.1 Inclusion criteria

Curate `traitmech:000057` when an assay establishes:

1. one bacterial flagellum or flagellar filament per cell;
2. insertion at a pole, including an explicitly monopolar/old-pole position;
3. the mature morphological state, or a mechanism directly shown to generate that state.

A sheathed polar filament, as found in many *Vibrio* species, remains monotrichous if there is exactly one polar flagellum; sheath status is a separate structural attribute (arroyoperez2024aconservedcellpole pages 1-2).

### 1.2 Nearby traits that should remain separate

- **Lophotrichous:** multiple flagella forming a tuft at one pole. *P. putida* is treated as lophotrichous in the 2024 comparative study and should not be used as direct organism-level evidence for the terminal monotrichous phenotype, although it provides useful evidence for shared upstream machinery (arroyoperez2024aconservedcellpole pages 2-3).
- **Amphitrichous:** one or more flagella at both poles; number and bipolarity differ from the target state.
- **Peritrichous:** flagella distributed around the cell surface. The 2020 *Vibrio* study explicitly contrasts this state in *E. coli/Salmonella* with a single polar flagellum (terashima2020assemblymechanismof pages 2-4).
- **Lateral flagellation:** a separate flagellar system may coexist with the primary polar system. *S. putrefaciens* has a primary FlhF/FlhG-dependent polar system and a secondary FlhF/FlhG-independent lateral system; consequently, whole-cell “exactly one flagellum” must be established under the assayed condition rather than inferred solely from the polar module (dornes2024polarconfinementof pages 1-2).
- **Periplasmic/endoflagellar arrangements:** *Borrelia burgdorferi* bears 7–11 periplasmic flagella from each pole, not a single external polar flagellum. Its FlhF mechanism is evolutionarily informative but its phenotype is outside this trait (zhang2020flhfregulatesthe pages 1-2).
- **Motile/nonmotile:** motility is a physiological output influenced by motor energization, filament integrity, viscosity, and assay conditions. It is not equivalent to flagellar number or location. A mutant may retain polar flagella but swim poorly, or lose polar placement while retaining some motility.
- **Transient cell-cycle states:** newly divided cells may not yet have completed assembly. Curate the species/strain phenotype from an appropriate population and growth phase, not from an isolated preassembly cell.

### 1.3 Recommended graph interpretation

The terminal node should represent an **assay-observed morphology**, not a genomic capability. Presence of `flhF`, `flhG`, or `fipA` is insufficient because these genes also occur in organisms with lophotrichous or other polar patterns. The 2024 comparative genomic analysis found FipA only with FlhF/FlhG and in the sampled polar flagellates, but those species included both monotrichous and lophotrichous arrangements (arroyoperez2024aconservedcellpole pages 2-3).

## 2. Candidate nodes grouped by type

### 2.1 Trait and cellular structures

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| monotrichous | morphology class | `traitmech:000057` | Quote identifier verbatim in YAML. |
| bacterial-type flagellum | cellular component | `GO:0009288` | Mature appendage; verify GO release during implementation. |
| bacterial flagellar basal body | cellular component | `GO:0009425` | Broad structural parent for motor base. |
| MS-ring | complex, label-first | GO lookup recommended | Built from multiple FliF copies in the cytoplasmic membrane. |
| C-ring / switch complex | complex, label-first | GO lookup recommended | Contains FliG, FliM, and FliN. |
| cell pole | localization | `GO:0051286` | Location at which the polar system is initiated. |
| cytoplasmic membrane | localization | `GO:0005886` | FipA and FliF membrane context. |
| polar flagellum assembly | biological process | `GO:0044780` as broad bacterial-type flagellum assembly | Retain “polar” as contextual qualifier unless a verified narrower term is available. |

The flagellar core includes the membrane-embedded FliF MS-ring and a cytoplasmic C-ring composed of FliG/FliM/FliN; the rod, hook, and filament are assembled subsequently (arroyoperez2024aconservedcellpole pages 1-2, dornes2024polarconfinementof pages 1-2).

### 2.2 Proteins and regulators

| Node | Function in candidate graph | Grounding recommendation |
|---|---|---|
| FlhF | SRP-family GTPase; positive regulator and polar assembly organizer | Label plus organism-specific UniProt accession after strain-level validation |
| FlhG / FleN | MinD-family ATPase; negative numerical regulator and FlhF GTPase stimulator | Treat names as ortholog/synonym context, not necessarily interchangeable records |
| HubP / FimV | polar landmark/scaffold | Separate organism-specific protein records; functional correspondence is not identity |
| FipA | small integral-membrane FlhF-interacting protein containing DUF2802 | Label plus organism-specific UniProt accession; avoid equating all DUF2802 proteins without orthology checks |
| FliG | C-ring/rotor component captured by FlhF in the polar system | Organism-specific UniProt |
| FliF | transmembrane MS-ring subunit and initial structural building block | Organism-specific UniProt |
| FliM/FliN | later C-ring partners of FliG; coupled to FlhG-mediated progression | Organism-specific UniProt |
| FlrA / FleQ | flagellar master transcriptional regulator | Include only in an explicitly taxon-scoped regulatory branch |

FipA in *V. parahaemolyticus* is an approximately 18.4-kDa, 163-residue protein with an N-terminal transmembrane segment and cytoplasmic DUF2802; homologues were reported only in genomes also encoding FlhF and FlhG in that analysis (arroyoperez2024aconservedcellpole pages 2-3).

### 2.3 Chemicals and molecular states

| Node | Suggested CURIE | Role |
|---|---|---|
| GTP | `CHEBI:15996` | Binding favors active/dimeric FlhF; hydrolysis promotes inactivation/release. |
| GDP | `CHEBI:17552` | FlhF post-hydrolysis nucleotide state. |
| ATP | `CHEBI:15422` | Supports FlhG dimerization/membrane-associated regulatory activity. |
| ADP | `CHEBI:16761` | Product/state associated with ATPase cycling. |
| ion motive force | label-first | Powers rotation, not the number/placement phenotype itself. |

### 2.4 Experimental and environmental factors

Useful evidence nodes include `flhF`, `flhG/fleN`, `fipA`, `hubP/fimV`, `fliF`, or `fliG` deletion; FlhF N-terminal deletion; FipA DUF2802 substitutions; protein overexpression; fluorescent hook or FliF/FlhF localization; soft-agar spreading; electron microscopy; co-immunoprecipitation; two-hybrid assays; and in-vitro pulldowns. These are **evidence-generating perturbations**, not constitutive biological causes.

Environmental viscosity, surface contact, pH, ion composition, and growth phase can alter swimming or motor performance, but no retrieved evidence establishes them as general determinants of the one-polar-flagellum morphology. They should not enter the core graph without phenotype-specific evidence.

## 3. Candidate evidence-backed causal edges

| # | Subject–predicate–object | Scope and confidence | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|---|
| 1 | FipA **directly interacts with** FlhF | Three γ-proteobacteria; **high** | DOI: [10.7554/eLife.93004](https://doi.org/10.7554/eLife.93004), 5 Dec 2024 | “In all three species, FipA directly interacts with FlhF as demonstrated by reciprocal co-immunoprecipitations and by bacterial two-hybrid assays.” (arroyoperez2024aconservedcellpole pages 14-15) | Safe as a taxon-scoped physical-interaction edge. |
| 2 | FipA transmembrane localization **enables** FlhF targeting/function | Comparative; **high** | 10.7554/eLife.93004 | “A FipA mutant lacking its N-terminal transmembrane domain was non-functional, indicating that interaction of FlhF and FipA has to take place at the membrane.” (arroyoperez2024aconservedcellpole pages 14-15) | Prefer `required_for_normal` over an absolute universal `required_for`. |
| 3 | FipA **promotes** polar localization of FlhF | *Vibrio*, *Pseudomonas*, *Shewanella*; **high** | 10.7554/eLife.93004 | “In the absence of FipA, polar localization of FlhF was significantly decreased in all three species.” (arroyoperez2024aconservedcellpole pages 14-15) | Effect magnitude is species-dependent. |
| 4 | HubP/FimV and FipA **cooperatively promote** sufficient polar FlhF | Comparative; **high** | 10.7554/eLife.93004 | FlhF localization was “almost completely diminished when hubP or fimV was deleted together with fipA”; both pathways bring sufficient active FlhF to trigger MS-ring formation (arroyoperez2024aconservedcellpole pages 14-15). | Model as parallel inputs, not a simple obligatory linear chain. |
| 5 | HubP **binds/anchors** FlhF at the pole | Direct in *S. putrefaciens*; **high** | DOI: [10.1038/s41467-024-50274-4](https://doi.org/10.1038/s41467-024-50274-4), accepted 5 Jul 2024 | “The NG domain of FlhF is required for the interaction with HubP-C”; a ternary HubP–FlhF–FliG complex was observed (dornes2024polarconfinementof pages 4-6). | Direct molecular edge; broader conservation requires taxon annotation. |
| 6 | FlhF N-terminal FID **binds** polar-system FliG | *S. putrefaciens*; **high** | 10.1038/s41467-024-50274-4 | FlhF strongly interacted with polar FliG but not FliF-C, FliM, FliN, or lateral-system FliG; the N-terminal 60 residues were necessary and sufficient (dornes2024polarconfinementof pages 2-4). | Explicitly distinguish polar FliG from lateral-system paralogues. |
| 7 | HubP-bound FlhF **recruits** FliG to the pole | *S. putrefaciens*; **high** | 10.1038/s41467-024-50274-4 | “FlhF is able to bridge HubP and FliG in vitro” (dornes2024polarconfinementof pages 4-6). | Physical recruitment is strongly supported; physiological stoichiometry remains contextual. |
| 8 | FlhF-bound FliG **captures** FliF | *S. putrefaciens*; **high** | 10.1038/s41467-024-50274-4 | “When bound to FlhF, FliG was able to interact with the cytoplasmic domain…of FliF,” while unable to bind FliM/N (dornes2024polarconfinementof pages 2-4). | Strong mechanistic edge connecting localization to MS-ring initiation. |
| 9 | FlhF **promotes polar localization of** FliF | *V. alginolyticus*; **high** | DOI: [10.1128/JB.00236-20](https://doi.org/10.1128/JB.00236-20), published 27 Jul 2020 | GFP-FliF was polar in wild type but not in the `flhF` null mutant; FlhF restored polar localization even in an `rpoN` mutant lacking other flagellar proteins (terashima2020assemblymechanismof pages 4-6). | Supports a direct/near-direct localization role independent of other flagellar components. |
| 10 | FlhF **facilitates** FliF MS-ring assembly | *Vibrio* with heterologous *E. coli* reconstitution; **high, assay-specific** | 10.1128/JB.00236-20 | Coexpression of FliF and FlhF produced much more FliF in the MS-ring fraction and “a large number” of rings by EM, whereas FliF alone assembled inefficiently (terashima2020assemblymechanismof pages 1-2, terashima2020assemblymechanismof pages 4-6). | Retain heterologous-reconstitution evidence qualifier. |
| 11 | FliF **assembles into** the MS-ring | Broad flagellar mechanism; **high** | 10.1128/JB.00236-20 | “Flagellar biogenesis is initiated by the assembly of the MS-ring…[which] consists of a few dozen copies of…FliF” (terashima2020assemblymechanismof pages 1-2). | Core structural edge. |
| 12 | FlhG **stimulates GTPase activity of** FlhF | Polar flagellates; **high** | 10.1038/s41467-024-50274-4; 10.1128/JB.00236-20 | FlhF GTPase activity “is stimulated by FlhG,” and the 2020 study likewise states that FlhG enhances FlhF GTPase activity (terashima2020assemblymechanismof pages 2-4, dornes2024polarconfinementof pages 1-2). | Curate as biochemical regulation, not merely genetic antagonism. |
| 13 | FlhG-mediated FlhF inactivation **limits** additional polar initiation events | Strong in *Vibrio/Shewanella*; **high** | 10.7554/eLife.93004; 10.1128/JB.00236-20 | Loss of FlhG produces hyperflagellation, while FlhG reduces polar FlhF and suppresses its function to construct a single polar flagellum (arroyoperez2024aconservedcellpole pages 2-3, terashima2020assemblymechanismof pages 2-4). | This is the principal number-control edge leading to “one.” |
| 14 | FlhF FID/FliG coupling **causes proper polar placement** of the hook | *S. putrefaciens*; **high** | 10.1038/s41467-024-50274-4 | ΔN44-FlhF remained polar, but hooks became mostly subpolar/lateral; wild type had exclusively polar hooks in about 75% of cells (dornes2024polarconfinementof pages 4-6). | Excellent causal separation of regulator localization from machinery localization. |
| 15 | polar MS-ring/C-ring initiation **enables** progressive motor–rod–hook–filament assembly | General, **high but broad** | 10.1128/JB.00236-20; 10.7554/eLife.93004 | MS-ring formation is described as essential for initiation, providing the base for later export and axial assembly (arroyoperez2024aconservedcellpole pages 1-2, terashima2020assemblymechanismof pages 1-2). | A useful bridge to the terminal phenotype; avoid implying number control from structural assembly alone. |
| 16 | completed single polar flagellum **realizes** `traitmech:000057` | Definition-level; **high** | 10.1128/JB.00236-20 | “A single flagellum at one of the cell poles (monotrichous flagellum)” (terashima2020assemblymechanismof pages 2-4). | Terminal graph edge. |

## 4. Minimal recommended graph for YAML

A conservative first revision could contain these nodes:

1. FipA;
2. HubP/FimV polar landmark;
3. active GTP-bound FlhF dimer;
4. FlhG/FleN ATPase;
5. polar-system FliG;
6. FliF;
7. polar FliF–FliG initiation complex;
8. MS-ring/C-ring assembly;
9. polar flagellum assembly;
10. `traitmech:000057`.

Recommended edge backbone:

- FipA `promotes_polar_localization_of` FlhF;
- HubP/FimV `anchors_at_cell_pole` FlhF;
- FlhF `binds` polar-system FliG;
- FlhF–FliG `recruits` FliF;
- FliF `assembles_into` MS-ring;
- MS-ring/C-ring initiation `enables` polar flagellum assembly;
- FlhG `stimulates_GTPase_activity_of` FlhF;
- FlhG-mediated FlhF inactivation `negatively_regulates` repeated initiation;
- polar flagellum assembly plus number restriction `results_in` `traitmech:000057`.

This expands the existing 10-node/8-edge summary while preserving a compact causal core. A separate transcription branch through FlrA/FleQ should be added only if the YAML permits taxon-specific subgraphs and its primary evidence is curated independently.

## 5. Recent developments and expert interpretation

### 5.1 2024 molecular resolution of polar confinement

Dornes et al. resolved a longstanding gap between FlhF pole localization and structural initiation. The study showed that FlhF uses different domains as a bridge: its NG GTPase domain binds HubP, and its N-terminal FID binds FliG; the resulting FliG engages FliF. FlhF initially prevents FliG from engaging FliM/FliN, while FlhG-driven FlhF inactivation permits progression of C-ring assembly (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 1-2). This supports a **diffusion–capture and gated-assembly model**, rather than a model in which FlhF directly binds FliF as its primary target.

The study also reconstructed HubP–FlhF–FliG localization in *E. coli*. At least 310 cells per biological replicate across three experiments were counted in the localization analysis, supporting reproducibility of the recruitment cascade, although heterologous expression levels were explicitly acknowledged as nonphysiological (dornes2024polarconfinementof pages 6-7).

### 5.2 2024 discovery of FipA as a licensing factor

Arroyo-Pérez et al. identified FipA as a second polarity determinant operating alongside HubP/FimV. FipA appears at the designated pole before flagellar synthesis and is required for normal synthesis in three distantly related γ-proteobacteria, supporting the authors’ interpretation of FipA as a licensing factor (arroyoperez2024aconservedcellpole pages 1-2).

The effect is not uniform across taxa. In *V. parahaemolyticus*, `ΔfipA` phenocopied `ΔflhF` and abolished flagellation even though FlhF remained polar in about one-third of cells. In *P. putida* and *S. putrefaciens*, deletions reduced flagellar number but often retained some flagellation and swimming. In *S. putrefaciens*, `ΔfipA` reduced number while remaining polar, whereas `ΔflhF` frequently caused delocalization (arroyoperez2024aconservedcellpole pages 12-14, arroyoperez2024aconservedcellpole pages 14-15). Thus, experts should interpret FipA primarily as an **FlhF activity/recruitment factor**, not as a universal positional landmark.

Quantitative localization differences reinforce this conclusion: FipA was diffuse in approximately half of *V. parahaemolyticus* cells, whereas nearly all *P. putida* cells had foci; bipolar-to-unipolar ratios were approximately 1:5 and 1:2, respectively (arroyoperez2024aconservedcellpole pages 12-14).

### 5.3 Mechanistic foundation from 2020 MS-ring reconstitution

Terashima et al. demonstrated that *Vibrio* FliF alone forms MS-rings only rarely in *E. coli*, whereas FlhF coexpression markedly increases ring formation. The rings were approximately 25 nm in diameter, and the MS-ring contains a few dozen FliF molecules (terashima2020assemblymechanismof pages 1-2, terashima2020assemblymechanismof pages 4-6). These results provide the structural initiation link required for a causal graph rather than a mere regulator-to-phenotype association.

## 6. Applications and real-world relevance

1. **Microscopy-based phenotyping and taxonomy.** Flagellar number and arrangement remain species-characteristic morphological attributes. Fluorescent hook/filament labeling and cryo-electron or conventional electron microscopy can operationalize `traitmech:000057`; soft-agar spreading alone cannot.
2. **Synthetic spatial organization.** Reconstitution of the HubP–FlhF–FliG cascade in *E. coli* demonstrates that polar recruitment modules can be transferred into a heterologous chassis, offering a route for engineering membrane-associated macromolecular assembly (dornes2024polarconfinementof pages 6-7).
3. **Motility and colonization control.** Polar flagella support movement along chemical gradients and host/environmental colonization, but interventions against motor function or chemotaxis should not automatically be annotated as changing monotrichous morphology (dornes2024polarconfinementof pages 1-2).
4. **Antimicrobial/antivirulence research.** FlhF, FipA, FliF, and assembly interfaces are plausible intervention points in motile pathogens, but the retrieved studies establish mechanism rather than validated clinical targets. Such application claims should remain prospective.
5. **Comparative cell biology.** The distinction between polar and lateral FliG recognized by FlhF in *S. putrefaciens* offers a system for studying how paralogous nanomachines are spatially insulated in one cell (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 1-2).

## 7. Statistics and assay-level data useful for curation

- Wild-type *S. putrefaciens* showed exclusively polar hooks in approximately **75%** of cells, whereas the FlhF ΔN44 mutant showed approximately **40% subpolar/lateral** and **10% polar** hooks; at least 330 cells per replicate across three experiments were analyzed (dornes2024polarconfinementof pages 4-6).
- Full-length FlhF formed fluorescent foci in approximately **90%** of cells versus approximately **70%** for ΔN44-FlhF; the mutant foci that formed remained polar (dornes2024polarconfinementof pages 4-6).
- Wild-type FlhF localization was monopolar in approximately **92%** of cells; truncating FliG produced pronounced FlhF accumulation at one or both poles, with about **60%** in one category reported in the text (dornes2024polarconfinementof pages 4-6).
- In *V. parahaemolyticus*, polar FlhF persisted in about **one-third** of `ΔfipA` cells despite complete failure to make flagella, demonstrating that localization alone is insufficient (arroyoperez2024aconservedcellpole pages 12-14).
- *B. burgdorferi* normally has **7–11** periplasmic flagella; `flhF` deletion reduced this to **4 ± 2 per cell tip**, illustrating conservation of numerical control but also why this organism is a boundary case rather than direct monotrichous evidence (zhang2020flhfregulatesthe pages 1-2).

## 8. Warnings: claims not ready for TraitMech curation

1. **Do not infer monotrichous morphology from gene presence.** FlhF/FlhG/FipA occur in lophotrichous taxa and regulate other polar patterns (arroyoperez2024aconservedcellpole pages 2-3).
2. **Do not make HubP absolutely required.** Many cells retain normal polar flagella without HubP, and FipA provides a parallel pathway (arroyoperez2024aconservedcellpole pages 14-15, arroyoperez2024aconservedcellpole pages 2-3).
3. **Do not curate “FipA stabilizes GTP-bound FlhF dimers” as established.** The 2024 article presents this as a mechanistic model under active investigation, not a demonstrated biochemical result (arroyoperez2024aconservedcellpole pages 14-15).
4. **Do not generalize the exact HubP–FlhF–FliG domain mechanism to every monotrichous bacterium.** Direct molecular evidence is strongest for *S. putrefaciens*.
5. **Do not equate FimV and HubP identifiers.** They are organism-specific homologous/analogous polar organizers and require separate protein records.
6. **Do not use *P. putida* as direct evidence for the terminal trait.** It is lophotrichous in the comparative study, although its upstream FipA/FlhF biology is relevant (arroyoperez2024aconservedcellpole pages 2-3).
7. **Do not use *B. burgdorferi* periplasmic flagellation as direct evidence.** Its multiple internal flagella are morphologically distinct (zhang2020flhfregulatesthe pages 1-2).
8. **Do not convert soft-agar spreading percentages into flagellar-number measurements.** Spreading combines growth, chemotaxis, motor output, and morphology.
9. **Do not treat FlhF as binding FliF directly in the refined core model.** The 2024 data support FlhF→FliG→FliF, while earlier localization experiments establish FlhF dependence without resolving the bridge (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 1-2).
10. **Do not add environmental causal nodes without direct morphological assays.** Viscosity and ion motive force affect propulsion, but the evidence reviewed here does not show that they generally determine the one-polar-flagellum arrangement.

## 9. DOI-first bibliography

1. **Dornes A, et al.** “Polar confinement of a macromolecular machine by an SRP-type GTPase.” *Nature Communications* 15, 5797. Accepted **5 July 2024**; published July 2024. DOI: [10.1038/s41467-024-50274-4](https://doi.org/10.1038/s41467-024-50274-4). Primary source for HubP–FlhF–FliG–FliF molecular architecture and FlhG-gated progression (dornes2024polarconfinementof pages 1-2).
2. **Arroyo-Pérez EE, Hook JC, et al.** “A conserved cell-pole determinant organizes proper polar flagellum formation.” *eLife* 13:RP93004. Version of record **5 December 2024**. DOI: [10.7554/eLife.93004](https://doi.org/10.7554/eLife.93004). Primary comparative source for FipA (arroyoperez2024aconservedcellpole pages 1-2).
3. **Terashima H, et al.** “Assembly Mechanism of a Supramolecular MS-Ring Complex To Initiate Bacterial Flagellar Biogenesis in *Vibrio* Species.” *Journal of Bacteriology* 202:e00236-20. Published **27 July 2020**. DOI: [10.1128/JB.00236-20](https://doi.org/10.1128/JB.00236-20). Primary source for FlhF-dependent FliF localization and MS-ring reconstitution (terashima2020assemblymechanismof pages 1-2).
4. **Zhang K, et al.** “FlhF regulates the number and configuration of periplasmic flagella in *Borrelia burgdorferi*.” *Molecular Microbiology* 113:1122–1139. **February 2020**. DOI: [10.1111/mmi.14482](https://doi.org/10.1111/mmi.14482). Boundary-case evidence for conserved FlhF numerical and positional control (zhang2020flhfregulatesthe pages 1-2).
5. **Schuhmacher JS, et al.** Existing foundational evidence supplied with the trait record. *FEMS Microbiology Reviews*. DOI: [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034). Supports monotrichous polar flagellation as a regular flagellation pattern.
6. **Flagellum review supplied with the trait record.** *Biomolecules* 9:279. DOI: [10.3390/biom9070279](https://doi.org/10.3390/biom9070279). Supports the helical filament as a locomotory organelle.

## Curation recommendation

The graph is ready for expansion around the **FipA/HubP–FlhF–FliG–FliF–MS-ring** initiation pathway and the antagonistic **FlhG number-control** branch. All mechanistic edges should carry organism scope. The phenotype-generating terminal edge should require direct observation of exactly one polar flagellum; gene content, motility, or polar localization of FlhF alone should not be accepted as sufficient evidence.

References

1. (terashima2020assemblymechanismof pages 2-4): Hiroyuki Terashima, Keiichi Hirano, Yuna Inoue, Takaya Tokano, Akihiro Kawamoto, Takayuki Kato, Erika Yamaguchi, Keiichi Namba, Takayuki Uchihashi, Seiji Kojima, and Michio Homma. Assembly mechanism of a supramolecular ms-ring complex to initiate bacterial flagellar biogenesis in <i>vibrio</i> species. Jul 2020. URL: https://doi.org/10.1128/jb.00236-20, doi:10.1128/jb.00236-20. This article has 29 citations and is from a peer-reviewed journal.

2. (arroyoperez2024aconservedcellpole pages 14-15): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (arroyoperez2024aconservedcellpole pages 2-3): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

4. (dornes2024polarconfinementof pages 1-2): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

5. (arroyoperez2024aconservedcellpole pages 1-2): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

6. (dornes2024polarconfinementof pages 4-6): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

7. (dornes2024polarconfinementof pages 2-4): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

8. (terashima2020assemblymechanismof pages 1-2): Hiroyuki Terashima, Keiichi Hirano, Yuna Inoue, Takaya Tokano, Akihiro Kawamoto, Takayuki Kato, Erika Yamaguchi, Keiichi Namba, Takayuki Uchihashi, Seiji Kojima, and Michio Homma. Assembly mechanism of a supramolecular ms-ring complex to initiate bacterial flagellar biogenesis in <i>vibrio</i> species. Jul 2020. URL: https://doi.org/10.1128/jb.00236-20, doi:10.1128/jb.00236-20. This article has 29 citations and is from a peer-reviewed journal.

9. (terashima2020assemblymechanismof pages 4-6): Hiroyuki Terashima, Keiichi Hirano, Yuna Inoue, Takaya Tokano, Akihiro Kawamoto, Takayuki Kato, Erika Yamaguchi, Keiichi Namba, Takayuki Uchihashi, Seiji Kojima, and Michio Homma. Assembly mechanism of a supramolecular ms-ring complex to initiate bacterial flagellar biogenesis in <i>vibrio</i> species. Jul 2020. URL: https://doi.org/10.1128/jb.00236-20, doi:10.1128/jb.00236-20. This article has 29 citations and is from a peer-reviewed journal.

10. (zhang2020flhfregulatesthe pages 1-2): Kai Zhang, Jun He, Claudio Cantalano, Youzhong Guo, Jun Liu, and Chunhao Li. Flhf regulates the number and configuration of periplasmic flagella in <i>borrelia burgdorferi</i>. Feb 2020. URL: https://doi.org/10.1111/mmi.14482, doi:10.1111/mmi.14482. This article has 32 citations and is from a domain leading peer-reviewed journal.

11. (dornes2024polarconfinementof pages 6-7): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

12. (arroyoperez2024aconservedcellpole pages 12-14): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.