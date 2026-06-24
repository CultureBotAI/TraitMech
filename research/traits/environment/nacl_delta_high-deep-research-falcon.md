---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:56:24.689781'
end_time: '2026-06-17T23:13:49.438819'
duration_seconds: 1044.75
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl delta high
  trait_identifier: METPO:1000482
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_delta_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl delta phenotype with a growth-supporting NaCl breadth above approximately
    8% (w/v), characteristic of extreme-euryhaline organisms.
  parent_traits: METPO:1000335
  synonyms: Nad_>8
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports very wide salinity-tolerance breadths as the extreme-euryhaline phenotype.)
    | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems
    review supports combined osmolyte / salt-in flexibility as the basis of very wide
    salinity tolerance.)'
  causal_graph_summary: 'nacl_delta_high_extreme_euryhaline: 3 nodes, 2 edges'
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
- **Trait label:** NaCl delta high
- **METPO identifier:** METPO:1000482
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth above approximately 8% (w/v), characteristic of extreme-euryhaline organisms.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports very wide salinity-tolerance breadths as the extreme-euryhaline phenotype.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports combined osmolyte / salt-in flexibility as the basis of very wide salinity tolerance.)
- **Existing causal graph summary:** nacl_delta_high_extreme_euryhaline: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_high.yaml`.

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
- **Trait label:** NaCl delta high
- **METPO identifier:** METPO:1000482
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth above approximately 8% (w/v), characteristic of extreme-euryhaline organisms.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports very wide salinity-tolerance breadths as the extreme-euryhaline phenotype.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports combined osmolyte / salt-in flexibility as the basis of very wide salinity tolerance.)
- **Existing causal graph summary:** nacl_delta_high_extreme_euryhaline: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_high.yaml`.

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


## Research Report: Microbial trait “NaCl delta high” (METPO:1000482) — extreme‑euryhaline salinity breadth >~8% (w/v)

### 0) Scope summary (curation-focused)
**Trait definition (METPO:1000482):** “NaCl delta high” denotes a **growth-supporting salinity breadth** with an **upper NaCl limit above ~8% (w/v)**, characteristic of **extreme-euryhaline** microorganisms. In curation terms, it is best treated as a **phenotypic capacity** observed in growth assays across a wide NaCl range (not merely survival). Engineered and natural examples show that extending growth above ~8% NaCl is feasible via increased osmoprotection and ion homeostasis (e.g., compatible-solute switching to proline). (khanh2024metabolicpathwayengineering pages 1-2)

**Distinguish from nearby traits / boundary cases**
- **Halotolerance vs. euryhalinity:** Halotolerance can mean survival at high salt; METPO:1000482 targets **growth** across a wide range, with an upper bound >8% NaCl. (khanh2024metabolicpathwayengineering pages 1-2)
- **Obligate/extreme halophily (salt-saturating habitats):** Some extreme halophiles thrive at **salt-saturating conditions (~≥30% w/v)** and often rely on “salt-in” physiology (molar intracellular K+) with strongly acidified proteomes; these organisms may have **low-salt growth constraints**, so a wide *breadth* (delta) is not guaranteed. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
- **Environmental definition of hypersalinity:** Hypersaline environments are commonly defined as **>100–150 g/L total dissolved salts**, often reaching saturation; these environmental thresholds help set assay context but do not alone define NaCl breadth. (oren2024novelinsightsinto pages 1-2)
- **Non-NaCl salts / chaotropicity:** High **MgCl2** (chaotropic) brines can inhibit growth above **~1.26 M MgCl2** even when NaCl-tolerance mechanisms exist; do not conflate NaCl breadth with general salt/chaotrope tolerance. (oren2024novelinsightsinto pages 4-5)

### 1) Key concepts and definitions (current understanding)
#### 1.1 “Salt-out” (compatible-solute) strategy
Microbes avoid high intracellular inorganic salt by accumulating **organic compatible solutes** (osmolytes) such as **glycine betaine, trehalose, glutamate, and proline**. This maintains enzyme function while matching external osmolarity. In *Natranaerobius thermophilus*, intracellular **glycine betaine, glutamate, and proline increase with rising salinity**, consistent with salt-out components. (xing2024thepolyextremophilenatranaerobius pages 1-2)

#### 1.2 “Salt-in” strategy
“Salt-in” organisms accumulate **high intracellular inorganic ions** (classically **KCl**), requiring proteomes adapted to function in high ionic strength. In extreme halophilic archaea, intracellular **K+ can reach up to ~4 M**, and **proteome acidification** (very low median pI) is a hallmark of this adaptation. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

