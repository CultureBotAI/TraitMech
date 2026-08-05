---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:38:32.902227'
end_time: '2026-08-03T23:51:28.786278'
duration_seconds: 775.88
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: predatory bacterium
  trait_identifier: traitmech:000054
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: predatory_bacterium
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic-ecology lifestyle in which a bacterium actively kills and
    consumes other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio
    bacteriovorus.
  parent_traits: METPO:1000059
  synonyms: bacterial predator
  evidence_summary: "DOI:10.1146/annurev.micro.091208.073346:  (Sockett, \"Predatory\
    \ lifestyle of Bdellovibrio bacteriovorus\", describes invasion, killing, and\
    \ digestion of prey bacteria as a predatory lifestyle.) | DOI:10.1111/1462-2920.13171:\
    \  (P\xE9rez et al. survey predatory bacteria, their hunting strategies, prey\
    \ ranges, and genome characteristics.)"
  causal_graph_summary: 'predatory_bacterium_prey_killing: 10 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** predatory bacterium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000054
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which a bacterium actively kills and consumes other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio bacteriovorus.
- **Parent traits:** METPO:1000059
- **Synonyms:** bacterial predator
- **Existing evidence:** DOI:10.1146/annurev.micro.091208.073346:  (Sockett, "Predatory lifestyle of Bdellovibrio bacteriovorus", describes invasion, killing, and digestion of prey bacteria as a predatory lifestyle.) | DOI:10.1111/1462-2920.13171:  (Pérez et al. survey predatory bacteria, their hunting strategies, prey ranges, and genome characteristics.)
- **Existing causal graph summary:** predatory_bacterium_prey_killing: 10 nodes, 6 edges

## Research Objective

Research the microbial trait **predatory bacterium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/predatory_bacterium.yaml`.

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
- **Trait label:** predatory bacterium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000054
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which a bacterium actively kills and consumes other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio bacteriovorus.
- **Parent traits:** METPO:1000059
- **Synonyms:** bacterial predator
- **Existing evidence:** DOI:10.1146/annurev.micro.091208.073346:  (Sockett, "Predatory lifestyle of Bdellovibrio bacteriovorus", describes invasion, killing, and digestion of prey bacteria as a predatory lifestyle.) | DOI:10.1111/1462-2920.13171:  (Pérez et al. survey predatory bacteria, their hunting strategies, prey ranges, and genome characteristics.)
- **Existing causal graph summary:** predatory_bacterium_prey_killing: 10 nodes, 6 edges

## Research Objective

Research the microbial trait **predatory bacterium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/predatory_bacterium.yaml`.

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


# Curation-focused research report: predatory bacterium

## 1. Scope summary

**Trait:** `traitmech:000054`  
**Category:** ECOLOGY; **term kind:** CLASS; **mapping:** REVIEWED  
**Parent supplied by the template:** `METPO:1000059`  
**Recommended operational definition:** a trophic lifestyle in which a bacterium actively attacks and kills living microbial prey and acquires prey-derived biomass or nutrients. The defining outcome is therefore not merely antagonism, but the causal sequence **active attack → prey death/lysis → nutrient acquisition**.

The class should encompass several independently evolved mechanisms:

1. **Endoperiplasmic predation:** *Bdellovibrio bacteriovorus* enters the periplasm of Gram-negative prey, converts it into a bdelloplast, consumes prey contents, grows filamentously, divides non-binarily, and lyses the remnant to exit. A sheathed polar flagellum promotes collision, type IV pili mediate attachment, and localized cell-wall remodeling permits entry. (kaplan2023bdellovibriopredationcycle pages 1-3, kaplan2023bdellovibriopredationcycle pages 3-4)
2. **Obligate epibiotic predation:** predators such as *Bdellovibrio exovorus* or *Micavibrio* remain outside the prey while feeding through an envelope junction. This is predation even without invasion because prey is killed and its biomass is consumed.
3. **Wolf-pack or extracellular/contact predation:** *Myxococcus xanthus* and related facultative predators use coordinated motility, contact-dependent systems, hydrolytic enzymes, secondary metabolites, and outer-membrane vesicles to kill prey externally. Wolf-pack predators can grow axenically, so obligate prey dependence is not part of the parent trait definition. (alexakis2024predatorybacteriain pages 1-2, mun2023predatorybacteriaas pages 1-2)
4. **Ixotrophy:** filamentous *Aureispira* captures motile prey using T9SS-secreted grappling hooks, punctures prey through a T6SS, and assimilates prey-derived material. This establishes a particularly complete molecular chain from capture through killing to nutrient uptake. (lien2024mechanismofbacterial pages 1-5, lien2024mechanismofbacterial pages 10-13, lien2024mechanismofbacterial pages 13-16)
5. **Facultative contact predation:** bradymonabacteria kill only after direct contact in the tested system but can proliferate without prey. This is a boundary case that belongs under the trait if prey-derived nutrient use is demonstrated or adequately supported. (wang2024thepredatoryproperties pages 5-8, wang2024thepredatoryproperties pages 1-2)

### Boundary rules

**Include:** active killing followed by consumption, whether prey is entered, fed upon externally, or lysed at short range. Both obligate and facultative predators qualify.

**Do not infer the trait from:**

- secretion of antibiotics or bacteriocins alone;
- competition, kin discrimination, or T6SS-mediated antagonism without evidence of trophic benefit;
- scavenging dead biomass without active killing;
- parasitic attachment that harms but does not kill/consume prey;
- bacteriophage susceptibility or phage-mediated killing;
- hydrolytic-enzyme abundance, genome annotation, plaque formation, or prey decline alone.

A practical assay should demonstrate at least prey killing plus one of: predator growth dependent on prey, incorporation of isotope-labelled prey material, loss of predation after disruption of an attack apparatus, or direct imaging of prey consumption.

## 2. Current mechanistic understanding

