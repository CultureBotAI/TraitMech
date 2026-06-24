---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:30:05.169212'
end_time: '2026-06-18T08:43:47.255362'
duration_seconds: 822.09
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'motile_energy_dependent_locomotion: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** motile
- **METPO identifier:** METPO:1000702
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism has the ability to move independently using metabolic energy.
- **Parent traits:** METPO:1000701
- **Synonyms:** yes
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: physical and molecular mechanisms that allow bacteria to move around (Supports motile bacteria as organisms whose movement is mediated by specific molecular machines.) | PMID:34680106: Pseudomonas aeruginosa is a motile bacterium (Organism example: Pseudomonas aeruginosa is described as motile.)
- **Existing causal graph summary:** motile_energy_dependent_locomotion: 6 nodes, 5 edges

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
- **METPO identifier:** METPO:1000702
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism has the ability to move independently using metabolic energy.
- **Parent traits:** METPO:1000701
- **Synonyms:** yes
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: physical and molecular mechanisms that allow bacteria to move around (Supports motile bacteria as organisms whose movement is mediated by specific molecular machines.) | PMID:34680106: Pseudomonas aeruginosa is a motile bacterium (Organism example: Pseudomonas aeruginosa is described as motile.)
- **Existing causal graph summary:** motile_energy_dependent_locomotion: 6 nodes, 5 edges

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


## Research report: microbial trait **motile** (METPO:1000702)

### 0) Executive scope summary
The METPO trait **motile** refers to energy-dependent, self-propelled locomotion of a microorganism. Current mechanistic understanding supports multiple distinct locomotion “implementations” under this trait label: (i) **flagellar motility** (rotary ion-motive-force-driven motor), including swimming in liquids and movement on/over surfaces; (ii) **type IV pilus (T4P)-based twitching** (ATPase-driven extension/retraction cycles producing surface translocation); (iii) **Bacteroidota gliding motility** (proton-gradient-driven rotary motor powering surface adhesin motion); and (iv) **archaeal motility systems**, notably **archaella** (rotary propellers) and retractile pili enabling twitching-like surface migration. A key boundary case for curation is that **non-flagellated ≠ non-motile**, because motility can be achieved by pili or gliding systems even when flagella are absent. (ramoneda2024ecologicalrelevanceof pages 5-6, thunes2024glidingmotilityproteins pages 1-2, ohara2024surfacehydrophilicitypromotes pages 1-2, charlesorszag2024adhesionpilusretraction pages 1-2)

---

## 1) Key concepts and definitions (current understanding)

### 1.1 What phenotype the trait represents
*Motile* should be curated as an organism-level **capacity for autonomous movement** (powered by metabolism) rather than a specific structure such as “flagellated.” Mechanistically, bacteria are explicitly described as able to “**swim in liquids and move over solid surfaces by rotating flagella**,” tying motility to flagellar rotation in many taxa. (nakamura2024structureanddynamics pages 1-3)

### 1.2 Distinguishing motility from nearby traits
- **Motile vs chemotactic:** chemotaxis is a **signal transduction/regulatory system** that biases motility direction by modulating motor switching; it is not itself the propulsion mechanism. Chemoreceptors regulate CheA kinase activity; CheA phosphorylates CheY; CheY-P binds the C-ring/switch to change rotation direction. (nakamura2024structureanddynamics pages 1-3, johnson2024structuralbasisof pages 1-5)
- **Motile vs flagellated:** a taxon may lack flagella but still be motile via gliding or pili. This is explicitly emphasized in soil-genome inference work: “**being nonflagellated does not mean taxa are nonmotile**” (example given: Bacteroidota gliding). (ramoneda2024ecologicalrelevanceof pages 5-6, thunes2024glidingmotilityproteins pages 1-2)
- **Motile vs surface spreading/sliding:** some surface motility modes are flagella-dependent and also require environmental wetting agents/surfactants; careful curation should avoid equating “surface spreading” with intrinsic propulsion without assay context. (jin2024microbesinporous pages 14-18)

### 1.3 Assay-observed property vs genomic inference
Motility is often observed in wet-lab assays (swim plates, twitching stab assays, live imaging), but recent work also supports **genome-based inference** of the *capacity for flagellar motility* from conserved gene repertoires, and metagenome-based inference of community prevalence. (ramoneda2024ecologicalrelevanceof pages 5-6, ramoneda2024ecologicalrelevanceof pages 1-2)

---

## 2) Recent developments and latest research (prioritize 2023–2024)

### 2.1 Flagellar motor: structure, energetics, and switching (2024)
- **Energetics and core architecture:** a common model is an ion-motive-force-driven rotary motor. The flagellar basal body motor is “**powered by a transmembrane electrochemical gradient of ions such as protons (H+) and sodium ions (Na+)**.” (nakamura2024structureanddynamics pages 1-3)
- **Stator stoichiometry and function:** the stator complex is described as “**composed of 5 MotA proteins and 2 MotB proteins**,” anchored via MotB’s peptidoglycan-binding domain; it “**can act as a transmembrane H+ channel**” and conducts H+ to generate torque via interactions with FliG. (nakamura2024structureanddynamics pages 1-3)
- **Directional switching mechanism:** CheA→CheY phosphorylation and CheY-P binding is directly linked to reversal. CheY-P binding to the basal body/C-ring can produce “**full reversal of the direction of rotation ... from the default counter-clockwise (CCW) ... to clockwise (CW)**,” and the response can be highly cooperative (Hill coefficient up to 21 with respect to CheY-P concentration). (johnson2024structuralbasisof pages 1-5)

