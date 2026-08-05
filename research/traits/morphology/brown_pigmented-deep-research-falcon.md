---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:20:16.072983'
end_time: '2026-08-04T07:28:30.974281'
duration_seconds: 494.9
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: brown pigmented
  trait_identifier: METPO:1003023
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: brown_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    brown due to accumulation of brown pigments such as pyomelanin or other melanins.
  parent_traits: METPO:1003021
  synonyms: Pigment_brown
  evidence_summary: 'DOI:10.1128/AEM.67.8.3463-3468.2001: Brown pigments are produced
    when homogentisic acid accumulates (Supports brown microbial pigmentation as a
    homogentisic-acid/pyomelanin pathway phenotype.)'
  causal_graph_summary: 'brown_pigmented_pyomelanin_pathway: 10 nodes, 10 edges'
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
- **Trait label:** brown pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003023
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear brown due to accumulation of brown pigments such as pyomelanin or other melanins.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_brown
- **Existing evidence:** DOI:10.1128/AEM.67.8.3463-3468.2001: Brown pigments are produced when homogentisic acid accumulates (Supports brown microbial pigmentation as a homogentisic-acid/pyomelanin pathway phenotype.)
- **Existing causal graph summary:** brown_pigmented_pyomelanin_pathway: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **brown pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/brown_pigmented.yaml`.

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
- **Trait label:** brown pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003023
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear brown due to accumulation of brown pigments such as pyomelanin or other melanins.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_brown
- **Existing evidence:** DOI:10.1128/AEM.67.8.3463-3468.2001: Brown pigments are produced when homogentisic acid accumulates (Supports brown microbial pigmentation as a homogentisic-acid/pyomelanin pathway phenotype.)
- **Existing causal graph summary:** brown_pigmented_pyomelanin_pathway: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **brown pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/brown_pigmented.yaml`.

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


# Curation report: microbial **brown pigmented** phenotype

## Executive summary

The target is the reviewed morphology class **“brown pigmented”**, identifier **`METPO:1003023`**, parent `METPO:1003021`, synonym *Pigment_brown*. It represents an assay-observed brown, reddish-brown, dark-brown, or brown-black appearance of microbial colonies, cells, or their surrounding medium. It does **not** by itself specify a pigment chemistry.

The strongest reusable mechanism is the homogentisate/pyomelanin pathway: L-tyrosine is transaminated to 4-hydroxyphenylpyruvate (4-HPP), HppD converts 4-HPP to homogentisate (HGA), HGA is exported, and extracellular HGA undergoes oxygen-dependent auto-oxidation and polymerization into pyomelanin. Functional HmgA instead consumes HGA; therefore, loss or impairment of HmgA increases HGA accumulation and brown pigmentation. This pathway has direct genetic support in bacteria and fungi. However, brown color is not diagnostic of pyomelanin, and HatABCDE-mediated export should presently remain *Pseudomonas aeruginosa*–specific. (wang2015identificationandmolecular pages 1-2, pavan2020melaninbiosynthesisin pages 3-4, schmalerripcke2009productionofpyomelanin pages 1-2, hunter2010aputativeabc pages 1-2)

