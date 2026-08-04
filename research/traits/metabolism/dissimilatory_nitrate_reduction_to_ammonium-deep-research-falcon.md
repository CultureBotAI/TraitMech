---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:58:58.075960'
end_time: '2026-08-04T06:08:25.439295'
duration_seconds: 567.36
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dissimilatory nitrate reduction to ammonium
  trait_identifier: traitmech:000030
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dissimilatory_nitrate_reduction_to_ammonium
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which nitrate is reduced via
    nitrite to ammonium (rather than to N2), conserving fixed nitrogen within the
    ecosystem. It is favored over denitrification under nitrate-limited, high-electron-donor
    conditions.
  parent_traits: METPO:1000802
  synonyms: DNRA, nitrate ammonification
  evidence_summary: 'DOI:10.1126/science.1254070:  (Kraft et al. show the donor-to-acceptor
    ratio governs whether nitrate respiration ends in ammonium (DNRA) or N2 (denitrification).)
    | DOI:10.1007/s11157-025-09719-5:  (Review of DNRA vs denitrification supports
    DNRA''s competitive advantage and nitrogen-retaining role under nitrate-limited
    conditions.)'
  causal_graph_summary: 'dnra_nitrate_to_ammonium: 11 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory nitrate reduction to ammonium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000030
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which nitrate is reduced via nitrite to ammonium (rather than to N2), conserving fixed nitrogen within the ecosystem. It is favored over denitrification under nitrate-limited, high-electron-donor conditions.
- **Parent traits:** METPO:1000802
- **Synonyms:** DNRA, nitrate ammonification
- **Existing evidence:** DOI:10.1126/science.1254070:  (Kraft et al. show the donor-to-acceptor ratio governs whether nitrate respiration ends in ammonium (DNRA) or N2 (denitrification).) | DOI:10.1007/s11157-025-09719-5:  (Review of DNRA vs denitrification supports DNRA's competitive advantage and nitrogen-retaining role under nitrate-limited conditions.)
- **Existing causal graph summary:** dnra_nitrate_to_ammonium: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **dissimilatory nitrate reduction to ammonium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.yaml`.

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
- **Trait label:** dissimilatory nitrate reduction to ammonium
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000030
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which nitrate is reduced via nitrite to ammonium (rather than to N2), conserving fixed nitrogen within the ecosystem. It is favored over denitrification under nitrate-limited, high-electron-donor conditions.
- **Parent traits:** METPO:1000802
- **Synonyms:** DNRA, nitrate ammonification
- **Existing evidence:** DOI:10.1126/science.1254070:  (Kraft et al. show the donor-to-acceptor ratio governs whether nitrate respiration ends in ammonium (DNRA) or N2 (denitrification).) | DOI:10.1007/s11157-025-09719-5:  (Review of DNRA vs denitrification supports DNRA's competitive advantage and nitrogen-retaining role under nitrate-limited conditions.)
- **Existing causal graph summary:** dnra_nitrate_to_ammonium: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **dissimilatory nitrate reduction to ammonium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.yaml`.

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


# Curation report: dissimilatory nitrate reduction to ammonium

## Trait record and scope

- **Trait label:** dissimilatory nitrate reduction to ammonium
- **Trait identifier:** `traitmech:000030`
- **Category / term kind / status:** `METABOLISM` / `CLASS` / `REVIEWED`
- **Parent:** `METPO:1000802`
- **Synonyms:** DNRA; nitrate ammonification

DNRA is an anaerobic, energy-conserving nitrate-respiration phenotype in which nitrate is reduced to nitrite and then to ammonium. Canonically, nitrate-to-nitrite is a two-electron reaction and nitrite-to-ammonia is a six-electron reaction. The ecological consequence is retention of reactive nitrogen, unlike denitrification, which produces N₂O or N₂ and can remove nitrogen from the local system (egas2024anovelmechanism pages 1-2).

### Recommended inclusion rule

Curate the complete trait only when evidence supports all of the following:

1. nitrate is used as the initial electron acceptor;
2. nitrite is an intermediate, whether transiently detected or mechanistically established;
3. ammonium/ammonia is a substantial terminal product;
4. reduction is dissimilatory and linked to respiratory metabolism rather than biomass assimilation; and
5. anoxic or oxygen-limited physiology is demonstrated or strongly supported.

The strongest phenotype assay is an anoxic nitrate-fed experiment with nitrogen balance and preferably a **¹⁵NO₃⁻ tracer yielding ¹⁵NH₄⁺**. Supporting evidence can include growth, electron-donor oxidation, nitrate/nitrite disappearance, ammonium formation, and expression or biochemical activity of pathway enzymes. Yuan et al., for example, combined slurry incubation with a ¹⁵N tracer rather than inferring activity solely from `nrfA` abundance (yuan2024spatiotemporalpatternsand pages 1-2).

### Boundary cases

- **Denitrification:** nitrate/nitrite reduction terminating substantially in NO, N₂O, or N₂. A strain may encode or operate both pathways; therefore, possession of `nar`, `nap`, or even nitrogen-gas genes does not determine the DNRA endpoint. In *Acididesulfobacillus acetoxydans*, a major ammonification branch coexists with a minor NO→N₂O→N₂ branch (egas2024anovelmechanism pages 10-13, egas2024anovelmechanism media 55eb6de8).
- **Assimilatory nitrate/nitrite reduction:** ammonium is produced for incorporation into biomass rather than as the product of respiratory electron disposal. `nasB`, `nirA`, and `nirB` can mediate assimilatory nitrite reduction and should not independently establish DNRA (egas2024anovelmechanism pages 1-2).
- **Nitrate reduction only:** nitrate→nitrite without ammonium formation is incomplete nitrate respiration, not the complete trait. For example, *T. ammonificans* showed weak growth on succinate but converted nitrate only to nitrite (sorokin2023trichlorobacterammonificansa pages 2-3).
- **Nitrite ammonification only:** NrfA-dependent nitrite→ammonium is the core second module, sometimes termed DNRA *sensu stricto*, but it does not prove capacity to start from nitrate.
- **Abiotic nitrate reduction or chemical nitrite disproportionation:** exclude unless microbial catalysis of the complete phenotype is demonstrated. Acidic nitrite chemistry can generate NO independently of a DNRA enzyme (egas2024anovelmechanism pages 10-13, egas2024anovelmechanism media 55eb6de8).
- **Ammonification of organic nitrogen:** decomposition of amino acids or other organic N is not DNRA.
- **Anammox:** consumes ammonium and nitrite to form N₂; it is mechanistically and ecologically distinct, although DNRA can supply ammonium to anammox communities.

## Current mechanistic model

The most defensible generic graph is:

**anoxia/oxygen limitation + nitrate + electron donor → nitrate respiration → nitrite → ammonium → retention of fixed nitrogen**.

The first reduction may be catalyzed by periplasmic NapAB or cytoplasm-facing NarGHI; NxrABC operating reductively is a newer candidate whose electron-flow control remains unresolved. The best-established second-step enzyme is periplasmic NrfAH. NrfA is a multiheme cytochrome-c nitrite reductase, while NrfH or NrfBCD connects it to membrane quinol oxidation. However, recent studies show that an `nrfA`-only graph is incomplete: ONR-type octaheme enzymes and apparently unrelated candidate reductases can also support ammonification (sorokin2023trichlorobacterammonificansa pages 2-2, egas2024anovelmechanism pages 1-2).

A concise set of the strongest graph-ready relationships is provided below.

| subject | predicate | object | evidence strength/qualifier | DOI |
|---|---|---|---|---|
| DNRA | retains | fixed nitrogen as ammonium rather than gaseous N loss | strong; scope-defining contrast with denitrification; ecological framing, not a molecular edge (egas2024anovelmechanism pages 1-2) | 10.1128/msystems.00967-23 |
| NapAB / NarGHI | catalyzes | nitrate → nitrite | strong; canonical DNRA first step; review/background in mechanistic study (egas2024anovelmechanism pages 1-2) | 10.1128/msystems.00967-23 |
| NrfAH | catalyzes | nitrite → ammonium | strong for canonical DNRA pathway as established background; not newly demonstrated in these papers (egas2024anovelmechanism pages 1-2) | 10.1128/msystems.00967-23 |
| octaheme nitrite reductase (ONR) | catalyzes | nitrite → ammonium | strong but taxon-specific; biochemically active in Trichlorobacter ammonificans and expressed during ammonifying growth (sorokin2023trichlorobacterammonificansa pages 2-3, sorokin2023trichlorobacterammonificansa pages 6-7) | 10.1038/s41396-023-01473-2 |
| nitrate-limited conditions | selects for / enriches | Trichlorobacter ammonificans DNRA over denitrifiers | strong but cultivation-specific; enrichment achieved by increasing acetate:nitrate ratio to nitrate-limited conditions (sorokin2023trichlorobacterammonificansa pages 2-3) | 10.1038/s41396-023-01473-2 |
| low redox potential | enables | complete nitrite reduction to ammonia in Trichlorobacter ammonificans | strong but taxon-specific; resting-cell and cultivation evidence (sorokin2023trichlorobacterammonificansa pages 2-3, sorokin2023trichlorobacterammonificansa pages 6-7) | 10.1038/s41396-023-01473-2 |
| high redox potential | increases | N2O formation during nitrite reduction in Trichlorobacter ammonificans | strong but taxon-specific; argues against complete DNRA endpoint under oxidized conditions (sorokin2023trichlorobacterammonificansa pages 2-3) | 10.1038/s41396-023-01473-2 |
| NarK | transports | nitrate into Acididesulfobacillus acetoxydans DNRA pathway | moderate; proposed in pathway model/figure, not directly assayed (egas2024anovelmechanism pages 10-13, egas2024anovelmechanism media 55eb6de8) | 10.1128/msystems.00967-23 |
| NarG | catalyzes | nitrate → nitrite in Acididesulfobacillus acetoxydans | strong; organism encodes Nar-type reductase and pathway model supports first step (egas2024anovelmechanism pages 1-2, egas2024anovelmechanism pages 10-13) | 10.1128/msystems.00967-23 |
| AsrABC | may reduce | nitrite → ammonia in Acididesulfobacillus acetoxydans | uncertain, taxon-specific; authors propose previously undescribed nitrite reductase activity (egas2024anovelmechanism pages 1-2, egas2024anovelmechanism pages 10-13) | 10.1128/msystems.00967-23 |
| DEACI_1836 (putative NirA homolog) | may reduce | nitrite → ammonia in Acididesulfobacillus acetoxydans | uncertain, taxon-specific; inferred candidate enzyme (egas2024anovelmechanism pages 1-2, egas2024anovelmechanism pages 10-13) | 10.1128/msystems.00967-23 |
| nitrite accumulation | upregulates / promotes | DNRA in “Ca. Alkanivorans nitratireducens” | moderate to strong but taxon-specific consortium evidence (wu2024anaerobicoxidationof pages 1-2) | 10.1093/ismejo/wrae063 |
| increased short-chain gaseous alkane supply | promotes | DNRA in “Ca. Alkanivorans nitratireducens” | moderate to strong but taxon-specific; electron-donor increase favored DNRA (wu2024anaerobicoxidationof pages 1-2) | 10.1093/ismejo/wrae063 |
| 40 mT static magnetic field | increases | DNRA potential rate and nrfA enrichment | strong for engineered application; reactor-specific, not general ecology (xie2024usingstaticmagnetic pages 1-2) | 10.1038/s41545-024-00352-3 |
| pH / organic carbon / altitude / sand concentration | positively correlates with | nrfA abundance in Lancang reservoir sediments | correlation only, noncausal; field association should not be curated as direct causal edge without stronger evidence (yuan2024spatiotemporalpatternsand pages 1-2) | 10.3389/fmicb.2024.1411753 |


*Table: This table condenses the strongest graph-ready causal edges and clearly marks taxon-specific, cultivation-specific, uncertain, and noncausal correlation claims. It is useful as a first-pass curation aid for building a TraitMech DNRA causal graph from the cited evidence.*

## Candidate nodes grouped by type

### 1. Trait, pathway, and process nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| Dissimilatory nitrate reduction to ammonium | `traitmech:000030` | Root trait; quote identifier verbatim. |
| Nitrate respiration | Label-only unless an existing project-approved ontology term is available | Parent respiratory process. |
| Nitrate reduction to nitrite | Rhea/MetaCyc/KEGG reaction candidate; verify before insertion | First, two-electron module. |
| Nitrite reduction to ammonium | EC `1.7.2.2` for cytochrome-c nitrite reductase (ammonia-forming), where applicable | Second, six-electron module; enzyme-specific grounding is preferable. |
| Nitrogen retention | Label-only | Ecosystem consequence, not a molecular reaction. |
| Denitrification | Use existing TraitMech/METPO term if available | Competing nitrate-respiration endpoint. |
| Assimilatory nitrate/nitrite reduction | Use existing TraitMech/METPO term if available | Explicit exclusion/contrast node. |
| Nitrosative-stress response | GO term candidate; verify exact accession | Relevant to Hcp and pathway switching but not constitutive DNRA. |

### 2. Chemicals and electron carriers

| Node | Suggested CURIE | Role |
|---|---|---|
| nitrate | `CHEBI:17632` | Initial electron acceptor |
| nitrite | `CHEBI:16301` | Free intermediate and possible toxic/stress signal |
| ammonium | `CHEBI:28938` | Predominant product at physiological pH |
| ammonia | `CHEBI:16134` | Uncharged conjugate/product terminology used by enzyme literature |
| nitric oxide | `CHEBI:16480` | Side-path intermediate and nitrosative stressor |
| nitrous oxide | `CHEBI:17045` | Denitrification/side-path product |
| dinitrogen | `CHEBI:17997` | Denitrification endpoint |
| hydroxylamine | `CHEBI:15429` | Proposed or assay-tested intermediate; not universal |
| acetate | `CHEBI:30089` | Demonstrated organic electron donor in *T. ammonificans* |
| glycerol | `CHEBI:17754` | Electron donor in *A. acetoxydans* experiments |
| dihydrogen | `CHEBI:18276` | Supplemental inorganic electron donor in *T. ammonificans* |
| quinone/quinol pool | Label or specific quinone CURIE only when known | Membrane electron-transfer carrier |
| reduced/oxidized ferredoxin | Label-only unless a specific cofactor term is chosen | Proposed donor to DEACI_1836 |
| short-chain gaseous alkanes | Label-only parent; propane/butane may be separately grounded | Donors linked to nitrate respiration in the 2024 consortium study |

Chemical CURIEs above are ontology-grounding suggestions and should be checked against the repository’s pinned ChEBI release before committing.

### 3. Genes, proteins, complexes, and transporters

| Node | Function and localization | Evidence status |
|---|---|---|
| `napA`, NapAB/NAP | Periplasmic-oriented nitrate reductase; active site in periplasmic NapA | Canonical first-step module (egas2024anovelmechanism pages 1-2) |
| `narGHI`, NarGHI/NAR | Membrane complex with cytoplasm-facing NarG active site | Canonical first-step module; directly implicated in *A. acetoxydans* (egas2024anovelmechanism pages 1-2) |
| `nxrABC`, NxrABC | Cytoplasmic nitrite oxidoreductase complex proposed to function reductively | **Uncertain directionality** (egas2024anovelmechanism pages 1-2) |
| `narK`, NarK | Nitrate/nitrite transporter | Proposed in the *A. acetoxydans* model; not independently assayed (egas2024anovelmechanism pages 10-13, egas2024anovelmechanism media 55eb6de8) |
| `nrfA`, NrfA | Periplasmic pentaheme cytochrome-c nitrite reductase; nitrite→ammonium | Canonical marker and catalyst |
| `nrfH`, NrfH | Membrane-bound quinol dehydrogenase/electron-transfer partner of NrfA | Canonical NrfAH module (sorokin2023trichlorobacterammonificansa pages 2-2) |
| `nrfBCD`, NrfBCD | Alternative membrane electron-transfer module supporting NrfA | Canonical in some Gammaproteobacteria (sorokin2023trichlorobacterammonificansa pages 2-2) |
| ONR/TaNiR | Octaheme ammonifying nitrite reductase | Strong, taxon-specific alternative in *T. ammonificans* (sorokin2023trichlorobacterammonificansa pages 2-3, sorokin2023trichlorobacterammonificansa pages 6-7) |
| `asrABC`, AsrABC | NADH-linked anaerobic sulfite reductase proposed to reduce nitrite | **Uncertain, taxon-specific candidate** in *A. acetoxydans* (egas2024anovelmechanism pages 1-2) |
| DEACI_1836 | Putatively ferredoxin-dependent NirA-like reductase | **Uncertain, taxon-specific candidate** (egas2024anovelmechanism pages 1-2, egas2024anovelmechanism pages 10-13) |
| Hcp | Hybrid-cluster protein; proposed NO→N₂O detoxification branch | Side pathway, not the defining DNRA reaction (egas2024anovelmechanism pages 10-13) |
| `nosZ`, NosZ; NosDFY | N₂O reduction and NosZ maturation | Denitrification/side branch; exclusionary rather than defining |
| PetABC | Proposed electron supply to NosZ | Taxon-specific side branch (egas2024anovelmechanism pages 10-13) |
| Amt-type transporter | Proposed ammonium export | **Model-based, not directly tested** (egas2024anovelmechanism pages 10-13, egas2024anovelmechanism media 55eb6de8) |
| [NiFe]-hydrogenases | H₂ uptake and electron donation | Three periplasmic uptake-hydrogenase operons occur in *T. ammonificans* (sorokin2023trichlorobacterammonificansa pages 2-3) |

Do not assign a generic UniProt CURIE to these nodes: protein accessions must be organism- and sequence-specific. Likewise, ONR and DEACI_1836 should remain label/locus-tag nodes until the exact sequence records are verified.

### 4. Cellular-localization nodes

Candidate groundings include **periplasm** (`GO:0042597`), **cytoplasm** (`GO:0005737`), and **membrane** (`GO:0016020`). NapA and NrfAH are classically periplasmic; NarG is cytoplasm-facing. In the proposed *A. acetoxydans* pathway, NarGHI, AsrABC, DEACI_1836, Hcp, NarK, Amt, and the electron-transfer components are arranged across the cytoplasm and membrane (egas2024anovelmechanism pages 1-2, egas2024anovelmechanism media 55eb6de8). The *T. ammonificans* ONR was predicted to be periplasmic but experimentally appeared membrane-associated, so its localization should carry a taxon-specific qualifier (sorokin2023trichlorobacterammonificansa pages 3-4).

### 5. Environmental and experimental-factor nodes

- anoxia or oxygen limitation;
- low redox potential;
- high electron-donor:nitrate ratio / nitrate-limited growth;
- organic-carbon availability and donor identity;
- nitrate and nitrite concentrations;
- nitrite accumulation;
- pH, particularly strongly acidic conditions for the *A. acetoxydans* mechanism;
- copper availability or depletion;
- sulfide and reduced iron availability;
- molybdenum and iron availability;
- temperature;
- static magnetic field intensity;
- low-frequency infrared electromagnetic-field intensity;
- reactor configuration, sediment type, and reservoir disturbance.

These should not all be represented as universal causes. Some are organism-specific experimental controls; others are field correlations.

### 6. Taxon and habitat nodes

- *Trichlorobacter ammonificans* G1: dedicated acetate-dependent ammonifier with a NAP–ONR module.
- *Acididesulfobacillus acetoxydans*: acidophilic sulfate-reducing bacterium with a proposed noncanonical cytoplasmic route.
- “Candidatus *Alkanivorans nitratireducens*”: switches between denitrification and DNRA in an alkane-fed consortium.
- *Anaeromyxobacter*, *Polyangium*, *Archangium*, *Geobacter*, and *Lacunisphaera*: prominent `nrfA`-associated genera in Lancang reservoir sediments.
- Activated sludge, wastewater bioreactors, freshwater sediment, wetland/coastal sediment, paddy soil, acid-mine-drainage sediment, and reduced sulfidic zones are relevant habitats.

NCBI Taxonomy CURIEs should be added only after resolving current accepted names and strain-level records; none should be inferred from genus labels alone.

## Evidence-backed candidate causal edges

| Subject | Predicate | Object | Supporting source text | Curation assessment |
|---|---|---|---|---|
| DNRA | has first step | nitrate→nitrite, 2 e⁻ | “DNRA canonically proceeds via two steps: the initial two-electron reduction of nitrate to nitrite…” (egas2024anovelmechanism pages 1-2) | **Curate:** generic pathway edge. |
| DNRA | has second step | nitrite→ammonia, 6 e⁻ | “…followed by the six-electron reduction of nitrite to ammonia” (egas2024anovelmechanism pages 1-2) | **Curate:** generic pathway edge. |
| NapAB | catalyzes | nitrate→nitrite | “The periplasmic-oriented Nap-type (NapAB) has its active site in the periplasmic NapA subunit” (egas2024anovelmechanism pages 1-2) | **Curate**, with periplasmic localization. |
| NarGHI | catalyzes | nitrate→nitrite | Nar-type NarGHI “has its active site in the cytoplasmic NarG subunit” (egas2024anovelmechanism pages 1-2) | **Curate**, with cytoplasm-facing qualifier. |
| NrfAH | catalyzes | nitrite→ammonium | “The best described dissimilatory nitrite reductase is the periplasmic NrfAH” (egas2024anovelmechanism pages 1-2) | **Curate:** canonical module. |
| NrfH/NrfBCD | transfers electrons from | quinol pool to NrfA | NrfH/NrfBCD are described as membrane-bound quinol dehydrogenases supporting NrfA (sorokin2023trichlorobacterammonificansa pages 2-2) | **Curate**, but encode alternatives rather than requiring both. |
| DNRA | retains | ecosystem fixed nitrogen | Nitrate reduction to ammonium versus N₂O/N₂ “determines whether nitrogen is retained within the system or lost as a gas” (egas2024anovelmechanism pages 1-2) | **Curate** as an ecosystem-level consequence, not a stoichiometric molecular edge. |
| Increasing acetate:nitrate electron ratio | enriches | *T. ammonificans* over denitrifiers | “High dominance…was achieved by gradually increasing the acetate to nitrate ratio…from nitrate excess to nitrate-limited conditions” (sorokin2023trichlorobacterammonificansa pages 2-3) | **Curate with cultivation/taxon qualifier.** Supports, but does not make universal, the donor:acceptor rule. |
| Low redox potential | enables | complete nitrite→ammonia in *T. ammonificans* | Resting cells demonstrated “the importance of low redox potential conditions for complete nitrite reduction to ammonia” (sorokin2023trichlorobacterammonificansa pages 2-3) | **Curate**, taxon- and assay-specific. |
| High redox potential | increases | N₂O formation in *T. ammonificans* | The same tests “showed that N₂O formation increased under high redox conditions” (sorokin2023trichlorobacterammonificansa pages 2-3) | **Curate**, taxon-specific competing endpoint. |
| Acetate | serves as electron donor for | nitrate ammonification by *T. ammonificans* | Strain G1 sustained growth only with acetate+nitrate and grew in nitrate-limited chemostats (sorokin2023trichlorobacterammonificansa pages 2-3) | **Curate**, taxon-specific. |
| H₂ | supplements electron donation to | nitrate ammonification by *T. ammonificans* | Acetate-limited tests showed G1 “was able to utilize H₂ as an additional e-donor for nitrate ammonification” (sorokin2023trichlorobacterammonificansa pages 2-3) | **Curate**, taxon-specific; not autotrophic growth. |
| ONR/TaNiR | catalyzes | nitrite→ammonium | ONR was the only nitrite reductase expressed during ammonifying growth and was highly active in vitro and apparently in vivo (sorokin2023trichlorobacterammonificansa pages 2-3) | **Curate**, strong taxon-specific alternative route. |
| NAP and ONR | form module for | DNRA in *T. ammonificans* | The organism encodes ammonifying ONR and complete β-subtype NAP “in a single genetic locus” (sorokin2023trichlorobacterammonificansa pages 2-3) | **Curate** as genetic-module association; physical-complex formation remains less certain. |
| DNRA by *T. ammonificans* | converts | nitrate predominantly to ammonia | Chemostat measurements reported 87 ± 11% conversion of nitrate to ammonia and no detectable NO/N₂O under complete-reduction conditions (sorokin2023trichlorobacterammonificansa pages 3-4) | **Curate** as phenotype evidence. |
| NarK | imports | nitrate in *A. acetoxydans* | “After the uptake of nitrate by NarK, nitrate is reduced to nitrite by NarG” (egas2024anovelmechanism pages 10-13) | **Uncertain:** pathway-model assignment rather than direct transport assay. |
| NarG | reduces | nitrate→nitrite in *A. acetoxydans* | Same proposed pathway plus Nar-type genomic and expression evidence (egas2024anovelmechanism pages 1-2, egas2024anovelmechanism pages 10-13) | **Curate**, taxon-specific. |
| AsrABC | may reduce | nitrite→ammonia in *A. acetoxydans* | Nitrite is “likely reduced” by the “previously undescribed nitrite reductase activity” of NADH-linked AsrABC (egas2024anovelmechanism pages 1-2) | **Do not curate as asserted fact:** retain as `may_catalyze`/hypothesis. |
| DEACI_1836 | may reduce | nitrite→ammonia in *A. acetoxydans* | Authors propose “a putatively ferredoxin-dependent homolog of…NirA (DEACI_1836), or both” (egas2024anovelmechanism pages 1-2) | **Do not curate as asserted fact:** candidate only. |
| Amt transporter | may export | ammonium | Ammonium “requires active transport, which could be carried out by an Amt-type ammonium transporter” (egas2024anovelmechanism pages 10-13) | **Do not curate as asserted fact.** |
| Nitrite accumulation | induces/promotes | DNRA expression in “Ca. *A. nitratireducens*” | Removing ammonium caused nitrite accumulation, ammonium production, and upregulated DNRA genes; nitrite reached as much as 1.4 mmol N L⁻¹ (wu2024anaerobicoxidationof pages 1-2) | **Curate**, consortium- and taxon-specific. |
| Increased short-chain alkane supply | promotes | DNRA in “Ca. *A. nitratireducens*” | Increasing SCGA supply promoted DNRA (wu2024anaerobicoxidationof pages 1-2) | **Curate**, taxon/reactor-specific electron-donor effect. |
| Anammox removal of nitrite | suppresses | DNRA in the alkane consortium | Eliminating nitrite accumulation increased alkane/nitrate consumption but suppressed DNRA (wu2024anaerobicoxidationof pages 1-2) | **Curate**, community-context-specific. |
| 40 mT static magnetic field | increases | DNRA reactor performance | Start-up fell from 75 to 41 days; day-80 rate was 174 ± 11 versus 88 ± 6 μmol kg⁻¹ h⁻¹ at 0 mT (xie2024usingstaticmagnetic pages 1-2) | **Curate only in an application subgraph.** Dose response is nonmonotonic: 80 mT delayed startup to 103 days. |
| 40 mT static magnetic field | enriches | `nrfA` and *Geobacter* | `nrfA` enrichment accelerated and *Geobacter* rose from 15.71% to 32.11% (xie2024usingstaticmagnetic pages 1-2) | **Curate as reactor-specific measured effect**, not direct molecular activation. |
| 0.04 μT IR-EMF | increases | ammonium conversion/DNRA potential | Ammonium conversion increased 117.7%; day-120 potential rate was 26.43 versus 8.49 μmol kg⁻¹ h⁻¹ in control (xie2024longtermoperationand pages 1-2) | **Curate only in application subgraph.** Mechanistic claim via ATP remains indirect. |
| Reservoir sediment pH/organic carbon/altitude/sand | correlates with | `nrfA` abundance | Pearson/RDA showed positive correlations (yuan2024spatiotemporalpatternsand pages 1-2) | **Do not encode with a causal predicate.** Use `correlated_with` if supported by the schema. |

The visually inspected *A. acetoxydans* pathway figure corroborates the proposed cellular arrangement of NarK, NarGHI, AsrABC/DEACI_1836, Amt, Hcp, and NosZ, but its dashed and candidate relationships remain hypotheses rather than direct enzyme assignments (egas2024anovelmechanism media 55eb6de8).

## Recent developments and quantitative findings, 2023–2024

### Mechanistic diversity beyond `nrfA`

Sorokin et al. demonstrated a dedicated acetate-dependent organism that lacks classical Nrf systems and instead couples a β-type periplasmic NAP module to an ammonifying octaheme nitrite reductase. The enzyme was expressed during ammonifying growth and biochemically active; the organism converted 87 ± 11% of nitrate to ammonia under low-redox, nitrate-limited conditions (sorokin2023trichlorobacterammonificansa pages 3-4, sorokin2023trichlorobacterammonificansa pages 2-3). This is authoritative evidence that absence of `nrfA` does **not** establish absence of DNRA.

Egas et al. then described an acidophile that carries NarGHI but lacks seven recognized nitrite-reductase systems. Transcriptomic/proteomic evidence implicated AsrABC, DEACI_1836, and Hcp, but the authors appropriately describe the ammonifying enzyme assignments as likely or putative. Reported responses included approximately 8-fold NarGHI upregulation, 16-fold DEACI_1836 upregulation, 29-fold AsrABC upregulation, and 30-fold Hcp upregulation under nitrate-reducing conditions (egas2024anovelmechanism pages 2-5). These are strong candidate-generation data, not purified-enzyme proof.

### Environmentally triggered pathway switching

In a 2024 alkane-oxidizing consortium, nitrite accumulated to about 1.4 mmol N L⁻¹ and DNRA expression increased in “Ca. *Alkanivorans nitratireducens*.” Increasing propane/butane supply also promoted DNRA, whereas anammox consumption of nitrite suppressed it. The authors interpret switching as a response that alleviates nitrite-associated oxidative stress (wu2024anaerobicoxidationof pages 1-2). This adds a regulatory mechanism to the classical donor:acceptor-ratio model.

For *T. ammonificans*, redox and trace-metal availability were at least as important as the bulk donor:acceptor ratio. Complete reduction occurred around strongly reducing chemostat conditions, whereas approximately +50 mV batch conditions favored denitrifiers and −350 mV enrichment conditions favored the ammonifier. The authors hypothesize that reduced, copper-depleted, organic/sulfide-rich zones favor DNRA, while more oxidized, copper- and NOx-rich zones favor denitrification (sorokin2023trichlorobacterammonificansa pages 2-3, sorokin2023trichlorobacterammonificansa pages 6-7). Because this is partly ecological interpretation from one isolate/enrichment, it should not be universalized.

### Field measurements

Lancang cascade-reservoir sediments showed potential DNRA rates of **0.01–0.15 nmol-N cm⁻³ h⁻¹** and `nrfA` abundances of **1.08 × 10⁵–2.51 × 10⁶ copies g⁻¹ dry weight**. Mean relative abundances among sequenced `nrfA` groups included *Anaeromyxobacter* 4.52%, *Polyangium* 4.09%, *Archangium* 1.86%, *Geobacter* 1.34%, and *Lacunisphaera* 1.32% (yuan2024spatiotemporalpatternsand pages 1-2). These values establish habitat prevalence but not universal rates or causal taxon contributions.

### Engineered applications

Current implementation research is aimed at converting nitrate-rich wastewater into recoverable ammonium rather than losing nitrogen as N₂. A 40 mT static magnetic field nearly doubled the reported potential DNRA rate relative to 0 mT and shortened startup by 34 days; 80 mT was inhibitory, demonstrating a narrow, nonmonotonic operating window (xie2024usingstaticmagnetic pages 1-2). A separate low-frequency IR-EMF reactor study reported control, 0.04 μT, and 0.06 μT ammonium-conversion efficiencies of 33.3%, 72.5%, and 54.0%, respectively (xie2024longtermoperationand pages 1-2, xie2024longtermoperationand pages 2-4). These are laboratory/reactor demonstrations, not yet evidence of routine full-scale deployment.

Practical opportunities include ammonium recovery from nitrate-rich wastewater, nitrogen-retaining bioelectrochemical barriers, coupling DNRA-produced ammonium to downstream recovery, and deliberate control of nitrite in anammox systems. The corresponding risk is that DNRA can undermine treatment designed for permanent nitrogen removal because ammonium remains bioavailable and can be reoxidized.

## Expert interpretation for TraitMech curation

1. **Represent chemistry before markers.** The defining evidence is nitrate→ammonium flux, not `nrfA` detection. `nrfA` is an excellent marker for canonical nitrite ammonification but misses ONR and candidate noncanonical pathways.
2. **Model DNRA as two modular reactions.** This permits Nap/Nar/Nxr alternatives for the first step and Nrf/ONR/other alternatives for the second.
3. **Separate generic and taxon-specific graphs.** Low redox, copper depletion, nitrite-stress switching, alkane donation, and acidophile-specific AsrABC hypotheses should not become unconditional universal edges.
4. **Keep endpoint competition explicit.** DNRA and denitrification can coexist in one genome and culture. Environmental conditions regulate electron partitioning, not merely gene presence.
5. **Distinguish causal experiments from correlations.** Controlled redox, donor, magnetic-field, and reactor interventions can support causal edges within their systems. Reservoir pH or organic-carbon associations should remain `correlated_with` observations.
6. **Attach assay provenance.** `nrfA` qPCR measures genetic potential/abundance; transcriptomics measures expression; purified-enzyme assays establish catalytic capacity; ¹⁵N flux and nitrogen balance most directly establish the phenotype.

## Claims that should not yet be asserted in TraitMech

- **AsrABC → nitrite-to-ammonium** and **DEACI_1836 → nitrite-to-ammonium** as confirmed catalytic edges. Both are compelling but unresolved alternatives (egas2024anovelmechanism pages 1-2).
- **NxrABC → nitrate-to-nitrite in DNRA** as a generic directed edge; direction-control is explicitly unclear (egas2024anovelmechanism pages 1-2).
- **NarK uptake** and **Amt ammonium export** in *A. acetoxydans* as experimentally verified transport events; both are pathway-model assignments (egas2024anovelmechanism pages 10-13).
- Hydroxylamine as a universal free DNRA intermediate. It was not detected during *T. ammonificans* nitrite reduction, and its broader role remains unresolved (egas2024anovelmechanism pages 1-2, sorokin2023trichlorobacterammonificansa pages 6-7).
- `nrfA` abundance as equivalent to DNRA rate or phenotype.
- Any universal rule that high C:NO₃ alone determines DNRA. Recent work shows important roles for redox, copper, nitrite stress, donor identity, community interactions, and inorganic donors (wu2024anaerobicoxidationof pages 1-2, sorokin2023trichlorobacterammonificansa pages 6-7).
- Reservoir correlations as causal environmental controls (yuan2024spatiotemporalpatternsand pages 1-2).
- Magnetic or infrared electromagnetic enhancement as field-ready, full-scale technology; present evidence is reactor-specific (xie2024usingstaticmagnetic pages 1-2, xie2024longtermoperationand pages 1-2).
- Reduced N₂O emissions as an intrinsic property of every DNRA organism. Some strains produce N₂O side products, and pathway coexistence is documented.

## DOI-first bibliography

1. Egas RA, Kurth JM, Boeren S, et al. **A novel mechanism for dissimilatory nitrate reduction to ammonium in *Acididesulfobacillus acetoxydans*.** *mSystems*. Published **7 February 2024**; 9(3). DOI: [10.1128/msystems.00967-23](https://doi.org/10.1128/msystems.00967-23). Primary source for canonical scope, localization, alternative enzyme candidates, and the inspected pathway model (egas2024anovelmechanism pages 1-2, egas2024anovelmechanism pages 10-13, egas2024anovelmechanism media 55eb6de8).
2. Sorokin DY, Tikhonova TV, Koch H, et al. **Trichlorobacter ammonificans, a dedicated acetate-dependent ammonifier with a novel module for dissimilatory nitrate reduction to ammonia.** *ISME Journal*. Published **July 2023**;17:1639–1648. DOI: [10.1038/s41396-023-01473-2](https://doi.org/10.1038/s41396-023-01473-2) (sorokin2023trichlorobacterammonificansa pages 3-4, sorokin2023trichlorobacterammonificansa pages 2-3, sorokin2023trichlorobacterammonificansa pages 6-7).
3. Wu M, Liu X, Engelberts JP, Tyson GW, McIlroy SJ, Guo J. **Anaerobic oxidation of ammonium and short-chain gaseous alkanes coupled to nitrate reduction by a bacterial consortium.** *ISME Journal*. Published **2024**;18. DOI: [10.1093/ismejo/wrae063](https://doi.org/10.1093/ismejo/wrae063) (wu2024anaerobicoxidationof pages 1-2).
4. Yuan B, Guo M, Zhou X, Li M, Xie S. **Spatiotemporal patterns and co-occurrence patterns of dissimilatory nitrate reduction to ammonium community in sediments of the Lancang River cascade reservoirs.** *Frontiers in Microbiology*. Published **19 June 2024**;15:1411753. DOI: [10.3389/fmicb.2024.1411753](https://doi.org/10.3389/fmicb.2024.1411753) (yuan2024spatiotemporalpatternsand pages 1-2).
5. Xie Y, Wang Z, Ni S-Q. **Using static magnetic field to recover ammonia efficiently by DNRA process.** *npj Clean Water*. Published **July 2024**;7:54. DOI: [10.1038/s41545-024-00352-3](https://doi.org/10.1038/s41545-024-00352-3) (xie2024usingstaticmagnetic pages 1-2).
6. Xie Y, Wang Z, Ismail S, Ni S-Q. **Long-term operation and dynamic response of dissimilatory nitrate reduction to ammonium process under low-frequency infrared electromagnetic field.** *npj Clean Water*. Published **July 2024**;7. DOI: [10.1038/s41545-024-00356-z](https://doi.org/10.1038/s41545-024-00356-z) (xie2024longtermoperationand pages 1-2, xie2024longtermoperationand pages 2-4).
7. Wu X, Yu S, Sui W, et al. **Aerobic carbon metabolism modulates nitrite ammonifiers for inhibiting nitrogen loss as revealed by microcosm experiment of agricultural upland soil.** *bioRxiv*. Posted **November 2024**. DOI: [10.1101/2024.11.04.621907](https://doi.org/10.1101/2024.11.04.621907). **Preprint; use cautiously** (wu2024aerobiccarbonmetabolism pages 8-12).

The most defensible expansion of the existing 11-node/9-edge graph is therefore a modular core containing nitrate, nitrite, ammonium, Nap/Nar alternatives, NrfA with its electron-transfer partner, electron donor, anoxia/low-redox context, and nitrogen retention. ONR–NAP should be added as a well-supported taxon-specific alternative; AsrABC/DEACI_1836, NxrABC directionality, Amt transport, and field correlations should remain provisional or excluded from asserted causal edges.

References

1. (egas2024anovelmechanism pages 1-2): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 11 citations and is from a peer-reviewed journal.

2. (yuan2024spatiotemporalpatternsand pages 1-2): Bo Yuan, Mengjing Guo, Xiaode Zhou, Miaojie Li, and Shuguang Xie. Spatiotemporal patterns and co-occurrence patterns of dissimilatory nitrate reduction to ammonium community in sediments of the lancang river cascade reservoirs. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1411753, doi:10.3389/fmicb.2024.1411753. This article has 4 citations and is from a peer-reviewed journal.

3. (egas2024anovelmechanism pages 10-13): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 11 citations and is from a peer-reviewed journal.

4. (egas2024anovelmechanism media 55eb6de8): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 11 citations and is from a peer-reviewed journal.

5. (sorokin2023trichlorobacterammonificansa pages 2-3): Dimitry Y Sorokin, Tamara V Tikhonova, Hanna Koch, Eveline M van den Berg, Renske S Hinderks, Martin Pabst, Natalia I Dergousova, Anastasia Y Soloveva, Gijs J Kuenen, Vladimir O Popov, Mark C M van Loosdrecht, and Sebastian Lücker. Trichlorobacter ammonificans, a dedicated acetate-dependent ammonifier with a novel module for dissimilatory nitrate reduction to ammonia. The ISME Journal, 17:1639-1648, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01473-2, doi:10.1038/s41396-023-01473-2. This article has 30 citations.

6. (sorokin2023trichlorobacterammonificansa pages 2-2): Dimitry Y Sorokin, Tamara V Tikhonova, Hanna Koch, Eveline M van den Berg, Renske S Hinderks, Martin Pabst, Natalia I Dergousova, Anastasia Y Soloveva, Gijs J Kuenen, Vladimir O Popov, Mark C M van Loosdrecht, and Sebastian Lücker. Trichlorobacter ammonificans, a dedicated acetate-dependent ammonifier with a novel module for dissimilatory nitrate reduction to ammonia. The ISME Journal, 17:1639-1648, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01473-2, doi:10.1038/s41396-023-01473-2. This article has 30 citations.

7. (sorokin2023trichlorobacterammonificansa pages 6-7): Dimitry Y Sorokin, Tamara V Tikhonova, Hanna Koch, Eveline M van den Berg, Renske S Hinderks, Martin Pabst, Natalia I Dergousova, Anastasia Y Soloveva, Gijs J Kuenen, Vladimir O Popov, Mark C M van Loosdrecht, and Sebastian Lücker. Trichlorobacter ammonificans, a dedicated acetate-dependent ammonifier with a novel module for dissimilatory nitrate reduction to ammonia. The ISME Journal, 17:1639-1648, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01473-2, doi:10.1038/s41396-023-01473-2. This article has 30 citations.

8. (wu2024anaerobicoxidationof pages 1-2): Mengxiong Wu, Xiawei Liu, J Pamela Engelberts, Gene W Tyson, Simon J McIlroy, and Jianhua Guo. Anaerobic oxidation of ammonium and short-chain gaseous alkanes coupled to nitrate reduction by a bacterial consortium. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae063, doi:10.1093/ismejo/wrae063. This article has 11 citations.

9. (xie2024usingstaticmagnetic pages 1-2): Yuyang Xie, Zhibin Wang, and Shou-Qing Ni. Using static magnetic field to recover ammonia efficiently by dnra process. npj Clean Water, Jul 2024. URL: https://doi.org/10.1038/s41545-024-00352-3, doi:10.1038/s41545-024-00352-3. This article has 16 citations and is from a peer-reviewed journal.

10. (sorokin2023trichlorobacterammonificansa pages 3-4): Dimitry Y Sorokin, Tamara V Tikhonova, Hanna Koch, Eveline M van den Berg, Renske S Hinderks, Martin Pabst, Natalia I Dergousova, Anastasia Y Soloveva, Gijs J Kuenen, Vladimir O Popov, Mark C M van Loosdrecht, and Sebastian Lücker. Trichlorobacter ammonificans, a dedicated acetate-dependent ammonifier with a novel module for dissimilatory nitrate reduction to ammonia. The ISME Journal, 17:1639-1648, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01473-2, doi:10.1038/s41396-023-01473-2. This article has 30 citations.

11. (xie2024longtermoperationand pages 1-2): Yuyang Xie, Zhibin Wang, Sherif Ismail, and Shou-Qing Ni. Long-term operation and dynamic response of dissimilatory nitrate reduction to ammonium process under low-frequency infrared electromagnetic field. npj Clean Water, Jul 2024. URL: https://doi.org/10.1038/s41545-024-00356-z, doi:10.1038/s41545-024-00356-z. This article has 12 citations and is from a peer-reviewed journal.

12. (egas2024anovelmechanism pages 2-5): Reinier A. Egas, Julia M. Kurth, Sjef Boeren, Diana Z. Sousa, Cornelia U. Welte, and Irene Sánchez-Andrea. A novel mechanism for dissimilatory nitrate reduction to ammonium in <i>acididesulfobacillus acetoxydans</i>. Mar 2024. URL: https://doi.org/10.1128/msystems.00967-23, doi:10.1128/msystems.00967-23. This article has 11 citations and is from a peer-reviewed journal.

13. (xie2024longtermoperationand pages 2-4): Yuyang Xie, Zhibin Wang, Sherif Ismail, and Shou-Qing Ni. Long-term operation and dynamic response of dissimilatory nitrate reduction to ammonium process under low-frequency infrared electromagnetic field. npj Clean Water, Jul 2024. URL: https://doi.org/10.1038/s41545-024-00356-z, doi:10.1038/s41545-024-00356-z. This article has 12 citations and is from a peer-reviewed journal.

14. (wu2024aerobiccarbonmetabolism pages 8-12): Xiaogang Wu, Siyu Yu, Weikang Sui, Xinyu Zhang, Ji Li, Qiaoyu Wu, and Xiaojun Zhang. Aerobic carbon metabolism modulates nitrite ammonifiers for inhibiting nitrogen loss as revealed by microcosm experiment of agricultural upland soil. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.04.621907, doi:10.1101/2024.11.04.621907. This article has 1 citations.