For the best-resolved endoperiplasmic model, the lifecycle can be represented as:

**motile attack phase → prey collision → T4P/MAT-mediated recognition and attachment → local prey-envelope remodeling → portal-mediated entry and sealing → prey killing and macromolecule hydrolysis → nutrient-dependent filamentous growth/chromosome replication → non-binary septation → prey-remnant lysis and progeny exit.**

Cryo-electron tomography directly visualized T4aP connecting predator and prey and an electron-dense attachment plaque spanning the contact region. The plaque measured approximately 15–70 nm across. During invasion it was replaced by a portal that bridged the predator and prey outer membranes; the predator’s envelope spacing was reduced by approximately 50% at the entry point, supporting a tight-seal model. (kaplan2023bdellovibriopredationcycle pages 4-6, kaplan2023bdellovibriopredationcycle pages 3-4, kaplan2023bdellovibriopredationcycle media 45a9f5f1, kaplan2023bdellovibriopredationcycle media 2e25126f)

The same work overturned the prior assumption that the flagellum is simply shed: after committed attachment, it is resorbed into the predator periplasm and degraded. This is biologically important but should be modeled as lifecycle remodeling, not as a direct cause of prey killing. (kaplan2023bdellovibriopredationcycle pages 1-3, kaplan2023bdellovibriopredationcycle pages 4-6)

## 3. Candidate nodes grouped by type

### A. Taxa and predation modes

- *Bdellovibrio bacteriovorus* — endoperiplasmic predator; label plus NCBI Taxonomy mapping should be resolved during implementation.
- *Bdellovibrio exovorus* — obligate epibiotic predator.
- *Myxococcus xanthus* — facultative wolf-pack/contact predator.
- *Aureispira* sp. CCB-QB1 — ixotrophic filamentous predator.
- Bradymonabacteria/Bradymonadia — facultative prey-dependent, contact predator.
- Gram-negative bacterial prey; *Escherichia coli*, *Vibrio cholerae*, *Vibrio campbellii*, *Proteus mirabilis*.

Because taxonomic accessions were not independently verified here, retain labels until checked against the current NCBI Taxonomy release rather than inserting remembered identifiers.

### B. Cellular structures and localizations

- sheathed unipolar flagellum — candidate grounding: `GO:0009288` only after checking that the ontology label and intended granularity match;
- type IV pilus/type IVa pilus/type IVb pilus;
- predator invasive or “biting” pole;
- prey outer membrane;
- prey periplasm;
- prey peptidoglycan/cell wall;
- bdelloplast;
- attachment plaque;
- invasion portal/entry porthole;
- CpoB-containing invasion vesicle;
- outer-membrane vesicle;
- predator–prey outer-membrane junction;
- rhapidosome/T6SS apparatus;
- GhpA grappling hook.

The attachment structures have direct visual support: T4aP contacts prey outer membrane, whereas the plaque abuts prey peptidoglycan. (kaplan2023bdellovibriopredationcycle pages 3-4, kaplan2023bdellovibriopredationcycle media 45a9f5f1, kaplan2023bdellovibriopredationcycle media 2e25126f)

### C. Genes and proteins

**High-priority *B. bacteriovorus* nodes**

- `CpoB` / locus `Bd0635` — vesicle-associated protein; deletion attempts yielded wild-type revertants, so essentiality is suggested but not conclusively demonstrated.
- MAT fibre family — 21 proteins in strain HD100, including `Bd1334`, `Bd2133`, `Bd2439`, `Bd2734`, `Bd2740`, and `Bd3182`.
- `flp1`, `flp2`, `flp4` — type IVb pilins necessary for predation in older knockout evidence; retain as taxon-specific.
- type IV pilus basal-body and retraction machinery.
- `MglA` — proposed connection between pilus dynamics and invasion signaling; secondary-review support only in the retrieved evidence.
- `Bd2269` — subtilase-family serine protease implicated in prey-remnant damage and exit; currently supported by a December 2024 preprint.
- prey peptidoglycan hydrolases, transglycosylases, endopeptidases, amidases, deacetylases — use family-level or label-only nodes unless a particular locus has direct perturbation evidence.

**Ixotrophy nodes**

- `GhpA` — 5,898-aa T9SS substrate assembling as a heptameric grappling hook;
- `SprB` — T9SS-associated gliding motility factor;
- `SprA/Sov` outer-membrane translocon;
- type IX secretion system;
- type VI secretion system subtype iv;
- insertion-sequence element;
- `iee` and `recB`, associated with starvation-responsive IS excision/reactivation.

**Myxobacterial candidates**

- Tad-like apparatus;
- type III-like contact apparatus;
- type II secretion system;
- siderophore transport components;
- hydrolytic enzymes;
- OMV cargo;
- secondary metabolites such as myxovirescin and myxalamide.

These myxobacterial nodes should generally remain in a separate taxon-specific branch. The evidence supports a multifactorial predation program but does not justify treating every antimicrobial metabolite as necessary or sufficient for the trait.

### D. Chemicals, nutrients, and environmental factors

- prey-surface glycans, including *P. mirabilis*-associated glycans;
- N-acetylglucosamine (`CHEBI:28009`) as a bound glycan component in MAT structural analysis; check whether the graph intends the free monosaccharide or a glycan residue before using this CURIE;
- prey proteins, nucleic acids, lipids, amino acids, and other macromolecule-derived nutrients;
- glutamate, serine, aspartate, isoleucine, and threonine as carbon sources supporting prey-independent *Bdellovibrio* growth; these are not themselves evidence of predation;
- iron and siderophores in myxobacterial predation;
- low nutrient availability/starvation;
- surfaces, biofilms, aqueous environments, salinity, pH, temperature, and medium viscosity;
- prey motility and prey flagella.

### E. Biological processes and candidate ontology grounding

