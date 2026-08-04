---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:05:38.481826'
end_time: '2026-08-04T11:20:11.470259'
duration_seconds: 872.99
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dormancy
  trait_identifier: traitmech:000080
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: dormancy
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A reversible physiological state of greatly reduced metabolic activity
    that allows a cell to survive unfavorable conditions and later resuscitate, generating
    a microbial seed bank.
  parent_traits: METPO:1000059
  synonyms: dormant state
  evidence_summary: 'DOI:10.1038/nrmicro2504:  (Lennon & Jones review microbial seed
    banks and the mechanisms by which microorganisms enter and exit dormancy; parent
    of VBNC and persister sub-variants.) | DOI:10.1038/nrmicro1557:  (Lewis links
    dormancy to persister-cell survival and infectious disease.)'
  causal_graph_summary: 'dormancy_seed_bank: 10 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 74
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dormancy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000080
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A reversible physiological state of greatly reduced metabolic activity that allows a cell to survive unfavorable conditions and later resuscitate, generating a microbial seed bank.
- **Parent traits:** METPO:1000059
- **Synonyms:** dormant state
- **Existing evidence:** DOI:10.1038/nrmicro2504:  (Lennon & Jones review microbial seed banks and the mechanisms by which microorganisms enter and exit dormancy; parent of VBNC and persister sub-variants.) | DOI:10.1038/nrmicro1557:  (Lewis links dormancy to persister-cell survival and infectious disease.)
- **Existing causal graph summary:** dormancy_seed_bank: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **dormancy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/dormancy.yaml`.

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
- **Trait label:** dormancy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000080
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A reversible physiological state of greatly reduced metabolic activity that allows a cell to survive unfavorable conditions and later resuscitate, generating a microbial seed bank.
- **Parent traits:** METPO:1000059
- **Synonyms:** dormant state
- **Existing evidence:** DOI:10.1038/nrmicro2504:  (Lennon & Jones review microbial seed banks and the mechanisms by which microorganisms enter and exit dormancy; parent of VBNC and persister sub-variants.) | DOI:10.1038/nrmicro1557:  (Lewis links dormancy to persister-cell survival and infectious disease.)
- **Existing causal graph summary:** dormancy_seed_bank: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **dormancy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/dormancy.yaml`.

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


# Microbial Trait Causal Graph Research Report: Dormancy (traitmech:000080)

## Executive Summary

This report delivers source-backed mechanistic entities and causal edges for curation into `data/traits/physiology/dormancy.yaml`. Dormancy is defined as "a reversible physiological state of greatly reduced metabolic activity that allows a cell to survive unfavorable conditions and later resuscitate, generating a microbial seed bank" (carvalho2024aquaticenvironmentdrives pages 1-2). Recent 2024 primary studies reveal quantitative mechanistic detail across induction, maintenance, and resuscitation phases, with taxon-specific regulatory genes, metabolic pathways, and timescales now resolved (carvalho2024aquaticenvironmentdrives pages 1-2, blattman2024identificationandgenetic pages 1-2, yang2024resuscitationofviable pages 1-2, imminger2024survivalandrapid pages 1-2, gou2024viablebutnonculturable pages 1-2).

---

## 1. Trait Scope Summary

Dormancy is an umbrella trait representing reversible, low-metabolic/non-growing physiological states across diverse bacteria (keep2006bacterialresuscitationfactors pages 1-2, sexton2020rolesoflysm pages 1-2, dhaouadi2024persistenceandculturability pages 1-2). It encompasses overlapping but operationally distinct subtypes:

- **Viable but nonculturable (VBNC)**: Cells retain viability and metabolic activity but cannot form colonies on standard media; resuscitation may require specific media or conditions (carvalho2024aquaticenvironmentdrives pages 1-2, yang2024resuscitationofviable pages 1-2, gou2024viablebutnonculturable pages 1-2).
- **Persisters**: Rare dormant variants exhibiting antibiotic tolerance; can regrow on original medium once stress is removed (blattman2024identificationandgenetic pages 1-2, blattman2024identificationandgenetic pages 3-4, dhaouadi2024persistenceandculturability pages 1-2).
- **Endospores** (Bacillus, Clostridium): Highly resistant, specialized dormant structures with distinct morphogenesis pathways (not covered in depth here; dormancy broadly includes non-spore-forming taxa).
- **Stationary-phase cells**: Growth-arrested but metabolically active; partially overlap with above categories but not always reversible via simple nutrient addition.

**Boundary cases:**

- **Exclude**: Irreversible death, genetic antibiotic resistance, and continuous slow growth without demonstrated reversible arrest.
- **Caution**: The 2024 literature explicitly distinguishes VBNC from persisters on the basis of culturability: "Persister cells can regrow after the stressor is removed. In contrast, VBNCs have lost culturability in the original medium that they are formed in but can be resuscitated in a different medium" (dhaouadi2024persistenceandculturability pages 1-2). Do not equate these without experimental confirmation of both viability and culturability/resuscitation criteria.
- **Practical overlap**: Many dormant cells exhibit both low culturability and antibiotic tolerance, and "there is a continuum between active cells and cell death, with VBNCs being at a deeper state of dormancy than persister cells" (dhaouadi2024persistenceandculturability pages 1-2).

---

## 2. Candidate Causal Graph Entities (Grouped by Type)

### Regulatory Genes, Proteins, Enzymes, Transporters, and Complexes

- **SigB** (*Listeria monocytogenes*): Stress-response transcription factor acting as a "major actor of VBNC state transition" (carvalho2024aquaticenvironmentdrives pages 1-2). Suggested CURIE: **GO:0006950** (response to stress) or genus-specific annotation.
- **NamA** (*L. monocytogenes*): Autolysin enzyme; "major actor of VBNC state transition" (carvalho2024aquaticenvironmentdrives pages 1-2).
- **HipA** (*Escherichia coli*): Toxin kinase; overexpression induces high-level persistence and reduced culturability (dhaouadi2024persistenceandculturability pages 1-2). CURIE: UniProt P23874 (*E. coli* K-12).
- **Lon protease** (*E. coli*): Highly conserved ATP-dependent protease; identified as "critical gene with large effects" on persister formation via genome-wide CRISPRi (blattman2024identificationandgenetic pages 1-2). CURIE: UniProt P0A9M0 (*E. coli* K-12).
- **YqgE** (*E. coli*): Poorly characterized protein; "strongly modulates the duration of post-starvation dormancy and persistence" (blattman2024identificationandgenetic pages 1-2). CURIE: UniProt P67603 (*E. coli* K-12).
- **RfaL (O-antigen ligase)** (*E. coli* O157:H7): Deletion shortens VBNC resuscitation lag phase by freeing ATP for NAD+ synthesis (yang2024resuscitationofviable pages 1-2). CURIE: EC 2.4.1.- (glycosyltransferase family).
- **Rpf (resuscitation-promoting factor) family**: Secreted peptidoglycan-cleaving enzymes with lysozyme-like fold; reactivate dormant *Micrococcus luteus*, *Mycobacterium tuberculosis*, *Streptomyces* spores at picomolar concentrations (keep2006bacterialresuscitationfactors pages 1-2, li2024resuscitationpromotionfactor pages 1-3, sexton2020rolesoflysm pages 1-2). CURIE: **GO:0008933** (lytic transglycosylase activity) or Pfam PF06737 (Rpf domain). Includes accessory LysM (peptidoglycan-binding, Pfam PF01476) and LytM (peptidase, Pfam PF01551) domains enhancing activity 65–70% (sexton2020rolesoflysm pages 1-2).
- **(p)ppGpp synthases/hydrolases**: Stringent-response alarmone regulators (background from additional searches; not extracted in detail from 2024 primary data).

### Chemicals, Electron Donors/Acceptors, Nutrients, Metabolites, Inhibitors

