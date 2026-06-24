---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:02:29.945026'
end_time: '2026-06-18T01:28:39.643899'
duration_seconds: 1569.7
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pressure delta
  trait_identifier: traitmech:000006
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: pressure_delta
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pressure phenotype with numerical limits expressing the breadth (maximum
    minus minimum) of hydrostatic pressure supporting growth of an organism.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP
    are usually known as piezophiles, referring to their preference for high pressure
    (Pressure-adaptation review supports the breadth of the pressure-tolerance span
    as a derived descriptor of pressure-adaptation flexibility.) | DOI:10.1099/ijsem.0.001671:
    growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (The 80-140 MPa span
    of Colwellia marinimaniae MTCD1 (delta = 60 MPa) illustrates the breadth this
    phenotype records.)'
  causal_graph_summary: 'pressure_delta_breadth_descriptor: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pressure delta
- **METPO identifier:** traitmech:000006
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits expressing the breadth (maximum minus minimum) of hydrostatic pressure supporting growth of an organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports the breadth of the pressure-tolerance span as a derived descriptor of pressure-adaptation flexibility.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (The 80-140 MPa span of Colwellia marinimaniae MTCD1 (delta = 60 MPa) illustrates the breadth this phenotype records.)
- **Existing causal graph summary:** pressure_delta_breadth_descriptor: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pressure delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_delta.yaml`.

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
- **Trait label:** pressure delta
- **METPO identifier:** traitmech:000006
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits expressing the breadth (maximum minus minimum) of hydrostatic pressure supporting growth of an organism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports the breadth of the pressure-tolerance span as a derived descriptor of pressure-adaptation flexibility.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (The 80-140 MPa span of Colwellia marinimaniae MTCD1 (delta = 60 MPa) illustrates the breadth this phenotype records.)
- **Existing causal graph summary:** pressure_delta_breadth_descriptor: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pressure delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_delta.yaml`.

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


## Research report: Microbial trait **pressure delta** (TraitMech: pressure growth-range breadth)

### 1) Scope summary (TraitMech curation focus)

**Trait label:** pressure delta  
**METPO identifier:** traitmech:000006  
**Definition (curation-ready):** the **breadth of hydrostatic pressure supporting growth** under a defined assay, computed as **Pmax(growth) − Pmin(growth)** (units typically MPa). This is a *derived* phenotype from experimentally observed **minimum growth pressure** and **maximum growth pressure**, and should be curated together with the assay context (temperature, medium, incubation time, inoculum state, oxygen availability, pressure steps). Direct examples show how min/max/optimum are reported for piezophiles and how delta is derived (e.g., *Colwellia marinimaniae* MTCD1 grows **80–140 MPa**, delta = 60 MPa) (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media 84a4f0b4).

**What it is not:**
- Not the **optimum growth pressure** (Popt), which is a different scalar phenotype (e.g., MTCD1 Popt ≈120 MPa) (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media 84a4f0b4).  
- Not **survival** at pressure without growth (short exposures can greatly exceed growth limits; survival should not be conflated with growth-range endpoints) (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 2-3).  
- Not a categorical ecological label (“piezophile/piezotolerant/piezosensitive”), though those classes often imply different expected deltas and should be tracked as related context nodes (peters2023effectsofcrowding pages 7-9, stief2023hydrostaticpressureinduces pages 8-9).

**Boundary cases / curation warnings:**
- **Assay dependence:** pressure-range bounds can change with growth phase (stationary vs exponential), exposure duration, and temperature; therefore, pressure delta should be curated with those experimental covariates (malas2024biologicalfunctionsat pages 2-3, malas2024biologicalfunctionsat pages 1-2).  
- **Community vs isolate:** ecological microcosm studies can show pressure thresholds for respiration/community function, but these should be treated as *environmental process edges* rather than isolate pressure-delta phenotypes (stief2023hydrostaticpressureinduces pages 1-2).

### 2) Key concepts and definitions (current understanding)

#### 2.1 Terminology for pressure-adaptation classes
- **Piezophiles:** organisms that “grow optimally at pressures higher than atmospheric (0.1 MPa)” and have specialized adaptations for high pressure (malas2024biologicalfunctionsat pages 1-2).  
- **Piezosensitive / piezotolerant / piezophilic / obligate piezophilic:** a biophysical review describes these as classes ranging from organisms living around ambient pressure (piezosensitive/piezotolerant) to those that require high pressure to grow (piezophilic/obligate piezophilic) (peters2023effectsofcrowding pages 7-9).  
- **Piezotolerant vs piezophilic vs piezosensitive in vertical gradients:** in marine-snow context, piezotolerant taxa “only survive… but do not thrive better at high than at low hydrostatic pressure,” whereas piezophiles may be selected for and piezosensitive selected against (stief2023hydrostaticpressureinduces pages 8-9).