### 2.2 Motility adaptation to mechanical load/viscosity (2024)
- **Stator recruitment with load:** stators are dynamic and load-responsive; increased load can recruit up to ~11 stators in Salmonella (used as a quantitative exemplar). (johnson2024structuralbasisof pages 1-5)
- **Viscosity-dependent swimming in Campylobacter:** *Campylobacter jejuni* swimming velocity can increase markedly in high-viscosity non-Newtonian fluids; the study reports **50–100 µm/s** in high-viscosity non-Newtonian fluids (contrasted with ~35–45 µm/s for *Salmonella/E. coli*). The work identifies VidA/VidB as auxiliary modulators controlling low-viscosity behavior (VidA required for low-viscosity swimming; VidB proposed brake/clutch). (ribardo2024viscositydependentdeterminantsof pages 1-2)
- **Dual-stator specialization in Pseudomonas:** in *Pseudomonas aeruginosa*, MotAB vs MotCD stators enable torque tuning across load regimes; solvent isotope and pH perturbations implicate proton-transfer/PMF components as rate-limiting in certain regimes, and Ficoll concentrations are used to define load conditions. (wu2024torquespeedrelationshipof pages 13-15)

### 2.3 Chemosensory system diversity: CheA domain architectures (2024)
A major 2024 contribution is a genome-wide architecture survey of CheA (central to chemosensory pathways): a final dataset of **13,673 CheA sequences** from **6,896 bacterial** and **471 archaeal** genomes is reported; only **46%** retain the classical five-domain architecture; nearly **52%** lack the P2/CheY-binding domain; a CheY-like receiver domain occurs in ~**34–35%**; CheW was detected in **100%** of sequences; and **18%** contain ≥2 Hpt domains. (berry2024diversedomainarchitectures pages 3-6, berry2024diversedomainarchitectures pages 8-10, berry2024diversedomainarchitectures pages 6-8)

### 2.4 Non-flagellar motility mechanisms (2024)
- **T4P twitching:** twitching is defined as surface translocation powered by T4P extension/retraction, involving PilB (extension ATPase) and PilT (retraction ATPase). (ohara2024surfacehydrophilicitypromotes pages 1-2)
- **Surface physicochemistry:** bile salts and other detergents can enhance twitching not via a stress response but by increasing **surface hydrophilicity**, and hydrophilic surfaces (glass, treated plastics) can promote twitching without detergents—an important assay/environment dependency for curation. (ohara2024surfacehydrophilicitypromotes pages 1-2)
- **Bacteroidota gliding/T9SS intersection:** gliding in *Flavobacterium columnare* is tied to surface adhesins (SprB) and a proton-gradient-driven rotary motor (GldL/GldM). Genetic separation of secretion vs gliding supports that motility itself can contribute to virulence. (thunes2024glidingmotilityproteins pages 1-2)

### 2.5 Archaeal motility updates (2024)
- **Archaeal twitching via retractile pili:** *Sulfolobus acidocaldarius* shows twitching motility driven by retractable Aap pili under physiologically relevant conditions (75 °C, pH 2), despite the absence of PilT homologs; deletion of AapF abolishes twitching and quantitative tracking differences are reported. (charlesorszag2024adhesionpilusretraction pages 1-2)
- **Post-translational modification impacts motility:** N-glycan truncation on *Halobacterium salinarum* archaellins yields altered swimming behavior (loss of stable unidirectional motility; direction changes within limited area) and filament clustering; authors propose glycans act as spacers limiting filament aggregation. (sofer2024perturbednglycosylationof pages 1-2)

---

## 3) Current applications and real-world implementations

### 3.1 Trait inference in ecology and microbiome datasets
A 2024 ISME Journal study demonstrates a **genome-based approach** to infer flagellar motility capacity across large genome collections and then quantify prevalence in metagenomes across soil carbon gradients, validated with glucose-amendment incubations. This is directly relevant to curating motile as a trait that can be inferred computationally (with explicit limitations). (ramoneda2024ecologicalrelevanceof pages 5-6, ramoneda2024ecologicalrelevanceof pages 1-2)

### 3.2 Methods enabling mechanistic measurements
A 2024 mBio study develops an optical trapping/labeling approach to quantify torque-speed relationships in a dual-stator system, illustrating how modern biophysical instrumentation supports mechanistic edges (e.g., load dependence, pH effects). (wu2024torquespeedrelationshipof pages 13-15)

### 3.3 Clinical/industrial relevance via surface interactions
T4P-dependent twitching is sensitive to surface hydrophilicity, implying that tissue/implant materials can modulate pilus-driven motility (and thus colonization behaviors) through physicochemical surface properties. (ohara2024surfacehydrophilicitypromotes pages 1-2)

---

## 4) Expert opinions and analysis (authoritative synthesis)

### 4.1 Motility as modular: propulsion + regulation + environment
Across 2024 sources, a consistent conceptual model emerges:
1) **Propulsion module:** motor/filament system (flagellum; T4P; gliding motor/adhesin track; archaellum).
2) **Regulatory module:** chemosensory/chemotaxis signaling tunes directionality and behavioral outputs (CheA/CheY switching; diverse CheA architectures). (nakamura2024structureanddynamics pages 1-3, johnson2024structuralbasisof pages 1-5, berry2024diversedomainarchitectures pages 3-6)
3) **Environmental/mechanical coupling:** load, viscosity, and surface physicochemistry change effective motility and can recruit different mechanical states (stator recruitment; dual stator swapping; hydrophilicity effects on twitching). (wu2024torquespeedrelationshipof pages 13-15, ribardo2024viscositydependentdeterminantsof pages 1-2, ohara2024surfacehydrophilicitypromotes pages 1-2, johnson2024structuralbasisof pages 1-5)

