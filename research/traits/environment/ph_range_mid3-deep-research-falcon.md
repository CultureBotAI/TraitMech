---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:50:06.208105'
end_time: '2026-06-18T01:08:31.366114'
duration_seconds: 1105.16
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range mid3
  trait_identifier: METPO:1000463
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_mid3
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH range phenotype in which the growth-supporting external pH range\
    \ spans approximately 8\u201310, characteristic of alkaliphile physiology."
  parent_traits: METPO:1000332
  synonyms: Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, Facultative acidophile,
    pHR_8_to_10
  evidence_summary: "DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review\
    \ supports alkaliphile physiology growing across pH 8\u201310.)"
  causal_graph_summary: 'ph_range_mid3_alkaliphile_range: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range mid3
- **METPO identifier:** METPO:1000463
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 8–10, characteristic of alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, Facultative acidophile, pHR_8_to_10
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports alkaliphile physiology growing across pH 8–10.)
- **Existing causal graph summary:** ph_range_mid3_alkaliphile_range: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid3.yaml`.

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
- **Trait label:** pH range mid3
- **METPO identifier:** METPO:1000463
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 8–10, characteristic of alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, Facultative acidophile, pHR_8_to_10
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports alkaliphile physiology growing across pH 8–10.)
- **Existing causal graph summary:** ph_range_mid3_alkaliphile_range: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid3.yaml`.

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


## Curation-focused research report: Microbial trait **pH range mid3** (METPO:1000463)

### Scope summary (TraitMech interpretation)
**pH range mid3** represents a growth-supporting **external** pH window spanning approximately **pH 8–10**, consistent with **alkaliphile/alkali-resistant physiology**. Definitions in the recent literature vary: a commonly used definition is that alkaliphiles grow optimally **above pH 9** (often ~pH 10–12), while some authors adopt a broader threshold (thriving at **pH > 8**). Importantly, **alkali-tolerant** organisms may grow at alkaline pH but often have a **growth optimum below pH 8**; “facultative” alkaliphiles/tolerant organisms can overlap with neutral pH growth and thus create boundary cases for this trait class. These definitional and boundary issues are explicitly discussed in recent reviews, and they imply that **assay conditions** (buffer system, sodium/carbonate, ionic strength) can shift the apparent pH niche. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2, rekadwad2023extremophilesthespecies pages 8-10)

Operationally for curation into `ph_range_mid3.yaml`, this trait should be interpreted as:
- **Phenotype:** ability to grow when external pH is maintained in the alkaline range (~8–10).
- **Mechanistic hallmark:** systems maintaining **cytoplasmic pH near neutral** despite low extracellular proton availability (“inverted pH gradient”), frequently using **Na+ cycles** and **cation/proton antiporters**. (jong2023membraneproteomeof pages 1-2)

### Trait scope: boundary cases and nearby traits
1. **Obligate alkaliphile vs alkalitolerant**: organisms whose **optimum is above pH 9** and that are impaired near neutral pH align with strict alkaliphily; organisms that grow at pH 8–10 but also grow well at pH ~7 may be better represented as “alkali-resistant/alkalitolerant.” (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2, rekadwad2023extremophilesthespecies pages 8-10)
2. **Haloalkaliphiles**: alkaline growth can be **sodium-dependent**, and Na+ requirements can change with pH, confounding purely “pH” traits with “salt” traits. (krishna2021comparativegenomeanalysis pages 12-14)
3. **Extremes beyond mid3**: growth at pH ≥10–12 (“hyperalkaliphily”) is adjacent to but beyond the mid3 window; many systems discussed for alkaliphiles also apply there, but the trait label here is specifically centered on **8–10**.

### Recent developments and current understanding (2023–2024 prioritized)

#### Quantitative pH growth-range data (recent primary studies)
- **Thermoalkaliphile** *Caldalkalibacillus thermarum* TA2.A1: reported to grow from **pH 7.5 to pH 11**, spanning the mid3 range and beyond. (jong2023membraneproteomeof pages 1-2)
- **Alkaliphilic/alkalitolerant aceticlastic methanogens** (Frontiers 2023): strain M04Ac grew from **pH 7.5–10.0** (optimum 9.0); strain Mx grew from **pH 7.7–10.2** (optimum 9.3–9.5) with optimal total Na+ of **0.2–0.3 M**. These are strong, recent examples that map directly onto pH range mid3. (khomyakova2023phenotypicandgenomic pages 1-2)

#### Antiporter-centric alkaline adaptation: Mrp and NhaC
- **Mrp-type Na+/H+ antiporters (mechanistic detail)**: high-resolution cryo-EM + molecular dynamics of the **Mrp antiporter from an alkaliphilic Bacillus** provides a detailed model for coupled Na+/H+ transport. The paper describes Mrp antiporters as **essential for growth** of many alkaliphilic/halophilic bacteria under stress and explicitly links them to **pH and Na+ homeostasis**. A key mechanistic advance is a proposed **histidine-switch** in MrpA that enables proton transfer coupled to gated sodium translocation (diagrammed in the paper’s mechanistic schematic). (lee2022iontransfermechanisms pages 1-2, lee2022iontransfermechanisms pages 8-9, lee2022iontransfermechanisms media c9c04a9d)
- **NhaC family antiporters (functional demonstration, 2023)**: two archaeal NhaC antiporters (**NhaC1/NhaC2**) from *Natronorubrum daqingense* increased **alkaline pH resistance** when expressed in *E. coli* KNabc, extending growth to approximately **pH 8.5 (NhaC1)** and **pH 9.5 (NhaC2)**. Antiport activity was **pH-dependent** across **pH 7–10** with an optimum at **pH 9.5** in vesicle assays. This provides a strong gene-to-phenotype link relevant to mid3. (wang2023characterizationoftwo pages 7-8)

