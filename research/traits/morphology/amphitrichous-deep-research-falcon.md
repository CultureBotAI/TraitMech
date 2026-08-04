---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:10:22.423892'
end_time: '2026-08-04T07:16:26.381533'
duration_seconds: 363.96
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: amphitrichous
  trait_identifier: traitmech:000059
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: amphitrichous
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagellar arrangement with flagella (single filaments or tufts) at
    both poles of the cell.
  parent_traits: traitmech:000056
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe bipolar
    (amphitrichous) flagellation among the flagellation patterns governed by FlhF/FlhG.)
    | DOI:10.3390/biom9070279:  (Flagellum review supports polar flagellar filaments
    as locomotory organelles.)'
  causal_graph_summary: 'amphitrichous_bipolar_flagella: 11 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** amphitrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000059
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella (single filaments or tufts) at both poles of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe bipolar (amphitrichous) flagellation among the flagellation patterns governed by FlhF/FlhG.) | DOI:10.3390/biom9070279:  (Flagellum review supports polar flagellar filaments as locomotory organelles.)
- **Existing causal graph summary:** amphitrichous_bipolar_flagella: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **amphitrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/amphitrichous.yaml`.

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
- **Trait label:** amphitrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000059
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella (single filaments or tufts) at both poles of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe bipolar (amphitrichous) flagellation among the flagellation patterns governed by FlhF/FlhG.) | DOI:10.3390/biom9070279:  (Flagellum review supports polar flagellar filaments as locomotory organelles.)
- **Existing causal graph summary:** amphitrichous_bipolar_flagella: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **amphitrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/amphitrichous.yaml`.

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


# Curation-focused research report: amphitrichous

## Record and scope summary

- **Trait:** amphitrichous
- **Identifier:** `traitmech:000059`
- **Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED
- **Parent:** `traitmech:000056`
- **Working definition:** a flagellar arrangement in which flagellar filaments occur at both cell poles. Under the supplied TraitMech definition, either a single filament or a tuft may occupy each pole.

The phenotype is an **observed spatial arrangement**, not merely possession of flagellar genes, swimming ability, polar flagella, or bipolar localization of a regulatory protein. *Campylobacter jejuni* is the best experimentally developed amphitrichous model: it is described as carrying a single flagellum at each pole, although culture populations can contain cells flagellated at only one pole. Reviews also list *Magnetospirillum magneticum* as amphitrichous. (liang2018flhf(t368a)modulatesmotility pages 11-14, grognot2021morethanpropellers pages 4-5)

### Boundary cases

1. **Monotrichous:** one flagellum at one pole; not amphitrichous.
2. **Unipolar lophotrichous:** a tuft at only one pole; not amphitrichous.
3. **Bipolar lophotrichous:** a tuft at each pole, exemplified by *Helicobacter suis*. This satisfies the supplied broad definition but should be qualified as `bipolar_lophotrichous`, because some literature treats it as distinct from amphitrichous sensu stricto, meaning approximately one filament per pole. (grognot2021morethanpropellers pages 5-7, grognot2021morethanpropellers pages 1-2)
4. **Peritrichous:** flagella distributed over the cell surface rather than restricted to both poles. (grognot2021morethanpropellers pages 2-4, schuhmacher2015howbacteriamaintain pages 2-4)
5. **Transient predivision bipolarity:** a normally monotrichous organism may place assembly factors or a nascent flagellum at the future daughter pole before cytokinesis. Neither bipolar FlhF/FipA foci nor this cell-cycle intermediate alone establishes an amphitrichous species-level phenotype. (arroyoperez2024aconservedcellpole pages 12-14, schuhmacher2015howbacteriamaintain pages 4-5)
6. **Motility:** swimming is a functional consequence, not the defining morphology. Nonmotile cells may retain bipolar filaments, while motile cells need not be amphitrichous.

## Current mechanistic understanding

The strongest amphitrichous-specific model combines two layers:

1. **Placement/number control:** the SRP-family GTPase FlhF and MinD-family ATPase FlhG regulate polar flagellar position and number. In amphitrichous *C. jejuni*, loss of `flhF` abolishes flagella, whereas loss of `flhG` produces hyperflagellation; the latter was also associated with minicell/cell-division defects. These observations establish necessity for correct morphology but do not, by themselves, explain how the two poles are selected. (schuhmacher2015howbacteriamaintain pages 5-7)
2. **Assembly-coupled transcription:** FliF, FliG, and the flagellar type III secretion system form an early assembly checkpoint sensed by FlgS. FlgS→FlgR signaling, together with σ54, activates rod and hook transcription; later hook completion permits σ28-dependent filament and motor completion. This pathway is demonstrated directly in amphitrichous *C. jejuni*. (burnham2020apolarflagellar pages 2-4)

Recent 2024 studies refine the physical mechanism for **polar** assembly. In *Shewanella putrefaciens*, FlhF binds the landmark HubP through its NG domain and binds FliG through an N-terminal FliG-interaction domain. FlhF-bound FliG can engage the MS-ring protein FliF while initially excluding FliM/FliN, suggesting a regulated diffusion-capture and assembly-checkpoint mechanism. This is compelling mechanistic evidence for polar localization, but it is not yet direct evidence for selecting both poles in an amphitrichous organism. (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 7-8)

A second 2024 study identified FipA as a membrane-associated FlhF partner. FipA promotes FlhF activity and polar accumulation, while FipA and HubP provide partly independent inputs. FipA can exhibit uni- or bipolar localization, but the work used *Vibrio parahaemolyticus*, *Pseudomonas putida*, and *S. putrefaciens*, not a validated amphitrichous model. (arroyoperez2024aconservedcellpole pages 14-15, arroyoperez2024aconservedcellpole pages 12-14)

## Candidate nodes

### Trait and taxon nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| amphitrichous flagellar arrangement | `traitmech:000059` | Target morphology; preserve identifier verbatim. |
| *Campylobacter jejuni* | `NCBITaxon:197` | Strongest direct mechanistic taxon. Strain-specific experiments should additionally identify PT14, 81-176, or the relevant strain. |
| *Magnetospirillum magneticum* | Label plus verified NCBITaxon ID before use | Morphological example, but the retrieved evidence does not establish the same mechanism. |
| bipolar-lophotrichous *Helicobacter suis* | Label plus verified NCBITaxon ID before use | Boundary/subtype example, not evidence for a universal amphitrichous mechanism. |

### Genes and proteins

| Node | Function in candidate graph | Grounding recommendation |
|---|---|---|
| FlhF | SRP-type GTPase controlling polar placement and assembly | Use gene symbol plus strain-specific UniProt accession only after sequence verification. |
| FlhG/FleN | MinD-like ATPase controlling flagellar number; stimulates FlhF GTPase | Gene symbol; strain-resolved UniProt required. |
| HubP/FimV | Polar landmark binding FlhF | **Uncertain for amphitrichous graph**; demonstrated in other polar systems. |
| FipA/DUF2802 protein | Membrane FlhF partner/pole-licensing factor | **Uncertain and taxon-specific**. |
| FliF | Flagellar MS-ring protein | Component of the assembly checkpoint. |
| FliG | Rotor/C-ring protein and FlhF-binding assembly intermediate | Direct checkpoint role in *C. jejuni*; direct FlhF binding shown in *S. putrefaciens*. |
| FliM and FliN | C-ring switch proteins | Do not merge with FliG; checkpoint requirements differ. |
| FlhA, FlhB, FliP, FliQ, FliR | fT3SS core proteins | Group node is acceptable if individual edges are not needed. |
| FlgS | Sensor histidine kinase detecting assembled MS-ring/rotor/fT3SS | Direct in *C. jejuni*. |
| FlgR | Response regulator activating σ54-dependent genes | Direct in *C. jejuni*. |
| RpoN/σ54 | Sigma factor for rod/hook transcription | Use strain-specific gene/protein grounding. |
| FliA/σ28 and FlgM | Late flagellar transcription factor and anti-sigma factor | Downstream completion module; not specific to bipolar placement. |

### Structures, localizations, and processes