#### 2.2 Mechanistic framing: why pressure bounds exist
Multiple sources converge on the idea that pressure constrains growth by impacting **membranes**, **proteins**, **nucleic acids**, and **translation/replication**:
- High pressure reduces system volume (Le Châtelier-type reasoning) and can cause **loss of membrane fluidity**, **protein denaturation/altered function**, **loss of motility**, and **suppressed transcription/translation** (malas2024biologicalfunctionsat pages 2-3).  
- In marine-snow experiments, high pressure is described as causing reduced membrane fluidity, protein dissociation/unfolding, DNA hydrogen-bond stabilization, and **ribosome dissociation**, leading to dysfunctional energy conservation, DNA replication, and RNA translation (stief2023hydrostaticpressureinduces pages 1-2).  
- A Chemical Reviews synthesis emphasizes membrane phase behavior (high pressure promotes more ordered/gel-like states) and highlights roles for osmolytes/cosolutes and the sensitivity of ribosomal RNA as stress markers (peters2023effectsofcrowding pages 9-11).

**Interpretation for pressure delta:** pressure delta can be seen as an *integrated systems phenotype* reflecting how many of these subsystems remain functional across a pressure interval. Mechanisms that stabilize membranes/proteins/translation/energy are candidates to widen Pmax−Pmin.

### 3) Recent developments and latest research (prioritize 2023–2024)

#### 3.1 2024: Titan-relevant high-pressure transcriptomics in *Shewanella oneidensis* MR-1
Malas et al. (Frontiers in Microbiology; published **13 Feb 2024**) used a high-pressure culturing system and exposed *S. oneidensis* MR-1 to **158 MPa** for **15 min** and **2 h**; they report MR-1 remained metabolically active at HHP and could show viable growth following 2 h exposure, with minimal pressure training (malas2024biologicalfunctionsat pages 1-2). Key mechanistic signals include:  
- **Arginine biosynthesis upregulation** (argA/B/C/F; plus argR) with arginine proposed as a protein stabilizer under pressure (malas2024biologicalfunctionsat pages 9-10).  
- **Membrane/lipid remodeling signals** (multiple fatty-acid biosynthesis genes detected; changes in acpP and fab genes suggesting shifts toward branched-chain fatty acid synthesis) (malas2024biologicalfunctionsat pages 9-10, malas2024biologicalfunctionsat pages 6-9).  
- **DNA repair/replication stress response** (recN, topB, dinB, dinG induced) (malas2024biologicalfunctionsat pages 6-9).  
- **Translation stress** (ribosome recycling factor frr downregulated) (malas2024biologicalfunctionsat pages 6-9).  
This paper expands the mechanistic toolkit relevant to pressure-delta graphs by providing gene-level candidates responsive at pressures beyond most natural deep-sea habitats (malas2024biologicalfunctionsat pages 1-2).

#### 3.2 2023: High-pressure impacts on sinking particles and microbial respiration thresholds
Stief et al. (Communications Earth & Environment; **Oct 2023**) simulated sinking diatom aggregates with pressure increased over time and observed that microbial respiration decreased gradually and **ceased by 60 MPa**; DOC leakage increased at ≥40 MPa and community composition shifted at 60–100 MPa (stief2023hydrostaticpressureinduces pages 1-2). While not an isolate growth-range assay, these data provide useful *process-level* thresholds and mechanistic constraints (membrane fluidity loss, ribosome dissociation) relevant to upper pressure bounds (stief2023hydrostaticpressureinduces pages 1-2).

#### 3.3 2023: Biophysical synthesis of HHP, membranes, osmolytes, and pressure classes
Peters et al. (Chemical Reviews; **Nov 2023**) provides an authoritative synthesis linking high-pressure effects to membrane phase behavior, protein thermodynamics, and osmolyte/crowding effects, and defines pressure-response classes (piezosensitive/piezotolerant vs piezophilic/obligate piezophilic) (peters2023effectsofcrowding pages 7-9, peters2023effectsofcrowding pages 9-11). This serves as a mechanistic “expert opinion” anchor for why membrane composition and cosolutes are consistent candidate nodes in pressure-delta graphs.

### 4) Current applications and real-world implementations

1. **Deep biosphere and hadal ecology:** Pressure gradients (60–110 MPa hadal) can select for pressure-tolerant taxa and alter particle remineralization; simulated sinking experiments show pressure can suppress respiration at ≥60 MPa and shift community composition at 60–100 MPa (stief2023hydrostaticpressureinduces pages 1-2).

2. **Astrobiology / ocean-world habitability:** Titan subsurface ocean pressures are modeled ≥150 MPa, above the highest pressures known to support life in natural ecosystems; understanding pressure-adaptation mechanisms informs habitability assessments and experimental designs (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 2-3).  

3. **Low- and high-pressure growth technology:** A notable real-world implementation is high-pressure cultivation systems enabling growth assays across large pressure intervals. For example, *Carnobacterium* strains were grown anaerobically at 2°C across **10^3–10^7 Pa**, demonstrating a very broad growth pressure range (miller2023carnobacteriumspeciescapableof pages 1-3).  

### 5) Relevant statistics and quantitative data points (from recent studies)

