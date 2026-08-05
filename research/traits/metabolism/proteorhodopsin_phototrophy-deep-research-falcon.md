---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:50:33.052115'
end_time: '2026-08-04T07:01:18.412210'
duration_seconds: 645.36
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: proteorhodopsin phototrophy
  trait_identifier: traitmech:000036
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: proteorhodopsin_phototrophy
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A light-harvesting metabolism in which a retinal-containing membrane
    protein (proteorhodopsin) acts as a light-driven proton pump, generating proton
    motive force without chlorophyll-based reaction centers. Widespread among marine
    bacterioplankton.
  parent_traits: traitmech:000037
  synonyms: rhodopsin-based phototrophy
  evidence_summary: "DOI:10.1126/science.289.5486.1902:  (B\xE9j\xE0 et al. identified\
    \ proteorhodopsin, a retinal-binding light-driven proton pump in an uncultivated\
    \ marine bacterium, as evidence for a new type of phototrophy in the sea.) | DOI:10.1038/35081051:\
    \  (B\xE9j\xE0 et al., \"Proteorhodopsin phototrophy in the ocean\", supports\
    \ proteorhodopsin as a widespread, spectrally tuned light-energy capture system\
    \ in marine bacteria.)"
  causal_graph_summary: 'proteorhodopsin_light_driven_proton_pump: 8 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** proteorhodopsin phototrophy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000036
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A light-harvesting metabolism in which a retinal-containing membrane protein (proteorhodopsin) acts as a light-driven proton pump, generating proton motive force without chlorophyll-based reaction centers. Widespread among marine bacterioplankton.
- **Parent traits:** traitmech:000037
- **Synonyms:** rhodopsin-based phototrophy
- **Existing evidence:** DOI:10.1126/science.289.5486.1902:  (Béjà et al. identified proteorhodopsin, a retinal-binding light-driven proton pump in an uncultivated marine bacterium, as evidence for a new type of phototrophy in the sea.) | DOI:10.1038/35081051:  (Béjà et al., "Proteorhodopsin phototrophy in the ocean", supports proteorhodopsin as a widespread, spectrally tuned light-energy capture system in marine bacteria.)
- **Existing causal graph summary:** proteorhodopsin_light_driven_proton_pump: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **proteorhodopsin phototrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteorhodopsin_phototrophy.yaml`.

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
- **Trait label:** proteorhodopsin phototrophy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000036
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A light-harvesting metabolism in which a retinal-containing membrane protein (proteorhodopsin) acts as a light-driven proton pump, generating proton motive force without chlorophyll-based reaction centers. Widespread among marine bacterioplankton.
- **Parent traits:** traitmech:000037
- **Synonyms:** rhodopsin-based phototrophy
- **Existing evidence:** DOI:10.1126/science.289.5486.1902:  (Béjà et al. identified proteorhodopsin, a retinal-binding light-driven proton pump in an uncultivated marine bacterium, as evidence for a new type of phototrophy in the sea.) | DOI:10.1038/35081051:  (Béjà et al., "Proteorhodopsin phototrophy in the ocean", supports proteorhodopsin as a widespread, spectrally tuned light-energy capture system in marine bacteria.)
- **Existing causal graph summary:** proteorhodopsin_light_driven_proton_pump: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **proteorhodopsin phototrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteorhodopsin_phototrophy.yaml`.

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


# Curation report: proteorhodopsin phototrophy

## Trait record and scope

- **Trait label:** proteorhodopsin phototrophy
- **Trait identifier:** **`traitmech:000036`**
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `traitmech:000037`
- **Synonym:** rhodopsin-based phototrophy

### Recommended operational definition

Proteorhodopsin phototrophy is the physiological capacity to use a **retinal-bound, outward proton-pumping proteorhodopsin in the cytoplasmic membrane** to convert absorbed light into a transmembrane electrochemical proton gradient. That proton-motive force can support ATP synthesis and, depending on organism and conditions, transport, motility, maintenance, growth, or survival. It is generally an **energy-supplementing photoheterotrophic mechanism**, not carbon-fixing photosynthesis: proteorhodopsin supplies energy but does not itself provide a reaction center, electron-transfer chain, reducing power, or carbon-fixation pathway. PR-bearing SAR86 genomes, for example, lack autotrophic carbon-fixation pathways despite having PR-based energetic potential. (feng2023isproteorhodopsina pages 17-23, dupont2012genomicinsightsto pages 8-9)

The minimum mechanistic phenotype should require evidence for functional light-driven proton translocation, or a sufficiently complete genotype plus functional validation. A proteorhodopsin-like sequence alone is not enough: retinal availability, membrane expression, pump direction, and ion specificity can determine whether the phenotype exists. SAR86 illustrates this distinction because some genomes carry PR but apparently lack retinal biosynthesis and may have to acquire the chromophore externally. (dupont2012genomicinsightsto pages 8-9)

### Boundary cases

**Include:** outward H⁺-pumping bacterial proteorhodopsins that bind retinal and generate proton motive force under illumination, including systems that principally improve maintenance or stress survival rather than measurable exponential growth.