- **ATP (adenosine triphosphate)**: Residual ATP in VBNC cells marks viability; ATP depletion accompanies dormancy entry; ATP consumption during lag phase promotes NAD+ synthesis and resuscitation (yang2024resuscitationofviable pages 1-2, carvalho2024aquaticenvironmentdrives pages 2-3, yang2024resuscitationofviable pages 2-4). CURIE: **CHEBI:15422**.
- **NAD+ (nicotinamide adenine dinucleotide, oxidized)**: Synthesized via Handler and salvage pathways during VBNC resuscitation; balances redox reactions and recovers energy production (yang2024resuscitationofviable pages 1-2). CURIE: **CHEBI:57540**.
- **Peptidoglycan fragments (muropeptides)**: Cleavage products of Rpf and other autolysins; may function as signaling molecules for resuscitation in some systems (debated; stronger evidence for structural remodeling) (keep2006bacterialresuscitationfactors pages 1-2, sexton2020rolesoflysm pages 10-11, sexton2020rolesoflysm pages 1-2). CURIE: **CHEBI:8005** (peptidoglycan).
- **Oxygen limitation/hypoxia**: Induces stress responses, growth arrest, and dormancy-like states in biofilms and mycobacteria (referenced in background context; not extracted in full mechanistic detail from 2024 primary data).
- **Starvation / nutrient limitation**: Core environmental trigger for dormancy entry (carvalho2024aquaticenvironmentdrives pages 1-2, blattman2024identificationandgenetic pages 3-4, imminger2024survivalandrapid pages 1-2).

### Environmental Factors and Experimental Factors

- **Mineral water incubation** (*L. monocytogenes*): Oligotrophic starvation inducer; "bacteria starved in mineral water become VBNC" (carvalho2024aquaticenvironmentdrives pages 1-2, carvalho2024aquaticenvironmentdrives pages 2-3). CURIE: **ENVO:00002006** (water).
- **Low-grade fever temperature (38.8°C)**: Induces VBNC state in *Bartonella henselae* after 19 days (gou2024viablebutnonculturable pages 1-2). CURIE: **PATO:0000146** (temperature).
- **Antibiotic exposure**: Induces VBNC in *B. henselae* within 4 days, particularly bactericidal agents (gou2024viablebutnonculturable pages 1-2); induces persistence in *E. coli* (blattman2024identificationandgenetic pages 1-2, dhaouadi2024persistenceandculturability pages 1-2). CURIE: **CHEBI:33281** (antibacterial agent).
- **High-pressure CO2 (HPCD)**: Experimental inducer for *E. coli* O157:H7 VBNC (yang2024resuscitationofviable pages 1-2, yang2024resuscitationofviable pages 2-4).
- **Desiccation / drought**: Triggers dormancy in desert biocrust microbes (imminger2024survivalandrapid pages 1-2, imminger2024survivalandrapid pages 2-3).
- **Rewetting / simulated rain**: Rapid resuscitation trigger; "nearly all microbial populations resuscitate within minutes" in desert biocrust (imminger2024survivalandrapid pages 1-2, imminger2024survivalandrapid pages 3-4). CURIE: **ENVO:00002042** (precipitation).

### Cellular Localizations, Molecular Functions, Biological Processes

- **Peptidoglycan cell wall**: Target of Rpf lytic transglycosylases; progressive depletion during *L. monocytogenes* VBNC transition (carvalho2024aquaticenvironmentdrives pages 3-4, carvalho2024aquaticenvironmentdrives pages 2-3, sexton2020rolesoflysm pages 1-2). CURIE: **GO:0009274** (peptidoglycan-based cell wall).
- **Plasma membrane rigidification**: Membrane fluidity decreases prior to cell-wall loss in *L. monocytogenes* VBNC cells, measured by laurdan generalized polarization and Nile red TIR-FCS (carvalho2024aquaticenvironmentdrives pages 3-4). CURIE: **GO:0016020** (membrane) + **PATO:0001546** (quality of rigidity).
- **Translational deficiency**: "Dominant signature" of persister cells across genetic and physiological models; tetracycline-induced translation inhibition phenocopies persister transcriptome (blattman2024identificationandgenetic pages 1-2, blattman2024identificationandgenetic pages 3-4). CURIE: **GO:0006412** (translation) + negative regulation.
- **DNA repair (double-strand break repair)**: Upregulated in early resuscitation phase (first 15–30 min) in desert biocrust populations (imminger2024survivalandrapid pages 3-4). CURIE: **GO:0006302** (double-strand break repair).
- **Aerobic respiration (terminal oxidases)**: Cytochrome *c* and cytochrome *bd* upregulated early in resuscitation (imminger2024survivalandrapid pages 3-4). CURIE: **GO:0015002** (cytochrome-*c* oxidase activity), **GO:0009055** (cytochrome *bd* complex).

### Pathways and Metabolic Modules

- **Handler pathway** (Hanson pathway, also known as Preiss-Handler pathway): NAD+ biosynthesis from nicotinic acid; activated by ATP during *E. coli* O157:H7 VBNC resuscitation (yang2024resuscitationofviable pages 1-2). CURIE: **GO:0009435** (NAD biosynthetic process via nicotinate).
- **Salvage pathway**: NAD+ biosynthesis from nicotinamide or nicotinamide riboside; also ATP-activated during resuscitation (yang2024resuscitationofviable pages 1-2). CURIE: **GO:0034356** (NAD biosynthesis via salvage pathway).
- **LPS (lipopolysaccharide) biosynthesis pathway**: Inhibition in *ΔrfaL* mutant frees ATP for NAD+ synthesis, promoting resuscitation (yang2024resuscitationofviable pages 1-2, yang2024resuscitationofviable pages 2-4). CURIE: **GO:0009103** (lipopolysaccharide biosynthetic process).
- **Stringent response**: (p)ppGpp-mediated downregulation of ribosomal components and growth-related functions; background in multiple references but detailed mechanistic 2024 extraction pending further reading.

---

## 3. Evidence-Backed Causal Edges

The following artifact summarizes source-backed subject→predicate→object triples organized by induction, maintenance, and resuscitation phases. All edges include DOI-first references, supporting snippets, taxon/assay context, and uncertainty notes.

