---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:04:41.777481'
end_time: '2026-06-18T00:29:36.688128'
duration_seconds: 1494.91
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta mid1
  trait_identifier: METPO:1000475
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH delta phenotype with a growth-supporting pH breadth of approximately\
    \ 2\u20133 pH units, characteristic of organisms with moderate pH-tolerance breadth."
  parent_traits: METPO:1000232
  synonyms: pHd_2_3
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports moderate pH-homeostasis flexibility as common among non-extreme microorganisms.)'
  causal_graph_summary: 'ph_delta_mid1_moderate_breadth: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta mid1
- **METPO identifier:** METPO:1000475
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 2–3 pH units, characteristic of organisms with moderate pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_2_3
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports moderate pH-homeostasis flexibility as common among non-extreme microorganisms.)
- **Existing causal graph summary:** ph_delta_mid1_moderate_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid1.yaml`.

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
- **Trait label:** pH delta mid1
- **METPO identifier:** METPO:1000475
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 2–3 pH units, characteristic of organisms with moderate pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_2_3
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports moderate pH-homeostasis flexibility as common among non-extreme microorganisms.)
- **Existing causal graph summary:** ph_delta_mid1_moderate_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid1.yaml`.

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


## Curation-focused research report: Microbial trait **pH delta mid1** (METPO:1000475)

### 0) Scope summary
**pH delta mid1** is best interpreted as a **growth-supporting pH range (ΔpH) of ~2–3 pH units**—i.e., a moderate breadth of external pH values over which an organism can grow (not merely remain viable). This trait should be curated as a **growth phenotype** (acid/alkali tolerance breadth), and not conflated with **acid resistance**, which is survival under normally lethal pH without growth. (atasoy2024methodsforstudying pages 2-3, atasoy2024methodsforstudying pages 3-4, perezrodriguez2024methodsforstudying pages 3-5)

Boundary cases and assay confounders are central for this trait: (i) growth vs survival endpoints, (ii) acid identity (weak vs strong acids can differ at the same pH), (iii) buffering and active pH control because microbes can change medium pH during growth, (iv) induction by prior sublethal exposure (acid shock/ATR), (v) growth phase and biofilm vs planktonic state, and (vi) VBNC/persister subpopulations that may survive but appear “non-growing” in standard culturability assays. (atasoy2024methodsforstudying pages 2-3, atasoy2024methodsforstudying pages 3-4, atasoy2024methodsforstudying pages 4-5)

### 1) Key concepts and definitions (current understanding)

#### 1.1 Acid resistance vs acid tolerance (key definitional anchor)
Recent methodology syntheses explicitly distinguish:
- **Acid resistance:** “ability to survive a normally lethal pH” (survival phenotype). (atasoy2024methodsforstudying pages 3-4, perezrodriguez2024methodsforstudying pages 3-5)
- **Acid tolerance:** “ability to grow at a nonlethal but acidic pH” (growth phenotype). (atasoy2024methodsforstudying pages 2-3, atasoy2024methodsforstudying pages 3-4)

This distinction matters because **pH delta mid1** is defined as a **growth-supporting breadth** and should be assessed by growth profiling across pH gradients rather than lethal-survival assays alone. (atasoy2024methodsforstudying pages 3-4)

#### 1.2 pH preference/optimum vs pH breadth
Genome/biogeography work defines **pH preference** as the **environmental pH where a taxon reaches maximal relative abundance** (a realized niche metric influenced by abiotic/biotic constraints). (ramoneda2023buildingagenomebased pages 1-2)

For TraitMech curation, pH delta mid1 corresponds more directly to **pH breadth (range supporting growth)** than to pH preference alone; preference can be used as the central tendency around which breadth is expressed, but preference is not sufficient to specify ΔpH. (ramoneda2023buildingagenomebased pages 1-2, ramoneda2024leveraginggenomicinformation pages 2-4)

### 2) Recent developments and latest research (prioritizing 2023–2024)