- Cell pole; old pole; new pole; bipolar localization.
- Flagellum and flagellar filament — candidate `GO:0009288` for bacterial-type flagellum.
- Flagellar MS ring, C ring/rotor, rod, hook, and motor.
- Flagellar type III secretion system — candidate `GO:0030694`.
- Bacterial-type flagellum-dependent cell motility — candidate `GO:0071973`.
- Flagellum assembly, protein localization to cell pole, GTPase activity, ATPase activity, two-component signaling, σ54-dependent transcription, and cell division.

### Chemicals and experimental factors

- GTP `CHEBI:15996`; GDP `CHEBI:17552`.
- ATP `CHEBI:15422`; ADP `CHEBI:16761`.
- Magnesium ion should be grounded only after checking the current ChEBI record.
- Experimental factors: `flhF` deletion/insertion, `flhG` deletion, FlhF(T368A), genetic complementation, protein overexpression, growth temperature, growth phase, TEM/cryo-ET, motility agar, fluorescent focus localization, two-hybrid/pulldown, and transcriptional reporters.
- Environmental/nutrient inputs are not presently supported as direct causes of amphitrichous placement. Do not add oxygen, pH, mucin, or medium components without trait-specific perturbation evidence.

## Candidate causal edges

The following artifact gives the compact high-confidence set and separates direct evidence from extrapolation.

| subject | predicate | object | confidence/scope | key evidence |
|---|---|---|---|---|
| FlhF | enables assembly of | bipolar flagella / amphitrichous state | **High; direct in *Campylobacter jejuni*** | *flhF* deletion caused “absence of flagella,” while WT cells showed “typical bipolar flagella”; review states in amphitrichous *C. jejuni*, *flhF* deletion caused absence of flagella (liang2018flhf(t368a)modulatesmotility pages 14-17, schuhmacher2015howbacteriamaintain pages 5-7) |
| FlhF GTPase integrity | supports | flagellar assembly and motility | **High; direct in *C. jejuni*** | FlhF(T368A) impaired GTPase activity/stability; only ~24% of cells had single polar flagella and motility was reduced to ~50% of WT, indicating intact FlhF GTPase function supports proper bipolar assembly and swimming (liang2018flhf(t368a)modulatesmotility pages 4-8, liang2018flhf(t368a)modulatesmotility pages 1-4) |
| assembled FliF/FliG/fT3SS complex | activates via checkpoint sensing | FlgSR two-component system | **High; direct in *C. jejuni*** | “fT3SS core proteins… the FliF MS ring, and FliG rotor… form a regulatory checkpoint”; “FlgSR… detects MS ring-rotor-fT3SS formation to directly activate σ54-dependent flagellar rod and hook gene expression” (burnham2020apolarflagellar pages 2-4) |
| FlgR + σ54 | activates transcription of | flagellar rod and hook genes | **High; direct in *C. jejuni*** | “signal transduction through… FlgSR… results in phosphorylation… to promote… directly assist σ54 in activating transcription of rod and hook genes”; in *C. jejuni*, rod/hook expression is “dependent upon σ54 [and] the FlgSR TCS” (burnham2020apolarflagellar pages 2-4) |
| HubP/FimV | binds | FlhF NG domain | **Uncertain for amphitrichous; 2024 *S. putrefaciens* / general polar extrapolation** | 2024 work: “NG domain of FlhF interacts with the C-terminal domain of the landmark protein HubP”; mechanism shown in polar system, not direct amphitrichous evidence (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 7-8) |
| FlhF FID/B-domain | binds | FliG | **Uncertain for amphitrichous; 2024 *S. putrefaciens* / general polar extrapolation** | Y2H/pulldown showed FlhF interacts strongly with FliG; the B-domain/FID was “necessary and sufficient” for the interaction (dornes2024polarconfinementof pages 2-4) |
| FliG | engages | FliF | **Uncertain for amphitrichous; 2024 *S. putrefaciens* / general polar extrapolation** | In vitro, “FlhF-tethered FliG can interact with FliF-C,” supporting a pole-assembly tether model; not tested in amphitrichous bacteria (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 7-8) |
| FipA | promotes polar/active accumulation of | FlhF | **Uncertain for amphitrichous; 2024 γ-proteobacterial polar extrapolation** | 2024 study found FipA is “required for normal FlhF activity and function in polar flagellar synthesis”; deletion decreased polar FlhF localization, and FipA/HubP together recruit enough active FlhF for assembly (arroyoperez2024aconservedcellpole pages 14-15, arroyoperez2024aconservedcellpole pages 12-14) |


