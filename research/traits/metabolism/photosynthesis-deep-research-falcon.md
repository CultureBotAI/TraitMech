---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:43:18.102863'
end_time: '2026-08-04T06:51:28.388030'
duration_seconds: 490.29
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: photosynthesis
  trait_identifier: traitmech:000038
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: photosynthesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phototrophic metabolism that uses light energy and chlorophyll- or
    bacteriochlorophyll-based photochemical reaction centers to drive electron flow,
    fixing CO2 and/or generating reducing power. Subdivided into oxygenic and anoxygenic
    photosynthesis.
  parent_traits: traitmech:000037
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard treat prokaryotic
    photosynthesis (reaction-center based) as encompassing both oxygenic and anoxygenic
    forms across five phyla.) | DOI:10.1146/annurev-earth-060313-054810:  (Fischer
    et al., "Evolution of Oxygenic Photosynthesis", supports reaction-center photosynthesis
    as the chlorophyll-based, CO2-fixing branch of phototrophy distinct from rhodopsin-based
    light capture.)'
  causal_graph_summary: 'photosynthesis_chlorophyll_reaction_center: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photosynthesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000038
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy and chlorophyll- or bacteriochlorophyll-based photochemical reaction centers to drive electron flow, fixing CO2 and/or generating reducing power. Subdivided into oxygenic and anoxygenic photosynthesis.
- **Parent traits:** traitmech:000037
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard treat prokaryotic photosynthesis (reaction-center based) as encompassing both oxygenic and anoxygenic forms across five phyla.) | DOI:10.1146/annurev-earth-060313-054810:  (Fischer et al., "Evolution of Oxygenic Photosynthesis", supports reaction-center photosynthesis as the chlorophyll-based, CO2-fixing branch of phototrophy distinct from rhodopsin-based light capture.)
- **Existing causal graph summary:** photosynthesis_chlorophyll_reaction_center: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/photosynthesis.yaml`.

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
- **Trait label:** photosynthesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000038
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy and chlorophyll- or bacteriochlorophyll-based photochemical reaction centers to drive electron flow, fixing CO2 and/or generating reducing power. Subdivided into oxygenic and anoxygenic photosynthesis.
- **Parent traits:** traitmech:000037
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard treat prokaryotic photosynthesis (reaction-center based) as encompassing both oxygenic and anoxygenic forms across five phyla.) | DOI:10.1146/annurev-earth-060313-054810:  (Fischer et al., "Evolution of Oxygenic Photosynthesis", supports reaction-center photosynthesis as the chlorophyll-based, CO2-fixing branch of phototrophy distinct from rhodopsin-based light capture.)
- **Existing causal graph summary:** photosynthesis_chlorophyll_reaction_center: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/photosynthesis.yaml`.

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


# Curation report: microbial photosynthesis (`traitmech:000038`)

## Executive scope

**Recommended interpretation.** `traitmech:000038` should represent the cellular capacity for **chlorophyll- or bacteriochlorophyll-based reaction-center photochemistry**: antenna pigments absorb light, excitation reaches a type I or type II reaction center, charge separation initiates electron transport, and membrane bioenergetics produces reducing power and/or ATP. It encompasses **oxygenic photosynthesis** and **anoxygenic photosynthesis**, including photoautotrophic and photoheterotrophic implementations. Type I and type II reaction centers occur in multiple bacterial lineages, whereas cyanobacteria couple heterodimeric PSI and PSII for oxygenic photosynthesis. (martin2018aphysiologicalperspective pages 2-3)

**Important separation of modules.** Photosynthesis supplies photochemical energy and electrons, but it does not necessarily imply CO2 fixation. Aerobic anoxygenic phototrophs can be photoheterotrophs, while carbon-fixing phototrophs use lineage-dependent pathways, including the Calvin–Benson–Bassham (CBB) or reverse TCA cycles. Green sulfur bacteria, for example, assimilate CO2 through reverse TCA, whereas oxygenic phototrophs commonly use CBB. (tomasch2024aphotoheterotrophicbacterium pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 1-2, li2021exogenouselectricityflowing pages 1-6)

### Boundary cases

Include:

- Cyanobacterial oxygenic photosynthesis using PSII and PSI.
- Anoxygenic reaction-center phototrophy driven by bacteriochlorophyll.
- Cyclic anoxygenic electron transport that generates proton motive force and ATP even when carbon fixation is absent.
- Photoheterotrophic reaction-center activity.

Exclude or model separately:

- **Rhodopsin-based phototrophy**, because it uses retinal proton/ion pumps rather than chlorophyll reaction centers and charge-separated electron-transfer chains.
- Chlorophyll or bacteriochlorophyll biosynthesis alone; pigment production is neither sufficient evidence of an assembled functional reaction center nor of photosynthetic growth.
- CO2 fixation alone, which can be chemolithoautotrophic.
- Phototaxis, fluorescence, light sensing, or photoprotection without reaction-center electron transport.
- Artificial illumination and exogenous-electron inputs as defining components of the natural trait; these are experimental modifiers.

A practical positive assay should demonstrate at least one of: light-dependent reaction-center charge separation/electron transport, oxygen evolution, photophosphorylation, light-dependent growth dependent on a reaction center, or a functional reaction-center spectroscopic signature. Genomic photosynthesis-gene clusters are useful predictions but should remain genotype-level evidence until function is shown.

## Candidate graph architecture

A single linear graph would incorrectly imply that all phototrophs use PSII, water, oxygen evolution, PSI, and CBB. The YAML should therefore have a conserved upstream core followed by explicit **oxygenic** and **anoxygenic** branches:

1. light → antenna excitation → reaction-center excitation → charge separation;
2. oxygenic branch: PSII/water → quinone → cytochrome b6f → PSI → ferredoxin/NADPH, coupled to proton motive force and ATP synthesis;
3. anoxygenic branch: external donor and/or cyclic flow → type I or II reaction center → quinone/cytochrome or ferredoxin pathways → proton motive force/reducing power;
4. optional downstream carbon-fixation modules, linked conditionally rather than made definitional.

## Candidate nodes

### Trait and processes

- photosynthesis — `traitmech:000038`
- parent trait — `traitmech:000037`
- photosynthesis — `GO:0015979`
- light reaction of photosynthesis — `GO:0019684`
- photosynthetic electron transport chain — label candidate; verify the desired GO child term for each branch
- photosynthetic electron transport in photosystem II — `GO:0009772`
- photosynthetic electron transport in photosystem I — `GO:0009773`
- carbon fixation — `GO:0015977`
- Calvin–Benson–Bassham cycle — label candidate
- reverse tricarboxylic-acid cycle — label candidate
- cyclic photosynthetic electron transport — label candidate
- oxygenic photosynthesis; anoxygenic photosynthesis — retain as branch labels unless project-approved ontology terms are confirmed

### Complexes, proteins, and cofactors

- photosystem II; photosystem I
- PSII oxygen-evolving complex / Mn4CaO5 cluster
- P680; D1 protein/PsbA; D2/PsbD; redox-active TyrZ (D1-Y161)
- QA and QB plastoquinone sites
- cytochrome b6f complex
- plastocyanin; cytochrome c6
- P700; PsaA/PsaB core; PSI [4Fe–4S] clusters
- ferredoxin; ferredoxin–NADP+ reductase
- F-type ATP synthase
- type I anoxygenic reaction center; type II anoxygenic reaction center
- light-harvesting complexes LH1/LH2
- chlorosome; Fenna–Matthews–Olson protein
- sulfide:quinone oxidoreductase (SQR)
- flavocytochrome-c sulfide dehydrogenase (FccAB)
- SoxYZ/Sox system
- bacteriochlorophyll; chlorophyll a; carotenoids
- PpsR redox-responsive transcriptional regulator

For protein-complex and gene nodes, taxon-specific UniProt accessions should be added only when the YAML names an organism or strain; generic accessions would falsely imply orthology and subunit conservation.

### Chemicals

Confident candidates include water (`CHEBI:15377`), dioxygen (`CHEBI:15379`), carbon dioxide (`CHEBI:16526`), hydrogen sulfide (`CHEBI:16136`), molecular hydrogen (`CHEBI:18276`), ferrous ion (`CHEBI:29033`), ATP (`CHEBI:15422`), NADPH (`CHEBI:16474`), and elemental sulfur (`CHEBI:33403`). Additional useful labels are photon/light, proton, plastoquinone, plastoquinol, NADP+, reduced/oxidized ferredoxin, pyrite (FeS2), reactive oxygen species, acetate, and ethylene. Exact CHEBI identifiers for the latter compounds should be registry-validated during ingestion rather than inferred here.

### Structures and localization

- thylakoid membrane — `GO:0009579`
- photosynthetic membrane
- cytoplasmic/intracytoplasmic membrane
- chromatophore
- chlorosome
- thylakoid lumen
- periplasm

