---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:48:32.909278'
end_time: '2026-06-18T01:06:21.335326'
duration_seconds: 1068.43
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range mid2
  trait_identifier: METPO:1000462
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH range phenotype in which the growth-supporting external pH range\
    \ spans approximately 7\u20138, characteristic of neutrophile or mild-alkaliphile\
    \ physiology."
  parent_traits: METPO:1000332
  synonyms: Alkali Tolerant, Alkaliphile, Facultative acidophile, Neutrophile, pHR_7_to_8
  evidence_summary: "DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review\
    \ supports modest alkaline-tolerance physiology as the basis of growth across\
    \ pH 7\u20138.)"
  causal_graph_summary: 'ph_range_mid2_mild_alkaline_tolerance: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range mid2
- **METPO identifier:** METPO:1000462
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 7–8, characteristic of neutrophile or mild-alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Facultative acidophile, Neutrophile, pHR_7_to_8
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports modest alkaline-tolerance physiology as the basis of growth across pH 7–8.)
- **Existing causal graph summary:** ph_range_mid2_mild_alkaline_tolerance: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid2.yaml`.

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
- **Trait label:** pH range mid2
- **METPO identifier:** METPO:1000462
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 7–8, characteristic of neutrophile or mild-alkaliphile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Alkaliphile, Facultative acidophile, Neutrophile, pHR_7_to_8
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports modest alkaline-tolerance physiology as the basis of growth across pH 7–8.)
- **Existing causal graph summary:** ph_range_mid2_mild_alkaline_tolerance: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid2.yaml`.

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


## Microbial Trait Causal Graph Research Report: **pH range mid2** (METPO:1000462)

### Executive scope summary (trait definition and boundaries)
The trait **pH range mid2** describes a microbial **growth-supporting external pH range spanning ~7–8**, consistent with **neutrophile or mild-alkaliphile physiology** (external neutral to slightly alkaline). A central physiological requirement across this external range is maintenance of **near-neutral cytoplasmic pH (~7.0–7.5)** despite changes in external pH, with conserved bioenergetics through regulation of the **proton motive force (PMF)**. A contemporary synthesis emphasizes that many bacteria keep internal pH near 7.0–7.5 and adjust the partitioning of PMF between ΔpH and Δψ such that PMF can remain **relatively constant across external pH ~5–8**, i.e., explicitly covering the pH range relevant to this trait. (poolman2023physicochemicalhomeostasisin pages 1-2)

**Boundary cases / distinction from nearby traits.**
* **Neutrophiles with broader tolerance:** *Bacillus subtilis* (a neutrophile model) is described as replicating across ~pH 6–9 (thus including pH 7–8 but not uniquely confined to it). (mitchell2024penicillinbindingproteinredundancy pages 1-2)
* **Strong alkaliphiles:** alkaliphilic *Bacillus* spp. can grow at much higher pH (reported up to ~10.8), while still maintaining cytoplasmic pH suitable for catalysis; methanotroph examples have optima in the ~8.5–10 range. (mitchell2024penicillinbindingproteinredundancy pages 1-2, yao2023howmethanotrophsrespond pages 5-7)
* **Assay dependence:** buffered laboratory media can mask pH stress; minimally buffered conditions can reveal active pH regulation strategies (e.g., biofilm-level modulation of extracellular pH). (tran2024activephregulation pages 1-2)

### Key concepts and definitions (current understanding)

#### 1) Cytoplasmic pH homeostasis and buffering
A defining biophysical constraint is that bacterial cytoplasm contains **very few free protons at neutral pH** (Poolman notes ~10 free protons in ~1 fL cytoplasm at pH 7.2), so even small fluxes can cause large pH shifts unless buffering and regulated transport exist. This motivates cytoplasmic buffering and active membrane transport as core mechanistic entities for any pH-range trait around neutrality. (poolman2023physicochemicalhomeostasisin pages 1-2)

#### 2) Proton motive force (PMF) maintenance across external pH 5–8
PMF (Δp) is composed of **membrane potential (Δψ)** and **transmembrane pH difference (ΔpH)**. Neutralophiles can adjust the relative contributions of Δψ and ΔpH with external pH so that PMF is maintained relatively constant across external pH ~5–8; this directly supports growth around pH 7–8. (poolman2023physicochemicalhomeostasisin pages 1-2)

#### 3) Ion-coupled transport (Na+/H+ and K+/H+ antiport)
Na+/H+ and K+/H+ antiporters are highlighted as **key regulators**: when internal pH rises, these systems exchange Na+ or K+ for H+, thereby **acidifying the cytoplasm**. The presence of multiple transporters with different pH sensitivities supports dynamic regulation over environmental changes. (poolman2023physicochemicalhomeostasisin pages 1-2)