**Exclude or model separately:**

1. **Sensory rhodopsins**, light-gated channels, inward proton pumps, and chloride/sodium pumps; sequence homology to microbial rhodopsins does not establish PR phototrophy.
2. **Chlorophyll-based photosynthesis and aerobic anoxygenic phototrophy**, which use reaction centers and electron-transfer machinery absent from the minimal PR system.
3. **Retinal biosynthesis alone** or an unexpressed PR gene.
4. **Viral or eukaryotic proton-pumping rhodopsins** unless TraitMech explicitly intends the trait to extend beyond cellular bacterial PR systems. Viral rhodopsins can bind retinal and pump protons, but are evolutionarily and host-contextually distinct. (needham2019adistinctlineage pages 10-10)
5. **Autotrophy as an intrinsic consequence.** A 2024 culture study found no significant light–dark difference in inorganic-carbon assimilation, showing that PR-dependent ATP generation does not automatically imply carbon fixation.

| Subject | Predicate | Object | Confidence | Key evidence |
|---|---|---|---|---|
| light | activates | retinal-bound proteorhodopsin | High | PR is a "light-driven proton pump" whose mechanism depends on retinal/photoisomerization; foundational identification in marine bacteria and later mechanistic summaries support light activation (DOI:10.1126/science.289.5486.1902; DOI:10.1038/35081051; DOI:10.25959/23241740) (feng2023isproteorhodopsina pages 17-23, feng2023isproteorhodopsina pages 28-34) |
| retinal-bound proteorhodopsin | exports | protons (H+) across the membrane | High | Direct functional evidence from illuminated cells and heterologous expression shows outward proton pumping / external pH change; recent work summarizes PR as bacterial proton pumps (DOI:10.1128/AEM.02425-09; DOI:10.25959/23241740; DOI:10.1126/sciadv.adu5303) (johnson2010enhancementofsurvival pages 1-2, feng2023isproteorhodopsina pages 89-95, bukhdruker2025proteorhodopsininsightsinto pages 18-19) |
| proton export by proteorhodopsin | generates | proton motive force | High | Multiple sources explicitly state PR translocates protons to create membrane potential/PMF; direct in engineered Shewanella, established across PR literature (DOI:10.1128/AEM.02425-09; DOI:10.25959/23241740) (johnson2010enhancementofsurvival pages 1-2, feng2023isproteorhodopsina pages 28-34, feng2023isproteorhodopsina pages 17-23) |
| proton motive force | drives | F-type ATP synthase | Medium-High | Established bioenergetic coupling rather than directly reconstituted in every PR study: sources state PR-generated PMF drives ATP synthesis via F0F1-ATPase / proton-translocating ATPase (DOI:10.25959/23241740; DOI:10.1128/AEM.02425-09) (feng2023isproteorhodopsina pages 28-34, feng2023isproteorhodopsina pages 17-23, feng2023isproteorhodopsina pages 34-38, johnson2010enhancementofsurvival pages 1-2) |
| F-type ATP synthase | produces | ATP | High | Established ATP synthase function; PR studies cite ATP increases or ATP synthesis supported by PR-generated PMF in heterologous/native systems (DOI:10.1128/AEM.02425-09; DOI:10.25959/23241740) (johnson2010enhancementofsurvival pages 1-2, feng2023isproteorhodopsina pages 28-34) |
| beta-carotene cleavage / retinal supply | enables | functional proteorhodopsin | High | Genome and biochemical evidence link PR function to retinal availability: PR-containing marine genomes carry retinal biosynthesis genes including blh and carotenoid genes; PR requires retinal/retinol for functionality (DOI:10.1073/pnas.0712027105; DOI:10.1038/ismej.2011.189) (dupont2012genomicinsightsto pages 8-9) |


*Table: Compact curation table of the strongest mechanistic edges for proteorhodopsin phototrophy, from light activation and proton export to PMF-coupled ATP production, plus retinal supply. It distinguishes directly shown PR steps from the broader established ATP synthase coupling used in TraitMech curation.*

## Candidate graph nodes

Identifiers below are conservative suggestions; exact ontology labels and releases should be checked during repository validation. No identifier is proposed for a strain-specific PR protein without a verified accession.

### Genes, proteins, and complexes

| Candidate node | Role | Suggested grounding |
|---|---|---|
| proteorhodopsin gene (`pr`) | Encodes the retinal-binding outward H⁺ pump | Label-only unless a taxon-specific gene/protein accession is used |
| proteorhodopsin holoprotein | Light-activated integral-membrane proton pump | GO:0015078, proton transmembrane transporter activity; optionally label-only for protein identity |
| proteorhodopsin apoprotein | PR before retinal incorporation | Label-only |
| retinal–proteorhodopsin Schiff-base complex | Photoactive holoprotein state | Label-only |
| conserved retinal-binding lysine | Forms the protonated Schiff base with retinal | Label-only; residue numbering is protein-specific (reported as Lys230 in one PR context) (feng2023isproteorhodopsina pages 17-23) |
| `blh` β-carotene 15,15′-dioxygenase | Cleaves β-carotene to supply retinal | EC:1.13.11.63; use a verified UniProt accession only for a specified organism |
| `crtE`, `crtB`, `crtI`, `crtY` | Carotenoid/β-carotene precursor synthesis | Gene-label nodes unless exact enzyme reaction and taxon are specified |
| F-type H⁺-transporting ATP synthase | Uses PMF to phosphorylate ADP | GO:0015986, ATP synthesis coupled proton transport |
| carotenoid–PR antenna complex | Expanded light harvesting in certain Bacteroidota PRs | Label-only; recent and taxon-restricted |

