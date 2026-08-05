---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:24:12.593185'
end_time: '2026-08-04T05:30:59.309088'
duration_seconds: 406.72
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: anaerobic oxidation of methane
  trait_identifier: traitmech:000033
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: anaerobic_oxidation_of_methane
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which methane is oxidized under anoxic conditions, classically
    coupled to sulfate reduction and mediated by consortia of anaerobic methanotrophic
    archaea (ANME) and sulfate-reducing bacteria. It is a major sink for methane in
    marine sediments.
  parent_traits: METPO:1000802
  synonyms: AOM, anaerobic methanotrophy
  evidence_summary: 'DOI:10.1038/35036572:  (Boetius et al. described the marine microbial
    consortium of ANME archaea and sulfate-reducing bacteria mediating anaerobic oxidation
    of methane.) | DOI:10.3389/fmars.2025.1609892:  (Review of AOM in marine sediments
    supports sulfate- and metal-coupled anaerobic methane oxidation as a major methane
    sink.)'
  causal_graph_summary: 'aom_anme_sulfate_consortium: 8 nodes, 8 edges'
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
- **Trait label:** anaerobic oxidation of methane
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000033
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which methane is oxidized under anoxic conditions, classically coupled to sulfate reduction and mediated by consortia of anaerobic methanotrophic archaea (ANME) and sulfate-reducing bacteria. It is a major sink for methane in marine sediments.
- **Parent traits:** METPO:1000802
- **Synonyms:** AOM, anaerobic methanotrophy
- **Existing evidence:** DOI:10.1038/35036572:  (Boetius et al. described the marine microbial consortium of ANME archaea and sulfate-reducing bacteria mediating anaerobic oxidation of methane.) | DOI:10.3389/fmars.2025.1609892:  (Review of AOM in marine sediments supports sulfate- and metal-coupled anaerobic methane oxidation as a major methane sink.)
- **Existing causal graph summary:** aom_anme_sulfate_consortium: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **anaerobic oxidation of methane** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anaerobic_oxidation_of_methane.yaml`.

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
- **Trait label:** anaerobic oxidation of methane
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000033
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which methane is oxidized under anoxic conditions, classically coupled to sulfate reduction and mediated by consortia of anaerobic methanotrophic archaea (ANME) and sulfate-reducing bacteria. It is a major sink for methane in marine sediments.
- **Parent traits:** METPO:1000802
- **Synonyms:** AOM, anaerobic methanotrophy
- **Existing evidence:** DOI:10.1038/35036572:  (Boetius et al. described the marine microbial consortium of ANME archaea and sulfate-reducing bacteria mediating anaerobic oxidation of methane.) | DOI:10.3389/fmars.2025.1609892:  (Review of AOM in marine sediments supports sulfate- and metal-coupled anaerobic methane oxidation as a major methane sink.)
- **Existing causal graph summary:** aom_anme_sulfate_consortium: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **anaerobic oxidation of methane** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anaerobic_oxidation_of_methane.yaml`.

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


# Curation report: anaerobic oxidation of methane

## Record and scope