- **Upper bound of demonstrated microbial growth at HHP:** “currently demonstrated growth limit” at **140 MPa** (cited as Kusube et al. 2017 in Malas et al.; used as current limit framing) (malas2024biologicalfunctionsat pages 1-2).  
- **Explicit isolate growth ranges enabling direct pressure-delta computation:**  
  - *Colwellia marinimaniae* MTCD1: growth **80–140 MPa**; Popt ≈120 MPa → **pressure delta = 60 MPa** (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media 84a4f0b4).  
  - *Colwellia* sp. MT41: no growth below **35 MPa**; Popt ≈103 MPa (Pmax not stated in retrieved snippet; delta cannot be computed from available context) (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media 84a4f0b4).  
- **Community-process thresholds in particle incubations:** oxygen consumption ceases at **60–100 MPa** in sinking aggregate simulations; DOC leakage substantial at ≥40 MPa (stief2023hydrostaticpressureinduces pages 1-2).  
- **Shewanella MR-1 transcriptomic response at extreme pressure:** **264** differentially expressed genes after **15 min** at **158 MPa**; broad functional categories affected (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 9-10).  
- **Carnobacterium growth breadth:** **11/14** strains showed measurable growth at all pressures tested across **10^3–10^7 Pa** at 2°C under anaerobic conditions (5 orders of magnitude) (miller2023carnobacteriumspeciescapableof pages 1-3).

### 6) Candidate nodes grouped by type (ontology grounding suggestions)

> A) Phenotype/trait nodes: pressure delta — METPO:traitmech:000006 (target trait; growth-supporting hydrostatic pressure breadth = max minus min growth pressure); minimum growth pressure — label-only candidate (assay-derived lower bound of pressure supporting growth); maximum growth pressure — label-only candidate (assay-derived upper bound of pressure supporting growth); optimum growth pressure — label-only candidate (pressure of maximal growth rate). Explicit examples in *Colwellia* include MT41 “does not grow below 35 MPa” with optimum 103 MPa, and MTCD1 “growth range from 80 to 140 MPa” with optimum 120 MPa, illustrating how min/max/optimum compose pressure-delta breadth (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media 84a4f0b4, makhatadze2024modulationofelectrostatic pages 1-3)
>
> B) Environmental/assay nodes: hydrostatic pressure — ENVO:01001305 candidate for hydrostatic pressure environment, label “hydrostatic pressure (MPa)” for assay variable; pressure exposure duration — label-only (e.g., 15 min, 2 h at 158 MPa in *S. oneidensis* MR-1); temperature — label-only assay variable (e.g., 2°C in *Carnobacterium* growth-range experiments); growth phase — label-only (early stationary phase vs exponential phase affects HHP resistance); oxygen availability — label-only or ENVO candidate for anoxic conditions (e.g., anaerobic/anoxic cultivation in *Carnobacterium*); medium — label-only (complex liquid medium / defined cultivation medium). These are important because pressure-growth bounds are assay-dependent and change with exposure duration, temperature, oxygenation, and physiological state (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 2-3, miller2023carnobacteriumspeciescapableof pages 8-9, miller2023carnobacteriumspeciescapableof pages 1-3)
>
> C) Molecular/cellular process nodes: membrane fluidity — GO candidate: membrane organization / membrane fluidity regulation; homeoviscous adaptation — label-only candidate for pressure/temperature-dependent membrane lipid remodeling; translation — GO:0006412 candidate; ribosome integrity / ribosome dissociation — label-only candidate or GO ribosome-related process; DNA repair — GO:0006281; motility — GO:0048870 candidate / bacterial-type flagellum-dependent motility candidate; oxidative stress response — GO:0006979. Evidence links high pressure to loss of membrane fluidity, suppressed transcription/translation, ribosome dissociation, dysfunctional DNA replication/repair demands, motility loss, and antioxidant defense responses; homeoviscous adaptation is repeatedly proposed as a central mechanism that helps preserve membrane function under HHP (stief2023hydrostaticpressureinduces pages 1-2, malas2024biologicalfunctionsat pages 2-3, peters2023effectsofcrowding pages 7-9, miller2023carnobacteriumspeciescapableof pages 8-9)
>
> D) Gene/protein/pathway nodes from evidence: pfaABCD polyunsaturated fatty acid biosynthesis — KEGG candidate, label-only if unresolved; delta-9 acyl-phospholipid desaturase — label-only enzyme candidate; fatty acid cis/trans isomerase — label-only enzyme candidate; nuo complex I / NADH dehydrogenase I — KEGG/GO respiratory electron transport candidate; rnf complex — label-only respiratory/ion-translocating complex candidate; nqr / Na+-translocating NADH:quinone oxidoreductase — label-only or KEGG candidate; torSTRECAD TMAO reduction pathway — KEGG candidate with CHEBI candidate for trimethylamine N-oxide; argA, argB, argC, argF (arginine biosynthesis) — KEGG arginine biosynthesis candidates; argR — label-only arginine regulon regulator; cspG — label-only cold-shock protein candidate; frr — label-only ribosome recycling factor; recN — label-only DNA repair protein; topB — label-only DNA topoisomerase III candidate; dinB — label-only DNA damage-inducible polymerase IV candidate; dinG — label-only DNA damage-inducible helicase candidate; nhaA — label-only Na+/H+ antiporter candidate. These nodes are all reported in retrieved evidence: *Colwellia* comparative genomics supports pfaABCD, desaturase, cis/trans isomerase, nuo, rnf, nqr, torSTRECAD; *S. oneidensis* 158 MPa transcriptomics supports argA/B/C/F, argR, cspG, frr, recN, topB, dinB, dinG, nhaA (peoples2020distinctivegeneand pages 5-7, malas2024biologicalfunctionsat pages 6-9, malas2024biologicalfunctionsat pages 9-10, peoples2020distinctivegeneand pages 9-11)
>
> Suggested curation caution: phenotype nodes and assay nodes are strong candidates for immediate inclusion; process nodes are broadly supported across taxa; many gene-level nodes are taxon-specific and should be marked as uncertain unless curated as candidate mechanistic contributors to pressure-delta breadth rather than universal determinants (peoples2020distinctivegeneand pages 5-7, malas2024biologicalfunctionsat pages 1-2, peters2023effectsofcrowding pages 7-9)


