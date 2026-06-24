---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:39:44.306998'
end_time: '2026-06-18T00:49:49.312731'
duration_seconds: 605.01
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range low
  trait_identifier: METPO:1000460
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH range phenotype in which the growth-supporting external pH range\
    \ spans approximately 4\u20136, characteristic of acidophilic physiology."
  parent_traits: METPO:1000332
  synonyms: Acid Tolerant, Acidophile, Facultative acidophile, Obligative acidophile,
    pHR_4_to_6
  evidence_summary: "DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review\
    \ supports moderately acidic pH-homeostasis as the basis of growth in the pH 4\u2013\
    6 range.)"
  causal_graph_summary: 'ph_range_low_acidophile_range: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range low
- **METPO identifier:** METPO:1000460
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 4–6, characteristic of acidophilic physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Facultative acidophile, Obligative acidophile, pHR_4_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports moderately acidic pH-homeostasis as the basis of growth in the pH 4–6 range.)
- **Existing causal graph summary:** ph_range_low_acidophile_range: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_low.yaml`.

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
- **Trait label:** pH range low
- **METPO identifier:** METPO:1000460
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 4–6, characteristic of acidophilic physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Facultative acidophile, Obligative acidophile, pHR_4_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports moderately acidic pH-homeostasis as the basis of growth in the pH 4–6 range.)
- **Existing causal graph summary:** ph_range_low_acidophile_range: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_low.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **pH range low** (METPO:1000460)

## 0. Scope summary (curation-focused)

**Trait label:** pH range low (METPO:1000460) — ENVIRONMENT / CLASS.

**Operational definition for TraitMech curation:** capacity for **growth** (not merely survival) when the **growth-supporting external pH range spans approximately pH 4–6**, consistent with *acidophilic physiology* as defined in the template. This trait should be curated as an **environmental growth preference/compatibility** phenotype rather than an acute stress survival phenotype.

**Boundary cases / confounders to separate from METPO:1000460:**

1. **Extreme acidophily (optimum <3):** Mechanisms in extreme acidophiles are often shared, but the trait here is explicitly the pH 4–6 range (moderately acidic). Use taxon/assay notes when evidence comes from pH <3 systems. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
2. **Acid resistance systems measured at pH ~2–3 (survival, transit):** Enteric “acid resistance” systems (AR1/AR2/AR3) are frequently described for survival at pH 2.5 (e.g., gastric transit) and may not equal growth at pH 4–6; curate as **taxon- and assay-specific** unless clearly linked to growth range. (kim2023clcchloridechannels pages 2-4)
3. **Weak organic acid stress at low pH (uncoupler effect):** At low pH, undissociated organic acids can diffuse into cells and acidify the cytoplasm, inhibiting growth; this is a distinct axis from inorganic-acid pH tolerance and can dominate “low pH” assays in foods/bioprocessing. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7)

## 1. Key concepts and current understanding (mechanism-centric)

### 1.1 What “pH range low” means mechanistically
Growth at moderately low external pH requires maintaining **intracellular pH homeostasis** and electrochemical balance despite increased proton activity outside the cell. A recurrent mechanistic motif across taxa is a two-layer strategy:

- **First-line defenses (limit proton entry / control envelope permeability):** membrane lipid remodeling (e.g., cyclopropane fatty acids), outer-membrane permeability barrier changes (LPS/O-antigen; porins). (kim2023clcchloridechannels pages 2-4, deng2023strategiesofchemolithoautotrophs pages 14-16)
- **Second-line defenses (remove or consume protons that enter):** ATP-driven proton export (H+-ATPases), antiporters (Na+/H+), and **cytoplasmic proton-consuming buffering** reactions (amino-acid decarboxylase systems). (sreenivas2024evaluationofpyrophosphatedriven pages 1-2, kim2023clcchloridechannels pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

A frequently emphasized acidophile adaptation is generating an **inside-positive (inversed) membrane potential** (Δψ) to counteract proton influx; K+ uptake systems are repeatedly implicated in supporting this state. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, yao2023howmethanotrophsrespond media 6aab6742)

### 1.2 Weak acids as a key environmental boundary condition
In acidic environments relevant to pH 4–6, **organic acids** (e.g., acetate, lactate) can exist partly in an **undissociated** form depending on pKa, enabling diffusion into the cell and dissociation in the higher-pH cytoplasm, releasing protons and lowering internal pH. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7)

Recent quantitative details curated for node/edge support include pKa values (25 °C, in water): lactate ~3.86; acetate ~4.75; butyrate ~4.82; propionate ~4.87. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7)

## 2. Recent developments and latest research (prioritize 2023–2024)

### 2.1 2023–2024: genomics/transcriptomics sharpen candidate “core” node lists
A 2023 review focusing on (meta)genomes and transcriptomes of acidophiles reports repeated presence/expression of **K+ uptake systems (kdp; Kef-type)**, **Na+/H+ antiporters (nhaA)**, membrane remodeling enzymes (e.g., **cyclopropane-fatty-acyl-phospholipid synthase, cfa**), and cytoplasmic buffering systems (e.g., **adi, gadB/gadABC**). These are presented as adaptations supporting pH homeostasis in low-pH environments (e.g., AMD, acid soils). (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

### 2.2 2023: mechanistic framing of Δψ inversion and “electric shunts” in Gram-negative acid resistance
A 2023 review of Gram-negative systems consolidates a mechanistic picture where acid stress can reverse Δψ to inside-positive and where **ClC (clcA/eriC) H+/Cl− antiporters** serve as **electrical shunts** during amino-acid decarboxylase/antiporter-based acid resistance. (kim2023clcchloridechannels pages 2-4)

### 2.3 2023: envelope/permeability barrier genes highlighted in low pH adaptation in hydrothermal systems
A 2023 Microbiome study of chemolithoautotrophs under low pH and high temperature highlights enrichment/abundance of genes involved in outer-membrane permeability barriers (e.g., **O-antigen ligase; OmpA–OmpF family porin**) and notes that complex I subunits **nuoL/M/N** are homologous to Na+ or K+/H+ antiporter families—useful for hypothesis-driven edges (with uncertainty). (deng2023strategiesofchemolithoautotrophs pages 14-16)

### 2.4 2024: engineered mitigation of low-pH/weak-acid growth constraints in yeast cell factories
A 2024 industrially oriented study quantifies the energetic burden of pH homeostasis in *Saccharomyces cerevisiae* and shows a synthetic/engineering approach: expression of a **PPi-driven proton pump (H+-PPase)** improved growth rate **by 35%** at **pH 3.7 with 6 g·L−1 acetic acid** when localized to the vacuolar membrane. It also reports that PPi can be **10 to 1000× higher than ATP** during early growth on glucose. (sreenivas2024evaluationofpyrophosphatedriven pages 1-2)

## 3. Current applications and real-world implementations

### 3.1 Acidic mine drainage (AMD) and biomining-associated systems (acidophiles)
Acidophilic sulfate-reducing bacteria (aSRB) are described as key anaerobes in acidic environments and relevant for AMD contexts; their bioenergetics emphasizes proton motive force generation/maintenance and the complication that low pH can intensify proton stress, particularly when organic acids act as uncouplers. These contexts motivate curating inhibitory edges for weak acids alongside homeostasis mechanisms. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7)

### 3.2 Industrial fermentation / microbial cell factories under acidic and weak-acid stress
Low pH and acetate are common industrial stressors (e.g., lignocellulosic hydrolysates). The 2024 yeast study explicitly frames pH homeostasis as a major ATP drain and demonstrates a concrete productivity-oriented mitigation (PPi-driven proton pumping) under low pH/acetate stress. (sreenivas2024evaluationofpyrophosphatedriven pages 1-2)

## 4. Expert opinions / authoritative syntheses (what to treat as “high confidence”)

- **Core, cross-taxon mechanistic theme:** pH homeostasis relies on (i) controlling proton influx via envelope/membrane properties and (ii) removing/consuming protons via proton pumps, antiporters, and cytoplasmic buffering reactions. (kim2023clcchloridechannels pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9, deng2023strategiesofchemolithoautotrophs pages 14-16)
- **Strongly supported, mechanistically explicit modules:** amino-acid decarboxylase/antiporter systems (Gad/Adi/Cad), ClC H+/Cl− antiport shunting, cyclopropane fatty acid remodeling, and ATP-driven proton export. (kim2023clcchloridechannels pages 2-4, sreenivas2024evaluationofpyrophosphatedriven pages 1-2)
- **More tentative/inferred modules:** complex I (nuoL/M/N) antiporter-like role and porin/LPS contributions described as “suggested”; these are good candidate nodes but should be curated with **uncertainty flags** until direct functional evidence in the pH 4–6 growth regime is available. (deng2023strategiesofchemolithoautotrophs pages 14-16)

## 5. Candidate causal graph nodes (grouped by type)

### 5.1 Environmental / experimental factors
- External pH (ENVO label-only: acidic pH; assay metadata)
- Weak organic acids (CHEBI:15366 acetic acid; CHEBI:24995 lactic acid; plus pKa/speciation as contextual factor) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7)
- Chloride (CHEBI label-only) and potassium (CHEBI:29103) as key ions in electrochemical balance (kim2023clcchloridechannels pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

### 5.2 Biological processes / physiological states
- Intracellular pH homeostasis (GO:0051453)
- Proton motive force and Δψ inversion / inside-positive membrane potential (label-only state; mechanistic role supported) (kim2023clcchloridechannels pages 2-4, yao2023howmethanotrophsrespond media 6aab6742)
- Proton transport (GO:0015992)
- ATP hydrolysis-coupled proton transport (GO:0015991) (sreenivas2024evaluationofpyrophosphatedriven pages 1-2)

### 5.3 Transporters and complexes
- K+ uptake systems: **kdpABCDE**, **Kef-type** K+ transport (label-only KEGG grounding if needed) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
- Na+/H+ antiporter: **nhaA** (GO:0015385) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
- ClC H+/Cl− antiporter: **clcA/eriC** (label-only; role as electrical shunt) (kim2023clcchloridechannels pages 2-4)
- FoF1 ATPase / ATP synthase (role in proton export in AR1 context; taxon/assay-specific) (kim2023clcchloridechannels pages 2-4)
- Respiratory proton pumps / Complex I (nuo subunits; nuoL/M/N antiporter-homology) (deng2023strategiesofchemolithoautotrophs pages 14-16)

### 5.4 Enzymes / buffering systems
- Glutamate decarboxylase system: **gadA/gadB/gadABC** (EC:4.1.1.15; product GABA) (kim2023clcchloridechannels pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
- Arginine decarboxylase: **adi / speA** (EC:4.1.1.19) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
- Lysine decarboxylase system: **cadA/cadB** (EC:4.1.1.18) (kim2023clcchloridechannels pages 2-4)
- Urease system (ureABCDEFGHJ) (mentioned as buffering system in acidophile adaptations) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

### 5.5 Envelope / membrane features
- Cyclopropane-fatty-acyl-phospholipid synthase (**cfa**) / cyclopropane fatty acids → decreased membrane proton permeability (kim2023clcchloridechannels pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
- LPS biosynthesis: **O-antigen ligase** (permeability barrier) (deng2023strategiesofchemolithoautotrophs pages 14-16)
- Porins: OmpA–OmpF family porin (“TC.OOP”) implicated in acid tolerance (uncertain) (deng2023strategiesofchemolithoautotrophs pages 14-16)
- Hopanoid/squalene-related membrane adaptations (hpn genes; shc) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

## 6. Candidate causal edges (evidence-backed triples)

The following table is formatted for direct consideration as TraitMech curation candidates.

| Edge (Subject —predicate→ Object) | Node types | Suggested ontology grounding (CURIEs where available) | Evidence snippet/quote | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| K+ uptake system (kdpABCDE / K+ transporter / Kef-type K+ transport) —contributes_to→ inside-positive membrane potential | gene cluster/protein complex → physiological state | KEGG:KdpABC/KdpDE (label-only if exact IDs unresolved); CHEBI:29103 (potassium ion); GO:0051453 (regulation of intracellular pH) | “a potassium transporting ATPase suggested to be involved in the inside positive (inversed) membrane potential” and genomes/transcripts included “the Kef-type K+ transport system, a K+ transporter” and “kdpABCDE K+-transporting ATPase” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903, 2023, https://doi.org/10.3389/fmicb.2023.1149903 | Strong for acidophilic Proteobacteria; likely generalizable to low-pH growth but direct evidence comes mainly from acidophile comparative genomics/transcriptomics. |
| inside-positive membrane potential —reduces→ proton influx into cytoplasm | physiological state → process | GO:0006817 (phosphate ion transport not applicable); label-only: inversed membrane potential; GO:0051453 (regulation of intracellular pH) | AR2/AR3 “reversed [the membrane potential] from inside negative to inside positive charge” which “might be beneficial for E. coli to minimize excessive proton motive force generated during acid stress” (kim2023clcchloridechannels pages 2-4); figure caption notes K+ uptake “helps generate an internal positive membrane potential to maintain cytoplasmic pH” (yao2023howmethanotrophsrespond media 6aab6742) | 10.4014/jmb.2303.03009, 2023, https://doi.org/10.4014/jmb.2303.03009; 10.3389/fmicb.2022.1034164, 2023, https://doi.org/10.3389/fmicb.2022.1034164 | Mechanistically central but often described qualitatively; ontology grounding for the state itself is unclear. |
| P-type H+-ATPase / H+-ATPase —exports→ H+ | protein/complex → chemical | GO:0015991 (ATP hydrolysis coupled proton transport); CHEBI:15378 (hydron) | “The acid stress tolerance in S. cerevisiae is facilitated by an active export of protons via the expenditure of ATP… carried out by H+-ATPases (Pma1p and Vma3p)” (sreenivas2024evaluationofpyrophosphatedriven pages 1-2); At. ferrivorans had “a P-type ATPase proton efflux pump” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3390/microorganisms12030625, 2024, https://doi.org/10.3390/microorganisms12030625; 10.3389/fmicb.2023.1149903, 2023, https://doi.org/10.3389/fmicb.2023.1149903 | Strong, but domain-specific implementations differ: fungal Pma1/V-ATPase vs bacterial/acidophile P-type systems. |
| H+-ATPase activity —maintains→ intracellular pH homeostasis | process/protein activity → phenotype/process | GO:0051453 (regulation of intracellular pH); GO:0015991 (ATP hydrolysis coupled proton transport) | “In S. cerevisiae, pH homeostasis is presumed to use a majority of the ATP produced by glycolysis… due to the use of H+-ATPases (Pma1p and vacuolar ATPases)” (sreenivas2024evaluationofpyrophosphatedriven pages 1-2) | 10.3390/microorganisms12030625, 2024, https://doi.org/10.3390/microorganisms12030625 | Strong for yeast; broad principle applies across microbes but should not be over-generalized to all taxa without taxon tags. |
| FoF1 H+-translocating ATPase —exports→ intracellular protons | protein complex → chemical | GO:0015991; CHEBI:15378 | “For glucose-dependent AR1, the FoF1 H+-translocating ATPase on the cell membrane causes the release of intracellular protons into the extracellular environment” (kim2023clcchloridechannels pages 2-4) | 10.4014/jmb.2303.03009, 2023, https://doi.org/10.4014/jmb.2303.03009 | Strong for acid resistance in enteric bacteria; may represent survival at lower pH than growth-supporting pH 4–6, so curate with boundary note. |
| proton motive force —drives→ ATP synthase-mediated ATP formation | physiological process → process | GO:0015986 (ATP synthesis coupled proton transport); GO:0015992 (proton transport) | “The proton motive force… is maintained by the extrusion of H+… That proton potential then drives the phosphorylation of ADP and the formation of ATP by the ATP synthase” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7) | 10.1111/1758-2229.70019, 2024, https://doi.org/10.1111/1758-2229.70019 | General bioenergetic edge relevant to low-pH growth; source is acidophilic sulfate reducers. |
| nhaA Na+/H+ antiporter —contributes_to→ pH homeostasis at low pH | transporter/gene → process | GO:0015385 (sodium:proton antiporter activity); KEGG:K03313 (NhaA, if used); CHEBI:29101 (sodium ion); CHEBI:15378 | Acidophile genomes “harbor the kdpABCDE K+-transporting ATPase and the nhaA sodium/proton antiporter” and encoded “a sodium:proton antiporter” in AMD metatranscripts (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903, 2023, https://doi.org/10.3389/fmicb.2023.1149903 | Good candidate edge, but evidence here is genomic/transcriptomic association rather than direct knockout validation. |
| complex I membrane arm subunits (nuoL/M/N) —mediate→ Na+/K+/H+ antiporter-like ion exchange | protein subunits → process | KEGG:K00346/K00347 etc. (complex I subunits, approximate); GO:0008137 (NADH dehydrogenase activity) plus label-only antiporter-like function | “the nuoL/M/N subunits… are homologous to the Na+ or K+/H+ antiporter family” (deng2023strategiesofchemolithoautotrophs pages 14-16) | 10.1186/s40168-023-01712-w, 2023, https://doi.org/10.1186/s40168-023-01712-w | Useful mechanistic hypothesis, but homology-based; curate as uncertain/inferred. |
| arginine decarboxylase (adi / speA) —consumes→ cytoplasmic protons | enzyme/gene → chemical/process | EC:4.1.1.19 (arginine decarboxylase); GO:0008792; CHEBI:15378 | Acidophile genomes contained “proton-consuming cytoplasmic buffering systems adi” and “proton-consuming speA arginine decarboxylase” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903, 2023, https://doi.org/10.3389/fmicb.2023.1149903 | Strong candidate for buffering node; evidence strongest in Acidithiobacillus/Ferrovum acidophiles. |
| glutamate decarboxylase system (gadB / gadABC) —buffers→ cytoplasmic pH | enzyme system/gene cluster → process | EC:4.1.1.15; GO:0004351; CHEBI:16865 (glutamate); CHEBI:17822 (GABA) | Acidophile genomes contained “proton-consuming cytoplasmic buffering systems… gadB” and “gadABC glutamate deca…” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9); in E. coli, AR2 substrate/product table lists “GadC” and “GadA/B” producing “γ-aminobutyrate (GABA)” (kim2023clcchloridechannels pages 2-4) | 10.3389/fmicb.2023.1149903, 2023, https://doi.org/10.3389/fmicb.2023.1149903; 10.4014/jmb.2303.03009, 2023, https://doi.org/10.4014/jmb.2303.03009 | Strong across taxa for acid resistance; growth-supporting relevance at pH 4–6 may vary by organism and substrate availability. |
| lysine decarboxylase system (cadA/cadB) —neutralizes→ low extracellular pH stress | enzyme/antiporter system → phenotype/process | EC:4.1.1.18 (lysine decarboxylase); KEGG:CadA/CadB (label-only if needed); CHEBI:25094 (lysine); CHEBI:18019 (cadaverine) | Table lists AR4 with “CadB” and “CadA” and product “Cadaverine”; cited classic source: “cad operon: a system for neutralization of low extracellular pH” (kim2023clcchloridechannels pages 2-4, perezrodriguez2024methodsforstudying pages 36-37) | 10.4014/jmb.2303.03009, 2023, https://doi.org/10.4014/jmb.2303.03009; review cites 10.1128/jb.174.8.2659-2669.1992 in pqac-00000014 | Strong for enterics; likely too assay/pathogen-specific for direct generic curation unless marked taxon-specific. |
| amino acid antiporters (GadC/AdiC/CadB/PotE) —export→ decarboxylated cationic products | transporter proteins → chemicals | KEGG: GadC/AdiC/CadB/PotE (label-only); GO:0015171 family-specific transport broad label only | “Amino acid antiporters export more positively charged products than the substrates (for examples, Glu to GABA+ / Arg+ to Agm2+)” (kim2023clcchloridechannels pages 2-4) | 10.4014/jmb.2303.03009, 2023, https://doi.org/10.4014/jmb.2303.03009 | Mechanistically supports charge balancing and acid resistance; taxon- and substrate-dependent. |
| clcA H+/Cl− antiporter —acts_as→ electrical shunt during amino-acid acid resistance | transporter/gene → functional role | GO:0015107 (chloride transmembrane transporter activity, broad); KEGG:ClcA (label-only) | “ClC channels are used as electric shunts to counteract hyperpolarization” and “exchange two internal chloride ions for one proton from the outside of the cell” (kim2023clcchloridechannels pages 2-4) | 10.4014/jmb.2303.03009, 2023, https://doi.org/10.4014/jmb.2303.03009 | Strong mechanistic edge for amino-acid-mediated acid resistance; may be more relevant to transit survival than sustained growth. |
| clcA —required_for→ functional amino-acid-mediated acid resistance system | gene → phenotype/system | label-only: clcA; GO:0009651 (response to salt stress not apt); label-only acid resistance system | “the prokaryotic ClC channel clcA gene controls the amino acid-mediated AR system to be functional, which is linked to cell survival” (kim2023clcchloridechannels pages 2-4) | 10.4014/jmb.2303.03009, 2023, https://doi.org/10.4014/jmb.2303.03009 | Good edge but mostly from Gram-negative enterics; annotate taxon-specific. |
| cyclopropane-fatty-acyl-phospholipid synthase (cfa) / cyclopropane fatty acids —decrease→ membrane proton permeability | enzyme/lipid modification → membrane property | GO:0008800 (cyclopropane-fatty-acyl-phospholipid synthase activity); CHEBI label-only for cyclopropane fatty acids | “decreasing membrane proton permeability prevents the accumulation of intracellular protons” after conversion of unsaturated fatty acids into cyclopropane fatty acids (kim2023clcchloridechannels pages 2-4); Ferrovum transcripts included “cyclopropane-fatty-acyl-phospholipid synthase” for pH homeostasis (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.4014/jmb.2303.03009, 2023, https://doi.org/10.4014/jmb.2303.03009; 10.3389/fmicb.2023.1149903, 2023, https://doi.org/10.3389/fmicb.2023.1149903 | Strong and fairly generalizable membrane adaptation. |
| hopanoid/squalene biosynthesis (shc; hpnAIJKNHM) —contributes_to→ reduced proton influx / acid resistance | pathway/genes → phenotype/process | KEGG:shc (label-only); GO:0016491 broad oxidoreductase not specific; CHEBI label-only hopanoid | Acidophile genomes contained “the membrane hopanoid squalene synthesis and associated genes hpnAIJKNHM” and “a shc squalene-hopene… cyclase” among acidophile adaptations (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | 10.3389/fmicb.2023.1149903, 2023, https://doi.org/10.3389/fmicb.2023.1149903 | Plausible acid-resistance mechanism from comparative genomics; direct causal validation in pH 4–6 growth not shown here. |
| O-antigen ligase / LPS synthesis —strengthens→ outer-membrane permeability barrier | enzyme/pathway → cellular structure/property | GO:0009245 (lipid A biosynthetic process not exact); label-only O-antigen ligase; GO:0009279 (cell outer membrane) | “O-antigen ligase, which catalyzes a key step in the synthesis of lipopolysaccharide (LPS), a matter contributes to the effective permeability barrier of the bacterial outer membrane” (deng2023strategiesofchemolithoautotrophs pages 14-16) | 10.1186/s40168-023-01712-w, 2023, https://doi.org/10.1186/s40168-023-01712-w | Relevant especially for Gram-negative bacteria; low-pH role inferred from enrichment in acidic hydrothermal samples. |
| OmpA/OmpF-family porin (TC.OOP) —contributes_to→ acid tolerance | porin protein → phenotype | GO:0015288 (porin activity, broad); label-only TC.OOP/OmpA-OmpF porin family | “porin TC.OOP, a member of OmpA-OmpF porin that has been suggested to play an important role in acid tolerance” (deng2023strategiesofchemolithoautotrophs pages 14-16) | 10.1186/s40168-023-01712-w, 2023, https://doi.org/10.1186/s40168-023-01712-w | Promising but indirect (“suggested”); curate as uncertain. |
| weak organic acids (undissociated) —diffuse_into→ cell at low external pH | chemical → transport/process | CHEBI:24996 (organic acid, broad); CHEBI:15366 (acetic acid); CHEBI:24995 (lactic acid) | “Under acidic conditions, organic acids function as uncouplers… occur in their undissociated form and can diffuse into the cell” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7) | 10.1111/1758-2229.70019, 2024, https://doi.org/10.1111/1758-2229.70019 | Strong and highly relevant boundary condition: distinguishes low-pH growth from weak-acid inhibition assays. |
| intracellular dissociation of weak organic acids —lowers→ internal pH | chemical process → phenotype/process | CHEBI:15378; label-only weak-acid dissociation | “Once there, the higher pH of the cytoplasm will lead to dissociation of the acid, thus releasing protons and lowering the internal pH” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7) | 10.1111/1758-2229.70019, 2024, https://doi.org/10.1111/1758-2229.70019 | Strong causal edge; should likely be represented as inhibitory/negative effect on low-pH growth unless countered by homeostasis mechanisms. |
| PPi-driven H+-PPase (engineered) —improves→ growth under low pH plus acetic acid stress | engineered proton pump → phenotype | GO:0015078 (hydrogen ion transmembrane transporter activity, broad); CHEBI:45253 (pyrophosphate) | “A significant improvement of 35% in the growth rate at a pH of 3.7 and 6 g·L−1 acetic acid stress was observed in the vacuolar membrane H+-PPase strain” (sreenivas2024evaluationofpyrophosphatedriven pages 1-2) | 10.3390/microorganisms12030625, 2024, https://doi.org/10.3390/microorganisms12030625 | Explicitly engineered workaround in yeast, not a native broadly conserved trait mechanism; should be flagged as do-not-curate as native TraitMech unless engineering nodes are allowed. |
| exogenous/vacuolar H+-PPase —reduces_ATP_burden_of→ pH homeostasis | engineered protein → process | CHEBI:45253; GO:0015078 | “pH homeostasis is reliant on ATP… Here, an exogenous proton-translocating pyrophosphatase… which uses inorganic pyrophosphate (PPi) rather than ATP, was evaluated for its effect on reducing the ATP burden” (sreenivas2024evaluationofpyrophosphatedriven pages 1-2) | 10.3390/microorganisms12030625, 2024, https://doi.org/10.3390/microorganisms12030625 | Useful for applications/engineering section; not evidence for native microbial low-pH trait architecture. |


*Table: This table summarizes candidate subject-predicate-object edges for the microbial trait 'pH range low' using only evidence available in the cited context IDs. It is designed to help curators decide which mechanisms are broadly curation-ready versus taxon-specific, inferred, or engineering-only.*

## 7. Statistics and data points suitable for curation notes

- **Weak-acid pKa values (25 °C):** lactate ~3.86; acetate ~4.75; butyrate ~4.82; propionate ~4.87—useful for modeling/speciation nodes affecting intracellular acidification risk at pH 4–6. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7)
- **Engineered low-pH performance (yeast):** vacuolar H+-PPase strain showed **35% growth-rate improvement at pH 3.7 with 6 g·L−1 acetic acid**. (sreenivas2024evaluationofpyrophosphatedriven pages 1-2)
- **Energetic constraint framing (yeast):** pH homeostasis described as using “a majority of the ATP produced by glycolysis” due to ATP-driven H+ export, and PPi concentrations can be **10–1000× ATP** early in glucose growth. (sreenivas2024evaluationofpyrophosphatedriven pages 1-2)

## 8. Warnings / “do not curate yet” items

1. **Do not equate survival-at-pH-2.5 acid resistance (AR systems) with growth range pH 4–6** unless an explicit growth phenotype is demonstrated. Many mechanistic modules are likely relevant, but the trait definition is growth-supporting pH range. (kim2023clcchloridechannels pages 2-4)
2. **Homology-based functional claims** (e.g., nuoL/M/N “homologous to Na+ or K+/H+ antiporter family”) are valuable for hypothesis generation but should be curated with **uncertainty** or held until direct functional evidence is available in organisms/assays matching METPO:1000460. (deng2023strategiesofchemolithoautotrophs pages 14-16)
3. **Engineered solutions (H+-PPase in yeast)** improve low-pH/weak-acid performance but are not native trait mechanisms; curate only if TraitMech supports engineering nodes or if explicitly captured as “application/implementation” evidence rather than natural mechanism. (sreenivas2024evaluationofpyrophosphatedriven pages 1-2)

## 9. DOI-first bibliography (with URLs and publication dates where available)

1. Valdez-Nuñez LF, Kappler A, Ayala-Muñoz D, et al. **Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.** *Environmental Microbiology Reports.* **Oct 2024.** DOI: **10.1111/1758-2229.70019**. URL: https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7)
2. Sreenivas K, Eisentraut L, Brink DP, et al. **Evaluation of Pyrophosphate-Driven Proton Pumps in Saccharomyces cerevisiae under Stress Conditions.** *Microorganisms.* **20 Mar 2024 (published).** DOI: **10.3390/microorganisms12030625**. URL: https://doi.org/10.3390/microorganisms12030625 (sreenivas2024evaluationofpyrophosphatedriven pages 1-2)
3. Deng W, Zhao Z, Li Y, et al. **Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem.** *Microbiome.* **Dec 2023.** DOI: **10.1186/s40168-023-01712-w**. URL: https://doi.org/10.1186/s40168-023-01712-w (deng2023strategiesofchemolithoautotrophs pages 14-16)
4. Dopson M, González-Rosales C, Holmes DS, Mykytczuk N. **Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies.** *Frontiers in Microbiology.* **Mar 2023.** DOI: **10.3389/fmicb.2023.1149903**. URL: https://doi.org/10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
5. Kim M, Choi N-J, Choi E, Lee E-J. **ClC Chloride Channels in Gram-Negative Bacteria and Its Role in the Acid Resistance Systems.** *Journal of Microbiology and Biotechnology.* **Apr 2023.** DOI: **10.4014/jmb.2303.03009**. URL: https://doi.org/10.4014/jmb.2303.03009 (kim2023clcchloridechannels pages 2-4)
6. Yao X, Wang J, Hu B. **How methanotrophs respond to pH: A review of ecophysiology.** *Frontiers in Microbiology.* **Jan 2023.** DOI: **10.3389/fmicb.2022.1034164**. URL: https://doi.org/10.3389/fmicb.2022.1034164 (figure evidence for homeostasis schematic) (yao2023howmethanotrophsrespond media 6aab6742)
7. Pérez-Rodríguez F, Possas A, Scheler O. **Methods for studying microbial acid stress responses.** *FEMS Microbiology Reviews (cited section shown).* **2024 (Vol. 48, No. 5).** Includes foundational review citation: Nat Rev Micro 2011 DOI **10.1038/nrmicro2549**. (perezrodriguez2024methodsforstudying pages 36-37)


References

1. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

2. (kim2023clcchloridechannels pages 2-4): Minjeong Kim, Nak-Joong Choi, Eunna Choi, and Eun-Jin Lee. Clc chloride channels in gram-negative bacteria and its role in the acid resistance systems. Journal of Microbiology and Biotechnology, 33:857-863, Apr 2023. URL: https://doi.org/10.4014/jmb.2303.03009, doi:10.4014/jmb.2303.03009. This article has 8 citations and is from a peer-reviewed journal.

3. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 6-7): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

4. (deng2023strategiesofchemolithoautotrophs pages 14-16): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 14 citations and is from a highest quality peer-reviewed journal.

5. (sreenivas2024evaluationofpyrophosphatedriven pages 1-2): Krishnan Sreenivas, Leon Eisentraut, Daniel P. Brink, Viktor C. Persson, Magnus Carlquist, Marie F. Gorwa-Grauslund, and Ed W. J. van Niel. Evaluation of pyrophosphate-driven proton pumps in saccharomyces cerevisiae under stress conditions. Microorganisms, 12:625, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030625, doi:10.3390/microorganisms12030625. This article has 4 citations.

6. (yao2023howmethanotrophsrespond media 6aab6742): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

7. (perezrodriguez2024methodsforstudying pages 36-37): F Pérez-Rodríguez, A Possas, and O Scheler. Methods for studying microbial acid stress responses. Unknown journal, 2024.