#### 4) Coupling metabolism to pH regulation
Poolman emphasizes links between metabolism and pH homeostasis, including proton-consuming reactions and bioenergetic coupling: decarboxylation-linked transport can generate an electrochemical gradient, and PMF can be used by ATP synthase for ATP generation. (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin pages 1-2)

### Recent developments and latest research (prioritizing 2023–2024)

#### A) Genome-based inference of bacterial pH preferences (2023)
A 2023 *Science Advances* study combined pH-distribution data across **1470 soil/freshwater samples** (across five datasets) with comparative genomics to identify genes associated with pH preference and to build predictive models from genomes. The work supports the idea that pH preference is not reliably inferred from taxonomy alone, but can be predicted using gene content, and it highlights gene categories plausibly connected to pH homeostasis—particularly **Na+/H+ antiporter gene families (e.g., MrpF, MnhG, PhaGF, YufB)** enriched in higher-pH-preferring taxa. This is valuable for TraitMech graph expansion but should be curated with an “association” evidence tag rather than direct mechanistic causation. (ramoneda2023buildingagenomebased pages 3-5)

#### B) Biofilm-specific active pH regulation (2024)
A 2024 *mBio* paper reports that *B. subtilis* biofilms (in minimally buffered conditions) can modulate extracellular pH toward the **preferred neutrophile range**, and that this active regulation depends on a metabolic interplay between **acetate and acetoin biosynthesis**. The study further connects acidification to loss of functional PMF and impaired growth, linking metabolism → environmental pH → bioenergetic stress → growth phenotype. These findings highlight that “pH-range” traits may emerge not only from single-cell homeostasis systems but also from community-state metabolic buffering. (tran2024activephregulation pages 1-2)

#### C) Envelope enzyme redundancy under alkaline shock (2024)
A 2024 *Applied and Environmental Microbiology* study shows that under alkaline shock, a subset of **penicillin-binding proteins (PBPs)** are favored for growth, motivating a causal role for **envelope enzyme redundancy/specialization** in supporting growth when external pH perturbs the periplasmic/extracytoplasmic environment. This provides candidate nodes/edges for a causal graph, but note that this is centered on **alkaline shock** and may reflect acute stress rather than baseline pH 7–8 permissive growth. (mitchell2024penicillinbindingproteinredundancy pages 1-2, mitchell2024penicillinbindingproteinredundancy pages 14-16)

#### D) Direct experimental evidence for alkaline tolerance via NhaC antiporters (2023)
A 2023 *International Journal of Molecular Sciences* study experimentally characterized two **NhaC-family Na+(K+,Li+)/H+ antiporters** (NhaC1 and NhaC2) from *Natronorubrum daqingense*. In heterologous complementation assays in Na+/H+ antiporter-deficient *E. coli* KNabc, expression improved growth in alkaline conditions: the control strain showed poor growth at pH 8.0, while NhaC1 supported growth to pH 8.5 and NhaC2 to pH 9.5. Antiport activity was assayed over pH 7.0–10.0 using everted vesicles, providing direct molecular-function evidence that antiporters can extend growth into/through the mild alkaline range. (wang2023characterizationoftwo pages 7-8)

### Current applications and real-world implementations
1. **Cultivation strategy design and inoculant selection.** Genome-based prediction of pH preference can support improved cultivation and inoculant selection for specific environments (e.g., soils/freshwaters with near-neutral to mildly alkaline pH), aligning pH-mid2 trait assignment with practical strain selection and distribution modeling. (ramoneda2023buildingagenomebased pages 3-5)
2. **Biofilm management.** The discovery that biofilms can actively regulate extracellular pH in minimally buffered contexts suggests intervention targets for controlling unwanted biofilm growth by disrupting metabolic buffering (e.g., acetate/acetoin balance) or the ability to maintain PMF under acidifying microenvironments. (tran2024activephregulation pages 1-2)
3. **Engineering alkaline tolerance via transporters.** Demonstrations that specific Na+/H+ antiporters can confer growth at pH ≥8 support transporter-focused engineering approaches (e.g., introducing/optimizing antiport systems) to tune growth ranges for industrial or environmental use-cases where mild alkalinity occurs. (wang2023characterizationoftwo pages 7-8, poolman2023physicochemicalhomeostasisin pages 1-2)

### Expert opinions and authoritative synthesis (mechanistic analysis)

#### Physiological “core” for pH 7–8 growth: maintain internal pH and PMF
A high-authority 2023 synthesis frames pH homeostasis as part of broader physicochemical homeostasis: maintaining cytoplasmic pH near neutral (7.0–7.5) is treated as a general constraint, and the PMF is kept relatively constant across external pH 5–8 by shifting Δψ/ΔpH contributions. For pH-range-mid2 curation, this suggests a core causal backbone:
*external pH 7–8 → (Δψ/ΔpH rebalancing) → stable PMF → ATP synthesis/transport → growth*.
(poolman2023physicochemicalhomeostasisin pages 1-2)

