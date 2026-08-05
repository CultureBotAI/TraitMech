---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:44:47.380170'
end_time: '2026-08-04T08:55:30.332125'
duration_seconds: 642.95
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: green pigmented
  trait_identifier: METPO:1003025
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: green_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cultures appear
    green or blue-green due to pigments such as pyocyanin and pyoverdine.
  parent_traits: METPO:1003021
  synonyms: Pigment_green
  evidence_summary: 'DOI:10.1186/s12934-023-02122-1: green colorization of the culture
    plate (Supports green/blue-green pigmentation from pyocyanin and fluorescein or
    pyoverdine-like pigments in representative bacteria.)'
  causal_graph_summary: 'green_pigmented_pyocyanin_phenazine: 12 nodes, 11 edges'
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
- **Trait label:** green pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003025
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cultures appear green or blue-green due to pigments such as pyocyanin and pyoverdine.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_green
- **Existing evidence:** DOI:10.1186/s12934-023-02122-1: green colorization of the culture plate (Supports green/blue-green pigmentation from pyocyanin and fluorescein or pyoverdine-like pigments in representative bacteria.)
- **Existing causal graph summary:** green_pigmented_pyocyanin_phenazine: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **green pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/green_pigmented.yaml`.

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
- **Trait label:** green pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003025
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cultures appear green or blue-green due to pigments such as pyocyanin and pyoverdine.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_green
- **Existing evidence:** DOI:10.1186/s12934-023-02122-1: green colorization of the culture plate (Supports green/blue-green pigmentation from pyocyanin and fluorescein or pyoverdine-like pigments in representative bacteria.)
- **Existing causal graph summary:** green_pigmented_pyocyanin_phenazine: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **green pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/green_pigmented.yaml`.

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


# Curation report: microbial **green pigmented** trait

## 1. Trait scope

**Trait:** “green pigmented”  
**Identifier:** **METPO:1003025**  
**Category:** MORPHOLOGY; **term kind:** CLASS; **mapping:** REVIEWED  
**Parent:** METPO:1003021  
**Synonym:** Pigment_green

METPO:1003025 should represent an **assay-observed visible phenotype** in which a microbial colony, agar plate, or liquid culture appears green, blue-green, or greenish-blue because extracellular or cell-associated pigments alter the observed color. It is not itself a pathway, pigment identity, fluorescence measurement, or taxonomic diagnosis.

The best-supported mechanistic model has two separable pigment branches:

1. **Pyocyanin branch.** Oxidized pyocyanin is blue to blue-green at neutral or alkaline pH; its appearance is pH- and redox-dependent. In *Pseudomonas aeruginosa*, blue pyocyanin can itself look greenish-blue or combine optically with yellow fluorescent pyoverdine/“fluorescein” to generate the characteristic green culture-plate appearance. Pyocyanin is reported in approximately **90–95%** of *P. aeruginosa* strains, so its absence does not exclude that species. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 2-5, abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2, jabłonska2023thetwofaces pages 1-2)
2. **Pyoverdine branch.** Pyoverdines are fluorescent siderophores whose chromophore gives fluorescent pseudomonad cultures a characteristic yellow-green or green appearance, especially under iron restriction. This branch can produce a green-associated phenotype without pyocyanin and occurs in multiple fluorescent *Pseudomonas* species, not only *P. aeruginosa*. (schalk2020anoverviewof pages 12-13, ringel2018thebiosynthesisof pages 1-3)

### Boundary cases

- **Fluorescence versus visible pigmentation:** yellow-green fluorescence under UV illumination should be represented as an assay-dependent manifestation of pyoverdine, not automatically equated with green color under white light.
- **Color-state dependence:** pyocyanin is blue-greenish at neutral/alkaline pH, pink-red under acidic conditions, and colorless when reduced. Thus, pigment biosynthetic capacity does not guarantee a green observation in every assay. (jabłonska2023thetwofaces pages 1-2)
- **Other phenazines:** phenazine-1-carboxylic acid, phenazine-1-carboxamide, and related compounds may be yellow, orange, or red and should not independently imply METPO:1003025.
- **Non-pigment color changes:** pH indicators, medium chemistry, mineral precipitation, reflected fluorescence, and mixed-culture coloration are outside scope unless a microbial pigment is demonstrated.
- **Taxonomic inference:** green colonies are suggestive of fluorescent pseudomonads but are not species-specific or sufficient for identification.
- **Downstream activities:** virulence, redox cycling, iron acquisition, antimicrobial activity, and biofilm effects are functions of the pigments, not definitions of the morphology trait.

