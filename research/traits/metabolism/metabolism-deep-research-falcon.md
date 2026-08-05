---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:27:20.856569'
end_time: '2026-08-04T06:34:58.082235'
duration_seconds: 457.23
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: metabolism
  trait_identifier: METPO:1000060
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: metabolism
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biological process that maintains life in an organism.
  parent_traits: METPO:1000630
  synonyms: ''
  evidence_summary: 'DOI:10.1126/science.1238842: energy and microbial life (Microbial-energetics
    review supports metabolism as the energy and material-flow process maintaining
    microbial life.) | DOI:10.1146/annurev.biochem.71.110601.135503: ATP synthesis
    (ATP-energetics review supports energy conservation as the central output of catabolic
    metabolism.)'
  causal_graph_summary: 'metabolism_substrate_to_growth: 14 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** metabolism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000060
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biological process that maintains life in an organism.
- **Parent traits:** METPO:1000630
- **Synonyms:** 
- **Existing evidence:** DOI:10.1126/science.1238842: energy and microbial life (Microbial-energetics review supports metabolism as the energy and material-flow process maintaining microbial life.) | DOI:10.1146/annurev.biochem.71.110601.135503: ATP synthesis (ATP-energetics review supports energy conservation as the central output of catabolic metabolism.)
- **Existing causal graph summary:** metabolism_substrate_to_growth: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/metabolism.yaml`.

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
- **Trait label:** metabolism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000060
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biological process that maintains life in an organism.
- **Parent traits:** METPO:1000630
- **Synonyms:** 
- **Existing evidence:** DOI:10.1126/science.1238842: energy and microbial life (Microbial-energetics review supports metabolism as the energy and material-flow process maintaining microbial life.) | DOI:10.1146/annurev.biochem.71.110601.135503: ATP synthesis (ATP-energetics review supports energy conservation as the central output of catabolic metabolism.)
- **Existing causal graph summary:** metabolism_substrate_to_growth: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/metabolism.yaml`.

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


# Curation report: microbial metabolism

## Executive scope

**Target trait:** `METPO:1000060` (“metabolism”; category **METABOLISM**, term kind **CLASS**, reviewed; parent `METPO:1000630`). For TraitMech, the most defensible interpretation is the organism-level process/capacity by which a microbe transforms matter and conserves energy through coupled catabolic, anabolic, transport, and bioenergetic reactions. ATP is the principal extant energy currency, while substrate-level phosphorylation and chemiosmotic coupling are the two broadly conserved routes of ATP synthesis. (seto2020howthermodynamicsilluminates pages 4-6, nicholls2023onthepotential pages 1-2)

The graph should not equate metabolism with growth. Growth is a downstream, condition-dependent outcome of metabolic flux plus biomass assembly, maintenance, regulation, and stress costs. Likewise, respiration, fermentation, substrate utilization, trophic mode, metabolite production, and cross-feeding are components or neighboring phenotypes—not synonyms for the broad trait. Metabolism may be observed by substrate disappearance, product formation, ATP or redox changes, isotope incorporation, metabolite profiles, flux estimates, or growth, but no single assay fully defines it.

## Trait boundaries

**Include:** nutrient acquisition; central carbon pathways; oxidation–reduction reactions; electron carriers; respiratory or fermentative energy conservation; ion gradients; ATP formation; precursor/cofactor generation; biosynthesis; waste/product export; and environmental constraints on reaction feasibility.

**Do not automatically include:**

- **Growth rate or biomass yield:** downstream phenotypes influenced by metabolism but also maintenance and regulation.
- **A specific substrate-utilization trait:** narrower than metabolism and conditional on transport plus pathway expression.
- **Aerobicity/anaerobicity:** environmental or respiratory strategy descriptors.
- **Metabolite abundance alone:** a pool-size measurement, not reaction direction or flux. A metabolite can participate in multiple pathways, and increased abundance can reflect increased production or decreased consumption. (go2024integrationofmetabolomics pages 1-3, go2024integrationofmetabolomics pages 3-4)
- **Community co-occurrence:** it does not establish causal metabolic interaction. Reductionist experiments, genetics, isotope tracing, or validated models are needed. (pacheco2023resolvingmetabolicinteraction pages 3-4)
- **Signaling and antimicrobial interactions:** include only when the molecule is explicitly used as an energy/nutrient source or directly changes a curated metabolic mechanism; a recent review treats signaling and antimicrobial roles separately from resource exchange. (pacheco2023resolvingmetabolicinteraction pages 3-4)

