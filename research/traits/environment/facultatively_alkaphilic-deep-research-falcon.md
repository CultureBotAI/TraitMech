---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:41:52.293235'
end_time: '2026-08-04T00:48:58.927760'
duration_seconds: 426.63
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultatively alkaphilic
  trait_identifier: METPO:1003005
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultatively_alkaphilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference in which an organism can grow at alkaline pH
    but does not require it.
  parent_traits: METPO:1003000
  synonyms: facultative alkaliphile, facultative alkaphilic, facultatively alkaliphilic
  evidence_summary: 'DOI:10.3389/fbioe.2015.00075: capable of growing near neutral
    pH (Supports facultative alkaliphiles as alkaline-growing organisms that also
    grow near neutral pH.)'
  causal_graph_summary: 'facultatively_alkaphilic_sodium_cycle_homeostasis: 11 nodes,
    10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultatively alkaphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003005
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can grow at alkaline pH but does not require it.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative alkaliphile, facultative alkaphilic, facultatively alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: capable of growing near neutral pH (Supports facultative alkaliphiles as alkaline-growing organisms that also grow near neutral pH.)
- **Existing causal graph summary:** facultatively_alkaphilic_sodium_cycle_homeostasis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **facultatively alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_alkaphilic.yaml`.

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
- **Trait label:** facultatively alkaphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003005
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism can grow at alkaline pH but does not require it.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative alkaliphile, facultative alkaphilic, facultatively alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: capable of growing near neutral pH (Supports facultative alkaliphiles as alkaline-growing organisms that also grow near neutral pH.)
- **Existing causal graph summary:** facultatively_alkaphilic_sodium_cycle_homeostasis: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **facultatively alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_alkaphilic.yaml`.

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


# Curation report: facultatively alkaphilic

## Trait record and scope

- **Trait label:** facultatively alkaphilic
- **Trait identifier:** **METPO:1003005**
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Definition:** a pH-growth preference in which an organism grows under alkaline conditions but does not require alkaline pH.
- **Parent:** METPO:1003000
- **Synonyms:** facultative alkaliphile; facultative alkaphilic; facultatively alkaliphilic.

The clearest operational interpretation is **an alkaline growth optimum together with reproducible growth near neutral pH**. Preiss et al. define facultative alkaliphiles as strains that “grow optimally under stringent alkaline conditions but are also capable of growing near neutral pH.” Their review places alkaliphile growth generally above pH 9 and often within pH 10–13. (preiss2015alkaliphilicbacteriawith pages 1-2)

A 2024 study uses a more explicit scheme: alkali-tolerant organisms have an optimum at pH 7–9 and do not grow above approximately pH 9.5; facultative alkaliphiles grow well near neutral pH but have an optimum at pH 10 or above; obligate alkaliphiles grow optimally above pH 10 but not below pH 9. These numerical cutoffs are useful assay conventions, not universal biological constants. (maksimova2024metabolicandmorphological pages 1-2)

### Boundary cases

1. **Obligately alkaliphilic:** requires alkaline conditions and fails to grow near neutral pH. This is outside **METPO:1003005** even if its alkaline-homeostasis machinery resembles that of facultative strains. (preiss2015alkaliphilicbacteriawith pages 1-2)
2. **Alkali-tolerant:** survives or grows at elevated pH but retains a neutral or mildly alkaline optimum. High-pH survival alone is insufficient to infer facultative alkaliphily. (maksimova2024metabolicandmorphological pages 1-2)
3. **Haloalkaliphilic:** combines alkaline preference with a salt requirement or strong salt adaptation. Salinity should be represented separately; it is not entailed by this trait. Horikoshi distinguished alkaliphiles from haloalkaliphiles requiring both pH above 9 and high salinity. (horikoshi1999alkaliphilessomeapplications pages 1-3)
4. **Assay-dependent classifications:** nutrient composition, sodium concentration, temperature, aeration, buffer, growth phase, and the distinction between growth and short-term metabolic activity can alter the apparent pH optimum. Horikoshi explicitly noted that some organisms exhibit multiple optima depending on nutrients, metals, and temperature. (horikoshi1999alkaliphilessomeapplications pages 1-3)
5. **Mechanism versus phenotype:** possession of an Mrp antiporter, sodium motor, or alkaliphile-like ATP synthase motif does not by itself establish the trait. The phenotype requires a pH-resolved growth curve demonstrating both alkaline preference and near-neutral growth.