#### 1.3 Hybrid / dual strategies and salinity breadth
Environments with **extreme salinity fluctuations** can select for organisms with **hybrid “salt-in”/“salt-out” osmoregulation**, i.e., genomic potential for both strategies to allow scalable response to changing salinity. Dead Sea spring enrichments yielded MAGs containing genes for both strategies. (ionescu2024extremefluctuationsin pages 1-2)

### 2) Recent developments and latest research (prioritizing 2023–2024)
#### 2.1 Dual osmoadaptation quantified across very high salinity (2024)
Xing et al. (2024) quantified long-term salinity adaptation in the polyextremophilic bacterium *Natranaerobius thermophilus* across **2.5–5.0 M total Na+** (≈14.63–29.25% wt/vol Na+) with optimal growth at **3.1–4.3 M Na+**. They show a **dual strategy**: compatible-solute accumulation plus ion (K+) accumulation and transporter remodeling (e.g., TrkH, Opu/ProU, NhaC). (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 1-2)

*Visual evidence:* Growth curves and intracellular solute/K+ changes vs salinity are shown in the retrieved figure crops. (xing2024thepolyextremophilenatranaerobius media f9a64a84, xing2024thepolyextremophilenatranaerobius media 38da44bd)

#### 2.2 Extreme halophily limits and proteome signatures (2024)
Metagenomic analyses of salt-saturating/chaotropic brines show that **salt-in** strategists dominate near the upper limits of life; they display **extremely acidic proteomes** (e.g., median pI ≤4.4) and can accumulate **molar intracellular K+**. Moderate halophiles relying mainly on salt-out strategies are generally absent from NaCl-saturated environments. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

#### 2.3 Salinity transitions and proteome reorganization (2023)
Large-scale phylogenomics across aquatic biomes found that salinity transitions are accompanied by systematic changes in **amino-acid composition and isoelectric point (pI) distributions** and by convergent gene-function gains/losses, consistent with salinity being a deep evolutionary constraint shaping breadth and transitions. (jurdzinski2023largescalephylogenomicsof pages 1-1)

#### 2.4 Engineering osmolyte switching to cross the >8% NaCl threshold (2024)
Khanh et al. (2024) provide direct causal proof that **compatible-solute identity and accumulation** can determine whether growth above ~8% NaCl is possible. An ectoine-deficient *Halomonas elongata* strain that could not grow above **4% NaCl** was engineered to accumulate **proline**, enabling growth (“thrived”) at **8% NaCl** and reaching **353.1 ± 40.5 µmol proline/g cell fresh weight**. (khanh2024metabolicpathwayengineering pages 1-2)

### 3) Current applications and real-world implementations
#### 3.1 Hypersaline bioremediation (hydrocarbons and metals)
A 2025 review compiles numerous implementations where halophiles/euryhaline microbes remediate pollutants under high salinity. Examples with explicit salinity and performance include: **up to 97% fluorene removal at 8–12% NaCl** and **94% Pb reduction (1 mM) at 10% NaCl** by a *Halomonas* strain; other cases include **100% phenanthrene degradation at 10% salinity in 7 days** by *Hortaea* B15. These examples show that NaCl-delta-high physiology has practical value in treating saline industrial effluents and contaminated hypersaline sites. (rezaei2025innovativeapproachesin pages 7-8)

#### 3.2 Biomanufacturing / cell factories for osmolytes
*Halomonas elongata* is used industrially to produce **ectoine**, reportedly inducible when external NaCl exceeds **~3%**, and harvested via a “bacterial milking process.” Engineering can redirect osmolyte production: a GABA-accumulating engineered strain reached **176.94 µmol GABA/g cell dry weight** in **7% NaCl**, improving salt-stress tolerance (useful for robust bioprocessing). (zou2024metabolicengineeringof pages 1-2)

#### 3.3 Salinity-resilient agriculture (microbial inoculants)
Salt-tolerant *Halomonas* strains are being tested as plant growth-promoting rhizobacteria (PGPB) in saline soils. One strain tolerates **up to 14% NaCl** and is proposed to promote maize salt tolerance via altered K+/Na+ handling and antioxidant/ABA responses. Another *Halomonas* inoculant in pot trials reduced soil total salt by **9.33%** and EC by **8.09%** while increasing soil organic matter and nitrogen. (liu2025plantgrowthpromotingrhizobacteria pages 1-2, li2025wholegenomeanalysisof pages 1-2)

### 4) Expert synthesis / authoritative analysis
Across recent reviews and primary studies, a convergent mechanistic picture emerges:
1) **Upper NaCl growth limits** are strongly influenced by the capacity to either (a) accumulate/transport **compatible solutes** or (b) adopt/partially adopt **salt-in** ion accumulation with accompanying proteome adaptation. (xing2024thepolyextremophilenatranaerobius pages 1-2, gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
2) **Hybrid strategies** are plausible and may be selected in strongly fluctuating systems, suggesting that NaCl breadth (“delta”) can be achieved by combining “cheap” salt-in adjustments with “expensive” compatible-solute control depending on timescale and salinity shock magnitude. (ionescu2024extremefluctuationsin pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2)
3) Long-term salinity adaptation leaves **genome-wide and proteome-wide signatures** (pI distribution shifts, amino-acid composition changes), and these changes can constrain cross-biome transitions over evolutionary timescales. (jurdzinski2023largescalephylogenomicsof pages 1-1)