Polaribacter sp. MED152 contains PR together with carotenoid/retinal synthesis genes `crtEBIY` and `blh`, supporting inclusion of a retinal-supply module, although not every PR-bearing genome contains that complete module. (dupont2012genomicinsightsto pages 8-9)

### Chemicals and physical inputs

| Node | Suggested CURIE |
|---|---|
| light / photon | CHEBI:30212 (photon) |
| all-trans-retinal | CHEBI:15035 |
| β-carotene | CHEBI:17579 |
| proton (H⁺) | CHEBI:15378 |
| ATP | CHEBI:15422 |
| ADP | CHEBI:16761 |
| phosphate | CHEBI:43474 |
| myxol | Label-only pending ontology verification |
| zeaxanthin | CHEBI:27547 |
| carbon/organic substrate, lactate | Use substrate-specific CHEBI identifiers when the edge is taxon-specific |
| CCCP protonophore | CHEBI:3259; useful as an experimental perturbation node |

### Processes, functions, and locations

| Node | Suggested grounding |
|---|---|
| light absorption / retinal photoisomerization | GO:0018298 may be considered for protein–chromophore linkage; otherwise label-only process |
| proton transmembrane transport | GO:1902600 |
| proton-motive force | Label-only or ontology term after repository-specific verification |
| ATP synthesis coupled proton transport | GO:0015986 |
| cytoplasmic membrane | GO:0005886 |
| extracellular/periplasmic proton accumulation | Label-only compartments; use taxon-appropriate envelope model |
| substrate uptake | GO:0055085, transmembrane transport, or substrate-specific term |
| flagellar motility | GO:0001539 where applicable |
| maintenance during starvation | Label-only biological outcome |
| photoheterotrophic growth | Label-only phenotype |
| anaplerotic carbon fixation | Label-only unless a specific enzyme/reaction is represented |

### Environmental and experimental factors

- Blue–green illumination, wavelength, irradiance, and light/dark regime.
- Carbon or nutrient limitation; nutrient-replete conditions should be represented separately.
- Salinity/osmotic stress and low temperature for sea-ice isolates.
- Oxygen and respiratory status, because PR may supplement or sometimes replace respiratory energy conservation.
- External retinal supplementation, `blh`/carotenoid pathway status, and protonophore treatment.
- ENVO candidates should be selected for the sampled habitat—marine photic zone, seawater, Antarctic coastal water, or sea ice—only after checking exact ENVO terms.

### Exemplary taxa

Taxon nodes should use verified NCBITaxon records during curation. Relevant exemplars include *Dokdonia* sp. MED134, *Polaribacter* sp. MED152, *Psychroflexus torquis*, *Candidatus Puniceispirillum marinum* IMCC1322, SAR11, SAR86, and engineered *Shewanella oneidensis* MR-1. Field data also implicate Flavobacteriia/Bacteroidota, Alphaproteobacteria, and Gammaproteobacteria. (cifuentesanticevic2021proteorhodopsinphototrophyin pages 2-3, cifuentesanticevic2021proteorhodopsinphototrophyin pages 5-6)

## Candidate causal edges

“Core” indicates suitability for the main TraitMech graph. “Context” means the edge should be qualified by taxon or condition. Snippets are concise quotations or close source excerpts available from the retrieved text.

