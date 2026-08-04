---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:16:47.785728'
end_time: '2026-08-04T07:25:29.435223'
duration_seconds: 521.65
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: black pigmented
  trait_identifier: METPO:1003022
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: black_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    black or very dark due to accumulation of dark pigments such as melanins.
  parent_traits: METPO:1003021
  synonyms: Pigment_black
  evidence_summary: 'DOI:10.1016/j.biotechadv.2021.107773: dark-colored pigment (Supports
    black/dark microbial pigmentation as a melanin-associated color phenotype.)'
  causal_graph_summary: 'black_pigmented_melanin_polymer: 18 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** black pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003022
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear black or very dark due to accumulation of dark pigments such as melanins.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_black
- **Existing evidence:** DOI:10.1016/j.biotechadv.2021.107773: dark-colored pigment (Supports black/dark microbial pigmentation as a melanin-associated color phenotype.)
- **Existing causal graph summary:** black_pigmented_melanin_polymer: 18 nodes, 12 edges

## Research Objective

Research the microbial trait **black pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/black_pigmented.yaml`.

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
- **Trait label:** black pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003022
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear black or very dark due to accumulation of dark pigments such as melanins.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_black
- **Existing evidence:** DOI:10.1016/j.biotechadv.2021.107773: dark-colored pigment (Supports black/dark microbial pigmentation as a melanin-associated color phenotype.)
- **Existing causal graph summary:** black_pigmented_melanin_polymer: 18 nodes, 12 edges

## Research Objective

Research the microbial trait **black pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/black_pigmented.yaml`.

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


# Curation report: microbial **black pigmented**

## Trait record and scope

- **Trait:** black pigmented
- **Identifier:** **METPO:1003022**
- **Category / kind:** MORPHOLOGY / CLASS
- **Parent:** METPO:1003021
- **Synonym:** Pigment_black
- **Recommended operational meaning:** an observed colony-, cell-, spore-, biofilm-, or extracellular-material phenotype that is black or sufficiently dark brown/green-black to be scored as black under a stated assay or culture condition.

The phenotype is **not equivalent to “melanin production.”** Three melanin-associated modules commonly produce black-to-dark material: fungal DHN/allomelanin, DOPA-derived eumelanin, and homogentisate-derived pyomelanin. However, pigment identity, concentration, localization, medium, colony age, illumination, and scoring method all influence apparent color. Recent work on *Lomentospora prolificans*, for example, found medium- and age-dependent pigmentation and evidence for simultaneous DHN-, DOPA-, and pyomelanin-like material, so a black phenotype need not map to one exclusive pathway (liporagilopes2024newinsightsinto pages 15-18, liporagilopes2024newinsightsinto pages 12-15).

A critical boundary case is the “black-pigmented” oral anaerobes. *Porphyromonas gingivalis* produces green-black surface deposits of Fe(III) μ-oxo bisheme, and *Prevotella intermedia* produces brown-black monomeric Fe(III) protoporphyrin IX deposits. These are **heme pigments, not melanins** (olczak2024hemophorelikeproteinsof pages 5-7, olczak2024hemophorelikeproteinsof pages 2-5). Accordingly, the existing `black_pigmented_melanin_polymer` graph is appropriate as one mechanistic branch, but it should not be treated as an exhaustive definition of **METPO:1003022**.

### Recommended inclusion and exclusion rules

**Include** a strain-level assertion when a source directly reports black, green-black, black-brown, or very dark cells/colonies/material under specified conditions. Record the culture medium, age, precursor supplementation, oxygen/light conditions, and localization where available.

**Do not infer the trait solely from:**

1. Presence of a melanin-pathway gene without an observed dark phenotype.
2. UV resistance, virulence, antioxidant activity, or metal binding without color evidence.
3. A purified pigment described only as brown unless the organism itself is reported as black/very dark.
4. The name “black fungus,” “black mold,” or “black-pigmented anaerobe” without phenotype-level evidence.
5. Heme accumulation as evidence of melanin production.

## Candidate graph architecture

A robust TraitMech representation should use a **convergent graph** rather than a single linear pathway:

1. **DHN-melanin branch** → dark polymer → cell-wall/conidial deposition → black or very dark phenotype.
2. **DOPA/eumelanin branch** → DHI/DHICA-rich polymer → wall or extracellular deposition → dark phenotype.
3. **Pyomelanin branch** → extracellular HGA polymer → brown-black phenotype when abundance and assay conditions are sufficient.
4. **Heme-PPIX branch** → surface ferriheme/μ-oxo bisheme accumulation → brown-black or green-black phenotype; explicitly non-melanin.
5. Optional organism-specific branches for chemically distinct pigments, such as 5-deoxybostrycoidin-derived black perithecial pigment, only after primary evidence is curated (yin2026researchprogresson pages 20-20).