## 2. Recommended graph architecture

The existing 12-node pyocyanin graph is a useful core but is too narrow for the ontology definition. A robust TraitMech representation should use a **shared terminal phenotype node** with two optional modules:

- **Module A:** chorismate → phenazine-1-carboxylic acid → 5-methyl-PCA → pyocyanin → blue-green/greenish-blue appearance.
- **Module B:** iron restriction → pyoverdine precursor synthesis and maturation → secreted fluorescent pyoverdine → yellow-green/green appearance.

The modules should not be encoded as universally co-required. Their relative contribution depends on taxon, strain, medium, iron, oxygen, pH, redox state, growth mode, and illumination.

## 3. Candidate nodes grouped by type

### Trait and taxon nodes

- **green pigmented** — **METPO:1003025**
- *Pseudomonas aeruginosa* — **NCBITaxon:287**
- fluorescent pseudomonads — label-only group node; avoid treating it as one species
- *Pseudomonas* spp. — use species/strain CURIEs in evidence annotations whenever available

### Pigments, precursors, and nutrients

- pyocyanin — label-only pending identifier verification
- pyoverdine / pyoverdines — label-only because structurally diverse strain-specific congeners exist
- chorismate — label-only pending identifier verification
- phenazine-1-carboxylic acid (PCA) — label-only
- 5-methyl-phenazine-1-carboxylic acid or corresponding methylphenazine intermediate — label-only; nomenclature should be checked against the exact biochemical source
- ferribactin/acylated ferribactin — label-only
- Fe(II), Fe(III), ferripyoverdine — label-only unless identifiers are independently validated
- molecular oxygen — **CHEBI:15379**
- NADH — **CHEBI:57945**; NADPH should be a separate node if used
- reactive oxygen species — **CHEBI:26523**
- zinc oxide nanoparticles — label-only experimental material node

### Genes, proteins, operons, and regulatory systems

**Pyocyanin pathway**

- **phzA1–phzG1 / phz1** and **phzA2–phzG2 / phz2** phenazine operons
- PhzA–PhzG core phenazine biosynthetic enzymes
- **phzM / PhzM**, phenazine-specific methyltransferase
- **phzS / PhzS**, pyocyanin-forming hydroxylating enzyme
- **lasI/lasR**, **rhlI/rhlR**, and **pqsABCDEH/PqsR** quorum-sensing systems
- **NahK**, histidine kinase
- **RsmA**, post-transcriptional regulator
- PQS and HHQ signaling molecules — label-only pending chemical grounding

**Pyoverdine pathway**

- **PvdL, PvdI, PvdJ, PvdD**, nonribosomal peptide synthetases
- **PvdA** and **PvdF**, precursor-modifying enzymes
- **PvdE**, inner-membrane ABC exporter
- **PvdQ**, periplasmic deacylase
- **PvdP**, periplasmic oxidative-cyclization enzyme
- **PvdS**, iron-starvation-responsive extracytoplasmic-function sigma factor
- **Fur–Fe²⁺**, iron-responsive repressor complex
- **FpvA**, TonB-dependent ferripyoverdine outer-membrane receptor
- PvdRT–OpmQ or other secretion machinery — retain as a separate, taxon-specific candidate until primary evidence is attached

### Processes and pathways

- shikimate/chorismate biosynthesis
- phenazine biosynthetic process
- pyocyanin biosynthetic process
- quorum sensing — **GO:0009372**
- nonribosomal peptide biosynthesis — label-only unless a verified GO term is selected
- siderophore biosynthetic process — **GO:0019290**
- iron ion transport — **GO:0006826**
- transmembrane transport — **GO:0055085**
- oxidation–reduction process — **GO:0055114**
- pigmentation — **GO:0043473**

### Cellular locations

- cytoplasm — **GO:0005737**
- cytoplasmic/inner membrane — **GO:0005886** where appropriate
- periplasmic space — **GO:0042597**
- outer membrane — **GO:0019867**
- extracellular region — **GO:0005576**

### Environmental and assay factors

- iron-restricted environment; iron-replete environment
- oxygen availability / microaerobic culture
- neutral-to-alkaline versus acidic pH
- temperature
- aeration and shaking
- planktonic culture versus biofilm
- incubation time, medium composition, phosphate, carbon and nitrogen sources
- white-light visual inspection versus UV-induced fluorescence

## 4. Candidate causal edges