- bacterial-type flagellum-dependent motility — verify the current GO term before curation;
- pilus-dependent adhesion/attachment — label-only unless an exact GO term is confirmed;
- prey recognition;
- prey-envelope remodeling;
- peptidoglycan hydrolysis;
- periplasmic invasion;
- prey killing/lysis;
- uptake of prey-derived material;
- filamentous predator growth;
- chromosome replication;
- non-binary division;
- progeny exit;
- biofilm disruption.

For TraitMech, it is safer to preserve biologically precise labels than to force uncertain GO mappings. Specific locus tags such as `Bd0635` and `Bd2269` should not be represented as UniProt CURIEs until the strain-specific records are verified.

## 4. Candidate causal edges

The following table gives the prioritized graph structure. It distinguishes broadly reusable lifecycle edges from mechanism- and taxon-specific branches.

| Proposed subject–predicate–object edge | Representative taxon/mode | Evidence strength | Key quantitative support | DOI |
|---|---|---|---|---|
| flagellum → enables → prey encounter | *Bdellovibrio bacteriovorus* / endoperiplasmic | direct/strong | Cryo-ET shows a sheathed unipolar flagellum in attack-phase cells; expert review states it enables high-velocity collisions with prey (kaplan2023bdellovibriopredationcycle pages 1-3, negus2017predatorversuspathogen pages 2-4) | 10.1038/s41564-023-01401-2; 10.1146/annurev-micro-090816-093618 |
| type IVa pilus (T4aP) → mediates → prey attachment | *B. bacteriovorus* / endoperiplasmic | direct/strong | Cryo-ET captured predators connected to prey by T4aP with the pilus tip contacting prey OM; multiple basal bodies aligned at contact sites (kaplan2023bdellovibriopredationcycle pages 3-4, kaplan2023bdellovibriopredationcycle media 45a9f5f1) | 10.1038/s41564-023-01401-2 |
| MAT fibre repertoire → recognizes → diverse prey surface glycans | *B. bacteriovorus* / endoperiplasmic | direct/strong | 21 MAT proteins identified; one MAT binds multiple glycans including *Proteus mirabilis* surface glycans; surface localization before encounter supports prey handling role (caulton2024bdellovibriobacteriovorususes pages 1-2, caulton2024bdellovibriobacteriovorususes pages 2-4, caulton2024bdellovibriobacteriovorususes pages 8-9) | 10.1038/s41564-023-01552-2 |
| MAT fibres → support → prey invasion | *B. bacteriovorus* / endoperiplasmic | direct/taxon-specific | Δbd2734 and Δbd2740 reduced entry at 30 min to 90.5% and 91.1% versus 96.7% WT; predation rate defects on *E. coli* but not *P. mirabilis* indicate prey-specific contribution (caulton2024bdellovibriobacteriovorususes pages 4-4, caulton2024bdellovibriobacteriovorususes pages 8-9) | 10.1038/s41564-023-01552-2 |
| prey peptidoglycan/cell-wall modification → enables → predator entry | *B. bacteriovorus* / endoperiplasmic | direct/strong | Cryo-ET observed an attachment plaque extending from predator OM to prey PG and a portal replacing it during invasion; review supports enzymatic wall modification at contact point (kaplan2023bdellovibriopredationcycle pages 4-6, kaplan2023bdellovibriopredationcycle pages 3-4, kaplan2023bdellovibriopredationcycle pages 1-3) | 10.1038/s41564-023-01401-2 |
| portal structure → seals → prey outer membrane around entering predator | *B. bacteriovorus* / endoperiplasmic | direct/strong | Portal bridged predator and prey OMs, capped the open prey OM, and constricted predator envelope by ~50% at entry point, consistent with a tight seal (kaplan2023bdellovibriopredationcycle pages 4-6) | 10.1038/s41564-023-01401-2 |
| prey nutrients → enable → growth phase initiation in bdelloplast | *B. bacteriovorus* / endoperiplasmic | direct/strong | Cryo-ET study states “If sufficient nutrients are present in the bdelloplast, *B. bacteriovorus* enters its growth phase” (kaplan2023bdellovibriopredationcycle pages 1-3) | 10.1038/s41564-023-01401-2 |
| prey biomass hydrolysis/consumption → supports → filamentous growth and non-binary division | *B. bacteriovorus* / endoperiplasmic | direct/strong | Primary and review sources state the predator consumes prey cytoplasmic contents, grows as a filament, then septates/divides into progeny; chromosome replication occurs during reproductive phase only (kaplan2023bdellovibriopredationcycle pages 1-3, kaplan2023bdellovibriopredationcycle pages 3-4) | 10.1038/s41564-023-01401-2; 10.1128/aem.00730-19 |
| Bd2269 protease → promotes → prey-remnant damage and exit | *B. bacteriovorus* / endoperiplasmic | preprint | Quantitative proteome measured 2,195 predator proteins; Bd2269 showed log2FC 3.20 at exit phase; exit assays used n=60 per strain; heterologous expression damaged *E. coli* from within (lai2024quantitativeproteomeof pages 1-4, lai2024quantitativeproteomeof pages 27-30) | 10.1101/2024.12.23.630089 |
| T9SS/GhpA grappling hooks → capture → prey flagella | *Aureispira* sp. / ixotrophic | direct/strong | Grappling hooks are heptameric GhpA assemblies with seven binding sites; contact established by gliding motility plus extracellular grappling hooks binding prey flagella (lien2024mechanismofbacterial pages 1-5, lien2024mechanismofbacterial pages 13-16) | 10.1126/science.adp0614 |
| T6SS → kills → prey cell | *Aureispira* sp. / ixotrophic | direct/strong | In time-lapse microscopy, ~78% of contacts led to prey lysis; T6SS-negative mutants showed completely abolished killing ability (lien2024mechanismofbacterial pages 1-5, lien2024mechanismofbacterial pages 10-13) | 10.1126/science.adp0614 |
| prey-derived biomass → enters → predator cell | *Aureispira* sp. / ixotrophic | direct/strong | Stable-isotope single-cell analyses showed significantly higher deuterium labeling in T6SS-positive than T6SS-negative attackers, demonstrating uptake of prey-derived components (lien2024mechanismofbacterial pages 10-13) | 10.1126/science.adp0614 |
| starvation plus IS excision → reactivates → ixotrophic predation | *Aureispira* sp. / ixotrophic | direct/strong | Under starvation, iee and recB were upregulated; T6SS-negative strains regained killing on days 33–36 after IS excision confirmed by PCR/sequencing (lien2024mechanismofbacterial pages 10-13) | 10.1126/science.adp0614 |
| Tad-/type III-like contact systems and OMV/toxin cargo → contribute to → prey killing | *Myxococcus xanthus* / wolf-pack epibiotic | inferred | Recent reviews synthesize contact-dependent killing via Tad-like and type III-like systems and short-range OMV/enzyme/metabolite killing, but graph-ready edges remain less directly resolved than in *Bdellovibrio* or *Aureispira* (lien2024mechanismofbacterial pages 13-16, sester2020secondarymetabolismof pages 34-37) | 10.3389/fmicb.2024.1339696; 10.1099/mic.0.001372; 10.3390/microorganisms11040874 |
| direct cell contact → required for → prey killing | Bradymonabacteria / facultative prey-dependent contact predator | direct/taxon-specific | Transwell and co-culture observations found no extracellular lethal factor; prey death occurred only upon direct contact and correlated with predator density (wang2024thepredatoryproperties pages 5-8, wang2024thepredatoryproperties pages 1-2) | 10.3390/microorganisms12102008 |