## Current mechanistic model

The best-supported model is a coupled **proton–sodium cycle**. Respiratory complexes export protons and establish membrane potential. Electrogenic Mrp and related cation/proton antiporters then export Na+ while importing more H+, acidifying the cytoplasm relative to the alkaline exterior. Na+/solute symport, MotPS, and voltage-gated sodium channels replenish intracellular sodium, sustaining antiport. Proton entry through the F-type ATP synthase simultaneously supports ATP production and cytoplasmic pH homeostasis. (preiss2015alkaliphilicbacteriawith pages 4-5, krulwich2011molecularaspectsof pages 12-14, lebre2019genomicsofalkaliphiles. pages 13-17)

This creates an inverted ΔpH—inside more acidic than outside—which opposes the productive electrical component of proton motive force. Facultative alkaliphiles therefore depend heavily on ΔΨ, carefully controlled ion cycling, and adapted energy-transducing proteins. In *Bacillus* sp. TA2.A1, PMF reportedly changed from −164 mV at pH 7.5 to −78 mV at pH 10, illustrating the energetic penalty of alkaline growth. (lebre2019genomicsofalkaliphiles. pages 13-17)

For the model strain *Bacillus pseudofirmus* OF4, continuous cultures maintained pHin near 7.5 between external pH 7.5 and 9.5; at the approximate optimum pHout 10.5, pHin was 8.3. Growth continued more slowly at pHout at least 11 despite pHin at least 9.5, and the reported upper growth limit was approximately pH 11.4. (preiss2015alkaliphilicbacteriawith pages 4-5, krulwich2011molecularaspectsof pages 12-14)

## Candidate nodes grouped by type

### Trait, environment, and assay nodes

- **facultatively alkaphilic** — **METPO:1003005**
- **alkaline environmental pH** — label-only pending verification of the appropriate ENVO/PATO representation
- **near-neutral environmental pH** — label-only
- **external pH / pHout** — assay variable
- **intracellular pH / pHin** — assay variable
- **inverted transmembrane pH gradient** — label-only
- **membrane potential, ΔΨ** — label-only
- **proton motive force** — label-only; GO grounding should be verified before curation
- **sodium motive force** — label-only
- **oxygen availability / aeration** — label-only environmental factor
- **sodium concentration and salinity** — CHEBI:29101 for sodium(1+) may be used where the node is the ion; do not use it for salinity itself
- **malate-containing growth medium**, **growth rate**, and **growth at pH 7.5/10.5** — assay-context nodes

### Chemicals and metabolites

- **proton** — CHEBI:15378
- **sodium(1+)** — CHEBI:29101
- **potassium(1+)** — CHEBI:29103
- **oxygen** — CHEBI:15379
- **ATP** — CHEBI:15422
- **ADP** — CHEBI:16761
- **phosphate** — use a protonation-state-appropriate CHEBI identifier after checking assay context
- **menaquinone / reduced menaquinone pool** — specific CHEBI identifier depends on quinone species
- **acetate** — CHEBI:30089
- **magnesium ion** — CHEBI:18420
- **CCCP uncoupler** — label-only until the exact CHEBI record is verified

### Complexes, transporters, and channels