The following table summarizes the strongest graph skeleton. “Strong” indicates either direct 2024 genetic/experimental evidence or a pathway step consistently supported by authoritative synthesis; it does not imply taxonomic universality.

| branch | subject | predicate | object | evidence strength/qualifier | DOI |
|---|---|---|---|---|---|
| pyocyanin | PhzA-G phenazine biosynthesis enzymes | enable biosynthesis of | phenazine-1-carboxylic acid (PCA) from chorismate | Strong; review-consistent pathway summary in 2023-2024 sources, taxon-focused on *Pseudomonas aeruginosa* (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 2-5, marey2024transformingmicrobialpigment pages 1-2, jabłonska2023thetwofaces pages 1-2) | 10.1186/s12934-023-02122-1; 10.1186/s12934-024-02438-6; 10.1007/s11274-023-03548-w |
| pyocyanin | PhzM | converts | phenazine-1-carboxylic acid (PCA) to 5-methyl-PCA / methylphenazine intermediate | Strong; pathway step repeatedly stated in recent reviews, organism-specific to *P. aeruginosa* (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2, jabłonska2023thetwofaces pages 1-2) | 10.1186/s12934-023-02122-1; 10.1007/s11274-023-03548-w |
| pyocyanin | PhzS | converts | 5-methyl-PCA intermediate to pyocyanin | Strong; pathway step repeatedly stated in recent reviews and 2024 experimental context (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2, marey2024transformingmicrobialpigment pages 1-2) | 10.1186/s12934-023-02122-1; 10.1186/s12934-024-02438-6 |
| phenotype | pyocyanin | causes visible phenotype | blue-green / greenish-blue pigmentation | Strong; direct phenotype description (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 2-5, marey2024transformingmicrobialpigment pages 1-2, abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2) | 10.1186/s12934-023-02122-1; 10.1186/s12934-024-02438-6 |
| phenotype | pyocyanin + yellow fluorescent pigment (pyoverdine/fluorescein-like) | contributes to | green coloration of culture plate/culture | Moderate; review/summary evidence, visual-assay specific (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2, abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 2-5) | 10.1186/s12934-023-02122-1 |
| regulation | PQS quorum-sensing system | positively regulates | pyocyanin production | Strong; direct experimental support via ΔnahK mis-regulation and review support; mechanism partly indirect (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 5-9, jabłonska2023thetwofaces pages 1-2) | 10.1128/jb.00276-23; 10.1007/s11274-023-03548-w |
| regulation | phz2 operon | increases production of | pyocyanin | Strong; direct genetic evidence in 2024 *P. aeruginosa* study (mendoza2024thehistidinekinase pages 2-5) | 10.1128/jb.00276-23 |
| regulation | nahK deletion | increases | pyocyanin production | Strong; direct experiment, ~4-fold in planktonic culture and ~2-fold in biofilms; *P. aeruginosa*-specific (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 2-5) | 10.1128/jb.00276-23 |
| regulation | nahK deletion | upregulates | PQS system / pqs operon | Strong; direct experiment in *P. aeruginosa*; mediator to phz2 partly unresolved (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 12-14, mendoza2024thehistidinekinase pages 5-9) | 10.1128/jb.00276-23 |
| regulation | nahK deletion | upregulates | phzM and phzS expression | Strong; direct expression evidence in *P. aeruginosa* (mendoza2024thehistidinekinase pages 5-9, mendoza2024thehistidinekinase pages 2-5) | 10.1128/jb.00276-23 |
| environment | low ZnO nanoparticles (6.06 µg/mL) at 32°C | increases | pyocyanin production | Strong; direct 2024 optimization experiment, condition-specific (humme2024optimisedstress– pages 1-2) | 10.1186/s12934-024-02486-y |
| environment | high ZnO nanoparticles (275.75 µg/mL) with elevated temperature | abolishes / suppresses | pyocyanin production | Strong; direct 2024 optimization experiment, condition-specific (humme2024optimisedstress– pages 1-2) | 10.1186/s12934-024-02486-y |
| pyoverdine | PvdL/PvdI/PvdJ/PvdD NRPS system | synthesizes | ferribactin / pyoverdine precursor peptide | Strong; authoritative review synthesis, fluorescent pseudomonad-specific (schalk2020anoverviewof pages 12-13, ringel2018thebiosynthesisof pages 1-3) | 10.1111/1462-2920.14937; 10.15698/mic2018.10.649 |
| pyoverdine | PvdE ABC transporter | exports | ferribactin/acylated precursor to the periplasm | Strong; authoritative review synthesis (ringel2018thebiosynthesisof pages 1-3) | 10.15698/mic2018.10.649 |
| pyoverdine | PvdQ and PvdP | mature | ferribactin precursor into fluorescent pyoverdine in the periplasm | Strong; authoritative review synthesis (ringel2018thebiosynthesisof pages 1-3) | 10.15698/mic2018.10.649 |
| phenotype | pyoverdine | causes visible phenotype | yellow-green fluorescence / green color characteristic of fluorescent pseudomonad cultures | Strong; authoritative review statement, trait may be fluorescence-linked and taxon-specific (schalk2020anoverviewof pages 12-13, ringel2018thebiosynthesisof pages 1-3) | 10.1111/1462-2920.14937; 10.15698/mic2018.10.649 |
| regulation | iron-restricted conditions | derepress / increase | pyoverdine biosynthesis genes | Strong; authoritative review synthesis (schalk2020anoverviewof pages 12-13) | 10.1111/1462-2920.14937 |
| regulation | Fur-Fe2+ complex | represses | pyoverdine biosynthetic gene expression under iron-replete conditions | Strong; authoritative review synthesis (schalk2020anoverviewof pages 12-13) | 10.1111/1462-2920.14937 |
| pyoverdine | pyoverdine | chelates | Fe(III) with very high affinity | Strong; authoritative review synthesis (ringel2018thebiosynthesisof pages 1-3) | 10.15698/mic2018.10.649 |
| pyoverdine | ferripyoverdine | binds and is taken up by | FpvA outer membrane receptor | Strong; authoritative review synthesis (ringel2018thebiosynthesisof pages 1-3) | 10.15698/mic2018.10.649 |