### 4.2 Curation implication
For a TraitMech causal graph, it is more robust to curate motility as a **union of mechanistic subgraphs** with conditional edges (e.g., “high viscosity → more stators,” “hydrophilic surface → increased twitching”) rather than a single canonical “flagellum-only” pathway, because both the ecology (soil) and mechanism (gliding; archaeal pili) literature explicitly rejects a flagella-only mapping of motile. (ramoneda2024ecologicalrelevanceof pages 5-6, thunes2024glidingmotilityproteins pages 1-2, charlesorszag2024adhesionpilusretraction pages 1-2)

---

## 5) Relevant statistics and data (recent studies)

### 5.1 Genome- and metagenome-scale trait statistics (2024)
A genome-based motility inference model was trained on **1,225 strains** (388 motile; 837 nonmotile) and distilled to **21 predictive genes**; applied to **26,192 genomes across 12 bacterial phyla**, it reported phylum-level prevalence variability (e.g., Spirochaetota **93.2%**, Proteobacteria **78.3%**, Firmicutes **54.6%**, Actinobacteriota **15.9%**, Bacteroidota **0.7%**). Reported performance included being correct for all experimentally verified flagellated taxa and **94.5%** correct for nonflagellated taxa. (ramoneda2024ecologicalrelevanceof pages 5-6)

### 5.2 Flagellar motor quantitative values (2024)
- Flagellum assembly requires ~**50 genes** and the filament is polymerized from ~**20,000 flagellin subunits** (review/primer). (armitage2024microbialprimerthe pages 3-5)
- Ion-driven rotation speeds: proton-driven stator ~**300 r.p.s.**; sodium-driven motor ~**1300 r.p.s.** (review/primer). (armitage2024microbialprimerthe pages 3-5)
- Switching cooperativity: Hill coefficient up to **21** for CheY-P dependence (flagellar switching structural study). (johnson2024structuralbasisof pages 1-5)

### 5.3 Motility speed data in viscous environments (2024)
*C. jejuni* can reach **50–100 µm/s** in high-viscosity non-Newtonian fluids (versus ~35–45 µm/s in *Salmonella/E. coli*), consistent with adaptation for mucus colonization. (ribardo2024viscositydependentdeterminantsof pages 1-2)

### 5.4 Archaeal twitching tracking statistics (2024)
In *S. acidocaldarius*, ΔaapF “abolished twitching motility,” with quantitative track metrics reported (e.g., “46.2% of ΔaapF cells had a total displacement below 2 µm”; mean displacement and persistence reduced vs WT). (charlesorszag2024adhesionpilusretraction pages 1-2)

---

## 6) Candidate causal graph entities (nodes) grouped by type

### 6.1 Pathways / biological processes
- Flagellar motility / swimming motility: GO:0001539; chemotaxis: GO:0006935; flagellum assembly: GO:0009288. (nakamura2024structureanddynamics pages 1-3, johnson2024structuralbasisof pages 1-5)
- Twitching motility / T4P dynamics (label to GO terms as available; often curated as surface motility). (ohara2024surfacehydrophilicitypromotes pages 1-2)
- Gliding motility (GO:0006928). (thunes2024glidingmotilityproteins pages 1-2)
- Protein glycosylation impacting motility (N-glycosylation GO:1901657). (sofer2024perturbednglycosylationof pages 1-2)

### 6.2 Genes/proteins/complexes
- Flagellum: MotA/MotB stator; rotor/switch proteins FliG/FliM/FliN; MS ring FliF; hook/filament components (various). (nakamura2024structureanddynamics pages 1-3, johnson2024structuralbasisof pages 1-5)
- Chemotaxis: CheA, CheY, CheW, CheZ; domain modules P1–P5; receiver domains. (nakamura2024structureanddynamics pages 1-3, berry2024diversedomainarchitectures pages 3-6)
- T4P: PilA, PilB, PilT; PilJ chemoreceptor; Pil-Chp/cAMP axis (label-only). (ohara2024surfacehydrophilicitypromotes pages 1-2, yarrington2024thetypeiv pages 31-32)
- Gliding/T9SS: GldL/GldM motor; SprB adhesin; GldJ; PorV; T9SS machinery components (subset). (thunes2024glidingmotilityproteins pages 1-2)
- Archaeal: archaellum; Aap pili; AapF (assembly); archaellins and N-glycosylation pathway enzymes (Agl proteins). (charlesorszag2024adhesionpilusretraction pages 1-2, sofer2024perturbednglycosylationof pages 1-2)

### 6.3 Chemicals/ions and physical factors
- H+ (CHEBI:15378), Na+ (CHEBI:29101). (nakamura2024structureanddynamics pages 1-3)
- Proton motive force / ion motive force (label-only). (armitage2024microbialprimerthe pages 3-5, johnson2024structuralbasisof pages 1-5)
- Viscosity (label-only physical attribute). (ribardo2024viscositydependentdeterminantsof pages 1-2, johnson2024structuralbasisof pages 1-5)
- Surface hydrophilicity; bile salts/detergents (CHEBI grounding may be required per specific bile salt). (ohara2024surfacehydrophilicitypromotes pages 1-2)
- Soil carbon availability (environmental association). (ramoneda2024ecologicalrelevanceof pages 1-2)

---

## 7) Evidence-backed candidate causal edges (curation table)
The following table is designed for direct curation into `data/traits/morphology/motile.yaml` as candidate nodes and edges with citations, snippets, and uncertainty flags.