## Candidate nodes grouped by type

### Trait and phenotype nodes

- **black pigmented** — **METPO:1003022**
- black/dark colony pigmentation — label-only assay phenotype
- black/dark conidial pigmentation — label-only
- extracellular brown-black pigment — label-only; requires a color threshold/context qualifier
- green-black surface pigment — label-only; appropriate for *P. gingivalis*
- reduced/light pigmentation — label-only contrast phenotype

### Pathways and metabolic modules

- DHN-melanin biosynthesis
- DOPA-melanin/eumelanin biosynthesis
- tyrosine degradation/pyomelanin biosynthesis
- oxidative polymerization of phenolic or indolic precursors
- melanin granule trafficking and cell-wall anchoring
- heme acquisition and ferriheme surface accumulation
- cAMP/PKA regulation; HOG/MAPK regulation — organism-specific regulatory modules

### Genes, proteins, and enzymes

- Polyketide synthase: **PKS**, with taxon-specific genes including `pksP`, `PKS1`, `wdpks1`, and `bcpks13`
- T4HN/T3HN reductases: T4HNR, T3HNR; taxon-specific `THR1`
- Scytalone dehydratase: SCD; taxon-specific `SCD1`
- Laccase: **EC:1.10.3.2**; `LAC1`, `LAC2`, and taxon-specific `pbrB`
- Tyrosinase: **EC:1.14.18.1**
- 4-hydroxyphenylpyruvate dioxygenase: `hppD` — retain gene symbol plus taxon
- Homogentisate 1,2-dioxygenase: `hmgA` — taxon-specific role in HGA turnover
- Pyomelanin-cluster genes reported in *A. fumigatus*: `hppD`, `hmgX`, `hmgA`, `fahA`, `maiA`, `hmgR`
- Chitin synthase/anchoring factor `CHS3P` — verify exact nomenclature in the primary organism before curation
- Copper-handling proteins `Ccc2`, `Atx1`, `Ctr1`
- Transcriptional regulators `Bzp4`, `Usv101`, `Mbs1`, `Hob1`, `Amr1`, `VdCmr1`, `BcSMR1`, `StMR1`, and others — all taxon-specific
- Gingipains `RgpA`, `RgpB`, `Kgp`; hemophore-like **HmuY**; outer-membrane receptor **HmuR** — *P. gingivalis* heme branch

### Chemicals and metabolites

Use database lookup during YAML implementation rather than guessing CURIEs. High-priority candidates for ChEBI/Rhea grounding are:

- acetyl-CoA; malonyl-CoA
- 1,3,6,8-tetrahydroxynaphthalene (T4HN)
- scytalone; vermelone; 1,8-dihydroxynaphthalene (1,8-DHN)
- L-tyrosine; L-DOPA; dopaquinone
- 5,6-dihydroxyindole (DHI); 5,6-dihydroxyindole-2-carboxylic acid (DHICA)
- cysteine/cysteinyl-DOPA conjugates
- 4-hydroxyphenylpyruvate; homogentisic acid (HGA)
- benzoquinone acetate/benzoquinone acetic acid — normalize terminology against the primary source
- heme/iron protoporphyrin IX; methemoglobin; Fe(III) μ-oxo bisheme
- copper ion
- inhibitors: tricyclazole, pyroquilon, niacin, and nitisinone

### Cellular locations and processes

- fungal cell wall — suitable GO cellular-component grounding after ontology lookup
- conidial wall/surface
- extracellular space
- melanosome-like vesicles/secretory vesicles
- peroxisome — reported for early enzymes in some fungal systems, not universal
- outer membrane/cell surface — heme deposits and Hmu transport system
- chitin-dependent pigment anchoring
- vesicular transport of intermediates or granules

### Environmental and experimental factors

- precursor availability: tyrosine, L-DOPA, catecholamines, HGA
- heme/hemoglobin availability and blood agar
- copper concentration
- glucose availability; osmotic stress
- pH, illumination, humidity, aeration, medium composition, and culture age
- pathway inhibitors and gene-disruption experiments

The 2024 fungal review reports that copper supplementation at 0.01–0.2 g/L can enhance tyrosinase activity and that tyrosine, pH, darkness, humidity, and ventilation affect production, but these are optimization observations rather than universal trait determinants (qin2024melanininfungi pages 4-5).

## Candidate causal edges

The strongest curation candidates are summarized below. Predicates should be normalized to the relation vocabulary used elsewhere in TraitMech—for example, `substrate_of`, `catalyzes`, `produces`, `positively_regulates`, `inhibits`, `localizes_to`, and `causes_trait`.