- **MrpABCDEFG hetero-oligomeric Na+/H+ antiporter** — label-only complex; component genes **mrpA–mrpG**
- **Na+/H+ antiporter activity** — GO:0015385
- **Na+/solute symporters** — family or substrate-specific grounding required
- **MotPS sodium-conducting flagellar stator/channel** — label-only
- **NavBP/NaChBac voltage-gated sodium channel** — label-only pending protein-specific accession
- **Ktr potassium importer** — label-only
- **F-type H+-transporting ATP synthase** — GO:0045259 is a candidate complex term; verify ontology version
- **ATP synthase subunit a / AtpB** and **subunit c / AtpE** — gene/protein labels; use strain-specific UniProt accessions only after sequence verification
- **AtpI** — ATP-synthase assembly/stability-associated protein
- **AtpZ** — high-pH magnesium-acquisition-associated protein in OF4
- **respiratory complex III, menaquinol:cytochrome-c oxidoreductase** — label-only unless a taxon-specific complex is curated
- **respiratory complex IV, cytochrome-c oxidase** — label-only
- **cytochrome aa3, ba3, bb3, and bd oxidases** — distinct terminal oxidase nodes in the 2024 TA2.A1 oxygen study
- **putative sodium:acetate exporter** — label-only and explicitly hypothetical

### Processes and cellular locations

- **cytoplasmic pH homeostasis** — GO:0030641
- **sodium-ion homeostasis** — GO:0055078
- **potassium-ion homeostasis** — GO:0055075
- **oxidative phosphorylation** — GO:0006119
- **ATP synthesis coupled proton transport** — GO:0015986
- **respiratory electron transport chain** — GO:0022904
- **bacterial-type flagellum-dependent motility** — GO:0071973
- **plasma/cytoplasmic membrane** — GO:0005886
- **cytoplasm** — GO:0005737
- **extracellular region / cell exterior** — GO:0005576 may be usable at a general level
- **secondary cell-wall polymers and S-layer** — label-only; mechanistic edges need stronger direct evidence for facultative alkaliphily

### Taxon/context nodes

- *Bacillus pseudofirmus* OF4, also reported in newer nomenclature as *Alkalihalobacillus pseudofirmus* OF4 — model facultative alkaliphile; verify current NCBITaxon identifier before insertion
- *Bacillus halodurans* C-125 — mechanistically informative alkaliphilic comparator
- *Bacillus aequororis* 5-DB — facultative alkaliphile tested directly in 2024
- *Bacillus subtilis* ATCC 6633 — weakly alkali-tolerant comparator
- *Caldalkalibacillus thermarum* TA2.A1 — thermoalkaliphilic comparator with 2024 chemostat proteomics

Do not assign strain-level NCBITaxon or UniProt CURIEs without checking current records and synonymy.

## Candidate causal edges

The following compact graph summarizes the highest-priority and conditional edges.

