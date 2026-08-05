---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:03:56.190228'
end_time: '2026-08-04T09:14:28.428741'
duration_seconds: 632.24
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: motile
  trait_identifier: METPO:1000702
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: motile
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A motility in which an organism has the ability to move independently
    using metabolic energy.
  parent_traits: METPO:1000701
  synonyms: 'yes'
  evidence_summary: 'DOI:10.1038/s41579-021-00626-4: physical and molecular mechanisms
    that allow bacteria to move around (Supports motile bacteria as organisms whose
    movement is mediated by specific molecular machines.) | PMID:34680106: Pseudomonas
    aeruginosa is a motile bacterium (Organism example: Pseudomonas aeruginosa is
    described as motile.)'
  causal_graph_summary: 'motile_energy_dependent_locomotion: 20 nodes, 19 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** motile
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000702
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism has the ability to move independently using metabolic energy.
- **Parent traits:** METPO:1000701
- **Synonyms:** yes
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: physical and molecular mechanisms that allow bacteria to move around (Supports motile bacteria as organisms whose movement is mediated by specific molecular machines.) | PMID:34680106: Pseudomonas aeruginosa is a motile bacterium (Organism example: Pseudomonas aeruginosa is described as motile.)
- **Existing causal graph summary:** motile_energy_dependent_locomotion: 20 nodes, 19 edges

## Research Objective

Research the microbial trait **motile** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/motile.yaml`.

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
- **Trait label:** motile
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000702
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism has the ability to move independently using metabolic energy.
- **Parent traits:** METPO:1000701
- **Synonyms:** yes
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: physical and molecular mechanisms that allow bacteria to move around (Supports motile bacteria as organisms whose movement is mediated by specific molecular machines.) | PMID:34680106: Pseudomonas aeruginosa is a motile bacterium (Organism example: Pseudomonas aeruginosa is described as motile.)
- **Existing causal graph summary:** motile_energy_dependent_locomotion: 20 nodes, 19 edges

## Research Objective

Research the microbial trait **motile** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/motile.yaml`.

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


# Curation report: microbial trait **motile**

**Target trait:** `METPO:1000702`  
**Category:** MORPHOLOGY · **Term kind:** CLASS · **Mapping:** REVIEWED  
**Definition supplied:** “A motility in which an organism has the ability to move independently using metabolic energy.”  
**Parent:** `METPO:1000701`

## Executive curation recommendation

`METPO:1000702` should represent an organism-level capacity for **active, metabolically energized displacement**, not merely movement observed in an assay. Its causal graph should be modular rather than imply that every motile microbe possesses the same machinery. High-confidence modules are: (1) ion-motive-force-driven bacterial flagellar locomotion; (2) ATP-driven type IV pilus (T4P) twitching; (3) ATP-powered archaeal motility, including archaella and the newly demonstrated Aap-pilus twitching mechanism; and (4) taxon-specific active gliding systems. Chemotaxis controls direction or switching but is neither necessary nor sufficient for the parent trait.

The central graph can therefore be expressed as:

**metabolic energy → motor activity → appendage or adhesion-system dynamics → propulsive force → cellular displacement → `METPO:1000702`.**

| module | energy input | core machinery | locomotion output | strongest recent evidence | curation confidence |
|---|---|---|---|---|---|
| Core Motility Graph Modules |  |  |  |  |  |
| Bacterial flagellar motility | Proton motive force / ion motive force | Flagellar motor stators MotAB and/or MotCD, rotor, flagellum | Swimming; in some taxa also swarming/surface spreading | Direct 2024 motor evidence in *Pseudomonas aeruginosa* shows two H+-driven stator systems with additive torque contributions; foundational reviews support IMF-to-rotation coupling (wu2024torquespeedrelationshipof pages 1-2, botting2023flgvformsa pages 1-2) | High |
| Bacterial T4P twitching | ATP | Type IV pilus machine with PilB extension ATPase, PilT primary retraction ATPase, PilU accessory retraction ATPase, T4P filament | Twitching surface translocation | 2024 reviews and experiments support ATPase-powered T4P cycles and surface-dependent twitching behavior (ohara2024surfacehydrophilicitypromotes pages 1-2, geiger2024abacterialsense pages 1-3) | High |
| Archaeal Aap twitching | ATP-linked; PilT-independent | AapF-dependent adhesion pili (Aap pili); no dedicated PilT homolog established | Twitching motility on surfaces | 2024 *Sulfolobus acidocaldarius* study shows retractable Aap pili drive twitching under physiological conditions despite lack of PilT homolog (charlesorszag2024adhesionpilusretraction pages 1-2) | Medium-High |
| Active gliding | Proton motive force (taxon-specific evidence) | Myxobacterial focal-adhesion-like gliding machinery; AgmT-linked coupling to peptidoglycan | Surface gliding | 2024 evidence supports PMF-coupled myxobacterial gliding machinery, but mechanisms are not unified across gliding taxa (rosko2025cellularcoordinationunderpins pages 16-17) | Medium |
| Boundary / non-trait movement | None intrinsic, or indirect colony-level physicochemical forcing | Growth-driven sliding; passive spreading / swashing-like colony expansion | Colony expansion without dedicated locomotor nanomachine | Reviews distinguish sliding as non-active; propulsion-independent spreading should be excluded from METPO:1000702 core mechanism graph (jin2024microbesinporous pages 14-18) | High for exclusion |


