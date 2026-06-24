---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:01:49.270517'
end_time: '2026-06-17T22:12:40.772931'
duration_seconds: 651.5
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultatively acidophilic
  trait_identifier: METPO:1003007
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultatively_acidophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference characterized by optimal growth in acidic environments
    (pH below 5.5) with the capacity to also grow at near-neutral pH values.
  parent_traits: METPO:1003000
  synonyms: facultative acidophile
  evidence_summary: 'DOI:10.1099/ijs.0.066175-0: capable of growth at pH 4.0-7.2 (Species-level
    example supports acidic-to-near-neutral growth capacity in a mildly acidophilic
    bacterium.)'
  causal_graph_summary: 'facultatively_acidophilic_ph_homeostasis: 7 nodes, 6 edges'
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
- **Trait label:** facultatively acidophilic
- **METPO identifier:** METPO:1003007
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth in acidic environments (pH below 5.5) with the capacity to also grow at near-neutral pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative acidophile
- **Existing evidence:** DOI:10.1099/ijs.0.066175-0: capable of growth at pH 4.0-7.2 (Species-level example supports acidic-to-near-neutral growth capacity in a mildly acidophilic bacterium.)
- **Existing causal graph summary:** facultatively_acidophilic_ph_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **facultatively acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_acidophilic.yaml`.

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
- **Trait label:** facultatively acidophilic
- **METPO identifier:** METPO:1003007
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth in acidic environments (pH below 5.5) with the capacity to also grow at near-neutral pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** facultative acidophile
- **Existing evidence:** DOI:10.1099/ijs.0.066175-0: capable of growth at pH 4.0-7.2 (Species-level example supports acidic-to-near-neutral growth capacity in a mildly acidophilic bacterium.)
- **Existing causal graph summary:** facultatively_acidophilic_ph_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **facultatively acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultatively_acidophilic.yaml`.

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


## Curation-focused research report: Facultatively acidophilic (METPO:1003007)

### 1) Trait scope (phenotype definition and boundaries)

**Target trait (as provided):** *facultatively acidophilic* (syn. *facultative acidophile*) describes a pH growth preference where **optimal growth occurs at acidic pH (<5.5)**, while the organism **retains the ability to grow at near-neutral pH**. Mechanistically, this implies the cell can execute (and regulate) pH-homeostasis systems across a broad external pH range.

**Distinguishing from nearby traits**

1. **Moderate vs extreme/obligate acidophily (growth optimum concept):**
   * Acidophilic heterotroph review definitions: **moderate acidophiles** have optimal growth **pH 3–5**, while **extreme acidophiles** have optimal growth **pH ≤3**; an extreme example (*Picrophilus oshimae*) can grow at approximately **pH 0**. (gonzalez2024acidophilicheterotrophsbasic pages 1-2)
   * An acidophile lifestyle framing (Acidithiobacillia): **moderate acidophiles** have **pH optimum ≤5**, and **extreme acidophiles** grow optimally at **pH ≤3**. (gonzalezrosales2022integrativegenomicssheds pages 1-2)

2. **Acid-tolerant neutralophiles / “acid shock survivors” vs growth across acidic pH:**
   * A comparative acidophile paper contrasts true extreme acidophiles (thriving at **≤pH 3.5**) with neutrophiles that only survive transient exposure (“amateur acidophiles”). (vergara2020evolutionofpredicted pages 1-3)
   * In *E. coli*, the 2024 review notes that some strains can **survive for hours at pH 2 but cannot grow**—highlighting survival vs growth as a boundary case. (li2024responseofescherichia pages 1-2)

3. **Operationalizing the trait in assays (recommended for curation):**
   * Trait evidence should be based on **growth curves/OD or growth rate across a pH gradient**, not only viability after acid shock.
   * For facultative acidophily, the key criterion is a **growth-permissive range spanning acidic (e.g., pH ≤5.5) to near-neutral pH (~6.5–7.5)** with an **acidic optimum**.

**Quantitative context for intracellular pH homeostasis requirements**

Acidophiles are described as needing to **maintain a near-neutral cytoplasm** despite an **external-to-internal proton gradient up to 10^5-fold**. (gonzalezrosales2022integrativegenomicssheds pages 1-2)


### 2) Key concepts and mechanistic definitions (current understanding)

The “facultatively acidophilic” phenotype can be decomposed into two coupled capacities:

1. **Low-pH growth capacity** (acid-side): preventing proton influx and/or neutralizing/expelling protons.
2. **Near-neutral growth capacity** (neutral-side): maintaining energetic efficiency and ion homeostasis without maladaptive overexpression of extreme-acid modules.

A useful organizing principle (common in acidophile literature) is **“first-line” vs “second-line” defenses**:

* **First-line defenses: limit proton entry**
  * **Inside-positive membrane potential** (electrostatic barrier) often attributed to **K+ accumulation/uptake systems**. (gonzalezrosales2022integrativegenomicssheds pages 1-2, vergara2020evolutionofpredicted pages 1-3)
  * **Low-permeability cell envelopes** (e.g., rigid membranes, altered porins), plus lipid and polyamine effects. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2)

* **Second-line defenses: remove or consume internal protons**
  * **Proton export pumps and antiporters** (e.g., Na+/H+ exchange; chloride/proton antiport). (gonzalezrosales2022integrativegenomicssheds pages 1-2, vergara2020evolutionofpredicted pages 16-17)
  * **Proton-consuming metabolism** (e.g., amino-acid decarboxylation; urease). (nie2024researchprogressin pages 11-12, gonzalezrosales2022integrativegenomicssheds pages 1-2)


### 3) Candidate mechanistic entities (nodes) for a TraitMech causal graph

The table below provides a candidate node inventory grounded in the retrieved evidence.