| Subject | Predicate | Object | Evidence strength | Taxon/context |
|---|---|---|---|---|
| External alkaline pH | challenges | maintenance of low cytoplasmic pH and productive proton motive force | Strong review synthesis (preiss2015alkaliphilicbacteriawith pages 1-2, krulwich2011molecularaspectsof pages 12-14, lebre2019genomicsofalkaliphiles. pages 13-17) | Extreme/facultative alkaliphiles; especially Bacillus alkaliphiles |
| Respiratory complexes III and IV | export | H+ to cell exterior/bulk medium | Strong review synthesis (preiss2015alkaliphilicbacteriawith pages 4-5) | *Bacillus pseudofirmus* OF4 schematic bioenergetic model |
| Mrp Na+/H+ antiporter complex | exports | Na+ | Strong direct+review support (jong2024quantitativeproteomicsreveals pages 6-8, krulwich2011molecularaspectsof pages 12-14, lebre2019genomicsofalkaliphiles. pages 13-17) | Bacillus alkaliphiles; essential high-pH antiporter system in OF4/C-125 |
| Mrp Na+/H+ antiporter complex | imports | H+ | Strong direct+review support (jong2024quantitativeproteomicsreveals pages 6-8, preiss2015alkaliphilicbacteriawith pages 4-5, krulwich2011molecularaspectsof pages 12-14) | Alkaliphilic Bacillus spp.; C. thermarum discussion frames same directionality |
| H+ import via cation/proton antiport | lowers | cytoplasmic pH / supports acidic pHin relative to pHout | Strong review synthesis with quantitative example (preiss2015alkaliphilicbacteriawith pages 4-5, krulwich2011molecularaspectsof pages 12-14) | OF4 maintains pHin <= 8.3 at pHout 10.8 |
| Na+/solute symporters | replenish | cytoplasmic Na+ substrate for antiporters | Moderate review synthesis (preiss2015alkaliphilicbacteriawith pages 4-5, krulwich2011molecularaspectsof pages 12-14, lebre2019genomicsofalkaliphiles. pages 13-17) | Alkaliphilic Bacillus spp.; sodium cycle completion |
| MotPS sodium channel | replenishes | cytoplasmic Na+ | Moderate review synthesis (preiss2015alkaliphilicbacteriawith pages 4-5, krulwich2011molecularaspectsof pages 12-14, lebre2019genomicsofalkaliphiles. pages 13-17) | Flagellar stator/channel in *B. halodurans* C-125 and OF4 |
| NavBP/NaChBac sodium channel | replenishes | cytoplasmic Na+ | Moderate review synthesis (preiss2015alkaliphilicbacteriawith pages 4-5, lebre2019genomicsofalkaliphiles. pages 13-17) | Important especially at low sodium/solute conditions in C-125 and OF4 |
| ATP synthase proton uptake | contributes to | ATP synthesis | Strong review synthesis (preiss2015alkaliphilicbacteriawith pages 1-2, krulwich2011molecularaspectsof pages 12-14) | Aerobic alkaliphilic Bacillus spp. |
| ATP synthase proton uptake | contributes to | pH homeostasis | Strong review synthesis (krulwich2011molecularaspectsof pages 12-14) | Aerobic alkaliphilic Bacillus spp. |
| Inverted ΔpH plus membrane potential (ΔΨ) | yields | low but productive bulk PMF | Strong review synthesis with quantitative support (preiss2015alkaliphilicbacteriawith pages 4-5, lebre2019genomicsofalkaliphiles. pages 13-17) | Bacillus alkaliphiles; TA2.A1 PMF shifts from -164 mV to -78 mV when pH 7.5 -> 10 |
| ATP synthase a-subunit residue K180 | supports | high-pH ATP synthesis and growth | Strong taxon-specific mutant evidence (preiss2015alkaliphilicbacteriawith pages 7-8) | OF4; K180G causes major loss of growth at pH 10.5 but not 7.5 |
| Low oxygen | decreases abundance of | Mrp antiporter complex | Strong direct 2024 proteomics evidence (jong2024quantitativeproteomicsreveals pages 6-8) | *Caldalkalibacillus thermarum* TA2.A1 chemostats |
| Sodium:acetate exporter | partially replaces | Mrp function under low O2 | Weak/hypothesis only (jong2024quantitativeproteomicsreveals pages 6-8) | *C. thermarum* TA2.A1; authors explicitly hypothesize replacement under acetate-producing low-O2 conditions |


*Table: This table lists concise, curation-oriented causal edges relevant to facultative alkaliphily and closely studied alkaliphilic model systems. It highlights which mechanisms are well supported versus still hypothetical, helping prioritize TraitMech curation.*

### Evidence details and supporting snippets

