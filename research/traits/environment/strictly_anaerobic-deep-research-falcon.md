---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:28:42.943912'
end_time: '2026-06-18T01:53:34.753095'
duration_seconds: 1491.81
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: strictly anaerobic
  trait_identifier: METPO:1000611
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: strictly_anaerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An obligately anaerobic oxygen preference in which a microorganism\
    \ does not grow in the presence of oxygen gas (O\u2082)."
  parent_traits: METPO:1000607
  synonyms: strict obligate anaerobe
  evidence_summary: 'https://www.ncbi.nlm.nih.gov/books/NBK482349/: will not survive
    if there is more than half a percent oxygen (Supports strict anaerobiosis as a
    highly oxygen-sensitive subtype.) | PMID:39189748: Clostridioides difficile is
    a strict anaerobic, sporulating Firmicutes (Organism example: Clostridioides difficile
    is described as strictly anaerobic.)'
  causal_graph_summary: 'strict_anaerobe_oxygen_sensitivity: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** strictly anaerobic
- **METPO identifier:** METPO:1000611
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An obligately anaerobic oxygen preference in which a microorganism does not grow in the presence of oxygen gas (O₂).
- **Parent traits:** METPO:1000607
- **Synonyms:** strict obligate anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: will not survive if there is more than half a percent oxygen (Supports strict anaerobiosis as a highly oxygen-sensitive subtype.) | PMID:39189748: Clostridioides difficile is a strict anaerobic, sporulating Firmicutes (Organism example: Clostridioides difficile is described as strictly anaerobic.)
- **Existing causal graph summary:** strict_anaerobe_oxygen_sensitivity: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **strictly anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/strictly_anaerobic.yaml`.

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
- **Trait label:** strictly anaerobic
- **METPO identifier:** METPO:1000611
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An obligately anaerobic oxygen preference in which a microorganism does not grow in the presence of oxygen gas (O₂).
- **Parent traits:** METPO:1000607
- **Synonyms:** strict obligate anaerobe
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: will not survive if there is more than half a percent oxygen (Supports strict anaerobiosis as a highly oxygen-sensitive subtype.) | PMID:39189748: Clostridioides difficile is a strict anaerobic, sporulating Firmicutes (Organism example: Clostridioides difficile is described as strictly anaerobic.)
- **Existing causal graph summary:** strict_anaerobe_oxygen_sensitivity: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **strictly anaerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/strictly_anaerobic.yaml`.

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


## Microbial trait causal-graph curation report: **strictly anaerobic** (METPO:1000611)

### 0) Trait metadata (given)
**Trait label:** strictly anaerobic  
**METPO:** METPO:1000611  
**Definition (curation target):** obligately anaerobic oxygen preference where a microorganism does not grow in the presence of oxygen gas (O₂).  
**Synonyms:** strict obligate anaerobe.  

---

## 1) Scope summary (current understanding)

### 1.1 Phenotype represented
**Strictly anaerobic** refers to microorganisms whose vegetative growth is prevented by oxygen (O₂), because O₂ exposure triggers oxidative toxicity and/or inactivation of oxygen-labile catalytic systems essential for core metabolism. Mechanistically, O₂ is reduced at low-redox-potential centers, generating reactive oxygen species (ROS) that damage DNA and proteins, while O₂ and ROS also directly inactivate oxygen-sensitive metallocenters and radicals used by anaerobic enzymes (e.g., Fe–S cluster enzymes; glycyl radical enzymes). (rose2025commensalresilienceancient pages 7-9, rose2025commensalresilienceancient pages 9-11)

### 1.2 Boundary cases and distinctions from nearby traits
* **Strict anaerobe vs. facultative anaerobe:** Facultative anaerobes can grow with or without O₂; strict anaerobes cannot grow under O₂ even if they can sometimes transiently survive it. (rose2025commensalresilienceancient pages 9-11, zund2025decipheringoxidativestress pages 5-7)
* **Strict anaerobe vs. aerotolerant anaerobe:** Aerotolerant anaerobes may not use O₂ for respiration but can survive and/or recover after O₂ exposure via detoxification, scavenging, and repair systems. Notably, anammox bacteria are described as “previously classified as strict anaerobes” but show **reversible O₂ inhibition** in some genera, consistent with aerotolerance in an assay-defined sense. (okabe2023oxygentoleranceand pages 6-7)
* **Strict anaerobe vs. microaerophile:** Microaerophiles require O₂ at low tensions; the retrieved sources mostly operationalize “low O₂ tolerance” (IC50/DOmax; growth vs no growth) rather than using microaerophile as a formal category. In practice, a “strict anaerobe” can still show enzyme- or strain-specific tolerance to low O₂ ranges (e.g., ≤1–2% O₂) without being microaerophilic, because the phenotype is defined by *growth capability* in O₂, not merely survival. (caulat2024physiologicalroleand pages 1-2, zund2025decipheringoxidativestress pages 5-7)

### 1.3 Operationalization for curation (how the trait is observed)
Recent studies provide multiple quantifiable oxygen-sensitivity endpoints useful for TraitMech curation:
* **Growth/no-growth thresholds at defined O₂ tensions** (e.g., strain growth at 0.4%–1% O₂, survival after 48 h at 1% O₂). (caulat2024physiologicalroleand pages 2-5)
* **Inhibition kinetics for anaerobic activity:** IC50 and DOmax under controlled dissolved oxygen (DO). (okabe2023oxygentoleranceand media fd870038)
* **Cultivation-based oxygen transfer assays:** varying agar content to modulate O₂ transfer, recording which strains grow/arrest and whether they recover. (zund2025decipheringoxidativestress pages 5-7)

---

## 2) Key concepts and mechanistic definitions