| Edge (subject–predicate–object) | Node type(s) | Evidence snippet (verbatim short quote) | Source (DOI, year, URL) | Notes/uncertainty | Suggested CURIEs (GO/CHEBI/ENVO/UniProt/etc when possible) |
|---|---|---|---|---|---|
| ion motive force across cytoplasmic membrane → powers → bacterial flagellar rotation/motility | process → process/trait | “a membrane-embedded rotary motor fueled by an ion motive force across the cytoplasmic membrane” (nakamura2024structureanddynamics pages 1-3) | 10.3390/biom14121488, 2024, https://doi.org/10.3390/biom14121488 | Broad, cross-bacterial statement; good core edge for flagellar swimming | GO:0006935; GO:0001539; label:ion motive force |
| MotA–MotB stator complex → acts as → transmembrane H+ channel | protein complex → molecular function | “it can act as a transmembrane H+ channel” (nakamura2024structureanddynamics pages 1-3) | 10.3390/biom14121488, 2024, https://doi.org/10.3390/biom14121488 | H+-driven systems; Na+-driven stators are separate variants | MotA; MotB; CHEBI:15378 (H+); GO:0015078 |
| H+ flux through MotA–MotB → generates torque via → electrostatic interaction with FliG | chemical/process → motor output | “conducts H+ through the channel to generate torque by electrostatic interactions between MotA and FliG” (nakamura2024structureanddynamics pages 1-3) | 10.3390/biom14121488, 2024, https://doi.org/10.3390/biom14121488 | Strong mechanistic edge for canonical flagellar motors | CHEBI:15378; FliG; GO:0001539 |
| MotB peptidoglycan binding → enables → stator channel opening/engagement | protein/process → process | “peptidoglycan binding opens the channel” (armitage2024microbialprimerthe pages 3-5) | 10.1099/mic.0.001406, 2024, https://doi.org/10.1099/mic.0.001406 | Derived from primer/review but mechanistically standard | MotB; GO:0009273; GO:0015078 |
| CheA autophosphorylation → phosphorylates → CheY | kinase → response regulator | “Phosphorylated CheA transfers its phosphate group to a response regulator called CheY” (nakamura2024structureanddynamics pages 1-3) | 10.3390/biom14121488, 2024, https://doi.org/10.3390/biom14121488 | Core chemotaxis signaling edge | CheA; CheY; GO:0000160; GO:0000155 |
| CheY-P → binds → C-ring/flagellar switch complex | response regulator → complex | “Phosphorylated CheY (CheY-P) binds to the C-ring” (nakamura2024structureanddynamics pages 1-3) | 10.3390/biom14121488, 2024, https://doi.org/10.3390/biom14121488 | Core signal-to-motor coupling edge | CheY; FliM; FliN; GO:0006935 |
| CheY-P binding → switches → CCW to CW rotation | signaling event → motor behavior | “allowing the motor to switch the direction of rotation from CCW to CW” (nakamura2024structureanddynamics pages 1-3) | 10.3390/biom14121488, 2024, https://doi.org/10.3390/biom14121488 | Canonical for many bacteria; direction conventions can vary by taxon | CheY; GO:0006935 |
| increased load/viscosity → recruits/increases → stator copy number | environmental factor → complex abundance/function | “increasing external viscosity recruits more stators up to stall torque” (armitage2024microbialprimerthe pages 5-6) | 10.1099/mic.0.001406, 2024, https://doi.org/10.1099/mic.0.001406 | Review-level synthesis; applies to flagellar motors, not all motility systems | ENVO:01001274 (viscosity, label only if no stable CURIE); MotA; MotB |
| low load → requires → one or two stators | physical condition → motor state | “Under low filament load only one or two stators are needed” (armitage2024microbialprimerthe pages 5-6) | 10.1099/mic.0.001406, 2024, https://doi.org/10.1099/mic.0.001406 | Quantitative but review-derived; useful for load-dependent motor edges | MotA; MotB; GO:0001539 |
| high load in Salmonella motor → increases to → up to 11 stators | physical condition → motor stoichiometry | “increased load leads to up to 11 stators driving a Salmonella flagellum” (johnson2024structuralbasisof pages 1-5) | 10.1038/s41564-024-01630-z, 2024, https://doi.org/10.1038/s41564-024-01630-z | Species-specific numeric value; curate as exemplar with caution | NCBITaxon:28901; MotA; MotB |
| Pseudomonas MotAB stator → dominates torque at → low-load/high-speed swimming | stator complex → phenotype | “MotAB dominates torque at low-load (high-speed) swimming” (wu2024torquespeedrelationshipof pages 13-15) | 10.1128/mbio.00745-24, 2024, https://doi.org/10.1128/mbio.00745-24 | P. aeruginosa-specific dual-stator physiology | NCBITaxon:287; MotAB; GO:0001539 |
| Pseudomonas MotCD stator → provides high torque at → extreme loads/swarming on agar | stator complex → phenotype | “MotCD provides high torque at extreme loads (e.g., swarming on agar)” (wu2024torquespeedrelationshipof pages 13-15) | 10.1128/mbio.00745-24, 2024, https://doi.org/10.1128/mbio.00745-24 | Taxon-specific; useful as conditional edge | NCBITaxon:287; MotCD; GO:0009405 |
| FliL → modulates → stator selection under changing viscosity | protein → regulatory process | “FliL is identified as a stator-interacting modulator that may influence stator selection under changing viscosity” (wu2024torquespeedrelationshipof pages 13-15) | 10.1128/mbio.00745-24, 2024, https://doi.org/10.1128/mbio.00745-24 | Mark uncertain: “may influence” | FliL; label:viscosity |
| VidA → required for → swimming in low-viscosity environments | protein → phenotype | “VidA is required for swimming in low-viscosity environments” (ribardo2024viscositydependentdeterminantsof pages 1-2) | 10.1128/mbio.02544-23, 2024, https://doi.org/10.1128/mbio.02544-23 | Campylobacter-specific auxiliary factor | NCBITaxon:197; label:VidA; GO:0001539 |
| VidB → reduces → swimming velocity in low viscosity | protein → phenotype | “VidB acts like a brake/clutch to reduce velocity in low viscosity” (ribardo2024viscositydependentdeterminantsof pages 1-2) | 10.1128/mbio.02544-23, 2024, https://doi.org/10.1128/mbio.02544-23 | Mechanistic model supported by suppressors; species-specific | NCBITaxon:197; label:VidB |
| CCW-biased flagellar rotation in H. pylori → promotes → biofilm initiation | motor state → biofilm process | “mutants with a counterclockwise bias promoted biofilm initiation” (liu2024counterclockwiserotationof pages 1-2) | 10.1128/mbio.00440-24, 2024, https://doi.org/10.1128/mbio.00440-24 | Strong but H. pylori-specific | NCBITaxon:210; GO:0042710 |
| CW-biased flagellar rotation in H. pylori → inhibits → biofilm initiation | motor state → biofilm process | “those with a clockwise bias inhibited it” (liu2024counterclockwiserotationof pages 1-2) | 10.1128/mbio.00440-24, 2024, https://doi.org/10.1128/mbio.00440-24 | Taxon-specific rotational-bias phenotype | NCBITaxon:210; GO:0042710 |
| CCW-locked flagellum → elevates → biofilm initiation | motor state/mutant state → process | “a CCW-locked flagellum elevates initiation” (liu2024counterclockwiserotationof pages 1-2) | 10.1128/mbio.00440-24, 2024, https://doi.org/10.1128/mbio.00440-24 | Useful causal edge, but not sufficient alone for biofilm | NCBITaxon:210; GO:0042710 |
| GldL/GldM motor → powers → gliding motility via proton gradient | protein complex → motility process | “GldL and GldM form a proton gradient-driven rotary motor” (thunes2024glidingmotilityproteins pages 1-2) | 10.1128/jb.00068-24, 2024, https://doi.org/10.1128/jb.00068-24 | Strong mechanistic edge for Bacteroidota gliding | GldL; GldM; CHEBI:15378; GO:0006928 |
| GldLM motor → powers → SprB surface movement | protein complex → adhesin movement | “that powers SprB movement” (thunes2024glidingmotilityproteins pages 1-2) | 10.1128/jb.00068-24, 2024, https://doi.org/10.1128/jb.00068-24 | Species/mechanism from Flavobacterium model; broad to gliding Bacteroidota cautiously | SprB; GldL; GldM |
| SprB adhesin surface movement → drives → gliding motility | adhesin/process → phenotype | “gliding... is driven by the surface movement of adhesins (notably SprB) along the outer membrane” (thunes2024glidingmotilityproteins pages 1-2) | 10.1128/jb.00068-24, 2024, https://doi.org/10.1128/jb.00068-24 | Good non-flagellar motility edge | SprB; GO:0006928 |
| gldJ truncation preserving secretion but not gliding → reduces → virulence | genotype/protein → phenotype | “a gldJ truncation that preserves secretion but not gliding reduces virulence” (thunes2024glidingmotilityproteins pages 1-2) | 10.1128/jb.00068-24, 2024, https://doi.org/10.1128/jb.00068-24 | Supports motility–virulence link while separating secretion from motility | GldJ; GO:0009405 |
| PilB ATPase → promotes → T4P extension/assembly | ATPase → process | “PilB (extension ATPase)” (ohara2024surfacehydrophilicitypromotes pages 1-2) | 10.1128/msphere.00390-24, 2024, https://doi.org/10.1128/msphere.00390-24 | Review/assay framing but standard mechanistic claim | PilB; GO:0043716 |
| PilT ATPase → promotes → T4P retraction/disassembly | ATPase → process | “PilT (retraction ATPase)” (ohara2024surfacehydrophilicitypromotes pages 1-2) | 10.1128/msphere.00390-24, 2024, https://doi.org/10.1128/msphere.00390-24 | Core twitching mechanism | PilT; GO:0043717 |
| cycles of T4P extension and retraction → enable → twitching motility | process → phenotype | “recurrent cycles of T4P assembly (extension) and disassembly (retraction) power surface movement” (ohara2024surfacehydrophilicitypromotes pages 1-2) | 10.1128/msphere.00390-24, 2024, https://doi.org/10.1128/msphere.00390-24 | Good generic edge for pili-based motility | GO:0043716; GO:0043717; GO:0006928 |
| increased surface hydrophilicity → promotes → twitching motility | surface property → phenotype | “Hydrophilic surfaces... increase twitching” (ohara2024surfacehydrophilicitypromotes pages 1-2) | 10.1128/msphere.00390-24, 2024, https://doi.org/10.1128/msphere.00390-24 | Assay/environment-specific but clear | ENVO:00000022 (surface, broad); label:surface hydrophilicity |
| bile salts/detergents → enhance → twitching by increasing surface hydrophilicity | chemical/environmental factor → phenotype | “Bile salts and other detergents enhance twitching... by altering the physicochemical properties—specifically increasing surface hydrophilicity” (ohara2024surfacehydrophilicitypromotes pages 1-2) | 10.1128/msphere.00390-24, 2024, https://doi.org/10.1128/msphere.00390-24 | Assay-specific; not direct cellular signaling | CHEBI:3098 (bile acid/bile salts close match, candidate); label:detergent |
| Aap pili retraction → powers → archaeal twitching motility | pilus process → phenotype | “Aap pili are thus capable of retraction in the absence of a PilT homolog” (charlesorszag2024adhesionpilusretraction pages 1-2) | 10.1038/s41467-024-49101-7, 2024, https://doi.org/10.1038/s41467-024-49101-7 | Strong archaeal surface-motility edge; exact retraction motor unresolved | NCBITaxon:2285; label:Aap pilus; GO:0006928 |
| ΔaapF → abolishes → twitching motility | gene deletion → phenotype | “deleting the adhesion pilus assembly protein AapF (ΔaapF) ‘abolished twitching motility’” (charlesorszag2024adhesionpilusretraction pages 1-2) | 10.1038/s41467-024-49101-7, 2024, https://doi.org/10.1038/s41467-024-49101-7 | Species-specific gene-level edge in Sulfolobus acidocaldarius | label:AapF; NCBITaxon:2285 |
| archaellum rotation → generates → swimming motility in archaea | organelle/process → phenotype | “rotates to generate propulsion for swimming motility” (charlesorszag2024adhesionpilusretraction pages 1-2) | 10.1038/s41467-024-49101-7, 2024, https://doi.org/10.1038/s41467-024-49101-7 | Broad archaeal swimming edge | GO:0001539; label:archaellum |
| truncation of archaellar N-linked glycans → causes → compromised/directional motility defects | glycosylation state → phenotype | “glycan-truncated mutants swim in ever-changing directions within a limited area” (sofer2024perturbednglycosylationof pages 1-2) | 10.1038/s41467-024-50277-1, 2024, https://doi.org/10.1038/s41467-024-50277-1 | Strong archaeal post-translational mechanism | GO:1901657; label:archaellin N-glycosylation |
| N-linked tetrasaccharides on archaellins → prevent → filament aggregation that limits motility | glycan modification → physical state/phenotype | “N-linked tetrasaccharides act as physical spacers to reduce filament aggregation that limits cell motility” (sofer2024perturbednglycosylationof pages 1-2) | 10.1038/s41467-024-50277-1, 2024, https://doi.org/10.1038/s41467-024-50277-1 | Excellent mechanistic edge; archaeal-specific | CHEBI:506227 (generic glycan grounding unclear, candidate label preferred); archaellin |
| higher soil carbon availability → positively associates with → prevalence of flagellar motility | environmental factor → trait prevalence | “positive relationship between the prevalence of bacterial flagellar motility and soil carbon availability” (ramoneda2024ecologicalrelevanceof pages 1-2) | 10.1093/ismejo/wrae067, 2024, https://doi.org/10.1093/ismejo/wrae067 | Ecological association, not direct cellular causation; use as environment-trait link | ENVO:00001998 (soil); label:soil carbon availability |
| conserved flagellum assembly genes → infer → capacity for flagellar motility | gene set → trait inference | “presence/absence of conserved flagellum assembly genes can be used to predict a taxon's capacity for flagellar motility” (ramoneda2024ecologicalrelevanceof pages 5-6) | 10.1093/ismejo/wrae067, 2024, https://doi.org/10.1093/ismejo/wrae067 | Inference/assay edge rather than biological mechanism; useful for curation metadata | GO:0009288; label:flagellum assembly gene set |
| absence of flagella → does not imply → non-motile phenotype | structural trait → trait interpretation | “being nonflagellated does not mean taxa are nonmotile” (ramoneda2024ecologicalrelevanceof pages 5-6) | 10.1093/ismejo/wrae067, 2024, https://doi.org/10.1093/ismejo/wrae067 | Important boundary-case warning for trait scope; supports inclusion of pili/gliding/archaella | METPO:1000702; GO:0006928; GO:0001539 |


