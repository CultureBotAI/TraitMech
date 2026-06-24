---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:35:08.797476'
end_time: '2026-06-17T23:44:45.918402'
duration_seconds: 577.12
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: neutrophilic
  trait_identifier: METPO:1003001
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: neutrophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference characterized by optimal growth at near-neutral
    pH values, typically between pH 6.5 and 7.5.
  parent_traits: METPO:1003000
  synonyms: neutralophile, neutralophilic, neutrophile
  evidence_summary: 'DOI:10.1038/nrmicro2549: cytoplasmic pH ... must maintain for
    growth (Supports pH growth preference as tied to cytoplasmic pH requirements.)'
  causal_graph_summary: 'neutrophilic_neutral_ph_homeostasis: 5 nodes, 4 edges'
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
- **Trait label:** neutrophilic
- **METPO identifier:** METPO:1003001
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth at near-neutral pH values, typically between pH 6.5 and 7.5.
- **Parent traits:** METPO:1003000
- **Synonyms:** neutralophile, neutralophilic, neutrophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH ... must maintain for growth (Supports pH growth preference as tied to cytoplasmic pH requirements.)
- **Existing causal graph summary:** neutrophilic_neutral_ph_homeostasis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **neutrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/neutrophilic.yaml`.

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
- **Trait label:** neutrophilic
- **METPO identifier:** METPO:1003001
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth at near-neutral pH values, typically between pH 6.5 and 7.5.
- **Parent traits:** METPO:1003000
- **Synonyms:** neutralophile, neutralophilic, neutrophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH ... must maintain for growth (Supports pH growth preference as tied to cytoplasmic pH requirements.)
- **Existing causal graph summary:** neutrophilic_neutral_ph_homeostasis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **neutrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/neutrophilic.yaml`.

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


## Research report: Neutrophilic (neutralophile) microbial trait (METPO:1003001)

### 1) Scope summary (trait meaning, boundaries, and definitions)

**Trait intent.** The neutrophilic (neutralophile/neutralophilic) trait represents a **pH growth preference**: organisms whose growth is optimized around **near-neutral external pH** and whose physiology is tuned to maintain a **near-neutral cytoplasmic pH (pHi)** for enzyme function and macromolecular stability. A 2023 review summarizes a widely used quantitative characterization: **neutralophilic bacteria can grow at external pH ~5.5–9.0 while maintaining cytoplasmic pH ~7.2–7.8** (reported for *E. coli*) (rebelo2023unravelingtherole pages 18-20). This complements a broader bacterial-physiology perspective that **cytoplasmic pH is typically kept near ~7.0–7.5** across many cell types because pHi affects protein stability and function (terradot2024escherichiacolimaintains pages 1-2, poolman2023physicochemicalhomeostasisin pages 1-2).

**Boundary cases to curate explicitly.**
- **Preference vs tolerance:** “Neutrophilic” should be curated as **growth optimum/preference**, not merely survival. For example, recent literature separates **growth across moderate pH ranges** from **survival without growth at very low pH** (e.g., *E. coli* survival at very acidic pH) (li2024responseofescherichia pages 1-2). 
- **Distinguish from acidophilic/alkaliphilic traits:** acidophiles/alkaliphiles have growth optima at low/high pH, whereas neutralophiles typically maintain near-neutral pHi and experience low/high pH mainly as stressors (schumacher2023ribosomeprofilingreveals pages 1-2, rebelo2023unravelingtherole pages 18-20).
- **Assay dependence:** pH preference is often inferred from distribution across pH gradients; this may conflate preference with competitive fitness and habitat covariates. Genome-enabled prediction of pH preference is powerful but includes association-based uncertainty for causal curation (ramoneda2023buildingagenomebased pages 3-5).

### 2) Current mechanistic understanding (key concepts and definitions)

Neutralophilic growth depends on **pHi homeostasis** (near-neutral cytoplasmic pH) under variable external pH (pHe). Mechanistically, the dominant causal theme in recent syntheses and primary work is that **electrophysiology (PMF and membrane potential), buffering capacity, and proton-consuming/ion-transport reactions** jointly constrain the extracellular pH range compatible with growth.