| Subject | Predicate | Object | Status | Reference | Supporting snippet | Curation notes |
|---|---|---|---|---|---|---|
| photon | is absorbed by | retinal-bound proteorhodopsin | **Core** | Béjà et al. 2000/2001; Feng 2023 | “retinal-dependent photoisomerization”; retinal is linked through a “protonated Schiff base” | The foundational activation step; do not represent apo-PR as photoactive. (feng2023isproteorhodopsina pages 17-23, feng2023isproteorhodopsina pages 28-34) |
| photon absorption | causes | retinal photoisomerization and PR conformational change | **Core** | Feng 2023 | “conformational shifts upon light absorption” transport protons | A molecular intermediate that can be retained if the graph supports state changes. (feng2023isproteorhodopsina pages 17-23) |
| activated proteorhodopsin | transports | H⁺ from cytoplasmic to external side of membrane | **Core** | Johnson et al. 2010; Feng 2023 | illuminated cells showed “rapid external pH decline indicating proton extrusion” | Direct functional edge; CCCP-sensitive pH assays strengthen pump interpretation. (johnson2010enhancementofsurvival pages 1-2, feng2023isproteorhodopsina pages 89-95) |
| outward H⁺ transport | generates | membrane potential/proton-motive force | **Core** | Johnson et al. 2010; Feng 2023 | “generates membrane potential and proton motive force” | Strong mechanistic consensus. (johnson2010enhancementofsurvival pages 1-2, feng2023isproteorhodopsina pages 28-34) |
| proton-motive force | drives | F₀F₁ ATP synthase | **Core** | Feng 2023; Johnson et al. 2010 | “protons re-enter via ATP synthase” | Established chemiosmotic coupling; direct demonstration need not be repeated in every organism. (feng2023isproteorhodopsina pages 28-34, feng2023isproteorhodopsina pages 17-23, johnson2010enhancementofsurvival pages 1-2) |
| F-type ATP synthase | phosphorylates | ADP + phosphate to ATP | **Core** | Feng 2023 | PMF “drives ATP synthesis via F0F1-ATPase” | Use GO:0015986; biochemical stoichiometry should not be asserted without system-specific data. (feng2023isproteorhodopsina pages 17-23) |
| β-carotene | is cleaved by | Blh β-carotene 15,15′-dioxygenase | **Core-supporting module** | González et al. 2008; Kim et al. 2009 | PR genomes contain “genes for synthesis of the…chromophore retinal (`crtEBIY`, `blh`)” | The enzyme-level edge is well established, but the retrieved direct snippet primarily supports pathway/genome association. Retain DOI:10.1074/jbc.M109.002618 for biochemical validation. |
| Blh-mediated cleavage | produces | retinal | **Core-supporting module** | Kim et al. 2009 | recombinant Blh characterized as “β-carotene 15,15′-dioxygenase” | Curate when endogenous retinal synthesis is part of the organism-specific graph; otherwise model external retinal acquisition. |
| retinal | binds covalently to | conserved PR lysine | **Core** | Feng 2023 | retinal binding occurs through a “protonated Schiff base at lysine 230” | Numbering is taxon/protein-specific; curate the conserved function, not universal residue number 230. (feng2023isproteorhodopsina pages 17-23) |
| retinal supply | enables | functional PR proton pumping | **Core** | Dupont et al. 2012; Johnson et al. 2010 | “Proteorhodopsin requires retinol [retinal] for functionality” | Correct the source’s retinol/retinal terminology during curation; chromophore availability is a required condition. (dupont2012genomicinsightsto pages 8-9, johnson2010enhancementofsurvival pages 1-2) |
| PR-generated PMF | supports | substrate uptake | **Context** | Johnson et al. 2010 | “lactate consumption increased during illumination” | Direct in engineered *S. oneidensis*; do not generalize lactate specifically to marine PR organisms. (johnson2010enhancementofsurvival pages 1-2, johnson2010enhancementofsurvival pages 6-7) |
| PR-generated PMF | supports | flagellar rotation/motility | **Context** | Feng 2023 | PMF drives “flagella motility” | Mechanistically plausible and established for PMF, but phenotype depends on a flagellated host. (feng2023isproteorhodopsina pages 17-23) |
| PR activity under energy limitation | increases | survival/maintenance | **Context, strong** | Gómez-Consarnau et al. 2010; Johnson et al. 2010 | light-treated cells remained “2.5 times more abundant…after 10 days of starvation” | Strong but not universal; encode nutrient limitation and illumination as conditions. (feng2023isproteorhodopsina pages 34-38, johnson2010enhancementofsurvival pages 1-2) |
| PR activity under low carbon | increases | cell yield/growth in *Dokdonia* MED134 | **Taxon-specific** | summarized in Feng 2023; Gómez-Consarnau et al. 2007 | light: 3×10⁵ cells ml⁻¹; dark: 0.5×10⁵ cells ml⁻¹ | Quantitative but source chain is secondary here; verify against DOI:10.1038/nature05381 before YAML insertion. (feng2023isproteorhodopsina pages 34-38) |
| low-intensity illumination under salinity stress | increases | *P. torquis* growth | **Taxon/assay-specific** | Feng 2023 | growth rate increased 1.5-fold and abundance 2-fold at 3.7 μmol photons m⁻² s⁻¹ | Useful environmental branch, not a universal trait edge. High light was inhibitory. (feng2023isproteorhodopsina pages 89-95, feng2023isproteorhodopsina pages 95-101) |
| PR activity | increases | respiration/electrical current in engineered *S. oneidensis* | **Application-specific** | Johnson et al. 2010 | “increases electrical current generation during illumination” | Synthetic implementation, not part of the minimal natural-trait graph. (johnson2010enhancementofsurvival pages 1-2, johnson2010enhancementofsurvival pages 6-7) |
| PR color-tuning residue/environment | determines | blue- versus green-light absorption | **Context** | Béjà et al. 2001; Feng 2023 | absorption spans “blue (490 nm) to green (540 nm)” | The exact residue/state association must be curated per sequence; avoid a universal leucine/methionine rule without primary sequence evidence. (feng2023isproteorhodopsina pages 28-34) |
| myxol or zeaxanthin binding | transfers excitation energy to | PR retinal | **Uncertain/recent** | Fujiwara et al. 2024 preprint | efficiencies were approximately 9% for myxol and 22% for zeaxanthin | Taxon-restricted and preprint evidence; not required for canonical PR phototrophy. (fujiwara2024carotenoidpigmentsenhance pages 9-12) |
| carotenoid antenna binding | accelerates | PR photocycle / broadens light harvesting | **Uncertain/recent** | Fujiwara et al. 2024 preprint | carotenoid binding “accelerat[ed] the photocycle” and expanded blue–green harvesting | Restrict to supported Bacteroidota PRs; transferred excitation did not enhance retinal isomerization in every tested complex. (fujiwara2024carotenoidpigmentsenhance pages 9-12) |