#### 2.1 Genome-based inference of bacterial pH preferences (Science Advances 2023)
Ramoneda et al. compiled **five pH-gradient datasets (1,470 samples total; 795 soil, 675 freshwater; pH 3–10; 250,275 ASVs)** and inferred pH preferences for subsets of taxa. (Publication date: Apr 2023; URL: https://doi.org/10.1126/sciadv.adf8998). (ramoneda2023buildingagenomebased pages 1-2)

Key quantitative/statistical outcomes:
- Only **6–24%** of ASVs had GTDB representatives; they obtained **669 ASV-genome matches representing 580 genomes** (many MAGs/SAGs). (ramoneda2023buildingagenomebased pages 2-3)
- They identified **332 gene types** associated with pH preference in ≥2 datasets and **56 gene types** in ≥3 datasets; many relate to canonical pH-adaptation mechanisms (decarboxylases, urease/ammonia, ion transport, membrane/protein stability). (ramoneda2023buildingagenomebased pages 3-5)
- A gradient-boosted tree using the 56 genes achieved **MAE ~0.63** (training MAE ~0.43) with cross-dataset R² ~0.80; performance dropped in fully independent validation (UK soil R² ~0.21). (ramoneda2023buildingagenomebased pages 6-7)

This work is directly useful for pH delta mid1 curation because it supplies **candidate mechanistic nodes (gene families)** that plausibly contribute to tolerance breadth even when direct growth-range phenotyping is missing. (ramoneda2023buildingagenomebased pages 3-5)

#### 2.2 Methods and pitfalls in pH stress phenotyping (FEMS Microbiology Reviews 2024)
A 2024 methods review emphasizes that **measurement of pH-related traits is strongly assay-dependent**, including media composition, buffer selection, growth format (microtiter vs flasks), growth phase, and biofilm state; it also notes that some mechanisms are condition-dependent (e.g., GAD/AR2 Na⁺/K⁺ dependence and medium-specific induction). (Publication date: May 2024; URL: https://doi.org/10.1093/femsre/fuae015). (atasoy2024methodsforstudying pages 4-5)

#### 2.3 Mechanistic expansions relevant to moderate pH breadth (2024 exemplars)
- **Engineered mild-acid tolerance (pH 6.0)** in *E. coli* shows that overexpressing a synthetic module (gadE, hdeB, sodB, katE) can increase growth (OD600) at mildly acidic pH; transcriptomics associates oxidative phosphorylation, TCA cycle, ABC transporters and amino-acid metabolism with the phenotype. (Publication date: Jul 2024; URL: https://doi.org/10.3390/microorganisms12081565). (qin2024characterizationofmild pages 1-2, qin2024characterizationofmild pages 13-14)
- **Community/biofilm pH stress adaptability** can be modulated by **putrescine**, with **pH-dependent (protonation-dependent) switch-like effects**: benefits under acid conditions via intracellular H⁺ consumption and ATPase induction, but harm under alkaline conditions by exacerbating alkali stress. (Publication date: Jul 2024; URL: https://doi.org/10.1128/aem.00569-24). (jiang2024exogenousputrescineplays pages 1-2)

### 3) Current applications and real-world implementations

1. **Industrial strain engineering for acid-stressed fermentation:** engineered *E. coli* with targeted acid tolerance modules improves growth robustness under mildly acidic conditions, supporting industrial use cases where organic acid accumulation lowers pH. (qin2024characterizationofmild pages 1-2, qin2024characterizationofmild pages 13-14)

2. **Biofilm/activated sludge process control:** exogenous putrescine can regulate biofilm formation differently under acidic vs alkaline conditions, suggesting a lever for engineering biofilm stability in wastewater/bioprocess environments across pH perturbations. (jiang2024exogenousputrescineplays pages 1-2)

3. **Cultivation strategy and microbial inoculant selection:** genome-based prediction of environmental preferences (including pH) is highlighted as a route to guide cultivation and inoculant choice beyond the small, biased set of lab-characterized taxa. (ramoneda2024leveraginggenomicinformation pages 2-4)

### 4) Expert opinions and analysis (authoritative synthesis)

- The 2024 FEMS review argues that acid stress studies benefit from **multiple complementary assays** (growth curves, single-cell pH reporters, genetics, omics, evolution) because single assays can misclassify phenotypes, especially when survival, injury, and recovery are confounded. (atasoy2024methodsforstudying pages 3-4, atasoy2024methodsforstudying pages 4-5)
- The 2023 Science Advances study emphasizes that **taxonomy/phylogeny alone poorly predicts pH preference**, supporting a gene/trait-based causal-graph approach instead of purely taxonomic inference. (ramoneda2023buildingagenomebased pages 2-3, ramoneda2023buildingagenomebased pages 1-2)

### 5) Candidate nodes (entities) grouped by type
The following node inventory is evidence-supported and curation-ready as candidate graph entities:

| Node label | Type | Brief role in pH breadth | Evidence source(s) | Suggested ontology CURIE(s) |
|---|---|---|---|---|
| pH delta mid1 (growth-supporting pH breadth ~2–3 units) | Phenotype/assay node | Target phenotype: moderate growth-supporting pH range, distinct from survival-only acid resistance; should be operationalized by growth across pH, not just viability | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 2-3, atasoy2024methodsforstudying pages 3-4, atasoy2024methodsforstudying pages 4-5); Ramoneda et al. 2024, doi:10.1093/ismejo/wrae195, https://doi.org/10.1093/ismejo/wrae195 (ramoneda2024leveraginggenomicinformation pages 2-4) | METPO:1000475 |
| acid tolerance (growth at nonlethal acidic pH) | Phenotype/assay node | Growth-based low-pH phenotype; appropriate comparator concept for breadth on acidic side | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 2-3, atasoy2024methodsforstudying pages 3-4) | label-only |
| acid resistance (survival at lethal pH) | Phenotype/assay node | Survival-only phenotype; important boundary case that should not be conflated with growth-supporting pH breadth | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 2-3, atasoy2024methodsforstudying pages 3-4) | label-only |
| pH preference / pH optimum | Phenotype/assay node | Central pH value of best growth or highest realized abundance; distinct from breadth | Ramoneda et al. 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 8-9); Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 18-19) | label-only |
| growth assay across pH gradient | Phenotype/assay node | Preferred assay class for measuring breadth; distinguishes supportive growth range from lethal-survival endpoints | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 3-4, atasoy2024methodsforstudying pages 4-5); Ramoneda et al. 2024, doi:10.1093/ismejo/wrae195, https://doi.org/10.1093/ismejo/wrae195 (ramoneda2024leveraginggenomicinformation pages 2-4) | label-only |
| survival/CFU assay | Phenotype/assay node | Measures lethality/survival, not growth range; useful as warning node | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 3-4); Atasoy/Pérez-Rodríguez methods context (perezrodriguez2024methodsforstudying pages 3-5, perezrodriguez2024methodsforstudying pages 2-3) | label-only |
| low external pH / acid stress | Environmental/experimental factor | Primary stressor reducing cytoplasmic pH and selecting for proton-consuming/export systems | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4); Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 2-3) | label-only |
| high external pH / alkaline stress | Environmental/experimental factor | Opposite-side stressor; relevant for breadth limits and alkali-side homeostasis via antiporters | Jiang et al. 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2); Ramoneda et al. 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) | label-only |
| acid identity / weak vs strong acids | Environmental/experimental factor | Same nominal pH can produce different phenotypes depending on acid chemistry, pKa, and anion | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 2-3, perezrodriguez2024methodsforstudying pages 2-3, perezrodriguez2024methodsforstudyinga pages 2-3) | label-only |
| buffering / pH control | Environmental/experimental factor | Essential assay factor because microbes alter medium pH during growth; changes apparent breadth | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 4-5) | label-only |
| medium composition / ion availability | Environmental/experimental factor | Strongly modulates pH phenotypes; e.g., GAD/AR2 dependence on Na+/K+ and medium context | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 4-5) | label-only |
| prior sublethal acid exposure / acid shock history | Environmental/experimental factor | Inducible tolerance history can widen measured range without changing constitutive capability | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 2-3, perezrodriguez2024methodsforstudyinga pages 2-3) | label-only |
| growth phase / stationary phase | Environmental/experimental factor | Stationary-phase cells often show greater low-pH resistance than exponential cells | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 3-4, perezrodriguez2024methodsforstudyinga pages 3-5) | label-only |
| biofilm growth state | Environmental/experimental factor | Biofilms can increase pH stress protection and alter realized breadth relative to planktonic cells | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 3-4, atasoy2024methodsforstudying pages 4-5); Jiang et al. 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2) | GO:0042710 |
| glutamate-dependent acid resistance (Gad/AR2) | Pathway/module | Major proton-consuming system supporting low-pH homeostasis via glutamate decarboxylation and GABA exchange | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4); Figure summary (li2024responseofescherichia media e76b3b93) | label-only |
| F0F1-ATPase-associated acid response (AR1-linked) | Pathway/module | ATP hydrolysis-driven proton management under acid stress | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | GO:0045263 |
| glutamine-to-glutamate/ammonia acid resistance module | Pathway/module | Couples glutaminase activity with ammonia release and glutamate supply to support proton neutralization | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | label-only |
| lysine-dependent acid resistance system | Pathway/module | Acid-resistance pathway upregulated in mild acid-tolerant strain; relevant to moderate acidic breadth | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2, qin2024characterizationofmild pages 13-14); Li et al. 2024 (li2024responseofescherichia pages 10-12) | label-only |
| arginine-dependent acid resistance system | Pathway/module | Amino-acid decarboxylase/antiporter acid resistance mechanism contributing to proton consumption | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 10-12, qin2024characterizationofmild pages 13-14) | label-only |
| urease / urea-to-ammonia pathway | Pathway/module | Generates ammonia to counter acidity; associated with pH preference across taxa | Ramoneda et al. 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) | EC:3.5.1.5 |
| oxidative phosphorylation | Pathway/module | Supports proton export and PMF maintenance; positively associated with mild-acid growth | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2, qin2024characterizationofmild pages 13-14); Jiang et al. 2024 (jiang2024exogenousputrescineplays pages 1-2) | GO:0006119 |
| TCA cycle | Pathway/module | Metabolic support module upregulated with mild acid tolerance | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2, qin2024characterizationofmild pages 13-14) | GO:0006099 |
| membrane lipid remodeling / increased fatty-acid saturation | Pathway/module | Reduces proton diffusion and stabilizes membrane under pH stress | Jiang et al. 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2) | GO:0006643 |
| putrescine-responsive GABA/glutamate acid-stress module | Pathway/module | Under acidic pH, protonated putrescine enhances glutamate-based acid resistance and GABA metabolism | Jiang et al. 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2) | label-only |
| gadA | Gene/protein/complex | Glutamate decarboxylase subunit contributing to proton consumption at low pH | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | label-only |
| gadB | Gene/protein/complex | Glutamate decarboxylase subunit contributing to proton consumption at low pH | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | label-only |
| gadC | Gene/protein/complex | GABA/glutamate antiporter enabling operation of Gad acid-resistance cycle | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | label-only |
| GadE (YhiE) | Gene/protein/complex | Positive regulator of glutamate decarboxylase-dependent acid resistance; engineered contributor to mild-acid growth | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 10-12); Qin et al. 2024 (qin2024characterizationofmild pages 1-2) | label-only |
| YbaS | Gene/protein/complex | Glutaminase releasing ammonia and glutamate during acid stress | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | label-only |
| HdeB | Gene/protein/complex | Periplasmic chaperone in synthetic mild-acid tolerance module | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2) | label-only |
| SodB | Gene/protein/complex | ROS scavenger supporting acid-stress robustness in engineered strain | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2) | label-only |
| KatE | Gene/protein/complex | ROS scavenger supporting acid-stress robustness in engineered strain | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2) | label-only |
| SdiA | Gene/protein/complex | Regulator improving acid tolerance via GadW/GadY | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 36-37) | label-only |
| GadW | Gene/protein/complex | Regulatory target in SdiA-mediated acid tolerance control | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 36-37) | label-only |
| GadY | Gene/protein/complex | Regulatory target in SdiA-mediated acid tolerance control | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 36-37) | label-only |
| cad operon / CadA-CadC module | Gene/protein/complex | Neutralizes low extracellular pH; representative acid-homeostasis module | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 36-37); Li et al. 2024 (li2024responseofescherichia pages 10-12) | label-only |
| F0F1-ATPase complex | Gene/protein/complex | Proton-translocating ATPase associated with acid homeostasis | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | GO:0045263 |
| nuo / cyo / ndh / sdh respiratory complexes | Gene/protein/complex | Electron transport components upregulated under mild acid stress and expected to support proton export | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 13-14) | label-only |
| Na+/H+ antiporters (PhaGF, MnhG, MrpF, YufB) | Transporter | Associated with higher-pH preference and alkali-side homeostasis | Ramoneda et al. 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) | GO:0015385 |
| K+ transporters (KdpACD) | Transporter | Associated with low-pH-preferring taxa, likely contributing to ion/pH homeostasis | Ramoneda et al. 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) | GO:0015079 |
| amino-acid transporter(s) | Transporter | Support proton-consuming amino-acid stress pathways | Jiang et al. 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2); Ramoneda et al. 2023 (ramoneda2023buildingagenomebased pages 3-5) | label-only |
| GABA/glutamate antiporter (GadC function) | Transporter | Exchanges extracellular glutamate for intracellular GABA to sustain Gad cycle | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | GO:0015297 |
| arginine/agmatine antiporter | Transporter | Supports arginine-dependent extreme acid resistance | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 10-12) | label-only |
| urea transporter / ureide permease | Transporter | Imports substrate for ammonia-generating urease pathway | Ramoneda et al. 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) | label-only |
| ABC transporters | Transporter | Strongly associated with mild acid response; can import protective solutes/export toxins | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2, qin2024characterizationofmild pages 13-14) | GO:0042626 |
| Dpp peptide transporter | Transporter | Candidate protective transporter associated with improved acid survival | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 13-14) | GO:0015833 |
| glycine betaine transporter | Transporter | Candidate osmoprotective transporter linked to acid survival improvement | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 13-14) | label-only |
| glutamate | Metabolite/chemical | Substrate for Gad proton-consuming decarboxylation; central acidic-side homeostasis metabolite | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4); Jiang et al. 2024 (jiang2024exogenousputrescineplays pages 1-2) | CHEBI:29985 |
| GABA (4-aminobutyrate) | Metabolite/chemical | Product/exported metabolite of glutamate-dependent acid resistance | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | CHEBI:16865 |
| glutamine | Metabolite/chemical | Substrate for YbaS; feeds ammonia release and glutamate generation | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | CHEBI:28300 |
| ammonia | Metabolite/chemical | Basic product that neutralizes intracellular acidity | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4); Ramoneda et al. 2023 (ramoneda2023buildingagenomebased pages 3-5) | CHEBI:16134 |
| proton (H+) | Metabolite/chemical | Central stress currency consumed/exported/neutralized by pH homeostasis systems | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4); Qin et al. 2024 (qin2024characterizationofmild pages 13-14) | CHEBI:15378 |
| ATP | Metabolite/chemical | Energy source for ATPase-driven proton management and transport | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | CHEBI:15422 |
| putrescine | Metabolite/chemical | Protonation-state-dependent modulator of acid vs alkaline stress adaptability in biofilms | Jiang et al. 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2) | CHEBI:17148 |
| urea | Metabolite/chemical | Precursor for ammonia-generating urease pathway | Ramoneda et al. 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) | CHEBI:16199 |
| glycine betaine | Metabolite/chemical | Protective solute candidate linked to acid survival | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 13-14) | CHEBI:17750 |
| saturated fatty acids | Metabolite/chemical | Increased saturation can reduce proton permeability under pH stress | Jiang et al. 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2) | CHEBI:26607 |
| unsaturated fatty acids | Metabolite/chemical | Relative decrease accompanies saturation-based membrane protection under acid stress | Jiang et al. 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2) | CHEBI:27208 |
| cytoplasmic pH homeostasis | Cellular structure/process | Immediate physiological objective linking mechanisms to tolerance breadth | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4); Ramoneda et al. 2024, doi:10.1093/ismejo/wrae195, https://doi.org/10.1093/ismejo/wrae195 (ramoneda2024leveraginggenomicinformation pages 2-4) | label-only |
| proton motive force (PMF) | Cellular structure/process | Energetic state supporting proton export and pH maintenance during mild acid stress | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 13-14); Atasoy/Pérez-Rodríguez methods context (perezrodriguez2024methodsforstudyinga pages 40-41) | GO:0015986 |
| proton transmembrane transport | Cellular structure/process | Core process used by ATPase and respiratory chain to manage intracellular pH | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4); Jiang et al. 2024 (jiang2024exogenousputrescineplays pages 1-2) | GO:1902600 |
| membrane proton permeability | Cellular structure/process | Determinant of how strongly external pH perturbs the cytoplasm | Jiang et al. 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2) | label-only |
| biofilm extracellular matrix / EPS | Cellular structure/process | Structural protection that can broaden realized pH tolerance in communities | Jiang et al. 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2) | label-only |
| periplasm | Cellular structure/process | Relevant compartment for HdeB chaperone-mediated stress protection | Qin et al. 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2) | GO:0042597 |
| viable but non-culturable / persister subpopulation | Cellular structure/process | Boundary case that can distort apparent breadth when assay relies on culturability | Atasoy et al. 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 4-5) | label-only |