### 5) Relevant statistics and quantitative data (recent studies)
- **Trait-relevant threshold demonstration (>8% NaCl):** engineered *H. elongata* grows at **8% NaCl** via proline accumulation; parental ectoine-deficient strain fails above **4% NaCl**. (khanh2024metabolicpathwayengineering pages 1-2)
- **Very high salinity tolerance in a polyextremophile:** *N. thermophilus* growth reported across **2.5–5.0 M Na+** (≈14.63–29.25% wt/vol Na+). (xing2024thepolyextremophilenatranaerobius pages 6-7)
- **Intracellular osmolyte/ion levels:** proline **353.1 ± 40.5 µmol/g fresh weight** (8% NaCl, engineered *H. elongata*). (khanh2024metabolicpathwayengineering pages 1-2) GABA **176.94 µmol/g dry weight** (7% NaCl, engineered *H. elongata*). (zou2024metabolicengineeringof pages 1-2) Intracellular K+ increases with salinity in *N. thermophilus* (e.g., **227.2 → 440.2 mM** across 2.5–4.3 M Na+). (xing2024thepolyextremophilenatranaerobius pages 19-21)
- **Life at salt saturation and proteome properties:** extreme halophiles can accumulate **up to ~4 M K+** and show **median proteome pI ≤4.4** under near life-limiting chaotropic brines. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
- **Bioremediation at high NaCl:** **97% fluorene removal at 8–12% NaCl**; **94% Pb reduction at 10% NaCl**. (rezaei2025innovativeapproachesin pages 7-8)

---

## Candidate nodes (grouped) for `data/traits/environment/nacl_delta_high.yaml`
The following node inventory is designed for direct causal-graph curation.