### 2.1 Oxygen toxicity mechanisms relevant to strict anaerobiosis
Strict anaerobes are vulnerable because anaerobic metabolism frequently relies on oxygen-labile chemistry:
* O₂ and/or ROS can oxidize mononuclear iron enzymes and **solvent-exposed Fe–S clusters**, and inactivate **glycyl radical enzymes**, crippling essential pathways. (rose2025commensalresilienceancient pages 7-9)
* O₂ exposure causes ROS formation at reduced flavins and low-potential centers; ROS includes superoxide and hydrogen peroxide, with downstream damage via hydroxyl radicals (Fenton/Haber–Weiss chemistry). (rose2025commensalresilienceancient pages 7-9)

### 2.2 Oxygen/ROS defense systems that enable survival without aerobic growth
Even strict anaerobes encode “defense arsenals” that enable transient survival under oxygen stress:
* **Superoxide detoxification:** superoxide reductase (Sor) in many strict anaerobes; superoxide dismutase (SOD) in some more tolerant taxa. (lotoux2025defensearsenalof pages 1-2, okabe2023oxygentoleranceand pages 1-2)
* **Peroxide detoxification:** rubrerythrin (Rbr), peroxiredoxins (e.g., Bcp), catalase (in some taxa), and other peroxidases. (lotoux2025defensearsenalof pages 1-2, okabe2023oxygentoleranceand pages 1-2)
* **O₂ scavenging / reduction to water:** flavodiiron proteins (Fdp) and reverse rubrerythrins (revRbr) can reduce O₂ to H₂O (or contribute through peroxidase-like activity) and mitigate O₂ stress across defined O₂ windows. (caulat2024physiologicalroleand pages 1-2)

---

## 3) Recent developments and latest research (prioritizing 2023–2024)

### 3.1 Quantitative oxygen windows for O₂-reducing enzymes in *Clostridioides difficile* (2024)
A key 2024 mechanistic advance is the dissection of **multiple O₂-reducing enzymes with complementary O₂ ranges**, enabling a strict anaerobe to survive across physiological gradients:
* revRbr2: **<0.4% O₂**
* FdpA: **0.4–1% O₂**
* revRbr1: **0.1–4% O₂**
* FdpF: **>4% O₂ and air** (caulat2024physiologicalroleand pages 1-2)

The same work provides phenotype-linked genetics: multi-enzyme mutants fail to grow at **0.4% O₂** and show substantial survival defects at **1% O₂** over 24–48 h exposures. (caulat2024physiologicalroleand pages 2-5)

### 3.2 Oxygen-sensing and redox-sensing regulatory wiring (2024)
The 2024 study identifies an Spx-like regulator (OseR) as an O₂-responsive repressor/derepressor of O₂-reductase genes and clarifies sigma-factor logic:
* revrbr2 expression is under **dual σA/σB control**, with O₂ induction not exclusively σB-dependent. (caulat2024physiologicalroleand pages 9-11)
* OseR represses fdpA/fdpF/revRbr genes in anaerobiosis; O₂ exposure releases repression. (caulat2024physiologicalroleand pages 9-11)
* fdpF is regulated by **Rex**, linking O₂ defense to cellular NADH/NAD⁺ redox state. (caulat2024physiologicalroleand pages 1-2)

These are high-value causal graph edges because they connect environment (O₂) → regulators → enzyme systems → survival phenotype.

### 3.3 Quantitative oxygen inhibition kinetics in anammox bacteria (2023)
Okabe et al. quantified oxygen inhibition of anammox activity with IC50 and DOmax and connected tolerance to antioxidant enzyme activity profiles:
* Freshwater anammox: **IC50 2.7–4.2 µM DO; DOmax 10.9–26.6 µM**
* Marine *“Ca. Scalindua sp.”*: **IC50 18.0 µM DO; DOmax 51.6 µM** (okabe2023oxygentoleranceand pages 5-6)

The core quantitative results and recovery patterns are shown directly in figures (Figure 3 and Figure 5). (okabe2023oxygentoleranceand media fd870038)

### 3.4 Community/ecosystem evidence for “strict anaerobes under oxygen pulses” (2024)
Dyksma & Pester (2024) show that peatland sulfate-reducing bacteria—otherwise strictly anaerobic—can **grow and persist** under periodic oxic phases in a long-running bioreactor:
* Weekly O₂ exposures at **133 µM (50% air saturation)**
* Oxic (1 week) / anoxic (4 weeks) cycling over **>200 days**
* SRB reached up to **2.9% relative abundance**
* Metatranscriptomics implicates oxygen consumption genes, ROS detoxification genes, and protein repair/chaperone systems. (dyksma2024growthofsulfatereducing pages 1-2)

This is a key warning for trait curation: “strictly anaerobic” should not be equated with “cannot survive any oxygen,” but rather “cannot grow in oxygen,” with survival dependent on detox/repair programs and exposure regime.

---

## 4) Current applications and real-world implementations

### 4.1 Anammox wastewater treatment and marine nitrogen loss modeling
Anammox process performance depends on oxygen inhibition kinetics; Okabe et al. emphasize that a wide range of oxygen sensitivities complicates engineering design and ocean modeling. OMZs are defined as **≤5 µM O₂** and, despite being ~0.1% of ocean volume, contribute **20–40% of oceanic nitrogen loss** (context for why strict anaerobiosis and oxygen thresholds matter). (okabe2023oxygentoleranceand pages 1-2)

### 4.2 Gut oxygen gradients, infection biology, and pathogen persistence
Strict anaerobes in the gut inhabit oxygen-depleted niches; perturbations (e.g., inflammation) increase luminal oxygen and impose oxidative stress that reshapes communities and affects pathogen ecology. Oxygen gradients cited include ~0.4% O₂ in the lumen and higher oxygen near tissues; strict anaerobes must deploy detox systems to persist near these gradients. (rose2025commensalresilienceancient pages 7-9, lotoux2025defensearsenalof pages 1-2)