**Core physiological definitions (nodes you can reuse across traits).**
- **Cytoplasmic pH (pHi):** maintained close to neutral for macromolecular function (terradot2024escherichiacolimaintains pages 1-2).
- **Proton motive force (PMF):** electrochemical gradient of protons combining membrane voltage (ψ) and ΔpH; central to energy transduction and pH regulation (terradot2024escherichiacolimaintains pages 1-2).
- **Acid resistance (AR) systems:** stress-response modules (often amino-acid decarboxylase + antiporter) that consume cytoplasmic H+ and export alkaline products (schumacher2023ribosomeprofilingreveals pages 1-2, rebelo2023unravelingtherole pages 18-20).

### 3) Candidate causal-graph entities (nodes) with ontology grounding suggestions

Below are curation-ready **candidate nodes** grouped by type. Where stable CURIEs are obvious and general, they are suggested; where taxon/gene IDs vary, nodes are provided as labels suitable for later grounding.

#### A. Environmental / experimental factors
- **External pH / acidic pH stress / alkaline pH stress** (label-only; can map to ENVO concepts if used in your stack).
- **Short-chain fatty acids / organic acids** (CHEBI candidates; organic acid stress context) (schumacher2023ribosomeprofilingreveals pages 1-2, rebelo2023unravelingtherole pages 18-20).

#### B. Cellular physicochemical states
- **Cytoplasmic pH homeostasis** (GO:0051453 “maintenance of intracellular pH”; candidate).
- **Proton motive force** (label; GO term may be represented via “proton motive force-driven transmembrane transport” etc.).
- **Membrane potential (ψ)** (label).

#### C. Processes and pathways
- **Cytoplasmic buffering capacity** (proton sequestration by proteins/phosphate/polyamines) (schumacher2023ribosomeprofilingreveals pages 1-2).
- **Amino-acid decarboxylation-based acid resistance** (process node; includes glutamate/arginine/lysine/ornithine systems) (schumacher2023ribosomeprofilingreveals pages 1-2, rebelo2023unravelingtherole pages 18-20).
- **Urease-mediated urea hydrolysis → ammonia production** (process node; ammonia as base) (ramoneda2023buildingagenomebased pages 3-5).
- **Active proton efflux / cation–proton antiport** (process node) (terradot2024escherichiacolimaintains pages 1-2, ramoneda2023buildingagenomebased pages 3-5).
- **Cell wall assembly/maintenance under acid stress** (process node; especially for Gram-positives) (beetham2024histidinetransportis pages 1-2).

#### D. Molecular functions / protein complexes / gene modules
- **F1F0-ATPase proton pump (ATP synthase running in reverse)** (complex/function node; proton pump role under acid stress) (rebelo2023unravelingtherole pages 18-20).
- **Proton-ion antiporters (H+/Na+ or H+/K+ antiport)** (family node; e.g., Nha/Mrp/Mnh-like) (terradot2024escherichiacolimaintains pages 1-2, ramoneda2023buildingagenomebased pages 3-5).
- **Acid resistance decarboxylases + antiporters** (gene-module nodes):
  - *E. coli* GadA/GadB (glutamate decarboxylase) + GadC antiporter (schumacher2023ribosomeprofilingreveals pages 1-2, rebelo2023unravelingtherole pages 18-20)
  - AdiA (arginine decarboxylase) + AdiC antiporter (schumacher2023ribosomeprofilingreveals pages 1-2, rebelo2023unravelingtherole pages 18-20)
  - CadA (lysine decarboxylase) + CadB antiporter (schumacher2023ribosomeprofilingreveals pages 1-2, rebelo2023unravelingtherole pages 18-20)
  - SpeF (ornithine decarboxylase) + PotE antiporter (schumacher2023ribosomeprofilingreveals pages 1-2)
- **Urease accessory/structural components (e.g., UreE-like)** as genomic markers (label; gene-level grounding is species-specific) (ramoneda2023buildingagenomebased pages 3-5).
- **Kdp potassium transport system (KdpACD)** (label; KEGG/UniProt grounding species-specific) (ramoneda2023buildingagenomebased pages 3-5).
- **Histidine transporter (SAUSA300_0846 in *S. aureus*)** (taxon-specific label) (beetham2024histidinetransportis pages 1-2).

