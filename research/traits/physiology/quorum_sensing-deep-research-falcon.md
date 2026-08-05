---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T12:00:55.623144'
end_time: '2026-08-04T12:07:15.468506'
duration_seconds: 379.85
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: quorum sensing
  trait_identifier: traitmech:000084
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: quorum_sensing
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-density-dependent regulatory physiology in which cells produce,
    release, and detect diffusible autoinducer signals to coordinate gene expression
    across a population.
  parent_traits: METPO:1000059
  synonyms: autoinduction
  evidence_summary: 'DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler
    review quorum sensing as autoinducer-mediated cell-to-cell communication coordinating
    population-wide behavior.) | DOI:10.1146/annurev.micro.55.1.165:  (Miller & Bassler
    review quorum sensing across bacteria and its regulatory logic.)'
  causal_graph_summary: 'quorum_sensing_autoinducer: 7 nodes, 6 edges'
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
- **Trait label:** quorum sensing
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000084
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-density-dependent regulatory physiology in which cells produce, release, and detect diffusible autoinducer signals to coordinate gene expression across a population.
- **Parent traits:** METPO:1000059
- **Synonyms:** autoinduction
- **Existing evidence:** DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler review quorum sensing as autoinducer-mediated cell-to-cell communication coordinating population-wide behavior.) | DOI:10.1146/annurev.micro.55.1.165:  (Miller & Bassler review quorum sensing across bacteria and its regulatory logic.)
- **Existing causal graph summary:** quorum_sensing_autoinducer: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **quorum sensing** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/quorum_sensing.yaml`.

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
- **Trait label:** quorum sensing
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000084
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-density-dependent regulatory physiology in which cells produce, release, and detect diffusible autoinducer signals to coordinate gene expression across a population.
- **Parent traits:** METPO:1000059
- **Synonyms:** autoinduction
- **Existing evidence:** DOI:10.1146/annurev.cellbio.21.012704.131001:  (Waters & Bassler review quorum sensing as autoinducer-mediated cell-to-cell communication coordinating population-wide behavior.) | DOI:10.1146/annurev.micro.55.1.165:  (Miller & Bassler review quorum sensing across bacteria and its regulatory logic.)
- **Existing causal graph summary:** quorum_sensing_autoinducer: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **quorum sensing** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/quorum_sensing.yaml`.

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


# Curation report: quorum sensing

## Trait record and scope

- **Trait:** quorum sensing
- **Identifier:** `traitmech:000084`
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** `METPO:1000059`
- **Synonym:** autoinduction

Quorum sensing (QS) is the physiological capacity to **produce or release autoinducer signals, allow their extracellular abundance to reflect local population and transport conditions, perceive a cognate signal, and alter gene regulation in response**. Contemporary descriptions therefore treat QS as a dynamic sequence of signal synthesis, secretion, accumulation, perception, and response—not merely as the presence of a signal molecule or a high cell density. Positive feedback often sharpens the response into QS-OFF and QS-ON states. (juszczukkubiak2024molecularaspectsof pages 2-3, ostovar2024phenotypicmemoryin pages 1-2, hu2024nanomaterialsregulatebacterial pages 1-2)

### Boundaries for TraitMech

1. **Cell density is an input proxy, not a sufficient mechanistic definition.** Autoinducer concentration also depends on diffusion, flow, spatial confinement, degradation, uptake, growth history, and signal-production rate. A density-associated phenotype without signal synthesis, cognate perception, and regulatory response should not automatically be curated as QS.
2. **Biofilm formation, bioluminescence, virulence, competence, motility, conjugation, secretion, and public-good production are downstream outputs**, not synonyms for QS. A strain can form a biofilm without QS, and QS can regulate outputs other than biofilm formation. Recent reviews explicitly place these phenotypes downstream of signal perception. (ostovar2024phenotypicmemoryin pages 1-2, hu2024nanomaterialsregulatebacterial pages 1-2)
3. **Diffusion sensing and efficiency sensing are interpretive models** of what extracellular signal concentration encodes. They overlap mechanistically with QS but should not be asserted as equivalent without experiments separating population density from mass transfer or spatial confinement.
4. **Quorum quenching (QQ) is the inhibition of QS**, by signal destruction, synthesis inhibition, receptor antagonism, or disruption of signal transduction. It is not part of the positive trait itself.
5. **Contact-dependent signaling, electrical signaling, and constitutive metabolite responses are outside scope** unless a diffusible, produced signal is perceived through a demonstrated regulatory circuit.
6. **AI-2/LuxS requires special caution.** LuxS also participates in activated-methyl-cycle metabolism. Detection of `luxS`, AI-2-like activity, or a `luxS` mutant phenotype alone does not establish QS; signal export, perception, and rescue or receptor evidence are needed.
7. **Signal-response history matters.** A 2024 theoretical study predicts transient phenotypic memory because QS proteins and other biomolecules persist after signal removal; response can therefore depend on prior exposure as well as current density. This is a modifier of QS dynamics, not a separate core requirement. (ostovar2024phenotypicmemoryin pages 1-2)

## Recommended graph architecture

A single seven-node graph is too narrow to represent the mechanistic diversity of this trait. The YAML should use a **small taxon-neutral core** and attach **taxon-specific mechanism modules** rather than connecting LuxI/LuxR, Vibrio phosphorelays, and staphylococcal agr components into one universal linear pathway.