| Graph module | Strongest candidate nodes | Canonical causal direction | Confidence | Principal caveat |
|---|---|---|---|---|
| Tyrosine/HppD synthesis | L-tyrosine; tyrosine aminotransferase; 4-hydroxyphenylpyruvate; HppD (4-hydroxyphenylpyruvate dioxygenase); homogentisic acid | L-tyrosine → 4-hydroxyphenylpyruvate → homogentisic acid via aminotransferase + HppD; loss of hppD abolishes HGA/pyomelanin in tested bacteria and fungi (urbaniak2023invitroand pages 1-2, schmalerripcke2009productionofpyomelanin pages 1-2, wang2015identificationandmolecular pages 9-11, ahmad2016geneticdeterminantsfor pages 1-2) | High | Aminotransferase gene identity varies by taxon (e.g., tyrB, aspC); pathway is strongly supported for pyomelanin but not all brown pigments |
| HmgA competing catabolism | homogentisic acid; HmgA (homogentisate 1,2-dioxygenase); maleylacetoacetate | Functional HmgA diverts homogentisic acid away from pyomelanin; hmgA loss or inactivating mutation causes HGA accumulation and increased pigmentation (pavan2020melaninbiosynthesisin pages 3-4, schmalerripcke2009productionofpyomelanin pages 1-2, moustafa2024mutationofhmga pages 1-2, moustafa2024mutationofhmga pages 4-7) | High | Exact downstream central-pathway architecture differs among taxa; some genomes contain distant or apparently inactive HmgA homologs |
| HatABCDE export | homogentisic acid; HatABCDE ABC transporter operon; cytosol; extracellular milieu | Intracellular HGA accumulation induces hatABCDE expression, and HatABCDE promotes HGA export to the medium, enabling extracellular pyomelanin production (hunter2010aputativeabc pages 1-2, hunter2010aputativeabc pages 5-6) | Medium | Transport evidence is strong but mainly from Pseudomonas aeruginosa; exporter role should be curated as taxon-specific unless generalized further |
| Extracellular aerobic oxidation/polymerization | homogentisic acid; oxygen; benzoquinone acetic acid; pyomelanin polymer | Secreted HGA auto-oxidizes under aerobic conditions to benzoquinone acetic acid and polymerizes into pyomelanin extracellularly (urbaniak2023invitroand pages 1-2, wang2015identificationandmolecular pages 1-2, moustafa2024mutationofhmga pages 1-2) | High | Polymer chemistry is heterogeneous; exact intermediate sequence and polymer structure remain incompletely resolved |
| Brown phenotype expression | pyomelanin; colony/cell-surrounding medium brown pigment; extracellular polymer | Pyomelanin accumulation produces a dark brown, black-brown, or reddish-brown visible phenotype in colonies, cells, or supernatant (urbaniak2023invitroand pages 1-2, hunter2010aputativeabc pages 1-2, jiang2021pyomelaninproducingbrevundimonasvitisensis pages 1-2, elzawawy2024bioproductionandoptimization pages 1-2) | High | Color shade is assay- and taxon-dependent; brown phenotype alone is not diagnostic for pyomelanin versus other melanins or non-melanin pigments |
| Stress consequences | pyomelanin; hydrogen peroxide; nitric oxide; UV/UVC exposure; reactive oxygen intermediates | Pyomelanin can increase tolerance to oxidative or UV stress in several taxa, but effects are context dependent and may be absent for virulence endpoints (ahmad2016geneticdeterminantsfor pages 1-2, jiang2021pyomelaninproducingbrevundimonasvitisensis pages 1-2, schmalerripcke2009productionofpyomelanin pages 1-2, moustafa2024mutationofhmga pages 9-11) | Medium | Evidence is mixed: Burkholderia cenocepacia 2024 found no significant virulence effect in a CGD mouse lung model despite some in vitro protection signals |
| Application evidence | natural pyomelanin; antioxidant activity; sunscreen activity; antimicrobial activity; biocompatibility | Brown pyomelanin has current application potential as a biocompatible antioxidant, antimicrobial, photoprotective, and biomaterial pigment (elzawawy2024bioproductionandoptimization pages 1-2, urbaniak2023invitroand pages 1-2, qin2024melanininfungi pages 2-4) | Medium | Application evidence supports usefulness, not trait causation; many data come from purified pigment assays rather than native-cell phenotype studies |


*Table: This table condenses the strongest curation-ready modules for METPO:1003023 into candidate causal directions, confidence levels, and caveats. It is useful for deciding which pyomelanin-related nodes and edges are ready for TraitMech curation and which should remain taxon-specific or provisional.*

## 1. Trait scope and boundaries

### In scope

* Visible brown pigmentation of colonies or cells, including reddish-brown, dark-brown, and black-brown variants.
* Diffusible pigment that browns the culture supernatant or agar surrounding growth. In *P. aeruginosa*, pyomelanin is described as a “black–brown negatively charged extracellular polymer,” while HGA-derived pigment can manifest in colonies and the surrounding milieu. (urbaniak2023invitroand pages 1-2, hunter2010aputativeabc pages 1-2)
* Constitutive or conditional pigmentation, including phenotypes dependent on tyrosine supplementation, growth phase, oxygen, temperature, or stress.
* Pyomelanin as the best-supported causal route, provided chemical, genetic, or pathway evidence identifies it rather than color alone.

### Boundary cases and exclusions

1. **Other melanins:** Fungal DHN-melanin, DOPA/eumelanin, and pheomelanin can also appear brown or black. *Aspergillus fumigatus*, for example, has conidial DHN-melanin as well as tyrosine-derived pyomelanin; these must be represented as distinct mechanisms. (schmalerripcke2009productionofpyomelanin pages 1-2)
2. **Other pigments:** Pyocyanin, pyoverdine, carotenoids, phenazines, and chemically unrelated brown products should not be merged with pyomelanin merely because a culture appears brown.
3. **Pigment versus consequence:** UV tolerance, oxidative-stress tolerance, virulence, adhesion, and electron transfer are downstream or associated phenotypes, not definitions of `METPO:1003023`.
4. **Localization:** Pyomelanin is commonly extracellular, but pigment can also associate with cell surfaces or membranes. Consequently, “extracellular brown pigment” is a useful child-level observation, not an absolute requirement for the parent trait. (urbaniak2023invitroand pages 1-2, qin2024melanininfungi pages 2-4)
5. **Identification standard:** A brown colony alone supports `METPO:1003023`, but not the node “pyomelanin.” Pyomelanin assignment should require pathway genetics, HGA detection, or orthogonal physicochemical characterization.

## 2. Candidate causal-graph nodes

Identifiers below are conservative. Labels are retained without CURIEs where exact cross-species grounding was not verified.

### Trait and phenotype nodes

| Candidate node | Grounding | Curation note |
|---|---|---|
| brown pigmented | **`METPO:1003023`** | Target class; quote identifier verbatim in YAML. |
| brown pigment accumulation | Label only | Process/state connecting polymer accumulation to visible phenotype. |
| reddish-brown colony or surrounding medium | Label only | Assay-observed manifestation reported for *P. aeruginosa*. |
| dark-brown extracellular pigment | Label only | Reported for *Streptomyces djakartensis* NSS-3. (elzawawy2024bioproductionandoptimization pages 1-2) |
| pyomelanin | Label only | HGA-derived heterogeneous polymer; avoid assigning a small-molecule CHEBI identifier. |