*Table: This table lists evidence-supported candidate nodes for a TraitMech-style causal graph of pH delta mid1, grouped by entity type. It is useful for selecting curation-ready phenotype, mechanism, transporter, metabolite, and assay-factor nodes while keeping assay confounders explicit.*

### 6) Evidence-backed candidate causal edges (triples)
The following are proposed curation candidates for `data/traits/environment/ph_delta_mid1.yaml`. Edges are written as subject–predicate–object with evidence snippets, notes, and grounding suggestions.

| Edge (Subject — predicate — Object) | Evidence snippet | Source (DOI, year, URL) | Notes for curation | Suggested ontology grounding |
|---|---|---|---|---|
| Glutamate decarboxylase system (GadA/GadB/GadC) — enables — survival/growth at low external pH | “GadA and GadB decarboxylate glutamate to GABA and CO2 while consuming H+; GadC antiporter exports GABA in exchange for extracellular glutamate… enabling survival at pH ~2–2.5.” (li2024responseofescherichia pages 2-4) | Li et al., 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 | Strong mechanistic support for acid tolerance/resistance; evidence is mainly from *E. coli* extreme acid systems, so use as a mechanistic contributor rather than universal determinant of moderate 2–3 pH breadth. | gadA/gadB/gadC (label); glutamate decarboxylase activity GO:0004351; glutamate CHEBI:29985; 4-aminobutanoate/GABA CHEBI:16865; antiporter activity GO:0015297 |
| GadE — positively regulates — glutamate decarboxylase-dependent acid resistance | “GadE (YhiE) is an activator of glutamate decarboxylase-dependent resistance.” (li2024responseofescherichia pages 10-12) | Li et al., 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 | Strong for regulatory edge in *E. coli*; taxon-specific regulator, so curate with organism-context or as exemplar. | gadE (label); regulation of transcription, DNA-templated GO:0006355 |
| YbaS glutaminase — produces — ammonia that neutralizes intracellular protons | “The glutaminase YbaS converts glutamine to glutamate and releases ammonia, which neutralizes intracellular protons.” (li2024responseofescherichia pages 2-4) | Li et al., 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 | Strong direct mechanism; best curated as acid-homeostasis contributor. | ybaS (label); glutaminase activity GO:0004359; glutamine CHEBI:28300; ammonia CHEBI:16134; glutamate CHEBI:29985 |
| Glutamine + glutamate decarboxylation pathway — consumes — two intracellular H+ | “Glutamine conversion and glutamate decarboxylation can act together to consume two H+, enhancing acid resistance.” (li2024responseofescherichia pages 2-4) | Li et al., 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 | Strong pathway-level edge; more abstract than gene-level and useful for graph condensation. | proton CHEBI:15378; cellular pH reduction/maintenance labels |
| F0F1-ATPase — hydrolyzes ATP to consume/export H+ — cytoplasmic pH homeostasis under acid stress | “F0F1-ATPase… under acid stress hydrolyzes ATP to consume intracellular H+ to maintain homeostasis.” (li2024responseofescherichia pages 2-4) | Li et al., 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774 | Strong but largely from enteric bacteria literature; suitable as broad pH-homeostasis node. | ATPase activity GO:0016887; proton transmembrane transport GO:1902600; F-type ATPase complex GO:0045263 |
| K+ transporters (KdpACD) — associated with — lower-pH preference taxa | “K+ transporters (KdpACD) are overrepresented in low-pH-preferring taxa.” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al., 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | Association from comparative genomics, not direct perturbation; curate as uncertain/inferred ecological association. | kdpA/kdpC/kdpD (label); potassium ion transmembrane transporter activity GO:0015079; potassium(1+) CHEBI:29103 |
| Na+/H+ antiporters (PhaGF, MnhG, MrpF, YufB) — associated with — higher-pH preference / alkali adaptation | “Na+/H+ antiporters (PhaGF, MnhG, MrpF, YufB)… are linked to higher pH preference.” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al., 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | Good evidence for alkaline-side breadth contributors, but inference is genomic/ecological rather than direct experiment; mark uncertain for causal universality. | sodium:proton antiporter activity GO:0015385; sodium(1+) CHEBI:29101; proton CHEBI:15378; mrpF/mnhG/phaG/yufB (labels) |
| Urease / urea transport pathway — produces — ammonia that counters acidity | “Urease (UreE_C) hydrolyzes urea into ammonia” and urea transporters are associated with pH preference. (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al., 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | Useful pathway-level node for taxa using ammonia generation; evidence is association-heavy here, so moderate confidence unless backed by organism-specific experiments. | urease activity GO:0009039; urea CHEBI:16199; ammonia CHEBI:16134; EC 3.5.1.5 |
| Exogenous putrescine — enhances — glutamate-based acid resistance system and GABA pathway under acidic pH | “Protonated exogenous putrescine… reduc[es] acid stress by consuming intracellular H+ via enhancement of the glutamate-based acid resistance system and the GABA metabolic pathway.” (jiang2024exogenousputrescineplays pages 1-2) | Jiang et al., 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Strong in biofilm-based activated sludge; environment/community specific and chemically contingent on protonation state. | putrescine CHEBI:17148; gamma-aminobutyrate metabolic process GO:0009448; glutamate CHEBI:29985 |
| Exogenous putrescine — stimulates expression of — ATPase / H+ transmembrane transport | “Putrescine… stimulates ATPase expression to improve H+ transmembrane transport and oxidative phosphorylation.” (jiang2024exogenousputrescineplays pages 1-2) | Jiang et al., 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Good mechanistic edge in biofilm consortia; not yet gene-resolved; curate as conditional on acidic conditions. | putrescine CHEBI:17148; ATPase activity GO:0016887; proton transmembrane transport GO:1902600 |
| Limited putrescine protonation at alkaline pH — exacerbates — alkali stress / inhibits metabolism | “Under alkaline pH putrescine protonation is limited; its intracellular H+ consumption exacerbates alkali stress and inhibits cellular metabolism.” (jiang2024exogenousputrescineplays pages 1-2) | Jiang et al., 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Valuable bidirectional/condition-dependent edge showing same effector can narrow breadth on alkaline side. | putrescine CHEBI:17148; alkaline pH (label) |
| Increased membrane saturated fatty acids — decreases — proton diffusion across membrane | “Conversion of unsaturated to saturated fatty acids [limits] proton diffusion.” (jiang2024exogenousputrescineplays pages 1-2) | Jiang et al., 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Moderate confidence from review-like summary within study; mechanism is broadly plausible but not directly tied to specific gene in retrieved evidence. | saturated fatty acid CHEBI:26607; unsaturated fatty acid CHEBI:27208; membrane lipid metabolic process GO:0006643 |
| Oxidative phosphorylation / ETC genes (nuo, cyo, ndh, sdh) — increase proton export / PMF maintenance — mild acid stress resistance | “Upregulation of oxidative phosphorylation and TCA cycle genes… is expected to increase proton export rate and generate/maintain a proton motive force that helps cells resist cytoplasmic pH decreases.” (qin2024characterizationofmild pages 13-14) | Qin et al., 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 | Strong for engineered *E. coli* under pH 6.0; useful for moderate-breadth trait because this is a mild-acid growth phenotype rather than extreme survival only. | oxidative phosphorylation GO:0006119; proton motive force GO:0015986; nuo/cyo/ndh/sdh (labels) |
| Synthetic acid-tolerance module (gadE, hdeB, sodB, katE) overexpression — increases — growth at pH 6.0 | “SC3124 reached higher OD600 at pH 6.0 versus parent strain… overexpression of these genes causes metabolic changes that confer mild acid stress resistance.” (qin2024characterizationofmild pages 1-2) | Qin et al., 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 | Strong growth-phenotype edge directly relevant to moderate pH breadth; engineered-strain evidence, so mark as synthetic/assay-specific. | gadE (label); hdeB (label); sodB (label); katE (label); response to acid chemical GO:0001101; superoxide dismutase activity GO:0004784; catalase activity GO:0004096 |
| ABC transporters — positively associated with — mild acid stress responses | “ABC transporters… were highly positively associated with mild acid stress responses.” (qin2024characterizationofmild pages 1-2) | Qin et al., 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 | Moderate confidence because association comes from transcriptomics/coexpression rather than direct knockout; likely broad stress-protection role. | ATPase-coupled transmembrane transporter activity GO:0042626; ABC transporter complex GO:0043190 |
| Dpp peptide transport / glycine betaine uptake — improves — acid survival | “Dpp peptide transport and glycine betaine uptake… betaine transport and Dpp overexpression… improve acid survival.” (qin2024characterizationofmild pages 13-14) | Qin et al., 2024, doi:10.3390/microorganisms12081565, https://doi.org/10.3390/microorganisms12081565 | Moderate, partly cross-species extrapolation; useful as candidate supportive transport edge. | glycine betaine CHEBI:17750; peptide transport GO:0015833; dpp transporter (label) |
| Biofilm / EPS matrix — protects against — pH stress | “Biofilms provide protective resistance to pH stress.” (jiang2024exogenousputrescineplays pages 1-2) | Jiang et al., 2024, doi:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Moderate confidence; EPS not gene-resolved in retrieved evidence, but important environmental/structural node for realized breadth. | biofilm GO:0042710; extracellular polymeric substance (label) |
| SdiA — regulates GadW/GadY — improved acid tolerance | “SdiA is reported to improve *E. coli* acid tolerance via regulation of GadW and GadY expression.” (atasoy2024methodsforstudying pages 36-37) | Atasoy et al., 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 | Good regulatory edge from recent review; still *E. coli*-centric. | sdiA/gadW/gadY (labels); regulation of transcription GO:0006355 |
| cad operon — neutralizes — low extracellular pH | “The *E. coli* cad operon is described as a system for neutralization of low extracellular pH.” (atasoy2024methodsforstudying pages 36-37) | Atasoy et al., 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 | Strong qualitative mechanism; relevant mainly to acid side of breadth. | cadA/cadB/cadC (labels); lysine decarboxylase activity GO:0009034 |
| Assay endpoint choice (growth vs survival) — changes interpretation of — pH tolerance breadth | “Acid resistance is the ability to survive a normally lethal pH,” whereas “acid tolerance is the ability to grow at a nonlethal but acidic pH.” (atasoy2024methodsforstudying pages 3-4, perezrodriguez2024methodsforstudying pages 3-5) | Atasoy et al., 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015; Pérez-Rodríguez et al., 2024, journal details incomplete | Essential curation warning: do not equate survival-only data with growth-supporting breadth; this is a trait-definition edge, not a biological mechanism. | assay endpoint (label); growth phenotype (label); survival phenotype (label) |
| Buffering / medium composition / ion availability — modulates measurement of — apparent pH tolerance breadth | “pH must be actively monitored or buffered; choice of buffer… affects results,” and GAD/AR2 is Na+/K+-dependent and not induced in LB. (atasoy2024methodsforstudying pages 4-5) | Atasoy et al., 2024, doi:10.1093/femsre/fuae015, https://doi.org/10.1093/femsre/fuae015 | Essential assay-dependence edge; curate as metadata/experimental factor rather than organismal mechanism. | buffering agent (label); sodium ion CHEBI:29101; potassium ion CHEBI:29103; culture medium (ENVO/label) |


*Table: This table compiles curation-ready candidate causal edges for the microbial trait pH delta mid1, emphasizing mechanisms and assay factors that can expand or constrain a moderate growth-supporting pH breadth of about 2–3 units. It highlights which edges are directly mechanistic versus inferred, taxon-specific, or assay-dependent.*

### 7) Visual evidence (useful for mechanistic curation)
A schematic figure summarizing *E. coli* acid resistance systems AR1–AR6 (including Gad system and F0F1-ATPase) was retrieved and can be used to guide node/edge inclusion when curating acid-side mechanisms. (li2024responseofescherichia media e76b3b93)

### 8) Warnings / “do not curate yet” flags

1. **Do not equate survival-only acid resistance with growth-supporting breadth.** pH delta mid1 is a growth-range trait; lethal-survival assays alone can misrepresent growth breadth. (atasoy2024methodsforstudying pages 3-4, perezrodriguez2024methodsforstudying pages 3-5)

2. **Association ≠ causation (genome-wide gene–pH associations):** Ramoneda et al.’s gene associations (e.g., Na⁺/H⁺ antiporters with higher pH preference; Kdp transporters with lower pH taxa) are strong hypotheses for causal nodes, but should be marked **inferred/uncertain** unless supported by perturbation or direct physiological assays in the target organism. (ramoneda2023buildingagenomebased pages 3-5)

3. **Strong assay dependence:** buffering strategy, medium composition and ion availability (Na⁺/K⁺), growth format, growth phase, and biofilm vs planktonic state should be captured as **experimental factor nodes**, otherwise breadth values may not be comparable across studies. (atasoy2024methodsforstudying pages 4-5)

4. **Community-level interventions (putrescine) are conditional:** putrescine shows opposite effects under acidic vs alkaline conditions; edges should be curated with explicit conditionality and may not translate to pure-culture traits. (jiang2024exogenousputrescineplays pages 1-2)

### 9) DOI-first bibliography (with publication dates and URLs)

1. **Atasoy M, et al.** (May 2024). *Methods for studying microbial acid stress responses: from molecules to populations.* **FEMS Microbiology Reviews**. DOI: **10.1093/femsre/fuae015**. URL: https://doi.org/10.1093/femsre/fuae015 (atasoy2024methodsforstudying pages 2-3, atasoy2024methodsforstudying pages 3-4, atasoy2024methodsforstudying pages 4-5, atasoy2024methodsforstudying pages 36-37)

2. **Li Z, Huang Z, Gu P.** (Aug 2024). *Response of Escherichia coli to Acid Stress: Mechanisms and Applications—A Narrative Review.* **Microorganisms** 12:1774. DOI: **10.3390/microorganisms12091774**. URL: https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4, li2024responseofescherichia pages 10-12, li2024responseofescherichia media e76b3b93)