*Table: This table lists candidate causal edges for curating the microbial trait ‘motile’, spanning flagellar, pili-based, gliding, and archaeal mechanisms plus key environmental associations. It is useful as a starting evidence matrix for selecting robust TraitMech nodes and edges while flagging taxon- or assay-specific claims.*

---

## 8) Warnings / curation caveats (do not yet curate without constraints)
1) **Avoid “motile = flagellated”**: explicit evidence indicates nonflagellated taxa can be motile (e.g., gliding). Curate separate subgraphs or conditional edges. (ramoneda2024ecologicalrelevanceof pages 5-6, thunes2024glidingmotilityproteins pages 1-2)
2) **Assay dependence**: twitching is strongly affected by surface physicochemistry (hydrophilicity; detergents); edges like “bile salts → twitching” should be curated as **assay/surface-condition** edges, not universal physiology. (ohara2024surfacehydrophilicitypromotes pages 1-2)
3) **Taxon-specific innovations**: dual stators (MotAB/MotCD), VidA/VidB, and CCW-bias effects on biofilm are compelling but should be marked **taxon-specific** (Pseudomonas; Campylobacter; Helicobacter). (liu2024counterclockwiserotationof pages 1-2, wu2024torquespeedrelationshipof pages 13-15, ribardo2024viscositydependentdeterminantsof pages 1-2)
4) **Ecological associations vs mechanistic causation**: soil carbon availability correlates with community-level prevalence of flagellar motility; treat this as an **environment–trait association** rather than direct mechanistic causation at the single-cell level. (ramoneda2024ecologicalrelevanceof pages 1-2)