Chlorosomes are not universal anoxygenic structures: they occur in selected type-I-reaction-center lineages. Purple sulfur bacteria instead have intracytoplasmic membrane systems and LH1/LH2 antennae. (kushkevych2021anoxygenicphotosynthesisin pages 2-3, kushkevych2021anoxygenicphotosynthesisin pages 3-5, martin2018aphysiologicalperspective pages 2-3)

### Taxa and environmental/experimental factors

- Cyanobacteria — `NCBITaxon:1117`
- green sulfur bacteria/Chlorobiaceae; purple sulfur bacteria/Chromatiaceae
- aerobic anoxygenic phototrophic bacteria
- *Allochromatium vinosum* DSM 180
- *Sediminicoccus* sp. KRV36
- *Thermosynechococcus vulcanus*
- light intensity, wavelength, and photoperiod
- oxygen availability/redox state
- anoxia and sulfide abundance
- availability of copper versus iron, affecting plastocyanin versus cytochrome-c6 usage
- temperature, salinity, far-red light, and nutrient availability
- inhibitors or perturbations: PSII inhibition/deletion, intermittent illumination, and exogenous cathodic electrons

## Candidate causal edges

The compact table below lists the strongest initial edges. It should be treated as a starting graph rather than a claim that every edge occurs in every phototroph.