*Blockquote: This artifact lists candidate nodes for a TraitMech causal graph of microbial pressure delta, grouped by phenotype, assay environment, cellular process, and gene/pathway level. It is useful as a curation scaffold because it ties each node type to retrieved evidence and suggests ontology grounding where possible.*

### 7) Evidence-backed candidate causal edges (triples)

| Edge (subject —predicate→ object) | Node types | Ontology grounding suggestions | Evidence snippet | Source (DOI URL; pub. date) | Curation notes |
|---|---|---|---|---|---|
| Unsaturated fatty acid production / phospholipid desaturation —enables→ membrane fluidity maintenance under high hydrostatic pressure | pathway/process → process | label: unsaturated fatty acid production; GO: membrane lipid metabolic process (candidate); KEGG/MetaCyc: pfaABCD PUFA biosynthesis (candidate); GO:0016042 lipid catabolic/metabolic related candidates | Piezophilic *Colwellia* vary in “membrane fluidity adjustment”; genes involved in “unsaturated fatty acid production” are highlighted, and all piezophiles encode a “delta-9 acyl-phospholipid desaturase”; unsaturated chains “allow better adaptation to… higher pressures” (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7, peters2023effectsofcrowding pages 9-11) | Peoples 2020, *BMC Genomics*, https://doi.org/10.1186/s12864-020-07102-y, Oct 2020; Peters 2023, *Chemical Reviews*, https://doi.org/10.1021/acs.chemrev.3c00432, Nov 2023 | **Strength:** moderate. Strong mechanistic support for pressure adaptation generally; indirect for pressure-delta breadth specifically. Taxon-specific genomic support in *Colwellia*. |
| pfaABCD polyunsaturated fatty acid biosynthesis —contributes_to→ wider high-pressure growth support | gene cluster/pathway → phenotype | KEGG candidate: pfaABCD PUFA biosynthesis; label-only if ungrounded | All strains possess “pfaABCD for PUFA synthesis,” while piezophiles additionally encode desaturase-based unsaturation systems; MT41 reportedly produces “>15% docosahexaenoic acid” (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 11-12) | Peoples 2020, *BMC Genomics*, https://doi.org/10.1186/s12864-020-07102-y, Oct 2020 | **Strength:** weak-moderate. PUFA presence alone does not explain delta, because all compared strains carry pfaABCD; useful as background node, not a decisive curated edge unless combined with other lipid features. |
| Fatty acid cis/trans isomerase presence —associates_with→ piezosensitive rather than piezophilic pressure range | gene/enzyme → phenotype class | label: fatty acid cis/trans isomerase | A “cis/trans fatty acid isomerase is encoded in piezosensitive but absent in piezophiles,” contrasting membrane adaptation strategies (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 9-11) | Peoples 2020, *BMC Genomics*, https://doi.org/10.1186/s12864-020-07102-y, Oct 2020 | **Strength:** weak. Association only; direction toward pressure-delta breadth is inferred and taxon-specific. Mark uncertain for TraitMech. |
| nuo NADH dehydrogenase I complex —supports→ high-pressure respiratory energy conservation | gene cluster/complex → process | KEGG: NADH dehydrogenase I / Complex I (candidate); GO: respiratory electron transport chain (candidate); EC class candidate | “Operons for a nuo dehydrogenase… only present in the piezophiles”; hadal piezophiles uniquely carry the NADH dehydrogenase I complex, implying respiratory-chain composition modulates pressure tolerance (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7) | Peoples 2020, *BMC Genomics*, https://doi.org/10.1186/s12864-020-07102-y, Oct 2020 | **Strength:** moderate. Good comparative genomic support; direct effect on delta breadth not experimentally isolated. |
| Additional proton-translocating NADH dehydrogenase activity —increases→ energetic efficiency at high pressure | process/complex → process | label: proton-translocating NADH dehydrogenase activity | Peoples notes a piezophile-specific NADH ubiquinone oxidoreductase region and “a unique complex I variant that translocates more protons” may improve energy acquisition under HHP (peoples2020distinctivegeneand pages 11-12) | Peoples 2020, *BMC Genomics*, https://doi.org/10.1186/s12864-020-07102-y, Oct 2020 | **Strength:** weak-moderate. Mechanistically plausible but partly interpretive; suitable as tentative edge. |
| torSTRECAD TMAO reduction pathway absence —preserves→ TMAO as candidate piezolyte | pathway → chemical/process | CHEBI: trimethylamine N-oxide (candidate); label: torSTRECAD TMAO reductase pathway | Piezosensitive strains uniquely possess “TMAO reduction”; in piezophiles tor genes are absent, and TMAO is proposed to function as a “piezolyte rather than an electron acceptor” (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 11-12) | Peoples 2020, *BMC Genomics*, https://doi.org/10.1186/s12864-020-07102-y, Oct 2020 | **Strength:** weak. Interesting hypothesis but indirect and not directly tied to measured pressure-delta breadth. Mark uncertain. |
| Increased intracellular osmolytes / cosolutes —stabilize→ proteins under pressure | chemical class/process → process | CHEBI candidate: osmolyte; label: compatible solutes / cosolutes | Peters states osmolytes “reinforce the structure of proteins” and crowding/cosolutes modulate biomolecular function under HHP; Peoples notes “compatible solutes are also important” in pressure adaptation (peters2023effectsofcrowding pages 9-11, peoples2020distinctivegeneand pages 1-2, peters2023effectsofcrowding pages 7-9) | Peters 2023, *Chemical Reviews*, https://doi.org/10.1021/acs.chemrev.3c00432, Nov 2023; Peoples 2020, *BMC Genomics*, https://doi.org/10.1186/s12864-020-07102-y, Oct 2020 | **Strength:** moderate for general HHP adaptation; weak for trait delta specifically because no organism-level delta manipulation is shown. |
| Pressure-induced ribosome dissociation —decreases→ growth-supporting pressure range breadth | process → phenotype | GO candidate: translation; label: ribosome dissociation | High pressure causes “ribosome dissociation,” and therefore “energy conservation, DNA replication, and RNA translation may become dysfunctional, preventing growth and division” (stief2023hydrostaticpressureinduces pages 1-2) | Stief 2023, *Communications Earth & Environment*, https://doi.org/10.1038/s43247-023-01045-4, Oct 2023 | **Strength:** moderate. Direct physiological mechanism linking pressure to growth failure, but from community/particle incubations rather than pure-culture delta assays. |
| Ribosome recycling factor frr downregulation at 158 MPa —perturbs→ translation recovery under extreme pressure | gene/protein → process | label: frr / ribosome recycling factor; GO candidate: translation termination/recycling | In *S. oneidensis* at 158 MPa, “ribosome recycling factor frr” was downregulated (LFC −1.39), consistent with translation stress at Titan-like pressure (malas2024biologicalfunctionsat pages 6-9) | Malas 2024, *Frontiers in Microbiology*, https://doi.org/10.3389/fmicb.2024.1293928, Feb 2024 | **Strength:** moderate for acute pressure response; weak for direct pressure-delta breadth because assay measured short exposure transcriptomics, not growth-range endpoints. |
| recN / topB / dinB / dinG DNA repair-replication response —supports→ survival and growth under high pressure stress | genes/process → process | GO candidate: DNA repair; GO candidate: DNA topological change; label-only genes recN, topB, dinB, dinG | At 158 MPa, *S. oneidensis* upregulated “recN, topB, dinB, dinG_1” with LFC ≥2; piezophilic *Colwellia* are enriched in “replication/recombination/repair” genes (malas2024biologicalfunctionsat pages 6-9, peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 9-11) | Malas 2024, *Frontiers in Microbiology*, https://doi.org/10.3389/fmicb.2024.1293928, Feb 2024; Peoples 2020, *BMC Genomics*, https://doi.org/10.1186/s12864-020-07102-y, Oct 2020 | **Strength:** moderate. Strong stress-response evidence and comparative enrichment; direct link to delta breadth remains inferred. |
| More basic and hydrophobic proteome composition —stabilizes→ proteins against pressure-induced water intrusion | proteome property → process | label: basic proteome; label: hydrophobic proteome | Piezophilic *Colwellia* have “a more basic and hydrophobic proteome”; this may “stabilize and limit water intrusion into proteins as a result of high pressure” (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 9-11) | Peoples 2020, *BMC Genomics*, https://doi.org/10.1186/s12864-020-07102-y, Oct 2020 | **Strength:** moderate. Comparative and mechanistically coherent, but still association-level for pressure delta. |
| Modulation of electrostatic interactions in proteins —adapts_to→ higher hydrostatic pressure | process/proteome property → phenotype | label: electrostatic interaction modulation | Makhatadze proposes “modulation of interactions between charged residues” as a driver of *Colwellia* adaptation to HHP; strain ranges cited include MTCD1 “80–140 MPa” and MT41 “above 35 MPa” with optimum 103 MPa (makhatadze2024modulationofelectrostatic pages 1-3) | Makhatadze 2024, *bioRxiv*, https://doi.org/10.1101/2024.07.28.605522, Jul 2024 | **Strength:** weak. Preprint and hypothesis-driven; not yet strong enough for direct curation without corroborating experiments. |
| Cold-shock protein CspG induction —supports→ high-pressure stress tolerance | gene/protein → process | label: cspG / cold-shock protein; GO candidate: response to stress | *S. oneidensis* under 158 MPa induced “cold-shock protein CspG”; authors interpret this as a stress-response adaptation shared with other extremes (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 9-10) | Malas 2024, *Frontiers in Microbiology*, https://doi.org/10.3389/fmicb.2024.1293928, Feb 2024 | **Strength:** moderate for acute response; weak for pressure-delta breadth specifically. |
| Antioxidant defense induction —supports→ viability after extreme pressure exposure | process → process | GO candidate: response to oxidative stress | MR-1 at 158 MPa used “antioxidant defense related genes,” indicating oxidative-stress management during HHP exposure (malas2024biologicalfunctionsat pages 1-2) | Malas 2024, *Frontiers in Microbiology*, https://doi.org/10.3389/fmicb.2024.1293928, Feb 2024 | **Strength:** weak-moderate. Relevant stress node, but direct causal link to growth-range breadth remains untested. |
| Loss of membrane fluidity at high pressure —restricts→ growth at upper pressure bound | process → phenotype | GO candidate: membrane organization; label: membrane fluidity loss | High pressure causes “loss of membrane fluidity”; Stief similarly states reduced membrane fluidity under HHP, with respiration and diatom degradation ceasing by 60 MPa in non-adapted aggregate communities (malas2024biologicalfunctionsat pages 2-3, stief2023hydrostaticpressureinduces pages 1-2) | Malas 2024, *Frontiers in Microbiology*, https://doi.org/10.3389/fmicb.2024.1293928, Feb 2024; Stief 2023, *Communications Earth & Environment*, https://doi.org/10.1038/s43247-023-01045-4, Oct 2023 | **Strength:** strong for general upper-bound limitation; moderate for direct organismal delta because much evidence is physiological/community-level rather than curated strain-range assays. |
| Growth phase: early stationary phase —increases→ HHP resistance relative to exponential phase | environment/assay factor → phenotype | label: early stationary phase; label: exponential phase | Malas notes “early stationary phase” cells are “more HHP resistant than cells in exponential phase” (malas2024biologicalfunctionsat pages 2-3) | Malas 2024, *Frontiers in Microbiology*, https://doi.org/10.3389/fmicb.2024.1293928, Feb 2024 | **Strength:** moderate. Important assay modifier for observed pressure delta; resistance not always equivalent to sustained growth. |
| Exposure duration at 158 MPa —modulates→ apparent pressure tolerance / post-pressure growth | environment/assay factor → phenotype | label: pressure exposure duration | MR-1 was tested at 158 MPa for “15 min” and “2 h”; cells remained metabolically active in situ and showed viable growth after “2 h exposure… with minimal pressure training” (malas2024biologicalfunctionsat pages 1-2) | Malas 2024, *Frontiers in Microbiology*, https://doi.org/10.3389/fmicb.2024.1293928, Feb 2024 | **Strength:** moderate. Clear assay dependence; describes survival/viability more than formal growth-range delta. |
| Temperature–pressure interaction via homeoviscous adaptation —modulates→ breadth of pressure supporting growth | environment/process → phenotype | label: homeoviscous adaptation; ENVO candidate: deep ocean high-pressure environment | In *Carnobacterium*, “increasing pressure and decreasing temperature both tend to compress membranes”; cells maintain fluidity by altering lipid composition, and 11/14 strains grew across 10^3–10^7 Pa at 2°C (miller2023carnobacteriumspeciescapableof pages 8-9, miller2023carnobacteriumspeciescapableof pages 1-3) | Miller 2023, *Astrobiology*, https://doi.org/10.1089/ast.2022.0043, Jan 2023 | **Strength:** moderate. Strong real-world breadth example, but mechanistic edge remains general rather than gene-resolved. |
| Hydrostatic pressure ≥60 MPa in marine-snow incubations —suppresses→ respiration and community growth processes | environment/assay factor → process | ENVO candidate: marine snow; label: oxygen consumption / respiration | In simulated sinking particles, oxygen consumption “decreased across 0.1–40 MPa and then ceased completely by 60–100 MPa”; at 60 MPa “respiration and diatom degradation ceased completely” (stief2023hydrostaticpressureinduces pages 1-2) | Stief 2023, *Communications Earth & Environment*, https://doi.org/10.1038/s43247-023-01045-4, Oct 2023 | **Strength:** moderate. Strong pressure-threshold evidence, but from mixed communities and ecological process readouts rather than single-strain pressure-delta phenotype. |
| Min/max growth pressure bounds —define→ pressure delta breadth descriptor | phenotype component → phenotype | METPO: traitmech:000006 (target trait); label: minimum growth pressure; label: maximum growth pressure | *Colwellia* examples provide direct range bounds: MT41 “does not grow… below 35 MPa” and optimum 103 MPa; MTCD1 has “growth range from 80 to 140 MPa” with optimum 120 MPa, implying delta = 60 MPa (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media 84a4f0b4, makhatadze2024modulationofelectrostatic pages 1-3) | Peoples 2020, *BMC Genomics*, https://doi.org/10.1186/s12864-020-07102-y, Oct 2020; Makhatadze 2024, *bioRxiv*, https://doi.org/10.1101/2024.07.28.605522, Jul 2024 | **Strength:** strong for trait definition and direct curation anchor; not itself a mechanism, but essential to scope what downstream edges should explain. |