## Recent research and quantitative ecological evidence

### 2023: conditional stress physiology

Feng’s 2023 thesis provides a detailed culture-based analysis of *Psychroflexus torquis*. Under nutrient-rich conditions and low illumination, growth rate and cell abundance rose approximately **1.5-fold and 2-fold**, respectively, relative to darkness; proton pumping was greatest at **52.5 g L⁻¹ salinity** and **27.7 μmol photons m⁻² s⁻¹**, while the largest growth benefit occurred at only **3.7 μmol photons m⁻² s⁻¹**. PR represented approximately **0.4% of identified peptides**. These results favor a role in osmotic/cold stress adaptation but also show that protein abundance, pumping, and growth are not interchangeable phenotypes. (feng2023isproteorhodopsina pages 89-95, feng2023isproteorhodopsina pages 95-101, feng2023isproteorhodopsina pages 131-136)

Important null results accompanied the positive findings: PR transcription remained relatively constant across tested light/salinity treatments, elevated PR protein did not consistently predict growth, nutrient stress produced no growth benefit in that system, and higher illumination became inhibitory. The authoritative interpretation is therefore **conditional energy supplementation**, not an unconditional light-growth relation. (feng2023isproteorhodopsina pages 131-136, feng2023isproteorhodopsina pages 95-101)

### 2024: physiological limits and accessory light harvesting

In *Candidatus Puniceispirillum marinum* IMCC1322, ATP concentrations across light regimes and stationary/death phases ranged from **0.0331 to 1.74 mM**, equivalent to **13.9–367 zeptomoles ATP cell⁻¹**. Yet PR-dependent energy was judged insufficient to sustain protein turnover after logarithmic growth, and stable-isotope measurements detected no significant constant-light versus constant-dark difference in inorganic-carbon assimilation. This is strong evidence against curating “PR causes autotrophic carbon fixation” as a general edge.

A November 2024 bioRxiv preprint reported carotenoid antennae associated with some marine rhodopsins. Myxol and zeaxanthin transferred excitation to retinal at approximately **9% and 22% efficiency**, respectively, and carotenoid binding accelerated the PR photocycle. Tara Oceans transcripts placed supported Bacteroidota PRs through approximately **0–200 m** of the photic zone. Because this work was a preprint and the effect was taxon-specific—with no enhanced retinal isomerization in one tested NM-R3 complex—it should remain an optional, uncertain branch. (fujiwara2024carotenoidpigmentsenhance pages 9-12)

### Field prevalence

West Antarctic Peninsula surveys estimated PR-bearing bacteria at mean community fractions of **17%, 3.5%, and 29.7%** in 2014, 2016, and 2017, respectively. Bacteroidetes/Flavobacteriia comprised approximately **55–70%** of assigned PR sequences and Alphaproteobacteria approximately **17–25%** in analyzed samples. Green-absorbing PR genes were more abundant, but blue-absorbing variants accounted for **more than 50% of transcripts**, emphasizing that gene abundance and activity can differ. (cifuentesanticevic2021proteorhodopsinphototrophyin pages 2-3, cifuentesanticevic2021proteorhodopsinphototrophyin pages 5-6)

Broader summaries report more than **4,000 PR sequences across 41 marine environments** and estimates that PR-bearing organisms comprise **13–70%** of bacterioplankton in several well-studied seas. These are useful context statistics but should not become causal edges. (feng2023isproteorhodopsina pages 17-23, feng2023isproteorhodopsina pages 95-101)

## Current applications and real-world implementations