#### Transporters as causal mediators rather than correlates
The same synthesis explicitly assigns causal function to **Na+/H+ and K+/H+ antiporters** in cytoplasmic acidification when internal pH rises, supporting their inclusion as central nodes/edges in a TraitMech graph. (poolman2023physicochemicalhomeostasisin pages 1-2)

A 2024 electrophysiology review further supports the systems-level importance of antiporters in maintaining membrane potential when proton concentrations contribute little to Δψ under neutral conditions, consistent with the pH 7–8 regime. (lo2024bacterialelectrophysiology pages 10-12)

### Relevant statistics and quantitative data (recent studies)
* **Internal pH setpoint:** internal pH in many cells is maintained in the range **7.0–7.5**. (poolman2023physicochemicalhomeostasisin pages 1-2)
* **Free proton count:** ~**10 free protons** in a ~1 fL cytoplasm at pH **7.2**, motivating buffering and tight regulation. (poolman2023physicochemicalhomeostasisin pages 1-2)
* **External pH band where PMF is stabilized:** neutralophiles can keep PMF relatively constant across external pH **~5–8** (explicitly encompassing pH 7–8). (poolman2023physicochemicalhomeostasisin pages 1-2)
* **Alkaline growth rescue by antiporters (direct experiment):** in *E. coli* KNabc, NhaC1 supported growth to **pH 8.5** and NhaC2 to **pH 9.5**; antiport activity was characterized across **pH 7.0–10.0**. (wang2023characterizationoftwo pages 7-8)
* **Ecological/genomic dataset scale:** bacterial pH preference analysis used **1470 samples** across soil/freshwater pH gradients (five datasets). (ramoneda2023buildingagenomebased pages 3-5)

### Visual evidence (mechanistic schematic)
Poolman 2023 includes schematic figures summarizing pH homeostasis mechanisms (PMF, Na+/H+ and K+/H+ antiporters, and F0F1-ATPase), which are useful for causal-graph conceptualization and curator communication. (poolman2023physicochemicalhomeostasisin media 841fca8f, poolman2023physicochemicalhomeostasisin media 3a7140ff)

---