| Node label | Node type | Description (1 sentence) | Evidence source(s) (DOI, year, URL) | Suggested CURIE(s) if available |
|---|---|---|---|---|
| Low external pH | environmental factor | Acidic external conditions create the proton stress that defines the trait context and require active pH homeostasis. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2021.822229 (2022) https://doi.org/10.3389/fmicb.2021.822229; DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | ENVO: acidic environment candidate |
| Near-neutral pH growth | environmental factor | Facultatively acidophilic organisms must retain growth capacity when environmental pH approaches neutrality. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, qin2024characterizationofmild pages 1-2) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903; DOI:10.3390/microorganisms12081565 (2024) https://doi.org/10.3390/microorganisms12081565 | label only |
| Chloride stress | environmental factor | Chloride can intensify acid stress by promoting cytoplasmic acidification and oxidative stress in acidophiles. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2019.02455 (2019) https://doi.org/10.3389/fmicb.2019.02455 | CHEBI:17996 |
| Sulfate | environmental factor | Sulfate-rich acidic settings are common habitats for acidophilic sulfate reducers and acid-mine systems. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | DOI:10.1111/1758-2229.70019 (2024) https://doi.org/10.1111/1758-2229.70019 | CHEBI:16189 |
| Ferrous iron | environmental factor | Ferrous iron is a defining substrate in many acidic mine and iron-oxidizing habitats where low-pH adaptations are expressed. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | CHEBI:29033 |
| Acid mine drainage | application context | AMD is a major acidic ecosystem and biotechnology setting where acid-homeostasis mechanisms are environmentally relevant. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903; DOI:10.1111/1758-2229.70019 (2024) https://doi.org/10.1111/1758-2229.70019 | ENVO:00001991 candidate |
| Acid mine lake | application context | Acidic mine lakes provide natural low-pH habitats where nitrifiers and other acid-adapted microbes persist. (yao2023howmethanotrophsrespond pages 5-7, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | DOI:10.1128/AEM.00047-23 (2023) https://doi.org/10.1128/AEM.00047-23; DOI:10.1111/1758-2229.70019 (2024) https://doi.org/10.1111/1758-2229.70019 | ENVO candidate |
| Pit lake | application context | Pit lakes are field systems with quantified acidic gradients used to study acidophilic sulfate-reducing communities. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | DOI:10.1111/1758-2229.70019 (2024) https://doi.org/10.1111/1758-2229.70019 | ENVO candidate |
| Biomining / bioleaching | application context | Acidophilic physiology is exploited in biomining and bioleaching, making robust pH homeostasis industrially important. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, boase2022predictionandinferred pages 1-2) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903; DOI:10.3389/fmicb.2022.848410 (2022) https://doi.org/10.3389/fmicb.2022.848410 | label only |
| Bicarbonate production | metabolite | Bicarbonate generation can alkalinize the local microenvironment and mitigate external acidity. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | DOI:10.1111/1758-2229.70019 (2024) https://doi.org/10.1111/1758-2229.70019 | CHEBI:17544 |
| Near-neutral cytoplasm | process | Maintenance of a near-neutral cytoplasm is the central physiological target of acid-homeostasis systems. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903; DOI:10.3389/fmicb.2021.822229 (2022) https://doi.org/10.3389/fmicb.2021.822229 | GO:0006885 candidate |
| Cytoplasmic buffering | process | Intracellular buffering dampens proton fluctuations and is a shared mechanism between acidophiles and neutrophiles. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903; DOI:10.3389/fmicb.2021.822229 (2022) https://doi.org/10.3389/fmicb.2021.822229 | GO:0006885 candidate |
| Internal positive membrane potential | process | An inside-positive potential creates an electrochemical barrier that opposes proton influx at low pH. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, vergara2020evolutionofpredicted pages 1-3) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903; DOI:10.3390/genes11040389 (2020) https://doi.org/10.3390/genes11040389 | label only |
| Proton export | process | Proton-export systems form a key second line of defense after protons enter the cell. (nie2024researchprogressin pages 11-12, gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.13343/j.cnki.wsxb.20230336 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230336; DOI:10.3389/fmicb.2021.822229 (2022) https://doi.org/10.3389/fmicb.2021.822229 | GO:0015992 |
| Proton consumption | process | Proton-consuming metabolic reactions such as amino-acid decarboxylation and ureolysis directly neutralize acid stress. (nie2024researchprogressin pages 11-12, gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.13343/j.cnki.wsxb.20230336 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230336; DOI:10.3389/fmicb.2021.822229 (2022) https://doi.org/10.3389/fmicb.2021.822229 | label only |
| Oxidative phosphorylation | process | Respiratory-energy metabolism is positively associated with mild acid adaptation and can support proton-handling energetics. (yao2023howmethanotrophsrespond pages 5-7, qin2024characterizationofmild pages 1-2) | DOI:10.3389/fmicb.2022.1034164 (2023) https://doi.org/10.3389/fmicb.2022.1034164; DOI:10.3390/microorganisms12081565 (2024) https://doi.org/10.3390/microorganisms12081565 | KEGG:ko00190 |
| Mild acid stress response | process | Growth under moderately acidic pH involves a distinct systems-level transcriptional program separate from extreme acid shock. (qin2024characterizationofmild pages 1-2) | DOI:10.3390/microorganisms12081565 (2024) https://doi.org/10.3390/microorganisms12081565 | label only |
| Alkalinization of microenvironment | process | Some acid-adapted microbes increase local pH, helping sustain metabolism in acidic habitats. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | DOI:10.1111/1758-2229.70019 (2024) https://doi.org/10.1111/1758-2229.70019 | GO candidate |
| Kdp system | gene-protein system | The high-affinity Kdp transporter is repeatedly implicated in K+ uptake, membrane-potential generation, and acid tolerance. (vergara2020evolutionofpredicted pages 1-3, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3390/genes11040389 (2020) https://doi.org/10.3390/genes11040389; DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label:KdpABC/KdpDE |
| Kch potassium channel | gene-protein system | Kch is one of the K+ transport systems proposed to build the inside-positive barrier against proton entry. (vergara2020evolutionofpredicted pages 1-3) | DOI:10.3390/genes11040389 (2020) https://doi.org/10.3390/genes11040389 | label:Kch |
| Trk potassium transporter | gene-protein system | Trk-mediated K+ uptake contributes to positive membrane potential and low-pH resistance. (vergara2020evolutionofpredicted pages 1-3) | DOI:10.3390/genes11040389 (2020) https://doi.org/10.3390/genes11040389 | label:TrkAEH |
| Kef-type potassium transport | gene-protein system | Kef-type K+ transporters are reported in acidophilic genomes and likely participate in ionic homeostasis. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label:Kef |
| Voltage-gated potassium channel | gene-protein system | Voltage-gated K+ channels are additional candidates for building electrochemical defenses at low pH. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label only |
| NhaA Na+/H+ antiporter | gene-protein system | NhaA exchanges Na+ and H+ and is a core candidate for exporting excess intracellular protons. (nie2024researchprogressin pages 11-12, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.13343/j.cnki.wsxb.20230336 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230336; DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label:NhaA |
| NhaP Na+/H+ antiporter | gene-protein system | NhaP is proposed as a proton-expulsion mechanism in comparative acidophile analyses. (vergara2020evolutionofpredicted pages 16-17) | DOI:10.3390/genes11040389 (2020) https://doi.org/10.3390/genes11040389 | label:NhaP |
| Mrp cation/proton antiporter | gene-protein system | The multimeric Mrp antiporter is a recent mechanistic candidate for microbial pH homeostasis. (nie2024researchprogressin pages 11-12) | DOI:10.13343/j.cnki.wsxb.20230336 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230336 | label:Mrp complex |
| ClcA chloride/proton antiporter | gene-protein system | ClcA is proposed to participate in proton expulsion and acid adaptation in acidophile genomes and communities. (vergara2020evolutionofpredicted pages 16-17) | DOI:10.3390/genes11040389 (2020) https://doi.org/10.3390/genes11040389 | label:ClcA |
| F0F1-ATPase / ATP synthase | gene-protein system | ATP synthase is implicated in non-neutral pH bioenergetics and proton homeostasis. (nie2024researchprogressin pages 11-12, yao2023howmethanotrophsrespond pages 5-7) | DOI:10.13343/j.cnki.wsxb.20230336 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230336; DOI:10.3389/fmicb.2022.1034164 (2023) https://doi.org/10.3389/fmicb.2022.1034164 | GO:0015986 |
| GadA/GadB/GadC glutamate decarboxylase system | gene-protein system | The GAD system consumes intracellular protons during glutamate decarboxylation and can couple to glutamate/GABA antiport. (nie2024researchprogressin pages 11-12, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.13343/j.cnki.wsxb.20230336 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230336; DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label:GadA/GadB/GadC |
| GadE regulator | gene-protein system | GadE activation improved engineered E. coli growth under mild acid stress, making it a useful regulatory candidate node. (qin2024characterizationofmild pages 1-2) | DOI:10.3390/microorganisms12081565 (2024) https://doi.org/10.3390/microorganisms12081565 | label:GadE |
| SpeA arginine decarboxylase | gene-protein system | SpeA represents a proton-consuming amino-acid decarboxylase route linked to acid adaptation. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label:SpeA |
| Arginine deiminase / arginine-dependent acid resistance | gene-protein system | Arginine-dependent systems are recurrently cited among proton-consuming acid-resistance modules. (nie2024researchprogressin pages 11-12, boase2022predictionandinferred pages 1-2) | DOI:10.13343/j.cnki.wsxb.20230336 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230336; DOI:10.3389/fmicb.2022.848410 (2022) https://doi.org/10.3389/fmicb.2022.848410 | label only |
| Urease system (ureABCDEFGHJ) | gene-protein system | Urease neutralizes acid stress through urea hydrolysis and ammonia generation. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label:ureABCDEFGHJ |
| HdeB periplasmic chaperone | gene-protein system | HdeB is a periplasmic acid-stress chaperone shown to support growth in an engineered mild-acid-tolerant strain. (qin2024characterizationofmild pages 1-2) | DOI:10.3390/microorganisms12081565 (2024) https://doi.org/10.3390/microorganisms12081565 | label:HdeB |
| ClpXP protease | gene-protein system | ClpXP is part of the proteostasis network enriched in acidophiles and may protect proteins under low-pH stress. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label:ClpXP |
| rus/cyc2/petABC iron-oxidation module | gene-protein system | Ferrous-iron oxidation genes co-occur with acid-adaptation traits in low-pH iron-oxidizing lineages. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label:rus/cyc2/petABC |
| Hopanoids | membrane feature | Hopanoids are membrane lipids that reduce proton permeability and stabilize cells under acidic conditions. (boase2022predictionandinferred pages 1-2, gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2022.848410 (2022) https://doi.org/10.3389/fmicb.2022.848410; DOI:10.3389/fmicb.2021.822229 (2022) https://doi.org/10.3389/fmicb.2021.822229 | CHEBI:51963 candidate |
| hpnAIJKNHM hopanoid biosynthesis genes | gene-protein system | These genes represent the identified hopanoid biosynthesis module associated with acid adaptation. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label:hpnAIJKNHM |
| shc squalene-hopene cyclase | gene-protein system | Squalene-hopene cyclase is a key enzymatic entry point into hopanoid production and membrane remodeling. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | EC candidate; label:shc |
| cfa cyclopropane-fatty-acyl-phospholipid synthase | gene-protein system | cfa supports synthesis of cyclopropane fatty acids that can decrease membrane proton permeability. (nie2024researchprogressin pages 11-12, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.13343/j.cnki.wsxb.20230336 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230336; DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | label:cfa |
| Rigid / proton-impermeable membrane | membrane feature | A rigid membrane is a first-line defense limiting passive H+ influx. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903; DOI:10.1111/1758-2229.70019 (2024) https://doi.org/10.1111/1758-2229.70019 | GO:0016020 |
| Saturated fatty acids | membrane feature | Enrichment of saturated fatty acids is associated with lowered proton permeability in acid-adapted membranes. (yao2023howmethanotrophsrespond pages 5-7) | DOI:10.3389/fmicb.2022.1034164 (2023) https://doi.org/10.3389/fmicb.2022.1034164 | CHEBI class candidate |
| Spermidine | metabolite | Spermidine is a polyamine proposed to decrease outer-membrane permeability and contribute to acid resistance. (gonzalezrosales2022integrativegenomicssheds pages 1-2, vergara2020evolutionofpredicted pages 1-3) | DOI:10.3389/fmicb.2021.822229 (2022) https://doi.org/10.3389/fmicb.2021.822229; DOI:10.3390/genes11040389 (2020) https://doi.org/10.3390/genes11040389 | CHEBI:15746 |
| Alkaline amino acids | metabolite | Overproduction of alkaline amino acids is proposed to enhance cytoplasmic buffering under acid stress. (gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2021.822229 (2022) https://doi.org/10.3389/fmicb.2021.822229 | CHEBI class candidate |
| Glutamate | metabolite | Glutamate is the substrate for proton-consuming glutamate decarboxylation in GAD-based resistance systems. (nie2024researchprogressin pages 11-12, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.13343/j.cnki.wsxb.20230336 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230336; DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | CHEBI:29991 |
| GABA | metabolite | GABA is the decarboxylation product in the GAD pathway and part of glutamate/GABA antiport cycles. (nie2024researchprogressin pages 11-12, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.13343/j.cnki.wsxb.20230336 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230336; DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | CHEBI:16865 |
| Urea | metabolite | Urea is the substrate of urease-mediated acid neutralization systems. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903 (2023) https://doi.org/10.3389/fmicb.2023.1149903 | CHEBI:16199 |


*Table: This table lists candidate nodes for a causal graph of facultative acidophily, spanning environmental context, cellular processes, gene systems, metabolites, membrane traits, and applications. It is designed to support TraitMech curation by identifying reusable mechanistic entities grounded in the cited evidence.*


### 4) Evidence-backed candidate causal edges (triples)

The table below lists **candidate causal edges** suitable for a TraitMech causal graph, with mechanistic rationale, supporting snippets, and source metadata.

| Subject node | Predicate | Object node | Mechanistic rationale (1 sentence) | Evidence snippet (quote) | Source (DOI, year, URL) | Confidence | Suggested CURIEs (subject/object) |
|---|---|---|---|---|---|---|---|
| Low external pH | necessitates maintenance of | near-neutral cytoplasm | Acidophilic growth requires preserving cytoplasmic pH despite steep proton gradients. | "maintain a near-neutral cytoplasm" despite "an external to internal proton gradient across the cytoplasmic membrane up to 10^5-fold" (gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2021.822229; Feb 2022; https://doi.org/10.3389/fmicb.2021.822229 | high | ENVO:100? low pH environment / GO:0006885? candidate cytoplasmic pH regulation |
| Potassium ions | generate | internal positive membrane potential | Intracellular K+ accumulation helps create an inside-positive potential that opposes proton influx. | "internal positive membrane potential thought to be generated by potassium ions" (gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2021.822229; Feb 2022; https://doi.org/10.3389/fmicb.2021.822229 | high | CHEBI:29103 / label:internal positive membrane potential |
| Kch/Kdp/Trk potassium transporters | contribute to | inside-positive membrane potential | K+ transport systems are proposed first-line defenses because they raise internal positive charge and reduce proton entry. | "likely generated by potassium ions ... accumulated via the Kch, Kdp, and Trk K+ channel proteins" (vergara2020evolutionofpredicted pages 1-3) | DOI:10.3390/genes11040389; Apr 2020; https://doi.org/10.3390/genes11040389 | medium | label:Kch-Kdp-Trk K+ transporters / label:inside-positive membrane potential |
| Kdp potassium uptake system | supports | acid tolerance | High-affinity K+ uptake is repeatedly associated with low-pH adaptation in acidophiles. | "kdp potassium uptake system" and "kdpABCDE K+-transporting ATPase" were identified among acid/homeostasis traits (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903; Mar 2023; https://doi.org/10.3389/fmicb.2023.1149903 | medium | label:Kdp system / METPO:1003007 |
| Hopanoid biosynthesis | reduces | membrane proton permeability | Hopanoids stiffen membranes and are linked to resisting proton influx under low pH. | "membrane alterations via inclusion of hopanoids" and gain of "hopanoid biosynthesis" genes were linked to acidophilic lifestyle (gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2021.822229; Feb 2022; https://doi.org/10.3389/fmicb.2021.822229 | high | label:hopanoid biosynthetic process / label:reduced proton permeability |
| Spermidine | reduces | outer membrane permeability | Polyamines are proposed first-line defenses because they decrease permeability to protons. | "reduced outer membrane permeability via polyamines such as spermidine" (gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2021.822229; Feb 2022; https://doi.org/10.3389/fmicb.2021.822229 | medium | CHEBI:15756 / GO:0016236? candidate membrane permeability regulation |
| cfa cyclopropane-fatty-acyl-phospholipid synthase | promotes | membrane adaptation to low pH | Cyclopropane fatty acid synthesis is a canonical route to lower membrane proton permeability. | "cfa cyclopropane-fatty-acyl-phospholipid synthase" was among genes linked to acid adaptation (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903; Mar 2023; https://doi.org/10.3389/fmicb.2023.1149903 | medium | label:cfa / GO:0016104? candidate cyclopropane-fatty-acyl-phospholipid biosynthetic process |
| Rigid/impermeable membrane | limits | proton entry | A less permeable membrane acts as a barrier against excess H+ influx. | acidophiles use a "rigid and impermeable membrane" that resists proton entry (dopson2023eurypsychrophilicacidophilesfrom pages 2-4) | DOI:10.3389/fmicb.2023.1149903; Mar 2023; https://doi.org/10.3389/fmicb.2023.1149903 | high | GO:0016020 / CHEBI:15378 |
| Unique Omp40 porin | contributes to | proton exclusion | Altered porin properties can reduce passive proton influx across the outer membrane. | a "unique Omp40 porin protein in At. ferrooxidans" is cited among membrane features supporting low-pH growth (dopson2023eurypsychrophilicacidophilesfrom pages 2-4) | DOI:10.3389/fmicb.2023.1149903; Mar 2023; https://doi.org/10.3389/fmicb.2023.1149903 | uncertain | label:Omp40 porin / label:proton exclusion |
| Proton export pumps and antiporters | expel | cytoplasmic protons | Second-line defenses directly remove protons that have entered the cell. | "proton export pumps and antiporters" are listed among mechanisms maintaining pH homeostasis (gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2021.822229; Feb 2022; https://doi.org/10.3389/fmicb.2021.822229 | high | GO:0015992 / CHEBI:15378 |
| Primary and secondary pumps | remove | excess protons | Acidophiles share with neutrophiles active pumping systems that restore intracellular pH. | acidophiles share "primary and secondary pumps" that remove excess protons (dopson2023eurypsychrophilicacidophilesfrom pages 2-4) | DOI:10.3389/fmicb.2023.1149903; Mar 2023; https://doi.org/10.3389/fmicb.2023.1149903 | high | GO:0015992 / CHEBI:15378 |
| NhaA sodium/proton antiporter | exports | excess intracellular protons | Na+/H+ antiport exchanges intracellular H+ for extracellular Na+, aiding pH homeostasis. | "nhaA sodium/proton antiporter" and "Na+/H+ exchangers (NhaA)" have roles in pH homeostasis (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, nie2024researchprogressin pages 11-12) | DOI:10.13343/j.cnki.wsxb.20230336; 2024; https://doi.org/10.13343/j.cnki.wsxb.20230336 | high | label:NhaA / CHEBI:15378 |
| Mrp cation/proton antiporter | contributes to | pH homeostasis | Multi-subunit cation/proton antiporters are recent mechanistic candidates for microbial pH homeostasis. | "multi-subunit Mrp-type cation/proton antiporters" have roles in pH homeostasis (nie2024researchprogressin pages 11-12) | DOI:10.13343/j.cnki.wsxb.20230336; 2024; https://doi.org/10.13343/j.cnki.wsxb.20230336 | medium | label:Mrp complex / GO:0006885? candidate pH homeostasis |
| ClcA chloride/proton antiporter | mediates | proton expulsion | Cl-/H+ antiport is proposed as a second-line mechanism to alleviate intracellular acidification. | "proton expulsion mechanisms such as ClcA, NhaP, and Gad" (vergara2020evolutionofpredicted pages 16-17) | DOI:10.3390/genes11040389; Apr 2020; https://doi.org/10.3390/genes11040389 | medium | label:ClcA / CHEBI:15378 |
| Glutamate decarboxylase system (GadA/GadB/GadC) | consumes | intracellular protons | Glutamate decarboxylation removes H+ and can be coupled to antiport for sustained acid resistance. | "proton consuming reactions such as glutamate decarboxylase" (gonzalezrosales2022integrativegenomicssheds pages 1-2); "gadABC" identified among acid-adaptation genes (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2021.822229; Feb 2022; https://doi.org/10.3389/fmicb.2021.822229 | high | label:Gad system / CHEBI:15378 |
| Arginine decarboxylase SpeA / arginine-dependent acid resistance | consumes | intracellular protons | Arginine decarboxylation is another amino-acid-dependent route for cytoplasmic proton consumption. | "speA arginine decarboxylase" and "arginine decarboxylase system" were linked to acid adaptation (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, boase2022predictionandinferred pages 1-2) | DOI:10.3389/fmicb.2022.848410; Apr 2022; https://doi.org/10.3389/fmicb.2022.848410 | medium | label:SpeA / CHEBI:15378 |
| Urease system (ureABCDEFGHJ) | neutralizes | intracellular acid stress | Urea hydrolysis consumes protons/ammonia release and is a recognized acid-tolerance route. | "ureABCDEFGHJ urease system" and "Urease ... can consume protons via urea hydrolysis" (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | DOI:10.3389/fmicb.2023.1149903; Mar 2023; https://doi.org/10.3389/fmicb.2023.1149903 | medium | label:urease complex / CHEBI:15378 |
| Cytoplasmic buffering | stabilizes | intracellular pH | Buffering by cellular components and metabolites dampens pH fluctuations across environments. | shared mechanisms include "cytoplasmic buffering" (dopson2023eurypsychrophilicacidophilesfrom pages 2-4) | DOI:10.3389/fmicb.2023.1149903; Mar 2023; https://doi.org/10.3389/fmicb.2023.1149903 | high | GO:0006885? candidate / label:intracellular pH |
| Overproduction of alkaline amino acids | buffers | cytoplasm | Alkaline amino acids can raise buffering capacity and help offset proton influx. | "cytoplasmic buffering via an overproduction of alkaline amino acids" (gonzalezrosales2022integrativegenomicssheds pages 1-2) | DOI:10.3389/fmicb.2021.822229; Feb 2022; https://doi.org/10.3389/fmicb.2021.822229 | medium | label:alkaline amino acid overproduction / label:cytoplasmic buffering |
| F0F1-ATPase / ATP synthase adaptation | supports | proton homeostasis under non-neutral pH | ATP synthase can participate in proton handling and recent reviews note subunit adaptations for pH homeostasis. | "ATP synthase subunit adaptations support energy conservation under non-neutral pH" (nie2024researchprogressin pages 11-12); "F0F1-ATPase using returning proton flux for ATP synthesis" (yao2023howmethanotrophsrespond pages 5-7) | DOI:10.13343/j.cnki.wsxb.20230336; 2024; https://doi.org/10.13343/j.cnki.wsxb.20230336 | medium | GO:0015986 / CHEBI:15378 |
| gadE overexpression | increases | mild-acid growth robustness | In engineered E. coli, activating an acid-resistance regulator improved growth at pH 6.0, supporting a causal role in mild acid adaptation. | synthetic module included a "proton-consuming acid resistance system (gadE)" and final OD600 at pH 6.0 was "131% and 124%" of the parent controls (qin2024characterizationofmild pages 1-2) | DOI:10.3390/microorganisms12081565; Jul 2024; https://doi.org/10.3390/microorganisms12081565 | medium | label:gadE / METPO:1003007 |
| hdeB periplasmic chaperone | supports | mild-acid tolerance | Periplasmic chaperones protect envelope proteins during acid stress and improved growth when engineered into E. coli. | synthetic acid-tolerance module included "a periplasmic chaperone (hdeB)" (qin2024characterizationofmild pages 1-2) | DOI:10.3390/microorganisms12081565; Jul 2024; https://doi.org/10.3390/microorganisms12081565 | medium | label:HdeB / label:mild-acid tolerance |
| Oxidative phosphorylation genes | are upregulated during | mild acid stress response | Enhanced respiratory-energy metabolism is associated with adaptation to mildly acidic growth. | "upregulation of the genes involved in oxidative phosphorylation" and these genes were "highly positively associated with mild acid stress responses" (qin2024characterizationofmild pages 1-2) | DOI:10.3390/microorganisms12081565; Jul 2024; https://doi.org/10.3390/microorganisms12081565 | medium | KEGG:ko00190 / label:mild acid stress response |
| ABC transporters | are positively associated with | mild acid stress response | Transport remodeling appears to be part of the systems-level response that sustains growth at mildly acidic pH. | "ATP-binding cassette (ABC) transporters ... were highly positively associated with mild acid stress responses" (qin2024characterizationofmild pages 1-2) | DOI:10.3390/microorganisms12081565; Jul 2024; https://doi.org/10.3390/microorganisms12081565 | medium | KEGG:ko02010 / label:mild acid stress response |
| Acidophilic sulphate-reducing bacteria | alkalinize | acidic microenvironment | aSRB can raise local pH through metabolism, enabling persistence and useful remediation activity in acidic systems. | they can increase pH via "bicarbonate production (alkalinization...)" and are used for AMD treatment at "pH <3" (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2) | DOI:10.1111/1758-2229.70019; Oct 2024; https://doi.org/10.1111/1758-2229.70019 | medium | label:aSRB / ENVO:00001995? acidic microenvironment |
| Acidic growth optimum (pH 3–5) with circumneutral intracellular pH | is consistent with | facultatively acidophilic scope candidate | Moderate acidophile-like physiology overlaps with facultatively acidophilic microbes when they also retain growth near neutral pH. | moderate acidophiles grow optimally "from pH 3 to 5" and "maintain a circumneutral intracellular pH" (gonzalez2024acidophilicheterotrophsbasic pages 1-2) | DOI:10.3389/fmicb.2024.1374800; May 2024; https://doi.org/10.3389/fmicb.2024.1374800 | uncertain | METPO:1003007 / label:circumneutral intracellular pH |


*Table: This table compiles evidence-backed candidate causal edges relevant to facultatively acidophilic microbes, focusing on pH homeostasis mechanisms, membrane adaptations, proton-consuming pathways, and recent systems-level findings. It is structured for direct TraitMech curation and highlights where evidence is strong versus still taxon-specific or inferred.*


### 5) Recent developments and latest research (prioritizing 2023–2024)

#### 5.1 Systems-level gene inventories from acidic environments (2023)

A 2023 review of eurypsychrophilic acidophiles compiles gene-level mechanisms observed in genomes/MAGs from acidic systems, including multiple **K+ uptake systems (kdp variants; voltage-gated K+ channel)**, **Na+/H+ antiport (nhaA)**, **proton-consuming pathways (gadABC; speA)**, **urease (ureABCDEFGHJ)**, and membrane remodeling modules (**cfa; hopanoid genes hpnAIJKNHM; shc**) as part of low-pH adaptation toolkits. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

#### 5.2 General pH homeostasis synthesis including structural/transport advances (2024)

A 2024 review on microbial pH homeostasis emphasizes recurring roles of **amino-acid decarboxylase systems (gadA/gadBC), urease**, and **antiporters including NhaA and Mrp-type cation/proton antiporters**, and highlights membrane composition changes (e.g., cyclopropane/branched fatty acids) as strategies to reduce H+ permeability. (nie2024researchprogressin pages 11-12)

#### 5.3 Engineered evidence linking specific modules to mild-acid growth performance (2024)

A 2024 study of an engineered acid-tolerant *E. coli* strain explicitly distinguishes acid-stress regimes and provides quantitative performance under mild acid stress:

* Definitions: extreme acid stress **external pH 2–3, internal pH ~4.5**; moderate/acid-resistance response **external pH 4–5, internal pH ~7.0**; mild acid stress **external pH 5–6, internal pH ~7.4**. (qin2024characterizationofmild pages 1-2)
* A synthetic module combining **gadE** (proton-consuming acid resistance), **hdeB** (periplasmic chaperone), and ROS scavengers is associated with improved growth; at **pH 6.0**, final OD600 was **131%** and **124%** of the parent strain under respective comparisons. (qin2024characterizationofmild pages 1-2)

These results are useful for curating edges that connect **regulatory control (GadE)** and **periplasmic proteostasis (HdeB)** to **growth under mildly acidic conditions**, which is mechanistically relevant for “facultative” acidophily (growth at acidic pH without sacrificing near-neutral growth).

#### 5.4 Acidophilic sulfate-reducing bacteria (aSRB) and AMD applications (2024)

A 2024 review on acidophilic sulfate-reducing bacteria (aSRB) emphasizes adaptations such as **proton impermeability and Donnan potential**, and discusses AMD treatment (often **pH <3**) leveraging sulfide generation and metal precipitation. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2)


### 6) Current applications and real-world implementations

1. **AMD / acidic pit-lake remediation and metal sulfide precipitation**
   * aSRB are highlighted for AMD treatment (pH <3) via production of biogenic sulfide and metal precipitation, and can raise local pH via bicarbonate production. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2)

2. **Biomining / saline bioleaching settings**
   * Comparative genomics work on *Acidihalobacter* highlights acid tolerance gene repertoires relevant to industrial contexts (copper bioleaching), including potassium transporters, antiporters, decarboxylase systems, urease, and membrane stabilizing components (hopanoids/squalene). (boase2022predictionandinferred pages 1-2)

3. **Low-pH fermentation constraints and motivations for engineering**
   * A 2024 *E. coli* acid stress review notes industrial fermentations often face pH drops (e.g., below 5.0), and provides an illustrative statistic: **~50 g/L organic acids with pKa 3–5 can lower pH to ~2.0 without alkali addition**, motivating low-pH tolerant production strains to reduce neutralization costs. (li2024responseofescherichia pages 1-2)


### 7) Relevant statistics/data extracted from the retrieved studies

* **Proton gradient magnitude:** acidophiles maintain near-neutral cytoplasm against an external-to-internal proton gradient **up to 10^5-fold**. (gonzalezrosales2022integrativegenomicssheds pages 1-2)
* **pH regime definitions for mild vs extreme acid stress in bacteria (E. coli-specific):** external **pH 2–3** (internal ~4.5) vs **pH 5–6** (internal ~7.4). (qin2024characterizationofmild pages 1-2)
* **Engineered mild-acid growth outcome:** final OD600 at **pH 6.0** was **131%** and **124%** of parent strain comparisons in engineered *E. coli*. (qin2024characterizationofmild pages 1-2)
* **AMD/pit-lake field pH values:** pit-lake zones **pH 2.9–4.8**; chemocline **pH 3.9**; deep layer **pH 4.5**; microcosms **pH 3.2–3.3**; porewater **pH 2.6–3.0** with sulfate 9.0–16.2 mM in one study; sulfate concentrations up to **125–126 mM** reported. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2)
* **Community abundance metric:** aSRB reported as sometimes **<15%** of microbial communities in acidic habitats. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2)


### 8) Expert opinions / analysis (authoritative syntheses)

* **“First-line vs second-line” defense framing** (acidophiles as a lifestyle): comparative-genomics syntheses emphasize that evolution of acidophily involves (i) preventing proton influx (membrane modifications, inside-positive potential) and (ii) proton removal/neutralization (pumps, antiporters, proton-consuming enzymes), with gene redundancy and HGT contributing to robustness in fluctuating acidic environments. (gonzalezrosales2022integrativegenomicssheds pages 1-2)
* **Mechanistic convergence across taxa:** reviews note common motifs—K+ accumulation, antiporters, decarboxylases, urease, and membrane remodeling—reused across multiple lineages and contexts (acidic mines, gut, engineered chassis), suggesting these are high-priority candidate nodes/edges for curation. (nie2024researchprogressin pages 11-12, dopson2023eurypsychrophilicacidophilesfrom pages 8-9, qin2024characterizationofmild pages 1-2)


### 9) Ontology grounding suggestions (CURIE-first where feasible)

Grounding in the retrieved texts is partial; below are **safe, stable** CURIE suggestions where identifiers are unambiguous:

* **METPO:** METPO:1003007 (facultatively acidophilic) [provided]
* **CHEBI:** potassium ion (CHEBI:29103); chloride (CHEBI:17996); sulfate (CHEBI:16189); bicarbonate (CHEBI:17544); urea (CHEBI:16199); glutamate (CHEBI:29991); GABA (CHEBI:16865); spermidine (CHEBI:15746)
* **KEGG pathway (process grounding):** oxidative phosphorylation (ko00190); ABC transporters (ko02010)
* **GO (process candidates; verify exact match during curation):** proton transmembrane transport (GO:1902600) / ATP synthesis coupled proton transport (GO:0015986) / ion transmembrane transport (GO:0034220) / cellular pH homeostasis (GO:0030641)

For gene/protein systems (Kdp, Mrp, NhaA, ClcA, Gad, urease, HdeB), stable grounding could be done via **UniProt accessions** once a target taxon/genome is selected; at the trait-level, node labels may remain generic.


### 10) Warnings / items not yet ready for curation

1. **Species-level exemplar DOI currently unobtainable in this run:** the template cites DOI:10.1099/ijs.0.066175-0 (species with growth pH 4.0–7.2), but full text was not available via tools here; therefore **do not curate** that specific numeric growth range into the graph without verifying the primary source.

2. **Trait vs stress-response mismatch risk:** Many sources address **acid stress response** in neutralophiles (e.g., *E. coli*), which is mechanistically relevant but not identical to **acidophilic growth preference**; edges drawn from such systems should be marked taxon- and assay-specific unless corroborated in acidophiles/facultative acidophiles. (li2024responseofescherichia pages 1-2, qin2024characterizationofmild pages 1-2)

3. **Uncertain ontology IDs:** Several membrane-potential and “proton-impermeable membrane” nodes are not uniquely grounded to a single ontology term in the retrieved context; keep them as labeled nodes until grounded.


---

## DOI-first bibliography (with URLs and publication dates where available)

* Dopson M, González-Rosales C, Holmes DS, Mykytczuk N. **Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies.** *Frontiers in Microbiology* (Mar 2023). DOI:10.3389/fmicb.2023.1149903. https://doi.org/10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
* Yao X, Wang J, Hu B. **How methanotrophs respond to pH: A review of ecophysiology.** *Frontiers in Microbiology* (Jan 2023). DOI:10.3389/fmicb.2022.1034164. https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7)
* González E, Vera F, Scott F, et al. **Acidophilic heterotrophs: basic aspects and technological applications.** *Frontiers in Microbiology* (May 2024). DOI:10.3389/fmicb.2024.1374800. https://doi.org/10.3389/fmicb.2024.1374800 (gonzalez2024acidophilicheterotrophsbasic pages 1-2)
* Li Z, Huang Z, Gu P. **Response of *Escherichia coli* to Acid Stress: Mechanisms and Applications—A Narrative Review.** *Microorganisms* (Aug 2024). DOI:10.3390/microorganisms12091774. https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 1-2)
* Qin J, Guo H, Wu X, et al. **Characterization of Mild Acid Stress Response in an Engineered Acid-Tolerant *Escherichia coli* Strain.** *Microorganisms* (Jul 2024). DOI:10.3390/microorganisms12081565. https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2)
* Valdez-Nuñez LF, Kappler A, Ayala-Muñoz D, Chávez IJ, Mansor M. **Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.** *Environmental Microbiology Reports* (Oct 2024). DOI:10.1111/1758-2229.70019. https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2)
* Nie M, Yang Y, Li Z. **Research progress in the mechanisms of maintaining intracellular and extracellular pH homeostasis in microorganisms.** (2024). DOI:10.13343/j.cnki.wsxb.20230336. https://doi.org/10.13343/j.cnki.wsxb.20230336 (nie2024researchprogressin pages 11-12)
* Boase K, González C, Vergara E, Neira G, Holmes D, Watkin E. **Prediction and inferred evolution of acid tolerance genes in the biotechnologically important *Acidihalobacter* genus.** *Frontiers in Microbiology* (Apr 2022). DOI:10.3389/fmicb.2022.848410. https://doi.org/10.3389/fmicb.2022.848410 (boase2022predictionandinferred pages 1-2, boase2022predictionandinferred pages 2-3)
* González-Rosales C, Vergara E, Dopson M, Valdés JH, Holmes DS. **Integrative genomics sheds light on evolutionary forces shaping the Acidithiobacillia class acidophilic lifestyle.** *Frontiers in Microbiology* (Feb 2022). DOI:10.3389/fmicb.2021.822229. https://doi.org/10.3389/fmicb.2021.822229 (gonzalezrosales2022integrativegenomicssheds pages 1-2)
* Vergara E, Neira G, González C, et al. **Evolution of predicted acid resistance mechanisms in the extremely acidophilic *Leptospirillum* genus.** *Genes* (Apr 2020). DOI:10.3390/genes11040389. https://doi.org/10.3390/genes11040389 (vergara2020evolutionofpredicted pages 16-17, vergara2020evolutionofpredicted pages 1-3)



References

1. (gonzalez2024acidophilicheterotrophsbasic pages 1-2): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 7 citations and is from a peer-reviewed journal.

2. (gonzalezrosales2022integrativegenomicssheds pages 1-2): Carolina González-Rosales, Eva Vergara, Mark Dopson, Jorge H. Valdés, and David S. Holmes. Integrative genomics sheds light on evolutionary forces shaping the acidithiobacillia class acidophilic lifestyle. Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2021.822229, doi:10.3389/fmicb.2021.822229. This article has 32 citations and is from a peer-reviewed journal.

3. (vergara2020evolutionofpredicted pages 1-3): Eva Vergara, Gonzalo Neira, Carolina González, Diego Cortez, Mark Dopson, and David S. Holmes. Evolution of predicted acid resistance mechanisms in the extremely acidophilic leptospirillum genus. Genes, 11:389, Apr 2020. URL: https://doi.org/10.3390/genes11040389, doi:10.3390/genes11040389. This article has 39 citations.

4. (li2024responseofescherichia pages 1-2): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

5. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

6. (vergara2020evolutionofpredicted pages 16-17): Eva Vergara, Gonzalo Neira, Carolina González, Diego Cortez, Mark Dopson, and David S. Holmes. Evolution of predicted acid resistance mechanisms in the extremely acidophilic leptospirillum genus. Genes, 11:389, Apr 2020. URL: https://doi.org/10.3390/genes11040389, doi:10.3390/genes11040389. This article has 39 citations.

7. (nie2024researchprogressin pages 11-12): M NIE, Y YANG, and Z LI. Research progress in the mechanisms of maintaining intracellular and extracellular ph homeostasis in microorganisms. Unknown journal, 2024. URL: https://doi.org/10.13343/j.cnki.wsxb.20230336, doi:10.13343/j.cnki.wsxb.20230336.

8. (qin2024characterizationofmild pages 1-2): Jingliang Qin, Han Guo, Xiaoxue Wu, Shuai Ma, Xin Zhang, Xiaofeng Yang, Bin Liu, Lu Feng, Huanhuan Liu, and Di Huang. Characterization of mild acid stress response in an engineered acid-tolerant escherichia coli strain. Microorganisms, 12:1565, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081565, doi:10.3390/microorganisms12081565. This article has 2 citations.

9. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

10. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 1-2): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

11. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

12. (boase2022predictionandinferred pages 1-2): Katelyn Boase, Carolina González, Eva Vergara, Gonzalo Neira, David Holmes, and Elizabeth Watkin. Prediction and inferred evolution of acid tolerance genes in the biotechnologically important acidihalobacter genus. Frontiers in Microbiology, Apr 2022. URL: https://doi.org/10.3389/fmicb.2022.848410, doi:10.3389/fmicb.2022.848410. This article has 22 citations and is from a peer-reviewed journal.

13. (boase2022predictionandinferred pages 2-3): Katelyn Boase, Carolina González, Eva Vergara, Gonzalo Neira, David Holmes, and Elizabeth Watkin. Prediction and inferred evolution of acid tolerance genes in the biotechnologically important acidihalobacter genus. Frontiers in Microbiology, Apr 2022. URL: https://doi.org/10.3389/fmicb.2022.848410, doi:10.3389/fmicb.2022.848410. This article has 22 citations and is from a peer-reviewed journal.