| Node label | Node type | Description (1 line) | Suggested CURIE grounding | Key supporting sources (DOI+year) |
|---|---|---|---|---|
| high NaCl/salinity | environmental factor | Elevated external NaCl/Na+ imposes osmotic stress that selects for broad salinity-tolerance mechanisms. | CHEBI:26710 sodium chloride | 10.1128/aem.00145-24 (2024); 10.1038/s44185-024-00050-w (2024) (xing2024thepolyextremophilenatranaerobius pages 1-2, oren2024novelinsightsinto pages 1-2) |
| salinity fluctuation | environmental factor | Rapid and large salinity shifts favor scalable or hybrid osmoadaptation strategies. |  | 10.3389/frmbi.2023.1329925 (2024) (ionescu2024extremefluctuationsin pages 1-2) |
| hypersaline environment | environmental factor | Habitat class with >100–150 g/L salts, often reaching saturation, used to bound the trait’s ecological context. | ENVO:hypersaline environment | 10.1038/s44185-024-00050-w (2024) (oren2024novelinsightsinto pages 1-2) |
| compatible-solute accumulation | process | Salt-out osmoadaptation process based on intracellular buildup of organic osmolytes. | GO:0006970 | 10.1128/aem.00145-24 (2024); 10.3389/frmbi.2023.1329925 (2024) (xing2024thepolyextremophilenatranaerobius pages 1-2, ionescu2024extremefluctuationsin pages 1-2) |
| glycine betaine | metabolite | Major compatible solute accumulated and/or imported during high-salinity adaptation. | CHEBI:17750 | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17) |
| ectoine | metabolite | Canonical bacterial osmoprotectant supporting high-salt growth and industrial production. | CHEBI:17634 | 10.1128/aem.01195-24 (2024); 10.1128/aem.01905-23 (2024) (khanh2024metabolicpathwayengineering pages 1-2, zou2024metabolicengineeringof pages 1-2) |
| hydroxyectoine | metabolite | Hydroxylated ectoine derivative used by halophiles as a stress protectant at high salinity. | CHEBI:60302 | 10.1128/aem.01195-24 (2024) (khanh2024metabolicpathwayengineering pages 1-2) |
| proline | metabolite | Organic osmolyte whose accumulation can restore growth at high NaCl in engineered halophiles. | CHEBI:26271 | 10.1128/aem.01195-24 (2024); 10.1128/aem.00145-24 (2024) (khanh2024metabolicpathwayengineering pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| glutamate | metabolite | Osmolyte and metabolic precursor whose intracellular level rises with salinity in hybrid strategists. | CHEBI:29985 | 10.1128/aem.00145-24 (2024); 10.1128/aem.01905-23 (2024) (xing2024thepolyextremophilenatranaerobius pages 1-2, zou2024metabolicengineeringof pages 1-2) |
| trehalose | metabolite | Widely used compatible solute cited as part of the salt-out strategy in fluctuating salinity systems. | CHEBI:16551 | 10.3389/frmbi.2023.1329925 (2024); 10.1038/s44185-024-00050-w (2024) (ionescu2024extremefluctuationsin pages 1-2, oren2024novelinsightsinto pages 1-2) |
| GABA | metabolite | Alternative engineered osmolyte that improves salt tolerance when accumulated intracellularly. | CHEBI:16865 | 10.1128/aem.01905-23 (2024) (zou2024metabolicengineeringof pages 1-2) |
| salt-in strategy | process | Osmoadaptation strategy based on high intracellular inorganic ion concentrations rather than only organic solutes. | GO:0006970 | 10.1038/s41559-024-02505-6 (2024); 10.3389/frmbi.2023.1329925 (2024) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, ionescu2024extremefluctuationsin pages 1-2) |
| K+ accumulation | process | Intracellular potassium buildup supports osmotic balance and is a core salt-in signature. | GO:0006873 | 10.1128/aem.00145-24 (2024); 10.1038/s41559-024-02505-6 (2024) (xing2024thepolyextremophilenatranaerobius pages 6-7, gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| KCl | metabolite | Intracellular KCl is the characteristic ionic osmolyte of extreme salt-in strategists. | CHEBI:32588 | 10.1038/s41559-024-02505-6 (2024) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| Opu transporter family | complex | ABC-family glycine betaine/compatible-solute uptake systems repeatedly implicated in high-salt adaptation. |  | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17) |
| ProU transporter family | complex | ABC-compatible-solute transporter family contributing to glycine betaine/proline uptake under salt stress. |  | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17) |
| SSS symporter family | gene-protein | Na+/solute symporters implicated in uptake processes supporting adaptation to high salinity. | GO:0015294 | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| TrkH/TrkAH potassium uptake system | complex | Potassium uptake machinery associated with rising intracellular K+ at higher salinity. | GO:0015079 | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 19-21) |
| NhaC Na+/H+ antiporter | gene-protein | Sodium/proton antiporter upregulated at higher salinity to help maintain ion homeostasis. | GO:0015385 | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 6-7) |
| Na+/K+/H+ antiporters | complex | Broad ion-homeostasis systems supporting intracellular K+ maintenance and Na+ control under high salt. |  | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| ectABC ectoine biosynthesis pathway | process | Conserved ectoine biosynthetic module underlying a major bacterial osmoprotectant strategy. | GO:0019491 | 10.1128/aem.01195-24 (2024); 10.1128/aem.01905-23 (2024) (khanh2024metabolicpathwayengineering pages 1-2, zou2024metabolicengineeringof pages 1-2) |
| proB/proA/proC proline biosynthesis pathway | process | Engineered or native proline synthesis pathway enabling intracellular proline buildup and higher NaCl tolerance. | GO:0006561 | 10.1128/aem.01195-24 (2024) (khanh2024metabolicpathwayengineering pages 1-2) |
| gsmt/sdmt betaine synthesis pathway | process | Methylation pathway for de novo glycine betaine synthesis induced in a dual-strategy halophile. |  | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| glutamate decarboxylase (GAD) / GABA synthesis | process | Conversion of glutamate to GABA can improve salt tolerance and pH balance in engineered strains. | GO:0004351 | 10.1128/aem.01905-23 (2024) (zou2024metabolicengineeringof pages 1-2) |
| acidic proteome | phenotype signature | Proteome enriched in acidic proteins, characteristic of salt-in adaptation to very high intracellular salts. |  | 10.1038/s41559-024-02505-6 (2024); 10.1128/aem.00145-24 (2024) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, xing2024thepolyextremophilenatranaerobius pages 19-21) |
| low median proteome pI | phenotype signature | Shift toward lower median isoelectric point is a measurable proteomic hallmark of high-salinity adaptation. |  | 10.1038/s41559-024-02505-6 (2024); 10.1126/sciadv.adg2059 (2023) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, jurdzinski2023largescalephylogenomicsof pages 1-1) |
| D/E enrichment | phenotype signature | Enrichment in aspartate/glutamate residues increases negative surface charge in salt-in proteomes. |  | 10.1038/s41559-024-02505-6 (2024); 10.3390/microorganisms13040761 (2025) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, strakova2025strategiesofenvironmental pages 7-9) |
| growth range in % NaCl | assay factor | Phenotypic breadth metric directly relevant to NaCl-delta-high curation and boundary setting. |  | 10.1128/aem.01195-24 (2024); 10.1128/aem.00145-24 (2024) (khanh2024metabolicpathwayengineering pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| intracellular osmolyte concentration | assay factor | Quantification of compatible solutes used to mechanistically connect salinity to osmoadaptation. |  | 10.1128/aem.00145-24 (2024); 10.1128/aem.01195-24 (2024) (xing2024thepolyextremophilenatranaerobius media f9a64a84, khanh2024metabolicpathwayengineering pages 1-2) |
| ICP-OES for K+ | assay factor | Analytical method used to quantify intracellular potassium as evidence for salt-in behavior. |  | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 6-7) |
| iTRAQ proteomics | assay factor | Quantitative proteomics method used to detect salinity-responsive proteins and pathways. |  | 10.1128/aem.00145-24 (2024) (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 7-10) |
| bioremediation at 8–12% NaCl | application | Broad salinity tolerance enables pollutant degradation and metal removal in hypersaline wastewater or soils. |  | 10.1186/s12934-025-02817-7 (2025) (rezaei2025innovativeapproachesin pages 7-8) |
| ectoine industrial milking | application | Halophilic cell-factory process exploiting salt-triggered ectoine production and release. |  | 10.1128/aem.01905-23 (2024) (zou2024metabolicengineeringof pages 1-2) |
| agricultural PGPB in saline soils | application | Salt-tolerant microbes improve plant salt tolerance, rhizosphere composition, and soil quality under saline stress. |  | 10.1186/s12870-025-06765-7 (2025); 10.3390/microorganisms13081781 (2025) (liu2025plantgrowthpromotingrhizobacteria pages 1-2, li2025wholegenomeanalysisof pages 1-2) |