### Chemicals and environmental factors

| Candidate node | Suggested grounding | Role |
|---|---|---|
| L-tyrosine | CHEBI:L-tyrosine candidate; verify release-specific CURIE before import | Nutrient/substrate and transcriptional inducer. |
| 4-hydroxyphenylpyruvate (4-HPP/4-HPPA) | CHEBI candidate; verify exact protonation state | Immediate HppD substrate. |
| homogentisic acid/homogentisate (HGA) | CHEBI candidate; verify acid versus anion | Pyomelanin precursor and exported metabolite. |
| benzoquinone acetic acid | Label only | Proposed auto-oxidation intermediate. |
| molecular oxygen/aerobic conditions | CHEBI/ENVO candidate | Enables extracellular HGA oxidation. |
| maleylacetoacetate | CHEBI candidate | Product of HmgA; diverts HGA from pigment formation. |
| ascorbic acid | CHEBI candidate | Experimental inhibitor of HGA oxidation/polymerization at 10 mM. (hunter2010aputativeabc pages 5-6) |
| hydrogen peroxide | CHEBI candidate | Oxidative-stress assay factor. |
| nitric oxide / sodium nitroprusside | CHEBI candidates | Reactive-nitrogen-stress assay factor/donor. |
| ultraviolet C radiation | ENVO/exposure label candidate | Functional assay factor, not an upstream requirement for pigmentation. |

### Genes, proteins, and activities

| Candidate node | Grounding | Curation note |
|---|---|---|
| aromatic amino-acid/tyrosine aminotransferase | EC class candidate | Converts tyrosine to 4-HPP; bacterial genes include `tyrB` and `aspC`, but orthology is taxon-dependent. |
| `phhA`, phenylalanine hydroxylase | Label plus taxon-specific gene ID | Provides tyrosine from phenylalanine in *Aeromonas media*; peripheral rather than essential to all graphs. |
| `hppD` / 4-hydroxyphenylpyruvate dioxygenase | **EC:1.13.11.27** | Converts 4-HPP to HGA; high-confidence core node. (pavan2020melaninbiosynthesisin pages 3-4, jiang2021pyomelaninproducingbrevundimonasvitisensis pages 1-2) |
| `hmgA` / homogentisate 1,2-dioxygenase | EC candidate; verify exact EC record | Consumes HGA to maleylacetoacetate; loss/inactivation promotes pigment. |
| HatABCDE | Label plus *P. aeruginosa* locus identifiers | Putative ABC-type HGA exporter; preserve as taxon-specific. |
| `rpoS`, `hrpG`, `oxyR` | Taxon-specific gene IDs | Regulators required for pyomelanin under tested *Ralstonia solanacearum* conditions. (ahmad2016geneticdeterminantsfor pages 1-2) |
| `hmgB`, `hmgC`, `hmgR` | Label plus taxon-specific gene IDs | Downstream homogentisate pathway/regulatory candidates; do not make them direct pigment causes without perturbation evidence. |

### Locations and processes

* Cytosol: tyrosine catabolism and HGA formation.
* Cytoplasmic membrane/ABC transporter complex: HGA export in *P. aeruginosa*.
* Extracellular milieu or culture supernatant: HGA oxidation and polymerization.
* Cell wall/cell surface: possible fungal pyomelanin association; the 2024 fungal review reports 10–14 kDa pyomelanin capable of covering cell-wall surfaces, but generalization across fungi requires caution. (qin2024melanininfungi pages 2-4)
* Tyrosine degradation, HGA biosynthesis, transmembrane export, auto-oxidation, oxidative polymerization, pigment accumulation, and light absorption.

## 3. Candidate evidence-backed causal edges

“High” denotes direct biochemical/genetic evidence; “moderate” denotes strong but taxon- or assay-restricted evidence.