| branch | subject | predicate | object | evidence DOI/date | certainty/qualifier |
|---|---|---|---|---|---|
| oxygenic | Photosystem II (PSII) | oxidizes | water, releasing O2 and protons | 10.1038/s41586-023-06987-5 (2024-01-31) (li2024oxygenevolvingphotosystemii pages 1-2) | High; primary structural study in thermophilic cyanobacterial PSII |
| oxygenic | Photosystem II (PSII) | reduces | plastoquinone (PQ) | 10.3390/ijms25168767 (2024-08-12) (tian2024photosystemia pages 1-2) | High; review statement for oxygen-evolving photosynthetic microorganisms |
| oxygenic | Plastoquinol (PQH2) | transfers electrons to / contributes to pmf via | cytochrome b6f complex | 10.3390/plants13152103 (2024-07) (milrad2024regulationofmicroalgal pages 1-3) | High; review-level mechanism, broadly applicable to oxygenic phototrophs |
| oxygenic | Cytochrome b6f complex | passes electrons via plastocyanin or cytochrome c6 to | Photosystem I (PSI) | 10.3390/plants13152103 (2024-07) (milrad2024regulationofmicroalgal pages 1-3) | High; metal cofactor availability can determine Pc vs Cyt c6 usage |
| oxygenic | Photosystem I (PSI) | reduces | ferredoxin | 10.3390/ijms25168767 (2024-08-12) (tian2024photosystemia pages 1-2) | High; conserved PSI core chemistry in cyanobacteria/algae |
| oxygenic | Reduced ferredoxin / NADPH | provides reducing power for | CO2 fixation via Calvin-Benson-Bassham cycle | 10.1039/d1ee01526e (2021-09) (li2021exogenouselectricityflowing pages 1-6) | High for oxygenic cyanobacterial context; wording links PSI output to CBB |
| anoxygenic | Chlorosome / antenna pigments | transfers excitation energy to | reaction center | 10.3390/antiox10060829 (2021-05) (kushkevych2021anoxygenicphotosynthesisin pages 2-3, kushkevych2021anoxygenicphotosynthesisin pages 3-5) | High for green sulfur bacteria; chlorosome-specific, not universal across anoxygenic taxa |
| anoxygenic | Hydrogen sulfide (H2S) | is oxidized by | sulfide:quinone oxidoreductase (SQR) | 10.3390/antiox10060829 (2021-05) (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | High for sulfur phototrophs |
| anoxygenic | Sulfide:quinone oxidoreductase (SQR) | feeds electrons into | quinone-cytochrome photosynthetic electron flux | 10.3390/antiox10060829 (2021-05) (kushkevych2021anoxygenicphotosynthesisin pages 3-5) | High for sulfur phototrophs |
| anoxygenic | Cyclic photosynthetic electron transport | generates | proton motive force and ATP synthesis | 10.3390/antiox10060829 (2021-05) (kushkevych2021anoxygenicphotosynthesisin pages 2-3) | Moderate-High; general anoxygenic mechanism, taxon-specific architecture varies |
| anoxygenic | Pyrite (FeS2) | supports electron transfer for | autotrophic growth in Allochromatium vinosum | 10.1128/aem.00863-24 (2024-07) (alarcon2024evidenceforautotrophic pages 1-2) | Moderate; strong organism-specific evidence, not yet generalizable to all phototrophs |
| anoxygenic | Membrane-bound carotenoids and oxidative stress response genes | protect / safeguard | bacteriochlorophyll synthesis and photosystem assembly under oxic continuous light | 10.1128/msystems.01311-23 (2024-02-20) (tomasch2024aphotoheterotrophicbacterium pages 1-2) | Moderate; strong for Sediminicoccus sp. KRV36, likely niche-specific adaptation |
| scope boundary | Chlorophyll/bacteriochlorophyll reaction-center photochemistry | defines | microbial photosynthesis trait scope | 10.1093/femsre/fux056 (2018-11) (martin2018aphysiologicalperspective pages 2-3) | High; foundational scope support for RC1/RC2-based chlorophototrophy |


*Table: This table summarizes the strongest curation-ready causal edges for microbial reaction-center photosynthesis across oxygenic and anoxygenic branches. It highlights which edges are broadly conserved versus taxon- or condition-specific, helping prioritize TraitMech curation.*

### Expanded evidence table

| Proposed subject–predicate–object | Supporting snippet | Reference | Curation note |
|---|---|---|---|
| light excitation of P680 **causes** PSII charge separation | “light-driven excitation of P680” is followed by rapid charge separation producing P680•+/Pheo•− | Li et al.; published 31 Jan 2024; DOI: https://doi.org/10.1038/s41586-023-06987-5 | **High confidence; oxygenic branch.** Primary time-resolved structural work on cyanobacterial PSII. (li2024oxygenevolvingphotosystemii pages 1-2) |
| PSII oxygen-evolving complex **oxidizes** water **producing** O2 and protons | “PSII produces dioxygen by extracting electrons and protons from water”; oxidation occurs through the Mn4CaO5 S-state cycle | Same as above | **High confidence.** Do not generalize to anoxygenic phototrophs. (li2024oxygenevolvingphotosystemii pages 1-2) |
| PSII charge separation **transfers electrons to** QA and QB plastoquinones | “The electron is transferred from Pheo•− to the primary and secondary plastoquinones QA and QB” | Same as above | **High confidence.** Supports explicit Pheo→QA→QB edges if this granularity is desired. (li2024oxygenevolvingphotosystemii pages 1-2) |
| PSII water oxidation **reduces** PQ to PQH2 | PSII water oxidation “releases electrons that reduce plastoquinone (PQ) to plastoquinol (PQH2) at the QB site” | Milrad et al.; Jul 2024; DOI: https://doi.org/10.3390/plants13152103 | **High confidence; review evidence.** (milrad2024regulationofmicroalgal pages 1-3) |
| PQH2 **reduces** cytochrome b6f and **increases** proton motive force | “PQH2 diffuses in the thylakoid membrane to reduce the cytochrome b6f complex, increasing proton motive force” | Same as above | **High confidence.** A separate pmf→ATP-synthase edge is mechanistically appropriate, but a direct quotation for it was not recovered from the reviewed pages. (milrad2024regulationofmicroalgal pages 1-3) |
| cytochrome b6f **transfers electrons through** plastocyanin or cytochrome c6 **to** PSI | Electron transfer from Cytb6f to PSI is mediated by Pc or Cytc6; their expression depends on metal availability | Same as above | **High confidence.** Add copper/iron availability as regulatory context, not a universal deterministic edge. (milrad2024regulationofmicroalgal pages 1-3) |
| PSI antenna absorption **causes** P700 excitation and charge separation | Energy absorbed by antenna pigments is transferred to the core and “trapped at P700…where charge separation happens” | Tian & Chen; published 12 Aug 2024; DOI: https://doi.org/10.3390/ijms25168767 | **High confidence; oxygenic PSI.** (tian2024photosystemia pages 1-2) |
| PSI **reduces** ferredoxin | Electrons move through chlorophyll, phylloquinone, and [4Fe–4S] cofactors to terminal acceptor Fd | Same as above | **High confidence.** The review describes a conserved PsaA/PsaB core with flexible peripheral antenna/subunit architecture. (tian2024photosystemia pages 1-2) |
| plastocyanin/cytochrome donor **reduces** oxidized P700+ | “P700+ is replenished with an electron from…either a plastocyanin or a cytochrome” | Same as above | **High confidence.** (tian2024photosystemia pages 1-2) |
| PSI-derived reduced ferredoxin/NADPH **supports** CBB carbon fixation | PSI excitation initiates electron transfer to Fd and NADPH, which energizes CO2-fixing pathways such as CBB | Li et al.; Sep 2021; DOI: https://doi.org/10.1039/D1EE01526E | **High confidence for cyanobacteria; carbon fixation is downstream, not definitional.** (li2021exogenouselectricityflowing pages 1-6) |
| chlorosome **collects light and transfers excitation through** FMO **to** type-I reaction center | Chlorosomes contain about 200,000 BChl molecules; excitation is transferred via FMO to reaction centers averaging about 500 BChl molecules | Kushkevych et al.; May 2021; DOI: https://doi.org/10.3390/antiox10060829 | **High confidence but GSB-specific.** Reported chlorosome absorption maxima are 720–750 nm. (kushkevych2021anoxygenicphotosynthesisin pages 2-3, kushkevych2021anoxygenicphotosynthesisin pages 3-5) |
| H2S **is oxidized by** SQR, which **feeds electrons into** quinone–cytochrome photosynthetic flux | “SQR catalyzes H2S oxidation and provides electrons to photosynthetic electron flux via quinone-cytochrome complexes” | Same as above | **High confidence for sulfur phototrophs.** FccAB and Sox provide additional sulfur-oxidation routes whose exact graph connectivity is taxon-dependent. (kushkevych2021anoxygenicphotosynthesisin pages 3-5) |
| H2S **serves as electron donor for** anoxygenic photosynthesis, producing elemental sulfur in GSB | The 2024 review identifies H2S as the main donor and states that GSB oxidize it to elemental sulfur | Kushkevych et al.; published 11 Jul 2024; DOI: https://doi.org/10.3389/fmicb.2024.1417714 | **High confidence as a common sulfur-phototroph route, not universal.** H2 and reduced metal ions are alternatives. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| anoxygenic cyclic electron transport **generates** proton motive force **supporting** ATP synthesis | The reviewed sulfur-phototroph architecture is cyclic, lacks water oxidation/O2 evolution, and conserves energy through reaction-center electron transport | Kushkevych et al.; DOI: https://doi.org/10.3390/antiox10060829 | **Moderate–high.** Exact carriers differ between type-I and type-II systems; avoid one universal carrier chain. (kushkevych2021anoxygenicphotosynthesisin pages 2-3) |
| pyrite **supports** electron and sulfur supply for autotrophic growth of *A. vinosum* | Pyrite-supported cultures grew autotrophically; c- and b-type cytochrome genes were upregulated by as much as approximately 200-fold | Alarcon et al.; Jul 2024; DOI: https://doi.org/10.1128/AEM.00863-24 | **Uncertain/generalization prohibited.** Strong primary evidence for one strain and condition; do not curate pyrite as a universal donor. RC/LH genes were extensively downregulated, indicating complex source-dependent regulation. (alarcon2024evidenceforautotrophic pages 1-2) |
| continuous light plus O2 **promotes ROS risk**, while carotenoids and oxidative-stress responses **protect** BChl synthesis/assembly | KRV36 retained BChl synthesis; excess membrane carotenoids and constitutive oxidative-stress genes provided ROS-scavenging capacity | Tomasch et al.; published 20 Feb 2024; DOI: https://doi.org/10.1128/mSystems.01311-23 | **Taxon- and habitat-specific.** Cells contained 100–180 chromatophores; photosynthesis transcripts fell during the first 2 h of light but returned to initial levels by 24 h. (tomasch2024aphotoheterotrophicbacterium pages 1-2) |

## Recent developments and expert interpretation

### PSII water-oxidation mechanism

A major 2024 advance was nanosecond-to-millisecond pump–probe crystallography of *T. vulcanus* PSII. The study resolved coordinated electron/proton transfer and water delivery during S1→S2→S3 transitions. After two flashes, a water molecule appeared near D1-Glu189 and bound Ca2+ on a sub-microsecond timescale; its later disappearance coincided with growth of the O6 site, supporting it as the origin of O6 involved in O–O-bond formation. This provides unusually direct structural support for nodes representing the Mn4CaO5 cluster, D1-Glu189, TyrZ, substrate-water channels, proton release, and O2 formation. These details are mechanistically strong but may be too fine-grained for a ten-node trait-level graph. (li2024oxygenevolvingphotosystemii pages 1-2)

### PSI structural plasticity

Current structural synthesis portrays PSI as a conserved heterodimeric PsaA/PsaB photochemical core with flexible pigments, peripheral subunits, and antenna arrangements. Cyanobacterial PSI can occur as monomers, trimers, or tetramers, with cryo-EM revealing adaptations to fluctuating light, far-red light, iron deficiency, salinity, and other ecological constraints. Thus, “PSI reduces ferredoxin” is a stable core edge, whereas oligomeric state or particular antenna subunits should be taxon-qualified. (tian2024photosystemia pages 1-2)

### Environmental regulation of anoxygenic photosynthesis

The KRV36 study shows why oxygen and illumination should be modeled as contextual regulators rather than simple positive requirements. In many aerobic anoxygenic phototrophs, illuminated BChl intermediates generate ROS, and light suppresses pigment synthesis. KRV36 is an exception adapted to nearly continuous Arctic summer light: it maintained functional complexes, possessed 100–180 chromatophores per cell, and restored initially suppressed photosynthesis-gene expression within 24 h. This is compelling evidence for a protective carotenoid/oxidative-stress module but not for a universal anoxygenic mechanism. (tomasch2024aphotoheterotrophicbacterium pages 1-2)

### Expanding the donor repertoire

The 2024 *A. vinosum* study expands experimentally demonstrated solid electron sources to pyrite. Approximately 200-fold induction of several cytochrome genes, coupled with FccAB/SoxYZ induction and suppression of Dsr/Apr and RC/LH genes, suggests extracellular and periplasmic electron handling that differs substantially from soluble sulfide growth. The evidence supports a narrow “pyrite enables autotrophic growth in *A. vinosum* DSM 180” edge, not a generic “pyrite causes photosynthesis” assertion. (alarcon2024evidenceforautotrophic pages 1-2)

## Applications and real-world relevance

1. **H2S detoxification and sulfur recovery.** GSB and PSB can use sulfide as a photosynthetic electron donor and often generate separable elemental sulfur. Proposed implementations include treatment of sulfide-rich anoxic wastewater, natural gas, and biogas. The 2024 review classifies this as a promising environmental-management and biotechnology route, but the graph should represent it as an application of sulfur phototrophy rather than a core trait mechanism. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)