---

## 9) DOI-first bibliography (with dates and URLs where available)

1. Nakamura S, Minamino T. *Structure and Dynamics of the Bacterial Flagellar Motor Complex.* **Biomolecules**. Nov 2024. DOI: **10.3390/biom14121488**. URL: https://doi.org/10.3390/biom14121488 (nakamura2024structureanddynamics pages 1-3)
2. Johnson S, et al. *Structural basis of directional switching by the bacterial flagellum.* **Nature Microbiology**. Mar 2024. DOI: **10.1038/s41564-024-01630-z**. URL: https://doi.org/10.1038/s41564-024-01630-z (johnson2024structuralbasisof pages 1-5)
3. Armitage JP. *Microbial Primer: The bacterial flagellum – how bacteria swim.* **Microbiology**. Jan 2024. DOI: **10.1099/mic.0.001406**. URL: https://doi.org/10.1099/mic.0.001406 (armitage2024microbialprimerthe pages 3-5)
4. Wu H, et al. *Torque-speed relationship of the flagellar motor with dual-stator systems in Pseudomonas aeruginosa.* **mBio**. Dec 2024. DOI: **10.1128/mbio.00745-24**. URL: https://doi.org/10.1128/mbio.00745-24 (wu2024torquespeedrelationshipof pages 13-15)
5. Ribardo DA, Johnson JJ, Hendrixson DR. *Viscosity-dependent determinants of Campylobacter jejuni impacting the velocity of flagellar motility.* **mBio**. Jan 2024. DOI: **10.1128/mbio.02544-23**. URL: https://doi.org/10.1128/mbio.02544-23 (ribardo2024viscositydependentdeterminantsof pages 1-2)
6. Ramoneda J, et al. *Ecological relevance of flagellar motility in soil bacterial communities.* **The ISME Journal**. Jan 2024. DOI: **10.1093/ismejo/wrae067**. URL: https://doi.org/10.1093/ismejo/wrae067 (ramoneda2024ecologicalrelevanceof pages 5-6, ramoneda2024ecologicalrelevanceof pages 1-2)
7. O’Hara MT, et al. *Surface hydrophilicity promotes bacterial twitching motility.* **mSphere**. Sep 2024. DOI: **10.1128/msphere.00390-24**. URL: https://doi.org/10.1128/msphere.00390-24 (ohara2024surfacehydrophilicitypromotes pages 1-2)
8. Thunes NC, et al. *Gliding motility proteins GldJ and SprB contribute to Flavobacterium columnare virulence.* **Journal of Bacteriology**. Apr 2024. DOI: **10.1128/jb.00068-24**. URL: https://doi.org/10.1128/jb.00068-24 (thunes2024glidingmotilityproteins pages 1-2)
9. Charles‑Orszag A, et al. *Adhesion pilus retraction powers twitching motility in the thermoacidophilic crenarchaeon Sulfolobus acidocaldarius.* **Nature Communications**. Jun 2024. DOI: **10.1038/s41467-024-49101-7**. URL: https://doi.org/10.1038/s41467-024-49101-7 (charlesorszag2024adhesionpilusretraction pages 1-2)
10. Sofer S, et al. *Perturbed N-glycosylation of Halobacterium salinarum archaellum filaments leads to filament bundling and compromised cell motility.* **Nature Communications**. Jul 2024. DOI: **10.1038/s41467-024-50277-1**. URL: https://doi.org/10.1038/s41467-024-50277-1 (sofer2024perturbednglycosylationof pages 1-2)
11. Berry MA, Andrianova EP, Zhulin IB. *Diverse domain architectures of CheA histidine kinase, a central component of bacterial and archaeal chemosensory systems.* **Microbiology Spectrum**. Jan 2024. DOI: **10.1128/spectrum.03464-23**. URL: https://doi.org/10.1128/spectrum.03464-23 (berry2024diversedomainarchitectures pages 3-6, berry2024diversedomainarchitectures pages 8-10, berry2024diversedomainarchitectures pages 6-8)
12. Liu X, et al. *Counterclockwise rotation of the flagellum promotes biofilm initiation in Helicobacter pylori.* **mBio**. Jun 2024. DOI: **10.1128/mbio.00440-24**. URL: https://doi.org/10.1128/mbio.00440-24 (liu2024counterclockwiserotationof pages 1-2)
13. Jin C, Sengupta A. *Microbes in porous environments: from active interactions to emergent feedback.* **Biophysical Reviews**. Apr 2024. DOI: **10.1007/s12551-024-01185-7**. URL: https://doi.org/10.1007/s12551-024-01185-7 (jin2024microbesinporous pages 14-18)