*Table: This table lists candidate causal edges for the microbial trait pressure delta, combining direct growth-range examples with mechanistic and assay-level factors reported to influence pressure-supported growth. It is useful as a curation scaffold because it separates stronger, directly evidenced edges from weaker or taxon-specific hypotheses.*

### 8) Expert analysis (what is most curation-ready now)

**Most curation-ready edges** for a TraitMech graph are those where sources explicitly link pressure to a limiting cellular subsystem that determines growth feasibility (upper/lower bounds), and/or where a comparative genomic pattern strongly distinguishes piezophiles from non-piezophiles:
- Pressure → **loss of membrane fluidity** → growth limitation (mechanistic, cross-taxa; supports upper-bound interpretation) (malas2024biologicalfunctionsat pages 2-3, stief2023hydrostaticpressureinduces pages 1-2).  
- Pressure → **ribosome dissociation / translation suppression** → growth limitation (direct limiting pathway, though sometimes inferred from physiological outcomes) (stief2023hydrostaticpressureinduces pages 1-2, malas2024biologicalfunctionsat pages 2-3).  
- Presence of **nuo complex I** in hadal piezophiles (comparative genomic discriminator; candidate causal contributor to wider high-pressure growth support) (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 1-2).  
- **Membrane lipid unsaturation machinery** (desaturases, PUFA synthesis) as central pressure-adaptation node (strong conceptual support; specific gene-level edges likely taxon-specific) (peoples2020distinctivegeneand pages 5-7, peters2023effectsofcrowding pages 9-11).