*Table: This table prioritizes graph-ready causal edges for the predatory bacterium trait across major mechanistic modes, emphasizing the strongest 2023–2024 evidence and clearly marking taxon-specific, inferred, and preprint-supported claims.*

### Supporting snippets and curation notes

| Proposed triple | Supporting source snippet | Curation note |
|---|---|---|
| flagellum **enables** prey encounter | “a sheathed unipolar flagellum enables high-velocity collisions with prey” | Strong for *B. bacteriovorus*; not universal because gliding predators use other encounter mechanisms. (kaplan2023bdellovibriopredationcycle pages 1-3) |
| T4aP **mediates** prey attachment | “connected to prey by T4aP, with the tip of the extended pilus clearly in contact with the prey’s OM” | Direct cryo-ET evidence; safe as a taxon-specific edge. (kaplan2023bdellovibriopredationcycle pages 3-4, kaplan2023bdellovibriopredationcycle media 45a9f5f1) |
| attachment plaque **associates with** prey-wall modification | plaque thickness “extended from the predator’s OM to the prey’s PG cell wall,” suggesting modification at the contact point | Image-derived association, not a molecularly resolved catalytic mechanism. Do not assert that the plaque itself enzymatically hydrolyses PG. (kaplan2023bdellovibriopredationcycle pages 4-6, kaplan2023bdellovibriopredationcycle media 2e25126f) |
| MAT repertoire **enables** broad prey recognition | MAT proteins localize “on the predator surface before prey encounter”; one member has specificity for prey-surface glycans | Strong family-level evidence, but individual MATs are partially redundant and prey-specific. (caulton2024bdellovibriobacteriovorususes pages 1-2, caulton2024bdellovibriobacteriovorususes pages 8-9) |
| `Bd2734`/`Bd2740` **promote** *E. coli* invasion | entry at 30 min was 90.5% and 91.1% in mutants versus 96.7% in wild type | Small effect; prey-specific because *P. mirabilis* predation was not significantly affected. Curate as “contributes to,” not “required for.” (caulton2024bdellovibriobacteriovorususes pages 4-4) |
| `CpoB/Bd0635` **localizes to** invasion vesicle/porthole | CpoB “concentrates into a vesicular compartment that is deposited into the prey periplasm” | Direct localization. “CpoB seals the porthole” remains inferred. At 15 min, 59.3% of signals were diffuse; at 20 min, 80.9% were focused. (caulton2024bdellovibriobacteriovorususes pages 1-2) |
| invasion portal **seals** prey outer membrane during entry | portal “bridged the OMs of predator and prey” and capped the open prey membrane | Strong structural interpretation, but portal molecular composition is unresolved. (kaplan2023bdellovibriopredationcycle pages 4-6) |
| sufficient prey nutrients **enable** predator growth phase | “If sufficient nutrients are present in the bdelloplast, *B. bacteriovorus* enters its growth phase.” | Suitable lifecycle edge; the particular nutrient sensors and sufficiency threshold remain unresolved. (kaplan2023bdellovibriopredationcycle pages 1-3) |
| prey-content consumption **supports** filamentous growth and division | predator “consumes the cytoplasmic contents of the prey,” then septates after nutrient exhaustion | Strong lifecycle-level edge, but avoid asserting that exhaustion alone directly triggers septation without regulatory evidence. (kaplan2023bdellovibriopredationcycle pages 1-3) |
| `Bd2269` **promotes** prey-remnant damage/exit | “Bd2269 is involved in the prey exit process and damages *E. coli* from within” | Promising but preprint-only. Proteome quantified 2,195 proteins; Bd2269 had exit-phase log2 fold-change 3.20; exit analyses used 60 events per strain. (lai2024quantitativeproteomeof pages 1-4, lai2024quantitativeproteomeof pages 27-30) |
| T9SS-secreted GhpA hooks **bind** prey flagella | contacts are established by “extracellular grappling hook-like structures that bind prey flagella” | Strong, peer-reviewed *Aureispira*-specific edge. The hook has seven protomers/binding sites. (lien2024mechanismofbacterial pages 1-5, lien2024mechanismofbacterial pages 13-16) |
| T6SS **causes** ixotrophic prey killing | killing is mediated by “puncturing of the prey cell using a Type 6 Secretion System” | Strong genetic/structural evidence: T6SS-negative mutants abolished killing. Approximately 78% of observed contacts caused lysis, and about 60% of those lysed within seconds. (lien2024mechanismofbacterial pages 1-5, lien2024mechanismofbacterial pages 10-13) |
| prey killing **enables** prey-component uptake | stable-isotope-labelled prey components “are taken up by the attacker” | Direct trophic evidence and therefore highly valuable for defining predation rather than antagonism. (lien2024mechanismofbacterial pages 1-5, lien2024mechanismofbacterial pages 10-13) |
| starvation-driven IS excision **reactivates** ixotrophy | ixotrophy is “switched off by endogenous Insertion Sequence Elements and re-activated through their excision” | Strong but system-specific regulatory edge; killing returned on days 33–36 during starvation. (lien2024mechanismofbacterial pages 1-5, lien2024mechanismofbacterial pages 10-13) |
| direct predator–prey contact **is required for** bradymonabacterial killing | prey survived across restrictive Transwell separation; no extracellular lethal substance was detected | Direct assay evidence, but the proposed needle-less T3SS mechanism is genomic/homology-based and should remain uncertain. (wang2024thepredatoryproperties pages 5-8, wang2024thepredatoryproperties pages 1-2, wang2024thepredatoryproperties pages 2-4) |