| Proposed subject–predicate–object | Reference | Supporting snippet | Curation note |
|---|---|---|---|
| alkaline external pH — **challenges** — productive PMF | 10.3389/fbioe.2015.00075 | “The reversed gradient reduces the trans-membrane proton-motive force available to energize ATP synthesis.” | Strong conceptual edge; applies broadly to proton-coupled alkaliphiles. (preiss2015alkaliphilicbacteriawith pages 1-2) |
| respiratory complexes III and IV — **export** — H+ | 10.3389/fbioe.2015.00075 | complexes III and IV “pump protons out of the cell into the bulk medium” | Strong OF4 mechanistic model; retain taxon context. (preiss2015alkaliphilicbacteriawith pages 4-5) |
| respiratory H+ export — **generates** — PMF/ΔΨ | 10.1007/10_2018_83 | “outwards pumping of protons through the respiratory chain to generate a PMF” | Review synthesis; appropriate as a pathway-level edge. (lebre2019genomicsofalkaliphiles. pages 13-17) |
| Mrp Na+/H+ antiporter — **exports** — Na+ | 10.3389/fmicb.2024.1468929 | “facilitates the export of Na+ coupled with the import of H+” | Direction is explicit. The 2024 experiment is TA2.A1; OF4 necessity is supported by older mutant studies. (jong2024quantitativeproteomicsreveals pages 6-8) |
| Mrp Na+/H+ antiporter — **imports** — H+ | 10.3389/fmicb.2024.1468929 | “export of Na+ coupled with the import of H+” | High-priority edge. Specify electrogenic stoichiometry only if a primary source establishes it for the exact taxon. (jong2024quantitativeproteomicsreveals pages 6-8) |
| cation/H+ antiport — **maintains** — inverted ΔpH | 10.3389/fbioe.2015.00075 | antiporter proton movement “contributes to the maintenance of a low pH inside” | Strong review-supported edge; OF4 example is pHin 8.3 at pHout 10.5. (preiss2015alkaliphilicbacteriawith pages 4-5) |
| Mrp complex — **required for** — high-pH pH homeostasis | 10.1038/nrmicro2549 | Mrp has an “indispensible role at high pH” | Strong but primarily established in alkaliphilic *Bacillus*. A C-125 mrpA point mutation caused loss of alkaline pH homeostasis and the alkaliphilic phenotype. (krulwich2011molecularaspectsof pages 12-14) |
| mrpA–mrpG — **required for assembly/activity of** — Mrp antiporter | 10.1038/nrmicro2549 | “All the Mrp proteins are required to form a hetero-oligomeric complex and are required for Mrp antiport activity.” | Strong complex-composition edge; seven-gene OF4 operon was also reported essential for Na+ exclusion/antiport. (krulwich2011molecularaspectsof pages 12-14, lebre2019genomicsofalkaliphiles. pages 13-17) |
| Na+/solute symport — **replenishes** — cytoplasmic Na+ | 10.1038/nrmicro2549 | the Na+ requirement is met by “numerous Na+/solute symporters” | Moderate review support; substrate-specific transporters should replace the generic node when known. (krulwich2011molecularaspectsof pages 12-14) |
| MotPS — **imports** — Na+ | 10.3389/fbioe.2015.00075 | “Additional sodium ions enter through the MotPS sodium-ion channels” | Taxon-specific to OF4/C-125-like systems; MotPS also powers motility. (preiss2015alkaliphilicbacteriawith pages 4-5) |
| NavBP — **imports** — Na+ | 10.3389/fbioe.2015.00075 | sodium enters through “a voltage-gated sodium-ion channel, NavBP” | Retain OF4 context; importance increases under low sodium/solute conditions. (preiss2015alkaliphilicbacteriawith pages 4-5, lebre2019genomicsofalkaliphiles. pages 13-17) |
| Na+ re-entry — **enables continued** — H+ uptake by antiporters | 10.3389/fbioe.2015.00075 | Na+ influxes “complete a sodium-ion cycle, enabling continued uptake of protons via antiporters” | High-value causal bridge for the existing sodium-cycle graph. (preiss2015alkaliphilicbacteriawith pages 4-5) |
| MotPS sodium stator — **supports** — flagellar motility under inverted ΔpH | 10.1007/10_2018_83 | alkaliphiles “use SMF-driven motors to achieve motility” | Moderate, model-specific edge. Do not generalize to all facultative alkaliphiles. (lebre2019genomicsofalkaliphiles. pages 13-17) |
| F-type ATP synthase proton uptake — **produces** — ATP | 10.1038/nrmicro2549 | aerobic alkaliphilic *Bacillus* ATP synthases “function in the synthetic direction” | Strong model-specific edge. (krulwich2011molecularaspectsof pages 12-14) |
| ATP synthase proton uptake — **contributes to** — pH homeostasis | 10.1038/nrmicro2549 | “The proton uptake that accompanies ATP synthesis…contributes to alkaliphile pH homeostasis.” | Strong direct statement for aerobic alkaliphilic *Bacillus*. (krulwich2011molecularaspectsof pages 12-14) |
| ATP synthase a-subunit K180 — **supports** — high-pH growth/ATP synthesis | 10.3389/fbioe.2015.00075 | K180G caused “major loss of growth on malate at pH 10.5 but not 7.5” | Strong OF4 mutational evidence. K180G growth was 18% of WT at pH 10.5 versus 86% at pH 7.5; do not elevate a residue-level edge to a universal trait mechanism. (preiss2015alkaliphilicbacteriawith pages 7-8) |
| AtpZ — **enhances** — Mg acquisition at high pH | 10.3389/fbioe.2015.00075 | “atpZ gene has been shown to enhance the ability…to acquire sufficient magnesium…at elevated pH” | Potential auxiliary OF4 edge; curate only with the underlying primary experiment and precise gene/protein grounding. (preiss2015alkaliphilicbacteriawith pages 7-8) |
| low oxygen — **decreases abundance of** — Mrp | 10.3389/fmicb.2024.1468929 | “Mrp is also significantly downregulated at lower O2 concentrations.” | Direct 2024 proteomics in TA2.A1; condition- and taxon-specific, not a defining trait edge. (jong2024quantitativeproteomicsreveals pages 6-8) |
| low oxygen — **shifts terminal oxidase abundance from** — aa3 toward ba3 | 10.3389/fmicb.2024.1468929 | “Cyt. aa3 is downregulated when oxygen becomes limiting, while Cyt. ba3 is upregulated.” | Direct 2024 chemostat result; useful for a conditional subgraph. aa3 translocated 2 H+ per 2e− and ba3 1 H+ per 2e− in the authors’ comparison. (jong2024quantitativeproteomicsreveals pages 6-8) |
| sodium:acetate export — **partially substitutes for** — Mrp-mediated Na+ export | 10.3389/fmicb.2024.1468929 | “we hypothesize that the function of Mrp is—at least partly—replaced by the acetate exporter” | **Do not curate as established causality.** No in-vivo or in-vitro acetate-export data were reported. (jong2024quantitativeproteomicsreveals pages 6-8) |
| facultative alkaliphily — **enables tolerance of** — wide pH and 50 g/L NaCl | 10.1155/2024/3087296 | 5-DB showed “broader general resistance…(wide pH range, 50 g/L NaCl)” | Direct 2024 phenotype for *B. aequororis* 5-DB, but salt tolerance is a correlated strain phenotype, not entailed by METPO:1003005. (maksimova2024metabolicandmorphological pages 1-2) |