References

1. (ramoneda2024ecologicalrelevanceof pages 5-6): Josep Ramoneda, Kunkun Fan, Jane M Lucas, Haiyan Chu, Andrew Bissett, Michael S Strickland, and Noah Fierer. Ecological relevance of flagellar motility in soil bacterial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae067, doi:10.1093/ismejo/wrae067. This article has 37 citations.

2. (thunes2024glidingmotilityproteins pages 1-2): Nicole C. Thunes, Jason P. Evenhuis, Ryan S. Lipscomb, David Pérez-Pascual, Rebecca J. Stevick, Clayton Birkett, Jean-Marc Ghigo, and Mark J. McBride. Gliding motility proteins gldj and sprb contribute to <i>flavobacterium columnare</i> virulence. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00068-24, doi:10.1128/jb.00068-24. This article has 5 citations and is from a peer-reviewed journal.

3. (ohara2024surfacehydrophilicitypromotes pages 1-2): Megan T. O'Hara, Tori M. Shimozono, Keane J. Dye, David Harris, and Zhaomin Yang. Surface hydrophilicity promotes bacterial twitching motility. Sep 2024. URL: https://doi.org/10.1128/msphere.00390-24, doi:10.1128/msphere.00390-24. This article has 10 citations and is from a peer-reviewed journal.

4. (charlesorszag2024adhesionpilusretraction pages 1-2): Arthur Charles-Orszag, Marleen van Wolferen, Samuel J. Lord, Sonja-Verena Albers, and R. Dyche Mullins. Adhesion pilus retraction powers twitching motility in the thermoacidophilic crenarchaeon sulfolobus acidocaldarius. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49101-7, doi:10.1038/s41467-024-49101-7. This article has 13 citations and is from a highest quality peer-reviewed journal.

