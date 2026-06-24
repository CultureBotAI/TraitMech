---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:26:44.895071'
end_time: '2026-06-18T05:43:33.823494'
duration_seconds: 1008.93
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Oxidative phosphorylation
  trait_identifier: METPO:1000803
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: oxidative_phosphorylation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism that generates ATP through the transfer of electrons from
    electron donors to electron acceptors via redox reactions, coupled to the pumping
    of protons across a membrane to create an electrochemical gradient.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1038/191144a0: phosphorylation to electron and hydrogen
    transfer (Mitchell''s chemiosmotic proposal supports coupling electron transfer
    to phosphorylation.) | DOI:10.1038/s41598-019-38564-0: energized by the proton
    motive force (Supports proton motive force-driven ATP synthesis by F1Fo ATP synthase.)'
  causal_graph_summary: 'oxidative_phosphorylation_chemiosmotic_coupling: 6 nodes,
    5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Oxidative phosphorylation
- **METPO identifier:** METPO:1000803
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that generates ATP through the transfer of electrons from electron donors to electron acceptors via redox reactions, coupled to the pumping of protons across a membrane to create an electrochemical gradient.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/191144a0: phosphorylation to electron and hydrogen transfer (Mitchell's chemiosmotic proposal supports coupling electron transfer to phosphorylation.) | DOI:10.1038/s41598-019-38564-0: energized by the proton motive force (Supports proton motive force-driven ATP synthesis by F1Fo ATP synthase.)
- **Existing causal graph summary:** oxidative_phosphorylation_chemiosmotic_coupling: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **Oxidative phosphorylation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/oxidative_phosphorylation.yaml`.

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
- **Trait label:** Oxidative phosphorylation
- **METPO identifier:** METPO:1000803
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that generates ATP through the transfer of electrons from electron donors to electron acceptors via redox reactions, coupled to the pumping of protons across a membrane to create an electrochemical gradient.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/191144a0: phosphorylation to electron and hydrogen transfer (Mitchell's chemiosmotic proposal supports coupling electron transfer to phosphorylation.) | DOI:10.1038/s41598-019-38564-0: energized by the proton motive force (Supports proton motive force-driven ATP synthesis by F1Fo ATP synthase.)
- **Existing causal graph summary:** oxidative_phosphorylation_chemiosmotic_coupling: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **Oxidative phosphorylation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/oxidative_phosphorylation.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Oxidative Phosphorylation (METPO:1000803)

### Scope summary (Trait scope and boundary cases)
**Oxidative phosphorylation (OXPHOS)** in microbes is the physiological capacity to generate ATP using a membrane-bound ATP synthase driven by an electrochemical ion gradient (typically a proton motive force, PMF) that is established by electron transfer through a respiratory chain to a terminal electron acceptor (often O2 in aerobic respiration). This coupling is explicitly described as respiration generating a “proton electrochemical gradient” that is converted to ATP by ATP synthase (henry2024drugrepurposingapproachesto pages 24-28), and as complex I forming PMF that “drives ATP synthesis in oxidative phosphorylation” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2).

**Boundary cases and distinctions** relevant for curation:
- **Versus substrate-level phosphorylation:** OXPHOS requires an electrochemical gradient and ATP synthase; substrate-level phosphorylation does not (implied by defining ATP synthesis specifically “through conversion of the proton electrochemical gradient by ATP synthase”) (henry2024drugrepurposingapproachesto pages 24-28).
- **Aerobic vs anaerobic respiration:** Aerobic respiration is defined by final electron transfer to oxygen producing water and generating a proton electrochemical gradient (henry2024drugrepurposingapproachesto pages 24-28). Anaerobic respiration uses a final electron acceptor other than oxygen but still can conserve energy via ATP synthase (henry2024drugrepurposingapproachesto pages 24-28). This trait can be curated as respiratory-chain-driven phosphorylation regardless of terminal acceptor, but the strongest evidence in this packet is for oxygen respiration.
- **Versus photophosphorylation:** Not covered by the evidence retrieved here; should be treated as a nearby trait unless the trait definition is broadened.
- **Terminal oxidase boundary case (important):** heme–copper oxidases are “true proton pumps,” while **cytochromes bd** contribute to PMF without proton pumping, via “vector transfer of protons along the intraprotein proton-conducting pathway” (nastasi2024membraneboundredoxenzyme pages 1-2). This is a key mechanistic nuance for causal-graph edges.

---

## 1) Key concepts and definitions (current understanding)

### Chemiosmotic coupling and PMF
Recent bioenergetics reviews explicitly connect electron transfer to vectorial proton translocation and PMF generation. For example, proton-translocating NADH–ubiquinone oxidoreductase (complex I/NDH-1) couples NADH oxidation to “vectorial transmembrane transfer of four H+ ions” and conserves energy “in the form of an electrochemical gradient… (proton motive force, pmf),” which is used “primarily for ATP synthesis in oxidative phosphorylation” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2).

### Respiratory chain branching in bacteria
Bacteria can have branched electron transport chains with alternative entry dehydrogenases and multiple terminal oxidases. For *E. coli*, “type I and type II NADH dehydrogenases transfer electrons from NADH to ubiquinone-8 and/or menaquinone-8,” and electrons then flow to three terminal oxidases (bo3, bd-I, bd-II) to reduce O2 to water (nastasi2024membraneboundredoxenzyme pages 1-2). In *Bacillus licheniformis*, a branched chain with “various terminal oxidases” is inferred from the ability to respire in cyanide (uriberamirez2024modificationsofthe pages 1-2).

### Distinct terminal oxidase mechanisms
Terminal oxidases catalyze “four-electron reduction of O2 to 2H2O” and this redox chemistry is “coupled to the generation of proton-motive force” (nastasi2024membraneboundredoxenzyme pages 1-2). However, the mechanism differs across oxidase families: heme–copper oxidases pump protons, whereas cytochrome bd does not pump but can still contribute to PMF via vectorial proton transfer (nastasi2024membraneboundredoxenzyme pages 1-2).

---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### (A) Complex I mechanistic/structural progress (2024)
A 2024 review emphasizes that “great progress has been achieved in resolving complex I structure” by high-resolution cryo-EM and X-ray crystallography, enabling detailed hypotheses for coupling redox chemistry to proton translocation (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2). Mechanistically, the same review provides quantitative coupling context: ubiquinol produced by complex I delivers electrons down the chain to oxygen “coupled to the transmembrane transfer of six more protons,” and complex I contributes “approximately 40% to the total energy storage during the transfer of electrons from NADH to molecular oxygen” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2). These statements support curation of edges linking complex I proton pumping to PMF and downstream respiratory energy conservation.

### (B) OXPHOS as an anti-tuberculosis target and stress-adapted routing (2024)
A 2024 review on *Mycobacterium tuberculosis* frames OXPHOS as central to ATP/ADP homeostasis in stressful conditions and dormancy, and describes the ETC components that feed electrons into the menaquinone pool (NDH-1/NDH-2, succinate dehydrogenases Sdh-1/Sdh-2, and malate:quinone oxidoreductase Mqo), and downstream terminal oxidases (bcc/aa3 supercomplex and cytochrome bd) that reduce oxygen to water (harikishore2024mycobacteriumtuberculosisfatp pages 1-2). The review explicitly describes that as electrons traverse the ETC “protons are translocated… to generate the proton motive force (pmf),” and that proton return through the Fo domain provides “torque” for ATP synthesis (harikishore2024mycobacteriumtuberculosisfatp pages 1-2). It also provides a clear example of condition-dependent routing: proton-translocating Ndh-1 is used “during aerobic growth” while “non-proton contributing Ndh-2” is used “during hypoxia” (harikishore2024mycobacteriumtuberculosisfatp pages 1-2).

### (C) Terminal oxidases and gas/toxin resilience (2024)
A 2024 experimental paper on *E. coli* terminal oxidases reports that adding CO had “minimal effect on growth” in bd-I-only cells but severely impaired growth in bd-II-only and bo3-only strains, and that bd-I-only respiration is relatively CO-resistant (nastasi2024membraneboundredoxenzyme pages 1-2). The paper includes mechanistic schematics showing that CO can inhibit bo3 by binding to the active-site heme, whereas bd-I is relatively CO-resistant due to weak/high-off-rate binding (nastasi2024membraneboundredoxenzyme media 5dea1c8d). This supports an environment→terminal oxidase activity modulation module.

### (D) OXPHOS and persistence/tolerance (2024)
A 2024 minireview on PMF and antibiotic tolerance emphasizes that persisters require PMF for oxidative phosphorylation to power energy-demanding maintenance functions, and describes evidence that ETC components (e.g., NADH dehydrogenases I and II) are important for tolerance formation (wan2024protonmotiveforce pages 6-7). It also cites that respiratory inhibitors such as sodium azide showed strong killing effects on persisters (wan2024protonmotiveforce pages 6-7), providing an application-oriented edge linking OXPHOS/PMF disruption to persister eradication.

---

## 3) Current applications and real-world implementations

### Antimicrobial drug targeting of OXPHOS
- **Clinically deployed targeting (TB):** The 2024 *M. tuberculosis* review highlights **bedaquiline** as a “potent Mtb F1FO-ATP synthase inhibitor” active against replicating and non-replicating mycobacteria, bringing OXPHOS “into focus as an anti-TB target” (harikishore2024mycobacteriumtuberculosisfatp pages 1-2). It also gives global health context: TB is described as causing “over 1.13 million deaths annually,” and with “about 10.6 million new infections” (estimates referenced by the review) (harikishore2024mycobacteriumtuberculosisfatp pages 1-2).
- **Terminal oxidase inhibitors / drug repurposing pipelines:** A 2024 thesis focuses on in silico discovery of cytochrome bd inhibitors and states that respiration generates a proton electrochemical gradient used by ATP synthase (henry2024drugrepurposingapproachesto pages 24-28). It also provides a candidate quinone-site bd-I inhibitor (AD3-11), but as a thesis-derived claim it should be curated cautiously (henry2024drugrepurposingapproachesto pages 31-37).

### Environmental/host-derived gases as modulators (CO, cyanide)
- **CO as antimicrobial strategy:** The 2024 *E. coli* oxidase study notes that CO-releasing molecules (CORMs) can have additive effects with antibiotics in some microbes and frames CO delivery as an emerging antimicrobial strategy; it also cautions about off-target/toxicity mechanisms for certain CORMs (nastasi2024membraneboundredoxenzyme pages 1-2).
- **Cyanide tolerance via branched respiration:** *B. licheniformis* can “carry out aerobic respiration in the presence” of cyanide, consistent with a “branched respiratory chain with various terminal oxidases” (uriberamirez2024modificationsofthe pages 1-2). This kind of evidence supports adding environment→respiratory-branching edges.

---

## 4) Expert opinions and analysis (authoritative interpretations)

### Why cytochrome bd matters mechanistically
The distinction between proton pumping vs vectorial proton transfer is repeatedly emphasized: “Heme-copper oxidases are true proton pumps, whereas cytochromes bd generate proton-motive force solely due to the vector transfer of protons… without a mechanism of proton pumping” (nastasi2024membraneboundredoxenzyme pages 1-2). For trait curation, this supports representing **cytochrome bd** as contributing to PMF/Δψ without a canonical pumped-proton stoichiometry node.

### Why OXPHOS is an attractive antibacterial target
The persistence-focused review argues that active tolerance mechanisms are energy demanding, therefore persisters need PMF for oxidative phosphorylation, and the review highlights that disrupting PMF/ETC components can produce stronger persister killing than deleting single tolerance genes (wan2024protonmotiveforce pages 6-7). This supports adding a “PMF maintenance → tolerance maintenance” module as an application branch of the trait causal graph.

---

## 5) Recent statistics and quantitative data points

- **Complex I energetics:** Complex I transfers “four H+ ions” per NADH:quinone turnover (vectorial transmembrane transfer), and is stated to contribute “approximately 40%” to total energy storage during electron transfer from NADH to oxygen in the chain context discussed (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2).
- **TB burden and incidence:** The 2024 TB review states “over 1.13 million deaths annually” and “about 10.6 million new infections” (global estimates cited by the authors) (harikishore2024mycobacteriumtuberculosisfatp pages 1-2).
- **Terminal oxidase expression vs aeration (E. coli):** A chemostat-based conclusion summarized in the 2024 oxidase paper states bo3 operon is maximally induced under “fully aerobic conditions,” bd-I at “56% aerobiosis,” and bd-II at “0% aerobiosis” (nastasi2024membraneboundredoxenzyme pages 1-2). These are valuable quantitative condition→component-expression edges (though specific to *E. coli*).
- **Antibiotic pipeline count (context):** The 2024 thesis states that “Up to December 2020… 43 antibiotics” were in phases 1–3 or pending approval (henry2024drugrepurposingapproachesto pages 24-28). This is not OXPHOS-specific but contextualizes the motivation for alternative targets.

---

# Candidate nodes (grouped by type)
The following table is a curation-ready node inventory with suggested groundings.

| Node type | Node label | Suggested CURIE(s) if available | Source support (context IDs) | Notes |
|---|---|---|---|---|
| Process | oxidative phosphorylation | GO:0006119; METPO:1000803 | (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Core trait; ATP synthesis driven by ETC-generated electrochemical gradient. |
| Process | proton motive force | GO:0015992 | (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2, wan2024protonmotiveforce pages 6-7) | Central energetic intermediate; may include ΔpH and Δψ. |
| Process | proton translocation | GO:1902600 | (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Includes pumping and vectorial transfer; important boundary case for bd oxidases. |
| Process | oxygen reduction to water | GO:0019416 | (nastasi2024membraneboundredoxenzyme pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Terminal oxidase function in aerobic respiration. |
| Process | ATP synthesis coupled to proton transport | GO:0015986 | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Distinguishes OXPHOS from substrate-level phosphorylation. |
| Process | aerobic respiration | GO:0009060 | (nastasi2024membraneboundredoxenzyme pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Canonical context for many cited oxidases. |
| Process | anaerobic respiration | GO:0009061 | (henry2024drugrepurposingapproachesto pages 24-28) | Nearby trait; relevant as boundary case, not directly detailed for specific reductases in provided contexts. |
| Complex/Protein | Complex I / NDH-1 / NADH:quinone oxidoreductase | EC:7.1.1.2 | (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Proton-translocating entry complex; strong core node. |
| Complex/Protein | NDH-2 / type II NADH dehydrogenase | label-only; EC assignment varies in databases | (uriberamirez2024modificationsofthe pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2, wan2024protonmotiveforce pages 6-7) | Non-proton-pumping NADH dehydrogenase; taxon-specific use under hypoxia in mycobacteria. |
| Complex/Protein | succinate dehydrogenase / Complex II | EC:1.3.5.1 | (uriberamirez2024modificationsofthe pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Electron entry from succinate; proton-coupling status can vary in descriptions across taxa/sources. |
| Complex/Protein | malate:quinone oxidoreductase (Mqo) | EC:1.1.5.4 | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Supported in mycobacteria; not universal. |
| Complex/Protein | cytochrome bc complex | label-only | (uriberamirez2024modificationsofthe pages 1-2) | Bacillus/Actinobacteria-style bc complex; proton-translocating via redox coupling. |
| Complex/Protein | cytochrome bcc/aa3 oxidase supercomplex | label-only | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Mycobacterial supercomplex; accepts electrons from menaquinol and reduces O2. |
| Complex/Protein | cytochrome bd oxidase | label-only | (nastasi2024membraneboundredoxenzyme pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Non-proton-pumping but electrogenic terminal oxidase; important boundary case. |
| Complex/Protein | cytochrome bd-I oxidase | label-only | (nastasi2024membraneboundredoxenzyme pages 1-2, nastasi2024membraneboundredoxenzyme media 5dea1c8d) | E. coli isoform; relatively CO-resistant. |
| Complex/Protein | cytochrome bd-II oxidase | label-only | (nastasi2024membraneboundredoxenzyme pages 1-2, nastasi2024membraneboundredoxenzyme media 5dea1c8d) | E. coli isoform; more CO-sensitive than bd-I. |
| Complex/Protein | cytochrome bo3 quinol oxidase | label-only | (nastasi2024membraneboundredoxenzyme pages 1-2, nastasi2024membraneboundredoxenzyme media 5dea1c8d) | Heme-copper oxidase; preferentially expressed at high aeration in E. coli. |
| Complex/Protein | F1Fo-ATP synthase / F-type ATP synthase | GO:0042777 | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Final ATP-producing complex; core defining node. |
| Complex/Protein | Fo domain of ATP synthase | label-only | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Membrane proton-translocating sector. |
| Complex/Protein | F1 sector of ATP synthase | label-only | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Soluble catalytic ATP-synthesizing sector. |
| Gene (example) | nuoL | NCBIGene label-only | (wan2024protonmotiveforce pages 6-7) | Example ETC gene linked to PMF maintenance/tolerance; species-specific. |
| Gene (example) | ndh | NCBIGene label-only | (wan2024protonmotiveforce pages 6-7) | Example NDH-2-associated gene; role in tolerance formation discussed in review. |
| Gene (example) | cyoABCDE | NCBIGene label-only | (nastasi2024membraneboundredoxenzyme pages 1-2) | E. coli bo3 operon; example gene set, taxon-specific. |
| Gene (example) | cydABX | NCBIGene label-only | (nastasi2024membraneboundredoxenzyme pages 1-2) | E. coli bd-I operon; example gene set, taxon-specific. |
| Gene (example) | appCBX | NCBIGene label-only | (nastasi2024membraneboundredoxenzyme pages 1-2) | E. coli bd-II operon; example gene set, taxon-specific. |
| Small molecule/metabolite | proton | CHEBI:15378 | (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Core translocated ion in cited systems. |
| Small molecule/metabolite | oxygen | CHEBI:15379 | (nastasi2024membraneboundredoxenzyme pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Terminal electron acceptor in aerobic examples. |
| Small molecule/metabolite | water | CHEBI:15377 | (nastasi2024membraneboundredoxenzyme pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Product of terminal oxygen reduction. |
| Small molecule/metabolite | ATP | CHEBI:15422 | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Trait output. |
| Small molecule/metabolite | ADP | CHEBI:16761 | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | ATP synthase substrate. |
| Small molecule/metabolite | phosphate | CHEBI:43474 | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | ATP synthase substrate; inorganic phosphate. |
| Small molecule/metabolite | NADH | CHEBI:16908 | (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Major electron donor. |
| Small molecule/metabolite | quinone pool | label-only | (uriberamirez2024modificationsofthe pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Generic node useful across taxa; includes ubiquinone or menaquinone. |
| Small molecule/metabolite | ubiquinone | CHEBI:16389 | (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, nastasi2024membraneboundredoxenzyme pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Common in Gram-negative examples and generic reviews. |
| Small molecule/metabolite | ubiquinol | CHEBI:17976 | (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Reduced quinone carrier. |
| Small molecule/metabolite | menaquinone | CHEBI:18009 | (nastasi2024membraneboundredoxenzyme pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Major quinone in mycobacterial examples; exact CHEBI may need curator verification by side chain class. |
| Small molecule/metabolite | menaquinol | label-only | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Reduced quinone carrier in mycobacterial ETC. |
| Small molecule/metabolite | succinate | CHEBI:30031 | (uriberamirez2024modificationsofthe pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Electron donor via SDH. |
| Small molecule/metabolite | fumarate | CHEBI:18012 | (henry2024drugrepurposingapproachesto pages 24-28) | Product of succinate oxidation in overview source. |
| Small molecule/metabolite | malate | CHEBI:30797 | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Electron donor via Mqo in mycobacteria. |
| Environmental factor | hypoxia | ENVO:01000736 | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Supports alternate respiratory routing in mycobacteria. |
| Environmental factor | low oxygen / microaerobic conditions | label-only | (nastasi2024membraneboundredoxenzyme pages 1-2) | E. coli bd oxidases induced as oxygen decreases. |
| Environmental factor | starvation / nutrient starvation | label-only | (wan2024protonmotiveforce pages 6-7) | PMF maintenance and residual OXPHOS linked to persistence. |
| Environmental factor | carbon monoxide | CHEBI:17245 | (nastasi2024membraneboundredoxenzyme pages 1-2, nastasi2024membraneboundredoxenzyme media 5dea1c8d) | Environmental/toxic gas affecting terminal oxidases. |
| Environmental factor | cyanide | CHEBI:17514 | (uriberamirez2024modificationsofthe pages 1-2) | Inhibitory condition revealing branched respiration in B. licheniformis. |
| Environmental factor | alkaline medium / alkaline pH | label-only | (uriberamirez2024modificationsofthe pages 1-2) | Experimental/environmental modifier in B. licheniformis study. |
| Inhibitor/drug | bedaquiline | CHEBI:67457 | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Validated mycobacterial ATP synthase inhibitor; application-focused node. |
| Inhibitor/drug | sodium azide | CHEBI:35318 | (wan2024protonmotiveforce pages 6-7) | Respiratory chain inhibitor used in persistence context; indirect OXPHOS evidence. |
| Inhibitor/drug | antimycin A | CHEBI:29688 | (uriberamirez2024modificationsofthe pages 1-2) | Mentioned as inhibitor of bc complex; strong mechanistic utility. |
| Inhibitor/drug | CO-releasing molecules (CORMs) | label-only | (nastasi2024membraneboundredoxenzyme pages 1-2) | Antimicrobial strategy context; broad class rather than single compound. |
| Cellular location | plasma membrane / bacterial cytoplasmic membrane | GO:0005886 | (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2, henry2024drugrepurposingapproachesto pages 24-28) | Core location of prokaryotic OXPHOS. |
| Cellular location | coupling membrane | label-only | (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | Useful generic bioenergetic location term from review. |
| Cellular location | cytoplasm | GO:0005737 | (uriberamirez2024modificationsofthe pages 1-2, harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Proton source/sink side in cited bacterial examples. |
| Cellular location | intermembrane space | GO:0005757 | (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | Used in Mtb review wording; biologically awkward for bacteria, so curate cautiously as author terminology. |


*Table: This table lists candidate entities for a microbial oxidative phosphorylation causal graph, grouped by node type and grounded to stable identifiers where possible. It is useful for TraitMech curation because it separates core conserved nodes from taxon-specific, condition-specific, or potentially ambiguous entities.*

---

# Candidate causal edges (evidence-backed)
The table below provides proposed subject–predicate–object triples with evidence snippets and notes for curation.

| Subject node (label + suggested CURIE) | Predicate | Object node (label + CURIE) | Evidence snippet (short quote) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| NADH (CHEBI:16908) | is oxidized by | Complex I / NDH-1 (EC:7.1.1.2) | “complex I… catalyzes the oxidation of NADH by ubiquinone” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | 10.3390/ijms252413421, 2024, https://doi.org/10.3390/ijms252413421 | General bacterial/prokaryotic claim; strong support for NDH-1 role. |
| NADH (CHEBI:16908) | is oxidized by | NDH-2 (EC:7.1.1.2 or label-only NDH-2) | “alternative NADH dehydrogenases (NDH-2)… catalyze the oxidation of NADH and the reduction of quinone” (uriberamirez2024modificationsofthe pages 1-2) | 10.1007/s10863-024-10041-y, 2024, https://doi.org/10.1007/s10863-024-10041-y | Taxon-specific example from *Bacillus licheniformis*; use as supported bacterial instance. |
| Succinate (CHEBI:30031) | is oxidized by | Succinate dehydrogenase / Complex II (EC:1.3.5.1) | “succinate dehydrogenase… catalyzes the two-electron reduction of quinone by succinate” (uriberamirez2024modificationsofthe pages 1-2) | 10.1007/s10863-024-10041-y, 2024, https://doi.org/10.1007/s10863-024-10041-y | Strong for succinate→SDH in bacteria. |
| Malate (CHEBI:30797) | donates electrons via | Malate:quinone oxidoreductase / Mqo (EC:1.1.5.4) | “the malate/quione oxidoreductase (Mqo)… transfer electrons to the menaquinone (MQ) pool” (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | 10.3390/antibiotics13121169, 2024, https://doi.org/10.3390/antibiotics13121169 | Supported in mycobacteria; likely not universal to all microbes, so curate as taxon-specific if used directly. |
| Complex I / NDH-1 (EC:7.1.1.2) | reduces | Ubiquinone / quinone pool (CHEBI:16389) | “oxidation of NADH by ubiquinone” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | 10.3390/ijms252413421, 2024, https://doi.org/10.3390/ijms252413421 | Strong; ubiquinone in review, quinone/menaquinone pool may vary by taxon. |
| NDH-2 (label-only NDH-2) | reduces | Quinone (CHEBI:36141) | “NDH-2… catalyze the oxidation of NADH and the reduction of quinone” (uriberamirez2024modificationsofthe pages 1-2) | 10.1007/s10863-024-10041-y, 2024, https://doi.org/10.1007/s10863-024-10041-y | Strong for *Bacillus*; no proton translocation. |
| Complex I / NDH-1 (EC:7.1.1.2) | translocates | Proton (CHEBI:15378) | “coupled with the vectorial transmembrane transfer of four H+ ions” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | 10.3390/ijms252413421, 2024, https://doi.org/10.3390/ijms252413421 | Strong, canonical edge for OXPHOS. |
| Proton translocation (GO:1902600) | generates | Proton motive force (GO:0015992) | “energy conservation in the form of an electrochemical gradient… (proton motive force, pmf)” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | 10.3390/ijms252413421, 2024, https://doi.org/10.3390/ijms252413421 | Strong mechanistic edge. |
| Quinol / menaquinol (CHEBI:17976 or label-only menaquinol) | donates electrons to | Cytochrome bcc/aa3 oxidase supercomplex (label-only; mycobacterial bcc/aa3) | “The cytochrome bcc/aa3 oxidase supercomplex… accept electrons from menaquinol” (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | 10.3390/antibiotics13121169, 2024, https://doi.org/10.3390/antibiotics13121169 | Mycobacterial/taxon-specific but mechanistically strong. |
| Quinol / menaquinol (CHEBI:17976 or label-only menaquinol) | donates electrons to | Cytochrome bd oxidase (EC:7.1.1.- or label-only cytochrome bd) | “The cytochrome bcc/aa3 oxidase supercomplex and the cytochrome bd oxidase accept electrons from menaquinol” (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | 10.3390/antibiotics13121169, 2024, https://doi.org/10.3390/antibiotics13121169 | Strong for mycobacteria and broadly consistent with bacterial bd biology. |
| Terminal oxidases (label-only) | reduce | Oxygen (CHEBI:15379) | “Terminal oxidases catalyze four-electron reduction of O2 to 2H2O” (nastasi2024membraneboundredoxenzyme pages 1-2) | 10.3390/ijms25021277, 2024, https://doi.org/10.3390/ijms25021277 | Strong general bacterial claim. |
| Heme-copper oxidase (GO:0015002 or label-only) | pumps | Proton (CHEBI:15378) | “Heme-copper oxidases are true proton pumps” (nastasi2024membraneboundredoxenzyme pages 1-2) | 10.3390/ijms25021277, 2024, https://doi.org/10.3390/ijms25021277 | Strong general claim. |
| Cytochrome bd oxidase (label-only) | contributes to | Proton motive force (GO:0015992) | “cytochromes bd generate proton-motive force solely due to the vector transfer of protons… without a mechanism of proton pumping” (nastasi2024membraneboundredoxenzyme pages 1-2) | 10.3390/ijms25021277, 2024, https://doi.org/10.3390/ijms25021277 | Strong; distinguish from proton pumping. |
| Proton motive force (GO:0015992) | drives | F-type ATP synthase / F1Fo-ATP synthase (GO:0042777) | “These protons are transported back… providing the necessary torque to induce ATP synthesis” (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | 10.3390/antibiotics13121169, 2024, https://doi.org/10.3390/antibiotics13121169 | Strong coupling edge. |
| F-type ATP synthase / F1Fo-ATP synthase (GO:0042777) | synthesizes | ATP (CHEBI:15422) | “couple proton transport with ATP synthesis from ADP + Pi” (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | 10.3390/antibiotics13121169, 2024, https://doi.org/10.3390/antibiotics13121169 | Core defining edge of the trait. |
| Hypoxia (ENVO:01000736) | favors use of | NDH-2 (label-only NDH-2) | “proton-translocating Ndh-1… during aerobic growth or non-proton contributing Ndh-2 during hypoxia” (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | 10.3390/antibiotics13121169, 2024, https://doi.org/10.3390/antibiotics13121169 | Strong but mycobacterial/taxon-specific branching edge. |
| Carbon monoxide (CHEBI:17245) | inhibits | Cytochrome bo3 oxidase (label-only cytochrome bo3) | “in cytochrome bo3, CO binds to heme o3^2+, preventing O2 binding and inhibiting activity” (nastasi2024membraneboundredoxenzyme media 5dea1c8d) | 10.3390/ijms25021277, 2024, https://doi.org/10.3390/ijms25021277 | Supported by figure interpretation; acceptable but based on schematic context. |
| Carbon monoxide (CHEBI:17245) | has minimal inhibition on | Cytochrome bd-I oxidase (label-only cytochrome bd-I) | “cytochrome bd-I is relatively CO-resistant because CO does not bind with high affinity” (nastasi2024membraneboundredoxenzyme media 5dea1c8d) | 10.3390/ijms25021277, 2024, https://doi.org/10.3390/ijms25021277 | Supported by figure interpretation; useful environmental modulation edge. |
| Cyanide (CHEBI:17514) | selects for / permits respiration via | Branched respiratory chain with alternative terminal oxidases (label-only) | “can also carry out aerobic respiration in the presence of this compound… indicating… a branched respiratory chain with various terminal oxidases” (uriberamirez2024modificationsofthe pages 1-2) | 10.1007/s10863-024-10041-y, 2024, https://doi.org/10.1007/s10863-024-10041-y | Environmental-response edge; organism-specific example. |
| Bedaquiline (CHEBI:67457) | inhibits | Mycobacterial F1Fo-ATP synthase (label-only) | “Bedaquiline… [is a] potent Mtb F1FO-ATP synthase inhibitor” (harikishore2024mycobacteriumtuberculosisfatp pages 1-2) | 10.3390/antibiotics13121169, 2024, https://doi.org/10.3390/antibiotics13121169 | Strong drug-target edge, specific to mycobacteria. |
| AD3-11 (label-only inhibitor) | inhibits | Cytochrome bd-I oxidase (label-only cytochrome bd-I) | “competitive quinone-site inhibitor (AD3-11) of bd-I” (henry2024drugrepurposingapproachesto pages 31-37) | 10.22024/unikent/01.02.107244, 2024, https://doi.org/10.22024/unikent/01.02.107244 | Uncertain/secondary source (thesis); useful candidate but should be curated cautiously. |
| Sodium azide (CHEBI:35318) | kills / suppresses persistence of | Bacterial persisters (label-only) | “inhibitors of bacterial respiratory chain such as sodium azide exhibited strong killing effects on bacterial antibiotic persisters” (wan2024protonmotiveforce pages 6-7) | 10.1111/1751-7915.70042, 2024, https://doi.org/10.1111/1751-7915.70042 | Indirect trait-application edge; not a universal OXPHOS mechanistic edge, but relevant for application graph. |


*Table: This table lists candidate causal graph edges for microbial oxidative phosphorylation (METPO:1000803), grounded where possible and supported only by the specified context IDs. It is useful for TraitMech curation because it separates core mechanistic edges from taxon-specific or more uncertain application-related edges.*

---

## Visual evidence (figures)
The following figure region(s) schematize CO inhibition and differential CO resistance of *E. coli* terminal oxidases (bo3, bd-II, bd-I), supporting environmental modulation edges involving carbon monoxide and terminal oxidase activity (nastasi2024membraneboundredoxenzyme media 5dea1c8d).

---

## DOI-first bibliography (with publication dates and URLs)

1. **Grivennikova VG, Gladyshev GV, Zharova TV, Borisov VB.** Proton-Translocating NADH–Ubiquinone Oxidoreductase: Interaction with Artificial Electron Acceptors, Inhibitors, and Potential Medicines. *Int. J. Mol. Sci.* **2024-12-14**. DOI: **10.3390/ijms252413421**. URL: https://doi.org/10.3390/ijms252413421 (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)

2. **Harikishore A, Grüber G.** Mycobacterium tuberculosis F-ATP Synthase Inhibitors and Targets. *Antibiotics* **2024-12-03**. DOI: **10.3390/antibiotics13121169**. URL: https://doi.org/10.3390/antibiotics13121169 (harikishore2024mycobacteriumtuberculosisfatp pages 1-2)

3. **Nastasi MR, Borisov VB, Forte E.** Membrane-Bound Redox Enzyme Cytochrome bd-I Promotes Carbon Monoxide-Resistant Escherichia coli Growth and Respiration. *Int. J. Mol. Sci.* **2024-01-20**. DOI: **10.3390/ijms25021277**. URL: https://doi.org/10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 1-2)

4. **Wan Y, Zheng J, Chan EWC, Chen S.** Proton motive force and antibiotic tolerance in bacteria. *Microbial Biotechnology* **2024-11**. DOI: **10.1111/1751-7915.70042**. URL: https://doi.org/10.1111/1751-7915.70042 (wan2024protonmotiveforce pages 6-7)

5. **Uribe-Ramírez D, Romero-Aguilar L, Vázquez-Meza H, Cristiani-Urbina E, Pardo JP.** Modifications of the respiratory chain of Bacillus licheniformis as an alkalophilic and cyanide-degrading microorganism. *Journal of Bioenergetics and Biomembranes* **2024-11-05**. DOI: **10.1007/s10863-024-10041-y**. URL: https://doi.org/10.1007/s10863-024-10041-y (uriberamirez2024modificationsofthe pages 1-2)

6. **Henry SA.** Drug-repurposing approaches to target bacterial respiratory complexes. **2024-01**. DOI: **10.22024/unikent/01.02.107244**. URL: https://doi.org/10.22024/unikent/01.02.107244 (henry2024drugrepurposingapproachesto pages 24-28)

---

## Warnings / claims to curate cautiously

1. **Taxon-specific wiring and terminology:** Some mechanistic wiring is explicitly described for mycobacteria (e.g., bcc/aa3 supercomplex; “intermembrane space” wording in a bacterial context) and should be curated with taxon qualifiers (NCBITaxon) or generalized carefully (harikishore2024mycobacteriumtuberculosisfatp pages 1-2).

2. **Thesis-derived inhibitor claims:** Candidate inhibitors (e.g., AD3-11 as a cytochrome bd-I inhibitor) are described in a 2024 thesis; these may be useful leads but should be treated as **uncertain** unless corroborated by peer-reviewed primary literature (henry2024drugrepurposingapproachesto pages 31-37).

3. **Anaerobic terminal reductases not evidenced here:** While anaerobic respiration is defined as using a non-oxygen terminal acceptor, specific anaerobic terminal reductase complexes and their coupling are not supported by the evidence retrieved in this run; avoid curating specific nitrate/fumarate/sulfate reductase edges without additional sources (henry2024drugrepurposingapproachesto pages 24-28).


References

1. (henry2024drugrepurposingapproachesto pages 24-28): Samantha Amoy Henry. Drug-repurposing approaches to target bacterial respiratory complexes. Text, Jan 2024. URL: https://doi.org/10.22024/unikent/01.02.107244, doi:10.22024/unikent/01.02.107244. This article has 0 citations and is from a peer-reviewed journal.

2. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 7 citations.

3. (nastasi2024membraneboundredoxenzyme pages 1-2): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

4. (uriberamirez2024modificationsofthe pages 1-2): Daniel Uribe-Ramírez, Lucero Romero-Aguilar, Héctor Vázquez-Meza, Eliseo Cristiani-Urbina, and Juan Pablo Pardo. Modifications of the respiratory chain of bacillus licheniformis as an alkalophilic and cyanide-degrading microorganism. Journal of Bioenergetics and Biomembranes, 56:591-605, Nov 2024. URL: https://doi.org/10.1007/s10863-024-10041-y, doi:10.1007/s10863-024-10041-y. This article has 1 citations and is from a peer-reviewed journal.

5. (harikishore2024mycobacteriumtuberculosisfatp pages 1-2): Amaravadhi Harikishore and Gerhard Grüber. Mycobacterium tuberculosis f-atp synthase inhibitors and targets. Dec 2024. URL: https://doi.org/10.3390/antibiotics13121169, doi:10.3390/antibiotics13121169. This article has 9 citations.

6. (nastasi2024membraneboundredoxenzyme media 5dea1c8d): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

7. (wan2024protonmotiveforce pages 6-7): Yingkun Wan, Jiaqi Zheng, Edward Wai‐Chi Chan, and Sheng Chen. Proton motive force and antibiotic tolerance in bacteria. Microbial Biotechnology, Nov 2024. URL: https://doi.org/10.1111/1751-7915.70042, doi:10.1111/1751-7915.70042. This article has 15 citations and is from a peer-reviewed journal.

8. (henry2024drugrepurposingapproachesto pages 31-37): Samantha Amoy Henry. Drug-repurposing approaches to target bacterial respiratory complexes. Text, Jan 2024. URL: https://doi.org/10.22024/unikent/01.02.107244, doi:10.22024/unikent/01.02.107244. This article has 0 citations and is from a peer-reviewed journal.