**Edges to curate as uncertain** until stronger direct tests link them to pressure *breadth* (not only acute response):
- TMAO metabolism differences (tor genes absent in piezophiles; TMAO as proposed piezolyte) because evidence is currently comparative/inferential rather than causal for pressure delta (peoples2020distinctivegeneand pages 5-7).  
- Proteome-level electrostatics modulation as a driver of adaptation (preprint hypothesis) (makhatadze2024modulationofelectrostatic pages 1-3).  
- Acute transcriptomic responses in MR-1 at 158 MPa (valuable candidate nodes, but not yet pressure-delta endpoints) (malas2024biologicalfunctionsat pages 6-9, malas2024biologicalfunctionsat pages 9-10).

### 9) DOI-first bibliography (with URLs and publication dates where available)

1. Malas J. et al. **Biological functions at high pressure: transcriptome response of *Shewanella oneidensis* MR-1 to hydrostatic pressure relevant to Titan and other icy ocean worlds.** *Frontiers in Microbiology*. Published **13 Feb 2024**. DOI: 10.3389/fmicb.2024.1293928. URL: https://doi.org/10.3389/fmicb.2024.1293928 (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 2-3, malas2024biologicalfunctionsat pages 6-9, malas2024biologicalfunctionsat pages 9-10)

2. Peters J. et al. **Effects of crowding and cosolutes on biomolecular function at extreme environmental conditions.** *Chemical Reviews*. **Nov 2023**. DOI: 10.1021/acs.chemrev.3c00432. URL: https://doi.org/10.1021/acs.chemrev.3c00432 (peters2023effectsofcrowding pages 9-11, peters2023effectsofcrowding pages 7-9)

