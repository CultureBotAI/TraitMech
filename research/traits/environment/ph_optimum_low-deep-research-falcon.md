---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:29:02.038175'
end_time: '2026-06-18T00:50:05.126694'
duration_seconds: 1263.09
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH optimum low
  trait_identifier: METPO:1000455
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_optimum_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH optimum phenotype with the best-growth external pH at or below
    approximately 6, corresponding to acidophilic or extreme-acidophilic physiology.
  parent_traits: METPO:1000331
  synonyms: Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile,
    Obligative acidophile, pHO_0_to_6
  evidence_summary: 'DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis
    review supports growth at acidic external pH as the acidophilic / extreme-acidophilic
    category.)'
  causal_graph_summary: 'ph_optimum_low_acidophile_setpoint: 4 nodes, 3 edges'
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
- **Trait label:** pH optimum low
- **METPO identifier:** METPO:1000455
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH at or below approximately 6, corresponding to acidophilic or extreme-acidophilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHO_0_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth at acidic external pH as the acidophilic / extreme-acidophilic category.)
- **Existing causal graph summary:** ph_optimum_low_acidophile_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **pH optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_low.yaml`.

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
- **Trait label:** pH optimum low
- **METPO identifier:** METPO:1000455
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH at or below approximately 6, corresponding to acidophilic or extreme-acidophilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHO_0_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth at acidic external pH as the acidophilic / extreme-acidophilic category.)
- **Existing causal graph summary:** ph_optimum_low_acidophile_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **pH optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_low.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **pH optimum low** (METPO:1000455)

### 0) Scope summary (curation-focused)
The trait **pH optimum low** denotes microorganisms whose **optimal growth** occurs at **acidic external pH**, operationally corresponding to acidophilic physiology (often **optimum pH <5**) and including **extreme acidophiles** (**optimum pH ≤3**; many grow at **pH 1–3**) (dopson2023eurypsychrophilicacidophilesfrom pages 1-2, gonzalez2024acidophilicheterotrophsbasic pages 1-2, krulwich2011molecularaspectsof pages 3-5). A key physiological hallmark is that many extreme acidophiles maintain **near-circumneutral cytoplasmic pH (~6)** while growing at **external pH <3**, necessitating strong pH homeostasis mechanisms (krulwich2011molecularaspectsof pages 11-12, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4).

**Boundary cases / nearby traits:**
- **Acid tolerance / acid resistance / acid acclimation** can occur in neutralophiles (e.g., gastric bacteria) and may support survival or growth under episodic acid challenge without implying a low pH optimum (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 14-15). This is important for curation: the METPO trait is about **growth optimum** (and typically sustained growth), not merely **survival after acid shock**.
- Definitions vary by subfield: some reviews define acidophiles as capable of growth at **pH ≤5** (e.g., “acidophilic methanotrophs”), while others emphasize **optimum pH** thresholds (hwangbo2023acidophilicmethanotrophsoccurrence pages 1-2, dopson2023eurypsychrophilicacidophilesfrom pages 1-2).

### 1) Key concepts & current understanding (mechanistic themes)
Across bacteria and archaea, acidophily is explained by a small number of recurring mechanistic strategies:
1. **Electrochemical strategy:** extreme acidophiles tolerate a large outward-to-inward **ΔpH** by maintaining a **reversed/inside-positive membrane potential (Δψ)**, which electrostatically inhibits proton influx (krulwich2011molecularaspectsof pages 11-12, dopson2023eurypsychrophilicacidophilesfrom pages 2-4). A schematic and PMF framing are captured in Krulwich et al. (Box/Figure) (krulwich2011molecularaspectsof media ec1f0edf, krulwich2011molecularaspectsof media d8ab9528).
2. **Lower proton permeability barriers:** membranes and envelope features are modified to reduce passive proton leak (e.g., specialized porins; lipid composition remodeling) (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4).
3. **Active proton export and ion exchange:** proton pumps (ATPases and respiratory-chain complexes) and secondary transporters (Na+/H+ antiporters) remove or offset cytoplasmic protons (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 17-18).
4. **Cytoplasmic buffering and proton-consuming metabolism:** amino-acid decarboxylation systems (e.g., Gad) and urease-linked buffering consume protons and/or generate neutralizing species (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 11-12).
5. **Proteostasis/repair under acid stress:** acid stress drives upregulation of repair/turnover and proteostasis modules in some models, consistent with macromolecular damage at low pH (chiu2023membranelipidand pages 15-16).

### 2) Recent developments (prioritizing 2023–2024)
**Archaeal membrane biophysics and tetraether lipid mechanisms (2024):**
- A detailed 2024 synthesis links **archaeal tetraether membranes (GDGT/GDNT)** and their modifications (cyclopentane ring content, tetraether:diether ratios, polar headgroup glycosylation) to **very low passive proton permeability**, supporting maintenance of **intracellular pH ~5.4–6.5** in thermoacidophiles (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 1-2, chong2024archaeamembranesin pages 4-6).
- Quantitatively, PLFE tetraether liposomes exhibit **passive proton permeabilities ~0.3–0.5 × 10−8 cm s−1**, much lower than diester bilayers, consistent with a physical barrier mechanism for acidophily (chong2024archaeamembranesin pages 2-3).

**Linking lipid remodeling and gene expression under acid stress (2023):**
- In *Saccharolobus islandicus* (thermoacidophilic archaeon), acid stress experiments (control **pH 3.4** vs acid stress **pH 2.4**, both at 76°C) show: (i) impaired growth (doubling time increased), (ii) strong transcriptome shifts under acid stress, and (iii) coordinated changes in ATPase and lipid-related genes (chiu2023membranelipidand pages 2-3, chiu2023membranelipidand pages 5-6).
- Notably, **A-type ATPase subunits** are upregulated under acidic conditions (interpreted as ATP-fueled proton pumping), while **GDGT cyclization decreased** despite stress-associated changes in **grsB** expression—highlighting that transcriptional signals can fail to predict lipid outcomes (chiu2023membranelipidand pages 9-10, chiu2023membranelipidand pages 6-7, chiu2023membranelipidand pages 15-16).

**Acid mine drainage (AMD) and low-pH biotechnologies (2024):**
- Acidophilic sulfate-reducing bacteria reviews emphasize proton impermeability/Donnan potential and metal immobilization via sulfide precipitation as core applied functions at low pH (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2).
- A 2024 FEMS Microbiology Reviews synthesis documents low-pH industrial fermentation advances and performance gains at pH ~3 (e.g., >135 g/L lactic acid at pH 3 in an industrial strain), showing how low pH can be exploited for process economics and contamination control (atasoy2024exploitationofmicrobial pages 10-11).

### 3) Current applications and real-world implementations (examples + data)
**A) AMD treatment / metal recovery via sulfidogenesis**
Acidophilic sulfate reducers produce **biogenic sulfide** that **precipitates metals as metal sulfides**, and generate **bicarbonate** that can locally raise pH—mechanisms central to AMD remediation and resource recovery (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2). Reported AMD-related conditions include environmental pH values as low as ~2.6–3.3 and application-relevant enrichment/bioreactor settings around pH 2.5–3.5 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2).

**B) Biomining / bioleaching and low-pH redox transformations**
A 2024 review of acidophilic heterotrophs notes >80 heterotrophic acidophiles isolated and highlights iron redox cycling at low pH as enabling biomining/bioleaching; low pH reduces contamination risk in fermentation-like processes (gonzalez2024acidophilicheterotrophsbasic pages 1-2). The same review provides quantitative context: below ~pH 2.5 Fe(III) is highly available, oxygen solubility is ~2.56×10−4 mol/L, and Fe(III) redox potential at pH 2 is E°′ ~0.77 V (gonzalez2024acidophilicheterotrophsbasic pages 2-3).

**C) Low-pH fermentation (industrial biotechnology)**
Operating fermentations at low pH can reduce neutralization and downstream salt formation; a 2024 review reports an industrial strain producing **>135 g/L lactic acid at pH 3** with **~90% free lactic acid**, and adaptive strategies yielding **95% yield** at pH 3.6 in *Lactobacillus pentosus* (atasoy2024exploitationofmicrobial pages 10-11). These outcomes operationalize the “low pH reduces contamination and improves recovery” concept highlighted for acidophiles in biotechnology reviews (gonzalez2024acidophilicheterotrophsbasic pages 1-2).

### 4) Expert synthesis / authoritative analysis
A consistent expert-level conclusion across foundational and modern sources is that **acidophily is not one mechanism** but a **systems-level trade-off** between: (i) preventing proton influx (membrane barrier, reversed Δψ), (ii) exporting/neutralizing protons (ATPases, respiratory proton pumps, antiporters, decarboxylation/urease), and (iii) repairing acid damage (proteostasis/repair). Foundational synthesis emphasizes PMF component rebalancing and constitutive expression costs in extremophiles (krulwich2011molecularaspectsof pages 3-5), while 2023–2024 studies add quantitative membrane biophysics (proton permeability) and integrated multi-omics showing that organisms may prioritize ATP-dependent pumping/repair over lipid cyclization under stress (chong2024archaeamembranesin pages 2-3, chiu2023membranelipidand pages 15-16).

### 5) Candidate nodes grouped by type (for `ph_optimum_low.yaml`)
| Node label | Node type | Role in acidophily (1-line) | Evidence/source (DOI year) | Suggested CURIE grounding |
|---|---|---|---|---|
| low external pH | environmental factor | Primary environmental condition selecting for growth optima at acidic pH and driving homeostatic adaptations. (gonzalez2024acidophilicheterotrophsbasic pages 1-2, dopson2023eurypsychrophilicacidophilesfrom pages 1-2, krulwich2011molecularaspectsof pages 3-5) | 10.3389/fmicb.2024.1374800 (2024); 10.3389/fmicb.2023.1149903 (2023); 10.1038/nrmicro2549 (2011) | CHEBI:10014 (hydron) / label-only for acidic environment |
| transmembrane ΔpH | process | Large outside-acidic to inside-near-neutral pH gradient is a defining energetic challenge of extreme acidophily. (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof media ec1f0edf) | 10.1038/nrmicro2549 (2011) | GO:0035777 (candidate, proton motive force-driven ATP synthesis-related gradient term not exact); label-only recommended |
| reversed membrane potential (inside-positive Δψ) | process | Electrostatic barrier that opposes proton influx and helps maintain cytoplasmic pH. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof media ec1f0edf) | 10.3389/fmicb.2023.1149903 (2023); 10.1038/nrmicro2549 (2011) | label-only |
| cytoplasmic pH ~6 | process | Typical internal pH maintained by many extreme acidophiles despite external pH below 3. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, krulwich2011molecularaspectsof pages 11-12) | 10.1111/1758-2229.70019 (2024); 10.1038/nrmicro2549 (2011) | label-only |
| Kdp K+ uptake system (kdpABC/kdpABCDE/kdpDEABC) | gene/protein/complex | Imports K+ to help build the inside-positive membrane potential used to repel protons. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom pages 2-4) | 10.3389/fmicb.2023.1149903 (2023) | label-only |
| NhaA Na+/H+ antiporter | gene/protein/complex | Secondary cation/proton antiporter supporting pH homeostasis by coupling Na+ and H+ fluxes. (krulwich2011molecularaspectsof pages 17-18, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.1038/nrmicro2549 (2011); 10.3389/fmicb.2023.1149903 (2023) | label-only |
| P-type ATPase proton efflux pump | gene/protein/complex | ATP-driven proton export system proposed to reduce cytoplasmic proton load in acidophiles. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903 (2023) | label-only |
| A-type ATPase | gene/protein/complex | In thermoacidophilic archaea, acid-stress-upregulated ATPase proposed to function in proton pumping. (chiu2023membranelipidand pages 15-16, chiu2023membranelipidand pages 9-10) | 10.3389/fmicb.2023.1219779 (2023) | label-only |
| respiratory complex I membrane arm | gene/protein/complex | Proton-exporting NADH:ubiquinone oxidoreductase subunits contribute to acid adaptation in vent chemolithotrophs. (deng2023strategiesofchemolithoautotrophs pages 1-2) | 10.1186/s40168-023-01712-w (2023) | GO:0005747 (mitochondrial term not ideal for microbes); label-only recommended |
| Omp40 porin | gene/protein/complex | Outer membrane protein associated with reduced proton permeability in acidophilic bacteria. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | 10.3389/fmicb.2023.1149903 (2023); 10.1111/1758-2229.70019 (2024) | label-only |
| PspA | gene/protein/complex | Envelope stress/membrane-protective protein implicated in lowering proton permeability. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | 10.1111/1758-2229.70019 (2024) | label-only |
| cyclopropane fatty acids / cfa | metabolite/chemical | Cyclopropanated membrane lipids reduce H+ permeability and support acid survival. (krulwich2011molecularaspectsof pages 17-18, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.1038/nrmicro2549 (2011); 10.3389/fmicb.2023.1149903 (2023) | label-only |
| cyclopropane-fatty-acyl-phospholipid synthase (cfa) | gene/protein/complex | Enzyme producing cyclopropane fatty acids linked to acid-resistant membrane remodeling. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903 (2023) | label-only |
| hopanoids | metabolite/chemical | Membrane-stiffening lipids associated with proton-impermeable bacterial membranes in acidic habitats. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | 10.3389/fmicb.2023.1149903 (2023); 10.1111/1758-2229.70019 (2024) | label-only |
| hpn/shc hopanoid biosynthesis genes | gene/protein/complex | Genetic basis for hopanoid/squalene-derived membrane reinforcement in acidophiles. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903 (2023) | EC:5.4.99.17 for squalene-hopene cyclase (shc); others label-only |
| GDGT | metabolite/chemical | Archaeal tetraether lipid whose cyclization and abundance modulate membrane packing and proton permeability. (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 1-2, chiu2023membranelipidand pages 1-2) | 10.3389/frbis.2023.1338019 (2024); 10.3389/fmicb.2023.1219779 (2023) | label-only |
| GDNT | metabolite/chemical | Calditol-containing tetraether lipid expected to better tolerate acidic stress via stronger H-bonding. (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 4-6) | 10.3389/frbis.2023.1338019 (2024) | label-only |
| tetraether-rich archaeal membrane | cellular structure | Monolayer-like archaeal membrane with unusually low passive proton permeability. (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 7-7) | 10.3389/frbis.2023.1338019 (2024) | GO:0016020 (membrane), label-only for tetraether membrane |
| GrsA/GrsB GDGT ring synthases | gene/protein/complex | Radical SAM enzymes controlling GDGT cyclopentane ring insertion and membrane cyclization state. (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 2-3) | 10.3389/fmicb.2023.1219779 (2023) | label-only |
| lipid glycosylation / polar headgroup glycosylation | process | Adds OH-rich headgroups that strengthen membrane-surface H-bonding and a proton-shelter effect. (chong2024archaeamembranesin pages 1-2, chong2024archaeamembranesin pages 4-6) | 10.3389/frbis.2023.1338019 (2024) | GO:0070085 (glycosylation) |
| GadB glutamate decarboxylase | gene/protein/complex | Consumes cytoplasmic protons during glutamate decarboxylation, a classic acid-buffering mechanism. (krulwich2011molecularaspectsof pages 15-17, krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 (2011) | EC:4.1.1.15 |
| GadC glutamate/GABA antiporter | gene/protein/complex | Couples substrate/product exchange to the glutamate decarboxylase proton-consuming system. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof media d8ab9528) | 10.1038/nrmicro2549 (2011) | label-only |
| arginine decarboxylase (adi/speA) | gene/protein/complex | Proton-consuming amino-acid decarboxylation route contributing to cytoplasmic buffering. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903 (2023) | EC:4.1.1.19 |
| urease | gene/protein/complex | Generates ammonia/ammonium buffering capacity that mitigates low-pH stress. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, krulwich2011molecularaspectsof pages 11-12) | 10.3389/fmicb.2023.1149903 (2023); 10.1038/nrmicro2549 (2011) | EC:3.5.1.5 |
| UreI | gene/protein/complex | pH-gated urea channel enabling rapid urease-dependent buffering under acidic conditions. (krulwich2011molecularaspectsof pages 11-12) | 10.1038/nrmicro2549 (2011) | label-only |
| carbonic anhydrase (HP1186) | gene/protein/complex | Acid-acclimation enzyme in H. pylori, helping manage CO2/bicarbonate chemistry under low pH. (krulwich2011molecularaspectsof pages 17-18) | 10.1038/nrmicro2549 (2011) | EC:4.2.1.1 |
| ClpXP / Clp protease system | gene/protein/complex | Proteostasis machinery recurrently enriched in acidophiles to manage protein damage under acid stress. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903 (2023) | GO:0097057 (ClpXP complex, candidate) |
| sulfate reduction | pathway/module | Central low-pH anaerobic metabolism producing sulfide and enabling AMD remediation. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 20-21) | 10.1111/1758-2229.70019 (2024) | GO:0019419 |
| sulfide precipitation / metal sulfide biomineralization | process | Converts dissolved metals into insoluble metal sulfides during acidophilic sulfate reduction. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 20-21) | 10.1111/1758-2229.70019 (2024) | label-only |
| acid mine drainage (AMD) | environmental factor | Canonical extremely acidic, metal-rich habitat where acidophiles are abundant and exploited in remediation. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2, watkin2024editorialacidophilemicrobiology pages 1-2) | 10.1111/1758-2229.70019 (2024); 10.3389/fmicb.2024.1454559 (2024) | ENVO candidate; label-only recommended |
| bioreactor operation at pH ~5 | environmental factor | Real-world low-pH process condition supporting acidophile-based metal and sulfate removal. (atasoy2024exploitationofmicrobial pages 10-11) | 10.1093/femsre/fuad062 (2024) | label-only |


*Table: This table lists candidate mechanistic and environmental nodes for curating a TraitMech graph for low pH optimum. It groups key factors, processes, proteins, lipids, and application contexts with brief roles, evidence, and tentative ontology grounding.*

### 6) Candidate causal edges (triples) with evidence snippets and curation notes
| Edge (triple) | Mechanistic rationale | Evidence snippet (short quote) | Source (DOI, year) | Notes/uncertainty | Suggested ontology grounding |
|---|---|---|---|---|---|
| low external pH → drives → large transmembrane ΔpH | Acidophiles growing in acidic media must counter a steep outside-to-inside proton gradient. | “cytoplasmic pH ~6.0 while growing at external pH <3” (krulwich2011molecularaspectsof pages 11-12) | 10.1038/nrmicro2549, 2011 | Broad physiological edge; suitable as environmental input to graph. | low external pH: CHEBI:10014; transmembrane pH gradient: GO:0035777 (candidate); acid mine drainage environment label-only/ENVO candidate |
| inside-positive membrane potential (reversed Δψ) → counteracts → proton influx | Positive-inside Δψ electrostatically opposes proton entry and is a hallmark of extreme acidophiles. | “sustain a large ΔpH with a reversed inside-positive membrane potential” (krulwich2011molecularaspectsof pages 11-12); “inside positive membrane potential… create an electrochemical barrier to proton influx” (dopson2023eurypsychrophilicacidophilesfrom pages 2-4) | 10.1038/nrmicro2549, 2011; 10.3389/fmicb.2023.1149903, 2023 | Strong trait-level mechanism; not a single gene product. | membrane potential label-only; proton influx label-only; plasma membrane GO:0005886 |
| K+ uptake systems (kdpABC/kdpABCDE/kdpDEABC) → contributes_to → inside-positive Δψ | Accumulation of cations helps generate the reversed membrane potential used by acidophiles. | “kdpABC/ kdpABCDE / kdpDEABC… contribute to an inverted (inside positive) membrane potential” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903, 2023 | Mostly comparative-genomic/review synthesis; may be taxon-dependent. | KdpABC potassium-transporting ATPase: KEGG module/gene label-only; potassium ion CHEBI:29103 |
| Na+/H+ antiporter NhaA → exports/antiports → H+ relative to Na+ | Secondary cation/proton antiport helps remove excess cytoplasmic protons and maintain pH homeostasis. | “Na+/H+ antiporters (nhaA…)” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9); “E. coli NhaA = 2H+/1Na+” (krulwich2011molecularaspectsof pages 5-6) | 10.3389/fmicb.2023.1149903, 2023; 10.1038/nrmicro2549, 2011 | Strong for acid stress/homeostasis generally; direct evidence in extreme acidophiles is mixed. Mark as generalizable, not universal. | nhaA label-only; antiporter activity GO:0015297 (candidate); sodium CHEBI:29101; proton CHEBI:15378 |
| P-type ATPase proton efflux pump → decreases → cytoplasmic proton load | ATP-dependent proton export is one route to preserve near-neutral cytoplasmic pH at low external pH. | “P-type ATPase proton efflux pumps” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903, 2023 | Review-based association; gene family may differ among taxa. | P-type ATPase proton pump label-only; proton transmembrane transport GO:1902600 (candidate) |
| A-type ATPase upregulation → supports → proton pumping under acid stress | In thermoacidophilic archaea, A-type ATPase is proposed to run in proton-export mode during acid stress. | “upregulated an A-type ATPase, proposed to function as a proton pump” (chiu2023membranelipidand pages 15-16); “upregulation of six of eight A-type ATPase subunits” (chiu2023membranelipidand pages 9-10) | 10.3389/fmicb.2023.1219779, 2023 | Strong but taxon-specific to Saccharolobus islandicus experiment. | A-type ATPase label-only; ATPase activity GO:0016887; proton transmembrane transport GO:1902600 |
| proton-pumping respiratory complexes → removes → protons from cytoplasm | Respiratory proton pumps can actively extrude protons and contribute to low-pH homeostasis. | “proton pumps (Complexes I, III, and IV) remove protons” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9); “increased expression of proton-pumping respiratory chain complexes” (krulwich2011molecularaspectsof pages 5-6) | 10.3389/fmicb.2022.1034164, 2023 review context; 10.1038/nrmicro2549, 2011 | Broad mechanism; specific complexes vary by lineage. | respiratory chain complex I GO:0005747/EC:7.1.1.2 candidate; proton transport GO:0015992 |
| rigid proton-impermeable membrane → decreases → passive proton permeability | Reduced passive proton leak lowers energetic burden of pH homeostasis. | “rigid and impermeable membrane that is highly resistant to the influx of protons” (dopson2023eurypsychrophilicacidophilesfrom pages 2-4) | 10.3389/fmicb.2023.1149903, 2023 | Good high-level edge for trait graph. | membrane lipid organization GO:0061024; passive proton permeability label-only |
| cyclopropane-fatty-acyl-phospholipid synthase (cfa) → promotes → membrane proton impermeability | Cyclopropane fatty acids are associated with reduced H+ permeability in acidic conditions. | “cyclopropane-fatty-acyl-phospholipid synthase (cfa)” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9); “cyclopropane fatty acids reduce membrane H+ permeability” (krulwich2011molecularaspectsof pages 17-18) | 10.3389/fmicb.2023.1149903, 2023; 10.1038/nrmicro2549, 2011 | Stronger in bacteria than archaea; may fit moderate acidophiles better. | cfa label-only; cyclopropane fatty acid biosynthetic process label-only |
| hopanoid biosynthesis genes (hpnAIJKNHM, shc) → strengthens → membrane barrier to protons | Hopanoids/squalene-derived lipids stiffen membranes and are recurrently linked to acidophile adaptation. | “hopanoid and squalene-related synthesis genes (‘hpnAIJKNHM;’, ‘shc’)” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903, 2023 | Comparative-genomic support; causal direction inferred from review synthesis. | hopanoid biosynthesis label-only; squalene-hopene cyclase EC:5.4.99.17 |
| Omp40 outer membrane porin → reduces → proton permeability | Specialized outer membrane proteins are proposed to limit proton entry in acidophilic bacteria. | “specific porin adaptation cited is the ‘Omp40 porin protein in At. ferrooxidans’” (dopson2023eurypsychrophilicacidophilesfrom pages 2-4); “Omp40 and PspA reduce proton permeability” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | 10.3389/fmicb.2023.1149903, 2023; 10.1111/1758-2229.70019, 2024 | Likely taxon-specific; curate with Acidithiobacillus context. | Omp40 label-only; outer membrane GO:0019867 |
| PspA → contributes_to → proton impermeability/stress protection | Envelope stress proteins may stabilize membrane integrity at low pH. | “specific membrane proteins Omp40 and PspA that reduce proton permeability” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | 10.1111/1758-2229.70019, 2024 | Review statement; direct molecular experiments may be limited. | PspA label-only; stress response GO:0006950 |
| GDGT/GDNT-rich tetraether membrane → decreases → passive proton permeability | Archaeal tetraether monolayers form tightly packed, low-leak membranes suited to thermoacidophily. | “very low passive proton permeabilities ((0.3–0.5) x10−8 cm s−1)” and “maintenance of near-neutral intracellular pH (typically 5.4–6.5)” (chong2024archaeamembranesin pages 2-3) | 10.3389/frbis.2023.1338019, 2024 | Strong mechanistic evidence, especially for archaea and liposome systems. | GDGT label-only/CHEBI candidate; GDNT label-only; membrane organization GO:0061024 |
| increased cyclopentane ring cyclization in GDGTs → increases → membrane packing/rigidity | More ring cyclization condenses archaeal membranes and is linked to lower proton permeability. | “increased cyclopentane ring content condenses membranes” (chong2024archaeamembranesin pages 3-4); “increasing cyclopentane ring numbers makes GDGTs pack more tightly” (chiu2023membranelipidand pages 1-2) | 10.3389/frbis.2023.1338019, 2024; 10.3389/fmicb.2023.1219779, 2023 | Strong for archaeal membranes; the direction of stress response can vary experimentally. | GDGT cyclization label-only; grsA/grsB label-only |
| GDNT relative to GDGT → enhances → acid tolerance/proton barrier | Calditol-containing GDNT headgroups allow additional H-bonding and improved acid tolerance. | “GDNT differs from GDGT by carrying a calditol moiety with five free hydroxyls… membranes with GDNT are expected to better tolerate acidic stress” (chong2024archaeamembranesin pages 4-6) | 10.3389/frbis.2023.1338019, 2024 | Mechanistically plausible and well argued, but some statements are expectation/inference. | GDNT label-only; calditol label-only |
| polar headgroup glycosylation → strengthens → proton shelter at membrane surface | OH-rich headgroups can form H-bond networks that raise local surface pH and impede proton penetration. | “Additional sugar moieties add OH groups… strengthening hydrogen-bond networks and providing a ‘proton shelter’” (chong2024archaeamembranesin pages 4-6) | 10.3389/frbis.2023.1338019, 2024 | Strong biophysical model, partly supported by biomimetic systems. | glycosylation GO:0070085; carbohydrate moiety label-only |
| grsB (GDGT ring synthase) activity/expression → modulates → GDGT cyclization state | GDGT cyclization is enzymatically controlled by Grs proteins and linked to membrane adaptation. | “grsB, the GDGT ring synthase, is differentially expressed under both acid and cold stress” (chiu2023membranelipidand pages 1-2) | 10.3389/fmicb.2023.1219779, 2023 | Important node, but expression did not straightforwardly predict lipid outcome. | grsB label-only; radical SAM enzyme activity GO candidate |
| acid stress in S. islandicus → upregulates → proton pumping and repair pathways | Acid stress responses include energy-intensive proton export and molecular repair rather than only membrane cyclization. | “acid-specific responses including upregulation of genes related to proton pumping and molecular turnover” (chiu2023membranelipidand pages 1-2); “repair/degradation pathways” (chiu2023membranelipidand pages 15-16) | 10.3389/fmicb.2023.1219779, 2023 | Strong experimental edge, but phenotype is stress response in one archaeon. | proton transport GO:0015992; DNA repair GO:0006281; protein catabolic process GO:0030163 |
| glutamate decarboxylase system (GadB/GadABC + GadC) → consumes → cytoplasmic protons | Amino-acid decarboxylation is a classic proton-consuming acid-resistance/homeostasis mechanism. | “glutamate decarboxylase (GadB) consume[s] a proton to make GABA” (krulwich2011molecularaspectsof pages 5-6); “gadABC/gadB” in acidophiles (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.1038/nrmicro2549, 2011; 10.3389/fmicb.2023.1149903, 2023 | Common in acid tolerance; presence in acidophiles may be lineage-specific. | glutamate decarboxylase EC:4.1.1.15; GABA CHEBI:16865; glutamate CHEBI:29985 |
| arginine decarboxylase (adi/speA) → consumes → cytoplasmic protons | Decarboxylation of amino acids helps buffer low cytoplasmic pH. | “arginine decarboxylase (adi, speA)” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903, 2023 | Review-based; useful as optional node for broader acidophily graph. | arginine decarboxylase EC:4.1.1.19; arginine CHEBI:29016 |
| urease system (ureABCDEFGHJ) → produces → NH3/NH4+ buffering capacity | Urease-derived ammonia neutralizes acidity and is a canonical acid-acclimation mechanism. | “ureABCDEFGHJ urease system” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9); “export of CO2, NH3 and NH4+… buffers the periplasm” (krulwich2011molecularaspectsof pages 11-12) | 10.3389/fmicb.2023.1149903, 2023; 10.1038/nrmicro2549, 2011 | Strong for H. pylori and some acidophiles; not universal acidophile mechanism. | urease EC:3.5.1.5; ammonia CHEBI:16134; ammonium CHEBI:28938; urea CHEBI:16199 |
| UreI-mediated urease recruitment → enables → periplasmic buffering at low pH | Channel-assisted urease localization allows immediate access to urea and rapid buffering. | “recruitment of urease to the inner membrane via the UreI channel” and “membrane-bound urease activity increases two-fold at pH 4.5 relative to pH 7.4” (krulwich2011molecularaspectsof pages 11-12) | 10.1038/nrmicro2549, 2011 | Strong but assay- and taxon-specific to H. pylori; probably not a core acidophile trait node. | UreI label-only; periplasm label-only/GO:0042597 |
| alpha-carbonic anhydrase (HP1186) → supports → acid acclimation | Carbonic anhydrase participates in periplasm/cytoplasm buffering and is regulated by low pH. | “HP1186 alpha-carbonic anhydrase… essential for acid acclimation” (krulwich2011molecularaspectsof pages 17-18) | 10.1038/nrmicro2549, 2011 | Strong for H. pylori acid acclimation; taxon-specific. | carbonic anhydrase EC:4.2.1.1 |
| Clp proteases (clpXP/clpPXB) → protects → proteostasis under acid conditions | Low pH damages proteins; robust chaperone/protease systems are recurrent in acidophiles. | “Clp proteases (‘clpXPB Clp protease;’)” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903, 2023 | Genomic enrichment/review support rather than direct phenotype assays. | ClpXP complex GO:0097057 (candidate); proteolysis GO:0006508 |
| Campylobacterales proton-export genes/K+ accumulation genes → enables → adaptation to pH 2.2 vent conditions | Metagenomic evidence links proton export and K+ accumulation functions to active low-pH chemolithoautotrophs. | “genes encoding proteins involved in proton export… K+ accumulation… play essential roles in enabling Campylobacterales to adapt to extremely acidic conditions” (deng2023strategiesofchemolithoautotrophs pages 1-2) | 10.1186/s40168-023-01712-w, 2023 | Strong ecological experiment, but lineage-specific and community/metagenome based. | NADH:ubiquinone oxidoreductase membrane arm label-only; potassium transport label-only |
| sulfate reduction → produces → biogenic sulfide | aSRB respiration yields sulfide, which is central to low-pH bioremediation and metal capture. | “perform dissimilatory sulphate reduction… produce biogenic sulphide” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | 10.1111/1758-2229.70019, 2024 | Application-oriented but mechanistically clear. | sulfate reduction GO:0019419; sulfide CHEBI:16134? better CHEBI:18498 hydrogen sulfide |
| biogenic sulfide → precipitates → dissolved metals as metal sulfides | Sulfide production directly immobilizes metals, making acidophiles useful in AMD treatment. | “immobilizes metals via sulphide precipitation” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2); “metal sulphide nanoparticles recovered after AMD treatment” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | 10.1111/1758-2229.70019, 2024 | Strong application edge; useful for environment/application branch of graph. | metal sulfide label-only; biomineralization GO:0110148 (candidate) |
| acidic bioreactor operation (~pH 5) with acidophilic communities → achieves → high metal/sulfate removal | Real-world low-pH bioreactors validate functional importance of acidophilic communities in remediation. | “bioreactors operated at pH ~5 achieved dissolved metal removals >99% (except Mn), sulfate removal >75%, and iron removal >85%” (atasoy2024exploitationofmicrobial pages 10-11) | 10.1093/femsre/fuad062, 2024 | Implementation edge, not direct cell-mechanism edge; best kept as application evidence. | bioreactor label-only; acid mine drainage ENVO candidate; sulfate CHEBI:16189; iron CHEBI:18248 |
| low pH fermentation environment → reduces → contamination risk | Low-pH growth confers process robustness, a practical consequence of the trait. | “chances of contamination are reduced by the low pH” (gonzalez2024acidophilicheterotrophsbasic pages 1-2) | 10.3389/fmicb.2024.1374800, 2024 | Application edge; not a molecular mechanism of the trait itself. | low pH environment CHEBI:10014; fermentation GO:0006113 (broad candidate) |


*Table: This table compiles candidate subject–predicate–object edges for curating a TraitMech graph for the microbial trait 'pH optimum low'. It emphasizes source-backed mechanisms, quantitative snippets where available, and flags taxon-specific or application-oriented claims for cautious curation.*

### 7) Visual evidence available (figures/boxes)
Krulwich et al. includes a Box/Figure that schematizes the **PMF framing (ΔpH vs Δψ)** and **acid-challenge mechanisms** (proton-consuming reactions, antiporters, membrane adaptations, proton pumps) that are relevant to acidophily graphs (krulwich2011molecularaspectsof media ec1f0edf, krulwich2011molecularaspectsof media d8ab9528).

### 8) Warnings / curation flags (do-not-curate-yet or mark uncertain)
1. **Do not conflate acidophily with acid resistance/acclimation**: *Helicobacter pylori* urease/UreI and carbonic anhydrase exemplify acid acclimation in a gastric niche; these edges are mechanistically strong but taxon- and niche-specific and may not represent core “acidophile growth optimum” mechanisms (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 17-18).
2. **Review/inference-based edges**: Some gene-to-phenotype edges in comparative reviews (e.g., Kdp → inside-positive Δψ; hopanoids → proton impermeability) are plausible but often not demonstrated as necessary/sufficient in multiple taxa; mark as **candidate/uncertain** unless supported by direct perturbation data (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4).
3. **Transcription ≠ phenotype for archaeal lipids**: In *S. islandicus*, acid stress upregulated ATPase subunits and altered expression of cyclization genes, yet GDGT cyclization decreased, implying post-transcriptional regulation or energetic constraints; avoid curation that assumes monotonic “grsB up → cyclization up → acid tolerance up” (chiu2023membranelipidand pages 6-7, chiu2023membranelipidand pages 9-10).
4. **Trait definition heterogeneity across communities**: pH thresholds differ by domain (e.g., “growth at pH ≤5” vs “optimum pH <5”); in curation, keep a strict link to **optimum external pH ≤6 (ideally with measured growth curve)** (hwangbo2023acidophilicmethanotrophsoccurrence pages 1-2, dopson2023eurypsychrophilicacidophilesfrom pages 1-2).

---

## DOI-first bibliography (with URLs and publication dates)
1. Krulwich TA, Sachs G, Padan E. *Molecular aspects of bacterial pH sensing and homeostasis.* **Nature Reviews Microbiology** (May 2011). DOI: **10.1038/nrmicro2549**. URL: https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 5-6)
2. Dopson M, González-Rosales C, Holmes DS, Mykytczuk N. *Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies.* **Frontiers in Microbiology** (Mar 2023). DOI: **10.3389/fmicb.2023.1149903**. URL: https://doi.org/10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 1-2)
3. Valdez-Nuñez LF, Kappler A, Ayala-Muñoz D, et al. *Acidophilic sulphate‐reducing bacteria: Diversity, ecophysiology, and applications.* **Environmental Microbiology Reports** (Oct 2024). DOI: **10.1111/1758-2229.70019**. URL: https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2)
4. Chong PL-G. *Archaea membranes in response to extreme acidic environments.* **Frontiers in Biophysics** (Jan 2024). DOI: **10.3389/frbis.2023.1338019**. URL: https://doi.org/10.3389/frbis.2023.1338019 (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 1-2, chong2024archaeamembranesin pages 4-6)
5. Chiu BK, Waldbauer J, Elling FJ, et al. *Membrane lipid and expression responses of Saccharolobus islandicus REY15A to acid and cold stress.* **Frontiers in Microbiology** (Aug 2023). DOI: **10.3389/fmicb.2023.1219779**. URL: https://doi.org/10.3389/fmicb.2023.1219779 (chiu2023membranelipidand pages 6-7, chiu2023membranelipidand pages 9-10, chiu2023membranelipidand pages 2-3)
6. Deng W, Zhao Z, Li Y, et al. *Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem.* **Microbiome** (Dec 2023). DOI: **10.1186/s40168-023-01712-w**. URL: https://doi.org/10.1186/s40168-023-01712-w (deng2023strategiesofchemolithoautotrophs pages 1-2)
7. Atasoy M, Álvarez Ordóñez A, Cenian A, et al. *Exploitation of microbial activities at low pH to enhance planetary health.* **FEMS Microbiology Reviews** (Nov 2024). DOI: **10.1093/femsre/fuad062**. URL: https://doi.org/10.1093/femsre/fuad062 (atasoy2024exploitationofmicrobial pages 10-11)
8. González E, Vera F, Scott F, et al. *Acidophilic heterotrophs: basic aspects and technological applications.* **Frontiers in Microbiology** (May 2024). DOI: **10.3389/fmicb.2024.1374800**. URL: https://doi.org/10.3389/fmicb.2024.1374800 (gonzalez2024acidophilicheterotrophsbasic pages 1-2, gonzalez2024acidophilicheterotrophsbasic pages 2-3)
9. Hwangbo M, Shao Y, Hatzinger PB, Chu K-H. *Acidophilic methanotrophs: Occurrence, diversity, and possible bioremediation applications.* **Environmental Microbiology Reports** (Apr 2023). DOI: **10.1111/1758-2229.13156**. URL: https://doi.org/10.1111/1758-2229.13156 (hwangbo2023acidophilicmethanotrophsoccurrence pages 1-2)



References

1. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

2. (gonzalez2024acidophilicheterotrophsbasic pages 1-2): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 7 citations and is from a peer-reviewed journal.

3. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 11-12): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

5. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 14-15): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

7. (hwangbo2023acidophilicmethanotrophsoccurrence pages 1-2): Myung Hwangbo, Yiru Shao, Paul B. Hatzinger, and Kung‐Hui Chu. Acidophilic methanotrophs: occurrence, diversity, and possible bioremediation applications. Environmental Microbiology Reports, 15:265-281, Apr 2023. URL: https://doi.org/10.1111/1758-2229.13156, doi:10.1111/1758-2229.13156. This article has 17 citations and is from a peer-reviewed journal.

8. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

9. (krulwich2011molecularaspectsof media ec1f0edf): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

10. (krulwich2011molecularaspectsof media d8ab9528): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

11. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

12. (krulwich2011molecularaspectsof pages 17-18): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

13. (chiu2023membranelipidand pages 15-16): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

14. (chong2024archaeamembranesin pages 2-3): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 9 citations.

15. (chong2024archaeamembranesin pages 1-2): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 9 citations.

16. (chong2024archaeamembranesin pages 4-6): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 9 citations.

17. (chiu2023membranelipidand pages 2-3): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

18. (chiu2023membranelipidand pages 5-6): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

19. (chiu2023membranelipidand pages 9-10): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

20. (chiu2023membranelipidand pages 6-7): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

21. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

22. (atasoy2024exploitationofmicrobial pages 10-11): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

23. (gonzalez2024acidophilicheterotrophsbasic pages 2-3): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 7 citations and is from a peer-reviewed journal.

24. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

25. (deng2023strategiesofchemolithoautotrophs pages 1-2): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 14 citations and is from a highest quality peer-reviewed journal.

26. (chiu2023membranelipidand pages 1-2): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

27. (chong2024archaeamembranesin pages 7-7): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 9 citations.

28. (krulwich2011molecularaspectsof pages 15-17): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

29. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 20-21): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

30. (watkin2024editorialacidophilemicrobiology pages 1-2): Elizabeth L. J. Watkin, Ivan Nancucheo, and Axel Schippers. Editorial: acidophile microbiology: from extreme environments to biotechnological applications. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1454559, doi:10.3389/fmicb.2024.1454559. This article has 3 citations and is from a peer-reviewed journal.

31. (chong2024archaeamembranesin pages 3-4): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 9 citations.