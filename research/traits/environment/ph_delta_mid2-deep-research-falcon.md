---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:06:00.522813'
end_time: '2026-06-18T00:28:54.256945'
duration_seconds: 1373.73
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta mid2
  trait_identifier: METPO:1000476
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH delta phenotype with a growth-supporting pH breadth of approximately\
    \ 3\u20134 pH units, characteristic of organisms with broad pH-tolerance breadth."
  parent_traits: METPO:1000232
  synonyms: pHd_3_4
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports broad pH-homeostasis flexibility as the basis of generalist pH-tolerance
    physiology.)'
  causal_graph_summary: 'ph_delta_mid2_broad_breadth: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta mid2
- **METPO identifier:** METPO:1000476
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 3–4 pH units, characteristic of organisms with broad pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_3_4
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports broad pH-homeostasis flexibility as the basis of generalist pH-tolerance physiology.)
- **Existing causal graph summary:** ph_delta_mid2_broad_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid2.yaml`.

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
- **Trait label:** pH delta mid2
- **METPO identifier:** METPO:1000476
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 3–4 pH units, characteristic of organisms with broad pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_3_4
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports broad pH-homeostasis flexibility as the basis of generalist pH-tolerance physiology.)
- **Existing causal graph summary:** ph_delta_mid2_broad_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid2.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **pH delta mid2** (METPO:1000476)

## 0. Scope summary (curation-ready)
**Trait definition (METPO:1000476)**: *pH delta mid2* denotes a **growth-supporting pH breadth of ~3–4 pH units**, characteristic of **broad pH-tolerant (“generalist”)** organisms. Mechanistically, this phenotype is best treated as a **capacity trait**: the ability to maintain **cytoplasmic pH homeostasis** and bioenergetic function while external pH changes, rather than an “environmental preference” alone. Core mechanistic determinants include (i) **proton motive force (PMF = ΔpH + Δψ) management**, (ii) **H+ influx/efflux via ion antiporters and ATPases**, (iii) **proton-consuming metabolic pathways**, and (iv) **buffering and envelope adaptations** that reduce proton leak and stabilize macromolecules. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5, rebelo2023unravelingtherole pages 18-20)

**Boundary cases / nearby traits**:
- **Broad growth breadth vs survival**: Some microbes can **survive** at very low pH without **growing**; this should not be curated as pH delta mid2 if growth is not supported across the range. (li2024responseofescherichia pages 1-2)
- **Extremophiles vs generalists**: Extremophiles can grow at pH <3 or >11, but they may rely on constitutive/extreme adaptations not representative of generalist ~3–4-unit breadth; such edges should be flagged taxon-specific. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5)

## 1. Key concepts & current understanding (mechanistic framing)
### 1.1 Cytoplasmic pH homeostasis as the proximal mechanistic target
Most bacteria must maintain cytoplasmic pH within a narrow range compatible with growth, while tolerating much wider external pH ranges. A central framework is that external pH perturbs the **PMF components** (ΔpH and Δψ), and microbes adjust transport and metabolism to keep intracellular pH within growth-permissive limits. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5)

### 1.2 Core mechanistic “modules” relevant to broad pH breadth
From authoritative mechanistic synthesis, the main modules that can be curated into a causal graph include:
- **Primary proton pumps** (respiratory chain proton pumps; proton-translocating ATPases) generating PMF and driving compensatory transport. (krulwich2011molecularaspectsof pages 1-3)
- **Secondary transporters** that exchange cations for protons, especially **Na+/H+** and **K+/H+ antiport systems**, enabling either H+ extrusion (acid) or H+ import (alkali) depending on context. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 15-17)
- **Proton-consuming reactions** (e.g., **amino-acid decarboxylation** systems; hydrogenase; malolactic fermentation) that directly consume intracellular H+ during acid challenge. (krulwich2011molecularaspectsof pages 5-6, rebelo2023unravelingtherole pages 18-20)
- **Chemical buffering** (polyamines, polyphosphate, inorganic phosphate; proteins/amino acids) providing passive buffering capacity. (rebelo2023unravelingtherole pages 18-20)
- **Envelope/membrane adaptations** reducing proton permeability or altering surface charge/proton access. (krulwich2011molecularaspectsof pages 5-6, jiang2024exogenousputrescineplays pages 1-2)

## 2. Recent developments and latest research (prioritizing 2023–2024)
### 2.1 Genome-based inference of pH preferences (large-scale association evidence)
A major recent advance is linking **genome content to pH preference** (realized niche) across large environmental gradients. In a 2023 *Science Advances* study (1470 samples across pH gradients), Ramoneda et al. identified **56 functional gene types** reproducibly associated with inferred pH preference and built a predictive model. Reported performance included **cross-dataset average R² ≈ 0.80** and a held-out validation **MAE ≈ 0.63 pH units** (training MAE ≈ 0.43). (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)

Mechanistically interpretable gene families in this association set include **Na+/H+ antiport-related genes** (e.g., Mrp/Mnh-type components) associated with higher pH preference and **Kdp K+ transporters** associated with lower pH preference, among others. These are high-value candidates for TraitMech nodes, but edges should be marked **association-derived** unless backed by direct physiological perturbation experiments. (ramoneda2023buildingagenomebased pages 3-5)

### 2.2 Systems biology / omics evidence from engineered acid tolerance
A 2024 experimental study engineered *E. coli* with a synthetic acid-tolerance module (**gadE, hdeB, sodB, katE**) and reported improved growth at **pH 6.0**; the final OD600 was **131% and 124%** of the parent strain under specified comparisons. Transcriptomics implicated **oxidative phosphorylation**, **TCA cycle**, and **lysine-dependent acid resistance**, and WGCNA identified **263 hub genes** with strong positive association to mild acid response, including **ABC transporters**. This supports edges linking energy metabolism and transport capacity to pH stress robustness, but the engineered context should be flagged as non-native and potentially not generalizable. (qin2024characterizationofmild pages 1-2)

### 2.3 Chemical modulation of pH stress adaptability (polyamines)
A 2024 *Applied and Environmental Microbiology* study reported that **exogenous putrescine** can shift pH-stress adaptability in biofilm-based activated sludge: under acidic conditions, protonated putrescine increased membrane permeability/entry and promoted acid-resistance strategies (including glutamate/GABA-linked processes) and ATPase/oxidative phosphorylation activity; under alkaline conditions, its limited protonation and continued H+ consumption could exacerbate alkali stress. These findings support “environmental chemical modulator” edges (putrescine → acid resistance pathways/ATPase expression), but are **assay- and community-context-dependent**. (jiang2024exogenousputrescineplays pages 1-2)

## 3. Current applications and real-world implementations
### 3.1 Industrial fermentation: engineering strains to reduce pH-control costs
Acid accumulation during industrial fermentation can cause steep pH decline and inhibit microbial metabolism; modern strain engineering efforts therefore focus on improving acid tolerance to maintain productivity and reduce alkali dosing needs. Recent review-level synthesis describes organic acid accumulation (e.g., ~50 g/L with pKa 3–5) driving medium pH down to ~2.0 without base addition, motivating engineering and process control. (li2024responseofescherichia pages 1-2)

The engineered *E. coli* acid-tolerance module study (2024) is a concrete implementation path: modular overexpression of acid tolerance genes combined with omics-guided optimization, potentially applicable to acid-producing bioprocesses. (qin2024characterizationofmild pages 1-2)

### 3.2 Environmental microbiology: predicting pH niches from genomes
Genome-based prediction of pH preferences (2023) supports practical uses in **microbial inoculant selection**, **species distribution models**, and **cultivation strategy design** by prioritizing taxa with gene complements linked to pH niches. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)

## 4. Expert synthesis / authoritative analysis
Krulwich, Sachs & Padan (Nature Reviews Microbiology, 2011) remains a highly authoritative mechanistic framework for curating causal edges in pH tolerance graphs. It emphasizes that broad tolerance arises from integrated control of PMF, ion antiport, ATPase activity, and proton-consuming metabolism, with key environmental modulators (e.g., Na+, Cl−) that tune system performance. It also provides strong taxon-specific exemplars (e.g., alkaliphile Mrp requirement; *H. pylori* urease/UreI localization strategy) that should be curated with explicit taxonomic scope constraints. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 11-12)

## 5. Relevant statistics & quantitative data (from recent and authoritative sources)
- **Neutralophile growth external pH range**: ~**5.5–9.0** cited for neutralophiles, with cytoplasmic pH maintained near neutral/alkaline despite swings. (krulwich2011molecularaspectsof pages 1-3, rebelo2023unravelingtherole pages 18-20)
- **Genome-to-pH preference prediction**: cross-dataset **R² ≈ 0.80**; held-out **MAE ≈ 0.63 pH units** for 56-gene-type model (limitations outside pH 4–9). (ramoneda2023buildingagenomebased pages 6-7)
- **Engineered *E. coli* mild-acid phenotype**: final OD600 at pH 6.0 **131%** and **124%** of parent strain under specified comparisons; plus 263 hub genes from WGCNA linked to acid response. (qin2024characterizationofmild pages 1-2)

## 6. Candidate nodes (grouped by type; ontology grounding suggestions)
### 6.1 Environmental / experimental factors
- External pH (ENVO label-only)
- External Na+ availability (CHEBI:29101 sodium(1+)) (krulwich2011molecularaspectsof pages 12-14)
- Cl− as a modulator (CHEBI:17996 chloride) (krulwich2011molecularaspectsof pages 15-17)
- Organic acids (CHEBI class; pKa/undissociated fraction as experimental factor) (rebelo2023unravelingtherole pages 18-20)
- Exogenous polyamines (putrescine CHEBI:17148) (jiang2024exogenousputrescineplays pages 1-2)

### 6.2 Core bioenergetics and processes
- Proton motive force (PMF), ΔpH, Δψ (GO label-only) (krulwich2011molecularaspectsof pages 1-3)
- Oxidative phosphorylation (GO:0006119) (qin2024characterizationofmild pages 1-2)
- TCA cycle (GO:0006099) (qin2024characterizationofmild pages 1-2)

### 6.3 Transporters and complexes
- Na+/H+ antiporters (GO:0015385), including **NhaA** (label) (krulwich2011molecularaspectsof pages 5-6)
- **Mrp** Na+/H+ antiporter complex (label) (krulwich2011molecularaspectsof pages 12-14)
- K+/H+ exchangers (label) (krulwich2011molecularaspectsof pages 5-6)
- F1Fo ATP synthase / ATPase (GO:0046933) (krulwich2011molecularaspectsof pages 1-3)
- V-type Na+-pumping ATPase (label) (krulwich2011molecularaspectsof pages 15-17)
- ABC transporter complexes (GO:0043190) (qin2024characterizationofmild pages 1-2)

### 6.4 Metabolic acid resistance pathways / enzymes
- Glutamate decarboxylase system (GadB; GO:0047579) and GadC antiporter (label) (rebelo2023unravelingtherole pages 18-20)
- Arginine decarboxylase system (adiA/adiC; label) (rebelo2023unravelingtherole pages 18-20)
- Lysine decarboxylase system (cadA/cadB; label) (rebelo2023unravelingtherole pages 18-20)
- Urease (EC:3.5.1.5) and urea channel **UreI** (label) (krulwich2011molecularaspectsof pages 11-12)

### 6.5 Cellular envelope / buffering chemicals
- Membrane lipid remodeling (label; GO broad) (jiang2024exogenousputrescineplays pages 1-2)
- Buffering pools: polyamines, polyphosphate, inorganic phosphate (CHEBI) (rebelo2023unravelingtherole pages 18-20)

## 7. Candidate evidence-backed causal edges (curation table)
The table below is structured for direct translation into `data/traits/environment/ph_delta_mid2.yaml` as candidate edges (with curation notes for uncertainty/scope).

| Edge (Subject —predicate→ Object) | Node type(s) | Suggested ontology grounding | Evidence snippet | Source (DOI, year, URL) | Curation note |
|---|---|---|---|---|---|
| External pH stress —alters→ proton motive force (PMF) component balance (ΔpH, Δψ) | environmental factor → biological process | ENVO:environmental pH (label-only); GO:0015986 proton motive force-driven transport | “the relative magnitudes and even orientation can change with external pH; under strong pH stress a PMF component can reverse orientation” (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 1-3) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong general mechanism; useful upstream edge for phenotype scope rather than a gene-level trait edge |
| Proton-pumping respiratory complexes —generate→ PMF | protein complex → biological process | GO:0015990 proton motive force generation by electron transport chain; label-only respiratory chain proton pumps | “Primary proton pumps (respiratory chain pumps...) generate PMF” (krulwich2011molecularaspectsof pages 1-3) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong broad mechanism across bacteria |
| Respiratory chain upregulation under acid challenge —supports→ cytoplasmic pH homeostasis | biological process → biological process | GO:1902600 proton transmembrane transport (label-only for condition-specific upregulation) | “In respiratory bacteria the respiratory chain generates the PMF and is upregulated during acid challenge” (krulwich2011molecularaspectsof pages 3-5) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | General but somewhat inferred to breadth phenotype |
| F1Fo-ATPase activity —contributes to→ proton translocation for pH homeostasis | protein complex → biological process | GO:0046933 proton-transporting ATP synthase complex, rotational mechanism | “proton-coupled ATPases” are primary strategy; “F1–F0 ATPase proton pump” is an active acid-tolerance mechanism (krulwich2011molecularaspectsof pages 1-3, rebelo2023unravelingtherole pages 18-20) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549; 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Strong, general; direction of proton flow can be taxon/condition dependent |
| V-type Na+-pumping ATPase —supports→ alkaline pH homeostasis | protein complex → biological process | GO:0033178 proton-transporting two-sector ATPase complex, catalytic domain (closest generic); label-only Na+-pumping V1Vo ATPase | “E. hirae up-regulates Na+-pumping V1Vo at high pH” (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 15-17) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong but taxon-specific exemplar; curate as conditional/alkaline strategy |
| Na+/H+ antiporter activity —imports H+ / extrudes Na+ to support→ alkaline pH homeostasis | transporter → biological process | GO:0015385 sodium:proton antiporter activity | “cation/proton antiporters... are transcriptionally up-regulated for inward proton transport under alkaline stress” (krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong general alkaline-tolerance edge |
| NhaA Na+/H+ antiporter —mediates→ electrogenic 2H+/1Na+ exchange | transporter → molecular function | GO:0015385 sodium:proton antiporter activity; label-only NhaA | “E. coli NhaA 2H+/1Na+ couples Δψ to H+ entry” (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 15-17) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong mechanistic edge; taxon-specific protein but canonical example |
| Cytoplasmic Na+ availability —supports→ Mrp antiporter activity | chemical → transporter activity | CHEBI:29101 sodium(1+); label-only Mrp antiporter activity | “Cytoplasmic Na+ is necessary to sustain high antiport activity” (krulwich2011molecularaspectsof pages 12-14) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong in extreme alkaliphile context |
| Mrp Na+/H+ antiporter complex —required for→ alkaline pH homeostasis | protein complex → biological process | label-only Mrp antiporter complex; GO:0015385 sodium:proton antiporter activity | “Mrp antiporter is the major strategy for alkaliphile pH homeostasis;... mrpA point mutation abolishes Na+/H+ antiport and alkaline pH homeostasis” (krulwich2011molecularaspectsof pages 12-14) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Very strong but specific to alkaliphiles; high-value candidate edge |
| Na+/solute symporters and Na+ channels —maintain→ cytoplasmic Na+ pool | transporter → chemical homeostasis | label-only Na+/solute symporters; label-only MotPS/NavBP | “cytoplasmic Na+ is supplied by multiple Na+/solute symporters and Na+ channels” (krulwich2011molecularaspectsof pages 12-14) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong in alkaliphile model; indirect edge to pH breadth |
| ATP synthase subunit-a / subunit-c alkaliphile motifs —reduce→ proton loss | protein region/motif → biological process | label-only AxAxAxA motif; label-only PxxExxP motif | “specific sequence motifs... support function at high pH, guard against proton loss... Mutating these motifs reduces ATP synthase activity, impairs pH homeostasis” (krulwich2011molecularaspectsof pages 12-14) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong but sequence-feature curation may be difficult; extremophile-specific |
| Glutamate decarboxylase system (gad / GadB) —consumes→ intracellular H+ | enzyme/pathway → chemical | label-only gad; GO:0047579 glutamate decarboxylase activity; CHEBI:15378 H+ | “proton-consuming enzymes (glutamate decarboxylase GadB with its antiporter)” and GDAR is an active acid-tolerance mechanism (krulwich2011molecularaspectsof pages 5-6, rebelo2023unravelingtherole pages 18-20) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549; 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Strong acid-tolerance edge; broadly curated in Gram-negatives |
| GadC antiporter —exchanges→ extracellular glutamate for intracellular GABA | transporter → transport process | label-only GadC; CHEBI:18237 glutamate; CHEBI:16865 GABA | “GadC exchanges extracellular glutamate for intracellular GABA” (rebelo2023unravelingtherole pages 18-20) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Strong and specific; good node for acid-response subgraph |
| Arginine decarboxylase system (adiA/adiC) —contributes to→ acid resistance | gene/pathway → phenotype process | label-only adiA; label-only adiC | “Specific genes/transporters noted: adiA and adiC in ADAR” among active acid-tolerance mechanisms (rebelo2023unravelingtherole pages 18-20) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Moderate: review-level support in current context, but no direct breadth assay here |
| Lysine decarboxylase system (cadA/cadB) —contributes to→ acid resistance | gene/pathway → phenotype process | label-only cadA; label-only cadB | “cadA and cadB in LDAR” among active acid-tolerance mechanisms (rebelo2023unravelingtherole pages 18-20) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Moderate: review-level support; useful candidate but less directly tied to 3–4-unit breadth |
| Urease activity —produces→ ammonia/periplasmic buffering that supports acid acclimation | enzyme → chemical process | EC:3.5.1.5 urease; CHEBI:16134 ammonia | “acid acclimation depends on urease activity... producing periplasmic buffering” (krulwich2011molecularaspectsof pages 11-12) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong but mainly Helicobacter-specific |
| UreI expression —enables→ inner-membrane recruitment of urease | membrane protein → localization process | label-only UreI; label-only UreA/UreB urease | “UreA/UreB recruitment to the inner membrane (dependent on UreI expression) increases membrane-bound urease activity” (krulwich2011molecularaspectsof pages 11-12) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong mechanistic edge; highly taxon-specific |
| Inner-membrane recruitment of urease —increases→ membrane-bound urease activity | localization process → enzyme activity | label-only membrane-bound urease activity | “increases membrane-bound urease activity (two-fold at pH 4.5)” (krulwich2011molecularaspectsof pages 11-12) | 10.1038/nrmicro2549, 2011, https://doi.org/10.1038/nrmicro2549 | Strong quantitative support; Helicobacter-specific |
| Putrescine —enhances→ glutamate-based acid resistance / GABA pathway | metabolite → pathway | CHEBI:17148 putrescine; label-only glutamate-based acid resistance; label-only GABA pathway | “protonated putrescine enhances the glutamate-based acid resistance strategy and the γ-aminobutyric acid metabolic pathway to reduce acid stress” (jiang2024exogenousputrescineplays pages 1-2) | 10.1128/AEM.00569-24, 2024, https://doi.org/10.1128/AEM.00569-24 | Moderate: biofilm/community study; condition-specific and chemical-addition dependent |
| Putrescine —stimulates→ ATPase expression | metabolite → gene expression/process | CHEBI:17148 putrescine; label-only ATPase expression | “putrescine stimulated ATPase expression” (jiang2024exogenousputrescineplays pages 1-2) | 10.1128/AEM.00569-24, 2024, https://doi.org/10.1128/AEM.00569-24 | Moderate; useful as environmental/chemical modulation edge rather than core universal mechanism |
| Putrescine —stimulates→ oxidative phosphorylation activity | metabolite → pathway | CHEBI:17148 putrescine; GO:0006119 oxidative phosphorylation | “enhancing oxidative phosphorylation activity” (jiang2024exogenousputrescineplays pages 1-2) | 10.1128/AEM.00569-24, 2024, https://doi.org/10.1128/AEM.00569-24 | Moderate; context-specific to biofilm sludge and acid conditions |
| Membrane lipid remodeling toward saturated fatty acids —reduces→ proton diffusion across membrane | biological process → transport property | GO:0006633 fatty acid biosynthetic process (broad); label-only membrane lipid remodeling | “remodeling membrane lipids (unsaturated → saturated fatty acids) to limit proton diffusion” (jiang2024exogenousputrescineplays pages 1-2) | 10.1128/AEM.00569-24, 2024, https://doi.org/10.1128/AEM.00569-24 | Moderate-general; mechanistically plausible and widely cited, but current support is review-like in this context |
| Polyamines / amino acids / phosphate buffers —buffer→ cytoplasmic pH | chemical class → biological process | CHEBI:polyamines (label-only); CHEBI:18237 amino acids (broad); CHEBI:26078 phosphate | “Passive buffering of cytoplasmic pH is provided by small molecules (amino acids, proteins, polyamines, polyphosphate, inorganic phosphate)” (rebelo2023unravelingtherole pages 18-20) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Moderate; general buffering mechanism, not specific gene-level edge |
| Oxidative phosphorylation gene upregulation —positively associates with→ mild acid stress response | pathway → phenotype association | GO:0006119 oxidative phosphorylation | “genes involved in oxidative phosphorylation... were highly positively associated with mild acid stress responses” (qin2024characterizationofmild pages 1-2) | 10.3390/microorganisms12081565, 2024, https://doi.org/10.3390/microorganisms12081565 | Moderate association from engineered E. coli; not direct proof of broad pH breadth |
| TCA cycle gene upregulation —positively associates with→ mild acid stress response | pathway → phenotype association | GO:0006099 tricarboxylic acid cycle | “the TCA cycle... highly positively associated with mild acid stress responses” (qin2024characterizationofmild pages 1-2) | 10.3390/microorganisms12081565, 2024, https://doi.org/10.3390/microorganisms12081565 | Moderate association only; curate as inferred/supporting edge |
| ABC transporter gene upregulation —positively associates with→ mild acid stress response | transporter family → phenotype association | GO:0043190 ATP-binding cassette (ABC) transporter complex | “genes involved in ATP-binding cassette (ABC) transporters... were highly positively associated with mild acid stress responses” (qin2024characterizationofmild pages 1-2) | 10.3390/microorganisms12081565, 2024, https://doi.org/10.3390/microorganisms12081565 | Moderate association; function likely heterogeneous across substrates |
| Presence of Na+/H+ antiporter gene families (e.g., MnhG, MrpF, PhaGF, YufB) —associates with→ higher pH preference | gene family → phenotype association | label-only MnhG; label-only MrpF; label-only PhaGF; label-only YufB | “Genes associated with higher pH preferences include Na+/H+ antiporters (PhaGF, MnhG, MrpF, YufB)” (ramoneda2023buildingagenomebased pages 3-5) | 10.1126/sciadv.adf8998, 2023, https://doi.org/10.1126/sciadv.adf8998 | Moderate genomic association; excellent candidate for evidence-weighted but not fully causal curation |
| Presence of Kdp K+ transporter genes (KdpACD) —associates with→ low pH preference | gene family → phenotype association | label-only KdpA/KdpC/KdpD | “Specific transporters... associated with low pH preference include Kdp K+ membrane transporters (KdpACD)” (ramoneda2023buildingagenomebased pages 3-5) | 10.1126/sciadv.adf8998, 2023, https://doi.org/10.1126/sciadv.adf8998 | Moderate genomic association; mechanistic direction to breadth remains inferred |
| Presence of urease-related genes (UreE_C / ureide permease) —associates with→ low pH preference | gene family → phenotype association | label-only UreE_C; label-only ureide permease | “ureide_permeases and urease (UreE_C)” associated with low pH preference (ramoneda2023buildingagenomebased pages 3-5) | 10.1126/sciadv.adf8998, 2023, https://doi.org/10.1126/sciadv.adf8998 | Moderate association; compatible with acid-acclimation mechanism from Krulwich |
| Presence/absence of 56 functional gene types —predicts→ bacterial pH preference | gene set → phenotype prediction | label-only 56-gene pH preference model | “Using... 56 gene types... cross-dataset average R2 ≈ 0.80; validation MAE = 0.63 pH units” (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2) | 10.1126/sciadv.adf8998, 2023, https://doi.org/10.1126/sciadv.adf8998 | Strong predictive evidence for phenotype association, but not a direct mechanistic edge for TraitMech |
| Synthetic acid-tolerance module (gadE + hdeB + sodB + katE) overexpression —improves→ growth at pH 6.0 | engineered gene module → phenotype | label-only gadE; label-only hdeB; label-only sodB; label-only katE | “final OD600... at pH 6.0 was 131% and 124% of parent” after overexpression of synthetic acid-tolerance genes (qin2024characterizationofmild pages 1-2) | 10.3390/microorganisms12081565, 2024, https://doi.org/10.3390/microorganisms12081565 | Strong experimental evidence, but engineered-strain specific; not native generalist trait edge |


*Table: This table compiles curation-ready candidate causal edges for the trait pH delta mid2, covering broad mechanisms for acid and alkaline tolerance as well as recent gene-phenotype associations. It is designed to help prioritize edges that are strong, generalizable, and suitable for TraitMech curation while flagging taxon-specific or association-only claims.*

## 8. Warnings / claims not yet ready for TraitMech curation
1. **Association-only gene sets (genome ↔ realized pH preference)**: Ramoneda et al. (2023) provides strong predictive association evidence, but not direct causality; edges should be labeled **“associated_with”** unless validated by knockouts/physiology. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 3-5)
2. **Engineered strain omics edges**: Qin et al. (2024) supports that overexpressing an acid-tolerance module improves growth at pH 6.0 and correlates with energy/transport upregulation, but generalizing to natural broad pH breadth requires caution. (qin2024characterizationofmild pages 1-2)
3. **Taxon-specific exemplars**: *H. pylori* urease/UreI recruitment and extreme alkaliphile ATP synthase motif adaptations are mechanistically strong but narrow in taxonomic scope. Curate with explicit **NCBITaxon constraints** if included. (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 12-14)

## 9. DOI-first bibliography (with publication dates and URLs)
1. **Krulwich TA, Sachs G, Padan E.** (May 2011). *Molecular aspects of bacterial pH sensing and homeostasis.* **Nature Reviews Microbiology** 9:330–343. DOI: **10.1038/nrmicro2549**. URL: https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 1-3)
2. **Ramoneda J, Stallard-Olivera E, Hoffert M, et al.** (Apr 2023). *Building a genome-based understanding of bacterial pH preferences.* **Science Advances** 9. DOI: **10.1126/sciadv.adf8998**. URL: https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 1-2)
3. **Rebelo A, Almeida A, Peixe L, Antunes P, Novais C.** (Sep 2023). *Unraveling the Role of Metals and Organic Acids in Bacterial Antimicrobial Resistance in the Food Chain.* **Antibiotics** 12:1474. DOI: **10.3390/antibiotics12091474**. URL: https://doi.org/10.3390/antibiotics12091474 (rebelo2023unravelingtherole pages 18-20)
4. **Jiang G, Wang C, Wang Y, et al.** (Jul 2024). *Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.* **Applied and Environmental Microbiology**. DOI: **10.1128/aem.00569-24**. URL: https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2)
5. **Qin J, Guo H, Wu X, et al.** (Jul 2024). *Characterization of Mild Acid Stress Response in an Engineered Acid-Tolerant Escherichia coli Strain.* **Microorganisms** 12:1565. DOI: **10.3390/microorganisms12081565**. URL: https://doi.org/10.3390/microorganisms12081565 (qin2024characterizationofmild pages 1-2)
6. **Li Z, Huang Z, Gu P.** (Aug 2024). *Response of Escherichia coli to Acid Stress: Mechanisms and Applications—A Narrative Review.* **Microorganisms** 12:1774. DOI: **10.3390/microorganisms12091774**. URL: https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 1-2)

## 10. Visual evidence used
Key mechanistic overview figures and tables summarizing pH homeostasis (antiporters, ATPases, urease buffering, alkaliphile strategies) were extracted from Krulwich et al. 2011 (Nature Reviews Microbiology). (krulwich2011molecularaspectsof media 623f3d23, krulwich2011molecularaspectsof media be673b8c, krulwich2011molecularaspectsof media affe59c9, krulwich2011molecularaspectsof media 033c4b0e, krulwich2011molecularaspectsof media 43489457, krulwich2011molecularaspectsof media 58111408)

References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

3. (rebelo2023unravelingtherole pages 18-20): Andreia Rebelo, Agostinho Almeida, Luísa Peixe, Patrícia Antunes, and Carla Novais. Unraveling the role of metals and organic acids in bacterial antimicrobial resistance in the food chain. Antibiotics, 12:1474, Sep 2023. URL: https://doi.org/10.3390/antibiotics12091474, doi:10.3390/antibiotics12091474. This article has 33 citations.

4. (li2024responseofescherichia pages 1-2): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

5. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 15-17): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

7. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

8. (ramoneda2023buildingagenomebased pages 6-7): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

9. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

10. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

11. (qin2024characterizationofmild pages 1-2): Jingliang Qin, Han Guo, Xiaoxue Wu, Shuai Ma, Xin Zhang, Xiaofeng Yang, Bin Liu, Lu Feng, Huanhuan Liu, and Di Huang. Characterization of mild acid stress response in an engineered acid-tolerant escherichia coli strain. Microorganisms, 12:1565, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081565, doi:10.3390/microorganisms12081565. This article has 2 citations.

12. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

13. (krulwich2011molecularaspectsof pages 11-12): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

14. (krulwich2011molecularaspectsof media 623f3d23): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

15. (krulwich2011molecularaspectsof media be673b8c): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

16. (krulwich2011molecularaspectsof media affe59c9): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

17. (krulwich2011molecularaspectsof media 033c4b0e): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

18. (krulwich2011molecularaspectsof media 43489457): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

19. (krulwich2011molecularaspectsof media 58111408): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.