| Phase | Subject (entity causing change) | Predicate | Object (entity being changed) | Reference (DOI first) | Evidence Snippet | Taxon/Assay Specificity | Uncertainty/Notes |
|---|---|---|---|---|---|---|---|
| Induction | Starvation in mineral water | induces transition to | VBNC state | 10.1038/s41467-024-52633-7 (2024) | “We show that bacteria starved in mineral water become VBNC” (carvalho2024aquaticenvironmentdrives pages 1-2) | *Listeria monocytogenes*; mineral-water starvation, CFU + flow cytometry | Strong, direct primary evidence; taxon-specific VBNC subtype |
| Induction | Mineral water incubation | triggers | rod-to-coccus morphological transition | 10.1038/s41467-024-52633-7 (2024) | “incubation in mineral water triggers a rod-to-coccus transition in Lm cells” (carvalho2024aquaticenvironmentdrives pages 1-2, carvalho2024aquaticenvironmentdrives pages 2-3) | *L. monocytogenes*; phase contrast microscopy | Strong, direct morphology edge; species-specific |
| Induction | Mineral water starvation | causes | cell wall-deficient coccoid forms | 10.1038/s41467-024-52633-7 (2024) | “become VBNC by converting into osmotically stable cell wall-deficient coccoid forms” (carvalho2024aquaticenvironmentdrives pages 1-2) | *L. monocytogenes*; fluorescence microscopy, cryo-ET, muropeptides | Strong, direct |
| Induction | Reduced starting cell concentration in mineral water | increases rate/magnitude of | culturability loss | 10.1038/s41467-024-52633-7 (2024) | “the rate and magnitude of culturability loss increased when the starting bacterial concentration was reduced” (carvalho2024aquaticenvironmentdrives pages 2-3) | *L. monocytogenes*; CFU over 28 d | Experimental-condition edge; likely assay-specific |
| Induction | Exposure to 38.8°C (low-grade fever temperature) | induces | VBNC state | 10.3389/fcimb.2024.1486426 (2024) | “B. henselae cells entered a VBNC state after 19 days of exposure to 38.8°C” (gou2024viablebutnonculturable pages 1-2) | *Bartonella henselae*; CFU, SYBR Green I/PI, PMA-qPCR, resuscitation assay | Strong, direct; species-specific |
| Induction | Antibiotic treatment | induces | VBNC state | 10.3389/fcimb.2024.1486426 (2024) | “Antibiotics, particularly with bactericidal activity, induced the VBNC state within 4 days treatment” (gou2024viablebutnonculturable pages 1-2) | *B. henselae*; antibiotic exposure with resuscitation confirmation | Strong, direct; antibiotic class details not all extracted here |
| Induction | High-pressure CO2 (HPCD) | induces | VBNC state | 10.1016/j.jare.2023.08.002 (2024) | “high-pressure carbon dioxide (HPCD) induced E. coli O157:H7 cells to enter the VBNC state” (yang2024resuscitationofviable pages 1-2) | *Escherichia coli* O157:H7; HPCD induction, plate counts/flow cytometry | Strong for this experimental inducer; less general ecological relevance |
| Induction | Desiccation/drought | necessitates survival via | dormancy/persistence | 10.1038/s41467-024-46920-6 (2024) | “Long-term persistence, facilitated by dormancy, is critical in order for desert microorganisms to survive extended droughts” (imminger2024survivalandrapid pages 1-2) | Negev desert biocrust community; field-derived simulated rain study | Ecological statement supported by community data; mechanism broad rather than single-gene |
| Maintenance | SigB (stress-response regulator) | acts in | VBNC state transition | 10.1038/s41467-024-52633-7 (2024) | “We reveal the bacterial stress response regulator SigB … as major actors of VBNC state transition” (carvalho2024aquaticenvironmentdrives pages 1-2) | *L. monocytogenes*; genetic/mechanistic study | Strong but snippet is summary-level; exact mutant effect sizes not extracted here |
| Maintenance | NamA (autolysin) | acts in | VBNC state transition | 10.1038/s41467-024-52633-7 (2024) | “We reveal … the autolysin NamA as major actors of VBNC state transition” (carvalho2024aquaticenvironmentdrives pages 1-2) | *L. monocytogenes*; genetic/mechanistic study | Strong but summary-level snippet; curate with species specificity |
| Maintenance | Cell wall loss (molting-like shedding) | generates | wall-less coccoid VBNC forms | 10.1038/s41467-024-52633-7 (2024) | “lose their CW through a molting-like shedding process that generates wall-less coccoid cell forms” (carvalho2024aquaticenvironmentdrives pages 3-4) | *L. monocytogenes*; cryo-ET, fluorescence microscopy, muropeptide analysis | Strong, direct structural mechanism |
| Maintenance | Progressive CW depletion | accompanies/supports | transition to VBNC state | 10.1038/s41467-024-52633-7 (2024) | “confirm the progressive depletion of the Lm CW during transition to a VBNC state” (carvalho2024aquaticenvironmentdrives pages 2-3) | *L. monocytogenes*; UHPLC muropeptides | Strong, direct |
| Maintenance | Membrane rigidification | precedes/accompanies | CW loss / wall-less lifestyle adaptation | 10.1038/s41467-024-52633-7 (2024) | “an increase of the laurdan GP … was suggestive of decreased membrane fluidity” and “the reduction in membrane fluidity occurs prior to CW loss” (carvalho2024aquaticenvironmentdrives pages 3-4) | *L. monocytogenes*; laurdan GP, TIR-FCS, fatty-acid profiling | Strong, direct but organism-specific |
| Maintenance | Residual ATP in dormant cells | indicates | viability with reduced metabolism | 10.1038/s41467-024-52633-7 (2024) | “In cases of bacterial dormancy, such as persister or VBNC cells, a reduced metabolic state is associated with a residual ATP content” (carvalho2024aquaticenvironmentdrives pages 2-3) | *L. monocytogenes* context; luciferase ATP assay | Mixed: mechanistic statement partly general, evidence measured in Listeria |
| Maintenance | ATP depletion | is associated with | VBNC entry/dormancy depth | 10.1016/j.jare.2023.08.002 (2024) | “VBNC state formation is always accompanied by a decrease in intracellular ATP levels” (yang2024resuscitationofviable pages 2-4) | Review/introduction synthesized around *E. coli* O157:H7 work | Broad claim; treat as review-supported, not single direct experiment |
| Maintenance | Translational deficiency | defines | persister state | 10.1038/s41586-024-08124-2 (2024) | “persisters … converge to transcriptional states … [with] a dominant signature of translational deficiency” (blattman2024identificationandgenetic pages 1-2) | *E. coli* single-cell RNA-seq (PETRI-seq) across persistence models | Strong, direct for persister subtype |
| Maintenance | Tetracycline-mediated translation inhibition | clusters with / phenocopies | persister transcriptome | 10.1038/s41586-024-08124-2 (2024) | “Tetracycline-treated cells cluster with persister cells … implicating translational deficiency as a defining feature” (blattman2024identificationandgenetic pages 3-4) | *E. coli*; PETRI-seq after tetracycline | Strong for transcriptomic state; not equal to durable dormancy |
| Maintenance | hipA induction | leads to | high-level persister formation | 10.3390/antibiotics13090863 (2024) | “High-level persister formation and strong tolerance to ofloxacin were observed after high-level hipA induction” (dhaouadi2024persistenceandculturability pages 1-2) | *E. coli* BW25113/pRJW1; arabinose-inducible HipA, ofloxacin challenge | Strong, direct |
| Maintenance | hipA induction | decreases | culturability / increases deeper dormancy | 10.3390/antibiotics13090863 (2024) | “reduced culturability of E. coli and thus deeper dormancy under high-level hipA induction” (dhaouadi2024persistenceandculturability pages 1-2) | *E. coli*; persistence–culturability plot, CFU, counting chamber | Strong, direct but assay framework novel |
| Maintenance | hipA induction | decreases | cellular activity at PrrnBP1 | 10.3390/antibiotics13090863 (2024) | “controlled hipA induction led to decreased cellular activities at promoter PrrnBP1 and an increase in the non-culturable subpopulation” (dhaouadi2024persistenceandculturability pages 1-2) | *E. coli*; fluorescence imaging, flow cytometry | Strong, direct; promoter readout is assay-specific |
| Maintenance | HipA overexpression | causes | growth inhibition via glutamate starvation and stalled ribosomes | 10.3390/antibiotics13090863 (2024) | “ectopic expression of hipA in E. coli leads to significant growth inhibition due to glutamate starvation and stalled ribosomes” (dhaouadi2024persistenceandculturability pages 1-2) | *E. coli*; literature-grounded background in primary paper | Useful mechanistic link, but snippet cites prior work |
| Maintenance | Lon protease | contributes causally to | persister formation | 10.1038/s41586-024-08124-2 (2024) | “Among critical genes with large effects, we found lon” (blattman2024identificationandgenetic pages 1-2) | *E. coli*; ultra-dense CRISPRi across models | Strong causal genetics, but exact direction/effect size not in extracted snippet |
| Maintenance | YqgE | modulates | duration of post-starvation dormancy and persistence | 10.1038/s41586-024-08124-2 (2024) | “yqgE, a poorly characterized gene whose product strongly modulates the duration of post-starvation dormancy and persistence” (blattman2024identificationandgenetic pages 1-2) | *E. coli*; CRISPRi + single-cell atlas | Strong causal genetics; specific molecular function unresolved |
| Maintenance | Starvation for 6 days | increases occupancy of | persister cluster | 10.1038/s41586-024-08124-2 (2024) | “We next explored … we starved wild-type E. coli for 6 days, which increased the persistence rate … Remarkably, 7.4% of these cells were in the persister cluster” (blattman2024identificationandgenetic pages 3-4) | *E. coli*; PETRI-seq after prolonged starvation | Strong, direct for starvation-triggered persistence |
| Resuscitation | Rewetting / simulated rain | causes rapid resuscitation of | nearly all microbial populations | 10.1038/s41467-024-46920-6 (2024) | “nearly all microbial populations resuscitate within minutes after simulated rain” (imminger2024survivalandrapid pages 1-2) | Negev desert biocrust community; genome-resolved metatranscriptomics | Strong community-level edge; broad taxa |
| Resuscitation | Hydration (first 15 min) | changes transcription in | 85/96 populations | 10.1038/s41467-024-46920-6 (2024) | “85 out of 96 populations exhibited significant changes … within the first 15 min of hydration” (imminger2024survivalandrapid pages 3-4) | Biocrust metatranscriptomics | Strong quantitative community evidence |
| Resuscitation | Simulated rain / hydration | reactivates anabolic pathways in | majority of cells | 10.1038/s41467-024-46920-6 (2024) | “Within the first 3 h of hydration, 68.4% of the single cells were … active … reaching 91.0% after 12 h and 94.6 % after 24 h” (imminger2024survivalandrapid pages 2-3) | Biocrust single-cell NanoSIMS | Strong quantitative community evidence |
| Resuscitation | Resuscitated desert cells | exhibit limited productivity with | median replication times of 5.6–18.7 days | 10.1038/s41467-024-46920-6 (2024) | “median doubling time of 5.6 days” and “median doubling time increased to 18.7 days” (imminger2024survivalandrapid pages 3-4) | Biocrust single cells; inferred heterotrophic vs chemoautotrophic assumptions | Strong but model-dependent physiology assumptions |
| Resuscitation | ATP availability in ΔrfaL VBNC cells | promotes | resuscitation efficiency | 10.1016/j.jare.2023.08.002 (2024) | “DrfaL VBNC cells contained higher ATP levels, and ATP consumption during the resuscitating lag phase was highly correlated with resuscitation efficiency” (yang2024resuscitationofviable pages 1-2) | *E. coli* O157:H7; time-lapse, ATP measurements, mutant analysis | Strong, direct |
| Resuscitation | ATP | activates | Handler and salvage pathways for NAD+ synthesis | 10.1016/j.jare.2023.08.002 (2024) | “ATP was utilized to activate the Handler and salvage pathways to synthesize NAD+” (yang2024resuscitationofviable pages 1-2) | *E. coli* O157:H7; metabolomics, NAD(H), ATP assays | Strong, direct |
| Resuscitation | NAD+ synthesis | recovers/promotes | metabolic activity and exit from dormancy | 10.1016/j.jare.2023.08.002 (2024) | “using residual ATP to primarily recover metabolic activity, driving cells to exit dormancy” (yang2024resuscitationofviable pages 1-2) | *E. coli* O157:H7 VBNC resuscitation | Strong, direct |
| Resuscitation | rfaL deletion (O-antigen ligase loss) | shortens | resuscitating lag phase | 10.1016/j.jare.2023.08.002 (2024) | “Mutation of rfaL … markedly shortened the resuscitating lag phase” (yang2024resuscitationofviable pages 1-2) | *E. coli* O157:H7; mutant vs WT | Strong, direct; gene-specific inhibitor of resuscitation |
| Resuscitation | Rpf proteins | reactivate | dormant bacteria at very low concentration | 10.1007/s00018-006-6188-2 (2006); 10.3390/microorganisms12081528 (2024 review) | “Proteins containing the Rpf domain are able to reactivate dormant bacteria at very low concentration” (li2024resuscitationpromotionfactor pages 1-3) | High-G+C Actinobacteria, esp. *Micrococcus*, *Mycobacterium*; review/foundation | Foundational, not from 2024 primary experiment |
| Resuscitation | Rpf family | possesses | peptidoglycan hydrolase / lysozyme-like activity | 10.3390/microorganisms12081528 (2024); 10.1074/jbc.RA120.013994 (2020); 10.1007/s00018-006-6188-2 (2006) | “Rpf proteins are known to be peptidoglycan glycosidases” and “the Rpfs function as endo-acting lytic transglycosylases” (keep2006bacterialresuscitationfactors pages 1-2, sexton2020rolesoflysm pages 1-2) | Actinobacteria reviews and biochemical assays in *Streptomyces* | Strong biochemical support; taxon scope mostly actinobacterial |
| Resuscitation | LysM/LytM domains in Rpf proteins | enhance | Rpf enzyme activity / peptidoglycan binding | 10.1074/jbc.RA120.013994 (2020) | “their LysM and LytM domains enhance Rpf enzyme activity” and “promoted peptidoglycan binding” (sexton2020rolesoflysm pages 1-2) | *Streptomyces* Rpfs; mutagenesis + cleavage assay | Strong but not universal across all Rpfs |
| Resuscitation | Passage in chicken embryos | restores | walled, virulent state from VBNC | 10.1038/s41467-024-52633-7 (2024) | “VBNC Listeria revert to a walled and virulent state after passage in chicken embryos” (carvalho2024aquaticenvironmentdrives pages 1-2) | *L. monocytogenes*; embryo passage assay | Strong, direct resuscitation/virulence-restoration edge |
| Resuscitation | Modified Schneider’s medium + 10% defibrinated sheep blood | resuscitates | VBNC *B. henselae* | 10.3389/fcimb.2024.1486426 (2024) | “Successful resuscitation confirmed the VBNC state” and resuscitation used “modified Schneider’s medium with 10% defibrinated sheep blood” (gou2024viablebutnonculturable pages 1-2, gou2024viablebutnonculturable pages 2-3) | *B. henselae*; medium-based resuscitation assay | Strong assay-specific edge |
| Boundary / caution | VBNC state | is distinct from | persister state | 10.3390/antibiotics13090863 (2024) | “Persister cells can regrow after the stressor is removed. In contrast, VBNCs have lost culturability in the original medium” (dhaouadi2024persistenceandculturability pages 1-2) | Conceptual distinction in *E. coli* dormancy study | Useful scope boundary; not a causal edge |
| Boundary / caution | Dormancy umbrella trait | includes overlapping forms such as | persisters and VBNC | 10.1074/jbc.RA120.013994 (2020); 10.3390/antibiotics13090863 (2024) | “These non-replicating states include everything from persister cells and viable but not culturable (VBNC) bacteria” (sexton2020rolesoflysm pages 1-2) | Review/background across bacteria | Scope statement; curate as ontology note rather than mechanism |