*Table: This table lists candidate graph nodes for METPO:1000482, organized by mechanistic type and grounded where possible to stable ontology identifiers. It is useful for curating TraitMech node inventories before selecting evidence-backed causal edges.*

---

## Evidence-backed candidate causal edges (triples)
Edges are proposed for curation into the TraitMech graph. Each entry includes an evidence snippet, notes on strength/uncertainty, and suggested ontology grounding.

| Edge (triple) | Evidence snippet | Source (DOI + year) | Notes | Suggested ontology grounding |
|---|---|---|---|---|
| high external salinity → increases → compatible-solute accumulation | “intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/aem.00145-24 (2024) | Strong, direct physiological evidence in *Natranaerobius thermophilus*; taxon-specific but mechanistically generalizable to broad salinity tolerance | ENVO:hypersaline environment (label), GO:0006970 response to osmotic stress, CHEBI:17750 glycine betaine, CHEBI:29985 L-glutamate, CHEBI:26271 L-proline |
| glycine betaine ABC transporters (Opu/ProU) → enables → adaptation to high salinity | “employs the glycine betaine ABC transporters (Opu and ProU families) ... to adapt to high salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/aem.00145-24 (2024) | Strong for this taxon; suitable as transporter node supporting trait | GO:0015419 ATPase-coupled organic osmolyte transmembrane transporter activity (candidate), CHEBI:17750 glycine betaine |
| Na+/solute symporters (SSS family) → contributes to → high-salinity adaptation | “Na+/solute symporters (SSS family) ... to adapt to high salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/aem.00145-24 (2024) | Moderate; family-level mechanism, substrate specificity may vary | GO:0015294 solute:sodium symporter activity |
| glutamate biosynthetic pathway → increases cellular → glutamate osmolyte pool | “glutamate and proline synthesis pathways” and “intracellular content of ... glutamate ... increases with rising salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/aem.00145-24 (2024) | Moderate; pathway-level inference supported by measured metabolite increases | GO:0006537 glutamate biosynthetic process, CHEBI:29985 L-glutamate |
| proline biosynthetic pathway → increases cellular → proline osmolyte pool | “glutamate and proline synthesis pathways” and “intracellular content of ... proline, increases with rising salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/aem.00145-24 (2024) | Moderate; direct metabolite trend plus pathway statement | GO:0006561 proline biosynthetic process, CHEBI:26271 L-proline |
| TrkH potassium uptake system → increases intracellular → K+ | “upregulation of a potassium uptake system (TrkH, trkH Nther_0255)” and direct K+ measurements (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/aem.00145-24 (2024) | Strong in *N. thermophilus*; direct transporter-expression plus ion measurements | GO:0015079 potassium ion transmembrane transporter activity, CHEBI:29103 potassium(1+) |
| intracellular K+ accumulation → supports → salt-in osmoadaptation | “dual strategy of accumulating compatible solutes and K+” (xing2024thepolyextremophilenatranaerobius pages 6-7); “accumulate up to 4 M K+ in their cytoplasm” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | 10.1128/aem.00145-24 (2024); 10.1038/s41559-024-02505-6 (2024) | Strong concept-level edge across taxa; exact concentrations differ by lineage | GO:0006970 response to osmotic stress, CHEBI:29103 potassium(1+) |
| salt-in strategy → associated with → acidic proteome / low pI proteome | “proteome acidification is a hallmark of extreme halophily” and “median protein isoelectric points ≤4.4” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | 10.1038/s41559-024-02505-6 (2024) | Strong for extreme halophiles; trait-level signature rather than a manipulable gene edge | GO:0043621 protein self-association? (avoid curation), label-only: acidic proteome, label-only: low proteome pI |
| increasing salinity → decreases → median isoelectric points of upregulated proteins | “median isoelectric points of the upregulated proteins decrease with increasing salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | 10.1128/aem.00145-24 (2024) | Strong within assay; useful phenotype signature node, but not a molecular mechanism alone | label-only: lower proteome pI, GO:0006970 response to osmotic stress |
| salinity transition across biomes → drives → proteome reorganization / pI shifts | “Transitions were accompanied by systematic changes in amino acid composition and isoelectric point distributions” (jurdzinski2023largescalephylogenomicsof pages 1-1) | 10.1126/sciadv.adg2059 (2023) | Strong comparative-genomics evidence; broad evolutionary edge rather than short-term physiology | label-only: proteome reorganization, label-only: isoelectric point distribution shift |
| nhaC Na+/H+ antiporter upregulation → facilitates → Na+ homeostasis at high salinity | “strong upregulation of a Na+/H+ antiporter (nhaC Nther_2723) at higher salinities” (xing2024thepolyextremophilenatranaerobius pages 6-7) | 10.1128/aem.00145-24 (2024) | Strong for this species; causal role inferred from known antiporter function plus induction | GO:0015385 sodium:proton antiporter activity |
| hybrid salt-in/salt-out osmoregulation → supports survival in → fluctuating salinity environments | MAGs “contain genes for both the energetically cheaper ‘salt-in’ and more expensive ‘salt-out’ strategies” (ionescu2024extremefluctuationsin pages 1-2) | 10.3389/frmbi.2023.1329925 (2024) | Moderate; genome-content inference from enrichment culture/MAGs, not direct knockout evidence | GO:0006970 response to osmotic stress, ENVO:hypersaline environment (label) |
| proB/proA/proC-mediated proline biosynthesis → restores growth at → 8% NaCl | engineered strain “thrived in the medium containing 8% NaCl by accumulating Pro ... 353.1 ± 40.5 µmol/g cell fresh weight” (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24 (2024) | Strong but engineered and assay-specific; useful as proof that proline osmolyte accumulation can causally support >8% NaCl growth | KEGG:proB/proA/proC (label candidates), GO:0006561 proline biosynthetic process, CHEBI:26271 L-proline |
| putA deletion → increases → cellular proline accumulation | “the putA gene ... was deleted ... HN6 thrived ... by accumulating Pro” (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24 (2024) | Moderate-strong, but engineered background and coupled to operon replacement; curate as uncertain if generalized | GO:0004657 proline dehydrogenase activity, GO:0015293 symporter? (not needed), CHEBI:26271 L-proline |
| GABA accumulation → improves → salt-stress tolerance | “GOP-Gad strain exhibits higher salt tolerance ... by accumulating high concentration of GABA as an osmolyte ... 176.94 µmol/g cell dry weight in ... 7% NaCl” (zou2024metabolicengineeringof pages 1-2) | 10.1128/aem.01905-23 (2024) | Strong but engineered and taxon-specific; below >8% threshold, so supportive for mechanism not direct trait-defining evidence | CHEBI:16865 4-aminobutanoate, GO:0006538 glutamate catabolic process |
| hypersaline environment (>100–150 g/L salts) → selects for → halophilic osmoadaptation strategies | “hypersaline environments ... containing >100–150 g/L salts” and halophiles grow at “>100–150 g/L” (oren2024novelinsightsinto pages 1-2) | 10.1038/s44185-024-00050-w (2024) | Strong environmental-scope edge; good for trait boundary definition, not a gene mechanism | ENVO:hypersaline environment (label), METPO:1000482 |
| high MgCl2 / chaotropic brines above ~1.26 M → inhibits → microbial growth/activity | “microbial growth was inhibited above >1.26 M MgCl2” (oren2024novelinsightsinto pages 4-5) | 10.1038/s44185-024-00050-w (2024) | Strong boundary-condition edge; relevant negative environmental factor, but MgCl2 is not NaCl breadth itself | CHEBI:18420 magnesium chloride, label-only: growth inhibition |
| 8–12% NaCl or 10% NaCl-tolerant halophiles → enable → bioremediation under hypersaline conditions | “up to 97% fluorene at 8–12% NaCl” and “94% Pb reduction ... at 10% NaCl” (rezaei2025innovativeapproachesin pages 7-8) | 10.1186/s12934-025-02817-7 (2025) | Application edge; demonstrates real-world implementation of the trait, not core mechanism | ENVO:hypersaline environment (label), CHEBI:5118 fluorene, CHEBI:25016 lead(2+) |
| broad NaCl tolerance in *Halomonas elongata* (0.3–21% NaCl) → is supported by → compatible-solute strategy | “grows across salinities from 0.3% to 21% NaCl” and native ectoine/proline-compatible-solute context (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/aem.01195-24 (2024) | Strong organism-level evidence for extreme breadth; mechanistic support is compatible-solute based, especially ectoine/proline | NCBITaxon:*Halomonas elongata* (label), GO:0006970 response to osmotic stress, CHEBI:17634 ectoine, CHEBI:26271 L-proline |


*Table: This table compiles curation-ready candidate causal edges for METPO:1000482 NaCl delta high, linking salinity breadth to compatible solutes, ion transport, salt-in signatures, and boundary/application evidence. It is useful for selecting which mechanistic triples are strong enough for TraitMech curation and which should be marked uncertain or context-specific.*

---

## Warnings / curation caveats
1) **Do not overgeneralize engineered strain edges** (e.g., proline/GABA engineering in *Halomonas elongata*) to all taxa without marking as **engineered/assay-specific**; they are best curated as mechanistic support that “osmolyte identity and accumulation can causally expand NaCl growth limits.” (khanh2024metabolicpathwayengineering pages 1-2, zou2024metabolicengineeringof pages 1-2)
2) **Salt-in signatures (acidic proteomes, high K+)** are strongest for extreme halophilic archaea and a few bacterial analogs; their presence does not automatically imply *broad* NaCl breadth without explicit growth-range data. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
3) **Environmental hypersalinity definitions** (>100–150 g/L salts) are helpful for context but are not equivalent to “NaCl breadth” in lab assays; curate as environment nodes, not trait-defining evidence by themselves. (oren2024novelinsightsinto pages 1-2)
4) **Chaotropic ions (MgCl2, CaCl2, etc.)** impose additional constraints; wide NaCl tolerance does not imply tolerance to high MgCl2 brines (growth inhibited above ~1.26 M MgCl2 in some systems). (oren2024novelinsightsinto pages 4-5)