*Table: This table summarizes the main mechanistic modules relevant to curating the motile trait causal graph and separates core energy-dependent locomotion from excluded boundary phenomena. It is useful as a compact blueprint for which modules are ready for TraitMech curation and which require caution.*

## 1. Trait scope and boundaries

### Included phenotype

A microbial cell is *motile* when it can use metabolic energy to generate force that displaces itself relative to its surroundings. Included modes are:

- **Flagellar swimming** in liquid or hydrated matrices.
- **Flagellar swarming** where active flagellar propulsion is demonstrated.
- **T4P-dependent twitching**, generated by cycles of pilus extension, attachment, and retraction.
- **Archaellar swimming**, in which an ATP-powered rotating archaellum propels an archaeal cell.
- **Active gliding**, but only when a metabolically powered force-generating mechanism is established for the relevant taxon.

The phenotype is a **capacity**, so a genetically motile organism can appear stationary under conditions that suppress motor expression, energy supply, hydration, or mechanical coupling. Conversely, colony expansion does not prove intrinsic motility.

### Nearby traits that must remain distinct

1. **Chemotaxis:** biased orientation or switching in response to a chemical gradient. A cell may be motile but non-chemotactic, while intact chemosensory genes do not establish propulsion.
2. **Phototaxis, aerotaxis, mechanotaxis:** directional control layers upstream of a locomotor apparatus, not synonyms for motility.
3. **Sliding:** growth-driven colony expansion caused by division and surface forces. A 2024 review explicitly distinguishes sliding as non-active and mechanically driven by cell proliferation; exclude it from the core graph. (jin2024microbesinporous pages 14-18)
4. **Passive transport:** Brownian motion, sedimentation, bulk-flow advection, host-driven transport, or movement on a fluid wave does not meet the “using metabolic energy” definition.
5. **Swashing or osmotic spreading:** fermentation can indirectly generate osmotic gradients and fluid movement, but cells are carried by a colony-scale fluid mechanism rather than a dedicated locomotor motor. This is a boundary phenotype and should not be curated as direct evidence of `METPO:1000702` without single-cell evidence.
6. **Growth halo:** a soft-agar halo combines motility, growth, chemotaxis, agar structure, hydration, and nutrient effects. It is assay evidence, not itself the mechanism.
7. **Appendage presence:** flagella or pili seen by microscopy do not establish that the appendage is functional or that cells are motile.
8. **Intracellular molecular movement:** chromosome segregation, protein trafficking, and cytoplasmic streaming are not organismal locomotion.

## 2. Candidate graph nodes

Ontology identifiers are intentionally conservative. The supplied identifier `METPO:1000702` should be retained verbatim. Labels are preferable to guessed CURIEs; species-specific proteins should receive UniProt accessions only after strain-level verification.

### A. Trait and process nodes

- `METPO:1000702` — motile.
- Active cellular locomotion — label-only umbrella process.
- Flagellum-dependent swimming.
- Flagellum-dependent swarming.
- T4P-dependent twitching motility.
- Archaellum-dependent swimming.
- Active gliding motility.
- Flagellar rotation.
- T4P extension, surface attachment, and retraction.
- Chemotaxis — suggested grounding `GO:0006935`; curate as a regulator of trajectory, not as equivalent to motility.
- Surface colonization and host colonization — downstream consequences, taxon- and context-specific.

### B. Energy and chemical nodes

- ATP — suggested `CHEBI:15422`.
- ATP hydrolysis — molecular energy source for PilB/PilT-family motors and archaellar motors.
- Proton — suggested `CHEBI:15378`.
- Proton motive force (PMF) — label-only unless the project has an approved electrochemical-gradient ontology term.
- Sodium motive force — label-only; relevant to sodium-coupled bacterial flagellar stators, but not universal.
- Ion motive force — generic parent of proton- and sodium-coupled motor inputs.
- cAMP — regulatory second messenger in Pseudomonas surface adaptation; not a universal motility requirement.
- c-di-GMP — regulatory candidate that commonly reduces motile behavior, but effects are system- and taxon-specific.
- Bile salts/detergents and biosurfactants — environmental modifiers of surface wetting and mechanical coupling, not universal nutrients or energy sources.