1. **Synthetic bioenergetics and microbial electrosynthesis.** Functional PR expression in *S. oneidensis* MR-1 increased illuminated lactate uptake, respiration/current production, and survival under nutrient limitation. This demonstrates a real engineered system in which light-derived PMF augments metabolism and electricity generation. It did not universally increase growth in nutrient-rich culture. (johnson2010enhancementofsurvival pages 1-2, johnson2010enhancementofsurvival pages 6-7)
2. **Optogenetic metabolic control.** PR and related outward proton pumps provide a compact, single-protein route to manipulate PMF, ATP availability, substrate transport, and production metabolism. Retinal supply and membrane orientation remain engineering constraints.
3. **Marine ecosystem energetics.** PR-bearing bacteria are widespread and transcriptionally active in sunlit marine waters, including Antarctic coastal systems, suggesting a major non-chlorophyll route by which sunlight enters microbial energy budgets. Community prevalence alone, however, does not quantify ATP production or carbon-cycle flux. (cifuentesanticevic2021proteorhodopsinphototrophyin pages 2-3, cifuentesanticevic2021proteorhodopsinphototrophyin pages 5-6)
4. **Stress-resilient microbial platforms.** Conditional benefits during starvation, salinity stress, and impaired respiration suggest applications in low-nutrient bioprocesses, but effects are strain- and irradiance-dependent. (feng2023isproteorhodopsina pages 131-136, feng2023isproteorhodopsina pages 95-101, feng2023isproteorhodopsina pages 34-38)

## Recommended initial YAML graph

The most defensible minimal graph is:

`photon → retinal-bound proteorhodopsin activation → outward H+ transport → proton-motive force → F-type ATP synthase activity → ATP production`

Add a required enabling branch:

`carotenoid pathway → β-carotene → Blh cleavage → retinal → retinal–PR Schiff-base holoprotein`

Add growth, survival, transport, motility, carbon-assimilation, carotenoid-antenna, or electricity branches only with explicit taxon and condition qualifiers. The eight-node/seven-edge existing summary is therefore mechanistically appropriate if it centers on the minimal chain rather than treating all ecological outcomes as constitutive.

## Warnings: claims not yet suitable for unconditional curation

- **Do not infer the trait from a PR-like gene alone.** Pump direction, ion specificity, expression, membrane insertion, and retinal availability must be established.
- **Do not curate PR → autotrophic carbon fixation.** PR supplies energy, not reducing equivalents or a carbon-fixation pathway; recent culture evidence found no light-dependent increase in inorganic-carbon assimilation.
- **Do not make light → increased growth a core edge.** Benefits may occur only under carbon limitation, starvation, osmotic stress, suitable inoculum/nutrient states, or low irradiance; many strains show no growth response. (feng2023isproteorhodopsina pages 95-101, feng2023isproteorhodopsina pages 131-136)
- **Do not generalize exact spectral-residue rules across all PRs** without a sequence-specific source.
- **Do not universalize carotenoid antennae.** The 2024 evidence is preprint-level, Bacteroidota-enriched, and complex-dependent. (fujiwara2024carotenoidpigmentsenhance pages 9-12)
- **Do not curate salinity homeostasis as proven.** In *P. torquis*, sodium/osmotic regulation is a mechanistic hypothesis rather than a directly resolved causal pathway. (feng2023isproteorhodopsina pages 95-101)
- **Treat field metagenomic abundance as ecological association, not functional flux.** Transcription, pumping rate, ATP production, and growth were not directly measured in the Antarctic abundance survey. (cifuentesanticevic2021proteorhodopsinphototrophyin pages 2-3, cifuentesanticevic2021proteorhodopsinphototrophyin pages 5-6)
- **Retinol/retinal terminology requires normalization.** Proteorhodopsin’s chromophore is retinal; occasional source wording describing a requirement for “retinol” should not be copied literally into the graph. (dupont2012genomicinsightsto pages 8-9)

## DOI-first bibliography