*Table: This table organizes source-backed causal graph edges for microbial dormancy across induction, maintenance, and resuscitation phases. It is designed for TraitMech curation, with direct evidence snippets, DOI-first references, and notes on taxon specificity and uncertainty.*

**Key quantitative findings embedded in the artifact include:**

- Desert biocrust rewetting: 68.4% of cells anabolically active within 3 h, rising to 91.0% by 12 h and 94.6% by 24 h (imminger2024survivalandrapid pages 2-3); median replication times of 5.6–18.7 days despite rapid transcriptional resuscitation (imminger2024survivalandrapid pages 3-4).
- *B. henselae* VBNC induction: 19 days at 38.8°C or 4 days with bactericidal antibiotics (gou2024viablebutnonculturable pages 1-2).
- *E. coli* persister atlas: 7.4% of 6-day-starved wild-type cells occupy the persister cluster; translational deficiency is the dominant transcriptomic signature (blattman2024identificationandgenetic pages 3-4).
- Rpf activity: Enhances germination/resuscitation at picomolar concentrations; LysM and LytM domains boost activity 65–70% and 30% respectively (sexton2020rolesoflysm pages 1-2).

---

## 4. Ontology Grounding and Suggested CURIEs

Where stable identifiers are available, suggested CURIEs are provided in Section 2. Key examples:

- **Genes/proteins**: Use UniProt IDs for model organisms (*E. coli* K-12, *B. subtilis*); otherwise label-only until orthologs are confirmed.
- **Chemicals**: CHEBI:15422 (ATP), CHEBI:57540 (NAD+), CHEBI:8005 (peptidoglycan), CHEBI:33281 (antibacterial agent).
- **GO terms**: GO:0006412 (translation), GO:0006302 (double-strand break repair), GO:0009435 (NAD biosynthetic process via nicotinate), GO:0008933 (lytic transglycosylase activity), GO:0009274 (peptidoglycan-based cell wall).
- **Environmental ontology**: ENVO:00002006 (water), ENVO:00002042 (precipitation).
- **Phenotype/quality**: PATO:0000146 (temperature), PATO:0001546 (rigidity).
- **Pfam domains**: PF06737 (Rpf), PF01476 (LysM), PF01551 (LytM).

**Label-only candidates** (pending stable IDs or broader confirmation):

- **YqgE**: Function not yet annotated; conserved in enterobacteria but no ontology consensus.
- **SigB**, **NamA**: Genus-specific regulators/enzymes; consider NCBITaxon:1637 (*Listeria*) qualifier.

---

## 5. Current Applications and Real-World Implementations

### Public Health and Food Safety

- **Resuscitation risk**: VBNC pathogens (*L. monocytogenes*, *B. henselae*, *Vibrio*, *E. coli* O157:H7) pose diagnostic and outbreak challenges because standard culture-based detection underestimates viable cell counts (carvalho2024aquaticenvironmentdrives pages 1-2, yang2024resuscitationofviable pages 1-2, gou2024viablebutnonculturable pages 1-2). Successful resuscitation after passage in chicken embryos (*L. monocytogenes*) or modified media (*B. henselae*) confirms virulence restoration risk (carvalho2024aquaticenvironmentdrives pages 1-2, gou2024viablebutnonculturable pages 2-3, gou2024viablebutnonculturable pages 1-2).
- **Antibiotic tolerance**: Persisters and VBNC cells tolerate lethal antibiotic concentrations, contributing to chronic/recurrent infections; *B. henselae* VBNC cells demonstrated "greater drug tolerance than cells in the stationary phase" (gou2024viablebutnonculturable pages 1-2). HipA7 mutant *E. coli* clinical isolates occur in ~5% of uropathogenic samples (blattman2024identificationandgenetic pages 1-2).
- **Blood-culture-negative endocarditis (BCNE)**: *B. henselae* VBNC state complicates diagnosis; shell-vial culture methods improve recovery to 44% vs. 4% direct culture, suggesting VBNC-like phenomena (gou2024viablebutnonculturable pages 1-2).

### Ecosystem Ecology

- **Dryland carbon cycling**: Desert biocrusts cover ~12% of the global terrestrial surface; microbial activity confined to short rain events (~few days/year), yet communities maintain ecosystem processes via rapid resuscitation and high persistence (limited productivity: median replication 6–19 days) (imminger2024survivalandrapid pages 1-2, imminger2024survivalandrapid pages 2-3, imminger2024survivalandrapid pages 3-4).
- **Seed-bank hypothesis**: Dormancy enables long-term genetic storage in environmental reservoirs, influencing population dynamics and resilience (keep2006bacterialresuscitationfactors pages 1-2).

### Antimicrobial Strategy Development

- **Targeting resuscitation pathways**: Blocking ATP→NAD+ synthesis or Rpf activity could prevent VBNC resuscitation and reduce relapse risk (yang2024resuscitationofviable pages 1-2, yang2024resuscitationofviable pages 2-4). Small-molecule (p)ppGpp analogs and Rpf inhibitors are under investigation (referenced in background literature).
- **Diagnostic improvements**: PMA-qPCR and SYBR Green I/PI viability staining distinguish live VBNC cells from dead cells, improving detection over CFU counts alone (gou2024viablebutnonculturable pages 2-3, gou2024viablebutnonculturable pages 1-2).

---

## 6. Recent Research Highlights and Statistics (2023–2024 Sources)

### 2024 Primary Study Highlights

