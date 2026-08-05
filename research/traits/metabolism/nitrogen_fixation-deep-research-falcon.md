---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:34:22.085225'
end_time: '2026-08-04T06:43:13.992513'
duration_seconds: 531.91
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: nitrogen fixation
  trait_identifier: traitmech:000103
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: nitrogen_fixation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which an organism reduces atmospheric dinitrogen (N2)
    to ammonia using the nitrogenase enzyme complex, making fixed nitrogen biologically
    available (diazotrophy).
  parent_traits: METPO:1000060
  synonyms: diazotrophy
  evidence_summary: 'DOI:10.1038/nrmicro.2018.9:  (Kuypers, Marchant & Kartal place
    nitrogen fixation as the reductive entry point of the microbial nitrogen-cycling
    network.) | DOI:10.1038/nrmicro954:  (Dixon & Kahn review the genetic regulation
    of biological nitrogen fixation and nitrogenase.)'
  causal_graph_summary: 'nitrogen_fixation_nitrogenase: 11 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** nitrogen fixation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000103
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism reduces atmospheric dinitrogen (N2) to ammonia using the nitrogenase enzyme complex, making fixed nitrogen biologically available (diazotrophy).
- **Parent traits:** METPO:1000060
- **Synonyms:** diazotrophy
- **Existing evidence:** DOI:10.1038/nrmicro.2018.9:  (Kuypers, Marchant & Kartal place nitrogen fixation as the reductive entry point of the microbial nitrogen-cycling network.) | DOI:10.1038/nrmicro954:  (Dixon & Kahn review the genetic regulation of biological nitrogen fixation and nitrogenase.)
- **Existing causal graph summary:** nitrogen_fixation_nitrogenase: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **nitrogen fixation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/nitrogen_fixation.yaml`.

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
- **Trait label:** nitrogen fixation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000103
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism reduces atmospheric dinitrogen (N2) to ammonia using the nitrogenase enzyme complex, making fixed nitrogen biologically available (diazotrophy).
- **Parent traits:** METPO:1000060
- **Synonyms:** diazotrophy
- **Existing evidence:** DOI:10.1038/nrmicro.2018.9:  (Kuypers, Marchant & Kartal place nitrogen fixation as the reductive entry point of the microbial nitrogen-cycling network.) | DOI:10.1038/nrmicro954:  (Dixon & Kahn review the genetic regulation of biological nitrogen fixation and nitrogenase.)
- **Existing causal graph summary:** nitrogen_fixation_nitrogenase: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **nitrogen fixation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/nitrogen_fixation.yaml`.

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


# Curation-focused research report: microbial nitrogen fixation

## Trait record and scope