---

## DOI-first bibliography (with publication dates and URLs)
- Jurdzinski KT, Mehrshad M, et al. **Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity.** *Science Advances* (May 2023). DOI: **10.1126/sciadv.adg2059**. https://doi.org/10.1126/sciadv.adg2059 (jurdzinski2023largescalephylogenomicsof pages 1-1)
- Ionescu D, Zoccarato L, et al. **Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy.** *Frontiers in Microbiomes* (Jan 2024). DOI: **10.3389/frmbi.2023.1329925**. https://doi.org/10.3389/frmbi.2023.1329925 (ionescu2024extremefluctuationsin pages 1-2)
- Xing Q, Zhang S, et al. **The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.** *Applied and Environmental Microbiology* (May 2024). DOI: **10.1128/aem.00145-24**. https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius media f9a64a84, xing2024thepolyextremophilenatranaerobius media 38da44bd)
- Oren A. **Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems.** *npj Biodiversity* (Aug 2024). DOI: **10.1038/s44185-024-00050-w**. https://doi.org/10.1038/s44185-024-00050-w (oren2024novelinsightsinto pages 1-2, oren2024novelinsightsinto pages 4-5)
- Gutiérrez‑Preciado A, Dede B, et al. **Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines.** *Nature Ecology & Evolution* (Aug 2024). DOI: **10.1038/s41559-024-02505-6**. https://doi.org/10.1038/s41559-024-02505-6 (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
- Zou Z, Kaothien‑Nakayama P, et al. **Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient Halomonas elongata.** *Applied and Environmental Microbiology* (Jan 2024). DOI: **10.1128/aem.01905-23**. https://doi.org/10.1128/aem.01905-23 (zou2024metabolicengineeringof pages 1-2)
- Khanh HC, Kaothien‑Nakayama P, et al. **Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient Halomonas elongata.** *Applied and Environmental Microbiology* (Sep 2024). DOI: **10.1128/aem.01195-24**. https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 1-2)
- Rezaei Z, Amoozegar MA, Moghimi H. **Innovative approaches in bioremediation: the role of halophilic microorganisms in mitigating hydrocarbons, toxic metals, and microplastics in hypersaline environments.** *Microbial Cell Factories* (Aug 2025). DOI: **10.1186/s12934-025-02817-7**. https://doi.org/10.1186/s12934-025-02817-7 (rezaei2025innovativeapproachesin pages 7-8)
- Liu J, Zhao X, et al. **Plant growth-promoting rhizobacteria Halomonas alkaliantarcticae M23 promotes the salt tolerance of maize...** *BMC Plant Biology* (May 2025). DOI: **10.1186/s12870-025-06765-7**. https://doi.org/10.1186/s12870-025-06765-7 (liu2025plantgrowthpromotingrhizobacteria pages 1-2)
- Li Y, Gu M-y, et al. **Whole-genome analysis of Halomonas sp. H5...** *Microorganisms* (Jul 2025). DOI: **10.3390/microorganisms13081781**. https://doi.org/10.3390/microorganisms13081781 (li2025wholegenomeanalysisof pages 1-2)