*Table: This table compiles the strongest candidate causal edges for curating METPO:1003025, spanning pyocyanin and pyoverdine branches, key regulatory inputs, and environmental modifiers. It is designed as a compact evidence-oriented starting point for TraitMech graph construction.*

### Additional evidence snippets and curation notes

| Proposed triple | Supporting snippet | Reference and interpretation |
|---|---|---|
| pyocyanin **causes** greenish-blue pigmentation | “greenish-blue pigment pyocyanin”; blue pyocyanin combined with yellow fluorescein produces green plate coloration | Abdelaziz et al., June 2023. This directly supports the terminal phenotype edge but is a review statement and is specific to the visual assay context. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 2-5, abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2) |
| PhzA–PhzG **convert** chorismate toward PCA | “conversion of chorismate … to phenazine-1-carboxylic acid (PCA) via seven conserved PhzA–PhzG enzymes” | Jabłońska et al., February 2023. Suitable as a pathway-module edge; individual enzyme-level reactions should not be inferred from this aggregate statement. (jabłonska2023thetwofaces pages 1-2) |
| PhzM **converts** PCA to a methylphenazine intermediate | “PCA, then to 5-methyl-PCA … via PhzM” | Abdelaziz et al., June 2023. Strong pathway support, but exact protonation and intermediate naming should be normalized before chemical grounding. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2) |
| PhzS **converts** methylphenazine intermediate to pyocyanin | “finally to pyocyanin via PhzS-catalyzed hydroxylation” | Abdelaziz et al., June 2023. Suitable for *P. aeruginosa*; oxygen/cofactor details require a biochemical primary source before adding more granular edges. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2) |
| AHL/PQS quorum sensing **positively regulates** pyocyanin biosynthesis | “PqsR and RhlR directly controlling the phenazine synthesis operon” | Recent review synthesis. Encode regulator-to-operon edges rather than claiming direct binding to every biosynthetic gene. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 2-5) |
| nahK deletion **increases** pyocyanin | “4-fold increased PYO in planktonic culture and 2-fold increase in biofilms”; complementation restored production to wild-type levels | Mendoza et al., January 2024. This is strong direct genetic evidence in *P. aeruginosa*, but the biologically normal edge should be represented as NahK **negatively regulates** pyocyanin under the tested conditions. (mendoza2024thehistidinekinase pages 2-5) |
| nahK deletion **upregulates** phz2 | ΔnahK increased phz2 reporter expression; ΔnahKΔphz2 produced nearly undetectable phenazines, whereas deleting phz1 did not remove the phenotype | This supports phz2 as the operative phenazine locus in this experiment. It should not be generalized to all strains or conditions. (mendoza2024thehistidinekinase pages 2-5) |
| nahK deletion **activates** PQS signaling | “genes in the pqs operon … highly upregulated”; PQS derivatives HHQ and DHQ were more prevalent in ΔnahK supernatant | Direct qPCR and metabolomic evidence. The PQS→phz2 link was described as involving an unknown mediator, so a direct molecular edge is uncertain. (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 5-9) |
| low-dose ZnO nanoparticles at 32°C **increase** pyocyanin production | “6.06 µg/mL” ZnO nanoparticles and “32°C” enhanced production | Humme et al., July 2024. This is a process-optimization edge, not a constitutive biological mechanism. Preserve concentration, temperature, strain, and culture context in evidence metadata. (humme2024optimisedstress– pages 1-2) |
| high-dose ZnO nanoparticles plus elevated temperature **suppress** pyocyanin | “275.75 µg/mL” with higher temperature abolished pigment production while stimulating biomass | The response is non-monotonic: ZnO must not be represented simply as a universal positive regulator. (humme2024optimisedstress– pages 1-2) |
| iron restriction **derepresses** pyoverdine biosynthesis | Under iron-replete conditions, the “Fur-Fe2+ complex binds … Fur-box sequences … repressing their expression”; restriction allows derepression | Schalk et al., February 2020. Authoritative mechanistic synthesis, but primarily *P. aeruginosa*/fluorescent-pseudomonad specific. (schalk2020anoverviewof pages 12-13) |
| PvdL/PvdI/PvdJ/PvdD **synthesize** ferribactin precursor | “four NRPS enzymes … catalyzing pyoverdine synthesis associate with the inner membrane” | Supports an NRPS-module edge and cytoplasmic-face localization. Avoid assigning the same NRPS set to every pyoverdine-producing species. (schalk2020anoverviewof pages 12-13) |
| PvdE **exports** ferribactin into the periplasm | “PvdE exports acylated ferribactin into the periplasm” | Ringel and Brüser, October 2018. Review-derived but suitable as a conserved *P. aeruginosa* module. (ringel2018thebiosynthesisof pages 1-3) |
| PvdQ/PvdP **mature** ferribactin into fluorescent pyoverdine | “PvdQ deacylation and PvdP-catalyzed oxidative cyclization to generate the dihydroxyquinoline fluorophore” | Supports periplasmic maturation and fluorophore formation. It does not establish that fluorescence always appears visibly green under every illumination condition. (ringel2018thebiosynthesisof pages 1-3) |
| pyoverdine **chelates** Fe(III) | mature pyoverdine acts as an iron chelator with affinity reported at approximately 10³² | Appropriate as a functional edge; the affinity is congener- and condition-dependent and should be annotated rather than treated as a universal exact constant. (ringel2018thebiosynthesisof pages 1-3) |
| ferripyoverdine **is imported through** FpvA | “Ferric iron-bound pyoverdine binds to the FpvA receptor and is TonB-dependently transported” | Supports ligand–receptor binding followed by transport. These should ideally be represented as two edges. (ringel2018thebiosynthesisof pages 1-3) |