- **Trait label:** nitrogen fixation
- **Trait identifier:** `traitmech:000103`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1000060`
- **Synonym:** diazotrophy

### Scope summary

This trait is the **physiological capacity of a microorganism to reduce atmospheric dinitrogen to ammonia through an active nitrogenase system**. The canonical overall reaction is:

**N₂ + 8 H⁺ + 8 e⁻ + 16 MgATP → 2 NH₃ + H₂ + 16 MgADP + 16 Pi.**

Thus, the trait includes nitrogenase expression and maturation, supply of ATP and low-potential electrons, cofactor assembly, and protection from oxygen. It does not require extracellular ammonium excretion: fixed ammonia may instead be assimilated immediately through pathways such as GS–GOGAT. Mo-dependent nitrogenase is the canonical system, but V-dependent and Fe-only nitrogenases also confer the trait. (bennett2023engineeringnitrogenasesfor pages 1-2, barron2024nitrogenfixinggammaproteobacteria pages 4-7)

**Important boundaries:**

1. **Not nitrogen assimilation.** Uptake and assimilation of NH₄⁺ or nitrate use already fixed nitrogen and do not establish diazotrophy.
2. **Not ammonification, nitrification, or denitrification.** These transform fixed nitrogen compounds rather than introducing atmospheric N₂ into metabolism.
3. **Not merely `nifH` presence or expression.** `nifH` encodes the Fe-protein component, but active fixation also requires the catalytic component, appropriate metallocofactors, accessory functions, reductant, ATP, and a permissive oxygen regime. (bennett2023engineeringnitrogenasesfor pages 1-2, bennett2023engineeringnitrogenasesfor pages 6-7)
4. **Acetylene reduction is a proxy, not the defining phenotype.** Nitrogenase reduces acetylene to ethylene, but conversion to an N₂-fixation rate varies substantially among enzyme isoforms and environmental systems. Direct incorporation of ¹⁵N₂ is stronger phenotypic evidence. (smercina2019optimizationofthe pages 20-23, smercina2019optimizationofthe pages 1-5, bellenger2020biologicalnitrogenfixation pages 4-5)
5. **Growth in nitrogen-free medium is supportive but not definitive.** Cells can scavenge residual nitrogen from biomass or medium, so growth should be combined with nitrogenase activity or isotopic evidence. (bennett2023engineeringnitrogenasesfor pages 8-9)
6. **Ammonium excretion is a downstream/export phenotype.** It may be engineered and agriculturally useful but is not necessary for nitrogen fixation itself. (martinezferia2024geneticremodelingof pages 2-3)

## Current mechanistic understanding

In Mo nitrogenase, the `nifH` product is a homodimeric Fe protein containing a [4Fe–4S] cluster. It transfers one electron at a time to the `nifDK`-encoded MoFe protein, coupling each electron-transfer event to hydrolysis of two MgATP. Electrons move through the P-cluster to FeMo-cofactor, where N₂ reduction occurs. The obligatory H₂ coproduct and minimum 16-ATP cost make fixation intrinsically energy intensive. (bennett2023engineeringnitrogenasesfor pages 1-2)

Accessory machinery is part of the causal mechanism rather than optional annotation. NifS and NifU support Fe–S-cluster formation; NifB participates in synthesis of the active-site cofactor precursor; NifEN provides the scaffold used in FeMo-cofactor maturation; and NifV, NifM, electron carriers, and oxidoreductases contribute to maturation or electron delivery. In engineered hosts, coexpression of `nifF` and `nifJ` can markedly improve activity, illustrating that the structural genes alone do not guarantee the trait. (bennett2023engineeringnitrogenasesfor pages 1-2, bennett2023engineeringnitrogenasesfor pages 6-7)

Mo nitrogenase is the most widespread form. V nitrogenase and Fe-only nitrogenase are mechanistically homologous alternatives, generally less active and more oxygen sensitive. Environmental Mo availability can control isoform deployment; therefore, alternative systems should be represented as parallel trait-realization branches rather than mandatory components of one universal pathway. (bennett2023engineeringnitrogenasesfor pages 1-2, bellenger2020biologicalnitrogenfixation pages 4-5)

## Candidate nodes grouped by type

### Trait, process, and activity nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| nitrogen fixation | `traitmech:000103`; `GO:0009399` | Trait/root biological process |
| metabolism | `METPO:1000060` | Supplied parent trait |
| nitrogenase activity | `EC:1.18.6.1` | Enzymatic activity; verify database version before YAML commit |
| diazotrophic growth | Label-only | Phenotypic readout, not identical to direct N₂ reduction |
| ammonium assimilation by GS–GOGAT | Label-only pending pathway-specific grounding | Downstream of fixation, taxon/context dependent |
| ammonium excretion | Label-only | Application-relevant downstream phenotype |

### Genes, proteins, enzymes, and complexes

| Candidate node | Role | Grounding recommendation |
|---|---|---|
| `nifH` / NifH / Fe protein | ATP-dependent electron delivery to catalytic protein | Use gene/protein label; assign taxon-specific UniProt only in organism-specific graphs |
| `nifD`, `nifK` / NifDK / MoFe protein | Catalytic component containing P-cluster and FeMo-cofactor | Label-only complex plus taxon-specific proteins if needed |
| `nifB` / NifB | Active-site cofactor precursor biosynthesis | Label-only unless taxon fixed |
| `nifE`, `nifN` / NifEN | FeMo-cofactor assembly scaffold | Label-only complex |
| `nifS`, `nifU` | Sulfur mobilization and Fe–S-cluster assembly | Label-only or taxon-specific UniProt |
| `nifV`, `nifM`, `nifX` | Cofactor or nitrogenase maturation | Treat roles individually; not all are universally required |
| `nifF`, `nifJ` | Electron carrier and oxidoreductase supporting nitrogenase | Strong in particular engineered/proteobacterial systems; not universal |
| NifA | Transcriptional activator of nif genes | Regulatory architecture is taxon-specific |
| NifL | Inhibitory sensor/regulator of NifA | Proteobacterial branch, not universal |
| NtrB/NtrC, GlnB/PII | Nitrogen-status signaling | Taxon-specific regulatory module |
| FixABCX | Electron-bifurcating reductant-supply system | Strong evidence in *Azotobacter vinelandii* |
| Rnf complex | Ion-coupled ferredoxin reduction/electron supply | Strong evidence in *A. vinelandii* |
| GS–GOGAT | Assimilation of fixed ammonium | Downstream branch rather than part of nitrogenase reaction |
| uptake hydrogenase HupSL | Recovers H₂/electrons and can improve micro-oxic activity | Engineering/taxon-specific protective branch |
| FeSII/Shethna protein | Conformational protection against O₂ damage | *Azotobacter*-specific candidate |
| Anf3 terminal oxidase | Proposed respiratory protection of Fe-only nitrogenase | Keep uncertain pending direct causal validation |

### Cofactors, clusters, and chemicals

| Candidate node | Suggested grounding or status |
|---|---|
| dinitrogen | ChEBI chemical grounding recommended; verify exact current CURIE before commit |
| ammonia/ammonium | ChEBI grounding recommended; represent protonation state consistently |
| proton, electron, ATP, ADP, phosphate | ChEBI grounding recommended |
| dihydrogen | ChEBI grounding recommended |
| oxygen | ChEBI grounding recommended |
| molybdenum, vanadium, iron | ChEBI elemental/ionic grounding recommended, with oxidation state only when specified |
| MgATP | Label-only unless the intended ChEBI species is verified |
| [4Fe–4S] cluster | ChEBI/GO candidate; verify exact cofactor term |
| P-cluster ([8Fe–7S]) | Label-only candidate |
| FeMo-cofactor | Label-only candidate; composition includes Mo, Fe, S, interstitial C, and homocitrate |
| FeV-cofactor; FeFe-cofactor | Label-only alternative-nitrogenase cofactors |
| reduced ferredoxin/flavodoxin | ChEBI/protein labels; electron donor varies by organism |
| acetylene and ethylene | Assay substrate/product; ChEBI grounding recommended |
| ¹⁵N₂ | Isotopically labeled assay substrate; verify isotope-specific ChEBI entry |
| ammonium chloride | Experimental fixed-N repressor; ChEBI grounding recommended |
| α-ketoglutarate | Regulatory/metabolic signal in the *A. vinelandii* NifLA system |

### Environmental, localization, and assay nodes

- Low-oxygen or micro-oxic condition; anoxic condition; aerobic condition.
- Nitrogen limitation versus fixed-nitrogen-replete condition.
- Carbon/energy availability, soil moisture, pH, temperature, Fe availability, Mo availability, V availability, and phosphorus availability.
- Cytoplasm; photosynthetic membrane; heterocyst; plant root/rhizosphere; root-associated or endophytic niche.
- ¹⁵N₂ incorporation, acetylene-reduction assay, diazotrophic growth assay, nitrogenase H₂ evolution, `nifH` detection/expression, and extracellular ammonium measurement.

Environmental nodes should be grounded to ENVO only after selecting the exact context. “Micro-oxic” is an experimental oxygen regime, whereas “rhizosphere” and “soil” are environmental features; they should not be conflated.

## Candidate causal edges

The following table prioritizes graph-ready edges. Snippets are short evidence paraphrases or quotations derived from the retrieved text; uncertainty is explicit where a claim should be restricted by taxon or assay.

| # | Subject | Predicate | Object | Reference and supporting snippet | Curation notes |
|---:|---|---|---|---|---|
| 1 | nitrogenase | catalyzes | reduction of N₂ to NH₃ | Bennett et al. 2023: “N₂ + 8H⁺ + 8e⁻ + 16MgATP → 2NH₃ + H₂ + 16MgADP + 16Pi.” DOI: [10.34133/bdr.0005](https://doi.org/10.34133/bdr.0005). (bennett2023engineeringnitrogenasesfor pages 1-2) | **High confidence; core trait edge.** |
| 2 | nitrogen fixation | produces | H₂ as an obligatory coproduct | Same stoichiometric equation reports one H₂ per N₂ reduced. (bennett2023engineeringnitrogenasesfor pages 1-2) | High confidence for the canonical minimum reaction. |
| 3 | nitrogen fixation | consumes | at least 16 MgATP per N₂ | Bennett et al. report 16 ATP in the canonical equation; Barron et al. reiterate this energy requirement. (bennett2023engineeringnitrogenasesfor pages 1-2, barron2024nitrogenfixinggammaproteobacteria pages 4-7) | High confidence; actual cellular cost may exceed the theoretical minimum. |
| 4 | NifH Fe protein | transfers electrons to | NifDK MoFe protein | “NifH accepts electrons at its [4Fe–4S] cluster and transiently binds NifDK.” (bennett2023engineeringnitrogenasesfor pages 1-2) | High confidence for Mo nitrogenase. |
| 5 | NifH electron transfer | requires | hydrolysis of two MgATP per electron | Bennett et al.: NifH transfers electrons while “hydrolyzing 2 Mg-ATP per electron.” (bennett2023engineeringnitrogenasesfor pages 1-2) | High confidence. |
| 6 | NifDK | contains | P-cluster and FeMo-cofactor electron-transfer/catalytic centers | Electrons reach the [8Fe–7S] cluster and then FeMo-cofactor, where N₂ is reduced. (bennett2023engineeringnitrogenasesfor pages 1-2) | High confidence for Mo nitrogenase only. |
| 7 | NifEN | enables assembly of | FeMo-cofactor | MoFe nitrogenase “requires NifEN”; `nifE/nifN` are assigned cofactor-biosynthesis roles. (bennett2023engineeringnitrogenasesfor pages 1-2, bennett2023engineeringnitrogenasesfor pages 6-7) | High confidence for canonical Mo-nitrogenase maturation. |
| 8 | NifB | contributes to biosynthesis of | nitrogenase active-site cofactor | NifB is listed among required assembly factors and additional cofactor-biosynthesis steps. (bennett2023engineeringnitrogenasesfor pages 1-2, bennett2023engineeringnitrogenasesfor pages 6-7) | High confidence, but exact precursor intermediates need a dedicated source before adding finer edges. |
| 9 | NifS and NifU | enable assembly of | nitrogenase Fe–S clusters | The review assigns `nifU/nifS` to Fe–S-cluster biosynthesis. (bennett2023engineeringnitrogenasesfor pages 6-7) | High confidence; avoid implying they act only on nitrogenase in all taxa. |
| 10 | reduced ferredoxin/flavodoxin supply | provides | low-potential electrons to nitrogenase | FixABCX and Rnf generate low-potential electrons; loss of both eliminates diazotrophic capacity in *A. vinelandii*. (barron2024nitrogenfixinggammaproteobacteria pages 4-7, barron2024nitrogenfixinggammaproteobacteria pages 8-10) | **Taxon-specific implementation.** Generalize only to “low-potential reductant enables fixation.” |
| 11 | carbon and energy availability | promotes | nitrogen-fixation capacity | Carbon cocktails increased ARA approximately 1,700-fold and direct ¹⁵N₂ rates 17-fold relative to glucose alone in one soil assay system. (smercina2019optimizationofthe pages 1-5) | **Assay- and site-specific quantitative effect; do not universalize fold changes.** |
| 12 | fixed nitrogen/ammonium | represses | nif expression and nitrogen fixation | Nitrogen status controls σ⁵⁴-dependent nif transcription; remodeled strains retained some repression in ammonium chloride. (bennett2023engineeringnitrogenasesfor pages 1-2, martinezferia2024geneticremodelingof pages 2-3) | High-level edge is strong; NtrBC/NifLA mechanism is taxon-specific. |
| 13 | NtrBC/PII nitrogen-status signaling | regulates | nif transcription | Barron et al. describe GlnB/PII–NtrB–NtrC signaling governing nitrogen responses in *A. vinelandii*. (barron2024nitrogenfixinggammaproteobacteria pages 4-7) | **Taxon-specific.** Verify the directionality described for each nitrogen state before encoding detailed phosphorylation edges. |
| 14 | NifA | activates | nif transcription | NifLA controls nif transcription, with NifA responding to metabolic status including α-ketoglutarate. (barron2024nitrogenfixinggammaproteobacteria pages 8-10) | Proteobacterial branch; not universal among diazotrophs. |
| 15 | NifL | inhibits | NifA-dependent nif transcription under nonpermissive conditions | The NifLA system senses carbon/nitrogen status and oxygen; deletion of `nifL` was used to derepress engineered strains. (barron2024nitrogenfixinggammaproteobacteria pages 8-10, martinezferia2024geneticremodelingof pages 2-3) | Taxon/strain-specific regulatory edge. |
| 16 | oxygen | inactivates/inhibits | nitrogenase | Engineered oxygenic phototroph experiments identify O₂ toxicity as a principal challenge; photosynthetic O₂ deactivated nitrogenase within two hours in one system. (liu2018engineeringnitrogenfixation pages 8-9, dong2021anengineerednondiazotrophic pages 5-7) | High confidence at the enzyme level; whole-cell oxygen tolerance varies through protection. |
| 17 | high respiratory flux | lowers intracellular/local oxygen | nitrogenase-protective microenvironment | *A. vinelandii* uses parallel respiratory pathways and terminal oxidases for respiratory protection. (bennett2023engineeringnitrogenasesfor pages 7-8, barron2024nitrogenfixinggammaproteobacteria pages 8-10) | Strong but organism-specific implementation. |
| 18 | heterocyst differentiation | creates | micro-oxic site supporting nitrogen fixation | Heterocyst respiration and specialized protection permit oxic diazotrophic growth in filamentous cyanobacteria. (bennett2023engineeringnitrogenasesfor pages 7-8, varghese2019alowpotentialterminal pages 9-9) | **Cyanobacteria-specific.** Do not make heterocysts mandatory. |
| 19 | temporal separation from oxygenic photosynthesis | promotes | nighttime nitrogen fixation | Some cyanobacteria express nitrogenase at night, when photosynthetic O₂ generation stops, using glycogen for ATP. (bennett2023engineeringnitrogenasesfor pages 7-8) | **Taxon-specific strategy.** |
| 20 | uptake hydrogenase HupSL | increases | nitrogenase activity under micro-oxic conditions | In engineered *Synechocystis*, introduced hydrogenase genes produced up to a sixfold increase at 0.5–1.0% O₂. DOI: [10.1128/mbio.01029-18](https://doi.org/10.1128/mbio.01029-18). (liu2018engineeringnitrogenfixation pages 8-9) | **Engineered strain and assay-specific.** Curate as “promotes” rather than universal oxygen protection. |
| 21 | Mo availability | promotes preferential expression/activity of | Mo nitrogenase | Diazotrophs preferentially express Mo nitrogenase when environmental Mo is adequate. (bellenger2020biologicalnitrogenfixation pages 4-5) | Strong general tendency, but metal regulation varies by organism. |
| 22 | Mo limitation in organisms carrying alternatives | permits/induces use of | V or Fe-only nitrogenase | Alternative systems are encoded by `vnf` or `anf` genes and can replace Mo nitrogenase under appropriate metal conditions. (bennett2023engineeringnitrogenasesfor pages 1-2, bennett2023engineeringnitrogenasesfor pages 6-7, bellenger2020biologicalnitrogenfixation pages 4-5) | Restrict to organisms that actually possess the corresponding genes. |
| 23 | GS–GOGAT pathway | assimilates | nitrogenase-derived ammonium | Barron et al. identify GS–GOGAT as the primary ammonium-assimilation route in *A. vinelandii*. (barron2024nitrogenfixinggammaproteobacteria pages 4-7) | **Taxon-specific evidence; downstream of trait.** |
| 24 | ¹⁵N₂ incorporation | directly measures | nitrogen fixation | The ¹⁵N₂ method measures enrichment directly and is more accurate than ARA when appropriately optimized. (smercina2019optimizationofthe pages 20-23, smercina2019optimizationofthe pages 1-5, smercina2019optimizationofthe pages 16-20) | High-confidence assay edge; incubation and gas dissolution require optimization. |
| 25 | nitrogenase | reduces | acetylene to ethylene | This alternative substrate reaction forms the basis of ARA. (bellenger2020biologicalnitrogenfixation pages 4-5) | High confidence enzyme activity; ARA remains indirect for N₂ fixation. |
| 26 | acetylene-reduction assay | proxies | nitrogenase activity | ARA is rapid and inexpensive but isoform-dependent conversion factors range from less than 1 to greater than 30 in reported systems. (smercina2019optimizationofthe pages 20-23, smercina2019optimizationofthe pages 1-5) | **Do not equate ARA rate directly with N₂-fixed without calibration.** |
| 27 | `nifL`/`glnD` remodeling | derepresses | nitrogenase under N-rich conditions | Engineered *Klebsiella variicola* and *Kosakonia sacchari* retained activity and increased ammonium excretion under fixed-N-rich conditions. (martinezferia2024geneticremodelingof pages 2-3) | **Engineered, strain-specific; uncertain as a general graph edge.** |
| 28 | engineered root-associated diazotroph inoculation | contributes fixed N to | maize | ¹⁵N field analyses estimated an average 21.2 kg N ha⁻¹ by VT–R1, but the 95% CI ranged from −0.16 to 42.6 kg ha⁻¹. DOI: [10.1038/s41598-024-78243-3](https://doi.org/10.1038/s41598-024-78243-3). (martinezferia2024geneticremodelingof pages 10-11, martinezferia2024geneticremodelingof pages 1-2) | Application edge, not a universal trait mechanism; uncertainty is substantial. |

A compact subset of the most defensible edges is provided below.

| subject | predicate | object | confidence/context | DOI |
|---|---|---|---|---|
| nitrogenase (EC:1.18.6.1) | catalyzes | N2 + 8H+ + 8e- + 16MgATP -> 2NH3 + H2 + 16MgADP + 16Pi | High; canonical biological nitrogen fixation reaction/stochiometry in recent review (bennett2023engineeringnitrogenasesfor pages 1-2) | 10.34133/bdr.0005 |
| NifH (Fe protein) | transfers electrons to | NifDK (MoFe protein) | High; core Mo-nitrogenase mechanism, with NifH transiently interacting with NifDK (bennett2023engineeringnitrogenasesfor pages 1-2) | 10.34133/bdr.0005 |
| NifH (Fe protein) | hydrolyzes | 2 Mg-ATP per electron transferred | High; recent review explicitly links ATP hydrolysis to each electron transfer step (bennett2023engineeringnitrogenasesfor pages 1-2) | 10.34133/bdr.0005 |
| NifDK (MoFe protein) | catalyzes reduction of | dinitrogen at the FeMo-cofactor | High; NifDK is the catalytic component and FeMo-co is the active-site cofactor for N2 reduction (bennett2023engineeringnitrogenasesfor pages 1-2) | 10.34133/bdr.0005 |
| NifEN | is required for assembly of | FeMo-cofactor / active Mo-nitrogenase | High for Mo-nitrogenase; cofactor-biosynthesis scaffold in recent review and experimental support (bennett2023engineeringnitrogenasesfor pages 1-2, bennett2023engineeringnitrogenasesfor pages 6-7) | 10.34133/bdr.0005 |
| NifB | contributes to biosynthesis of | nitrogenase active-site cofactor | High; repeatedly identified as essential accessory/cofactor-biosynthesis gene (bennett2023engineeringnitrogenasesfor pages 1-2, bennett2023engineeringnitrogenasesfor pages 6-7) | 10.34133/bdr.0005 |
| NifU/NifS | support assembly of | Fe-S clusters required for nitrogenase function | High; accessory Fe-S cluster biosynthesis role in nitrogenase maturation (bennett2023engineeringnitrogenasesfor pages 1-2, bennett2023engineeringnitrogenasesfor pages 6-7) | 10.34133/bdr.0005 |
| oxygen (O2) | inhibits/inactivates | nitrogenase activity | High; broad mechanistic constraint, shown in reviews and engineered cyanobacteria experiments (bennett2023engineeringnitrogenasesfor pages 7-8, liu2018engineeringnitrogenfixation pages 8-9, dong2021anengineerednondiazotrophic pages 5-7) | 10.34133/bdr.0005; 10.1128/mbio.01029-18; 10.1016/j.xcrp.2021.100444 |
| fixed nitrogen / ammonium | represses | nif expression and biological nitrogen fixation | High, but regulatory details taxon-specific; NtrBC/NifLA and ammonium repression documented in Proteobacteria/engineered strains (bennett2023engineeringnitrogenasesfor pages 1-2, barron2024nitrogenfixinggammaproteobacteria pages 4-7, martinezferia2024geneticremodelingof pages 2-3) | 10.34133/bdr.0005; 10.3390/microorganisms12102087; 10.1038/s41598-024-78243-3 |
| FixABCX and Rnf | generate low-potential electrons for | nitrogenase / diazotrophic growth | High in Azotobacter vinelandii; deletion of both abolishes diazotrophic capacity, so curate as taxon-specific unless generalized (barron2024nitrogenfixinggammaproteobacteria pages 4-7, barron2024nitrogenfixinggammaproteobacteria pages 8-10) | 10.3390/microorganisms12102087 |
| 15N2 incorporation assay | directly measures | biological nitrogen fixation | High for assay interpretation; preferred direct assay versus acetylene-reduction proxy, with optimization caveats (smercina2019optimizationofthe pages 20-23, smercina2019optimizationofthe pages 1-5, smercina2019optimizationofthe pages 16-20) | 10.1007/s11104-019-04307-3 |


*Table: This table lists compact, high-confidence causal edges for curating a nitrogen fixation TraitMech graph, prioritizing core mechanism and assay interpretation. It also flags where evidence is strong but taxon-specific, helping separate broadly curatable biology from narrower context-dependent claims.*

## Recent developments and applications, emphasizing 2023–2024

### Synthetic-biology progress

A 2023 review frames the main engineering problem as integration of nitrogenase structural genes, cofactor maturation, electron transfer, ATP supply, oxygen protection, and appropriate regulation—not simple transfer of `nifHDK`. Heterologous work has tested bacterial chassis and targeting of nitrogenase/cofactor proteins to eukaryotic organelles, but fully autonomous nitrogen-fixing crops remain an engineering objective rather than an established application. (bennett2023engineeringnitrogenasesfor pages 1-2, barron2024nitrogenfixinggammaproteobacteria pages 8-10, bennett2023engineeringnitrogenasesfor pages 6-7)

The same evidence supports a practical expert interpretation: **oxygen management and energetic integration are at least as important as gene transfer**. In aerobic diazotrophs, high respiration simultaneously consumes oxygen and supplies energy, whereas engineered oxygenic cells must reconcile nitrogenase with photosynthetic O₂ production. (barron2024nitrogenfixinggammaproteobacteria pages 8-10, bennett2023engineeringnitrogenasesfor pages 7-8, dong2021anengineerednondiazotrophic pages 5-7)

### Engineered diazotrophs in maize

The most concrete 2024 real-world evidence concerns a commercial inoculant containing remodeled root-associated diazotrophs. Across 58 large on-farm side-by-side trials, inoculated maize receiving 39–45 kg N ha⁻¹ less synthetic fertilizer had essentially identical reported yield to business-as-usual treatment—13.42 versus 13.43 Mg ha⁻¹, *p*=0.871—and 8% lower yield coefficient of variation. Across 135 commercial fields, early-season measurements showed 39 g plant⁻¹ greater fresh weight, 12.6 µmol m⁻² greater leaf chlorophyll, and a median 14% increase in aboveground biomass N. (martinezferia2024geneticremodelingof pages 8-10, martinezferia2024geneticremodelingof pages 10-11)

The same study estimated approximately 11% nitrogen derived from the atmosphere, or 21.2 kg N ha⁻¹ by VT–R1. However, the confidence interval was wide (−0.16 to 42.6 kg ha⁻¹), a 2021 Wisconsin isotope result was only marginal (8.2% Ndfa, *p*=0.08), and 2022 sites showed no significant isotope dilution. Drought was associated with weak activity, and some grower fertilizer rates may already have exceeded agronomic optima by 17–28 kg N ha⁻¹. These limitations mean the field findings support **partial, context-dependent fertilizer substitution**, not a universal replacement coefficient. (martinezferia2024geneticremodelingof pages 10-11, martinezferia2024geneticremodelingof pages 11-12, martinezferia2024geneticremodelingof pages 3-6)

### Biofertilizer consortia

A 2024 two-species study reported that *Bacillus subtilis* stimulated *A. vinelandii* fixation under nitrogen limitation, approximately doubling N inputs and maintaining fixation during stationary phase; proteomics showed increased NifD/NifK abundance. This suggests that community interactions can be engineered into inoculant design, but it is a defined co-culture result rather than evidence that any plant-growth-promoting bacterium will stimulate diazotrophy.

### Bioelectrochemical and enzyme applications

Nitrogenase can be coupled to electrodes or engineered photosynthetic hosts for ambient-condition ammonia production. These systems currently serve primarily as mechanistic and proof-of-concept platforms because oxygen sensitivity, ATP coupling, electron-transfer efficiency, enzyme stability, and scale remain limiting. In an engineered oxygenic cyanobacterium, photosynthetic O₂ deactivated nitrogenase within two hours; chemical suppression of photosystem II was used to control O₂, illustrating both feasibility and the practical incompatibility still to be solved. (dong2021anengineerednondiazotrophic pages 5-7)

## Assay interpretation for TraitMech curation

A recommended evidence hierarchy is:

1. **Direct ¹⁵N₂ incorporation into biomass or a defined recipient** with gas-dissolution, contamination, incubation, and natural-abundance controls.
2. **Mass balance or quantified NH₃ production from N₂**, ideally with isotopic confirmation.
3. **ARA**, provided controls and an empirically appropriate conversion are reported.
4. **Diazotrophic growth**, with stringent exclusion of contaminating or recycled fixed N.
5. **Nitrogenase expression or `nifH` abundance**, which establishes genetic potential or regulation but not flux.

ARA can overestimate fixation because acetylene changes oxygen use, derepresses activity during long incubations, and interacts with endogenous ethylene production and consumption. In one labeled-acetylene analysis summarized by Smercina et al., only 43% of recovered ethylene arose from acetylene reduction. Direct ¹⁵N₂ assays are preferable but remain sensitive to incubation duration, gas dissolution, soil disturbance, and detection limits; intact samples and site-specific optimization are recommended. (smercina2019optimizationofthe pages 20-23, smercina2019optimizationofthe pages 27-31, smercina2019optimizationofthe pages 1-5)

## Expert analysis for graph design

The existing 11-node/10-edge graph should be expanded as a **branched causal architecture**:

1. **Core universal branch:** N₂ substrate → nitrogenase reaction → NH₃ + H₂, coupled to ATP and low-potential electrons.
2. **Mo-nitrogenase implementation:** `nifH` → NifH; `nifD/nifK` → NifDK; NifH → electron transfer → NifDK; NifB/NifEN/NifUS → cofactor and cluster maturation.
3. **Alternative implementation branches:** `vnf` and `anf` modules, each conditioned on gene presence and metal regime.
4. **Regulatory branch:** nitrogen limitation promotes expression; fixed nitrogen represses expression. NifLA and NtrBC should be taxon-qualified rather than asserted universally.
5. **Environmental branch:** O₂ inhibits nitrogenase, while heterocysts, temporal separation, respiratory protection, conformational protection, and uptake hydrogenase are alternative—not cumulative mandatory—solutions.
6. **Downstream branch:** NH₃ → NH₄⁺/assimilation through GS–GOGAT or, in engineered strains, export to a plant.
7. **Evidence branch:** direct ¹⁵N₂ assay versus ARA and genetic proxies. Assay nodes should not be represented as biological causes of the trait.

This design avoids the principal curation error: turning a mechanism documented in *A. vinelandii*, proteobacteria, cyanobacteria, or an engineered strain into a universal requirement for all diazotrophs.

## Warnings: claims not yet suitable for unqualified TraitMech curation

1. **Do not curate `nifH` as sufficient for nitrogen fixation.** Paralogs, incomplete gene clusters, absent maturation machinery, and environmental repression can all yield false-positive trait assignments.
2. **Do not encode NifLA or NtrBC as universal.** Their detailed wiring is lineage dependent.
3. **Do not make heterocysts, uptake hydrogenase, FeSII, Anf3, FixABCX, or Rnf universal requirements.** These are alternative, taxon-specific solutions.
4. **Do not treat extracellular ammonium production as synonymous with fixation.** Wild-type diazotrophs commonly assimilate NH₄⁺ rapidly; excretion often requires engineering.
5. **Do not infer exact N₂-fixation flux from ARA using a universal 3:1 ratio.** Reported conversion behavior varies by nitrogenase isoform and environment. (smercina2019optimizationofthe pages 20-23, smercina2019optimizationofthe pages 1-5)
6. **Do not curate the 21.2 kg N ha⁻¹ maize value as a general efficacy constant.** It is product-, crop-, stage-, site-, and weather-dependent, with a confidence interval including zero. (martinezferia2024geneticremodelingof pages 10-11)
7. **Treat Anf3-mediated oxygen protection as provisional.** Its oxidase activity and electron acceptance are established, but direct in vivo causal protection of Fe-only nitrogenase was presented as a prediction. (varghese2019alowpotentialterminal pages 9-9)
8. **Verify all chemical and protein CURIEs against current ontology releases before committing YAML.** Label-only nodes are preferable to guessed identifiers.
9. **Separate constitutive capacity from realized activity.** Diazotrophy can be encoded yet inactive under fixed-N-replete, energy-limited, metal-limited, or oxygen-rich conditions.

## DOI-first bibliography

1. Bennett EM, Murray JW, Isalan M. **Engineering Nitrogenases for Synthetic Nitrogen Fixation: From Pathway Engineering to Directed Evolution.** *Biodesign Research*. Published January 2023. DOI: [10.34133/bdr.0005](https://doi.org/10.34133/bdr.0005). (bennett2023engineeringnitrogenasesfor pages 1-2, bennett2023engineeringnitrogenasesfor pages 6-7)
2. Barron S, Mus F, Peters JW. **Nitrogen-Fixing Gamma Proteobacteria *Azotobacter vinelandii*—A Blueprint for Nitrogen-Fixing Plants?** *Microorganisms*. Published October 2024. DOI: [10.3390/microorganisms12102087](https://doi.org/10.3390/microorganisms12102087). (barron2024nitrogenfixinggammaproteobacteria pages 4-7, barron2024nitrogenfixinggammaproteobacteria pages 8-10)
3. Martinez-Feria R et al. **Genetic remodeling of soil diazotrophs enables partial replacement of synthetic nitrogen fertilizer with biological nitrogen fixation in maize.** *Scientific Reports*. Published November 2024. DOI: [10.1038/s41598-024-78243-3](https://doi.org/10.1038/s41598-024-78243-3). (martinezferia2024geneticremodelingof pages 8-10, martinezferia2024geneticremodelingof pages 10-11, martinezferia2024geneticremodelingof pages 1-2)
4. Liu D et al. **Engineering Nitrogen Fixation Activity in an Oxygenic Phototroph.** *mBio*. Published July 2018. DOI: [10.1128/mbio.01029-18](https://doi.org/10.1128/mbio.01029-18). (liu2018engineeringnitrogenfixation pages 8-9)
5. Smercina DN et al. **Optimization of the ¹⁵N₂ incorporation and acetylene reduction methods for free-living nitrogen fixation.** *Plant and Soil*. Published October 2019. DOI: [10.1007/s11104-019-04307-3](https://doi.org/10.1007/s11104-019-04307-3). (smercina2019optimizationofthe pages 20-23, smercina2019optimizationofthe pages 1-5)
6. Bellenger JP et al. **Biological nitrogen fixation by alternative nitrogenases in terrestrial ecosystems: a review.** *Biogeochemistry*. Published April 2020. DOI: [10.1007/s10533-020-00666-7](https://doi.org/10.1007/s10533-020-00666-7). (bellenger2020biologicalnitrogenfixation pages 4-5)
7. Varghese F et al. **A low-potential terminal oxidase associated with the iron-only nitrogenase from the nitrogen-fixing bacterium *Azotobacter vinelandii*.** *Journal of Biological Chemistry*. Published June 2019. DOI: [10.1074/jbc.RA118.007285](https://doi.org/10.1074/jbc.RA118.007285). (varghese2019alowpotentialterminal pages 9-9)
8. Dong F et al. **An engineered, non-diazotrophic cyanobacterium and its application in bioelectrochemical nitrogen fixation.** *Cell Reports Physical Science*. Published June 2021. DOI: [10.1016/j.xcrp.2021.100444](https://doi.org/10.1016/j.xcrp.2021.100444). (dong2021anengineerednondiazotrophic pages 5-7)

The strongest immediate additions to `data/traits/metabolism/nitrogen_fixation.yaml` are the canonical reaction, NifH-to-NifDK electron transfer with ATP coupling, NifDK/FeMo-cofactor catalysis, NifB/NifEN/NifUS maturation, oxygen inhibition, low-potential-electron dependence, and fixed-nitrogen repression. Organism-specific regulatory and oxygen-protection modules should be represented as qualified branches or deferred until TraitMech supports taxonomic/context constraints.

References

1. (bennett2023engineeringnitrogenasesfor pages 1-2): Emily M. Bennett, James W. Murray, and Mark Isalan. Engineering nitrogenases for synthetic nitrogen fixation: from pathway engineering to directed evolution. Biodesign Research, 5:0005, Jan 2023. URL: https://doi.org/10.34133/bdr.0005, doi:10.34133/bdr.0005. This article has 87 citations.

2. (barron2024nitrogenfixinggammaproteobacteria pages 4-7): Sayre Barron, Florence Mus, and John W. Peters. Nitrogen-fixing gamma proteobacteria azotobacter vinelandii—a blueprint for nitrogen-fixing plants? Microorganisms, 12:2087, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102087, doi:10.3390/microorganisms12102087. This article has 12 citations.

3. (bennett2023engineeringnitrogenasesfor pages 6-7): Emily M. Bennett, James W. Murray, and Mark Isalan. Engineering nitrogenases for synthetic nitrogen fixation: from pathway engineering to directed evolution. Biodesign Research, 5:0005, Jan 2023. URL: https://doi.org/10.34133/bdr.0005, doi:10.34133/bdr.0005. This article has 87 citations.

4. (smercina2019optimizationofthe pages 20-23): Darian N. Smercina, Sarah E. Evans, Maren L. Friesen, and Lisa K. Tiemann. Optimization of the 15n2 incorporation and acetylene reduction methods for free-living nitrogen fixation. Plant and Soil, 445:595-611, Oct 2019. URL: https://doi.org/10.1007/s11104-019-04307-3, doi:10.1007/s11104-019-04307-3. This article has 37 citations and is from a domain leading peer-reviewed journal.

5. (smercina2019optimizationofthe pages 1-5): Darian N. Smercina, Sarah E. Evans, Maren L. Friesen, and Lisa K. Tiemann. Optimization of the 15n2 incorporation and acetylene reduction methods for free-living nitrogen fixation. Plant and Soil, 445:595-611, Oct 2019. URL: https://doi.org/10.1007/s11104-019-04307-3, doi:10.1007/s11104-019-04307-3. This article has 37 citations and is from a domain leading peer-reviewed journal.

6. (bellenger2020biologicalnitrogenfixation pages 4-5): J. P. Bellenger, R. Darnajoux, X. Zhang, and A. M. L. Kraepiel. Biological nitrogen fixation by alternative nitrogenases in terrestrial ecosystems: a review. Biogeochemistry, 149:53-73, Apr 2020. URL: https://doi.org/10.1007/s10533-020-00666-7, doi:10.1007/s10533-020-00666-7. This article has 190 citations and is from a peer-reviewed journal.

7. (bennett2023engineeringnitrogenasesfor pages 8-9): Emily M. Bennett, James W. Murray, and Mark Isalan. Engineering nitrogenases for synthetic nitrogen fixation: from pathway engineering to directed evolution. Biodesign Research, 5:0005, Jan 2023. URL: https://doi.org/10.34133/bdr.0005, doi:10.34133/bdr.0005. This article has 87 citations.

8. (martinezferia2024geneticremodelingof pages 2-3): Rafael Martinez-Feria, Maegen B. Simmonds, Bilge Ozaydin, Stacey Lewis, Allison Schwartz, Alex Pluchino, Mary E. McKellar, Shayin S. Gottlieb, Tasha Kayatsky, Richelle Vital, Sharon E. Mehlman, Zoe Caron, Nicholas R. Colaianni, Jean-Michel Ané, Junko Maeda, V. Infante, Bjorn H. Karlsson, Caitlin McLimans, Tony Vyn, Brendan Hanson, Garrett Verhagen, Clayton Nevins, Lori Reese, Paul Otyama, Alice Robinson, Timothy Learmonth, Christine M. F. Miller, Keira L Havens, Alvin Tamsir, and Karsten Temme. Genetic remodeling of soil diazotrophs enables partial replacement of synthetic nitrogen fertilizer with biological nitrogen fixation in maize. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-78243-3, doi:10.1038/s41598-024-78243-3. This article has 39 citations and is from a peer-reviewed journal.

9. (barron2024nitrogenfixinggammaproteobacteria pages 8-10): Sayre Barron, Florence Mus, and John W. Peters. Nitrogen-fixing gamma proteobacteria azotobacter vinelandii—a blueprint for nitrogen-fixing plants? Microorganisms, 12:2087, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102087, doi:10.3390/microorganisms12102087. This article has 12 citations.

10. (liu2018engineeringnitrogenfixation pages 8-9): Deng Liu, Michelle Liberton, Jingjie Yu, Himadri B. Pakrasi, and Maitrayee Bhattacharyya-Pakrasi. Engineering nitrogen fixation activity in an oxygenic phototroph. mBio, Jul 2018. URL: https://doi.org/10.1128/mbio.01029-18, doi:10.1128/mbio.01029-18. This article has 72 citations and is from a domain leading peer-reviewed journal.

11. (dong2021anengineerednondiazotrophic pages 5-7): Fangyuan Dong, Yoo Seok Lee, Erin M. Gaffney, Matteo Grattieri, Helena Haddadin, Shelley D. Minteer, and Hui Chen. An engineered, non-diazotrophic cyanobacterium and its application in bioelectrochemical nitrogen fixation. Cell Reports Physical Science, 2:100444, Jun 2021. URL: https://doi.org/10.1016/j.xcrp.2021.100444, doi:10.1016/j.xcrp.2021.100444. This article has 49 citations and is from a peer-reviewed journal.

12. (bennett2023engineeringnitrogenasesfor pages 7-8): Emily M. Bennett, James W. Murray, and Mark Isalan. Engineering nitrogenases for synthetic nitrogen fixation: from pathway engineering to directed evolution. Biodesign Research, 5:0005, Jan 2023. URL: https://doi.org/10.34133/bdr.0005, doi:10.34133/bdr.0005. This article has 87 citations.

13. (varghese2019alowpotentialterminal pages 9-9): Febin Varghese, Burak Veli Kabasakal, Charles A.R. Cotton, Jörg Schumacher, A. William Rutherford, Andrea Fantuzzi, and James W. Murray. A low-potential terminal oxidase associated with the iron-only nitrogenase from the nitrogen-fixing bacterium azotobacter vinelandii. Journal of Biological Chemistry, 294:9367-9376, Jun 2019. URL: https://doi.org/10.1074/jbc.ra118.007285, doi:10.1074/jbc.ra118.007285. This article has 28 citations and is from a domain leading peer-reviewed journal.

14. (smercina2019optimizationofthe pages 16-20): Darian N. Smercina, Sarah E. Evans, Maren L. Friesen, and Lisa K. Tiemann. Optimization of the 15n2 incorporation and acetylene reduction methods for free-living nitrogen fixation. Plant and Soil, 445:595-611, Oct 2019. URL: https://doi.org/10.1007/s11104-019-04307-3, doi:10.1007/s11104-019-04307-3. This article has 37 citations and is from a domain leading peer-reviewed journal.

15. (martinezferia2024geneticremodelingof pages 10-11): Rafael Martinez-Feria, Maegen B. Simmonds, Bilge Ozaydin, Stacey Lewis, Allison Schwartz, Alex Pluchino, Mary E. McKellar, Shayin S. Gottlieb, Tasha Kayatsky, Richelle Vital, Sharon E. Mehlman, Zoe Caron, Nicholas R. Colaianni, Jean-Michel Ané, Junko Maeda, V. Infante, Bjorn H. Karlsson, Caitlin McLimans, Tony Vyn, Brendan Hanson, Garrett Verhagen, Clayton Nevins, Lori Reese, Paul Otyama, Alice Robinson, Timothy Learmonth, Christine M. F. Miller, Keira L Havens, Alvin Tamsir, and Karsten Temme. Genetic remodeling of soil diazotrophs enables partial replacement of synthetic nitrogen fertilizer with biological nitrogen fixation in maize. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-78243-3, doi:10.1038/s41598-024-78243-3. This article has 39 citations and is from a peer-reviewed journal.

16. (martinezferia2024geneticremodelingof pages 1-2): Rafael Martinez-Feria, Maegen B. Simmonds, Bilge Ozaydin, Stacey Lewis, Allison Schwartz, Alex Pluchino, Mary E. McKellar, Shayin S. Gottlieb, Tasha Kayatsky, Richelle Vital, Sharon E. Mehlman, Zoe Caron, Nicholas R. Colaianni, Jean-Michel Ané, Junko Maeda, V. Infante, Bjorn H. Karlsson, Caitlin McLimans, Tony Vyn, Brendan Hanson, Garrett Verhagen, Clayton Nevins, Lori Reese, Paul Otyama, Alice Robinson, Timothy Learmonth, Christine M. F. Miller, Keira L Havens, Alvin Tamsir, and Karsten Temme. Genetic remodeling of soil diazotrophs enables partial replacement of synthetic nitrogen fertilizer with biological nitrogen fixation in maize. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-78243-3, doi:10.1038/s41598-024-78243-3. This article has 39 citations and is from a peer-reviewed journal.

17. (martinezferia2024geneticremodelingof pages 8-10): Rafael Martinez-Feria, Maegen B. Simmonds, Bilge Ozaydin, Stacey Lewis, Allison Schwartz, Alex Pluchino, Mary E. McKellar, Shayin S. Gottlieb, Tasha Kayatsky, Richelle Vital, Sharon E. Mehlman, Zoe Caron, Nicholas R. Colaianni, Jean-Michel Ané, Junko Maeda, V. Infante, Bjorn H. Karlsson, Caitlin McLimans, Tony Vyn, Brendan Hanson, Garrett Verhagen, Clayton Nevins, Lori Reese, Paul Otyama, Alice Robinson, Timothy Learmonth, Christine M. F. Miller, Keira L Havens, Alvin Tamsir, and Karsten Temme. Genetic remodeling of soil diazotrophs enables partial replacement of synthetic nitrogen fertilizer with biological nitrogen fixation in maize. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-78243-3, doi:10.1038/s41598-024-78243-3. This article has 39 citations and is from a peer-reviewed journal.

18. (martinezferia2024geneticremodelingof pages 11-12): Rafael Martinez-Feria, Maegen B. Simmonds, Bilge Ozaydin, Stacey Lewis, Allison Schwartz, Alex Pluchino, Mary E. McKellar, Shayin S. Gottlieb, Tasha Kayatsky, Richelle Vital, Sharon E. Mehlman, Zoe Caron, Nicholas R. Colaianni, Jean-Michel Ané, Junko Maeda, V. Infante, Bjorn H. Karlsson, Caitlin McLimans, Tony Vyn, Brendan Hanson, Garrett Verhagen, Clayton Nevins, Lori Reese, Paul Otyama, Alice Robinson, Timothy Learmonth, Christine M. F. Miller, Keira L Havens, Alvin Tamsir, and Karsten Temme. Genetic remodeling of soil diazotrophs enables partial replacement of synthetic nitrogen fertilizer with biological nitrogen fixation in maize. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-78243-3, doi:10.1038/s41598-024-78243-3. This article has 39 citations and is from a peer-reviewed journal.

19. (martinezferia2024geneticremodelingof pages 3-6): Rafael Martinez-Feria, Maegen B. Simmonds, Bilge Ozaydin, Stacey Lewis, Allison Schwartz, Alex Pluchino, Mary E. McKellar, Shayin S. Gottlieb, Tasha Kayatsky, Richelle Vital, Sharon E. Mehlman, Zoe Caron, Nicholas R. Colaianni, Jean-Michel Ané, Junko Maeda, V. Infante, Bjorn H. Karlsson, Caitlin McLimans, Tony Vyn, Brendan Hanson, Garrett Verhagen, Clayton Nevins, Lori Reese, Paul Otyama, Alice Robinson, Timothy Learmonth, Christine M. F. Miller, Keira L Havens, Alvin Tamsir, and Karsten Temme. Genetic remodeling of soil diazotrophs enables partial replacement of synthetic nitrogen fertilizer with biological nitrogen fixation in maize. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-78243-3, doi:10.1038/s41598-024-78243-3. This article has 39 citations and is from a peer-reviewed journal.

20. (smercina2019optimizationofthe pages 27-31): Darian N. Smercina, Sarah E. Evans, Maren L. Friesen, and Lisa K. Tiemann. Optimization of the 15n2 incorporation and acetylene reduction methods for free-living nitrogen fixation. Plant and Soil, 445:595-611, Oct 2019. URL: https://doi.org/10.1007/s11104-019-04307-3, doi:10.1007/s11104-019-04307-3. This article has 37 citations and is from a domain leading peer-reviewed journal.