References

1. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

2. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4): Ana Gutiérrez-Preciado, Bledina Dede, Brittany A. Baker, Laura Eme, David Moreira, and Purificación López-García. Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines. Aug 2024. URL: https://doi.org/10.1038/s41559-024-02505-6, doi:10.1038/s41559-024-02505-6. This article has 23 citations and is from a highest quality peer-reviewed journal.

3. (oren2024novelinsightsinto pages 1-2): Aharon Oren. Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems. npj Biodiversity, Aug 2024. URL: https://doi.org/10.1038/s44185-024-00050-w, doi:10.1038/s44185-024-00050-w. This article has 65 citations and is from a peer-reviewed journal.

4. (oren2024novelinsightsinto pages 4-5): Aharon Oren. Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems. npj Biodiversity, Aug 2024. URL: https://doi.org/10.1038/s44185-024-00050-w, doi:10.1038/s44185-024-00050-w. This article has 65 citations and is from a peer-reviewed journal.

5. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

6. (ionescu2024extremefluctuationsin pages 1-2): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 11 citations.

7. (xing2024thepolyextremophilenatranaerobius pages 6-7): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

8. (xing2024thepolyextremophilenatranaerobius media f9a64a84): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

9. (xing2024thepolyextremophilenatranaerobius media 38da44bd): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