### C. Machinery and cellular structures

**Bacterial flagellar module**

- Bacterial flagellum and filament.
- Flagellar motor.
- MotA/MotB proton-conducting stator complex.
- MotC/MotD alternative stator system in *Pseudomonas aeruginosa*.
- Rotor/C-ring proteins FliG, FliM, FliN/FliY.
- MS ring.
- FlgV accessory motor ring in Campylobacterota.
- Cytoplasmic membrane, peptidoglycan, and stator–cell-wall anchoring.

**T4P module**

- Type IV pilus filament.
- PilB extension ATPase.
- PilT primary retraction ATPase.
- PilU accessory retraction ATPase.
- PilQ secretin, PilC membrane platform, PilZ chaperone/regulator, PilY1 adhesin.
- Pil-Chp/PilJ surface-response pathway in *P. aeruginosa*.

**Archaeal module**

- Archaellum and ATP-powered archaellar motor.
- Adhesion/Aap pilus.
- AapF, required for Aap-pilus-dependent twitching in *Sulfolobus acidocaldarius*.
- PilT-independent pilus retraction mechanism — label as unresolved rather than assigning a motor.

**Gliding module**

- Myxobacterial focal-adhesion-like gliding complex.
- PMF-powered gliding motor.
- Peptidoglycan.
- AgmT lytic transglycosylase/coupling protein.
- Cyanobacterial T4P-like gliding system — separate, taxon-specific module with lower confidence.

### D. Environmental and assay nodes

- External viscosity and non-Newtonian rheology.
- Surface hydrophilicity.
- Surface moisture/water-film thickness.
- Agar concentration and composition.
- Mechanical load and physical confinement.
- Temperature and pH.
- Soft-agar motility assay.
- Interstitial twitching assay.
- Live-cell single-cell tracking.
- Optical trapping/torque–speed measurement.
- Cryo-electron tomography or in-situ motor structure.

### E. Taxon nodes requiring strain-aware grounding

- *Pseudomonas aeruginosa* PAO1/PA14.
- *Helicobacter pylori* B128 and G27M.
- *Campylobacter jejuni*.
- *Xanthomonas albilineans* JG43.
- *Sulfolobus acidocaldarius*.
- *Myxococcus xanthus*.
- *Acinetobacter nosocomialis* and *A. baumannii*.

NCBI Taxonomy CURIEs should be added through an authoritative lookup during YAML implementation; none should be inferred from species names alone.

## 3. Candidate causal edges

Predicates below are curation-oriented labels. “Direct” denotes a perturbation, physical measurement, or direct visualization; “supported” denotes a well-established mechanism summarized by the source; “uncertain” marks hypotheses or limited taxonomic transfer.