3. **Qin J, et al.** (Jul 2024). *Characterization of Mild Acid Stress Response in an Engineered Acid-Tolerant Escherichia coli Strain.* **Microorganisms** 12:1565. DOI: **10.3390/microorganisms12081565**. URL: https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2, qin2024characterizationofmild pages 13-14)

4. **Jiang G, et al.** (Jul 2024). *Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.* **Applied and Environmental Microbiology**. DOI: **10.1128/aem.00569-24**. URL: https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2)

5. **Ramoneda J, et al.** (Apr 2023). *Building a genome-based understanding of bacterial pH preferences.* **Science Advances** 9. DOI: **10.1126/sciadv.adf8998**. URL: https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 2-3, ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 8-9)

6. **Ramoneda J, et al.** (Jan 2024). *Leveraging genomic information to predict environmental preferences of bacteria.* **The ISME Journal** 18. DOI: **10.1093/ismejo/wrae195**. URL: https://doi.org/10.1093/ismejo/wrae195 (ramoneda2024leveraginggenomicinformation pages 2-4)

---

### 10) Practical curation takeaway for `ph_delta_mid1.yaml`
For pH delta mid1, a conservative curation strategy is to model **moderate growth breadth** as an emergent property of (i) cytoplasmic pH homeostasis modules (proton consumption, proton export, ion antiport), (ii) membrane permeability control, (iii) energy/transport support (oxidative phosphorylation, ABC transporters), and (iv) assay/environmental factors (buffering, medium ions, growth history), with explicit conditionality and uncertainty annotations where evidence is association-based or community-specific. (atasoy2024methodsforstudying pages 4-5, ramoneda2023buildingagenomebased pages 3-5, qin2024characterizationofmild pages 13-14)