| # | Subject–predicate–object | Reference | Supporting snippet | Confidence and curation note |
|---:|---|---|---|---|
| 1 | L-tyrosine — **is converted by tyrosine aminotransferase to** → 4-HPP | Urbaniak et al. 2023, DOI 10.3390/ijms24097846 | “L-tyrosine is converted to 4-hydroxyphenylopyruvic acid … by tyrosine aminotransferase.” | **High** for the reaction; gene identity varies by taxon. (urbaniak2023invitroand pages 1-2) |
| 2 | `tyrB`/`aspC` disruption — **reduces or blocks** → brown pyomelanin pigmentation | Wang et al. 2015, DOI 10.1371/journal.pone.0120923 | Disruption of `phhA`, `tyrB`, `aspC`, or `hppD` “impairs or blocks pigmentation.” | **High**, but specific to *A. media* WS. (wang2015identificationandmolecular pages 1-2) |
| 3 | HppD (EC 1.13.11.27) — **converts** → 4-HPP to HGA | Wang et al. 2015; Pavan et al. 2020 | `hppD` encodes HppD, with homologs shown to catalyze conversion of 4-HPP to HGA. | **High**, core graph edge. (wang2015identificationandmolecular pages 9-11, pavan2020melaninbiosynthesisin pages 3-4) |
| 4 | `hppD` deletion — **abolishes** → HGA and pyomelanin | Schmaler-Ripcke et al. 2009, DOI 10.1128/AEM.02077-08 | “Homogentisic acid and pyomelanin were not observed with an hppD deletion mutant.” | **High**, direct fungal knockout evidence. (schmalerripcke2009productionofpyomelanin pages 1-2) |
| 5 | Functional HmgA — **converts/diverts** → HGA to maleylacetoacetate | Moustafa et al. 2024, DOI 10.1128/spectrum.00410-24 | HmgA “converts homogentisic acid … to maleylacetoacetate.” | **High**, conserved competing branch. (moustafa2024mutationofhmga pages 1-2) |
| 6 | `hmgA` deletion/inactivation — **causes accumulation of** → HGA | Schmaler-Ripcke et al. 2009; Moustafa et al. 2024 | “Accumulation of homogentisic acid provoked an increased pigment formation”; G378R renders HmgA nonfunctional. | **High** across tested fungus and bacterium. (schmalerripcke2009productionofpyomelanin pages 1-2, moustafa2024mutationofhmga pages 2-4) |
| 7 | HmgA G378R substitution — **causes** → pyomelanin-producing phenotype | Moustafa et al. 2024 | A “single amino acid substitution at position 378 (glycine to arginine) … determines pigment phenotype.” | **High**, but allele- and strain-specific to *B. cenocepacia*. (moustafa2024mutationofhmga pages 1-2, moustafa2024mutationofhmga pages 4-7) |
| 8 | Intracellular HGA accumulation — **induces expression of** → `hatABCDE` | Hunter & Newman 2010, DOI 10.1128/JB.01021-10 | “Intracellular accumulation of HGA elicits upregulation of these transport genes.” | **Moderate/high**, *P. aeruginosa*–specific. (hunter2010aputativeabc pages 1-2) |
| 9 | HatABCDE — **promotes export of** → HGA | Hunter & Newman 2010 | Transporter mutants produced less extracellular HGA with concurrent intracellular HGA accumulation. | **Moderate/high**; functional evidence supports transport, but the complex was described as “putative.” (hunter2010aputativeabc pages 1-2) |
| 10 | `hatABCDE` deletion in an `hmgA` background — **reduces** → extracellular HGA | Hunter & Newman 2010 | Parent reached 2.15 ± 0.15 mM extracellular HGA after 20 h; complementation partially restored 1.30 ± 0.1 mM. | **High** for the tested strain/condition; do not universalize. (hunter2010aputativeabc pages 5-6) |
| 11 | Secreted HGA + oxygen — **auto-oxidizes to** → benzoquinone acetic acid | Urbaniak et al. 2023; Wang et al. 2015 | “Secreted HGA autoxidizes to benzoquinone acetic acid.” | **High** as the accepted pathway model. (urbaniak2023invitroand pages 1-2, wang2015identificationandmolecular pages 1-2) |
| 12 | Benzoquinone acetic acid/HGA oxidation products — **polymerize into** → pyomelanin | Urbaniak et al. 2023 | The oxidation product “undergoes polymerization to form pyomelanin chains.” | **High** at pathway level; exact polymer microstructure remains heterogeneous. (urbaniak2023invitroand pages 1-2) |
| 13 | Ascorbic acid — **inhibits** → HGA oxidation and polymerization | Hunter & Newman 2010 | “Adding 10 mM ascorbic acid … prevented oxidation of HGA and subsequent polymerization.” | **High**, experimental edge useful for assay modeling. (hunter2010aputativeabc pages 5-6) |
| 14 | Extracellular pyomelanin accumulation — **causes** → brown/reddish-brown phenotype | Hunter & Newman 2010; Urbaniak et al. 2023 | Pyomelanin “manifests as a reddish brown pigmentation”; it is also described as dark brown to black. | **High**, core phenotype edge. (hunter2010aputativeabc pages 1-2, urbaniak2023invitroand pages 1-2) |
| 15 | L-tyrosine supplementation — **promotes** → pyomelanin production | Jiang et al. 2021; Moustafa et al. 2024 | *Brevundimonas* produced brown pigment in L-tyrosine medium; *Burkholderia* pigmentation was tested with 0.02% tyrosine. | **Moderate/high**, medium- and taxon-specific. (jiang2021pyomelaninproducingbrevundimonasvitisensis pages 1-2, moustafa2024mutationofhmga pages 9-11) |
| 16 | L-tyrosine — **induces transcription of** → `hppD` and `hmgA` | Schmaler-Ripcke et al. 2009 | “The transcription of both studied genes was induced by L-tyrosine.” | **High** in *A. fumigatus*; do not assume universal regulation. (schmalerripcke2009productionofpyomelanin pages 1-2) |
| 17 | `rpoS`, `hrpG`, or `oxyR` disruption — **decreases HppD expression/HGA and prevents** → pyomelanin | Ahmad et al. 2016, DOI 10.1371/journal.pone.0160845 | Wild type produced pigment and extracellular HGA, whereas regulatory mutants did not; HppD expression was higher in wild type. | **Moderate/high**, *R. solanacearum*–specific regulatory module. (ahmad2016geneticdeterminantsfor pages 1-2) |
| 18 | Pyomelanin — **can increase** → oxidative-stress tolerance | Ahmad et al. 2016; Schmaler-Ripcke et al. 2009 | Pigmented *Ralstonia* had higher H₂O₂ tolerance; fungal `hppD` mutant germlings were more sensitive to reactive oxygen intermediates. | **Moderate** because effects are taxon/context dependent. (ahmad2016geneticdeterminantsfor pages 1-2, schmalerripcke2009productionofpyomelanin pages 1-2) |
| 19 | Pyomelanin/melanized cells — **can increase** → UVC tolerance | Jiang et al. 2021 | “Melanized GR-TSA-9T cells could protect the cells against UVC exposure.” | **Moderate**, experimentally supported in one strain. (jiang2021pyomelaninproducingbrevundimonasvitisensis pages 1-2) |
| 20 | Pyomelanin production — **does not necessarily increase** → virulence | Moustafa et al. 2024 | Isogenic pigment changes did not significantly alter lung colonization, survival, or infection outcome in CGD mice. | **High negative evidence**; essential qualifier against a universal virulence edge. (moustafa2024mutationofhmga pages 1-2, moustafa2024mutationofhmga pages 7-9) |