### Taxon-neutral core

`microbial population growth/spatial confinement → extracellular autoinducer accumulation → cognate autoinducer perception → signal-transduction or transcription-regulator activation → QS-responsive gene expression → coordinated population phenotype`

The first edge must be qualified: greater population abundance generally promotes accumulation, but environmental transport and signal turnover modify it. The strongest graph blueprint is summarized below.

| module/taxon | subject | predicate | object | evidence strength | DOI |
|---|---|---|---|---|---|
| General QS | autoinducer | accumulates to threshold concentration in extracellular milieu | cognate QS perception/activation | Strong review consensus (2024) (juszczukkubiak2024molecularaspectsof pages 2-3, hu2024nanomaterialsregulatebacterial pages 1-2) | 10.3390/ijms25052655; 10.1002/advs.202306070 |
| General QS | cognate autoinducer perception | activates | QS-responsive gene regulation | Strong review consensus (2024) (juszczukkubiak2024molecularaspectsof pages 2-3, hu2024nanomaterialsregulatebacterial pages 1-2) | 10.3390/ijms25052655; 10.1002/advs.202306070 |
| LuxI/LuxR (Aliivibrio/Vibrio model) | LuxI | synthesizes | AHL (e.g., 3-oxo-C6-HSL) | Strong canonical mechanism (juszczukkubiak2024molecularaspectsof pages 2-3, chan2015inhibitingnacylhomoserinelactone pages 1-2) | 10.3390/ijms25052655; 10.3389/fmicb.2015.01173 |
| LuxI/LuxR (Aliivibrio/Vibrio model) | AHL | binds | LuxR | Strong canonical mechanism (juszczukkubiak2024molecularaspectsof pages 2-3, chan2015inhibitingnacylhomoserinelactone pages 1-2) | 10.3390/ijms25052655; 10.3389/fmicb.2015.01173 |
| LuxI/LuxR (Aliivibrio/Vibrio model) | LuxR-AHL complex | binds promoter of | lux-box target genes | Strong canonical mechanism (juszczukkubiak2024molecularaspectsof pages 2-3) | 10.3390/ijms25052655 |
| LuxI/LuxR (Aliivibrio/Vibrio model) | LuxR-AHL complex | activates transcription of | luxI | Strong canonical positive-feedback edge (juszczukkubiak2024molecularaspectsof pages 2-3, chan2015inhibitingnacylhomoserinelactone pages 1-2) | 10.3390/ijms25052655; 10.3389/fmicb.2015.01173 |
| Vibrio harveyi/cholerae | LuxN/LuxPQ/CqsS receptors at low AI | phosphorylate via phosphorelay | LuxU | Strong primary/review support (eickhoff2021luxtcontrolsspecific pages 1-2, walker2023asimplemechanism pages 1-2) | 10.1371/journal.pgen.1009336; 10.7554/eLife.86699 |
| Vibrio harveyi/cholerae | LuxU | transfers phosphate to | LuxO | Strong primary/review support (eickhoff2021luxtcontrolsspecific pages 1-2, walker2023asimplemechanism pages 1-2) | 10.1371/journal.pgen.1009336; 10.7554/eLife.86699 |
| Vibrio harveyi/cholerae | LuxO-P + sigma-54 | activates transcription of | qrr sRNAs | Strong primary/review support (eickhoff2021luxtcontrolsspecific pages 1-2, walker2023asimplemechanism pages 1-2) | 10.1371/journal.pgen.1009336; 10.7554/eLife.86699 |
| Vibrio harveyi/cholerae | Qrr sRNAs | activate translation of | AphA | Strong primary/review support (eickhoff2021luxtcontrolsspecific pages 1-2, walker2023asimplemechanism pages 1-2) | 10.1371/journal.pgen.1009336; 10.7554/eLife.86699 |
| Vibrio harveyi/cholerae | Qrr sRNAs | repress translation/expression of | HapR/LuxR | Strong primary/review support (eickhoff2021luxtcontrolsspecific pages 1-2, walker2023asimplemechanism pages 1-2) | 10.1371/journal.pgen.1009336; 10.7554/eLife.86699 |
| Vibrio cholerae high-cell-density state | high autoinducer abundance | permits expression of | HapR | Strong primary support (walker2023asimplemechanism pages 1-2) | 10.7554/eLife.86699 |
| Staphylococcus aureus agr | AgrD | is precursor of | AIP | Strong canonical mechanism (juszczukkubiak2024molecularaspectsof pages 5-7, green2023modelledmicrogravityreducesvirulence pages 1-2) | 10.3390/ijms25052655; 10.3390/ijms242115997 |
| Staphylococcus aureus agr | AgrB | processes/matures | AgrD into AIP | Strong canonical mechanism (juszczukkubiak2024molecularaspectsof pages 5-7) | 10.3390/ijms25052655 |
| Staphylococcus aureus agr | AIP | binds/activates | AgrC | Strong primary/review support (green2023modelledmicrogravityreducesvirulence pages 1-2, juszczukkubiak2024molecularaspectsof pages 5-7) | 10.3390/ijms242115997; 10.3390/ijms25052655 |
| Staphylococcus aureus agr | AgrC | phosphorylates | AgrA | Strong canonical mechanism (green2023modelledmicrogravityreducesvirulence pages 1-2) | 10.3390/ijms242115997 |
| Staphylococcus aureus agr | AgrA | activates transcription of | RNAIII | Strong canonical mechanism (juszczukkubiak2024molecularaspectsof pages 5-7) | 10.3390/ijms25052655 |
| Staphylococcus aureus agr | RNAIII | inhibits translation/activity of | Rot | Strong canonical mechanism (juszczukkubiak2024molecularaspectsof pages 5-7) | 10.3390/ijms25052655 |
| Staphylococcus aureus agr | reduced AIP production under modeled microgravity | delays | agr activation | Strong 2023 condition-specific evidence; environment-specific (green2023modelledmicrogravityreducesvirulence pages 1-2) | 10.3390/ijms242115997 |