#### E. Chemicals and metabolites
- **H+ (proton)** (CHEBI:15378 candidate).
- **Glutamate / GABA / CO2 / cadaverine / agmatine** (CHEBI candidates; use pathway-specific nodes) (rebelo2023unravelingtherole pages 18-20, poolman2023physicochemicalhomeostasisin pages 2-4).
- **Polyamines (e.g., putrescine)** (CHEBI candidate; stress-modulator node) (jiang2024exogenousputrescineplays pages 4-6, schumacher2023ribosomeprofilingreveals pages 1-2).
- **Ammonia (NH3/NH4+)** (CHEBI candidate; base production) (ramoneda2023buildingagenomebased pages 3-5).

### 4) Evidence-backed causal edges (triples) for TraitMech curation

The following table is designed for direct graph curation and includes snippets and strength notes.

| Edge (triple) | Mechanistic rationale | Evidence snippet (short quote) | Source (DOI, publication year, URL) | Strength/Scope |
|---|---|---|---|---|
| external acidic pH -> increases proton influx into cytoplasm | Low external pH increases H+ entry across/through the membrane, challenging neutral cytoplasmic pH homeostasis. | “at low pH, H+ can permeate into the cytoplasm via protonated water chains, ion channels, or damaged membranes” (schumacher2023ribosomeprofilingreveals pages 1-2) | Schumacher et al. 2023, DOI:10.1128/msystems.01037-23, https://doi.org/10.1128/msystems.01037-23 | General for neutralophilic bacteria; strong |
| cytoplasmic buffering capacity -> stabilizes intracellular pH | Proton sequestration by cytoplasmic buffers dampens pH fluctuations and protects enzyme function. | “protons can be sequestered by side-chains of proteins, inorganic phosphates, polyphosphates, or polyamines” (schumacher2023ribosomeprofilingreveals pages 1-2) | Schumacher et al. 2023, DOI:10.1128/msystems.01037-23, https://doi.org/10.1128/msystems.01037-23 | General for neutralophiles; strong |
| amino-acid decarboxylation -> consumes cytoplasmic protons | Decarboxylation directly removes H+ from the cytoplasm, raising internal pH. | “The decarboxylation of amino acids is an enzyme-catalyzed reaction that consumes protons” (rebelo2023unravelingtherole pages 18-20) | Rebelo et al. 2023, DOI:10.3390/antibiotics12091474, https://doi.org/10.3390/antibiotics12091474 | General/acid-tolerance in neutralophiles; strong |
| amino-acid decarboxylation + antiporter exchange -> generates proton motive force | Charge-differential substrate/product exchange plus proton consumption couples pH homeostasis to PMF generation. | “the chemistry of the decarboxylation reaction requires a proton, and thus the internal pH is increased” and “the equivalent of 1 proton is pumped per molecule decarboxylated” (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin media 9822aa51) | Poolman 2023, DOI:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033 | General mechanism; strong |
| GadA/GadB + GadC system -> increases intracellular and extracellular pH | Glutamate decarboxylation consumes H+ and GadC exchanges substrate/product, jointly alkalinizing cell and environment. | “Each AR system consists of an H+-consuming amino acid decarboxylase… and a corresponding antiporter… This strategy ensures a simultaneous increase in intracellular and extracellular pH” (schumacher2023ribosomeprofilingreveals pages 1-2) | Schumacher et al. 2023, DOI:10.1128/msystems.01037-23, https://doi.org/10.1128/msystems.01037-23 | Strong, but system characterized especially in E. coli and related taxa |
| protonated glutamate decarboxylation -> GABA export via GadC | Specific mechanistic edge for GDAR: substrate conversion plus antiport cycle drives acid resistance. | “conversion of protonated glutamate (Glu) to… GABA and carbon dioxide, followed by the export of GABA through the GadC antiporter” (rebelo2023unravelingtherole pages 18-20) | Rebelo et al. 2023, DOI:10.3390/antibiotics12091474, https://doi.org/10.3390/antibiotics12091474 | Strong; well supported, but pathway-specific |
| AdiA + AdiC system -> acid stress survival | Arginine decarboxylase plus arginine/agmatine antiport is a proton-consuming acid-resistance module. | “adiA—arginine decarboxylase and adiC—arginine–agmatine antiporter… important feature for neutralizing and surviving acid stress” (rebelo2023unravelingtherole pages 18-20) | Rebelo et al. 2023, DOI:10.3390/antibiotics12091474, https://doi.org/10.3390/antibiotics12091474 | Strong; taxon-enriched in enterics |
| CadA + CadB system -> acid stress survival | Lysine decarboxylation plus lysine/cadaverine antiport consumes protons and exports alkaline product. | “cadA—lysine decarboxylase and cadB—lysine–cadaverine antiporter… important feature for neutralizing and surviving acid stress” (rebelo2023unravelingtherole pages 18-20) | Rebelo et al. 2023, DOI:10.3390/antibiotics12091474, https://doi.org/10.3390/antibiotics12091474 | Strong; pathway-specific |
| proton pumps / F1F0-ATPase -> counteracts acid stress | ATP-dependent proton transport helps restore cytoplasmic pH under acid challenge. | “Common mechanisms involved in bacterial acid tolerance… include… the F1-F0-ATPase proton pump” (rebelo2023unravelingtherole pages 18-20) | Rebelo et al. 2023, DOI:10.3390/antibiotics12091474, https://doi.org/10.3390/antibiotics12091474 | General; strong but broad review statement |
| urease activity -> ammonia production -> counters acidity | Ammonia is a basic product that neutralizes acidity and supports low-pH preference/tolerance. | “cells will produce basic compounds, such as ammonia released from urea to counter acidity” and “a gene for urease… hydrolyzes urea into ammonia” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al. 2023, DOI:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | Strong for association; mechanistic but partly inferred from comparative genomics |
| ureide permeases / urease genes -> associated with low-pH preference | Genomic enrichment suggests urea import and hydrolysis are determinants of bacterial preference for lower pH environments. | “ureide_permeases overrepresented in taxa with low pH preference… as well as a gene for urease (UreE_C, soils)” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al. 2023, DOI:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | Comparative-genomic association; uncertain for direct curation as causal edge |
| central metabolism-driven proton efflux -> powers proton-ion antiporters | Metabolic proton export provides energy input used by antiporters to build/maintain PMF. | “Their principal function, powered by the central-metabolism-enabled proton efflux, is to generate the PMF by moving other ions” (terradot2024escherichiacolimaintains pages 1-2) | Terradot et al. 2024, DOI:10.1103/prxlife.2.043015, https://doi.org/10.1103/prxlife.2.043015 | Strong for E. coli/model-based plus experiment |
| proton-ion antiporters -> generate membrane potential and PMF | Antiporters move non-proton ions to establish electrical potential needed for near-neutral pHi maintenance. | “cells use antiporters to generate the plasma membrane potential and thus their PMF” (terradot2024escherichiacolimaintains pages 1-2) | Terradot et al. 2024, DOI:10.1103/prxlife.2.043015, https://doi.org/10.1103/prxlife.2.043015 | Strong in E. coli; likely broader but scope should be curated cautiously |
| PMF strength -> determines extracellular pH range permitting pH homeostasis | A sufficiently strong PMF sets the pHe range over which neutral cytoplasmic pH can be maintained. | “the strength of the PMF sets the maximal rate at which the antiporters work, and so determines the extracellular pH range for which the two homeostases hold” (terradot2024escherichiacolimaintains pages 1-2) | Terradot et al. 2024, DOI:10.1103/prxlife.2.043015, https://doi.org/10.1103/prxlife.2.043015 | Strong in E. coli; mechanistically important |
| decreased PMF -> impairs intracellular pH maintenance | Experimental perturbation shows PMF is causally required for maintaining near-neutral pHi. | “decreasing the PMF’s strength impairs the cells’ ability to maintain pH” (terradot2024escherichiacolimaintains pages 1-2) | Terradot et al. 2024, DOI:10.1103/prxlife.2.043015, https://doi.org/10.1103/prxlife.2.043015 | Strong in E. coli |
| zero/collapsed PMF -> loss of membrane potential | Membrane potential depends on intact PMF in this model system. | “artificially collapsing the PMF destroys the membrane potential” (terradot2024escherichiacolimaintains pages 1-2) | Terradot et al. 2024, DOI:10.1103/prxlife.2.043015, https://doi.org/10.1103/prxlife.2.043015 | Strong in E. coli |
| Na+/H+ antiporters (e.g., PhaGF/MnhG/MrpF/YufB) -> associated with higher-pH preference | Comparative genomics links cation/proton antiport with growth preference toward higher external pH. | “Na+/H+ antiporters [PhaGF, MnhG, MrpF, and YufB]… were overrepresented in taxa with preferences for higher pH” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al. 2023, DOI:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | Association, not direct experiment; uncertain for general neutrophilic edge |
| Kdp K+ transporters -> associated with low-pH preference | Potassium transport is repeatedly associated with low-pH adapted taxa, suggesting contribution to ionic/pH homeostasis. | “Kdp K+ membrane transporters (KdpACD)… were overrepresented in taxa with low pH preference” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al. 2023, DOI:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | Association only; uncertain |
| cell wall assembly/maintenance -> promotes growth under low pH | Cell wall properties are major determinants of survival/growth during acid stress, likely by limiting surface proton stress. | “Most hits encode cell wall assembly/maintenance functions, implicating cell wall charge/composition in acid survival” (beetham2024histidinetransportis pages 1-2) | Beetham et al. 2024, DOI:10.1371/journal.ppat.1011927, https://doi.org/10.1371/journal.ppat.1011927 | Strong but taxon-specific (S. aureus) |
| histidine transport -> supports cytosolic pH maintenance at low pH | Histidine uptake supports acid-stress physiology; loss of transporter reduces ability to maintain pHi. | “the mutant cannot maintain cytosolic pH as well as wild-type, linking histidine uptake to cytosolic pH homeostasis” (beetham2024histidinetransportis pages 1-2) | Beetham et al. 2024, DOI:10.1371/journal.ppat.1011927, https://doi.org/10.1371/journal.ppat.1011927 | Strong but taxon-specific (S. aureus) |
| exogenous putrescine -> promotes amino-acid metabolism under acidic conditions | Polyamine availability can reprogram metabolism toward improved acid-stress adaptation. | “exogenous putrescine promoted amino acids metabolism in the acid group” (jiang2024exogenousputrescineplays pages 4-6) | Jiang et al. 2024, DOI:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Community/biofilm context; uncertain for direct TraitMech core |
| exogenous putrescine + acidic pH -> increases biofilm biomass and intact cells | Putrescine can improve pH-stress adaptability in acidic biofilms, though this is an assay-specific community effect. | “under acid conditions, biofilm production increased by 102%” and “the proportion of intact cells increased by 125% under acidic conditions” (jiang2024exogenousputrescineplays pages 4-6) | Jiang et al. 2024, DOI:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Assay-specific, mixed-community biofilm; uncertain for core neutrophilic trait |
| neutralophilic bacteria -> maintain cytoplasmic pH ~7.2–7.8 while growing at external pH ~5.5–9.0 | Quantitative trait-defining edge linking the phenotype to near-neutral internal pH despite moderate external variation. | “neutralophilic bacteria can grow at external pH values between ~5.5–9.0, while maintaining a cytoplasmic pH between ~7.2–7.8” (rebelo2023unravelingtherole pages 18-20) | Rebelo et al. 2023, DOI:10.3390/antibiotics12091474, https://doi.org/10.3390/antibiotics12091474 | Trait-defining summary; strong but review-based |