5. (nakamura2024structureanddynamics pages 1-3): Shuichi Nakamura and Tohru Minamino. Structure and dynamics of the bacterial flagellar motor complex. Biomolecules, 14:1488, Nov 2024. URL: https://doi.org/10.3390/biom14121488, doi:10.3390/biom14121488. This article has 26 citations.

6. (johnson2024structuralbasisof pages 1-5): Steven Johnson, Justin C. Deme, Emily J. Furlong, Joseph J. E. Caesar, Fabienne F. V. Chevance, Kelly T. Hughes, and Susan M. Lea. Structural basis of directional switching by the bacterial flagellum. Nature microbiology, 9:1282-1292, Mar 2024. URL: https://doi.org/10.1038/s41564-024-01630-z, doi:10.1038/s41564-024-01630-z. This article has 59 citations and is from a highest quality peer-reviewed journal.

7. (jin2024microbesinporous pages 14-18): Chenyu Jin and Anupam Sengupta. Microbes in porous environments: from active interactions to emergent feedback. Biophysical Reviews, 16:173-188, Apr 2024. URL: https://doi.org/10.1007/s12551-024-01185-7, doi:10.1007/s12551-024-01185-7. This article has 42 citations and is from a peer-reviewed journal.

8. (ramoneda2024ecologicalrelevanceof pages 1-2): Josep Ramoneda, Kunkun Fan, Jane M Lucas, Haiyan Chu, Andrew Bissett, Michael S Strickland, and Noah Fierer. Ecological relevance of flagellar motility in soil bacterial communities. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae067, doi:10.1093/ismejo/wrae067. This article has 37 citations.

9. (ribardo2024viscositydependentdeterminantsof pages 1-2): Deborah A. Ribardo, Jeremiah J. Johnson, and David R. Hendrixson. Viscosity-dependent determinants of <i>campylobacter jejuni</i> impacting the velocity of flagellar motility. Jan 2024. URL: https://doi.org/10.1128/mbio.02544-23, doi:10.1128/mbio.02544-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

10. (wu2024torquespeedrelationshipof pages 13-15): Haolin Wu, Zhengyu Wu, Maojin Tian, Rongjing Zhang, and Junhua Yuan. Torque-speed relationship of the flagellar motor with dual-stator systems in <i>pseudomonas aeruginosa</i>. Dec 2024. URL: https://doi.org/10.1128/mbio.00745-24, doi:10.1128/mbio.00745-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

11. (berry2024diversedomainarchitectures pages 3-6): Marissa A. Berry, Ekaterina P. Andrianova, and Igor B. Zhulin. Diverse domain architectures of chea histidine kinase, a central component of bacterial and archaeal chemosensory systems. Jan 2024. URL: https://doi.org/10.1128/spectrum.03464-23, doi:10.1128/spectrum.03464-23. This article has 9 citations and is from a domain leading peer-reviewed journal.

12. (berry2024diversedomainarchitectures pages 8-10): Marissa A. Berry, Ekaterina P. Andrianova, and Igor B. Zhulin. Diverse domain architectures of chea histidine kinase, a central component of bacterial and archaeal chemosensory systems. Jan 2024. URL: https://doi.org/10.1128/spectrum.03464-23, doi:10.1128/spectrum.03464-23. This article has 9 citations and is from a domain leading peer-reviewed journal.

13. (berry2024diversedomainarchitectures pages 6-8): Marissa A. Berry, Ekaterina P. Andrianova, and Igor B. Zhulin. Diverse domain architectures of chea histidine kinase, a central component of bacterial and archaeal chemosensory systems. Jan 2024. URL: https://doi.org/10.1128/spectrum.03464-23, doi:10.1128/spectrum.03464-23. This article has 9 citations and is from a domain leading peer-reviewed journal.

14. (sofer2024perturbednglycosylationof pages 1-2): Shahar Sofer, Zlata Vershinin, Leen Mashni, Ran Zalk, Anat Shahar, Jerry Eichler, and Iris Grossman-Haham. Perturbed n-glycosylation of halobacterium salinarum archaellum filaments leads to filament bundling and compromised cell motility. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50277-1, doi:10.1038/s41467-024-50277-1. This article has 15 citations and is from a highest quality peer-reviewed journal.

15. (armitage2024microbialprimerthe pages 3-5): Judith P. Armitage. Microbial primer: the bacterial flagellum – how bacteria swim. Jan 2024. URL: https://doi.org/10.1099/mic.0.001406, doi:10.1099/mic.0.001406. This article has 15 citations and is from a peer-reviewed journal.

16. (yarrington2024thetypeiv pages 31-32): Kaitlin D. Yarrington, Tyler N. Shendruk, and Dominique H. Limoli. The type iv pilus chemoreceptor pilj controls chemotaxis of one bacterial species towards another. PLOS Biology, 22:e3002488, Feb 2024. URL: https://doi.org/10.1371/journal.pbio.3002488, doi:10.1371/journal.pbio.3002488. This article has 24 citations and is from a highest quality peer-reviewed journal.

17. (armitage2024microbialprimerthe pages 5-6): Judith P. Armitage. Microbial primer: the bacterial flagellum – how bacteria swim. Jan 2024. URL: https://doi.org/10.1099/mic.0.001406, doi:10.1099/mic.0.001406. This article has 15 citations and is from a peer-reviewed journal.

18. (liu2024counterclockwiserotationof pages 1-2): Xiaolin Liu, Paphavee Lertsethtakarn, Vanessa T. Mariscal, Fitnat Yildiz, and Karen M. Ottemann. Counterclockwise rotation of the flagellum promotes biofilm initiation in <i>helicobacter pylori</i>. Jun 2024. URL: https://doi.org/10.1128/mbio.00440-24, doi:10.1128/mbio.00440-24. This article has 22 citations and is from a domain leading peer-reviewed journal.