## Recent developments, 2023–2024

### Condition-dependent sodium-cycle regulation

The most directly relevant recent mechanistic study is the October 2024 quantitative-proteomics analysis of *C. thermarum* TA2.A1 across 0.25–4.2% O2 in chemostats. The organism grew even at 0.25% inlet O2. Mrp abundance declined under lower oxygen, while terminal-oxidase usage shifted: aa3 predominated at the highest O2 level and ba3 at lower levels. This demonstrates that the canonical sodium-cycle graph is not static but is regulated by respiratory state. (jong2024quantitativeproteomicsreveals pages 6-8)

The authors proposed that sodium-coupled acetate export might reduce reliance on Mrp during oxygen limitation, when acetate is produced concurrently with respiration. Because the paper explicitly states that no in-vivo or in-vitro acetate-export data were available, this remains a testable hypothesis rather than a curation-grade edge. (jong2024quantitativeproteomicsreveals pages 6-8)

### Broader stress physiology of a facultative alkaliphile

The 2024 *B. aequororis* 5-DB study compared a facultative alkaliphile with weakly alkali-tolerant *B. subtilis* ATCC 6633 using dehydrogenase activity, ATP bioluminescence, AFM, and fluorescent intracellular-pH measurements. Strain 5-DB grew at pH 11 and 50 g/L NaCl and showed broader pH resistance, maintenance of ΔpH, and less cellular damage than the comparator. (maksimova2024metabolicandmorphological pages 1-2)