## 5. Recent developments and quantitative findings, 2023–2024

### Prey recognition and invasion organelle

Caulton et al. identified **21 MAT proteins** in *B. bacteriovorus* HD100. Thirteen possess an S74 peptidase-associated architecture and eight lack that domain. MAT proteins form trimeric fibre-like structures and are surface displayed before prey encounter. The work also identified a persistent CpoB-containing vesicle deposited at the invasion site, giving a plausible physical framework for sequential adhesion and prey-envelope handling. Individual MAT deletions caused modest, prey-dependent defects, showing that repertoire redundancy—not one universal receptor—supports broad prey range. (caulton2024bdellovibriobacteriovorususes pages 1-2, caulton2024bdellovibriobacteriovorususes pages 4-4, caulton2024bdellovibriobacteriovorususes pages 4-5, caulton2024bdellovibriobacteriovorususes pages 2-4)

### Nanometre-scale lifecycle architecture

Kaplan et al. resolved the attachment pilus, a 15–70-nm attachment plaque, flagellar resorption, and a flexible invasion portal. The evidence strongly supports a mechanically sealed entry process but does not yet identify all portal proteins. (kaplan2023bdellovibriopredationcycle pages 1-3, kaplan2023bdellovibriopredationcycle pages 4-6, kaplan2023bdellovibriopredationcycle pages 3-4)

### Molecular mechanism of ixotrophy

Lien et al. provided one of the clearest complete demonstrations of bacterial trophic predation. In *Aureispira*, SprB-associated gliding and a heptameric GhpA hook capture flagellated prey; a subtype-iv T6SS punctures and kills them; stable-isotope analysis demonstrates assimilation. Environmental analysis of a 93-day coastal time series found **35 correlated Vibrionaceae–Saprospiraceae pairs**, with ixotrophy-positive predators increasing after prey blooms around Julian days 238–242. These observations link the mechanism to natural community dynamics, although correlation alone does not prove field predation. (lien2024mechanismofbacterial pages 10-13, lien2024mechanismofbacterial pages 13-16)

### Exit-phase proteomics

The December 2024 preprint by Lai et al. quantified **2,195 predator proteins**, representing approximately **61%** of the predicted *B. bacteriovorus* proteome, and grouped them into nine temporal clusters. `Bd2269` was strongly enriched near exit and damaged *E. coli* upon heterologous expression. The genome was described as encoding approximately **10% hydrolytic enzymes**, including about **150 predicted proteases**, illustrating both its mechanistic potential and the large uncharacterized space. These numbers should be treated as strain- and annotation-specific. (lai2024quantitativeproteomeof pages 1-4, lai2024quantitativeproteomeof pages 27-30)

### Predatory flexibility

Recent work challenges a simple obligate/facultative dichotomy. Host-independent *Bdellovibrio* variants can arise through mutations affecting flagellar stators and c-di-GMP signaling, while retaining predation to varying degrees. Amino-acid-rich media can also support axenic biomass and ATP production without erasing predatory capacity. These phenotypes are boundary modifiers—not evidence against classifying the organism as a predator—because prey independence and predatory capacity are separate axes.

## 6. Applications and real-world implementation status

Predatory bacteria are being investigated for:

- reduction of multidrug-resistant Gram-negative pathogens and biofilms;
- food-processing surface and produce biofilm control;
- aquaculture control of *Vibrio* and *Aeromonas*;
- plant-pathogen biocontrol;
- wastewater treatment and environmental resistome management;
- discovery of cell-damaging enzymes such as predatory proteases;
- synthetic-biology chassis and predator–prey co-culture systems.

The 2024 clinical review reports broad in-vitro activity, generally low immune stimulation/cytotoxicity, and reductions in bacterial burden in several animal models. However, outcomes vary with prey, dose, infection site, and animal model, and **no human clinical trial had been reported**. Thus, “living antibiotic” is an application concept, not an approved clinical implementation. (alexakis2024predatorybacteriain pages 1-2, alexakis2024predatorybacteriain pages 4-5, alexakis2024predatorybacteriain pages 14-15)

Food-industry reviews identify activity against biofilms and compatibility/safety as desirable properties, but most demonstrations remain laboratory or pilot-scale rather than routine industrial deployment. (mun2023predatorybacteriaas pages 12-13, mun2023predatorybacteriaas pages 1-2)

Environmental isolates also show strong context dependence. In one 2024 three-day assay, Bdellovibrio-like isolates tolerated pH 5–9 but were killed at pH 2 and 12 and at 60 °C. Reported inhibition ranged from **70.48% for *Salmonella enterica*** to **3.84% for *Pseudomonas aeruginosa*** among tested Gram-negative prey; these values should not be generalized beyond the isolates and assay conditions.