References

1. (atasoy2024methodsforstudying pages 2-3): Merve Atasoy, Simona Bartkova, Zeynep Çetecioğlu-Gürol, Nuno P Mira, Conor O'Byrne, Fernando Pérez-Rodríguez, Arícia Possas, Ott Scheler, J. Sedlakova-Kadukova, Mirka Sinčák, Matthias Steiger, Carmit Ziv, and Peter A Lund. Methods for studying microbial acid stress responses: from molecules to populations. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae015, doi:10.1093/femsre/fuae015. This article has 9 citations and is from a domain leading peer-reviewed journal.

2. (atasoy2024methodsforstudying pages 3-4): Merve Atasoy, Simona Bartkova, Zeynep Çetecioğlu-Gürol, Nuno P Mira, Conor O'Byrne, Fernando Pérez-Rodríguez, Arícia Possas, Ott Scheler, J. Sedlakova-Kadukova, Mirka Sinčák, Matthias Steiger, Carmit Ziv, and Peter A Lund. Methods for studying microbial acid stress responses: from molecules to populations. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae015, doi:10.1093/femsre/fuae015. This article has 9 citations and is from a domain leading peer-reviewed journal.

3. (perezrodriguez2024methodsforstudying pages 3-5): F Pérez-Rodríguez, A Possas, and O Scheler. Methods for studying microbial acid stress responses. Unknown journal, 2024.