### Recommended minimal core graph

For the existing 10-node/10-edge graph, the most defensible expansion is:

`L-tyrosine → 4-HPP → HGA → exported HGA → oxidized HGA/benzoquinone-acetic-acid species → pyomelanin → METPO:1003023`, with HppD catalyzing HGA formation, HatABCDE promoting export only in the *P. aeruginosa* contextual subgraph, oxygen enabling oxidation, and HmgA negatively regulating pigment flux by consuming HGA.

## 4. Recent developments, applications, and quantitative evidence

### 2024 mechanistic reassessment

Moustafa et al. used allelic exchange in two epidemic *B. cenocepacia* strains to isolate the effect of HmgA residue 378. G378R was sufficient to switch the pigmentation state through HmgA loss of function and HGA accumulation. Yet pigment status did not significantly alter acute H₂O₂/NO survival or CGD-mouse lung infection outcome. Although parental J2315 caused 100% mortality by day 4 and parental K56-2 by day 9, isogenic pigment swaps did not reproduce that between-strain difference, demonstrating that background factors—not pyomelanin alone—drove virulence. Tests included 100 mM H₂O₂, nitric-oxide donor exposures over 0–120 minutes, and intratracheal infection at 10³ CFU. (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 7-9, moustafa2024mutationofhmga pages 4-7)

This is the most important recent curation correction: **do not encode “pyomelanin causes virulence” as an unconditional edge**.

### 2023–2024 biomaterial and production research

Natural *P. aeruginosa* pyomelanin was characterized in 2023 as a negatively charged extracellular HGA polymer. Water-soluble and insoluble bacterial forms showed higher biosafety than synthetic pyomelanin in the tested fibroblast, monocyte, and *Galleria mellonella* systems, supporting evaluation for antimicrobial, immunomodulatory, and regenerative applications rather than establishing clinical use. (urbaniak2023invitroand pages 1-2)

A 2024 *S. djakartensis* study obtained an extracellular dark-brown pigment and assigned it as nitrogen-free pyomelanin using UV–Vis, FTIR, Raman, SEM/EDX, and NMR. Medium optimization increased production 4.19-fold to 118.73 mg/10 mL. Purified pigment showed radical-scavenging IC₅₀ 18.03 µg/mL, in-vitro SPF 18.5, cancer-cell-line IC₅₀ values of 108.9, 43.83, and 81.99 µg/mL, and MICs of 6.25 and 25 µg/mL against two MDR isolates. These are promising purified-pigment assay data, not evidence of therapeutic efficacy in humans. (elzawawy2024bioproductionandoptimization pages 1-2)

The 2024 fungal synthesis review emphasizes that pyomelanin remains structurally heterogeneous, is relatively low molecular weight—reported as approximately 10–14 kDa—and contains quinone-rich redox-active units. It highlights water solubility, radical-scavenging activity, heat stability, and potential electron-transfer behavior, while also noting unresolved polymer and cell-wall interactions. (qin2024melanininfungi pages 2-4)

### Environmental and real-world contexts

* Clinical isolates: pyomelanin overproduction occurs among *P. aeruginosa* isolates from cystic-fibrosis and urinary-tract infections; mutation or deletion of `hmgA` is a recurrent route. (hunter2010aputativeabc pages 1-2)
* Plant-associated bacteria: grape endophyte *Brevundimonas vitisensis* produced 0.19 g/L pigment in tryptic soy broth containing 1.0 mg/mL tyrosine at 25°C after six days; spectroscopy and mass spectrometry supported pyomelanin identity. (jiang2021pyomelaninproducingbrevundimonasvitisensis pages 1-2)
* Plant pathogens: stationary-phase *R. solanacearum* produces a brown pigment in tyrosine minimal medium, with `rpoS`, `hrpG`, and `oxyR` contributing to pathway regulation and H₂O₂ tolerance. (ahmad2016geneticdeterminantsfor pages 1-2)
* Potential engineered uses include sunscreens, antioxidant/antimicrobial formulations, coatings, dyes, metal binding, extracellular electron transfer, and bioelectronic materials. These remain predominantly laboratory or preclinical applications. (urbaniak2023invitroand pages 1-2, qin2024melanininfungi pages 2-4, elzawawy2024bioproductionandoptimization pages 1-2)