## 5. Recent developments and quantitative evidence

### Regulatory mechanism: NahK–PQS–phz2 axis

Mendoza et al. identified NahK as a previously unrecognized negative regulator of pyocyanin. Deleting **nahK** caused approximately a **fourfold** increase in planktonic pyocyanin and a **twofold** increase in biofilms; complementation restored wild-type production. Genetic analysis localized the increase principally to **phz2**, while expression and metabolomic measurements showed activation of the PQS system and increased **phzM/phzS** expression. The authors nevertheless concluded that PQS control of phz2 includes an unknown mediator and may be especially relevant under microaerobic conditions. This is high-value graph evidence, but it should remain explicitly strain- and condition-specific. (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 12-14, mendoza2024thehistidinekinase pages 5-9, mendoza2024thehistidinekinase pages 2-5)

### Bioprocess control with ZnO nanoparticles

A 2024 design-of-experiments study found that **6.06 µg/mL ZnO nanoparticles at 32°C** enhanced pyocyanin production and that this response persisted during scale-up. Conversely, **275.75 µg/mL** ZnO combined with higher temperature stimulated biomass but abolished pyocyanin. Increased production coincided with altered gene expression, membrane potential, reactive oxygen species, and cellular zinc accumulation. The main curation lesson is that nanoparticle stress has a **dose- and temperature-dependent, non-monotonic** effect rather than a simple activating relationship. (humme2024optimisedstress– pages 1-2)

### Clinical-isolate characterization and bioactivity