## Candidate nodes grouped by type

Identifiers below are conservative suggestions; label-only nodes should remain ungrounded until checked against the project’s ontology release.

### Trait and biological-process nodes

- Metabolism — `METPO:1000060`; broad GO analogue `GO:0008152`.
- Glycolytic process — `GO:0006096`.
- Tricarboxylic acid cycle — `GO:0006099`.
- Oxidative phosphorylation — `GO:0006119`.
- ATP synthesis coupled proton transport — `GO:0015986`.
- Aerobic respiration — `GO:0009060`.
- Substrate-level phosphorylation — label-only candidate.
- Fermentation — use an appropriately specific GO term only after pathway/taxon is known.
- Chemiosmosis, catabolism, anabolism, biomass synthesis, maintenance metabolism, metabolite cross-feeding — label-only or ontology-check candidates.

### Chemicals, nutrients, and physical drivers

- ATP — `CHEBI:15422`; ADP — `CHEBI:16761`; phosphate — `CHEBI:43474`.
- NADH — `CHEBI:16908`; NAD+ — `CHEBI:57540`.
- Ubiquinone — `CHEBI:16389`; ubiquinol — `CHEBI:17976`.
- Proton — `CHEBI:15378`; water — `CHEBI:15377`; dioxygen — `CHEBI:15379`.
- Carbon dioxide — `CHEBI:16526`; dihydrogen — `CHEBI:18276`.
- Acetate — `CHEBI:30089`; ethanol — `CHEBI:16236`.
- Sodium ion — `CHEBI:29101`; potassium ion — `CHEBI:29103`.
- Glucose 6-phosphate — `CHEBI:4170`.
- Electron donor, terminal electron acceptor, carbon source, nitrogen source, trace nutrient, proton-motive force, sodium-motive force, Gibbs free-energy change, and minimum driving force — label-only candidates where a stable ontology mapping has not been verified.

### Proteins, enzymes, transporters, and complexes

- Respiratory complex I / proton-translocating NADH:quinone oxidoreductase; bacterial core usually has 13–14 subunits, including an NADH-oxidizing N module, quinone-associated Q module, and membrane proton-translocating P module. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 2-4)
- F-type H+-transporting ATP synthase and Na+-coupled F1Fo ATP synthase — ontology/EC mapping should be selected after ion specificity and taxon are known.
- Rnf reduced-ferredoxin:NAD+ oxidoreductase — label-only candidate unless the organism’s characterized complex is specified.
- Electron-bifurcating [FeFe]-hydrogenase; ferredoxin; Nfn transhydrogenase; acetaldehyde:ferredoxin oxidoreductase; acetate kinase; substrate transporters; terminal oxidases/reductases.
- Taxon-specific gene nodes such as bacterial `nuo` genes should be added only with strain-level evidence or a genome annotation accession.

### Cellular locations and environmental nodes

- Cytoplasmic/plasma membrane, cytoplasm, periplasm, extracellular environment, and—only for microbial eukaryotes—mitochondrion or chloroplast.
- Oxic/anoxic condition, substrate concentration, H2 partial pressure, pH, temperature, salinity, and nutrient limitation.
- Do not add an organelle node to a bacterial graph merely because a review discusses homologous mitochondrial machinery.

## Candidate causal edges

The table separates broadly reusable edges from taxon-, assay-, and model-specific propositions. Quoted text is intentionally short.