## 7. Recommended graph architecture

A single universal linear graph would overgeneralize. A better YAML design is:

1. **Shared trait core**
   - predator encounters living prey;
   - predator establishes proximity/contact;
   - attack machinery causes prey damage/death;
   - prey biomass becomes accessible;
   - predator assimilates prey-derived nutrients;
   - nutrient acquisition supports predator maintenance or reproduction.

2. **Endoperiplasmic *Bdellovibrio* branch**
   - flagellum → collision;
   - T4P and MATs → attachment/recognition;
   - localized PG remodeling → entry;
   - portal/CpoB vesicle → sealed invasion-site organization;
   - prey digestion → filamentous growth;
   - septation → progeny;
   - exit enzymes, provisionally Bd2269 → remnant lysis/exit.

3. **Ixotrophic *Aureispira* branch**
   - gliding/SprB → encounter;
   - T9SS/GhpA → prey-flagellum capture;
   - contact → T6SS activation/puncture;
   - prey lysis → isotope-demonstrated uptake;
   - nutrient state/IS excision → predation-state regulation.

4. **Myxobacterial branch**
   - gliding/social motility → prey-field localization;
   - contact systems plus short-range enzymes/metabolites/OMVs → prey killing;
   - extracellular hydrolysis → nutrient access.

This structure preserves the common trophic logic without incorrectly making T4P, T6SS, OMVs, or periplasmic invasion universal requirements.

## 8. Warnings: claims not yet ready for TraitMech curation

1. **Do not curate `CpoB causes porthole sealing` as established.** Localization is direct; molecular sealing activity is inferred.
2. **Do not curate MAT proteins as universally required.** Single deletions cause modest and prey-specific effects, consistent with redundancy.
3. **Do not curate the bradymonabacterial needle-less T3SS as the demonstrated killing apparatus.** The claim is largely genomic/homology-based. (wang2024thepredatoryproperties pages 1-2, wang2024thepredatoryproperties pages 2-4)
4. **Do not curate every myxobacterial antibiotic, hydrolytic enzyme, or OMV cargo as a predation determinant.** Some factors are correlated, redundant, prey-specific, or also function in competition and development.
5. **Do not curate GAPDH or PGK as OMV-lysis enhancers.** Purified proteins inhibited *E. coli* growth but did not lyse prey or enhance OMV-mediated lysis in the retrieved 2023 study.
6. **Treat `Bd2269 → exit` as provisional.** The detailed evidence is presently a bioRxiv preprint, despite knockout, expression, and proteomic support. (lai2024quantitativeproteomeof pages 1-4, lai2024quantitativeproteomeof pages 27-30)
7. **Do not infer predation from prey reduction alone.** Antibiosis, resource competition, grazing by another organism, or assay artifacts can produce the same population-level result.
8. **Do not make Gram-negative prey a universal restriction.** It applies strongly to canonical intraperiplasmic *Bdellovibrio*, but wolf-pack and ixotrophic predators can have broader prey spectra.
9. **Do not equate host independence with loss of the trait.** Obligate/facultative growth is orthogonal to the capacity to kill and consume bacteria.
10. **Avoid unverified CURIEs.** Keep strain-specific proteins, attachment plaque, portal, bdelloplast, MAT family, and GhpA as labels/locus-tag nodes until exact ontology or database records are checked.

## 9. DOI-first bibliography