| subject | predicate | object | taxon/context | evidence strength | DOI/source | short supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| acetyl-CoA + malonyl-CoA | are precursors for | 1,3,6,8-tetrahydroxynaphthalene (T4HN) | fungal DHN-melanin pathway | moderate; review-derived | 10.3390/plants14142121 | “PKS-catalyzed formation of 1,3,6,8-tetrahydroxynaphthalene (T4HN) from acetyl-CoA or malonyl-CoA” (jia2025fungalmelaninin pages 2-4) | Candidate pathway edge for DHN melanin; broadly fungal, not universal across all microbes. |
| polyketide synthase (PKS) | catalyzes formation of | T4HN | fungal DHN-melanin pathway | moderate; review-derived | 10.3390/plants14142121 | “DHN melanin biosynthesis involves polyketide synthase (PKS)-catalyzed formation of… T4HN” (jia2025fungalmelaninin pages 2-4) | Ground node to PKS label/EC if specific ortholog unclear. |
| T4HN | is reduced to | scytalone | fungal DHN-melanin pathway | moderate; review-derived | 10.3390/plants14142121 | “followed by sequential reduction and dehydration by hydroxynaphthol reductases… and scytalone dehydratase” (jia2025fungalmelaninin pages 2-4) | Intermediate step inferred from pathway summary; review-level support. |
| scytalone dehydratase (SCD) | converts | scytalone to downstream DHN intermediates including vermelone | fungal DHN-melanin pathway | moderate; review-derived | 10.3390/plants14142121 | “sequential reduction and dehydration by… scytalone dehydratase (SCD), producing intermediates scytalone, vermelone, and DHN” (jia2025fungalmelaninin pages 2-4) | Captures dehydration step; exact stoichiometric substep may need primary-source curation. |
| vermelone | is converted to | 1,8-dihydroxynaphthalene (DHN) | fungal DHN-melanin pathway | moderate; review-derived | 10.3390/plants14142121 | “producing intermediates scytalone, vermelone, and DHN” (jia2025fungalmelaninin pages 2-4) | Intermediate edge supported at pathway level, not enzyme-resolved in gathered excerpt. |
| laccase / tyrosinase | oxidatively polymerizes | DHN to melanin polymer | fungal DHN-melanin pathway | moderate; review-derived | 10.3390/plants14142121 | “ultimately polymerized by LAC”; “LAC and tyrosinase mediate the oxidative polymerization step” (jia2025fungalmelaninin pages 2-4, jia2025fungalmelaninin pages 10-12) | Good candidate edge for polymerization; enzyme identity can vary by taxon. |
| tricyclazole | inhibits | 3HNR in DHN-melanin pathway | rice-blast/fungal inhibitor context | moderate; review-derived, taxon-linked | 10.3390/plants14142121 | “tricyclazole (specific 3HNR inhibitor)” (jia2025fungalmelaninin pages 10-12) | Curate as inhibitor edge, not trait-defining by itself. |
| L-tyrosine / L-DOPA | are precursors for | eumelanin (DOPA-melanin) | fungal DOPA pathway | moderate; review-derived | 10.1186/s12934-024-02614-8 | “eumelanin (derived from L-dopa/L-tyrosine oxidation, producing indole-based structures via DHI or DHICA intermediates” (qin2024melanininfungi pages 1-2) | Broad fungal/eukaryotic melanin route; may apply to some bacteria too, but evidence here is fungal-focused. |
| tyrosinase | oxidizes | tyrosine toward dopaquinone in melanin biosynthesis | fungal DOPA pathway | moderate; review-derived | 10.1186/s12934-024-02614-8 | “Tyrosinase catalyzes tyrosine oxidation” (qin2024melanininfungi pages 8-10) | Exact product named as DAQ in excerpt; map cautiously to dopaquinone-like node. |
| DHI / DHICA intermediates | polymerize to form | eumelanin | fungal DOPA pathway | moderate; review-derived | 10.1186/s12934-024-02614-8 | “indole-based structures via DHI or DHICA intermediates” (qin2024melanininfungi pages 1-2) | Polymerization chemistry is heterogeneous; useful as pathway abstraction. |
| copper ions (e.g., CuSO4) | increase activity of | tyrosinase | fungal melanin production conditions | moderate; review-derived | 10.1186/s12934-024-02614-8 | “copper ions (CuSO4 at 0.01-0.2 g/L) improves tyrosinase activity” (qin2024melanininfungi pages 4-5) | Environmental/experimental factor; assay- and concentration-specific. |
| L-tyrosine | increases | melanin production | Auricularia auricula; Yarrowia lipolytica W29 | weak-moderate; review-derived, taxon-specific | 10.1186/s12934-024-02614-8 | “L-tyrosine… increases production in A. auricula and Y. lipolytica W29” (qin2024melanininfungi pages 4-5) | Keep taxon-specific; not universal. |
| tyrosine catabolism | produces | homogentisic acid (HGA) | fungal pyomelanin pathway | moderate; review-derived | 10.1186/s12934-024-02614-8 | “pyomelanin is synthesized from tyrosine through the tyrosine degradation pathway, which produces homogentisic acid (HGA)” (qin2024melanininfungi pages 15-15) | Strong route-defining edge for pyomelanin branch. |
| homogentisic acid (HGA) | oxidatively polymerizes to form | pyomelanin | microbial pyomelanin | moderate; review + primary-supporting recent paper | 10.3390/ijms24097846 | “pyomelanin is a black–brown negatively charged extracellular polymer of homogentisic acid” (urbaniak2023invitroand pages 1-2) | Good phenotype-proximal edge; pyomelanin often brown-black rather than jet black. |
| hppD disruption | causes | light phenotype / reduced pyomelanin | Aspergillus fumigatus | moderate; review-derived, taxon-specific | 10.1186/s12934-024-02614-8 | “For A. fumigatus pyomelanin… hppD disruption causes light phenotype” (qin2024melanininfungi pages 7-8) | Strong gene→phenotype edge but taxon-specific. |
| chitin-dependent cell wall anchoring | enables deposition of | melanin granules on cell wall | fungal melanization | moderate; review-derived | 10.1186/s12934-024-02614-8 | “melanin granules deposit on cell wall via chitin-dependent mechanism; CHS3P gene disruption inhibits anchoring” (qin2024melanininfungi pages 7-8) | Good localization/process edge; gene symbol from review excerpt may need validation before grounding. |
| dark environment / neutral to slightly acidic pH / ~70% humidity | favor | fungal melanogenesis | fungal culture conditions | weak-moderate; review-derived, assay-specific | 10.1186/s12934-024-02614-8 | “Environmental factors: neutral/slightly acidic pH, ~70% humidity, dark environment” (qin2024melanininfungi pages 4-5) | Experimental-factor node set; not a conserved mechanistic pathway edge. |
| gingipains (RgpA, Kgp) + HmuY/HmuR heme uptake system | cause accumulation of | surface Fe(III)PPIX / μ-oxo bisheme black pigment | Porphyromonas gingivalis; blood/heme-rich context | strong for taxon-specific non-melanin route; review-derived from specialized literature | 10.1128/mmbr.00131-23 | “P. gingivalis accumulates Fe(III) μ-oxo bisheme (green-black pigment)… mechanism involves: (1) gingipains… release heme… (3) HmuY… binding… heme… and (4) HmuY transferring heme to… HmuR” (olczak2024hemophorelikeproteinsof pages 5-7) | Important boundary-case edge: black pigmentation here is heme-derived, not melanin; curate separately or exclude from melanin subgraph. |


*Table: This table compiles the strongest candidate causal edges for curating METPO:1003022, covering melanin-associated DHN, DOPA, and pyomelanin routes, deposition and environmental factors, plus a separate non-melanin Porphyromonas heme-pigment boundary case.*

### Additional edge recommendations

The following phenotype-proximal terminal edges should be added only where the cited organism and assay report visible color:

- **DHN-melanin accumulation —causes→ black/very dark conidial or colony pigmentation.** Strong conceptually, but attach organism-specific evidence rather than asserting universality.
- **DOPA/eumelanin accumulation —causes→ black-brown pigmentation.** DOPA-derived eumelanin is characteristically dark, but apparent color depends on abundance and co-pigments (qin2024melanininfungi pages 1-2).
- **extracellular HGA polymer accumulation —can_cause→ brown-black pigmentation.** Pyomelanin is a black-brown extracellular HGA polymer in *Pseudomonas aeruginosa*; use `can_cause` or an uncertainty qualifier because many pyomelanins are reported as brown rather than black (urbaniak2023invitroand pages 1-2).
- **hppD disruption —causes→ light pigmentation** in *A. fumigatus*. This is a useful reverse/contrast edge supporting the pyomelanin branch, but it should remain taxon-specific (qin2024melanininfungi pages 7-8).
- **gingipain-mediated heme liberation + HmuY/HmuR acquisition —promotes→ surface ferriheme accumulation —causes→ green-black pigmentation** in *P. gingivalis*. This should be a distinct non-melanin subgraph (olczak2024hemophorelikeproteinsof pages 5-7).

## Mechanistic interpretation

### DHN melanin

The canonical fungal route begins with acetyl-CoA/malonyl-CoA and a polyketide synthase, proceeds through T4HN, scytalone, vermelone, and 1,8-DHN, and terminates in oxidative polymerization. Reductases and scytalone dehydratase mediate the alternating reduction/dehydration steps; laccase or related oxidases can participate in polymer formation. Knockout evidence across fungal taxa supports essential roles for PKS, reductases, dehydratase, and laccase, although gene names and exact reaction order vary (jia2025fungalmelaninin pages 2-4).

The pigment is commonly deposited in conidial or cell walls. Some systems compartmentalize early enzymes in intracellular organelles or melanosome-like vesicles and complete later reactions at the wall; chitin contributes to anchoring. These localization claims should not be generalized across fungi without species-specific evidence (jia2025fungalmelaninin pages 2-4, qin2024melanininfungi pages 7-8).

DHN-melanin inhibitors provide perturbational support. Tricyclazole targets a hydroxynaphthalene reductase step and is used against rice-blast fungi; related inhibitors disrupt appressorial melanization and consequently turgor-dependent plant penetration (jia2025fungalmelaninin pages 10-12). This evidence supports the pathway and biological role, but fungicide efficacy is not itself evidence that every treated colony becomes non-black.

### DOPA/eumelanin

DOPA melanogenesis oxidizes tyrosine or L-DOPA through dopaquinone and indolic intermediates, especially DHI and DHICA, followed by heterogeneous polymerization. Tyrosinase and laccase are principal copper-dependent oxidases. In *Cryptococcus neoformans*, LAC1 is predominantly associated with the wall and has the major melanization role, whereas LAC2 is more cytoplasmic; copper uptake and delivery through Ctr1, Atx1, and Ccc2 influence enzyme function (qin2024melanininfungi pages 8-10).

Unlike many autonomous fungal DHN pathways, exogenous catecholamines or L-DOPA may be required by particular organisms. Thus, “genetically capable of DOPA melanization” and “black under the reported medium” should be represented separately.

### Pyomelanin

Pyomelanin is generated when tyrosine degradation supplies HGA, which is exported or accumulates and oxidatively polymerizes into a negatively charged extracellular brown-black polymer. In *A. fumigatus*, the reviewed cluster includes `hppD`, `hmgX`, `hmgA`, `fahA`, `maiA`, and `hmgR`; disruption of `hppD` causes a lighter phenotype (qin2024melanininfungi pages 7-8). In many bacteria, reduced HGA catabolism—frequently involving deficient `hmgA` activity—can increase extracellular HGA and pyomelanin, but this particular `hmgA loss → black phenotype` edge should be added only after a directly supporting primary paper is attached.

Pyomelanin should be modeled as **potentially sufficient but not definitionally equivalent** to METPO:1003022 because reported colors span light brown to black-brown (liporagilopes2024newinsightsinto pages 1-5, urbaniak2023invitroand pages 1-2).

### Heme-derived black pigmentation

In *P. gingivalis*, RgpA and Kgp degrade hemoglobin and facilitate heme release; RgpA promotes conversion of oxyhemoglobin to methemoglobin, from which HmuY can sequester heme. HmuY transfers heme to HmuR, while Fe(III) μ-oxo bisheme accumulates at the cell surface and produces a green-black appearance. *P. intermedia* instead accumulates monomeric Fe(III)PPIX and appears brown-black (olczak2024hemophorelikeproteinsof pages 5-7, olczak2024hemophorelikeproteinsof pages 20-22, olczak2024hemophorelikeproteinsof pages 2-5). This mechanism is strong evidence that the broad morphology trait requires more than a melanin-only graph.

## Recent developments, applications, and quantitative data

### 2023–2024 research

- The December 2024 review by Qin and Xia synthesizes advances in fungal melanin structures, pathway regulation, compartmentalization, and metabolic engineering. It reports production examples of 2.97 g/L in *Auricularia auricula*, 5.60 g/L eumelanin in *Hortaea werneckii*, and a reported maximum of 27.98 g/L eumelanin in *Armillaria cepistipes*. These are production metrics, not prevalence statistics for the black trait (qin2024melanininfungi pages 4-5, qin2024melanininfungi pages 2-4).
- A November 2024 *L. prolificans* preprint used inhibitors, TEM, EPR, FTIR, and solid-state NMR to argue for a mixture of DHN-, DOPA-, and pyomelanin-like material. A three-inhibitor combination suppressed UV absorbance more strongly than individual treatments, suggesting pathway compensation. Because this is a preprint and chemical assignment is partly indirect, it is hypothesis-generating rather than a high-confidence universal graph (liporagilopes2024newinsightsinto pages 15-18, liporagilopes2024newinsightsinto pages 12-15).
- A March 2024 authoritative review established the ferriheme basis of black pigmentation and the HmuY-centered heme-acquisition system in oral/gut Bacteroidota, strengthening the non-melanin boundary case (olczak2024hemophorelikeproteinsof pages 5-7, olczak2024hemophorelikeproteinsof pages 2-5).

### Real-world and emerging applications

Microbial melanins are being investigated for UV protection, antioxidant and antimicrobial formulations, agricultural biocontrol, stabilization of insecticidal proteins, metal/dye remediation, cosmetics, packaging, and biomaterials. The 2024 agricultural review regards these largely as promising or developing applications, not uniformly mature commercial deployments (munoztorres2024exploringtheagricultural pages 12-13).

A 2024 *Streptomyces djakartensis* NSS-3 study optimized extracellular pyomelanin production by 4.19-fold to **118.73 mg/10 mL**. Purified material showed antioxidant **IC50 = 18.03 µg/mL**, in-vitro **SPF = 18.5**, MICs of **6.25 and 25 µg/mL** against two multidrug-resistant bacterial isolates, and cancer-cell IC50 values of **108.9, 43.83, and 81.99 µg/mL** for HCT116, HEPG, and MCF7 cells, respectively. These are laboratory measurements and should not be interpreted as clinical efficacy (elzawawy2024bioproductionandoptimization pages 1-2).

A 2023 study compared water-soluble, water-insoluble, and synthetic *P. aeruginosa* pyomelanins. Natural variants showed better biological safety than the synthetic polymer in in-vitro and *Galleria mellonella* assays, supporting further evaluation for biomedical formulations rather than demonstrating an approved implementation (urbaniak2023invitroand pages 1-2).

## Ontology-grounding recommendations

1. Preserve the supplied trait CURIE verbatim: **METPO:1003022**.
2. Use **EC:1.10.3.2** for laccase and **EC:1.14.18.1** for tyrosinase where the source supports enzyme class rather than a specific protein (qin2024melanininfungi pages 8-10).
3. Ground genes/proteins with organism-specific UniProt accessions only after strain/species verification. Symbols such as `pksP`, `hppD`, `hmgA`, `LAC1`, `HmuY`, and `HmuR` are not globally unique identifiers.
4. Resolve metabolites through ChEBI and reactions through Rhea before committing IDs. Do not treat “melanin” as one chemically uniform molecule; DHN melanin, eumelanin, pheomelanin, and pyomelanin are heterogeneous polymer classes.
5. Ground taxa at the species/strain level using NCBITaxon where the evidence is taxon-specific. Important candidates include *Aspergillus fumigatus*, *Cryptococcus neoformans*, *Lomentospora prolificans*, *Pseudomonas aeruginosa*, *Streptomyces djakartensis*, *Porphyromonas gingivalis*, and *Prevotella intermedia*.
6. Represent culture factors with ENVO or assay-condition terms only when an appropriate stable term exists; otherwise retain a label and literal value.

## Claims that should not yet be curated

- **“All black microbial pigmentation is melanin.”** Directly contradicted by ferriheme-based black pigmentation in *Porphyromonas/Prevotella* (olczak2024hemophorelikeproteinsof pages 5-7, olczak2024hemophorelikeproteinsof pages 2-5).
- **“All melanized microbes are black.”** Melanins range from light brown and reddish-brown to black; abundance and context matter (liporagilopes2024newinsightsinto pages 1-5, qin2024melanininfungi pages 1-2).
- **A universal `hmgA loss → black pigmentation` edge.** Plausible and known in particular organisms, but the gathered evidence here does not provide a sufficiently direct primary snippet for universal curation.
- **Universal organelle localization.** Peroxisomal or melanosome-like compartmentalization is species- and pathway-specific (jia2025fungalmelaninin pages 2-4, qin2024melanininfungi pages 7-8).
- **The mixed-melanin model of *L. prolificans* as settled fact.** It derives from a 2024 preprint using inhibitor and spectroscopic inference; retain as uncertain (liporagilopes2024newinsightsinto pages 15-18, liporagilopes2024newinsightsinto pages 12-15).
- **Culture optimization factors as conserved biological causes.** Copper, pH, humidity, darkness, and precursor supplementation are assay- and taxon-dependent (qin2024melanininfungi pages 4-5).
- **Biomedical or agricultural efficacy from in-vitro assays.** SPF, MIC, antioxidant, cytotoxicity, and insecticidal-protein stabilization data support applications research, not clinical or field effectiveness (munoztorres2024exploringtheagricultural pages 12-13, elzawawy2024bioproductionandoptimization pages 1-2, urbaniak2023invitroand pages 1-2).
- **Exact stable metabolite or protein CURIEs without database validation.** Label-only nodes are preferable to invented or mismatched identifiers.

## DOI-first bibliography

1. Qin Y, Xia Y. **Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering.** *Microbial Cell Factories*. Published December 2024. DOI: [10.1186/s12934-024-02614-8](https://doi.org/10.1186/s12934-024-02614-8). (qin2024melanininfungi pages 7-8, qin2024melanininfungi pages 4-5, qin2024melanininfungi pages 8-10)
2. Olczak T, Śmiga M, Antonyuk SV, Smalley JW. **Hemophore-like proteins of the HmuY family in the oral and gut microbiome: unraveling the mystery of their evolution.** *Microbiology and Molecular Biology Reviews*. Published March 2024. DOI: [10.1128/mmbr.00131-23](https://doi.org/10.1128/mmbr.00131-23). (olczak2024hemophorelikeproteinsof pages 5-7, olczak2024hemophorelikeproteinsof pages 2-5)
3. Muñoz-Torres P, Cárdenas-Ninasivincha S, Aguilar Y. **Exploring the Agricultural Applications of Microbial Melanin.** *Microorganisms*. Published July 2024. DOI: [10.3390/microorganisms12071352](https://doi.org/10.3390/microorganisms12071352). (munoztorres2024exploringtheagricultural pages 12-13)
4. El-Zawawy NA, Kenawy E-R, Ahmed S, El-Sapagh S. **Bioproduction and optimization of newly characterized melanin pigment from *Streptomyces djakartensis* NSS-3.** *Microbial Cell Factories*. Published January 2024. DOI: [10.1186/s12934-023-02276-y](https://doi.org/10.1186/s12934-023-02276-y). (elzawawy2024bioproductionandoptimization pages 1-2)
5. Urbaniak MM et al. **In Vitro and In Vivo Biocompatibility of Natural and Synthetic *Pseudomonas aeruginosa* Pyomelanin for Potential Biomedical Applications.** *International Journal of Molecular Sciences*. Published April 2023. DOI: [10.3390/ijms24097846](https://doi.org/10.3390/ijms24097846). (urbaniak2023invitroand pages 1-2)
6. Paillat M, Silva IL, Cascales E, Doan T. **A journey with type IX secretion system effectors: selection, transport, processing and activities.** *Microbiology*. Published April 2023. DOI: [10.1099/mic.0.001320](https://doi.org/10.1099/mic.0.001320).
7. Liporagi-Lopes LC et al. **New Insights Into the Melanin Structure of *Lomentospora prolificans*.** bioRxiv preprint. Posted November 2024. DOI: [10.1101/2024.11.01.621558](https://doi.org/10.1101/2024.11.01.621558). (liporagilopes2024newinsightsinto pages 15-18, liporagilopes2024newinsightsinto pages 12-15)
8. Jia H et al. **Fungal Melanin in Plant Pathogens: Complex Biosynthesis Pathways and Diverse Biological Functions.** *Plants*. Published July 2025; used as a recent synthesis where 2024 evidence was incomplete. DOI: [10.3390/plants14142121](https://doi.org/10.3390/plants14142121). (jia2025fungalmelaninin pages 2-4, jia2025fungalmelaninin pages 10-12)

## Curation priority

For the next revision of `data/traits/morphology/black_pigmented.yaml`, the highest-value additions are: **(i)** explicit DHN-, DOPA-, and pyomelanin branch nodes; **(ii)** organism-qualified perturbation edges such as `hppD disruption → light phenotype`; **(iii)** cell-wall/extracellular localization; and **(iv)** a separate heme-PPIX branch for black-pigmented oral anaerobes. The graph should converge on the observed phenotype through pigment accumulation and localization, while retaining chemistry, taxon, and assay qualifiers.

References

1. (liporagilopes2024newinsightsinto pages 15-18): Livia C. Liporagi-Lopes, Christine Chrissian, Arlind Kacirani, Emma Camacho, Ruth E. Stark, and Arturo Casadevall. New insights into the melanin structure of lomentospora prolificans. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.01.621558, doi:10.1101/2024.11.01.621558. This article has 2 citations.

2. (liporagilopes2024newinsightsinto pages 12-15): Livia C. Liporagi-Lopes, Christine Chrissian, Arlind Kacirani, Emma Camacho, Ruth E. Stark, and Arturo Casadevall. New insights into the melanin structure of lomentospora prolificans. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.01.621558, doi:10.1101/2024.11.01.621558. This article has 2 citations.

3. (olczak2024hemophorelikeproteinsof pages 5-7): Teresa Olczak, Michał Śmiga, Svetlana V. Antonyuk, and John W. Smalley. Hemophore-like proteins of the hmuy family in the oral and gut microbiome: unraveling the mystery of their evolution. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00131-23, doi:10.1128/mmbr.00131-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

4. (olczak2024hemophorelikeproteinsof pages 2-5): Teresa Olczak, Michał Śmiga, Svetlana V. Antonyuk, and John W. Smalley. Hemophore-like proteins of the hmuy family in the oral and gut microbiome: unraveling the mystery of their evolution. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00131-23, doi:10.1128/mmbr.00131-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

5. (yin2026researchprogresson pages 20-20): Yanling Yin, Yang Jiang, Huijie Li, Wei Yi, Fan Li, Guoqing Chen, and Zhentao Wang. Research progress on the molecular structure, biosynthetic mechanism, and multidisciplinary applications of natural melanin. Agricultural Products Processing and Storage, Jan 2026. URL: https://doi.org/10.1007/s44462-025-00055-z, doi:10.1007/s44462-025-00055-z. This article has 3 citations.

6. (qin2024melanininfungi pages 4-5): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 59 citations and is from a peer-reviewed journal.

7. (jia2025fungalmelaninin pages 2-4): Hui Jia, Ning Liu, Lu Zhang, Pan Li, Yanan Meng, Wei Yuan, Haixiao Li, Dezeng Tantai, Qing Qu, Zhiyan Cao, and Jingao Dong. Fungal melanin in plant pathogens: complex biosynthesis pathways and diverse biological functions. Plants, 14:2121, Jul 2025. URL: https://doi.org/10.3390/plants14142121, doi:10.3390/plants14142121. This article has 14 citations.

8. (jia2025fungalmelaninin pages 10-12): Hui Jia, Ning Liu, Lu Zhang, Pan Li, Yanan Meng, Wei Yuan, Haixiao Li, Dezeng Tantai, Qing Qu, Zhiyan Cao, and Jingao Dong. Fungal melanin in plant pathogens: complex biosynthesis pathways and diverse biological functions. Plants, 14:2121, Jul 2025. URL: https://doi.org/10.3390/plants14142121, doi:10.3390/plants14142121. This article has 14 citations.

9. (qin2024melanininfungi pages 1-2): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 59 citations and is from a peer-reviewed journal.

10. (qin2024melanininfungi pages 8-10): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 59 citations and is from a peer-reviewed journal.

11. (qin2024melanininfungi pages 15-15): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 59 citations and is from a peer-reviewed journal.

12. (urbaniak2023invitroand pages 1-2): Mateusz M. Urbaniak, Małgorzata Gazińska, Karolina Rudnicka, Przemysław Płociński, Monika Nowak, and Magdalena Chmiela. In vitro and in vivo biocompatibility of natural and synthetic pseudomonas aeruginosa pyomelanin for potential biomedical applications. International Journal of Molecular Sciences, 24:7846, Apr 2023. URL: https://doi.org/10.3390/ijms24097846, doi:10.3390/ijms24097846. This article has 17 citations.

13. (qin2024melanininfungi pages 7-8): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 59 citations and is from a peer-reviewed journal.

14. (liporagilopes2024newinsightsinto pages 1-5): Livia C. Liporagi-Lopes, Christine Chrissian, Arlind Kacirani, Emma Camacho, Ruth E. Stark, and Arturo Casadevall. New insights into the melanin structure of lomentospora prolificans. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.01.621558, doi:10.1101/2024.11.01.621558. This article has 2 citations.

15. (olczak2024hemophorelikeproteinsof pages 20-22): Teresa Olczak, Michał Śmiga, Svetlana V. Antonyuk, and John W. Smalley. Hemophore-like proteins of the hmuy family in the oral and gut microbiome: unraveling the mystery of their evolution. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00131-23, doi:10.1128/mmbr.00131-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

16. (qin2024melanininfungi pages 2-4): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 59 citations and is from a peer-reviewed journal.

17. (munoztorres2024exploringtheagricultural pages 12-13): Patricio Muñoz-Torres, Steffany Cárdenas-Ninasivincha, and Yola Aguilar. Exploring the agricultural applications of microbial melanin. Microorganisms, 12:1352, Jul 2024. URL: https://doi.org/10.3390/microorganisms12071352, doi:10.3390/microorganisms12071352. This article has 30 citations.

18. (elzawawy2024bioproductionandoptimization pages 1-2): Nessma A. El-Zawawy, El-Refaie Kenawy, Sara Ahmed, and Shimaa El-Sapagh. Bioproduction and optimization of newly characterized melanin pigment from streptomyces djakartensis nss-3 with its anticancer, antimicrobial, and radioprotective properties. Microbial Cell Factories, Jan 2024. URL: https://doi.org/10.1186/s12934-023-02276-y, doi:10.1186/s12934-023-02276-y. This article has 63 citations and is from a peer-reviewed journal.