2. **CO2 capture and biomass/bioenergy.** Microalgal systems are being developed in photobioreactors and coupled wastewater/flue-gas processes for CO2 capture and production of biomass, biodiesel, bio-oil, ethanol, biogas, or hydrogen. A 2024 review reports literature estimates that microalgae can fix CO2 **10–50 times faster** than terrestrial plants, while stressing sensitivity to irradiation, pH, temperature, nutrients, dissolved oxygen, and inlet CO2 concentration. These are review-level comparative estimates, not a universal organism-level rate. (ashour2024usageofchlorella pages 1-2)

3. **Electrophototrophic carbon valorization.** A cyanobacterial bioelectrochemical system supplied external electrons to a PSII-deficient strain through PSI and produced acetate only when both illumination and electrons were provided. Reported acetate energy-conversion efficiency reached approximately **9%** for photons/electrons received by the biotic system and approximately **3%** based on total supplied energy; engineered cells also produced ethylene. This is an important real implementation of photosynthetic electron-chain rewiring, but exogenous electricity is an engineered bypass, not part of the natural trait definition. (li2021exogenouselectricityflowing pages 1-6)

## Recommended minimal curation set

For a compact initial graph, prioritize these broadly defensible edges:

- light → excites → chlorophyll/bacteriochlorophyll antenna;
- excited antenna → transfers excitation to → photosynthetic reaction center;
- reaction-center excitation → causes → charge separation;
- charge separation/electron transport → contributes to → transmembrane proton motive force;
- proton motive force → drives → ATP synthesis;
- **oxygenic subgraph:** water → donates electrons to PSII; PSII → produces O2; PSII → reduces PQ; PQH2 → reduces cytochrome b6f; plastocyanin/cytochrome c6 → reduces PSI; PSI → reduces ferredoxin; reducing power and ATP → support CBB carbon fixation;
- **anoxygenic subgraph:** reduced donor → supplies electrons to reaction-center chain; cyclic electron flow → produces proton motive force; optional H2S→SQR→quinone edge, explicitly restricted to sulfur phototrophs.