## Candidate nodes for TraitMech causal graph
| Group | Node label | Brief description | Suggested grounding / CURIE | Supporting source |
|---|---|---|---|---|
| Phenotype/environment | pH range mid2 | Growth-supporting external pH spans approximately 7–8; consistent with neutrophile to mild-alkaliphile physiology | METPO:1000462 | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Phenotype/environment | external pH 7–8 | Mildly alkaline to neutral external condition under which cytoplasmic pH homeostasis must be maintained | ENVO candidate: alkaline environment term uncertain | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Phenotype/environment | neutrophile range | Preferred extracellular pH near neutral; biofilms can modulate local pH toward this range | label only | Tran et al. 2024, mBio, Mar 2024, doi:10.1128/mbio.03387-23, https://doi.org/10.1128/mbio.03387-23 (tran2024activephregulation pages 1-2) |
| Phenotype/environment | alkaline shock | Acute elevation of external pH challenging envelope and pH-homeostasis systems | label only | Mitchell et al. 2024, Appl Environ Microbiol, Jan 2024, doi:10.1128/aem.00548-23, https://doi.org/10.1128/aem.00548-23 (mitchell2024penicillinbindingproteinredundancy pages 1-2) |
| Processes/physiology | cytoplasmic pH homeostasis | Maintenance of internal pH near neutrality despite external pH variation | GO:0010447 | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Processes/physiology | proton motive force | Composite electrochemical proton gradient used for energy transduction and transport; maintained across external pH shifts | GO:0015986 | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Processes/physiology | membrane potential (Δψ) / ΔpH rebalancing | Relative contributions of Δψ and ΔpH shift with external pH to preserve PMF | label only | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Processes/physiology | cytoplasmic buffering | Inorganic/organic buffers reduce pH fluctuation when free proton count is very low | label only | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Processes/physiology | Na+/H+ antiport | Acidifies cytoplasm by coupling Na+ export/import balance to H+ movement | GO:0015385 | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Processes/physiology | K+/H+ antiport | Acidifies cytoplasm through coupled K+ and H+ exchange under alkaline stress | GO:0015386 | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Processes/physiology | amino-acid decarboxylation-driven pH control | Proton-consuming decarboxylation can generate PMF and support pH regulation | EC class candidate: decarboxylases; GO label only | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 2-4) |
| Processes/physiology | extracellular pH regulation by biofilms | Community-level metabolic tuning shifts local pH toward growth-permissive range | label only | Tran et al. 2024, mBio, Mar 2024, doi:10.1128/mbio.03387-23, https://doi.org/10.1128/mbio.03387-23 (tran2024activephregulation pages 1-2) |
| Processes/physiology | acetate/acetoin buffering interplay | Metabolic rerouting reduces harmful acidification during dense growth | label only | Tran et al. 2024, mBio, Mar 2024, doi:10.1128/mbio.03387-23, https://doi.org/10.1128/mbio.03387-23 (tran2024activephregulation pages 1-2) |
| Processes/physiology | maintenance of membrane potential by proton:ion antiporters | Antiporters contribute directly to sustaining Δψ when proton concentrations contribute little | label only | Lo et al. 2024, Annu Rev Biophys, Jul 2024, doi:10.1146/annurev-biophys-030822-032215, https://doi.org/10.1146/annurev-biophys-030822-032215 (lo2024bacterialelectrophysiology pages 10-12) |
| Gene/protein families/complexes | F0F1-ATPase | ATP synthase using proton re-entry to couple PMF to ATP generation | GO:0015986 | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Gene/protein families/complexes | respiratory proton pumps (Complex I/III/IV) | Primary proton-pumping respiratory complexes that expel protons from cytoplasm | GO:0015992 | Yao et al. 2023, Front Microbiol, Jan 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7) |
| Gene/protein families/complexes | NhaC-family Na+(K+,Li+)/H+ antiporter | Membrane antiporter family active across pH 7–10; can support growth under mild alkaline conditions | label only | Wang et al. 2023, Int J Mol Sci, Jun 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8, wang2023characterizationoftwo pages 10-12) |
| Gene/protein families/complexes | NhaC1 | Specific NhaC homolog conferring growth of KNabc up to pH 8.5 in heterologous assay | label only | Wang et al. 2023, Int J Mol Sci, Jun 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8) |
| Gene/protein families/complexes | NhaC2 | Specific NhaC homolog conferring stronger alkaline resistance up to pH 9.5 in heterologous assay | label only | Wang et al. 2023, Int J Mol Sci, Jun 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8) |
| Gene/protein families/complexes | Mrp/Mnh-type Na+/H+ antiporter subunits (e.g., MrpF, MnhG) | Antiporter gene families statistically associated with higher-pH preference across genomes | KEGG tentative: MrpF K05571; MnhG tentative | Ramoneda et al. 2023, Sci Adv, Apr 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) |
| Gene/protein families/complexes | PhaGF / YufB antiporter-related genes | Additional Na+/H+ antiporter-associated gene families enriched in higher-pH taxa | label only | Ramoneda et al. 2023, Sci Adv, Apr 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) |
| Gene/protein families/complexes | penicillin-binding proteins (PBPs) | Envelope enzymes with redundancy/specialization that support growth during alkaline shock | label only | Mitchell et al. 2024, Appl Environ Microbiol, Jan 2024, doi:10.1128/aem.00548-23, https://doi.org/10.1128/aem.00548-23 (mitchell2024penicillinbindingproteinredundancy pages 1-2, mitchell2024penicillinbindingproteinredundancy pages 14-16) |
| Gene/protein families/complexes | S-layer glycoproteins | Negatively charged surface polymers proposed to attract protons near alkaline cell surfaces | label only | Yao et al. 2023, Front Microbiol, Jan 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7) |
| Metabolites/chemicals | proton | Core chemical species whose transmembrane gradient and cytoplasmic abundance define pH homeostasis | CHEBI:15378 | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Metabolites/chemicals | sodium ion | Major coupling ion for Na+/H+ antiport in alkaline adaptation/homeostasis | CHEBI:29101 | Poolman 2023, FEMS Microbiol Rev, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Metabolites/chemicals | potassium ion | Cation involved in K+/H+ exchange and generation of positive membrane potential | CHEBI:29103 | Yao et al. 2023, Front Microbiol, Jan 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7) |
| Metabolites/chemicals | lithium ion | Alternative substrate handled by NhaC antiporters in functional assays | CHEBI:30145 | Wang et al. 2023, Int J Mol Sci, Jun 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8) |
| Metabolites/chemicals | acetate | Overflow metabolite whose accumulation acidifies biofilms and stresses PMF maintenance | CHEBI:30089 | Tran et al. 2024, mBio, Mar 2024, doi:10.1128/mbio.03387-23, https://doi.org/10.1128/mbio.03387-23 (tran2024activephregulation pages 1-2) |
| Metabolites/chemicals | acetoin | Less-acidifying overflow product implicated in buffering against biofilm acidification | CHEBI:15343 | Tran et al. 2024, mBio, Mar 2024, doi:10.1128/mbio.03387-23, https://doi.org/10.1128/mbio.03387-23 (tran2024activephregulation pages 1-2) |
| Metabolites/chemicals | ammonia | Basic compound produced by urease-associated systems in pH adaptation datasets | CHEBI:16134 | Ramoneda et al. 2023, Sci Adv, Apr 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) |
| Metabolites/chemicals | phosphatidylglycerol / phosphatidylcholine / cardiolipin | Lipids increased in some alkaline-adapted methanotroph membranes | CHEBI candidates: PG 17517; PC 64482; cardiolipin 28494 | Yao et al. 2023, Front Microbiol, Jan 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7) |
| Assay/experimental context | heterologous complementation in E. coli KNabc | Antiporter-deficient host used to test whether candidate antiporters restore alkaline/salt tolerance | NCBITaxon:562 | Wang et al. 2023, Int J Mol Sci, Jun 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8, wang2023characterizationoftwo pages 10-12) |
| Assay/experimental context | everted membrane vesicle antiport assay | Functional assay measuring Na+(K+,Li+)/H+ exchange across pH 7–10 | label only | Wang et al. 2023, Int J Mol Sci, Jun 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8) |
| Assay/experimental context | minimally buffered biofilm medium | Experimental condition revealing active extracellular pH regulation otherwise masked in buffered media | label only | Tran et al. 2024, mBio, Mar 2024, doi:10.1128/mbio.03387-23, https://doi.org/10.1128/mbio.03387-23 (tran2024activephregulation pages 1-2) |
| Assay/experimental context | chronic exposure above pH 9.5 | Boundary condition used in B. subtilis alkaline-shock/growth analyses | label only | Mitchell et al. 2024, Appl Environ Microbiol, Jan 2024, doi:10.1128/aem.00548-23, https://doi.org/10.1128/aem.00548-23 (mitchell2024penicillinbindingproteinredundancy pages 6-8) |
| Assay/experimental context | genome–environment association across pH gradients | Comparative genomics approach linking gene content to pH preference, including higher-pH associated antiporters | label only | Ramoneda et al. 2023, Sci Adv, Apr 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) |