*Table: This table compiles candidate subject–predicate–object edges for curating a causal graph of the neutrophilic microbial trait. It emphasizes mechanisms that maintain near-neutral cytoplasmic pH, while flagging which claims are broad, taxon-specific, or only association-based.*

**Mechanistic figure evidence (useful for curation decisions).** Poolman (2023) provides a schematic linking **substrate decarboxylation + antiporter exchange** to **PMF generation and pH homeostasis**, which supports several core edges above (poolman2023physicochemicalhomeostasisin media 9822aa51).

### 5) Recent developments (prioritizing 2023–2024)

#### 5.1 Genome-based inference of bacterial pH preference across environments (2023)
Ramoneda et al. compiled **five datasets spanning soil and freshwater pH gradients (1470 samples)**, inferred taxon pH preferences, and identified gene families consistently associated with inferred pH preference across datasets, then used these to build predictive models (ramoneda2023buildingagenomebased pages 3-5). They explicitly organize pH-adaptation mechanisms into **four main mechanisms**—(i) proton-consuming reactions, (ii) base production (e.g., ammonia), (iii) active proton efflux, and (iv) membrane/protein maturation changes—and show that genes linked to these functions are associated with pH preference in real communities (ramoneda2023buildingagenomebased pages 3-5).

Curation relevance: this paper is excellent for **candidate node discovery** (e.g., antiporters, urease, Kdp) but many statements are **association-based** (genomic enrichment vs direct perturbation) and should be curated with an “uncertain/association” flag unless supported by experimental genetics/physiology (ramoneda2023buildingagenomebased pages 3-5).

