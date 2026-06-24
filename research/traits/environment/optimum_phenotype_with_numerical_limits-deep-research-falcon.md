---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:51:02.444963'
end_time: '2026-06-18T00:03:54.447405'
duration_seconds: 772.0
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: optimum phenotype with numerical limits
  trait_identifier: METPO:1000536
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: optimum_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by the value at which an organism exhibits
    maximum growth rate or activity.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review
    supports the environmental value at which growth is maximal as a standard quantitative
    descriptor.) | DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review
    supports the external pH at which cytoplasmic homeostasis sustains peak growth
    as an analogous optimum on the pH axis.)'
  causal_graph_summary: 'optimum_phenotype_descriptor: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** optimum phenotype with numerical limits
- **METPO identifier:** METPO:1000536
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the value at which an organism exhibits maximum growth rate or activity.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports the environmental value at which growth is maximal as a standard quantitative descriptor.) | DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports the external pH at which cytoplasmic homeostasis sustains peak growth as an analogous optimum on the pH axis.)
- **Existing causal graph summary:** optimum_phenotype_descriptor: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **optimum phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/optimum_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** optimum phenotype with numerical limits
- **METPO identifier:** METPO:1000536
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the value at which an organism exhibits maximum growth rate or activity.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports the environmental value at which growth is maximal as a standard quantitative descriptor.) | DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports the external pH at which cytoplasmic homeostasis sustains peak growth as an analogous optimum on the pH axis.)
- **Existing causal graph summary:** optimum_phenotype_descriptor: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **optimum phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/optimum_phenotype_with_numerical_limits.yaml`.

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


## Research Report: METPO:1000536 “Optimum phenotype with numerical limits” (ENVIRONMENT)

### 1) Short scope summary (trait semantics and boundary cases)

**Trait definition (operational):** The trait describes a **numerical environmental value** (e.g., temperature, pH, salinity) at which an organism exhibits **maximum growth rate or activity** under a specified assay context. This matches METPO’s definition (“value at which an organism exhibits maximum growth rate or activity”) and aligns with how microbial physiology and predictive microbiology define “optimum” as the peak of a performance curve (e.g., μ(T), μ(pH), μ(salinity)). Quantitative “optimum” values are typically estimated from growth curves or from fitted secondary models that include an explicit optimum parameter (e.g., Topt). (ombura2024dualsuppressionof pages 9-11, ombura2024dualsuppressionof pages 6-7)

**Distinguish from adjacent traits:**
- **Tolerance range / growth limits:** Distinct from the **range of conditions permitting growth** (minimum/maximum). Cardinal-parameter frameworks explicitly distinguish **Tmin, Topt, Tmax** and treat Tmin/Tmax as limiting boundaries where growth approaches zero, while Topt is the maximum. (ombura2024dualsuppressionof pages 9-11, ombura2024dualsuppressionof pages 6-7)
- **Homeostasis traits (mechanistic capacities):** Optimum along the pH axis is often *enabled* by **intracellular pH homeostasis**, but “optimum pH” is not itself the homeostasis mechanism; it is an *assay-derived phenotype* contingent on the ability to maintain cytoplasmic conditions in a permissive range. (krulwich2011molecularaspectsof pages 1-3, poolman2023physicochemicalhomeostasisin pages 1-2)
- **“Broad optimum range” vs single optimum:** Some organisms are reported with **broad optimal growth ranges** across an axis (e.g., pH 3–5) versus a narrow optimum. This suggests that TraitMech curation should either: (i) store a point estimate plus uncertainty, or (ii) explicitly represent **optimal range endpoints** as “numerical limits” (depending on how METPO intends “numerical limits”). (ianutsevich2023theroleof pages 1-2)

**Boundary cases to curate carefully:**
- **Survival vs growth:** Reviews emphasize organisms may survive outside growth-permissive conditions; “optimum” should be tied to **growth/activity maxima**, not survival. (krulwich2011molecularaspectsof pages 1-3)
- **Assay dependence:** Optimum depends on medium composition, measurement endpoint (growth rate, germination, radial growth, enzyme activity), and model choice (CTMI, Ratkowsky, etc.), so assay-factor nodes are important context. (ombura2024dualsuppressionof pages 6-7, zajc2014osmoadaptationstrategyof pages 2-3)

### 2) Key concepts and definitions (current understanding)

#### 2.1 Cardinal-parameter definition of optimum
A widely used formalization is the **cardinal temperature model** (including CTMI), in which:
- **Tmin, Topt, Tmax** are the **minimum, optimum, and maximum temperatures (°C)**, with Topt corresponding to maximal performance (e.g., maximal conidial germination or growth rate) and Tmin/Tmax describing limiting boundaries. (ombura2024dualsuppressionof pages 9-11)

Quantitative example (2024, CTMI-derived for entomopathogenic fungal radial growth):
- **Topt ~ 26.7–31.1°C**, **Tmin ~ −3.7 to 13.1°C**, **Tmax ~ 35.2 to 45.4°C** depending on strain. (ombura2024dualsuppressionof pages 6-7)

#### 2.2 pH-optimum definitions used in microbial ecology/physiology
Recent synthesis work defines classes by **optimum growth pH**:
- **Acidophiles:** optimum growth pH **< 5**.
- **Extreme acidophiles:** optimum growth pH **< 3**.
- **Moderate acidophiles:** may grow from **pH 3 to 7.5** with optima between **pH 4 and 5**. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2)

Fungal-focused synthesis also highlights that some acidophilic fungi exhibit:
- **Narrow optimum** (e.g., Phlebiopsis gigantea optimum at **pH 4.0** with sharp decline at **pH 2.6 and 5.0**).
- **Broad optimum range** (e.g., Mollisia sp. **pH 3.0–5.0**). (ianutsevich2023theroleof pages 1-2)

#### 2.3 Salinity/NaCl optimum vs growth range (halophiles)
In a halophilic fungus example, the optimum is explicitly separated from growth boundaries:
- *Wallemia ichthyophaga* exhibits a salinity optimum at **15–20% (wt/vol) NaCl**, while growth is only possible between approximately **10% and saturation (~32% NaCl)**, illustrating “optimum” versus “limits/range.” (zajc2014osmoadaptationstrategyof pages 1-2)

### 3) Recent developments and latest research (prioritize 2023–2024)

#### 3.1 2023: Physicochemical homeostasis as mechanistic foundation for optima
Poolman (FEMS Microbiology Reviews, 2023) consolidates how **internal pH (often ~7.0–7.5)**, **PMF**, and **ionic strength** are kept within limits, shaping the organism’s ability to maintain maximal growth under a given external condition. The review explicitly identifies **Na+/H+ and K+/H+ antiporters as key regulators of bacterial pH homeostasis**, and connects pH regulation to energy coupling via PMF. (poolman2023physicochemicalhomeostasisin pages 1-2)

It also provides quantitative context relevant to osmotic/salinity optima:
- Typical intracellular **K+** concentrations differ greatly across taxa (e.g., ~0.2 M in *E. coli*, ~0.8 M in *L. lactis*, ~2.1 M in *Haloferax volcanii*), reinforcing that ion homeostasis is a mechanistic node that can shift optimal performance across environments. (poolman2023physicochemicalhomeostasisin pages 2-4)

#### 3.2 2023: Explicit optimum-growth definitions for pH and temperature classifications
Dopson et al. (Frontiers in Microbiology, 2023) provides explicit definitions of optimum growth pH for acidophile categories and a temperature-optimum-based definition for eurypsychrophiles: microbes that can grow down to ~4°C but have an optimum growth temperature above 15°C. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2)

#### 3.3 2024: Cardinal-parameter quantification in real-world fungal deployment contexts
Ombura et al. (Frontiers in Microbiology, 2024) applies CTMI/cardinal concepts to entomopathogenic fungi relevant to biocontrol, explicitly defining Tmin/Topt/Tmax and estimating ranges for strains; this is a clear recent, applied example of “optimum phenotype with numerical limits” being extracted and used for real-world implementation decisions. (ombura2024dualsuppressionof pages 9-11, ombura2024dualsuppressionof pages 6-7)

### 4) Current applications and real-world implementations

**Predictive microbiology / process design:** Cardinal models (Tmin/Topt/Tmax) and related secondary models are used to translate experimental growth curves into parameters for **risk assessment and process optimization** (e.g., food safety, fermentation, biocontrol). The 2024 EPF study uses temperature optima and tolerance bounds to select strains compatible with operational conditions, illustrating real-world parameterization of optima. (ombura2024dualsuppressionof pages 6-7, ombura2024dualsuppressionof pages 1-2)

**Industrial and environmental microbiology:** pH and osmolarity optima inform:
- **Selection of organisms/enzymes** for acidic/alkaline processes (pH optima and homeostasis mechanisms are central to extremophile utility).
- **Bioremediation/bioprocess performance** where salinity or ionic strength constraints determine feasible growth/activity maxima.

**Biotechnology at low pH/low temperature:** Reviews of acidophiles/eurypsychrophiles highlight biotechnological use-cases such as low-temperature metal sulfide dissolution, where both pH optimum and temperature optimum constrain operational design. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2)

### 5) Expert opinions / authoritative synthesis (mechanistic analysis)

High-authority reviews emphasize that “optimum” is an emergent phenotype resulting from integrated systems-level constraints:
- **pH homeostasis** enables growth across external pH variation by maintaining internal pH in a narrow functional range; this is coupled to **PMF**, respiratory proton pumps, ATP synthase, and antiporters. (krulwich2011molecularaspectsof pages 1-3, poolman2023physicochemicalhomeostasisin pages 1-2)
- **Osmoadaptation strategies** shape salinity optima through either **compatible-solute accumulation** or **inorganic ion (“salt-in”) strategies**, with energetic tradeoffs and proteome constraints. (deole2020apotassiumchloride pages 1-2, poolman2023physicochemicalhomeostasisin pages 2-4)

### 6) Candidate causal-graph entities (nodes)

The following node inventory is designed for TraitMech curation and grouped by type, with suggested ontology grounding where available.

| Node label | Node type | Suggested CURIE(s) | Evidence/notes |
|---|---|---|---|
| external pH | environmental factor | ENVO:3100031 (pH) | Core environmental axis for many microbial optima; external pH can differ markedly from cytoplasmic pH maintained during growth, so this node should represent the assayed outside-medium condition rather than intracellular pH (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 12-14). |
| optimum external pH | environmental factor | label-only candidate; related to METPO:1000536 | “Optimum growth pH” is explicitly used in recent reviews to classify acidophiles/extreme acidophiles; examples include optimum growth pH <5 for acidophiles and <3 for extreme acidophiles (dopson2023eurypsychrophilicacidophilesfrom pages 1-2). |
| temperature | environmental factor | ENVO:09200014 | Cardinal models treat temperature as an environmental driver with Tmin/Topt/Tmax; growth curves peak at Topt and decline to zero near Tmin/Tmax (ombura2024dualsuppressionof pages 9-11, ombura2024dualsuppressionof pages 6-7). |
| optimum temperature (Topt) | environmental factor | label-only candidate | CTMI/cardinal-parameter literature explicitly defines Topt as the optimum temperature for growth/germination, distinct from lower and upper tolerance bounds Tmin and Tmax (ombura2024dualsuppressionof pages 9-11, ombura2024dualsuppressionof pages 6-7). |
| salinity | environmental factor | ENVO:3100022 | Salinity is directly assayed as NaCl % in halophile studies; growth optimum is separable from wider tolerance range (e.g., optimum at 15–20% NaCl with broader growth limits) (zajc2014osmoadaptationstrategyof pages 1-2, zajc2014osmoadaptationstrategyof pages 2-3). |
| sodium chloride concentration | environmental factor | CHEBI:26710 | Used operationally to define salinity optimum in culture media; optimal NaCl is a standard quantitative descriptor for halophiles/halotolerant taxa (zajc2014osmoadaptationstrategyof pages 1-2, zajc2014osmoadaptationstrategyof pages 2-3). |
| water activity | environmental factor | label-only candidate | Salinity studies often report water-activity range alongside NaCl optimum, helping distinguish optimum from broader permissive range (zajc2014osmoadaptationstrategyof pages 1-2). |
| osmolarity / hyperosmotic stress | environmental factor | label-only candidate | Hypertonicity causes shrinkage/plasmolysis and induces compatible-solute accumulation systems that influence where growth remains optimal (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin pages 1-2). |
| potassium availability | environmental factor | CHEBI:29103 | In extreme halophiles, environmental K+ can determine whether cells use a KCl-based or glycine-betaine-based osmoprotection strategy, potentially shifting optimal performance under salinity (deole2020apotassiumchloride pages 8-8, deole2020apotassiumchloride pages 1-2). |
| growth medium composition | assay factor | label-only candidate | Reported “optimum” is assay-dependent and typically measured in defined or saline media; medium composition affects osmolyte use, ion availability, and inferred optimum values (zajc2014osmoadaptationstrategyof pages 2-3, deole2020apotassiumchloride pages 1-2). |
| batch-culture growth rate assay | assay factor | label-only candidate | Salinity optima in Wallemia were inferred from specific growth rates/dry biomass in batch cultures, emphasizing that the trait is assay-observed (zajc2014osmoadaptationstrategyof pages 1-2, zajc2014osmoadaptationstrategyof pages 2-3). |
| conidial germination / radial growth assay | assay factor | label-only candidate | Temperature optima are often model-derived from radial-growth or germination assays; CTMI-derived Topt/Tmin/Tmax depend on this assay context (ombura2024dualsuppressionof pages 9-11, ombura2024dualsuppressionof pages 6-7). |
| cardinal temperature model with inflection (CTMI) | assay factor | label-only candidate | Useful assay/model node because it operationalizes optimum as Topt and distinguishes it from Tmin/Tmax; likely should remain as assay context rather than mechanism (ombura2024dualsuppressionof pages 9-11, ombura2024dualsuppressionof pages 6-7). |
| intracellular pH homeostasis | process | GO:0006885 | Central mechanistic determinant of pH optimum; bacteria/fungi maintain a relatively narrow internal pH range while growing across broader external pH values (krulwich2011molecularaspectsof pages 1-3, ianutsevich2023theroleof pages 1-2). |
| proton motive force | process | GO:0015988 | PMF integrates membrane potential and transmembrane ΔpH and is a core energetic determinant of pH-dependent growth performance (poolman2023physicochemicalhomeostasisin pages 1-2, krulwich2011molecularaspectsof pages 1-3). |
| transmembrane pH gradient (ΔpH) | process | GO:1902600 | One PMF component; direction/magnitude shifts with external pH and helps explain growth optima and limits (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 1-3). |
| membrane potential (Δψ) | process | GO:0006811 | Second PMF component; acidophiles/alkaliphiles adjust Δψ together with ΔpH to sustain growth under non-neutral pH (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 1-3). |
| Na+/H+ antiport | process | GO:0015385 | Major pH-homeostasis mechanism; antiporters exchange cytoplasmic Na+ or K+ for protons and are repeatedly identified as key regulators of bacterial pH homeostasis (krulwich2011molecularaspectsof pages 3-5, poolman2023physicochemicalhomeostasisin pages 1-2). |
| K+/H+ antiport | process | GO:0015386 | Included with Na+/H+ antiporters as core pH regulators affecting cytoplasmic pH and thus pH optimum (poolman2023physicochemicalhomeostasisin pages 1-2). |
| compatible-solute accumulation | process | GO:0015893 | Cells counter hyperosmotic stress by importing/accumulating compatible solutes to (sub)molar levels, affecting salinity optimum (poolman2023physicochemicalhomeostasisin pages 2-4, zajc2014osmoadaptationstrategyof pages 1-2). |
| osmoadaptation | process | GO:0042594 | Umbrella process covering compatible-solute synthesis/import and ionic strategies that determine salinity optimum and tolerance (zajc2014osmoadaptationstrategyof pages 1-2, deole2020apotassiumchloride pages 1-2). |
| glycerol biosynthetic process | process | GO:0006071 | Glycerol is the major osmotically regulated solute in Wallemia under salt stress; likely mechanistically tied to optimal growth at high salinity (zajc2014osmoadaptationstrategyof pages 1-2, zajc2014osmoadaptationstrategyof pages 2-3). |
| ectoine biosynthetic process | process | GO:0019491 | Included because ectoine synthesis is a canonical compatible-solute pathway in halophiles and was identified genomically in a high-salt adapted bacterium (deole2020apotassiumchloride pages 1-2). |
| potassium ion accumulation | process | GO:1901669 | Represents the “salt-in” KCl strategy in halophiles; intracellular K+ rises in some conditions and can substitute for organic osmolytes (deole2020apotassiumchloride pages 8-8, deole2020apotassiumchloride pages 1-2). |
| HOG MAPK signaling pathway | process | GO:0000165 | In Wallemia, Hog1/HOG signaling is implicated in osmoadaptation and should be considered a candidate regulatory process for salinity optimum (zajc2014osmoadaptationstrategyof pages 2-3). |
| fatty-acid / membrane-lipid remodeling | process | GO:0006633, GO:0006643 | Recent pH-stress studies and fungal acidophile work link membrane lipids to adaptation outside the optimum, suggesting contribution to pH optimum breadth or sharpness (ianutsevich2023theroleof pages 1-2). |
| F0F1-ATP synthase complex | gene/protein/complex | GO:0045259 | ATP synthase contributes to pH homeostasis and PMF interconversion; alkaliphile-specific adaptations affect activity especially at high pH (krulwich2011molecularaspectsof pages 12-14, poolman2023physicochemicalhomeostasisin pages 1-2). |
| Mrp Na+/H+ antiporter complex | gene/protein/complex | GO:0009274 (bacterial-type flagellum not suitable); label-only candidate for Mrp complex | The Mrp hetero-oligomeric antiporter is highlighted as a major alkaliphile pH-homeostasis determinant; curate as label-only complex if exact stable complex identifier is unavailable (krulwich2011molecularaspectsof pages 12-14). |
| OpuA compatible-solute ABC transporter | gene/protein/complex | UniProtKB label-only candidate “OpuA”; GO:0015893 | Poolman highlights OpuA as an active importer that accumulates glycine betaine to high levels during hyperosmotic stress, directly relevant to salinity optimum mechanisms (poolman2023physicochemicalhomeostasisin pages 2-4). |
| Hog1 MAP kinase | gene/protein/complex | label-only candidate | Hog1 is cited in Wallemia osmoadaptation context; regulatory evidence exists but may be taxon-specific and should be curated cautiously (zajc2014osmoadaptationstrategyof pages 2-3). |
| GPD1 / glycerol-3-phosphate dehydrogenase | gene/protein/complex | label-only candidate; EC:1.1.1.8 | Mentioned as linked to glycerol production in Wallemia osmoadaptation, supporting a mechanistic route from gene activity to compatible-solute accumulation (zajc2014osmoadaptationstrategyof pages 2-3). |
| V-ATPase | gene/protein/complex | GO:0033180 | In fungi, V-ATPase is identified among systems maintaining intracellular pH, making it a candidate determinant of pH optimum (ianutsevich2023theroleof pages 1-2). |
| Pma1 plasma-membrane H+-ATPase | gene/protein/complex | label-only candidate | Fungal proton pumping by Pma1 is cited as a key contributor to near-neutral internal pH maintenance under acidic conditions (ianutsevich2023theroleof pages 1-2). |
| respiratory-chain proton pumps | gene/protein/complex | label-only candidate | Primary proton pumps are part of the pH-homeostasis machinery that helps establish PMF and sustain growth near pH optima (krulwich2011molecularaspectsof pages 3-5, poolman2023physicochemicalhomeostasisin pages 1-2). |
| glycine betaine | metabolite/chemical | CHEBI:17750 | Canonical compatible solute; imported by OpuA and used by halophiles as an alternative to KCl, influencing growth under saline conditions (deole2020apotassiumchloride pages 8-8, poolman2023physicochemicalhomeostasisin pages 2-4). |
| glycerol | metabolite/chemical | CHEBI:17522 | Major compatible solute/osmolyte in Wallemia at high salinity; strong candidate node for salinity-optimum graphs (zajc2014osmoadaptationstrategyof pages 1-2, zajc2014osmoadaptationstrategyof pages 2-3). |
| trehalose | metabolite/chemical | CHEBI:16589 | Reported as a major osmolyte in acidophilic fungi under optimal pH and implicated in adaptation when pH deviates from optimum (ianutsevich2023theroleof pages 1-2). |
| polyols | metabolite/chemical | CHEBI:26191 | Broad osmolyte class reported in acidophilic fungi and halophiles; useful node when exact compound identity varies by taxon (ianutsevich2023theroleof pages 1-2, zajc2014osmoadaptationstrategyof pages 1-2). |
| proline | metabolite/chemical | CHEBI:17203 | Mentioned as an osmolyte candidate in fungi; evidence is weaker/general, so likely uncertain unless linked to a specific taxon/assay (ianutsevich2023theroleof pages 1-2). |
| ectoine | metabolite/chemical | CHEBI:53300 | Hallmark compatible solute in bacterial osmoadaptation; genes for ectoine synthesis support high-salt adaptation in a deep-brine isolate (deole2020apotassiumchloride pages 1-2). |
| potassium chloride | metabolite/chemical | CHEBI:32588 | Represents the inorganic “salt-in” osmoprotectant strategy used by extreme halophiles; may oppose or substitute for organic osmolytes depending on K+ availability (deole2020apotassiumchloride pages 8-8, deole2020apotassiumchloride pages 1-2). |
| sodium ion | metabolite/chemical | CHEBI:29101 | Exchange substrate for Na+/H+ antiporters and contributor to external salinity stress; relevant to pH and osmotic homeostasis (krulwich2011molecularaspectsof pages 3-5, poolman2023physicochemicalhomeostasisin pages 1-2). |
| potassium ion | metabolite/chemical | CHEBI:29103 | Cytoplasmic K+ concentration is a major determinant of ionic strength and a direct osmoadaptation variable in salt-in strategists (poolman2023physicochemicalhomeostasisin pages 2-4, deole2020apotassiumchloride pages 8-8). |
| proton | metabolite/chemical | CHEBI:15378 | Central to PMF, antiporter function, ATP synthase coupling, and intracellular pH control (poolman2023physicochemicalhomeostasisin pages 1-2, krulwich2011molecularaspectsof pages 1-3). |
| membrane lipids | cellular component | GO:0097060 | pH adaptation in fungi is associated with changes in membrane lipid composition; candidate structural node for breadth/sharpness of pH optimum (ianutsevich2023theroleof pages 1-2). |
| cytoplasmic membrane | cellular component | GO:0005886 | Physical location for antiporters, ATP synthase, proton pumps, and PMF generation; essential cellular context node (krulwich2011molecularaspectsof pages 3-5, poolman2023physicochemicalhomeostasisin pages 1-2). |
| cytoplasm | cellular component | GO:0005737 | Location of controlled internal pH, ionic strength, compatible-solute accumulation, and enzyme performance that ultimately shape the measured optimum (poolman2023physicochemicalhomeostasisin pages 1-2, krulwich2011molecularaspectsof pages 1-3). |
| cell wall | cellular component | GO:0005618 | Wallemia shows cell-wall thickening and cell-wall enrichment at high salinity; likely protective but may be taxon-specific/uncertain for generic optimum graphs (zajc2014osmoadaptationstrategyof pages 2-3). |


*Table: This table lists curation-ready candidate nodes for a TraitMech graph of 'optimum phenotype with numerical limits,' covering environmental axes, assay context, mechanisms, molecules, and cellular structures. It emphasizes evidence-backed nodes relevant to pH, temperature, and salinity optima, with citations to available context IDs.*

### 7) Evidence-backed edges (subject–predicate–object triples)

Edges below are selected because they map to generalizable mechanisms (pH homeostasis; compatible-solute uptake) and/or provide explicit, taxon-specific mechanistic examples useful as conditional subgraphs.

| Subject | Predicate | Object | Evidence snippet (quote) | Reference details (DOI, year, URL) | Citation ID | Notes/uncertainty |
|---|---|---|---|---|---|---|
| Na+/H+ antiporters | contribute_to | intracellular pH homeostasis | "Key regulators of bacterial pH homeostasis are Na+/H+ and K+/H+ antiporters" | DOI:10.1093/femsre/fuad033; 2023; https://doi.org/10.1093/femsre/fuad033 | (poolman2023physicochemicalhomeostasisin pages 1-2) | Strong general bacterial mechanism; supports pH-optimum maintenance indirectly by stabilizing internal pH. |
| proton-sensing ion/H+ antiporters | exchange | cytoplasmic Na+ or K+ for protons | "Proton-sensing ion/H+ antiporters ... export K+ or Na+ in exchange for protons" | DOI:10.1093/femsre/fuad033; 2023; https://doi.org/10.1093/femsre/fuad033 | (poolman2023physicochemicalhomeostasisin pages 1-2) | Mechanistic edge supporting how antiporters regulate intracellular pH. |
| F0F1-ATPase | interconverts_with | proton motive force | "the F0F1-ATPase uses three to five protons to synthesize one molecule of ATP" | DOI:10.1093/femsre/fuad033; 2023; https://doi.org/10.1093/femsre/fuad033 | (poolman2023physicochemicalhomeostasisin pages 1-2) | General bioenergetic mechanism relevant to pH homeostasis. |
| F1F0-ATP synthase activity | contributes_to | pH homeostasis at high external pH | "F1F0-ATP synthase activity contributes to pH homeostasis" and alkaliphile-specific adaptations show greater effects "at high pH" | DOI:10.1038/nrmicro2549; 2011; https://doi.org/10.1038/nrmicro2549 | (krulwich2011molecularaspectsof pages 12-14) | Strong but partly review-level; especially relevant to alkaliphiles/high-pH growth. |
| OpuA compatible-solute transporter | increases | intracellular glycine betaine | "OpuA can 'accumulat[e] the compatible solute glycine betaine to (sub)molar levels'" | DOI:10.1093/femsre/fuad033; 2023; https://doi.org/10.1093/femsre/fuad033 | (poolman2023physicochemicalhomeostasisin pages 2-4) | Strong mechanistic edge for osmolarity optimum under hypertonic stress. |
| hyperosmotic stress | activates/selects_for | compatible-solute accumulation | "Hypertonicity causes shrinkage and plasmolysis ... active importers such as OpuA can 'accumulat[e] the compatible solute glycine betaine to (sub)molar levels'" | DOI:10.1093/femsre/fuad033; 2023; https://doi.org/10.1093/femsre/fuad033 | (poolman2023physicochemicalhomeostasisin pages 2-4) | General physiological relationship; assay/environment dependent. |
| high NaCl salinity | induces | glycerol accumulation | "glycerol is identified as the major osmotically regulated (compatible) solute" | DOI:10.1128/AEM.02702-13; 2014; https://doi.org/10.1128/AEM.02702-13 | (zajc2014osmoadaptationstrategyof pages 1-2) | Taxon-specific to *Wallemia ichthyophaga*; mark uncertain for generic graph. |
| high NaCl salinity | induces | cell-wall thickening / altered morphology | "3-fold cell-wall thickening, ~4-fold increase in clump size" | DOI:10.1128/AEM.02702-13; 2014; https://doi.org/10.1128/AEM.02702-13 | (zajc2014osmoadaptationstrategyof pages 2-3) | Taxon-specific to *Wallemia ichthyophaga*; uncertain for broad curation. |
| environmental K+ availability | triggers | KCl-to-glycine betaine osmoprotectant switch | "medium K+ concentration (~10 mM) at which the KCl to glycine betaine osmoprotectant switch in H. halophila occurs" | DOI:10.1038/s41598-020-59231-9; 2020; https://doi.org/10.1038/s41598-020-59231-9 | (deole2020apotassiumchloride pages 1-2) | Strong but taxon-specific to *Halorhodospira halophila*; uncertain for generic graph. |
| K+ limitation | decreases | cytoplasmic K+ concentration | "respond to K+ limitation by reducing their cytoplasmic K+ concentration" | DOI:10.1038/s41598-020-59231-9; 2020; https://doi.org/10.1038/s41598-020-59231-9 | (deole2020apotassiumchloride pages 8-8) | Supports mechanistic route for osmoprotection switching; taxon-specific/uncertain. |
| glycine betaine | replaces_role_of | KCl as osmoprotectant under K+ limitation | "the role of KCl as an osmoprotectant is largely taken over by glycine betaine" | DOI:10.1038/s41598-020-59231-9; 2020; https://doi.org/10.1038/s41598-020-59231-9 | (deole2020apotassiumchloride pages 8-8) | Strong within *H. halophila*; uncertain for generalization. |
| amino-acid decarboxylation | contributes_to | pH homeostasis | "amino-acid decarboxylases have 'remarkably low pH optima' and their activity increases when internal pH drops, contributing directly to pH homeostasis" | DOI:10.1093/femsre/fuad033; 2023; https://doi.org/10.1093/femsre/fuad033 | (poolman2023physicochemicalhomeostasisin pages 2-4) | Strong general mechanism, especially under acid stress. |
| amino-acid decarboxylation plus antiporter exchange | generates | proton motive force | "decarboxylation plus antiporter exchange generates a proton motive force (PMF) with 'the equivalent of 1 proton ... per molecule decarboxylated'" | DOI:10.1093/femsre/fuad033; 2023; https://doi.org/10.1093/femsre/fuad033 | (poolman2023physicochemicalhomeostasisin pages 2-4) | Strong mechanistic edge linking acid-stress physiology to energy coupling. |


*Table: This table summarizes evidence-backed subject–predicate–object edges relevant to microbial pH and salinity/osmolarity optima. It highlights which relationships are broadly supported versus taxon-specific and therefore more uncertain for TraitMech curation.*

### 8) Relevant statistics and quantitative data (from recent studies)

**Cardinal temperature parameters (2024, EPF strains; CTMI):**
- Reported **Topt range** for radial growth: **26.7–31.1°C**.
- Reported **Tmin range**: **−3.7 to 13.1°C**.
- Reported **Tmax range**: **35.2 to 45.4°C**. (ombura2024dualsuppressionof pages 6-7)

**Conidial germination thermal bounds (2024, EPF strains):**
- Germination thermal range **8.1–45.4°C** and “optimal range” **26.7–31.1°C** are reported for SIT-compatible strains in this context. (ombura2024dualsuppressionof pages 1-2)

**Internal pH range (2023 synthesis):**
- Internal pH of many cell types is maintained around **7.0–7.5**, relevant as a mechanistic constraint shaping where external pH yields maximal growth. (poolman2023physicochemicalhomeostasisin pages 1-2)

**Intracellular K+ concentration examples (2023 synthesis):**
- ~**0.2 M** (*E. coli*), **0.8 M** (*L. lactis*), **2.1 M** (*Haloferax volcanii*). (poolman2023physicochemicalhomeostasisin pages 2-4)

**pH optimum examples (2023 acidophilic fungi synthesis):**
- *Phlebiopsis gigantea* narrow optimum at **pH 4.0**.
- *Mollisia* sp. broad optimum range **pH 3.0–5.0**.
- Acidophilic yeasts: “optimal cellular pH” **4.5–5.5** (taxon-context). (ianutsevich2023theroleof pages 1-2)

**Salinity optimum vs limits example (2014):**
- *Wallemia ichthyophaga* optimum **15–20% NaCl**, growth limits around **10–32% NaCl**. (zajc2014osmoadaptationstrategyof pages 1-2)

### 9) Curation warnings (claims that may be too weak/general or too taxon-specific)

1. **Taxon-specific osmolyte details:** The strong evidence that *Wallemia ichthyophaga* uses glycerol as a major osmolyte and exhibits morphological/cell-wall changes at high NaCl is valuable but likely **not generalizable across microbes**; curate as a taxon-scoped subgraph or mark as uncertain. (zajc2014osmoadaptationstrategyof pages 1-2, zajc2014osmoadaptationstrategyof pages 2-3)
2. **KCl↔glycine betaine switch:** The K+-dependent osmoprotectant switch in *Halorhodospira halophila* is a compelling mechanistic edge but is **taxon- and habitat-specific**; curate as an example mechanism rather than a universal rule. (deole2020apotassiumchloride pages 1-2, deole2020apotassiumchloride pages 8-8)
3. **Model/assay nodes vs biology nodes:** CTMI/cardinal parameters are critical for how optima are *estimated*, but they are **assay/model context** rather than mechanistic determinants; ensure they are placed in an “experimental factor/model” layer, not as biological causal drivers. (ombura2024dualsuppressionof pages 9-11, ombura2024dualsuppressionof pages 6-7)

---

## DOI-first bibliography (with publication dates and URLs)

1. **Poolman B.** Physicochemical homeostasis in bacteria. *FEMS Microbiology Reviews*. **2023-06**. DOI: **10.1093/femsre/fuad033**. https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2, poolman2023physicochemicalhomeostasisin pages 2-4)
2. **Dopson M, González-Rosales C, Holmes DS, Mykytczuk N.** Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies. *Frontiers in Microbiology*. **2023-03**. DOI: **10.3389/fmicb.2023.1149903**. https://doi.org/10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 1-2)
3. **Ianutsevich EA, Danilova OA, Grum-Grzhimaylo OA, Tereshina VM.** The Role of Osmolytes and Membrane Lipids in the Adaptation of Acidophilic Fungi. *Microorganisms*. **2023-07**. DOI: **10.3390/microorganisms11071733**. https://doi.org/10.3390/microorganisms11071733 (ianutsevich2023theroleof pages 1-2)
4. **Ombura FLO, Abd-Alla AMM, Akutse KS, et al.** Dual suppression of *Glossina pallidipes* using entomopathogenic fungal-based biopesticides and sterile insect technique. *Frontiers in Microbiology*. **2024-12**. DOI: **10.3389/fmicb.2024.1472324**. https://doi.org/10.3389/fmicb.2024.1472324 (ombura2024dualsuppressionof pages 9-11, ombura2024dualsuppressionof pages 6-7, ombura2024dualsuppressionof pages 1-2)
5. **Krulwich TA, Sachs G, Padan E.** Molecular aspects of bacterial pH sensing and homeostasis. *Nature Reviews Microbiology*. **2011-05**. DOI: **10.1038/nrmicro2549**. https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 12-14)
6. **Zajc J, Kogej T, Galinski EA, Ramos J, Gunde-Cimerman N.** Osmoadaptation strategy of the most halophilic fungus, *Wallemia ichthyophaga*, growing optimally at salinities above 15% NaCl. *Applied and Environmental Microbiology*. **2014-01**. DOI: **10.1128/AEM.02702-13**. https://doi.org/10.1128/aem.02702-13 (zajc2014osmoadaptationstrategyof pages 1-2, zajc2014osmoadaptationstrategyof pages 2-3)
7. **Deole R, Hoff WD.** A potassium chloride to glycine betaine osmoprotectant switch in the extreme halophile *Halorhodospira halophila*. *Scientific Reports*. **2020-02**. DOI: **10.1038/s41598-020-59231-9**. https://doi.org/10.1038/s41598-020-59231-9 (deole2020apotassiumchloride pages 1-2, deole2020apotassiumchloride pages 8-8)


References

1. (ombura2024dualsuppressionof pages 9-11): Fidelis L. O. Ombura, Adly M.M Abd-Alla, Komivi S. Akutse, Steven Runo, Paul O. Mireji, Rosemary Bateta, Joseck E. Otiwi, Inusa J. Ajene, and Fathiya M. Khamis. Dual suppression of glossina pallidipes using entomopathogenic fungal-based biopesticides and sterile insect technique. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1472324, doi:10.3389/fmicb.2024.1472324. This article has 3 citations and is from a peer-reviewed journal.

2. (ombura2024dualsuppressionof pages 6-7): Fidelis L. O. Ombura, Adly M.M Abd-Alla, Komivi S. Akutse, Steven Runo, Paul O. Mireji, Rosemary Bateta, Joseck E. Otiwi, Inusa J. Ajene, and Fathiya M. Khamis. Dual suppression of glossina pallidipes using entomopathogenic fungal-based biopesticides and sterile insect technique. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1472324, doi:10.3389/fmicb.2024.1472324. This article has 3 citations and is from a peer-reviewed journal.

3. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

4. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

5. (ianutsevich2023theroleof pages 1-2): Elena A. Ianutsevich, Olga A. Danilova, Olga A. Grum-Grzhimaylo, and Vera M. Tereshina. The role of osmolytes and membrane lipids in the adaptation of acidophilic fungi. Microorganisms, 11:1733, Jul 2023. URL: https://doi.org/10.3390/microorganisms11071733, doi:10.3390/microorganisms11071733. This article has 22 citations.

6. (zajc2014osmoadaptationstrategyof pages 2-3): Janja Zajc, Tina Kogej, Erwin A. Galinski, José Ramos, and Nina Gunde-Cimerman. Osmoadaptation strategy of the most halophilic fungus, wallemia ichthyophaga, growing optimally at salinities above 15% nacl. Applied and Environmental Microbiology, 80:247-256, Jan 2014. URL: https://doi.org/10.1128/aem.02702-13, doi:10.1128/aem.02702-13. This article has 129 citations and is from a peer-reviewed journal.

7. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

8. (zajc2014osmoadaptationstrategyof pages 1-2): Janja Zajc, Tina Kogej, Erwin A. Galinski, José Ramos, and Nina Gunde-Cimerman. Osmoadaptation strategy of the most halophilic fungus, wallemia ichthyophaga, growing optimally at salinities above 15% nacl. Applied and Environmental Microbiology, 80:247-256, Jan 2014. URL: https://doi.org/10.1128/aem.02702-13, doi:10.1128/aem.02702-13. This article has 129 citations and is from a peer-reviewed journal.

9. (poolman2023physicochemicalhomeostasisin pages 2-4): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

10. (ombura2024dualsuppressionof pages 1-2): Fidelis L. O. Ombura, Adly M.M Abd-Alla, Komivi S. Akutse, Steven Runo, Paul O. Mireji, Rosemary Bateta, Joseck E. Otiwi, Inusa J. Ajene, and Fathiya M. Khamis. Dual suppression of glossina pallidipes using entomopathogenic fungal-based biopesticides and sterile insect technique. Frontiers in Microbiology, Dec 2024. URL: https://doi.org/10.3389/fmicb.2024.1472324, doi:10.3389/fmicb.2024.1472324. This article has 3 citations and is from a peer-reviewed journal.

11. (deole2020apotassiumchloride pages 1-2): Ratnakar Deole and Wouter D. Hoff. A potassium chloride to glycine betaine osmoprotectant switch in the extreme halophile halorhodospira halophila. Scientific Reports, Feb 2020. URL: https://doi.org/10.1038/s41598-020-59231-9, doi:10.1038/s41598-020-59231-9. This article has 43 citations and is from a peer-reviewed journal.

12. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

13. (deole2020apotassiumchloride pages 8-8): Ratnakar Deole and Wouter D. Hoff. A potassium chloride to glycine betaine osmoprotectant switch in the extreme halophile halorhodospira halophila. Scientific Reports, Feb 2020. URL: https://doi.org/10.1038/s41598-020-59231-9, doi:10.1038/s41598-020-59231-9. This article has 43 citations and is from a peer-reviewed journal.

14. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.