### 4.3 Anaerobic ecosystem function under fluctuating redox regimes (peatlands)
The 2024 peatland SRB bioreactor work provides a real-world analog for oxic-anoxic interfaces (tidal sediments, wetlands), showing that strictly anaerobic functional guilds can maintain energy metabolism gene expression and oxygen defense programs under repeated oxygen stress. (dyksma2024growthofsulfatereducing pages 5-6, dyksma2024growthofsulfatereducing pages 6-10)

### 4.4 Practical assay implementation for microbiome and anaerobe screening
Cultivation-based assays explicitly control oxygen transfer and oxidative exposures:
* O₂ stress: agar 0–0.15% to vary O₂ transfer
* H₂O₂ stress: 0–7.3 mM
* Exposure timelines: 24 h anaerobic pre-culture → 24 h stress → 24 h post-stress recovery
* Species-specific growth constraints: e.g., *Agathobacter rectalis* required ≥0.13% agar to grow; *Clostridium sporogenes* grew at 0.05% agar. (zund2025decipheringoxidativestress pages 5-7)

---

## 5) Candidate nodes grouped by type (with ontology grounding)

| Node label | Node type | Suggested ontology grounding | Notes |
|---|---|---|---|
| O2 | environmental factor | CHEBI:15379 | Primary inhibitory oxygen species for strict anaerobes (caulat2024physiologicalroleand pages 1-2, rose2025commensalresilienceancient pages 7-9) |
| dissolved oxygen (DO) | assay-metric | label-only | Operational oxygen exposure metric; used for IC50/DOmax (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand media fd870038) |
| superoxide | metabolite-chemical | CHEBI:18421 | ROS generated on O2 exposure; detoxified by Sor/Sod (lotoux2025defensearsenalof pages 1-2, rose2025commensalresilienceancient pages 7-9) |
| hydrogen peroxide | metabolite-chemical | CHEBI:16240 | ROS detoxified by Rbr/Bcp/catalase/peroxidases (lotoux2025defensearsenalof pages 8-10, lotoux2025defensearsenalof pages 1-2) |
| reactive oxygen species | metabolite-chemical | label-only | Includes superoxide and H2O2; major oxygen-linked stressors (lotoux2025defensearsenalof pages 1-2, rose2025commensalresilienceancient pages 7-9) |
| NADH | metabolite-chemical | CHEBI:57945 | Electron donor for O2/ROS detox systems; sensed by Rex (caulat2024physiologicalroleand pages 1-2, lotoux2025defensearsenalof pages 21-23) |
| NAD+ | metabolite-chemical | CHEBI:57540 | Redox partner in NADH/NAD+ ratio sensed by Rex (caulat2024physiologicalroleand pages 1-2) |
| NADH/NAD+ ratio | assay-metric | label-only | Redox state controlling Rex-regulated oxygen response (caulat2024physiologicalroleand pages 1-2) |
| FdpA | enzyme-protein | label-only | Flavodiiron protein; active mainly at 0.4%–1% O2 in C. difficile (caulat2024physiologicalroleand pages 1-2) |
| FdpF | enzyme-protein | label-only | Class F flavodiiron protein; active mainly at >4% O2 and air; NADH-dependent (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5) |
| revRbr1 | enzyme-protein | label-only | Reverse rubrerythrin; broad 0.1%–4% O2 protective role (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5) |
| revRbr2 | enzyme-protein | label-only | Reverse rubrerythrin; strongest role below 0.4% O2 (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5) |
| rubrerythrin (Rbr) | enzyme-protein | label-only | Major peroxidase for H2O2 detoxification and air/4% O2 survival (lotoux2025defensearsenalof pages 8-10, lotoux2025defensearsenalof pages 15-17) |
| peroxiredoxin Bcp | enzyme-protein | label-only | Central H2O2 detox enzyme; important for oxidative survival (lotoux2025defensearsenalof pages 8-10, lotoux2025defensearsenalof pages 1-2) |
| superoxide reductase Sor | enzyme-protein | label-only | Superoxide detox enzyme favored in anaerobes (lotoux2025defensearsenalof pages 8-10, rose2025commensalresilienceancient pages 9-11) |
| superoxide dismutase Sod | enzyme-protein | EC:1.15.1.1 | Canonical superoxide detox enzyme; linked to higher O2 tolerance in some taxa (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 8-9) |
| catalase Cat | enzyme-protein | EC:1.11.1.6 | H2O2 detox enzyme; contributes in some more aerotolerant anaerobes (okabe2023oxygentoleranceand pages 1-2, dyksma2024growthofsulfatereducing pages 1-2) |
| cytochrome bd oxidase CydAB | enzyme-protein | label-only | Oxygen-consuming terminal oxidase in oxygen-stressed SRB (dyksma2024growthofsulfatereducing pages 5-6, dyksma2024growthofsulfatereducing pages 6-10) |
| rubredoxin:oxygen oxidoreductase Roo/NorV | enzyme-protein | label-only | Oxygen reduction/consumption system implicated in anaerobe O2 defense (dyksma2024growthofsulfatereducing pages 5-6, dyksma2024growthofsulfatereducing pages 6-10) |
| thioredoxin TrxA | enzyme-protein | label-only | Reducing partner for peroxide defense/protein repair systems (dyksma2024growthofsulfatereducing pages 1-2, dyksma2024growthofsulfatereducing pages 6-10) |
| thioredoxin reductase TrxB | enzyme-protein | EC:1.8.1.9 | Regenerates thioredoxin for repair/detox cycles (dyksma2024growthofsulfatereducing pages 1-2) |
| methionine sulfoxide reductase MsrA/B | enzyme-protein | label-only | Repairs oxidized methionine residues after oxidative damage (dyksma2024growthofsulfatereducing pages 1-2, mcgregor2025fusobacteriumnucleatum pages 10-12) |
| PerR | regulator | label-only | Peroxide-sensing repressor controlling oxidative stress genes (lotoux2025defensearsenalof pages 1-2, lotoux2025defensearsenalof pages 8-10) |
| Rex | regulator | label-only | NADH/NAD+-responsive regulator controlling fdpF (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5) |
| sigmaB (σB) | regulator | label-only | General stress sigma factor controlling multiple O2-defense genes (lotoux2025defensearsenalof pages 1-2, caulat2024physiologicalroleand pages 9-11) |
| sigmaA (σA) | regulator | label-only | Contributes to revRbr2 transcription with σB (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 9-11) |
| OseR (Spx-like) | regulator | label-only | O2-responsive repressor/derepressor of fdp and revRbr genes (lotoux2025defensearsenalof pages 1-2, caulat2024physiologicalroleand pages 9-11) |
| OxyR | regulator | label-only | Redox-sensing regulator of broad oxidative defense in Bacteroides (rose2025commensalresilienceancient pages 9-11) |
| pyruvate formate-lyase (PFL) | enzyme-protein | label-only | Oxygen-sensitive glycyl radical enzyme in anaerobic metabolism (rose2025commensalresilienceancient pages 7-9, mcgregor2025fusobacteriumnucleatum pages 10-12) |
| PFL activating enzyme (PFL-AE) | enzyme-protein | label-only | [4Fe-4S]-dependent activating enzyme; highly O2 sensitive (mcgregor2025fusobacteriumnucleatum pages 10-12, bystrom2024couplingbutyrylcoenzymea pages 17-21) |
| glycyl radical enzymes | pathway-process | label-only | Enzyme class intrinsically incompatible with O2 (rose2025commensalresilienceancient pages 7-9, rose2025commensalresilienceancient pages 9-11) |
| pyruvate:ferredoxin oxidoreductase (PFOR) | enzyme-protein | label-only | Key low-potential anaerobic enzyme damaged or downregulated under O2 stress (rose2025commensalresilienceancient pages 7-9, xie2024bacteroidesthetaiotaomicronenhances pages 8-9) |
| iron-sulfur cluster enzymes | enzyme-protein | label-only | O2/ROS-sensitive redox enzymes central to anaerobic metabolism (rose2025commensalresilienceancient pages 7-9, bystrom2024couplingbutyrylcoenzymea pages 17-21) |
| Fenton reaction | pathway-process | label-only | Converts H2O2 and iron into highly damaging hydroxyl radicals (rose2025commensalresilienceancient pages 7-9, bystrom2024couplingbutyrylcoenzymea pages 17-21) |
| oxidative stress response | pathway-process | GO:0006979 | Global stress program induced by O2/ROS (lotoux2025defensearsenalof pages 1-2, dyksma2024growthofsulfatereducing pages 1-2) |
| oxidation-reduction process | pathway-process | GO:0055114 | Broad redox process underlying O2 reduction/detoxification (caulat2024physiologicalroleand pages 1-2, rose2025commensalresilienceancient pages 7-9) |
| oxygen reduction | pathway-process | GO:0015671 | O2 scavenging/detoxification activity in anaerobes (caulat2024physiologicalroleand pages 1-2, dyksma2024growthofsulfatereducing pages 5-6) |
| ROS detoxification | pathway-process | label-only | Enzymatic removal of superoxide/H2O2 (lotoux2025defensearsenalof pages 1-2, dyksma2024growthofsulfatereducing pages 1-2) |
| protein repair | pathway-process | label-only | Repair of oxidized proteins during oxygen stress (dyksma2024growthofsulfatereducing pages 1-2, dyksma2024growthofsulfatereducing pages 6-10) |
| GroEL/ES | enzyme-protein | label-only | Chaperone system upregulated in oxygen-stressed SRB (dyksma2024growthofsulfatereducing pages 1-2, dyksma2024growthofsulfatereducing pages 6-10) |
| DnaK/ClpB | enzyme-protein | label-only | Chaperone/disaggregase repair system under oxic stress (dyksma2024growthofsulfatereducing pages 1-2, dyksma2024growthofsulfatereducing pages 6-10) |
| IC50 for oxygen inhibition | assay-metric | label-only | 50% inhibitory O2 concentration for anaerobic activity (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand media fd870038) |
| DOmax | assay-metric | label-only | Upper dissolved-O2 limit permitting activity (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand media fd870038) |
| air exposure survival | assay-metric | label-only | Operational survival phenotype under 21% O2 exposure (lotoux2025defensearsenalof pages 8-10, okabe2023oxygentoleranceand pages 7-8) |
| growth/no-growth at low % O2 | assay-metric | label-only | Direct phenotypic assay for strict anaerobiosis boundaries (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 2-5) |