Carbon fixation and particular electron donors should be conditional modules. This avoids misclassifying photoheterotrophs or implying that all anoxygenic phototrophs use sulfide.

## Warnings: claims not yet suitable for unqualified TraitMech curation

- Do not encode PSII, oxygen production, or water as universal to `traitmech:000038`.
- Do not encode CO2 fixation as necessary or sufficient for the trait.
- Do not merge “photosystem I-like/type I RC” in GSB with oxygenic PSI without a taxon/branch qualifier; naming conventions can conceal major architectural differences.
- Do not treat “PS2” terminology in older sulfur-bacteria reviews as equivalent to cyanobacterial oxygen-evolving PSII.
- Do not universalize chlorosomes, FMO, LH1/LH2, SQR, FccAB, Sox, reverse TCA, CBB, or a particular donor.
- Keep pyrite utilization **uncertain and strain-specific** pending replication across taxa and direct resolution of the extracellular electron-transfer pathway. (alarcon2024evidenceforautotrophic pages 1-2)
- Keep KRV36 continuous-light tolerance, 100–180 chromatophores, and carotenoid-mediated ROS protection **strain- and condition-specific**. (tomasch2024aphotoheterotrophicbacterium pages 1-2)
- Do not infer functional photosynthesis solely from pigment genes, chlorophyll fluorescence, or a photosynthesis-gene cluster.
- Verify ontology releases before committing CURIEs for reaction-center subclasses, cyclic electron transport, chlorosome, chromatophore, and individual quinones. Label-only nodes are preferable to uncertain identifiers.
- The retrieved evidence strongly covers core photochemistry and 2024 advances but does not independently validate every possible inhibitor edge. Herbicide or inhibitor relationships should be added only with compound-specific primary evidence and assay conditions.