1. **Carvalho *et al.*, *Nature Communications*, October 2024** (DOI: 10.1038/s41467-024-52633-7; URL: https://doi.org/10.1038/s41467-024-52633-7)  
   *L. monocytogenes* transitions to VBNC via osmotically stable cell-wall-deficient coccoid forms after starvation in mineral water. SigB and NamA identified as major regulators. Resuscitation confirmed via chicken embryo passage, restoring walled, virulent state (carvalho2024aquaticenvironmentdrives pages 3-4, carvalho2024aquaticenvironmentdrives pages 1-2, carvalho2024aquaticenvironmentdrives pages 2-3).

2. **Blattman *et al.*, *Nature*, November 2024** (DOI: 10.1038/s41586-024-08124-2; URL: https://doi.org/10.1038/s41586-024-08124-2)  
   High-resolution single-cell RNA atlas of *E. coli* growth transitions via PETRI-seq. Persisters from diverse models converge to a translational-deficiency state distinct from all growth phases. Lon protease and YqgE identified via genome-wide CRISPRi as critical modulators; YqgE "strongly modulates the duration of post-starvation dormancy and persistence" (blattman2024identificationandgenetic pages 2-3, blattman2024identificationandgenetic pages 1-2, blattman2024identificationandgenetic pages 3-4, blattman2024identificationandgenetic pages 4-5).

3. **Yang *et al.*, *Journal of Advanced Research*, June 2024** (DOI: 10.1016/j.jare.2023.08.002; URL: https://doi.org/10.1016/j.jare.2023.08.002)  
   *E. coli* O157:H7 VBNC resuscitation promoted by ATP-mediated NAD+ synthesis. Deletion of *rfaL* (O-antigen ligase) shortens lag phase by freeing ATP from LPS biosynthesis; metabolomics confirms ATP activates Handler and salvage pathways (yang2024resuscitationofviable pages 1-2, yang2024resuscitationofviable pages 2-4).

4. **Imminger *et al.*, *Nature Communications*, April 2024** (DOI: 10.1038/s41467-024-46920-6; URL: https://doi.org/10.1038/s41467-024-46920-6)  
   Negev Desert biocrust microbes: nearly universal resuscitation within minutes of simulated rain (85/96 populations show differential gene expression by 15 min; 91% of single cells anabolically active by 12 h), but median replication times 6–19 days. Community optimizes short activity windows via "fast and universal resuscitation enabling the maintenance of key ecosystem functions" (imminger2024survivalandrapid pages 1-2, imminger2024survivalandrapid pages 2-3, imminger2024survivalandrapid pages 3-4).

5. **Gou *et al.*, *Frontiers in Cellular and Infection Microbiology*, November 2024** (DOI: 10.3389/fcimb.2024.1486426; URL: https://doi.org/10.3389/fcimb.2024.1486426)  
   *B. henselae* enters VBNC state after 19 days at 38.8°C or 4 days of antibiotic treatment. Resuscitation confirmed in modified Schneider's medium + 10% defibrinated sheep blood. Proteomic analysis: upregulation of stress-resistance and host-invasion proteins; VBNC cells show "greater drug tolerance than cells in the stationary phase" (gou2024viablebutnonculturable pages 2-3, gou2024viablebutnonculturable pages 1-2).

6. **Dhaouadi *et al.*, *Antibiotics*, September 2024** (DOI: 10.3390/antibiotics13090863; URL: https://doi.org/10.3390/antibiotics13090863)  
   Dose- and time-dependent dormancy in *E. coli* via arabinose-induced HipA toxin expression. Novel persistence–culturability plot reveals deeper dormancy (increased VBNC-like subpopulation) under high-level induction (dhaouadi2024persistenceandculturability pages 1-2, dhaouadi2024persistenceandculturability pages 2-4).

### 2024 Review and Mechanistic Summary Articles

7. **Li *et al.*, *Microorganisms*, July 2024** (DOI: 10.3390/microorganisms12081528; URL: https://doi.org/10.3390/microorganisms12081528)  
   Comprehensive review of Rpf distribution, mode of action, and functional mechanisms across bacterial species. Rpfs possess peptidoglycan hydrolase activities; applications in increasing bacterial diversity and isolating functional species (li2024resuscitationpromotionfactor pages 3-6, li2024resuscitationpromotionfactor pages 1-3).

8. **Niu *et al.*, *Signal Transduction and Targeted Therapy*, July 2024** (DOI: 10.1038/s41392-024-01866-5; URL: https://doi.org/10.1038/s41392-024-01866-5)  
   Review: Bacterial persisters—molecular mechanisms and therapeutic development. Summarizes HipA, Lon, stringent response, and biofilm tolerance; emphasizes need for anti-persister compounds (dhaouadi2024persistenceandculturability pages 15-16, yang2024resuscitationofviable pages 13-13).

### Additional Recent Perspectives

- **McDonald *et al.*, *Trends in Microbiology*, February 2024** (DOI: 10.1016/j.tim.2023.08.006): "What is microbial dormancy?" — addresses definitional challenges and proposes unifying frameworks (unobtainable but title/abstract relevant).
- **Liu *et al.*, *The ISME Journal*, 2024** (DOI: 10.1093/ismejo/wrae179): Microbial community coalescence and dormancy as "seed bank" for resuscitation of inactive resident species (carvalho2024aquaticenvironmentdrives pages 15-16).

---

## 7. Warnings and Claims Unsuitable for TraitMech Curation

### Taxon-Specific Edges — Do Not Generalize

- **SigB, NamA**: Evidence is specific to *Listeria monocytogenes*. Do not assume these exact regulators control dormancy in other genera without ortholog confirmation and functional assays.
- **RfaL**: *E. coli* O157:H7-specific VBNC resuscitation regulator; effect is mediated by LPS biosynthesis pathway diversion, which is not universal.
- **HipA, Lon, YqgE**: Genetic evidence is from *E. coli* K-12 or closely related strains. HipA7 mutation occurs in some clinical isolates, but prevalence and conservation vary.
- **Rpf family**: Well-characterized in Actinobacteria (*Micrococcus*, *Mycobacterium*, *Streptomyces*); limited data in other phyla.

### Correlative or Marker Findings — Not Causal Without Further Validation

- **Low ATP levels**: Consistently observed in dormancy but may be a consequence rather than a driver. Experimental ATP depletion/replenishment studies are needed to confirm causality.
- **Translational deficiency**: Dominant *transcriptomic* signature of persisters, but tetracycline-induced translation inhibition does not produce durable dormancy equal to self-maintained persistence (blattman2024identificationandgenetic pages 3-4). Mark as marker/phenotype, not universal causal driver.
- **Reduced membrane fluidity**: Observed in *L. monocytogenes* VBNC cells prior to cell-wall loss; may be adaptation rather than trigger.

### Assay-Dependent or Experimental Artifacts

- **Culturability vs. viability**: CFU counts alone cannot distinguish VBNC from dead cells. Flow cytometry (CFDA, Live/Dead, SYBR Green I/PI) and PMA-qPCR improve viability assessment, but no single assay is definitive. Resuscitation assays are the gold standard but may be media/condition-specific.
- **Persistence–culturability plot**: Novel framework introduced by Dhaouadi *et al.* (2024); provides nuanced view of dormancy depth but interpretation depends on assumptions about VBNC vs. persister vs. dead-cell proportions (dhaouadi2024persistenceandculturability pages 1-2, dhaouadi2024persistenceandculturability pages 2-4).
- **High-pressure CO2 (HPCD)**: Useful experimental inducer but not an ecologically relevant stressor; do not assume HPCD-induced VBNC mechanisms generalize to natural starvation or temperature stress.

### Mechanistic Gaps and Unresolved Questions

- **Rpf signaling vs. structural function**: Debate persists. Sexton *et al.* (2020) argue for structural cell-wall remodeling in *Streptomyces* rather than muropeptide signaling, as germination could not be stimulated by known germinants and Rpf activity is independent of peptidoglycan-responsive Ser/Thr kinases (sexton2020rolesoflysm pages 1-2). Contrast with *Bacillus* PrkC–muropeptide signaling model. Do not universalize either mechanism.
- **YqgE molecular function**: CRISPRi identifies strong effect on dormancy duration, but protein function is uncharacterized. Tentatively label as dormancy-modulating factor pending biochemical studies.
- **Community resuscitation mechanisms**: Desert biocrust data show rapid, near-universal transcriptional resuscitation (imminger2024survivalandrapid pages 1-2, imminger2024survivalandrapid pages 3-4), but the underlying single-cell triggers (e.g., water potential, osmoprotectant dilution, redox shift) are not mechanistically resolved. Do not assume a single molecular switch.

### Do Not Equate Dormancy Subtypes

- **VBNC ≠ persister ≠ endospore ≠ stationary phase**: Operational definitions differ by culturability, resuscitation requirements, and physiological state. Use appropriate taxon/assay qualifiers. "There is a continuum between active cells and cell death, with VBNCs being at a deeper state of dormancy than persister cells" (dhaouadi2024persistenceandculturability pages 1-2), but this does not imply mechanistic identity.

---

## 8. DOI-First Bibliography

### Primary 2024 Studies

1. Carvalho, F., Carreaux, A., Sartori-Rupp, A., *et al.* (2024). Aquatic environment drives the emergence of cell wall-deficient dormant forms in *Listeria*. *Nature Communications*, 15:8499. DOI: [10.1038/s41467-024-52633-7](https://doi.org/10.1038/s41467-024-52633-7). Published October 2024.

2. Blattman, S. B., Jiang, W., McGarrigle, E. R., Liu, M., Oikonomou, P., & Tavazoie, S. (2024). Identification and genetic dissection of convergent persister cell states. *Nature*, 636:438-446. DOI: [10.1038/s41586-024-08124-2](https://doi.org/10.1038/s41586-024-08124-2). Published November 2024.

3. Yang, D., Wang, W., Zhao, L., Rao, L., & Liao, X. (2024). Resuscitation of viable but nonculturable bacteria promoted by ATP-mediated NAD+ synthesis. *Journal of Advanced Research*, 60:27-39. DOI: [10.1016/j.jare.2023.08.002](https://doi.org/10.1016/j.jare.2023.08.002). Published June 2024.

4. Imminger, S., Meier, D. V., Schintlmeister, A., *et al.* (2024). Survival and rapid resuscitation permit limited productivity in desert microbial communities. *Nature Communications*, 15:3056. DOI: [10.1038/s41467-024-46920-6](https://doi.org/10.1038/s41467-024-46920-6). Published April 2024.

5. Gou, Y., Liu, D., Xin, Y., *et al.* (2024). Viable but nonculturable state in the zoonotic pathogen *Bartonella henselae* induced by low-grade fever temperature and antibiotic treatment. *Frontiers in Cellular and Infection Microbiology*, 14:1486426. DOI: [10.3389/fcimb.2024.1486426](https://doi.org/10.3389/fcimb.2024.1486426). Published November 2024.

6. Dhaouadi, Y., Hashemi, M. J., & Ren, D. (2024). Persistence and culturability of *Escherichia coli* under induced toxin expression. *Antibiotics*, 13(9):863. DOI: [10.3390/antibiotics13090863](https://doi.org/10.3390/antibiotics13090863). Published September 2024.

7. Li, X., Ren, Q., Sun, Z., Wu, Y., & Pan, H. (2024). Resuscitation promotion factor: A pronounced bacterial cytokine in propelling bacterial resuscitation. *Microorganisms*, 12(8):1528. DOI: [10.3390/microorganisms12081528](https://doi.org/10.3390/microorganisms12081528). Published July 2024.

8. Niu, H., Gu, J., & Zhang, Y. (2024). Bacterial persisters: molecular mechanisms and therapeutic development. *Signal Transduction and Targeted Therapy*, 9:186. DOI: [10.1038/s41392-024-01866-5](https://doi.org/10.1038/s41392-024-01866-5). Published July 2024.

9. Yuan, S., Shen, Y., Quan, Y., *et al.* (2024). Molecular mechanism and application of emerging technologies in study of bacterial persisters. *BMC Microbiology*, 24:478. DOI: [10.1186/s12866-024-03628-3](https://doi.org/10.1186/s12866-024-03628-3). Published November 2024.

10. Liu, X. & Salles, J. F. (2024). Drivers and consequences of microbial community coalescence. *The ISME Journal*, 18:wrae179. DOI: [10.1093/ismejo/wrae179](https://doi.org/10.1093/ismejo/wrae179). Published 2024.

### Foundational and Recent Mechanistic Studies

11. Sexton, D. L., Herlihey, F. A., Brott, A. S., *et al.* (2020). Roles of LysM and LytM domains in resuscitation-promoting factor (Rpf) activity and Rpf-mediated peptidoglycan cleavage and dormant spore reactivation. *Journal of Biological Chemistry*, 295(27):9171-9182. DOI: [10.1074/jbc.ra120.013994](https://doi.org/10.1074/jbc.ra120.013994). Published July 2020.

12. Keep, N. H., Ward, J. M., Robertson, G., Cohen-Gonsaud, M., & Henderson, B. (2006). Bacterial resuscitation factors: revival of viable but non-culturable bacteria. *Cellular and Molecular Life Sciences CMLS*, 63:2555-2559. DOI: [10.1007/s00018-006-6188-2](https://doi.org/10.1007/s00018-006-6188-2). Published September 2006.

13. Pan, H. & Ren, Q. (2022). Wake up! Resuscitation of viable but nonculturable bacteria: Mechanism and potential application. *Foods*, 12(1):82. DOI: [10.3390/foods12010082](https://doi.org/10.3390/foods12010082). Published December 2022.

14. Gupta, R. Kr. & Srivastava, R. (2012). Resuscitation promoting factors: a family of microbial proteins in survival and resuscitation of dormant mycobacteria. *Indian Journal of Microbiology*, 52(2):114-121. DOI: [10.1007/s12088-011-0202-6](https://doi.org/10.1007/s12088-011-0202-6). Published August 2012.

15. den Bergh, B. V., Fauvart, M., & Michiels, J. (2017). Formation, physiology, ecology, evolution and clinical importance of bacterial persisters. *FEMS Microbiology Reviews*, 41(3):219-251. DOI: [10.1093/femsre/fux001](https://doi.org/10.1093/femsre/fux001). Published May 2017.

16. Bergkessel, M., Basta, D. W., & Newman, D. K. (2016). The physiology of growth arrest: uniting molecular and environmental microbiology. *Nature Reviews Microbiology*, 14(9):549-562. DOI: [10.1038/nrmicro.2016.107](https://doi.org/10.1038/nrmicro.2016.107). Published August 2016.

17. Kundra, S., Colomer-Winter, C., & Lemos, J. A. (2020). Survival of the fittest: The relationship of (p)ppGpp with bacterial virulence. *Frontiers in Microbiology*, 11:601417. DOI: [10.3389/fmicb.2020.601417](https://doi.org/10.3389/fmicb.2020.601417). Published December 2020.

18. Salina, E. G. & Makarov, V. (2022). *Mycobacterium tuberculosis* dormancy: How to fight a hidden danger. *Microorganisms*, 10(12):2334. DOI: [10.3390/microorganisms10122334](https://doi.org/10.3390/microorganisms10122334). Published November 2022.

19. Gengenbacher, M. & Kaufmann, S. H. E. (2012). *Mycobacterium tuberculosis*: success through dormancy. *FEMS Microbiology Reviews*, 36(3):514-532. DOI: [10.1111/j.1574-6976.2012.00331.x](https://doi.org/10.1111/j.1574-6976.2012.00331.x). Published May 2012.

20. Stewart, P. S., White, B., Boegli, L., *et al.* (2019). Conceptual model of biofilm antibiotic tolerance that integrates phenomena of diffusion, metabolism, gene expression, and physiology. *Journal of Bacteriology*, 201(22):e00307-19. DOI: [10.1128/jb.00307-19](https://doi.org/10.1128/jb.00307-19). Published November 2019.

---

## Contact and Next Steps

This report synthesizes 2024 primary experimental data and foundational mechanistic studies to provide TraitMech curators with source-backed, taxon-qualified causal edges for the dormancy graph. All major claims are linked to DOI references, publication dates, and supporting snippets. Curators should:

1. **Prioritize direct genetic/biochemical edges** from 2024 primary studies (Carvalho, Blattman, Yang, Imminger, Gou, Dhaouadi).
2. **Apply taxon and assay qualifiers** to all edges; do not universalize findings without cross-species validation.
3. **Use label-only nodes** for poorly characterized factors (YqgE) and mark for future ontology updates.
4. **Flag review-derived or correlative claims** for lower curation priority pending experimental confirmation.
5. **Consult the causal-edge artifact table** (artifact-00) for ready-to-curate triples with all required metadata.

For questions, refer to the cited DOIs and context IDs (keep2006bacterialresuscitationfactors pages 1-2, gou2024viablebutnonculturable pages 1-2) in the evidence base.

References

1. (carvalho2024aquaticenvironmentdrives pages 1-2): Filipe Carvalho, Alexis Carreaux, Anna Sartori-Rupp, Stéphane Tachon, Anastasia D. Gazi, Pascal Courtin, Pierre Nicolas, Florence Dubois-Brissonnet, Aurélien Barbotin, Emma Desgranges, Matthieu Bertrand, Karine Gloux, Catherine Schouler, Rut Carballido-López, Marie-Pierre Chapot-Chartier, Eliane Milohanic, Hélène Bierne, and Alessandro Pagliuso. Aquatic environment drives the emergence of cell wall-deficient dormant forms in listeria. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52633-7, doi:10.1038/s41467-024-52633-7. This article has 28 citations and is from a highest quality peer-reviewed journal.

2. (blattman2024identificationandgenetic pages 1-2): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636:438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 45 citations and is from a highest quality peer-reviewed journal.

3. (yang2024resuscitationofviable pages 1-2): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

4. (imminger2024survivalandrapid pages 1-2): Stefanie Imminger, Dimitri V. Meier, Arno Schintlmeister, Anton Legin, Jörg Schnecker, Andreas Richter, Osnat Gillor, Stephanie A. Eichorst, and Dagmar Woebken. Survival and rapid resuscitation permit limited productivity in desert microbial communities. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46920-6, doi:10.1038/s41467-024-46920-6. This article has 52 citations and is from a highest quality peer-reviewed journal.

5. (gou2024viablebutnonculturable pages 1-2): Yu-Ping Gou, Dongxia Liu, Yuxian Xin, Ting Wang, Jiaxing Li, Yiwen Xi, Xiaoling Zheng, Tuanjie Che, Ying Zhang, Tingting Li, and Jie Feng. Viable but nonculturable state in the zoonotic pathogen bartonella henselae induced by low-grade fever temperature and antibiotic treatment. Frontiers in Cellular and Infection Microbiology, Nov 2024. URL: https://doi.org/10.3389/fcimb.2024.1486426, doi:10.3389/fcimb.2024.1486426. This article has 5 citations.

6. (keep2006bacterialresuscitationfactors pages 1-2): N. H. Keep, J. M. Ward, G. Robertson, M. Cohen-Gonsaud, and B. Henderson. Bacterial resuscitation factors: revival of viable but non-culturable bacteria. Cellular and Molecular Life Sciences CMLS, 63:2555-2559, Sep 2006. URL: https://doi.org/10.1007/s00018-006-6188-2, doi:10.1007/s00018-006-6188-2. This article has 60 citations.

7. (sexton2020rolesoflysm pages 1-2): Danielle L. Sexton, Francesca A. Herlihey, Ashley S. Brott, David A. Crisante, Evan Shepherdson, Anthony J. Clarke, and Marie A. Elliot. Roles of lysm and lytm domains in resuscitation-promoting factor (rpf) activity and rpf-mediated peptidoglycan cleavage and dormant spore reactivation. Journal of Biological Chemistry, 295:9171-9182, Jul 2020. URL: https://doi.org/10.1074/jbc.ra120.013994, doi:10.1074/jbc.ra120.013994. This article has 33 citations and is from a domain leading peer-reviewed journal.

8. (dhaouadi2024persistenceandculturability pages 1-2): Yousr Dhaouadi, Mohamad Javad Hashemi, and Dacheng Ren. Persistence and culturability of escherichia coli under induced toxin expression. Sep 2024. URL: https://doi.org/10.3390/antibiotics13090863, doi:10.3390/antibiotics13090863. This article has 4 citations.

9. (blattman2024identificationandgenetic pages 3-4): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636:438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 45 citations and is from a highest quality peer-reviewed journal.

10. (li2024resuscitationpromotionfactor pages 1-3): Xinxin Li, Qing Ren, Zhanbin Sun, Yanan Wu, and Hanxu Pan. Resuscitation promotion factor: a pronounced bacterial cytokine in propelling bacterial resuscitation. Microorganisms, 12:1528, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081528, doi:10.3390/microorganisms12081528. This article has 10 citations.

11. (carvalho2024aquaticenvironmentdrives pages 2-3): Filipe Carvalho, Alexis Carreaux, Anna Sartori-Rupp, Stéphane Tachon, Anastasia D. Gazi, Pascal Courtin, Pierre Nicolas, Florence Dubois-Brissonnet, Aurélien Barbotin, Emma Desgranges, Matthieu Bertrand, Karine Gloux, Catherine Schouler, Rut Carballido-López, Marie-Pierre Chapot-Chartier, Eliane Milohanic, Hélène Bierne, and Alessandro Pagliuso. Aquatic environment drives the emergence of cell wall-deficient dormant forms in listeria. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52633-7, doi:10.1038/s41467-024-52633-7. This article has 28 citations and is from a highest quality peer-reviewed journal.

12. (yang2024resuscitationofviable pages 2-4): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

13. (sexton2020rolesoflysm pages 10-11): Danielle L. Sexton, Francesca A. Herlihey, Ashley S. Brott, David A. Crisante, Evan Shepherdson, Anthony J. Clarke, and Marie A. Elliot. Roles of lysm and lytm domains in resuscitation-promoting factor (rpf) activity and rpf-mediated peptidoglycan cleavage and dormant spore reactivation. Journal of Biological Chemistry, 295:9171-9182, Jul 2020. URL: https://doi.org/10.1074/jbc.ra120.013994, doi:10.1074/jbc.ra120.013994. This article has 33 citations and is from a domain leading peer-reviewed journal.

14. (imminger2024survivalandrapid pages 2-3): Stefanie Imminger, Dimitri V. Meier, Arno Schintlmeister, Anton Legin, Jörg Schnecker, Andreas Richter, Osnat Gillor, Stephanie A. Eichorst, and Dagmar Woebken. Survival and rapid resuscitation permit limited productivity in desert microbial communities. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46920-6, doi:10.1038/s41467-024-46920-6. This article has 52 citations and is from a highest quality peer-reviewed journal.

15. (imminger2024survivalandrapid pages 3-4): Stefanie Imminger, Dimitri V. Meier, Arno Schintlmeister, Anton Legin, Jörg Schnecker, Andreas Richter, Osnat Gillor, Stephanie A. Eichorst, and Dagmar Woebken. Survival and rapid resuscitation permit limited productivity in desert microbial communities. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46920-6, doi:10.1038/s41467-024-46920-6. This article has 52 citations and is from a highest quality peer-reviewed journal.

16. (carvalho2024aquaticenvironmentdrives pages 3-4): Filipe Carvalho, Alexis Carreaux, Anna Sartori-Rupp, Stéphane Tachon, Anastasia D. Gazi, Pascal Courtin, Pierre Nicolas, Florence Dubois-Brissonnet, Aurélien Barbotin, Emma Desgranges, Matthieu Bertrand, Karine Gloux, Catherine Schouler, Rut Carballido-López, Marie-Pierre Chapot-Chartier, Eliane Milohanic, Hélène Bierne, and Alessandro Pagliuso. Aquatic environment drives the emergence of cell wall-deficient dormant forms in listeria. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52633-7, doi:10.1038/s41467-024-52633-7. This article has 28 citations and is from a highest quality peer-reviewed journal.

17. (gou2024viablebutnonculturable pages 2-3): Yu-Ping Gou, Dongxia Liu, Yuxian Xin, Ting Wang, Jiaxing Li, Yiwen Xi, Xiaoling Zheng, Tuanjie Che, Ying Zhang, Tingting Li, and Jie Feng. Viable but nonculturable state in the zoonotic pathogen bartonella henselae induced by low-grade fever temperature and antibiotic treatment. Frontiers in Cellular and Infection Microbiology, Nov 2024. URL: https://doi.org/10.3389/fcimb.2024.1486426, doi:10.3389/fcimb.2024.1486426. This article has 5 citations.

18. (blattman2024identificationandgenetic pages 2-3): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636:438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 45 citations and is from a highest quality peer-reviewed journal.

19. (blattman2024identificationandgenetic pages 4-5): Sydney B. Blattman, Wenyan Jiang, E. Riley McGarrigle, Menghan Liu, Panos Oikonomou, and Saeed Tavazoie. Identification and genetic dissection of convergent persister cell states. Nature, 636:438-446, Nov 2024. URL: https://doi.org/10.1038/s41586-024-08124-2, doi:10.1038/s41586-024-08124-2. This article has 45 citations and is from a highest quality peer-reviewed journal.

20. (dhaouadi2024persistenceandculturability pages 2-4): Yousr Dhaouadi, Mohamad Javad Hashemi, and Dacheng Ren. Persistence and culturability of escherichia coli under induced toxin expression. Sep 2024. URL: https://doi.org/10.3390/antibiotics13090863, doi:10.3390/antibiotics13090863. This article has 4 citations.

21. (li2024resuscitationpromotionfactor pages 3-6): Xinxin Li, Qing Ren, Zhanbin Sun, Yanan Wu, and Hanxu Pan. Resuscitation promotion factor: a pronounced bacterial cytokine in propelling bacterial resuscitation. Microorganisms, 12:1528, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081528, doi:10.3390/microorganisms12081528. This article has 10 citations.

22. (dhaouadi2024persistenceandculturability pages 15-16): Yousr Dhaouadi, Mohamad Javad Hashemi, and Dacheng Ren. Persistence and culturability of escherichia coli under induced toxin expression. Sep 2024. URL: https://doi.org/10.3390/antibiotics13090863, doi:10.3390/antibiotics13090863. This article has 4 citations.

23. (yang2024resuscitationofviable pages 13-13): Dong Yang, Wenxin Wang, Liang Zhao, Lei Rao, and Xiaojun Liao. Resuscitation of viable but nonculturable bacteria promoted by atp-mediated nad+ synthesis. Jun 2024. URL: https://doi.org/10.1016/j.jare.2023.08.002, doi:10.1016/j.jare.2023.08.002. This article has 31 citations and is from a peer-reviewed journal.

24. (carvalho2024aquaticenvironmentdrives pages 15-16): Filipe Carvalho, Alexis Carreaux, Anna Sartori-Rupp, Stéphane Tachon, Anastasia D. Gazi, Pascal Courtin, Pierre Nicolas, Florence Dubois-Brissonnet, Aurélien Barbotin, Emma Desgranges, Matthieu Bertrand, Karine Gloux, Catherine Schouler, Rut Carballido-López, Marie-Pierre Chapot-Chartier, Eliane Milohanic, Hélène Bierne, and Alessandro Pagliuso. Aquatic environment drives the emergence of cell wall-deficient dormant forms in listeria. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52633-7, doi:10.1038/s41467-024-52633-7. This article has 28 citations and is from a highest quality peer-reviewed journal.