#### Bioenergetics: sodium cycling and ATP synthase adaptation
- **Na+-translocating F1Fo-ATPase in a polyextremophile (2024 AEM)**: *Natranaerobius thermophilus* (grown at pH 9.5 in carbonate-buffered medium) is reported to possess a **Na+-translocating FOF1-ATPase** and to upregulate **Na+/K+/H+ transporters**, consistent with a sodium-linked bioenergetic strategy in haloalkaline conditions. (xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Thermoalkaliphile membrane proteome benchmark (2023 Frontiers)**: the TA2.A1 membrane proteome includes a complete oxidative phosphorylation pathway and discusses that alkaliphiles may harness **either proton or sodium gradients** via ATP synthase to maintain energy generation under alkaline conditions with low external proton availability. (jong2023membraneproteomeof pages 1-2)

#### Compatible solutes and osmotic/pH co-adaptation
- Membrane proteomics detected transporters for **ectoine and glycine betaine** in TA2.A1, proposed to support maintaining near-neutral internal pH under alkaline conditions (caveated as “may assist”). (jong2023membraneproteomeof pages 1-2)
- In *Natranaerobius thermophilus*, multi-omics evidence supports increased intracellular **glycine betaine, glutamate, and proline** with rising salinity at pH 9.5, with implicated transporters (Opu/ProU) and synthesis pathways; while the perturbation was salinity, it is ecologically coupled to alkaline soda lake conditions and supports a haloalkaline adaptation module relevant to mid3 in many systems. (xing2024thepolyextremophilenatranaerobius pages 1-2)
- In alkaliphilic aceticlastic methanogens, genomes encoded **ectoine biosynthesis**, highlighted as the first evidence of ectoine formation in archaea in this context. (khomyakova2023phenotypicandgenomic pages 1-2)

#### Cell envelope adaptations: acidic cell wall polymers and membrane lipids
- Comparative evidence for alkaliphilic Bacilli indicates cell-wall reinforcement with **negatively charged acidic polymers** such as **teichuronic acid**, hypothesized to repel hydroxyl ions and bind Na+/H+ at the cell surface, contributing to alkaline tolerance. (krishna2021comparativegenomeanalysis pages 1-2)
- Membrane lipid adaptation hypotheses include enrichment in **negatively charged phospholipids** including **cardiolipin**, and *A. okhensis* encodes multiple cardiolipin synthases; however, direct lipidomics/causal tests are flagged as needing follow-up. (krishna2021comparativegenomeanalysis pages 11-12)

### Candidate causal-graph nodes (grouped by type)

#### A) Phenotype / environment / assay context
- **METPO:1000463 pH range mid3** (trait)
- **ENVO: alkaline environment** (suggested label; soda lake / alkaline habitat context) (rekadwad2023extremophilesthespecies pages 8-10)
- **Carbonate-buffered medium** / sodium carbonate-buffered medium (assay factor) (xing2024thepolyextremophilenatranaerobius pages 1-2, rekadwad2023extremophilesthespecies pages 8-10)
- **External Na+ availability** / ionic strength (experimental factor; can be required for alkaline growth in some taxa) (krishna2021comparativegenomeanalysis pages 12-14)

#### B) Genes/proteins/complexes (transport and bioenergetics)
- **MrpABCDEFG complex** (Na+/H+ antiporter; “multiple resistance and pH adaptation”) (lee2022iontransfermechanisms pages 1-2, jong2024quantitativeproteomicsreveals pages 1-2)
- **NhaC-family Na+(K+,Li+)/H+ antiporters** (e.g., NhaC1/NhaC2) (wang2023characterizationoftwo pages 7-8)
- **Na+-translocating F1Fo-ATPase** (in some haloalkaliphiles) (xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Electron transport chain / oxidative phosphorylation components** (TA2.A1 detected complete OXPHOS pathway) (jong2023membraneproteomeof pages 1-2)

#### C) Pathways and processes
- **Cation/proton antiport** (cytoplasmic acidification / pH homeostasis) (krishna2021comparativegenomeanalysis pages 1-2, krishna2021comparativegenomeanalysis pages 12-14)
- **Compatible-solute transport and biosynthesis** (glycine betaine uptake, ectoine pathway, proline/glutamate synthesis) (xing2024thepolyextremophilenatranaerobius pages 1-2, khomyakova2023phenotypicandgenomic pages 1-2, jong2023membraneproteomeof pages 1-2)
- **Cell wall organization / acidic polymer enrichment** (teichuronic acid-related) (krishna2021comparativegenomeanalysis pages 1-2)
- **Membrane lipid remodeling / cardiolipin biosynthesis** (candidate; evidence indirect in extracted text) (krishna2021comparativegenomeanalysis pages 11-12)

#### D) Chemicals (candidate CHEBI nodes)
- **Na+** (sodium ion) (krishna2021comparativegenomeanalysis pages 12-14)
- **H+** (proton) (krishna2021comparativegenomeanalysis pages 1-2)
- **Sodium carbonate / bicarbonate** (buffering agents; assay and environment) (rekadwad2023extremophilesthespecies pages 8-10)
- **Glycine betaine, ectoine, glutamate, proline** (compatible solutes) (xing2024thepolyextremophilenatranaerobius pages 1-2, jong2023membraneproteomeof pages 1-2)

### Key mechanistic model (expert synthesis grounded in sources)
Under external pH ~8–10, many alkaliphiles maintain a **more acidic cytoplasm** relative to their environment (“inverted pH gradient”), which challenges proton-dependent bioenergetics and transport. A central adaptive theme is reliance on **Na+-coupled energetics and transport**, including **Na+/H+ antiporters** that import scarce protons in exchange for sodium, supporting cytoplasmic pH control and enabling continued respiration/ATP synthesis. The Mrp complex is one of the best-resolved examples, with current (cryo-EM/MD) mechanistic models specifying proton and sodium pathways and a residue-level switching mechanism (histidine switch) that couples proton transfer to sodium translocation. (jong2023membraneproteomeof pages 1-2, lee2022iontransfermechanisms pages 1-2, lee2022iontransfermechanisms pages 8-9, lee2022iontransfermechanisms media c9c04a9d)

### Evidence-backed candidate edges (curation table)
The following table is designed for direct use in TraitMech curation (subject–predicate–object edges with supporting snippets, notes, and grounding suggestions):

| Edge (Subject —predicate→ Object) | Evidence snippet | Reference | Evidence strength | Notes for TraitMech curation | Suggested ontology grounding |
|---|---|---|---|---|---|
| Mrp Na+/H+ antiporter complex —maintains→ intracellular pH homeostasis under alkaline stress | Mrp antiporters are described as “essential for growth of a variety of halophilic and alkaliphilic bacteria under stress conditions” and for maintaining intracellular pH and sodium homeostasis; structural work identifies proton/sodium translocation pathways and a histidine-switch mechanism in MrpA (lee2022iontransfermechanisms pages 1-2, lee2022iontransfermechanisms pages 8-9) | Lee, 2022, *Ion transfer mechanisms in Mrp-type antiporters from high resolution cryoEM and molecular dynamics simulations*, https://doi.org/10.1038/s41467-022-33640-y, Jan 2022 | strong | Mechanistic support is strong, but direct trait edge is inferred from an alkaliphilic Bacillus model rather than universal across all taxa; best curated as a conserved mechanism for many alkaliphiles, not all organisms with pH 8–10 growth (lee2022iontransfermechanisms pages 1-2, lee2022iontransfermechanisms pages 8-9) | GO:cation transmembrane transporter activity (candidate); GO:sodium:proton antiporter activity (candidate); CHEBI:29101 sodium(1+); CHEBI:15378 proton; NCBITaxon:Bacillus pseudofirmus (label) |
| MrpA histidine-switch mechanism —enables→ proton-coupled Na+ translocation by Mrp | Cryo-EM/MD support that “a histidine moves between three hydrated pathways to enable proton transfer that drives gated transmembrane sodium translocation”; proposed stoichiometry is electrogenic antiport with ~2H+ per Na+ (lee2022iontransfermechanisms pages 8-9, lee2022iontransfermechanisms media c9c04a9d) | Lee, 2022, *Ion transfer mechanisms in Mrp-type antiporters from high resolution cryoEM and molecular dynamics simulations*, https://doi.org/10.1038/s41467-022-33640-y, Jan 2022 | strong | Very specific mechanistic edge at subunit/residue level; useful for mechanistic annotation but probably too fine-grained for a generic trait graph unless residue-level nodes are allowed | MrpA subunit (label); CHEBI:29101 sodium(1+); CHEBI:15378 proton |
| NhaC-family Na+/H+ antiporter —increases→ alkaline pH tolerance | Heterologous expression of *nhaC1* and *nhaC2* from *Natronorubrum daqingense* allowed E. coli KNabc growth “up to pH 8.5/9.5,” and antiport activity was pH-dependent from pH 7.0–10.0 with optimum at pH 9.5 (wang2023characterizationoftwo pages 7-8) | Wang, 2023, *Characterization of Two Na+(K+, Li+)/H+ Antiporters from Natronorubrum daqingense*, https://doi.org/10.3390/ijms241310786, Jun 2023 | strong | Strong functional evidence, but assay is complementation in E. coli and taxon-specific to archaeal antiporters; curate as transporter-level mechanism with assay note | GO:sodium:proton antiporter activity (candidate); CHEBI:29101 sodium(1+); CHEBI:30145 lithium(1+); CHEBI:29103 potassium(1+); CHEBI:15378 proton; NCBITaxon:Natronorubrum daqingense (label) |
| External Na+ availability —supports→ growth across alkaline pH range | In *Alkalihalobacillus okhensis*, growth assays showed no growth without NaCl across pH 7–10; 0.5% NaCl permitted growth only at pH 10, 2% NaCl permitted growth at pH 8–10, and ~4% NaCl supported survival across tested pH values (krishna2021comparativegenomeanalysis pages 12-14) | Krishna, 2021, *Comparative genome analysis of Alkalihalobacillus okhensis Kh10-101T reveals insights into adaptive mechanisms for halo-alkali tolerance*, https://doi.org/10.1007/s13205-021-02938-x, Jul 2021 | strong | Good physiology edge linking environmental sodium to apparent alkaliphily; likely taxon- and medium-dependent, especially for haloalkaliphiles | CHEBI:29101 sodium(1+); ENVO:alkaline environment (label); NCBITaxon:Alkalihalobacillus okhensis (label) |
| Na+/H+ antiport activity —acidifies→ cytoplasm during alkaline growth | The A. okhensis study states alkaliphiles “rely heavily on dedicated, highly effective Na+/H+ antiporters” that import H+ in exchange for Na+, thereby acidifying the cytoplasm for pH homeostasis (krishna2021comparativegenomeanalysis pages 1-2, krishna2021comparativegenomeanalysis pages 12-14) | Krishna, 2021, *Comparative genome analysis of Alkalihalobacillus okhensis Kh10-101T reveals insights into adaptive mechanisms for halo-alkali tolerance*, https://doi.org/10.1007/s13205-021-02938-x, Jul 2021 | moderate | Mechanistic statement is persuasive but partly interpretive/genome-guided; direct biochemical measurement of cytoplasmic pH not shown in extracted passage | GO:sodium:proton antiporter activity (candidate); GO:intracellular pH reduction / pH homeostasis (candidate); CHEBI:15378 proton; CHEBI:29101 sodium(1+) |
| Na+-translocating F1Fo-ATPase —supports→ bioenergetics at high pH | *Natranaerobius thermophilus* is reported to possess a “Na+-translocating FOF1-ATPase,” consistent with sodium-coupled ATP synthesis/ion cycling in alkaline, hypersaline conditions (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing, 2024, *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+*, https://doi.org/10.1128/AEM.00145-24, May 2024 | moderate | Strong organism-specific evidence for Na+-coupled ATPase, but not all alkaliphiles use Na+-coupled ATP synthases; curate as taxon-specific or subgroup mechanism | GO:ATP synthesis coupled ion transmembrane transport (candidate); CHEBI:29101 sodium(1+); NCBITaxon:Natranaerobius thermophilus (label) |
| F1Fo-ATP synthase subunit adaptations —enable→ ATP synthesis under alkaline conditions | A cited thermoalkaliphile example indicates “a specific adaptation in the a subunit of thermoalkaliphilic F1Fo-ATP synthase permits ATP synthesis at high pH but not at neutral pH” (jong2023membraneproteomeof pages 9-10) | de Jong, 2023, *Membrane proteome of the thermoalkaliphile Caldalkalibacillus thermarum TA2.A1*, https://doi.org/10.3389/fmicb.2023.1228266, Jul 2023 | moderate | Valuable mechanistic concept, but extracted passage summarizes prior literature rather than direct assay within the paper; use with caution unless primary ATPase paper is added | GO:ATP synthase activity (candidate); GO:proton motive force-driven ATP synthesis (candidate); NCBITaxon:Caldalkalibacillus thermarum (label) |
| Glycine betaine / ectoine transporters —contribute to→ near-neutral internal pH and alkaline adaptation | Membrane proteomics in *C. thermarum* detected transporters for ectoine and glycine betaine, “osmolytes that may assist in maintaining a near neutral internal pH when the external pH is highly alkaline” (jong2023membraneproteomeof pages 1-2) | de Jong, 2023, *Membrane proteome of the thermoalkaliphile Caldalkalibacillus thermarum TA2.A1*, https://doi.org/10.3389/fmicb.2023.1228266, Jul 2023 | moderate | Good proteomic evidence for transporter presence, but causal link to pH homeostasis is phrased as “may assist”; curate as tentative unless corroborated with phenotype assays | CHEBI:glycine betaine (candidate); CHEBI:ectoine (candidate); GO:compatible solute transmembrane transporter activity (candidate); NCBITaxon:Caldalkalibacillus thermarum (label) |
| Glycine betaine / glutamate / proline accumulation —supports→ adaptation to haloalkaline stress | Proteome, transcript, and metabolite data in *N. thermophilus* showed increased intracellular glycine betaine, glutamate, and proline with rising salinity, alongside transporter/synthesis pathways, supporting a hybrid compatible-solute strategy in alkaline high-Na+ conditions (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing, 2024, *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+*, https://doi.org/10.1128/AEM.00145-24, May 2024 | strong | Strong multi-omics support, but primary phenotype tested is long-term salinity adaptation at pH 9.5 rather than isolated pH effect; best curated as haloalkaline adaptation node/edge | CHEBI:glycine betaine (candidate); CHEBI:glutamate(2-) (candidate); CHEBI:proline (candidate); GO:osmotic stress response (candidate); NCBITaxon:Natranaerobius thermophilus (label) |
| Opu/ProU-family compatible-solute transporters —mediate→ glycine betaine uptake during haloalkaline adaptation | The 2024 AEM study reports that *N. thermophilus* uses “glycine betaine ABC transporters (Opu and ProU families)” and Na+/solute symporters during adaptation to alkaline hypersaline conditions (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing, 2024, *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+*, https://doi.org/10.1128/AEM.00145-24, May 2024 | strong | Well-supported transporter-level edge, but specific contribution to pH 8–10 growth versus salinity adaptation remains partly bundled | GO:betaine transmembrane transporter activity (candidate); CHEBI:glycine betaine (candidate); NCBITaxon:Natranaerobius thermophilus (label) |
| Ectoine biosynthesis —contributes to→ alkaline/saline adaptation | Alkaliphilic aceticlastic methanogens encoded “ectoine biosynthesis,” noted as the first evidence for formation of this osmoprotectant in archaea from haloalkaline habitats (khomyakova2023phenotypicandgenomic pages 1-2) | Khomyakova, 2023, *Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens and proposal of a novel genus Methanocrinis gen. nov. within the family Methanotrichaceae*, https://doi.org/10.3389/fmicb.2023.1233691, Oct 2023 | moderate | Genome-based evidence for pathway presence in alkaliphilic archaea; direct knockout/physiology not shown in extracted text | CHEBI:ectoine (candidate); MetaCyc:ectoine biosynthesis (candidate); NCBITaxon:Methanocrinis natronophilus / Methanocrinis alkalitolerans (label) |
| Teichuronic acid / acidic cell-wall polymers —contribute to→ alkaline pH tolerance | Alkaliphilic Bacilli are described as reinforcing the cell wall with “a dense layer of negatively charged teichuronic acid and other acidic polymers,” hypothesized to repel OH− and adsorb Na+ and H+; high-pH shifts cause envelope damage when this protection is insufficient (krishna2021comparativegenomeanalysis pages 1-2, krishna2021comparativegenomeanalysis pages 15-17) | Krishna, 2021, *Comparative genome analysis of Alkalihalobacillus okhensis Kh10-101T reveals insights into adaptive mechanisms for halo-alkali tolerance*, https://doi.org/10.1007/s13205-021-02938-x, Jul 2021 | moderate | Plausible, often-cited alkaliphile mechanism; extracted support is partly inferential and based on comparative genomics plus morphology | teichuronic acid (label); GO:cell wall organization (candidate); CHEBI:hydroxide (candidate) |
| Teichuronopeptide —supports→ pH homeostasis in alkaliphilic Bacillus | de Jong 2023 cites prior evidence that the cell-wall component “teichuronopeptide” contributes to pH homeostasis and alkaliphily in *Bacillus lentus* C-125 (jong2023membraneproteomeof pages 9-10) | de Jong, 2023, *Membrane proteome of the thermoalkaliphile Caldalkalibacillus thermarum TA2.A1*, https://doi.org/10.3389/fmicb.2023.1228266, Jul 2023 | weak | Secondary citation within review/discussion context, not direct new evidence from de Jong 2023; should be curated only after retrieving original Bacillus lentus paper | teichuronopeptide (label); GO:cell wall organization (candidate); NCBITaxon:Bacillus lentus C-125 (label) |
| Cardiolipin-rich / negatively charged membrane lipids —support→ pH homeostasis at high pH | Comparative genomics notes alkaliphiles tend to have membranes enriched in negatively charged phospholipids including cardiolipin; A. okhensis encodes three cardiolipin synthases, and cardiolipin is noted as “especially important for pH homeostasis” (krishna2021comparativegenomeanalysis pages 11-12) | Krishna, 2021, *Comparative genome analysis of Alkalihalobacillus okhensis Kh10-101T reveals insights into adaptive mechanisms for halo-alkali tolerance*, https://doi.org/10.1007/s13205-021-02938-x, Jul 2021 | moderate | Comparative and genomic evidence rather than direct lipidomics/phenotype in extracted text; taxon-specific follow-up desirable | CHEBI:cardiolipin (candidate); GO:cardiolipin biosynthetic process (candidate); GO:membrane organization (candidate) |
| Carbonate-buffered alkaline medium —enables assay/observation of→ alkaliphile growth phenotype | Alkaliphiles are commonly cultured with sodium carbonate to set pH around 10; *N. thermophilus* cultures were grown anaerobically in carbonate-buffered medium at pH 9.5, and alkaline methanogens were enriched in sodium carbonate/bicarbonate buffer near pH 9.5 (rekadwad2023extremophilesthespecies pages 8-10, xing2024thepolyextremophilenatranaerobius pages 1-2, khomyakova2023phenotypicandgenomic pages 1-2) | Rekadwad, 2023, *Extremophiles: the species that evolve and survive under hostile conditions*, https://doi.org/10.1007/s13205-023-03733-6, Aug 2023; Xing, 2024, https://doi.org/10.1128/AEM.00145-24, May 2024; Khomyakova, 2023, https://doi.org/10.3389/fmicb.2023.1233691, Oct 2023 | strong | Important experimental-factor edge: carbonate and sodium buffering can shape measured pH niche; useful in TraitMech as assay context rather than intrinsic mechanism | CHEBI:sodium carbonate (candidate); CHEBI:bicarbonate (candidate); ENVO:alkaline environment (label) |
| Growth-supporting pH range 7.5–10.2 / 7.5–11 —is evidence for→ pH range mid3 phenotype | Examples from recent primary studies: *C. thermarum* grows from pH 7.5 to 11; alkaliphilic methanogen strain M04Ac grows from 7.5–10.0 and strain Mx from 7.7–10.2 with optimum 9.3–9.5 (jong2023membraneproteomeof pages 1-2, khomyakova2023phenotypicandgenomic pages 1-2) | de Jong, 2023, *Membrane proteome of the thermoalkaliphile Caldalkalibacillus thermarum TA2.A1*, https://doi.org/10.3389/fmicb.2023.1228266, Jul 2023; Khomyakova, 2023, *Phenotypic and genomic characterization...*, https://doi.org/10.3389/fmicb.2023.1233691, Oct 2023 | strong | This is a phenotype-defining edge rather than mechanism; useful to delimit trait scope and boundary cases around pH 8–10 | METPO:1000463; PATO/growth at alkaline pH (candidate); NCBITaxon-specific labels |
| Facultative/alkalitolerant growth near neutral pH —distinguishes→ boundary cases from obligate alkaliphily | Recent definitions note alkaliphiles often have optima >pH 9, whereas alkali-tolerant organisms can grow at alkaline pH but may have optima <8; facultative alkaliphiles may also grow at acidic pH (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2, rekadwad2023extremophilesthespecies pages 8-10) | Fernández-López, 2023, *Alkaliphilic/Alkali-Tolerant Fungi: Molecular, Biochemical, and Biotechnological Aspects*, https://doi.org/10.3390/jof9060652, Jun 2023; Rekadwad, 2023, *Extremophiles: the species that evolve and survive under hostile conditions*, https://doi.org/10.1007/s13205-023-03733-6, Aug 2023 | moderate | Scope/definition edge, not molecular causation; include only if TraitMech graph models phenotype classes and exclusions | METPO:1000463; alkaliphile (label); alkali-tolerant organism (label) |


*Table: This table summarizes curation-ready candidate causal edges for the pH range mid3 trait, linking alkaline growth to transport, bioenergetics, osmoadaptation, cell-envelope mechanisms, and assay context. It is designed to help prioritize which edges are strong enough for TraitMech curation and which need caution due to taxon specificity or indirect evidence.*

### Visual evidence (for mechanistic curation)
The structural/mechanistic schematic for the Mrp antiporter (including the proposed **histidine-switch** and putative ion pathways) is available as cropped figure evidence from Lee et al. 2022. (lee2022iontransfermechanisms media c9c04a9d, lee2022iontransfermechanisms media ec1ad568, lee2022iontransfermechanisms media ccbf6fbb)

### Current applications and real-world implementations (linked to pH mid3 physiology)
Although the extracted evidence in this run focuses on mechanisms rather than engineering deployments, recent reviews emphasize that alkaliphiles/alkali-tolerant microbes are actively leveraged because alkaline pH is common in industrial streams (e.g., detergent enzymes, textile and leather processing, and alkaline wastewater contexts). For eukaryotic microbes, a 2023 review highlights industrial relevance of **alkali-stable enzymes** (e.g., proteases) and pH-regulated pathways in model fungi, illustrating why growth/function at pH >8–9 is commercially important. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 12-13, fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2)

### Relevant statistics and data points (from included sources)
- *Methanocrinis* strains: growth windows **7.5–10.0** and **7.7–10.2** with optima ~**9.0–9.5**; Na+ optimum **0.2–0.3 M**. (khomyakova2023phenotypicandgenomic pages 1-2)
- TA2.A1: growth from **pH 7.5 to pH 11**. (jong2023membraneproteomeof pages 1-2)
- NhaC antiporters: antiport activity pH range **7.0–10.0**; optimum **pH 9.5**; complementation supports growth to **pH 8.5–9.5** (depending on NhaC). (wang2023characterizationoftwo pages 7-8)
- Sodium dependence example (*A. okhensis*): growth assays show no growth without NaCl across tested pH; 0.5% NaCl supports growth only at **pH 10**, while 2% supports **pH 8–10**. (krishna2021comparativegenomeanalysis pages 12-14)

### Warnings / claims not yet ready for curation
1. **Transporter presence ≠ causal necessity**: proteomic detection of compatible-solute transporters (glycine betaine/ectoine) supports node inclusion but the causal phrasing (“may assist”) is tentative without mutant phenotypes. (jong2023membraneproteomeof pages 1-2)
2. **Membrane lipid/cardiolipin edges are partly inferential**: comparative-genomics statements about cardiolipin and negative phospholipids are plausible but not direct functional tests in the extracted text; best curated as **hypothesis/uncertain** unless lipidomics or genetic perturbations are added. (krishna2021comparativegenomeanalysis pages 11-12)
3. **Mrp essentiality is broad but not universal**: Lee 2022 supports strong mechanistic confidence for Mrp antiporters and states essentiality in many organisms, but trait curation should avoid over-generalizing to all taxa with pH 8–10 growth. (lee2022iontransfermechanisms pages 1-2)
4. **Assay coupling to Na+/carbonate**: carbonate buffers and sodium concentrations are both natural and experimental covariates in alkaline systems; “pH range” phenotypes may shift under different buffer ions, osmolarity, or carbon sources and should be explicitly recorded as experimental conditions when curating. (xing2024thepolyextremophilenatranaerobius pages 1-2, rekadwad2023extremophilesthespecies pages 8-10)

---

## DOI-first bibliography (with URLs and publication dates where available)
- Lee Y, Haapanen O, Altmeyer A, Kühlbrandt W, Sharma V, Zickermann V. **Ion transfer mechanisms in Mrp-type antiporters from high resolution cryoEM and molecular dynamics simulations.** *Nature Communications*. **Jan 2022**. DOI: **10.1038/s41467-022-33640-y**. URL: https://doi.org/10.1038/s41467-022-33640-y (lee2022iontransfermechanisms pages 1-2, lee2022iontransfermechanisms pages 8-9)
- Wang Q, Qiao M, Song J. **Characterization of Two Na+(K+, Li+)/H+ Antiporters from Natronorubrum daqingense.** *International Journal of Molecular Sciences*. **Jun 2023**. DOI: **10.3390/ijms241310786**. URL: https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8)
- de Jong SI, Sorokin DY, van Loosdrecht MCM, Pabst M, McMillan DGG. **Membrane proteome of the thermoalkaliphile Caldalkalibacillus thermarum TA2.A1.** *Frontiers in Microbiology*. **Jul 2023**. DOI: **10.3389/fmicb.2023.1228266**. URL: https://doi.org/10.3389/fmicb.2023.1228266 (jong2023membraneproteomeof pages 1-2)
- Khomyakova MA, Merkel AY, Slobodkin AI, Sorokin DY. **Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens and proposal of a novel genus Methanocrinis gen.nov.** *Frontiers in Microbiology*. **Oct 2023**. DOI: **10.3389/fmicb.2023.1233691**. URL: https://doi.org/10.3389/fmicb.2023.1233691 (khomyakova2023phenotypicandgenomic pages 1-2)
- Fernández-López M G, Batista-García RA, Aréchiga-Carvajal ET. **Alkaliphilic/Alkali-Tolerant Fungi: Molecular, Biochemical, and Biotechnological Aspects.** *Journal of Fungi*. **Jun 2023**. DOI: **10.3390/jof9060652**. URL: https://doi.org/10.3390/jof9060652 (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2, fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 12-13)
- Rekadwad BN, Li W-J, Gonzalez JM, et al. **Extremophiles: the species that evolve and survive under hostile conditions.** *3 Biotech*. **Aug 2023**. DOI: **10.1007/s13205-023-03733-6**. URL: https://doi.org/10.1007/s13205-023-03733-6 (rekadwad2023extremophilesthespecies pages 8-10)
- Xing Q, Zhang S, Tao X, et al. **The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.** *Applied and Environmental Microbiology*. **May 2024**. DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2)
- Kim M, Kim W, Park Y, Jung J, Park W. **Lineage-specific evolution of Aquibium… during habitat adaptation.** *Applied and Environmental Microbiology*. **Feb 2024**. DOI: **10.1128/aem.02091-23**. URL: https://doi.org/10.1128/aem.02091-23 (kim2024lineagespecificevolutionof pages 1-2)
- de Jong SI, Wissink M, Yildirim K, Pabst M, van Loosdrecht MCM, McMillan DGG. **Quantitative proteomics reveals oxygen-induced adaptations in Caldalkalibacillus thermarum TA2.A1 microaerobic chemostat cultures.** *Frontiers in Microbiology*. **Oct 2024**. DOI: **10.3389/fmicb.2024.1468929**. URL: https://doi.org/10.3389/fmicb.2024.1468929 (jong2024quantitativeproteomicsreveals pages 1-2)

(Background but older than 2023–2024, used for specific physiology example)
- Krishna PS, Raghunathan S, Prakash JSS. **Comparative genome analysis of Alkalihalobacillus okhensis…** *3 Biotech*. **Jul 2021**. DOI: **10.1007/s13205-021-02938-x**. URL: https://doi.org/10.1007/s13205-021-02938-x (krishna2021comparativegenomeanalysis pages 12-14, krishna2021comparativegenomeanalysis pages 1-2, krishna2021comparativegenomeanalysis pages 11-12)


References

1. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 1-2): Maikel Gilberto Fernández-López, Ramón Alberto Batista-García, and Elva Teresa Aréchiga-Carvajal. Alkaliphilic/alkali-tolerant fungi: molecular, biochemical, and biotechnological aspects. Journal of Fungi, 9:652, Jun 2023. URL: https://doi.org/10.3390/jof9060652, doi:10.3390/jof9060652. This article has 35 citations.

2. (rekadwad2023extremophilesthespecies pages 8-10): Bhagwan Narayan Rekadwad, Wen-Jun Li, Juan M. Gonzalez, Rekha Punchappady Devasya, Arun Ananthapadmanabha Bhagwath, Ruchi Urana, and Khalid Parwez. Extremophiles: the species that evolve and survive under hostile conditions. 3 Biotech, Aug 2023. URL: https://doi.org/10.1007/s13205-023-03733-6, doi:10.1007/s13205-023-03733-6. This article has 49 citations and is from a peer-reviewed journal.

3. (jong2023membraneproteomeof pages 1-2): Samuel I. de Jong, Dimitry Y. Sorokin, Mark C. M. van Loosdrecht, Martin Pabst, and Duncan G. G. McMillan. Membrane proteome of the thermoalkaliphile caldalkalibacillus thermarum ta2.a1. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1228266, doi:10.3389/fmicb.2023.1228266. This article has 5 citations and is from a peer-reviewed journal.

4. (krishna2021comparativegenomeanalysis pages 12-14): Pilla Sankara Krishna, Sarada Raghunathan, and Jogadhenu S. S. Prakash. Comparative genome analysis of alkalihalobacillus okhensis kh10-101 t reveals insights into adaptive mechanisms for halo-alkali tolerance. 3 Biotech, Jul 2021. URL: https://doi.org/10.1007/s13205-021-02938-x, doi:10.1007/s13205-021-02938-x. This article has 8 citations and is from a peer-reviewed journal.

5. (khomyakova2023phenotypicandgenomic pages 1-2): Maria A. Khomyakova, Alexander Y. Merkel, Alexander I. Slobodkin, and Dimitry Y. Sorokin. Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens and proposal of a novel genus methanocrinis gen.nov. within the family methanotrichaceae. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1233691, doi:10.3389/fmicb.2023.1233691. This article has 13 citations and is from a peer-reviewed journal.

6. (lee2022iontransfermechanisms pages 1-2): Yongchan Lee, Outi Haapanen, Anton Altmeyer, Werner Kühlbrandt, Vivek Sharma, and Volker Zickermann. Ion transfer mechanisms in mrp-type antiporters from high resolution cryoem and molecular dynamics simulations. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-022-33640-y, doi:10.1038/s41467-022-33640-y. This article has 28 citations and is from a highest quality peer-reviewed journal.

7. (lee2022iontransfermechanisms pages 8-9): Yongchan Lee, Outi Haapanen, Anton Altmeyer, Werner Kühlbrandt, Vivek Sharma, and Volker Zickermann. Ion transfer mechanisms in mrp-type antiporters from high resolution cryoem and molecular dynamics simulations. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-022-33640-y, doi:10.1038/s41467-022-33640-y. This article has 28 citations and is from a highest quality peer-reviewed journal.

8. (lee2022iontransfermechanisms media c9c04a9d): Yongchan Lee, Outi Haapanen, Anton Altmeyer, Werner Kühlbrandt, Vivek Sharma, and Volker Zickermann. Ion transfer mechanisms in mrp-type antiporters from high resolution cryoem and molecular dynamics simulations. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-022-33640-y, doi:10.1038/s41467-022-33640-y. This article has 28 citations and is from a highest quality peer-reviewed journal.

9. (wang2023characterizationoftwo pages 7-8): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

10. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

11. (krishna2021comparativegenomeanalysis pages 1-2): Pilla Sankara Krishna, Sarada Raghunathan, and Jogadhenu S. S. Prakash. Comparative genome analysis of alkalihalobacillus okhensis kh10-101 t reveals insights into adaptive mechanisms for halo-alkali tolerance. 3 Biotech, Jul 2021. URL: https://doi.org/10.1007/s13205-021-02938-x, doi:10.1007/s13205-021-02938-x. This article has 8 citations and is from a peer-reviewed journal.

12. (krishna2021comparativegenomeanalysis pages 11-12): Pilla Sankara Krishna, Sarada Raghunathan, and Jogadhenu S. S. Prakash. Comparative genome analysis of alkalihalobacillus okhensis kh10-101 t reveals insights into adaptive mechanisms for halo-alkali tolerance. 3 Biotech, Jul 2021. URL: https://doi.org/10.1007/s13205-021-02938-x, doi:10.1007/s13205-021-02938-x. This article has 8 citations and is from a peer-reviewed journal.

13. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

14. (jong2023membraneproteomeof pages 9-10): Samuel I. de Jong, Dimitry Y. Sorokin, Mark C. M. van Loosdrecht, Martin Pabst, and Duncan G. G. McMillan. Membrane proteome of the thermoalkaliphile caldalkalibacillus thermarum ta2.a1. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1228266, doi:10.3389/fmicb.2023.1228266. This article has 5 citations and is from a peer-reviewed journal.

15. (krishna2021comparativegenomeanalysis pages 15-17): Pilla Sankara Krishna, Sarada Raghunathan, and Jogadhenu S. S. Prakash. Comparative genome analysis of alkalihalobacillus okhensis kh10-101 t reveals insights into adaptive mechanisms for halo-alkali tolerance. 3 Biotech, Jul 2021. URL: https://doi.org/10.1007/s13205-021-02938-x, doi:10.1007/s13205-021-02938-x. This article has 8 citations and is from a peer-reviewed journal.

16. (lee2022iontransfermechanisms media ec1ad568): Yongchan Lee, Outi Haapanen, Anton Altmeyer, Werner Kühlbrandt, Vivek Sharma, and Volker Zickermann. Ion transfer mechanisms in mrp-type antiporters from high resolution cryoem and molecular dynamics simulations. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-022-33640-y, doi:10.1038/s41467-022-33640-y. This article has 28 citations and is from a highest quality peer-reviewed journal.

17. (lee2022iontransfermechanisms media ccbf6fbb): Yongchan Lee, Outi Haapanen, Anton Altmeyer, Werner Kühlbrandt, Vivek Sharma, and Volker Zickermann. Ion transfer mechanisms in mrp-type antiporters from high resolution cryoem and molecular dynamics simulations. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-022-33640-y, doi:10.1038/s41467-022-33640-y. This article has 28 citations and is from a highest quality peer-reviewed journal.

18. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 12-13): Maikel Gilberto Fernández-López, Ramón Alberto Batista-García, and Elva Teresa Aréchiga-Carvajal. Alkaliphilic/alkali-tolerant fungi: molecular, biochemical, and biotechnological aspects. Journal of Fungi, 9:652, Jun 2023. URL: https://doi.org/10.3390/jof9060652, doi:10.3390/jof9060652. This article has 35 citations.

19. (kim2024lineagespecificevolutionof pages 1-2): Minkyung Kim, Wonjae Kim, Yerim Park, Jaejoon Jung, and Woojun Park. Lineage-specific evolution of aquibium, a close relative of mesorhizobium, during habitat adaptation. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.02091-23, doi:10.1128/aem.02091-23. This article has 4 citations and is from a peer-reviewed journal.