A 2024 study examined **30 clinical isolates**: every isolate carried at least one of **phzM** or **phzS**, while **13/30** carried both. Extracted pigment showed antibacterial MICs of **31.25–125 µg/mL** against tested Gram-positive bacteria and **250–1000 µg/mL** against *E. coli* isolates. Reported cancer-cell IC₅₀ values were **130 µg/mL** for A549, **105 µg/mL** for MDA-MB-231, and **187.9 µg/mL** for Caco-2. These are in-vitro extract results and do not establish therapeutic safety, clinical efficacy, or a causal edge to green pigmentation. (marey2024transformingmicrobialpigment pages 1-2)

## 6. Current applications and expert interpretation

- **Culture phenotype and presumptive detection:** blue-green or green colonies remain a useful visible clue for pigment-producing pseudomonads, but pigment-negative strains and pyoverdine-only producers prevent species-level diagnosis from color alone. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2, schalk2020anoverviewof pages 12-13)
- **Antivirulence discovery:** pyocyanin is a measurable output of QS/PQS activity, making color or extracted-pigment assays useful for screening quorum-sensing inhibitors. The NahK study also illustrates how pigment output can reveal regulatory-network perturbation. (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 2-5)
- **Industrial pigment production:** medium composition, aeration, pH, temperature, iron, incubation time, and controlled stress can steer yield. One review reported an optimal temperature of 37°C, pH 7.4–8.4, 72-hour incubation, and aeration-associated increases of 31–63.5%, but these are aggregated, strain- and protocol-dependent values rather than universal optima. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 2-5)
- **Redox and bioelectrochemical applications:** pyocyanin is a redox-active electron shuttle, motivating microbial-fuel-cell and electrochemical-sensing research. Its redox activity is also connected to oxidative stress and virulence, so application claims require toxicity controls. (jabłonska2023thetwofaces pages 1-2)
- **Antimicrobial and anticancer screening:** recent extracts show measurable in-vitro activity, but authoritative interpretation remains cautious because pyocyanin is itself a *P. aeruginosa* virulence factor and redox toxin. The 2024 authors explicitly called for in-vivo and combination studies. (marey2024transformingmicrobialpigment pages 1-2)
- **Iron competition and biocontrol:** pyoverdine’s high-affinity Fe(III) capture can restrict competitors and support colonization under low iron. This functional branch is biologically important but lies downstream of pigment production and should not be made necessary for the visible trait. (schalk2020anoverviewof pages 12-13, ringel2018thebiosynthesisof pages 1-3)

## 7. Warnings: claims not yet ready for TraitMech curation

1. **Do not make pyocyanin universally necessary.** Some green/yellow-green cultures are pyoverdine-driven, and 5–10% of *P. aeruginosa* strains may lack detectable pyocyanin under relevant conditions. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2)
2. **Do not require pyocyanin and pyoverdine together.** They are alternative or additive proximate causes.
3. **Do not curate “green pigment → *P. aeruginosa*.”** Color is neither a unique nor a sufficiently sensitive taxonomic marker.
4. **Do not encode fluorescence as equivalent to visible green color.** Add illumination and assay metadata.
5. **Do not add a direct PQS→phz2 molecular interaction without an uncertainty flag.** The 2024 study supports regulatory dependence but reports an unresolved mediator. (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 12-14)
6. **Do not generalize NahK effects beyond the tested *P. aeruginosa* background and conditions.** The effect may be microaerobic and network-dependent. (mendoza2024thehistidinekinase pages 12-14)
7. **Do not represent ZnO nanoparticles as a simple activator.** Low and high concentrations had opposite effects, with temperature as an interacting variable. (humme2024optimisedstress– pages 1-2)
8. **Do not add exact oxygen, iron, pH, temperature, or nutrient thresholds as universal graph edges.** Most values are medium-, strain-, and reactor-specific. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 2-5)
9. **Do not infer enzyme-level reactions for every PhzA–PhzG protein from the aggregate operon evidence.** Curate the pathway-module edge until primary biochemical evidence is attached.
10. **Do not treat every pyoverdine as one chemical entity.** Pyoverdines possess strain-variable peptide side chains; use a class node unless the congener is analytically identified. (ringel2018thebiosynthesisof pages 1-3)
11. **Do not curate therapeutic efficacy from the 2024 MIC/IC₅₀ study.** Results were in vitro and concerned extracted material; pyocyanin’s virulence and redox toxicity remain major translational barriers. (marey2024transformingmicrobialpigment pages 1-2)
12. **Verify all chemical and protein CURIEs before YAML insertion.** Label-only nodes are preferable to an incorrect stable identifier.

## 8. DOI-first bibliography