*Table: This table lists candidate nodes for a strictly anaerobic trait graph, spanning environmental inputs, oxygen/ROS detox enzymes, regulators, vulnerable anaerobic functions, and assay metrics. It is useful for converting the literature into grounded TraitMech graph entities with brief evidence-based notes.*

---

## 6) Candidate causal edges (curation table)

| Subject node | Predicate | Object node | Evidence snippet (verbatim or near-verbatim) | Reference (DOI, year, URL) | Notes/uncertainty | Suggested grounding for key nodes (CURIEs when available) |
|---|---|---|---|---|---|---|
| O2 | inhibits growth of | strictly anaerobic microorganism | "many Bacteroidetes, including B. thetaiotaomicron, are not able to grow in the presence of oxygen levels exceeding the micromolar range (>~0.5% O2)" (rose2025commensalresilienceancient pages 9-11) | 10.1128/IAI.00502-24, 2025, https://doi.org/10.1128/iai.00502-24 | Review-level ecological generalization; useful as trait boundary, not a single-gene mechanism | O2 = CHEBI:15379; strictly anaerobic = METPO:1000611 |
| O2 exposure | causes | reactive oxygen species formation | "Molecular O2 is rapidly reduced at low-redox-potential cellular centers, producing reactive oxygen species (ROS)" (rose2025commensalresilienceancient pages 9-11) | 10.1128/IAI.00502-24, 2025, https://doi.org/10.1128/iai.00502-24 | Broad mechanistic claim across anaerobes; appropriate upstream edge | O2 = CHEBI:15379; ROS = label-only |
| O2/ROS | oxidizes/inactivates | iron-sulfur cluster enzymes | "oxygen directly oxidizes mononuclear iron enzymes and solvent-exposed iron-sulfur clusters" (rose2025commensalresilienceancient pages 7-9) | 10.1128/IAI.00502-24, 2025, https://doi.org/10.1128/iai.00502-24 | General mechanism; node may remain label-only pending specific GO/EC mapping | O2 = CHEBI:15379; iron-sulfur cluster enzymes = label-only |
| O2 | inactivates | glycyl radical enzymes | "Certain enzyme classes (e.g., glycyl radical enzymes) are inherently incompatible with molecular oxygen" (rose2025commensalresilienceancient pages 9-11) | 10.1128/IAI.00502-24, 2025, https://doi.org/10.1128/iai.00502-24 | Strong mechanistic framing for strict anaerobiosis; broad across taxa | glycyl radical enzymes = label-only |
| O2/ROS | inactivates | PFOR/PFL and other low-potential enzymes | "key enzymes involved in energy metabolism in anaerobes such as pyruvate ferrodoxin oxidoreductase (PFOR), pyruvate formate lyase (PFL)... and proteins containing low potential iron-sulfur (Fe-S) clusters are known to be O2 sensitive" (okabe2023oxygentoleranceand pages 6-7) | 10.1038/s43705-023-00251-7, 2023, https://doi.org/10.1038/s43705-023-00251-7 | Mechanistic claim in anammox paper citing broader anaerobe biology; curate as general but literature-synthesized | PFOR = label-only; PFL = label-only |
| Sor | protects against | superoxide donor menadione | "Sor has a superoxide reductase activity in vitro and protects the bacterium from exposure to menadione, a superoxide donor" (lotoux2025defensearsenalof pages 1-2) | 10.1128/mbio.03753-24, 2025, https://doi.org/10.1128/mbio.03753-24 | Strong C. difficile-specific edge; menadione is assay-linked proxy for superoxide stress | Sor = label-only; menadione = CHEBI:41045 |
| Rbr | detoxifies | hydrogen peroxide | "rubrerythrin, Rbr... together with the peroxiredoxin, Bcp, plays a central role in the detoxification of H2O2" (lotoux2025defensearsenalof pages 1-2) | 10.1128/mbio.03753-24, 2025, https://doi.org/10.1128/mbio.03753-24 | Strong enzyme-to-process edge in C. difficile | Rbr = label-only; H2O2 = CHEBI:16240 |
| Bcp | detoxifies | hydrogen peroxide | "the peroxiredoxin, Bcp, plays a central role in the detoxification of H2O2" (lotoux2025defensearsenalof pages 1-2) | 10.1128/mbio.03753-24, 2025, https://doi.org/10.1128/mbio.03753-24 | Strong enzyme-to-process edge in C. difficile | Bcp = label-only; H2O2 = CHEBI:16240 |
| Rbr and Bcp | promotes survival in | air or 4% O2 | "Rbr... together with the peroxiredoxin, Bcp... promotes the survival of C. difficile in the presence of not only H2O2 but also air or 4% O2" (lotoux2025defensearsenalof pages 1-2) | 10.1128/mbio.03753-24, 2025, https://doi.org/10.1128/mbio.03753-24 | Joint edge; could be split into two edges if curator prefers finer granularity | air = label-only; 4% O2 = label-only |
| RevRbr2 | protects at | low O2 tensions (<0.4%) | "revRbr2 is specific to low O2 tensions (<0.4%)" (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24, 2024, https://doi.org/10.1128/mbio.01591-24 | C. difficile-specific O2 window; highly curatable quantitative edge | revRbr2 = label-only; O2 = CHEBI:15379 |
| FdpA | protects at | 0.4%–1% O2 | "FdpA [is specific] to low and intermediate O2 tensions (0.4%–1%)" (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24, 2024, https://doi.org/10.1128/mbio.01591-24 | Quantitative, strain-specific but strong | FdpA = label-only; O2 = CHEBI:15379 |
| revRbr1 | protects at | 0.1%–4% O2 | "revRbr1 has a wider spectrum of activity (0.1%–4%)" (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24, 2024, https://doi.org/10.1128/mbio.01591-24 | Quantitative spectrum in C. difficile | revRbr1 = label-only; O2 = CHEBI:15379 |
| FdpF | protects at | >4% O2 and air | "FdpF is more specific to tensions > 4% and air" (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24, 2024, https://doi.org/10.1128/mbio.01591-24 | Strong quantitative edge; useful for modeling high-end oxygen defense | FdpF = label-only; O2 = CHEBI:15379 |
| OseR | represses in anaerobiosis | fdpA/fdpF/revRbr1/revRbr2 expression | "In anaerobiosis, we observed a derepression of fdpA, fdpF, revrbr1, and revrbr2 genes in the ΔoseR mutant... OseR most likely acts as a repressor of these genes in anaerobiosis" (caulat2024physiologicalroleand pages 9-11) | 10.1128/mbio.01591-24, 2024, https://doi.org/10.1128/mbio.01591-24 | Clean regulator edge; taxon-specific to C. difficile | OseR = label-only |
| O2 exposure | relieves repression by | OseR | "whereas O2 exposure releases the repression" (caulat2024physiologicalroleand pages 9-11) | 10.1128/mbio.01591-24, 2024, https://doi.org/10.1128/mbio.01591-24 | Useful conditional regulatory edge; wording inferred from same passage | O2 = CHEBI:15379; OseR = label-only |
| σB | positively regulates | revrbr1/fdpA/fdpF expression | "the expression of the revrbr1, fdpA, and fdpF genes decreased in the sigB::erm compared to the WT strain" (caulat2024physiologicalroleand pages 9-11) | 10.1128/mbio.01591-24, 2024, https://doi.org/10.1128/mbio.01591-24 | Multi-target regulatory edge in C. difficile | sigmaB = label-only |
| σA and σB | jointly regulate | revrbr2 expression | "the regulation of the revrbr2 gene is more complex, as the gene is expressed under the dual control of σA and σB" (caulat2024physiologicalroleand pages 9-11) | 10.1128/mbio.01591-24, 2024, https://doi.org/10.1128/mbio.01591-24 | Strong transcriptional regulation edge | sigmaA = label-only; sigmaB = label-only |
| Rex | regulates | fdpF | "fdpF is regulated by Rex, a regulator sensing the NADH/NAD+ ratio" (caulat2024physiologicalroleand pages 1-2) | 10.1128/mbio.01591-24, 2024, https://doi.org/10.1128/mbio.01591-24 | Strong regulator edge; redox-sensing mechanism explicit | Rex = label-only; NADH = CHEBI:57945; NAD+ = CHEBI:57540 |
| PerR | regulates | rbr-sor-CD0828 oxidative stress operon | "The CD0828 gene... forms an operon with rbr, sor, and perR encoding a H2O2-sensing repressor" (lotoux2025defensearsenalof pages 1-2) | 10.1128/mbio.03753-24, 2025, https://doi.org/10.1128/mbio.03753-24 | Supports PerR-centered oxidative regulation; exact promoter logic may need full-text curation | PerR = label-only; rbr = label-only; sor = label-only |
| high SOD activity | associated with higher | oxygen tolerance (higher IC50/DOmax) | "only Scalindua exhibited high Sod activity of 22.6 ± 1.9 U/mg-protein... This Sod-Cat dependent detoxification system could be responsible for the higher O2 tolerance of Scalindua" (okabe2023oxygentoleranceand pages 1-2, okabe2023oxygentoleranceand pages 8-9) | 10.1038/s43705-023-00251-7, 2023, https://doi.org/10.1038/s43705-023-00251-7 | Association across anammox taxa rather than direct gene knockout; mark as comparative/inferred | SOD = EC:1.15.1.1 |
| periodic 133 µM O2 stress | induces transcription of | oxygen consumption/ROS detoxification/protein repair genes | "weekly oxygen exposures at 133 µM (50% air saturation)... most transcribed genes in three functional categories... (1) oxygen consumption... (2) reactive oxygen species (ROS) detoxification... and (3) repair and chaperone systems" (dyksma2024growthofsulfatereducing pages 1-2, dyksma2024growthofsulfatereducing pages 6-10) | 10.1186/s40168-024-01909-7, 2024, https://doi.org/10.1186/s40168-024-01909-7 | Community/metatranscriptomic edge in SRB bioreactor; broad but operationally relevant | O2 = CHEBI:15379; oxidative stress response = GO:0006979 |
| 50% air saturation O2 / 133 µM O2 | permits growth of | sulfate-reducing bacteria populations | "SRB... established growing populations (up to 2.9% relative abundance) despite weekly periods of oxygen exposures at 133 µM (50% air saturation)" (dyksma2024growthofsulfatereducing pages 1-2) | 10.1186/s40168-024-01909-7, 2024, https://doi.org/10.1186/s40168-024-01909-7 | Important boundary-case warning: strictly anaerobic taxa can persist under intermittent oxic pulses via defense programs | O2 = CHEBI:15379; sulfate-reducing bacteria = label-only |


*Table: This table lists candidate subject-predicate-object edges for curating the strictly anaerobic trait graph, with near-verbatim evidence, recent references, and grounding suggestions. It emphasizes oxygen toxicity mechanisms, detoxification systems, regulatory control, and quantitative oxygen thresholds.*

---

## 7) Key quantitative statistics (recent studies)

### 7.1 Oxygen thresholds and inhibition kinetics
* **C. difficile O₂ defense windows:** revRbr2 (<0.4%), FdpA (0.4–1%), revRbr1 (0.1–4%), FdpF (>4% and air). (caulat2024physiologicalroleand pages 1-2)
* **Anammox DO inhibition kinetics:** freshwater IC50 2.7–4.2 µM and DOmax 10.9–26.6 µM; marine *Scalindua* IC50 18.0 µM and DOmax 51.6 µM. (okabe2023oxygentoleranceand pages 5-6, okabe2023oxygentoleranceand media fd870038)
* **Anammox recovery after O₂ exposure:** evidence for reversible inhibition in some taxa after 12 h exposure up to ambient air. (okabe2023oxygentoleranceand pages 6-7)

### 7.2 Oxygen stress in complex environments
* **Peatland SRB oxygen pulse magnitude:** 133 µM O₂ (50% air saturation), weekly, with sustained SRB populations over >200 days. (dyksma2024growthofsulfatereducing pages 1-2)

### 7.3 Detox enzyme activity linked to tolerance (comparative)
* *Scalindua* SOD activity **22.6 ± 1.9 U/mg-protein** and catalase **1.6 ± 0.7 U/mg-protein**; proposed to underpin higher O₂ tolerance relative to taxa lacking measurable SOD activity. (okabe2023oxygentoleranceand pages 1-2)

---

## 8) Expert opinions / authoritative analysis (from sources)

* The gut resilience review frames strict anaerobiosis as a consequence of “anaerobic excellence,” i.e., reliance on low-redox, oxygen-labile chemistry (Fe–S, radicals) that is incompatible with sustained O₂ exposure, explaining why rising luminal O₂ during inflammation filters out obligate anaerobes. (rose2025commensalresilienceancient pages 7-9)
* The anammox study concludes that oxygen tolerance must be quantified using standardized inhibition kinetics (IC50/DOmax) because reported tolerances vary widely; biomass form (aggregates vs planktonic) and cell density can alter apparent oxygen tolerance, warning against naïve trait assignments from non-standard assays. (okabe2023oxygentoleranceand pages 6-7, okabe2023oxygentoleranceand pages 2-3)

---

## 9) Warnings for TraitMech curation (do not curate yet / curate as uncertain)

1. **Do not equate “strict anaerobe” with “dies instantly in oxygen.”** Several strict anaerobes survive transient exposures using detoxification and repair systems; phenotype depends on exposure regime (duration, O₂ tension, growth phase). Curate survival-related edges as conditional/assay-specific. (dyksma2024growthofsulfatereducing pages 1-2, zund2025decipheringoxidativestress pages 5-7)
2. **Association vs causation:** Some oxygen-tolerance conclusions are comparative (e.g., SOD/CAT activity vs IC50/DOmax across anammox taxa) rather than genetic perturbations; these edges should be marked *inferred/associative* unless supported by direct intervention. (okabe2023oxygentoleranceand pages 1-2)
3. **Taxon specificity:** The detailed O₂ windows (revRbr/Fdp) and regulatory network (OseR, Rex, σA/σB) are strongly supported for *C. difficile* but should be curated as organism-conditional unless conserved ortholog evidence is added. (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 9-11)

---

## 10) DOI-first bibliography (with dates/URLs)

1. **Caulat LC, et al.** *Physiological role and complex regulation of O2-reducing enzymes in the obligate anaerobe Clostridioides difficile.* **mBio**. **Oct 2024**. DOI: **10.1128/mbio.01591-24**. URL: https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 1-2, caulat2024physiologicalroleand pages 9-11)
2. **Okabe S, et al.** *Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria.* **ISME Communications**. **May 2023**. DOI: **10.1038/s43705-023-00251-7**. URL: https://doi.org/10.1038/s43705-023-00251-7 (okabe2023oxygentoleranceand pages 5-6, okabe2023oxygentoleranceand media fd870038)
3. **Dyksma S, Pester M.** *Growth of sulfate-reducing Desulfobacterota and Bacillota at periodic oxygen stress of 50% air-O2 saturation.* **Microbiome**. **Oct 2024**. DOI: **10.1186/s40168-024-01909-7**. URL: https://doi.org/10.1186/s40168-024-01909-7 (dyksma2024growthofsulfatereducing pages 1-2)
4. **Rose AE, Fansler RT, Zhu W.** *Commensal resilience: ancient ecological lessons for the modern microbiota.* **Infection and Immunity**. **Jun 2025**. DOI: **10.1128/iai.00502-24**. URL: https://doi.org/10.1128/iai.00502-24 (rose2025commensalresilienceancient pages 7-9)
5. **Lotoux A, et al.** *Defense arsenal of the strict anaerobe Clostridioides difficile against reactive oxygen species encountered during its infection cycle.* **mBio**. **Apr 2025**. DOI: **10.1128/mbio.03753-24**. URL: https://doi.org/10.1128/mbio.03753-24 (lotoux2025defensearsenalof pages 1-2, lotoux2025defensearsenalof pages 8-10)
6. **Zünd JN, et al.** *Deciphering oxidative stress responses in human gut microbes and fecal microbiota: a cultivation-based approach.* **FEMS Microbiology Ecology**. **May 2025**. DOI: **10.1093/femsec/fiaf054**. URL: https://doi.org/10.1093/femsec/fiaf054 (zund2025decipheringoxidativestress pages 5-7)
7. **Xie S, Ma J, Lu Z.** *Bacteroides thetaiotaomicron enhances oxidative stress tolerance through rhamnose-dependent mechanisms.* **Frontiers in Microbiology**. **Dec 2024**. DOI: **10.3389/fmicb.2024.1505218**. URL: https://doi.org/10.3389/fmicb.2024.1505218 (xie2024bacteroidesthetaiotaomicronenhances pages 8-9)

---

## 11) Curation-ready takeaways (for `strictly_anaerobic.yaml`)

* Represent strict anaerobiosis as an emergent property from (a) oxygen toxicity mechanisms (ROS generation; inactivation of Fe–S and radical enzymes) and (b) protective systems that permit survival but do not confer aerobic growth. (rose2025commensalresilienceancient pages 7-9, rose2025commensalresilienceancient pages 9-11)
* Encode oxygen tension as a quantitative environmental node; model O₂ windows for specific detox/scavenging modules when evidence exists (e.g., *C. difficile* revRbr/Fdp windows; anammox IC50/DOmax). (caulat2024physiologicalroleand pages 1-2, okabe2023oxygentoleranceand media fd870038)
* Explicitly flag assay/condition dependence (air vs 1% vs 0.4% O₂; dissolved oxygen µM; exposure time; biomass aggregation). (okabe2023oxygentoleranceand pages 2-3, caulat2024physiologicalroleand pages 2-5)


References

1. (rose2025commensalresilienceancient pages 7-9): Abigail E. Rose, Ryan T. Fansler, and Wenhan Zhu. Commensal resilience: ancient ecological lessons for the modern microbiota. Jun 2025. URL: https://doi.org/10.1128/iai.00502-24, doi:10.1128/iai.00502-24. This article has 9 citations and is from a peer-reviewed journal.

2. (rose2025commensalresilienceancient pages 9-11): Abigail E. Rose, Ryan T. Fansler, and Wenhan Zhu. Commensal resilience: ancient ecological lessons for the modern microbiota. Jun 2025. URL: https://doi.org/10.1128/iai.00502-24, doi:10.1128/iai.00502-24. This article has 9 citations and is from a peer-reviewed journal.

3. (zund2025decipheringoxidativestress pages 5-7): Janina N Zünd, Marina Caflisch, Denisa Mujezinovic, Serafina Plüss, Christophe Lacroix, and Benoit Pugin. Deciphering oxidative stress responses in human gut microbes and fecal microbiota: a cultivation-based approach. FEMS Microbiology Ecology, May 2025. URL: https://doi.org/10.1093/femsec/fiaf054, doi:10.1093/femsec/fiaf054. This article has 13 citations and is from a peer-reviewed journal.

4. (okabe2023oxygentoleranceand pages 6-7): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

5. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

6. (caulat2024physiologicalroleand pages 2-5): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

7. (okabe2023oxygentoleranceand media fd870038): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

8. (lotoux2025defensearsenalof pages 1-2): Aurélie Lotoux, Léo Caulat, Catarina Martins Alves, Carolina Alves Feliciano, Claire Morvan, Filipe Folgosa, and Isabelle Martin-Verstraete. Defense arsenal of the strict anaerobe <i>clostridioides difficile</i> against reactive oxygen species encountered during its infection cycle. Apr 2025. URL: https://doi.org/10.1128/mbio.03753-24, doi:10.1128/mbio.03753-24. This article has 5 citations and is from a domain leading peer-reviewed journal.

9. (okabe2023oxygentoleranceand pages 1-2): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

10. (caulat2024physiologicalroleand pages 9-11): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (okabe2023oxygentoleranceand pages 5-6): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

12. (dyksma2024growthofsulfatereducing pages 1-2): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 49 citations and is from a highest quality peer-reviewed journal.

13. (dyksma2024growthofsulfatereducing pages 5-6): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 49 citations and is from a highest quality peer-reviewed journal.

14. (dyksma2024growthofsulfatereducing pages 6-10): Stefan Dyksma and Michael Pester. Growth of sulfate-reducing desulfobacterota and bacillota at periodic oxygen stress of 50% air-o2 saturation. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01909-7, doi:10.1186/s40168-024-01909-7. This article has 49 citations and is from a highest quality peer-reviewed journal.

15. (lotoux2025defensearsenalof pages 8-10): Aurélie Lotoux, Léo Caulat, Catarina Martins Alves, Carolina Alves Feliciano, Claire Morvan, Filipe Folgosa, and Isabelle Martin-Verstraete. Defense arsenal of the strict anaerobe <i>clostridioides difficile</i> against reactive oxygen species encountered during its infection cycle. Apr 2025. URL: https://doi.org/10.1128/mbio.03753-24, doi:10.1128/mbio.03753-24. This article has 5 citations and is from a domain leading peer-reviewed journal.

16. (lotoux2025defensearsenalof pages 21-23): Aurélie Lotoux, Léo Caulat, Catarina Martins Alves, Carolina Alves Feliciano, Claire Morvan, Filipe Folgosa, and Isabelle Martin-Verstraete. Defense arsenal of the strict anaerobe <i>clostridioides difficile</i> against reactive oxygen species encountered during its infection cycle. Apr 2025. URL: https://doi.org/10.1128/mbio.03753-24, doi:10.1128/mbio.03753-24. This article has 5 citations and is from a domain leading peer-reviewed journal.

17. (lotoux2025defensearsenalof pages 15-17): Aurélie Lotoux, Léo Caulat, Catarina Martins Alves, Carolina Alves Feliciano, Claire Morvan, Filipe Folgosa, and Isabelle Martin-Verstraete. Defense arsenal of the strict anaerobe <i>clostridioides difficile</i> against reactive oxygen species encountered during its infection cycle. Apr 2025. URL: https://doi.org/10.1128/mbio.03753-24, doi:10.1128/mbio.03753-24. This article has 5 citations and is from a domain leading peer-reviewed journal.

18. (okabe2023oxygentoleranceand pages 8-9): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

19. (mcgregor2025fusobacteriumnucleatum pages 10-12): Alexandra K. McGregor and Kirsten R. Wolthers. <i>fusobacterium nucleatum</i> : strategies for adapting to aerobic stress. Journal of Bacteriology, Jul 2025. URL: https://doi.org/10.1128/jb.00090-25, doi:10.1128/jb.00090-25. This article has 7 citations and is from a peer-reviewed journal.

20. (bystrom2024couplingbutyrylcoenzymea pages 17-21): Liam Bystrom. Coupling butyryl-coenzyme a oxidation to oxygen reduction in fusobacterium nucleatum. Text, Jan 2024. URL: https://doi.org/10.14288/1.0447284, doi:10.14288/1.0447284. This article has 0 citations and is from a peer-reviewed journal.

21. (xie2024bacteroidesthetaiotaomicronenhances pages 8-9): Shuo Xie, Junze Ma, and Zheng Lu. Bacteroides thetaiotaomicron enhances oxidative stress tolerance through rhamnose-dependent mechanisms. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1505218, doi:10.3389/fmicb.2024.1505218. This article has 21 citations and is from a peer-reviewed journal.

22. (okabe2023oxygentoleranceand pages 7-8): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.

23. (okabe2023oxygentoleranceand pages 2-3): Satoshi Okabe, Shaoyu Ye, Xi Lan, Keishi Nukada, Haozhe Zhang, Kanae Kobayashi, and Mamoru Oshiki. Oxygen tolerance and detoxification mechanisms of highly enriched planktonic anaerobic ammonium-oxidizing (anammox) bacteria. ISME Communications, May 2023. URL: https://doi.org/10.1038/s43705-023-00251-7, doi:10.1038/s43705-023-00251-7. This article has 68 citations and is from a peer-reviewed journal.