#### 5.2 Systems-level translation + transcription under acid stress in a model neutralophile (2023)
Schumacher et al. used **RNA-seq and ribosome profiling** to compare *E. coli* responses at control pH 7.6 versus mild acid (pH 5.8) and severe acid (pH 4.4), identifying **new genes/pathways and 18 candidate small ORFs** induced by acid stress and highlighting heterogeneity and regulatory complexity of AR networks (schumacher2023ribosomeprofilingreveals pages 1-2). The paper provides quantitative pH-shift framing (pH 7.6 → 5.8/4.4) and mechanistic definitions of AR systems as decarboxylase + antiporter modules that increase intracellular and extracellular pH (schumacher2023ribosomeprofilingreveals pages 1-2).

Curation relevance: supports mechanistic edges for **buffering**, **acid-induced proton influx**, and **decarboxylase/antiporter acid resistance modules** in a canonical neutralophile (schumacher2023ribosomeprofilingreveals pages 1-2).

#### 5.3 Electrophysiology reframing: membrane potential and PMF constrain pHi maintenance (2024)
Terradot et al. propose and test a quantitative electrophysiology model in which **central metabolism exports protons**, and **proton-ion antiporters—powered by this proton efflux—generate membrane potential and thus the PMF**, with the **PMF strength determining the extracellular pH range for which pHi homeostasis holds** (terradot2024escherichiacolimaintains pages 1-2). They report experimental support that **decreasing PMF impairs pH maintenance** and that collapsing PMF eliminates membrane potential (terradot2024escherichiacolimaintains pages 1-2).