| # | Subject — predicate → object | Reference and supporting snippet | Curation notes |
|---:|---|---|---|
| 1 | Proton motive force — powers → MotAB/MotCD stator activity | Wu et al. 2024: both *P. aeruginosa* stator systems were “driven by H+ ions.” DOI: [10.1128/mbio.00745-24](https://doi.org/10.1128/mbio.00745-24), Dec 2024. (wu2024torquespeedrelationshipof pages 1-2) | **Direct; taxon-specific.** Do not assert that every flagellar motor is proton driven because sodium-coupled motors exist. |
| 2 | MotAB stator — generates → flagellar torque | The 2024 optical-trapping study measured torque–speed relationships for single-stator mutants and wild type. (wu2024torquespeedrelationshipof pages 1-2) | **Direct.** Appropriate intermediate between PMF and rotation. |
| 3 | MotCD stator — generates → flagellar torque | MotCD independently enabled swimming and had load-dependent catch-bond behavior. (wu2024torquespeedrelationshipof pages 1-2) | **Direct; P. aeruginosa.** |
| 4 | MotAB torque + MotCD torque — contributes additively to → wild-type motor torque | “The torque of the wild-type motor is similar to the combined torque” of the individual stator motors. (wu2024torquespeedrelationshipof pages 1-2) | **Direct quantitative motor result; P. aeruginosa PAO1.** Avoid universalizing dual stators. |
| 5 | Ion flow through MotA/MotB — drives → rotor rotation | Botting et al.: “Proton flow through the stator is thought to power rotation of the MotA pentamer around the stationary MotB dimer.” DOI: [10.1371/journal.pone.0287514](https://doi.org/10.1371/journal.pone.0287514), Nov 2023. (botting2023flgvformsa pages 1-2) | **Supported mechanism.** The wording “thought to” warrants mechanistic rather than experiment-specific confidence. |
| 6 | Flagellar rotation — drives → swimming displacement | *P. aeruginosa* measurements separately quantified cell-body and filament rotation in trapped swimming bacteria. (wu2024torquespeedrelationshipof pages 1-2) | **Direct physical link.** This is the terminal flagellar edge into motility. |
| 7 | FlgV ring — supports → efficient high-torque flagellar motor function | Δ*flgV* reduced soft-agar motility; FlgV formed a ring near the MS/C-ring junction. (botting2023flgvformsa pages 1-2) | **Direct but Campylobacterota-specific.** “Supports” is safer than “is required for motility,” because deletion reduced rather than universally abolished movement. |
| 8 | Flagellar motility — enables → *H. pylori* stomach colonization | “Flagella-driven motility is essential for *Helicobacter pylori* to colonize the human stomach.” (botting2023flgvformsa pages 1-2) | **Strong downstream application edge; organism-specific.** Not part of the minimal generic motility mechanism. |
| 9 | External viscosity — modulates → *C. jejuni* swimming velocity | *C. jejuni* reached approximately 50–100 µm/s in high-viscosity non-Newtonian fluids; Δ*vidA* was non-motile or slow at low viscosity but recovered wild-type velocity at high viscosity. DOI: [10.1128/mbio.02544-23](https://doi.org/10.1128/mbio.02544-23), Jan 2024. (ribardo2024viscositydependentdeterminantsof pages 1-2) | **Direct; strongly taxon-specific and non-monotonic.** Do not encode “viscosity inhibits motility” generically. |
| 10 | VidA — permits → efficient low-viscosity swimming | Δ*vidA* cells were non-motile or slow in low-viscosity media. (ribardo2024viscositydependentdeterminantsof pages 1-2) | **Direct deletion evidence; C. jejuni locus Cjj81176_0996.** |
| 11 | VidB activity — reduces → low-viscosity swimming velocity | Suppressors support a proposed “brake- or clutch-like” function for VidB. (ribardo2024viscositydependentdeterminantsof pages 1-2) | **Uncertain mechanism.** Curate as “negatively regulates” only with the species and low-viscosity condition attached. |
| 12 | ATP hydrolysis by PilB — drives → T4P extension | The 2024 surface-sensing review states that PilB is an ATP-hydrolysis-driven hexameric extension motor. DOI: [10.1128/jb.00442-23](https://doi.org/10.1128/jb.00442-23), Jul 2024. (geiger2024abacterialsense pages 1-3) | **High-confidence supported mechanism.** |
| 13 | ATP hydrolysis by PilT/PilU — drives → T4P retraction | PilT is the primary and PilU an accessory retraction motor; both are ATPase hexamers. (geiger2024abacterialsense pages 1-3) | **High confidence for P. aeruginosa-like bacterial T4P.** Not applicable to the PilT-lacking archaeal Aap system. |
| 14 | T4P extension–binding–retraction cycles — pull → cell across surface | Twitching is described as cooperative “binding, pulling, and unbinding” that moves the cell. (geiger2024abacterialsense pages 1-3) | **High-confidence process chain.** |
| 15 | Surface hydrophilicity — promotes → T4P twitching | Cells showed increased twitching on glass and tissue-culture-treated polystyrene; detergents acted by changing surface hydrophilicity rather than inducing a stress response. DOI: [10.1128/msphere.00390-24](https://doi.org/10.1128/msphere.00390-24), Sep 2024. (ohara2024surfacehydrophilicitypromotes pages 1-2) | **Direct but assay/environment dependent.** Applies to tested *Acinetobacter* and *Pseudomonas* strains. |
| 16 | VirB11 — promotes → flagellum assembly and T4P morphogenesis | Δ*virB11* lost swimming and twitching and failed to form flagella and normal T4P; 28 flagellar-assembly and 10 chemotaxis DEGs occurred among 123 total DEGs. DOI: [10.1111/mpp.70001](https://doi.org/10.1111/mpp.70001), Sep 2024. (li2024virb11atraffic pages 1-2) | **Direct phenotype and structure; regulatory mechanism partly inferred.** Restrict to *X. albilineans*. |
| 17 | Flagellum assembly + T4P morphogenesis — enables → swimming and twitching | Loss of both structures in Δ*virB11* accompanied loss of both motility modes without a discernible growth defect. (li2024virb11atraffic pages 1-2) | **Strong causal association**, although the pleiotropic mutation prevents assigning each phenotype solely to one downstream target. |
| 18 | AapF/Aap pili — enable → archaeal twitching motility | In *S. acidocaldarius*, retractable Aap pili drove twitching at 75 °C and pH 2; Δ*aapF* abolished twitching, with 46.2% of cells displaced <2 µm. DOI: [10.1038/s41467-024-49101-7](https://doi.org/10.1038/s41467-024-49101-7), Jun 2024. (charlesorszag2024adhesionpilusretraction pages 1-2) | **Direct.** A strong new archaeal module. |
| 19 | Aap pilus retraction — generates → twitching displacement | Retraction forces were approximately 100 pN, with speeds up to 1 µm/s; wild-type total displacement averaged 4.6–6.6 µm. (charlesorszag2024adhesionpilusretraction pages 1-2) | **Direct and quantitative.** Do not add PilT as the motor: this archaeon lacks a PilT homolog. |
| 20 | Myxobacterial PMF-powered gliding machinery — generates → active gliding | Evidence summarized that myxobacterial gliding requires PMF-powered machinery and focal-adhesion-like complexes. (rosko2025cellularcoordinationunderpins pages 16-17) | **Supported but taxon-specific.** Do not merge all forms of “gliding” into this mechanism. |
| 21 | AgmT-modified peptidoglycan — couples → gliding motor/focal-adhesion complex | 2024 work reports failure of gliding-motor connection and focal-adhesion assembly without active AgmT, with heterologous MltG rescuing gliding. DOI: [10.7554/eLife.99273.1](https://doi.org/10.7554/eLife.99273.1), Jul 2024. | **Promising direct evidence but version/status should be checked before production curation.** |
| 22 | T4P cycling — produces → approximately 1 µm/s twitching on moist surfaces | A 2024 porous-environment review reports T4P-powered twitching at about 1 µm/s. DOI: [10.1007/s12551-024-01185-7](https://doi.org/10.1007/s12551-024-01185-7), Apr 2024. (jin2024microbesinporous pages 14-18) | **Descriptive statistic.** Use primarily as contextual evidence, not a universal speed. |
| 23 | Growth and division — cause → passive sliding | Sliding is described as mechanically driven by cell division rather than an active motility machine. (jin2024microbesinporous pages 14-18) | **Exclusion edge.** Encode in a boundary/negative-evidence section, not as a route to `METPO:1000702`. |
| 24 | PilT-mediated surface engagement — may signal through → PilJ/Pil-Chp → cAMP | Geiger et al. propose that PilT relays surface engagement via PilJ, increasing cAMP. (geiger2024abacterialsense pages 1-3) | **Uncertain/proposed model.** Do not curate as settled causality without primary perturbation evidence for each link. |

## 4. Recommended minimal TraitMech graph

A compact first production graph should prioritize broadly supported edges and avoid joining mutually exclusive mechanisms into one linear chain:

### Shared trunk

1. Metabolic energy availability → enables motor activity.
2. Motor activity → generates mechanical force.
3. Mechanical force → causes cellular displacement.
4. Cellular displacement capacity → realizes `METPO:1000702`.

### Alternative mechanism branches

**Branch A — bacterial flagellum**  
Respiration/ion gradient → PMF or sodium motive force → stator ion flux → rotor torque → flagellar rotation → propulsion → swimming or active swarming → `METPO:1000702`.

**Branch B — bacterial T4P**  
ATP → PilB-dependent extension → surface attachment → PilT/PilU-dependent retraction → traction force → twitching displacement → `METPO:1000702`.

**Branch C — archaeal Aap twitching**  
ATP-linked Aap machinery → Aap-pilus extension/retraction → traction force → twitching displacement → `METPO:1000702`. The molecular retraction motor remains unresolved and must not be filled with PilT. (charlesorszag2024adhesionpilusretraction pages 1-2)

**Branch D — archaellum**  
ATP hydrolysis → archaellar motor rotation → archaellum rotation → swimming → `METPO:1000702`. This mechanism is well established but should be represented separately from the bacterial flagellum because the structures, assembly, and energy coupling differ.

**Branch E — active gliding**  
PMF or ATP, depending on taxon → taxon-specific gliding motor → substrate-coupled force transmission → gliding displacement → `METPO:1000702`. Keep separate subgraphs for myxobacteria and cyanobacteria because “gliding” is mechanistically heterogeneous. (rosko2025cellularcoordinationunderpins pages 16-17)

## 5. Recent developments, applications, and quantitative findings

### Major 2023–2024 advances

- **Dual-stator motor mechanics:** Optical trapping showed that *P. aeruginosa* MotAB and MotCD have different load-dependent binding behavior and contribute approximately additive torque. This explains environmental adaptability more mechanistically than a simple presence/absence model of flagella. (wu2024torquespeedrelationshipof pages 1-2)
- **Viscosity-specific motor control:** *C. jejuni* does not follow a generic “higher viscosity means slower swimming” rule. VidA and VidB modulate performance so that cells can attain roughly 50–100 µm/s in high-viscosity non-Newtonian environments, compared with approximately 35–45 µm/s cited for *E. coli* and *Salmonella*. (ribardo2024viscositydependentdeterminantsof pages 1-2)
- **Archaeal twitching without PilT:** *S. acidocaldarius* Aap pili retract and propel cells despite the absence of a PilT homolog, overturning the assumption that archaeal adhesion pili cannot power twitching. Retraction generated approximately 100 pN and speeds up to 1 µm/s under 75 °C, pH 2 conditions. (charlesorszag2024adhesionpilusretraction pages 1-2)
- **Surface physics as part of phenotype expression:** Surface hydrophilicity, rather than a detergent-induced cellular stress program, promoted twitching in three tested opportunistic pathogens. This demonstrates that assay material is a causal experimental factor. (ohara2024surfacehydrophilicitypromotes pages 1-2)
- **Cross-system regulation:** In the sugarcane pathogen *X. albilineans*, VirB11 deletion disrupted both flagella and T4P, eliminated swimming and twitching, and changed 123 transcripts, connecting assembly systems, motility, and virulence while also illustrating pleiotropy. (li2024virb11atraffic pages 1-2)

### Real-world implementations and uses

- **Pathogenesis and anti-virulence discovery:** Flagellar and T4P motility support host entry, tissue navigation, surface sensing, and biofilm initiation. *H. pylori* flagellar motility is essential for gastric colonization, while T4P systems are important virulence determinants and potential targets for disabling surface colonization without directly inhibiting growth. (botting2023flgvformsa pages 1-2, geiger2024abacterialsense pages 1-3)
- **Plant disease and agriculture:** Motility contributes to colonization by rhizobacteria and plant pathogens. The *X. albilineans* VirB11 result links swimming/twitching to sugarcane leaf-scald virulence and identifies a mechanistic intervention point. (li2024virb11atraffic pages 1-2)
- **Medical-device and tissue-surface design:** The finding that hydrophilic surfaces enhance T4P functionality implies that implant materials and tissue-like surfaces can alter colonization behavior; surface chemistry should therefore be treated as an experimental and engineering variable. (ohara2024surfacehydrophilicitypromotes pages 1-2)
- **Environmental transport:** In soil, mucus, and porous materials, pore geometry, rheology, hydration, and surface interactions alter microbial dispersal. Models based solely on dilute-liquid swimming will not transfer reliably to these environments. (ribardo2024viscositydependentdeterminantsof pages 1-2, jin2024microbesinporous pages 14-18)
- **Phenotyping and diagnostics:** Soft-agar halos remain useful screening tools, but live-cell tracking, optical trapping, and structural imaging are needed to separate growth, chemotaxis, propulsion, and motor mechanics. The 2024 *P. aeruginosa* optical-trapping method directly measured cell-body and filament rotation while avoiding bead-labeling limitations. (wu2024torquespeedrelationshipof pages 1-2)

## 6. Expert analysis

The current literature supports treating “motile” as a **mechanistically plural capability** rather than a single conserved pathway. The most transferable causal abstraction is energy conversion into mechanical force and displacement. Genes such as *motA*, *motB*, *pilB*, or *pilT* belong in mechanism-specific branches and should not be asserted as universal determinants.

Environmental variables should be modeled as **contextual modifiers**, not intrinsic causes of the trait. Viscosity can enhance *C. jejuni* velocity, hydrophilicity can promote twitching, and moisture can enable swarming, but each effect depends on organism, motor, and assay geometry. (ribardo2024viscositydependentdeterminantsof pages 1-2, jin2024microbesinporous pages 14-18, ohara2024surfacehydrophilicitypromotes pages 1-2)

For genotype-to-trait curation, direct loss-of-function evidence is strongest when growth is unchanged and the motor or appendage defect is independently confirmed. Δ*virB11*, for example, has useful evidence because growth was not discernibly affected and microscopy showed appendage defects, but its transcriptomic pleiotropy means the edge should be “VirB11 promotes assembly/morphogenesis,” not “VirB11 directly powers movement.” (li2024virb11atraffic pages 1-2)

## 7. Claims that should **not yet** be curated

1. **Do not equate chemotaxis with motility.** Chemotaxis is a directional-control phenotype.
2. **Do not curate colony expansion alone as active motility.** Exclude growth-driven sliding, osmotic swashing, surfactant-driven passive spreading, and bulk-flow transport unless active single-cell propulsion is demonstrated. (jin2024microbesinporous pages 14-18)
3. **Do not make PMF universal.** Bacterial flagella may use H+ or Na+; T4P and archaella use ATP-dependent machinery.
4. **Do not assign PilT to archaeal Aap retraction.** *S. acidocaldarius* lacks a PilT homolog; the retraction mechanism remains unresolved. (charlesorszag2024adhesionpilusretraction pages 1-2)
5. **Do not unify all gliding mechanisms.** Reviews explicitly note that a clear general mechanism remains unresolved; myxobacterial PMF-based focal adhesions and cyanobacterial T4P-like gliding require separate taxon-qualified branches. (jin2024microbesinporous pages 14-18, rosko2025cellularcoordinationunderpins pages 16-17)
6. **Do not curate VidB as a definitive molecular brake without qualification.** Its brake/clutch activity is proposed from suppressor evidence and is restricted to *C. jejuni* under low-viscosity conditions. (ribardo2024viscositydependentdeterminantsof pages 1-2)
7. **Do not make surface hydrophilicity universally activating.** The result is strong for the tested interstitial twitching systems but depends on surface material and taxa. (ohara2024surfacehydrophilicitypromotes pages 1-2)
8. **Do not interpret every VirB11 ortholog as a motility determinant.** The demonstrated effect is in *X. albilineans* and is pleiotropic. (li2024virb11atraffic pages 1-2)
9. **Do not assign ontology identifiers by name similarity.** Verify GO, UniProt, KEGG, Rhea, and NCBI Taxonomy records against the exact organism, strain, and protein.
10. **Do not use preprints or reviewed-version DOIs interchangeably.** For the Aap study, use the peer-reviewed DOI `10.1038/s41467-024-49101-7`, not the earlier bioRxiv DOI. (charlesorszag2024adhesionpilusretraction pages 1-2, charlesorszag2023sulfolobusacidocaldariusadhesion pages 2-3)

## DOI-first bibliography

1. Wu H, Wu Z, Tian M, Zhang R, Yuan J. “Torque-speed relationship of the flagellar motor with dual-stator systems in *Pseudomonas aeruginosa*.” *mBio* 15. **December 2024.** DOI: [10.1128/mbio.00745-24](https://doi.org/10.1128/mbio.00745-24). (wu2024torquespeedrelationshipof pages 1-2)
2. Ribardo DA, Johnson JJ, Hendrixson DR. “Viscosity-dependent determinants of *Campylobacter jejuni* impacting the velocity of flagellar motility.” *mBio* 15. **January 2024.** DOI: [10.1128/mbio.02544-23](https://doi.org/10.1128/mbio.02544-23). (ribardo2024viscositydependentdeterminantsof pages 1-2)
3. Charles-Orszag A et al. “Adhesion pilus retraction powers twitching motility in the thermoacidophilic crenarchaeon *Sulfolobus acidocaldarius*.” *Nature Communications* 15. **June 2024.** DOI: [10.1038/s41467-024-49101-7](https://doi.org/10.1038/s41467-024-49101-7). (charlesorszag2024adhesionpilusretraction pages 1-2)
4. Li M et al. “VirB11, a traffic ATPase, mediated flagella assembly and type IV pilus morphogenesis to control the motility and virulence of *Xanthomonas albilineans*.” *Molecular Plant Pathology* 25. **September 2024.** DOI: [10.1111/mpp.70001](https://doi.org/10.1111/mpp.70001). (li2024virb11atraffic pages 1-2)
5. O’Hara MT et al. “Surface hydrophilicity promotes bacterial twitching motility.” *mSphere* 9. **September 2024.** DOI: [10.1128/msphere.00390-24](https://doi.org/10.1128/msphere.00390-24). (ohara2024surfacehydrophilicitypromotes pages 1-2)
6. Geiger CJ, Wong GCL, O’Toole GA. “A bacterial sense of touch: T4P retraction motor as a means of surface sensing by *Pseudomonas aeruginosa* PA14.” *Journal of Bacteriology* 206. **July 2024.** DOI: [10.1128/jb.00442-23](https://doi.org/10.1128/jb.00442-23). (geiger2024abacterialsense pages 1-3)
7. Jin C, Sengupta A. “Microbes in porous environments: from active interactions to emergent feedback.” *Biophysical Reviews* 16:173–188. **April 2024.** DOI: [10.1007/s12551-024-01185-7](https://doi.org/10.1007/s12551-024-01185-7). (jin2024microbesinporous pages 14-18)
8. Botting JM et al. “FlgV forms a flagellar motor ring that is required for optimal motility of *Helicobacter pylori*.” *PLOS ONE* 18:e0287514. **November 2023.** DOI: [10.1371/journal.pone.0287514](https://doi.org/10.1371/journal.pone.0287514). (botting2023flgvformsa pages 1-2)
9. Ramirez Carbo C, Faromiki OG, Nan B. “A lytic transglycosylase connects bacterial focal adhesion complexes to the peptidoglycan cell wall.” **July 2024 version.** DOI: [10.7554/eLife.99273.1](https://doi.org/10.7554/eLife.99273.1). Publication/version status should be verified before production curation.
10. Wadhwa N, Berg HC. “Bacterial motility: links to the environment and a driving force for microbial physics.” *Nature Reviews Microbiology*. **2022 issue; published online 2021.** DOI: [10.1038/s41579-021-00626-4](https://doi.org/10.1038/s41579-021-00626-4). This is the supplied foundational evidence for physical and molecular motility mechanisms.

References

1. (wu2024torquespeedrelationshipof pages 1-2): Haolin Wu, Zhengyu Wu, Maojin Tian, Rongjing Zhang, and Junhua Yuan. Torque-speed relationship of the flagellar motor with dual-stator systems in <i>pseudomonas aeruginosa</i>. Dec 2024. URL: https://doi.org/10.1128/mbio.00745-24, doi:10.1128/mbio.00745-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

2. (botting2023flgvformsa pages 1-2): Jack M. Botting, Shoichi Tachiyama, Katherine H. Gibson, Jun Liu, Vincent J. Starai, and Timothy R. Hoover. Flgv forms a flagellar motor ring that is required for optimal motility of helicobacter pylori. PLOS ONE, 18:e0287514, Nov 2023. URL: https://doi.org/10.1371/journal.pone.0287514, doi:10.1371/journal.pone.0287514. This article has 9 citations and is from a peer-reviewed journal.

3. (ohara2024surfacehydrophilicitypromotes pages 1-2): Megan T. O'Hara, Tori M. Shimozono, Keane J. Dye, David Harris, and Zhaomin Yang. Surface hydrophilicity promotes bacterial twitching motility. Sep 2024. URL: https://doi.org/10.1128/msphere.00390-24, doi:10.1128/msphere.00390-24. This article has 13 citations and is from a peer-reviewed journal.

4. (geiger2024abacterialsense pages 1-3): C. J. Geiger, G. C. L. Wong, and G. A. O'Toole. A bacterial sense of touch: t4p retraction motor as a means of surface sensing by <i>pseudomonas aeruginosa</i> pa14. Journal of Bacteriology, Jul 2024. URL: https://doi.org/10.1128/jb.00442-23, doi:10.1128/jb.00442-23. This article has 22 citations and is from a peer-reviewed journal.

5. (charlesorszag2024adhesionpilusretraction pages 1-2): Arthur Charles-Orszag, Marleen van Wolferen, Samuel J. Lord, Sonja-Verena Albers, and R. Dyche Mullins. Adhesion pilus retraction powers twitching motility in the thermoacidophilic crenarchaeon sulfolobus acidocaldarius. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49101-7, doi:10.1038/s41467-024-49101-7. This article has 12 citations and is from a highest quality peer-reviewed journal.

6. (rosko2025cellularcoordinationunderpins pages 16-17): Jerko Rosko, Kelsey Cremin, Emanuele Locatelli, Rebecca N. Poon, Mary Coates, Sarah J. N. Duxbury, Kieran Randall, Katie Croft, Chantal Valeriani, Marco Polin, and Orkun S. Soyer. Cellular coordination underpins rapid reversals in gliding filamentous cyanobacteria and its loss results in plectonemes. eLife, Mar 2025. URL: https://doi.org/10.1101/2024.02.06.579126, doi:10.1101/2024.02.06.579126. This article has 3 citations and is from a domain leading peer-reviewed journal.

7. (jin2024microbesinporous pages 14-18): Chenyu Jin and Anupam Sengupta. Microbes in porous environments: from active interactions to emergent feedback. Biophysical Reviews, 16:173-188, Apr 2024. URL: https://doi.org/10.1007/s12551-024-01185-7, doi:10.1007/s12551-024-01185-7. This article has 42 citations and is from a peer-reviewed journal.

8. (ribardo2024viscositydependentdeterminantsof pages 1-2): Deborah A. Ribardo, Jeremiah J. Johnson, and David R. Hendrixson. Viscosity-dependent determinants of <i>campylobacter jejuni</i> impacting the velocity of flagellar motility. Jan 2024. URL: https://doi.org/10.1128/mbio.02544-23, doi:10.1128/mbio.02544-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

9. (li2024virb11atraffic pages 1-2): Meilin Li, Liya Xiong, Wenhan Chen, YiSha Li, Abdullah Khan, Charles A. Powell, Baoshan Chen, and Muqing Zhang. Virb11, a traffic atpase, mediated flagella assembly and type iv pilus morphogenesis to control the motility and virulence of xanthomonas albilineans. Molecular Plant Pathology, Sep 2024. URL: https://doi.org/10.1111/mpp.70001, doi:10.1111/mpp.70001. This article has 4 citations and is from a peer-reviewed journal.

10. (charlesorszag2023sulfolobusacidocaldariusadhesion pages 2-3): Arthur Charles-Orszag, Marleen van Wolferen, Samuel J. Lord, Sonja-Verena Albers, and Dyche Mullins. Sulfolobus acidocaldarius adhesion pili power twitching motility in the absence of a dedicated retraction atpase. bioRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.04.552066, doi:10.1101/2023.08.04.552066. This article has 10 citations.