*Table: This table summarizes the strongest, curation-ready causal edges for quorum sensing across general, LuxI/LuxR, Vibrio, and staphylococcal agr modules. It is designed as a compact graph blueprint highlighting well-supported mechanistic nodes and edges with direct literature grounding.*

## Candidate nodes grouped by type

### Trait and biological-process nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| quorum sensing | `traitmech:000084`; consider `GO:0009372` for bacterial-type QS process | Retain the supplied TraitMech CURIE verbatim. Verify the current GO label/version during implementation. |
| signal production | GO label candidate only | Prefer a system-specific process if available. |
| extracellular signal accumulation | Label-only | Concentration state rather than a conventional biological process. |
| signal perception | GO label candidate only | Ground receptor activity separately where possible. |
| signal-transduction phosphorelay | GO term candidate | Applicable to Vibrio sensor and agr two-component systems, not cytosolic LuxR-type systems. |
| QS-responsive transcription | GO label candidate only | Represents the proximal output of the trait. |
| biofilm formation | `GO:0042710` | Downstream phenotype; never use as an identity relation to QS. |
| bioluminescence | `GO:0008218` | Canonical *Aliivibrio fischeri* output. |
| natural competence, virulence regulation, motility, conjugation, T6SS | GO label candidates | Taxon- and circuit-specific outputs. |
| quorum quenching | Label-only unless a verified ontology term is selected | Negative modifier of the trait. |

### Chemicals and signals

| Candidate node | Grounding recommendation | Notes |
|---|---|---|
| N-acyl-L-homoserine lactone (AHL) | CHEBI class candidate; verify exact CURIE | Proteobacterial signal class; chain length and oxidation state determine specificity. |
| 3-oxo-C6-HSL | CHEBI candidate; verify exact CURIE | Canonical LuxI/LuxR signal. |
| 3-oxo-C12-HSL and C4-HSL | CHEBI candidates; verify exact CURIEs | *Pseudomonas aeruginosa* Las and Rhl signals, respectively. |
| autoinducing peptide (AIP) | Label-only or system-specific chemical entity | Mature cyclic/thiolactone peptide; sequence and agr group matter. |
| AI-2 family | CHEBI candidate; verify chemically specific form | Do not collapse DPD and its borated/non-borated receptor-bound derivatives without qualification. |
| CAI-1 | CHEBI candidate; verify exact chemical species | Vibrio-genus signal. |
| DPO | CHEBI candidate; verify exact CURIE | *V. cholerae* autoinducer; receptor pathway should be modeled separately if expanded. |
| S-adenosyl-L-methionine and acyl-ACP | CHEBI and protein-complex candidates | LuxI substrates; the acyl donor varies. |

### Genes, proteins, RNAs, and complexes

- **LuxI/LuxR module:** `luxI`, LuxI AHL synthase, `luxR`, LuxR transcription factor, AHL–LuxR complex, lux box, `luxCDABE`.
- ***P. aeruginosa* modules:** LasI/LasR and RhlI/RhlR. These are homologous but use distinct AHLs and should be separate subgraphs.
- **Vibrio parallel-input module:** LuxM/AI-1/LuxN; LuxS/AI-2/LuxP–LuxQ; CqsA/CAI-1/CqsS; LuxU; LuxO; σ54; Qrr sRNAs; AphA; HapR or the *V. harveyi* master regulator LuxR. The retrieved evidence identifies three autoinducers and their cognate receptors in *V. harveyi*. (eickhoff2021luxtcontrolsspecific pages 1-2)
- ***S. aureus* agr module:** AgrD precursor, AgrB processing/export protein, mature AIP, AgrC sensor histidine kinase, AgrA response regulator, RNAII, RNAIII, and Rot.
- **Quenching nodes:** AHL lactonase, AHL acylase, oxidoreductase, receptor antagonist, synthesis inhibitor, signal-adsorbing or catalytic nanomaterial. Add enzyme-family CURIEs only after sequence- or reaction-specific verification.

For genes and proteins, **do not assign one universal UniProt accession**. Accessions are strain-specific and should accompany a taxon/strain context in each implementation. Likewise, EC and Rhea identifiers should be added only after verifying that the exact enzymatic reaction—not merely the protein family—is represented.

### Taxa and localization nodes

Useful taxon contexts include *Aliivibrio fischeri*, *Vibrio harveyi*, *Vibrio cholerae*, *Pseudomonas aeruginosa*, and *Staphylococcus aureus*. Use verified `NCBITaxon` identifiers in the YAML rather than inferring them from genus names. Relevant localizations are cytoplasm, cytoplasmic membrane, extracellular region, DNA promoter region, and—where applicable—periplasm.