*Table: This table organizes candidate causal-graph nodes for microbial growth at external pH ~7–8 into phenotype, process, molecular, chemical, and assay-context groups. It is useful as a curation starting point because it pairs each node with tentative ontology grounding and a source-backed citation.*

---

## Candidate evidence-backed causal edges (triples)
| Subject | Predicate | Object | Node type | Proposed grounding | Evidence snippet | Reference | Evidence strength | Notes / uncertainty |
|---|---|---|---|---|---|---|---|---|
| external pH 7–8 | permits maintenance of | cytoplasmic pH 7.0–7.5 | environment → process | ENVO:09200014; GO:0010447 | “internal pH of many cell types is kept within the range of 7.0 to 7.5” and neutralophiles keep PMF relatively constant across external pH 5–8 (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | review | Good high-level trait-scope edge; not gene-specific. ENVO term for alkaline environment is approximate for pH 7–8 and may need curation review. |
| cytoplasmic buffering | stabilizes | cytoplasmic pH homeostasis | process | GO:0010447 | Cytoplasmic buffering is “critical because a ~1 fL bacterial cytoplasm at pH 7.2 contains only ≈10 free protons” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | review | Broad mechanism; buffer species not uniquely identifiable for all taxa. |
| Na+/H+ antiporter activity | acidifies | cytoplasm | process | GO:0015385 | “Na+/H+ and K+/H+ antiporters acidify the cytoplasm by exporting K+ or Na+ in exchange for H+ when internal pH rises” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | review | Strong consensus mechanism, but not sufficient alone to distinguish mild alkalitolerance from stronger alkaliphily. |
| K+/H+ antiporter activity | acidifies | cytoplasm | process | GO:0015386 | “Na+/H+ and K+/H+ antiporters acidify the cytoplasm by exporting K+ or Na+ in exchange for H+ when internal pH rises” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | review | Generic mechanism; specific transporter identities vary across taxa. |
| proton motive force (PMF) | remains relatively constant across | external pH 5–8 | process → environment | GO:0015986 | “neutralophilic bacteria adjust contributions of ΔpH versus membrane potential so that the proton motive force (PMF) remains relatively constant across an external pH range of about 5–8” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | review | Very relevant trait-level edge for pH mid2; applies to neutralophiles broadly. |
| membrane potential (Δψ) / ΔpH rebalancing | maintains | PMF | process | GO:1902600; GO:0015986 | “the relative contribution of ΔpH and Δψ shifts with external pH” to preserve PMF (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | review | Useful abstract edge; grounding of Δψ as ontology term may require curator judgment. |
| F0F1-ATPase | couples | proton motive force to ATP synthesis | protein complex / process | GO:0015986; GO:0006754 | PMF “drives ATP synthesis” and F0F1 “uses ~3–5 H+ per ATP” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | review | Canonical bioenergetic edge; supportive but not uniquely diagnostic for pH 7–8 growth. |
| decarboxylation pathways | generate or reinforce | proton motive force | process | GO:0016831; GO:0015986 | “the equivalent of 1 proton is pumped per molecule decarboxylated” and decarboxylation can be used to generate PMF (poolman2023physicochemicalhomeostasisin pages 2-4) | Poolman 2023, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | review | Often emphasized for acid stress; may be auxiliary rather than central in mild alkaline tolerance. |
| amino-acid decarboxylase activity | responds to | low internal pH | process | GO:0004069 | “Amino acid decarboxylases have low pH optima and increase activity when internal pH drops” (poolman2023physicochemicalhomeostasisin pages 2-4) | Poolman 2023, Jun 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | review | More directly supports acid-resistance circuitry; include as contextual/conditional edge only. |
| NhaC-family Na+(K+,Li+)/H+ antiporter NhaC1 | enables growth up to | pH 8.5 | gene/protein |  | In E. coli KNabc, “KNabc/nhaC1 supported growth to pH 8.5” and antiport activity occurred over pH 7.0–10.0 (wang2023characterizationoftwo pages 7-8) | Wang 2023, Jun 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 | direct experimental | Strong direct evidence, but from heterologous expression in haloarchaeal gene complementation; taxon-specific and beyond pH mid2 optimum. |
| NhaC-family Na+(K+,Li+)/H+ antiporter NhaC2 | enables growth up to | pH 9.5 | gene/protein |  | In E. coli KNabc, “nhaC2 conferred resistance to pH 9.5” and antiport activity occurred over pH 7.0–10.0 (wang2023characterizationoftwo pages 7-8) | Wang 2023, Jun 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 | direct experimental | Strong but extends into strong alkaliphily; likely too extreme to use as a defining edge for mid2 without uncertainty flag. |
| NhaC1/NhaC2 membrane localization | enables | Na+(K+,Li+)/H+ antiport activity | protein / process | GO:0016020; GO:0015385 | NhaC1/NhaC2 were detected “only in total and membrane protein fractions,” consistent with membrane localization, and showed antiport activity in everted vesicles (wang2023characterizationoftwo pages 7-8) | Wang 2023, Jun 2023, doi:10.3390/ijms241310786, https://doi.org/10.3390/ijms241310786 | direct experimental | Mechanistically solid, though localization alone is not a trait edge. |
| Na+/H+ antiporter genes (PhaGF, MnhG, MrpF, YufB) | are associated with preference for | higher pH | gene family | KEGG:K05571 (MrpF, tentative); KEGG:K05565 (MnhG, tentative) | “Na+/H+ antiporter genes… were consistently overrepresented in taxa with preferences for higher pH” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al. 2023, Apr 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | association | Useful hypothesis-generation edge; not direct causal proof. Groundings tentative and family-dependent. |
| ATPase genes | are associated with | pH preference | gene family / process | GO:0016887 | “ATPases… are among the gene types associated with pH preference” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al. 2023, Apr 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | association | Too nonspecific for direct curation unless tied to a particular ATPase function. |
| urease / ammonia-producing systems | counter | acidity | pathway / chemical | EC:3.5.1.5; CHEBI:16134 | “production of basic compounds (e.g., urease-driven ammonia production)” is among canonical pH-tolerance mechanisms (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al. 2023, Apr 2023, doi:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | association / review | Better suited to low-pH tolerance than pH 7–8 mild alkalinity; curate cautiously. |
| acetate accumulation | disrupts | proton motive force | chemical → process | CHEBI:30089; GO:0015986 | Excessive acidification from overflow metabolites “disrupt[s] a cell’s ability to maintain functional proton motive force (PMF)” (tran2024activephregulation pages 1-2) | Tran et al. 2024, Mar 2024, doi:10.1128/mbio.03387-23, https://doi.org/10.1128/mbio.03387-23 | direct experimental | Biofilm-context edge; describes failure mode rather than positive determinant. |
| acetate/acetoin biosynthesis interplay | buffers against | biofilm acidification | pathway / process |  | Biofilms use a “dynamic interplay between acetate and acetoin biosynthesis” and this is “required to buffer against biofilm acidification” (tran2024activephregulation pages 1-2) | Tran et al. 2024, Mar 2024, doi:10.1128/mbio.03387-23, https://doi.org/10.1128/mbio.03387-23 | direct experimental | Strong for B. subtilis biofilms in minimally buffered medium; assay-specific and community-state-specific. |
| active extracellular pH regulation by B. subtilis biofilms | shifts environment toward | preferred neutrophile range | process → environment |  | Biofilms “modulate their extracellular pH to the preferred neutrophile range… while planktonic cells cannot” (tran2024activephregulation pages 1-2) | Tran et al. 2024, Mar 2024, doi:10.1128/mbio.03387-23, https://doi.org/10.1128/mbio.03387-23 | direct experimental | Valuable ecological/assay edge; phenotype of biofilm state, not universal single-cell mechanism. |
| alkaline shock | favors activity of | subset of penicillin-binding proteins (PBPs) | environment → protein family |  | “a subset of the PBPs are favored for growth under alkaline conditions” (mitchell2024penicillinbindingproteinredundancy pages 1-2) | Mitchell et al. 2024, Jan 2024, doi:10.1128/aem.00548-23, https://doi.org/10.1128/aem.00548-23 | direct experimental | Strong for envelope adaptation during alkaline shock; not yet specific to pH 7–8 and may reflect acute stress more than baseline preference. |
| PBP redundancy / specialization | enables growth during | alkaline shock | protein family / process |  | “PBPs are notable for their redundant activity” and redundancy “enables growth during alkaline shock” (mitchell2024penicillinbindingproteinredundancy pages 1-2, mitchell2024penicillinbindingproteinredundancy pages 14-16) | Mitchell et al. 2024, Jan 2024, doi:10.1128/aem.00548-23, https://doi.org/10.1128/aem.00548-23 | direct experimental + review context | Suitable as envelope-support mechanism; likely secondary to core pH-homeostasis transport systems. |
| proton:ion antiporters | maintain | membrane potential (Δψ) | process | GO:0006970 | Antiporters have a “direct role in maintaining membrane potential” in E. coli (lo2024bacterialelectrophysiology pages 10-12) | Lo et al. 2024, Jul 2024, doi:10.1146/annurev-biophys-030822-032215, https://doi.org/10.1146/annurev-biophys-030822-032215 | review | Mechanistically important systems-level edge; not pH-mid2 exclusive. |
| potassium uptake | supports | positive transmembrane electrical potential | process / chemical | CHEBI:29103 | A “potassium uptake transporter helps generate an internal positive membrane potential” supporting cytoplasmic pH control (yao2023howmethanotrophsrespond pages 5-7) | Yao et al. 2023, Jan 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | review | In review focused partly on methanotrophs/alkaliphiles; likely generalizable but not directly demonstrated here for pH 7–8 taxa. |
| respiratory proton pumps (Complex I/III/IV) | expel | protons from cytoplasm | protein complexes / process | GO:0015992; CHEBI:15378 | “Respiratory primary proton pumps (Complexes I, III, and IV) expel protons from the cytoplasm” (yao2023howmethanotrophsrespond pages 5-7) | Yao et al. 2023, Jan 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | review | Broad bioenergetic mechanism; better as background than trait-defining edge. |
| F0F1-ATPase | allows controlled re-entry of | protons for ATP generation | protein complex / process | GO:0015986; CHEBI:15378 | “protons re-enter to generate ATP via the F0F1-ATPase” (yao2023howmethanotrophsrespond pages 5-7) | Yao et al. 2023, Jan 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | review | Consistent with Poolman; not exclusive to mild alkalitolerance. |
| S-layer glycoproteins / increased negative surface charge | attract | external protons | protein / process | GO:0097502 | Alkaliphiles use “S-layer glycoproteins with net negative charge to attract external protons” (yao2023howmethanotrophsrespond pages 5-7) | Yao et al. 2023, Jan 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | review | More characteristic of stronger alkaliphiles than pH 7–8 taxa; likely over-curation risk for mid2. |
| phospholipid remodeling (↑PG/PC/CL, ↓PE/PS/PA) | modulates | membrane adaptation to high pH | pathway / process | CHEBI:17001; CHEBI:64482; CHEBI:17962 | High-pH response includes increased PG, PC, CL and decreased PE, PS, PA (yao2023howmethanotrophsrespond pages 5-7) | Yao et al. 2023, Jan 2023, doi:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | review | Taxon-specific lipid pattern from methanotroph examples; not yet a general causal edge for mid2. |
| B. subtilis (neutrophile) | replicates across | pH ~6–9 | organism / environment | NCBITaxon:1423 | “B. subtilis, representing most neutrophiles, replicates across pH ~6–9” (mitchell2024penicillinbindingproteinredundancy pages 1-2) | Mitchell et al. 2024, Jan 2024, doi:10.1128/aem.00548-23, https://doi.org/10.1128/aem.00548-23 | review/background in experimental paper | Helpful boundary case for trait scope; organism-specific, not mechanistic. |


*Table: This table compiles curation-ready candidate causal edges for microbial growth across external pH ~7–8, emphasizing pH homeostasis, PMF regulation, antiporters, ATP synthase, metabolic buffering, and envelope adaptations. It separates direct experimental evidence from review- and association-level support so curators can prioritize robust edges for TraitMech.*

---

## Warnings / curation caveats (do not over-curate)
1. **Association ≠ causation in comparative genomics.** Gene enrichments (e.g., Mrp/Mnh antiporter subunits enriched in higher-pH taxa) are valuable for hypotheses and candidate nodes, but should be curated as **association-level** evidence unless direct functional experiments exist for the focal taxa/trait context. (ramoneda2023buildingagenomebased pages 3-5)
2. **Biofilm state is a distinct physiological context.** Extracellular pH modulation via acetate/acetoin is demonstrated in *B. subtilis* **biofilms** under minimally buffered conditions; it may not generalize to planktonic growth assays commonly used for trait annotation. Curate with an **assay/context qualifier**. (tran2024activephregulation pages 1-2)
3. **Strong alkaliphile mechanisms may not be specific to pH 7–8.** S-layer proton-attracting strategies and certain lipid remodeling patterns are described for alkaliphiles and specific taxa (e.g., methanotrophs with optima 8.5–10). These may be inappropriate as defining edges for a mild-alkaline trait without taxon/context constraints. (yao2023howmethanotrophsrespond pages 5-7)
4. **Heterologous complementation edges need taxon caution.** NhaC1/2 experiments provide strong mechanistic evidence for antiporter function and alkaline tolerance, but the growth phenotype was measured in *E. coli* complementation and includes pH values beyond the mid2 band; curate with **uncertainty/taxon qualifiers**. (wang2023characterizationoftwo pages 7-8)

---

## DOI-first bibliography (with URLs and publication dates)
1. Poolman B. **Physicochemical homeostasis in bacteria.** *FEMS Microbiology Reviews.* Jun 2023;47(4). DOI: **10.1093/femsre/fuad033**. URL: https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2)
2. Ramoneda J, Stallard-Olivera E, Hoffert M, et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances.* Apr 2023;9(17). DOI: **10.1126/sciadv.adf8998**. URL: https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5)
3. Tran P, Lander SM, Prindle A. **Active pH regulation facilitates Bacillus subtilis biofilm development in a minimally buffered environment.** *mBio.* Mar 2024;15(3). DOI: **10.1128/mbio.03387-23**. URL: https://doi.org/10.1128/mbio.03387-23 (tran2024activephregulation pages 1-2)
4. Mitchell SL, Kearns DB, Carlson EE. **Penicillin-binding protein redundancy in Bacillus subtilis enables growth during alkaline shock.** *Applied and Environmental Microbiology.* Jan 2024;90(1). DOI: **10.1128/aem.00548-23**. URL: https://doi.org/10.1128/aem.00548-23 (mitchell2024penicillinbindingproteinredundancy pages 1-2)
5. Lo W-C, Krasnopeeva E, Pilizota T. **Bacterial Electrophysiology.** *Annual Review of Biophysics.* Jul 2024;53(1):487–510 (final online publication expected May 2024 per journal note). DOI: **10.1146/annurev-biophys-030822-032215**. URL: https://doi.org/10.1146/annurev-biophys-030822-032215 (lo2024bacterialelectrophysiology pages 10-12)
6. Yao X, Wang J, Hu B. **How methanotrophs respond to pH: A review of ecophysiology.** *Frontiers in Microbiology.* Jan 2023;13. DOI: **10.3389/fmicb.2022.1034164**. URL: https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7)
7. Wang Q, Qiao M, Song J. **Characterization of Two Na+(K+, Li+)/H+ Antiporters from Natronorubrum daqingense.** *International Journal of Molecular Sciences.* Jun 2023;24(13):10786. DOI: **10.3390/ijms241310786**. URL: https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8)


References

1. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

2. (mitchell2024penicillinbindingproteinredundancy pages 1-2): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

3. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

4. (tran2024activephregulation pages 1-2): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

5. (poolman2023physicochemicalhomeostasisin pages 2-4): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

6. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

7. (mitchell2024penicillinbindingproteinredundancy pages 14-16): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

8. (wang2023characterizationoftwo pages 7-8): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

9. (lo2024bacterialelectrophysiology pages 10-12): Wei-Chang Lo, Ekaterina Krasnopeeva, and Teuta Pilizota. Bacterial electrophysiology. Jul 2024. URL: https://doi.org/10.1146/annurev-biophys-030822-032215, doi:10.1146/annurev-biophys-030822-032215. This article has 23 citations and is from a domain leading peer-reviewed journal.

10. (poolman2023physicochemicalhomeostasisin media 841fca8f): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

11. (poolman2023physicochemicalhomeostasisin media 3a7140ff): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

12. (wang2023characterizationoftwo pages 10-12): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

13. (mitchell2024penicillinbindingproteinredundancy pages 6-8): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.