4. (atasoy2024methodsforstudying pages 4-5): Merve Atasoy, Simona Bartkova, Zeynep Çetecioğlu-Gürol, Nuno P Mira, Conor O'Byrne, Fernando Pérez-Rodríguez, Arícia Possas, Ott Scheler, J. Sedlakova-Kadukova, Mirka Sinčák, Matthias Steiger, Carmit Ziv, and Peter A Lund. Methods for studying microbial acid stress responses: from molecules to populations. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae015, doi:10.1093/femsre/fuae015. This article has 9 citations and is from a domain leading peer-reviewed journal.

5. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

6. (ramoneda2024leveraginggenomicinformation pages 2-4): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 25 citations.

7. (ramoneda2023buildingagenomebased pages 2-3): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

8. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

9. (ramoneda2023buildingagenomebased pages 6-7): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

10. (qin2024characterizationofmild pages 1-2): Jingliang Qin, Han Guo, Xiaoxue Wu, Shuai Ma, Xin Zhang, Xiaofeng Yang, Bin Liu, Lu Feng, Huanhuan Liu, and Di Huang. Characterization of mild acid stress response in an engineered acid-tolerant escherichia coli strain. Microorganisms, 12:1565, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081565, doi:10.3390/microorganisms12081565. This article has 2 citations.

