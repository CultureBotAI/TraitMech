---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:46:25.799791'
end_time: '2026-06-17T21:59:45.718007'
duration_seconds: 799.92
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: euryhaline
  trait_identifier: METPO:1000627
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: euryhaline
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A halophily preference in which an organism can tolerate a wide range
    of salinity conditions.
  parent_traits: METPO:1000629
  synonyms: ''
  evidence_summary: 'DOI:10.5928/kaiyou.14.337: growing over a salinity range of 15%
    (Supports euryhaline halophiles as organisms growing across a wide salinity range.)
    | PMID:22675587: due to its strong euryhaline phenotype (Organism example: Chromohalobacter
    salexigens is described as having a strong euryhaline phenotype.)'
  causal_graph_summary: 'euryhaline_wide_salinity_tolerance: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** euryhaline
- **METPO identifier:** METPO:1000627
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can tolerate a wide range of salinity conditions.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.5928/kaiyou.14.337: growing over a salinity range of 15% (Supports euryhaline halophiles as organisms growing across a wide salinity range.) | PMID:22675587: due to its strong euryhaline phenotype (Organism example: Chromohalobacter salexigens is described as having a strong euryhaline phenotype.)
- **Existing causal graph summary:** euryhaline_wide_salinity_tolerance: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **euryhaline** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/euryhaline.yaml`.

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
- **Trait label:** euryhaline
- **METPO identifier:** METPO:1000627
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can tolerate a wide range of salinity conditions.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.5928/kaiyou.14.337: growing over a salinity range of 15% (Supports euryhaline halophiles as organisms growing across a wide salinity range.) | PMID:22675587: due to its strong euryhaline phenotype (Organism example: Chromohalobacter salexigens is described as having a strong euryhaline phenotype.)
- **Existing causal graph summary:** euryhaline_wide_salinity_tolerance: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **euryhaline** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/euryhaline.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **euryhaline** (METPO:1000627)

### 0) Scope summary (TraitMech-ready)
The microbial trait **euryhaline** (METPO:1000627) denotes the **capacity to tolerate a wide range of environmental salinities** (i.e., broad salinity niche width), in contrast to **stenohaline** organisms whose “life processes are confined to environments where salinity remains relatively stable.” (wu2024metagenomicinsightsinto pages 1-2). In a recent metagenomic study of the Pearl River Estuary (PRE), Wu et al. operationalized this concept by classifying metagenome-assembled genomes (MAGs) as **stenohaline** if mean relative abundance in one salinity bin exceeded the other two by **an order of magnitude**, and labeling MAGs that did not meet this criterion as **euryhaline** (wu2024metagenomicinsightsinto pages 1-2). This is an **assay/analysis-derived definition** based on abundance across a salinity gradient rather than a universal physiological threshold (warning below).

Mechanistically, euryhaline tolerance in microbes is generally underpinned by a combination of osmoadaptation strategies that buffer cytoplasmic water activity and macromolecular function: (i) **“salt-in”** (inorganic ion uptake/management), (ii) **“salt-out”** (accumulation of **compatible solutes** via uptake and/or biosynthesis), and (iii) rapid response systems for downshifts in osmolarity (e.g., **mechanosensitive channels**) and water transport regulation (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 13-14, bonnaud2024haloarchaeaaspromising pages 2-4, galisteo2023astepinto pages 13-14). In natural gradients, ion-transport gene features—particularly Trk-type K+ uptake (COG0168)—were highlighted as dominant correlates of salinity adaptation (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 11-13).

### 1) Trait boundaries and nearby traits (curation guidance)
**Key boundary cases for curation**:
1. **Euryhaline vs stenohaline (operational vs physiological)**: Wu et al. explicitly caution that salinity-tolerance categories can be inferred from **relative abundance fluctuations** across environments, making this classification dependent on sampling design and ecology (wu2024metagenomicinsightsinto pages 1-2). For TraitMech, this suggests a distinction between:
   - **Phenotype node**: “wide salinity tolerance” (METPO:1000627), and
   - **Assay/analysis node**: “stable abundance across low/intermediate/high salinity bins” (dataset-specific classifier) (wu2024metagenomicinsightsinto pages 1-2).
2. **Euryhaline vs halophilic/halotolerant**: A haloarchaeal review emphasizes that extreme halophiles often favor **salt-in**, whereas **salt-out** is described as typical for “halotolerant organisms,” though haloarchaea may deploy both depending on conditions (bonnaud2024haloarchaeaaspromising pages 2-4). This indicates that **euryhaline** should not be equated with either “salt-in” or “salt-out”; rather, it can involve **strategy switching, redundancy, or flexible regulation**.
3. **Euryhaline vs mere growth at one salinity extreme**: Presence in hypersaline habitats or encoding osmoadaptation genes does not, by itself, prove euryhalinity; it may indicate **halophily** or **halotolerance** without evidence of performance across a broad salinity range.

### 2) Candidate causal-graph nodes (grouped by type)
Below are curation candidates with suggested grounding where the sources provide it.

#### 2.1 Environmental / experimental factors
- **Environmental salinity gradient** (label-only; could be grounded to ENVO “saline water” terms if chosen later) (wu2024metagenomicinsightsinto pages 1-2).
- **Salinity category bins**: low / intermediate / high (dataset-level operational factors) (wu2024metagenomicinsightsinto pages 1-2).
- **Short residence-time estuary context** (PRE residence time 3–12 days) (wu2024metagenomicinsightsinto pages 1-2).

#### 2.2 Processes / strategies
- **Salt-in osmoadaptation strategy** (label-only) (wu2024metagenomicinsightsinto pages 1-2).
- **Salt-out (compatible-solute) osmoadaptation strategy** (label-only) (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 13-14).
- **Regulation of water channel activity** (GO:0015250 linked by authors to COG0580) (wu2024metagenomicinsightsinto pages 13-14).
- **Osmotic downshock response / emergency release** (mechanosensitive channels) (bonnaud2024haloarchaeaaspromising pages 2-4, galisteo2023astepinto pages 13-14).
- **Proteome charge remodeling / increased acidity (high ionic strength adaptation)** (label-only; supported in brackish transitions) (jurdzinski2023largescalephylogenomicsof pages 11-12).

#### 2.3 Genes / proteins / transport systems (salt-in)
- **Trk-type K+ transport system**: COG0168; transmembrane subunits **TrkH/TrkG** (COG0168) (wu2024metagenomicinsightsinto pages 11-13).
- **Kup-type K+ transport system**: COG3158 (wu2024metagenomicinsightsinto pages 11-13).
- **Ca2+:K+/Na+ antiporter**: COG0530 (wu2024metagenomicinsightsinto pages 11-13).
- **Cl− channel**: COG0038 (wu2024metagenomicinsightsinto pages 11-13).
- **Na+/H+ antiporters** (label-only; described as Na+ expulsion route) (bonnaud2024haloarchaeaaspromising pages 2-4).
- **Cl−/Na+ symport** (label-only; haloarchaea salt-in) (bonnaud2024haloarchaeaaspromising pages 2-4).
- **Halorhodopsin (light-driven Cl− pump)** (label-only) (bonnaud2024haloarchaeaaspromising pages 2-4).

#### 2.4 Genes / proteins / pathways (salt-out; compatible solutes)
- **Compatible-solute uptake COGs**: COG0591/COG0477/COG1115; described as supporting uptake of compatible solutes “such as glycine betaine, proline, and alanine” (wu2024metagenomicinsightsinto pages 13-14).
- **Osmoprotectant uptake (Opu) system**: opuABC (KO: K05845/K05846/K05847) (galisteo2023astepinto pages 13-14).
- **OpuD (BCCT family)**: glycine betaine affinity (label-only; family-level) (galisteo2023astepinto pages 13-14).
- **ProVWX (ABC transporter)**: KO K02000/K02001/K02002 (galisteo2023astepinto pages 13-14).
- **Glycine betaine biosynthesis from choline**: BetA (KO:K00108) + BetB (KO:K00130) (galisteo2023astepinto pages 13-14).
- **Ectoine biosynthesis from L-aspartate**: lysC (KO:K00928), asd (KO:K00133), ectB (KO:K00836), ectA (KO:K06718), ectC (KO:K06720), plus ectABC operon context (galisteo2023astepinto pages 13-14, galisteo2023astepinto pages 14-17).
- **Ectoine TRAP transporters**: TeaABC and UehABC (label-only) (galisteo2023astepinto pages 13-14).
- **Ectoine degradation**: DoeA/DoeB (label-only) (galisteo2023astepinto pages 13-14).
- **Trehalose/2-sulfotrehalose and glycine betaine uptake** as widespread osmoadaptation mechanisms in Halobacteriales (reviewed with genome counts) (bonnaud2024haloarchaeaaspromising pages 2-4).

#### 2.5 Chemicals / metabolites (CHEBI where possible)
- **K+** (CHEBI:29103, candidate) (bonnaud2024haloarchaeaaspromising pages 2-4).
- **Cl−** (CHEBI:17996, candidate) (wu2024metagenomicinsightsinto pages 11-13, bonnaud2024haloarchaeaaspromising pages 2-4).
- **Na+** (CHEBI:29101, candidate) (bonnaud2024haloarchaeaaspromising pages 2-4).
- **Glycine betaine** (CHEBI:17750, candidate) (wu2024metagenomicinsightsinto pages 13-14, galisteo2023astepinto pages 13-14).
- **Choline** (CHEBI:15354, candidate) (galisteo2023astepinto pages 13-14).
- **Proline** (CHEBI:17203, candidate) (wu2024metagenomicinsightsinto pages 13-14).
- **Alanine** (CHEBI:16449, candidate) (wu2024metagenomicinsightsinto pages 13-14).
- **Ectoine** (CHEBI:22563, candidate) (galisteo2023astepinto pages 13-14).
- **Glutamate** (CHEBI:29985, candidate) (jurdzinski2023largescalephylogenomicsof pages 11-12).

### 3) Candidate causal edges (evidence-backed)
The table below is intended for direct transfer into `data/traits/environment/euryhaline.yaml` after curator review.

| Edge (S–P–O) | Mechanism class | Candidate node grounding | Evidence snippet | Source (DOI, year, URL) | Curation notes/uncertainty |
|---|---|---|---|---|---|
| MAG not meeting stenohaline abundance criterion – classified as – euryhaline | definition/trait scope | METPO:1000627; label-only: euryhaline MAG | “Those that did not meet this criterion were classified as euryhaline” and stenohaline MAGs were defined where abundance in one salinity class exceeded the other two “by an order of magnitude” (wu2024metagenomicinsightsinto pages 1-2) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Operational dataset-specific definition from estuarine MAGs; useful for assay/annotation boundary, not a universal physiological threshold. |
| increasing environmental salinity – increases relative abundance of – COG0168 / Trk-type K+ transport system | salt-in | COG:COG0168; GO:0006813 (potassium ion transport, candidate) | “COG0168… exhibited an upward trend” and “The K+ uptake-based ‘salt-in’ strategy may be the key mechanism” (wu2024metagenomicinsightsinto pages 11-13, wu2024metagenomicinsightsinto pages 13-14) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Strong salinity association in metagenomes/MAGs; edge is environment-to-feature, not direct proof of necessity for all euryhaline taxa. |
| COG0168 / Trk-type K+ transport system – contributes to – salt-in strategy | salt-in | COG:COG0168 | “these were assumed to be implicated in the ‘salt-in’ strategy” referring to COG0168, COG3158, COG0530, and COG0038 (wu2024metagenomicinsightsinto pages 11-13) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Curate as supported-but-inferred mechanistic role; wording in source is “assumed to be implicated.” |
| COG0530 / Ca2+:K+/Na+ antiporter – contributes to – salt-in strategy | salt-in | COG:COG0530 | “COG0530 (Ca2+: K+/Na+ antiporter)… [was] assumed to be implicated in the ‘salt-in’ strategy” (wu2024metagenomicinsightsinto pages 11-13) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Supported by annotation and salinity trend; broad taxonomic generalization should be marked uncertain. |
| increasing environmental salinity – increases relative abundance of – COG0530 / Ca2+:K+/Na+ antiporter | salt-in | COG:COG0530 | “COG0168, COG0530, and COG0038 exhibited an upward trend” (wu2024metagenomicinsightsinto pages 11-13) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Association edge only; likely useful as environment-feature relation in TraitMech. |
| COG0038 / chloride channel – contributes to – salt-in strategy | salt-in | COG:COG0038; CHEBI:17996 (chloride) candidate | “COG0038 (Cl− channel)… [was] assumed to be implicated in the ‘salt-in’ strategy” (wu2024metagenomicinsightsinto pages 11-13) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Annotation-based and salinity-correlated; exact transporter biophysics unresolved here. |
| COG3158 / Kup-type K+ transport system – contributes to – salt-in strategy | salt-in | COG:COG3158 | “COG3158 (Kup-type K+ transport system)… [was] assumed to be implicated in the ‘salt-in’ strategy” (wu2024metagenomicinsightsinto pages 11-13) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Note opposite salinity trend versus COG0168; may indicate low-salinity-biased K+ uptake mode rather than general euryhaline marker. |
| increasing environmental salinity – decreases relative abundance of – COG3158 / Kup-type K+ transport system | salt-in | COG:COG3158 | “COG3158… displayed a linear decline with rising salinity” (wu2024metagenomicinsightsinto pages 11-13) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Important negative edge; may help distinguish low- vs high-salinity adaptation modules. |
| COG0580 – enables – facilitated diffusion of water | water transport | COG:COG0580; GO:0015250 | “COG0580 is linked to GO:0015250, and its function is to enable the facilitated diffusion of water” (wu2024metagenomicinsightsinto pages 13-14) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Good ontology-grounded functional node; exact gene identity unspecified in excerpt. |
| increasing environmental salinity – decreases relative abundance of – COG0580 | water transport | COG:COG0580; GO:0015250 | “COG0580 presented a decreasing trend in relative abundance with increasing salinity” (wu2024metagenomicinsightsinto pages 11-13) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Salinity association may reflect reduced water-channel regulation at high salinity; mechanism indirect. |
| COG0591/COG0477/COG1115 – facilitate uptake of – compatible solutes (glycine betaine, proline, alanine) | salt-out | COG:COG0591; COG:COG0477; COG:COG1115; CHEBI:17750 (glycine betaine); CHEBI:17203 (L-proline); CHEBI:16449 (alanine) candidate | “COG0591, COG0477, and COG1115 were recognized as contributors to the ‘salt-out’ strategy, facilitating the uptake of compatible solutes, such as glycine betaine, proline, and alanine” (wu2024metagenomicinsightsinto pages 13-14) | 10.1186/s40168-024-01817-w, 2024, https://doi.org/10.1186/s40168-024-01817-w | Strong generic salt-out edge, but specific transporter identities for each COG should be resolved before fine-grained curation. |
| OpuABC osmoprotectant uptake system – imports – compatible solutes from environment | salt-out | KO:K05845; KO:K05846; KO:K05847 | “harbored the osmoprotectant uptake (Opu) system (opuABC genes… ), an ABC transporter for acquisition of different compatible solutes (especially choline) from the environment” (galisteo2023astepinto pages 13-14) | 10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 | Species/genome-specific evidence from Bacillaceae isolates; mechanistically strong but taxon-limited. |
| OpuD (BCCT family) – has high affinity for – glycine betaine | salt-out | label-only: OpuD; CHEBI:17750 | “all the studied strains presented OpuD from the BCCT… family, with high affinity for glycine betaine” (galisteo2023astepinto pages 13-14) | 10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 | High-confidence substrate relation; presence in studied strains does not alone establish euryhalinity. |
| ProVWX ABC transporter – mediates uptake of – glycine betaine | salt-out | KO:K02000; KO:K02001; KO:K02002; CHEBI:17750 | “Another ABC-type transporter, namely ProVWX… for glycine betaine uptake… was present in all genomes under study” (galisteo2023astepinto pages 13-14) | 10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 | Strong transporter-substrate edge; taxon-specific to analyzed genomes. |
| BetA + BetB – convert – choline to glycine betaine | salt-out | KO:K00108; KO:K00130; CHEBI:15354 (choline); CHEBI:17750 (glycine betaine) | “Choline is transformed into glycine betaine in two oxidative steps carried out by BetA (K00108) and BetB (K00130)” (galisteo2023astepinto pages 13-14) | 10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 | Good biosynthetic edge; direct enzymatic statement suitable for curation. |
| lysC + asd + ectB + ectA + ectC – biosynthesize – ectoine from L-aspartate | salt-out | KO:K00928; KO:K00133; KO:K00836; KO:K06718; KO:K06720; CHEBI:28885 (L-aspartate); CHEBI:22563 (ectoine) candidate | “Ectoine is obtained from L-aspartate in five steps mediated by… lysC… asd… ectB… ectA… and… ectC” (galisteo2023astepinto pages 13-14) | 10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 | Strong pathway edge; ectoine widely implicated in halophily and salinity tolerance. |
| TeaABC transporter – reuptakes/imports – ectoine | salt-out | label-only: TeaABC; CHEBI:22563 | “TeaABC transporter… with high affinity for ectoine… It allows the reuptake of secreted ectoine in Halomonas elongata” (galisteo2023astepinto pages 13-14) | 10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 | Evidence includes Halomonas-based functional interpretation applied to comparative genomes; curate with moderate confidence. |
| UehABC transporter – imports – ectoine and hydroxyectoine | salt-out | label-only: UehABC; CHEBI:22563; label-only: 5-hydroxyectoine | “UehABC is a second TRAP transporter… that imports ectoine and hydroxyectoine” (galisteo2023astepinto pages 13-14) | 10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 | Functional statement derives from prior characterization; presence sparse in analyzed genomes. |
| higher abundance of TeaABC-related genes than UehABC-related genes – indicates prevalence of – osmoprotective use of ectoine over catabolic use | salt-out | label-only: TeaABC; label-only: UehABC; CHEBI:22563 | “The higher abundance of TeaABC-related genes over UehABC-related ones might indicate a prevalence of the osmoprotective activity of ectoine” (galisteo2023astepinto pages 13-14) | 10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 | Explicitly inferential (“might indicate”); mark uncertain and avoid over-curation. |
| DoeA/DoeB – participate in – ectoine degradation | salt-out | label-only: DoeA; label-only: DoeB; CHEBI:22563 | “DoeA and DoeB proteins seem to be relevant in the degradation” of ectoine/hydroxyectoine (galisteo2023astepinto pages 13-14) | 10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 | Relevant for ectoine turnover, but this may oppose stable osmolyte accumulation; context-dependent. |
| Msc mechanosensitive channels – release – ions and organic solutes during sudden downward osmotic shocks | osmotic shock | K16053; K03282; GO:0008381 (mechanosensitive ion channel activity, candidate) | “Msc mechanosensitive channels… play an important role in releasing ions” and Bonnaud: “serve as safety valves, allowing the rapid release of ions and organic solutes in the case of sudden downward osmotic shocks” (galisteo2023astepinto pages 13-14, bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 ; 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | Strong general osmotic-shock edge across halophiles/halotolerant taxa; likely broadly curatable. |
| Na+/H+ antiporter – expels – sodium ions from cytoplasm | salt-in | label-only: Na+/H+ antiporter; CHEBI:29101 (sodium(1+)); CHEBI:15378 (hydron) candidate | “sodium ions are expelled from the cytoplasm… usually performed with the help of Na+/H+ antiporters” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | Review-level statement for haloarchaea; broad but authoritative. |
| Cl−/Na+ symport and halorhodopsin pump – transport – chloride into cytoplasm | salt-in | CHEBI:17996; label-only: halorhodopsin; label-only: Cl-/Na+ symport | “Cl− uptake occurs with the help of two energy-dependent pumps… a Cl−/Na+ symport… and a primary light-dependent Cl− pump (… halorhodopsin)” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | Haloarchaeal and high-salt-focused; may be too taxon-specific for generic euryhaline graph unless tagged uncertain. |
| accumulation of K+ and Cl− in cytoplasm – requires adaptation of – enzymes/cellular components to high salinity | proteome remodeling | CHEBI:29103 (potassium(1+)); CHEBI:17996 | “This strategy requires a number of physiological changes… adaptation of enzymes and cellular components to high salinity” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | General mechanistic background for salt-in organisms; not specific to euryhaline taxa. |
| transition to higher salinity/brackish biome – selects for – more acidic proteome / increased acidic amino acids | proteome remodeling | label-only: acidic proteome; CHEBI:29985 (L-glutamate) candidate | Jurdzinski summary: “increase in acidic amino acids (notably glutamate)” and “acidification of the proteome would be essential for protein solubility” in high salinity contexts (jurdzinski2023largescalephylogenomicsof pages 11-12, bonnaud2024haloarchaeaaspromising pages 2-4) | 10.1126/sciadv.adg2059, 2023, https://doi.org/10.1126/sciadv.adg2059 ; 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | Proteome-acidification edge is strong conceptually but excerpt here comes from evidence summary rather than direct full-text quote for Jurdzinski; curate with moderate confidence. |
| gain/loss of salinity-adaptive gene functions and proteome reorganization – constrains/enables – cross-biome salinity transitions | proteome remodeling | label-only: mobile genetic elements; label-only: salinity-adaptive functions | Jurdzinski summary: transitions were “accompanied by systematic changes in amino acid composition and isoelectric point distributions… as well as convergent gains or losses of specific gene functions” (jurdzinski2023largescalephylogenomicsof pages 1-1) | 10.1126/sciadv.adg2059, 2023, https://doi.org/10.1126/sciadv.adg2059 | Broad evolutionary edge; useful for higher-level graph but not a direct cell-physiology mechanism node. |


*Table: This table compiles candidate causal edges for curating the microbial trait euryhaline (METPO:1000627), grounded in evidence from four cited 2023–2024 sources. It emphasizes operational trait definition, salt-in and salt-out osmoadaptation, osmotic-shock release systems, water transport, and proteome remodeling, with notes on confidence and taxon specificity.*

### 4) Recent developments and latest research emphasis (2023–2024)

#### 4.1 Natural-gradient “omics” operationalization of euryhalinity (2024)
Wu et al. (Microbiome, 2024) provide a modern, reproducible way to label euryhaline vs stenohaline microbial genomes directly from gradient metagenomes (wu2024metagenomicinsightsinto pages 1-2). Their workflow includes: salinity binning, MAG reconstruction (n=127), and feature selection (Boruta) to identify osmoregulatory gene categories, highlighting **inorganic ion transport** as a prominent genomic discriminator and **Trk-type K+ transport (COG0168)** as the top feature whose abundance rises with salinity (wu2024metagenomicinsightsinto pages 1-2).

**Figure evidence**: In Wu et al., relative abundance differences for key “salt-in” COGs across salinity categories and trends for water-channel regulation are shown in the extracted figures (wu2024metagenomicinsightsinto media 22d779d4, wu2024metagenomicinsightsinto media 6bd2f532).

#### 4.2 Proteome remodeling and gene-function changes during salinity transitions (2023; corrected 2024)
A large-scale phylogenomic analysis of aquatic bacteria (Science Advances, 2023; erratum/correction noted 2024) links brackish/marine transitions to systematic proteome-scale changes. In brackish-associated patterns, the authors state they connected isoelectric point distribution changes to “increase in proportion of acidic amino acids, most notably glutamate,” which they interpret as improving protein solubility at higher ionic strength (jurdzinski2023largescalephylogenomicsof pages 11-12). They also identify brackish-enriched genes involved in glutamate posttranslational modifications, noting these modifications “increase the acidity of residues,” providing a mechanistic link between salinity regime and proteome charge adaptation (jurdzinski2023largescalephylogenomicsof pages 11-12).

#### 4.3 Expansion of mechanism catalogs for osmoadaptation (2023–2024)
Two 2023–2024 sources consolidate gene- and pathway-level nodes for osmoadaptation:
- A comparative-genomics study of Bacillaceae from hypersaline soils details a salt-out repertoire spanning **Opu/ProVWX uptake**, **glycine betaine biosynthesis (BetA/BetB)**, **ectoine biosynthesis (lysC/asd/ectB/ectA/ectC)**, **ectoine transport (TeaABC/UehABC)**, and **mechanosensitive channels (Msc)** for downshock (galisteo2023astepinto pages 13-14, galisteo2023astepinto pages 14-17).
- A 2024 haloarchaea review highlights mechanistic separation between strategies, emphasizing Na+ expulsion via Na+/H+ antiporters, and describing Msc channels as “safety valves” enabling rapid release of ions/organic solutes after osmotic downshifts (bonnaud2024haloarchaeaaspromising pages 2-4).

### 5) Current applications and real-world implementations

#### 5.1 Biotechnological production of osmoprotectants (ectoine)
Ectoine is emphasized as a “valuable molecule for biotechnological purposes” due to protection of “cell components under stressful conditions, such as freezing, high temperature, and drying.” (galisteo2023astepinto pages 14-17). A cited industrially relevant example is that *Halomonas bluephagenesis* TD01 “has been demonstrated to yield **28 g L−1** of ectoine during a **28-h fed-batch** growth process” (galisteo2023astepinto pages 14-17). This provides a concrete real-world linkage between osmoadaptation chemistry and bioprocess implementation.

#### 5.2 Environmental microbiome management/monitoring in estuaries
In the PRE, salinity acts as an influential abiotic factor structuring microbial community composition and function, and the study context includes large freshwater inflow (~**330×10^9 m^3 per annum**) and residence time **3–12 days**, which drive dynamic gradients where euryhaline vs stenohaline taxa can be separated (wu2024metagenomicinsightsinto pages 1-2). For applied settings (e.g., coastal monitoring), the salinity-responsive gene features (COG0168 etc.) provide candidate molecular markers for salinity stress and niche partitioning (wu2024metagenomicinsightsinto pages 1-2).

### 6) Statistics and data points extracted from recent studies
- **Operational euryhaline definition (MAG-based)**: euryhaline MAGs are those not showing an order-of-magnitude enrichment in a single salinity bin (wu2024metagenomicinsightsinto pages 1-2).
- **PRE hydrology**: freshwater inflow ~**330×10^9 m^3/year**; residence time **3–12 days** (wu2024metagenomicinsightsinto pages 1-2).
- **Gene-feature statistics (examples)**: metagenome-level trends for compatible solute uptake COGs and water-channel COG0580 include reported R² and p-values (e.g., COG0591 R²=0.6467; COG1115 R²=0.8093; COG0580 R²=0.4783) (wu2024metagenomicinsightsinto pages 11-13).
- **Industrial ectoine titer**: **28 g/L in 28 h** fed-batch (galisteo2023astepinto pages 14-17).
- **Proteome adaptation**: brackish-associated “increase in proportion of acidic amino acids, most notably glutamate,” interpreted as improving solubility at higher ionic strength (jurdzinski2023largescalephylogenomicsof pages 11-12).

### 7) Expert opinions / authoritative interpretations (for curator notes)
- Wu et al. interpret the “K+ uptake-based ‘salt-in’ strategy” as potentially “the key mechanism allowing estuarine microorganisms to adapt to salinity stress” in their system (wu2024metagenomicinsightsinto pages 13-14). This is an interpretation based on feature selection and abundance trends.
- Bonnaud et al. emphasize a cost/benefit framing: salt-out has “high energy cost” and is “less adapted to saturating salt concentrations,” while haloarchaea “favor the salt-in strategy at high salt concentrations” (bonnaud2024haloarchaeaaspromising pages 2-4). This frames strategy selection as environment-dependent.
- Jurdzinski et al. connect proteome-level acidity changes to physical chemistry (“charged amino acids increase protein solubility at higher ionic strength”) and highlight that annotation-based functional conclusions “should be treated with caution” (jurdzinski2023largescalephylogenomicsof pages 11-12), which is directly relevant to curation conservatism.

### 8) Warnings / items not yet safe to curate into TraitMech
1. **Do not treat abundance-based labels as definitive physiology**: The Wu et al. operational definition of euryhaline/stenohaline is tied to relative abundance across sampled salinity bins and may not map 1:1 to lab growth-range phenotypes (wu2024metagenomicinsightsinto pages 1-2).
2. **“Assumed to be implicated” phrasing**: For several COG→strategy links (e.g., COG0168/3158/0530/0038), the text states these were “assumed to be implicated” in salt-in (wu2024metagenomicinsightsinto pages 11-13). These edges are appropriate as **candidate** edges but should be marked **inferred** unless corroborated by functional genetics.
3. **Taxon-specific mechanisms**: Halorhodopsin-mediated Cl− pumping and some haloarchaeal salt-in details may be too specific to haloarchaea to include as generic euryhaline mechanisms unless you encode taxon constraints (bonnaud2024haloarchaeaaspromising pages 2-4).
4. **Ectoine production example is a citation chain**: The 28 g/L ectoine statistic is reported in a 2023 paper but sourced to earlier work (Ma et al., 2020) (galisteo2023astepinto pages 14-17). If the curation requires primary experimental provenance, retrieve and cite the original Ma et al. study separately.

---

## DOI-first bibliography (with publication dates and URLs)

1. **Wu Z, Li M, Qu L, Zhang C, Xie W.** *Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary.* **Microbiome** (Published 2024-06). DOI: **10.1186/s40168-024-01817-w**. URL: https://doi.org/10.1186/s40168-024-01817-w (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 11-13, wu2024metagenomicinsightsinto pages 13-14, wu2024metagenomicinsightsinto media 22d779d4, wu2024metagenomicinsightsinto media 6bd2f532)

2. **Jurdzinski KT, Mehrshad M, Delgado LF, Deng Z, Bertilsson S, Andersson AF.** *Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity.* **Science Advances** (Published 2023-05-26; corrected 2024-05-24 per article footer). DOI: **10.1126/sciadv.adg2059**. URL: https://doi.org/10.1126/sciadv.adg2059 (jurdzinski2023largescalephylogenomicsof pages 11-12)

3. **Galisteo C, de la Haba RR, Sánchez-Porro C, Ventosa A.** *A step into the rare biosphere: genomic features of the new genus Terrihalobacillus and the new species Aquibacillus salsiterrae from hypersaline soils.* **Frontiers in Microbiology** (Published 2023-05). DOI: **10.3389/fmicb.2023.1192059**. URL: https://doi.org/10.3389/fmicb.2023.1192059 (galisteo2023astepinto pages 13-14, galisteo2023astepinto pages 14-17)

4. **Bonnaud E, Oger PM, Ohayon A, Louis Y.** *Haloarchaea as Promising Chassis to Green Chemistry.* **Microorganisms** (Published 2024-08). DOI: **10.3390/microorganisms12081738**. URL: https://doi.org/10.3390/microorganisms12081738 (bonnaud2024haloarchaeaaspromising pages 2-4)


References

1. (wu2024metagenomicinsightsinto pages 1-2): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

2. (wu2024metagenomicinsightsinto pages 13-14): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

3. (bonnaud2024haloarchaeaaspromising pages 2-4): Emma Bonnaud, Philippe M. Oger, Avigaël Ohayon, and Yoann Louis. Haloarchaea as promising chassis to green chemistry. Microorganisms, 12:1738, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081738, doi:10.3390/microorganisms12081738. This article has 7 citations.

4. (galisteo2023astepinto pages 13-14): Cristina Galisteo, Rafael R. de la Haba, Cristina Sánchez-Porro, and Antonio Ventosa. A step into the rare biosphere: genomic features of the new genus terrihalobacillus and the new species aquibacillus salsiterrae from hypersaline soils. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1192059, doi:10.3389/fmicb.2023.1192059. This article has 12 citations and is from a peer-reviewed journal.

5. (wu2024metagenomicinsightsinto pages 11-13): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

6. (jurdzinski2023largescalephylogenomicsof pages 11-12): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 60 citations and is from a highest quality peer-reviewed journal.

7. (galisteo2023astepinto pages 14-17): Cristina Galisteo, Rafael R. de la Haba, Cristina Sánchez-Porro, and Antonio Ventosa. A step into the rare biosphere: genomic features of the new genus terrihalobacillus and the new species aquibacillus salsiterrae from hypersaline soils. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1192059, doi:10.3389/fmicb.2023.1192059. This article has 12 citations and is from a peer-reviewed journal.

8. (jurdzinski2023largescalephylogenomicsof pages 1-1): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 60 citations and is from a highest quality peer-reviewed journal.

9. (wu2024metagenomicinsightsinto media 22d779d4): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

10. (wu2024metagenomicinsightsinto media 6bd2f532): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.