## 5. Expert synthesis for TraitMech

The literature supports treating **HGA flux balance**, rather than the presence of any single “melanin gene,” as the central causal principle. HppD increases HGA supply; HmgA decreases it; export and extracellular oxygen chemistry convert excess HGA into visible polymer. This explains why either increased upstream synthesis or impaired downstream catabolism can produce the same brown phenotype. (pavan2020melaninbiosynthesisin pages 3-4)

The graph should separate three evidence layers:

1. **Core chemistry:** tyrosine → 4-HPP → HGA → oxidized/polymerized HGA → pyomelanin → brown phenotype.
2. **Taxon-specific control:** `tyrB`/`aspC`, HatABCDE, HmgA G378R, and `rpoS`/`hrpG`/`oxyR`.
3. **Contextual consequences:** UV or oxidant tolerance, adhesion, electron transfer, iron interactions, and virulence.

Only the first layer is currently suitable for broad cross-taxon assertions. The second should use taxon-scoped edges, and the third should retain assay qualifiers and negative evidence.

## 6. Claims not yet ready for unconditional curation

* **Brown color ⇒ pyomelanin:** unsafe without HGA/pathway or chemical evidence.
* **All microbial pyomelanin is extracellular:** too broad; cell-surface, cell-wall, and membrane-associated fractions occur.
* **HatABCDE is the universal HGA exporter:** evidence is compelling in *P. aeruginosa* but insufficient across taxa.
* **HmgA loss is required for pyomelanin:** false; normal or increased HGA synthesis plus export can also produce pigment.
* **`hmgB` or `hmgC` directly causes brown pigmentation:** pathway presence alone is insufficient; these generally process downstream metabolites and may instead reduce HGA availability.
* **Pyomelanin universally increases oxidative-stress tolerance or virulence:** contradicted by strain-dependent and negative 2024 *B. cenocepacia* results. (moustafa2024mutationofhmga pages 1-2, moustafa2024mutationofhmga pages 4-7)
* **Every melanin-related stress phenotype belongs in the morphology graph:** downstream benefits should be separate contextual branches.
* **Exact pyomelanin structure:** current reviews emphasize heterogeneity; avoid a single definitive repeat unit or molecular formula. (qin2024melanininfungi pages 2-4)
* **2024 Pseudomonas UV-structure findings as established consensus:** the retrieved April 2024 source was a preprint; use the subsequently published FEBS Letters version, DOI 10.1002/1873-3468.15000, before curation if full text can be verified. The preprint tested 254-nm UVC at 0.93 W m⁻² and 0.15 mg/mL purified pigment but should be labeled provisional here. (appella2024beyonduniformitypyomelanin’s pages 19-24)

## DOI-first bibliography