The intracellular-pH assays found pHin below pHout for both cultures under alkaline conditions, with 5-DB maintaining a larger ΔpH at pHout 11 in 50 g/L than 0.5 g/L NaCl. These observations support a homeostasis phenotype but do not identify the responsible genes experimentally. (maksimova2024metabolicandmorphological pages 5-6)

### State of the field

Recent work expands understanding of conditional respiratory and transport regulation, but the core causal evidence for facultative alkaliphily still derives largely from OF4/C-125 physiology and mutants. The authoritative synthesis emphasizes that pH homeostasis is cell-wide and varies with oxygen and salinity, while quantitative omics and transporter kinetics remain relatively scarce for extremophiles. (krulwich2011molecularaspectsof pages 12-14)

## Applications and real-world relevance

Alkaliphilic microorganisms and their enzymes are used where high pH improves processing or suppresses contaminants. Established areas include alkaline proteases, amylases, and cellulases; traditional alkaline indigo fermentation; and use of alkaliphilic cells in high-pH bioprocesses such as biological removal of H2S from sour gas streams. (preiss2015alkaliphilicbacteriawith pages 1-2, horikoshi1999alkaliphilessomeapplications pages 1-3)

Facultative strains are particularly attractive for engineering because they can be cultivated near neutral pH and deployed under alkaline process conditions. The 2024 5-DB study highlights lipase and amylase activity plus tolerance of pH 11 and 50 g/L NaCl as potentially useful process traits, although no industrial-scale implementation of that strain was demonstrated. (maksimova2024metabolicandmorphological pages 1-2)

## Priority recommendation for `facultatively_alkaphilic.yaml`

A defensible conserved core graph is:

1. **alkaline external pH → decreases bulk proton availability / imposes inverted ΔpH**;
2. **respiratory electron transport → exports H+ → establishes ΔΨ/PMF**;
3. **Mrp Na+/H+ antiport → exports Na+ and imports H+**;
4. **H+ import → lowers pHin → supports cytoplasmic-pH homeostasis**;
5. **MotPS/NavBP/Na+-solute symport → import Na+ → sustain Mrp turnover**;
6. **F-type ATP synthase proton uptake → ATP synthesis and contributes to pH homeostasis**;
7. **combined pH homeostasis and energy conservation → enables growth at alkaline pH**;
8. **retained growth near neutral pH → distinguishes facultative from obligate alkaliphily**.

Edges 2–6 should initially carry a taxon/evidence qualifier such as “demonstrated in aerobic alkaliphilic *Bacillus*, especially OF4,” because they are not proven universal across bacterial and archaeal facultative alkaliphiles.

## Warnings: claims not yet suitable for unqualified TraitMech curation