## DOI-first bibliography

1. Li H. et al. **Oxygen-evolving photosystem II structures during S1–S2–S3 transitions.** *Nature* 626, 670–677. Published 31 January 2024. https://doi.org/10.1038/s41586-023-06987-5 (li2024oxygenevolvingphotosystemii pages 1-2)
2. Tian L.-R., Chen J.-H. **Photosystem I: A Paradigm for Understanding Biological Environmental Adaptation Mechanisms in Cyanobacteria and Algae.** *International Journal of Molecular Sciences* 25, 8767. Published 12 August 2024. https://doi.org/10.3390/ijms25168767 (tian2024photosystemia pages 1-2)
3. Milrad Y., Mosebach L., Buchert F. **Regulation of Microalgal Photosynthetic Electron Transfer.** *Plants* 13, 2103. July 2024. https://doi.org/10.3390/plants13152103 (milrad2024regulationofmicroalgal pages 1-3)
4. Alarcon H.V. et al. **Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source.** *Applied and Environmental Microbiology* 90. July 2024. https://doi.org/10.1128/AEM.00863-24 (alarcon2024evidenceforautotrophic pages 1-2)
5. Kushkevych I. et al. **Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments.** *Frontiers in Microbiology* 15:1417714. Published 11 July 2024. https://doi.org/10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
6. Tomasch J. et al. **A photoheterotrophic bacterium from Iceland has adapted its photosynthetic machinery to the long days of polar summer.** *mSystems* 9. Published 20 February 2024. https://doi.org/10.1128/msystems.01311-23 (tomasch2024aphotoheterotrophicbacterium pages 1-2)
7. Ashour M. et al. **Usage of Chlorella and diverse microalgae for CO2 capture—towards a bioenergy revolution.** *Frontiers in Bioengineering and Biotechnology* 12:1387519. Published 20 August 2024. https://doi.org/10.3389/fbioe.2024.1387519 (ashour2024usageofchlorella pages 1-2)
8. Li Z. et al. **Exogenous Electricity Flowing through Cyanobacterial Photosystem I Drives CO2 Valorization with High Energy Efficiency.** *Energy & Environmental Science* 14, 5480–5490. September 2021. https://doi.org/10.1039/D1EE01526E (li2021exogenouselectricityflowing pages 1-6)
9. Kushkevych I. et al. **Anoxygenic Photosynthesis in Photolithotrophic Sulfur Bacteria and Their Role in Detoxication of Hydrogen Sulfide.** *Antioxidants* 10, 829. May 2021. https://doi.org/10.3390/antiox10060829 (kushkevych2021anoxygenicphotosynthesisin pages 2-3, kushkevych2021anoxygenicphotosynthesisin pages 3-5)
10. Martin W.F., Bryant D.A., Beatty J.T. **A physiological perspective on the origin and evolution of photosynthesis.** *FEMS Microbiology Reviews* 42, 205–231. 2018. https://doi.org/10.1093/femsre/fux056 (martin2018aphysiologicalperspective pages 2-3)

References

1. (martin2018aphysiologicalperspective pages 2-3): William F Martin, Donald A Bryant, and J Thomas Beatty. A physiological perspective on the origin and evolution of photosynthesis. FEMS Microbiology Reviews, 42:205-231, Nov 2018. URL: https://doi.org/10.1093/femsre/fux056, doi:10.1093/femsre/fux056. This article has 189 citations and is from a domain leading peer-reviewed journal.

2. (tomasch2024aphotoheterotrophicbacterium pages 1-2): Jürgen Tomasch, Karel Kopejtka, Tomáš Bílý, Alastair T. Gardiner, Zdenko Gardian, Sahana Shivaramu, Michal Koblížek, and David Kaftan. A photoheterotrophic bacterium from iceland has adapted its photosynthetic machinery to the long days of polar summer. Mar 2024. URL: https://doi.org/10.1128/msystems.01311-23, doi:10.1128/msystems.01311-23. This article has 5 citations and is from a peer-reviewed journal.

3. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

4. (li2021exogenouselectricityflowing pages 1-6): Zhaodong Li, Chao Wu, Xiang Gao, Bennett Addison, Shrameeta Shinde, Xin Wang, Xihan Chen, Jianping Yu, Drazenka Svedruzic, Jeffrey L. Blackburn, and Wei Xiong. Exogenous electricity flowing through cyanobacterial photosystem i drives co2 valorization with high energy efficiency. Energy & Environmental Science, 14:5480-5490, Sep 2021. URL: https://doi.org/10.1039/d1ee01526e, doi:10.1039/d1ee01526e. This article has 39 citations and is from a highest quality peer-reviewed journal.

5. (kushkevych2021anoxygenicphotosynthesisin pages 2-3): Ivan Kushkevych, Veronika Bosáková, Monika Vítězová, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis in photolithotrophic sulfur bacteria and their role in detoxication of hydrogen sulfide. Antioxidants, 10:829, May 2021. URL: https://doi.org/10.3390/antiox10060829, doi:10.3390/antiox10060829. This article has 19 citations.

6. (kushkevych2021anoxygenicphotosynthesisin pages 3-5): Ivan Kushkevych, Veronika Bosáková, Monika Vítězová, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis in photolithotrophic sulfur bacteria and their role in detoxication of hydrogen sulfide. Antioxidants, 10:829, May 2021. URL: https://doi.org/10.3390/antiox10060829, doi:10.3390/antiox10060829. This article has 19 citations.

7. (li2024oxygenevolvingphotosystemii pages 1-2): Hongjie Li, Yoshiki Nakajima, Eriko Nango, Shigeki Owada, Daichi Yamada, Kana Hashimoto, Fangjia Luo, Rie Tanaka, Fusamichi Akita, Koji Kato, Jungmin Kang, Yasunori Saitoh, Shunpei Kishi, Huaxin Yu, Naoki Matsubara, Hajime Fujii, Michihiro Sugahara, Mamoru Suzuki, Tetsuya Masuda, Tetsunari Kimura, Tran Nguyen Thao, Shinichiro Yonekura, Long-Jiang Yu, Takehiko Tosha, Kensuke Tono, Yasumasa Joti, Takaki Hatsui, Makina Yabashi, Minoru Kubo, So Iwata, Hiroshi Isobe, Kizashi Yamaguchi, Michihiro Suga, and Jian-Ren Shen. Oxygen-evolving photosystem ii structures during s1–s2–s3 transitions. Nature, 626:670-677, Jan 2024. URL: https://doi.org/10.1038/s41586-023-06987-5, doi:10.1038/s41586-023-06987-5. This article has 132 citations and is from a highest quality peer-reviewed journal.

8. (tian2024photosystemia pages 1-2): Li-Rong Tian and Jing-Hua Chen. Photosystem i: a paradigm for understanding biological environmental adaptation mechanisms in cyanobacteria and algae. International Journal of Molecular Sciences, 25:8767, Aug 2024. URL: https://doi.org/10.3390/ijms25168767, doi:10.3390/ijms25168767. This article has 8 citations.

9. (milrad2024regulationofmicroalgal pages 1-3): Yuval Milrad, Laura Mosebach, and Felix Buchert. Regulation of microalgal photosynthetic electron transfer. Plants, 13:2103, Jul 2024. URL: https://doi.org/10.3390/plants13152103, doi:10.3390/plants13152103. This article has 13 citations.

10. (alarcon2024evidenceforautotrophic pages 1-2): Hugo V. Alarcon, Jonathon E. Mohl, Grace W. Chong, Ana Betancourt, Yi Wang, Weinan Leng, Jason C. White, and Jie Xu. Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source. Jul 2024. URL: https://doi.org/10.1128/aem.00863-24, doi:10.1128/aem.00863-24. This article has 6 citations and is from a peer-reviewed journal.

11. (ashour2024usageofchlorella pages 1-2): Mohamed Ashour, Abdallah Tageldein Mansour, Yousef A. Alkhamis, and Mostafa Elshobary. Usage of chlorella and diverse microalgae for co2 capture - towards a bioenergy revolution. Frontiers in Bioengineering and Biotechnology, Aug 2024. URL: https://doi.org/10.3389/fbioe.2024.1387519, doi:10.3389/fbioe.2024.1387519. This article has 100 citations.