Curation relevance: provides a causal backbone connecting **metabolism → proton efflux → antiporters → membrane potential/PMF → pHi homeostasis range**, appropriate for a neutralophile trait mechanism graph (terradot2024escherichiacolimaintains pages 1-2).

#### 5.4 New gene-to-phenotype link: histidine transport and pHi maintenance in a pathogen (2024)
Beetham et al. used genome-wide Tn-seq in *Staphylococcus aureus* and found **31 genes essential for growth at pH 4.5**, with many related to **cell wall assembly/maintenance**, and identified a **histidine transporter (SAUSA300_0846)** whose loss reduces the ability to maintain cytosolic pH compared with wild type (beetham2024histidinetransportis pages 1-2).

Curation relevance: highlights that in some taxa, **cell envelope physiology and amino acid transport** can be essential for growth under acidic conditions. This is valuable but should be curated as **taxon-specific** (Gram-positive pathogen; extreme pH assay) rather than a universal neutralophile mechanism (beetham2024histidinetransportis pages 1-2).

### 6) Current applications and real-world implementations (with recent data)

#### 6.1 Wastewater/activated sludge biofilms: polyamine modulation of pH-stress adaptation (2024)
Jiang et al. report that exogenous putrescine has a **pH-dependent “switch-like” effect** on activated-sludge biofilm formation: under **acid conditions**, biofilm production increased **by 102%**, while under **alkali conditions** it decreased **by 37%** (static cultivation); they also report that putrescine increased the **proportion of intact cells by 125% under acidic conditions** and decreased intact cells by **36% under alkali conditions** (jiang2024exogenousputrescineplays pages 4-6). These data illustrate an engineering-relevant lever (polyamine addition) that interacts with pH stress adaptation and community composition.

Curation note: These are **mixed-community biofilm phenotypes** and should be treated as **assay-/ecosystem-specific** edges (e.g., putrescine → biofilm biomass under acidic pH) rather than core trait-defining edges for neutrophily (jiang2024exogenousputrescineplays pages 4-6).