1. Caulton SG et al. “*Bdellovibrio bacteriovorus* uses chimeric fibre proteins to recognize and invade a broad range of bacterial hosts.” *Nature Microbiology* 9:214–227. Published online **4 January 2024**. DOI: [10.1038/s41564-023-01552-2](https://doi.org/10.1038/s41564-023-01552-2). (caulton2024bdellovibriobacteriovorususes pages 1-2)
2. Lien Y-W et al. “Mechanism of bacterial predation via ixotrophy.” *Science* 386. Published **October 2024**. DOI: [10.1126/science.adp0614](https://doi.org/10.1126/science.adp0614). (lien2024mechanismofbacterial pages 10-13, lien2024mechanismofbacterial pages 13-16)
3. Kaplan M et al. “Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography.” *Nature Microbiology* 8:1267–1279. Published **June 2023**. DOI: [10.1038/s41564-023-01401-2](https://doi.org/10.1038/s41564-023-01401-2). (kaplan2023bdellovibriopredationcycle pages 1-3)
4. Wang S et al. “The Predatory Properties of Bradymonabacteria, the Representative of Facultative Prey-Dependent Predators.” *Microorganisms* 12:2008. Published **October 2024**. DOI: [10.3390/microorganisms12102008](https://doi.org/10.3390/microorganisms12102008). (wang2024thepredatoryproperties pages 5-8)
5. Alexakis K, Baliou S, Ioannou P. “Predatory Bacteria in the Treatment of Infectious Diseases and Beyond.” *Infectious Disease Reports* 16:684–698. Published **25 July 2024**. DOI: [10.3390/idr16040052](https://doi.org/10.3390/idr16040052). (alexakis2024predatorybacteriain pages 1-2)
6. Lai TF et al. “Quantitative proteome of bacterial periplasmic predation reveals a prey damaging protease.” bioRxiv preprint. Posted **23 December 2024**. DOI: [10.1101/2024.12.23.630089](https://doi.org/10.1101/2024.12.23.630089). (lai2024quantitativeproteomeof pages 1-4)
7. Mun W et al. “Predatory bacteria as potential biofilm control and eradication agents in the food industry.” *Food Science and Biotechnology*. Published **May 2023**. DOI: [10.1007/s10068-023-01310-4](https://doi.org/10.1007/s10068-023-01310-4). (mun2023predatorybacteriaas pages 12-13, mun2023predatorybacteriaas pages 1-2)
8. Avidan O et al. “Identification and Characterization of Differentially-Regulated Type IVb Pilin Genes Necessary for Predation in Obligate Bacterial Predators.” *Scientific Reports* 7. Published **April 2017**. DOI: [10.1038/s41598-017-00951-w](https://doi.org/10.1038/s41598-017-00951-w). (avidan2017identificationandcharacterization pages 10-11)
9. Negus D et al. “Predator Versus Pathogen: How Does Predatory *Bdellovibrio bacteriovorus* Interface with the Challenges of Killing Gram-Negative Pathogens in a Host Setting?” *Annual Review of Microbiology* 71:441–457. Published **September 2017**. DOI: [10.1146/annurev-micro-090816-093618](https://doi.org/10.1146/annurev-micro-090816-093618). (negus2017predatorversuspathogen pages 2-4)
10. Pérez J et al. “Bacterial predation: 75 years and counting!” *Environmental Microbiology* 18:766–779. Published **March 2016**. DOI: [10.1111/1462-2920.13171](https://doi.org/10.1111/1462-2920.13171).

**Curation recommendation:** expand the existing 10-node/6-edge graph with the strongly supported *B. bacteriovorus* recognition–attachment–entry–growth–exit chain, but represent ixotrophy and myxobacterial predation as parallel taxon-specific mechanism branches. The most defensible universal trait edge remains **active prey killing → accessibility and assimilation of prey-derived nutrients**.

References

1. (kaplan2023bdellovibriopredationcycle pages 1-3): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

2. (kaplan2023bdellovibriopredationcycle pages 3-4): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

3. (alexakis2024predatorybacteriain pages 1-2): Konstantinos Alexakis, Stella Baliou, and Petros Ioannou. Predatory bacteria in the treatment of infectious diseases and beyond. Infectious Disease Reports, 16:684-698, Jul 2024. URL: https://doi.org/10.3390/idr16040052, doi:10.3390/idr16040052. This article has 8 citations.

4. (mun2023predatorybacteriaas pages 1-2): Wonsik Mun, Seong Yeol Choi, Sumudu Upatissa, and Robert J. Mitchell. Predatory bacteria as potential biofilm control and eradication agents in the food industry. Food Science and Biotechnology, pages 1-15, May 2023. URL: https://doi.org/10.1007/s10068-023-01310-4, doi:10.1007/s10068-023-01310-4. This article has 23 citations and is from a peer-reviewed journal.

5. (lien2024mechanismofbacterial pages 1-5): Yun-Wei Lien, Davide Amendola, Kang Soo Lee, Nina Bartlau, Jingwei Xu, Go Furusawa, Martin F. Polz, Roman Stocker, Gregor L. Weiss, and Martin Pilhofer. Mechanism of bacterial predation via ixotrophy. Oct 2024. URL: https://doi.org/10.1126/science.adp0614, doi:10.1126/science.adp0614. This article has 47 citations and is from a highest quality peer-reviewed journal.

6. (lien2024mechanismofbacterial pages 10-13): Yun-Wei Lien, Davide Amendola, Kang Soo Lee, Nina Bartlau, Jingwei Xu, Go Furusawa, Martin F. Polz, Roman Stocker, Gregor L. Weiss, and Martin Pilhofer. Mechanism of bacterial predation via ixotrophy. Oct 2024. URL: https://doi.org/10.1126/science.adp0614, doi:10.1126/science.adp0614. This article has 47 citations and is from a highest quality peer-reviewed journal.

7. (lien2024mechanismofbacterial pages 13-16): Yun-Wei Lien, Davide Amendola, Kang Soo Lee, Nina Bartlau, Jingwei Xu, Go Furusawa, Martin F. Polz, Roman Stocker, Gregor L. Weiss, and Martin Pilhofer. Mechanism of bacterial predation via ixotrophy. Oct 2024. URL: https://doi.org/10.1126/science.adp0614, doi:10.1126/science.adp0614. This article has 47 citations and is from a highest quality peer-reviewed journal.

8. (wang2024thepredatoryproperties pages 5-8): Shuo Wang, Ya Gong, Guan-Jun Chen, and Zong-Jun Du. The predatory properties of bradymonabacteria, the representative of facultative prey-dependent predators. Microorganisms, 12:2008, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102008, doi:10.3390/microorganisms12102008. This article has 4 citations.

9. (wang2024thepredatoryproperties pages 1-2): Shuo Wang, Ya Gong, Guan-Jun Chen, and Zong-Jun Du. The predatory properties of bradymonabacteria, the representative of facultative prey-dependent predators. Microorganisms, 12:2008, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102008, doi:10.3390/microorganisms12102008. This article has 4 citations.

10. (kaplan2023bdellovibriopredationcycle pages 4-6): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

11. (kaplan2023bdellovibriopredationcycle media 45a9f5f1): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

12. (kaplan2023bdellovibriopredationcycle media 2e25126f): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

13. (negus2017predatorversuspathogen pages 2-4): David Negus, Chris Moore, Michelle Baker, Dhaarini Raghunathan, Jess Tyson, and R. Elizabeth Sockett. Predator versus pathogen: how does predatory bdellovibrio bacteriovorus interface with the challenges of killing gram-negative pathogens in a host setting? Annual review of microbiology, 71:441-457, Sep 2017. URL: https://doi.org/10.1146/annurev-micro-090816-093618, doi:10.1146/annurev-micro-090816-093618. This article has 109 citations and is from a peer-reviewed journal.

14. (caulton2024bdellovibriobacteriovorususes pages 1-2): Simon G. Caulton, Carey Lambert, Jess Tyson, Paul Radford, Asmaa Al-Bayati, Samuel Greenwood, Emma J. Banks, Callum Clark, Rob Till, Elisabete Pires, R. Elizabeth Sockett, and Andrew L. Lovering. Bdellovibrio bacteriovorus uses chimeric fibre proteins to recognize and invade a broad range of bacterial hosts. Nature Microbiology, 9:214-227, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01552-2, doi:10.1038/s41564-023-01552-2. This article has 36 citations and is from a highest quality peer-reviewed journal.

15. (caulton2024bdellovibriobacteriovorususes pages 2-4): Simon G. Caulton, Carey Lambert, Jess Tyson, Paul Radford, Asmaa Al-Bayati, Samuel Greenwood, Emma J. Banks, Callum Clark, Rob Till, Elisabete Pires, R. Elizabeth Sockett, and Andrew L. Lovering. Bdellovibrio bacteriovorus uses chimeric fibre proteins to recognize and invade a broad range of bacterial hosts. Nature Microbiology, 9:214-227, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01552-2, doi:10.1038/s41564-023-01552-2. This article has 36 citations and is from a highest quality peer-reviewed journal.

16. (caulton2024bdellovibriobacteriovorususes pages 8-9): Simon G. Caulton, Carey Lambert, Jess Tyson, Paul Radford, Asmaa Al-Bayati, Samuel Greenwood, Emma J. Banks, Callum Clark, Rob Till, Elisabete Pires, R. Elizabeth Sockett, and Andrew L. Lovering. Bdellovibrio bacteriovorus uses chimeric fibre proteins to recognize and invade a broad range of bacterial hosts. Nature Microbiology, 9:214-227, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01552-2, doi:10.1038/s41564-023-01552-2. This article has 36 citations and is from a highest quality peer-reviewed journal.

17. (caulton2024bdellovibriobacteriovorususes pages 4-4): Simon G. Caulton, Carey Lambert, Jess Tyson, Paul Radford, Asmaa Al-Bayati, Samuel Greenwood, Emma J. Banks, Callum Clark, Rob Till, Elisabete Pires, R. Elizabeth Sockett, and Andrew L. Lovering. Bdellovibrio bacteriovorus uses chimeric fibre proteins to recognize and invade a broad range of bacterial hosts. Nature Microbiology, 9:214-227, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01552-2, doi:10.1038/s41564-023-01552-2. This article has 36 citations and is from a highest quality peer-reviewed journal.

18. (lai2024quantitativeproteomeof pages 1-4): Ting F. Lai, Denis Jankov, Jonas Grossmann, Bernd Roschitzki, and Simona G. Huwiler. Quantitative proteome of bacterial periplasmic predation reveals a prey damaging protease. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.23.630089, doi:10.1101/2024.12.23.630089. This article has 2 citations.

19. (lai2024quantitativeproteomeof pages 27-30): Ting F. Lai, Denis Jankov, Jonas Grossmann, Bernd Roschitzki, and Simona G. Huwiler. Quantitative proteome of bacterial periplasmic predation reveals a prey damaging protease. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.23.630089, doi:10.1101/2024.12.23.630089. This article has 2 citations.

20. (sester2020secondarymetabolismof pages 34-37): Angela Sester, Juliane Korp, and Markus Nett. Secondary metabolism of predatory bacteria. ArXiv, pages 127-153, Jan 2020. URL: https://doi.org/10.1007/978-3-030-45599-6\_5, doi:10.1007/978-3-030-45599-6\_5. This article has 10 citations.

21. (wang2024thepredatoryproperties pages 2-4): Shuo Wang, Ya Gong, Guan-Jun Chen, and Zong-Jun Du. The predatory properties of bradymonabacteria, the representative of facultative prey-dependent predators. Microorganisms, 12:2008, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102008, doi:10.3390/microorganisms12102008. This article has 4 citations.

22. (caulton2024bdellovibriobacteriovorususes pages 4-5): Simon G. Caulton, Carey Lambert, Jess Tyson, Paul Radford, Asmaa Al-Bayati, Samuel Greenwood, Emma J. Banks, Callum Clark, Rob Till, Elisabete Pires, R. Elizabeth Sockett, and Andrew L. Lovering. Bdellovibrio bacteriovorus uses chimeric fibre proteins to recognize and invade a broad range of bacterial hosts. Nature Microbiology, 9:214-227, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01552-2, doi:10.1038/s41564-023-01552-2. This article has 36 citations and is from a highest quality peer-reviewed journal.

23. (alexakis2024predatorybacteriain pages 4-5): Konstantinos Alexakis, Stella Baliou, and Petros Ioannou. Predatory bacteria in the treatment of infectious diseases and beyond. Infectious Disease Reports, 16:684-698, Jul 2024. URL: https://doi.org/10.3390/idr16040052, doi:10.3390/idr16040052. This article has 8 citations.

24. (alexakis2024predatorybacteriain pages 14-15): Konstantinos Alexakis, Stella Baliou, and Petros Ioannou. Predatory bacteria in the treatment of infectious diseases and beyond. Infectious Disease Reports, 16:684-698, Jul 2024. URL: https://doi.org/10.3390/idr16040052, doi:10.3390/idr16040052. This article has 8 citations.

25. (mun2023predatorybacteriaas pages 12-13): Wonsik Mun, Seong Yeol Choi, Sumudu Upatissa, and Robert J. Mitchell. Predatory bacteria as potential biofilm control and eradication agents in the food industry. Food Science and Biotechnology, pages 1-15, May 2023. URL: https://doi.org/10.1007/s10068-023-01310-4, doi:10.1007/s10068-023-01310-4. This article has 23 citations and is from a peer-reviewed journal.

26. (avidan2017identificationandcharacterization pages 10-11): Ofir Avidan, Margarita Petrenko, René Becker, Sebastian Beck, Michael Linscheid, Shmuel Pietrokovski, and Edouard Jurkevitch. Identification and characterization of differentially-regulated type ivb pilin genes necessary for predation in obligate bacterial predators. Scientific Reports, Apr 2017. URL: https://doi.org/10.1038/s41598-017-00951-w, doi:10.1038/s41598-017-00951-w. This article has 51 citations and is from a peer-reviewed journal.