| # | Subject–predicate–object | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|
| 1 | NADH — **is oxidized by / donates electrons to** — respiratory complex I | DOI [10.3390/ijms252413421](https://doi.org/10.3390/ijms252413421), published 14 Dec 2024 | “primary enzymes that catalyze the oxidation of NADH by ubiquinone” | **High confidence.** Broad for organisms possessing canonical complex I; absence of complex I must not imply absence of respiration. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)
| 2 | Respiratory complex I — **reduces** — quinone | Same | “electron transfer from NADH to a natural quinone electron acceptor” | **High confidence**, but the quinone species varies: bacteria may use ubiquinone or menaquinone. Prefer generic quinone unless experimentally resolved. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 2-4)
| 3 | Respiratory complex I — **translocates across membrane** — four H+ per catalytic turnover | Same | oxidation is “accompanied by the transmembrane transfer of four protons” | **High confidence for canonical complex I stoichiometry.** Store “4 H+” as a qualified stoichiometric annotation rather than an unqualified universal edge. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)
| 4 | Respiratory complex I — **contributes to formation of** — proton-motive force | Same | “energy conservation in the form of an electrochemical gradient…(proton motive force)” | **High confidence** for proton-translocating complex I. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)
| 5 | Proton-motive force — **drives** — ATP synthesis in oxidative phosphorylation | Same | pmf “drives ATP synthesis in oxidative phosphorylation” | **High confidence.** Add ATP synthase as mediator when graph granularity permits. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)
| 6 | Oxidative decomposition of carbohydrates/fatty acids/proteins — **produces** — NADH | Same | “NADH formed during the oxidative decomposition of carbohydrates, fatty acids, and proteins” | **High confidence as a broad summary**, but individual pathway reactions should replace this aggregate edge in a detailed graph. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)
| 7 | Complex-I-dependent NADH oxidation — **maintains** — NAD+/NADH ratio supporting central catabolic turnover | Same | “maintains the physiological NAD+/NADH ratio necessary for an efficient turnover” of glycolysis, TCA cycle, and β-oxidation | **Moderate–high.** Context depends on the respiratory architecture and carbon source. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)
| 8 | Substrate-level phosphorylation — **synthesizes** — ATP | DOI [10.3389/fevo.2020.602809](https://doi.org/10.3389/fevo.2020.602809), Nov 2020; DOI [10.3389/fmicb.2023.1239189](https://doi.org/10.3389/fmicb.2023.1239189), 2 Aug 2023 | ATP is synthesized by “substrate-level phosphorylation (SLP) or chemiosmotic coupling” | **High confidence.** Keep distinct from fermentation: SLP occurs in fermentative pathways but is not synonymous with fermentation. (seto2020howthermodynamicsilluminates pages 4-6, nicholls2023onthepotential pages 1-2)
| 9 | ATP — **drives** — energetically unfavorable metabolic reactions | DOI 10.3389/fmicb.2023.1239189 | ATP supports “storage, transfer, and release of cellular energy, driving unfavorable metabolic reactions” | **High confidence** but broad; connect ATP to specific biosynthetic reactions when possible. (nicholls2023onthepotential pages 1-2)
| 10 | Thermodynamic driving force / metabolite concentrations — **constrain** — pathway feasibility and energy yield | DOI [10.1101/2023.02.13.528271](https://doi.org/10.1101/2023.02.13.528271), Feb 2023 record | Method evaluates feasibility by optimizing energy yield and driving forces as functions of intermediate concentrations | **Computational/theoretical evidence.** Curate as a conditional regulatory/constraint edge, not as a direct molecular reaction. Carrier choice and proton-translocating steps alter predicted feasibility. (taha2023optimalevaluationof pages 24-28, taha2023optimalevaluationof pages 1-4)
| 11 | Reduced ferredoxin oxidation by Rnf — **builds** — Na+ electrochemical potential | DOI [10.1128/JB.00399-15](https://doi.org/10.1128/JB.00399-15), posted 6 Jul 2015 | Rnf reduction of NAD+ is “associated with the buildup of an electrochemical sodium ion potential” | **Taxon/pathway-specific.** Evidence describes acetogen energetics, especially *Acetobacterium woodii*; do not generalize to all microbes or all Rnf complexes. (mock2015energyconservationassociated pages 1-5)
| 12 | Na+ electrochemical potential — **drives** — ADP phosphorylation by F1Fo ATP synthase | Same | potential “drives the phosphorylation of ADP via the F1Fo ATP synthase complex” | **Taxon-specific.** Reported values were 1 Na+ translocated per electron and 3.3 Na+ per ATP in the cited scheme. (mock2015energyconservationassociated pages 1-5)
| 13 | H2 partial pressure — **modulates** — ATP yield of H2/CO2-to-ethanol metabolism | Same | schemes allow “0.14 to 1.5 mol ATP per mol ethanol” depending on H2 partial pressure | **Uncertain/generalization warning.** Mechanistic proposal for *Clostridium autoethanogenum*, supported by enzyme, transcriptional, mutational, and thermodynamic analyses—not a universal yield. (mock2015energyconservationassociated pages 1-5)
| 14 | Sphingomonas-derived dethiobiotin — **facilitates growth of** — a Rhizobium strain | DOI [10.1016/j.mib.2023.102317](https://doi.org/10.1016/j.mib.2023.102317), Aug 2023 review | “vitamin cross-feeding…Sphingomonas…facilitate[d] the growth of a Rhizobium strain via…dethiobiotin” | **Community-, strain-, and host-context specific.** Strong candidate only if the primary study is obtained before YAML curation. (pacheco2023resolvingmetabolicinteraction pages 3-4)
| 15 | Antibiotic removal of bile-acid 7α-dehydroxylating bacteria — **permits** — *C. difficile* proliferation | DOI [10.1007/s00253-024-13384-z](https://doi.org/10.1007/s00253-024-13384-z), published 19 Dec 2024 review | after antibiotics, “C. difficile proliferated due to the elimination” of these bacteria | **Indirect, community-level edge.** Mechanism includes bile-acid conversion and tryptophan-derived antibiotics; obtain primary causal papers before graph insertion. (go2024integrationofmetabolomics pages 3-4)
| 16 | Metatranscriptomic constraints — **improve contextualization of** — community metabolic flux models | DOI [10.1016/j.crmeth.2022.100383](https://doi.org/10.1016/j.crmeth.2022.100383), published 23 Jan 2023 | integration “better capture[s] metabolic activity” in anaerobic digestion and gut communities | **Model/assay edge**, not a biological causal edge. Keep in provenance or evidence methodology rather than the organismal graph. (zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 1-3)
| 17 | 13C/15N-labeled substrate uptake — **causes** — isotopic enrichment detectable by NanoSIMS | DOI [10.1038/s43586-024-00311-9](https://doi.org/10.1038/s43586-024-00311-9), May 2024 | labeled compounds “track uptake and metabolic products”; FISH–SIMS can “link identity with metabolic function” | **Assay-observation edge.** Isotope enrichment supports assimilation/activity, not necessarily pathway identity or net flux without controls. (lockyer2024secondaryionmass pages 22-24)

The highest-confidence subset suitable for initial YAML implementation is summarized here:

| Subject | Predicate | Object | Grounding | Evidence DOI | Confidence/context |
|---|---|---|---|---|---|
| NADH | electron donor for | respiratory complex I | CHEBI:16908; label: respiratory complex I | 10.3390/ijms252413421 (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | High; review states complex I catalyzes oxidation of NADH by ubiquinone |
| respiratory complex I | reduces | quinone | label: respiratory complex I; label: quinone | 10.3390/ijms252413421 (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 2-4) | High; bacterial complex I transfers electrons from NADH to natural quinone acceptor |
| respiratory complex I | translocates | 4 H+ | label: respiratory complex I; CHEBI:15378 | 10.3390/ijms252413421 (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | High; exact review statement says transfer of four protons |
| proton motive force | drives | ATP synthesis | CHEBI:57540; GO:0015986 | 10.3390/ijms252413421 (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | High; general oxidative phosphorylation mechanism in bacteria and mitochondria |
| ATP | powers | unfavorable metabolic reactions | CHEBI:15422 | 10.3389/fmicb.2023.1239189 (nicholls2023onthepotential pages 1-2) | High; review states ATP drives unfavorable metabolic reactions and phosphorylates metabolites |
| substrate-level phosphorylation | synthesizes | ATP | label: substrate-level phosphorylation; CHEBI:15422 | 10.3389/fevo.2020.602809 (seto2020howthermodynamicsilluminates pages 4-6), 10.3389/fmicb.2023.1239189 (nicholls2023onthepotential pages 1-2) | High; broad bioenergetic mechanism, not trait-specific to one taxon |
| chemiosmosis | synthesizes | ATP | label: chemiosmosis; CHEBI:15422 | 10.3389/fevo.2020.602809 (seto2020howthermodynamicsilluminates pages 4-6), 10.3389/fmicb.2023.1239189 (nicholls2023onthepotential pages 1-2) | High; broad bioenergetic mechanism via ion gradient and ATP synthase |
| Rnf complex | builds | sodium motive force | label: Rnf complex; label: sodium motive force | 10.1128/JB.00399-15 (mock2015energyconservationassociated pages 1-5) | Medium-high; explicit for acetogens and A. woodii scheme, not universal |
| sodium motive force | drives | F1Fo ATP synthase | label: sodium motive force; label: F1Fo ATP synthase | 10.1128/JB.00399-15 (mock2015energyconservationassociated pages 1-5) | Medium-high; acetogen-specific energy conservation scheme |
| metabolite cross-feeding | modulates | partner growth | label: metabolite cross-feeding; label: partner growth | 10.1016/j.mib.2023.102317 (pacheco2023resolvingmetabolicinteraction pages 3-4, pacheco2023resolvingmetabolicinteraction pages 1-3) | Medium; community- and system-specific, depends on exchanged metabolite |


*Table: This table summarizes the strongest, most curation-ready causal edges for microbial metabolism, emphasizing broadly applicable bioenergetic links and clearly marking taxon- or community-specific claims.*

## Recommended graph architecture

A compact, reusable core would be:

1. **Environmental substrate availability** → enables **transport/uptake**.
2. Uptake → supplies **catabolic pathway**.
3. Catabolism → produces **reduced electron carrier** and precursor metabolites.
4. NADH → donates electrons to **complex I**.
5. Complex I → reduces **quinone** and translocates H+.
6. H+ translocation → establishes **proton-motive force**.
7. Proton-motive force → drives **ATP synthase** → ATP.
8. In parallel, suitable catabolic intermediates → **substrate-level phosphorylation** → ATP.
9. ATP + reducing power + precursors → enable **anabolic/maintenance reactions**.
10. Anabolic flux, after maintenance demands are met → supports **biomass formation/growth**.
11. Environmental concentrations and Gibbs free energy → constrain feasible direction, ATP yield, and pathway choice.

Branches should represent alternative respiratory acceptors, fermentation, phototrophy, methanogenesis, acetogenesis, and ion specificity rather than forcing every microbe through oxygen, ubiquinone, or proton-coupled complex I.

## Recent developments and applications (2023–2024)

### Condition-specific community metabolic models

Zampieri and colleagues integrated genome-centric metatranscriptomes with genome-scale metabolic models rather than relying only on genomic potential. Their culture-independent workflow modeled anaerobic digestion consortia and human gut microbiota, identifying hydrogen-dependent syntrophic responses, archaeal amino-acid requirements, and a reduced short-chain-fatty-acid exchange network associated with Crohn’s disease. The authors emphasize that genome content can be “scarcely indicative of real functional activity,” supporting transcript-aware rather than gene-presence-only graph evidence. (zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 1-3, zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 3-4)

### Multi-omics rather than metabolite-pool inference

A December 2024 review stresses that no current analytical method captures all metabolites simultaneously and that pool sizes cannot uniquely identify the responsible reaction. It reports that *E. coli* and *Saccharomyces cerevisiae* are predicted to possess thousands of metabolites, yet approximately **700** and **500**, respectively, had been identified in the cited datasets. The recommended direction is integration with genomics, transcriptomics, proteomics, or fluxomics to reduce false positives and false negatives. (go2024integrationofmetabolomics pages 1-3, go2024integrationofmetabolomics pages 3-4)

### Single-cell and spatial metabolic activity

The 2024 SIMS methods primer reports elemental SIMS spatial resolution below **50 nm**, molecular depth information below **10 nm** in suitable applications, and routine use of 13C/15N labels to trace uptake and products. In microbiology, NanoSIMS has been applied to iron redox processes, nitrogen fixation, and syntrophic interactions; combining FISH with high-resolution SIMS links taxonomic identity to activity. Matrix effects and low molecular secondary-ion yields—approximately **10^-3 to 10^-5**, versus roughly **10^-2** for elemental ions under reactive beams—remain major quantitative limitations. (lockyer2024secondaryionmass pages 22-24, lockyer2024secondaryionmass pages 1-5)

### Mechanism-guided microbiome engineering

Plant-microbiome research increasingly combines community sequencing, isolate phenotyping, synthetic-community drop-in/drop-out designs, genetics, metabolomics, and models. Reported culture collections recover around **50%** of operational taxonomic units in representative studies, illustrating both progress and residual uncultured diversity. Applications include predictive community assembly, plant protection, bioremediation, sustainable agriculture, pathogen suppression, and nutrient cycling. (pacheco2023resolvingmetabolicinteraction pages 1-3)

### Industrial gas fermentation

*Clostridium autoethanogenum* is used industrially to ferment syngas or steel-manufacturing off-gases. A mechanistic study linked the Wood–Ljungdahl pathway, electron bifurcation, Rnf/Nfn systems, and ATP conservation to ethanol production, predicting **0.14–1.5 mol ATP per mol ethanol** depending on H2 partial pressure. This is a valuable implementation case but should remain a taxon- and condition-qualified branch. (mock2015energyconservationassociated pages 1-5)

## Expert synthesis

The literature supports treating metabolism as a **causal network constrained by mass balance, redox balance, thermodynamics, enzyme capacity, and environmental availability**, not as a binary annotation. The strongest universal layer is energy/material transformation; respiratory machinery and products are modular and taxon dependent. Thermodynamic optimization studies further show a yield–driving-force/rate trade-off: maximizing ATP recovery can reduce reaction driving force and increase enzyme demand, so “highest theoretical yield” is not necessarily the physiologically selected pathway. (taha2023optimalevaluationof pages 24-28, taha2023optimalevaluationof pages 1-4)

For evidence grading, direct biochemical perturbation and isotope-resolved flux should rank above metabolite abundance, transcript abundance, genome annotation, or unconstrained model prediction. Metatranscriptomics can improve condition specificity, but RNA abundance remains a modeling constraint rather than proof of flux. Co-occurrence is hypothesis-generating only. (zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 1-3, pacheco2023resolvingmetabolicinteraction pages 3-4)

## Claims not yet ready for TraitMech curation

1. **Metabolite concentration → pathway activation.** Direction is ambiguous; G6P, for example, participates in glycolysis, gluconeogenesis, and the pentose-phosphate pathway. (go2024integrationofmetabolomics pages 1-3, go2024integrationofmetabolomics pages 3-4)
2. **Gene presence → active metabolism.** Genomes encode potential, not condition-specific activity. (zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 1-3)
3. **Transcript abundance → reaction flux.** Useful as a constraint, but post-transcriptional regulation, enzyme kinetics, substrate availability, and thermodynamics intervene.
4. **Co-occurrence → cross-feeding or competition.** Experimental validation is required. (pacheco2023resolvingmetabolicinteraction pages 3-4)
5. **Oxygen as the universal terminal acceptor.** Many microbes respire alternative acceptors or ferment; complex-I/oxygen edges need pathway qualifiers.
6. **Four H+ per complex-I turnover as universal across every homolog/condition.** Strong for canonical complex I, but divergent enzymes and uncoupling require care.
7. **Rnf always establishes a Na+ gradient.** Ion specificity is organism dependent; the cited stoichiometry is acetogen-specific. (mock2015energyconservationassociated pages 1-5)
8. **Growth as a direct synonym or necessary observation of metabolism.** Nongrowing cells can retain maintenance or transformation activity.
9. **NanoSIMS enrichment as proof of a specific pathway.** It establishes label uptake/localization; pathway assignment requires labeled-substrate design, controls, and complementary evidence. (lockyer2024secondaryionmass pages 22-24)
10. **Review-reported dethiobiotin or bile-acid edges as final primary evidence.** Retrieve and curate the underlying experimental papers first.

## DOI-first bibliography

1. Grivennikova VG et al. “Proton-Translocating NADH–Ubiquinone Oxidoreductase.” *International Journal of Molecular Sciences* 25, 13421. **Published 14 December 2024.** DOI: [10.3390/ijms252413421](https://doi.org/10.3390/ijms252413421). (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 2-4, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)
2. Go D et al. “Integration of metabolomics and other omics: from microbes to microbiome.” *Applied Microbiology and Biotechnology* 108:538. **Published online 19 December 2024.** DOI: [10.1007/s00253-024-13384-z](https://doi.org/10.1007/s00253-024-13384-z). (go2024integrationofmetabolomics pages 1-3, go2024integrationofmetabolomics pages 3-4)
3. Lockyer NP et al. “Secondary ion mass spectrometry.” *Nature Reviews Methods Primers* 4:32. **May 2024.** DOI: [10.1038/s43586-024-00311-9](https://doi.org/10.1038/s43586-024-00311-9). (lockyer2024secondaryionmass pages 22-24, lockyer2024secondaryionmass pages 1-5)
4. Zampieri G et al. “Metatranscriptomics-guided genome-scale metabolic modeling of microbial communities.” *Cell Reports Methods* 3:100383. **23 January 2023.** DOI: [10.1016/j.crmeth.2022.100383](https://doi.org/10.1016/j.crmeth.2022.100383). (zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 1-3, zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 3-4)
5. Pacheco AR, Vorholt JA. “Resolving metabolic interaction mechanisms in plant microbiomes.” *Current Opinion in Microbiology* 74:102317. **August 2023.** DOI: [10.1016/j.mib.2023.102317](https://doi.org/10.1016/j.mib.2023.102317). (pacheco2023resolvingmetabolicinteraction pages 3-4, pacheco2023resolvingmetabolicinteraction pages 1-3)
6. Nicholls JWF et al. “On the potential roles of phosphorus in the early evolution of energy metabolism.” *Frontiers in Microbiology* 14:1239189. **2 August 2023.** DOI: [10.3389/fmicb.2023.1239189](https://doi.org/10.3389/fmicb.2023.1239189). (nicholls2023onthepotential pages 1-2)
7. Taha A et al. “Optimal evaluation of energy yield and driving force in microbial metabolic pathway variants.” **February 2023 record.** DOI available in retrieved record: [10.1101/2023.02.13.528271](https://doi.org/10.1101/2023.02.13.528271). **Bibliographic warning:** this DOI is a bioRxiv identifier even though the retrieval metadata labels the venue PLOS Computational Biology; verify the final journal DOI before production curation. (taha2023optimalevaluationof pages 24-28, taha2023optimalevaluationof pages 1-4)
8. Mock J et al. “Energy Conservation Associated with Ethanol Formation from H2 and CO2 in *Clostridium autoethanogenum* Involving Electron Bifurcation.” *Journal of Bacteriology* 197:2965–2980. **Posted 6 July 2015.** DOI: [10.1128/JB.00399-15](https://doi.org/10.1128/JB.00399-15). (mock2015energyconservationassociated pages 1-5)
9. Seto M, Iwasa Y. “How Thermodynamics Illuminates Population Interactions in Microbial Communities.” *Frontiers in Ecology and Evolution* 8. **November 2020.** DOI: [10.3389/fevo.2020.602809](https://doi.org/10.3389/fevo.2020.602809). (seto2020howthermodynamicsilluminates pages 4-6)

**Curation recommendation:** begin `metabolism.yaml` with the high-confidence energy-conservation spine (catabolic reducing equivalents → complex I/alternative electron-transfer module → ion gradient → ATP synthase → ATP-supported cellular work), represent substrate-level phosphorylation as a parallel route, and attach explicit taxon/environment/evidence qualifiers to every respiratory acceptor, quinone, ion-coupling, fermentation, and community-exchange branch.

References

1. (seto2020howthermodynamicsilluminates pages 4-6): Mayumi Seto and Yoh Iwasa. How thermodynamics illuminates population interactions in microbial communities. Frontiers in Ecology and Evolution, Nov 2020. URL: https://doi.org/10.3389/fevo.2020.602809, doi:10.3389/fevo.2020.602809. This article has 7 citations and is from a peer-reviewed journal.

2. (nicholls2023onthepotential pages 1-2): Jack W. F. Nicholls, Jason P. Chin, Tom A. Williams, Timothy M. Lenton, Vincent O’Flaherty, and John W. McGrath. On the potential roles of phosphorus in the early evolution of energy metabolism. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1239189, doi:10.3389/fmicb.2023.1239189. This article has 68 citations and is from a peer-reviewed journal.

3. (go2024integrationofmetabolomics pages 1-3): Daewon Go, Gun-Hwi Yeon, Soo Jin Park, Yujin Lee, Hyun Gi Koh, Hyunjin Koo, Kyoung Heon Kim, Yong-Su Jin, Bong Hyun Sung, and Jungyeon Kim. Integration of metabolomics and other omics: from microbes to microbiome. Applied Microbiology and Biotechnology, Dec 2024. URL: https://doi.org/10.1007/s00253-024-13384-z, doi:10.1007/s00253-024-13384-z. This article has 40 citations and is from a domain leading peer-reviewed journal.

4. (go2024integrationofmetabolomics pages 3-4): Daewon Go, Gun-Hwi Yeon, Soo Jin Park, Yujin Lee, Hyun Gi Koh, Hyunjin Koo, Kyoung Heon Kim, Yong-Su Jin, Bong Hyun Sung, and Jungyeon Kim. Integration of metabolomics and other omics: from microbes to microbiome. Applied Microbiology and Biotechnology, Dec 2024. URL: https://doi.org/10.1007/s00253-024-13384-z, doi:10.1007/s00253-024-13384-z. This article has 40 citations and is from a domain leading peer-reviewed journal.

5. (pacheco2023resolvingmetabolicinteraction pages 3-4): Alan R. Pacheco and Julia A. Vorholt. Resolving metabolic interaction mechanisms in plant microbiomes. Aug 2023. URL: https://doi.org/10.1016/j.mib.2023.102317, doi:10.1016/j.mib.2023.102317. This article has 18 citations and is from a peer-reviewed journal.

6. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 2-4): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 10 citations.

7. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 10 citations.

8. (taha2023optimalevaluationof pages 24-28): Ahmed Taha, David R Penas, Mauricio Patón, Julio R Banga, and Jorge Rodríguez. Optimal evaluation of energy yield and driving force in microbial metabolic pathway variants. PLOS Computational Biology, Feb 2023. URL: https://doi.org/10.1101/2023.02.13.528271, doi:10.1101/2023.02.13.528271. This article has 9 citations and is from a highest quality peer-reviewed journal.

9. (taha2023optimalevaluationof pages 1-4): Ahmed Taha, David R Penas, Mauricio Patón, Julio R Banga, and Jorge Rodríguez. Optimal evaluation of energy yield and driving force in microbial metabolic pathway variants. PLOS Computational Biology, Feb 2023. URL: https://doi.org/10.1101/2023.02.13.528271, doi:10.1101/2023.02.13.528271. This article has 9 citations and is from a highest quality peer-reviewed journal.

10. (mock2015energyconservationassociated pages 1-5): Johanna Mock, Yanning Zheng, Alexander P. Mueller, San Ly, Loan Tran, Simon Segovia, Shilpa Nagaraju, Michael Köpke, Peter Dürre, and Rudolf K. Thauer. Energy conservation associated with ethanol formation from h <sub>2</sub> and co <sub>2</sub> in clostridium autoethanogenum involving electron bifurcation. Journal of Bacteriology, 197:2965-2980, Sep 2015. URL: https://doi.org/10.1128/jb.00399-15, doi:10.1128/jb.00399-15. This article has 287 citations and is from a peer-reviewed journal.

11. (zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 1-3): Guido Zampieri, Stefano Campanaro, Claudio Angione, and Laura Treu. Metatranscriptomics-guided genome-scale metabolic modeling of microbial communities. Cell Reports Methods, 3:100383, Jan 2023. URL: https://doi.org/10.1016/j.crmeth.2022.100383, doi:10.1016/j.crmeth.2022.100383. This article has 92 citations.

12. (lockyer2024secondaryionmass pages 22-24): Nicholas P. Lockyer, Satoka Aoyagi, John S. Fletcher, Ian S. Gilmore, Paul A. W. van der Heide, Katie L. Moore, Bonnie J. Tyler, and Lu-Tao Weng. Secondary ion mass spectrometry. Nature Reviews Methods Primers, May 2024. URL: https://doi.org/10.1038/s43586-024-00311-9, doi:10.1038/s43586-024-00311-9. This article has 122 citations and is from a peer-reviewed journal.

13. (pacheco2023resolvingmetabolicinteraction pages 1-3): Alan R. Pacheco and Julia A. Vorholt. Resolving metabolic interaction mechanisms in plant microbiomes. Aug 2023. URL: https://doi.org/10.1016/j.mib.2023.102317, doi:10.1016/j.mib.2023.102317. This article has 18 citations and is from a peer-reviewed journal.

14. (zampieri2023metatranscriptomicsguidedgenomescalemetabolic pages 3-4): Guido Zampieri, Stefano Campanaro, Claudio Angione, and Laura Treu. Metatranscriptomics-guided genome-scale metabolic modeling of microbial communities. Cell Reports Methods, 3:100383, Jan 2023. URL: https://doi.org/10.1016/j.crmeth.2022.100383, doi:10.1016/j.crmeth.2022.100383. This article has 92 citations.

15. (lockyer2024secondaryionmass pages 1-5): Nicholas P. Lockyer, Satoka Aoyagi, John S. Fletcher, Ian S. Gilmore, Paul A. W. van der Heide, Katie L. Moore, Bonnie J. Tyler, and Lu-Tao Weng. Secondary ion mass spectrometry. Nature Reviews Methods Primers, May 2024. URL: https://doi.org/10.1038/s43586-024-00311-9, doi:10.1038/s43586-024-00311-9. This article has 122 citations and is from a peer-reviewed journal.