- Do **not** define the trait by a single pH threshold. Use an assay-supported alkaline optimum plus near-neutral growth.
- Do **not** infer facultative alkaliphily from survival, ATP content, dehydrogenase activity, genome annotation, or transporter presence alone.
- Do **not** treat sodium coupling as universally obligatory. Some alkaliphiles use proton-coupled ATP synthases; sodium cycling is important but not universal. (lebre2019genomicsofalkaliphiles. pages 13-17)
- Do **not** generalize OF4 ATP-synthase motifs, MotPS, NavBP, or Mrp essentiality to every facultative alkaliphile.
- Do **not** curate cell-wall polymers, S-layers, neutral-lipid ratios, or localized proton-retention models as necessary causes of this trait without direct mutant or intervention evidence in a facultative strain.
- Do **not** curate the 2024 acetate-exporter→Mrp-substitution edge except as `hypothesized` or `uncertain`.
- Do **not** merge alkaliphily with halotolerance. The 50 g/L NaCl phenotype of 5-DB is strain-specific. (maksimova2024metabolicandmorphological pages 1-2)
- Verify all NCBITaxon, UniProt, Rhea, KEGG, and strain identifiers before YAML insertion; nomenclature changes involving *Bacillus*/*Alkalihalobacillus* are a particular risk.

## DOI-first bibliography

1. Maksimova YG, Eliseeva A, Maksimov A. **Metabolic and Morphological Aspects of Adaptation of Alkaliphilic *Bacillus aequororis* 5-DB and Alkali-Tolerant *Bacillus subtilis* ATCC 6633 to Changes in pH and Mineralization.** *International Journal of Microbiology*. Published 2024; received April 10 and accepted July 10, 2024. DOI: [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296). (maksimova2024metabolicandmorphological pages 1-2)
2. de Jong SI et al. **Quantitative proteomics reveals oxygen-induced adaptations in *Caldalkalibacillus thermarum* TA2.A1 microaerobic chemostat cultures.** *Frontiers in Microbiology*. Published October 2024. DOI: [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929). (jong2024quantitativeproteomicsreveals pages 6-8)
3. Lebre PH, Cowan DA. **Genomics of Alkaliphiles.** *Advances in Biochemical Engineering/Biotechnology*. Published January 2019. DOI: [10.1007/10_2018_83](https://doi.org/10.1007/10_2018_83). (lebre2019genomicsofalkaliphiles. pages 13-17)
4. Preiss L, Hicks DB, Suzuki S, Meier T, Krulwich TA. **Alkaliphilic Bacteria with Impact on Industrial Applications, Concepts of Early Life Forms, and Bioenergetics of ATP Synthesis.** *Frontiers in Bioengineering and Biotechnology*. Published June 3, 2015. DOI: [10.3389/fbioe.2015.00075](https://doi.org/10.3389/fbioe.2015.00075). (preiss2015alkaliphilicbacteriawith pages 1-2)
5. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology*. Published May 2011. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 12-14)
6. Horikoshi K. **Alkaliphiles: Some Applications of Their Products for Biotechnology.** *Microbiology and Molecular Biology Reviews*. Published December 1999. DOI: [10.1128/MMBR.63.4.735-750.1999](https://doi.org/10.1128/MMBR.63.4.735-750.1999). (horikoshi1999alkaliphilessomeapplications pages 1-3)

**Overall assessment:** **METPO:1003005** is suitable for a TraitMech graph centered on alkaline pH, inverted ΔpH, respiration, cation/proton antiport, sodium-cycle closure, and ATP synthesis. The graph should be framed as a best-supported aerobic *Bacillus*-type mechanism with explicit taxon qualifiers, rather than as a universal molecular definition of facultative alkaliphily.

References

1. (preiss2015alkaliphilicbacteriawith pages 1-2): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

2. (maksimova2024metabolicandmorphological pages 1-2): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

3. (horikoshi1999alkaliphilessomeapplications pages 1-3): Koki Horikoshi. Alkaliphiles: some applications of their products for biotechnology. Microbiology and Molecular Biology Reviews, 63:735-750, Dec 1999. URL: https://doi.org/10.1128/mmbr.63.4.735-750.1999, doi:10.1128/mmbr.63.4.735-750.1999. This article has 1281 citations and is from a domain leading peer-reviewed journal.

4. (preiss2015alkaliphilicbacteriawith pages 4-5): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

5. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

6. (lebre2019genomicsofalkaliphiles. pages 13-17): Pedro H. Lebre and Don A. Cowan. Genomics of alkaliphiles. Advances in biochemical engineering/biotechnology, pages 135-155, Jan 2019. URL: https://doi.org/10.1007/10\_2018\_83, doi:10.1007/10\_2018\_83. This article has 9 citations.

7. (jong2024quantitativeproteomicsreveals pages 6-8): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

8. (preiss2015alkaliphilicbacteriawith pages 7-8): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

9. (maksimova2024metabolicandmorphological pages 5-6): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.