*Table: This table summarizes the strongest candidate causal edges for curating traitmech:000059 amphitrichous, separating direct Campylobacter jejuni evidence from broader 2024 polar-flagellation mechanisms that should be marked taxon-specific and uncertain.*

A fuller curation table follows. “High” denotes direct evidence in amphitrichous *C. jejuni*; “medium/uncertain” denotes broader polar-flagellation evidence requiring a taxon qualifier.

| Subject | Predicate | Object | Evidence snippet | Reference | Curation note |
|---|---|---|---|---|---|
| FlhF | enables | bipolar polar-flagellum assembly | Wild-type *C. jejuni* showed “typical bipolar flagella”; `flhF` inactivation caused “complete loss of flagella structures.” | Liang & Connerton, 2018, DOI [10.1111/mmi.14120](https://doi.org/10.1111/mmi.14120) (liang2018flhf(t368a)modulatesmotility pages 14-17, liang2018flhf(t368a)modulatesmotility pages 4-8) | **High; curate.** Taxon-specific to *C. jejuni*. |
| intact FlhF GTPase function | promotes | correct bipolar assembly | FlhF(T368A) impaired GTPase activity/stability; only 24% of cells bore a single polar flagellum rather than the normal bipolar state. | DOI [10.1111/mmi.14120](https://doi.org/10.1111/mmi.14120) (liang2018flhf(t368a)modulatesmotility pages 14-17, liang2018flhf(t368a)modulatesmotility pages 4-8) | **High; curate**, but phrase as enabling normal assembly, not proving a two-pole selector. |
| correct bipolar flagellation | enables | efficient swimming motility | `flhF` null cells were nonmotile; complementation restored approximately 90% motility, with 88% of cells displaying polar flagella. | DOI [10.1111/mmi.14120](https://doi.org/10.1111/mmi.14120) (liang2018flhf(t368a)modulatesmotility pages 4-8) | **High but downstream.** Motility is not part of the morphology definition. |
| FlhF(T368A) | reduces | swimming motility | Swarming was about 50% of wild type and measurable only at 42°C in the reported assay. | DOI [10.1111/mmi.14120](https://doi.org/10.1111/mmi.14120) (liang2018flhf(t368a)modulatesmotility pages 4-8) | **Assay- and strain-specific.** |
| FlhG | limits | flagellar number | Review of direct *C. jejuni* work: `flhG` deletion yielded hyperflagellated cells. | Schuhmacher et al., 2015, DOI [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034) (schuhmacher2015howbacteriamaintain pages 5-7) | **High for number control.** Avoid asserting that FlhG alone specifies both poles. |
| FlhG perturbation | disrupts | normal cell division | `flhG`-associated phenotypes included “minicell” defects. | DOI [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034) (schuhmacher2015howbacteriamaintain pages 5-7) | **Potential pleiotropy.** Keep separate from the morphology edge. |
| FliF–FliG–fT3SS assembled complex | is detected by | FlgS | The proteins assemble into a “regulatory checkpoint”; FlgS physically interacted with FliF/FliG only after multimerization around the fT3SS core. | Burnham et al., 2020, DOI [10.1128/mBio.03107-19](https://doi.org/10.1128/mBio.03107-19) (burnham2020apolarflagellar pages 2-4) | **High; curate** as an assembly module in *C. jejuni*. |
| FlgS | activates through phosphotransfer | FlgR | Checkpoint detection initiates phosphotransfer to the FlgR response regulator. | DOI [10.1128/mBio.03107-19](https://doi.org/10.1128/mBio.03107-19) (burnham2020apolarflagellar pages 2-4) | **High; curate.** |
| phosphorylated FlgR + σ54 | activates transcription of | flagellar rod/hook genes | FlgR works with σ54 for rod and hook gene expression. | DOI [10.1128/mBio.03107-19](https://doi.org/10.1128/mBio.03107-19) (burnham2020apolarflagellar pages 2-4) | **High; curate.** Necessary for flagellum completion but not uniquely bipolar. |
| hook completion / fT3SS substrate switch | causes export of | FlgM | Hook completion promotes secretion of the anti-σ factor FlgM. | DOI [10.1128/mBio.03107-19](https://doi.org/10.1128/mBio.03107-19) (burnham2020apolarflagellar pages 2-4) | **Moderate for this trait graph:** general late assembly edge. |
| FlgM export | releases inhibition of | σ28 | FlgM secretion derepresses σ28-dependent transcription of flagellins and late motor proteins. | DOI [10.1128/mBio.03107-19](https://doi.org/10.1128/mBio.03107-19) (burnham2020apolarflagellar pages 2-4) | **Moderate:** curate only if graph depth includes filament completion. |
| HubP/FimV | binds/tethers | FlhF NG domain at pole | “The NG domain of FlhF interacts with the C-terminal domain” of HubP. | Dornes et al., 2024, DOI [10.1038/s41467-024-50274-4](https://doi.org/10.1038/s41467-024-50274-4), published July 2024 (dornes2024polarconfinementof pages 7-8) | **Uncertain for amphitrichous curation:** direct in *S. putrefaciens*. |
| FlhF FID domain | binds | polar FliG | The N-terminal domain was necessary and sufficient for FlhF–FliG interaction; lateral-system FliG did not interact. | DOI [10.1038/s41467-024-50274-4](https://doi.org/10.1038/s41467-024-50274-4) (dornes2024polarconfinementof pages 2-4) | **Uncertain/taxon-specific.** |
| FlhF-bound FliG | recruits/engages | FliF | “FlhF-tethered FliG can interact with FliF-C.” | DOI [10.1038/s41467-024-50274-4](https://doi.org/10.1038/s41467-024-50274-4) (dornes2024polarconfinementof pages 2-4) | **Mechanistically strong but not amphitrichous-specific.** |
| FlhF binding to FliG | initially prevents | FliG–FliM/FliN interaction | FlhF was an “impediment” to FliG engagement with FliM/FliN. | DOI [10.1038/s41467-024-50274-4](https://doi.org/10.1038/s41467-024-50274-4) (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 7-8) | **Uncertain:** biochemical mechanism from another polar system. |
| FlhG | stimulates | FlhF GTPase activity | The 2024 model places FlhG stimulation upstream of progression in C-ring assembly. | DOI [10.1038/s41467-024-50274-4](https://doi.org/10.1038/s41467-024-50274-4) (dornes2024polarconfinementof pages 7-8) | **Conserved-biochemistry candidate**, but qualify by organism. |
| FipA | promotes | active/polar FlhF accumulation | FipA interacts with FlhF; deletion reduces polar FlhF, while combined `fipA hubP` deletion nearly eliminates polar accumulation. | Arroyo-Pérez et al., 2024, DOI [10.7554/eLife.93004.3](https://doi.org/10.7554/eLife.93004.3), published December 2024 (arroyoperez2024aconservedcellpole pages 14-15) | **Do not yet curate as a core amphitrichous edge.** |
| FlhF(T368A)-dependent flagellar reduction | reduces | bacteriophage adsorption/infection | The mutation reduced the phage adsorption constant and infection efficiency. | DOI [10.1111/mmi.14120](https://doi.org/10.1111/mmi.14120) (liang2018flhf(t368a)modulatesmotility pages 1-4) | **Application edge only; indirect and phage/strain-specific.** |

## Recent developments and expert analysis

### 2024: molecular tethering of a polar flagellar precursor

Dornes and colleagues moved the field beyond the older statement that FlhF merely “marks” a pole. Their biochemical and structural model makes FlhF a physical bridge: HubP–FlhF–FliG–FliF. The work also introduces a checkpoint in which FlhF permits FliG–FliF association while delaying FliM/FliN addition. This is a major advance in explaining how a membrane-diffusing MS-ring precursor can be captured at a pole. However, the authors note substantial species-to-species variation in HubP phenotypes—loss of HubP has minor, severe, or even opposite effects in different polar flagellates—so the mechanism must not be universalized to amphitrichous bacteria without direct tests. (dornes2024polarconfinementof pages 7-8)

### 2024: FipA as a pole-licensing factor

Arroyo-Pérez and colleagues identified FipA as a conserved FlhF-interacting membrane protein. Its dynamic localization before flagellar synthesis suggests “licensing” rather than simply becoming part of the mature organelle. In *P. putida*, FipA foci occurred at an approximately 1:2 bipolar:unipolar ratio, compared with approximately 1:5 in *V. parahaemolyticus*. These are protein-localization statistics, not amphitrichous flagellation frequencies. (arroyoperez2024aconservedcellpole pages 12-14)

### Interpretation for TraitMech

The current evidence supports a compact core graph centered on **FlhF/FlhG placement-number control plus FlgSR/σ54 assembly-coupled transcription**. HubP, FipA, and the detailed FlhF–FliG–FliF tether are valuable extension nodes, but they should either be omitted from the initial general graph or represented with explicit organism qualifiers and `uncertain: true`. The major unsolved step is how an amphitrichous cell distinguishes and licenses **both** poles rather than one designated pole.

## Applications and real-world relevance

- **Pathogen motility:** correct bipolar flagellation supports *C. jejuni* motility, which is biologically relevant to movement through host-associated environments. The evidence retrieved here directly supports motility effects but does not quantify colonization or disease risk. (liang2018flhf(t368a)modulatesmotility pages 4-8)
- **Phage susceptibility:** FlhF(T368A)-driven loss/truncation of flagella reduced phage adsorption and infection efficiency, illustrating how perturbing flagellar architecture can alter receptor availability and stabilize a bacteriophage carrier state. This is a strain-specific application, not a defining causal edge for amphitrichy. (liang2018flhf(t368a)modulatesmotility pages 1-4)
- **Motility engineering and synthetic cell polarity:** the HubP/FipA/FlhF modules provide candidate handles for repositioning or changing the number of polar nanomachines. This remains an engineering prospect rather than a demonstrated amphitrichous implementation.
- **Phenotype annotation and diagnostics:** TEM, cryo-electron tomography, or validated filament staining is necessary to distinguish true bipolar filaments from regulatory foci or motility alone.

## Recommended minimal graph for `amphitrichous.yaml`

A conservative first-pass graph could contain the following nodes and edges:

1. `FlhF --positively_regulates--> polar_flagellum_assembly`
2. `FlhF_GTPase_activity --enables--> correct_bipolar_flagellation`
3. `FlhG --negatively_regulates--> flagellar_number`
4. `FliF_FliG_fT3SS_checkpoint --activates--> FlgS_FlgR_signaling`
5. `FlgR_sigma54_complex --activates--> rod_and_hook_gene_transcription`
6. `rod_and_hook_assembly --enables--> flagellar_filament_completion`
7. `flagellar_filament_at_both_poles --realizes--> traitmech:000059`
8. `traitmech:000059 --contributes_to--> swimming_motility`

Edges 1–6 should carry a *C. jejuni* taxon context unless the evidence field explicitly cites broader polar-flagellate support. Edge 8 is downstream and non-definitional.

## Warnings: claims not ready for curation

1. **Do not assert that HubP or FipA is required for amphitrichy generally.** The strongest 2024 evidence comes from mono- or lophotrichous/polar γ-proteobacteria, and HubP effects vary by species. (arroyoperez2024aconservedcellpole pages 14-15, dornes2024polarconfinementof pages 7-8)
2. **Do not equate bipolar protein foci with bipolar flagella.** FipA or FlhF localization must be paired with filament/basal-body imaging.
3. **Do not infer a universal FlhF/FlhG phenotype across taxa.** For example, FlhG loss can cause hyperflagellation in *C. jejuni* but lack of flagella in lophotrichous *H. pylori*. (schuhmacher2015howbacteriamaintain pages 5-7)
4. **Do not make FlgSR/σ54 the two-pole selection mechanism.** It controls assembly-coupled transcription; available evidence does not show that it chooses both poles.
5. **Do not curate phage resistance, virulence, colonization, mucin penetration, pH preference, or temperature preference as intrinsic amphitrichous consequences.** The retrieved findings are indirect, strain-specific, or assay-specific.
6. **Do not assign protein UniProt CURIEs without a strain context.** Ortholog names are conserved, but sequences and functions differ. Label-only nodes are safer than incorrect accessions.
7. **Treat “single flagellum at one or both poles” carefully.** Population heterogeneity means individual cells observed with one polar filament do not satisfy the strict two-pole phenotype at that time; curate the assay prevalence and growth phase where available. (liang2018flhf(t368a)modulatesmotility pages 1-4)

## DOI-first bibliography

1. **Arroyo-Pérez EE et al.** “A conserved cell-pole determinant organizes proper polar flagellum formation.” *eLife* 13. Published December 2024. DOI: [10.7554/eLife.93004.3](https://doi.org/10.7554/eLife.93004.3). (arroyoperez2024aconservedcellpole pages 14-15, arroyoperez2024aconservedcellpole pages 12-14)
2. **Dornes A et al.** “Polar confinement of a macromolecular machine by an SRP-type GTPase.” *Nature Communications* 15, 5797. Published July 2024. DOI: [10.1038/s41467-024-50274-4](https://doi.org/10.1038/s41467-024-50274-4). (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 7-8)
3. **Bansil R et al.** “Motility of Different Gastric *Helicobacter* spp.” *Microorganisms* 11, 634. Published March 2023. DOI: [10.3390/microorganisms11030634](https://doi.org/10.3390/microorganisms11030634). Relevant mainly to bipolar-lophotrichous boundary cases.
4. **Grognot M, Taute KM.** “More than propellers: how flagella shape bacterial motility behaviors.” *Current Opinion in Microbiology* 61:73–81. Published June 2021. DOI: [10.1016/j.mib.2021.02.005](https://doi.org/10.1016/j.mib.2021.02.005). (grognot2021morethanpropellers pages 4-5, grognot2021morethanpropellers pages 5-7, grognot2021morethanpropellers pages 1-2)
5. **Burnham PM, Kolar WP, Hendrixson DR.** “A Polar Flagellar Transcriptional Program Mediated by Diverse Two-Component Signal Transduction Systems and Basal Flagellar Proteins Is Broadly Conserved in Polar Flagellates.” *mBio* 11:e03107-19. Published April 2020. DOI: [10.1128/mBio.03107-19](https://doi.org/10.1128/mBio.03107-19). (burnham2020apolarflagellar pages 2-4, burnham2020apolarflagellar pages 7-9)
6. **Liang L, Connerton IF.** “FlhF(T368A) modulates motility in the bacteriophage carrier state of *Campylobacter jejuni*.” *Molecular Microbiology* 110:616–633. Published October 2018. DOI: [10.1111/mmi.14120](https://doi.org/10.1111/mmi.14120). (liang2018flhf(t368a)modulatesmotility pages 14-17, liang2018flhf(t368a)modulatesmotility pages 4-8, liang2018flhf(t368a)modulatesmotility pages 1-4)
7. **Schuhmacher JS, Thormann KM, Bange G.** “How bacteria maintain location and number of flagella?” *FEMS Microbiology Reviews* 39:812–822. Published November 2015. DOI: [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034). (schuhmacher2015howbacteriamaintain pages 5-7, schuhmacher2015howbacteriamaintain pages 2-4)

References

1. (liang2018flhf(t368a)modulatesmotility pages 11-14): Lu Liang and Ian F. Connerton. Flhf(t368a) modulates motility in the bacteriophage carrier state of campylobacter jejuni. Molecular Microbiology, 110:616-633, Oct 2018. URL: https://doi.org/10.1111/mmi.14120, doi:10.1111/mmi.14120. This article has 15 citations and is from a domain leading peer-reviewed journal.

2. (grognot2021morethanpropellers pages 4-5): Marianne Grognot and Katja M Taute. More than propellers: how flagella shape bacterial motility behaviors. Jun 2021. URL: https://doi.org/10.1016/j.mib.2021.02.005, doi:10.1016/j.mib.2021.02.005. This article has 103 citations and is from a peer-reviewed journal.

3. (grognot2021morethanpropellers pages 5-7): Marianne Grognot and Katja M Taute. More than propellers: how flagella shape bacterial motility behaviors. Jun 2021. URL: https://doi.org/10.1016/j.mib.2021.02.005, doi:10.1016/j.mib.2021.02.005. This article has 103 citations and is from a peer-reviewed journal.

4. (grognot2021morethanpropellers pages 1-2): Marianne Grognot and Katja M Taute. More than propellers: how flagella shape bacterial motility behaviors. Jun 2021. URL: https://doi.org/10.1016/j.mib.2021.02.005, doi:10.1016/j.mib.2021.02.005. This article has 103 citations and is from a peer-reviewed journal.

5. (grognot2021morethanpropellers pages 2-4): Marianne Grognot and Katja M Taute. More than propellers: how flagella shape bacterial motility behaviors. Jun 2021. URL: https://doi.org/10.1016/j.mib.2021.02.005, doi:10.1016/j.mib.2021.02.005. This article has 103 citations and is from a peer-reviewed journal.

6. (schuhmacher2015howbacteriamaintain pages 2-4): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 167 citations and is from a domain leading peer-reviewed journal.

7. (arroyoperez2024aconservedcellpole pages 12-14): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

8. (schuhmacher2015howbacteriamaintain pages 4-5): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 167 citations and is from a domain leading peer-reviewed journal.

9. (schuhmacher2015howbacteriamaintain pages 5-7): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 167 citations and is from a domain leading peer-reviewed journal.

10. (burnham2020apolarflagellar pages 2-4): Peter M. Burnham, William P. Kolar, and David R. Hendrixson. A polar flagellar transcriptional program mediated by diverse two-component signal transduction systems and basal flagellar proteins is broadly conserved in polar flagellates. Apr 2020. URL: https://doi.org/10.1128/mbio.03107-19, doi:10.1128/mbio.03107-19. This article has 22 citations and is from a domain leading peer-reviewed journal.

11. (dornes2024polarconfinementof pages 2-4): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

12. (dornes2024polarconfinementof pages 7-8): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 11 citations and is from a highest quality peer-reviewed journal.

13. (arroyoperez2024aconservedcellpole pages 14-15): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 7 citations and is from a domain leading peer-reviewed journal.

14. (liang2018flhf(t368a)modulatesmotility pages 14-17): Lu Liang and Ian F. Connerton. Flhf(t368a) modulates motility in the bacteriophage carrier state of campylobacter jejuni. Molecular Microbiology, 110:616-633, Oct 2018. URL: https://doi.org/10.1111/mmi.14120, doi:10.1111/mmi.14120. This article has 15 citations and is from a domain leading peer-reviewed journal.

15. (liang2018flhf(t368a)modulatesmotility pages 4-8): Lu Liang and Ian F. Connerton. Flhf(t368a) modulates motility in the bacteriophage carrier state of campylobacter jejuni. Molecular Microbiology, 110:616-633, Oct 2018. URL: https://doi.org/10.1111/mmi.14120, doi:10.1111/mmi.14120. This article has 15 citations and is from a domain leading peer-reviewed journal.

16. (liang2018flhf(t368a)modulatesmotility pages 1-4): Lu Liang and Ian F. Connerton. Flhf(t368a) modulates motility in the bacteriophage carrier state of campylobacter jejuni. Molecular Microbiology, 110:616-633, Oct 2018. URL: https://doi.org/10.1111/mmi.14120, doi:10.1111/mmi.14120. This article has 15 citations and is from a domain leading peer-reviewed journal.

17. (burnham2020apolarflagellar pages 7-9): Peter M. Burnham, William P. Kolar, and David R. Hendrixson. A polar flagellar transcriptional program mediated by diverse two-component signal transduction systems and basal flagellar proteins is broadly conserved in polar flagellates. Apr 2020. URL: https://doi.org/10.1128/mbio.03107-19, doi:10.1128/mbio.03107-19. This article has 22 citations and is from a domain leading peer-reviewed journal.