3. Stief P. et al. **Hydrostatic pressure induces transformations in the organic matter and microbial community composition of marine snow particles.** *Communications Earth & Environment*. **Oct 2023**. DOI: 10.1038/s43247-023-01045-4. URL: https://doi.org/10.1038/s43247-023-01045-4 (stief2023hydrostaticpressureinduces pages 1-2)

4. Miller K.M. et al. **Carnobacterium species capable of growth at pressures ranging over 5 orders of magnitude, from the surface of Mars (10^3 Pa) to deep oceans (10^7 Pa) in the Solar System.** *Astrobiology*. **Jan 2023**. DOI: 10.1089/ast.2022.0043. URL: https://doi.org/10.1089/ast.2022.0043 (miller2023carnobacteriumspeciescapableof pages 1-3, miller2023carnobacteriumspeciescapableof pages 8-9)

5. Peoples L.M. et al. **Distinctive gene and protein characteristics of extremely piezophilic *Colwellia*.** *BMC Genomics*. **Oct 2020**. DOI: 10.1186/s12864-020-07102-y. URL: https://doi.org/10.1186/s12864-020-07102-y (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand media 84a4f0b4)

6. Makhatadze G.I. **Modulation of electrostatic interactions as a mechanism of cryptic adaptation of *Colwellia* to high hydrostatic pressure.** *bioRxiv* preprint. **Jul 2024**. DOI: 10.1101/2024.07.28.605522. URL: https://doi.org/10.1101/2024.07.28.605522 (makhatadze2024modulationofelectrostatic pages 1-3)

### 10) Warnings (claims not ready for TraitMech curation)