### Environmental and experimental factors

- cell abundance or local biomass density;
- spatial confinement and aggregate/biofilm architecture;
- diffusion, advection/flow, and medium volume;
- autoinducer degradation, dilution, adsorption, and uptake;
- pH and temperature, which can change signal stability and receptor behavior;
- carbon/nutrient status and cAMP–CRP signaling;
- modeled low-shear microgravity;
- exogenous autoinducer addition;
- signal-degrading enzymes, probiotics, phages, nanoparticles, and receptor antagonists.

## Evidence-backed candidate edges

The snippets below are concise evidence extracts or faithful excerpt-level paraphrases from the retrieved sources. Predicates should be mapped to the relation vocabulary already used by TraitMech.

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| microbial population increase | promotes | extracellular autoinducer accumulation | 2024 review: QS proceeds through AI synthesis, membrane diffusion/transport, accumulation to a threshold, and cognate detection. DOI: [10.3390/ijms25052655](https://doi.org/10.3390/ijms25052655). (juszczukkubiak2024molecularaspectsof pages 2-3) | **Curate with qualifier.** Flow, confinement, and degradation also control concentration. |
| threshold autoinducer abundance | activates | cognate signal perception and downstream regulation | “When bacterial abundance reaches a threshold, accumulated signals activate perception elements” and downstream gene regulation. DOI: [10.1002/advs.202306070](https://doi.org/10.1002/advs.202306070). (hu2024nanomaterialsregulatebacterial pages 1-2) | Strong taxon-neutral core edge. |
| LuxI | synthesizes | 3-oxo-C6-HSL | LuxI generates 3-oxo-C6-HSL from S-adenosylmethionine and acyl-ACP. DOI: [10.3389/fmicb.2015.01173](https://doi.org/10.3389/fmicb.2015.01173). (chan2015inhibitingnacylhomoserinelactone pages 1-2) | Strong; canonical *A. fischeri* module, not universal. |
| 3-oxo-C6-HSL | binds | LuxR | The signal binds the LuxR transcriptional regulator. DOI: [10.3389/fmicb.2015.01173](https://doi.org/10.3389/fmicb.2015.01173). (chan2015inhibitingnacylhomoserinelactone pages 1-2) | Strong and direct. |
| AHL–LuxR complex | binds | lux-box promoter DNA | LuxR’s C-terminal helix-turn-helix region binds the palindromic lux box near target genes. DOI: [10.3390/ijms25052655](https://doi.org/10.3390/ijms25052655). (juszczukkubiak2024molecularaspectsof pages 2-3) | Strong; exact promoter geometry is system-specific. |
| AHL–LuxR complex | activates transcription of | `luxICDABE`/`luxI` | Signal-bound LuxR activates the lux operon, including signal synthase expression, producing autoinduction. DOI: [10.3389/fmicb.2015.01173](https://doi.org/10.3389/fmicb.2015.01173). (chan2015inhibitingnacylhomoserinelactone pages 1-2) | Strong positive-feedback edge. |
| `luxCDABE` expression | increases | bioluminescence | LuxR activation induces luciferase-system expression and light production. DOI: [10.1002/mbo3.70016](https://doi.org/10.1002/mbo3.70016). (liu2025quorumsensingnot pages 2-6) | Strong but output-specific. |
| AI-1 / AI-2 / CAI-1 | binds | LuxN / LuxPQ / CqsS, respectively | *V. harveyi* uses AI-1–LuxN, AI-2–LuxPQ, and CAI-1–CqsS channels. DOI: [10.1371/journal.pgen.1009336](https://doi.org/10.1371/journal.pgen.1009336). (eickhoff2021luxtcontrolsspecific pages 1-2) | Strong, taxon-specific. |
| unliganded Vibrio receptors at low density | phosphorylate through | LuxU → LuxO | At low density, receptors act as kinases; LuxU transfers phosphate to LuxO. DOI: [10.1371/journal.pgen.1009336](https://doi.org/10.1371/journal.pgen.1009336). (eickhoff2021luxtcontrolsspecific pages 1-2) | Split into receptor→LuxU and LuxU→LuxO edges. |
| LuxO-P with σ54 | activates transcription of | Qrr sRNAs | LuxO-P and σ54 activate five Qrr sRNAs in *V. harveyi*. DOI: [10.1371/journal.pgen.1009336](https://doi.org/10.1371/journal.pgen.1009336). (eickhoff2021luxtcontrolsspecific pages 1-2) | Strong; *V. cholerae* has four Qrrs in the retrieved 2023 study. |
| Qrr sRNAs | promotes translation of | AphA | Qrr sRNAs promote the low-cell-density regulator AphA. DOI: [10.1371/journal.pgen.1009336](https://doi.org/10.1371/journal.pgen.1009336). (eickhoff2021luxtcontrolsspecific pages 1-2) | Strong. |
| Qrr sRNAs | repress | HapR/LuxR master regulator | Qrrs repress the high-density master regulator; in *V. cholerae*, high AI reverses this state and permits HapR. DOI: [10.7554/eLife.86699](https://doi.org/10.7554/eLife.86699). (walker2023asimplemechanism pages 1-2) | Strong; use species-correct regulator name. |
| HapR | regulates | approximately 100 genes | 2023 genome-wide analysis reports that HapR controls about 100 genes; mapped binding identified 32 target loci in that experiment. DOI: [10.7554/eLife.86699](https://doi.org/10.7554/eLife.86699). (walker2023asimplemechanism pages 1-2) | Quantitative and taxon-specific; “controls” includes direct and indirect effects. |
| AgrD | precursor-of | mature AIP | AgrD encodes the precursor peptide. DOI: [10.3390/ijms25052655](https://doi.org/10.3390/ijms25052655). (juszczukkubiak2024molecularaspectsof pages 5-7) | Strong. |
| AgrB | processes | AgrD into mature AIP | AgrB controls processing and thiolactone-ring formation. DOI: [10.3390/ijms25052655](https://doi.org/10.3390/ijms25052655). (juszczukkubiak2024molecularaspectsof pages 5-7) | Strong; processing details can vary and may involve additional factors. |
| extracellular AIP | binds and activates | AgrC | AIP accumulation activates the AgrC sensor. DOI: [10.3390/ijms242115997](https://doi.org/10.3390/ijms242115997). (green2023modelledmicrogravityreducesvirulence pages 1-2) | Strong. AgrC is a membrane histidine kinase, not a transcriptional regulator. |
| activated AgrC | phosphorylates | AgrA | AIP–AgrC activation leads to AgrA phosphorylation. DOI: [10.3390/ijms242115997](https://doi.org/10.3390/ijms242115997). (green2023modelledmicrogravityreducesvirulence pages 1-2) | Strong two-component-system edge. |
| AgrA | activates | agr P2/P3 transcription and RNAIII | AgrA/AgrC induces RNAII and controls the RNAIII effector. DOI: [10.3390/ijms25052655](https://doi.org/10.3390/ijms25052655). (juszczukkubiak2024molecularaspectsof pages 5-7) | Prefer separate promoter-specific edges. |
| RNAIII | inhibits | Rot-mediated virulence repression | RNAIII acts through translational inhibition of the virulence repressor Rot. DOI: [10.3390/ijms25052655](https://doi.org/10.3390/ijms25052655). (juszczukkubiak2024molecularaspectsof pages 5-7) | Strong, *S. aureus*-specific. |
| modeled low-shear microgravity | decreases | AIP production | In MRSA JE2 and MSSA SH1000, modeled microgravity reduced AIP, delayed agr activation, reduced cytotoxicity, and increased fibronectin binding; exogenous AIP restored cytotoxicity. DOI: [10.3390/ijms242115997](https://doi.org/10.3390/ijms242115997). (green2023modelledmicrogravityreducesvirulence pages 1-2) | Strong experimental edge but **condition- and strain-specific**. Do not generalize to natural microgravity without validation. |
| AHL-degrading enzymes | decreases | effective AHL concentration | QQ reviews describe enzymatic signal inactivation as a means to inhibit QS-regulated behavior. DOI: [10.3389/fpls.2022.1063393](https://doi.org/10.3389/fpls.2022.1063393). | Suitable inhibitory edge after specifying enzyme and substrate; broad class claim otherwise. |
| nanomaterial intervention | may inhibit | signal synthesis, accumulation, perception, or response | 2024 expert review organizes nanomaterial action across signal supply and transduction stages. DOI: [10.1002/advs.202306070](https://doi.org/10.1002/advs.202306070). (hu2024nanomaterialsregulatebacterial pages 1-2) | **Do not curate as one generic edge.** Require material-specific, dose-specific primary evidence. |

## Recent developments and current applications

### Mechanistic advances, 2023–2024

- A 2023 *eLife* study showed that *V. cholerae* integrates QS with carbon-status signaling: HapR and cAMP receptor protein can occupy shared genomic sites, and their direct interaction allows HapR to block CRP-dependent activation. This demonstrates that QS output is integrated with environmental physiology rather than operating as an isolated density switch. DOI: [10.7554/eLife.86699](https://doi.org/10.7554/eLife.86699), published July 2023. (walker2023asimplemechanism pages 1-2)
- The 2023 modeled-microgravity study provided a useful causal perturbation: reduced AIP generation delayed agr signaling, whereas exogenous AIP restored cytotoxicity. This localizes the environmental effect upstream of receptor activation and illustrates how a graph can incorporate experimental factors. DOI: [10.3390/ijms242115997](https://doi.org/10.3390/ijms242115997), published November 2023. (green2023modelledmicrogravityreducesvirulence pages 1-2)
- A 2024 computational study formalized QS phenotypic memory. Its models predict that memory strength depends on regulated-gene fold change, autoinducer synthesis rate, activation threshold, growth rate, and how density was perturbed. These predictions are mechanistically plausible but should remain **uncertain/model-derived** until validated broadly in vivo. DOI: [10.1371/journal.pcbi.1011696](https://doi.org/10.1371/journal.pcbi.1011696), published November 2024. (ostovar2024phenotypicmemoryin pages 1-2)
- A 2024 *Advanced Science* review treats nanomaterial modulation as a multistage engineering problem—signal synthesis, secretion, accumulation, perception, and response—and emphasizes that both material properties and environmental conditions determine efficacy. DOI: [10.1002/advs.202306070](https://doi.org/10.1002/advs.202306070), published February 2024. (hu2024nanomaterialsregulatebacterial pages 1-2)

### Applications and implementation status

1. **Anti-virulence and antibiofilm therapy.** The principal strategy is to disarm pathogens rather than directly inhibit growth. Targets include synthases, signals, receptors, and downstream regulators. Biofilm-associated bacteria can exhibit approximately **1,000-fold greater antibiotic resistance/tolerance** than planktonic counterparts in the reviewed literature, motivating QQ, but this figure is context-dependent and should not be treated as a universal fold change. DOI: [10.3390/ijms25052655](https://doi.org/10.3390/ijms25052655), February 2024. (juszczukkubiak2024molecularaspectsof pages 2-3)
2. **Aquaculture biocontrol.** Signal antagonists and signal-degrading bacteria are being developed against Harveyi- and Splendidus-clade vibrios that cause disease in shrimp, fish, oysters, and sea cucumbers. The authoritative 2023 review characterizes the approach as promising but largely an antivirulence/biocontrol research strategy rather than a universally validated commercial replacement for antibiotics. DOI: [10.1111/raq.12787](https://doi.org/10.1111/raq.12787), January 2023. (zhang2023quorum‐sensinginterferencein pages 1-5)
3. **Agriculture and plant disease.** AHL- and diffusible-signal-factor quenching microbes or enzymes are investigated for phytopathogen control. A 2023 review also describes applications in aquaculture and membrane bioreactors. DOI: [10.3389/fpls.2022.1063393](https://doi.org/10.3389/fpls.2022.1063393), published January 2023.
4. **Wastewater and membrane-bioreactor biofouling control.** QQ bacteria and immobilized signal-degrading enzymes are tested to disrupt AHL-dependent biofilm development. Implementations remain reactor-, community-, and material-specific; community-wide ecological effects must be measured rather than inferred from a single reporter strain.
5. **Nanomaterial-enabled QQ.** Nanoparticles and nanocomposites can adsorb or degrade signals, inhibit signal synthesis, or interfere with receptor/transduction steps. Expert reviews warn that activity cannot be generalized by material class. Silver nanoparticles may accumulate in organs, and aluminum oxide nanoparticles can cause oxidative stress; resistance evolution under chronic nanoparticle exposure also remains insufficiently resolved. (hu2024nanomaterialsregulatebacterial pages 1-2, juszczukkubiak2024molecularaspectsof pages 16-18)
6. **Probiotics and phages.** Lactic-acid bacteria, including *Lactiplantibacillus plantarum* PA100, have been reported to interfere with AHL-dependent *P. aeruginosa* behavior; phage cocktails may penetrate established biofilms better than single phages. These effects may involve mechanisms beyond QS and should not be curated as QS edges without direct signal or receptor measurements. (juszczukkubiak2024molecularaspectsof pages 16-18)
7. **Device-associated infection control.** A 2023 report cited in the 2024 review used CRISPR/Cas9-HDR targeting QS and adhesion genes to reduce *E. coli* biofilm formation on urinary catheters. This is promising proof-of-concept rather than evidence of routine clinical deployment. (juszczukkubiak2024molecularaspectsof pages 40-40)
8. **Space microbiology.** The modeled-microgravity result is relevant to microbial control in crewed systems, but it was obtained in a low-shear ground model and two *S. aureus* strains. Its value for curation is primarily as an environmental perturbation of AIP synthesis. (green2023modelledmicrogravityreducesvirulence pages 1-2)

## Expert interpretation

The strongest current interpretation is that QS is **context-sensitive chemical decision-making**, not a literal cell counter. Signal abundance combines information about producer density, spatial geometry, transport, degradation, metabolic state, and past exposure. Recent authoritative work also shows extensive integration with global regulators such as CRP and with hierarchical post-transcriptional networks such as the Vibrio Qrr sRNAs. (walker2023asimplemechanism pages 1-2, eickhoff2021luxtcontrolsspecific pages 1-2)

Anti-QS treatment is attractive because it may impose less selection than bactericidal therapy, but “evolution-proof” is not justified. Resistance can arise through receptor alteration, signal overproduction, bypass regulation, altered efflux or permeability, or community protection. Translation is further constrained by bioavailability, toxicity, target specificity, polymicrobial signaling, and the possibility that suppressing one QS output favors another ecological state. Recent reviews specifically identify toxicity and bioavailability as barriers and call for mechanism- and environment-specific optimization. (hu2024nanomaterialsregulatebacterial pages 1-2, liu2025quorumsensingnot pages 14-15, zhang2023quorum‐sensinginterferencein pages 1-5)

## Warnings: claims not yet suitable for broad TraitMech curation

- Do **not** assert `high cell density causes quorum sensing` as an unconditional edge; add spatial/transport qualifiers.
- Do **not** make `quorum sensing is_a biofilm formation` or `QS always increases biofilm`. Direction and magnitude vary by species, stage, medium, and circuit.
- Do **not** infer QS solely from a `luxI`, `luxR`, `luxS`, or `agr` homolog. Demonstrate signal production and cognate response.
- Do **not** label AI-2 “universal interspecies communication” without taxon-specific receptor evidence. LuxS metabolic effects are a major confounder.
- Do **not** merge Vibrio LuxR/HapR master regulators with AHL-binding LuxR-family receptors merely because both are called “LuxR.” They are mechanistically distinct protein classes.
- Do **not** universalize the *A. fischeri* 3-oxo-C6-HSL pathway, *V. harveyi* three-channel phosphorelay, or *S. aureus* agr pathway to all bacteria.
- Do **not** curate generic “nanoparticle inhibits QS” edges. Record material composition, size/coating, concentration, organism, assay, affected QS step, and growth controls.
- Treat phenotypic memory as **model-supported/uncertain** unless the selected edge has direct experimental evidence.
- Distinguish QS inhibition from growth inhibition. Reduced reporter activity caused by toxicity is not specific quorum quenching.
- Avoid unverified CHEBI, UniProt, EC, Rhea, KEGG, or MetaCyc identifiers. Label-only nodes are preferable to incorrect grounding.

## DOI-first bibliography

1. Hu C, et al. “Nanomaterials Regulate Bacterial Quorum Sensing: Applications, Mechanisms, and Optimization Strategies.” *Advanced Science*. Published February 2024. [https://doi.org/10.1002/advs.202306070](https://doi.org/10.1002/advs.202306070). (hu2024nanomaterialsregulatebacterial pages 1-2)
2. Juszczuk-Kubiak E. “Molecular Aspects of the Functioning of Pathogenic Bacteria Biofilm Based on Quorum Sensing Signal-Response System and Innovative Non-Antibiotic Strategies for Their Elimination.” *International Journal of Molecular Sciences* 25:2655. Published February 2024. [https://doi.org/10.3390/ijms25052655](https://doi.org/10.3390/ijms25052655). (juszczukkubiak2024molecularaspectsof pages 2-3)
3. Ostovar G, Boedicker JQ. “Phenotypic memory in quorum sensing.” *PLOS Computational Biology* 20. Published November 2024. [https://doi.org/10.1371/journal.pcbi.1011696](https://doi.org/10.1371/journal.pcbi.1011696). (ostovar2024phenotypicmemoryin pages 1-2)
4. Walker LM, et al. “A simple mechanism for integration of quorum sensing and cAMP signalling in *Vibrio cholerae*.” *eLife* 12. Published July 2023. [https://doi.org/10.7554/eLife.86699](https://doi.org/10.7554/eLife.86699). (walker2023asimplemechanism pages 1-2)
5. Green MJ, et al. “Modelled-Microgravity Reduces Virulence Factor Production in *Staphylococcus aureus* through Downregulation of agr-Dependent Quorum Sensing.” *International Journal of Molecular Sciences* 24:15997. Published November 2023. [https://doi.org/10.3390/ijms242115997](https://doi.org/10.3390/ijms242115997). (green2023modelledmicrogravityreducesvirulence pages 1-2)
6. Zhang S, et al. “Quorum-sensing interference in vibrios.” *Reviews in Aquaculture* 15:1452–1466. Published January 2023. [https://doi.org/10.1111/raq.12787](https://doi.org/10.1111/raq.12787). (zhang2023quorum‐sensinginterferencein pages 1-5)
7. Zhu X, et al. “Innovative microbial disease biocontrol strategies mediated by quorum quenching and their multifaceted applications: A review.” *Frontiers in Plant Science* 13. Published January 2023. [https://doi.org/10.3389/fpls.2022.1063393](https://doi.org/10.3389/fpls.2022.1063393).
8. Eickhoff MJ, et al. “LuxT controls specific quorum-sensing-regulated behaviors in Vibrionaceae spp. via repression of qrr1.” *PLOS Genetics* 17:e1009336. Published April 2021. [https://doi.org/10.1371/journal.pgen.1009336](https://doi.org/10.1371/journal.pgen.1009336). (eickhoff2021luxtcontrolsspecific pages 1-2)
9. Chan K-G, Liu Y-C, Chang C-Y. “Inhibiting N-acyl-homoserine lactone synthesis and quenching Pseudomonas quinolone quorum sensing to attenuate virulence.” *Frontiers in Microbiology* 6. Published October 2015. [https://doi.org/10.3389/fmicb.2015.01173](https://doi.org/10.3389/fmicb.2015.01173). (chan2015inhibitingnacylhomoserinelactone pages 1-2)
10. Waters CM, Bassler BL. “Quorum Sensing: Cell-to-Cell Communication in Bacteria.” *Annual Review of Cell and Developmental Biology* 21. Published 2005. [https://doi.org/10.1146/annurev.cellbio.21.012704.131001](https://doi.org/10.1146/annurev.cellbio.21.012704.131001).
11. Miller MB, Bassler BL. “Quorum Sensing in Bacteria.” *Annual Review of Microbiology* 55. Published 2001. [https://doi.org/10.1146/annurev.micro.55.1.165](https://doi.org/10.1146/annurev.micro.55.1.165).

References

1. (juszczukkubiak2024molecularaspectsof pages 2-3): Edyta Juszczuk-Kubiak. Molecular aspects of the functioning of pathogenic bacteria biofilm based on quorum sensing (qs) signal-response system and innovative non-antibiotic strategies for their elimination. International Journal of Molecular Sciences, 25:2655, Feb 2024. URL: https://doi.org/10.3390/ijms25052655, doi:10.3390/ijms25052655. This article has 152 citations.

2. (ostovar2024phenotypicmemoryin pages 1-2): Ghazaleh Ostovar and James Q. Boedicker. Phenotypic memory in quorum sensing. PLOS Computational Biology, Nov 2024. URL: https://doi.org/10.1371/journal.pcbi.1011696, doi:10.1371/journal.pcbi.1011696. This article has 14 citations and is from a highest quality peer-reviewed journal.

3. (hu2024nanomaterialsregulatebacterial pages 1-2): Chen Hu, Guixin He, Yujun Yang, Ning Wang, Yanli Zhang, Yuan Su, Fujian Zhao, Junrong Wu, Linlin Wang, Yuqing Lin, and Longquan Shao. Nanomaterials regulate bacterial quorum sensing: applications, mechanisms, and optimization strategies. Advanced Science, Feb 2024. URL: https://doi.org/10.1002/advs.202306070, doi:10.1002/advs.202306070. This article has 65 citations and is from a peer-reviewed journal.

4. (chan2015inhibitingnacylhomoserinelactone pages 1-2): Kok-Gan Chan, Yi-Chia Liu, and Chien-Yi Chang. Inhibiting n-acyl-homoserine lactone synthesis and quenching pseudomonas quinolone quorum sensing to attenuate virulence. Frontiers in Microbiology, Oct 2015. URL: https://doi.org/10.3389/fmicb.2015.01173, doi:10.3389/fmicb.2015.01173. This article has 112 citations and is from a peer-reviewed journal.

5. (eickhoff2021luxtcontrolsspecific pages 1-2): Michaela J. Eickhoff, Chenyi Fei, Xiuliang Huang, and Bonnie L. Bassler. Luxt controls specific quorum-sensing-regulated behaviors in vibrionaceae spp. via repression of qrr1, encoding a small regulatory rna. PLOS Genetics, 17:e1009336, Apr 2021. URL: https://doi.org/10.1371/journal.pgen.1009336, doi:10.1371/journal.pgen.1009336. This article has 21 citations and is from a domain leading peer-reviewed journal.

6. (walker2023asimplemechanism pages 1-2): Lucas M Walker, James RJ Haycocks, Julia C Van Kessel, Triana N Dalia, Ankur B Dalia, and David C Grainger. A simple mechanism for integration of quorum sensing and camp signalling in vibrio cholerae. eLife, Jul 2023. URL: https://doi.org/10.7554/elife.86699, doi:10.7554/elife.86699. This article has 20 citations and is from a domain leading peer-reviewed journal.

7. (juszczukkubiak2024molecularaspectsof pages 5-7): Edyta Juszczuk-Kubiak. Molecular aspects of the functioning of pathogenic bacteria biofilm based on quorum sensing (qs) signal-response system and innovative non-antibiotic strategies for their elimination. International Journal of Molecular Sciences, 25:2655, Feb 2024. URL: https://doi.org/10.3390/ijms25052655, doi:10.3390/ijms25052655. This article has 152 citations.

8. (green2023modelledmicrogravityreducesvirulence pages 1-2): Macauley J. Green, Ewan J. Murray, Paul Williams, Amir M. Ghaemmaghami, Jonathan W. Aylott, and Philip M. Williams. Modelled-microgravity reduces virulence factor production in staphylococcus aureus through downregulation of agr-dependent quorum sensing. International Journal of Molecular Sciences, 24:15997, Nov 2023. URL: https://doi.org/10.3390/ijms242115997, doi:10.3390/ijms242115997. This article has 11 citations.

9. (liu2025quorumsensingnot pages 2-6): Derun Liu, Yonglin Lu, Ziyun Li, Xin Pang, and Xueyan Gao. Quorum sensing: not just a bridge between bacteria. MicrobiologyOpen, Feb 2025. URL: https://doi.org/10.1002/mbo3.70016, doi:10.1002/mbo3.70016. This article has 45 citations and is from a peer-reviewed journal.

10. (zhang2023quorum‐sensinginterferencein pages 1-5): Shanshan Zhang, Qian Yang, Mieke Eggermont, and Tom Defoirdt. Quorum‐sensing interference in vibrios. Reviews in Aquaculture, 15:1452-1466, Jan 2023. URL: https://doi.org/10.1111/raq.12787, doi:10.1111/raq.12787. This article has 23 citations and is from a domain leading peer-reviewed journal.

11. (juszczukkubiak2024molecularaspectsof pages 16-18): Edyta Juszczuk-Kubiak. Molecular aspects of the functioning of pathogenic bacteria biofilm based on quorum sensing (qs) signal-response system and innovative non-antibiotic strategies for their elimination. International Journal of Molecular Sciences, 25:2655, Feb 2024. URL: https://doi.org/10.3390/ijms25052655, doi:10.3390/ijms25052655. This article has 152 citations.

12. (juszczukkubiak2024molecularaspectsof pages 40-40): Edyta Juszczuk-Kubiak. Molecular aspects of the functioning of pathogenic bacteria biofilm based on quorum sensing (qs) signal-response system and innovative non-antibiotic strategies for their elimination. International Journal of Molecular Sciences, 25:2655, Feb 2024. URL: https://doi.org/10.3390/ijms25052655, doi:10.3390/ijms25052655. This article has 152 citations.

13. (liu2025quorumsensingnot pages 14-15): Derun Liu, Yonglin Lu, Ziyun Li, Xin Pang, and Xueyan Gao. Quorum sensing: not just a bridge between bacteria. MicrobiologyOpen, Feb 2025. URL: https://doi.org/10.1002/mbo3.70016, doi:10.1002/mbo3.70016. This article has 45 citations and is from a peer-reviewed journal.