#### 6.2 Food-chain and processing: acid stress mechanisms intersect with preservative acids and AMR (2023)
A 2023 review frames neutralophiles as frequently challenged by acidic environments in hosts and food-processing contexts and catalogs canonical acid-resistance strategies (decarboxylation systems; F1F0-ATPase; alkali production), which are directly relevant to managing growth of neutralophilic pathogens/commensals in acidic foods or disinfectant settings (rebelo2023unravelingtherole pages 18-20).

#### 6.3 Cultivation strategy and inoculant design: genome-to-trait prediction (2023)
Ramoneda et al. emphasize that predicting pH preference from genomes can guide **species distribution models, inoculant selection, and cultivation strategies**, addressing a practical bottleneck: many taxa have unknown pH preferences (ramoneda2023buildingagenomebased pages 3-5).

### 7) Statistics and quantitative data points suitable for curation

- **Neutralophile quantitative trait window:** external pH growth **~5.5–9.0** with maintained cytoplasmic pH **~7.2–7.8** (reported for *E. coli*) (rebelo2023unravelingtherole pages 18-20).
- **Stress assay pH values in a neutralophile model:** control pH **7.6**, mild acid **5.8**, severe acid **4.4**; example transient internal pH drop to **~6.0** when external pH is reduced to **5.5** (schumacher2023ribosomeprofilingreveals pages 1-2).
- **Environmental-scale dataset size for pH preference inference:** **1470 samples** across soil/freshwater pH gradients used to infer pH preferences and gene associations (ramoneda2023buildingagenomebased pages 3-5).
- **Wastewater biofilm engineering effect sizes:** putrescine increased biofilm production **102%** in acid and decreased **37%** in alkali; intact-cell proportion **+125% (acid)** and **−36% (alkali)** (jiang2024exogenousputrescineplays pages 4-6).

### 8) Expert synthesis (authoritative interpretations that can guide curation)

- Poolman (2023) emphasizes that **decarboxylation + antiport** can be an energy-coupled pH-homeostasis mechanism: decarboxylation consumes a proton and, with antiport exchange, contributes to **PMF generation** and pH regulation (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin media 9822aa51).
- Terradot et al. (2024) provide a recent “electrophysiology-first” viewpoint: **antiporters may primarily serve to generate membrane potential/PMF**, with direct pHi regulation constrained by that role; this helps structure causal graphs around PMF as a central mediator (terradot2024escherichiacolimaintains pages 1-2).
- Schumacher et al. (2023) position acid-response capacity as crucial for neutralophilic bacteria and formalize AR modules as decarboxylase+antiporter systems that increase intra/extracellular pH (schumacher2023ribosomeprofilingreveals pages 1-2).

### 9) Warnings / claims not ready for strong TraitMech curation

1. **Association vs causation (genome-enrichment):** edges such as “Na+/H+ antiporters → higher-pH preference” or “Kdp → low-pH preference” derived from cross-environment genomic overrepresentation should be curated as **uncertain/inferred**, unless supplemented by perturbation experiments in the target taxon (ramoneda2023buildingagenomebased pages 3-5).
2. **Acid resistance vs neutrophilic preference:** many mechanistic studies focus on **acid stress survival/growth at low pH**, which is adjacent to (but not identical with) a **near-neutral growth optimum** trait. When curating, keep the causal chain anchored to maintaining near-neutral pHi and growth near neutral pHe, using acid/alkali systems as mechanisms enabling **robustness around neutral preference** (schumacher2023ribosomeprofilingreveals pages 1-2, rebelo2023unravelingtherole pages 18-20).
3. **Community/engineering interventions:** putrescine effects in activated sludge biofilms are valuable for applications but likely reflect a mixture of community shifts, biofilm matrix changes, and cell physiology; treat as **context-specific** (jiang2024exogenousputrescineplays pages 4-6).
4. **Taxon-specific cell wall and amino acid transport claims:** the *S. aureus* low-pH essentiality of cell wall genes and histidine transport is a strong recent result but should be curated as **Gram-positive/pathogen/extreme pH assay-specific** unless corroborated across taxa (beetham2024histidinetransportis pages 1-2).

---

## DOI-first bibliography (with publication dates and URLs)