- **Trait:** anaerobic oxidation of methane (AOM; anaerobic methanotrophy)
- **Identifier:** `traitmech:000033`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1000802`

The trait should represent **net biological oxidation of methane under anoxic conditions**, with methane-derived electrons ultimately transferred to an external acceptor. The canonical marine form couples methane oxidation by anaerobic methanotrophic archaea (ANME) to sulfate reduction, usually by a syntrophic sulfate-reducing bacterial partner. Other accepted subtypes use nitrate, nitrite, metal oxides, humic compounds, or experimentally supplied electrodes. Mechanistically, archaeal AOM generally begins with methyl-coenzyme M reductase (MCR) operating in the oxidative direction and proceeds through a reversed, modified methanogenesis pathway to CO₂/HCO₃⁻. All eight electrons released by complete methane oxidation must be discharged to terminal acceptors. (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48, timmers2017reversemethanogenesisand pages 1-2)

### Boundary cases

1. **Exclude aerobic methane oxidation.** Canonical aerobic methanotrophs activate methane with methane monooxygenase and oxygen-derived chemistry, whereas archaeal AOM uses MCR/F430. Nitrite-dependent *Candidatus Methylomirabilis* is a special boundary case: the environment is anoxic, but internally generated O₂ supports methane monooxygenase chemistry. It is appropriately treated as an AOM subtype, while preserving this mechanistic distinction. (scheller2020catabolicpathwaysand pages 45-48)
2. **Exclude methanogenesis and trace methane oxidation.** Methanogens can oxidize a small amount of methane while remaining net methane producers; ANME can likewise display backward methane-forming flux during net oxidation. Only **net methane consumption** establishes the trait. (timmers2017reversemethanogenesisand pages 12-14, timmers2017reversemethanogenesisand pages 1-2)
3. **Exclude non-methane alkane oxidation.** Ethane-, propane-, butane-, and longer-alkane activation by divergent alkyl-coenzyme M reductases is a neighboring but separate trait.
4. **Do not infer AOM from `mcrA` alone.** MCR is reversible and occurs in methanogens as well as ANME; directionality requires physiology, isotopic flux, environmental context, or a sufficiently resolved pathway/taxon assignment.
5. **Electron-acceptor branches are not universal attributes.** Sulfate-, nitrate-, nitrite-, metal-, humic-, and electrode-dependent AOM should be modeled as subgraphs rather than asserting that every AOM organism uses every acceptor. (zhang2021anaerobicoxidationof pages 8-9, zhang2021anaerobicoxidationof pages 5-5, timmers2017reversemethanogenesisand pages 1-2)

## Candidate nodes

### Trait, pathways, and processes

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| anaerobic oxidation of methane | trait/process | `traitmech:000033` | Root trait node; quote identifier verbatim. |
| reverse methanogenesis | pathway | Label-only candidate | Core archaeal carbon-oxidation module. |
| sulfate-coupled AOM | metabolic subtype | Label-only candidate | Canonical marine branch. |
| nitrate-dependent AOM | metabolic subtype | Label-only candidate | Primarily *Ca. Methanoperedens*; taxon-specific. |
| nitrite-dependent AOM | metabolic subtype | Label-only candidate | Primarily *Ca. Methylomirabilis*; intra-aerobic mechanism. |
| metal-dependent AOM | metabolic subtype | Label-only candidate | Separate Fe(III) and Mn(IV) branches where evidence permits. |
| extracellular electron transfer | process | GO grounding should be verified before use | Includes transfer to minerals, humics, partners, or electrodes. |
| direct interspecies electron transfer | process | Label-only candidate | Mechanism candidate, not universal. |
| sulfate reduction | process | GO term should be verified | Usually assigned to the bacterial partner. |
| nitrate/nitrite reduction | process | GO terms should be verified | Keep separate because organisms and products differ. |

### Genes, proteins, cofactors, and complexes

| Candidate node | Type | Suggested grounding | Role |
|---|---|---|---|
| methyl-coenzyme M reductase | enzyme complex | `EC:2.8.4.1` | Activates methane in archaeal AOM; enzyme is an α₂β₂γ₂ complex. |
| `mcrA`, `mcrB`, `mcrG` | genes/subunits | Gene symbols; taxon-specific accessions preferred | Encode MCR α, β, and γ subunits. |
| coenzyme F430 | prosthetic group | ChEBI identifier should be independently verified | Nickel hydrocorphin at the MCR active site. |
| coenzyme M | cofactor/substrate | ChEBI identifier should be independently verified | Accepts the methane-derived methyl group. |
| coenzyme B | cofactor | ChEBI identifier should be independently verified | Participates in MCR/heterodisulfide chemistry. |
| CoM-S-S-CoB | metabolite | ChEBI identifier should be independently verified | Heterodisulfide redox intermediate. |
| heterodisulfide reductase | enzyme complex | EC/KEGG grounding should be verified by lineage | Reversed electron-flow component of archaeal AOM. |
| tetrahydromethanopterin | C1 carrier | ChEBI identifier should be independently verified | Carries successively oxidized C1 intermediates. |
| coenzyme F420 | redox cofactor | ChEBI identifier should be independently verified | Supports reverse-methanogenesis redox reactions. |
| multiheme c-type cytochrome | electron-transfer protein | Protein-family or taxon-specific accession preferred | Candidate EET conduit in several ANME lineages. |
| nitrate reductase | enzyme complex | Taxon-specific Nar accessions preferred | Reduces nitrate to nitrite in nitrate-dependent AOM. |
| methane monooxygenase | enzyme | `EC:1.14.18.3` for particulate MMO; verify exact form | Used by *Methylomirabilis*, not by canonical archaeal AOM. |
| putative nitric oxide dismutase | enzyme candidate | Label-only | Proposed source of intracellular O₂; direct molecular assignment remains unsettled. |

MCR with nickel-containing F430 cleaves methane’s C–H bond and transfers the methyl group to coenzyme M; the carbon is then oxidized through tetrahydromethanopterin-linked reverse methanogenesis to CO₂. This is the strongest molecular anchor for the graph. (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48)

### Chemicals and environmental factors

High-confidence chemical nodes include methane, CO₂/HCO₃⁻, sulfate, sulfide/HS⁻, nitrate, nitrite, nitric oxide, O₂, N₂, Fe(III), Fe(II), Mn(IV), reduced manganese, humic substances, AQDS, and conductive electrodes. Stable ChEBI identifiers should be resolved from the ontology during implementation rather than copied from memory.

Environmental nodes include anoxic conditions, marine sediment, sulfate–methane transition zone, freshwater sediment, wetland, aquifer, paddy soil, wastewater biofilm, methane availability, terminal-electron-acceptor availability, conductive material, and oxygen exposure. Oxygen is chiefly an exclusion/inhibitory factor for canonical ANME, although some lineages tolerate transient exposure and *Methylomirabilis* generates oxygen internally.

### Organisms and consortia

- **ANME-1, ANME-2a/b/c, and ANME-3:** principally sulfate-associated AOM archaea.
- **ANME-2d / *Candidatus Methanoperedens*:** nitrate-dependent and, in some systems, metal-/extracellular-acceptor-associated AOM.
- **Sulfate-reducing bacterial partners:** often Deltaproteobacteria-associated lineages; use partner-specific taxonomy where a source resolves it.
- ***Candidatus Methylomirabilis*:** nitrite-dependent bacterial AOM using intracellular oxygen production and methane monooxygenase.
- **Anammox bacteria:** engineering partners that consume nitrite and ammonium in combined nitrogen-removal systems.
- ***Geobacter* and *Methanobacterium*:** electrode-enrichment association; assay-specific and not a replacement for the canonical ANME model. (gao2017anaerobicoxidationof pages 6-7)

## Candidate causal edges

Snippets below are concise source-derived statements or very close extractive summaries. Before committing them to YAML, curators should verify wording against the publisher PDF.

| Subject | Predicate | Object | Reference and supporting snippet | Evidence assessment / curation note |
|---|---|---|---|---|
| methane | is activated by | methyl-coenzyme M reductase | Scheller et al.: MCR with nickel cofactor F430 “cleaves the C–H bond” and transfers the methyl group to coenzyme M. DOI [10.1007/978-3-319-50391-2_3](https://doi.org/10.1007/978-3-319-50391-2_3), January 2020. (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48) | **Strong/core.** Curate. |
| methyl-coenzyme M reductase | uses cofactor | coenzyme F430 | Same source explicitly identifies the “nickel cofactor F430.” (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48) | **Strong/core.** Curate. |
| methyl-coenzyme M reductase | produces | methyl-coenzyme M from methane and coenzyme M | Methane activation transfers its methyl group “to coenzyme M.” (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48) | **Strong/core**, but verify exact reaction participants and Rhea mapping before formal reaction grounding. |
| reverse methanogenesis | oxidizes | methane-derived carbon to CO₂ | The pathway oxidizes methane-derived carbon “via tetrahydromethanopterin intermediates” to CO₂. (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48) | **Strong/core.** Curate. |
| AOM | requires | disposal of eight electrons to external acceptor | “All 8 electrons from methane oxidation must be disposed externally to terminal electron acceptors.” (scheller2020catabolicpathwaysand pages 48-51) | **Strong/core energetic constraint.** Curate. |
| ANME archaea | perform | reverse-methanogenesis AOM | AOM is catalyzed by ANME through “a reverse and modified methanogenesis pathway.” DOI [10.1155/2017/1654237](https://doi.org/10.1155/2017/1654237), January 2017. (timmers2017reversemethanogenesisand pages 1-2) | **Strong/core.** Curate. |
| sulfate | serves as terminal electron acceptor for | sulfate-coupled AOM | Sulfate-coupled AOM is described as exergonic, approximately ΔG°′ = −16 to −21 kJ mol⁻¹ CH₄ under cited standard-state treatments. (scheller2020catabolicpathwaysand pages 48-51, timmers2017reversemethanogenesisand pages 1-2) | **Strong/canonical.** Preserve source-specific thermodynamic assumptions. |
| sulfate-coupled AOM | requires | ANME–SRB syntrophy | ANME handle carbon metabolism while sulfate-reducing bacteria handle sulfur metabolism. (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48) | **Strong/canonical**, although some partner-free or alternate-coupling systems should not be precluded. |
| sulfate-reducing bacteria | reduce | sulfate to sulfide | The bacterial partner reduces sulfate and produces H₂S/HS⁻. (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48, chauhan2024chemistryofcoenzyme pages 10-11) | **Strong/canonical.** Curate. |
| *Ca. Methanoperedens* | couples | methane oxidation to nitrate reduction | *Ca. Methanoperedens nitroreducens* reduces nitrate to nitrite during AOM. (scheller2020catabolicpathwaysand pages 48-51) | **Strong but taxon/subtype-specific.** Curate in nitrate branch. |
| nitrate reduction | produces | nitrite | The nitrate-dependent ANME pathway reduces nitrate “to nitrite.” (scheller2020catabolicpathwaysand pages 48-51) | **Strong/subtype-specific.** Curate. |
| nitrite-removing partner | enables | nitrate-dependent ANME activity | Partner organisms detoxify nitrite by further reduction; coupled communities can yield N₂. (scheller2020catabolicpathwaysand pages 48-51) | **Moderate/context-dependent.** Do not assert an obligatory named partner universally. |
| *Ca. Methylomirabilis* | couples | nitrite reduction to methane oxidation | Review evidence describes nitrite-dependent oxygen production followed by methane oxidation. (scheller2020catabolicpathwaysand pages 45-48) | **Strong subtype concept**, but add a direct primary citation before YAML publication. |
| nitric oxide dismutation | generates | intracellular O₂ and N₂ | The proposed *Methylomirabilis* route proceeds through NO to N₂ and O₂. (scheller2020catabolicpathwaysand pages 45-48) | **Mechanistically important but uncertain at enzyme identity level.** Curate process-level edge with qualification; defer a specific “Nod enzyme” edge. |
| intracellular O₂ | enables | methane monooxygenase-dependent methane activation | This explains how bacterial methane monooxygenase can function in an externally anoxic system. (scheller2020catabolicpathwaysand pages 45-48) | **Strong subtype mechanism.** Not applicable to ANME/MCR AOM. |
| Fe(III)/Mn(IV) oxides | can accept electrons from | AOM | Reviews recognize AOM coupled to Fe(III)/Mn(IV) reduction and outline direct, shuttle-mediated, and partner-mediated EET possibilities. DOI [10.1111/1758-2229.13008](https://doi.org/10.1111/1758-2229.13008), September 2021. (zhang2021anaerobicoxidationof pages 8-9) | **Moderate.** Curate as alternative branch; do not assert one universal mechanism. |
| humic substances/AQDS | can accept electrons from | AOM | Fe(III) chelates, AQDS, biochar, and related extracellular acceptors support AOM in enrichment systems. (zhang2021anaerobicoxidationof pages 5-5) | **Moderate, often assay-specific.** Curate with experimental-context qualifier. |
| electrode | acts as terminal electron sink for | AOM | A carbon-fiber anode sustained 11.0 ± 1.3 mA m⁻², with isotopic support for AOM–EET. DOI [10.1038/s41598-017-05180-9](https://doi.org/10.1038/s41598-017-05180-9), July 2017. (gao2017anaerobicoxidationof pages 6-7) | **Direct reactor evidence but assay-specific.** Alternative experimental branch only. |
| multiheme c-type cytochromes | may mediate | ANME extracellular electron transfer | Reviews propose direct transfer through membrane-bound multiheme cytochromes, potentially with conductive appendages. (zhang2021anaerobicoxidationof pages 8-9, chauhan2024chemistryofcoenzyme pages 10-11) | **Moderate/lineage-specific.** Mark uncertain. |
| ANME | may transfer electrons directly to | sulfate-reducing bacteria | DIET is supported for some ANME–SRB associations, but evidence and machinery differ among lineages. (scheller2020catabolicpathwaysand pages 45-48, zhang2021anaerobicoxidationof pages 8-9, chauhan2024chemistryofcoenzyme pages 10-11) | **Moderate, not universal.** Mark uncertain. |
| low external electron-acceptor availability | increases reversibility of | intracellular AOM reactions | Isotopic work shows sulfate availability changes pathway reversibility and isotope effects. DOI [10.1126/sciadv.abe4939](https://doi.org/10.1126/sciadv.abe4939), May 2021. | **Strong physiological modulation**, useful as an environmental-regulation edge after direct source verification. |
| oxygen exposure | inhibits/downregulates | canonical nitrate-dependent ANME metabolism | Oxygen exposure downregulated methane-oxidation and nitrate-reduction genes in *Ca. Methanoperedens*. DOI [10.1128/AEM.01832-18](https://doi.org/10.1128/AEM.01832-18), December 2018. | **Taxon- and assay-specific.** Use as a conditional inhibitory edge, not a universal lethal effect. |

## Curation priorities

The table below separates robust core edges from subtype branches and claims requiring deferral.

| tier | candidate causal triple | evidence strength | recommended YAML action |
|---|---|---|---|
| Core | methane --is_activated_by--> methyl-coenzyme M reductase (MCR) during anaerobic oxidation of methane | Strong, mechanistic review support; direct core-pathway consensus (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48, timmers2017reversemethanogenesisand pages 1-2) | Curate as core edge; keep enzyme label-level unless stable protein-family grounding is added separately |
| Core | methyl-coenzyme M reductase (MCR) --uses_cofactor--> coenzyme F430 | Strong, mechanistic review support (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48) | Curate as core edge |
| Core | anaerobic oxidation of methane --realized_by--> reverse methanogenesis pathway | Strong, authoritative review support (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48, timmers2017reversemethanogenesisand pages 1-2) | Curate as core pathway edge |
| Core | reverse methanogenesis pathway --produces--> carbon dioxide / bicarbonate | Strong, pathway-level review support (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48, timmers2017reversemethanogenesisand pages 1-2) | Curate as core product edge |
| Core | anaerobic methane-oxidizing archaea (ANME) --bear_trait--> anaerobic oxidation of methane | Strong, broad consensus across reviews and enrichment studies (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48, timmers2017reversemethanogenesisand pages 1-2) | Curate as taxon-mechanism association with broad ANME label |
| High | sulfate --enables_terminal_electron_accepting_process_for--> sulfate-coupled anaerobic oxidation of methane | Strong for canonical marine AOM (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48, timmers2017reversemethanogenesisand pages 1-2) | Curate as canonical environmental/electron-acceptor edge |
| High | sulfate-coupled anaerobic oxidation of methane --requires--> syntrophic partnership of ANME and sulfate-reducing bacteria | Strong, foundational and review support (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48) | Curate as canonical consortium edge |
| High | sulfate-reducing bacteria --reduce--> sulfate to sulfide during sulfate-coupled AOM | Strong, canonical sulfur-metabolism assignment (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48, chauhan2024chemistryofcoenzyme pages 10-11) | Curate as partner-function edge |
| High | anaerobic oxidation of methane --depends_on--> external electron disposal to terminal electron acceptor | Strong pathway-level support (scheller2020catabolicpathwaysand pages 48-51, timmers2017reversemethanogenesisand pages 1-2) | Curate as general energetic constraint |
| Medium | Candidatus Methanoperedens --couples_methane_oxidation_to--> nitrate reduction | Strong for nitrate-dependent subtype; taxon-specific (scheller2020catabolicpathwaysand pages 48-51, li2023phylogeneticandmetabolic pages 9-9) | Curate as subtype/taxon-specific edge, not universal AOM edge |
| Medium | nitrate reduction by Candidatus Methanoperedens --produces--> nitrite | Strong for nitrate-dependent subtype (scheller2020catabolicpathwaysand pages 48-51) | Curate as subtype-specific edge |
| Medium | nitrite-dependent anaerobic methane oxidation --is_performed_by--> Candidatus Methylomirabilis | Strong background support in retrieved literature; less direct mechanistic detail in current evidence set (scheller2020catabolicpathwaysand pages 45-48, li2023phylogeneticandmetabolic pages 9-9) | Curate cautiously as subtype-specific edge only if separate direct source is added in YAML references |
| Medium | Candidatus Methylomirabilis --generates--> intracellular oxygen from nitric oxide dismutation | Moderate; widely accepted but only indirectly represented in current evidence set (scheller2020catabolicpathwaysand pages 45-48, li2023phylogeneticandmetabolic pages 9-9) | Mark uncertain or defer pending direct primary-source citation in YAML |
| Medium | nitrate-/nitrite-dependent AOM --supports--> methane-dependent nitrogen removal in engineered systems | Moderate; peer-reviewed wastewater evidence, partly genomic/transcriptomic (li2023phylogeneticandmetabolic pages 9-9) | Curate as application note, not core mechanism edge |
| Medium | metal oxides / humic substances / electrodes --can_serve_as--> extracellular electron acceptors for AOM | Moderate to strong, but mechanism and responsible taxa vary by system (zhang2021anaerobicoxidationof pages 8-9, zhang2021anaerobicoxidationof pages 5-5, gao2017anaerobicoxidationof pages 6-7) | Curate as alternative electron-acceptor branch with uncertainty notes |
| Medium | ANME extracellular electron transfer --may_involve--> multiheme c-type cytochromes | Moderate; supported by reviews and enrichment/electrode studies, but lineage-specific and not universally resolved (zhang2021anaerobicoxidationof pages 8-9, chauhan2024chemistryofcoenzyme pages 10-11) | Curate as uncertain/mechanism-candidate edge |
| Medium | ANME-SRB coupling --may_occur_via--> direct interspecies electron transfer | Moderate; plausible and influential but not universal across all consortia (scheller2020catabolicpathwaysand pages 45-48, zhang2021anaerobicoxidationof pages 8-9, chauhan2024chemistryofcoenzyme pages 10-11) | Curate only with uncertainty flag |
| Low | conductive archaella / nanowires --mediate--> long-range electron transfer in all ANME | Weak/generalized from limited systems and preprint-level extension | Do not curate as general trait edge yet |
| Warning | methane-dependent sulfate reduction alone --does_not_by_itself_prove--> net AOM | Strong caution from expert review (timmers2017reversemethanogenesisand pages 12-14) | Add curator warning to avoid overinterpreting assays |
| Warning | metal-dependent methane oxidation observations --do_not_by_themselves_prove--> obligate ANME-metal syntrophy | Strong caution from review (zhang2021anaerobicoxidationof pages 8-9, timmers2017reversemethanogenesisand pages 12-14) | Add curator warning; require stronger direct evidence |
| Warning | Methylomirabilis complete nitrate-to-N2 denitrification --is_currently_supported_mainly_by--> genomic/transcriptomic inference in specific systems | Moderate but inference-heavy (li2023phylogeneticandmetabolic pages 9-9) | Do not generalize to all nitrite-driven AOM; keep taxon- and study-specific |
| Warning | electrode-AOM consortia with Methanobacterium/Geobacter --should_not_be_generalized_to--> canonical ANME biology | Moderate, system-specific enrichment evidence (gao2017anaerobicoxidationof pages 6-7) | Keep out of core TraitMech graph or annotate as assay-specific branch |


*Table: This table prioritizes candidate causal edges for curating traitmech:000033, separating robust core AOM mechanisms from subtype-specific and uncertain claims. It is useful for deciding which relations belong in the core YAML versus alternative branches or curator warnings.*

## Recent developments, applications, and quantitative observations

### 2023–2024 developments

A 2023 metagenomic/metatranscriptomic study of engineered biofilms found that nitrogen loading of **0.1 versus 1.0 kg N m⁻³ d⁻¹** selected different combinations of anammox bacteria, *Ca. Methanoperedens*, and *Ca. Methylomirabilis*. It recovered two novel *Methylomirabilis* genomes; expression of nitrate-reduction genes in proposed *Ca. Methylomirabilis nitratireducens* suggested a complete nitrate-to-N₂ route. This challenges the older assumption that complete methane-dependent denitrification necessarily requires an archaeal–bacterial consortium, but remains genomic/transcriptomic inference rather than purified-culture biochemical proof. DOI [10.1038/s43705-023-00246-4](https://doi.org/10.1038/s43705-023-00246-4), April 2023. (li2023phylogeneticandmetabolic pages 9-9)

A 2024 MCR-focused review identifies MCR as both the methane-forming enzyme of methanogenesis and the initial methane-oxidation enzyme of ANME. It emphasizes F430, extensive post-translational modification, difficulty of in-vitro study, and the near-term practicality of genetically tractable methanogenic hosts for methane bioconversion rather than uncultured ANME. DOI [10.1021/acs.accounts.4c00413](https://doi.org/10.1021/acs.accounts.4c00413), August 2024. This is a useful application perspective, but engineered MCR bioconversion should not be represented as part of the natural AOM causal core.

A 2024 ANME-2d bioelectrochemical **preprint** reported methane-dependent current comprising **91–93% of total current** and *Ca. Methanoperedens* enrichment to **82%** on anodes, proposing a short-range electron-transfer complex and OmcZ-like nanowires. DOI [10.1101/2023.07.24.550278](https://doi.org/10.1101/2023.07.24.550278), July 2024. Because this was retrieved as bioRxiv and proposes incompletely characterized machinery, it should inform future curation but not support universal nanowire edges.

A 2024 sedimentary copper study found that medium/high insoluble-copper treatments caused a **46.6–77.4% decline in denitrification** and mortality among representative DAMO organisms, although apparent methane consumption was less affected than with soluble copper. DOI [10.3390/microorganisms12112259](https://doi.org/10.3390/microorganisms12112259), November 2024. This supports an assay-specific inhibitor branch, not a general claim that all copper minerals inhibit AOM equally.

### Current and prospective implementations

1. **Marine methane biofilter.** Sulfate-dependent AOM at sulfate–methane interfaces consumes methane before sedimentary release, making it a major control on marine methane flux. The low energy yield—reported around −16 to −21 kJ mol⁻¹ CH₄ under standard-state formulations—helps explain slow growth and the difficulty of cultivation. (scheller2020catabolicpathwaysand pages 48-51, timmers2017reversemethanogenesisand pages 1-2)
2. **Wastewater nitrogen and dissolved-methane removal.** n-DAMO can use methane already present in anaerobic effluent as an electron donor for nitrate/nitrite removal. Coupling *Methanoperedens*, *Methylomirabilis*, and anammox can reduce demand for externally supplied organic carbon and aeration. The 2023 biofilm study demonstrates implementation-level community activity but also shows that reactor loading strongly restructures the functional guild. (li2023phylogeneticandmetabolic pages 9-9)
3. **Bioelectrochemical methane conversion.** Electrodes can replace soluble terminal acceptors in experimental systems. One peer-reviewed reactor maintained **11.0 ± 1.3 mA m⁻²**; metagenomics attributed **89% of cytochrome-c** and **94% of type-IV-pilus** annotations to *Geobacter*, while the associated *Methanobacterium* lacked detected multiheme cytochromes. The authors therefore favored formate/H₂-mediated interspecies transfer over DIET in that system. (gao2017anaerobicoxidationof pages 6-7)
4. **Conductive materials and redox mediators.** AQDS, biochar, activated carbon, magnetite, and pyrogenic carbon are being studied as EET facilitators or redox shuttles. Their effects are material-, community-, and dose-dependent; these are experimental-factor nodes rather than intrinsic requirements of AOM. (zhang2021anaerobicoxidationof pages 8-9, zhang2021anaerobicoxidationof pages 5-5)
5. **Methane-to-chemical biomanufacturing.** MCR offers selective anaerobic methane activation, but enzyme complexity, oxygen sensitivity, F430 maturation, post-translational modifications, and poor ANME tractability remain major barriers. The authoritative 2024 assessment favors methanogenic chassis as the nearer-term engineering platform.

## Expert interpretation

The most defensible TraitMech graph is a **small invariant core plus electron-acceptor-specific branches**. The invariant core is: anoxia and methane availability → MCR/F430 methane activation in ANME → reverse-methanogenesis C1 oxidation → CO₂/HCO₃⁻ formation and eight-electron release → electron disposal to an external acceptor. The sulfate branch adds ANME–SRB syntrophy and sulfide production; nitrate/nitrite branches add distinct taxa and nitrogen transformations; metal, humic, and electrode branches add alternative EET routes. (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48, zhang2021anaerobicoxidationof pages 8-9)

Mechanistic confidence falls sharply beyond this core. Multiheme cytochromes are credible EET candidates in several ANME lineages, but the exact terminal conduits and the relative importance of DIET, soluble shuttles, conductive minerals, hydrogen, or formate vary. The absence of obligate metal-reducing syntrophy proof and the contrasting electrode consortium illustrate why a single universal electron-transfer edge would overstate present knowledge. (zhang2021anaerobicoxidationof pages 8-9, gao2017anaerobicoxidationof pages 6-7)

## Warnings: claims not yet ready for TraitMech

- Do not curate methane-dependent sulfate reduction, metal reduction, gene presence, or isotope signatures alone as proof of net AOM; expert review states that net methane oxidation is the decisive criterion in complex communities. (timmers2017reversemethanogenesisand pages 12-14)
- Do not assign AOM from `mcrA` without directionality and taxonomic/contextual evidence.
- Do not make DIET or multiheme cytochromes mandatory for all sulfate-dependent AOM.
- Do not curate conductive archaella, OmcZ-like nanowires, or one named short-range complex as universal ANME machinery; current evidence is lineage-specific and partly preprint-level.
- Do not represent *Methylomirabilis* intracellular oxygen formation as canonical archaeal AOM. It is a bacterial, nitrite-dependent subtype using methane monooxygenase.
- Do not generalize complete nitrate-to-N₂ conversion by one proposed *Methylomirabilis* lineage to the genus; the 2023 evidence is genome/transcriptome-based. (li2023phylogeneticandmetabolic pages 9-9)
- Do not infer obligate ANME–metal-reducing-bacterium syntrophy; it remains unproven. (zhang2021anaerobicoxidationof pages 8-9)
- Do not put electrode, AQDS, biochar, magnetite, or pyrogenic carbon in the invariant biological core.
- Do not transfer gene/protein edges from genetically tractable *Methanosarcina acetivorans* directly to uncultured ANME without orthology and functional evidence.
- Resolve all ChEBI, GO, Rhea, UniProt, KEGG, and NCBITaxon identifiers programmatically before YAML insertion; label-only nodes are safer than invented or memory-derived CURIEs.

## DOI-first bibliography

1. Boetius A. et al. **A marine microbial consortium apparently mediating anaerobic oxidation of methane.** *Nature* 407, 623–626. October 2000. [https://doi.org/10.1038/35036572](https://doi.org/10.1038/35036572).
2. Timmers P.H.A. et al. **Reverse Methanogenesis and Respiration in Methanotrophic Archaea.** *Archaea*. January 2017. [https://doi.org/10.1155/2017/1654237](https://doi.org/10.1155/2017/1654237). (timmers2017reversemethanogenesisand pages 1-2)
3. Gao Y. et al. **Anaerobic oxidation of methane coupled with extracellular electron transfer to electrodes.** *Scientific Reports*. July 2017. [https://doi.org/10.1038/s41598-017-05180-9](https://doi.org/10.1038/s41598-017-05180-9). (gao2017anaerobicoxidationof pages 6-7)
4. Scheller S., Ermler U., Shima S. **Catabolic Pathways and Enzymes Involved in Anaerobic Methane Oxidation.** January 2020. [https://doi.org/10.1007/978-3-319-50391-2_3](https://doi.org/10.1007/978-3-319-50391-2_3). (scheller2020catabolicpathwaysand pages 48-51, scheller2020catabolicpathwaysand pages 45-48)
5. Zhang X., Yuan Z., Hu S. **Anaerobic oxidation of methane mediated by microbial extracellular respiration.** *Environmental Microbiology Reports* 13, 790–804. September 2021. [https://doi.org/10.1111/1758-2229.13008](https://doi.org/10.1111/1758-2229.13008). (zhang2021anaerobicoxidationof pages 8-9, zhang2021anaerobicoxidationof pages 5-5)
6. Wegener G. et al. **Sulfate-dependent reversibility of intracellular reactions explains the opposing isotope effects in the anaerobic oxidation of methane.** *Science Advances*. May 2021. [https://doi.org/10.1126/sciadv.abe4939](https://doi.org/10.1126/sciadv.abe4939).
7. Li J. et al. **Phylogenetic and metabolic diversity of microbial communities performing anaerobic ammonium and methane oxidations under different nitrogen loadings.** *ISME Communications*. April 2023. [https://doi.org/10.1038/s43705-023-00246-4](https://doi.org/10.1038/s43705-023-00246-4). (li2023phylogeneticandmetabolic pages 9-9)
8. Dinh T.-A., Allen K.D. **Toward the Use of Methyl-Coenzyme M Reductase for Methane Bioconversion Applications.** *Accounts of Chemical Research* 57, 2746–2757. August 2024. [https://doi.org/10.1021/acs.accounts.4c00413](https://doi.org/10.1021/acs.accounts.4c00413).
9. Ouboter H.T. et al. **Mechanisms of extracellular electron transfer in anaerobic methanotrophic archaea.** bioRxiv preprint. July 2024. [https://doi.org/10.1101/2023.07.24.550278](https://doi.org/10.1101/2023.07.24.550278).
10. Xia L. et al. **The Effects of Model Insoluble Copper Compounds in a Sedimentary Environment on Denitrifying Anaerobic Methane Oxidation Enrichment.** *Microorganisms* 12, 2259. November 2024. [https://doi.org/10.3390/microorganisms12112259](https://doi.org/10.3390/microorganisms12112259).

References

1. (scheller2020catabolicpathwaysand pages 48-51): Silvan Scheller, Ulrich Ermler, and Seigo Shima. Catabolic Pathways and Enzymes Involved in Anaerobic Methane Oxidation, pages 31-59. Springer International Publishing, Jan 2020. URL: https://doi.org/10.1007/978-3-319-50391-2\_3, doi:10.1007/978-3-319-50391-2\_3. This article has 32 citations.

2. (scheller2020catabolicpathwaysand pages 45-48): Silvan Scheller, Ulrich Ermler, and Seigo Shima. Catabolic Pathways and Enzymes Involved in Anaerobic Methane Oxidation, pages 31-59. Springer International Publishing, Jan 2020. URL: https://doi.org/10.1007/978-3-319-50391-2\_3, doi:10.1007/978-3-319-50391-2\_3. This article has 32 citations.

3. (timmers2017reversemethanogenesisand pages 1-2): Peer H. A. Timmers, Cornelia U. Welte, Jasper J. Koehorst, Caroline M. Plugge, Mike S. M. Jetten, and Alfons J. M. Stams. Reverse methanogenesis and respiration in methanotrophic archaea. Archaea, 2017:1-22, Jan 2017. URL: https://doi.org/10.1155/2017/1654237, doi:10.1155/2017/1654237. This article has 448 citations.

4. (timmers2017reversemethanogenesisand pages 12-14): Peer H. A. Timmers, Cornelia U. Welte, Jasper J. Koehorst, Caroline M. Plugge, Mike S. M. Jetten, and Alfons J. M. Stams. Reverse methanogenesis and respiration in methanotrophic archaea. Archaea, 2017:1-22, Jan 2017. URL: https://doi.org/10.1155/2017/1654237, doi:10.1155/2017/1654237. This article has 448 citations.

5. (zhang2021anaerobicoxidationof pages 8-9): Xueqin Zhang, Zhiguo Yuan, and Shihu Hu. Anaerobic oxidation of methane mediated by microbial extracellular respiration. Environmental microbiology reports, 13:790-804, Sep 2021. URL: https://doi.org/10.1111/1758-2229.13008, doi:10.1111/1758-2229.13008. This article has 41 citations and is from a peer-reviewed journal.

6. (zhang2021anaerobicoxidationof pages 5-5): Xueqin Zhang, Zhiguo Yuan, and Shihu Hu. Anaerobic oxidation of methane mediated by microbial extracellular respiration. Environmental microbiology reports, 13:790-804, Sep 2021. URL: https://doi.org/10.1111/1758-2229.13008, doi:10.1111/1758-2229.13008. This article has 41 citations and is from a peer-reviewed journal.

7. (gao2017anaerobicoxidationof pages 6-7): Yaohuan Gao, Jangho Lee, Josh D. Neufeld, Joonhong Park, Bruce E. Rittmann, and Hyung-Sool Lee. Anaerobic oxidation of methane coupled with extracellular electron transfer to electrodes. Scientific Reports, Jul 2017. URL: https://doi.org/10.1038/s41598-017-05180-9, doi:10.1038/s41598-017-05180-9. This article has 82 citations and is from a peer-reviewed journal.

8. (chauhan2024chemistryofcoenzyme pages 10-11): Shive Murat Singh Chauhan. Chemistry of coenzyme f420 in environment. Journal of Molecular Chemistry, Apr 2024. URL: https://doi.org/10.62110/sciencein.jmc.2024.696, doi:10.62110/sciencein.jmc.2024.696. This article has 5 citations.

9. (li2023phylogeneticandmetabolic pages 9-9): Jie Li, Tao Liu, Simon J McIlroy, Gene W Tyson, and Jianhua Guo. Phylogenetic and metabolic diversity of microbial communities performing anaerobic ammonium and methane oxidations under different nitrogen loadings. ISME Communications, Apr 2023. URL: https://doi.org/10.1038/s43705-023-00246-4, doi:10.1038/s43705-023-00246-4. This article has 65 citations and is from a peer-reviewed journal.