1. **Moustafa DA et al.** “Mutation of *hmgA* … is responsible for pyomelanin production but does not impact virulence…” *Microbiology Spectrum* 12(7), published July 2024. DOI: [10.1128/spectrum.00410-24](https://doi.org/10.1128/spectrum.00410-24). (moustafa2024mutationofhmga pages 1-2)
2. **Qin Y, Xia Y.** “Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering.” *Microbial Cell Factories* 23, published December 2024. DOI: [10.1186/s12934-024-02614-8](https://doi.org/10.1186/s12934-024-02614-8). (qin2024melanininfungi pages 2-4)
3. **El-Zawawy NA et al.** “Bioproduction and optimization of newly characterized melanin pigment from *Streptomyces djakartensis* NSS-3…” *Microbial Cell Factories* 23:23, published January 2024. DOI: [10.1186/s12934-023-02276-y](https://doi.org/10.1186/s12934-023-02276-y). (elzawawy2024bioproductionandoptimization pages 1-2)
4. **Urbaniak MM et al.** “In Vitro and In Vivo Biocompatibility of Natural and Synthetic *Pseudomonas aeruginosa* Pyomelanin…” *International Journal of Molecular Sciences* 24:7846, published 25 April 2023. DOI: [10.3390/ijms24097846](https://doi.org/10.3390/ijms24097846). (urbaniak2023invitroand pages 1-2)
5. **Lorquin F et al.** “New insights and advances on pyomelanin production: from microbial synthesis to applications.” *Journal of Industrial Microbiology and Biotechnology* 49(4), published July 2022. DOI: [10.1093/jimb/kuac013](https://doi.org/10.1093/jimb/kuac013). (lorquin2022newinsightsand pages 19-19)
6. **Jiang L et al.** “Pyomelanin-Producing *Brevundimonas vitisensis* sp. nov.” *Frontiers in Microbiology* 12:733612, published 14 October 2021. DOI: [10.3389/fmicb.2021.733612](https://doi.org/10.3389/fmicb.2021.733612). (jiang2021pyomelaninproducingbrevundimonasvitisensis pages 1-2)
7. **Pavan ME et al.** “Melanin biosynthesis in bacteria, regulation and production perspectives.” *Applied Microbiology and Biotechnology* 104:1357–1370, online December 2019/issue 2020. DOI: [10.1007/s00253-019-10245-y](https://doi.org/10.1007/s00253-019-10245-y). (pavan2020melaninbiosynthesisin pages 3-4)
8. **Ahmad S et al.** “Genetic Determinants for Pyomelanin Production and Its Protective Effect against Oxidative Stress in *Ralstonia solanacearum*.” *PLOS ONE* 11:e0160845, published 11 August 2016. DOI: [10.1371/journal.pone.0160845](https://doi.org/10.1371/journal.pone.0160845). (ahmad2016geneticdeterminantsfor pages 1-2)
9. **Wang H et al.** “Identification and Molecular Characterization of the Homogentisate Pathway … in *Aeromonas media* WS.” *PLOS ONE* 10:e0120923, published March 2015. DOI: [10.1371/journal.pone.0120923](https://doi.org/10.1371/journal.pone.0120923). (wang2015identificationandmolecular pages 9-11)
10. **Hunter RC, Newman DK.** “A Putative ABC Transporter, HatABCDE, Is among Molecular Determinants of Pyomelanin Production in *Pseudomonas aeruginosa*.” *Journal of Bacteriology* 192:5962–5971, published November 2010. DOI: [10.1128/JB.01021-10](https://doi.org/10.1128/JB.01021-10). (hunter2010aputativeabc pages 1-2)
11. **Schmaler-Ripcke J et al.** “Production of Pyomelanin … via the Tyrosine Degradation Pathway in *Aspergillus fumigatus*.” *Applied and Environmental Microbiology* 75:493–503, published January 2009. DOI: [10.1128/AEM.02077-08](https://doi.org/10.1128/AEM.02077-08). (schmalerripcke2009productionofpyomelanin pages 1-2)
12. **Foundational evidence supplied with the template:** *Applied and Environmental Microbiology* 67:3463–3468, published 2001. DOI: [10.1128/AEM.67.8.3463-3468.2001](https://doi.org/10.1128/AEM.67.8.3463-3468.2001). Use as support that accumulated HGA yields brown pigment, while retaining the newer knockout and transport studies above for individual causal edges.

References

1. (wang2015identificationandmolecular pages 1-2): He Wang, Yunqian Qiao, Baozhong Chai, Chenxi Qiu, and Xiangdong Chen. Identification and molecular characterization of the homogentisate pathway responsible for pyomelanin production, the major melanin constituents in aeromonas media ws. PLOS ONE, 10:e0120923, Mar 2015. URL: https://doi.org/10.1371/journal.pone.0120923, doi:10.1371/journal.pone.0120923. This article has 64 citations and is from a peer-reviewed journal.

2. (pavan2020melaninbiosynthesisin pages 3-4): María Elisa Pavan, Nancy I. López, and M. Julia Pettinari. Melanin biosynthesis in bacteria, regulation and production perspectives. Applied Microbiology and Biotechnology, 104:1357-1370, Dec 2020. URL: https://doi.org/10.1007/s00253-019-10245-y, doi:10.1007/s00253-019-10245-y. This article has 201 citations and is from a domain leading peer-reviewed journal.

3. (schmalerripcke2009productionofpyomelanin pages 1-2): Jeannette Schmaler-Ripcke, Venelina Sugareva, Peter Gebhardt, Robert Winkler, Olaf Kniemeyer, Thorsten Heinekamp, and Axel A. Brakhage. Production of pyomelanin, a second type of melanin, via the tyrosine degradation pathway in <i>aspergillus fumigatus</i>. Applied and Environmental Microbiology, 75:493-503, Jan 2009. URL: https://doi.org/10.1128/aem.02077-08, doi:10.1128/aem.02077-08. This article has 321 citations and is from a peer-reviewed journal.

4. (hunter2010aputativeabc pages 1-2): Ryan C. Hunter and Dianne K. Newman. A putative abc transporter, hatabcde, is among molecular determinants of pyomelanin production in<i>pseudomonas aeruginosa</i>. Nov 2010. URL: https://doi.org/10.1128/jb.01021-10, doi:10.1128/jb.01021-10. This article has 76 citations and is from a peer-reviewed journal.

5. (urbaniak2023invitroand pages 1-2): Mateusz M. Urbaniak, Małgorzata Gazińska, Karolina Rudnicka, Przemysław Płociński, Monika Nowak, and Magdalena Chmiela. In vitro and in vivo biocompatibility of natural and synthetic pseudomonas aeruginosa pyomelanin for potential biomedical applications. International Journal of Molecular Sciences, 24:7846, Apr 2023. URL: https://doi.org/10.3390/ijms24097846, doi:10.3390/ijms24097846. This article has 17 citations.

6. (wang2015identificationandmolecular pages 9-11): He Wang, Yunqian Qiao, Baozhong Chai, Chenxi Qiu, and Xiangdong Chen. Identification and molecular characterization of the homogentisate pathway responsible for pyomelanin production, the major melanin constituents in aeromonas media ws. PLOS ONE, 10:e0120923, Mar 2015. URL: https://doi.org/10.1371/journal.pone.0120923, doi:10.1371/journal.pone.0120923. This article has 64 citations and is from a peer-reviewed journal.

7. (ahmad2016geneticdeterminantsfor pages 1-2): Shabir Ahmad, Seung Yeup Lee, Hyun Gi Kong, Eun Jeong Jo, Hye Kyung Choi, Raees Khan, and Seon-Woo Lee. Genetic determinants for pyomelanin production and its protective effect against oxidative stress in ralstonia solanacearum. PLoS ONE, 11:e0160845, Aug 2016. URL: https://doi.org/10.1371/journal.pone.0160845, doi:10.1371/journal.pone.0160845. This article has 51 citations and is from a peer-reviewed journal.

8. (moustafa2024mutationofhmga pages 1-2): Dina A. Moustafa, Linda Wu, Melissa Ivey, Sarah C. Fankhauser, and Joanna B. Goldberg. Mutation of <i>hmga</i> , encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of <i>burkholderia cenocepacia</i> in a chronic granulomatous disease mouse lung infection. Jul 2024. URL: https://doi.org/10.1128/spectrum.00410-24, doi:10.1128/spectrum.00410-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

9. (moustafa2024mutationofhmga pages 4-7): Dina A. Moustafa, Linda Wu, Melissa Ivey, Sarah C. Fankhauser, and Joanna B. Goldberg. Mutation of <i>hmga</i> , encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of <i>burkholderia cenocepacia</i> in a chronic granulomatous disease mouse lung infection. Jul 2024. URL: https://doi.org/10.1128/spectrum.00410-24, doi:10.1128/spectrum.00410-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

10. (hunter2010aputativeabc pages 5-6): Ryan C. Hunter and Dianne K. Newman. A putative abc transporter, hatabcde, is among molecular determinants of pyomelanin production in<i>pseudomonas aeruginosa</i>. Nov 2010. URL: https://doi.org/10.1128/jb.01021-10, doi:10.1128/jb.01021-10. This article has 76 citations and is from a peer-reviewed journal.

11. (jiang2021pyomelaninproducingbrevundimonasvitisensis pages 1-2): Lingmin Jiang, Doeun Jeon, Jueun Kim, Chul Won Lee, Yuxin Peng, Jiyoon Seo, Ju Huck Lee, Jin Hyub Paik, Cha Young Kim, and Jiyoung Lee. Pyomelanin-producing brevundimonas vitisensis sp. nov., isolated from grape (vitis vinifera l.). Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.733612, doi:10.3389/fmicb.2021.733612. This article has 7 citations and is from a peer-reviewed journal.

12. (elzawawy2024bioproductionandoptimization pages 1-2): Nessma A. El-Zawawy, El-Refaie Kenawy, Sara Ahmed, and Shimaa El-Sapagh. Bioproduction and optimization of newly characterized melanin pigment from streptomyces djakartensis nss-3 with its anticancer, antimicrobial, and radioprotective properties. Microbial Cell Factories, Jan 2024. URL: https://doi.org/10.1186/s12934-023-02276-y, doi:10.1186/s12934-023-02276-y. This article has 63 citations and is from a peer-reviewed journal.

13. (moustafa2024mutationofhmga pages 9-11): Dina A. Moustafa, Linda Wu, Melissa Ivey, Sarah C. Fankhauser, and Joanna B. Goldberg. Mutation of <i>hmga</i> , encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of <i>burkholderia cenocepacia</i> in a chronic granulomatous disease mouse lung infection. Jul 2024. URL: https://doi.org/10.1128/spectrum.00410-24, doi:10.1128/spectrum.00410-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

14. (qin2024melanininfungi pages 2-4): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 59 citations and is from a peer-reviewed journal.

15. (moustafa2024mutationofhmga pages 2-4): Dina A. Moustafa, Linda Wu, Melissa Ivey, Sarah C. Fankhauser, and Joanna B. Goldberg. Mutation of <i>hmga</i> , encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of <i>burkholderia cenocepacia</i> in a chronic granulomatous disease mouse lung infection. Jul 2024. URL: https://doi.org/10.1128/spectrum.00410-24, doi:10.1128/spectrum.00410-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

16. (moustafa2024mutationofhmga pages 7-9): Dina A. Moustafa, Linda Wu, Melissa Ivey, Sarah C. Fankhauser, and Joanna B. Goldberg. Mutation of <i>hmga</i> , encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of <i>burkholderia cenocepacia</i> in a chronic granulomatous disease mouse lung infection. Jul 2024. URL: https://doi.org/10.1128/spectrum.00410-24, doi:10.1128/spectrum.00410-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

17. (appella2024beyonduniformitypyomelanin’s pages 19-24): Mateo N. Diaz Appella, Adriana Kolender, Oscar J. Oppezzo, Nancy I. López, and Paula M. Tribelli. Beyond uniformity: pyomelanin’s structural complexity impacts on uv shielding in<i>pseudomonas</i>species with different lifestyles. BioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.11.589128, doi:10.1101/2024.04.11.589128. This article has 0 citations.

18. (lorquin2022newinsightsand pages 19-19): Faustine Lorquin, Philippe Piccerelle, Caroline Orneto, Maxime Robin, and Jean Lorquin. New insights and advances on pyomelanin production: from microbial synthesis to applications. Journal of Industrial Microbiology and Biotechnology, Jul 2022. URL: https://doi.org/10.1093/jimb/kuac013, doi:10.1093/jimb/kuac013. This article has 61 citations and is from a peer-reviewed journal.