1. Rebelo A, Almeida A, Peixe L, Antunes P, Novais C. **Unraveling the Role of Metals and Organic Acids in Bacterial Antimicrobial Resistance in the Food Chain.** *Antibiotics* **2023-09**. DOI: **10.3390/antibiotics12091474**. URL: https://doi.org/10.3390/antibiotics12091474 (rebelo2023unravelingtherole pages 18-20)
2. Poolman B. **Physicochemical homeostasis in bacteria.** *FEMS Microbiology Reviews* **2023-06**. DOI: **10.1093/femsre/fuad033**. URL: https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin pages 1-2, poolman2023physicochemicalhomeostasisin media 9822aa51)
3. Ramoneda J, Stallard-Olivera E, Hoffert M, et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances* **2023-04-28**. DOI: **10.1126/sciadv.adf8998**. URL: https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5)
4. Schumacher K, Gelhausen R, Kion-Crosby W, et al. **Ribosome profiling reveals the fine-tuned response of *Escherichia coli* to mild and severe acid stress.** *mSystems* **2023-11-01**. DOI: **10.1128/msystems.01037-23**. URL: https://doi.org/10.1128/msystems.01037-23 (schumacher2023ribosomeprofilingreveals pages 1-2)
5. Terradot G, Krasnopeeva E, Swain PS, Pilizota T. **Escherichia coli Maintains pH via the Membrane Potential.** *PRX Life* **2024-11-27**. DOI: **10.1103/prxlife.2.043015**. URL: https://doi.org/10.1103/prxlife.2.043015 (terradot2024escherichiacolimaintains pages 1-2)
6. Beetham CM, Schuster CF, Kviatkovski I, et al. **Histidine transport is essential for the growth of *Staphylococcus aureus* at low pH.** *PLOS Pathogens* **2024-01**. DOI: **10.1371/journal.ppat.1011927**. URL: https://doi.org/10.1371/journal.ppat.1011927 (beetham2024histidinetransportis pages 1-2)
7. Jiang G, Wang C, Wang Y, et al. **Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.** *Applied and Environmental Microbiology* **2024-07**. DOI: **10.1128/aem.00569-24**. URL: https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 4-6)
8. Li Z, Huang Z, Gu P. **Response of *Escherichia coli* to Acid Stress: Mechanisms and Applications—A Narrative Review.** *Microorganisms* **2024-08**. DOI: **10.3390/microorganisms12091774**. URL: https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 1-2)


References

1. (rebelo2023unravelingtherole pages 18-20): Andreia Rebelo, Agostinho Almeida, Luísa Peixe, Patrícia Antunes, and Carla Novais. Unraveling the role of metals and organic acids in bacterial antimicrobial resistance in the food chain. Antibiotics, 12:1474, Sep 2023. URL: https://doi.org/10.3390/antibiotics12091474, doi:10.3390/antibiotics12091474. This article has 33 citations.

2. (terradot2024escherichiacolimaintains pages 1-2): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 9 citations.

3. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

4. (li2024responseofescherichia pages 1-2): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

5. (schumacher2023ribosomeprofilingreveals pages 1-2): Kilian Schumacher, Rick Gelhausen, Willow Kion-Crosby, Lars Barquist, Rolf Backofen, and Kirsten Jung. Ribosome profiling reveals the fine-tuned response of <i>escherichia coli</i> to mild and severe acid stress. Dec 2023. URL: https://doi.org/10.1128/msystems.01037-23, doi:10.1128/msystems.01037-23. This article has 20 citations and is from a peer-reviewed journal.

6. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

7. (beetham2024histidinetransportis pages 1-2): Catrin M. Beetham, Christopher F. Schuster, Igor Kviatkovski, Marina Santiago, Suzanne Walker, and Angelika Gründling. Histidine transport is essential for the growth of staphylococcus aureus at low ph. PLOS Pathogens, 20:e1011927, Jan 2024. URL: https://doi.org/10.1371/journal.ppat.1011927, doi:10.1371/journal.ppat.1011927. This article has 28 citations and is from a highest quality peer-reviewed journal.

8. (poolman2023physicochemicalhomeostasisin pages 2-4): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

9. (jiang2024exogenousputrescineplays pages 4-6): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

10. (poolman2023physicochemicalhomeostasisin media 9822aa51): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.