- **Do not treat survival at extreme pressure as growth-range expansion.** Non-piezophiles can survive short exposures up to ~1.5 GPa, but that does not define growth-supporting pressure delta (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 2-3).  
- **Community-level pressure thresholds are not isolate traits.** Marine-snow microcosm respiration cessation at 60 MPa is valuable, but should be curated as an environmental/process relationship, not as an organism’s pressure-delta phenotype (stief2023hydrostaticpressureinduces pages 1-2).  
- **Preprint hypotheses require corroboration.** Electrostatic interaction modulation is plausible but currently hypothesis-level and should be marked uncertain (makhatadze2024modulationofelectrostatic pages 1-3).  
- **Comparative genomics associations are not necessarily causal.** Genes enriched in piezophiles (e.g., nuo, desaturases) are strong candidates but typically require functional validation before being curated as definitive causal edges for pressure delta (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 1-2).


References

1. (peoples2020distinctivegeneand pages 1-2): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

2. (peoples2020distinctivegeneand media 84a4f0b4): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

3. (malas2024biologicalfunctionsat pages 1-2): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

4. (malas2024biologicalfunctionsat pages 2-3): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

5. (peters2023effectsofcrowding pages 7-9): Judith Peters, Rosario Oliva, Antonino Caliò, Philippe Oger, and Roland Winter. Effects of crowding and cosolutes on biomolecular function at extreme environmental conditions. Chemical reviews, 123:13441-13488, Nov 2023. URL: https://doi.org/10.1021/acs.chemrev.3c00432, doi:10.1021/acs.chemrev.3c00432. This article has 46 citations and is from a highest quality peer-reviewed journal.

6. (stief2023hydrostaticpressureinduces pages 8-9): Peter Stief, Clemens Schauberger, Kevin W. Becker, Marcus Elvert, John Paul Balmonte, Belén Franco-Cisterna, Mathias Middelboe, and Ronnie N. Glud. Hydrostatic pressure induces transformations in the organic matter and microbial community composition of marine snow particles. Communications Earth &amp; Environment, Oct 2023. URL: https://doi.org/10.1038/s43247-023-01045-4, doi:10.1038/s43247-023-01045-4. This article has 18 citations and is from a peer-reviewed journal.

7. (stief2023hydrostaticpressureinduces pages 1-2): Peter Stief, Clemens Schauberger, Kevin W. Becker, Marcus Elvert, John Paul Balmonte, Belén Franco-Cisterna, Mathias Middelboe, and Ronnie N. Glud. Hydrostatic pressure induces transformations in the organic matter and microbial community composition of marine snow particles. Communications Earth &amp; Environment, Oct 2023. URL: https://doi.org/10.1038/s43247-023-01045-4, doi:10.1038/s43247-023-01045-4. This article has 18 citations and is from a peer-reviewed journal.

8. (peters2023effectsofcrowding pages 9-11): Judith Peters, Rosario Oliva, Antonino Caliò, Philippe Oger, and Roland Winter. Effects of crowding and cosolutes on biomolecular function at extreme environmental conditions. Chemical reviews, 123:13441-13488, Nov 2023. URL: https://doi.org/10.1021/acs.chemrev.3c00432, doi:10.1021/acs.chemrev.3c00432. This article has 46 citations and is from a highest quality peer-reviewed journal.

9. (malas2024biologicalfunctionsat pages 9-10): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

10. (malas2024biologicalfunctionsat pages 6-9): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

11. (miller2023carnobacteriumspeciescapableof pages 1-3): Kathleen M. Miller, Flora Tang, Sixuan Li, Kelli K. Mullane, Brontë R. Shelton, Lam Bui, Douglas H. Bartlett, and Wayne L. Nicholson. <i>carnobacterium</i>species capable of growth at pressures ranging over 5 orders of magnitude, from the surface of mars (10<sup>3</sup>pa) to deep oceans (10<sup>7</sup>pa) in the solar system. Astrobiology, 23:94-104, Jan 2023. URL: https://doi.org/10.1089/ast.2022.0043, doi:10.1089/ast.2022.0043. This article has 2 citations and is from a peer-reviewed journal.

12. (makhatadze2024modulationofelectrostatic pages 1-3): George I. Makhatadze. Modulation of electrostatic interactions as a mechanism of cryptic adaptation of colwellia to high hydrostatic pressure. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.28.605522, doi:10.1101/2024.07.28.605522. This article has 1 citations.

13. (miller2023carnobacteriumspeciescapableof pages 8-9): Kathleen M. Miller, Flora Tang, Sixuan Li, Kelli K. Mullane, Brontë R. Shelton, Lam Bui, Douglas H. Bartlett, and Wayne L. Nicholson. <i>carnobacterium</i>species capable of growth at pressures ranging over 5 orders of magnitude, from the surface of mars (10<sup>3</sup>pa) to deep oceans (10<sup>7</sup>pa) in the solar system. Astrobiology, 23:94-104, Jan 2023. URL: https://doi.org/10.1089/ast.2022.0043, doi:10.1089/ast.2022.0043. This article has 2 citations and is from a peer-reviewed journal.

14. (peoples2020distinctivegeneand pages 5-7): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

15. (peoples2020distinctivegeneand pages 9-11): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

16. (peoples2020distinctivegeneand pages 11-12): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.