11. (qin2024characterizationofmild pages 13-14): Jingliang Qin, Han Guo, Xiaoxue Wu, Shuai Ma, Xin Zhang, Xiaofeng Yang, Bin Liu, Lu Feng, Huanhuan Liu, and Di Huang. Characterization of mild acid stress response in an engineered acid-tolerant escherichia coli strain. Microorganisms, 12:1565, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081565, doi:10.3390/microorganisms12081565. This article has 2 citations.

12. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

13. (ramoneda2023buildingagenomebased pages 8-9): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

14. (atasoy2024methodsforstudying pages 18-19): Merve Atasoy, Simona Bartkova, Zeynep Çetecioğlu-Gürol, Nuno P Mira, Conor O'Byrne, Fernando Pérez-Rodríguez, Arícia Possas, Ott Scheler, J. Sedlakova-Kadukova, Mirka Sinčák, Matthias Steiger, Carmit Ziv, and Peter A Lund. Methods for studying microbial acid stress responses: from molecules to populations. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae015, doi:10.1093/femsre/fuae015. This article has 9 citations and is from a domain leading peer-reviewed journal.

15. (perezrodriguez2024methodsforstudying pages 2-3): F Pérez-Rodríguez, A Possas, and O Scheler. Methods for studying microbial acid stress responses. Unknown journal, 2024.