1. **Mendoza AG et al.** “The histidine kinase NahK regulates pyocyanin production through the PQS system.” *Journal of Bacteriology*. **January 2024**. DOI: [10.1128/jb.00276-23](https://doi.org/10.1128/jb.00276-23). (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 2-5)
2. **Honselmann genannt Humme J et al.** “Optimised stress – intensification of pyocyanin production with zinc oxide nanoparticles.” *Microbial Cell Factories*. **July 2024**. DOI: [10.1186/s12934-024-02486-y](https://doi.org/10.1186/s12934-024-02486-y). (humme2024optimisedstress– pages 1-2)
3. **Marey MA et al.** “Transforming microbial pigment into therapeutic revelation: extraction and characterization of pyocyanin from *Pseudomonas aeruginosa* and its therapeutic potential as an antibacterial and anticancer agent.” *Microbial Cell Factories*. **June 2024**. DOI: [10.1186/s12934-024-02438-6](https://doi.org/10.1186/s12934-024-02438-6). (marey2024transformingmicrobialpigment pages 1-2)
4. **Abdelaziz AA et al.** “*Pseudomonas aeruginosa*’s greenish-blue pigment pyocyanin: its production and biological activities.” *Microbial Cell Factories*. **June 2023**. DOI: [10.1186/s12934-023-02122-1](https://doi.org/10.1186/s12934-023-02122-1). (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 2-5, abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2)
5. **Jabłońska J et al.** “The two faces of pyocyanin—why and how to steer its production?” *World Journal of Microbiology and Biotechnology*. **February 2023**. DOI: [10.1007/s11274-023-03548-w](https://doi.org/10.1007/s11274-023-03548-w). (jabłonska2023thetwofaces pages 1-2)
6. **Schalk IJ, Rigouin C, Godet J.** “An overview of siderophore biosynthesis among fluorescent pseudomonads and new insights into their complex cellular organization.” *Environmental Microbiology*. **February 2020**. DOI: [10.1111/1462-2920.14937](https://doi.org/10.1111/1462-2920.14937). (schalk2020anoverviewof pages 12-13)
7. **Ringel MT, Brüser T.** “The biosynthesis of pyoverdines.” *Microbial Cell*. **October 2018**. DOI: [10.15698/mic2018.10.649](https://doi.org/10.15698/mic2018.10.649). (ringel2018thebiosynthesisof pages 1-3)

## Curation recommendation

For `data/traits/morphology/green_pigmented.yaml`, retain the existing pyocyanin graph as one taxon-specific mechanism and add a second pyoverdine module. Join both only at the terminal **METPO:1003025** phenotype through qualified `causes_or_contributes_to` edges. The highest-confidence immediate additions are **PhzA–G→PCA**, **PhzM→methylphenazine intermediate**, **PhzS→pyocyanin**, **pyocyanin→greenish-blue appearance**, **iron restriction/Fur→pyoverdine biosynthesis**, **PvdE→periplasmic precursor transport**, **PvdQ/PvdP→fluorophore maturation**, and **pyoverdine→yellow-green/green culture appearance**. NahK, PQS, ZnO, exact culture parameters, and therapeutic effects should be represented as condition-specific evidence annotations or optional regulatory branches rather than universal determinants.

References

1. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 2-5): Ahmed A. Abdelaziz, Amal M. Abo Kamer, Khaled B. Al-Monofy, and Lamiaa A. Al-Madboly. Pseudomonas aeruginosa’s greenish-blue pigment pyocyanin: its production and biological activities. Microbial Cell Factories, Jun 2023. URL: https://doi.org/10.1186/s12934-023-02122-1, doi:10.1186/s12934-023-02122-1. This article has 209 citations and is from a peer-reviewed journal.

2. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2): Ahmed A. Abdelaziz, Amal M. Abo Kamer, Khaled B. Al-Monofy, and Lamiaa A. Al-Madboly. Pseudomonas aeruginosa’s greenish-blue pigment pyocyanin: its production and biological activities. Microbial Cell Factories, Jun 2023. URL: https://doi.org/10.1186/s12934-023-02122-1, doi:10.1186/s12934-023-02122-1. This article has 209 citations and is from a peer-reviewed journal.

3. (jabłonska2023thetwofaces pages 1-2): Joanna Jabłońska, Adrian Augustyniak, Kamila Dubrowska, and Rafał Rakoczy. The two faces of pyocyanin - why and how to steer its production? World Journal of Microbiology & Biotechnology, Feb 2023. URL: https://doi.org/10.1007/s11274-023-03548-w, doi:10.1007/s11274-023-03548-w. This article has 48 citations and is from a peer-reviewed journal.

4. (schalk2020anoverviewof pages 12-13): Isabelle J. Schalk, Coraline Rigouin, and Julien Godet. An overview of siderophore biosynthesis among fluorescent pseudomonads and new insights into their complex cellular organization. Environmental Microbiology, 22:1447-1466, Feb 2020. URL: https://doi.org/10.1111/1462-2920.14937, doi:10.1111/1462-2920.14937. This article has 125 citations and is from a domain leading peer-reviewed journal.

5. (ringel2018thebiosynthesisof pages 1-3): Michael T. Ringel and Thomas Brüser. The biosynthesis of pyoverdines. Microbial Cell, 5:424-437, Oct 2018. URL: https://doi.org/10.15698/mic2018.10.649, doi:10.15698/mic2018.10.649. This article has 200 citations.

6. (marey2024transformingmicrobialpigment pages 1-2): Moustafa A. Marey, Rania Abozahra, Nefertiti A. El-Nikhely, Miranda F. Kamal, Sarah M. Abdelhamid, and Mohammed A. El-Kholy. Transforming microbial pigment into therapeutic revelation: extraction and characterization of pyocyanin from pseudomonas aeruginosa and its therapeutic potential as an antibacterial and anticancer agent. Microbial Cell Factories, Jun 2024. URL: https://doi.org/10.1186/s12934-024-02438-6, doi:10.1186/s12934-024-02438-6. This article has 32 citations and is from a peer-reviewed journal.

7. (mendoza2024thehistidinekinase pages 1-2): Alicia G. Mendoza, Danielle Guercio, Marina K. Smiley, Gaurav K. Sharma, Jason M. Withorn, Natalie V. Hudson-Smith, Chika Ndukwe, Lars E. P. Dietrich, and Elizabeth M. Boon. The histidine kinase nahk regulates pyocyanin production through the pqs system. Journal of Bacteriology, Jan 2024. URL: https://doi.org/10.1128/jb.00276-23, doi:10.1128/jb.00276-23. This article has 12 citations and is from a peer-reviewed journal.

8. (mendoza2024thehistidinekinase pages 5-9): Alicia G. Mendoza, Danielle Guercio, Marina K. Smiley, Gaurav K. Sharma, Jason M. Withorn, Natalie V. Hudson-Smith, Chika Ndukwe, Lars E. P. Dietrich, and Elizabeth M. Boon. The histidine kinase nahk regulates pyocyanin production through the pqs system. Journal of Bacteriology, Jan 2024. URL: https://doi.org/10.1128/jb.00276-23, doi:10.1128/jb.00276-23. This article has 12 citations and is from a peer-reviewed journal.

9. (mendoza2024thehistidinekinase pages 2-5): Alicia G. Mendoza, Danielle Guercio, Marina K. Smiley, Gaurav K. Sharma, Jason M. Withorn, Natalie V. Hudson-Smith, Chika Ndukwe, Lars E. P. Dietrich, and Elizabeth M. Boon. The histidine kinase nahk regulates pyocyanin production through the pqs system. Journal of Bacteriology, Jan 2024. URL: https://doi.org/10.1128/jb.00276-23, doi:10.1128/jb.00276-23. This article has 12 citations and is from a peer-reviewed journal.

10. (mendoza2024thehistidinekinase pages 12-14): Alicia G. Mendoza, Danielle Guercio, Marina K. Smiley, Gaurav K. Sharma, Jason M. Withorn, Natalie V. Hudson-Smith, Chika Ndukwe, Lars E. P. Dietrich, and Elizabeth M. Boon. The histidine kinase nahk regulates pyocyanin production through the pqs system. Journal of Bacteriology, Jan 2024. URL: https://doi.org/10.1128/jb.00276-23, doi:10.1128/jb.00276-23. This article has 12 citations and is from a peer-reviewed journal.

11. (humme2024optimisedstress– pages 1-2): Joanna Honselmann genannt Humme, Kamila Dubrowska, Bartłomiej Grygorcewicz, Marta Gliźniewicz, Oliwia Paszkiewicz, Anna Głowacka, Daniel Musik, Grzegorz Story, Rafał Rakoczy, and Adrian Augustyniak. Optimised stress – intensification of pyocyanin production with zinc oxide nanoparticles. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02486-y, doi:10.1186/s12934-024-02486-y. This article has 9 citations and is from a peer-reviewed journal.