10. (jurdzinski2023largescalephylogenomicsof pages 1-1): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 60 citations and is from a highest quality peer-reviewed journal.

11. (rezaei2025innovativeapproachesin pages 7-8): Zeinab Rezaei, M. A. Amoozegar, and Hamid Moghimi. Innovative approaches in bioremediation: the role of halophilic microorganisms in mitigating hydrocarbons, toxic metals, and microplastics in hypersaline environments. Microbial Cell Factories, Aug 2025. URL: https://doi.org/10.1186/s12934-025-02817-7, doi:10.1186/s12934-025-02817-7. This article has 12 citations and is from a peer-reviewed journal.

12. (zou2024metabolicengineeringof pages 1-2): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 17 citations and is from a peer-reviewed journal.

13. (liu2025plantgrowthpromotingrhizobacteria pages 1-2): Jiang Liu, Xinghua Zhao, Yuqi Niu, Yongkang Ren, Ming Wang, Bin Han, Changbiao Wang, and Haizhen Ma. Plant growth-promoting rhizobacteria halomonas alkaliantarcticae m23 promotes the salt tolerance of maize by increasing the k+/na+ ratio, antioxidant levels, and aba levels and changing the rhizosphere bacterial community. BMC Plant Biology, May 2025. URL: https://doi.org/10.1186/s12870-025-06765-7, doi:10.1186/s12870-025-06765-7. This article has 26 citations and is from a peer-reviewed journal.

14. (li2025wholegenomeanalysisof pages 1-2): Yan Li, Mei-ying Gu, Wanli Xu, Jing Zhu, Min Chu, Qiyong Tang, Yuanyang Yi, Lijuan Zhang, Pan Li, Yunshu Zhang, Osman Ghenijan, Zhidong Zhang, and Ning Li. Whole-genome analysis of halomonas sp. h5 revealed multiple functional genes relevant to tomato growth promotion, plant salt tolerance, and rhizosphere soil microecology regulation. Microorganisms, 13:1781, Jul 2025. URL: https://doi.org/10.3390/microorganisms13081781, doi:10.3390/microorganisms13081781. This article has 5 citations.

15. (xing2024thepolyextremophilenatranaerobius pages 19-21): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

16. (xing2024thepolyextremophilenatranaerobius pages 14-17): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

17. (strakova2025strategiesofenvironmental pages 7-9): Dáša Straková, Cristina Sánchez-Porro, Rafael R. de la Haba, and Antonio Ventosa. Strategies of environmental adaptation in the haloarchaeal genera haloarcula and natrinema. Microorganisms, 13:761, Mar 2025. URL: https://doi.org/10.3390/microorganisms13040761, doi:10.3390/microorganisms13040761. This article has 9 citations.

18. (xing2024thepolyextremophilenatranaerobius pages 7-10): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.