16. (li2024responseofescherichia pages 2-4): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

17. (perezrodriguez2024methodsforstudyinga pages 2-3): F Pérez-Rodríguez, A Possas, and O Scheler. Methods for studying microbial acid stress responses. Unknown journal, 2024.

18. (perezrodriguez2024methodsforstudyinga pages 3-5): F Pérez-Rodríguez, A Possas, and O Scheler. Methods for studying microbial acid stress responses. Unknown journal, 2024.

19. (li2024responseofescherichia media e76b3b93): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

20. (li2024responseofescherichia pages 10-12): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

21. (atasoy2024methodsforstudying pages 36-37): Merve Atasoy, Simona Bartkova, Zeynep Çetecioğlu-Gürol, Nuno P Mira, Conor O'Byrne, Fernando Pérez-Rodríguez, Arícia Possas, Ott Scheler, J. Sedlakova-Kadukova, Mirka Sinčák, Matthias Steiger, Carmit Ziv, and Peter A Lund. Methods for studying microbial acid stress responses: from molecules to populations. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae015, doi:10.1093/femsre/fuae015. This article has 9 citations and is from a domain leading peer-reviewed journal.

22. (perezrodriguez2024methodsforstudyinga pages 40-41): F Pérez-Rodríguez, A Possas, and O Scheler. Methods for studying microbial acid stress responses. Unknown journal, 2024.