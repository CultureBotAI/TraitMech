---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:22:56.209845'
end_time: '2026-06-17T23:37:38.439759'
duration_seconds: 882.23
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl range high
  trait_identifier: METPO:1000472
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_range_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl range phenotype in which the growth-supporting NaCl range extends
    above approximately 8% (w/v), characteristic of extreme-halophile organisms.
  parent_traits: METPO:1000334
  synonyms: Extreme halophile, NaR_>8
  evidence_summary: 'DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation
    review supports growth ranges extending above 8% NaCl as the extreme-halophile
    category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum
    (Saline-Systems review supports salt-in physiology underlying extended high-salt
    growth.)'
  causal_graph_summary: 'nacl_range_high_extreme_halophile: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range high
- **METPO identifier:** METPO:1000472
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range extends above approximately 8% (w/v), characteristic of extreme-halophile organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Extreme halophile, NaR_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports growth ranges extending above 8% NaCl as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports salt-in physiology underlying extended high-salt growth.)
- **Existing causal graph summary:** nacl_range_high_extreme_halophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_high.yaml`.

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
- **Trait label:** NaCl range high
- **METPO identifier:** METPO:1000472
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range extends above approximately 8% (w/v), characteristic of extreme-halophile organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Extreme halophile, NaR_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports growth ranges extending above 8% NaCl as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports salt-in physiology underlying extended high-salt growth.)
- **Existing causal graph summary:** nacl_range_high_extreme_halophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_high.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **NaCl range high** (METPO:1000472)

### Publication focus
This report prioritizes 2024 peer‑reviewed sources for mechanisms and quantitative salinity phenotypes, and uses high-authority reviews/chapters for foundational definitions and classification boundaries. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, xing2024thepolyextremophilenatranaerobius pages 1-2, khanh2024metabolicpathwayengineering pages 1-2, ionescu2024extremefluctuationsin pages 1-2)

---

## 1) Scope summary (trait meaning, boundaries, and distinctions)

### Trait definition (curation intent)
**NaCl range high (METPO:1000472)** represents a **growth-supporting NaCl range whose upper bound extends above ~8% (w/v)**, aligning with **extreme halophily** in many classification systems and with organisms thriving in brines that approach salt saturation. The trait is about **growth range** (not merely survival) and is most often realized by organisms adapted to **very high ionic strength and low water activity** habitats such as saltern crystallizers and salt-saturating brines. (lee2018naclsaturatedbrinesare pages 12-15, gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

### How “extreme halophile” is defined in the literature (useful thresholds)
Classification schemes vary (optimum vs requirement vs range), so curating the trait should explicitly capture that **METPO:1000472 uses an upper growth-range criterion (>~8% w/v NaCl)** rather than solely optimum.

* **Optimum-based schemes**: One scheme classifies halophiles by **optimal** NaCl: mild 1–6%, moderate 7–15%, extreme 15–30%. (Cira‑Chávez 2019; DOI:10.5772/intechopen.81100) (cirachavez2019kineticsofhalophilic pages 1-3)
* **Molarity-based schemes**: Another scheme defines **extreme halophiles** around **2.5–5.2 M NaCl**, and provides example organism growth ranges (e.g., *Halobacterium salinarum* 2.4–5.2 M NaCl). (Bartha 2022 excerpt) (bartha2022investigatingextremotolerantmicrobes pages 21-25, bartha2022investigatingextremotolerantmicrobes pages 25-28)
* **Community transition threshold**: In saltern systems, there is evidence for a community transition around **~3.4 M NaCl**, separating moderate and high-salt communities, indicating that above this range selection strongly favors extreme halophily. (Lee 2018; DOI:10.1093/femsre/fuy026) (lee2018naclsaturatedbrinesare pages 12-15)
* **Salt-saturating environments**: Solar saltern crystallizers are described as **“salinity above 30%‑w/v”** environments where extremely halophilic archaea use salt-in strategies. (Gutiérrez‑Preciado 2024; DOI:10.1038/s41559-024-02505-6) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

### Boundary cases to distinguish during curation
* **Halotolerant vs halophilic**: Halotolerant organisms can grow in salt but do **not require** it; this differs mechanistically and ecologically from extreme halophiles that typically require high salt. (bartha2022investigatingextremotolerantmicrobes pages 21-25, bartha2022investigatingextremotolerantmicrobes pages 25-28)
* **Upper range vs optimum**: Some organisms have broad ranges that include >8% w/v but do not have “extreme” optima; engineering studies explicitly show that changing osmolyte pathways shifts the **upper limit** of growth (e.g., enabling growth at 8% NaCl). (khanh2024metabolicpathwayengineering pages 1-2)
* **NaCl vs total dissolved salts / non‑NaCl brines**: Some extreme systems are dominated by chaotropic salts (Mg/Ca/Li/Fe) and very high total salinity; NaCl-range phenotypes may not fully capture these. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

---

## 2) Current understanding: core concepts and mechanisms

### Concept A: Osmoregulation strategies
Two canonical strategies are repeatedly emphasized:

1. **“Salt‑in” strategy**: cells accumulate **inorganic ions (mainly K+ with Cl−) to molar levels** to balance external osmotic pressure; intracellular machinery is adapted to high ionic strength. (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4, ionescu2024extremefluctuationsin pages 1-2)
2. **“Salt‑out/compatible‑solute” strategy**: cells maintain relatively lower intracellular salt and instead accumulate **organic compatible solutes** (e.g., glycine betaine, trehalose, proline, ectoine). (bartha2022investigatingextremotolerantmicrobes pages 25-28, ionescu2024extremefluctuationsin pages 1-2)

A notable modern development is the recognition of **hybrid strategies** in some bacteria under fluctuating salinity regimes. (xing2024thepolyextremophilenatranaerobius pages 1-2, ionescu2024extremefluctuationsin pages 1-2)

### Concept B: Proteome acidification as a salt-in signature
A consistent mechanistic theme in extreme halophily is **proteome acidification**:
* Extremely halophilic archaea in salt-saturating environments accumulate **molar K+** and exhibit **acidic proteomes enriched in Asp/Glu**, facilitating protein solubility and function at high ionic strength. (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
* In Danakil brines, metagenome/MAG-inferred proteomes were described as **“the most acidic proteomes ever observed”** (median pI ≤ 4.4) in near life-limiting brines, supporting proteome acidification as a major axis of adaptation. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

### Concept C: Compatible solutes (chemistry and function)
Compatible solutes support high-salt growth by stabilizing macromolecules; osmolytes are described as **protein stabilizers/chaperones** and influence hydration/aggregation behaviors. (ghosh2019microbialdiversityof pages 13-15)

---

## 3) Recent developments (prioritized 2023–2024)

### 3.1 Hybrid salt-in/salt-out selection in fluctuating hypersaline environments (2024)
Dead Sea spring biofilms experience strong, rapid salinity changes (ambient waters sometimes **>35% total dissolved salts**) and select for organisms with **hybrid “salt‑in”/“salt‑out”** capacity; MAGs contained genes for both strategies. (Ionescu 2024; DOI:10.3389/frmbi.2023.1329925) (ionescu2024extremefluctuationsin pages 1-2)

### 3.2 Multi-omics evidence for dual strategy + transporter families (2024)
In *Natranaerobius thermophilus* (extremely halophilic alkalithermophile), growth occurs between **3.1–4.9 M Na+** (optimum **3.3–3.9 M**), and experimental conditions (2.5–4.3 M) are explicitly mapped to **14.63%–25.16% (wt/vol) Na+**. The organism uses a hybrid adaptation strategy with increasing intracellular **glycine betaine, glutamate, and proline**, while also supporting intracellular K+ homeostasis. Mechanistic entities include **Opu/ProU ABC transporters**, **SSS-family Na+/solute symporters**, and **Na+/K+/H+ transporters**, plus evidence for more acidic proteome characteristics with salinity. (Xing 2024; DOI:10.1128/aem.00145-24) (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 10-14)

### 3.3 Genetic causality for osmolytes shifting upper NaCl growth limits (2024)
A directly curation-relevant engineering result shows causal links between osmolyte genetics and high-NaCl growth:
* *Halomonas elongata* OUT30018: growth across **0.3%–21% (w/v) NaCl**.
* An ectoine-deficient derivative fails above **4% NaCl**.
* An engineered proline-overproducing strain **thrives at 8% NaCl** while accumulating intracellular proline to **353.1 ± 40.5 µmol/g cell fresh weight**.
* Genetic entities: **ectABC** operon replacement; **proB/proA/proC** (proline biosynthesis enzymes); **putA** (proline catabolism) deletion. (Khanh 2024; DOI:10.1128/aem.01195-24) (khanh2024metabolicpathwayengineering pages 1-2)

### 3.4 Extreme halophily in salt-saturating and hyper-saline brines (2024)
In Danakil chaotropic brines, salinity spans roughly **~30 to >70% w/v**, and extremely halophilic archaea dominate in near life-limiting conditions; adaptation includes **molar cytoplasmic K+ (up to ~4 M)** and strong proteome acidification (median pI ≤4.4). (Gutiérrez‑Preciado 2024; DOI:10.1038/s41559-024-02505-6) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

---

## 4) Candidate nodes (grouped by type; ontology grounding where available)

A curation-ready node inventory is provided here:

| Node label | Node type | Suggested ontology grounding | Evidence/supporting source(s) |
|---|---|---|---|
| **Environmental/assay factors** |  |  |  |
| high external NaCl / hypersaline brine | environmental factor | CHEBI:26710 sodium chloride | (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| extreme salinity fluctuations | environmental factor | label-only | (ionescu2024extremefluctuationsin pages 1-2) |
| salt-saturating saltern crystallizers (>30% w/v salinity) | environment | ENVO:00000304 saltern, label-only for salt-saturating condition | (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| growth range 3.1–4.9 M Na+ (optimum 3.3–3.9 M) | assay/growth metric | label-only | (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| growth range 0.3–21% NaCl for *Halomonas elongata* OUT30018 | assay/growth metric | label-only | (khanh2024metabolicpathwayengineering pages 1-2) |
| **Osmoregulation strategies/processes** |  |  |  |
| salt-in strategy | biological process/strategy | label-only | (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4, ionescu2024extremefluctuationsin pages 1-2) |
| salt-out / compatible-solute strategy | biological process/strategy | label-only | (bartha2022investigatingextremotolerantmicrobes pages 25-28, ionescu2024extremefluctuationsin pages 1-2) |
| hybrid salt-in/salt-out osmoregulation | biological process/strategy | label-only | (xing2024thepolyextremophilenatranaerobius pages 1-2, ionescu2024extremefluctuationsin pages 1-2) |
| compatible-solute accumulation | biological process | GO:0006970 response to osmotic stress | (bartha2022investigatingextremotolerantmicrobes pages 25-28, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| intracellular K+ accumulation / ion homeostasis | biological process | GO:0055075 potassium ion homeostasis | (xing2024thepolyextremophilenatranaerobius pages 10-14, gutierrezpreciado2024extremelyacidicproteomes pages 1-4, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| glutamate synthesis pathway | metabolic pathway | label-only | (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| proline synthesis pathway | metabolic pathway | label-only | (xing2024thepolyextremophilenatranaerobius pages 1-2, khanh2024metabolicpathwayengineering pages 1-2) |
| **Chemicals/metabolites/ions** |  |  |  |
| NaCl | chemical | CHEBI:26710 sodium chloride | (lee2018naclsaturatedbrinesare pages 15-17, khanh2024metabolicpathwayengineering pages 1-2) |
| K+ | ion | CHEBI:29103 potassium(1+) | (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Cl- | ion | CHEBI:17996 chloride | (bartha2022investigatingextremotolerantmicrobes pages 25-28) |
| KCl | chemical | CHEBI:32588 potassium chloride | (bartha2022investigatingextremotolerantmicrobes pages 25-28) |
| glycine betaine | compatible solute | CHEBI:17750 glycine betaine | (bartha2022investigatingextremotolerantmicrobes pages 25-28, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| glutamate | compatible solute/metabolite | CHEBI:29985 glutamate | (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| proline | compatible solute/metabolite | CHEBI:26271 L-proline | (bartha2022investigatingextremotolerantmicrobes pages 25-28, xing2024thepolyextremophilenatranaerobius pages 1-2, khanh2024metabolicpathwayengineering pages 1-2) |
| ectoine | compatible solute | CHEBI:27887 ectoine | (bartha2022investigatingextremotolerantmicrobes pages 25-28, khanh2024metabolicpathwayengineering pages 1-2) |
| trehalose | compatible solute | CHEBI:16551 trehalose | (bartha2022investigatingextremotolerantmicrobes pages 25-28, ionescu2024extremefluctuationsin pages 1-2) |
| glycerol | compatible solute/polyol | CHEBI:17522 glycerol | (bartha2022investigatingextremotolerantmicrobes pages 25-28, lee2018naclsaturatedbrinesare pages 15-17) |
| **Transporters/complexes** |  |  |  |
| Opu-family glycine betaine ABC transporters | transporter family | label-only | (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| ProU-family glycine betaine ABC transporters | transporter family | label-only | (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| SSS-family Na+/solute symporters | transporter family | label-only | (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Na+/K+/H+ transporters | transporter family/complex | label-only | (xing2024thepolyextremophilenatranaerobius pages 10-14, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Na+-translocating FOF1-ATPase | enzyme complex | label-only | (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| **Genes/operons** |  |  |  |
| ectABC operon | gene cluster | label-only | (khanh2024metabolicpathwayengineering pages 1-2) |
| proB | gene | label-only | (khanh2024metabolicpathwayengineering pages 1-2) |
| proA | gene | label-only | (khanh2024metabolicpathwayengineering pages 1-2) |
| proC | gene | label-only | (khanh2024metabolicpathwayengineering pages 1-2) |
| putA | gene | label-only | (khanh2024metabolicpathwayengineering pages 1-2) |
| **Protein/proteome properties** |  |  |  |
| acidic proteome | proteome property | label-only | (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| low proteome isoelectric point (low pI) | proteome property | label-only | (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| acidic residue enrichment (Asp/Glu-rich proteins) | protein property | CHEBI:29958 aspartate, CHEBI:29985 glutamate | (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| high protein hydrophilicity / negatively charged surface | protein property | label-only | (lee2018naclsaturatedbrinesare pages 15-17) |
| **Example taxa/contexts** |  |  |  |
| *Natranaerobius thermophilus* | example taxon | NCBITaxon:label-only | (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| *Halomonas elongata* OUT30018 / engineered HN6 | example taxon/context | NCBITaxon:label-only | (khanh2024metabolicpathwayengineering pages 1-2) |
| haloarchaea in salt-saturating systems | example taxonomic/ecological context | label-only | (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| Dead Sea spring biofilms | ecological context | ENVO:label-only | (ionescu2024extremefluctuationsin pages 1-2) |


*Table: This table lists curation-ready candidate nodes for a causal graph of the NaCl range high trait, grouped by entity type and restricted to evidence-supported concepts from the gathered sources. It is useful as a starting node inventory for TraitMech YAML curation and ontology grounding.*

---

## 5) Evidence-backed candidate causal edges (triples)

A curation-ready edge table (with supporting snippets, DOI/URL, and scope/uncertainty notes) is provided here:

| Edge (subject–predicate–object) | Node types (S/O) | Suggested ontology grounding for subject/object | Evidence snippet (verbatim short quote) | Reference (first author, year, journal) | DOI + URL | Notes on scope/uncertainty |
|---|---|---|---|---|---|---|
| high external NaCl / hypersaline brine – induces – intracellular K+ accumulation (“salt-in” strategy) | environmental condition / chemical | Subject: high NaCl hypersaline environment [label-only]; Object: CHEBI:29103 potassium(1+) | “the canonical osmoadaptive ‘salt-in’ strategy involves accumulating molar cytoplasmic K+ (reported here up to 4M K+)” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | Gutiérrez-Preciado, 2024, Nat Ecol Evol | 10.1038/s41559-024-02505-6 https://doi.org/10.1038/s41559-024-02505-6 | Broad; strongest for extremely halophilic archaea in salt-saturating systems. |
| salt-in strategy – results in – acidic proteome | biological process / molecular quality | Subject: GO:0006970 response to osmotic stress [approx. label-only for salt-in strategy]; Object: acidic proteome [label-only] | “accumulating molar cytoplasmic K+ … accompanied by proteome acidification through enrichment in acidic amino acids (glutamate/aspartate)” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | Gutiérrez-Preciado, 2024, Nat Ecol Evol | 10.1038/s41559-024-02505-6 https://doi.org/10.1038/s41559-024-02505-6 | Broad; mechanism-level summary, not a single gene edge. |
| acidic amino acid enrichment (Asp/Glu) – contributes to – protein functionality at very high ionic strength | chemical property / biological process | Subject: CHEBI:29958 aspartate, CHEBI:29985 glutamate; Object: protein function at high ionic strength [label-only] | “Salt-in intracellular proteins are more hydrophilic and enriched in acidic residues (glutamate, aspartate), producing negatively charged surfaces that enable functionality at very high ionic strength.” (lee2018naclsaturatedbrinesare pages 15-17) | Lee, 2018, FEMS Microbiol Rev | 10.1093/femsre/fuy026 https://doi.org/10.1093/femsre/fuy026 | Broad review language; curate as physiochemical adaptation, not universal causal sufficiency. |
| extreme halophile physiology – depends on – high intracellular K+ | phenotype / chemical | Subject: METPO:1000472 NaCl range high; Object: CHEBI:29103 potassium(1+) | “Cellular vitality of salt-in organisms is dependent on high intracellular K+ (with many proteins misfolding when K+ falls below ~2.2 M).” (lee2018naclsaturatedbrinesare pages 15-17) | Lee, 2018, FEMS Microbiol Rev | 10.1093/femsre/fuy026 https://doi.org/10.1093/femsre/fuy026 | Broad; specifically salt-in organisms, not all high-NaCl-range taxa. |
| extreme halophile / salt-in organism – accumulates – KCl | organismal strategy / chemical | Subject: salt-in organism [label-only]; Object: CHEBI:32588 potassium chloride | “the salt-in strategy accumulates high intracellular K+ and Cl- (~4.5 M KCl)” (bartha2022investigatingextremotolerantmicrobes pages 25-28) | Bartha, 2022, thesis excerpt | URL not available in gathered evidence | Broad, review-style summary; taxon examples include Halobacteria, Salinibacter, Halanaerobiales. |
| compatible-solute strategy – accumulates – glycine betaine | biological process / chemical | Subject: compatible-solute strategy [label-only]; Object: CHEBI:17750 glycine betaine | “biosynthesizes or imports organic osmolytes (e.g., proline, glycerol, glycine betaine, ectoine, DMSP, sucrose, trehalose)” (bartha2022investigatingextremotolerantmicrobes pages 25-28) | Bartha, 2022, thesis excerpt | URL not available in gathered evidence | Broad; applies to salt-out taxa, not specifically all extreme halophiles. |
| compatible-solute strategy – accumulates – ectoine | biological process / chemical | Subject: compatible-solute strategy [label-only]; Object: CHEBI:27887 ectoine | “biosynthesizes or imports organic osmolytes (e.g., proline, glycerol, glycine betaine, ectoine” (bartha2022investigatingextremotolerantmicrobes pages 25-28) | Bartha, 2022, thesis excerpt | URL not available in gathered evidence | Broad; often more relevant to halophilic bacteria than haloarchaea. |
| high salinity in Natranaerobius thermophilus – increases intracellular – glycine betaine | environmental condition / chemical | Subject: high salinity [label-only]; Object: CHEBI:17750 glycine betaine | “intracellular glycine betaine, glutamate, and proline increase with salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing, 2024, Appl Environ Microbiol | 10.1128/aem.00145-24 https://doi.org/10.1128/aem.00145-24 | Taxon-specific (N. thermophilus); strong experimental evidence. |
| high salinity in Natranaerobius thermophilus – increases intracellular – glutamate | environmental condition / chemical | Subject: high salinity [label-only]; Object: CHEBI:29985 glutamate | “intracellular glycine betaine, glutamate, and proline increase with salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing, 2024, Appl Environ Microbiol | 10.1128/aem.00145-24 https://doi.org/10.1128/aem.00145-24 | Taxon-specific (N. thermophilus). |
| high salinity in Natranaerobius thermophilus – increases intracellular – proline | environmental condition / chemical | Subject: high salinity [label-only]; Object: CHEBI:26271 L-proline | “intracellular glycine betaine, glutamate, and proline increase with salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing, 2024, Appl Environ Microbiol | 10.1128/aem.00145-24 https://doi.org/10.1128/aem.00145-24 | Taxon-specific (N. thermophilus). |
| Opu-family ABC transporters – contribute to – adaptation to high salinity | transporter family / phenotype | Subject: Opu family glycine betaine ABC transporters [label-only]; Object: high-salinity adaptation [label-only] | “Identified mechanistic entities include glycine betaine ABC transporters (Opu and ProU families)” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing, 2024, Appl Environ Microbiol | 10.1128/aem.00145-24 https://doi.org/10.1128/aem.00145-24 | Taxon-specific; family-level grounding only. |
| ProU-family ABC transporters – contribute to – adaptation to high salinity | transporter family / phenotype | Subject: ProU family transporter [label-only]; Object: high-salinity adaptation [label-only] | “Identified mechanistic entities include glycine betaine ABC transporters (Opu and ProU families)” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing, 2024, Appl Environ Microbiol | 10.1128/aem.00145-24 https://doi.org/10.1128/aem.00145-24 | Taxon-specific; family-level grounding only. |
| SSS-family Na+/solute symporters – contribute to – adaptation to high salinity | transporter family / phenotype | Subject: SSS family Na+/solute symporter [label-only]; Object: high-salinity adaptation [label-only] | “Identified mechanistic entities include … Na+/solute symporters (SSS family)” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing, 2024, Appl Environ Microbiol | 10.1128/aem.00145-24 https://doi.org/10.1128/aem.00145-24 | Taxon-specific; transporter family mentioned without locus IDs. |
| Na+/K+/H+ transporters – maintain – intracellular K+ homeostasis under varying salinities | transporter / biological process | Subject: Na+/K+/H+ transporter [label-only]; Object: K+ homeostasis [label-only] | “the upregulation of Na+/ K+/ H+ transporters facilitates the maintenance of intracellular K+ concentration, ensuring cellular ion homeostasis under varying salinities” (xing2024thepolyextremophilenatranaerobius pages 10-14) | Xing, 2024, Appl Environ Microbiol | 10.1128/aem.00145-24 https://doi.org/10.1128/aem.00145-24 | Taxon-specific; strong mechanistic statement but family/subunit IDs not provided in excerpt. |
| high salinity in Natranaerobius thermophilus – causes – shift toward more acidic proteome | environmental condition / molecular quality | Subject: high salinity [label-only]; Object: acidic proteome [label-only] | “The organism exhibits cytoplasmic acidification and a shift toward more acidic proteomes (median isoelectric points decrease with salinity)” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing, 2024, Appl Environ Microbiol | 10.1128/aem.00145-24 https://doi.org/10.1128/aem.00145-24 | Taxon-specific; supports convergence with salt-in logic. |
| fluctuating extreme salinity – selects for – hybrid salt-in/salt-out osmoregulation | environmental condition / physiological strategy | Subject: extreme salinity fluctuations [label-only]; Object: hybrid salt-in/salt-out strategy [label-only] | “extreme and rapid salinity fluctuations … select for organisms capable of using both strategies” (ionescu2024extremefluctuationsin pages 1-2) | Ionescu, 2024, Front Microbiomes | 10.3389/frmbi.2023.1329925 https://doi.org/10.3389/frmbi.2023.1329925 | Broad for fluctuating environments; not a defining feature of all extreme halophiles. |
| high salinity in Halomonas elongata – induces accumulation of – ectoine | environmental condition / chemical | Subject: high salinity [label-only]; Object: CHEBI:27887 ectoine | “H. elongata OUT30018 is a moderately halophilic bacterium that accumulates ectoine (Ect)” (khanh2024metabolicpathwayengineering pages 1-2) | Khanh, 2024, Appl Environ Microbiol | 10.1128/aem.01195-24 https://doi.org/10.1128/aem.01195-24 | Taxon-specific; moderate halophile, included because it illuminates compatible-solute mechanism relevant to high-NaCl growth. |
| ectABC operon deletion/replacement – decreases ability to grow above – 4% NaCl | gene cluster / phenotype | Subject: ectABC operon [label-only]; Object: growth above 4% NaCl [label-only] | “The ect-deficient H. elongata KA1 could not grow in minimal media containing more than 4% NaCl” (khanh2024metabolicpathwayengineering pages 1-2) | Khanh, 2024, Appl Environ Microbiol | 10.1128/aem.01195-24 https://doi.org/10.1128/aem.01195-24 | Taxon-specific engineering evidence; does not directly establish >8% trait in wild taxa. |
| replacement of ectABC with proBm1AC cluster – enables growth at – 8% NaCl | engineered gene replacement / phenotype | Subject: engineered replacement of ectABC with proBm1AC [label-only]; Object: growth at 8% NaCl [label-only] | “H. elongata HN6 thrived in the medium containing 8% NaCl by accumulating Pro” (khanh2024metabolicpathwayengineering pages 1-2) | Khanh, 2024, Appl Environ Microbiol | 10.1128/aem.01195-24 https://doi.org/10.1128/aem.01195-24 | Taxon-specific, engineered, assay-specific; useful mechanistic analogy but not a native extreme-halophile edge. |
| proBm1AC-mediated proline biosynthesis – increases intracellular – proline | engineered pathway / chemical | Subject: proBm1AC / proline biosynthesis pathway [label-only]; Object: CHEBI:26271 L-proline | “accumulating Pro to 353.1 ± 40.5 µmol/g cell fresh weight” (khanh2024metabolicpathwayengineering pages 1-2) | Khanh, 2024, Appl Environ Microbiol | 10.1128/aem.01195-24 https://doi.org/10.1128/aem.01195-24 | Taxon-specific engineering evidence. |
| putA deletion – promotes – proline accumulation under high salinity | gene / chemical | Subject: putA [label-only]; Object: CHEBI:26271 L-proline | “deleted putA to enable Pro accumulation” (khanh2024metabolicpathwayengineering pages 1-2) | Khanh, 2024, Appl Environ Microbiol | 10.1128/aem.01195-24 https://doi.org/10.1128/aem.01195-24 | Taxon-specific, engineered; gene label only because stable strain-specific ID not provided in excerpt. |
| high salinity – induces synthesis of – betaine | environmental condition / chemical | Subject: high salinity [label-only]; Object: CHEBI:17750 glycine betaine | “K. pneumoniae synthesizes betaine across 0.17–3.5 M NaCl while ectoine appears only above 2 M NaCl” (ghosh2019microbialdiversityof pages 13-15) | Ghosh, 2019, Soil Biology chapter | 10.1007/978-3-030-18975-4_4 https://doi.org/10.1007/978-3-030-18975-4_4 | Broad to moderate halophiles/halotolerants; not specific to extreme halophiles. |
| high salinity (>2 M NaCl) – induces synthesis of – ectoine | environmental condition / chemical | Subject: high salinity >2 M NaCl [label-only]; Object: CHEBI:27887 ectoine | “K. pneumoniae synthesizes betaine across 0.17–3.5 M NaCl while ectoine appears only above 2 M NaCl” (ghosh2019microbialdiversityof pages 13-15) | Ghosh, 2019, Soil Biology chapter | 10.1007/978-3-030-18975-4_4 https://doi.org/10.1007/978-3-030-18975-4_4 | Broad; not necessarily extreme-halophile-specific. |
| intracellular compatible solutes – stabilize – proteins/enzymes under salt stress | chemical / biological process | Subject: compatible solutes [label-only]; Object: protein stabilization under osmotic stress [label-only] | “osmolytes act as protein stabilizers/chaperones” (ghosh2019microbialdiversityof pages 13-15) | Ghosh, 2019, Soil Biology chapter | 10.1007/978-3-030-18975-4_4 https://doi.org/10.1007/978-3-030-18975-4_4 | Broad review language; mechanistically relevant but indirect for trait curation. |
| extreme halophile classification – has growth range – 2.5–5.2 M NaCl | phenotype / chemical environment | Subject: METPO:1000472 NaCl range high; Object: NaCl 2.5–5.2 M [label-only] | “extreme halophiles (2.5–5.2 M NaCl)” (bartha2022investigatingextremotolerantmicrobes pages 21-25) | Bartha, 2022, thesis excerpt | URL not available in gathered evidence | Broad classification support; useful for scope, not a mechanistic edge. |
| extreme halophile classification – includes optimum/growth at – 15–30% NaCl | phenotype / chemical environment | Subject: METPO:1000472 NaCl range high; Object: 15–30% NaCl [label-only] | “an optimum-based scheme (mild 1–6%, moderate 7–15%, extreme 15–30%)” (cirachavez2019kineticsofhalophilic pages 1-3) | Cira-Chávez, 2019, IntechOpen chapter | 10.5772/intechopen.81100 https://doi.org/10.5772/intechopen.81100 | Broad classification scheme; note this refers to optimum-based categories, not simply upper range >8% w/v. |


*Table: This table lists curation-ready candidate causal edges for the 'NaCl range high' trait, grounded only in the gathered evidence. It highlights mechanistic links around K+/KCl accumulation, acidic proteomes, compatible solutes, transport systems, and engineered pathway substitutions, while flagging taxon-specific and broad-review claims.*

---

## 6) Visual evidence (figures) supporting mechanistic interpretation

Favreau et al. (2023) report microscopy evidence consistent with ion precipitation/redistribution during acclimation to halite brine inclusions (KCl crystals at halite surface) and provide a schematic of proteomic shifts in *Halobacterium salinarum* during acclimation to brine inclusion microenvironments. These visuals are useful as curation context for the **KCl accumulation / salt‑in physiology** axis (though not a direct gene-level edge). (favreau2023molecularacclimationof media e42a87e3, favreau2023molecularacclimationof media 86c02d7b, favreau2023molecularacclimationof media 8ac1f198)

---

## 7) Current applications and real-world implementations

### 7.1 Halophilic enzymes (extremozymes) in high-salt industrial conditions
Halophilic enzymes are described as having a **high requirement for salt** for biological functions and being useful where processes occur under high salt (e.g., residue treatment in oil deposits under high salt and temperature). (Cira‑Chávez 2019; DOI:10.5772/intechopen.81100) (cirachavez2019kineticsofhalophilic pages 1-3)

### 7.2 Osmolytes as industrial products and enabling technologies
Compatible solutes (e.g., ectoines, betaines, proline, trehalose) are described as stabilizing biomolecules and supporting applications (e.g., stabilizers/cryoprotectants; PCR enhancer for GC-rich templates). A commercialized bioprocess (“bacterial milking”) cycles osmolarity to harvest excreted osmolytes. (Ghosh 2019; DOI:10.1007/978-3-030-18975-4_4) (ghosh2019microbialdiversityof pages 13-15)

### 7.3 Engineering salt tolerance via osmolyte pathways
The 2024 *H. elongata* engineering study provides a modern example of metabolic engineering shifting growth limits and producing **proline-rich biomass** for potential single-cell feed additives, highlighting the mechanistic leverage of osmolyte pathways. (Khanh 2024; DOI:10.1128/aem.01195-24) (khanh2024metabolicpathwayengineering pages 1-2)

---

## 8) Statistics and quantitative data points (recent + authoritative)

* **Salt-saturating saltern crystallizers**: “salinity above **30%‑w/v**”. (Gutiérrez‑Preciado 2024; DOI:10.1038/s41559-024-02505-6) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
* **Danakil brines**: salinity reported as **~30 to >70% w/v** (system-specific). (Gutiérrez‑Preciado 2024) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
* **Natranaerobius thermophilus**: growth **3.1–4.9 M Na+**, optimum **3.3–3.9 M**; experimental salinities mapped to **14.63%–25.16% (wt/vol) Na+**. (Xing 2024; DOI:10.1128/aem.00145-24) (xing2024thepolyextremophilenatranaerobius pages 1-2)
* **Engineered osmolyte causality in *H. elongata***: ectoine-deficient strain fails >**4% NaCl**; engineered proline strain grows at **8% NaCl** and accumulates proline **353.1 ± 40.5 µmol/g cell fresh weight**. (Khanh 2024; DOI:10.1128/aem.01195-24) (khanh2024metabolicpathwayengineering pages 1-2)
* **Community selection threshold**: selection for extreme halophiles around **~3.4 M NaCl** and shift between moderate (<3.5 M) and high-salt (>3.5 M) conditions in saltern systems. (Lee 2018; DOI:10.1093/femsre/fuy026) (lee2018naclsaturatedbrinesare pages 12-15)

---

## 9) Expert analysis / interpretation (grounded in sources)

1. **Mechanistic convergence**: Across disparate hypersaline systems, high-NaCl growth capacity is repeatedly supported by a small set of convergent physiological themes: (i) **K+ (KCl) accumulation** for salt-in organisms; (ii) **compatible-solute accumulation** in salt-out organisms; and (iii) a frequent signature of **proteome acidification** accompanying salt-in physiology. (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4, xing2024thepolyextremophilenatranaerobius pages 1-2)
2. **Hybrid strategies are likely under-curated**: 2024 data indicate that fluctuating salinity regimes can select for organisms combining both strategies, implying that causal graphs for “NaCl range high” may require explicit nodes for **environmental fluctuation** and regulatory tradeoffs (energetic cost vs flexibility). (ionescu2024extremefluctuationsin pages 1-2)
3. **Genetic leverage points**: 2024 engineering shows direct causality between osmolyte pathway genetics (**ectABC**, **proB/proA/proC**, **putA**) and upper salinity growth limits (4% vs 8% NaCl), providing strong candidate mechanistic edges—though these are **taxon- and context-specific** and should be flagged as such when curating a general trait graph. (khanh2024metabolicpathwayengineering pages 1-2)

---

## 10) Warnings / curation caveats (do not over-curate)

* **Definition heterogeneity**: “Extreme halophile” may refer to **optimum** NaCl (e.g., >15%) or **requirement/range** (e.g., 2.5–5.2 M). For METPO:1000472, keep the primary assertion tied to the **upper growth-supporting range >~8% w/v**, and record alternate definitions as synonyms or mapping notes rather than hard constraints. (cirachavez2019kineticsofhalophilic pages 1-3, bartha2022investigatingextremotolerantmicrobes pages 21-25)
* **Taxon-specific edges**: Transporter-family and metabolite trends in *N. thermophilus* are strong but should be curated as **taxon-specific evidence** unless corroborated across taxa. (xing2024thepolyextremophilenatranaerobius pages 1-2)
* **Engineered evidence**: Edges derived from pathway replacements/deletions in *H. elongata* (ectABC replacement, putA deletion) demonstrate mechanism but are not equivalent to native extreme-halophile physiology; tag as **engineered/assay-specific**. (khanh2024metabolicpathwayengineering pages 1-2)
* **Non-NaCl brines**: Extremely saline/chaotropic systems may not map cleanly to NaCl-only phenotypes; avoid generalizing NaCl-range edges to total dissolved salt extremes dominated by Mg/Ca/Li/Fe salts without additional sources. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

---

## 11) DOI-first bibliography (with URLs and publication dates)

**2024 (prioritized)**
1. Gutiérrez‑Preciado A, et al. *Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines.* **Nature Ecology & Evolution**. **Aug 2024**. DOI: **10.1038/s41559-024-02505-6**. https://doi.org/10.1038/s41559-024-02505-6 (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
2. Ionescu D, et al. *Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy.* **Frontiers in Microbiomes**. **Jan 2024**. DOI: **10.3389/frmbi.2023.1329925**. https://doi.org/10.3389/frmbi.2023.1329925 (ionescu2024extremefluctuationsin pages 1-2)
3. Xing Q, et al. *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.* **Applied and Environmental Microbiology**. **May 2024**. DOI: **10.1128/aem.00145-24**. https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2)
4. Khanh HC, et al. *Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient Halomonas elongata.* **Applied and Environmental Microbiology**. **Sep 2024**. DOI: **10.1128/aem.01195-24**. https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 1-2)

**2023**
5. Favreau C, et al. *Molecular acclimation of Halobacterium salinarum to halite brine inclusions.* **Frontiers in Microbiology**. **Jan 2023**. DOI: **10.3389/fmicb.2022.1075274**. https://doi.org/10.3389/fmicb.2022.1075274 (visual evidence used) (favreau2023molecularacclimationof media e42a87e3, favreau2023molecularacclimationof media 86c02d7b, favreau2023molecularacclimationof media 8ac1f198)

**Foundational / background (high-authority reviews/chapters)**
6. Lee CJD, et al. *NaCl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats.* **FEMS Microbiology Reviews**. **Jun 2018**. DOI: **10.1093/femsre/fuy026**. https://doi.org/10.1093/femsre/fuy026 (lee2018naclsaturatedbrinesare pages 12-15, lee2018naclsaturatedbrinesare pages 15-17)
7. Cira‑Chávez LA, et al. *Kinetics of Halophilic Enzymes.* **IntechOpen (book chapter)**. **Jan 2019**. DOI: **10.5772/intechopen.81100**. https://doi.org/10.5772/intechopen.81100 (cirachavez2019kineticsofhalophilic pages 1-3)
8. Ghosh S, et al. *Microbial Diversity of Saline Habitats: An Overview of Biotechnological Applications.* **Soil Biology (book chapter)**. **Jan 2019**. DOI: **10.1007/978-3-030-18975-4_4**. https://doi.org/10.1007/978-3-030-18975-4_4 (ghosh2019microbialdiversityof pages 13-15)

---

## Appendix: How to map into `nacl_range_high.yaml` (TraitMech curation guidance)

* Encode METPO:1000472 as the phenotype node.
* Represent high external NaCl (and optionally fluctuating salinity) as environmental drivers.
* Include two mechanistic subgraphs:
  * **Salt-in arm**: external high NaCl → K+ accumulation/KCl → proteome acidification (Asp/Glu enrichment) → protein function at high ionic strength → growth at high NaCl.
  * **Compatible-solute arm**: external high NaCl → compatible-solute transport/biosynthesis (glycine betaine, ectoine, proline, glutamate; transporters Opu/ProU/SSS) → osmoprotection → growth at high NaCl.
* Annotate edges with scope tags (broad vs taxon-specific vs engineered).

(Edges and nodes are provided in artifacts for direct import/curation.) (xing2024thepolyextremophilenatranaerobius pages 1-2, khanh2024metabolicpathwayengineering pages 1-2, lee2018naclsaturatedbrinesare pages 15-17)

References

1. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4): Ana Gutiérrez-Preciado, Bledina Dede, Brittany A. Baker, Laura Eme, David Moreira, and Purificación López-García. Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines. Aug 2024. URL: https://doi.org/10.1038/s41559-024-02505-6, doi:10.1038/s41559-024-02505-6. This article has 23 citations and is from a highest quality peer-reviewed journal.

2. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

3. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

4. (ionescu2024extremefluctuationsin pages 1-2): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 11 citations.

5. (lee2018naclsaturatedbrinesare pages 12-15): Callum J D Lee, Phillip E McMullan, Callum J O’Kane, Andrew Stevenson, Inês C Santos, Chayan Roy, Wriddhiman Ghosh, Rocco L Mancinelli, Melanie R Mormile, Geoffrey McMullan, Horia L Banciu, Mario A Fares, Kathleen C Benison, Aharon Oren, Mike L Dyall-Smith, and John E Hallsworth. Nacl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats. FEMS microbiology reviews, 42 5:672-693, Jun 2018. URL: https://doi.org/10.1093/femsre/fuy026, doi:10.1093/femsre/fuy026. This article has 90 citations and is from a domain leading peer-reviewed journal.

6. (cirachavez2019kineticsofhalophilic pages 1-3): Luis Alberto Cira-Chávez, Joseph Guevara-Luna, Marisela Yadira Soto-Padilla, Brenda Román-Ponce, María Soledad Vásquez- Murrieta, and María Isabel Estrada-Alvarado. Kinetics of halophilic enzymes. Kinetics of Enzymatic Synthesis, Jan 2019. URL: https://doi.org/10.5772/intechopen.81100, doi:10.5772/intechopen.81100. This article has 20 citations.

7. (bartha2022investigatingextremotolerantmicrobes pages 21-25): E Bartha. Investigating extremotolerant microbes in non-extreme environments and altering the salinity growth limits of halophiles. Unknown journal, 2022.

8. (bartha2022investigatingextremotolerantmicrobes pages 25-28): E Bartha. Investigating extremotolerant microbes in non-extreme environments and altering the salinity growth limits of halophiles. Unknown journal, 2022.

9. (lee2018naclsaturatedbrinesare pages 15-17): Callum J D Lee, Phillip E McMullan, Callum J O’Kane, Andrew Stevenson, Inês C Santos, Chayan Roy, Wriddhiman Ghosh, Rocco L Mancinelli, Melanie R Mormile, Geoffrey McMullan, Horia L Banciu, Mario A Fares, Kathleen C Benison, Aharon Oren, Mike L Dyall-Smith, and John E Hallsworth. Nacl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats. FEMS microbiology reviews, 42 5:672-693, Jun 2018. URL: https://doi.org/10.1093/femsre/fuy026, doi:10.1093/femsre/fuy026. This article has 90 citations and is from a domain leading peer-reviewed journal.

10. (ghosh2019microbialdiversityof pages 13-15): Shubhrima Ghosh, Sumit Kumar, and Sunil Kumar Khare. Microbial diversity of saline habitats: an overview of biotechnological applications. Soil Biology, pages 65-92, Jan 2019. URL: https://doi.org/10.1007/978-3-030-18975-4\_4, doi:10.1007/978-3-030-18975-4\_4. This article has 26 citations and is from a peer-reviewed journal.

11. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

12. (favreau2023molecularacclimationof media e42a87e3): Charly Favreau, Alicia Tribondeau, Marie Marugan, François Guyot, Beatrice Alpha-Bazin, Arul Marie, Remy Puppo, Thierry Dufour, Arnaud Huguet, Séverine Zirah, and Adrienne Kish. Molecular acclimation of halobacterium salinarum to halite brine inclusions. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1075274, doi:10.3389/fmicb.2022.1075274. This article has 12 citations and is from a peer-reviewed journal.

13. (favreau2023molecularacclimationof media 86c02d7b): Charly Favreau, Alicia Tribondeau, Marie Marugan, François Guyot, Beatrice Alpha-Bazin, Arul Marie, Remy Puppo, Thierry Dufour, Arnaud Huguet, Séverine Zirah, and Adrienne Kish. Molecular acclimation of halobacterium salinarum to halite brine inclusions. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1075274, doi:10.3389/fmicb.2022.1075274. This article has 12 citations and is from a peer-reviewed journal.

14. (favreau2023molecularacclimationof media 8ac1f198): Charly Favreau, Alicia Tribondeau, Marie Marugan, François Guyot, Beatrice Alpha-Bazin, Arul Marie, Remy Puppo, Thierry Dufour, Arnaud Huguet, Séverine Zirah, and Adrienne Kish. Molecular acclimation of halobacterium salinarum to halite brine inclusions. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1075274, doi:10.3389/fmicb.2022.1075274. This article has 12 citations and is from a peer-reviewed journal.