1. Béjà O, et al. **Bacterial rhodopsin: evidence for a new type of phototrophy in the sea.** *Science*. Published 15 September 2000. DOI: [10.1126/science.289.5486.1902](https://doi.org/10.1126/science.289.5486.1902).
2. Béjà O, et al. **Proteorhodopsin phototrophy in the ocean.** *Nature*. Published June 2001. DOI: [10.1038/35081051](https://doi.org/10.1038/35081051).
3. Gómez-Consarnau L, et al. **Light stimulates growth of proteorhodopsin-containing marine Flavobacteria.** *Nature*. Published January 2007. DOI: [10.1038/nature05381](https://doi.org/10.1038/nature05381).
4. González JM, et al. **Genome analysis of the proteorhodopsin-containing marine bacterium Polaribacter sp. MED152.** *PNAS*. Published June 2008. DOI: [10.1073/pnas.0712027105](https://doi.org/10.1073/pnas.0712027105).
5. Kim Y-S, et al. **In vitro characterization of recombinant Blh as a β-carotene 15,15′-dioxygenase.** *Journal of Biological Chemistry*. Published June 2009. DOI: [10.1074/jbc.M109.002618](https://doi.org/10.1074/jbc.M109.002618).
6. Johnson ET, et al. **Enhancement of survival and electricity production in an engineered bacterium by light-driven proton pumping.** *Applied and Environmental Microbiology*. Published July 2010. DOI: [10.1128/AEM.02425-09](https://doi.org/10.1128/AEM.02425-09). (johnson2010enhancementofsurvival pages 1-2)
7. Dupont CL, et al. **Genomic insights to SAR86, an abundant and uncultivated marine bacterial lineage.** *ISME Journal*. Published 2012. DOI: [10.1038/ismej.2011.189](https://doi.org/10.1038/ismej.2011.189). (dupont2012genomicinsightsto pages 8-9)
8. Cifuentes-Anticevic J, et al. **Proteorhodopsin phototrophy in Antarctic coastal waters.** *mSphere*. Published August 2021. DOI: [10.1128/mSphere.00525-21](https://doi.org/10.1128/mSphere.00525-21). (cifuentesanticevic2021proteorhodopsinphototrophyin pages 2-3, cifuentesanticevic2021proteorhodopsinphototrophyin pages 5-6)
9. Tu W, Huang WE. **Rhodopsin-driven microbial CO₂ fixation using synthetic biology design.** *Environmental Microbiology*. Published online October 2022. DOI: [10.1111/1462-2920.16243](https://doi.org/10.1111/1462-2920.16243).
10. Feng S. **Is proteorhodopsin a general light-driven stress adaptation system for survival in cold environments?** University of Tasmania thesis. Published January 2023. DOI: [10.25959/23241740](https://doi.org/10.25959/23241740). (feng2023isproteorhodopsina pages 89-95, feng2023isproteorhodopsina pages 131-136, feng2023isproteorhodopsina pages 17-23)
11. Oh H-M, et al. **Effect of light regime on Candidatus Puniceispirillum marinum IMCC1322 in nutrient-replete conditions.** *Journal of Microbiology and Biotechnology*. Published November 2024. DOI: [10.4014/jmb.2410.10034](https://doi.org/10.4014/jmb.2410.10034).
12. Fujiwara T, et al. **Carotenoid pigments enhance rhodopsin-mediated phototrophy by light-harvesting and photocycle-accelerating.** bioRxiv preprint. Published November 2024. DOI: [10.1101/2024.11.08.622755](https://doi.org/10.1101/2024.11.08.622755). (fujiwara2024carotenoidpigmentsenhance pages 9-12)

Overall, the evidence strongly supports curating the retinal-dependent outward-proton-pump/PMF/ATP chain for **`traitmech:000036`**. Ecological outcomes should be modeled as conditional downstream branches rather than defining components of the trait.

References

1. (feng2023isproteorhodopsina pages 17-23): Shi Feng. Is proteorhodopsin a general light-driven stress adaptation system for survival in cold environments. Text, Jan 2023. URL: https://doi.org/10.25959/23241740, doi:10.25959/23241740. This article has 0 citations and is from a peer-reviewed journal.

2. (dupont2012genomicinsightsto pages 8-9): Chris L Dupont, Douglas B Rusch, Shibu Yooseph, Mary-Jane Lombardo, R Alexander Richter, Ruben Valas, Mark Novotny, Joyclyn Yee-Greenbaum, Jeremy D Selengut, Dan H Haft, Aaron L Halpern, Roger S Lasken, Kenneth Nealson, Robert Friedman, and J Craig Venter. Genomic insights to sar86, an abundant and uncultivated marine bacterial lineage. The ISME Journal, 6:1186-1199, Dec 2012. URL: https://doi.org/10.1038/ismej.2011.189, doi:10.1038/ismej.2011.189. This article has 575 citations.

3. (needham2019adistinctlineage pages 10-10): David M. Needham, Susumu Yoshizawa, Toshiaki Hosaka, Camille Poirier, Chang Jae Choi, Elisabeth Hehenberger, Nicholas A. T. Irwin, Susanne Wilken, Cheuk-Man Yung, Charles Bachy, Rika Kurihara, Yu Nakajima, Keiichi Kojima, Tomomi Kimura-Someya, Guy Leonard, Rex R. Malmstrom, Daniel R. Mende, Daniel K. Olson, Yuki Sudo, Sebastian Sudek, Thomas A. Richards, Edward F. DeLong, Patrick J. Keeling, Alyson E. Santoro, Mikako Shirouzu, Wataru Iwasaki, and Alexandra Z. Worden. A distinct lineage of giant viruses brings a rhodopsin photosystem to unicellular marine predators. Proceedings of the National Academy of Sciences of the United States of America, 116:20574-20583, Sep 2019. URL: https://doi.org/10.1073/pnas.1907517116, doi:10.1073/pnas.1907517116. This article has 179 citations and is from a highest quality peer-reviewed journal.

4. (feng2023isproteorhodopsina pages 28-34): Shi Feng. Is proteorhodopsin a general light-driven stress adaptation system for survival in cold environments. Text, Jan 2023. URL: https://doi.org/10.25959/23241740, doi:10.25959/23241740. This article has 0 citations and is from a peer-reviewed journal.

5. (johnson2010enhancementofsurvival pages 1-2): Ethan T. Johnson, Daniel B. Baron, Belén Naranjo, Daniel R. Bond, Claudia Schmidt-Dannert, and Jeffrey A. Gralnick. Enhancement of survival and electricity production in an engineered bacterium by light-driven proton pumping. Applied and Environmental Microbiology, 76:4123-4129, Jul 2010. URL: https://doi.org/10.1128/aem.02425-09, doi:10.1128/aem.02425-09. This article has 97 citations and is from a peer-reviewed journal.

6. (feng2023isproteorhodopsina pages 89-95): Shi Feng. Is proteorhodopsin a general light-driven stress adaptation system for survival in cold environments. Text, Jan 2023. URL: https://doi.org/10.25959/23241740, doi:10.25959/23241740. This article has 0 citations and is from a peer-reviewed journal.

7. (bukhdruker2025proteorhodopsininsightsinto pages 18-19): Sergey Bukhdruker, Ivan Gushchin, Vitaly Shevchenko, Kirill Kovalev, Vitaly Polovinkin, Fedor Tsybrov, Roman Astashkin, Alexey Alekseev, Anatoly Mikhaylov, Siarhei Bukhalovich, Dmitry Bratanov, Yury Ryzhykau, Daria Kuklina, Nicolas Caramello, Tatyana Rokitskaya, Yuri Antonenko, Maksim Rulev, Chavdar Stoev, Dmitrii Zabelskii, Ekaterina Round, Andrey Rogachev, Valentin Borshchevskiy, Rohit Ghai, Gleb Bourenkov, Mahel Zeghouf, Jacqueline Cherfils, Martin Engelhard, Igor Chizhov, Francisco Rodriguez-Valera, Ernst Bamberg, and Valentin Gordeliy. Proteorhodopsin insights into the molecular mechanism of vectorial proton transport. Apr 2025. URL: https://doi.org/10.1126/sciadv.adu5303, doi:10.1126/sciadv.adu5303. This article has 9 citations and is from a highest quality peer-reviewed journal.

8. (feng2023isproteorhodopsina pages 34-38): Shi Feng. Is proteorhodopsin a general light-driven stress adaptation system for survival in cold environments. Text, Jan 2023. URL: https://doi.org/10.25959/23241740, doi:10.25959/23241740. This article has 0 citations and is from a peer-reviewed journal.

9. (cifuentesanticevic2021proteorhodopsinphototrophyin pages 2-3): Jerónimo Cifuentes-Anticevic, María E. Alcamán-Arias, Tomás Alarcón-Schumacher, Javier Tamayo-Leiva, Carlos Pedrós-Alió, Laura Farías, and Beatriz Díez. Proteorhodopsin phototrophy in antarctic coastal waters. Aug 2021. URL: https://doi.org/10.1128/msphere.00525-21, doi:10.1128/msphere.00525-21. This article has 5 citations and is from a peer-reviewed journal.

10. (cifuentesanticevic2021proteorhodopsinphototrophyin pages 5-6): Jerónimo Cifuentes-Anticevic, María E. Alcamán-Arias, Tomás Alarcón-Schumacher, Javier Tamayo-Leiva, Carlos Pedrós-Alió, Laura Farías, and Beatriz Díez. Proteorhodopsin phototrophy in antarctic coastal waters. Aug 2021. URL: https://doi.org/10.1128/msphere.00525-21, doi:10.1128/msphere.00525-21. This article has 5 citations and is from a peer-reviewed journal.

11. (johnson2010enhancementofsurvival pages 6-7): Ethan T. Johnson, Daniel B. Baron, Belén Naranjo, Daniel R. Bond, Claudia Schmidt-Dannert, and Jeffrey A. Gralnick. Enhancement of survival and electricity production in an engineered bacterium by light-driven proton pumping. Applied and Environmental Microbiology, 76:4123-4129, Jul 2010. URL: https://doi.org/10.1128/aem.02425-09, doi:10.1128/aem.02425-09. This article has 97 citations and is from a peer-reviewed journal.

12. (feng2023isproteorhodopsina pages 95-101): Shi Feng. Is proteorhodopsin a general light-driven stress adaptation system for survival in cold environments. Text, Jan 2023. URL: https://doi.org/10.25959/23241740, doi:10.25959/23241740. This article has 0 citations and is from a peer-reviewed journal.

13. (fujiwara2024carotenoidpigmentsenhance pages 9-12): Takayoshi Fujiwara, Toshiaki Hosaka, Masumi Hasegawa-Takano, Yosuke Nishimura, Kento Tominaga, Kaho Mori, Satoshi Nishino, Yuno Takahashi, Tomomi Uchikubo-Kamo, Kazuharu Hanada, Takashi Maoka, Shinichi Takaichi, Keiichi Inoue, Mikako Shirouzu, and Susumu Yoshizawa. Carotenoid pigments enhance rhodopsin-mediated phototrophy by light-harvesting and photocycle-accelerating. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.08.622755, doi:10.1101/2024.11.08.622755. This article has 1 citations.

14. (feng2023isproteorhodopsina pages 131-136): Shi Feng. Is proteorhodopsin a general light-driven stress adaptation system for survival in cold environments. Text, Jan 2023. URL: https://doi.org/10.25959/23241740, doi:10.25959/23241740. This article has 0 citations and is from a peer-reviewed journal.